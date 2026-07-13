<!-- FILE_START: crystal-resonance-intro.md -->
Macroscopic structures typically average over substrate variation, blurring the precise local value of $q$. Crystal resonance avoids this. A perfect lattice forces constructive interference of Reeb shifts. This section specifies the crystal experiments.
- Experimental configuration outlines the necessary hardware, from continuous-wave drivers to ultra-pure crystalline targets.
- Resonance spectrum and measurement defines the observables, linking the $q$-dependent Bragg peaks to the underlying geometry.
- Expected bounds and sensitivity analyses the projected accuracy of the measurement.

We establish the $q$-crystal shift effect first.
<!-- FILE_END: crystal-resonance-intro.md -->

<!-- FILE_START: crystal-probe-q.md -->
A periodic crystal lattice acts as a macroscopic, coherent probe of the local value $q|_U$ established in [local substrate $q$](#prop:local-substrate-q). The discrete translational symmetry of the lattice isolates a set of reciprocal vectors that couple directly to the horizontal distribution of the CR manifold $M$. Where the lattice spacing is commensurate with the characteristic scale of a $q$-torsion leaf ([$q$-torsion leaf](#ex:q-torsion-leaf)), a resonance condition triggers. The $q$-harmonic forms ([$q$-harmonic form](#def:q-harmonic-form)) on the brane constructively interfere with the crystal's phonon modes, amplifying vacuum fluctuations at specific frequencies. The resonance frequency $\nu_{\mathrm{res}}$ depends entirely on $q|_U$ and lattice geometry. This supplies an independent experimental route to measure the substrate parameter.
<!-- FILE_END: crystal-probe-q.md -->

<!-- FILE_START: substrate-telescope.md -->
The directional dependence of $q$-torsion suggests a new class of detector: the Substrate Telescope. A large, high-purity single crystal is slowly rotated while the variation of vacuum noise power or phonon resonance efficiency is recorded as a function of orientation. The $q$-torsion leaves carry a preferred direction inherited from the $q$-deformed Reeb flow ([$q$-Reeb flow](#ex:q-reeb-flow)). Consequently, the noise spectrum should exhibit a modulation correlated with the crystal's orientation relative to the bulk bundle. Analogous to a Weber-bar gravitational wave detector, this instrument targets the anisotropy of the substrate parameter rather than metric strain.
<!-- FILE_END: substrate-telescope.md -->

<!-- FILE_START: magnetic-friction.md -->
Recent experiments by Gu, Luders, and Bechinger demonstrate that a two-dimensional array of rotatable magnetic dipoles sliding over a commensurate magnetic substrate exhibits a pronounced non-monotonic dependence of friction on interlayer separation. Friction peaks at an intermediate distance. Here, competing ferromagnetic and antiferromagnetic interactions induce dynamical frustration and hysteretic torque cycles during sliding.

This collective rotor phenomenon admits a natural explanation within the QOU framework. The competing magnetic alignments realise a discrete analogue of $q$-torsion frustration. This frustration arises when a lattice's translational symmetry is incommensurate with the characteristic scale of the $q$-torsion leaves ([$q$-torsion leaf](#ex:q-torsion-leaf)). In this reading, the non-monotonic friction profile reflects a resonance--anti-resonance transition. The local value of the substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)) governs this transition. Maximal dissipation occurs at the separation where the rotor array's magnetic periodicity matches the $q$-harmonic form spectrum ([$q$-harmonic form](#def:q-harmonic-form)).

A quantitative comparison requires specifying the lattice geometry and its coupling to the horizontal distribution of the CR manifold $M$. We outline the necessary ingredients in [lattice layout](#rem:lattice-layout) below.
<!-- FILE_END: magnetic-friction.md -->

<!-- FILE_START: lattice-layout.md -->
Connecting the resonance condition ([crystal probe of $q$](#rem:crystal-probe-q)) to concrete lattice experiments requires three undeveloped structural ingredients:

1. **Lattice--leaf commensurability.** For a $d$-dimensional Bravais lattice with basis vectors $\{\vec{a}_i\}$, the resonance condition ([crystal probe of $q$](#rem:crystal-probe-q)) requires Diophantine matching between the reciprocal lattice vectors $\{\vec{G}_j\}$ and the characteristic wave-vectors of the $q$-torsion leaves. The lattice symmetry group acts on the space of $q$-harmonic forms. This selects a finite set of resonance channels indexed by the irreducible representations of the point group.
2. **Frustration and non-monotonicity.** When the lattice hosts internal rotational degrees of freedom (e.g., magnetic rotor arrays), the coupling to $q$-torsion may become non-monotonic in a control parameter like interlayer separation or applied field. The $q$-deformed Reeb flow ([$q$-Reeb flow](#ex:q-reeb-flow)) introduces a preferred orientation that competes with the lattice symmetry. This competition produces frustrated configurations where energy dissipation maximizes at an intermediate commensurability.
3. **Quantum coherence at the lattice scale.** Kagome many-body interference indicates that quantum coherence extends over macroscopic lattice domains. In our framework, the correlation length of the $q$-harmonic forms on the brane bounds this coherence length. This correlation length depends on the local curvature of the CR manifold $M$. Establishing this bound quantitatively requires computing the $q$-deformed propagator on the lattice. We leave this to future work.
<!-- FILE_END: lattice-layout.md -->

<!-- FILE_START: crystal-resonance-planned.md -->
**Planned observations.**

- Next-generation phononic crystal experiments utilizing tunable lattice constants. These enable a systematic scan of the resonance condition across different effective $q$ regimes.
- Extension of kagome and pyrochlore quantum-interference experiments to larger single crystals incorporating controlled rotational staging.
- Cryogenic SQUID-based noise spectroscopy conducted on rotating high-purity sapphire or silicon crystals.
- Systematic variation of interlayer separation in magnetic rotor arrays. This tests whether the non-monotonic friction profile correlates with the predicted $q$-torsion resonance channels.
<!-- FILE_END: crystal-resonance-planned.md -->

<!-- FILE_START: crystal-resonance-experiments.md -->
**Potential new experiments.**

- A dedicated Substrate Telescope prototype: a cryogenically cooled, slowly rotating single crystal (using ultra-pure silicon or quartz) instrumented with SQUID magnetometers and phonon sensors. This tests for orientation-dependent modulation of the vacuum noise floor.
- Comparative resonance measurements across crystals possessing varying lattice symmetries (cubic, hexagonal, trigonal). This maps the dependence of $\nu_{\mathrm{res}}$ on lattice geometry to constrain the local value of $q$.
- Archival re-analysis of resonant-bar detector data (AURIGA, NAUTILUS, EXPLORER) isolating residual orientation-dependent signals that are consistent with $q$-torsion anisotropy rather than gravitational wave backgrounds.
<!-- FILE_END: crystal-resonance-experiments.md -->

