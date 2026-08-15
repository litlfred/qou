---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-154-2b-the-reduction
section_title: "2B. The reduction"
section_number: null
pages: 296-297
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
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
