#!/usr/bin/env python3
"""Reject vault writes that introduce a type, tag, status, or property the vault does not already use.

Usage: python3 vault-check.py [--vault DIR] [files...]
--vault defaults to $VAULT, else the nearest parent folder containing AGENTS.md, else the current folder.
With no files, checks every modified or new .md file per git status.
Prints the offenders and exits 1 when something new appears. Skips hidden folders and any folder named Journal."""
import os,re,subprocess,sys,glob
args=sys.argv[1:]
V=None
if '--vault' in args:
    i=args.index('--vault'); V=os.path.abspath(args[i+1]); del args[i:i+2]
if not V: V=os.environ.get('VAULT')
if not V:
    d=os.getcwd()
    while d!=os.path.dirname(d):
        if os.path.exists(os.path.join(d,'AGENTS.md')): V=d; break
        d=os.path.dirname(d)
    V=V or os.getcwd()
def fm(path):
    try: t=open(path,errors='ignore').read()
    except: return {}
    m=re.match(r'^---\n(.*?)\n---',t,re.S)
    if not m: return {}
    out={};key=None
    for l in m.group(1).splitlines():
        km=re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$',l)
        if km:
            key=km.group(1); v=km.group(2).strip(); out.setdefault(key,[])
            if v and v not in('|','>'): out[key].append(v.strip('"\''))
        elif key and re.match(r'^\s*-\s+',l): out[key].append(re.sub(r'^\s*-\s+','',l).strip().strip('"\''))
    return out
def skip(p): return '/.' in p or '/Journal' in p or '/03 - Journal/' in p
def changed():
    r=subprocess.run(['git','-C',V,'status','--porcelain'],capture_output=True,text=True).stdout
    return [os.path.join(V,l[3:].strip().strip('"')) for l in r.splitlines() if l[:2].strip() in('M','A','??','AM','MM') and l.strip().endswith('.md')]
files=[os.path.abspath(f) for f in args] or changed()
if not files: print("vault-check: nothing to check"); sys.exit(0)
bk=set();bt=set();bg=set();bs=set()
for p in glob.glob(V+'/**/*.md',recursive=True):
    if skip(p) or os.path.abspath(p) in files: continue
    d=fm(p); bk.update(d.keys()); bt.update(d.get('types',[])); bs.update(d.get('status',[])); bg.update(t.lstrip('#') for t in d.get('tags',[]))
bad=[]
for f in files:
    d=fm(f)
    bad+=[(f,'property',k) for k in d if k not in bk]
    bad+=[(f,'type',t) for t in d.get('types',[]) if t not in bt]
    bad+=[(f,'tag',t) for t in d.get('tags',[]) if t.lstrip('#') not in bg]
    bad+=[(f,'status',t) for t in d.get('status',[]) if t not in bs]
if bad:
    print("vault-check: new values the vault does not already use:")
    for f,kind,v in bad: print(f"  {kind}: {v}  in {os.path.relpath(f,V)}")
    sys.exit(1)
print(f"vault-check: ok ({len(files)} files)")
