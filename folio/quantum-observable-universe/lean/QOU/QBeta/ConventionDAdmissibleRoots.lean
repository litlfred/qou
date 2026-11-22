import Mathlib.Tactic

/-!
# Convention-D admissible base: the `(1³)`-weight has EXACTLY two roots `{q, z_D}`

`qou-cds1` (S1, the Q_β `c_k` ladder under convention D) rests on a
base-admissibility fact established by `qou-99qc` **in sympy**
(`computations/qbeta/qbeta_admissible_functionals_bracket_probe.py`, 15/15) but
not yet Lean-proved:

> Under convention D a functional on `H₃(q)` **descends** to the two-row
> (Temperley–Lieb) quotient iff it annihilates the `(1³)` ideal, i.e. iff its
> Markov parameter `z` is a root of the `(1³)`-block Ocneanu weight
> `y_(1³)(z)`. That weight, solved rather than sampled, is **quadratic in `z`
> with exactly two roots** `z = q` and `z = z_D = q³/(q²+1)`; at `z = q` the
> Markov trace **is** the augmentation, so the admissible set is *closed at two
> elements*. The coordinate sum `net` the ansatz evaluates is `tr_M` at `z = 1`,
> and `z = 1` is **neither** root — so `net` is structurally excluded.

This file makes the **completeness** (exactly two roots; `z = 1` excluded) a
theorem. It complements
[`WenzlWeightVanishing.lean`](WenzlWeightVanishing.lean), which proves the
*row criterion at the fixed level* `r = 2` (`z = z_D` ⇒ the `≥3`-row blocks die);
here `z` is a **variable** and both roots are exhibited.

## The exact weight (cited input, from the Markov-trace character solve on H₃)

The `(1³)`-block Ocneanu weight at `n = 3`, as a function of the Markov
parameter `z`, is
```
  y_(1³)(z) = q² · N(q, z) / (q⁴ + q² + 1),   N(q, z) = (q²+1)z² − (2q³+q)z + q⁴,
```
with denominator `q⁴+q²+1 > 0` over `ℝ` (never vanishing). The **roots** are the
roots of the numerator `N`, and this file proves `N` factors — over **any**
commutative ring — as
```
  N(q, z) = (z − q) · ((q²+1)·z − q³),
```
so the two admissible Markov parameters `{q, z_D}` are manifest and `z = 1` is
excluded on the substrate window `1 < q < ` (supergolden ratio `≈ 1.4656`,
the root of `x³ = x² + 1`; NOT the plastic number `≈ 1.32472`, which is the
root of `x³ = x + 1`).

**What is cited vs. what is proved.** That `N` *is* the `(1³)`-weight numerator
is the external input (the exact Markov-character solve; the sympy probe). The
**algebra** — the factorisation, the exactly-two-roots equivalence, and the
`z = 1` exclusion — is what is proved here, unconditionally. No `c_k`, no base
choice, nothing wired; this hardens the *foundation* the D re-derivation stands
on, it does not pick the base.

Base ring (§7c): the factorisation and the root `iff` are generic
(`CommRing` / `Field`); only the `z = 1` exclusion is archimedean (`ℝ`,
ordering), and it lives below the wall as a separate lemma.

-- Ref: [leitner2026] computations/qbeta/qbeta_admissible_functionals_bracket_probe.py
   (the exact y_(1³)(z), its two roots {q, z_D}, and z=1 excluded; 15/15)
-- Ref: [leitner2026] .beans/qou-99qc (admissible set COMPLETE, solved not sampled)
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors",
--       Invent. Math. 92 (1988) 349-383.
-/

namespace QOU.QBeta.AdmissibleRoots

/-- The **numerator** of the `(1³)`-block Ocneanu weight `y_(1³)(z)` at `n = 3`,
as a polynomial in the Markov parameter `z` over the substrate parameter `q`
(from the exact Markov-trace character solve on `H₃(q)`):
`N(q,z) = (q²+1)z² − (2q³+q)z + q⁴`. -/
def wtNumer {R : Type*} [CommRing R] (q z : R) : R :=
  (q ^ 2 + 1) * z ^ 2 - (2 * q ^ 3 + q) * z + q ^ 4

/-- **The weight numerator factors, over any commutative ring:**
`N(q,z) = (z − q)·((q²+1)·z − q³)`. The two linear factors are the two
admissible Markov parameters. Pure `ring`. -/
theorem wtNumer_factor {R : Type*} [CommRing R] (q z : R) :
    wtNumer q z = (z - q) * ((q ^ 2 + 1) * z - q ^ 3) := by
  unfold wtNumer; ring

/-- **Exactly two roots (domain form, denominator-free).** Over a field, the
weight numerator vanishes iff `z = q` or `(q²+1)·z = q³` — the two admissible
Markov parameters, before clearing the `z_D` denominator. -/
theorem wtNumer_eq_zero_iff {R : Type*} [Field R] (q z : R) :
    wtNumer q z = 0 ↔ z = q ∨ (q ^ 2 + 1) * z = q ^ 3 := by
  rw [wtNumer_factor, mul_eq_zero, sub_eq_zero, sub_eq_zero]

/-- The **convention-D Markov parameter** `z_D = q³/(q²+1)` (Wenzl level `r = 2`). -/
noncomputable def zD {R : Type*} [Field R] (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- The second admissible root is exactly `z_D` (when `q²+1 ≠ 0`):
`(q²+1)·z = q³ ↔ z = z_D`. -/
theorem second_root_eq_zD {R : Type*} [Field R] (q z : R) (hq2 : q ^ 2 + 1 ≠ 0) :
    (q ^ 2 + 1) * z = q ^ 3 ↔ z = zD q := by
  rw [zD, eq_div_iff hq2, mul_comm]

/-- **(COMPLETENESS) The `(1³)`-weight numerator has EXACTLY two roots `{q, z_D}`.**
For `q` with `q²+1 ≠ 0`, `N(q,z) = 0 ↔ z = q ∨ z = z_D`. This is the closed
admissible set: the base functional under convention D is one of exactly two —
the augmentation (`z = q`) or the Markov trace at `z_D` — and no third. -/
theorem admissible_markov_param_iff {R : Type*} [Field R] (q z : R)
    (hq2 : q ^ 2 + 1 ≠ 0) :
    wtNumer q z = 0 ↔ z = q ∨ z = zD q := by
  rw [wtNumer_eq_zero_iff, second_root_eq_zD q z hq2]

/-! ### Archimedean exclusion of the coordinate-sum evaluation `z = 1` -/

/-- Over `ℝ` the denominator `q⁴+q²+1` and the factor `q²+1` never vanish, so the
weight and its numerator share their roots. -/
theorem q_sq_add_one_ne_zero (q : ℝ) : q ^ 2 + 1 ≠ 0 := by positivity

/-- **`z = 1` is NOT a root on the substrate window** `1 < q` with
`q³ − q² − 1 < 0` (i.e. `q` below the supergolden ratio `≈ 1.4656`; the substrate
`q₀ ≈ 1.110` is well inside). Hence the coordinate-sum functional `net = tr_M`
at `z = 1` does **not** descend to the two-row quotient — it is neither
admissible root. `N(q,1) = (1−q)·(q²+1−q³) < 0`. -/
theorem one_not_root {q : ℝ} (h1 : 1 < q) (hplastic : q ^ 3 - q ^ 2 - 1 < 0) :
    wtNumer q 1 ≠ 0 := by
  have hval : wtNumer q 1 = (1 - q) * (q ^ 2 + 1 - q ^ 3) := by
    rw [wtNumer_factor]; ring
  have hlt : 1 - q < 0 := by linarith
  have hgt : 0 < q ^ 2 + 1 - q ^ 3 := by linarith
  have : wtNumer q 1 < 0 := by rw [hval]; exact mul_neg_of_neg_of_pos hlt hgt
  exact ne_of_lt this

/-- **(CAPSTONE) Convention-D base admissibility is closed at exactly two Markov
parameters, and `z = 1` (the coordinate sum `net`) is excluded.** On the
substrate window (`1 < q`, `q` below the supergolden ratio), the `(1³)`-weight
numerator vanishes at exactly `z = q` and `z = z_D`, and not at `z = 1`. This is
the Lean form of `qou-99qc`'s measured completeness — the base functional of the
convention-D Q_β ladder is one of exactly two (augmentation `z = q`, or Markov
trace at `z_D`), and the ansatz's coordinate-sum base is structurally excluded. -/
theorem conventionD_base_completeness {q : ℝ} (h1 : 1 < q)
    (hplastic : q ^ 3 - q ^ 2 - 1 < 0) :
    (∀ z : ℝ, wtNumer q z = 0 ↔ z = q ∨ z = zD q) ∧ wtNumer q 1 ≠ 0 :=
  ⟨fun z => admissible_markov_param_iff q z (q_sq_add_one_ne_zero q),
   one_not_root h1 hplastic⟩

end QOU.QBeta.AdmissibleRoots
