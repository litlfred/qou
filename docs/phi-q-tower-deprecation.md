# Φ_q Tower Code — DEPRECATED (2026-04-24)

*Status marker written after the pivot to the JSJ + hyperbolic-volume
framework described in [`path-to-1ppb.md`](./path-to-1ppb.md).*

## TL;DR

The Φ_q-tower binding pipeline (`binding_per_block_log.py`,
`canonical_plus_multibrane.py`, `unified_lift.py`, `kahler_lift.py`,
`binding_full_pipeline.py`, `binding_fast_pipeline.py`,
`binding_full_content_pair.py`) is **paused** in favor of the JSJ
canonical pipeline:

$$B(Z, N) = \sum_{P \in \mathrm{JSJ}(K_{Z,N})}
           \rho_F(P) \cdot \mathrm{Vol}_{\mathrm{hyp}}(P).$$

The Φ_q code is **not deleted** — it may return if the JSJ path hits
a wall, or if the pentagon-defect expansion (Phase 2 in the
handover) needs the per-block Wedderburn machinery.  Treat
everything in "Files affected" below as legacy / reference until
further notice.

## Why the pivot

The per-block log formula `B = Σ_λ w_λ m_e Σ_i ln|Φ_q(V̂_i^λ)|`
implemented in this branch reaches a **0.15% baseline floor** on
deuterium that neither jet-tower augmentation nor Kähler-lift
corrections can break — the level-0 model itself is the limit.
Commit `6d6d2c9` "Jet-tower + Kähler lift probes on per-block log
binding" documents the result in witness data:

| atom | B_phys (MeV) | B_AME (MeV) | \|Δm/m\|% |
|------|-------------:|------------:|-------:|
| D    |  5.09        | 2.22        | 0.15%  |
| T    | 10.83        | 8.48        | 0.08%  |
| ³He  |  9.71        | 7.72        | 0.07%  |
| ⁴He  | 15.46        | 28.30       | 0.34%  |

The JSJ pipeline delivers 0.09% on ¹⁶O and has a clear path to 1
ppb via Phases 1–5 of the handover.  The Φ_q-tower's 0.1–1%
class sits an order of magnitude above that.

## What's deprecated vs retained

### Code — **DEPRECATED, kept on disk**

These files carry banner comments warning against extension:

- `folio-assistant/computations/binding_per_block_log.py`
- `folio-assistant/computations/canonical_plus_multibrane.py`
- `folio-assistant/computations/unified_lift.py`
- `folio-assistant/computations/kahler_lift.py`
- `folio-assistant/computations/binding_full_pipeline.py`
- `folio-assistant/computations/binding_fast_pipeline.py`
- `folio-assistant/computations/binding_full_content_pair.py`

The `tower_mass_level(include_desc=...)` parameter introduced in
this PR remains the structurally correct behaviour for the Φ_q
tower — if the tower ever returns, the code is correct per
`prop:descended-level-zero`.

### Content — **RETAINED, relevance re-scoped**

The four new derivation propositions are orthogonal to the
engine choice; they prove statements about the categorical
action / Hecke-trace structure that hold regardless of whether
the mass engine uses Φ_q, JSJ volumes, or something else:

1. **[`prop:markov-pair-z2`](../content/quantum-observable-universe/braids-and-knots/markov-pair-z2.md)** —
   all-pairs Markov-trace identity $\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$.
   *General Hecke result.  No Φ_q dependence.*

2. **[`prop:pentagon-uv-commutation`](../content/quantum-observable-universe/braids-and-knots/pentagon-uv-commutation.md)** —
   quantum-torus relation $uv = q\,vu$ on the transient Wedderburn
   block.  *Directly supports Phase 2 of the handover* ("pentagon
   defect computation for adjacent crossings").  Framing involves
   the pentagon identity of Φ_q, but the underlying Hecke
   commutation result is engine-independent.

3. **[`prop:descended-level-zero`](../content/quantum-observable-universe/braids-and-knots/descended-level-zero.md)** —
   iterated descent idempotence ⇒ descended contribution lives at
   level 0 only.  *General categorical-action result.  No Φ_q
   dependence.*

4. **[`prop:delta-max-uniform-bound`](../content/quantum-observable-universe/braids-and-knots/delta-max-uniform-bound.md)** —
   explicit uniform bound $\Delta_{\max}$ for jet-tower
   convergence.  **Tightly coupled to the Φ_q tower** — DEPRECATED
   along with the tower.  Retained for reference in case the
   tower returns.

## Usage guidance for agents

- **Do not import `binding_per_block_log` or any `tower_mass_level`
  caller into new code.**  Use the JSJ pipeline
  (`jsj_verification.py`, `jsj_atom_volume.py`,
  `jsj_alpha_clustering.py`) per the handover docs.
- The derivation props (`markov-pair-z2`, `pentagon-uv-commutation`,
  `descended-level-zero`) are safe to `uses[]`-cite from new
  content blocks.
- `delta-max-uniform-bound` should only be cited from blocks that
  explicitly discuss the Φ_q tower.

## How to un-deprecate (if needed)

If the JSJ path hits an obstruction and the Φ_q tower must
return:

1. Delete the DEPRECATED banners from the seven code files listed
   above.
2. Un-tag `delta-max-uniform-bound.ts` (remove the `deprecated`
   tag).
3. Refresh this doc's status line from "DEPRECATED" back to
   "ACTIVE".

No code needs to be rewritten — everything still runs as of this
commit (sanity checks pass in `binding-per-block-log.witness.json`
and the jet/Kähler probes produce convergent results).
