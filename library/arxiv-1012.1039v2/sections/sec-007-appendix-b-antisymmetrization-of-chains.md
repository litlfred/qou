---
doc_id: arxiv-1012.1039v2
doc_title: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS"
section_id: sec-007-appendix-b-antisymmetrization-of-chains
section_title: "Appendix B. (Anti)Symmetrization of chains"
section_number: null
pages: 18-20
source_pdf: 1012.1039v2.pdf
source_sha256: acb2575050db419d
toc_source: outline
doc_brief: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS — Let M be a hyperbolic n–manifold whose cusps have torus cross- sections."
---
In this section we prove that the chain map S deﬁned in Section 2.2 is chain
homotopic to the identity.
We let ∆n denote the standard n–simplex, and begin by deﬁning a “coning”
operator for all n and k
cn : Ck(∆n; R) →Ck+1(∆n; R).
We deﬁne cn on a singular k–simplex ψ: ∆k →∆n and then extend by linearity.
Let ι: ∆k →∆k+1 be the aﬃne map taking each vertex ei of ∆k to the vertex
ei+1 of ∆k+1; the vertex e0 is the only one missed by ι. Each point in ∆k+1 is
SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS
19
uniquely expressible convex combination of some point in ι(∆k) with e0. Let mn
be the barycenter of ∆n, and deﬁne
cn(ψ) (te0 + (1 −t)ι(x)) = tmn + (1 −t)ψ(x).
In words, cn(ψ) is ψ coned to the barycenter mn. The key fact about cn is that for
any chain a ∈Ck(∆n; R), we have
(10)
∂cn(a) = a −cn(∂a).
(In other words, cn is a chain contraction of C∗(∆n; R).)
We use the coning operator to inductively deﬁne an element µn ∈Cn+1(∆n; R),
and, for any space Y , a map
P (Y )
n
: Cn(Y ; R) →Cn+1(Y ; R).
As in the deﬁnition of symmetrization, we abuse notation by using q ∈Sn+1 to
denote the unique aﬃne map from ∆n to itself which is equal to q when restricted
to the vertices. We start with µ0 = 0, and P0 = 0 for all Y . We may assume P (∆n)
n−1
has been deﬁned, and set
(11)
µn =


1
|Sn+1|
X
q∈Sn+1
sign(q)cn(q)

−cn(1∆n) −cn

P (∆n)
n−1 (∂1∆n)

.
For any space Y , we deﬁne Pn : Cn(Y ; R) →Cn+1(Y ; R) on simplices, and then
extend linearly; for φ: ∆n →Y a singular n–simplex, deﬁne
(12)
P (Y )
n
(φ) = φ♯(µn).
The maps P (·)
n
commute with continuous maps:
Lemma B.1. If f : X →Y is any continuous map, and n is an integer, then
f♯◦P (X)
n
= P (Y )
n
◦f♯.
Proof. Since all the maps involved are linear, it suﬃces to verify this for a single
singular simplex φ: ∆n →X. We have:
(f♯◦P (X)
n
)(φ) = f♯φ♯(µn) = (f ◦φ)♯(µn) = P (Y )
n
(f ◦φ) = (P (Y )
n
◦f♯)(φ).
□
Lemma B.2. P (X)
∗
as deﬁned in equation (12) is a chain homotopy between S and
1C∗(X;R).
Proof. In this proof we’ll write P (X)
k
as Pk.
It suﬃces to show that, for each n and each singular n–simplex φ,
∂Pn(φ) = S(φ) −φ −Pn−1(∂φ).
For n = 0, this is immediate, so we suppose that n > 0 and argue inductively. We
compute from (12) and (10),
∂Pn(φ) =φ♯
 
1
|Sn+1|
X
q∈Sn+1
sign(q)(q −cn(∂q))
−1∆n + cn(∂1∆n) −Pn−1(∂1∆n) + cn∂

P (∆n)
n−1 (∂1∆n)
 !
20
K. FUJIWARA AND J. F. MANNING
By induction on n (and the fact that ∂2 = 0) we have
∂P (∆n)
n−1 (∂1∆n) = S(∂1∆n) −∂1∆n,
so we can rewrite
∂Pn(φ) = φ♯
 
1
|Sn+1|
X
q∈Sn+1
sign(q)(q −cn(∂q))
−1∆n + cn(∂1∆n) −P (∆n)
n−1 (∂1∆n) + cn(S(∂1∆n) −∂1∆n)
!
= φ♯
 
S(1∆n) −1∆n −P (∆n)
n−1 (∂1∆n)
+ cn(S(∂1∆n)) −
1
|Sn+1|
X
q∈Sn+1
sign(q)cn(∂q)
!
The last two terms exactly cancel because cn and ∂are both linear, so
1
|Sn+1|
X
q∈Sn+1
sign(q)cn(∂q) = cn∂


1
|Sn+1|
X
q∈Sn+1
sign(q)q

= cn∂S(1∆n)
and, since S is a chain map, cn(∂S(1∆n)) = cn(S(∂1∆n)). We therefore have
∂Pn(φ) = φ♯

S(1∆n) −1∆n −P (∆n)
n−1 (∂1∆n)

.
We now invoke Lemma B.1, which implies that
φ♯

P (∆n)
n−1 (∂1∆n)

= Pn−1(∂φ),
and so
∂Pn(φ) = S(φ) −φ −Pn−1(∂φ).
□
