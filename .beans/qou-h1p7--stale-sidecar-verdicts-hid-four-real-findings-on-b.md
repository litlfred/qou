---
# qou-h1p7
title: Stale sidecar verdicts hid four real findings on blocks the voice fix touched
status: completed
type: task
priority: normal
created_at: 2026-08-24T19:37:40Z
updated_at: 2026-08-24T20:15:45Z
---

Found 2026-08-24 while refreshing the 71 sidecars affected by the
`voice-scholarly-default` checker fix (`folio-assistant-fl5m`). The refresh
was expected to flip that one criterion; it also re-ran every other SCRIPT
criterion on those blocks at its current version, and four blocks turned out
to have been carrying **passing verdicts stamped 2026-07-13 / 2026-08-09
against older checker versions** while the current checker fails them.

None of these was caused by the voice fix. They were already true; nothing had
re-run the checker that says so.

## The four

**1. `prop:fivetwo-saddle-sum-rule` — `lean-ref-owns-decl` FAIL.**
`lean.ref` `qou:QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule` is
**also claimed by `thm:five-two-saddle-sum-rule`**. A declaration can be owned
by only one statement-bearing block; the formal graph attaches it to one of
them and the other is silently unbacked. This is the most serious of the four
and the only one that is not a prose-register issue: deciding which block owns
it is an authoring call, and until it is made, one of the two blocks' Lean
backing is fictional.

**2. `rem:markov-axioms-primitive` — `voice-author-notes-pollution` FAIL.**
`markov-axioms-primitive.md:20` opens
`**Selection note (owner ruling 2026-08-09 — convention C excised).**` in the
published prose. Per §4d that is `authorNotes` material.

**3. `prop:centered-hecke-variance-positive` — `voice-author-notes-pollution`
FAIL.** Same shape, `centered-hecke-variance-positive.md:20`:
`**Corrected 2026-08-09.** This proposition previously read
$z = 1/(q^{1/2}+q^{-1/2})$ — convention C, excised by the owner ruling of
2026-08-09 — ...`. A dated correction banner in prose.

**4. `prop:centered-hecke-variance-positive` — `voice-editorializing` FAIL.**
`...md:11`: "the variance is not **merely** positive — it **is** a Wenzl
weight." Also a `uses-editorial-hygiene` warn on the same block (one
transitively redundant `uses` edge).

Items 2-4 are exactly the class `qou-cauj` dispositioned for
`q-beta-c3-continuum-geometry`: a dated `**CORRECTION**` banner sitting in
published prose instead of `authorNotes`. The remedy there was to move the
banner and keep the content.

## Why this is a bean and not a fix in that commit

Item 1 needs an owner decision (which block keeps the declaration). Items 2-3
need the correction's substance preserved while the register moves, and item 3
carries a live convention-C/D correction whose wording matters. None is
mechanical, and none is in scope for a checker fix.

## The general point

A `.qa.json` criterion holds a HISTORY of entries, not one verdict. A stale
`pass` from July sits there looking authoritative until something re-runs the
checker — and nothing does, unless a block is edited or someone sweeps it.
`check-sidecars.sh` reports staleness only for CHANGED files, so a block that
nobody touches keeps its July verdict indefinitely. Four of 71 blocks — 6 % —
were in that state. A corpus-wide sweep would say how large the class really
is; that has not been run.

---

## RESOLVED 2026-08-24 — all four, and item 1 turned out to be determinable

### 1. `prop:fivetwo-saddle-sum-rule` — the duplicate is merged, not arbitrated

I filed this as needing an owner decision. The commit history decides it.

* **2026-08-15** `a1fcca562d` added `thm:five-two-saddle-sum-rule` to
  `mass-theory` as an **exposition** block (BEAN expo, "two more exposition
  blocks, both with lean.ref verified to resolve BEFORE committing").
* **2026-08-19** `e4279a6b6b` (bean `qou-yq50`) added
  `prop:fivetwo-saddle-sum-rule` to `appendix-qvalues`, opening:
  *"~180 probes and 33 sorry-free Lean files of 5_2 work, and **not one
  content block anywhere in the paper**."*

That sentence is the finding. The 08-19 author believed no block existed — four
days after one was added in another chapter under a slug differing only by a
hyphen (`five-two-` against `fivetwo-`). This is an accidental re-authoring, not
a deliberate pair, so it is a duplicate to merge rather than a design to
adjudicate.

**The appendix block survives, on consumers:** `fivetwo-bar-odd-arithmetic-home`,
`fivetwo-level-seven-ladder` and `fivetwo-envelope-transport` read it; nothing
reads the `mass-theory` one. It also sits in the deliberate `5_2` lane beside
`prop:fivetwo-trace-field`, and carries the bar-EVEN caveat that exists to stop
a strong bar-even result being mis-read as bar-odd progress.

**Nothing of the retired block is discarded.** Folded into the survivor: its
`cites: [zagier1986]`, its `uses` of `prop:hyperbolic-knot-shape-fields`, and
the two passages its prose had that the survivor's did not — the
volume-conjecture disclaimer (the sum rule is *not* `Vol = 3D(y_1)`, and *not*
Ohtsuki's theorem) and the shape-field contrast explaining why
`Q(sqrt-23)` keeps the `5_2` analysis off the `4_1` route.

**On `leanok`.** The retired block asserted it; the survivor stays
`not_checked`, with the reason recorded on the block. Verified here: the
declaration exists (`theorem fiveTwo_saddle_sum_rule`,
`FiveTwoComplexPentagon.lean:1865`, namespace `QOU.QBeta.FiveTwoComplexPentagon`)
and the file has no `sorry`. NOT verified: that it builds. The retired block's
`leanok` rested on a `lake env lean` run of 2026-08-15, which is not a current
build, and this container cannot produce one — see the cache note below.

### 2-4. The prose-register items

* `rem:markov-axioms-primitive` — the dated "Selection note (owner ruling ...)"
  banner is gone from the prose; the **forcing argument it carried is kept**,
  restated as mathematics ("the selection is forced by the dimension of the mass
  fibre") rather than as this remark's edit history. An `authorNotes` entry
  records that an earlier version stipulated. The convention-C comparison stays
  in the prose, because D-vs-C is mathematics and not versioning.
* `prop:centered-hecke-variance-positive` — the "Corrected 2026-08-09" banner is
  removed outright: the `.ts` `authorNotes` already said all of it. The "Open
  (2026-08-09)" note is **kept**, rewritten as a scope paragraph, because it
  gates how the statement may be read (the probabilistic reading is not
  established under D) and a reader needs that, not just an author.
* Same block, `voice-editorializing`: "not merely positive — it **is** a Wenzl
  weight" is now the plain claim.

### What the sweep of the survivor then surfaced

Three more script criteria were failing latently on
`prop:fivetwo-saddle-sum-rule` and had never been evaluated at current versions:
`cite-named-theorem` ("Ohtsuki theorem", now `[ohtsuki2016]`, which was already
in `references.ts`), `voice-editorializing` ("not merely about a structure that
might be empty"), and `wall-side-correct` (the Lean file is archimedean
throughout — `Real.log`, `Complex.arg` — with no §7c acknowledgement anywhere).
All three fixed. The §7c note is the "forced by the statement" row: `arg` and
`log` have no generic-`CommRing` form.

Only an agent `trap-em-dash` verdict of 2026-08-22 remains on that block, and
two agent verdicts on `centered-hecke-variance-positive` from 2026-07-07 —
including `da-lean-narrative-divergence`, which is **correct and known**: that
block's own `authorNotes` says the Lean sibling still carries the convention-C
statement.

### An agent verdict can go stale in the other direction too

`rem:markov-axioms-primitive` still records `trap-meta-commentary: fail` from an
**agent** on 2026-08-15, quoting *"this is where an earlier version of this
remark was weaker than the mathematics"* — a sentence this change deletes. A
script sweep cannot clear an agent verdict, so the block will keep reporting a
fixed problem until an agent re-adjudicates it. Worth knowing: the staleness
this bean is about runs both ways.

### Cost incurred: I destroyed the olean cache and restored it

Chasing `leanok`, I ran `lake build QOU.QBeta.FiveTwoComplexPentagon`. Lake
decided mathlib's URL had changed, deleted `.lake/packages/mathlib` and started
re-cloning; killing it left 278 oleans of 7268. **`lake-cache.sh status` says
this will happen** — "trace coverage is only 0% — `lake build` WILL rebuild the
rest ... rebuilding evicts the untraced neighbours" — and I ran the build
without checking status first. Fully restored (`restore --branch
lake-cache/qou-v4-24-0`, back to 7268); `--branch` is required because the
default resolves to `lake-cache/mathlib-v4-24-0`, which does not exist on
origin. The cache is dependencies-only by construction (bean
`folio-assistant-5d7z`), so no `QOU.*` module can be built or checked here, and
that is why `leanok` could not be re-earned.
