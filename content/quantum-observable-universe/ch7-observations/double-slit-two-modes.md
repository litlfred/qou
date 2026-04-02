The QOU double-slit model predicts two structurally distinct scattering
modes, summarised in the following table:

| | **Mode 1: Massive particle** | **Mode 2: Photon** |
|---|---|---|
| **Geometric identity** | $q$-harmonic form ($\Delta_q\alpha = 0$) | Exceptional-divisor flux |
| **Phase mechanism** | $q$-Laplacian cross-coupling | Chiral twist $q\phi$ |
| **Interference formula** | $\cos^2(\Delta\Phi_q / 2)$ | $\cos^2(q\,d\sin\theta / 2R)$ |
| **Envelope** | $q$-corrected sinc${}^2$ | Julia-set measure $\mu_J$ |
| **Band-width shift** | Wider by $(1 - q^{-1})^2$ | Power-law tails ($\sim\lvert\theta\rvert^{-d_H}$) |
| **Classical limit** ($q \to 1$) | Fraunhofer | Airy |

**Band-width predictions versus observation.**
Standard diffraction theory predicts band widths from slit geometry
alone (Fraunhofer for matter waves, Airy for photons).  Precision
experiments report systematic deviations:

1. *Electron diffraction*: subsidiary maxima are wider than the
   Fraunhofer sinc${}^2$ envelope predicts.  The excess is typically
   attributed to Coulomb interaction with slit edges, but the
   correction is *ad hoc* and not derived from the wave equation.
   In the QOU model, the excess width arises from the spin-core term
   $(1 - q^{-1})^2\,\Delta_\xi$ of the $q$-Laplacian, which adds
   Reeb-direction broadening to the envelope *without free parameters*
   once $q$ is fixed by the
   [local substrate value](#prop:local-substrate-q).

2. *Molecular diffraction* (C$_{60}$, large organics): fringe
   visibility matches predictions, but measured band widths are
   systematically broader.  The standard explanation invokes van der
   Waals attraction to the grating.  The QOU prediction is quantitative:
   heavier particles have larger $\langle\Delta_\xi\rangle / \langle\Delta\rangle$
   (more Reeb modes per unit mass), giving wider envelopes that scale
   with molecular complexity rather than dipole moment.

3. *Photon diffraction*: subsidiary Airy maxima are more suppressed
   than $1/(m\pi)^2$, and the intensity tails are heavier than
   $|\theta|^{-2}$.  The Julia-set envelope $\mu_J$ naturally
   produces both effects: the fractal boundary concentrates measure
   near the central peak (suppressing subsidiaries) while the
   power-law decay $|\theta|^{-d_H}$ with $d_H > 1$ gives broader
   tails.

**Observation and coherence loss.**
When a detector is placed at one slit, the
[observation](#def:observation) $\mathfrak{I}_p$ shifts the substrate
parameter $q \mapsto q + \delta q$ on that path via Hopf coaction.
The two paths now carry *different* $q$-values.  The Reeb phases
$\Phi_{\mathrm{Reeb}}^{(1)}$ and $\Phi_{\mathrm{Reeb}}^{(2)}$
become incommensurate, and their cross terms average to zero over the
detector integration time.  The result is the same as the which-path
experiment: fringes vanish, but the *envelope* (single-slit pattern)
is modified --- it carries a residual asymmetry of order $\delta q / q$,
reflecting the permanent geometric deformation left by the
observation.

**Experimental discriminant.**
The two modes predict a specific ratio of photon-to-electron envelope
widths at the same slit geometry:

$$
  \frac{w_{\mathrm{photon}}}{w_{\mathrm{electron}}}
  \;=\;
  \frac{d_H}{2}\,
  \frac{1 + (1 - q^{-1})^2\,\langle\Delta_\xi\rangle_e /
            \langle\Delta\rangle_e}{1},

$$

where $d_H = d_H(q)$ is the Hausdorff dimension of $J(f_q) \cap S^1$.
This ratio is independent of slit width and wavelength, depending only
on $q$.  A simultaneous electron--photon double-slit measurement at
the same apparatus would determine $q$ and $d_H$ independently,
providing a sharp test of the two-mode prediction.
