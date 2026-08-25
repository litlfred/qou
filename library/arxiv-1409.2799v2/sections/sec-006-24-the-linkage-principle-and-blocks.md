---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY"
section_id: sec-006-24-the-linkage-principle-and-blocks
section_title: "The linkage principle and blocks"
section_number: 2.4
pages: 10-14
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on"
---
A0 = {k ∈ Z | −1 < k < l − 1}, ¯A0 = {k ∈ Z | −1 ≤ k ≤ l − 1}.
We call A0 the fundamental alcove. Any other alcove in Z≥−1 is clearly of the form A0 + il for
some i ∈ Z≥0. Moreover, we call −1, l − 1 ∈ ¯A0 − A0 walls of A0.
10
The afﬁne Weyl groupis Wl = ⟨sr, tr | r ∈ Z⟩ where sr and tr act on Z via
sr.k = −k − 2 + (4r + 2)l, t r.k = −k − 2 + 4rl, k ∈ Z
Note that Wl is isomorphic to the inﬁnite dihedral group D∞: we have Wl ∼= Z/2Z ⋉ lZ ∼
= D∞
(with Z/2Z being the Weyl group ofsl2) and we denote the two generators of D∞ by s and t (with
the evident association). They act “alcove-wise” as indicated in (6).
We denote by Wl.x the orbits in Z≥−1 under the action of the afﬁne Weyl group acting on
x ∈ Z≥−1. For l = 3 this can be visualized as
(6)
−1 0 1 2 3 4 5 6 7 8 9
s-wall s-wall
t-wall
r = 0 r = 1
r = 1
dead-end
with red (or top) action by s and green (or bottom) action by t.
We say i ∈ Z≥0 is linked to i′ ∈ Z≥0 if there exists w ∈ Wl such that w.i = i′. We, by
convention, set all Uq-modules indexed by negative numbers to be zero.
The following is known as the sl2-linkage principle. The more general (and highly non-trivial)
statement can be found in [2, Corollaries 4.4 and 4.6].
Theorem 2.23. (The linkage principle) All composition factors of Tq(i) have maximal weights
i′ linked to i. Moreover, Tq(i) is a simple Uq-module if i ∈ Wl.( ¯A0 − A0).
In addition, if i is linked to an element of A0, then Tq(i) is a simple Uq-module iff i ∈ A 0. □
Proof. Use Propositions 2.7 and 2.20 and Corollary 2.8. ■
Notation 2.24. We always use λ for elements in the fundamental alcove A0 and µ for elements on
the walls of the fundamental alcove ¯A0 − A0. Moreover, set
Ai = {i′ | il − 1 < i ′ < (i + 1)l − 1} = A0 + il, ¯Ai = {i′ | il − 1 ≤ i′ ≤ (i + 1)l − 1} = ¯A0 + il,
for each i ∈ Z≥0. Suppose λ ∈ A 0 and µ ∈ ¯A0 − A0. We write λi and µi for the unique elements
in Ai ∩ Wl.λ and ¯Ai ∩ Wl.µ. Note that, if µ = µ0 = −1, then µ1 = µ2, µ3 = µ4 and so forth,
while for µ = µ0 = l − 1 we have µ0 = µ1, µ2 = µ3 etc. See also (6). ▲
We deﬁne the tilting generator Tq(∞ ) and its cut-off’s Tq(≤ m) that will play a crucial role in
Section 3. By abuse of notation, we denote them in the same way for all λ and µ and hope that it
is clear from the context which ones we consider.
Deﬁnition 2.25. (The tilting generator) Let m ∈ Z≥0 ∪ {∞}. We call the Uq-modules given by
Tq(∞ ) =
∞⨁
i=0
Tq(λi) and Tq(≤ m) =
m⨁
i=0
Tq(λi)
the tilting generator and its m-th cut-off, respectively. Likewise for µ’s instead ofλ’s. ▲
Denote by Tλ for λ ∈ A 0 the λ block of T: all indecomposable summands of objects of Tλ
should be of the form Tq(i) for i ∈ Wl.λ. Note that blocks are in general not indecomposable as
categories. We, using a similar notation on walls, note the following.
11
Lemma 2.26. We have
T =
⨁
λ∈A0
Tλ ⊕ T−1 ⊕ Tl−1
with semisimple categories T−1 and Tl−1 equivalent to the corresponding Uv-module categories.
We have for all λ ∈ A 0 (similar for T−1 and Tl−1):
(a) The categories Tλ are additive, closed under ﬁnite direct sums and under duals.
(b) The categories Tλ are full Krull-Schmidt subcategories of T. Moreover, every indecom-
posable tilting in Tλ is of the form Tq(i) for some i ∈ Z≥0 and i ∈ Wl.λ. □
Proof. This is now only a combination of Theorem 2.23 and Lemma 2.18.Note that T−1 and Tl−1
are equivalent to categories of Uv-modules by Proposition 2.20 part (a). ■
Notation 2.27. If it is clear from the context which λ we consider, then we, by abuse of notation,
write Tq(λi) = Tq(i) for short. Similarly for simple and (dual) Weyl modules, and on walls. ▲
Example 2.28. Take l = 3 again. Then we only have to consider λ = 0, 1 and µ = −1, 2.
The indecomposable tiltings in T0 are Tq(i) for i = 0, 4, 6, . . . as a look at (6) indicates. For T1
they are Tq(i) for i = 1, 3, 7, . . .. The two blocks T−1 and T2 are semisimple and consist of direct
sums of Lq(i) ∼= Tq(i) for i = 5, 11, . . . and for i = 2, 8, . . . respectively. ▲
Remark 2.29. As in the usual case for an indeterminate v, we have a triangular decomposition
Uq = U−
q U0
qU+
q , see for example [5, Section 1]. There is a character χi : U0
q → Q(q) for any
i ∈ Z≥0 (how the character is determined by i can be found in [5, Lemma 1.1]). We note that
the Weyl module ∆ q(i) has the following universal property: for any Uq-module M there is an
isomorphism of vector spaces
HomUq (∆ q(i), M) ∼= {m ∈ Mi | E(j)m = 0 for all j ∈ Z≥0},
where Mi = {m ∈ M | um = χi(u)m, u ∈ U0
q} is the i weight space of M. This together with
Deﬁnition 2.5, Proposition 2.7 and Corollary 2.8 imply that
HomUq (∆ q(i), Lq(j)) ∼
= HomUq (∆ q(i), ∇q(j)) ∼= δijQ(q)
for all i, j ∈ Z≥0. In particular,
(7) HomUq(Lq(i), Lq(j)) ∼= δijQ(q),
i.e. Schur’s Lemma holds in our set-up (although Q(q) is not algebraically closed). Note that this
is true for general quantum groups over arbitrary ﬁelds, see [5, Corollary 7.4]. In addition5, we get
HomUq (∇q(i), ∆ q(i)) ∼= Q(q).
for all i ∈ Z≥0 (by using Proposition 2.7 and Corollary 2.8). ▲
We call the following maps up uλ
i , down dλ
i and loop ελ
i (or simply ui, di and εi) respectively.
Proposition 2.30. There exist up to scalars unique Uq-intertwiners uλ
i , dλ
i with
uλ
i : Tq(λi) → Tq(λi+1), i = 0, 1, . . . , d λ
i : Tq(λi) → Tq(λi−1), i = 1, 2, . . . ,
uλ
i ◦ uλ
i−1 = 0 = dλ
i ◦ dλ
i+1, i = 1, 2, . . . , d λ
i+1 ◦ uλ
i = ελ
i = uλ
i−1 ◦ dλ
i , i = 1, 2, . . .
ελ
i ◦ ελ
i = 0, i = 1, 2, . . . , d λ
1 ◦ uλ
0 = 0,
for λ ∈ A 0. The equation on the bottom right is called the dead-end relation. □
5We point out that this fails in general. An explicit counterexample can be found for example in [4, Section 5].
12
Proof. First let us assume that we are not in case of the dead-end relation (in fact, we leave it to the
reader to verify this special case), that is, the indicesi are at least 1. We want to use Proposition 2.7
and Corollary 2.8. Moreover, we note that the Uq-morphisms below will only be unique up to
scalars and their precise form does not matter. We only assume that they are non-zero. In fact, by
abuse of notation, we always use the same symbols, but the maps are of course different in general.
We consider
Lq(λi) /d31 /d127 /d47/d47 ∇q(λi)
a /d47/d47 /d47/d47 Lq(λi−1) /c61/c60/c66/c67
/c70
b
/c16/c23/c17⑧⑧⑧⑧⑧
/d47/d47 Lq(λi−1)/d31 /d127 c /d47/d47 ∆ q(λi)
d /d47/d47 /d47/d47 Lq(λi) /c61/c60/c66/c67
/c70
e
/c16/c23/c17⑧⑧⑧⑧⑧
/d47/d47 Lq(λi)/d31 /d127 f /d47/d47 ∇q(λi) /d47/d47 /d47/d47 Lq(λi−1).
Hence, we see that HomUq(∇q(λi), ∆ q(λi)) is one dimensional: as noted in Remark 2.29, the
hom-spaces between Weyl and dual Weyl modules are at most 1-dimensional. The composite cba
ensures that the dimension is exactly 1 since it spans the hom-space.
Likewise for HomUq(∆ q(λi), ∇q(λi)) by using f ed. Note that the composite f edcba = 0 due
to the fact that the middle row is exact. The same holds when th e roles of ∆ q(λi) and ∇q(λi)
are exchanged. Moreover, note that the morphism from ∇q(λi) to ∆ q(λi) uses only Lq(λi−1)
while the other way around uses only Lq(λi). Thus, up to scalars, morphisms from ∇q(λi) to
∆ q(λi) are the “same” as morphisms from ∆ q(λi−1) to ∇q(λi−1). We can now construct, by using
Proposition 2.20, up uλ
i and down dλ
i as a composition of the following maps.
∆ q(λi) /d31 /d127 /d47/d47
Tq(λi)
a /d47/d47 /d47/d47 ∆ q(λi−1) /c61/c60/c66/c67
/c70
b
/c16/c23/c17⑧⑧⑧⑧⑧
/d47/d47 ∆ q(λi−1)/d31 /d127 c /d47/d47 Tq(λi−1)
d /d47/d47 /d47/d47 ∆ q(λi−2) /c61/c60/c66/c67
/c70
e
/c16/c23/c17⑧⑧⑧⑧⑧
/d47/d47 ∆ q(λi−2)/d31 /d127 f /d47/d47 Tq(λi−2) /d47/d47 /d47/d47 ∆ q(λi−3).
We deﬁne dλ
i to be the composite cba. Similar for uλ
i , but using the right-hand side of part (b) of
Proposition 2.20. By the same reasoning as above we see that they are unique up to scalars.
We have to check the relations between the various up uλ
i and down dλ
i maps now. To see
that uλ
i ◦ uλ
i−1 = 0 and dλ
i ◦ dλ
i+1 = 0 we can simply use the second diagram above and its dual
counterpart and the fact that the rows are exact. Now consider
Tq(λi−1)/d79/d79
id
/d15/d15
∆ q(λi−1)/d63 /d95/d111/d111
Lq(λi−1)→Lq(λi−1)
/d15/d15
Tq(λi)/d79/d79
id
/d15/d15
/d47/d47 /d47/d47/d111/d111/d111/d111 ∇q(λi)/d31 /d127 /d47/d47
Lq(λi−1)→Lq(λi−1)
/d15/d15
Tq(λi+1)/d79/d79
id
/d15/d15
Tq(λi−1) /d47/d47 /d47/d47 ∇q(λi−1)/d31 /d127 /d47/d47 Tq(λi) ∆ q(λi)/d63 /d95/d111/d111 Tq(λi+1)/d111/d111/d111/d111
Combining everything, we see that (up to scalars) dλ
i+1 ◦ uλ
i = ελ
i = uλ
i−1 ◦ dλ
i ⁄= 0. Moreover, by
the reasoning above, the ελ
i is an up to scalars unique non-zero Uq-morphism Tq(λi) to Tq(λi) that
squares to zero. ■
13
Corollary 2.31. Let i, i′ ∈ Z≥0. Then we have the following.
(a) Outside of walls:
HomUq (Tq(λi), Tq(λi′)) ∼
=





Q(q)[ε], if |i − i′| = 0 and i = i′ ⁄= 0,
Q(q), if |i − i′| = 1 or i = i′ = 0,
0, if |i − i′| > 1,
where Q(q)[ε] ∼= Q(q)[X]/(X 2) denotes the Q(q)-algebra of dual numbers.
(b) On walls:
HomUq(Tq(µi), Tq(µi′)) ∼=
{
Q(q), if |i − i′| = 0,
0, if |i − i′| > 0,
where Q(q) is the trivial Uq-module. □
Proof. Because of Proposition 2.30, we only need to verify (b). But since the Tq(µi) are simple on
walls (by Proposition 2.20), part (b) follows from “Schur’sLemma” (7). ■
