---
# qou-offl
title: 'Route 1 (parent: qnnq): off-lattice ϑ_K = cone-manifold / generalized-Dehn-filling deformation. Non-integer (m,ℓ) is standard geometry: Thurston generalized Dehn surgery coefficients ∈ ℝ², Hodgson–Kerckhoff cone-manifold rigidity, Gukov/Murakami generalized volume conjecture (continuous parameter u off the complete structure). Probe: fit probed ϑ values (4₁: proton 0.203, muon 0.059) to real filling coefficients on the NZ volume function; Lean: conditional NZ dVol/du statement.'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-07-31T19:30:00Z
updated_at: 2026-10-04T15:15:05Z
parent: qou-n4nr
---

Literature anchors:
- Gukov, "Three-dimensional quantum gravity, Chern-Simons theory, and the A-polynomial" — generalized volume conjecture, continuous u.
- H. Murakami — cone-manifold volumes from deformed colored Jones limits (figure-eight AND Borromean rings; the latter feeds qou-mcus).
- Hodgson–Kerckhoff, "Rigidity of hyperbolic cone-manifolds and hyperbolic Dehn surgery" (JDG 48, 1998) — real cone angles are rigid: an off-lattice ϑ is a well-defined geometric datum, not a fudge.
- Neumann–Zagier volume function Φ(u) for the derivative structure.

The T4-inverted ϑ values are NOT on the (√3/2)·ln q₀ integer lattice — this route says they shouldn't be: the braid word determines a real slope (generalized filling coefficient), quantization to ℤ² is only for closed fillings.


---

## 2026-08-01 RE-SPEC — this is now the arc's live independent leg (PR #4513)

`qou-rdmr` is refuted at scope (a), so this is the remaining candidate for an
`A_ω`-independent determination of ϑ. Two corrections + a test spec.

### Correction 1 — do NOT fit to the T4 ϑ values

This bean says to "fit probed ϑ values to real filling coefficients". Those ϑ
are T4-inverted and therefore `A_ω`-conditioned (see the circularity note);
fitting to them is exactly the `circ-derived-used-as-input` defect. Predict
from geometry first; compare after.

### Correction 2 — the anchors are two DIFFERENT knots

"4₁: proton 0.203, muon 0.059" is wrong. Per `qbeta_t3_multiknot_binding_probe.py`:
muon → 4₁ (figure-eight), proton → 𝔹₃ (Borromean). Two knots, two words.

### The acceptance test (new — this is what makes the route well-posed)

Eliminating `A_ω` between the two anchor equations leaves an invariant built
from measured `S` alone — no `A_ω`, no `q₀`:

    (ln²q₀ − ϑ_μ²) / (ln²q₀ − ϑ_p²)  =  S_μ/S_p  =  −0.2453912076

Solved: ϑ_p² = L − (L − ϑ_μ²)/r,  L = ln²q₀.

**Test:** produce ϑ for BOTH 4₁ and 𝔹₃ from cone-manifold geometry alone, then
check the pair against the curve. Landing on it DETERMINES
`A_ω = S_μ/(κ(L − ϑ_μ²))` — the arc's first genuine determination rather than a
literature import. Missing it refutes the route at scope (a).

### Two hazards to design against

- **Re-parameterization.** If the geometric ϑ carries its own free
  normalization, the route has moved the degree of freedom, not removed it. The
  test is immune only if the normalization is fixed BEFORE the comparison.
  State it up front.
- **Single-anchor fitting.** Any route can hit ONE ϑ by choosing its
  normalization. The curve is a genuine test precisely because it constrains
  the PAIR; a one-anchor match establishes nothing.

Curve: computations/probes/qbeta_qnnq_afree_theta_constraint_probe.py
Note:  docs/scope/2026-08-01-theta-independent-routes.md §2-§3


### 2026-08-01 addendum — a whole SHAPE of candidate is already ruled out

Derived before any geometry (formalize-first). Two anchor equations, three
unknowns: ONE extra scalar closes the system exactly (zero residual, nothing
to check); TWO over-determine by one and leave a failable residual.

So a route supplying a RATIO ϑ_p/ϑ_μ is **unfalsifiable by construction**.
Verified concretely: ρ(A) is a monotone bijection from A ∈ (A_crit, ∞) onto
ρ ∈ (1, ∞), running ~598 → 1.005. Every ratio > 1 is attained by exactly one
A, so no ratio candidate can be refuted — it only NAMES an A.

Worse, plausible geometric ratios cluster: Vol(𝔹₃)/Vol(4₁) → A = 2.909,
2√3 → 2.990, cusp count 3/1 → 3.344. Three of six candidates inside
A ∈ [2.5, 4], which is a mere ~2× band in ρ. A "match near 3" is close to
guaranteed. **Do not reach for the 2√3 row because it forces A = 2.990.**

NET REQUIREMENT: supply BOTH ϑ absolutely, normalization fixed in advance.

Probe: computations/probes/qbeta_offl_ratio_candidates_unfalsifiable_probe.py


### 2026-08-07 corpus-grep after the 796-commit main catch-up

Ran the corpus-grep that should have preceded the 2026-08-01 re-spec. Two
pre-existing corpus objects bear directly on this route. **Neither is new (both
landed 2026-07-27, before that re-spec) — this is a miss, not a new landing.**

**1. WARNING — the obvious construction is already excluded.**
`QOU/Knot/FigureEightDeformedMeridianWinding.lean` (sorry-free) proves the
substrate-matched Murakami meridian datum `u = N*t - 2*pi*i*k` has
`Im u = -2*pi*k`, hence `|u| >= 2*pi` for every `k >= 1` — structurally OUTSIDE
Murakami's controlled small-|u| neighbourhood where `Vol(4_1; u)` tracks the
geometric branch.

This bean's stated machinery IS Murakami's continuous-u deformation, so the most
obvious offl construction is already refuted at scope (a). Not a refutation of
the whole route — that exclusion was derived under `q_eval = q0` matching (the
anchor-free-q0 question), which theta_K does not require. But offl must now
**state which matching it uses and why it escapes |u| >= 2*pi**. New
precondition; cheap to state, cheap to check.

**2. CANDIDATE — the missing absolute normalization may already exist.**
`QOU/Knot/CuspShapeBarParity.lean`: 4_1's cusp shape is `omega = e^{i*pi/3}`;
the bar split gives bar-even `omega + omega^-1 = 1` (Vol / rational side) and
bar-odd `omega - omega^-1` with `(barOdd omega)^2 = -3` (the sqrt(-3),
Chern-Simons / Im V axis). It identifies the meridian as the **bar-odd (boost)
cycle** and puts `q` on the boost hyperbola `barEven q^2 - barOdd q^2 = 4`.

The T4 channel `ln^2 q0 - theta^2` carries exactly that Minkowski signature, and
the T4 probe's own language is "boost-dominated (theta < ln q0)" /
"spin-dominated (theta > ln q0)". So the corpus already contains a candidate
IDENTIFICATION of what theta is — the bar-odd / CS component against ln q0's
bar-even / Vol component — which is precisely the "normalization fixed in
advance" this route was told it needs.

**STATED AS A CANDIDATE, NOT A FINDING.** The signature match is suggestive;
`ln^2 q0 - theta^2` is a quadratic form in (ln q0, theta), not literally
`barEven^2 - barOdd^2`. The identification is unverified.

**And the obvious reading of it is dead on arrival.** 4_1 cusp field Q(sqrt-3)
-> angle pi/3; Borromean cusp field Q(i) -> pi/2; ratio 3/2. That is a RATIO,
which this bean's 2026-08-01 addendum proves unfalsifiable — it merely names
`A = 10.35` (the rho = 1.5 row of the U2 table) and cannot be tested. Exactly
the trap: the cusp-shape route must yield theta ABSOLUTELY, per knot, or it
buys nothing.

## Progress (Round 57)
- Round 57 (`litlfred/qou#8213`, commit `2301811899d7f5b7e6235c29e2d41d3e068ef89b`): Added `meridian_normSq_strict_mono_winding` and `off_lattice_inside_disk_ne_meridian` in `FigureEightDeformedMeridianWinding.lean` plus 80-dps mpmath witness.
