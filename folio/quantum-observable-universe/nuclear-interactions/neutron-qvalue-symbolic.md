**Proposition (conditional on Borromean quark conjecture — $\mathfrak{Q}_\beta$ of free neutron $\beta^{-}$-decay).**
*The $Q$-value of free neutron $\beta^-$-decay $n \to p + e^- + \bar\nu_e$ is derived symbolically from the categorical three-calibration inputs $m_e$ ($H^0$) and $q_0$ ($H^1$). The value $\mathfrak{Q}_\beta(n)$ ($H^2$) is the $\beta$-decay datum being predicted rather than used as input.*

## Single-wrap normal-form computation

A single wrap of typed crossings in $H_3(q)$ represents the proton and neutron. Let $h = q - q^{-1}$. A $uu$ crossing is $\sigma$, a $dd$ crossing is $\sigma^{-1} = \sigma - h$, and a mixed $ud$ crossing is the average $\tfrac12(\sigma + \sigma^{-1}) = \sigma - \tfrac h2$.

This typed-crossing assignment is the only input in the construction that tells $u$ from $d$. It enters as a definition rather than a derived result. No weight-preserving operator that commutes with the isospin lowering operator $F_3$ separates $uud$ from $udd$ beyond the pivot factor.

**Proton** $[u, u, d]$: the typed crossing operators give:
$$
  L_+ - \tfrac{h}{2}\sigma_0
$$

**Neutron** $[u, d, d]$:
$$
  L_+ - h\sigma_0 - \tfrac{h}{2}\sigma_1 + \tfrac{h^2}{2}\gamma
$$

## Symbolic $\Delta$

$$
  \Delta
  =
  \mathrm{net}(n) - \mathrm{net}(p)
  =
  \tfrac{h^2}{2}\gamma - \tfrac{h}{2}\sigma_0 - \tfrac{h}{2}\sigma_1.
$$

The $L_+$ and $L_-$ contributions cancel exactly because both nucleons share the same Hopf content at single wrap. The entire $Q$-value arises from the vacuum channel and the two crossing channels.

## $Q$-value from two inputs

The energy scale $E_0 = m_e / \bigl(q_0(q_0 - 1)(1 - \hbar_q^2)\bigr)$, with $\hbar_q = 1 - q_0^{-1}$, converts dimensionless differences to MeV. This geometric-series tower factor $(1 - \hbar_q^2)^{-1}$ increases the order-zero scale $m_e/(q_0(q_0-1))$ by $0.98\%$, while a first-principles derivation of that geometric-series prefactor is conjectural. Evaluating $\Delta = \mathrm{net}(n) - \mathrm{net}(p) = \tfrac{h^2}{2}\gamma - \tfrac{h}{2}\sigma_0 - \tfrac{h}{2}\sigma_1$ under the convention-D Markov trace at $z_D = q^3/(q^2+1)$, which sends $\gamma \mapsto 1$ and $\sigma_i \mapsto z_D$, gives:

$$
  \mathfrak{Q}_\beta
  =
  \bigl|\mathrm{tr}_{z_D}(\Delta)\bigr| \times E_0
  =
  \Bigl|\frac{h^2}{2} - h\,z_D\Bigr|\,\frac{m_e}{q(q-1)(1-\hbar_q^2)}.
$$

Under convention D the sign block $(1^3)$ has trace weight $0$, so $\mathrm{tr}_{z_D}$ sees $\Delta$ only modulo the radical of the trace. $\Delta$ does have a sign-block part: every $\sigma_i$ acts there by $-q^{-1}$, so $\Delta$ acts by $\tfrac{h^2}{2} + \tfrac{h}{q} = \tfrac12(q^2 - q^{-2})$. That part is invisible to $\mathrm{tr}_{z_D}$, and every element with the same image on the surviving blocks gives the same value, so no number depends on the choice of lift.

## Numerical evaluation and Convention-D hierarchy

At $q_0 \approx 1.110$ and $m_e \approx 0.511$ MeV, the single-wrap bare Convention-D trace evaluates to:

$$
  \mathfrak{Q}_\beta^{z_D,\text{single-wrap}}
  =
  0.4491 \text{ MeV}
  \qquad
  (\text{CODATA: } 0.7823 \text{ MeV},
  \quad -42.59\%).
$$

With the order-zero $E_0 = m_e/(q_0(q_0-1))$ the same single-wrap trace gives $0.4447$ MeV ($-43.16\%$). Reselecting the nucleon word over the extended $\{V, V^{-1}, L_+, L_-\}$ generator set raises the bare Convention-D trace to $0.6515$ MeV ($-16.72\%$, corresponding to $m_n \approx 939.435$ MeV, $-139$ ppm).

The **all-order Convention-D generating function** $\mathcal{G}_D(u; q)$ and cumulant coefficients $c_2^{(D)} = -1$, $c_3^{(D)}(q) = -\frac{3q^2-1}{2q(q^2+1)}$, and $c_4^{(D)}(q)$ are derived in closed form (converging geometrically with radius $R_u \approx 0.369$), alongside the GPMT-screened axial coupling $g_A(q_0) \approx 1.2690$ ($-0.50\%$ vs.\ PDG). Two structural facts separate the bare trace $\mathrm{tr}_{z_D}(\Delta)$ from the full $0.7823$ MeV decay energy:

1. **Order of the $c_k^{(D)}$ series refinement:** Multiplying a base value by $(1 + c_2^{(D)} u^2 + c_3^{(D)} u^3 + \cdots)$ at $u = b\hbar_q^2 \approx 0.00852$ supplies an $O(10^{-4})$ ($< 0.01\%$) higher-order series refinement, whereas a cosine phase satisfies $\cos\alpha \le 1$ ([cos-resummation](#prop:q-beta-cos-resummation)).
2. **Unbraided single-wrap $(2,1)$ trace cancellation and GPMT $(1,1,1)$ sign-block closure on the 11-crossing Borromean nucleon words:** On the unbraided single-wrap difference $\Delta = \tfrac{1}{2}h^2\gamma - \tfrac{1}{2}h(\sigma_0 + \sigma_1)$, the two-dimensional Hoefsmit standard representation $(2,1)$ has exact opposite eigenvalues $\pm h/2$, so $\mathrm{tr}_{(2,1)}(\Delta) = 0$ identically while the bare Convention-D trace $\mathrm{tr}_{z_D}$ assigns weight $y_{(1,1,1)}(z_D) = 0$ to the antisymmetric baryon sign block $(1,1,1)$ ($0.4491$ MeV, $-42.59\%$). On the 11-crossing Borromean nucleon normal forms, by contrast, $\chi_{(2,1)}(n - p) < 0$ is non-vanishing and $\chi_{(1,1,1)}(n - p) < 0$ shares the sign of $\chi_{(3)}(n - p) < 0$. Restoring the antisymmetric baryon sign block $(1,1,1)$ via its positive Geer–Patureau-Mirand–Turaev (GPMT) modified quantum dimension $|d_{\mathrm{mod}}(1,1,1)| = \frac{1}{[2]_q[3]_q}$ together with $\mathcal{G}_D(u; q)$ and the connected Borromean $V^3$ QED splitting ($\Delta M_{\mathrm{QED}}^{\mathrm{Bor}} = -0.332$ keV) yields a parameter-free $\mathfrak{Q}_\beta = 0.77065$ MeV ($-1.49\%$; $\Delta m_{np} = 1.28101$ MeV, $-0.95\%$) on the interleaved ordering and $\mathfrak{Q}_\beta = 0.78682$ MeV ($+0.57\%$; $0.78616$ MeV, $+0.49\%$ before $\mathcal{G}_D$; $\Delta m_{np} = 1.29716$ MeV, $+0.30\%$) on the generator-grouped ordering, bracketing CODATA $0.78233$ MeV ($\Delta m_{np} = 1.29333$ MeV) to $\sim 0.5\%\text{--}1.5\%$ with zero fitted parameters (while the Kashiwara $b^2$ Convention-D $N=2$ resummation evaluates to $0.78247$ MeV, $+178$ ppm; $+46.9$ ppm with the connected two-term Borromean $V^3$ QED correction).

## Retired Form A (historical cross-check only)

Weighting every basis element by $1$, the Markov trace at $z = 1$, gives the coordinate sum

$$
  \Delta(\mathrm{net}) = \frac{h(h - 2)}{2},
  \qquad
  |\Delta(\mathrm{net})| \times E_0
  =
  \frac{m_e \cdot |q^2 - 2q - 1| \cdot (q+1)}{2q^3}
  \approx 0.7836 \text{ MeV} \quad (+0.17\%).
$$

The algebraic identity is exact, but $z = 1$ is not an admissible Markov parameter under convention D. The $+0.17\%$ figure is therefore kept for comparison only and is not the prediction.

## Relation to the transfer-matrix eigenfunction form

The retired Form A (the normal-form coordinate sum, i.e. the trace at $z = 1$) is related to the transfer-matrix log-ratio form (Form B) by the Markov–Jones normalization $z$:

$$
  \mathfrak{Q}_\beta^{\mathrm{A}}
  \;=\;
  \mathfrak{Q}_\beta^{\mathrm{B}} \cdot \Bigl(1 + \tfrac{(z-1)\,h}{2} + O(h^2)\Bigr).
$$

This relates the two forms to each other. It does not make either one the ruled base, which is the trace at $z_D$ above.
