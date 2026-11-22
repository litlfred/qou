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

## Round 9 (2026-11-22): the electron from photons, in Lean and with three factors

Owner: *"Both. What does Breit–Wheeler / Feynman diagram say about producing electrons from
constituents, particularly photons?"*

1. **Two photons: proved in Lean.**
   [`QOU/MassTheory/ElectronNotTwoPhoton.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/ElectronNotTwoPhoton.lean),
   generic field `R` with `q ≠ 0`, `q² + 1 ≠ 0`, `q² ± q + 1 ≠ 0`, no `sorry`, lean-direct
   exit 0. `electron_not_two_photon` says: if `γ(a,b,c)·γ(a',b',c') = λ·σ₀σ₁σ₀` holds on the
   2-dim block (where `σ₀σ₁σ₀` is the antidiagonal `−1`, `electronMat_eq`) and under the
   trivial (`↦ q³`) and sign (`↦ −q⁻³`) characters, then `λ = 0`. The proof is a polynomial
   certificate: `λ·det γ` and `det γ·det γ' + λ²` are explicit combinations of the six block
   equations, so `λ³ = 0`. The same file proves that `S0, S1` satisfy the Hecke and braid
   relations and that `V³ = 1 + h²(V − V²)` on the 2-dim block (`vertex_cube`). **Not
   formalised:** the Wedderburn step "an identity in `H₃(q)` holds iff it holds in the three
   blocks". It is taken as the hypothesis shape.
2. **Three photons: yes, numerically.**
   [`electron_three_photon_probe.py`](../../computations/probes/proton_q3_photon_factorisation/electron_three_photon_probe.py),
   mpmath 60 dps at the sample point `q = 11/10` (a value of the formal variable, not an
   anchor). With `γ₃ = γ(3/10, −7/10, 9/20)` fixed and `λ = 1`, Newton converges to residual
   below `10⁻⁵⁰`, the Jacobian is nonsingular (`det J ≈ 453`) and all three photons are
   invertible in every block. So `σ₀σ₁σ₀ = γ₁γ₂γ₃` has an isolated solution there. This is
   numerical evidence, not a proof. An exact solution was not found.
3. **Any `n ≥ 3` photons then work**, by padding with the bare photon `γ(0,0,0) = 1`. One photon
   fails because `σ₀σ₁σ₀` is not in `span{1, σ₀, σ₁, σ₀σ₁⁻¹}`. So the count is: 1 and 2 fail,
   3 and more succeed.
4. **Correction to Round 8 point 3.** Round 8 called the two-photon negative "the algebra-level
   counterpart of `gammaGamma_length_even`". That overstates it. `H₃(q)` has no parity grading
   at generic `q`: `σ² = hσ + 1` mixes word lengths 2 and 1. And point 3 shows three photons
   succeed, which a parity law would also allow, while four also succeed, which it would forbid.
   The two-photon obstruction is a statement about two factors, not about even length. Nothing
   else cites the Round 8 wording.
5. **Breit–Wheeler and Feynman diagrams (comparison only; no proof uses this).**
   In QED, `γγ → e⁺e⁻` (Breit–Wheeler, 1934) has two tree diagrams, electron exchange in the
   `t` and `u` channels, and a threshold `s ≥ (2m_e)²`. It was seen with many laser photons
   plus one high-energy photon at SLAC E144 (1997). Photons are neutral and a vertex conserves
   charge, so **no number of photons makes a single electron**: they make pairs. Furry's
   theorem (odd-photon closed loops vanish by C-parity) concerns loops, not this.
   Set against the model: products in `H₃(q)` carry no charge bookkeeping, so the algebra lets
   three photons multiply to the electron word, which physics forbids as a process. If photon
   products are meant to model production, the model needs a charge (or lepton-number)
   grading that photons do not carry and `σ₀σ₁σ₀` does. If the products are only a way to
   **select** words (`qou-ales`), Breit–Wheeler says the natural two-photon target is a
   particle–antiparticle pair (for example an electron word times its mirror), not the
   electron alone. Both readings are open. Neither changes a computed number.

## Round 10 — 2026-11-22: charge, norm 1, and the electron in the TL quotient

Photon throughout (owner ruling 2026-11-20): `γ(a,b,c) = 1 + a·σ₀ + b·σ₁ + c·σ₀σ₁⁻¹`.

### 10.1 Photons conserve charge (Lean, sorry-free)

`QOU/MassTheory/PhotonChargeConservation.lean` works on `(C²)^⊗3` with the Jimbo
check-R matrices (`ee ↦ q·ee`, `ud ↦ du`, `du ↦ ud + h·du`, `h = q − q⁻¹`), over a
generic field.

- `photon_prod_preserves`: every finite product of photons maps the span of basis
  vectors with `#u = n` into itself. The proton weight space is `n = 2` (K = q) and the
  neutron is `n = 1` (K = q⁻¹), with charge per strand `1/6 + T³`. So photon products
  conserve charge. The proof is Schur–Weyl in its easy direction: every element of the
  algebra generated by `σ₁, σ₂` commutes with each `diag(f(#u))` (`adjoin_commute`).
- `hecke_sig2`: `σ₂² = h·σ₂ + 1` on this representation.
- Not in Lean: the match of `σ₁, σ₂` restricted to `#u = 2` with the matrices in
  `NucleonWeightSpaceTraces`. Checked by hand only.

### 10.2 H₃(q) itself has no U(1) charge (Lean)

`no_scaling_of_hecke`: an algebra map that scales a generator `σ ↦ t·σ` and respects
`σ² = h·σ + 1` forces `t = 1` (for `h ≠ 0`). So charge cannot be an internal grading of
H₃(q). It lives only in a representation, as in 10.1.

### 10.3 "Norm 1" for a single word

`trivWord_eq`: the trivial block of a word is `q^writhe`. The block norms of a word are
`(q^w, (−q⁻¹)^w, (−1)^w)`. All three equal 1 iff `w = 0` (`trivWord_eq_one_iff`, for q
not a root of unity). With `writhe_eq_zero_of_neutral` (PhotonU1NeutralCut) this gives:
neutral ⇒ norm 1. The converse fails, for example `σ₀²σ₁⁻²` has writhe 0 and is not
neutral. So "norm 1" is weaker than the neutrality cut of the 2026-11-21 ruling.

### 10.4 Quantum versions of norm 1 (computed, not ruled)

Let `†` be the anti-involution `q ↦ q⁻¹` on coefficients, `σ ↦ σ⁻¹`, words reversed.

| option | statement | status |
|---|---|---|
| A. block norm | each linear character is 1 | 10.3; equals writhe 0 on words |
| B. bar norm | `γγ† = 1` | The two ruled Borromean photons `γ(0,0,qh)`, `γ(0,0,−q⁻¹h)` give `γγ† = 1` on the trivial and sign blocks and det 1 on the 2-dim block, but not the identity there (sympy, scratch `qnorm.py`) |
| B′. Galois norm | `N(γ)·θ(N(γ)) = 1`, θ: q ↦ q⁻¹ | This is the relative norm of `Q(q)/Q(q+q⁻¹)`. By Hilbert 90 its kernel is `{x/θ(x)}`, for example `q² = q/θ(q)`. Fits the Borromean pair |
| C. unitarity at \|q\| = 1 | θ becomes complex conjugation | gives a genuine compact unit sphere; not computed |
| D. Markov sphere | `τ(γγ†) = 1` at convention D | not computed |
| E. Hopf / antipode | photon group-like, tied to K | speculative; asked of the α_em thread |

General photon, trivial and sign blocks of `γγ†`:
`triv = (a+b+cq+q)(aq+bq+c+1)/q`, `sign = −(−a−b+cq+q)(aq+bq−c−1)/q`.

### 10.5 The electron as a photon product: TL changes the answer

- **H₃(q), all three blocks:** not a two-photon product (Lean,
  `electron_not_two_photon`); a three-photon product (rigorous now: Krawczyk interval
  test at q = 11/10, box radius 1e-20, `K` strictly inside; probe
  `electron_three_photon_krawczyk.py`).
- **TL quotient (trivial + 2-dim block only):** this is what `(C²)^⊗3` sees. There is
  no sign block in Schur–Weyl for sl₂, and convention D has `y_(1³) = 0`. Here the
  electron **is** a two-photon product, exactly, at generic q. Probe
  `electron_two_photon_tl_probe.py` (exact sympy; all checks pass). Two families:
  - `γ₁ = γ(0, −(q⁴−4q²+2)/(q(q²−q−1)(q²+q−1)), 1)`,
    `λ = (q²−2)(2q²−1)/(q(q²−1)(q²−q−1)²(q²+q−1)²)`;
  - `γ₁ = γ(0, −q³/(q⁴−q²+1), −1)`, `λ = q/((q²−1)(q⁴−q²+1)²)`.

  The sign-block mismatch is nonzero in both, which is the H₃ negative again.
- So the two-photon negative is a statement about the sign block. In the 6-strand
  U_q(sl₂) picture of the lepton-pair ruling the sign block is absent, and the negative
  does not apply. The TL solutions use rational-function photon weights, not the ruled
  Borromean weights `qh, −q⁻¹h`. They are existence results, not a selection.
- Not done: photons placed at other positions on 6 strands. A 6-strand photon is not
  ruled; any such extension would be the agent's.

### 10.6 Pair word

In B₃, `σ₀σ₁σ₀ · (σ₀σ₁σ₀)⁻¹ = 1 = γ(0,0,0)²`. The Breit–Wheeler pair test is trivial
there. The meaningful version is the 6-strand one (e⁻ ⊔ ν̄ ⊔ unknot), which needs a
6-strand photon placement that is not ruled.

### 10.7 Drafted wording for the 2026-11-21 neutrality ruling (for owner approval only)

The ledger row says "whole-word U(1) neutrality". 10.2 shows H₃ has no U(1) grading and
10.3 shows the cut is stronger than writhe 0. Draft, not applied:

> **The γγ word is selected by whole-word linking neutrality** (the central colouring of
> QEDHigherOrderCovariance §P applied to the whole braid: the word's net linking under
> that colouring is zero), then reading-3 Frobenius selection. It implies writhe 0
> (block norm 1) but is strictly stronger. It is not a U(1) grading of H₃(q), which has
> none (`no_scaling_of_hecke`); charge is conserved only in the `(C²)^⊗3` representation
> (`photon_prod_preserves`).

No ledger row is edited until the owner approves.

## Round 11 — 2026-11-22: owner "Do all" follow-ups

Owner approved the "linking neutrality" wording (ledger row revised and a dated row
added). The other items:

### 11.1 Lean: the TL two-photon electron

`QOU/MassTheory/ElectronTwoPhotonTL.lean` (lean-direct exit 0, axioms propext /
Classical.choice / Quot.sound; generic field). For the family
`γ₁ = γ(0, −q³/(q⁴−q²+1), −1)` with `λ = q/((q²−1)(q⁴−q²+1)²)`, it proves
`electron_two_photon_block`, `electron_two_photon_triv`, `lam_ne_zero`, and
`electron_two_photon_sign_defect` (sign mismatch
`= (q²+1)(q²−q+1)(q²+q+1)/(q²(q²−1)(q⁴+1))`). These are block identities; the bridge
to H₃(q)'s TL quotient as an algebra is not formalised (same as the sibling file).
Checking it lean-direct needs an olean for `ElectronNotTwoPhoton`, built the same way
first.

### 11.2 Do the ruled Borromean weights fit the TL two-photon electron? No.

Probe `electron_tl_borromean_weights_probe.py` (exact sympy, 27/27 checks):
- With `γ₁ = γ(0,0,c)` the 2-dim block fixes `γ₂, λ` uniquely; the trivial block then
  requires `F2(c) = (q²−1)c² − (q²−1)²c + q² = 0`. Its discriminant
  `(q²−1)(q³−q²−q−1)(q³+q²−q+1)` is not a square in Q(q), so the admissible chiral
  `c` are quadratic irrationals, complex at q₀ (real only for q at or above the
  tribonacci constant). The partner `γ₂` is never chiral.
- The ruled `c = qh` gives `F2 = −q²`; `c = −q⁻¹h` gives `F2 = −(q⁸−q⁶+2q²−1)/q⁴`.
  Both nonzero for q > 1.
- Two chiral photons `γ(0,0,c)γ(0,0,c′)` lie in span{1, V} and cannot equal `λE` for
  any `λ ≠ 0`, even on the 2-dim block alone.
- Reverse order (ruled photon as `γ₂`, checked in scratch): trivial-block residuals
  `q²(q²−2)(q²−q+1)(q²+q+1)/(q²−1)` for `qh` and
  `−(q²−q+1)(q²+q+1)(q⁴−q²+1)/(q²(q²−1))` for `−q⁻¹h`. Nonzero at generic q and at
  q₀; the first vanishes only at q² = 2.

### 11.3 Quantum norm options C and D

Probe `quantum_norm_cd_probe.py` (exact sympy, 30/30 checks):
- **C (unitarity, |q| = 1):** the unique invariant Hermitian form on the 2-dim block is
  `H = [[1, −q/(q²+1)], [−q/(q²+1), 1]]`, positive for |θ| < π/3. Under it the adjoint
  of σ is σ⁻¹, so unitarity equals `γγ† = 1`. Each Borromean photon is unitary on the
  1-dim blocks, not on the 2-dim block. Their product is unitary only because it is
  the braid word V³. Among chiral photons only `c = 0` is unitary on all blocks.
- **D (Markov sphere, convention D):** `y₃ = (q⁴+1)/(q²+1)²`, `y₂₁ = q²/(q²+1)²`,
  `y₁₁₁ = 0`. Each Borromean photon gives
  `τ(γγ†) = −(q⁸−2q⁶−2q⁴−2q²+1)/(q²(q²+1)²)` (≈ 0.9671 at the proton q₀), not 1.
  The product gives 1, again only as a braid word.

So no quantum norm-1 option singles out the individual ruled photon weights; every
option is satisfied by their product for the trivial reason that it is a braid word.

## Round 12 — 2026-11-22: the γγ lepton pair on six strands, photon by photon

Owner card: "1 Sliding photon at each i". On six strands γᵢ(a,b,c) = 1 + aσᵢ + bσᵢ₊₁ +
cσᵢσᵢ₊₁⁻¹, i = 0…3, larger letter inverted. Target link e⁻ ⊔ ν̄ ⊔ loop (Hopf ⊔ 2 unknots,
owner 2026-11-21). Probe `computations/probes/six_strand_photon_pair/` (pre-registration and
addendum committed first; exact arithmetic).

**12.1 Which vertex words close to the pair (Part 1, evidence by invariant at q = 2, 3).**
264 words of at most 6 vertices match the target or its mirror. The smallest have 3 vertices:
18 words (9 + 9 mirror), e.g. V₀V₀V₁, V₀V₁V₀. Every one moves only four strands, so two
components are untouched strands. If every strand must lie in some vertex footprint, the
smallest count is 5 (25 + 25 words). No candidate is whole-word linking-neutral: the Hopf
pair has lk = 1, so the proton's neutrality rule cannot apply to the lepton pair as stated.
The zero-charge K-sector trace of the nine minimal e⁻ words is one value pair, −61/4 (q = 2)
and −3614/81 (q = 3).

**12.2 A single photon closes to the electron's link (Lean, exact, generic ring).**
`PhotonCrossingMonomials.photon_hopf`: γ(0, −h⁻¹, −1) = −h⁻¹·σ₀²σ₁⁻¹. On three strands
σ₀²σ₁⁻¹ closes to the Hopf link. So the electron's *link* is the closure of one photon.
The ruled electron *element* σ₀σ₁σ₀ is a different braid with the same closure; Round 9
showed it is not a two-photon product in H₃(q). Also `photon_neg_crossing`:
γ(0, −h⁻¹, 0) = −h⁻¹·σ₁⁻¹, a single negative crossing. No positive crossing is a photon
multiple (1 + aσ is never proportional to σ).

**12.3 Two photons make the whole pair (Lean, exact).** `pair_word_two_photons`:
V₀V₁V₂V₀V₃ = σ₀²σ₁⁻¹σ₄⁻¹ = h²·γ₀(0, −h⁻¹, −1)·γ₃(0, −h⁻¹, 0). The two photons sit on
disjoint strands (0–2 and 3–5) and commute: the first closes to the electron's Hopf link,
the second to a kinked unknot, and strand 3 is a free loop. The 5-vertex footprint hides
this, because after braid reduction strand 3 is untouched. The same pattern (a Hopf photon
times a single-crossing photon) gives V₀V₁V₀ = σ₀²σ₂⁻¹σ₁⁻¹ at (1, 0) and (2, 0). The weights
are unique at q = 2 and 3 (zero-dimensional Gröbner basis), so they are forced, not fitted.

**12.4 What does not factor.** At q = 2 and 3, no other 3-vertex match and no other 5-vertex
match is a two-photon product, in the TL quotient or (hence) in H₆(q). V₀V₀V₁ needs three
photons. In TL this works at placements (0,0,1) and (1,0,1); in the full H₄(q) only at
(0,0,1). The real weights form a two-parameter family (coset reduction H₄ = ⊕ H₃·T_d forces
the third photon to γ₁(0, −h⁻¹, z); mpmath at 40 digits, q = 2 and 11/10). So V₀V₀V₁'s
weights are not determined.

**Scope.** Section 12.1 is evidence, not isotopy proofs. Sections 12.2 and 12.3 are exact
algebra identities, sorry-free; that their closures are the Hopf link and the pair link is
the standard reading of the braid, not formalised. Section 12.4's negatives were first
found at two rational q; 12.5 extends them to generic q. Nothing is selected.

**12.5 The two-photon negatives hold for generic q (computed, exact).** Gröbner bases over
ℚ(q), symbolic q, for every 3- and 5-vertex match and all 16 photon placements: the
two-photon factorisations are exactly the 13 (word, i, j) cells found at q = 2 and 3, and
every other cell has Gröbner basis [1]. So no other match is a two-photon product for
generic q. Finitely many special q (where a leading coefficient vanishes) are not
excluded. Over ℚ(q) the weights are again unique: −h⁻¹ = −q/(q²−1), −1, and μ = h⁻².
Not formalised in Lean; it is a computer-algebra result.

**12.6 Convention-D trace of the pair word (COMPARISON ONLY, not a Q_β prediction).**
Owner's request in thread, "All", covering the option "compute the β-decay trace at z_D on
the two-photon pair word … it would need your OK as a comparison". Trace: the Jimbo quantum
trace Tr(K^{⊗n}ρ(w))/[2]ⁿ, which is the convention-D Markov trace (tr σ = z_D = q³/(q²+1),
checked). Exact values:

| word | strands | tr_D |
|---|---|---|
| pair σ₀²σ₁⁻¹σ₄⁻¹ | 6 | (q⁴+1) / (q²(q²+1)³) |
| Hopf photon σ₀²σ₁⁻¹ | 3 | (q⁴+1) / (q(q²+1)²) |
| crossing photon σ⁻¹ | 2 | 1 / (q(q²+1)) |
| electron σ₀σ₁σ₀ | 3 | q³(q⁴+1) / (q²+1)² |

tr(pair) = tr(Hopf photon)·tr(crossing photon), as Markov factorisation over disjoint
strands requires (checked). At the proton q₀ with the canonical tower-summed E₀,
|tr_D(pair)|·E₀ = 0.776939463185 MeV; CODATA Q_β = 0.78233 MeV, a −0.69 % gap. All 264
matching γγ words give this one value for the e⁻ + ν̄ + loop orientation (they have writhe
0 and close to the same link), and 1.453031 MeV for the mirror.

Why this is not evidence, stated plainly:
- The pair word is not the decay element Δ. The β-decay functional is ε(Δ), with Δ a
  nucleon difference (bean `qou-99qc`); nothing here derives that the pair word replaces it.
- The number depends on choices made outside any derivation: tr(1) = 1 normalisation on six
  strands, which E₀ form (order-zero E₀ gives 0.769312), and which orientation.
- Closeness to CODATA, reached after choosing among those, is the selection-against-target
  pattern the no-fitting rule names. Treat 0.7769 as a coincidence until a derivation says
  why the pair word's trace should be Q_β/E₀.
- The ruled z_D base on the ruled element stays at −43 %; this does not change it.

**Owner ruling 2026-11-22 (decision card, option A "Record as coincidence"):** the
0.7769 MeV value is recorded as a coincidence. It is not wired to any dashboard, ladder or
content block, and no derivation route for "pair-word trace = Q_β/E₀" is opened on its
strength. It may be revisited only if a derivation independently produces the pair word as
the decay element.

**12.7 Sibling checks (2026-11-22).** The ⁴He thread: no conflict. Its bond letter is
Vᵢ³ = γ(0,0,qh)·γ(0,0,−q⁻¹h), the lone single-crossing interface letters were retired on
2026-11-15, and the γ₃ factor should be traced with right-hand closure (#8800). The ε / Q_β
thread: no conflict, different word. Its Borromean V³ has one factorisation with weights in
ℚ(q), the bar-paired (0,0,qh)·(0,0,−q⁻¹h); the other six need roots of an irreducible
sextic. The pair here is not bar-paired: bar sends (0,−h⁻¹,−1) to (0,h⁻¹,−1), not to the
partner (0,−h⁻¹,0). No general bar-pairing rule for γγ factors is on record, so this neither
supports nor contradicts either result.
