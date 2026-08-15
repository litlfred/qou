---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-026-81-generic-decorations-ptolemy-coordinates-and-s
section_title: "Generic decorations, Ptolemy coordinates and shapes"
section_number: 8.1
pages: 26-28
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
GL(n, C), let{g}i denote the ordered set consisting of the ﬁrst i column vectors of g.
Deﬁnition 8.6. A GL(n, C)/N-decoration (g0N,g 1N,g 2N,g 3N) on ∆3
n is generic if for each
(t0,t 1,t 2,t 3)∈ ∆3
n(Z)
(8.1) det
(
{g0}t0∪{g1}t1∪{g2}t2∪{g3}t3
)
⁄= 0.
Genericity of PGL(n, C)/B-decorations is deﬁned similarly.
The deﬁnition is obviously independent of the choice of coset representatives, and of the
ordering of the tuple.
Remark 8.7. Although all representations can be decorated, some representations may
only have non-generic decorations. However, after a single barycentric subdivision, every
representation has a generic decoration. For SL( n, C)/N-decorations this is proved in [11,
Prop. 5.4], and the proof for PGL( n, C)/B-decorations is similar. This proves the last
statement of Theorem 1.2.
Lemma 8.8 (Fock-Goncharov [8, Lemma 10.3]; see also [11]) . A generic GL( n, C)/N-
decoration (g0N,g 1N,g 2N,g 3N) of ∆ 3
n induces a Ptolemy assignment
(8.2) c: ˙∆3
n(Z)→ C∗, t ↦→ det ({g0}t0∪{g1}t1∪{g2}t2∪{g3}t3).
□
Corollary 8.9. We have a map
(8.3) C :{Generic GL(n, C)/N-decorations on ∆ 3
n}→{ Ptolemy assignments on ∆ 3
n}.
□
Note thatC is invariant under the left action by SL(N, C).
Lemma 8.10. The mapC is compatible with pullbacks, i.e.,
(8.4) σ∗(C(g0N,g 1N,g 2N,g 3N) =C(gσ(0)N,gσ(1)N,gσ(2)N,gσ(3)N).
Proof. Let c =C(g0N,g 1N,g 2N,g 3N) and c′ =C(gσ(0)N,gσ(1)N,gσ(2)N,gσ(3)N). Then
(8.5) cσ(t) = det
( 3⋃
i=0
{gi}tσ−1(i)
)
, c ′
t = det
( 3⋃
i=0
{gσ(i)}ti
)
.
One easily checks that
(8.6)
( 3⋃
i=0
{gi}tσ−1(i)
)
Iσ,σ(t) =
3⋃
i=0
{gσ(i)}ti,
from which it follows that (σ∗c)t =cσ(t) det(Iσ,σ(t)) =c′
t. This proves the result. □
Corollary 8.11. A generic SL(n, C)/N-decoration on (M,T ) induces a Ptolemy assignment
on (M,T ).
Proof. We only need to show that Ptolemy coordinates are identiﬁed via the pullback. This
follows from Lemma 8.10. □
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 27
Remark 8.12. A GL(N, C)/N-decoration does not induce a Ptolemy assignment on (M,T ).
Forg∈ GL(N, C), let ¯g denote the image of g in PGL(N, C).
Proposition 8.13. We have a well deﬁned map
(8.7) Z :{PGL(n, C)/B-decorations on ∆ 3
n}→{ shape assignments on ∆ 3
n},
(¯g0B, ¯g1B, ¯g2B, ¯g3B)↦→µ◦C (g0N,g 1N,g 2N,g 3N),
which is invariant under the left PGL(n, C)-action and compatible with pullbacks.
Proof. Let c =C(g0N,g 1N,g 2N,g 3N). To prove thatZ is well deﬁned, we must prove that
(8.8) µ(c) =µ(c′), with c′ =C(g0d0N,...,g 3d3N),
wheredi =d(λi
1,...,λ i
n) are diagonal matrices. We prove that µ(c)1100
s =µ(c′)1100
s , the other
cases being similar. Using (8.1) we have
(8.9) µ(c′)1100
s = c′
s+1001c′
s+0110
c′
s+1010c′
s+0101
, c ′
t = det(
⋃
{gidi}ti) =
( 3∏
j=0
ti∏
i=1
λj
i
)
ct.
Expanding each term, we obtain
(8.10)
c′
s+1001 =
( 3∏
j=0
si∏
i=1
λj
i
)
λ0
s0+1λ3
s3+1cs+1001, c ′
s+0110 =
( 3∏
j=0
si∏
i=1
λj
i
)
λ1
s1+1λ2
s2+1cs+0110
c′
s+1010 =
( 3∏
j=0
si∏
i=1
λj
i
)
λ0
s0+1λ2
s2+1cs+1010, c ′
s+0101 =
( 3∏
j=0
si∏
i=1
λj
i
)
λ1
s1+1λ3
s3+1cs+0101.
It now easily follows that
(8.11) µ(c′)1100
s = c′
s+1001c′
s+0110
c′
s+1010c′
s+0101
= cs+1001cs+0110
cs+1010cs+0101
=µ(c)1100
s
as desired. Invariance under left multiplication follows from the fact that det( ∪{ggi}ti) =
det(g) det(∪{gi}ti), and compatibility with pullbacks follows from the fact that both µ and
C enjoy this property. □
Corollary 8.14. A generic PGL(n, C)/B-decoration on (M,T ) induces a shape assignment
on (M,T ).
Proof. By Proposition 8.13, we have a shape assignment on each simplex, and we must
prove that these satisfy the generalized gluing equations. We proceed as in the proof of
Theorem 6.3. Let K be the local model of an edge point as deﬁned in Section 6.1. We can
pullback the decoration on T to a decoration on K using the simplical map π. Since K is
simply connected, we can change the decoration of each simplex by left multiplication by an
element in PGL(n, C) such that vertices of simplices that get identiﬁed in K carry the same
coset. This does not aﬀect the shapes. For each vertex in K decorated by gB we pick a lift
˜gN and applyC to get a Ptolemy assignment on K. By Lemma 6.5 the shapes satisfy the
edge equations. The result for the face, and interior gluing equations is similar. □
28 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
