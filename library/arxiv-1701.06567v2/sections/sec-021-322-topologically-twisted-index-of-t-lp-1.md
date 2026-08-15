---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-021-322-topologically-twisted-index-of-t-lp-1
section_title: "Topologically twisted index of T [L(p, 1)]"
section_number: 3.2.2
pages: 34-37
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
For group G = SU (2), the topologically twisted index (reﬁned by angular momentum) of
T [L(p, 1)] reads [56]:
Itop(q,t ) = 1
2
∑
m∈Z
∫
JK
dz
2πiz
z2(p+2)mq−m (1−z2qm)(1−z−2qm)
(z2tq1−m;q)2m−1(z−2tq1+m;q)−2m−1(tq;q)−1
, (3.43)
where, as usual, the Pochhammer symbol with negative integer in the subscript is deﬁned via
the following identity:
(x;q)n = 1
(xqn;q)−n
. (3.44)
The contour in (3.54) is chosen according to the Jeﬀrey-Kirwan residue prescription. Namely,
we either choose poles at z = 0, z =±
√
tq··· or at z =∞, z =±1/
√
tq···. The result is
strikingly simple:
Itop(q,t ) =



1
(t2q2;q)−3
≡ (t2/q;q)3, p= 1,
1−t4, p = 2,
1−t3, p ≥ 3.
(3.45)
31The full indexIU(N)(q,t ) of T [L(p, 1)] vanishes in the unreﬁned limit t→ 1,
IU(N)(q,t )∼ (1−t−1)NIU(N)(q), (3.38)
due to the contribution of Cartan components of the adjoint chiral multiplet with R-charge 2, which saturate
the unitarity bound. The rescaling in ( 3.40) removes their contribution and makes the limit ﬁnite. Another
method of regularization is to take the same limit but in the form t =qϵ, ϵ→ 0, which correponds to taking
R-charge to be 2−ϵ, and then just remove an appropriate power of ϵ:
I′
U(N)(q) = lim
ϵ→0
IU(N)(q,t )·ϵ−N = (logq)NIU(N)(q). (3.39)
This is the approach that was used in [31]. Then the (log q)N∝k−N factor agrees with the factorization if we
include the overall factor k−N/2 in (2.42) into the deﬁnition of Za(q).
– 33 –
As expected, the result for p = 1 is in agreement with the dual description by a free chiral
multiplet with R-charge 4. Note that for p> 1 the result turns out to be q-independent. In
fact, for large p, the twisted index of T [L(p, 1);G] with a general Lie group G becomes
Itop
p≫1
−→ P−t(G), (3.46)
where P−t(G) denotes the Poincar´ e polynomial ofG in variable−t. For G =SU (2),
P−t(G) = 1 −t3 (3.47)
and, for SU (3), one has [69]:
Itop
p≫1
−→ 1−t3−t5 +t8 =P−t(SU (3)). (3.48)
Additionally, the BPS spectrum can be identiﬁed with the cohomology of G,
H•
tw-BPS =H•(G). (3.49)
An argument for this relation mentioned above is essentially given in section 5 of [70] after
Proposition 3, as summarized in the following.
The twisted index of T [L(p, 1)] computes the equivariant index of certain K-theory class
over MH(CP1;G), the Hitchin moduli stack over CP1,32
Itop(q,t ) = Indt(MH,Fq⊗Lp). (3.50)
Here, MH is a complicated derived stack, but using the projection mapMH(CP1)→ M(CP1)
to the moduli stack of GC-bundles over CP1, the above index can be written as 33
Itop(q,t ) = Ind(M,StTM⊗Fq⊗Lp), (3.51)
and can be further decomposed into a summation over diﬀerent strata of M(CP1), given by
Grothendieck’s classiﬁcation theorem.
For suﬃciently large p, the contribution from the unstable strata all vanish. And the
semi-stable stratum is the classifying stack BGC (it could be viewed as a single point —
the moduli space — with GC as the stabilizer). As both Lp andFq are trivial over BGC,
both q and p dependence disappears, and the problem only depends on the choice of G. In
this simple case, one can actually directly compute the cohomology groups (BPS states) that
contribute to the index in ( 3.51)
H•
tw-BPS =H•(M,StTM⊗Fq⊗Lp). (3.52)
32In this equation, L is the determinant line bundle and Fq is an object in the derived category of coherent
sheaves on MH with dependence on q. In general, as explain in [54, 69], the twisted partition function of
T [L(k, 1)] on S1× Σ gives the “equivariant Verlinde formula,” which in turn can be written as a K-theory
index over MH(Σ). This fact, combined with the projection map MH→ M, is the starting point for the proof
of the equivariant Verlinde formula [70,71].
33Here StTM denotes the total symmetric power of the tangent complex of M.
– 34 –
The tangent space of BGC is given by the two-step complex g→ 0 with g placed at degree
−1. So in the end, one has
Hj
tw-BPS =H−j
G (Λjg[j]) = (Λjg)G =Hj(G), (3.53)
with the BPS states represented by the elements in the cohomolgy of the group G, or equiva-
lently, elements in (Λ•g)G. And, in this concrete example, one again ﬁnds that t-degree agrees
with cohomological degree. The “(co-)homological-ﬂavor locking” in this case is a result of
the tangent complex g→ 0 being concentrated in degree −1.
In fact, the above explanation using the stack language can be readily “translated” into
a physics argument as follows. When p is suﬃciently large, in the topologically twisted index
of T [M3] only the zero-ﬂux sector m = 0 survives — this is what mathematicians would call
the “semi-stable stratum.” Then, the index essentially becomes the index of the N = 2 SQM
(which can be considered as a reduction of a 2d N = (0, 2) theory) with gauge group G and
an adjoint Fermi multiplet Ψ of U(1)β charge 1. In particular, for G =SU (2) we have
Itop(q,t ) = 1
2
∑
m∈Z
∫
JK
dz
2πiz (1−z±2)(1−tz±2)(1−t) = (1−t3). (3.54)
In the IR, such theory should be eﬀectively described by gauge-invariant combinations of
Fermi-ﬁelds, corresponding precisely to generators of G-invariant part of the exterior algebra
(Λg)G, which, in turn, can be understood as generators of the cohomology of the Lie group.
ForG =SU (N) these correspond to TrΨ 3, TrΨ5, ..., TrΨ2N−1 in the SQM.
Although the topological index looks much simpler compared to the superconformal
index, it should also admit a factorization into the homological blocks via ( 2.39). For
G =SU (2), we would like to check
Itop(q,t ) =
∑
a∈Zp/Z2
|Wa|ˆZa(q,t )ˆZa(1/q,t ). (3.55)
It is easy to see how this works for p = 1 (M3 =S3):
ˆZ0(q,t )· ˆZ0(1/q,t ) = 1
(t2q2;q)∞
· 1
(t2q−2;q−1)∞
= (t2q−1;q)∞
(t2q2;q)∞
= (t2/q;q)3. (3.56)
In the case p> 1, again, the problem of deﬁning ˆZa(1/q,t ) arises. It will be resolved for both
superconformal and topologically twisted index in section 3.2.4.
3.2.3 t =qβ reduction
Consider the case of G = SU (2). Instead of taking the unreﬁned limit t → 1, one can
consider more general 34 limit t→ qβ, with β∈ Z. One can show that in such a limit the
34A similar reduction was considered in [19] for reﬁned Chern-Simons theory as a way to circumvent certain
technicalities.
– 35 –
reduced (that is with removed contribution of the Cartan component of the adjoint chiral)
the superconformal index given by formula ( 3.54) becomes a Laurent polynomial in q or a
rational function, depending on the sign of β:
I(β)(q)≡ lim
t→qβ
I(q,t ) (qt;q)∞
(1/t;q)∞
∈
{
Z[q,q−1], β∈ Z+,
Z(q), β ∈− Z+. (3.57)
Similarly, for topologically twisted index we have
I(β)
top(q)≡ lim
t→qβ
Itop(q,t ) (qt;q)−1 = lim
t→qβ
Itop(q,t )
1−t , (3.58)
while for the homological blocks we obtain
ˆZ(β)
a (q)≡ (qt;q)∞ˆZa(q,t )
⏐⏐⏐
t=qβ
∈q
a2
p ·
{
Z[q], β∈ Z+,
Z(q), β∈− Z+. (3.59)
Explicitly, we have
ˆZ(β)
a (q) = 1
|Wa|
∫ dz
2πiz (z2;q)β+1(z−2;q)β+1
∑
n∈pZ+a
qn2/pz2n. (3.60)
Taking into account that
(q−1t−1;q−1)∞ = 1
(1/t;q)∞
, (3.61)
the formula ( 3.35) then reduces to the following relation between Laurent polynomials (for
β∈ Z+) or rational functions (for β∈− Z+):
I(β)(q) =
∑
a∈Zp/Z2
|Wa|ˆZ(β)
