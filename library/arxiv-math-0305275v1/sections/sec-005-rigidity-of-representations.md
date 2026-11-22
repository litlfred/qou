---
doc_id: arxiv-math-0305275v1
doc_title: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds"
section_id: sec-005-rigidity-of-representations
section_title: "Rigidity of representations"
section_number: null
pages: 21-34
source_pdf: 0305275v1.pdf
source_sha256: 9b356a9d716a0d3e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.993
doc_brief: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds — Let W be a compact manifold and let ρ be a representation of its fundamental group into PSL(2, C)."
---
[]{#s r label="s r"} This section is completely devoted to proving the following:

::: teo
[]{#t ug label="t ug"} Let M be a non-compact, complete, orientable hyperbolic $3$-manifold of finite volume. Let $\Gamma\cong\pi_1(M)$ be the sub-group of ${\rm PSL}(2,\ensuremath{\mathbb C})$ such that $M=\ensuremath{\mathbb H}^3/\Gamma$. Let $\rho:\Gamma\to$ PSL$(2,\ensuremath{\mathbb C})$ be a representation. If $|{\rm vol}(\rho)|={\rm vol}(M)$ then $\rho$ is discrete and faithful. More precisely there exists $\ensuremath{\varphi}\in{\rm PSL}(2,\ensuremath{\mathbb C})$ such that for any $\gamma\in\Gamma$ $$\rho(\gamma)=\ensuremath{\varphi}\circ\gamma\circ\ensuremath{\varphi}^{-1}.$$
:::

::: remark
It is well-known that, in the hypotheses of Theorem [\[t ug\]](#t ug){reference-type="ref" reference="t ug"}, the manifold $M$ is the interior of a compact manifold $\ensuremath{\overline{M}}$ whose boundary consists of tori. Thus $M$ is a cusped manifold and, by Remark [\[r acmcbid\]](#r acmcbid){reference-type="ref" reference="r acmcbid"}, all the definitions and results we gave for ideally triangulated manifold apply.

As product structure on the cusps we fix the horospherical one, having the arc-length as cone parameter. For this section $D_\rho$ will denote a fixed pseudo-developing map for $\rho$.
:::

::: remark
By Proposition [\[p pos\]](#p pos){reference-type="ref" reference="p pos"} we can suppose ${\rm vol}(\rho)\geq0$.
:::

::: remark
[]{#r none label="r none"} A subgroup of PSL$(2,\ensuremath{\mathbb C})$ is said to be *elementary* if it has an invariant set of at most two points in $\partial \ensuremath{\mathbb H}^3$. If the image of $\rho$ is elementary, then one can construct a pseudo-developing map as in Lemma [\[l 1\]](#l 1){reference-type="ref" reference="l 1"} in such a way that all the tetrahedra of any ideal triangulation of $M$ collapse in the straightening. Thus, by Theorem [\[t vsd\]](#t vsd){reference-type="ref" reference="t vsd"}, ${\rm vol}(\rho)=0$.
:::

This remark implies that, in the present case, since ${\rm vol}(\rho)={\rm vol}(M)\neq0$, the image of $\rho$ is non-elementary.

The idea for proving Theorem [\[t ug\]](#t ug){reference-type="ref" reference="t ug"} is to rewrite the Gromov-Thurston-Goldman-Dunfield proof of Mostow's rigidity, valid in the compact case.

We will follow the lead-line of [@D], with the difference that we will use classical chains instead of measure-chains. The technique for constructing classical chains representing smear-cycles is that used in [@BP] for the proof of Mostow's rigidity for compact manifolds. As an effect of non-compactness we will work with infinite chains. Therefore, we have to prove that some usual homological arguments actually work for our chains.

The core of the proof is to deduce from the equality ${\rm vol}(\rho)={\rm vol}(M)$ that $D_\rho$ "does not shrink the volume." This allows us to construct a measurable extension of $D_\rho$ to the whole $\ensuremath{\overline{\ensuremath{\mathbb H}}}^3$, whose restriction to $\partial \ensuremath{\mathbb H}^3$ is almost everywhere a Möbius transformation. Such a Möbius transformation will be the $\ensuremath{\varphi}$ of Theorem [\[t ug\]](#t ug){reference-type="ref" reference="t ug"}.

The key fact is the following proposition, whose proof can be found in [@D] (claim $3$ of Theorem 6.1).

::: prop
[]{#p k label="p k"} Let $f:\partial \ensuremath{\mathbb H}^3\to \partial \ensuremath{\mathbb H}^3$ be a measurable map that maps the vertices of almost all regular ideal tetrahedra to vertices of regular ideal tetrahedra. Then $f$ coincides almost everywhere with the trace of an isometry $\varphi$.
:::

We want to apply Proposition [\[p k\]](#p k){reference-type="ref" reference="p k"} to $D_\rho$, and we do it in two steps. Let $M_0$ be $M$ minus the cusps and let $\pi:\ensuremath{\mathbb H}^3\to M$ be the universal cover.

::: prop
[]{#p nnp1 label="p nnp1"} The map $D_\rho$ extends to $\ensuremath{\overline{\ensuremath{\mathbb H}}}^3$. More precisely, there exists a measurable map $\ensuremath{\overline{D}}_\rho:\partial \ensuremath{\mathbb H}^3\to\partial \ensuremath{\mathbb H}^3$ such that for almost all $x\in\partial \ensuremath{\mathbb H}^3$, for any geodesic $\gamma^x$ ending at $x$, for any sequence $t_n\to\infty$ such that $\pi(\gamma^x(t_n))\in M_0$, we have $$\lim_{n\to\infty}D_\rho(\gamma^x(t_n))=\ensuremath{\overline{D}}_\rho(x).$$
:::

::: prop
[]{#p nnp2 label="p nnp2"} The map $\ensuremath{\overline{D}}_\rho$ satisfies the hypothesis of Proposition [\[p k\]](#p k){reference-type="ref" reference="p k"}.
:::

Before proving Propositions [\[p nnp1\]](#p nnp1){reference-type="ref" reference="p nnp1"}, and [\[p nnp2\]](#p nnp2){reference-type="ref" reference="p nnp2"} we show how they imply Theorem [\[t ug\]](#t ug){reference-type="ref" reference="t ug"}

By Proposition [\[p nnp2\]](#p nnp2){reference-type="ref" reference="p nnp2"}, Proposition [\[p k\]](#p k){reference-type="ref" reference="p k"} applies. By Proposition [\[p nnp1\]](#p nnp1){reference-type="ref" reference="p nnp1"} the equivariance of $D_\rho$ implies the equivariance of $\ensuremath{\overline{D}}_\rho$, getting for any $\gamma\in\Gamma$ $$\rho(\gamma)=\ensuremath{\varphi}\circ\gamma\circ\ensuremath{\varphi}^{-1}.$$\

::: remark
Both Propositions [\[p nnp1\]](#p nnp1){reference-type="ref" reference="p nnp1"}, and [\[p nnp2\]](#p nnp2){reference-type="ref" reference="p nnp2"} will follow from Lemma [\[l cind\]](#l cind){reference-type="ref" reference="l cind"} and [\[l ladf\]](#l ladf){reference-type="ref" reference="l ladf"} below. We notice that Lemma [\[l cind\]](#l cind){reference-type="ref" reference="l cind"} is a restatement of Lemmas $6.2$ of [@D]. While Proposition [\[p nnp2\]](#p nnp2){reference-type="ref" reference="p nnp2"} corresponds to *Claim $2$* of [@D]. Proposition [\[p nnp1\]](#p nnp1){reference-type="ref" reference="p nnp1"} follows from Lemmas [\[l cind\]](#l cind){reference-type="ref" reference="l cind"} and [\[l ladf\]](#l ladf){reference-type="ref" reference="l ladf"} exactly as in [@D]. We will give a complete proof of Proposition [\[p nnp2\]](#p nnp2){reference-type="ref" reference="p nnp2"} because the proof of *Claim $2$* in [@D] seems to be incomplete.
:::

From now until Lemma [\[l nnp3\]](#l nnp3){reference-type="ref" reference="l nnp3"} we will describe how to construct a simplicial version of the *smearing* process of measure-homology (see [@Th1] or [@R]). Then we will prove Lemma [\[l ladf\]](#l ladf){reference-type="ref" reference="l ladf"}. Finally we will complete the proof of Theorem [\[t ug\]](#t ug){reference-type="ref" reference="t ug"} by proving Propositions [\[p nnp1\]](#p nnp1){reference-type="ref" reference="p nnp1"} and [\[p nnp2\]](#p nnp2){reference-type="ref" reference="p nnp2"}.

Let $\mu$ be the Haar measure on Isom$(\ensuremath{\mathbb H}^3)$ such that for each $x\in\ensuremath{\mathbb H}^3$ and $A\subset \ensuremath{\mathbb H}^3$ we have $$\mu\{g\in{\rm Isom}(\ensuremath{\mathbb H}^3)\, :\, g(x)\in A\}={\rm vol}(A)$$ where ${\rm vol}(A)$ is the hyperbolic volume of $A$.

In the following by a tetrahedron of $\ensuremath{\overline{\ensuremath{\mathbb H}}}^3$ we mean an ordered 4-tuple of points (the vertices). The volume of a tetrahedron is the hyperbolic volume with sign of the convex hull of its vertices.

Let $S$ be the set of all genuine (non-ideal, non-degenerate) tetrahedra: $$S=\{(y_0,\dots,y_3)\in(\ensuremath{\mathbb H}^3)^4:\ {\rm vol}(y_0,\dots,y_3)\neq0\}.$$

For any $Y\in S$ let $S(R)$ be the set of all isometric copies of $Y$: $$S(Y)=\{X\in S:\ \exists g\in{\rm Isom}(\ensuremath{\mathbb H}^3),\  X=g(Y)\}.$$

Then a natural bijection $f_Y:\ $Isom$(\ensuremath{\mathbb H}^3)\to S(Y)$ is well-defined by $$f_Y(g)=g(Y).$$ Thus $\mu$ induces a measure, which we still call $\mu$, on $S(Y)$ defined by $$\mu(A)=\mu(f_Y^{-1}(A)).$$

We consider the sets $S_\pm(Y)=f_Y^{-1}($Isom$^\pm(\ensuremath{\mathbb H}^3))$ of tetrahedra respectively positively and negatively isometric to $Y$. Note that $S_+(Y)$ and $S(Y)_-$ are both measurable.

Set $\ensuremath{\mathfrak S}=\Gamma^4/\Gamma$ where $\Gamma$ acts on $\Gamma^4$ by left multiplication. Each element $\sigma=[(\gamma_0,\dots,\gamma_3)]\in \ensuremath{\mathfrak S}$ has a unique representative with $\gamma_0={\rm Id}$. When we write $\sigma\in\ensuremath{\mathfrak S}$ we tacitly assume that the representative of the form $(\gamma_0,\dots,\gamma_3)$ with $\gamma_0={\rm Id}$ has been chosen. So $\gamma_0$ is always the identity.

For the rest of the section we fix a fundamental polyhedron $F\subset\ensuremath{\mathbb H}^3$ for $M$. For all $\ensuremath{\varepsilon}>0$ let $\ensuremath{\cal F}^\ensuremath{\varepsilon}$ be a locally finite $\varepsilon$-net in $F$. For any $\xi\in\ensuremath{\cal F}^\ensuremath{\varepsilon}$ let $$F_\xi=\{x\in F:\ d(x,\xi)=d(x,{\ensuremath{\cal F}}^\ensuremath{\varepsilon})\}.$$

Each $F_\xi$ is a geodesic polyhedron of diameter less than $\varepsilon$. From the cone-property of $D_\rho$ it follows that the diameters of $D_\rho(F_\xi)$ are bounded by a constant $\delta$ that depends on $\varepsilon$. Moreover, by removing some boundary face from some $F_\xi$, we get that $F$ is the disjoint union of the $F_\xi$'s. We define now a family of special simplices. Let $$\ensuremath{\mathfrak N}=\{(\gamma_0,\dots,\gamma_3,\xi_0,\dots,\xi_3):\
(\gamma_0,\dots,\gamma_3)\in{\ensuremath{\mathfrak S}},\  
\xi_i\in{\ensuremath{\cal F}}^\ensuremath{\varepsilon}\textrm{ for all } i\}.$$

For each $\eta\in\ensuremath{\mathfrak N}$ define $\Delta_\eta$ as the straight geodesic singular $3$-simplex whose vertices are the points $\xi_0,\gamma_1(\xi_1),\gamma_2(\xi_2),\gamma_3(\xi_3)$, more precisely $$\Delta_\eta:\Delta^3\ni t \mapsto 
\pi\Big(\sum_{i=0}^3t_i\gamma_i(\xi_i)\Big).$$

For each tetrahedron $X=(x_0,\dots,x_3)\in S(Y)$ there exists a unique $\eta=(\gamma_0,\dots,\gamma_3,\xi_0,\dots,\xi_3)\in\ensuremath{\mathfrak N}$ such that $x_i\in \gamma_i(F_{\xi_i})$ for $i=0,\dots,3$. This defines a function $$s_Y:S(Y)\to\ensuremath{\mathfrak N}.$$ Roughly speaking, $\mathfrak N$ is a locally finite $\varepsilon$-net in the space of $3$-simplices of $M$ and $s_Y$ is the "closest point"-projection.

For any $\eta\in\ensuremath{\mathfrak N}$ define $$a_Y^\pm(\eta)=\mu\{s_Y^{-1}(\eta)\cap S_\pm(Y)\}=
\mu\{X\in S_\pm(Y) :\ x_i\in\gamma_i(F_{\xi_i})\}$$ and $$a_Y(\eta)=a^+_Y(\eta)-a^-_Y(\eta).$$

In the language of measures, one can think of $a_Y^\pm$ as the push-forward of the measure $\mu$ under the map $s_Y:S_\pm(Y)\to\ensuremath{\mathfrak N}$. This is the key for the passage from measure-chains to classical ones.

The smearing of the tetrahedron $Y$ is the cycle: $$Z_Y=\sum_{\eta\in\ensuremath{\mathfrak N}}a_Y(\eta)\Delta_\eta.$$ We notice that, as $\ensuremath{\mathfrak N}$ depends on the family $\ensuremath{\cal F}^\ensuremath{\varepsilon}$, the cycle $Z_Y$ actually depends on $\varepsilon$.

::: remark
The smearing of a tetrahedron in general is not a finite sum. Nevertheless, as the following lemma shows, it has bounded $l^1$-norm.
:::

::: lemma
[]{#l L1 label="l L1"} For any $Y\in S$, we have $\displaystyle{\sum_\eta|a_Y(\eta)|<{\rm vol}(M)}.$
:::

 If $Y=(y_0,\dots y_3)$ then $$\begin{array}{l}
\displaystyle{\sum_\eta|a_Y(\eta)|\leq\sum_\eta
  \big(a^+_Y(\eta)+a_Y^-(\eta)\big)}=\displaystyle{
  \sum_\eta\mu\{s_Y^{-1}(\eta)\}=\mu\Big\{\,\bigcup_\eta
  s_Y^{-1}(\eta)\Big\}}\\
=\displaystyle{\mu\{\,s_Y^{-1}(\ensuremath{\mathfrak N})\,\}}=
\mu\{\,f_Y^{-1}s_Y^{-1}(\ensuremath{\mathfrak N})\,\}=
 \mu\{g:\ g(y_0)\in F\}={\rm vol}(F)={\rm vol}(M).
\end{array}$$\

::: lemma
[]{#l nnp3 label="l nnp3"} The infinite chain $Z_Y$ is a cycle, *i.e.* $\partial Z_Y=0$.
:::

  First note that the $l^1$-norm of $\partial Z_Y$ is bounded by $4$ times the $l^1$-norm of $Z_Y$. Thus all the sums we will consider make sense.

Let $\upsilon$ be a simplex of $\partial Z_Y$. By construction $\upsilon$ is obtained as the projection of an $(n-1)$-simplex having vertices in $F_{\xi_0},\gamma_1(F_{\xi_1}),\gamma_2(F_{\xi_2})$ for some $\gamma_1,\gamma_2\in\Gamma$ and $\xi_0,\xi_1,\xi_2\in\ensuremath{\cal F}^\ensuremath{\varepsilon}$. Let $A_\upsilon$ be the set of the elements of $\mathfrak N$ of the form $\eta=(\gamma_0,\gamma_1,\gamma_2,\gamma,\xi_0,\xi_1,\xi_2,\xi)$ with $\gamma\in\Gamma$ and $\xi\in\ensuremath{\cal F}^\ensuremath{\varepsilon}$. The simplices $\Delta_\eta$ of $Z_Y$ having $\upsilon$ as the last face contribute to the coefficient of $\upsilon$ in $\partial Z_Y$ by $$\begin{array}{ll}
\displaystyle{\sum_{\eta\in A_\upsilon} a_Y(\eta)=\sum_{\eta\in
  A_\upsilon}\mu(s_Y^{-1}(\eta)\cap S_+(Y)) -\sum_{\eta\in A_\upsilon}
  \mu(s_Y^{-1}(\eta)\cap S_-(Y))}\\=
\mu(s_Y^{-1}(A_\upsilon)\cap S_+(Y))-\mu(s_Y^{-1}(A_\upsilon)\cap
S_-(Y))=0.\end{array}$$

The same calculation, made with the simplices having $\upsilon$ as the $i$th face, shows that the coefficient of $\upsilon$ in $\partial Z_Y$ is zero.\

For any ideal, non-flat, tetrahedron $Y=(y_0,\dots,y_3)$ let $t\mapsto y_i(t)$ be the geodesic ray from the center of mass of $Y$ to $y_i$, $i=0,\dots,3$. For any $R>0$ let $Y_R$ be the following element of $S$: $$Y_R=(y_0(R),\dots,y_3(R)).$$

::: remark
From now on we fix a positively oriented regular ideal tetrahedron $Y$, and we write $S_\pm(R)$, $f_R$, $s_R$, $a_R(\eta)$ and $Z_R$ for $S_\pm(Y_R)$, $f_{Y_R}$, $s_{Y_R}$, $a_{Y_R}(\eta)$ and $Z_{Y_R}$.
:::

We say that a $3$-simplex $\Delta$ is $\varepsilon$-close to a tetrahedron $X$ if the vertices of $\Delta$ are $\varepsilon$-close to $X$. We define $$\epsilon(R,\ensuremath{\varepsilon})=\sup\{v_3-{\rm vol}(\Delta):\ 
\Delta\textrm{ is \ensuremath{\varepsilon}-close to an element of } S(R)\}$$

::: lemma
[]{#l and label="l and"} For any fixed $\varepsilon$, for large $R$ the function $\epsilon(R,\ensuremath{\varepsilon})$ goes to zero exponentially in $R$.
:::

This is because $v_3-{\rm vol}(Y_R)$ goes to zero like $e^{-R}$ and the volume of any $\Delta$ which is $\varepsilon$-close to $Y_R$ is close to the volume of $Y_R$. See [@BP], [@D], [@Th1] for details.

::: remark
What we actually need to prove our claims is a restatement for $Z_R$ of the *Step [\[stp3\]](#stp3){reference-type="ref" reference="stp3"}* of Theorem [\[t sv\]](#t sv){reference-type="ref" reference="t sv"}. From now until Proposition [\[p 27\]](#p 27){reference-type="ref" reference="p 27"}, we prove facts that are standard for finite chains, but need a proof for $Z_R$.
:::

For $\eta\in\ensuremath{\mathfrak N}$, we set $v_\eta={\rm vol}(\Delta_\eta)$. Using the fact that all the $F_\xi$'s have diameter less than $\varepsilon$, one can prove the following lemma (see [@BP] for details). Recall that $\ensuremath{\mathfrak N}$ depends on $\ensuremath{\cal F}^\ensuremath{\varepsilon}$ and so it depends on $\varepsilon$.

::: lemma
[]{#l novo label="l novo"} For any $\ensuremath{\varepsilon}>0$, for large enough $R$ we have that for any $\eta\in \ensuremath{\mathfrak N}$

-   $a_R^+(\eta)\cdot a_R^-(\eta)=0$.

-   $a_R(\eta)\neq 0\implies a_R(\eta)\cdot v_\eta\geq 0$.
:::

::: lemma
[]{#l lemmaX label="l lemmaX"} There exists a constant $c$ such that $|D_\rho^*\omega|<c|\omega|$, where $\omega$ is the volume-form of $\ensuremath{\mathbb H}^3$.
:::

  Let $M_0$ be $M$ minus the cusps. The function $|D_\rho^*\omega|/|\omega|$ is continuous and hence bounded on $M_0$. In the cusps, by direct calculation and using the cone property of $D_\rho$, one can show that the same bound holds.\

::: lemma
The integrals $\langle\omega,Z_R\rangle$ and $\langle
D_\rho^*\omega,Z_R\rangle$ are well-defined.
:::

  As $\sum|a_R(\eta)|<+\infty$, since $|\langle\omega,\Delta_\eta\rangle|$ is bounded by $v_3$, then $\langle
\omega,Z_R\rangle$ is well-defined. Consider now $D_\rho^*\omega$. From Lemma [\[l lemmaX\]](#l lemmaX){reference-type="ref" reference="l lemmaX"} it follows that the integral of $|D_\rho^*|$ over straight geodesic simplices is bounded by $cv_3$. Hence also $\langle D_\rho^*\omega,Z_R\rangle$ is well-defined.\

As above, let $M_0$ denote $M$ minus the cusps and, for $k\in \ensuremath{\mathbb N}^*$ let $$M_k=\displaystyle{\bigcup_{T\subset\partial M_0}T\times[k-1,k).}$$

Let ${\ensuremath{\cal F}}_k^\ensuremath{\varepsilon}={\ensuremath{\cal F}^\ensuremath{\varepsilon}}\cap \pi^{-1}(M_k)$ and $\ensuremath{\mathfrak N}_k=\{\eta\in\ensuremath{\mathfrak N}:\ \xi_0\in{\cal F}_k^\ensuremath{\varepsilon}\}$. We have $$Z_R=\sum_{k\in\ensuremath{\mathbb N}}\sum_{\eta\in\ensuremath{\mathfrak N}_k}a_R(\eta)\Delta_\eta.$$

::: lemma
[]{#l lemmaY label="l lemmaY"} For any $k$ the chain $\sum_{\eta\in\ensuremath{\mathfrak N}_k} a_R(\eta)\Delta_\eta$ is a finite sum.
:::

  If $a_R(\eta)\neq0$ and $\eta\in\ensuremath{\mathfrak N}_k$ then $\Delta_\eta$ is $\varepsilon$-close to an element $X\in
S(R)$ having first vertex in $F_{\xi_0}$ with $\xi_0\in{\cal F}^\ensuremath{\varepsilon}_k$ . Since $\ensuremath{\cal F}^\ensuremath{\varepsilon}$ is locally finite and $\ensuremath{\overline{M}}_k$ is compact, ${\cal F}_k^\ensuremath{\varepsilon}$ is finite, so there is only a finite number of possibilities for $\xi_0$. Since $\ensuremath{\overline{F}}_{\xi_0}$ is compact, any $X\in S(R)$ with first vertex in $F_{\xi_0}$ lies on a compact ball $B$ of $\ensuremath{\mathbb H}^3$. Since $F$ is a fundamental domain, then there exists only a finite number of elements $\gamma\in\Gamma$ so that $\gamma(F)$ intersects $B$. Then for any $\xi_0$ there is only a finite number of possibilities for $\xi_1,\ \xi_2$ and $\xi_3$. It follows that there exists only a finite number of $\eta\in\ensuremath{\mathfrak N}_k$ such that $a_R(\eta)\neq0$.\

::: lemma
[]{#l lemmaZ label="l lemmaZ"} For any $R$, if $k$ is large enough, then for any $\eta\in \ensuremath{\mathfrak N}_k$ with $a_R(\eta)\neq 0$, the simplex $\Delta_\eta$ is completely contained in a cusp of $M$.
:::

  If $X=(x_0,\dots,x_3)\in S(R)$ then $X$ lies in the ball $B(x_0,2R)$. Since $M$ has a finite number of cusps, for any $R$ there exists $m\in \ensuremath{\mathbb N}$ such that for $k\geq m$ if $x_0\in M_k$ then the whole ball $B(x_0,2R+\ensuremath{\varepsilon})$ is contained in the cusp containing $x_0$. If $\eta\in\ensuremath{\mathfrak N}_k$ and $a_R(\eta)\neq0$, then there exists $X\in S(R)$ with $x_0\in \pi^{-1}(M_k)\cap F$ hence $\Delta_\eta$ is $\varepsilon$-close to $X$. Thus $\Delta_\eta\subset
B(x_0,2R+\ensuremath{\varepsilon})$ is contained in the cusp that contains $x_0$.\

Now for $k\in\ensuremath{\mathbb N}$ define $$Z_{R,k}=\sum_{j<k}\sum_{\eta\in \ensuremath{\mathfrak N}_j}a_R(\eta)\Delta_\eta.$$

$Z_{R,k}$ is a finite chain by Lemma [\[l lemmaY\]](#l lemmaY){reference-type="ref" reference="l lemmaY"}. Moreover, since $\partial Z_R=0$, then each simplex $\upsilon$ of $\partial Z_{R,k}$ appears as a face of a simplex $\Delta_\eta$ with $a_R(\eta)\neq 0$ and $\eta\in{\ensuremath{\mathfrak N}}_j$ for some $j\geq k$. Therefore, by Lemma [\[l lemmaZ\]](#l lemmaZ){reference-type="ref" reference="l lemmaZ"}, for $k$ large enough each simplex $\upsilon$ of $\partial Z_{R,k}$ is contained in a cusp of $M$. Thus to each $\upsilon$ there corresponds an ideal point of $\ensuremath{\widehat{M}}$. For each $\upsilon\in\partial
  Z_{R,k}$ let $\lambda_{R,k}(\upsilon)$ be the coefficient of $\upsilon$ in $\partial Z_{R,k}$ and let $C_\upsilon$ be the cone from $\upsilon$ to the corresponding ideal point.

Let $\ensuremath{\widehat{Z}}_{R,k}$ be the chain obtained by adding to $Z_{R,k}$ the cones $C_\upsilon$: $$\ensuremath{\widehat{Z}}_{R,k}=Z_{R,k}+\sum_{\upsilon\in\partial Z_{R,k}}\lambda_{R,k}(\upsilon)C_\upsilon.$$ The chain $\ensuremath{\widehat{Z}}_{R,k}$ is a finite sum and it is easily checked that it is a cycle.

For any $3$-simplex $\Delta$ let ${\rm Strvol}(\Delta)$ denote the volume of the convex hull of the vertices of $D_\rho(\Delta)$. For any $\eta\in\ensuremath{\mathfrak N}$ set $w_\eta={\rm Strvol}(\Delta_\eta)$.

::: prop
[]{#p 27 label="p 27"} For any $R>0$ We have: $$\sum_\eta a_R(\eta) v_\eta=
\langle \omega,Z_R\rangle=\langle
D_\rho^*\omega,Z_R\rangle=\sum_\eta a_R(\eta)w_\eta.$$
:::

 The first equality is tautological. We use now the cycles $\ensuremath{\widehat{Z}}_{R,k}$ to approximate $Z_R$. Since ${\rm vol}(\rho)= {\rm vol}(M)$, then $[\omega]=[D_\rho^*\omega]$ as elements of $H^3(\ensuremath{\widehat{M}})$. Thus for any $k\in\ensuremath{\mathbb N}$ we have $\langle \omega,\ensuremath{\widehat{Z}}_{R,k}\rangle=\langle
D^*_\rho\omega,\ensuremath{\widehat{Z}}_{R,k}\rangle.$ As in *Step [\[stp3\]](#stp3){reference-type="ref" reference="stp3"}* of Theorem [\[t sv\]](#t sv){reference-type="ref" reference="t sv"}, we can straighten the finite cycle $\ensuremath{\widehat{Z}}_{R,k}$, getting: $$\langle \omega,\ensuremath{\widehat{Z}}_{R,k}\rangle=\langle
D^*_\rho\omega,\ensuremath{\widehat{Z}}_{R,k}\rangle=
\sum_{j<k}\sum_{\eta\in\ensuremath{\mathfrak N}_k}a_R(\eta)w_\eta
+\sum_{\upsilon \in\partial Z_{R,k}}\lambda_{R,k}(\upsilon){\rm Strvol}(C_\upsilon).$$

For each simplex $\alpha$ of $\ensuremath{\widehat{Z}}_{R,k}$ we have $|{\rm vol}(\alpha)|\leq v_3$, $|{\rm Strvol}(\alpha)|\leq v_3$ and, by Lemma [\[l lemmaX\]](#l lemmaX){reference-type="ref" reference="l lemmaX"}, $|\langle D^*_\rho \omega,
\alpha\rangle|\leq cv_3$. It follows that to get the remaining inequalities it suffices to show that $$\lim_{k\to \infty}\sum_{\upsilon\in\partial 
Z_{R,k}}|\lambda_{R,k}(\upsilon)|=0.$$

Since $\partial Z_R=0$, if $\upsilon\in\partial Z_{R,k}$ then $\upsilon\in\partial \Delta_\eta$ with $a_R(\eta)\neq 0$ and $\eta\in\ensuremath{\mathfrak N}_j$ for some $j\geq k$. So we have $$\begin{array}{cl}
~&\displaystyle{\sum_{\upsilon\in\partial Z_{R,k}}|\lambda_{R,k}(\upsilon)|\leq
4\sum_{j\geq k}\sum_{\eta\in\ensuremath{\mathfrak N}_j}a^+_R(\eta)+a^-_R(\eta)=
4\sum_{j\geq k}\sum_{\eta\in\ensuremath{\mathfrak N}_j}\mu\{s_R^{-1}(\eta)\}}\\
=& \displaystyle{4\sum_{j\geq k} \mu\{s_R^{-1}(\ensuremath{\mathfrak N}_j)\}=4\sum_{j\geq k}\mu\{Y\in S(R):\exists\xi\in{\ensuremath{\cal F}}_j^\ensuremath{\varepsilon},\
y_0\in F_\xi\}}\\
=& \displaystyle{4\sum_{j\geq k}\sum_{\xi\in{\ensuremath{\cal F}}^\ensuremath{\varepsilon}_j}{\rm vol}(F_\xi)
\leq4{\rm vol}(\bigcup_{j\geq k-\ensuremath{\varepsilon}}M_j)}
\end{array}$$ The last term goes to zero as $k\to\infty$ because $M$ has finite volume and the desired equality follows.\

Now that we have Proposition [\[p 27\]](#p 27){reference-type="ref" reference="p 27"}, forget about the cycles $\ensuremath{\widehat{Z}}_{R,k}$.

From triangular inequality, Proposition [\[p 27\]](#p 27){reference-type="ref" reference="p 27"} and Lemma [\[l novo\]](#l novo){reference-type="ref" reference="l novo"} we have $$\begin{array}{cl}
&\displaystyle{\sum_\eta|a_R(\eta)|\cdot|w_\eta|\geq 
\Big|\sum_\eta a_R(\eta)w_\eta\Big|=\Big|\sum_\eta a_R(\eta)v_\eta\Big|}\\
=&\displaystyle{
\sum_\eta|a_R(\eta)|\cdot|v_\eta|\geq \sum_\eta
|a_R(\eta)|(v_3-\epsilon(R,\ensuremath{\varepsilon}))}
\end{array}$$ from which and Lemma [\[l L1\]](#l L1){reference-type="ref" reference="l L1"} we get:

::: prop
[]{#p p14 label="p p14"} For $R$ large enough we have $$\sum_{\eta\in\ensuremath{\mathfrak N}}|a_R(\eta)|(v_3-|w_\eta|)\leq
\sum_{\eta\in\ensuremath{\mathfrak N}}|a_R(\eta)|\epsilon(R,\ensuremath{\varepsilon})\leq {\rm vol}(M)\epsilon(R,\ensuremath{\varepsilon}).$$
:::

For any $R>0$ let $A_R\subset\ensuremath{\mathfrak N}$ be the set of tetrahedra with "small" straight volume: $$A_R=\{\eta\in\ensuremath{\mathfrak N}:\ v_3-|w_\eta|>R^2\cdot{\rm vol}(M)\cdot\epsilon(R,\ensuremath{\varepsilon})\}.$$

::: lemma
[]{#l cind label="l cind"} For $R$ large enough we have $$\sum_{\eta\in A_R}|a_R(\eta)|\leq\frac{1}{R^2}.$$
:::

  From Proposition [\[p p14\]](#p p14){reference-type="ref" reference="p p14"} we get $$\begin{array}{ll}
&\displaystyle{
R^2{\rm vol}(M)\epsilon(R,\ensuremath{\varepsilon})\cdot\sum_{\eta\in A_R}|a_R(\eta)|
\leq\sum_{\eta\in A_R}|a_R(\eta)|(v_3-|w_\eta|)}\\
\leq&
\displaystyle{\sum_{\eta\in \ensuremath{\mathfrak N}}|a_R(\eta)|(v_3-|w_\eta|)}
\leq {\rm vol}(M)\epsilon(R,\ensuremath{\varepsilon})
\end{array}$$ The claimed inequality follows.\

::: lemma
[]{#l ladf label="l ladf"} For almost all isometries $g$ we have $$\lim_{n\to\infty}{\rm Strvol}(g(Y_n))=v_3.$$
:::

  Since $a_R^+\cdot a_R^-=0$, then $\sum_{\eta\in A_R}|a_R(\eta)|=\mu(s_R^{-1}(A_R))$. Thus for any fixed $R>0$ we have $$\mu\Big(\bigcup_{\ensuremath{\mathbb N}\ni n> R}s_R^{-1}(A_n)\Big)
\leq\sum_{n>R}\frac{1}{n^2}<\frac{1}{R}.$$

Recalling that for any set $A\subset\ensuremath{\mathfrak N}$ we have $\mu(s_R^{-1}(A))=\mu(f_R^{-1}s_R^{-1}(A))$, we get $$\mu\{
g\in\textrm{ Isom}(\ensuremath{\mathbb H}^3): \exists n>R,\
w_{s_n(g(Y_n))}<v_3-n^2\cdot{\rm vol}(M)\cdot\epsilon(n,\ensuremath{\varepsilon})
\}<\frac{1}{R}.$$

From Lemma [\[l and\]](#l and){reference-type="ref" reference="l and"} it follows that $\lim_{n\to\infty}n^2\epsilon(n,\ensuremath{\varepsilon})=0$. As $R\to\infty$, this implies that for any $\ensuremath{\varepsilon}>0$, for almost any isometry $g$ we have $$\lim_{n\to\infty}w_{s_n(g(Y_n))}=v_3.$$

Let $g$ be one of such maps. Since the diameters of the $D_\rho(F_\xi)$ are bounded by $\delta$, then $D_\rho(\Delta_{s_R(g(Y_R))})$ is $\delta$-close to $D_\rho(g(Y_R))$. Recalling that $w_{s_R(g(Y_R))}={\rm Strvol}(\Delta_{s_R(g(Y_R))})$, we have that $$\lim_{n\to\infty}{\rm Strvol}(\Delta_{s_n(g(Y_n))})=v_3$$ and, since $D_\rho(g(Y_R))$ is $\delta$-close to $D_\rho(\Delta_{s_R(g(Y_R))})$, then also $$\lim_{n\to\infty}{\rm Strvol}(g(Y_n))=v_3.$$\

We sketch here the proof of Proposition [\[p nnp1\]](#p nnp1){reference-type="ref" reference="p nnp1"}, referring to [@D] for details.

In the disc model let $\gamma$ be a geodesic from $0$ to a point in $\partial \ensuremath{\mathbb H}^3$. Let $X_R$ be a family of regular tetrahedra of edge $R$ with first vertex in $0$ and second in $\gamma(R)$. All the claims from Lemma [\[l L1\]](#l L1){reference-type="ref" reference="l L1"} to Lemma [\[l ladf\]](#l ladf){reference-type="ref" reference="l ladf"} hold for $\{X_R\}$. It follows that for almost all isometries $g$ we have $$\lim_{n\to\infty}{\rm Strvol}(g(X_n))=v_3.$$ Then $D_\rho(g(\gamma(n)))$ must reach the boundary of $\ensuremath{\mathbb H}^3$. Using again the above property of the limit, one can estimate the angle $\alpha(n)$ between the geodesic from $D_\rho(g(0))$ to $D_\rho(g(\gamma(n)))$ and the geodesic from $D_\rho(g(0))$ and $D_\rho(g(\gamma(n+1)))$. Such estimate shows that $\sum
\alpha(n)<\infty$, which implies that $D_\rho(g(\gamma(n)))$ converges. The claim follows because $D_\rho$ is locally Lipschitz outside the cusps. Measurability follows because the extension can be viewed as a point-wise limit of measurable functions.\

::: remark
In general $D_\rho$ is not uniformly continuous in the cusps. So it cannot be locally Lipschitz on the whole $\ensuremath{\mathbb H}^3$.
:::

We come now to the proof of Proposition [\[p nnp2\]](#p nnp2){reference-type="ref" reference="p nnp2"}.

::: lemma
[]{#l nnpp label="l nnpp"} Let $X=(x_0,x_1,x_2,x_3)$ be an ideal tetrahedron in $\ensuremath{\overline{\ensuremath{\mathbb H}}}^3$. Suppose that no three vertices of $X$ coincide. Then for any $\ensuremath{\varepsilon}>0$ there exist neighborhoods $U_i$ of $x_i$ in $\ensuremath{\overline{\ensuremath{\mathbb H}}}^3$ such that for any tetrahedron $Y=(y_0,\dots,y_3)$ with $y_i\in U_i$ we have $|{\rm vol}(Y)-{\rm vol}(X)|<\ensuremath{\varepsilon}$.
:::

This follows from the formula of the volume for ideal tetrahedra, see [@BP] for details.

::: remark
Lemma [\[l nnpp\]](#l nnpp){reference-type="ref" reference="l nnpp"} does not hold if three vertices of $X$ coincide. To see this, let $Y$ be a regular ideal tetrahedron and let $\gamma$ be a parabolic or hyperbolic isometry. Then $\gamma^n(Y)$ is a family of tetrahedra with maximal volume, but at least three of the vertices of $\gamma^n(Y)$ converge to the same point.
:::

::: lemma
[]{#l era1 label="l era1"} For almost all regular ideal tetrahedra $Y$, the ideal tetrahedron $\ensuremath{\overline{D}}_\rho(Y)$ is defined. Moreover, for almost all $Y$ either $\ensuremath{\overline{D}}_\rho(Y)$ is regular (whence ${\rm vol}(\ensuremath{\overline{D}}_\rho(Y))=v_3$) or at least three of its vertices coincide (whence ${\rm vol}(\ensuremath{\overline{D}}_\rho(Y))=0$).
:::

  Without loss of generality, we can restrict the first claim to the space of positive regular ideal tetrahedra. We parametrize such a space with $$\{(a,b,c)\in S_\infty^2\times S_\infty^2\times S_\infty^2:\ a\neq b\neq
  c\}$$ where $S_\infty^2=\partial \ensuremath{\mathbb H}^3$, by mapping $(a,b,c)$ to the unique positive regular ideal tetrahedron with $(a,b,c)$ as the first three vertices. We denote by $Q(a,b,c)$ the fourth vertex of such tetrahedron. Since $\ensuremath{\overline{D}}_\rho$ is defined almost everywhere, the first claim follows from Fubini's theorem. The second claim follows from Lemmas [\[l ladf\]](#l ladf){reference-type="ref" reference="l ladf"} and [\[l nnpp\]](#l nnpp){reference-type="ref" reference="l nnpp"}.\

With the above notation, by Lemma [\[l era1\]](#l era1){reference-type="ref" reference="l era1"} we can restate Proposition [\[p nnp2\]](#p nnp2){reference-type="ref" reference="p nnp2"} as follows.

::: prop
[]{#p base label="p base"} The set $\{Y\in S_\infty^2\times S_\infty^2\times S_\infty^2:\ {\rm vol}(\ensuremath{\overline{D}}_\rho(Y))=0\}$ has zero measure.
:::

The proof of this result will follow from the next:

::: lemma
[]{#l basedue label="l basedue"} If the set $$\{Y\in S_\infty^2\times S_\infty^2\times S_\infty^2:\ {\rm vol}(\ensuremath{\overline{D}}_\rho(Y))=0\}$$ has positive measure, then the map $\ensuremath{\overline{D}}_\rho$ is constant almost everywhere.
:::

Before proving Lemma [\[l basedue\]](#l basedue){reference-type="ref" reference="l basedue"} we show how it implies Proposition [\[p base\]](#p base){reference-type="ref" reference="p base"}.

 

By contradiction, we apply Lemma [\[l basedue\]](#l basedue){reference-type="ref" reference="l basedue"} deducing that $\ensuremath{\overline{D}}_\rho$ is a.e. a constant $p$. From the equivariance of $\ensuremath{\overline{D}}_\rho$ it follows that for any $\gamma \in\Gamma$ and $x\in\partial \ensuremath{\mathbb H}^3$ we have $$p=\ensuremath{\overline{D}}_\rho \gamma(x)=\rho(\gamma)(\ensuremath{\overline{D}}_\rho(x))=\rho(\gamma)(p).$$ Thus $p$ is a fixed point of any element of $\Gamma$. This implies that the image of $\rho$ is elementary, but this cannot happen because of Remark [\[r none\]](#r none){reference-type="ref" reference="r none"}.\

We now prove Lemma [\[l basedue\]](#l basedue){reference-type="ref" reference="l basedue"}.

::: lemma
In the hypothesis of Lemma [\[l basedue\]](#l basedue){reference-type="ref" reference="l basedue"} there exists a positive-measure set $A\subset S_\infty^2$ such that $\ensuremath{\overline{D}}_\rho$ is constant on A.
:::

 By Lemma [\[l era1\]](#l era1){reference-type="ref" reference="l era1"} it is not restrictive to suppose that the set $$\{(a,b,c)\in S_\infty^2\times S_\infty^2\times S_\infty^2:\ 
\ensuremath{\overline{D}}_\rho(a)=\ensuremath{\overline{D}}_\rho(b)=\ensuremath{\overline{D}}_\rho(c)\}$$ has positive measure. Then by Fubini's theorem there exists a positive-measure set $A_0\subset S_\infty^2$ such that for all $a_0\in A_0$ the set $$\{(b,c)\in S_\infty^2\times S_\infty^2:\ 
\ensuremath{\overline{D}}_\rho(a_0)=\ensuremath{\overline{D}}_\rho(b)=\ensuremath{\overline{D}}_\rho(c)\}$$ has positive measure in $S_\infty^2\times S_\infty^2$. Again by Fubini's theorem for all $a_0\in A_0$ there exists a positive-measure set $A_1\in S_\infty^2$ such that for any $a_1\in A_1$ the set $$\{c\in S_\infty^2:\ensuremath{\overline{D}}_\rho(a_0)=\ensuremath{\overline{D}}_\rho(a_1)=\ensuremath{\overline{D}}_\rho(c)\}$$ has positive measure. In particular $\ensuremath{\overline{D}}_\rho$ is constant on $A_1$.\

We set $p=\ensuremath{\overline{D}}_\rho(A_1)$ and $A=\ensuremath{\overline{D}}_\rho^{-1}(p)$.

::: remark
In the sequel we use the symbol $\ensuremath{\widetilde{\forall}}$ to mean *"for almost all."*
:::

By Lemma [\[l era1\]](#l era1){reference-type="ref" reference="l era1"} the set $A$ has the following property $$\ensuremath{\widetilde{\forall }}(a_0,a_1,x)\in A\times A\times A^c,\ \ Q(a_0,a_2,x)\in A.$$

We work now in the half space model $\ensuremath{\mathbb C}\times \ensuremath{\mathbb R}^+$ of $\ensuremath{\mathbb H}^3$. So $S_\infty^2=\ensuremath{\mathbb C}\cup\{\infty\}$. In that model $$Q(\infty,a,z)=\alpha(z-a)+a$$ where $\alpha=(1+i\sqrt 3)/2$. Again by Fubini's theorem $\ensuremath{\widetilde{\forall }}a_0\in
A,\ \ensuremath{\widetilde{\forall }}(a_1,x)\in A\times A^c$, we have $Q(a_0,a_1,x)\in A$ and we can suppose that this holds for $a_0=\infty$.

In other words, for almost all $(a,x)\in A\times A^c$ the third vertex of the equilateral triangle with the first two vertices in $a$ and $x$ is in $A$. For any $a,x\in\ensuremath{\mathbb C}$ we call $E_x(a)$ the set of the vertices of the regular hexagon centered at $x$ and with a vertex in $a$. Then we have $$\label{1}
\ensuremath{\widetilde{\forall }}(a,x)\in A\times A^c, \ E_x(a)\subset A$$ and in particular $\ensuremath{\widetilde{\forall }}(a,x)\in A\times A^c, \ 2x-a\in A.$ Note that $x$ is the middle-point of the segment between $a$ and $2x-a$.

::: lemma
[]{#l v2 label="l v2"} For any open set $B\subset\ensuremath{\mathbb C}$ we have $\mu(A\cap B)>0$.
:::

  Suppose the contrary. Then there exists an open set $B$ such that $\mu(A\cap B)=0$. That is, almost all the points of $B$ are in $A^c$. Moreover, from ([\[1\]](#1){reference-type="ref" reference="1"}) and Fubini's theorem it follows that $\ensuremath{\widetilde{\forall }}x\in
A^c, \ensuremath{\widetilde{\forall }}a\in A, E_x(a)\in A$. Therefore there exists a point $x_0\in B$ such that a small ball $B_0=B(x_0,r_0)$ is contained in $B$ and $$\label{2}
\ensuremath{\widetilde{\forall }}a\in A,\ E_{x_0}(a)\in A.$$

Since $\mu(A)>0$ then there exists a small ball $B_1=B(x_1,r_1)$ such that $\mu(A\cap B_1)>0$. Let $x_2=(x_1+x_0)/2$. If there exists $r>0$ such that $\mu(A\cap
B(x_2,r))=0$, then applying the same argument we can find a point $y$ arbitrarily close to $x_2$ such that ([\[2\]](#2){reference-type="ref" reference="2"}) holds for $y$. In particular we get that almost all the points of the set $C=\{2y-a:\ a\in B_1\cap A\}$ are in $A$. But if $y$ is close enough to $x_2$ then $C\cap B_0$ has positive measure, contradicting that $\mu(A\cap B)=0$.

It follows that for all $r_2>0$ we have $\mu(A\cap
B(x_2,r_2))>0$, in particular we choose $r_2<r_0/2$. By iterating this construction, we find a sequence of points $x_n\to x_0$ and radii $r_0/2>r_n>0$ such that $\mu(A\cap B(x_n,r_n))>0$. For $n$ large enough this contradicts the fact that $\mu(A\cap B)=0$.\

::: lemma
[]{#l v3 label="l v3"} For all $z\in \ensuremath{\mathbb C}$ we have $$\label{3}
\forall r>0\ \ \mu(B(z,r)\cap A)\geq\frac{1}{2}\mu(B(z,r)).$$
:::

  From Fubini's theorem, and condition ([\[1\]](#1){reference-type="ref" reference="1"}), it follows that for almost all $a\in A$ we have $$\label{4}
\ensuremath{\widetilde{\forall }}x\in A^c, \ E_x(a)\subset A.$$ Note that if $(\ref{4})$ holds for $a$, then $(\ref{3})$ holds for $a$.

Let $z\in \ensuremath{\mathbb C}$. From Lemma [\[l v2\]](#l v2){reference-type="ref" reference="l v2"} it follows that there exists a sequence $x_n\to z$ such that $(\ref{4})$ (and hence $(\ref{3})$) holds for $x_n$. As the function $x\mapsto
\mu(A\cap B(x,r))$ is continuous, then the claim holds for $z$.\

::: lemma
Let $X\subset \ensuremath{\mathbb R}^2$ be a measurable set. If there exists $\alpha>0$ such that for any ball $B$ $$\mu(B\cap X)\geq\alpha\mu(B)$$ then $\mu(\ensuremath{\mathbb R}^2\setminus X)=0$.
:::

This is a standard fact of integration theory and it follows from Lebesgue's differentiation theorem (see for example [@Ru]).

From this lemma and Lemma [\[l v3\]](#l v3){reference-type="ref" reference="l v3"} it follows that the set $A$ has full measure. Since $A=\ensuremath{\overline{D}}_\rho^{-1}(p)$ then $\ensuremath{\overline{D}}_\rho$ is constant almost everywhere and Lemma [\[l basedue\]](#l basedue){reference-type="ref" reference="l basedue"} is proved.\

This completes the proof of Theorem [\[t ug\]](#t ug){reference-type="ref" reference="t ug"}.
