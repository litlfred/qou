---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL (2)"
section_id: sec-003-twisted-hochschild-and-cyclic-homology
section_title: "twisted hochschild and cyclic homology"
section_number: null
pages: 4-6
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.968
doc_brief: "Twisted homology of quantum SL (2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra of the quan- tum SL(2) group"
---
[]{#section:cyclic_module label="section:cyclic_module"}

Let $\mathcal{A}$ be a unital, associative algebra over a field $k$ (assumed to be of characteristic zero) and $\sigma$ an automorphism. We define the cyclic object [@connes2], [@loday] underlying twisted cyclic homology $HC_\ast^\sigma(\mathcal{A})$ of $\mathcal{A}$ relative to $\sigma$. Set $C_n:=\mathcal{A}^{\otimes (n+1)}$. For clarity, we will denote $a_0 \otimes a_1 \otimes \cdots \otimes a_n \in C_n$ by $(a_0, a_1, \ldots , a_n)$. Define $$d_{n,i} (a_0, a_1, \ldots , a_n) = (a_0, \ldots , a_i a_{i+1} , \ldots ,
a_n) \quad 0 \leq i \leq n-1$$ $$d_{n,n} (a_0, a_1, \ldots , a_n) = (\sigma(a_n) a_0, a_1, \ldots , a_{n-1})$$ $$s_{n,i} (a_0, a_1, \ldots , a_n) = 
    (a_0 , \ldots a_i , 1 , a_{i+1} , \ldots , a_n) \quad 0 \leq i \leq n$$ $$\tau_n (a_0, a_1, \ldots , a_n) = ( \sigma(a_n) , a_0 , \ldots , a_{n-1})$$ For $\sigma = \mathrm{id}$ these are the face, degeneracy and cyclic operators of the standard cyclic object associated to $\mathcal{A}$ [@loday]. For general $\sigma$ the operator $T_n:=\tau_n^{n+1}$ is not equal to the identity, but all other relations of the cyclic category are fulfilled. Hence $C_\ast$ becomes what is called a paracyclic object [@getjon]. To obtain a cyclic object, we pass to the cokernels $C^\sigma_n:= C_n / C_n^1$, $C_n^1:=\mathrm{im}(\mathrm{id}-T_n)$. Dualizing [@kmt], we call the cyclic homology of this cyclic object the $\sigma$-twisted cyclic homology $HC_\ast^\sigma(\mathcal{A})$ of $\mathcal{A}$. Hence $HC_\ast^\sigma(\mathcal{A})$ is the total homology of Connes' mixed $(b,B)$-bicomplex

$$\label{gemischt}
\label{mixed_b_B_bicomplex}
        \begin{CD}
    @ V{b_4} VV @ V{b_3} VV @ V{b_2} VV @ V{b_1} VV @ . @ . @ .\\
    {C^\sigma_3} @ <{B_2}<< {C^\sigma_2} @ <{B_1} << {C^\sigma_1} @ <{B_0} <<
    {C^\sigma_0} @ . @ . @ . @ .\\ 
    @ V{b_3} VV @ V{b_2} VV @ V{b_1} VV @ . @ . @ . @ .\\
    {C^\sigma_2} @ <{B_1} << {C^\sigma_1} @ <{B_0} << {C^\sigma_0} @ . @ . @ . @ . @ .\\
    @ V{b_2} VV @ V{b_1} VV @ . @ . @ . @ . @ .\\
    {C^\sigma_1} @ <{B_0} << {C^\sigma_0} @ . @ . @ . @ . @ . \\
    @ V{b_1} VV @ . @ .  @ . @ . @ . @ .\\
    {C^\sigma_0} @ . @ . @ . @ . @ . @ .\\
        \end{CD}$$\
The maps $b_n$ and $B_n$ are given by $$b_n = \sum_{i=0}^n \; (-1)^i d_{n,i},\quad
    B_n = (1+ (-1)^n \tau_{n+1} ) s_n N_n,$$ with $N_n = \sum_{j=0}^n \; (-1)^{nj} \tau_n^j$, and $s_n  :  C^\sigma_n\rightarrow C^\sigma_{n+1}$ the "extra degeneracy" $$s_n ( a_0, a_1, \ldots , a_n) = (1, a_0, a_1, \ldots , a_n)$$

We calculate $HC_\ast^\sigma(\mathcal{A})$ via the spectral sequence associated to the mixed complex. Let $HH_\ast^\sigma(\mathcal{A})$ denote the entries of its first page, that is, $HH_n^\sigma(\mathcal{A}):=H_n(C^\sigma_\ast,b_\ast)$ (the homologies of the columns). For $\sigma=\mathrm{id}$ these are the Hochschild homologies $HH_\ast ( \mathcal{A})=H_\ast ( \mathcal{A},\mathcal{A})$. Hence we call $HH_\ast^\sigma(\mathcal{A})$ as in [@kmt] the $\sigma$-twisted Hochschild homology of $\mathcal{A}$.

To compute $HH_\ast^\sigma(\mathcal{A})$ consider the mixed complex ([\[gemischt\]](#gemischt){reference-type="ref" reference="gemischt"}) with $C^\sigma_n$ replaced by the original $C_n$. This is not a bicomplex: the commutation relations in a paracyclic object imply that the (lifts of the) operators $b_\ast$ and $B_\ast$ anticommute according to (see [@getjon], Theorem 2.3) $$\label{neuegl}
    b_{n+1} B_n +B_{n-1} b_n=\mathrm{id}-T_n.$$ But the columns form the complex $(C_\ast,b_\ast)$ which computes the Hochschild homology $H_\ast(\mathcal{A},{}_\sigma\mathcal{A})$ of $\mathcal{A}$ with coefficients in the bimodule ${}_\sigma\mathcal{A}$ which is $\mathcal{A}$ as a vector space with bimodule structure $$\label{twisted_bimodule}
a \triangleright b  \triangleleft c:=\sigma(a)bc$$ In many cases $C_n=C_n^0 \oplus C_n^1$, $C_n^0:=\mathrm{ker}(\mathrm{id}-T_n)$, for example when $\sigma$ is diagonalizable. In this case, $T_n = \sigma^{\otimes (n+1)}$ is also diagonalizable, and $C_n^0$ and $C_n^1$ are the eigenspace of $T_n$ corresponding to the eigenvalue $1$ and the direct sum of all other eigenspaces, respectively. Then:

::: prop
[]{#tatata label="tatata"} If $C_n=C_n^0 \oplus C_n^1$, then $H_\ast(\mathcal{A},{}_\sigma\mathcal{A}) \cong HH_\ast^\sigma(\mathcal{A})$.
:::

::: pf
Note that ([\[neuegl\]](#neuegl){reference-type="ref" reference="neuegl"}) implies that $b_\ast$ commutes with $\mathrm{id}-T_\ast$, so the decomposition $C_n=C_n^0 \oplus C_n^1$ defines a decomposition of complexes, and we can identify $HH_\ast^\sigma(\mathcal{A})$ with the homologies of the subcomplex $(C_\ast^0,b_\ast) \subset (C_\ast,b_\ast)$. Hence $H_\ast(\mathcal{A},{}_\sigma\mathcal{A})$ is the direct sum of $HH_\ast^\sigma(\mathcal{A})$ and the homologies of $(C_\ast^1,b_\ast)$. But $(\mathrm{id}- T_n)|_{C_n^1}$ is a bijection under these assumptions, and we have on $C_n^1$ again by ([\[neuegl\]](#neuegl){reference-type="ref" reference="neuegl"}) the relation $$b_{n+1} (1-T_n)^{-1} B_n +(1-T_n)^{-1} B_{n-1} b_n=\mathrm{id}.$$ So $(\mathrm{id}- T_n)^{-1}B_\ast$ is a contracting homotopy for $(C_\ast^1,b_\ast)$ and the claim follows.
:::

This will allow us to calculate $HH_\ast^\sigma(\mathcal{A})$ using standard techniques of homological algebra.

The spectral sequence calculation is most efficiently done by passing to the normalized mixed complex (see for example [@weibel], Application 9.8.4). This leaves the first page unchanged. The second step is to calculate the horizontal homology of the rows relative to the maps $B_n$ which in the normalized complex are given explicitly by $$\label{B_n}
        B_n(a_0,\ldots,a_n) =
        \sum_{i=0}^{n} (-1)^{ni}
        (1,\sigma (a_i),\ldots,\sigma (a_n),a_0,\ldots,a_{i-1}).$$ For quantum $SL(2)$, we find that everything stabilises at the second page, and we can then read off the twisted cyclic homology.

For later use we note that by using the Hochschild-Kostant-Rosenberg theorem applied to an appropriate subalgebra, we obtain:

::: lemma
[]{#lemma:B_0_x^s_y^t label="lemma:B_0_x^s_y^t"} If $x$, $y$ are commuting elements of $\mathcal{A}$, with $\sigma(x) =x$, $\sigma(y)=y$, then for any $s$, $t \geq 0$ we have $$B_0 [ x^s y^t ] = t [( x^s y^{t-1}, y)] + s[( x^{s-1} y^t ,x)] \in 
    HH_1^\sigma(\mathcal{A})$$
:::

From now on, we will drop the suffices and write $b_n$ as $b$.
