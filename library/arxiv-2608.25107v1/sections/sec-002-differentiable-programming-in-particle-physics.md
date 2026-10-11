---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-002-differentiable-programming-in-particle-physics
section_title: "Differentiable programming in particle physics"
section_number: null
pages: 2-3
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 0.979
---
[]{#sec:intro_diffprog label="sec:intro_diffprog"}

Differentiable programming makes a simulation differentiable in its own inputs, so that derivatives of the prediction are produced by the program rather than reconstructed outside it. Automatic differentiation [@Baydin:2015tfa] decomposes a program into elementary operations and applies the chain rule through each of them, giving the exact derivative of the output with respect to any input; in reverse mode a full gradient costs a small constant multiple of one forward evaluation, independent of the number of inputs, and higher derivatives follow by nesting the same construction.

Physics is adopting this formalism broadly [@Schoenholz:2019jaxmd; @Kasim:2021dqc; @Weymouth:2023waterlily; @Meunier:2025veros; @Liao:2019tensor; @Kaiser:2024cheetah; @Agol:2021nbody; @Li:2022pmwd]. Within high-energy physics, applications are emerging rapidly. The stochastic sampling long presumed to obstruct them has proved tractable [@Arya:2022stochad], and gradient information has been put to use across the full range of common experimental tasks: detector design [@MODE:2022znx], physics modelling [@Heinrich:2022xfa; @Cranmer:2021gdt; @Nachman:2022jbj; @BarhamAlzas:2024ggt], and data analysis [@Simpson:2022suz]. In neutrino physics, differentiable frameworks now exist for the two most widely used detector technologies, liquid argon time projection chambers [@Gasiorowski:2023tqf] and optical Cherenkov and scintillation detectors [@Alterkait:2026ocv; @CCM:2025dbq], with demonstrated applications to detector calibration and event reconstruction. [ADoNIS]{.smallcaps} extends this emerging paradigm to the modelling of neutrino interactions.

# A Differentiable Neutrino Event Generator {#sec:adonis}

We developed [ADoNIS]{.smallcaps}, **A** **D**ifferentiable generat**O**r of **N**eutrino **I**nteraction **S**amples, a JAX-based open-source neutrino event generator[^1]. [ADoNIS]{.smallcaps} follows the interaction physics choices of the ACHILLES generator [@Isaacson:2020wlx; @Isaacson:2022cwh; @Isaacson:2025cnk], implemented in a fully differentiable manner, and so provides differentiable event weights for fully exclusive neutrino--nucleus final states.

ACHILLES is a modern, open-source[^2], self-consistent generator built around fully exclusive final states. Its vertex implements two channels. Quasi-elastic scattering is computed from the one-body electroweak current in the extended factorisation scheme [@Isaacson:2022cwh], with Kelly vector and $z$-expansion axial nucleon form factors [@Kelly:2004hm; @Meyer:2016oeg]. Resonant single-pion production is taken from the ANL--Osaka dynamical coupled-channels model [@Nakamura:2015rta], whose meson--baryon amplitudes also enter the corresponding scattering cross sections used in the intranuclear cascade. The nuclear ground state is carried by hole spectral functions $S(p,E)$---the probability of removing a nucleon of momentum $p$ and leaving the residual system with excitation energy $E$, normalised separately for protons and neutrons---obtained for $^{12}$C from correlated-basis function theory [@Benhar:1994hw; @Rocco:2019gfb] and for $^{40}$Ar from $(e,e'p)$ measurements [@JeffersonLabHallA:2022cit; @JeffersonLabHallA:2022ljj; @Nikolakopoulos:2024mjj]. Hadrons produced at the vertex are transported through a sampled nucleon configuration, taken from Green's function Monte Carlo for carbon [@Carlson:2014vla] and, since argon is not amenable to continuum quantum Monte Carlo, from single-nucleon densities there [@Isaacson:2020wlx]; pion absorption follows the Oset model [@Oset:1987re]. Charged-current, neutral-current and electromagnetic probes are all supported, so the same code is confronted with $(e,e')$ data as well as with neutrino measurements, and a tagged hadron beam allows the cascade to be exercised on its own. [ADoNIS]{.smallcaps} mirrors these choices. The full derivations are given in the ACHILLES papers [@Isaacson:2020wlx; @Isaacson:2022cwh; @Isaacson:2025cnk]; what follows recalls each ingredient only as far as is needed to show how it is made differentiable, and then describes how gradient information is carried from the physics parameters through to the final observables.

Meson-exchange currents and deep-inelastic scattering are absent from ACHILLES and are planned additions to it [@Isaacson:2025cnk]; the same is true of [ADoNIS]{.smallcaps}, and both lie outside the scope of this paper. More generally, the physics choices described above are inherited from ACHILLES rather than selected as preferred models: their purpose here is to provide a realistic generator chain on which to demonstrate differentiability. In particular, reproducing the fully stochastic ACHILLES intranuclear cascade in [ADoNIS]{.smallcaps} demonstrates that differentiability can be retained even through discrete transport histories.

JAX [@jax2018github] supplies the automatic differentiation, just-in-time compilation and vectorisation, and allows the same implementation to run on CPU or GPU. Their relative performance depends strongly on the stage of event generation. For neutrino interactions on carbon with energies sampled from the T2K flux, pre-FSI generation showed no GPU acceleration, running at about $1.8\times10^{3}$ events/s on both a single AMD EPYC CPU core and an NVIDIA A100 GPU. The computational bottleneck is instead the intranuclear cascade, whose throughput increases from about $55$ events/s on a single CPU core to $560$ events/s on an RTX 2080 Ti GPU and $720$ events/s on an A100 GPU. A GPU is therefore not required for event generation, but can substantially accelerate the cascade calculation. The computational performance of the differentiable inference is discussed separately in Sec. [\[sec:fit_performance\]](#sec:fit_performance){reference-type="ref" reference="sec:fit_performance"}.

We denote by $\bm\theta$ the vector of differentiable physics parameters. For illustration, in this paper we consider $28$ parameters, chosen to exercise every part of the generator and to demonstrate operation in high-dimensional spaces.

[^1]: <https://github.com/cesarjesusvalls/ADoNIS/>

[^2]: <https://github.com/AchillesGen/Achilles>
