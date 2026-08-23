---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-019-34-independence-of-a-choice-of-meridian-path
section_title: "Independence of a choice of meridian path"
section_number: 3.4
pages: 18-19
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
M induces a triangulation of its boundary torus ∂M . Consider two simple closed meridian
loops in∂M in general (normal) position with respect to the triangulation of ∂M . Recall that
these paths are drawn on the triangulated 2-dimensional torus ∂M where faces of tetrahedra
correspond to edges in the 2-dimensional triangulation, and edges of tetrahedra to vertices.
In particular, for a one-cusped manifold M, every edge of the triangulation intersects a pair
of vertices on the boundary ∂M .
z
z′
z′′ 
w
w ′ w ′′ 
z
z′
z′′ 
w
w ′ w ′′ 
r1
rj
s1s2
sj′
r1
rj
s1s2
sj′
Figure 6. The fundamental move for changing a meridian path. Here, we
deform through an edge EI with gluing constraint XI = Z +W +R1 +... +
Rj +S1 +... +Sj′ = 2πi.
We can deform one of our meridian paths into the other by using repe ated applications of
the fundamental move shown in Figure 6 — locally pushing a section of the path across a
vertex of ∂M . Thus, it suﬃces to assume that the two paths only diﬀer by one suc h move.
Suppose that we cross the I th edge (by Section 3.3 we may assume that I⁄=N), which has
a combinatorial gluing constraint
(3.13) XI :=
N∑
i=1
(
GIiZi + G′
IiZ ′
i + G′′
IiZ ′′
i
)
= 2πi,
and that the two tetrahedra where the paths enter and exit the v icinity of the edge have
parameters (Z,Z ′,Z ′′) and (W,W ′,W ′′), as in the ﬁgure. We do not exclude the possibility
that (Z,Z ′,Z ′′) and ( W,W ′,W ′′) both coincide with the same triple ( Zi,Z ′
i,Z ′′
i ), in some
cyclic permutation. Then the diﬀerence in the logarithmic meridian equ ations (
2.5) for the
two paths will be
(3.14) δµ =±
(
XI− (Z +Z ′ +Z ′′)− (W +W ′ +W ′′)
)
.
Note that two logarithmic meridian constraints that diﬀer by (
3.14) are compatible and
equivalent, since upon using the additional equations XI = 2πi and Z +Z ′ +Z ′′ = W +
W ′ +W ′′ =iπ, we ﬁnd that δµ = 0. A discretized version of this observation demonstrates
that that the same ﬂattening satisﬁes both discretized meridian co nstraints.2
2Note that this would not be the case if we allowed self-intersections o f the meridian loops.
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 19
If we compute matrices A, B using one meridian path and ~A, ~B using the other — keeping
quad type, ﬂattening, and edge the same — the change ( 3.14) implies that
(3.15) ~A =P (µ )
I
±1A, ~B =P (µ )
I
±1B,
where P (µ )
I is the SL(N, Z) matrix
(3.16) P (µ )
I =I +EN I,
i.e. the identity plus an extra entry ‘1’ in the N th (meridian) row and I th column. Since
detP (µ )
I = 1, this immediately shows that det
(~A∆ z′′ +~B∆ −1
z
)
= det
(
A∆ z′′ + B∆ −1
z
)
, and
so the a change in the meridian path cannot aﬀect τT .
3.5. Independence of a choice of ﬂattening. Now suppose that we choose two ﬂattenings
(f,f ′,f ′′) and ( ~f, ~f ′,~f ′′), both satisfying
(3.17) Af + Bf ′′ =ν, f +f ′ +f ′′ = 1.
(3.18) A~f + B~f ′′ =ν, ~f + ~f ′ + ~f ′′ = 1.
We may assume that we have a quad type with B non-degenerate. Indeed, by the result of
Section 3.2, ﬂattening invariance in one quad type implies ﬂattening invariance in a ny quad
type. Moreover, by Lemma A.3 of Appendix A, a quad type with non-degenerate B always
exists. We also note that when B is invertible the matrix B−1A is symmetric (Lemma A.2).
The determinant in τT is insensitive to the change of ﬂattening. The monomial, on the
other hand, can be manipulated as follows. Let us choose logarithms (Z,Z ′,Z ′′) of the shape
parameters such that AZ + BZ ′′ = iπν. Then, assuming that B is non-degenerate, we
compute:
z ˜f ′′
z′′− ˜f
zf ′′
z′′−f = exp
[
Z· (f ′′− ~f ′′)−Z ′′· (f− ~f )
]
= exp
[
−Z· B−1A(f− ~f )− (iπB−1ν− B−1AZ)· (f− ~f )
]
= exp
[
−iπB−1ν· (f− ~f )
]
= exp
[
−iπf ′′· (f− ~f )−iπB−1Af· (f− ~f )
]
= exp
[
−iπf ′′· (f− ~f ) +iπf· (f ′′− ~f ′′)
]
= exp
[
iπ(f ′′· ~f−f· ~f ′′)
]
=±1.
Therefore, the monomial can change at most by a sign, and τT is invariant as desired.
This completes the proof of Theorem 1.3. □
