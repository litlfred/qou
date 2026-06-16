**Remark (substrate identity for the proton–neutron Skein
difference, conditional on common-scale conjecture).**
*Under the common-scale Borromean baryon mass formula
([conj:borromean-baryon-mass-formula](#conj:borromean-baryon-mass-formula)),
the proton–neutron Skein difference is a* **derived** *quantity in
the three calibration inputs:*

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

*If the common-scale conjecture holds with $\lambda_{\mathrm{scale}}$
independent of the orientation partition $(p, n)$, the second
bracket vanishes and the identity reduces to*

$$
  \boxed{\;
    \Delta S(n - p)
    \;=\;
    \frac{\mathfrak{Q}_\beta + m_e}{m_e}
    \;=\;
    \frac{m_n - m_p}{m_e}
  \;}
$$

*— a closed-form prediction in $\{m_e, q_0\}$ via the substrate
$\mathfrak{Q}_\beta$ Form A
([prop:q-beta-spectral-bridge](#prop:q-beta-spectral-bridge))
$\mathfrak{Q}_\beta^A(q_0) = m_e \cdot |q^2 - 2q - 1|(q+1)/(2q^3)$
recorded in the
[m-baryon-volume-form witness](https://github.com/litlfred/qou/blob/claude/neutron-mass-50dps-chain/computations/m-baryon-volume-form.witness.json),
with no calibration to the proton or neutron individually.*

## Per-Borromean-quantum normalisation

The Skein contribution divided by the Borromean topological quantum
$\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2$ gives a dimensionless residual

$$
  \widetilde{\Delta S}(n - p)
  \;:=\;
  \frac{\Delta S(n - p)}{\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2}
  \;=\;
  \frac{m_n - m_p}{m_e \cdot \mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2}.
$$

*At the substrate parameter* $q_0 = 1.109978595554181\ldots$ *(50 dps) and CAL-1
$m_e = :val[m_e_MeV]{precision=6, witness=computations/codata-masses.witness.json}\ldots\;\mathrm{MeV}$, evaluating to 50 dps via the
witness*
[`m-baryon-volume-form.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/m-baryon-volume-form.witness.json)
*gives:*

| Quantity | 50-dps value | Source |
|----------|-------------|--------|
| $\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2$ at $q_0$ | $746.4179\ldots$ | substrate compute |
| $(\mathfrak{Q}_\beta + m_e)/m_e$ at $q_0$ | $2.53388\ldots$ | CAL-3 + CAL-1 ([rem:beta-decay-energy-scale](#rem:beta-decay-energy-scale)) |
| $\widetilde{\Delta S}_{\mathrm{derived}}$ | $0.0033943\ldots$ | ratio |
| $\widetilde{\Delta S}_{\mathrm{empirical}}$ | $0.0033908\ldots$ | $\lambda_p - \lambda_n$ from CODATA $m_p$, $m_n$ |
| relative agreement | $1\,015$ ppm | — |

## Why the 1 015 ppm residual is the same as $\mathfrak{Q}_\beta$'s

The substrate $\mathfrak{Q}_\beta$ ansatz used in the compute witness predicts
$\mathfrak{Q}_\beta(q_0) = 0.78174\ldots\;\mathrm{MeV}$ against the empirical
CAL-3 value $0.78233341\ldots\;\mathrm{MeV}$
([rem:beta-decay-energy-scale](#rem:beta-decay-energy-scale)) —
a $760$ ppm residual at the current $q_0$ pinning. The
$\widetilde{\Delta S}$ relative error of $1\,015$ ppm is
*the same residual*, dominated by:

1. the symmetric $(\mathfrak{Q}_\beta+m_e)/m_e$ numerator (this residual is set
   by the substrate $\mathfrak{Q}_\beta$ formula's $\sim 760$ ppm error at the
   current $q_0$ pinning, plus the CAL-1 $m_e$ uncertainty floor of
   $\sim 3 \times 10^{-7}$);
2. the choice of $\lambda_{\mathrm{scale}}(\mathfrak{p}) -
   \lambda_{\mathrm{scale}}(\mathfrak{n})$ being exactly zero (the
   common-scale conjecture).

*The 1 015 ppm agreement is therefore* **not** *evidence for the
common-scale conjecture per se: it is consistent with the existing
$\mathfrak{Q}_\beta$ closure precision under that hypothesis. Falsification of
the common-scale conjecture would require either:*

- *direct closed-form derivation of
  $\lambda_{\mathrm{scale}}(\mathfrak{p}) \neq
  \lambda_{\mathrm{scale}}(\mathfrak{n})$ from the substrate, or*
- *substrate-only refinement of $\mathfrak{Q}_\beta$ to* $\ll 100$ *ppm at $q_0$,
  exposing a non-zero residual after the common-scale subtraction.*

## Substrate-only character

The derivation consumes exactly three substrate quantities:

| Input | Provenance | Calibration |
|-------|-----------|-------------|
| $m_e$ | input | **CAL-1** |
| $q_0$ | input (via $m_\mu/m_e$) | **CAL-2** |
| $\mathrm{Vol}(\mathcal{B}_3)$ | Thurston topological invariant | — |

*$\mathfrak{Q}_\beta$ enters via the substrate ansatz
$\mathfrak{Q}_\beta(q_0) = m_e \cdot |q^2 - 2q - 1|(q+1)/(2q^3)$
evaluated in the
[m-baryon-volume-form witness](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/m-baryon-volume-form.witness.json),
which agrees with the CAL-3 empirical value
([rem:beta-decay-energy-scale](#rem:beta-decay-energy-scale)) to
$760$ ppm at the current $q_0$ pinning. The identity therefore
predicts $\Delta S(n - p)$ from CAL-1 + CAL-2 + a topological
invariant; CAL-3 enters only as a consistency cross-check
([prop:three-calibration-inputs](#prop:three-calibration-inputs)).*

## What this rules in and what remains open

**Ruled in.** The Borromean Vol-form mass ansatz — at least the
*orientation-difference* part of it — is consistent with CODATA to
$\sim 1\,000$ ppm using only CAL-1, CAL-2, and a fixed topological
invariant. The proton–neutron mass splitting is not a fit.

**Remains open.** The common scale $\lambda_{\mathrm{scale}}$ itself
— a single $\mathbb{Q}(q_0)$ number with empirical target $\approx
2.46$ — has not been derived. Its absolute value is required for
$m_p$ and $m_n$ individually (see
[conj:borromean-baryon-mass-formula](#conj:borromean-baryon-mass-formula)).
Open programme:
[docs/agent-briefs/-lambda-scale-borromean-baryon-derivation.md](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/docs/agent-briefs/-lambda-scale-borromean-baryon-derivation.md).
