---
doc_id: arxiv-math-0105186v2
doc_title: "arXiv:math/0105186v2 [math.SG] 20 Jul 2002"
section_id: sec-011-31-preliminaries
section_title: "Preliminaries"
section_number: 3.1
pages: 51-60
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
toc_source: inferred
---
This section sets up the framework for the whole chapter. The data are: M is
an exact symplectic manifold. L0, L1 ⊂M are exact Lagrangian submanifolds.
L ⊂M is an exact Lagrangian sphere, which comes with a diﬀeomorphism
f : Sn →L and a symplectic embedding ι : T (λ) →M for some λ > 0, such
that ι|T (0) = f. We use the Dehn twist τL deﬁned using ι and a function R.
Also given are small constants ǫ, δ > 0. The following conditions are required
to hold:
(I) L ∩L0, L ∩L1, L0 ∩L1 are transverse intersections, and L ∩L0 ∩L1 = ∅.
(II) The actions aL0,L1(x) of distinct points x ∈L0 ∩L1 diﬀer by at least
3ǫ.
Secondly, as (x0, x1) runs over (L0 ∩L) × (L ∩L1), the numbers
aL0,L(x0) + aL,L1(x1) diﬀer pairwise by at least 3ǫ. Thirdly, for any x ∈
L0 ∩L1, (x0, x1) ∈(L0 ∩L) × (L ∩L1) one has
|aL0,L1(x) −aL0,L(x0) −aL,L1(x1)| ≥5ǫ.
(III) For all yk ∈f −1(L∩Lk), k = 0, 1, the distance dist(y0, y1) in the standard
metric on Sn is ≥2πδ.
(IV) ι∗θ = θT |T (λ) is the standard one-form, and the function KL associated
to L is zero. Moreover, each ι−1(Lk) ⊂T (λ) is a union of ﬁbres; one can
write this as
ι−1(Lk) =
[
y∈ι−1(L∩Lk)
T (λ)y.
(3.1)
(V) R satisﬁes 0 ≥2πR(0) > −ǫ, and is such that τL is δ-wobbly.
Remark 3.1. Since we will establish the exact sequence under these conditions,
it is necessary to convince ourselves that they do not restrict its validity in any
51
way. Suppose then that we are given arbitrary exact Lagrangian submanifolds
L0, L1 and a framed exact Lagrangian sphere (L, [f]) in M. After perturbing the
submanifolds slightly, one can assume that (I) holds. Another such perturbation
achieves (II) for some ǫ > 0. This is an instance of a general fact: by moving
one of two transverse exact Lagrangian submanifolds slightly, the action of the
intersection points can be changed independently of each other, by arbitrary
suﬃciently small amounts. Choose some representative f of the framing. Since
L0 ∩L1 ∩L = ∅, (III) is automatically true for some δ > 0.
Because the
intersections L ∩Lk are transverse, one can ﬁnd a symplectic embedding ι :
T (λ) →M, for some λ > 0, which extends f and such that ι−1(L ∩Lk) is a
union of ﬁbres. By replacing θ with θ + dH for a suitable H, and making λ
smaller, one can ensure that ι∗θ = θT is satisﬁed. Note that when one modiﬁes
θ in this way, the functions associated to exact Lagrangian submanifolds change
accordingly. One can use this and the freedom in the choice of H to arrange that
KL becomes equal to zero. In any case, the values of the action functional at
intersection points remain the same, so that this does not interfere with (II). We
have now satisﬁed (IV). It is no problem to choose R such that (V) holds for the
previously obtained ǫ, δ. None of the changes which we have made aﬀects Floer
cohomology. Therefore, once the exact sequence is established for the modiﬁed
data, it also holds for the original ones.
Next, we need to draw some elementary inferences. (IV) implies that dKLk =
θ|Lk vanishes on Lk ∩im(ι); in other words KLk ◦ι is constant on each ﬁbre
in (3.1). Let τ be the model Dehn twist from which τL is constructed. The
function Kτ associated to it was determined in Lemma 1.8. Now KτL vanishes
outside im(ι) and, again by (IV), satisﬁes KτL ◦ι = Kτ. Concretely
KτL(ι(y)) = 2π(R′(||y||)||y|| −R(||y||))
= −2πR(0) + 2π
Z ||y||
0
(R′(||y||) −R′(t)) dt.
(3.2)
In particular KτL|L = −2πR(0), which by (V) lies in [0; ǫ). The same condition
says that R′ decreases monotonically from R′(0) = 1/2 until it reaches the value
δ, and thereafter takes values in [0; δ). By combining this with (3.2) one obtains
the estimate, valid for all y ∈T (λ) with R′(||y||) ≥δ,
−2πR(0) ≥KτL(ι(y)) ≥−2πR(0) −2π
Z ∞
0
R′(t)dt = 0.
(3.3)
Now consider the R-graded vector spaces
C′ = CF(L, L1) ⊗CF(τL(L0), L),
C′′ = CF(L0, L1).
The ﬁrst part of (II) implies that C′′ has gap (0; 3ǫ). Clearly, a point ˜x0 lies in
τL(L0) ∩L iﬀx0 = τ −1
L (˜x0) lies in L0 ∩L1. By deﬁnition of KτL(L0) and the
52
computation above,
aτL(L0),L(˜x0) = aL0,L(x0) −KτL(x0) = aL0,L(x0) + 2πR(0).
(3.4)
Hence C′ can be identiﬁed with CF(L, L1) ⊗CF(L0, L) up to a shift in the
grading, which is by a constant of size < ǫ. It therefore follows from (II) that C′
has gap (0; 3ǫ), and that the distance between the supports of C′, C′′ is at least
4ǫ. To summarize, what we have shown is that C′, C′′ satisfy the assumptions
(i), (ii) of Lemma 2.32.
Lemma 3.2. τL(L0), L1 intersect transversally, and there are injective maps
p : (τL(L0) ∩L) × (L ∩L1) −→τL(L0) ∩L1,
q : L0 ∩L1 −→τL(L0) ∩L1
such that τL(L0) ∩L1 is the disjoint union of their images. These maps have
the following properties:
(i) q is the inclusion q(x) = x. It preserves the values of the action functional,
aτL(L0),L1(x) = aL0,L1(x). Moreover, for any w ∈τL(L0) ∩L1 and x ∈
L0 ∩L1 with w̸ = q(x) one has aL0,L1(x) −aτL(L0),L1(w) /∈[0; 3ǫ).
(ii) Set ˜x = p(˜x0, x1). Then
0 ≤aτL(L0),L1(˜x) −aτL(L0),L(˜x0) −aL,L1(x1) < ǫ.
(3.5)
Moreover, for any w ∈τL(L0) ∩L1 and (˜x0, x1) ∈(τL(L0) ∩L) × (L ∩L1)
with w̸ = p(˜x0, x1) one has aτL(L0),L1(w) −aτL(L0),L(˜x0) −aL,L1(x1) /∈
[0; 3ǫ).
(iii) Suppose that there are xk ∈L∩Lk, k = 0, 1, whose preimages yk = ι−1(xk)
are antipodes on Sn. Since τ|Sn is the antipodal map, ˜x0 = τL(x0) is equal
to x1 (hence x1 ∈τL(L0)∩L∩L1, and these are all such triple intersection
points). In that case p(˜x0, x1) = ˜x0 = x1, and aτL(L0),L1(p(˜x0, x1)) =
aτL(L0),L(˜x0) + aL,L1(x1).
Proof. (I) and (IV) imply that L0 ∩L1 ∩im(ι) = ∅. Since τL is the identity
outside im(ι), one has L0 ∩L1 = (τL(L0) ∩L1) \ im(ι), so that q can indeed be
deﬁned to be the inclusion. The equality aτL(L0),L1(x) = aL0,L1(x) follows from
the fact that KτL vanishes outside im(ι).
There is a bijective correspondence between pairs (˜x0, x1) ∈(τL(L0) ∩L) ×
(L ∩L1) and (y0, y1) ∈ι−1(L0 ∩L) × ι−1(L ∩L1), given by setting y0 =
ι−1(τ −1
L (˜x0)), y1 = ι−1(x1). As a consequence of (IV),
ι−1(τL(L0) ∩L1) =
[
y0,y1
τ(T (λ)y0) ∩T (λ)y1.
(3.6)
Since τ is δ-wobbly (V) and dist(y0, y1) ≥2πδ (III), one can apply Lemma 1.9
which tells us that each subset on the right hand side of (3.6) consists of exactly
53
one point. Fix temporarily some (y0, y1) and write τ(T (λ)y0) ∩T (λ)y1 = {˜y},
˜x = ι(˜y). One deﬁnes p(˜x0, x1) = ˜x. Then
aτL(L0),L1(˜x) = KL1(˜x) −KτL(L0)(˜x)
= KL1(˜x) −KL0(τ −1
L (˜x)) −KτL(τ −1
L (˜x)).
By construction ˜y lies in the ﬁbre T (λ)y1, and since KL1 ◦ι is constant on ﬁbres,
KL1(˜x) = KL1(x1). The same reasoning shows that KL0(τ −1
L (˜x)) = KL0(x0),
where x0 = τ −1
L (˜x0). Moreover, one sees from (3.2) that KτL is invariant under
τL, so that KτL(τ −1
L (˜x)) = KτL(˜x). With this and (3.4) in mind, one continues
the computation
aτL(L0),L1(˜x) = KL1(x1) −KL0(x0) −KτL(˜x)
= aL,L1(x1) + aL0,L(x0) −KτL(˜x)
= aL,L1(x1) + aτL(L0),L(˜x0) −KτL(ι(˜y)) −2πR(0).
(3.7)
Lemma 1.9 also says that R′(||˜y||) ≥δ. Combining this with (3.3) and (V) shows
that −KτL(ι(˜y)) −2πR(0) lies in [0; ǫ), which completes our proof of (3.5).
It is clear from their deﬁnitions that p, q are injective. A point of τL(L0)∩L1
falls into im(q) or im(p) depending on whether it lies inside or outside im(ι),
hence the two images are disjoint and cover τL(L0) ∩L1. The transversality
follows from Lemma 1.9 for im(p) and from that of L0 ∩L1 for im(q). We now
turn to the claim made in the last sentence of (i). Supposing that w is a point
of L0 ∩L1 diﬀerent from x, one has |aτL(L0),L1(w) −aL0,L1(x)| = |aL0,L1(w) −
aL0,L1(x)| ≥3ǫ by (II). In the remaining case, which is when w = p(˜x0, x1), (3.5)
shows that |aτL(L0),L1(w)−aL0,L1(x)| > |aτL(L0),L(˜x0)+aL,L1(x1)−aL0,L1(x)|−
ǫ. We already know that the supports of C′, C′′ are at least 4ǫ apart, and one
concludes that |aτL(L0),L1(w) −aL0,L1(x)| > 3ǫ. A similar argument, paying
a little more attention to signs, proves the parallel statement in (ii). Finally,
the only non-obvious things in (iii) are the fact that p(˜x0, x1) = x1 and the
statement about the action. But these follow from Lemma 1.9 and the deﬁnition
of p, respectively from (3.7) and KτL|L = −2πR(0).
Lemma 3.2 and (II) imply that the actions aτL(L0),L1(x) of diﬀerent points
x ∈τL(L0) ∩L1 diﬀer by at least 2ǫ. In fact, for two such points which lie in
im(q) the statement follows from (i) in the lemma; for two points which lie in
im(p), from (ii); and combining the two parts shows it when one point lies in
im(p) and the other in im(q). Set
C = CF(τL(L0), L1).
We have just seen that this has gap (0; 2ǫ). Deﬁne maps β : C′ →C, γ : C →C′′
by β(⟨x1⟩⊗⟨˜x0⟩) = ⟨p(˜x0, x1)⟩and γ(⟨p(˜x0, x1)⟩) = 0, γ(⟨q(x)⟩) = ⟨x⟩. The
result above shows that these are of order [0; ǫ) and ﬁt into a short exact sequence
as in Lemma 2.32(iii). What remains to be done is to realize them as “low order
parts” of chain maps b, c, and to construct the homotopy h.
54
3.2
The ﬁrst map
Let S be the surface in Figure 3, which has three boundary components ∂kS
and three strip-like ends (two positive and a negative one). Take the trivial
exact symplectic ﬁbration π : E = S × M →S, with Ω∈Ω2(E), Θ ∈Ω1(E)
pulled back from ω, θ.
Equip this with the Lagrangian boundary condition
Q = (∂1S × τL(L0)) ∪(∂2S × L) ∪(∂3S × L1); κQ is zero, and KQ(z, x) is equal
to KτL(L0)(x), KL(x) or KL1(x), for z in the respective component ∂kS. This
gives rise to a relative invariant
Φrel
0 (E, π, Q) : HF(L, L1) ⊗HF(τL(L0), L) →HF(τL(L0), L1).
The purpose of this section is to analyse this more closely, on the cochain level.
Fix a complex structure j on S, trivial over the ends, and let U ⊂S be the
open set shaded in Figure 3.
S
2
S
3
S
1
Figure 3:
Lemma 3.3. (E, π, Q) and U satisfy the conditions of Proposition 2.28(i).
Proof. The curvature of (E, π) is zero. A section u(z) = (z, σ(z)) is horizontal
iﬀσ(z) ≡x ∈M is constant, and it further satisﬁes u(∂S) ⊂Q iﬀx ∈τL(L0) ∩
L∩L1. If W ⊂S is a connected open subset which intersects all three boundary
components, the same description applies to partial horizontal sections w : W →
E|W with w(W ∩∂S) ⊂Q. As a consequence, any such section can be extended
to u ∈Mh. This is in particular true for W = U.
Fix some x ∈τL(L0)∩L∩L1 and the corresponding constant section u ∈Mh.
By deﬁnition A(u) = 0, and it remains to prove that ind Du,J = 0. From the
description of the points x in Lemma 3.2(iii), together with the corresponding
local statement in Lemma 1.9, it follows that there is a symplectic isomorphism
T Mx ∼= Cn which takes the tangent spaces to τL(L0), L, and L1 to Rn, e2πi/3Rn,
and eπi/3Rn respectively. Since the index is independent of the almost complex
structure, we may choose J = j × JM to be the product of j and some ω-
compatible JM on M. We may also assume that the isomorphism T Mx ∼= Cn
takes JM
x
to the standard complex structure. By deﬁnition, the domain of Du,J
are sections of the vector bundle u∗(T Ev, J|T Ev) ∼= S × T Mx, with boundary
55
conditions given by the tangent spaces to τL(L0), L, L1. Its range are (0, 1)-
forms with values in the same vector bundle. The preceding discussion allows
us to identify
W1
u = {X ∈W 1,p(S, Cn) : Xz ∈ei(1−k)π/3Rn for z ∈∂kS},
W0
u,J = Lp(Λ0,1S ⊗Cn).
(3.8)
In (2.5) take ∇= ∇S × ∇M to be the product of torsion-free connections on
S and on M. Then the second term (∇XJ) ◦Du ◦j in the formula vanishes,
because Du ◦j takes values in T Eh whereas ∇XJ is nontrivial only on T Ev;
and moreover, the pullback connection u∗∇on u∗T Ev is trivial. This shows
that Du,J is the standard ¯∂-operator for functions S →Cn, with boundary
conditions (3.8).
2
z
z
z
z1
3
z0
4
z5
Figure 4:
There is a general index formula for such operators, but we prefer to use an
ad hoc gluing trick instead. Consider the compact surface ¯S in Figure 4, which
is of genus one with one boundary component. Parametrize the boundary by
a closed path l : [0; 6] →∂¯S, such that l(t) = zt for t ∈{0, 1, 2, 3, 4, 5} are the
marked points in Figure 4. Take a smooth nondecreasing function λ : [0; 6] →R
such that
λ(t) =









0
0 ≤t ≤1,
1/3
2 ≤t ≤3,
2/3
4 ≤t ≤5.
1
t = 6.
56
Let ¯D be the ¯∂-operator on the trivial bundle ¯S × Cn →¯S, with boundary
condition given by the family of Lagrangian subspaces Λl(t) = eπiλ(t)Rn ⊂Cn.
As a loop in the Lagrangian Grassmannian, this represents n times the standard
generator of the fundamental group. Riemann-Roch for compact surfaces with
boundary therefore tells us that ind ¯D = nχ( ¯S)+n = 0. On the other hand, one
can divide ¯S into ﬁve pieces (two shaded and three unshaded ones) as indicated
in Figure 4, and add strip-like ends to each piece; the standard gluing theory
for elliptic operators says that ind ¯D is the sum of the indices of the obvious
corresponding operators on those pieces. For each shaded piece, this yields a
copy of Du,J (in one of the two cases, the vector space Cn has been rotated
by eπi/3). The unshaded pieces give rise to operators of index zero. This can
be derived from the index theorem of [20], or else by directly deforming the
operator to an invertible one. Consider for instance the two intervals of ∂¯S
which are contained in the leftmost unshaded piece. The Lagrangian subspaces
Λz parametrized by the points z in one of these intervals are all equal to eπi/3Rn;
for the other interval, they are of the form eπisRn for 2/3 ≤s ≤1.
Since
eπi/3Rn ∩eπisRn = 0 for all such s, the Maslov index for paths [20] is zero. The
same holds for the other unshaded pieces, and one concludes that 0 = ind ¯D =
2 ind Du,J.
At this point, ﬁx
J(1) ∈Jreg(M, τL(L0), L),
J(2) ∈Jreg(M, L, L1),
J(3) ∈Jreg(M, τL(L0), L1).
Proposition 2.28(i) tells us that there is a J ∈J(E, π, j, J(1), J(2), J(3)) which
is both horizontal and regular. By part (ii) of the same result, the coeﬃcients
νJ(˜x0, x1, x) for ˜x0 ∈τL(L0)∩L, x1 ∈L∩L1, x ∈τL(L0)∩L1, are zero whenever
χ(˜x0, x1, x) = aτL(L0),L1(x) −aτL(L0),L(˜x0) −aL,L1(x1)
(3.9)
is < 0. Lemma 3.2(ii) shows that χ(˜x0, x1, x), if ≥0, must be either in [0; ǫ) or
[3ǫ; ∞), and that the ﬁrst case only happens for x = p(˜x0, x1). Hence, if one
writes the relative invariant as
CΦrel
0 (E, π, Q, J) = φ + (CΦrel
0 (E, π, Q, J) −φ),
φ(⟨˜x0⟩⊗⟨x1⟩) = νJ(˜x0, x1, p(˜x0, x1))⟨p(˜x0, x1)⟩
(3.10)
then φ is of order [0; ǫ), while the second term is of order [3ǫ; ∞). The rest of
this section contains the proof of the following result, which determines the low
order part:
Proposition 3.4. νJ(˜x0, x1, p(˜x0, x1)) = 1 for all (˜x0, x1).
There is one particular case of this which follows from the previous con-
siderations.
Namely, suppose that there is a pair (˜x0, x1) with ˜x0 = x1 =
57
x ∈τL(L0) ∩L ∩L1. In that case p(x, x) = x and χ(x, x, x) = 0 by Lemma
3.2(iii), and therefore νJ(x, x, x) = #Mh(x, x, x) by Proposition 2.28(ii). Now
#Mh(x, x, x) = 1 because, as we saw already when proving Lemma 3.3, the
unique element of that space is the constant section u(z) = (z, x). Our strategy
will be to reduce the computation of all the νJ(˜x0, x1, p(˜x0, x1)) to this case, by
using suitable deformations.
What “deformation” means here is keeping the submanifolds L, L0, L1 and
the constant ǫ ﬁxed, while changing the remaining data. More precisely, for
0 ≤µ ≤1 we consider the following: a smooth family f µ of diﬀeomorphisms
Sn →L; smoothly varying positive numbers λµ, and symplectic embeddings
ιµ : T (λµ) →M with ιµ|T (0) = f µ; the Dehn twists τ µ
L deﬁned using ιµ and
functions Rµ supported in (−∞; λµ); and constants δµ.
These should agree
with the given data f, λ, ι, R, τL, δ for µ = 0. We also require that the analogues
of (III)–(V) continue to hold for any µ; where in (V) we take the original ǫ
throughout.
Choose ˜x0 ∈τL(L0) ∩L, x1 ∈L ∩L1. Given a “deformation” in the sense
which we have just explained, one can set ˜xµ
0 = τ µ
L(τL)−1(˜x0) ∈τ µ
L(L0) ∩L and
xµ
1 = x1 ∈L ∩L1, which “continues” the points smoothly into the deformed
situation.
We claim that x = p(˜x0, x1) ﬁts similarly into a smooth family
xµ ∈τ µ
L(L0) ∩L1. The point is that since (I)–(V) continue to hold, Lemma 3.2
can be applied to the situation for any µ. This ensures that the intersections
τ µ
L(L0) ∩L1 remain transverse, which implies that a unique family xµ exists. In
fact, it even provides a smooth family of injective maps pµ : (τ µ
L(L0)∩L)×(L ∩
L1) →τ µ
L(L0) ∩L1, such that xµ = pµ(˜xµ
0 , xµ
1).
Lemma 3.5. For any (˜x0, x1) there is a “deformation” such that ˜x1
0 = x1
1.
Proof. From (III) we know that y0 = f −1(τ −1
L (˜x0)), y1 = f −1(x1) are points
on Sn whose distance is ≥2πδ. Let gµ ∈Diﬀ(Sn) be an isotopy, g0 = id, such
that g1(y0), g1(y1) are antipodes. There are Cµ ≥1, smoothly depending on µ
and with C0 = 1, with the property that
Cµ ≥||D(gµ)y||, ||D(gµ)−1
y ||
for all y ∈Sn.
Consider the “deformation” f µ = f ◦(gµ)−1, λµ = λ/Cµ, ιµ = ι ◦Gµ|T (λµ),
δµ = δ/Cµ; here Gµ ∈Sympe(T ) is induced by gµ, in the sense that Gµ|T (0) =
(gµ)−1. The bound on D(gµ) implies that Gµ maps T (λµ) to T (λ), so that
ιµ is well-deﬁned. On the other hand, because of the bound on D(gµ)−1, the
distance between any point of (f µ)−1(L∩L0) = gµf −1(L∩L0) and any point of
(f µ)−1(L∩L1) = gµf −1(L∩L1) is ≥2πδµ, which shows that (III) holds during
the deformation. For (IV) it is suﬃcient to note that Gµ takes the canonical
one-form θT to itself and maps ﬁbres to ﬁbres. And it is no problem to ﬁnd
functions Rµ which satisfy (V) with the δµ deﬁned above and the given ǫ. By
deﬁnition
τL|L = f ◦A ◦f −1,
τµ
L|L = f µ ◦A ◦(f µ)−1 = f ◦(gµ)−1 ◦A ◦gµ ◦f −1.
58
Since g1(y1) = A(g1(y0)) by construction, one sees that
˜x1
0 = τ1
L(τL)−1(˜x0) = f ◦(g1)−1 ◦A ◦g1(y0) = f(y1) = x1 = x1
1.
Given a “deformation”, one can repeat the construction at the beginning of
this section in a parametrized sense, which means equipping the trivial exact
symplectic symplectic ﬁbration (E, π) with a smooth family Qµ of Lagrangian
boundary conditions, modelled over the ends on the pairs of exact Lagrangian
submanifolds (τ µ
L(L0), L), (L, L1), and (τ µ
L(L0), L1). Since their intersections
are transverse for all µ, it makes sense to consider parametrized moduli spaces
of pseudo-holomorphic sections. To do that, take smooth families of almost com-
plex structures J(1),µ, J(2),µ, J(3),µ ∈J(M) which reduce to the previously cho-
sen ones for µ = 0, and similarly a family Jµ ∈Jh(E, π, j, J(1),µ, J(2),µ, J(3),µ).
The parametrized moduli space we are interested in is
Mpara =
[
µ
{µ} × MJµ(˜xµ
0 , xµ
1, xµ)
for points ˜xµ
0, xµ
1, xµ as introduced above.
Lemma 3.6. Mpara is compact.
Proof. Consider CF(L, L1), CF(τ µ
L(L0), L), CF(τ µ
L(L0), L1). We already know
that the ﬁrst of these R-graded vector spaces has gap (0; 3ǫ); for the second one,
the same is true because it agrees with CF(L0, L) up to a constant shift in the
grading; and by repeating the considerations after Lemma 3.2, one can show
that CF(τ µ
L(L0), L1) has gap (0; 2ǫ). As another consequence of Lemma 3.2(ii)
in the deformed situation, any (µ, u) ∈Mpara satisﬁes
A(u) = aτ µ
L(L0),L1(xµ) −aτ r
L(L0),L(˜xµ
0 ) −aL,L1(xµ
1) ∈[0; ǫ).
One can now argue exactly as in Lemma 2.24; there are no points at inﬁnity in
the parametrized Gromov-Floer compactiﬁcation, since the principal component
of any such point would have negative action, which would contradict the fact
that (E, π) has nonnegative curvature.
Suppose now that the J(k),µ and Jµ for µ = 1 have been chosen regular; for
J1 this can be achieved without leaving the class of horizontal almost complex
structure, because Lemma 3.3 equally applies to the deformed situation for
µ = 1. By using a parametrized version of the same lemma and of Proposition
2.28(i), one sees that in addition, the family (Jµ) can be chosen to be regular in
the parametrized sense. Then the one-dimensional part of Mpara is a compact
one-manifold, and its boundary points are precisely those with µ = 0 or 1. One
concludes that
νJ(˜x0, x1, x) = νJ1(˜x0
0, x1
1, x1).
59
If the “deformation” is as in Lemma 3.5, the situation for r = 1 is exactly the
special case which we have already discussed, so that νJ1(˜x0
0, x1
1, x1) = 1. Since
such deformations exist for all (˜x0, x1), Proposition 3.4 is proved.
From now on, we ﬁx some J = J(4) ∈Jreg,h(E, π, Q, j, J(1), J(2), J(3)) and
write b = CΦrel
0 (E, π, Q, J(4)) : C′ →C for the relative invariant on the cochain
level. Let β be the map deﬁned at the end of Section 3.1. What (3.10) and
Proposition 3.4 say is that b = β + (b −β), with b −β of order [3ǫ; ∞), which is
even slightly more than required by Lemma 2.32.
L1
L
L
τ
0
L0
(L  )
Figure 5:
Remark 3.7. Our relative invariant is the well-known pair-of-pants product,
or Donaldson product; in fact, if u(z) = (z, σ(z)) lies in MJ(˜x0, x1, x), then σ :
S →M is a “pseudo-holomorphic triangle” whose sides lie on τL(L0), L, L1 and
whose vertices are ˜x0, x1, x. Proposition 3.4 asserts that there is an odd number
of low-area triangles with certain speciﬁed vertices. In the lowest dimension,
n = 1, one can see directly that there is precisely one such triangle (Figure 5).
In higher dimensions it is still easy to construct explicitly the analogue of this
particular triangle, but proving that there are no others seems more diﬃcult. For
that reason, we have preferred to take the indirect approach via “deformations”,
which eﬀectively meant moving τL(L0) in such a way that the area of the triangle
shrinks to zero.
3.3
