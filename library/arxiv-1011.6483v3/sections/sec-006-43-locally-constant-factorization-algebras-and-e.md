---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY"
section_id: sec-006-43-locally-constant-factorization-algebras-and-e
section_title: "Locally constant factorization algebras and En-algebras"
section_number: 4.3
pages: 37-40
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY — W e study the higher Hochschild chain functor, factorizatio n alge- bras and their relationship with topological chiral homolo gy."
---
cally constant factorization algebra on M×Dn−m, pushforward along the natural
projection π1 : M×Dm−n→ M induces a factorization algebra π1∗(A) on M ,
which is locally constant. Given a monoidal ( ∞, 1)-categoryC and a manifold X,
we denote by Faclc
X (C) the (sub)category of locally constant factorization
algebra on X taking value in C.
We recall the following Proposition which is essentially due to Lurie [25] a nd
Costello [9].
Proposition 10. The pushforward along p : Rn→ pt induces an equivalence of
(∞, 1)-categories
p∗ :Faclc
Rn (k-Mod ∞)
≃
−→En-Alg∞.
Proof. We sketch the proof. Details will appear elsewhere. Restricting to o pen
sets homeomorphic to an euclidean disk, we obtain a tautological fun ctor for :
Faclc
Rn (k-Mod ∞)→ N (Disklc(Rn))-Alg where N (Disklc(Rn))-Alg stands for the
full subcategory spanned by the locally constant N (Disk(Rn))-algebras in the sense
of [25, Deﬁnition 5.2.4.7]. By [25, Theorem 5.2.4.9 and Example 5.2.4.3], the la tter
category is equivalent to En-Alg∞ and, under this equivalence, for (F ) identiﬁes
with the global sectionF (Rn)∼=p∗(F ) for any locally constant factorization algebra
F .
We deﬁne an inverse to p∗ as follows. Let CVX be the set of open convex
subsets of Rn, which is a factorizing basis. To an En-algebra E, one associates
aCVX -factorization algebra E deﬁned by C↦→E(C) := E. As shown in [8], the
CVX -factorization algebraE has an unique extension to a factorization algebra on
Rn iﬀ it satisﬁes the ˇCech condition ˇC(U,E)→E (U ) for any factorizing subcover
U⊂CVX of a convex open U . This follows again from [25, Section 5]. Indeed, by
Theorem 5.3.4.10 in [25], the En-algebraE gives rise to a factorizable cosheaf E on
the Ran space Ran( Rn). It is easy to check that the factorizing cover U gives rise
to a cover of Ran( U ) precisely given by PU. Since every open set in U is convex,
and
∫
CE∼= E for any convex open subset C⊂ U , by [25, Theorem 5.3.4.14], we
get a canonical equivalence ˇC(PU,E )
≃
−→ ˇC(U,E) which makes the diagram
E(Ran(U ))
≃
/d39/d39❖❖❖❖❖❖❖❖❖❖❖❖ ˇC(PU,E )≃/d111/d111 ≃ /d47/d47 ˇC(U,E)
/d120/d120qqqqqqqqqqq
E
commutative (the top left equivalence follows from the fact that E is a cosheaf
on Ran(U )). Thus, ˇC(U,E)→E (U ) is an equivalence and E aCVX -factorization
algebra. We denote q(E) :=E the induced factorization algebra over Rn.
We need to check that q(E) is locally constant. It is suﬃcient to prove that for
any open D homeomorphic to an euclidean disk, the map E(D)→E (Rn)∼= E is
an equivalence. This follows from the Kister-Mazur Theorem [25, The orem 5.2.1.5]
which yields an isotopy between the inclusion֒→Rn and an homeomorphism of
Rn.
By construction,p∗◦q(E) = p∗(E)∼=E. Conversely,F being locally constant, for
any convex open set C, we have a canonical equivalence F (C)∼=F (Rn). It follows
that theCVX -factorization algebra deﬁned by p∗(F ) is canonically equivalent to the
38 G. GINOT, T. TRADLER, AND M. ZEINALIAN
restriction ofF to convex open sets. By uniqueness of the extension of factoriza tion
algebra deﬁned on a factorization basis, q◦p∗∼= id. □
Lemma 4. LetM be a manifold and π1 :M× Rd→M the canonical projection.
The pushforward by π1 induces an equivalence of (∞, 1)-categories
π1∗ :Faclc
M×Rd (k-Mod ∞)
≃
−→Faclc
M (Ed-Alg∞)
In particular, if F∈ Faclc
M×Rd (k-Mod ∞), then its factorization homology
HF (F,M× Rd) = p∗(F )(pt)∼=p∗◦π1∗(F )(pt)∼=HF (π1∗(F ),M )
is an Ed-algebra (here p :X→pt is the unique map).
Proof. Let π2 : M× Rd→ Rd be the second canonical projection. For any open
setU inM , the restriction A|U×Rd is a (locally constant) factorization algebra and
π2∗(A|U×Rd ) is a factorization algebra on Rd. Note that π2∗(A|U×Rd ) is locally
constant. Indeed, let B be any (open, homeomorphic to a) ball B⊂ Rn and denote
Ballg(U ) the set of geodesic convex open sets in U (for a choice of a metric on
U ). Then the family Ballg(U )×B is a factorizing cover of U×B. Since A is
locally constant, for any inclusion֒→˜B of open sets (homeomorphic to) balls
and geodesic convex open set O inU , the structure map A(O×B)→A (O× ~B) is
a quasi-isomorphism. Using that A is a factorization algebra we get
π2∗(A|U×Rd )(B) ∼= A(U×B)
∼= ˇC(Ballg(U )×B,A)
∼=
⨁
k>0
⨁
α1...αk∈P Ball g (U)
⨂
i1∈α1,...ik∈αk
A((Ui1∩···∩ Uik )×B)[k− 1]
∼=
⨁
k>0
⨁
α1...αk∈P Ball g (U)
⨂
i1∈α1,...ik∈αk
A((Ui1∩···∩ Uik )× ˜B)[k− 1]
∼= ˇC(Ballg(U )× ~B,A) ∼= π2∗(A|U×Rd )( ~B),
which proves that π2∗(A|U×Rd ) is locally constant (since the above composition is
the structure map π2∗(A|U×Rd )(B)→π2∗(A|U×Rd )( ~B)). Hence, by Proposition 10,
π2∗(A|U×Rd ) is equivalent to an Ed-algebraAU and there are canonical equivalences
AU ∼= π2∗(A|U×Rd )(Rd) ∼= A(U× Rd).
Since π1∗(A)(U ) = A(U× Rd)∼= AU , it follows that for each open subset U ∈
Op(M ), π1∗(A)(U ) is an Ed-algebra. Since A is a (pre)factorization algebra on
M× Rd, the structure maps
µU1,...,Uk,V :π1∗(A)(U1)⊗···⊗ π1∗(A)(Uk)∼=A(U1× Rd)⊗···⊗A (Uk× Rd)
−→A (V× Rd)∼=π1∗(A)(V )
are maps of Ed-algebras. Further, since A is a factorization algebra and locally
constant, it follows that π1∗(A)(U ) belongs to Faclc
M (Ed-Alg∞).
Now we build an inverse of π1∗. Consider B in Faclc
M (Ed-Alg∞). For any
U∈Op(M ),B(U ) is an Ed-algebra (compatible with the prefactorization algebra
structure map) and thus deﬁnes canonically a locally constant fact orization algebra
on Rd: Op(Rd)∋V ↦→B(U )(V ). A basis of neighborhood of M×Rd is given by the
productsU×V ∈Op(M )×Op(Rd). In order to extend B to a factorization algebra
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 39
onM×Rd, it is enough (by [8]) to prove that the rule ( U×V )↦→B(U )(V ) deﬁnes an
Op(M )×Op(Rd)-factorization algebra whereOp(M )×Op(Rd) is the cover ofM×Rd
obtained by taking the products of open sets. The latter follows fr om the fact
that the Ed-algebra structure is natural with respects to the inclusions µU1...,Un, ˜U
of pairwise disjoint open subsets of ˜U ∈ Op(M ). Hence the rule ( U× V ) ↦→
B(U )(V ) extends to give a factorization algebra E(B) on M× Rd. It is immediate
by construction that E(B) is locally constant and functorial in B.
It remains to prove that E :Faclc
M (Ed-Alg∞)→Faclc
M×Rd (k-Mod ∞) is a natural
inverse toπ1∗. Recall from above that the Ed-algebra structure on π1∗(A)(U ) is the
one of the Ed-algebraA(U× Rd), which corresponds to the factorization algebra
V ↦→π2∗(A|U×Rd (V ))∼=A(U×V ). It follows that there is a natural equivalence
E
(
π1∗(A)
)(
U×V
) ∼=A(U×V ) in k-Mod ∞. Further there are natural equivalences
(inEd-Alg∞)π1∗(E(B))(U )∼=E(B)(U× Rd)∼=B(U ). The lemma now follows. □
LetA be a locally constant factorization algebra on a manifold M and assume
that there is a codimension 1 submanifold (possibly with corners) N of M with a
trivialization N×D1 of its neighborhood such that M is decomposable as M =
X∪N ×IY where X,Y are submanifolds (with corners) of M glued along N×D1.
According to Lemma 4 above HF (A|N ×D1 ) is an E1-algebra.
Lemma 5 (Excision for locally constant factorization algebras) . HF (A|X ) and
HF (A|Y ) are right and left HF (A|N ×D1)-modules and further,
HF (A) ∼= HF (A|X )
L
⊗
HF (A|N ×D1 )
HF (A|Y ).
Proof. SinceA is locally constant, the canonical map A
(
X\
(
N× [t, 1)
) )
→A (X)
is an equivalence for all t∈ D1. This follows, since for any open set of the form
U× (a,b ) ⊂ N× D1, where U is homeomorphic to a ball, there is a natural
equivalenceA(U× (a,b ))∼=A(U× (a′,b ′)) for any a′ < a < b < b′ and that the
open sets of the form U× (a,b ) form a factorizing cover of N×D1. Similarly, we
have natural equivalences of E1-algebrasA(N× (a,b ))
≃
−→N×D1 (as in the proof
of Lemma 4).
Let U be an open set in X and V1,...,V k be (not necessarily disjoint) open
subsets inN . Then for any sequence of pairwise disjoint open intervals I0,I 1,...,I k
inD1 (where we assumeI0 = (−1,t 0) for somet0∈D1), the open Vi×Ii (i = 1...k )
are pairwise disjoint and disjoint from X−\
(
N× [t0, 1). To shorten notation, we
denote Xt0 :=X\
(
N× [t0, 1)
)
The structure maps of a prefactorization algebras
yield a map
A(X)⊗A (N×D1)⊗n
/d44/d44❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳❳
∼= /d47/d47A(Xt0 )⊗A (N×I1)⊗···⊗A (N×Ik)
µXt0 ,N ×I1...N ×Ik,X
/d15/d15
A(X)
This map is natural with respect to the prefactorization algebra st ructure ofA and
AN ×D1, hence induces a structure of right HF (AN ×D1 )∼=A(N×D1)-module on
HF (A|X )∼=A(X). A similar argument applies to HF (A|Y ).
40 G. GINOT, T. TRADLER, AND M. ZEINALIAN
The open sets Xt0,Ys :=Y\
(
N×(−1,s ]
)
andN×(a,b ) (wheret0,s,a<b ∈D1)
forms a factorizing coverN ofM and we also denote ~N the induced factorizing cover
ofN×D1. A ﬁnite sequence of pairwise disjoint open sets in N is just a sequence
Xto,N × (t1,t 2),...,N × (tm,tm+1),Ytm for−1<t 0 <··· <t m+2 < 1. Note that
the complexes A
(
N× (ti,ti+1)
)
are canonically equivalent to π2∗(A)
(
(ti,ti+1)
)
,
where π2 : N×D1→ D1 is the projection on the second factor. Since A(Xt0 )∼=
A(X),A(Ytm+2 )∼=A(Y ), we have
HF (A) ∼= ˇC(N,A) ∼= A(X)⊗ ˇC( ~N,A|N ×D1)⊗A (Y ).
Note that the canonical map p : M → pt factors as M
q
→ [−1, 1]→ pt where
q is the map identifying X\ (N×D1) with {−1}, Y \ (N×D1) with {1} and
projecting N×D1 onto D1 = (−1, 1) by the second projection. Then the factor-
ization homology HF (A)∼= p∗(A)∼= p∗
(
q∗(A)
)
identiﬁes with the factorization
homology of the locally constant factorization algebra q∗(A) on the closed interval
[−1, 1] and further ˇC
(
N,A
) ∼= ˇC
(
I,q ∗(A)
)
whereI is the (factorizing) cover of
[−1, 1] given by the intervals. Thus we are left to the case of a (locally con stant)
factorization algebra on [−1, 1] which assign the E1-algebraA(N×D1) to any open
interval (a,b ), and the modules A(X) to [−1,t ) and A(Y ) to ( s, 1] (with respect
to the modules structures deﬁned in the beginning of the proof). B y [9, 8], its
factorization homology is the (derived) tensor product A(X)⊗L
A(N ×D1)A(Y ). In-
deed, the ˇCech complex ˇC
(
I,q ∗(A)
)
is equivalent to the two-sided Bar construction
Bar
(
A(X),A(N×D1),A(Y )
)
(strictly speaking after replacing the E1-algebra
and modules by diﬀerential graded associative ones). □
