The calibrated energy scale $E_0 \approx 4.179$ MeV
([energy scale](#rem:beta-decay-energy-scale)) has a
natural interpretation in terms of the $q$-deformed Planck
scale: it is the energy of one Hecke reduction step — the
cost of resolving a single $\sigma_i^2 \to h\sigma_i + \mathbf{1}$
in physical units.

## The near-identity

Numerically at $q_0$:

$$
  E_0
  \approx
  m_e \cdot c_q^2 \cdot \hbar_q
  =
  \frac{m_e}{(q-1)^2} \cdot \frac{q-1}{q}
  =
  \frac{m_e}{q(q-1)}
$$

| Quantity | Value | Formula |
|----------|-------|---------|
| $E_0$ (calibrated) | $4.179$ MeV | from $Q_\beta / \lvert\Delta\mathrm{net}\rvert$ |
| $m_e c_q^2 \hbar_q$ | $4.196$ MeV | $m_e / q(q-1)$ |
| Ratio | $0.990$ | $1\%$ discrepancy |

The $1\%$ residual is the difference between the calibrated
$E_0$ (which depends on the specific NF coefficients of
neutron decay) and the pure-$q$ expression.

## Physical meaning

$$
  m_e \cdot c_q^2 \cdot \hbar_q
  =
  \underbrace{m_e \cdot c_q^2}_{\text{electron rest energy}}
  \times
  \underbrace{\hbar_q}_{\text{action per Planck tick}}
  =
  \frac{m_e \cdot c_q^2}{t_P}
$$

This is the **electron's rest energy per Planck time** —
the natural energy quantum for a single interaction step
in a universe where:
- the lightest charged particle has mass $m_e$,
- the speed of information is $c_q = 1/(q-1)$,
- one Planck time is $t_P = 1/\hbar_q \approx 10.1$
  Reeb operations.

Each Hecke reduction step $\sigma_i^2 \to h\sigma_i + \mathbf{1}$
corresponds to one Planck tick of interaction: the double
crossing resolves into a weighted single crossing (energy cost
$h = q - q^{-1}$ in Skein units) plus an identity strand
(photon release).  The physical energy cost of this step is
$E_0$.

## Why free neutron decay calibrates this

The free neutron decay $n \to p + e^- + \bar\nu_e$ is the
simplest process that exercises a single Hecke step in the
hadronic sector: one crossing change $\mathfrak{d} \to \mathfrak{u}$
inside one nucleon, with no nuclear environment corrections.
The Q-value $Q_\beta = 0.782$ MeV is the energy released by
this single crossing change.  Dividing by the dimensionless
Hecke NF difference $\lvert\Delta\mathrm{net}\rvert \approx 0.188$
gives $E_0 = Q_\beta / \lvert\Delta\mathrm{net}\rvert \approx 4.179$ MeV.

This is analogous to measuring the speed of light by timing
the simplest electromagnetic process: you need one clean
measurement to set the scale, and every other speed follows.

## The three calibration inputs in Planck units

Using the three $q$-constants $c_q$, $\hbar_q$, $t_P$
(all determined by $q_0$ alone), the categorical
three-calibration inputs
([three-calibration discipline](#prop:three-calibration-discipline)) become:

| Input | $H^k$ degree | What it fixes | In $q$-Planck units |
|-------|:-----------:|--------------|---------------------|
| $m_e$ | $H^0$ | The mass unit | $E_0/(c_q^2 \hbar_q)$ (the size) |
| $m_\mu/m_e$ | $H^1$ | $q_0$ | The shape (dimensionless) |
| $Q_\beta(n)$ | $H^2$ | The $\beta$-decay scale | $E_0$ in MeV |

Once $q_0$ is fixed, $c_q$, $\hbar_q$, $t_P$, and $G(q)$ are
all determined.  The mass scale $E_0$ then sets the
correspondence between the $q$-Planck system and SI units.
The $1\%$ residual between $E_0$ and $m_e c_q^2 \hbar_q$
is the signature of the brane tower contribution — the
difference between single-level and full-tower mass.
