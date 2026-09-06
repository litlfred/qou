---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-073-126-derived-restriction-induction-and-coinductio
section_title: "Derived Restriction, Induction and Coinduction Functors"
section_number: 12.6
pages: 235-238
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
fore, there is a nonzero commutative base ringK. All DG rings areK-central, and
all homomorphisms between them are overK.
Deﬁnition 12.6.1.Let u :A→B be a DG ring homomorphism.
(1) The restriction functor is the K-linear DG functor Restu = Rest B/A :
C(B)→C(A), that is the identity on the underlying DGK-modules, and
the A-action is viau.
(2) Since the functorRestu is exact, it extends to a triangulated functorRestu :
D(B)→D(A).
Deﬁnition 12.6.2.Let u :A→B be a DG ring homomorphism.
(1) The induction functor is the DG functorIndu = IndB/A : C(A)→C(B)
with formula Indu :=B⊗A (−).
(2) The derived induction functor LIndu = LIndB/A : D(A)→D(B) is the
triangulated left derived functor ofIndu, namely LIndu :=B⊗L
A (−).
For every M ∈D(A) there is the canonical morphism ηL
M : LInd u(M) →
Indu(M) in D(B), which is part of the left derived functor.
Deﬁnition 12.6.3.Let u : A→B be a DG ring homomorphism, and letM ∈
D(A) and N∈D(B) be DG modules. A morphismλ:M→Restu(N) in D(A) is
called aforward morphism inD(A) over u.
Similarly there are forward morphisms overu in the categories C(A), Cstr(A)
and K(A).
We often omit the functorRestu, and just talk about a forward morphismλ:
M→N in D(A) overu, etc.
For any DG moduleM∈C(A) there is a canonical forward homomorphism
(12.6.4) qu,M :M→B⊗AM = Indu(M), qu,M(m) := 1B⊗m
in Cstr(A) overu. Now letN∈C(B). The usual change of ring adjunction formula
gives a canonical isomorphism
(12.6.5) fadju,M,N : HomC(A)(M,N )
≃
− →HomC(B)
(
B⊗AM,N
{
in Cstr(K). It is characterized by the property that for every forward morphism
λ:M→N there is equalityfadju,M,N (λ)◦qu,M =λ. We refer to the isomorphism
fadju,M,N as forward adjunction. Since the isomorphismfadju,M,N is functorial in
M and N, we see that the functorIndu is a left adjoint ofRestu.
The next theorem shows that this is also true on the derived level.
Theorem 12.6.6. Letu :A→B be a homomorphism of DGK-rings.
(1) For eachM∈D(A) there is a unique forward morphism
qL
u,M :M→B⊗L
AM = LIndu(M)
in D(A) overu, called thecanonical forward morphism, which is functorial
in M, and satisﬁesηL
M◦qL
u,M = qu,M.
(2) For eachM∈D(A) andN∈D(B) there is a uniqueK-linear isomorphism
fadjL
u,M,N : HomD(A)
(
M, Restu(N)
{≃
− →HomD(B)
(
LIndu(M),N
{
,
called derived forward adjunction, such that fadjL
u,M,N (λ)◦qL
u,M = λfor
all forward morphisms λ: M →N in D(A) over u. The isomorphism
fadjL
u,M,N is functorial inM and N.
(3) The functor LIndu : D(A)→D(B) is left adjoint toRestu.
235
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Here are the commutative diagrams inD(A) illustrating the theorem.
M
qL
u,M

qu,M
’’
LIndu(M)
ηL
M
// Indu(M)
M
qL
u,M

λ
((
LIndu(M)
fadjL
u,M,N (λ)
// N
Proof.
(1) Let us choose a system of K-projective resolutions inC(A), as in Deﬁnition
10.2.16, and use it to present the derived functorLIndu. To construct an isomor-
phism qL
u,M which is functorial inM, it suﬃces to consider a K-projective DG
A-module M = P. But then LIndu(P ) = Ind u(P ), ηL
P = idP, and we have no
choice but to deﬁneqL
u,P := qu,P.
(2) We keep the system of K-projective resolutions. As in item (1), it is enough to
say what isfadjL
u,P,N for a K-projective DGA-moduleP. Then there is a canonical
isomorphism
QA : HomK(A)(P,N )
≃
− →HomD(A)(P,N ).
SinceB⊗AP = LIndu(P ) is a K-projective DGB-module, we also have a canonical
isomorphism
QB : HomK(B)(B⊗AP,N )
≃
− →HomD(B)(B⊗AP,N ).
But the usual adjunction formula (12.6.5) induces, by passing to0-th cohomology
on both sides, an isomorphism
H0(fadju,P,N ) : HomK(A)(P,N )
≃
− →HomK(B)(B⊗AP,N ),
and it satisﬁesH0(fadju,P,N )(λ)◦qu,P = λfor any forward morphismλ: P→N
in K(A). We deﬁne
fadjL
u,P,N := QB◦H0(fadju,P,N )◦Q−1
A .
(3) SincefadjL
u,M,N is a bifunctorial isomorphism, it determines an adjunction.□
Deﬁnition 12.6.7.Let u : A→B be a DG ring homomorphism, and letM ∈
D(A) and N∈D(B) be DG modules. A forward morphismλ: M→N in D(A)
overu is called anondegenerate forward morphismif the corresponding morphism
fadjL
u,M,N (λ) :B⊗L
AM = LIndu(M)→N
in D(B) is an isomorphism.
Example 12.6.8. Given M∈D(A), letN := B⊗L
AM∈D(B). The canonical
derived forward morphismqL
u,M :M→N is a nondegenerate forward morphism in
D(A) overu, because fadjL
u,M,N (qL
u,M) = idN.
Proposition 12.6.9.SupposeA
u
− →B
v
− →C are homomorphisms of DG rings,L∈
D(A), M∈D(B) and N∈D(C) are DG modules,λ:L→M is a nondegenerate
forward morphism in D(A) over u, and µ: M →N is a nondegenerate forward
morphism in D(B) over v. Then µ◦λ: L →N is a nondegenerate forward
morphism in D(A) over v◦u.
Proof. Since λis a nondegenerate forward morphism, it induces an isomorphism
N ∼= B⊗L
A M. We can thus assume that N = B⊗L
A M and that λ= q L
u,M :
M→B⊗L
AM. Similarly, we can assume thatµ= qL
v,N :N→C⊗L
BN. But now
µ◦λ= q L
v,N◦qL
u,M = q L
v◦u,L : L→N, and this is known to be a nondegenerate
forward morphism (see Example 12.6.8). □
236
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 12.6.10.Let u :A→B be a homomorphism of DGK-rings.
(1) The coinduction functor is theK-linear DG functor CIndu = CIndB/A :
C(A)→C(B) with formula CIndu := HomA(B,−).
(2) The derived coinduction functorRCIndu = RCIndB/A : D(A)→D(B) is
the triangulated right derived functor ofCIndu.
Thus for eachM∈D(A) we have RCIndu(M) = RHomA(B,M ). There is the
canonical morphismηR
M : CIndu(M)→RCIndu(M) in D(B), which is part of the
right derived functor,
Deﬁnition 12.6.11.Let u : A→B be a DG ring homomorphism, and letM∈
D(A) and N∈D(B) be DG modules. A morphismθ: Restu(N)→M in D(A) is
called abackward(or trace) morphism in D(A) over u.
Similarly there are backward morphisms overu in the categoriesC(A), Cstr(A)
and K(A).
We shall use the terms “backward morphism” and “trace morphism” synony-
mously. We often omit the functorRestu, and just talk about a backward morphism
θ:N→M in D(A) overu.
For any DG moduleM∈C(A) there is a canonical backward homomorphism
tru,M : CIndu(M) = Hom A(B,M )→M, tru,M(φ) := φ(1B) in Cstr(A) over u.
Now letN∈C(B). The usual change of ring adjunction formula gives a canonical
isomorphism
badju,M,N : HomC(A)(N,M )
≃
− →HomC(B)
(
N, HomA(B,M )
{
in Cstr(K). It is characterized by the property that for every backward morphism
θ:N→M there is equalitytru,M◦badju,M,N (θ) =θ. We refer to the isomorphism
badju,M,N as backward adjunction. Since the isomorphismbadju,M,N is functorial
in M and N, we see that the functorCIndu is a right adjoint ofRestu.
The next theorem shows that this is also true on the derived level.
Theorem 12.6.12. Letu :A→B be a homomorphism of DGK-rings.
(1) For eachM∈D(A) there is a unique backward morphism
trR
u,M : RCIndu(M) = RHomA(B,M )→M
in D(A) over u, called thecanonical backward morphism, which is functo-
rial inM, and satisﬁestrR
u,M◦ηR
M = tru,M.
(2) For eachM∈D(A) andN∈D(B) there is a uniqueK-linear isomorphism
badjR
u,M,N : HomD(A)
(
Restu(N),M
{≃
− →HomD(B)
(
N, RCIndu(M)
{
,
called derived backward adjunction, such thattrR
u,M◦badjR
u,M,N (θ) =θfor
all backward morphismsθ: N →M in D(A) over u. The isomorphism
badjR
u,M,N is functorial inM and N.
(3) The functor RCIndu : D(A)→D(B) is right adjoint toRestu.
Here are the commutative diagrams inD(A) illustrating the theorem.
CIndu(M)
ηR
M //
tru,M
((
RCIndu(M)
trR
u,M

M
N
badjR
u,M,N (θ)
//
θ
((
RCIndu(M)
trR
u,M

M
Proof. The proof is very similar to that of Theorem 12.6.6. The only change is
that now we choose a system of K-injective resolutions inC(A). For a K-injective
DG A-module I, the DGB-module HomA(B,I ) is K-injective, and it represents
RCIndu(M). □
237
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 12.6.13.Let u : A→B be a DG ring homomorphism, and letM∈
D(A) and N∈D(B) be DG modules. A backward morphismθ:N→M in D(A)
overu is calleda nondegenerate backward morphismif the corresponding morphism
badjR
u,M,N (θ) :N→RHomA(B,M ) = RCIndu(M)
in D(B) is an isomorphism.
Example 12.6.14. Given M ∈D(A), let N := RHomA(B,M )∈D(B). The
canonical backward morphismtrR
u,M :N→M is a nondegenerate backward mor-
phism in D(A) overu, because badjR
u,M,N (trR
u,M) = idN.
Proposition 12.6.15. Suppose A
u
− →B
v
− →C are homomorphisms of DG rings,
L∈D(A), M∈D(B) and N∈D(C) are DG modules,θ: M→L is a nonde-
generate backward morphism inD(A) over u, andζ:N→M is a nondegenerate
backward morphism in D(B) over v. Then θ◦ζ: N →L is a nondegenerate
backward morphism inD(A) over v◦u.
Proof. Since θis a nondegenerate backward morphism, it induces an isomorphism
M ∼= RHomA(B,L ). We can thus assume that M = RHom A(B,L ) and that
θ= trR
u,L. Similarly, we can assume thatN = RHomB(C,M ) and thatζ= trR
v,M.
But now θ◦ζ= tr R
u,L◦trR
v,M = tr R
v◦u,L : N →L, and this is known to be a
nondegenerate backward morphism (see Example 12.6.14). □
Example 12.6.16. If A = B and u = idA, then backward and forward mor-
phisms overu are just morphisms inD(A). Nondegenerate (backward or forward)
morphisms are just isomorphisms inD(A).
