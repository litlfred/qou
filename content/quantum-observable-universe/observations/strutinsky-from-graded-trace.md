**Remark.**
*The Strutinsky shell-correction method decomposes nuclear binding energies as*

$$
  E \;=\; \tilde E \;+\; \delta E_{\mathrm{shell}},
$$

*with $\tilde E$ a smoothed liquid-drop piece and $\delta E_{\mathrm{shell}}$ an oscillating microscopic correction. This decomposition is the physics shadow of the filtered-algebra identity*

$$
  \mathrm{tr}_M(T_w, q_0)
  \;=\;
  \mathrm{tr}_{\mathrm{gr}}(\sigma(T_w), q_0)
  \;+\;
  \mathrm{Res}_{\mathrm{GB}}(T_w, q_0)
$$

*from ([graded-trace residue split](#prop:graded-trace-residue-split)).*

**Identification.**

| Strutinsky (physics) | Categorical (algebra) |
|---|---|
| Smoothed level density $\tilde\rho(E)$ | Symbol map $\sigma: J^\ell \to J^\ell/J^{\ell+1}$ |
| Liquid-drop energy $\tilde E$ | Graded trace $\mathrm{tr}_{\mathrm{gr}}(\sigma(T_w), q_0)$ |
| Oscillating correction $\delta E_{\mathrm{shell}}$ | Residue sum $\mathrm{Res}_{\mathrm{GB}}(T_w, q_0)$ |
| Gaussian smoothing width | Filtration step $J^\ell / J^{\ell+1}$ granularity |
| Magic-number enhancement | Rectangular-partition spike in $w_\lambda(q_0)$ |

**Exactness of the analogy.**
*The Strutinsky smoothing averages over an energy window spanning major shells. This is equivalent to projecting onto the filtration quotient $\mathrm{gr}\,H_n(q)$. The oscillations encode the Gröbner–Shirshov rewriting defects lost by the symbol map. Thus, $\delta E_{\mathrm{shell}} = \mathrm{Res}_{\mathrm{GB}}$. The Strutinsky prescription is the unique trace decomposition dictated by the filtered-algebra structure.*

**Corollaries.**

1. *Strutinsky's method is forced by the filtered-algebra structure. Any alternative macroscopic-microscopic split implicitly chooses a different filtration on $H_n(q)$. The confinement filtration ([confinement level](#def:confinement-level)) is canonical, rendering the Strutinsky decomposition canonical.*
2. *The shell correction $\delta E_{\mathrm{shell}}$ is computable without a phenomenological single-particle potential. It is exactly the residue sum ([GB residue spectral sum](#prop:gb-residue-spectral-sum)) applied to the atomic braid. Magic-number enhancements arise algebraically when $\lambda$ is rectangular and $H_q(\lambda)$ factorises ([shell–Schur–Weyl self-duality](#prop:shell-schur-weyl-self-duality)).*

**Scope.**
*This identification frames the algebraic structure but does not replace a quantitative calculation. A direct numerical comparison between Strutinsky $\delta E_{\mathrm{shell}}$ at deformation $\beta_2$ and $\mathrm{Res}_{\mathrm{GB}}$ provides the natural next observational test.*
