---
doc_id: arxiv-math-0605314v1
doc_title: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO"
section_id: sec-062-91-the-twist-element-ω-ˆp-deﬁne-two-elements-ωω
section_title: "The twist element ω∈ ˆP. Deﬁne two elements ω+,ω −∈ ˆP by"
section_number: 9.1
pages: 33-34
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the"
---
ω± =
∞∑
n=0
(±1)nv± 1
2 n(n+3)P ′
n.
SetSQ(v) =S⊗ Z[q,q−1] Q(v)⊂R Q(v). By Proposition 6.6, the bilinear map
⟨,⟩: P×S Q(v)→ Q(v) induces a bilinear map
⟨,⟩: ˆP×S Q(v)→ Q(v).
Proposition 9.1. For each x∈S Q(v), we have
⟨ω±,x⟩=JU±(x),(9.1)
whereU± is a ±1-framed unknot.
Proof. We may assume x = V′
2k = V2k/[2k + 1], k≥ 0, without loss of generality.
By (6.10), we have
⟨ω±, V′
2k⟩=
∑
n≥0
(±1)nv± 1
2 n(n+3)⟨P ′
n, V′
2k⟩=
k∑
n=0
(±1)nv± 1
2 n(n+3){k +n}2n
{n}! .(9.2)
Since V2k is an irreducible Uh-module, we have r∓1v2k
i = JU±(V′
2k)v2k
i for all
i = 0,... , 2k. (Recall that r∈ Uh denotes the ribbon element, and v2k
i for i =
0,... , 2k denote the basis elements of the irreducible left Uh-module V2k.) Consider
the case i =k. By straightforward calculations using (3.8) and (3.9), we obtain
r∓1v2k
k =
k∑
n=0
(±1)nv± 1
2 n(n+3){k +n}2n
{n}! v2k
k .
Hence, JU±(V′
2k) is equal to the right-hand side of (9.2). Hence, we have (9.1 ) for
x = V′
2k.
Proposition 9.2. ω+ and ω− are inverse to each other in the algebra ˆP.
Proof. A direct proof using (8.1) is possible. Here we give another p roof.
By Proposition 9.1 and the fact that ⟨−, V′
2p⟩: SQ(v)→ Q(v) is a Q(v)-algebra
homomorphism, we have
⟨ω+ω−, V′
2p⟩=⟨ω+, V′
2p⟩⟨ω−, V′
2p⟩=qp(p+1)q−p(p+1) = 1 =⟨1, V′
2p⟩
for each p≥ 0. Hence, we have ⟨ω+ω−,x⟩=⟨1,x⟩for all x∈S Q(v). Since the map
ˆP→ Fun(SQ(v), Q(v)), x ↦→(y↦→⟨x,y⟩),
is injective (by Proposition 6.6), it follows that ω+ω− = 1. (Here Fun(SQ(v), Q(v))
denotes the set of functions on SQ(v) with values in Q(v).)
Set ω =ω+. We have ω− =ω−1.
Remark 9.3. The twist element ω was announced ﬁrst in [16] in a formulation using
skein theory, and then in [17] in the present form (without pr oofs). Later, Masbaum
[58] gave a proof using skein theory.
34 KAZUO HABIRO
...
...
......
Lir
K K= ∑
...Li1
e
Figure 9.1. A fusing identity.
9.2. Twisting theorem.
Theorem 9.4. LetL1∪···∪ Lm∪K be an (m + 1)-component, algebraically-split,
0-framed link such that K is an unknot. Set L = L1∪···∪ Lm, and let L(K,±1)
denote the framed link in S3 obtained fromL by±1-framed surgery along K. Then,
for any x1,... ,x m∈ ˆP, we have
JL∪K(x1,... ,x m,ω ∓1) = JL(K, ±1)(x1,... ,x m).(9.3)
Proof. By Theorem 8.2, it suﬃces to prove (9.3) for x1,... ,x m∈P . In fact, we
will show (9.3) for x1,... ,x m∈R Q(v). (Well-deﬁnedness of the left-hand side of
(9.3) in this case follows from the argument below.) Apply th e standard “fusing”
argument to the strands running through the unknot K, see Figure 9.1. In the left-
hand side, the strands running through K are paired in such a way that each pair
contains two segments from the same component of L in the opposite orientations.
By fusing these strands, we obtain a linear combination of tr ivalent colored graphs,
where each term has exactly one edge e running through K, colored by an even
number. Hence, there is y∈S Q(v) such that
JL∪K(x1,... ,x m,ω ∓1) = JH (y,ω ∓1) =⟨ω∓1,y⟩,
whereH denotes the Hopf link with 0-framings. By Proposition 9.1, t he right-hand
side is equal to JU∓ (y), where U∓ denotes the∓1-framed unknot. Since we have
JU∓(y) = JL(K, ±1)(x1,... ,x m),
we have (9.3).
