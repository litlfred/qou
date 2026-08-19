---
doc_id: arxiv-math-9911033v1
doc_title: "ON THE LOWER BOUND ESTIMA TES OF SECTIONS OF THE CANONICAL BUNDLES OVER A RIEMANN SURF ACE ZHIQIN LU Contents 1. Introductions 1 2. A lower bound estimate 4 3. A counterexample 11 "
section_id: sec-008-c-then-f-is-a
section_title: "Then f is a"
section_number: C
pages: 12-14
source_pdf: 9911033v1.pdf
source_sha256: 196c05d2e3419565
doc_brief: "ON THE LOWER BOUND ESTIMATES OF SECTIONS OF THE CANONICAL BUNDLES OVER A RIEMANN SURFACE ZHIQIN LU Contents 1. Introductions 1 2. A lower bound estimate 4 3. A counterexample 11 4. Partial uniform est"
---
period function on [ −R,R ] × R, satisfying
f (ρ,θ ±δ) = f (ρ,θ ).
Let the Fourier expansion of f (−R,θ ) and f (R,θ ) be
f (−R,θ ) =
+∞∑
k=−∞
Ake
2πi
δ kθ;
f (R,θ ) =
+∞∑
k=−∞
Bke
2πi
δ kθ.
12
Deﬁne
g1 =
∞∑
k=1
Ake− 4π
δ k( π
4 −arctan e− R)wk,
g2 =B0,
g3 =
−1∑
k=−∞
Bke− 4π
δ k( π
4 −arctan eR)wk,
(3.4)
where w is in (3.2). We have the following lemma:
Lemma 3.1. With the notations as above, g1,g 2,g 3 are holomorphic func-
tions on C. Furthermore
f =g1 +g2 +g3.
Proof. g2 is a constant. So it is automatically holomorphic. By equa-
tion (3.2), we have
|w| ≤ e− 4π
δ (arctan eρ − π
4 ).
Thus we have
|g1| = |
∞∑
k=1
Ake− 4π
δ k( π
4 −arctan e− R)wk|
≤
∞∑
k=1
|Ak|e− 4π
δ k(arctan eρ −arctan e− R)
≤ (
∞∑
k=1
|Ak|2)
1
2 (
∞∑
k=1
e− 8π
δ k(arctan eρ −arctan e− R))
1
2.
By the Bessel inequality, we have
+∞∑
k=1
|Ak|2 ≤ 1
δ
∫
M
|f (−R,θ )|2dθ.
Thus if ρ > −R, the series is convergent absolutely. So g1 deﬁnes a holo-
morphic function on {−R<ρ<R }.
By the same argument, g3 is also holomorphic.
In order to prove that
f =g1 +g2 +g3,
we just need to prove that on the set {ρ = 0}, f =g1 +g2 +g3. Deﬁne
pk(ρ) =
∫ δ
0
f (ρ,θ )e− 2πi
δ θkdθ(3.5)
for k ∈ Z. Apparently
pk(R) = Bkδ, p k(−R) = Akδ
13
for k ∈ Z. By the deﬁnition of z in (3.1), we have
∂
∂z = 1
2 (
√
−1 coshρ ∂
∂ρ + ∂
∂θ ).
Using the equation ∂f
∂ z = 0, from (3.5), we have
p′
k = − 2πk
δ coshρpk.
Solving the above diﬀerential equation gives
pk(0) = Ake− 4π
δ k( π
4 −arctan e− R), k = 1, 2, · · ·,
p0(0) = B0,
pk(0) = Bke− 4π
δ k( π
4 −arctan eR), k = −1, −2, · · ·.
(3.6)
From (3.4) and (3.6), we see that
f |ρ=0 = (g1 +g2 +g3)|ρ=0.
Thus
f =g1 +g2 +g3
on C because both sides are holomorphic functions.
LetM be a Riemann surface of curvature ( −1) and genus g ≥ 2. Assume
that there is a closed geodesic γ onM such that length(γ) = δ >0. Assume
that δ is small enough. Let θ be the arc length parameter and ρ be the
distance function to the geodesic. Then
Lemma 3.2. (ρ,θ ) is the local coordinate system of M as long as
sinhρ ·δ ≤ε1 = 8
√
5
.
Proof. Note that the area of {−R0 <ρ<R 0} isδ sinhR0 for anyR0 > 0.
The lemma follows from Theorem 3.1.
LetC = {−R<ρ<R }, where R satisﬁes δ sinhR =ε1. Then z =x +iy
deﬁnes a complex structure of C where x and y are in (3.1). We have
Lemma 3.3. Either z =x +iy or z =x −iy is holomorphic on M .
Proof. A straightforward computation gives
ds2 = (coshρ)2dzdz.
Thus z deﬁnes a conformal structure which is the same as the one on M .
So either z or z is holomorphic.
Without losing generality, we assume that z is holomorphic. Fixing m ≥
