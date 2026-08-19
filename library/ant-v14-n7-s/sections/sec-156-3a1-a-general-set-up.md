---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-156-3a1-a-general-set-up
section_title: "3A1. A general set-up"
section_number: null
pages: 298-302
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
such that there exist G a simple, simply connected algebraic group over Fq and F a Steinberg morphism
satisfying S= G/Z(G) with G:= G F perfect. Let (G∗, F∗) be dual to(G, F).
If Z(G) is trivial, we deﬁne ˜G:= G. Otherwise, we further let ι: G↪→˜G be a regular embedding as
in [Cabanes and Enguehard 2004, 15.1] and let ι∗: ˜G∗→ G∗ be the corresponding surjection of dual
groups. Write ˜G:=˜G F, G∗:=(G∗)F∗
, and ˜G∗:=(˜G∗)F∗
. We may then ﬁnd F-stable maximally split
tori T and˜T for G and ˜G, respectively, such that T≤˜T. Write T:= T F and˜T:=˜T F. Then Z(˜G) is
connected, G◁˜G, and Z(˜G)∩ G= Z(G). We will write˜S:=˜G/Z(˜G), and note that Aut(S) is generated
by˜S and the graph-ﬁeld automorphisms. Further, the (linear) characters of ˜G/G are in bijection with
elements of Z(˜G∗), and we have ˜χs⊗ˆz=˜χsz , where z∈ Z(˜G∗) corresponds toˆz∈ Irr(˜G/G) and for
semisimple s∈˜G∗,˜χs denotes the semisimple character of˜G corresponding to s. (See [Digne and Michel
1991, 13.30].) It will also be useful in what follows to note that if s∈[˜G∗,˜G∗] is semisimple, then the
semisimple character of ˜G corresponding to s is trivial on Z(˜G) by [Navarro and Tiep 2013, Lemma 4.4].
When q is a power of p, we note that Irrp′(B0(S))= Irrp′(S), which can be seen using [Cabanes and
Enguehard 2004, 6.14, 6.15, and 6.18] and the facts that p ∤|Z(G)| and S is a group with a strongly split
BN pair as in [loc. cit., 2.20].
In the case of types An−1 and 2An−1, we have S is PSLϵ
n(q) withϵ∈{± 1}; G= SLϵ
n(q); ˜G= GLϵ
n(q);
and˜S= PGLϵ
n(q). Here ϵ= 1 means S= PSLn(q),ϵ=− 1 means S= PSUn(q), and similarly for G
and ˜G. We use similar notation for other twisted types. For example, Eϵ
6(q) will denote E6(q) forϵ=+
and 2E6(q) forϵ=− .
3B. The case p= 2. Here we prove Theorem C in the case p= 2. The following, found in [Navarro
et al. 2018, Lemma 3.1], will be useful in what follows.
Lemma 3.2 (Navarro, Sambale and Tiep). Let G be a ﬁnite group. Ifχ∈ Irr2′(G) is real-valued, thenχ
belongs to B0(G).
In particular, note that an odd character degree ofG with multiplicity one must necessarily come from a
character ﬁxed by all automorphisms and G, which is therefore an X-invariant member of Irr2′(B0(G))σ1.
Lemma 3.3. Let S be a simple sporadic group, alternating group An with n≥ 5, or one of the simple
groups PSL2(4), PSL3(2), PSL3(4), PSU4(2), PSU4(3), PSLϵ
6(2), 2B2(8), B3(2), B3(3), D4(2), F4(2),
2F4(2)′, E6(2), 2E6(2), G2(2)′, G2(3), or G2(4). Then Theorem C holds for S and the prime p= 2.
Proof. For n≥ 7, the automorphism group of An is the symmetric group Sn. Recall that every irreducible
character of Sn is rational-valued and that an odd-degree character of Sn must restrict irreducibly to An
since it has index 2. In this case, if n= 2n1+···+ 2nt with n1< n2<··· < nt is the 2-adic decomposition
of n, then [Macdonald 1971, Corollary 1.3] yields that there are2n1+···+nt≥ 8 odd-degree characters of Sn,
whose restrictions therefore yield at least3 nontrivial members of Irr2′(B0(An))σ1 invariant under Aut(An).
Galois action on the principal block and cyclic Sylow subgroups 1965
For the remaining groups listed, the statement can be seen using [GAP 2004] and the GAP character table
library. In fact, we see that for the sporadic groups other than the Janko groups, there exist at least two
nontrivial odd character degrees with multiplicity 1. □
Proposition 3.4. Let S be a simple group of Lie type deﬁned over Fq with q a power of an odd prime𝓁.
Then Theorem C holds for S and the prime p= 2.
Proof. We may assume that S is not isomorphic to any of the groups in Lemma 3.3, so is as in Section 3A1.
In this case, the Steinberg character is rational-valued and Aut(S)-invariant, and therefore it sufﬁces to
show that there is another nontrivial member of Irr2′(B0(S))σ1. Further, we note that if S is not a Suzuki
or Ree group, then unipotent characters of odd degree are rational-valued (see, e.g., [Schaeffer Fry 2019,
Lemma 4.4]). Hence in these cases, applying Lemma 3.2, it sufﬁces to ﬁnd another nontrivial unipotent
character of odd degree, when possible. By observing the explicit list of unipotent character degrees in
[Carter 1985, Section 13.9], we see that there is at least one other nontrivial odd-degree unipotent character
for the exceptional groups G2(q), 3D4(q), F4(q), Eϵ
6(q), E7(q), and E8(q). For 2G2(q), we see from the
generic character table in [Geck et al. 1996] that there is another odd degree with multiplicity one.
For the classical groups An−1(q), 2An−1(q), Bn(q), Cn(q), Dn(q), or 2Dn(q), we know by [Malle
and Späth 2016, Proposition 7.4] that all unipotent characters of G with odd degree lie in the principal
series, and hence are in bijection with the odd-degree irreducible characters of the Weyl group W of
G. In these cases, W contains a quotient isomorphic to Sn, which has at least 4 odd-degree characters
for n≥ 4, again using [Macdonald 1971, Corollary 1.3]. We also see, for example using the GAP, that
there are at least 4 odd-degree characters of W in the case of B2, B3, and C3. Using the well-known
character table for PSL2(q), we see that all four odd-degree characters are ﬁxed by σ1. Further, in this
case, Irr2′(S)= Irr2′(B0(S)). We see from part (iii) of the proof of [Navarro et al. 2018, Theorem 3.3]
that if S= PSLϵ
3(q), then the Weil characterζ(q−ϵ)/2
3,q is a member of Irr 2′(B0(S)) and is real-valued. □
Proposition 3.5. Let S be a simple group of Lie type deﬁned in characteristic 2. Then Theorem C holds
for S for the prime p= 2.
Proof. Again, we may assume that S is not as in Lemma 3.3. In particular, we may keep the notation as
in Section 3A1 and we have Irr2′(B0(S))= Irr2′(S). If S is 2B2(q) or 2F4(q), then the generic character
tables available in CHEVIE yield the result, since |Out(S)| is odd and there are at least two distinct
degrees of nontrivial odd-degree characters whose values are ﬁxed by σ1.
Otherwise, we may take the Steinberg endomorphism on G to be F= Fq◦τ, where Fq is the standard
Frobenius induced by the map x↦→ xq andτ is some graph automorphism. Write q:= q|τ|= 22bm with
m odd and let X≤ Aut(S) such that X/S∈ Syl2(Out(S)).
Since q is a power of 2, we have Z(G)= 1 and ˜G= G unless S is one of PSLϵ
n(q) or Eϵ
6(q). In the
latter cases, G=[˜G,˜G]. In any case, since ˜G/G has odd order, we may view X/S as generated by Fm
2
and graph automorphisms.
Now, if m> 1, then the proof of [Schaeffer Fry and Taylor 2018, Lemma 6.4] (and taking into account
the remark after [loc. cit., Proposition 6.5]) yields a member of Irr2′(S) invariant under X which is the
1966 Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
restriction to G of a semisimple character of ˜G trivial on Z(G). Since semisimple elements have odd
order andσ1 ﬁxes odd roots of unity, Lemma 3.1 shows that this character is also ﬁxed byσ1. If m= 1, we
may similarly obtain an X-invariant member of Irr2′(S) ﬁxed byσ1 by arguing as in [loc. cit., Lemma 6.4]
and the remark after [loc. cit., Proposition 6.5] but using an element of F×
4 of order 3 rather than an
element of F×
q of order 5.
For S= G2(q), F4(q), 3D4(q), E7(q), or E8(q), the list of character degrees at [Lübeck 2007] yields
at least one more distinct nontrivial odd character degree, completing the proof in these cases, since by
[Malle 2007, Theorem 6.8], odd-degree characters are semisimple (recall that we may assume q⁄= 2
when S= G2(q) or F4(q)), and hence ﬁxed by σ1 using Lemma 3.1.
Now, in the remaining cases, S is a classical group or Eϵ
6(q). Here ˜G∗∼=˜G. In the case S= PSL2(q)
or PSLϵ
3(q), we see that there is at least one more odd-degree character with a different degree that is
ﬁxed byσ1, using the generic character tables available in [Geck et al. 1996]. If ˜G= GLϵ
n(q), Spn(q),
orϵ
n(q) with n≥ 4 and n even in the latter two cases, let s1 and s2 be elements of ˜G with eigenvalues
{δ,δ−1, 1,..., 1} and{δ,δ,δ −1,δ−1, 1,..., 1}, respectively, where 1⁄=δ∈ F×
q .
Then s1 and s2 are not Aut(S)-conjugate, and hence the corresponding semisimple characters of ˜G
have odd degree, are not Aut(S)-conjugate, and are ﬁxed by σ1 by Lemma 3.1. Further, if ˜G= GLϵ
n(q),
semisimple classes are determined by the eigenvalues, and Z(˜G) is comprised of scalar matrices, so we
see for i= 1, 2, si is not conjugate to si z for any z∈ Z(˜G) unless possibly if n= 6. In this case, we may
assume q⁄= 2 using Lemma 3.3 and instead take δ∈ F×
q2 to have order at least 5, again yielding si is not
conjugate to si z for any z∈ Z(˜G). In any case, the corresponding semisimple characters therefore restrict
irreducibly to G and are trivial on Z(˜G) since si∈[˜G,˜G]= G. Finally, let S be Eϵ
6(q) with q> 2. Then
we may argue analogously to [Giannelli et al. 2020, Proposition 4.3] to ﬁnd elements s1 and s2 in ˜G with
|C˜G(s1)|2⁄=| C˜G(s2)|2 such that the corresponding semisimple characters (which again must be ﬁxed by
σ1) are irreducible on G and trivial on Z(˜G). (Indeed, we may replace the δ used there with aδ∈ F×
q2
such that 3∤|δ|). In all cases, this yields at least one more nontrivial member of Irr2′(B0(S))σ1 that is not
Aut(S)-conjugate to the X-invariant one from above. □
Theorem C for p= 2 now follows by combining Propositions 3.4 and 3.5 with Lemma 3.3.
3C. The case p= 3. Here we prove Theorem C in the case p= 3. We begin by stating the following
classiﬁcation of simple groups with cyclic Sylow 3-subgroups.
Proposition 3.6. Let S be a ﬁnite nonabelian simple group with order divisible by 3. Then S has a cyclic
Sylow 3-subgroup if and only if S is one of : the alternating group A5; the sporadic simple group J1;
PSL2(q) for 3∤q; or PSLϵ
3(q) for 3|(q+ϵ).
Proof. The main result of [Shen and Zhou 2016] yields a classiﬁcation of simple groups S and primes p
such that S has an abelian Sylow p-subgroup. In particular, if p= 3, then such a simple group must be of
the form An with n< 9, one of a short list of sporadic simple groups, PSL2(q), PSLϵ
n(q) for 3|(q+ϵ)
and n= 3, 4, 5, or PSp4(q) with 3 ∤q.
Galois action on the principal block and cyclic Sylow subgroups 1967
Using the atlas [Conway et al. 1985] and since A6 has a noncyclic Sylow 3-subgroup and can be
viewed as a subgroup of An for n≥ 7, we see that the only simple alternating or sporadic groups with
cyclic Sylow 3-subgroups are A5 and the Janko group J1. The remaining possibilities are of the form
G/Z(G) for G a classical group SLϵ
n(q) with n< 6, or Sp4(q). Further, except in the cases of PSLϵ
3(q)
listed in the statement,|Z(G)| is relatively prime to 3, and hence S has a cyclic Sylow 3-subgroup if and
only if G does. Further, for the cases G= SLϵ
n(q) with n= 3, 4, 5 under consideration, we may view the
Sylow subgroup as a Sylow subgroup of ˜G= GLϵ
n(q), since[˜G: G] is not divisible by 3.
Now, using the description of the Sylow subgroups of classical groups in [Carter and Fong 1964;
Weir 1955], we see that the Sylow subgroups of GLϵ
4(q), GLϵ
5(q), and Sp4(q) are direct products of
Sylow subgroups of at least two lower-rank groups, and hence the Sylow 3-subgroup of G is not cyclic.
In the case PSLϵ
3(q) with 3|(q+ϵ) or PSL2(q) with 3∤q, we may explicitly construct a cyclic Sylow
3-subgroup. Finally, if S= PSL2(q) with 3| q, the Sylow 3-subgroup can be identiﬁed with the unipotent
radical of SL2(q), which is not cyclic unless q= 3, contradicting that S is simple. □
Our goal in the remainder of this section is to prove the following, from which we obtain Theorem C
for p= 3 as a corollary.
Theorem 3.7. Let S be a nonabelian simple group with order divisible by 3.
(i) If S has a cyclic Sylow 3-subgroup, then there exist 1S⁄=χ1,χ 2∈ Irr3′(B0(S))σ1 such thatχ1 extends
to Aut(S).
(ii) If S does not have a cyclic Sylow 3-subgroup and is not a group of Lie type deﬁned in characteristic3,
then there exist nontrivialχ1,χ 2,χ 3∈ Irr3′(B0(S))σ1 such thatχ1 andχ2 extend to Aut(S). In this
case, if S is further not one of A6, A7, 2F4(2)′, PSLn(q) with n≤ 4, or PSp4(22m+1), then there exist
nontrivialχ1,χ 2,χ 3∈ Irr3′(B0(S))σ1 such thatχi each extend to Aut(S).
(iii) If S is a group of Lie type in characteristic 3, then there exist nontrivialχ1,χ 2,χ 3∈ Irr3′(B0(S))σ1
that are pairwise not Aut(S)-conjugate and such that χ1 is invariant under X, where X/S∈
Syl3(Aut(S)/S).
We ﬁrst consider Theorem 3.7 for sporadic and alternating groups, as well as some “small” groups of
Lie type. For two positive integers n and m, we will use n‖ m to mean that n| m and gcd(n, m/n)= 1.
Proposition 3.8. Theorem 3.7 holds for the sporadic simple groups , G2(3), 2F4(2)′, B3(3), G2(2)′=
PSU3(3), PSU4(3), and the alternating groups An with n≥ 5.
Proof. Since the result can be seen directly using GAP for the other cases, we may assume S= An with
n> 10. In this case, S does not have a cyclic Sylow 3-subgroup and satisﬁes Aut(S)= Sn, where Sn
denotes the corresponding symmetric group.
The characters of Sn are rational-valued and parametrized by partitions ofn, with their degrees given by
the hook formula. Further, two characters lie in the same 3-block if and only if they have the same 3-core.
We also know thatχ∈ Irr(Sn) corresponding to the partitionλ restricts irreducibly to An if and only if
1968 Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
Condition on n Partition χ(1)
3| n (1, n− 1) n− 1
3| n (1, 1, n− 2) ( n− 1)(n− 2)/2
3‖ n, 32|(n− 2), or 3‖(n− 1) ( 3, n− 3) n(n− 1)(n− 5)/6
32| n, 3‖(n− 2), or 3‖(n− 1) ( 13, n− 3) ( n− 1)(n− 2)(n− 3)/6
3|(n− 1) ( 2, n− 2) n(n− 3)/2
32|(n− 1) ( 1, 2, n− 3) n(n− 2)(n− 4)/3
32|(n− 1) ( 13, 2, n− 5) n(n− 2)(n− 3)(n− 4)(n− 6)/30
3|(n− 2) ( 1n−4, 2, 2) n(n− 3)/2
3|(n− 2) ( 1n−2, 2) n− 1
Table 1. Some members of Irr3′(B0(Sn)) irreducible on An, n> 10.
the partition is not self-conjugate. Table 1 lists the partitions and character degrees for three characters in
Irr3′(Sn) that restrict irreducibly to An, completing the proof. □
