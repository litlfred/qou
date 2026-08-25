---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-009-2-vector-bundles-andq-diﬀerence-modules
section_title: "Vector bundles andq-diﬀerence modules"
section_number: 2
pages: 13-20
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
We recall thatO denotes the algebra of the holomorphic functions on
C∗ and that a diﬀerence moduleM overO is a left module over the ring
O[Φ,Φ−1],freeofsomerank m< ∞overO.Further pr : C∗ →Eq := C∗/qZ
denotes the canonical map. One associates toM the vector bundlev(M)o f
rankmonEq givenby v(M)(U)= {f ∈O(pr−1U)⊗OM |Φ(f)= f },where,
foranyopen V ⊂ C∗,O(V)isthealgebraoftheholomorphicfunctionson V.
Ontheotherhand,letavectorbundle Mofrank monEq begiven.Then
N :=pr∗M is a vector bundle onC∗ provided with a natural isomorphism
σ∗
q N→ N , where σq is the mapσq(z)= qz. One knows that N is in
fact a free (or trivial) vector bundle of rankm on C∗ (see [For], p. 204).
Therefore,M,thecollectionoftheglobalsectionsof N,isafree O-moduleof
rankm provided with an invertible action Φ satisfying Φ(fm)= φ(f)Φ(m)
for f ∈ O and m ∈ M. It is easily veriﬁed that the above describes an
equivalencev of tensor categories.
The equivalencev extends to an equivalence between the leftO[Φ,Φ−1]-
modules which are ﬁnitely generated asO-module and the coherent sheaves
– 676 –
Galois theory ofq-diﬀerence equations
onEq. This is an equivalence of Tannakian categories.
Byan admissible diﬀerence module overOwewillmeanaleft O[Φ,Φ−1]-
module which is a direct limit of leftO[Φ,Φ−1]-modules of ﬁnite type over
O. The equivalencev extends to a Tannakian equivalence between category
of the admissible diﬀerence modules overO and the category of the quasi-
coherent sheaves onEq.
Lemma 2.1.— There are isomorphismsker(Φ−1,M) →H0(Eq,v(M))
and coker(Φ −1,M) →H1(Eq,v(M)) between these functors deﬁned on the
category of the admissible diﬀerence modulesM over O.
Proof.— The isomorphism ker(Φ−1,M) →H0(Eq,v(M)) follows from
the deﬁnition ofv. Letv−1 denote the ‘inverse’ of the functorv. ThenM↦ →
ker(Φ − 1,v −1(M)) is canonically isomorphic toM↦ →H0(Eq, M). One
observes that an exact sequence 0→ M1 → M2 → M3 → 0 of admissible
diﬀerence modules overO induces (by the snake lemma) an exact sequence
0 →ker(Φ −1,M 1) →ker(Φ −1,M 2) →ker(Φ −1,M 3) →
coker(Φ −1,M 1) →coker(Φ −1,M 2) →coker(Φ −1,M 3) →0.
From this it easily follows that the ﬁrst right derived functor of the functor
M ↦→ker(Φ −1,M), on the category of admissible modules overO, is equal
to coker(Φ−1,M). Now the second isomorphism of functors follows. □
Examples 2.2.— (1) ConsiderM = Oe with Φ(e)= e. Thenv(M)
is the structure sheafOEq of Eq. Any element inm ∈ M can be written
uniquely asm= ∑
n∈Zanzne. Then (Φ−1)m= ∑
n∈Z(qn −1)anzne. One
observes that ker(Φ−1,M)= Ce and that coker(Φ−1,M) is represented
by Ce. This illustrates Lemma 2.1.
(2) Consider diﬀerence moduleM = Oe with Φe = ce and c ∈ C∗, |q| <
|c| ⩽ 1. Ifc ⁄= 1, thenθce is a meromorphic section ofv(M) with divisor
−pr(c−1)+ pr(1). One concludes thatv(M) ∼=OEq(pr(c−1) −pr(1)). Thus
one ﬁnds all line bundles of degree 0 onEq in this way.
(3) Consider the diﬀerence moduleM := Oe with Φe =( −z)e. There is
a Φ-invariant element, namely Θe. This is a global section ofv(M). The
cokernel of the morphismOEq →v(M), given by 1↦→Θe, is a skyscraper
sheaf with support{1} and stalk C at that point. Indeed, the function Θ
has simple zeros atqZ. One concludes thatv(M) ∼=OEq([1]). Using tensor
products one obtains that the line bundlev(M), withM =Oe, Φe=czte,
has degreet. Moreover every line bundle onEq is obtained in this way.
– 677 –
Marius van der Put, Marc Reversat
(4) LetM =O/OΘ with the Φ-action induced by the usual one ofO. Then
v(M) is the skyscraper sheaf onEq with support {1} and with stalkC at
that point.
Werecallthata split diﬀerence moduleM overK isadirectsumofpure
modules Mi. The global moduleMglobal over C[z,z −1] associated toM is
by deﬁnition the direct sum of the global modules (Mi)global. A morphism
f : M → N between split modules is easily seen to be the direct sum of
morphisms between the pure components ofM andN. In particularf maps
Mglobal toNglobal.
One associates to a split diﬀerence moduleM the diﬀerence module
O⊗C[z,z−1]Mglobal and,byLemma2.1,avectorbundleon Eq.Fornotational
convenience we write againv(M) for this vector bundle. In this way we
obtain a functorv from the category of the split diﬀerence modules overK
tothecategoryofvectorbundleson Eq.OneobservesthatHom( M1,M 2) →
Hom(v(M1),v(M2)) isC-linear and injective. Moreover, one easily sees that
v preserves tensor products.
Theorem 2.3.— The functorv from the category of the split diﬀerence
modules overK to the category of the vector bundles onEq is bijective on
isomorphy classes of objects. This bijection respects tensor products.
Proof.— We have to show thatv induces a bijection between the iso-
morphy classes of the indecomposable objects in the two categories. We
start by proving that for an indecomposable pure diﬀerence moduleM the
corresponding vector bundlev(M) is indecomposable.
From Examples 2.2 one concludes thatv provides a bijection between
the isomorphy classes of the diﬀerence modules of dimension 1 overK and
the isomorphy classes of all line bundles onE
q.
By Corollary 1.6, an indecomposable pure diﬀerence module has the
form M =Res(E(czt/n)) ⊗Um, with uniquen /greaterorequalslant1, (t,n)=1 ,m /greaterorequalslant1 and
cn such that |q|< |cn| ⩽ 1. The vector bundlev(M) has clearly ranknm.
The exterior product ΛnmM is equal toKf with Φf = sztmf for some
s ∈ C∗.T h u sv(M) has degreetm. The casenm = 1 has been treated above
and we suppose nownm> 1.
One can presentMglobal as C[z1/n,z −1/n] ⊗W, withW a C-linear space
of dimensionmand Φ given by Φ(1⊗w)= czt/n ⊗U(w) whereU is a unipo-
tent map with minimal polynomial (U −1)m = 0. ThenO ⊗C[z,z−1] Mglobal
can be represented asHn ⊗W, whereHn consists of the convergent Lau-
rent series inz1/n.T h u sHn consists of the expressions∑ +∞
k=−∞akzk/n with
– 678 –
Galois theory ofq-diﬀerence equations
lim|k|→∞ |ak|1/|k| = 0. One providesW with some norm‖‖. The elements
of Hn ⊗W have the form∑ +∞
k=−∞zk/n ⊗wk with lim|k|→∞ ‖wk‖1/|k| =0 .
Then Φ acts onHn ⊗W by
Φ(
∑
zk/n ⊗wk)=
∑
qk/nzk/nczt/n ⊗U(wk).
Write Ψ =z−tΦn. Then
Ψ(
∑
zk/n ⊗wk)=
∑
zk/n ⊗dqkUn(wk), withd =cnqt(n−1)/2 .
For eachk, the vector spacezk/n ⊗W is invariant under Ψ and this operator
has eigenvaluesqkd on this vector space. One concludes from this that the
subsetMglobal ⊂Hn ⊗W consistsoftheelements fe suchthatthereexistsa
non zero polynomialL ∈ C[T] withL(Ψ)(fe) = 0. This has as consequence
thatevery O-linearendomorphism AofO⊗C[z,z−1]Mglobal,commutingwith
Φ, is theO-linear extension of a uniqueC[z,z −1]-linear endomorphismB
ofMglobal commuting with Φ.
A direct sum decomposition ofv(M) induces aO-linear endomorphism
A ofO ⊗C[z,z−1]Mglobal commuting with Φ and such thatA2 =A. The cor-
responding B induces a direct sum decomposition ofMglobal, contradicting
that M is indecomposable. Thusv(M) is indecomposable. A similar rea-
soning proves that for indecomposableM1,M 2 the relationv(M1) ∼=v(M2)
implies that M1 ∼= M2. In this way we have found a collection of inde-
composable vector bundles onEq. That we have found all of them follows
at once from the classiﬁcation given in [At], Theorem 10. Indeed, Atiyah
constructs a certain indecomposable vector bundle of rankr and degreed,
called E
A(r,d). Leth =( r,d). Then every indecomposable vector bundle
of rankr and degreed has the formL ⊗EA(r,d) withL a line bundle of
degree 0. ThisL is unique up to multiplication with a line bundleN such
thatN ⊗r/h is the trivial line bundle. □
The ﬁnal part of the proof of Theorem 2.3 depends on [At]. We present
now a proof which only uses a simple result of this paper, namely Lemma
11, formulated as follows:
Let W be an indecomposable vector bundle of rankm and degree 0 on an
elliptic curve E, thenW = L ⊗W
′, withL a line bundle of degree 0 and
such that the indecomposableW ′has a sequence of subbundles0= W ′
0 ⊂
W ′
1 ⊂· · ·⊂ W ′
m = W ′ such that each quotientW ′
i+1/W ′
i is isomorphic
to OE.
Proof.— V is an indecomposable vector bundle onEq, rank nm and
degree tm with n,m /greaterorequalslant1, g.c.d.(t,n) = 1. As before we considerpr : C∗
z →
Eq = C∗
z/qZ. The indexz means that we usez as variable on this copy
– 679 –
Marius van der Put, Marc Reversat
of C∗. WriteM := H0(C∗,pr ∗(V)). It suﬃces to produce aC[z,z −1]-su-
bmodule M0 ⊂M, invariant under Φ and Φ−1, such that the natural map
O ⊗C[z,z−1] M0 →M is bijective andK ⊗C[z,z−1] M0 is a pure module.
Let β : C∗
s → C∗
z be given bys ↦→sn = z (or bys = z1/n). Deﬁne
the elliptic curveE by γ : C∗
s → E := C∗
s/(q1/n)Z. There is an induced
morphism ofα :E →Eq, of degreen, such thatα ◦γ =pr ◦β.
The mapα is an unramiﬁed cyclic covering of degreen. Letσ denote a
generator of the automorphism group of this covering. One can take forσ
the automorphism of C∗
s → C∗
z, given bys ↦→e2πi/ns. The last map will
also be calledσ.
The vector bundleα∗V on E has ranknm and degreetnm. Thenα∗V
is a direct sum of indecomposable vector bundlesW1 ⊕···⊕ Wr onE. Let
W1,W 2,...,W r′ with r′ ⩽ r be all theWi which have the same rank and
degree asW1. The direct sumW1 ⊕···⊕ Wr′ is invariant under the action
of σ∗. SinceV is indecomposable, one hasr′ = r. Thus allWi have the
same rank and degree. It follows thatOE(−t[1E]) ⊗α∗V is the direct sum
of indecomposable vector bundlesW ′
i onE of degree 0 and ranknm/r.
Using Lemma 11 of [At], we conclude that the diﬀerence moduleH :=
H0(C∗
s,γ ∗W ′
i) overO(C∗
s) has a sequence of submodules 0 =H0 ⊂· · ·⊂
Hnm/r =H suchthateachquotienthastheform O(C∗
s)ewithΦe=e.Th us
H has a basise1,...,e mn/r overO(C∗
s) such that the matrix of Φ w.r.t. this
basis is upper triangular and all its diagonal entries are 1. One easily veriﬁes
thatabasechangeturnsthismatrixintoamatrixwithconstantcoeﬃcients.
The diﬀerence module overO(C
∗
s) associated toOE(t[1E]) has the form
O(C∗
s)e with Φe = cste for some constantc. By taking the tensor prod-
uct with this module and direct sums, we conclude that the diﬀerence
module N over O(C
∗
s), associated to γ∗α∗V = β∗pr∗V, has a basis for
which the matrices of Φ and Φ−1 have coeﬃcients in C ·sZ. In particu-
lar, there is aC[s,s −1]-module N0 of N, invariant under Φ and Φ−1, such
that O(C∗
s) ⊗C[s,s−1] N0 = N. This submodule is, by construction, invari-
ant under the action ofσ. Therefore the C[z,z −1]-module M0 := Nσ
0 is
ﬁnitely generated and invariant under the actions of Φ and Φ−1. Moreover
O(C∗
z) ⊗C[z,z−1] M0 =Nσ =M andK ⊗C[z,z−1] M0 is pure. □
Remarks 2.4.— Tensor products of pure diﬀerence modules overK.
One rediscovers Part III of [At] (for the base ﬁeldC) by using Theorem 2.3
and some calculations for diﬀerence modules. We will give some results.
(1) The indecomposable vector bundle corresponding toUm is calledFm in
[At]. The tensor productUa ⊗Ub corresponds to the tensor product of two
– 680 –
Galois theory ofq-diﬀerence equations
unipotent operatorsA,B on vector spacesV,W of dimensionsa,b, having
each only one Jordan block. One can ﬁnd a decomposition of the unipotent
operator A ⊗B ∈ GL(V ⊗W) as a direct sum of Jordan blocks. This will
produce the formulas in [At], Theorem 8 and our method is close to the
remarks [At], p. 438-439.
(2) Consider the module (K
ne,Φe = czt1/n1e) with (t1,n 1) = 1 andn =
dn1 with d> 1. We note thatc is determined up to an element ofµn1 ×
qZ/n, whereµk denotes the group of thekth roots of unity. This module
decomposes as the direct sum of the irreducible modules (Kn1ej,Φej =
qj/nczt1/n1ej)for j =0,...,d −1.Achangeof cwillpermutethesemodules.
(3) Mi := (Kniei,Φei = cizti/niei) fori =1 ,2 with (ti,ni)=1 .L e td =
(n1,n 2) andn =n1n2
d . We note thatci is determined up to an element in
µni ×qZ/ni.Write t1/n1+t2/n2 =t3/n3 with(t3,n 3) = 1andn =kn3.Then
M1⊗M2 isthedirectsumof( Knfj,Φfj =ζjc1c2zt3/n3fj)for j =0,...,d −1
and suitablenth roots of unityζj. Each term has a further decomposition,
according to (2), ifk> 1.
(4) M =( Kne,Φe = czt/ne) with (t,n) = 1. The dualM ∗ is equal to
(Kne∗,Φe∗ = c−1z−t/ne∗). FurtherM ⊗M ∗ is the direct sum of then2
diﬀerence modules (Kes,t,Φes,t = qs/ne2πit/nes,t) with 0⩽ s,t < n. This
corresponds to the direct sum of all line bundlesL of order dividingn.
(5) The homomorphismHom(M1,M 2) →Hom(v(M1),v(M2)), whereM1,M 2
are split modules overK, is in general not surjective. Indeed, the category
of the split diﬀerence modules overK is Tannakian and the category of the
vector bundles onEq is not even an abelian category.
Theorem 2.5.—L et M be a pure diﬀerence module overK with slope
λ< 0. The maps
(1) coker(Φ−1,Mglobal) →coker(Φ −1,O ⊗C[z,z−1] Mglobal)
(2) coker(Φ−1,Mglobal) →coker(Φ −1,K ⊗C[z,z−1] Mglobal)
are isomorphisms. Moreover,coker(Φ −1,Mglobal) is canonical isomorphic
to H1(Eq,v(M)) and has dimension−λ ·dimKM over C.
Before starting the technical proof we study the simplest example:
Mglobal = C[z,z −1]e with Φe=z−1e.
An element ofO ⊗Mglobal =Oe has the form∑ anzne. By Examples 2.2,
v(O ⊗Mglobal)= OEq(−[1]) and by Lemma 2.1, one has ker(Φ− 1,O ⊗
Mglobal)= H0(Eq,OEq(−[1])) = 0. Consider the equation
(Φ −1)
∑
anzne=
∑
(an+1qn+1 −an)zne=
∑
bnzne,
– 681 –
Marius van der Put, Marc Reversat
foragiven ∑ bnzne ∈Oe.Thereisatmostonesolution.Ifthereisasolution
then its coeﬃcients satisfy the recurrencean+1qn+1 −an = bn which can
also be written as
an+1q(n+2)(n+1)/2 −anq(n+1)n/2 =bnq(n+1)n/2 .
Summation of these recurrences over alln ∈ Z implies ∑ bnq(n+1)n/2 =0 .
On the other hand, the condition∑ bnq(n+1)n/2 = 0 leads to a formula
an := ∑ ∞
s=n −bsq(s+1)s/2−(n+1)n/2. One easily veriﬁes that this inﬁnite sum
converges, that the series∑ anzne belongs toOe and solves the equation.
If, moreover, ∑ bnzne ∈ C[z,z −1]e = Mglobal, then also ∑ anzne lies in
Mglobal. This proves part (1) of Theorem 2.5 for this example.
Proof.— (1)Let −t/n< 0,with t,n /greaterorequalslant1, g.c.d.(t,n) = 1,betheslopeof
M. ThenMglobal can be written asC[z1/n,z −1/n]⊗CW with Φ action given
by Φ(f ⊗w)= z−t/nφ(f)⊗A(w)forsome A ∈GL(W).Then O⊗Mglobal can
be written asOn ⊗CW, whereOn consists of the convergent Laurent series
in z1/n. The action of Φ is again given by Φ(f ⊗w)= z−t/nφ(f) ⊗A(w).
Consider the equation
(Φ −1)(
∑
k∈Z
zk/n ⊗xk)=
∑
k∈Z
zk/n ⊗(q(k+t)/nA(xk+t) −xk)=
∑
k∈Z
zk/n ⊗wk,
where the given series∑ zk/n ⊗wk is either ﬁnite or convergent. This yields
recurrence relations for thexk. Writek =k0 +st withk0 ∈{0,1,...,t −1}
ands ∈ Z. The recurrence relations are
q(k0+(s+1)t)/nA(xk0+(s+1)t) −xk0+st =wk0+st
fork0 ∈{0,1,...,t −1},s ∈ Z.
Putm(k0,s)= sk0
n +s(s+1)t
2n . Then the recurrences can be rewritten as
qm(k0,s+1)As+1(xk0+(s+1)t) −qm(k0,s)As(xk0+st)= qm(k0,s)As(wk0+st).
Suppose that there exists a convergent solution∑ zk/n ⊗xk, then, for each
k0, the sum over alls ∈ Z of the left hand side is 0. Thus a necessary
condition for the existence of a convergent solution is
∑
s∈Z
qm(k0,s)As(wk0+st) = 0 fork0 =0,1,...,t −1.
Thisconditionisalsosuﬃcientfortheexistenceofaconvergentsolution.
Indeed,therecurrencesandtheaboveconditiononthecoeﬃcients {wk0+st}
– 682 –
Galois theory ofq-diﬀerence equations
lead to the formula
xk0+st =
∞∑
a=s
−qm(k0,a)−m(k0,s)Aa−s(wk0+st).
The possibly inﬁnite sum in this formula converges and one can verify that
theresultingseries ∑ zk/n ⊗xk liesin On ⊗W andsolvestheaboveequation.
Ifthereareonyﬁnitelymany wk ⁄= 0andtheaboveconditionissatisﬁed,
then the unique solution∑
kzk ⊗xk has only ﬁnitely manyxk ⁄= 0. From
this observation statement (1) follows.
The proof of (2) is similar. Lemma 2.1 and the above computation yield a
proof of the last statement of the theorem. □
