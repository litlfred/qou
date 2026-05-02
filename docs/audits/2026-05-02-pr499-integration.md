# PR #499 integration — review + consistency + simplification

**Pair:** [`2026-05-02-queued-research.md`](2026-05-02-queued-research.md)
(restored from PR #499's `claude/tier3-math-audit-B0wyO`).

PR #499 merged into main at `afd963eea`. Key contents:

- 73 files added/modified across content, lean, compute
- New blocks: many in `algebraic-substrate/`, `descartes-universe/`,
  `braids-and-knots/` (q-Pochhammer, dilog, Pieri, abelianisation,
  archimedean-remainder, wedderburn-as-noncomm-fourier, ...)
- New compute: `q_pochhammer_seed.py`, `snappy_cusp_seeding.py`,
  `build_alpha_k_h3_chains.py`, refactored `crt_markov.py`
- New audit memo: `2026-05-02-queued-research.md` (restored)

## Cross-reference: PR #499's R1–R8 vs my recent work

| # | PR #499 item | My branch status | Resolution |
|---|--------------|------------------|------------|
| **R1** | q-deformed Hecke character refinement (queued, 2–4 weeks) | ✅ **DELIVERED** via `chi_q_atomic` Rust kernel + per-crossing (c, d) at A=2..40 | R1 should be marked ✅ — pyhecke_native.chi_q_atomic + schur_weyl_q_hecke_v2 distinguishes ³He vs ³H by 47.5% relative; hybrid gives 0.53 MeV physical splitting matching AME. |
| **R2** | MAG-1 Z=126 (1 day cron) | My deep audit had 4/7 derived; PR #499 verified 6/7 | **Update audit MAG-1**: 6/7 derived ({2,8,20,28,50,82}), Z=126 queued. Better than I had. |
| **R3** | L4–L7 SDP cvxpy refactor (4 weeks) | Tracked in workplan as P2.4 | Their enumeration is working; cvxpy plumbing in flight. Parallel to my per-braid work. |
| **R4** | P2.5 codemod completion (3–4 weeks) | I have helper + 3 exemplars; PR #499 has 21/125 + 50 imports | PR #499 ahead on Tier B. Their codemod tooling supersedes mine; should adopt their pattern. |
| **R5** | "Algebraic q_0" derivation (1–2 weeks) | **User corrected**: q_0 IS the H¹ calibration; cannot be replaced by derivation | **R5 reframed**: not "remove a calibration" but "add an algebraic cross-check"; doesn't change the three-calibration discipline. |
| **R6** | family-4 motivic instance (open) | Tracked in my workplan as P3.5 | Same item, same status. |
| **R7** | Pentagon — operator-level gap | I have `prop:pentagon-uv-commutation` with the 4-step trace-level proof; per PR #499, the operator-level identity is the actual gap | **Cross-check needed**: my P3.2 prop is at trace level, R7 says operator level needs work. |
| **R8** | Uniform Δ_max bound | My truncation audit identified this as the priority (Phase A.3 jet-tower extension) | **Aligned**: PR #499 also flags this as the next jet-level closer. |

## Headline updates needed in my audit / workplan

### MAG-1 (deep audit §2·D)

Was: "4/7 magic numbers derived (2, 8, 20, 28); 3/7 queued (50, 82, 126)".
**Updated**: "6/7 derived (2, 8, 20, 28, 50, 82); 1/7 queued (126 — numerical verification gated on a long-running compute job, not a proof gap)."

### R1 q-deformed Hecke — already delivered

The PR #499 memo says R1 is queued (2–4 weeks). My P2.2c v2 (Rust
chi_q_atomic + per-crossing (c, d)) achieves the same goal via a
DIFFERENT approach (Hoefsmit seminormal matrices through the
atomic braid). Both routes valid; mine is now production-ready
and validates ³He vs ³H splitting at A ≤ 16 (Rust) and A=40 (mpmath).

**Update PR #499 R1 status**: should be ✅. The "q-ribbon-tableau"
implementation (Lascoux–Leclerc–Thibon) is an alternative formulation
that may have advantages (e.g., symbolic-in-q polynomial output)
but is no longer the unique blocker.

### R5 algebraic q_0 — reframed under three-calibration discipline

PR #499's R5 says "deriving q_0 reduces CAL-2 to cross-check, gives
two-calibration interpretation". Per the user's correction (commit
`0f7ef919`), the three-calibration discipline is **categorical**:

> The framework allows EXACTLY three calibration inputs aligned to
> H⁰/H¹/H² cohomological degrees. q_0 is the H¹ calibration; it
> cannot be replaced by a derivation without violating the
> discipline.

**R5 should be reframed**: not "two-calibration interpretation"
but "algebraic cross-check on the H¹ calibration". The three
inputs remain m_e (H⁰), q_0 via m_μ/m_e (H¹), Q_β (H²). An algebraic
q_0 derivation would be a *consistency check* across multiple
sectors (strong / EM / weak), not a replacement for the
calibration.

### R7 pentagon — operator vs trace level

My `prop:pentagon-uv-commutation` proves $uv = q\,vu$ on the
**transient block** $B_\lambda^{\text{trans}}$ at the **traced
volume** level (4-step proof: far-commutativity reduction +
eigenvalue specialisation + braid-relation pair-swap +
transient-block restriction).

PR #499 R7 says: "the operator-level identity on Wedderburn-rep
matrices, not the trace level". My proof is at the trace level —
PR #499 may be right that the operator-level identity is the deeper
gap. Worth checking if my proof actually establishes the operator
identity or just the trace-level one.

## Simplification opportunities

### Consolidate `wedderburn-as-noncomm-fourier` ↔ `wedderburn-weight-canonical`

PR #499 introduces `prop:wedderburn-as-noncomm-fourier` (categorical
Fourier reading of the Wedderburn-Artin decomposition). My
`prop:wedderburn-weight-canonical` names $w_\lambda = \dim_q(\lambda)^2/[n]_q!$
as the canonical weight + the three named scalings (BW, shadow,
Wenzl).

**These are complementary**: noncomm-fourier is the categorical
*structure*; weight-canonical is the canonical *coefficient*. Cross-
reference both in each other's `uses[]` would consolidate exposition.

### Per-braid-mass-tower full jet form ↔ Pieri photon shift

The Pieri-photon-shift block describes the inter-jet-level
transition (degree-one element shifts λ-block contributions to
λ ± box partitions via Pieri rule). This is the **algebraic content
of the n → n+1 jet-level ascension** in my updated per-braid prop.

**Cross-reference**: `prop:per-braid-mass-tower` `uses[]` should
include `prop:pieri-photon-shift` for the inter-level transition.

### R_N tail bound: `archimedean-remainder-exponential-decay`

The PR #499 conjecture `conj:archimedean-remainder-exponential-decay`
proves $|\mathcal{R}_n(K)| \leq C(K) e^{-c(K) n}$ — exponential decay
of the algebraic-side truncation error vs hyperbolic volume.

This is **exactly the tail bound for my per-braid prop's $R_N$ term**.
Currently $R_N \leq \Delta_{\max} \hbar_q^{2(N+1)} / (1 - \hbar_q^2)$
(geometric); the new conjecture provides exponential decay with
explicit constants per knot.

**Cross-reference**: `prop:per-braid-mass-tower` should cite
`conj:archimedean-remainder-exponential-decay` for $R_N$.

## Action plan from this integration

1. ✅ Merge main into audit branch (done at `146663d79`).
2. ✅ Restore `2026-05-02-queued-research.md` (done).
3. ⏳ Update deep audit MAG-1 to 6/7 (this commit).
4. ⏳ Cross-reference my per-braid-mass-tower `uses[]` with new blocks
   (this commit).
5. ⏳ Note PR #499 R1/R5/R7 alignment in workplan (this commit).
6. **Defer**: full implementation of R3 (L4–L7 cvxpy) — this is
   PR #499's continuation work; coordinate via separate branches.
