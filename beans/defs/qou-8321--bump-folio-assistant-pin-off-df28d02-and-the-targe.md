---
# qou-8321
title: Bump .folio-assistant-pin off df28d02 — and the target is moving ~80 commits/hour
status: todo
type: feature
priority: high
tags:
    - platform
    - migration
created_at: 2026-09-26T11:20:29Z
updated_at: 2026-09-27T10:07:45Z
parent: qou-n4r9
---

**Owner-gated. `qou-ty42` records this as step 5, "NOT DONE — owner's call".
Nothing here changes that; this story records what the bump now involves.**

## The target is moving fast enough to matter

Measured this session, roughly one hour apart:

```
e53bba80284   (first measurement)
42ccfb38b63   (second)      -> 80 commits
```

The pin is `df28d02` (2026-09-07), so it is now **~19 days and several hundred
commits behind**. Two consequences:

1. **Pick a sha and hold it.** "Bump to main" is not a reviewable instruction at
   this velocity — the sha that gets reviewed will not be the sha that lands.
   Name the exact sha in `.folio-assistant-pin` and in the commit message.
2. **Any plan written against main goes stale in hours.** This epic's own
   `qou-yf1y` had to be corrected mid-session for exactly that: a sibling reading
   said the declaration was folded into the config, and 80 commits later it is a
   separate `<name>.json`.

## The pin file's own rule, which binds this commit

From `.folio-assistant-pin`'s header:

> When you bump it, state the before/after issue counts in the commit message —
> a change in count is a platform behaviour change and should be looked at, not
> absorbed silently.

**Both counts must be taken at the SAME corpus commit**, which the last bump's
note is explicit about. The 2026-09-07 bump recorded `428ca5c → 6 lines / "9
issue(s)"` against `df28d02 → 3 lines / "3 issue(s)"`, and explained the delta
(three `Unknown field` warnings clearing because four block schemas began
extending `BlockBaseSchema`). That is the standard to meet.

Current baseline at the pin, measured 2026-09-26: `run-validate
content/quantum-observable-universe` → **2 issue(s)** (a bibliography info line +
`lem:piece-a-corner-removal-obligation` with no Lean declaration).

## Prerequisites, and one of them is a hard blocker

- **`qou-yf1y` MUST land first.** After the bump, `findDeclarationFile` decides
  what an instance is, and `harness.json` fails its test (stem `harness` ≠ name
  `qou`). Bump without it and qou has **no discoverable instance**.
- **`qou-pwp9` should land first.** `build.yml` calls the platform at `@main`,
  which bypasses the pin entirely — bumping the pin while that line stands
  improves nothing for the published build.
- `qou-utbr` and `qou-yqko` are independent of the bump and can land either side.

## The layout probe already handles both worlds

`setup-folio-assistant.sh` probes for `cat-harness/schemas/types.ts` and points
the symlink at whichever root holds the platform, so qou works against the
pre-split and split layouts. This session's run reported `platform layout:
pre-split (clone root)`. So the bump is not a cliff — but note the same script
**silently declines to move a dirty clone and still exits 0** (`qou-ty1p`), which
is precisely how a bump can appear to have happened and not have.

## Not started.



## Added 2026-09-26 — this bump now OWNS one deletion

`qou-yf1y` has landed `qou.json` + `qou.config.json` and deliberately left
`folio.config.json` in place, because at the pin it is the only config the platform reads.

**So the bump commit must also `git rm folio.config.json`.** Doing it earlier leaves the
folio unconfigured with no error — `profile-check.ts` reports `undetermined` and runs
every criterion including the paper adapter's LaTeX-shaped axes. Doing it later leaves two
configs that can disagree.

Also note `qaAxes` is now set in **both** files. At the pin it is a no-op (measured:
`archimedean-wall` is not an axis there); after the bump the `qou.config.json` copy is the
live one.


---

## 2026-09-27 — THE BUMP LANDED. This bean's title and its "Not started" are both false, and the bump turned on six QA criteria nobody has verified.

Found while doing repo-separation prep. Three corrections and one live finding.

### Correction 1 — the pin is not `df28d02`

| claim here | ground truth |
|---|---|
| title: *"Bump `.folio-assistant-pin` off `df28d02`"* | `.folio-assistant-pin` last line: **`37a36ce9296b95a9ad4862d51dc496ac44053143`** |
| §*"## Not started."* (line 75) | `1ea9676d3f` — *"pin(qou-8321): bump the platform df28d02 -> 37a36ce, and re-point the 77 files the restructure moved"* |
| — | `bash scripts/folio-pin-coupling-check.sh` → `ok: platform pin coupled — both declare 37a36ce9296` |

### Correction 2 — the `git rm folio.config.json` this bean requires did NOT happen

Line 84: *"**So the bump commit must also `git rm folio.config.json`.** Doing it
earlier leaves the folio unconfigured."* Measured: `folio.config.json` **is still
present**. The commit that was supposed to carry the deletion landed without it.

**Not deleting it here.** Two independent gates: `qou-n4r9` records that *"the
ruling that `folio.config.json` must not be deleted holds until `qou-yf1y`"* (still
`in-progress`), and that file's own comment defers the question to `qou-w5av`.
§🟥 ASK THE OWNER applies on top. Recorded, not acted on.

### 🛑 Correction 3, and it is the one that matters — both config files say "inert at the pin", and at the CURRENT pin they are LIVE

`qou.config.json:29` and `qou.json:19` each carry a `_platform_scope_comment`
measured **2026-09-26 at `df28d02`**:

> *"the PINNED platform df28d02 has no `resolveHarnessConfigPath` and reads
> `folio.config.json` (src/index.ts:94), so **THIS FILE IS INERT AT THE PIN**"*

And `qou.config.json:30`, on the `qaAxes` key:

> *"Measured at df28d02: the string `archimedean-wall` occurs EXACTLY ONCE in
> `content/pipeline/qa-criteria-registry.ts`, and it is part of a criterion ID …
> **not an axis name**. … So this key is a **NO-OP at the pin** and becomes
> load-bearing only after the bump."*

**The bump happened.** Measured at `37a36ce`:

| | `df28d02` (what the comments measured) | `37a36ce` (the live pin) |
|---|---|---|
| `resolveHarnessConfigPath` | absent | **present** — `cat-harness/schemas/harness-config.ts:501` |
| `archimedean-wall` in `qa-criteria-registry.ts` | 1 occurrence, a criterion **id** | **16 occurrences**, and a real **axis** |
| the axis gate | does not exist | `folioOptionalAxes().includes("archimedean-wall")` gates `FRAMEWORK` at **:2503** and `WALL` at **:2508** |

So `qaAxes: ["archimedean-wall"]` is **no longer a no-op**. On the comment's own
list, that registers six criteria plus their watcher buckets:
`framework-canonical`, `wall-side-correct`, `wall-side-statement`,
`wall-side-proof`, `wall-base-ring-minimal`, `detangler-archimedean-wall`.

**The conclusion is robust to which config is read.** Whether the platform now
resolves `qou.config.json` (stem == instance name) or still `folio.config.json`,
**both files set the same `qaAxes`**, so the axis is on either way. I did not
settle which one is read, and it does not change this.

### What is NOT established

- **Whether the six criteria have actually produced verdicts since the bump.** No
  sidecar sweep was run. "The axis is registered" and "criteria have run" are
  different claims and only the first is measured.
- Whether turning them on is *wanted*. The comment calls it the deliberate opt-in
  for this folio's mathematics, so presumably yes — but it happened as a side
  effect of a pin bump rather than as a decision, and nothing reported it.
- Whether `q-usage` should also be listed. The same comment leaves that explicitly
  open and calls it an owner call.

### Status

Stays **todo**, and the title should be re-read as *"finish what the bump left
behind"*: the `folio.config.json` deletion (gated), the two stale scope comments,
and a verification pass on the six newly-live criteria. The bump itself is done.
