# Phase A.3 audit: where does the mass tower truncate?

**Date:** 2026-05-03
**Branch:** `claude/phase-a3-mass-tower-audit`
**Goal:** identify the current jet-level truncation `N` in the
mass-tower pipeline per issue #522 phase A.3.

## Verdict: **truncation at jet level n = 0 only.**

The current implementation in `per_braid_tower_hybrid.py`
sums **only the n = 0 jet level** of the mass-tower formula. Levels
n = 1, 2, 3, … are entirely missing.

## The mass-tower formula

From [`pentagon-uv-commutation.md`](../../content/quantum-observable-universe/braids-and-knots/pentagon-uv-commutation.md)
lines 86–106:

$$
  \mathfrak{m}
  \;=\;
  |\mathrm{tr}_M(W)|
  \;+\;
  \sum_{n=0}^{N}\!\Bigl(
    \sum_{\xi \in \mathcal{S}^{(n)}_1}\!\Phi_q(|\mathrm{tr}_M(\xi)|)
    \;+\;
    z^{2}\!\!\!\sum_{(\xi,\xi') \in \mathcal{S}^{(n)}_2}\!\!\!\Phi_q(|\mathrm{tr}_M(\xi\xi')|)
  \Bigr)
  \;+\;
  R_N
$$

The outer sum is over jet levels `n = 0, 1, …, N`. At each level,
singletons `S_1^(n)` and pairs `S_2^(n)` contribute. The pentagon
identity (`pentagon-uv-commutation.md` line 56–60) certifies that
no triples appear at any level — every triple at level n absorbs
into a pair + singleton at level n plus a residual at level n+1.

## What the implementation actually computes

`folio-assistant/computations/per_braid_tower_hybrid.py:90–155`:

| Term in pipeline | Pentagon-formula label | Notes |
|---|---|---|
| `desc` (q-Hecke descended atom-braid trace) | `\|tr_M(W)\|` outer term | Level 0 base |
| `single` (per-nucleon Φ_q, q=1 MN) | `Σ_{ξ ∈ S_1^(0)} Φ_q(\|tr_M(ξ)\|)` | Level **n=0** singletons only |
| `cross` (per-pair Φ_q, q-Hecke) | `z² · Σ_{(ξ,ξ') ∈ S_2^(0)} Φ_q(\|tr_M(ξξ')\|)` | Level **n=0** pairs only |
| (none) | `n ≥ 1` levels | **NOT COMPUTED** |
| (none) | `R_N` tail | **NOT COMPUTED** |

There is no `for n in range(...)` over jet levels in the pipeline.
The code-comment labels "Level 1" and "Level 2" refer to **strand
arity** (singleton vs pair), not the jet-level index n.

## Where the truncation lives

`folio-assistant/computations/per_braid_tower_hybrid.py:101–141`.
Specifically:

- **lines 101–103** — `tr_p`, `tr_n`: per-nucleon traces (level n=0
  singletons).
- **lines 119–121** — `tr_pp`, `tr_nn`, `tr_pn`: per-pair traces
  (level n=0 pairs).
- **lines 125–141** — sums singletons + pairs into `single + cross`.
- **No further levels.**

The `mass_endomorphism.py` module mostly delegates to the canonical
pipeline (binding-energy / mass tower) via `markov_peel.tr_M_atomic`
and similar; it does not iterate jet levels either.

## Geometric tail bound (for reference)

`prop:jet-tower-convergence` says the level-(n+1) contribution is
suppressed by a factor in q. The exact suppression factor at q₀
(per `2026-05-02-nv-frob-filter-conjectures.md`'s related Σ_all
decay) is `0.2575^A` per A unit on Σ_all-style sums — but the mass
tower convergence rate is a separate object and has not yet been
numerically pinned down at q₀ in this audit.

The geometric series suggests the level-1 contribution is the next
biggest missing term; its size relative to the per-atom residual
(500–3200 ppm per `9b66f7571` audit) determines whether extending
the truncation closes the gap.

## What's needed to close A.3 (out of audit scope)

1. **Identify the level-n sub-braids** for each atom — what are the
   jet-prolonged sub-braids ξ at level n=1? The pentagon-uv
   document defines them via the level-shift operator τ̂_n but doesn't
   give the explicit braid words.
2. **Compute level-1 Φ_q contribution at the proton** (smallest case)
   — ~30 min compute once (1) is fixed.
3. **Compare to current proton residual** (~500 ppm = 0.47 MeV).
4. If level-1 contribution ≳ residual: **extend the truncation by 1**
   in `per_braid_tower_hybrid.py` (add a level-1 sum block) and
   re-run binding-canonical to see if proton residual drops.

Step 1 requires either
- explicit construction of the level-shift operator `τ̂_n` (mentioned
  in `pentagon-uv-commutation.md:117` as "deferred to the descent
  involution's quantization"), or
- a phenomenological proxy — e.g. derivative-prolongation of the
  level-0 sub-braids in some explicit jet bundle.

Both are research-grade sub-tasks; neither is currently implemented.

## Recommendation

**Phase A.3 is the largest unimplemented piece of issue #522's
mass-tower track.** The level-1 contribution is currently 100%
missing, not approximated.

The size of the level-1 contribution is **unknown** without first
computing it. An earlier draft of this memo cited a "geometric
tail bound ~0.066× of level-0" estimate by analogy with the
`Σ_all` decay rate from `2026-05-02-nv-frob-filter-conjectures.md`,
but that analogy is wrong (Σ_all decay is a different convergence
rate; applied naively at level-0 ~ proton mass it would predict a
~62 MeV correction, ~10⁵× the observed proton residual; Gemini PR
#531 review caught this inconsistency). The jet-tower geometric
tail bound from `prop:jet-tower-convergence` hasn't been
numerically pinned at q₀; whether the level-1 contribution is
comparable to the per-atom residual or much smaller is an open
empirical question — answerable only after `τ̂_n` is realised.

But step 1 is a real sub-project: defining what the level-1 sub-braids
ARE. Without `τ̂_n` realised in code, level-1 Φ_q can't be computed.

**Suggested next step (out of this audit):** open a separate issue
/ branch to construct the level-shift operator `τ̂_n` per
`pentagon-uv-commutation.md:117`, even just at proton scale. Once
that's in place, the level-1 sum addition is a 5-line patch.

## Files

- Witness: [`folio-assistant/computations/phase-a3-mass-tower-audit.witness.json`](../../folio-assistant/computations/phase-a3-mass-tower-audit.witness.json)
- This memo
- No code changes — audit-only.

## Status

**Audit-only finding.** Truncation = level n=0; everything beyond is
missing infrastructure (the level-shift operator τ̂_n is referenced
but not implemented). Next step is the τ̂_n construction, not a
truncation-bump patch.
