/-
# vdV Lemma 1 for the Whitehead link: generic-`t` tangle formula → Kashaev point

`WhiteheadLinkScaffold.lean` defines `whiteheadLinkKashaev N` as van der Veen's
Lemma 1 closed form at `t = e^{2πi/N}`, and that formula was CITED.  Lemma 1 in
arXiv:math/0611181 (p. 3–4) is proved in two layers:

1. the generic-`t` tangle formula (Zheng, math/0508138; vdV p. 4)
   `J_N(W_{0,1,1,0})(t) = Σ_{n<N} ([2n+1]/[N])·B(n,t)·C(n,t)`, with
   `B(n,t) = [N(2n+1)]/[2n+1]` and the clasp
   `C(n,t) = t^{(N²−1)/2+N(N−1)/2} Σ_{k<N−n} t^{−N(n+k)} ∏_{j=1}^{n}
     (1−t^{N−j−k})(1−t^{j+k})/(1−t^j)`;
2. "routine calculations" evaluating layer 1 at `t = e^{2πi/N}`.

Layer 1 is stated here as a definition in the variable `s = t^{1/2}`. Layer 2,
its value at `s = e^{πi/N}`, is derived sorry-free in the transcendental companion
`QOU/Transcendental/BraidKnotOctonion/WhiteheadLemma1RootOfUnityKashaev.lean`
(`vdvWhiteheadLinkJones_at_kashaev_point`). This file holds only the algebraic part:
the definitions and the belt-factor identity, over `ℂ` with no exponential.  So the citation now rests only on layer 1
(the tangle functions `B`, `C` and multiplicativity), not on the root-of-unity
evaluation.

One point needs care.  At the root, `[N] = 0`, so `[2n+1]/[N]·B = [N(2n+1)]/[N]`
is a `0/0`.  We use its Laurent-polynomial representative `vdvBeltFused`
(`Σ_{j≤2n} s^{N(2n−2j)}`) and prove `[N]·vdvBeltFused = [N(2n+1)]` for every
`s ≠ 0` (`vdvBeltFused_spec`).  Being a Laurent polynomial, it is the
continuous extension of the ratio through the root.
-/

import Mathlib.Data.Complex.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring

namespace QOU.Knot.FigureEightVolume

open Complex

/-- The quantum integer `[m] = (s^m − s^{−m})/(s − s⁻¹)` in `s = t^{1/2}`. -/
noncomputable def vdvQnum (s : ℂ) (m : ℤ) : ℂ := (s ^ m - s ^ (-m)) / (s - s⁻¹)

/-- Laurent-polynomial representative of `[2n+1]/[N] · B(n,t) = [N(2n+1)]/[N]`. -/
noncomputable def vdvBeltFused (s : ℂ) (N n : ℕ) : ℂ :=
  ∑ j ∈ Finset.range (2 * n + 1), s ^ ((N : ℤ) * (2 * (n : ℤ) - 2 * (j : ℤ)))

/-- vdV's clasp tangle function `C(n,t)` (with the `c + d = 1` framing factor),
    written in `s = t^{1/2}`. -/
noncomputable def vdvClasp (s : ℂ) (N n : ℕ) : ℂ :=
  s ^ (((N : ℤ) ^ 2 - 1) + (N : ℤ) * ((N : ℤ) - 1)) *
    ∑ k ∈ Finset.range (N - n), s ^ (-(2 * (N : ℤ) * ((n : ℤ) + k))) *
      ∏ j ∈ Finset.range n,
        (1 - s ^ (2 * ((N : ℤ) - ((j : ℤ) + 1) - k))) * (1 - s ^ (2 * ((j : ℤ) + 1 + k)))
          / (1 - s ^ (2 * ((j : ℤ) + 1)))

/-- vdV's generic-`t` colored Jones of the Whitehead link `W_{0,1,1,0}`. -/
noncomputable def vdvWhiteheadLinkJones (s : ℂ) (N : ℕ) : ℂ :=
  ∑ n ∈ Finset.range N, vdvBeltFused s N n * vdvClasp s N n

/-! ### The fused belt factor is the Laurent polynomial of `[N(2n+1)]/[N]` -/

theorem telescope_zpow (u : ℂ) (hu : u ≠ 0) (m : ℕ) :
    (u - u⁻¹) * ∑ j ∈ Finset.range m, u ^ ((m : ℤ) - 1 - 2 * j) = u ^ (m : ℤ) - u ^ (-(m : ℤ)) := by
  induction m with
  | zero => simp
  | succ m ih =>
    rw [Finset.sum_range_succ]
    have hshift : ∀ j ∈ Finset.range m,
        u ^ (((m + 1 : ℕ) : ℤ) - 1 - 2 * j) = u * u ^ ((m : ℤ) - 1 - 2 * j) := by
      intro j _
      rw [← zpow_one_add₀ hu]; congr 1; push_cast; ring
    rw [Finset.sum_congr rfl hshift, ← Finset.mul_sum, mul_add, ← mul_assoc,
      mul_comm (u - u⁻¹) u, mul_assoc, ih]
    have e1 : u ^ (((m + 1 : ℕ) : ℤ) - 1 - 2 * (m : ℕ)) = u ^ (-(m : ℤ)) := by
      congr 1; push_cast; ring
    rw [e1]
    have hm1 : u ^ (((m + 1 : ℕ) : ℤ)) = u * u ^ (m : ℤ) := by
      rw [← zpow_one_add₀ hu]; congr 1; push_cast; ring
    have hm2 : u ^ (-(((m + 1 : ℕ) : ℤ))) = u⁻¹ * u ^ (-(m : ℤ)) := by
      rw [← zpow_neg_one, ← zpow_add₀ hu]; congr 1; push_cast; ring
    rw [hm1, hm2]
    ring_nf

theorem vdvBeltFused_spec (s : ℂ) (hs : s ≠ 0) (N n : ℕ) :
    vdvQnum s N * vdvBeltFused s N n = vdvQnum s ((N : ℤ) * (2 * n + 1)) := by
  have hu : s ^ (N : ℤ) ≠ 0 := zpow_ne_zero _ hs
  have key := telescope_zpow (s ^ (N : ℤ)) hu (2 * n + 1)
  have hsum : vdvBeltFused s N n =
      ∑ j ∈ Finset.range (2 * n + 1),
        (s ^ (N : ℤ)) ^ (((2 * n + 1 : ℕ) : ℤ) - 1 - 2 * j) := by
    unfold vdvBeltFused
    refine Finset.sum_congr rfl fun j _ => ?_
    rw [← zpow_mul]; congr 1; push_cast; ring
  rw [hsum]
  unfold vdvQnum
  rw [div_mul_eq_mul_div]
  congr 1
  have e1 : ((s ^ (N : ℤ))⁻¹) = s ^ (-(N : ℤ)) := by rw [zpow_neg]
  rw [e1] at key
  rw [key]
  rw [← zpow_mul, ← zpow_mul]
  congr 2

end QOU.Knot.FigureEightVolume
