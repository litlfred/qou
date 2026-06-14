The QOU double-slit model predicts two structurally distinct scattering
modes, summarised in the following table:

| | **Mode 1: Massive particle** | **Mode 2: Photon (with color content)** |
|---|---|---|
| **Geometric identity** | $q$-harmonic form ($\Delta_q\alpha = 0$) | Color-dressed identity $\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ |
| **Phase mechanism** | $q$-Laplacian cross-coupling | Color twist $q\phi$ + polarisation eigenvalues $(\varphi_0 q, -\varphi_1 q^{-1})$ |
| **Interference formula** | $\cos^2(\Delta\Phi_q / 2)$ | $\cos^2(\Delta\Phi_q^{(\mathrm{color})} / 2)$ |
| **Envelope** | $q$-corrected sinc${}^2$ | Julia-set measure $\mu_J$ modulated by color visibility $V_{\mathrm{color}}$ |
| **Band-width shift** | Wider by $(1 - q^{-1})^2$ | Power-law tails ($\sim\lvert\theta\rvert^{-d_H}$) + polarisation asymmetry |
| **Classical limit** ($q \to 1$) | Fraunhofer | Airy |

**Band-width predictions versus observation.**
Standard diffraction theory predicts band widths from slit geometry
alone (Fraunhofer for matter waves, Airy for photons). Precision
experiments report systematic deviations:

1. *Electron diffraction*: subsidiary maxima are wider than the
 Fraunhofer sinc${}^2$ envelope predicts. The excess is typically
 attributed to Coulomb interaction with slit edges, but the
 correction is *ad hoc* and not derived from the wave equation.
 In the QOU model, the excess width arises from the spin-core term
 $(1 - q^{-1})^2\Delta_\xi$ of the $q$-Laplacian, which adds
 Reeb-direction broadening to the envelope *without free parameters*
 once $q$ is fixed by the
 [local substrate value](#prop:local-substrate-q).

2. *Molecular diffraction* (C$_{60}$, large organics): fringe
 visibility matches predictions, but measured band widths are
 systematically broader. The standard explanation invokes van der
 Waals attraction to the grating. The QOU prediction is quantitative:
 heavier particles have larger $\langle\Delta_\xi\rangle / \langle\Delta\rangle$
 (more Reeb modes per unit mass), giving wider envelopes that scale
 with molecular complexity rather than dipole moment.

3. *Photon diffraction*: subsidiary Airy maxima are more suppressed
 than $1/(m\pi)^2$, and the intensity tails are heavier than
 $|\theta|^{-2}$. The Julia-set envelope $\mu_J$ accordingly
 produces both effects: the fractal boundary concentrates measure
 near the central peak (suppressing subsidiaries) while the
 power-law decay $|\theta|^{-d_H}$ with $d_H > 1$ gives broader
 tails. When the photon carries non-trivial color content
 $(\varphi_0, \varphi_1)$
 ([color content](#rem:knot-basis-color-content)), the
 polarisation-dependent Reeb phases introduce an additional
 fringe-visibility modulation $V_{\mathrm{color}}$ that depends
 on the slit material's Hecke dressing --- a signature absent
 both in standard quantum optics and in the bare-photon
 ($\varphi_0 = \varphi_1 = 0$) QOU prediction.

**Observation and coherence loss.**
When a detector is placed at one slit, the
[observation](#def:observation) $\mathfrak{O}_p$ shifts the substrate
parameter $q \mapsto q + \delta q$ on that path via Hopf coaction.
The two paths now carry *different* $q$-values. The Reeb phases
$\Phi_{\mathrm{Reeb}}^{(1)}$ and $\Phi_{\mathrm{Reeb}}^{(2)}$
become incommensurate, and their cross terms average to zero over the
detector integration time. The result is the same as the which-path
experiment: fringes vanish, but the *envelope* (single-slit pattern)
is modified --- it carries a residual asymmetry of order $\delta q / q$,
reflecting the permanent geometric deformation left by the
observation.

**Experimental discriminant.**
The two modes predict a specific ratio of photon-to-electron envelope
widths at the same slit geometry:

$$
  \frac{w_{\mathrm{photon}}}{w_{\mathrm{electron}}}
  = 
  \frac{d_H}{2}
  \frac{1 + (1 - q^{-1})^2\langle\Delta_\xi\rangle_e /
            \langle\Delta\rangle_e}{1},
$$

where $d_H = d_H(q)$ is the Hausdorff dimension of $J(f_q) \cap S^1$.
This ratio is independent of slit width and wavelength, depending only
on $q$. A simultaneous electron--photon double-slit measurement at
the same apparatus would determine $q$ and $d_H$ independently,
providing a sharp test of the two-mode prediction.

**Color-content discriminant.**
A more refined test exploits the photon color content. Using linearly
polarised light with controlled polarisation angle $\alpha$
(corresponding to color weights
$\varphi_0 = \cos\alpha$, $\varphi_1 = \sin\alpha$), the
fringe shift acquires an $\alpha$-dependent term:

$$
  \delta\Delta\Phi(\alpha)
  = 
  (\cos\alphaq - \sin\alphaq^{-1})
  \hbar_q\mathrm{Vol}(K_{\mathrm{mat}})\Delta\phi_\xi.
$$

Sweeping $\alpha$ from $0$ to $\pi/2$ traces a sinusoidal modulation of
the fringe positions. The amplitude of this modulation scales with
$(q + q^{-1})\hbar_q\mathrm{Vol}(K_{\mathrm{mat}})$ and is
material-dependent (different slit materials give different
$\mathrm{Vol}(K_{\mathrm{mat}})$), while the classical birefringence
prediction depends on refractive index. A single apparatus with
rotatable polariser and interchangeable slit materials would separate
the two effects.
