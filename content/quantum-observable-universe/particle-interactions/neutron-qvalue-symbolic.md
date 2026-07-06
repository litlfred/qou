**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark) — $\mathfrak{Q}_\beta$ of free neutron $\beta^{-}$-decay).**
The $Q$-value of free neutron $\beta^-$-decay
$n \to p + e^- + \bar\nu_e$ is derived symbolically from
the categorical three-calibration inputs $m_e$ ($H^0$) and $q_0$ ($H^1$,
fixed by $m_\mu/m_e$) — $\mathfrak{Q}_\beta(n)$ ($H^2$) is the
$\beta$-decay datum being predicted, not used as input
([three-calibration discipline](#prop:three-calibration-discipline)).

## Single-wrap NF computation

The proton and neutron are each represented by a single wrap
of typed crossings in $H_3(q)$.  Write $h = q - q^{-1}$.

**Proton** $[u, u, d]$: the typed crossing operators at
generators $\sigma_0$ and $\sigma_1$ give:

$$
  \sigma_0 \cdot \bigl(\sigma_1 - \tfrac{h}{2}\mathbf{1}\bigr)
  = L_+ - \tfrac{h}{2}\sigma_0
$$

| $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | $L_-$ | $e^-$ | net |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $-h/2$ | $0$ | $1$ | $0$ | $0$ | $1 - h/2$ |

**Neutron** $[u, d, d]$:

$$
  \bigl(\sigma_0 - \tfrac{h}{2}\mathbf{1}\bigr)
  \cdot
  \bigl(\sigma_1 - h\mathbf{1}\bigr)
  = L_+ - h\sigma_0 - \tfrac{h}{2}\sigma_1 + \tfrac{h^2}{2}\gamma
$$

| $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | $L_-$ | $e^-$ | net |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $h^2/2$ | $-h$ | $-h/2$ | $1$ | $0$ | $0$ | $1 - 3h/2 + h^2/2$ |

## Symbolic $\Delta(\text{net})$

$$
  \Delta(\mathrm{net})
  =
  \mathrm{net}(n) - \mathrm{net}(p)
  =
  \frac{h^2}{2} - h
  =
  \frac{h(h - 2)}{2}.
$$

Per basis element:

| $\Delta\gamma$ | $\Delta\sigma_0$ | $\Delta\sigma_1$ | $\Delta L_+$ | $\Delta L_-$ | $\Delta e^-$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $+h^2/2$ | $-h/2$ | $-h/2$ | $0$ | $0$ | $0$ |

The $L_+$ and $L_-$ contributions cancel exactly (both nucleons
have the same Hopf content at single wrap).  The entire
$Q$-value comes from the vacuum channel ($+h^2/2$), the two
crossing channels ($-h/2$ each), and no trefoil content.

In terms of $q$:

$$
  \Delta(\mathrm{net})
  =
  \frac{(q+1)(q-1)(q^2 - 2q - 1)}{2q^2}.
$$

## $Q$-value from two inputs

The energy scale $E_0 = m_e / (q_0(q_0 - 1))$
([energy scale](#rem:energy-scale-planck)) converts
dimensionless NF differences to MeV:

$$
  \mathfrak{Q}_\beta
  =
  |\Delta(\mathrm{net})| \times E_0
  =
  \frac{(2 - h) \cdot h}{2}
  \times
  \frac{m_e}{q(q-1)}.
$$

Substituting $h = q - q^{-1}$:

$$
  \mathfrak{Q}_\beta
  =
  \frac{m_e \cdot (2 - h) \cdot h}{2q(q-1)}
  =
  \frac{m_e \cdot |q^2 - 2q - 1| \cdot (q+1)}{2q^3}.
$$

## Numerical evaluation

At $q_0 = 1.109978595554181\ldots$ (50 dps) (from $m_\mu/m_e$) and
$m_e = :val[m_e_MeV]{precision=6, witness=computations/codata-masses.witness.json} \pm 0.00000000015$ MeV (CODATA 2022):

$$
  \mathfrak{Q}_\beta
  =
  0.7836 \text{ MeV}
  \qquad
  (\text{CODATA: } 0.7823 \text{ MeV},
  \quad +0.17\%,
  \quad +1.3 \text{ keV}).
$$

The $1.3$ keV discrepancy ($0.17\%$) is the brane tower
correction to the energy scale $E_0$: the derived
$E_0 = m_e/(q(q-1))$ is the single-level (Planck-tick)
approximation, while the exact tower-summed $E_0$ would
absorb the $0.17\%$ residual.

**This is a 2-input closed form *conditional on the ansatz*
$\mathfrak{Q}_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$** (stated
"by construction" in
[`pre-archimedean-derivation-chain.md`](../braids-and-knots/pre-archimedean-derivation-chain.md):391,
not derived from the canonical per-braid mass formula). No
hadronic calibration (neutron mass, proton mass, or $\mathfrak{Q}_\beta$
itself) is used in the closed form *given the ansatz*; the
+0.17% match is empirical evidence for the ansatz but does
not derive it. The functional standing of the relation — the
counit $\varepsilon$ used here versus the Markov trace
$\mathrm{tr}_M$ of the mass formula — is analysed in
[`prop:qbeta-counit-closed-form`](#prop:qbeta-counit-closed-form)
and [`rem:qbeta-counit-transition`](#rem:qbeta-counit-transition);
see also
[`docs/audits/-q-beta-net-ansatz-fitting-finding.md`](../../../docs/audits/-q-beta-net-ansatz-fitting-finding.md)
for the audit and resolution paths.

**Witness**: symbolic derivation verified at
$q_0 = 1.109978595554181$ from `q_parameter.py`.

## Relation to the transfer-matrix eigenfunction form

The closed form above (Form A, NF-counit basis) is equivalent to
the transfer-matrix log-ratio form
([prop:beta-decay-transfer-matrix](#prop:beta-decay-transfer-matrix))
up to the Markov–Jones normalization
$z = 1/(\sqrt q + 1/\sqrt q)$, with explicit bridge identity in
[prop:q-beta-spectral-bridge](#prop:q-beta-spectral-bridge):

$$
  \mathfrak{Q}_\beta^{\mathrm{A}}
  \;=\;
  \mathfrak{Q}_\beta^{\mathrm{B}} \cdot \Bigl(1 + \tfrac{(z-1)\,h}{2} + O(h^2)\Bigr).
$$

The two forms are **not competing predictions** — they are the same
observable in two bases. Form A is canonical here because the
single-wrap NF-counit reduces to a closed symbolic expression in
$q$; Form B is the natural eigenfunction basis for $N \geq 1$
brane-tower truncation analysis.
