---
doc_id: arxiv-math-0105186v2
doc_title: "A long exact sequence for symplectic Floer cohomology"
section_id: sec-012-31-preliminaries
section_title: "Preliminaries"
section_number: 3.1
pages: 51-55
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
toc_source: inferred
doc_brief: "A long exact sequence for symplectic Floer cohomology — 17 sections: Front matter; Introduction; Dehn twists, and all that"
---
Preliminaries
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
