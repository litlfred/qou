---
doc_id: arxiv-1203.6551v1
doc_title: "On the number of hyperbolic 3-manifolds of a given volume"
section_id: sec-008-9-some-open-questions
section_title: "Some Open Questions"
section_number: 9
pages: 23-24
source_pdf: 1203.6551v1.pdf
source_sha256: a8e84f8ed63dbcca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.89
latex_coverage_ratio: 0.992
doc_brief: "On the number of hyperbolic 3-manifolds of a given volume — The work of Jørgensen and Thurston shows that there is a ﬁnite number N(v) of orientable hyperbolic 3-manifolds with any given volume v."
---
1.  Find additional exact values of $N(v)$ or upper bounds on $N(v)$.

2.  (Gromov [@Gr], 1979) Is $N(v)$ locally bounded?

    This reduces to the question of whether the number of manifolds with a given volume $v$ is uniformly bounded amongst all hyperbolic Dehn fillings on any given cusped hyperbolic 3-manifold.

3.  What is the largest volume $< v_\omega= 2.029883\ldots$ of a closed hyperbolic 3-manifold that does not arise from Dehn filling of $m004$ or $m003$? (This would allow us to make the result of Theorem [\[closed_unique\]](#closed_unique){reference-type="ref" reference="closed_unique"} explicit.)

    Experimental evidence suggests that the largest such volume is $2.028853\ldots$ for the closed manifold $m006(-5,2)$. (This is the largest such volume arising in the Hodgson-Weeks census of low volume closed hyperbolic 3-manifolds with shortest closed geodesic of length $>0.3$, and also for Dehn fillings on the "magic manifold" s776.)

4.  \(i\) Are all hyperbolic Dehn fillings on $m004$ determined by their volumes, amongst Dehn fillings on $m004$?\
    (ii) Are all hyperbolic Dehn fillings on $m003$ determined by their volumes, amongst Dehn fillings on $m003$?\
    (iii) There are some equalities between volumes of Dehn fillings on $m003$ and $m004$, observed in [@HMW], and shown in equation ([\[eq26\]](#eq26){reference-type="ref" reference="eq26"}) above. Explicitly, for all pairs of relatively prime integers $p,q$ with $p$ a multiple of $4$, the manifolds $m004(p,q)$ and $m003(-p/2-q,2q)=m003(p/2-q,2q)$ are not homeomorphic, but have a common 2-fold cover so have equal volumes. \*\*check this -- describe change in peripheral curves from WL(-5,1) to m003\*\* The Meyerhoff manifold of volume $0.981368\ldots$ also arises as Dehn filling on both: $m004(5,1)=m003(-2,3) = m003(-1, 3)$. Are these the only equalities between volumes of Dehn fillings on $m003$ and $m004$?

    (These statements can be checked experimentally using SnapPy and Snap: for instance they are true for all hyperbolic Dehn fillings on $m003$ and $m004$ with $\text{volume} < 2.0289$.)

5.  For which cusped hyperbolic 3-manifolds $N$ are there infinitely many hyperbolic Dehn fillings on $N$ that are uniquely determined by their volumes amongst Dehn fillings on $N$?

    Our methods give some further results on this question when the cusp shape $\tau$ lies in an imaginary quadratic number field. But for $\tau$ algebraic of higher degree, our approach would require new results on the distribution of gaps in the values of the quadratic form $Q(a,b) =|a+ b \tau|^2$ for integers $a,b$. This question also arises in the subject of "Quantum Chaos", and it is conjectured that the successive gaps should be randomly distributed according to a Poisson distribution (see [@sarnak], [@rudnick], [@EMM]). This would imply that arbitrarily large 2-sided gaps always exist.

6.  Are there sequences $x_i \to \infty$ with $N(x_i)=1$ for all $i$?

7.  Are there sequences $x_i \to \infty$ such that the growth rate of the number $N_L(x_i)$ of link complements with volume $x_i$ is faster than exponential, i.e with $\displaystyle\limsup_{i\to \infty} {\log N_L(x_i) \over \log x_i} = +\infty$?
