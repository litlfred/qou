---
doc_id: cor-ma1
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-006-10-syl-vie-corteel-and-olivier-mallet
section_title: "SYL VIE CORTEEL AND OLIVIER MALLET"
section_number: 10
pages: 11-12
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
Proof. We only prove the case n≥ 0. The case n < 0 is identical as ( a)−n = (−1/a)nq(
n+1
2 )/(aq)n and
therefore
(−aq)n(−qn/a)N −nq(N +1
2 )−(n+1
2 )aN −n
(q)N +n(q)N −n
= (−aq)−n(−q−n/a)N +nq(N +1
2 )−(−n+1
2 )aN +n
(q)N +n(q)N −n
.
We present an analytical proof and a combinatorial one.
Analytical proof:
∞∑
N =n
(−aq)n(−qn/a)N −nq(
N +1
2 )−(
n+1
2 )aN −n
(q)N +n(q)N −n
=
∞∑
N =0
(−aq)n(−qn/a)N q(
N +n+1
2 )−(
n+1
2 )aN
(q)N (q)N +2n
= (−aq)n
(q)2n
∞∑
N =0
qN n+(N +1
2 )(−qn/a)N aN
(q)N (q2n+1)N
We now apply the q-Gauss summation (Corollary 2.4 of [3] with n → N , a → −qn/a, b → −∞and
c→ q2n+1)
= (−aq)n
(q)2n
(−aqn+1)∞
(q2n+1)∞
= (−aq)∞
(q)∞
Combinatorial proof: Let n be a ﬁxed non-negative integer and let N be the greatest integer such that
the sum of the number of overlined parts greater than n and of the number of non-overlined parts greater
than or equal to N + n is greater than or equal to N− n. By deﬁnition, N , if it exists, is unique. We
check that N = n satisﬁes the condition: the sum of the number of overlined pa rts > n and of the number
of non-overlined parts ≥ 2n is indeed ≥ 0. Therefore, N exists and it is unique. We call N the size of the
generalized n-Durfee square. Note that if n = 0, N is the size of the generalized Durfee square and this
bijection is the same as the one presented in the proof of Prop osition 2.2. For example, if n = 2 then the
overpartition (8, 8, ¯
6, 5, 5, 3, 3, ¯
3, ¯
1) gives N = 6.
We now show that the generating function for the overpartiti ons with generalized n-Durfee square N is:
(−aq)n(−qn/a)N −nq(
N +1
2 )−(
n+1
2 )aN −n
(q)N +n(q)N −n
.
The factor ( −aq)n corresponds to the overlined parts ≤ n and the factor 1
(q)N +n
corresponds to the
non-overlined parts≤ N + n.
The remaining factors correspond to an overpartition into N− n parts whose overlined parts are > n and
whose non-overlined parts are ≥ N + n. To prove this, let us show that there exists a bijection betw een
such overpartitions θ and triples ( ε, ζ, η) where ε is the overpartition ( N ,N− 1, . . . ,n + 1) which has N− n
parts (corresponding to the factor aN −nq(
N +1
2 )−(
n+1
2 )), ζ is a partition into distinct parts which lie between
n and N− 1 (corresponding to the factor ( −qn/a)N −n) and η is a partition into N− n non-negative parts
(corresponding to the factor 1
(q)N −n
). This bijection (similar to Algorithm Z [9]) is deﬁned as fo llows: ﬁrst
for all i we set θi = εi + ηi. Then for each part n + i in ζ, we add n + i to θi+1 and we remove the overlining
of that part. This implies that the non-overlined parts are ≥ N + n. Finally, we reorder the parts. It is easy
to see that this is a bijection as there only a unique ordering of the parts of θ which allows, if θi+1 is not
overlined, to take oﬀ n + i from it and overline it and get a partition into distinct over lined parts.
For example for N = 7 and n = 3, if ε = (¯
7, ¯
6, ¯
5, ¯
4), η = (3, 3, 1, 0) and ζ = (6, 3), then θ = (13, ¯
9, ¯
6, 10) =
(13, 10, ¯
9, ¯
6).
□
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDEN TITIES 11
Summing on N we get
∑
N ≥0
E k,i(N ) =
∑
N ≥0
aN q(
N +1
2 )(−1/a)N
N∑
n=−N
(−1)n qkn2+n(k−i)−(
n
2)
(q)N −n(q)N +n
=
∑
N ≥0
N∑
n=−N
aN q(
N +1
2 )(−1/a)N (−1)n qkn2+n(k−i)−(n
2)
(q)N −n(q)N +n
=
∞∑
n=−∞
∑
N ≥|n|
aN q(N +1
2 )(−1/a)N (−1)n qkn2+n(k−i)−(
n
2)
(q)N −n(q)N +n
=
∞∑
n=−∞
(−1)nanqkn2+(k−i+1)n (−1/a)n
(−aq)n
·
∑
N ≥|n|
(−aq)n( −qn
a )N −nq(N +1
2 )−(n+1
2 )aN −n
(q)N −n(q)N +n
=
∞∑
n=−∞
(−1)nanqkn2+(k−i+1)n (−1/a)n
(−aq)n
(−aq)∞
(q)∞
by Proposition 3.3
= (−aq)∞
(q)∞
∞∑
n=−∞
(−1)nanqkn2+(k−i+1)n (−1/a)n
(−aq)n
.
This is equation (1.1) of Theorem 1.5.
