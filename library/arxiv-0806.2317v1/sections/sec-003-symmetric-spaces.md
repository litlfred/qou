---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces Aidan Roy ∗"
section_id: sec-003-symmetric-spaces
section_title: "Symmetric spaces"
section_number: null
pages: 7-10
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
doc_brief: "Bounds for codes and designs in complex subspaces Aidan Roy ∗ — We introduce the concepts of complex Grassmannian codes and designs."
---
The group U (n)/U (m) × U (n − m) is an example of a symmetric space : a
factor group G/K such that G is a connected semisimple Lie group and K is
the ﬁxed point set of an involutive automorphism of G. In this section, we use
results from Goodman and Wallach [15] to explain how the deco mposition of
representations of Gm,n follows from this structure.
Let sm denote the m × m matrix with backwards diagonal entries of 1 and
0 elsewhere:
sm :=


0 1
. . .
1 0

 .
Then U (n, s n) denotes the group of matrices which preserve the Hermitian
form ( x, y ) ↦→x∗sny: that is, U (n, s n) is the set of matrices M such that
M ∗snM = sn. This group is isomorphic the standard unitary group U (n).
Deﬁne
Jm,n :=


sm
In−2m
sm

 ,
and consider the involution θ(M ) := Jm,n M Jm,n on GLn(C). The ﬁxed points
of θ have the form
M =


a b c
d e ds m
smcsm smb s masm

 ,
so the ﬁxed point set in GLn(C) is isomorphic to GLm(C) × GLn−m(C).
Lemma 4.1. The ﬁxed point set K of θ in G = U (n, s n) is isomorphic to
U (m) × U (n − m). Therefore Gm,n is a symmetric space.
Proof. For a = (a1, . . . , a m), let ˘a denote the reversal of a, namely
˘a := sma = (am, . . . , a 1).
7
If a, b, and c have length m, n − 2m and m respectively, then we have
Jm,n (a, b, c )T = (˘c, b, ˘a)T . Therefore the 1 and −1 eigenspaces of Jm,n are
V+ = {(a, b, ˘a)} and V− = {(a, 0, −˘a)} respectively. These spaces are orthogo-
nal with respect to the form ( x, y ) ↦→x∗sny.
Now K is the set of points in U (n, s n) which commute with Jm,n . So
decomposing Cn into V+ ⊕ V−, we have that K is the set of points in U (n, s n)
which leave both V+ and V− invariant. In other words, K is the set of points
which preserve the form sn on the subspaces V+ and V−. Thus
K ∼= U (V+, s n|V+ ) × U (V−, s n|V−) ∼= U (n − m) × U (m).
The fact that K is the ﬁxed point set of θ in G implies ([15, Theorem 12.3.5])
that (G, K ) is a spherical pair : for every irreducible representation Vλ of G, the
subspace V K
λ of points ﬁxed by K satisﬁes dim V K
λ ≤ 1. Those representations
such that V K
λ has dimension exactly 1 are called spherical representations. The
following theorem [16, Theorem V.4.3] explains how those re presentation relate
to L2(G/K ).
Theorem 4.2. Let G be a compact simply connected semisimple Lie group,
and let K ≤ G be the ﬁxed point group of an involutive automorphism of G.
Further let ˆGK denote the set of equivalence classes of spherical represen tations
Vλ of G with respect to K. Then L2(G/K ) is a multiplicity-free representation
of G, and
L2(G/K ) ∼=
⨁
λ ∈ ˆGK
Vλ .
To describe which representations are spherical, we now con sider diagonal
subgroups of G and K. For d = ( d1, . . . , d n), let diag( d) denote the diagonal
matrix with diagonal entries d1, . . . , d n. Firstly, note that diag( d) is in U (n, s n)
if and only if dn+1−k = 1/ ¯dk, where ¯dk is the complex conjugate of dk. In other
words, if ¯d−1 denotes the vector (1 / ¯d1, . . . , 1/ ¯dk), then diag( d) is in U (n, s n) if
and only if ˘d = ¯d−1. Secondly, note that if d = diag( a, b, c ) with a and c of
length m, then θ(d) = (˘c, b, ˘a). It follows that the diagonal group
T := {diag(a1, . . . , a m, c m+1, . . . , c n−m, a m, . . . , a 1) : |ai| = 1, ˘c = ¯c −1}
is contained in K. In fact, it is a maximal Abelian subgroup of K: this is called
a torus of K.
Recall that the irreducible representations of G are indexed by the dominant
weights λ = ( λ 1, . . . , λ n), where λ i ≥ λ i+1 and λ i ∈ Z. Now the spherical
representations of G with respect to K are indexed by those particular dominant
8
weights such that tλ = 1 for all t = ( t1, . . . , t n) in the torus T (see Goodman
and Wallach [15, p. 540]). So a dominant weight λ is spherical if it has the
form
λ = (λ 1, . . . , λ m, 0, . . . , 0, −λ m, . . . , −λ 1)
with λ 1 ≥ . . . ≥ λ m ≥ 0 and λ i ∈ Z. In other words:
Theorem 4.3. The irreducible representations of U (n) occurring in L2(Gm,n )
are in one-to-one correspondence with the integer partitio ns with at most m
parts.
For any partition µ , we let Hµ (n), or simply Hµ , denote the irreducible
representation in L2(Gm,n ) isomorphic to V(µ, 0,..., 0, −˘µ ). The Weyl character
formula (equation (3.1)) now tells us the dimension of each Hµ . The ﬁrst few
dimensions are:
dim H(0) = dim V(0,..., 0) = 1
dim H(1) = dim V(1, 0,..., 0, −1) = n2 − 1
dim H(2) = n2(n − 1)(n + 3)
4
dim H(1, 1) = n2(n + 1)(n − 3)
4
dim H(2, 1) = (n2 − 1)2(n2 − 9)
9
dim H(k) =
(n + k − 2
k
) 2 n + 2k − 1
n − 1
dim H(1,..., 1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
k
) =
(n + 1
k
) 2 n − 2k + 1
n + 1
If m = 1, then Gm,n is the complex projective space CP n−1, and only the
spaces H(k) occur. In that case H(k) is isomorphic to the space Harm( k, k ) of
harmonic polynomials of homogeneous degree k in both z and ¯z, where z =
(z1, . . . , z n) is a point on the unit sphere in Cn. Those harmonic polynomials
were used by Delsarte, Goethals, and Seidel in their LP bound s for codes and
designs the complex unit sphere [11].
We now record a few more representations of U (n) we will need later. Given
an nonincreasing sequence of nonnegative integers µ = ( µ 1, µ 2, . . . ), we say µ
has size k and write |µ | = k if µ is a partition of k; that is, ∑
i µ i = k. We also
say µ has length l and write len( µ ) = l if µ has l nonzero entries. For example,
9
(2, 1, 0, . . . ) has size 3 and length 2. Then for ﬁxed Gm,n , deﬁne Hk = Hk(m, n )
as follows:
Hk(m, n ) :=
⨁
|µ |≤k
len(µ )≤m
Hµ (n).
For k > 0 this representation is reducible, and Hk−1 is contained in Hk. When
m = 1, Hk is isomorphic to the space of homogeneous polynomials degre e k in
both z and ¯z on the unit sphere in Cn. In the next section, we will see that
Hk is also the span of the degree- k symmetric polynomials on the principal
angles between a ∈ G m,n and some ﬁxed b ∈ G m,n . Moreover, if g and h are
polynomials in Hk and Hk′ respectively, then gh is in Hk+k′, and in fact Hk+k′
is spanned by polynomials of that form.
We also let Hom k(n) ⊆ L2(Gm,n ) denote the space of polynomials which are
homogeneous of degree k in the entries of Pa, where Pa is the projection matrix
of a ∈ G m,n . Since the constant function Pa ↦→tr(Pa) = m is in Hom 1(n), it
follows that Hom k−1(n) can be embedded into Hom k(n). Similarly for ﬁxed b,
the distance function Pa ↦→tr(PaPb) is in Hom 1(n). The next section will also
show that Hk is a subspace of Hom k.
James and Constantine [17] further investigated the irredu cible subspaces
