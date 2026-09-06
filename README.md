# The one file my agent reads before it touches my vault

My Obsidian vault is the operating system I run my life on. It is not an AI memory store. If you let agents do whatever they want inside it, you get mountains of slop, and it compounds. This file tells them how to operate in there without wrecking the structure or the mental model in my head.

This repo gives you two things.

| File | What it is |
|---|---|
| [`AGENTS.md`](AGENTS.md) | My real one. Nine boundaries, a map of every folder, what an agent may write, how to write. Read it to see what a good one contains. Do not copy it. Your vault is not mine. |
| [`PROMPT.md`](PROMPT.md) | A prompt that makes your agent interview you, one question at a time, until you both agree on the shape of your vault. Then it writes yours. |

Also here: [`vault-check.py`](vault-check.py), a small script that fails when a note introduces a type, tag, status, or property your vault has never used. Agents run it before they commit. It is the only mechanical gate; the rest is the file.

## The one rule, if you only add one

Read whatever you need. Write nothing without my permission.

## Set it up

1. Put `AGENTS.md` and `PROMPT.md` from this repo in your vault folder, next to your notes. If you use Claude Code, add a `CLAUDE.md` containing only `@AGENTS.md`.
2. Open your agent in that folder and paste the contents of `PROMPT.md`.
3. Answer its questions. Push back. Say "approved" only when the draft is yours.
4. Delete my `AGENTS.md`. Yours is the one that stays.

Optional: keep `vault-check.py` in the vault and tell agents to run it on their changed files before every commit. It reads only the frontmatter block at the top of each note.

## What the nine boundaries are for

1. Write only what I asked for. My version of a note wins.
2. Search before you create. One note per thing.
3. The journal is mine.
4. Never invent a value. Not sure means ask me, or leave it blank.
5. The template decides the fields. No new types, tags, statuses, or properties.
6. One completed request, one commit, under the agent's own name.
7. A task's status changes only when I ask.
8. Nothing leaves the vault for an audience without my approval.
9. A request is the permission for that work, not for more. Silence is not a yes.

Every one of these exists because an agent did the opposite in my vault. Duplicate tasks. A rewritten weekly note. A priority I never set. Thirty-one view files "archived" while every note still used them.

## Works with

Claude Code, Codex, Hermes, Pi, OpenCode, anything that reads an `AGENTS.md` or a `CLAUDE.md` at the root of the folder it runs in. The file is plain Markdown. Cheaper models behave better with a strict map and hard boundaries than strong models without them.

## License

MIT. Take it, change it, keep the parts that fit.
