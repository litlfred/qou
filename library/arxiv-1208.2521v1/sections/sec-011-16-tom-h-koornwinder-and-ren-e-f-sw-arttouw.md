---
doc_id: arxiv-1208.2521v1
doc_title: "On q-analogues of the Fourier and Hankel transforms"
section_id: sec-011-16-tom-h-koornwinder-and-ren-e-f-sw-arttouw
section_title: "TOM H. KOORNWINDER AND REN ´E F. SW ARTTOUW"
section_number: 16
pages: 16-18
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
doc_brief: "On q-analogues of the Fourier and Hankel transforms — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
for the q-derivative, we obtain from (5.1) and (5.3) that
(1 − q) Dq,z cos(z; q2) = −q sin(qz; q2),
(1 − q) Dq,z sin(z; q2) = cos( z; q2).
Hence
(1 − q)2 (D2
q f )(q− 1z) =
{ −q2 λ 2 f (z) if f (z) = cos( λz ; q2),
−q λ 2 f (z) if f (z) = sin( λz ; q2).
So the two systems of functions z ↦→cos(qnz) ( n ∈ Z) and z ↦→sin(qnz) ( n ∈ Z)
have disjoint eigenvalues with respect to the operator whic h sends f to the function
z ↦→(1 − q)2 (D2
q f )(q− 1z) = q z− 2(
q f (q− 1z) − (1 + q) f (z) + f (qz)
)
.
This operator has also the selfadjointness property
∞∑
k=−∞
qk (D2
q f )(qk− 1) g(qk) =
∞∑
k=−∞
qk f (qk) (D2
q g)(qk− 1)
for f , g of ﬁnite support on {qk | k ∈ Z}.
Observe that the q-deformation of d2/dx 2 considered above yields a symmetry
breaking. The two-dimensional eigenspaces of d2/dx 2 are broken apart into one-
dimensional eigenspaces. Therefore it does not seem to be ve ry useful to consider a
q-exponential built from the functions deﬁned by (5.1) and (5 .3). Any linear com-
bination f (z) of cos( λz ; q2) and sin( λz ; q2) will no longer satisfy an eigenfunction
equation
(5.6) (1 − q)2 (D2
q f )(q− 1z) = µ f (z),
while the nice function
f (z) := 1φ 1(0; −q1/ 2; q1/ 2, ±iq3/ 4λz ) = cos( λz ; q2) ∓ iq1/ 4 sin(q1/ 2λz ; q2)
(cf. Exton [4, 5.2.2.1]), which satisﬁes (5.6) with µ = −q2λ 2, no longer remains
within the spectral decompositions implied by (5.5).
Appendix A. Rigorous proofs of some limit results
In this Appendix we will give proofs of the limit transitions from little q-Jacobi
polynomials to q-Bessel functions and from q-Bessel functions to ordinary Bessel
functions.
ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS 17
Proposition A.1. For 0 < a < q − 1, 0 ≤ b < q − 1 we have
lim
n→∞ 2φ 1(q− n, q n+1ab; qa; q, q nx) = 1φ 1(0; qa; q, x ),
uniformly for x in compact subsets of C.
Proof. Put
Rn(x) := 2φ 1(q− n, q n+1ab; qa; q, q nx) − 1φ 1(0; qa; q, x )
=
∞∑
k=1
(−1)k qk(k− 1)/ 2 xk
(qa; q)k (q; q)k
(
−1 +
k∏
j=1
(1 − qn− j+1) (1 − qn+j ab)
)
.
Since
k∏
j=1
(1 − xj) ≥ 1 −
k∑
j=1
xj if 0 ≤ xj ≤ 1, j = 1, . . . , k ,
we have
⏐
⏐
⏐
⏐−1 +
k∏
j=1
(1 − qn− j+1) (1 − qn+jab)
⏐
⏐
⏐
⏐ ≤
k∑
j=1
qn− j+1 +
k∑
j=1
qn+j ab
≤ qn− k+1(1 + ab)
1 − q
if k ≤ n, while the left-hand side is equal to 1 otherwise. Thus, for |x| ≤ M :
|Rn(x)| ≤ qn+1(1 + ab)
1 − q
∞∑
k=1
qk(k− 1)/ 2 q− kM k
(qa; q)k (q; q)k
+
∞∑
k=n+1
qk(k− 1)/ 2 M k
(qa; q)k (q; q)k
,
which tends to 0 as n → ∞. □
Proposition A.2. For α > −1 we have
lim
q↑1 1φ 1(0; qα +1; q, (1 − q)2z) = 0F1(−; α + 1; −z),
uniformly for z in compact subsets of C.
Proof.
1φ 1(0; qα +1; q, (1 − q)2z) =
∞∑
k=0
(−1)k qk(k− 1)/ 2 (1 − q)2k zk
(qα +1; q)k (q; q)k
and the summand in the sum at the right-hand side can be majori zed by
(A.1) ( q− α/ 2|z|)k
k− 1∏
j=0
(q(α +j)/ 2 − q1+(α +j)/ 2) (qj/ 2 − q1+j/ 2)
(1 − q1+α +j) (1 − q1+j) .
