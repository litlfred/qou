# A_ω normalization capstone — the one-instanton map, from the literature (2026-07-25)

**PR:** #4246. **Branch:** `claude/aomega-5two-weight-normalization-2026-07-25`.
**Continues:** #4213 (GZ weight rule, merged), the 5₂ weight instance (this PR).

## The question

The A_ω *rigidity* leg (that A_ω carries zero fitting freedom) is closed on main
(boundedness + divisor routes). The A_ω *value* — the **`Im 𝔙_q → N_odd`
normalization** (`docs/scope/2026-07-18-im-vq-to-nodd-normalization-capstone.md`) —
is the single genuinely-open capstone: what is the structural map from the fibre-level
Stokes datum `O = ½(S⁺−S⁻)` (5₂, derived, calibration-free) to the archimedean
observable `N_odd(q) = S(q)·u³`?

## The literature answer — the one-instanton imaginary-part formula

A literature pass (Écalle; Garoufalidis–Gu–Mariño resurgence of complex Chern–Simons;
Fantini–Rella) identifies the map as the **standard one-instanton discontinuity
formula** of resurgence. The corpus already states the two halves:

- the **bridge equation** `Δ_ω f̃ = A_ω · ∂f̃` with `A_ω` the Stokes constant
  (`ecalle-borel-resurgence-vocabulary.md`);
- **`st` = median resummation** (`st-is-median-resummation.md`): the standard-part map
  projecting the fibre value to ℝ *is* the real single-valued (median) Borel sum;
- a **scope-b proof** that the bridge map is *necessarily* a Borel/median resummation
  (even channel Gevrey-1 divergent, odd channel convergent ⇒ no term-by-term bridge;
  `2026-07-12-borel-alien-calculus-utilization-audit.md`).

The missing piece is the **geometric identification of the numerator**. The
literature's one-instanton formula supplies its shape: for a real series whose Stokes
ray is ℝ₊, the lateral ambiguity is purely imaginary, and at one-instanton order

> `N_odd(q₀) = Im 𝔙_q(q₀) = ½(s⁺−s⁻)[φ_K](q₀) = 𝒜_K · e^{ −Re 𝔙_K(q₀)/(π ℏ_q(q₀)) } · sin( Im 𝔙_K(q₀)/(π ℏ_q(q₀)) ) · P(q₀)`
> `                                              ≕ M(q₀) · Z(q₀)`

with

- **`𝒜_K` the integer Stokes amplitude** — the `b = κ(σ) − κ(σ′) = 0` weight branch
  (the geometric↔conjugate ray, both non-trivial), i.e. exactly the `Ind^rot` integer
  the merged `GZWeightSelection` (#4213) and this PR's `GZWeightGeneral` (5₂ instance)
  certify. **Not** the refuted half-integer `β = 3/2` (that is `κ(σ₀)`, the *trivial*
  connection's Kashaev-prefactor weight — a type error, `2026-07-25-beta-three-halves-…`);
- the **anchor-dependence entirely in the exponent** `𝔙_K(q₀)/(π ℏ_q(q₀))`, evaluated
  at the moving substrate q₀ — matching capstone constraint 4;
- the **simple zero at q\*** where `Im 𝔙_K` crosses zero (`𝔙_K` becomes real, an
  amphichiral-type locus) — a *geometric* origin for `N_odd(q*) = 0`.

Borel singularities sit at `ω_{ij} = (CS_i − CS_j)/2πi` (complex-volume differences);
the Stokes constants are the integer DT/BPS rotated 3d-indices (GGM Conj. 2). Sources:
GGM [2007.10190](https://arxiv.org/abs/2007.10190), [2012.00062](https://arxiv.org/abs/2012.00062),
[2111.04763](https://arxiv.org/abs/2111.04763); Garoufalidis–Zagier
[2111.06645](https://arxiv.org/abs/2111.06645); Fantini–Rella
[2404.11550](https://arxiv.org/abs/2404.11550); Écalle (1981).

## The structural-consistency finding (Lean, this PR)

`QOU/QBeta/OneInstantonNormalization.lean` (sorry-free, `lean`-direct exit 0) proves
the one-instanton form is **structurally consistent** with the committed
`BarOddLadderShape`, not merely conjectured to fit:

- `numerator_hasDerivAt_at_zero` — for `A = M·Z` with `Z(q*) = 0`, the slope at `q*` is
  `M(q*)·Z′(q*)`; the `M′·Z` term is killed by the simple zero. So the smooth
  exponential amplitude `M`'s own log-derivative **drops out** at `q*`.
- `barOddLadderShape_of_oneInstanton` — the one-instanton `A = M·Z` (with the geometric
  zero and positive combined slope `M(q*)·Z′ > 0`) **inhabits** `BarOddLadderShape`
  with `A′ = M(q*)·Z′`.
- `hasDerivAt_S_at_qstar_oneInstanton` — hence the geometric `S`-slope at `q*` is the
  pure static lever `M(q*)·Z′/u(q*)³`, log-derivative-free.

**Why this matters.** `BarOddLadderShape.hasDerivAt_S_at_qstar` (the committed
exactness: the `S`-slope at `q*` has *zero log-derivative correction*) is **not** an
extra hypothesis the one-instanton form must be checked against — it is an **automatic
consequence** of the product shape `M·Z` at a simple zero of `Z`. The committed
exactness that looked like a constraint is a *prediction* of the one-instanton map.
This turns the capstone from "does the class fit?" into a single **magnitude
identification**: `M(q*)·Z′ = A′ ≈ +2.37`.

## Honesty / scope (STRICT)

This is a **conditional** result (§3b-cond; conditional-proved ≠ premise-established):
it proves *one-instanton structure ⇒ `BarOddLadderShape` numerator*, **not** that the
actual geometric `𝔙_q` has that structure. The identification of `M, Z` with the real
`Im 𝔙_q(q₀)` data, and the magnitude match to `A′ ≈ +2.37`, remain the open capstone
(`conj:algebraic-geometric-dilog-equivalence`). Nothing is wired; no instance for the
actual `𝔙_q` is exhibited. No fit.

## The concrete open next step (well-defined magnitude probe)

Compute, from the corpus geometric `𝔙_q` data (the anchor-smooth quantum volume,
`|d𝔙/dq| ≈ 1.47` for 5₂ σ1, cornering-capstone census) and `ℏ_q(q*)`:

1. `M(q*) = 𝒜_K · e^{−Re 𝔙_K(q*)/(π ℏ_q(q*))} · P(q*)` (integer amplitude × exp × prefactor);
2. `Z′(q*) = d/dq[ sin(Im 𝔙_K/(π ℏ_q)) ]|_{q*} = (Im 𝔙_K/(π ℏ_q))′(q*)` (phase slope at the Im-zero);
3. test `M(q*)·Z′(q*) ≟ A′ ≈ +2.37`.

A match confirms the one-instanton normalization map (closing the value capstone); a
miss is a genuine scope-(a) constraint on the amplitude/prefactor, not a refutation of
the ingredient (the structural consistency above stands regardless). This is the
formalize-first-pruned successor to `β = 3/2` — the invariant (integer `b=0` amplitude,
exponent-carried anchor-dependence, log-derivative-free slope at the Im-zero) is fixed
*before* the numerical evaluation.
