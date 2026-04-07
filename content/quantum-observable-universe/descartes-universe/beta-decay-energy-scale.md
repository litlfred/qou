The Gröbner--Shirshov normal form coefficients are dimensionless Laurent
polynomials in $q$.  To connect them to observed energies we need
an **energy scale** $\mathbf{E}_0$ (in MeV) such that

$$
  |\Delta(\mathrm{net})| \times \mathbf{E}_0
  \;=\;
  Q_{\beta}
  \;=\;
  \mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} - \mathfrak{m}_{e}
  \;\approx\; 0.7823\;\text{MeV}.
$$

## Linearity

The transition $\Delta = \mathrm{NF}(\mathfrak{n}) -
\mathrm{NF}(\mathfrak{p})$ equals $\mathrm{NF}(\mathfrak{n} -
\mathfrak{p})$ because $\mathrm{NF}$ is coordinate extraction in
the Gröbner--Shirshov basis — a linear map on the 6-dimensional
vector space $H_3(q)$.

## Derivation (typed crossings)

From the witness (`free-neutron-decay.witness.json`, typed crossings):

- $\mathrm{net}(\mathfrak{n}) = +0.810835$, $\mathrm{net}(\mathfrak{p}) = +0.999125$
- $\Delta(\mathrm{net}) = -0.188291$

From CODATA 2022:

- $\mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} = 1.29333\;\text{MeV}$
- $\mathfrak{m}_{e} = 0.51100\;\text{MeV}$
- $Q_{\beta} = 0.78233\;\text{MeV}$

Therefore:

$$
  \mathbf{E}_0
  \;=\;
  \frac{Q_{\beta}}{|\Delta(\mathrm{net})|}
  \;=\;
  \frac{0.78233}{0.18829}
  \;\approx\; 4.155\;\text{MeV}
  \;\approx\; 8.131 \times \mathfrak{m}_{e}.
$$

Note: $\Delta(\mathrm{net}) < 0$ (net$(\mathfrak{n}) <$
net$(\mathfrak{p})$ with typed crossings), so we use $|\Delta|$ to
keep $\mathbf{E}_0 > 0$.

## NF$_+$ / NF$_-$ decomposition

Each nucleon's NF splits into positive and negative coefficient
sums:

| | NF$_+$ | NF$_-$ | Net |
|:---:|---:|---:|---:|
| **Neutron** | $+1.0664$ ($H^0, H^1, L_-$) | $-0.2555$ ($\nu, L_+, e^-$) | $+0.8108$ |
| **Proton** | $+1.1420$ ($H^0, H^1, L_+, L_-$) | $-0.1429$ ($\nu, e^-$) | $+0.9991$ |
| **$\Delta$** | $-0.0756$ | $-0.1127$ | $-0.1883$ |

The neutron has **three** negative terms ($\nu, L_+, e^-$) while
the proton has only **two** ($\nu, e^-$).  The $L_+$ sign flip is
the typed-crossing effect: the $d$-$d$ crossing in neutron
$[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ shifts the Hopf link
coefficient below zero.

## Observable vs virtual: $Q_{\geq 2}$

Terms of word length $\ell \geq 2$ (Hopf links $L_\pm$ and trefoil
$e^-$) are topologically non-trivial and therefore **observable**.
Terms $\ell < 2$ ($\nu, H^0, H^1$) are virtual.

| | Observable ($\ell \geq 2$) | Virtual ($\ell < 2$) |
|:---:|---:|---:|
| **Neutron** | $-0.0446$ | $+0.8554$ |
| **Proton** | $+0.0655$ | $+0.9336$ |
| **$\Delta$** | $-0.1101$ | $-0.0782$ |

The observable-only $Q$-value, using $\mathbf{E}_0(\mathrm{net})$:

$$
  Q_{\geq 2} = |\Delta(\ell \geq 2)| \times \mathbf{E}_0
  = 0.11007 \times 4.155
  \approx 0.4573\;\text{MeV}
  \;=\; 58.5\%\;\text{of}\;Q_\beta.
$$

## Energy scale scenarios

| Scenario | $|\Delta|$ | $\mathbf{E}_0$ (MeV) | $\mathbf{E}_0 / \mathfrak{m}_e$ |
|:---|---:|---:|---:|
| All terms $|\Delta\mathrm{net}|$ | $0.18829$ | $4.155$ | $8.131$ |
| Observable $|\Delta(\ell \geq 2)|$ | $0.11007$ | $7.108$ | $13.909$ |
| Positive $|\Delta\mathrm{NF}_+|$ | $0.07563$ | $10.345$ | $20.244$ |
| Leptonic $|\Delta\nu| + |\Delta e^-|$ | $0.10302$ | $7.594$ | $14.861$ |

## Full energy budget

Each of the six NF terms contributes
$\Delta_i \times \mathbf{E}_0$ to the total decay energy.
The budget is:

| Term | Word | Knot/Link | $\ell$ | $\Delta_i$ | $\Delta_i \times \mathbf{E}_0$ (MeV) |
|:---:|:---:|:---:|:---:|---:|---:|
| $\nu$ | $\mathbf{1}$ | unknot ($0_1$) | $0$ | $-0.10205$ | $+0.4240$ |
| $H^0$ | $\sigma_0$ | virtual | $1$ | $+0.01240$ | $-0.0515$ |
| $H^1$ | $\sigma_1$ | virtual | $1$ | $+0.01143$ | $-0.0475$ |
| $L_+$ | $\sigma_0\sigma_1$ | Hopf link | $2$ | $-0.10899$ | $+0.4529$ |
| $L_-$ | $\sigma_1\sigma_0$ | Hopf link | $2$ | $-0.00010$ | $+0.0004$ |
| $e^-$ | $\sigma_0\sigma_1\sigma_0$ | trefoil ($3_1$) | $3$ | $-0.00098$ | $+0.0041$ |
|  |  |  |  | **Sum** | **$+0.782$ MeV** |

(Signs: $\Delta(\mathrm{net}) < 0$ with typed crossings, so the
$\mathbf{E}_0$ budget uses the sign convention
$\Delta_i \times \mathbf{E}_0 \times (-\mathrm{sgn}\,\Delta_{\mathrm{net}})$
to give $Q > 0$.)

## The $L_+$ dominance (typed crossings)

With typed crossings, the single largest contributor is
$\Delta(L_+) = -0.1090$, giving $+0.453\;\text{MeV}$ — larger
than the $\nu$ debt ($+0.424\;\text{MeV}$).  This replaces the
$\sigma_1$ dominance of the untyped computation.

The $\nu$ debt ($+0.424\;\text{MeV}$) and $L_+$ shift
($+0.453\;\text{MeV}$) together account for
$0.877\;\text{MeV}$ — more than $Q_\beta$.  The small
virtual terms ($H^0, H^1$) absorb the excess:

$$
  \underbrace{+0.453}_{L_+}
  \;\underbrace{+0.424}_{\nu\text{ debt}}
  \;\underbrace{-0.052}_{H^0}
  \;\underbrace{-0.047}_{H^1}
  \;\underbrace{+0.004}_{\text{other}}
  \;=\;
  +0.782\;\text{MeV}.
$$

## Physical interpretation

Beta decay pays down the neutron's leptonic debt.  With typed
crossings, the process
$\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu_e$
releases $Q_\beta = 0.782\;\text{MeV}$ because:

1. The neutron's $L_+$ (Hopf link) coefficient is **negative**
   ($-0.010$) while the proton's is positive ($+0.099$).  This
   $\Delta L_+ = -0.109$ is the dominant energy source.

2. The neutron carries a larger $\nu$ debt than the proton
   ($\Delta\nu = -0.102$), contributing $+0.424\;\text{MeV}$.

3. The virtual terms ($H^0, H^1$) contribute small negative
   corrections ($-0.099\;\text{MeV}$ total).

4. The $e^-$ channel contributes only $+0.004\;\text{MeV}$ —
   the electron debt difference is nearly zero.

Witness: `beta-decay-energy-scale.witness.json`.
