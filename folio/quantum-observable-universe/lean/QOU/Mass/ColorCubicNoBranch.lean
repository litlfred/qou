/-
Copyright (c) 2026 litlfred. All rights reserved.

# No single-valued algebraic branch: the S₃ obstruction (W1)

W1 brick (bean `qou-d8de`). The witness `computations/qbeta/c3_w1_cover_monodromy.witness.json`
computes that the color-cubic sheet cover has **full S₃ monodromy** (cubic irreducible over
`ℂ(z)`, `branchSextic` squarefree with 6 branch points, disc not a square). The structural
consequence relevant to `D_q` is: **there is no single-valued algebraic branch** — no
root of the cubic in the base field — so the prolongation `D_q` cannot be a single-valued
algebraic operator on the base; it lives on the 3-sheeted cover.

This file proves the general algebraic fact underlying that consequence: **an irreducible
polynomial of degree > 1 over a field has no root in the field.** Applied to the color
cubic over `ℂ(z)` (irreducible per the witness), it yields "no single-valued rational
branch". The irreducibility itself is the computed input (not re-proved in Lean); the
theorem here is the honest bridge from it to the no-branch obstruction.

**Scope.** The general no-root lemma + the conditional no-branch corollary (conditional on
irreducibility, the computed W1 input). Sorry-free. No fit; nothing wired. The S₃
identification is the witness's; this is its permanent algebraic consequence.

-- Ref: [leitner2026] docs/audits/2026-08-01-branch-selection-birkhoff-connection-matrix.md (W1)
-/
import Mathlib.Algebra.Polynomial.Div
import Mathlib.Algebra.Polynomial.Eval.Irreducible

namespace QOU.Mass.ColorCubicNoBranch

open Polynomial

variable {K : Type*} [Field K]

/-- **An irreducible polynomial of degree > 1 over a field has no root.** A root `a` gives
`(X − C a) ∣ p`; since `X − C a` is not a unit and `p` is irreducible, `p` is associate to
`X − C a`, forcing `natDegree p = 1` — contradicting `1 < natDegree p`. -/
theorem no_root_of_irreducible {p : K[X]} (hp : Irreducible p) (hdeg : 1 < p.natDegree)
    (a : K) : p.eval a ≠ 0 := by
  intro hroot
  have hdvd : (X - C a) ∣ p := dvd_iff_isRoot.mpr hroot
  obtain ⟨c, hc⟩ := hdvd
  rcases hp.isUnit_or_isUnit hc with hu | hu
  · -- X - C a is not a unit (natDegree 1 ≠ 0)
    have := natDegree_eq_zero_of_isUnit hu
    rw [natDegree_X_sub_C] at this
    exact one_ne_zero this
  · -- c is a unit ⇒ natDegree p = natDegree (X - C a) = 1, contradicting 1 < natDegree p
    have hcdeg : c.natDegree = 0 := natDegree_eq_zero_of_isUnit hu
    have hpne : p ≠ 0 := hp.ne_zero
    have hXne : (X - C a) ≠ 0 := X_sub_C_ne_zero a
    have : p.natDegree = (X - C a).natDegree + c.natDegree := by
      rw [hc, natDegree_mul hXne (fun h => by simp [h] at hc; exact hpne hc)]
    rw [natDegree_X_sub_C, hcdeg, add_zero] at this
    rw [this] at hdeg
    exact absurd hdeg (lt_irrefl 1)

/-- **No single-valued algebraic branch** of the color cubic (conditional on its computed
irreducibility over the base field). If the cubic `C` is irreducible and has degree > 1,
no element of the field is a root — i.e. there is no single-valued branch section. This is
the permanent consequence of the witness's `monodromy = S₃`. -/
theorem no_branch_section {C : K[X]} (hirr : Irreducible C) (hdeg : 1 < C.natDegree) :
    ¬ ∃ a : K, C.eval a = 0 := by
  rintro ⟨a, ha⟩
  exact no_root_of_irreducible hirr hdeg a ha

end QOU.Mass.ColorCubicNoBranch
