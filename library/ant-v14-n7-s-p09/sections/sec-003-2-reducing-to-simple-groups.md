---
doc_id: ant-v14-n7-s-p09
doc_title: "Galois action on the principal block and cyclic Sylow subgroups"
section_id: sec-003-2-reducing-to-simple-groups
section_title: "Reducing to simple groups"
section_number: 2
pages: 8-10
source_pdf: ant-v14-n7-s-p09.pdf
source_sha256: c8fe963200a79d25
doc_brief: "Galois action on the principal block and cyclic Sylow subgroups — 8 sections: Introduction; Blocks with normal defect group; Suppose that|D|= 2n. Since G/CD ac"
---
The aim of this section is to reduce the statement of Theorem A to a problem on simple groups that we
will solve in Section 3.
2A. Preliminaries. We start these preliminaries with results concerning the action of Galois automor-
phisms on characters belonging to principal blocks. Recall that χ∈ Irr(B0(G)) if, and only if,
∑
x∈G0
χ( x)⁄= 0,
where G0 is the subset of elements of G of order not divisible by p. Some properties of characters in the
principal block are listed below.
Lemma 2.1. Let G be a ﬁnite group, and let N◁ G.
(a) We have that Irr(B0(G/N))⊆ Irr(B0(G)), with equality whenever N is a p′-group.
(b) If Hi are ﬁnite groups andγi∈ Irr(B0(Hi)), for i= 1,..., t, thenγ1×···× γt∈ Irr(B0(H1×···× Ht)).
Proof. The ﬁrst part of (a) and (b) follow directly from the deﬁnition of principal block [Navarro 1998,
Deﬁnition 3.1]. The second part of (a) is [loc. cit., Theorem 9.9.(c)]. □
We summarize below some results obtained in Section 1, here stated with respect to the principal block.
The ﬁrst part was ﬁrst observed by G. Navarro (in private communication).
Lemma 2.2. Let G be a ﬁnite group and let P be a Sylow p-subgroup of G.
(a) If P is normal in G , then Irrp′(B0(G))σ1= Irr(G/Op′(G)8(P)).
(b) If P is cyclic , then 1≤| Irrp′(B0(G))σ1|≤ p.
(c) If P is nontrivial and p∈{ 2, 3}, then|Irrp′(B0(G))σ1|⁄= 0 is divisible by p.
Galois action on the principal block and cyclic Sylow subgroups 1961
Proof. To prove part (a), assume that P◁ G. Then G is p-solvable and by Fong’s theorem [Navarro 1998,
Theorem 10.20] Irr(B0(G))= Irr(G/Op′(G)). Hence we may assume that Op′(G)= 1 and, in particular,
CG(P)⊆ P. By Lemma 1.2
Irrp′(B0(G))σ1= Irrp′(G)σ1=
⋃
λ∈Irr(P/8( P))
Irr(G|λ)= Irr(G/8( P)).
Part (b) is a straightforward application of Lemma 1.3. Part (c) is a direct consequence of Lemma 1.4. □
Next is a classical result by J. L. Alperin and E. C. Dade.
Theorem 2.3. Suppose that N is a normal subgroup of G and G/N is a p′-group. Let P∈ Sylp(G) and
assume that G= N CG(P). Then restriction of characters deﬁnes a bijection Irr(B0(G))→ Irr(B0(N)).
In particular,|Irrp′(B0(G))σ1|=| Irrp′(B0(N))σ1|.
Proof. The case where G/N is solvable was proved in [Alperin 1976, Lemma 1.1]. The general case in
the main result of [Dade 1977]. The latter statement follows since σ1 acts on Irr p′(B0(G)). □
We will also use the following.
Lemma 2.4. Suppose that G is a ﬁnite group, P∈ Sylp(G) and P CG(P)≤ H≤ G. Ifθ∈ Irrp′(B0(H))σ1,
then there exists a someχ∈ Irrp′(B0(G))σ1 lying overθ.
Proof. Note that B0(H)G= B0(G) by the comments before [Navarro 1998, Theorem 9.24] and Brauer’s
third main theorem [loc. cit., Theorem 6.7]. Write
9=
∑
χ∈Irr(B0(G))
[θ G,χ]χ,
so that9 has p′-degree by [loc. cit., Theorem 6.4]. (Note that9 is exactly(θ G)B where B= B0(G) in the
notation of [loc. cit.].) Let A=⟨σ1⟩, where here we viewσ1 as an element of Gal(Q(ξ)/ Q) for o(ξ)=| G|.
For every a∈ A we have that9a=9 as A acts on Irr(B0(G)) and ﬁxesθ. By [Navarro and Tiep 2019,
Lemma 2.1(ii)] there is some χ∈ Irrp′(G)σ1 appearing with p′-multiplicity in9. The statement now
follows since every irreducible constituent of 9 lies in the principal block and its multiplicity in 9 is
exactly the multiplicity ofθ in its restriction to H. □
We end the preliminaries with a technical result.
Lemma 2.5. Let G be a ﬁnite group and let N◁ G be a direct product of t copies of a simple nonabelian
group S transitively permuted by G. Let P∈ Sylp(G). If some 1S⁄=φ∈ Irrp′(B0(S))σ1 is X-invariant,
where X∈ Sylp(Aut(S)), then there exists some P-invariant 1N⁄=θ∈ Irrp′(B0(N))σ1. In particular, if N
is a minimal normal subgroup of G, thenθ extends to aσ1-invariant irreducible character of PN.
Proof. Let 1N⁄=θ∈ Irr(N) the character of N corresponding to φ×···× φ∈ Irrp′(B0(S)t)σ1, then
θ∈ Irrp′(B0(N))σ1 by Lemma 2.1(b). By [Navarro et al. 2007, Lemma 4.1(ii)], we may assume that θ is
P-invariant.
For the second part of the statement, notice that since PN/N is a p-group and N is perfect,θ has a
canonical extensionˆθ∈ Irrp′(PN) by [Isaacs 1976, Corollary 6.28]. In particular, ˆθ isσ1-invariant. □
1962 Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
