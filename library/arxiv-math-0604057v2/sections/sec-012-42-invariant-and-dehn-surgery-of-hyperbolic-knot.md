---
doc_id: arxiv-math-0604057v2
doc_title: "Volume conjecture, regulator and SL2(C)-character variety of a knot"
section_id: sec-012-42-invariant-and-dehn-surgery-of-hyperbolic-knot
section_title: "Invariant and Dehn Surgery of Hyperbolic Knots"
section_number: 4.2
pages: 9-12
source_pdf: 0604057v2.pdf
source_sha256: 649fad141dc34eb9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.978
doc_brief: "Volume conjecture, regulator and SL2(C)-character variety of a knot — In this paper, by using the regulator map of Beilinson-Deligne, we show that the quan- tization condition posed by Gukov is true"
---
In this subsection, we define an algebro-geometric invariant of the $3$-manifolds $K(p/q)$ resulting from the $(p,q)$ Dehn surgery along a hyperbolic knot complement in $S^3$. A Casson type $SL_2(\mathbb{C})$ invariant for $K(p/q)$ is also established.

Let $A_0(m,l)$ be the defining equation of the closure of the affine curve $D_0$ in $\mathbb{C}\times \mathbb{C}$. We also require that it has no repeated factors. It is a factor of the $A$-polynomial of the knot $K$ defined in [@CCGLS], and $A_0(m,l)^d$ is the $A$-polynomial of $X_0$ defined in [@BZ Page 109], where $d$ is the degree of regular map $r:X_0\rightarrow Y_0$.

Denote by $\widetilde{X_0}$ (resp. $\widetilde{Y_0}$) a smooth projective model of the affine curve $X_0$ (resp. $Y_0$). The restriction morphism $r:X_0\rightarrow Y_0$ induces a regular map $\widetilde{r}: \widetilde{X_0}\rightarrow \widetilde{Y_0}$.

::: lemma
[]{#le1 label="le1"} The regular map $\widetilde{r}$ is an isomorphism.
:::

::: proof
*Proof.* By our assumption, $M_K$ is the complement of a knot in $S^3$, hence $H^1(M_K;\mathbb{Z}_2)=\mathbb{Z}_2$. By [@Dun Corollary 3.2], $r$ is a birational isomorphism onto $r(X_0)$. Since $\widetilde{r}$ is induced by $r$, the result follows. ◻
:::

Let $\gamma=p\mu+q\lambda\in H_1(\partial M_K;\mathbb{Z})$ be a non-zero primitive element with $p,q$ coprime. Define a regular function $f_{\gamma}=I_{\gamma}^2-4$ on $X_0$. Since $I_{\gamma}$ is nonconstant, so is $f_{\gamma}$. It is also a meromorphic function on $\widetilde{X_0}$ or equivalently, a non-constant holomorphic function from $\widetilde{X_0}$ to $\mathbb{CP}^1$ and we denote it again by $f_{\gamma}$ .

Since $\gamma\in H_1(\partial M_K;\mathbb{Z})$, we can think of $I_{\gamma}$ as a regular function on $Y_0$ in $X(\partial M)$. Define on $Y_0$ the function $f_{\gamma}^{\prime}=I_{\gamma}^2-4$. Similarly, it is a non-constant regular function on $Y_0$, and hence a non-constant holomorphic function from $\widetilde{Y_0}$ to $\mathbb{CP}^1$, denoted also by $f_{\gamma}^{\prime}$. Then by the definition, we have $$f_{\gamma}=f_{\gamma}^{\prime}\circ \widetilde{r}.$$ In particular, $\text{deg}f_{\gamma}=\text{deg}f_{\gamma}^{\prime}$ by Lemma [\[le1\]](#le1){reference-type="ref" reference="le1"}.

We denote by $Z_{\gamma}$ the set of zeroes of the function $f_{\gamma}$ on $X_0$. If $\chi\in Z_{\gamma}$, then there exists a representation $\rho\in R_0$ such that its character $\chi_\rho=\chi$.

::: lemma
[]{#le2 label="le2"} Suppose $\chi_\rho\in Z_{\gamma}$. Then either $\rho(\gamma)=\pm
\text{I}$ or $\rho(\gamma)\ne \pm I$ and $\sigma(\rho(\alpha))=\pm
2$ for all $\alpha\in \pi_1(\partial M_K)$.
:::

::: proof
*Proof.* Note that $f_{\gamma}(\chi_\rho)=0$ is equivalent to that the trace of $\rho(\gamma)$ is $\pm 2$. If $\rho(\gamma)\ne \pm I$, then $\rho(\gamma)$ is a parabolic element in $SL_2(\mathbb{C})$. Since $\rho(\gamma)$ and $\rho(\alpha)$ commute for all $\alpha\in
\pi_1(\partial M_K)$, $\sigma(\rho(\alpha))=\pm 2$. ◻
:::

Suppose that $\rho\in R_0\subset R(M_K)$ is irreducible. Then its character $\chi_{\rho}$ is contained in the component $X_0$. Assume that $\rho(\mu)$ and $\rho(\lambda)$ are parabolic. Up to conjugation, we have $$\rho(\mu)=\pm
  \left[
  \begin{matrix}
    1 & 1\\
    0 & 1
  \end{matrix}
  \right]; \;\;
\rho(\lambda)=\pm
  \left[
  \begin{matrix}
    1 & t(\rho)\\
    0 & 1
  \end{matrix}
  \right],$$

where $t(\rho)$ is a complex number. We have the following:

::: conjecture
Let $\rho\in R_0$ be an irreducible $SL_2(\mathbb{C})$-representation of a hyperbolic knot in $S^3$. If $\rho(\mu)$ and $\rho(\lambda)$ are parabolic, then $t(\rho)\notin \mathbb{Q}$.
:::

::: remark
\(1\) If $\rho=\rho_0$ is the discrete faithful representation of the hyperbolic structure, then we know $\rho(\mu)$ and $\rho(\lambda)$ are parabolic and $t(\rho_0)$ is called the *cusp constant* and the *cusp polynomial* is the minimum polynomial for $t(\rho_0)$ over $\mathbb{Q}$. Moreover $\{1,
t(\rho_0)\}$ generates a lattice of $\mathbb{C}$. Therefore, $t(\rho_0)\notin \mathbb{R}$. For more detail, see [@CL Section 6]. So $t(\rho)$ can be thought of as the generalization of the cusp constant.

\(2\) The conjecture can not be extended to non-hyperbolic knots. There is an example in [@Ril1 Section 5] of an irreducible parabolic representation $\rho$ of alternating torus knot such that $t(\rho)\in \mathbb{Z}$.
:::

The conjecture is true for the figure-eight knot. In fact, for the figure-eight knot, by Proposition [\[8cha-1\]](#8cha-1){reference-type="ref" reference="8cha-1"}, if $\rho$ satisfies the condition of the conjecture, then it must be the discrete faithful representation of the hyperbolic structure. By the remark, $t(\rho)\notin \mathbb{R}$.

::: proposition
[]{#kin label="kin"} Suppose the above conjecture is true. Let $\gamma=p\mu+q\lambda\in
H_1(\partial M_K;\mathbb{Z})$ with $p,q$ non-zero coprime integers. Let $\chi_{\rho}\in Z_{\gamma}$ be the character of an irreducible representation $\rho$. Then $\rho(\gamma)=\pm I$ if and only if the trace of $\rho(\mu)$ is not equal to $\pm 2$.
:::

::: proof
*Proof.* If the trace of $\rho(\mu)$ is not equal to $\pm 2$, then $\rho(\mu)$ is not parabolic or $\pm I$. Since $\rho(\mu)$ and $\rho(\gamma)$ commute, $\rho(\gamma)$ is not parabolic. Since $\chi_{\rho}\in Z_{\gamma}$, $\sigma(\rho(\gamma))=\pm 2$. Thus, we obtain $\rho(\gamma)=\pm I$.\
Next suppose that the trace of $\rho(\mu)$ is equal to $\pm 2$. We show that $\rho(\gamma)\ne \pm I$. There are two cases.\
Case I. $\rho(\mu)=\pm I$. We know that the $1/0$ Dehn surgery produces $S^3$. Hence $\rho$ induced a representation of $\pi_1(S^3)$ in $PSL_2(\mathbb{C})$. It is trivial. Therefore, the image of $\rho$ in $SL_2(\mathbb{C})$ is contained in $\{\pm I\}$. So $\rho$ is reducible. This contradiction shows that Case I can not happen.\
Case II. $\rho(\mu)$ is parabolic. Since $\rho(\mu)$ and $\rho(\lambda)$ commute, up to conjugation, we can assume that $$\rho(\mu)=\pm
  \left[
  \begin{matrix}
    1 & 1\\
    0 & 1
  \end{matrix}
  \right], \;\;
\rho(\lambda)=\pm
  \left[
  \begin{matrix}
    1 & t(\rho)\\
    0 & 1
  \end{matrix}
  \right].$$

Now $\gamma=p\mu+q\lambda$, so $\rho(\gamma)=\rho(\mu)^p\rho(\lambda)^q$. If $t(\rho)=0$, $\rho(\gamma)\ne \pm I$ unless $p=0$. If $t(\rho)\ne 0$, by the assumption $t(\rho)\notin \mathbb{Q}$, then $\rho(\gamma)\ne \pm
I$. ◻
:::

::: proposition
[]{#redu label="redu"} Suppose $\chi\in Z_{\gamma}$ is the character of a reducible representation $\rho$. Then $\chi(\mu)\ne \pm 2$ and $\rho(\gamma)=\pm I$.
:::

::: proof
*Proof.* Let $m$ be an eigenvalue of $\rho(\mu)$. By [@CCGLS Proposition 6.2], $m^2$ must be a root of the Alexander polynomial $\Delta(t)$ of the knot. It is well-known that $\Delta(1)\ne 0$, hence $m\ne \pm 1$ and $\chi(\mu)\ne \pm
2$. This also means that $\rho(\mu)$ is not parabolic or $\pm I$. Since $\rho(\mu)$ and $\rho(\gamma)$ commute and the trace of $\rho(\gamma)$ is $\pm 2$, we must have $\rho(\gamma)=\pm I$. ◻
:::

::: remark
Compare with Proposition [\[kin\]](#kin){reference-type="ref" reference="kin"}, for the reducible characters, it is much simpler and there is no need of the conjecture.
:::

Let $E(p,q)$ be the reducible curve $m^pl^q=\pm 1$ in $\mathbb{C}^{*}\times \mathbb{C}^{*}$ for $p,q$ coprime integers. Then the image $t_D(E(p,q))$ is a curve in $X(\partial M_K)$. We know $r(X_0)$ is an irreducible curve in $X(\partial M_K)$. They do not have common irreducible component because the traces of characters of $X_0$ are not constant. Hence $t_D(E(p,q))\cap
r(X_0)$ is finite. The set $t_D(E(p,q))\cap r(X_0)$ consists of possible characters in $X_0$ which can also be the characters of $K(p/q)$, where $K(p/q)$ denotes the closed $3$-manifold obtained from $M_K$ by the Dehn surgery along the simple closed curve of $\partial M_K$ which represents the class $\gamma$ in $H_1(\partial M_K;\mathbb{Z})$. The following definition should be thought of as the *algebro-geometric* invariant for the $(p,q)$ Dehn surgery of $M_K$.

::: definition
$$b(p,q)=\sum_{\chi\in t_D(E(p,q))\cap r(X_0)}n_{\chi},$$ where $n_{\chi}$ is the intersection multiplicity at $\chi$.
:::

::: theorem
[]{#b-inv label="b-inv"} The integer $b(p,q)$ is a well-defined invariant of the $3$-manifold $K(p/q)$ resulting from the Dehn filling on the hyperbolic knot complement $M_K$. It is always positive.
:::

::: proof
*Proof.* As mentioned above, the set $t_D(E(p,q))\cap r(X_0)$ is finite and hence $b(p,q)<\infty$. On the other hand, because $\chi_{\rho_0}(\mu)=\pm 2$, $\chi_{\rho_0}$ is always contained in this set, where $\rho_0\in R_0$ is the discrete faithful representation of the hyperbolic metric. Therefore, $b(p,q)>0$.

The intersection between $t_D(E(p,q))$ and $r(X_0)$ is taking place in the surface $X(\partial M_K)$ described in Proposition [\[torus\]](#torus){reference-type="ref" reference="torus"}. If two hyperbolic knots $K_1$ and $K_2$ are homeomorphic, then they have the isomorphic fundamental groups of their complements in $S^3$, hence they have isomorphic $X_0$. Therefore, they have the same $b(p,q)$. Thus $b(p,q)$ is an invariant of $K(p/q)$ depending only on the hyperbolic knot $K$ and the Dehn surgery coefficient $p/q$. ◻
:::

Now set $S(p,q)=\{\chi\in t_D(E(p,q))\cap r(X_0)|\chi(\mu)\ne \pm
2\}\subset r(X_0)\subset X(\partial M)$.

::: proposition
[]{#count label="count"} Suppose the conjecture 1 is true. Then $S(p,q)$ is exactly the set of characters in $X_0$ which are also the characters of $K(p/q)$.
:::

::: proof
*Proof.* This follows from the definition of $S(p,q)$ and Proposition [\[kin\]](#kin){reference-type="ref" reference="kin"}. ◻
:::

::: definition
[]{#lambda label="lambda"} $$\lambda (p,q)=\sum_{\chi\in S(p,q)} n_{\chi},$$ where $n_{\chi}$ is the intersection multiplicity at $\chi$.
:::

By Proposition [\[redu\]](#redu){reference-type="ref" reference="redu"}, the set $S(p,q)$ contains all possible reducible characters. Hence the number $\lambda (p,q)$ counts both irreducible and reducible characters of $K(p/q)$. From the mathematical physics point of view in [@Guk], it is important to count both irreducible and reducible representations in $SL_2(\mathbb{C})$ case. It is easy to count the abelian and non-abelian reducible characters, so there is a computable way to count the irreducible characters for $K(p/q)$.

::: theorem
[]{#c-inv label="c-inv"} Assume the conjecture 1 is true. The quantity $\lambda (p,q)$ is a well-defined *algebro-geometric* $SL_2(\mathbb{C})$ Casson type invariant of $K(p/q)$.
:::

::: proof
*Proof.* It follows from Theorem [\[b-inv\]](#b-inv){reference-type="ref" reference="b-inv"} and Proposition [\[count\]](#count){reference-type="ref" reference="count"}. ◻
:::

Note that by definition, $\lambda (p,q)\leq b(p,q)$ for any coprime $p$, $q$ and a hyperbolic knot in $S^3$.

The invariant $\lambda (p,q)$ is for the hyperbolic knot and its $(p,q)$ Dehn surgery. An $SL_2(\mathbb{C})$ knot invariant obtained from the character variety of $1$-dimensional components is given by the first author in [@Li]. The construction in [@Li] was purely topological by choosing generic smooth perturbations and generic values of $\chi(\mu)$. The topological definition of the Casson-type invariant is not easy to calculate. Our invariant $\lambda (p,q)$, defined via the intersection multiplicity, is easier or at least very explicit for computation. It can also be interpreted as the intersection cycles of the appropriate cohomology classes of $X(\partial M)$.

::: proposition
[]{#prop-liv label="prop-liv"} If $\lambda (p,q)>0$, then $\pi_1(K(p/q))$ is non-cyclic.
:::

::: proof
*Proof.* (1) If $\lambda (p,q)>0$, then there exists $\rho\in R_0$ such that its character $\chi_{\rho}\in S(p,q)$. Hence $F_{\mu}(\chi_{\rho})\ne 0$, and $F_{\gamma}(\chi_{\rho})=0$. By [@CGLS Proposition 1.5.2], there exists a representation from $\pi_1(K(p/q))$ to $PSL_2(\mathbb{C})$ with non-cyclic image. The result follows. ◻
:::

::: remark
\(1\) Our invariant $\lambda (p,q)$ is defined as the algebraic intersection multiplicity in $X(\partial M)$ from the $X_0$ component. This is different from the definition in [@Cu1] where the number $\lambda(K_{p/q})$ is defined over all components of $X(M)$ and the intersection is taken in different space.\
(2) For hyperbolic knot $K$, $K(p/q)$ may not be NSL manifold. For the component $X_0$, the intersection in [@Cu1] is $r(X_0)\cap
(t_D(t_D^{-1}(\overline{r(X_0)})\cap \{m^pl^q=1\}))$. This is different from our Definition [\[lambda\]](#lambda){reference-type="ref" reference="lambda"}. Moreover, the intersection multiplicity of an intersection point in $X(\partial
M_K)$ is counted by its multiplicity in $X(K(p/q))$ via an appropriate Heegaard splitting of $K(p/q)$ in [@Cu1].\
(3) It would be interesting to prove that the two character varieties of Heegaard handle-bodies are smooth and their intersection is always proper. In [@FM Section 4], Fulton and MacPherson only sketched an argument that if the two smooth subvarieties intersect properly, then the topological intersection multiplicity agrees with the algebraic intersection multiplicity .
:::

In [@CGLS Section 1.4], a norm $|.|$ is defined on the real vector space $H_1(\partial M_K,\mathbb{R})$ with the property that $|\gamma|=\text{deg}f_{\gamma}$ for any $\gamma\in H_1(\partial
M_K,\mathbb{Z})$. This norm is called the Culler-Shalen norm. In particular, $|\gamma|=\text{deg}f_{\gamma}^{\prime}$.

Let $\pi: \widetilde{Y_0}\rightarrow Y_0$ be the birational isomorphism. Note that $\pi$ is well-defined only on a Zariski dense subset of $\widetilde{Y_0}$ and is surjective. A point of the set $I=\widetilde{Y_0}\setminus  \pi^{-1}(Y_0)$ is called an ideal point. Denote by $Z_{\gamma}^{\prime}$ the set of zeroes of the meromorphic function $f_{\gamma}^{\prime}:\widetilde{Y_0}\rightarrow \mathbb{C}$. Then $$\text{deg}f_{\gamma}^{\prime}=\sum_{y\in
  Z_{\gamma}^{\prime}}v_y,$$ where $v_y$ is the order of vanishing of $f_{\gamma}^{\prime}$ at $y$.\
Set $Z_1=\{y\in Z_{\gamma}^{\prime}|\pi(y)\in S(p,q)\}$ and $I(p,q)=Z_{\gamma}^{\prime}\cap I$. Now we have another quantity: $$\label{v-num}
  \widehat{\lambda}(p,q)=\sum_{y\in Z_1}v_y.$$ The natural question is to find the relationship between $\widehat{\lambda}(p,q)$ and $\lambda(p,q)$ of the Definition [\[lambda\]](#lambda){reference-type="ref" reference="lambda"}. It seems that there is no easy answer to this question. See the remark below. Nevertheless, we have the following:

::: proposition
[]{#deg-ine label="deg-ine"} Assume that for every $\chi\in S(p,q)$, $t_D(E(p,q))$ intersects $r(X_0)$ transversely at $\chi$. Then\
(i) $\lambda(p,q)\leq \widehat{\lambda}(p,q)$,\
(ii) $\lambda(p,q)+\widehat{I}(p,q)\leq \text{deg}f_{\gamma}$, where $\widehat{I}(p,q)=\sum_{x\in I(p,q)}v_x$.
:::

::: proof
*Proof.* If the intersection is transverse, then intersection multiplicity $n_{\chi}=1$. The order of vanishing is at least one, hence (i) holds.

For (ii), note that $Z_1$ and $I(p,q)$ are subsets of $Z_{\gamma}^{\prime}$. Thus, $\lambda(p,q)+\widehat{I}(p,q)\leq
\text{deg}f_{\gamma}^{\prime}=\text{deg}f_{\gamma}$. ◻
:::

::: remark
If the intersection is not transversal, for instance, some $\chi$ is a singular point of $r(X_0)$, then we do not know how to compare them. One difficulty is that when $\chi$ is a singular point, there is NO well-defined notion of the order of vanishing of $f_{\gamma}^{\prime}$ at $\chi$ in $Y_0$. Moreover, $\pi^{-1}(\chi)$ has more than one element in $\widetilde{Y_0}$ and each of them is a zero of $f_{\gamma}^{\prime}$.
:::
