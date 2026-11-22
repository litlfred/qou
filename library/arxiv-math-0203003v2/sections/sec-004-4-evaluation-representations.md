---
doc_id: arxiv-math-0203003v2
doc_title: "arXiv:math/0203003v2 [math.QA] 24 Apr 2002"
section_id: sec-004-4-evaluation-representations
section_title: "Evaluation Representations"
section_number: 4
pages: 10-10
source_pdf: 0203003v2.pdf
source_sha256: 7579ae76959396b8
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.971
doc_brief: "arXiv:math/0203003v2 [math.QA] 24 Apr 2002 — 8 sections: Front matter; Introduction; Representations of Quantum Dynamic"
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
