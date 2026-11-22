---
doc_id: arxiv-1211.1525v2
doc_title: "PARTIAL TRANSPOSE OF RANDOM QUANTUM STATES: EXACT FORMULAS AND MEANDERS"
section_id: sec-016-appendix-b-measure-concentration
section_title: "Appendix B. Measure concentration"
section_number: null
pages: 29-29
source_pdf: 1211.1525v2.pdf
source_sha256: 51ff1c8f90c025a4
toc_source: outline
doc_brief: "PARTIAL TRANSPOSE OF RANDOM QUANTUM STATES: EXACT FORMULAS AND MEANDERS — We investigate the asymptotic behavior of the empirical eigenvalues distribution of the partial transpose of a random quantum"
---
APPENDIX B. MEASURE CONCENTRATION
In this section we collect some results from asymptotic geometric analy-
sis and random matrix theory, which we use in this paper.
The following theorem states that continuous functions on high-dimensional
unit spheres have almost constant value except for sets of small measure:
Lemma B.1 (Levy’s lemma [Lév51]). Let f : Sk →R be a function with
Lipschitz constant L, then there exists a constant 0 < c0 < 1 and
Pr{x ∈Sk : |f(x) −Median[f]| ≥ϵ} < exp
−c0(k −1)ϵ2
L2

.
It is well-known that singular values of random matrices of Gaussian
entries are asymptotically concentrated [MP67]. For example, a sharp esti-
mate is found in the proof of Lemma 7.3 in [HT03] and we restate it in our
setting:
Lemma B.2 (Haagerup, Thorbjørnsen). Let mn
l
= al and for ϵ > 0 we have
Pr
(
λmax(˜ρl) ≥1
l
"q
a−1
l
+ 1
2
+ ϵ
#)
≤all exp

−
allϵ2
4(a−1
l
+ 1)

.
Here, ˜ρl =
Wl
lmn and λmax(˜ρ) is the maximum eigenvalue of ˜ρ.
A similar phenomenon is also true even when they are normalized to have
the Hilbert-Schmidt norm one, and we have the following corollary:
Corollary B.3. Let mn
l
= al, which converges. Then, there exist two con-
stants c, C > 0 such that
Pr

λmax(ρl) ≥C
l

≤exp {−cl} .
for large enough l ∈N. Here, ρl =
Wl
Tr Wl.
