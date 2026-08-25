---
doc_id: arxiv-1103.2082v1
doc_title: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St)"
section_id: sec-016-52-the-object-mn
section_title: "The Object Mn"
section_number: 5.2
pages: 9-10
source_pdf: 1103.2082v1.pdf
source_sha256: 0ac5371486b38eac
doc_brief: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St) — Deligne has deﬁned a category which interpolates among the representations of the various symmetric groups."
---
Proposition 5.1. We have the following results about Mn.
(1) Mn =L((1n)) in Rep(S0) for all n≥ 0.
(2) Mn =L((1n))⊕L((1n−1)) in Rep(St) for all n> 0 whenever t⁄= 0.
9
Proof. (1) This is [CO11, Proposition 6.1].
(2) Notice Liftt(Mn) = ([n],sn) for allt∈F (see [CO11,§3.2]). In particular, Liftt(Mn) =
Lift0(Mn) for all t∈ F . Hence, by part (1) along with [CO11, Example 5.10(1), Lemma
5.20(2)], Liftt(Mn) =L((1n))⊕L((1n−1)) for allt∈F . Notice that P(1n)(x) = 1
n!
∏n
k=1(x−k)
for alln> 0 (see [CO11, section 3.5]). Hence L((1n)) is in a nontrivial block of Rep(St) if and
only ift is a nonnegative integer witht⁄∈{ 1,...,n } (see [CO11, Proposition 5.11]). If t is an
integer greater than n, then L((1n)) is the minimal object in a nontrivial block of Re p(St)
(see [CO11, Corollary 5.9]). Hence, by [CO11, Lemma 5.20(1)], Lift t(L((1n))) =L((1n)) for
all n >0, t⁄= 0. Therefore, by [CO11, Proposition 3.12(3)], Mn = L((1n))⊕L((1n−1)) in
Rep(St) for all n> 0, t⁄= 0. □
Corollary 5.2. Supposet andn are nonnegative integers witht<n . Then Mn is a negligible
object in Rep(St).
Proof.Mn is negligible if and only if the image of Mn is zero under the functor Re p(St)→
Rep(St) (see for instance [CO11, Theorem 3.24]). The result now follows from Proposition
5.1 along with [CO11, Proposition 3.25]. □
In the remainder of this section we examine the endomorphisms of Mn.
Proposition 5.3. We have the following equalities.
(1) σsn =snσ = sgn(σ)sn for all σ∈Sn.
(2) snπsn = 0 for all partition diagrams π⁄∈Sn⊔S−
n .
(3) snσisn = sgn(σ)snxnsn for all σ∈Sn, 1≤i≤n.
Proof. Part (1) is clear.
(2) If π⁄∈ Sn⊔S−
n then one of the following is true: (i) two of the top vertices of π are
in the same part; (ii) two of the top vertices of π are in parts of size one; (iii) two of the
bottom vertices of π are in the same part; (iv) two of the bottom vertices of π are in parts
of size one. If (i) or (ii) (resp. (iii) or (iv)) is true, then there exists a transposition τ∈Sn
with πτ = π (resp τπ = π). By part (1) τsn (resp. snτ) is equal to −sn, hence we have
snπsn =snπτsn =−snπsn (resp, snπsn =snτπsn =−snπsn). The result follows since F is
not of characteristic 2.
(3) Suppose σ∈ Sn and i∈{ 1,...n }. If we let τ∈ Sn denote the transposition i↔ n,
thenτσ−1σiτ =xn. Hence, by part (1), snσisn = sgn(σ−1)snτσ−1σiτsn = sgn(σ)snxnsn. □
Corollary 5.4. The set{sn,snxnsn} is a basis of EndRep(St)(Mn) for all t∈F , n> 0.
