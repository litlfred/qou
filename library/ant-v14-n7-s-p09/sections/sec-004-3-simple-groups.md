---
doc_id: ant-v14-n7-s-p09
doc_title: "Galois action on the principal block and cyclic Sylow subgroups"
section_id: sec-004-3-simple-groups
section_title: "Simple groups"
section_number: 3
pages: 10-25
source_pdf: ant-v14-n7-s-p09.pdf
source_sha256: c8fe963200a79d25
doc_brief: "Galois action on the principal block and cyclic Sylow subgroups — 8 sections: Introduction; Blocks with normal defect group; Suppose that|D|= 2n. Since G/CD ac"
---
Theorem 2.6 below. Theorem C collects the properties of simple groups that will be key for performing
such reduction. We would like to remark that the conditions in Theorem C related to the conjugation by
group automorphisms are not needed in this context, but may be of independent interest.
Theorem 2.6. Let G be a ﬁnite group of order divisible by p where p∈{ 2, 3}. Let P∈ Sylp(G). Then
|Irrp′(B0(G))σ1|= p if, and only if, P is cyclic.
Proof. If P is cyclic, then|Irrp′(B0(G))σ1|= p by Lemma 1.3.
We assume now that|Irrp′(B0(G))σ1|= p and we work to prove that P is cyclic by induction on the
order of G.
First, notice that we may assume that G is not simple, by Theorem C(a), and NG(P) <G by
Theorem 1.5.
Step 1. We may assume Op′(G)= 1. This follows by Lemma 2.1(a) and induction.
Step 2. We may assume that O p′
(G)= G. Otherwise, let M◁ G with|G/M| not divisible by p and
G/M> 1 simple. Then P⊆ M and by the Frattini argument M NG(P)= G. Hence M CG(P)◁ G and
therefore G= CG(P)M or CG(P)⊆ M. Suppose G= M CG(P), then restriction deﬁnes a bijection
Irrp′(B0(G))σ1→ Irrp′(B0(M))σ1 by Theorem 2.3. In this case we are done by induction. Therefore we
may assume that CG(P)⊆ M. We claim that B0(G) is the only block of G covering B0(M). Indeed, let
B be a block of G covering B0(M). By [Navarro 1998, Theorem 9.26], we have that P is a defect group
of B. By [loc. cit., Lemma 9.20], B is regular with respect to M and hence by [loc. cit., Theorem 9.19],
B0(M)G= B. By Brauer’s third main theorem we have that B0(M)G= B0(G) and hence B= B0(G)
and the claim is proven. In particular, Irr(G/M)⊆ Irrp′(B0(G))σ1 as every character in Irr(G/M) has
p′-degree and is σ1-invariant (for G/M is a p′-group). By hypothesis|Irr(G/M)|≤ p. As G/M is a
nontrivial p′-group, we immediately get a contradiction if p= 2. If p= 3, then|Irr(G/M)|≤ 3 forces
G/M= C2. Write Irrp′(B0(G))σ1={ 1,λ,θ} with M⊆ kerλ, for instance. Let τ∈ Irrp′(B0(M))σ1 be
nontrivial by Lemma 1.4. Let χ∈ Irr(B0(G)) be overτ. Since|G/M| is not divisible by p, we have that
χ∈ Irrp′(B0(G))σ1 by [Navarro and Tiep 2019, Lemma 5.1]. Thus necessarily χ=θ. SinceθM has at
most two irreducible constituents, we have that|Irrp′(B0(M))σ1|= 3 and we are done by induction in
this case.
Step 3. If 1⁄= M◁ G, then everyχ∈ Irrp′(B0(G))σ1 satisﬁes M⊆ kerχ and P M/M> 1 is cyclic. By
Step 2, we have that p divides|G/M| and hence|Irrp′(B0(G/M))σ1|= p follows from Lemma 1.4. The
claim of the step now follows from Lemma 2.1(a) and by induction.
Step 4. If 1⁄= M◁G andγ∈ Irrp′(B0(M P))σ1, then there is someχ∈ Irrp′(B0(G))σ1 lying overγ . Write
H= M PCG(P), so that M P◁ H. By Theorem 2.3, restriction deﬁnes a bijection Irrp′(B0(H))σ1→
Irrp′(B0(M P))σ1, and hence someθ∈ Irrp′(B0(H))σ1 extendsγ . By Lemma 2.4, the claim of the step
follows.
Galois action on the principal block and cyclic Sylow subgroups 1963
Step 5. Let N be a minimal normal subgroup of G. We may assume PN < G. Suppose the contrary. By
Step 1 and the fact that NG(P)< G (so G is not a p-group), we have that N is the direct product of t
copies of a nonabelian simple group S of order divisible by p (which are transitively permuted by G). By
Theorem C there exist 1S⁄=φ∈ Irrp′(B0(S))σ1 X-invariant for some X∈ Sylp(Aut(S)). By Lemma 2.5,
there is some 1N⁄=θ∈ Irrp′(B0(N))σ1 that extends to aσ1-invariant characterχ∈ Irr(G). Since B0(G)
is the only block covering B0(N) by [Navarro 1998, Corollary 9.6], we have that χ∈ Irrp′(B0(G))σ1
contradicting Step 3.
Final Step. Since NP < G by Step 5, if|Irrp′(B0(NP))σ1|= p, then we are done by induction. Hence
we may assume that|Irrp′(B0(NP))σ1|> p by Lemma 1.4. By Step 3, we have that PN/N is cyclic, and
hence|Irrp′(B0(PN/N))σ1|= p. Therefore there exists some θ∈ Irrp′(B0(NP))σ1 such that N ⊈ ker(θ)
(here we are using that NP/N has just one p-block). By Step 4, some χ∈ Irrp′(B0(G))σ1 lies overθ. In
particular N ⊈ kerχ, a contradiction with Step 3. □
3. Simple groups
In this Section we prove Theorem C, which will complete the proof of Theorem A.
3A. Some generalities on groups of Lie type. Since the groups of Lie type play a large role in what
follows, we begin by recalling some essentials about their blocks and characters.
Let q be a power of a prime. When G= G F is the group of ﬁxed points of a connected reductive
algebraic group G deﬁned over Fq under a Steinberg map F, the set of irreducible characters Irr(G) can be
written as a disjoint union ⨆ E(G, s) of so-called rational Lusztig series corresponding to G∗-conjugacy
classes of semisimple elements s∈ G∗ (i.e., elements of order relatively prime to q). Here G∗=(G∗)F∗
,
where(G∗, F∗) is dual to(G, F).
With this notation, we record the following lemma, proved in [Schaeffer Fry and Taylor 2018,
Lemma 3.4], which describes the action of H on the set of rational Lusztig series and will be useful
throughout this section.
Lemma 3.1. Let p be a prime and let s∈ G∗ be a semisimple element. Let f and b be integers and let
σ∈ H be such thatσ(ξ)=ξ p f
for all p′-roots of unityξ andσ(ζ)=ζ b for all p-power roots of unityζ .
Ifχ∈ E(G, s), thenχσ∈ E(G, s p f
p′ sb
p).
The characters in the series E(G, 1) are called unipotent characters, and there is a bijection E(G, s)→
E(CG∗(s), 1). Hence, characters of Irr(G) may be indexed by pairs (s,ψ) , where s∈ G∗ is a semisimple
element, up to G∗-conjugacy, andψ∈ Irr(CG∗(s)) is a unipotent character of CG∗(s). We remark that
CG∗(s) may fail to be connected, in which case unipotent characters of CG∗(s) are taken to be those lying
over a unipotent character of(CG∗(s)◦)F. In particular, we will denote by χs the character indexed by
(s, 1CG∗(s)), which are semisimple, and they have degree|G∗: CG∗(s)|q′.
Using [Cabanes and Enguehard 2004, Theorem 9.12], it follows that when p ∤q, the set Ep(G, 1):=⋃ E(G, s), where s ranges over elements of p-power order in G∗, is a union of p-blocks (ﬁrst shown
1964 Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
in [Broué and Michel 1989]) and that each such block intersects E(G, 1) nontrivially. Such blocks are
called unipotent blocks.
3A1. A general set-up. We will often be interested in the following situation: Let S be a simple group
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
3C1. Lie type in cross-characteristic for p= 3. In this section, we prove Theorem 3.7 for groups of Lie
type in nondeﬁning characteristic. That is, we deal with the case S is of the form G/Z(G) for G a ﬁnite
group of Lie type of simply connected type deﬁned over a ﬁeld Fq with 3∤q. (Given Proposition 3.8, this
will complete the proof of parts (i) and (ii) of Theorem 3.7.)
We will use 8m to denote the m-th cyclotomic polynomial in the variable q. Note that using e.g.,
[Malle 2007, Lemma 5.2], 3 divides8m if and only if m= 3id for some i≥ 0, where d is the order of q
modulo 3, and in this case 3‖8m unless m= d.
Proposition 3.9. Let S be a simple group of Lie type deﬁned over Fq with 3∤q and assume S is not one of
the groups PSLϵ
n(q) with n≤ 3. Then there exist three nontrivial charactersχ1,χ 2,χ 3∈ Irr3′(B0(S))σ1
such thatχ1 andχ2 extend to Aut(S).
Further, if S is not PSLϵ
4(q) nor PSp4(2a) with a odd, thenχ1,χ2, andχ3 may be chosen to extend to
Aut(S).
Proof. We may assume that S is not isomorphic to one of the groups considered in Proposition 3.8.
Keep the notation and considerations for G, ˜G, ˜T , and ˜S from Section 3A. By the work of Lusztig
[1988], the unipotent characters of ˜G are trivial on Z(˜G) and restrict irreducibly to G. Further, when
viewed as characters of˜S, they are extendible to Aut(S), by [Malle 2008, Theorems 2.4 and 2.5], aside
from some speciﬁc exceptions. The only unipotent characters which take irrational values occur for
exceptional groups and have values in Q(
√
−1,ζ 3,ζ 5,√q), whereζ3 andζ5 are third and ﬁfth roots of
unity, respectively, by [Geck 2003, Proposition 5.6 and Table 1]. In any case, the unipotent characters are
σ1-invariant, since√q is a sum of roots of unity of order relatively prime to 3.
Let d be the order of q modulo 3. In particular, we have d= 1 or 2. If d= 1, unipotent characters of
degree relatively prime to 3 are constituents of the Harish-Chandra induced character R˜G
˜T(1) using [Malle
Galois action on the principal block and cyclic Sylow subgroups 1969
Type Condition on d Character χ(1)(notation from [Carter 1985, 13.9])
G2(q)
d= 1 φ2,2 1
2q82
286
φ1,3′ 1
3q8386
d= 2 G2[1] 1
6q82
186
φ1,3′ 1
3q8386
3D4(q) d= 1, 2 φ1,3′ q812
φ1,3′′ q7812
F4(q)
d= 1 φ4,1 1
2q82
282
688
φ8,3′ q382
488812
d= 2 B2,ϵ 1
2q1382
182
388
B2,1 1
2q82
182
388
E6(q) d= 1, 2 φ20,2 q2848588812
φ20,20 q20848588812
2E6(q) d= 1, 2 φ4,1 q28488810812
φ4,13 q208488810812
E7(q) d= 1, 2 φ7,1 q87812814
φ7,46 q4687812814
E8(q) d= 1, 2 φ8,1 q82
488812820824
φ35,2 q28587810814815820830
2B2(q), Note: 3 ∤|S|
2B2[a] 1√
2q(q2− 1)
q2= 22m+1 2B2[b] 1√
2q(q2− 1)
2F4(q), Note: 3|(q2+ 1) cusp 1
12q482
182
2(8′
8)2812(8′
24)2
q2= 22m+1 cusp 1
12q482
182
2(8′′
8)2812(8′′
24)2
Table 2. Some unipotent characters in Irr 3′(B0(S))σ1 for exceptional types with 3 ∤q.
2007, Corollary 6.6]. Further, by [Enguehard 2000, Theorem A], all members of R˜G
˜T(1) lie in the same
block, namely B0(˜G).
If d= 2, then the centralizer of a Sylow d-torus is a maximal torus, using e.g., [Malle and Späth 2016,
Lemma 3.2]. Unipotent blocks of ˜G are parametrized by certain ˜G-conjugacy classes of pairs (˜L,λ)
where˜L is a d-split Levi subgroup of ˜G andλ is a d-cuspidal unipotent character of˜L, by [Enguehard
2000, Theorem A]. Further, a unipotent character in the block parametrized by (˜L,λ) can have 3′-degree
1970 Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
n Additional Condition on n, e Partition χ(1)q′
n≥ 6 e= 2 and n even; or (1, n− 1) qn−1−ϵn−1
q−ϵe= 1 and 3 ∤(n− 1) ( 1n−2, 2)
n≥ 6 e| n and 3 ∤n (2, n− 2) (qn−ϵn)(qn−3−ϵn−3)
(q−ϵ)(q2−1)(1n−4, 2, 2)
n≥ 6 3| n; or (1, 1, n− 2) (qn−1−ϵn−1)(qn−2−ϵn−2)
(q−ϵ)(q2−1)e= 2 and n odd and 3|(n− 2) ( 1n−3, 3)
n≥ 6 e= 2 and n odd and 3|(n− 1)
(1, 1, 2, n− 4) (qn−ϵn)(qn−2−ϵn−2)(qn−3−ϵn−3)(qn−5−ϵn−5)
(q−ϵ)2(q2−1)2(q2+1)
(2, n− 2) (qn−ϵn)(qn−3−ϵn−3)
(q−ϵ)(q2−1)
n= 5 e= 1 (1, 4) (q+ϵ)(q2+ 1)
(1, 1, 1, 2)
n= 5 e= 2 (2, 3) q5−ϵ
q−ϵ
(1, 1, 3) ( q2+ 1)(q2+ϵq+ 1)
n= 4 e= 2 (1, 3) q2+ϵq+ 1
(1, 1, 2)
n= 4 e= 1 (2, 2) q2+ 1
Table 3. Some unipotent characters in Irr 3′(B0(S))σ1 for type Aϵ
n−1(q) with n≥ 4 and 3 ∤q.
only when˜L is the centralizer of a Sylow d-torus, using [Malle 2007, Corollary 6.6]. This yields that
again in the case d= 2, there is a unique block of ˜G containing unipotent characters of 3′-degree.
Hence when 3∤q, every unipotent character in Irr3′(˜G) is a member of Irr3′(B0(˜G))σ1, and restricts to
a member of Irr3′(B0(G))σ1 trivial on the center. Then this restriction may be viewed as an element of
Irr3′(B0(S))σ1, using e.g., [Cabanes and Enguehard 2004, Lemma 17.2].
In particular, since the Steinberg character has degree a power ofq, it sufﬁces to ﬁnd two more unipotent
characters of 3′-degree that are not one of the exceptional cases in [Malle 2008, Theorem 2.5]. In what
follows, we will use the notation and degrees for unipotent characters as in [Carter 1985, Sections 13.8
and 13.9].
Exceptional Types. In the case that S is an exceptional group of Lie type deﬁned over Fq with 3∤q, we
list in Table 2 two unipotent characters invariant under Aut(S) that have degree relatively prime to 3,
completing the proof in this case.
Types A n−1 and 2An−1, n≥ 4. In this case, let S be PSLϵ
n(q) with n≥ 4 andϵ∈{± 1}. Write e∈{ 1, 2}
for the number such that q≡ϵe (mod 3). That is, e is the order ofϵq modulo 3. Two unipotent characters
are in the same 3-block of˜G= GLϵ
n(q) if and only if they have the same e-core (see [Fong and Srinivasan
Galois action on the principal block and cyclic Sylow subgroups 1971
1982]). For n≥ 5 or for(n, e)=(4, 2), the unipotent characters described in Table 3 are Aut(S)-invariant
members of Irr3′(B0(S))σ1.
Now assume n= 4 and e= 1. Then the unipotent character in the last line of Table 3 is an Aut(S)-
invariant member of Irr3′(B0(S))σ1. In this case, 1S, StS, and the character listed are the only unipotent
characters in Irr3′(S). However, since e= 1, we see that every unipotent character is a member of the
principal block of ˜G, which means that E3(˜G, 1) is comprised of only one block. Let ζ∈ F×
q2 with order 3.
Then taking s to be the element diag(ζ,ζ,ζ, 1) of ˜G∗∼= GLϵ
4(q), the semisimple characterχs∈ E(˜G, s)
lies in the principal block of ˜G and is trivial on Z(˜G) since s∈ SLϵ
4(q)∼=[˜G∗,˜G∗]. Further, we see using
Lemma 3.1 thatχs is ﬁxed by σ1.
Since C˜G∗(s)∼= GLϵ
1(q)× GLϵ
3(q), we see
χs(1)=(q+ϵ)(q2+ 1).
Further, since the semisimple classes of ˜G are determined by their eigenvalues and Z(˜G) is comprised of
scalar matrices, we see that s is not conjugate to sz for any nontrivial z∈ Z(˜G). Henceχs|G is irreducible,
by the second-to-last paragraph of Section 3A, and is therefore a member of Irr3′(B0(G)), since the
principal block of G is the only block covered by the principal block of ˜G. But since Z(G)≤ Z(˜G) is
in the kernel ofχs, this character is therefore a member of Irr3′(B0(G/Z(G)))σ1= Irr3′(B0(S))σ1, again
using [Cabanes and Enguehard 2004, Lemma 17.2]. Note that this character is not Aut(S)-conjugate to
1S, StS, nor the unipotent character labeled by (2, 2), which completes the proof for S= PSLϵ
n(q) with
n≥ 4.
Types B n and C n, n≥ 2. When S is type Bn or Cn with n≥ 2 deﬁned in characteristic different than 3,
Table 4 exhibits at least two distinct unipotent characters in Irr3′(B0(S))σ1 that are Aut(S)-invariant, with
the exception of the case S= PSp4(2a) with a odd. In the latter situation, we may instead consider the
characters indexed by
( 1 2
0
)
and
( 0 1 2
∅
)
with degrees q
2(q2+ 1) and q
2(q− 1)2, respectively. (Note that we
do not consider PSp4(2)∼= S6.) These characters lie in Irr3′(B0(S))σ1 and the latter character extends to
Aut(S). (However, we remark that the ﬁrst character is not Aut(S)-invariant, as in this case it is switched
with
( 0 1
2
)
under the action of the graph automorphism, by [Malle 2008, Theorem 2.5]).
Type D n and 2Dn, n≥ 4. In this case, if S is not D4(q), Tables 5 and 6 list at least two distinct unipotent
characters that are Aut(S)-invariant members of Irr3′(B0(S))σ1. If S is D4(q) and 3|(q− 1), we may
instead take the unipotent characters labeled by symbols
( 1
0
3
2
)
and
(3
1
)
withχ(1)q′= 1
2(q+ 1)3(q3+ 1)
and(q2+ 1)2, respectively. When 3|(q+ 1), we may take the characters index by
(3
1
)
and
( 0 1 2 3
∅
)
, the
latter of which satisﬁes χ(1)q′= 1
2(q− 1)3(q3− 1). □
We next establish Theorem 3.7 for the case that S has cyclic Sylow 3-subgroups, which we recall from
Proposition 3.6 occurs when S= PSL2(q) for 3 ∤q and when S= PSLϵ
3(q) for 3|(q+ϵ).
Proposition 3.10. Let S= PSL2(q) with 3∤q or PSLϵ
3(q) with 3|(q+ϵ). Then there exist nontrivial
χ1,χ 2∈ Irr3′(B0(S))σ1 such thatχ1 extends to Aut(S).
1972 Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
Conditions on q, n Symbol χ(1)q′
(
possibly excluding factors of 1
2
)
3|(q− 1) or
3|(q+ 1); n even; 3∤(n− 1) or
( 0 1
n
) (qn−1+1)(qn+1)
q+1
3|(q+ 1); n odd; 3 ∤n
3|(q− 1); 3∤n
( 0 2
n−1
) (q2n−1)(qn−3+1)(qn−1+1)
q4−1
3|(q− 1); 3∤(n− 1) or ( 1 n
0
) (qn−1−1)(qn+1)
q−13|(q+ 1); n even
3|(n− 1)
( 1 n−1
1
) (q2n−1)(q2(n−2)−1)
(q2−1)2
3|(q+ 1); n odd or ( 0 n
1
) (qn−1+1)(qn−1)
q−13|(q− 1); 3 ∤n
3|(q+ 1); n odd; 3| n or
3|(q+ 1); n even; 3|(n− 2) or
( 0 1 n
1 2
) (q2(n−1)−1)(qn−1)(qn−2+1)
(q2−1)2
3|(q− 1); 3|(n− 2)
Table 4. Some unipotent characters in Irr3′(B0(S))σ1 for type Bn(q) and Cn(q) with
n≥ 2 and 3 ∤q.
Proof. First let S= PSL2(q) with 3∤q. In this case, every character of S is either 3-defect zero or has
degree prime to 3. As before, the Steinberg character is a member of Irr3′(B0(S))σ1 and extends to Aut(S).
Further, the only two unipotent characters, 1˜G and St˜G, both lie in the principal block of ˜G= GL2(q),
and hence there is a unique unipotent block of ˜G. We may takeχ1= StS as before.
Now, let s∈˜G= GL2(q) have eigenvaluesζ,ζ−1, whereζ∈ F×
q2 has order 3. Then the semisimple
characterχs∈ E(˜G, s)⊆ E3(˜G, 1) lies in the principal block of ˜G and is trivial on Z(˜G) since s∈
SL2(q)∼=[˜G∗,˜G∗]. Since sz is not conjugate to s for 1⁄= z∈ Z(˜G∗), we also see χs is irreducible on
restriction to G. Further, Lemma 3.1 yields that χs is ﬁxed by σ1. Then the restriction (χs)G lies in
B0(G) since the principal block of ˜G covers a unique block of G. Finally, in this case χs(1)= q+η,
whereη∈{± 1} is such that 3| q−η. Hence this character may be viewed as a member of Irr3′(B0(S))σ1,
arguing as before.
Now let S= PSLϵ
3(q) with 3|(q+ϵ). Then
S= G= SLϵ
3(q) and ˜G∗∼=˜G= G× Z(˜G).
Since the unipotent characters of G are 1G, StG, and a character of degree q(q+ϵ), we see that again
B0(G) is the only unipotent block of maximal defect (as the other has defect zero). Then every character
of E3(G, 1) with 3′-degree is a member of B0(G). We may again takeχ1= StG. Taking s∈˜G∗ to have
Galois action on the principal block and cyclic Sylow subgroups 1973
Conditions on q, n Symbol χ(1)q′
(
possibly excluding factors of 1
2
)
3∤(n− 1)
( 1 n
0 1
) q2(n−1)−1
q2−1
3| n
( 1 2 n
0 1 2
) (q2(n−2)−1)(q2(n−1)−1)
(q2−1)2(q2+1)
3|(n− 2) or ( n−2
2
) (q2(n−1)−1)(qn−1)(qn−4+1)
(q2−1)2(q2+1)3|(q+ 1); 3| n; n odd
3|(q− 1); 3|(n− 1) or ( 1 n−1
0 2
) (qn−1)(qn−2−1)(qn−1+1)(qn−3+1)
(q−1)2(q2+1)3|(q+ 1); n odd
3|(q− 1); 3|(n− 2) or
3|(q+ 1); 3∤n; n even or
( 0 n−1
1 2
) (qn−1)(qn−2+1)(qn−1−1)(qn−3+1)
(q2−1)2
3|(q+ 1); 3| n; n odd
3|(q− 1); 3∤n or
( n−1
1
) (qn−1)(qn−2+1)
q2−1
3|(q+ 1); 3|(n− 1) or
3|(q+ 1); 3|(n− 2); n even or
3|(q+ 1); 3| n; n odd
Table 5. Some unipotent characters in Irr 3′(B0(S))σ1 for type Dn(q) with n≥ 5 and 3 ∤q.
eigenvalues{ζ,ζ−1, 1}, whereζ∈ F×
q2 has order 3, the corresponding character of G has degree q3−ϵ,
and we may again view(χs)G as a character of Irr 3′(B0(S))σ1. □
Proposition 3.11. Let S= PSLϵ
3(q) with 3|(q−ϵ). Then there exist nontrivialχ1,χ 2,χ 3∈ Irr3′(B0(S))σ1
such thatχ1 andχ2 extend to Aut(S).
Proof. In this case, we see that all three unipotent characters are members of Irr3′(˜G) and that there
is a unique unipotent block B0(˜G). Further, the unipotent characters are rational-valued, and therefore
are members of Irr3′(B0(˜G))σ1. Then we may take χ1 andχ2 to be the restrictions to G (viewed as a
character of S) of the two nontrivial unipotent characters.
The semisimple element s∈ ˜G∗ with eigenvalues{ζ,ζ−1, 1}, where ζ∈ F×
q2 has order 3, is now
conjugate to sz where z=ζ· I3∈ Z(˜G∗). The corresponding semisimple character has degree χs(1)=
(q+ϵ)(q2+ϵq+ 1), soχs∈ Irr(B0(˜G))σ1 satisﬁes 3‖χs(1) and is not irreducible on restriction to G.
Then the constituents of the restriction to G are members of Irr3′(B0(G)), and are trivial on Z(G) since
s∈[˜G∗,˜G∗]∼= G, so it sufﬁces to see that they are also σ1-invariant, using the character table available
in CHEVIE. □
Together, Propositions 3.9 through 3.11 yield Theorem 3.7 for the simple groups of Lie type in
nondeﬁning characteristic, completing parts (i) and (ii).
1974 Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
Conditions on q, n Symbol χ(1)q′
(
possibly excluding factors of 1
2
)
3∤(n− 1)
( 0 1 n
1
) q2(n−1)−1
q2−1
3|(n− 1) or
( 1 n−1
∅
) (qn+1)(qn−2−1)
q2−1
3|(q− 1); 3| n or
3|(q+ 1); 3| n; n even or
3|(q+ 1); 3|(n− 2); n odd
3|(q− 1); 3∤(n− 1) or
3|(q+ 1); 3|(n− 2) or
( 2 n−2
∅
) (q2(n−1)−1)(qn+1)(qn−4−1)
(q2−1)2(q2+1)
3|(q+ 1); 3| n; n even
3| n
( 0 1 2 n
1 2
) (q2(n−1)−1)(q2(n−2)−1)
(q2−1)2(q2+1)
3|(q− 1); 3|(n− 1)
3|(q+ 1); 3∤n; n odd
( 1 2 n−1
0
) (qn+1)(qn−1+1)(qn−2−1)(qn−3−1)
(q2−1)2
3|(q+ 1); 3| n; n even
3|(q− 1); 3| n
3|(q+ 1); 3|(n− 1); n even
( 0 1 n−1
2
) (qn+1)(qn−1−1)(qn−2−1)(qn−3+1)
(q2−1)2
3|(q+ 1); 3|(n− 2); n odd
Table 6. Some unipotent characters in Irr 3′(B0(S))σ1 for type 2Dn(q) with n≥ 4 and 3 ∤q.
3C2. Lie type in deﬁning characteristic for p= 3. We now consider the case S is as in Section 3A1 with
G of simply connected type deﬁned in characteristic 3. Let(G∗, F∗) be dual to(G, F). Keep in mind
the notations and considerations of Section 3A, where now q is a power of 3. Note that|˜S/S|=| Z(G)|,
and this is 1 unless G is of classical type or G= E7,sc(q).
Since ˜G/G has size prime to 3, it follows that any irreducible character of G lying under Irr3′(˜G) is
a member of Irr3′(G). Since|σ1| is a power of 3, we further see that for any ˜χ∈ Irr3′(˜G)σ1, there is a
member of Irr3′(G)σ1 lying under ˜χ. We also have Irr3′(B0(S))= Irr3′(S), so any member of Irr3′(G)
with Z(G) in its kernel may be viewed as a member of Irr 3′(B0(S)).
Now, given a semisimple element s∈ ˜G∗, we have|s| is prime to 3, and hence the Lusztig series
E(˜G, s) is ﬁxed byσ1 using Lemma 3.1. Then in particular, the unique semisimple character˜χs∈ Irr3′(˜G)
in this series must be ﬁxed by σ1. To illustrate three nontrivial characters of Irr3′(G)σ1 that are not
Aut(S)-conjugate, it therefore sufﬁces to show that there are semisimple elements 1⁄= s1, s2, s3∈˜G∗
such that
Galois action on the principal block and cyclic Sylow subgroups 1975
(1) si is not ˜G∗-conjugate to sϕ
j z for i⁄= j, z∈ Z(˜G∗), andϕ any (possibly trivial) graph-ﬁeld automor-
phism.
In most cases, we further ensure that one of these characters is Aut(S)-invariant, by choosing s1 so that
(2) the class of s1 is invariant under graph-ﬁeld automorphisms and
(3) s1 is not ˜G∗-conjugate to s1z for any 1⁄= z∈ Z(˜G∗).
Property (2) will ensure that ˜χs1 is invariant under graph-ﬁeld automorphisms, using [Navarro et al. 2008,
Corollary 2.4], and property (3) will imply that ˜χs1 restricts irreducibly to G, so the resulting character of
G is Aut(S)- andσ1-invariant. Finally, we will choose s1, s2, and s3 such that
(4) si∈[˜G∗,˜G∗] for i= 1, 2, 3,
so that the ˜χsi are trivial on Z(˜G), ensuring that all three characters of G may be viewed as characters of
Irr3′(B0(S))σ1 from the above discussion.
Proposition 3.12. Let S= G2(q), 3D4(q), 2G2(q), E±
6(q), E7(q), F4(q) or E8(q) be simple with q a
power of 3. Then there exist nontrivialχ1,χ 2,χ 3∈ Irr3′(B0(S))σ1 that are pairwise not Aut(S)-conjugate
and such thatχ1 is Aut(S)-invariant.
Proof. Note that we may assume S is not one of the groups from Proposition 3.8. The character degrees in
these cases are available at [Lübeck 2007]. If S is G2(q), 3D4(q), 2G2(q), E6(q), 2E6(q), F4(q) or E8(q),
then ˜G= G= S and there is a nontrivial odd character degree of multiplicity one, which therefore must
beσ1- and Aut(S)-invariant. Similarly, E7(q) has a unique character of degree 83868789812814818,
which restricts irreducibly from a character of ˜S= E7(q)ad . Finally, in each case there are at least two
more semisimple characters with different degrees, which must yield members of Irr3′(B0(S))σ1 by the
above discussion. □
Proposition 3.13. Let S= PSLϵ
n(q) be simple with q a power of 3 and n≥ 2 and let X≤ Aut(S) such
that X/S is a Sylow 3-subgroup of Aut(S)/S. Then there exist nontrivialχ1,χ 2,χ 3∈ Irr3′(B0(S))σ1 that
are pairwise not Aut(S)-conjugate and such thatχ1 is X-invariant. Further, if n≥ 3, thenχ1 may be
chosen to be Aut(S)-invariant, and if n≥ 5, thenχ1,χ 2,χ 3 may all be chosen to be Aut(S)-invariant.
Proof. Throughout, let δ∈ F×
q2 have order 4 and assume S is not isomorphic to one of the groups in
Proposition 3.8. Recall that the conjugacy classes of semisimple elements in˜G∗= GLϵ
n(q) are determined
by their eigenvalues and that Z(˜G∗) is comprised of scalar matrices.
If n= 2, then|˜S/S|= 2 and Aut(S)/˜S is generated by a ﬁeld automorphism. The semisimple elements
s1, s2, and s3 with eigenvalues{δ,δ−1},{ζ1,ζ−1
1 }, and{ξ1,ξ−1
1 } withζ1∈ F×
q andξ1∈ F×
q2\ F×
q and
|ξ|⁄= 4⁄=|ζ| satisfy properties (1), (2), and (4). Now, since ˜χs1 is ﬁxed by ﬁeld automorphisms, and
hence by X, and since|˜S/S| is relatively prime to 3, we see that the irreducible constituents of the
restriction(˜χs1)G are still ﬁxed by X and byσ1. If n= 3 or 4, then s1, s2, s3 satisfy (1)–(4) if chosen to
have eigenvalues{δ,δ−1},{−1,−1}, and{ξ,ξ−1} with remaining eigenvalues 1, where|ξ|> 2 divides
q+η if 4| q−η.
1976 Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
Now suppose that n≥ 5. Consider semisimple elements s1, s2, and s3 of˜G∗= GLϵ
n(q) with eigenvalues
(δ,δ−1, 1,..., 1),(−1,−1, 1,..., 1), and(δ,δ−1,δ,δ −1, 1,..., 1), respectively. If n= 6, instead deﬁne
s3 to have eigenvalues (−1,−1,−1,−1, 1, 1). Then these satisfy (1)–(4), and in fact properties (2)
and (3) are held by all three elements. Hence the corresponding semisimple characters ˜χsi of ˜G are
invariant under graph-ﬁeld automorphisms and restrict irreducibly to members of Irr3′(B0(G))σ1 that are
trivial on Z(G). Hence these restrictions are members of Irr 3′(B0(S))σ1 invariant under Aut(S). □
Proposition 3.14. Let q be a power of 3. Let S= PSp2n(q), P2n+1(q), or P±
2n(q) be simple with
n≥ 2, 3, 4 respectively. Then there exist nontrivial χ1,χ 2,χ 3∈ Irr3′(B0(S))σ1 that are pairwise not
Aut(S)-conjugate and such thatχ1 is invariant under Aut(S).
Proof. We may again assume S is not one of the groups in Proposition 3.8. Let δ∈ F×
q2 with|δ|= 4, and
we keep the notation from Section 3A. Let 8 and1:={α1,α 2,...,α n} be a system of roots and simple
roots, respectively, for˜G∗ with respect to a maximal torus ˜T∗, following the standard model described in
[Gorenstein et al. 2002, Remark 1.8.8]. Then8 is type Bn, Cn, or Dn in the caseS=PSp2n(q), P2n+1(q),
or P±
2n(q), respectively. Further,8 has no nontrivial graph automorphism unless we are in the case of
Dn, in which case all members of1 have the same length and that automorphism has order 2 unless n= 4.
We use the notation as in [Gorenstein et al. 2002] for the Chevalley generators. In particular, givenα∈8,
let hα denote the corresponding coroot. Let K:=[˜G∗,˜G∗], so we have hα(t)∈ K for t∈ F×
q by [loc. cit.,
Theorem 1.10.1(a)] and ˜G∗= K.Z(˜G∗). Notice that for s, s′∈ K (not necessarily distinct), we have s is
˜G∗-conjugate to s′z for z∈ Z(˜G∗) if and only if z∈ Z(K) and the conjugating element can be chosen in K.
By [Gorenstein et al. 2002, Theorem 1.12.4] and [Cabanes and Enguehard 2004, 15.1], K is isomorphic
as an abstract group to the simply connected simple algebraic group (˜G∗)sc associated to ˜G∗, and the
Chevalley relations and generators of(˜G∗)sc and K may be identiﬁed. We will make this identiﬁcation.
In particular, choosing s1, s2, and s3 in K, the properties (1)–(3) may be veriﬁed by computation in K
rather than ˜G∗.
Let T denote a maximal torus of K under this identiﬁcation, and note that
T=⟨ hα(t)| t∈ F×
q,α∈8⟩ and NK(T)=⟨ T, nα(1)|α∈8⟩.
Further, note that
W:= N˜G∗(˜T∗)/˜T∗∼= NK(T)/T.
By [Digne and Michel 1991, Corollary 0.12], we know that NK(T) controls fusion in T, so two elements
of T are conjugate if and only if there is a conjugating element in W. Further, we have an isomorphism
(F×
q)n→ T given by(t1,..., tn)↦→∏n
i=1 hαi(ti).
Now using the standard model for 8 and1 as in [Gorenstein et al. 2002], since 8 is type Bn, Cn,
or Dn, we have αi:= ei− ei+1 for 1≤ i≤ n− 1, where{e1,..., en} is an orthonormal basis for the
n-dimensional Euclidean space. Here W≤ C2≀ Sn where the generators of the base subgroup Cn
2 act
via negation on the ei and the copy of Sn permutes the ei.
Galois action on the principal block and cyclic Sylow subgroups 1977
Using this information and the description of Z(K) in [Gorenstein et al. 2002, Table 1.12.6], compu-
tation with the Chevalley relations yields that the element s′
1:= hα1(δ) is not ˜G∗-conjugate to s′
1z for any
1⁄= z∈ Z(˜G∗). Ifδ∈ F×
q , we see that s′
1 is F∗-ﬁxed, and we write s1:= s′
