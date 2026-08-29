---
doc_id: arxiv-math-0701051v4
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA"
section_id: sec-006-21-young-symmetrizer
section_title: "Young symmetrizer"
section_number: 2.1
pages: 5-7
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA — We prove an upper bound for characters of the symmetric groups."
---
In the following we will distinguish the symmetric group Sn which per-
mutes the elements {1, . . . , n} and the symmetric group ˜Sn which permutes
the boxes of λ.
For a box □ ∈ λ we denote by r(□ ) ∈ N (respectively, c(□ ) ∈ N) the
row (respectively, the column) of □ ; in this way □ = (c(□ ), r(□ )).
If σ ∈ ˜Sn has a property that if two different boxes □ 1, □ 2 are in the
same row then their images σ(□ 1), σ(□ 2) are not in the same column then
we deﬁne its number of column inversions cinv(σ) as the number of pairs
□ 1, □ 2 such that σ(□ 1), σ(□ 2) are in the same column, r(□ 1) < r (□ 2)
and r(σ(□ 1)) > r (σ(□ 2)). If σ ∈ ˜Sn does not have this property, then we
deﬁne (−1)cinv(σ) = 0.
The following theorem gives a very esthetically appealing f ormula for
the characters of the symmetric groups.
Theorem 4. Let a Young diagram λ having n boxes and π ∈ Sn be given.
Let ˆπ ∈ ˜Sn be a random permutation distributed with the uniform distribu-
tion on the conjugacy class deﬁned by π. Then
χλ(π) = E[(−1)cinv(ˆπ)].
Proof. We denote
Pλ ={σ ∈ ˜Sn : σ preserves each row of λ},
Qλ ={σ ∈ ˜Sn : σ preserves each column of λ}
and deﬁne
aλ =
∑
σ∈Pλ
σ ∈ C[ ˜Sn],
bλ =
∑
σ∈Qλ
(−1)|σ|σ ∈ C[ ˜Sn],
cλ =bλaλ.
It is well-known that pλ = αλcλ is an idempotent for a constantαλ which
will be speciﬁed later. Its image Vλ = C[ ˜Sn]pλ under multiplication from
the right on the regular representation gives a representat ion ρλ (where the
symmetric group acts by left multiplication) associated to a Young diagram
λ. It turns out that αλ = dim Vλ
n! . It follows that for ˜π ∈ ˜Sn
(8) n! Trρλ(˜π)
dim Vλ
= Trρλ(˜π−1)
αλ
= 1
αλ
∑
µ∈ ˜Sn
⟨δµ, ˜π−1δµpλ⟩ =
∑
µ∈ ˜Sn
∑
˜σ1∈Qλ
∑
˜σ2∈Pλ
(−1)|˜σ1|[µ = ˜π−1µ˜σ1˜σ2].
6 V ALENTIN FÉRAY AND PIOTR ´SNIADY
We deﬁne ˆπ = µ−1˜πµ. For such a permutation ˆπ there exists at most
one factorization ˆπ = ˜σ1˜σ2; by Young lemma this factorization exists if
and only if (−1)cinv(ˆπ) ⁄= 0. Furthermore, if such a factorization exists then
(−1)|σ1| = (−1)cinv(ˆπ). It follows that
n! Trρλ(˜π)
dim Vλ
=
∑
µ∈ ˜Sn
(−1)cinv(µ−1 ˜πµ).
As µ runs over all permutations, ˆπ = µ−1˜πµ runs over all elements of the
conjugacy class deﬁned by π which ﬁnishes the proof. □
For permutations σ1, σ2 ∈ Sl we deﬁne ˜N λ(σ1, σ2) as the number of one-
to-one functions f from {1, . . . , l} to the set of boxes of λ with a property
that r ◦ f is constant on each cycle of σ2 and c ◦ f is constant on each cycle
of σ1.
Proposition 5. Let λ be a Young diagram having n boxes. For any permu-
tation π ∈ Sl (where l ≤ n)
Σ λ(π) =
∑
σ1,σ2∈Sl
σ1σ2=π
(−1)|σ1| ˜N λ(σ1, σ2).
Proof. Let us consider the case l = n. Let ˜π ∈ ˜Sn be any permutation with
the same cycle structure as π ∈ Sn. Our starting point is the analysis of (8).
Notice that the multliset of the values of µ−1˜πµ (over µ ∈ ˜Sn) coincides
with the multiset of the values of f ◦ π ◦ f −1 (over bijections f). We deﬁne
σi = f −1 ◦ ˜σi ◦ f; then condition µ = ˜π−1µ˜σ1˜σ2 is equivalent to π = σ1σ2.
It is easy to check that ˜σ1 ∈ Qλ if and only if c ◦ f is constant on each cycle
of σ1 and ˜σ2 ∈ Pλ if and only if r ◦ f is constant on each cycle of σ2. Thus
(9) n! Trρλ(˜π)
dim Vλ
=
∑
σ1,σ2∈Sn,
σ1σ2=π
(−1)|σ1| ˜N λ(σ1, σ2)
and the proof in the case when l = n is ﬁnished.
For a permutation σ ∈ Sn we denote by supp σ ⊆ {1, . . . , n} the support
of a permutation (the set of non-ﬁxed points). We claim that a factorization
π = σ1σ2 has a non-zero contribution to (9) only if supp σ1, supp σ2 ⊆
supp π. Indeed, if m ∈ supp σ1 \ supp π = supp σ2 \ supp π then for any
bijection f at least one of the following conditions hold true: r(f (m)) ⁄=
r(f (σ2(m))) (in this case r ◦ f is not constant on the cycles of σ2) or
c(f (m)) ⁄= c(f (σ2(m))) (in this case c(f (σ1(σ2(m)))) ⁄= c(f (σ2(m)))
hence c ◦ f is not constant on the cycles of σ1).
ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS 7
It follows that if π ∈ Sl then we may restrict the sum in (9) to factoriza-
tions π = σ1σ2, where σ1, σ2 ∈ Sl. It remains to notice that
˜N λ
Sn(σ1, σ2) = ( n − l)! ˜N λ
Sl(σ1, σ2),
where the quantity on the left-hand side regards σ1, σ2 as elements of Sn
while on the quantity on the right-hand side regards them as e lements of
Sl and that the analogous relation holds between Σ λ(π) for π ∈ Sn and
π ∈ Sl. □
