---
doc_id: cor-ma1
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-019-24-syl-vie-corteel-and-olivier-mallet
section_title: "SYL VIE CORTEEL AND OLIVIER MALLET"
section_number: 24
pages: 25-25
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
• The number of paths that use four kinds of unitary steps with s pecial (k, i)-conditions where n is
twice the sum of the x-coordinates of the peaks minus the number of South steps.
Remark. The ﬁrst two parts of the theorem are the Andrews’ generaliza tion of the Gordon-G¨ ollnitz iden-
tities. The interpretation in terms of successive ranks and Durfee dissection is new to our knowledge.
7.3. Superpartitions. We give new partition theorems related to Gordon’s theorems for overpartitions [28]
which are the combinatorial interpretation of the case i = k of equation (1.5) and i = 1 of equation (1.6). We
now interpret combinatorially equations (1.5) and (1.6). S uperpartitions [21] are overpartitions where the ﬁrst
occurrence of a part can be overlined and the part 0 can appear. Let Bk,i(n) be the number of overpartitions
of n of the form ( λ1, λ2, . . . , λs), where λℓ− λℓ+k−1≥ 1 if λℓ+k−1 is overlined and λℓ− λℓ+k−1≥ 2 otherwise
and at most i− 1 parts are equal to 1.
Theorem 7.2. For 1≤ i≤ k− 1, the number of overpartitions counted by Bk,i(n) plus the number of
overpartitions counted by Bk,i+1(n) is equal to the number of superpartitions where the non-over lined parts
are not congruent to 0,±i modulo 2k.
Proof. Theorem 1.4 tells us that Bk,i(n) + Bk,i+1(n) is the coeﬃcient of qn ofE k,i(1, q) +E k,i+1(1, q).
Thanks to equation (1.5), we know that E k,i(1, q) +E k,i+1(1, q) =
= (−q)∞
(q)∞


2(k−i)∑
j=0
(−1)j(qi+j, q2k−i−j , q2k; q2k)∞ +
2(k−i−1)∑
j=0
(−1)j(qi+1+j, q2k−i−1−j , q2k; q2k)∞


= (−q)∞
(q)∞


2(k−i)∑
j=0
(−1)j(qi+j, q2k−i−j , q2k; q2k)∞ −
2(k−i)−1∑
j=1
(−1)j(qi+j, q2k−i−j , q2k; q2k)∞


= (−1)∞
(q)∞
(qi, q2k−i, q2k; q2k)∞ .
The coeﬃcient of qn in that last equation is the number of superpartitions where the non-overlined parts
are not congruent to 0 ,±i modulo 2 k. □
Theorem 7.3. For 2≤ i≤ k− 1, the number of superpartitions of n of the form (λ1, λ2, . . . , λs), where
λℓ− λℓ+k−1≥ 1 if λj is overlined and λℓ− λℓ+k−1≥ 2 otherwise and where the number of non-overlined ones
plus the number of 0 is at most i− 1 is equal to the number of overpartitions of n where the non-overlined
parts are not congruent to 0,±i modulo 2k plus the number of overpartitions of n where the non-overlined
parts are not congruent to 0,±(i− 1) modulo 2k.
Proof. We interpret combinatorially the coeﬃcient of qn in equation (1.6). This is the number of over-
partitions of n where the non-overlined parts are not congruent to 0 ,±i modulo 2 k plus the number of
overpartitions of n where the non-overlined parts are not congruent to 0 ,±(i− 1) modulo 2 k. Note that this
is the interpretation of E k,i(1/q, q). This implies that all the overlined parts in Theorem 1.4 ar e decreased
by one and the result follows. □
