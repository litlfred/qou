---
doc_id: arxiv-math-0612592v1
doc_title: "Analytic q-difference equations Marius van der Put"
section_id: sec-000-document
section_title: "Document"
section_number: null
pages: 1-16
source_pdf: 0612592v1.pdf
source_sha256: a5d29fa15a0b74ff
doc_brief: "Analytic q-difference equations Marius van der Put — 1 sections: Document"
---
arXiv:math/0612592v1  [math.AC]  20 Dec 2006
Analytic q-diﬀerence equations
Marius van der Put
Department of Mathematics, University of Groningen, P.O.Box 800,
9700 A V Groningen, The Netherlands, mvdput@math.rug.nl
Introduction
A complex number q with 0 < |q| < 1 is ﬁxed. By an analytic q-diﬀerence
equation we mean an equation which can be represented by a matrix e quation
Y (z) = A(z)Y (qz) where A(z) is an invertible n × n-matrix with coeﬃcients
in the ﬁeld K = C({z}) of the convergent Laurent series and where Y (z)
is a vector of size n. The aim of this paper is to give an overview of our
present knowledge of these equations and their solutions. Deﬁnitio ns and
statements are presented in detail. Examples illustrate the main res ults.
For proofs we refer to the cited literature. For section 1 and part of the
following sections, the reference is [P-S]. For the later sections the reference
is [P-R]. The last section presents unpublished results. The theory o f linear
diﬀerential equations over K (see [P-S.2], especially Chapter 10) has many
of the features presented in this survey.
The manuscript [R-S] contains a concise overview of analytic q-diﬀerence
equations and its main purpose is to develop a theory of q-summation leading
to, in our terminology, a description of a universal diﬀerence Galois g roup.
As the authors of [R-S] note, this is only partially achieved and part o f their
work is still conjectural. However for a certain class of q-diﬀerence equations,
namely those having at most two slopes and such that the slopes are integral,
they have explicit results. An important part of the extensive litera ture on
q-diﬀerence equations can be found in the papers cited here.
1
1 Diﬀerence equations in general
A diﬀerence ﬁeld F is a ﬁeld provided with an automorphism φ of inﬁnite
order. A scalar linear diﬀerence equation is an equation of the form
φn(y) + an−1φn−1(y) + · · · + a1φ(y) + a0y = 0
with given ai ∈ F and, say, a0 ⁄= 0. As in the case of linear diﬀerential
equations, one can transform this equation into a matrix diﬀerence equation,
i.e., an equation of the form Y = Aφ(Y ), where A is a given invertible n × n-
matrix with coeﬃcients in F and Y denotes a vector of length n. On the
vector space M = F n one considers the operator Φ : Y ↦→Aφ(Y ). The
bijective map Φ : M → M is additive and Φ( f · m) = φ(f ) · Φ( m) for m ∈ M
and f ∈ F . This leads to the following deﬁnition of a diﬀerence module
M = (M, Φ) over F :
M is a ﬁnite dimensional vector space over F and Φ : M → M is an additive,
bijective map satisfying Φ( f · m) = φ(f ) · Φ( m) for m ∈ M and f ∈ F . The
equation, corresponding to a diﬀerence module is Y = Φ( Y ). In general this
equation has few solutions in M itself. Like ordinary polynomial equations
over ﬁelds, one has to construct extensions of F in order to have suﬃciently
many solutions.
We will now assume that F has characteristic zero and that its ﬁeld of
constants C := {f ∈ F | φ(f ) = f } is algebraically closed. A Picard-Vessiot
ring (or extension) R for a diﬀerence module M, say, represented by the
matrix equation Y = Aφ(Y ) is deﬁned by:
(i) R is an F -algebra (commutative and with a 1),
(ii) R is provided with an automorphism φ extending φ on F ,
(iii) R has only trivial φ-invariant ideals,
(iv) there exists an invertible matrix U (called fundamental matrix) with
coeﬃcients in R such that U = Aφ(U),
(v) R is generated over F by the coeﬃcients of U and 1
det U .
Property (iii) translates in terms of M into V := {a ∈ R⊗F M| Φ( a) = a}
is a vector space over C and the natural map R ⊗C V → R ⊗F M is an
isomorphisms.
One constructs R as follows. Let X denote a matrix ( Xi,j ) of indetermi-
nates and put D := det X. The F -algebra R0 := F [X, 1
D ] is provided with a
φ-action, extending the one on F , by the formula ( φXi,j ) = A−1(Xi,j ). Let
2
I ⊂ R0 denote an ideal maximal among the ideals invariant under φ. Then
R = R0/I is a Picard-Vessiot ring for the given equation.
The basic results of diﬀerence Galois theory are:
(1) A Picard-Vessiot ring R exists and is unique up to a, non unique, iso-
morphism.
(2) R is reduced (i.e., has no nilpotent elements).
(3) The set constants of the ring of total fractions of R is C.
(4) Let G be the group of the F -linear automorphism of R, commuting with
φ. The natural action of G on R ⊗F M induces a faithful action of G on V ,
the solution space. The image of G in GL( V ) is a linear algebraic subgroup
of the latter. This makes G into a linear algebraic group over C.
(5) The action of G on Spec(R) makes the latter into an G-torsor over F .
In other words, there exists a ﬁnite extension F + ⊃ F and a G-equivariant
isomorphism F +⊗C C[G] → F +⊗F R, where C[G] is the coordinate ring of G.
Most of the notions and ‘operations of linear algebra’, such as mor-
phisms, kernels, cokernels, direct sums have an obvious equivalent for diﬀer-
ence modules. Let ( M1, Φ 1), (M2, Φ 2) denote two diﬀerence modules. The
tensor product of the two modules is deﬁned as M1 ⊗F M2 with Φ given
by Φ( m1 ⊗ m2) = (Φ 1m1) ⊗ (Φ 2m2). The internal hom of the two mod-
ules is Hom F (M1, M2) with Φ deﬁned by (Φ( L))(m1) = Φ −1
2 (L(Φ 1m1)) for
L ∈ HomF (M1, M2) and m1 ∈ M1.
This leads to another, more abstract but very useful, formulation of the
above Picard-Vessiot theory, namely that of (neutral) Tannakian categories.
The category of all diﬀerence modules over F is a neutral Tannakian category.
We will return to this in section 6. For a speciﬁc diﬀerence ﬁeld F one can
say much more than the above formalism (analogous to the case of o rdinary
Galois theory for speciﬁc ﬁelds).
2 First examples of q-diﬀerence equations
This exposition is concerned with the diﬀerence ﬁeld K = C({z}), i.e., the
ﬁeld of convergent Laurent series over C, provided with the automorphism
φ given by φ(z) = qz, where q is a ﬁxed complex number satisfying 0 <
|q| < 1. In order to deﬁne φ on the algebraic closure K∞ = ∪n≥1Kn, with
Kn := C({z1/n }), of K we choose a τ ∈ C with ℑ(τ ) > 0 such that q = e2πiτ .
Deﬁne qλ for λ ∈ Q (or any λ ∈ C) as e2πiλτ . Then the action of φ on K∞
3
is given by φ(zλ ) = qλ zλ . The action of φ on ˆK = C((z)), i.e., the ﬁeld of
the formal Laurent series, and on its algebraic closure ˆK∞ = ∪n≥1 ˆKn, with
ˆKn := C((z1/n )), is deﬁned in a similar way.
Some q-diﬀerence rings F = ( F, φ) will be considered, namely C[z, z−1]
and O, the ring of the holomorphic functions on C∗. A diﬀerence module
M = (M, Φ) over a q-diﬀerence ring F will be a free F -module of ﬁnite rank
provided with a bijective additive map Φ : M → M such that Φ( f · m) =
φ(f ) · Φ( m) for f ∈ F, m ∈ M.
Examples 2.1
(a) Ke, Φ( e) = ce, c ∈ C∗. There exists a solution ( ⁄= 0) in K ⇔ c ∈ qZ.
Indeed, Φ( zte) = cqtzte. If c ∈ qZ, then the Picard-Vessiot ring is K itself
and the diﬀerence Galois group is {1}.
There exists a solution ( ⁄= 0) in Kn ⇔ c ∈ q
1
n Z. If c ∈ q
1
n Z with n
minimal, then Kn is the Picard-Vessiot ring and the diﬀerence Galois group
is µn := {a ∈ C| an = 1}.
In the remaining case, the Picard-Vessiot ring is K[X, X −1] with the
action of φ given by φ(X) = c−1X. The diﬀerence Galois group is Gm := C∗.
It consists of the automorphisms σ given by σ(X) = aX (for any a ∈ C∗).
We will use the symbol e(c) for this X. It can be given an interpretation as
multivalued function zb for a b with qb = c−1.
(b) The diﬀerence module Un := Ke 1 + · · ·+ Ke n with Φ given by the matrix


1 1
1 1
1
1


is called unipotent of length n. The Picard-Vessiot ring is K[X], with
φ(X) = X + 1. The diﬀerence Galois group is Ga := C. The elements σ of
this group have the form σ(X) = X + a (any a ∈ C). We will use the symbol
ℓ for this X. It has an interpretation as multivalued function log z
2πiτ . For n = 2
one easily veriﬁes that the solution space has C-basis {e1 − ℓe2, e 2}. ✷
A diﬀerence module M over K is called regular singular if M has a basis
e1, . . . , em such that C{z}e1 + · · · + C{z}em is invariant under Φ and Φ −1.
Theorem 2.2 The following are equivalent
(i) M regular singular.
4
(ii) M = K ⊗C W , dimC W < ∞ and Φ( f ⊗ w) = φ(f ) ⊗ A(w) for some
A ∈ GL(W ). Moreover, there is a unique A such that every eigenvalue c
satisﬁes |q| < |c| ≤ 1.
(iii) M is obtained by ⊕, ⊗ from the examples in 2.1.
The diﬀerence module ( Ke, Φ e = ( −z)e) is the basic example of an ir-
regular singular diﬀerence module. Its Picard-Vessiot ring is K[X, X −1] with
φ(X) = ( −z)−1X. The diﬀerence Galois group is Gm. We will use the sym-
bol e(−z) for this X. It has the interpretation Θ( z) := ∑
n∈Z qn(n−1)/ 2(−z)n
because of the well known formula ( −z)Θ( qz) = Θ( z).
3 Towards a classiﬁcation of modules
We present here the ‘classics’ by G.D. Birkhof, P.E. Guenther, C.R. A dams
et al. and ‘modern’ work by J.-P. Ramis, Ch. Zhang, J. Sauloy, A. Duv al,
M.F. Singer, M. van der Put, M. Reversat et al., concerning q-diﬀerence
equations over K.
Let K[Φ , Φ −1] be the skew ring of diﬀerence operators. The elements
of this ring are the ﬁnite formal sums ∑
n∈Z anΦ n and the multiplication is
given by the rule Φ · f = φ(f )Φ. This ring is (left and right) Euclidean. Any
diﬀerence module ( M, Φ M ) can be seen as a left K[Φ , Φ −1]-module where
the action of Φ on M is just Φ M . This left module is cyclic (i.e., generated
by one element) and therefore M ∼= K[Φ , Φ −1]/K[Φ , Φ −1]L for some L =
Φ m + am−1Φ m−1 + · · · + a1Φ + a0 with a0 ⁄= 0.
The usual discrete valuation v on K is given by v(0) = + ∞ and for
a ∈ K ∗, v(a) is the order of a. Using the values v(ai) one deﬁnes the Newton
polygon of L, as in the case of an ordinary polynomial in K[T ]. This Newton
polygon depends on M only. The slopes of the Newton polygon are in Q. A
diﬀerence module M is called pure if there is only one slope.
Examples 3.1 M is regular singular if and only if M is pure of slope 0.
Further (Ke, Φ e = c(−z)te) with c ∈ C∗, t ∈ Z is pure of slope t. ✷
Theorem 3.2 (Adams, Birkhoﬀ, Guenther, Ramis, Sauloy)
M has a unique tower of submodules 0 = M0 ⊂ M1 ⊂ · · · ⊂ Mr = M such
that every Mi/Mi−1 is pure of slope λi and λ1 < · · · < λ r.
5
This ﬁltration is called the slope ﬁltration of M and one deﬁnes the graded
module gr(M) of M by gr(M) = ⊕iMi/Mi−1. In proving Theorem 3.2, one
observes that the above operator L has a unique factorization L1 · L2 · · · Lr
with each Li ∈ ˆK[Φ , Φ −1] monic and having only one slope λi. The main step
is to show that these Li are actually convergent, i.e., belong to K[Φ , Φ −1].
This factorization of L induces the slope ﬁltration.
We note that for obtaining convergence, it is essential that λ1 < · · · < λ r.
For any order of the slopes λi there is a similar factorization of L in the ring
ˆK[Φ , Φ −1]. This has as consequence that ˆK ⊗K M is in fact equal to the direct
sum ⊕i( ˆK ⊗K Mi/Mi−1) = ˆK ⊗K gr(M). In the next section we will study
the moduli spaces that describe the modules M with a ﬁxed graded module
gr(M). A diﬀerence module M over K is called split if it is isomorphic to
its graded module gr(M). Here we continue with the classiﬁcation of pure
modules over K. We note that by Theorem 3.2 any irreducible module over
K is pure.
Deﬁnition 3.3 The module E(czt/n ).
Given are the data t/n, n ≥ 1, (t, n) = 1 , c ∈ C∗, |q|1/n < |c| ≤ 1. They
deﬁne a diﬀerence module over Kn of dimension 1, namely ( Kne, Φ e =
czt/n e). This object, considered as diﬀerence module over K, has dimension
n over K and is called E(czt/n ). ✷
Theorem 3.4 E(czt/n ) is pure, irreducible and has slope t/n. Further,
E(c1zt/n ) ∼= E(c2zt/n ) if and only if cn
1 = cn
2 . Moreover, every irreducible
M over K is isomorphic to some E(czt/n ).
A diﬀerence module is called indecomposable if it is not the direct sum
of two proper submodules. We note that an indecomposable module o ver K
need not be pure.
Theorem 3.5 The indecomposable pure modules over K are E(czt/n ) ⊗ Um
with |q|1/n < |c| ≤ 1. Further, the triple (t/n, cn, m) is unique.
Deﬁnition 3.6 Global lattices.
A global lattice Λ for a q-diﬀerence module M over K is a ﬁnitely generated
C[z, z−1]-submodule of M (and hence free), invariant under Φ and Φ −1, such
that the natural map K ⊗C[z,z −1] Λ → M is an isomorphism. ✷
6
We will see later that any diﬀerence module M has a unique global lat-
tice. This means that the q-diﬀerence equation, deﬁned locally at z = 0, is
equivalent to an equation on all of P1 with at most poles at z = 0 and z = ∞.
From the explicit description of the indecomposable pure modules ove r K it
is not hard to deduce the following.
Corollary 3.7 Every pure indecomposable diﬀerence module M over K has
a unique global lattice. This lattice, denoted by Mglobal, is a diﬀerence module
over C[z, z−1]. The same holds for split diﬀerence modules over K.
Moreover, any morphism f : M → N between split diﬀerence modules over
K maps Mglobal into Nglobal.
Before going on, we remark that the classiﬁcation of the diﬀerence mod-
ules over ˆK is remarkably simple. With the same methods used in the proof
of Theorem 3.5, one shows that every pure indecomposable diﬀeren ce module
over ˆK has the form ˆK ⊗K (E(czt/n ) ⊗ Um) (again with unique ( t/n, cn, m)).
Finally, as remarked before, any diﬀerence module over ˆK is a direct sum of
pure modules over ˆK.
It is well known that the elliptic curve Eq := C∗/qZ, which we like to call
the Tate curve , plays an important role for q-diﬀerence equations. With the
help of 3.5, 3.6 and 3.7 one can deduce the following rather striking res ult.
Theorem 3.8 There is an additive, faithful functor V from the category of
the split diﬀerence modules over K to the category of the vector bundles on
Eq. It has the properties:
(i) V induces a bijection between the (isomorphy classes of ) inde composable
modules over K and the (isomorphy classes of ) indecomposable vector bun-
dles on Eq.
(ii) V induces a bijection between (isomorphy classes of ) objects .
(iii) V respects the constructions of linear algebra, i.e., tensor products, ex-
terior powers etc.
Proof. We will sketch a proof.
(1). We recall that O denotes the algebra of the holomorphic functions on
C∗ and that a diﬀerence module M over O is a left module over the ring
O[Φ , Φ −1], free of some rank m < ∞ over O. Further pr : C∗ → Eq := C∗/qZ
denotes the canonical map. One associates to M the vector bundle v(M) of
7
rank m on Eq given by v(M)(U) = {f ∈ O(pr−1U) ⊗O M| Φ( f ) = f }, where,
for any open W ⊂ C∗, O(W ) is the algebra of the holomorphic functions on
W .
On the other hand, let a vector bundle M of rank m on Eq be given.
Then N := pr∗M is a vector bundle on C∗ provided with a natural isomor-
phism σ∗
q N → N , where σq is the map σq(z) = qz. One knows that N is
in fact a free vector bundle of rank m on C∗. Therefore, M, the collection
of the global sections of N , is a free O-module of rank m provided with an
invertible action Φ satisfying Φ( f m) = φ(f )Φ( m) for f ∈ O and m ∈ M. It
is easily veriﬁed that the above describes an equivalence v of tensor categories.
(2). One associates to any split diﬀerence module M over K, its global lat-
tice Mglobal and the q-diﬀerence module O ⊗C[z,z −1] Mglobal over O. The latter
induces by (1) a vector bundle on Eq, which we call V (M). For a morphism
f : M → N between split modules one has f : Mglobal → Nglobal.Therefore
f induces a morphism V (f ) : V (M) → V (N). Thus we found the additive,
faithful functor V . Clearly V respects the constructions of linear algebra.
(3). As (ii) is an immediate consequence of (i), we are left with proving
(i). The indecomposable module M := E(czt/n ) ⊗ Um is producing a vector
bundle V (M) of rank nm and degree tm. One can show that V (M) is
indecomposable and that V (M) is irreducible if m = 1. Further one can
verify that non isomorphic indecomposable M, N produce non isomorphism
vector bundles V (M), V (N). It is somewhat more complicated to show that
every indecomposable vector bundle is isomorphic to V (M) for a suitable
indecomposable M. This last step can be avoided by an inspection of Atiyah’s
paper where the classiﬁcation of the indecomposable vector bundle s on Eq is
explicitly given. ✷
Corollary 3.9 Let B be a split module over K, then
(i) ker(Φ − 1, O ⊗ Bglobal) ∼= H 0(Eq, V (B)).
(ii) coker(Φ − 1, O ⊗ Bglobal) ∼= H 1(Eq, V (B)).
(iii) The two canonical maps coker(Φ − 1, Bglobal) → coker(Φ − 1, B) and
coker(Φ − 1, Bglobal) → coker(Φ − 1, O ⊗ Bglobal) are isomorphisms.
Examples 3.10 Consider the diﬀerence module ( B = Ke, Φ e = ( −z)te)
with t ∈ Z. The line bundle V (B) is equal to OEq(t · [1]), where 1 denotes
the neutral element of Eq.
8
For t ≥ 1, coker(Φ − 1, O ⊗ Bglobal) = 0 and ker(Φ − 1, O ⊗ Bglobal) is the
t-dimensional vector space with basis {Θ( ζz )te|ζ t = 1}.
For t = 0, ker(Φ − 1, O) = C1 and coker(Φ − 1, O) has dimension 1.
Explicitly, O is the vector space of the everywhere convergent Laurent serie s
and has the formula (Φ − 1)(∑
n∈Z anzn) = ∑
n∈Z(qn − 1)anzn. ✷
4 Moduli spaces for diﬀerence modules
Fix a split diﬀerence module S = P1 ⊕ · · · ⊕ Pr over K, where Pi is pure
with slope λi and λ1 < · · · < λ r. The problem is to classify the diﬀerence
modules M over K such that gr(M) is isomorphic to S. The collection of
the isomorphy classes is a rather ugly object due to the fact that S has many
automorphisms.
A better way to formulate the problem is to consider pairs ( M, f ) con-
sisting of a diﬀerence module M and an isomorphism f : gr(M) → S. Two
pairs ( M1, f1), (M2, f2) are called equivalent if there exists an isomorphism
g : M1 → M2 such that the induced graded isomorphism gr(g) : gr(M1) →
gr(M2) has the property f1 = f2 ◦ gr(g). Let Equiv (S) denote the set of
equivalence classes.
This formulation allows us to deﬁne a covariant functor F from the cate-
gory of ﬁnitely generated C-algebras R (i.e., R is commutative and has a 1)
to the category of sets. For a ﬁnitely generated C-algebra R one considers
KR := R ⊗C K and one can deﬁne the notion of diﬀerence module over KR.
The set F (R) is the set of equivalence classes of pairs ( M, f ) with M a dif-
ference module over KR and f is a KR-isomorphism f : gr(M) → KR ⊗ S.
Equivalence of two pairs is deﬁned as above. We note that F (C) is precisely
Equiv (S).
One can see the functor F as a contravariant functor on the category of
aﬃne C-schemes (of ﬁnite type).
Theorem 4.1 The contravariant functor F on aﬃne C-schemes is repre-
sentable. In fact, the aﬃne space AN
C with N = ∑
i<j(λj − λi) dim Pi · dim Pj,
represents F . In other words, the covariant functor F is represented by a cer-
tain universal q-diﬀerence module M over C[X1, . . . , XN ]. Further Equiv (S)
identiﬁes with CN .
For the case of integer slopes λi, the above result is announced by J.-P. Ramis
and J. Sauloy. The general case is treated in [P-R].
9
One can normalize the representing space AN
C by letting 0 correspond to
the class of the pair ( S, idS). The vector space structure of AN
C has an inter-
pretation for s = 2, namely as the vector space coker(Φ − 1, Hom(P2, P1)).
For s > 2, the functor F and its representing space still have a weaker
structure, namely that of an iterated torsor.
We illustrate Theorem 4.1 by the following basic example :
S = P1 ⊕ P2, where P1 = ( Ke 1, Φ e1 = e1) and P2 = ( Ke 2, Φ e2 = ( −z)te2)
with t > 0. The moduli space is At
C and the universal family above this
moduli space is
K[x0, . . . , xt−1]e1 + K[x0, . . . , xt−1]e2, Φ e1 = e1,
Φ e2 = (−z)te2 + (x0 + x1z + · · · + xt−1zt−1)e1 .
Surprisingly enough, Theorem 4.1 (for the case of integer slopes) a nd this
example are already present in the work of Birkhoﬀ of Guenther.
Corollary 4.2 Every diﬀerence module M over K has a unique global lat-
tice. This lattice will be called, as before, Mglobal. Moreover, every morphism
f : M → N satisﬁes f (Mglobal) ⊂ Nglobal. In particular, one can extend the
functor V of Theorem 3.8 to the category of all q-diﬀerence modules over K.
This corollary can be deduced from the Theorem 4.1 and Corollary 3.9.
5 Diﬀerence Galois groups
In the last section a complete, however complicated, classiﬁcation o f the dif-
ference modules over K is given. Using this classiﬁcation we will be able to
give a complete description of the diﬀerence Galois groups. The diﬀer ence
Galois group of a module M will be denoted by Gal(M).We start with the
easiest case and build up to the general case.
(1) Regular singular modules .
We recall that a regular singular module has the form M = K ⊗C W and
Φ( f ⊗ w) = φ(f ) ⊗ A(w) with A ∈ GL(W ). We normalize A such that the
eigenvalues of A have absolute values in ( |q|, 1] ⊂ R. Let L ⊂ C∗/qZ = Eq
be the group generated by the images of the eigenvalues of A. Then:
Gal(M) = Hom( L, C∗) (×C).
10
Write L = Lf ree ⊕ Ltorsion with the ﬁrst summand a free Z-module of rank
g ≥ 0 and where the second term is a ﬁnite commutative group. Then
Hom(L, C∗) is a product of Gg
m with a ﬁnite commutative group generated
by at most two elements. If A is semi-simple, then this is Gal(M). If A is
not semi-simple, then the term Ga = C is also present.
(2) Irreducible modules.
We recall that M = E(czt/n ). For n = 1 and t ⁄= 0, the group Gal(M)
is Gm = C∗. For n > 1 one can describe Gal(M) be an exact sequence
1 → Gm → Gal(M) → (Z/nZ)2 → 0. The group Gal(M) is not commuta-
tive and is not a semi-direct product of Gm and ( Z/nZ)2.
(3) Indecomposable modules.
We may suppose M = E(czt/n ) ⊗ Um with t/n ⁄= 0 and m > 1. Then
Gal(M) = Gal(E(czt/n ) × Ga.
(4) Split modules .
A split module M is a direct sum of pure modules Mi. An explicit com-
bination of the diﬀerence Galois groups of the Mi (described above) yields
Gal(M).
(5) The general case .
We recall that M has a slope ﬁltration 0 = M0 ⊂ M1 ⊂ · · · ⊂ Mr = M
with Pi := Mi/Mi−1 pure and gr(M) = S := P1 ⊕ · · · ⊕ Pr. Let ξ in the
moduli space, introduced in section 4, represent M. Then there exists an
exact sequence
1 → Uξ → Gal(M) → Gal(S) → 1 ,
with Uξ a unipotent group, explicitly determined by ξ. This sequence is in
fact a semi-direct product and the action, by conjugation, of Gal(S) on U is
again explicit.
Remarks 5.1
(1) The above description of Gal(M) implies that Gal(M)o is a solvable
group. This is in contrast with the diﬀerential Galois groups that occ ur for
diﬀerential equations over K.
(2) Diﬀerence modules over ˆK. For a diﬀerence module N over ˆK, there
11
exists a unique split diﬀerence module M over K such that N ∼= ˆK ⊗K M.
Further, N and M have the same diﬀerence Galois group.
(3) Let M be a diﬀerence module over K. The step from M to its global
lattice Mglobal is probably not algorithmic since it involves a computation
with arbitrary complex numbers. However, the classiﬁcation in sect ions 3
and 4, assuming the knowledge of Mglobal, is algebraic and can be shown to
be algorithmic. The computation of Gal(M) (and of the Picard-Vessiot ring
for M), on the basis of the classiﬁcation, is algorithmic as well.
We note that for linear diﬀerential equations over K, the existence of a
theoretical algorithm is proven by E. Hrushovski (2001). In that case no
explicit algorithm is known. ✷
6 Universal Picard-Vessiot rings and
universal diﬀerence Galois groups
We start by explaining some notions and constructions (see also [P-S 2]).
An aﬃne group scheme G over C is given by a C-algebra A provided with
the structure of a Hopf-algebra. The latter is deﬁned by a triple ( m, e, i) of
C-algebra morphisms:
(a) m : A → A ⊗C A (the co-multiplication)
(b) e : A → C with e(1) = 1 (the co-unit element),
(c) i : A → A is an isomorphism (the co-inverse).
Put G := Spec(A). The induced map m∗ : G × G → G is the multiplication,
further e∗ : Spec(C) → G is the unit element of G and the induced map
i∗ : G → G is the map g ↦→g−1. The usual rules for a group, expressed
in m∗, e∗, i∗, are translated into rules for m, e, i. These rules deﬁne a Hopf-
algebra.
If A is ﬁnitely generated over C, then G is an ordinary linear algebraic
group over C. In general, A is the direct limit (in fact a ﬁltered union) of
ﬁnitely generated sub-Hopf-algebras. This means that G is the projective
limit of linear algebraic groups.
A representation of an aﬃne group scheme G over C is a morphism of
aﬃne group schemes G → GL(W ), where W is a ﬁnite dimensional vector
space over C. Morphisms between representations are deﬁned in the obvious
way and thus we can talk about the category ReprG of all representations of
G. In this category one can perform all ‘constructions of linear algeb ra’, e.g.,
12
kernels, co-kernels, direct sums, tensor products, duals, and t he rules that one
knows from linear algebra are valid. We note that an equivalence betw een
ReprG1 and ReprG2, preserving the constructions of linear algebra, comes
from an isomorphism G1 → G2 of aﬃne group schemes (this is Tannaka’s
theorem).
We adopt here the following rather trivial deﬁnition of neutral Tannakian
category, namely it is a category T having all constructions and rules of lin-
ear algebra and is, for these structures, equivalent to ReprG for a suitable
aﬃne group scheme G. Of course there is an intrinsic deﬁnition of neutral
Tannakian category. Using that, one can show that ∆ K, the category of
all diﬀerential modules over K, is a Tannakian category. The aﬃne group
scheme G such that ∆ K is isomorphic to ReprG, is called the universal dif-
ference Galois group for the category ∆ K. It is this group that we want to
describe.
A full subcategory ∆ of ∆ K (i.e., for any objects A, B of ∆, one has
Hom∆ (A, B) = Hom ∆ K (A, B) ), closed under the operations of linear algebra,
is again a neutral Tannakian category.
Consider an object M of ∆ K. Write {{M}} for the full subcategory of
∆ K generated by M and all constructions of linear algebra applied to M.
Then {{M}} is isomorphic to some ReprH. Moreover, there is a Picard-
Vessiot ring P V R(M) attached to M. It is a general result that H can be
identiﬁed with the linear algebraic group consisting of the K-automorphisms
of P V R(M) that commute with φ. In other words, H can be identiﬁed with
the diﬀerence Galois group of M.
The above holds for any full subcategory ∆ of ∆ K, closed under the
operations of linear algebra. There is a Picard-Vessiot ring P V R(∆) for ∆,
namely the direct limit of the P V R(M) for all objects of ∆. Moreover the
aﬃne group scheme H, such that ReprH is equivalent to ∆, identiﬁes with
the group of the K-linear automorphism of P V R(∆), commuting with φ.
An explicit description of the universal Picard-Vessiot ring for ∆ K is what
we are aiming to produce.
We build up a description of the universal Picard-Vessiot ring and the
universal Galois group of ∆ K, by considering suitable subcategories of ∆ K.
(1) ∆ rs, the category of the regular singular diﬀerence modules ove r K.
P V R(∆ rs) = K[{e(c)}c∈C∗, ℓ] with rules:
e(c1c2) = e(c1) · e(c2), e (q) = z−1 and φ(e(c)) = c−1e(c), φ (ℓ) = 1 + ℓ
13
One identiﬁes zλ = e(q−λ ) for λ ∈ Q and thus P V R(∆ rs) contains the alge-
braic closure K∞ of K. We can therefore rewrite P V R(∆ rs) as K∞[{e(c)}, ℓ]
with the additional relations zλ = e(q−λ ) for all λ ∈ Q. Further, the diﬀer-
ence Galois group Grs is Hom( C∗/qZ, C∗) × C.
A similar description holds for regular diﬀerence modules over ˆK. Let ˆK∞
denote the algebraic closure of ˆK. Then the universal Picard-Vessiot ring
is ˆK[{e(c)}, ℓ] and the universal diﬀerence Galois group coincides with the
above group Grs.
Comments. This description follows from the observation that P V R(∆ rs)
is generated by the solutions for the modules in Examples 2.1. The give n
expression for Grs has to be interpreted as an aﬃne group scheme. The de-
scription follows from section 5, part (1).
(2) ∆ split, the category of the split diﬀerence modules over K.
P V R(∆ split) = K∞[{e(c)}c∈C∗, ℓ, {e(zλ )}λ ∈Q]
with additional rules e(zλ +µ ) = e(zλ ) · e(zµ ), φ (e(zλ )) = z−λ · e(zλ ).
Let the corresponding universal diﬀerence Galois group be denote d by Gsplit.
From the inclusion ∆ rs ⊂ ∆ split one obtains an exact sequence of aﬃne group
schemes
1 → Hom(Q, C∗) → Gsplit → Grs → 1 .
The group scheme Gsplit is not a semi-direct product and Hom( Q, C∗) lies in
the center of Gsplit.
Comments. The new universal Picard-Vessiot ring is generated over the one
of (1) by solutions for the modules E(czt/n ). This explains the terms e(zλ ).
The exact sequence and its features follow from an explicit calculatio n of the
automorphism of P V R(∆ split). We note the contrast with the diﬀerential
case! Finally, the descriptions for the universal Picard-Vessiot rin g and the
universal diﬀerence Galois group for ∆ bK, the category of all diﬀerence mod-
ules over ˆK, is rather similar.
(3) ∆ K, this is the most interesting and the most complicated case .
What can be proved at present is the following:
(a) P V R(∆ K) = D[{e(c)}, ℓ, {e(zλ )}] and the latter is a subalgebra of the
explicit universal Picard-Vessiot ring P V R(∆ bK) = ˆK∞[{e(c)}, ℓ, {e(zλ )}].
Further D is the K∞-subalgebra of ˆK∞ consisting of the elements f ∈ ˆK∞
14
satisfying a scalar q-diﬀerential equation over K∞.
(b) The K-algebra D is generated over K∞ by the solutions in ˆK∞ of all
equations of the form
(c1z−λ 1φ − 1)m1 · · ·(crz−λ r φ − 1)mr f = zµ ,
where 0 < λ 1 < · · · < λ r, r ≥ 1, m 1, . . . , mr ≥ 1, µ ∈ Q.
(c) The universal diﬀerence group G admits an exact sequence (in fact is a
canonical semi-direct product) 1 → N → G → Gsplit → 1 , where N is a
(connected) unipotent group scheme.
(d) The (pro)-Lie algebra Lie(N) of N consists of the K∞-linear derivations
D of P V R(∆ K) commuting with φ and zero on the elements e(c), ℓ, e(zλ ).
We note that any such D is determined by its restriction to D.
Remarks 6.1
(1) A standard example for (b) is f = ∑
n≥1 q−n(n+1)/ 2zn, the only solution
of ( z−1φ − 1)f = 1 in ˆK∞.
(2) In [R-S] it is suggested, in analogy with the diﬀerential case, tha t Lie(N)
is a nilpotent completion of a free Lie algebra with a set of free genera tors
derived from the analytic tool of q-summation. ✷
The main obstruction for the determination of Lie(N) is the absence of
an explicit description of the algebra D. Now we present an intermediate
Tannakian category ∆ 2,K . It is the Tannakian subcategory of ∆ K generated
by the diﬀerence modules having at most two slopes. For this catego ry
one has P V R(∆ 2,K ) = D2[{e(c)}, ℓ, {e(zλ )}] for a certain K∞-subalgebra
D2 ⊂ D ⊂ ˆK∞ and a universal diﬀerence Galois group G2 which is the semi-
direct product of Gsplit and a (connected) unipotent group scheme N2. The
latter is a quotient of N and the pro-Lie algebra Lie(N2) is a quotient of
Lie(N). Any D ∈ Lie(N2) is a K∞-linear derivation D : D2 → P V R(∆ 2,K ),
commuting with φ.
Deﬁnition 6.2 The elements fm,c,µ .
For µ ∈ Q with µ > 0, c ∈ C∗ with |qµ | < |c| ≤ 1 and m ≥ 1, the unique
solution in ˆK∞ of the equation ( c−1z−µ φ − 1)my = 1 is called fm,c,µ . ✷
Theorem 6.3 D2 is generated over K∞ by the elements fm,c,µ . These ele-
ments are algebraically independent over K∞.
15
We note that φ(fm,c,µ ) = czµ (fm,c,µ + fm−1,c,µ ), where we use the notation
f0,c,µ = 1 for all c, µ. Thus the action of φ on D2 is explicit. An element
D ∈ Lie(N2) is a K∞-derivation D2 → P V R(∆ 2,K ), commuting with φ.
Since the fm,c,µ are free generators of D2, the values D(fm,c,µ ) have the only
restriction that φ(D(fm,c,µ )) = czµ (D(fm,c,µ ) + D(fm−1,c,µ )).
Choose for every µ, c as above, a sequence of complex numbers
a0(µ, c), a1(µ, c), a2(µ, c), . . . . Deﬁne D by the formula D(fm,c,µ ) :=
(a0(µ, c)
( ℓ
m − 1
)
+a1(µ, c)
( ℓ
m − 2
)
+· · ·+am−1(µ, c)
( ℓ
0
)
)·e(c−1)e(z−µ ) .
One can verify that D commutes with the action of φ and thus D deﬁnes an
element of Lie(N2). Moreover, every element of Lie(N2) has this form.
One observes that Lie(N2) is commutative. Now we propose topological
generators for the pro-Lie algebra Lie(N2) by considering the elements Dµ,c,n
with µ > 0, |qµ | < |c| ≤ 1, n ≥ 0 deﬁned by the sequences {ak(µ′, c′)} with
ak(µ′, c′) = δµ,µ ′δc,c ′δk,n .
It is not diﬃcult to verify that any element ξ ∈ P V R(∆ 2,K ), invariant
under Gsplit and satisfying Dµ,c,n ξ = 0 for all µ, c, n , lies in K. This implies
that N2 is connected and that its pro-Lie-algebra is actually topologically
generated by {Dµ,c,n }. We conjecture that Lie(N2) is actually Lie(N)ab :=
Lie(N)/[Lie(N), Lie(N)].
In [R-S] a set of free topological generators for the pro-Lie-alge bra Lie(N)
is proposed. It seems that the restriction of this set to the quotie nt Lie(N2)
has a translation into our set {Dµ,c,n }.
References
[P-R] M. van der Put and M. Reversat - Galois theory of q-diﬀerence equa-
tions - Ann. Fac. Sci. de Toulouse, vol XVI, no 2, p. 1-54, 2007
[P-S] M. van der Put and M.F. Singer - Galois theory of diﬀerence equations
- Lecture Notes in Mathematics, 1666, Springer Verlag, 1997
[P-S.2] M. van der Put and M.F. Singer - Galois theory of linear diﬀerential
equations - Grundlehren der mathematische Wissenschaften, 328, Springer
Verlag, 2003
[R-S] J.-P. Ramis and J. Sauloy - The q-analogue of the wild fundamental
group (I) - arXiv:math.QA/0611521 v1 17 Nov 2006
16
