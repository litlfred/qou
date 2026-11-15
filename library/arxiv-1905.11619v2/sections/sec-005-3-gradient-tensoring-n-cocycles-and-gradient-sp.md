---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-005-3-gradient-tensoring-n-cocycles-and-gradient-sp
section_title: "Gradient tensoring, n-cocycles and gradient-Sp"
section_number: 3
pages: 5-8
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.956
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an analysis of quantum Markov semi-groups."
---
[]{#Sect=GradientTensor label="Sect=GradientTensor"} The aim of this section is to construct $n$-cocycles in Hochschild cohomology using quantum Markov semi-groups.

::: dfn
A **quantum Markov semi-group** $(\Phi_t)_{t \geq 0}$ on $(M, \tau)$ is a semi-group of unital completely positive maps $\Phi_t: M\rightarrow M$ that preserve the trace, i.e. $\tau \circ \Phi_t = \tau$ for all $t \geq 0$. Further we assume that $\Phi_t$ is symmetric $\tau(\Phi_t(x) y) = \tau(x \Phi_t(y)), x,y \in M$. Moreover, we assume that for every $x \in M$ the map $t \mapsto \Phi_t(x)$ is continuous for the strong topology of $M$.
:::

## Gradient tensoring

Let $(\Phi_t)_{t \geq 0}$ be a quantum Markov semi-group on $M$. Let $$\Phi_t^{(2)}: L_2(M) \rightarrow L_2(M): x \Omega_\tau \mapsto \Phi_t(x) \Omega_\tau,$$ be the corresponding semi-group on $L_2(M)$. Let $\Delta \geq 0$ be its generator, i.e. $\Delta$ is the unbounded positive (self-adjoint) operator on $L_2(M)$ such that $$\exp(-t \Delta) =  \Phi_t^{(2)}$$ as a semi-group on $L_2(M)$.

We shall assume that there exists a $\sigma$-weakly dense $\ast$-subalgebra $\mathcal{A}$ of $M$ such that $\mathcal{A}\Omega_\tau$ is contained in the domain of $\Delta$ and moreover $\Delta(\mathcal{A}\Omega_\tau) \subseteq \mathcal{A}\Omega_\tau$. We simply write $\Delta(a), a \in \mathcal{A}$ for the map $\Delta$ on the level of $\mathcal{A}$. We assume moreover that for every $a \in \mathcal{A}$ the map $t \mapsto \Phi_t(a)$ is norm continuous. Let $$A := \overline{\mathcal{A}}^{\Vert \: \cdot \: \Vert}$$ be the C$^\ast$-closure of $\mathcal{A}$. In general we cannot guarantee the existence of such an algebra $\mathcal{A}$, but in many concrete cases it exists. The assumption should be compared to similar assumptions and remarks made in [@CiprianiFagnola Section 5], [@JungeMei] or [@CaspersGradient].

We introduce the following definition, which is in principle $\mathcal{A}$-dependent. For $p = 2$ it was introduced in [@CaspersGradient].

::: dfn
[]{#Dfn=GradientSp label="Dfn=GradientSp"} Let $1 \leqslant p \leqslant \infty$. We say that a quantum Markov semi-group $(\Phi_t)_{t \geq 0}$ is **immediately gradient-$\mathcal{S}_p$** if for every $a,b \in \mathcal{A}$ and every $t > 0$ we have that $$\label{Eqn=GradientMap}
  \Psi^{a,b}_t: x  \mapsto -\frac{1}{2} \Phi_t \left(  \Delta(ax b) + a \Delta(x) b - \Delta(ax) b - a \Delta(xb)   \right),$$ extends to a bounded map $x \Omega_\tau \mapsto \Psi^{a,b}_t(x) \Omega_\tau$ on $L_2(M)$ that is moreover in $\mathcal{S}_p$. $(\Phi_t)_{t \geq 0}$ is **gradient-$\mathcal{S}_p$** if for every $a, b \in \mathcal{A}$ the map [\[Eqn=GradientMap\]](#Eqn=GradientMap){reference-type="eqref" reference="Eqn=GradientMap"} is in $\mathcal{S}_p$ for $t = 0$. We set $\Psi^{a,b} = \Psi^{a,b}_0$.
:::

::: example
We illustrate Definition [\[Dfn=GradientSp\]](#Dfn=GradientSp){reference-type="ref" reference="Dfn=GradientSp"} by a simple (counter)example. Suppose that $\mathbb{T}$ is the torus seen as the unit circle in $\mathbb{C}$. Let $e_k(z) = z^k, z \in \mathbb{T}$. Let $\mathcal{A}$ be the span of $e_k, k \in \mathbb{Z}$, i.e. the $\ast$-algebra of trigonometric polynomials. Set $M= L_\infty(\mathbb{T})$.

-   Let $\Delta$ be the Laplacian given by $\Delta(e_k) = k^2 e_k$ which generates the **heat semi-group** $(e^{-t \Delta})_{t \geq 0}$. This semi-group is not gradient-$\mathcal{S}_p$ for any $1 \leq p \leq \infty$. Indeed, we find that $$\Psi^{e_l, e_m}(e_k) = -\frac{1}{2} ( (l+k+m)^2 + k^2 - (l+k)^2 - (k+m)^2 )   e_{l + k + m} = - lm \: e_{l + k + m},$$ and this map is not even compact on $L_2(\mathbb{T})$ unless $lm = 0$.

-   However, if we consider the **Poisson semi-group** $(e^{-t \Delta^{\frac{1}{2}}})_{t \geq 0}$ then we find, $$\Psi^{e_l, e_m}(e_k) = -\frac{1}{2} ( \vert l+k+m \vert + \vert k \vert - \vert l+k \vert - \vert k+m \vert )   e_{l + k + m},$$ which is 0 as soon as $\vert k\vert \geq \vert l \vert + \vert m \vert$. Therefore $\Psi^{e_l, e_m}$ is finite rank and therefore $(e^{-t \Delta^{\frac{1}{2}}})_{t \geq 0}$ is gradient-$\mathcal{S}_p$ for every $p \in [1, \infty]$.
:::

::: rmk
Morally, one can expect that a quantum Markov semi-group is gradient-$\mathcal{S}_p$ if the eigenvalues of the generator grow (almost) linearly (like for the Poisson semi-group) and if there is not too much interaction between the operators $a$ and $b$ in an expression $axb$ if $x$ has a very large 'length' (this obviously requires more structure to explain in more detail). The current paper gives quantitative examples of this, see Section [\[Sect=Orhnstein-Uhlenbeck\]](#Sect=Orhnstein-Uhlenbeck){reference-type="ref" reference="Sect=Orhnstein-Uhlenbeck"} and Theorem B of Section [\[Sect=Intro\]](#Sect=Intro){reference-type="ref" reference="Sect=Intro"}. More examples as well as stability properties for gradient-$\mathcal{S}_2$ for free products were given in [@CaspersGradient].
:::

In [@CiprianiSauvageot] the following bimodule is constructed. We set the **gradient form** (or **carré du champ**), $$\Gamma(x,y) = \frac{1}{2}( \Delta(y)^\ast x + y^\ast  \Delta(x) - \Delta(y^\ast x) ), \qquad x,y \in \mathcal{A},$$ which we view as an $\mathcal{A}$-valued inner product. Let $H$ be any $A$-$A$-bimodule. Equip the algebraic tensor product $\mathcal{A} \otimes_{{\rm alg}}H$ with the (degenerate) inner product $$\langle x \otimes \xi, y \otimes \eta \rangle =  \langle \Gamma(x,y) \xi, \eta  \rangle, \qquad x,y \in \mathcal{A}, \xi, \eta \in H.$$ The Hilbert space obtained by quotienting out the degenerate part and taking the completion will be called the **gradient tensor product** which we denote by $H_\nabla$. We will denote by $a \otimes_\nabla\xi, a \in \mathcal{A}, \xi \in H$ the class of $a \otimes \xi$ in $H_\nabla$. $H_\nabla$ has an $\mathcal{A}$-$\mathcal{A}$ bimodule structure given by the left action $$\label{Eqn=LeftAction}
  x \cdot (y \otimes_\nabla\xi) = xy \otimes_\nabla\xi - x \otimes_\nabla y \xi, \qquad x,y \in \mathcal{A}, \xi \in H,$$ and the right action $$\label{Eqn=RightAction}
  (y \otimes_\nabla\xi ) \cdot x = y \otimes_\nabla\xi x, \qquad x,y \in \mathcal{A}, \xi \in H.$$

::: prop
[]{#Prop=Module label="Prop=Module"} The left and right actions defined in [\[Eqn=LeftAction\]](#Eqn=LeftAction){reference-type="eqref" reference="Eqn=LeftAction"} and [\[Eqn=RightAction\]](#Eqn=RightAction){reference-type="eqref" reference="Eqn=RightAction"} are well-defined contractive left and right actions of $\mathcal{A}$ that moreover commute. That is, $H_\nabla$ is an $A$-$A$-bimodule where $A$ is the C$^\ast$-closure of $\mathcal{A}$.
:::

::: proof
*Proof.* The proof in case $H = L_2(M)$ is the trivial $M$-$M$-bimodule is given as [@CiprianiSauvageot Lemma 3.5]. But in fact the same proof works for any $A$-$A$-bimodule $H$. Note that the proof that the right action is contractive is straightforward. ◻
:::

::: dfn
We call $(\Phi_t)_{t \geq 0}$ **gradient coarse** if the $A$-$A$-bimodule actions on $L_2(M)_{\nabla}$ extend to normal $M$-$M$-bimodule actions and further $L_2(M)_{\nabla}$ is weakly contained in the coarse bimodule of $M$.
:::

By Proposition [\[Prop=Module\]](#Prop=Module){reference-type="ref" reference="Prop=Module"} for an $A$-$A$-bimodule $H$ we may define $$H_{\nabla^{(n)}} = ((H_{\nabla})_{\nabla} \ldots )_\nabla,$$ for the $n$-fold application of $H \mapsto H_\nabla$. The following connects the map [\[Eqn=GradientMap\]](#Eqn=GradientMap){reference-type="eqref" reference="Eqn=GradientMap"} to the bimodule structure defined above.

::: lem
[]{#Lem=GradientComp label="Lem=GradientComp"} Let $H$ be an $A$-$A$-bimodule. For $x, y, a, b \in \mathcal{A}$ and $\xi, \eta \in H$ we have, $$\langle  x \cdot (a \otimes_\nabla\xi) \cdot y, b \otimes_\nabla\eta   \rangle =
         \langle  \Psi^{b^\ast, a}(x) \xi y, \eta \rangle.$$
:::

::: proof
*Proof.* Indeed, we find that, $$\begin{split}
    \langle  x \cdot (a \otimes_\nabla\xi) \cdot y, b \otimes_\nabla\eta   \rangle = &
    \langle    (xa \otimes_\nabla\xi y - x \otimes_\nabla a \xi y), b \otimes_\nabla\eta \rangle \\
    = &
    \langle  (\Gamma(xa, b) - \Gamma(x, b)a) \xi y,  \eta \rangle \\
    = &
    \frac{1}{2} \langle  (
    \Delta(b^\ast) xa + b^\ast \Delta(xa) - \Delta(b^\ast xa)
    - \Delta(b^\ast )xa - b^\ast \Delta(x) a + \Delta(b^\ast x) a )\xi y ,  \eta \rangle    \\
    = &
    \langle  \Psi^{b^\ast, a}(x) \xi y, \eta \rangle.
    \end{split}$$ This concludes the proof. ◻
:::

::: rmk
[]{#Rmk=Positive label="Rmk=Positive"} Let $H$ be an $A$-$A$-bimodule and let $\xi \in H$. Then the functional on $A \otimes_{{\rm max}} A^{{\rm op}}$ given by $x \otimes y^{{\rm op}} \mapsto \langle x \xi y , \xi \rangle$ is positive and therefore also its restriction to $A \otimes_{{\rm alg}} A^{{\rm op}} \rightarrow \mathbb{C}$ sends elements of the form $x^\ast x$ with $x \in A \otimes_{{\rm alg}} A^{{\rm op}}$ to non-negative reals. Therefore if this map is $\otimes_{{\rm min}}$ continuous we obtain a positive map $A \otimes_{{\rm min}}A^{{\rm op}} \rightarrow \mathbb{C}$.
:::

For any $n\in \mathbb{N}_{\geq 1}$, we say that a vector $\xi \in L^2(M)_{\nabla^{(n)}}$ is *algebraic* if it is contained in a linear span of elements of $a_0\otimes_\nabla a_1\otimes_\nabla \cdots \otimes_\nabla a_n$ for some $a_0,\ldots,a_n\in \mathcal A$.

::: thm
[]{#Thm=IGHS-GC label="Thm=IGHS-GC"} Let $n \in \mathbb{N}_{\geq 1}$. Suppose that the quantum Markov semi-group $\Phi = (\Phi_t)_{t \geq 0}$ is gradient-$\mathcal{S}_p$ for $p = 2 n$.

Then for any algebraic $\xi \in L_2(M)_{\nabla^{(n)}}$, $\overline{A\xi A}$ is contained in the coarse bimodule $L_2(M) \otimes L_2(M)$ as $A$-$A$ bimodules.

In particular, $L_2(M)_{\nabla^{(n)}}$ is contained in an infinite multiple of the coarse bimodule $L_2(M) \otimes L_2(M)$ as $A$-$A$ bimodules and the $A$-$A$ bimodule actions on $L_2(M)_{\nabla^{(n)}}$ extend to normal $M$-$M$ bimodule actions via this embedding.
:::

::: proof
*Proof.* Take $a_0, a_1, \ldots,  a_n, b_0, b_1, \ldots, b_n \in \mathcal{A}$. Consider vectors $\alpha := a_0 \otimes \ldots \otimes a_{n-1} \otimes a_n \Omega_\tau, \beta := b_0 \otimes \ldots \otimes b_{n-1} \otimes b_n \Omega_\tau  \in L_2(M)_{\nabla^{(n)}}$. For $x, y \in \mathcal{A}$ we get from Lemma [\[Lem=GradientComp\]](#Lem=GradientComp){reference-type="ref" reference="Lem=GradientComp"} that, $$\begin{split}
    \langle x \cdot \alpha \cdot y, \beta \rangle
    = & \langle x \cdot (  a_0 \otimes_\nabla\ldots \otimes_\nabla a_{n-1} \otimes_\nabla a_n \Omega_\tau ) \cdot y,  b_0 \otimes_\nabla\ldots \otimes_\nabla b_{n-1} \otimes_\nabla b_n \Omega_\tau \rangle  \\
 = &
    \langle
    \Psi^{b_{n-1}^\ast, a_{n-1}} \circ   \ldots \circ  \Psi^{b_1^\ast, a_1} \circ  \Psi^{b_0^\ast, a_0}(x)  a_n \Omega_\tau y, b_n \Omega_\tau  \rangle \\
    = &  \langle b_n^{\ast}
    \Psi^{b_{n-1}^\ast, a_{n-1}} \circ   \ldots \circ  \Psi^{b_1^\ast, a_1} \circ  \Psi^{b_0^\ast, a_0}(x)  a_n \Omega_\tau  ,  \Omega_\tau y^\ast \rangle \\
    = & \langle b_n^{\ast}
    \Psi^{b_{n-1}^\ast, a_{n-1}} \circ   \ldots \circ  \Psi^{b_1^\ast, a_1} \circ  \Psi^{b_0^\ast, a_0}(x)  a_n \Omega_\tau  ,  y^\ast \Omega_\tau \rangle,
    \end{split}$$ where the last equality uses the fact that $\Omega_{\tau} y^{\ast} = y^{\ast} \Omega_{\tau}$.

Since each $\Psi^{b_j^\ast, a_j}$ is an element of $\mathcal{S}_p$ with $p = 2n$ we find that $$\Psi :=   \Psi^{b_{n-1}^\ast, a_{n-1}} \circ   \ldots \circ  \Psi^{b_1^\ast, a_1} \circ  \Psi^{b_0^\ast, a_0} \in \mathcal{S}_2.$$ Then also $x \Omega_\tau \mapsto  b_n^\ast \Psi(x) a_n\Omega_\tau$ is in $\mathcal{S}_2$. Therefore, there exists $\zeta_{\alpha, \beta}  \in  L_2(M) \otimes \overline{ L_2(M) }$ such that, $$\label{Eqn=MinBd}
            \langle x \cdot \alpha \cdot y, \beta \rangle =
    \langle x \Omega_\tau \otimes  \overline{ y^{\ast}} \overline{\Omega_{\tau}},  \zeta_{\alpha, \beta}   \rangle$$ Since the map $M^{{\rm op}} \ni y^{{\rm op}} \mapsto \overline{y^{\ast}} \in \overline{M}$ is a $\ast$-isomorphism, we deduce that assigning [\[Eqn=MinBd\]](#Eqn=MinBd){reference-type="eqref" reference="Eqn=MinBd"} to $x \otimes y^{{\rm op}} \in M \otimes_{{\rm alg}} M^{{\rm op}}$ is $\otimes_{{\rm min}}$-bounded and moreover normal.

Now take any algebraic $\alpha \in L^2(M)_{\nabla^{(n)}}$. The previous paragraph shows that the map $\rho: M \otimes M^{{\rm op}}: x \otimes y^{{\rm op}} \rightarrow \langle x \cdot \alpha \cdot y, \alpha \rangle$ extens to $M \overline{\otimes}M^{{\rm op}}$. Moreover, $\rho$ is positive on $\mathcal{A}\otimes_{{\rm alg}} \mathcal{A}^{{\rm op}} \rightarrow \mathbb{C}$, see Remark [\[Rmk=Positive\]](#Rmk=Positive){reference-type="ref" reference="Rmk=Positive"}. We claim that $\rho$ is also a positive map $M \overline{\otimes}M^{{\rm op}} \rightarrow \mathbb{C}$. Indeed, take $z \in M \overline{\otimes}M^{{\rm op}}$ positive and write $z = d^\ast d, d \in M \overline{\otimes}M^{{\rm op}}$. By Kaplansky's density theorem, let $d_j \in \mathcal{A}\otimes \mathcal{A}^{{\rm op}}$ be a bounded net converging strongly to $d$. Then $d_j^\ast d_j \rightarrow d^\ast d = z$ weakly and hence $\sigma$-weakly since these topologies coincide on the unit ball. Since $\rho$ is normal (i.e. $\sigma$-weakly continuous), we get $0 \leq \rho(d_j^\ast d_j) \rightarrow \rho(z)$. Since $L_2(M) \otimes L_2(M)$ is the standard Hilbert space for $M \overline{\otimes}M^{{\rm op}}$ there exists $\zeta_{\alpha} \in L_2(M) \otimes L_2(M)$ such that $\langle x \cdot \alpha \cdot y, \alpha \rangle = \langle x \cdot \zeta_{\alpha} \cdot y, \zeta_\alpha \rangle$. As algebraic vectors in $L^2(M)_{\nabla^{(n)}}$ form a dense subspace, we conclude by Lemma [\[Lem=Containment\]](#Lem=Containment){reference-type="ref" reference="Lem=Containment"}. ◻
:::

::: cor
[]{#Cor=GradientCoarseConsequence label="Cor=GradientCoarseConsequence"} Suppose that the quantum Markov semi-group $(\Phi_t)_{t \geq 0}$ is gradient-$\mathcal{S}_2$; then it is gradient coarse.
:::
