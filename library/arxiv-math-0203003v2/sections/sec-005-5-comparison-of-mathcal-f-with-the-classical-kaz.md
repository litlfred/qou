---
doc_id: arxiv-math-0203003v2
doc_title: "arXiv:math/0203003v2 [math.QA] 24 Apr 2002"
section_id: sec-005-5-comparison-of-mathcal-f-with-the-classical-kaz
section_title: "Comparison of $\mathcal F$ with the classical Kazhdan-Lusztig functor"
section_number: 5
pages: 10-11
source_pdf: 0203003v2.pdf
source_sha256: 7579ae76959396b8
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 1.0
doc_brief: "arXiv:math/0203003v2 [math.QA] 24 Apr 2002 — 8 sections: Front matter; Introduction; Representations of Quantum Dynamic"
---
The sense in which the functor $\text{$\mathcal{F}$}$ is a q-analog of the Kazhdan-Lusztig functor is not straightforward, and needs to be explained.

Indeed, the Kazhdan-Lusztig functor is a functor from the fusion category of representations of an affine Kac-Moody algebra $\widehat{\mathfrak{g}}$ at some level $k$ to the category of representations of the quantum group $U_v(\mathfrak{g})$, where $v=e^{\frac{\pi i}{{\rm m}(k+h^\vee)}}$. On the other hand, in this paper we do not seem to be considering any q-fusion categories.

Nevertheless, there is a sense in which $\text{$\mathcal{F}$}$ is a q-analogue of the Kazhdan-Lusztig functor. A two-line justification is that while the Kazhdan-Lusztig functor arises from the analysis of the monodromy of the Knizhnik-Zamolodchikov equations, the functor $\text{$\mathcal{F}$}$ arises in a similar way from the analysis of the monodromy of the quantum Knizhnik-Zamolodchikov equations. To some extent this is explained in [@FrRe92] and [@KaSo95]. However, let us give a somewhat more vivid explanation, in the special case $\mathfrak{g}=\frak{sl}_n$. This explanation uses the small elliptic quantum group of Tarasov and Varchenko.

Recall that the classical Kazhdan-Lusztig functor $\text{$\mathcal{F}$}_0$, essentially, does the following. Given a finite dimensional representation $V$ of $\mathfrak{g}$ and a (generic) level $k$, it introduces on $V$ an action of the quantum group $U_v(\mathfrak{g})$, with $v=e^{\frac{\pi i}{{\rm m}(k+h^\vee)}}$. More precisely, one first uses the exchange construction for $\widehat{\mathfrak{g}}$ at level $k$ to turn $V$ into a representation of the exchange dynamical quantum group $F_v(G)$, $G=SL_n$ (see [@EtVa99]), and then turns it into a representation of $U_v(\mathfrak{g})$ by sending the dynamical parameter to infinity.

On the other hand, given a (generic) level $k$ and a finite dimensional representation $V$ of $U_q(\mathfrak{g})$, the functor $\text{$\mathcal{F}$}$ introduces on $V$ an action of the elliptic quantum group $E_{\tau,\gamma/2}(\mathfrak{g})$, with $\tau=-\frac{(k+h^\vee)\log
  q}{\pi i}$, and $\gamma=\frac{\log q}{\pi i}$ (by first affinizing $V$ and then applying the functor $\text{$\mathcal{F}$}$).

Now, one may check using modular invariance of theta-functions that $E_{\tau,\gamma/2}(\mathfrak{g})$ is isomorphic to $E_{-1/\tau,\gamma/2\tau}(\mathfrak{g})$ (the corresponding dynamical R-matrices are gauge equivalent). Thus, $V$ becomes a representation of $E_{-1/\tau,\gamma/2\tau}(\mathfrak{g})$. This representation is easily seen to be an evaluation representation, i.e., it factors through the small elliptic quantum group $e_{-1/\tau,\gamma/2\tau}(\mathfrak{g})$ ([@TaVa01]).

Finally, we claim that if $k$ is fixed then the algebra $e_{-1/\tau,\gamma/2\tau}(\mathfrak{g})$ is a q-deformation of the exchange dynamical quantum group $F_{v}(G)$ (which allows us to regard $\text{$\mathcal{F}$}$ as a q-deformation of $\text{$\mathcal{F}$}_0$). Indeed, it is easy to check that as $\omega\to \infty$, $e_{\omega,a}(\mathfrak{g})$ degenerates into $F_{e^{-2\pi ia}}(G)$. Since we have $-1/\tau=\frac{\pi i}{(k+h^\vee)\log q}$, and $\gamma/2\tau=-\frac{1}{2(k+h^\vee)}$, the claim follows.
