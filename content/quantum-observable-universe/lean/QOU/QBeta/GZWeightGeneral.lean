import Mathlib.Tactic

/-!
# Knot-independent Garoufalidis–Zagier weight rule, and its `5₂` instance

The merged `QOU.QBeta.GZWeightSelection` proved the weight-difference selection rule
for the **`4₁`** connections. This file abstracts that rule to its **knot-independent**
form — GZ eq. 3.7's automorphy weight `κ(σ) = 3/2·[σ trivial]` is universal (the `3/2`
is the Kashaev `N^{3/2}`-prefactor exponent for *any* knot, `⟨K⟩_N ∼ N^{3/2}e^{vN}Φ`,
GZ eq. 1.1) — and instantiates it at **`5₂`**, the non-amphichiral knot where the
bar-odd A_ω actually lives.

**Why this matters for A_ω.** The `5₂` GGM Stokes automorphisms `S±(q)` are assembled
and the integer index `Ind^{rot}_{5₂}(q) = 2·H⁺_{1,0}·H⁻_{1,0} = 1−12q+3q²+74q³+90q⁴`
is extracted (probe `qbeta_5two_stokes_barodd_index_probe.py`, GGM 2007.10190 eq. 102,
the `(σ₁,σ₁)` diagonal entry of `S⁺`). This file **certifies** — via the
knot-independent weight rule — that this index is a genuine **integer-exponent**
(`b = 0`) Stokes datum: the `5₂` geometric and conjugate saddles are both non-trivial,
so any ray between them (the A_ω ray) has weight difference `0 ∈ ℤ`, and `b = ±3/2`
would require the trivial connection as an endpoint — a *different* ray. It is the
`5₂` analogue of the merged `4₁` `weightDiff_aomega_zero`, closing the "`5₂` is the
follow-up" note of PR #4213.

Discipline: no fit; the weight *values* are the cited GZ definition, the selection
*rules* are their algebraic consequences; the only `5₂`-specific input is that the
geometric/conjugate/real saddles are non-trivial (true — they are the non-abelian
character-variety saddles, distinct from the trivial connection). Nothing wired;
`conj:algebraic-geometric-dilog-equivalence` stays open. Verified `lean`-direct
(exit 0).

-- Ref: [garoufalidis-zagier-2024] https://arxiv.org/abs/2111.06645 (SIGMA 20 (2024) 055, eq. 3.7)
-- Ref: [garoufalidis-gu-marino2021] https://doi.org/10.1007/s00220-021-04076-0 (Conj. 2; 2007.10190 eq. 102, 5₂ index)
-/

namespace QOU.QBeta.GZWeightGeneral

/-- **Knot-independent GZ automorphy weight.** For any connection type with a
`trivial`-connection predicate, `κ(σ) = 3/2` iff `σ` is trivial, else `0` (GZ eq. 3.7).
The `3/2` is the Kashaev `N^{3/2}`-prefactor exponent — universal across knots, indexed
only by triviality of the flat connection. -/
noncomputable def kappaGZ {Conn : Type*} (isTrivial : Conn → Prop)
    [DecidablePred isTrivial] (σ : Conn) : ℚ :=
  if isTrivial σ then 3 / 2 else 0

/-- The **Borel characteristic exponent** of a Stokes ray joining `σ, σ′` is the GZ
weight difference `b = κ(σ) − κ(σ′)`. -/
noncomputable def weightDiffGZ {Conn : Type*} (isTrivial : Conn → Prop)
    [DecidablePred isTrivial] (σ σ' : Conn) : ℚ :=
  kappaGZ isTrivial σ - kappaGZ isTrivial σ'

variable {Conn : Type*} (isTrivial : Conn → Prop) [DecidablePred isTrivial]

/-- **Both endpoints non-trivial ⇒ integer exponent `0`.** The A_ω-type ray
(geometric ↔ conjugate, both non-trivial) has weight difference `0 ∈ ℤ` for *every*
knot — so its Stokes constant is an integer (the DT/BPS rotated `3d`-index, GGM
Conj. 2), never a half-integer-weight modular datum. Knot-independent. -/
theorem weightDiffGZ_eq_zero_of_both_nontrivial {σ σ' : Conn}
    (h : ¬ isTrivial σ) (h' : ¬ isTrivial σ') :
    weightDiffGZ isTrivial σ σ' = 0 := by
  simp [weightDiffGZ, kappaGZ, h, h']

/-- **A half-integer exponent forces a trivial endpoint.** `b = ±3/2` can occur only
on a `σ₀ ↔ (non-trivial)` ray. So the geometric–conjugate A_ω ray (both non-trivial)
can *never* carry `±3/2` — the `β = 3/2` category error, in knot-independent form. -/
theorem weightDiffGZ_half_integer_needs_trivial {σ σ' : Conn}
    (h : weightDiffGZ isTrivial σ σ' = 3 / 2 ∨ weightDiffGZ isTrivial σ σ' = -(3 / 2)) :
    isTrivial σ ∨ isTrivial σ' := by
  by_contra hc
  push_neg at hc
  obtain ⟨hσ, hσ'⟩ := hc
  rw [weightDiffGZ_eq_zero_of_both_nontrivial isTrivial hσ hσ'] at h
  rcases h with h | h <;> norm_num at h

/-! ## The `5₂` instance -/

/-- The flat connections of `5₂` carrying the resurgent structure: the **trivial**
connection `sigma0`, and the three non-abelian saddles of the cubic trace field
`ℚ(ξ)`, `disc = −23` (one **real** saddle, and the **geometric** saddle with its
complex **conjugate** — the `disc < 0` `1+2` splitting). The GGM Stokes matrices
`S±(q)` are `3×3` over the three non-trivial saddles; the `(σ₁,σ₁) = (geometric,
geometric)` diagonal entry is the rotated index `Ind^{rot}_{5₂}` (eq. 102). -/
inductive FiveTwoConn where
  | sigma0
  | geometric
  | conjugate
  | realSaddle
  deriving DecidableEq

open FiveTwoConn

/-- Triviality predicate on the `5₂` connections: only `sigma0` is trivial. -/
def fiveTwoTrivial : FiveTwoConn → Prop
  | sigma0 => True
  | _      => False

instance : DecidablePred fiveTwoTrivial := by
  intro σ; cases σ <;> unfold fiveTwoTrivial <;> infer_instance

/-- **`5₂` A_ω ray has integer exponent `b = 0`.** The geometric saddle and its
conjugate are both non-trivial, so the `5₂` A_ω (geometric ↔ conjugate) ray has GZ
weight difference `0 ∈ ℤ` — certifying that the extracted `Ind^{rot}_{5₂}` is a genuine
integer Stokes datum, exactly as the merged `4₁` `weightDiff_aomega_zero`. -/
theorem fiveTwo_weightDiff_aomega_zero :
    weightDiffGZ fiveTwoTrivial geometric conjugate = 0 :=
  weightDiffGZ_eq_zero_of_both_nontrivial fiveTwoTrivial (by simp [fiveTwoTrivial])
    (by simp [fiveTwoTrivial])

/-- **`5₂`: `±3/2` needs the trivial connection.** Any `5₂` Stokes ray carrying the
half-integer weight `±3/2` must have `sigma0` as an endpoint — never the
geometric–conjugate A_ω ray. -/
theorem fiveTwo_half_integer_needs_trivial {σ σ' : FiveTwoConn}
    (h : weightDiffGZ fiveTwoTrivial σ σ' = 3 / 2
        ∨ weightDiffGZ fiveTwoTrivial σ σ' = -(3 / 2)) :
    σ = sigma0 ∨ σ' = sigma0 := by
  have := weightDiffGZ_half_integer_needs_trivial fiveTwoTrivial h
  rcases this with h0 | h0
  · left; cases σ <;> simp_all [fiveTwoTrivial]
  · right; cases σ' <;> simp_all [fiveTwoTrivial]

end QOU.QBeta.GZWeightGeneral
