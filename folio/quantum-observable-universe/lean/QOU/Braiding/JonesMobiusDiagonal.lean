import Mathlib.Algebra.Group.Basic


/-!
# QOU.Braiding.jones_mobius_diagonal — Jones polynomial as the Möbius contact term

The fundamental ($N = 2$) Jones polynomial is the diagonal / contact datum of
the categorical Möbius two-point kernel, and the categorical Möbius energy is
the off-diagonal (renormalized) remainder.  Hence the fundamental Jones data
embeds into the Möbius two-point data as its self-energy / contact term.

LaTeX label: `lem:jones-mobius-diagonal`

## Structure

The two categorical facts are recorded as class fields:

1. `contact_is_markov` — the kernel's diagonal contact coefficient is the
   fundamental Markov trace (`lem:mobius-energy-frobenius-kernel` restricted to
   the diagonal, identified via `thm:jones-markov-trace`);
2. `renormalization` — the Möbius energy is the regularized two-point value
   minus the diagonal contact (Hadamard finite part).

The **embedding** conclusion `markov_eq_mobius_contact` is then *proved* (no
`sorry`): the fundamental Jones polynomial equals the term the Möbius
renormalization subtracts.  The base ring is generic (`AddCommGroup`) since the
renormalization is an additive identity (AGENTS.md §7c base-ring convention);
it specialises to `R_q = ℤ[q, q⁻¹]` and to `ℝ`.

## References

- [freedman1994] https://doi.org/10.2307/2946626
- [kashaev1997], [murakami-murakami2001] (coloured-trace / volume context)
- [leitner2026] climax-volume-mass/jones-mobius-diagonal
-/

namespace QOU.Braiding

/-- Abstract data for the Jones–Möbius diagonal identity over a base ring `R`.
    `R` is generic (the renormalization is an additive identity, §7c). -/
class JonesMobiusDiagonal (R : Type*) [AddCommGroup R] where
  /-- Fundamental ($N = 2$) Markov trace `tr_M(ρ(β_K))`; its value is the Jones
      polynomial `J_K`. -/
  markovTrace : R
  /-- Diagonal contact coefficient of the categorical Möbius kernel
      `tr(Δ(ϱ(s)) ⊗ Δ(ϱ(t)))` — the regularized residue on `s = t`. -/
  contact : R
  /-- Off-diagonal (renormalized) categorical Möbius energy `E_cat(ϱ)`. -/
  mobiusEnergy : R
  /-- Regularized two-point value: the full kernel integral over
      `S¹ × S¹ ∖ diag` with the universal singular part removed (finite part). -/
  twoPointReg : R
  /-- **(Diagonal = Jones).** The kernel's contact coefficient is the
      fundamental Markov trace — the coincidence restriction of
      `lem:mobius-energy-frobenius-kernel`, identified via
      `thm:jones-markov-trace`. -/
  contact_is_markov : contact = markovTrace
  /-- **(Renormalization).** The Möbius energy is the regularized two-point
      value minus the diagonal contact (Hadamard finite part). -/
  renormalization : mobiusEnergy = twoPointReg - contact

namespace JonesMobiusDiagonal

variable {R : Type*} [AddCommGroup R] [JonesMobiusDiagonal R]

/-- **Lemma (Jones polynomial = Möbius contact term).**
    The fundamental Jones polynomial (Markov trace) is exactly the diagonal
    self-energy subtracted by the Möbius renormalization:
    `J_K = twoPointReg − E_cat`.  The fundamental Jones data therefore embeds
    into the Möbius two-point data as its contact / diagonal term; the converse
    map loses the off-diagonal fusion content `Δ(e_λ) = Σ N^λ_{μν} e_μ ⊗ e_ν`. -/
-- Ref: [freedman1994], [leitner2026] climax-volume-mass/jones-mobius-diagonal
theorem markov_eq_mobius_contact :
    (markovTrace : R) = twoPointReg - mobiusEnergy := by
  have hr : (mobiusEnergy : R) = twoPointReg - contact := renormalization
  have hc : (contact : R) = markovTrace := contact_is_markov
  rw [hr, hc, sub_sub_cancel]

end JonesMobiusDiagonal

end QOU.Braiding
