---
doc_id: gambaudo-ghys-braids-signatures-2005
doc_title: "Braids and signatures"
section_id: sec-005-21-the-burau-representation-consider-the-homomor
section_title: "The Burau representation. — Consider the homomorphism φ n from"
section_number: 2.1
pages: 8-10
source_pdf: gambaudo-ghys-braids-signatures-2005.pdf
source_sha256: 647f4c28cab7428d
doc_brief: "Braids and signatures — 62 sections: Introduction; (v1) −v1 =v2 −γ 2(v2) and deﬁne; (α,β ) which is a 2-fold branched"
---
the fundamental group of the punctured disc D2 \ {x0
1,...,x 0
n} to Z which
maps every (conjugacy class of) small positive simple loop a round each base
point x0
i to the generator 1 in Z. The kernel of this homomorphism deﬁnes
an inﬁnite cyclic covering D∞
n of D2 \ {x0
1,...,x 0
n}. Figure 5 illustrates this
covering for n = 3 and shows the graph of z ↦→arg(z3 − 1).
Figure 5. Covering of the punctured disc
A standard result by Birman [4] states that the Artin braid gr oup Bn is iso-
morphic to the group of isotopy classes of homeomorphisms of the disc D2(n+ 1
2 )
that ﬁx the boundary ∂ D2(n + 1
2 ) pointwise and leave globally invariant the set
of points {x0
1,...,x 0
n}. Thus, each braid β in Bn can be represented by some
homeomorphism hβ of D2(n + 1
2 ). We choose the lift ~hβ of hβ to D∞
n that
leaves the boundary pointwise ﬁxed. Clearly this lift is not uniquely deﬁned
byβ but its homotopy class is. In particular, the map ( ~hβ )⋆ induced by ~hβ on
the ﬁrst homology group of D∞
n is determined by β . Note that the braid α ·β
consists of α followed byβ so that we get a linear anti-representation (rather
than a representation) of Bn in the group of automorphisms of H1(D∞
n ; R). If
we consider the dual action on the ﬁrst cohomology with compa ct support, we
get a linear representation of Bn.
tome 133 – 2005 – n o 4
BRAIDS AND SIGNATURES 549
In order to produce an explicit formula for this representat ion, we choose
a base point z in D2 \ {x0
1,...,x 0
n} and embed a wedge Rn of n circles based
at z, made of n positive simple loops e1,...,e n going once around x0
1,...,x 0
n
respectively. Choose some lift ~z of z in D∞
n and denote by ~e1,..., ~en the
paths lifting e1,...,e n and starting from ~z. The inverse image of Rn in D∞
n
is a 1-complex ~R∞
n and we denote by ~C∞
n the module of integral 1-chains
on ~R∞
n , which can be seen as a Z[t,t − 1]-module, using the deck transformations.
This is a free module on ~e1,..., ~en. The sub-module ~Z ∞
n of 1-cycles consists of
those chains in ~R∞
n such that the sum of the coordinates in this basis is zero.
Therefore, ~Z ∞
n is the free module on
v1 = ~e1 − ~e2, v2 = ~e2 − ~e3, ... , vn− 1 = ~en− 1 − ~en.
z
~z
t~z
e1
t~e1
~e1
Figure 6. The complex Rn and its cover
The action of any braid in Bn on the ﬁrst homology of D∞
n commutes
with the action of deck transformations. This homology is is omorphic to ~Z∞
as a Z[t,t − 1]-module. By deﬁnition, the dual action on cohomology with c om-
pact support, in the dual basis, is the (reduced) Burau representation Bt. In the
standard presentation of Bn, the images of the generators σ i are the matrices
Bt(σ 1) =






−t− 1 0 0 ... 0
t− 1 1 0 ... 0
0 0 1 ... 0.
.
.
.
.
.
.
.
. . . . .
.
.
0 0 0 ... 1






, Bt(σ n− 1) =






1 ... 0 0 0.
.
. . . . .
.
. .
.
. .
.
.
0 ... 1 0 0
0 0 0 1 1
0 0 0 0 −t− 1






Bt(σ i) =











1 ... 0 0 0 ... 0.
.
. . . . .
.
.
.
.
.
.
.
.
.
.
.
0 ... 1 1 0 ... 0
0 ... 0 −t− 1 0 ... 0
0 ... 0 t− 1 1 ... 0.
.
. .
.
. .
.
. .
.
. . . . .
.
.
0 ... 0 0 0 ... 1











(for 2 ≤ i ≤ n − 2, where the diagonal −t− 1 is in position ( i,i )).
BULLETIN DE LA SOCI ´ET´E MATH ´EMATIQUE DE FRANCE
550 GAMBAUDO (J.-M.) & GHYS (E.)
We also denote by Bt the corresponding linear representation of B∞ in the
ascending union GL(∞, Z[t,t − 1]) of the GL(n − 1, Z[t,t − 1]).
Remark 1 . — The convention about the choice of the generators of the
braid group is not uniform in the literature. Many authors us e the generators
σ ′
i =σ − 1
i . This remark will help the reader to convince himself or hers elf that
the above Burau representation is indeed the Burau represen tation [13].
Remark 2 . — The matrices that one gets using the action in homology are
obviously transposed of the previous ones. When referring t o these matrices, we
will speak about the Burau anti-representation and transpo sed Burau matrices.
