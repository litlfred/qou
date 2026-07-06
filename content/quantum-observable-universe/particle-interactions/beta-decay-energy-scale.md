The Gröbner--Shirshov normal form coefficients are dimensionless Laurent
polynomials in $q$.  To connect them to observed energies we need
an **energy scale** $\mathfrak{E}_0$ (in MeV) such that

$$
  |\Delta(\mathrm{net})| \times \mathfrak{E}_0
  = 
  Q_{\beta}
  = 
  \mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} - \mathfrak{m}_{e}
   \approx  0.7823 \text{MeV}.
$$

The framework gives $\mathfrak{E}_0$ in two forms — a **single-Planck-tick**
($N=0$) value and a **tower-summed** ($N \to \infty$) geometric form —
that differ by the brane-tower correction $1/(1-\hbar_q^2) \approx 1.0099$
at $q_0 \approx 1.110$.  Both are derivable from CAL-1 ($m_e$) and CAL-2
($q_0$) alone; CAL-3 ($\mathfrak{Q}_\beta(n)$) is the cross-check.  See the
[notation register](../notation/notation-register.md) for the
$\mathfrak{E}_0^{(N=0)}$ / $\mathfrak{E}_0^{\text{full}}$ symbol convention
and the [collisions note](../notation/notation-collisions.md) for why
$\mathfrak{E}_0$ is **not** $\mathfrak{Q}_\beta(n)$.

## Linearity

The transition $\Delta = \mathrm{NF}(\mathfrak{n}) -
\mathrm{NF}(\mathfrak{p})$ equals $\mathrm{NF}(\mathfrak{n} -
\mathfrak{p})$ because $\mathrm{NF}$ is coordinate extraction in
the Gröbner--Shirshov basis — a linear map on the 6-dimensional
vector space $H_3(q)$.

## Derivation (typed crossings)

From the witness (`free-neutron-decay.witness.json`, typed crossings):

- $\mathrm{net}(\mathfrak{n}) = +0.810835$, $\mathrm{net}(\mathfrak{p}) = +:val[confinement_B3_net_proton]{precision=6}$
- $\Delta(\mathrm{net}) = -0.188291$

From CODATA 2022:

- $\mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} \approx 1.29333\;\text{MeV}$
- $\mathfrak{m}_{e} \approx 0.51100\;\text{MeV}$
- $Q_{\beta} \approx 0.78233\;\text{MeV}$

**Derived energy scale — single-tick (Planck-tick) form, $\mathfrak{E}_0^{(N=0)}$.**
The leading-order energy scale is derivable from the categorical
three-calibration inputs $m_e$ ($H^0$) and $q_0$ ($H^1$) alone —
$\mathfrak{Q}_\beta(n)$ ($H^2$) is the datum the framework predicts, not consumed
here ([three-calibration discipline](#prop:three-calibration-discipline)):

$$
  \mathfrak{E}_0^{(N=0)}
  :=
  \frac{m_e}{q_0(q_0 - 1)}
  =
  m_e \cdot c_q^2 \cdot \hbar_q
  \approx  4.186 \text{MeV}.
$$

This is the electron rest energy per Planck time
([energy scale and Planck time](#rem:energy-scale-planck)).

**Derived energy scale — tower-summed form, $\mathfrak{E}_0^{\text{full}}$.**
The full brane-tower geometric series ([symbolic derivation](https://github.com/litlfred/qou/blob/main/computations/q_beta_form_a_n1_extension.py#L32))
is

$$
  \mathfrak{E}_0^{\text{full}}
  :=
  \mathfrak{E}_0^{(N=0)} \cdot \sum_{k=0}^{\infty} \hbar_q^{2k}
  =
  \frac{\mathfrak{E}_0^{(N=0)}}{1 - \hbar_q^2}
  \approx  4.228 \text{MeV}
$$

at $q_0 \approx 1.110$, $\approx$ +0.99% over the single-tick value. Truncations
$\mathfrak{E}_0^{(N)} = \mathfrak{E}_0^{(N=0)} \cdot (1 - \hbar_q^{2(N+1)})/(1 - \hbar_q^2)$
recover the tower at finite depth.

**Calibration cross-check, $\mathfrak{E}_0^{(\text{cal})}$.**
The same scale can be extracted from CODATA by dividing the
free neutron $Q$-value by the Hecke NF difference:

$$
  \mathfrak{E}_0^{(\text{cal})}
  =
  \frac{Q_{\beta}}{|\Delta(\mathrm{net})|}
  =
  \frac{0.78233}{0.18829}
   \approx  4.155 \text{MeV}
   \approx  8.131 \times \mathfrak{m}_{e}.
$$

The values, computed from the witness
[`q-beta-form-a-n1-extension.witness.json`](https://github.com/litlfred/qou/blob/main/computations/q-beta-form-a-n1-extension.witness.json):

| Quantity | Value (MeV) | vs $\mathfrak{E}_0^{(\text{cal,symb})}$ |
|----------|------------:|------------------------------:|
| $\mathfrak{E}_0^{(N=0)}$ (single-tick derived) | $:val[E_0_N0_MeV]{precision=4}$ | $+0.17\%$ |
| $\mathfrak{E}_0^{\text{full}}$ (geometric-tower derived) | $:val[E_0_full_MeV]{precision=4}$ | $+1.16\%$ |
| $\mathfrak{E}_0^{\text{full},\mathrm{Li}_2^q}$ (symmetric q-dilogarithm candidate) | $:val[E_0_full_li2q_MeV]{precision=4}$ | $+1.15\%$ |
| $\mathfrak{E}_0^{(\text{cal,symb})}$ (CODATA / $h(h-2)/2$) | $:val[E_0_calibrated_MeV]{precision=4}$ | reference (symbolic) |
| $\mathfrak{E}_0^{(\text{cal,typed})}$ (CODATA / $\lvert\Delta(\text{net,typed})\rvert$) | $4.155$ | typed-crossings value (finite-size noise, 0.6% below symbolic) |

**Open finding.** Both the geometric tower form
$1/(1-\hbar_q^2)$ and the bounded symmetric $\mathrm{Li}_2^q$
candidate move the framework prediction *further from* the
calibrated values at the substrate level (only $\approx$ 0.01% apart
at $q_0$). The direction-of-residual puzzle is recorded in
[`docs/audits/-tower-mev-calibration-finding.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-tower-mev-calibration-finding.md)
(the audit independently confirms $-\mathrm{Li}_2^q(-V)$ is the
correct Kashaev specialisation, while the asserted $\Phi_q(V)$
form is off by $10^{6}$), and the open closure question is now formally
posed as the conjecture
[`conj:alpha-k-categorical-closure`](../braids-and-knots/alpha-k-categorical-closure.md)
(existence, family selection, CAL-3 direction). The H_3 explicit
$\alpha_k$ values from
[`prop:alpha-k-derivation-procedure`](../braids-and-knots/alpha-k-derivation-procedure.md)
do **not** satisfy the naive recursion $\alpha_k = \hbar_q^{2(k-1)}\alpha_{k-1}$
($\alpha_1 = 0$, not $\hbar_q^0 \alpha_0 = 1$), so neither the
geometric nor the Li_2^q closure is a trivial substitution — the
correct closure is a non-obvious resummation identity that the
conjecture seeks.

Note: $\Delta(\mathrm{net}) < 0$ (net$(\mathfrak{n}) <$
net$(\mathfrak{p})$ with typed crossings), so we use $|\Delta|$ to
keep $\mathfrak{E}_0 > 0$.

## NF$_+$ / NF$_-$ decomposition

Each nucleon's NF splits into positive and negative coefficient
sums:

| | NF$_+$ | NF$_-$ | Net |
|:---:|---:|---:|---:|
| **Neutron** | $+1.0664$ ($\sigma_0, \sigma_1, L_-$) | $-0.2555$ ($\gamma, L_+, e^-$) | $+0.8108$ |
| **Proton** | $+1.1420$ ($\sigma_0, \sigma_1, L_+, L_-$) | $-0.1429$ ($\gamma, e^-$) | $+0.9991$ |
| **$\Delta$** | $-0.0756$ | $-0.1127$ | $-0.1883$ |

The neutron has **three** negative terms ($\gamma, L_+, e^-$) while
the proton has only **two** ($\gamma, e^-$).  The $L_+$ sign flip is
the typed-crossing effect: the $d$-$d$ crossing in neutron
$[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ shifts the Hopf link
coefficient below zero.

## Observable vs virtual: $Q_{\geq 2}$

Terms of word length $\ell \geq 2$ (Hopf links $L_\pm$ and trefoil
$e^-$) are topologically non-trivial and therefore **observable**.
Terms $\ell < 2$ ($\gamma, \sigma_0, \sigma_1$) are virtual.

| | Observable ($\ell \geq 2$) | Virtual ($\ell < 2$) |
|:---:|---:|---:|
| **Neutron** | $-0.0446$ | $+0.8554$ |
| **Proton** | $+0.0655$ | $+0.9336$ |
| **$\Delta$** | $-0.1101$ | $-0.0782$ |

The observable-only $Q$-value, using $\mathfrak{E}_0(\mathrm{net})$:

$$
  Q_{\geq 2} = |\Delta(\ell \geq 2)| \times \mathfrak{E}_0
  = 0.11007 \times 4.155
  \approx 0.4573 \text{MeV}
  =  58.5\% \text{of}\mathfrak{Q}_\beta.
$$

## Energy scale scenarios

| Scenario | $|\Delta|$ | $\mathfrak{E}_0$ (MeV) | $\mathfrak{E}_0 / \mathfrak{m}_e$ |
|:---|---:|---:|---:|
| All terms $|\Delta\mathrm{net}|$ | $0.18829$ | $4.155$ | $8.131$ |
| Observable $|\Delta(\ell \geq 2)|$ | $0.11007$ | $7.108$ | $13.909$ |
| Positive $|\Delta\mathrm{NF}_+|$ | $0.07563$ | $10.345$ | $20.244$ |
| Leptonic $|\Delta\nu| + |\Delta e^-|$ | $0.10302$ | $7.594$ | $14.861$ |

## Full energy budget

Each of the six NF terms contributes
$\Delta_i \times \mathfrak{E}_0$ to the total decay energy.
The budget is:

| Term | Word | Knot/Link | $\ell$ | $\Delta_i$ | $\Delta_i \times \mathfrak{E}_0$ (MeV) |
|:---:|:---:|:---:|:---:|---:|---:|
| $\gamma$ | $\mathbf{1}$ | photon | $0$ | $-0.10205$ | $+0.4240$ |
| $\sigma_0$ | $\sigma_0$ | virtual | $1$ | $+0.01240$ | $-0.0515$ |
| $\sigma_1$ | $\sigma_1$ | virtual | $1$ | $+0.01143$ | $-0.0475$ |
| $L_+$ | $\sigma_0\sigma_1$ | Hopf link | $2$ | $-0.10899$ | $+0.4529$ |
| $L_-$ | $\sigma_1\sigma_0$ | Hopf link | $2$ | $-0.00010$ | $+0.0004$ |
| $e^-$ | $\sigma_0\sigma_1\sigma_0$ | trefoil ($3_1$) | $3$ | $-0.00098$ | $+0.0041$ |
|  |  |  |  | **Sum** | **$+0.782$ MeV** |

(Signs: $\Delta(\mathrm{net}) < 0$ with typed crossings, so the
$\mathfrak{E}_0$ budget uses the sign convention
$\Delta_i \times \mathfrak{E}_0 \times (-\mathrm{sgn}\Delta_{\mathrm{net}})$
to give $Q > 0$.)

## The $L_+$ dominance (typed crossings)

With typed crossings, the single largest contributor is
$\Delta(L_+) = -0.1090$, giving $+0.453 \text{MeV}$ — larger
than the $\gamma$ debt ($+0.424 \text{MeV}$).  This replaces the
$\sigma_1$ dominance of the untyped computation.

The $\gamma$ debt ($+0.424 \text{MeV}$) and $L_+$ shift
($+0.453 \text{MeV}$) together account for
$0.877 \text{MeV}$ — more than $\mathfrak{Q}_\beta$.  The small
virtual terms ($\sigma_0, \sigma_1$) absorb the excess:

$$
  \underbrace{+0.453}_{L_+}
  \underbrace{+0.424}_{\gamma\text{ debt}}
  \underbrace{-0.052}_{\sigma_0}
  \underbrace{-0.047}_{\sigma_1}
  \underbrace{+0.004}_{\text{other}}
  = 
  +0.782 \text{MeV}.
$$

## Physical interpretation

Beta decay pays down the neutron's leptonic debt.  With typed
crossings, the process
$\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu_e$
releases $\mathfrak{Q}_\beta = 0.782 \text{MeV}$ because:

1. The neutron's $L_+$ (Hopf link) coefficient is **negative**
   ($-0.010$) while the proton's is positive ($+0.099$).  This
   $\Delta L_+ = -0.109$ is the dominant energy source.

2. The neutron carries a larger $\gamma$ debt than the proton
   ($\Delta\gamma = -0.102$), contributing $+0.424 \text{MeV}$.

3. The virtual terms ($\sigma_0, \sigma_1$) contribute small negative
   corrections ($-0.099 \text{MeV}$ total).

4. The $e^-$ channel contributes only $+0.004 \text{MeV}$ —
   the electron debt difference is nearly zero.

Witness: `beta-decay-energy-scale.witness.json`.
