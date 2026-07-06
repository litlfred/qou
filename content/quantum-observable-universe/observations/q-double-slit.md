We present an interactive particle simulation of the $q$-deformed double-slit experiment (§6.7, §11).

Particles are emitted from a source, traverse a pair of slits in a barrier material with knot volume $\mathrm{Vol}(K)$, and strike a detection screen. The categorical Dirac equation $\mathcal{D}_\nabla \psi = 0$ governs the interference pattern. The Reeb contraction term $(1 - q^{-1})\iota_\xi \nabla$ modifies the phase accumulation relative to the classical ($q = 1$) baseline.

**Default view.** We set a moderate $q$-deformation ($q \approx q_0$) with torsion parameters matching a typical nucleon boundary. The accumulation of $\sim 500$ particles reveals the fringe shift relative to Fraunhofer diffraction.

**Parameters.**

- $q$ — substrate parameter; controls $\hbar_q = 1 - q^{-1}$.
- $D$ — slit separation (mm).
- $d$ — slit width ($\mu$m).
- $w$ — barrier thickness ($\mu$m).
- $\lambda$ — wavelength (nm).
- $w_0$ — Gaussian beam waist at barrier (mm).
- $\mathrm{Vol}(K)$ — hyperbolic volume of the boundary knot.
- Torsion — torsion intensity of the slit material.

The simulation executes in real time on an HTML5 canvas. Particle emission rate and speed are configurable.
