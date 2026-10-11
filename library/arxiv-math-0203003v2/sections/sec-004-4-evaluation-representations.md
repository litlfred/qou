---
doc_id: arxiv-math-0203003v2
doc_title: "arXiv:math/0203003v2 [math.QA] 24 Apr 2002"
section_id: sec-004-4-evaluation-representations
section_title: "Evaluation Representations"
section_number: 4
pages: 10-11
source_pdf: 0203003v2.pdf
source_sha256: 7579ae76959396b8
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.982
---
In this section we would like to study the action of the functor $\text{$\mathcal{F}$}$ on evaluation representations of $U_q(\widehat{\mathfrak{s}}l_n)$. Let $W_\nu(z)$ be the evaluation representation of $U_q({\widehat{\mathfrak{s}}l}_n)$ with dominant integral highest weight $\nu$, evaluated at $z\in \text{$\mathbb{C}$}^*$.

::: prop
The representation ${\text{$\mathcal{F}$}}(W_\nu(z))$ is isomorphic to the evaluation representation $V_\mu(z)$ of the elliptic quantum group defined in [@TaVa01] (see Corollary 3.4 and Theorem 5.9), tensored with a 1-dimensional representation.
:::

::: proof
*Proof.* Similarly to quantum affine algebra, for elliptic quantum group there is a natural notion of a highest weight for a finite dimensional representation $W$ (it was studied in detail in [@Ca01]). Namely, the highest weight is, essentially, the set of eigenvalues of the diagonal entries of the noncommutative matrix $L_W(u,\hat\lambda)$ on the highest weight vector.

It is not difficult to compute highest weights of representations ${\text{$\mathcal{F}$}}(W_\nu(z))$ and show that they coincide with highest weights of $V_\nu(z)$ up to tensoring with a 1-dimensional representation. Namely one needs to prove this statement for the fundamental representations (exterior powers), since for other representations the statement follows by taking tensor products.

To prove the statement for exterior powers, one first proves it for the vector representation $V$, in which case it is trivial, since it reduces to analyzing entries of $R_V$. To pass to an arbitrary exterior power, one may use fusion procedure (i.e. the fact that $\Lambda^iV$ is contained in the product of $i$ copies of $V$ with appropriate shifts).

Now, it was shown in [@Ca01] that if two irreducible highest weight finite dimensional representations of the elliptic quantum group have the same highest weight, then they are isomorphic. This completes the proof. ◻
:::

It is clear that the functor $\mathcal F$ extends naturally to a tensor functor $\text{\bf Rep}_{\text{$\mathcal{O}$}}(U_q({\widehat{\mathfrak{s}}l}_n))\otimes_{\text{$\mathbb{C}$}}M_V\to 
\text{\bf Rep}_{\text{$\mathcal{O}$}}(R_{\tau,\gamma}^{ell})$ between the categories $\mathcal O$ of representations of the quantum affine algebra, respectively the elliptic quantum group (i.e. categories of representations whose $\mathfrak{h}$-weight multiplicities are finite, and the multiplicity function is supported on a finite union of sets of the form $\mu-Q_+$, where $Q_+$ is the positive cone in the root lattice of $\mathfrak{g}$). Namely, the construction of $\mathcal F$ we gave generalizes to this case in a straighforward way. Moreover, it is not hard to see that after this extension the functor remains fully faithful (the proof of full faithfulness also generalizes without significant changes). In particular, we see that any evaluation module for $U_q({\widehat{\mathfrak{s}}l}_n)$ admits an elliptic deformation. This was conjectured in [@TaVa01], and the conjecture was checked for Verma modules and finite dimensional representations.

# Comparison of $\mathcal F$ with the classical Kazhdan-Lusztig functor

The sense in which the functor $\text{$\mathcal{F}$}$ is a q-analog of the Kazhdan-Lusztig functor is not straightforward, and needs to be explained.

Indeed, the Kazhdan-Lusztig functor is a functor from the fusion category of representations of an affine Kac-Moody algebra $\widehat{\mathfrak{g}}$ at some level $k$ to the category of representations of the quantum group $U_v(\mathfrak{g})$, where $v=e^{\frac{\pi i}{{\rm m}(k+h^\vee)}}$. On the other hand, in this paper we do not seem to be considering any q-fusion categories.

Nevertheless, there is a sense in which $\text{$\mathcal{F}$}$ is a q-analogue of the Kazhdan-Lusztig functor. A two-line justification is that while the Kazhdan-Lusztig functor arises from the analysis of the monodromy of the Knizhnik-Zamolodchikov equations, the functor $\text{$\mathcal{F}$}$ arises in a similar way from the analysis of the monodromy of the quantum Knizhnik-Zamolodchikov equations. To some extent this is explained in [@FrRe92] and [@KaSo95]. However, let us give a somewhat more vivid explanation, in the special case $\mathfrak{g}=\frak{sl}_n$. This explanation uses the small elliptic quantum group of Tarasov and Varchenko.

Recall that the classical Kazhdan-Lusztig functor $\text{$\mathcal{F}$}_0$, essentially, does the following. Given a finite dimensional representation $V$ of $\mathfrak{g}$ and a (generic) level $k$, it introduces on $V$ an action of the quantum group $U_v(\mathfrak{g})$, with $v=e^{\frac{\pi i}{{\rm m}(k+h^\vee)}}$. More precisely, one first uses the exchange construction for $\widehat{\mathfrak{g}}$ at level $k$ to turn $V$ into a representation of the exchange dynamical quantum group $F_v(G)$, $G=SL_n$ (see [@EtVa99]), and then turns it into a representation of $U_v(\mathfrak{g})$ by sending the dynamical parameter to infinity.

On the other hand, given a (generic) level $k$ and a finite dimensional representation $V$ of $U_q(\mathfrak{g})$, the functor $\text{$\mathcal{F}$}$ introduces on $V$ an action of the elliptic quantum group $E_{\tau,\gamma/2}(\mathfrak{g})$, with $\tau=-\frac{(k+h^\vee)\log
  q}{\pi i}$, and $\gamma=\frac{\log q}{\pi i}$ (by first affinizing $V$ and then applying the functor $\text{$\mathcal{F}$}$).

Now, one may check using modular invariance of theta-functions that $E_{\tau,\gamma/2}(\mathfrak{g})$ is isomorphic to $E_{-1/\tau,\gamma/2\tau}(\mathfrak{g})$ (the corresponding dynamical R-matrices are gauge equivalent). Thus, $V$ becomes a representation of $E_{-1/\tau,\gamma/2\tau}(\mathfrak{g})$. This representation is easily seen to be an evaluation representation, i.e., it factors through the small elliptic quantum group $e_{-1/\tau,\gamma/2\tau}(\mathfrak{g})$ ([@TaVa01]).

Finally, we claim that if $k$ is fixed then the algebra $e_{-1/\tau,\gamma/2\tau}(\mathfrak{g})$ is a q-deformation of the exchange dynamical quantum group $F_{v}(G)$ (which allows us to regard $\text{$\mathcal{F}$}$ as a q-deformation of $\text{$\mathcal{F}$}_0$). Indeed, it is easy to check that as $\omega\to \infty$, $e_{\omega,a}(\mathfrak{g})$ degenerates into $F_{e^{-2\pi ia}}(G)$. Since we have $-1/\tau=\frac{\pi i}{(k+h^\vee)\log q}$, and $\gamma/2\tau=-\frac{1}{2(k+h^\vee)}$, the claim follows.
