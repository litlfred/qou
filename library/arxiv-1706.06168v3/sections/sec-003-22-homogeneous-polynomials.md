---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-003-22-homogeneous-polynomials
section_title: "Homogeneous Polynomials"
section_number: 2.2
pages: 6-7
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.671
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
[]{#homog_subsect label="homog_subsect"}

The usual degree-$n$ homogenization of a polynomial $f \in \mathbb{C}^n[x]$ is defined on monomials as follows and is extended linearly. $$\begin{split}
        \mathop{\mathrm{Hmg}}_n : \mathbb{C}^n[x] &\rightarrow V(n) \\
        x^k &\mapsto x^ky^{n-k}
    \end{split}$$ More generally, for $\lambda \in \mathbb{N}_0^m$ the *degree-$\lambda$ homogenization* is defined on monomials as follows and is extended linearly. $$\begin{split}
        \mathop{\mathrm{Hmg}}_\lambda: \mathbb{C}^\lambda[x_1,\ldots,x_m] &\rightarrow V(\lambda)\\
        x^{\mu} &\mapsto x^{\mu}y^{\lambda-\mu}
    \end{split}$$ $\mathbb{C}^n[x]$ and $V(n)$ are isomorphic as vector spaces via $\mathop{\mathrm{Hmg}}_n$, and we will mainly utilize bivariate homogeneous polynomials in $V(n)$ over the usual univariate polynomials in $\mathbb{C}^n[x]$.

What homogeneity gets us is a simplification of a number of issues related to the fact that polynomials in $\mathbb{C}^n[x]$ have *at most* $n$ zeros. Specifically, it is more natural to think of the missing zeros (when the number of zeros is less than $n$) as being "at infinity". Certain results require premises restricting to convex regions or to polynomials of degree exactly $n$ (e.g., the classical Grace-Walsh-Szegő coincidence theorem), and such details vanish when considering homogeneous polynomials with possible roots at infinity. Another way to say this is that we consider polynomials in $V(n)$ to have exactly $n$ roots in $\mathbb{CP}^1$, which can also be thought of as the Riemann sphere. We also consider polynomials $p(x,y) = p(x_1,y_1,\ldots,x_m,y_m) \in V(\lambda)$ to have zeros in $(\mathbb{CP}^1)^m$, where each pair $(x_k,y_k)$ corresponds to a single factor of $\mathbb{CP}^1$ in $(\mathbb{CP}^1)^m$.

We use the notation $(a:b) \in \mathbb{CP}^1$, which is meant to give off the connotation of a ratio; that is, $(a:b)$ should feel like $a/b$. We also use the notation $(a:b) = \big((a_1:b_1), \ldots, (a_m:b_m)\big) \in (\mathbb{CP}^1)^m$. Note that this connotation aligns with the idea of considering the zeros of polynomials to be in $(\mathbb{CP}^1)^m$. given the following equality. Defining $p := \mathop{\mathrm{Hmg}}_\lambda(f)$ for a given polynomial $f \in \mathbb{C}^\lambda[x_1,\ldots,x_m]$, we have: $$p(x,y) = p(x_1,y_1,\ldots,x_m,y_m) = \prod_k y_k^{\lambda_k} \cdot f(x_1/y_1,\ldots,x_m/y_m) = y^\lambda \cdot f(x/y)$$

Finally, we give an important definition which will essentially replace the notion of a monic polynomial for homogeneous polynomials.

::: definition
Given $p \in V(\lambda)$, we say that $p$ is *top-degree monic* if the coefficient of $x^\lambda$ in $p$ equals 1. In particular, if $p \in V(n)$ is top-degree monic, then $p$ has no roots at infinity.
:::
