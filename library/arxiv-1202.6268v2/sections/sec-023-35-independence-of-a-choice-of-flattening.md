---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-023-35-independence-of-a-choice-of-flattening
section_title: "Independence of a choice of flattening"
section_number: 3.5
pages: 19-19
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.895
latex_coverage_ratio: 1.0
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.invflat label="sec.invflat"}

Now suppose that we choose two flattenings $(f,f',f'')$ and $(\widetilde f,\widetilde f',\widetilde f'')$, both satisfying

$$\mathbf A  f  + \mathbf B f'' = \nu\,,\qquad 
f+ f'+ f''=1\,.$$

$$\mathbf A \widetilde f  + \mathbf B\widetilde f'' = \nu\,,\qquad 
\widetilde f+\widetilde f'+\widetilde f''=1\,.$$

We may assume that we have a quad type with $\mathbf B$ non-degenerate. Indeed, by the result of Section [\[sec.invgauge\]](#sec.invgauge){reference-type="ref" reference="sec.invgauge"}, flattening invariance in one quad type implies flattening invariance in any quad type. Moreover, by Lemma [\[lemma.B\]](#lemma.B){reference-type="ref" reference="lemma.B"} of Appendix [\[app.symp\]](#app.symp){reference-type="ref" reference="app.symp"}, a quad type with non-degenerate $\mathbf B$ always exists. We also note that when $\mathbf B$ is invertible the matrix $\mathbf B^{-1}\mathbf A$ is symmetric (Lemma [\[lemma.BA\]](#lemma.BA){reference-type="ref" reference="lemma.BA"}).

The determinant in $\tau_{\mathcal{T}}$ is insensitive to the change of flattening. The monomial, on the other hand, can be manipulated as follows. Let us choose logarithms $(Z,Z',Z'')$ of the shape parameters such that $\mathbf A Z+\mathbf B Z''=i\pi \nu$. Then, assuming that $\mathbf B$ is non-degenerate, we compute:

$$\begin{aligned}
 \frac{z^{\tilde f''}z''^{-\tilde f}}{z^{f''}z''{}^{-f}}
 &= \exp\big[ Z\cdot (f''-\widetilde f'')-Z''\cdot (f-\widetilde f) \big] \notag\\
 &= \exp\big[ -Z\cdot \mathbf B^{-1}\mathbf A(f-\widetilde f)
-(i\pi \mathbf B^{-1}\nu-\mathbf B^{-1}\mathbf A Z)\cdot (f-\widetilde f)\big] \notag\\
 &= \exp\big[-i\pi \mathbf B^{-1}\nu\cdot (f-\widetilde f)\big] \notag \\
 &= \exp\big[-i\pi f''\cdot(f-\widetilde f)
-i\pi \mathbf B^{-1}\mathbf A f\cdot(f-\widetilde f)\big] \notag\\
 &= \exp\big[-i\pi f''\cdot(f-\widetilde f)+i\pi  f\cdot(f''-\widetilde f'')\big] \notag \\
 &= \exp\big[i\pi (f''\cdot \widetilde f- f\cdot\widetilde f'')\big] = \pm 1\,. \notag
\end{aligned}$$

Therefore, the monomial can change at most by a sign, and $\tau_{\mathcal{T}}$ is invariant as desired.

This completes the proof of Theorem [\[thm.indep\]](#thm.indep){reference-type="ref" reference="thm.indep"}. 0◻
