---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-008-8-delignelusztig-theory
section_title: "Deligne–Lusztig Theory"
section_number: 8
pages: 52-61
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.972
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the Weyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
[]{#sec:dl label="sec:dl"}

## 

The goal of this section is to prove Theorems [\[thm:virtual\]](#thm:virtual){reference-type="ref" reference="thm:virtual"}, [\[thm:induction\]](#thm:induction){reference-type="ref" reference="thm:induction"}, and [\[thm:pole\]](#thm:pole){reference-type="ref" reference="thm:pole"}. Throughout, we assume that $W$ is a Weyl group and use the notation and hypotheses of Sections [\[sec:mixed\]](#sec:mixed){reference-type="ref" reference="sec:mixed"}-[\[sec:hecke\]](#sec:hecke){reference-type="ref" reference="sec:hecke"}. In particular, we continue to assume that $\bb{F}$ is of large characteristic. We will write $\ur{H}_!^\ast(-) = \ur{H}_!^\ast(-, \bar{\mathbf{Q}}_\ell)$ to denote cohomology with compact support.

## 

The proofs of Theorems [\[thm:virtual\]](#thm:virtual){reference-type="ref" reference="thm:virtual"} and [\[thm:induction\]](#thm:induction){reference-type="ref" reference="thm:induction"} rely on properties of the virtual characters of $G^F$ introduced by Deligne--Lusztig [@dl], which we now review.

For all $w \in W$, the **Deligne--Lusztig variety** $X_w \subseteq \cal{B} \times \cal{B}$ is the transverse intersection of $O_w$ with the graph of the Frobenius map $F : \cal{B} \to \cal{B}$. The $G$-action on $\cal{B} \times \cal{B}$ restricts to a $G^F$-action on $X_w$, so the formal sum $$\begin{aligned}
R_w = \sum_n
{(-1)^n}\ur{H}_!^n(X_w)
\end{aligned}$$ defines a virtual representation of $G^F$. In general, a virtual representation of $G^F$ is **unipotent** iff it occurs with nonzero multiplicity in $R_w$ for some $w$.

We have $X_1 = \cal{B}^F$, a scheme of finitely many points, and $R_1 = \bar{\mathbf{Q}}_\ell[\cal{B}^F]$, the $\bar{\mathbf{Q}}_\ell$-vector space of functions on $\cal{B}^F$. For all $B \in \cal{B}^F$, let $\bb{1}_B$ be the indicator function on $\{B\}$. Recall, *cf.* Remark [\[rem:iwahori\]](#rem:iwahori){reference-type="ref" reference="rem:iwahori"}, that Iwahori constructed an isomorphism $$\begin{aligned}
\bar{\mathbf{Q}}_\ell\otimes H_W|_{\bm{q}^{1/2} = q^{1/2}} \xrightarrow{\sim} \End_{G^F}(R_1).
\end{aligned}$$ In terms of the functions $\bb{1}_B$, the action of $\sigma_w \in H_W$ on $R_1$ is given by $$\begin{aligned}
\label{eq:hecke-operator}
\tilde{\sigma}_w \cdot \bb{1}_B = \sum_{(B, B') \in O_w^F}
\bb{1}_{B'},
\end{aligned}$$ where $\tilde{\sigma}_w = q^{\frac{|w|}{2}} \sigma_w$.

Irreducible representations of $W$ give rise to unipotent virtual representations of $G^F$ in two ways:

### 

For any $\phi \in \hat{W}$, the formal $\bb{Q}$-linear combination $$\begin{aligned}
\label{eq:almost}
R_\phi = \frac{1}{|W|} \sum_{w \in W} \phi(w)R_w
\end{aligned}$$ has nonzero multiplicity in $R_1$ (where we mean $1 \in W$, not $1 \in \hat{W}$), so it is unipotent. The characters of the virtual representations $R_\phi$ are called **almost-characters**, being very close to irreducible characters: See Lemma-Postulate [\[lempost:almost\]](#lempost:almost){reference-type="ref" reference="lempost:almost"}, below.

### 

For any $\phi \in \hat{W}$, the trace $\phi_{\bm{q}} : \bb{Q}(\bm{q}^{\frac{1}{2}}) \otimes H_W \to \bb{Q}(\bm{q}^{\frac{1}{2}})$ (see §[\[subsec:hecke-generic\]](#subsec:hecke-generic){reference-type="ref" reference="subsec:hecke-generic"}) restricts to a function $H_W \to  \bb{Z}[\bm{q}^{\pm\frac{1}{2}}]$ [@gp Thm. 9.3.5]. So we can set $$\begin{aligned}
\phi_q = \phi_{\bm{q}}|_{\bm{q}^{1/2} = q^{1/2}} : H_W \to \bb{Z}[q^{\pm\frac{1}{2}}].
\end{aligned}$$ Then the double centralizer theorem gives an isomorphism of $(H_W \times G^F)$-modules $$\begin{aligned}
\label{eq:double-centralizer}
R_1 \simeq \bigoplus_{\phi \in \hat{W}}
V_{\phi, q} \otimes \rho_\phi,
\end{aligned}$$ where $V_{\phi, q}$, *resp.* $\rho_\phi$, is a simple $H_W$-module of character $\phi_q$, *resp.* a unipotent irreducible representation of $G^F$. The representations $\rho_\phi$ are called the **unipotent principal series**.

If $\rho$ is a representation of $G^F$, then $\Hom_{G^F}(R_1, \rho)$ forms an $\End_{G^F}(R_1)$-module under precomposition. In particular, applying $\Hom_{G^F}(R_1, -)$ to both sides of [\[eq:double-centralizer\]](#eq:double-centralizer){reference-type="eqref" reference="eq:double-centralizer"} yields an isomorphism of $H_W$-bimodules: $$\begin{aligned}
\End_{G^F}(R_1) \simeq \bigoplus_{\phi \in \hat{W}}
V_{\phi, q} \otimes \Hom_{G^F}(R_1, \rho_\phi).
\end{aligned}$$ By Artin--Wedderburn, we deduce:

::: lem
[]{#lem:restriction label="lem:restriction"} For all $\phi \in \hat{W}$, we have $\Hom_{G^F}(R_1, \rho_\phi) \simeq V_{\phi, q}$ as $\End_{G^F}(R_1)$-modules, hence as $H_W$-modules.
:::

The map $\rho \mapsto \Hom_{G^F}(R_1, \rho)$ extends uniquely to an additive map from virtual representations to virtual modules. We emphasize that *$\Hom_{G^F}(R_1, \rho)$ may still be nonzero even when its virtual dimension $(R_1, \rho)_{G^F}$ is zero*.

## 

Lusztig showed that the unipotent irreducible representations of $G^F$ can be indexed by a set that only depends on $W$ [@lusztig_1984 Ch. 4]. This is the set denoted $\mathrm{Uch}(W)$ in §[\[subsec:fourier\]](#subsec:fourier){reference-type="ref" reference="subsec:fourier"}. Abusing notation, we will conflate the elements of $\mathrm{Uch}(W)$ with the unipotent irreducible representations themselves. Then the embedding $\hat{W} \to \mathrm{Uch}(W)$ is precisely the map $\phi \mapsto \rho_\phi$. Cor. 4.24-4.25 of [@lusztig_1984] entail:

::: lempost
[]{#lempost:almost label="lempost:almost"} There is a function $\Delta : \mathrm{Uch}(W) \to \{\pm 1\}$ such that for all $\phi \in \hat{W}$, we have:

1.  $\Delta(\rho_\phi) = 1$.

2.  The transformation rule $$\begin{aligned}
    R_\phi
    =   \sum_{\rho \in \mathrm{Uch}(W)}
    {\{\rho_\phi, \rho\}}\Delta(\rho)\rho.
    \end{aligned}$$ Equivalently, $(\Delta(\rho)\rho, R_\phi) = \{\rho_\phi, \rho\}$ for all $\rho \in \mathrm{Uch}(W)$.
:::

::: rem
We have $R_\phi(1) = \mathrm{Feg}_\phi(q)$ and $\rho_\phi(1) = \mathrm{Deg}_\phi(q)$ for all $\phi \in \hat{W}$.
:::

## 

Springer conjectured [@springer_1976], and Kazhdan proved [@kazhdan], a remarkable identity relating the character values of the virtual representations $R_w$ to the action of $W$ on the fibers of the Grothendieck--Springer map. To state it, let $\cal{B}_g$ denote the fiber of $\tilde{G} \to G$ above $g \in G^F$, and let $$\begin{aligned}
Q_g(w) = \sum_n
{\tr(wF \mid \ur{H}^{2n}(\cal{B}_g))}.
\end{aligned}$$ (By [@dlp], $\cal{B}_g$ has no odd cohomology.) The main result of [@kazhdan] implies:

::: thm
[]{#thm:kazhdan label="thm:kazhdan"} For all $g \in G^F$ and $w \in W$, we have $Q_g(w) = R_w(g)$.
:::

::: rem
Lusztig generalized the functions $Q_g$ to bad characteristic in [@lusztig_1981], and similarly generalized Kazhdan's theorem in [@lusztig_1990].
:::

## 

In this subsection, we state our arguments in such a way that *we do not need to assume $G$ is semisimple*. The following result recovers Theorem [\[thm:virtual\]](#thm:virtual){reference-type="ref" reference="thm:virtual"} in the semisimple case.

::: thm
[]{#thm:virtual-reductive label="thm:virtual-reductive"} For all $\beta \in \mathit{Br}_W^+$, we have $$\begin{aligned}
(\langle{\tilde{\beta}}\rangle_{\bm{q}} \cdot \varepsilon[\Sym(\bb{V})]_{\bm{q}})|_{\bm{q}^{1/2} = q^{1/2}}
&= \frac{(-1)^{r}}{|G^F|}
    \sum_{u \in \cal{U}^F}
    |\cal{U}(\beta)_u^F| Q_u
\end{aligned}$$ in $\bb{Q}(q^{\frac{1}{2}}) \otimes R(W)$, where $\tilde{\beta} = q^{\frac{|\beta|}{2}} \beta$.
:::

::: rem
[]{#rem:special label="rem:special"} An algebraic group $H$ is **special** iff every principal $H$-bundle in the étale topology is Zariski-locally trivial [@grothendieck_1958]. If $G$ is special, then [@hr Appendix] and [@joyce Thm. 4.10] together imply that the right-hand side of the identity is the virtual weight series of $[\cal{Z}(\beta)/G]$. In this case, the identity is essentially a corollary of Theorem [\[thm:decat\]](#thm:decat){reference-type="ref" reference="thm:decat"}. The sign character appears when we use Verdier duality to match the dual of Borel--Moore homology with compactly-supported cohomology, *cf.* [@ahjr Lem. 4.5].

However, not all reductive algebraic groups are special. If $X_0$ is a $G_0$-variety and $G$ is not special, then the virtual weight series of $[X/G]$ need not be the quotient of the virtual weight polynomial of $X$ by that of $G$: See [@joyce Ex. 4.9]. The force of Theorem [\[thm:virtual\]](#thm:virtual){reference-type="ref" reference="thm:virtual"} is that for $X_0 = \cal{Z}(\beta)_0$, that property holds anyway.
:::

The following orthogonality result for the characters $Q_u$ will reduce our work to computing the multiplicities $(Q_u, \langle{\tilde{\beta}}\rangle_{\bm{q}})_W$. We are using the version quoted by Shoji in [@shoji 510], in turn based on [@springer_1976 Thm. 5.6]. The counterpart for the characters $R_w$ is [@dl Thm. 6.9], which holds in any characteristic.

::: thm
[]{#thm:orthogonality label="thm:orthogonality"} For all $\phi \in R(W)$, we have $$\begin{aligned}
q^N \phi \cdot \varepsilon Q_1 
= 
\sum_{u \in \cal{U}^F}
{(Q_u, \phi)_W} Q_u
\end{aligned}$$ in $R(W)$.
:::

Before we can use Theorem [\[thm:orthogonality\]](#thm:orthogonality){reference-type="ref" reference="thm:orthogonality"}, we must rewrite the left-hand side of the orthogonality identity:

::: lem
[]{#lem:q1 label="lem:q1"} We have $[\Sym(\bb{V})]_{\bm{q}} = \frac{(-1)^r}{|G^F|} \bm{q}^N Q_1$.
:::

::: proof
*Proof.* We have $\cal{B}_1 = \cal{B}$, so the Borel isomorphism states that $Q_1$ is the algebra of $W$-coinvariants of $\bb{V}$, graded by $\bm{q}$. That is, $$\begin{aligned}
Q_1 = [\Sym(\bb{V})]_{\bm{q}} \cdot \prod_{1 \leq i \leq r} {(1 - \bm{q}^{d_i})},
\end{aligned}$$ where $d_1, \ldots, d_r$ are the invariant degrees of the $W$-action on $\bb{V}$ [@gp 149]. (If $G$ is not semisimple, then we might have $d_i = 1$ for one or more $i$.) At the same time, if $B_0 \subseteq G_0$ is a fixed Borel, then $$\begin{aligned}
|G^F| = |B^F||\cal{B}^F| = \bm{q}^N (\bm{q}- 1)^r \sum_{w \in W} \bm{q}^{|w|}.
\end{aligned}$$ By the Bott--Solomon formula [@solomon], $\sum_{w \in W} \bm{q}^{|w|} = \prod_{i : d_i \neq 1} \frac{\bm{q}^{d_i} - 1}{\bm{q}- 1} = \prod_i \frac{\bm{q}^{d_i} - 1}{\bm{q}- 1}$. ◻
:::

Combining Theorem [\[thm:orthogonality\]](#thm:orthogonality){reference-type="ref" reference="thm:orthogonality"} and Lemma [\[lem:q1\]](#lem:q1){reference-type="ref" reference="lem:q1"}, it remains to prove the following multiplicity formula:

::: prop
[]{#prop:multiplicity label="prop:multiplicity"} For any $G$-orbit $C \subseteq \cal{U}$ and $\beta \in \mathit{Br}_W^+$, we have $$\begin{aligned}
\sum_{u \in C^F}
{(Q_u, \langle{\tilde{\beta}}\rangle_{\bm{q}})_W|_{\bm{q}^{1/2} = q^{1/2}}}
= 
\sum_{u \in C^F}
|\cal{U}(\beta)_u^F|,
\end{aligned}$$ where $\tilde{\beta} = q^{\frac{|\beta|}{2}} \beta$.
:::

::: lem
[]{#lem:reciprocity label="lem:reciprocity"} For all $\beta \in H_W$ and $w \in W$, we have $$\begin{aligned}
\langle{\beta}\rangle_{\bm{q}}(w)|_{\bm{q}^{1/2} = q^{1/2}} = \tr(\beta \mid \Hom_{G^F}(R_1, R_w)).
\end{aligned}$$
:::

::: proof
*Proof.* By Lemma [\[lem:restriction\]](#lem:restriction){reference-type="ref" reference="lem:restriction"} and Lemma-Postulate [\[lempost:almost\]](#lempost:almost){reference-type="ref" reference="lempost:almost"}, the left-hand side equals $$\begin{aligned}
\sum_{\phi, \psi \in \hat{W}}
    (\rho_\phi, R_\psi)_{G^F} \tr(\beta \mid \Hom_{G^F}(R_1, \rho_\phi)) \psi(w).
\end{aligned}$$ If $\rho \in \mathrm{Uch}(W)$ does not take the form $\rho_\phi$ for some $\phi \in \hat{W}$, then $\Hom_{G^F}(R_1, \rho) = 0$. So above, the sum over $\phi \in \hat{W}$ can be extended to a sum over $\rho \in \mathrm{Uch}(W)$, giving $$\begin{aligned}
\begin{split}
&\sum_{\psi \in \hat{W}} \sum_{\rho \in \mathrm{Uch}(W)}
(\rho, R_\psi)_{G^F} 
\tr(\beta \mid \Hom_{G^F}(R_1, \rho)) \psi(w)\\
&=  \sum_{\psi \in \hat{W}}
    \tr(\beta \mid \Hom_{G^F}(R_1, R_\psi)) \psi(w).
\end{split}
\end{aligned}$$ By [\[eq:almost\]](#eq:almost){reference-type="eqref" reference="eq:almost"} and Schur orthogonality, the last expression is $\tr(\beta \mid \Hom_{G^F}(R_1, R_w))$. ◻
:::

::: lem
[]{#lem:point-count label="lem:point-count"} For all $\beta \in \mathit{Br}_W^+$ and $g \in G^F$, we have $$\begin{aligned}
|G(\beta)_g^F| = \tr(\tilde{\beta} \times g \mid R_1),
\end{aligned}$$ where $\tilde{\beta} = q^{\frac{|\beta|}{2}} \beta$.
:::

::: proof
*Proof.* Fix $B_0 \in \cal{B}^F$. Suppose that $\beta = \sigma_{s_1} \cdots \sigma_{s_\ell}$, where $s_1, \ldots, s_\ell \in S$. Then $$\begin{aligned}
G(\beta)_{g, B_0}^F 
\simeq 
\left\{(B_1, \ldots, B_\ell) \in (\cal{B}^F)^\ell : 
\begin{array}{ll}
B_0 = g^{-1} B_\ell g,\\
(B_{i - 1}, B_i) \in O_{s_i} &\text{for $1 \leq i \leq \ell$}
\end{array}
\right\}.
\end{aligned}$$ By [\[eq:hecke-operator\]](#eq:hecke-operator){reference-type="eqref" reference="eq:hecke-operator"}, the cardinality of the right-hand side is precisely the coefficient of $\bb{1}_{B_0}$ in the expansion of $(\tilde{\beta}, g) \cdot \bb{1}_{B_0}$ with respect to the basis $\{\bb{1}_B\}_{B \in \cal{B}^F}$ of $R_1$. Summing over $B_0$ gives the result. ◻
:::

::: proof
*Proof of Proposition [\[prop:multiplicity\]](#prop:multiplicity){reference-type="ref" reference="prop:multiplicity"}.* By Schur orthogonality, Lemma [\[lem:reciprocity\]](#lem:reciprocity){reference-type="ref" reference="lem:reciprocity"}, and Theorem [\[thm:kazhdan\]](#thm:kazhdan){reference-type="ref" reference="thm:kazhdan"}, $$\begin{aligned}
\begin{split}
(Q_u, \langle{\tilde{\beta}}\rangle_{\bm{q}})_W
&=  \frac{1}{|W|} \sum_{w \in W} {\langle{\beta}\rangle_{\bm{q}}(w)} Q_u(w)\\
&=  \frac{1}{|W|} \sum_{w \in W} {\tr(\beta \mid \Hom_{G^F}(R_1, R_w))} R_w(u).
\end{split}
\end{aligned}$$ On the other hand, by Lemma [\[lem:point-count\]](#lem:point-count){reference-type="ref" reference="lem:point-count"}, [\[eq:double-centralizer\]](#eq:double-centralizer){reference-type="eqref" reference="eq:double-centralizer"}, and Lemma [\[lem:restriction\]](#lem:restriction){reference-type="ref" reference="lem:restriction"}, $$\begin{aligned}
\begin{split}
|\cal{U}(\beta)_u^F| 
&=  \tr(\tilde{\beta} \times u \mid R_1)\\
&=  \sum_{\phi \in \hat{W}}
    \phi_{\bm{q}}(\tilde{\beta}) \rho_\phi(u)\\
&=  \sum_{\rho \in \mathrm{Uch}(W)}
    \tr(\beta \mid \Hom_{G^F}(R_1, \rho)) \rho(u).
\end{split}
\end{aligned}$$ So the following result concludes the proof. ◻
:::

::: prop
We have $$\begin{aligned}
\sum_{u \in C^F} \rho(u) = 
\sum_{u \in C^F}
\frac{1}{|W|}
\sum_{w \in W}
{(\rho, R_w)_{G^F}}
R_w(u)
\end{aligned}$$ for any $G$-orbit $C \subseteq \cal{U}$ and $\rho \in \mathrm{Uch}(W)$.
:::

::: proof
*Proof.* This is shown on pages 497-498 of [@lusztig_2011], relying on [@geck_1996 Prop. 1.3]. ◻
:::

::: rem
If $G$ is of type $A$, then the identity holds without summing over $C^F$ on both sides, *i.e.*, at the level of individual $u \in C^F$.
:::

## 

Recall from Section [\[sec:decat\]](#sec:decat){reference-type="ref" reference="sec:decat"} that for any topological braid $\beta$, we write $\hat{\beta}$ for its link closure and $[\hat{\beta}]_{\bm{q}} \in \bb{Z}(\!(\bm{q}^{\frac{1}{2}})\!)[a^{\pm 1}]$ to denote the HOMFLY series of the link; for any finite Coxeter group $W$, we write $\mathsf{tr} : H_W \to \bb{Z}[\bm{q}^{\pm\frac{1}{2}}](a)$ to denote Gomi's Markov trace. In [@kalman], Kálmán proved the following result.

::: thm
For all $n$ and $\beta \in \mathit{Br}_n$, we have an equality of $\bm{q}^{\frac{1}{2}}$-series: $$\begin{aligned}
\text{coefficient of $a^{|\beta| + n - 1}$ in $[\widehat{\beta\pi}]$}
=
\text{coefficient of $a^{|\beta| - n + 1}$ in $[\hat{\beta}]$}.
\end{aligned}$$ More generally, if $W$ is any finite Coxeter group of rank $r$, then we have an equality $$\begin{aligned}
\text{coefficient of $a^{2r}$ in $\overline{\mathsf{tr}}(\beta \pi)$}
=
\text{coefficient of $a^0$ in $\overline{\mathsf{tr}}(\beta)$},
\end{aligned}$$ where $\overline{\mathsf{tr}} = \pa{\frac{1 - a^2}{1 - \bm{q}}}^r\mathsf{tr}$.
:::

More precisely, [@kalman] includes two proofs of the statement about HOMFLY. The second proof only uses the structure of $H_W$, so it generalizes to a proof of the statement about $\mathsf{tr}$. By Proposition [\[prop:markov\]](#prop:markov){reference-type="ref" reference="prop:markov"}, we deduce:

::: cor
For any finite Coxeter group $W$ and $\beta \in \mathit{Br}_W$, we have $$\begin{aligned}
(\varepsilon, \langle{\beta\pi}\rangle_{\bm{q}}^0)_W = \bm{q}^{\frac{|\pi|}{2}} (1, \langle{\beta}\rangle_{\bm{q}}^0)_W.
\end{aligned}$$
:::

::: cor
[]{#cor:virtual label="cor:virtual"} Under the hypotheses of Theorem [\[thm:virtual-reductive\]](#thm:virtual-reductive){reference-type="ref" reference="thm:virtual-reductive"}, we have $$\begin{aligned}
|\cal{X}(\beta\pi)^F| = |\cal{U}(\beta)^F|.
\end{aligned}$$
:::

::: proof
*Proof.* The proof is similar to that of Corollary [\[cor:kr-to-varieties\]](#cor:kr-to-varieties){reference-type="ref" reference="cor:kr-to-varieties"} in Section [\[sec:kr\]](#sec:kr){reference-type="ref" reference="sec:kr"}. Namely, by Springer theory, we have:

1.  $(1, Q_u)_W = 1$ for all $u \in \cal{U}^F$.

2.  $(\varepsilon, Q_1)_W = \bm{q}^{\dim \cal{B}}$ and $(\varepsilon, Q_u)_W = 0$ for all $u \neq 1$.

Now, Theorem [\[thm:virtual-reductive\]](#thm:virtual-reductive){reference-type="ref" reference="thm:virtual-reductive"} and the preceding corollary together imply $q^{\dim \cal{B}} |\cal{X}(\beta\pi)^F| = q^{\frac{|\pi|}{2}} |\cal{U}(\beta)^F|$. But we have $\dim \cal{B} = N = |w_0| = \frac{1}{2}|\pi|$. ◻
:::

::: rem
We claim that, in the case where $\beta = \sigma_w$, Corollary [\[cor:virtual\]](#cor:virtual){reference-type="ref" reference="cor:virtual"} recovers Proposition 2.2 of [@lusztig_2021]. In our notation, the latter states that $$\begin{aligned}
\label{eq:r-polynomial}
|\cal{U}(\sigma_w)^F| = q^N |\cal{B}^F| R_{1, w}(q),
\end{aligned}$$ where $R_{1, w}(\bm{q}) \in \bb{Z}[\bm{q}]$ is the so-called $R$-polynomial defined in [@kl]. If $B_+, B_- \in \cal{B}^F$ are fixed Borels in opposite position, then $$\begin{aligned}
R_{1, w} = |\{B \in \cal{B}^F : (B_+, B) \in O_w,\, (B, B_-) \in O_{w_0}\}|
\end{aligned}$$ by [@kl Lem. A.4]. So, by the transitivity of the $G^F$-action on $O_{w_0}^F$, we have $$\begin{aligned}
|\cal{X}(\sigma_w\pi)^F| = |O_{w_0}^F| R_{1, w}(q) 
= q^{\dim \cal{B}} |\cal{B}^F| R_{1, w}(q).
\end{aligned}$$ Now Corollary [\[cor:virtual\]](#cor:virtual){reference-type="ref" reference="cor:virtual"} implies [\[eq:r-polynomial\]](#eq:r-polynomial){reference-type="eqref" reference="eq:r-polynomial"}.
:::

## 

In the next subsection, we will prove Theorem [\[thm:induction\]](#thm:induction){reference-type="ref" reference="thm:induction"}. Before doing so, we set notation for parabolic subgroups and review how they interact with the virtual representations $R_w$.

Fix a split torus $T_0 \subseteq G_0$. We identify the character lattice $\bb{X}$ in the root datum of $G$ with the character lattice of $T$. We identify the set $S \subseteq W$ with the set of reflections in $\bb{V}^\vee$ corresponding to a system of simple roots in $\bb{X}$. This system of simple roots determines a Borel $B_0 = T_0 \ltimes U_0$.

If $P_0$ is a parabolic subgroup of $G_0$ containing $B_0$, then the Weyl group of the Levi quotient of $P_0$ is an $S$-parabolic subgroup of $W$ (see §[\[subsec:parabolic\]](#subsec:parabolic){reference-type="ref" reference="subsec:parabolic"}). (Conversely, every $S$-parabolic subgroup of $W$ arises in this way.) We fix such a parabolic $P_0$. We write $U_{P, 0}$ and $L_0$ for its unipotent radical and Levi quotient, respectively. In general, we will distinguish the data attached to $L_0$ with a subscript. Thus,

1.  $W_L$ is the Weyl group of $L_0$.

2.  $\cal{B}_{L, 0}$ is the flag variety of $L_0$.

3.  $\cal{U}_{L, 0}$ is the unipotent locus of $L_0$.

4.  If $\beta \in \mathit{Br}_{W_L}^+$, then we write $O_L(\beta)_0$ for the analogue of $O(\beta)$ with $L_0$ in place of $G_0$.

5.  If $w \in W_L$, then $R_{L, w}$ is the Deligne--Lusztig virtual character with $L^F$ in place of $G^F$.

The following formula for the parabolic restriction of the $R_w$ is [@carter Prop. 7.4.4], though it originates in [@dl §8].

::: prop
[]{#prop:induction-deligne-lusztig label="prop:induction-deligne-lusztig"} For all $w \in W$, we have $$\begin{aligned}
(R_w)^{U_P^F} = \frac{1}{|W_L|} \sum_{\substack{x \in W \\ xwx^{-1} \in W_L}} R_{L, xwx^{-1}}
\end{aligned}$$ as virtual representations of $L^F$, where $(-)^{U_P^F}$ means we take $U_P^F$-invariants.
:::

## 

We now use Theorem [\[thm:virtual\]](#thm:virtual){reference-type="ref" reference="thm:virtual"} to prove Theorem [\[thm:induction\]](#thm:induction){reference-type="ref" reference="thm:induction"}. In what follows, let $W' \subseteq W$ be a parabolic subgroup, and let $d \geq 0$ be the difference in their ranks.

### 

First, we establish the commutative diagram: $$\label{eq:induction-br}
\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2.5em, column sep=3em, text height=2ex, text depth=0.5ex]
{   \mathit{Br}_{W'}
        &R(W')[\![\bm{q}]\!]\\
    \mathit{Br}_W
        &R(W)[\![\bm{q}]\!]\\
        };
\path[->,font=\scriptsize, auto]
(m-1-1)     edge node{$\langle{-}\rangle_{\bm{q}}^0$} (m-1-2)
            edge (m-2-1)
(m-1-2)     edge node{$\frac{1}{(1 - \bm{q})^d} \Ind_{W'}^W$} (m-2-2)
(m-2-1)     edge node{$\langle{-}\rangle_{\bm{q}}^0$} (m-2-2);
\end{tikzpicture}$$ We can and will assume that $W' = W_L$ in the setup of the previous subsection.

To disambiguate notation, we will write $\langle{-}\rangle_{\bm{q}}^0$, *resp.* $\langle{-}\rangle_{\bm{q}}^{0'}$, for the function on $\mathit{Br}_W$, *resp.* $\mathit{Br}_{W'}$. For all $w \in W'$, let the $G_0$-schemes $\cal{U}_{w, 0}$, $\cal{U}_{L, w, 0}$ over $\bb{F}$ be defined by the cartesian squares: $$\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2.5em, column sep=3em, text height=2ex, text depth=0.5ex]
{   O_{w, 0}
        &\cal{U}_{w, 0}\\
    \cal{B}_0 \times \cal{B}_0
        &\cal{U}_0 \times \cal{B}_0\\
        };
\path[->,font=\scriptsize, auto]
(m-1-2)     edge (m-1-1)
            edge (m-2-2)
(m-1-1)     edge (m-2-1)
(m-2-2)     edge node[above]{$\mathit{act}$} (m-2-1);
\end{tikzpicture}
\qquad
\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2.5em, column sep=3em, text height=2ex, text depth=0.5ex]
{   O_{L, w, 0}
        &\cal{U}_{L, w, 0}\\
    \cal{B}_{L, 0} \times \cal{B}_{L, 0}
        &\cal{U}_{L, 0} \times \cal{B}_{L, 0}\\
        };
\path[->,font=\scriptsize, auto]
(m-1-2)     edge (m-1-1)
            edge (m-2-2)
(m-1-1)     edge (m-2-1)
(m-2-2)     edge node[above]{$\mathit{act}$} (m-2-1);
\end{tikzpicture}$$ Let $\bb{V}' = \bb{V}/\bb{V}^{W'}$, so that $\bb{V}'$ is a realization of $W'$ satisfying $(\bb{V}')^{W'} = 0$. Then $d = \dim \bb{V} - \dim \bb{V}'$. So for all $x \in W'$, Theorems [\[thm:kazhdan\]](#thm:kazhdan){reference-type="ref" reference="thm:kazhdan"} and [\[thm:virtual-reductive\]](#thm:virtual-reductive){reference-type="ref" reference="thm:virtual-reductive"} give $$\begin{aligned}
\langle{\sigma_w}\rangle_{\bm{q}}^0(x)|_{\bm{q}= q}
&=  \frac{(-1)^{r - |\beta|}}{|G^F|}
    \sum_{u \in \cal{U}^F} 
    |(\cal{U}_w)_u^F| R_x(u),\\
\frac{(\Ind_{W'}^W \langle{\sigma_w}\rangle_{\bm{q}}^{0'})(x)|_{\bm{q}= q}}{(1 - q)^d}
&=  \frac{(-1)^{r - |\beta|}}{|L^F||W'|}
    \sum_{u' \in \cal{U}_L^F} 
    \sum_{\substack{y \in W \\ yxy^{-1} \in W'}}
    |(\cal{U}_{L, w})_{u'}^F| 
    R_{L, yxy^{-1}}(u').
\end{aligned}$$ Since $\beta \mapsto {(-\bm{q}^{-\frac{1}{2}})^{|\beta|}}\langle{\beta}\rangle_{\bm{q}}^0$ is linear as a function on $H_W$, it remains to match the right-hand sides above for all $w$ and $x$. By Proposition [\[prop:induction-deligne-lusztig\]](#prop:induction-deligne-lusztig){reference-type="ref" reference="prop:induction-deligne-lusztig"}, we further reduce the problem to: $$\begin{aligned}
\label{eq:l-to-g}
\frac{1}{|G^F|}
    \sum_{u \in \cal{U}^F} 
    |(\cal{U}_w)_u^F| R_x(u)
&=  
    \frac{1}{|L^F|}
    \sum_{u' \in \cal{U}_L^F} 
    |(\cal{U}_{L, w})_{u'}^F| 
    (\Res_{P^F}^{G^F} R_x)^{U_P^F}(u').
\end{aligned}$$ We will rewrite the point counts on both sides. Let $(\cal{U}_w)_B \subseteq \cal{U}_w$ be the fiber of $\cal{U}_w \to \cal{U} \times \cal{B} \to \cal{B}$ above our fixed Borel $B \in \cal{B}^F$, so that $$\begin{aligned}
(\cal{U}_w)_B^F = \{u \in \cal{U}^F : (u^{-1}Bu, B) \in O_w\}.
\end{aligned}$$ Let $B^F$ act on $G^F$, *resp.* $(\cal{U}_w)_B^F$, by right multiplication, *resp.* right conjugation. (Thus its action on $(\cal{U}_w)_B^F \times G^F$ is free.) Analogously to Lemma [\[lem:assoc-bundle\]](#lem:assoc-bundle){reference-type="ref" reference="lem:assoc-bundle"}, we have:

::: lem
[]{#lem:bruhat label="lem:bruhat"} We have a $G^F$-equivariant bijection $$\begin{aligned}
\begin{array}{rcl}
((\cal{U}_w)_B^F \times G^F)/B^F 
    &\xrightarrow{\sim} 
    &\cal{U}_w^F\\
{[u, g]}
    &\mapsto 
    &gug^{-1}
\end{array}
\end{aligned}$$ where $G^F$ acts on $((\cal{U}_w)_B^F \times G^F)/B^F$ by left multiplication on the factor of $G^F$.
:::

Let $\{\cal{U}_i^F\}_i$ be the set of $G^F$-orbits of $\cal{U}^F$. For each $i$ such that $\cal{U}_i^F$ intersects $(\cal{U}_w)_B^F$, we pick a point $u_i \in \cal{U}_i^F$. Using Lemma [\[lem:bruhat\]](#lem:bruhat){reference-type="ref" reference="lem:bruhat"}, we expand: $$\begin{aligned}
\begin{split}
\frac{1}{|G^F|}
\sum_{u \in \cal{U}^F} 
    |(\cal{U}_w)_u^F| R_x(u)
&=  \frac{1}{|B^F|}
\sum_i
|\cal{U}_i^F \cap (\cal{U}_w)_B^F| R_x(u_i)\\
&=  \frac{1}{|B^F|}
\sum_{u \in (\cal{U}_w)_B^F}
R_x(u).
\end{split}
\end{aligned}$$ Let $B_L = L \cap B$. As above, let $\{\cal{U}_{L, j}^F\}_j$ be the set of $L^F$-orbits of $\cal{U}_L^F$. For each $j$ such that $\cal{U}_{L, j}^F$ intersects $(\cal{U}_{L, w})_{B_L}^F$, we pick a point $u'_j \in (\cal{U}_{L, j})_{B_L}^F$. Then we can also expand: $$\begin{aligned}
\begin{split}
\frac{1}{|L^F|}
    \sum_{u' \in \cal{U}_L^F}
    |(\cal{U}_{L, w})_{u'}^F|
    (R_x)^{U^F}(u')
&=  \frac{1}{|B_L^F|}
    \sum_j
    |(\cal{U}_{L, j})_B^F|
    (R_x)^{U^F}(u'_j)
    \\
&=  \frac{1}{|B_L^F|}
    \sum_{u' \in (\cal{U}_{L, j})_B^F}
    (R_x)^{U^F}(u')\\
&=  \frac{1}{|B_L^F||U_P^F|}
    \sum_{\substack{u' \in (\cal{U}_{L, j})_B^F \\ u'' \in U_P^F}}
    R_x(u'u'').
\end{split}
\end{aligned}$$ Above, $|B_L^F||U_P^F| = |B^F|$. So the following lemma concludes the proof of [\[eq:l-to-g\]](#eq:l-to-g){reference-type="eqref" reference="eq:l-to-g"}.

::: lem
For all $w \in W_L$, we have $(\cal{U}_w)_B = (\cal{U}_{L, w})_{B_L} U_P \simeq (\cal{U}_{L, w})_{B_L} \times U_P$.
:::

::: proof
*Proof.* Lifting $w \in W_L \simeq N_L(T)/T$ to a point $\dot{w} \in N_L(T)$, we observe that $$\begin{aligned}
B\dot{w}B = U_PB_L\dot{w}B_LU_P = (B_L\dot{w}B_L)U_P \simeq B_L\dot{w}B_L \times U_P.
\end{aligned}$$ But $(\cal{U}_w)_B = B\dot{w}B \cap \cal{U}$ and $(\cal{U}_{L, w})_{B_L} = B_L\dot{w}B_L \cap \cal{U}_L$. ◻
:::

### 

We claim that commutativity of [\[eq:induction-br\]](#eq:induction-br){reference-type="eqref" reference="eq:induction-br"} implies commutativity of: $$\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2.5em, column sep=3em, text height=2ex, text depth=0.5ex]
{   H_{W'}
        &R(W')[\bm{q}^{\pm\frac{1}{2}}]\\
    H_W
        &R(W)[\bm{q}^{\pm\frac{1}{2}}]\\
        };
\path[->,font=\scriptsize, auto]
(m-1-1)     edge node{$\langle{-}\rangle_{\bm{q}}$} (m-1-2)
            edge (m-2-1)
(m-1-2)     edge node{$\Ind_{W'}^W$} (m-2-2)
(m-2-1)     edge node{$\langle{-}\rangle_{\bm{q}}$} (m-2-2);
\end{tikzpicture}$$ This follows from the projection formula for induced representations, as we now explain. If $[\mathop{\mathrm{\text{$\Lambda$}}}(\bb{V})]_{\bm{q}} = \sum_i {(-\bm{q})^i} \mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V})$, then $\varepsilon [\mathop{\mathrm{\text{$\Lambda$}}}(\bb{V})]_{\bm{q}}$ is the multiplicative inverse of $\varepsilon [\Sym(\bb{V})]_{\bm{q}}$ in $R(W)[\![\bm{q}]\!]$. By the projection formula, we have $$\begin{aligned}
\begin{split}
(-\bm{q}^{\frac{1}{2}})^{|\beta|} 
\Ind_{W'}^W \langle{\beta}\rangle_{\bm{q}} 
&=  
    \Ind_{W'}^W
    {(\langle{\beta}\rangle_{\bm{q}}^0 \cdot \varepsilon_{W'} [\mathop{\mathrm{\text{$\Lambda$}}}(\bb{V}')]_{\bm{q}})}\\
&=  
    \Ind_{W'}^W
    {(\langle{\beta}\rangle_{\bm{q}}^0 \cdot \Res_{W'}^W(\varepsilon_W [\mathop{\mathrm{\text{$\Lambda$}}}(\bb{V}')]_{\bm{q}}))}\\
&=  
    (\Ind_{W'}^W \langle{\beta}\rangle_{\bm{q}}^0) \cdot \varepsilon_W [\mathop{\mathrm{\text{$\Lambda$}}}(\bb{V}')]_{\bm{q}}
\end{split}
\end{aligned}$$ Since $d = \dim \bb{V} - \dim \bb{V}'$, we have $$\begin{aligned}
\begin{split}
(-\bm{q}^{\frac{1}{2}})^{|\beta|} \langle{\beta}\rangle_{\bm{q}}
&=  
    \langle{\beta}\rangle_{\bm{q}}^0 \cdot \varepsilon_W [\mathop{\mathrm{\text{$\Lambda$}}}(\bb{V})]_{\bm{q}}\\
&=
    \frac{1}{(1 - \bm{q})^d}\,\langle{\beta}\rangle_{\bm{q}}^0 \cdot \varepsilon_W [\mathop{\mathrm{\text{$\Lambda$}}}(\bb{V}')]_{\bm{q}}.
\end{split}
\end{aligned}$$ So the commutativity of [\[eq:induction-br\]](#eq:induction-br){reference-type="eqref" reference="eq:induction-br"} implies $\Ind_{W'}^W(\langle{\beta}\rangle_{\bm{q}}) = \langle{\beta}\rangle_{\bm{q}}$, as needed.

## 

Finally, we prove Theorem [\[thm:pole\]](#thm:pole){reference-type="ref" reference="thm:pole"}, stating that $$\begin{aligned}
\langle{\beta}\rangle_{\bm{q}}^0 \in \frac{1}{(1 - \bm{q})^{r(w)}}\, R(W)[\bm{q}],
\end{aligned}$$ where $w$ is the image of $\beta$ in $W$ and $r(w) = \dim \bb{V}^w$.

First, we introduce a function $\delta : W \to \bb{Z}$. For all $w \in W$, we claim that $$\begin{aligned}
\delta(w) = \lim_{\bm{q}\to 1} 
\frac{\det(1 - \bm{q}w \mid \bb{V})}{(1 - \bm{q})^{r(w)}}
\end{aligned}$$ exists and takes values in $\bb{Z}$. Indeed, since $w$ has finite order, its action on $\bb{V}$ is diagonalizable. Thus $r(w)$ equals the multiplicity of $1 - \bm{q}$ in the characteristic polynomial $\det(1 - \bm{q}w \mid \bb{V})$. This shows that $\delta(w)$ exists. It is an integer because $\bb{Q}_W = \bb{Q}$ and character values are algebraic integers. We can now state:

::: thm
[]{#thm:isotropy label="thm:isotropy"} If $G$ is semisimple and $\beta \in \mathit{Br}_W^+$ maps to $w \in W$, then the isotropy groups of the $G$-action on $G(\beta)$ are diagonalizable groups $D$ such that $$\begin{aligned}
|D^F|
\quad\text{divides}\quad
(q - 1)^{r(w)} \delta(w)|Z(G)|,
\end{aligned}$$ where $Z(G)$ is the center of $G$. In particular, the isotropy groups of the $G^F$-action on $G(\beta)^F$ satisfy the same divisibility condition.
:::

::: proof
*Proof.* Fix a maximal split torus $T_0 \subseteq G_0$ and a lift $\dot{w} \in N_G(T)$ of $w$. In the case where $G$ is adjoint and $w$ is **elliptic**, meaning $T^w$ is discrete, the proof is analogous to the proof of [@lusztig_2011 Thm. 5.2]. However, the argument there actually shows more: For general $G$ and $w$, it shows that we can assume $D \subseteq T^{\dot{w}}$, independently of $\beta$. Let $\bar{G} = G/Z(G)$, the adjoint group of $G$, and let $\bar{T}, \bar{D}$ be the images of $T, D$ in $\bar{G}$. Writing $\bar{T}'$ for the identity component of $\bar{T}^{\dot{w}}$, we see that $\bar{T}'$ is a split torus of rank $r(w)$ such that $\bar{T}^{\dot{w}}/\bar{T}'$ is discrete. So we get $|(\bar{T}^{\dot{w}})^F| = (q - 1)^{r(w)}\delta(w)$ from the elliptic case. Finally, $|(T^{\dot{w}})^F| = |(\bar{T}^{\dot{w}})^F||Z(G)|$. ◻
:::

::: proof
*Proof of Theorem [\[thm:pole\]](#thm:pole){reference-type="ref" reference="thm:pole"}.* Combining Theorems [\[thm:virtual\]](#thm:virtual){reference-type="ref" reference="thm:virtual"} and [\[thm:isotropy\]](#thm:isotropy){reference-type="ref" reference="thm:isotropy"}, we see that $$\begin{aligned}
\label{eq:pole-1}
\langle{\beta}\rangle_{\bm{q}}^0|_{\bm{q}= q} \in \frac{1}{(1 - q)^{r(w)} \delta(w)|Z(G)|}\, R(W)
\end{aligned}$$ for all $q \gg 0$. At the same time, by Proposition [\[prop:rationality\]](#prop:rationality){reference-type="ref" reference="prop:rationality"}, $$\begin{aligned}
\label{eq:pole-2}
\langle{\beta}\rangle_{\bm{q}}^0 \in \frac{1}{(1 - \bm{q}^{d_1}) \cdots (1 - \bm{q}^{d_r})}\, R(W)[\bm{q}_0],
\end{aligned}$$ where $\bm{q}_0$ is defined by [\[eq:exception\]](#eq:exception){reference-type="eqref" reference="eq:exception"} and $d_i \in \bb{Z}$ for all $i$. Therefore, [\[eq:pole-1\]](#eq:pole-1){reference-type="eqref" reference="eq:pole-1"} simplifies to $$\begin{aligned}
\langle{\beta}\rangle_{\bm{q}}^0|_{\bm{q}= q} \in \frac{1}{(1 - q)^{r(w)}}\, R(W)
\end{aligned}$$ for all $q \gg 0$. Therefore, [\[eq:pole-2\]](#eq:pole-2){reference-type="eqref" reference="eq:pole-2"} simplifies to $$\begin{aligned}
\langle{\beta}\rangle_{\bm{q}}^0 \in \frac{1}{(1 - \bm{q})^{r(w)}}\, R(W)[\bm{q}],
\end{aligned}$$ as needed. ◻
:::
