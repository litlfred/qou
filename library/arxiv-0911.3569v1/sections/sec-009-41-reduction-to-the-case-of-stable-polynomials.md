---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-009-41-reduction-to-the-case-of-stable-polynomials
section_title: "Reduction to the case of stable polynomials."
section_number: 4.1
pages: 11-13
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
prove GWS for open circular regions, since a closed circular region is the intersection
of all the open circular regions which contain it. Second, it suﬃces to show that
for any g∈ C[x] of degree at most m, if deg(g) =m or A is convex, and z∈ Am is
such that Polmg(z) = 0, then there exists z∈ A such that g(z) = 0. This implies
the stated form of GWS by applying this special case to g(x) = f(x)−c, where
c = Polmf(z). Stated otherwise, it suﬃces to show that if f(z)⁄= 0 for all z∈ A
then Polmf(z)⁄= 0 for all z∈ Am (provided that either deg(f) =m or A is convex).
Let M be the set of M¨ obius transformationsz↦→φ(z) = (az +b)/(cz +d) with
a,b,c,d ∈ C andab−cd =±1. Then M with the operation of functional composition
is a group of conformal transformations of the Riemann sphere ˆC = C∪{∞} ,
12 DAVID G. WAGNER
Figure 1. Illustration of the Grace-Walsh-Szeg˝ o Theorem.
and it acts simply transitively on the set of all ordered triples of distinct points
of ˆC. Consequently, for any open circular region A there is a φ∈ M such that
φ(H) ={φ(z) : z∈ H} = A. We henceforth regard circular regions as subsets of
ˆC. Note that an open circular region A is convex if and only if it does not contain
∞. (The point ∞ is on the boundary of any open half-plane.) In this case, if
φ(z) = (az +b)/(cz +d) is such that φ(H) = A then cz +d⁄= 0 for all z∈ H.
Given 0 ⁄≡ f ∈ C[x] of degree at most m, consider the polynomial ~f(x) =
(cx +d)mf((ax +b)/(cx +d)). If either deg( f) = m or A is convex, then f is
nonvanishing on A if and only if ~f(z) is nonvanishing on H. Also,
Polm~f(x) = Polmf(φ(x1),...,φ (xm))·
m∏
i=1
(cxi +d).
Thus, to prove GWS it suﬃces to prove the following lemma.
Lemma 4.2. Letf∈ C[x] be a univariate polynomial of degree at most m. Then
Polmf is stable if and only if f is stable.
Clearly, diagonalization implies that if Polmf is stable then f is stable, so only the
converse implication needs proof. This is accomplished in the following two easy
steps.
MULTIVARIATE STABLE POLYNOMIALS 13
