---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-012-4-funk-billiards-and-duality
section_title: "Funk billiards and duality"
section_number: 4
pages: 13-18
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
---
Let K⊂ int(L) in Pn be a pair of convex bodies. Using the L-Funk metric on
K, we can consider the corresponding billiard dynamics inside K following [14],
which we call the L-Funk billiard in K. As it is a non-reversible Finsler structure,
some care should be taken, however the results we need go through unaltered. In
particular, using [14, Lemma 3.3] we get the following description of the reﬂection
law, illustrated in ﬁgure 1.
Assumeq1∈∂K, andv∈Sq1K is an incoming ray. Extend the ray until its ﬁrst
intersectionp0 with ∂L. Let Q1 be a hyperplane tangent to ∂K at q1, and P0 the
hyperplane tangent to L at p0. Let z1 = RPn−2 be the intersection Q1∩P0, and
note that z1⊂ RPn\L. Let P1 be the other tangent hyperplane to ∂L throughz1,
andp1∈∂L the tangency point. The vector v′∈Sq1K pointing towardsp1 is then
the outgoing ray.
v
q1
z1
p0
p1
P1
P0
Q1
L
K
v′
q0
q2
Figure 1. Funk billiard reﬂection law
Remark 4.1. It is clear from this description that a proper Funk billiard trajectory
when K,L are smooth and strictly convex, will extend indeﬁnitely, in terms of
bounces, as a proper billiard trajectory.
One can also consider the billiard deﬁned by the reverse Funk metric RFunkL(K).
Its billiard trajectories coincide with the time-reversed Funk billiard trajectories of
FunkL(K).
The same billiard can also be considered from an outer perspective: the phase
space then consists of all ( n− 2)-dimensional planes z⊂ Pn that do not intersect
L, and the billiard map mapping z0 to z1 is deﬁned by the same diagram, which
is reproduced in ﬁgure 2 from the outer billiard perspective. By analogy with the
aﬃne setting, we call this the outer Funk billiard on L with geometry set by K.
Example 4.1. Assume K⊂ B⊂ R2 are two discs centered at the origin. Then
the resulting Funk billiard inside K coincides with the standard Euclidean one, as
illustrated in ﬁgure 3. Indeed, take p0,p 1∈ ∂B, and let z be the intersection of
the tangents to B at those points. Since ∡op0z =∡op1z =∡oq1z = π
2 , the points
p0,p 1,q 1,z,o all lie on the circle having zo as its diameter. It follows that the
incidence angle is ∡p0q1z =∡p0p1z, while the reﬂected angle is ∡p1q1z =∡p1p0z.
It remains to note that |zp0| =|zp1|.
Examining the Funk billiard law description, we see it is projectively invariant.
The following provides an alternative proof of this fact, and extends the projective
invariance to include the length spectrum.
14 A Funk perspective on billiards, projective geometry and Mahler volume
q1
z1
p0
P0
Q1
L
K
q0
z0
Figure 2. Funk outer billiard reﬂection law
o
q1
p0
p1
z
q0
Figure 3. Funk billiard in concentric discs
Proposition 4.2. Choose a hyperplane at inﬁnity η∈ int(L∨). The corresponding
L-Funk billiard reﬂection law in the interior of K is then independent of η, and
thus projectively invariant. Furthermore, the L-Funk length of a periodic orbit is
also projectively invariant.
Proof. Let dη(x,y ) be the (L,η )-Funk distance from x to y. Replacing η byη′, we
havedη′(x,y ) =dη(x,y ) +h(y)−h(x) for some h =hη,η′ by Proposition 3.7.
Now letp,r∈∂K be ﬁxed points. Then p,q,r are consecutive reﬂection points of
the billiard ifq is an extremal point fordη(p,q )+dη(q,r ). Since dη′(p,q )+dη′(q,r ) =
dη(p,q ) +dη(q,r ) +h(r)−h(p), this condition is independent of η.
Finally, ifp0,...,p N−1,pN =p0 is a periodic orbit, then evidently
N−1∑
j=0
dη′(pj,pj+1) =
N−1∑
j=0
dη(pj,pj+1) +
N−1∑
j=0
(h(pj+1)−h(pj)) =
N−1∑
j=0
dη(pj,pj+1),
concluding the proof. □
Example 4.2. Consider the Euclidean ball Bn⊂ Rn. The Funk Finsler norm in
int(Bn) is given by
φx(v) =
√
(1−|x|2)|v|2 +⟨x,v⟩2
1−|x|2 + ⟨x,v⟩
1−|x|2.
The ﬁrst summand is the Beltrami-Klein model of hyperbolic geometry . The second
summand is the 1-form 1
1−|x|2
∑n
j=1xjdxj, which is exact. Consequently, for any
15 A Funk perspective on billiards, projective geometry and Mahler volume
domain K ⊂ int(Bn), the Bn-Funk billiard in K coincides with the hyperbolic
billiard, and the length of periodic orbits is the same in both geometries.
A careful examination of the reﬂection law shows that it is anti-symmetric under
the duality (K,L )↔ (L∨,K∨), namely a Funk billiard trajectory in one naturally
deﬁnes a reverse Funk billiard trajectory in the other, which we call the dual tra-
jectory, as follows. Let us write Qj =LK(qj) = Tqj∂K∈ ∂K∨ for qj∈ ∂K, and
similarly Pj ∈ ∂L∨ for pj ∈ ∂L. We identify the phase space with a subset of
{(q,p ) : q∈ ∂K,p ∈ ∂L∨}, where (q,p ) represents the outgoing ray from q in the
direction of p.
The billiard tranformation ( q0,p 0)↦→ (q1,p 1) can be understood as two dual
billiards unraveling simultaneously, taking alternating steps: the Funk billiard
FunkL(K), and the reverse Funk billiard RFunk K∨(L∨). In P, the ray arrives
at q1∈∂K, and Q1 =LK(q1) is marked on ∂K∨. In P∨, the interval from Q1 to
P0 =LL(p0) (which avoids L∨) is extended until its second intersection P1 with
∂L∨. Now p1 =LL∨(P1)∈∂L is marked, and the outgoing ray from q1 is (q1,p 1).
This dual dynamic is illustrated in ﬁgure 4, where the same letter is used for both
a point and its dual hyperplane.
q1
z1
p0
p1
P1
P0
Q1
L
K
q0
q2
K ∨
L∨
P0
P1
Q1
Q2
P2
p1
q2
Q2
q1
Z1
Z1
z1
p0
Figure 4. Dual Funk - reverse Funk billiard dynamics
We thus established the following.
Proposition 4.3. Let q0,q 1,···∈ ∂K be an L-Funk billiard trajectory in K. Let
pj∈∂L be the ﬁrst intersection of the extension of the oriented segment [qj,qj+1]
with ∂L, and Pj the hyperplane tangent to L at pj. Then P0,P 1,... is a K∨-
reverse Funk billiard trajectory in L∨. In the plane, the two orbits have equal
rotation number.
Remark 4.4. The stark similarity to the duality in Minkowski billiards is not
without reason. In the limit when L is much bigger than K, the Funk billiard
becomes Minkowski, much like the hyperbolic plane is almost Euclidean in small
scale. More precisely, take K⊂ L⊂ Rn, ﬁx a∈ L and set LR = a +R(L−a).
Then as R→∞ , the Funk billiard orbits in K converge to the Minkowski billiard
orbits with geometry given by L centered at a. In particular, if L is the Euclidean
ball and a its center, we recover the Euclidean billiard inside K.
Consider the case of the projective plane. Since the Funk billiard trajectory
consists of straight segments and preserves the symplectic form on the phase space
[14, Theorem 4.3], Birkhoﬀ’s theorem on the existence of two m-periodic orbits, for
anym≥ 2 and any rotation number, remains valid.
16 A Funk perspective on billiards, projective geometry and Mahler volume
As an example, the two 2-periodic orbits when K⊂ L are two non-concentric
circles appear in ﬁgure 5.
Figure 5. 2-periodic orbits in a pair of discs
To motivate the next result, let us consider 2-periodic orbits in general. Assume
thatq0,q 1∈∂K are the bounce points of a 2-periodic orbit γ of theL-Funk billiard
in K, and p0,p 1∈∂L the corresponding intersection points, appearing on the line
in the order p1,q 0,q 1,p 0 as in ﬁgure 6. Note that γ is also a reverse Funk billiard
orbit. Its Funk length is twice the Hilbert distance between the points:
LengthF
L(γ) = LengthRF
L (γ) = log|p1q1|
|p1q0| + log|q0p0|
|q1p0| = 2dH
L (q0,q 1).
p1
p0
q0
q1
P1
Q0
Q1
P0
Figure 6. 2-periodic orbit
Since,
dH
L (q0,q 1) = 1
2 log[p1,q 0,q 1,p 0] = 1
2 log[P1,Q 0,Q 1,P 0] =dH
K∨(P0,P 1),
it holds that dual 2-periodic orbits have equal length. In fact, the duality of billiard
orbits extends to the metric realm in full generality.
We now assume K⊂ int(L) are smooth, strictly convex bodies in RPn.
Theorem 4.5. Dual periodic orbits in FunkL(K) and RFunkK∨(L∨) have equal
lengths.
We will need the following auxiliary fact of independent interest.
17 A Funk perspective on billiards, projective geometry and Mahler volume
Proposition 4.6. There is a GL(V )-invariant non-degenerate 2-form ω on P×
P∨\Z . Such a form is unique up to constant, and moreover it is canonically
normalized. Furthermore, it is a symplectic form.
Proof. Let H = Stabx,ξ⊂ GL(V ) be the stabilizer of a ﬁxed point ( x,ξ ), which
acts on TxP by the full linear group, and similarly on TξP∨. Observe that
∧2T∗
x,ξ(P× P∨) =∧2(x⊗x⊥⊕ξ⊗ξ⊥) =x⊗2⊗∧2x⊥⊕ξ⊗2⊗∧2ξ⊥⊕x⊗x⊥⊗ξ⊗ξ⊥.
The ﬁrst and second summand evidently have no H-invariant elements. As for the
third summand, we may write
x⊗x⊥⊗ξ⊗ξ⊥ = (x⊗ξ)⊗ (x⊥⊗ξ⊥).
There is a natural identiﬁcation θ :x⊗ξ→ R, and a natural pairing η :x⊥⊗ξ⊥→
R, which is moreover non-degenerate as (x,ξ ) /∈Z . We then let ωx,ξ correspond to
θ⊗η−1. It is immediate from the construction that ω is non-degenerate, and it is
evidently canonically normalized.
For uniqueness, it remains to show that any H-invariant non-trivial pairing ψ :
x⊥⊗ξ⊥→ R must be a multiple ofη−1. Writingξ⊥ =W and identifyingx⊥ =W∗,
H acts on x⊥⊗ξ⊥ =W∗⊗W by GL(W ), admitting a unique invariant line.
Finally, let us verify thatω is symplectic, that isdω = 0. As dω∈ Ω3(P×P∨\Z) is
GL(V )-invariant, it suﬃces to show that there are no non-trivial invariant 3-forms.
We have an invariant decomposition
∧3T∗
x,ξ(P× P∨) =x⊗3⊗∧ 3x⊥⊕ξ⊗3⊗∧ 3ξ⊥
⊕x⊗2⊗∧ 2x⊥⊗ξ⊗ξ⊥⊕x⊗x⊥⊗ξ⊗2⊗∧ 2ξ⊥.
As before, the ﬁrst and second summands do not have invariant lines. Consid-
ering the third summand, we have
x⊗2⊗∧ 2x⊥⊗ξ⊗ξ⊥ =x⊗∧ 2x⊥⊗ξ⊥.
One can choose an elementg∈H acting by the identity onx⊥ andξ⊥, and rescaling
x non-trivially. Thus there are no invariant elements in the third summand, and
similiarly neither in the fourth. □
Proof of Theorem 4.5. Recall that by Proposition 4.2, the Funk length of a
periodic orbit is a projective invariant.
Now ﬁxη∈ P∨, and deﬁne Hη : (P\η⊥)× P∨\Z→ T∗P by identifying, for any
x /∈η⊥, x∗ =η, and setting
Hη(x,ξ ) =−
(
ˆη↦→ (x⊥ + ˆη)∩ξ− ˆη
)
∈η∗⊗x⊥ =x⊗x⊥ =T∗
x P. (3)
Forη⁄=η′, we have in the common domain of deﬁnition the equality
Hη′(x,ξ ) =Hη(x,ξ ) +βη,η′(x),
whereβη,η′∈ Ω1(P\ (η⊥∪η′⊥)) is a closed 1-form by the proof of Proposition 3.7.
Let ω0 be the canonic symplectic form on T∗P. We claim that for distinct
η,η′ ∈ P∨, the 2-forms H∗
ηω0 and H∗
η′ω0 coincide on their common domain of
deﬁnition. In light of the previous paragraph, it suﬃces to show that β
∗
ω0 = 0,
whereβ(x,ξ ) = (x,β (x)), andβ∈ Ω1(U) is a closed form, deﬁned in a neighborhood
U ⊂ P. We may choose coordinates locally such that ω0 = ∑dxi∧dξi, while
β =∑ ∂f
∂xi
dxi, and denote B :=Dxβ = ( ∂2f
∂xi∂xj
). Choose u,v∈Tx,ξ(P× P∨), and
write ˆu =dx(u), ˆv =dx(v)∈TxP. We have
18 A Funk perspective on billiards, projective geometry and Mahler volume
β
∗
ω0(u,v ) =ω0((ˆu,B ˆu), (ˆv,B ˆv))
=
∑
i
(ˆui(Bˆv)i− ˆvi(Bˆu)i) =
∑
i,j
Bij ˆuiˆvj−
∑
i,j
Bji ˆuiˆvj = 0.
It follows that as η∈ P∨ varies, H∗
ηω0 patch to a globally deﬁned form ω′∈
Ω2(P× P∨\Z ). Let us check that ω′ is projectively invariant. First we compute
that for g∈ GL(V ),
Hη◦g(x,ξ ) =Hη(gx,g−∗ξ) = (gx, ˆη↦→ (g−∗x⊥ + ˆη)∩g−∗ξ− ˆη) =gHg∗η(x,ξ ).
Consequently,
g∗ω′ =g∗H∗
ηω0 =H∗
g∗ηg∗ω0 =H∗
g∗ηω0 =ω′.
It follows by Proposition 4.6 that ω′ =cω, for some c∈ R. To ﬁnd the value of c,
we note that ωn =µ deﬁnes the Holmes-Thompson volume by Lemma 3.10, which
by deﬁnition corresponds to ωn
0 , and so cn = 1. It is also clear that c> 0, e.g. by
writing both forms explicitly using Euclidean coordinates at a point where ξ =x.
Thusc = 1.
Replacing T∗P with T∗P∨, one similarly has the map
Hθ : P×(P∨\θ⊥)\Z→ T∗P∨, (x,ξ )↦→
(
ˆθ↦→ (ξ⊥ + ˆθ)∩x− ˆθ
)
∈θ∗⊗ξ⊥ =ξ⊗ξ⊥,
and the various formsHθ
∗
ω∨
0 asθ varies patch to giveω′′ =ω′ =c′ω. The constant
is c′ = 1, as the sign is ﬂipped twice compared to Hη: once due to the change of
order of P, P∨, and a second time due to the sign change in the deﬁnition of Hθ.
Fix η∈ int(L∨), θ∈ int(K). It holds by Proposition 3.4 that
S∗ Funkη
L(K) =Hη(K×∂L∨), S ∗ RFunkθ
K∨(L∨) =Hθ(∂K×L∨).
Consider now Σ := ∂(K×L∨)⊂ P× P∨\Z . Denote by α0,α0 the Liouville
1-forms on T∗P, resp. T∗P∨. Deﬁne αη = H∗
ηα0, αθ = Hθ
∗
α0. It holds that
dαη−dαθ =ω−ω = 0, and so αη−αθ =df for some function f deﬁned near Σ.
A dual pair of billiard trajectories corresponds to a trajectory on Σ, as we now de-
scribe. It ﬁrst follows an integral curve of Kerω|K×∂L∨ while on Σ1 := int(K)×∂L∨,
and of Ker ω|∂K×L∨ while on Σ 2 = ∂K× int(L∨), corresponding to the straight
segments of FunkL(K) and RFunkK∨(L∨), respectively. By Remark 4.1, it can
only arrive to ∂K×∂L∨ transversally, and so the reﬂection law translates to sim-
ply switching from one integral curve to another, which similarly must also be
transversal to ∂K×∂L∨. Such a trajectory on Σ is called a generalized character-
istic.
Let a generalized characteristic Γ correspond to a dual pair of orbits γ ⊂
FunkL(K) andγ⊂ RFunkK∨(L∨). Noting that αη|Γ∩∂K×L∨ = 0,αθ|Γ∩K×∂L∨ = 0,
we conclude that
Length(γ) =
∫
Γ
αη =
∫
Γ
αθ = Length(γ).
