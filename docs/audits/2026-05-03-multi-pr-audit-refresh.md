# Multi-PR audit refresh — 2026-05-03

**Compiled** 2026-05-03 on `claude/4-parallel-followup-tests`.
**Scope**: synthesise findings from 6 in-flight / recent PRs and refresh the audit-flag ledger.

| PR | branch | status | scope |
|---|---|---|---|
| #503 | `claude/refactor-computation-framework-Dmvva` | **merged** | forward derivation; FROB-FILTER closed-form; MAG-126 1-shot; §3·B closed (crt_markov_v3) |
| #509 | `claude/electron-1-categorical-correction` | open | ELECTRON-1 closure; NV-1 PSLQ negative result |
| #511 | `claude/post-electron1-multi-tackle` | open | weak-spectral-completeness; crt_markov_v4; hecke_core_symbolic; 6 GS conjectures |
| #515 | `claude/4-parallel-followup-tests` | open (this branch) | 4-parallel followup tests; N_sym(q) framework; v4 key-bug fix |
| #512 | `claude/rho-3he-plan-h-probe` | open (other agent) | Plan H probe — single-integer ρ insufficient for ³He |
| #513 | `claude/ew-higgs-mass-ratio-probe` | open (other agent) | **EW/Higgs ratio test**: m_Z/m_W ✓ (2.7%); m_H/m_W ✗ (−11.4%) |
| #514 | `claude/plan-h-census-and-higgs-correction` | open (other agent) | Negative-result probes: Plan H census + Higgs scalar-correction sweep |

This document refreshes the audit-flag ledger across all of the above.

---

## §1. Conjecture status — what holds, what doesn't

### 🟢 Closed (post PR #503 / #509 / #511 / #515)

| Flag | Resolution | PR |
|------|-----------|----|
| **MAG-126** | q(378) = 174,972,341 in 1.47ms; 1000-sample κ=0 spot-check at 76.8ms | #503 |
| **FROB-FILTER** symbolic closed form | Σ_all(A+2)/Σ_all(A) = 3(q⁴−1)²/(8q⁴) verified A=1..6 | #503 |
| **§3·B** (Wedderburn at H_{3A}) | crt_markov_v3 predicts proton/²H/³H/³He to 0.05–0.32% | #503 |
| **ELECTRON-1** | "+1" = electron categorical action / m_e = 1 (forced by CAL-0) | #509 |
| **GAP 13a** (6 GS-residue opaques) | 6 conjectures explicitly authored | #511 |

### 🟡 Refined / sharpened (still open, but with concrete next-tests)

| Flag | Status | Most-likely next-test |
|------|--------|-----------------------|
| **NV-1** | Path-α structural id verified PSD-feasible (#511); explicit closed form blocked on $\mathcal{N}_{\rm sym}(q)$ | Discharge candidate (a) Gram determinant for $\mathcal{N}_{\rm sym}$ |
| **§3·A** v4 wiring | v4 has tower-term diagnostics (#511); fixed-key v4 mass pipeline (#515) shows wrong-direction correction with $\alpha_{\rm bind} = 8 m_e G$ | Re-test with $\alpha_{\rm bind}^{\rm EW} = m_e \cdot \mathcal{N}_{\rm sym}$ once derived |
| **§3·E** symbolic-in-q | hecke_core_symbolic.py companion module landed (#511) | Migrate downstream callers to use it |
| **GT-MATRIX** | $g_A = [5]_q/[4]_q (1 + \tfrac{2}{27}\hbar_q^2[5]_q)$ candidate at $10^{-5}$ residual | Locked on PDG g_A precision; future PDG measurement at ≥$10^{-5}$ would test |

### 🔴 Refined — what was conjectured doesn't hold as stated

| Flag | What was conjectured | Empirical finding | What's needed |
|------|---------------------|-------------------|---------------|
| **conj:electroweak-higgs-torus-link-triplet** (#511) | $m_W : m_Z : m_H \propto \mathrm{tr}_M(T(2,4)) : \mathrm{tr}_M(T(2,6)) : \mathrm{tr}_M(T(2,8))$ | **PR #513**: $m_Z/m_W$ matches to 2.7% ✓, **but $m_H/m_W$ off by −11.4% ✗**. PR #514 sweep of 18 corrections finds none clean. | Retract / reformulate: the W↔Z gauge-boson part survives; the Higgs scalar slot likely needs a different categorical structure (not the $T(2,8)$ vector form) |
| **SHELL-7 BB-stratum partition-sum** (#515) | $f_{\rm magic}(Z, N) = \sum_{\lambda = \lambda'} w_\lambda \chi_\lambda$ | **Pearson r = −0.057** vs AME shell corrections; predictions off by 73 orders of magnitude | Reformulate: full $\kappa = 0$ stratum (not just SC); different weight; restore (Z,N) dependence |
| **Plan H ρ-from-multiplicity** (#512) | $\rho \in \mathbb{Z}$ derivable from Wedderburn block count | "True" ρ at ³He = 2.062 — structural integer 2 plus 3.1% substrate-q correction | Refine: ρ has substrate-q-dependent correction beyond integer count |

### Cross-PR conjecture-revision impact

The most-significant retraction is `conj:electroweak-higgs-torus-link-triplet`. PR #513's empirical test is decisive:

| ratio | conjecture predicts | PDG | error |
|------:|--------------------:|----:|------:|
| $m_Z / m_W$ | 1.165 | 1.134 | +2.7% ✓ |
| $m_H / m_W$ | 1.381 | 1.558 | **−11.4%** ✗ |

**Survival of U5 monotonicity** (mass increases with crossings) is intact: $\mathrm{tr}_M(T(2, 2k))$ is strictly increasing in $k$. **What fails** is the assumption that the Higgs **scalar** belongs in the same family as $W^\pm$ and $Z$ **vectors**. Categorically natural fix: place $W^\pm, Z$ as $T(2,4), T(2,6)$ (the genus-1 + genus-2 even-twist torus links → vectors), and find a different categorical object for the Higgs scalar (likely a non-torus knot or a different host surface).

This is consistent with my own SHELL-7 finding (negative) and the audit's prior caveat that U2 (force-carriers as 2-component links) was a structural premise needing categorical justification.

---

## §2. New research-grade open problems exposed by the negative results

| ID | Problem | Most-tractable next step |
|----|---------|-------------------------|
| **HIGGS-SLOT** | Where does the Higgs scalar live in the QOU torus-knot dictionary? PR #513 rules out $T(2,8)$ at the simple $m \propto \mathrm{tr}_M$ level. | Test non-torus knots (4_1 / 5_2 / 6_3) for Higgs; or test Higgs as $T(2,8) + $ scalar-channel correction beyond Markov trace |
| **RHO-SUBSTRATE** | Plan H's $\rho$ has a 3.1% substrate-q correction beyond integer block-count (#512) | Identify the categorical origin of the +3.1% ³He correction |
| **N-SYM-CLOSED-FORM** | $\mathcal{N}_{\rm sym}(q_0) \approx 213.11$ has no clean simple closed form (#515) | Compute candidate (a) Gram determinant of EW Wedderburn block; check if it matches $\mathcal{N}_{\rm sym}$ to better than 1% |
| **SHELL-7-FULL-KAPPA** | SC-only partition sum gives r=−0.057 with AME (#515) | Test full κ=0 stratum (transpose-pair-summed) with proper Plancherel reweighting |

---

## §3. Refreshed workplan

### High-priority (1 day each, concrete tests)

1. **$\mathcal{N}_{\rm sym}$ Gram determinant** (closes NV-1)
   - Compute: Gram matrix of EW Wedderburn block under $\langle\cdot,\cdot\rangle_F$; compare $\det \mathcal{G}_{\rm EW}$ to 213.11
   - Outcome: either confirms candidate (a) and closes NV-1, or guides toward (b)/(c)

2. **HIGGS-SLOT non-torus probe** (recovers part of conj:electroweak-higgs-torus-link-triplet)
   - Compute: $\mathrm{tr}_M$ of figure-eight (4_1), $5_2$, and $6_3$ at $q_0$
   - Compare $m_H/m_W$ predictions to PDG 1.558
   - Outcome: locate the right Higgs slot and reformulate the conjecture

3. **SHELL-7 full κ=0 stratum** (rescues SHELL-7-SCALE)
   - Enumerate transpose-pair partitions of 3A with $\kappa(\lambda) + \kappa(\lambda') = 0$
   - Re-test against AME with proper q-Plancherel weight
   - Outcome: either rescues the partition-sum hypothesis or locates a deeper failure

### Medium-priority (2–4 days)

4. **Lean siblings** for the 9 new conjectures across PR #511 + #515:
   - `conj:weak-spectral-completeness`
   - `conj:n-sym-symmetric-channel-normalization`
   - 6 GS-residue conjectures
   - `prop:electron-categorical-action-unity` (already provable)

5. **Conjecture revision** for `conj:electroweak-higgs-torus-link-triplet`:
   - Split into `conj:weak-vector-bosons-genus-2-torus-links` (W±, Z = T(2,4), T(2,6))
   - And separate `conj:higgs-scalar-categorical-slot` (TBD per HIGGS-SLOT probe)
   - Update U2 / U4 references accordingly

### Research-grade (1–2 weeks each)

6. **Categorical Higgs mechanism** in $\mathbf{Rep}$ (still discharges U2/U4)
7. **Motivic-Galois character instance** for QOU at $q_0$ (GAP 6a)
8. **Pentagon $uv = q\,vu$ sharpness** + **closed-form mass endomorphism** (GAP 17/18)

---

## §4. Numbers to watch

| quantity | current best value at $q_0$ | source |
|----------|---------------------------:|--------|
| $1/\alpha_{\rm EM}$ | 137.035998166 | PR #503 prior, 6.7 ppb of CODATA |
| Q(n→p) | 0.7816 MeV (−0.097% of PDG) | #509 (ELECTRON-1) |
| Q(³H→³He) | 18.23 keV (−2.0% of PDG) | #509 (categorical Σ_all only) |
| MAE on 45 isotopes (k=5) | 0.006% | #503 / pre-existing |
| $N_v$ | 1,445,519.45 (read from CODATA $G_F$) | #509, #515 — **not yet derived** |
| $\mathcal{N}_{\rm sym}(q_0)$ | 213.111807… (pinned by $N_v$) | #515 — **not yet a closed form** |
| $g_A$ | 1.27510 PDG; leading [5]_q/[4]_q = 1.27028 (−0.4%) | #515 — at PDG precision floor |
| Higgs-slot under T(2,8) | $m_H/m_W$ = 1.381 vs PDG 1.558 | #513 — falsifies simple m∝tr_M for Higgs |
| ρ(³He) "true" | 2.062 (= 2 + 3.1% substrate correction) | #512 — single integer insufficient |

---

## §5. Recommended single-target

**Compute $\det \mathcal{G}_{\rm EW}(q_0)$** — the Gram determinant of the EW Wedderburn-block bilinear form, candidate (a) for $\mathcal{N}_{\rm sym}(q)$ closed form.

If matches 213.11 to better than 1%: NV-1 closes via the existing PSLQ infrastructure on extended basis.

If matches to 5–10%: identifies the leading-order structure and the next correction term to chase.

If matches at 30%+: rule out candidate (a), pursue (b) Higgs-eaten Goldstone or (c) Hochschild-Plancherel.

This is the single highest-value-per-day test currently available — it would either close a 🔴 hard flag or sharpen the conjecture's failure mode in a way that informs HIGGS-SLOT (which shares the EW Wedderburn machinery).

---

**End of audit refresh.**
