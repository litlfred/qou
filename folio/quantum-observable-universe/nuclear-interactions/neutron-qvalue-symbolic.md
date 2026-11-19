**Proposition (conditional on Borromean quark conjecture — $\mathfrak{Q}_\beta$ of free neutron $\beta^{-}$-decay).**
*We derive the $Q$-value of free neutron $\beta^-$-decay $n \to p + e^- + \bar\nu_e$ symbolically from the categorical three-calibration inputs $m_e$ ($H^0$) and $q_0$ ($H^1$). The value $\mathfrak{Q}_\beta(n)$ ($H^2$) is the $\beta$-decay datum being predicted, not used as input.*

## Single-wrap normal-form computation

A single wrap of typed crossings in $H_3(q)$ represents the proton and neutron. Let $h = q - q^{-1}$. A $uu$ crossing is $\sigma$, a $dd$ crossing is $\sigma^{-1} = \sigma - h$, and a mixed $ud$ crossing is the average $\tfrac12(\sigma + \sigma^{-1}) = \sigma - \tfrac h2$.

This typed-crossing assignment is the only input in the construction that tells $u$ from $d$. It is a definition, not a derived result. No weight-preserving operator that commutes with the isospin lowering operator $F_3$ separates $uud$ from $udd$ beyond the pivot factor (Lean `commutant_trace_eq` in `QOU/BraidsAndKnots/NucleonIsospinExclusions.lean`).

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

The energy scale $E_0 = m_e / \bigl(q_0(q_0 - 1)(1 - \hbar_q^2)\bigr)$, with $\hbar_q = 1 - q_0^{-1}$, converts dimensionless differences to MeV. This tower-summed form is canonical under the full-tower ruling; the derivation of its series is still open. The order-zero form $m_e/(q_0(q_0-1))$ is $0.98\%$ smaller. The functional applied to $\Delta = \mathrm{net}(n) - \mathrm{net}(p) = \tfrac{h^2}{2}\gamma - \tfrac{h}{2}\sigma_0 - \tfrac{h}{2}\sigma_1$ is the Markov trace at $z_D = q^3/(q^2+1)$ (convention D, owner ruling 2026-09-08), which sends $\gamma \mapsto 1$ and $\sigma_i \mapsto z_D$:

$$
  \mathfrak{Q}_\beta
  =
  \bigl|\mathrm{tr}_{z_D}(\Delta)\bigr| \times E_0
  =
  \Bigl|\frac{h^2}{2} - h\,z_D\Bigr|\,\frac{m_e}{q(q-1)(1-\hbar_q^2)}.
$$

Under convention D the sign block $(1^3)$ has trace weight $0$, so $\mathrm{tr}_{z_D}$ sees $\Delta$ only modulo the radical of the trace. $\Delta$ does have a sign-block part: every $\sigma_i$ acts there by $-q^{-1}$, so $\Delta$ acts by $\tfrac{h^2}{2} + \tfrac{h}{q} = \tfrac12(q^2 - q^{-2})$. That part is invisible to $\mathrm{tr}_{z_D}$, and every element with the same image on the surviving blocks gives the same value, so no number depends on the choice of lift.

## Numerical evaluation

At $q_0 \approx 1.110$ and $m_e \approx 0.511$ MeV:

$$
  \mathfrak{Q}_\beta
  =
  0.4491 \text{ MeV}
  \qquad
  (\text{CODATA: } 0.7823 \text{ MeV},
  \quad -42.59\%).
$$

The $-333.2$ keV miss is reported as it stands. With the order-zero $E_0$ the same trace gives $0.4447$ MeV ($-43.16\%$). The convention-D $c_k$ ladder that would correct this base is not yet derived, and a cosine phase cannot close it, because $\cos\alpha \le 1$ while the base needs a factor above $1$ ([cos-resummation](#prop:q-beta-cos-resummation)).

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
