---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-019-322-topologically-twisted-index-of-tlp1
section_title: "Topologically twisted index of $T[L(p,1)]$"
section_number: 3.2.2
pages: 34-39
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
For group G = SU(2), the topologically twisted index (reﬁned by angular momentum) of
T[L(p, 1)] reads [56]:
Itop(q, t) = 1
2
X
m∈Z
Z
JK
dz
2πiz
z2(p+2)m q−m (1 −z2qm)(1 −z−2qm)
(z2tq1−m; q)2m−1(z−2tq1+m; q)−2m−1(tq; q)−1
,
(3.43)
where, as usual, the Pochhammer symbol with negative integer in the subscript is deﬁned via
the following identity:
(x; q)n =
1
(xqn; q)−n
.
(3.44)
The contour in (3.54) is chosen according to the Jeﬀrey-Kirwan residue prescription. Namely,
we either choose poles at z = 0, z = ±
√
t q··· or at z = ∞, z = ±1/
√
t q···. The result is
strikingly simple:
Itop(q, t) =





1
(t2q2;q)−3 ≡(t2/q; q)3, p = 1,
1 −t4,
p = 2,
1 −t3,
p ≥3.
(3.45)
31The full index IU(N)(q, t) of T[L(p, 1)] vanishes in the unreﬁned limit t →1,
IU(N)(q, t) ∼(1 −t−1)NIU(N)(q),
(3.38)
due to the contribution of Cartan components of the adjoint chiral multiplet with R-charge 2, which saturate
the unitarity bound. The rescaling in (3.40) removes their contribution and makes the limit ﬁnite. Another
method of regularization is to take the same limit but in the form t = qϵ, ϵ →0, which correponds to taking
R-charge to be 2 −ϵ, and then just remove an appropriate power of ϵ:
I′
U(N)(q) = lim
ϵ→0 IU(N)(q, t) · ϵ−N = (log q)NIU(N)(q).
(3.39)
This is the approach that was used in [31]. Then the (log q)N ∝k−N factor agrees with the factorization if we
include the overall factor k−N/2 in (2.42) into the deﬁnition of Za(q).
– 33 –
As expected, the result for p = 1 is in agreement with the dual description by a free chiral
multiplet with R-charge 4. Note that for p > 1 the result turns out to be q-independent. In
fact, for large p, the twisted index of T[L(p, 1); G] with a general Lie group G becomes
Itop
p≫1
−→P−t(G),
(3.46)
where P−t(G) denotes the Poincar´e polynomial of G in variable −t. For G = SU(2),
P−t(G) = 1 −t3
(3.47)
and, for SU(3), one has [69]:
Itop
p≫1
−→1 −t3 −t5 + t8 = P−t(SU(3)).
(3.48)
Additionally, the BPS spectrum can be identiﬁed with the cohomology of G,
H•
tw-BPS = H•(G).
(3.49)
An argument for this relation mentioned above is essentially given in section 5 of [70] after
Proposition 3, as summarized in the following.
The twisted index of T[L(p, 1)] computes the equivariant index of certain K-theory class
over MH(CP1; G), the Hitchin moduli stack over CP1,32
Itop(q, t) = Indt(MH, Fq ⊗Lp).
(3.50)
Here, MH is a complicated derived stack, but using the projection map MH(CP1) →M(CP1)
to the moduli stack of GC-bundles over CP1, the above index can be written as33
Itop(q, t) = Ind(M, StTM ⊗Fq ⊗Lp),
(3.51)
and can be further decomposed into a summation over diﬀerent strata of M(CP1), given by
Grothendieck’s classiﬁcation theorem.
For suﬃciently large p, the contribution from the unstable strata all vanish. And the
semi-stable stratum is the classifying stack BGC (it could be viewed as a single point —
the moduli space — with GC as the stabilizer). As both Lp and Fq are trivial over BGC,
both q and p dependence disappears, and the problem only depends on the choice of G. In
this simple case, one can actually directly compute the cohomology groups (BPS states) that
contribute to the index in (3.51)
H•
tw-BPS = H•(M, StTM ⊗Fq ⊗Lp).
(3.52)
32In this equation, L is the determinant line bundle and Fq is an object in the derived category of coherent
sheaves on MH with dependence on q. In general, as explain in [54, 69], the twisted partition function of
T[L(k, 1)] on S1 × Σ gives the “equivariant Verlinde formula,” which in turn can be written as a K-theory
index over MH(Σ). This fact, combined with the projection map MH →M, is the starting point for the proof
of the equivariant Verlinde formula [70,71].
33Here StTM denotes the total symmetric power of the tangent complex of M.
– 34 –
The tangent space of BGC is given by the two-step complex g →0 with g placed at degree
−1. So in the end, one has
Hj
tw-BPS = H−j
G (Λjg[j]) = (Λjg)G = Hj(G),
(3.53)
with the BPS states represented by the elements in the cohomolgy of the group G, or equiva-
lently, elements in (Λ•g)G. And, in this concrete example, one again ﬁnds that t-degree agrees
with cohomological degree. The “(co-)homological-ﬂavor locking” in this case is a result of
the tangent complex g →0 being concentrated in degree −1.
In fact, the above explanation using the stack language can be readily “translated” into
a physics argument as follows. When p is suﬃciently large, in the topologically twisted index
of T[M3] only the zero-ﬂux sector m = 0 survives — this is what mathematicians would call
the “semi-stable stratum.” Then, the index essentially becomes the index of the N = 2 SQM
(which can be considered as a reduction of a 2d N = (0, 2) theory) with gauge group G and
an adjoint Fermi multiplet Ψ of U(1)β charge 1. In particular, for G = SU(2) we have
Itop(q, t) = 1
2
X
m∈Z
Z
JK
dz
2πiz (1 −z±2)(1 −tz±2)(1 −t) = (1 −t3).
(3.54)
In the IR, such theory should be eﬀectively described by gauge-invariant combinations of
Fermi-ﬁelds, corresponding precisely to generators of G-invariant part of the exterior algebra
(Λg)G, which, in turn, can be understood as generators of the cohomology of the Lie group.
For G = SU(N) these correspond to TrΨ3, TrΨ5, ..., TrΨ2N−1 in the SQM.
Although the topological index looks much simpler compared to the superconformal
index, it should also admit a factorization into the homological blocks via (2.39).
For
G = SU(2), we would like to check
Itop(q, t) =
X
a∈Zp/Z2
|Wa| bZa(q, t) bZa(1/q, t).
(3.55)
It is easy to see how this works for p = 1 (M3 = S3):
bZ0(q, t) · bZ0(1/q, t) =
1
(t2q2; q)∞
·
1
(t2q−2; q−1)∞
= (t2q−1; q)∞
(t2q2; q)∞
= (t2/q; q)3.
(3.56)
In the case p > 1, again, the problem of deﬁning bZa(1/q, t) arises. It will be resolved for both
superconformal and topologically twisted index in section 3.2.4.
3.2.3 t = qβ reduction
Consider the case of G = SU(2).
Instead of taking the unreﬁned limit t →1, one can
consider more general34 limit t →qβ, with β ∈Z. One can show that in such a limit the
34A similar reduction was considered in [19] for reﬁned Chern-Simons theory as a way to circumvent certain
technicalities.
– 35 –
reduced (that is with removed contribution of the Cartan component of the adjoint chiral)
the superconformal index given by formula (3.54) becomes a Laurent polynomial in q or a
rational function, depending on the sign of β:
I(β)(q) ≡lim
t→qβ I(q, t) (qt; q)∞
(1/t; q)∞
∈
(
Z[q, q−1], β ∈Z+,
Z(q),
β ∈−Z+.
(3.57)
Similarly, for topologically twisted index we have
I(β)
top(q) ≡lim
t→qβ Itop(q, t) (qt; q)−1 = lim
t→qβ
Itop(q, t)
1 −t
,
(3.58)
while for the homological blocks we obtain
bZ(β)
a (q) ≡(qt; q)∞bZa(q, t)

t=qβ
∈q
a2
p ·
(
Z[q], β ∈Z+,
Z(q), β ∈−Z+.
(3.59)
Explicitly, we have
bZ(β)
a (q) =
1
|Wa|
Z
dz
2πiz (z2; q)β+1(z−2; q)β+1
X
n∈pZ+a
qn2/p z2n.
(3.60)
Taking into account that
(q−1t−1; q−1)∞=
1
(1/t; q)∞
,
(3.61)
the formula (3.35) then reduces to the following relation between Laurent polynomials (for
β ∈Z+) or rational functions (for β ∈−Z+):
I(β)(q) =
X
a∈Zp/Z2
|Wa| bZ(β)
a (q) bZ(β)
a (1/q).
(3.62)
For the topologically twisted index we have instead
I(β)
top(q) =
X
a∈Zp/Z2
|Wa| bZ(β)
a (q) bZ(−β)
a
(1/q).
(3.63)
These relations are easy to check for various values of p and β. For example, for p = 5 we
should check
I(β)(q) = 2 bZ(β)
0
(q) bZ(β)
0
(1/q) + bZ(β)
1
(q) bZ(β)
1
(1/q) + bZ(β)
2
(q) bZ(β)
2
(1/q)
(3.64)
and
I(β)
top(q) = bZ(β)
0
(q) · 2 bZ(−β)
0
(1/q) + bZ(β)
1
(q) bZ(−β)
1
(1/q) + bZ(β)
2
(q) bZ(−β)
2
(1/q).
(3.65)
The particular expressions for a few ﬁrst values of β are as follows.
– 36 –
For β = 0,
bZ(0)
0 (q) = 1, bZ(0)
1 (q) = −q1/5, bZ(0)
2 (q) = 0.
I(0)(0) = 3,
I(0)
top(0) = 3.
(3.66)
For β = 1,35
bZ(1)
0 (q) = 1 + q + q2, bZ(1)
1 (q) = −q1/5(1 + 2q + q2), bZ(1)
2 (q) = q9/5.
2 bZ(−1)
0
(q) = 1, bZ(−1)
1
(q) = 0, bZ(−1)
2
(q) = 0.
I(1)(q) = 3
q2 + 8
q + 13 + 8 q + 3 q2,
I(1)
top(q) = 1 + q + q2.
(3.67)
For β = 2,
bZ(2)
0 (q) = 1 + q + 2q2 + 2q3 + 2q4 + q5 + q6,
bZ(2)
1 (q) = −q1/5(1 + 2q + 3q2 + 3q3 + 3q4 + 2q5 + q6),
bZ(2)
2 (q) = q9/5(1 + q + 2q + q4).
2 bZ(−2)
0
(q) = −q2/(1 −q2),
bZ(−2)
1
(q) = −q6/5/(1 −q2),
bZ(−2)
2
(q) = −q4/5/(1 −q2).
I(2)(q) = 3
q6 + 8
q5 + 21
q4 + 35
q3 + 55
q2 + 65
q + 76 + 65q + 55q2 + 35q3 + 21q4 + 8q5 + 3q6,
I(2)
top(q) = 1 + q2 + q4.
(3.68)
And for β = 3,
bZ(3)
0 (q) = q12 + q11 + 2q10 + 3q9 + 4q8 + 4q7 + 5q6 + 4q5 + 4q4 + 3q3 + 2q2 + q + 1,
bZ(3)
1 (q) = −q1/5  q12 + 2q11 + 3q10 + 4q9 + 6q8 + 7q7 + 8q6 + 7q5 + 6q4 + 5q3 + 3q2 + 2q + 1

,
bZ(3)
2 (q) = q9/5(q10 + 2q8 + 2q7 + 2q6 + 3q5 + 3q4 + 2q3 + 3q2 + q + 1).
2 bZ(−3)
0
(q) = (q7 + q5 + q4 + q3 + q2)/
 (1 −q3)(1 −q4)

,
bZ(−3)
1
(q) = q11/5  q4 + q3 + q2 + q + 1

/
 (1 −q3)(1 −q4)

,
bZ(−3)
2
(q) = q14/5  q3 + q2 + 2q + 1

/
 (1 −q3)(1 −q4)

.
I(3)
top(q) = 1 + q3 + q6
(3.69)
· · ·
Notice that the coeﬃcients of the q-expansions are always positive (up to an overall sign),
and this reﬂects that the BPS space H(β)
a
obtained from the spectral sequence (3.19), now
doubly-graded by the eigenvalues under the U(1)q × U(1)R action,
H(β)
a
=
M
i,j∈Z
H(β)i,j
a
,
(3.70)
35Notice that after removing a (1 −t) factor from Itop(q, t), we are left with (1 −t3)/(1 −t) = 1 + t + t2.
– 37 –
enjoys some highly non-trivial properties — subspaces with odd j-degree are either all empty,
or have their contributions canceled when we take the equivariant Euler characteristic. More-
over, the spectral sequence (3.19) is consistent with the following property, which one can
check explicitly order by order in q:
(−qt; q)∞bZa(q, −t) = bZ(β)
a (q) + (1 + qβt−1)P+(q, t)
(3.71)
where all the coeﬃcient are positive (up to an overall common sign). Namely,
(−qt; q)∞bZa(q, −t), P+(q, t) ∈±Z+[t][[q]],
bZa(q) ∈±Z+[q]
(3.72)
The second term in (3.71) represent the pairs of states that go away in the cohomology w.r.t.
the deformed supercharge.
Also, the complexity of the blocks bZ(β)
a
and bZ(−β)
a
will grow with β, this is expected from
the discussion in section 3.1.2 via spectral sequence, where we have seen more cancellations
for smaller β and fewer ones for larger β.
