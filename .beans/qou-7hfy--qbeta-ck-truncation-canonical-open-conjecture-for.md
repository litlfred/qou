---
# qou-7hfy
title: 'qbeta_ck_truncation_canonical_conjecture is VACUOUS, not open — the statement is satisfied by a family that ignores q; verified sorry-free in Lean'
status: todo
type: task
created_at: 2026-08-12T10:23:22Z
updated_at: 2026-08-21T15:10:00Z
---

> **Was an empty auto-generated stub** (title only, no body) from 2026-08-12.
> Investigated 2026-08-21; it turns out to name a real defect, so it is filled in
> rather than scrapped. The work is **not done** — the finding is established,
> the repair is authorial.

## What the file claims

`content/quantum-observable-universe/appendix-qvalues/qbeta-ck-truncation-canonical.lean`
carries exactly one `sorry` (line 87), under the §3b conjectural-Lean convention
— *"the `sorry` IS the conjecture (not a missing proof)"*:

```lean
def CanonicalCkForm (c : ℕ → ℝ → ℝ) (f : ℕ → ℝ) : Prop :=
  ∀ k q, c k q = f k

class QbetaCkTruncationCanonicalClass (c : ℕ → ℝ → ℝ) : Prop where
  c2_proved_exact          : ∀ q, c 2 q = -1
  c3_near_match_jones_hopf : ∀ q, c 3 q = jonesHopfClassicalLimitCk   -- := -2
  canonical_ck_exists      : ∃ f : ℕ → ℝ, CanonicalCkForm c f

theorem qbeta_ck_truncation_canonical_conjecture :
    ∃ c : ℕ → ℝ → ℝ, QbetaCkTruncationCanonicalClass c := by
  sorry
```

## The defect: nothing ties `c` to Q_β, so the statement is vacuous

The theorem is existential over **all** families `ℕ → ℝ → ℝ`. No hypothesis says
`c` are the Q_β ladder coefficients — that `Q_β = Q_base·∏(1 + c_k u^k)`, or that
`c` reproduces any anchor. So a family constant in `q` discharges every field,
and `CanonicalCkForm` (which just says `c` does not depend on `q`) is satisfied by
construction rather than proved.

**Verified, not asserted.** Definitions replicated verbatim and the theorem proved
with no `sorry` (Lean 4.24.0, Mathlib, `lake env lean`):

```lean
def trivialCk : ℕ → ℝ → ℝ :=
  fun k _ => if k = 2 then -1 else if k = 3 then -2 else 0

theorem conjecture_is_trivial :
    ∃ c : ℕ → ℝ → ℝ, QbetaCkTruncationCanonicalClass c := by
  refine ⟨trivialCk, ?_, ?_, ?_⟩
  · intro q; norm_num [trivialCk]
  · intro q; norm_num [trivialCk, jonesHopfClassicalLimitCk]
  · exact ⟨fun k => trivialCk k 0, fun _ _ => rfl⟩
```

`#print axioms conjecture_is_trivial` →
`[propext, Classical.choice, Quot.sound]` — **no `sorryAx`**.

So the `sorry` at line 87 is not an open conjecture. It is a one-line proof
nobody wrote, guarding a statement with no content about Q_β.

## Two consequences, and they point opposite ways

1. **Do NOT discharge the `sorry`.** Proving it is easy and would be actively
   harmful: it would stamp "theorem" on a vacuity and retire a tracked open item
   without any mathematics happening. The `sorry` is currently the only thing
   signalling that something is unfinished here.
2. **The statement must be strengthened before it is proved.** A non-vacuous form
   has to bind `c` to the ladder it claims to describe — minimally, quantify over
   families satisfying a Q_β-reconstruction hypothesis
   (`∀ q, Q_β q = Q_base q * ∏ k, (1 + c k q * u q ^ k)`) and *then* assert an
   anchor-independent closed form exists. As written, `canonical_ck_exists` is
   the only field with conjectural content and it is discharged by fiat.

## The third instance of one pattern

Same defect class as the two already recorded on this channel:

| # | site | shape |
|---|---|---|
| 1 | `q-beta-c-2-eq-neg-one-structural.lean` | `by ring` over an arbitrary `CommRing` — proves `1 − b²ℏ⁴ = 1 − (bℏ²)²`, i.e. a change of variable |
| 2 | `qbeta_ck_cache.py` c_3 extraction | `c_3 := (Q_codata/Q_prev − 1)/u³` makes `Q_N3 ≡ Q_codata`, so the `EPS_RESIDUAL` "convergence" guard is a tautology |
| 3 | **this bean** | `∃ c, …` with `c` unconstrained — satisfied by a family that ignores the substrate |

In all three a Lean/numeric artefact carries a label ("PROVED", "converged",
"open conjecture") that the artefact's own content does not support. Worth adding
as a row to `docs/audits/2026-08-15-detector-blindness-taxonomy.md`: **a
conjecture whose existential is unconstrained is indistinguishable, to every
detector and to the manifest, from one that is open.** The `sorry` count, the
open-conjecture manifest, and the §3b convention all read this file as healthy.

## Relation to other beans

- `qou-cds1` (ACTIVE) — re-derive the ladder under D. This is the Lean statement
  of the thing cds1 is re-deriving; a strengthened version is what its result
  should eventually discharge.
- `qou-a613` — the sidecar/doc-contract defects around the same ladder.
- `qou-rwhj` — prunes Option E as the 1ppQ lever on the ground that the ladder is
  C-frame-unmoored under D; consistent with this, since the vacuous conjecture
  cannot constrain anything either.

## Not done here

The strengthening is a mathematical modelling decision about how to state the
Q_β-reconstruction hypothesis, on a channel with a documented six-entry
flip-flop history. Left `todo` and unclaimed.
