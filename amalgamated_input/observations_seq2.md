<!-- FILE_START: double-slit-intro.md -->
The double-slit experiment provides a sharp test for any quantum framework. It requires a single formalism that reproduces interference fringes, predicts their envelope, and explains the loss of coherence upon observation. In the QOU setting, the experiment splits into two structurally distinct scattering modes: photons and massive particles propagate through different geometric substrates.

A massive particle—a $q$-harmonic form $\alpha$ with $\Delta_q\alpha = 0$ ([particle](#def:q-harmonic-form))—propagates via the full $q$-Laplacian. Its cross-coupling terms mix spatial and Reeb degrees of freedom to produce interference. A photon—background flux on the exceptional divisor ([exceptional divisor](#def:exceptional-divisor))—is not a bare identity $\mathbf{1}$. It is a photon with color content $\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ ([color content](#rem:knot-basis-color-content)). The Hecke generators $\sigma_0, \sigma_1$ encode horizontal and vertical polarisation, while $\sigma_0\sigma_1$ is the Hopf link dressing. The color twist $q\phi$ governs its phase, rather than the $q$-Laplacian. The color weights $(\varphi_0, \varphi_1, \varphi_{01})$ introduce a polarisation-dependent correction to the interference envelope, which is absent in standard treatments.

The two modes predict different envelope shapes at the detector screen: a $q$-corrected sinc${}^2$ for massive particles, and a fractal Julia-set envelope for photons. Both reduce to standard Fraunhofer and Airy patterns in the classical limit $q \to 1$. However, at $q \neq 1$, the band widths deviate from textbook predictions. These anomalies match those reported in precision scattering experiments. The benchmark dataset is the controlled double-slit electron diffraction experiment of Bach et al. \cite{bach2013}. They recorded 6235 individual electron detections at 600 eV ($\lambda = 50$ pm, slit width $a = 50$ nm, separation $d = 280$ nm).
<!-- FILE_END: double-slit-intro.md -->

<!-- FILE_START: double-slit-q-phase.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q \in k^{\times}$ ([substrate parameter](#def:substrate-parameter)). Let $\gamma_i$ ($i = 1,2$) be two paths from a source to a screen position $y$. Each path passes through one slit of width $a$. The slits are separated by distance $d$.

The $q$-deformed path phase accumulated along $\gamma_i$ is

$$
  \Phi_q^{(i)}(y)
  =  \frac{1}{\hbar_q}\!\int_{\gamma_i}\! d_q\psi
  =  q^{-1}\Phi_{\mathrm{geom}}^{(i)}(y)
        +  (1 - q^{-1})\Phi_{\mathrm{Reeb}}^{(i)}(y).
$$

The terms are:

- $\Phi_{\mathrm{geom}}^{(i)} = (2\pi/\lambda)\ell_i(y)$: The geometric (de Broglie) phase. $\ell_i(y)$ is the Euclidean path length through slit $i$ to screen point $y$.
- $\Phi_{\mathrm{Reeb}}^{(i)} = \int_{\gamma_i} \iota_\xi\varTheta$: The Reeb phase. This is the rotation accumulated by the internal color fibre along $\gamma_i$ ([Reeb derivation](#def:categorical-reeb)).
- $\hbar_q = 1 - q^{-1}$: The [quantum Planck constant](#def:quantum-planck-constant).

This decomposition follows directly from the [$q$-exterior derivative](#def:categorical-q-ext-deriv) $d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d$. It splits every phase integral into a horizontal (geometric) part weighted by $q^{-1}$ and a vertical (Reeb) part weighted by $1 - q^{-1}$.

The $q$-deformed phase difference between the two paths is

$$
  \Delta\Phi_q(y)
  =  \Phi_q^{(1)}(y) - \Phi_q^{(2)}(y)
  =  q^{-1}\frac{2\pid\sin\theta}{\lambda}
        +  (1 - q^{-1})\Delta\phi_\xi(y).
$$

Here $\theta$ is the scattering angle and $\Delta\phi_\xi(y) = \Phi_{\mathrm{Reeb}}^{(1)}(y) - \Phi_{\mathrm{Reeb}}^{(2)}(y)$ is the Reeb phase mismatch. At $q = 1$, the Reeb term vanishes, recovering the standard Young phase difference.
<!-- FILE_END: double-slit-q-phase.md -->

<!-- FILE_START: double-slit-massive-pattern.md -->
Let $\alpha$ be a massive $q$-harmonic form ([particle](#def:q-harmonic-form)) with de Broglie wavelength $\lambda$. It is incident on a double slit of width $a$ and separation $d$. A detector screen sits at distance $L$. The $q$-deformed intensity at scattering angle $\theta$ is

$$
  I_q(\theta)
  =  4I_0\cos^2\!\!\left(\frac{\Delta\Phi_q(\theta)}{2}\right)
        \cdot
        \left(\frac{\sin\beta_q(\theta)}{\beta_q(\theta)}\right)^{\!2}.
$$

The interference phase, derived from the [$q$-deformed path phase](#def:double-slit-q-phase), is

$$
  \Delta\Phi_q(\theta)
  =  q^{-1}\frac{2\pid\sin\theta}{\lambda}
        +  (1 - q^{-1})\Delta\phi_\xi(\theta).
$$

The envelope parameter is

$$
  \beta_q(\theta)
  =  q^{-1}\frac{\pia\sin\theta}{\lambda}
        +  (1 - q^{-1})^2\beta_\xi(\theta),
$$

where $\beta_\xi(\theta)$ is the contribution from the spin-core term of the [$q$-Laplacian expansion](#rem:q-laplacian-expansion).

The $q$-Laplacian separates into three scales:

- **Classical core** ($\propto q^{-2}$): Standard Hodge diffusion $\Delta$. This yields the Fraunhofer sinc${}^2$ envelope.
- **Spin core** ($\propto (1 - q^{-1})^2$): Pure Reeb dynamics $\Delta_\xi$. This adds an angular broadening $\beta_\xi$ to the envelope.
- **Cross-coupling** ($\propto q^{-1}(1 - q^{-1})$): The terms $d(\mathcal{L}_\xi^*\iota_\xi) + (\varTheta \wedge \mathcal{L}_\xi)\delta + \delta(\varTheta \wedge \mathcal{L}_\xi) + (\mathcal{L}_\xi^*\iota_\xi)d$. These mix spatial and Reeb modes, producing the interference fringes.

The fringe spacing on the screen is $q$-corrected:

$$
  \Delta y_q =  \frac{q\lambdaL}{d}.
$$

The envelope half-width is broadened relative to the Fraunhofer prediction:

$$
  w_q =  \frac{q^2\lambdaL}{a}
        \left(1 +  (1 - q^{-1})^2
        \frac{\langle\Delta_\xi\rangle}{\langle\Delta\rangle}\right),
$$

where $\langle\Delta_\xi\rangle / \langle\Delta\rangle$ is the ratio of Reeb to spatial Laplacian eigenvalues on the particle's harmonic mode.

At $q = 1$, we have $\Delta\Phi_1 = 2\pi d\sin\theta/\lambda$ and $\beta_1 = \pi a\sin\theta/\lambda$. The standard Fraunhofer double-slit pattern is recovered exactly. For $q \neq 1$, the envelope is wider than the Fraunhofer envelope by a factor of order $(1 - q^{-1})^2$. This is consistent with the systematic excess width observed in precision electron and molecular diffraction experiments \cite{bach2013}.
<!-- FILE_END: double-slit-massive-pattern.md -->

<!-- FILE_START: double-slit-two-modes.md -->
The QOU double-slit model predicts two structurally distinct scattering modes:

| | **Mode 1: Massive particle** | **Mode 2: Photon (with color content)** |
|---|---|---|
| **Geometric identity** | $q$-harmonic form ($\Delta_q\alpha = 0$) | Color-dressed identity $\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ |
| **Phase mechanism** | $q$-Laplacian cross-coupling | Color twist $q\phi$ + polarisation eigenvalues $(\varphi_0 q, -\varphi_1 q^{-1})$ |
| **Interference formula** | $\cos^2(\Delta\Phi_q / 2)$ | $\cos^2(\Delta\Phi_q^{(\mathrm{color})} / 2)$ |
| **Envelope** | $q$-corrected sinc${}^2$ | Julia-set measure $\mu_J$ modulated by color visibility $V_{\mathrm{color}}$ |
| **Band-width shift** | Wider by $(1 - q^{-1})^2$ | Power-law tails ($\sim\lvert\theta\rvert^{-d_H}$) + polarisation asymmetry |
| **Classical limit** ($q \to 1$) | Fraunhofer | Airy |

## Band-width predictions versus observation

Standard diffraction theory predicts band widths from slit geometry alone (Fraunhofer for matter waves, Airy for photons). Precision experiments report systematic deviations.

1. **Electron diffraction**: Subsidiary maxima are wider than the Fraunhofer sinc${}^2$ envelope predicts. This excess is often attributed to Coulomb interaction with slit edges, but that correction is ad hoc and not derived from the wave equation. In the QOU model, the excess width arises directly from the spin-core term $(1 - q^{-1})^2\Delta_\xi$ of the $q$-Laplacian. This adds Reeb-direction broadening to the envelope with no free parameters once $q$ is fixed by the [local substrate value](#prop:local-substrate-q).
2. **Molecular diffraction** (C$_{60}$, large organics): Fringe visibility matches predictions, but measured band widths are systematically broader. The standard explanation invokes van der Waals attraction to the grating. The QOU prediction is quantitative: heavier particles have larger $\langle\Delta_\xi\rangle / \langle\Delta\rangle$ (more Reeb modes per unit mass). This yields wider envelopes that scale with molecular complexity rather than dipole moment.
3. **Photon diffraction**: Subsidiary Airy maxima are more suppressed than $1/(m\pi)^2$, and the intensity tails are heavier than $|\theta|^{-2}$. The Julia-set envelope $\mu_J$ produces both effects. The fractal boundary concentrates measure near the central peak (suppressing subsidiaries), while the power-law decay $|\theta|^{-d_H}$ with $d_H > 1$ gives broader tails. When the photon carries non-trivial color content $(\varphi_0, \varphi_1)$ ([color content](#rem:knot-basis-color-content)), the polarisation-dependent Reeb phases introduce an additional fringe-visibility modulation $V_{\mathrm{color}}$. This depends on the slit material's Hecke dressing. This signature is absent both in standard quantum optics and in the bare-photon ($\varphi_0 = \varphi_1 = 0$) QOU prediction.

## Observation and coherence loss

When a detector is placed at one slit, the [observation](#def:observation) $\mathfrak{O}_p$ shifts the substrate parameter $q \mapsto q + \delta q$ on that path via Hopf coaction. The two paths now carry different $q$-values. The Reeb phases $\Phi_{\mathrm{Reeb}}^{(1)}$ and $\Phi_{\mathrm{Reeb}}^{(2)}$ become incommensurate. Their cross terms average to zero over the detector integration time. The result is the same as the which-path experiment: fringes vanish, but the envelope (single-slit pattern) is modified. It carries a residual asymmetry of order $\delta q / q$, reflecting the permanent geometric deformation left by the observation.

## Experimental discriminant

The two modes predict a specific ratio of photon-to-electron envelope widths for the same slit geometry:

$$
  \frac{w_{\mathrm{photon}}}{w_{\mathrm{electron}}}
  = 
  \frac{d_H}{2}
  \frac{1 + (1 - q^{-1})^2\langle\Delta_\xi\rangle_e /
            \langle\Delta\rangle_e}{1}.
$$

Here $d_H = d_H(q)$ is the Hausdorff dimension of $J(f_q) \cap S^1$. This ratio is independent of slit width and wavelength; it depends only on $q$. A simultaneous electron–photon double-slit measurement at the same apparatus would determine $q$ and $d_H$ independently, providing a sharp test of the two-mode prediction.

## Color-content discriminant

A refined test exploits the photon color content. Using linearly polarised light with controlled polarisation angle $\alpha$ (color weights $\varphi_0 = \cos\alpha$, $\varphi_1 = \sin\alpha$), the fringe shift acquires an $\alpha$-dependent term:

$$
  \delta\Delta\Phi(\alpha)
  = 
  (\cos\alphaq - \sin\alphaq^{-1})
  \hbar_q\mathrm{Vol}(K_{\mathrm{mat}})\Delta\phi_\xi.
$$

Sweeping $\alpha$ from $0$ to $\pi/2$ traces a sinusoidal modulation of the fringe positions. The amplitude of this modulation scales with $(q + q^{-1})\hbar_q\mathrm{Vol}(K_{\mathrm{mat}})$. This amplitude is material-dependent, as different slit materials give different $\mathrm{Vol}(K_{\mathrm{mat}})$. In contrast, the classical birefringence prediction depends on the refractive index. A single apparatus with a rotatable polariser and interchangeable slit materials would separate these two effects.
<!-- FILE_END: double-slit-two-modes.md -->

<!-- FILE_START: q-deformed-double-slit.md -->
The [substrate parameter](#def:substrate-parameter) $q$ encodes a physical deformation of wave propagation. The slit material acts as a defining boundary of the brane. Here, the Reeb vector field exerts a geometric push on the traversing test particle.

Wave propagation satisfies the categorical Dirac equation ([categorical Dirac operator](#def:categorical-dirac-operator)):

$$\mathcal{D}_\nabla\psi =  0,$$

where $\mathcal{D}_\nabla = q^{-1}\nabla + (1-q^{-1})\iota_\xi\nabla$ ([variational equations](#prop:variational-equations)). The test particle $\psi$ is a photon with color content $\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ ([color content](#rem:knot-basis-color-content)). The elements $\sigma_0$ and $\sigma_1$ are the horizontal and vertical polarisation generators. The product $\sigma_0\sigma_1$ is the Hopf link dressing on $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$ ([Breit--Wheeler vertex](#rem:breit-wheeler-vertex)). The photon propagates on an instanton background ([categorical instanton](#def:categorical-instanton)). The identity component $\mathbf{1}$ propagates as pure horizontal flux. The generators $\varphi_i\sigma_i$ carry polarisation-dependent phase from the Hecke eigenvalues $+q$ and $-q^{-1}$.

Recall the $q$-deformed differential ([the local substrate proposition](#prop:local-substrate-q)):

$$d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d.$$

As $q \to 1$, the quantum Planck constant $\hbar_q = 1 - q^{-1}$ vanishes, and $d_q \to d$. The vertical component drops out, recovering classical interference. For $q > 1$, the vertical differential $\pi_V \circ d$ introduces a transverse momentum shift that modifies the interference pattern.

The Reeb contraction term $(1-q^{-1})\iota_\xi\nabla$ drives wavefront spreading ([wavefront propagation](#rem:wavefront-propagation)). This term allows a point-source photon to illuminate both slits. The beam width $w_0$ at the barrier is determined by the Green's function of $\mathcal{D}_\nabla$ on the flat instanton background ($F_\nabla = 0$).

The phase difference for a path $\gamma$ grazing the fermionic slit boundary is

```tex
\Delta\phi =  \Delta\phi_{\mathrm{classical}} +  \hbar_q \int_{\gamma} \pi_V \circ d,
```

The integral evaluates the vertical Reeb differential along $\gamma$. This correction depends on the torsion intensity of the slit material. A nucleon modeled as a [localized knot](#def:localized-knot) with the Borromean rings topology $6_2^3$ determines $q$ via the local substrate map. Heavier atoms with complex knotted configurations produce larger deformations. This yields a material-dependent fringe spacing absent in classical diffraction.

On an instanton background, the Lagrangian simplifies ([instanton on-shell](#rem:instanton-on-shell)):

$$\mathcal{L}_q\big|_{\text{instanton}} = c_2(A) + \psi^* \otimes \mathcal{D}_\nabla\psi,$$

The gauge sector is topological ($c_2$ is fixed by the material's knot type). All observable physics resides in $\mathcal{D}_\nabla\psi = 0$. The intensity pattern derivation is given in [the photon wavefront example](#ex:photon-wavefront).

An interactive simulation is available in the [q-deformed double-slit simulator](q-double-slit.html). It provides real-time parameter sweeps against the classical baseline.

## Color content and polarisation-dependent interference

The photon color content $(\varphi_0, \varphi_1)$ modifies the interference pattern in two ways.

**1. Polarisation-weighted phase.**
Each polarisation mode $\sigma_i$ acquires a Reeb phase along path $\gamma_j$ through slit $j$. The total phase for a color-dressed photon is

$$
  \Phi_q^{(\mathrm{color})}(\gamma_j)
  = 
  \Phi_q^{(j)}
  + 
  \varphi_0q\Phi_{\mathrm{Reeb}}^{(j)}
  + 
  \varphi_1(-q^{-1})\Phi_{\mathrm{Reeb}}^{(j)},
$$

where $+q$ and $-q^{-1}$ are the Hecke eigenvalues of $\sigma_0$ and $\sigma_1$ ([Breit--Wheeler vertex](#rem:breit-wheeler-vertex)). The bare-photon phase difference $\Delta\Phi_q$ of the [$q$-deformed path phase](#def:double-slit-q-phase) acquires a polarisation correction

$$
  \Delta\Phi_q^{(\mathrm{color})}
  = 
  \Delta\Phi_q
  + 
  (\varphi_0q - \varphi_1q^{-1})\Delta\phi_\xi,
$$

where $\Delta\phi_\xi$ is the Reeb phase mismatch. For unpolarised light ($\varphi_0 = \varphi_1$), the correction reduces to $\varphi_0(q - q^{-1})\Delta\phi_\xi$.

**2. Cross-color interference.**
When path amplitudes interfere at the detector, the product of the path states in $H_3(q)$ generates cross-color terms $\sigma_0\sigma_1$ and $\sigma_1\sigma_0$. These are the Hopf-link basis elements $L_{\pm}$ ([color content](#rem:knot-basis-color-content)). Their coefficients are $\varphi_0\psi_1$ and $\varphi_1\psi_0$. The color weights $\psi_i$ are imparted by the slit-wall Reeb interaction ([photon wavefront example](#ex:photon-wavefront)). These cross-color terms contribute a linking amplitude that modulates the fringe visibility:

$$
  V_{\mathrm{color}}
  = 
  1 - |\varphi_0\psi_1 - \varphi_1\psi_0|^2.
$$

When the slit material's color axis aligns with the photon's polarisation ($\varphi_0\psi_1 = \varphi_1\psi_0$), the Hopf-link terms cancel and visibility is maximal ($V_{\mathrm{color}} = 1$). Misalignment partially suppresses fringes. This material-dependent decoherence arises from the Hecke algebra structure, not from environmental noise.

**Observable signature.**
The color-content correction is second order in $\hbar_q$ for unpolarised light, but first order for linearly polarised light. A double-slit experiment with controlled linear polarisation exhibits a polarisation-dependent fringe shift proportional to $(\varphi_0 q - \varphi_1 q^{-1})\hbar_q\mathrm{Vol}(K_{\mathrm{mat}})$. This shift depends on the slit material's knot volume, separating it from classical birefringence.
<!-- FILE_END: q-deformed-double-slit.md -->

