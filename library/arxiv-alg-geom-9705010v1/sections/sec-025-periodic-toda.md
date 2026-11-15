---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-025-periodic-toda
section_title: "Periodic Toda"
section_number: null
pages: 32-34
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
RON Y. DONAGI
and (after identifying g with g∗, so that b∗becomes the lower triangulars):
ǫ =






0
1
0
...
0
1
0






, x =






0
1
0
...
0
1
0






.
The orbit Ox ⊂b∗consists of all matrices of the form:





b1
0
a1
...
...
0
an−1bn





with aj̸ = 0 and Σbj = 0. The shifted orbit consists of tridiagonal matrices:





b1
1
0
a1
·
·
·
·
·
·
·
1
0
an−1
bn




.
This is a 2(n−1)-dimensional symplectic manifold (X, σ), isomorphic as symplectic
manifold to the cotangent bundle of the maximal torus T ≈(C∗)n−1. The restric-
tion to it of the symmetric polynomials of SL(n) (= coeﬃcients of the characteristic
polynomial) gives n−1 independent, commuting Hamiltonians. This is the classical
Toda system.
An equivalent system is obtained if ǫ is replaced by m · ǫ with m ∈C∗. When
m = 0, the Hamiltonians become the symmetric functions of the bi. We get the
cotangent bundle X of (C∗)n−1, ﬁbered by its moment map over (C)n−1. Another
variant is to take ǫ = 0, but replace a by the algebra so(n) of skew symmetric
matrices. Now b∗sits in sl(n) as the symmetric matrices, and the orbit consists of
symmetric tridiagonal matrices






b1
c1
c1
b2
...
bn−1
cn−1
cn−1
bn






.
This is conjugate to the previous matrix with ai = c2
i , so we obtain a new version
( ˜X, ˜σ) of Toda which is just a 2n−1-sheeted cover of the previous, basic version,
(X, σ).
The Toda system for a semisimple Lie algebra g is obtained with b a Borel
subalgebra, a the nilpotent radical of the opposite Borel, x = Σeα and ǫ = Σe−α,
where the sums are over the simple roots α with respect to b, and the e±α are
normalized root vectors. The total space can again be identiﬁed with the cotangent
bundle of the maximal torus, a typical element having the form
Σ
α simple(bαhα +
aαeα + e−α) with respect to a standard basis hα, e±α.
Periodic Toda
SEIBERG-WITTEN INTEGRABLE SYSTEMS
33
The periodic Toda systems are obtained when the semisimple algebra g is re-
placed by a loop algebra g(1). This has an extended Dynkin diagram consisting of
the simple roots α of g plus the aﬃne root α0, corresponding to the highest root of
g. The general element of the periodic Toda system can thus be written as
Σα(bαhα + aαeα + e−α) + zeα0 + z−1a0e−α0,
where z is the loop variable, and the product a0
Q
α aα = µ is a ﬁxed non-zero
constant. (For g = sl(n), this is:





b1
1
a0z−1
a1
...
...
...
...
1
z
an−1
bn




,
with Q ai = µ, Σbj = 0).
As in the case of Higgs bundles, the spectral curves Cρ,b depend on the choice
of a representation ρ of G. These Toda curves and their relationships were ﬁrst
studied in [Ml] and [MS], with some clariﬁcations added in [MW1]. Each Cρ,b is
a branched cover of the z-line P1
z. The latter plays the role for periodic Toda which
the base curve E played for the meromorphic Higgs system in §2. The cameral
cover in this situation has a strikingly simple description.
The classifying map
P1
z 99K t/W, which is usually only locally deﬁned, is now a morphism for z̸ = 0, ∞.
It factors through the double cover
P1
z →P1
w
z 7→w = z + µz−1
which maps P1
z\{0, ∞} to A1
w = P1
w\{∞}, followed by an aﬃne linear map
A1
w 7→t/W
whose image in t/W is a straight line pointing in the direction of the invariant
polynomial of highest degree, which is equal to the Coxeter number hg of g. More
precisely, the algebra of polynomial functions on t/W is isomorphic to the algebra
of invariant polynomials on t, which is ﬁltered by the degree. The equations of the
image of A1
w are obtained by ﬁxing the values of all polynomials on t/W whose
pullback to t has degree < hg. The induced W-cover of P1
w then has r = rank(g)
branch points in A1
w, and one at w = ∞. The choice of a Borel labels the ﬁnite
branch points wα by the simple roots α in such a way that the monodromy at wα
is the reﬂection corresponding to α. The monodromy at ∞is then the product of
these reﬂections, the Coxeter element. The Cameral cover is the pullback to P1
z. It
can be described as the W-cover obtained from the trivial cover W ×P1
z by making
r + 1 cuts labelled by the extended set of roots {α} ∪{α0}, each running from
a point zα to µz−1
α , and pasting across each cut according to the corresponding
element of W.
In addition to the loop algebras g(1), there are twisted versions g(k) where k
is the order of an automorphism of the Dynkin diagram of g, and each of these
also gives rise to a periodic Toda system. The basic observation of Martinec and
Warner [MW1] is that each of the known families of pure N = 2 SYM curves arises
as spectral curves for one of these twisted periodic Toda systems.
The speciﬁc
34
RON Y. DONAGI
identiﬁcation involves Langlands duality (Olive-Montonen duality, to a physicist)
exchanging the direction of arrows in the extended diagram. The (untwisted) ex-
tended diagrams for types A, D, E are self-dual, yielding ordinary Toda systems.
The remaining cases yield twisted algebras and systems:
(B(1)
r )∨= A(2)
2r−1, (C(1)
r )∨= D(2)
r+1, (F (1)
4
)∨= E(2)
6 , (G(1)
2 )∨= D(3)
4 .
