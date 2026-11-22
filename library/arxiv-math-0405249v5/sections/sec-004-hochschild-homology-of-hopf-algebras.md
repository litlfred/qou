---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL (2)"
section_id: sec-004-hochschild-homology-of-hopf-algebras
section_title: "hochschild homology of hopf algebras"
section_number: null
pages: 6-7
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.949
doc_brief: "Twisted homology of quantum SL (2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra of the quan- tum SL(2) group"
---
For arbitrary algebras, the Hochschild homologies are derived functors in the category of $\mathcal{A}\otimes \mathcal{A}^\mathrm{op}$-modules, and working with explicit resolutions usually involves lengthy calculations. But if $\mathcal{A}$ is a Hopf algebra then we can describe $H_\ast(\mathcal{A},\mathcal{M})$ for an arbitrary $\mathcal{A}$-bimodule $\mathcal{M}$ as a derived functor in the category of $\mathcal{A}$-modules. Define a right $\mathcal{A}$-module $\mathcal{M}'$ which is $\mathcal{M}$ as a vector space with right action given by $$\label{act}
    m \blacktriangleleft a :=  \sum \; S(a_{(2)}) \triangleright m \triangleleft
    a_{(1)},\quad
    a \in \mathcal{A},m \in \mathcal{M}.$$ Consider $k$ as the trivial $\mathcal{A}$-module $\mathcal{A}/\mathrm{ker}\, \varepsilon$. Feng and Tsygan proved:

::: prop
[@FT] []{#tor label="tor"} There is an isomorphism of vector spaces $$H_n(\mathcal{A},\mathcal{M}) \simeq 
    \mathrm{Tor}_n^\mathcal{A}(\mathcal{M}',k).$$
:::

::: pf
The $\mathrm{Tor}_n^\mathcal{A}(\mathcal{M}',k)$ are computed from the complex $(C_\ast,d)$ (with zeroth tensor component now being $\mathcal{M}'$) with boundary map $d$ given by $$d = \tilde d_0 + \sum_{i=1}^{n-1} (-1)^i d_i + (-1)^n \tilde d_n,$$ where the $d_i$ are as above and

$$\tilde d_0 (a_0, a_1,  \ldots , a_n) 
:= (a_0 \blacktriangleleft a_1,  a_2,  \ldots , a_n),$$ $$\tilde d_n (a_0, a_1,  \ldots , a_n) 
:= (\varepsilon(a_n)a_0 , a_1 , \ldots , a_{n-1}).$$ We define two linear maps $\xi,\xi' : C_n \rightarrow C_n$ by $$\xi(a_0, a_1, \ldots , a_n)  
    :=( S((a_1  \ldots a_n)_{(2)}) \triangleright a_0,   
    (a_1)_{(1)}, \ldots , (a_n)_{(1)})$$ $$\label{fetsimo}
\xi'(a_0,  \ldots , a_n)
:= ((a_1  \ldots  a_n)_{(2)}) \triangleright a_0,  
    (a_1)_{(1)}, \ldots , (a_n)_{(1)}).$$ Then $\xi \circ \xi'=\xi' \circ \xi=\mathrm{id}_{C_n}$. It is easily checked that $\xi$ commutes with $d_i$ for $1 \le i \le n-1$ and that $\xi \circ \tilde d_i=d_i \circ \xi$, $i=0,n$. Hence $\xi \circ d=b \circ \xi$ and $\xi$ is an isomorphism of complexes of $k$-vector spaces.
:::

Let $\pi : \mathcal{M}' \rightarrow H_0(\mathcal{A},\mathcal{M})$ be the canonical projection. Then we have $\pi (m \blacktriangleleft a)=\varepsilon(a) \pi(m)$, and if we consider $H_0(\mathcal{A},\mathcal{M})$ as trivial right $\mathcal{A}$-module, then $\pi \otimes \mathrm{id}_{\mathcal{A}^{\otimes n}}$ induces a morphism $$H_n(\mathcal{A},\mathcal{M}) 
    \rightarrow 
    H_0(\mathcal{A},\mathcal{M}) \otimes_k \mathrm{Tor}_n^\mathcal{A}(k,k).$$ If $\mathcal{A}$ is commutative and $\mathcal{M}=\mathcal{A}$ with the standard bimodule structure, then $H_0(\mathcal{A},\mathcal{M})=\mathcal{A}$, $\pi$ is the identity, and the above map is the isomorphism of the Hochschild-Kostant-Rosenberg theorem. For $\mathcal{M}={}_\sigma\mathcal{A}$ the map defines a "classical shadow\" of twisted Hochschild homology.
