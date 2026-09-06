# The interview prompt

Paste this into your agent (Claude Code, Codex, Hermes, Pi, anything that reads files) with your vault as the working folder. It reads the example AGENTS.md, then interviews you until you both agree on the shape of your vault, then writes yours.

---

You are helping me write the AGENTS.md for my Obsidian vault. This file tells every agent that opens the vault how to operate inside it without wrecking the structure or adding slop.

Read `AGENTS.md` in this folder first. It is one person's real file, not a template. Mine will be different. Use it only to understand what a good one contains: a short statement of what the vault is, hard boundaries, a map of every folder, what an agent may write, and how to write.

Then interview me. One question at a time. Wait for my answer before the next one. Short questions, plain words, no lists of options unless I ask. Cover, in this order:

1. What this vault is for. One sentence in my words.
2. My folders. Run `ls` and show me the tree, then ask what each top folder holds and which ones agents must never touch.
3. What I write by hand and what I want agents to write. Be specific: tasks, meeting notes, daily notes, project notes, reference notes.
4. How I track tasks (a plugin, checkboxes, a folder) and who is allowed to change a task's status.
5. What my notes look like: which properties I actually use, which tags, what the filename is. Read three or four of my notes to check before asking.
6. What must never leave the vault without my say-so: sends, posts, publishing, spending.
7. How I want changes recorded: git commits or not, one change per commit or not, whose name goes on them.
8. Anything you saw in my notes that looks like slop an agent left behind. Ask if I want a rule against it.

After the interview, draft my AGENTS.md. Keep it under 100 lines. Boundaries first, numbered. Then the map, every folder with one line. Then what an agent writes, split into "when I ask" and "always." Then one line on how to write. Plain words, no em dashes, no filler. Every rule must trace to something I told you or something you saw in my notes; do not invent rules.

Show me the draft. I will edit or object. Revise until I say "approved." Only then save it as `AGENTS.md` at the root of my vault, and add a `CLAUDE.md` next to it containing only `@AGENTS.md` if I use Claude Code. Do not write anything else to my vault during this.
