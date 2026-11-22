/-
Copyright (c) 2026 litlfred. All rights reserved.

# The candidate base operator for the q-difference prolongation `D_q` (W1 route 1)

First concrete ingredient of the open W1 wall (bean `qou-d8de`): construct the
q-difference prolongation `D_q` on the color spectral curve `Σ`. The scoping audit
(`docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md` §2) proved the
**classical** lift `d/dz` is dead (exactness ⇒ periods = 0; and
`ColorCubicPowerSums.color_power_sums`: the power sums are **q-free**), so `D_q` must
be **non-classical (q-difference)**. This file pins the natural candidate for the
*base-level* operator and proves the mechanism by which it is non-classical: the
q-shift `z ↦ q·z` / Jackson q-derivative produces the **quantum integer** `[n]_q`,
not the classical integer `n`.

Concretely (over any `CommRing`, then `Field` to name `[n]_q`):

- `qShift q f = fun z ↦ f (q·z)` — the base q-dilation.
- **`jackson_monomial_numerator`**: `(q·z)^n − z^n = [n]_q · (q−1) · z^n`. Dividing by
  the Jackson denominator `(q−1)z` gives `D_q(z^n) = [n]_q · z^{n−1}` — the q-integer
  `[n]_q = ∑_{i<n} q^i` is exactly what the classical derivative (`n·z^{n−1}`) cannot
  produce. This is the concrete realisation of "the prolongation must be q-difference".
- **`qInt_one_eq_natCast`**: `[n]_1 = n` — the q→1 degeneration recovers the classical
  coefficient, so the candidate `D_q` limits correctly to `d/dz`.

**Scope (candidate operator, NOT the prolongation).** This is the *base* q-difference
operator only. The open W1 core — lifting it to the jet tower `Jⁿ E → Jⁿ⁺¹ E` over the
algebraic curve `Σ` compatibly with the SW connection — is untouched here and stays
beaned (`qou-d8de`); the ramification-symbol extraction (`qou-xufp` / W2) and the
anti-fit `symbol = C1` comparison (`qou-ailp` / W3) likewise. This file asserts **no**
identification with C1 and defines **no** conjecture-class doing so — that would be the
laundering the anti-fit gate forbids. It only records a proved, standard, non-circular
ingredient. §7c: core identity over generic `CommRing`; `[n]_q` naming over `Field`.
Sorry-free. No fit; nothing wired.

-- Ref: [leitner2026] docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md (W1/G1)
-/
import QOU.MathlibExt.QIntegerFactorial

namespace QOU.Mass.QDiffProlongationBaseOperator

open Finset
open QOU.MathlibExt

/-! ## Disambiguation (`qInt`)

`QOU.Mass.qInt` (`QHookDimension`) is the **balanced** q-integer
`∑_{i<n} q^{2i-(n-1)}`; the geometric `∑_{i<n} q^i` this file means is
`QOU.MathlibExt.qInt`. Lean resolves a bare name against the enclosing namespace
before an `open`ed one, so inside `namespace QOU.Mass.*` a bare `qInt` is the
**balanced** one however this file opens `QOU.MathlibExt`. Every reference below is
therefore fully qualified: the bare form compiled against the wrong convention from
`1646b5d6d3` until this was fixed, and a bare form reintroduced here would silently
mean different mathematics again. Bean `qou-lksc`. -/

/-- **The base q-dilation** `σ_q f = z ↦ f(q·z)` — the candidate base operator whose
jet-tower lift would be the sought prolongation `D_q`. -/
def qShift {R : Type*} [CommRing R] (q : R) (f : R → R) : R → R := fun z => f (q * z)

/-- `σ_q` sends the monomial `w ↦ w^n` to `z ↦ q^n · z^n`. -/
@[simp] theorem qShift_monomial {R : Type*} [CommRing R] (q : R) (n : ℕ) (z : R) :
    qShift q (fun w => w ^ n) z = q ^ n * z ^ n := by
  simp [qShift, mul_pow]

/-- **The cleared Jackson q-derivative on a monomial** (over any `CommRing`).
`(q·z)^n − z^n = (∑_{i<n} q^i)·(q−1)·z^n`. The bracket `∑_{i<n} q^i` is the quantum
integer `[n]_q`; dividing by the Jackson denominator `(q−1)z` gives
`D_q(z^n) = [n]_q · z^{n−1}`. -/
theorem jackson_monomial_numerator_commRing {R : Type*} [CommRing R] (q z : R) (n : ℕ) :
    (q * z) ^ n - z ^ n = (∑ i ∈ range n, q ^ i) * (q - 1) * z ^ n := by
  have hgeom : (∑ i ∈ range n, q ^ i) * (q - 1) = q ^ n - 1 := geom_sum_mul q n
  rw [mul_pow]
  rw [hgeom]
  ring

/-- **The Jackson q-derivative names the quantum integer `[n]_q`** (over a `Field`,
reusing the corpus `QOU.MathlibExt.qInt`): `(q·z)^n − z^n = [n]_q · (q−1) · z^n`. Contrast the classical
`d/dz (z^n) = n·z^{n−1}` (`n` is q-free); here the coefficient is `[n]_q`, so the base
operator is genuinely non-classical — the mechanism the C1 kernel needs. -/
theorem jackson_monomial_numerator {K : Type*} [Field K] (q z : K) (n : ℕ) :
    (q * z) ^ n - z ^ n = QOU.MathlibExt.qInt q n * (q - 1) * z ^ n := by
  simpa [QOU.MathlibExt.qInt] using jackson_monomial_numerator_commRing q z n

/-- **q→1 degeneration:** `[n]_1 = n`. The candidate q-difference base operator recovers
the classical integer coefficient in the classical limit, so `D_q → d/dz` as `q → 1`. -/
@[simp] theorem qInt_one_eq_natCast {K : Type*} [Field K] (n : ℕ) :
    QOU.MathlibExt.qInt (1 : K) n = (n : K) := by
  simp [QOU.MathlibExt.qInt, Finset.sum_const, Finset.card_range]

end QOU.Mass.QDiffProlongationBaseOperator
