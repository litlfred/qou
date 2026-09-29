---
# qou-msp2
title: setup-folio-assistant.sh links folio-assistant to cat-harness/, but all 46 importers expect the clone root
status: completed
type: bug
priority: high
tags:
    - platform
    - migration
created_at: 2026-09-29T21:12:50Z
updated_at: 2026-09-29T21:39:45Z
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


--------

## Summary of Changes (2026-09-29): option 1, link to the clone root

**`scripts/setup-folio-assistant.sh`** links `folio-assistant` → the clone
ROOT in both layouts. The layout is still detected, but it is kept in
`PLATFORM_SPLIT` and no longer inferred from the link target. That matters
because the pre-split bibliography bridge was guarded by
`PLATFORM_ABS = CLONE_ABS`, which would have become true on a split clone
too and minted stray `folio/schema/` and `schemas/` directories there. It is
now guarded by `PLATFORM_SPLIT = 0`. A pre-split clone gets a warning, since
qou no longer has importers for that layout.

**The other convention, measured before choosing.** The bean said "0 files"
use `folio-assistant/<x>`. That was a blind count: its pattern could not see
`../folio-assistant/scripts/…`. Recounted over all live code, CI and config,
**7 sites** went through the link in the old form. All 7 moved to
`folio-assistant/cat-harness/<x>`, and each target exists at pin `37a36ce92`:
- `scripts/refresh-authors-note.ts` import. This is what the
  `witness-staleness` CI job runs.
- `.github/workflows/lake-cache-refresh.yml` `lake-cache.sh` candidate.
- `deploy/provision.sh` `ui` copy.
- 4 printed help commands, for `pdf-structure.py` and `pdf-ocr.py`.

Also moved: `deploy/update-server.sh` `../folio-assistant/ui`. That is the
sibling clone path, not the link, but the same split left it pointing at
nothing. `kg-vocabulary-gate.yml` already tried both forms. Its comment is
corrected, and the current form now comes first; the old one stays for
checkouts linked by the previous script.

**Verified with a fresh setup (the done-when test)** against a pinned clone:
- The link resolves to `../<clone>`.
- On a split clone the bridge is correctly skipped, and the platform clone is
  left untouched: 0 dirty files, no stray directories.
- `run-validate.ts folio/quantum-observable-universe` passes: exit 0,
  "4 issue(s)", the same as `main`.
- `refresh-authors-note.ts --check` passes: exit 0.
- `lake-cache.sh`, `gen-block-jsonld.ts` and `ui` all resolve.
- Every unique `folio-assistant/cat-harness/…` path (35) resolves, with 1
  exception below. The two `.js` ones are the ESM form of `.ts` files that exist.

**Calibrated.** `main`'s script against the same clone links `cat-harness/`,
and `run-validate` then exits 1 with `Cannot find module
'../folio-assistant/cat-harness/content/pipeline/value-registry-di'`. Re-running
the fixed script over that old link repairs it, and `run-validate` passes.

**Found and deliberately left:** `computations/m_tau_complex_volume_search.py`
and `m_tau_knot_prediction.py` write `"$schema":
"../../folio-assistant/cat-harness/schemas/witness.schema.json"`. No such file
exists anywhere in the platform, under either link. It is dead on `main`
too, and it is a JSON Schema hint, not an import. qou's own copy is
`tools/hecke-engine/schemas/witness.schema.json`. Separate from this bean.
