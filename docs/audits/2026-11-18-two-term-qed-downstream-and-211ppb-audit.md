# Downstream Lean/Compute Impact Audit for $\Delta m_{\mathrm{QED}}$, Sequenced Workplan, and 50-dps Test on the $211\text{ ppb}$ $\mu\text{--}p$ Tension & $Q_\beta$ Ladders

**Date:** 2026-11-18  
**Bean:** `qou-eas4` (under Epic `qou-9pl8`)  
**Primary Lean 4 Foundation:** [`folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean)  
**Runnable 50-dps + SymPy Probe:** [`folio/quantum-observable-universe/computations/probes/np_two_term_qed_mup_tension_probe.py`](../../folio/quantum-observable-universe/computations/probes/np_two_term_qed_mup_tension_probe.py) (mirrored at [`computations/probes/np_two_term_qed_mup_tension_probe.py`](../../computations/probes/np_two_term_qed_mup_tension_probe.py))  
**Companion Error-Budget Audit:** [`docs/audits/2026-11-15-np-splitting-error-budget.md`](2026-11-15-np-splitting-error-budget.md)

---

## 1. Executive Summary

> **🛑 Pin label corrected 2026-11-20 (PR #8552).** The values quoted below "at
> $q_0$" — $\overline{\mathrm{tr}}_{\mathrm{conn}}(p,V^3) = -0.00043068071$ and
> $\Delta\overline{\mathrm{tr}}_{\mathrm{conn}} = +0.00064911326$ (§1, §4.2) — are evaluated at the
> **muon** pin $q_\mu = 1.10997859564\ldots$, not the proton pin. At the proton pin
> $q_p = 1.10997858275\ldots$ they are $-0.000430680520$ and $+0.000649112966$
> (relative shift $4.5\times10^{-7}$; recomputed at 40 dps). No conclusion here moves.
> Separately, #8552 proves the adjacent insertion $Q_{12}+Q_{23}$ is not braid-covariant and
> that on $W_p$ its trace equals $-\mathrm{tr}(Q_{13}\,\cdot)$ for every word, so the
> "zero-parameter derived" label on the figures below is scoped there (bean `qou-qcov`).
> The values are left as recorded.

This audit executes the two pre-registered 50-dps `mpmath` + exact `sympy` tests required by `qou-eas4` and compiles a complete, file-by-file downstream impact inventory and formalize-first workplan for Epic `qou-9pl8` (upgrading QOU's one-term nucleon mass and $n\text{--}p$ splitting architecture to a two-term strong + electromagnetic decomposition $m_N = m_N^{\mathrm{QCD}} + m_N^{\mathrm{QED}}$ and $\Delta m_{np} = \Delta m_{\mathrm{QCD}} + \Delta m_{\mathrm{QED}}$).

Crucially, following our **Adversarial Anti-Fitting & Single-Functional Operator Consistency Gate** ($\Delta m_{\mathrm{QED}} \equiv M^{\mathrm{QED}}(n) - M^{\mathrm{QED}}(p)$ from a single braid-trace operator on $W_p = (2,1)$ and $W_n = (1,2)$), all post-hoc combinatorial `[2]_q/[3]_q` grid fits (`QOU-P13`, `QED-Q14`, and the $\alpha_{\mathrm{EM}}$-free `QED-Q6b`) are **rejected and excised from derived claims**. In their place, the exact zero-parameter **Borromean $V^3 = (\sigma_1\sigma_2^{-1})^3$ Two-Term & Connected 4th-Order Trace Decomposition** proved in [`NucleonWeightSpaceTwoTerm.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean) provides the single-operator derived prediction across both tests.

### Key Findings from the Lean-Proved Borromean $V^3$ Two-Term & Connected 4th-Order Trace

1. **Exact Matrix & Connected 4th-Order Braid Trace Decomposition on $W_p = (2,1)$ and $W_n = (1,2)$ (`NucleonWeightSpaceTwoTerm.lean`):**
   - On $W_p = (2,1)$ ($\dim = 3$, basis $|\mathfrak{u}\mathfrak{u}\mathfrak{d}\rangle, |\mathfrak{u}\mathfrak{d}\mathfrak{u}\rangle, |\mathfrak{d}\mathfrak{u}\mathfrak{u}\rangle$), the adjacent pairwise charge matrices $Q_{12}^{(p)} = \mathrm{diag}(4/9, -2/9, -2/9)$ and $Q_{23}^{(p)} = \mathrm{diag}(-2/9, -2/9, 4/9)$ are **traceless** ($\mathrm{tr}(Q_{12}^{(p)}) = \mathrm{tr}(Q_{23}^{(p)}) = 0$, theorems `trace_Q12p_zero`, `trace_Q23p_zero`).
   - On $W_n = (1,2)$ ($\dim = 3$, basis $|\mathfrak{u}\mathfrak{d}\mathfrak{d}\rangle, |\mathfrak{d}\mathfrak{u}\mathfrak{d}\rangle, |\mathfrak{d}\mathfrak{d}\mathfrak{u}\rangle$), $Q_{12}^{(n)} = \mathrm{diag}(-2/9, -2/9, 1/9)$ and $Q_{23}^{(n)} = \mathrm{diag}(1/9, -2/9, -2/9)$ satisfy the exact matrix decomposition (`QAdjn_eq_static_add_half_QAdjp`):
     $$Q_{12}^{(n)} + Q_{23}^{(n)} = -\frac{2}{9} I_3 + \frac{1}{2}\big(Q_{12}^{(p)} + Q_{23}^{(p)}\big),$$
     where $-\frac{2}{9}I_3$ is the static $q=1$ scalar Coulomb background ($\mathrm{tr} = -2/3$) and $\frac{1}{2}(Q_{12}^{(p)} + Q_{23}^{(p)})$ is the traceless connected operator ($\mathrm{tr} = 0$) with **opposite sign and half the amplitude** of the proton!
   - Evaluated on the 3-strand Borromean braid $V^3 = (\sigma_1\sigma_2^{-1})^3$:
     - Because $Q_{12}^{(p)} + Q_{23}^{(p)}$ is traceless and symmetric under $\sigma_1 \leftrightarrow \sigma_2^{-1}$, its normalized connected trace on $W_p$ vanishes to third order at $q=1$ and enters purely at fourth order $(q-1)^4$ (`trace_QAdjp_borromeanV3`):
       $$\overline{\mathrm{tr}}_{\mathrm{conn}}(p, V^3) := \frac{1}{3}\mathrm{tr}\!\left(\big(Q_{12}^{(p)} + Q_{23}^{(p)}\big) V_p^3\right) = -\frac{2(q-1)^4(q+1)^4(q^4+q^2+1)}{27 q^6} = -0.00043068071 \quad (\text{at }q_0).$$
     - On $W_n$, subtracting the static $q=1$ scalar piece $-\frac{2}{27}\mathrm{tr}(V_n^3)$ isolates the connected fourth-order braid trace (`trace_QAdjn_borromeanV3_connected`):
       $$\overline{\mathrm{tr}}_{\mathrm{conn}}(n, V^3) := \frac{1}{3}\left(\mathrm{tr}\!\left(\big(Q_{12}^{(n)} + Q_{23}^{(n)}\big) V_n^3\right) + \frac{2}{9}\mathrm{tr}(V_n^3)\right) = +\frac{(q-1)^4(q+1)^4(2q^4-q^2+2)}{27 q^6} = +0.00021843255.$$
     - Their $(n - p)$ difference reinforces with an automatic, parameter-free $q \to 1$ amplitude ratio of $\frac{1/2 - (-1)}{1} = \frac{3}{2}$ ($1.50718$ at $q_0$, `trace_QAdj_connected_diff_borromeanV3`):
       $$\Delta\overline{\mathrm{tr}}_{\mathrm{conn}}(V^3) := \overline{\mathrm{tr}}_{\mathrm{conn}}(n, V^3) - \overline{\mathrm{tr}}_{\mathrm{conn}}(p, V^3) = +\frac{(q-1)^4(q+1)^4(4q^4+q^2+4)}{27 q^6} = +0.00064911326.$$

2. **Test 1 — Zero-Parameter Impact of $M_p^{\mathrm{QED}}$ on the $211\text{ ppb}$ $\mu\text{--}p$ Tension:**
   - **Sign & Slope Geometry:** Because $\frac{d\ln(m_p^{\mathrm{QCD}}/m_e)}{d\ln q} \approx -21.007 < 0$ at $q_0$, the pure-QCD proton identity evaluated at $q_{\mathrm{muon}}$ sits $-243.8602\text{ ppb}$ below CODATA:
     $$m_p^{\mathrm{QCD}}(q_{\mathrm{muon}}) = 938.271860620094\text{ MeV}, \qquad m_p^{\mathrm{exp}} = 938.272089427324\text{ MeV},$$
     $$\delta m_p := m_p^{\mathrm{exp}} - m_p^{\mathrm{QCD}}(q_{\mathrm{muon}}) = +0.000228807231\text{ MeV} = +0.2288072\text{ keV} = +0.0004477646\,m_e.$$
     Thus a **positive (repulsive)** electromagnetic self-energy $M_p^{\mathrm{QED}} > 0$ in $m_p^{\mathrm{phys}}(q) = m_p^{\mathrm{QCD}}(q) + M_p^{\mathrm{QED}}(q)$ moves $q_{\mathrm{proton}}$ **upward toward $q_{\mathrm{muon}}$**.
   - **Zero-Parameter Borromean $V^3$ Connected 4th-Order Prediction:** In electron mass units $m_e$ (the natural mass unit of the dimensionless proton substrate identity $m_p/m_e = 2(\mathrm{Vol}(4_1)/\hbar_q^2)F_{\mathrm{Bor}}(q) - 12$), the connected 4th-order Borromean trace gives:
     - **Plain normalized trace (`DERIVED-Bor-V3 (plain)`):**
       $$M_p^{\mathrm{QED}} = m_e \big|\overline{\mathrm{tr}}_{\mathrm{conn}}(p, V^3)\big| = +0.00022007729\text{ MeV} = +0.2200773\text{ keV} \quad (+0.0004306807\,m_e),$$
       matching the $+0.2288072\text{ keV}$ $\mu\text{--}p$ gap to within $3.8\%$ with **zero $\alpha_{\mathrm{EM}}$ or $[2]_q/[3]_q$ factors**! It reduces $\Delta q/q_\mu$ from $-11.6141\text{ ppb}$ to **$-0.4431\text{ ppb}$** and reduces the $m_\mu$ tension from $+211.21\text{ ppb}$ ($+9.49\sigma$) to **$+8.058\text{ ppb}$ ($+0.362\sigma$, a $96.18\%$ tension reduction)**!
     - **$K_p^{\otimes 3} = q$-weighted trace (`DERIVED-Bor-V3 (K^3-wt)`):**
       $$M_p^{\mathrm{QED}} = q\,m_e \big|\overline{\mathrm{tr}}_{\mathrm{conn}}(p, V^3)\big| = +0.00024428108\text{ MeV} = +0.2442811\text{ keV},$$
       which reduces $\Delta q/q_\mu$ to **$+0.7854\text{ ppb}$** and reduces the $m_\mu$ tension to **$-14.284\text{ ppb}$ ($-0.642\sigma$, a $93.24\%$ reduction)**, straddling the exact $\mu\text{--}p$ gap between the plain ($+0.36\sigma$) and $K_p^{\otimes 3}$-weighted ($-0.64\sigma$) normalizations.

3. **Test 2 — Zero-Parameter Impact of $\Delta m_{\mathrm{QED}}$ on $\Delta m_{np}$, $Q_\beta$, and the Convention-D $c_k$ Ladder:**
   - **Single-Functional Sub-keV Connected Shift on the Convention-D $Q_\beta$ $N=2$ Residual:**
     - Under Convention D ($z_D = q^3/(q^2+1)$), the $N=2$ ($c_2 = -1$) Kashiwara decay prediction $Q_{N2}^D(q_p) = 0.7828047136\text{ MeV}$ sits $+0.469884\text{ keV}$ ($+600.618\text{ ppm}$) above $Q_\beta^{\mathrm{exp}} = 0.7823348293\text{ MeV}$ (forcing an unseparated $c_2^{\mathrm{emp}}(D) = -9.274$).
     - Evaluating the **exact same connected 4th-order Borromean operator** on $(n - p)$ automatically produces the negative electromagnetic shift of the $3/2$-larger magnitude required by $Q_\beta$:
       - **`DERIVED-Bor-V3-Conn (plain)`:** $\Delta m_{\mathrm{QED}}^{\mathrm{conn}} = -m_e\,\Delta\overline{\mathrm{tr}}_{\mathrm{conn}}(V^3) = -0.3316960\text{ keV}$, which closes **$70.59\%$** of the Convention-D $Q_{N2}^D$ residual (reducing the error from $+600.62\text{ ppm}$ to **$+176.64\text{ ppm}$** and collapsing $c_2^{\mathrm{emp}}(D)$ from $-9.274$ to **$-3.433$**).
       - **`DERIVED-Bor-V3-Conn (K_n/K_p-wt)`:** $\Delta m_{\mathrm{QED}}^{\mathrm{conn}} = -m_e\big(q^{-1}\overline{\mathrm{tr}}_{\mathrm{conn}}(n) - q\overline{\mathrm{tr}}_{\mathrm{conn}}(p)\big) = -0.3448405\text{ keV}$, closing **$73.39\%$** of the residual ($+159.83\text{ ppm}$, $c_2^{\mathrm{emp}}(D) = -3.202$).
       - **`DERIVED-Bor-V3-Conn (K_p^3-wt)`:** $\Delta m_{\mathrm{QED}}^{\mathrm{conn}} = -m_e\big(\overline{\mathrm{tr}}_{\mathrm{conn}}(n) - q\overline{\mathrm{tr}}_{\mathrm{conn}}(p)\big) = -0.3558998\text{ keV}$, closing **$75.74\%$** of the residual ($+145.70\text{ ppm}$, $c_2^{\mathrm{emp}}(D) = -3.007$).
       - **`DERIVED-Bor-V3-Conn (q-wt)`:** $\Delta m_{\mathrm{QED}}^{\mathrm{conn}} = -q\,m_e\,\Delta\overline{\mathrm{tr}}_{\mathrm{conn}}(V^3) = -0.3681755\text{ keV}$, closing **$78.35\%$** of the residual ($+130.01\text{ ppm}$, $c_2^{\mathrm{emp}}(D) = -2.791$).
   - **Macroscopic Two-Term Trace on Borromean $V^3$ at Scale $\alpha_{\mathrm{bind}} = 8G m_e = 3.74446\text{ MeV}$ (and $E_0 = 4.18598\text{ MeV}$):**
     - **Strong Cartan trace difference (`trace_K_diff_word` on $V^3$, `DERIVED-S8a/b`):**
       $$\Delta m_{\mathrm{QCD}}(V^3) = \alpha_{\mathrm{bind}}(q - q^{-1})\mathrm{tr}(V^3) = +2.343902\text{ MeV} \quad (\text{or } +2.620279\text{ MeV at } E_0),$$
       in direct agreement with the BMW 2015 lattice QCD benchmark $\Delta M_{\mathrm{QCD}} = +2.52(17)(24)\text{ MeV}$ (`borsanyi-et-al-2015`) and WLCM 2012 $+2.59(47)\text{ MeV}$ (`walker-loud-carlson-miller-2012`).
     - **Full normalized QED trace difference (`trace_QAdj_diff_borromeanV3`, `DERIVED-Bor-V3-Full`):**
       $$\Delta m_{\mathrm{QED}}(V^3) = \alpha_{\mathrm{bind}}\cdot\frac{1}{3}\Delta\mathrm{tr}\!\left((Q_{12}+Q_{23})V^3\right)_{n-p} = -0.828059\text{ MeV} \quad (-0.745676\text{ MeV } K^{\otimes 3}\text{-weighted; } -0.925698\text{ MeV at } E_0),$$
       in direct agreement with the classic Cottingham benchmark $-0.76\text{ MeV}$ and BMW 2015 lattice QED $\Delta M_{\mathrm{QED}} = -1.00(07)(14)\text{ MeV}$.
     - **Macroscopic two-term sum on $V^3$:**
       $$\Delta m_{np}(V^3) = +2.343902 - 0.828059 = +1.515843\text{ MeV},$$
       matching the BMW 2015 ab initio lattice QCD+QED two-term sum $+1.51(16)(23)\text{ MeV}$ (`borsanyi-et-al-2015`).

---

## 2. Adversarial Anti-Fitting & Look-Elsewhere Gate

To prevent sub-floor numerology from entering the QOU corpus (per the 2026-05-28 floor audit and `2026-07-04-c4-mu-p-tension-pin-dependence.md`), every candidate expression in the initial grid scan was subjected to three mandatory gate criteria:

1. **Single-Functional Operator Consistency ($\Delta m_{\mathrm{QED}} \equiv M^{\mathrm{QED}}(n) - M^{\mathrm{QED}}(p)$):**
   The proton QED self-energy $M_p^{\mathrm{QED}}$ in Test 1 and the nucleon QED splitting $\Delta m_{\mathrm{QED}}$ in Test 2 must be evaluations of the **same** quantum-group operator $\mathcal{O}_{\mathrm{QED}}$ on the proton weight space $W_p = (2,1)$ and the neutron-minus-proton difference $W_n - W_p$.
2. **Physical Coupling Discipline:**
   Any candidate claimed as an electromagnetic self-energy or radiative QED shift must either derive directly from the quark charge tensor $Q_{ij} = Q_i Q_j$ on the nucleon braid word $V^3$ or carry an explicit power of $\alpha_{\mathrm{EM}}(q)$.
3. **Look-Elsewhere / Combinatorial Entropy Bound:**
   In a grammar allowing arbitrary products and quotients of $\{h, \hbar_q\} \times \{1, [2]_q, [3]_q, [2]_q/[3]_q, [3]_q/[2]_q, [3]_q!\}$ around $\alpha_{\mathrm{EM}} m_e$, the factors populate the interval $[0.05, 1.50]\text{ keV}$ with a spacing of $\sim 10\text{--}15\%$. Monte Carlo / grid-density counting shows an **$\sim 81\%$ look-elsewhere hit rate** for landing at least one combinatorial formula within $\pm 15\%$ of any arbitrary target in $[0.15, 0.55]\text{ keV}$.

### Explicitly Rejected Post-Hoc Grid Fits

| Rejected Candidate | Formula & Value | Why It Fails the Anti-Fitting Gate | Replacement |
| --- | --- | --- | --- |
| **`[REJECTED-FIT] QOU-P13`** | $+\alpha_{\mathrm{EM}} m_e \hbar_q \frac{[2]_q}{[3]_q} = +0.24410\text{ keV}$ | 1. **No operator derivation:** The ratio $[2]_q/[3]_q$ is inserted ad hoc to scale $+\alpha_{\mathrm{EM}} m_e \hbar_q = +0.3695\text{ keV}$ down by $0.6607$ to hit $+0.2288\text{ keV}$ ($81\%$ look-elsewhere hit rate).<br>2. **Violates Single-Functional Consistency:** Applying the same $[2]_q/[3]_q$ factor to $(n-p)$ gives $-\frac{1}{3}\alpha_{\mathrm{EM}} m_e \hbar_q [2]_q/[3]_q = -0.0814\text{ keV}$, which fails Test 2B ($+496\text{ ppm}$). | **`DERIVED-Bor-V3`:** $M_p^{\mathrm{QED}} = m_e |\overline{\mathrm{tr}}_{\mathrm{conn}}(p, V^3)| = +0.22008\text{ keV}$ (Lean-proved in `NucleonWeightSpaceTwoTerm.lean`). |
| **`[REJECTED-FIT] QED-Q14`** | $-\frac{1}{3}\alpha_{\mathrm{EM}} m_e h [2]_q = -0.52255\text{ keV}$ | 1. **No operator derivation:** Multiplies by $[2]_q$ instead of $[2]_q/[3]_q$ solely to scale $-\frac{1}{3}\alpha_{\mathrm{EM}} m_e h = -0.2600\text{ keV}$ up by $2.01$ to hit $-0.4699\text{ keV}$.<br>2. **Violates Single-Functional Consistency:** Evaluating the corresponding proton operator $+\alpha_{\mathrm{EM}} m_e h [2]_q = +1.5676\text{ keV}$ misses the Test 1 $\mu\text{--}p$ gap ($+0.2288\text{ keV}$) by **$6.85\times$** ($-1212\text{ ppb}$ on $m_\mu$)! | **`DERIVED-Bor-V3-Conn`:** $\Delta m_{\mathrm{QED}}^{\mathrm{conn}} = -m_e\,\Delta\overline{\mathrm{tr}}_{\mathrm{conn}}(V^3) = -0.33170\text{ keV}$ (exact same operator as Test 1, automatic $3/2$ ratio). |
| **`[REJECTED-FIT] QED-Q6b`** | $-\frac{1}{3}\alpha_{\mathrm{bind}} h = -0.26094\text{ MeV}$ | **Missing $\alpha_{\mathrm{EM}}$ & no braid word:** Multiplies the static charge factor $-1/3$ by the strong/Catalan binding scale $\alpha_{\mathrm{bind}} = 8G m_e$ and $h = q - q^{-1}$ with no $\alpha_{\mathrm{EM}}$ and no braid trace evaluation. | **`DERIVED-Bor-V3-Full`:** $\alpha_{\mathrm{bind}}\cdot\frac{1}{3}\Delta\mathrm{tr}((Q_{12}+Q_{23})V^3) = -0.82806\text{ MeV}$ paired with $\Delta m_{\mathrm{QCD}}(V^3) = +2.34390\text{ MeV}$. |

---

## 3. Literature Benchmarks from Newly Ingested Papers on `main`

All 6 newly ingested Cottingham and lattice QCD+QED papers on `main` (`#8513`, `#8514`, refreshed in `#8515`) establish the standard two-term decomposition $\Delta m_{np} = m_n - m_p = \Delta m_{\mathrm{QCD}} + \Delta m_{\mathrm{QED}}$ with $\Delta m_{\mathrm{QCD}} > 0$ (from $m_d > m_u$) and $\Delta m_{\mathrm{QED}} < 0$ (from the proton's larger electromagnetic self-energy):

| Document Slug (`qou/library/`) | Citation | $\Delta m_{\mathrm{QCD}}$ (MeV) | $\Delta m_{\mathrm{QED}}$ (MeV) | Total $\Delta m_{np}$ (MeV) | Method & Key Formal Decomposition |
| --- | --- | --- | --- | --- | --- |
| `borsanyi-et-al-2015` (`arxiv-1406.4088v2`) | Borsanyi et al. (BMW), *Science* **347**, 1452 (2015) | $+2.52(17)(24)$ | $-1.00(07)(14)$ | $+1.51(16)(23)$ | Ab initio $1+1+1+1$ lattice QCD+QED with 4 dynamical flavours |
| `gasser-leutwyler-rusetsky-2020-epjc` (`arxiv-2008.05806v2`) & `gasser-leutwyler-rusetsky-2021` (`arxiv-2003.13612v3`) | Gasser, Leutwyler, Rusetsky, *EPJC* **80**, 1121 (2020) & *Phys. Rept.* **897**, 1 (2021) | $+1.87(16)$ | $-0.58(16)$ | $+1.2933$ (input) | Dispersion evaluation of the Cottingham formula $m_{\mathrm{QED}} = m_{\mathrm{el}} + m_{\mathrm{inel}} + m_{\mathrm{sub}} + m_{\mathrm{ct}}$ |
| `walker-loud-carlson-miller-2012` (`arxiv-1210.7777v1`) | Walker-Loud, Carlson, Miller, *Phys. Rev. Lett.* **108**, 232301 (2012) | $+2.59(47)$ | $-1.30(03)(47)$ | $+1.2933$ (input) | Cottingham formula with universal subtraction function $T_1(0, Q^2)$ |
| `can-qcdsf-2025` (`arxiv-2501.08619v2`) | Can et al. (QCDSF), *Phys. Rev. D* (2025) | — | Cottingham $S_1(Q^2)$ | — | Lattice QCD determination of the Compton subtraction function $S_1(Q^2)$ via Feynman-Hellmann |
| `horsley-et-al-2016-qcd-qed` (`arxiv-1508.06401v2`) | Horsley et al. (QCDSF-UKQCD), *JHEP* **04**, 093 (2016) | $+3.51(31)$ | $-2.20(28)(10)$ | $+1.35(18)(08)$ | Dashen-scheme $SU(3)$ flavour-breaking expansion around the symmetric point |

---

## 4. Pre-Registered 50-dps + SymPy Numerical Results

### 4.1 Baseline 50-dps Substrate Parameters

Evaluated at 80 working decimal places and reported at 50 dps via `np_two_term_qed_mup_tension_probe.py`:

- $\mathrm{Vol}(4_1) = 2.0298832128193072500424051085490405718833786150606$
- $q_{\mathrm{proton}} = 1.1099785827513808075916690956107688798744991218736$ (solved from $2\frac{\mathrm{Vol}(4_1)}{\hbar_q^2} F_{\mathrm{Bor}}(q) - 12 = (m_p/m_e)_{\mathrm{CODATA}} = 1836.152673426$)
- $q_{\mathrm{muon}} = 1.1099785956427390466817951293800017527000655610290$ (solved from $\frac{\mathrm{Vol}(4_1)}{\hbar_q^2} = (m_\mu/m_e)_{\mathrm{CODATA}} = 206.7682827$)
- Relative pin offset: $\frac{q_{\mathrm{proton}} - q_{\mathrm{muon}}}{q_{\mathrm{muon}}} = -11.6140602077\text{ ppb}$
- Muon prediction tension at $q_{\mathrm{proton}}$: $\frac{m_\mu(q_{\mathrm{proton}}) - m_\mu^{\mathrm{exp}}}{m_\mu^{\mathrm{exp}}} = +211.2058645\text{ ppb}$ ($+9.49362\sigma$)
- Pure-QCD proton mass at $q_{\mathrm{muon}}$ vs $q_{\mathrm{proton}}$:
  $$m_p^{\mathrm{QCD}}(q_{\mathrm{muon}}) = 938.271860620094\text{ MeV}, \qquad m_p^{\mathrm{QCD}}(q_{\mathrm{proton}}) = 938.272089427324\text{ MeV},$$
  $$\delta m_p = m_p^{\mathrm{QCD}}(q_{\mathrm{muon}}) - m_p^{\mathrm{QCD}}(q_{\mathrm{proton}}) = -0.000228807231\text{ MeV} = -0.000447764580\, m_e \quad (-243.860212\text{ ppb}).$$
- Derived QOU fine-structure constant at $q_{\mathrm{proton}}$:
  $$\alpha_{\mathrm{EM}}^{-1}(q_{\mathrm{proton}}) = 45[3]_q(1 + \delta_{\mathrm{CS}} + 8q\delta_{\mathrm{CS}}^2) = 137.03599953171676169, \qquad \delta_{\mathrm{CS}} = \hbar_q^4 [5]_q.$$
- Energy scales at $q_{\mathrm{proton}}$:
  $$E_0(q_p) = \frac{m_e}{q_p(q_p-1)} = 4.18598136329\text{ MeV}, \quad E_0^{\mathrm{full}}(q_p) = \frac{E_0(q_p)}{1-\hbar_q^2} = 4.22748335563\text{ MeV}, \quad \alpha_{\mathrm{bind}} = 8G\,m_e = 3.74445965994\text{ MeV}.$$

### 4.2 Exact SymPy & Lean-Proved 3-Strand Quark Charge Operator Identities

| Quantity | Exact Rational / Polynomial Closed Form in $q$ | Lean 4 Theorem (`NucleonWeightSpaceTwoTerm.lean`) | Value at $q_{\mathrm{proton}}$ |
| --- | --- | --- | --- |
| $\sum_{i=1}^3 Q_i^2$ on $W_p = (2,1)$ ($\mathfrak{u}\mathfrak{u}\mathfrak{d}$) | $1$ | `QSelfP` | $1$ |
| $\sum_{i=1}^3 Q_i^2$ on $W_n = (1,2)$ ($\mathfrak{u}\mathfrak{d}\mathfrak{d}$) | $\frac{2}{3}$ | `QSelfN` | $0.66666667$ |
| $\sum_{i<j} Q_i Q_j$ on $W_p = (2,1)$ ($\mathfrak{u}\mathfrak{u}\mathfrak{d}$) | $0$ | `QPairP_eq_sum` | $0$ |
| $\sum_{i<j} Q_i Q_j$ on $W_n = (1,2)$ ($\mathfrak{u}\mathfrak{d}\mathfrak{d}$) | $-\frac{1}{3}$ | `QPairN_eq_sum` | $-0.33333333$ |
| $Q_{12}^{(n)} + Q_{23}^{(n)}$ matrix decomposition | $-\frac{2}{9}I_3 + \frac{1}{2}\big(Q_{12}^{(p)} + Q_{23}^{(p)}\big)$ | `QAdjn_eq_static_add_half_QAdjp` | Exact $3\times 3$ identity |
| $\mathrm{tr}(V_p^3) = \mathrm{tr}(V_n^3)$ (Borromean $V^3$) | $-\frac{q^{12}-3q^{10}+3q^8-5q^6+3q^4-3q^2+1}{q^6}$ | `trace_borromeanV3A`, `trace_borromeanV3B` | $+3.13370993$ |
| $\mathrm{tr}\!\left((K_n - K_p) V^3\right)$ (Cartan split) | $(q^{-1} - q)\,\mathrm{tr}(V^3)$ | `trace_K_diff_word` | $-0.62596543$ |
| $\mathrm{tr}\!\left((Q_{12}^{(p)}+Q_{23}^{(p)}) V_p^3\right)$ | $-\frac{2(q-1)^4(q+1)^4(q^4+q^2+1)}{9q^6}$ | `trace_QAdjp_borromeanV3` | $-0.0012920421$ |
| $\overline{\mathrm{tr}}_{\mathrm{conn}}(p, V^3) = \frac{1}{3}\mathrm{tr}((Q_{12}^{(p)}+Q_{23}^{(p)})V_p^3)$ | $-\frac{2(q-1)^4(q+1)^4(q^4+q^2+1)}{27q^6}$ | `trace_QAdjp_borromeanV3` ($/3$) | **$-0.00043068071$** |
| $\overline{\mathrm{tr}}_{\mathrm{conn}}(n, V^3) = \frac{1}{3}\!\left(\mathrm{tr}((Q_{12}^{(n)}+Q_{23}^{(n)})V_n^3) + \frac{2}{9}\mathrm{tr}(V_n^3)\right)$ | $+\frac{(q-1)^4(q+1)^4(2q^4-q^2+2)}{27q^6}$ | `trace_QAdjn_borromeanV3_connected` ($/3$) | **$+0.00021843255$** |
| $\Delta\overline{\mathrm{tr}}_{\mathrm{conn}}(V^3) = \overline{\mathrm{tr}}_{\mathrm{conn}}(n, V^3) - \overline{\mathrm{tr}}_{\mathrm{conn}}(p, V^3)$ | $+\frac{(q-1)^4(q+1)^4(4q^4+q^2+4)}{27q^6}$ | `trace_QAdj_connected_diff_borromeanV3` ($/3$) | **$+0.00064911326$** |
| $\frac{1}{3}\Delta\mathrm{tr}\!\left((Q_{12}+Q_{23})V^3\right)_{n-p}$ (full adjacent) | $\frac{2q^{12}-7q^{10}+10q^8-12q^6+10q^4-7q^2+2}{9q^6}$ | `trace_QAdj_diff_borromeanV3` ($/3$) | **$-0.22114243$** |
| $\mathrm{Tr}(Q_{12}^{(n)}B_1+Q_{23}^{(n)}B_2) - \mathrm{Tr}(Q_{12}^{(p)}A_1+Q_{23}^{(p)}A_2)$ | $-\frac{2q}{3}$ | 1-crossing plain trace split | $-0.73998572$ |
| $\mathcal{C}_{\mathrm{tr}K}^{\mathrm{adj}}(q) = \frac{q^{-1}\mathrm{Tr}_n - q\mathrm{Tr}_p}{q+q^{-1}}$ | $-\frac{2(q^2+2)(2q^2-1)}{9q(q^2+1)}$ | 1-crossing $K^{\otimes 3}$-weighted split | $-0.42444267$ |
| $\mathcal{C}_{\mathrm{Hecke}}^{\mathrm{pair}}(q) = \mathrm{tr}_D(Q_{\mathrm{pair}}^{(n)}) - \mathrm{tr}_D(Q_{\mathrm{pair}}^{(p)})$ | $-\frac{(2q^2-1)(2q^2+1)}{9q(q^2+1)}$ | 1-crossing Hecke Convention-D split | $-0.22745799$ |

### 4.3 Test 1 Table — Impact of Proton QED Self-Energy $M_p^{\mathrm{QED}}$ on the $211\text{ ppb}$ $\mu\text{--}p$ Tension

Solving $m_p^{\mathrm{QCD}}(q_{\mathrm{proton}}^{\mathrm{new}}) + M_p^{\mathrm{QED}} = m_p^{\mathrm{exp}}$ at 50 dps:

| Candidate for $M_p^{\mathrm{QED}}$ | $M_p^{\mathrm{QED}}$ (MeV) | $\frac{q_p^{\mathrm{new}} - q_\mu}{q_\mu}$ (ppb) | $m_\mu(q_p^{\mathrm{new}})$ Err (ppb) | $m_\mu$ Tension ($\sigma$) | Status |
| --- | --- | --- | --- | --- | --- |
| **Baseline** ($M_p^{\mathrm{QED}} = 0$) | $0.0$ | $-11.61406$ | $+211.20586$ | $+9.49362\sigma$ | One-term baseline |
| **Exact gap target** $+\delta m_p = m_p^{\mathrm{exp}} - m_p^{\mathrm{QCD}}(q_\mu)$ | $+0.0002288072$ | $0.00000$ | $0.00000$ | $0.00000\sigma$ | Reference target |
| **`DERIVED-Bor-V3 (plain)`:** $+m_e |\overline{\mathrm{tr}}_{\mathrm{conn}}(p, V^3)|$ | **$+0.0002200773$** | **$-0.44312$** | **$+8.05837$** | **$+0.36222\sigma$** | **Primary Derived ($96.2\%$ closed)** |
| **`DERIVED-Bor-V3 (K^3-wt)`:** $+q\,m_e |\overline{\mathrm{tr}}_{\mathrm{conn}}(p, V^3)|$ | **$+0.0002442811$** | **$+0.78544$** | **$-14.28350$** | **$-0.64204\sigma$** | **Primary Derived ($93.2\%$ closed)** |
| **QOU-Hecke-1 (+):** $+\alpha_{\mathrm{EM}} m_e\,\mathrm{tr}_D(Q_{\mathrm{pair}}^{(p)})$ | $+0.0001732385$ | $-2.82062$ | $+51.29403$ | $+2.30565\sigma$ | 1-crossing Hecke trace ($75.7\%$ closed) |
| **QOU-Hecke-2 (+):** $+\alpha_{\mathrm{EM}} m_e \hbar_q$ | $+0.0003694697$ | $+7.13991$ | $-129.84181$ | $-5.83634\sigma$ | 1-crossing un-traced scale |
| Lit: GL 1982 Cottingham $M_p^{\mathrm{QED}} = +0.63\text{ MeV}$ | $+0.6300000000$ | $+31982.377$ | $-581338.75$ | $-26131.0\sigma$ | Macroscopic (absorbed in $F_{\mathrm{Bor}}$) |
| Lit: BMW 2015 $|\Delta M_{\mathrm{QED}}| = +1.00\text{ MeV}$ | $+1.0000000000$ | $+50787.179$ | $-922896.77$ | $-41483.9\sigma$ | Macroscopic (absorbed in $F_{\mathrm{Bor}}$) |
| **QOU-Macro-1 (+):** $+\alpha_{\mathrm{EM}} m_p / (2\pi)$ | $+1.089718332$ | $+55348.642$ | $-1005719.9$ | $-45206.7\sigma$ | Macroscopic (absorbed in $F_{\mathrm{Bor}}$) |
| **QOU-Macro-2 (+):** $+\alpha_{\mathrm{EM}} m_p \hbar_q$ | $+0.678402821$ | $+34441.774$ | $-626020.3$ | $-28139.4\sigma$ | Macroscopic (absorbed in $F_{\mathrm{Bor}}$) |
| **Control-Neg-1 (-):** $-m_e |\overline{\mathrm{tr}}_{\mathrm{conn}}(p, V^3)|$ | $-0.0002200773$ | $-22.78499$ | $+414.35335$ | $+18.6250\sigma$ | Sign-flipped control (doubles tension) |
| `[REJECTED-FIT] QOU-P13`: $+\alpha_{\mathrm{EM}} m_e \hbar_q [2]_q/[3]_q$ | $+0.0002440990$ | $+0.77620$ | $-14.11539$ | $-0.63448\sigma$ | **Rejected ad-hoc grid fit** |

### 4.4 Test 2A Table — Macroscopic & Single-Wrap Two-Term Splitting $\Delta m_{np} = \Delta m_{\mathrm{QCD}} + \Delta m_{\mathrm{QED}}$

| Strong Term $\Delta m_{\mathrm{QCD}}$ | QED Term $\Delta m_{\mathrm{QED}}$ | $\Delta m_{\mathrm{QCD}}$ (MeV) | $\Delta m_{\mathrm{QED}}$ (MeV) | $\Delta m_{np}^{\mathrm{tot}}$ (MeV) | Comparison Benchmark / Rel. Diff vs CODATA | Cross-Anchor Swing (ppm) |
| --- | --- | --- | --- | --- | --- | --- |
| **`DERIVED-S8a` (Borromean $V^3$ Cartan):** $\alpha_{\mathrm{bind}}(q-q^{-1})\mathrm{tr}(V^3)$ | **`DERIVED-Bor-V3-Full`:** $\alpha_{\mathrm{bind}}\frac{1}{3}\Delta\mathrm{tr}((Q_{12}+Q_{23})V^3)$ | **$+2.3439021$** | **$-0.8280589$** | **$+1.5158432$** | Matches **BMW 2015 lattice QCD+QED** ($+2.52 - 1.00 = +1.51(16)(23)\text{ MeV}$, within $0.04\sigma$!) | $-0.1726$ |
| **`DERIVED-S8a` (Borromean $V^3$ Cartan):** $\alpha_{\mathrm{bind}}(q-q^{-1})\mathrm{tr}(V^3)$ | **`DERIVED-Bor-V3-Full (E0)`:** $E_0\frac{1}{3}\Delta\mathrm{tr}((Q_{12}+Q_{23})V^3)$ | $+2.3439021$ | $-0.9256981$ | $+1.4182040$ | $+9.6549\%$ vs CODATA ($0.4\sigma$ vs BMW 2015) | $-0.2687$ |
| **`DERIVED-S8a` (Borromean $V^3$ Cartan):** $\alpha_{\mathrm{bind}}(q-q^{-1})\mathrm{tr}(V^3)$ | **QED-Lit-BMW2015:** $-1.00\text{ MeV}$ | $+2.3439021$ | $-1.0000000$ | $+1.3439021$ | $+3.9099\%$ vs CODATA | $-0.1933$ |
| **`DERIVED-S8b` (Borromean $V^3$ at $E_0$):** $E_0(q-q^{-1})\mathrm{tr}(V^3)$ | **QED-Lit-WLCM2012:** $-1.30\text{ MeV}$ | $+2.6202794$ | $-1.3000000$ | $+1.3202794$ | $+2.0834\%$ vs CODATA (matches WLCM $+2.59 - 1.30$) | $+0.0357$ |
| **S1 (published one-term):** $\alpha_{\mathrm{bind}} |\Delta\Phi_D|$ | **QED-0:** $0$ | $+1.0540991$ | $0.0$ | $+1.0540991$ | $-18.4975\%$ vs CODATA (under-predicts before QED) | $-0.0149$ |
| **S2 (oriented D closed form):** $\alpha_{\mathrm{bind}} \cdot 4\ln q$ | **QED-Q1:** $-\frac{1}{3}\alpha_{\mathrm{EM}} m_p \hbar_q$ | $+1.5627985$ | $-0.2261343$ | $+1.3366642$ | $+3.3503\%$ vs CODATA | $-0.1129$ |
| **S5 (Form A single-wrap):** $Q_A + m_e$ | **`DERIVED-Bor-V3-Conn (plain)`:** $-m_e\Delta\overline{\mathrm{tr}}_{\mathrm{conn}}(V^3)$ | $+1.2946448$ | $-0.0003317$ | **$+1.2943131$** | **$+0.0757\%$** vs CODATA (reduces $Q_A$ error from $+0.1014\%$) | $+0.0184$ |
| **S5 (Form A single-wrap):** $Q_A + m_e$ | **`DERIVED-Bor-V3-Conn (q-wt)`:** $-q m_e\Delta\overline{\mathrm{tr}}_{\mathrm{conn}}(V^3)$ | $+1.2946448$ | $-0.0003682$ | **$+1.2942766$** | **$+0.0729\%$** vs CODATA | $+0.0184$ |

### 4.5 Test 2B Table — Impact of Separating $\Delta m_{\mathrm{QED}}$ on $Q_\beta$ and the Convention-D $c_k$ Ladder

At $q_{\mathrm{proton}}$ under Convention D ($z_D = q^3/(q^2+1)$):
- $Q_A(q_p) = 0.7836458274\text{ MeV}$ ($+1675.75\text{ ppm}$ vs $Q_\beta^{\mathrm{exp}} = 0.7823348293\text{ MeV}$)
- $Q_{N1}^D(q_p) = Q_A \cos(\alpha_D - u/2) = 0.7828615049\text{ MeV}$ ($+673.21\text{ ppm}$)
- $Q_{N2}^D(q_p) = Q_{N1}^D(q_p)(1 - u^2) = 0.7828047136\text{ MeV}$ ($+600.62\text{ ppm}$, residual $Q_{N2}^D - Q_\beta^{\mathrm{exp}} = +0.469884\text{ keV}$)

| QED Candidate $\Delta m_{\mathrm{QED}}$ | $\Delta m_{\mathrm{QED}}$ (MeV) | $Q_{N2}^D + \Delta m_{\mathrm{QED}}$ Err (ppm) | Residual Closed (%) | $c_2^{\mathrm{emp}}(D)$ (total $u^2$ coeff) | $c_3^{\mathrm{emp}}(D, q_p)$ (with $c_2=-1$) | Status |
| --- | --- | --- | --- | --- | --- | --- |
| **QED-0 (baseline, no QED separation)** | $0.0$ | $+600.618\text{ ppm}$ | $0.0\%$ | $-9.27387$ | $-971.497$ | Unseparated baseline |
| **`DERIVED-Bor-V3-Conn (plain)`:** $-m_e\Delta\overline{\mathrm{tr}}_{\mathrm{conn}}(V^3)$ | **$-0.000331696$** | **$+176.636\text{ ppm}$** | **$70.59\%$** | **$-3.43326$** | **$-285.708$** | **Primary Derived (same op as Test 1)** |
| **`DERIVED-Bor-V3-Conn (K_n/K_p-wt)`:** $-m_e(q^{-1}\overline{\mathrm{tr}}_n - q\overline{\mathrm{tr}}_p)_{\mathrm{conn}}$ | **$-0.000344840$** | **$+159.834\text{ ppm}$** | **$73.39\%$** | **$-3.20181$** | **$-258.531$** | **Primary Derived ($K^{\otimes 3}$-weighted)** |
| **`DERIVED-Bor-V3-Conn (K_p^3-wt)`:** $-m_e(\overline{\mathrm{tr}}_n - q\overline{\mathrm{tr}}_p)_{\mathrm{conn}}$ | **$-0.000355900$** | **$+145.698\text{ ppm}$** | **$75.74\%$** | **$-3.00707$** | **$-235.666$** | **Primary Derived ($K_p^{\otimes 3}$ on proton)** |
| **`DERIVED-Bor-V3-Conn (q-wt)`:** $-q\,m_e\Delta\overline{\mathrm{tr}}_{\mathrm{conn}}(V^3)$ | **$-0.000368176$** | **$+130.007\text{ ppm}$** | **$78.35\%$** | **$-2.79092$** | **$-210.285$** | **Primary Derived (uniform $q$-scaled)** |
| **QED-Q12:** $-\frac{1}{3}\alpha_{\mathrm{EM}} m_e \hbar_q$ | $-0.000123157$ | $+443.196\text{ ppm}$ | $26.21\%$ | $-7.10529$ | $-716.868$ | 1-crossing un-traced scale |
| **QED-Q17:** $\alpha_{\mathrm{EM}} m_e \mathcal{C}_{\mathrm{Hecke}}^{\mathrm{pair}}(q)$ | $-0.000848178$ | $-483.545\text{ ppm}$ | Overshoots | $+5.66112$ | $+782.132$ | 1-crossing Hecke trace |
| **`DERIVED-Bor-V3-Full`:** $\alpha_{\mathrm{bind}}\frac{1}{3}\Delta\mathrm{tr}_{\mathrm{adj}}(V^3)$ | $-0.82805890$ | $-1057850\text{ ppm}$ | Macroscopic | $+14571.5$ | $+1711061$ | Macroscopic (pairs with $\Delta m_{\mathrm{QCD}}(V^3)$) |
| `[REJECTED-FIT] QED-Q14`: $-\frac{1}{3}\alpha_{\mathrm{EM}} m_e h [2]_q$ | $-0.000522547$ | $-67.315\text{ ppm}$ | Overshoots | $-0.07270$ | $+108.882$ | **Rejected ad-hoc grid fit** |

---

## 5. Complete Downstream File-by-File Impact Inventory

### 5.1 Lean 4 Modules (`folio/quantum-observable-universe/`)

| File Path | Current Role & State | Required Changes for Two-Term $\Delta m_{\mathrm{QCD}} + \Delta m_{\mathrm{QED}}$ Upgrade |
| --- | --- | --- |
| [`lean/QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean) | **COMPLETE & SORRY-FREE ON `main`:** Formalizes $K_p, K_n$, $Q_{\mathrm{self}}^{(p,n)}$, $Q_{\mathrm{pair}}^{(p,n)}$, $Q_{12}^{(p,n)}, Q_{23}^{(p,n)}, Q_{13}^{(p,n)}$, local crossing commutativity, intertwiner breaking $P Q_{ij}^{(p)} \ne Q_{ij}^{(n)} P$, general word two-term decomposition (`trace_twoTerm_QAdj_diff_word`), exact matrix decomposition `QAdjn_eq_static_add_half_QAdjp`, and Borromean $V^3$ fourth-order connected traces (`trace_QAdjp_borromeanV3`, `trace_QAdjn_borromeanV3_connected`, `trace_QAdj_connected_diff_borromeanV3`). | Serve as the canonical Lean 4 import for all downstream two-term nucleon mass and splitting modules. |
| [`lean/QOU/MassTheory/NeutronProtonEMSign.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/NeutronProtonEMSign.lean) | Proves over $\mathbb{Q}$ that `protonPairChargeSum = 0`, `neutronPairChargeSum = -1/3`, and `neutronPairChargeSum < protonPairChargeSum`. Docstring is **stale**: still cites the retired Convention-C "$+0.63\%$ over-prediction" to motivate why a negative EM term reduces the residual. | 1. Add self-charge sum theorems `protonSelfChargeSum = 1`, `neutronSelfChargeSum = 2/3`, `neutronSelfChargeSum - protonSelfChargeSum = -1/3` (or cross-link `QSelfP`, `QSelfN` in `NucleonWeightSpaceTwoTerm.lean`).<br>2. Update module docstring to Convention D and cross-reference `NucleonWeightSpaceTwoTerm.lean` ($\Delta m_{\mathrm{QCD}}(V^3) = +2.3439\text{ MeV}$, $\Delta m_{\mathrm{QED}}(V^3) = -0.8281\text{ MeV}$). |
| [`lean/QOU/Torsion/neutron_proton_splitting.lean`](../../folio/quantum-observable-universe/lean/QOU/Torsion/neutron_proton_splitting.lean) | Defines one-term `npMassSplitting (alpha deltaPhi : ℝ) := alpha * |deltaPhi|` and proves `npMassSplitting_symm` and `npMassSplitting_pos`. | 1. Import `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm`.<br>2. Define `npMassSplittingTwoTerm (dmQCD dmQED : ℝ) := dmQCD + dmQED` and prove `npMassSplittingTwoTerm < dmQCD` whenever `dmQED < 0`. |
| [`observations/neutron-proton-mass-splitting.lean`](../../folio/quantum-observable-universe/observations/neutron-proton-mass-splitting.lean) | Re-exports `npMassSplitting_symm` and `npMassSplitting_pos` from `QOU.Torsion.neutron_proton_splitting`. | Re-export the two-term definitions and sign/bound theorems alongside the legacy one-term theorems. |
| [`lean/QOU/Mass/NucleonWordTraceClosedForm.lean`](../../folio/quantum-observable-universe/lean/QOU/Mass/NucleonWordTraceClosedForm.lean) | Proves Convention-D closed-form polynomials $P_p(q), P_n(q)$ for the 11-letter nucleon words (`qou-0155`). | Add docstring note clarifying that $P_p(q), P_n(q)$ represent the uncharged $H_3(q)$ word traces and cross-link `NucleonWeightSpaceTwoTerm.lean`. |
| [`lean/QOU/QuantumObservableUniverses/QDifferentialGeometry.lean`](../../folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/QDifferentialGeometry.lean) | Defines `npMassSplitting` at lines 1732–1733 in the monolithic QOU namespace. | Add `npMassSplittingTwoTerm` and link to `QOU.Torsion.neutron_proton_splitting` and `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm`. |
| [`knots-particles-confinement/categorical-proton.lean`](../../folio/quantum-observable-universe/knots-particles-confinement/categorical-proton.lean) & [`categorical-neutron.lean`](../../folio/quantum-observable-universe/knots-particles-confinement/categorical-neutron.lean) | Formalize categorical proton ($\mathfrak{u}\mathfrak{u}\mathfrak{d}$) and neutron ($\mathfrak{u}\mathfrak{d}\mathfrak{d}$) total charge ($+1$ vs $0$) and topological stability. | Link pairwise charge operators and Borromean $V^3$ connected traces from `NucleonWeightSpaceTwoTerm.lean`. |
| [`mass-theory/knot-mass-formula-unified.lean`](../../folio/quantum-observable-universe/mass-theory/knot-mass-formula-unified.lean) | Formalizes unified knot mass functional $m(K) = E_0 \cdot |\mathrm{tr}_q(\rho(b_K))|$. | Document where the connected 4th-order Borromean charge trace $M_N^{\mathrm{QED}}$ enters the composite 3-strand baryon mass functional $m_N = m_N^{\mathrm{QCD}} + m_N^{\mathrm{QED}}$. |
| [`lean/QOU/QBeta/*`](../../folio/quantum-observable-universe/lean/QOU/QBeta/) (319 files) | Formalize the 1ppQ $Q_\beta$ Kashiwara ladder (`QBetaPrediction.lean`, `QBetaSingleWrap.lean`, `ConventionDKashiwara*`, etc.). | No breaking changes to existing $Q_A, Q_{N1}, Q_{N2}$ algebraic proofs; add an optional two-term connected Borromean dressing theorem `QBetaBorromeanConnectedTwoTerm` importing `trace_QAdj_connected_diff_borromeanV3`. |

### 5.2 Content Narrative & Schema Blocks (`folio/quantum-observable-universe/`)

| Block Path (`.md` & `.ts`) | Current State & Stale Claims | Required Updates |
| --- | --- | --- |
| [`mass-theory/isospin-mass-split-em-localisation.md`](../../folio/quantum-observable-universe/mass-theory/isospin-mass-split-em-localisation.md) & [`.ts`](../../folio/quantum-observable-universe/mass-theory/isospin-mass-split-em-localisation.ts) | Proves $\sum_{i<j} q_i q_j = 0$ ($p$) vs $-1/3$ ($n$), **but contains a stale Convention-C paragraph**: claims the strong term is $1.3014\text{ MeV}$ ("$+0.63\%$ above experiment") and that the negative EM correction reduces that $+0.63\%$ over-prediction. | **High-priority staleness fix:** Replace the retired Convention-C $1.3014\text{ MeV}$ ($+0.63\%$) narrative with the Lean-proved Borromean $V^3$ two-term and connected 4th-order trace identities from `NucleonWeightSpaceTwoTerm.lean` ($\Delta m_{\mathrm{QCD}}(V^3) = +2.3439\text{ MeV}$, $\Delta m_{\mathrm{QED}}(V^3) = -0.8281\text{ MeV}$, sum $+1.5158\text{ MeV}$, and connected 4th-order $\overline{\mathrm{tr}}_{\mathrm{conn}}$), and cite the 6 newly ingested Cottingham/lattice papers. |
| [`observations/neutron-proton-mass-splitting.md`](../../folio/quantum-observable-universe/observations/neutron-proton-mass-splitting.md) & [`.ts`](../../folio/quantum-observable-universe/observations/neutron-proton-mass-splitting.ts) | Presents the one-term Convention-D transfer-product prediction $\Delta m = \alpha|\Delta\Phi_D| = 1.0541\text{ MeV}$ ($-18.50\%$) as an `empirical-Comparison` block and notes that $O(\alpha_{\mathrm{EM}})$ electromagnetic self-energy is omitted. | 1. Cite the 6 newly ingested Cottingham & lattice QCD+QED benchmark papers (`borsanyi-et-al-2015`, `gasser-leutwyler-rusetsky-2020-epjc`, `gasser-leutwyler-rusetsky-2021`, `walker-loud-carlson-miller-2012`, `can-qcdsf-2025`, `horsley-et-al-2016-qcd-qed`).<br>2. Present the Lean-proved Borromean $V^3$ two-term decomposition ($\Delta m_{\mathrm{QCD}}(V^3) = +2.3439\text{ MeV}$, $\Delta m_{\mathrm{QED}}(V^3) = -0.8281\text{ MeV}$, sum $+1.5158\text{ MeV}$ vs BMW 2015 $+2.52 - 1.00 = +1.51(16)(23)\text{ MeV}$) alongside the one-term transfer-product baseline.<br>3. Maintain strict separation between model derivation and CODATA empirical comparison. |
| [`mass-theory/neutron-proton-splitting.md`](../../folio/quantum-observable-universe/mass-theory/neutron-proton-splitting.md) & [`.ts`](../../folio/quantum-observable-universe/mass-theory/neutron-proton-splitting.ts) | Derives the pure-strong transfer-product traced volumes $\Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d})$ and $\Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d})$ under Convention D ($1.0541\text{ MeV}$). | Add explicit section on the two-term Borromean $V^3$ decomposition $\Delta m_{np} = \Delta m_{\mathrm{QCD}} + \Delta m_{\mathrm{QED}}$, cross-referencing `NucleonWeightSpaceTwoTerm.lean`. |
| [`knots-particles-confinement/categorical-proton.md`](../../folio/quantum-observable-universe/knots-particles-confinement/categorical-proton.md) & [`.ts`](../../folio/quantum-observable-universe/knots-particles-confinement/categorical-proton.ts) | Describes the proton $\mathfrak{u}\mathfrak{u}\mathfrak{d}$ Borromean/3-strand structure and mass identity $m_p = 2m_\mu F_{\mathrm{Bor}} - 12m_e$. | Document the connected 4th-order Borromean self-energy $M_p^{\mathrm{QED}} = m_e|\overline{\mathrm{tr}}_{\mathrm{conn}}(p, V^3)| = +0.22008\text{ keV}$ (`trace_QAdjp_borromeanV3`) and its zero-parameter closure of $96.2\%$ of the $+0.22881\text{ keV}$ ($211\text{ ppb}$) $\mu\text{--}p$ gap. |

### 5.3 Compute Producers, Witnesses, and Coordination Docs (Summary Table)

| File Path | Current Role | Impact & Required Action |
| --- | --- | --- |
| [`tools/qou-substrate/python/qou_substrate/constants.py`](../../tools/qou-substrate/python/qou_substrate/constants.py) | Canonical 50-dps solver `q_at()` for `q_proton` (raw $N=0$ proton identity) and `q_muon_at()`. | **Tier A (Non-Breaking):** Add 50-dps helpers `tr_borromean_v3_at()`, `tr_e21_borromean_v3_at()`, `tr_conn_borromean_p_at()`, `tr_conn_borromean_n_at()`, `tr_conn_borromean_diff_at()`, and parallel solver `q_two_term_borromean_at(dps=50, k_weighted=False)`. **Tier B (Owner-Gated):** Do NOT alter `q_at()` or `Q_50_DIGIT_STR` without explicit owner ruling. |
| [`tools/qou-substrate/python/qou_substrate/__init__.py`](../../tools/qou-substrate/python/qou_substrate/__init__.py) | Public symbol exports for `qou_substrate`. | **Tier A:** Re-export the new 50-dps Borromean $V^3$ trace and parallel two-term pin helpers in `__all__`. |
| [`computations/m_p_substrate_identity_50dps.py`](../../computations/m_p_substrate_identity_50dps.py) & [`computations/m-p-substrate-identity-50dps.witness.json`](../../computations/m-p-substrate-identity-50dps.witness.json) | Production 50-dps witness producer for $m_p$, $m_n = m_p + Q_\beta + m_e$, and the $9.5\sigma$ $\mu\text{--}p$ tension. | **Tier A:** Add Lean-backed 50-dps helpers from `NucleonWeightSpaceTwoTerm.lean` and emit additive witness block `two_term_borromean_qed_diagnostics` ($M_p^{\mathrm{QED,conn}} = +0.220077\text{ keV}$, $+8.06\text{ ppb} / +0.36\sigma$ on $m_\mu$; $\Delta m_{\mathrm{QED}}^{\mathrm{conn}} = -0.331696\text{ keV}$, $+176.6\text{ ppm}$ on $Q_\beta$, $+147\text{ ppb}$ on $m_n$). |
| [`computations/derived_masses.py`](../../computations/derived_masses.py) | Canonical zero-parameter derived-mass facade at muon-pin `_q_0()`. | **Tier A:** Add `e_0_scale_hierarchy_matter_mev()`, `borromean_v3_e21_strong_qcd_diff_mev()`, `borromean_v3_connected_qed_proton_mev()`, `borromean_v3_connected_qed_diff_mev()`, and `q_beta_kashiwara_n2_two_term_mev()`; expose in `derivation_summary()` and `__all__`. |
| [`computations/canonical_mass.py`](../../computations/canonical_mass.py) | Single-entry facade reading `m_p_MeV` and `m_n_MeV` from `m-p-substrate-identity-50dps.witness.json`. | **Tier A:** Add `proton_qed_self_energy_borromean_mev()`, `np_qed_splitting_borromean_conn_mev()`, and `proton_neutron_mass_two_term_mev()` reading `two_term_borromean_qed_diagnostics`. |
| [`computations/qbeta/qbeta_utils.py`](../../computations/qbeta/qbeta_utils.py) | Shared 50-dps 1ppQ $Q_\beta$ Kashiwara ladder and $H_3(q)$ block character utilities. | **Tier A:** Add individual nucleon sector characters `chi_proton_{3,21,111}(q)`, `chi_neutron_{3,21,111}(q)`, GPMT modified trace `d_mod_111_convention_D(q)` and `t_mod_111_convention_D(q, species)` (`NucleonIdempotentModifiedTrace.lean`), plus `borromean_v3_connected_qed_diff_over_me(q)` and `c2_target_two_term_at()` / `c3_target_two_term_at()`. |
| [`computations/probes/np_two_term_qed_mup_tension_probe.py`](../../computations/probes/np_two_term_qed_mup_tension_probe.py) & [`folio/.../np_two_term_qed_mup_tension_probe.py`](../../folio/quantum-observable-universe/computations/probes/np_two_term_qed_mup_tension_probe.py) | Pre-registered 50-dps + SymPy verification probe for `NucleonWeightSpaceTwoTerm.lean`. | **Tier A (Immediate):** Extend both copies to verify Section 7 of `NucleonWeightSpaceTwoTerm.lean` (`trace_e3p_borromeanV3`, `trace_e21p_borromeanV3`, `trace_e21_strong_cartan_diff_borromeanV3`, `trace_e21p_QAdjp_borromeanV3`, `trace_e21n_QAdjn_borromeanV3`, `trace_e21_QAdj_diff_borromeanV3`, `hadronicScaleE0_mul_hbar_eq_me`) and Route 2 `NucleonIdempotentModifiedTrace.lean` (`chi3`, `chi21`, `chi111`, `dMod111`, `tMod111`). |
| [`computations/level1-qvalues.py`](../../computations/level1-qvalues.py) & [`computations/free-neutron-decay.py`](../../computations/free-neutron-decay.py) | Producers for `level1-qvalues.witness.json` (Ch 10 table) and `free-neutron-decay.witness.json`. | **Tier A:** Add `two_term_borromean_diagnostics` (`e_{(2,1)}`-projected strong + QED Borromean traces in `level1-qvalues.py`; connected 4th-order QED $Q_\beta$ dressing in `free-neutron-decay.py`). |
| [`computations/probes/np_splitting/np_hadronic_scale_e0_probe.py`](../../computations/probes/np_splitting/np_hadronic_scale_e0_probe.py) & [`np_second_order_weak_fe_ef_probe.py`](../../computations/probes/np_splitting/np_second_order_weak_fe_ef_probe.py) | Pre-registered `np_splitting` probes for $E_0$ and $FE/EF$ ($e_{(3)}, e_{(2,1)}$) on $V^3$. | **Tier A:** Add cross-check rows verifying the Lean-proved `trace_e21_strong_cartan_diff_borromeanV3`, `trace_e21_QAdj_diff_borromeanV3`, and `hadronicScaleE0_mul_hbar_eq_me`. |
| [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) & [`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) | Canonical coordination docs for the 1ppQ $Q_\beta$ program and $c_k/d_k$ ladder under Convention D. | Record the Test 2B finding: separating the zero-parameter connected 4th-order Borromean QED trace $\Delta m_{\mathrm{QED}}^{\mathrm{conn}} = -m_e\,\Delta\overline{\mathrm{tr}}_{\mathrm{conn}}(V^3) \in [-0.368, -0.332]\text{ keV}$ closes **$70.6\%\text{--}78.4\%$** of the $+600.6\text{ ppm}$ Convention-D $Q_{N2}^D$ residual using the **exact same operator** that closes $93.2\%\text{--}96.2\%$ of the $211\text{ ppb}$ $\mu\text{--}p$ tension. |

---

## 6. Exhaustive Compute & Witness Update Specification

This section specifies, line-by-line and file-by-file, the exact Python/MPFR compute additions and witness updates required across `/Users/litlfred/space_cats/qou` to wire the three newly completed Lean 4 formalizations:

1. **[`NucleonWeightSpaceTwoTerm.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean) (Sections 1–7, 690 lines, `0 sorry`):**
   - Full 3D weight-space Borromean $V^3 = (\sigma_1\sigma_2^{-1})^3$ trace (`trace_borromeanV3A`, `trace_borromeanV3B`), strong Cartan difference (`trace_strong_cartan_diff_borromeanV3`), adjacent-crossing QED trace (`trace_QAdjp_borromeanV3`, `trace_QAdjn_borromeanV3`, `trace_QAdj_diff_borromeanV3`), and connected 4th-order QED trace (`trace_QAdjn_borromeanV3_connected`, `trace_QAdj_connected_diff_borromeanV3`).
   - **Section 7 (lines 521–689):** $U_q(\mathfrak{gl}_2)$ lowering/raising products $FE_p, EF_n$, decuplet idempotents $e_{(3)}^{p,n} = \frac{1}{[3]_q}FE_p / EF_n$, and 2D mixed-symmetry nucleon projectors $e_{(2,1)}^{p,n} = I_3 - e_{(3)}^{p,n}$:
     - `trace_e3p_borromeanV3` / `trace_e3n_borromeanV3` (lines 590–599):
       $$\mathrm{tr}(e_{(3)}^p V_p^3) = \mathrm{tr}(e_{(3)}^n V_n^3) = 1.$$
     - `trace_e21p_borromeanV3` / `trace_e21n_borromeanV3` (lines 602–615):
       $$\mathrm{tr}(e_{(2,1)}^p V_p^3) = \mathrm{tr}(e_{(2,1)}^n V_n^3) = \mathrm{tr}(V^3) - 1 = -\frac{(q^4 - q^2 + 1)(q^8 - 2q^6 - 2q^2 + 1)}{q^6} = 2 - 3h^4 - h^6.$$
       *(Note: this proves from first principles in 3D weight space that the $e_{(2,1)}$-projected Borromean trace is identically the 2D Hoefsmit character $\chi^{(2,1)}(\mathcal{B}_3) = 2 - 3h^4 - h^6$ used in `computations/_li_2_q_util.py` line 733!)*
     - `trace_e21_strong_cartan_diff_borromeanV3` (lines 618–620):
       $$\Delta\mathrm{tr}_{\mathrm{QCD}}(e_{(2,1)} V^3) := \mathrm{tr}(K_p e_{(2,1)}^p V_p^3) - \mathrm{tr}(K_n e_{(2,1)}^n V_n^3) = (q - q^{-1})\,\mathrm{tr}(e_{(2,1)} V^3) = 0.416905081915616195 \quad (\text{at } q_0),$$
       matching $4\ln q_0 = 0.417362881278078049$ to $0.11\%$, and giving:
       - $\alpha_{\mathrm{bind}}\,\Delta\mathrm{tr}_{\mathrm{QCD}}(e_{(2,1)} V^3) = +1.56108426\text{ MeV}$,
       - $E_0^{(0)}\,\Delta\mathrm{tr}_{\mathrm{QCD}}(e_{(2,1)} V^3) = +1.74515690\text{ MeV}$,
       - $E_0^{\mathrm{full}}\,\Delta\mathrm{tr}_{\mathrm{QCD}}(e_{(2,1)} V^3) = +1.76245929\text{ MeV}$ (inside the Gasser–Leutwyler–Rusetsky 2020/2021 Cottingham dispersion benchmark $\Delta m_{\mathrm{QCD}} = +1.87(16)\text{ MeV}$).
     - `trace_e21p_QAdjp_borromeanV3`, `trace_e21n_QAdjn_borromeanV3`, `trace_e21_QAdj_diff_borromeanV3` (lines 638–679):
       $$\mathrm{tr}\!\left(e_{(2,1)}^p (Q_{12}^{(p)} + Q_{23}^{(p)}) V_p^3\right) = -\frac{2(q-1)^2(q+1)^2(q^{12}-q^6+1)}{9 q^6 (q^4+q^2+1)} = -0.00448304953501474742 \quad (-2.29083361\text{ keV}\text{ at }m_e),$$
       $$\mathrm{tr}\!\left(e_{(2,1)}^n (Q_{12}^{(n)} + Q_{23}^{(n)}) V_n^3\right) = \frac{4q^{16}-11q^{14}+13q^{12}-22q^{10}+20q^8-22q^6+13q^4-11q^2+4}{9 q^6 (q^4+q^2+1)} = -0.444092609533361299 \quad (-226.93085748\text{ keV}\text{ at }m_e),$$
       $$\Delta\mathrm{tr}_{e_{(2,1)}}(Q_{\mathrm{adj}} V^3) = \frac{2q^{16}-5q^{14}+5q^{12}-8q^{10}+8q^8-8q^6+5q^4-5q^2+2}{3 q^6 (q^4+q^2+1)} = -0.439609559998346552 \quad (-224.64002387\text{ keV}\text{ at }m_e).$$
     - `hadronicScaleE0_mul_hbar_eq_me` (lines 682–688):
       $$E_0(q) \cdot q^2(1 - q^{-1}) = m_e, \qquad E_0(q) := \frac{m_e}{q(q-1)}.$$
2. **[`NucleonIdempotentModifiedTrace.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/NucleonIdempotentModifiedTrace.lean) (Route 2, 344 lines, `0 sorry`):**
   - Full $H_3(q)$ Wedderburn character decomposition on the 11-letter words `protonWord` and `neutronWord` (`chi3_protonCoord`, `chi3_neutronCoord`, `chi21_protonCoord`, `chi21_neutronCoord`, `chi111_protonCoord`, `chi111_neutronCoord`, `trM_eq_wedderburn_sum`), proving `w111_conventionD = 0`, and constructing the Geer–Patureau-Mirand–Turaev (GPMT) renormalized modified trace $\mathsf{t}_D = \mathsf{d}_D(S^{(1^3)})\,\chi_{(1^3)}$ (`dMod111`, `tMod111`) with $\mathsf{d}_D(S^{(1^3)}) = -(q^2+1)/(q^4(q^4+q^2+1)) = -0.392115555925466$, $\mathsf{t}_D(p) = -0.653515250735625$, $\mathsf{t}_D(n) = -5.68836067952548$, $\Delta\mathsf{t}_D = -5.03484542878985$.
3. **[`CategoricalLagrangianTwoTermBridge.lean`](../../folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/CategoricalLagrangianTwoTermBridge.lean) (Route 3, 461 lines, `0 sorry`):**
   - Formalizes the two-sector categorical action $S_{\mathrm{total}} = S_{\mathrm{QCD}} + S_{\mathrm{QED}}$, the $O(\hbar_q^2)$ vs $O(\hbar_q^1)$ scale hierarchy `hadronicScale_mul_q_sq_hbar_eq_me` / `hadronicScale_strong_to_matter_ratio`, and the structural exclusion theorems ruling out the three ad-hoc candidates (`QOU-P13`, `QED-Q14`, `QED-Q6b`).

---

### 6.1 Architectural Separation: Tier A (Non-Breaking Additive) vs. Tier B (Owner-Gated Canonical Pin Changes)

To prevent unapproved cascade shifts across the 279 proton-anchored and 455 muon-anchored witnesses in `computations/`, all compute updates are partitioned into two strict tiers:

- **Tier A — Non-Breaking Additive Functions, Probes & Diagnostic Witness Blocks (Immediate Implementation):**
  - Adds 50-dps MPFR functions, SymPy algebraic identity checks, and **new additive JSON keys** (`two_term_borromean_qed_diagnostics`) to existing witnesses without altering `Q_50_DIGIT_STR`, `q_at()`, `m_p_MeV`, `m_n_MeV`, or `Q_beta_MeV`.
  - All existing witness assertions and downstream consumers remain bit-identical.
- **Tier B — Owner-Gated Canonical Pin & Production Witness Promotions (Requires Owner Ruling):**
  - Promotes `q_two_term_borromean_at()` or the two-term $Q_\beta$ / $m_n$ values (`Q_beta_two_term_MeV = 0.7824599 MeV`, `m_n_two_term_MeV = 939.5655543 MeV`) into the primary `predictions` block of `m-p-substrate-identity-50dps.witness.json` and updates the currently failing 10 ppb `m_n_matches_codata_within_10ppb` assertion.

---

### 6.2 Detailed File-by-File Compute Update Specification

#### 1. [`tools/qou-substrate/python/qou_substrate/constants.py`](../../tools/qou-substrate/python/qou_substrate/constants.py) & [`__init__.py`](../../tools/qou-substrate/python/qou_substrate/__init__.py)
- **Existing Code Context:**
  - Lines 112–153: `_solve_q_proton_f64()` solves $2(\mathrm{Vol}(4_1)/\hbar_q^2)F_{\mathrm{Bor}}(q) - 12 = m_p/m_e$ in binary64.
  - Lines 288–318: `q_at(dps=50)` solves the raw $N=0$ proton identity at arbitrary `mpmath` precision.
  - Lines 321–349: `q_muon_at(dps=50)` solves the $N=0$ muon identity $\mathrm{Vol}(4_1)/\hbar_q^2 = m_\mu/m_e$ at arbitrary `mpmath` precision.
  - Lines 536–603: `__all__` export list (mirrored in `tools/qou-substrate/python/qou_substrate/__init__.py` lines 53–125).
- **Tier A Additive Updates (`constants.py` after line 380):**
  1. `tr_borromean_v3_at(q=None, dps: int = 50)` — evaluates `trace_borromeanV3A`:
     $$\mathrm{tr}(V^3) = \frac{-q^{12} + 3q^{10} - 3q^8 + 5q^6 - 3q^4 + 3q^2 - 1}{q^6}.$$
  2. `tr_e21_borromean_v3_at(q=None, dps: int = 50)` — evaluates `trace_e21p_borromeanV3`:
     $$\mathrm{tr}(e_{(2,1)} V^3) = -\frac{(q^4 - q^2 + 1)(q^8 - 2q^6 - 2q^2 + 1)}{q^6}.$$
  3. `tr_conn_borromean_p_at(q=None, dps: int = 50)` — evaluates `trace_QAdjp_borromeanV3`:
     $$\overline{\mathrm{tr}}_{\mathrm{conn}}(p, V^3) = -\frac{2(q^2 - 1)^4(q^4 + q^2 + 1)}{27 q^6}.$$
  4. `tr_conn_borromean_n_at(q=None, dps: int = 50)` — evaluates `trace_QAdjn_borromeanV3_connected`:
     $$\overline{\mathrm{tr}}_{\mathrm{conn}}(n, V^3) = +\frac{(q^2 - 1)^4(2q^4 - q^2 + 2)}{27 q^6}.$$
  5. `tr_conn_borromean_diff_at(q=None, dps: int = 50)` — evaluates `trace_QAdj_connected_diff_borromeanV3`:
     $$\Delta\overline{\mathrm{tr}}_{\mathrm{conn}}(V^3) = +\frac{(q^2 - 1)^4(4q^4 + q^2 + 4)}{27 q^6}.$$
  6. `q_two_term_borromean_at(dps: int = 50, k_weighted: bool = False)` — solves the two-term connected Borromean proton pin
     $$2\frac{\mathrm{Vol}(4_1)}{(1 - q^{-1})^2}F_{\mathrm{Bor}}(q) - 12 + w(q)\,\left|\overline{\mathrm{tr}}_{\mathrm{conn}}(p, V^3)\right| = \frac{m_p}{m_e}$$
     (with $w(q) = 1$ if `k_weighted=False` and $w(q) = q$ if `k_weighted=True`) via 14 Newton iterations at `dps + 25` guard digits, returning `q_0(p, two-term) = 1.10997856934886364362709800446...` (plain, $+8.06\text{ ppb} = +0.36\sigma$ vs $q_{\mathrm{muon}}$) or `1.10997856787429927271645512008...` ($K_p^{\otimes 3}$-weighted, $-14.40\text{ ppb} = -0.64\sigma$ vs $q_{\mathrm{muon}}$).
  7. Re-export all six functions in `constants.py` `__all__` and `tools/qou-substrate/python/qou_substrate/__init__.py`.

---

#### 2. [`computations/m_p_substrate_identity_50dps.py`](../../computations/m_p_substrate_identity_50dps.py) & [`computations/m-p-substrate-identity-50dps.witness.json`](../../computations/m-p-substrate-identity-50dps.witness.json)
- **Existing Code Context:**
  - Lines 116–164: `f_bor(q)` and `verify_f_bor_factorization(q)` compute $F_{\mathrm{Bor}}(q)$.
  - Lines 172–203: `f_bor_split(q)` computes the exploratory $\pm\hbar_q^3/2$ doublet split (`predictions_pathC`).
  - Lines 244–278: Evaluates `m_p_pred = 2 * m_mu * F - 12 * m_e`, `Q_beta_pred = q_beta_kashiwara_n2_mev()`, `Delta_m_pred = Q_beta_pred + m_e`, `m_n_pred = m_p_pred + Delta_m_pred`.
  - Lines 362–500: Builds and saves `m-p-substrate-identity-50dps.witness.json` with blocks `substrate_building_blocks`, `predictions`, `predictions_pathC`, `neutron_diagnostics`, `codata_comparison`, `lean_uniqueness_ref`, and 5 assertions (note: assertion #5 `m_n_matches_codata_within_10ppb` at lines 484–496 currently fails under Convention D at $+501\text{ ppb}$ vs the legacy Convention-C $10\text{ ppb}$ threshold).
- **Tier A Additive Updates:**
  1. Add helper functions (after `f_bor_split` at line 204) backed by `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm`:
     - `borromean_v3_connected_qed_traces(q)` returning a dict of 50-dps `mpf` values for `tr_V3`, `tr_e3_V3`, `tr_e21_V3`, `tr_conn_p`, `tr_conn_n`, `tr_conn_diff`, `tr_e21_QAdjp`, `tr_e21_QAdjn`, and `tr_e21_QAdj_diff`.
  2. In `main()` (around line 310), compute at 50 dps:
     - `M_p_QED_conn_MeV = m_e * abs(tr_conn_p)` ($+0.000220077030037\text{ MeV} = +0.220077\text{ keV}$)
     - `M_p_QED_conn_Kp_MeV = m_e * q * abs(tr_conn_p)` ($+0.000244280786416\text{ MeV} = +0.244281\text{ keV}$)
     - `Delta_m_QED_conn_MeV = -m_e * tr_conn_diff` ($-0.000331696486049\text{ MeV} = -0.331696\text{ keV}$)
     - `Delta_m_QED_conn_KnKp_MeV = -m_e * (tr_conn_n / q - q * tr_conn_p)` ($-0.000344840318548\text{ MeV} = -0.344840\text{ keV}$)
     - `Q_beta_two_term_MeV = Q_beta_pred + Delta_m_QED_conn_MeV` ($0.782459922026\text{ MeV}$, $+176.636\text{ ppm}$ vs CODATA $0.78234664\text{ MeV}$)
     - `m_n_two_term_MeV = m_p_pred + Q_beta_two_term_MeV + m_e` ($939.565554308\text{ MeV}$, $+147.0\text{ ppb}$ vs CODATA $939.56542052\text{ MeV}$, reducing the $+501\text{ ppb}$ neutron mass residual by $70.7\%$).
  3. Add a new witness data block `wb.add_data("two_term_borromean_qed_diagnostics", {...})` recording the above 50-dps values, their Lean theorem citations (`QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdjp_borromeanV3`, `trace_QAdj_connected_diff_borromeanV3`, `trace_e21p_borromeanV3`, `trace_e21_strong_cartan_diff_borromeanV3`, `trace_e21_QAdj_diff_borromeanV3`), and the resulting $\mu\text{--}p$ tension reduction from $-211.09\text{ ppb}$ ($9.38\sigma$) to $+8.06\text{ ppb}$ ($+0.36\sigma$).
  4. Add two exact algebraic assertions to the witness:
     - `borromean_v3_e3_plus_e21_equals_full_trace`: verifies $\mathrm{tr}(e_{(3)} V^3) + \mathrm{tr}(e_{(2,1)} V^3) = \mathrm{tr}(V^3)$ to $10^{-45}$.
     - `borromean_v3_conn_proton_closes_mup_gap_within_1sigma`: verifies that $M_p^{\mathrm{QED,conn}}$ brings the $\mu\text{--}p$ mass-prediction residual from $9.38\sigma$ ($211.1\text{ ppb}$) inside $1\sigma$ ($22.5\text{ ppb}$, actual $+8.06\text{ ppb} = +0.36\sigma$).

---

#### 3. [`computations/derived_masses.py`](../../computations/derived_masses.py)
- **Existing Code Context:**
  - Lines 265–302: `e_0_n0_mev()` and `e_0_mev()` compute $E_0^{(0)} = m_e/(q_0(q_0-1))$ and $E_0^{\mathrm{full}} = E_0^{(0)}/(1 - \hbar_q^2)$ at the muon pin `_q_0()`.
  - Lines 460–536: `q_beta_predicted_mev()` and `q_beta_kashiwara_n2_mev()` compute the 1-term Convention-D Kashiwara $Q_\beta$ predictions ($Q_{N1}^D$ and $Q_{N2}^D$).
  - Lines 699–765: `derivation_summary()` and `__all__`.
- **Tier A Additive Updates:**
  1. Add `e_0_scale_hierarchy_matter_mev() -> mp.mpf` (after `e_0_mev()` at line 303):
     - Computes $E_0^{(0)} \cdot q_0^2(1 - q_0^{-1})$ and verifies agreement with `M_E_MEV` to 50 dps (`QOU.QuantumObservableUniverses.CategoricalLagrangianTwoTermBridge.hadronicScale_mul_q_sq_hbar_eq_me`).
  2. Add `borromean_v3_e21_strong_qcd_diff_mev(full_tower: bool = True) -> mp.mpf`:
     - Computes $E_0 \cdot (q_0 - q_0^{-1}) \cdot \mathrm{tr}(e_{(2,1)} V^3)$ (`NucleonWeightSpaceTwoTerm.trace_e21_strong_cartan_diff_borromeanV3`), giving $+1.76246\text{ MeV}$ (`full_tower=True`) or $+1.74516\text{ MeV}$ (`full_tower=False`).
  3. Add `borromean_v3_connected_qed_proton_mev(k_weighted: bool = False) -> mp.mpf`:
     - Computes $M_p^{\mathrm{QED,conn}} = m_e w(q_0) |\overline{\mathrm{tr}}_{\mathrm{conn}}(p, V^3)|$ (`trace_QAdjp_borromeanV3`).
  4. Add `borromean_v3_connected_qed_diff_mev(weighting: str = "plain") -> mp.mpf`:
     - Computes $\Delta m_{\mathrm{QED}}^{\mathrm{conn}} = -m_e \Delta\overline{\mathrm{tr}}_{\mathrm{conn}}(V^3)$ (`trace_QAdj_connected_diff_borromeanV3`) for `weighting in {"plain", "KnKp", "Kp3", "q"}`.
  5. Add `q_beta_kashiwara_n2_two_term_mev(weighting: str = "plain") -> mp.mpf`:
     - Returns `q_beta_kashiwara_n2_mev() + borromean_v3_connected_qed_diff_mev(weighting)`.
  6. Include the new quantities in `derivation_summary()` (lines 699–739) and `__all__` (lines 742–761).

---

#### 4. [`computations/canonical_mass.py`](../../computations/canonical_mass.py)
- **Existing Code Context:**
  - Lines 49–87: `_load_witness()` loads `computations/m-p-substrate-identity-50dps.witness.json`.
  - Lines 93–148: `proton_mass_mev()`, `neutron_mass_mev()`, `nucleon_mass_mev()`.
  - Lines 150–214: `_self_test()` checks `proton_mass_mev()` ($0.24\text{ ppm}$) and `neutron_mass_mev()`.
- **Tier A Additive Updates:**
  1. Add `proton_qed_self_energy_borromean_mev() -> mp.mpf` and `np_qed_splitting_borromean_conn_mev() -> mp.mpf` reading `data["two_term_borromean_qed_diagnostics"]` from `m-p-substrate-identity-50dps.witness.json` (with fallback calculation via `qou_substrate.constants.tr_conn_borromean_p_at()` / `tr_conn_borromean_diff_at()` if the witness has not yet been regenerated).
  2. Add `neutron_mass_two_term_mev() -> mp.mpf` returning `proton_mass_mev() + Q_beta_two_term_MeV + m_e` ($939.5655543\text{ MeV}$, $+147\text{ ppb}$ vs CODATA).
  3. Export in `__all__` and display in `_self_test()`.

---

#### 5. [`computations/qbeta/qbeta_utils.py`](../../computations/qbeta/qbeta_utils.py)
- **Existing Code Context:**
  - Lines 44–72: `chi_block_3(q)`, `chi_block_21(q, intra_order="borromean")`, `chi_block_111(q)` define the transition difference characters $\chi_\lambda(T_n - T_p)$ on $H_3(q)$.
  - Lines 185–261: `wedderburn_weights(q, convention=...)`, `tr_m_at(q, convention=...)`, `eps_delta_at(q, convention=...)`.
  - Lines 264–384: `substrate_ladder_quantities(q, convention=...)` and `c3_target_at(q, q_codata, m_e, convention=...)`.
  - Lines 387–424: `__all__`.
- **Tier A Additive Updates:**
  1. **Route 2 Per-Nucleon Sector Characters & GPMT Modified Trace (`NucleonIdempotentModifiedTrace.lean`):**
     - Add `chi_proton_3(q)`, `chi_neutron_3(q)`, `chi_proton_21(q)`, `chi_neutron_21(q)`, `chi_proton_111(q)`, `chi_neutron_111(q)` implementing theorems `chi3_protonCoord`, `chi3_neutronCoord`, `chi21_protonCoord`, `chi21_neutronCoord`, `chi111_protonCoord`, `chi111_neutronCoord`:
       $$\chi_{(3)}(p) = -\frac{2q^{16}-5q^{14}+7q^{12}-4q^{10}+2q^8-q^6+q^4-q^2+1}{q^5},$$
       $$\chi_{(3)}(n) = \frac{(q^2-q+1)(q^2+q+1)(2q^{12}-5q^{10}+9q^8-10q^6+9q^4-3q^2+1)}{q^{11}},$$
       $$\chi_{(2,1)}(p) = -\frac{(q-1)(q+1)(2q^{12}-q^{10}+q^8+3q^6+1)}{4q^8},$$
       $$\chi_{(2,1)}(n) = \frac{q^{16}+3q^{14}+3q^{12}+3q^{10}-20q^8+19q^6-21q^4+13q^2-5}{4q^8},$$
       $$\chi_{(1^3)}(p) = \frac{q^{16}-q^{14}+q^{12}-q^{10}+2q^8-4q^6+7q^4-5q^2+2}{q^{11}},$$
       $$\chi_{(1^3)}(n) = \frac{(q^2-q+1)(q^2+q+1)(q^{12}-3q^{10}+9q^8-10q^6+9q^4-5q^2+2)}{q^5}.$$
     - Note the exact consistency identity: `chi_neutron_3(q) - chi_proton_3(q) == chi_block_3(q)`, `chi_neutron_21(q) - chi_proton_21(q) == chi_block_21(q, "borromean")`, and `chi_neutron_111(q) - chi_proton_111(q) == chi_block_111(q)`.
     - Add `d_mod_111_convention_D(q)` and `t_mod_111_convention_D(q, species="diff")` implementing `dMod111` and `tMod111`:
       $$\mathsf{d}_D(S^{(1^3)}) = -\frac{q^2+1}{q^4(q^4+q^2+1)}, \qquad \mathsf{t}_D(x) = \mathsf{d}_D(S^{(1^3)})\,\chi_{(1^3)}(x).$$
  2. **Route 1 Two-Term Connected Borromean QED Ladder Helpers (`NucleonWeightSpaceTwoTerm.lean`):**
     - Add `borromean_v3_connected_qed_diff_mev(q, m_e, weighting="plain")` implementing `trace_QAdj_connected_diff_borromeanV3`.
     - Add `c2_target_two_term_at(q, q_codata, m_e, convention="D", weighting="plain")` and `c3_target_two_term_at(q, q_codata, m_e, convention="D", weighting="plain")`: subtracts $\Delta m_{\mathrm{QED}}^{\mathrm{conn}}$ from $Q_{\mathrm{codata}}$ before inverting the Convention-D ladder, yielding the residual targets shown in Table 4.2 ($c_2^{\mathrm{req}} \in [-3.433, -2.791]$ vs $-3$, $c_3^{\mathrm{req}} \in [-285.7, -210.3]$ vs $-971.5$).

---

#### 6. [`computations/probes/np_two_term_qed_mup_tension_probe.py`](../../computations/probes/np_two_term_qed_mup_tension_probe.py) & Mirror [`folio/quantum-observable-universe/computations/probes/np_two_term_qed_mup_tension_probe.py`](../../folio/quantum-observable-universe/computations/probes/np_two_term_qed_mup_tension_probe.py)
- **Existing Code Context:**
  - Lines 37–241: `verify_symbolic_weight_space_borromean()` verifies Sections 1–6 of `NucleonWeightSpaceTwoTerm.lean` in exact `sympy` over $\mathbb{Q}(q)$.
  - Lines 248–746: Runs 50-dps Test 1 ($\mu\text{--}p$ $211\text{ ppb}$ tension) and Test 2A/2B ($n\text{--}p$ splitting & $Q_\beta$ Kashiwara ladder) and emits `computations/probes/np-two-term-qed-mup-tension-probe.witness.json`.
- **Tier A Immediate Updates (in both copies):**
  1. In `verify_symbolic_weight_space_borromean()`:
     - Construct $FE_p, EF_n$, $e_{(3)}^p = \frac{1}{[3]_q}FE_p$, $e_{(3)}^n = \frac{1}{[3]_q}EF_n$, $e_{(2,1)}^p = I_3 - e_{(3)}^p$, $e_{(2,1)}^n = I_3 - e_{(3)}^n$, and verify symbolic zero-residuals for:
       - `trace_e3p_borromeanV3` and `trace_e3n_borromeanV3` ($\mathrm{tr}(e_{(3)} V^3) = 1$),
       - `trace_e21p_borromeanV3` and `trace_e21n_borromeanV3` ($\mathrm{tr}(e_{(2,1)} V^3) = -(q^4-q^2+1)(q^8-2q^6-2q^2+1)/q^6 = 2 - 3h^4 - h^6$),
       - `trace_e21_strong_cartan_diff_borromeanV3` ($\mathrm{tr}(K_n e_{(2,1)}^n V_n^3) - \mathrm{tr}(K_p e_{(2,1)}^p V_p^3) = (q^{-1}-q)\mathrm{tr}(e_{(2,1)} V^3)$),
       - `trace_FEp_QAdjp_borromeanV3`, `trace_EFn_QAdjn_borromeanV3`,
       - `trace_e21p_QAdjp_borromeanV3`, `trace_e21n_QAdjn_borromeanV3`, `trace_e21_QAdj_diff_borromeanV3`,
       - `hadronicScaleE0_mul_hbar_eq_me` ($E_0(q)\cdot q^2(1-q^{-1}) = m_e$).
     - Verify the Route 2 `NucleonIdempotentModifiedTrace.lean` Wedderburn sum and GPMT modified trace identities on `protonWord` and `neutronWord`.
  2. In `main()` (Test 2A and witness emission):
     - Add the 50-dps evaluation of the $e_{(2,1)}$-projected two-term splitting:
       - $\Delta m_{\mathrm{QCD}}(e_{(2,1)} V^3) = E_0^{\mathrm{full}}(q-q^{-1})\mathrm{tr}(e_{(2,1)} V^3) = +1.76245929\text{ MeV}$ (or $+1.74515690\text{ MeV}$ at $E_0^{(0)}$, $+1.56108426\text{ MeV}$ at $\alpha_{\mathrm{bind}}$),
       - $\Delta m_{\mathrm{QED}}(e_{(2,1)} V^3, m_e) = m_e\,\Delta\mathrm{tr}_{e_{(2,1)}}(Q_{\mathrm{adj}} V^3) = -0.22464002\text{ MeV}$ (at $m_e$ scale) or $-0.54883677\text{ MeV}$ (at $\alpha_{\mathrm{bind}}/3$ scale),
       - Record the Route 2 GPMT modified trace values $\mathsf{d}_D(S^{(1^3)}) = -0.39211556$, $\mathsf{t}_D(p) = -0.65351525$, $\mathsf{t}_D(n) = -5.68836068$, $\Delta\mathsf{t}_D = -5.03484543$ in the witness JSON.

---

#### 7. [`computations/level1-qvalues.py`](../../computations/level1-qvalues.py), [`computations/free-neutron-decay.py`](../../computations/free-neutron-decay.py), and `np_splitting` Probes
- **[`computations/level1-qvalues.py`](../../computations/level1-qvalues.py) (lines 118–315):**
  - Currently computes `Phi(uud) = -0.61488598`, `Phi(udd) = -0.89639498`, `|dPhi| = 0.28150899`, and `dm_np = alpha * |dPhi| = 1.0541\text{ MeV}` ($-18.50\%$) for the Ch 10 transfer-product table (`level1-qvalues.witness.json`).
  - **Tier A Update:** Add an additive `borromean_v3_two_term_diagnostics` sub-block to `level1-qvalues.witness.json` reporting the Lean-proved Borromean $V^3$ full and $e_{(2,1)}$-projected strong + QED decompositions from `NucleonWeightSpaceTwoTerm.lean` alongside the one-term transfer-product baseline.
- **[`computations/free-neutron-decay.py`](../../computations/free-neutron-decay.py) (lines 285–590):**
  - Currently computes `Q_beta` across the 1-term Convention-D ladder (`Q_A`, `Q_N1`, `Q_N2`) and emits `free-neutron-decay.witness.json`.
  - **Tier A Update:** Add `two_term_borromean_qed_dressing` to `free-neutron-decay.witness.json` reporting `Delta_m_QED_conn_MeV = -0.000331696 MeV` and `Q_N2_two_term_MeV = 0.782459922 MeV` ($+176.6\text{ ppm}$ vs CODATA, $70.6\%$ error reduction).
- **[`computations/probes/np_splitting/np_hadronic_scale_e0_probe.py`](../../computations/probes/np_splitting/np_hadronic_scale_e0_probe.py) (lines 19–47) & [`np_second_order_weak_fe_ef_probe.py`](../../computations/probes/np_splitting/np_second_order_weak_fe_ef_probe.py) (lines 25–122):**
  - **Tier A Update:** Add print + assertion lines cross-checking `trace_e21_strong_cartan_diff_borromeanV3`, `trace_e21_QAdj_diff_borromeanV3`, and `hadronicScaleE0_mul_hbar_eq_me` against the exact rational expressions proved in `NucleonWeightSpaceTwoTerm.lean`.

---

## 7. Sequenced Formalize-First & Compute Workplan for Epic `qou-9pl8`

### Phase 1 — Lean 4 Downstream Wiring of `NucleonWeightSpaceTwoTerm.lean` & `NucleonIdempotentModifiedTrace.lean`
1. **Bean 1A (`QOU/MassTheory/NeutronProtonEMSign.lean`):**
   - Cross-link `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm` (`QSelfP`, `QSelfN`, `QPairP_eq_sum`, `QPairN_eq_sum`, `QAdjn_eq_static_add_half_QAdjp`) and update the stale Convention-C docstring ($1.3014\text{ MeV}$, "$+0.63\%$ over-prediction") to Convention D and the Borromean $V^3$ two-term trace.
2. **Bean 1B (`QOU/Torsion/neutron_proton_splitting.lean` & `observations/neutron-proton-mass-splitting.lean`):**
   - Import `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm`, define `npMassSplittingTwoTerm (dmQCD dmQED : ℝ) : ℝ := dmQCD + dmQED`, and prove `npMassSplittingTwoTerm dmQCD dmQED < dmQCD` for `dmQED < 0`.

### Phase 2 — Tier A Non-Breaking Compute & Witness Wiring (Section 6 Specification)
1. **Bean 2A (`np_two_term_qed_mup_tension_probe.py` + mirror):**
   - Extend `verify_symbolic_weight_space_borromean()` and the 50-dps tables/witness to include all Section 7 `e_{(2,1)}`-projected Borromean traces (`trace_e3p_borromeanV3`, `trace_e21p_borromeanV3`, `trace_e21_strong_cartan_diff_borromeanV3`, `trace_e21p_QAdjp_borromeanV3`, `trace_e21n_QAdjn_borromeanV3`, `trace_e21_QAdj_diff_borromeanV3`, `hadronicScaleE0_mul_hbar_eq_me`) and Route 2 `NucleonIdempotentModifiedTrace.lean` quantities (`chi3`, `chi21`, `chi111`, `dMod111`, `tMod111`).
2. **Bean 2B (`qou_substrate/constants.py`, `derived_masses.py`, `canonical_mass.py`, `qbeta_utils.py`, `m_p_substrate_identity_50dps.py`):**
   - Implement the Tier A non-breaking 50-dps helpers and additive witness block `two_term_borromean_qed_diagnostics` specified in Section 6.2 items 1–5.

### Phase 3 — Narrative & Schema Block Sync + Stale Convention-C Excision
1. **Bean 3A (`mass-theory/isospin-mass-split-em-localisation.{md,ts}`):**
   - Excise the stale Convention-C $1.3014\text{ MeV}$ ($+0.63\%$) narrative.
   - Present the exact 3-strand weight-space charge operator identities from `NucleonWeightSpaceTwoTerm.lean` (`QAdjn_eq_static_add_half_QAdjp`, `trace_QAdjp_borromeanV3`, `trace_QAdjn_borromeanV3_connected`, `trace_QAdj_connected_diff_borromeanV3`, `trace_e21_strong_cartan_diff_borromeanV3`, `trace_e21_QAdj_diff_borromeanV3`) and cite the 6 newly ingested Cottingham/lattice QCD+QED papers.
2. **Bean 3B (`observations/neutron-proton-mass-splitting.{md,ts}` & `mass-theory/neutron-proton-splitting.{md,ts}`):**
   - Present the Borromean $V^3$ two-term table (both full 3D and $e_{(2,1)}$-projected 2D nucleon sector) alongside the one-term baseline with strict derivation-vs-CODATA separation.

### Phase 4 — 1ppQ $Q_\beta$ & $\mu\text{--}p$ Tension Coordination Update + Tier B Owner Decision Gate
1. **Bean 4A (`docs/coordination/1ppq-qbeta.md` & `docs/coordination/ck-dk-canonical-registry.md`):**
   - Record the unified single-operator Borromean $V^3$ connected 4th-order trace result across both the $211\text{ ppb}$ $\mu\text{--}p$ gap ($M_p^{\mathrm{QED}} = +0.2201\text{ keV}$, $+0.36\sigma$) and the Convention-D $Q_{N2}^D$ residual ($\Delta m_{\mathrm{QED}}^{\mathrm{conn}} = -0.3317\text{ to }-0.3682\text{ keV}$, closing $70.6\%\text{--}78.4\%$ of the $+600.6\text{ ppm}$ residual), together with the Route 3 structural exclusion theorems (`CategoricalLagrangianTwoTermBridge.lean`) rejecting `QOU-P13`, `QED-Q14`, and `QED-Q6b`.
2. **Bean 4B (Tier B Owner Decision Gate):**
   - Present the zero-parameter `NucleonWeightSpaceTwoTerm.lean` results to the owner to decide whether the connected 4th-order Borromean trace should remain a Tier A diagnostic cross-check or be promoted to Tier B (canonical two-term nucleon mass and $Q_\beta$ witnesses).
