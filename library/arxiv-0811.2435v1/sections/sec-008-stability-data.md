---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-008-stability-data
section_title: "Stability data"
section_number: null
pages: 20-22
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.967
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
Let us fix a free abelian group $\Gamma$ of finite rank, and a graded Lie algebra $\g=\oplus_{\gamma\in \Gamma}\g_{\gamma}$ over $\Q$.[^1]

::: defn
Stability data on $\g$ is a pair $\sigma=(Z,a)$ such that:

1\) $Z: \Gamma\to \R^2\simeq \C$ is a homomorphism of abelian groups called the central charge;

2\) $a=(a(\gamma))_{\gamma\in \Gamma\setminus \{0\}}$ is a collection of elements $a(\gamma)\in \g_{\gamma}$,

satisfying the following

**Support Property**:

Pick a norm $\parallel\bullet\parallel$ on the vector space $\Gamma_{\R}=\Gamma\otimes_{\Z}\R$. Then there exists $C>0$ such that for any $\gamma\in \op{Supp}a$ (i.e. $a(\gamma)\ne 0$) one has $$\parallel\gamma\parallel\le C|Z(\gamma)|\,\,.$$
:::

Obviously the Support Property does not depend on the choice of the norm. We will denote the set of all stability data on $\g$ by $Stab(\g)$. Later we will equip this set with a Hausdorff topology.

The Support Property is equivalent to the following condition (which we will also call the Support Property):

*There exists a quadratic form $Q$ on $\Gamma_{\R}$ such that*

1\) $Q_{|\op{Ker}\, Z}<0$;

2\) $\op{Supp} a\subset \{\gamma\in \Gamma\setminus \{0\}|\,\,Q(\gamma)\geqslant 0\}$,

where we use the same notation $Z$ for the natural extension of $Z$ to $\Gamma_{\R}$.

Indeed, we may assume that the norm $\parallel\bullet\parallel$ is the Euclidean norm in a chosen basis and take $Q(\gamma)=-\parallel\gamma\parallel^2+C_1|Z(\gamma)|^2$ for sufficiently large positive constant $C_1$. Generically $Q$ has signature $(2,n-2)$, where $n=\op{rk}\Gamma$. In degenerate cases $Q$ can have signature $(1,n-1)$ or $(0,n)$.

For a given quadratic form $Q$ on $\Gamma_{\R}$ we denote by $Stab_Q(\g)\subset Stab(\g)$ the set of stability data satisfying the above conditions 1) and 2). Obviously $Stab(\g)=\cup_QStab_Q(\g)$, where the union is taken over all quadratic forms $Q$.

::: rmk
In the case of a $3$-dimensional Calabi-Yau manifold $X$ there is a natural candidate for the quadratic form $Q$ of the signature $(2,n-2)$ needed to formulate the Support Property. Namely, identifying $H^3(X,\R)$ with $H^{3,0}(X,\C)\oplus H^{2,1}(X,\C)$ we can equip $H^3(X,\R)$ with the complex structure. Furthermore, the natural symplectic form coming from the Hodge structure gives rise to a pseudo-hermitian form on $H^3(X,\R)$ of the signature $(2,n-2)$, where $n=\dim _{\R}H^3(X,\R)$. One can ask whether this form is positive on every special Lagrangian submanifold of $X$. If this is true, then the Support Property gives rise to a bound on the support of the function $\Omega$ discussed in Section 1.4.
:::

Support Property implies the following estimate for the number of points in the $\op{Supp}a$ with the central charge inside of the disc of radius $R$: $$\#\left(Z(\op{Supp}a)\cap \{z\in \C|\,\,|z|\le R\}\right)=O(R^n)\,\,,$$ where $R\to \infty$ and $n=\op{rk}\Gamma$, Therefore the set $Z(\op{Supp}a)$ is discrete in $\C$ and does not contain zero.

::: rmk
It seem reasonable to consider "limiting cases" of stability data when the Support Property is not satisfied. Then the numbers $\op{Re}Z$ and $\op{Im}Z$ are allowed to take values in arbitrary totally ordered fields, e.g. $\R((t))$ (here $t$ is a formal parameter such that $t>0$ and $t<x$ for any $x\in \R_{>0}$). Some of our considerations below make sense in this situation. In the framework of stability conditions on triangulated categories such structures appeared in [@Ba], [@Tod1].
:::

[^1]: In examples $\g$ is a $R$-linear Lie algebra, where $R$ is a commutative unital $\Q$-algebra.
