---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-010-6-proofs-of-theorem-16-and-corollary-17
section_title: "Proofs of Theorem 1.6 and Corollary 1.7"
section_number: 6
pages: 19-21
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
With the preparation in the previous section, we can finally prove Theorem 1.6 and Corollary
1.7.
Proof of Theorem 1.6.Letn≥5, and letSbe a nonempty normal set inS n. LetA S,BS and
CS be as in (3). ThenS=A S∪B S∪C S. Since Cay(S n,S) is normal, by (6) and Table 1,
its eigenvalue corresponding to the partition (n−1,1) is
λ(n−1,1) =
∑
σ∈S
˜χ(n−1,1)(σ)
= 1
n−1
∑
σ∈S
(|fix(σ)|−1)
= 1
n−1

 ∑
σ∈AS
(|fix(σ)|−1)−
∑
σ∈CS
1


= 1
n−1



 ∑
σ∈AS
|fix(σ)|

−(|AS|+|C S|)

.(12)
By our assumption (5) and equation (12), we haveλ (n−1,1)≤1.
Necessity.Suppose that Cay(S n,S) has the Aldous property. Then its strictly second
largest eigenvalue, which is attained by the standard representationρ (n−1,1), isλ (n−1,1)≤1.
By Theorem 5.5, we haveS∈{S n\{e},S n\An,An\{e}}.
Sufficiency.IfS=S n\{e}, then Cay(S n,S) ∼= Kn! has spectrum{(n!−1) 1,(−1)n!−1}.
The eigenvaluen!−1 is attained byρ (n), while the strictly second largest eigenvalue−1 is
attained byρ (n−1,1).
IfS=S n\A n, then Cay(Sn,S) ∼= Kn!/2,n!/2 has spectrum
{(
n!
2
)1
,0n!−2,
(
−n!
2
)1}
.The
eigenvalue n!
2 is attained byρ (n), the eigenvalue− n!
2 is attained byρ (1n), and the strictly
second largest eigenvalue 0 is attained byρ (n−1,1).
IfS=A n\{e}, then Cay(S n,S) ∼= 2Kn!/2 has spectrum
{(
n!
2−1
)2
,(−1)n!−2
}
.The
eigenvalue n!
2−1 is attained by bothρ (n) andρ (1n), while the strictly second largest eigenvalue
−1 is attained byρ (n−1,1).
19
Therefore, in all three cases, Cay(Sn,S) has the Aldous property. Moreover, since in each
case the strictly second largest eigenvalue isλ (n−1,1)≤1, it follows from (12) that all three
setsSsatisfy (5).
This proves the sufficiency and completes the proof.
Proof of Corollary 1.7.Letn≥5, and letSbe a nonempty normal set inS n.
(a) Suppose thatS⊆Supp n({n−1,n}). ThenA S =∅, soSsatisfies condition (5). Hence
Theorem 1.6 applies to Cay(Sn,S). Sincen≥5, each ofS n\{e},Sn\An andA n\{e}contains
an element whose support size is neithern−1 norn. Thus,S /∈{S n\{e},S n\An,An\{e}}
and therefore, by Theorem 1.6, Cay(S n,S) does not have the Aldous property.
(b) Suppose that| AS|−| CS|+ 2(n−1)≥0 andS /∈{S n\{e},S n\A n,An\{e}}. By
(3) and (4),{A S,AS,BS,BS,CS,CS}is a partition ofS n\{e}. Hence
|AS|+| AS|+|B S|+| BS|+|C S|+| CS|=n!−1.(13)
Set
X={(σ,i)∈S n×[n] :σ(i) =i}.
We use double counting to enumerateX. First, for each fixedi, there are exactly (n−1)!
permutationsσ∈S n satisfyingσ(i) =i. Therefore,
|X|=
n∑
i=1
|{σ∈S n :σ(i) =i}|=
n∑
i=1
(n−1)! =n!.(14)
Second, each permutationσcontributes exactly|fix(σ)|to the cardinality ofX. Thus,
|X|=
∑
σ∈Sn
|fix(σ)|
=
n∑
k=0
∑
σ∈Suppn(k)
|fix(σ)|
=
∑
σ∈Suppn(0)
|fix(σ)|+
∑
σ∈Suppn(1)
|fix(σ)|+
n−1∑
k=2
∑
σ∈Suppn(k)
|fix(σ)|+
∑
σ∈Suppn(n)
|fix(σ)|
=n+ 0 +
n−1∑
k=2
∑
σ∈Suppn(k)
|fix(σ)|+ 0
=n+
∑
σ∈Suppn({2,3,...,n−2})
|fix(σ)|+
∑
σ∈Suppn(n−1)
|fix(σ)|.
This together with (13) and (14) yields
∑
σ∈AS
|fix(σ)|+
∑
σ∈AS
|fix(σ)|=
∑
σ∈Suppn({2,3,...,n−2})
|fix(σ)|
=n!−n−
∑
σ∈Suppn(n−1)
|fix(σ)|(15)
20
=n!−n−
∑
σ∈BS
|fix(σ)|−
∑
σ∈BS
|fix(σ)|
=n!−n−|B S|−| BS|
=|A S|+| AS|+|C S|+| CS|+ 1−n.
Since| AS|−| CS|+ 2(n−1)≥0 by our assumption, it follows that
|AS|+|C S|+n−1−
∑
σ∈AS
|fix(σ)|=
∑
σ∈AS
|fix(σ)|−| AS|−| CS|+ 2(n−1)
=
∑
σ∈AS
(|fix(σ)|−1)−| CS|+ 2(n−1)
≥|AS|−| CS|+ 2(n−1)
≥0.
That is,Ssatisfies condition (5). SinceS /∈{S n\{e},S n\An,An\{e}}by our assumption,
it follows from Theorem 1.6 that Cay(S n,S) does not have the Aldous property.
(c) Suppose that Supp n(n)⊆SandS̸=S n\{e}. Since Supp n(n) contains both even
and odd permutations,Sis neitherS n\A n norA n\{e}. Moreover,C S = Suppn(n) and
hence CS =∅. Thus,| AS|−| CS|+ 2(n−1) =| AS|+ 2(n−1)≥0 and therefore by (b),
Cay(Sn,S) does not have the Aldous property.
AcknowledgementsChenhui Lv was supported by the Outstanding Doctoral Students
Overseas Study Program of the University of Science and Technology of China. Sanming Zhou
was supported by a Discovery Project (DP250104965) of the Australian Research Council.
