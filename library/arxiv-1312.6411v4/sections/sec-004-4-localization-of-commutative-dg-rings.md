---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-004-4-localization-of-commutative-dg-rings
section_title: "Localization of Commutative DG Rings"
section_number: 4
pages: 19-24
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — We consider commutative DG rings (better known as nonpositive stronglycommutativeassociativeunitalDGalgebras)."
---
In this section we specialize to DG rings satisfying a commutativity condition.
Such a DG ringA can be localized onSpec ¯A.
Deﬁnition 4.1.Let A =⨁
i∈Z Ai be a DG ring.
(1) Aiscalled weaklycommutative if b· a = (−1)ij· a· bforall a∈ Aiand b∈ Aj.
(2) A is calledstrongly commutativeif it is weakly commutative, and ifa· a = 0
for alla∈ Ai with i odd.
(3) Aiscalleda commutativeDGring ifitisstronglycommutativeandnonpos-
itive.
If A is weakly commutative, then any left DGA-module M can be viewed as a
right DG A-module. The formula for the right action is this:m· a := (−1)ij· a· m
for a∈ Ai and m∈ Mj.
Thefullsubcategoryof DGRonthecommutativeDGringsisdenotedby DGR≤0
sc .
Convention 4.2. By default, all DG rings from here on in the paper are commu-
tative (Deﬁnition 4.1(3)), unless explicitly stated otherwise; i.e. we work inside
DGR≤0
sc . In particular all rings are commutative by default.
Since our DG rings are now commutative, we can talk about cohomologically
pseudo-noetherian DG rings, instead of cohomologically left pseudo-noetherian
ones (Deﬁnition 1.18).
Remark 4.3. In [YZ1], and in earlier versions of this paper, we used the name
“super-commutative” for what we now call “strongly commutative”. The book
[ML] uses the term “strictly commutative”.
Of course when2is invertible in the ringA0 (e.g. in characteristic0), there is no
diﬀerence between weakly commutative and strongly commutative DG rings.
Thereadermaywonderwhywechosetoworkinthecategory DGR≤0
sc ofstrongly
commutativenonpositiveDGrings,andnotinthecategory DGR≤0
wc ofweaklycom-
mutative ones. Here is the reason.
Consider any nontrivial commutative base ringK (e.g. K = Z), and the cor-
responding slice categoryDGR≤0
sc /K. Let X be a set of nonpositive graded vari-
ables. The strongly commutative polynomial ring inX (see [Ye5, Deﬁnition 3.10])
is denoted byKsc[X]. It is easy to see thatKsc[X] is a ﬂatK-module. A DG ring
A∈ DGR≤0
sc /Kiscalledsemi-freeif A♮∼= Ksc[X]forsome X. Suchasemi-freeDG
ring A is a bounded above complex of ﬂatK-modules, and thus it is a K-ﬂat DG
K-module. We had shown in [YZ1] that there are enough semi-free resolutions in
DGR≤0
sc /K. Therefore there are enough K-ﬂat resolutions inDGR≤0
sc /K.
Ontheotherhand,letusexaminethecategory DGR≤0
wc /Z. Theweaklycommu-
tative polynomial ringZwc[x] over Z, in a single variablex of degree−1, has this
structure as a gradedZ-module:
Zwc[x] = Z⊕ (Z· x)⊕
( Z
(2)· x2)
⊕
( Z
(2)· x3)
⊕··· .
We see that it is not ﬂat overZ. Moreover, it is not hard to see that ifA is any
object inDGR≤0
wc /Z such that A♮∼= Zwc[x], then A is not a K-ﬂat DGZ-module.
Similarly,itseemsthatanysemi-freeobject A∈ DGR≤0
wc thathasanontrivialdegree
−1 component, also fails to be a K-ﬂat DGZ-module. The upshot is that, most
likely,there are not enough K-ﬂat resolutions inDGR≤0
wc /Z.
20 AMNON YEKUTIELI
Proposition 4.4. Let A be a DG ring. The action ofA0 on C(A) makes D(A) into an
¯A-linear category.
Proof. Let φ : M→ N be a morphism inC(A); namely φ is a degree0 cocycle
in the DG abelian groupHomA(M, N). For any a ∈ A−1, the homomorphism
d(a)· φ = d(a· φ) is a degree0coboundary inHomA(M, N), and so it vanishes in
the homotopy categoryK(A). Therefore K(A) is an ¯A-linear category, and hence
so is its localizationD(A). □
Deﬁnition 4.5.Let A be a DG ring, with canonical homomorphismπ : A→ ¯A =
H0(A). Given a multiplicatively closed subsetS of ¯A, the set˜S := π−1(S)∩ A0 is
a multiplicatively closed subset ofA0. Deﬁne the ringA0
S := ˜S−1· A0 (this is the
usuallocalization),andtheDGring AS := A0
S⊗A0 A. ThereisacanonicalDGring
homomorphism λS : A→ AS.
If S ={si}i∈N for some elements∈ ¯A, then we also use the notationAs := AS.
There is the usual localization ¯AS = S−1· ¯A of the ring ¯A w.r.t. S. We get
a graded ringH(A)S := ¯AS⊗ ¯A H(A). There are graded ring homomorphisms
H(A)→ H(A)S and H(λS) : H(A)→ H(AS).
Proposition 4.6. Let A be a DG ring andS⊆ ¯A a multiplicatively closed subset.
(1) There is a unique isomorphism of gradedH(A)-rings H(AS)∼= H(A)S.
(2) ForanyDG A-module Mthereisauniqueisomorphismofgraded H(AS)-modules
H(AS⊗A M)∼= H(A)S⊗H(A) H(M)
that is compatible with the homomorphisms fromH(M).
(3) If A is cohomologically pseudo-noetherian, then so isAS.
Proof. Items (1-2) are true because the ring homomorphismλS : A0→ A0
S is ﬂat.
Item (3) is an immediate consequence of (1-2). □
Deﬁnition 4.7.Let A be a ring, and leta = ( a1, . . . , an) be a sequence of elements
of A. We calla a covering sequenceof A if ∑n
i=1 A· ai = A.
Consider the spectrumSpec A of the ringA. For an elementa∈ A we identify
the principal open set{p∈ Spec A| a /∈ p} with the schemeSpec Aa, whereAa is
the localization ofA w.r.t. a. Clearly a sequencea = ( a1, . . . , an) in A is a covering
sequence iﬀSpec A =⋃n
i=1 Spec Aai.
Let A be a DG ring, and leta = ( a1, . . . , an) be a covering sequence of¯A. For
any strictly increasing sequencei = ( i0, . . . , ip) of length p in the integer interval
[0, n], i.e.1≤ i0 <··· < ip≤ n, we deﬁne the ring
(4.8) C(A0; a)(i) := A0
ai0
⊗A0···⊗ A0 A0
aip
,
where A0
a0, . . . , A0
ap are the localizations from Deﬁnition 4.5. Next, for anyp ∈
[0, n− 1] we let
(4.9) Cp(A0; a) :=
⨁
i
C(A0; a)(i) ,
wherethesumisonallstrictlyincreasingsequences ioflength p. Finallywedeﬁne
the DGA0-module
(4.10) C(A0; a) :=
n−1⨁
p=0
Cp(A0; a).
The diﬀerentialCp(A0; a)→ Cp+1(A0; a) is ∑i,k(−1)k· λi,k, wherei runs over the
strictly increasing sequences of lengthp + 1, k∈ [0, p + 1], ∂k(i) is the sequence
COMMUTATIVE DG RINGS 21
obtained from i by omitting ik, and λi,k : C (A0; a)(∂k(i)) → C(A0; a)(i) is the
canonical ring homomorphism.
Deﬁnition4.11.Let AbeaDGring,andlet a = ( a1, . . . , an)beacoveringsequence
of ¯A. For a DGA-module M, theČech DG moduleof M is the DGA-module
C(M; a) := C(A0; a)⊗A0 M.
There is a canonical DG module homomorphismcM : M→ C(M; a), sending
m∈ M to ∑i 1i⊗ m∈ C(M; a), where1i is the element1∈ A0
ai⊆ C0(A0; a).
Proposition 4.12. Let a = ( a1, . . . , an) be a covering sequence of¯A, and letM be a DG
A-module. Then the homomorphismcM : M→ C(M; a) is a quasi-isomorphism.
Proof. Since C(A; a) is a K-ﬂat DGA-module, and C(M; a)∼= C(A; a)⊗A M, we
seethat C(−; a)isatriangulatedfunctorfrom D(A)toitself. Thehomomorphism
cM is a quasi-isomorphism iﬀ it is an isomorphism inD(A).
Thecohomologicaldimensionofthefunctor C(−; a)isﬁnite: itisatmost n− 1.
According to Theorem 2.10(3) it suﬃces to check thatcM is a quasi-isomorphism
for M∈ Mod ¯A. But in this caseC(M; a)∼= C( ¯A; a)⊗ ¯A M, soC(M; a) is the usual
Čech complex for the covering ofSpec ¯A determined by the sequencea. In geo-
metric language (cf. [Ha, Section III.4]), writingX := Spec ¯A and Ui := Spec ¯Aai,
andlettingMdenotethequasi-coherent OX-modulecorrespondingto M,wehave
M∼= Γ(X,M) and C(M; a)∼= C({Ui},M). By [SP, Lemma 01X9], the homomor-
phism cM : M→ C(M; a) is a quasi-isomorphism. □
Remark 4.13. Actually the DGA-module C(A; a) has more structure. There is a
cosimplicial commutative ringCcos(A0; a), whose degreep piece is
Cp
cos(A0; a) := ∏
i
C(A0; a)(i),
where i = ( i0, . . . , ip)areweaklyincreasingsequencesin [1, n]. TheČechDGmod-
ule C(A0; a)isthestandardnormalizationof Ccos(A0; s),andassuchithasastruc-
tureofnoncommutativecentralDG A0-ring(whichisconcentratedinnon-negative
degrees). HenceC(A; a) is a noncommutative DG ring, andcA : A→ C(A; a) is a
DG ring quasi-isomorphism. See [PSY, Section 8].
Deﬁnition 4.14.Let A be a ring, and lete = ( e1, . . . , en) be a sequence of elements
of A. We calle an idempotent covering sequenceif eachei is an idempotent element
of A, ei· ej = 0 for i⁄= j, and1 = ∑n
i=1 ei.
Suppose e = ( e1, . . . , en) is an idempotent covering sequence of the ringA. Of
course e is a covering sequence in the sense of Deﬁnition 4.7. For anyi there is
a unique A-ring isomorphism Aei
∼= A/(1− ei)· A; namely the localization ofA
with respect to the elementei is also the quotient ring modulo the ideal generated
by the complementary idempotent1− ei. There is a ring isomorphism
(4.15) A ≃− →
n
∏
i=1
Aei .
The schemeSpec Aei is an open-closed subscheme ofSpec A, and
(4.16) Spec A =
n
∐
i=1
Spec Aei .
Deﬁnition 4.17.Let e = ( e1, . . . , en) be an idempotent covering sequence of the
ring A. Thee-induced decompositionof A is the ring isomorphism (4.15).
22 AMNON YEKUTIELI
Deﬁnition4.18. Let Abearing. Thesetoflocallyconstantfunctions f : Spec A→
Z (for the Zariski topology onSpec A) shall be denoted byFlc(Spec A, Z). It is an
abelian group by pointwise addition.
Proposition 4.19. Let A be a ring. There is a bijection between the setFlc(Spec A, Z),
and the set of pairs(e, k), consisting of an idempotent covering sequencee = ( e1, . . . , en)
of A, and a nondecreasing sequence of integersk = ( k1, . . . , kn). This bijection sends a
function f∈ Flc(Spec A, Z) to the pair(e, k) that satisﬁesf−1(ki) = Spec Aei.
Proof. Consider a locally constant functionf : Spec A→ Z. Then f is continuous
forthediscretetopologyon Z. Sincethetopologicalspace Spec Aisquasi-compact,
the image off must be ﬁnite. This gives rise to a ﬁnite decomposition ofSpec A
into open-closed subsets, which must be of the form (4.16) for some idempotent
covering sequencee. After suitable renumbering we get the pair(e, k).
The converse is clear. □
Example4.20. Often Spec Aofthering Ahasﬁnitelymanyconnectedcomponents;
say n of them. Prototypes are:
(1) A is a noetherian ring.
(2) A is a semilocal ring.
(3) Aistheringofcontinuous(resp.diﬀerentiable)functions X→ R,where X
isaconnectedtopologicalspace(resp.aconnecteddiﬀerentiablemanifold).
Here n = 1.
Anorderingoftheconnectedcomponentsof Spec Agivesrisetoanidempotent
covering sequencee = ( e1, . . . , en). The sequence of delta functions(δ1, . . . , δn) is
a basis of the groupFlc(Spec A, Z), which is thus isomorphic toZn.
Deﬁnition 4.21.Let A be a ring, and assume thatSpec A has ﬁnitely many con-
nected components. Aconnected component idempotent covering sequenceof A is an
idempotentcoveringsequence e = ( e1, . . . , en),suchthateach Spec Aei isnonempty
and connected.
Clearly a connected component idempotent covering sequence ofA is unique
up to permutation.
Proposition4.22. Let AbeaDGring,andlet e = ( e1, . . . , en)beanidempotentcovering
sequence of ¯A = H0(A). For anyi we have the localized DG ringAi := Aei from Deﬁni-
tion4.5,andtheDGringhomomorphism λi : A→ Ai. ThentheDGringhomomorphism
(λ1, . . . , λn) : A→ A1×···× An
is a quasi-isomorphism.
Proof. Let’s write¯Ai := ¯Aei = H0(A)ei, so ¯A = ∏n
i=1 ¯Ai. Using Proposition 4.6(1)
we obtain canonical graded ring isomorphisms
H(A)∼= ∏
n
i=1
( ¯Ai⊗ ¯A H(A)
)∼= ∏
n
i=1 H(Ai)∼= H
(
∏
n
i=1 Ai
)
.
The composition of these isomorphisms is exactlyH(λ1, . . . , λn). □
Corollary 4.23. With A1, . . . , An as in Proposition4.22, the restriction functorsrestλi :
D(Ai)→ D(A) induce an equivalence of triangulated categories⨁n
i=1 D(Ai)→ D(A).
Proof. This is standard. Cf. [YZ1, Proposition 1.4]. □
Deﬁnition 4.24.Let A be a DG ring, and lete∈ ¯A = H0(A) be an idempotent
element. Consider the localized DG ringAe corresponding to e, as in Deﬁnition
4.5. The triangulated functor
E : D(A)→ D(A) , E(M) := Ae⊗A M,
COMMUTATIVE DG RINGS 23
is called theidempotent functorcorresponding toe.
Deﬁnition 4.25.Let A be a DG ring, and lete = ( e1, . . . , en) be an idempotent
covering sequence ofSpec ¯A.
(1) The corresponding DG ring quasi-isomorphism
(λ1, . . . , λn) : A→ A1×···× An ,
from Proposition 4.22 is called thee-induced decompositionof A.
(2) The corresponding functorsE1, . . . , En from Deﬁnition 4.24 are called the
e-induced idempotent functorsof A.
(3) In caseSpec ¯A has ﬁnitely many connected components, ande is one of its
connected component idempotent covering sequence, then the expression
“e-induced” above is sometimes replaced by “connected component”.
Proposition4.26. Suppose e = ( e1, . . . , en)isanidempotentcoveringsequenceof ¯A. Let
E1, . . . , En be thee-induced idempotent functors.
(1) We haveEi◦ Ei∼= Ei, Ei◦ Ej = 0 for i⁄= j, and∑n
i=1 Ei∼= idD(A).
(2) UndertheequivalenceofcategoriesinCorollary 4.23, D(Ai)istheessentialimage
of Ei.
Proof. This is similar to the proof of Proposition 4.22, and is left to the reader.□
Proposition 4.27. Let f : A→ B be a DG ring homomorphism, and letM, N∈ D(B).
We write ¯f := H0( f ) and F := rest f : D(B)→ D(A). Assume that the ring homomor-
phism ¯f : ¯A→ ¯B is surjective. Lete = ( e1, . . . , en) be an idempotent covering sequence
of ¯B, let E1, . . . , En be the e-induced idempotent functors ofB, and writeMi := Ei(M)
and Ni := Ei(N). Then for anyi⁄= j we have
HomD(A)
(
F(Mi), F(Nj)
)
= 0.
Therefore we get a canonical isomorphism of¯A-modules
HomD(A)
(
F(M), F(N)
)∼=
n⨁
i=1
HomD(A)
(
F(Mi), F(Ni)
)
.
Proof. For anyi choose some elementai∈ ¯A such that ¯f (ai) = ei. Consider the
noncommutativerings EndD(B)(Mi)and EndD(A)(F(Mi)). Thereisacommutative
diagram (of noncommutative rings)
¯A //
¯f

EndD(A)(F(Mi))
¯B // EndD(B)(Mi) .
F
OO
Cf. Proposition 4.4.
Taketwodistinctindices i, j. Weknowthat ei· idMi = idMi in EndD(B)(Mi),and
ei· idMj = 0 in EndD(B)(Mj). Therefore ai· idF(Mi) = idF(Mi) in EndD(A)(F(Mi)),
and ai· idF(Mj) = 0 in EndD(A)(F(Mj)).
Consider any morphismφ : F(Mi)→ F(Nj) in D(A). Then
φ = idF(Mj)◦ φ◦ idF(Mi) = idF(Mj)◦ φ◦ (ai· idF(Mi))
= ( ai· idF(Mj))◦ φ◦ idF(Mi) = 0.
□
24 AMNON YEKUTIELI
