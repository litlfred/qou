---
# qou-yf1y
title: 'Instance declaration + config: qou.json and qou.config.json replace three retired spellings'
status: todo
type: feature
priority: high
tags:
    - platform
    - config
    - reorg-2026-10-04
created_at: 2026-09-26T11:18:46Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-n4r9
---

**Answers the owner's question of 2026-09-26: *"Should need
folio-assistant.config.json.... why folio.config.json"*. Measured against
platform main `42ccfb38b63`.**

## The answer: `qou.json` + `qou.config.json`. Two files, not one.

`cat-harness/schemas/cat-harness.ts` on current main:

```
export const DECLARATION_SUFFIX = ".json";
export const CONFIG_SUFFIX      = ".config.json";
export function instanceConfigFilename(name)      { return `${name}${CONFIG_SUFFIX}`; }
export function instanceDeclarationFilename(name) { return `${name}${DECLARATION_SUFFIX}`; }
```

So an instance named `qou` is declared by **`qou.json`** and configured by
**`qou.config.json`**.

## Why not `folio-assistant.config.json`

`findDeclarationFile()` decides what a declaration IS, and the rule is a
self-consistency check, not a lookup:

> *"Scans for `*.json` and returns the one that both carries a `name` and whose
> filename stem EQUALS that name."*

The stem names **this instance**, not the harness the instance runs on. The
platform's own checkout is the worked example: it holds `cat-harness`,
`bootstrap` and `folio-assist-core` as instances and names their files after
*them*. A `folio-assistant.config.json` in qou would need a
`folio-assistant.json` declaring `"name": "folio-assistant"` — which would
declare **qou's checkout to be an instance called folio-assistant**. It is not;
it is an instance called qou that *depends on* folio-assistant. The dependency is
expressed by `dependencies.folioAssistant` inside the config, not by the filename.

So the owner's FIRST instinct this session was right — *"Will need
qou.config.json if new harness"* — and the later `folio-assistant.config.json`
would misname the instance. Flagging both because they conflict and only one is
implementable.

## Why `folio.config.json` exists at all

It is simply the oldest of three names, and the platform says in its own words
that it *"described the wrong thing: the file configures the HARNESS — adapter
selection, the skills directory, the viewer, simulators, translation, the two
work-plan stores — not the folio's content."* Lineage:

| name | status upstream | present in qou? |
|---|---|---|
| `folio.config.json` | retired 2026-09-18 | **yes — and it is the ONLY one the pinned platform reads** |
| `harness.config.json` | `LEGACY_HARNESS_CONFIG`, kept only so `check:instance-config` can find it | yes |
| `harness.json` | superseded by `<name>.json` | yes |
| `qou.json` + `qou.config.json` | current | **absent** |

## 🛑 `harness.json` is not merely old-named — it FAILS the declaration test today

Its stem is `harness`; its `name` field is `"qou"`. Stem ≠ name, so
`findDeclarationFile` rejects it outright. The platform has a phrase for exactly
this state: *"a mismatched stem is the rename-half-done case
`check:instance-config` already reports."* So after a pin bump, qou would have
**no discoverable instance at all** until this story lands.

## The work

1. `git mv harness.json qou.json` — content unchanged, `"name": "qou"` already
   correct, stem now agrees.
2. `git mv harness.config.json qou.config.json`.
3. Fold `harness.json`'s `directories` block into `qou.config.json` **only if**
   current main wants it there — measure, do not assume; the two-function split
   above suggests declaration and config stay separate files.
4. Fix `feedbackDir` to `.folio-feedback` in whichever file is live (see
   `qou-sm2c` — this is a real defect today, independent of the migration).
5. `folio.config.json`: keep until the pin moves (`qou-ty42`: "must not" be
   deleted), then delete in the SAME commit as the bump, never before.

## Cost / risk

Four file operations plus one value fix. Risk is concentrated in step 5: delete
`folio.config.json` while the pin is still `df28d02` and the folio becomes
**unconfigured** — `profile-check.ts` reports `undetermined` and runs every
criterion including the paper adapter's LaTeX-shaped axes, per
`harness.config.json`'s own comment. That failure is silent.



## Claimed 2026-09-26 by `claude/folio-assistant-instantiation-and-bean-hierarchy-2026-09-26`

Owner said "Go" on the recommended ordering (this story first).



## 2026-09-26 — RENAME DONE; one step deliberately deferred

Done on `claude/folio-assistant-instantiation-and-bean-hierarchy-2026-09-26`:

1. `git mv harness.json qou.json` — stem now equals the file's own `name` field, so it
   passes `findDeclarationFile` where `harness` ≠ `qou` failed it.
2. `git mv harness.config.json qou.config.json`.
3. **`feedbackDir` fixed in `folio.config.json`** — `folio-assistant/feedback` →
   `.folio-feedback`. This is the live defect of `qou-sm2c`: the pin reads
   `folio.config.json`, so the broken value was in force. Verified **no data moves**:
   both `.folio-feedback` and `folio-assistant/feedback` are absent on disk, which also
   confirms the original diagnosis that the old path never existed under either layout.
4. `qaAxes: ["archimedean-wall"]` added to `folio.config.json` — a no-op at the pin,
   correct after a bump. **Verified as a no-op rather than assumed:** `run-validate`
   reports **2 issue(s)** before and after, identical.
5. Comments in both renamed files SCOPED to the platform they describe (`qou-29i6`), and
   `qou.config.json` now answers the naming question in-file: it is not
   `folio-assistant.config.json` because the stem names this instance, not the harness.
6. `scripts/setup-folio-assistant.sh` comment updated `harness.json` → `qou.json`.

**Verification:** `run-validate` 2 issues (baseline, unchanged); `readme-sections --check`
exit 0; all three JSON files parse; `bash -n` on the setup script; declaration scan finds
**exactly one** declaration (`qou.json`) where it previously found zero. Checked for a
collision first: `package.json` also carries `"name": "qou"` but its stem is
`package`, so it fails the stem==name test and is not a declaration.

**STATUS STAYS in-progress.** One step remains and it is NOT this bean's to take:
deleting `folio.config.json`. `qou-ty42` says it must not be deleted, and at the pin it
is the only config actually read — deleting it now leaves the folio UNCONFIGURED, silently.
It is deleted in the same commit that bumps the pin, which is **`qou-8321`** (owner's
call).

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.


## Progress 2026-11-16 (Round 49 verification — kept `in-progress` per owner closure rule)

- **Verified on `origin/main` (`dc12b128cc`):**
  - `qou.json` and `qou.config.json` are live at the repository root (`name: "qou"`, `needs: ["folio-assistant-sci"]`, `dependencies.folioAssistant` pinned to `.folio-assistant-pin = 82b389982a73701b77f723d34d42c77acf41b5b4`).
  - All three retired config/declaration spellings (`folio.config.json`, `harness.config.json`, `harness.json`) are completely absent from `origin/main`.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8167, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
