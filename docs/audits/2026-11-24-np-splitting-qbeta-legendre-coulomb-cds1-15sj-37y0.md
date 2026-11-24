# First-Principles Derivation & 80-dps Adjudication of Free-Neutron $Q_\beta$ and Nucleon Mass Splitting $\Delta m_{np} = m_n - m_p$ (`qou-cds1`, `qou-15sj`, `qou-37y0`)

**Date:** 2026-11-24  
**Branch:** `claude/np-splitting-qbeta-legendre-coulomb-derivation-20261124` (based on `origin/main` @ `742bffc2141`, post-`#9364` Reservoir split and post-`#9366` `ACCURACY.md`)  
**Lean 4 Formalization:** [`folio/quantum-observable-universe/lean/QOU/MassTheory/NucleonSplittingLegendreCoulomb.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/NucleonSplittingLegendreCoulomb.lean) (`0 sorry`, `0 axiom`, generic `[CommRing R]` / `[Field K]` per §7c)  
**80-dps Compute Probe & Stamped Witness:** [`computations/probes/np_splitting_qbeta_legendre_coulomb_probe.py`](../../computations/probes/np_splitting_qbeta_legendre_coulomb_probe.py) $\to$ [`computations/probes/np-splitting-qbeta-legendre-coulomb.witness.json`](../../computations/probes/np-splitting-qbeta-legendre-coulomb.witness.json) (`mp.dps = 80`, zero `float64`, evaluated at both proton and muon $q_0$ anchors)

---

## 1. Executive Summary & Honest Verdict

On `ACCURACY.md` Table 3.1a (§5.1 Priority #3), the free neutron mass $m_n$ sits at **`-486.29 ppm`** (`939.10852231 MeV` vs CODATA-2022 `939.56542194 ± 0.00000048 MeV`) because the scored Path-C nucleon splitting predicts $\Delta m_{np} = Q_\beta^{\mathrm{scored}} + m_e = 0.83643288\text{ MeV}$ against CODATA `1.29333251 ± 0.00000056 MeV` (shortfall `-0.45689963 MeV`, `-35.33%`; $Q_\beta^{\mathrm{scored}} = 0.32543393\text{ MeV}$ vs `0.78233356 MeV`, `-58.40%`).

This audit maps every existing term in $\Delta m_{np}$ symbolically over $\mathbb{Q}(q)$ and numerically at 80 decimal places across both the proton anchor ($q_p = 1.10997858275138080759166909561\dots$) and the muon anchor ($q_\mu = 1.10997859564273904668179512938\dots$), enforcing **all three quark pairs `(12, 23, 13)` symmetrically** (no `pair-13` omission) and **zero fitted parameters** (only $(m_e, q_0)$ enter; $m_{\pi^\pm}$ enters nowhere):

1. **Legendre Hamiltonian Two-Channel Sign Theorem (`hamiltonian_at_two_a2_eq`, `delta_hamiltonian_two_channel_split`):**
   Starting from the quadratic Reeb-velocity Lagrangian $L(v) = a_2 v^2 + a_1 v + a_0$ with canonical momentum $p = \partial L / \partial v = 2 a_2 v + a_1$, the Legendre transform $H_{\mathrm{can}}(p) = \frac{(p - a_1)^2}{4 a_2} - a_0$ evaluated at the unshifted kinetic momentum $p = 2 a_2$ yields
   $$H_{\mathrm{can}}(2 a_2) = a_2 - a_1 + \frac{a_1^2}{4 a_2} - a_0.$$
   Taking the neutron-minus-proton difference gives four exact algebraic channels:
   $$\Delta H_{\mathrm{can}} = \underbrace{+\Delta a_2}_{\text{strong Reeb-spin}} \;-\; \underbrace{\Delta a_1}_{\text{linear Reeb/EM}} \;+\; \underbrace{\Delta\!\left(\frac{a_1^2}{4 a_2}\right)}_{\text{diamagnetic recoil}} \;-\; \underbrace{\Delta a_0}_{\text{own-sector horizontal}}.$$
   - Unlike $L(1) = a_2 + a_1 + a_0$ (where $+a_2$ and $+a_1$ add with the same sign) and $p(1)\cdot 1 - L(1) = a_2 - a_0$ (where $a_1$ cancels identically), $H_{\mathrm{can}}(2a_2)$ flips $+a_1 \mapsto -a_1$ and $+a_0 \mapsto -a_0$.
   - Consequently, the strong isospin channel ($+\Delta a_2 > 0$, or $-\Delta a_0 = +(1 - q^{-2}) c > 0$ from the $q^{-2}$ own-sector horizontal constant on $-12 m_e$) and the repulsive intra-nucleon electromagnetic self-energy ($\Delta m_{np}^{\mathrm{EM}} = E_{\mathrm{EM}}(n) - E_{\mathrm{EM}}(p) < 0$ because proton `uud` has pairwise charge sum $0 > -1/3$ and self-charge sum $1 > 2/3$) carry **opposite signs**, matching the QCD + Cottingham structure ($\Delta m_{np} = \Delta m_{np}^{\mathrm{strong}} + \Delta m_{np}^{\mathrm{EM}}$ with $\Delta m_{np}^{\mathrm{strong}} > \Delta m_{np} > 0$ and $\Delta m_{np}^{\mathrm{EM}} < 0$).
   - **Immediate Diagnostic Consequence on `ACCURACY.md`:** Because the current `V³` base (`0.83643288 MeV`) is already *below* CODATA (`1.29333251 MeV`), adding any physically negative Cottingham electromagnetic self-energy ($\Delta m_{np}^{\mathrm{EM}} < 0$) without restoring the missing strong/Legendre channel moves $\Delta m_{np}$ *further down* away from experiment.

2. **All-3-Pairs `(12, 23, 13)` Permutation-Symmetric Charge & Borromean $V^3$ Quantum-Trace Identities (`cartan_qtrace_breaks_self_pair_degeneracy`, `eps_flavour_eq_neg_three_q_sq_sub_one_mul_deltaT_allPairs`):**
   - Keeping all three quark pairs `(12, 23, 13)` symmetrically gives $Q_{\mathrm{pair}} = Q_{12} + Q_{23} + Q_{13} = 0$ on $W_p$ (`uud`) and $-\frac{1}{3} I$ on $W_n$ (`udd`). Its **connected** Borromean $V^3$ quantum trace vanishes identically ($\Delta t_{\mathrm{conn}}(\text{all\_pairs}) = 0$), whereas its **raw** quantum trace under $\mathrm{Tr}(K^{\otimes 3} X V^3) / [2]_q^3$ satisfies the exact universal polynomial relation
     $$\varepsilon_{\mathrm{flavour}}(V^3) = -3 (q^2 - 1) \, \Delta t_{\mathrm{raw}}(\text{all\_pairs}), \qquad \Delta t_{\mathrm{raw}}(\text{all\_pairs})(q_p) = -0.110579214913254481\dots$$
   - Furthermore, whereas unweighted ($q = 1$) nucleon differences make self-charge $\sum Q_i^2$ (`2/3 - 1 = -1/3`) and pairwise charge $\sum_{i<j} Q_i Q_j$ (`-1/3 - 0 = -1/3`) degenerate (`ChargeQuadraticSumRule`), the Cartan quantum-trace weights ($q^{-1}$ on $W_n$, $q$ on $W_p$) **break that degeneracy** for all $q^2 \neq 1$:
     $$\Delta t_{\mathrm{raw}}(Q_{\mathrm{self}}, V^3) - \Delta t_{\mathrm{raw}}(Q_{\mathrm{pair}}, V^3) = -\varepsilon_{\mathrm{flavour}}(V^3) = -\frac{(q - q^{-1})\,\mathrm{tr}(V^3)}{[2]_q^3}.$$

3. **Two-Row Markov Parameter $z = q^3/(q^2+1)$ Obstruction (`qou-cds1`, `two_row_z_bar_defect_and_n2_rung`):**
   - Under the bar involution $q \mapsto q^{-1}$, $z(q^{-1}) = q^{-4} z(q)$ and $z(q) - z(q^{-1}) = q - q^{-1} = h_q$ (bar exchanges $z$ with the negative Markov stabilisation loop value $z - h_q$).
   - The sole derived higher rung is the $N = 2$ Kashiwara/Hoefsmit factor $1 - b^2 \hbar_q^4 = 1 - \frac{[3]_q}{[2]_q^2} \hbar_q^4 = 0.9999274568\dots$ (`-72.54 ppm`). Because $\cos(\alpha - u/2) \le 1$ for every real phase $\alpha$ while closing $Q_\beta^{\mathrm{CODATA}} / Q_\beta^{\mathrm{scored}}$ requires $F_{\mathrm{req}} = \mathbf{2.4039704844 > 1}$ (and $1.75923699 > 1$ on the $\Delta_S$ two-row trace), **no real-phase $c_k$ cosine ladder can close $Q_\beta$**.

4. **Post-`#9360` Derived Form-B $\alpha_{\mathrm{EM}}(q_0)$ Intra-Nucleon Coulomb Scale (`qou-15sj`, `qou-37y0`):**
   - Using the parameter-free 1-loop Schwinger Form-B coupling $\alpha_{\mathrm{EM}}^{\mathrm{FormB}}(q_p)^{-1} = 137.0359991269509\dots$ (`-0.3652 ppb`, derived in `EmFermionLoopFourTopology` PR `#9360`) and $m_p(q_p) = 938.2720894273\text{ MeV}$ (zero $m_\pi$ input, all 3 pairs kept):
     - **Borromean $V^3$ all-pairs quantum trace (`E07`):** $\alpha_{\mathrm{EM}}^{\mathrm{FormB}}(q_p)\, m_p(q_p)\, \Delta t_{\mathrm{raw}}(\text{all\_pairs}) = \mathbf{-0.7571250743\text{ MeV}}$ (implied $\Delta m_{np}^{\mathrm{strong}} = +2.05045758\text{ MeV}$).
     - **Constituent Compton `1/9` (`E05`):** $-\frac{1}{9} \alpha_{\mathrm{EM}}^{\mathrm{FormB}}(q_p)\, m_p(q_p) = \mathbf{-0.7607669156\text{ MeV}}$ (implied $\Delta m_{np}^{\mathrm{strong}} = +2.05409943\text{ MeV}$; Legendre recoil $+\frac{a_{1,n}^2}{4 a_{2,n}} = +0.1542\text{ keV}$).
     Both match standard Cottingham QED evaluations (`-0.76 ± 0.30 MeV`; BMW lattice QED `-1.00 ± 0.16 MeV`) in both sign and magnitude with zero new coupling constants.

5. **120-Cell Pre-Committed Zero-Parameter Operator Catalog & CODATA Entropy Audit:**
   - Evaluating all $N_{\mathrm{total}} = 10 \times 12 = 120$ combinations $(\Delta m_{np}^{\mathrm{strong}}, \Delta m_{np}^{\mathrm{EM}})$ consumes $\log_{10}(120) = 2.0792\text{ digits}$ of look-elsewhere entropy, requiring $|\delta \Delta m_{np} / \Delta m_{np}| \le \frac{1}{20 \times 120} = 416.67\text{ ppm}$ to clear even a **1-net-digit** non-coincidence bar.
   - **Honest Negative Result:** **0 of 120 combinations** pass the 1-digit CODATA entropy bar (`best live cell = -1278.07 ppm`, `best first-principles cell = +1818.08 ppm` carrying only `0.360` net digits). Combining the Legendre own-sector horizontal shift $+\Delta_{\mathrm{horiz}} = (1 - q_p^{-2}) \cdot 12 m_e = +1.15493681\text{ MeV}$ with the Borromean `V³` trace (`+0.83643288 MeV` $\to$ `S04 = +1.99136969 MeV`) and the Borromean all-pairs Coulomb self-energy (`E07 = -0.75712507 MeV`) yields $\Delta m_{np} = \mathbf{1.23424461\text{ MeV}}$ (`-4.57%`, reducing the raw `ACCURACY.md` shortfall nearly $8\times$ from `-0.4569 MeV` to `-0.0591 MeV`), but **does not close** `1.29333251 MeV`. Nothing is fitted and `ACCURACY.md` is left untouched pending a first-principles derivation of the strong/spatial normalization kernel.

---

## 2. Complete 80-dps Map of Existing & Derived Terms (`proton` vs `muon` Anchors)

All values below are reproduced from `computations/probes/np-splitting-qbeta-legendre-coulomb.witness.json` (`mp.dps = 80`):

| Quantity / Term | Algebraic Expression | Proton Anchor ($q_p$) | Muon Anchor ($q_\mu$) | Status / Physical Role |
|---|---|---|---|---|
| Substrate $q_0$ | $q_{\mathrm{at}}(80)$ / $q_{\mu,\mathrm{at}}(80)$ | `1.109978582751380808` | `1.109978595642739047` | Cross-anchor $\Delta q_0 / q_0 = +11.61\text{ ppb}$ |
| Derived Form-B $\alpha_{\mathrm{EM}}^{-1}(q_0)$ | Cubic w/ 4-topology $(1 - h_q^2 \alpha)$ (`#9360`) | `137.035999126950912` | `137.036010002595537` | `-0.3652 ppb` at $q_p$ (`qou-15sj` closed) |
| Order-zero $E_0^{\mathrm{ord0}}$ | $m_e / (q_0 (q_0 - 1))$ | `4.185981363294476 MeV` | `4.185980824010171 MeV` | Bare $q$-Lagrangian hadronic scale |
| Tower-summed $E_0^{\mathrm{twr}}$ | $E_0^{\mathrm{ord0}} / (1 - \hbar_q^2)$ | `4.227483355629031 MeV` | `4.227482819850350 MeV` | Canonical `qbeta_e0` scale (`+0.9915%`) |
| Borromean flavour trace $\varepsilon_{\mathrm{flavour}}(V^3)$ | $-(q^2 - 1) P_{\mathrm{Bor}}(q) / (q^4 (q^2 + 1)^3)$ | `+0.076980534601364` | `+0.076980542854938` | Equal to $-3(q^2 - 1)\,\Delta t_{\mathrm{raw}}(\text{all\_pairs})$ |
| Scored $Q_\beta^{\mathrm{scored}}$ | $|\varepsilon_{\mathrm{flavour}}(V^3)| \cdot E_0^{\mathrm{twr}}$ | `0.325433928734692 MeV` | `0.325433922382005 MeV` | `-58.40%` vs CODATA `0.78233356 MeV` |
| Scored $\Delta m_{np}^{\mathrm{scored}}$ (`S01`) | $Q_\beta^{\mathrm{scored}} + m_e$ | `0.836432879424692 MeV` | `0.836432873072005 MeV` | `-35.33%` vs CODATA `1.29333251 MeV` |
| All-3-pairs `V³` connected QED (`E01`) | $m_e \, \Delta t_{\mathrm{conn}}(Q_{12}+Q_{23}+Q_{13}, V^3)$ | `0` (exact) | `0` (exact) | `deltaT_allPairs_connected_eq_zero` |
| All-3-pairs `V³` raw QED at $m_e$ (`E02`) | $m_e \, \Delta t_{\mathrm{raw}}(Q_{12}+Q_{23}+Q_{13}, V^3)$ | `-0.056505862788797 MeV` | `-0.056505861878470 MeV` | Electronic scale; $13.4\times$ below Cottingham |
| Adjacent `(12, 23)` connected QED | $-m_e \, \Delta t_{\mathrm{conn}}(Q_{12}+Q_{23}, V^3)$ | `-0.000127224301334 MeV` | `-0.000127224358863 MeV` | Drops pair `(1,3)`; non-covariant (`#8552`) |
| All-3-pairs `V³` $\alpha_{\mathrm{EM}} m_p$ (`E07`) | $\alpha_{\mathrm{EM}}^{\mathrm{FormB}}(q_0) m_p(q_0) \Delta t_{\mathrm{raw}}(\text{all\_pairs})$ | `-0.757125074322804 MeV` | `-0.757124817404590 MeV` | Matches Cottingham `-0.76 ± 0.30 MeV` |
| Constituent Compton `1/9` (`E05`) | $-\frac{1}{9} \alpha_{\mathrm{EM}}^{\mathrm{FormB}}(q_0) m_p(q_0)$ | `-0.760766915591528 MeV` | `-0.760766669693707 MeV` | Implies $\Delta m_{np}^{\mathrm{strong}} = +2.05410\text{ MeV}$ |
| Legendre recoil $\Delta(a_1^2 / (4 a_2))$ | $a_{1,n}^2 / (2 m_p(q_0))$ at $a_{1,n} = \frac{1}{9}\alpha_{\mathrm{EM}} m_p$ | `+0.000154203121549 MeV` | `+0.000154203059482 MeV` | Second-order diamagnetic recoil (`+0.154 keV`) |
| Legendre own-sector horizontal (`S03`) | $(1 - q_0^{-2}) \cdot 12 m_e$ | `+1.154936806625984 MeV` | `+1.154936922233514 MeV` | $-\Delta a_0$ from proton's $-12 m_e$ constant |
| Two-row $N=2$ ladder factor (`qou-cds1`) | $1 - ([3]_q / [2]_q^2) \hbar_q^4$ | `0.999927456834648` | `0.999927456816748` | `-72.54 ppm` (`< 1`, vs $F_{\mathrm{req}} = 2.4040$) |

---

## 3. Pre-Committed $10 \times 12 = 120$ Zero-Parameter Catalog & Entropy Bounds

With $N_{\mathrm{strong}} = 10$ canonical strong/kinematic candidates and $N_{\mathrm{EM}} = 12$ all-3-pairs symmetric electromagnetic candidates ($N_{\mathrm{total}} = 120$), the discrete look-elsewhere entropy is $\log_{10}(120) = 2.07918\text{ digits}$, setting the **1-net-digit CODATA threshold** at $|\delta \Delta m_{np} / \Delta m_{np}| \le 416.67\text{ ppm}$ (`0.0417%`).

### Top Ranked Cells & Physical Cottingham Pair (Proton Anchor $q_p$)

| Rank | Strong Channel $S_i$ | All-Pairs EM Channel $E_j$ | $\Delta m_{\mathrm{strong}}$ (MeV) | $\Delta m_{\mathrm{EM}}$ (MeV) | $\Delta m_{\mathrm{pred}}$ (MeV) | Residual (ppm) | Net Digits | Verdict |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `S10` (retired $z=1$ counit) | `E01` ($0$, conn. all-pairs) | `+1.294645` | `0` | `1.294645` | `+1014.6` | `+0.613` | Excluded by $z = q^3/(q^2+1)$ ruling + `< 1` net digit |
| 2 | `S07` (skein Cayley ansatz) | `E01` ($0$, conn. all-pairs) | `+1.291680` | `0` | `1.291680` | `-1278.1` | `+0.513` | Conjectural `conj:flavor-split-substrate-mass`; wrong sign for $\Delta m_{\mathrm{EM}} < 0$ |
| 3 | `S09` ($(1-q^{-2}) E_0^{\mathrm{ord0}} + m_e$) | `E12` ($-\alpha_{\mathrm{EM}} m_e$) | `+1.299413` | `-0.003729` | `1.295684` | `+1818.1` | `+0.360` | Best first-principles hit, but `< 1` net digit (`4193 σ_exp`) |
| — | `S04` (`V³` + Legendre $12 m_e$) | `E07` ($\alpha_{\mathrm{EM}} m_p \Delta t_{\mathrm{raw}}$) | `+1.991370` | `-0.757125` | `1.234245` | `-45686.5` | `< 0` | Reproduces both QCD (`+1.99 MeV`) & QED (`-0.76 MeV`) scales; `-59.1 keV` open gap |
| — | `S04` (`V³` + Legendre $12 m_e$) | `E05` ($-\frac{1}{9}\alpha_{\mathrm{EM}} m_p$) | `+1.991370` | `-0.760767` | `1.230603` | `-48502.3` | `< 0` | Constituent `1/9` Cottingham pair; `-62.7 keV` open gap |

---

## 4. Per-Bean Disposition Summary

- **`qou-15sj` (completed in PR `#9211` / upgraded in PR `#9360`):** Verified and integrated at 80 dps; the 4-topology `EmFermionLoopFourTopology` Form-B $\alpha_{\mathrm{EM}}(q_0)$ removes the historical free electromagnetic coupling input $k$ at the coupling level.
- **`qou-cds1` (`Refs qou-cds1` — remains open):** Formalized `two_row_z_bar_defect_and_n2_rung` in `QOU.MassTheory.NucleonSplittingLegendreCoulomb` and verified at 80 dps that $F_{\mathrm{req}} = 2.4039704844 > 1$ on the `V³` base excludes every real-phase cosine ladder on `z = q^3/(q^2+1)`.
- **`qou-37y0` (`Refs qou-37y0` — remains open on spatial kernel):** Formalized the Legendre two-channel sign flip, Cartan quantum-trace breaking of the self-vs-pair charge degeneracy, universal $\varepsilon_{\mathrm{flavour}}(V^3) = -3(q^2 - 1)\Delta t_{\mathrm{raw}}(\text{all\_pairs})$ relation, and `§3b-cond` two-channel Cottingham decomposition; quantified the exact `-59.1 keV` (`-4.57%`) remaining gap when combining `S04 + E07` without spatial-kernel fitting.
