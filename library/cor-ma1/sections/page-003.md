---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-003
section_title: "Page 3"
section_number: null
pages: 3-3
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
2
SYLVIE CORTEEL AND OLIVIER MALLET
Notice that Lovejoy’s result can be seen as an overpartition analogue of Gordon’s theorem, in the sense
that the conditions on the Bk(n) reduce to the conditions on the Bk,k(n) if the overpartition has no overlined
parts and is indeed a partition.
Two questions naturally arise. First, given the similarities between Theorems 1.1 and 1.3, is there some
general framework which contains these two theorems? Second, is there an analogue for overpartitions of
Andrews’ result, Theorem 1.2? In this paper, both of these questions shall be answered in the aﬃrma-
tive.
Moreover, our results contain many other partition and overpartition identities, such as Andrews’
generalization of the G¨ollnitz-Gordon identities [6].
It is well understood combinatorially that Bk,i(n) = Ck,i(n) = Dk,i(n) and this result was established
by some beautiful work of Burge [16, 17] using some recursive arguments. This work was reinterpreted
by Andrews and Bressoud [8] who showed that Burge’s argument could be rephrased in terms of lattice
paths with two kinds of steps and that Gordon’s theorem can be established thanks to these combinatorial
arguments and the Jacobi Triple product identity [25]. Finally Bressoud [14] reinterpreted these in terms of
diﬀerent lattice paths with three kinds of steps and gave some direct bijections between the objects counted
by Bk,i(n), Ck,i(n), Dk,i(n) and the lattice paths.
With our main theorem we extend the main results of the above works [8, 14, 16, 17] to overpartitions.
In particular, we generalize all of the combinatorial deﬁnitions to overpartitions and successfully adapt the
methods of proof. This is the result that provides a unifying framework for Theorems 1.1, 1.2, and 1.3.
Theorem 1.4.
• Let Bk,i(n, j) be the number of overpartitions of n of the form (λ1, λ2, . . . , λs) with j overlined parts,
where λℓ−λℓ+k−1 ≥1 if λℓ+k−1 is overlined and λℓ−λℓ+k−1 ≥2 otherwise and at most i −1 parts
are equal to 1.
• Let Ck,i(n, j) be the number of overpartitions of n with j non-overlined parts in the bottom row of
their Frobenius representation and whose successive ranks lie in [−i + 2, 2k −i −1].
• Let Dk,i(n, j) be the number of overpartitions of n with j overlined parts and i −1 successive Dur-
fee squares followed by k −i successive Durfee rectangles, the ﬁrst one being a generalized Durfee
square/rectangle.
• Let Ek,i(n, j) be the number of paths that use four kinds of unitary steps with special (k, i)-conditions,
major index n, and j South steps.
Then Bk,i(n, j) = Ck,i(n, j) = Dk,i(n, j) = Ek,i(n, j).
All of the combinatorial notions in this theorem will be deﬁned in detail in Section 2. The addition of
the generalized lattice paths counted by Ek,i(n, j) is the key step which allows us to prove Theorem 1.4
combinatorially. In terms of generating functions, we have:
Theorem 1.5. The generating function Ek,i(a, q) = P
n,j Ek,i(n, j)qnaj is:
(1.1)
Ek,i(a, q) = (−aq)∞
(q)∞
∞
X
n=−∞
(−1)nanqkn2+(k−i+1)n (−1/a)n
(−aq)n
.
Here we have used the classical q-series notations:
(a)∞
=
(a; q)∞=
∞
Y
i=0
(1 −aqi),
(a)n
=
(a)∞/(aqn)∞,
(a1, . . . , ak; q)∞
=
(a1; q)∞. . . (ak; q)∞.
In several cases, we can use the Jacobi Triple Product identity [25]:
(1.2)
(−1/z, −zq, q; q)∞=
∞
X
n=−∞
znq(n+1
2 )
to show that this generating function has a very nice form. For example,
