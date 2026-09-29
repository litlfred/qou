---
# qou-msp2
title: setup-folio-assistant.sh links folio-assistant to cat-harness/, but all 46 importers expect the clone root
status: todo
type: bug
priority: high
tags:
    - platform
    - migration
created_at: 2026-09-29T21:12:50Z
updated_at: 2026-09-29T21:12:50Z
parent: qou-n4r9
---

**Measured 2026-09-29 on main `32cb188c0`, platform pin `37a36ce92`.**

`scripts/setup-folio-assistant.sh` detects the split platform layout and
links `folio-assistant` → `<clone>/cat-harness` (`PLATFORM_ABS`, line 193).
But every qou file that imports the platform spells the path with
`cat-harness/` inside it:

    folio-assistant/cat-harness/<x>   46 files (.ts/.py/.sh)
    folio-assistant/<x>                0 files

So under the link the script creates, each of those resolves to
`<clone>/cat-harness/cat-harness/<x>`, which does not exist. Example:
`bun run scripts/run-validate.ts` fails on its first platform import.

**Found while verifying PR #7485.** `run-validate` could only run after
re-linking by hand: `ln -sfn <clone> folio-assistant`. Its output was then
identical on branch and main, so the pointer, not the corpus, is at fault.
`precision-gates.sh` does not import the platform, which is why it ran green
under either link and did not reveal this.

**Probable cause.** The 2026-09-26 pin bump (see `.folio-assistant-pin`)
re-pointed 77 files to `folio-assistant/cat-harness/<x>`. The setup script's
split-layout branch predates that and links one level too deep.

**Fix options, to check before choosing:**
1. Link to the clone root (`PLATFORM_ABS="$CLONE_ABS"`). One line; all 46
   resolve. The pre-split bibliography-bridge branch keys off
   `PLATFORM_ABS = CLONE_ABS`, so check that it is not triggered wrongly.
2. Keep the link and strip `cat-harness/` from the 46 importers. Larger,
   and it reverses the pin-bump commit's convention.

**Done when:** a fresh `scripts/setup-folio-assistant.sh`, followed by
`bun run scripts/run-validate.ts folio/quantum-observable-universe`, runs
with no manual re-link.
