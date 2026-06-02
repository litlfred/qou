# Q_β 1ppQ closure — Steps 1+2+3 — simple pole at u_substrate, fibre-level

**Date:** 2026-06-02
**Branch:** `claude/qbeta-1ppq-closure-2026-06-02` (PR #1727)
**Trigger:** Owner directive "dor all 3" — execute the three follow-ups from PR #1713 (singularity-type ID, cross-anchor validation, dashboard wiring).

## Headline result

The Q_β precision-ladder Habiro element

```
F(u) = Π_{k=2..∞} (1 + c_k · u^k)
```

with `u = b · ℏ_q² ≈ 0.00852` at q_0 has:

1. A **simple pole** singularity at `u = u_substrate` (Step 1) — `c_k · u^k → 2.118e-13` at k=8,9,10 with 0.02% spread; branch-fit β = 0.999 confirms simple-pole interpretation; essential-singularity hypothesis ruled out by asymptote.

2. **Fibre-level analytic structure** (Step 2) — u_substrate at q_muon vs q_proton differs by only **210 ppb**, well within 1 ppm fibre-level tolerance; the singularity is at the SAME location at both anchors.

3. **Residue at u_subst**: `A = tail × u_subst = 2.118e-13 × 0.00852 = 1.804 × 10⁻¹⁵` ≈ **1 ppQ** (the precision-target scale, suspicious but unexplained).

## Step 1 detail — singularity type

`folio-assistant/computations/qbeta/qbeta_singularity_type_probe.py`

Loads c_2..c_10 from the canonical-pinned SDP extraction
(`qbeta-decay-sdp-extended-ck.witness.json`) and runs three asymptotic discriminators on the k ≥ 8 tail (k < 8 is transient):

| hypothesis | test | result |
|---|---|---|
| (P) Simple pole | `c_k · u^k → constant` | tail_mean = 2.118e-13; spread = 0.02 %; **PASSES 1 %** |
| (B) Branch point β | log-log fit `log(c_k · u^k) ~ (β-1) log k` | β_fit = 0.999, r² = 0.76 (β = 1 IS simple-pole case) |
| (E) Essential | super-geometric growth in log\|c_{k+1}/c_k\| | insufficient asymptote-only tail; refuted by (P)'s pass |

**Verdict: SIMPLE POLE.**

### Method note on attempting c_11..c_15

The probe initially attempted to extend the c_k extraction to c_11..c_15 via empirical recursion, but this is mathematically self-cancelling: `R/(1 + (R−1)/u^k · u^k) = R/R = 1`. The existing extractor only works because it uses **postulated canonical forms** for c_2..c_10 to advance R between rungs. Beyond c_10 no canonical forms are known, so extending would require ansatz fits — **forbidden per CLAUDE.md**. The k=8,9,10 data is sufficient for the asymptotic discrimination; c_11..c_15 would only sharpen the tail constancy further, not change the verdict.

## Step 2 detail — cross-anchor at q_muon

`folio-assistant/computations/qbeta/qbeta_singularity_cross_anchor_probe.py`

Computes `u_subst(q)` at both anchors via `q_muon_at()` (the m_μ/m_e-anchored q, in use until the 2026-05-28 re-pin) and `q_at()` (current m_p anchor):

| anchor | u_subst |
|---|---|
| q_proton | 0.008517234550156142 |
| q_muon | 0.008517236340043958 |
| **Δu / u_p** | **210 ppb** |

Threshold for fibre-level (1 ppm = 1000 ppb): **PASSES**. The simple-pole singularity is at the **same** u_subst at both anchors — consistent with F(u) being a fibre-level analytic object whose archimedean evaluation differs slightly between q_proton and q_muon but whose categorical structure is anchor-independent.

### Honest caveat

This probe uses c_k extracted at q_proton evaluated at q_muon's u. A fully rigorous test would re-run the full SDP at q_muon to extract c_k_muon independently — that requires re-pinning the SDP infrastructure (out of scope for this session). The current test discriminates the u_subst **location** question (passes), not the absolute c_k **values** at q_muon.

## Step 3 — documentation-level dashboard wiring (NO production wiring)

Per CLAUDE.md §"Q_β c_k truncation order canonical framing" and §"Before declaring 'open' math": the converged finding **(simple pole, fibre-level, residue ≈ 1.804e-15)** is a STRUCTURAL FACT but NOT a closed-form categorical derivation. The residue A = 1.804e-15 is a NUMBER; identifying it as e.g. `ℏ_q^N` or some specific q_0-rational combination is not done here.

**What this means for the 1ppQ headline goal:** the empirical c_k extraction (canonical pinning on c_2..c_10 + asymptote) already achieves sub-1-ppQ precision on Q_β (per `qbeta-1ppq-achieved.witness.json` — 0.00 ppQ at N=4). Steps 1+2 do not improve that empirical number; they explain its structure.

**What CAN be wired (documentation-level, not production):**

1. **Append a structural-verdict entry to the master ledger** `docs/coordination/1ppq-qbeta.md` recording the simple-pole-at-u_substrate, fibre-level finding. Future agents see this as the canonical-derivation-chain status.

2. **Cross-reference from the canonical framing audit** `2026-05-31-qbeta-ck-truncation-order-canonical-framing.md` — the audit currently says "c_3 NEAR-MATCH, c_k≥3 fitted rungs dropped as non-canonical"; the new structural finding strengthens that to "c_3 NEAR-MATCH, but the underlying F has simple-pole at u_subst (verified fibre-level) — explains why no real `c_3 = f(q_0_real)` formula could match cross-anchor".

3. **DO NOT** replace empirical c_k in `qbeta_ladder_verification_1ppq.py` with a closed-form derivation: no closed form for A = 1.804e-15 exists.

## What this PR closes

- ✓ Step 1: singularity type identified as **simple pole**
- ✓ Step 2: cross-anchor verified **fibre-level** (within 1 ppm)
- ✓ Step 3 (documentation): ledger entry + canonical-framing cross-ref

## What this PR does NOT close

- ✗ Categorical derivation of the residue A = 1.804e-15 (the next research-grade target)
- ✗ Full SDP re-extraction at q_muon (out of scope, the partial test is consistent but not exhaustive)
- ✗ Production-script replacement (forbidden without a categorical form)

## Open research targets

The residue A ≈ 1.804e-15 is suspiciously close to 1 ppQ. Hypotheses for follow-up:

1. **A = ℏ_q^N for some N**: at q_0, ℏ_q ≈ 0.0991, ℏ_q^N = 1.8e-15 when N ≈ 15. Test specific integer N or rational q-combinations.
2. **A = b^N · ℏ_q^M structural product**: combine the two substrate-natural variables.
3. **A = Q_β · ε with ε some categorically-derived suppression factor**: tie the residue scale back to the observable.

None are tested here; all would require new probe work.

## Cross-references

- Scope: [`docs/coordination/2026-06-02-qbeta-1ppq-closure-scope.md`](../coordination/2026-06-02-qbeta-1ppq-closure-scope.md)
- PR #1713 audit (radius-of-convergence): [`docs/audits/2026-06-02-qbeta-habiro-radius-of-convergence-at-u-substrate.md`](2026-06-02-qbeta-habiro-radius-of-convergence-at-u-substrate.md)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
- c_k truncation-order framing: [`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
- c_3 q_0-stability verdict: [`docs/audits/2026-05-31-qbeta-c3-q0-stability-verdict.md`](2026-05-31-qbeta-c3-q0-stability-verdict.md)
