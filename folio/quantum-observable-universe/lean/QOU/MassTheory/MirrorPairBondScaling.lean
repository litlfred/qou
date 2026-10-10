import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.Tactic

/-!
# Mirror-pair bond scaling — the isospin split generalizes to `(a/b)^{d(A−1)}`

The general law behind the just-landed A=3 identity
`triton_helium3_split : T/³He = (a/b)²`
([`BondWeightIsospinSplit.lean`](./BondWeightIsospinSplit.lean), PR #3841,
bean `qou-r1sr`). Same Mayer/Ursell pairwise (`b₂`) setting: each nucleon–nucleon
bond `(x,y)` carries the inverse-product ideal-gas weight `w(x,y) = 1/(τx·τy)`,
`a := τ(proton)`, `b := τ(neutron)`; a nucleus' aggregate is the product of its
bond weights.

For a nucleus with `Z` protons and `N` neutrons the pairwise bonds are
`C(Z,2)` `pp`-bonds (weight `a⁻²` each), `C(N,2)` `nn`-bonds (`b⁻²`), and `Z·N`
`pn`-bonds (`(ab)⁻¹`). The total `a`- and `b`-exponents of the *bond-trace
product* `∏ τx·τy` collapse to a single factor `A−1`:

`2·C(Z,2) + Z·N = Z(Z−1) + ZN = Z(A−1)`,  likewise `N(A−1)`,  `A = Z+N`.

So the whole pairwise cluster level is governed by **one** exponent `A−1`.
Two consequences, both proved here (with `m := A−1` kept as a free `ℕ` so the
statements are clean `CommMonoid` / `Field` identities — no `ℕ`-subtraction; the
physical `m = A−1` is instantiated in the corollaries):

* **scaling law** `bondTraceProduct Z N m = (a^Z · b^N)^m` — the pairwise level
  is a single `m`-th power of the "nucleon content" monomial `a^Z b^N`;
* **mirror-pair split** for the pair `(Z, Z+d) ↔ (Z+d, Z)` (isospin gap `d`,
  shared `A`), the aggregate ratio is exactly `(a/b)^{d·m}` — the degeneracy
  break a type-blind bond model gives as `1`.

Recoveries / predictions (instantiating `m = A−1`):
`(Z,d,A) = (1,1,3)` ⇒ `(a/b)²` — recovers `triton_helium3_split` (T/³He);
`(3,1,7)` ⇒ `(a/b)⁶` — the ⁷Li/⁷Be pairwise prediction (new).

Scope (§7c + the sibling's own note): this is a **generic-field** algebraic
identity (no `ℝ`, no ordering); the archimedean `a,b := tr_M` at `q₀` lives in the
witness. It isolates the pairwise (`b₂`) isospin-scaling law; it does **not**
close the extensivity gap (the open magnitude is the connected `b₄` term,
orthogonal to this pairwise object). The exponent `d(A−1)` growing with `A`
makes the pairwise model's over-scaling for heavier mirrors explicit — a feature,
not a fit.

Background: the Mayer–Ursell cluster (`b₂`/pairwise) expansion of statistical
mechanics; see `BondWeightIsospinSplit.lean` for the A=3 special case and the
`qou-r1sr` grounding witness.
-/

namespace QOU.MassTheory

variable {R : Type*}

/-- Inverse-product (Mayer ideal-gas) bond weight `w(x,y) = 1/(x·y)`. -/
def bondWeightM [DivisionRing R] (x y : R) : R := (x * y)⁻¹

/-- The **bond-trace product** of a nucleus `(Z,N)`: the product of `τx·τy` over
all pairwise bonds, whose collapsed exponents are `Z·m` on `a` and `N·m` on `b`
with `m := A−1`. Kept with the multiplicity `m` free (a `ℕ`), so no
`ℕ`-subtraction enters. -/
def bondTraceProduct [Monoid R] (Z N m : ℕ) (a b : R) : R := a ^ (Z * m) * b ^ (N * m)

/-- The pairwise **aggregate** of `(Z,N)`: the product of the inverse-product bond
weights, i.e. the reciprocal of the bond-trace product. -/
def pairAggregate [DivisionRing R] (Z N m : ℕ) (a b : R) : R :=
  (bondTraceProduct Z N m a b)⁻¹

/-- **Scaling law.** The bond-trace product is a single `m`-th power of the
nucleon-content monomial: `bondTraceProduct Z N m = (a^Z · b^N)^m`. The entire
pairwise cluster level is governed by the one exponent `m = A−1`. -/
theorem bondTraceProduct_eq_pow [CommMonoid R] (Z N m : ℕ) (a b : R) :
    bondTraceProduct Z N m a b = (a ^ Z * b ^ N) ^ m := by
  unfold bondTraceProduct
  rw [mul_pow, ← pow_mul, ← pow_mul]

/-- **Mirror-pair isospin split (general law).** For the mirror pair
`(Z, Z+d) ↔ (Z+d, Z)` (isospin gap `d`, shared mass number, shared multiplicity
`m = A−1`), the aggregate ratio is exactly `(a/b)^{d·m}` — the split a type-blind
bond model gives as `1`. Requires `a, b ≠ 0` (the traces are nonzero at `q₀`). -/
theorem mirror_pair_split (Z d m : ℕ) (a b : R) [Field R] (ha : a ≠ 0) (hb : b ≠ 0) :
    pairAggregate Z (Z + d) m a b / pairAggregate (Z + d) Z m a b = (a / b) ^ (d * m) := by
  unfold pairAggregate bondTraceProduct
  simp only [div_pow, add_mul, pow_add]
  field_simp

/-- **Recovery of the A=3 identity** `triton_helium3_split`: `(Z,d,A) = (1,1,3)`,
so `m = A−1 = 2`, giving the T/³He split `(a/b)²`. -/
theorem triton_helium3_recovered (a b : R) [Field R] (ha : a ≠ 0) (hb : b ≠ 0) :
    pairAggregate 1 2 2 a b / pairAggregate 2 1 2 a b = (a / b) ^ 2 := by
  have h := mirror_pair_split 1 1 2 a b ha hb
  simpa using h

/-- **New prediction, ⁷Li/⁷Be**: `(Z,d,A) = (3,1,7)`, so `m = 6`, giving the
pairwise mirror ratio `(a/b)⁶`. (Pairwise `b₂` level only — the large exponent is
the model's explicit over-scaling for heavier mirrors, not a closure.) -/
theorem li7_be7_pairwise_prediction (a b : R) [Field R] (ha : a ≠ 0) (hb : b ≠ 0) :
    pairAggregate 3 4 6 a b / pairAggregate 4 3 6 a b = (a / b) ^ 6 := by
  have h := mirror_pair_split 3 1 6 a b ha hb
  simpa using h

end QOU.MassTheory
