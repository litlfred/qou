# `migration/folio-assistant/` — staging for work destined for the platform

Owner, 2026-09-26: *"QOU KG content, skills, tools, stay in QOU. if you think it
should be in folio-assistant, put in sub-dir folio-assistant for now as part of
migration."*

So: **qou's KG content, skills and tools stay in qou.** This directory is only for
things an agent judges belong **upstream** in `litlfred/folio-assistant`, parked here
until they are actually contributed. Anything here is a *proposal*, not a dependency —
nothing in qou may import from this directory.

## 🛑 Why it is not literally `folio-assistant/`

The instruction says "sub-dir folio-assistant", and that path is taken:

    $ ls -ld folio-assistant
    lrwxrwxrwx  folio-assistant -> ../folio-assistant

`folio-assistant/` in a qou checkout is a **gitignored symlink** to the sibling
platform clone, created by
[`scripts/setup-folio-assistant.sh`](../../scripts/setup-folio-assistant.sh). It is
load-bearing, not incidental: every pipeline invocation in the repo goes through it —
`folio-assistant/content/pipeline/readme-sections.ts`,
`folio-assistant/content/pipeline/qa-sweep.ts`, `folio.config.json`'s
`adapterModule`, and the `../../../folio-assistant/schemas/builders` import in every
one of ~3,760 content-block `.ts` files.

A **tracked** directory at that path would collide with the symlink. So the staging
area is one level in, where the name still says what it means.

The owner separately selected "retire the symlink first" alongside this option, which
is the larger change — it needs `setup-folio-assistant.sh` rewritten and every
consumer path re-pointed. That is its own story; this directory does not wait on it,
and if the symlink is ever retired this directory can move to `folio-assistant/`
unchanged.

## What belongs here

- A checker, schema or Tool that is genuinely generic rather than qou-specific.
- A fix to platform behaviour that qou discovered — the platform is a separate repo
  this session cannot push to, so the patch is staged rather than applied.

## What does NOT belong here

- Anything qou imports or executes. Nothing may depend on this path.
- qou's own KG content, skills or tools. Those stay where they are, by the ruling
  above.
- A copy of a platform file for reference. Read it in the `folio-assistant/` checkout
  or in a throwaway clone; a copy here is a fork that goes stale silently.

## Contributing upstream

`litlfred/folio-assistant` is read-only from this session (anonymous git reads only,
no push, no GitHub API). Landing anything from here means either the owner pushes it
or a session is given push access to that repo.
