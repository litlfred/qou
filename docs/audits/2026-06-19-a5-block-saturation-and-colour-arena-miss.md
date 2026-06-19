# ⁵He Wedderburn-block saturation + the finite-colour-arena miss grows with A (2026-06-19)

**Branch:** `claude/aoperator-a5-followups-2026-06-19` (PR #2492)
**Picks up:** the merged #2459 A=5 combiner cross-check. Extracts the *structural*
content the scalar transfer discards — which Wedderburn blocks ⁵He saturates — and
connects it to the s5-so3 keystone's "no finite colour arena" finding (#2406).
**Discipline:** corpus-grep first; descriptive audit of the production tr_M; no
value change, no fit.

## Probe

[`computations/probes/aoperator_a5_block_profile.py`](../../computations/probes/aoperator_a5_block_profile.py)
(+ witness). Ranks the H₁₅ irreducible blocks λ⊢15 by signed share of
`tr_M(⁵He) = Σ_λ y_λ χ^λ`, using the **exact** 50-dps transfer characters
(`reduced_block_kernel.chi_all_lambda_reduced_block`) — the object #2459 showed the
operator combiner reproduces to machine precision — weighted by the canonical
Wenzl/Jones–Markov `y_λ`. Fast (transfer only; no ρ_ξ build).

## Finding 1 — ⁵He saturates the two-row blocks

`tr_M(⁵He) = 0.0148348268146` (matches #2459); signed/L1 = 0.897 (coherent — not a
near-cancellation). The top blocks:

| rank | λ⊢15 | d_λ | share of tr_M |
|---|---|---:|---:|
| 1 | (11,4) | 910 | 20.8% |
| 2 | (12,3) | 350 | 16.8% |
| 3 | (10,5) | 1638 | 16.3% |
| 4 | (9,6) | 2002 | 15.5% |
| 5 | (13,2) | 90 | 6.6% |
| 6 | (14,1) | 14 | 4.2% |
| 8 | (11,3,1) | 2835 | 2.5% (first ≥3-row) |

- The **top 6 are all two-row** `λ=(15−k,k)` — ~80% of tr_M. **10/176 blocks → 90%**, **27/176 → 99%**.
- Saturation concentrates on the **near-symmetric (low-row-count)** representations, even though χ^λ is largest for high-dimensional middle blocks (e.g. (9,3,3) has χ=162 but y=2.1e-6, so 2.3%): the `y_λ` weight decays fast off the two-row edge.

## Finding 2 — the finite-colour-arena miss GROWS with A (the load-bearing result)

A finite colour-SU(N) arena realizes only partitions with **≤ N rows**. Aggregating
tr_M by row-count of λ:

| shell | ⁵He share of tr_M | arena |
|---|---:|---|
| ≤2-row | **84.22%** | SU(2)/Temperley–Lieb shadow |
| ≤3-row | **94.00%** | colour ℂ³ (SU_q(3)) |
| ≥4-row | **6.00%** | beyond any colour-ℂ³ arena |

Compared to the established ⁴He datum (#2406, `2026-06-16-keystone-arena-is-full-hecke-not-su3.md`):

| | colour-ℂ³ (≤3-row) **miss** |
|---|---:|
| ⁴He (A=4) | **3.4%** (#2406) |
| ⁵He (A=5) | **6.0%** (this audit) |

**The miss roughly doubles A=4→A=5.** This is direct quantitative support for #2406's
conclusion that **no finite colour-SU(N) arena** hosts the production trace: the
required row-count (hence N) grows with the nucleon number, so no fixed N suffices.
The production trace is the **full-Hecke principal specialization** `s_λ(1,q,q²,…)`,
intrinsically `p(3A)`-dimensional (s5-so3-keystone.md "Corrected open object").

## Corpus reconciliation — "are these the right terms?" is already answered

A first read suggested a *two-row (SU_q(2)/TL/Jones) vs all-λ (full Hecke)* tension —
`prop:knot-eigenbasis-complete` states the SU_q(2) physical eigenbasis is **two-row
only** (rank SU(2)=1), yet tr_M sums **all** λ⊢n. **Corpus-grep resolves it:** those
are *different objects*. The two-row eigenbasis is a SU_q(2) **lower bound** (#2406:
"strand fibre ≥ colour ℂ³"); the production **mass** trace is the full-Hecke
principal specialization (all λ⊢n), per #2406 + the s5-so3 keystone ledger, and
`W_λ = d_q(λ)²/[n]_q!` (regular-rep / q-Plancherel) is **not** the production weight
(matches #2481's `full`≠`std`, `std`=Jones–Markov=tr_M). So tr_M is complete over
all λ⊢n by Wedderburn semisimplicity (Jimbo: `H_n(q)≅ℂ[S_n]` at q₀ not a root of
unity; corpus `prop:knot-eigenbasis-complete`, Lean `QOU.Braiding.knot_eigenbasis_complete`);
the ≥3-row content is genuine, not an artifact. Finding 2 quantifies *how much*
genuine ≥colour content there is, and that it grows with A.

## How the compute was improved (and the remaining wall)

- **Combiner (#2459 → here):** the naive A=5 combiner rebuilt the mpmath
  `interface_blocks` per λ⊢15 and ran > 2.75 h. An **exact regrouping**
  (`combiner_chi_fast`: precompute the a-independent `G[w]` from the tiny `nW×nW`
  alignment, run the `d_ξ` loop in float64 with `bridge(δ)` cached) cut it to **11 s**
  (~900×), A never materialised. Validated against both `chi_young` (1.4e-14) and the
  original mpmath combiner (1.8e-15).
- **The profile is transfer-based** — exact 50-dps characters, seconds, no ρ_ξ build.
  Optimal already.
- **Remaining wall (A≥6):** the ρ_ξ **diagonal** cost is `Σ_ξ d_ξ²·|W| = n!·|W|`,
  untouched by the regrouping (it removes the *combiner* cost, not the diagonal one).
  A=6 is 10.7 d float64 / 150 d Rust — out of reach for any rep-based backend; the
  only escapes are a rep-free weighted-trace method (none known; the `v_a`-weighted
  diagonal breaks the class-function structure so Murnaghan–Nakayama does not apply)
  or the fine-Bratteli transfer itself (production, hence not an *independent* check).

## Anything needed to prove (formalize-first targets this surfaces)

1. **Combiner branching completeness (tractable).** The cross-check empirically shows
   the peel recursion reconstructs *every* λ⊢15 (combiner == transfer, all 176, to
   1e-12). The matching theorem — the Littlewood–Richardson branching
   `H_{n−3}×H_3 ↑ H_n` enumerated by `interface_blocks` is complete (Frobenius
   reciprocity; `Σ_{(ξ,ν)} c^λ_{ξν}` exhausts each λ) — is provable and would
   formalize "we get all terms" for the *operator* route, complementing the existing
   semisimplicity proof `knot_eigenbasis_complete` (which covers the *scalar*
   `tr_M = Σ_λ y_λ χ^λ` completeness).
2. **"Miss grows with A ⇒ no finite colour arena" (high-value).** Findings 2 gives
   two data points (3.4%→6.0%). The formalize-first upgrade: a structural lower bound
   showing the ≥(N+1)-row share of `tr_M(ᴬX)` is bounded below by a function
   increasing in A, for every fixed N — turning #2406's empirical "no finite arena"
   into a theorem. This is the formalize-first complement to the keystone.
3. **The keystone proper (open, owner-gated).** Does the full-Hecke
   principal-specialization trace admit *any* geometric realization whose index
   reproduces the canonical Markov weights? Finite-dim Sasakian ruled out
   (s5-so3-keystone.md). Finding 2 is structural input (the block support the
   realization must reproduce), not a closure.

## Cross-links
- [`aoperator_a5_block_profile.py`](../../computations/probes/aoperator_a5_block_profile.py) + witness — this probe.
- [`2026-06-17-aoperator-a6-cost-wall-contraction-only.md`](2026-06-17-aoperator-a6-cost-wall-contraction-only.md) — A=5 cross-check + cost wall (#2459).
- [`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — the keystone this feeds; #2406 (full-Hecke arena), #2481 (regular-rep vs Jones–Markov).
- `prop:knot-eigenbasis-complete` — semisimplicity/completeness (Lean `QOU.Braiding.knot_eigenbasis_complete`).
