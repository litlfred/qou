---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-011-crossing-the-wall-of-second-kind
section_title: "Crossing the wall of second kind"
section_number: null
pages: 30-32
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.995
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
Here we will interpret the parallel transport in a different way, introducing a wall of another kind. We use the notation from the previous section. In particular, we fix the quadratic form $Q_0$ and the connected component $U$ of the set $\{Z\in \op{Hom}(\Gamma,\C)|\,\, (Q_{0})_{|\op{Ker} Z}<0\}$.

For a given primitive $\gamma\in \Gamma\setminus \{0\}$ we introduce the set ${\cal W}_{\gamma}^{Q_0}=\{Z\in U|\,Z(\gamma)\in \R_{>0}\}$. It is a hypersurface in $U$. We call it a *wall of second kind* associated with $\gamma$. We call the union $\cup_{\gamma}{\cal W}_{\gamma}^{Q_0}$ the *wall of second kind* and denote it by ${\cal W}_2$.

::: defn
We say that a path $\sigma=(Z_t)_{0\le t\le 1}\subset U$ is short if the convex cone $C_{\sigma}$ which is the convex hull of $\left(\cup_{0\le t\le 1}Z_t^{-1}(\R_{>0})\right)\cap \{Q_0\geqslant 0\}$ is strict.
:::

With a short path we associate a pro-nilpotent group $G_{C_{\sigma}}$ with the Lie algebra $\g_{C_{\sigma}}=\prod_{\gamma\in C_{\sigma}\cap \Gamma}\g_{\gamma}$.

The following result is obvious.

::: prp
For a generic short path $\sigma=(Z_t)_{0\le t\le 1}$ there exists no more than countable set $t_i\in [0,1]$ and corresponding primitive $\gamma_i\in \Gamma\setminus \{0\}$ such that $Z_{t_i}\in {\cal W}_{\gamma_i}^{Q_0}$. For each $i$ we have: $\op{rk} Z_{t_i}^{-1}(\R)\cap \Gamma=1$.
:::

Let us recall the continuous lifting map $\phi: U\to Stab(\g)$ from the previous section. In the notation of the previous Proposition we define for any $t_i$ a group element $$A_{t_i}=\exp\left(\varepsilon_i\sum_{n\geqslant 1}a_{t_i}({n\gamma_i})\right)\in G_{C_{\sigma}}\,\,,$$ where $\varepsilon_i=\pm 1$ depending on the direction in which the path $Z_t(\gamma_i)$ crosses $\R_{>0}$ for $t$ sufficiently close to $t_i$.

::: thm
For any short loop the monodromy $\prod_{t_i}^{\longrightarrow}A_{t_i}$ is equal to the identity (here the product is taken in the increasing order of the elements $t_i$).
:::

*Proof.* Here we also present a sketch of the proof. Similarly to the proof of the Theorem 3 we consider the case of infinitesimally small loop $\sigma$ around a point $Z$ such that $\op{rk} \Gamma_2=2$ where $\Gamma_2:=Z^{-1}(\R)\cap \Gamma$ (i.e. $Z$ is a point where two, and hence infinitely many, walls of second kind intersect). Since $\sigma$ is infinitesimally small we can replace $\Gamma$ by $\Gamma_2$. Then we have the space $\op{Hom}(\Gamma_2,\C)\simeq \R^4$ which contains a countable collection of walls consisting of those $Z: \Gamma_2\to \C$ for which there exists $\gamma\in \Gamma_2\setminus \{0\}$ such that $Q_0(\gamma)\geqslant 0$ and $Z(\gamma)\in \R$. All the hypersurfaces contain $\R^2= \op{Hom}(\Gamma_2,\R)\subset \op{Hom}(\Gamma_2,\C)$. Factorizing by this subspace $\R^2$ we obtain a collection of lines with rational slopes in the union of two opposite strict sectors $S\cup (-S)\subset \R^2=\op{Hom}(\Gamma_2,i\R)$.

We have to prove that the product over a loop surrounding $(0,0)$ is the identity element. But it is easy to see that the product over the rays belonging to each of the sectors is equal to the left (resp. right) hand side of the wall-crossing formula. $\blacksquare$

Let us now introduce a set ${\cal X}_1\subset \Gamma\times U$ which consists of pairs $(\gamma,Z)$ such that $\gamma\in\Gamma\setminus\{0\}$ is a non-zero element, $Q_0(\gamma)\geqslant 0, Z(\gamma)\in \R_{>0}$ and $Z^{-1}(\R_{>0})\cap \Gamma=(\Q_{>0}\cdot \gamma)\cap \Gamma$.

::: prp
The set of continuous sections $\psi: U\to Stab(\g)$ such that $\psi(Z)$ is compatible with $Q_0$ for any $Z\in U$ is in one-to-one correspondence with functions $\tilde{a}: {\cal X}_1\to \g$ such that $\tilde{a}(\gamma,Z)\in \g_{\gamma}$ satisfying the property that for any small loop $\sigma$ the monodromy defined in the previous theorem is equal to the identity.
:::

*Proof.* The bijection is given by the formula $\tilde{a}(\gamma, Z)=a_{\psi(Z)}(\gamma)$. By the previous theorem the corresponding monodromy is trivial. Conversely, the triviality of the monodromy is equivalent to the wall-crossing formula in the special case when a $2$-dimensional sublattice of $\Gamma$ is mapped by $Z$ into the line $\R\subset \C$. The general case of an arbitrary line can be reduced to this one by a rotation $Z\mapsto Ze^{2\pi it}$ (it does not change the values $a(\gamma)$ because we do not cross the wall of first kind). $\blacksquare$

Let us also introduce a set ${\cal X}_2\subset \Gamma\times U$ which consists of such pairs $(\gamma,Z)$ that $Q_0(\gamma)\geqslant 0, Z(\gamma)>0$ and there are no non-zero $\Q$-independent elements $\gamma_1,\gamma_2\in \Gamma$ with the property $\gamma=\gamma_1+\gamma_2, Q_0(\gamma_i)\geqslant 0, Z(\gamma_i)>0, i=1,2$. Since ${\cal X}_2$ is a locally-closed hypersurface in $U\times \op{Hom}(\Gamma,\C)$ it has finitely many connected components. Obviously, we have ${\cal X}_1\subset {\cal X}_2$.

It follows from the wall-crossing formula that for a continuous section $\psi:U\to Stab(\g)$ the restriction of the function $a$ to ${\cal X}_2$ is locally-constant and uniquely determines the section $\psi$. Therefore, the values of the restriction $a_{|\pi_0({\cal X}_2)}$ provides a countable coordinate system (satisfying a countable system of equations) on the set of continuous sections $\{\psi: U\to Stab(\g)\}$ as above. It can be compared with another countable coordinate system (with no constraints) given the value $\psi(Z_0)$ for $Z_0\in U$. The latter coordinate system is not very convenient since one has to choose a generic $Z_0$.
