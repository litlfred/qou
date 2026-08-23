---
doc_id: arxiv-math-9911033v1
doc_title: "On the lower bound estimates of sections of the canonical bundles over a Riemann surface"
section_id: sec-007-3-a-counterexample
section_title: "A counterexample"
section_number: 3
pages: 11-12
source_pdf: 9911033v1.pdf
source_sha256: 196c05d2e3419565
doc_brief: "On the lower bound estimates of sections of the canonical bundles over a Riemann surface — 18 sections: Introductions 1; A lower bound estimate 4; A counterexample 11"
---
In the last section, we give a lower bound estimate of (1.1) in terms of
the injective radius of M . In this section, we give a counterexample that
the uniform estimate is not true. More precisely, we are goin g to disapprove
the following:
Conjecture. LetKM be the canonical line bundle of a Riemann surface
M of genus g ≥ 2 and constant Gauss curvature ( −1). Then for m suﬃ-
ciently large, there is a number C(m,g ) > 0, depending only on m and g,
such that for any orthonormal basis S1, · · ·,S d of H 0(M,K m
M ), we have
inf
d∑
i=1
||Si||2 ≥C(m,g ).
In order to give the counterexample, we use the following Col lar Theorem
of Keen [7, p264]:
Theorem 3.1 (Keen). Consider the region T of U , the upper half plane,
bounded by the curve r = 1, r =el, θ =θ0 and θ =π −θ0. Let γ be a closed
geodesic on M with length l. Then there is a conformal isometric mapping
ϕ : T → M such that ϕ (iy) = γ. The image ϕ (T ) of T is called a collar.
Then we can choose θ0 small enough such that the area of the Collar is at
least 8
√
5 .
The following theorem gives the counterexample and implies Theorem 1.2:
Theorem 3.2. For any ε> 0 andm ≥ 2, there is a Riemann surface M of
constant curvature (−1) and genus g ≥ 2 such that there is a point x0 ∈M
satisfying
||S||(x0) ≤ε
for any S ∈H 0(M,K m
M ) with ||S||L2 = 1.
The idea of the proof is that when the length of a closed geodes ic line
tends to zero, the collar will be longer and longer in order to keep the area
of the collar having a lower bound. Topologically, a collar i s a cylinder. By
expanding the functions on the corollary using the Fourier s eries, we can ﬁnd
the suitable x0 and the estimates. We begin by discussing some elementary
properties of a collar.
11
Let R > 0 be a large real number. Let ( ρ,θ ) ∈ (−R,R ) × R. Let the
group Z acting on the space ( −R,R ) × R by
(n,ρ,θ ) ↦→(ρ,θ +nδ)
for n ∈ Z, where δ >0 satisﬁes
δ sinhR =ε1(= 8√
5
).
as in Theorem 3.1. Deﬁne the metric
ds2 =dρ2 + (coshρ)2dθ2
on ( −R,R ) × R which descends to a metric on
C = (−R,R ) × R/ Z.
The curvature of the metric is ( −1). Note that on C, ρ is a global function
but θ is only locally deﬁned.
We call C a collar of parameter δ.
Let
{
x =θ
y = 2 arctaneρ − π
2.(3.1)
Deﬁne z =x +iy. Clearly z is not a global function of C. But it deﬁnes a
complex structure of C.
Let
w =e
2πi
δ (θ+2i(arctan eρ − π
4 )) =e
2πi
δ z.(3.2)
Then w is a global holomorphic function on C. Consequently
dz = δ
2πi
dw
w(3.3)
is a global holomorphic 1-form on C.
Let f be a holomorphic function on a neighborhood of
