# Self-assuming-projection triage — the 201 `§3b-cond` candidates

**Date:** 2026-06-18
**Branch:** `claude/kind-wozniak-i1vex4`
**Predecessor:** [`2026-06-18-lean-vacuity-recall-fix-and-drain-queue.md`](2026-06-18-lean-vacuity-recall-fix-and-drain-queue.md) ([PR #2462](https://github.com/litlfred/qou/pull/2462)) — the recall-fix that took this category from 22 → 201.
**Scanner / witness:** [`lean-vacuity-axiom-audit.ts`](../../content/pipeline/lean-vacuity-axiom-audit.ts) → [`2026-06-17-lean-vacuity-axiom-audit.json`](2026-06-17-lean-vacuity-axiom-audit.json) (the 201-candidate refreshed witness from #2462).
**Sidecar:** [`2026-06-18-self-assuming-projection-triage.json`](2026-06-18-self-assuming-projection-triage.json) — full per-candidate verdict (file · line · decl · pattern · verdict).

This **drains queue item Q1** of the predecessor doc — *read-only* triage of the
201 `proof-no-self-assuming-projection` candidates into **degenerate**
(needs restate-or-demote, a claim-change) vs **legitimate** (the valid
`§3b-cond` conditional-class pattern, a scanner false-positive). It does **not**
restate or demote anything — those are claim-changes gated on owner sign-off and
a working Lean toolchain (both unavailable this session). It turns the
predecessor's *count* into an actionable per-block ledger for the eventual
`/integration-backlog proof` campaign.

## Verdict

| | count | disposition |
|---|---:|---|
| **degenerate — field-projection** | 114 | restate class to carry *hypotheses* + derive (`§3b-cond` item 5), or demote to `remark` |
| **degenerate — tuple-split** | 85 | same |
| **legitimate** | 2 | valid iff-from-directions; **scanner false-positive** — recommend exempting (see §4) |
| **total** | **201** | **199 degenerate / 2 legitimate** |

99 % of the recall-expanded category is genuinely degenerate. The two
false-positives are a precision gap in the scanner, not in the corpus.

## 1. Field-projections (114) are degenerate *by construction*

A `field-projection` hit is, by the scanner's definition
([`lean-vacuity-axiom-audit.ts:438`](../../content/pipeline/lean-vacuity-axiom-audit.ts)),
a body matching `/^([a-z][\w']*)\.([A-Za-z_][\w']*)\s*$/` — i.e. a **bare**
single projection `ctx.field` with no application and no deriving tactic
(`DERIVES` already filters out `Iff.intro`, `constructor`, `linarith`,
`obtain`, … before this point), whose field name matches `CONCLUSION_FIELD`
(`claim_*`, `*_iff`, `is_*`, `holds`, …).

For

```lean
theorem foo [ctx : FooContext] : P := ctx.claim_foo
```

to typecheck, `ctx.claim_foo` must have type defeq `P`. So the class field
`claim_foo : P` **carries the theorem's conclusion verbatim**, and the theorem
"proves" it by projection. That is exactly the defect `§3b-cond` item 5 names:

> *A class that carries the block's own conclusion as a field, with a "theorem"
> that merely projects it (`:= ctx.claim_foo`), is a vacuous self-assuming
> projection.*

This is a typing argument, not a heuristic: **all 114 are degenerate**. There is
no body-reading subtlety because the body is a single bare field of
conclusion type. The honest fix per item 5 is to restate the class so its fields
are the *sub-hypotheses* of the proof chain and have the theorem *compose* them
(the verified exemplar is
[`q_bkm_criterion.lean`](../../content/quantum-observable-universe/lean/QOU/FluidDynamics/q_bkm_criterion.lean)),
or — where no honest derivation exists — demote `theorem → conjecture`.

## 2. Tuple-projections (87): 85 degenerate-split, 2 legitimate

A `tuple-projection` body is `⟨ctx.a, ctx.b, …⟩` (all fields from the *same*
instance, no deriving tactic). The anonymous constructor `⟨…⟩` is **not** in the
scanner's `DERIVES` regex, so it is flagged regardless — but `⟨_, _⟩` is exactly
how one *derives* an `Iff` (`Iff.intro`) or an `Exists`. So this pattern is
genuinely two populations:

- **degenerate-split** — conclusion is a top-level `∧`/`∃` whose conjuncts are
  carried verbatim as class fields: `theorem : P ∧ Q := ⟨ctx.p, ctx.q⟩` with
  `ctx.p : P`, `ctx.q : Q`. The class still carries the conclusion (just split),
  so it is self-assuming. These very often name the fields `claim_i_*`,
  `claim_ii_*`, … — a reliable tell.
- **legitimate** — conclusion is a top-level `↔` (or `→`) **derived** from class
  fields that are the *directions / sub-implications*, not the conclusion:
  `theorem : A ↔ B := ⟨ctx.fwd, ctx.bwd⟩` with `ctx.fwd : A → B`,
  `ctx.bwd : B → A`. The constructor does real work; the class carries
  hypotheses. This is the valid `§3b-cond` pattern.

### Pilot (6 hand-read)

| decl | conclusion | body | verdict |
|---|---|---|---|
| `acoustic_horizon_regularity` | `A ≠ 0 ∧ 0 ≤ T00` | `⟨ctx.nondegenerate, ctx.energy_condition⟩` | degenerate-split |
| `borromean_hopf_energy_crossover` | 3-way `∧` | `⟨ctx.claim_i_*, ctx.claim_ii_*, ctx.claim_iii_*⟩` | degenerate-split |
| `joint_tower_sdp_confinement` | `∧` referencing `ctx.claim_i_*` | `⟨ctx.claim_i_*, …⟩` | degenerate-split |
| `hecke_mass_trace` | 2-way `∧` of equalities | `⟨ctx.…, ctx.…⟩` | degenerate-split |
| `neutron_qvalue_symbolic` | 4-way `∧` | `⟨ctx.claim_i_*, …, ctx.claim_iv_*⟩` | degenerate-split |
| `q_bkm_criterion` | `extendsSmoothly ↔ vorticityIntegralFinite` | `⟨ctx.bkm_necessity, ctx.bkm_continuation⟩` | **legitimate** |

### Mechanized sweep (all 87)

Classifier: top-level `↔` in the conclusion (parenthesized groups stripped, so a
`↔` *nested inside a conjunct* does not count) **and** no `.claim_` field in the
body → legitimate; else degenerate-split. This correctly rejects
`borromean_hopf_energy_crossover` (whose `↔` is inside its third conjunct) and
yields exactly **2 legitimate**, **85 degenerate-split**. Both legitimate cases
were then hand-confirmed:

- [`q_bkm_criterion.lean:69`](../../content/quantum-observable-universe/lean/QOU/FluidDynamics/q_bkm_criterion.lean) — class fields `bkm_necessity : extendsSmoothly → vorticityIntegralFinite`, `bkm_continuation : vorticityIntegralFinite → extendsSmoothly`; body `⟨…⟩` is `Iff.intro`. ✓
- [`ns_obstruction_tower.lean:46`](../../content/quantum-observable-universe/lean/QOU/FluidDynamics/ns_obstruction_tower.lean) — class fields `obstruction_forces_singular : (∃ n, res_sigma n ≠ 0) → is_NS_singular`, `singular_exhibits_obstruction : is_NS_singular → (∃ n, res_sigma n ≠ 0)`; body `⟨…⟩` is `Iff.intro`. ✓

> **Caveat (honest scope of the sweep).** The classifier is a *structural*
> heuristic on text, not a Lean check. It is conservative for the `↔` pattern
> but does **not** attempt to catch a legitimate `∃`-derivation
> (`⟨ctx.witness, ctx.proof⟩` where `witness` is data and `proof` a genuine
> hypothesis) — if any exist among the 85, they would currently read as
> degenerate-split. None surfaced in the pilot, but per-block confirmation of
> the 85 is part of the backlog campaign (§5), where each restate is Lean-checked
> anyway. The two `↔` cases are the only ones asserted legitimate here.

## 3. Degenerate batches (199) — for the backlog campaign

Per chapter-tree, sized for `/integration-backlog proof`'s ≤ 49-file Gemini
limit. Full per-candidate rows in the [sidecar JSON](2026-06-18-self-assuming-projection-triage.json).

| tree | degenerate |
|---|---:|
| `BraidKnot` | 33 |
| `Archimedean` | 23 |
| `ParticleInteractions` | 19 |
| sibling-`.lean` (under chapter dirs, not `lean/QOU/`) | 13 |
| `FluidDynamics` | 9 |
| `AlgebraicSubstrate` / `Braiding` / `BraidsAndKnots` / `Torsion` | 7 each |
| `Molecular` / `Observations` / `QuantumObservableUniverse` | 6 each |
| `AppendixSurreals` / `BraidsKnots` / `LiftingDescent` | 5 each |
| `ArchimedeanUniverse` / `Information` / `Interactions` / `WedderburnMass` | 4 each |
| `HadronicMass` / `TopologicalMass` | 3 each |
| `Brings` / `Experimental` | 2 each |
| 9 misc trees | 1 each |
| **total** | **199** |

`claim_*`-named field/conjunct projections dominate, so a batch is mostly the
same mechanical restate — but each is a **claim-change** (§5).

## 4. Scanner precision-fix — ✅ landed in #2462

> **Update (2026-06-18):** implemented and **merged** in #2462 (the scanner is
> modified there, so the fix lives with it rather than diverging a `main`-forked
> branch). The scanner now exempts a two-field tuple-projection whose
> conclusion's top-level connective is `↔` with
> `exempt_reason: "legitimate iff-from-directions conditional-class"`; both cases
> are auto-exempt and the live counts are **199 self-assuming / 48 exempt**. This
> §4 records the original recommendation and its resolution.

The 2 legitimate cases are scanner false-positives: the `DERIVES` filter misses
the anonymous `Iff.intro` constructor `⟨ctx.fwd, ctx.bwd⟩` for a **top-level
`↔`** conclusion. A precision-fix — exempt a tuple-projection whose conclusion's
top-level connective is `↔` and whose two fields are the directions — clears
both and prevents the pattern recurring. Because the scanner lives on
**#2462** (modified there by the recall fix), this change belongs on that branch,
not on a branch forked from `main` (which would diverge the scanner). It is
flagged here as a one-line follow-up; this triage branch deliberately does **not**
touch the scanner.

## 5. What this does *not* do (and why)

This is a **read-only** catalog. The actual remediation of the 199 — restate each
degenerate class to carry hypotheses + derive the conclusion, or demote
`theorem → conjecture` — is **out of scope this session** because each item:

1. **Changes a `theorem` claim** → owner sign-off required
   (CLAUDE.md `§3b-cond` item 5; `/integration-backlog proof` recipe-4).
2. **Needs `lake build` / `lean`-direct verification** of the restated proof →
   the Lean toolchain is unavailable in this sandbox (elan cannot reach
   `release.lean-lang.org`).

The right vehicle is `/integration-backlog proof` over the §3 batches as small
per-chapter PRs, each with the author in the loop on the claim-changes. This
catalog is its input ledger.

## Verification

- Triage is derived purely from the #2462 witness (201 candidates) + read-only
  reads of the flagged `.lean` files; no `.lean`, `.ts`, or scanner file was
  modified by this branch.
- Re-derive: `python3` over [`2026-06-17-lean-vacuity-axiom-audit.json`](2026-06-17-lean-vacuity-axiom-audit.json)
  filtering `category == "proof-no-self-assuming-projection"` reproduces
  114 field / 87 tuple; the 2 legitimate are the top-level-`↔` cases listed in §2.
