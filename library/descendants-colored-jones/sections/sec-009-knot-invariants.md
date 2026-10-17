---
doc_id: descendants-colored-jones
doc_title: "The descendant colored Jones polynomials"
section_id: sec-009-knot-invariants
section_title: "Knot invariants"
section_number: null
pages: 19-23
source_pdf: descendants_colored_jones.pdf
source_sha256: f00693a5926c074f
toc_source: outline
---
We can use the r-matrix given in Equation (28) to construct knot invariants
from their planar projections. This is a standard construction explained in
several places that include [Jon89, RT90, Tur88, Tur94]. We will follow the
presentation of [Kas] which does not require neither the theory of Hopf alge-
bras nor the existence of ribbon elements, and uses as a combinatorial input a
generic planar projection of a long knot with no local extrema oriented from
left to right and equal numbers of positive and negative crossings. Locally,
such a planar projection has eight types of crossings (four positive and four
negative ones)
(47)
to which one assigns the suitably “rotated” r-matrices shown in Equations
(16)–(19) of [Kas], two types of vertical segments, and two types of local
extrema
(48)
2326
Stavros Garoufalidis and Rinat Kashaev
to which ones assigns respectively the identity operators and ε and η maps
of Equation (7) of [Kas]. In our case, we ﬁx a primitive root of unity ζ of
order N, a (discrete spectral parameter) n ∈Z/NZ and a planar projection
D of a long knot K. We color each arc of D by an element of Z/NZ, place r-
matrices at the crossings (using the ﬁxed spectral parameter at all crossings),
according to the rules described below, and sum over all indices. The result
of this contraction is a complex number that depends on the colors i and j
of the outgoing and incoming arcs of the diagram of the long knot. These
complex numbers arrange in a matrix
(49)
⟨D⟩N,n ∈MatN(Z[N−1, ζ])
The r-matrices given below are rigid, i.e., satisfy the Yang-Baxter equation
(9) and the inverse matrix equation (10) of [Kas]. The next theorem follows
from the results of [Kas].
Theorem 3.1. The state-sum ⟨D⟩N,n depends on the long knot K and not
on the planar projection D used.
It remains to explain the rules for the r-matrices.
Starting with the case with m = n = 0, we get the following rules for the
four types of positive crossings
k
l
j
i
=
j
k
i
l
=
i
j
l
k
=Vi,j,k,l(ζ)ζk−l,
k
l
j
i
=Vk,l,i,j−1(¯ζ)ζj−1−k
(50)
and for the four types of negative crossings
k
l
j
i
=
j
k
i
l
=
i
j
l
k
=Vi,j,k,l(¯ζ)ζl−k,
k
l
j
i
=Vk,l,i,j−1(ζ)ζk−j+1.
(51)
Note that the weights of the negative crossings are the complex conjugates of
the corresponding weights of the positive crossings.
The descendant colored Jones polynomials
2327
Switching in now the general colors m and n, we get the rules for the
positive crossings
k
l
j
i
m
n
=
j
k
i
l
n
m
=
i
j
l
k
m
n
= Vi,j−m,k−n,l(ζ)ζk−l−n+(k−i−n)m,
k
l
j
i
n
m
= Vk,l,i−m,j−n−1(¯ζ)ζj−1−k−n+(j−l−n)m
(52)
and the negative crossings
k
l
j
i
n
m
=
j
k
i
l
m
n
=
i
j
l
k
n
m
= Vi,j−n,k−m,l(¯ζ)ζl−k+(l−j+1+n)m,
k
l
j
i
m
n
= Vk,l,i−n,j−m−1(ζ)ζk−j+1+(k−i+1+n)m.
(53)
Note that for general m, n, the weights of the negative crossings are not the
complex conjugates of the corresponding weights of the positive crossings.
Note also that the eight r-matrices needed in Equations (16)–(19) of [Kas],
up to powers of ζ, are all expressed in terms of the symbols Vi,j,k,l(ζ) and
their complex conjugates Vi,j,k,l(¯ζ).
Additionally, we have relations between colored and uncolored weights
k
l
j
i
m
n
=
j
k
i
l
n
m
=
i
j
l
k
m
n
=
k −n
l
j −m
i
ζ(k−i−n)m,
(54)
k
l
j
i
n
m
=
k
l
j −n
i −m
ζ(j−l−n)m
2328
Stavros Garoufalidis and Rinat Kashaev
in the case of positive crossings, and
k
l
j
i
n
m
=
j
k
i
l
m
n
=
i
j
l
k
n
m
=
k −m
l
j −n
i
ζ(l−j+n)m,
k
l
j
i
m
n
=
k
l
j −m
i −n
ζ(k−i+n)m
(55)
in the case of negative crossings.
We complement the rules by the weights on the four types of segments
(56)
i
j
=
j
i
=
i
j =
i
j = δi,j.
With our rules, one can calculate weights of few simplest composed dia-
grams in the colored case
(57)
j
i
n = δj,{i+1}N,
j
i
n = δj,{i+1}Nζn
and
(58)
j
i
n
= δi,{j+1}N,
j
i
n
= δi,{j+1}Nζ−n
which imply that
(59)
i
j
n
= δi,jζn,
i
j
n
= δi,jζ−n.
It is interesting to note, that the continuous spectral parameter can be
used in an alternative formulation of knot and link invariants along the idea
of Jones [Jon89] of considering a “statistical mechanics” model on piecewise
linear diagrams with straight segments where the multiplicative angles are
encoded in the continuous spectral parameters. In our case, such an approach
might be applicable only in the case with color n ≡−1 (mod N) but not for
The descendant colored Jones polynomials
2329
other values of n. In the case n ≡−1 (mod N), the starting graphical rules
would look like
(60)
k
l
j
i
x
= ⟨i, j|r(x; −1, −1)|k, l⟩,
j
i
x
= ⟨i|h(−1/x, 0)|j⟩,
where the continuous variables x’s are thought of as exponentiated angles eiα,
whose product around each vertex is 1.
