---
doc_id: arxiv-math-0203273v3
doc_title: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéa"
section_id: sec-301-v-further-h-acts-on-the-associated-graded-grµv-t
section_title: "Further H acts on the associated graded GrµV through M, and µ induces an"
section_number: V
pages: 132-146
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéaux et radicaux 7 — 3"
---
M-homomorphismV⊗k Grn
µV→ Grn+1
µ V for eachn.
Lemma C.4. Suppose that k is algebraically closed, and let H be a connected
afﬁnek-group with prounipotent radical of dimension> 1. Then there exists a rep-
resentation of H over the afﬁne line A1 with ﬁbres at k-points of A1 pairwise
non-isomorphic.
Proof. We may suppose that H is of ﬁnite type over k. If U is the prounipotent
radical ofH andZ1⊂Z2⊂···⊂ Zm−1⊂Zm =U is the upper central series of
U, then theZi are normal subgroups ofH, andZm/Zm−1 is of dimension> 1 since
U is of dimension> 1. Factoring outZm−1, we may suppose thatU is commutative.
We haveH = U ⋊M withM a connected reductive subgroup of H. WriteV for
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 133
the Lie algebra of U. The action of M onU deﬁnes a representation of M onV .
If ¯U is anM-quotient ofU of dimension> 1 we may replaceH =U ⋊M by its
quotient ¯U ⋊M, so we may suppose that V is either irreducible of dimension> 1
or is the direct sum of two 1-dimensional representations. It will be convenient to
distinguish the following three cases :
I V is the direct sum of two isomorphic 1-dimensional representations ;
II V is either the direct sum of two non-isomorphic1-dimensional representa-
tions, or is irreducible of dimension 2 or 3 ;
III V is irreducible of dimension> 3.
Suppose I holds. Then we may identify U with G2
a, where M acts on both fac-
tors as the same character χ. With A1 = Spec(k[t]), we may identify the endo-
morphism ring of (Ga)A1 over A1 withk[t]. If M acts on (Ga)A1 asχ, then the
semidirect product over A1 of (1,−t) : UA1 = ( Ga)2
A1→ (Ga)A1 withMA1 is
a homomorphism p : HA1 → (Ga ⋊M )A1 over A1. Given a faithful represen-
tation τ : Ga ⋊M → GL(n), the kernel of the ﬁbre above x∈ A1(k) = k of
τA1◦p :HA1→GL(n)A1 is the subgroup
(x
1
)
: Ga→ G2
a =U ofU⊂H. The
ﬁbres of the representationτA1◦p ofH over A1 are thus pairwise non-isomorphic.
Now suppose II holds. Apply Lemma C.3 to obtain a family (V i
j,r i
j,s i
j)i,j∈N,
withri
j : V ⊗k V i
j → V i+1
j andsi
j : V⊗k V i
j+1→ V i
j , such that (i) and (ii) of
Lemma C.3 hold. Write A1 = Spec(k[t]), and deﬁne a family (E i
j,f i
j,g i
j)i,j∈N of
freeOA1-modules of ﬁnite type E i
j andOA1-homomorphisms f i
j :E i
j → Ei+1
j ,
gi
j :E i
j+1→E i
j byE 0
0 =E 1
0 =E 0
1 =E 2
1 =E 1
2 =E 2
2 =OA1,E 1
1 =O2
A1,E i
j = 0 for
all otheri,j , andf 0
0 = g0
0 = f 1
2 =g2
1 = 1 andf 0
1 =
(1
0
)
,g1
0 = (1,−t),g1
1 =
(0
1
)
,
f 1
1 = (−1, 1). The non-zeroE,f,g thus form a commutative diagram
(C.8)
OA1
1−−−−→ OA1


↓ (0
1)


↓ 1
OA1
(1
0)−−−−→ O2
A1
(−1,1)
−−−−→ OA1


↓ 1


↓ (1,−t)
OA1
1−−−−→ OA1
Now setV =⨁
i,j∈NV i
j⊗E i
j and letµ :V⊗kV→V have component
V⊗kV i
j⊗kE i
j→V i′
j′⊗E i′
j′
given by ri
j⊗f i
j if (i′,j′) = ( i + 1,j ), si
j⊗gi
j if (i′,j′ + 1) = ( i,j ), and 0 in
all other cases. Clearly µ(3) = 0 , and the restriction of µ(2) to⋀ 2V ⊗kV is 0
by (ii) of Lemma C.3 together with the fact that (C.8) commute s. Thus (V,µ ) is a
representation ofH over A1.
We now show that an isomorphism between the ﬁbres (Vx,µ x) and (Vy,µ y) of
(V,µ ) at the k-points x and y of A1 induces an isomorphism between the ﬁbres
134 YVES ANDR ´E ET BRUNO KAHN
at x and y of the diagram (C.8). This will give an isomorphism k2 = (E 1
1 )x ≃
(E 1
1 )y = k2 which sends Im(g1
1)x, Ker(f 1
1 )x, Im(f 0
1 )x, Ker(g1
0)x respectively to
Im(g1
1)y, Ker(f 1
1 )y, Im(f 0
1 )y, Ker(g1
0)y, hence an isomorphism P1≃ P1 which
sends 0, 1,∞,x respectively to 0, 1,∞,y , and so will implyx =y as required.
For any x we haveVx =⨁
i,j∈NV i
j⊗kEi
j withEi
j the ﬁbre ofE i
j atx. Write
V n
x = ⨁
i−j=nV i
j ⊗k Ei
j, so that Vx = ⨁
n∈ZV n
x . Then µx : V ⊗kVx →V x
restricts to anM-homomorphism
µn
x :V⊗kV n
x→V n+1
x
for each n. Further µn
x is an epimorphism for n≥− 1 because its composite with
each projectionV n+1
x → V i
j ⊗k Ei
j is an epimorphism by (C.8), and the V i
j with
i−j =n + 1 are pairwise non-M-isomorphic by (i) of Lemma C.3. Sinceµn
x = 0
forn< −1, it follows that the image ofµ(n)
x :V⊗n⊗kVx→V x is⨁
m≥n−1V m
x .
Hence Grn
µxVx =V n−1
x , andV⊗k Grn
µxVx→ Grn+1
µx Vx induced byµx coincides
withµn−1
x . Thus any isomorphism θ : (Vx,µ x)→ (Vy,µ y) induces on passage to
the associated graded an isomorphism
θn :V n
x→V n
y
for eachn such that the diagram
(C.9)
V⊗kV n
x
µn
x
−−−−→ Vn+1
x

↓ V⊗θn


↓ θn+1
V⊗kV n
y
µn
y
−−−−→ Vn+1
y
commutes. Since for eachn theV i
j withi−j =n are pairwise non-M-isomorphic
by (i) of Lemma C.3, there arek-isomorphismsθi
j :Ei
j→Ei
j such that
θn =V i
j⊗kθi
j.
From (C.9) it then follows that
ri
j⊗ (θi+1
j (f i
j )x) = ri
j⊗ ((f i
j )yθi
j)
si
j⊗ (θi
j(gi
j)x) = si
j⊗ ((gi
j )yθi
j+1)
fori,j ≥ 0. Since theri
j andsi
j are non-zero,
θi+1
j (f i
j )x = (f i
j )yθi
j
θi
j(gi
j )x = (gi
j)yθi
j+1,
so theθi
j give an isomorphism between the ﬁbres of (C.8) atx andy.
Finally suppose III holds. In the notation of Lemma C.1, chooseτ∈P such that
τ +λ∈ P and τ +λ /∈ Λ forλ∈ Λ . Then V⊗k Vτ ≃ ⨁
λ∈Λ V m(λ)
τ +λ . Choose
by Lemma C.2 distinct non-zero elements λ1,λ2,λ3,λ4 of Λ , and write V0 = Vτ
and Vj = Vτ +λj, j = 1, 2, 3, 4. The Vi, i = 0, 1, 2, 3, 4 are then pairwise non-
isomorphic irreducible representations ofM, andVj is a direct summand ofV⊗kV0
for j = 1, 2, 3, 4. Let rj : V ⊗k V0→ Vj be a non-zero M-homomorphism for
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 135
j = 1, 2, 3, 4. With A1 = Spec(k[t]), setE0 =O2
A1,Ej =OA1 forj = 1, 2, 3, 4,
and deﬁnefj :Ej→E 0 forj = 1, 2, 3, 4 byf1 = (1, 0),f2 = (−1, 1),f3 = (0, 1),
f4 = (1,−t). Now setV =⨁ 4
i=0Vi⊗kEi and letµ :V⊗kV→V have component
V⊗kVi⊗E i→Vi′⊗E i′
given byrj⊗fj wheni = 0,i′ =j andj = 1, 2, 3, 4, with all other components 0.
Thenµ(2) = 0 so (V,µ ) is a representation ofH over A1.
Suppose that θ :Vx→V y is an isomorphism between the ﬁbres (Vx,µ x) and
(Vy,µ y) atx andy. SinceVx =⨁ 4
i=0Vi⊗kEi withEi the ﬁbre ofEi atx, and since
theVi are pairwise non-M-isomorphic, we haveθ =⨁ 4
i=0Vi⊗θi for isomorphisms
θi :Ei→Ei. Compatibility ofθ withµx andµy then shows that forj = 1, 2, 3, 4
rj⊗ (θj(fj)x) = rj⊗ ((fj)yθ0)
whence
θj(fj)x = (fj)yθ0
sincerj⁄= 0 . Thus the θi give an isomorphismk2 = E0≃ E0 = k2 which sends
Ker(fj)x to Ker(fj)y forj = 1, 2, 3, 4, and hence an isomorphism P1≃ P1 which
sends 0, 1,∞,x respectively to 0, 1,∞,y . Thusx =y as required. □
Lemma C.5. LetH be an afﬁnek-group with prounipotent radicalU of dimension
≤ 1. Then there exists a k-homomorphism H→ GL(2) with restriction to U an
embedding. If g is such a k-homomorphism and p : H→ H/U is the projection
then every indecomposable representation ofH is isomorphic to g∗V⊗kp∗W for
some representationV ofGL(2) andW ofH/U .
Proof. We may suppose thatU is of dimension 1. ThenM =H/U acts onU as a
characterχ. Taking a Levi decomposition ofH and identifyingU with Ga we may
supposeH = Ga ⋊χM. The restriction toU of thek-homomorphismH→GL(2)
deﬁned by
am↦→
(
χ(m) a
0 1
)
for pointsa of Ga andm ofM is then an embedding.
A representation of H on a k-vector spaceE is a representation of M onE to-
gether with anM-homomorphismE⊗kχ→E such thatE⊗kχr→E induced
by iteration is 0 forr large. Equivalently, a representation ofH onE is a represen-
tation of M on E together with a structure of module on E over the polynomial
ringk[n] such thatn acts nilpotently andmne =χ(m)nme for eachk-algebrak′,
m∈M (k′) ande∈E⊗kk′.
IfD is the standard 2-dimensional representation of GL(2), then the kernel of
g∗D→ g∗D deﬁned by the action of n is 1-dimensional and stable under M. Let
d0⁄= 0 be an element of a1-dimensionalM-stable subspace ofg∗D complementary
to this kernel. Then d1 = nd0 ⁄= 0 , nd1 = 0 , and md0 = χ0(m)d1, md1 =
χ(m)χ0(m)d1 for points m ofM and some character χ0 ofM. Thus if V is the
rth symmetric power of D, there is a basis v0,...,v r of g∗V for which mvi =
χi(m)χr
0(m)vi andnvi =vi+1 ifi<r andnvr = 0.
136 YVES ANDR ´E ET BRUNO KAHN
Now letE be a representation ofH. LetE0 be anM-subrepresentation ofE, and
suppose thatnr+1E = 0. Then if W = E0⊗χ−r
0 , the assignment vi⊗w↦→niw
deﬁnes an H-homomorphismϕ :g∗V⊗kp∗W→E. For the second statement, it
will thus sufﬁce to show that ifE isH-indecomposable, and ifr andE0 are chosen
so that nrE⁄= 0 ,nr+1E = 0 , and E0⊕nE = E, then ϕ is an isomorphism, i.e.
eache∈E has a unique decomposition
(C.10) e =e0 +ne1 +··· +nrer
withei∈ E0 fori = 0,...,r . In fact from E0⊕nE = E it follows inductively
thatE = E0 +··· +niE0 +ni+1E so taking i = r shows that each e∈ E has
a decomposition (C.10). To prove the uniqueness, write E′′ for the kernel of nr
restricted toE0 and letE′ be anM-subspace ofE0 such thatE0 =E′⊕E′′. Since
nrE⁄= 0 we haveE′⁄= 0. Ife′ =∑ r
i=0nie′
i ande′′ =∑ r
i=0nie′′
i withe′
i∈E′ and
e′′
i ∈ E′′, then e′ = e′′ impliese′
i = 0 fori = 0, 1,...,r , as is seen by induction
on i : given that e′
0 = e′
1 =··· = e′
i−1 = 0 , from nr−ie′ = nr−ie′′ we have
nre′
i = nre′′
i = 0 whencee′
i = 0 . Thusk[n]E′∩k[n]E′′ = 0 andE = k[n]E0 =
k[n]E′⊕k[n]E′′. Since E is H-indecomposable and k[n]E′ and k[n]E′′ are H-
subspaces of E, we have E′′ = 0 andE′ = E0, whence the required uniqueness
sincee′ = 0 impliese′
i = 0 fori = 0, 1,...,r . □
Lemma C.6. LetH be an afﬁnek-group, letk′ be an extension ofk, and letV′ be
a representation ofH overk′.
(i) IfH is proreductive thenV′ is a direct summand of someV⊗kk′.
(ii) Ifk′ is algebraic overk thenV′ is a direct summand of someV⊗kk′.
(iii) If k is algebraically closed and V′ is a direct summand of V ⊗k k′, then
V′≃V0⊗kk′ for some direct summandV0 ofV .
Proof. There is a canonical epimorphism
(C.11) V′⊗kk′→V′→ 0
of (not necessarily ﬁnite dimensional)H-representations overk′. SinceV′ is ﬁnite-
dimensional overk′ there is a ﬁnite dimensionalH-subrepresentationV ofV′ over
k such that the restriction of (C.11) toV⊗kk′ is an epimorphism. IfH is reductive,
V′ is a direct summand of V⊗k k′, whence (i). To prove (ii) we may suppose k′
ﬁnite overk. ThenV′ is ﬁnite dimensional overk and there is a canonical splitting of
(C.11), deﬁned using the trace fromk′ tok. For (iii), note that ifA = End H (V ), any
idempotente inA⊗kk′ is conjugate to one in A. Indeede generates a semisimple
k′-subalgebra of A⊗k k′ and so some conjugate lies in the extension to k′ of a
maximal semisimple subalgebra ofA. Withk algebraically closed, it is then obvious
that some conjugate lies inA. □
Theorem C.1. IfH is an afﬁnek-group the following conditions are equivalent :
(a) the prounipotent radical ofH is of dimension≤ 1 ;
(b) for everyk-schemeS of ﬁnite type and familyV of representations ofH over
S, there is a ﬁnite extension k′ of k and a stratiﬁcation of Sk′ by locally closed
subschemes such that the familyVk′ of representations ofHk′ overSk′ is constant
along each stratum ;
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 137
(c) for everyk-schemeS of ﬁnite type and familyV of representations ofH over
S, the set ofH-isomorphism classes of the ﬁbres ofV atk-points ofS is ﬁnite ;
(d) for every familyV representations ofH over A1 there exists a representation
V ofH overk such thatVx≃V for an inﬁnite set ofx∈ A1(k).
Proof. (a) =⇒ (b) : We may suppose that k is algebraically closed. It is enough
to show then that, assuming the prounipotent radical U ofH is of dimension≤ 1,
each representationV ofH over a non-empty reduced and irreducible k-schemeS
of ﬁnite type is constant along some non-empty open subschem e of S. Let V1 be
the generic ﬁbre of V. If K = GL(2)×M/U and k′ is the function ﬁeld of S
there is by Lemma C.5 a k-homomorphismf : H→ K such thatV1≃ f∗
k′V′ for
some representationV′ ofKk′. FurtherV′≃V⊗kk′ for some representationV of
K by (i) and (iii) of Lemma C.6, so there is an H-isomorphismV1≃ f∗V⊗kk′.
This extends to an H-isomorphism ofV with the constant family f∗V along some
non-empty open subscheme ofS.
(b) =⇒ (c) : It is enough to note that representations V and W of H which
become isomorphic overk′ are themselves isomorphic, because the determinant is
then not identically zero on HomH(V,W ).
(c) =⇒ (d) is immediate.
(d) =⇒ (a) : Call the ﬁbres of a representation V ofH over A1 almost distinct
if for each representation V of H over k we haveVx ≃ V for only a ﬁnite set
ofx∈ A1(k). The ﬁbres of V are almost distinct provided that those of the rep-
resentation obtained from V by either extension of scalars, pullback along some
H′→ H, or passage to a direct summand, are almost distinct. This is immediate
in the ﬁrst two cases and in the case of direct summands follow s from the fact that
by Krull–Schmidt anyVx has only a ﬁnite set of pairwise non-H-isomorphic direct
summands. Now suppose that (a) does not hold. Then we show tha t there exists a
V whose ﬁbres are almost distinct, so that (d) does not hold. To do this we may
suppose by passing to a quotient thatH is of ﬁnite type.
Consider ﬁrst the case where k is algebraically closed. If H 0 is the connected
component of H there is then by Lemma C.4 a representation V 0 ofH 0 over A1
with almost distinct ﬁbres. Since V 0 is a direct H 0-summand of the induced H-
representation IndH
H 0V 0, the ﬁbres of IndH
H 0V 0 are almost distinct.
For arbitrary k, with algebraic closure ¯k, there is thus a representation ¯V ofH
over A1¯k with almost distinct ﬁbres. We have ¯V =V′⊗k′ ¯k for some ﬁnite extension
k′ ofk andH-representationV′ over Ak′. If p : A1
k′→ A1 is the projection and
we writeV =p∗V′ thenV′ is a directH-summand ofV⊗ kk′ =p∗p∗V′. The ﬁbres
ofV′ and henceV are thus almost distinct. □
Theorem C.2. Let H be an afﬁne k-group and let k′ be an extension of k. Then
every representation ofH overk′ is a direct summand of a representation deﬁned
overk if and only if either k′ is algebraic overk or the prounipotent radical of H
has dimension≤ 1.
Proof. Ifk′ is algebraic overk then each representationV′ ofH overk′ is a direct
summand of someV⊗kk′ by Lemma C.6(ii). Suppose that the prounipotent radical
138 YVES ANDR ´E ET BRUNO KAHN
U ofH has dimension≤ 1. IfK =GL(2)×M/U there is then by Lemma C.5 ak-
homomorphismf :H→K such that any representationV′ ofHk′ is isomorphic to
f∗
k′W′ for some representationW′ ofKk′. ThenW′ is a direct summand ofW⊗kk′
for some representation W ofK by Lemma C.6(i), so V′ is a direct summand of
f∗W⊗kk′.
For the converse, suppose thatk′ is transcendental overk and that the prounipo-
tent radical of H has dimension > 1. Then by the equivalence of (a) and (d) of
Theorem C.1, there is a representationV ofH over A1 with an inﬁnite set of pair-
wise non-isomorphic ﬁbres at k-points of A1. Choose an embedding of k(t) ink′,
and letV1 be the generic ﬁbre ofV. We show thatV1⊗k(t)k′ is not a direct summand
of anyV⊗kk′. In fact suppose the contrary. Then for someV the identity ofV1 lies
in the image of the composition homomorphism
HomH,k(t)(V⊗kk(t),V 1)⊗k(t) HomH,k(t)(V1,V ⊗kk(t))→ EndH,k(t)V1,
since this is so after extending scalars from k(t) tok′. Thus for some n there are
H-homomorphismsri :V⊗kk(t)→V1,si :V1→V⊗kk(t),i = 1,...,n over
k(t) such that r1s1 +··· +rnsn = 1 V1. This implies that V1 is a direct summand
ofV n⊗kk(t). ThusV is a direct summand of the constant family V n along some
non-empty open subscheme of A1. By Krull–Schmidt this contradicts the fact that
V has an inﬁnite set of pairwise non-isomorphic ﬁbres. □
C.2. Application to proreductive envelopes. In connection with proreductive en-
velopes it will be convenient to use the following terminology. Letf :H→K be
ak-homomorphism from an afﬁne k-group to a proreductive k-group. Call f uni-
versal if each k-homomorphism H → K′ to a proreductive K′ factors, uniquely
up to conjugation by a k-point of K′, through f. Equivalently,f is universal if its
conjugacy class is the embedding of H into its proreductive envelope. Th´ eor` eme
19.3.1 states that for each H there exists a universalf. Callf minimal iff factors
through no proper proreductive subgroup ofK. IfL is proreductive,h :H→L is
universal, andf = lh, thenf is universal if and only if l is an isomorphism and f
is minimal if and only ifl is faithfully ﬂat.
By considering k-homomorphisms to general linear groups it can be seen that
if f is universal then f∗ induces a bijection on isomorphism classes of objects
(Proposition 19.3.4). We note also the following fact, whic h generalises a result
due to Kostant [33, Theorem 3.6]. If f is universal, then any k-homomorphism
h :H→K′ to a proreductiveK′ factors throughf uniquely up to conjugation by
a uniquek-point of the prounipotent radicalRuCK ′(h) of the centraliserCK ′(h) of
h. Equivalently, ifh = lf thenCK ′(l) is a Levi subgroup of CK ′(h), i.e. CK ′(h)
is the semidirect product of RuCK ′(h) andCK ′(l). To verify this, let L be a Levi
subgroup ofCK ′(h). Thenh factors through the proreductive subgroupCK ′(L) of
K′, so by universality of f the conjugate ofl by somek-pointz ofCK ′(h) factors
through CK ′(L). Thus L⊂ zCK ′(l)z−1⊂ CK ′(h) and zCK ′(l)z−1 = L since
CK ′(l) is proreductive.
The main facts required about universal and minimalk-homomorphisms are con-
tained in the following lemma.
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 139
Lemma C.7. Letf : H→ K be a k-homomorphism from an afﬁne k-group to a
proreductivek-group. Then
(i)f is universal if and only if f is minimal and each representation of H is a
direct summand off∗V for some representationV ofK.
(ii) Iff is minimal thenfk′ :Hk′→Kk′ is minimal for any extensionk′ ofk.
(iii) Iff is universal thenfk′ :Hk′→Kk′ is universal for any algebraic exten-
sionk′ ofk.
Proof. Factor f as H
g
→ L l→ K with L proreductive and g universal. Then g∗
induces a bijection on isomorphism classes of objects, and f is universal (resp.
minimal) if and only ifl is an isomorphism (resp. faithfully ﬂat).
Thusf is universal⇐⇒f is minimal andl is a closed immersion. Furtherl is a
closed immersion⇐⇒each representation of L is a direct summand of some l∗V
(becauseL is proreductive)⇐⇒ each representation of H is a direct summand of
somef∗V . This gives (i).
If W is representation of a k-group G, write mG(W ) for the multiplicity of
the trivial G-representation k in a decomposition of W into G-indecomposables.
ClearlymG(W ) is the rank of the canonical k-homomorphismW G→ WG, so it
is preserved by extension of the scalars. Then l is surjective⇐⇒l∗ is fully faith-
ful (because L is proreductive)⇐⇒ dimk HomK(k,V ) = dim k HomL(k,l∗V )
for each representation V of K ⇐⇒mK (V ) = mL(l∗V ) for each V ⇐⇒
mK(V ) = mH(f∗V ) for eachV⇐⇒eachV is a direct summand of some V1 for
whichmK (V1) = mH(f∗V1) (becausemK(V )≤ mH(f∗V )). By Lemma C.6(i),
if the last condition is satisﬁed it is also satisﬁed with f,H andK replaced byfk′,
Hk′ andKk′. This gives (ii).
For (iii) it is enough by (i) and (ii) to show if each representation ofH is a direct
summand of some f∗V then each representation of Hk′ is a direct summand of
somef∗
k′V′. This is clear from Lemma C.6(ii). □
Theorem C.3. LetH be an afﬁnek-group and letk′ be an extension ofk. Then the
canonical morphism p Red(Hk′)→ p Red(H)k′ is an isomorphism if and only if
eitherk′ is algebraic overk or the prounipotent radical ofH is of dimension≤ 1.
Proof. Letf : H→ K, with K proreductive, be universal. Then p Red(Hk′)→
p Red(H)k′ is an isomorphism⇐⇒fk′ is universal⇐⇒each representation ofHk′
is a direct summand of somef∗
k′W′ (Lemma C.7)⇐⇒each representation ofHk′ is
a direct summand of somef∗W⊗kk′ (Lemma C.6(i))⇐⇒each representation of
Hk′ is a direct summand of someV⊗kk′. The result thus follows from Theorem C.2.
□
Theorem C.4. Let U be a unipotent k-group of dimension 1, equipped with an
action of the proreductivek-groupM. Then
(i) There exists anM-embeddingU→SL(2) for some action ofM onSL(2).
(ii) Iff :U→SL(2) is anM-embedding andh :U→K is anM-homomorphism
withK proreductive, then there is an M-homomorphisml : SL(2)→ K, unique
up to conjugation by ak-point ofK ﬁxed byM, such thath =lf .
140 YVES ANDR ´E ET BRUNO KAHN
(iii) Iff :U→SL(2) is anM-embedding then (the conjugacy class of)f ⋊M :
U ⋊M→SL(2) ⋊M is the embedding ofU ⋊M into its proreductive envelope.
Proof. By Lemma C.5 there is ak-homomorphismg :U ⋊M→GL(2) non-trivial
onU. The restriction of g toU factors through anM-embeddingf :U→SL(2),
whereM acts onSL(2) throughg and the inner action ofGL(2). This gives (i).
It will sufﬁce to prove (ii) and (iii) for the f just constructed. Consider ﬁrst (iii).
LetL be a proreductive subgroup ofSL(2)⋊M through whichf ⋊M factors. Then
L∩SL(2)⊃U is reductive sinceSL(2) is normal inSL(2)⋊M, soL∩SL(2) = L
andL⊃SL(2). AlsoL⊃M, soL =SL(2) ⋊M. Thusf ⋊M is minimal. The
projectionU ⋊M→ M factors throughf ⋊M : U ⋊M→ SL(2) ⋊M, andg
factors throughf ⋊M by construction. Thus (f ⋊M )∗ is essentially surjective by
Lemma C.5, and so universal by Lemma C.7(i).
Givenh as in (ii),h⋊M is by universality off ⋊M the composite off ⋊M with
ak-homomorphismSL(2)⋊M→K ⋊M, necessarily of the forml ⋊M for some
M-homomorphisml. Thush =lf . If alsoh =l′f for anM-homomorphisml′, then
l andl′ are by universality off conjugate by a uniquek-pointα of the prounipotent
radical of the centraliser ofh. This implies thatlk′ andl′
k′ are conjugate bymα for
any extensionk′ ofk andm∈ M (k′). SinceM stabilises the centraliser of h and
so the prounipotent radical of this centraliser,M ﬁxesα by uniqueness. □
An afﬁnek-groupG will be called ﬁnite dimensional if its quotients of ﬁnite type
are of bounded dimension. It is equivalent to require that the connected component
ofG be an extension of a group of ﬁnite type by a pro´ etale group.
Lemma C.8. Ifk is algebraically closed then a connected ﬁnite dimensionalreduc-
tivek-group has only a ﬁnite number of non-isomorphic irreducible representations
of given dimension and determinant.
Proof. The connected semisimple case follows from Weyl’s dimension formula. In
general, a connected ﬁnite dimensional reductive group is a quotient ofT×G for
some protorus T and connected semisimple G. An irreducible representation of
T×G of dimensionn and determinantχ is the tensor product of ann-dimensional
irreducible representation ofG with a 1-dimensional representation ofT deﬁned by
a character ψ withψn = χ. Since there is at most one such ψ, the result follows
from the connected semisimple case. □
Theorem C.5. The proreductive envelope of an afﬁne k-groupH is of ﬁnite type
overk (resp. ﬁnite dimensional) if and only ifH is of ﬁnite type overk (resp. ﬁnite
dimensional) and the prounipotent radical ofH is of dimension≤ 1.
Proof. The “if” is clear by Theorem C.4(iii). Letf :H→K, withK proreductive,
be universal. For the “only if”, it sufﬁces to show that if the prounipotent radical of
H has dimension> 1 thenK is not ﬁnite dimensional. By Lemma C.7(iii) we may
suppose thatk is algebraically closed. If ¯H is a quotient ofH and ¯H→ ¯K, with ¯K
proreductive, is universal, then H→ ¯H→ ¯K is minimal, and so factors through
a faithfully ﬂat K→ ¯K. Replacing H by an appropriate ¯H, we may thus further
supposeH to be of ﬁnite type (see also Proposition 19.4.7 c)). Let j : H 0→ H
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 141
be the embedding of the connected component of H and g : H 0 → L, with L
proreductive, be universal, so that fj = lg for some l : L → K. Then l is a
closed immersion. Indeed otherwise some representation ofL would not be a direct
summand of any l∗V , whence the same would hold with L andl replaced by H 0
andj, sincef∗ andg∗ induce bijections on isomorphism classes of objects. But each
representationW ofH 0 is a direct summand of j∗ IndH
H 0W . Replacing H byH 0
we may thus supposeH connected (see also Proposition 19.4.7 a)). ThenK also is
connected, as is seen by consideringk-homomorphisms to ﬁnite groups.
By Theorem C.1 there is a family V of representations of H, parametrised by
A1, such that the set of H-isomorphism classes of the ﬁbres Vx forx∈ A1(k) is
inﬁnite. There thus exists an inﬁnite set S of pairwise non-isomorphic irreducible
representationsV ofH such that each V ∈S is a direct summand of someVx for
x∈ A1(k). Let T be the radical of a a Levi subgroup of H. The restrictions to
T of theVx are isomorphic, so among direct summands of the Vx there are only a
ﬁnite number of possible T -isomorphism classes. Since the determinant of a rep-
resentation of H is deﬁned uniquely by its restriction to T , it follows that there is
an inﬁnite subsetS′ ofS such that eachV ∈S ′ has the same determinantχ. Then
χ = ψ◦f for a unique character ψ ofK. EachV ∈S ′ is isomorphic to f∗W for
some representationW ofK, and each suchW has determinantψ and dimension at
most that of the ﬁbres ofV. Lemma C.8 then shows thatK is not ﬁnite dimensional.
□
By a similar argument it can be shown for example that if k is uncountable the
proreductive envelope of an afﬁne k-group with prounipotent radical of dimension
> 1 is not a countable limit ofk-groups of ﬁnite type.
142 YVES ANDR ´E ET BRUNO KAHN
R´EF ´ERENCES
[1] Y . Andr´ e, B. Kahn, Construction inconditionnelle de groupes de Galois motiviques, C.R. Acad.
Sci. Paris, S´ er I.331 (2002), 989–994.
[2] A. Beilinson, Height pairing between algebraic cycles, in : K-theory, Arithmetic and Geometry,
Lect.notes in Math. 1289, Springer (1987), 27–41.
[3] D. Benson, Representations and cohomology I , Cambridge studies 30, Cambridge Univ.
Press,1995.
[4] F. Beukers, D. Brownawell, G. Heckman, Siegel normality , Annals of Math. 127 (1988), 279–
308.
[5] N. Bourbaki, Alg` ebre, chapitre VIII, Hermann, 1958.
[6] N. Bourbaki, Groupes et alg` ebres de Lie, chapitre VI, Hermann/CCLS, 1975.
[7] N. Bourbaki, Groupes et alg` ebres de Lie, chapitre VIII, Hermann/CCLS, 1975.
[8] L. Breen, Tannakian categories, in Motives, Proc. Symposia pure Math. 55 (I), AMS, 1994, 337–
376.
[9] A. Brugui` eres, Th´ eorie tannakienne non commutative,Comm. in Algebra, 22(14) (1994), 5817–
5860.
[10] A. Brugui` eres, Tresses et structure enti` ere sur la cat´ egorie des repr´ esentations deSLN quantique,
Comm. in Algebra 28 (2000), 1989–2028.
[11] H. Cartan, S. Eilenberg, Homological algebra, Princeton Univ. Press, 1956.
[12] P. Cartier, Construction combinatoire des invariants de Vassiliev-Kontsevich des nœuds, C. R.
Acad. Sci. Paris 316 (1993), 1205–1210.
[13] J. Cuntz, D. Quillen, Algebra extensions and nonsingul arity, Journal A.M.S. 8 2 (1995), 251–
289.
[14] P. Deligne, Cat´ egories tannakiennes, in : The Grothendieck Festschrift, vol. 2, Birkh¨ auser P.M.
87 (1990), 111–198.
[15] P. Deligne et al., Quantum ﬁelds and strings : a Course for Mathematicians, AMS, 1999.
[16] P. Gabriel, Des cat´ egories ab´ eliennes, Bull. Soc. Math. France 90 (1962), 323–448.
[17] P. Gabriel, Probl` emes actuels de th´ eorie des repr´ esentations, L’Ens. Math.20 (1974), 323–332.
[18] J. Giraud, Cohomologie non ab´ elienne, Springer, 1971.
[19] A. Grothendieck, Sur quelques points d’alg` ebre homol ogique, Tohoku Math. J. (2), 9 (1957),
119–221.
[20] V . Ginzburg, Principal nilpotent pairs in a semisimple Lie algebra. I, Invent. Math. 140 (2000),
511–561.
[21] V . Guletskii, C. Pedrini, The Chow motive of the Godeaux surface, pr´ epublication (2001).
[22] D. Happel, Triangulated categories in the representation theory of ﬁnite dimensional algebras,
London Math. Soc. Lect. notes 119 (1988), Cambridge Univ. Press.
[23] G. Higman, On a conjecture of Nagata, Proc. Camb. Philos . Soc. 52 (1956), 1–4.
[24] N. Jacobson, Ann. of Math. 36 (1935), 875–881.
[25] U. Jannsen, Motives, numerical equivalence and semi-s implicity, Invent. Math. 107 (1992),
447–452.
[26] U. Jannsen, Equivalence relations on algebraic cycles , in The arithmetic and geometry of alge-
braic cycles (Banff, AB, 1998), 225–260, NATO Sci. Ser. C Math. Phys. Sci., 548, Kluwer Acad.
Publ., Dordrecht, 2000.
[27] A. Joyal, R. Street, Braided monoidal categories, Adv. in Math. 102 (1993), 20–78.
[28] C. Kassel, M. Rosso, V . Turaev, Quantum groups and knot invariants , S.M.F. Panoramas et
synth` eses5 (1997).
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 143
[29] N. Katz, W. Messing, Some consequences of the Riemann hy pothesis for varieties over ﬁnite
ﬁelds, Invent. Math. 23 (1974), 73–77.
[30] G. M. Kelly, On the radical of a category, J. Australian M ath. Soc. 4 (1964), 299–307.
[31] O. Kerner, A. Skowro´ nski, On module categories with nilpotent inﬁnite radical, Compos. Math.
77 3 (1991), 313–333.
[32] S.I. Kimura, Chow motives can be ﬁnite-dimensional, in some sense, ` a paraˆ ıtre au J. of Alg.
Geom.
[33] B. Kostant, The principal three-dimensional subgroup and the Betti numbers of a complex sim-
ple Lie group, Amer. J. Math. 81 (1959), 973–1032.
[34] K. K¨ unneman, On the Chow motive of an abelian scheme, in : Motives, Proc. Symposia pure
Math. 55 (I), AMS, 1994, 189–205.
[35] P.Y . Leduc, cat´ egories semi-simples et cat´ egories primitives, Canad. J. Math. 20 (1968), 612–
628.
[36] S. Mac Lane, Categories for the working mathematician, 2` eme ´ ed., Springer GTM5 (1998).
[37] G. A. Margulis, Discrete subgroups of semisimple Lie groups, Springer, Berlin, 1991.
[38] B. Mitchell, Rings with several objects, Adv. Math. 8 (1972), 1–161.
[39] V .V . Morozov, Sur un ´ el´ ement nilpotent dans une alg` ebre de Lie semi-simple (en russe), Dokl.
Akad. Nauk SSSR 36 (1942), 83–86.
[40] V .V . Morozov, Sur le centralisateur d’une sous-alg` ebre semi-simple d’une alg` ebre de Lie semi-
simple (en russe), Dokl. Akad. Nauk SSSR 36 (1942), 259–261.
[41] J.P. Murre, On a conjectural ﬁltration on the Chow group s of an algebraic variety, parts I and II,
Indag. Math. 4 (1993), 177–201.
[42] M. Nagata, On the nilpotency of nil-algebras, J. Math. S oc. Japan 4 (1952), 296–301.
[43] M. Nathanson, Classiﬁcation problems in K-categories, Fund. Math.105 3 (1979/80), 187–197.
[44] P. O’Sullivan, lettres aux auteurs, 29 avril et 12 mai 2002.
[45] D. I. Panyushev, Nilpotent pairs in semisimple Lie alge bras and their characteristics, Internat.
Math. Res. Notices 2000 1–21.
[46] A. Piard, Indecomposable representations of a semi-di rect product sl(2) ⋉ A and semi-simple
groups containing sl(2) ⋉ A, in : Sympos. Math. XXXI (Roma, 1988), 185–195, Acad. Press,
1990.
[47] Platon, Ph´ edon, § LIII.
[48] N. Popescu, Abelian categories with applications to rings and modules, Acad. Press, 1973.
[49] M. Prest, Model theory and modules , L.M.S. Lecture note series 130, Cambridge Univ. Press
1988.
[50] C. M. Ringel, Recent advances in the representation the ory of ﬁnite dimensional algebras, in
Representation theory of ﬁnite groups and ﬁnite-dimension al algebras, Birkh¨ auser Progress in
Math. 95 (1991).
[51] L. Rowen, Ring theory, vol. 1, Acad. Press, 1988.
[52] W. Rump, Doubling a path algebra, or : how to extend indec omposable modules to simple
modules, in : Representation theory of groups, algebras and orders (Costant ¸a, 1995), An. S ¸tiint ¸.
Univ. Ovidius Constant ¸a Ser Mat.4 2 (1996), 174–185.
[53] N. Saavedra Rivano, cat´ egories tannakiennes, Lect. Notes in Math. 265, Springer, 1972.
[54] J.-P. Serre, G` ebres, L’Ens. Math.39 (1993), 33–85.
[55] J.-P. Serre, Propri´ et´ es conjecturales des groupes de Galois motiviques et des repr´ esentations
l-adiques, in Motives, Proc. Symposia pure Math. 55 (I), AMS, 1994, 377–400.
144 YVES ANDR ´E ET BRUNO KAHN
[56] D. Simson, A. Skowro´ nski, The Jacobson radical power s eries of module categories and the
representation type, Bol. Soc. Mat. Mexicana 5 2 (1999), 223–236.
[57] R. Street, Ideals, radicals and structure of additive c ategories, Appl. Cat. Structures 3 (1995),
139–149.
[58] R. Thomason, The classiﬁcation of triangulated catego ries, Compos. Math. 105 (1997), 1–27.
[59] V . V oevodsky, A nilpotence theorem for cycles algebrai cally equivalent to zero, International
Mathematics Research Notices 4 (1995), 1–12.
[60] P. V ogel, Invariants de Witten-Reshetikin-Turaev et th´ eories quantiques des champs, in : Panora-
mas et synth` eses7 (1999), 117-143.
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 145
INDEX TERMINOLOGIQUE
A-id´ eal ` a gauche . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . 1.3.4, 1.3.10, 6.2.1
A-module (` a gauche) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1.3.3, 1.3.10, 2.1.1, 11.1, appendice A
A-bimodule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11.1
anneau de repr´ esentations . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . .10.2.1, 20.2
artinien . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . 2.1.2, 2.3.2, 2.3.4, A.2.1, A.2.3
auto-dual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . 1.4.4, 2.1.2, 2.2.6, 2.3.2, 19.5.2
Auslander (alg` ebre d’) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17.2
biproduit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1
compact . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3.5, 5.1.3, 5.2.2, 5.2.5, 5.3.1, 5.3.2, 14.1.3
compl´ ement unipotent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19.3.2
conservatif . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4.4, 1.4.7, 1.4.8, 2.3.4, 5.2, 7.1.6, 19.4.6, A.2.14
coproduit (de cat´ egories) . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A.2.2
cor´ etraction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . 1.4.4, 1.4.9, 7.1.3
dimension (rigide) . . . . . . . . . . . . . 7.1, 7.2.4, 7.2.7, 7.3.1, 7.3.2, 8.1.2, 8.1.3, 8.2.4, 8.3, 9.1.7, 9.2.1
dimension ﬁnie au sens de Kimura . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1.1
dimension de Kimura (ou kimension) . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1.13
dual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. 5.2.1, 6.1, 10.2.1, 13.8.3, 14.1.3, 17.1.2
enveloppe pro-semi-simple . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17.1
enveloppe r´ eductive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20.1.2
enveloppe pro-r´ eductive . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19.3.2
´ epaisse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1.2
faiblement (exact, ´ epi) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . .19.2.1, 19.4.4, 19.4.5
gerbe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . 14.2.1, 18.2.5,
groupe ` a conjugaison pr` es . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . 19.1, 19.3.2
h´ er´ editaire . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17.3
Hochschild (homologie) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . 10.2, 11.2.1
Hochschild (cohomologie) . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11.2
id´ eal (bilat` ere) d’une cat´ egorie additive . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3
indice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2.7
K-cat´ egorie,K-foncteur, K-lin´ eaire . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . 1.1
Kimura (cat´ egorie de) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9.1.16
mono¨ ıdal (id´ eal) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1.1
mono¨ ıdal (foncteur) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13.1
Morita (´ equivalence de) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3.9
pr´ esentation ﬁnie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3.7
produit local (de cat´ egories) . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A.2.2
proﬁnie (alg` ebre) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17.1
pseudo-ab´ elien . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1
puissance ext´ erieure, sym´ etrique . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2.3
radical . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4.1
⊗ -radical . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .7.4.1
radical inﬁni . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.1
radiciel (mon mari) . . . . . . . . . . . . . . . . . . . . . . 1.4.6, 2.1.5,2.3.4, 3.1.2, 4.1.4, 12.2.1, 13.7.1, 15.4.1
146 YVES ANDR ´E ET BRUNO KAHN
r´ etraction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4.4, 1.4.9
rigide . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1, 7.1.4, 8.2, 8.1.2, 8.1.1, 7.1.7, 8.2.2, 8.3.1, 10.1, 18.1.1
semi-primaire . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .2.3.1
semi-simple . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . 2.1.1, A.2.1
s´ eparable (cat´ egorie) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2.6
simple (objet, cat´ egorie) . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A.2.1
sorite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13.3
stricte (cat´ egorie mono¨ ıdale, foncteur mono¨ ıdal) . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13.4
strictement (semi-primaire, de Wedderburn, K-lin´ eaire)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.3
structure balanc´ ee . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . 15.3.4, 15.3.6
trace. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1, 7.2,
7.2.1, 7.2.6, 7.3.1, 7.3.3, 8.2, 10.1,10.2
tressage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1, 7.1, 7.1.4, 15.1, 15.2, 15.3.3, 15.3.5, 15.3.6
tressage inﬁnit´ esimal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . 15.3.6, 15.4.2
type de repr´ esentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . 3.1.1, 3.2, 3.2.1, 17.2, 17.3, 19.7
Wedderburn (cat´ egorie de) . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.4.1
D ´EPARTEMENT DE MATH ´EMATIQUES ET APPLICATIONS , ´ECOLE NORMALE SUP ´ERIEURE ,, 45
RUE D ’ULM, 75230 P ARIS CEDEX 05, F RANCE .
E-mail address: andre@dmi.ens.fr
INSTITUT DE MATH ´EMATIQUES DE JUSSIEU , 175–179 RUE DU CHEVALERET ,
75013 P ARIS , FRANCE .
E-mail address: kahn@math.jussieu.fr
39 E DGECLIFFE AVE, COOGEE , NSW 2034, A USTRALIA
E-mail address: pjosullivan@optusnet.com.au
