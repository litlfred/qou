---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-021-61-the-nontrivial-block-in-reps0-f
section_title: "The nontrivial block in Rep(S0; F)"
section_number: 6.1
pages: 37-39
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
toc_source: outline
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Rep(St)."
---
Next, we show that for ﬁxed d ∈Z≥0, the nontrivial blocks in Rep(Sd; F) are all
equivalent. We then state a conjecture which would allow us to compare blocks
in Rep(Sd; F) with those in Rep(Sd−1; F) using a “restriction functor.” Finally,
we use Martin’s results on the partition algebras to give a complete description of
nontrivial blocks.
6.1. The nontrivial block in Rep(S0; F). In this section we give a complete
description of the one nontrivial block in Rep(S0; F). In this particular case the
constructions of all idempotents are easy enough that we are able to fully describe
the block by brute force computations. We expect this method is too computation-
ally complicated in other cases.
Throughout this section we consider the group algebra of the symmetric group
FSn as a subalgebra of the partition algebra FPn(0) (see Remark 2.14). With this
in mind, we have the following idempotents:
sn := 1
n!
X
σ∈Sn
sgn(σ)σ ∈FPn(0).
Proposition 6.1. In Rep(S0; F), ([n], sn) ∼= L((1n)) for all n ≥0.
Proof. The proposition is certainly true when n = 0, so we assume n > 0. Since
the projection FPn(0) ↠FSn maps sn 7→sn, and in FSn the idempotent sn
is primitive corresponding to (1n), we know any orthogonal decomposition of sn
into primitive idempotents in FPn(0) must contain a summand corresponding to
L((1n)) in Rep(S0; F). Thus, by Example 5.10(1) and Proposition 5.22 it suﬃces
to show dimF snFPn(0)sn = 2.
Suppose µ ∈Pn,n satisﬁes τµ = π for some transposition τ ∈Sn ⊂Pn,n. Then
snµsn = snτµsn = −snπsn, which implies snµsn = 0. Similarly, if µτ = µ for some
transposition τ, then snµsn = 0. The only elements of µ ∈Pn,n such that τµ̸ = µ
and µτ̸ = µ for all transpositions τ ∈Sn are either elements of Sn or of the form
σxσ′ for some σ, σ′ ∈Sn with x = idn−1 ⊗π where π ∈P1,1 is as in the proof of
Theorem 3.4. If µ ∈Sn, then snµsn = ±sn. If µ = σxσ′ for some σ, σ′ ∈Sn, then
snµsn = ±snxsn. Hence, sn and snxsn span snFPn(0)sn.
□
As a consequence of Example 5.10(1) and Proposition 6.1, describing the non-
trivial block in Rep(S0; F) amounts to describing morphisms among the objects
([n], sn) for n ≥0. To describe such morphisms, let x1
0 denote the unique element
of P1,0 and let xn+1
n
= idn ⊗x1
0 for all n > 0. Finally, let xn
n+1 = (xn+1
n
)∨for all
n ≥0 as pictured below.
.  .  .
.  .  .
The following lemma records a couple properties useful in forthcoming calculations.
38
JONATHAN COMES AND VICTOR OSTRIK
Lemma 6.2. The following identities hold in Rep(S0; F):
(1) snxn+1
n
sn+1 = xn+1
n
sn+1 for all n ≥0.
(2) −nsnxn−1
n
xn
n−1sn = (n + 1)xn+1
n
sn+1xn
n+1 for all n > 0.
(3) xn
n−1xn+1
n
sn+1 = 0 for all n > 0.
Proof. To prove part (1), let s′
n = sn ⊗id1 ∈FPn+1(0) for all n ≥0.
Then
snxn+1
n
sn+1 = xn+1
n
s′
nsn+1 = xn+1
n
sn+1.
To prove part (2), notice that for σ ∈Sn+1 there are exactly (n−1)! pairs (τ1, τ2)
with τ1, τ2 ∈Sn such that τ1xn−1
n
xn
n−1τ2 = xn+1
n
σxn
n+1. Moreover, for such a pair
sgn(τ1τ2) = −sgn(σ). Conversely, given any τ1, τ2 ∈Sn, either τ1xn−1
n
xn
n−1τ2 = 0
or there exists a unique σ ∈Sn+1 with τ1xn−1
n
xn
n−1τ2 = xn+1
n
σxn
n+1. Therefore,
−(n!sn)xn−1
n
xn
n−1(n!sn) = (n −1)!xn+1
n
(n + 1)!sn+1xn
n+1 which is equivalent to the
identity in part (2).
To prove part (3), let τ ∈Sn+1 denote the transposition n ↔n + 1. Then
xn
n−1xn+1
n
sn+1 = (xn
n−1xn+1
n
τ)sn+1 = xn
n−1xn+1
n
(τsn+1) = −xn
n−1xn+1
n
sn+1. The
result follows.
□
Next, deﬁne the following morphisms:
αn := (−1)n(n + 1)!sn+1xn
n+1sn,
βn := 1
n!snxn+1
n
sn+1
(n ≥0),
γn := (−1)nnsnxn−1
n
xn
n−1sn
(n > 0).
The next lemma contains all calculations needed to describe the nontrivial block
in Rep(S0; F).
Lemma 6.3. The following equations hold in Rep(S0; F):
(1) αn̸ = 0 for n ≥0.
(2) βn̸ = 0 for n ≥0.
(3) γn̸ = 0 for n > 0.
(4) γ2
n = 0 for n > 0, hence γn is not a scalar multiple of sn.
(5) β0α0 = 0.
(6) βnαn = γn for n > 0.
(7) αn−1βn−1 = γn for n > 0.
(8) αnαn−1 = 0 for n > 0.
(9) βn−1βn = 0 for n > 0.
Proof. Up to a nonzero scalar multiple, αn and β∨
n are equal. Hence, parts (1) and
(8) will follow from parts (2) and (9) respectively.
(2) Write βn = P
π∈Pn+1,n bππ. Then bxn+1
n
=
1
n!(n+1)!.
(3) Write γn = P
π∈Pn+1,n cππ. Then cxn−1
n
xn
n−1 = (−1)n
n!
.
(4) γ2
n = −n(n + 1)snxn−1
n
xn
n−1xn+1
n
sn+1xn
n+1 = 0, (Lemma 6.2(2)&(3)).
(5) β0α0 = −x1
0x0
1 = 0 in Rep(S0; F).
(6) βnαn = (−1)n+1(n + 1)snxn+1
n
sn+1xn
n+1sn = γn, (Lemma 6.2(2)).
(7) αn−1βn−1 = (−1)nnsnxn−1
n
sn−1xn
n−1sn = γn, (Lemma 6.2(1)).
(9) βn−1βn =
1
(n−1)!n!sn−1xn
n−1snxn+1
n
sn+1, which (by Lemma 6.2(1)) is equal
to
1
(n−1)!n!sn−1xn
n−1xn+1
n
sn+1, which (by Lemma 6.2(3)) is equal to zero.
□
The following theorem describes the nontrivial block in Rep(S0; F).
ON BLOCKS OF DELIGNE’S CATEGORY Rep(St).
39
Theorem 6.4. Let Ln := L((1n)) for all n ≥0. The nontrivial block in Rep(S0; F)
has the following associated quiver
with relations: β0α0 = 0, αnαn−1 = 0, βn−1βn = 0, βnαn = αn−1βn−1 for n > 0.
Proof. The indecomposable objects in the block follow from Example 5.10(1). The
fact that the arrows generate all the morphisms between the indecomposable objects
follows from Lemma 5.22 and Lemma 6.3(1)-(4)&(6). By Lemma 6.3(5)-(9), the
relations hold. Finally, the relations imply that the only nonzero compositions of
α’s and β’s are of the form αn (n ≥0), βn (n ≥0), and βnαn (n > 0). By Lemma
6.3(4)&(6), βnαn and sn = idLn are linearly independent. Hence the relations are
exhaustive.
□
Remark 6.5. The block described in Theorem 6.4 is equivalent to the nontrivial
blocks in the Temperley-Lieb category. This can be deduced from the results in
[Wes95, §10].
