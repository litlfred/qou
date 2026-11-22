---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-014-complex-integrable-systems-and-stability-data
section_title: "Complex integrable systems and stability data"
section_number: null
pages: 35-38
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.984
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
In this section we explain how complex integrable systems (with some additional structures) give rise to stability data in the graded Lie algebra $\mathfrak{g}_\Gamma$ associated with a symplectic lattice. In particular, Seiberg-Witten differential can be interpreted as the central charge for a complex integrable system, while the BPS degeneracies are interpreted via our "numerical\" Donaldson-Thomas invariants as the number of certain gradient trees on the base of a complex integrable system.

Recall that a *complex integrable system* is a holomorphic map $\pi:X\to B$ where $(X,\omega^{2,0}_X)$ is a holomorphic symplectic manifold, $\dim X=2\dim B$, and the generic fiber of $\pi$ is a Lagrangian submanifold, which is a polarized abelian variety. We assume (in order to simplify the exposition) that the polarization is principal. The fibration $\pi$ is non-singular outside of a closed subvariety $B^{sing}\subset B$ of codimension at least one. It follows that on the open subset $B^{sm}:=B\setminus B^{sing}$ we have a local system ${\bf \Gamma}$ of symplectic lattices with the fiber over $b\in B^{sm}$ equal to $\Gamma_b:=H_1(X_b,\Z), X_b=\pi^{-1}(b)$ (the symplectic structure on $\Gamma_b$ is given by the polarization).

Furthermore, the set $B^{sm}$ is locally (near each point $b\in B^{sm}$) embedded as a holomorphic Lagrangian subvariety into an affine symplectic space parallel to $H_1(X_b,\C)$. Namely, let us choose a symplectic basis $\gamma_i\in \Gamma_b, 1\le i\le 2n$. Then we have a collection of holomorphic closed $1$-forms $\alpha_i=\int_{\gamma_i}\omega^{2,0}_X, 1\le i\le 2n$ in a neighborhood of $b$. There exists (well-defined locally up to an additive constant) holomorphic functions $z_i, 1\le i\le 2n$ such that $\alpha_i=dz_i, 1\le i\le 2n$. They define an embedding of a neighborhood of $b$ into $\C^{2n}$. The collection of $1$-forms $\alpha_i$ gives rise to an element $\delta\in H^1(B^{sm}, {\bf \Gamma}^{\vee}\otimes \C)$. *We assume that $\delta=0$*. This assumption is equivalent to an existence of a section $Z\in \Gamma(B^{sm},{\bf \Gamma}\otimes {\cal O}_{B^{sm}})$ such that $\alpha_i=Z(\gamma_i), 1\le i\le 2n$.

::: defn
We call $Z$ the central charge of the integrable system.
:::

Hence, for every point $b\in B^{sm}$ we have a symplectic lattice $\Gamma_b$ endowed with an additive map $Z_b:\Gamma_b\to \C$. Our goal will be to define a continuous family of stability data on graded Lie algebras $\mathfrak{g}_{\Gamma_b}$ with central charges $Z_b$.

First, we show an example of section $Z$.

::: exa
(Seiberg-Witten curve)

Let $B=\C$ be a complex line endowed with a complex coordinate $u$. We denote by $X^0=T^{\ast}\left(\C\setminus\{0\}\right)$ the cotangent bundle to the punctured line. We endow it with the coordinates $(x,y), y\ne 0$ and the symplectic form $$\omega^{2,0}=dx\wedge{dy\over{y}}\,\,.$$ There is a projection $\pi^0:X^0\to B$ given by $$\pi(x,y)={1\over{2}}(x^2-y-{c\over{y}})\,\,,$$ where $c$ is a fixed constant. Fibers of $\pi^0$ are punctured elliptic curves $$y+{c\over{y}}=x^2-2u\,\,.$$ We denote by $X$ the compactification of $X^0$ obtained by the compactifications of the fibers. We denote by $\pi:X\to B$ the corresponding projection. Then $Z_u\in H^1(\pi^{-1}(u),\C)$ is represented by a meromorphic $1$-form $\lambda_{SW}={xdy\over{y}}$ (Seiberg-Witten form). The form $\lambda_{SW}$ has zero residues, hence it defines an element of $H^1(\pi^{-1}(u),\C)$ for any $u\in B^{sm}$, where $B^{sm}=B\setminus\{b_{-},b_{+}\}$ consists of points where the fiber of $\pi$ is a non-degenerate elliptic curve.
:::

The dense open set $B^{sm}\subset B$ carries a Kähler form $$\omega_{B}^{1,1}=\op{Im}\left(\sum_{1\le i\le n}\alpha_i\wedge\overline{\alpha_{n+i}}\right)\,\,.$$ We denote by $g_{B}$ the corresponding Kähler metric.

For any $t\in \C^{\ast}$ we define an integral affine structure on $C^{\infty}$-manifold $B^{sm}$ given by a collection of closed $1$-forms $\op{Re}(t\alpha_i), 1\le i\le 2n$. For any simply-connected open subset $U\subset B^{sm}$ and a covariantly constant section $\gamma\in \Gamma(B^{sm},{\bf \Gamma})$ we have a closed $1$-form $$\alpha_{\gamma,t}=\op{Re}\left(t\int_{\gamma}\omega_X^{2,0}\right)=d\op{Re}(tZ(\gamma))\,\,,$$ and the corresponding gradient vector field $v_{\gamma,t}=g_B^{-1}(\alpha_{\gamma,t})$. Notice that this vector field is a constant field with integral direction in the integral affine structure associated with closed $1$-forms $\op{Im}(t\alpha_i), 1\le i\le 2n$.

Similarly to [@KoSo1] we can construct infinite oriented trees lying in $B$ such that its external vertices belong to $B^{sing}$, and edges are *positively oriented* trajectories of vector fields $v_{\gamma,t}$. All internal vertices have valency at least $3$, and every such vertex should be thought of as a splitting point: a trajectory of the vector field $v_{\gamma,t}$ is split at a vertex into several trajectories of vector fields $v_{\gamma_1,t},\dots,v_{\gamma_k,t}$ such that $\gamma=\gamma_1+\dots+\gamma_k$.

The restriction of the function $Z$ to a tree gives rise to a $\C$-valued function such that on the trajectory of vector field $v_{\gamma,t}$ it is equal to the restriction of $Z(\gamma)$ to this trajectory. We assume that this function approach to zero as long as we approach an external vertex of the tree (which belongs to $B^{sing}$). It is easy to see that $tZ(\gamma)$ is a positive number at any other point of the tree (hence it defines a length function). We expect that for any point $b\in B^{sm}$ and $\gamma\in \Gamma_b$ there exist finitely many such trees which pass the point $b$ in the direction of $\gamma$ (we can think of $b$ as a root of the tree, hence we can say above that we consider oriented trees such that all external vertices except of the root belong to $B^{sing}$). Here we choose an affine structure with $t\in \R_{>0}(Z(\gamma)_b^{-1})$. Probably the number of such trees for fixed $b,\gamma$ is finite, since their lengths should be bounded.[^1]

For a fixed $t\in \C^{\ast}$ the union $W_t$ of all trees as above is in fact a countable union of real hypersurfaces in $B^{sm}$. They are analogs of the walls of second kind. The set $W_t$ depends on $\op{Arg}t$ only. The union $\cup_{\theta\in [0,2\pi i)}W_{te^{i\theta}}$ swap the whole space $B^{sm}$. Let us denote by $W^{(1)}$ the union over all $t\in \C^{\ast}/\R_{>0}$ of the sets of internal vertices of all trees in $W^{(1)}$ (splitting points of the gradient trajectories). This is an analog of the wall of first kind.

In [@KoSo1] we suggested a procedure of assigning rational multiplicities to edges of trees (see also [@GS1],[@GS2]). This leads to the following picture. Consider the total space $tot({\bf \Gamma})$ of the local system ${\bf \Gamma}$. It follows from above assumptions and considerations that we have a locally constant function $\Omega:tot({\bf \Gamma})\to \Q$ which jumps at the subset consisting of the lifts of the wall $W^{(1)}$ to $tot({\bf \Gamma})$. Then for a fixed $b\in
B^{sm}$ the pair $(Z,\Omega)$ defines stability data on the graded Lie algebra $\g_{\Gamma_b}$ of the group of formal symplectomorphisms of the symplectic torus ${\mathbb T}_{\Gamma_b}$. In this way we obtain a local embedding $B^{sm}\hookrightarrow Stab(\g_{\Gamma_b})$.

In the above example of Seiberg-Witten curve, the wall $W^{(1)}$ is an oval-shaped curve which contains two singular points $b_{\pm}\in B^{sing}$. A typical $W_t$ looks such as follows.

The wall-crossing formula coincides with the one for $T_{a,b}^{(2)}$ (see Introduction).

::: rmk
1\) We expect that the above considerations are valid for a large class of complex integrable systems, e.g. Hitchin system.

2\) In the case when we have a $3d$ complex compact Calabi-Yau manifold $X$, the moduli space ${\cal M}_X$ of complex structures on $X$ is locally embedded into the projective space ${\bf P}(H^3(X,\C))$ as a base of a Lagrangian cone ${\cal L}_X\subset H^3(X,\C)$. It carries a Kähler metric (Weil-Petersson metric). We can repeat the above considerations given for integrable systems, replacing the gradient flows by the attractor flow (see e.g. [@DM]). The above case of integrable systems is obtained in the limit, when the cone becomes "very sharp\".
:::

[^1]: In [@KoSo1] we modified the gradient fields near $B^{sing}$ in order to guarantee the convergence of infinite products in the adic topology. It seems that we were too cautious, and the convergence holds without any modification.
