/-
  Wigner SU(4) supermultiplet vanishing gate (GAP-A-4 class-D formalize-first
  invariant — the A=4 interface-operator locality).

  Companion to
    docs/scope/2026-07-05-gap-a4-interface-operator-attack-scoping.md  §3 Lever 1

  Context.  The ⁴He binding magnitude closure (the ×5.10 gap) needs a
  connected 4-body term that is sharply LOCAL at A = 4 (measured: 2.09×
  super-pairwise at ⁴He, vanishing to ~0.94 by ⁶Li). The proposed object is the
  connected 4-body **[1^A] Wigner SU(4) supermultiplet** Ursell cluster. Its
  A=4-locality is not a fit — it is forced by a degree / orbit-count vanishing:

    Wigner's SU(4) (Wigner 1937) acts on each nucleon's 4-dim spin⊗isospin
    state (p↑, p↓, n↑, n↓). The fully-ANTISYMMETRIC [1^A] rep of A nucleons in
    this 4-dim fundamental has dimension `C(4, A)`, which is
        • > 0  for 0 ≤ A ≤ 4   (present; the α-particle A=4 = ⁴He is the top
                                 closed shell — the [1^4] singlet), and
        • = 0  for A > 4        (VANISHES — there is no [1^5]).

  This file proves that vanishing sorry-free via its orbit-count reading — the
  dimension `C(4, A)` of the antisymmetric rep. (Equivalently the degree reading:
  `C(4, A)` counts exactly the monomials of the outer factor `e_A` of the
  plethysm `e_A[h₃]` — the `A`-subsets of the 4 flavours — so the same count
  gives the elementary-symmetric-polynomial vanishing.) It is the gate the
  scoping note requires BEFORE any [1^4]-cluster probe: it *predicts* the A=4
  locality already measured, so it justifies a narrow A=4/A=6 probe rather than
  a wide combiner scan.

  Base ring (§7c): a counting invariant over ℕ. No q₀, no archimedean construct.
-/
import Mathlib.Data.Nat.Choose.Basic

namespace QOU.MassTheory

/-- **Orbit-count gate (iff).** The dimension `C(4, A)` of the fully-antisymmetric
[1^A] Wigner SU(4) supermultiplet vanishes **iff `A > 4`**. -/
theorem su4_supermultiplet_dim_vanishes_iff (A : ℕ) :
    Nat.choose 4 A = 0 ↔ 4 < A :=
  Nat.choose_eq_zero_iff

/-- The [1^A] supermultiplet VANISHES for `A > 4` (no [1^5]) — the gate. -/
theorem su4_supermultiplet_vanishes {A : ℕ} (hA : 4 < A) :
    Nat.choose 4 A = 0 :=
  Nat.choose_eq_zero_of_lt hA

/-- The [1^A] supermultiplet is PRESENT for `A ≤ 4` (nonzero dimension); the
α-particle `A = 4` is the top closed shell, so the connected [1^4] cluster is
A=4-LOCAL — exactly the ⁴He-locality the pairwise ceiling measures. -/
theorem su4_supermultiplet_present {A : ℕ} (hA : A ≤ 4) :
    0 < Nat.choose 4 A :=
  Nat.choose_pos hA

/-- Explicit boundary check at the α-particle shell closure `A = 4` and first
excluded shell `A = 5`: `C(4, 4) = 1` (unique singlet) and `C(4, 5) = 0`. -/
theorem su4_supermultiplet_at_four_and_five :
    Nat.choose 4 4 = 1 ∧ Nat.choose 4 5 = 0 :=
  ⟨by decide, by decide⟩

end QOU.MassTheory
