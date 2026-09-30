---
# qou-8321
title: Bump .folio-assistant-pin off df28d02 — and the target is moving ~80 commits/hour
status: completed
type: feature
priority: high
tags:
    - platform
    - migration
created_at: 2026-09-26T11:20:29Z
updated_at: 2026-09-30T15:14:27Z
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

## Measured 2026-09-27 — nothing "turned on", and one of the six CANNOT: the pin bump changed no verdict

The item this bean left open — *"whether the six criteria have actually produced
verdicts since the bump"* — is now measured across all **3653** `.qa.json`
sidecars on this branch. The answer corrects the framing of the entry above.

### They were already live, for months

| criterion | automated? | entries | verdicts | `reviewed_at` range |
|---|---|---:|---|---|
| `framework-canonical` | yes — `checkFrameworkCanonical` | 3577 | 3574 pass / **3 fail** | 2026-07-13 .. 2026-09-15 |
| `wall-side-correct` | yes — `checkWallSide` | 3577 | 1296 pass / 2274 n/a / **7 fail** | 2026-07-07 .. 2026-09-26 |
| `wall-base-ring-minimal` | yes — `checkBaseRingMinimal` | 3588 | 1245 pass / 2279 n/a / **64 warn** | 2026-07-13 .. 2026-09-26 |
| `wall-side-statement` | **no** — agent-adjudicated | 603 | 582 pass / 1 warn / 20 n/a | 2026-06-13 .. 2026-09-03 |
| `wall-side-proof` | **no** — agent-adjudicated | 393 | 372 pass / **18 fail** / 3 n/a | 2026-06-13 .. 2026-08-23 |
| `detangler-archimedean-wall` | yes, but a **stub** | 3577 | **3577 n/a, nothing else, ever** | 2026-07-13 .. 2026-09-26 |

The earliest verdict is **2026-06-13**, three months before the bump. So
"six newly-live criteria" and "turned on as a side effect of a pin bump" are
**wrong**: five of the six had been producing verdicts continuously, and the
bump moved no verdict at all.

### 🛑 And `qou.config.json:30` was RIGHT — my correction of it was the error

That comment says `archimedean-wall` is *"a NO-OP at the pin"*. The entry above
treats that as stale. It is not, for the criterion it names. At the **live** pin
`37a36ce`, `cat-harness/content/pipeline/qa-checkers-extended.ts:1856`:

```ts
export function checkDetanglerArchimedeanWall(
  _tsPath: string | undefined,
  _leanPath: string | undefined,
): CheckerResult {
  // TODO: parse the chapter directory + classify Lean files as
  // archimedean / generic-R / mixed; verify the chapter's expected
  // wall side per the chapter-ts metadata. n/a until wired.
  return { result: "n/a", hits: [] };
}
```

Both parameters are underscore-prefixed and unread; the body is an
unconditional `n/a`. **3577 of 3577 `n/a` is exactly that function's output** —
2274 annotated *"block has no .lean sibling"* by the harness and **1303 with no
note at all**, i.e. blocks that DO have a `.lean` and still get `n/a`, because
the checker never looks. It is a no-op in the platform source, not behind an
axis gate, so no config change of any kind can make it fire.

**What my measurement got right and what it got wrong.** The axis facts hold —
`resolveHarnessConfigPath` exists at `harness-config.ts:501`, `archimedean-wall`
occurs 16 times and is a real axis, and `folioOptionalAxes()` gates `FRAMEWORK`
at `:2503` and `WALL` at `:2508`. What was wrong was the **inference**: from
"the axis registers these criteria" to "these criteria began producing
verdicts". Registered ≠ ran — the exact distinction this bean itself flagged as
unmeasured one paragraph earlier, and then reasoned past.

### The live findings, with freshness, since they are the actionable part

Freshness = every key of the entry's `field_hash` still matches the sidecar's
current `source_hashes`. A stale verdict adjudicates a block version that no
longer exists.

| criterion | fail/warn | FRESH | stale | entry freshness overall |
|---|---:|---:|---:|---|
| `framework-canonical` | 3 fail | **3** | 0 | 3077 fresh / 500 stale |
| `wall-side-correct` | 7 fail | **6** | 1 | 3240 fresh / 337 stale |
| `wall-base-ring-minimal` | 64 warn | **60** | 4 | 3376 fresh / 212 stale |
| `wall-side-proof` | 18 fail | **0** | **18** | 58 fresh / 263 stale / 72 no-field-hash |
| `wall-side-statement` | 1 warn | — | — | 154 fresh / 366 stale / 83 no-field-hash |

The three fresh `framework-canonical` fails: `information-theory/skein-filtration-trichotomy`,
`notation/notation-collisions`, `notation/notation-register-table4-data`.

The six fresh `wall-side-correct` fails: `appendix-qvalues/fivetwo-discriminant-vanishes`,
`appendix-qvalues/fivetwo-envelope-transport`,
`knots-particles-confinement/unstable-atom-decay-channel`,
`mass-theory/descended-level-zero`, `mass-theory/poincare-lefschetz-borromean`,
`stochastic-mechanics/macroscopic-stability-equivalence`.

**`wall-side-proof` is the one to read carefully: 18 fails and NOT ONE is
fresh.** They are dated 2026-06-28 / 2026-07-07 and say *"Lean proof contains
compilation errors"* (10), *"sorry placeholder"* (5), *"Missing proof"* / *"no
corresponding proof block"* (2), *"lean file not found"* (1) — against blocks
whose Lean has moved in the three months since. Because the criterion is
`automated: false`, **nothing re-runs it**; a sweep cannot refresh it and only an
agent adjudicating the block can. So "18 failing proofs" is not a current
corpus state and must not be quoted as one — it is 18 unrefreshed records, over
half of them plausibly already fixed by the Lean work that landed since.

### What I did NOT do, deliberately

No sidecar was refreshed and no finding was fixed. Draining 3 + 6 + 60 fresh
findings across five chapters, or re-adjudicating 18 stale `wall-side-proof`
records, is a corpus-wide pass in files I was not sent to, which §🟥 ASK THE
OWNER puts behind a decision. Measuring is not changing; this entry is the
measurement.

### Status

Stays **todo**. The open items narrow to three, of which only the first is new:

1. **`detangler-archimedean-wall` is a stub with 3577 records and zero
   information** — worth its own bean upstream (the TODO is in the platform, not
   here), and worth *not* counting as a live wall gate anywhere in qou's docs.
2. The `folio.config.json` deletion — still gated (`qou-n4r9` / `qou-w5av`).
3. `qou.config.json:29` / `qou.json:19`'s *"INERT AT THE PIN"* comments — stale
   as to `resolveHarnessConfigPath`, and **`:30` is not stale**, per above.


## Summary of Changes (2026-09-30)
Bumped 37a36ce -> 378a100 in #7491 (merged, e339aced), with the pin and build.yml in one commit. run-validate: 4 -> 4 issues, the same lines, once run-validate.ts and preload-registry.ts import configureLeanPackages from cat-harness/content/pipeline/lean-formal-ref. Without that import it was 21 (17 false 'requires Lean formalization'). A follow-up bump to the folio-assistant#1620 merge rides with #7490's follow-up PR.
