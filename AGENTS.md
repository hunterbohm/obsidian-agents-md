# Hunter's vault

Everything Hunter owns plus his notes: planning, projects, tasks, people,
meetings, knowledge, content. He authors the thinking. Agents file, link, and
help keep the structure, never without his approval. Empty beats filler.

This file is the what and the boundaries. The `obsidian` skill is the how
(search, create, move, tasks, the Log line, commit). Load it first. Where
the two disagree, this file wins.

## Boundaries

1. Write only what Hunter asked for in this session. Never overwrite his
   notes. Read the note first; his version wins.
2. Search the folder before you create. One note per thing.
3. `03 - Journal/` is Hunter's alone. Open it only when he says so.
4. Use facts Hunter supplied or sources read this session. Ask about uncertain
   values or leave them blank. Put any proposed inference in prose, clearly
   marked unverified. A fact that changes (a price, a count, a retainer)
   carries `as of YYYY-MM-DD`.
5. Use the current template for that note type and TaskNotes configuration
   for tasks. An existing note is not permission to introduce a field or
   value. Before you commit, run
   `python3 vault-check.py` on your changed files.
   It checks whether vocabulary exists elsewhere in the vault, not whether
   it belongs on that kind of note.
6. Commit each completed request under your agent name, with a message that
   says what and why. Include only your changes. Preserve Hunter's edits and
   other agents' work. Touch only the lines the request requires.
7. A task's status changes only when Hunter asks.
8. Nothing leaves the vault for an audience without Hunter's approval. No
   sends, posts, or publishing. A draft stays a draft until he says approved.
9. A direct request from Hunter authorizes that work. Ask before expanding
   its scope. Silence is not approval. If a request breaks one of these
   rules, say which one and offer the version that keeps it.

## The map

- `00 - Inbox/`: unprocessed captures. Hunter sorts them. Unsure where a
  note goes: create it here.
- `01 - Areas/`: one note per ongoing area of life or business.
- `02 - Planning/`: `Daily/` one note per day; `Weekly/` and `Quarterly/`
  plans; `Task Records/` one TaskNote per task, filename is the title.
- `03 - Journal/`: Hunter's alone.
- `04 - Projects/`: `Active/`, `Client Projects/`, `Completed/`. One note per
  project; a filled `client:` makes it a client project.
- `05 - Content/`: `Personal Brand/` ideas and drafts, with `_brand/` for
  voice, audience, platforms and email; `Hubs/` weekly content hubs;
  `Assets/` media; `Archive/` published and legacy work.
- `06 - Contacts/`: `Work/`, `Personal/`, `Family/` people; `Orgs/`
  organizations, with `clients/`, `relationships/`, `family/` under it;
  `Meetings/` one note per meeting, `YYYY-MM-DD HHMM Topic`, created by the
  calendar sync and filled by `meeting-processing`.
- `08 - Resources/`: reference notes by type: Books, Courses, Documents,
  Homelab, Ideas, Learning, Movies, Places, Podcasts, Products, Project
  Notes, Reference, Shows, Sources, Subscriptions, Testimonials, Topics,
  Travel, Wishlist.
- `Utilities/`: `Templates/` one template per note type, its folder is the
  note's folder; `Bases/` the views notes embed; `Views/` dataviewjs views;
  `Attachments/`; `Scripts/`; `Archive/` the one archive.
- `Clippings/`, `Excalidraw/`: plugin output.

Client delivery lives in `~/clients/<name>`, code in `~/code`, agent setup in
`~/command-center`, raw data in `~/archives`. The vault links to them and
holds no copies. Events live in Google Calendar.

## What an agent writes

When Hunter asks, and only then:

- **Tasks.** One TaskNote per task, from the TaskNotes schema, in
  `02 - Planning/Task Records/`.
- **Updates to notes that exist.** A project's status tag, Overview and
  links; a reference note filled from a receipt or an archive. Nothing
  invented.
- **Linking.** When linking is requested, link existing words where the
  connection helps, or use an existing relationship property. Read the
  target note first. Keep Hunter's wording and add no properties just to
  create links.
- **Views.** Bases, dataviewjs views, dashboards, templates. Written once,
  embedded by link. Dashboards and task views read the source notes. Keep
  counts, statuses, and task lists in those records rather than maintaining
  copied summaries.
- **Cleanup.** Delete, archive, retag, or move, with the list agreed first.

Always:

- **Answers.** Most of the time the agent reads and writes nothing: it finds
  the note and answers from it.
- **The Log line.** One `- HH:MM — text (agent)` line under `## Log` in
  today's daily note after meaningful work. `## Scratch` is Hunter's.

Automations that write on their own: the calendar sync creates meeting and
contact notes; `meeting-processing` fills meeting notes; the habit check
ticks `## Habits`. Other agents read those and edit one only when Hunter asks.

Write it plainly.  Plain words, periods and commas, no em dashes in prose. Wikilinks for notes, Markdown links for URLs.
