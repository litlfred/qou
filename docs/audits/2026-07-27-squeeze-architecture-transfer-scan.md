# Squeeze-architecture transfer scan: Whitehead 4G and s5-so3 W_λ

**Date**: 2026-07-27 · **Beans**: qou-f6rs, qou-4cfh (milestone qou-pz3d) · **Status**: both fronts assessed; one blocked-on-source, one structurally out of scope.

Following the two in-repo volume-conjecture discharges (4₁ #4323, Borromean
#4381), this scan asks where else the elementary positive-sum squeeze
architecture (Riemann sums of `log(2 sin)` against the Clausen primitive +
saddle + two-envelope squeeze) applies.

> **RESOLVED (2026-08-02, PR #4400).** The owner uploaded the sources
> (`library/arxiv-math-0611181v2/0611181v2.pdf` = van der Veen; `library/1172-3/1172-3.pdf` = Habiro,
> Kōkyūroku 1172) and the third instance is now machine-proved sorry-free
> for the **2-belt chain `W_{a,2,1,0}`** (same volume 4G):
> `tendsto_log_whiteheadKashaev_vol` in
> `QOU/Knot/WhiteheadChainVolume.lean` (bricks W1–W5, milestone qou-k49o).
> Route refinement over the §1 expectation below: at odd `N = 2M+1` the
> `b ≥ 2` chain modulus is EXACTLY the phase-free positive sum
> `N^b (Σ_k S_{M,k})^{c+d}` (vdV Lemma 1) — a 1D squeeze, simpler than the
> Borromean. The `b = 1` Whitehead link proper carries outer Fresnel
> phases (vdV Lemma 4, Gaussian/erfc) and stays open in-repo — see
> `docs/audits/2026-08-02-whitehead-chain-positive-sum-route.md`.

## 1. Whitehead link (Vol = 4G) — FEASIBLE-CONDITIONAL, blocked on source access

**Verdict: the third instance is very likely one session of work with the
existing bricks, but it is blocked on a corpus-verified single-sum formula.**

- The corpus deliberately builds `⟨W⟩_N` from the validated `U_q(sl₂)`
  R-matrix engine (`whitehead_colored_jones.py`,
  `whitehead_weightblock_engine.py` — anti-guessing: "NO Whitehead
  colored-Jones closed form is transcribed from memory"). The R-matrix/
  weight-block representation is complex-valued blockwise — it does not
  expose the positivity the squeeze needs.
- The single-sum sources — Habiro [Hab00] (RIMS Kōkyūroku 1172) and
  van der Veen arXiv:math/0611181 (whose Whitehead-chain formula IS a
  positive sum at the Kashaev point; that positivity is the engine of his
  proof) — are **not in `library/`** and arXiv is firewalled in-sandbox
  (checked 2026-07-27: no `0611181` PDF among the 145 uploads).
- By analogy with the Borromean case (GL2011 App. A single sum → exact sign
  analysis → `kashaevProd`-powers over sin-squares → B-bricks), the expected
  shape for the Whitehead link is survivors of the form
  `kashaevProd(N,l)^2 / (window)` with saddle at the `π/2`-adjacent angle
  giving `4G = 4·Cl₂(π/2)`; the Clausen/Catalan value infrastructure is
  already in place. **This expectation is not a transcription** — no formula
  is asserted here.

**Unblock path**: owner uploads `math/0611181` (or Kōkyūroku 1172) →
transcribe + anchor-verify the Whitehead single sum (the
`habiro_borromean_colored_jones.py` 4-anchor pattern; the R-matrix engine is
the in-corpus independent cross-check, a *stronger* validation than the
Borromean had) → run the sign analysis → B-brick program. Coordinated with
PR #4382 (their `[Kas95]` state-sum route, `library/arxiv-q-alg-9504020v1/9504020v1.pdf`, may
independently expose the positive structure).

## 2. s5-so3 `W_λ` (colored Σ(2,3,5) WRT / q-Bessel) — squeeze DOES NOT APPLY (type mismatch, two counts)

**Verdict: negative — structurally, not for lack of effort.** Per the
s5-so3 ledger (`docs/coordination/s5-so3-keystone.md` §sharpened-open-object):

1. **Wrong question type.** The open `W_λ` object is the **value at the real
   interior point** `1/q₀ ≈ 0.901` of a convergent Habiro-ring q-series (the
   `q ↦ q⁻¹` bar-involution pullback of the WRT series), NOT a root-of-unity
   `N → ∞` growth rate. The squeeze architecture computes asymptotic growth
   rates of divergent-at-the-root sums; there is no `N` to send to infinity
   in the `W_λ` evaluation.
2. **No positivity anyway.** Even on the WRT root-of-unity side, the
   Σ(2,3,5) radial limits are Lawrence–Zagier **false theta** series with
   alternating periodic-character coefficients — the sign structure the
   squeeze cannot absorb (same reason 5₂/8₁₁ are out of reach).

**What DOES transfer to this front**: the `ClausenValueBounds` /
`CatalanValueBounds` certified-partial-sum-plus-tail skeleton is exactly the
right tool for machine-certifying values of convergent q-series at
`1/q₀` — e.g. the operational `Ψ(1/q₀) = 2.32958…` and, once the colored
λ-family series is pinned (the actual open item), each `W_λ` value. The
ledger's warning stands: `Ψ` alone is one number vs a λ-family (type
mismatch, the numerology trap) — certifying it now would be effort ahead of
the mathematics. Deferred until the family is pinned.

## Summary table

| Front | Squeeze applies? | Blocker | Reusable piece |
|---|---|---|---|
| Whitehead 4G | very likely (van der Veen positivity) | source PDF not in-sandbox | whole B-brick program + Catalan values |
| higher Whitehead chains | plausibly (2D deviation extension) | same source + new 2D bookkeeping | E/B-brick skeleton |
| 5₂, 8₁₁, generic knots | **no** | oscillatory sums (structural) | — |
| s5-so3 `W_λ` | **no** (type mismatch ×2) | — | certified value-bounds skeleton, once the colored series is pinned |
