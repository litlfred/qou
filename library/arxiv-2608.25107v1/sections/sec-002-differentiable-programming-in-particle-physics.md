---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples"
section_id: sec-002-differentiable-programming-in-particle-physics
section_title: "Differentiable programming in particle physics"
section_number: null
pages: 2-2
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.798
latex_coverage_ratio: 0.991
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples — 19 sections: ADoNIS: A Differentiable generatOr; Introduction; Differentiable programming in part"
---
[]{#sec:intro_diffprog label="sec:intro_diffprog"}

Differentiable programming makes a simulation differentiable in its own inputs, so that derivatives of the prediction are produced by the program rather than reconstructed outside it. Automatic differentiation [@Baydin:2015tfa] decomposes a program into elementary operations and applies the chain rule through each of them, giving the exact derivative of the output with respect to any input; in reverse mode a full gradient costs a small constant multiple of one forward evaluation, independent of the number of inputs, and higher derivatives follow by nesting the same construction.

Physics is adopting this formalism broadly [@Schoenholz:2019jaxmd; @Kasim:2021dqc; @Weymouth:2023waterlily; @Meunier:2025veros; @Liao:2019tensor; @Kaiser:2024cheetah; @Agol:2021nbody; @Li:2022pmwd]. Within high-energy physics, applications are emerging rapidly. The stochastic sampling long presumed to obstruct them has proved tractable [@Arya:2022stochad], and gradient information has been put to use across the full range of common experimental tasks: detector design [@MODE:2022znx], physics modelling [@Heinrich:2022xfa; @Cranmer:2021gdt; @Nachman:2022jbj; @BarhamAlzas:2024ggt], and data analysis [@Simpson:2022suz]. In neutrino physics, differentiable frameworks now exist for the two most widely used detector technologies, liquid argon time projection chambers [@Gasiorowski:2023tqf] and optical Cherenkov and scintillation detectors [@Alterkait:2026ocv; @CCM:2025dbq], with demonstrated applications to detector calibration and event reconstruction. [ADoNIS]{.smallcaps} extends this emerging paradigm to the modelling of neutrino interactions.
