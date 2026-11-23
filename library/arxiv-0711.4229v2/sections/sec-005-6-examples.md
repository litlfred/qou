---
doc_id: arxiv-0711.4229v2
doc_title: "MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS"
section_id: sec-005-6-examples
section_title: "Examples"
section_number: 6
pages: 11-15
source_pdf: 0711.4229v2.pdf
source_sha256: 2e6cc61069016627
toc_source: outline
doc_brief: "MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS — In this paper we give a re-normalization of the Reshetikhin-Turaev quantum invariants of links, by modiﬁed quantum dimensions."
---
We give three classes of examples of ambidextrous objects and associated re-normalized link
invariants.
6.1. Link invariants from Lie algebras. Let g be a simple Lie algebra and let Uq(g) be the
Drinfeld-Jimbo C(q)-algebra associated to g (see [9], XI.6). (Note here q is not a root of unity.)
Let C be the category of ﬁnite dimensional Uq(g)-modules. It is well known that C is a ribbon
Ab-category with ground ring K = C(q). Here F = K and trC (resp. dimC) is the quantum
trace (resp. quantum dimension).
Lemma 22. All simple objects of C are ambidextrous.
Proof. This follows from Lemma 1, as dimC(J)̸ = 0 for any simple object J of C.
□
Let I be the set of isomorphism classes of simple objects of C. One can show that S′(V, W)̸ = 0
for any V, W ∈I (for a similar calculation see [2], Proposition 2.2). Thus, A(J) = I for all
J ∈I. The construction of Section 3 derives from J and any non-zero d0 ∈F a function dJ and
an invariant F ′. Lemma 15 implies that F ′ is essentially independent of the choice of J.
Proposition 23. For any J ∈I and d0 = qdim(J), the J-determined quantum dimension dJ
is equal to the usual quantum dimension and F ′ is the usual Reshetikhin-Turaev quantum group
invariant arising from g.
Proof. This follow from Corollary 17.
□
6.2. Link invariants from Lie superalgebras. In [2, 3] the ﬁrst two authors derived new
link invariants from Lie superalgebras osp(2|2n) and sl(m|n) with m̸ = n. In particular, the
invariants associated with sl(m|1) generalize both the multivariable Alexander polynomial of
links and Kashaev’s link invariants. We explain here that the construction of [2, 3] is a special
case of the construction of Section 3.
In this subsection we work in the category of vector superspaces with even morphisms, i.e.,
the category whose objects are Z/2Z-graded vector spaces and the morphisms are even linear
maps. A Lie superalgebra g = sl(m|n) or g = osp(2|2n) gives rise to the quantized universal
enveloping C[[h]]-superalgebra Uh(g). Let C be the category of topologically free Uh(g)-modules
of ﬁnite rank (i.e., modules of the form V [[h]] where V is a ﬁnite dimensional g-module). It
is known that C is a ribbon Ab-category with ground ring K = C[[h]], see for instance [2] and
references there. The object V [[h]] of C is simple if and only if V is a simple g-module. The
ﬁnite dimensional simple g-modules are divided into two classes: typical and atypical. A simple
g-module is typical if each time it is a submodule or a factor-module of a ﬁnite dimensional
g-module, it splits as a direct summand. We call a Uh(g)-module V [[h]] (a)typical if V is a
(a)typical g-module.
Let I be the set of isomorphism classes of simple objects of C and let B be the subset of I
consisting of isomorphism classes of typical Uh(g)-modules.
Lemma 24. If V is an element of B, then dimC(V ) = 0. The link invariant F restricted to
LB is zero.
Proof. The ﬁrst statement follows from a direct calculation using the character formula of V
(see [2]). The second statement follows from Corollary 17.
□
12
NATHAN GEER, BERTRAND PATUREAU-MIRAND, AND VLADIMIR TURAEV
The following lemma is a restatement of Lemma 2.8 in [2].
Lemma 25. There exists an element J0 ∈B such that J0⊗J0 splits as a direct sum of elements
of B with multiplicity one. In particular, the algebra EndC(J0 ⊗J0) is commutative.
Corollary 26. The object J0 of C is ambidextrous.
Proof. Lemma 25 implies that the braiding cJ0,J0 commutes with all elements of EndC(J0 ⊗J0).
Thus, the corollary follows from Lemma 1.
□
In [2] the ﬁrst two authors have shown that S′(U, V )̸ = 0 for all U, V ∈B and S′(U, W) = 0
for all U ∈B, W ∈I −B. In other words, the set B is complete.
Proposition 27. Every element J ∈B is ambidextrous and A(J) = B. The construction in
Section 3 gives a function d = dJ : B →C[[h]][h−1] and an invariant F ′ = F ′
J, which do not
depend on J up to multiplication by a non-zero element of C[[h]][h−1].
Proof. Since B is complete and contains J the lemma follows from Lemma 15.
□
The link invariant introduced in [2] is deﬁned on LB. Its deﬁnition is similar to the one of F ′
above but uses a certain function d : B →C[[h]][h−1] rather than d. By Lemma 11, the function
d must be proportional to d and therefore the link invariant of [2] is equal to the invariant F ′
associated with an arbitrary J ∈B and an appropriate d0 (depending on J).
Remark 28. (1) In this example there is no canonical choice for J ∈B. However, for each J
there is a suitable choice of d0 (possibly, distinct from d0 = 1) such that dJ has a nice formula
(cf. [2]). This justiﬁes our choice to include the factor d0 in the deﬁnition of F ′.
(2) The extension of F ′ in Section 3 could be useful in computing F ′ for links colored with non
semisimple modules.
(3) It would be interesting to extend the constructions of this subsection to other Lie superalge-
bras.
6.3. Link invariants from Uq(sl(2)) at roots of unity. In this subsection we will consider
the generalized multivariable Alexander invariants deﬁned by Akutsu, Deguchi and Ohtsuki in
[1], which contain Kashaev’s invariants (see [4, 7]). These invariants are indexed by positive
integers. In [6], Jun Murakami gives a framed version of these invariants using the universal
R-matrix of Uq(sl(2)) and calls them the colored Alexander invariants. Here we show that these
invariants are restrictions of invariants deﬁned using ribbon categories as formulated above.
Fix a positive integer N and let q = e
π√−1
N
be a 2N-root of unity. We use the notation
qx = e
π√−1x
N
. Here we give a slightly generalized version of Uq(sl(2)). Let U H
q (sl(2)) be the
C(q)-algebra given by generators E, F, K, K−1, H and relations:
HK = KH,
HK−1 = K−1H,
[H, E] = 2E,
[H, F] = −2F,
KK−1 = K−1K = 1,
KEK−1 = q2E,
KFK−1 = q−2F,
[E, F] = K −K−1
q −q−1 .
The algebra U H
q (sl(2)) is a Hopf algebra where the coproduct, counit and antipode are deﬁned
by
∆(E) = 1 ⊗E + E ⊗K,
∆(F) = K−1 ⊗F + F ⊗1,
∆(H) = H ⊗1 + 1 ⊗H,
∆(K) = K ⊗K,
∆(K−1) = K−1 ⊗K−1,
ǫ(E) = ǫ(F) = ǫ(H) = 0,
ǫ(K) = ǫ(K−1) = 1,
S(E) = −EK−1,
S(F) = −KF,
S(K) = K−1.
MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS
13
Deﬁne ¯Uq(sl(2)) to be the Hopf algebra U H
q (sl(2)) modulo the relations EN = F N = 0.
We say a ¯Uq(sl(2))-module V is a weight module if V has a weight decomposition with respect
to H and if qH acts as K. Let C be the tensor Ab-category of ﬁnite dimensional weight ¯Uq(sl(2))-
modules (here the ground ring is C). We say a simple weight module is typical if its highest
weight is in the set (C\Z)∪{−1+kN : k ∈Z} otherwise we say it is atypical. A typical module
is N dimensional and indexed by its highest weight λ. We denote such a module by Vλ (for a
basis of this module see [6]). The weights of Vλ are λ −2i for 0 ≤i ≤N −1, so its character
formula is PN−1
i=0 uλ−2i where the coeﬃcient of ua is the dimension of the a-weight space.
We will now recall that the category C is a ribbon Ab-category. For a ∈C and n ∈N we set
{a} = qa −q−a and {n}! = {n}{n −1}...{1}. In [8] Ohtsuki deﬁnes an element Rt given by
Rt = qH⊗H/2
N−1
X
n=0
{1}2n
{n}! qn(n−1)/2En ⊗F n,
where qH⊗H/2 is a formal symbol. If v and v′ are two weight vectors of weights of λ and λ′ then
qH⊗H/2 acts on v ⊗v′ by
qH⊗H/2.(v ⊗v′) = qλλ′/2v ⊗v′.
Thus, the action of Rt on the tensor product of two objects of C is well deﬁned and induces an
endomorphism on such a tensor product. Moreover, Rt gives rise to a braiding cV,W : V ⊗W →
W ⊗V on C deﬁned by v ⊗w 7→τ(Rt(v ⊗w)) where τ is the permutation x ⊗y 7→y ⊗x (see
[6, 8]).
Remark 29. It is important that ¯Uq(sl(2)) contains H because the modules Vλ and Vλ+2N over
Uq(sl(2))/{EN = F N = 0} are isomorphic but the action of the R-matrix on V ⊗2
λ
and V ⊗2
λ+2N
are diﬀerent. These modules are distinct in C as H acts diﬀerently.
Let V and W be objects of C. Let {vi} be a basis of V and {v∗
i } be a dual basis of V ∗. Then
bV :C →V ⊗V ∗, given by 1 7→
X
vi ⊗v∗
i
dV :V ∗⊗V →C, given by f ⊗w 7→f(w)
are duality morphisms of C.
Also, in [8] Ohtsuki deﬁnes an element u given by
N−1
X
n=0
S(tn)q−H2/2sn
where Rt = qH⊗H/2 PN−1
n=0 sn ⊗tn and q−H/2 is a formal symbol whose action on a weight
vector vλ is given by q−H2/2.vλ = q−λ2/2vλ. Let θ = uKN−1 = KN−1u. The twist θV : V →V
is deﬁned by v 7→θ−1v (see [6, 8]).
If L is a link colored with objects of C such that one of the colors is typical then F(L) = 0
where as above F is the usual ribbon functor F : RibC →C. We will now show that the general
construction above gives rise to a non-trivial invariant F ′, which contains the ADO invariants
and so Kashaev’s invariants.
Fix a typical ¯Uq(sl(2))-module Vλ0 such that λ0 ∈C \ 1
2Z and denote it by J0.
Lemma 30. The tensor product J0 ⊗J0 splits as a direct sum of typical ¯Uq(sl(2))-modules with
no multiplicity. In particular, the algebra EndC(J0 ⊗J0) is commutative.
Proof. First, using the character formula for J0 one sees that all the weights of J0 ⊗J0 are not
integral. Then since typical modules always split we have that J0 ⊗J0 is a direct sum of typical
modules. The character formula for a typical module then implies that J0 ⊗J0 = ⊕N−1
i=0 V2λ0−2i,
which completes the proof.
□
14
NATHAN GEER, BERTRAND PATUREAU-MIRAND, AND VLADIMIR TURAEV
Corollary 31. The element J0 is ambidextrous.
Proof. The corollary follows directly from Lemma 1 and Lemma 30.
□
Next we will compute dimC(Vλ) and S′(Vλ, Vλ′). To do this we will need the morphisms
d′
V : V ⊗V ∗→C and b′
V : C →V ∗⊗V deﬁned by
d′
V = dV cV,V ∗(θV ⊗IdV ∗)
b′
V = (IdV ∗⊗θV )CV,V ∗bV .
A direct computation shows that
d′
V (v ⊗f) = f(K1−Nv)
b′
V (1) =
X
KN−1vi ⊗v∗
i .
Lemma 32. Let Vλ be typical ¯Uq(sl(2))-module then dimC(Vλ) = 0.
Proof. Let {vi} be a basis of Vλ such that vi is a non-zero vector of weight λ −2i. By deﬁnition
we have dimC(Vλ) = (d′
Vλ ◦bVλ)(1) which is equal to:
N−1
X
i=0
vi ⊗v∗
i =
N−1
X
i=0
v∗
i (K1−Nvi) =
N−1
X
i=0
q(N−1)(λ−2i) = q(N−1)λ 1 −q−2N
1 −q−2
where q−2N = 1 and so dimC(Vλ) = 0.
□
Lemma 33. Let Vλ be a typical module and let Vλ′ be any simple weight module with highest
weight λ′. We have
S′(Vλ, Vλ′) = q(λ+1−N)(λ′+1−N) {N(λ′ + 1 −N)}
{λ′ + 1 −N}
,
where {N(λ′+1−N)}
{λ′+1−N}
is a Laurent polynomial in qλ′.
Proof. The proof follows from a direct computations. A detailed presentation of an analogous
computation is given in Proposition 2.2 of [2].
□
Let I be the set of isomorphism classes of simple objects of C and let B be the subset of I
consisting of isomorphism classes of typical ¯Uq(sl(2))-modules.
Lemma 34. The usual invariant F restricted to LB is zero.
Proof. Follows from Corollary 17 and Lemma 32.
□
Let Vλ be in B then from Lemma 33 we have S′(Vλ, V )̸ = 0 for all V ∈B and S′(Vλ, W) = 0
for all W ∈I \ B. In other words, the set B is complete.
Proposition 35. Every element of J ∈B is ambidextrous and B = A(J). The construction in
Section 3 gives a function dJ : B →C and an invariant F ′
J, which do not depend on J up to
multiplication by a non-zero element of C.
Proof. Since B is complete and contains J then the lemma follows from Lemma 15.
□
Let d = dJ0 and F ′ = F ′
J0 be objects deﬁned in Section 3 arising from the ambidextrous
element J0 and the constant d0 = 1/(QN−2
j=0 {λ0 + N −j}). We will now compute d explicitly.
By a direct computation, for λ ∈C\Z one has
1
QN−2
j=0 {λ+N−j} = (−1)Nq−N(N+1)/2
{λ+1−N}
{N(λ+1−N)}.
Therefore, from the expression of S′ in Lemma 33 we have that
QN−2
j=0 {λ0 + N −j}S′(J, Vλ) = QN−2
j=0 {λ + N −j}S′(Vλ, J). Then by deﬁnition we have
d(Vλ) =
1
QN−2
j=0 {λ + N −j}
MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS
15
where we use the above choice of d0.
Next we will show that F ′ restricts to the colored Alexander invariant given by Jun Murakami
in [6]. The colored Alexander invariant is a reconstruction of the link invariants deﬁned in [1].
Murakami’s construction uses the universal R-matrix of Uq(sl(2)) and state sums. In particular,
let T be a (1,1)-tangle whose ith component is colored by a parameter λi (i = 1, ..., k) and the
ﬁrst component is the open component. Murakami deﬁnes ON
T (λ1, ..., λk) to be the element
of End(Vλ1) obtained by assigning the matrix elements of the R-matrix for the crossings of
T and particular scalars to the maximal and minimal points of T (these scalars are same as
the scalars coming from the morphisms bVλi, dVλi , b′
Vλi, d′
Vλi given above). Let ΦN
T (λ1, ..., λk) =
d(Vλ1)ON
T (λ1, ..., λk). Then in [6] Murakami shows that ΦN
T (λ1, ..., λk) is a framed version of
the analogous invariant deﬁned in [1].
Thus, ΦN
T (λ1, ..., λk) is a well deﬁned invariant of a
colored framed link L obtained by closing the tangle T ; denote this invariant by ΦN
L . Since the
construction of F ′ uses the same R-matrix, duality, twist and scaling d as the construction of
ΦN
L we have proved the following theorem.
Theorem 36. The invariant F ′ restricted to framed links colored with typical modules is equal
to the colored Alexander invariant ΦN
L .
