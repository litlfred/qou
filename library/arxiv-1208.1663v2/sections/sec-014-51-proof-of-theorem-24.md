---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-014-51-proof-of-theorem-24
section_title: "Proof of Theorem 2.4"
section_number: 5.1
pages: 14-16
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
known lemma due to Farkas [30].
Lemma 5.1. Fix ﬁnite collections A = {a1, . . . , ar} and B = {b1, . . . , bs} of vectors in RN.
The following are equivalent:
(a) there does not exist v̸ = 0 such that ai · v ≥0 for i = 1, . . . , r and bj · v = 0 for
j = 1, . . . , s.
(b) A ∪B span RN and there exist αi > 0 for i = 1, . . . , r and γj ∈R for j = 1, . . . , s
such that 0 = P
i αiai + P
j γjbj.
Proof. (a) is equivalent to
(c) there does not exist v̸ = 0 such that ai · v ≥0 for i = 1, . . . , r and bj · v ≥0 for
j = 1, . . . , s and (−bj) · v ≥0 for j = 1, . . . , s.
(c) implies (b). Let C denote the cone spanned by A∪B∪−B. (c) states that C not contained
in any half-space through the origin. By Farkas’ lemma [30], it follows that C = RN. Thus,
A ∪B ∪−B spans RN and −P
i ai ∈C. (b) follows.
(b) implies (c): consider v such that ai · v ≥0 and bj · v = 0 for all i, j. We know there
exist αi > 0 and γj real such that 0 = P
i αiai + P
j γjbj. Taking inner product with v, it
follows that 0 = P
i αiai · v. Since αi > 0 and ai · v ≥0 for all i, it follows that ai · v = 0 for
all i. Thus, v is perpendicular to A ∪B which is assumed to span RN. Thus v = 0 and (c)
follows.
□
The next lemma concerns super-linear polynomial functions on a cone.
Lemma 5.2. Suppose C is a closed cone in Rr and p : C −→R is a polynomial that satisﬁes
p(nx) ≥cxn for n > 0, x ∈C \ {0} and cx > 0. Then, there exists c > 0 and c′ > 0 such
that p(x) ≥c|x| for all x ∈C with |x| ≥c′.
Proof. Let S = {x ∈Rr | |x| = 1} denote the unit sphere and let p = Pd
k=0 pk(x) denote the
decomposition of p into homogeneous polynomials pk of degree k. Since p(nx) = P
k nkpk(x),
it follows that that for every x ∈S ∩C there exists i such that pj(x) = 0 for j > i and
pi(x) > 0. In particular, pd : S ∩C −→[0, ∞).
Case 1: pd(S ∩C) ⊂(0, ∞).
By compactness, pd(x) ≥c0 > 0 for x ∈S ∩C and
|pk(x)| ≤ck for x ∈S ∩C and k = 1, . . . , d −1. Thus p(x) ≥c0|x|d −Pd−1
k=0 |x|kck ≥c|x| for
some c > 0.
THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES
15
Case 2: There exists x ∈S ∩C such that pd(x) = 0 and pd−1(x) > 0. Argue as above
using the complement of a neighborhood of x where p1 is strictly positive, and conclude the
proof by induction on the depth of a point.
□
Consider the restriction
(5.1)
Iρ
M(m, e)(q) =
X
n∈N
q
n
2 v·k0
rY
i=1
I∆(mi −nbi · k0, ei + nai · k0)
of the sum that deﬁnes IM on a ray ρ = Nk0 for k0 ∈Zr, k0̸ = 0. Consider the union R of
the 3 rays in R2 shown in Figure 5.
Figure 5. The degree of the tetrahedron index.
If ρ = Nk0 is a ﬁxed ray, let x = BTk0 = (x1, . . . , xs) and y = ATk0 = (y1, . . . , ys).
Lemma 5.3. (a) If (−xi, yi)̸ ∈R for some i = 1, . . . , s, then Iρ
M(m, e) converges for all m, e.
(b) If (−xi, yi) ∈R for all i = 1, . . . , s. Then, there exist Q ∈{1, . . . , s} →{1, 2, 3} such
that (−xi, yi) ∈ρQ(i) for all i = 1, . . . , s. Then Iρ
M does not converge if and only if all of the
following inequalities hold:
bi · k0 = 0,
ai · k0 ≥0,
(−v) · k0 ≤0
if
Q(i) = 1
(5.2a)
(ai −bi) · k0 = 0,
(−bi) · k0 ≥0,
(−v + bi) · k0 ≤0
if
Q(i) = 2
(5.2b)
(−ai) · k0 = 0,
(−ai + bi) · k0 ≥0,
(−v + ai) · k0 ≤0
if
Q(i) = 3
(5.2c)
Proof. (a) Without loss of generality, let us assume m = e = 0. In that case, the degree of
the summand in Equation (5.1) is given by
n2
s
X
i=1
δ2(−xi, yi) + n
s
X
i=1
δ1(−xi, yi) + n
2v · k0
where δ1 and δ2 are piece-wise quadratic and linear functions given by Figure 6.
Figure 6. Piece-wise quadratic and linear functions δ2 and δ1.
16
STAVROS GAROUFALIDIS
If (−xi, yi)̸ ∈R for some i = 1, . . . , s, it follows that the degree of the summand is a
quadratic function of n with nonvanishing leading term, thus Iρ
M converges.
(b) The above computation shows that Iρ
M(0, 0) diverges if and only if δ2(−xi, yi) = 0 for
all i = 1, . . . , s and in addition the coeﬃcient of n is less than or equal to zero. The ﬁrst
condition is equivalent to (−xi, yi) ∈R for all i and together with the second one, they are
equivalent to the inequalities (5.2).
□
Proof. (of Theorem 2.4) Lemma 5.2 implies that IM converges if and only Iρ
M converges for
all rays ρ. This is true since the degre of the summand of IM is a piece-wise quadratic
polynomial. Lemma 5.3 gives necessary and suﬃcient conditions for the convergence of Iρ
M.
It remains to match these conditions with the deﬁnition of an index structure on M using
Lemma 5.1.
The above discussion implies that IM is convergent if and only if for every Q: {1, . . . , s} →
{1, 2, 3}, there does not exist k0̸ = 0 such that Equation (5.2) holds. Assume for simplicity
that s = 1.
Case 1: If Q(1) = 1 Inequality (5.2) and Lemma 5.1 implies that there exist α1 > 0 and
γ1 real such that v = α1a1 + γ1b1. Deﬁne β1 = 1 −α1 −γ1.
Case 2: If Q(1) = 2 Inequality (5.2) and Lemma 5.1 implies that there exist α′
1 > 0 and
γ′
1 real such that v −b1 = α′
1(−b1) + γ′
1(a1 −b1). Letting (α1, β1, γ1) = (γ′
1, α′
1, −γ′
1 −α′
1 + 1)
it follows that
v = α1a1 + γ1b1,
β1 > 0 .
Case 3: If Q(1) = 3 Inequality (5.2) and Lemma 5.1 implies that there exist α′
1 > 0 and
γ′
1 real such that v −a1 = α′
1(−a1 + b1) + γ′
1(−a1). Letting (α1, β1, γ1) = (1 −α′
1 −γ′
1, γ′
1, α′
1)
it follows that
v = α1a1 + γ1b1,
γ1 > 0 .
It follows that M admits an index structure.
The general case of s follows as above. Indeed for each Q : {1, . . . , s} →{1, 2, 3}, assume
(−xi, yi) ∈ρQ(i) for i = 1, . . . , s. Then Iρ
M convergences if and only if there exists (α, β, γ)
that satisﬁes Equations (2.1) and inequalities (2.2). This completes the convergence proof
of Theorem 2.4. q-holonomicity follows from the main theorem of Wilf-Zeilberger [27], using
the fact that IM(m, e) is a 2r-dimensional sum of a proper q-hypergeometric summand.
□
