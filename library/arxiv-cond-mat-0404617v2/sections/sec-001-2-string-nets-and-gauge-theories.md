---
doc_id: arxiv-cond-mat-0404617v2
doc_title: "String-net condensation: A physical mechanism for topological phases"
section_id: sec-001-2-string-nets-and-gauge-theories
section_title: "String-nets and gauge theories"
section_number: 2
pages: 2-3
source_pdf: cond-mat-0404617v2.pdf
source_sha256: 8e31b9ec8ac2e034
toc_source: inferred
doc_brief: "String-net condensation: A physical mechanism for topological phases — 18 sections: Front matter; Introduction; String-nets and gauge theories"
---
In this section, we introduce the string-net picture in
the context of gauge theory [27, 37, 38]. We point out
that all deconﬁned gauge theories can be understood as
string-net condensates where the strings are essentially
electric ﬂux lines. We hope that this result provides in-
tuition for (and motivates) the string-net picture in the
general case.
We begin with the simplest gauge theory - Z2 lattice
gauge theory [39]. The Hamiltonian is
HZ2 = −U
∑
i
σx
i + t
∑
p
∏
edges of p
σz
j (1)
where σx,y,z are the Pauli matrices, and I, i, p label the
sites, links, and plaquettes of the lattice. The Hilbert
space is formed by states satisfying
∏
legs of I
σx
i |Φ ⟩= |Φ ⟩, (2)
for every site I. For simplicity we will restrict our dis-
cussion to trivalent lattices such as the honeycomb lattice
(see Fig. 2).
It is well known that Z2 lattice gauge theory is dual
to the Ising model in (2 + 1) dimensions [40]. What
σ x
σ x σ x
σ z
σ zσ z
x
xx
x
x
x
σ z
σ z
σ z
p
I
σ   =−1
σ   =−1σ   =−1
σ   =−1
σ   =−1
σ   =−1
FIG. 2: The constraint term ∏
legs of I σ x
i and magnetic term∏
edges of p σ z
j in Z2 lattice gauge theory. In the dual picture,
we regard the links with σ x = − 1 as being occupied by a
string, and the links with σ x = +1 as being unoccupied. The
constraint term then requires the strings to be closed - as
shown on the right.
is less well known is that there is a more general dual
description of Z2 gauge theory that exists in any number
of dimensions [41]. To obtain this dual picture, we view
links with σx = −1 as being occupied by a string and
links with σx = +1 as being unoccupied. The constraint
(2) then implies that only closed strings are allowed in
the Hilbert space (Fig. 2).
In this way, Z2 gauge theory can be reformulated as a
closed string theory, and the Hamiltonian can be viewed
as a closed string Hamiltonian. The electric and mag-
netic energy terms have a simple interpretation in this
dual picture: the “electric energy” −U∑
i σx
i is a string
tension while the “magnetic energy” t∑
p
∏
edges of p σz
j
is a string kinetic energy. The physical picture for the
conﬁning and deconﬁned phases is also clear. The con-
ﬁning phase corresponds to a large electric energy and
hence a large string tension U ≫ t. The ground state
is therefore the vacuum conﬁguration with a few small
strings. The deconﬁned phase corresponds to a large
magnetic energy and hence a large kinetic energy. The
ground state is thus a superposition of many large string
conﬁgurations. In other words, the deconﬁned phase of
Z2 gauge theory is a quantum liquid of large strings - a
“string condensate.” (Fig. 3a).
A similar, but more complicated, picture exists for
other deconﬁned gauge theories. The next layer of com-
plexity is revealed when we consider other Abelian the-
ories, such as U (1) gauge theory. As in the case of Z2,
U (1) lattice gauge theory can be reformulated as a the-
ory of electric ﬂux lines. However, unlike Z2, there is
more then one type of ﬂux line. The electric ﬂux on a
link can take any integral value in U (1) lattice gauge the-
ory. Therefore, the electric ﬂux lines need to be labeled
with integers to indicate the amount of ﬂux carried by
the line. In addition, the ﬂux lines need to be oriented
to indicate the direction of the ﬂux. The ﬁnal point is
that the ﬂux lines don’t necessarily form closed loops.
It is possible for three ﬂux lines E1, E2, E3 to meet at a
point, as long as Gauss’ law is obeyed: E1 + E2 + E3 = 0.
Thus, the dual formulation of U (1) gauge theory involves
not strings, but more general objects: networks of strings
1
-1
-4
2
5
-3
2
5
1/2
1
2
3/2
(a) (b) (c)
5
7/23
FIG. 3: Typical string-net conﬁgurations in the dual formu-
lation of (a) Z2, (b) U (1), and (c) SU (2) gauge theory. In
the case of (a) Z2 gauge theory, the string-net conﬁgura-
tions consist of closed (non-intersecting) loops. In (b) U (1)
gauge theory, the string-nets are oriented graphs with edge s
labeled by integers. The string-nets obey the branching rul es
E1 + E2 + E3 = 0 for any three edges meeting at a point.
In the case of (c) SU (2) gauge theory, the string-nets con-
sist of (unoriented) graphs with edges labeled by half-inte gers
1/ 2, 1, 3/ 2, ... . The branching rules are given by the triangle
inequality: {E1, E 2, E 3} are allowed to meet at a point if and
only if E1 ≤ E2 + E3, E2 ≤ E3 + E1, E3 ≤ E1 + E2, and
E1 + E2 + E3 is an integer.
(or “string-nets”). The strings in a string-net are labeled ,
oriented, and obey branching rules, given by Gauss’ law
(Fig. 3b).
This “string-net” picture exists for general gauge the-
ories. In the general case, the strings (electric ﬂux lines)
are labeled by representations of the gauge group. The
branching rules (Gauss’ law) require that if three strings
E1, E2, E3 meet at a point, then the product of the rep-
resentations E1 ⊗ E2 ⊗ E3 must contain the trivial rep-
resentation. (For example, in the case of SU (2), the
strings are labeled by half-integers E = 1 /2, 1, 3/2, ...,
and the branching rules are given by the triangle inequal-
ity: {E1, E2, E3} are allowed to meet at a point if and
only if E1 ≤ E2 + E3, E2 ≤ E3 + E1, E3 ≤ E1 + E2 and
E1 + E2 + E3 is an integer (Fig. 3c)) [37]. These string-
nets provide a general dual formulation of gauge theory.
As in the case of Z2, the deconﬁned phase of the gauge
theory always corresponds to highly ﬂuctuating string-
nets – a string-net condensate.
