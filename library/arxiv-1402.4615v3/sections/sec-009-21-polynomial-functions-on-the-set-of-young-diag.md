---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-009-21-polynomial-functions-on-the-set-of-young-diag
section_title: "Polynomial functions on the set of Young diagrams"
section_number: 2.1
pages: 12-14
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.885
latex_coverage_ratio: 0.978
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
[]{#subsec:polfunct label="subsec:polfunct"} The ring $\Lambda_\star^{(1)}$ of *polynomial functions on the set of Young diagrams* (briefly: the ring of *polynomial functions*) has been introduced by Kerov and Olshanski in order to study irreducible character values of the symmetric groups [@KerovOlshanskiPolFunc].

The first characterization of $\Lambda_\star^{(1)}$, that we shall use as definition, is the following.

::: definition
[]{#def:polynomial label="def:polynomial"} A function $F$ on the set of all Young diagrams belongs to $\Lambda_\star^{(1)}$ if there exists a collection of polynomials $\left(F_h \in \mathbb{Q}[\lambda_1,\dots,\lambda_h]\right)_{h > 0}$ such that

-   for a diagram $\lambda=(\lambda_1,\dots,\lambda_h)$ of length $h$, one has $F(\lambda)=F_h(\lambda_1,\ldots,\lambda_h)$;

-   each $F_h$ is symmetric in variables $\lambda_1 - 1, \lambda_2 -2, \ldots ,\lambda_h-h$;

-   the compatibility relation $$F_{h+1}(\lambda_1,\dots,\lambda_h,0) = F_h(\lambda_1,\dots,\lambda_h)$$ holds true for all values of $h$.
:::

The ring $\Lambda_\star^{(1)}$, as defined above, is sometimes called the ring of *shifted symmetric functions* in $\lambda_1, \lambda_2,\ldots$. It was first considered by Knop and Sahi [@KnopSahiShiftedSym] in a more general context. While this is not obvious, one can prove that $\mathop{\mathrm{Ch}}^{(1)}_\mu$ belongs to $\Lambda_\star^{(1)}$. In fact, one has more [@KerovOlshanskiPolFunc Section 3].

::: proposition
When $\mu$ runs over all partitions, the family $(\mathop{\mathrm{Ch}}^{(1)}_\mu)_\mu$ forms a linear basis of $\Lambda_\star^{(1)}$.
:::

An equivalent description of $\Lambda_\star^{(1)}$ can be given using Kerov's interlacing coordinates of a Young diagram. Recall that the *content* of a box of a Young diagram is $j-i$, where $j$ is its column index and $i$ its row index and, more generally, the content of a point of the plane is the difference between its $x$-coordinate and its $y$-coordinate. We denote by $\mathbb{I}_\lambda$ the set of contents of the *inner corners* of $\lambda$, that is corners, at which a box could be added to $\lambda$ to obtain a new diagram of size $|\lambda|+1$. Similarly, the set $\mathbb{O}_\lambda$ is defined as the contents of the *outer corners*, that is corners at which a box can be removed from $\lambda$ to obtain a new diagram of size $|\lambda|-1$. An example is given in Figure [1](#FigCorners){reference-type="ref" reference="FigCorners"} (we use the French convention to draw Young diagrams).

<figure id="FigCorners">
<div class="flushright">

</div>
<p><span class="math display">$$\begin{aligned}
        \mathbb{O}_\lambda&amp;=\{-1,2\} \\
        \mathbb{I}_\lambda&amp;=\{-3,0,4\}
    
\end{aligned}$$</span></p>
<figcaption>A Young diagram with its inner and outer corners (marked respectively with <span class="math inline"><em>i</em></span> and <span class="math inline"><em>o</em></span>).</figcaption>
</figure>

If $k$ is a positive integer, one can consider the power-sum symmetric function $p_k$, evaluated on the difference of alphabets $\mathbb{I}_\lambda - \mathbb{O}_\lambda$. By definition, it is a function on Young diagrams given by: $$\lambda \mapsto p_k(\mathbb{I}_\lambda - \mathbb{O}_\lambda):= \sum_{i \in \mathbb{I}_\lambda} i^k - 
\sum_{o \in \mathbb{O}_\lambda} o^k.$$ It can easily be seen that, for any Young diagram, $p_1(\mathbb{I}_\lambda - \mathbb{O}_\lambda)=0$. As any symmetric function can be written (uniquely) in terms of $p_k$, we can define $f(\mathbb{I}_\lambda - \mathbb{O}_\lambda)$ for any symmetric function $f$ as follows: if $a_\rho$ ($\rho$ partition) are the coefficients of the $p$-expansion of $f$, that is $f=\sum_\rho a_\rho p_{\rho_1} \cdots p_{\rho_\ell}$, then by definition, $$f(\mathbb{I}_\lambda - \mathbb{O}_\lambda)=\sum_\rho a_\rho p_{\rho_1}(\mathbb{I}_\lambda - \mathbb{O}_\lambda)
\cdots p_{\rho_\ell} (\mathbb{I}_\lambda - \mathbb{O}_\lambda).$$ With this notion of symmetric functions evaluated on difference of alphabets, the ring $\Lambda_\star^{(1)}$ admits the following equivalent description [@IvanovOlshanski2002 Corollary 2.8].

::: proposition
[]{#prop:pk_basis label="prop:pk_basis"} The functions $(\lambda \mapsto p_k(\mathbb{I}_\lambda - \mathbb{O}_\lambda))_{k \geq 2}$ form an algebraic basis of $\Lambda_\star^{(1)}$.
:::

In other terms, any function $F$ in $\Lambda_\star^{(1)}$ is equal to $\lambda \mapsto f(\mathbb{I}_\lambda - \mathbb{O}_\lambda)$, for some symmetric function $f$. This symmetric function $f$ is unique up to addition of a multiple of $p_1$.
