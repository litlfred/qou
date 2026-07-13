# A=4 binding-K stage 1/1.5 VOIDED — GP presentation identity measured, canonical convention certified end-to-end

**Date:** 2026-07-13 (same-day correction) · **Branch:**
`claude/he4-binding-k-convention-correction-2026-07-13` · **Probe:**
[`he4_binding_k_presentation_correction_probe.py`](../../computations/deltalambda/he4_binding_k_presentation_correction_probe.py)
(+witness, `allPassed: true`) · **Scope:** (a) correction + certification; no fit;
nothing wired.

## What is retracted

The two A=4 probes merged earlier today (#3770, #3775) are **void**:

| claim | status |
|---|---|
| stage 1: "best plain inter-nucleon K at rel Δ = 14.7%" | ⛔ void (wrong presentation) |
| stage 1.5: "averaged 3-bond captures 96.2%; the residual 3.8% is the measured woven color-tube structure" | ⛔ void (wrong presentation; wrong constituent product; wrong seam placement) |

Both probes evaluated the Rust Geck–Pfeiffer Laurent characters **at q₀**. The
GP kernel's Laurent variable is **√q**: its generator eigenvalues are
(v², −v⁻²), i.e. the paper presentation (q, −q⁻¹) with q = v². Evaluating at
q₀ therefore computed the paper trace at **q₀²**. The probes' words were only
mildly writhe-imbalanced, so the wrong-point values looked plausibly close to
the target — the 3.8% was a presentation artifact, not structure. Both probe
files now carry ⛔ VOID banners; their witnesses stand as records of the void
runs (`voided_claims` in the new witness lists them).

## How it was caught

Validating the pipeline end-to-end: a 512-branch expansion of the canonical
⁴He recipe gave 1.05 vs the certified combiner 0.0554 (19×), and the plain
sign-of-c word gave 137.7 (2487×) — the writhe-+47 canonical word is maximally
sensitive to the evaluation point. An H₂ probe then measured the GP generator
eigenvalues directly: χ(σ) = q², χ(σ⁻¹) = q⁻² per shape.

## The certified convention (measured, all in the new witness)

1. **Presentation.** GP(√q) ≡ seminormal(q): exact 50-digit match
   (rel 8e-51) on the plain Borromean word at H₃; GP(q) is off 2.6%.
2. **Operator dictionary** for the production word triples `(c, d, g)` from
   `atom_braid_word_3A` (paper presentation, σ⁻¹ = σ − h, h = q − q⁻¹):

   | triple | operator | GP encoding |
   |---|---|---|
   | `(1, 0, g)` | σ | `(1, g+1)` |
   | `(1, −h, g)` | σ⁻¹ | `(−1, g+1)` |
   | `(1, −h/2, g)` | (σ+σ⁻¹)/2 | `(0, g+1)` = σ+σ⁻¹ **unnormalized** — ÷2 per crossing |
   | `(1, −h(½−δ/4), g)` | (½+δ/4)σ + (½−δ/4)σ⁻¹ | two weighted branches; δ = `_avg_color_delta()` |

3. **Pin.** The certified chi-cache/combiner chain is **canonical-muon-pinned**
   (`q-pinning-50-digit.witness.json`, 1.10997859555733471989976…), resolved
   through the anchor-adaptive `q_parameter` (`q0_anchor_manifest.json`
   `ideal_muon`). **Trap measured:** an ad-hoc process (not in the manifest)
   silently resolves the *proton* pin — this shifts a reproduction by ~8.8e-8
   and the color-weight δ by enough to leave a 5.9e-11 floor. The correction
   probe sets `QOU_Q0_ANCHOR=ideal` before imports. (The stage-1/1.5 hardcoded
   muon string agreed with the canonical value to ~1e-17 — the pin was *not*
   their error.)
4. **End-to-end certification** (GP with the dictionary at v = √q_muon vs the
   certified combiner traces): proton 2.9e-49, neutron 2.9e-49, deuteron
   1.1e-20, ⁴He 1.1e-20 (D/⁴He floor = the χ-cache 50-dps serialization).

## The real answer to the A=4 "binding K" question

No fingerprint search is needed — the canonical ⁴He binding structure is
**explicit in the builder** (`mass_at_3A_proper.atom_braid_word_3A(2,2)`):

```
T_⁴He = p(0) · σ₂ · p(3) · cw₅ · n(6) · σ₈⁻¹ · n(9)
```

- four **canonical 11-crossing operator-valued nucleon blocks** (each contains
  σ⁻¹ and averaged crossings — NOT the plain Borromean [σ₁σ₂⁻¹]³ that
  stage 1/1.5 used as constituent product);
- exactly **one inter-nucleon crossing per adjacent seam**, at generators
  **{2, 5, 8}** (0-based; stage 1/1.5 searched {3, 6, 9});
- **pair-typed seam operators**: p-p → plain σ; p-n → color-weighted average
  σ − h(½−δ/4); n-n → σ⁻¹.

Stage 1's "one crossing per interface emerges" was a mis-evaluated
rediscovery of this explicit structure. What remains genuinely open and
non-tautological for A=4 is **stage 2**: the per-block PSD filter +
operator-selection LP with duals (the A≤3 procedure's second stage), which
needs per-block H₁₂ matrices.

## Honesty note

The stage-1/1.5 numbers were merged this morning and voided this evening by
the same session's own end-to-end validation — the anti-fit discipline's
"validate against the certified target before interpreting residuals" applied
to my own work. The presentation identity, the operator dictionary, the
anchor-adaptive pin trap, and the seam structure are all now measured and
recorded, so the next A=4 attempt (stage 2) starts from a certified pipeline.
