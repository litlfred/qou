# A.3 jet-extension result — q-Plancherel scaffold (per-braid hybrid)

**Pair:** [`per_braid_tower_hybrid_jet.py`](../../computations/per_braid_tower_hybrid_jet.py)
+ witness [`2026-05-02-per-braid-hybrid-jet.witness.json`](2026-05-02-per-braid-hybrid-jet.witness.json).

The truncation audit
([`2026-05-02-truncation-audit.md`](2026-05-02-truncation-audit.md))
flagged that the per-braid hybrid was using the **level-0-only**
form of the mass tower and hypothesised that extending to jet
levels $n \geq 1$ would close the cal/$m_e$ spread from 0.65–1.06%
toward the calibration floor (~22 ppb).

## Method

A.3 scaffold: q-Plancherel-descent lift on the sub-braid traces.
At each jet level $n$:

- Per-pair traces scaled by $T_{\mathrm{pair}}^n = T_q(2)^n \approx 0.323^n$
- Descended trace scaled by $(z \cdot T_{3A})^n$ — atom-dependent,
  smaller for larger atoms
- $\Phi_q$ applied to the scaled traces; $z^2$ pair coupling preserved

This is **not** the true jet-prolonged Hecke algebra computation
(which requires Kähler-differential propagation per
[`prop:jet-stratified-reduction`](../../content/quantum-observable-universe/braids-and-knots/jet-stratified-reduction.md))
— it is a multiplicative scaffold testing whether atom-dependent
multiplicative corrections close the spread.

## Result

| $N_{\mathrm{jet}}$ | mean cal/$m_e$ | spread % |
|------------------:|---------------:|---------:|
| 0 (with tail bound) | 0.977 | **1.06** |
| 1 | 0.987 | **1.04** |
| 2 | 0.987 | **1.00** |
| level-0-only (no tail, baseline) | 0.987 | **1.06** |

**The q-Plancherel scaffold shrinks the spread by only ~6%**
(1.06% → 1.00%). It does **not** approach the ~22 ppb
calibration floor.

## Interpretation

Three possibilities:

1. **The scaffold is too crude.** True jet prolongation produces
   genuinely new $\mathrm{tr}_M$ values at level $n$ via the
   Kähler-differential action on $H_n(q)$, not multiplicative
   scaling. The atom-dependence of the correction may be
   stronger than what $T_q(2 \to A)$ captures.
2. **The spread is not from jet truncation.** Under any
   multiplicative lift (universal or atom-dependent), the
   spread is bounded by the variation of the lift factor across
   atoms. For q-Plancherel, $T_q(2)$ is constant across all
   atoms (per-pair sub-braid is always 2 strands); only the
   descended (3A-strand) lift varies, and the descended is
   exponentially small for $A \geq 4$. Hence the per-pair
   contribution dominates and is uniform in $A$.
3. **The truncation audit's hypothesis was wrong** — i.e., the
   1.06% spread is from a different source (e.g., the level-0
   q-Hecke descended vs q=1 MN tower mismatch, or the
   $H_3$-at-$H_{3A}$ weight approximation noted in P2.2a).

## Mean shift, not spread reduction

The dominant effect of jet levels is the **mean shift** from
0.977 (with tail bound only) to 0.987 (with $N_{\mathrm{jet}} =
1$). This pulls cal/$m_e$ closer to 1.0, which is the
calibration constraint $E_0 \cdot \mathrm{cal} = m_e$. Mean
shift is **absorbed by the $E_0$ calibration** ($H^2$ input)
and does not change the per-atom spread.

## Recommendation

Don't pursue the q-Plancherel scaffold further. The spread reduction
is too small to justify deeper development. Two productive next
steps:

1. **Investigate the spread source directly.** Plot cal/$m_e$ vs
   $A$, vs $|N - Z|$, vs (Z mod something), to identify the
   structural variable that drives the 1% spread. If it's
   monotone in $A$, the truncation is structural; if it's tied
   to (Z, N) parity or shell structure, the residual is an
   atom-physics effect.
2. **Check the H_3-at-H_{3A} weight approximation (P2.2a).**
   The weights $w_\lambda$ used for the q-Hecke descended at
   level 0 are computed at $H_3$ and applied at $H_{3A}$.
   Switching to proper $H_{3A}$ weights via
   `schur_weyl_symbolic.markov_trace_schur_weyl_eval` may close
   more of the spread than any jet-level extension.

## Status

A.3 scaffold landed; **negative-but-informative result**. The
truncation audit's prediction (jet levels close the spread to
~22 ppb) is not borne out by the q-Plancherel scaffold. The
real closer is likely the H_3-at-H_{3A} weight fix (already
queued as P2.2a) or a structural correction at level 0, not
jet prolongation.
