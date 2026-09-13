---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-013-5-integrability-of-funk-billiard-in-conics
section_title: "Integrability of Funk billiard in conics"
section_number: 5
pages: 18-22
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
---
Recall that by Example 4.2, the reﬂection laws of the Bn-Funk and Beltrami-
Klein hyperbolic metrics coincide. Similarly, the Funk geodesics on a manifold
M⊂ int(Bn) are also those of the metric induced from hyperbolic space.
19 A Funk perspective on billiards, projective geometry and Mahler volume
In particular, if K is an ellipsoid nested in Bn, the Funk billiard in K is com-
pletely integrable [34, 28]. We now recover and reﬁne this observation in the case
of the projective plane by analyzing the Funk billiard directly. Let K⊂ int(B) be
nested conics in P2.
Theorem 5.1. Any given orbit in FunkB(K) remains tangent to a conic Qi, while
the points of the outer orbit all lie on a conic Qo. Furthermore, Qo belongs to the
linear pencil of conics deﬁned by QK =∂K,QB =∂B, while Qi belongs to the dual
pencil. Moreover, the quadruplet Qi,QK,QB,Qo is harmonic.
Proof. We ﬁrst observe that by Proposition 4.3, the existence of an inner caustic
implies the existence of an outer caustic and vice versa. Moreover, the outer caustic
belongs to the linear pencil of QK,QB if and only if the inner caustic lies on the
dual pencil.
Let us establish the existence of an outer caustic which belongs to the linear
pencil through QK and QB. We may assume B is the unit disc. By applying
a projective transformation preserving B, we may further assume that QK is a
centered ellipse, that is QK ={q :⟨Aq,q⟩ = 1}. Consider a point z0∈Bc, and let
z1 be its image under the outer Funk billiard map. Eachzj belongs to a unique conic
in the linear pencil, which is parametrized by t∈ R,Qt :={⟨(A +tI)v,v⟩ = 1 +t}.
It remains to show that t1 =t2, or equivalently
⟨Az0,z 0⟩− 1
1−|z0|2 =⟨Az1,z 1⟩− 1
1−|z1|2 . (4)
Let p0∈QB be the tangency point of [z0,z 1]. Denoting ‖v‖A :=⟨Av,v⟩, we have
|z0|2− 1
|z1|2− 1 =|z0−p0|2
|z1−p|2 =‖z0−p0‖2
A
‖z1−p0‖2
A
,
the last inequality due to the fact that z0,pp 0,z 1 lie on one line. Similarly,
⟨Az0,z 0⟩− 1
⟨Az1,z 1⟩− 1 =‖z0−q0‖2
A
‖z1−q1‖2
A
.
Thus (4) becomes
‖z0−q0‖A
‖z0−p0‖A
=‖z1−q1‖A
‖z1−p0‖A
⇐⇒ sin∡Az0q0p0
sin∡Az0p0q0
= sin∡Az1q1p0
sin∡Az1p0q1
,
where∡A is the angle with respect to ‖•‖ A. As ∡Az0p0q0 +∡Az1p0q1 = π, it
remains to notice that ∡Az0q0p0 = 1
2∡Aq0oq1 =∡Az1q1p0.
p0
QK
QB
Qt
z0
z1
q1
q0
o
Figure 7. Outer caustic
20 A Funk perspective on billiards, projective geometry and Mahler volume
For the last statement, we consider a point z∈ Qt, tangent to QB at p and to
QK at q as in ﬁgure 8.
p
QK
QB
Qt
z
q
Figure 8. Relating the inner and outer caustics
Deﬁne the conic Q byQ−1 := (Q−1
B Qo)Q−1
K . To show that Qi =Q, we ought to
prove thatp−q is tangent to Q. Now the line through p,q is represented in R3 by
w := (p, 1)× (p−q, 0) = (J(p−q), det(p,p−q)), where J is the counterclockwise
rotation by π
2 . It remains to check that
⟨Q−1w,w⟩ = 0 ⇐⇒ ⟨(I +tA−1)J(p−q),J (p−q)⟩− (1 +t) det(p,p−q)2 = 0.
Putting t =−⟨Az,z⟩−1
|z|2−1 and z =p +sJp =q +rJAq for some s,r∈ R, we ﬁnd
|z|2− 1 =s2, ⟨Az,z⟩ = 1 +r2⟨AJAq,JAq⟩.
Since det(p,p−q)2 +⟨p,p−q⟩2 =|p−q|2, the claimed equality becomes
s2⟨p,p−q⟩2 =r2‖JAq‖2
A(‖J(p−q)‖2
A−1− det(p,p−q)2).
The left hand side can be rewrriten as
⟨sp,p−q⟩2 =⟨sJp,J (p−q)⟩2 =⟨z−p,J (p−q)⟩2 =
⟨z−q,J (p−q)⟩2 =r2⟨JAq,J (p−q)⟩2 =r2⟨Aq,p−q⟩2.
It thus remains to check that whenever |p| = 1 and⟨Aq,q⟩ = 1, one has
⟨Aq,p−q⟩2 =‖JAq‖2
A(‖J(p−q)‖2
A−1− det(q,p−q)2).
We can write
‖J(p−q)‖2
A−1− det(q,p−q)2 =‖J(p−q)‖2
A−1−⟨J(p−q),q⟩2
=‖J(p−q)‖2
A−1−⟨Aq,J (p−q)⟩2
A−1
=⟨J(p−q),ν⟩2
A−1
where ν = Jq
‖Jq‖A−1
, since‖Aq‖2
A−1 =⟨A−1Aq,Aq⟩ = 1 and⟨ν,Aq⟩A−1 = 0.
It remains to check that
‖Jq‖A−1⟨JAq,J (p−q)⟩ =‖JAq‖A⟨A−1Jq,J (p−q)⟩,
or equivalently that
‖Jq‖A−1JAq =‖JAq‖AA−1Jq.
21 A Funk perspective on billiards, projective geometry and Mahler volume
If JAq =λA−1Jq then
λ = ‖JAq‖A
‖A−1Jq‖A
=‖JAq‖A
‖Jq‖A−1
,
so it remains to check that JA andA−1J, or equivalently AJA andJ, are propor-
tional. Both are anti-symmetric 2 × 2 matrices, and so that must be the case.
□
Remark 5.2. When K approaches B, Qi and Qo become polars of one another
with respect to ∂B.
6. Sch¨affer’s dual girth conjecture
The Gutkin-Tabachnikov duality of Minkowski billiards has a continuous coun-
terpart, namely Sch¨ aﬀer’s dual girth conjecture [26], which is a theorem of´Alvarez
Paiva [1]. The setting of Funk geometry is no diﬀerent, providing another collection
of projective invariants enjoying duality.
Theorem 6.1. LetL be a smooth, strictly convex body in Pn.
i) Let M ⊂ int(L) be a compact submanifold with boundary, and consider
Funkη
L(M). Then its Holmes-Thompson volume, its geodesics and the length
of closed geodesics are all independent of η, and thus constitute projective
invariants of (M,L ).
ii) IfK⊂ int(L) is strictly convex, then FunkL(∂K) and RFunkK∨(∂L∨) have
the same Holmes-Thompson volumes and length spectra.
Proof. The ﬁrst claim follows immediately by Proposition 3.7 and Lemma 3.2, as
the Funk metric induces on M a projectively-invariant exact co-nomadic Finsler
structure.
For the second claim, we follow closely the proof in [1]. Write for simplicity ∂K
for Funkη
L(∂K), and similarly ∂L∨ for RFunkθ
K∨(∂L∨).
Deﬁne a smooth embedding Φ η : S∗∂K → ∂K×∂L∨ as follows. Let πx :
T∗
xK→ T∗
x∂K be the natural projection. Recall that by Proposition 3.4, S∗
xK =
Hη(x×∂L∨), where Hη : K×L∨→ T∗K is given by eq. (3). Now πx(S∗
xK) =
B∗
x∂K, and S∗
x∂K is diﬀeomorphic to its preimage under πx, namely the shadow
boundary Zx⊂ S∗
xK. Denote τx = π−1
x : S∗
x∂K→ Zx, and deﬁne τη : S∗∂K→
S∗K, (x,ξ′)↦→ (x,τx(ξ′)). Set
Φη(x,ξ′) =H−1
η ◦τη(x,ξ′).
Let us describe the image of Φ η. It holds that ( x,ξ )∈ Im(Φη) if and only if the
restricted projection πx : TξS∗
xK→ T∗
x∂K is not an isomorphism, or equivalently
if the natural pairing Tx∂K⊗Tξ∂L∨ → R is degenerate. The latter pairing is
induced from the natural non-degenerate pairing TxP⊗TξP∨→ R, which is given
by identifyingξ =x∗, (x⊥)∗ =ξ⊥, so that TxP =x∗⊗ (x⊥)∗ =ξ⊗ξ⊥ =T∗
ξ P∨. In
particular, Im(Φη) does not depend on η.
Turning to the dual manifold, deﬁne Φθ =Hθ
−1
◦τθ :S∗∂L∨→∂K×∂L∨ in full
analogy with Φη. Observe that the images of the two maps Φη, Φθ coincide by their
common description as the degeneracy locus of the pairing Tx∂K⊗Tξ∂L∨→ R.
Let α1 be the canonical contact form on S∗∂K, and α1 that of S∗∂L∨. Deﬁne
αη = (Φ−1
η )∗α1∈ Ω1(Im(Φη)) and αθ = (Φ
−1
θ )∗α1∈ Ω1(Im(Φη)), which coincide
22 A Funk perspective on billiards, projective geometry and Mahler volume
with the restriction to Im(Φ η) of the corresponding 1-forms on ∂K×∂L∨ in the
proof of Theorem 4.5, in particular by that proof αη−αθ is an exact form.
We now have
volHT (FunkL(∂K)) =
∫
S∗∂K
(dα1)n−2∧α1 =
∫
Im(Φη)
dαn−2
η ∧αη
=
∫
Im(Φθ)
dαn−2
θ ∧αθ = volHT (FunkK∨(∂L∨)).
Similarly, the length spectrum of Funk η
L(∂K) coincides with the action spectrum
of αη on Im(Φη), which is also the action spectrum of αθ. □
We remark that the Holmes-Thompson volumes of FunkL(∂K) and RFunkL(∂K)
trivially coincide.
Proof of Corollary 2. This follows at once from Theorem 6.1, since the Hilbert
length of a curve coincides with its 1-dimensional Funk Holmes-Thompson volume.
□.
