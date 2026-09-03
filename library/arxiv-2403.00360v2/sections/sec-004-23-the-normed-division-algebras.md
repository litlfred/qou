---
doc_id: arxiv-2403.00360v2
doc_title: "CAUSAL FERMION SYSTEMS AND OCTONIONS"
section_id: sec-004-23-the-normed-division-algebras
section_title: "The Normed Division Algebras"
section_number: 2.3
pages: 6-7
source_pdf: 2403.00360v2.pdf
source_sha256: b0764ca18a83a84f
doc_brief: "CAUSAL FERMION SYSTEMS AND OCTONIONS — We compare the structures and methods in the theory of causal fermion systems with approaches to fundamental physics based on division algebras, in par- ticular"
---
where division is always well-defined, except by zero. A normed division algebra has
the additional property that it is also a normed vector space, with the norm defined
in terms of a conjugate. A well-known result by Hurwitz [71] states that there exist
only four normed division algebras (over the field of real numbers): R, C, H, O, being
of dimensions one, two, four and eight, respectively. In going to higher-dimensional
algebras, successive algebraic properties are lost: R is self-conjugate, commutative
and associative, C is commutative and associative (but no longer self-conjugate), H
is associative but no longer commutative, and finally O is neither commutative nor
associative (but alternative).
The octonions O are the largest division algebra, of dimension eight. Its orthonormal
basis is comprised of the seven imaginary units e1,...,e 7 along with the unit 1 = e0. A
general octonion x may then be written as
x =x0e0 +x1e1 +... +x7e7 with x0,...,x 7∈ R.
The octonionic conjugatex is defined as x =x0e0−x1e1−...−x7e7. The norm of an
octonion x is subsequently defined by ||x||2 =xx =xx, and the inverse of x is given
byx−1 =x/||x||2.
There are many different multiplication tables for octonions, with different authors
using different multiplication rules. Here we will follow the multiplication table used
in [79], which is the multiplication table most naturally obtained via the Cayley-
Dickson process. That is the multiplication of e0,e 1,e 2,e 3 generates H and the mul-
tiplication of e0,e 1 generates C (and of course e0 generates R trivially). One way to
represent octonion multiplication is in terms of the Fano plane; see Figure 1.
Figure 1. The Fano plane, encoding the multiplicative structure of
our octonions, where a≡ea, a= 1,..., 7. Note that each line is cyclic,
representing a quaternionic triple.
The Fano plane representing the multiplication of octonion basis elements can be
summarized as:
eiej =



ej ifi = 0
ei ifj = 0
−δij +ϵijkek otherwise,
where ϵijk is the completely antisymmetric tensor with value 1 when ijk = 123, 145,
176, 246, 257, 347 or 365.
Each projective line in the Fano plane corresponds (together with the identity e0)
to a quaternion ( H) subalgebra; there are seven such subalgebras. All the imaginary
octonion units anti-commute under multiplication. Unlike for the smaller division
CAUSAL FERMION SYSTEMS AND OCTONIONS 7
algebras, the multiplication of elements not belonging to the same H subalgebra is
non-associative. For example,
e4(e7e6) =−e5̸=e5 = (e4e7)e6.
Octonion multiplication however is alternative, meaning that
x(xy) = (xx)y and y(xx) = (yx)x for all x,y∈ O.
By singling out one imaginary octonion basis element, an octonion can be written
as
x = (x0 +x4e4)e0 + (x1−x5e4)e1 + (x2−x6e4)e2 + (x3−x7e4)e3. (2.1)
This singling out of one of the imaginary basis elements of the octonions is equivalent
to choosing a privileged subalgebra of C⊗ O, and induces a splitting of O as C⊕ C3.
Therefore, as vector spaces, the octonions O are therefore isomorphic to C4. this
splitting of O as C⊕ C3 has been associated with the lepton-quark splitting [81]. The
space of internal states of a quark then corresponds to the three complex dimensional
space C3, whereas the internal space of a lepton is C.
The automorphism group of O is the 14-dimensional exceptional Lie groupG2. This
exceptional group contains SU(3) as one of its maximal subgroups, corresponding to
the stabilizer subgroup of one of the octonion imaginary units or, equivalently, the
subgroup of Aut(O) that preserves the representation ofO as the complex space C⊕C3.
On account of being a division algebra, the octonions do not contain any projectors.
One way to include projectors it to instead consider the complex octonions C⊗ O1,
and this is one reason why in octonionic models it is inevitably the complex octonion
algebra C⊗ O that is considered, and not just O. The algebra C⊗ O is no longer a
division algebra (even though the separate factors are), but C⊗ O remains alternative.
Two specific projectors can be introduced in C⊗ O by singling out one of the octonion
basis elements, say e4. The the two mutually annihilating projectors are
ρ± = 1
2(1±ie4),
satisfying the relations
ρ− +ρ+ = 1, ρ 2
− =ρ−, ρ 2
+ =ρ+, ρ −ρ+ =ρ+ρ− = 0.
