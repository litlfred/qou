---
# qou-yf1y
title: 'Instance declaration + config: qou.json and qou.config.json replace three retired spellings'
status: todo
type: feature
priority: high
tags:
    - platform
    - config
created_at: 2026-09-26T11:18:46Z
updated_at: 2026-09-26T11:23:02Z
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
