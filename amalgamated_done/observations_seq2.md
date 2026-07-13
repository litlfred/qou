<!-- FILE_START: double-slit-intro.md -->
The double-slit experiment tests any quantum framework. It requires a single formalism that reproduces interference fringes, predicts their envelope, and explains coherence loss upon observation. In the QOU setting, the experiment splits into two scattering modes: photons and massive particles.

A massive particle propagates via the full $q$-Laplacian ([particle](#def:q-harmonic-form)). Its cross-coupling terms mix spatial and Reeb degrees of freedom to produce interference. A photon is background flux on the exceptional divisor ([exceptional divisor](#def:exceptional-divisor)). It carries color content $\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ ([color content](#rem:knot-basis-color-content)). The Hecke generators $\sigma_0, \sigma_1$ encode polarization. The color twist $q\phi$ governs its phase. The color weights $(\varphi_0, \varphi_1, \varphi_{01})$ correct the interference envelope.

The two modes predict different envelope shapes: a $q$-corrected sinc${}^2$ for massive particles, and a fractal Julia-set envelope for photons. Both recover classical Fraunhofer and Airy patterns at $q = 1$. At $q \neq 1$, band widths deviate. These anomalies match the Bach et al. \cite{bach2013} 600 eV electron diffraction dataset.
<!-- FILE_END: double-slit-intro.md -->

<!-- FILE_START: double-slit-q-phase.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q \in k^{\times}$ ([substrate parameter](#def:substrate-parameter)). Let $\gamma_i$ ($i = 1,2$) be two paths through slits of width $a$ separated by distance $d$.

The $q$-deformed path phase along $\gamma_i$ is

$$
  \Phi_q^{(i)}(y)
  =  \frac{1}{\hbar_q}\!\int_{\gamma_i}\! d_q\psi
  =  q^{-1}\Phi_{\mathrm{geom}}^{(i)}(y)
        +  (1 - q^{-1})\Phi_{\mathrm{Reeb}}^{(i)}(y).
$$

The terms are:

- $\Phi_{\mathrm{geom}}^{(i)} = (2\pi/\lambda)\ell_i(y)$: The geometric phase.
- $\Phi_{\mathrm{Reeb}}^{(i)} = \int_{\gamma_i} \iota_\xi\varTheta$: The Reeb phase ([Reeb derivation](#def:categorical-reeb)).
- $\hbar_q = 1 - q^{-1}$: The [quantum Planck constant](#def:quantum-planck-constant).

This decomposition stems from the [$q$-exterior derivative](#def:categorical-q-ext-deriv) $d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d$.

The $q$-deformed phase difference is

$$
  \Delta\Phi_q(y)
  =  \Phi_q^{(1)}(y) - \Phi_q^{(2)}(y)
  =  q^{-1}\frac{2\pid\sin\theta}{\lambda}
        +  (1 - q^{-1})\Delta\phi_\xi(y).
$$

Here $\theta$ is the scattering angle and $\Delta\phi_\xi(y)$ is the Reeb phase mismatch. At $q = 1$, the Reeb term vanishes.
<!-- FILE_END: double-slit-q-phase.md -->

<!-- FILE_START: double-slit-massive-pattern.md -->
Let $\alpha$ be a massive $q$-harmonic form ([particle](#def:q-harmonic-form)) incident on a double slit. The $q$-deformed intensity at scattering angle $\theta$ is

$$
  I_q(\theta)
  =  4I_0\cos^2\!\!\left(\frac{\Delta\Phi_q(\theta)}{2}\right)
        \cdot
        \left(\frac{\sin\beta_q(\theta)}{\beta_q(\theta)}\right)^{\!2}.
$$

The interference phase is

$$
  \Delta\Phi_q(\theta)
  =  q^{-1}\frac{2\pid\sin\theta}{\lambda}
        +  (1 - q^{-1})\Delta\phi_\xi(\theta).
$$

The envelope parameter is

$$
  \beta_q(\theta)
  =  q^{-1}\frac{\pia\sin\theta}{\lambda}
        +  (1 - q^{-1})^2\beta_\xi(\theta).
$$

The term $\beta_\xi(\theta)$ is the spin-core contribution of the [$q$-Laplacian expansion](#rem:q-laplacian-expansion).

The $q$-Laplacian separates into three scales:

- **Classical core** ($\propto q^{-2}$): Standard Hodge diffusion $\Delta$.
- **Spin core** ($\propto (1 - q^{-1})^2$): Pure Reeb dynamics $\Delta_\xi$.
- **Cross-coupling** ($\propto q^{-1}(1 - q^{-1})$): Mixes spatial and Reeb modes.

The fringe spacing is

$$
  \Delta y_q =  \frac{q\lambdaL}{d}.
$$

The envelope half-width broadens:

$$
  w_q =  \frac{q^2\lambdaL}{a}
        \left(1 +  (1 - q^{-1})^2
        \frac{\langle\Delta_\xi\rangle}{\langle\Delta\rangle}\right).
$$

At $q = 1$, we recover the Fraunhofer pattern. For $q \neq 1$, the envelope widens, matching precision observations \cite{bach2013}.
<!-- FILE_END: double-slit-massive-pattern.md -->

<!-- FILE_START: double-slit-two-modes.md -->
We predict two structurally distinct scattering modes:

| | **Mode 1: Massive particle** | **Mode 2: Photon** |
|---|---|---|
| **Geometric identity** | $q$-harmonic form ($\Delta_q\alpha = 0$) | Color-dressed identity $\gamma$ |
| **Phase mechanism** | $q$-Laplacian cross-coupling | Color twist $q\phi$ |
| **Interference formula** | $\cos^2(\Delta\Phi_q / 2)$ | $\cos^2(\Delta\Phi_q^{(\mathrm{color})} / 2)$ |
| **Envelope** | $q$-corrected sinc${}^2$ | Julia-set measure $\mu_J$ |
| **Band-width shift** | Wider by $(1 - q^{-1})^2$ | Power-law tails |
| **Classical limit** ($q \to 1$) | Fraunhofer | Airy |

## Band-width predictions versus observation

Standard theory predicts band widths from slit geometry alone.

1. **Electron diffraction**: The excess envelope width arises from the spin-core term $(1 - q^{-1})^2\Delta_\xi$ of the $q$-Laplacian.
2. **Molecular diffraction**: Heavier particles have larger $\langle\Delta_\xi\rangle / \langle\Delta\rangle$, yielding wider envelopes scaling with molecular complexity.
3. **Photon diffraction**: The Julia-set envelope suppresses subsidiary maxima and broadens tails.

## Observation and coherence loss

A detector at one slit shifts the substrate parameter $q \mapsto q + \delta q$ via Hopf coaction ([observation](#def:observation)). The Reeb phases become incommensurate. Fringes vanish, and the single-slit pattern carries an asymmetry of order $\delta q / q$.

## Experimental discriminant

The modes predict a specific width ratio:

$$
  \frac{w_{\mathrm{photon}}}{w_{\mathrm{electron}}}
  = 
  \frac{d_H}{2}
  \frac{1 + (1 - q^{-1})^2\langle\Delta_\xi\rangle_e /
            \langle\Delta\rangle_e}{1}.
$$

Simultaneous electron–photon double-slit measurements isolate this ratio.

## Color-content discriminant

Linearly polarized light traces a sinusoidal fringe modulation:

$$
  \delta\Delta\Phi(\alpha)
  = 
  (\cos\alphaq - \sin\alphaq^{-1})
  \hbar_q\mathrm{Vol}(K_{\mathrm{mat}})\Delta\phi_\xi.
$$

The modulation amplitude depends on the slit material's knot volume.
<!-- FILE_END: double-slit-two-modes.md -->

<!-- FILE_START: q-deformed-double-slit.md -->
The [substrate parameter](#def:substrate-parameter) $q$ physicalizes wave propagation deformation. The slit material defines the brane boundary.

Wave propagation obeys the categorical Dirac equation ([categorical Dirac operator](#def:categorical-dirac-operator)):

$$\mathcal{D}_\nabla\psi =  0,$$

where $\mathcal{D}_\nabla = q^{-1}\nabla + (1-q^{-1})\iota_\xi\nabla$ ([variational equations](#prop:variational-equations)). The test particle $\psi$ is a photon with color content ([color content](#rem:knot-basis-color-content)). It propagates on an instanton background ([categorical instanton](#def:categorical-instanton)).

The $q$-deformed differential is:

$$d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d.$$

As $q \to 1$, $d_q \to d$. For $q > 1$, the vertical differential introduces transverse momentum shift.

The Reeb contraction drives wavefront spreading ([wavefront propagation](#rem:wavefront-propagation)). The phase difference along path $\gamma$ grazing the slit boundary is

```tex
\Delta\phi =  \Delta\phi_{\mathrm{classical}} +  \hbar_q \int_{\gamma} \pi_V \circ d,
```

The integral depends on the slit material's torsion intensity. The Lagrangian simplifies on an instanton background ([instanton on-shell](#rem:instanton-on-shell)):

$$\mathcal{L}_q\big|_{\text{instanton}} = c_2(A) + \psi^* \otimes \mathcal{D}_\nabla\psi.$$

An interactive simulation provides real-time parameter sweeps against the classical baseline.

## Color content and polarisation-dependent interference

The color content modifies interference via:

**1. Polarisation-weighted phase.**
Each polarisation mode acquires a Reeb phase. The total phase is

$$
  \Phi_q^{(\mathrm{color})}(\gamma_j)
  = 
  \Phi_q^{(j)}
  + 
  \varphi_0q\Phi_{\mathrm{Reeb}}^{(j)}
  + 
  \varphi_1(-q^{-1})\Phi_{\mathrm{Reeb}}^{(j)}.
$$

The bare-photon phase difference acquires a polarisation correction:

$$
  \Delta\Phi_q^{(\mathrm{color})}
  = 
  \Delta\Phi_q
  + 
  (\varphi_0q - \varphi_1q^{-1})\Delta\phi_\xi.
$$

**2. Cross-color interference.**
Interference generates cross-color terms. This modulates fringe visibility:

$$
  V_{\mathrm{color}}
  = 
  1 - |\varphi_0\psi_1 - \varphi_1\psi_0|^2.
$$

Material-dependent decoherence stems from the Hecke algebra structure.

**Observable signature.**
The correction is first order in $\hbar_q$ for linearly polarised light. A double-slit experiment isolates this material-dependent shift.
<!-- FILE_END: q-deformed-double-slit.md -->
