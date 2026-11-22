---
doc_id: on-the-garoufalidis-kashaev-state-integral-invariant
doc_title: "ON THE GAROUFALIDIS-KASHAEV STATE-INTEGRAL INVARIANT"
section_id: sec-001-abstract
section_title: "ABSTRACT"
section_number: null
pages: 5-10
source_pdf: On the Garoufalidis-Kashaev State-Integral Invariant.pdf
source_sha256: eda230da2a596783
toc_source: outline
doc_brief: "ON THE GAROUFALIDIS-KASHAEV STATE-INTEGRAL INVARIANT — 67 sections: Front matter; ACKNOWLEDGMENTS; ABSTRACT"
---
This thesis explores a construction of the family of topological invariants
for certain oriented 3-manifolds based on the state-integral approach developed by
Andersen, Garoufalidis, and Kashaev in the Archimedean setting. Starting from an
ideal triangulation of a 3-manifold equipped with angle data, variables are assigned
to the faces and tetrahedra, taking values in a so-called ’Gaussian group’. The
invariant is defined by integrating a distribution defined from the combinatorics of
the triangulation and a special function over a product of the Gaussian group.
The special function is a quantum dilogarithm, whose valuable feature, the pentagon
relation, ensures the resulting integral remains unchanged under local modifications
of the triangulation, thereby reflecting the topology of the manifold.
v
TABLE OF CONTENTS
ACKNOWLEDGMENTS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . iv
ABSTRACT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . v
LIST OF TABLES . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . x
1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
1.1
Motivation and Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
1.2
Overview of the Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2
1.3
Main Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2
1.4
Structure of the Thesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1.5
Connections and Outlook . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
1.6
Connections to Representation Theory . . . . . . . . . . . . . . . . . . . . . . . . . .
5
2
Locally Compact Abelian Groups, Pontryagin Duality, and Gaussian
Structures [10] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.1
Locally Compact Abelian Groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.1.1
Foundational Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.1.2
Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.1.3
Structure Theorem (Informal) . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.2
Pontryagin Duality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.2.1
Character Groups and Duality . . . . . . . . . . . . . . . . . . . . . . . . . .
8
vi
2.2.2
Pontryagin Duality Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
2.2.3
Examples of Dual Pairs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
2.3
Gaussian Group . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.3.1
Pontryagin Characters and Gauss Characters . . . . . . . . . . . . . . . 11
2.4
Local Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3
Quantum Dilogarithm. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.1
A quantum dilogarithm over a Gaussian group . . . . . . . . . . . . . . . . . . . 15
3.2
A quantum dilogarithm over a Special Gaussian Group . . . . . . . . . . . . . 16
3.2.1
Fourier transform of the Archimedean quantum dilogarithm . . . 16
3.2.2
Pentagon identity in the Archimedean case. . . . . . . . . . . . . . . . . 18
3.3
Angled Quantum Dilogarithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.3.1
Angle Space and Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.3.2
Triangle Angle Condition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.3.3
Definition of the Angled Quantum Dilogarithm . . . . . . . . . . . . . 21
3.3.4
Temperedness and Positivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.3.5
Symmetries of the Angled Quantum Dilogarithm . . . . . . . . . . . . 26
3.3.6
Angled Pentagon Identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4
The State-Integral Invariant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.1
Triangulations and State Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.2
The Kinematical Kernel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.3
Angle Structures and Dynamical Weights . . . . . . . . . . . . . . . . . . . . . . . 35
4.3.1
Balanced Angle Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
4.3.2
Quantum Dilogarithmic Weights . . . . . . . . . . . . . . . . . . . . . . . . . 36
4.4
The State-Integral Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
vii
4.5
Summary of the Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
5
Target of the State-Integral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.1
Target Statement for the Archimedean State-Integral . . . . . . . . . . . . . . 39
5.2
Manifolds with Boundary (∂M̸ = ∅) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.2.1
Manifolds with Torus Boundary (∂M ∼= T 2) . . . . . . . . . . . . . . . . 40
5.3
Closed Manifolds (∂M = ∅) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5.4
Angle Structures and Parameter Dependence . . . . . . . . . . . . . . . . . . . . . 41
5.5
Algebraic Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.5.1
Summary Table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
5.5.2
Remark . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
6
Topological Invariance of the State-Integral . . . . . . . . . . . . . . . . . . . . 45
6.1
The Pentagon Identity and Pachner Moves . . . . . . . . . . . . . . . . . . . . . . 46
6.1.1
Combinatorics of the Pachner Move . . . . . . . . . . . . . . . . . . . . . . 46
6.1.2
Analytic Expression via Pentagon Identity . . . . . . . . . . . . . . . . . 46
6.2
(P1) Pachner Invariance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
6.2.1
Triangulation Equivalence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
6.2.2
Invariance Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
6.3
(P2) Analytic Control and Temperedness . . . . . . . . . . . . . . . . . . . . . . . . 47
6.3.1
Tempered Distribution Framework . . . . . . . . . . . . . . . . . . . . . . . 47
6.3.2
Conditions Ensuring Convergence . . . . . . . . . . . . . . . . . . . . . . . . 48
6.4
(P3) Angle Gauge Invariance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
6.4.1
Internal Angle Shifts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
6.4.2
Cancellation in the Integral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
6.5
Topological Invariance Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
viii
6.6
Conceptual Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
REFERENCES . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
ix
