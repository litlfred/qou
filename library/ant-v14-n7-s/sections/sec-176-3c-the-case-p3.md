---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory"
section_id: sec-176-3c-the-case-p3
section_title: "3C. The case p=3"
section_number: null
pages: 300-302
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
toc_source: outline
---
classiﬁcation of simple groups with cyclic Sylow 3-subgroups.
Proposition 3.6. Let S be a ﬁnite nonabelian simple group with order divisible by 3. Then S has a cyclic
Sylow 3-subgroup if and only if S is one of: the alternating group A5; the sporadic simple group J1;
PSL2(q) for 3∤q; or PSLϵ
3(q) for 3 | (q + ϵ).
Proof. The main result of [Shen and Zhou 2016] yields a classiﬁcation of simple groups S and primes p
such that S has an abelian Sylow p-subgroup. In particular, if p = 3, then such a simple group must be of
the form An with n < 9, one of a short list of sporadic simple groups, PSL2(q), PSLϵ
n(q) for 3 | (q + ϵ)
and n = 3, 4, 5, or PSp4(q) with 3∤q.
Galois action on the principal block and cyclic Sylow subgroups
1967
Using the atlas [Conway et al. 1985] and since A6 has a noncyclic Sylow 3-subgroup and can be
viewed as a subgroup of An for n ≥7, we see that the only simple alternating or sporadic groups with
cyclic Sylow 3-subgroups are A5 and the Janko group J1. The remaining possibilities are of the form
G/Z(G) for G a classical group SLϵ
n(q) with n < 6, or Sp4(q). Further, except in the cases of PSLϵ
3(q)
listed in the statement, |Z(G)| is relatively prime to 3, and hence S has a cyclic Sylow 3-subgroup if and
only if G does. Further, for the cases G = SLϵ
n(q) with n = 3, 4, 5 under consideration, we may view the
Sylow subgroup as a Sylow subgroup of ˜G = GLϵ
n(q), since [ ˜G : G] is not divisible by 3.
Now, using the description of the Sylow subgroups of classical groups in [Carter and Fong 1964;
Weir 1955], we see that the Sylow subgroups of GLϵ
4(q), GLϵ
5(q), and Sp4(q) are direct products of
Sylow subgroups of at least two lower-rank groups, and hence the Sylow 3-subgroup of G is not cyclic.
In the case PSLϵ
3(q) with 3 | (q + ϵ) or PSL2(q) with 3∤q, we may explicitly construct a cyclic Sylow
3-subgroup. Finally, if S = PSL2(q) with 3 | q, the Sylow 3-subgroup can be identiﬁed with the unipotent
radical of SL2(q), which is not cyclic unless q = 3, contradicting that S is simple.
□
Our goal in the remainder of this section is to prove the following, from which we obtain Theorem C
for p = 3 as a corollary.
Theorem 3.7. Let S be a nonabelian simple group with order divisible by 3.
(i) If S has a cyclic Sylow 3-subgroup, then there exist 1S̸ = χ1, χ2 ∈Irr3′(B0(S))σ1 such that χ1 extends
to Aut(S).
(ii) If S does not have a cyclic Sylow 3-subgroup and is not a group of Lie type deﬁned in characteristic 3,
then there exist nontrivial χ1, χ2, χ3 ∈Irr3′(B0(S))σ1 such that χ1 and χ2 extend to Aut(S). In this
case, if S is further not one of A6, A7, 2F4(2)′, PSLn(q) with n ≤4, or PSp4(22m+1), then there exist
nontrivial χ1, χ2, χ3 ∈Irr3′(B0(S))σ1 such that χi each extend to Aut(S).
(iii) If S is a group of Lie type in characteristic 3, then there exist nontrivial χ1, χ2, χ3 ∈Irr3′(B0(S))σ1
that are pairwise not Aut(S)-conjugate and such that χ1 is invariant under X, where X/S ∈
Syl3(Aut(S)/S).
We ﬁrst consider Theorem 3.7 for sporadic and alternating groups, as well as some “small” groups of
Lie type. For two positive integers n and m, we will use n ∥m to mean that n | m and gcd(n, m/n) = 1.
Proposition 3.8. Theorem 3.7 holds for the sporadic simple groups, G2(3), 2F4(2)′, B3(3), G2(2)′ =
PSU3(3), PSU4(3), and the alternating groups An with n ≥5.
Proof. Since the result can be seen directly using GAP for the other cases, we may assume S = An with
n > 10. In this case, S does not have a cyclic Sylow 3-subgroup and satisﬁes Aut(S) = Sn, where Sn
denotes the corresponding symmetric group.
The characters of Sn are rational-valued and parametrized by partitions of n, with their degrees given by
the hook formula. Further, two characters lie in the same 3-block if and only if they have the same 3-core.
We also know that χ ∈Irr(Sn) corresponding to the partition λ restricts irreducibly to An if and only if
1968
Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
Condition on n
Partition
χ(1)
3 | n
(1, n −1)
n −1
3 | n
(1, 1, n −2)
(n −1)(n −2)/2
3 ∥n, 32 | (n −2), or 3 ∥(n −1)
(3, n −3)
n(n −1)(n −5)/6
32 | n, 3 ∥(n −2), or 3 ∥(n −1)
(13, n −3)
(n −1)(n −2)(n −3)/6
3 | (n −1)
(2, n −2)
n(n −3)/2
32 | (n −1)
(1, 2, n −3)
n(n −2)(n −4)/3
32 | (n −1)
(13, 2, n −5)
n(n −2)(n −3)(n −4)(n −6)/30
3 | (n −2)
(1n−4, 2, 2)
n(n −3)/2
3 | (n −2)
(1n−2, 2)
n −1
Table 1. Some members of Irr3′(B0(Sn)) irreducible on An, n > 10.
the partition is not self-conjugate. Table 1 lists the partitions and character degrees for three characters in
Irr3′(Sn) that restrict irreducibly to An, completing the proof.
□
