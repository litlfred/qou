---
doc_id: arxiv-2602.15276v1
doc_title: "Compact Q-balls and Q-shells within aCP N Skyrme-Faddeev type model"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-4
source_pdf: 2602.15276v1.pdf
source_sha256: 18d77d6aa140fc50
doc_brief: "Compact Q-balls and Q-shells within aCP N Skyrme-Faddeev type model — 11 sections: Introduction; The Lagrangian and Euler-Lagrange ; Radial reduction"
---
Scalar fields play a crucial role in theoretical physics. They are extensively employed for mod-
eling physical matter across a diverse range of contexts, from fundamental fields such as the Higgs
field [1] to effective descriptions like the order parameter field in the Landau-Ginzburg model [2].
Depending on the inherent complexity of the physical phenomenon under investigation, scalar fields
can be represented by straightforward real-valued functions or by more intricate structures, such
as multiple complex-valued fields defined on complex projective spaces (CP N models) [3].
This paper examines a scalar field theory characterized by aCPN target space. The model under
consideration represents an extension of the conventional Skyrme-Faddeev (SF) model, specifically
through the inclusion of additional quartic terms and a potential function. Our central objective is
the identification of stationary, finite-energy solutions, which are commonly referred to as Q-balls.
Under specific selections for the potential, these Q-balls are realized ascompactons, meaning they
are solutions characterized by compact support.
The Skyrme-Faddeev (SF) model, initially proposed by L. D. Faddeev in 1975 [4, 5], is a modified
sigma model defined in three spatial dimensions. This model is characterized by a topological charge
∗ eduardo.luizcolaco@gmail.com
† pawel.klimas@ufsc.br
‡ livramento@usp.br
§ sawadoph@rs.tus.ac.jp
¶ yanai@toyota-ct.ac.jp
arXiv:2602.15276v1  [hep-th]  17 Feb 2026
2
associated with the Hopf mapS 3→S 2. Faddeev introduced this particular model with the goal of
identifying finite-energy knot soliton solutions. This theoretical concept was subsequently validated
by numerical studies [6, 7], which successfully demonstrated the existence of stable toroidal solitons
and knot structures.
In contrast, the analytical solutions for this model remain largely unexamined. The crucial
relevance of the model within emerging physical contexts is the main reason behind continuous
efforts to find these solutions using analytical methods. Specifically, a conjecture based on the Cho-
Faddeev-Niemi decomposition postulates that the SF model can be obtained as a low-energy, non-
perturbative effective model forSU(2) Yang-Mills theory [8]. Furthermore, results established by
Gies [9] indicate that the SF model can be derived from an analysis of the Wilsonian effective action
forSU(2) Yang-Mills theory. This analysis not only reproduces the original SF Lagrangian but
also generatesnovel termsthat are quartic in derivatives. The inclusion of these terms within the
Lagrangian yields a modified SF model. Notably, the presence of a quartic term was instrumental
in the construction of the exact time-dependent vortex solution in 3 + 1 dimensions by Ferreira
[10], a solution which exists for a specific combination of coupling constants.
The model can also be extended through the generalization of its target space. For instance,
the SF model (without additional non-Skyrme type quartic terms) defined on the coset space
SU(N+ 1)/U(1) N was proposed in [11]. This specific case was identified as the ”maximum case”
in the classification presented in [12]. An alternative generalization, designated the ”minimum
case” by the same authors, utilizes the coset spaceSU(N+ 1)/SU(N)⊗U(1), which corresponds
to complex projectiveCP N space. A modified SF model incorporating theCP N target space
was subsequently proposed in [13]. This particular formulation introduces two additional coupling
constants that multiply two distinct types of quartic terms, which can be included forN≥2.
When these coupling constants satisfy a specific constraint, the model is shown to support vortex
solutions within its holomorphic (or anti-holomorphic) sector. Further analysis of these vortex
solutions was conducted in [14]. It was later observed in [15] that the condition imposed on the
coupling constants can be relaxed if the model is augmented by a potential (non-derivative) term.
The authors of [15] successfully discovered exact and numerical vortex solutions for the model with
aCP 1 target space. The concept of vortex solutions in the simultaneous presence of both quartic
terms and a potential was also investigated in [16]. This principle retains its validity when the
model’s target space is extended toCP N space. According to the findings in [17], vortex solutions
exist for a certain class of potentials, even when the coupling constants do not satisfy the usual
condition initially introduced in [13].
A crucial requirement for physical relevance is that the solutions must possess finite total energy.
However, all known vortex solutions of the extended Skyrme-Faddeev (ESF) model extend infinitely
along thez-axis. Consequently, they exhibit infinite total energy, even though their energy per
unit length remains finite. For realistic physical systems, finite-energy solutions in 3+1 dimensions
are intuitively expected to be spatially confined. Analogous to vortices observed in liquid helium,
which necessarily terminate at the boundaries of their container, these solutions should not extend
indefinitely in any spatial direction.
The construction of finite-energy solutions within higher-dimensionalCP N target spaces ne-
3
cessitates rigorous theoretical refinements. In theCP 1 framework, the existence of topological
solutions is facilitated by the non-trivial homotopy classπ 3(CP 1)∼= Z. Conversely, forN≥2,
higher-dimensional target spaces do not support such configurations because the third homotopy
group is trivial,π 3(CPN) = 0. In the absence of conserved topological charges, the analysis is
restricted to non-topological solutions [18], which require auxiliary stabilization mechanisms to
ensure localized energy density. For static configurations, Derrick’s theorem [19] imposes strict
constraints on the dimensionality of stable solutions, derived from the scaling behavior of the en-
ergy functional with respect to the soliton size. To circumvent the limitations imposed by Derrick’s
theorem, two primary strategies are generally employed. First, the Lagrangian may be augmented
with terms containing higher powers of derivatives; these terms exhibit scaling properties opposite
to those of the standard quadratic kinetic terms, thereby allowing for a global energy minimum
at a finite scale parameter. Alternatively, one may consider stationary solitons characterized by
a harmonic time dependence. Such solutions, extensively investigated in [20–22], are known as
Q-balls. These configurations possess a temporal dependence of the forme iωt, where the frequency
ωfacilitates the stabilization of the non-topological charge. Furthermore, non-topological solitons
may possess conserved Noether charges, which provide an additional mechanism for addressing the
issue of stability. Our previous investigations regarding compact Q-balls were restricted to complex
field models containing only quadratic kinetic terms; consequently, harmonic temporal dependence
represented the sole method for evading the constraints of Derrick’s theorem. In the present work,
we extend this analysis to a model incorporating quartic terms. This inclusion introduces a sec-
ondary stabilization mechanism, allowing for a more comprehensive exploration of the interplay
between higher-order derivatives and stationary field configurations.
The existence of non-topological solutions within the ESF model, analogous to its non-integrable
sector’s vortices, necessitates the inclusion of a potential term. The precise functional form of this
potential in the vicinity of its minimum directly governs the field’s asymptotic behavior at spatial
infinity. However, models featuring sharp, V-shaped potentials at their minimum, when combined
with standard quadratic derivative terms in the Lagrangian, exhibit an unconventional field behav-
ior near that minimum. In these cases, the field approaches its vacuum quadratically–characterized
by a parabolic approach–thereby reaching the minimum within a finite spatial distance. Solutions
possessing this characteristic are non-zero exclusively within a compact support, leading to their
designation as compactons.
The signum-Gordon model [23, 24] provides the simplest supporting example of compacton
solutions. This model is essentially a Klein-Gordon model in which the typical quadratic potential,
ϕ2, is substituted by the sharp potential,|ϕ|. A version of this model employing a complex-valued
scalar field is known to support compact Q-balls [25–27]. Importantly, compactons are classified as
solutions in a weak sense [28, 29], implying they satisfy the integrated Euler-Lagrange equations.
Interest in compact solutions has increased substantially in recent years, with compactons emerging
in various domains of physics, including condensed matter physics [30], nuclear physics [31], and
cosmology [32]. More recently, oscillons [33], another class of compact solutions, were discovered
within the BPS submodel, which satisfies the Bogomol’nyi–Prasad–Sommerfield bound, of the
Skyrme model [34, 35]. These oscillons are expected to play a crucial role in the radiation spectrum
4
observed during skyrmion scattering. Analogously, we expect that time-dependent non-topological
solutions will appear in the radiation spectrum of the ESF model when a potential term is included.
This paper examines compact non-topological solutions within the ESF model augmented with
a potential term. Initial research into these solutions, detailed in [36], established the existence
of compact Q-balls and Q-shells in theCP N model (specifically for oddN) when a particular V-
shaped potential is introduced. These solutions are characterized by a non-trivial radial function
in spherical coordinates and exhibit time dependence via the factore iωt. Their angular component
is described by spherical harmonics.
The remainder of this paper is organized as follows. Section II details the model and its
parameterization. Section III is dedicated to the discussion of Noether charges. Subsequently, in
Section IV, we present and analyze the numerical compact solutions. The final section is reserved
for summarizing the key findings and discussing the implications of the results.
II. THE EXTENDED SKYRME-F ADDEEV MODEL WITH POTENTIAL
