/-!
# QOU.BraidKnot.InterfaceComposition — canonical-braid interface counts

Closed-form definitions for the inter-nucleon interface composition
of the canonical atomic braid β(Z, N) at H_{3A}(q) under canonical
pppnnn ordering.

The A − 1 inter-nucleon interfaces are classified by pair type:
  - pp interface: σ (positive Hecke gen)
  - pn interface: avg = σ − h/2
  - nn interface: σ⁻¹ (negative Hecke gen)

Closed forms:
  n_pp(Z, N) = max(0, Z − 1)
  n_nn(Z, N) = max(0, N − 1)
  n_pn(Z, N) = 1 if (Z ≥ 1 and N ≥ 1) else 0

Verified empirically on 19 atoms in
`canonical-braid-interface-composition.witness.json` (D to ¹⁶O).

LaTeX: `\\label{def:canonical-braid-interface-composition}`
-/

import QOU.Basic

namespace QOU.BraidKnot

/-- **Canonical-braid interface composition** for atom (Z, N) under
    pppnnn ordering.

    Returns the (n_pp, n_pn, n_nn) tuple with the closed-form
    definitions documented in
    `def:canonical-braid-interface-composition`. -/
structure InterfaceComposition (Z N : ℕ) where
  n_pp : ℕ
  n_pn : ℕ
  n_nn : ℕ
  n_pp_eq : n_pp = Z - 1
  n_nn_eq : n_nn = N - 1
  /-- pn interface is exactly one for any (Z, N) with both Z ≥ 1
      and N ≥ 1 (canonical pppnnn ordering has one heterogeneous
      transition).  This field encodes the indicator. -/
  n_pn_le_one : n_pn ≤ 1

namespace InterfaceComposition

/-- Total interface count = A − 1 = (Z + N) − 1. -/
theorem total_eq_A_minus_one (Z N : ℕ) (ic : InterfaceComposition Z N)
    (hZ : Z ≥ 1) (hN : N ≥ 1) (hPn : ic.n_pn = 1) :
    ic.n_pp + ic.n_pn + ic.n_nn = Z + N - 1 := by
  rw [ic.n_pp_eq, ic.n_nn_eq, hPn]
  omega

/-- **Trivial-model instance** for atomic table entries.  Returns a
    canonical witness with the closed-form n_pp, n_pn, n_nn values.

    -- Ref: [manuscript] docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md
-/
def mk (Z N : ℕ) : InterfaceComposition Z N where
  n_pp := Z - 1
  n_pn := if Z ≥ 1 ∧ N ≥ 1 then 1 else 0
  n_nn := N - 1
  n_pp_eq := rfl
  n_nn_eq := rfl
  n_pn_le_one := by
    split_ifs <;> norm_num

/-- Z↔N exchange swaps `n_pp` and `n_nn`. -/
theorem swap_z_n (Z N : ℕ) :
    (InterfaceComposition.mk Z N).n_pp =
      (InterfaceComposition.mk N Z).n_nn := by
  simp [mk]

end InterfaceComposition

end QOU.BraidKnot
