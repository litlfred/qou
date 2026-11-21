---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-111-165-symmetry-of-derived-torsion
section_title: "Symmetry of Derived Torsion"
section_number: 16.5
pages: 371-377
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
tation of results from [157, Section 8] to the connected graded setting. Among other
things, we prove that the χ condition of Artin-Zhang implies symmetry of derived
torsion.
In Section 17 below we are going to use the symmetry of derived torsion to give
an alternative proof of Van den Bergh’s theorem on existence of balanced dualizing
complexes (see Theorem 17.3.19).
We continue with Conventions 15.1.17 and 15.2.1. Thus K is a ﬁeld, and all
graded rings are algebraically graded central K-rings. The following setup is as-
sumed in this subsection:
Setup 16.5.1. We are given a noetherian connected graded K-ring A, with aug-
mentation ideal m. The augmentation ideal of the opposite ring Aop is mop.
The assumption that A is noetherian means that both A and Aop are left noe-
therian. The enveloping ring of A is Aen = A ⊗Aop, and it is often not noetherian.
As explained in the previous subsection, there is a torsion functor Γm : M(A, gr)
→M(A, gr).
But by the same token, there is also a torsion functor Γmop :
M(Aop, gr) →M(Aop, gr). On the category M(Aen, gr) we have two torsion func-
tors:
Γm, Γmop : M(Aen, gr) →M(Aen, gr).
These functors commute with each other. Indeed, for any M ∈M(Aen, gr) there is
equality Γm(Γmop(M)) = Γmop(Γm(M)) of graded Aen-submodules of M.
Deﬁnition 16.5.2. Under Setup 16.5.1, we say that A has ﬁnite local cohomolog-
ical dimension if the torsion functors Γm and Γmop, on M(A, gr) and M(Aop, gr)
respectively, have ﬁnite right cohomological dimensions, in the sense of Deﬁnition
16.1.2. Namely if there is a natural number d such that Hp
m = 0 and Hp
mop = 0 for
all p > d. See also formula (16.3.20).
Note that the vanishing of the derived functors Hp
m = RpΓm, and thus the coho-
mological dimension of the functor Γm, is the same on bimodules and on modules,
by Proposition 16.3.16(4). Likewise for Hp
mop.
As explained in Proposition 16.3.16(1), there are derived torsion functors
(16.5.3)
RΓm, RΓmop : D(Aen, gr) →D(Aen, gr).
There is no reason for these derived functors to commute with each other in general.
Deﬁnition
16.5.4. Under Setup 16.5.1,
the morphisms from Proposition
16.3.16(2) associated to the derived functors in formula (16.5.3) are denoted by
σR
m : RΓm →Id and σR
mop : RΓmop →Id.
Deﬁnition 16.5.5. Under Setup 16.5.1:
(1) We denote by M(tor,..)(Aen) the full subcategory of M(Aen) on the bi-
modules M that are m-torsion as A-modules; i.e. such that RestA(M) ∈
Mtor(A).
371
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(2) We denote by M(..,tor)(Aen) the full subcategory of M(Aen) on the bimod-
ules M that are mop-torsion as Aop-modules.
(3) We let
M(tor,tor)(Aen) := M(tor,..)(Aen) ∩M(..,tor)(Aen).
(4) Let ⋆, ⋄be torsion indicators, i.e. “tor” or “..”. We denote by D(⋆,⋄)(Aen)
the full subcategory of D(Aen) on the complexes M such that Hp(M) ∈
M(⋆,⋄)(Aen) for every integer p.
Trivially, for M ∈D(Aen, gr) the A-modules Hp(RΓm(M)) are m-torsion, and
the Aop-modules Hp(RΓmop(M)) are mop-torsion. Sometimes more happens:
Deﬁnition 16.5.6. Under Setup 16.5.1, a complex M ∈D(Aen, gr) is said to have
weakly symmetric derived m-torsion if these two conditions hold:
• For every p ∈Z the bimodule Hp(RΓm(M)) is mop-torsion.
• For every p ∈Z the bimodule Hp(RΓmop(M)) is m-torsion.
In terms of Deﬁnition 16.5.5, a complex M ∈D(Aen, gr) has weakly symmetric
derived m-torsion if
RΓm(M) , RΓmop(M) ∈D(tor,tor)(Aen, gr).
Deﬁnition 16.5.7. Under Setup 16.5.1, a complex M ∈D(Aen, gr) is said to have
symmetric derived m-torsion if there is an isomorphism
ϵM : RΓm(M)
≃
−→RΓmop(M)
in D(Aen, gr), such that the diagram
RΓm(M)
ϵM
∼
=
/
σR
m,M
'
RΓmop(M)
σR
mop,M

M
in D(Aen, gr) is commutative. Such an isomorphism ϵM is called a symmetry iso-
morphism.
Of course if M has symmetric derived m-torsion, then it has weakly symmetric
derived m-torsion.
Theorem 16.5.8 (Symmetric Derived Torsion, [157]). Let A be a noetherian con-
nected graded K-ring of ﬁnite local cohomological dimension. If M ∈D(Aen, gr)
has weakly symmetric derived m-torsion, then M has symmetric derived m-torsion.
Moreover, the symmetry isomorphism ϵM is unique, and it is functorial in such
complexes M.
Proof. In Theorem 16.4.3, with B := A, we have an isomorphism
evR,L
m,(−) : PA ⊗L
A (−)
≃
−→RΓm(−)
of triangulated functors from D(Aen, gr) to itself. The same theorem, but with the
roles of A and Aop exchanged, gives an isomorphism
evR,L
mop,(−) : (−) ⊗L
A PAop
≃
−→RΓmop(−)
of triangulated functors from D(Aen, gr) to itself.
Here PAop := RΓmop(A) ∈
D(Aen, gr).
Consider diagram (16.5.9) in D(Aen, gr). In this diagram, α is the associativity
isomorphism of the derived tensor product, and ru, lu are the monoidal unitor iso-
morphisms – all belonging to the monoidal structure of D(Aen, gr). A quick check,
372
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(16.5.9)
(PA ⊗L
A M) ⊗L
A PAop
id ⊗L
AσR
mop,A

α
∼
=
/ PA ⊗L
A (M ⊗L
A PAop)
σR
m,A⊗L
Aid

(PA ⊗L
A M) ⊗L
A A
ru

A ⊗L
A (M ⊗L
A PAop)
lu

PA ⊗L
A M
σR
m,A⊗L
Aid
*
M ⊗L
A PAop
id ⊗L
AσR
mop,A

M
using K-ﬂat resolutions and elements in them, shows that this is a commutative
diagram.
By Theorem 16.4.3, diagram (16.5.9) gives rise to diagram (16.5.10), with its
solid arrows only. This new diagram in D(Aen, gr) (solid arrows only) is isomorphic
to the previous one (without its second row), via the various isomorphisms evR,L
m,(−)
and evR,L
mop,(−).
(16.5.10)
RΓmop(RΓm(M))
α′
∼
=
/
σR
mop,RΓm(M)

RΓm(RΓmop(M))
σR
m,RΓmop (M)

RΓm(M)
σR
m,M
)
ϵM
/ RΓmop(M)
σR
mop,M

M
Because RΓm(M) ∈D(tor,tor)(Aen, gr), Proposition 16.3.29, applied with Aop
instead of with A, says that σR
mop,RΓm(M) is an isomorphism. Likewise, because
RΓmop(M) ∈D(tor,tor)(Aen, gr), Proposition 16.3.29 says that σR
m,RΓmop(M) is an
isomorphism. We deﬁne ϵM to be the unique isomorphism (the dashed arrow) that
makes diagram (16.5.10) commutative.
Diagram (16.5.10) shows that ϵM is unique: it has to be
ϵM = σR
m,RΓmop(M) ◦α′ ◦(σR
mop,RΓm(M))−1.
The functoriality of ϵM is a consequence of the functoriality of diagram (16.5.10).
□
Corollary 16.5.11. Under the assumptions of Theorem 16.5.8, if the bimodule A
has has weakly symmetric derived m-torsion, then there is a unique isomorphism
ϵA : PA
≃
−→PAop in D(Aen, gr) such that σR
m,A = σR
mop,A◦ϵA as morphisms PA →A.
Proof. Take M = A in the theorem.
□
The socle functor from Deﬁnition 15.2.31 extends to complexes.
Lemma 16.5.12. Let I be a minimal complex of graded-injective A-modules, and
let W := Soc(I). Then the diﬀerential of the complex W is zero.
373
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proof. Take some nonzero homogeneous element w ∈W p, say w ∈W p
q . Let U :=
K·w ⊆W p
q , so U is a nonzero graded A-submodule of Ip. Because Zp(I) is an
essential graded A-submodule of Ip we must have Zp(I) ∩U̸ = 0. Thus w ∈Zp(I),
so d(w) = 0.
□
Coﬁnite graded A-modules were deﬁned in Deﬁnition 15.2.33. By graded Matlis
duality (Theorem 15.2.34) the coﬁnite graded A-modules are the artinian objects
of M(A, gr). The full subcategory Mcof(A, gr) of coﬁnite modules is a thick abelian
subcategory of M(A, gr), closed under subobjects and quotients.
Lemma 16.5.13. Consider a complex M ∈D+(A, gr) and an integer p.
(1) If Extp
A(K, M) is a ﬁnite graded K-module, then Hp
m(M) is a coﬁnite graded
A-module.
(2) If Hq
m(M) is a coﬁnite graded A-module for every q ≤p, then Extq
A(K, M)
is a ﬁnite graded K-module for every q ≤p.
Proof.
(1) Let M →I be a minimal graded-injective resolution, and let W := Soc(I). Then
Extp
A(K, M) ∼= Hp(W). But by Lemma 16.5.12 we know that the diﬀerential of W
is zero, so in fact Extp
A(K, M) ∼= W p. Therefore W is a ﬁnite graded K-module.
Next, let J := Γm(I). This complex has the property that Hp
m(M) ∼= Hp(J).
According to Lemma 16.3.24 we have an isomorphism Jp ∼= A∗⊗W p. Since A∗is
a coﬁnite graded A-module, and Jp is a ﬁnite direct sum of degree twists of A∗, it
is also a coﬁnite graded A-module. But Hp
m(M) is a subquotient of Jp, so it too is
a coﬁnite graded A-module.
(2) We continue with the minimal graded-injective resolution M →I. We may as-
sume that H(M)̸ = 0. Let p0 := inf(H(M)); so p0 = inf(I). Take the subcomplexes
W ⊆J ⊆I as above. We know that Jq ∼= A∗⊗W q for every q. We will prove that
W q is a ﬁnite graded K-module for every q ≤p, by induction on q, starting with
q = p0.
So take an integer q in the range p0 ≤q ≤p, and assume that W q−1 is a ﬁnite
graded K-module. There is an exact sequence
Jq−1
d−→Zq(J) →Hq
m(M) →0
in M(A, gr). Since Jq−1 ∼= A∗⊗W q−1, this is a coﬁnite graded A-module, as we
already noticed. We also know that Hq
m(M) is coﬁnite. It follows that Zq(J) is a
coﬁnite graded A-module. But by Lemma 16.5.12 we have W q ⊆Zq(J), so W q
is a coﬁnite graded A-module annihilated by m. Therefore W q is a ﬁnite graded
K-module.
□
Deﬁnition 16.5.14 (Artin-Zhang, [10]). Assume Setup 16.5.1.
(1) We say that the ring A satisﬁes the left χ condition if for every M ∈
Mf(A, gr) and every integer p, the graded K-module Extp
A(K, M) is ﬁnite.
(2) The ring A is said to satisfy the χ condition if both graded rings A and Aop
satisfy the left χ condition.
Another way to state the left χ condition is this:
M ∈Mf(A, gr) implies
RHomA(K, M) ∈Df(K, gr).
Remark 16.5.15. What we call the “left χ condition” was actually called the “left
χ◦condition” in [10, Deﬁnition 3.2]. Their “left χ condition” (in [10, Deﬁnition 3.7])
is much more complicated to state. However, for a left noetherian connected graded
ring A (as we have here) these two conditions are equivalent, by [10, Proposition
3.11(2)].
Deﬁnition 16.5.16. Assume Setup 16.5.1 .
374
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(1) We say that the ring A satisﬁes the left special χ condition if for every
integer p, the graded K-module Extp
A(K, A) is ﬁnite.
(2) The ring A is said to satisfy the special χ condition if both graded rings A
and Aop satisfy the left special χ condition.
Proposition 16.5.17. The following two conditions are equivalent.
(i) A satisﬁes the left χ condition.
(ii) For every M ∈Mf(A, gr) and every p the graded A-module Hp
m(M) is
coﬁnite.
Proof. This is immediate from Lemma 16.5.13.
□
Deﬁnition
16.5.18. We denote by Db
(f,f)(Aen, gr) the full subcategory of
Db(Aen, gr) on the complexes of bimodules M whose cohomology bimodules Hp(M)
are ﬁnite graded modules over A and over Aop.
Proposition 16.5.19.
(1) If A satisﬁes the χ condition, then it satisﬁes the special χ condition.
(2) If A satisﬁes the χ condition, then every M ∈Db
(f,f)(Aen, gr) has weakly
symmetric derived m-torsion.
(3) If A satisﬁes the special χ condition, then the bimodule A has weakly sym-
metric derived m-torsion.
Proof.
(1) This is trivial.
(2) Take some M ∈Db
(f,f)(Aen, gr). Using smart truncation and induction on the
amplitude of cohomology, we can assume that M ∈M(f,f)(Aen, gr).
The χ condition tells us that Extp
A(K, M) and Extp
Aop(K, M) are ﬁnite as graded
K-modules, for all p.
For every q ≥1 the graded bimodule A/mq is gotten
from K by ﬁnitely many degree twists and extensions in M(Aen, gr). Therefore
Extp
A(A/mq, M) and Extp
Aop(A/mq, M) are ﬁnite as graded K-modules, for all p
and all q ≥1. Thus as left and as right graded A-modules, Extp
A(A/mq, M) and
Extp
Aop(A/mq, M) are of ﬁnite length, and thus torsion on both sides. Passing to
the direct limit using Proposition 16.3.16(5), we see that Hp
m(M) and Hp
mop(M) are
torsion A-modules on both sides.
(3) This is just a special case of the proof of item (2).
□
Lemma 16.5.20. Assume the functor Γm has ﬁnite cohomological dimension, and
A has the left special χ condition. Then for every M ∈Df(A, gr) and every integer
i, the graded A-module Hi
m(M) is coﬁnite.
Proof. Fix an integer i. We will prove that the graded A-module Hi
m(M) is coﬁnite.
Say Γm has cohomological dimension ≤d for some natural number d.
Step 1. Consider M ′ := smt≤i+1(M), the smart truncation of the complex M below
i + 1. There is a distinguished triangle M ′ →M →M ′′
△
−−→in D(A, gr), and hence
there is a distinguished triangle
RΓm(M ′) →RΓm(M) →RΓm(M ′′)
△
−−→.
Because Hj
m(M ′′) = 0 for j ≤i + 1, we see that Hi
m(M) ∼= Hi
m(M ′). Therefore, by
replacing M with M ′, we can assume that M ∈D−
f (A, gr).
Step 2. Now M ∈D−
f (A, gr). Choose a resolution P →M, where P is a bounded
above complex of ﬁnite graded-free A-modules. Let P ′ := stt≥i−d−2(P), the stupid
truncation of P above i −d −2. Then Hi
m(M) ∼= Hi(P ′). But P ′ is gotten from A
375
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
by ﬁnitely many cones, ﬁnite direct sums, translations and degree twists. Since A
has the left special χ condition, and using Lemma 16.5.13(1), the graded A-module
Hj
m(A) is coﬁnite for every j. Therefore Hj
m(P ′) is coﬁnite for every j; including
j = i.
□
Here is a converse to the trivial implication in Proposition 16.5.19(1), under an
extra ﬁniteness condition.
Proposition 16.5.21. If A satisﬁes the special χ condition and has ﬁnite local
cohomological dimension, then A satisﬁes the χ condition.
Proof. This is an immediate consequence of Lemma 16.5.20 and Proposition 16.5.17,
applied to both A and Aop.
□
AS regular graded rings were introduced in Deﬁnition 15.4.8.
Corollary 16.5.22. Let A be an AS regular graded ring. Then A satisﬁes the χ
condition and has ﬁnite local cohomological dimension.
Proof. The special χ condition is an immediate consequence of the AS condition
(Deﬁnition 15.4.6). The graded global cohomological dimension of A bounds its
local cohomological dimension, so the latter is ﬁnite. By Proposition 16.5.21, A
satisﬁes the χ condition.
□
Actually this is true also for AS Gorenstein rings, but the proof is harder. See
Corollary 17.3.14 and Corollary 17.2.13.
The χ condition, and the ﬁniteness of local cohomological dimension, occur in
many important examples of noncommutative graded rings. The main results that
ensure it involve a lifting argument – Theorems 15.4.13 and 17.4.35.
Here are
several examples.
Example 16.5.23. Let A := K[x1, . . . , xn], the commutative polynomial ring in
n ≥1 variables from Example 15.2.20. This is an AS regular graded ring of dimen-
sion n. By Corollary 16.5.22 the graded ring A has the χ condition and ﬁnite local
cohomological dimension.
Example 16.5.24. If B is a commutative noetherian connected graded K-ring,
then there is a ﬁnite homomorphism A →B from a polynomial ring A as in the
previous example. By Corollaries 17.4.16 and 17.4.17 the ring B satisﬁes the χ
condition and has ﬁnite local cohomological dimension.
Example 16.5.25. Let A be the homogeneous Weyl algebra from Example 15.2.21.
The element t ∈A is central regular of degree 1, and A/(t) ∼= K[x, y], the commu-
tative polynomial ring in two variables of degree 1. The ring K[x, y] is AS regular
of dimension 2, so by Theorem 15.4.13 the ring A is AS regular of dimension 3. By
Corollary 16.5.22 the graded ring A has the χ condition and ﬁnite local cohomo-
logical dimension.
As noted before, in characteristic 0 the ring A is very noncommutative.
Example 16.5.26. Let A be the homogeneous universal enveloping algebra from
Example 15.2.22. The element t ∈A is central regular of degree 1, and A/(t) ∼=
K[x1, . . . , xn], the commutative polynomial ring in n variables. The polynomial
ring is AS regular of dimension n, so by Theorem 15.4.13 the ring A is AS regular
of dimension n + 1. By Corollary 16.5.22 the graded ring A has the χ condition
and ﬁnite local cohomological dimension.
As noted in Example 15.2.22, the ring A could be very noncommutative, if g is
very nonabelian (e.g. semisimple).
376
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
We end this subsection with a result that ties the χ condition to symmetry of
derived torsion. Recall that D(f,f)(Aen, gr) is the full subcategory of D(Aen, gr) on
the complexes M such that for every p the graded bimodule Hp(M) is ﬁnite over
A and Aop.
Theorem 16.5.27. Under Setup 16.5.1, assume A satisﬁes the χ condition and
has ﬁnite local cohomological dimension. Then there is a unique isomorphism
ϵ : RΓm
≃
−→RΓmop
of triangulated functors Db
(f,f)(Aen, gr) →D(Aen, gr), such that the diagram
RΓm
ϵ
∼
=
/
σR
m
%
RΓmop
σR
mop

Id
is commutative.
Proof. According to Proposition 16.5.19(2) every complex M ∈Db
(f,f)(Aen, gr) has
weakly symmetric derived m-torsion. By Theorem 16.5.8 such a complex M has
symmetric derive torsion, and the symmetry isomorphism ϵM is unique and func-
torial.
□
16.6. NC
MGM
Equivalence. The
commutative
MGM
Equivalence
was
explained in Example 12.4.6.
A noncommutative variant of this theory was re-
cently developed by R. Vyas and A. Yekutieli [157], and in this subsection we give
an adaptation of it to the case of a NC connected graded ring A. In Section 17 be-
