---
doc_id: alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari
doc_title: "Theta Functions, Modular Invariance, and Strings"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: alvarez-gaume-moore-vafa-1986-theta-functions-modular-invariance-and-strings.pdf
source_sha256: c99ca1cd756f7aa6
toc_source: inferred
doc_brief: "Theta Functions, Modular Invariance, and Strings — We use Quillen's theorem and algebraic geometry to investigate the modular transformation properties of some quantities of interest in string"
---
Two-dimensional quantum field theories have served as toy models in attempts to
understand more complicated four-dimensional theories. The two dimensional
theories capture many essential features of higher dimensions, without sharing the
complexities of higher dimensions. Certain features of Id QFT's such as Bose-
Fermi equivalence have led to a large number of exactly solvable theories.
In string theories, two-dimensional conformal QFT plays an even more
important role [1-3]. The string sweeps out a surface as it moves through space-
time, and therefore, the first quantized theory corresponds to a two dimensional
QFT. The string can sweep out a surface with any number of handles. Whereas in
most well known results one considers the underlying space to be JR2 (or R x S1, or
S1 x S1 corresponding to periodic boundary conditions in space or time), for string
theories one must consider the space to be an arbitrary Riemann surface. Thus,
understanding multiloop string amplitudes requires an understanding of QFT on
a Riemann surface. In the general case, few explicit facts are known.
Many questions remain unanswered in string theory. For instance, how can we
prove the vanishing of the cosmological constant in superstring theories? This has
been shown explicitly at 1-loop. For higher loops, even though there is an indirect
argument for the vanishing of the cosmological constant [3, 4], one would like to
show this important fact more directly.
There are other issues: What happens to the string amplitude in the limit of a
degenerating Riemann surface? Are superstring theories finite? Is the perturbation
2 
L. Alvarez-Gaume, G. Moore, and C. Vafa
expansion valid? Can one develop an operator formalism for surfaces with more
than one handle? How does the bosonization work at higher loops? etc.
Motivated by these questions, we address below some issues regarding the
determinant of some operators, in particular the chiral Dirac operator, defined on
a Riemann surface. We will discuss in some detail the spin structure dependence of
the determinant of the Dirac operator. Our main tools are Quillen's holomorphic
anomaly, algebraic geometry, and bosonization. We feel that the algebraic
geometric techniques are very powerful and well suited for applications to a better
understanding of string theories. This viewpoint has also been advocated recently
by several groups.
In Sect. 2 we illustrate some of the issues which will be discussed in this paper,
in the context of the simple case of the torus. In Sect. 3 we discuss the mathematical
concepts which will be used. Many of them, for example, modular transformations,
generalized theta functions and spin structures appear as natural generalizations
of the concepts already appearing in the case of the torus. Yet others, such as
divisors of theta functions and their relation to spin structures, although important
for higher loops, do not play a central role in the genus one case.
In Sect. 4 we discuss Quillen's holomorphic anomaly, and a slight general-
ization of it. This anomaly is the obstruction to expressing as a holomorphic
function the determinant of a family of operators depending holomorphically on
some complex parameter.
In Sect. 5 we show that the spin dependence of the determinant of the chiral
Dirac operator is given by theta functions. In Sect. 6 we discuss these results from
the viewpoint of bosonization. In Sect. 7 we apply the results obtained to address
some questions related to the modular invariance of the measure for heterotic
strings [5]. Finally, in Sect. 8 we present our conclusions.
2. Fermions on a Torus
In this section we will consider fermions on a torus. We label the points of the torus
by the complex quantity σ1 + τσ2, where σx and σ2 are periodic variables with
period 2π. This means that
x ~ x + 2π ~ x 4- 2πτ.
For bosonic fields defined on the torus one requires the periodic boundary
conditions:
X(σ1 + 2π, σ2) = X(σu σ2 + 2π) = X(σl9 σ2)
For fermions, we have the option of choosing periodic or antiperiodic boundary
conditions in each direction. Therefore we have four different possible boundary
conditions: (A, A), (P,A), (A,P), and (P,P)9 where P(A) stands for periodic
(antiperiodic). These are called the spin structures. So for genus 1 we have four
different spin structures.
For the torus we have chosen 2π and 2πτ to generate the lattice defining it. We
could have chosen a different basis for the same lattice, thereby obtaining the same
torus. For example the tori defined by 2π(l,τ) and 2π(l,τ + l) differ from one
another by a global diffeomorphism. To see this we simply cut the torus along the
Theta Functions, Modular Invariance, and Strings 
3
σx cycle and rotate the two boundary circles relative to one another by 2π and glue
them back together. (This is called a Dehn twist, and its general form will be
discussed in Sect. 3.)
Different choices of the lattice defining the torus could be obtained by means of
2x2, invertible (unit determinant) and integral matrices acting on a basis. This is
the group SL(2, Z) which is referred to as the modular group. Under an element of
SL(2, Z), with entries α, b, c, d,
aτ + b
T~* cτ + d'
The Dehn twists about the σx and σ2 cycles correspond respectively to
Ί 
l\ 
(\
)
