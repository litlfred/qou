---
# qou-vkg5
title: 'GAP: the Ecalle bridge equation (AlienDerivation §4) is unproved'
status: todo
type: task
created_at: 2026-08-08T13:55:07Z
updated_at: 2026-08-08T13:55:07Z
---


`QOU/Mathlib/AlienDerivation.lean`.

Its header used to list four things the file formalizes. Items 3 and 4 were
never in it — a plan read as an inventory. The header now says so (PR #4771).

**§3 is closed**, and the reason it was stuck is worth recording: the obstacle
was a single lemma missing from *Mathlib*, not from this corpus. `Derivation`
has `leibniz`, `leibniz_pow`, `leibniz_inv`, `leibniz_div` but no iterate —
`Nat.choose` appears nowhere under `Mathlib/RingTheory/Derivation/`. Supplied
as `QOU/MathlibExt/DerivationIterateLeibniz.iterate_leibniz`:

    Dⁿ(f·g) = Σ_{k≤n} C(n,k) · Dᵏf · D^{n−k}g

That binomial convolution *is* the Cauchy product of two exponential series,
which is why it is exactly what makes `exp(D)` multiplicative. Also landed:
`exp_leibniz_iff_cross_vanishes` — at `D² = 0`, `(1+D)` is multiplicative **iff**
`Df·Dg = 0`, i.e. at one-instanton order the automorphism property is
*equivalent* to the vanishing of the two-instanton cross-term.

**§4 — the bridge equation — is what remains open.** Écalle's statement relates
the alien derivatives to the ordinary derivative,

    Δ_ω ∘ ∂  −  ∂ ∘ Δ_ω  =  −ω · Δ_ω ,

so that the `Δ_ω` assemble into the "bridge" between the formal and analytic
sides. Nothing in the corpus asserts it and nothing depends on it.

## What a first honest attempt would need

1. **The commutator relation as a structure field, not a theorem.** `Δ_ω` is
   currently a bare `Derivation R A A` with no relation to a distinguished `∂`.
   The bridge equation is a *hypothesis* on the system, so it belongs as a field
   on `AlienDerivationSystem` (or a §3b conditional class) carrying the `−ω·Δ_ω`
   commutator — not as something to be derived from the present data, which
   cannot support it.
2. **Then the consequences are provable.** With the commutator as a hypothesis,
   the standard corollaries (the `Δ_ω` span a graded Lie algebra; `exp` of the
   sum factorises when the `Δ_ω` commute) become algebra, and `iterate_leibniz`
   is already in hand for the `exp` half.

## Do not

Do **not** add the bridge equation as an `axiom`, and do **not** state it as an
unconditional theorem about the existing `AlienDerivationSystem` — per
AGENTS.md §"Axiomatization is NOT a Proof", axiomatising it would not prove it,
and per §3b-cond a hypothesis-carrying class is the honest encoding.

Also unresolved and prior to all of this: the q-native question. C1 **cannot**
be confluenced to the classical setting (`L1 → (x−1)σ²`, not rank 2 —
[`2026-08-08-rsz-c1-infinity-route-closed.md`](../docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md)),
so a classical bridge equation would not transfer to it even once proved.

## LANDED 2026-08-08 — the relation is encoded, with a model that makes it bite

`QOU/Mathlib/AlienBridgeEquation.lean`, sorry-free (PR #4771).

Done exactly as this bean specified — as a **field** on a bundled `BridgeSystem`
(`ord`, `alien : Ω → Derivation`, `weight : Ω → R`, `bridge`), not an `axiom`,
not an unconditional theorem about the existing `AlienDerivationSystem`.

**Derived from the field** (each would fail without it):

| result | content |
|---|---|
| `weight_shift` | `Δ_ω` moves an `∂`-eigenvector of eigenvalue `λ` to one of eigenvalue `λ + ω` — why alien derivatives detect instanton sectors |
| `weight_add_of_comp` | weights **add** under composition: the `Δ_ω` generate a weight-graded algebra |
| `ord_dotted_comm` | the dotted `Δ̇_ω := e_ω·Δ_ω` **commutes with `∂`** — the bridge proper |
| `ord_comm_of_weight_zero` | at weight 0 the relation *is* commutation (sign/placement check) |

**Two checks that it is not decoration**, since a field every system satisfies
would leave the above true but empty:

* `alien_eq_zero_of_ord_comm` — the relation is *incompatible* with `∂`
  commuting with `Δ_ω` at nonzero weight; commutation forces `Δ_ω = 0`.
* A concrete model. Any `(A, D, t)` with `D t = t` gives one on `Ω = ℕ` via
  `Δ_n := tⁿ·D`, weight `n` — the bridge holds *because* `D` scales `tⁿ` by `n`.
  Witnessed by `R[X]` with the Euler operator `X·d/dX`, `t = X`, where
  `Δ₁X = X² ≠ 0`. So: inhabited at **nonzero** weight by a **nonzero** alien
  family, precisely the regime commutation forbids.

Incidental: Mathlib has `Polynomial.derivative` as a linear map and
`derivative_mul` as Leibniz but does not package them as a `Derivation`;
`polyDerivation` does.

## What is still open

1. **`ord_dotted_comm`'s hypothesis is not witnessed concretely.** The Euler
   operator's eigenvalues on `R[X]` are the degrees `≥ 0`, so `R[X]` has no
   element of eigenvalue `−n`. A witness needs Laurent polynomials `R[t,t⁻¹]`
   with `e = t^{−n}`. The theorem is proved; only its hypothesis is so far
   abstract.
2. **The q-native form — the actual blocker for C1.** Everything above is the
   *classical* relation. C1 cannot be confluenced to the classical setting
   (`L1 → (x−1)σ²`, not rank 2), so this does not transfer to it. The q-analogue
   would replace `∂` by the dilation `σ_q : x ↦ qx` and the commutator by a
   q-commutator; what `weight` means there — and whether the eigenvalue shift is
   additive or multiplicative — is not settled.
3. **No analytic construction is claimed to satisfy the relation.** The structure
   says what a system *with* the bridge equation looks like; exhibiting one from
   a resurgent function is untouched.

Item 2 is the one that matters for the C1 residual. Closing is a human action —
leaving status as-is.

## Item 2 ANSWERED 2026-08-08 — multiplicative, and forced; the mixed case is the general one

`QOU/Mathlib/QAlienBridgeEquation.lean`, sorry-free (PR #4771).

The open question was whether the q-native weight shift is additive or
multiplicative. **It is multiplicative, and the dichotomy is forced rather than a
modelling choice.**

The operator being conjugated by is a *derivation* classically and an
*automorphism* in the q-setting (the dilation `σ_q`). Conjugating by a derivation
is a commutator ⇒ additive shift. Conjugating by an automorphism is
`σ ∘ Δ ∘ σ⁻¹`, and an algebra map passes **through** the product `tⁿ·E(−)`,
multiplying by `σ(t)ⁿ` ⇒ multiplicative shift. A derivation would instead have
*differentiated* that product and produced `n` additively.

| setting | operator | relation | shift |
|---|---|---|---|
| classical | derivation `∂` | `⁅∂,Δ_ω⁆ = ω·Δ_ω` | `λ ↦ λ + ω` |
| q-difference | automorphism `σ` | `σΔ_ωσ⁻¹ = c_ω·Δ_ω` | `λ ↦ c_ω·λ` |

**The link is exact, not analogical.** `euler_weight_additive_qweight_multiplicative`:
for the *same* `(A,E,t)` carrying both structures, the two systems have the *same*
alien family `Δ_n = tⁿ·E` on the *same* index `n`; the classical weight is `n` and
the q-weight is `cⁿ`. One grading — the classical weight *is* the index, the
q-weight is the character `c^{(−)}` evaluated on it.

**The owner's third option was right and is the general case.** `QBridgeSystem`
carries a Jordan pair, `σΔ_ωσ⁻¹ = weight ω · Δ_ω + unipotent ω`; `qweight_shift`
shows the semisimple part *multiplies* the eigenvalue while the unipotent part
*adds* a correction. That is the Levi decomposition of the local q-difference
Galois group: a torus of characters `qⁿ` extended by a unipotent part.

Not decorative — there is a genuinely mixed model. With `σ t = t + 1` and
`σDσ⁻¹ = D`, the derivation `Δ := t·D` has `σΔσ⁻¹ = 1·Δ + D`: trivial semisimple
weight, all content unipotent. `σ t = t + 1` is the defining property of the
**q-logarithm** (`σ_q ℓ_q = ℓ_q + 1`), which generates exactly the unipotent part.
Witnessed concretely on `R[X]` by the shift `X ↦ X+1` with `Δ = X·d/dX`, unipotent
part `d/dX ≠ 0` (`polyUnipotentSystem_not_isSemisimple`).

Also landed: `conjDeriv` (conjugating a `Derivation` by an `AlgEquiv` is a
`Derivation` — Mathlib has both halves, not this), `qweight_mul_of_comp` (weights
**multiply** under composition), `alien_eq_zero_of_dil_comm` (teeth; note the
degenerate value is `c_ω = 1`, not `0`).

## Remaining on this bean

1. **`ord_dotted_comm`'s hypothesis still lacks a concrete witness** (classical
   file) — needs Laurent polynomials `R[t,t⁻¹]` for an element of `∂`-eigenvalue
   `−n`.
2. **No analytic q-difference module is claimed to satisfy the q-bridge**, C1
   included. The structure says what such a system looks like and what follows;
   exhibiting one from a resurgent q-series — and identifying C1's actual weights
   — is untouched. **This is now the whole remaining gap for the C1 residual**;
   the additive-vs-multiplicative ambiguity that blocked it is gone.

Closing is a human action — leaving status as-is.

## 2026-08-08 (later) — the twist, E_q proved forced, and where the gap now sits

Three further commits on PR #4771, all sorry-free.

### A correction to my own structure

`QBridgeSystem` (committed an hour earlier) assumed `σ ∘ Δ_ω ∘ σ⁻¹` is a multiple
of **`Δ_ω` itself** — the same index. For q-difference equations that is an
over-restriction: the dilation acts on the Borel plane too, so it moves a
singularity at `ω` to `qω`. `TwistedQBridgeSystem` carries the shift;
`QBridgeSystem` is exactly the `shift = id` case (`toTwisted` / `untwist`), so
nothing proved earlier is lost.

### What was prose is now theorems

The earlier commit *asserted* in a docstring that `E_q` is the right base. Proved,
in three pieces:

| theorem | content |
|---|---|
| `QGevreyTaming.qBorelCoeff_dilate` | the q-Borel transform intertwines the two dilations, `B(qⁿ·aₙ) = qⁿ·B(aₙ)` — the one step of the argument that is a computation, and the reason the singularity moves at all |
| `shift_mul_eq_id_iff` | with `shift ω = q·ω`, the shift is the identity **iff `q = 1`** — so on `ℂ*` the untwisted form is simply unavailable for a genuine dilation |
| `untwist` | the twist vanishes exactly when the alien family is shift-invariant, i.e. constant along q-spirals, i.e. factors through `ℂ*/q^ℤ` |

Together: **`E_q` is not a convenient base, it is the unique quotient on which the
bridge relation can be index-preserving.** Independent corroboration of the
corpus's `E_q` framing (`qou-qbe9x`, where `x = q⁻²` was found to be the identity
orbit `[q⁻²] = [1]`).

`conjDeriv_iterate` is the content of the twist when it is *not* removed:
`σⁿΔ_ωσ⁻ⁿ = (∏_{k<n} c_{shiftᵏω})·Δ_{shiftⁿω}` — weights accumulate along the
orbit.

### Every field now has a concrete witness

`polyQEulerSystem` — `R[X]` with a genuine q-dilation `X ↦ c·X` (an `AlgEquiv`,
which is the whole point) and the Euler operator. `polyQEuler_weights`
instantiates the punchline concretely: same family, same index `n`, classical
weight `n`, q-weight `cⁿ`. Combined with the unipotent model, the semisimple
weight, the unipotent part, and the classical/q contrast all have models.

### Where the gap is now

**Narrowed twice, not closed.**

1. ~~additive or multiplicative~~ — **answered**: multiplicative, forced, mixed in
   general.
2. ~~which index set~~ — **answered**: `E_q`, proved forced.
3. **Open: C1's actual weights.** No analytic q-difference module is exhibited
   satisfying the relation. This needs the q-Borel/Laplace construction
   (sector-dependent summation, the theta-function jump) — the old S3, correctly
   flagged then as "genuinely multi-session; not a session brick". It has not
   become cheaper.

A **prune** narrowing where to look: `monomial_eigenvalue_mem_zpowers` — the
dilation's monomial eigenvalues `qⁿ` all lie in the identity class of `E_q`, so
the monomial grading cannot exhibit a weight at all. Scope-(a): for C1's `∞` the
weight would have to come from the *quadratic* factor certified by
`deg_q(cₙ) = n²`, not from the powers of `x`. This says where not to look; it does
not say C1's weight is trivial.

Closing is a human action — leaving status as-is.

## 2026-08-08 (later still) — the weight LATTICE is pinned; the weight is not

`QOU/QBeta/C1NewtonRamification.lean`, sorry-free.

Three of the four sub-questions are now answered:

| question | state |
|---|---|
| additive or multiplicative? | **multiplicative**, forced; mixed in general |
| which index set? | **`E_q`**, proved forced |
| which multiplicative group? | **`q^{½ℤ}`, up to the deck sign** — below |
| the actual weight? | **OPEN** |

**The lattice.** Chain, with its one non-Lean step named:

1. *[standard q-difference theory, not proved here]* slope denominator `s` ⇒
   ramification index `s`; C1 at `∞` has `s = 2`, so `ζ² = x`. Not a fresh
   assumption — PR #4721's degree budget independently found ramify-then-level-2
   is the only pairing with sub-quadratic leftover (`ramified_qBorel_budget`,
   `m² = m(m−1) + m`).
2. *[proved]* the dilation lifts to `ζ ↦ c·ζ` with `c² = q`, and `q` is **not a
   square** in `ℚ[q]` (degree parity, same argument as the existing
   `not_isSquare_newtonEdgeConstant`) — so no lift over the base field.
3. *[proved]* two lifts differ by exactly a sign: the deck group `ℤ/2` is the
   whole ambiguity.
4. *[proved]* `c^{2k} = q^k` but `c^{2k+1} = c·q^k` — the group generated is
   `q^ℤ ⊔ c·q^ℤ`, index 2 over `q^ℤ`.

Reading, scope-(a): **the weight lies in `q^{½ℤ}`, determined up to the deck
sign.** The half-integrality is forced by the slope being `½`; the sign ambiguity
*is* the ramification.

## The one remaining item

**Compute C1's actual weight.** Needs the analytic q-Borel/Laplace construction —
sector-dependent summation and the theta-function jump. This is the old S3,
flagged when the plan was written as "genuinely multi-session; not a session
brick", and nothing since has made it cheaper. Everything landed on this branch
constrains that computation rather than performing it.

Two prunes now bound the search for it:

* `monomial_eigenvalue_mem_zpowers` — the monomial grading cannot exhibit a
  weight at all (its eigenvalues `qⁿ` are all the identity class of `E_q`), so the
  weight must come from the quadratic factor certified by `deg_q(cₙ) = n²`.
* the lattice above — whatever it is, it is a half-integral power of `q` up to
  sign. A candidate outside `q^{½ℤ}` is wrong without further computation.

Closing is a human action — leaving status as-is.

## ATTACK OPTIONS for the remaining item (C1's `∞` weight)

Three routes, ranked by cost/decisiveness. **Option B has already paid off in
part** — its `0`-side half is landed (below), which is what makes it the
recommended entry point.

### Option B — connection / indicial route  ← RECOMMENDED, partly landed

The two ends are *not* symmetric, and that asymmetry is exploitable: `0` is
**Fuchsian**, so its weights are the roots of an indicial equation — pure
algebra, no analysis. `∞` is irregular. The Birkhoff connection matrix ties them,
and the `∞` weight is the theta-quasi-periodicity of that matrix.

**Landed** (`QOU/QBeta/C1FuchsianExponents.lean`, sorry-free): C1's `0`-side
weights are the roots of

    t² + (q−1)·t + (q−1) = 0,   discriminant q² − 6q + 5 = (q−1)(q−5)

derived two independent ways (evaluating coefficients at `x = 0`; and as the
resonance condition of the actual recurrence `bₙ[q^{2n} + (q−1)qⁿ + (q−1)] =
q^{2n}b_{n−1}`). Proved: the discriminant is **not a square in `ℚ[q]`**, so the
`0`-weights are irrational over `ℚ(q)`. Note the proof needs a *multiplicity*
argument, not the degree parity that worked on the `∞` side — the degree is even,
so parity is silent; `(q−1)(q−5)` has simple roots.

**Remaining:** build the connection matrix and read its quasi-periodicity. Needs
the `0`-side solution basis (q-hypergeometric, explicit) and the `∞`-side formal
basis (have it: `deg_q(cₙ) = n²`). Decisive if it closes.

### Option A — theta functional equation

For slope `½`, the instanton factor on the ramified cover `ζ² = x` is a Jacobi
theta in `ζ` with base `√q`. `θ(qx) = x·θ(x)` for the normalisation
`θ(x) = Σ q^{−n(n+1)/2}xⁿ`; the weight is then the `σ`-eigenvalue of that factor
under `ζ ↦ c·ζ`, `c² = q`. Consistent with the proved lattice `q^{½ℤ}`.

**Hazard, stated up front:** this is the route most likely to produce a
plausible-but-wrong answer, because the theta normalisation is convention-heavy
and several inequivalent conventions are in circulation. Pin the normalisation
against a cited source *before* computing, and check the result reproduces the
proved lattice and the proved deck-sign ambiguity. Do not report a weight from
this route without an independent cross-check.

### Option C — numerical probe

Sum the divergent `∞` series in two sectors at high precision and difference
them. **This is a check, never a derivation** — a constant extracted this way is
a fit and must be labelled one (AGENTS.md anti-fit). Useful only to *falsify* a
candidate from A or B.

### Constraints any answer must satisfy (already proved — use as filters)

1. multiplicative, on `E_q` — not additive, not on `ℂ*`
2. in `q^{½ℤ}`, up to the deck sign (`dilationLift_*`)
3. not visible in the monomial grading (`monomial_eigenvalue_mem_zpowers`) — must
   come from the quadratic `deg_q(cₙ) = n²` factor
4. the `∞` ramification constant is `√(q−1)`, non-removable
   (`not_isSquare_newtonEdgeConstant`)

A candidate failing any of these is wrong before any further computation.
