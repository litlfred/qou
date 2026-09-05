---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY"
section_id: sec-009-53-relation-with-the-blob-complex
section_title: "Relation with the Blob complex"
section_number: 5.3
pages: 47-55
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY — W e study the higher Hochschild chain functor, factorizatio n alge- bras and their relationship with topological chiral homolo gy."
---
the Blob complex of Morrison-Walker is equivalent to an unoriented variant of
topological chiral homology. We brieﬂy explain here how to deduce th is equivalence
from the proof of Theorem 5 and several statements from [29]. Th e main diﬀerence
with§ 5.1 and§ 5.2 to keep in mind is that we no longer assume our manifold to be
framed. Indeed, we are using the variant of topological chiral homology fo r (non-
necessarily framed nor oriented) manifolds of dimension n. However this forces us
to restrict our attention to unorientedEn-algebras:
48 G. GINOT, T. TRADLER, AND M. ZEINALIAN
Deﬁnition 5. The category of unoriented En-algebras, denoted EO(n)
n -Alg∞ is
deﬁned as the ((∞, 1)-)category of symmetric monoidal functors
EO(n)
n -Alg∞ := Fun⊗(Diskn, k-Mod ∞)
where Diskn is the category with objects the integers and morphism the spaces
Diskn(k,ℓ ) := Emb(∐
k Rn, ∐
ℓ Rn) of smooth embeddings of k disjoint copies of a
disk Rn into ℓ such copies; the monoidal structure is induced by disjoint union of
copies of disks.
Note that EO(n)
n -algebras are denoted EBn-algebras in [29].
Remark 15. The deﬁnition above is extracted from [25, 11]. There is an nat-
ural action of the orthogonal group O(n) on En-Alg∞, see [26]; the category
(En-Alg∞)hO(n) ofO(n)-homotopy ﬁxed points is equivalent to the (∞, 1)-category
EO(n)
n -Alg∞ of Deﬁnition 5 In particular, any CDGA is an unoriented En-algebra.
If one replaces the action of O(n) by SO(n),one recovers the notion of oriented
En-algebras which are commonly known as framedEn-algebras in the literature.
Let M be a dimension n manifold. By [29, Example 6.2.10], an EO(n)
n -algebra
A deﬁnes an A∞-n-category6CA and thus yields the Blob complex B∗(M,CA),
see [29, Deﬁnition 7.0.1]. Similarly we can form the topological chiral hom ology∫
MA, see [11, Deﬁnition 3.15] (or [25, 26]).
Proposition 12. LetM be a closedn-dimensional manifold (non necessarily framed
nor oriented) and A an EO(n)
n -algebra. There is an natural equivalence∫
M
A ∼= B∗(M,CA)
in k-Mod ∞. Further, if A is a CDGA, there is an natural equivalence CH •
M (A)∼=∫
MA in k-Mod ∞.
Proof. According to [29, Theorem 7.2.1], the Blob complex B∗(M,CA) satisﬁes
the excision property for closed manifolds and can be computed usin g a colimit
construction ([29, § 6.3]) similar to Deﬁnition 4. It also converts disjoint union
of manifolds to tensor products [29, Property 1.3.2] and B∗(Dn,CA)∼= A by [29,
Property 1.3.4] (and [29, Example 6.2.10]). The same properties hold f or topological
chiral homology as in Proposition 11 (or Lemma 8), the proofs and re ferences to [11,
25, 26] in the unoriented case being essentially the same as in the fra med one (using
O(n)-homotopy ﬁxed En-algebras). It follows that one can apply mutatis mutandis
the proof of Theorem 5 to get the equivalences stated in the propo sition. □
Remark 16. Let A = C•(ΩnY ) be the En-algebra associated to the n-fold loop
space of an n-connective pointed space Y . The Blob complex B∗(M,CC•(Ω nY ))
for non-necessarily closed manifolds shall not be mistaken with the B lob complex
associated to the A∞-n-category associated to the fundamental groupoid of the
space Y in [29, § 6] (though the construction share some similarities). Indeed,
it is claimed [29, Theorem 7.3.1] that the latter construction compute the chains
on the space of all maps Map( M,Y ), while the ﬁrst one, by non-abelian Poincar´ e
6this is, for n = 1, an instance of the linear category with a single object as sociated to an
associative algebra and, for general n, a slight variant of the construction of an ( ∞ , n)-category
Bn(A) associated to an En-algebra A as in [11]
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 49
duality [25],
∫
M ΩnY is the chains on the space of maps with compact support
Mapc(M,Y ).
Theorem 6 below and Proposition 12 suggest that the blob complex sh ould be
closely related to Factorization algebras as well. It would be interest ing to relate
system of ﬁelds, n-category and the blob complex in the sense of [2 9] to factorization
algebras (with extra properties) in the sense of [8]. We plan to invest igate these
relationship in a future work.
5.4. T opological chiral homology as a factorization algebra. In this sec-
tion we give a precise relationship between factorization algebras, t opological chiral
homology for (stably) framed manifolds, and En-algebras.
5.4.1. Topological chiral homology and factorization algebras fo r n-framed mani-
folds. For any manifold M of dimension m which is n-framed ( i.e. M×Dn−m is
framed) and En-algebra A, we can consider the topological chiral homology
∫
MA
as well as
∫
UA for every open subset U inM (equipped with the induced framing).
Further, if U1,...,U k are pairwise disjoint open subsets of V ∈Op(M ), there is a
canonical equivalence ([25, Theorem 3.5.1])
∫
U1
A⊗···⊗
∫
Uk
A
≃
−→
∫
U1∪···∪Uk
A
and a natural map
∫
U1∪···∪Uk
A→
∫
V A (since any ball in ⋃ Ui is a ball in V ).
Composing these two maps yield natural maps of Em−n-algebras
(24) µU1,...,Uk,V :
∫
U1
A⊗···⊗
∫
Uk
A −→
∫
V
A.
Proposition 13. LetM be an n-framed manifold of dimension m.
(1) For any En-algebraA, the rule U↦→
∫
UA (for U open in M ) together with
the structure maps µU1,...,Uk,V (24) deﬁne a locally constant factorization
algebraTC M (−,A ) on M , such that TC M (U,A ) =
∫
UA is canonically an
En−m-algebra for any open U .
(2) The ruleA↦→TCM (−,A ) deﬁnes a functorTC M :En-Alg∞→FacM (En−m-Alg∞)
which ﬁts into the following commutative diagram
En-Alg∞
∫
M /d47/d47
T C M
/d15/d15
En−m-Alg∞
FacM (En−m-Alg∞)
HF (−)
/d52/d52✐✐✐✐✐✐✐✐✐✐✐✐✐✐✐✐✐
In other words topological chiral homology computes the factoriz ation homology
ofTC M .
The idea behind Proposition 13 is that for any submanifold U of M and En-
algebraA, we can cover U by a (coherent family of) open balls on which A deﬁnes
a locally constant factorization algebra. Gluing these data deﬁnes a factorization
algebra on U whose homology can be computed from the balls by using the glu-
ing/locality lemma given above (Lemma 5). Since the topological chiral homology
is equivalent to A on balls and satisfy a similar locality axiom, they agree on U .
50 G. GINOT, T. TRADLER, AND M. ZEINALIAN
Proof of Proposition 13. For any open subset V ofM , the topological chiral homol-
ogy
∫
V A is the colimit lim−→ψV , where ψV :N (Disj(V ))→k-Mod ∞ is the diagram
given by the formula ψV (V1∪···∪ Vn) =
∫
V1
A⊗···⊗
∫
Vn
A whereV1,...,V n are dis-
joint open sets homeomorphic to a ball (Deﬁnition 4). In particular, the structure
mapsµU1,...,Un,V are induced by a map of colimits and it is easy to check that they
are natural with respect to open embeddings and thus deﬁnes a pr efactorization
algebra. Hence TC M (−,A ) is functorially (in A) a prefactorization algebra on M
with value in En−m-algebras.
To prove thatTC M (−,A ) is actually a factorization algebra, the idea is ﬁrst to
use a handle body decomposition to deﬁne another locally constant f actorization
algebraFM on M whose factorization homology HF (F,M ) is equivalent to
∫
MA
and then to prove that this factorization algebra is indeed equivalen t to TC M .
Note that by Lemma 4, if FM is a locally constant factorization algebra on M
with value in Ed-algebras such that
∫
MA∼=HF (FM,M ), then we have a natural
factorization algebraFM×Rd onM× Rd and further HF (FM×Rd,M× Rd)∼=
∫
MA
as an Ed-algebra.
We start with the case of open balls. By deﬁnition of topological chira l homology,
for every manifold B homeomorphic to an m-dimensional ball, there is a natural
equivalence
∫
BA ∼= A of En−m-algebras (where the En−m-algebra structure of
A is by restriction of structure), see [25, 26]. By a result of Lurie [25 ] (also see
[9, Proposition 3.4.1] or Proposition 10), there is a locally constant fa ctorization
algebraFB on B whose factorization homology is isomorphic to A.
We now prove that the factorization algebra FB is equivalent toTC B, i.e., that
there are equivalences of prefactorization algebras FB(U )∼=
∫
UA (for any open
subset U ⊂ B). Note that FB(U ) ∼= FB |U (U ) ∼= HF (FB |U,U ). To shorten
notation, we denoteFU the factorization algebra FB |U induced on U by restriction
ofFB to U . One has A⊗n ∼=
∫
U1
A⊗···
∫
Ul
A∼=
∫
U1∪···∪Ul
A for any pairwise
disjoint open subsets U1,...,U n of B homeomorphic to a ball ([25]) and
FB
( l∐
i=1
Bi
)
∼=
l⨂
i=1
FB(Bi) ∼=
l⨂
i=1
A
for any open balls Bi⊂ B (sinceFB is locally constant). Hence FB(U )∼=
∫
UA
when U is a disjoint union of balls. In particular, this equivalence holds for any
(framed) embedding of S0×Dm in B. We now prove, by induction on i, that
FB(Si×Dm−i) ∼= HF (FSi×Dm−i,Si×Dm−i) ∼=
∫
Si×Dm−i
A
for any embedding of Si×Dm−i in B (where i≥ 1). We have a decomposition
of the sphere Si×Dm−i as Si×Dm−i∼= D+∪Si−1×Di−m×D1 D− where D+ and
D− are homeomorphic to framed open subballs of B. By above, the factorization
homology ofFD+ andFD− are equivalent to A and the factorization homology of
FSi−1×Di−m×D1 is equivalent to
∫
Si−1×Di−mA as an E1-algebra by the induction
hypothesis. Now the equivalence HF (FSi×Dm−i,Si×Dm−i)∼=
∫
Si×Dm−iA follows
from Lemma 5 and Proposition 11. This completes the inductive step. For general
open submanifold U of B, we use a handle decomposition as in the proof of The-
orem 5 (using Lemma 5 instead of Theorem 1 and arguments similar to w hat has
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 51
just been explained above for spheres) to obtain, in a similar way, th at
∫
U
A ∼= HF
(
FU,U
) ∼= F (U ).
This proves that TC B∼=FB and thus that TC B is a factorization algebra.
IfM = ∐ l
i=1Bi is a disjoint union of balls of dimension m, then we also deduce
thatTC M is a factorization algebra since
∫
U1
A⊗···⊗
∫
Ul
A∼=
∫
U1
∐ ··· ∐ Ul
A for
any open subsets Ui⊂Bi. In particular, this applies to the case of S0×Dd (d≥ 0).
Now let M∼=Sm×Dd (d≥ 0,m≥ 1) be framed (we do not assume it is embedded
as an open set of an euclidean space). We work by induction on m so that we may
assume the result of the proposition is known for Sm−1×Dl.
Assume we have a cover U∪V of a space X and factorization algebras BU ,BV ,
BU∩V on U , V and U∩V with equivalences BU∩V
≃
−→B U |U∩V andBU∩V
≃
−→
BV |U∩V . Then we can glue these factorization algebras to deﬁne a factoriz ation
algebra onX, see [8] (note that this descent property can be generalized to ar bitrary
covers). We wish to apply this to a decomposition of the m-sphere Sm as Sm∼=
D+∪Sm−1×D1 D− where D+ and Dm are homeomorphic to framed open balls.
By the above analysis, there are locally constant factorization alge brasF+,F− on
D+×Dd and D−×Dd which are equivalent to TC Dm+d (A). Restricting these
equivalences to Sm−1×D1×Dd, we get an equivalence
F+|Sm−1×D1×Dd
≃
−→F −|Sm−1×D1×Dd.
Since Sm−1×D1×Dd is the intersection of D+×Dd with D−×Dd, we thus get
a locally constant factorization algebra F on their union Sm×Dd. It follows from
Lemma 5 and Proposition 11, that F (Sm×Dd)∼=
∫
Sm×DdA as an Ed-algebra.
The equivalences F (U )∼=
∫
UA follows for any open proper subset of Sm×Dd
by the above case for open balls (or by mimicking the proof). It follow s that
TC Sm×Dd∼=F and thus is a factorization algebra.
The case of general n-framed manifolds M is done similarly. Using a handle de-
composition, induction and the descent property of factorization algebras we build
a locally constant factorization algebra FM onM and then prove, by using handle
decomposition of any open subset U of M , that FM (U )∼=
∫
UM ; the argument is
similar to the case of spheres (as in the proof of Theorem 5).
The factorization algebra TC M (−,A ) is locally constant by construction (since∫
BA∼=A for any ball B) and its factorization homology is precisely the topological
chiral homology of M with value in A. FurtherTC M (−,A ) is functorial in A since
topological chiral homology is. □
Remark 17. Theorem 5 follows easily from Proposition 13 and Corollary 9.
5.4.2. Topological chiral homology and factorization algebras fo r En[M ]-algebras.
We now go beyond the notion of n-framed manifolds M , and, more generally,
consider locally constant algebras over an operad En[M ], for which there might not
exist a globally deﬁned En-algebra.
Following Lurie [25], topological chiral homology can also be deﬁned for a (locally
constant) family of En-algebras parametrized by the points in M×Dm−n even if
M is not n-framed. Such families objects are (locally constant) algebras ove r an
(∞-)operad En[M ] := E⊗
M×Dn−m , the operad of little n-cubes in M×Dm−n, see [25,
52 G. GINOT, T. TRADLER, AND M. ZEINALIAN
Deﬁnition 5.2.4.1] (here M is still of dimension m, and of course one can choose
m = n). Note that there is a canonical map of ∞-operads from En[M ] to the
the operad Comm governing CDGAs. Thus a CDGA is an En[M ]-algebra in a
canonical way.
By [25, Theorem 5.2.4.9], we can also describe an En[M ]-algebra as a locally
constant N (Disk(M×Dn−m))-algebra. Indeed, by [25, Remark 5.3.2.7] we can
extend Deﬁnition 4 to an En[M ]-algebraA as well by replacing the last equivalence
in (17) by A(V1)⊗···⊗A (Vn). That is, there is an equivalence
(25)
∫
M
A ∼= lim−→
∫
V1
A⊗···⊗
∫
Vn
A∼= lim−→A(V1)⊗···⊗A (Vn)
where V1,...,V n are disjoint open sets homeomorphic to a ball.
Lemma 8 (Lurie [25]) . LetM be a manifold and A be an E[M ]-algebra. Assume
that there is a codimension 1 submanifold N of M with a trivialization N×D1 of
its neighborhood such that M is decomposable as M =X∪N ×D1Y whereX,Y are
submanifolds of M glued along N×D1. Then
(1) ∫
N ×D1A is an E1-algebra and ∫
XA and ∫
YA are right and left modules
over
∫
N ×D1A.
(2) The natural map
∫
X
A
L
⊗∫
N ×D1 A
∫
Y
A −→
∫
M
A
is an equivalence.
Proof. The lemma is explained in [25] after Theorem 5.3.4.14 (where
∫
N ×D1A is
simply denoted by
∫
NA). Let us give some more details. There is a homeomorphism
N×D1∼=N× (0, 1) and similarly (since X has a neighborhood homeomorphic to
N×D1) a homeomorphism X∼= X0 where X0 = X\N× [0, 1) (we also denote
Y0 = Y \N× (−1, 0]). Since N× (−1, 0) and N× (0, 1) are disjoint open sets
in N×D1, we get a natural map
∫
X0
A⊗
∫
N ×(0,1)A→
∫
XA. Then the module
structure on
∫
XA is given the composition
∫
X
A⊗
∫
N ×D1
A
≃
−→
∫
X0
A⊗
∫
N ×(0,1)
A−→
∫
X
A
and similarly for the module structure of
∫
YA and the E1-structure of
∫
N ×D1A.
For the second statement, we need to prove that the canonical m ap
(26) lim −→
( ∫
X
A⊗
∫
N ×D1
A⊗
∫
Y
A ⇒
∫
X
A⊗
∫
Y
A
)
−→
∫
M
A
induced by the two module structures is an equivalence. Using the eq uivalences
of modules ∫
X0
A
≃
→ ∫
XA, ∫
Y0
A
≃
→ ∫
YA and Deﬁnition 4 (or more precisely the
equivalence (25)), the left hand side of the map (26) is computed by the colimit
lim−→
U1,...,U ℓ ∈ ~Ball
pairwise disjoint
∫
U1
A⊗···⊗
∫
Uℓ
A
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 53
where ~Ball is the set of open sets U∈Op(M ) homeomorphic to a ball such that U
is either in X0 or Y0 or in N×D1. Thus, denoting Ball (M ) the set of open sets
homeomorphic to a ball in M , we are left to prove that the canonical map
(27)
lim−→
U1,...,U ℓ ∈ ~Ball
pairwise disjoint
∫
U1
A⊗···⊗
∫
Uℓ
A−→ lim−→
V1,...,V i ∈ B all (M)
pairwise disjoint
∫
V1
A⊗···⊗
∫
Vi
A→
∫
V
A
is an equivalence. For every family B1,...,B k of pairwise disjoint open subsets
of M homeomorphic to a ball which intersects N×{ 0}, choosing a point xj in
each Bj∩
(
N×{ 0}
)
, we can ﬁnd disjoint open subsets (homeomorphic to a ball)
U1,...,U k included in N×D1, such that Uj containsxj and is included in Bj. The
inclusion map Uj֒→Bj induces a canonical morphism
∫
Uj
A→
∫
Bj
A which is an
equivalence since there is a natural equivalence
∫
BA∼= A for any ball. It follows
that the map of (homotopy) colimits (27) is an equivalence. □
The generalization of Proposition 13 to En[M ]-algebras is:
Theorem 6. LetM be a manifold of dimension m and d∈ N an integer.
(1) The rule A↦→
(
U ↦→
∫
UA
)
deﬁnes a functor of (∞, 1)-algebrasTC M :
Ed[M ]-Alg→Faclc
M (Ed-Alg) which ﬁts into a commutative diagram
Ed[M ]-Alg
∫
M /d47/d47
T C M
/d15/d15
Ed-Alg∞
Faclc
M (Ed-Alg∞)
HF (−)
/d53/d53❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥
(2) The functor TC M : Ed[M ]-Alg → Faclc
M (Ed-Alg) is an equivalence of
(∞, 1)-categories.
In particular, any locally constant factorization algebra F on M with values
in Ed-algebras is equivalent to TC M (A) for a unique (up to equivalences) Ed[M ]-
algebraA, i.e., . algebra over the operad of little cubes in M×Dd. Further,
topological chiral homology of an open set U with value in the associated E⊗
M×Dd -
algebra computes the (derived) sections of the factorization alge bra.
Also note that if M is any manifold and A is a CDGA, viewed as an Ed[M ]-
algebra, then the factorization algebra TC M (A) induced by Theorem 6 is strongly
constant in the sense of Section 4.2. Thus by Corollary 9, there is an natural
equivalence of (Ed-algebras)
∫
M
A ∼= CHM (A)
extending Theorem 5 to non-framed manifolds.
Proof of Theorem 6. We ﬁrst deal with assertion (1). By Lemma 4, it is enough to
prove that the rule U↦→
∫
UA, together with the structure maps
(28)
∫
U1
A⊗···⊗
∫
Uℓ
A
∼
−→
∫
U1∪···∪Uℓ
A−→
∫
V
A
54 G. GINOT, T. TRADLER, AND M. ZEINALIAN
forUi’s pairwise disjoint open subsets ofV ∈Op(M×Dd), deﬁnes a locally constant
factorization algebra on M×Dd, naturally in A∈ E⊗
M×Dd -Alg. Note that, by [25,
Theorem 5.2.4.9], the E⊗
M×Dd -algebraA satisﬁes that, for any ball B which is a
subset of a ball B′, the canonical map
∫
BA∼=A(B)→A (B′)∼=
∫
B′A is an equiv-
alence in k-Mod ∞. Now we can apply the same proof as the one of Proposition 13
withA instead of A, using Lemma 8 instead of Proposition 11.
We now prove assertion (2). By [25, Theorem 5.2.4.9], the canonical e mbed-
ding θ : E⊗
M×Dd -Alg → N (Disk(M× Rd))-Alg induces an equivalence between
E⊗
M×Dd -Alg and locally constantN (Disk(M×Rd))-algebras; we writeN (Disklc(M ))-Alg
for the latter subcategory. It is thus enough to deﬁne a functor EAM :Faclc
M (Ed-Alg∞)→
N (Disklc(M ))-Alg such thatTC M◦EAM andEAM◦TC M are respectively equiva-
lent to the identity functors of Faclc
M (Ed-Alg∞) and N (Disklc(M ))-Alg. Let F be
in Faclc
M (Ed-Alg∞). By Lemma 4, we can think of F as a locally constant factor-
ization algebra on M×Dd. Let B∈Op(M×Dd) be homeomorphic to a ball. Then
the restriction F|B is a locally constant factorization algebra on B∼= Rn, thus is
equivalent to an En-algebra (which is canonically equivalent to F (B)). Further, for
any ﬁnite family B1,...,B ℓ of pairwise disjoint open subsets homeomorphic to a
ball and U an open subset homeomorphic to a ball containing the Bi’s, the locally
constant factorization algebra structure deﬁnes a canonical ma p
γB1,...,Bl,U :F (B1)⊗···⊗F (Bℓ)−→F (U )
which is an equivalence if ℓ = 1. The maps γB1,...,Bl,U are compatible in a natural
way. This shows that the collection F (B) for all open sets B⊂ M×Dd home-
omorphic to a ball is a locally constant N (Disk(M× Rd))-algebra, denoted AF
and we deﬁne the functor EAM to be deﬁned by EAM (F ) := AF (for M = pt it
is the same as the functor for deﬁned in the proof of Proposition 10). In other
words, the functorEAM (F ) is simply induced by the composition Disk( M× Rd)֒→
Op(M×Rd)
F
→k-Mod ∞. By abuse of notation, we also write AF for the associated
(well deﬁned up to equivalences) E⊗
M×Dd -algebra.
LetA be an E⊗
M×Dd -algebra. By construction EAM◦TC M (A) is the (locally
constant) N (Disk(M× Rd))-algebra given, on any (open set homeomorphic to an
euclidean) ball B, by
(
EAM◦TC M (A)
)
(B) =
∫
B
A∼=A(B)
by deﬁnition of topological chiral homology [25, Example 5.3.2.8]. Hence there is a
canonical equivalenceEAM◦TC M (A)∼=A of locally constant N (Disk(M× Rd))-
algebras and thus of E⊗
M×Dd -algebras as well.
It remains to prove that, there are natural equivalences TC M (AF )∼=F of fac-
torization algebras, where AF is the E⊗
M×Dd -algebraEAM (F ) associated to F as
above. Fixing a Riemannian metric on M×Dd, we can ﬁnd a cover Ballg(M×Dd)
of M given by open sets in M×Dd which are geodesically convex. On every
U∈B allg(M× Rd), the restrictions TC |U (AF ) and F|U are naturally isomorphic
by the above paragraph. In particular, for any set UI := ⋂
i∈IUi and any subset
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 55
J⊂I, the following diagram
TC |UI (AF ) ≃ /d47/d47
/d15/d15
F|UI
/d15/d15
TC |UI\J (AF ) ≃ /d47/d47F|UI\J
is commutative. Since TC M (AF ) and F are the factorization algebras obtained
by descent from their restrictions on the cover Ballg(M× Rd), on which they are
naturally equivalent, it follows that F is equivalent to TC M (AF ). □
Example 12. SinceS2×D1 embeds as an open set in R3, anyE3-algebraA yields,
by restriction, a (locally constant) factorization algebra AS2 on S2 (with values in
E1-Alg) (Lemma 4). By Theorem 6 and Proposition 11, decomposing the sph ere as
two disks glued along the equator, we get that the factorization ho mology of AS2
is given by
HF (AS2 ) ∼= A
L
⊗
CHS1 (A)
A
as an E1-algebra. Here CHS1 (A) is the usual Hochschild chain complex of the
(underlying) E1-algebra structure of A, which is naturally an E2-algebra by [25,
Theorem 5.3.3.11] and Proposition 11.
Similarly, any E2-algebraB yields a (translation invariant and locally constant)
factorization algebra on R2, and thus a (locally constant) factorization algebra BT
on a torus T =S1×S1∼= R2/Z2. Since T is framed, we can also deﬁne its topologi-
cal chiral homology directly using the framing. It follows easily from t he uniqueness
statement in Theorem 6, that BT is equivalent to TC T (B) in FacT (k-Mod ∞).
Note that the two canonical projections p1,p 2 : R2 → R deﬁne two locally
constant factorization algebras p1∗(B), p2∗(B) on R and thus, two E1-algebras B1
and B2. Now, cutting the torus along two meridian circles, we get two copies of
S1×D1∼= R2/(Z⊕{ 0}) glued along their boundaries. By Theorem 6 again, the
topological chiral homology of S1×D1 is the same as the factorization algebra
homology of the descent factorization algebra BZ⊕{0}. Thus
∫
S1×D1B is equivalent
to the usual Hochschild chain complex CHS1(B1) and the later complex inherits an
E1-structure from the E2-algebra structure of B. From Proposition 11, we deduce
a natural equivalence (in k-Mod ∞)
HF (BT )∼=CHS1 (B1)
L
⊗
CHS1 (B1)⊗(CHS1 (B1))op
CHS1(B1)∼=CHS1 (CHS1 (B1)).
Note that if B was actually a CDGA, then the later equivalence follows directly
from Corollary 11.
