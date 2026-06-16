The energy scale $E_0$ is **derived** from CAL-1 ($m_e$) and CAL-2
($q_0$) alone — no β-decay calibration consumed. It has a
natural interpretation in terms of the $q$-deformed Planck
scale: it is the energy of one Hecke reduction step — the
cost of resolving a single $\sigma_i^2 \to h\sigma_i + \mathbf{1}$
in physical units.

## Derived form (single Hecke tick)

$$
  \boxed{
  E_0
  =
  m_e \cdot c_q^2 \cdot \hbar_q
  =
  \frac{m_e}{(q-1)^2} \cdot \frac{q-1}{q}
  =
  \frac{m_e}{q(q-1)}
  }
$$

At $q_0 \approx 1.110$, $E_0 \approx 4.186$ MeV.

**Input-error propagation** (CAL-1 $\sigma_{m_e}/m_e \approx 0.3$ ppb,
CAL-2 $\sigma_{q_0}/q_0 \approx 1.22$ ppb). The q_0 amplification
factor $\partial \ln E_0 / \partial \ln q_0 = (1 - 2q_0)/(q_0 - 1)
\approx -11.09$ at $q_0 = 1.110$:

$$
  \sigma_{E_0} / E_0
  \approx
  \sqrt{(0.3\,\mathrm{ppb})^2 + (11.09 \times 1.22\,\mathrm{ppb})^2}
  \approx 13.5\,\mathrm{ppb}.
$$

That is $\sigma_{E_0} \approx 5.7 \times 10^{-8}$ MeV — completely
negligible at the keV scale of β-decay observables.

## Calibration-cross-check (NOT used for predictions)

A historical "calibrated $E_0$" definition used CAL-3 ($\mathfrak{Q}_\beta$)
as input via $E_0^{(\text{cal})} = \mathfrak{Q}_\beta^{\text{CODATA}}
/ \lvert\Delta(\mathrm{net})\rvert \approx 4.155$ MeV. **This form
is no longer used** in the prediction pipeline because it consumes
CAL-3 as input rather than treating it as a prediction (per
[`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic)).

The 0.74% gap between the derived $E_0 \approx 4.186$ MeV and the
cross-check $\approx 4.155$ MeV is the brane-tower truncation
residual at $N=0$, identical to the +0.17% / +1.31 keV residual
in $\mathfrak{Q}_\beta$ prediction. Per the structural bound
([`per-braid-mass-tower.md`](#prop:per-braid-mass-tower)) this is
$O(\hbar_q^2/(1 - \hbar_q^2)) \approx 1\%$ at $N=0$.

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
The Q-value $\mathfrak{Q}_\beta = 0.782$ MeV is the energy released by
this single crossing change.  Dividing by the dimensionless
Hecke NF difference $\lvert\Delta\mathrm{net}\rvert \approx 0.188$
gives $E_0 = \mathfrak{Q}_\beta / \lvert\Delta\mathrm{net}\rvert \approx 4.179$ MeV.

This is analogous to measuring the speed of light by timing
the simplest electromagnetic process: we need one clean
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
| $\mathfrak{Q}_\beta(n)$ | $H^2$ | The $\beta$-decay scale | $E_0$ in MeV |

Once $q_0$ is fixed, $c_q$, $\hbar_q$, $t_P$, and $G_q$ are
all determined.  The mass scale $E_0$ then sets the
correspondence between the $q$-Planck system and SI units.
The $1\%$ residual between $E_0$ and $m_e c_q^2 \hbar_q$
is the signature of the brane tower contribution — the
difference between single-level and full-tower mass.
