/-
Copyright (c) 2026 litlfred. All rights reserved.

# The principal grading g_ρ as the GS/jet-order filtration grading

The Δ_λ chirality sign is the principal (ρ) grading `g_ρ` evaluated at ζ₄:
`sgn(Δ_λ) = (−1)^{n(λ)} = q^{2n(λ)}|_{q=i}` (merged #3509/#3523/#3529), and
`Δ_λ = tr(g_ρ) = (−1)^{n(λ)}·dim(λ)` (#3537). The construction of `g_ρ` from the
drivers is the **jet-order derivation** (owner lead: the Gram-inverse / knot-operator
basis on the GB filtration):

* the QOU **Gröbner–Shirshov normal-form basis** is filtered by **word length = jet
  order**; the principal grading `g_ρ` is this jet-order grading operator;
* its **bottom degree** on `V_λ` is `n(λ) = min_{T∈SYT(λ)} maj(T)`, the classical
  **fake-degree valuation** (Steinberg / Lusztig; Macdonald I.5 — the fake degree
  `R_λ(q)=Σ_T q^{maj T}` has lowest term `q^{n(λ)}`, from `s_λ(1,q,q²,…)=q^{n(λ)}·∏…`).
  Verified computationally for λ⊢3..8 in
  `computations/deltalambda/deltalambda-grho-jet-order-derivation.witness.json`.

This file formalises the **provable** core: the principal grading `n(λ)`, its ζ₄
evaluation giving the Δ_λ sign, the sign's ±1 / bar-parity structure, the **assembly
identity** `Δ_λ = tr(g_ρ) = (−1)^{n(λ)}·dim(λ)` (magnitude `dim(λ)` taken as the #3537
input `d`, not re-derived), and the **bar-parity selection rule** (`Δ_λ` sign `= +1`/`−1`
iff `n(λ)` even/odd). The fake-degree valuation itself (`n(λ) = min maj(SYT(λ))`) is a
**published classical theorem**, cited via `-- Ref: [macdonald1995]`, not re-proved here;
a full Mathlib formalisation (SYT + major index + valuation) is a standalone effort.
Honest scope: this derives/grounds the **sign carrier** and the assembly *identity*; the
full binding *closure* (`B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` magnitude derivation + wiring) is a
further step (`docs/audits/2026-07-11-deltalambda-grho-jet-order-derivation.md`).

Generic base ring per §7c: the ζ₄ evaluation is stated over any `CommRing` with an
element `i` satisfying `i² = −1`; no archimedean structure.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Ring.Basic
import Mathlib.Data.List.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace QOU.BraidKnot.PrincipalGradingJetOrder

/-- The principal (ρ) grading `n(λ) = Σ_i (i)·λ_{i}` (0-indexed rows) = `Σ_box row(box)`
    — the co-content / principal-specialisation exponent (`s_λ(1,q,q²,…)=q^{n(λ)}·∏…`).
    Equivalently (classical) the fake-degree valuation `min_{T∈SYT(λ)} maj(T)`; see the
    module docstring and `-- Ref: [macdonald1995]`. -/
def principalGrading (l : List ℕ) : ℕ :=
  ((List.range l.length).map (fun i => i * l.getD i 0)).sum

@[simp] theorem principalGrading_nil : principalGrading [] = 0 := rfl

/-- `n([n]) = 0` for a single-row shape (all boxes in row 0). -/
@[simp] theorem principalGrading_single (n : ℕ) : principalGrading [n] = 0 := by
  simp [principalGrading]

/-- **ζ₄ evaluation of the principal grading gives the Δ_λ sign.** Over any commutative
    ring with `i² = −1`, `i^{2·n(λ)} = (−1)^{n(λ)}`. This is the algebraic core of
    `sgn(Δ_λ) = q^{2n(λ)}|_{q=i} = (−1)^{n(λ)}`: the sign is the ζ₄ (root-of-unity)
    evaluation of the principal grading. Generic base ring per §7c. -/
theorem zeta4_eval_principalGrading {R : Type*} [CommRing R] (i : R) (hi : i ^ 2 = -1)
    (l : List ℕ) : i ^ (2 * principalGrading l) = (-1 : R) ^ principalGrading l := by
  rw [pow_mul, hi]

/-- The Δ_λ sign as the ζ₄-evaluated principal grading, valued in `ℤ`. -/
def deltaSign (l : List ℕ) : ℤ := (-1) ^ principalGrading l

/-- The sign is `±1` (its square is `1`) — it is a genuine `ℤ/2` grading value. -/
theorem deltaSign_sq (l : List ℕ) : deltaSign l ^ 2 = 1 := by
  unfold deltaSign
  rw [← pow_mul, mul_comm, pow_mul]
  simp

/-- **Bar-parity of the sign carrier.** `deltaSign` lands in `{+1, −1}`; combined with
    `zeta4_eval_principalGrading` this identifies it as the ζ₄ evaluation of the
    jet-order (principal) grading — the bar-odd / ζ₄ fibre datum of the Δ_λ closure. -/
theorem deltaSign_eq_neg_one_pow (l : List ℕ) :
    deltaSign l = (-1 : ℤ) ^ principalGrading l := rfl

/-! ### Assembly: `Δ_λ = tr(g_ρ) = (−1)^{n(λ)}·dim(λ)`

Combining the **magnitude** `dim(λ)` — the ordinary dimension of `V_λ` (`#SYT(λ)`),
established as the whole magnitude of `Δ_λ` in the magnitude reduction (PR #3537) — with
the **sign carrier** `(−1)^{n(λ)}` derived here gives the assembled per-partition value
`Δ_λ = tr(g_ρ)`. The dimension enters as the abstract input `d : ℕ`; its value `dim(λ)`
is the classical #3537 result and is **not** re-derived here (taking it as a Lean
hypothesis would be a self-assuming projection). The lemmas below verify only that the
assembly **decomposes correctly**: its magnitude is exactly `d` and its sign is
`deltaSign`. Honest scope: this formalises the *assembly identity*, not the physical
binding closure `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` (still open — see the audit doc). -/

/-- The assembled `Δ_λ = tr(g_ρ)` value over a generic base ring (§7c): the
    ζ₄-evaluated principal grading `(−1)^{n(λ)}` times the magnitude `d = dim(λ)`. -/
def deltaValueRing {R : Type*} [CommRing R] (l : List ℕ) (d : ℕ) : R :=
  (-1 : R) ^ principalGrading l * (d : R)

/-- **The assembly identity at ζ₄.** Over any `CommRing` with `i² = −1`,
    `i^{2·n(λ)}·d = (−1)^{n(λ)}·d = Δ_λ`: the graded trace `tr(g_ρ)` of the principal
    grading, scaled by the magnitude `d`, is the ζ₄ evaluation. This is the ring-level
    statement of `Δ_λ = tr(g_ρ) = (−1)^{n(λ)}·dim(λ)` (#3537 magnitude × #3542 sign).
    Generic base ring per §7c. -/
theorem deltaValueRing_zeta4 {R : Type*} [CommRing R] (i : R) (hi : i ^ 2 = -1)
    (l : List ℕ) (d : ℕ) :
    i ^ (2 * principalGrading l) * (d : R) = deltaValueRing l d := by
  unfold deltaValueRing
  rw [pow_mul, hi]

/-- The assembled `Δ_λ = tr(g_ρ)` value in `ℤ`: `deltaSign λ · dim(λ)`. -/
def deltaValue (l : List ℕ) (d : ℕ) : ℤ := deltaSign l * (d : ℤ)

/-- **Magnitude projection.** `|Δ_λ| = dim(λ)` — the sign carrier leaves the magnitude
    (the #3537 dimension `d`) unchanged. -/
theorem deltaValue_natAbs (l : List ℕ) (d : ℕ) : (deltaValue l d).natAbs = d := by
  unfold deltaValue deltaSign
  rcases Nat.even_or_odd (principalGrading l) with h | h
  · rw [h.neg_one_pow]; simp
  · rw [h.neg_one_pow]; simp

/-- **Sign projection.** the assembled value factors as sign `·` magnitude. -/
theorem deltaValue_eq_deltaSign_mul (l : List ℕ) (d : ℕ) :
    deltaValue l d = deltaSign l * (d : ℤ) := rfl

/-! ### Bar-parity selection rule

The sign carrier `deltaSign λ = (−1)^{n(λ)}` is a `ℤ/2` (bar-parity) **selection rule**
keyed on the parity of the fake-degree valuation `n(λ)`: `V_λ` sits in the bar-EVEN
(symmetric, `+`) sector iff `n(λ)` is even, the bar-ODD (antisymmetric, `−`) sector iff
`n(λ)` is odd. This is the Lean form of the bar-parity Δ_λ selection rule. -/

/-- Bar-even selection: the `Δ_λ` sign is `+1` iff the fake-degree valuation `n(λ)` is even. -/
theorem deltaSign_eq_one_iff_even (l : List ℕ) :
    deltaSign l = 1 ↔ Even (principalGrading l) := by
  unfold deltaSign
  constructor
  · intro h
    rcases Nat.even_or_odd (principalGrading l) with he | ho
    · exact he
    · rw [ho.neg_one_pow] at h; norm_num at h
  · intro h; exact h.neg_one_pow

/-- Bar-odd selection: the `Δ_λ` sign is `−1` iff the fake-degree valuation `n(λ)` is odd. -/
theorem deltaSign_eq_neg_one_iff_odd (l : List ℕ) :
    deltaSign l = -1 ↔ Odd (principalGrading l) := by
  unfold deltaSign
  constructor
  · intro h
    rcases Nat.even_or_odd (principalGrading l) with he | ho
    · rw [he.neg_one_pow] at h; norm_num at h
    · exact ho
  · intro h; exact h.neg_one_pow

/- The jet-order derivation `n(λ) = min maj(SYT(λ))` (the classical fake-degree
   valuation, Steinberg/Lusztig/Macdonald I.5) is what identifies `principalGrading`
   with the bottom GS/jet-order degree of `V_λ`. It is a **published classical theorem**
   applied to the QOU Gröbner–Shirshov filtration; it is cited (`-- Ref: [macdonald1995]`)
   and verified computationally (λ⊢3..8) in the companion witness, NOT re-proved here — a
   full Mathlib formalisation (SYT + major index + valuation) is a standalone effort, and
   a Lean lemma that merely re-assumed the equality would be a vacuous self-assuming
   projection. So the SYT-level theorem lives in the audit/witness, and this file carries
   only the genuinely-provable algebraic core above. -/

end QOU.BraidKnot.PrincipalGradingJetOrder
