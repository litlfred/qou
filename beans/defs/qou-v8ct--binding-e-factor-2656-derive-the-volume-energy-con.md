---
# qou-v8ct
title: 'Binding E₀ factor 2.656: derive the volume-energy conversion without routing through m_e, or show the residual belongs to the bond factors (decision-frame avenue 1; queued, not dispatched)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T18:27:14Z
updated_at: 2026-10-04T15:12:00Z
parent: qou-v2om
---

Decision-frame §5 avenue 1. Derived E₀ = m_e/(q₀(q₀−1)) = 4.186 MeV vs best single scale 11.119 MeV (2.656×). E₀·|ln z| = 2.0507 MeV is the Markov-weight rendering (§7.1). Queued behind qou-qve5 — the shape residual is 22.7× the scale freedom, so shape first.

## 2026-09-08 — dispatched (front `e0-scale`, session qou-vyvt): enumerated, formalized, measured. NOT derived; stays open.

Branch `claude/binding-e0-scale-derivation-2026-09-08`. Producer
`computations/qbeta/qbeta_e0_scale_candidates_probe.py` (15/15, proton pin
`Q_50_DIGIT_STR`, 70 dps, AME parsed `parse_float=str`), witness
`qbeta-e0-scale-candidates.witness.json`. Lean
`QOU/Hecke/BindingScaleCandidates.lean`, 15 decls, sorry-free,
`[propext, Classical.choice, Quot.sound]`, lean-direct `-DautoImplicit=false`
exit 0 against the restored Mathlib cache.

### Corpus-grep, run before anything was declared open
`2.656` / `11.119` / `4.1859` / `4.2274` / "volume-energy conversion" across
docs/audits, content/, computations/, docs/coordination, .beans, library
INDEX.md (641 rows / 662 dirs), library/*/sections and library/*/ocr. The
scale question is worked in `qou-59j5` (completed, with the 2026-08-31
"E_0 is NOT derivable" addendum and the LP-dual negative), `qou-2pnv`,
`qou-qkbp` (derived form + tower ruling), `qou-xf14` (loop value pinned),
`qou-q7ga`. Library: no source on a volume->energy conversion in either tier.
Nothing new was found that closes it; everything below builds on those.

### 1. The candidate table (proton pin, 70 dps; last column DIAGNOSTIC only)

| key | formula | class | carrier | MeV | /E_0 | /11.119 |
|---|---|---|---|---:|---:|---:|
| E0_N0 | m_e/(q(q-1)) = m_e c_q^2 hbar_q | scale | YES (rem:energy-scale-planck) | 4.18598 | 1 | 0.3765 |
| E0_full | E0/(1-hbar_q^2) = m_e q/((q-1)(2q-1)) | scale | YES (ruling 2026-09-05) | 4.22748 | 1.00991 | 0.3802 |
| E0 abs ln z_D | per p-p bond (Markov weight, §7.1) | bond-content | no | 2.05071 | 0.4899 | 0.1844 |
| E0 ln[2]_q | per strand (qou-xf14) | bond-content | no | 2.92425 | 0.6986 | 0.2630 |
| 3 E0 ln[2]_q | per nucleon, 3 strands (qou-qkbp; mechanism unrealisable qou-0c19) | bond-content | no | 8.77274 | 2.0957 | 0.7890 |
| 3 E0_full ln[2]_q | same | bond-content | no | 8.85972 | 2.1165 | 0.7968 |
| E0/(q^2+1) | crossing weight | bond-content | no | 1.87540 | 0.4480 | 0.1687 |
| E0 [2]_q | loop value | bond-content | no | 8.41758 | 2.0109 | 0.7570 |
| E0 [3]_q!/q^3 | F_Bor dressing (muon anchor in m_p chain) | ladder-rung | no | 18.7347 | 4.4756 | 1.6849 |
| m_e | bare CAL-1 (qou-59j5 probes; not in E_0_CONVENTIONS) | ladder-rung | no | 0.51100 | 0.1221 | 0.0460 |
| m_e/hbar_q | | ladder-rung | no | 5.15735 | 1.2321 | 0.4638 |
| m_e/hbar_q^2 | mass prefactor (deprecated for absolute mass) | ladder-rung | no | 52.0515 | 12.435 | 4.681 |
| E0/hbar_q = m_e c_q^2 | | ladder-rung | no | 42.2478 | 10.093 | 3.800 |
| m_mu = m_e Vol(4_1)/hbar_q^2 | muon anchor (mass chain) | ladder-rung | no | 105.658 | 25.241 | 9.503 |
| m_mu hbar_q | dimensional combination, NO carrier anywhere — recorded as numerology | ladder-rung | no | 10.4688 | 2.5009 | 0.9415 |
| Q_beta closed | registry B (refuted multiplicative law; functional inadmissible under D) | registry | no | 0.78365 | 0.1872 | 0.0705 |
| y_0^* m_e | registry D, LP dual — recorded NEGATIVE | negative | no | 0.19182 | 0.0458 | 0.0173 |

Exactly TWO candidates carry a corpus derivation assigning them to the binding
scale, and both sit > 2x from 11.119: the 2.656 is not a truncation-order
question. The bond-content rows are pruned in Lean: `b_pp b_nn = 1/[2]_q^2`,
`b_pp = q^2/[2]_q`, `b_nn = q^-2/[2]_q`, `L_pp + L_nn = 2 ln[2]_q` — so [2]_q,
z_D, 1/(q^2+1) are INSIDE S and a scale carrying them double-counts. Every
candidate is m_e x f(q_0): the algebra is dimensionless, ONE anchor is
unavoidable (qou-qkbp), and "without routing through m_e" can only mean
"which f". The m_mu hbar_q row at 0.94 is exactly the kind of number the
anti-fit rule forbids landing on; it is listed so it is on record as having no
carrier.

### 2. What is proved (Lean)
- `E0_eq_planck`, `one_sub_hbarQ_sq`, `E0full_closed`, `E0full_div_E0`
  (generic Field): the two derived forms and their m_e-free ratio q^2/(2q-1).
- `E0full_eq_E0_mul_tsum` (ℝ, 1<q): "tower-summed" IS the geometric series
  sum_N hbar_q^{2N}.
- `fPP_mul_fNN`, `fPP_eq_sq_div_quantumTwo`, `fNN_eq_inv_sq_div_quantumTwo`,
  `fNN_eq_markovZ_sub_heckeH` (generic Field), `neg_log_fPP_add_neg_log_fNN`
  (ℝ): qou-xf14's pinning identity, previously symbolic-probe only.
- `sum_sq_sub_decomp`, `mean_minimises`, `sum_sq_eq_const_add_shape`,
  `bestLogScale_eq_mean`, `bestLogScale_singleton` (ℝ, Finset): the
  log-least-squares "best scale" is E_0 exp(mean ln r_i) — exactly the probe's
  `_geo` — so 11.119 is a SAMPLE STATISTIC of the residual.
- `residual_ratio_scale_invariant`, `candidate_ratio_indep_of_anchor`: no E
  changes any ratio r_i/r_j.

### 3. The separation measurement (2548 measured nuclides)
- best single scale (geo mean) = 11.11908 MeV = 2.65627 x E_0 (reproduces the
  30-dps 11.119).
- ln r_i = mu + eps_i: n mu^2 = 2431.7, sum eps^2 = 34.4 → a CONSTANT factor
  is 98.6 % of the squared log-residual; the shape is 1.4 % (RMS eps 0.116,
  ±12 %). In FORM the defect is overwhelmingly uniform.
- single-nuclide best scale runs 0.320 x E_0 (6H, drip line) .. 3.259 x E_0
  (4He); p5–p95 spread 1.225 (scale-invariant).
- band best scale / E_0: A<40 2.366 (n=247) · 40≤A<100 2.863 (593) ·
  100≤A<240 2.647 (1603) · A≥240 2.410 (105) · N=Z 2.813 (42) — drift 1.21x;
  the target moves with the sample.
- isotope chains at fixed Z (only the n-n count changes): r max/min = O 2.077,
  Ca 1.166, Ni 1.099, Sn 1.088, Pb 1.042 — every chain exceeds the ENTIRE
  derived scale freedom E0_full/E0 = 1.0099 (the threshold is derived, not sized
  to the miss).
- cross-check: under 3·E0_full exactly 1 of 2548 exceeds the bound (4He 1.0758),
  reproducing qou-qkbp.

### 4. Verdict — scope (a)
The 2.656 is a constant to 1.4 % of the squared log-residual, and a constant is
observationally INDISTINGUISHABLE between "scale defect" and "uniform
rescaling of all three bond energies": E·(cS) = (cE)·S. What a measurement CAN
assign is the non-uniform ±12 % (bands, chains, 4He vs 6H), and that is
bond-factor content by the scale-invariance lemma. So "is 2.656 a scale
defect?" cannot be answered at fixed law by any measurement; it is answerable
only by a DERIVATION of a uniform factor, and the corpus holds none with a
carrier — the tower gives 1.0099, the strand count 3 has no realisable
mechanism (qou-0c19), the LP dual is a recorded negative, and every other
enumerated quantity is either inside S already or a dimensional combination
with no block behind it. The fitted 11.119 is exp(mean ln r_i)·E_0, a sample
statistic of the missing SEMF shape, so no derived constant can be "checked
against" it until the shape is removed — and #7165 proves no pair-additive
bond count removes it. Not (b): no invariant forbids a uniform derived factor;
none has been found.

Next honest step (judgement): the uniform factor and the shape are coupled
through the sample mean, so the scale question is downstream of the shape
question (qou-qve5 / #7165), not parallel to it. Do not reopen "derive E_0" —
qou-59j5 already closed that; what would move this bean is a derived
per-nucleon multiplicity (the 3, or a replacement) with a realisable
mechanism, which qou-0c19 excludes for the colour tube.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 69 Formalization Progress (PR #8293)
- Formalized `QOU.Hecke.BindingScaleCandidates.fPP_div_fNN_eq_pow_four` (sorry-free, 0 advisories across all 6 static vacuity audits).
- Verified at 80-dps `mpmath` (`computations/probes/scale_mobius_adjoint_reduced_trefoil_probe.py`, `scriptHash: ae187b673714`, Commit 1 `9b139cda51963d9af6817b576a80c90bb2f74d00`, Commit 2 / Witness `474ee8c61ef5b687f244b6a129aeb23ef9956372`, PR `litlfred/qou#8293`).
