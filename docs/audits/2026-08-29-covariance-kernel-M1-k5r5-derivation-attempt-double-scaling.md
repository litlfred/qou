# Covariance-kernel epic (`qou-x631`) — M₁>0 gap `qou-k5r5`: the derivation attempt bottoms out in the BDJ/DIK soft-edge double-scaling RH analysis

**Date:** 2026-08-29 · **Branch:** `claude/m1-k5r5-bulk-sine-kernel-rate-2026-08-29` · **Tier:**
derivation attempt with primary-source reading; honest terminus · **Discipline:** no fake closure —
this **corrects** an earlier over-simplification of my own and identifies the exact analysis the rate
needs, which is research-grade RH and is **not** performed here. **Epic:** `qou-h315`/`qou-x631`;
gap `qou-k5r5`.

## What the attempt found (and a self-correction)

I set out to derive the bulk variance rate via the Toeplitz + Fisher–Hartwig route. Reading
Deift–Its–Krasovsky (`deift-its-krasovsky2012`) at the source changes the picture on two points:

1. **It is double-scaling, not a fixed Fisher–Hartwig singularity (self-correction).** The FH
   asymptotic `D_n(f) ~ (smooth)·n^{Σ_j(α_j²−β_j²)}` (DIK p29, p36; Ehrhardt) is for singularities at
   **fixed** points of the circle. The Plancherel spectral edge is a **moving soft edge** at
   `±2√θ` with Airy (`θ^{1/6}`) scaling — DIK's **double-scaling** regime (§11, "Double-scaling
   limits"), governed by **Painlevé II** (Airy), not a fixed FH exponent. My prior audit's "arc ⇒
   Fisher–Hartwig ⇒ algebraic remainder" was too glib; the correct mechanism is the soft-edge
   double-scaling limit.

2. **DIK §11 is *literally* the Plancherel problem.** DIK p53 treats the Poissonized Plancherel
   determinant (Gessel's `φ_n`) and states its recovery requires "analyz[ing] the double-scaling limit
   for the determinant as `λ, n → ∞`", citing **Baik–Deift–Johansson (BDJ)** as the main result. So
   the descent process's Toeplitz determinant *is* the object DIK's double-scaling section analyzes,
   and the tool is the BDJ / Painlevé-II Riemann–Hilbert analysis.

## An edge-vs-bulk decomposition test — honest negative

I hypothesized that the `θ^{−1}` remainder is *edge-dominated* (the Airy transition), with the deep
bulk converging faster. A crude annulus decomposition of `V_A(θ)/θ²` (edge annulus
`|x| ∈ [2√θ − 3θ^{1/6}, 2√θ + 3θ^{1/6}]`, θ = 2000…32000, exact mpmath) **does not confirm this**:

- the total remainder is clean, `θ·(V_A/θ² − 8/π²) ≈ −0.067` (stable, `θ^{−1}`, small ≲2% oscillation —
  consistent with `qou-tvok`);
- the edge annulus contributes a **large, slowly-decreasing** share of `V_A/θ²` (`≈ 0.53 → 0.36`
  across the range, `~ θ^{−0.14}`) — but the deep-bulk share moves oppositely, so the two regions
  **compensate**, and the split does **not** isolate which region carries the `θ^{−1}` remainder.

So I do **not** assert edge-dominance. What *is* solid is that the mechanism is a **soft-edge
double-scaling limit** (Airy, Painlevé II — DIK §11), not a fixed Fisher–Hartwig singularity; whether
the remainder is edge- or bulk-led is not resolved by a crude annulus split (a clean decomposition
would itself need the per-region limit constants, which have no closed form here). The `qou-tvok`
"Airy-edge signature" is suggestive of an edge contribution but is not, on its own, a proof of
dominance. Recorded as an honest negative so a later attempt does not assume the reframing.

## Honest terminus of the derivation attempt

The rate derivation reduces to the **BDJ / DIK §11 double-scaling Riemann–Hilbert analysis** of the
Plancherel Toeplitz determinant (Painlevé II / Airy), differentiated twice in the linear-statistic
parameter to extract the variance and its `θ^{−1}` remainder with an explicit constant. **This is a
research-grade RH computation.** I will **not** fabricate it: producing a plausible-looking but
unverified RH derivation would be exactly the laundering the discipline forbids ("fake progress is
worse than no progress"). The honest output of attempting the derivation is therefore:

- the route is now **precisely identified and fully sourced** (Gessel `φ_n` → BDJ/DIK §11 double-
  scaling → Painlevé II / Airy → differentiate for the variance rate),
- the mechanism is **corrected** (soft-edge double-scaling / Painlevé II, not a fixed Fisher–Hartwig
  singularity),
- the `θ^{−1}` exponent is **measured** and consistent (`qou-tvok`),
- and the rigorous exponent-plus-constant is the **BDJ/DIK double-scaling analysis**, which remains
  genuinely **open** and is not attempted here.

## What would actually close it

Either (a) the BDJ/DIK double-scaling RH computation carried out for the descent-process linear
statistics `Σ|c|, Σc², ΣD²` (research), or (b) a citation that states the second-order (variance-rate)
BDJ asymptotic in a directly usable form. The BDJ paper itself (Baik, Deift, Johansson, *J. Amer.
Math. Soc.* 12 (1999) 1119–1178) is **not yet in corpus**; DIK §11 references but does not restate its
variance-level second-order term.

## Status of `qou-k5r5`

Gap **OPEN**. The two `DescentDPPMarginConvergence.*_tendsto` Lean fields are the open input; their
rate is a double-scaling (Airy) RH analysis, now precisely sourced. The leading margin is **proved**,
the tail and de-Poissonization **cited**, and the remaining step is correctly re-identified as a
soft-edge double-scaling (Airy / Painlevé II) analysis — a research computation, not a missing
citation and not faked.

## Sources

- `deift-its-krasovsky2012` = `library/arxiv-1207.4990v3` (FH p29/36; double-scaling §11 p49–53;
  Plancherel/Gessel/BDJ p53).
- Airy edge: `library/arxiv-hep-th-9211141v1` (Tracy–Widom Airy kernel).
- `qou-tvok` (`θ^{−1}` measured, Airy-edge signature); `tail_bulk_split.py` (tail proved);
  `bulk_kernel_rate_probe.py` (pointwise oscillatory → integrated route).

## Cross-references

- Corrected predecessor: [`2026-08-29-covariance-kernel-M1-k5r5-bulk-rate-toolkit-complete.md`](2026-08-29-covariance-kernel-M1-k5r5-bulk-rate-toolkit-complete.md)
- Cited-inputs Lean class: `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/M1DescentDPPConvergence.lean`
- Epic `qou-h315`/`qou-x631`; gap `qou-k5r5`.
