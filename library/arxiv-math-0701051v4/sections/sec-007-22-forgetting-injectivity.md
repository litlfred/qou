---
doc_id: arxiv-math-0701051v4
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA"
section_id: sec-007-22-forgetting-injectivity
section_title: "Forgetting injectivity"
section_number: 2.2
pages: 7-8
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA — We prove an upper bound for characters of the symmetric groups."
---
ﬁne ˆN λ(σ1, σ2) as the number of all functions f : {1, . . . , l} → λ (with
values in the set of boxes ofλ) with a property that r ◦ f is constant on each
cycle of σ2 and c ◦ f is constant on each cycle of σ1.
Lemma 6. For any Young diagramλ and a permutation π ∈ Sl
(10)
∑
σ1,σ2∈Sl
σ1σ2=π,
(−1)|σ1| ˜N λ(σ1, σ2) =
∑
σ1,σ2∈Sl
σ1σ2=π,
(−1)|σ1| ˆN λ(σ1, σ2).
Proof. For a given function f : {1, . . . , l} → λ we will show that it has the
same contribution to the left-hand side and to the right-han d side. Clearly,
it is enough to consider the case when f is not a one-to-one function. It
follows that there exists a transposition µ ∈ Sl with a property that f is
constant on the orbits of µ. Function f contributes to the right-hand side
with multiplicity
(11)
∑
σ1,σ2∈Sl
σ1σ2=π
(−1)|σ1|,
where the sum runs over pairs (σ1, σ2) with a property that σ1σ2 = π and
c ◦ f is constant on each cycle of σ1 and r ◦ f is constant on each cycle of
σ2. Map (σ1, σ2) ↦→(σ′
1, σ′
2) with σ′
1 = σ1µ, σ′
2 = µσ2 is an involution
of the pairs (σ1, σ2) which contribute to (11); the only less trivial condition
which should be veriﬁed is that c ◦ f is constant on each cycle of σ′
1 but this
is equivalent to c ◦ f being constant on each cycle of σ′
1
−1 = µσ−1
1 .
Since (−1)|σ1| = ( −1) · (−1)|σ′
1| therefore the contributions of the pairs
(σ1, σ2) and (σ′
1, σ′
2) to (11) cancel. In this way we proved that (11) is equal
to zero which ﬁnishes the proof. □
Proof of Theorem 2. Proposition 5 and Lemma 6 show that
Σ λ(π) =
∑
σ1,σ2∈Sl
σ1σ2=π
(−1)|σ1| ˆN λ(σ1, σ2).
8 V ALENTIN FÉRAY AND PIOTR ´SNIADY
Now it is enough to notice that N λ(σ1, σ2) = ˆN λ(σ1, σ2); the desired bi-
jection is deﬁned as follows: if m ∈ { 1, . . . , l} fulﬁlls m ∈ c1 ∩ c2 for
ci ∈ C(σi) we set f (m) = ( h(c1), h(c2)). □
2.3. Generalization to Young diagrams onR2
+. We may identify a Young
diagram with a subset of R2 given by a graphical representation of λ (ac-
cording to the French notation). For example, for a partition λ = (λ1, . . . , λk)
it is the set
(12)
⋃
1≤i≤k
[0, λi] × [i − 1, i].
In this way we may consider colorings h of the cycles of permutations σ1
and σ2 which take real values instead of natural numbers. If we ﬁx so me
numbering of the cycles in C = C(σ1) ⊔ C(σ2) then any such coloring
h : C → R+ can be identiﬁed with an element of R|C|
+ .
We deﬁne
(13) N λ(σ1, σ2) = vol {h ∈ R|C|
+ : h compatible with λ}.
Notice that in the case when λ ⊂ R2 is as prescribed by (12), the set of
functions h ∈ R|C|
+ compatible with λ is a polyhedron hence there is no
difﬁculty in deﬁning its volume; furthermore deﬁnitions (7 ) and (13) give
the same value.
The advantage of the deﬁnition (13) is that it allows to deﬁne characters
for any bounded set λ ∈ R2
+, in particular for generalized Young diagrams
(see [Ker93]).
It is very natural therefore to ask if Theorem 2 holds true als o for skew
Young diagrams. Unfortunately, this is not the case as it canbe seen for the
skew Young diagramλ = (3, 2) \ (1).
3. C HARACTERS OF SYMMETRIC GROUPS , RANDOM MATRICES AND
FREE PROBABILITY
