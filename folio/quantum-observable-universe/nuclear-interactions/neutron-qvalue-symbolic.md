**Conditional on Borromean quark conjecture.**
*The $Q$-value of free neutron $\beta^-$-decay $n \to p + e^- + \bar\nu_e$ is derived symbolically from the categorical three-calibration inputs $m_e$ ($H^0$) and $q_0$ ($H^1$). The value $\mathfrak{Q}_\beta(n)$ ($H^2$) is the $\beta$-decay datum being predicted, not used as input.*

## Single-wrap normal-form computation

A single wrap of typed crossings in $H_3(q)$ represents the proton and neutron. Let $h = q - q^{-1}$. A $uu$ crossing is $\sigma$, a $dd$ crossing is $\sigma^{-1} = \sigma - h$, and a mixed $ud$ crossing is the average $\tfrac12(\sigma + \sigma^{-1}) = \sigma - \tfrac h2$.

This typed-crossing assignment is the only input in the construction that tells $u$ from $d$. It is a definition, not a derived result. No weight-preserving operator that commutes with the isospin lowering operator $F_3$ separates $uud$ from $udd$ beyond the pivot factor.

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

The energy scale $E_0 = m_e / \bigl(q_0(q_0 - 1)(1 - \hbar_q^2)\bigr)$, with $\hbar_q = 1 - q_0^{-1}$, converts dimensionless differences to MeV. This tower-summed form is the canonical energy scale, though the first-principles derivation of its geometric series remains open. The order-zero form $m_e/(q_0(q_0-1))$ is $0.98\%$ smaller. The functional applied to $\Delta = \mathrm{net}(n) - \mathrm{net}(p) = \tfrac{h^2}{2}\gamma - \tfrac{h}{2}\sigma_0 - \tfrac{h}{2}\sigma_1$ is the Markov trace at $z = q^3/(q^2+1)$, which sends $\gamma \mapsto 1$ and $\sigma_i \mapsto z$:

$$
  \mathfrak{Q}_\beta
  =
  \bigl|\mathrm{tr}_M(\Delta)\bigr| \times E_0
  =
  \Bigl|\frac{h^2}{2} - h\,z\Bigr|\,\frac{m_e}{q(q-1)(1-\hbar_q^2)}.
$$

At $z = q^3/(q^2+1)$ the sign block $(1^3)$ has trace weight $0$, so $\mathrm{tr}_M$ evaluates $\Delta$ modulo the trace radical. Although $\Delta$ has a non-zero sign-block projection (every $\sigma_i$ acts there by $-q^{-1}$, giving $\tfrac{h^2}{2} + \tfrac{h}{q} = \tfrac12(q^2 - q^{-2})$), that component lies in the radical and every representative with the same two-row projection yields the same value.

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

The $-333.2$ keV miss is reported as it stands. With the order-zero $E_0$ the same trace gives $0.4447$ MeV ($-43.16\%$). The $z = q^3/(q^2+1)$ $c_k$ ladder that would correct this base is not yet derived, and a cosine phase cannot close it, because $\cos\alpha \le 1$ while the base needs a factor above $1$ ([cos-resummation](#prop:q-beta-cos-resummation)).

The value scored on the L2 scorecard is not this one. The scored $\mathfrak{Q}_\beta$ applies the $T^3$ weight split of the $z = q^3/(q^2+1)$ trace to the $\gamma\gamma$ base $V^3 = (\sigma_0\sigma_1^{-1})^3$:

$$
  \mathfrak{Q}_\beta^{\mathrm{scored}}
  =
  \bigl|\varepsilon_{\mathrm{flavour}}(V^3)\bigr|\,E_0
  =
  \frac{(q_0^2-1)\,\lvert P(q_0)\rvert}{q_0^4\,(q_0^2+1)^3}\,E_0
  \approx 0.3254 \text{ MeV}
  \qquad (-58.40\%),
$$

with $P(q) = q^{12} - 3q^{10} + 3q^8 - 5q^6 + 3q^4 - 3q^2 + 1$. The $\Delta$ value $0.4491$ MeV above is kept as an unscored comparison. Read as $\mathfrak{Q}_\beta$, the scored value gives $\mathfrak{m}_n - \mathfrak{m}_p = \mathfrak{Q}_\beta + m_e \approx 0.8364$ MeV ($-35.3\%$).

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

The algebraic identity is exact, but $z = 1$ does not satisfy the two-row Markov condition $y_{(1^3)}(z) = 0$. The $+0.17\%$ figure is therefore kept for comparison only and is not the prediction.

## Relation to the transfer-matrix eigenfunction form

The retired Form A (the normal-form coordinate sum, i.e. the trace at $z = 1$) is related to the transfer-matrix log-ratio form (Form B) by the Markov–Jones normalization $z$:

$$
  \mathfrak{Q}_\beta^{\mathrm{A}}
  \;=\;
  \mathfrak{Q}_\beta^{\mathrm{B}} \cdot \Bigl(1 + \tfrac{(z-1)\,h}{2} + O(h^2)\Bigr).
$$

This relates the two forms to each other. It does not make either one the canonical base, which is the Markov trace at $z = q^3/(q^2+1)$ above.
