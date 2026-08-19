---
doc_id: arxiv-2301.02038v1
doc_title: "Contemporary Mathematics Vinogradov’s Cohomological Geometry of Partial Diﬀerential Equations"
section_id: sec-002-11-jet-spaces
section_title: "jet spaces"
section_number: 1.1
pages: 3-6
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
doc_brief: "Contemporary Mathematics Vinogradov’s Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a"
---
1.2. the Cartan distribution 6
1.3. diﬃeties 8
2. Cohomology of PDEs 10
2.1. horizontal cohomology 10
2.2. interpreting horizontal cohomologies 12
2.3. algebraic structures on horizontal cohomologies 15
3. Homotopy of PDEs 18
3.1. homotopy algebras 18
3.2. the LR∞-algebra of secondary vector ﬁelds 20
3.3. the A∞-algebra of secondary diﬀerential operators 22
References 25
4 F ABRIZIO PUGLIESE, GIOV ANNI SPARANO, AND LUCA VITAGLIANO
1. Geometry of PDEs
In this section we show that a system of, generically non-lin ear, PDEs can be
encoded into a geometric object: a diﬃety . We will work in the rather general
setting of a PDEs imposed on submanifolds N of a ﬁxed dimension n in a manifold
P (see [ 10]), in contrast with most of the literature where only PDEs im posed on
sections of a ﬁbration (or a ﬁber bundle) are considered.
1.1. jet spaces. Let n,m be non-negative integers, and let P be a manifold
of dimension n +m. We begin providing an intrinsic deﬁnition of derivatives of
an n-dimensional submanifold N⊆ P . In the following, n should be interpreted
as the number of independent variables , m as the number of dependent variables ,
and P as the space parameterizing both independent and dependent variables. In
other words, in this theory, dependent and independent vari ables can be mixed
and swapped. Around every point p∈ N there are coordinates (xi,uα) on P ,
i = 1,...,n ,α = 1,...,m , adapted toN in the sense that, in these coordinates, N
looks like the graph of a map :
(1.1) N :uα =fα(x).
We will need to take multiple partial derivatives of the f ’s with respect to the x’s.
We adopt the following notation. Let h be a non-negative integer and letI =i1··· ih
be a multiindex, i.e. a (possibly empty) word containing h letters iℓ∈{ 1,...,n },
ℓ = 1,...,h . We identify two words if they only diﬀer by a permutation of t heir
letters. We also compose two words by concatenation. Denote |I| :=h and call it
the lenght of the multiindex I. Finally denote
∂|I|fα
∂xI := ∂hfα
∂xi1...∂x ih
.
If there is another n-dimensional submanifolds ˜N through p, i.e. p∈ N∩ ˜N ,
then around p there are coordinates (xi,uα) on P adapted to both N, ˜N :
N :uα =fα(x), and ˜N :uα = ˜fα(x).
In this case we say that N and ˜N are tangent up to order k = 0, 1,..., ∞ at p if
∂|I|fα
∂xI (p) = ∂|I| ˜fα
∂xI (p), for all multiindexes I with|I|≤ k,
and we write N∼k
p ˜N . Tangency up to order k at p is a well-deﬁned equivalence
relation on submanifolds through p. In particular, it is independent of the choice of
adapted coordinates. The equivalence class of N is denoted Nk
p and called the k-jet
of N at p. In other words, k-jets at p encode partial derivatives of n-dimensional
submanifolds at p up to order k. The space of tangency classes is denoted Jk
p (P,n ).
Finally put
Jk(P,n ) =
∐
p∈P
Jk
p (P,n ).
We call Jk(P,n ) the k-jet space of n-dimensional submanifolds of P . It is clear
that J 0(P,n ) identiﬁes naturally with P and J 1(P,n ) identify with the bundle of
n-Grassmannians in the ﬁbers of the tangent bundle TP . More precisely, the 0-jet
ofN atp identiﬁes with p itself, while the 1-jet of N atp identiﬁes with the tangent
space TpN . For a general k, the space Jk(P,n ) can be coordinatized as follows.
Choose coordinates (xi,uα) on P , and let U⊆ Jk(P,n ) be the subset consisting
VINOGRADOV’S COHOMOLOGICAL GEOMETRY OF PDES 5
of k-jets of submanifolds for which (xi,uα) are adapted coordinates. We deﬁne
coordinates (xi,uα
I ) on U by putting
xi(
Nk
p
)
:=xi(p), and uα
I
(
Nk
p
)
= ∂|I|fα
∂xI (p),
for allN locally given by (1.1), i = 1,...,n ,α = 1,...,m , and|I|≤ k. The (xi,uα)
are called jet coordinates, they cover Jk(P,n ) and, for k <∞, they give to Jk(P,n )
the structure of a smooth manifold. For all h≤k≤∞ the are projections
Jk(P,n )→Jh(P,n ), N k
p↦→Nh
p,
and by Borel Lemma J ∞(P,n ) identiﬁes with the inverse limit of the tower of
surjective submersions
J 0(P,n )←−···←− Jk−1(P,n )←−Jk(P,n )←−··· .
This gives to the ∞-jet space the structure of a pro-ﬁnite dimensional manifol d
(see, e.g., [ 2, 27 ], see also [ 3]).
Remark 1.1. For the reader more familiar with jets of sections, we mentio n
that, when P is ﬁbered over some n-dimensional manifold M , then, for all k≤∞ ,
the space Jk(P,M ) of k-jets of sections of P overM can be recovered as the open
and dense submanifold of Jk(P,n ) consisting of jets of n-dimensional submanifolds
transverse to the projection P→ M . The open embedding Jk(P,M )֒→Jk(P,n )
maps the k-jet at x∈ M of a (possibly local) section s of P→ M to the k-jet of
its image at s(x).
Diﬀerential calculus on J ∞(P,n ) can be deﬁned algebraically. For instance,
we deﬁne smooth functions C∞(J ∞(P,n )) on J ∞(P,n ) as the direct limit of the
algebra ﬁltration
(1.2) C∞(
J 0(P,n )
)
֒···֒→C∞(
Jk−1(P,n )
)
֒→C∞(
Jk(P,n )
)
֒··· .
In other words a smooth function on J ∞(P,n ) is a smooth function of the inde-
pendent variables xi, the dependent variables uα, and their derivatives up to some
ﬁnite order k, but k can be arbitrarily high (sometimes they are deﬁned as func-
tions which are only locally of this type). Vector ﬁelds, diﬀ erential forms, etc., on
J ∞(P,n ) are deﬁned in a way compatible with the ﬁltration (1.2). We wi ll not
insist on these technicalities and we refer to [ 2] for details.
Remark 1.2. We stress that, in this ∞-dimensional setting, some important
results in ﬁnite dimensional diﬀerential geometry might fa il. To mention a few: the
inverse function theorem, existence and uniqueness of the ﬂ ow of a vector ﬁeld, the
Frobenius theorem, etc.
Anyn-dimensional submanifold N⊆P deﬁnes a new n-dimensional submani-
fold
Nk :=
{
Nk
p :p∈N
}
in Jk(P,n ), called the k-jet prolongation of N . If N locally looks like (1.1) in
coordinates, then Nk locally looks like
Nk :uα
I = ∂|I|fα
∂xI (x), |I|≤ k,
in jet coordinates.
6 F ABRIZIO PUGLIESE, GIOV ANNI SPARANO, AND LUCA VITAGLIANO
Remark 1.3. Let N⊆ P be an n-dimensional submanifold. For all k≤∞ ,
the map
jk :N→Nk, p ↦→Nk
p
is a diﬀeomorphism. In particular N embeds into Jk(P,n ) for all k. When P is
ﬁbered over some n-dimensional manifold M , and s :M→P is a (possibly local)
section of P overN , then the usual k-jet prolongation jks ofs can be recovered as
the composition
jks :M
s
−→ ims
jk
−→ (ims)k֒→Jk(P,M ).
Remark 1.4. Let r be a non-negative integer and let Q ⊆ P be an (n +
r)-dimensional submanifold. Then, for all k ≥ 0, the k-jet space Jk(Q,n ) is a
submanifold in the k-jet space Jk(P,n ) in the obvious natural way.
