---
doc_id: arxiv-2411.04021v1
doc_title: "On the Gram determinants of the Specht modules"
section_id: sec-002-proof-of-theorem-11
section_title: "Proof of Theorem 1.1"
section_number: null
pages: 7-19
source_pdf: 2411.04021v1.pdf
source_sha256: f5b6980f08d25394
toc_source: outline
doc_brief: "On the Gram determinants of the Specht modules — For every partition λ of a positive integer n, let Sλ be the corresponding Specht module of the symmetric group Sn, and let det(λ) ∈Z denote the Gram"
---
Proof of Theorem 1.1
We fix a positive integer n and an even partition λ. Let r be the integer such that
2r ≤n < 2r+1. Our goal is to work towards a proof of Theorem 1.1. The following
definition will be useful:
Definition 3.1. Let M ⊆Podd
λ
be any subset. We say that M is odd if there is a
square-free odd integer d such that
Y
µ∈M
h1
λ(µ)
h2
λ(µ) · (Q×)2 = d · (Q×)2.
Remark 3.2. Recall that det(λ) = m · 2a(2)
λ
for some odd integer m. Now, the
integer a(2)
λ
being even is equivalent to 2a(2)
λ
being a square. Together with Remark
2.11, we conclude that Theorem 1.1 holds true if it can be shown that Podd
λ
is odd,
for any even partition λ.
7
The idea now is to find a suitable set partition
Podd
λ
= M1 ∪M2 ∪· · · ∪Mk
such that each of the Mi is odd.
Definition 3.3. We set an equivalence relation on the set of odd branches of λ by
saying that µ1 ∼µ2 for partitions µ1, µ2 ∈Podd
λ
if and only if D(µ1) = D(µ2). For
any odd branch µ of λ we denote with (µ)∼the equivalence class of µ. We may also
write D((µ)∼) := D(µ).
Example 3.4. Let again λ = (2, 1(5)) as in Example 2.12. Recall that are four odd
branches of λ. We calculate that
D((3, 3, 1)) = D((7)) = D((3, 1(4))) = (3)
and D((5, 1, 1)) = (1, 1, 1), so Podd
λ
decomposes into two equivalence classes.
By definition, for any odd branch µ of λ, we have d(λ, µ) = 2. Since d is a
distance function, it follows that d(λ, D(µ)) ∈{1, 2, 3}. We will first observe that
the case d(λ, D(µ)) = 1 cannot occur.
Lemma 3.5. Let µ be an odd branch of λ. Then d(λ, D(µ)) ∈{2, 3}. Moreover,
2r̸ ∈{h1
λ(µ), h2
λ(µ)}.
Proof. Assume for a contradiction that d(λ, D(µ)) = 1. Choose sequences of β-
numbers βλ := (b1, b2, . . . , bm) and βD(µ) := (b′
1, b2, . . . , bm) for λ and D(µ), respec-
tively. Since λ is a partition of n and D(µ) is a partition of n −2r, it is clear that
b′
1 = b1−2r. By Corollary 2.5 it now follows that D(λ) = D(µ). But now by Lemma
2.4 the parities of fλ and fµ have to be equal, which is a contradiction.
For the second statement we will also be using contradiction, so let βµ :=
(b′
1, b′
2, b3, . . . , bm) be a sequence of β-numbers for µ and assume that either h1
λ(µ)
or h2
λ(µ) is equal to 2r. This implies, after maybe a renumbering, that b′
1 = b1 + 2r
and b′
2 = b2 −2r. Then both βλ −2re2 and βµ −2re1 are sequences of β-numbers for
D(µ) = D(λ), which is again a contradiction to Lemma 2.4.
There are thus two cases remaining for an odd branch µ of λ; either d(λ, D(µ))
is equal to 2 or 3. The case of the distance being 3 is easily understood:
Lemma 3.6. Let µ be an odd branch of λ with d(λ, D(µ)) = 3. Then |(µ)∼| =
1, OddRank(λ) > 0 and D(µ) is an odd branch of D(λ).
Moreover, hi
λ(µ) =
hi
D(λ)(D(µ)) for i = 1, 2.
8
Proof. Let βλ := (b1, b2, b3, . . . , bm) ∈B(λ). After reordering we can assume that
there are h1, h2, h3 ∈Z\{0} such that
βD(µ) := (b1 −h1, b2 −h2, b3 −h3, . . . , bm) ∈B(D(µ)).
For any partition κ ∈(µ)∼, there has to be an index j such that βD(µ)+2rej ∈B(κ).
Since d(λ, κ) = 2, it follows that j ∈{1, 2, 3} and that hj = 2r, assume without loss
of generality that j = 3. By Lemma 3.5 we know that 2r̸ ∈{|h1|, |h2|}, so there can
only be one such index and κ = µ.
Since d(λ, D(µ)) = 3, the entry b3 −h3 = b3 −2r cannot appear in βλ. So
βλ −2re3 = (b1, b2, b3 −2r, . . . , bm) ∈Bn−2r.
By Corollary 2.5 it follows that βλ −2re3 ∈B(D(λ)).
The final statement is easy to see: For the calculation of hi
λ(µ) for i = 1, 2, we
compare the sequences
(b1, b2,b3, . . . , bm),
(b1 −h1, b2 −h2,b3, . . . , bm).
For the calculation of hi
D(λ)(D(µ)) for i = 1, 2, we compare the sequences
(b1, b2,b3 −2r, . . . , bm),
(b1 −h1, b2 −h2,b3 −2r, . . . , bm).
So the numbers clearly coincide. This concludes the proof.
Example 3.7. Let λ = (6, 3, 2) and µ = (6, 4, 1) be an odd branch of λ. Then
d(λ, D(µ)) = 3 with D(λ) = (2, 1) and D(µ) = (3). Moreover, we calculate that
h1
λ(µ) = h1
D(λ)(D(µ)) = 3 and h2
λ(µ) = h2
D(λ)(D(µ)) = 1.
8
7
5
3
2
1
4
3
1
2
1
8
6
5
4
2
1
5
3
2
1
1
Figure 3: Hook diagrams of (6, 3, 2) and (6, 4, 1).
We are left with the case that d(λ, D(µ)) = 2 for an odd branch µ of λ. This case
requires some work, as we have to go over the possible ways the signs of 2r −hi
λ(µ)
for i = 1, 2 can distribute. First we gather some general statements.
Lemma 3.8. Let µ be an odd branch of λ with d(λ, D(µ)) = 2. The following hold:
9
(i) |(µ)∼| ≤4.
(ii) There is a partition κ ∈(µ)∼, which we call a distinguished representative of
(µ)∼, such that the following holds: Let
βλ :=(b1, b2, b3, . . . , bm) ∈B(λ),
βκ :=(b′
1, b′
2, b3, . . . , bm) ∈B(κ)
such that b1 > b2 and b′
1 > b′
2.
Then
βκ −2re1 = (b′
1 −2r, b′
2, b3, . . . , bm) ∈B(D(µ)).
Proof. Let βλ := (b1, b2, . . . , bm) ∈B(λ). We assume that bi > 0 for all i, which
means that the entries of βλ are the hook lengths of the first column of [λ]. After
reordering we can assume that there are h1, h2 ∈Z\{0} such that
βD(µ) := (b1 −h1, b2 −h2, . . . , bm) ∈B(D(µ)).
Assume without loss of generality that b1 > b2 and b1 −h1 > b2 −h2.
An upper bound for |(µ)∼| is the number of indices i such that
dm(βλ, βD(µ) + 2rei) = 2.
There are at most four possibilities for i: Either i = 1, or i = 2, or if there is an
index j (resp. k) such that bj = b1 −2r (resp. bk = b2 −2r), then i could also be
equal to j or k. Thus, |(µ)∼| is at most 4.
For the next claim, first observe that h2 > 0. Indeed, h1 + h2 = 2r, so h2 < 0
implies that h1 > 2r. Then
(b1 −|h2|, b2 + |h2|, . . . , bm) ∈B(µ).
But since b1 > b2, it would follow that µ ⊴λ which is absurd.
Next, we regard the sequence
α := βD(µ) + 2re1 = (b1 −h1 + 2r, b2 −h2, . . . , bm).
If α ∈Bn, then by setting κ := Part(α) we have found a distinguished representative
κ ∈(µ)∼.
So assume that α̸ ∈Bn. This means that the entry b1 −h1 + 2r appears twice
in α, in position 1 and in another position i. Since b1 −h1 > b2 −h2, we know that
i̸ = 2. After a reordering we can assume that i = 3, i.e.,
βλ = (b1, b2, b1 −h1 + 2r, . . . ).
10
Consider the sequence
γ := (b2 −h2 + 2r, b1 −h1, b1 −h1 + 2r, . . . ).
First, since b3 = b1−h1+2r < 2r+1, it holds that b1−h1 < 2r. Clearly b2−h2 ≥0,
it follows that
b2 −h2 + 2r > b1 −h1.
Assume now there is an index j ≥4 such that bj appears in the first or second
entry of γ. Since βD(µ) is a sequence of β-numbers, it follows that bj̸ = b1 −h1. So
then bj = b2 −h2 + 2r. But then both βλ −2re3 and βλ −2rej are sequences of
β-numbers which contradicts Corollary 2.5.
We conclude that γ ∈Bn.
Finally, we can now set κ := Part(γ) to be a
distinguished representative of (µ)∼.
Example 3.9. Let λ = (2, 1(5)) as in the examples 2.12 and 3.4. Let µ1 := (7) and
µ2 := (5, 1, 1). Then d(λ, D(µ1)) = d(λ, D(µ2)) = 2 with the size of their respective
equivalence classes being 3 and 1.
Let βλ := (7, 5, 4, 3, 2, 1) and βµ1 = (12, 0, 4, 3, 2, 1) be sequences of β-numbers
of λ and µ1, respectively. Then βµ1 −4e1 = (8, 0, 4, 3, 2, 1) ∈B((3)). So we see
that (7) is a distinguished representative of its equivalence class. Similarly, we can
confirm the same for µ2.
The following definition gives us a setup to handle the classification of the dis-
tance 2 cases.
Definition 3.10. Let µ be an odd branch of λ with d(λ, D(µ)) = 2 and assume that
µ is a distinguished representative in its equivalence class. We fix some sequences
of β-numbers
βλ :=(b1, b2, b3, . . . , bm) ∈B(λ),
βµ :=(b′
1, b′
2, b3, . . . , bm) ∈B(µ)
with bi > 0 for all i, b1 > b2 and b′
1 > b′
2. Define the sequence
αµ := βµ −2re1 + 2re2 = (b′
1 −2r, b′
2 + 2r, b3, . . . , bm).
Lemma 3.11. Assume we are in the situation of Definition 3.10. Further assume
that h2
λ(µ) > 2r.
(i) Assume that αµ ∈Bn. Then |(µ)∼| = 4. Moreover, (µ)∼is odd.
(ii) Assume that αµ̸ ∈Bn. Then |(µ)∼| = 3. Moreover, OddRank(λ) > 0, D(µ)
is an odd branch of D(λ) and (µ)∼is odd if and only if {D(µ)} ⊆Podd
D(λ) is
odd.
11
Proof. First note that both b1, b2 > 2r. It follows that neither
βλ −2re1 = (b1 −2r, b2, b3, . . . , bm)
nor
βλ −2re2 = (b1, b2 −2r, b3, . . . , bm)
are sequences of β-numbers. Indeed, assume βλ−2rei were a sequence of β-numbers,
for i either 1 or 2. Since all the bj > 0 and bi > 2r, the sequence βλ−2rei corresponds
to the hook lengths of the first column of the partition D(λ) ∈Pn−2r. This is a
contradiction, since b3−i > 2r > n −2r.
So there are indices i, j > 2 with bi = b1 −2r, bj = b2 −2r. In other words, after
a reordering, we have that
βλ = (b1, b2, b1 −2r, b2 −2r, b5, . . . , bm).
We define
γ1 := βλ + (h1
λ(µ) −2r)e2 −(h1
λ(µ) −2r)e3 =
= (b1, b′
1 −2r, b′
2, b2 −2r, b5, . . . , bm) ∈Bn
and
γ2 := βλ + (h2
λ(µ) −2r)e1 −(h2
λ(µ) −2r)e4 =
= (b′
1 −2r, b2, b1 −2r, b′
2, b5, . . . , bm) ∈Bn.
Let κ1 := Part(γ1), κ2 := Part(γ2). It is clear that both γ1 −2re1 and γ2 −2re2
are sequences of β-numbers for D(µ). Thus κ1, κ2 ∈(µ)∼.
If αµ is a sequence of β-numbers, then also αµ −2re2 is a sequence of β-numbers
for D(µ) and thus κ3 := Part(αµ) ∼µ. So
(µ)∼= {µ, κ1, κ2, κ3}
with
Y
ν∈(µ)∼
h1
λ(ν)
h2
λ(ν) = h1
λ(µ)
h2
λ(µ) ·
h2
λ(µ)
h1
λ(µ) −2r ·
h1
λ(µ)
h2
λ(µ) −2r · h1
λ(µ) −2r
h2
λ(µ) −2r =

h1
λ(µ)
h2
λ(µ) −2r
2
and so (µ)∼is odd.
If on the other hand αµ is not a sequence of β-numbers, then the entry b′
2 + 2r
already appears somewhere in βλ. So after reordering, βλ is of the form
(b1, b2, b1 −2r, b2 −2r, b′
2 + 2r, . . . , bm).
12
Thus OddRank(λ) > 0 and
βλ −2re5 = (b1, b2, b1 −2r, b2 −2r, b′
2, . . . , bm) ∈B(D(λ)).
Moreover,
(µ)∼= {µ, κ1, κ2}
and it is clear that D(µ) ∈Podd
λ
with hk
D(λ)(D(µ)) = hk
λ(µ) −2r for k = 1, 2 from
which the statement follows.
Example 3.12.
(i) Let λ = (4, 4, 2, 2, 1, 1, 1) and let µ = (13, 1, 1). Then µ is an
odd brach of λ with d(λ, D(µ)) = 2 and µ is a distinguished representative.
Moreover,
(µ)∼= {µ, (5, 5, 2, 2, 1), (5, 4, 2, 2, 1, 1), (5, 3, 2, 2, 1, 1, 1)}
and we are in the situation of Lemma 3.11(i).
(ii) It is easy to confirm that the partitions λ = (2, 1(5)) and µ = (7) as in the
previous examples are an instance of Lemma 3.11(ii).
Lemma 3.13. Assume we are in the situation of Definition 3.10. Further assume
that h1
λ(µ) < 2r.
(i) Assume that αµ ∈Bn. Then |(µ)∼| = 2. Moreover, (µ)∼is odd.
(ii) Assume that αµ̸ ∈Bn. Then |(µ)∼| = 1. Moreover, OddRank(λ) > 0, D(µ)
is an odd branch of D(λ) and (µ)∼is odd if and only if {D(µ)} ⊆Podd
D(λ) is
odd.
Proof. One sees easily that the assumption implies that |(µ)∼| ≤2. Thus, if αµ ∈Bn
then
(µ)∼= {µ, Part(αµ)}
with
Y
ν∈(µ)∼
h1
λ(ν)
h2
λ(ν) = h1
λ(µ)
h2
λ(µ) · 2r −h2
λ(µ)
2r −h1
λ(µ)
and thus (µ)∼is odd.
So assume now that αµ̸ ∈Bn. We can now argue as in Lemma 3.11 and see that
OddRank(λ) > 0 and D(µ) ∈Podd
D(λ). Moreover, (µ)∼= {µ} and
hi
D(λ)(D(µ)) = 2r −h3−i
λ (µ)
for i = 1, 2, which shows the claim.
13
Example 3.14.
(i) Let λ = (6, 3, 2, 1), µ1 = (9, 1, 1, 1) and µ2 = (7, 2, 2, 1) be
partitions of 12. Then µ1 and µ2 are odd branches of λ with d(λ, D(µ1)) = 2
and (µ1)∼= {µ1, µ2}. Both µ1 and µ2 are distinguished representatives in
their equivalence class and we are in the situation of Lemma 3.13(i).
(ii) Let λ = (5, 5, 2, 1) and let µ = (7, 6) be partitions of 13.
Then µ is an
odd branch of λ with d(λ, D(µ)) = 2 and µ is a distinguished representative.
Moreover,
(µ)∼= {µ}
and we are in the situation of Lemma 3.13(ii).
Lemma 3.15. Assume we are in the situation of Definition 3.10. Further assume
that h1
λ(µ) > 2r, h2
λ(µ) < 2r.
(i) If there is an index i ≥3 with b1 −bi = 2r, then |(µ)∼| = 2. Moreover, (µ)∼is
odd.
(ii) If there does not exist an index i with b1 −bi = 2r, then |(µ)∼| = 1. Moreover,
OddRank(λ) > 0, D(µ) is an odd branch of D(λ) and (µ)∼is odd if and only
if {D(µ)} ⊆Podd
D(λ) is odd.
(iii) If b1 −b2 = 2r, then |(µ)∼| = 1. Moreover, (µ)∼is odd.
Proof. Unlike in the lemmas 3.11 and 3.13, there is no partition in Podd
λ
that can
come from αµ. Assume that αµ ∈Bn. Then b1 > b1 + h2
λ(µ) −2r = b′
1 −2r since
h2
λ(µ) < 2r and b1 > b1 −h1
λ(µ) + 2r = b′
2 + 2r since h1
λ(µ) > 2r. It thus follows that
Part(αµ) ⊴λ, so indeed, Part(αµ) is not a branch of λ.
Next, we convince ourselves that b2 < 2r. Assume by contradiction that b2 ≥2r,
so b2 + h1
λ(µ) = b′
1 > 2r+1. This means that b′
1 can not be the hook length of any
c ∈[λ], in particular, there has to be an entry in βµ that is equal to 0. Since all
the entries bi > 0, it follows that b′
2 = 0. But then b2 = h2
λ(µ) < 2r by assumption,
which is a contradiction. So |(µ)∼| ≤2 now follows by the discussion in the proof
of Lemma 3.8(i).
Let us now discuss the case of |(µ)∼| = 2. For this to occur, there has to be an
index i ≥3 such that b1 −bi = 2r. Assume this is the case; after some reordering
we can assume that i = 3. So
βλ = (b1, b2, b1 −2r, b4, . . . , bm).
Let
γ := βλ + h2
λ(µ)e3 −h2
λ(µ)e2 =
= (b1, b′
2, b′
1 −2r, b4, . . . , bm) ∈Bn.
14
Let κ := Part(γ).
It is easy to see that κ ∈Podd
λ
and that (µ)∼= {µ, κ}. If
b2 > b1 −2r, then
h1
λ(κ) = h2
λ(µ), h2
λ(κ) = h1
λ(µ) −2r.
If b2 < b1 −2r, then
h1
λ(κ) = h1
λ(µ) −2r, h2
λ(κ) = h2
λ(µ).
In both cases, (µ)∼is odd.
So in all other cases, |(µ)∼| = 1. Assume that there is no index i such that
b1 −bi = 2r. Then OddRank(λ) > 0 and
(b1 −2r, b2, . . . , bm) ∈B(D(λ)).
Moreover, we see that D(µ) is an odd branch of D(λ). We have the same case
distinction as before: If b2 > b1 −2r, then
h1
D(λ)(D(µ)) = h2
λ(µ), h2
D(λ)(D(µ)) = h1
λ(µ) −2r.
If b2 < b1 −2r, then
h1
D(λ)(D(µ)) = h1
λ(µ) −2r, h2
D(λ)(D(µ)) = h2
λ(µ).
To finish the proof, assume now that b1 −b2 = 2r. Then h1
λ(µ) = h2
λ(µ) + 2r and
so (µ)∼is odd. The statement now follows.
Example 3.16.
(i) Let λ = (4, 2(4), 1(3)) and let µ = (5, 2(4), 1, 1). Then µ is an
odd branch of λ with d(λ, D(µ)) = 2 and µ is a distinguished representative.
Moreover,
(µ)∼= {µ, (4, 2(5), 1)}
and we are in the situation of Lemma 3.15(i).
(ii) Let λ = (10, 2) and let µ = (11, 1).
Then µ is an odd branch of λ with
d(λ, D(µ)) = 2 and µ is a distinguished representative. Moreover,
(µ)∼= {µ}
and we are in the situation of Lemma 3.15(ii).
(iii) Let λ = (2, 1(5)) and let µ = (5, 1, 1), as seen in Example 3.9. Then µ is an
odd branch of λ with d(λ, D(µ)) = 2 and µ is a distinguished representative.
Moreover,
(µ)∼= {µ}
and we are in the situation of Lemma 3.15(iii).
15
We gather the previous results in the following statement:
Corollary 3.17. Let µ be an odd branch of λ. Then at least one of the following is
true:
(i) (µ)∼is odd.
(ii) OddRank(λ) > 0, D(µ) is an odd branch of D(λ) and (µ)∼is odd if and only
if {D(µ)} ⊆Podd
D(λ) is odd.
We need one final piece to finish the puzzle:
Lemma 3.18. Assume OddRank(λ) > 0 and let κ be an odd branch of D(λ). Then
there is an odd branch µ of λ such that D(µ) = κ and (µ)∼is odd if and only if
{κ} ⊆Podd
D(λ) is odd.
Proof. Let
βλ := (b1, b2, b3, . . . , bm) ∈B(λ)
and assume that, after a suitable reordering,
(b1 −2r, b2, b3, . . . , bm) ∈B(D(λ)).
There are two indices i, j and a positive integer h such that
βλ −2re1 + hei −hej ∈B(κ)
and bi > bj. There are three possibilities: Either 1 /∈{i, j}, or i = 1, or j = 1. We
will regard
α := βλ + hei −hej.
Assume first that 1 /∈{i, j}. After a reordering we can assume that i = 2, j = 3.
There are three further possibilities: Either α ∈Bn, or b1 = b3 −h, or b1 = b2 + h.
If α ∈Bn, then it is clear that we can set µ := Part(α) with µ ∈Podd
λ
and that
d(λ, κ) = 3. We are thus in the situation of Lemma 3.6 and we are done.
Assume now that b1 = b3 −h. Then
γ := (b1 −2r, b2 + h + 2r, b3 −h, b4, . . . , bm) ∈Bn.
If we now set µ := Part(γ), then clearly µ ∈Podd
λ
and d(λ, κ) = 2. Moreover, µ is
a distinguished representative of its equivalence class and
h1
λ(µ) = b2 −b3 + h + 2r, h2
λ(µ) = h + 2r,
so we are in the case of Lemma 3.11(ii).
16
Assume now that b1 = b2 + h. Here, we can set
γ := (b1 −2r, b2 + h, b3 −h + 2r, b4, . . . , bm) ∈Bn.
We again set µ := Part(γ) and again, d(λ, κ) = 2 and µ is a distinguished represen-
tative of its equivalence class. We calculate that
h1
λ(µ) = 2r −h, h2
λ(µ) = 2r −(b2 −b3 + h),
so we are in the case of Lemma 3.13(ii).
Being done with that case, we can now assume that either i = 1 or j = 1. After
reordering, we have
(b1 −2r + δh, b2 −δh, b3, . . . , bm) ∈B(κ)
for
δ =
(
1,
if i = 1,
−1,
if j = 1.
We set
γ := (b1 −2r + δh, b2 −δh + 2r, b3, . . . , bm) ∈Bn
and let µ := Part(γ) be the corresponding partition. It is easy to see that d(λ, κ) = 2
and µ is a distinguished representative of its equivalence class. We quickly confirm
that we are in the case of Lemma 3.15(iii). This concludes the proof.
We can now finally prove the main theorem:
Proof. (of Theorem 1.1) We will show that Podd
λ
is odd by induction on the oddness
rank of λ. To begin, the statement for OddRank(λ) = 0 immediately follows by
Corollary 3.17.
So assume now OddRank(λ) > 0 and that we know the result to hold for D(λ).
We define the set
M := D−1(Podd
D(λ)) ⊆Podd
λ
,
where the subset relation holds by Lemma 2.4.
We decompose
Podd
λ
= M ∪M ′
for some other set M ′ ⊆Podd
λ
into a disjoint union. Lemma 3.18 tells us that M
is odd if and only if Podd
D(λ) is odd, which we know by the induction hypothesis.
Moreover, for all µ ∈M ′, it holds that D(µ) is not an odd branch of D(λ) and so
by Corollary 3.17, the set (µ)∼is odd; it follows that the whole set M ′ must be odd,
and so Podd
λ
is odd. The theorem now follows by Remark 3.2.
17
Remark 3.19. We have confirmed that a(2)
λ
is even for any even partition λ. So if
there is a partition µ such that a(2)
µ
is odd, then µ must necessarily be odd as well.
The reason this can occur for odd partitions relies critically in the failure of Lemma
3.5. We denote
A(n) := #{µ ∈Pn | aµ is odd}.
and
B(n) := #{µ ∈Pn | µ is odd}.
It is clear that B(n) is an upper bound for A(n); an explicit formula for B(n)
can be found in [8]. With some code in GAP [3], we calculated the values of A(n)
for 1 ≤n ≤100.
n
1
2
3
4
5
6
7
8
9
10
A(n)
0
1
1
2
2
4
4
4
4
4
B(n)
1
2
2
4
4
8
8
8
8
16
n
11
12
13
14
15
16
17
18
19
20
A(n)
8
20
16
32
32
8
8
16
16
24
B(n)
16
32
32
64
64
16
16
32
32
64
n
21
22
23
24
25
26
27
28
29
30
A(n)
24
64
64
64
64
128
128
256
256
512
B(n)
64
128
128
128
128
256
256
512
512
1024
n
31
32
33
34
35
36
37
38
39
40
A(n)
480
16
16
28
32
68
64
128
128
112
B(n)
1024
32
32
64
64
128
128
256
256
256
Table 1: The values of A(n) and B(n) for the first 40 values of n.
Some patterns are easily observed: It seems that A(n) = B(n)/2 in most cases;
for 1 ≤n ≤100, this holds true for 75 values of n. Moreover, it holds that the
difference B(n)/2 −A(n) ≥0 with only a few exceptions; these being n = 12, 36,
48, 54, 91 and 92 for n ≤100. The values of |B(n)/2 −A(n)| seem to be either
an integer power of 2, or a multiple of 12; the nonzero multiples of 12 occurring for
n = 41, 54, 61, 90 and 93 for n ≤100.
Acknowledgments. I want to thank Gabriele Nebe and Jonas Hetz for their feed-
back on parts of this paper. This paper is a contribution to Project-ID 286237555
– TRR 195 – by the Deutsche Forschungsgemeinschaft (DFG, German Research
Foundation).
18
References
[1] Arvind Ayyer, Amritanshu Prasad, and Steven Spallone.
Odd partitions in
Young’s lattice. Sém. Lothar. Combin., 75:Art. B75g, 13, 2015.
[2] Richard Dipper and Gordon James. Blocks and idempotents of Hecke algebras
of general linear groups. Proc. London Math. Soc. (3), 54(1):57–82, 1987.
[3] The GAP Group.
GAP – Groups, Algorithms, and Programming, Version
4.13.1, 2024.
[4] Linda Hoyer. Orthogonal Determinants of Finite Groups of Lie Type. PhD
thesis, RWTH Aachen University, 2024.
[5] I. M. Isaacs, Gabriel Navarro, Jørn B. Olsson, and Pham Huu Tiep. Character
restrictions and multiplicities in symmetric groups. J. Algebra, 478:271–282,
2017.
[6] G. D. James and G. E. Murphy. The determinant of the Gram matrix for a
Specht module. J. Algebra, 59(1):222–235, 1979.
[7] G.D. James and A. Kerber.
The Representation Theory of the Symmetric
Group. Encyclopedia of mathematics and its applications. Addison-Wesley Pub-
lishing Company, Advanced Book Program, 1981.
[8] I. G. Macdonald. On the degrees of the irreducible representations of symmetric
groups. Bull. London Math. Soc., 3:189–192, 1971.
[9] Gabriele Nebe. On orthogonal discriminants of characters. Albanian J. Math.,
16(1):41–49, 2022.
[10] Gabriele Nebe. Orthogonal determinants of characters. Arch. Math. (Basel),
119(1):19–26, 2022.
[11] Yukio Tsushima. On some simple constituents of the Specht modules of the
symmetric groups. J. Algebra, 243(1):131–141, 2001.
19
