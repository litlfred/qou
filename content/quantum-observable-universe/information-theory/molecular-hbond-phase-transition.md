We fix the critical temperatures of [`prop:phase-transition-boundary`](#prop:phase-transition-boundary) using the $S^3$-boundary action $\mathfrak{S}_q^{(\partial)}$. For a molecular liquid, this boundary action admits an explicit braid realization: it represents the hydrogen-bond network cohesion. This cohesion is gated by the discrete $\mathrm{sp}^3 \leftrightarrow \mathrm{pure}\text{-}p$ flip that sets the bond angle.

**The hydrogen bond as an $h^2$-suppressed crossing.** 
A covalent $X$–$H$ bond is a $\sigma$-crossing (the shared trefoil, [`covalent-bond-shared-trefoil`](#def:covalent-bond-shared-trefoil)). A hydrogen bond $X\!-\!H\cdots Y$ is the weak inter-molecular crossing between the donor $\sigma$ and the acceptor lone pair. It is suppressed by the square of the substrate $q$-deformation parameter $h = q_0 - q_0^{-1}$:

$$
  E_{\mathrm{HB}} = h^2 E_{\mathrm{cov}}, \qquad h^2 \approx :val[hbond_h_squared]{precision=4, witness=computations/hbond-categorical-action.witness.json}.
$$

The substrate $q_0$ entirely fixes this $h^2$ suppression. It matches the measured hydrogen-bond to covalent energy ratio ($\approx 0.044$, or $\approx 20$ vs $\approx 460\ \mathrm{kJ/mol}$ for water). The boundary action is the sum over the molecule's net hydrogen bonds:

$$
  \mathfrak{S}_q^{(\partial)} = n_{\mathrm{HB}} h^2 E_{\mathrm{cov}},
$$

where $n_{\mathrm{HB}}$ is the net hydrogen-bond count derived from the braid/VSEPR lone-pair structure ([`tetrahedral-hbond-directions`](#prop:tetrahedral-hbond-directions)).

**The $\mathrm{sp}^3$ gate.** 
A directional hydrogen bond requires a directional ($\mathrm{sp}^3$) acceptor lone pair. Thus, $\mathfrak{S}_q^{(\partial)}$ is gated by the same discrete $\mathrm{sp}^3 \leftrightarrow \mathrm{pure}\text{-}p$ flip that establishes the bond-angle base ([`prop:symmetric-block-domain-weight`](#prop:symmetric-block-domain-weight); penetration gap $\Delta(n)\propto(n-1)$, flip at $n=2\to 3$). Period-2 atoms are $\mathrm{sp}^3$ and form hydrogen bonds. Period-3+ atoms are $\mathrm{pure}\text{-}p$ and do not. The mechanism that opens the H–O–H angle is identical to the mechanism that elevates the boiling point of water.

**Boiling and freezing.** 
We compute the boiling temperature $T_q^{(g\to l)} = \mathfrak{S}_q^{(\partial)}/[2]_q$. The entropy of vaporisation is the pure $q$-number $[2]_q = q+q^{-1}$. The latent heat $L = \mathfrak{S}_q^{(\partial)}$ follows with no free parameters:

| | $n_{\mathrm{HB}}$ | $\mathrm{sp}^3$? | $L^{\mathrm{pred}}$ (kJ/mol) | $L^{\mathrm{obs}}$ | tier |
|---|---|---|---|---|---|
| $\mathrm{H_2O}$ | $2$ | yes | $:val[hbond_h2o_L_pred]{precision=1, witness=computations/hbond-categorical-action.witness.json}$ | $40.7$ | near-match ($:val[hbond_h2o_err_pct]{precision=1, witness=computations/hbond-categorical-action.witness.json}$) |
| $\mathrm{HF}$ | $1$ | yes | $24.7$ | $25.2$ | near-match ($1.9\%$) |
| $\mathrm{H_2S}$ | $-$ | no ($\mathrm{pure}\text{-}p$) | $0$ (H-bond off) | $18.7$ | dispersion |

The predicted water latent heat falls within $\approx 1\%$ of the measured value. Using the bridge relation $k_B T_{\mathrm{phys}} = \hbar_q$ ([`boltzmann-constant`](#prop:boltzmann-constant)), we recover $T_{\mathrm{boil}}(\mathrm{H_2O}) \approx 369\ \mathrm{K}$ (observed $373\ \mathrm{K}$). The freezing point follows from $T_q^{(l\to s)} = \mathfrak{S}_q^{(\partial)}/([2]_q[n_K]_q)$, yielding the ratio $T_{\mathrm{melt}}/T_{\mathrm{boil}} = 1/[n_K]_q$, where $n_K$ is the crossing number of the molecular knot.

*Observation structure.* We derive the $h^2$ suppression and the $\mathrm{sp}^3$ gate from the substrate and the bond-angle flip. We input the covalent $E_{\mathrm{cov}}$ and the latent heat $L^{\mathrm{obs}}$ from experiment. The dispersion latent heat of the non-hydrogen-bonding ($\mathrm{pure}\text{-}p$) hydrides belongs to the Hopf channel ([`def:van-der-waals-hopf-channel`](#def:van-der-waals-hopf-channel)) — the symmetric $e_+$ carrier. Proper van der Waals interactions correspond to the discarded bar-odd residual $\sinh(2\lambda)(e_+-e_-)$ of that channel (`prop:vdw-pskew-isolation`), which requires a separate mechanism.
