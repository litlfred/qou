---
doc_id: arxiv-math-0510265v3
doc_title: "Triply-graded link homology and Hochschild homology of Soergel bimodules Mikhail Khovanov"
section_id: sec-002-1-r-over-the-subalgebra-r
section_title: "R′ over the subalgebra R′"
section_number: 1
pages: 8-17
source_pdf: 0510265v3.pdf
source_sha256: 548a0eece08bd967
doc_brief: "Triply-graded link homology and Hochschild homology of Soergel bimodules Mikhail Khovanov — We trade matrix factorizations and Koszul complexes for Hochschild homology of Soergel bimodules to modify"
---
1
of symmetric polynomials in x1, x2.
Thus, the relation between [KR2] and Soergel bimodules beco mes clear,
at least locally, for a single wide edge. Globally, a resolut ion D consists of
several wide edges and a number of arcs, as shown in ﬁgure 4. Pu t marks
(i, j) on arcs of D, for 0 ≤ i ≤ r and 1 ≤ j ≤ m, where r is the number of
wide edges.
Consider the polynomial ring ~R = Q[xi,j] in ( r + 1) m variables. The
Koszul complex of D (in the a = 0 case) corresponds to the following sequence
of ( r + 1)m elements of ~R. For each 1 ≤ i ≤ r we have m elements, two of
which are xi,s + xi,s+1 − xi−1,s − xi−1,s+1, x i,sxi,s+1 − xi−1,sxi−1,s+1 and the rest
are xi,j − xi−1,j for 1 ≤ j ≤ m, j ⁄= s, s + 1. Here s is the position (counting
from the left) of the i-th wide edge of D; s is a function of i. The remaining
m elements of the sequence are x0,j − xr,j for 1 ≤ j ≤ m.
Lemma 1 The ﬁrst rm elements on the above list constitute a regular se-
quence in ~R.
To prove the lemma, start with the bottom m variables x0,1, . . . , x0,m and
work your way up. Each time we add a new layer of m variables, we encounter
m new elements xi,s + xi,s+1 − xi−1,s − xi−1,s+1, x i,sxi,s+1 − xi−1,sxi−1,s+1, and
xi,j − xi−1,j for 1 ≤ j ≤ m, j ⁄= s, s + 1. These constitute a regular sequence,
for they can be matched with the new variables (for any Q-algebra S and
any f ∈ S, the element xk − f is not a zero divisor in S[x]). □
By the time we reach the top layer of variables, we take the quo tient of ~R
by the above rm variables. The quotient ring is naturally isomorphic to the
8
0,1 0,2
1,21,1 1,m
0,m
r,1 r,2 r,m
Figure 4: A resolution D of a braid’s closure
Soergel bimodule B′(D) assigned to D, the tensor product of r bimodules
B′
s (s is as before, and depends on the layer of the diagram). The Kos zul
complex of D is quasiisomorphic to the Koszul complex of the quotient rin g
B′(D) assigned to the sequence of the remaining m elements x0,j − xr,j,
for 1 ≤ j ≤ m. The latter complex computes the Hochschild homology of
B′(D). Thus, the Hochschild homology of B′(D) is naturally isomorphic to
the homology of the Koszul complex of D, the latter isomorphic to the direct
sum of two copies of CH (D).
Downsizing from m variables xi,1, . . . , xi,m to their diﬀerences gives us
an isomorphism between the reduced homology CH (D) and the Hochchild
homology of B(D). These isomorphisms, over all D, respect the diﬀeren-
tials in the complexes computing H(σ) and HHH( σ), leading to the desired
isomorphism
HHH(σ) ∼= H(σ).
It was shown in [KR2] that H(σ) is a link invariant, up to a grading shift.
Therefore, the same is true of HHH( σ).
□
The isomorphism between H and HHH is nontrivial on their trigradings.
First of all, a not so natural shift by ( −1, 1, 0) was built into the deﬁnition
of H due to the presence of a. After shifting H back by (1 , −1, 0), both
9
homology groups H(σ∗) and HHH( σ∗) of the trivial 1-strand braid σ∗ become
one-dimensional vector spaces sitting in tridegree (0 , 0, 0). After this shift is
accounted for, the trigradings of the two theories relate as follows.
The third gradings of H and HHH perfectly match. The third grading
is the “cohomological” grading of both theories which comes last into the
deﬁnition and not visible on the homology groups CH (D) and H(R, B(D))
assigned to resolutions.
The Hochschild grading on HHH matches the Koszul grading on H taken
with the minus sign, the sign due to the diﬀerence in conventi ons.
Finally, the second grading on H equals the grading on HHH by deg( xi)
minus the Hochschild grading, due to the normalization in [K R2, page 2]
giving d bidegree (1 , 1).
Hecke algebras, Soergel bimodules and Kazhdan-Lusztig the ory.
The Iwahori-Hecke algebra Hm of the symmetric group is a Z[q, q−1]-algebra
with generators T1, . . . Tm−1 and relations
(Ti − q2)(Ti + 1) = 0 ,
TiTi+1Ti = Ti+1TiTi+1,
TiTj = TjTi for |i − j| > 1.
(our q is usually denoted q
1
2 in the literature). Hm is a free Z[q, q−1]-module of
rank n! and has a natural basis {Tw}w, over all permutations w ∈ Sm, where
Tw = Ti1 . . . Tir if si1 . . . sir is a reduced presentation of w as the product of
transpositions si = ( i, i + 1). We denote r by l(w) and call it the length of
w. In our notations, Tsi = Ti. Left multiplication by Ti in this basis has the
form
TiTw =
{ Tsiw if l(siw) > l(w)
q2Tsiw + (q2 − 1)Tw if l(siw) < l(w)
The involution ι of Hm takes q to q−1, T w to (Tw−1)−1 and acts on generators
by
ι(Ti) = q−2Ti + (q−2 − 1).
The element C ′
i = q−1(1 + Ti) is ﬁxed by ι.
Proposition 2 The Hecke algebra has a basis {C ′
w}, over all w ∈ Sm, with
the elements uniquely determined by the conditions ι(C ′
w) = C ′
w and
C ′
w = q−l(w)
∑
y≤w
Py,w(q)Ty,
where Py,w(q) ∈ Z[q2], P w,w = 1 and deg Py,w < l (w) − l(y) if y ⁄= w. The
inequality sign under the sum sign refers to the Bruhat parti al order on Sm.
10
This proposition is due to Kazhdan and Lusztig [KL1] and admi ts a
direct combinatorial proof. The basis {C ′
w} is called the Kazhdan-Lusztig
basis (they also introduced a related basis {Cw} which won’t appear in this
exposition). The incredibly hard result, though, is the fol lowing.
Proposition 3 Coeﬃcients of polynomials Py,w are nonnegative integers.
The multiplication in the basis {C ′
w} has coeﬃcients in N[q, q−1].
Kazhdan-Lusztig’s proof of this result [KL2] is essentiall y a categoriﬁca-
tion: coeﬃcients of Py,w are realized as dimensions of cohomology groups
associated to simple perverse sheaves on the ﬂag variety G/B, where G =
SL(m, C) and B a Borel subgroup of G. Multiplication in the basis {C ′
w}
corresponds to the convolution of correspondences on the pr oduct variety
G/B×G/B. Both positivity results rely on Beilinson, Bernstein and De ligne’s
theory of perverse sheaves [BBD] (see also [GM]), including the decomposi-
tion theorem, which, in turn, requires Deligne’s theory of w eights and mixed
l-adic sheaves (an outgrowth of Deligne’s proof of the Weil co njectures). The
latter is based on Grothendieck’s etale cohomology theory o f varieties in ﬁnite
characteristic. A characteristic zero alternative approa ch, via mixed Hodge
modules, was developed by M. Saito (see [Sa], [T] and referen ces therein).
Moreover, the work of Beilinson-Bernstein [BB] and Brylins ki-Kashiwara
[BK] on localization relates the whole story to inﬁnite-dim ensional repre-
sentations of slm and implies that Py,w(1) describe multiplicities of simple
modules in the Verma modules for slm.
Here are some additional references on these topics. See [H] for Hecke
algebras and Kazhdan-Lusztig polynomials, [Sp], [Mi] for l ocalization, [M],
[Ki] for intersection homology and perverse sheaves, [KW] f or l-adic and
perverse sheaves and relation to KL polynomials.
To explain how Soergel bimodules ﬁt into the picture, we rewr ite the
deﬁning relations for the Hecke algebra via the generators C ′
i = C ′
si. The
relations become
C ′2
i = ( q + q−1)C ′
i,
C ′
iC ′
i+1C ′
i + C ′
i+1 = C ′
i+1C ′
iC ′
i+1 + C ′
i,
C ′
iC ′
j = C ′
jC ′
i |i − j| > 1.
To match the bimodule Bi with the generator C ′
i, shift its grading down by
1 and denote by
Bi = Bi{−1}.
Now recall one of Soergel’s results [S1].
11
Proposition 4 There are isomorphisms of graded R-bimodules
Bi ⊗R Bi ∼= Bi{1} ⊕ Bi{−1},
(Bi ⊗R Bi+1 ⊗R Bi) ⊕ Bi+1 ∼= (Bi+1 ⊗R Bi ⊗R Bi+1) ⊕ Bi,
Bi ⊗R Bj ∼= Bj ⊗R Bi |i − j| > 1.
Only the middle isomorphism is non-trivial. Let
Bi,i+1 = R ⊗Ri,i+1 R{−3},
where Ri,i+1 is the ring of invariants under the action of S3 on R permuting
xi, xi+1, xi+2. Soergel shows
Bi ⊗R Bi+1 ⊗R Bi ∼= Bi,i+1 ⊕ Bi,
Bi+1 ⊗R Bi ⊗R Bi+1 ∼= Bi,i+1 ⊕ Bi+1,
which implies the middle isomorphism.
The above isomorphisms between tensor products of Soergel b imodules
lift deﬁning relations in the Hecke algebra, when we associa te bimodule Bi
to the element C ′
i. Multiplication by q corresponds to the grading shift up
by 1.
Furthermore, the Kazhdan-Lusztig basis in H3 is given by
C ′
e = 1, C ′
s1 = C ′
1, C ′
s2 = C ′
2,
C ′
s1s2 = C ′
1C ′
2, C ′
s2s1 = C ′
2C ′
1,
C ′
w = C ′
1C ′
2C ′
1 − C ′
1 = C ′
2C ′
1C ′
2 − C ′
2,
where w = s1s2s1 = s2s1s2 is the longest element in S3 and e denotes the
unit element of S3.
Arbitrary tensor products of bimodules B1, B2 can have only 6 diﬀerent
indecomposable summands, up to isomorphism and grading shi fts:
R, B1, B2, B1 ⊗R B2, B2 ⊗R B1, B1,2.
Tensor products of these bimodules match the multiplicatio n in the Kazhdan-
Lusztig basis of H3.
Soergel extends this patterns to all m. For technical reasons he uses C as
the ground ﬁeld instead of Q. He shows the existence of graded indecompos-
able R-bimodules Bw, for w ∈ Sm, with the following properties:
• Bw is a ﬁnitely-generated projective left R-module and a ﬁnitely-generated
projective right R-module.
12
• Bsi = Bi, and Be = R.
• This collection of bimodules is closed under tensor product :
Bw ⊗R By ∼= ⊕
z∈Sm
B
nz
wy
z ,
where nz
wy ∈ N[q, q−1] are structure coeﬃcients of the multiplication in
the Kazhdan-Lusztig basis {C ′
w} of Hm,
C ′
wC ′
y =
∑
z
nz
wyC ′
z.
This construction, together with the original work of Kazhd an and Lusztig,
can be viewed as a categoriﬁcation of the Hecke algebra. The K azhdan-
Lusztig basis lifts to a collection of bimodules, multiplic ation in the Hecke
algebra lifts to the tensor products of bimodules, etc.
More precisely, Soergel bimodules can be used to produce a ca tegoriﬁca-
tion of the Hecke algebra action on its regular representati on. The regular
representation becomes the Grothendieck group of the grade d version of the
category of Harish-Chandra bimodules for slm (with generalized trivial cen-
tral character on both sides). To each w ∈ Sm there is assigned an exact
endofunctor in this category, which acts on the Grothendiec k group in the
same way as C ′
w acts by left multiplication on Hm. The endofunctors can be
reconstructed from bimodules Bw, composition of endofunctors matching the
tensor product of these bimodules. Some details can be found in [S1], others
follow from Soergel’s results.
The group G = SL(m, C) acts transitively on the ﬂag variety G/B. The
diagonal action of G on G/B × G/B has ﬁnitely many orbits, which are in a
natural bijection with elements of the symmetric group. The diagonal orbit
corresponds to the trivial element, and the open orbit–to th e maximal length
permutation. Let Ow be the orbit associated with w ∈ Sm. There exists a
complex of sheaves IC( Ow) (the intersection cohomology sheaf), supported
on the closure of Ow. This complex of sheaves is G-equivariant and its stalk
cohomology groups are constant along each orbit. According to Soergel [S2],
bimodule Bw is isomorphic to the G-equivariant cohomology of this complex,
Bw ∼= HG(IC(Ow)).
The bimodule structure comes from identifying R with the G-equivariant
cohomology of G/B.
13
Example: when m = 2, the ﬂag variety is P1 and G acts on P1 × P1 with
two orbits: the diagonal and its complement. The closure of e ach orbit is
smooth, and the IC sheaf is the constant sheaf on the orbit’s c losure, shifted
by the dimension of the orbit. Consequently, the equivarian t cohomology
groups of these IC sheaves are the equivariant cohomology gr oups of the
diagonal and of P1 × P1. They are
HG(P1) ∼= HB(·) ∼= HSO(2)(·) ∼= C[y] ∼= R,
HG(P1 × P1) ∼= HB(P1) ∼= HSO(2)(P1) ∼= B1,
where dot denotes a point, and y a generator of H 2(CP∞, Q). The group
SO(2) acts on P1 ∼= S2 by rotations about the north pole-south pole axis.
The action is free except at the poles, and the quotient by the action is nat-
urally the interval [ −1, 1]. The cohomology can be rewritten as H( S2 ×SO(2)
ESO (2)). The space S2 ×SO(2) ESO (2) maps onto the orbit space [ −1, 1] of
S2 under the SO(2) action. The ﬁber over each point other than −1, 1 is
contractible, while over −1 and 1 the ﬁber is isomorphic to CP∞. Therefore,
the equivariant cohomology is naturally isomorphic to the c ohomology of the
1-point union of two copies of CP∞. This cohomology can be identiﬁed with
R ⊗R1 R as a graded R-bimodule, and even as a ring.
For an arbitrary m, the bimodule Bi is isomorphic to the G-equivariant
cohomology groups of the “thickened” ﬂag variety
Y = {(L1, . . . , Li, . . . , Lm−1, L′
i)| dim(Lj) = j, dim(L′
i) = i,
0 ⊂ L1 ⊂ L2 ⊂ · · · ⊂Lm−1 ⊂ Cm, Li−1 ⊂ L′
i ⊂ Li+1}.
Bimodules B w and link homology.
Our deﬁnition of link homology HHH( σ) used only tensor products of Bi
rather than all Bw, which are the indecomposable summands of the ten-
sor products. However, the Koszul resolution of indecompos able bimod-
ule Bsisi+1si appear in the proof of the invariance of H(σ) under the third
Reimeister move [KR2, Section 6].
Indecomposable bimodules Bw might prove useful in computations of link
homology. Each term F j(σ) of the complex F (σ) decomposes as a direct sum
of Bw, with various shifts and multiplicities,
F j(σ) ∼= ⊕
w
Bnw(σ,j)
w , n w(σ, j) ∈ N[q, q−1].
Suppose we know these multiplicities nw(σ, j) and have the formula for the
diﬀerential with respect to these direct sum decomposition s of F j(σ). For
14
each j the diﬀerential is described by an n!×n! matrix, with rows and columns
enumerated by w. The (y, w)-entry is itself a matrix with ny(σ, j+1)|q=1 rows
and nw(σ, j)|q=1 columns describing the direct summand
Bnw(σ,j)
w − →Bny(σ,j+1)
y
of the diﬀerential
∂ : F j(σ) − →F j+1(σ).
Each entry of the latter matrix is a homomorphism of bimodule s Bw − →By
of a particular degree.
This horrendous complex can be simpliﬁed, by stripping oﬀ co ntractible
summands of the form
0 − →Bw{i}
1
− →Bw{i} − →0.
Such a summand exists whenever there is an entry in the j-th matrix of
matrices which is a nonzero complex multiple (recall we are w orking over C)
of the identity map of Bw{i}.
Throwing out all contractible summands from F (σ) results in a much
smaller complex which we denote Fmin(σ). Up to isomorphism, Fmin(σ) does
not depend on the order and choices of removed contractible s ummands. The
reduction to Fmin(σ) is best done inductively on the length of σ = σǫ1
i1 . . . σǫn
in
Once we found Fmin(σǫ1
i1 . . . σǫr
ir ), for some r < n, tensor it with F (σǫr+1
ir+1 ) and
reduce to minimal size. We start with r = 1 and proceed until r = n. The
resulting minimal complex is isomorphic to Fmin(σ).
To determine HHH( σ), we take the Hochschild homology of each term
F j
min(σ), arrange them into a complex and take its cohomology.
Remark: A similar algorithm to compute the sl(2) link homology was
found by Dror Bar-Natan and implemented by him and Jeremy Green [BN1,2,3].
They represent a link as a composition of elementary tangles L = t1 . . . tn. In
the language of [K], the invariant of a tangle t1 . . . tr is a complex of graded
projective H s-modules where 2 s is the number of endpoints of t1 . . . tr. After
splitting oﬀ all contractible summands from the complex (th us reducing it to
minimal size), tensor it with the complex assigned to tr+1, reduce the product
to minimal size, and so on. We note that Bar-Natan and Green us e a more
reﬁned and, at the same time, more geometric framework than t hat of rings
H s.
Example: When m = 2 and σ = σn
1 , the reduction leads to a simple
computation of homology groups HHH( σ). The complex F (σ) consists of 2 n
15
terms which are tensor powers of B1. The minimal complex has only n + 1
indecomposable bimodules:
0 − →R{2n}
d0
− →B1{2n − 2}
d1
− →B1{2n − 4}
d2
− → · · ·
dn
− →B1 − →0
The diﬀerential is
d0(1) = 1 ⊗ y + y ⊗ 1,
di(1 ⊗ 1) = 1 ⊗ y − y ⊗ 1 odd i > 0,
di(1 ⊗ 1) = 1 ⊗ y + y ⊗ 1 even i > 0,
where R = Q[y], y = x1 − x2, R1 = Q[y2] and B1 = Q[y] ⊗Q[y2] Q[y]. We take
the Hochschild homology of each term, and the resulting comp lex splits into
the direct sum of two complexes of graded R-modules (for HH 0 and HH 1).
The complex of Hochschild homologies of zero degree is
0 − →R{2n}
2y
− →R{2n − 2}
0
− →R{2n − 4}
2y
− →R{2n − 6}
0
− →. . . .
It has cohomology Q in bidegrees (2 n − 2, 1), (2n − 6, 3), . . . ,(0, n), where
the ﬁrst grading corresponds to the degrees of variables xi and the second is
cohomological.
The Hochschild homology complex of degree one is
0 − →R{2n+2}
1
− →R{2n+2}
0
− →R{2n}
2y
− →R{2n−2}
0
− →R{2n−4}
2y
− →. . . .
It has cohomology Q in bidegrees (2 n − 2, 3), (2n − 6, 5), . . . ,(4, n).
Hence, for the (2 , n)-torus knot L, homology HHH( L) has rank n, as
previously computed by Rasmussen (private communication) . It was pre-
dicted in [GSV], [DGR] that the suitable HOMFLYPT homology g roups of
the (2 , n) torus knot have rank n. If H ∼= HHH is isomorphic to the theory
conjectured to exist in [GSV] and [DGR], one would have an int eresting link
between perverse sheaves on ﬂag varieties and the Gromov-Wi tten theory on
the total space of the O(−1) ⊕ O(−1) bundle over P1.
The approach to computing HHH( σ) via bimodules becomes signiﬁcantly
more challenging already for m = 3 . With six indecomposable bimodules
Bw the endomorphism algebra End Re( ⊕
w∈S3
Bw) looks quite complicated. If
we don’t exclude trivial cases and use various symmetries, d escribing the
multiplication
Hom(Bw, By) ⊗ Hom(By, Bz) − →Hom(Bw, Bz)
16
directly requires dealing with 6 3 = 216 possibilities for w, y, z ∈ S3. Also,
knowing the endomorphism algebra is only the ﬁrst (and not th e most dif-
ﬁcult) step in the algorithm. It’s almost certain that descr ibing H(σ) via
the limit N → ∞ of SL(N) link homologies, as suggested by Gornik, Rass-
mussen and [DGR], together with Rasmussen’s methods [Ra] fo r computing
the latter, will get the job done much faster.
Acknowledgements: This paper is a write-up of the talk the author
gave at the knot homology conference at UQAM in Montreal in Se ptember,
2005. I am grateful to Olivier Collin for organizing the conf erence and giving
me an opportunity to present the above observations. Severa l ideas implicit
or explicit in this paper (setting a of [KR2] to 0 , passing from the Koszul
complex of a wide edge to its zeroth cohomology) had been inde pendently
suggested by Jacob Rasmussen. Theorem 1 clariﬁes Maxim Vybo rnov’s con-
jecture [V] that the link homology of [KR2] should be related to the category
O and perverse sheaves on the ﬂag variety. We were also inﬂuenc ed by
Jozef Przytycki’s comparison of the Hochschild homology of truncated poly-
nomial algebras and the link homology of (2 , n)-torus knots [P]. The author
would like to thank Charles Frohman, Sergei Gukov, Lev Rozan sky and Ilya
Shapiro for useful discussions. Partial support came from t he NSF grant
DMS-0407784.
