---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-003-22-elementary-properties
section_title: "Elementary properties."
section_number: 2.2
pages: 3-4
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
---
tivariate problems to be reduced to univariate ones, as will be seen.
Lemma 2.3. A polynomial f∈ C[x] is stable if and only if for all a, b∈ Rm with
b> 0, f(a + bt) is stable in S[t].
Proof. Since Hm ={a+bt : a, b∈ Rm, b> 0, andt∈ H}, the result follows. □
Forf∈ C[x] and i∈ [m], let degi(f) denote the degree of xi in f.
Lemma 2.4. These operations preserve stability of polynomials in C[x].
(a) Permutation: for any permutation σ : [m]→ [m], f↦→f(xσ(1),...,x σ(m)).
(b) Scaling: for c∈ C and a∈ Rm with a> 0, f↦→cf(a1x1,...,a mxm).
(c) Diagonalization: for{i,j}⊆ [m], f↦→f(x)|xi=xj .
(d) Specialization: for a∈ H, f↦→f(a,x 2,...,x m).
(e) Inversion: if deg1(f) =d, f↦→xd
1f(−x−1
1 ,x 2,...,x m).
(f) Diﬀerentiation (or “Contraction”): f↦→∂1f(x).
Proof. Parts (a,b,c) are clear. Part (d) is also clear in the case that Im( a)> 0. For
a∈ R apply part (d) with values in the sequence (a+i2−n : n∈ N), and then apply
Hurwitz’s Theorem to the limit as n→∞ . Part (e) follows from the fact that H is
invariant under the operationz↦→−z−1. For part (f), letd = deg1(f), and consider
the sequence fn = n−df(nx1,x 2,...,x m) for all n≥ 1. Each fn is stable and the
sequence converges to a polynomial, so the limit is stable. Since deg 1(f) =d, this
limit is not identically zero. This implies that for all z2,...,z m∈ H, the polynomial
g(x) = f(x,z 2,...,z m)∈ C[x] has degree d. Clearly g′(x) = ∂1f(x,z 2,...,z m). Let
ξ1,...,ξ d be the roots of g(x), so that g(x) =c∏d
h=1(x−ξh) for some c∈ C. Since
f is stable, Im(ξh)≤ 0 for all h∈ [d]. Now
g′(x)
g(x) = d
dx logg(x) =
d∑
h=1
1
x−ξh
.
4 DAVID G. WAGNER
If Im(z) > 0 then Im(1/(z−ξh)) < 0 for all h∈ [d], so that g′(z)⁄= 0. Thus, if
z∈ Hm then ∂1f(z)⁄= 0. That is, ∂1f is stable. □
Of course, by permutation, parts (d,e,f) of Lemma 2.4 apply for any index i∈ [m]
as well (not just i = 1). Part (f) is essentially the Gauss-Lucas Theorem: the roots
of g′(x) lie in the convex hull of the roots of g(x).
