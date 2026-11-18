/-
  Keystone bridge C1 ↔ binding module: the NORMALIZED binding OGF satisfies the
  PROVED q-lift kernel.

  The Tier-1 keystone (`conj:binding-manybody-eq-jet-filtration` /
  `conj:qdifference-kernel-prolongation-symbol`) claims the proved confluent
  q-lift kernel C1
      classical:  (n+2)·b_{n+2} = b_{n+1} + b_n        (`normalized_classical_kernel_exists`)
      q-lift:     [n+2]_q·b_{n+2} = b_{n+1} + b_n       (`qlift_normalized_kernel_exists`)
  is the generating structure of the BINDING series. The obstacle is a
  NORMALIZATION mismatch between the two proved objects:

    * the C1 carrier proved so far is `b_n = f_n/[n]_q!`  (q-factorial normalized;
      classically `f_n/n!`, the involution EGF coefficient), while
    * the binding PERIOD is `a_D^{(n)} = f_n/n`  (`sw-classical-jet-exactness`;
      the `q=1` value of `S(n)=Σ_{λ⊢n} dim_q λ`, `BindingGevreyHalf`), so the
      body term is `B_n = m_e·f_n/n`.

  THE CRUX, worked exactly. `B_n/N(n) = b_n` forces
      m_e·f_n/(n·N(n)) = m_e·f_n/n!   ⟺   n·N(n) = n!   ⟺   N(n) = (n−1)!.
  So the UNIQUE fixed normalizer is the (q-)Borel/factorial strip
      classical:  N(n) = (n−1)!            (`period_carrier_strip`)
      q-lift:     N_q(n) = [n−1]_q! = qfact q (n−1).
  Under it the normalized binding OGF is *exactly* the C1 carrier and therefore
  satisfies the proved kernel — the constant m_e cancels (the kernel is linear
  homogeneous). Both legs are discharged sorry-free below
  (`keystone_bridge_binding_classical`, `keystone_bridge_binding_qlift`),
  concretely for the involution numbers (`keystone_bridge_involution`).

  DERIVED (proved here, sorry-free):
    * the exact normalizer N(n) = (n−1)! (resp. [n−1]_q!) reconciling period and
      carrier — no fit, forced by n·N(n) = n! (resp. [n]_q!);
    * the normalized binding OGF satisfies the PROVED depth-2 confluent/q-lift
      kernel, for any sequence with the (q-)involution recurrence, m_e cancelling.

  CONJECTURAL (NOT proved here — the honest residual):
    * that this depth-2 carrier IS the Seiberg–Witten prolongation SYMBOL — the
      GEOMETRIC identification `conj:qdifference-kernel-prolongation-symbol`.
      This bridge closes the *normalization/recurrence* leg only; the geometry
      (that the kernel arises from the fibre root-of-unity singularity structure
      of λ_SW) stays open.
    * the q-lift bridge is stated for the q-NATURAL period `S(n)/[n]_q` (n→[n]_q,
      matching the dim_q q-deformation of S(n)); promoting the manuscript's
      plain-integer `S(n)/n` to `S(n)/[n]_q` is a fibre-natural definitional
      choice, NOT a fit — see the audit.

  Base ring: classical leg over ℚ (pre-archimedean, no ordering used beyond the
  rationals; §7c wall-safe — no ℝ); q-lift over a generic field with
  non-vanishing q-integers. Shifted indices `n+1,n+2,n+3` keep every `/k` and
  `(k−1)!` division-safe with no ℕ-subtraction.

  -- Ref: [leitner2026] mass-theory, conj:binding-manybody-eq-jet-filtration,
  --      conj:qdifference-kernel-prolongation-symbol, prop:sw-classical-jet-exactness;
  --      docs/audits/2026-07-20-keystone-bridge-c1-binding.md
-/

import Mathlib.Tactic
import QOU.Mass.QDifferenceConfluentObstruction
import QOU.Mass.BindingGevreyHalf

namespace QOU.Mass.KeystoneBridgeC1Binding

open QOU.Mass.QDifferenceConfluentObstruction
open QOU.BraidKnot.KeystoneC8SuperExpBound
open Finset

/-- **The factorial strip `N(n) = (n−1)!` (classical).** The binding PERIOD at
    index `m+1` is `p_{m+1} = f_{m+1}/(m+1)`; the C1 carrier is
    `b_{m+1} = f_{m+1}/(m+1)!`. Since `(m+1)! = (m+1)·m!` they differ by exactly
    `m! = ((m+1)−1)!`:  `p_{m+1} = b_{m+1}·m!`, i.e. `b_{m+1} = p_{m+1}/m!`.
    This exhibits the unique fixed normalizer `N(n) = (n−1)!`
    (equivalently `n·N(n) = n!`) reconciling the period `f_n/n` with the carrier
    `f_n/n!`. Over ℚ (`m+1` and factorials are invertible — no positive-
    characteristic degeneration). -/
theorem period_carrier_strip (f : ℕ → ℚ) (m : ℕ) :
    f (m + 1) / ((m : ℚ) + 1)
      = (f (m + 1) / ((m + 1).factorial : ℚ)) * (m.factorial : ℚ) := by
  have hm : (m.factorial : ℚ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero m
  have hm1 : ((m : ℚ) + 1) ≠ 0 := by positivity
  have hfac : ((m + 1).factorial : ℚ) = ((m : ℚ) + 1) * (m.factorial : ℚ) := by
    rw [Nat.factorial_succ]; push_cast; ring
  rw [hfac]
  field_simp

/-- **Keystone bridge C1 ↔ binding (classical fibre) — PROVED.**
    For any sequence `f` with the involution recurrence
    `f(n+2) = f(n+1) + (n+1)·f(n)`, the binding period `p_k = f_k/k` gives the
    body term `B_k = m_e·p_k`, and its `N(k)=(k−1)!`-normalized carrier
    `b_k = B_k/(k−1)! = m_e·f_k/k!` satisfies the PROVED depth-2 confluent kernel
        `(n+2)·b_{n+2} = b_{n+1} + b_n`.
    Stated on the PERIOD directly (`b_k = m_e·(f_k/k)/(k−1)!`) so the normalizer
    is explicit; indices shifted by 1 to avoid ℕ-subtraction. The constant `m_e`
    cancels — the kernel is linear homogeneous. Discharges the normalization leg;
    the SW-prolongation-symbol identification stays conjectural. -/
theorem keystone_bridge_binding_classical (f : ℕ → ℚ) (me : ℚ)
    (hrec : ∀ n, f (n + 2) = f (n + 1) + ((n : ℚ) + 1) * f n) (n : ℕ) :
    ((n : ℚ) + 3) * (me * (f (n + 3) / ((n : ℚ) + 3)) / ((n + 2).factorial : ℚ))
      = me * (f (n + 2) / ((n : ℚ) + 2)) / ((n + 1).factorial : ℚ)
        + me * (f (n + 1) / ((n : ℚ) + 1)) / (n.factorial : ℚ) := by
  have hfac2 : ((n + 2).factorial : ℚ) = ((n : ℚ) + 2) * ((n + 1).factorial : ℚ) := by
    rw [Nat.factorial_succ (n + 1)]; push_cast; ring
  have hfac1 : ((n + 1).factorial : ℚ) = ((n : ℚ) + 1) * (n.factorial : ℚ) := by
    rw [Nat.factorial_succ n]; push_cast; ring
  have hne0 : (n.factorial : ℚ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero n
  have hn1 : ((n : ℚ) + 1) ≠ 0 := by positivity
  have hn2 : ((n : ℚ) + 2) ≠ 0 := by positivity
  have hn3 : ((n : ℚ) + 3) ≠ 0 := by positivity
  have hr : f (n + 3) = f (n + 2) + ((n : ℚ) + 2) * f (n + 1) := by
    have h := hrec (n + 1)
    rw [show n + 1 + 2 = n + 3 from rfl, show n + 1 + 1 = n + 2 from rfl] at h
    push_cast at h
    linarith [h]
  rw [hr, hfac2, hfac1]
  field_simp

/-- **Keystone bridge C1 ↔ binding (q-lift) — PROVED.**
    Over a field with non-vanishing q-integers, for any q-na-Stokes numerator `S`
    with the q-involution recurrence `S(n+2) = S(n+1) + [n+1]_q·S(n)`, the
    q-natural binding period `p_k = S_k/[k]_q` gives `B_k = m_e·p_k`, and its
    `N_q(k) = [k−1]_q!`-normalized carrier `b_k = B_k/[k−1]_q! = m_e·S_k/[k]_q!`
    satisfies the PROVED depth-2 q-difference kernel
        `[n+2]_q·b_{n+2} = b_{n+1} + b_n`
    — with `c(q) = 1`, no free constant. At `q = 1` (`qint 1 k = k`) this is the
    classical bridge above. The q-lift uses the q-natural period `S/[n]_q`; see
    the audit for the plain-`/n` vs `/[n]_q` definitional note. -/
theorem keystone_bridge_binding_qlift {K : Type*} [Field K] (q : K) (me : K)
    (S : ℕ → K) (hq : ∀ k, 1 ≤ k → qint q k ≠ 0)
    (hrec : ∀ n, S (n + 2) = S (n + 1) + qint q (n + 1) * S n) (n : ℕ) :
    qint q (n + 3) * (me * (S (n + 3) / qint q (n + 3)) / qfact q (n + 2))
      = me * (S (n + 2) / qint q (n + 2)) / qfact q (n + 1)
        + me * (S (n + 1) / qint q (n + 1)) / qfact q n := by
  have hfz : ∀ m, qfact q m ≠ 0 := by
    intro m
    induction m with
    | zero => simp [qfact]
    | succ k ih => exact mul_ne_zero (hq (k + 1) (Nat.succ_le_succ (Nat.zero_le k))) ih
  have hq1 : qint q (n + 1) ≠ 0 := hq (n + 1) (by omega)
  have hq2 : qint q (n + 2) ≠ 0 := hq (n + 2) (by omega)
  have hq3 : qint q (n + 3) ≠ 0 := hq (n + 3) (by omega)
  have hf2 : qfact q (n + 2) = qint q (n + 2) * qfact q (n + 1) := rfl
  have hf1 : qfact q (n + 1) = qint q (n + 1) * qfact q n := rfl
  have hr : S (n + 3) = S (n + 2) + qint q (n + 2) * S (n + 1) := by
    have h := hrec (n + 1)
    rw [show n + 1 + 2 = n + 3 from rfl, show n + 1 + 1 = n + 2 from rfl] at h
    exact h
  rw [hr, hf2, hf1]
  field_simp

/-- **Concrete discharge on the involution numbers.** `involutionNumber`
    satisfies the involution recurrence by `rfl`, so `keystone_bridge_binding_classical`
    applies verbatim: the `(n−1)!`-normalized binding OGF built from the classical
    na-Stokes period `I(n)/n` satisfies the proved depth-2 kernel. This is the
    classical fibre of the keystone, discharged for the corpus sequence
    (`sw-classical-jet-exactness`, `BindingGevreyHalf.involutionNumber_pos`). -/
theorem keystone_bridge_involution (me : ℚ) (n : ℕ) :
    ((n : ℚ) + 3)
        * (me * ((involutionNumber (n + 3) : ℚ) / ((n : ℚ) + 3)) / ((n + 2).factorial : ℚ))
      = me * ((involutionNumber (n + 2) : ℚ) / ((n : ℚ) + 2)) / ((n + 1).factorial : ℚ)
        + me * ((involutionNumber (n + 1) : ℚ) / ((n : ℚ) + 1)) / (n.factorial : ℚ) := by
  refine keystone_bridge_binding_classical (fun k => (involutionNumber k : ℚ)) me ?_ n
  intro m
  show ((involutionNumber (m + 2) : ℚ))
      = (involutionNumber (m + 1) : ℚ) + ((m : ℚ) + 1) * (involutionNumber m : ℚ)
  have hI : involutionNumber (m + 2)
      = involutionNumber (m + 1) + (m + 1) * involutionNumber m := rfl
  rw [hI]; push_cast; ring

/-- **Vanishing difference form of `period_carrier_strip` (`qou-2wtx`).**
For any `f : ℕ → ℚ` and `m : ℕ`,
`f (m + 1) / ((m : ℚ) + 1) - (f (m + 1) / ((m + 1).factorial : ℚ)) * (m.factorial : ℚ) = 0`. -/
theorem period_carrier_strip_sub_eq_zero (f : ℕ → ℚ) (m : ℕ) :
    f (m + 1) / ((m : ℚ) + 1)
      - (f (m + 1) / ((m + 1).factorial : ℚ)) * (m.factorial : ℚ) = 0 :=
  sub_eq_zero.mpr (period_carrier_strip f m)

end QOU.Mass.KeystoneBridgeC1Binding
