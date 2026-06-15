The critical temperatures of [`prop:phase-transition-boundary`](#prop:phase-transition-boundary)
are fixed by the $S^3$-boundary action $\mathfrak{S}_q^{(\partial)}$. For a **molecular
liquid** this boundary action has an explicit braid realization: it is the
**hydrogen-bond network cohesion**, and it is gated by the same
sp$^3 \leftrightarrow$ pure-$p$ flip that sets the bond angle.

**The hydrogen bond is the $h^2$-suppressed crossing.** A covalent $X$–$H$ bond
is a $\sigma$-crossing (the shared trefoil,
[`covalent-bond-shared-trefoil`](#def:covalent-bond-shared-trefoil)). A
hydrogen bond $X\!-\!H\cdots Y$ is the *weak* inter-molecular crossing between
the donor $\sigma$ and the acceptor lone pair, suppressed by the square of the
substrate $q$-deformation parameter $h = q_0 - q_0^{-1}$:

$$
  E_{\mathrm{HB}} \;=\; h^2\, E_{\mathrm{cov}},
  \qquad h^2 \approx :val[hbond_h_squared]{precision=4, witness=folio-assistant/computations/hbond-categorical-action.witness.json}.
$$

This $h^2$ — fixed entirely by the substrate $q_0$ — is the measured
hydrogen-bond/covalent energy ratio ($\approx 0.044$, i.e. $\approx 20$ vs
$\approx 460\ \mathrm{kJ/mol}$ for water). The boundary action is then the sum
over the molecule's net hydrogen bonds,

$$
  \mathfrak{S}_q^{(\partial)} \;=\; n_{\mathrm{HB}}\, h^2\, E_{\mathrm{cov}},
$$

with $n_{\mathrm{HB}}$ the net hydrogen-bond count from the braid / VSEPR
lone-pair structure ([`tetrahedral-hbond-directions`](#prop:tetrahedral-hbond-directions)).

**The sp$^3$ gate (one flip, two observables).** A directional hydrogen bond
requires a directional (sp$^3$) acceptor lone pair. So $\mathfrak{S}_q^{(\partial)}$ is gated
by the *same* discrete sp$^3 \leftrightarrow$ pure-$p$ flip that sets the bond-angle base
([`prop:symmetric-block-domain-weight`](#prop:symmetric-block-domain-weight);
penetration gap $\Delta(n)\propto(n-1)$, flip at $n=2\to3$): period-2 atoms are
sp$^3$ and hydrogen-bond; period-3+ are pure-$p$ and do **not** (their latent heat
is dispersion, outside this model). The flip that opens the H–O–H angle and the
flip that makes water boil high are one mechanism.

**Boiling and freezing.** With $T_q^{(g\to l)} = \mathfrak{S}_q^{(\partial)}/[2]_q$, the
entropy of vaporisation is the pure $q$-number $[2]_q = q+q^{-1}$ (no separate
input), and the latent heat $L = \mathfrak{S}_q^{(\partial)}$ follows with no fit:

| | $n_{\mathrm{HB}}$ | sp$^3$? | $L^{\mathrm{pred}}$ (kJ/mol) | $L^{\mathrm{obs}}$ | tier |
|---|---|---|---|---|---|
| $\mathrm{H_2O}$ | $2$ | yes | $:val[hbond_h2o_L_pred]{precision=1, witness=folio-assistant/computations/hbond-categorical-action.witness.json}$ | $40.7$ | near-match ($:val[hbond_h2o_err_pct]{precision=1, witness=folio-assistant/computations/hbond-categorical-action.witness.json}$) |
| $\mathrm{HF}$ | $1$ | yes | $24.7$ | $25.2$ | near-match ($1.9\%$) |
| $\mathrm{H_2S}$ | $-$ | no (pure-$p$) | $0$ (H-bond off) | $18.7$ | dispersion |

The water latent heat lands within $\approx 1\%$ of measured, giving
$T_{\mathrm{boil}}(\mathrm{H_2O}) \approx 369\ \mathrm{K}$ (observed $373$) once
$L$ is converted to kelvin by the bridge $k_B T_{\mathrm{phys}} = \hbar_q$
([`boltzmann-constant`](#prop:boltzmann-constant)). The freezing point follows
from the second relation $T_q^{(l\to s)} = \mathfrak{S}_q^{(\partial)}/([2]_q[n_K]_q)$, i.e.
$T_{\mathrm{melt}}/T_{\mathrm{boil}} = 1/[n_K]_q$ in the crossing number $n_K$ of
the molecular knot.

*This realization is a tiered observation: the $h^2$ suppression and the sp$^3$
gate are derived from the substrate and the already-proved bond-angle flip; the
covalent $E_{\mathrm{cov}}$ and the latent heat $L^{\mathrm{obs}}$ are
experimental inputs; the dispersion latent heat of the non-hydrogen-bonding
(pure-$p$) hydrides is the **van der Waals channel**
([`def:van-der-waals-hopf-channel`](#def:van-der-waals-hopf-channel)) — the Hopf
symmetric block, a separate interaction not captured by the directional H-bond
model here.*
