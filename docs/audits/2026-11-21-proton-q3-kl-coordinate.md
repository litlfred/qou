# The proton's `/q³`: the integral, bar-invariant coordinate criterion

Date: 2026-11-21. PR #8964. Owner request: *"1 2 in audit"*, where

1. look for an axiom-level reason for requiring integral, bar-invariant coordinates;
2. record the criterion as a stated working conjecture.

## Summary

- **Option 1: no axiom forces the criterion.** The corpus has both ingredients
  as defined objects: the bar involution (`def:bar-involution`) and the
  integral form ℤ[q, q⁻¹] (named as the trace's base ring in the
  braids-and-knots chapter intro). It has no axiom saying that a coordinate on
  the Markov-trace family must be taken from them. The derivation is
  therefore **conditional**: given the criterion, the factor is forced and
  sorry-free; without it, it is not.
- **The criterion is minimal.** Each half is needed, and both counterexamples
  are proved.
- **Option 2: recorded** as a working conjecture in
  `braids-and-knots/f-bor-borromean-observable.md`, and here. It is the agent's
  framing, not a ruling.
- **No number moves.** F_Bor keeps the normaliser `c_sign = [3]_q!·q⁻³`; the
  q₀ pin and Q_β are unchanged.

## Setup

`tr_z` is the Markov trace on H₂ with `tr_z(σ) = z`. For the sign quasi-idempotent
`x₋`, `t(z) = tr_z(x₋)` vanishes at the convention-D point `z_D = q³/(q²+1)`,
and `∂_z t(z_D) = −q⁻³` (`hasDerivAt_trXMinus_zD`). Reparametrise the family by
`c = tr_z(b)` with `b = u·σ + v`. Then `c = u z + v`, and the derivative becomes
`u⁻¹·q⁻³`. Other coordinates give other values: the idempotent τ(P₋) gives
`−[2]_q q⁻³`, and Wenzl's `a` gives `−1/(q⁴(q²−1)(q²+1)²)`.

## The criterion and what it forces (proved)

**Criterion.** (A) `b` and `1` span H₂ over ℤ[q, q⁻¹], i.e. `u` is a unit of the
Laurent ring. (B) `b` is fixed by the bar involution `σ ↦ σ⁻¹ = σ − (q − q⁻¹)`,
`q ↦ q⁻¹`.

Writing out (B): `bar u = u` and `bar v − v = u·(q − q⁻¹)`.

| Lean declaration | Statement |
|---|---|
| `LaurentUnits.isUnit_iff_eq_C_mul_T` | over an integral domain R, the units of R[T;T⁻¹] are `C r · Tᵐ` with r a unit |
| `LaurentUnits.int_isUnit_iff` | over ℤ, the units are `±qᵐ` |
| `KLCoordinateLaurent.kl_coord_classification` | (A) and (B) hold iff `u = ±1` and `v = −u·q + c` with `c` bar-invariant, i.e. `b = ±(σ − q) + c` (the KL elements) |
| `KLCoordinateLaurent.unit_not_bar_invariant` | (A) alone: every `qᵐ` is a unit, bar-invariant only for `m = 0`, giving derivative `±q^(−m)·q⁻³` for any m |
| `KLCoordinateLaurent.bar_invariant_coord_not_unit` | (B) alone: `b = [2]_q σ − q²` is bar-invariant but `[2]_q` is not a unit (it is 2 at q = 1), giving `q⁻³/[2]_q` |
| `ProtonQ3Schur.kl_coordinate_derivative` | under `u = ±1`, `|u⁻¹ q⁻³| = q⁻³` |

Verified with `lean -DautoImplicit=false -s 65536`, exit 0. `#print axioms`:
propext, Classical.choice, Quot.sound only. No `sorry`.

## Option 1: is there an axiom-level reason?

Searched the corpus for a principle selecting the coordinate: the
`def:bar-involution` block and its properties, the chapter intro's integral
form, the §7b symmetric-crystal guidance (bar-fixed GS normal forms model
stable matter), and the Kazhdan–Lusztig material. Findings:

- **Integrality (A).** The corpus evaluates traces over ℤ[q, q⁻¹], but it
  states no rule that a reparametrisation of the trace family must be integral.
  A rule like "observables are defined over the integral form" would supply it.
  That rule is not on record.
- **Bar invariance (B).** The bar involution is defined, and §7b uses
  bar-fixed objects as the stable ones. That is authoring guidance about
  matter, not a statement about coordinates on the trace family.
- **Other candidate reasons not found:** a uniqueness theorem for modified
  traces (Geer–Patureau-Mirand) fixes the modified trace only up to a global
  scalar, which is exactly the freedom at issue. The KL basis is unique among
  bar-invariant integral bases only after a degree condition, which is a
  further choice. It does not affect the derivative, since `v` drops out.

This is the result of a targeted search, not an exhaustive one; it is a
scope-(a) negative. A derivation would need a new axiom or a theorem
that observables factor through the integral, bar-symmetric form.

## Option 2: working conjecture (agent's framing)

> **Working conjecture (KL coordinate).** The factor `q⁻³` in the proton
> normaliser `c_sign = [3]_q!·q⁻³` is the derivative of the sign-block Markov
> trace at the convention-D point `z_D`, taken in a coordinate `tr(b)` where
> `b` spans H₂ with `1` over ℤ[q, q⁻¹] and is bar-invariant.

Status: conditional result proved; the criterion is not derived. Recorded in
the F_Bor block's text, and (owner: *"1 2"*, second round) as the block
`conj:proton-normaliser-kl-coordinate`
(`braids-and-knots/proton-normaliser-kl-coordinate.{ts,md,lean}`). Its Lean
sibling carries conditions (A) and (B) as the content-bearing class
`KLCoordinateConjecture u v` and derives `u = ±1` (`unit_eq_pm_one`). The class is
satisfiable (`kl_element_meets_conditions`). What no Lean term carries is the
identification that `F_Bor` is read in such a coordinate; that is the open part.

## Second round: looking for the factorisation principle

The owner asked for a theorem that observables factor through the integral,
bar-symmetric form, which would derive the criterion. **Not found.** What the
attempt produced is a check of the rule on a second block:

| Block | Trace zero | Derivative there (standard/KL coordinate) | Schur element |
|---|---|---|---|
| sign, `x₋` | `z_D = q³/(q²+1)` | `−q⁻³` (`hasDerivAt_trXMinus_zD`) | `c_sign = q⁻³·[3]_q!` |
| trivial, `x₊` | `z₊ = −1/(q³+q)` | `+q³` (`hasDerivAt_trXPlus_zero`) | `c_triv = q³·[3]_q!` |

`linear_blocks_derivative_rule` states both: in the KL coordinates, each
linear Schur element is ±(derivative)·[3]_q!.

> **Correction (third round, same day).** I first called this "one independent
> check" that could have failed. It could not have failed. See the next section:
> it follows from the Ocneanu slopes for any scaling of the element.

## Third round (owner: *"1 / Try more on derivarion"*): the derivation fails

Lean: `QOU/MassTheory/ProtonQ3OcneanuSlopes.lean`, lean-direct exit 0, standard
axioms only.

1. **Ocneanu weights.** `ocneanu_decomposition` checks
   `tr_z = y₃χ_triv + y₁₃χ_sign + y₂₁χ_refl` on all four classes, with
   - `y₃ = (qz+1)(q³z+qz+1)/((q²+1)(q⁴+q²+1))`
   - `y₁₃ = q²(z−q)(z(q²+1)−q³)/((q²+1)(q⁴+q²+1))`
   - `y₂₁ = −q(z−q)(qz+1)/(q⁴+q²+1)`

   The reflection character values `2, q−q⁻¹, −1, 0` come from `τ = Σχ/c_χ`.
2. **The derivative reading is circular.** Each linear weight has slope `±1/[3]_q!`
   at its zeros (`ySign_slope_zD`, `yTriv_slope_zero`). Also
   `tr_z(x₋) = c_sign·y₁₃` (`trXMinus_eq_schurSign_mul_ySign`). So the derivative of
   the trace of any element of a linear block is its square constant over
   `[3]_q!`. The `q⁻³` comes from scaling `x₋` with coefficient 1 on the identity,
   and does not come from the derivative. The trivial-block result is the same
   identity, not an independent check.
3. **The criterion applied uniformly gives k = 0.** `bar(x₋) = q⁶x₋`, using the sign
   character and `schurTriv_eq_q6_mul_schurSign`. The step "`bar(x₋)` lies in the
   sign line" is argued, not formalised. Hence among the integral generators
   `ε qᵐ x₋` only `m = 3` is bar-invariant (`sign_line_bar_fixed_iff`). For
   `q³x₋` the derivative at `z_D` is `−1` (`hasDerivAt_klSign_zD`), and the
   square constant is `q³c_sign = [3]_q!` (`q3_mul_schurSign`), the bar-symmetric
   normaliser. **So "integral and bar-invariant", applied to both the coordinate
   and the element, selects k = 0, not the proton's k = −3.** It is a proved
   statement under that uniform criterion (scope b relative to the criterion).
   It does not refute F_Bor, whose normaliser stays asserted.
4. **Reflection block.** `y₂₁` vanishes at `z = q` with slope `−q(q²+1)/(q⁴+q²+1)`.
   Times `[3]_q!` that is `−[2]_q²` (`yRefl_slope_times_fact`), not `±1`. The
   slope rule does not extend.

**Net.** The derivative route reduces to choosing a generator of the integral sign
line, and that is the original `k` question restated. The uniform KL criterion
picks `k = 0`. The proton's `k = −3` corresponds to "coefficient 1 on the identity",
which is integral but not bar-invariant. I found no principle that selects it.
`conj:proton-normaliser-kl-coordinate` is updated to say this. Whether to keep it,
restate it, or retire it is the owner's call.

What a derivation would need: a statement that every observable is a
ℤ[q,q⁻¹]-linear functional on the integral Hecke algebra commuting with the
bar involution up to a fixed twist. No such statement is in the corpus axioms,
and I did not find one in the ingested library on a targeted search.
Scope (a).

## Related

- PR #8955 (n–p cell thread, relayed by the coordinator):
  `WeightSpaceMarkov.lean` proves the convention-D weights are
  `y₃ = 1 − 2/[2]² = (q⁴+1)/(q²+1)²`, `y₂₁ = 1/[2]²`, `y₁₃ = 0`. This agrees with
  the F_Bor text: `q³/[3]_q!` is not the convention-D `y₃`.
- Pre-registered q₀/Q_β shifts of the alternative normalisers:
  `computations/probes/proton_q3_normaliser/`.

## Default if the owner does nothing

Nothing changes: F_Bor keeps `c_sign`, which is labelled as asserted, and the
criterion stays a stated working conjecture.

## Disposition (owner: *"All"*, 2026-11-21)

The owner picked all three options. They are reconciled as follows:
`conj:proton-normaliser-kl-coordinate` is **restated** to show the split
(criterion on the coordinate only, element scaled by its identity coefficient).
It is **retired** as a derivation route (status note, tag `retired`), with the
negative result kept in the block and here. PR #8964 is marked ready for review.
