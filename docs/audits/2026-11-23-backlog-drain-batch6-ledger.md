# Repo Backlog Drain — Batch 6 Audit & Execution Ledger (`qou-rp3g`, `qou-ra4e`)

- **Date:** 2026-11-23
- **Parent Epic:** `qou-xip2` (Batch 6: `qou-rp3g` `Q-Drain-6` + `qou-ra4e` `Issues-Cluster-6`)
- **Base Commit (`origin/main`):** `e330ab6aa048abefe34a93474f667f3284483d71` (post-`#9200..#9221`)
- **Branch:** `origin/claude/backlog-drain-batch6-20261123`
- **Worker:** Worker 41 (`/Users/litlfred/space_cats/qou-wt/ws12-pr9180`)

---

## Executive Summary

1. **Verified Non-Conjectural Lean 4 Formalizations & Docstring Fixes Landed on `origin/claude/backlog-drain-batch6-20261123`:**
   - **`8bddf72a4dd`** (`feat(lean,qbeta): formalize C1 connection/Casoratian/singular-locus identities, bound-form q-Gevrey order, and GGM 4_1/5_2 docstring fix (qou-c1ln, qou-wgnx, qou-qbe9x, qou-slvl, qou-3ent)`):
     - Added sorry-free, axiom-free Lean 4 module `folio/quantum-observable-universe/lean/QOU/QBeta/C1ConnectionAlgebraicIdentities.lean` (`858` lines, `42` declarations = `31` theorems + `11` definitions, `lean -DautoImplicit=false -s 65536 -j 1` `EXIT=0`, `0` warnings, `0` `sorry`, `0` `axiom`, `0` self-assuming findings, `0` vacuous-theorem findings):
       1. **§1 — Ramified C1 Casoratian Recurrence (`qou-c1ln` Row 4, `qou-wgnx`):** `casoratian_step_cleared`, `casoratian_iterated_cleared`, `casoratian_step_div`, and `det_ramifiedCompanion` proving over any `[CommRing R]` / `[Field K]` that any pair of solutions of the ramified $u$-gauge C1 system satisfies $(1 - q^2 u^2)\,W(p u) = -p^2(1 - q)\,W(u)$ and $\prod_{k=0}^{n-1}(1 - q^2(p^k u)^2)\,W(p^n u) = (-p^2(1 - q))^n\,W(u)$.
       2. **§2 — Elliptic Constancy & Rebasing Invariance (`qou-c1ln` Row 4, `qou-wgnx`):** `connectionMatrix_elliptic_units`, `connectionMatrix2_elliptic`, `casoratian_ratio_elliptic`, and `chi_rebasing_invariant` proving $P(p u) = P(u)$ whenever $Y_\infty(p u) = A(u) Y_\infty(u)$ and $Y_0(p u) = A(u) Y_0(u)$ in $\mathrm{GL}_n(R)$, plus invariance of the Birkhoff cross-ratio $\chi(P) = (P_{00}P_{11})/(P_{01}P_{10})$ under right-diagonal gauge $P \mapsto P\,\mathrm{diag}(d_0, d_1)$ over any `[Field K]`.
       3. **§3 — Real-Fixed-Locus Reflection Law (`qou-c1ln` Row 6, `qou-wgnx`):** `connectionMatrix2_conj_row_swap`, `connectionMatrix2_fixed_locus_rows`, `chi_reflection_law`, and `norm_chi_real` proving that when conjugation swaps the two infinity-side basis rows ($Y_\infty(\bar u) = S\,\overline{Y_\infty(u)}$, $S = \begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$) and commutes with $Y_0$, $P(\bar u) = S\,\overline{P(u)}$, so on the real locus $u = \bar u$ one has $P_{10} = \overline{P_{00}}$, $P_{11} = \overline{P_{01}}$, $\chi(P)\,\overline{\chi(P)} = 1$, and $\|\chi(P)\| = 1$ in `ℂ`.
       4. **§4 — Canonical vs Edge Normalisation & Divisor Product (`qou-c1ln` Row 6, `qou-wgnx`):** `canonical_vs_edge_sq_ratio` ($(\theta_c(q,-u)/\theta_c(q,u))^2 / (\theta(q^2,-q u)/\theta(q^2,q u))^2 = q$), `connDivisor_product_sq_eq_q_cubed` ($(\alpha\beta)^2 = q^3$ for roots $\alpha,\beta$ of $X^2 \pm \sqrt{q(1-q)}\,X + q^{3/2}$), and `norm_connDivisorAlpha_eq_q_three_quarters` ($\|\alpha_{\mathrm{conn}}(q)\| = q^{3/4}$ for $0 < q < 1$, strictly unifying the canonical-gauge vs edge-gauge theta-quotient normalisations).
       5. **§5 — Third Singular Site $x = q^{-2}$ on Identity Orbit $[1] \in E_q$ (`qou-qbe9x`):** `det_companion_gauge`, `coeff_comp_C_mul_X`, `natDegree_comp_C_mul_X`, `comp_C_mul_X_ne_zero`, `natTrailingDegree_comp_C_mul_X`, `torusDeg_comp_scale_eq`, and `c1_third_singular_site_torusDeg_neg_one` proving that rational companion gauge transformations multiply $\det A(x)$ by $g(q x)/g(x)$ whose torus divisor degree $\mathrm{deg}(\mathrm{div}(\cdot)|_{K^\times}) = \mathrm{natDegree} - \mathrm{natTrailingDegree}$ vanishes identically, whereas C1's `detA q x = -(q - 1)/(q^2 x - 1)` has pole $x = q^{-2}$ (representing $[1] \in \mathbb{C}^\times / q^{\mathbb{Z}}$) of net torus degree $-1 \neq 0$, hence cannot be gauged away over $K^\times$.
       6. **§6 — RSZ §1.3.2 Bound-Form $q$-Gevrey Order & Full Lacunary $L_k$ Sequence (`qou-slvl` item 1):** `IsQGevreyOrderLE`, `isQGevreyOrderLE_of_order_add_eps`, `not_forall_isQGevreyOrder_imp_le` (explicitly refuting the unshifted $\varepsilon = 0$ implication via $a_n = n + 1$), `lacunarySlopeKCoeff`, and `lacunarySlopeKCoeff_orderLE_sharp` proving without subsequence restriction that the full lacunary series $L_k(z) = \sum_{m\ge 0} q^{-k m^2/2} z^{k m}$ belongs to $\mathbb{C}[[z]]_{q;\,1/k}$ and to no $\mathbb{C}[[z]]_{q;\,s}$ with $s < 1/k$.
     - Updated `folio/quantum-observable-universe/lean/QOU/QBeta/StokesDTBPSBridge.lean` (`qou-3ent`, `EXIT=0`, `0` warnings, preserving zero-instance `class StokesDTBPSBridge` per Rule 13a): corrected stale docstrings attributing $\{3, 4\}$ to $4_1$ (it is $5_2$ data from Garoufalidis–Gu–Mariño §3.2 eqs. 96/98), noted GGM eq. 21 is diagonal-only and GGM Conjecture 3(d) is conditional for every knot including $4_1$ (matching `#7592` `65c3a99eab7`), and linked `QOU.Nuclear.ColourReconnectionStokesAssembly.ggm_stokes_symmetry_three` (`#9221` `bdb51c4b35c`).
   - **Strict Anti-Fit Compliance (`qou-offl`):** Zero fitting performed (`NO FITTING, EXCEPT CAL-1/2/3`); zero `float64` introduced.

2. **Batch 6 Triage Totals (`origin/main` = `e330ab6aa04`):**
   - **`qou-rp3g` (`Q-Drain-6` — 13 Child Beans):**
     - **1 `ALREADY-DONE` on `origin/main` (ready to mark `completed` immediately on owner/coordinator sync):** `qou-slpd` (items 1–5 + final owner-card fix in **PR `#8825`** `314ce7c5120` / `50e0af4c79a` on `origin/main`; bean explicitly says *"Close when it merges"*).
     - **2 `DONE AFTER BATCH 6 MERGES` (`8bddf72a4dd`, no Rule-13a conjecture tags):** `qou-slvl` (items 1 & 2 on `origin/main` + optional bound-form `IsQGevreyOrderLE` / `lacunarySlopeKCoeff_orderLE_sharp` in `8bddf72a4dd`), `qou-qbe9x` (`05abb83e8c2` write-up + `0-sorry` torus-degree non-removability proof in `8bddf72a4dd`, candidate `completed` on owner OK).
     - **2 `TARGET-DISSOLVED / NEEDS-OWNER` (`scrapped` vs re-title under `qou-frzo`):** `qou-odh5`, `qou-wgnx` (local Stokes multipliers at $\infty$ proved dimension `0` by pure isoclinicity $k = 1$ on `origin/main` in `QOU.MathlibExt.RSZ.c1_infinity_isoformalDim_eq_zero`; connection matrix $P$/$\chi$ algebraic layer now `0-sorry` in `8bddf72a4dd`, while `BirkhoffCrossRatioSuppliesAmplitude` stays a 0-instance §3b class).
     - **1 `[PAUSED]` bean with full algebraic layer discharged in `8bddf72a4dd`, kept `todo` per owner `85e79364e87`:** `qou-c1ln`.
     - **7 Rule-13a / owner-gated beans narrowed cleanly against `origin/main` (including `#9221` `bdb51c4b35c`) and kept strictly open:** `qou-8vt2`, `qou-offl`, `qou-vr3q`, `qou-3ent` (100% of prose + Lean docstring action item completed via `#7592` `65c3a99eab7` + `8bddf72a4dd`; kept open solely for Rule-13a `StokesDTBPSBridge`), `qou-vdvE`, `qou-8mtd`, `qou-eptr`.
   - **`qou-ra4e` (`Issues-Cluster-6` — 12 Open GitHub Issues + `#9154` Guard):**
     - **3 Issues `100% LANDED ON origin/main` (ready to close on owner OK):** **`#7710`** (PR `#7719` `e1f5d1b4e6c` + `#7673` `69ba92de67f` + `#8859` `e2c49449b7a`), **`#7704`** (PR `#7706` `860f6dba1c2`), **`#7703`** (PR `#7705` `1eeebc5f0df`).
     - **2 Issues `CORE / PER-CLASS MANDATE SETTLED ON origin/main` (candidate close on owner OK vs keep for narrow residual):** **`#7092`** (PRs `#7183` `caf9210bfcf`, `#7273` `f933db58cd4`, `#7290` `f039bf90ef2` — 100% of falsifiable coboundary question answered while `qou-qjhc` stays `in-progress`), **`#7942`** (PRs `#7946` `823cda34561`, `#9139` `02715c7f7f8`, `#9189` `bdb0f07969a`, `#9211` `cf39d247932` — all 3 classes instantiated/narrowed/refuted; only `x > 1` `Re Li₂` restatement `qou-adgd` & period-conjecture-obstructed `BringZeroModeBlochClass` `qou-006b` remain).
     - **7 Issues `KEEP OPEN` (residual items / open PRs / derivation gaps):** `#7400`, `#7912`, `#8979`, `#8967`, `#8809`, `#7550`, `#6897`.
     - **Special Guard `#9154`:** **STRICTLY KEPT OPEN** (`#9157` and `#9095` remain unmerged).

---

## Section 1 — `qou-rp3g` (`Q-Drain-6`): Audit of All 13 Child Beans Against `origin/main` (`e330ab6aa04`)

### 1.1 Summary Table

| Bean | Current Status | Rule-13a Guard / Conjecture Class | Status on `origin/main` (`e330ab6aa04`) + Batch 6 (`8bddf72a4dd`) | Recommended Transition |
| :--- | :---: | :--- | :--- | :--- |
| **`qou-slpd`** | `todo` | None (batch PR `#8457` closed/rejected) | **100% on `origin/main`:** Items 1–5 landed (`53275fa93d8`, `115f5405cbd`, `21a01411ec6`, `a8fbee879b7`, `60968f685c2`), and final owner-card fix on `theta_eq_half_gs_bridge` (`QGevreyOrder.lean:571–575, 764–775`) merged in **PR `#8825`** (`314ce7c5120` / `50e0af4c79a`). | **`completed`** (already on `origin/main`) |
| **`qou-slvl`** | `in-progress` | None | Items 1 (`slopeKCoeff_order`, `QGevreyOrder.lean:1031–1118`) & 2 (`infCoeffAt_eq_zero_iff`, `zeroCoeffAt_eq_zero_iff`, `C1SeriesConvergence.lean:541–569` + `c3_w2_c1_side_recursions_derived.py`) `0-sorry` on `main`; optional bound-form `IsQGevreyOrderLE` + full lacunary `L_k` order discharged `0-sorry` in **`8bddf72a4dd`** (`C1ConnectionAlgebraicIdentities.lean` §6). Supersedes `#8195` on `qou-slvl`. | **`completed`** once Batch 6 (`8bddf72a4dd`) merges |
| **`qou-qbe9x`** | `in-progress` | None | Exact 3-site singular locus write-up in `05abb83e8c2`; `0-sorry` algebraic proof that $x = q^{-2}$ (`[1] \in E_q`) has gauge-invariant torus divisor degree $-1 \neq 0$ (`torusDeg_comp_scale_eq`, `c1_third_singular_site_torusDeg_neg_one`) landed in **`8bddf72a4dd`** (`C1ConnectionAlgebraicIdentities.lean` §5). Supersedes `#8195` on `qou-qbe9x`. | **`completed`** on owner OK once Batch 6 (`8bddf72a4dd`) merges |
| **`qou-c1ln`** | `todo` (`[PAUSED]`) | Paused by owner `85e79364e87` (`0` consumers) | Rows 1 (`C1ConnectionPoles.lean`), 2 (`C1ThetaZeroLocus.lean`, `#4770`), 3 (`C1SeriesConvergence.lean`) `0-sorry` on `main`; Row 5 do-not-work; **entire algebraic layer of Rows 4 & 6 discharged `0-sorry` in `8bddf72a4dd`** (`C1ConnectionAlgebraicIdentities.lean` §§1–4). Only paused analytic meromorphy/JTP glue remains. | Keep **`todo` (`[PAUSED]`)**, narrowed with `8bddf72a4dd` citation |
| **`qou-odh5`** | `in-progress` | Target dissolved; `qou-frzo` alien-calculus question | Local Stokes multipliers at $\infty$ proved dimension `0` ($k=1$ pure isoclinic) `0-sorry` on `main` (`QOU.MathlibExt.RSZ.c1_infinity_isoformalDim_eq_zero`, `ThetaSlopeArithmetic.newtonSlopes_c1`; `b8bc5a41a7c`, `ee212cc3635`). Open PR `#8230` unmerged. | **`NEEDS-OWNER`**: `scrapped` (dissolved target) vs re-title under `qou-frzo` |
| **`qou-wgnx`** | `in-progress` | `BirkhoffCrossRatioSuppliesAmplitude` (`0` instances, §3b) | Local Stokes at $\infty$ trivial (`c1_infinity_isoformalDim_eq_zero`); $P$/$\chi$ closed form (`c3_w2_c1_connection_matrix.py`, `C1ConnectionPoles.lean`) + algebraic Casoratian/ellipticity/reflection/divisor proofs in **`8bddf72a4dd`**; $\|\chi\| = 1$ on $\mathbb{R}$ (`norm_chi_real`), refuting naive real-locus amplitude against $r^* \approx 1.585$. Open PR `#8201` unmerged. | **`NEEDS-OWNER`**: `scrapped` vs keep open for `BirkhoffCrossRatioSuppliesAmplitude` / `qou-frzo` |
| **`qou-8vt2`** | `todo` | Rule 13a: `SDeformedVolumeChannel` (`0` instances) | 4 exclusion filters (`ChannelMeridianIdentification.lean`, `CompleteStructureExclusion.lean`, `ThetaLipschitzObstruction.lean`, `SLeakZeroCrossing.lean`) + $q$-JM eigenvalue/parity narrowing (`7a1e138ce64`, `9cf9bd2b62f`) `0-sorry` on `main`; `SDeformedVolumeChannel.u` remains uninstantiated (`channelFree`). PR `#8245` closed (`#8531`). | Keep **`todo`** (Rule 13a) |
| **`qou-offl`** | `in-progress` | Rule 13a: `stays open` + **NO FITTING** | Rescoped 2026-11-22 to pure cone-manifold / generalized Dehn-filling geometry of $4_1$ and $\mathbb{B}_3$ (dropping all comparison/fitting to T4-inverted $\vartheta$). `FigureEightDeformedMeridianWinding.lean` + `qbeta_offl_ratio_candidates_unfalsifiable_probe.py` (`c387138d01d`) on `main`; PR `#8213` (`OPEN`) is scalar algebra only. | Keep **`in-progress`** (Rule 13a, zero fitting) |
| **`qou-vr3q`** | `todo` | Rule 13a: `FaddeevPhi`, `FaddeevPhiPhysical` (`0` instances) | Uniqueness modulo regularity (`DoublyPeriodicLiouville.lean`, `FaddeevPhiFullUniqueness.lean`), `StokesQZeroDTCount.lean` ($S^+(0)_{01} = 3$), `FiveTwoDTSpectrumSplit.lean`, **and `#9221` (`bdb51c4b35c` `ColourReconnectionStokesAssembly.ggm_stokes_symmetry_three` proving $\tilde S_{01} + \tilde S_{10} = 3\tilde S_{00}$ bilinearly from GGM eq. 59a)** on `main`. PR `#8277` closed (`#8531`). | Keep **`todo`** (Rule 13a; narrow with `#9221` `bdb51c4b35c`) |
| **`qou-3ent`** | `in-progress` | Rule 13a: `StokesDTBPSBridge` (`0` instances) | Prose fixed on `main` in **PR `#7592`** (`65c3a99eab7` in `aomega-fourone-dt-count.{md,ts}` & `stokes-dt-bps-bridge.md`); `#9221` (`bdb51c4b35c`) proved $A_\omega = 3$ bilinearly from GGM eq. 59a Wronskian sandwich; **last stale Lean docstring in `StokesDTBPSBridge.lean` fixed in `8bddf72a4dd`** (superseding that piece of `#8236`). | Keep **`in-progress`** per Rule 13a (`StokesDTBPSBridge` 0-instance), with prose/docstring action item marked **100% done** |
| **`qou-vdvE`** | `in-progress` | Rule 13a: `stays open` (outward-facing owner gate) | Exact evaluation, SnapPy checks, and `one_loop_vdv_constant_closed_form_probe.py` landed on `main` (`5518a024e5f`, `e0ae78061d5` port of `#8358`), plus `docs/outreach/2026-08-08-van-der-veen-whitehead-chains-corrections.md` (`8a3cc3dac7d`). Awaits owner review/decision to send note to Roland van der Veen. | Keep **`in-progress`** (owner outreach gate) |
| **`qou-8mtd`** | `in-progress` | Rule 13a: `HyperbolicVolumeBridge` (`0` instances) | Conditional bridge `ManifoldVolumeBridge.lean` (`900295ff69c`, `b41a6f6dda7`), `MostowTriangulationBridge.lean` (`96179f6f00f`), and `HyperbolicQuotient.lean` (`#6056` `7f225713a2d`) `0-sorry` on `main` (PR `#8483` closed). Mostow + Thurston hyperbolisation + triangulation remain open. | Keep **`in-progress`** (Rule 13a) |
| **`qou-eptr`** | `todo` | Rule 13a: `stays open` (`b_3` binding gap `qou-brng`) | Route-level structural obstruction proved/measured on `main` (`af4828e3081`, `2af417f6c45`, `f6129d4044f`, `c902ae566f6` port of `#8145`: `atom_canonical_crossings` uses $2A$ `averaged` Hecke letters outside $\mathrm{im}(B_n \to H_n(q))$); `#9221` (`bdb51c4b35c` Part B) supplies an alternative $6q$–$12q$ skew-Howe colour-reconnection carrier (`5, 42, 462` singlets). | Keep **`todo`** (Rule 13a; narrow with `c902ae566f6` + `#9221` `bdb51c4b35c`) |

### 1.2 Detailed Per-Bean Evidence Notes (`qou-rp3g`)

1. **`qou-slpd` — *Lean: C1 formal-solution growth at 0 and ∞ — q-Gevrey index s = 1 and θ = ½ bridge*:**
   - **Landed on `origin/main`:**
     - Item 1 (`IsQGevreyOrder` / `IsQGevreyOrderUpTo`): `folio/quantum-observable-universe/lean/QOU/Mathlib/QGevreyOrder.lean` (`53275fa93d8`).
     - Item 2 (`newtonSlopes_c1` = `{-1}`, `newtonSlopes_c1_inf` = `{1}`, `thetaFromSlope_eq_half`): `folio/quantum-observable-universe/lean/QOU/QBeta/ThetaSlopeArithmetic.lean` (`115f5405cbd`).
     - Item 3 (`c1ZeroFormalCoeff`, `c1InfFormalCoeff`, `c1ZeroFormalCoeff_order`, `c1InfFormalCoeff_order`): `folio/quantum-observable-universe/lean/QOU/QBeta/C1FormalSolutionGrowth.lean` (`21a01411ec6`, `60968f685c2`).
     - Item 4 (sharp `s = 1` lower/upper growth): `QGevreyOrder.lean` (`a8fbee879b7`).
     - Item 5 + Owner-card fix (`theta_eq_half_gs_bridge` docstring scoping Garoufalidis–Sun vs Ramis $q$-Borel–Laplace): merged on `origin/main` in **PR `#8825`** (`314ce7c5120`, commit `50e0af4c79a`, verified at `QGevreyOrder.lean:571–575, 764–775`).
   - **Verdict:** Bean body explicitly states *"Fix applied on owner card (2026-11-21) in PR #8825 ... Close when it merges."* `#8825` is merged on `origin/main` (`e330ab6aa04`). Ready to mark **`completed`** immediately.

2. **`qou-slvl` — *Close the two narrow generalisations left open by qou-slpd*:**
   - **Landed on `origin/main`:**
     - Item 1 (limit form for every integer $k \ge 1$): `slopeKCoeff` and `slopeKCoeff_order` (`IsQGevreyOrder q (1 / (k : ℝ)) (slopeKCoeff q k)`) in `QOU/Mathlib/QGevreyOrder.lean:1031–1118` (`0 sorry`).
     - Item 2 (closed-form C1 recursion derivation at both $x = 0$ and $x = \infty$): `infCoeffAt`, `infCoeffAt_eq_zero_iff`, `zeroCoeffAt`, `zeroCoeffAt_eq_zero_iff` in `QOU/QBeta/C1SeriesConvergence.lean:541–569` (`0 sorry`) + `computations/qbeta/c3_w2_c1_side_recursions_derived.py` (`4517bb590a7`).
   - **Discharged in Batch 6 (`8bddf72a4dd`):**
     - `QOU/QBeta/C1ConnectionAlgebraicIdentities.lean` §6 formalizes RSZ Astérisque 355 §1.3.2 big-$O$ bound-form `IsQGevreyOrderLE`, proves `isQGevreyOrderLE_of_order_add_eps` and `not_forall_isQGevreyOrder_imp_le` (refuting the unshifted $\varepsilon = 0$ implication), and proves `lacunarySlopeKCoeff_orderLE_sharp` (`IsQGevreyOrderLE q (1 / (k : ℝ)) (lacunarySlopeKCoeff q k) ∧ ∀ s < 1 / (k : ℝ), ¬ IsQGevreyOrderLE q s (lacunarySlopeKCoeff q k)`) for the full lacunary sequence $L_k$ without subsequence restriction.
   - **Verdict:** Zero Rule-13a conjecture classes; supersedes unmerged dirty PR `#8195`'s `qou-slvl` claim. Ready to mark **`completed`** once `8bddf72a4dd` merges.

3. **`qou-qbe9x` — *Audit the third singular site [1] ∈ E_q of C1*:**
   - **Landed on `origin/main` + Batch 6 (`8bddf72a4dd`):**
     - Complete 3-site classification recorded in `05abb83e8c2`: $x = 0$ (irregular, Newton slope $-1$, $q$-Gevrey index $1$), $x = \infty$ (irregular, pure isoclinic slope $+1$, $q$-Gevrey index $1$), and $x = q^{-2}$ (representing $[1] \in \mathbb{C}^\times / q^{\mathbb{Z}}$, finite apparent/determinantal singularity where $\det A(x) = -(q - 1)/(q^2 x - 1)$ has a simple pole).
     - `QOU/QBeta/C1ConnectionAlgebraicIdentities.lean` §5 (`8bddf72a4dd`) proves `det_companion_gauge`, `torusDeg_comp_scale_eq`, and `c1_third_singular_site_torusDeg_neg_one`: any rational companion gauge transformation $y \mapsto g(x) y$ multiplies $\det A(x)$ by $g(q x)/g(x)$ whose torus divisor degree on $K^\times$ is identically $0$, whereas `detA q x` has net torus divisor degree $-1 \neq 0$ concentrated at $x = q^{-2}$, so $[1]$ survives every rational companion re-normalisation on $K^\times$.
   - **Verdict:** Zero Rule-13a tags; supersedes unmerged dirty PR `#8195`'s `qou-qbe9x` claim. Ready to mark **`completed`** on owner OK once `8bddf72a4dd` merges.

4. **`qou-c1ln` — *[PAUSED] Lean: C1 Birkhoff connection matrix and divisor invariant*:**
   - **Landed on `origin/main` (`0 sorry`):**
     - Row 1 (`differentiableOn_qThetaC`, `qThetaC_functional_eq`): `QOU/QBeta/C1ConnectionPoles.lean`.
     - Row 2 (`qThetaC_eq_zero_iff` via Jacobi triple product): `QOU/QBeta/C1ThetaZeroLocus.lean` (`#4770`).
     - Row 3 (`summable_zeroSideCoeff`, `summable_infSideCoeff`, `zeroSide_recurrence`): `QOU/QBeta/C1SeriesConvergence.lean`.
     - Row 5 ($F_\pm$ asymptotic basis): explicitly marked **do not work** (`0` downstream consumers).
   - **Discharged in Batch 6 (`8bddf72a4dd`, `0 sorry`):**
     - `QOU/QBeta/C1ConnectionAlgebraicIdentities.lean` §§1–4 discharges the **entire purely algebraic layer** of Rows 4 & 6: Casoratian step & $n$-step product (`casoratian_step_cleared`, `casoratian_iterated_cleared`, `casoratian_step_div`, `det_ramifiedCompanion`), elliptic constancy of $P(u) = Y_\infty(u)^{-1} Y_0(u)$ (`connectionMatrix_elliptic_units`, `connectionMatrix2_elliptic`, `casoratian_ratio_elliptic`), diagonal rebasing invariance of $\chi(P)$ (`chi_rebasing_invariant`), real-locus row-swap reflection $P(\bar u) = S\,\overline{P(u)} \implies \chi\bar\chi = 1 \implies \|\chi\| = 1$ (`connectionMatrix2_conj_row_swap`, `chi_reflection_law`, `norm_chi_real`), canonical-vs-edge theta-quotient ratio $q$ (`canonical_vs_edge_sq_ratio`), and connection-divisor identities $(\alpha\beta)^2 = q^3$, $\|\alpha_{\mathrm{conn}}(q)\| = q^{3/4}$ (`connDivisor_product_sq_eq_q_cubed`, `norm_connDivisorAlpha_eq_q_three_quarters`).
   - **Remaining paused analytic layer:** Matrix meromorphy of $Y_0, Y_\infty$ on $\mathbb{C}^\times$ and analytic identification of $\chi(Y_\infty^{-1}Y_0)$ with the explicit theta closed form (`0` downstream consumers; stays **`todo` (`[PAUSED]`)** per owner `85e79364e87`).

5. **`qou-odh5` (*Derive the C1 Stokes multiplier at x = ∞ via q-Borel-Laplace*) & `qou-wgnx` (*Extract the Stokes / connection data of C1 directly*):**
   - **Status on `origin/main` + Batch 6 (`8bddf72a4dd`):**
     - Local Stokes multipliers at $x = \infty$ are **identically trivial** (dimension `0`) because C1 at $\infty$ is pure isoclinic of single slope $k = 1$, proved `0-sorry` in `QOU/MathlibExt/RSZ.lean` (`c1_infinity_isoformalDim_eq_zero`) and `QOU/QBeta/ThetaSlopeArithmetic.lean` (`newtonSlopes_c1_inf`), and audited in `docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md` & `docs/audits/2026-08-08-c1-infinity-has-no-stokes-multiplier.md` (`b8bc5a41a7c`, `ee212cc3635`).
     - Global Birkhoff connection matrix $P(u)$ and $\chi$ closed form are computed at 80 dps in `computations/qbeta/c3_w2_c1_connection_matrix.py`, pole-typed in `QOU/QBeta/C1ConnectionPoles.lean`, and algebraically proved in `8bddf72a4dd` (`C1ConnectionAlgebraicIdentities.lean` §§1–4), including $\|\chi\| = 1$ on the real locus (confirming scope-(a) negative against $r^* \approx 1.585$; `BirkhoffAmplitudeE.BirkhoffCrossRatioSuppliesAmplitude` remains a 0-instance §3b class).
     - Unmerged batch PRs `#8230` (`qou-odh5`) and `#8201` (`qou-wgnx`) remain `OPEN` and dirty.
   - **Verdict:** Both beans explicitly note that choosing between `scrapped` (dissolved local-Stokes target) vs re-titling under `qou-frzo` ($q$-native alien calculus / `qou-vkg5`) is **`NEEDS-OWNER`**.

6. **`qou-8vt2` — *Derive the figure-eight S-deformed channel u(q) from first principles*:**
   - **Status on `origin/main`:** Four structural exclusion theorems (`ChannelMeridianIdentification.lean`, `CompleteStructureExclusion.lean`, `ThetaLipschitzObstruction.lean`, `SLeakZeroCrossing.lean`) and $q$-Jucys–Murphy eigenvalue/parity narrowing (`7a1e138ce64`, `9cf9bd2b62f`) are `0-sorry` on `main`. Batch PR `#8245` was closed in `#8531`.
   - **Verdict:** Keep **`todo`** per Rule 13a (`SDeformedVolumeChannel` in `QOU/Mass/FigureEightChannel.lean` has `0` instances; `channelFree` proves `u` is unconstrained by existing axioms).

7. **`qou-offl` — *Off-shell deformed 4_1 / B_3 geometry at real q (pure cone-manifold geometry)*:**
   - **Status on `origin/main`:** Rescoped 2026-11-22 to pure cone-manifold / generalized Dehn-filling geometry of $4_1$ and $\mathbb{B}_3$ at real $q$, dropping all comparison/fitting to T4-inverted $\vartheta$ values. `QOU/QBeta/FigureEightDeformedMeridianWinding.lean` and `computations/probes/qbeta_offl_ratio_candidates_unfalsifiable_probe.py` (`c387138d01d`) are on `main`; open PR `#8213` contains only scalar algebra and does not close the cone-manifold geometry.
   - **Verdict:** Keep **`in-progress`** per Rule 13a (`stays open`), strictly enforcing **`NO FITTING, EXCEPT CAL-1/2/3`**.

8. **`qou-vr3q` — *Derive the figure-eight Stokes multiplier A_ω = 3 from the state integral*:**
   - **Status on `origin/main` (including `#9221` `bdb51c4b35c`):**
     - `QOU/QBeta/DoublyPeriodicLiouville.lean` + `FaddeevPhiFullUniqueness.lean` (`faddeevPhi_uniqueUpToScalar`), `StokesQZeroDTCount.lean` ($S^+(0)_{01} = 3$), and `FiveTwoDTSpectrumSplit.lean` are `0-sorry` on `main`.
     - **Major `#9221` narrowing (`bdb51c4b35c` / commit `fe4f1320214`):** `QOU/Nuclear/ColourReconnectionStokesAssembly.lean` proves `ggm_stokes_symmetry_three` and `ggm_discharges_symmetryConstant_and_imV41` over any `[CommRing R]` (`0 sorry`): from GGM eq. (59a)'s bilinear Wronskian sandwich $\tilde S(W) = J\,W^T\,\Sigma^{-1}\,W$ with $A_{4_1} = \begin{psmallmatrix}-1&3\\0&-2\end{psmallmatrix}$ ($\Sigma^{-1} = \begin{psmallmatrix}0&1\\-1&3\end{psmallmatrix}$), $\tilde S_{01}(W) + \tilde S_{10}(W) = 3\,\tilde S_{00}(W)$ identically for **every** $2\times 2$ Wronskian $W$, and at $W_{-1}(0) = \begin{psmallmatrix}0&2\\-1&0\end{psmallmatrix}$ one gets $\tilde S = 2\begin{psmallmatrix}1&3\\0&1\end{psmallmatrix}$, discharging `SymmetryConstantFromThreefold` without importing $S^+(0)_{01} = 3$ entry-by-entry!
     - Batch PR `#8277` was closed in `#8531`.
   - **Verdict:** Keep **`todo`** per Rule 13a (`FaddeevPhi` and `FaddeevPhiPhysical` have `0` instances; internal Hecke/categorification derivation of $A_{4_1}$ / DT invariants without importing GGM's cusp matrix $\Sigma$ remains open).

9. **`qou-3ent` — *Reconcile the A_ω = 3 DT-invariants bridge with GGM's actual Conjecture 3 status*:**
   - **Status on `origin/main` + Batch 6 (`8bddf72a4dd`):**
     - Prose files `folio/quantum-observable-universe/content/mass-theory/aomega-fourone-dt-count.{md,ts}` and `stokes-dt-bps-bridge.md` were already corrected on `origin/main` in **PR `#7592`** (`65c3a99eab7`).
     - `#9221` (`bdb51c4b35c`, `ColourReconnectionStokesAssembly.lean`) proved $A_\omega = 3$ bilinearly from GGM eq. (59a)'s Wronskian sandwich without relying on GGM Conjecture 3(d).
     - **Commit `8bddf72a4dd`** updates `QOU/QBeta/StokesDTBPSBridge.lean` to eliminate the last stale docstring lines claiming $\{3, 4\}$ is $4_1$'s off-diagonal spectrum (it is $5_2$ from GGM §3.2 eqs. 96/98) and claiming GGM proved Conjecture 3 for $4_1$ (GGM eq. 21 is diagonal-only; Conj 3(d) is conditional for every knot including $4_1$).
   - **Verdict:** **100% of `qou-3ent`'s prose & Lean docstring correction action item is now complete** (superseding that piece of unmerged PR `#8236`); bean stays **`in-progress`** solely per Rule 13a's zero-instance guard on `class StokesDTBPSBridge`.

10. **`qou-vdvE` — *Prepare and send outreach note to Roland van der Veen on Whitehead chains*:**
    - **Status on `origin/main`:** Mathematical evaluations, SnapPy confirmations, and `computations/probes/one_loop_vdv_constant_closed_form_probe.py` landed in `5518a024e5f` and `e0ae78061d5` (port of `#8358`), and the outreach draft `docs/outreach/2026-08-08-van-der-veen-whitehead-chains-corrections.md` landed in `8a3cc3dac7d`.
    - **Verdict:** Keep **`in-progress`** per Rule 13a / outward-facing owner gate (awaits owner review & decision whether to send).

11. **`qou-8mtd` — *Lean: manifold-to-group hyperbolic volume bridge (Mostow + triangulation)*:**
    - **Status on `origin/main`:** Conditional bridge `QOU/MathlibExt/ManifoldVolumeBridge.lean` (`900295ff69c`, `b41a6f6dda7`), `QOU/Encounter/MostowTriangulationBridge.lean` (`96179f6f00f`), and `QOU/Archimedean/HyperbolicQuotient.lean` (`#6056` `7f225713a2d`) are `0-sorry` on `main` (batch PR `#8483` closed).
    - **Verdict:** Keep **`in-progress`** per Rule 13a (`HyperbolicVolumeBridge` has `0` instances; Mostow rigidity + Thurston hyperbolisation + knot-complement triangulation remain open Mathlib-scale infrastructure).

12. **`qou-eptr` — *Probe: Epstein–Penner cell decomposition for the 9-quark ³H / ³He link*:**
    - **Status on `origin/main`:** Structural scope-(a) obstruction proved/measured in `af4828e3081`, `2af417f6c45`, `f6129d4044f`, and `c902ae566f6` (port of `#8145`, `QOU/Nuclear/CanonicalCrossingsHeckeSupport.lean` + `computations/nuclear/tritium_canonical_word_obstruction.py`): `atom_canonical_crossings` carries $2A$ `averaged` Hecke letters $\tfrac12(g_k + g_k^{-1})$ outside the image of $B_n \to H_n(q)$, so link closure and Epstein–Penner decomposition are undefined on that carrier. Meanwhile `#9221` (`bdb51c4b35c` `ColourReconnectionStokesAssembly.lean` Part B) establishes a $6q$–$12q$ skew-Howe colour-reconnection carrier (`5, 42, 462` `SU(3)_c` singlets).
    - **Verdict:** Keep **`todo`** per Rule 13a (`stays open` while `b_3` / `qou-brng` remains open).

---

## Section 2 — `qou-ra4e` (`Issues-Cluster-6`): Audit of All 12 Open GitHub Issues (+ `#9154` Guard) Against `origin/main` (`e330ab6aa04`)

### 2.1 Summary Table

| Issue | Title (Abbreviated) | Linked Beans | Merged PRs & SHAs on `origin/main` (`e330ab6aa04`) | Deliverable Completion | Verdict |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **`#7710`** | Lean: KZ holonomy on $n$ points as a braid group rep (`qou-9634`) | `qou-9634` (`in-progress`) | **PR `#7719`** (`e1f5d1b4e6c` / `f93ab4b2414`), **PR `#7673`** (`69ba92de67f`), **PR `#8859`** (`e2c49449b7a`) — `QOU/Mass/KZHolonomy/` (17 modules, `0 sorry`) | **5 / 5 (`100%`)** | **100% Landed on `main` — Ready to Close** on owner OK |
| **`#7704`** | Lean: Fuchsian local theory & KZ associator for $\mathfrak{gl}_2$ (DK Step 1) | `qou-9634` / DK arc | **PR `#7706`** (`860f6dba1c2`, generalized to $\mathfrak{gl}_n$) + `f6ee5224525` (`QOU/KZ/`, 48 modules, `0 sorry`) | **4 / 4 (`100%`)** | **100% Landed on `main` — Ready to Close** on owner OK |
| **`#7703`** | Lean: oriented (HOMFLYPT) skein category $\mathsf{OS}(z,t)$ & universal property (DK Step 3) | `qou-9634` / DK arc | **PR `#7705`** (`1eeebc5f0df` — `QOU/OrientedSkein/`, 21 modules, `0 sorry`) | **4 / 4 (`100%`)** | **100% Landed on `main` — Ready to Close** on owner OK |
| **`#7092`** | Is the duality/$\sigma$ ratio a coboundary? — falsifiable form of `qou-qjhc` | `qou-qjhc` (`in-progress`, Rule 13a) | **PR `#7183`** (`caf9210bfcf`), **PR `#7273`** (`f933db58cd4`), **PR `#7290`** (`f039bf90ef2`) | **3 / 3 (`100%` of falsifiable question)** | **Core 100% Answered on `main` — Candidate Close** on owner OK (`qou-qjhc` stays open per Rule 13a) |
| **`#7942`** | Instantiate (or narrow / refute) the three $\alpha_{\mathrm{em}}$ Lean classes | `qou-adgd`, `qou-006b` | **PR `#7946`** (`823cda34561`), **PR `#9139`** (`02715c7f7f8`), **PR `#9189`** (`bdb0f07969a`), **PR `#9211`** (`cf39d247932`) | **3 / 3 classes adjudicated** (`x > 1` `qou-adgd` + §3b `qou-006b` open) | **Substantially Settled — Owner Call** (close as adjudicated vs keep open for `x > 1` `Re Li₂`) |
| `#7400` | Pole-to-cusp arc: channel-product mass, GB curvature, dead labels | `qou-bybn` (`completed`), `qou-3kni` (`todo`), `qou-2cz1` (`todo`) | **PR `#7401`** (`77695711d28`), **PR `#7546`** (`7ad18710b7a`), **PR `#7586`** (`66fab2f5de`, dead-label gate `26 → 0`) | **5.5 / 6** | **Keep Open** (residual `qou-3kni` / `qou-2cz1` broken `IM_PERTURBATION` import + `contentBlock`) |
| `#7912` | Volume conjecture and dilogarithm bricks | `qou-0yqu..8f2p` (`completed`), `qou-xblo`, `qou-1gkf` | **PRs `#8561`** (`d2e9f40e472`), **`#8763`** (`b0aa08459dd`), **`#8880`** (`732f750bc6d`), **`#8941..#8962`**, **`#9181`** (`07457bee00c`) | Bricks 1–4 + Whitehead VC landed | **Keep Open** (explicitly held open in `#9181` for Markov `#8902` + Zickert `qou-xblo`) |
| `#8979` | Why does the photon carry Markov weights $(1, 0, -1)$? | `qou-15sj`, `qou-itdn`, `qou-p49y` | **14 PRs** (`#8980..#9100` + **`#9211` `cf39d247932` `AlphaEmT35Linchpin.lean`**) | Kinematic/algebraic characterizations landed | **Keep Open** (first-principles selection of $\iota$-odd trace part `qou-15sj` + `qou-p49y` open) |
| `#8967` | Proton mass identity: which structure produces integers $2$ and $12$? | `qou-c9y8`, `qou-p12k` | **PR `#8968`** (`7e8e4731085`), **PR `#9219`** (`f5f72c1b4f0` `ContinuumECatIntraNucleonEM.lean` §2) | K1–K7 + classical $2 \times 6 = 12$ proved | **Keep Open** (link from Schur $2 \times 6 = 12$ to $-12\,m_e$ Reeb-square $k = 2$ slot unproved) |
| `#8809` | Derive the $-12\,m_e$ constant in the proton identity | `qou-p12k`, `qou-c9y8` | **PR `#8827`** (`dada9975b00`), **PR `#8804`** (`5342537fb28`), **PR `#9219`** (`f5f72c1b4f0`) | Narrowed to Reeb weight $k = 2$ (`-k²·3 = -12`) | **Keep Open** (`12` still labelled a fit per 2026-11-18 ruling pending substrate derivation of $k = 2$) |
| `#7550` | Mass endomorphism: consolidate beans, rerun bad-data, attack "mass = fibre trace" | `qou-zf9n` (`in-progress`), `qou-endo` | **PR `#8523`** (`4cbbc77101a`); **PR `#9228`** (`5978c1eb262` `ChenMultiplicativeIntegralBridge.lean`) is **`OPEN` (unmerged)** | Partial (`#8523` merged; `#9228` open) | **Keep Open** (`#9228` unmerged + 2 stale `zf9n` witnesses + T5 Molien vs Plancherel full-tower run) |
| `#6897` | Route-E follow-through: $\mathrm{Sym}^2$ gate, class 2–13 sweep, GGZ hypotheses in Lean, `categorical_mass` rename | `qou-uc6r` (`completed`), `qou-29s2`, `qou-tbmr`, `qou-0y6l` | **PR `#6898`** (`d22c609fccd`), `ObstructionClassForcesComplexType.lean`, `ObstructionH2Mathlib.lean` (`0 sorry`) | **3 / 4** (D done; A & B group-level done) | **Keep Open** (C `qou-0y6l` Gröbner/msolve wall + topological relative $H^2(M,\partial M;\mathbb{Z}/3)$ `qou-tbmr` open) |
| **`#9154`** | *(Special Guard)* Literature / BHK / `arXiv:2501.03260` ingestion tracking | Literature tracking | **PR `#9184`** (`dc8919ec7a3` `arxiv-0903.1376v1`); **`#9157`** & **`#9095`** still **`OPEN`** | Partial (`1 / 3`) | **STRICTLY KEEP OPEN** (`#9157` BHK `references.ts` & `#9095` `2501.03260` unmerged) |

### 2.2 Detailed Per-Issue Deliverable Checklists (`qou-ra4e`)

#### Group A — 100% Stated Deliverables Merged on `origin/main` (Ready to Close on Owner OK)

1. **`#7710` — *Lean: KZ holonomy on n points as a braid group representation (bean qou-9634)*:**
   - **Stated 5-step deliverables in `#7710` body — ALL 5 ON `origin/main` (`0 sorry`):**
     - Step 1 (Picard–Lindelöf / Gronwall fundamental matrix on `[0,1]`): `QOU/Mass/KZHolonomy/LinearODE.lean` (`e1f5d1b4e6c`).
     - Step 2 (Flatness $\implies$ endpoint homotopy invariance): `QOU/Mass/KZHolonomy/FlatTransport.lean` (`e1f5d1b4e6c`).
     - Step 3 (Arnold relations & infinitesimal braid relations $\implies$ KZ flatness): `QOU/Mass/KZHolonomy/GaudinCommute.lean` + `KZForm.lean` (`e1f5d1b4e6c`).
     - Step 4 (Explicit Artin generator loops & $B_n$ homomorphism `kzBraidRep`): `QOU/Mass/KZHolonomy/BraidGeometry.lean` + `BraidRep.lean` (`e1f5d1b4e6c`).
     - Step 5 ($\hbar \to 0$ continuity `kzBraidRep_zero_σ`, `continuous_kzBraidRep`): `QOU/Mass/KZHolonomy/Continuity.lean` (`e1f5d1b4e6c`).
   - **Subsequent `origin/main` extensions:** **PR `#7673`** (`69ba92de67f`) and **PR `#8859`** (`e2c49449b7a`, `22fd440d794`) added `LocalMonodromy.lean`, `Eigenvalues.lean`, `Hecke.lean`, `ArtinGenerators.lean`, `SmoothGauge.lean`, `SmoothODE.lean`, and `KohnoAssembly.lean` / `KohnoWeighted.lean` (`17` modules under `QOU/Mass/KZHolonomy/`, `0 sorry`). *(Open PR `#8148` is an optional generic-ring refactor; `#7710`'s 5-step scope is 100% on `origin/main`.)*

2. **`#7704` — *Lean: Fuchsian local theory and the KZ associator for gl₂ (Drinfeld–Kohno Step 1)*:**
   - **Stated 4-brick deliverables in `#7704` body — ALL 4 ON `origin/main` (`0 sorry`, generalized from $\mathfrak{gl}_2$ to $\mathfrak{gl}_n$ in PR `#7706` `860f6dba1c2`):**
     - Brick 1 (Fuchsian formal canonical solution at $0$ & $1$, non-resonance): `QOU/KZ/FuchsianFormal.lean`, `GLnKZ.lean`, `GLnResidues.lean`, `NonResonantInt.lean` (`960ba65b0`).
     - Brick 2 (Analytic convergence on $(0,1)$ & parameter analyticity in $\hbar$): `QOU/KZ/FuchsianConvergence.lean`, `FuchsianAnalytic.lean`, `FuchsianParam.lean` (`c4399b27b01`).
     - Brick 3 (Drinfeld KZ associator $\Phi_{\mathrm{KZ}} = G_1^{-1} G_0$, invertibility, $\Phi_{\mathrm{KZ}}(0) = 1$, duality $\Phi(B,A) = \Phi(A,B)^{-1}$): `QOU/KZ/AssociatorKZ.lean`, `DrinfeldAssociator.lean` (`0affbcb3040`).
     - Brick 4 (Hexagon & pentagon equations via 4-point KZ flatness on $\mathcal{M}_{0,5}$): `QOU/KZ/KZHexagon.lean`, `KZPentagon.lean` (`2bb13170cd0`, `860f6dba1c2`), plus `QOU/KZ/Drinfeld/` braided/ribbon quasi-bialgebra assembly (`f6ee5224525`, `48` modules total under `QOU/KZ/`, `0 sorry`).

3. **`#7703` — *Lean: oriented (HOMFLYPT) skein category OS(z,t) and its universal property (Drinfeld–Kohno Step 3)*:**
   - **Stated 4-stage deliverables in `#7703` body — ALL 4 ON `origin/main` (`0 sorry` in PR `#7705` `1eeebc5f0df` under `QOU/OrientedSkein/`, `21` modules):**
     - Stage 1 (Hecke crossing algebraic bridge): `QOU/OrientedSkein/HeckeCrossing.lean` (`442d5daa25d`).
     - Stage 2 (Abstract skein datum & $\mathfrak{gl}_n$ model datum): `SkeinDatum.lean`, `OS/Datum.lean`, `Model/GLnDatum.lean` (`9c03c0535d8`).
     - Stage 3 (Free monoidal presentation $\mathsf{OS}(z,t)$, universal property, uniqueness & non-vacuity): `OS/{Syntax,Category,Monoidal,Interpret,Unique,Universal,NonVacuity}.lean` (`4b26cec3397`, `779bd237608`).
     - Stage 4 (Markov trace / closure & $\mathfrak{gl}_n$ faithfulness): `MarkovClosure.lean`, `BraidedClosure.lean`, `Model/{GLnTrace,GLnClosure,GLnFaithful,GLnOSFaithful}.lean` (`7a70bf62336`).

#### Group B — Core / Per-Class Mandate Settled on `origin/main` (Owner Call: Close vs Keep for Narrow Residual)

4. **`#7092` — *Is the duality/σ ratio a coboundary? — the falsifiable form of qou-qjhc*:**
   - **All 3 technical requirements & the falsifiable yes/no question answered on `origin/main`:**
     - **PR `#7183`** (`caf9210bfcf`, `computations/ptolemy/ptolemy_duality_sigma_coboundary_test.py`): exact arithmetic in $K = \mathbb{Q}[T]/(f)$ across all $128$ Ptolemy coordinates — $\sigma_b$ is **YES** in $T_{\mathrm{PGL}(3)}(K)$ (irreducible $\mathrm{SL}(3)$ lift class), $\sigma_a$ is **NO**, scalar edge-ansatz is **NO**.
     - **PR `#7273`** (`f933db58cd4`): exact recovery of all 6 eliminated fixed Ptolemys as $\mu_3$ twists + sorry-free Lean `PtolemyTwist.lean` & `GaugeAnsatzNesting.lean`.
     - **PR `#7290`** (`f039bf90ef2`): variety-wide $D = \sigma_b$ across all 4 Galois conjugate points + character-level representation agreement + sorry-free Lean `GaloisOrbitTransport.lean` & `PointwiseAgreementOnReduced.lean`.
   - **Verdict:** `#7092`'s specific falsifiable question is 100% answered (`#7092` can close on owner OK while `qou-qjhc` remains `in-progress` per Rule 13a for general Ptolemy$\to$rep injectivity and classes 2–13).

5. **`#7942` — *Instantiate (or narrow / refute) the three α_em Lean classes: ArchimedeanLimit, BlochSuslinUniqueness, BringZeroModeBlochClass*:**
   - **All 3 classes adjudicated on `origin/main` (`0 sorry`):**
     - `BlochSuslinUniqueness`: original `ℝ → ℝ` class proved $\iff D = 0$ (`mass-theory/archimedean-functor-uniqueness.lean`), restated over $\mathbb{C} \setminus \{0,1\}$ in `QOU/Archimedean/BlochSuslinComplex.lean`, and **both** `BlochWignerFiveTerm` (`1473bdd2373`) and `BlochSuslinRigidity` (`6cbad1078a1`) instantiated sorry-free for `FiveTermProof.blochD` (**PR `#7946`** `823cda34561`).
     - `BringZeroModeBlochClass`: `BlochWigner_unit_circle` given its $\mathrm{Cl}_2$ body with IVT witness `BringZeroModeClausenWitness.lean`, then restated on owner card (`dc49a51dd95`, **PR `#7946`**) over algebraic Bloch–Wigner sums in `EmCouplingBringZeroMode.lean` (expected false by the Kontsevich–Zagier period conjecture, kept 0-instance per §3b-cond / `qou-006b`, while $2/(3\pi)$ itself is proved unconditionally from the $(2,4,5)$ tiling via `bringZeroMode_fully_tiling_derived` and reinforced in **`#9211` `cf39d247932` `AlphaEmT35Linchpin.lean`**).
     - `ArchimedeanLimit x`: $(0,1)$ proved (`DilogPartAConvergence.lean`); $x < -1$ refuted (`ArchimedeanLimitDomain.lean`, **PR `#7946`** `823cda34561`); $(-1,0)$ proved (`ArchimedeanLimitNegative.lean`, **PR `#9139`** `02715c7f7f8`); $x = -1$ proved (`archimedeanLimit_neg_one`), $x = 1$ refuted as stated (`not_archimedeanLimit_one`), and shifted-index $(q;q)_n$ proved (`archimedeanLimit_shifted_one`, Owner Default B1) in `ArchimedeanLimitEndpoints.lean` (**PR `#9189`** `bdb0f07969a`).
   - **Residual if kept open:** Only $x > 1$ (`Re Li₂` target restatement, `qou-adgd`) and period-conjecture-obstructed `BringZeroModeBlochClass` (`qou-006b`).

#### Group C — Keep Open (Active Residuals / Open PRs / Conjecture Gaps)

6. **`#7400` — *Pole-to-cusp arc: channel-product mass, GB curvature, dead labels*:**
   - **Landed on `origin/main` (`5.5 / 6`):** Items 1, 3, 4, 5, 6 merged in **PR `#7401`** (`77695711d28`), hop-propagation fixed in **PR `#7546`** (`7ad18710b7a`), `qou-bybn` `completed`, and dead-label gate drained `26 → 0` (`--max 0`, **PR `#7586`** `66fab2f5de` + `docs/audits/2026-10-11-retired-label-records.md`).
   - **Residual keeping `#7400` open:** `qou-3kni` (`todo`) / `qou-2cz1` (`todo`) — broken `IM_PERTURBATION` import in `snappy_cusp_seeding.py`, `channel_product_mass.py` witness `contentBlock`, and conjecture-tier GB–PL identification.

7. **`#7912` — *Volume conjecture and dilogarithm bricks*:**
   - **Landed on `origin/main`:** Bricks 1–4 + full Whitehead Reshetikhin–Turaev coloured Jones volume conjecture + Laurent polynomial + Bring route-2 $\Delta(2,4,5)$ traces merged sorry-free across **PRs `#8561`** (`d2e9f40e472`), **`#8763`** (`b0aa08459dd`), **`#8880`** (`732f750bc6d`), **`#8941`** (`f849c837fa1`), **`#8943`** (`388d8b2d6e3`), **`#8944`** (`47e6c6de3b4`), **`#8946`** (`fb78063fd11`), **`#8962`** (`79c49584753`), and **`#9181`** (`07457bee00c`), completing `qou-0yqu, qou-u1b5, qou-9r2q, qou-clx8, qou-ph1k, qou-e86p, qou-8f2p`.
   - **Residual keeping `#7912` open:** Explicitly kept open in `#9181` for Markov's theorem (`#8902`), Zickert's extended-Bloch step (`qou-xblo`), and `qou-1gkf` / `qou-r75d`.

8. **`#8979` — *Why does the photon carry Markov weights (1,0,−1)?*:**
   - **Landed on `origin/main`:** 14 PRs (`#8980` `145d4d9f57a`, `#8982` `f28245faa3b`, `#8987` `9eea870d0d3`, `#9011` `6932b7a8bc7`, `#9017` `5c74ecd3546`, `#9020` `8087b6524e8`, `#9021` `21053416340`, `#9024` `3b91b735de9`, `#9029` `e287a67d236`, `#9082` `9acb5f7ca34`, `#9088` `25efd9db273`, `#9091` `8a9e334a502`, `#9100` `5f4466b28a1`, **plus `#9211` `cf39d247932` `QOU/StandardModel/AlphaEmT35Linchpin.lean`**, which proves Diophantine $g = 4 \iff \{T(2,9), T(3,5)\}$, $(w_3, w_{21}, w_{111}) = (1, 0, -1) \iff \mathrm{t35WeightedTrace} = q^{10} - q^{-10}$, $U(1)_{\mathrm{EM}}$ Cartan inner derivation $[Q, \cdot]$, and $2\log t = -\alpha_{\mathrm{EM}}(q)$).
   - **Residual keeping `#8979` open:** First-principles derivation of *why* $\alpha_{\mathrm{em}}$ projects onto the $\iota$-odd ($\lambda \leftrightarrow \lambda'$) part of $\mathrm{tr}_M$ (`qou-15sj`, `qou-itdn` `in-progress`) and the genus-4 saturation mechanism (`qou-p49y`).

9. **`#8967` — *Proton mass identity: which structure produces the integers 2 and 12?*:**
   - **Landed on `origin/main`:** **PR `#8968`** (`7e8e4731085`, `dim W_p = 3` and K1–K7 negative sweep) and **PR `#9219`** (`f5f72c1b4f0`, `QOU/QBeta/ContinuumECatIntraNucleonEM.lean` §2 proving `schurH3_std21_mult_unique` $m = 2 = \dim S^{(2,1)}$, `proton_k_minus3_sign_schur_iff` $k = -3$ in $c_{(1^3)}(q^2) = q^{-3}[3]_q!$, and `proton_structural_integers_12` $\dim S^{(2,1)} \cdot c_{(1^3)}(1) = 2 \times 6 = 12$).
   - **Residual keeping `#8967` open:** Connecting the classical Schur product $2 \times 6 = 12$ to the $-12\,m_e$ Reeb-square slot ($k = 2$ in $-k^2 \cdot \dim W_p$) remains open; author explicitly left `#8967` open.

10. **`#8809` — *Derive the −12 m_e constant in the proton identity*:**
    - **Landed on `origin/main`:** **PR `#8827`** (`dada9975b00` `ProtonTwelveOrigin.lean`), **PR `#8804`** (`5342537fb28`), and **PR `#9219`** (`f5f72c1b4f0` `ContinuumECatIntraNucleonEM.lean`).
    - **Residual keeping `#8809` open:** Reduced on the two-term Lagrangian route to deriving scalar Reeb weight $k = 2$ (`-k² · 3 = -12`); `12` remains labelled a fit per 2026-11-18 owner ruling.

11. **`#7550` — *Mass endomorphism: consolidate beans, rerun bad-data results, attack "mass = fibre trace"*:**
    - **Landed / in-flight:** **PR `#8523`** (`4cbbc77101a`: `FibreQuantumTraceOnV3.lean`, 5 fake instances removed, `qbeta_delta_net_borromean_word_rerun_probe.py`) is on `origin/main`; W7 `ChenMultiplicativeIntegralBridge.lean` (`nablaEndo` `MassTraceIdentity` instantiation) is on **open PR `#9228`** (`5978c1eb262`, **not yet merged** to `origin/main`).
    - **Residual keeping `#7550` open:** Merging `#9228`, regenerating the two stale `zf9n` witnesses (`qou-zf9n` `in-progress`), and executing the T5 side-by-side Molien vs Plancherel full-tower run.

12. **`#6897` — *Route-E follow-through: Sym² gate, class 2–13 sweep, GGZ hypotheses in Lean, categorical_mass rename*:**
    - **Landed on `origin/main` (`3 / 4`):** Item D (`qou-uc6r` `categorical_mass` rename) is `completed`; Item A ($\mathrm{Sym}^2$ gate) settled structurally across all 13 nontrivial classes in **PR `#6898`** (`d22c609fccd`, with `qou-29s2` flavour-triple follow-up `todo`); Item B (GGZ hypotheses in Lean) closed at group-cohomology level + Mathlib `cocycles₂`/`coboundaries₂` equality in `ObstructionClassForcesComplexType.lean`, `ObstructionH2.lean`, and `ObstructionH2Mathlib.lean` (`0 sorry`).
    - **Residual keeping `#6897` open:** Item C (`qou-0y6l` `in-progress`, explicit Gröbner/msolve variety decomposition of classes 2–13 hit $> 2700$–$5400\,\mathrm{s}$ walls) and the topological relative $H^2(M, \partial M; \mathbb{Z}/3)$ identification in `qou-tbmr`.

- **Special Guard `#9154`:** **STRICTLY KEPT OPEN.** `library/arxiv-0903.1376v1` landed in **PR `#9184`** (`dc8919ec7a3`), whereas open PR `#9157` (BHK `references.ts` registration) and open PR `#9095` (`arXiv:2501.03260` ingestion) remain unmerged.

---

## Section 3 — Coordinator Action Checklist

### 3.1 Bean Transitions (`/tmp/qou-beans-latest` — Coordinator Only)
1. **Mark `completed` immediately (already 100% on `origin/main` `e330ab6aa04`):**
   - `qou-slpd` — cite **PR `#8825`** (`314ce7c5120` / `50e0af4c79a`, `QGevreyOrder.lean`, `ThetaSlopeArithmetic.lean`, `C1FormalSolutionGrowth.lean`).
2. **Mark `completed` once `origin/claude/backlog-drain-batch6-20261123` (`8bddf72a4dd`) merges:**
   - `qou-slvl` — cite `QGevreyOrder.lean:1031–1118`, `C1SeriesConvergence.lean:541–569`, and `8bddf72a4dd` (`C1ConnectionAlgebraicIdentities.lean` §6 `IsQGevreyOrderLE` + `lacunarySlopeKCoeff_orderLE_sharp`).
   - `qou-qbe9x` *(on owner OK)* — cite `05abb83e8c2` and `8bddf72a4dd` (`C1ConnectionAlgebraicIdentities.lean` §5 `torusDeg_comp_scale_eq` + `c1_third_singular_site_torusDeg_neg_one`).
3. **Owner decision (`scrapped` vs re-title under `qou-frzo`):**
   - `qou-odh5`, `qou-wgnx` — cite `QOU.MathlibExt.RSZ.c1_infinity_isoformalDim_eq_zero` (`b8bc5a41a7c`, `ee212cc3635`) + `8bddf72a4dd` (`C1ConnectionAlgebraicIdentities.lean` §§1–4).
4. **Update notes & keep open (Rule-13a / owner-gated / paused):**
   - `qou-c1ln` (`todo` `[PAUSED]`), `qou-3ent` (`in-progress`, prose + Lean docstring action item 100% done via `#7592` `65c3a99eab7` + `8bddf72a4dd`, `#9221` `bdb51c4b35c` cited), `qou-vr3q` (`todo`, `#9221` `bdb51c4b35c` cited), `qou-8vt2` (`todo`), `qou-offl` (`in-progress`, zero fitting), `qou-vdvE` (`in-progress`), `qou-8mtd` (`in-progress`), `qou-eptr` (`todo`, `c902ae566f6` + `#9221` `bdb51c4b35c` cited).

### 3.2 GitHub Issue Candidates (Owner OK Required Before Closing)
1. **Ready to close (100% stated deliverables merged on `origin/main`):**
   - **`#7710`** (merged in `#7719` `e1f5d1b4e6c` + `#7673` `69ba92de67f` + `#8859` `e2c49449b7a`)
   - **`#7704`** (merged in `#7706` `860f6dba1c2`)
   - **`#7703`** (merged in `#7705` `1eeebc5f0df`)
2. **Owner call (falsifiable question / per-class mandate settled on `origin/main`):**
   - **`#7092`** (merged in `#7183` `caf9210bfcf`, `#7273` `f933db58cd4`, `#7290` `f039bf90ef2`; `qou-qjhc` stays `in-progress`)
   - **`#7942`** (merged in `#7946` `823cda34561`, `#9139` `02715c7f7f8`, `#9189` `bdb0f07969a`, `#9211` `cf39d247932`; keep open only if tracking `x > 1` `Re Li₂` restatement `qou-adgd` on `#7942`)
3. **Keep open:** `#7400`, `#7912`, `#8979`, `#8967`, `#8809`, `#7550`, `#6897`, and guarded `#9154`.
