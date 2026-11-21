---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-014-34-products-of-normalized-characters
section_title: "Products of normalized characters"
section_number: 3.4
pages: 10-11
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.972
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
As the abstract Fourier transform is a ring homomorphism, the point-wise multiplication of functions over Young diagrams of size $n$ corresponds to the product in the center of the symmetric group algebra. But, in $Z(\mathbb{C}\mathfrak{S}_n)$, one has $$\varSigma_\mu \cdot \varSigma_\nu = \sum_{\substack{\forall i,\,\,A_i \in \mathcal{A}(n,\,\mu_i)\\ \forall i\neq j,\,\,A_i\cap A_j=\emptyset}} \ \sum_{ \substack{\forall i,\,\,B_i \in \mathcal{A}(n,\,\nu_i)\\ \forall i\neq j,\,\,B_i\cap B_j=\emptyset}} C(A_1)\,C(A_2)\,\cdots \,C(A_r)\, C(B_1)\,C(B_2)\,\cdots \,C(B_r).$$ As the $A_i$'s and the $B_j$'s may have elements in common, this is not equal to $\varSigma_{\mu \cup \nu}$. Let us split this double summation over $a_{i,j}$ and $b_{k,l}$ in the following way. To each indexing sequence $a_{i,j}, b_{k,l}$, we associate the partial matching between the sets $I_A=(i,j)_{1 \leq j \leq \mu_i}$ (indices of the $a$'s) and $I_B=(k,l)_{1 \leq k \leq \nu_l}$, which links $(i,j)$ and $(k,l)$ if and only if $a_{i,j}=b_{k,l}$. When we sum the quantity $$\label{eq:prod_cycles}
 C(A_1)\,C(A_2)\,\cdots \,C(A_r)\, C(B_1)\,C(B_2)\,\cdots \,C(B_r)$$ over indexing sequences with a given partial matching, we obtain $\Sigma_\rho$ for some $\rho$ depending on the matching. Indeed, if we know which of the $a_{i,j}$'s are equal to which of the $b_{k,l}$'s, the product [\[eq:prod_cycles\]](#eq:prod_cycles){reference-type="eqref" reference="eq:prod_cycles"} can be rewritten as a product of cycles with disjoint supports in a way which does not depend of the values of the $a$'s and of the $b$'s. Finally, $$\varSigma_\mu \cdot \varSigma_\nu = \sum \varSigma_{\rho(M)},$$ where the sum runs over partial matchings $M$ of the set of indices of the $a$'s with the set of indices of the $b$'s.

::: example
Let us compute $\varSigma_{2} \cdot \varSigma_{3}$. The set of indices of the $a$'s (resp. the $b$'s) is $\{1,2\}$ (resp. $\{1,2,3\}$).

-   If $A$ and $B$ have no common element, the product $C(A) \, C(B)$ is a 3-cycle multiplied by a 2-cycle with disjoint supports and the corresponding sum is $\varSigma_{3,2}$.

-   If $a_1=b_1$, but all other elements are different, then $(a_1\ a_2\ a_3)\cdot (a_1\ b_2) = (a_1\ b_2\ a_2\ a_3)$. When we sum on all possible values of $a_1$, $b_2$, $a_2$, $a_3$ (all different), one obtains $\varSigma_4$.

    The result is the same for any of the $6$ matchings of size $1$.

-   If $a_1=b_1$ and $a_2=b_2$, then $(a_1,a_2,a_3)\cdot (a_1,a_2) = (a_1,a_3)(a_2)$. When we sum on all possible values of $a_1$, $a_2$, $a_3$, we obtain $\varSigma_{2,1}$ (note that here it is important to remember that we have to sum over indices $a_2$ even if its value does not change the permutation).

    Once again, the result is the same for any of the $6$ matchings of size $2$.

Thus, $\varSigma_{2} \cdot \varSigma_{3} = \varSigma_{2,3} + 6 \varSigma_4 + 6 \varSigma_{2,1}$.
:::

In general, one has the following properties:

1.  The size of $\rho(M)$ is simply $|\mu|+|\nu|-|M|$ where $|M|$ is the size of the matching.

2.  The term corresponding to the empty matching is $\varSigma_{\nu \cup \mu}$. Thus, $$\varSigma_\nu \cdot \varSigma_\mu = \varSigma_{\nu \cup \mu} + \sum_{|\rho| < |\mu|+ |\nu|} c^\rho_{\nu,\mu} \,\varSigma_\rho.$$ By induction, one obtains that, if $k_1 \geq k_2 \geq \ldots \geq k_r$: $$\varSigma_{k_1} \cdot \varSigma_{k_2}\cdots \varSigma_{k_r} = \varSigma_{k_1,\ldots,k_r} + \sum_{|\rho| < k_1 + \cdots + k_r} c^\rho_{k_1,\ldots,k_r}\, \varSigma_\rho.$$ This triangular relation can be inverted, so the $\varSigma_\rho$ are in the algebra $\mathscr{O}$ and span it linearly. Moreover, $\varSigma_\rho$ is a non-homogeneous element of degree $|\rho|$ and its homogeneous component of maximal degree is $p_\rho$.

3.  If $\mu=(l)$ and $\nu=(m)$, all matchings of size $1$ give a term $\varSigma_{l+m-1}$. As there are $ml$ such matchings, one has $$\varSigma_l \,\varSigma_m = \varSigma_{l,m} +ml\, \varSigma_{l+m-1}+(\text{terms of degree at most }l+m-2).$$
