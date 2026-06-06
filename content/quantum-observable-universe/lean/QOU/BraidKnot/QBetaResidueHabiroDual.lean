import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring

/-!
# Q_β residue-A Habiro element: the bar-ODD dual of α_EM

The α_EM next-order factor `H = [2]_q·(1 − h²α)` (`alpha-em-habiro-bar-involution`,
PR #1511) is **bar-EVEN** — a fixed point of the bar involution `q ↦ q⁻¹` —
with a modular **zero at ζ₄** (`[2]_q = q + q⁻¹` vanishes there). The α_EM block
records that the **Q_β analogue** "whose trace difference is *not* a bar fixed
point … required a separate cancellation analysis", and that it carries a
modular **pole at ζ₄** — "the exact structural dual" of α_EM's zero.

Two independent results this session pin the Q_β residue (the `c_3` source) to
the **bar-ANTIsymmetric** sector:
- PR #1900: the c_k-recursion kernel's leading coefficient `a_1 = −c_3 = √2·Φ₂`
  is bar-odd;
- PR #1907: the on-main `α_eff = (z−1)·h/2` is bar-odd (`h = q − q⁻¹` bar-odd).

This file formalises the residue element's **structure** as the explicit dual
of α_EM, at the fibre level (generic `CommRing`, `q`/`qi` independent, bar = the
swap `q ↔ qi`; no reality, no archimedean evaluation — per CLAUDE.md
"Im(q) fibre vs observable"). The bar-EVEN generator is `[2]_q = q + qi`; the
bar-ODD generator is `h = q − qi`. The residue **numerator** `N = h·(1 − h²α)`
is bar-odd; the residue element `F = N / [2]_q` has a **pole** exactly at the
`[2]_q` zero (the ζ₄ locus), which is characterised here without leaving
`CommRing` by evaluating at the bar-antifixed locus `qi = −q` (`[2]_q = 0`,
`N ≠ 0`).

This is a **structural** statement (parity + pole locus). It does NOT claim the
full `F`, the archimedean evaluation `τ(F) = c_3`, or any `c_3` value — those
remain the KLR/SW-residue kernel frontier
(`docs/scope/2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`).

LaTeX label: `prop:qbeta-residue-habiro-dual`

## References
- α_EM bar-even Habiro element (the dual partner): `alpha-em-habiro-bar-involution` (PR #1511)
- bar-odd kernel parity: PR #1900; bar-odd `α_eff`: PR #1907
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.BraidKnot.QBetaResidueDual

variable {R : Type*} [CommRing R]

/-- bar-EVEN generator `[2]_q = q + qi` (the α_EM prefactor; its zero locus is
the ζ₄ pole locus of the dual). -/
def bracketTwo (q qi : R) : R := q + qi

/-- bar-ODD Hecke differential `h = q − qi`. -/
def heckeDiff (q qi : R) : R := q - qi

/-- The Q_β residue-A **numerator** `N = h·(1 − h²α)` — the bar-ODD dual of the
α_EM factor `[2]_q·(1 − h²α)`. The residue element is `F = N / [2]_q` (pole at
the `[2]_q` zero). -/
def residueNum (q qi α : R) : R := heckeDiff q qi * (1 - heckeDiff q qi ^ 2 * α)

/-- **`[2]_q` is bar-EVEN** — invariant under the swap `q ↔ qi`. -/
theorem bracketTwo_bar_even (q qi : R) :
    bracketTwo qi q = bracketTwo q qi := by
  unfold bracketTwo; ring

/-- **`h` is bar-ODD** — flips sign under the swap `q ↔ qi`. -/
theorem heckeDiff_bar_odd (q qi : R) :
    heckeDiff qi q = -(heckeDiff q qi) := by
  unfold heckeDiff; ring

/-- **The Q_β residue numerator is bar-ODD**: `N(q⁻¹) = −N(q)`. This is the
structural complement of α_EM's `alphaEmHabiro_bar_invariant` (bar-EVEN): the
Q_β residue lives in the bar-ANTIsymmetric sector (PR #1900, PR #1907), which
is exactly why it required a separate cancellation analysis rather than a
Habiro-fixed-point identification. -/
theorem residueNum_bar_odd (q qi α : R) :
    residueNum qi q α = -(residueNum q qi α) := by
  unfold residueNum heckeDiff; ring

/-- **`[2]_q` vanishes at the bar-antifixed (ζ₄) locus `qi = −q`** — i.e.
`q + q⁻¹ = 0`. Since `[2]_q` is a *factor* of α_EM, this is precisely α_EM's
modular **zero at ζ₄**. -/
theorem bracketTwo_zero_at_zeta4 (q : R) :
    bracketTwo q (-q) = 0 := by
  unfold bracketTwo; ring

/-- **The Q_β residue numerator is NON-zero at the ζ₄ locus**:
`N(q, −q) = 2q·(1 − 4q²·α)`. Combined with `bracketTwo_zero_at_zeta4`, the
element `F = N / [2]_q` has a **pole** exactly where α_EM has its zero — the
structural dual recorded in the α_EM block. (Generically nonzero; the only
degeneracies are the trivial `q = 0` or the tuned `α = 1/(4q²)`.) -/
theorem residueNum_at_zeta4 (q α : R) :
    residueNum q (-q) α = (2 * q) * (1 - (2 * q) ^ 2 * α) := by
  unfold residueNum heckeDiff; ring

/-- **Pole/zero duality, packaged.** At the ζ₄ locus `qi = −q`: the α_EM factor
`[2]_q` is zero while the Q_β residue numerator `N` equals `2q(1 − 4q²α)`. So
`F = N/[2]_q` is singular exactly where α_EM vanishes — `0` and `pole` are the
two faces of the same `[2]_q` factor, in the bar-even (α_EM) and bar-odd (Q_β)
sectors respectively. -/
theorem residue_pole_dual_to_alphaEm_zero (q α : R) :
    bracketTwo q (-q) = 0 ∧ residueNum q (-q) α = (2 * q) * (1 - (2 * q) ^ 2 * α) :=
  ⟨bracketTwo_zero_at_zeta4 q, residueNum_at_zeta4 q α⟩

end QOU.BraidKnot.QBetaResidueDual
