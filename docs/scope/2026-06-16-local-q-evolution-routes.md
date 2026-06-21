# Local-q evolution: germ-dynamics (route 2) and fixed-point selection (route 1) — sketches

**Date:** 2026-06-16
**Status:** EXPLORATORY SKETCH — not paper content. Route 2 assembles two
existing blocks with a clearly-labeled ansatz for the evolution law;
route 1 is a re-opened research direction with the naive form refuted.
Validity assessment: [`docs/audits/2026-06-16-q-anchor-drift-and-local-q-routes.md`](../audits/2026-06-16-q-anchor-drift-and-local-q-routes.md) Part B.

---

## Route 2 — germ-dynamics of `δq(p)` (✅ mostly exists)

### Step 1 — the germ `δq(p)` already lives in the corpus

[`two-observer-parallelogram.md`](../../content/quantum-observable-universe/quantum-observable-universes/two-observer-parallelogram.md):
two independent observations at a point `p` each perturb the substrate
by `δq_i(p)`, giving shifted parameters `q_i'(p) = q(p) + δq_i(p)`, and
the obstruction is the **commutator of observations**

$$
[\mathfrak{O}_{1,p}, \mathfrak{O}_{2,p}](\alpha_p)
  = [q_1'(p),\, q_2'(p)] \cdot (\alpha_V)_p
  = [\delta q_1(p),\, \delta q_2(p)] \cdot (\alpha_V)_p,
$$

since `q(p)` is central (it lives in `End(𝟙)`). So the **germ-level
non-commutativity of two observations is the local seed of `δq`** — and
it acts only on the fermionic component `(α_V)_p` (vanishes on bosons).

### Step 2 — identify the germ commutator with the q-connection curvature

In the archimedean realisation `A = C^∞(M)`, the germ algebra
`A/𝔪_p² = C^∞_p(M)/𝔪_p²` is the first jet at `p`. Two observations are
two transport directions `X_1, X_2 ∈ T_pM`; the "parallelogram"
(transport along `X_1` then `X_2` minus the reverse) over an
area element `dA = X_1 ∧ X_2` picks up holonomy = curvature × area.
Identifying the parallelogram commutator with the curvature 2-form of the
**q-flat connection** ([`q-flat-connection.md`](../../content/quantum-observable-universe/q-geometric-langlands/q-flat-connection.md)):

$$
[\delta q_1(p),\, \delta q_2(p)]
  \;\simeq\;
  \nabla_q^2(X_1, X_2)
  \;=\;
  (q-1)\,\mathcal{F}_q^{\mathrm{intr}}(X_1, X_2)
  \;+\;
  \mathcal{F}_q^{\mathrm{conn}}(X_1, X_2).
$$

This is the bridge `two-observer-parallelogram → q-flat-connection`: the
local disagreement of observers **is** the q-curvature evaluated on the
loop. In vacuum (`q`-flat, `𝓕_q^conn = 0`) only the perpetual intrinsic
term `(q-1)𝓕_q^intr` survives; matter turns on `𝓕_q^conn`.

### Step 3 — an evolution law (ANSATZ, not derived)

The only missing piece is *time evolution* of `q(p)`. The natural
candidate uses the existing **q-heat equation**
([`q-gaussian-solves-q-heat.md`](../../content/quantum-observable-universe/information-theory/q-gaussian-solves-q-heat.md)),
whose fundamental solution is the Reeb-invariant q-Gaussian with the
clock running at rate `q⁻²`. Promote `q(p)` itself to the diffusing
field — a **q-harmonic-map heat flow**:

$$
\partial_t\, q \;=\; -\Delta_q\, q,
\qquad
\Delta_q = q^{-2}\Delta + q^{-1}(1-q^{-1})\mathfrak{C} + (1-q^{-1})^2 \Delta_\xi .
$$

> **Honesty flag.** `q-gaussian-solves-q-heat` governs diffusion of a
> scalar density *at fixed `q`*. Making `q(p)` itself the field that
> diffuses is a **new postulate**, not a theorem in the corpus. What is
> solid: (i) the germ `δq(p)` (Step 1, exists); (ii) its identification
> with q-curvature (Step 2, standard differential geometry on an existing
> block). What is an ansatz: the specific PDE in Step 3. Report it as
> such.

**Fixed points** of this flow are the q-harmonic sections `Δ_q q = 0`;
the vacuum constant `q ≡ q₀` is the trivial one. This is the hand-off to
route 1.

---

## Route 1 — `q₀` as a fixed point (⚠ naive form refuted; reframed)

### The stated condition does NOT select `q₀`

`∇_q² = (q-1)𝓕_q^intr` holds for **every** `q` — it is the *definition*
of `q`-flatness with intrinsic curvature, parametric in `q`. It cannot
single out the numerical `q₀ ≈ 1.1097`. **The naive route is false.**
(Refuting this saves a numerical chase — formalize-first discipline.)

### A selection condition needs an extra equation

`substrate-parameter.md` states `q` is "*not* intrinsic to the triple…
records where one sits in the `𝔾_m`-family" — i.e. `q₀` is a **modulus**.
Selecting it requires distinguishing one point of the `𝔾_m`-family.
Candidate conditions (all conjectural; consistent with the candidate list
in [`epistemic-status-of-calibrations.md`](../../content/quantum-observable-universe/observations/epistemic-status-of-calibrations.md)):

1. **Curvature extremum.** `q₀ = ` critical point of the intrinsic-curvature
   functional `q ↦ ‖(q-1)\mathcal{F}_q^{\mathrm{intr}}‖`. Needs the explicit
   `q`-dependence of `‖𝓕_q^intr‖` from `κ_0` under HKR — open.
2. **Reeb closed-orbit / period-integrality.** `q₀` where a period
   `∮_{Reeb} ω_q ∈ ℤ` (quantization). Matches the "K-theoretic period /
   Bring `χ=−6` fixed-point" candidates.
3. **q-harmonic stationarity with a Reeb source.** `q₀` as the nontrivial
   stationary point of the route-2 flow that balances `(q-1)𝓕_q^intr`
   against the Reeb-fibre source — couples routes 1 and 2.

> **Scope flag (STRICT).** Substrate-derivation of `q₀` was **declined
> 2026-05-08** (AGENTS.md Subgoal-2) and **re-opened** by the owner
> question driving this session. These remain research directions /
> conjectures — not to be wired to production or quoted as derived until
> a closure clears the three-calibration discipline review.

---

## What is worth doing next (no probe run here — formalize-first)

| # | Item | Type | Gate |
|---|---|---|---|
| 2a | Author the Step-2 identification as a `proposition` (germ commutator = q-curvature on the loop) — it IS provable from existing blocks | paper content | Lean + validation tooling (currently absent on checkout) |
| 2b | Author the Step-3 flow as a `conjecture` block (q-harmonic heat flow), PDE labeled ansatz | paper content | — |
| 1a | Derive `‖(q-1)𝓕_q^intr‖(q)` explicitly, then test for a critical point near `q₀` | compute probe | needs `pyhecke_native` / κ_0 HKR; owner-gated (re-opened) |
