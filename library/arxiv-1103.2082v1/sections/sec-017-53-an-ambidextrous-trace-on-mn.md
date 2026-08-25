---
doc_id: arxiv-1103.2082v1
doc_title: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St)"
section_id: sec-017-53-an-ambidextrous-trace-on-mn
section_title: "An Ambidextrous Trace on Mn"
section_number: 5.3
pages: 10-14
source_pdf: 1103.2082v1.pdf
source_sha256: 0ac5371486b38eac
doc_brief: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St) — Deligne has deﬁned a category which interpolates among the representations of the various symmetric groups."
---
to deﬁne a linear functional on End Rep(St)(Mn) it suﬃces to give the values of the linear
functional on sn and snxnsn. Let tn be the following linear map:
tn : EndRep(St)(Mn) → F
sn ↦→ 1
snxnsn ↦→ 1
Notice that t1 is the ambidextrous trace on M1 = L(2) in Re p(S0) studied in section 4.
In this section we will show that tn is an ambidextrous trace on Mn in Re p(St) for all
t∈ F , n >0. To do so, we must examine the endomorphism ring End Rep(St)(Mn⊗Mn) =
(sn⊗sn)FP 2n(t)(sn⊗sn).
10
For the remainder of this section assume n> 0. Given a partition diagram π∈P2n, write
πL (resp. πR) for the partition diagram in Pn obtained by restricting the partition π to the
vertices{1, 1′,...,n,n ′} (resp.{n + 1, (n + 1)′,..., 2n, (2n)′}). For example,
.
Finally, let Θ1, Θ2 :P2n→ EndRep(St)(Mn) be the maps given by
.
The following lemma is the ﬁrst of three lemmas concerning Θ 1 and Θ 2 which will be used
to show that tn is an ambidextrous trace.
Lemma 5.5. Supposeπ∈P2n is a partition diagram such thatπL⁄∈Sn⊔S−
n orπR⁄∈Sn⊔S−
n .
Then Θ1(π) = 0 = Θ2(π).
Proof. If πL ⁄∈ Sn⊔S−
n then (arguing as in the proof of Proposition 5.3) there exists a
transposition τ∈Sn with π(τ⊗ Idn) =π or (τ⊗ Idn)π =π. Thus
In either case, by Proposition 5.3(1), Θ 1(π) =−Θ1(π) and hence Θ 1(π) = 0 as the charac-
teristic of F is not 2. Moreover,
Using Proposition 5.3(1) again, we have Θ 2(π) = −Θ2(π) so that Θ 2(π) = 0. The proof
when πR⁄∈Sn⊔S−
n is similar. □
Now for the second lemma on Θ 1 and Θ 2. In this lemma, the symbol ≥ refers to the
partial order on partition diagrams found in [CO11, Section 2.1].
Lemma 5.6. Supposeπ∈P2n is such that πL,πR∈Sn⊔S−
n . If πL (resp. πR) is in S−
n then
there exists a partition diagram π′∈P2n with π′
L (resp. π′
R) in Sn such that π′
R≥πR (resp.
π′
L≥πL) and tn(Θi(π′)) = tn(Θi(π)) for i = 1, 2.
Proof. Suppose πL∈S−
n so that πL =σi for some σ∈Sn and i∈{ 1,...,n }. Let π′∈P2n
be the partition diagram obtained from π by adding an edge between the vertices labelled i
11
andσ(i)′. Then π′≥π which impliesπ′
R≥πR. Also, π′
L =σ∈Sn. Moreover, given τ∈Sn,
the connected components of the graph
(5.6)
are all cycles. Hence, as the graph of
(5.7)
is obtained from (5.6) by deleting one edge, the partitions of {1, 1′,...,n,n ′} corresponding
to the connected components of (5.6) and (5.7) are equal. Therefore,
for every τ∈Sn. Hence
which implies Θ 2(π′) = Θ2(π).
Now, ﬁx ρ∈Sn and let µρ,µ′
ρ∈Pn, 𝓁(ρ),𝓁 (ρ)′∈ Z≥0 be such that
.
Notice that𝓁(ρ) (resp. 𝓁(ρ)′) is the number of connected components of the partition diagram
π(Idn⊗ρ) (resp. π′(Idn⊗ρ)) which only contain vertices labelled by integers greater than n.
The connected components of π andπ′ (and hence of π(Idn⊗ρ) and π′(Idn⊗ρ)) which only
contain vertices labelled by integers greater than n are identical. Hence 𝓁(ρ) = 𝓁(ρ)′. Also,
it is easy to see that µρ≥ πL. Thus, as πL∈ S−
n , there are three cases: (i) µρ = πL, (ii)
µρ =π′
L, (iii)µρ⁄∈Sn⊔S−
n . Next, we show that tn(snµρsn) = tn(snµ′
ρsn) in each of the three
cases above:
(i) Ifµρ =πL =σi then it is easy to see thatµ′
ρ =π′
L =σ. Hence, by Proposition 5.3(1)&(3)
and the deﬁnition of tn, tn(snµρsn) = sgn(σ) = tn(snµ′
ρsn).
(ii) If µρ =π′
L then µ′
ρ =π′
L too. Hence tn(snµρsn) = tn(snµ′
ρsn).
(iii) If µρ⁄∈Sn⊔S−
n then µ′
ρ⁄∈Sn⊔S−
n too. Therefore, by Proposition 5.3(2), tn(snµρsn) =
0 = tn(snµ′
ρsn).
As ρ was an arbitrary element of Sn, we have
tn(Θ1(π)) =
∑
ρ∈Sn
sgn(ρ)t𝓁(ρ) tn(snµρsn) =
∑
ρ∈Sn
sgn(ρ)t𝓁(ρ)′
tn(snµ′
ρsn) = tn(Θ1(π′)).
The statement of the lemma with πL∈S−
n follows. The proof when πR∈S−
n is similar. □
12
Before proving the third and ﬁnal lemma on Θ 1 and Θ 2 we need to introduce a bit more
notation. Suppose π∈ P2n is such that πL,πR∈ Sn. Let I = Iπ⊂{ 1,...,n } denote the
set of all i∈{ 1,...,n } which correspond to vertices in π whose parts are of size two. Now
let πL−R = σI where σ∈ Sn is any permutation with σ(i) = j whenever the top vertices
labelled by i and n +j are in the same part of π. For example,
.
The following proposition concerning πL−R will be used in the proof of the ﬁnal lemma on
Θ1 and Θ2.
Proposition 5.7. Suppose π∈ P2n is such that πL,πR∈ Sn. If π′∈ P2n has π′
L = πL,
π′
R =πR, and π′
L−R =πL−R, then π′ =π.
Proof. Since πL,πR∈ Sn, each part of π is of one of the following three types: (i) {i,j′}
with 1 ≤ i,j ≤ n; (ii) {i,j′} with n < i,j≤ 2n; (iii) {i,j′,k,l ′} with 1 ≤ i,j ≤ n and
n<k,l ≤ 2n. Hence π is completely determined by πL,πR, and πL−R. □
Lemma 5.8. If π∈P2n is such that πL,πR∈Sn, then Θ1(π) = Θ2(π).
Proof. Write I = Iπ as above and let σ∈ Sn be any permutation with πL−R = σI. Let
µ,µ′∈P2n be the following partition diagrams
.
It is easy to check that µL = πR = µ′
L, µR = πL = µ′
R, and µL−R = (σ−1)J = µ′
L−R
where J ={σ(i)| i∈ I}. Hence, by Proposition 5.7, µ = µ′. Also, by Proposition 5.3(1),
Θ1(π) = Θ1(µ). Therefore Θ 1(π) = Θ1(µ) = Θ1(µ′) = Θ2(π). □
Now we prove the main result of this section.
Theorem 5.9. tn is a nonzero ambidextrous trace on Mn in Rep(St) for all t∈F , n> 0.
Proof. We are required to show tn(Θ1(π)) = tn(Θ2(π)) for all π∈P2n. If either πL or πR is
not inSn⊔S−
n then the result follows from Lemma 5.5. Hence we can assumeπL,πR∈Sn⊔S−
n .
IfπL∈S−
n then by Lemma 5.6 there existsπ′∈P2n withπ′
L∈Sn and tn(Θi(π′)) = tn(Θi(π))
for i = 1, 2. If π′
R⁄∈ Sn⊔S−
n then by Lemma 5.5 we have tn(Θi(π)) = tn(Θi(π′)) = 0 for
i = 1, 2; hence we can assume π′
R∈ Sn⊔S−
n . If π′
R∈ S−
n then by Lemma 5.6 there exists
π′′∈P2n with π′′
R∈Sn, π′′
L≥π′
L, and tn(Θi(π′′)) = tn(Θi(π′)) for i = 1, 2. If π′′
L⁄∈Sn⊔S−
n
then by Lemma 5.5 we have tn(Θi(π)) = tn(Θi(π′′)) = 0 for i = 1, 2; hence we can assume
π′′
L∈Sn⊔S−
n . Also, since π′′
L≥π′
L andπ′
L∈Sn it follows thatπ′′
L⁄∈S−
n . Thus, we can assume
π′′
L∈Sn. In this case, by Lemma 5.8, tn(Θ1(π)) = tn(Θ1(π′′)) = tn(Θ2(π′′)) = tn(Θ2(π)). □
Corollary 5.10. Ift∈ Z≥0 then there exists a nonzero trace on the ideal of negligible objects
in Rep(St).
13
Proof. This follows from Theorem 2.4 and Theorem 5.9 that there is a nonzero trace onIMn.
By Corollary 5.2 we have that Mn is an object in I =I(N ) and, hence, IMn ⊆I . By
Lemma 2.6 we haveJ(IMn) is not the zero ideal and J(IMn)⊆J(I). By the classiﬁcation of
tensor ideals in Rep(St),N is the unique proper tensor ideal of Rep(St). Thus J(IMn) =J(I)
and by Lemma 2.6 IMn =I. This proves the trace function is in fact deﬁned on the entire
ideal of negligible objects in Re p(St). □
Remark 5.11. When t /∈ Z≥0 then Re p(St) is a semisimple category [Del07, Th´ eor` eme
2.18]. Consequently, there are no proper ideals in Re p(St) and the categorical trace is the
only nontrivial trace.
6. A Graded V ariation on Deligne’s Category
In this section we brieﬂy examine a graded version of Deligne’s category and show that it
can be used to recover the writhe of a knot – a well-known invariant of framed knots.
