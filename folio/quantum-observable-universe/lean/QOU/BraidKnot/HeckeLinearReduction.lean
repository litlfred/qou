/-
# Linear reduction in a single Hecke generator, and the sym/alt ratio quantum

Two facts that were used numerically before they were proved.

`hecke_linear_mul` is the algebra behind the `per_generator_V_hat_3A`
rewrite (`23b9c4f5ba`, merged in #5622): a product of factors
`c • sigma + d` in the SAME generator collapses to `alpha • sigma + beta`
by a scalar recursion, so no matrix product is needed. That change landed on
numerical agreement (9.107e-16 over 171 fields); this is the proof it rested on.

`symAltRatio_*` explain the integer quantisation of the chirality invariant
`Phi_3 = sum_i log |lambda_sym_i / lambda_alt_i|`. Each chain factor's ratio is
`-q^2`, `-q^(-2)` or `-1`, so the exponent moves in steps of two and
`Phi_3 / log q` is an EVEN integer. Measured before it was proved: 6 and 2 for
the two nucleon chains, and 4, 6, 6, 12, 12 for H-1, D, T, 3He, 4He. All even.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.BraidKnot

/-! ## Linear reduction in one generator -/

/-- Two elements linear in the same Hecke generator multiply to a linear
element, with the coefficients given by an explicit scalar recursion.

`s` is the generator, subject only to the Hecke quadratic relation
`s^2 = delta * s + 1` (with `delta = q - q⁻¹` in the intended reading).
Stated over a generic `CommRing`: no ordering, no square root, nothing
archimedean is used, per the §7c base-ring convention. -/
theorem hecke_linear_mul {R : Type*} [CommRing R] (s delta a b c d : R)
    (hs : s ^ 2 = delta * s + 1) :
    (a * s + b) * (c * s + d)
      = (a * c * delta + a * d + b * c) * s + (a * c + b * d) := by
  have expand : (a * s + b) * (c * s + d)
      = a * c * s ^ 2 + (a * d + b * c) * s + b * d := by ring
  rw [expand, hs]; ring

/-- The recursion is exactly the one the compute uses: folding a chain factor
`(c, d)` onto an accumulated `(a, b)` sends it to
`(a*c*delta + a*d + b*c, a*c + b*d)`. Starting from the identity `(0, 1)`
reproduces the factor itself, which is the base case of that fold. -/
theorem hecke_linear_mul_id {R : Type*} [CommRing R] (s delta c d : R)
    (hs : s ^ 2 = delta * s + 1) :
    ((0 : R) * s + 1) * (c * s + d)
      = (0 * c * delta + 0 * d + 1 * c) * s + (0 * c + 1 * d) :=
  hecke_linear_mul s delta 0 1 c d hs

/-! ## The sym/alt ratio is a power of `q^2`, up to sign

On a chain factor `c • sigma + d`, the one-dimensional symmetric rep sends
`sigma ↦ q` and the alternating rep sends `sigma ↦ -q⁻¹`. The three factor
shapes occurring in the atomic chains are `d = 0`, `d = -h` and `d = -h/2`,
with `h = q - q⁻¹`.

The `d = -h/2` case needs `q^2 + 1 ≠ 0` as a hypothesis. It is NOT provable
without one: over a field with `q^2 = -1` the denominator `-(q + q⁻¹)/2`
vanishes and the ratio is undefined. Carried as an explicit hypothesis rather
than specialised to `ℝ`, per the §7c base-ring convention — the substrate
reading has `q` real and `> 1`, where it holds, but nothing here needs the
ordering. -/

variable {K : Type*} [Field K]

/-- `d = 0`: the ratio is `-q^2`. -/
theorem symAltRatio_zero (q : K) (hq : q ≠ 0) :
    (1 * q + 0) / (-(1 / q) + 0) = -q ^ 2 := by
  field_simp
  ring

/-- `d = -h` with `h = q - q⁻¹`: the ratio is `-q⁻²`.

Both sides simplify first: `q - h = q⁻¹` and `-q⁻¹ - h = -q`. -/
theorem symAltRatio_full (q : K) (hq : q ≠ 0) :
    (1 * q + -(q - 1 / q)) / (-(1 / q) + -(q - 1 / q)) = -(1 / q ^ 2) := by
  have hn : (1 * q + -(q - 1 / q)) = 1 / q := by ring
  have hd : (-(1 / q) + -(q - 1 / q)) = -q := by ring
  rw [hn, hd, div_neg]
  congr 1
  field_simp

/-- `d = -h/2`: the ratio is `-1`, because numerator and denominator differ
only by sign — `q - h/2 = (q + q⁻¹)/2` and `-q⁻¹ - h/2 = -(q + q⁻¹)/2`.

This is the factor carrying NO chirality: it contributes `0` to `Phi_3`, which
is why the two `(1, -h/2)` factors present in every chain drop out of the count.

Needs BOTH hypotheses, and neither is removable:
* `(2 : K) ≠ 0` — in characteristic two `2⁻¹ = 0` and the halving identity
  `q - h/2 = (q + q⁻¹)/2` is simply false;
* `q ^ 2 + 1 ≠ 0` — where `q ^ 2 = -1` the denominator vanishes and the ratio
  is undefined.
Both hold in the substrate reading (`q` real, `q > 1`), but the ordering is not
what makes them true, so they are carried as hypotheses rather than by
specialising to `ℝ` — §7c. -/
theorem symAltRatio_half (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0)
    (hq1 : q ^ 2 + 1 ≠ 0) :
    (1 * q + -((q - 1 / q) / 2)) / (-(1 / q) + -((q - 1 / q) / 2)) = -1 := by
  have hn : (1 * q + -((q - 1 / q) / 2)) = (q + 1 / q) / 2 := by
    field_simp
    ring
  have hd : (-(1 / q) + -((q - 1 / q) / 2)) = -((q + 1 / q) / 2) := by
    field_simp
    ring
  have key : q + 1 / q = (q ^ 2 + 1) / q := by
    field_simp
  have hsum : q + 1 / q ≠ 0 := by
    rw [key]; exact div_ne_zero hq1 hq
  have hX : (q + 1 / q) / 2 ≠ 0 := div_ne_zero hsum h2
  rw [hn, hd, div_neg, div_self hX]


/-! ### Determinants of the transfer factors — the `Phi_2` half

`Phi_3` is governed by the sym/alt RATIO lemmas above; `Phi_2 = sum ln|det M_i|`
is governed by the DETERMINANT of the same factors. For the factor `c*sigma + d`
the transfer matrix is `T = ![![c*h + d, c], ![c, d]]`, so

    det T = (c * h + d) * d - c ^ 2.

The point of the four lemmas below is a dichotomy: of the six crossing types in
`tbl:atomic-braid-table1-data`, FIVE have `|det| = 1` and contribute nothing to
`Phi_2`; only the proton-neutron factor does not. That is what collapses `Phi_2`
to a single pair-count, and it is why `Phi_2` — unlike `Phi_1` — needs no
Markov parameter and is therefore convention-independent.

These are stated over a `CommRing` with no ordering and no `q` at all: `h` is a
free variable, so nothing here depends on `h = q - q⁻¹`, on the substrate
anchor, or on the C/D convention. (§7c: generic base ring; the archimedean
reading specialises later.) -/

section Determinants

variable {R : Type*} [CommRing R]

/-- The transfer-matrix determinant of the factor `c * sigma + d`. -/
def detT (h c d : R) : R := (c * h + d) * d - c ^ 2

/-- `d = 0` (the `pp` and `ee` crossings, `c = 1`): `det = -1`. -/
theorem detT_zero (h c : R) : detT h c 0 = -c ^ 2 := by
  unfold detT; ring

/-- `d = -c*h` (the `nn` and `pe` crossings, `c = 1`): `det = -c^2`, so `-1`
at `c = 1`. Note this is the SAME determinant as the `d = 0` case even though
the two have opposite chirality — `Phi_2` cannot separate them, which is
exactly why `Phi_3` is the invariant that carries the sign information. -/
theorem detT_full (h c : R) : detT h c (-(c * h)) = -c ^ 2 := by
  unfold detT; ring

/-- The identity factor `c = 0`, `d = 1` (the `ne` crossing): `det = 1`. -/
theorem detT_id (h : R) : detT h 0 1 = 1 := by
  unfold detT; ring

end Determinants

/-! ### The proton-neutron determinant — the only one that is not a unit

The `pn` factor needs division by `2`, so it is stated over a field alongside
the ratio lemmas rather than over a bare `CommRing`. -/

section PnDeterminant

variable {K : Type*} [Field K]

/-- `d = -h/2` (the `pn` crossing, `c = 1`): `det = -(1 + h^2/4)`.

THIS IS THE ONLY CROSSING OF THE SIX WITH `|det| ≠ 1`. Every other factor
contributes `0` to `Phi_2 = sum ln|det M_i|`, so the whole invariant collapses
to one term per proton-neutron pair:

    Phi_2 = Z * N * log (1 + h^2/4).

Equivalently `1 + h^2/4 = ((q + q⁻¹)/2)^2 = ([2]_q / 2)^2` when `h = q - q⁻¹`,
which is the form used in the notation register.

`h` is free — nothing here fixes `h = q - q⁻¹`, so the statement is independent
of the substrate anchor AND of the Markov convention (no `z` occurs). That
independence is the load-bearing part: it is why the C→D excision moves `Phi_1`
and leaves `Phi_2` alone. -/
theorem detT_half (h : K) (h2 : (2 : K) ≠ 0) :
    (1 * h + -(h / 2)) * -(h / 2) - 1 ^ 2 = -(1 + h ^ 2 / 4) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  field_simp
  ring

/-- The `[2]_q` form of the same determinant, for `h = q - q⁻¹`:
`1 + h^2/4 = ((q + q⁻¹)/2)^2`. -/
theorem one_add_hSq_div_four (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    1 + (q - 1 / q) ^ 2 / 4 = ((q + 1 / q) / 2) ^ 2 := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  field_simp
  ring

end PnDeterminant

/-! ### The chirality count

`Phi_3 = w * ln q` with `w` an even integer, and under the all-pairs chain
structure `w` is a signed pair count: `+1` for each `pp` and `ee` pair, `-1` for
each `nn` and `pe` pair, `0` for `pn` and `ne`. With `Z` protons, `N` neutrons
and `Z` electrons those counts are `C(Z,2)`, `C(Z,2)`, `C(N,2)` and `Z^2`.

The lemma below is the resulting collapse. It is stated with the binomials
already doubled (`2 * C(n,2) = n * (n-1)`) so that it holds over any commutative
ring with no division and no `Nat` subtraction. -/

section ChiralityCount

variable {R : Type*} [CommRing R]

/-- The all-pairs chirality count collapses:

    2 * [ 2*C(Z,2) - C(N,2) - Z^2 ]  =  -2*Z - N*(N-1),

written with `2*C(n,2) = n*(n-1)` so no division appears. The `Z^2` term is the
proton-electron pairs, the two `C(Z,2)` are `pp` and `ee`, and `C(N,2)` is `nn`.

Note what survives: the `Z^2` from `pe` cancels the `2*Z^2` coming from the two
proton/electron `C(Z,2)` terms, leaving only a LINEAR proton contribution
against a QUADRATIC neutron one. That asymmetry is the whole content of the
formula — it is why `w` grows like `N^2` and not like `A^2`. -/
theorem chiralityCount_collapse (Z N : R) :
    2 * (Z * (Z - 1)) - N * (N - 1) - 2 * Z ^ 2 = -2 * Z - N * (N - 1) := by
  ring

/-- Subtracting the collapsed form from the all-pairs count cancels to zero (`qou-m8zb`). -/
theorem chiralityCount_collapse_sub_eq_zero (Z N : R) :
    (2 * (Z * (Z - 1)) - N * (N - 1) - 2 * Z ^ 2) - (-2 * Z - N * (N - 1)) = 0 := by
  rw [chiralityCount_collapse Z N, sub_self]

end ChiralityCount

end QOU.BraidKnot
