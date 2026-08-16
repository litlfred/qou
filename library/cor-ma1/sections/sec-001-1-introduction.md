---
doc_id: cor-ma1
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
In 1961 Gordon established his celebrated combinatorial ge neralization of the Rogers-Ramanujan identi-
ties:
Theorem 1.1. [26] Let Bk,i(n) denote the number of partitions of n of the form (λ1, λ2, . . . , λs), where
λℓ− λℓ+k−1≥ 2 and at most i− 1 of the parts are equal to 1. Let Ak,i(n) denote the number of partitions
of n into parts not congruent to 0,±i modulo 2k + 1. Then Ak,i(n) = Bk,i(n).
Over the years, a number of other combinatorial functions ha ve been found to be equal to the Ak,i(n) in
Gordon’s theorem. Most notable, perhaps, are two results of Andrews that employ Atkin’s successive ranks
[11] and Andrews’ own new idea of Durfee dissection :
Theorem 1.2. [5] Let Ck,i(n) be the number of partitions of n whose successive ranks lie in the interval
[−i + 2, 2k− i− 1] and let Dk,i(n) be the number of partitions of n with i− 1 successive Durfee squares
followed by k− i successive Durfee rectangles. Then
Ak,i(n) = Bk,i(n) = Ck,i(n) = Dk,i(n).
An overpartition is a partition where the ﬁnal occurrence of a part can be overlined [18]. For example,
there exist 8 overpartitions of 3
(3), (
3), (2, 1), (2, 1), (2, 1), (2, 1), (1, 1, 1), (1, 1, 1).
In recent years overpartitions have been heavily studied, s ometimes under diﬀerent names and guises. They
have been called joint partitions [12], or dotted partition s [13], and they are closely related to 2-modular
diagrams [32], jagged partitions [23, 24] and superpartiti ons [21]. Overpartitions arise in the study of the
combinatorics of basic hypergeometric series identities [ 19, 24, 28, 29, 38], congruences properties of modular
forms [23, 33], supersymmetric functions [21], Lie algebra s [27] and mathematical physics [21, 23, 24].
In 2003 Lovejoy [28] proved an overpartition identity where in one of the functions closely resembles the
Bk,i(n) in Gordon’s theorem:
Theorem 1.3 (“Gordon’s theorem for overpartitions”) . [28] Let Bk(n) denote the number of overpartitions
of n of the form (λ1, λ2, . . . , λs), where λℓ− λℓ+k−1≥ 1 if λℓ+k−1 is overlined and λℓ− λℓ+k−1≥ 2 otherwise.
Let Ak(n) denote the number of overpartitions of n into parts not divisible by k. Then Ak(n) = Bk(n).
2000 Mathematics Subject Classiﬁcation. Primary 11P81; Secondary 05A17.
Key words and phrases. Partitions, overpartitions, Rogers-Ramanujan identitie s, lattice paths.
The authors are partially supported by the ACI Jeunes Cherch eurs “Partitions d’entiers ` a la fronti` ere de la combinato ire,
des q-s´ eries et de la th´ eorie des nombres.”
1
2 SYL VIE CORTEEL AND OLIVIER MALLET
Notice that Lovejoy’s result can be seen as an overpartition analogue of Gordon’s theorem, in the sense
that the conditions on the Bk(n) reduce to the conditions on the Bk,k(n) if the overpartition has no overlined
parts and is indeed a partition.
Two questions naturally arise. First, given the similariti es between Theorems 1.1 and 1.3, is there some
general framework which contains these two theorems? Secon d, is there an analogue for overpartitions of
Andrews’ result, Theorem 1.2? In this paper, both of these qu estions shall be answered in the aﬃrma-
tive. Moreover, our results contain many other partition an d overpartition identities, such as Andrews’
generalization of the G¨ ollnitz-Gordon identities [6].
It is well understood combinatorially that Bk,i(n) = Ck,i(n) = Dk,i(n) and this result was established
by some beautiful work of Burge [16, 17] using some recursive arguments. This work was reinterpreted
by Andrews and Bressoud [8] who showed that Burge’s argument could be rephrased in terms of lattice
paths with two kinds of steps and that Gordon’s theorem can be established thanks to these combinatorial
arguments and the Jacobi Triple product identity [25]. Fina lly Bressoud [14] reinterpreted these in terms of
diﬀerent lattice paths with three kinds of steps and gave som e direct bijections between the objects counted
by Bk,i(n), Ck,i(n), Dk,i(n) and the lattice paths.
With our main theorem we extend the main results of the above w orks [8, 14, 16, 17] to overpartitions.
In particular, we generalize all of the combinatorial deﬁni tions to overpartitions and successfully adapt the
methods of proof. This is the result that provides a unifying framework for Theorems 1.1, 1.2, and 1.3.
Theorem 1.4.
• Let Bk,i(n, j) be the number of overpartitions of n of the form (λ1, λ2, . . . , λs) with j overlined parts,
where λℓ− λℓ+k−1≥ 1 if λℓ+k−1 is overlined and λℓ− λℓ+k−1≥ 2 otherwise and at most i− 1 parts
are equal to 1.
• Let Ck,i(n, j) be the number of overpartitions of n with j non-overlined parts in the bottom row of
their Frobenius representation and whose successive ranks lie in [−i + 2, 2k− i− 1].
• Let Dk,i(n, j) be the number of overpartitions of n with j overlined parts and i− 1 successive Dur-
fee squares followed by k− i successive Durfee rectangles, the ﬁrst one being a generali zed Durfee
square/rectangle.
• Let Ek,i(n, j) be the number of paths that use four kinds of unitary steps wit h special (k, i)-conditions,
major index n, and j South steps.
Then Bk,i(n, j) = Ck,i(n, j) = Dk,i(n, j) = Ek,i(n, j).
All of the combinatorial notions in this theorem will be deﬁn ed in detail in Section 2. The addition of
the generalized lattice paths counted by Ek,i(n, j) is the key step which allows us to prove Theorem 1.4
combinatorially. In terms of generating functions, we have :
Theorem 1.5. The generating function E k,i(a, q) =∑
n,j Ek,i(n, j)qnaj is:
(1.1) E k,i(a, q) = (−aq)∞
(q)∞
∞∑
n=−∞
(−1)nanqkn2+(k−i+1)n (−1/a)n
(−aq)n
.
Here we have used the classical q-series notations:
(a)∞ = ( a; q)∞ =
∞∏
i=0
(1− aqi),
(a)n = ( a)∞/(aqn)∞,
(a1, . . . , ak; q)∞ = ( a1; q)∞ . . . (ak; q)∞.
In several cases, we can use the Jacobi Triple Product identi ty [25]:
(1.2) ( −1/z,−zq, q; q)∞ =
∞∑
n=−∞
znq(n+1
2 )
to show that this generating function has a very nice form. Fo r example,
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDEN TITIES 3
Corollary 1.6.
E k,i(0, q) = (qi, q2k+1−i, q2k+1; q2k+1)∞
(q)∞
(1.3)
E k,i(1/q, q2) = (q2; q4)∞(q2i−1, q4k+1−2i, q4k; q4k)∞
(q)∞
(1.4)
E k,i(1, q) = (−q)∞
(q)∞
2(k−i)∑
j=0
(−1)j(qi+j , q2k−i−j , q2k; q2k)∞(1.5)
E k,i(1/q, q) = (−q)∞
(q)∞
((qi, q2k−i, q2k; q2k)∞
+(qi−1, q2k+1−i, q2k; q2k)∞)(1.6)
Hence our result gives a general view of diﬀerent problems on partitions and overpartitions and shows
how they are related.
• Equation (1.3) corresponds to the Andrews-Gordon identiti es [5].
• Equation (1.4) corresponds to Andrews’s generalization of the Gordon-G¨ ollnitz identities [6, 8].
• Equation (1.5) with i = k and (1.6) with i = 1 correspond to the two Gordon’s theorems for
overpartitions of Lovejoy [28].
Therefore our extension of the work on the Andrews-Gordon id entities [8, 14, 16, 17] to the case of overparti-
tions includes these identities, but it also includes Andre ws’s generalization of the Gordon-G¨ ollnitz identities
and Gordon’s theorems for overpartitions. We prove this Cor ollary and deduce some new partition theorems
in Section 7.
In Section 2 we present all the necessary notions. In Section 3 we present the paths counted by Ek,i(n, j)
and compute the generating function. In Section 4 we present a direct bijection between the paths counted by
Ek,i(n, j) and the overpartitions counted by Ck,i(n, j). In Section 5 we present a recursive bijection between
the paths counted by Ek,i(n, j) and the overpartitions counted by Bk,i(n, j). We also give a generating
function proof. In Section 6, we present a combinatorial arg ument that shows that the paths counted by
Ek,i(n, j) and the overpartitions counted by Dk,i(n, j) are in bijection. All these bijections are reﬁnements
of Theorem 1.4. The number of peaks of the paths will correspo nd respectively to the number of columns of
the Frobenius representations, the length of the multiplic ity sequence and the size of the generalized Durfee
square. In Section 7 we prove Corollary 1.6 and interpret it c ombinatorially. We conclude in Section 8 with
further questions.
