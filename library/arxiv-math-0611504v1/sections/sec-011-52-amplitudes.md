---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-011-52-amplitudes
section_title: "Amplitudes"
section_number: 5.2
pages: 24-26
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
doc_brief: "Quantum hyperbolic geometry STEPHANE BASEILHAC RICCARDO BENEDETTI — 19 sections: Introduction; Universal QHG; Building blocks"
duplicate_of: "agt-v7-n2-p13-s"
---
V −1 for the dual space. Both are endowed with the hermitian inner prod uct with orthonormal basis
the vectors e0 and (ei +eN −i)/
√
2, i = 1,...,N − 1.
Recall the notations of section 3. For each base surface F ﬁx an e-triangulation (T,b ), an or-
dering of the set T (2) of 2-simplices, and let V (T,b ) = ⊗t∈T (2)Vσ±(t). Given a QHFT bordism
B = ( ˜Y, ˜LF,ρ,α ±) with a distinguished ﬂat/charged I-triangulation T (B), the trace tensor in (11)
is a morphism HN (T (B)) ∈ Hom(V (α−),V (α+)), where V (α±) is the tensor product of isomorphic
copies of the spaces V (T,b ) over the (ordered) components of α±.
Theorem 5.4. The morphism HN (B,h,k ) = HN (T (B)) does not depend on the choice of T (B) up
to sign and multiplication by N th roots of unity, and HN (B,h,k ) = HN (B,h ′,k ′) if the mod( N Z)
reductions of h and h′ (resp. k and k′) are the same, that is, if we have k −k′ ∈ H 1( ˜LF ; Z) and
k −k′ = 0 ∈ H 1( ˜LF ; Z/NZ), and similarly for h and h′. Moreover, there is no sign ambiguity if
we restrict to even valued ﬂattenings as in Lemma 2.9 (hence w ith h = 0 ). We call HN (B,h,k ) the
amplitude of (B,h,k ).
Proof. The result up to sign is an immediate consequence of Proposition 2.5 an d the last claim in
Theorem 5.3. For the dependance with respect to the mod( N Z) reductions of weights, we note that
the associated systems of N th roots of moduli (see Remark 2.11) are connected by QHG isomorp hisms.
Indeed, the diﬀerence k −k′ ∈H 1( ˜LF ;N Z) coincides with γ(f ) −γ(f ′)/
√
−1π andγ(c) −γ(c′)/
√
−1π
for some f , f ′ and c, c′, and similarly for h −h′ and the γ2 maps. By ﬁrst considering ( k −k′)/N
we can eventually take the collections of values of f −f ′ and c −c′ in N Z, and equal. Hence the
conclusion follows from (5) and (6). For even valued ﬂattenings, th e claim follows from the fact that
Proposition 2.5 has no sign ambiguity. For clarity let us state the resu lt with some details.
Consider all the possible branching conﬁgurations of 2 ↔ 3 QHG transits, up to obvious symmetries.
They are obtained from a single one by composing with the transposit ions (01), (12), (23) and (34)
of the vertices (ordered in accordance with the branching). Any s uch a transposition changes the
matrix dilogarithm of each tetrahedron by matrix conjugation and m ultiplication by a determined
scalar factor (see Corollary 5.6 of [5]). Now, there is a prefered “b asic” 2 ↔ 3 QHG transit, for which
even ﬂattenings give no sign ambiguity in Proposition 2.5 (see the proof of T heorem 5.7 in [5]). The
corresponding branching conﬁguration is deﬁned by ordering the v ertices as 1 and 3 on the bottom
and top of the central edge, and 0, 2, 4 counterclockwise as viewe d from the 3rd vertex. The following
QUANTUM HYPERBOLIC GEOMETRY 25
table describes for each tetrahedron ∆ i, opposite to the i-th vertex, the scalar factors induced by the
above transpositions (we put v = exp(
√
−1π(1 −N )/2N ), which is −ζ−(m+1)(1−N )/2 in the notations
of [5], and the cl
k are charge values):
∆ 1 ∆ 3 ∆ 0 ∆ 2 ∆ 4
(01) 0 vc3
0
0 vc2
0
vc4
0
(12) 0 vc3
1
vc0
0
0 vc4
1
(23) vc1
1
0 vc0
1
0 vc4
0
(34) vc1
0
0 vc0
0
vc2
0
0
Because of (8), we see that the scalars at both sides are equal. He nce, for any 2 ↔ 3 log-branch transit
with even ﬂattenings, the only ambiguity in Proposition (2.5) is by multip lication by N th roots of
unity, which is due to the deﬁnition of the function g in (4). The conclusion follows as before by
using QHG-isomorphisms preserving the parity of ﬂattenings (when ce based on even multiples of the
generators of ﬂat/charge lattices). ✷
Remark 5.5. (Cheeger-Chern-Simons invariants and H1.) By the results of [25], there is an injective
homomorphism from H3(PSL (2, C); Z) (discrete homology) to a scissors congruence group ˆP(C),
such that the dilogarithm (3), deﬁned on ˆP(C), restricts to the universal Cheeger-Chern-Simons class
ˆC2 : H3(PSL (2, C); Z) → C/π2Z. Hence H1 is a natural extension of exp( ˆC2/iπ), the exponential
of a constant times Vol + iCS , to classes representing QHFT bordisms. Recently J. Dupont and C .
Zickert produced dilogarithmic formulas for the lift ˆC′
2 of ˆC2 toH3(SL(2, C); Z), such that exp( ˆC′
2/iπ)
coincides with the lift of H1 determined by even ﬂattenings in Theorem 5.4 [13]. We are indebted to
their work for pointing out the existence of such ﬂattenings.
Recall Deﬁnition 4.3. Assume that B′′ = B′ ∗ B exists, and let T (B) and T (B′) be given weights ( h,k )
and (h′,k ′), respectively. Then T (B′) ∗ T (B) is a distinguished ﬂat/charged I-triangulation T (B′′),
with some weight (h′′,k ′′). (It follows from the Mayer-Vietoris exact sequence for ( B′′, B′, B) that even
ifh =h′ = 0, it can happen that h′′ ⁄= 0. However, if the glued part of the boundary is connected, or
is a boundary in B ∗ B ′, then h =h′ = 0 implies h′′ = 0.)
Proposition 5.6. (Functoriality) For any composition B′′ = B′ ∗ B of bordisms, HN (B′′,h ′′,k ′′)
coincides with HN (B′,h ′,k ′) ◦ HN (B,h,k ) up to sign and multiplication by N th roots of unity.
This is a direct consequence of Theorem 5.4. Also, we prove as in Prop osition 4.29 of [5]:
Proposition 5.7. (Polarity) Write ¯B for the QHFT bordism with opposite orientation and complex
conjugate holonomy ¯ρ. Then HN ( ¯B, −h, −k) and HN (B,h,k )∗, the adjoint for the hermitian structure
of V (α±), coincide up to sign and multiplication by N th roots of unity.
In the proof of Theorem 5.3 we have seen that the space ˜W +(T,b ) of (+)-Log- I-parameters over
W +(T,b ) (the disjoint union of spaces W +(T,b, C)) is isomorphic to ˜C−3χ(F )+2p, where ˜C is the
universal cover of C \ {0}. Similarly, for any admissible triangulation τ of a topological cusp with n
2-simplices, we have the analytic subspace Def (τ ) of ˆCn made of the n-uples of log-branches for the
tetrahedra of I-cusps with base triangulation τ , where ˆC is deﬁned in Section 2.1. Such log-branches
satisfy the compatibility relations LT (e) = 0 at interior edges.
Deﬁnition 5.8. LetX = (Y,L F,α ±) be a marked topological bordism with e-triangulated or admis-
sibly triangulated boundary components. The phase space of X is the (analytic) subset Def (X) in
the product of the spaces ˜W +(T,b ) and Def (τ ) over the components of ∂ ˜Y andL, determined by the
family of distinguished ﬂat/charged I-triangulations of QHFT bordisms supported by ( Y,L F,α ±).
26 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
When Y has empty boundary, Def (X) is a generalization of the well known deformation space of
hyperbolic structures supported by ideal triangulations of Y \L, introduced in [29], and recently
studied in [11] and [12]. When ˜Y is the mapping cylinder of a diﬀeomorphism φ ofF , the amplitudes
of QHFT bordisms supported by ˜Y deﬁne a morphism of the trivial vector bundle
(18) E(F )+ =E(T,b )+ : ˜W +(T,b ) ×V (T,b ) → ˜W +(T,b ).
(Note that any two choices of e-triangulations (T1,b 1) and ( T2,b 2) of F yield isomorphic bundles
E(T1,b 1) and E(T2,b 2), with birationally equivalent bases.) The resulting mapping of section s of
E(F ), the states of F , are studied in [3].
Proposition 5.9. (Analyticity) For everyN ≥ 1, the amplitudes of QHFT bordisms supported by X =
(Y,L F,α ±) vary analytically with the boundary structure in Def (X), up to sign and multiplication by
N th roots of unity.
This follows immediately from the fact that the matrix dilogarithms are analytic, together with the
fact that any path in Def (X) lifts to a path of log-branches via the relations induced by Deﬁnition
5.2 (4).
