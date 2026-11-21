---
doc_id: arxiv-1208.2521v1
doc_title: "ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS"
section_id: page-008
section_title: "Page 8"
section_number: null
pages: 8-8
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
toc_source: undetermined
doc_brief: "ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
8
TOM H. KOORNWINDER AND REN´E F. SWARTTOUW
3. Some limit transitions
Jacobi polynomials tend to Bessel functions:
P (α,β)
nN
(1 −x2/(2N 2))
P (α,β)
nN
(1)
= 2F1(−nN, nN + α + β + 1; α + 1; x2/(4N 2))
N→∞
−−−−→0F1(−; α + 1; −(λx/2)2) = (λx/2)−α Γ(α + 1) Jα(λx),
where nN/N tends to λ for N →∞. When this limit transition is applied to the
formula which recovers a function from its Fourier-Jacobi coeﬃcients, we obtain,
at least formally, Hankel’s Fourier-Bessel integral (1.9).
The q-analogue of this limit transition starts with the little q-Jacobi polynomials
pn(x; a, b; q) := 2φ1(q−n, abqn+1; aq; q, qx),
which satisfy orthogonality relations
(3.1)
(qa, qb; q)∞
(q, q2ab; q)∞
∞
X
k=0
(pnpm)(qk; a, b; q) (qa)k (qk+1; q)∞
(qk+1b; q)∞
= (qa)n (1 −qab) (qb, q; q)n
(1 −q2n+1ab) (qa, qab; q)n
δnm,
where 0 < a < q−1, b < q−1 (see Andrews and Askey [2]).
It is clear that
pN−n(qNx; a, b; q) = 2φ1(q−N+n, abqN−n+1; aq; q, qN+1x)
tends formally (termwise) to 1φ1(0; aq; q, qn+1x) as N →∞. (See Proposition A.1
for a rigorous proof of this limit result.) Also, when we replace in (3.1) n, m, k by
N −n, N −m, N + k, respectively (so the sum runs from −N to ∞), and when
we let N →∞, we obtain as a formal (termwise) limit the orthogonality relations
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
∞
X
k=−∞
q(k+n)(α+1) (q2α+2; q2)∞
(q2; q2)∞
1φ1(0; q2α+2; q2, q2k+2n+2) f(qk),
f(qk) =
∞
X
n=−∞
q(k+n)(α+1) (q2α+2; q2)∞
(q2; q2)∞
1φ1(0; q2α+2; q2, q2k+2n+2) g(qn),
where f, g are L2-functions on the set {qk | k ∈Z} with respect to counting measure.
With the ad hoc notation
(3.3)
Jα(z; q2) := zα (q2α+2; q2)∞
(q2; q2)∞
1φ1(0; q2α+2; q2, q2 z2)
