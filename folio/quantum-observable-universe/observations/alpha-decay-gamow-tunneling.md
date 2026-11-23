Heavy-nucleus $\alpha$-decay $(Z, A) \to (Z - 2, A - 4) + {}^{4}\mathrm{He}$ tests simultaneously the derived fine-structure coupling, the nuclear contact length set by the pion Compton scale, and the vacuum behaviour of the [$q$-exterior derivative](#def:categorical-q-ext-deriv) outside a hadronic core. Following Hans Geiger and John Mitchell Nuttall (1911), George Gamow (1928) \cite{gamow1928}, and Ronald W. Gurney and Edward U. Condon (1928), an $\alpha$ cluster separating from a daughter nucleus $(Z_d, A_d) = (Z - 2, A - 4)$ releases exact inter-fragment proton-pair count

$$
  \binom{Z}{2} - \binom{Z - 2}{2} - 1 = 2(Z - 2) = Z_\alpha Z_d
$$

and tunnels from contact radius $R_{\mathrm{touch}}$ to classical turning radius $R_{\mathrm{turn}} = 2 Z_d \alpha_q \hbar c / Q_\alpha$ in exterior vacuum where the effective deformation relaxes to $q_{\mathrm{local}}(r) \to 1$.

With zero fitted nuclear parameters, all inputs are fixed by the three calibrations: the [substrate parameter](#def:substrate-parameter) $q_0$ determines the Bring--Schwinger coupling $\alpha_q^{-1} \approx 137.036$, while the charged-pion Compton length $r_\pi = \hbar c / m_{\pi^\pm} \approx 1.4138\;\mathrm{fm}$ fixes the tetrahedral bond $\ell_{\mathrm{bond}} = \tfrac{3}{2} r_\pi$ and the face-centred cubic Wigner--Seitz radius constant

$$
  r_0^{\mathrm{FCC}}
  = \left(\frac{3}{4\pi\sqrt{2}}\right)^{1/3}\frac{3}{2}\,\frac{\hbar c}{m_{\pi^\pm}}
  \approx 1.1721\;\mathrm{fm},
  \qquad
  R_{\mathrm{touch}} = r_0^{\mathrm{FCC}}\bigl(A_d^{1/3} + 4^{1/3}\bigr).
$$

For reduced mass $\mu$ and decay energy $Q_\alpha = B(Z_d, N_d) + B_\alpha - B(Z, N) > 0$ with $x = R_{\mathrm{touch}} / R_{\mathrm{turn}} < 1$, the sub-barrier WKB action and assault frequency $\nu_0 = \sqrt{2 Q_\alpha / \mu}\,c / (2 R_{\mathrm{touch}})$ determine the bare tunneling half-life

$$
  2 G(Z_d, Q_\alpha)
  = \frac{2\sqrt{2\mu Q_\alpha}}{\hbar c}\,R_{\mathrm{turn}}
    \Bigl(\arccos\sqrt{x} - \sqrt{x(1 - x)}\Bigr),
  \qquad
  T_{1/2}^{\mathrm{WKB}} = \frac{\ln 2}{\nu_0}\,e^{2 G(Z_d, Q_\alpha)},
$$

recovering the affine Geiger--Nuttall scaling in $Q_\alpha^{-1/2}$ at small $x$. If the core value $q_0 > 1$ persisted uniformly across the exterior Coulomb barrier ($k_q = k / q_0$), the exponent $2 G$ would shrink to $2 G / q_0$, under-predicting the ${}^{238}\mathrm{U}$ half-life by $3.42\;\mathrm{dex}$; $\alpha$-decay therefore confirms directly that $q_{\mathrm{local}}(r) \to 1$ outside nuclear matter.

## Open-shell benchmark versus the $N = 126$ shell closure

Evaluated at experimental AME2020 $Q_\alpha$ values across heavy ground-state emitters spanning $24$ orders of magnitude in observed half-life, the bare $S_\alpha = 1$ formula reproduces all five open-shell nuclei within $0.14$--$0.40\;\mathrm{dex}$ while isolating the classic closed-shell spectroscopic hindrance at magic $N = 126$ (${}^{210}\mathrm{Po}$):

| Nuclide | $N$ | $Q_\alpha$ (MeV) | $T_{1/2}^{\mathrm{exp}}$ | $T_{1/2}^{\mathrm{WKB}}$ | $\log_{10}(T^{\mathrm{WKB}}/T^{\mathrm{exp}})$ | $S_\alpha^{\mathrm{emp}}$ |
|:--------|----:|-----------------:|-------------------------:|-------------------------:|-----------------------------------------------:|--------------------------:|
| ${}^{212}\mathrm{Po}$ | $128$ | $8.954$ | $2.94 \times 10^{-7}\;\mathrm{s}$ | $4.06 \times 10^{-7}\;\mathrm{s}$ | $+0.139$ | $1.38$ |
| ${}^{214}\mathrm{Po}$ | $130$ | $7.834$ | $1.64 \times 10^{-4}\;\mathrm{s}$ | $3.06 \times 10^{-4}\;\mathrm{s}$ | $+0.272$ | $1.87$ |
| ${}^{222}\mathrm{Rn}$ | $136$ | $5.590$ | $3.30 \times 10^{5}\;\mathrm{s}$ | $5.95 \times 10^{5}\;\mathrm{s}$ | $+0.256$ | $1.80$ |
| ${}^{226}\mathrm{Ra}$ | $138$ | $4.871$ | $5.05 \times 10^{10}\;\mathrm{s}$ | $1.10 \times 10^{11}\;\mathrm{s}$ | $+0.338$ | $2.18$ |
| ${}^{238}\mathrm{U}$ | $146$ | $4.270$ | $1.41 \times 10^{17}\;\mathrm{s}$ | $3.58 \times 10^{17}\;\mathrm{s}$ | $+0.405$ | $2.54$ |
| ${}^{210}\mathrm{Po}$ | $126$ | $5.408$ | $1.20 \times 10^{7}\;\mathrm{s}$ | $6.61 \times 10^{5}\;\mathrm{s}$ | $-1.257$ | $0.0553$ |

Two parameter-free mechanisms govern the observed preformation drop $S_\alpha^{\mathrm{emp}}({}^{210}\mathrm{Po}) \approx 0.0553$ across the $N = 126$ closure of Maria Goeppert Mayer (1949) \cite{mayer1949} and Otto Haxel, J. Hans D. Jensen, and Hans E. Suess (1949):

1. **Mayer--Jensen seniority pair projection.** Above $N = 126$, coherent pairing across the open valence shell enhances two-neutron transfer, whereas at closed $N = 126$ (${}^{210}_{84}\mathrm{Po}_{126} \to {}^{206}_{82}\mathrm{Pb}_{124} + \alpha$) neutron superfluidity is quenched and the cluster draws two valence protons from $1h_{9/2}^2$ ($2 j_p + 1 = 10$) together with two hole neutrons from $3p_{1/2}^{-2}$ ($2 j_n + 1 = 2$). The joint $J = 0$ single-subshell projection is

$$
  S_{\mathrm{MJ}}^{(\pi \otimes \nu)}
  = \frac{1}{(2 j_p + 1)(2 j_n + 1)}
  = \frac{1}{10 \times 2}
  = 0.0500,
$$

matching $S_\alpha^{\mathrm{emp}} \approx 0.0553$ to $-0.044\;\mathrm{dex}$ and predicting $T_{1/2}({}^{210}\mathrm{Po}) = T_{1/2}^{\mathrm{WKB}} / S_{\mathrm{MJ}}^{(\pi \otimes \nu)} \approx 1.32 \times 10^{7}\;\mathrm{s}$ ($+0.044\;\mathrm{dex}$ from observation).

2. **Shell-kink chemical-potential barrier.** By the derivative-discontinuity theorem of John P. Perdew, Robert G. Parr, Mel Levy, and Jose L. Balduz Jr. (1982), a shell closure is a convex-cone vertex kink where the two-neutron shadow price jumps by $\Delta_{\mathrm{shell}}(126)$. Internal cluster formation across the pion-Compton range $r_\pi = \hbar c / m_{\pi^\pm}$ carries WKB attenuation $\exp(-2\sqrt{2\mu_\alpha\Delta_{\mathrm{shell}}}\,r_\pi / \hbar c)$. Using the categorical Compton oscillator spacing $\hbar\omega_{\mathrm{QOU}}(210) = [m_e / (q_0 - 1)^2]\,210^{-1/3} \approx 7.11\;\mathrm{MeV}$ gives $S_{\mathrm{kink}} \approx 0.0381$ ($-0.162\;\mathrm{dex}$), whereas the empirical two-neutron separation jump $S_{2n}(84,126) - S_{2n}(84,128) \approx 4.07\;\mathrm{MeV}$ gives $S_{\mathrm{kink}} \approx 0.0845$ ($+0.184\;\mathrm{dex}$), bracketing $S_\alpha^{\mathrm{emp}}$ without free parameters.

## Sensitivity to internally derived $Q_\alpha$

Replacing experimental mass differences by differences of the smooth face-centred cubic ($k = 12$, $(111)$ surface deficit $a_S / a_V = 3/4$) standard-channel [Borromean baryon](#def:borromean-baryon) binding Hamiltonian plus $B_\alpha^{\mathrm{QOU}} = 64 m_e G \approx 29.96\;\mathrm{MeV}$ yields $Q_\alpha^{\mathrm{FCC}}({}^{238}\mathrm{U}) \approx 3.966\;\mathrm{MeV}$ versus $4.270\;\mathrm{MeV}$ observed ($\Delta Q_\alpha = -0.304\;\mathrm{MeV}$). Because the Geiger--Nuttall slope reaches $\partial\log_{10} T_{1/2} / \partial Q_\alpha \approx -8.52\;\mathrm{dex}/\mathrm{MeV}$ at ${}^{238}\mathrm{U}$ (and $-2.39$ to $-6.63\;\mathrm{dex}/\mathrm{MeV}$ across ${}^{212}\mathrm{Po}$--${}^{226}\mathrm{Ra}$), that $0.30\;\mathrm{MeV}$ offset shifts $T_{1/2}({}^{238}\mathrm{U})$ by $+3.15\;\mathrm{dex}$, while omitting discrete shell-closure binding terms near $N = 126$ shifts $Q_\alpha$ by several MeV and $T_{1/2}$ by over $30\;\mathrm{dex}$. Sub-dex half-life prediction from internal nuclear masses alone therefore requires $\sim 0.05\;\mathrm{MeV}$ ($30\;\mathrm{ppm}$) shell-resolved binding accuracy.
