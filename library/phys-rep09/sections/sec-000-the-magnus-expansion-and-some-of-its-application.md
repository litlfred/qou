---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-000-the-magnus-expansion-and-some-of-its-application
section_title: "The Magnus expansion and some of its applications"
section_number: null
pages: 1-3
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
S. Blanes?, F. Casas, J.A. Oteo‘, J. Ros °**

* Instituto de Matematica Multidisciplinar, Universidad Politécnica de Valencia, E-46022 Valencia, Spain
> Departament de Matematiques, Universitat Jaume I, E-12071 Castell6n, Spain

© Departament de Fisica Teorica, Universitat de Valéncia, E-46100 Burjassot, Valencia, Spain

4 IFIC, Centre Mixt Universitat de Valéncia-CSIC, E-46100 Burjassot, Valencia, Spain

ARTICLE INFO ABSTRACT

Article history:

Accepted 13 November 2008
Available online 25 November 2008
editor: D.L. Mills

Approximate resolution of linear systems of differential equations with varying coefficients
is a recurrent problem, shared by a number of scientific and engineering areas, ranging
from Quantum Mechanics to Control Theory. When formulated in operator or matrix form,
the Magnus expansion furnishes an elegant setting to build up approximate exponential

PACS:
03.65
02.30.Hq
02.60.Cb
02.20.Rt

representations of the solution of the system. It provides a power series expansion for
the corresponding exponent and is sometimes referred to as Time-Dependent Exponential
Perturbation Theory. Every Magnus approximant corresponds in Perturbation Theory to
a partial re-summation of infinite terms with the important additional property of
preserving, at any order, certain symmetries of the exact solution.

The goal of this review is threefold. First, to collect a number of developments
scattered through half a century of scientific literature on Magnus expansion. They
concern the methods for the generation of terms in the expansion, estimates of the radius
of convergence of the series, generalizations and related non-perturbative expansions.
Second, to provide a bridge with its implementation as generator of especial purpose
numerical integration methods, a field of intense activity during the last decade. Third,
to illustrate with examples the kind of results one can expect from Magnus expansion,
in comparison with those from both perturbative schemes and standard numerical
integrators. We buttress this issue with a revision of the wide range of physical applications
found by Magnus expansion in the literature.

© 2008 Elsevier B.V. All rights reserved.

Contents

1. Introduction...

1.1.
1.2.

2. The Magnus expansion (ME)...

2.1.
2.2.
2.3.
24.
25.
2.6.
2.7.

Motivation, overview wand history.
Mathematical preliminaries and notations..

A proof of Magnus’ Theorem
Formulae for the first terms in Magnus expansion .
Magnus expansion generator.

Magnus expansion and time-dependent perturbation theory
Graph theoretical analysis of Magnus expansion.
Time-symmetry of the expansion....
Convergence of the Magnus expansion

* Corresponding author at: Departament de Fisica Tedrica, Universitat de Valéncia, E-46100 Burjassot, Valencia, Spain.
E-mail address: Jose.Ros@uv.es (J. Ros).

0370-1573/$ - see front matter © 2008 Elsevier B.V. All rights reserved.
doi: 10.1016/j.physrep.2008.11.001
152

S. Blanes et al. / Physics Reports 470 (2009) 151-238

. 166
. 167
. 168
. 169

2.7.1. On the existence of 2(t)
2.7.2. Convergence of the Magnus series
2.7.3. An improved radius of convergence
2.7.4. Further discussion .......

2.8. | Magnus expansion and the BCH formula .171
2.9. Preliminary linear transformations .. .172
2.10. | Exponential product representations.. .173
2.10.1. | Fer method . 173
2.10.2. | Wilcox method .. .175
2.10.3. | Wei-Norman factorization .175
2.11. | The continuous BCH formula...

Generalizations of the Magnus expansion 176
3.1. Voslamber iterative method .. .177
3.2. Floquet-Magnus expansion 179
3.3. Magnus expansions for nonlinear matrix equations.. . 180
3.4. Treatment of general nonlinear equations... . 182
3.4.1. | Treatment of Hamiltonian systems .185
3.5. | Magnus expansion and the Chen-Fliess series . 186
Illustrative examples... . 188
4.1. MEin the Interaction Picture. . 188
4.1.1. Linearly forced harmonic oscillator . 188
4.1.2. Two-level quantum systems . 189
4.2. MEin the Adiabatic Picture.... . 193
4.2.1. Linearly forced harmonic oscillator. . 194
4.2.2. _Rosen-Zener model . 194
4.3. Fer and Wilcox infinite-product expansions 195
4.3.1. Linearly forced harmonic oscillator. 195
4.3.2. _Two-level quantum system: Rectangular ste . 195
4.4. Voslamber iterative method .. . 196
4.5. Linear periodic systems: Floquet-Magnus formalism .. . 197
Numerical integration methods based on the Magnus expansion .. . 198
5.1. Introduction... . 198
5.2. Runge-Kutta method. . 200
5.3. Preservation of qualitative properties . 202
5.4. | Magnus integrators for linear systems . 203
5.4.1. From Magnus to Fer and Cayley methods . 206

5.4.2. Fer based methods .
5.4.3. Cayley-transform methods . 207
5.5. | Numerical illustration: The Rosen-Zener model revisited . . 208
5.6. Computing the exponential of a matrix.. 210
5.6.1. Scaling and squaring with Padé ‘approximation 211

5.6.2. Chebyshev approximation .
5.6.3. Krylov space methods ..... 213
5.6.4. Splitting methods .... 213
5.7. Additional numerical examples 214
5.8. Modified Magnus integrators. 216
5.8.1. Variations on the basic algorithm. 216
5.8.2. Commutator-free Magnus integrator: 217

5.9. | Magnus integrators for nonlinear differential equations

. 220
. 220

5.9.1. Nonlinear matrix equations in Lie groups
5.9.2. The general nonlinear problem ...

Some applications of the numerical integrators based on ME. 221
6.1. | Case study: Numerical treatment of the Schrodinger equation 222
6.1.1. Time-dependent Schrédinger equation 222
6.1.2. Time-independent Schrédinger equation 225
6.2. | Sturm-Liouville problems 225
6.3. The differential Riccati equation 226
6.4. | Stochastic differential equation: 228
Physical applications... 230
7.1. Nuclear, atomic and molecular physic: 230
7.2. Nuclear magnetic resonance: Average Hamiltonian theory .
7.3. Quantum field theory and high energy physic: 231
7A. Electromagnetism 232
75. . 232
76. 233

7.7.

233
S. Blanes et al. / Physics Reports 470 (2009) 151-238 153

7.8. Geometric control of mechanical systems
8. Conclusions...
Acknowledgments
References
