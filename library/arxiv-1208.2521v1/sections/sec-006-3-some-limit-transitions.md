---
doc_id: arxiv-1208.2521v1
doc_title: "On q-analogues of the Fourier and Hankel transforms"
section_id: sec-006-3-some-limit-transitions
section_title: "Some limit transitions"
section_number: 3
pages: 8-10
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
doc_brief: "On q-analogues of the Fourier and Hankel transforms — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
Jacobi polynomials tend to Bessel functions:
P (α,β )
nN (1 − x2/ (2N 2))
P (α,β )
nN (1)
= 2F1(−nN , n N + α + β + 1; α + 1; x2/ (4N 2))
N→∞
− − − − →0F1(−; α + 1; −(λx/ 2)2) = ( λx/ 2)− α Γ( α + 1) Jα (λx),
where nN /N tends to λ for N → ∞ . When this limit transition is applied to the
formula which recovers a function from its Fourier-Jacobi c oeﬃcients, we obtain,
at least formally, Hankel’s Fourier-Bessel integral (1.9) .
The q-analogue of this limit transition starts with the little q-Jacobi polynomials
pn(x; a, b ; q) := 2φ 1(q− n, abq n+1; aq; q, qx ),
which satisfy orthogonality relations
(3.1) (qa, qb ; q)∞
(q, q 2ab; q)∞
∞∑
k=0
(pnpm)(qk; a, b ; q) (qa)k (qk+1; q)∞
(qk+1b; q)∞
= (qa)n (1 − qab) (qb, q ; q)n
(1 − q2n+1ab) (qa, qab ; q)n
δnm,
where 0 < a < q − 1, b < q − 1 (see Andrews and Askey [2]).
It is clear that
pN− n(qN x; a, b ; q) = 2φ 1(q− N+n, abq N− n+1; aq; q, q N+1x)
tends formally (termwise) to 1φ 1(0; aq; q, q n+1x) as N → ∞. (See Proposition A.1
for a rigorous proof of this limit result.) Also, when we repl ace in (3.1) n, m, k by
N − n, N − m, N + k, respectively (so the sum runs from −N to ∞), and when
we let N → ∞ , we obtain as a formal (termwise) limit the orthogonality re lations
(2.11).
In order to see that (2.11) is a q-analogue of Hankel’s Fourier-Bessel integral
(1.9), rewrite (2.11) as the transform pair
(3.2)











g(qn) =
∞∑
k=−∞
q(k+n)(α +1) (q2α +2; q2)∞
(q2; q2)∞
1φ 1(0; q2α +2; q2, q 2k+2n+2) f (qk),
f (qk) =
∞∑
n=−∞
q(k+n)(α +1) (q2α +2; q2)∞
(q2; q2)∞
1φ 1(0; q2α +2; q2, q 2k+2n+2) g(qn),
where f, g are L2-functions on the set {qk | k ∈ Z} with respect to counting measure.
With the ad hoc notation
(3.3) Jα (z; q2) := zα (q2α +2; q2)∞
(q2; q2)∞
1φ 1(0; q2α +2; q2, q 2 z2)
ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS 9
(diﬀerent from Rahman’s proposal in [13, (1.13)]) and with t he replacement of
f (qk), g(qn) by qkf (qk), qng(qn) this becomes
(3.4)











g(qn) =
∞∑
k=−∞
q2k Jα (qk+n; q2) f (qk),
f (qk) =
∞∑
n=−∞
q2n Jα (qk+n; q2) g(qn).
Now observe that
Jα ((1 − q)z; q2) = (1 + q)− α zα
Γ q2 (α + 1) 1φ 1(0; q2α +2; q2, (1 − q2)2 (qz/ (1 + q))2)
converges, for q ↑ 1, to the Bessel function
Jα (z) = 2− α zα
Γ( α + 1) 0F1(−; α + 1; −z2/ 4),
where we used Proposition A.2 and the fact that
(1 − q2)α (q2α +2; q2)∞
(q2; q2)∞
= 1
Γ q2(α + 1) − → 1
Γ( α + 1)
as q ↑ 1, cf. Andrews [1, Appendix A], Koornwinder [11, Appendix B] . We can
apply this to (3.4) when we let q ↑ 1 under the side condition that log(1− q)
log q ∈ 2Z.
For such q we can replace qk, qn in (3.4) by (1 − q)1/ 2qk, (1 − q)1/ 2qn, and next
f ((1 − q)1/ 2qk), g((1 − q)1/ 2qn) by f (qk), g(qn). With the q-integral notation
∫ ∞
0
h(z) dqz := (1 − q)
∞∑
j=−∞
h(qj) qj,
(3.4) then takes the form







g(λ) =
∫ ∞
0
f (x) Jα ((1 − q)λx; q2) x dqx,
f (x) =
∫ ∞
0
g(λ) Jα ((1 − q)λx; q2) λ dqλ,
where λ in the ﬁrst identity and x in the second identity take the values qn, n ∈ Z.
For q ↑ 1 we obtain, at least formally, the Hankel transform pair







g(λ) =
∫ ∞
0
f (x) Jα (λx) x dx,
f (x) =
∫ ∞
0
g(λ) Jα (λx) λ dλ,
