---
doc_id: arxiv-hep-th-9211141v1
doc_title: "arXiv:hep-th/9211141v1 1 Dec 1992"
section_id: sec-000-1-introduction-and-summary-of-results
section_title: "INTRODUCTION AND SUMMARY OF RESULTS"
section_number: 1
pages: 2-4
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-th/9211141v1 1 Dec 1992 — 17 sections: Front matter; INTRODUCTION AND SUMMARY OF RESULT; The System of Partial Differential"
---
[]{#sec:intro_summary label="sec:intro_summary"}

##  Introduction {#subsec:intro}

In this paper we present new results for the *level spacing distribution functions* obtained from scaling random matrix models of $N\times N$ hermitian matrices at the edge of the support of the (tree-level) eigenvalue densities when the parameters of the potential $V$ are not "finely tuned." This universality class is already present in the Gaussian Unitary Ensemble. It is known [@bowick_brezin; @forrester; @mehta_book; @moore] that these distribution functions are expressible in terms of a Fredholm determinant of an integral operator $K$ whose kernel involves Airy functions.

It turns out that there are striking analogies between the properties of this *Airy kernel* $$K(x,y) = {A(x) A^\prime(y) - A^\prime(x) A(y) \over x-y}$$ where $A(x) = \sqrt{\lambda}\> {\rm Ai}(x)$, and the *sine kernel* $${\lambda\over \pi}\> {\sin\pi(x-y)\over x-y} \, ,$$ whose associated Fredholm determinant describes the classical level spacing distribution functions first studied by Wigner, Dyson, Mehta, and others [@dyson62a; @mehta_book; @porter].

To be a little more explicit about how these kernels arise we remind the reader that in the GUE the probability density that the eigenvalues of a random $N\times N$ hermitian matrix lie in infinitesimal intervals about $x_1,\cdots, x_N$ is given by [@mehta_book] $$P_N(x_1,\cdots,x_N)={1\over N!} {\rm det}\left( K_N(x_i,x_j)\right)_{
i,j=1,\cdots,N}$$ where $$K_N(x,y)=\sum_{k=0}^{N-1} \varphi_k(x) \varphi_k(y) \, .$$ Here $\lbrace \varphi_k(x) \rbrace$ is the sequence obtained by orthonormalizing the sequence $$\left\lbrace x^k \exp (-x^2) \right\rbrace$$ over $(-\infty,\infty)$. More generally the $n$-point correlation function $R_n(x_1,\cdots,x_n)$, which is the probability density that $n$ of the eigenvalues (irrespective of order) lie in infinitesimal intervals about $x_1,\cdots,x_n$, is given by $$R_n(x_1,\cdots,x_n) ={\rm det}\left( K_N(x_i,x_j)\right)_{i,j=1,\cdots,n}$$ In particular $R_1(x)$, the density of eigenvalues at $x$, equals $K_N(x,x)$.

Replacing $K_N(x,y)$ by $${1\over R_1(z)} K_N\left(z+{x\over R_1(z)},z+{y\over R_1(z)}\right)$$ has the effect of making the point $z$ in the spectrum the new origin and rescaling so that the eigenvalue density at this point becomes equal to $1$. Now if $z$ is fixed then $$R_1(z)=K_N(z,z) \sim {1\over\pi}\sqrt{2N}$$ as $N\rightarrow\infty$, and $$\lim_{N\rightarrow\infty} {\pi\over \sqrt{2N}}
K_N\left(z+{\pi x\over \sqrt{2N}},z+{\pi y\over \sqrt{2N}}\right)=
{1\over\pi}\, {\sin\pi (x-y)\over  (x-y)}\, ,$$ so we obtain the sine kernel in this way.  (This limit is obtained by applying the Christoffel-Darboux formula to $K_N(x,y)$ and then using the known asymptotics of $\varphi_N(x)$ as $N\rightarrow\infty$.)  The "edge of the spectrum" corresponds to $z\sim\pm\sqrt{2N}$ and one has there the scaling limit [@forrester; @moore] $$\lim_{N\rightarrow\infty} {1\over 2^{1/2} N^{1/6}}
K_N\left(\sqrt{2N}+{x\over 2^{1/2} N^{1/6}},\sqrt{2N}+{y\over 2^{1/2} N^{1/6}}
\right)= {{\rm Ai}(x){\rm Ai}^\prime(y) - {\rm Ai}^\prime(x) {\rm Ai}(y)\over
x-y}\, .$$

We now present some of the analogies which we have found. (That such analogies between properties of the sine kernel and Airy kernel exist is perhaps not suprising since they are both scaling limits of the same family of kernels.)  The first is the analogue of the completely integrable system of P.D.E.'s of Jimbo, Miwa, Môri, and Sato [@jmms] when the underlying domain is a union of intervals. The second is the fact that in the case of the semi-infinite interval $(s,\infty)$ (the analogue of a single finite interval for the sine kernel) the Fredholm determinant is closely related to a Painlevé transcendent of the second kind (the fifth transcendent arises for the sine kernel [@jmms]). And the third is the existence of a second order differential operator commuting with the Airy operator $K$. (The existence of such a differential operator in the sine kernel case has been known for some time, see e.g. [@ince], page 201.) This last fact leads to an explicit asymptotic formula, as the interval $(s,\infty)$ expands, for the probability that it contains precisely $n$ eigenvalues ($n=1,2,\ldots$) (the analogue of results in [@btw; @widom92]). Here are our results, stated in some detail. (A short announcement appears in [@tw2].)
