---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-098-165-symmetry-of-derived-torsion
section_title: "Symmetry of Derived Torsion"
section_number: 16.5
pages: 371-377
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
an alternative proof of Van den Bergh’s theorem on existence of balanced dualizing
complexes (see Theorem 17.3.19).
We continue with Conventions 15.1.17 and 15.2.1. ThusK is a ﬁeld, and all
graded rings are algebraically graded centralK-rings. The following setup is as-
sumed in this subsection:
Setup 16.5.1. We are given a noetherian connected gradedK-ring A, with aug-
mentation ideal m. The augmentation ideal of the opposite ringAop is mop.
The assumption thatA is noetherian means that bothA and Aop are left noe-
therian. The enveloping ring ofA isAen =A⊗Aop, and it is often not noetherian.
As explained in the previous subsection, there is a torsion functorΓ m : M(A, gr)
→M(A, gr). But by the same token, there is also a torsion functor Γ mop :
M(Aop, gr)→M(Aop, gr). On the category M(Aen, gr) we have two torsion func-
tors:
Γ m, Γ mop : M(Aen, gr)→M(Aen, gr).
These functors commute with each other. Indeed, for anyM∈M(Aen, gr) there is
equality Γ m(Γ mop(M)) = Γ mop(Γ m(M)) of gradedAen-submodules ofM.
Deﬁnition 16.5.2.Under Setup 16.5.1, we say thatA has ﬁnite local cohomolog-
ical dimension if the torsion functors Γ m and Γ mop, on M(A, gr) and M(Aop, gr)
respectively, have ﬁnite right cohomological dimensions, in the sense of Deﬁnition
16.1.2. Namely if there is a natural numberd such that Hp
m = 0 and Hp
mop = 0 for
all p>d . See also formula (16.3.20).
Note that the vanishing of the derived functorsHp
m = RpΓ m, and thus the coho-
mological dimension of the functorΓ m, is the same on bimodules and on modules,
by Proposition 16.3.16(4). Likewise forHp
mop.
As explained in Proposition 16.3.16(1), there are derived torsion functors
(16.5.3) RΓ m, RΓ mop : D(Aen, gr)→D(Aen, gr).
There is no reason for these derived functors to commute with each other in general.
Deﬁnition 16.5.4. Under Setup 16.5.1, the morphisms from Proposition
16.3.16(2) associated to the derived functors in formula (16.5.3) are denoted by
σR
m : RΓ m→Id and σR
mop : RΓ mop→Id.
Deﬁnition 16.5.5.Under Setup 16.5.1:
(1) We denote by M(tor,..)(Aen) the full subcategory of M(Aen) on the bi-
modules M that are m-torsion as A-modules; i.e. such that RestA(M)∈
Mtor(A).
371
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(2) We denote byM(..,tor)(Aen) the full subcategory ofM(Aen) on the bimod-
ules M that are mop-torsion asAop-modules.
(3) We let
M(tor,tor)(Aen) := M(tor,..)(Aen)∩M(..,tor)(Aen).
(4) Let ⋆,⋄be torsion indicators, i.e. “tor” or “..”. We denote byD(⋆,⋄)(Aen)
the full subcategory of D(Aen) on the complexesM such that Hp(M)∈
M(⋆,⋄)(Aen) for every integerp.
Trivially, forM ∈D(Aen, gr) the A-modules Hp(RΓ m(M)) are m-torsion, and
the Aop-modules Hp(RΓ mop(M)) are mop-torsion. Sometimes more happens:
Deﬁnition 16.5.6.Under Setup 16.5.1, a complexM∈D(Aen, gr) is said to have
weakly symmetric derivedm-torsion if these two conditions hold:
•For everyp∈Z the bimodule Hp(RΓ m(M)) is mop-torsion.
•For everyp∈Z the bimodule Hp(RΓ mop(M)) is m-torsion.
In terms of Deﬁnition 16.5.5, a complexM∈D(Aen, gr) has weakly symmetric
derived m-torsion if
RΓ m(M), RΓ mop(M)∈D(tor,tor)(Aen, gr).
Deﬁnition 16.5.7.Under Setup 16.5.1, a complexM∈D(Aen, gr) is said to have
symmetric derived m-torsion if there is an isomorphism
ϵM : RΓ m(M)
≃
− →RΓ mop(M)
in D(Aen, gr), such that the diagram
RΓ m(M)
ϵM
∼=
//
σR
m,M
’’
RΓ mop(M)
σR
mop,M

M
in D(Aen, gr) is commutative. Such an isomorphismϵM is called asymmetry iso-
morphism.
Of course ifM has symmetric derivedm-torsion, then it has weakly symmetric
derived m-torsion.
Theorem 16.5.8(Symmetric Derived Torsion, [157]). LetA be a noetherian con-
nected gradedK-ring of ﬁnite local cohomological dimension. IfM ∈D(Aen, gr)
has weakly symmetric derivedm-torsion, thenM has symmetric derivedm-torsion.
Moreover, the symmetry isomorphismϵM is unique, and it is functorial in such
complexesM.
Proof. In Theorem 16.4.3, withB :=A, we have an isomorphism
evR,L
m,(−) : PA⊗L
A (−)
≃
− →RΓ m(−)
of triangulated functors fromD(Aen, gr) to itself. The same theorem, but with the
roles ofA and Aop exchanged, gives an isomorphism
evR,L
mop,(−) : (−)⊗L
APAop
≃
− →RΓ mop(−)
of triangulated functors from D(Aen, gr) to itself. Here PAop := RΓ mop(A) ∈
D(Aen, gr).
Consider diagram (16.5.9) inD(Aen, gr). In this diagram,αis the associativity
isomorphism of the derived tensor product, andru, lu are the monoidal unitor iso-
morphisms – all belonging to the monoidal structure ofD(Aen, gr). A quick check,
372
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(16.5.9) (PA⊗L
AM)⊗L
APAop
id⊗L
AσR
mop,A

α
∼=
//PA⊗L
A (M⊗L
APAop)
σR
m,A⊗L
Aid

(PA⊗L
AM)⊗L
AA
ru

A⊗L
A (M⊗L
APAop)
lu

PA⊗L
AM
σR
m,A⊗L
Aid
**
M⊗L
APAop
id⊗L
AσR
mop,A

M
using K-ﬂat resolutions and elements in them, shows that this is a commutative
diagram.
By Theorem 16.4.3, diagram (16.5.9) gives rise to diagram (16.5.10), with its
solid arrows only. This new diagram inD(Aen, gr) (solid arrows only) is isomorphic
to the previous one (without its second row), via the various isomorphismsevR,L
m,(−)
and evR,L
mop,(−).
(16.5.10) RΓ mop(RΓ m(M)) α′
∼=
//
σR
mop,RΓm(M)

RΓ m(RΓ mop(M))
σR
m,RΓmop(M)

RΓ m(M)
σR
m,M
))
ϵM // RΓ mop(M)
σR
mop,M

M
Because RΓ m(M) ∈D(tor,tor)(Aen, gr), Proposition 16.3.29, applied with Aop
instead of with A, says that σR
mop,RΓm(M) is an isomorphism. Likewise, because
RΓ mop(M)∈D(tor,tor)(Aen, gr), Proposition 16.3.29 says thatσR
m,RΓmop(M) is an
isomorphism. We deﬁneϵM to be the unique isomorphism (the dashed arrow) that
makes diagram (16.5.10) commutative.
Diagram (16.5.10) shows thatϵM is unique: it has to be
ϵM =σR
m,RΓmop(M)◦α′◦(σR
mop,RΓm(M))−1.
The functoriality ofϵM is a consequence of the functoriality of diagram (16.5.10).
□
Corollary 16.5.11. Under the assumptions of Theorem16.5.8, if the bimoduleA
has has weakly symmetric derivedm-torsion, then there is a unique isomorphism
ϵA :PA
≃
− →PAop in D(Aen, gr) such thatσR
m,A =σR
mop,A◦ϵA as morphismsPA→A.
Proof. TakeM =A in the theorem. □
The socle functor from Deﬁnition 15.2.31 extends to complexes.
Lemma 16.5.12. LetI be a minimal complex of graded-injectiveA-modules, and
let W := Soc(I). Then the diﬀerential of the complexW is zero.
373
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. Take some nonzero homogeneous elementw∈Wp, sayw∈Wp
q. Let U :=
K·w⊆Wp
q, so U is a nonzero gradedA-submodule of Ip. Because Zp(I) is an
essential gradedA-submodule ofIp we must haveZp(I)∩U⁄= 0. Thusw∈Zp(I),
so d(w) = 0. □
Coﬁnite gradedA-modules were deﬁned in Deﬁnition 15.2.33. By graded Matlis
duality (Theorem 15.2.34) the coﬁnite gradedA-modules are the artinian objects
of M(A, gr). The full subcategoryMcof(A, gr) of coﬁnite modules is a thick abelian
subcategory of M(A, gr), closed under subobjects and quotients.
Lemma 16.5.13. Consider a complexM∈D+(A, gr) and an integerp.
(1) If Extp
A(K,M ) is a ﬁnite gradedK-module, thenHp
m(M) is a coﬁnite graded
A-module.
(2) If Hq
m(M) is a coﬁnite gradedA-module for everyq≤p, then Extq
A(K,M )
is a ﬁnite gradedK-module for everyq≤p.
Proof.
(1)Let M→I beaminimalgraded-injectiveresolution, andlet W := Soc(I). Then
Extp
A(K,M )∼= Hp(W ). But by Lemma 16.5.12 we know that the diﬀerential ofW
is zero, so in factExtp
A(K,M )∼=Wp. ThereforeW is a ﬁnite gradedK-module.
Next, let J := Γ m(I). This complex has the property that Hp
m(M)∼= Hp(J).
According to Lemma 16.3.24 we have an isomorphismJp∼=A∗⊗Wp. SinceA∗is
a coﬁnite gradedA-module, andJp is a ﬁnite direct sum of degree twists ofA∗, it
is also a coﬁnite gradedA-module. But Hp
m(M) is a subquotient ofJp, so it too is
a coﬁnite gradedA-module.
(2) We continue with the minimal graded-injective resolutionM→I. We may as-
sume thatH(M)⁄= 0. Letp0 := inf(H(M)); sop0 = inf(I). Take the subcomplexes
W⊆J⊆I as above. We know thatJq∼=A∗⊗Wq for everyq. We will prove that
Wq is a ﬁnite gradedK-module for everyq≤p, by induction onq, starting with
q =p0.
So take an integerq in the rangep0≤q≤p, and assume thatWq−1 is a ﬁnite
gradedK-module. There is an exact sequence
Jq−1 d
− →Zq(J)→Hq
m(M)→0
in M(A, gr). Since Jq−1∼= A∗⊗Wq−1, this is a coﬁnite gradedA-module, as we
already noticed. We also know thatHq
m(M) is coﬁnite. It follows thatZq(J) is a
coﬁnite gradedA-module. But by Lemma 16.5.12 we haveWq⊆Zq(J), so Wq
is a coﬁnite gradedA-module annihilated by m. Therefore Wq is a ﬁnite graded
K-module. □
Deﬁnition 16.5.14(Artin-Zhang, [10]). Assume Setup 16.5.1.
(1) We say that the ring A satisﬁes theleft χcondition if for every M ∈
Mf(A, gr) and every integerp, the gradedK-module Extp
A(K,M ) is ﬁnite.
(2) The ringA is said to satisfy theχconditionif both graded ringsA andAop
satisfy the leftχcondition.
Another way to state the left χcondition is this: M ∈Mf(A, gr) implies
RHomA(K,M )∈Df(K, gr).
Remark 16.5.15.What we call the “leftχcondition” was actually called the “left
χ◦condition” in [10, Deﬁnition 3.2]. Their “leftχcondition” (in [10, Deﬁnition 3.7])
is much more complicated to state. However, for a left noetherian connected graded
ring A (as we have here) these two conditions are equivalent, by [10, Proposition
3.11(2)].
Deﬁnition 16.5.16.Assume Setup 16.5.1 .
374
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(1) We say that the ringA satisﬁes theleft special χcondition if for every
integerp, the gradedK-module Extp
A(K,A ) is ﬁnite.
(2) The ringA is said to satisfy thespecialχcondition if both graded ringsA
and Aop satisfy the left specialχcondition.
Proposition 16.5.17. The following two conditions are equivalent.
(i) A satisﬁes the leftχcondition.
(ii) For every M ∈Mf(A, gr) and every p the graded A-module Hp
m(M) is
coﬁnite.
Proof. This is immediate from Lemma 16.5.13. □
Deﬁnition 16.5.18. We denote by Db
(f,f)(Aen, gr) the full subcategory of
Db(Aen, gr) on the complexes of bimodulesM whose cohomology bimodulesHp(M)
are ﬁnite graded modules overA and overAop.
Proposition 16.5.19.
(1) If A satisﬁes theχcondition, then it satisﬁes the specialχcondition.
(2) If A satisﬁes theχcondition, then everyM ∈Db
(f,f)(Aen, gr) has weakly
symmetric derived m-torsion.
(3) If A satisﬁes the specialχcondition, then the bimoduleA has weakly sym-
metric derived m-torsion.
Proof.
(1) This is trivial.
(2) Take someM∈Db
(f,f)(Aen, gr). Using smart truncation and induction on the
amplitude of cohomology, we can assume thatM∈M(f,f)(Aen, gr).
Theχcondition tells us thatExtp
A(K,M ) and Extp
Aop(K,M ) are ﬁnite as graded
K-modules, for all p. For every q ≥1 the graded bimodule A/mq is gotten
from K by ﬁnitely many degree twists and extensions inM(Aen, gr). Therefore
Extp
A(A/mq,M ) and Extp
Aop(A/mq,M ) are ﬁnite as gradedK-modules, for all p
and allq≥1. Thus as left and as right gradedA-modules, Extp
A(A/mq,M ) and
Extp
Aop(A/mq,M ) are of ﬁnite length, and thus torsion on both sides. Passing to
the direct limit using Proposition 16.3.16(5), we see thatHp
m(M) and Hp
mop(M) are
torsion A-modules on both sides.
(3) This is just a special case of the proof of item (2). □
Lemma 16.5.20. Assume the functorΓ m has ﬁnite cohomological dimension, and
A has the left specialχcondition. Then for everyM∈Df(A, gr) and every integer
i, the gradedA-module Hi
m(M) is coﬁnite.
Proof. Fix an integeri. We will prove that the gradedA-module Hi
m(M) is coﬁnite.
Say Γ m has cohomological dimension≤d for some natural numberd.
Step 1. ConsiderM′:= smt≤i+1(M), the smart truncation of the complexM below
i + 1. There is a distinguished triangleM′→M→M′′∆
−−→in D(A, gr), and hence
there is a distinguished triangle
RΓ m(M′)→RΓ m(M)→RΓ m(M′′)
∆
−−→.
Because Hj
m(M′′) = 0 for j≤i + 1, we see thatHi
m(M)∼= Hi
m(M′). Therefore, by
replacing M with M′, we can assume thatM∈D−
f (A, gr).
Step 2. NowM∈D−
f (A, gr). Choose a resolutionP→M, whereP is a bounded
above complex of ﬁnite graded-freeA-modules. LetP′:= stt≥i−d−2(P ), the stupid
truncation ofP abovei−d−2. Then Hi
m(M)∼= Hi(P′). ButP′is gotten fromA
375
Derived Categories | Amnon Yekutieli | 14 Apr 2019
by ﬁnitely many cones, ﬁnite direct sums, translations and degree twists. SinceA
has the left specialχcondition, and using Lemma 16.5.13(1), the gradedA-module
Hj
m(A) is coﬁnite for everyj. Therefore Hj
m(P′) is coﬁnite for everyj; including
j =i. □
Here is a converse to the trivial implication in Proposition 16.5.19(1), under an
extra ﬁniteness condition.
Proposition 16.5.21. If A satisﬁes the specialχcondition and has ﬁnite local
cohomological dimension, thenA satisﬁes theχcondition.
Proof. ThisisanimmediateconsequenceofLemma16.5.20andProposition16.5.17,
applied to bothA and Aop. □
AS regular graded rings were introduced in Deﬁnition 15.4.8.
Corollary 16.5.22. Let A be an AS regular graded ring. ThenA satisﬁes theχ
condition and has ﬁnite local cohomological dimension.
Proof. The special χcondition is an immediate consequence of the AS condition
(Deﬁnition 15.4.6). The graded global cohomological dimension ofA bounds its
local cohomological dimension, so the latter is ﬁnite. By Proposition 16.5.21,A
satisﬁes theχcondition. □
Actually this is true also for AS Gorenstein rings, but the proof is harder. See
Corollary 17.3.14 and Corollary 17.2.13.
The χcondition, and the ﬁniteness of local cohomological dimension, occur in
many important examples of noncommutative graded rings. The main results that
ensure it involve a lifting argument – Theorems 15.4.13 and 17.4.35. Here are
several examples.
Example 16.5.23. Let A :=K[x1,...,xn], the commutative polynomial ring in
n≥1 variables from Example 15.2.20. This is an AS regular graded ring of dimen-
sionn. By Corollary 16.5.22 the graded ringA has theχcondition and ﬁnite local
cohomological dimension.
Example 16.5.24. If B is a commutative noetherian connected gradedK-ring,
then there is a ﬁnite homomorphismA→B from a polynomial ringA as in the
previous example. By Corollaries 17.4.16 and 17.4.17 the ringB satisﬁes theχ
condition and has ﬁnite local cohomological dimension.
Example 16.5.25.LetAbe the homogeneous Weyl algebra from Example 15.2.21.
The elementt∈A is central regular of degree1, andA/(t)∼=K[x,y ], the commu-
tative polynomial ring in two variables of degree1. The ringK[x,y ] is AS regular
of dimension2, so by Theorem 15.4.13 the ringA is AS regular of dimension3. By
Corollary 16.5.22 the graded ringA has theχcondition and ﬁnite local cohomo-
logical dimension.
As noted before, in characteristic0 the ringA is very noncommutative.
Example 16.5.26. Let A be the homogeneous universal enveloping algebra from
Example 15.2.22. The elementt∈A is central regular of degree1, andA/(t)∼=
K[x1,...,xn], the commutative polynomial ring inn variables. The polynomial
ring is AS regular of dimensionn, so by Theorem 15.4.13 the ringA is AS regular
of dimensionn + 1. By Corollary 16.5.22 the graded ringA has theχcondition
and ﬁnite local cohomological dimension.
As noted in Example 15.2.22, the ringA could be very noncommutative, ifg is
very nonabelian (e.g. semisimple).
376
Derived Categories | Amnon Yekutieli | 14 Apr 2019
We end this subsection with a result that ties theχcondition to symmetry of
derived torsion. Recall thatD(f,f)(Aen, gr) is the full subcategory ofD(Aen, gr) on
the complexesM such that for everyp the graded bimodule Hp(M) is ﬁnite over
A and Aop.
Theorem 16.5.27. Under Setup 16.5.1, assume A satisﬁes theχcondition and
has ﬁnite local cohomological dimension. Then there is a unique isomorphism
ϵ: RΓ m
≃
− →RΓ mop
of triangulated functorsDb
(f,f)(Aen, gr)→D(Aen, gr), such that the diagram
RΓ m
ϵ
∼=
//
σR
m %%
RΓ mop
σR
mop

Id
is commutative.
Proof. According to Proposition 16.5.19(2) every complexM∈Db
(f,f)(Aen, gr) has
weakly symmetric derived m-torsion. By Theorem 16.5.8 such a complexM has
symmetric derive torsion, and the symmetry isomorphismϵM is unique and func-
torial. □
