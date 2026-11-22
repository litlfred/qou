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

## Round 4 (2026-11-22): the three follow-up options

Owner, verbatim: *"Merge and try all"*. PR #8964 was merged (rebase) and the
three remaining options were tried.

1. **k = 0.** Already measured by the pre-registered probe
   `computations/probes/proton_q3_normaliser/` (arm A1): with `[3]_q!` the
   proton-pinned `q₀` moves to `1.13154` (+1.94 %), and `m_p` at the muon pin
   is `1285.39` MeV (+37.0 %). Nothing new was computed.
2. **The proton from the convention-D trace.** Pre-registered in
   `computations/probes/proton_d_trace_normaliser/PREREGISTRATION.md` before
   the run. The production `tr_M` is already the registry's convention-D value
   (gate passes at 1e-30), so the question reduces to the normaliser. Closure
   normalisers supplied by D, against `m_p` at the muon pin: `tr(1) = 1`
   −78.2 %, `[2]_q²` −9.7 %, `[2]_q³` +82.2 %, `(1/z_D)²` −40.7 %. As
   expected, none reproduces `m_p`.
3. **Labelling.** `conj:proton-mass-substrate-identity` now states that the
   identity is fitted in the normaliser, and that its 0.24 ppm residual is at
   the muon pin (at the proton pin it holds exactly, by construction).

## Round 5 (2026-11-22): does the photon form fix the scale of x₋?

**Question.** The `/q³` in `F_Bor` is the scaling of `x₋ = Σ_w (−q)^{−ℓ(w)} σ_w` that gives
it identity coefficient 1. The photon `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` has identity
coefficient 1 by definition. If `x₋` were a photon product at a *forced* scale, the
normaliser would be inherited from the photon rather than chosen.

**Result: scope-(a) negative, two halves.** Exact symbolic arithmetic at generic `q`,
[`computations/probes/proton_q3_photon_factorisation/`](../../computations/probes/proton_q3_photon_factorisation/proton_q3_photon_factorisation_probe.py).

1. **Chiral photons `γ(0,0,c)` never give `x₋`.** `σ₀σ₁⁻¹` acts as `q·q⁻¹ = 1` in the
   trivial representation and as `(−q⁻¹)(−q) = 1` in the sign representation, so every
   product of chiral photons, of any length, has equal trivial and sign images. A nonzero
   multiple of `x₋` has trivial image 0 and sign image `1 + 2q⁻² + 2q⁻⁴ + q⁻⁶ ≠ 0`. This is
   the family the Borromean core `V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h)` lives in.
2. **General two-photon products give `x₋` at any scale.** `γ·γ = λ·x₋` has a
   two-parameter family of solutions, and `λ` varies continuously on it (at `q = 11/10`:
   0.13832…, 0.11467…, 0.03135… at three sample points; one point cross-checked in the
   six-dimensional regular representation). So the photon definition does not fix `λ`.

**What this does not exclude.** A further rule that singles out one point of the family
(for example a bar-invariance or unit condition on the photon parameters) could still
fix `λ`. No such rule is in the corpus. Not formalised in Lean: half 1 is a one-line
character evaluation, and half 2 is a statement about a solution family that the probe
checks exactly.

**Status of `/q³` after Round 5:** still chosen, not derived; the photon route does not
supply it.

## Round 6 (2026-11-22): what a bar-invariant photon would imply

Owner: *"Photon may have bar invariance ... But what would that mean about the particles it
generates under γγ?"* Exact check at generic `q` (bar: `q ↦ q⁻¹`, `σ_i ↦ σ_i⁻¹`). In the
basis `{1, σ₀, σ₁, σ₀σ₁}`, with `h = q − q⁻¹` and `f̄(q) = f(q⁻¹)`:

    γ      = 1 + (φ₀ − hφ₀₁)σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁
    bar(γ) = (1 − h(φ̄₀ + φ̄₁)) + φ̄₀σ₀ + (φ̄₁ − hφ̄₀₁)σ₁ + φ̄₀₁σ₀σ₁

1. **Strict invariance `bar(γ) = γ` forces `φ₀ + φ₁ = 0`** (identity coefficient), together
   with `φ̄₀₁ = φ₀₁` and `φ̄₀ = φ₀ − hφ₀₁`. Then `χ_triv(γ) = 1 + q(φ₀+φ₁) + φ₀₁ = 1 + φ₀₁ =
   χ_sign(γ)`. So every product of bar-invariant photons has equal trivial and sign images,
   and it can never be a nonzero multiple of `x₋` (or of `x₊`).
2. **It excludes the chiral vertex.** `bar(σ₀σ₁⁻¹) = σ₀⁻¹σ₁`, its mirror, and
   `bar(V³) ≠ V³`. A nonzero chiral photon `γ(0,0,c)` is never bar-invariant, because
   invariance would need `φ₀ = hφ₀₁` with `φ₀ = 0`. So strict invariance would forbid the
   γγ factorisation of the Borromean core `V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h)`. Every γγ particle
   would equal its own mirror.
3. **The weaker reading holds: the photon family is closed under bar up to scale.**
   `bar(γ)` always lies in the photon span. Its identity coefficient is `1 − h(φ̄₀+φ̄₁)`, so
   after rescaling it is again a photon. Example: `bar(γ(0,0,c)) = γ(hc̄, −hc̄, c̄)`. So bar
   pairs each photon with a mirror photon (matter with antimatter, per AGENTS.md §7b). The
   identity-coefficient-1 normalisation is not bar-stable. This matches Round 2:
   `bar(x₋) = q⁶x₋`, and the bar-stable normaliser is `[3]_q!`, not `[3]_q!/q³`.

### Round 6, formalised (2026-11-22)

All Round 6 assertions are proved in
[`QOU/MassTheory/PhotonBarClosure.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/PhotonBarClosure.lean).
lean-direct (`-DautoImplicit=false -s 65536`) exits 0. The file has no `sorry`, and every
declaration depends only on `propext`, `Quot.sound` and `Classical.choice`. The setting is an
`R`-algebra with units `σ₀, σ₁`, `σᵢ⁻¹ = σᵢ − h`, and a `θ`-semilinear ring map `b` with
`b σᵢ = σᵢ⁻¹`. No other relation of `H₃(q)` is assumed.

| claim | declaration |
|---|---|
| `b γ(φ) = γ(barColour φ) + (s − 1)·1`, with `s = 1 − h(θφ₀ + θφ₁)` | `bar_photon` |
| closure up to scale: `b γ = s • γ(s⁻¹ • barColour φ)` | `bar_photon_eq_smul` |
| `b γ(0,0,c) = γ(hθc, −hθc, θc)` | `bar_chiral` |
| `b(σ₀σ₁⁻¹) = σ₀σ₁⁻¹ + hσ₀ − hσ₁` | `bar_vertex` |
| strict invariance forces `φ₀ + φ₁ = 0` (independence, `h` a non-zero-divisor) | `phi_sum_zero_of_bar_fixed` |
| a chiral photon is bar-fixed iff `c = 0` | `chiral_bar_fixed_iff` |
| the vertex is not bar-fixed | `vertex_not_bar_fixed` |
| characters with `χσ₀ = χσ₁` agree on products of `φ₀+φ₁=0` photons, so no such product is `λx` with `λ ≠ 0` when `χ₁x = 0 ≠ χ₂x` | `chars_agree_on_products`, `no_multiple_of_split` |
| trivial and sign characters intertwine bar with `θ` on photons | `char_bar_photon` |
| `(σ₀⁻¹σ₁)³ ≠ (σ₀σ₁⁻¹)³` on the 3-dim weight space (`q² ≠ 1`, `q⁴ ≠ −1`) | `bar_borromean_ne` |

## Round 7 (2026-11-22): a norm instead of a fixed 1

Owner: *"maybe … the photon have Norm one? So there isn't a fixed 1? But photon lives on a
sphere? Then maybe we can see more symmetries?"* This round is an exact sympy computation at
generic `q`; it is not formalised.

Replace the fixed identity coefficient 1 by homogeneous coordinates `(e, φ₀, φ₁, φ₀₁)`. The
natural norms on `H₃(q)` are the block norms `N = (χ_triv, χ_sign, det ρ₂)`. Their product,
`χ_triv · χ_sign · det ρ₂`, is the reduced norm, a quartic form.

1. **All three block norms are bar-equivariant on photons:** `N(b γ) = θ N(γ)`, checked
   symbolically for each component. They are multiplicative, so "norm one" is a condition
   that bar preserves and products preserve. The identity coefficient is preserved by
   neither.
2. **Norm-one photons cannot produce the proton's projector.** `x₋` and every block
   idempotent are zero divisors, with norm `0`. So no product of norm-one photons, nor of
   any units, is a nonzero multiple of `x₋`. The scale of `x₋` is fixed instead by
   idempotency: `e₋ = x₋ / c_sign` with `c_sign = q⁻³[3]_q!`. `e₋` is bar-invariant, since
   `b x₋ = q⁶ x₋` and `θ c_sign = q³[3]_q!`. Its identity coefficient is `q³/[3]_q!`. So
   `F_Bor`'s normaliser `[3]_q!/q³` is `1/(identity coefficient of e₋)`, the Schur element
   already identified (`ProtonQ3SchurElement`). A norm adds nothing new on `/q³`.
3. **The Borromean photons are a conjugate pair.** The two chiral factors of
   `V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h)` have block norms `(q², q², q⁻²)` and `(q⁻², q⁻², q²)`.
   Their weights are related by `θ(qh) = −q⁻¹h`, so `V³ = γ(0,0,c)·γ(0,0,θc)` with
   `c = qh`, a norm-like product `γ·γ^θ`, where `θ` acts on coefficients only. `V` itself
   has block norm `(1,1,1)`. This is an observation; whether other γγ particle words have
   the form `γ·γ^θ` is untested.

## Round 8 (2026-11-22): which particles are γγ products, and why V³ is γ·γ̄

Owner: *"Aren't all of the other particles generated from the photons so they would
necessarily need to have that form? … Can we actually generate the particles that we have
now?"* Exact sympy at generic `q`, except where marked numerical.
[`electron_two_photon_probe.py`](../../computations/probes/proton_q3_photon_factorisation/electron_two_photon_probe.py).

1. **Why `V³ = γ·γ̄`.** In `H₃(q)`, `V³ = 1 + h²V − h²V²` with `V = σ₀σ₁⁻¹`. Factoring the
   quadratic `1 + h²x − h²x²` as `(1 + αx)(1 + βx)` gives `α + β = h²` and `αβ = −h²`, so
   `{α, β} = {qh, −q⁻¹h}`. The coefficients involve only `h²`, and `θ(h²) = h²`, so `θ`
   permutes the two roots. The conjugate pair therefore comes from the bar involution acting
   on the coefficients of `V`'s polynomial: a Galois-type symmetry of this one element.
2. **Not every γγ product has this form.** `V³` itself has a continuous family of other
   two-photon factorisations, with varying scale and non-chiral weights (60-digit mpmath
   root finding at `q = 1.1`, five distinct real solutions found). The Borromean pair is
   the one point with scale 1 and both factors chiral.
3. **The electron `σ₀σ₁σ₀` is not a two-photon product.** No `γ₁γ₂` with any weights,
   complex allowed, is a nonzero multiple of `σ₀σ₁σ₀`. Because `σ₀σ₁σ₀` is a unit, `γ₁` must
   be invertible. A lex Gröbner basis of the two remaining conditions forces `b = c/q` or
   `b = −cq`, and on both branches every solution has `det ρ₂(γ₁) = 0`. This is the algebra-level
   counterpart of the corpus's word-level `gammaGamma_length_even`. Three or more photons are
   untested.
4. **Mass computations: no number moves.** At `q = 1`, `h = 0`, both Borromean photons are the
   bare photon and `V³ = 1`. This agrees with the working assumption `m_p = m_n` at `q = 1`
   (bean `qou-az9l`, `FlipSymmetryAtOne`). A rule "particle words are norms `γ·γ̄`" would be a
   non-census way to select words (`qou-ales`). It is a hypothesis only, and point 3 shows it
   does not cover the electron as a two-photon word.
