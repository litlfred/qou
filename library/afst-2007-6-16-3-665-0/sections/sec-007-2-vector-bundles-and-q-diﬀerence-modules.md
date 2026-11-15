---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-007-2-vector-bundles-and-q-diﬀerence-modules
section_title: "Vector bundles and q-diﬀerence modules"
section_number: 2
pages: 13-21
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
toc_source: inferred
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
We recall that O denotes the algebra of the holomorphic functions on
C∗and that a diﬀerence module M over O is a left module over the ring
O[Φ, Φ−1], free of some rank m < ∞over O. Further pr : C∗→Eq := C∗/qZ
denotes the canonical map. One associates to M the vector bundle v(M) of
rank m on Eq given by v(M)(U) = {f ∈O(pr−1U)⊗OM| Φ(f) = f}, where,
for any open V ⊂C∗, O(V ) is the algebra of the holomorphic functions on V .
On the other hand, let a vector bundle M of rank m on Eq be given. Then
N := pr∗M is a vector bundle on C∗provided with a natural isomorphism
σ∗
qN →N, where σq is the map σq(z) = qz. One knows that N is in
fact a free (or trivial) vector bundle of rank m on C∗(see [For], p. 204).
Therefore, M, the collection of the global sections of N, is a free O-module of
rank m provided with an invertible action Φ satisfying Φ(fm) = φ(f)Φ(m)
for f ∈O and m ∈M. It is easily veriﬁed that the above describes an
equivalence v of tensor categories.
The equivalence v extends to an equivalence between the left O[Φ, Φ−1]-
modules which are ﬁnitely generated as O-module and the coherent sheaves
– 676 –
Galois theory of q-diﬀerence equations
on Eq. This is an equivalence of Tannakian categories.
By an admissible diﬀerence module over O we will mean a left O[Φ, Φ−1]-
module which is a direct limit of left O[Φ, Φ−1]-modules of ﬁnite type over
O. The equivalence v extends to a Tannakian equivalence between category
of the admissible diﬀerence modules over O and the category of the quasi-
coherent sheaves on Eq.
Lemma 2.1. — There are isomorphisms ker(Φ−1, M) →H0(Eq, v(M))
and coker(Φ−1, M) →H1(Eq, v(M)) between these functors deﬁned on the
category of the admissible diﬀerence modules M over O.
Proof. — The isomorphism ker(Φ −1, M) →H0(Eq, v(M)) follows from
the deﬁnition of v. Let v−1 denote the ‘inverse’ of the functor v. Then M →
ker(Φ −1, v−1(M)) is canonically isomorphic to M →H0(Eq, M). One
observes that an exact sequence 0 →M1 →M2 →M3 →0 of admissible
diﬀerence modules over O induces (by the snake lemma) an exact sequence
0 →ker(Φ −1, M1) →ker(Φ −1, M2) →ker(Φ −1, M3) →
coker(Φ −1, M1) →coker(Φ −1, M2) →coker(Φ −1, M3) →0 .
From this it easily follows that the ﬁrst right derived functor of the functor
M →ker(Φ−1, M), on the category of admissible modules over O, is equal
to coker(Φ−1, M). Now the second isomorphism of functors follows.
□
Examples 2.2. — (1) Consider M = Oe with Φ(e) = e. Then v(M)
is the structure sheaf OEq of Eq. Any element in m ∈M can be written
uniquely as m = 
n∈Z anzne. Then (Φ −1)m = 
n∈Z(qn −1)anzne. One
observes that ker(Φ −1, M) = Ce and that coker(Φ −1, M) is represented
by Ce. This illustrates Lemma 2.1.
(2) Consider diﬀerence module M = Oe with Φe = ce and c ∈C∗, |q| <
|c| ⩽1. If c̸ = 1, then θce is a meromorphic section of v(M) with divisor
−pr(c−1) + pr(1). One concludes that v(M) ∼= OEq(pr(c−1) −pr(1)). Thus
one ﬁnds all line bundles of degree 0 on Eq in this way.
(3) Consider the diﬀerence module M := Oe with Φe = (−z)e. There is
a Φ-invariant element, namely Θe. This is a global section of v(M). The
cokernel of the morphism OEq →v(M), given by 1 →Θe, is a skyscraper
sheaf with support {1} and stalk C at that point. Indeed, the function Θ
has simple zeros at qZ. One concludes that v(M) ∼= OEq([1]). Using tensor
products one obtains that the line bundle v(M), with M = Oe, Φe = czte,
has degree t. Moreover every line bundle on Eq is obtained in this way.
– 677 –
Marius van der Put, Marc Reversat
(4) Let M = O/OΘ with the Φ-action induced by the usual one of O. Then
v(M) is the skyscraper sheaf on Eq with support {1} and with stalk C at
that point.
We recall that a split diﬀerence module M over K is a direct sum of pure
modules Mi. The global module Mglobal over C[z, z−1] associated to M is
by deﬁnition the direct sum of the global modules (Mi)global. A morphism
f : M →N between split modules is easily seen to be the direct sum of
morphisms between the pure components of M and N. In particular f maps
Mglobal to Nglobal.
One associates to a split diﬀerence module M the diﬀerence module
O⊗C[z,z−1]Mglobal and, by Lemma 2.1, a vector bundle on Eq. For notational
convenience we write again v(M) for this vector bundle. In this way we
obtain a functor v from the category of the split diﬀerence modules over K
to the category of vector bundles on Eq. One observes that Hom(M1, M2) →
Hom(v(M1), v(M2)) is C-linear and injective. Moreover, one easily sees that
v preserves tensor products.
Theorem 2.3. — The functor v from the category of the split diﬀerence
modules over K to the category of the vector bundles on Eq is bijective on
isomorphy classes of objects. This bijection respects tensor products.
Proof. — We have to show that v induces a bijection between the iso-
morphy classes of the indecomposable objects in the two categories. We
start by proving that for an indecomposable pure diﬀerence module M the
corresponding vector bundle v(M) is indecomposable.
From Examples 2.2 one concludes that v provides a bijection between
the isomorphy classes of the diﬀerence modules of dimension 1 over K and
the isomorphy classes of all line bundles on Eq.
By Corollary 1.6, an indecomposable pure diﬀerence module has the
form M = Res(E(czt/n)) ⊗Um, with unique n ⩾1, (t, n) = 1, m ⩾1 and
cn such that |q| < |cn| ⩽1. The vector bundle v(M) has clearly rank nm.
The exterior product ΛnmM is equal to Kf with Φf = sztmf for some
s ∈C∗. Thus v(M) has degree tm. The case nm = 1 has been treated above
and we suppose now nm > 1.
One can present Mglobal as C[z1/n, z−1/n]⊗W, with W a C-linear space
of dimension m and Φ given by Φ(1⊗w) = czt/n⊗U(w) where U is a unipo-
tent map with minimal polynomial (U −1)m = 0. Then O ⊗C[z,z−1] Mglobal
can be represented as Hn ⊗W, where Hn consists of the convergent Lau-
rent series in z1/n. Thus Hn consists of the expressions +∞
k=−∞akzk/n with
– 678 –
Galois theory of q-diﬀerence equations
lim|k|→∞|ak|1/|k| = 0. One provides W with some norm ∥∥. The elements
of Hn ⊗W have the form +∞
k=−∞zk/n ⊗wk with lim|k|→∞∥wk∥1/|k| = 0.
Then Φ acts on Hn ⊗W by
Φ(

zk/n ⊗wk) =

qk/nzk/nczt/n ⊗U(wk) .
Write Ψ = z−tΦn. Then
Ψ(

zk/n ⊗wk) =

zk/n ⊗dqkU n(wk), with d = cnqt(n−1)/2 .
For each k, the vector space zk/n⊗W is invariant under Ψ and this operator
has eigenvalues qkd on this vector space. One concludes from this that the
subset Mglobal ⊂Hn⊗W consists of the elements fe such that there exists a
non zero polynomial L ∈C[T] with L(Ψ)(fe) = 0. This has as consequence
that every O-linear endomorphism A of O⊗C[z,z−1]Mglobal, commuting with
Φ, is the O-linear extension of a unique C[z, z−1]-linear endomorphism B
of Mglobal commuting with Φ.
A direct sum decomposition of v(M) induces a O-linear endomorphism
A of O ⊗C[z,z−1] Mglobal commuting with Φ and such that A2 = A. The cor-
responding B induces a direct sum decomposition of Mglobal, contradicting
that M is indecomposable. Thus v(M) is indecomposable. A similar rea-
soning proves that for indecomposable M1, M2 the relation v(M1) ∼= v(M2)
implies that M1 ∼= M2. In this way we have found a collection of inde-
composable vector bundles on Eq. That we have found all of them follows
at once from the classiﬁcation given in [At], Theorem 10. Indeed, Atiyah
constructs a certain indecomposable vector bundle of rank r and degree d,
called EA(r, d). Let h = (r, d). Then every indecomposable vector bundle
of rank r and degree d has the form L ⊗EA(r, d) with L a line bundle of
degree 0. This L is unique up to multiplication with a line bundle N such
that N ⊗r/h is the trivial line bundle.
□
The ﬁnal part of the proof of Theorem 2.3 depends on [At]. We present
now a proof which only uses a simple result of this paper, namely Lemma
11, formulated as follows:
Let W be an indecomposable vector bundle of rank m and degree 0 on an
elliptic curve E, then W = L ⊗W ′, with L a line bundle of degree 0 and
such that the indecomposable W ′ has a sequence of subbundles 0 = W ′
0 ⊂
W ′
1 ⊂· · · ⊂W ′
m = W ′ such that each quotient W ′
i+1/W ′
i is isomorphic
to OE.
Proof. — V is an indecomposable vector bundle on Eq, rank nm and
degree tm with n, m ⩾1, g.c.d.(t, n) = 1. As before we consider pr : C∗
z →
Eq = C∗
z/qZ. The index z means that we use z as variable on this copy
– 679 –
Marius van der Put, Marc Reversat
of C∗. Write M := H0(C∗, pr∗(V )). It suﬃces to produce a C[z, z−1]-su-
bmodule M0 ⊂M, invariant under Φ and Φ−1, such that the natural map
O ⊗C[z,z−1] M0 →M is bijective and K ⊗C[z,z−1] M0 is a pure module.
Let β : C∗
s →C∗
z be given by s →sn = z (or by s = z1/n). Deﬁne
the elliptic curve E by γ : C∗
s →E := C∗
s/(q1/n)Z. There is an induced
morphism of α : E →Eq, of degree n, such that α ◦γ = pr ◦β.
The map α is an unramiﬁed cyclic covering of degree n. Let σ denote a
generator of the automorphism group of this covering. One can take for σ
the automorphism of C∗
s →C∗
z, given by s →e2πi/ns. The last map will
also be called σ.
The vector bundle α∗V on E has rank nm and degree tnm. Then α∗V
is a direct sum of indecomposable vector bundles W1 ⊕· · · ⊕Wr on E. Let
W1, W2, . . . , Wr′ with r′ ⩽r be all the Wi which have the same rank and
degree as W1. The direct sum W1 ⊕· · · ⊕Wr′ is invariant under the action
of σ∗. Since V is indecomposable, one has r′ = r. Thus all Wi have the
same rank and degree. It follows that OE(−t[1E]) ⊗α∗V is the direct sum
of indecomposable vector bundles W ′
i on E of degree 0 and rank nm/r.
Using Lemma 11 of [At], we conclude that the diﬀerence module H :=
H0(C∗
s, γ∗W ′
i) over O(C∗
s) has a sequence of submodules 0 = H0 ⊂· · · ⊂
Hnm/r = H such that each quotient has the form O(C∗
s)e with Φe = e. Thus
H has a basis e1, . . . , emn/r over O(C∗
s) such that the matrix of Φ w.r.t. this
basis is upper triangular and all its diagonal entries are 1. One easily veriﬁes
that a base change turns this matrix into a matrix with constant coeﬃcients.
The diﬀerence module over O(C∗
s) associated to OE(t[1E]) has the form
O(C∗
s)e with Φe = cste for some constant c. By taking the tensor prod-
uct with this module and direct sums, we conclude that the diﬀerence
module N over O(C∗
s), associated to γ∗α∗V = β∗pr∗V , has a basis for
which the matrices of Φ and Φ−1 have coeﬃcients in C · sZ. In particu-
lar, there is a C[s, s−1]-module N0 of N, invariant under Φ and Φ−1, such
that O(C∗
s) ⊗C[s,s−1] N0 = N. This submodule is, by construction, invari-
ant under the action of σ. Therefore the C[z, z−1]-module M0 := N σ
0 is
ﬁnitely generated and invariant under the actions of Φ and Φ−1. Moreover
O(C∗
z) ⊗C[z,z−1] M0 = N σ = M and K ⊗C[z,z−1] M0 is pure.
□
Remarks 2.4. — Tensor products of pure diﬀerence modules over K.
One rediscovers Part III of [At] (for the base ﬁeld C) by using Theorem 2.3
and some calculations for diﬀerence modules. We will give some results.
(1) The indecomposable vector bundle corresponding to Um is called Fm in
[At]. The tensor product Ua ⊗Ub corresponds to the tensor product of two
– 680 –
Galois theory of q-diﬀerence equations
unipotent operators A, B on vector spaces V, W of dimensions a, b, having
each only one Jordan block. One can ﬁnd a decomposition of the unipotent
operator A ⊗B ∈GL(V ⊗W) as a direct sum of Jordan blocks. This will
produce the formulas in [At], Theorem 8 and our method is close to the
remarks [At], p. 438-439.
(2) Consider the module (Kne, Φe = czt1/n1e) with (t1, n1) = 1 and n =
dn1 with d > 1. We note that c is determined up to an element of µn1 ×
qZ/n, where µk denotes the group of the kth roots of unity. This module
decomposes as the direct sum of the irreducible modules (Kn1ej, Φej =
qj/nczt1/n1ej) for j = 0, . . . , d−1. A change of c will permute these modules.
(3) Mi := (Kniei, Φei = cizti/niei) for i = 1, 2 with (ti, ni) = 1. Let d =
(n1, n2) and n = n1n2
d . We note that ci is determined up to an element in
µni×qZ/ni. Write t1/n1+t2/n2 = t3/n3 with (t3, n3) = 1 and n = kn3. Then
M1⊗M2 is the direct sum of (Knfj, Φfj = ζjc1c2zt3/n3fj) for j = 0, . . . , d−1
and suitable nth roots of unity ζj. Each term has a further decomposition,
according to (2), if k > 1.
(4) M = (Kne, Φe = czt/ne) with (t, n) = 1. The dual M ∗is equal to
(Kne∗, Φe∗= c−1z−t/ne∗). Further M ⊗M ∗is the direct sum of the n2
diﬀerence modules (Kes,t, Φes,t = qs/ne2πit/nes,t) with 0 ⩽s, t < n. This
corresponds to the direct sum of all line bundles L of order dividing n.
(5) The homomorphism Hom(M1, M2) →Hom(v(M1), v(M2)), where M1, M2
are split modules over K, is in general not surjective. Indeed, the category
of the split diﬀerence modules over K is Tannakian and the category of the
vector bundles on Eq is not even an abelian category.
Theorem 2.5. — Let M be a pure diﬀerence module over K with slope
λ < 0. The maps
(1) coker(Φ −1, Mglobal) →coker(Φ −1, O ⊗C[z,z−1] Mglobal)
(2) coker(Φ −1, Mglobal) →coker(Φ −1, K ⊗C[z,z−1] Mglobal)
are isomorphisms. Moreover, coker(Φ −1, Mglobal) is canonical isomorphic
to H1(Eq, v(M)) and has dimension −λ · dimKM over C.
Before starting the technical proof we study the simplest example:
Mglobal = C[z, z−1]e with Φe = z−1e .
An element of O ⊗Mglobal = Oe has the form  anzne. By Examples 2.2,
v(O ⊗Mglobal) = OEq(−[1]) and by Lemma 2.1, one has ker(Φ −1, O ⊗
Mglobal) = H0(Eq, OEq(−[1])) = 0. Consider the equation
(Φ −1)

anzne =

(an+1qn+1 −an)zne =

bnzne ,
– 681 –
Marius van der Put, Marc Reversat
for a given  bnzne ∈Oe. There is at most one solution. If there is a solution
then its coeﬃcients satisfy the recurrence an+1qn+1 −an = bn which can
also be written as
an+1q(n+2)(n+1)/2 −anq(n+1)n/2 = bnq(n+1)n/2 .
Summation of these recurrences over all n ∈Z implies  bnq(n+1)n/2 = 0.
On the other hand, the condition  bnq(n+1)n/2 = 0 leads to a formula
an := ∞
s=n −bsq(s+1)s/2−(n+1)n/2. One easily veriﬁes that this inﬁnite sum
converges, that the series  anzne belongs to Oe and solves the equation.
If, moreover,  bnzne ∈C[z, z−1]e = Mglobal, then also  anzne lies in
Mglobal. This proves part (1) of Theorem 2.5 for this example.
Proof. — (1) Let −t/n < 0, with t, n ⩾1, g.c.d.(t, n) = 1, be the slope of
M. Then Mglobal can be written as C[z1/n, z−1/n]⊗C W with Φ action given
by Φ(f⊗w) = z−t/nφ(f)⊗A(w) for some A ∈GL(W). Then O⊗Mglobal can
be written as On ⊗C W, where On consists of the convergent Laurent series
in z1/n. The action of Φ is again given by Φ(f ⊗w) = z−t/nφ(f) ⊗A(w).
Consider the equation
(Φ−1)(

k∈Z
zk/n ⊗xk) =

k∈Z
zk/n ⊗(q(k+t)/nA(xk+t)−xk) =

k∈Z
zk/n ⊗wk,
where the given series  zk/n ⊗wk is either ﬁnite or convergent. This yields
recurrence relations for the xk. Write k = k0 + st with k0 ∈{0, 1, . . . , t −1}
and s ∈Z. The recurrence relations are
q(k0+(s+1)t)/nA(xk0+(s+1)t) −xk0+st = wk0+st
for k0 ∈{0, 1, . . . , t −1}, s ∈Z.
Put m(k0, s) = sk0
n + s(s+1)t
2n
. Then the recurrences can be rewritten as
qm(k0,s+1)As+1(xk0+(s+1)t) −qm(k0,s)As(xk0+st) = qm(k0,s)As(wk0+st) .
Suppose that there exists a convergent solution  zk/n ⊗xk, then, for each
k0, the sum over all s ∈Z of the left hand side is 0. Thus a necessary
condition for the existence of a convergent solution is

s∈Z
qm(k0,s)As(wk0+st) = 0 for k0 = 0, 1, . . . , t −1 .
This condition is also suﬃcient for the existence of a convergent solution.
Indeed, the recurrences and the above condition on the coeﬃcients {wk0+st}
– 682 –
Galois theory of q-diﬀerence equations
lead to the formula
xk0+st =
∞

a=s
−qm(k0,a)−m(k0,s)Aa−s(wk0+st) .
The possibly inﬁnite sum in this formula converges and one can verify that
the resulting series  zk/n⊗xk lies in On⊗W and solves the above equation.
If there are ony ﬁnitely many wk̸ = 0 and the above condition is satisﬁed,
then the unique solution 
k zk ⊗xk has only ﬁnitely many xk̸ = 0. From
this observation statement (1) follows.
The proof of (2) is similar. Lemma 2.1 and the above computation yield a
proof of the last statement of the theorem.
□
2.6 (Canonical representatives for coker(Φ −1, Mglobal)). —
Let M be a pure diﬀerence module over K with slope −t/n and n, t ⩾1,
g.c.d.(t, n) = 1. As in the proof of Theorem 2.5, one writes Mglobal =
C[z1/n, z−1/n] ⊗W with Φ action given by Φ(f ⊗w) = z−t/nφ(f) ⊗A(w).
One requires that |q|1/n < |c| ⩽1 for every eigenvalue of A. This makes the
presentation unique.
Deﬁne W + := (C1 + Cz1/n + · · · + Cz(t−1)/n) ⊗W. We claim that
W + →coker(Φ −1, Mglobal) is a bijection.
Indeed, write w+ ∈W + as w+ = t−1
i=0 zi/n ⊗wi. Then w+ lies in the image
of Φ−1 if and only if for all k0 ∈{0, 1, . . . , t−1} one has 
s∈Z qm(k0,s)wk0+st
= 0. This implies that w+ = 0. Hence W + →coker(Φ −1, Mglobal) is
injective. Since both spaces have dimension t·dim W, the map is a bijection.
For any C-linear operator T on M, one writes Eigen(T, c) for the gen-
eralized eigenspace of T for the eigenvalue c ∈C. Thus Eigen(T, c) =

s⩾1 ker((T −c)s, M). With this notation one observes that
W += ⊕|q|t/n<|c|⩽1Eigen(zt/nΦ, c) and W += ⊕|q|t<|c|⩽1Eigen((zt/nΦ)n, c) .
We write Repr(Mglobal) or Repr(M) for the vector space W + of repre-
sentative of coker(Φ −1, M). We note that Repr(M) does not depend on
the choice of the module N over Kn with M = Res(N).
M →Repr(M) has some functorial properties, namely:
A morphism f : M1 →M2 between pure modules of the same negative slope
maps Repr(M1) to Repr(M2).
This follows easily from the second description of W +.
– 683 –
Marius van der Put, Marc Reversat
Let M1, M2 denote pure modules of slopes λ1, λ2 < 0. Then
Repr(M1) ⊗C Repr(M2) is mapped to Repr(M1 ⊗M2) ⊂M1 ⊗M2.
The proof goes as follows. The pure module M3 := M1⊗KM2 has slope λ3 =
λ1+λ2. Choose an integer n ⩾1 such that nλ1, nλ2 ∈Z. For each i = 1, 2, 3,
the vector space Repr(Mi) is equal to ⊕|q|−nλi<|c|⩽1Eigen((z−λiΦ)n, c). The
statement that we want to prove follows from (zλiΦ)n =q−λin(n−1)/2z−nλiΦn
and the observation that q−λ3n(n−1)/2z−nλ3Φn(w1 ⊗w2) equals
q−λ1n(n−1)/2z−nλ1Φn(w1) ⊗q−λ2n(n−1)/2z−nλ2Φn(w2)
for w1 ∈Repr(M1), w2 ∈Repr(M2).
There is a second method, based on subsection 1.4.1, to deﬁne a subspace
of representatives for coker(Φ −1, N) with N pure of slope λ < 0. Let
data(N) = (λ, V, A, {D(σ)}) and K∞⊗N = K∞⊗C V . Then
V + :=

s∈Q, 0⩽s<−λ
zs ⊗V
can be seen to be a vector space of representative for coker(Φ−1, K∞⊗V ).
This set of representatives is invariant under the action of Gal and therefore
Repr∗(N) := (V +)Gal (depending on the choice of L ⊂C) is a C-subspace
of Nglobal representing coker(Φ −1, N). Again N →Repr∗(N) has the
same functorial properties as M →Repr(M). However the behaviour of
Repr∗(N) with respect to tensor products is more transparent.
