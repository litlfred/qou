# The boundary deficit of a bounded-degree bond count derives the SEMF **surface shape** — and its magnitude test is **generic**, by the corpus's own genericity guard applied to itself

**Date:** 2026-09-05 · **Beans:** `qou-kqdn` (this), `qou-rav3` (the guard this applies to itself),
`qou-yau0` (the re-promotion that motivated it), `qou-brng`, `qou-ib3g` · **Arc:** binding law /
extensive term · **Scope:** formalize-first Lean (sorry-free) plus a probe whose **main finding is
against the probe's own magnitude claim**. **Nothing is wired, nothing is fitted.**

## 1. Why, and what was open

`qou-yau0` (#6690) re-promoted the surface term: on the artifact-free normalised law the residual's
surface correlation is **−0.298**, not the −0.178 that #6611 demoted it on, and the SEMF projection
sits at `R² = 0.96`. #6611's decision frame Avenue 2 names the test — *"an edge set derived from the
braid geometry rather than assumed, which adds surface behaviour with no new constant"*.

`QOU.Mass.CoordinationSaturation` on main gives **every** nucleon `k` neighbours (`k·A/2` bonds), so
`B/A = ε·k/2` exactly: a pure volume term. A finite cluster cannot do that — boundary nucleons have
fewer neighbours. That deficit had never been computed.

**Corpus-grep, six paths (path 0 unavailable: the `paper-assistant` MCP server failed to connect,
so a differently-worded prior approach could have been missed).** The boundary-deficit bond count is
**open**: proposed 2026-05-02 (`2026-05-02-level-1-binding-energy-probe.md` §Term 2, *"Status. Not
currently implemented"*), re-proposed 2026-09-04 (Avenue 2), never built and never refuted. Four
nearby closures were checked and **none reaches it**:

| closure | scope | why it does not reach this |
|---|---|---|
| `CoordinationSaturation.bounded_degree_saturates` | positive, `k·A/2` exactly | it is the `c = 0` special case of this object |
| `ChainBondOrderDependence.orderIndependent_iff` | (b), chain arrangement-dependence | its own text prescribes *"change the bond set — a coordination graph"* |
| 2026-06-10 bond-graph audit | static **integer** edge multisets, `A ≤ 4` | this deficit is non-integer and asymptotic |
| `UniformBondSimpleGraphExclusion.b3Uniform_nonpos` | (b), `b₃ ≤ 0` for uniform-bond simple graphs | **does** bite: this must not be claimed to explain `b₃ = +1.426 MeV > 0` |

Distinguished from the one scope-(a) negative nearby: `av_surface_correction_probe.py` refutes a
surface term bolted onto `B_vol = a_V·A` at the **net** saturation scale, which double-counts. This
is a correction to a bond **count** under the log law, a different object.

## 2. Lean — `QOU/Mass/CoordinationSurfaceDeficit.lean` (sorry-free, 6 declarations axiom-clean)

| declaration | statement |
|---|---|
| `bondCount_split` | `M = (k·A_int + k'·A_surf)/2 = k·A/2 − (k−k')·A_surf/2` — the deficit, exactly |
| `perNucleon_split` | `B/A = ε·k/2 − (ε(k−k')/2)·(A_surf/A)` — volume term plus a deficit with the SEMF sign |
| **`perNucleon_surfaceLaw`** | under `A_surf = c·A^{2/3}`: `B/A = ε·k/2 − (ε c (k−k')/2)·A^{−1/3}` — **the SEMF volume-minus-surface shape** |
| `perNucleon_lt_plateau` | `k' < k` and a boundary ⇒ `B/A < ε·k/2`: the plateau is approached **from below** |
| `perNucleon_tendsto_plateau` | `B/A → ε·k/2` as `A → ∞` — `bounded_degree_saturates` recovered as the limit; this **refines**, does not contradict |
| **`surfaceToVolume_ratio`** | `a_S/a_V = c·(k−k')/k` — **`ε` cancels and `k` cancels**: the ratio depends only on the *fractional* degree loss `1 − k'/k` |

`lean`-direct exit 0; `#print axioms` on all six `= {propext, Classical.choice, Quot.sound}`; zero
`sorry`. Ground ring `ℝ` (§7c: real powers and an order claim).

**Hypothesis, stated as one:** that the coordination graph is a compact 3-D packing with
`A_surf = c·A^{2/3}`. Not proved; an isoperimetric bound for sphere packings is not attempted.
**Not derived:** that the substrate emits such a graph. Avenue 2 asks for the edge set to come from
the **braid geometry**; this assumes a packing instead, which is a weaker input. `qou-brng`'s
linking-vs-self-energy assignment remains the open input.

## 3. Probe — `computations/probes/coordination_surface_deficit_probe.py`, **12/12**

50 dps, 2548 measured AME nuclides, #6611's selection and percentile helpers.

**Data.** Least squares of `B/A` on the full SEMF basis: `a_V = 14.11`, `a_S = 13.55`,
`|a_S/a_V| = 0.9607`, `R² = 0.964`. Textbook SEMF is 1.130. (Volume+surface alone gives 0.528 at
`R² = 0.198` — an under-specified basis, discarded on its own terms, not on matching.)

**Falsification check the Lean makes available, and it passes:** `perNucleon_lt_plateau` says the
plateau is approached from below, so `B/A` must **rise** with `A` over the light nuclei. Median
`B/A` by band: 6.03 → 8.01 → 8.55 (A ≤ 62), then 8.60 → 8.33 → 7.81. Rises, then turns over above
the iron peak — the Coulomb term, outside this file's scope.

**Geometry, computed before the data was consulted.** For a one-shell sphere `c = 3`, so
`a_S/a_V = 3(1 − k'/k)`:

| facet (fcc, `k = 12`) | `k'` | `1 − k'/k` | `a_S/a_V` (leading) | × exact one-shell at `A = 56` |
|---|---:|---:|---:|---:|
| (111) | 9 | 0.250 | 0.750 | 0.571 |
| (100) | 8 | 0.333 | 1.000 | 0.761 |
| (110) | 7 | 0.417 | 1.250 | 0.952 |

## 4. The finding — the magnitude test is **generic**

It is tempting to stop at "fcc (100) at leading order gives exactly 1.00 against a measured 0.96".
That is the move `qou-rav3` exists to forbid. That guard measured that inverting `B/A = ε·k/2` for
`k` reaches **73.7 %** of the plausible window `[2,12]`, so landing near any lattice coordination is
*"a property of WHICH ε and WHICH empirical target were chosen"* — and it pre-commits successors to
derive-then-check.

My ratio is genuinely **`k`-independent** (`surfaceToVolume_ratio`), so the guard does not apply
verbatim. The disciplined move is to apply its *method* to my own quantity rather than assume I
escape. Free choices here: the facet (`k' ∈ {7,8,9}`) and the shell treatment (leading vs exact).

    combinations tried            : 6  (3 facets x 2 shell treatments)
    reachable a_S/a_V             : 0.571 .. 1.250
    plausible window              : 0.5 .. 1.5
    fraction of window reachable  : 67.9 %
    measured (full SEMF basis)    : 0.961      textbook 1.130

**67.9 % of the window is reachable.** That is the same failure mode `qou-rav3` found, at 73.7 %.
So: the measured ratio lying inside the range is a **consistency check, not a prediction**, and the
apparent fcc-(100) match is an artifact of choosing a facet and a shell treatment. **The magnitude
does not constrain the geometry.**

**What survives is the shape**, and it survives cleanly: the `A^{−1/3}` form, the SEMF sign, the
approach from below, and the `A → ∞` recovery of saturation are all exact and choice-free.

## 5. Verdict and scope

- **Scope-(a) positive, on the shape only.** A bounded-degree bond count with its boundary deficit
  produces the SEMF volume-minus-surface shape exactly, with the right sign, refining
  `bounded_degree_saturates` rather than contradicting it. This is the first execution of an avenue
  proposed on 2026-05-02 and again on 2026-09-04.
- **Explicitly NOT a magnitude result.** Measured generic at 67.9 %; do not quote the fcc-(100)
  coincidence as support for close packing.
- **Does not explain `b₃ > 0`.** `UniformBondSimpleGraphExclusion.b3Uniform_nonpos` closes that for
  uniform-bond simple graphs, scope-(b), and this object is inside that conjunction.
- **Does not close Avenue 2.** Avenue 2 wants the edge set from the braid geometry; this assumes a
  packing. What it does is convert Avenue 2 from "would a surface term appear?" (yes, exactly, and
  here is its form) into the sharper remaining question: **what fixes `1 − k'/k`?**

## 6. Options for the author (default first; recommendation is judgement)

- **Default — nothing changes.** The shape result and the genericity negative are both on the
  record; Avenue 2 stays open with its question sharpened. Cost 0.
- **Attack `1 − k'/k` from the braid side.** The fractional degree loss is now the single number
  that would turn this from shape into prediction, and it is `k`-free — so it is immune to the
  `qou-rav3` inversion trap by construction. What would settle it: a derived statement about how
  many inter-nucleon interfaces a *boundary* nucleon's braid word carries relative to an interior
  one. Cost: a formalize-first tranche. Risk: the braid word is a 1-D chain with no notion of
  boundary, so the answer may be that the question is not posable without the coordination graph
  Avenue 2 asks for — a negative worth having.
- **Do not** pursue the facet match. It is measured generic.

**Recommendation (judgement):** the second. It is the only remaining free number in the surface
term, it is `k`-independent, and a negative on it would close Avenue 2 rather than leave it open.

## 7. Verification

- `lean`-direct exit 0 on `CoordinationSurfaceDeficit.lean`; 6 declarations axiom-clean; 0 `sorry`;
  the imported `CoordinationSaturation.olean` built lean-direct from `main`.
- Probe 12/12. One check in the first version was **wrong and is corrected in place**: adjacent band
  medians cannot test the turnover, because the `[63,100]` median sits at the plateau *above* the
  `[41,62]` median, which its light end drags down. The test now compares the heavy bands to the
  peak band. The defect was in the probe, not in the data.
- `scripts/precision-gates.sh --changed` — result recorded in the PR body.
- Repo CI is `workflow_dispatch`-only; this agent verification is the gate.
