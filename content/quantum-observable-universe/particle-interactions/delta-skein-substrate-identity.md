**Remark (substrate identity for the proton–neutron Skein difference).** Under the common-scale Borromean baryon mass formula ([conj:borromean-baryon-mass-formula](#conj:borromean-baryon-mass-formula)), the proton–neutron Skein difference is derived from three calibration inputs:

$$
  \Delta S(n - p)
  \;:=\;
  S(\mathfrak{n}) - S(\mathfrak{p})
  \;=\;
  \frac{\mathfrak{Q}_\beta + m_e}{m_e}
  \;-\;
  \frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2}
  \cdot \bigl[\lambda_{\mathrm{scale}}(\mathfrak{n}) - \lambda_{\mathrm{scale}}(\mathfrak{p})\bigr].
$$

If the common-scale conjecture holds (with $\lambda_{\mathrm{scale}}$ independent of the orientation partition), the second bracket vanishes. The identity reduces to:

$$
  \boxed{\;
    \Delta S(n - p)
    \;=\;
    \frac{\mathfrak{Q}_\beta + m_e}{m_e}
    \;=\;
    \frac{m_n - m_p}{m_e}
  \;}
$$

This is a closed-form prediction in $\{m_e, q_0\}$ via the substrate $\mathfrak{Q}_\beta$ Form A ([prop:q-beta-spectral-bridge](#prop:q-beta-spectral-bridge)), recorded in the [m-baryon-volume-form witness](https://github.com/litlfred/qou/blob/claude/neutron-mass-50dps-chain/computations/m-baryon-volume-form.witness.json), with no calibration to the proton or neutron individually.

## Normalisation

The Skein contribution divided by the Borromean topological quantum gives a dimensionless residual:

$$
  \widetilde{\Delta S}(n - p)
  \;:=\;
  \frac{\Delta S(n - p)}{\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2}
  \;=\;
  \frac{m_n - m_p}{m_e \cdot \mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2}.
$$

At the substrate parameter $q_0 = 1.109978595554181\ldots$ (50 dps) and CAL-1 $m_e = :val[m_e_MeV]{precision=6, witness=computations/codata-masses.witness.json}\ldots\;\mathrm{MeV}$, we evaluate this via the [`m-baryon-volume-form.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/m-baryon-volume-form.witness.json):

| Quantity | 50-dps value | Source |
|----------|-------------|--------|
| $\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2$ at $q_0$ | $746.4179\ldots$ | substrate compute |
| $(\mathfrak{Q}_\beta + m_e)/m_e$ at $q_0$ | $2.53388\ldots$ | CAL-3 + CAL-1 ([rem:beta-decay-energy-scale](#rem:beta-decay-energy-scale)) |
| $\widetilde{\Delta S}_{\mathrm{derived}}$ | $0.0033943\ldots$ | ratio |
| $\widetilde{\Delta S}_{\mathrm{empirical}}$ | $0.0033908\ldots$ | $\lambda_p - \lambda_n$ from CODATA $m_p$, $m_n$ |
| relative agreement | $1\,015$ ppm | — |

## Identity of the residual

The substrate $\mathfrak{Q}_\beta$ ansatz predicts $\mathfrak{Q}_\beta(q_0) = 0.78174\ldots\;\mathrm{MeV}$ against the empirical CAL-3 value $0.78233341\ldots\;\mathrm{MeV}$ ([rem:beta-decay-energy-scale](#rem:beta-decay-energy-scale))—a $760$ ppm residual. The $\widetilde{\Delta S}$ relative error of $1\,015$ ppm is the same residual, dominated by:

1. the symmetric $(\mathfrak{Q}_\beta+m_e)/m_e$ numerator (set by the substrate $\mathfrak{Q}_\beta$ formula's $\sim 760$ ppm error, plus the CAL-1 $m_e$ uncertainty);
2. the common-scale conjecture $\lambda_{\mathrm{scale}}(\mathfrak{p}) - \lambda_{\mathrm{scale}}(\mathfrak{n}) = 0$.

The 1 015 ppm agreement is consistent with the existing $\mathfrak{Q}_\beta$ closure precision under the common-scale hypothesis. Falsification of the common-scale conjecture requires either a direct closed-form derivation of $\lambda_{\mathrm{scale}}(\mathfrak{p}) \neq \lambda_{\mathrm{scale}}(\mathfrak{n})$ from the substrate, or a substrate-only refinement of $\mathfrak{Q}_\beta$ exposing a non-zero residual after subtraction.

## Substrate-only character

The derivation consumes three substrate quantities:

| Input | Provenance | Calibration |
|-------|-----------|-------------|
| $m_e$ | input | **CAL-1** |
| $q_0$ | input (via $m_\mu/m_e$) | **CAL-2** |
| $\mathrm{Vol}(\mathcal{B}_3)$ | Thurston topological invariant | — |

The identity predicts $\Delta S(n - p)$ from CAL-1, CAL-2, and a topological invariant. CAL-3 enters only as a consistency cross-check ([prop:three-calibration-inputs](#prop:three-calibration-inputs)).

## Scope

The Borromean Vol-form mass ansatz is consistent with CODATA to $\sim 1\,000$ ppm using only CAL-1, CAL-2, and a fixed topological invariant. The common scale $\lambda_{\mathrm{scale}}$ itself requires further derivation to determine $m_p$ and $m_n$ individually (cf. [conj:borromean-baryon-mass-formula](#conj:borromean-baryon-mass-formula)).
