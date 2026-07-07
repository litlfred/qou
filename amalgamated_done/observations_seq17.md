<!-- FILE_START: crystal-resonance-intro.md -->
Macroscopic structures typically average over substrate variation, blurring the precise local value of $q$. Crystal resonance avoids this. A perfect lattice forces constructive interference of Reeb shifts. This section specifies the crystal experiments.
- Experimental configuration outlines the necessary hardware, from continuous-wave drivers to ultra-pure crystalline targets.
- Resonance spectrum and measurement defines the observables, linking the $q$-dependent Bragg peaks to the underlying geometry.
- Expected bounds and sensitivity analyses the projected accuracy of the measurement.

We establish the $q$-crystal shift effect first.
<!-- FILE_END: crystal-resonance-intro.md -->

<!-- FILE_START: crystal-shift.md -->
Perfect crystals amplify $q$-deformation. A scattering process through $N$ lattice planes typically yields an amplitude $A \propto \sum_{n=1}^N e^{i n \phi}$. In the Descartes universe, the momentum transfer picks up a geometric phase shift $\delta_q$ proportional to $1 - q^{-1}$. The amplitude becomes

$$
  A_q \propto \sum_{n=1}^N q^{-n/2} e^{i n (\phi + \delta_q)}.
$$

The non-unitary decay $q^{-n/2}$ dominates over macroscopic distances. Consequently, the standard Bragg peak broadens asymmetrically. The shift $\delta_q$ and the broadening directly measure the substrate parameter $q$. This requires single-crystal targets of exceptional purity and size, cooled below their Debye temperatures to suppress thermal phonons.
<!-- FILE_END: crystal-shift.md -->

<!-- FILE_START: experimental-config.md -->
**Proposition.**
*An experimental configuration $(\mathcal{C}, S)$ capable of measuring the substrate parameter $q$ to precision $\delta q / q < 10^{-6}$ requires the following minimal components:*

*1. Source $S$: A continuous-wave X-ray or neutron source with fractional momentum spread $\Delta p / p < 10^{-6}$.*
*2. Target $\mathcal{C}$: A monolithic, dislocation-free single crystal (e.g., Silicon or Germanium) of thickness $L > 10^7$ lattice constants.*
*3. Temperature control: Cryogenic cooling to $T \ll \Theta_D$ (Debye temperature) to suppress the Debye-Waller thermal broadening.*
*4. Detector array: High-resolution angular and energy resolving detectors covering the forward scattering region.*

*Proof.*
The $q$-deformation induces a peak shift $\delta \theta_q \sim (q-1) \lambda / d$. To resolve this shift from standard dynamic diffraction (Darwin width), the source monochromaticity must exceed the shift scale. The macroscopic thickness $L$ ensures the non-unitary $q^{-N/2}$ attenuation visibly distorts the peak shape. The temperature constraint ensures thermal phonon scattering does not mask the topological shift.
<!-- FILE_END: experimental-config.md -->

<!-- FILE_START: crystal-resonance-spectrum.md -->
The measured resonance spectrum $I(\theta, E)$ in the forward-scattering direction isolates $q$. The [crystal shift](#prop:crystal-shift) amplitude yields an intensity profile:

$$
  I(\theta) = |A_q|^2 \propto \frac{1 - q^{-N}}{1 - 2q^{-1/2}\cos(\phi + \delta_q) + q^{-1}}.
$$

This is a $q$-deformed Airy function. The signature of $q \neq 1$ is threefold:
1. **Peak shift.** The maximum intensity occurs at $\theta_{B, q} = \theta_B + \delta \theta_q$.
2. **Asymmetry.** The peak profile is skewed towards higher momentum transfer.
3. **Attenuation saturation.** Increasing the crystal thickness $N$ beyond $N_q \sim 1/\ln q$ does not increase the peak intensity.

Extracting $q$ requires fitting the observed $I(\theta)$ to this profile, correcting for standard dynamical diffraction effects (Pendellösung fringes, anomalous transmission).
<!-- FILE_END: crystal-resonance-spectrum.md -->
