---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-007-44-negative-tripartite-information
section_title: "Negative tripartite information"
section_number: 4.4
pages: 21-23
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
A useful characterization of multipartite entanglement is the tripartite information,
deﬁned as
I3(A,B,C )≡SA +SB +SC−SAB−SAC−SBC +SABC. (4.13)
For a general (mixed) tripartite quantum state, I3 can take any real value. It is zero,
though, for any tripartite pure state of ABC, since in that case SABC = 0 and e.g.
regions A and BC, being complementary, have the same entropy and therefore make
cancelling contributions to I3. Nor is there a contribution to I3 from EPR pairs shared
between a pair of the three regions (because e.g. a pair shared by AB yields positive
contributions to SA and SB which are cancelled by negative contributions from −SAC
and−SBC) or from entanglement shared between one of the three regions and a fourth
disjoint region. Thus, for a holographic state and for any partition of the boundary
into four regions A,B,C,D, nonzero contributions to I3(A,B,C ) can arise only from
the distilled multipartite states trapped in residual regions.
In the holographic setting, it has been shown that I3≤ 0 follows from the RT
formula [9]. For holographic states and codes, the non-positivity of I3 is not ensured in
general, because of the potential (small) violations of the RT formula. In some special
cases, though, RT holds exactly, and the non-positivity ofI3 then follows. For example,
suppose that we partition the boundary into four connected regionsA,B,C,D , and that
each connected component of the multipartite residual region traps just one perfect
tensor. In that case there is no bipartite residual region, so Theorem 3 implies that RT
is exact and therefore I3≤ 0. To see that there is no bipartite residual region in this
case, consider the bipartite partition of the boundary into the two disconnected regions
AC and BD, and consider an isolated 2 n-index perfect tensor surrounded by three or
– 19 –
all four of the greedy geodesics γ⋆
A,γ⋆
B,γ⋆
C,γ⋆
D. This tensor must have at least n legs
crossing either γ⋆
A∪γ⋆
C or γ⋆
B∪γ⋆
D. Therefore, when we apply the greedy algorithm to
the boundary regions AC andBD, one cut or the other will advance past this isolated
tensor, excluding it from the bipartite residual region.
Under suitable conditions we can actually prove a stronger result — that I3 is
strictly negative. Let us say that a connected component of the multipartite residual
region is three sided if surrounded by three of the four greedy geodesics, and four
sided if surrounded by all four greedy geodesics. Three-sided components make no
contribution to I3; if the three surrounding greedy geodesics are those of X,Y,Z , the
symmetry of I3 implies I3(A,B,C ) =I3(X,Y,Z ), which vanishes for any pure state of
XYZ . But an isolated 2 n-index perfect tensor which crosses all four greedy geodesics
makes a negative contribution to I3:
Theorem 4. Suppose the 2n indices of a perfect tensor state are partitioned into four
disjoint nonempty sets A,B,C,D such that 0<|A|,|B|,|C|,|D|<n . Then the tripar-
tite information I3 is strictly negative: I3(A,B,C )< 0.
Proof. First we notice that for a four-part pure stateABCD , the tripartite information
I(A,B,C ) is actually completely symmetric under permutations of the four subsystems,
which we can see by using the property that complementary regions have the same
entropy in a pure state:
I3(A,B,C ) =SA +SB +SC−SAB−SBC−SAC +SABC (4.14)
=SA +SB +SC +SD− 1
2(SAB +SCD +SBC +SAD +SAC +SBD).
(4.15)
We may therefore assume without loss of generality that |A|≤| B|≤| C|≤| D| which
implies|AB|≤| CD| and|AC|≤| BD|. Now we use the deﬁning property of 2 n-
index perfect tensors, that a set of n or fewer indices is maximally entangled with
its complement, which implies SX = min(|X|, 2n−|X|), with entropy expressed in
units of log v. Therefore SA =|A|,SB =|B|,SC =|C|,SD =|D|, and furthermore
SAB =|AB| and SAC =|AC|. Now we distinguish two cases. If |AD|≤| BC|, then
SBC =SAD =|AD| and we have
I3(A,B,C ) =|A| +|B| +|C| +|D|−| AB|−| AC|−| AD| =−2|A|< 0. (4.16)
If on the other hand |BC|≤| AD|, then SAD =SBC =|BC| and we have
I3(A,B,C ) =|A| +|B| +|C| +|D|−| AB|−| AC|−| BC| = 2|D|− 2n< 0, (4.17)
– 20 –
where to obtain the second equality we use|AB| +|AC| +|BC| = 2(|A| +|B| +|C|) =
2(2n−|D|). This completes the proof.
For a holographic state with boundary partitioned into sets A,B,C,D , the condi-
tions of Theorem 4 are satisﬁed by an isolated perfect tensor trapped inside a four-sided
component of the multipartite residual region; fewer than n of the tensor’s legs cross
any greedy geodesic, because otherwise the greedy algorithm would have moved the
cut forward past this perfect tensor, which therefore would not be in the multipartite
residual region. Furthermore, since entropy is additive for a product state, I3 is also
strictly negative for any product of perfect tensor states shared byA,B,C,D , provided
that at least one factor has support on all four sets. Since only the four-sided regions
contribute to I3, we conclude that I3 is strictly negative if the multipartite residual
region contains at least one four-sided connected component, and if each four-sided
connected component contains only one perfect tensor.
