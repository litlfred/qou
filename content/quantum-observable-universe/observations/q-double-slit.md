Interactive overhead-view particle simulation of the $q$-deformed double-slit experiment (§6.7, §11).

Individual particles are emitted from a source, pass through a pair of slits in a barrier material with knot volume $\mathrm{Vol}(K)$, and arrive at a detection screen.  The interference pattern is governed by the categorical Dirac equation $\mathcal{D}_\nabla \psi = 0$, where the Reeb contraction term $(1 - q^{-1})\iota_\xi \nabla$ modifies the phase accumulation relative to the classical ($q = 1$) baseline.

**Default view**: Moderate $q$-deformation ($q \approx q_0$) with torsion parameters matching a typical nucleon boundary.  The buildup of $\sim 500$ particles shows the characteristic fringe shift relative to Fraunhofer diffraction.

**Parameters**:

- $q$ — substrate parameter; controls $\hbar_q = 1 - q^{-1}$
- $D$ — slit separation (mm)
- $d$ — slit width ($\mu$m)
- $w$ — barrier thickness ($\mu$m)
- $\lambda$ — wavelength (nm)
- $w_0$ — Gaussian beam waist at barrier (mm)
- $\mathrm{Vol}(K)$ — hyperbolic volume of the boundary knot
- Torsion — torsion intensity of the slit material

The simulation runs in real time on an HTML5 canvas with configurable particle emission rate and speed.
