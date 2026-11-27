# Pre-Registration: Zero-Parameter Gamow $\alpha$-Decay, Magic $N=126$ Preformation ($S_\alpha$), and Internally Derived $Q_\alpha^{\mathrm{QOU}}$ Benchmark (2026-11-23)

Bean `qou-i2jl`. Written and committed **before** evaluating the candidate $N=126$ overlap/kink preformation mechanisms or the internally derived $Q_\alpha^{\mathrm{QOU}}$ half-lives against experiment.

## 1. Calibration & Precision Discipline (STRICT)

- **Working precision:** `mpmath.workdps(80)` throughout (`OUT_DPS = 50`), zero `float64` imports, literals, or casts (`parse_float=str` on JSON inputs).
- **Substrate pin:** `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`).
- **Fine-structure constant:** QOU Form-B Bring–Schwinger root $\alpha_q = \alpha_{\mathrm{EM}}(q_0)$ (`1/\alpha_q = 137.035999127...`); **zero** imported CODATA $\alpha_{\mathrm{EM}}$.
- **Allowed physical calibrations:** CAL-1 $m_e$ (`codata("electron mass energy equivalent in mev")`), CAL-2/proton-pinned $q_0$, CAL-3 charged pion mass $m_{\pi^\pm} = 139.57039\;\mathrm{MeV}$ fixing reduced pion Compton length $r_\pi = \bar{\lambda}_\pi = \hbar c / m_{\pi^\pm}$ and 3D FCC Wigner–Seitz nuclear radius constant
  $$r_0^{\mathrm{FCC}} = \left(\frac{3}{4\pi\sqrt{2}}\right)^{1/3} \frac{3}{2}\,\frac{\hbar c}{m_{\pi^\pm}}.$$
- **Zero fitting:** No preformation factor $S_\alpha$, radius constant $r_0$, screening shift, or oscillator gap is adjusted to match NUBASE2020 half-lives.

## 2. Pre-Registered Observables & Mechanisms

### Part A — Baseline Open-Shell vs Magic $N=126$ Gamow–Gurney–Condon WKB Benchmark
Evaluate unscreened and Perlman–Rasmussen-screened Gamow–Gurney–Condon WKB half-lives $T_{1/2}^{\mathrm{WKB}}$ across open-shell heavy emitters `${}^{212}\mathrm{Po}, {}^{214}\mathrm{Po}, {}^{222}\mathrm{Rn}, {}^{226}\mathrm{Ra}, {}^{238}\mathrm{U}$ (plus ${}^8\mathrm{Be}$) versus magic $N=126$ `${}^{210}\mathrm{Po}$ (`NUBASE2020` + `AME2020`), recording the empirical closed-shell spectroscopic preformation ratio
$$S_\alpha^{\mathrm{emp}}({}^{210}\mathrm{Po}) = \frac{T_{1/2}^{\mathrm{WKB}}({}^{210}\mathrm{Po})}{T_{1/2}^{\mathrm{exp}}({}^{210}\mathrm{Po})}.$$

### Part B — Two Zero-Parameter Candidate Mechanisms for $N=126$ (${}^{210}\mathrm{Po}$) Cluster Hindrance
Both mechanisms are pre-registered and reported side-by-side without post-hoc selection:

1. **Mechanism B1 (Mayer–Jensen combinatorial seniority / pair-degeneracy overlap $S_\alpha^{\mathrm{MJ}}$):**
   From QOU's Mayer–Jensen sub-shell sequence (`knot-centric-table-table2-data.md`; Maria Goeppert Mayer 1949; Otto Haxel, J. Hans D. Jensen & Hans E. Suess 1949), ${}^{210}_{84}\mathrm{Po}_{126} \to {}^{206}_{82}\mathrm{Pb}_{124} + \alpha$ extracts two valence protons from $1h_{9/2}^2$ ($j_p = 9/2$, $2j_p + 1 = 10$, pair degeneracy $\Omega_p = 5$) and two hole neutrons from the closed $N=126$ $3p_{1/2}$ sub-shell ($j_{n,<} = 1/2$, $2j_{n,<} + 1 = 2$, $\Omega_{n,<} = 1$), whereas open-shell ${}^{212}_{84}\mathrm{Po}_{128}$ extracts two valence neutrons from $2g_{9/2}^2$ above $N=126$ ($j_{n,>} = 9/2$, $2j_{n,>} + 1 = 10$, $\Omega_{n,>} = 5$). Pre-registered exact rational overlaps:
   - Single-proton-subshell $J=0$ projection: $S_{\mathrm{MJ}}^{(\pi)} = \frac{1}{2 j_p + 1} = \frac{1}{10} = 0.1$.
   - Neutron pair-capacity ratio across $N=126$ ($3p_{1/2}^{-2}$ vs $2g_{9/2}^2$): $S_{\mathrm{MJ}}^{(\nu\text{-ratio})} = \frac{2 j_{n,<} + 1}{2 j_{n,>} + 1} = \frac{2}{10} = \frac{1}{5} = 0.2$.
   - Joint closed-shell quenched-BCS proton $\times$ neutron $J=0$ pair projection:
     $$S_{\mathrm{MJ}}^{(\pi\otimes\nu)} = \frac{1}{(2 j_p + 1)(2 j_{n,<} + 1)} = \frac{1}{10 \times 2} = \frac{1}{20} = 0.05.$$

2. **Mechanism B2 (Perdew–Parr / Goeppert-Mayer shell-kink internal WKB attenuation across $r_\pi$):**
   By Perdew–Parr–Levy–Balduz (1982) / LP shadow-price vertex-kink duality, $N = 126$ is a polyhedral/spectrahedral kink where the two-neutron chemical potential jumps by the shell gap $\Delta_{\mathrm{shell}}(126)$, creating an internal cluster-formation WKB attenuation across the CAL-3 pion-Compton formation length $r_\pi = \hbar c / m_{\pi^\pm}$:
   $$S_\alpha^{\mathrm{kink}} = \exp\!\left(-\frac{2\sqrt{2\,\mu_{\mathrm{int}}\,\Delta_{\mathrm{shell}}(126)}\,r_\pi}{\hbar c}\right).$$
   To eliminate any hidden ambiguity in $(\Delta_{\mathrm{shell}}(126), \mu_{\mathrm{int}})$, we pre-register the full $2 \times 2$ zero-parameter QOU matrix plus the AME2020 Perdew–Parr $S_{2n}$ kink reference:
   - **QOU Compton HO spacing:** $\hbar\omega_{\mathrm{QOU}}(A) = E_{\mathrm{osc}}(q_0)\,A^{-1/3}$ with $E_{\mathrm{osc}}(q_0) = \mathfrak{E}_e = m_e / (q_0 - 1)^2$ (`E0MuonUnit.lean`), evaluated at $A = 210$:
     * Gap G1 (1-quantum HO shell jump): $\Delta_{\mathrm{HO}}(210) = \hbar\omega_{\mathrm{QOU}}(210)$.
     * Gap G2 (Mayer–Jensen $\ell = 6$ $1i_{13/2}$ QOU $\hbar_q$-spin-orbit gap): $\Delta_{\mathrm{SO,QOU}}(210) = \hbar_q (2\ell + 1)\,\hbar\omega_{\mathrm{QOU}}(210)\big|_{\ell=6} = 13\,\hbar_q\,\hbar\omega_{\mathrm{QOU}}(210)$ with $\hbar_q = 1 - q_0^{-1}$.
     * Gap G3 (Empirical Perdew–Parr two-neutron separation kink, comparison reference): $\Delta_{2n}^{\mathrm{AME}}(126) = S_{2n}(84,126) - S_{2n}(84,128) = [B_{\mathrm{AME}}(84,126) - B_{\mathrm{AME}}(84,124)] - [B_{\mathrm{AME}}(84,128) - B_{\mathrm{AME}}(84,126)]$.
   - **Internal reduced mass $\mu_{\mathrm{int}}$:** evaluated at BOTH (M1) the $2n$–$2p$ intra-$\alpha$ pair reduced mass $\mu_{2n,2p} = \frac{(2m_n)(2m_p)}{2m_n + 2m_p} \approx m_N$, and (M2) the $\alpha$–daughter reduced mass $\mu_{\alpha,d} = \frac{m_\alpha m_d}{m_\alpha + m_d} \approx 4 m_N$.

### Part C — Honest Derived-$Q_\alpha^{\mathrm{QOU}}$ vs $Q_\alpha^{\mathrm{AME}}$ Benchmark & Sensitivity
Evaluate $Q_\alpha^{\mathrm{QOU}} = B_{\mathrm{QOU}}(Z-2, N-2) + B_\alpha^{\mathrm{QOU}} - B_{\mathrm{QOU}}(Z, N)$ with $B_\alpha^{\mathrm{QOU}} = 16 m_e \mathrm{Vol}(\mathcal{B}_3)$ (`magic_A_binding(2,2)`) across `212Po, 214Po, 222Rn, 210Po, 226Ra, 238U` under both canonical heavy-nucleus binding models in the corpus:
- **H1 (`L4_qclt_periodic_table`, from `canonical_isotope_witness.py`):** $B_{\mathrm{L4}}(Z,N) = B_{\mathrm{qCLT,fac}}(Z,N) - E_C^{\mathrm{CAL3}}(Z,A)$ (`A-1` tree scaling).
- **H2 (`FCC_k12_TL_periodic_table`, from `coordination_surface_deficit_probe.py` + `channel_binding.py`):** 3D FCC $k=12$ close-packed contact count with $(111)$ facet surface deficit ($M_{\mathrm{FCC}}(A) = 6A - \frac{9}{2}A^{2/3}$, $a_S/a_V = 3/4$), evaluated for both `STANDARD_MAP` (flavour-weighted standard channel) and `PAULI_MAP` (`pn`-only standard channel), minus Form-B $r_0^{\mathrm{FCC}}$ Coulomb energy $E_C^{\mathrm{FCC}}(Z,A) = \frac{3}{5}\frac{Z(Z-1)\alpha_q\hbar c}{r_0^{\mathrm{FCC}} A^{1/3}}$.
For each emitter, compute the exact Geiger–Nuttall log-half-life sensitivity $\partial \log_{10} T_{1/2}^{\mathrm{WKB}} / \partial Q_\alpha$ (in $\mathrm{dex/MeV}$) and report the resulting $\Delta Q_\alpha$ and $\Delta \log_{10} T_{1/2}$ honestly, including any unphysical ($Q_\alpha^{\mathrm{QOU}} \le 0$) or multi-dex regimes!
