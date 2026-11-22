---
doc_id: 0309214v3
doc_title: "The colored Jones function is q –holonomic"
section_id: sec-039-742-uqsl2-is-q--holonomic
section_title: "Uq(sl2) is q--holonomic"
section_number: 7.4.2
pages: 33-35
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
toc_source: outline
doc_brief: "The colored Jones function is q –holonomic — A function of several variables is called holonomic if, roughly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many linear"
---
Lemma 7.10 Theorem 7 holds true for g = sl2.
Geometry & Topology, Volume 9 (2005)
1286
Stavros Garoufalidis and Thang T Q Lˆe
Proof The PBW basis for U is F nKjEm, with m, n ∈N and j ∈Z. First of
all we know that
Em
α F n
α =
∞
X
i=0
 m
i

vα
 n
i

vα
F n−i
α
b(Kα; 2i −n −m, i) Em−i
α
,
where
b(Kα; a, i) :=
iY
j=1
Kαva−j+1
α
−K−1
α v−a+j−1
α
vα −v−1
α
.
Here for any root γ, one deﬁnes vγ = v(γ,γ)/2, and
 m
i

vα
is the usual
quantum binomial coeﬃcient calculated with v replaced by vα.
Hence
(F mKkEn)(F m′Kk′Em′) =
∞
X
i=0
F m+m′−i a(m, k, n, m′, k′, n′, i) En+n′−i,
where
a(m, k, n, m′, k′, n′, i)
= v2k(i−m′)+2k′(i−n)
 n
i
 m′
i

[i]! b(K; 2i −n −m′, i) Kk+k′.
The value of the function a is in Z[v±1][K±1]. Consider the coeﬃcient of Kr
in a; one gets a function of m, n, k, m′, n′, k′, i, r with values in Z[v±1] which is
clearly q–holonomic with respect to all variables. The lemma follows.
7.4.3
Ek
α, F k
α : U →U are q–holonomic in k
Proposition 7.11 For a ﬁxed fundamental root α ∈{α1, . . . , αℓ}, the opera-
tors Ek
α, F k
α : U →U of left multiplication are q–holonomic with respect to k
and all the coordinates of the matrix entry. Similarly, the right multiplication
by Ek
α, F k
α are q–holonomic with respect to k and all the coordinates of the
matrix entry.
Proof (a) Left multiplication by F k
α and right multiplication by Ek
α.
Choose w as in the proof of Lemma 7.9. Then ft = Fα and et = Eα, and
an element of the PBW basis has the form f nt
t xKβyemt
t
. It’s clear that left
multiplication by Fα and right multiplication by Eα are q–holonomic.
(b) Left multiplication by Ek
α.
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q–holonomic
1287
Choose a reduced word w = si1 . . . sit representing the longest element ω0 that
begins with α: αi1 = α. We have the corresponding PBW basis fi, ei, i =
1, . . . , t with f1 = Fα and e1 = Eα. Thus a typical element of the PBW basis
has the form
xF n1
α KβEm1
α y,
(7)
where x = f nt
t
. . . f n2
2 , y = em2
2
. . . emt
t
. By [17, 8.26.6], since x ∈U−[t, 2], one
has r′
α(x) = 0. Using formula [17, 6.17.1], one can easily prove by induction
that
(Eα)kx =
∞
X
i=0
vi−ik
 k
i

vα
Ki
α
(vα −v−1
α )i (rα)i(x)Ek−i
α
.
Using this formula one can move the Eα past x in the expression (7), (there
appear rα and Kα), then one moves Eα past Fα using the sl2 case. The last
step is moving past Kβ is easy, since
EαKβ = v−(β,α)KβEα.
Using Lemmas 7.9 and 7.10, we see that each “moving step” is q–holonomic.
Hence we get the result for the left multiplication by Ek
α.
(c) Right multiplication by F k
α .
The proof is similar. We use the same basis (7) as in the case b). For y, by
Lemma 8.26 of [17], one has rα(y) = 0. Hence using induction based on the
formula (6.17.2) of [17] one can show that
yF n
α =
∞
X
i=0
vi(n−i)
α
(v−1
α −vα)i
 n
i

vα
F n−i
α
K−i
α (r′
α)i(y).
Using this formula, and the results for r′
α (Lemma 7.9) and sl2 (Lemma 7.10)
we can move Fα to the right.
7.4.4
