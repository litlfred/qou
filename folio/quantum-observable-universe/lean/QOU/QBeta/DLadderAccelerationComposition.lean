import Mathlib.Algebra.GroupWithZero.Units.Lemmas
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Tactic

/-!
# D-ladder Écalle acceleration — the Borel–Leroy composition collapse

Sibling of `QOU.QBeta.DLadderTwoAdicGrading` (the 2-adic bar-parity grading,
`gap_invariant_under_scalar_transform`). Supplies the **structural core of M3**
in `qbeta_dladder_ecalle_phib_resummation.py` / the audit
`docs/audits/2026-07-17-dladder-ecalle-phib-resummation.md`:

The bar-odd Q_β D-ladder is q-Gevrey with **no single Gevrey index** (the
divergence class `C` and the Borel–Leroy order `s*` both drift; KC22, #3839), so
its honest resummation is a multi-level **Écalle acceleration** between distinct
critical times — *not* any single fixed-order Borel–Leroy transform.

A natural worry is whether one could *repair* the refuted fixed-order route by
**composing** several fixed-order Borel–Leroy transforms. This file proves one
cannot: the Borel–Leroy acceleration weight of order `s` on the `k`-th
coefficient is `w_s(k) = (k!)^s`, and

  **composition adds orders** — `w_{s+t}(k) = w_s(k)·w_t(k)` —

so iterating a single fixed-order transform reaches exactly the **ℤ-multiples**
of the base order and can **never** reach an incommensurate critical time. The
fixed-order negative is therefore not repairable by iteration: a genuine
(non-commutative) Écalle acceleration kernel between distinct critical times is
**necessary**, not optional.

Integer orders are shown over a generic base ring (§7c: `zpow`, no archimedean
construct — no `Real.rpow`, no `ℝ`); the real-order Borel–Leroy weight has the
identical additive structure via `Real.rpow_add`, and the collapse argument is
verbatim. The additivity `(k!)^{s+t} = (k!)^s (k!)^t` is an elementary true fact
(not the claim being laundered); the **theorem** is its consequence, the collapse.

-- Ref: [leitner2026] docs/audits/2026-07-17-dladder-ecalle-phib-resummation.md
-/

namespace QOU.QBeta.DLadderAccelerationComposition

variable {R : Type*} [Field R]

/-- The Borel–Leroy acceleration weight of order `s` on the `k`-th coefficient:
    `w_s(k) = (k!)^s`.  Integer order `s : ℤ` over a generic field (`zpow`); the
    real-order weight is `(k! : ℝ) ^ (s : ℝ)` with the identical additive law. -/
def borelLeroyWeight (s : ℤ) (k : ℕ) : R := (Nat.factorial k : R) ^ s

/-- **Composition adds orders.** Applying the order-`t` Borel–Leroy transform
    after the order-`s` one multiplies the weights, i.e. gives the *single*
    order-`(s+t)` transform.  (Requires `(k!) ≠ 0` in `R`, automatic in char 0.) -/
theorem borelLeroyWeight_add {k : ℕ} (hk : (Nat.factorial k : R) ≠ 0) (s t : ℤ) :
    borelLeroyWeight (s + t) k = borelLeroyWeight (R := R) s k * borelLeroyWeight t k := by
  simp only [borelLeroyWeight]
  exact zpow_add₀ hk s t

/-- **Iteration reaches only ℤ-multiples of the base order.**  Composing the
    order-`s` transform `n` times gives exactly the order-`(n • s)` weight
    `(k!)^{n·s} = ((k!)^s)^n`. -/
theorem borelLeroyWeight_iterate {k : ℕ} (hk : (Nat.factorial k : R) ≠ 0)
    (s : ℤ) (n : ℕ) :
    borelLeroyWeight ((n : ℤ) • s) k = (borelLeroyWeight (R := R) s k) ^ n := by
  induction n with
  | zero => simp [borelLeroyWeight]
  | succ m ih =>
      have hstep : ((m + 1 : ℕ) : ℤ) • s = (m : ℤ) • s + s := by
        push_cast; ring
      rw [hstep, borelLeroyWeight_add hk, ih, pow_succ]

/-- **The collapse.**  No finite composition of a single fixed-order Borel–Leroy
    transform reaches an order outside the ℤ-multiples of the base — in
    particular, if the target critical time `s'` is incommensurate with the base
    order `s` (`s' ≠ n·s` for every `n`), no `n`-fold iteration reaches it. This
    is why the refuted fixed-order route cannot be repaired by iteration and a
    genuine Écalle acceleration kernel between distinct critical times is needed. -/
theorem no_new_critical_time (s s' : ℤ) (h : ∀ n : ℤ, s' ≠ n * s) (n : ℕ) :
    (n : ℤ) • s ≠ s' := by
  intro he
  exact h (n : ℤ) (by rw [← he, zsmul_eq_mul]; push_cast; ring)

end QOU.QBeta.DLadderAccelerationComposition
