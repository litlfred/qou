import Mathlib.Tactic

/-!
# Formal Laurent residues: the residue of an exact form vanishes

Library home of the invariant behind `prop:sw-classical-jet-exactness` (the
content-block sibling `brings-surface/sw-classical-jet-exactness.lean` carries a
self-contained copy per the sibling convention): a local Laurent expansion is
modelled by its coefficient function `f : ℤ → R`, the **residue** is the
coefficient of `t⁻¹`, and the **termwise derivative** shifts every exponent down
by one — so the residue of a derivative is `((−1)+1)·f(0) = 0`. Iterating gives
the jet form: every positive-order classical jet is exact, hence residue-free at
every point, hence period-free on every closed cycle (the residue-sum shape of
`prop:sw-period-residue-sum`).

The model is deliberately coefficient-level: it does not encode convergence or
the curve, only the algebraic identity that kills the residues — which is the
load-bearing (b)-invariant. Everything is over a generic `CommRing R`
(§7c wall-safe; no archimedean content).

## Main results

* `fresidue_fderiv` — the residue of a derivative vanishes.
* `fresidue_jet_succ` — every positive-order jet has vanishing residue.
* `fderiv_add`, `fderiv_smul`, `fresidue_add`, `fresidue_sum` — (bi)linearity,
  so the vanishing extends to finite residue sums of exact families
  (`fresidue_sum_jet_succ`).

## References

- [leitner2026] §5-brings-surface/sw-classical-jet-exactness
-/

namespace QOU.Mathlib.FormalLaurentResidue

open scoped BigOperators

variable {R : Type*} [CommRing R]

/-- Formal residue of a local Laurent expansion, presented as its coefficient
function `f : ℤ → R`: the coefficient of `t⁻¹`. -/
def fresidue (f : ℤ → R) : R := f (-1)

/-- Termwise derivative of a formal Laurent expansion:
`(Σ c_e tᵉ)' = Σ (e+1)·c_{e+1} tᵉ`. -/
def fderiv (f : ℤ → R) : ℤ → R := fun e => (e + 1) • f (e + 1)

/-- **The residue of an exact form vanishes.** -/
theorem fresidue_fderiv (f : ℤ → R) : fresidue (fderiv f) = 0 := by
  show ((-1 : ℤ) + 1) • f (-1 + 1) = 0
  norm_num

/-- The `n`-th classical jet: `n`-fold termwise derivative (the coefficient-level
face of `X^{(n)} = dⁿX/dzⁿ` along a curve). -/
def jet (X : ℤ → R) : ℕ → ℤ → R
  | 0 => X
  | n + 1 => fderiv (jet X n)

/-- Every positive-order classical jet is exact, so its residue vanishes. -/
theorem fresidue_jet_succ (X : ℤ → R) (n : ℕ) : fresidue (jet X (n + 1)) = 0 :=
  fresidue_fderiv _

@[simp] theorem fderiv_add (f g : ℤ → R) :
    fderiv (fun e => f e + g e) = fun e => fderiv f e + fderiv g e := by
  funext e
  simp [fderiv, smul_add]

@[simp] theorem fderiv_smul (r : R) (f : ℤ → R) :
    fderiv (fun e => r * f e) = fun e => r * fderiv f e := by
  funext e
  simp [fderiv]
  ring

@[simp] theorem fresidue_add (f g : ℤ → R) :
    fresidue (fun e => f e + g e) = fresidue f + fresidue g := rfl

theorem fresidue_sum {ι : Type*} (s : Finset ι) (F : ι → ℤ → R) :
    fresidue (fun e => ∑ i ∈ s, F i e) = ∑ i ∈ s, fresidue (F i) := rfl

/-- A finite residue sum of positive-order jets vanishes — the library form of
the exactness (b)-exclusion: no residue-sum period can be sourced by classical
jets. -/
theorem fresidue_sum_jet_succ {ι : Type*} (s : Finset ι) (Xs : ι → ℤ → R) (n : ℕ) :
    ∑ i ∈ s, fresidue (jet (Xs i) (n + 1)) = 0 := by
  simp [fresidue_jet_succ]

end QOU.Mathlib.FormalLaurentResidue
