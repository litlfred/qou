---
doc_id: oberwolfachreports1223-v20120708-9-40
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by"
section_id: sec-004-a-new-construction-of-the-fukayaseidel-category
section_title: "A new construction of the Fukaya–Seidel category"
section_number: null
pages: 15-16
source_pdf: OberwolfachReports1223_v20120708_9_40.pdf
source_sha256: 94f82cfc185955ba
toc_source: inferred
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by — This meeting concentrated on topological invariants in low di"
---
Andriy Haydys
Inspired by Seidel’s construction [2], I present a new construction of the Fukaya–
Seidel category, which is associated to a symplectic Lefschetz ﬁbration.
Let (M, ω = dλ, J) be an exact symplectic manifold equipped with an al-
most complex structure. A symplectic Lefschetz ﬁbration in our setting is a J–
holomorphic function f : M →C with ﬁnitely many non–degenerate critical points
m1, . . . , mk. Then one can conjecturally associate to f an A∞–category Af as fol-
lows (see [1] for details). The objects of Af are critical points of f. To deﬁne
the morphism spaces choose a pair of critical points m± ∈{m1, . . . , mk} and de-
note by Γ(m−, m+) a suitably chosen subspace of {γ : R →M | γ(±∞) = m∓}.
Consider the functional
F: Γ(m−, m+) −→R,
F(γ) =
"
R
γ∗λ +
"
R
Im
#
e−iθ(t)f ◦γ(t)
$
dt,
where θ
=
θ(t) is a suitably chosen function.
Then, roughly speaking,
hom(m−, m+) is the Morse–Witten complex of F. Let us describe some details.
The critical points of F are solutions of the problem
(1)
˙γ + vt = 0,
lim
t→±∞γ(t) = m∓,
where vt
=
cos θ(t) gradRef + sin θ(t) grad Im f.
These freely generate
hom(m−, m+) as a Z/2Z–vector space.
16
Oberwolfach Report 28/2012
Furthermore, choose a pair γ± of solutions of (1) and consider the problem
(2)
∂su + J
%
∂tu + vt&
= 0,
u: R2
s,t →M,
lim
t→±∞u(s, t) = m∓,
lim
s→±∞u(s, t) = γ∓(t),
lim
t→±∞
" +∞
−∞
|∂su(s, t)| ds = 0,
lim
s→±∞
" b
a
|∂su(s, t)| dt = 0.
Notice that the ﬁrst equation is formally the antigradient ﬂow equation for the
functional F. Denote the space of solutions of the above equations by M(γ−; γ+)
and put
ˆ
M(γ−; γ+) = M(γ−; γ+)/R, where R acts by translations in s–variable.
One deﬁnes the diﬀerential ∂: hom(m−, m+) →hom(m−, m+) in the usual way,
provided points in
ˆ
M(γ−; γ+) can be sensibly counted.
The composition
hom(mp, mq) ⊗hom(mq, mr) →hom(mp, mr) as well as the “Massey products”
are deﬁned in a similar manner. Conjecturally, these combine to an A∞–structure.
Theorem 1. The space M(γ−; γ+) is the zero locus of a Fredholm section.
Theorem 2. Assume critical values f(m1), . . . , f(mk) are in convex position and
the ﬁbration f : M →C is trivial in the neighbourhood of inﬁnity. Then the space
ˆ
M(m−; m+) =
'
γ±
ˆ
M(γ−; γ+)
is compact, where the union is taken over all pairs of solutions of (1).
References
[1] A. Haydys, Fukaya-Seidel category and gauge theory, arXiv:1010.2353.
[2] P. Seidel, Fukaya categories and Picard-Lefschetz theory, Z¨urich Lectures in Advanced Math-
ematics. European Mathematical Society (EMS), Z¨urich, 2008.
