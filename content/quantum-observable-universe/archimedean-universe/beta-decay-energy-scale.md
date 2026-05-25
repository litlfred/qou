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

**Ansatz disclaimer (2026-05-24, PR #1127).** The first equality
$|\Delta(\mathrm{net})| \times \mathfrak{E}_0 = Q_\beta$ is an
**ansatz**: it asserts that the unweighted sum of NF coefficients
(the "net") of the proton/neutron braid words gives the leading-
order mass difference when multiplied by the single-tick energy
scale $\mathfrak{E}_0$. It has **not** been derived from the
canonical per-braid mass formula
[`prop:per-braid-mass-tower`](../braids-and-knots/per-braid-mass-tower.md),
which uses Markov-trace **weighted** sums ($\mathrm{tr}_M(\gamma) = z$,
$\mathrm{tr}_M(\sigma_i) = z^2$, $\mathrm{tr}_M(L_+) = z^3$, $\ldots$) —
a different quantity. The +0.17% match to CODATA is empirical
evidence for the ansatz but does not derive it; the gap could
equally be a numerical coincidence. Full audit:
[`docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md`](../../../docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md).
The second equality is energy conservation in $\beta$-decay (rigorous).

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

Therefore:

$$
  \mathfrak{E}_0
  = 
  \frac{Q_{\beta}}{|\Delta(\mathrm{net})|}
  = 
  \frac{0.78233}{0.18829}
   \approx  4.155 \text{MeV}
   \approx  8.131 \times \mathfrak{m}_{e}.
$$

Note: $\Delta(\mathrm{net}) < 0$ (net$(\mathfrak{n}) <$
net$(\mathfrak{p})$ with typed crossings), so we use $|\Delta|$ to
keep $\mathfrak{E}_0 > 0$.

## NF$_+$ / NF$_-$ decomposition

Each nucleon's NF splits into positive and negative coefficient
sums:

See [Table 1](#tbl:beta-decay-energy-scale-table1-data).

The neutron has **three** negative terms ($\gamma, L_+, e^-$) while
the proton has only **two** ($\gamma, e^-$).  The $L_+$ sign flip is
the typed-crossing effect: the $d$-$d$ crossing in neutron
$[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ shifts the Hopf link
coefficient below zero.

## Observable vs virtual: $Q_{\geq 2}$

Terms of word length $\ell \geq 2$ (Hopf links $L_\pm$ and trefoil
$e^-$) are topologically non-trivial and therefore **observable**.
Terms $\ell < 2$ ($\gamma, \sigma_0, \sigma_1$) are virtual.

See [Table 2](#tbl:beta-decay-energy-scale-table2-data).

The observable-only $Q$-value, using $\mathfrak{E}_0(\mathrm{net})$:

$$
  Q_{\geq 2} = |\Delta(\ell \geq 2)| \times \mathfrak{E}_0
  = 0.11007 \times 4.155
  \approx 0.4573 \text{MeV}
  =  58.5\% \text{of}Q_\beta.
$$

## Energy scale scenarios

See [Table 3](#tbl:beta-decay-energy-scale-table3-data).

## Full energy budget

Each of the six NF terms contributes
$\Delta_i \times \mathfrak{E}_0$ to the total decay energy.
The budget is:

See [Table 4](#tbl:beta-decay-energy-scale-table4-data).

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
$0.877 \text{MeV}$ — more than $Q_\beta$.  The small
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
releases $Q_\beta = 0.782 \text{MeV}$ because:

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
