---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-027-numerical-realization-of-motivic-functions
section_title: "Numerical realization of motivic functions"
section_number: null
pages: 75-77
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.939
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
This section is not used in further consideration, its goal is only to show that the abstractly defined ring $\overline{{\cal M}}^{G,\mu}(X)$ can be realized as certain ring of functions with numerical values.

Let $Z$ be a scheme of finite type over a finite field $\k\simeq{\bf F}_q$ endowed with an action of the group $\mu_n$ of roots of $1$ such that $n<p=char \, {\bf F}_q$. We choose a prime $l\ne p$. Let us define $Y$ as the quotient $(Z\times ({\bf A}^1_{\k}\setminus \{0\}))/\mu_n$ with respect to the diagonal action of $\mu_n$. Then we have a morphism $$\pi: Y\to {\bf A}^1_{\k}\setminus \{0\},\,\,\,(z,t)\mapsto t^n \,\,\forall (z,t)\in (Z\times {\bf A}^1_{\k}\setminus \{0\})(\overline{\bf F}_q)\,.$$ Let $j:{\bf A}^1_{\k}\setminus \{0\}\to {\bf A}^1_{\k}$ be the natural embedding. We define the number $$N_Z=\op{Tr}_{Fr}({\cal F}(j_{\ast}\pi_{!}({\Q}_{l,Y}))_{|s=1})\in \overline{\Q_{l}}\,\,,$$ which is the trace of the Frobenius $Fr$ of the fiber at $s=1$ of the Fourier transform of the $l$-adic sheaf $j_{\ast}\pi_{!}({\Q}_{l,Y})$, where ${\Q}_{l,Y}$ denotes the constant sheaf $\Q_l$ on $Y$. In fact the number $N_Z$ can be considered as an element of the cyclotomic field $\Q(\eta_p)$, where $\eta_p$ is a primitive $p$-th root of $1$: $$1+\eta_p+\dots+\eta_p^{p-1}=0\,\,.$$

We have a canonical non-trivial character $\chi:{\bf F}_q\to \Q(\eta_p)^{\ast}$ given by the composition of the trace $\op{Tr}_{{\bf F}_q\to{\bf F}_p}:{\bf F}_q\to {\bf F}_p$ with the additive character $$\chi_p:{\bf F}_p\to \Q(\eta_p)^{\ast}, \,\,\,m\op{mod} p\mapsto \eta_p^m\,.$$ Then $$N_Z=\sum_{s\in ({\bf A}^1_{\k}\setminus \{0\})({\bf F}_q)}\#(\pi^{-1}(s)({\bf F}_q))\,\chi(s)\,\,.$$ Notice that the last formula makes sense for constructible $Z$ as well.

Let now $X$ be a constructible set over a field $\k, char\,\k=0$, endowed with an action of an affine algebraic group $G$.

::: defn
We call a model for $(X,G)$ the following choices:

-   a finitely generated subring $R\subset \k$,

-   a scheme ${\cal X}\to Spec(R)$ of finite type,

-   an affine group scheme ${\cal G}\to Spec(R)$ together with an embedding ${\cal G}\hookrightarrow GL(N)_R$,

-   an action of ${\cal G}$ on ${\cal X}$,

-   a constructible identification over $\k$ of ${\cal X}\times_{Spec(R)}Spec(\k)$ with $X$, as well as an isomorphism of groups ${\cal G}\times_{ Spec(R)}Spec(\k)\simeq G$ over $k$, compatible with the actions.
:::

Such a model always exists, and models form a filterted system. With a given model for $(X,G)$ we associate a commutative unital ring $$K({\cal X})=\varinjlim_{\{\mathrm{open}\,\,\,U\subset ({\cal X}\times GL(n))/{\cal G}\}}\prod_{\{\mathrm{closed}\,\,\,x\in U\}}\Q(\eta_{char\, \k(x)})\,\,,$$ where $\k(x)$ is the residue field of $x$ (which is a finite field).

Suppose that we are given a model for $(X,G)$ and let $f\in {\cal M}^{G,\mu}(X)$. As always we assume that the $\mu$-action on $X$ is good and factors through the action of some $\mu_n$.

::: defn
A model for $f$ compatible with the model $(R,{\cal X},{\cal G})$ for $(X,G)$ consists of the following data:

-   a finite set $J$, numbers $N_j,d_j, n_j\in \Z$, where $j\in J$, such that all numbers $N_j$ are positive and invertible in ${\cal O}({\cal X})$,

-   ${\cal G} \times \mu_{N_j}$-equivariant morphisms of constructible sets ${\cal Y}_j\to {\cal X}$ given for each $j\in J$, where ${\cal Y}_j\to {\cal X}$ are ${\cal G}\times \mu_{N_j}$-schemes of finite type, and we endow ${\cal X}$ with the trivial action of the group $\mu_{N_j}$,

These data are required to satisfy the condition that $$f=\sum_{j\in J}\,n_j\,[{\cal Y}_j\times_{Spec(R)}Spec(\k)\to X]\cdot{\mathbb L}^{d_j}\,.$$
:::

Models for $f$ always exist. Moreover, for any finite collection $(f_i)_{I\in I}$ of elements of ${\cal M}^{G,\mu}(X)$ there exists a model for $(X,G)$ with compatible models for $(f_i)_{I\in I}$ .

Having a model for $f$ we can associate with it an element $f_{num}\in K({\cal X})$ in the following way. Let $x\in ({\cal X}\times GL(N)_R)/{\cal G}$ be a closed point. We can apply the considerations of the beginning of this section to the fiber $Z_{j,x}$ over the point $x$, of the map $({\cal Y}_j\times GL(N)_R)/{\cal G}\to ({\cal X}\times GL(N)_R)/{\cal G}$, where ${\cal Y}_j$ is the scheme from the definition of the model for $f$. Then for each $j$ we obtain an element $N_{Z_{j,x}}\in \Q(\eta_p), p=char\,\k(x)$. Finally, we set $$f_{num}(x):=\sum_{j\in J}n_j\,q_x^{d_j}N_{Z_{j,x}}\,\,,$$ where $q_x:=\#\k(x)$. Hence we realize $f$ as a function with values in numbers.
