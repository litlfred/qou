---
# qou-uir6
title: Reconcile qou-za3q (Omega_2 Wenzl z_D ruling, 2026-09-13) with D7 full-tower binding
status: todo
type: task
priority: normal
created_at: 2026-10-11T07:23:25Z
updated_at: 2026-10-11T07:39:44Z
parent: qou-slz5
---

Owner 2026-10-11 asked to reconcile. The qou-za3q ruling adopted convention-D Wenzl weights for the Magnus Omega_2 binding pairing (Jones-Ocneanu characterisation; Plancherel refused). D7 (2026-09-07) puts binding on the full tower, and D is not faithful there (not_isFaithful_trLim). Faithful positive Markov traces are exactly z in [0, q-1/q] (FullTowerTraceWindow, #7612). Question: does the Omega_2 pairing belong to the decay channel (so D stands) or to binding (so it must move into the window)? Frame the options for the owner.


## 2026-10-11 corpus result (session_01ST9RpvTF7JHNdUNafrjf9J; paths 1-4 and 6; library and corpus_search not run)
- za3q (qou-za3q:522-526) adopted Wenzl z_D for P = Σ y_λ tr(ρ_λ Ω₂_λ). Its basis is Jones–Ocneanu: tr(1)=1, cyclicity, Markov stabilisation (qou-gba1:98-187). Its text never mentions D7, decay/binding or faithfulness, and it knowingly uses the r=2 row cap (qou-za3q:36).
- **Every author classifies Ω₂ as a BINDING correction** (probe titles, qou-gba1:21-23, qou-za3q:577). None calls it decay; the trace-convention registry has no Ω₂ row.
- **The za3q basis is z-generic.** Every Ocneanu weight is a z-Markov trace (FullTowerTraceWindow markov_ocneanuWeight / eq_ocneanu_of_markov). The 'pins z to 140 digits' control swapped only the scalar z under D weights, so it never compared against another Markov trace. The ruling correctly excludes Plancherel and is silent between z_D and the window.
- Blast radius: probes and beans only. No content block and no dashboard reads the Ω₂ witnesses.
- Ω₂ at z in [0,h]: NOT evaluated. P(z) is a polynomial in the weights (degree ≤ 3A); the per-λ traces are already in the three witnesses, so it is a cheap scan.
- Options: (i) classify as decay (contradicts every description); (ii) classify as binding and scan P(z) across the window; (iii) relabel the D results as a two-row/TL diagnostic. Agent judgement: (iii) plus the (ii) scan.


## 2026-10-11 window scan — P(z) measured on the whole faithful window (session_01ST9RpvTF7JHNdUNafrjf9J)
Probe `computations/deltalambda/magnus_omega2_window_scan_probe.py` + witness `magnus-omega2-window-scan.witness.json` (30/30 assertions).

**Inputs (checked, not assumed).** The three sign-probe witnesses are post the 2026-09-05 ordering ruling (deuteron/triton 2026-09-13, ⁴He 2026-09-11); each builds its word with `atom_braid_word_3A` with no `intra_order` override (default `borromean`); each carries ALL p(n) partitions, ≥3-row included (11/30/77); same q0 string. ⁴He's recorded scriptHash ≠ live producer (shallow clone, diff not inspectable); kept because its P_total_wenzl reproduces exactly at z_D. Nothing recomputed.

**Derived.** Weights = `ocneanuWeight q z μ` (OcneanuWeight.lean:91), slot Σ f^λ w_λ = 1 (verified as a polynomial identity in z). Each cell factor is linear in z with zero slope on the diagonal, so P(z) is a polynomial of degree 3A−1 (5/8/11); coefficients recorded in the witness. Cross-checks: w(z_D) = `y_lambda_wenzl_bridge_numeric` (≤6e-72); P(z_D) reproduces committed P_total_wenzl −6.92125 / −13.93056 / −20.46648 (≤5e-59); imaginary-rank form = direct form at y=1; every weight >0 on the grid.

**Measured, h = 0.2090603, 21-point grid + 2000-point sign scan + polyroots (agree):**
- A=2: P(0) = −0.77587 (Molien), P(h/2) = −1.55809, P(h) = −2.55122. **Negative on all of [0,h], no root.**
- A=3: P(0) = +2.9676e-4, P(h/2) = −0.13547, P(h) = −0.66367. **One root z_T = 7.99335e-4 (z_T/h = 0.0038235).**
- A=4: P(0) = +2.8143e-7, P(h/2) = −8.7325e-3, P(h) = −0.12694. **One root z_He = 2.09497e-3 (z_He/h = 0.0100209).**
- Sign pattern over A=2,3,4: **(−,+,+) on [0,z_T); (−,−,+) on (z_T,z_He); (−,−,−) on (z_He,h]** — every interior grid point and both h/2 and h give (−,−,−).

**Precision.** Traces are central-FD germs (EPS 1e-50 at 70 dps) → ~1e-20 relative despite 60 printed digits. Cancellation margin |P|/Σw|tr| at z=0 is 1.45e-3 (A=3), 1.36e-5 (A=4), ≥4.4e-1 (A=2); all signs determined against a 1e-15 floor. Root uncertainty from that floor: δz ≤ 5e-14.

**Reading (agent's, not a finding).** z_D's (−,−,−) is NOT an artifact of leaving the window: the same pattern holds on ~99 % of [0,h]. The Plancherel-like (−,+,+) survives only on a sliver of width z_T ≈ 0.4 % of the window next to the Molien endpoint z=0, where |P| is small (3e-4, 3e-7). So under options (ii)/(iii) of the entry above, moving into the window does not by itself produce the A=2→3 sign change except within ~0.4 % of the Molien end; any statement that it does would have to select that sliver, which is selection against the target. Nothing here selects a z.
