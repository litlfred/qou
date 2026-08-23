---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-008-23-generalized-young-diagrams
section_title: "Generalized Young diagrams"
section_number: 2.3
pages: 15-17
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
⋆ is interesting
because it shows that the value of a polynomial function is deﬁned on more general
objects than just Young diagrams.
Deﬁnition 2.6. A generalized Young diagram is a broken line going from a point
(0, y) on the y-axis to a point (x, 0) on the x-axis such that every piece is either a
horizontal segment from left to right or a vertical segment from top to bottom.
Any Young diagram can be seen as such a broken line: just consi der its border.
The notions of inner and outer corners can be easily adapted to generalized Young
diagrams, as well as the setsIL and OL of their contents. It is illustrated in Figure 3.
Note also that the relation p1(IL − OL) = 0 holds for generalized Young diagrams
as well.
Any polynomial function F on the set of Young diagrams corresponds to the
function
λ ↦→f (Iλ − Oλ)
for some symmetric functionf. Recall that f is uniquely determined up to addition
of a multiple of p1. Thus, F can be canonically extended to generalized Young
diagrams by setting
F (L) = f (IL − OL).
As the relation p1(IL − OL) = 0 holds, F (L) is well-deﬁned, i.e. it does not
depend on the choice of f.
16 M. DOŁ ˛ EGA AND V . FÉRAY
i1 = − 2 o1 = − 1.5
i2 = 0 o2 = 2 .5
i3 = 3
FIGURE 3. A generalized Young diagram L with the correspond-
ing sets OL = {o1, o2} and IL = {i1, i2, i3}.
λ
↦→
T2, 1
2
(λ)
FIGURE 4. Example of a Young diagram λ on the left and a
stretched Young diagram T2, 1
2
(λ) on the right.
We will be in particular interested in the following generalized Young diagrams.
Let λ be a (generalized) Young diagram and s and t two positive real numbers.
Ts,t(λ) denotes the generalized Young diagram obtained from λ by stretching it
horizontally by a factor s and vertically by a factor t in French convention (see
Figure 4). These anisotropic Young diagrams have been ﬁrst considered by Kerov
in [Ker00a], also in the context of Jack polynomials.
In the case s = t, we denote by Ds(λ) := Ts,s(λ) the diagram obtained from
λ by applying a homothetic transformation of ratio s and we will call it dilated
Young diagram. In the case s = t−1 = √α for some α ∈ R+ we denote by
Aα(λ) := T√α,√α−1(λ) the diagram obtained from λ by stretching it horizontally
by a factor √α and vertically by a factor √α−1. We call it α-anisotropic Young
diagram.
It is easy to check that the sets IDs(λ) and ODs(λ) are obtained from Iλ and Oλ
by multiplying all values bys. In particular, if F is a polynomial function such that
the corresponding symmetric function f is homogeneous of degree d, then
λ ↦→F (Ds(λ)) = f (IDs(λ) − ODs(λ)) = sdf (Iλ − Oλ) = sdF (λ)
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 17
is also a polynomial function. Finally, for any ﬁxed s > 0, F is a polynomial
function if and only if λ ↦→F (Ds(λ)) is a polynomial function.
