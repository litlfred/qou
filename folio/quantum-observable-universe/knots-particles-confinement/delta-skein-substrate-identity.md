**Remark (substrate identity for the proton–neutron Skein difference).** Under the common-scale Borromean baryon mass formula, the proton–neutron Skein difference is derived from three calibration inputs:

$$
  \Delta S(n - p)
  \;:=\;
  S(\mathfrak{n}) - S(\mathfrak{p})
  \;=\;
  \frac{\mathfrak{Q}_\beta + m_e}{m_e}
  \;-\;
  \frac{1}{m_e}
  \bigl[\mathfrak{m}_{\mathcal{B}_3}^{(\mathfrak{n})} - \mathfrak{m}_{\mathcal{B}_3}^{(\mathfrak{p})}\bigr],
$$

where $\mathfrak{m}_{\mathcal{B}_3}^{(B)}$ is the a-priori baryon-dependent common Borromean term of the [Borromean baryon mass formula](#conj:borromean-baryon-mass-formula). If the common-scale conjecture holds, the second bracket vanishes. The identity reduces to:

$$
  \boxed{\;
    \Delta S(n - p)
    \;=\;
    \frac{\mathfrak{Q}_\beta + m_e}{m_e}
    \;=\;
    \frac{m_n - m_p}{m_e}
  \;}
$$

This is a closed-form prediction in $\{m_e, q_0\}$ via the substrate $\mathfrak{Q}_\beta$ Form A, recorded in the witness file, with no calibration to the proton or neutron individually.

## Normalisation

The Skein contribution divided by the Borromean topological quantum gives a dimensionless residual:

$$
  \widetilde{\Delta S}(n - p)
  \;:=\;
  \frac{\Delta S(n - p)}{\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2}
  \;=\;
  \frac{m_n - m_p}{m_e \cdot \mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2}.
$$

At the substrate parameter $q_0 = 1.109978595642739\ldots$ (muon pin, 16 dps) and CAL-1 $m_e = {{ qou.library.codata-2022.electron-mass-energy-equivalent-in-mev | precision: 6 }}\;\text{MeV}\ldots\;\mathrm{MeV}$, this evaluates to:

| Quantity | 50-dps value | Source |
|----------|-------------|--------|
| $\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2$ at $q_0$ | $746.4179\ldots$ | substrate compute |
| $(\mathfrak{Q}_\beta + m_e)/m_e$ at $q_0$ | $2.53388\ldots$ | CAL-2 proxy $\mathfrak{Q}_\beta$ + CAL-1 |
| $\widetilde{\Delta S}_{\mathrm{derived}}$ | $0.0033943\ldots$ | ratio |
| $\widetilde{\Delta S}_{\mathrm{empirical}}$ | $0.0033908\ldots$ | per-baryon common-term difference implied by CODATA $m_p$, $m_n$ |
| relative agreement | $1\,015$ ppm | — |

## Identity of the residual

The substrate $\mathfrak{Q}_\beta$ ansatz predicts $\mathfrak{Q}_\beta(q_0) = 0.78174\ldots\;\mathrm{MeV}$ against the empirical $\mathfrak{Q}_\beta = P_{\mathrm{skew}}^{\beta} = 0.78233341\ldots\;\mathrm{MeV}$—a $760$ ppm residual. The $\widetilde{\Delta S}$ relative error of $1\,015$ ppm is the same residual, dominated by:

1. the symmetric $(\mathfrak{Q}_\beta+m_e)/m_e$ numerator;
2. the common-scale conjecture $\mathfrak{m}_{\mathcal{B}_3}^{(\mathfrak{p})} - \mathfrak{m}_{\mathcal{B}_3}^{(\mathfrak{n})} = 0$.

The 1 015 ppm agreement is consistent with the $\mathfrak{Q}_\beta$ closure precision under the common-scale hypothesis. Falsification of the common-scale conjecture requires either a direct closed-form derivation of $\mathfrak{m}_{\mathcal{B}_3}^{(\mathfrak{p})} \neq \mathfrak{m}_{\mathcal{B}_3}^{(\mathfrak{n})}$ from the substrate, or a substrate-only refinement of $\mathfrak{Q}_\beta$ exposing a non-zero residual after subtraction.

## Substrate-only character

The derivation consumes three substrate quantities:

| Input | Provenance | Calibration |
|-------|-----------|-------------|
| $m_e$ | input | **CAL-1** |
| $q_0$ | input (via $m_\mu/m_e$) | **CAL-2** |
| $\mathrm{Vol}(\mathcal{B}_3)$ | Thurston topological invariant | — |

The identity predicts $\Delta S(n - p)$ from CAL-1, CAL-2, and a topological invariant. CAL-2 is overdetermined: its modulus is pinned here through the mass proxy $m_\mu/m_e$, so the empirical $Q$-value proxy $\mathfrak{Q}_\beta$ is not a further input but a consistency cross-check on the same calibration. CAL-3 ($P_{\mathrm{avg}}^{\pi}$, proxy $m_\pi$) does not enter at all.

## Scope

The Borromean mass ansatz is consistent with CODATA to $\sim 1\,000$ ppm using only CAL-1, CAL-2, and a fixed topological invariant. The common Borromean term $\mathfrak{m}_{\mathcal{B}_3}$ requires further derivation to determine $m_p$ and $m_n$ individually.
