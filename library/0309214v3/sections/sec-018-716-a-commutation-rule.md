---
doc_id: 0309214v3
doc_title: "The colored Jones function is q-holonomic"
section_id: sec-018-716-a-commutation-rule
section_title: "A commutation rule"
section_number: 7.1.6
pages: 27-29
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
doc_brief: "The colored Jones function is q-holonomic — A function of several variables is called holonomic if, roug hly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many l inear"
---
For x, y ∈ U homogeneous let us deﬁne
[x, y]q := xy − v(|x|,|y|)yx.
Note that, in general, [ y, x]q is not proportional to [ x, y]q .
An important property of the PBW basis is the following commu tation rule, see
[18]. If i < j then [ fi, fj]q belongs to U −[j − 1, i + 1] (which is 0 if j = i + 1).
Geometry & Topology, Volume 9 (2005)
1280 Stavros Garoufalidis and Thang T Q Lˆ e
It follows that U −[j, i] is an algebra. This allows us to sort algorithmically non-
commutative monomials in the variables fi . Also two consecutive variables
always q –commute: [ fi, fi+1]q = 0.
Similarly, if i < j then [ ei, ej]q belongs to U +[i+1, j−1] (which is 0 if j = i+1).
It follows that U +[i, j] is an algebra, and two consecutive variables always q –
commute, [ ei, ei+1]q = 0.
7.2 q–holonomicity of quantum groups
Suppose A : U → U is a linear operator. Using the PBW basis of U (see
Equation (4)), we can present A by a matrix:
A(xσ) =
∑
σ′
Aσ′
σ xσ′,
with Aσ′
σ ∈ Q(v). We call ( σ, σ′) the coordinates of the matrix entry Aσ′
σ .
Deﬁnition 7.2 We say that A is q –holonomic if the matrix entry Aσ′
σ , con-
sidered as a function of ( σ, σ′) is q –holonomic with respect to all the variables.
A priori this deﬁnition depends on the reduced word w. But we will soon see
that if A is q –holonomic in one PBW basis, then it is so in any other PBW
basis.
7.2.1 q –holonomicity of transition matrix
Suppose xσ(w′) is another PBW basis associate to another reduced word w′
representing the longest element of W . Then we have the transition matrix M σ′
σ
between the two bases, with entries in Q(v). The next proposition checks that
the entries of the transition matrix are q –holonomic, by a standard reduction
to the rank 2 case.
Proposition 7.3 Except for the case of G2 , the matrix entry M σ′
σ is q –
holonomic with respect to all its coordinates.
Proof Since any two reduced presentations of an element of W are related
by a sequence of Coxeter moves, it is enough to consider the ca se of a single
Coxeter move. Since each Coxeter move involves only two fund amental roots
and all Tα ’s are algebra isomorphisms, it is enough to considered the case of
rank 2 Lie algebras. For all rank 2 Lie algebras (except G2 ) we present the
proof in Appendix.
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q –holonomic 1281
