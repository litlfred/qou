---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-010-topology-and-the-wall-crossing-formula
section_title: "Topology and the wall-crossing formula"
section_number: null
pages: 25-30
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.997
latex_coverage_ratio: 0.984
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
Here we are going to introduce a Hausdorff topology on the set of stability data in such a way that the forgetting map $$Stab(\g)\to \op{Hom}(\Gamma,\C)\simeq \C^n,\,\, (Z,a)\mapsto Z$$ will be a local homeomorphism. In particular $Stab(\g)$ carries a structure of a complex manifold (in general with an uncountable number of components, each of which is paracompact). In order to define the topology we define the notion of a continuous family of points in $Stab(\g)$.

Let $X$ be a topological space, $x_0\in X$ be a point, and $(Z_x,a_x)\in Stab(\g)$ be a family parametrized by $X$.

::: defn
We say that the family is continuous at $x_0$ if the following conditions are satisfied:

a\) The map $X\to \op{Hom}(\Gamma,\C), x\mapsto Z_x$ is continuous at $x=x_0$.

b\) Let us choose a quadratic form $Q_0$ such that $(Z_{x_0},a_{x_0})\in Stab_{Q_0}(\g)$. Then there exists an open neighborhood $U_0$ of $x_0$ such that $(Z_{x},a_{x})\in Stab_{Q_0}(\g)$ for all $x\in U_0$.

c\) For any closed strict sector $V$ such that $Z(\op{Supp}a_{x_0})\cap \partial V=\emptyset$ the map $$x\mapsto \log\,A_{V,x,Q_x}\in \g_{V,Z_x,Q_x}\subset \prod_{\gamma\in \Gamma}\g_{\gamma}$$ is continuous at $x=x_0$. Here we endow the vector space $\prod_{\gamma\in \Gamma}\g_{\gamma}$ with the product topology of discrete sets, and $A_{V,x,Q_x}$ is the group element associated with $(Z_x,a_x)$, sector $V$ and a quadratic form $Q_x$ such that $(Z_x,a_x)\in Stab_{Q_x}(\g)$.
:::

::: rmk
Part c) of the Definition 3 means that for any $\gamma\in \Gamma\setminus\{0\}$ the component of $\log\,A_{V,x,Q_x}$ belonging to $\g_{\gamma}$ is locally constant as a function of $x$ in a neighborhood of $x_0$.
:::

The element $\log(A_{V,x,Q_x})\in \prod_{\gamma\in \Gamma}\g_{\gamma}$ does not depend on $Q_x$, e.g. we can take $Q_x:=Q_0$ for $x$ close to $x_0$. The continuity means informally that for any closed triangle $\Delta\subset \R^2$ with one vertex at the origin, the projection of $\log\,A_{V,Z_x,Q_x}$ into the vector space $\oplus_{\gamma\in \Delta}\g_{\gamma}$ does not depend on $x\in X$ as long as there is no element $\gamma\in \op{Supp}a_x$ such that $Z(\gamma)$ crosses the boundary $\partial\Delta$.

It is easy to see that the above definition gives rise to a topology on $Stab(\g)$.

::: prp
This topology is Hausdorff.
:::

*Proof.* Let $(Z,a)$ and $(Z^{\prime},a^{\prime})$ be two limits of a sequence $(Z_n,a_n)$ as $n\to \infty$. We have to prove that $(Z,a)=(Z^{\prime},a^{\prime})$. It is clear that $Z=Z^{\prime}$ since $\op{Hom}(\Gamma,\C)$ is Hausdorff. Let us now choose quadratic forms $Q$ and $Q^{\prime}$ which are compatible with $a$ and $a^{\prime}$ respectively in the sense of Definition 3. Then there exists a quadratic form ${Q}_0$ such that ${Q}_0$ is negative on $\op{Ker}Z=\op{Ker}Z^{\prime}$ and also $Q\le {Q}_0, Q^{\prime}\le {Q}_0$. Then for all sufficiently large $n$ the form ${Q}_0$ is compatible with $a_n$.

For a generic sector $V\subset \R^2$ its boundary rays do not intersect $Z(\Gamma)$. By part c) of the Definition 3 we have: $A_{V,Z, {Q}_0}=A_{V,Z^{\prime}, {Q}_0}^{\prime}$ since the product $\prod_{\gamma \in \Gamma}\g_{\gamma}$ is Hausdorff. Since any ray in $\R^2$ with the vertex at the origin can be obtained as an intersection of generic sectors then we conclude that $a=a^{\prime}$. The Proposition is proved. $\blacksquare$

Let us fix an element $Z_0\in \op{Hom}(\Gamma,\C)$ and a quadratic form $Q_0$ compatible with $Z_0$ (i.e. negative on its kernel). We denote by $U_{Q_0,Z_0}$ the connected component containing $Z_0$ in the domain $\{Z\in \op{Hom}(\Gamma,\C)|\,\, (Q_0)_{|\op{Ker} Z}<0\}$. In what follows we will frequently use the following elementary observation.

::: prp
If $Q$ is a quadratic form on a finite-dimensional vector space $\Gamma_{\R}$ and $Z:\Gamma_{\R}\to \C$ is an $\R$-linear map such that $Q_{|\op{Ker}Z}<0$ then the intersection $\{x\in \Gamma_{\R}|Q(x)\geqslant 0\}\cap Z^{-1}(l)$ is a convex cone (possibly empty) for any ray $l\subset \C$ with the vertex at the origin.
:::

Let $\gamma_1,\gamma_2\in \Gamma\setminus \{0\}$ be two $\Q$-linearly independent elements such that $Q_0(\gamma_i)\geqslant 0, Q_0(\gamma_1+\gamma_2)\geqslant 0, i=1,2$. We introduce the set $${\cal W}^{Q_0}_{\gamma_1,\gamma_2}=\{Z\in U_{Q_0,Z_0}|\,\,\R_{>0}Z(\gamma_1)=\R_{>0}Z(\gamma_2)\}\,\,.$$ In this way we obtain a countable collection of hypersurfaces ${\cal W}^{Q_0}_{\gamma_1,\gamma_2}\subset U_{Q_0,Z_0}$ called the *walls corresponding to $Q_0,\gamma_1,\gamma_2$*. We denote their union by ${\cal W}_1:={\cal W}_1^{Q_0}$ and sometimes call it *the wall of first kind* (physicists call it the wall of marginal stability).

Let us consider a continuous path $Z_t, 0\le t\le 1$ in $U_{Q_0,Z_0}$ which intersects each of these walls for finitely many values of $t\in [0,1]$. Suppose that we have a continuous lifting path $(Z_t,a_t)$ of this path such that $Q_0$ is compatible with each $a_t$ for all $0\le t\le 1$. Then for any $\gamma\in \Gamma\setminus \{0\}$ such that $Q_0(\gamma)\geqslant 0$ the element $a_t(\gamma)$ does not change as long as $t$ satisfies the condition $$Z_t(\gamma)\notin \cup_{\gamma_1,\gamma_2\in \Gamma\setminus \{0\},\, \gamma_1+\gamma_2=\gamma}{\cal W}_{\gamma_1,\gamma_2}^{Q_0}\,\,.$$ If this condition is not satisfied we say that $t$ is a discontinuity point for $\gamma$. For a given $\gamma$ there are finitely many discontinuity points.

Notice that for each $t\in [0,1]$ there exist limits $$a^{\pm}_t(\gamma)=\lim_{\varepsilon\to 0, \,\varepsilon>0}a_{t\pm \varepsilon}(\gamma)$$ (for $t=0$ or $t=1$ only one of the limits is well-defined). Then the continuity of the lifted path $(Z_t,a_t)$ is equivalent to the following *wall-crossing formula* which holds for *any $t\in [0,1]$* and arbitrary $\gamma\in \Gamma\setminus\{0\}$: $$\prod_{\mu\in \Gamma^{prim},\,Z_t(\mu)\in l_{{\gamma},t}}^{\longrightarrow}\exp\left(\sum_{n\geqslant 1}a_t^{-}(n\mu)\right)=$$ $${}=\exp\left(\sum_{\mu\in \Gamma^{prim},\,Z_t(\mu)\in l_{{\gamma},t}, \,n\geqslant 1}a_t(n\mu)\right)=\prod_{\mu\in \Gamma^{prim},\,Z_t(\mu)\in l_{{\gamma},t}}^{\longrightarrow}\exp\left(\sum_{n\geqslant 1}a^{+}_t(n\mu)\right),$$ where $l_{\gamma,t}=\R_{>0}Z_t(\gamma)$, and $\Gamma^{prim}\subset \Gamma$ is the set of primitive vectors. The first and the last products are taken in the clockwise order of $\op{Arg}(Z_{t-\varepsilon})$ and $\op{Arg}(Z_{t+\varepsilon})$ respectively, where $\varepsilon>0$ is sufficiently small. Moreover, for each $\gamma$ we have $a_t^{-}(\gamma)=a_t^{+}(\gamma)=a_t(\gamma)$ unless there exist non-zero $\gamma_1,\gamma_2$ such that $\gamma=\gamma_1+\gamma_2$ and $Z_t\in {\cal W}_{\gamma_1,\gamma_2}^{Q_0}$.

::: rmk
Informally speaking, the wall-crossing formula says that for a very small sector $V$ containing the ray $l_{{\gamma},t}$ the corresponding element $A_V$, considered as a function of time, is locally constant in a neighborhood of $t$.
:::

For each $\gamma\in \Gamma\setminus \{0\}$ the wall-crossing formula allows us to calculate $a_{1}(\gamma)$ is terms of $a_{0}(\gamma^{\prime})$ for a finite collection of elements $\gamma^{\prime}\in \Gamma\setminus \{0\}$. Morally it is an inductive procedure on the ordered set of discontinuity points $t_i\in [0,1]$. The only thing we need to check is that for each $\gamma\in \Gamma\setminus \{0\}$ the computation involves finitely many elements of $\Gamma$. For that we need some preparation. First we introduce a partial order on the set $S_{Q_0}=(\Gamma\cap Q^{-1}_0(\R_{\geqslant 0}))\times [0,1]$ generated by the following relations:

a\) $(\gamma,t)\geqslant (\gamma,t^{\prime})$ if $t\geqslant t^{\prime}$;

b\) if $\gamma=\sum_{1\le i\le m}\gamma_i, Q_0(\gamma_i)\geqslant 0, Z_t(\gamma_i)\in \R_{>0}Z_t(\gamma), 1\le i\le m, m\geqslant 2$, where not all $\gamma_i$ belong to $\Q\cdot\gamma$, then $(\gamma,t)\geqslant (\gamma_i,t)$ for all $1\le i\le m$.

::: lmm
For any $(\gamma,t)\in S_{Q_0}$ the set $(\gamma^{\prime},t^{\prime})\in S_{Q_0}$ such that $(\gamma^{\prime},t^{\prime})\le (\gamma,t)$ is a finite union of sets of the form $\{\gamma_{\alpha}\}\times [0,t_{\alpha}]$.
:::

The Lemma immediately implies the desired result.

::: cor
The element $a_t({\gamma})$ is a finite Lie expression of the elements $a_{0}(\gamma_{\alpha})$.
:::

*Proof of the Lemma*. Let us assume the contrary. Then we have an infinite sequence $t_1>t_2>t_3>\dots$ such that $$(\gamma_1,t_1)\geqslant _{a)}(\gamma_2,t_2)\geqslant_{b)}(\gamma_3,t_3)\geqslant_{a)}(\gamma_4,t_4)\geqslant_{b)}\dots\,\,,$$ where the subscript $a)$ or $b)$ denotes the two different possibilities for the partial order defined above. Let $t_{\infty}=\lim_{n\to \infty}t_n$. It is easy to see that there exists a Euclidean norm $\parallel\bullet\parallel$ on $\Gamma_{\R}$ such that for any $v_1,v_2\in \Gamma_{\R}$ satisfying the properties $Q_0(v_i)\geqslant 0, Z_{t_{\infty}}(v_1)\in \R_{>0}Z_{t_{\infty}}(v_2)$ we have the inequalities $\parallel v_i\parallel <\parallel v_1+v_2\parallel$ for $i=1,2$.

Moreover the same property holds if we replace the map $Z_{t_{\infty}}$ by an additive map $Z$ which is close to it. Then we conclude that $$\parallel \gamma_{2n}\parallel>\parallel \gamma_{2n+1}\parallel=
\parallel \gamma_{2n+2}\parallel$$ for all sufficiently large $n$. This contradicts to the fact the lattice $\Gamma$ is discrete in $\Gamma_{\R}$. The Lemma is proved. $\blacksquare$

The previous discussion allows us to lift a generic path $Z_t, 0\le t\le 1$ as above to a unique continuous path $(Z_t,a_t)\in Stab(\g), 0\le t\le 1$ which starts at a given point $(Z_0,a_0)\in Stab(\g)$. In other words, we have the notion of a *parallel transport* along a generic path. This observation is a part of the following more general statement.

::: thm
For given quadratic form $Q_0$ and $(Z_0,a_0)\in Stab_{Q_0}(\g)$ there exists a unique continuous map $\phi: U_{Z_0,Q_0}\to Stab(\g)$ such that it is a section of the natural projection $Stab(\g)\to U_{Z_0, Q_0}$, and $\phi(Z_0)=(Z_0,a_0)$.
:::

*Proof.* We have already proved the existence of a lifted path $(Z_t,a_t)$ for a generic path $Z_t$ provided the beginning point $Z_0$ is fixed. What is left to prove that the endpoint $(a_1,Z_1)$ does not depend on a choice of the generic path $Z_t$. We are going to sketch the proof leaving the details for the reader.

Let us consider an infinitesimally small loop around the intersection point $Z$ of two or more walls. We would like to prove that the monodromy of the parallel transport along the loop is trivial. There are two possibilities:

a\) there are two different sublattices $\Gamma_1,\Gamma_2\subset \Gamma$ of ranks $\geqslant 2$ such that $Z(\Gamma_i), i=1,2$ belong to two different lines in the plane $\R^2$;

b\) there exists a sublattice $\Gamma_3\subset \Gamma$ such that $\op{rk}\Gamma_3\geqslant 3$ and $Z(\Gamma_3)$ belongs to a line in $\R^2$.

In the case a) the corresponding Lie subalgebras of the completion of $\g_{\Gamma}$ are graded by non-intersecting subsets of $\Gamma$. Hence the corresponding wall-crossing transformations commute.

In the case b) let us choose a decomposition $\R^2\setminus \{(0,0)\}=\sqcup_{1\le i\le 4}V_i$, where $V_i, 1\le i\le 4$ are strict sectors such that $\R\cdot Z(\Gamma_3)\subset V_1\sqcup V_3\sqcup \{(0,0)\}$. When we move around the infinitesimally small loop the element $a(\gamma)$ can change only for $\gamma\in \Gamma_3$. Hence we can replace $\Gamma$ by $\Gamma_3$ in all computations. The wall-crossing formula implies that the elements $A_{V_i}, 1\le i\le 4$ do not change along the loop (moreover, by our assumption we have $A_{V_2}=A_{V_4}=1$). By Remark 7 from Section 2.2 we conclude that the stability data with the central charge $Z^{\prime}$ which is close to $Z$ are uniquely determined by $Z^{\prime}$ and the collection of elements $A_{V_i}, 1\le i\le 4$. Hence the monodromy around the loop is trivial.

Finally one has to check the the *global* monodromy around a loop in $U_{Z_0,Q_0}$ is trivial. It follows from the fact that the fundamental group $\pi_1(U_{Z_0,Q_0})$ is generated by the loop $Z\mapsto Ze^{2\pi it}, t\in [0,1]$. But the monodromy around this loop is trivial for generic $Z$, because the loop does not intersect the walls. $\blacksquare$.

We can write the wall-crossing formula in the way similar to the one from the Introduction. In the case of generic path we have at a discontinuity point $t_0\in [0,1]$ a two-dimensional lattice $\Gamma_0\simeq \Z^2$ which is projected by $Z_{t_0}$ into a real line in $\R^2$. We choose an isomorphism $\Gamma_0\simeq \Z^2$ in such a way that $Q_0^{-1}(\R_{\geqslant 0})\cap (\Gamma_0\setminus \{0\})$ is contained in $\Z_{>0}^2\cup \Z^2_{<0}$. Also we assume that the orientation of $\Gamma_0\otimes \R$ defined by $Z_t$ agrees with the one on $\Z^2_{>0}$ for $t=t_0-\varepsilon$ and is opposite to it for $t=t_0+\varepsilon$, where $\varepsilon>0$ is sufficiently small.

Then if $\gamma=(m,n)\in \Z^2_{>0}$, and $a^{\pm}_{t_0}(\gamma):=a^{\pm}(m,n)$, we can write the the wall-crossing formula in the following way: $$\prod_{(m,n)=1}^{\longrightarrow}\exp\left(\sum_{k\geqslant 1}a^{-}(km,kn)\right)=\prod_{(m,n)=1}^{\longleftarrow}\exp\left(\sum_{k\geqslant 1}a^{+}(km,kn)\right),$$ where in the LHS we take the product over all coprime $m,n$ in the increasing order of $m/n\in \Q$, while in the RHS we take the product over all coprime $m,n$ in the decreasing order. Both products are equal to $\exp(\sum_{m,n> 0}a_{t_0}(m,n))$.
