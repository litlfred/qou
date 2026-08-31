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
  y_(1³)(z) = q² · N(q, z) / ((q²+1)(q⁴ + q² + 1)),
  N(q, z) = (q²+1)z² − (2q³+q)z + q⁴,
```
with denominator `(q²+1)(q⁴+q²+1) = q⁶+2q⁴+2q²+1 > 0` over `ℝ` (never
vanishing). The **roots** are the roots of the numerator `N`, and this file
proves `N` factors — over **any** commutative ring — as

> **Denominator corrected 2026-08-31.** This read `q⁴+q²+1`, i.e. it was
> short by a factor `(q²+1)` (`= 2.232` at the substrate pin). **No theorem
> in this file changes** — every result here is about `wtNumer`, the
> *numerator*, and both candidate denominators are strictly positive over
> `ℝ`, so the root set and the `z=1` exclusion are untouched. What changes is
> the value a consumer computes if it reads this formula: `y_(1³)` comes out
> **2.232× too large** at the pin. Caught by a probe that did exactly that and
> then disagreed with two independent corpus derivations which agree with each
> other — the `y_111_symbolic` of
> `computations/qbeta/qbeta-admissibility-is-a-magnitude.witness.json` and the
> symbolic-`z` Borromean Markov solve in
> `computations/qbeta/qbeta_z_symbolic_borromean_crosscheck.py`, whose
> `q⁶+2q⁴+2q²+1` is `(q²+1)(q⁴+q²+1)` factored.
```
  N(q, z) = (z − q) · ((q²+1)·z − q³),
```
so the two admissible Markov parameters `{q, z_D}` are manifest and `z = 1` is
excluded on the substrate window `1 < q < ` (plastic number `≈ 1.4656`).

**What is cited vs. what is proved.** That `N` *is* the `(1³)`-weight numerator
is the external input (the exact Markov-character solve; the sympy probe). The
**algebra** — the factorisation, the exactly-two-roots equivalence, and the
`z = 1` exclusion — is what is proved here, unconditionally. No `c_k`, no base
choice, nothing wired; this hardens the *foundation* the D re-derivation stands
on, it does not pick the base.

Base ring (§7c): the factorisation and the root `iff` are generic
(`CommRing` / `Field`); only the `z = 1` exclusion is archimedean (`ℝ`,
ordering), and it lives below the wall as a separate lemma.

-- Ref: [manuscript] computations/qbeta/qbeta_admissible_functionals_bracket_probe.py
   (the exact y_(1³)(z), its two roots {q, z_D}, and z=1 excluded; 15/15)
-- Ref: [manuscript] .beans/qou-99qc (admissible set COMPLETE, solved not sampled)
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
`q³ − q² − 1 < 0` (i.e. `q` below the plastic number `≈ 1.4656`; the substrate
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
substrate window (`1 < q`, `q` below the plastic number), the `(1³)`-weight
numerator vanishes at exactly `z = q` and `z = z_D`, and not at `z = 1`. This is
the Lean form of `qou-99qc`'s measured completeness — the base functional of the
convention-D Q_β ladder is one of exactly two (augmentation `z = q`, or Markov
trace at `z_D`), and the ansatz's coordinate-sum base is structurally excluded. -/
theorem conventionD_base_completeness {q : ℝ} (h1 : 1 < q)
    (hplastic : q ^ 3 - q ^ 2 - 1 < 0) :
    (∀ z : ℝ, wtNumer q z = 0 ↔ z = q ∨ z = zD q) ∧ wtNumer q 1 ≠ 0 :=
  ⟨fun z => admissible_markov_param_iff q z (q_sq_add_one_ne_zero q),
   one_not_root h1 hplastic⟩


/-! ### The SIGN of the weight is an interval fact, not a point fact

`one_not_root` above is stated at the single point `z = 1`, and the corpus has
read its negative value there — and the negative value at the `z*` the Q_β
inversion demands — as two findings about those points. They are one fact about
an interval, and it is visible directly in `wtNumer_factor`: the numerator is an
upward parabola in `z` whose two real roots are exactly the two admissible
parameters, so it is negative on the whole open interval between them and
positive outside. Every negative `y_(1³)` the corpus has measured says only
`z ∈ (z_D, q)`; none of them is evidence about a particular `z`.
-/

/-- The two admissible roots are **ordered and distinct** for every positive `q`:
`z_D < q`. -/
theorem zD_lt_self {q : ℝ} (hq : 0 < q) : zD q < q := by
  rw [zD, div_lt_iff₀ (by positivity)]
  nlinarith

/-- The gap between the two admissible parameters is exactly `q/(q²+1)`. -/
theorem sub_zD_eq {q : ℝ} (hq : 0 < q) : q - zD q = q / (q ^ 2 + 1) := by
  rw [zD]
  field_simp
  ring

/-- **(INTERVAL) The weight numerator is negative on the whole open interval
between the two admissible roots**, and only there. For `z_D < z < q` the
`(1³)`-block Ocneanu weight is strictly negative — a sign violation at *every*
such `z`, not at any distinguished one. -/
theorem wtNumer_neg_of_between {q z : ℝ} (hq : 0 < q)
    (hlo : zD q < z) (hhi : z < q) : wtNumer q z < 0 := by
  rw [zD, div_lt_iff₀ (by positivity : (0:ℝ) < q ^ 2 + 1)] at hlo
  rw [wtNumer_factor]
  exact mul_neg_of_neg_of_pos (by linarith) (by linarith)

/-- **The weight numerator is positive strictly left of the smaller root.**
For `0 < q` and `z < z_D` (and `z < q`, automatic there since `z_D < q`) both
linear factors are negative, so the product is positive. -/
theorem wtNumer_pos_of_lt_zD {q z : ℝ} (hq : 0 < q) (hlo : z < zD q) :
    0 < wtNumer q z := by
  have hzq : zD q < q := zD_lt_self hq
  rw [zD, lt_div_iff₀ (by positivity : (0:ℝ) < q ^ 2 + 1)] at hlo
  rw [wtNumer_factor]
  refine mul_pos_of_neg_of_neg (by nlinarith) (by linarith)

/-- **`one_not_root` is the `z = 1` instance of the interval lemma.** Restated as
a corollary to make the dependency explicit: the value at `z = 1` is negative
because `1` lies between the two admissible parameters on the substrate window,
for no reason particular to `1`. -/
theorem one_not_root_of_interval {q : ℝ} (h1 : 1 < q)
    (hplastic : q ^ 3 - q ^ 2 - 1 < 0) : wtNumer q 1 < 0 := by
  refine wtNumer_neg_of_between (by linarith) ?_ h1
  rw [zD, div_lt_one (by positivity)]
  linarith

/-! ### Convention C's Markov parameter is inadmissible for EVERY `q > 1` -/

/-- The **convention-C** Markov parameter `z_C = √q/(q+1)` (excised as a
convention by the 2026-08-15 owner ruling; kept here to state the fact about
it). -/
noncomputable def zC (q : ℝ) : ℝ := Real.sqrt q / (q + 1)

private theorem zC_lt_zD_aux {s : ℝ} (hs : 1 < s) :
    s * ((s ^ 2) ^ 2 + 1) < (s ^ 2) ^ 3 * (s ^ 2 + 1) := by
  have hs0 : (0:ℝ) < s := by linarith
  have h7 : (1:ℝ) < s ^ 7 := by
    calc (1:ℝ) = 1 ^ 7 := by norm_num
    _ < s ^ 7 := by gcongr
  have h5 : (0:ℝ) < s ^ 5 := by positivity
  nlinarith [mul_pos hs0 (by linarith : (0:ℝ) < s ^ 7 - 1),
             mul_pos h5 (by linarith : (0:ℝ) < s - 1)]

/-- **`z_C < z_D` for every `q > 1`** — convention C's Markov parameter lies
strictly left of the smaller admissible root, on the whole substrate window. -/
theorem zC_lt_zD {q : ℝ} (h1 : 1 < q) : zC q < zD q := by
  have hq : (0:ℝ) < q := by linarith
  have hs1 : (1:ℝ) < Real.sqrt q := by
    have := Real.sqrt_lt_sqrt (by norm_num : (0:ℝ) ≤ 1) h1
    rwa [Real.sqrt_one] at this
  have hsq : Real.sqrt q ^ 2 = q := Real.sq_sqrt hq.le
  rw [zC, zD, div_lt_div_iff₀ (by linarith) (by positivity)]
  have := zC_lt_zD_aux hs1
  rw [hsq] at this
  linarith

/-- **(CONVENTION C IS NOT A ROOT, FOR EVERY `q > 1`.)** `wtNumer q (z_C q) > 0`,
so convention C's Markov parameter never annihilates the `(1³)` ideal and the
convention-C functional never descended to the two-row (Temperley–Lieb) quotient
either. This is the all-`q` statement; the corpus carries only the point
measurement at the substrate pin. Note the **sign**: `z_C` is positive here while
the counit point `z = 1` is negative, so the two sit on **opposite sides** of the
admissible set. -/
theorem zC_not_root {q : ℝ} (h1 : 1 < q) : 0 < wtNumer q (zC q) :=
  wtNumer_pos_of_lt_zD (by linarith) (zC_lt_zD h1)

end QOU.QBeta.AdmissibleRoots

#print axioms QOU.QBeta.AdmissibleRoots.wtNumer_neg_of_between
#print axioms QOU.QBeta.AdmissibleRoots.wtNumer_pos_of_lt_zD
#print axioms QOU.QBeta.AdmissibleRoots.one_not_root_of_interval
#print axioms QOU.QBeta.AdmissibleRoots.zC_lt_zD
#print axioms QOU.QBeta.AdmissibleRoots.zC_not_root
