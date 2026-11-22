---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-007-7-the-decategorified-trace
section_title: "The Decategorified Trace"
section_number: 7
pages: 45-52
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.97
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the Weyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
[]{#sec:decat label="sec:decat"}

## 

To state the main definition of this section, let $W$ denote an *arbitrary* finite Coxeter group.

As before, $H_W$ is the Iwahori--Hecke algebra of $W$. Moreover, we will draw freely upon the notation introduced in Appendix [\[sec:coxeter\]](#sec:coxeter){reference-type="ref" reference="sec:coxeter"}:

-   $R(W)$ is the representation ring of $W$.

-   $\bb{Q}_W \subseteq \bar{\bb{Q}}$ is the splitting field of $W$.

-   $(-, -)_W : R(W) \times R(W) \to \bb{Z}$ be the multiplicity pairing.

-   We write $$\begin{aligned}
    {[\Sym(\bb{V})]_{\bm{q}}} = \sum_i {\bm{q}^i} \Sym^i(\bb{V}).
    \end{aligned}$$

-   If $\phi : W \to \bb{Q}_W$ is an irreducible character, then $\phi_{\bm{q}} : H_W(\bm{q}^{\frac{1}{2}}) \to \bb{Q}_W(\bm{q}^{\frac{1}{2}})$ is the corresponding $\bb{Z}[\bm{q}^{\pm\frac{1}{2}}]$-linear trace.

-   $\{-, -\} : \hat{W} \times \hat{W} \to \bb{Q}_W$ is the symmetric pairing (derived from) Lusztig's exotic Fourier transform.

::: df
For any finite Coxeter group $W$, the **$R(W)$ trace** on its Iwahori--Hecke algebra is the $\bb{Z}[\bm{q}^{\pm\frac{1}{2}}]$-linear trace $$\begin{aligned}
\langle{-}\rangle_{\bm{q}} : H_W \to R(W) \otimes \bb{Q}_W(\bm{q}^{\frac{1}{2}})
\end{aligned}$$ defined by $$\begin{aligned}
\langle{\beta}\rangle_{\bm{q}} = \sum_{\phi, \psi \in \hat{W}} {\{\phi, \psi\}} 
\phi_{\bm{q}}(\beta)\psi
\end{aligned}$$ for all $\beta \in H_W$.
:::

In the next two subsections, we assume that $W$ is still a Weyl group and prove Theorem [\[thm:decat\]](#thm:decat){reference-type="ref" reference="thm:decat"}, which relates the $R(W)$ trace to the decategorification of the $\bb{A}_W$ trace. In the remainder of the section, we allow $W$ to be an arbitrary finite Coxeter group and relate the $R(W)$ trace to the Markov trace studied by Ocneanu and Gomi. We conclude by proving Propositions [\[prop:rationality\]](#prop:rationality){reference-type="ref" reference="prop:rationality"} and [\[prop:symmetry\]](#prop:symmetry){reference-type="ref" reference="prop:symmetry"}, which roughly generalize rationality and symmetry properties of the Markov trace.

## 

Recall that an object of $\mathsf{Mod}_2^b(\bar{\mathbf{Q}}_\ell[W])$ is a $\bar{\mathbf{Q}}_\ell[W]$-module equipped with a $W$-invariant bigrading where the first grading is bounded below and the second is bounded. We have an additive map $$\begin{aligned}
\sf{AH} : H_W \xrightarrow{\sim} [\sf{H}_W]_\triangle \to [\mathsf{Mod}_2^b(\bar{\mathbf{Q}}_\ell[W])]_\oplus
\end{aligned}$$ induced by the composition $$\begin{aligned}
\sf{H}_W^\op \xrightarrow{\sf{AH}} \mathsf{Mod}_2^b(\bb{A}_W) \to \mathsf{Mod}_2^b(\bar{\mathbf{Q}}_\ell[W]),
\end{aligned}$$ where the second arrow is the forgetful functor. Note that $\mathsf{Mod}_2^b(\bar{\mathbf{Q}}_\ell[W])$ is semisimple, since $\bar{\mathbf{Q}}_\ell[W]$ is.

For any ring $R$, such as $R = R(W)$, we write $R(\!(\bm{q}^{\frac{1}{2}})\!) = R[\![\bm{q}^{\frac{1}{2}}]\!][\frac{1}{\bm{q}}]$. Let $$\begin{aligned}
_{\bm{q}} : [\sf{Mod}_{1, 1}(\bar{\mathbf{Q}}_\ell[W])]_\oplus \to R(W)(\!(\bm{q}^{\frac{1}{2}})\!)
\end{aligned}$$ be the additive map defined by $$\begin{aligned}
_{\bm{q}} = \sum_{i, j}
{(-1)^{i - j}} \bm{q}^{\frac{j}{2}} M^{i, j}.
\end{aligned}$$ We say that $[M]_{\bm{q}}$ is the **$\bm{q}$-graded character** of $M$. For all $i, j$, let $$\begin{aligned}
(\sf{AH}^\vee)^{i, j}(-) = \Hom_{\bar{\mathbf{Q}}_\ell}(\sf{AH}^{i, j}(-), \bar{\mathbf{Q}}_\ell).
\end{aligned}$$ Then the composition $$\begin{aligned}
_{\bm{q}} \vcentcolon= [-]_{\bm{q}} \circ \sf{AH}^\vee
    : H_W \to R(W)(\!(\bm{q}^{\frac{1}{2}})\!)
\end{aligned}$$ is $\bb{Z}[\bm{q}^{\pm\frac{1}{2}}]$-linear.

## 

Recall from Section [\[sec:hecke\]](#sec:hecke){reference-type="ref" reference="sec:hecke"} that $\{\gamma_w\}_w$ denotes the Kazhdan--Lusztig basis of the Iwahori--Hecke algebra. Then Theorem [\[thm:decat\]](#thm:decat){reference-type="ref" reference="thm:decat"} reduces to the claim that: $$\begin{aligned}
_{\bm{q}} = \langle{\gamma_w}\rangle_{\bm{q}} \cdot [\Sym(\bb{V})]_{\bm{q}}
\end{aligned}$$ for all $w \in W$. To prove it, we use a multiplicity formula for unipotent character sheaves, derived from [@lusztig_1985_3 Cor. 14.11] and [@lusztig_1986 Thm. 23.1].

As in §[\[subsec:decat\]](#subsec:decat){reference-type="ref" reference="subsec:decat"}, let $[\sf{C}(G_0)]_\oplus$ be endowed with the action of $\bb{Z}[\bm{q}^{\frac{1}{2}}]$ in which $\bm{q}^{\frac{1}{2}}$ acts by $\langle -1\rangle$. The following version of the formula is the one quoted in [@ww_2008 413], fixed to incorporate semisimplification.

::: thm
[]{#thm:lusztig-character label="thm:lusztig-character"} For all $w \in W$, we have $$\begin{aligned}
{[\sf{CH}(\mathit{IC}_w)^{ss}]} = \sum_{\phi, \psi \in \hat{W}}
{\{\phi, \psi\}} \phi_{\bm{q}}(\gamma_w) [\cal{G}_\psi] + \text{cuspidal terms}
\end{aligned}$$ in $[\sf{C}(G_0)]_\oplus$, where "cuspidal terms" refers to the contribution of simple objects not of the form $\cal{G}_\psi$ for some $\psi \in \hat{W}$, and "$ss$" refers to the semisimplification of (shifted) perverse summands.
:::

::: proof
*Proof of Theorem [\[thm:decat\]](#thm:decat){reference-type="ref" reference="thm:decat"}.* By an argument similar to the proof of the second equivalence in Lemma [\[lem:sheaves-to-reps\]](#lem:sheaves-to-reps){reference-type="ref" reference="lem:sheaves-to-reps"}, Theorem [\[thm:lusztig-algebra\]](#thm:lusztig-algebra){reference-type="ref" reference="thm:lusztig-algebra"} implies that for all $i, j \in \bb{Z}$, we have $$\begin{aligned}
\gr_j^{\bm{w}} \SHom^i(\cal{S}_\psi, \cal{S}) \simeq 
\left\{\begin{array}{ll}
V_\psi \otimes \Sym^{\frac{i}{2}}(\bb{V})
    &i = j\\
0
    &i \neq j
\end{array}\right.
\end{aligned}$$ as representations of $W$. So Theorem [\[thm:lusztig-character\]](#thm:lusztig-character){reference-type="ref" reference="thm:lusztig-character"} yields $$\begin{aligned}
\begin{split}
[\sf{AH}^\vee(\mathit{IC}_w)]_{\bm{q}}
&=  \sum_{i, j} {(-1)^{i - j}} 
    \bm{q}^{\frac{j}{2}}
    \gr_j^{\bm{w}} 
    \SHom^i(i^\ast \sf{CH}(\mathit{IC}_w) \langle -r\rangle, \cal{S})^\vee\\
&=  \sum_{i, j}
    {(-1)^{i - j}}
    \bm{q}^{\frac{j}{2}}
    \sum_{\phi, \psi \in \hat{W}} 
    {\{\phi, \psi\}}
    \phi_{\bm{q}}(\gamma_w)
    \gr_j^{\bm{w}} \SHom^i(\cal{S}_\psi, \cal{S})^\vee\\
&=  \sum_{\phi, \psi \in \hat{W}} 
    {\{\phi, \psi\}}
    \phi_{\bm{q}}(\gamma_w)
    \sum_i
    {\bm{q}^{\frac{i}{2}}}\,
    (\psi \otimes \Sym^{\frac{i}{2}}(\bb{V}))^\vee.
\end{split}
\end{aligned}$$ Every representation of $W$ is self-dual because $\bb{Q}_W = \bb{Q} \subseteq \bb{R}$, so the inner sum in the last expression simplifies to $\psi \cdot [\Sym(\bb{V})]_{\bm{q}}$. ◻
:::

##  {#subsec:markov}

We now relate $\langle{-}\rangle_{\bm{q}}$ to Markov traces.

The **HOMFLY series** of a link $\lambda \subseteq \bb{R}^3$ is one of the predecessors of the isotopy invariant mentioned in Remark [\[rem:dgr\]](#rem:dgr){reference-type="ref" reference="rem:dgr"}. We will denote it by $$\begin{aligned}
_{a, \bm{q}} \in \bb{Z}[(\bm{q}^{\frac{1}{2}} - \bm{q}^{-\frac{1}{2}})^{\pm 1}, a^{\pm 1}].
\end{aligned}$$ We have $[\lambda]_{a, \bm{q}} = \bb{P}(\lambda)|_{t = -1}$, where $\bb{P}$ is the invariant in the remark. With this normalization, the HOMFLY series of the unknot equals $1$.

There are many different constructions of the HOMFLY invariant [@homfly]. Ocneanu's approach relies on Alexander's theorem, stating that every link in $\bb{R}^3$ is the closure of a braid. Namely, one constructs for each $n \geq 1$ a certain function on the Iwahori--Hecke algebra of $S_n$, now known as a Markov trace [@jones]. If $\mathit{Br}_n$ denotes the braid group of $S_n$, *i.e.*, the group of topological braids on $n$ strands, and $\lambda$ is the closure of $\beta \in \mathit{Br}_n$, then the HOMFLY series of $\lambda$ is the Markov trace of $\beta$, multiplied by a factor depending only on $|\beta|$ and $n$.

Y. Gomi generalized Ocneanu's Markov traces in a uniform way beyond type $A$, extending work of Geck--Lambropoulou in type $BC$ [@gomi]. We follow Gomi's conventions here.

Let $(W, S)$ be any finite Coxeter system. Recall from §[\[subsec:parabolic\]](#subsec:parabolic){reference-type="ref" reference="subsec:parabolic"} that if $S' \subseteq S$ and $W' \subseteq W$ is the $S$-parabolic subgroup generated by $S'$, then $H_{W'} \subseteq H_W$. A **Markov trace** on $H_W$ is a $\bb{Z}[\bm{q}^{\pm\frac{1}{2}}]$-linear function $$\begin{aligned}
\mathsf{tr} : H_W \to \bb{Z}[\bm{q}^{\pm\frac{1}{2}}](a)
\end{aligned}$$ such that:

1.  $\mathsf{tr}(1) = 1$.

2.  For all $\beta, \gamma \in H_W$, we have $\mathsf{tr}(\beta\gamma) = \mathsf{tr}(\gamma\beta)$.

3.  For all $s \in S$ and $\gamma \in H_{W'}$, where $W'$ is the $S$-parabolic subgroup of $W$ generated by $S \setminus s$, we have $$\begin{aligned}
            \mathsf{tr}(\sigma_s^{\pm 1}\gamma) 
            = -a^{\mp 1}
                \pa{\frac{\bm{q}^{\frac{1}{2}} - \bm{q}^{-\frac{1}{2}}}{a - a^{-1}}} 
                \mathsf{tr}(\gamma).
            
    \end{aligned}$$

Axioms (2) and (3) are respectively known as the first and second Markov moves.

::: thm
[]{#thm:ocneanu label="thm:ocneanu"} The axioms above uniquely define a Markov trace on the Iwahori--Hecke algebra of $S_n$ for all $n \geq 1$. For all $\beta \in \mathit{Br}_n$, we have $$\begin{aligned}
_{a, \bm{q}}
=   (-a)^{|\beta|}
    \pa{\frac{a - a^{-1}}{\bm{q}^{\frac{1}{2}} - \bm{q}^{-\frac{1}{2}}}}^{n - 1} 
    \mathsf{tr}(\beta),
\end{aligned}$$ where $\hat{\beta}$ is the link closure of $\beta$.
:::

Suppose that a Markov trace on $H_W$ exists. After base change from $\bb{Z}[\bm{q}^{\pm\frac{1}{2}}]$ to $\bb{Q}_W(\bm{q}^{\frac{1}{2}})$, we can view it as a trace on $H_W(\bm{q}^{\frac{1}{2}})$ (see §[\[subsec:hecke-generic\]](#subsec:hecke-generic){reference-type="ref" reference="subsec:hecke-generic"}). Then $$\begin{aligned}
\mathsf{tr} = \sum_{\phi \in \hat{W}} 
\mathsf{tr}_\phi {\phi_{\bm{q}}}
\end{aligned}$$ for some weights $\mathsf{tr}_\phi \in \bb{Q}_W(\bm{q}^{\frac{1}{2}}, a)$.

Axioms (1)-(3) show that $\mathsf{tr}|_{a^{-2} = 0}$ is the symmetrizing trace $\tau_{\bm{q}} : H_W(\bm{q}^{\frac{1}{2}}) \to \bb{Z}[\bm{q}^{\pm\frac{1}{2}}]$. Proposition [\[prop:molien\]](#prop:molien){reference-type="ref" reference="prop:molien"} then suggests that the weights $\mathsf{tr}_\phi$ should involve bivariate Molien series. These observations motivate the form of Gomi's Markov weights. Below, let $\bb{V}$ be a realization of $W$ such that $\bb{V}^W = 0$, and for all $\psi \in \hat{W}$, let $$\begin{aligned}
\begin{split}
\bm{m}_\psi(\bm{q}, x)
&=  \sum_{i, j}
    {(-x)^i} \bm{q}^j
    (\psi, \mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V}) \otimes \Sym^j(\bb{V}))_W.
\end{split}
\end{aligned}$$ By construction, $\bm{m}_\psi(\bm{q}, 0) = \bm{m}_\psi(\bm{q})$, the usual Molien series of $\psi$.

::: thm
[]{#thm:gomi label="thm:gomi"} The weights $$\begin{aligned}
\begin{split}
\mathsf{tr}_\phi
&=  \pa{\frac{1 - \bm{q}}{1 - a^{-2}}}^{r}
    \sum_{\psi \in \hat{W}}
    {\{\phi, \psi\}}
    \bm{m}_\psi(\bm{q}, a^{-2})
\end{split}
\end{aligned}$$ define a Markov trace on $H_W$ for any finite Coxeter group $W$ of rank $r$.
:::

This is a bivariate refinement of Proposition [\[prop:molien\]](#prop:molien){reference-type="ref" reference="prop:molien"}.

Henceforth, $\mathsf{tr}$ denotes Gomi's Markov trace. To relate it to the $R(W)$ trace, we introduce the normalization $$\begin{aligned}
\langle{\beta}\rangle_{\bm{q}}^0 = {(-\bm{q}^{\frac{1}{2}})^{|\beta|}} \langle{\beta}\rangle_{\bm{q}} \cdot \varepsilon [\Sym(\bb{V})]_{\bm{q}},
\end{aligned}$$ where $\varepsilon$ denotes the sign character of $W$ (see §[\[subsec:representation\]](#subsec:representation){reference-type="ref" reference="subsec:representation"}). We emphasize that whenever we use $\langle{-}\rangle_{\bm{q}}^0$, *we always assume that $\bb{V}^W = 0$*. For Weyl groups, the result below follows from Theorems [\[thm:ww\]](#thm:ww){reference-type="ref" reference="thm:ww"} and [\[thm:decat\]](#thm:decat){reference-type="ref" reference="thm:decat"}.

::: prop
[]{#prop:markov label="prop:markov"} Under the hypotheses of Theorem [\[thm:gomi\]](#thm:gomi){reference-type="ref" reference="thm:gomi"}, we have $$\begin{aligned}
\mathsf{tr}(\beta)
=   (-\bm{q}^{-\frac{1}{2}})^{|\beta|}
    \pa{\frac{1 - \bm{q}}{1 - a^2}}^r
    \sum_i
    {(-a^2)^i}
    (\mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V}), \langle{\beta}\rangle_{\bm{q}}^0)_W
\end{aligned}$$ for all $\beta \in \mathit{Br}_W$.
:::

::: lem
[]{#lem:self-dual label="lem:self-dual"} We have $$\begin{aligned}
\frac{1}{(1 - x^{-1})^r}
\sum_i {(-x^{-1})^i} \mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V})
=   
\frac{\varepsilon}{(1 - x)^r}
\sum_i {(-x)^i} \mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V})
\end{aligned}$$ in $R(W)(x)$.
:::

::: proof
*Proof.* Use the identity $\mathop{\mathrm{\text{$\Lambda$}}}^{r - i}(\bb{V}) = \varepsilon \mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V})$. ◻
:::

::: proof
*Proof of Proposition [\[prop:markov\]](#prop:markov){reference-type="ref" reference="prop:markov"}.* By Lemma [\[lem:self-dual\]](#lem:self-dual){reference-type="ref" reference="lem:self-dual"} and the self-duality of $\Sym(\bb{V})$, $$\begin{aligned}
\mathsf{tr}_\phi
=   \pa{\frac{1 - \bm{q}}{1 - a^2}}^r 
\sum_{\psi \in \hat{W}}
{\{\phi, \psi\}}
\sum_{i, j} {(-a^2)^i} \bm{q}^j
(\mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V}), \varepsilon \psi \cdot \Sym^j(\bb{V}))_W.
\end{aligned}$$ Comparing with the terms that make up $\langle{-}\rangle_{\bm{q}}^0$, we get the result. ◻
:::

::: cor
Under the hypotheses of Theorem [\[thm:gomi\]](#thm:gomi){reference-type="ref" reference="thm:gomi"}, we have $$\begin{aligned}
\tau_{\bm{q}} = (-\bm{q}^{-\frac{1}{2}})^{|\beta|} (1 - \bm{q})^r (\varepsilon, \langle{\beta}\rangle_{\bm{q}}^0)_W
\end{aligned}$$ as $\bb{Z}[\bm{q}^{\pm \frac{1}{2}}]$-linear traces on $H_W$.
:::

::: cor
[]{#cor:homfly label="cor:homfly"} Under the hypotheses of Theorem [\[thm:ocneanu\]](#thm:ocneanu){reference-type="ref" reference="thm:ocneanu"}, we have $$\begin{aligned}
{[\hat{\beta}]_{a, \bm{q}}}
=   (a\bm{q}^{-\frac{1}{2}})^{|\beta| - n + 1}
    \sum_{0 \leq i \leq n - 1}
    {(-a^2)^i}
    (\mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V}), \langle{\beta}\rangle_{\bm{q}}^0)_W
\end{aligned}$$ for all $\beta \in \mathit{Br}_n$.
:::

##  {#section-3}

To conclude this section, we prove:

1.  Proposition [\[prop:rationality\]](#prop:rationality){reference-type="ref" reference="prop:rationality"}, a rationality result that will simplify the proof of Theorem [\[thm:pole\]](#thm:pole){reference-type="ref" reference="thm:pole"} in Section [\[sec:dl\]](#sec:dl){reference-type="ref" reference="sec:dl"}.

2.  Proposition [\[prop:symmetry\]](#prop:symmetry){reference-type="ref" reference="prop:symmetry"}, a symmetry result. Together with (1) and Theorem [\[thm:pole\]](#thm:pole){reference-type="ref" reference="thm:pole"}, it implies Theorem [\[thm:symmetry\]](#thm:symmetry){reference-type="ref" reference="thm:symmetry"}, as we will also explain.

These results about the $R(W)$ trace respectively generalize, and are inspired by, the following facts about the HOMFLY series:

1.  HOMFLY has integer coefficients. Moreover, it is a $\bm{q}^{\frac{1}{2}}$-monomial shift of an element of $\bb{Z}[\![\bm{q}]\!][a^{\pm 1}]$, not just of $\bb{Z}[\![\bm{q}^{\frac{1}{2}}]\!][a^{\pm 1}]$.

2.  HOMFLY is invariant under $\bm{q}^{\frac{1}{2}} \mapsto -\bm{q}^{-\frac{1}{2}}$.

Note that the second claim of (1$'$) can be proved via the Markov trace, while (2$'$) is a consequence of the HOMFLY skein relation (see [@dgr §2.4], noting that their $q$ is our $\bm{q}^{\frac{1}{2}}$). By contrast, the proofs below are representation-theoretic. Throughout, we assume that the realization $\bb{V}$ satisfies $\bb{V}^W = 0$.

###  {#section-4}

Let $d_1, \ldots, d_r$ be the invariant degrees of the $W$-action on $\bb{V}$. Let: $$\begin{aligned}
\label{eq:exception}
\bm{q}_0 = 
\left\{\begin{array}{ll}
\bm{q}^{\frac{1}{2}}
    &\text{$W$ has a factor of type $E_7$ or $E_8$}\\
\bm{q}
    &\text{else}
    \end{array}\right.
\end{aligned}$$ The reason we make an exception for $E_7$ and $E_8$ is the existence of so-called exceptional characters in these types. See [@gp §9.5] and the references therein.

::: prop
[]{#prop:rationality label="prop:rationality"} For all $\beta \in \mathit{Br}_W$, we have $$\begin{aligned}
\langle{\beta}\rangle_{\bm{q}} &\in (\bm{q}^{-\frac{1}{2}})^{|\beta|} R(W)[\bm{q}_0],\\
\langle{\beta}\rangle_{\bm{q}}^0 &\in \frac{1}{(1 - \bm{q}^{d_1}) \cdots (1 - \bm{q}^{d_r})}\, R(W)[\bm{q}_0],\\
(1, \langle{\beta}\rangle_{\bm{q}}^0)_W &\in \frac{1}{(1 - \bm{q}^{d_1}) \cdots (1 - \bm{q}^{d_r})}\, (1 + \bm{q}_0\bb{Z}[\bm{q}_0]).
\end{aligned}$$
:::

::: proof
*Proof.* Let $\tilde{\beta} = \bm{q}^{\frac{|\beta|}{2}} \beta$. To prove the first statement, we must show that $$\begin{aligned}
(\psi, \langle{\tilde{\beta}}\rangle_{\bm{q}})_W
=   \sum_{\phi \in \hat{W}}
    {\{\phi, \psi\}}
    \phi_{\bm{q}}(\tilde{\beta}) \in \bb{Q}_W(\bm{q}^{\frac{1}{2}})
\end{aligned}$$ actually belongs to $\bb{Z}[\bm{q}_0]$ for all $\psi \in \hat{W}$. We make a series of reductions:

By Lemma-Postulate [\[lempost:fourier\]](#lempost:fourier){reference-type="ref" reference="lempost:fourier"}(1), we can assume that $W$ is irreducible.

We can expand $\tilde{\beta}$ as a $\bb{Z}[\bm{q}]$-linear combination of the elements $\tilde{\sigma}_w = \bm{q}^{\frac{|\sigma_w|}{2}} \sigma_w$ for $w \in W$. So we can assume that $\tilde{\beta} = \tilde{\sigma}_w$ for some $w$.

We can now check the non-crystallographic types case by case, using [@gp §8.3] and [@lusztig_1994] for the dihedral types, [@gp Table 9.1] and [@bm_1993 §7] for type $H_3$ (but see Remark [\[rem:h3\]](#rem:h3){reference-type="ref" reference="rem:h3"}, below), and [@al; @malle] for type $H_4$. So we can assume that $W$ is crystallographic.

Theorem [\[thm:decat\]](#thm:decat){reference-type="ref" reference="thm:decat"} implies that $(\psi, \langle{\tilde{\beta}}\rangle_{\bm{q}})_W \in \bb{Z}[\bm{q}^{\pm \frac{1}{2}}]$. So it remains to show that $(\psi, \langle{\tilde{\beta}}\rangle_{\bm{q}})_W \in \bb{Q}[\bm{q}_0]$. Since $\{-, -\}$ takes values in $\bb{Q}_W = \bb{Q}$, it is enough to get $\phi_{\bm{q}}(\tilde{\sigma}_w) \in \bb{Q}[\bm{q}_0]$ for all $\phi$. For crystallographic irreducible $W$, this is a theorem of Benson--Curtis [@bc] (joint with Springer in the case of $E_7$ and $E_8$).

The remaining two statements follow from the first statement, once we establish the following two lemmas. ◻
:::

::: lem
We have $$\begin{aligned}
{[\Sym(\bb{V})]_{\bm{q}}} \in \frac{1}{(1 - \bm{q}^{d_1}) \cdots (1 - \bm{q}^{d_r})}\, R(W)[\bm{q}].
\end{aligned}$$
:::

::: proof
*Proof.* In the notation of §[\[subsec:realization\]](#subsec:realization){reference-type="ref" reference="subsec:realization"} and §[\[subsec:degrees\]](#subsec:degrees){reference-type="ref" reference="subsec:degrees"}, we have $$\begin{aligned}
{[\Sym(\bb{V})]_{\bm{q}}} 
= \bm{m}_1(\bm{q})\sum_{\phi \in \hat{W}} {\mathrm{Feg}_\phi(\bm{q})\phi},
\end{aligned}$$ where $\bm{m}_1(\bm{q}) = \prod_i {(1 - \bm{q}^{d_i})^{-1}}$ and $\mathrm{Feg}_\phi(\bm{q}) \in \bb{Z}[\bm{q}]$ for each $\phi$. ◻
:::

::: lem
For all $\beta \in \mathit{Br}_W$, we have $(\varepsilon, \langle{\beta}\rangle_{\bm{q}})_W = \varepsilon_{\bm{q}}(\beta) = (-\bm{q}^{-\frac{1}{2}})^{|\beta|}$.
:::

::: proof
*Proof.* By [@gp 252], we have $\varepsilon_{\bm{q}}(\sigma_s) = -\bm{q}^{-\frac{1}{2}}$ for all $s \in S$. (Note that $T_s = \bm{q}^{\frac{1}{2}}\sigma_s$ in the notation of *ibid.*.) But $\varepsilon_{\bm{q}}$ is the character of a $1$-dimensional $\bb{Q}_W(\bm{q}^{\frac{1}{2}})$-vector space, so it is multiplicative on $\mathit{Br}_W$. We deduce that $\varepsilon_{\bm{q}}(\beta) = (-\bm{q}^{-\frac{1}{2}})^{|\beta|}$ for all $\beta \in \mathit{Br}_W$.

As for the other equality: By [@lusztig_1984 Ch. 4], we have $\{\phi, \varepsilon\} = 0$ for all $\phi \neq \varepsilon$. This implies $(\varepsilon, \langle{\beta}\rangle_{\bm{q}})_W = \varepsilon_{\bm{q}}(\beta)$. ◻
:::

::: rem
[]{#rem:h3 label="rem:h3"} The proof of Proposition [\[prop:rationality\]](#prop:rationality){reference-type="ref" reference="prop:rationality"} uses the explicit description of the exotic Fourier transform in type $H_3$. For this group, there are three nontrivial families (see §[\[subsec:families\]](#subsec:families){reference-type="ref" reference="subsec:families"}), one of which is exceptional. The $4 \times 4$ matrix in [@bm_1993 §7] represents the block of the Fourier matrix for the non-exceptional families. I learned from George Lusztig that by contrast, the data for the exceptional family matches that of the exceptional family in type $E_7$. The assertion in [@gm 189] that all three families have the same Fourier data is incorrect.
:::

###  {#section-5}

Turning to the symmetry result:

::: prop
[]{#prop:symmetry label="prop:symmetry"} For all $\beta \in \mathit{Br}_W$, we have $$\begin{aligned}
\langle{\beta}\rangle_{\bm{q}} 
&\in R(W)[\bm{q}^{\frac{1}{2}} - \varepsilon \bm{q}^{-\frac{1}{2}}],\\
\langle{\beta}\rangle_{\bm{q}}^0
&\in 
    (\bm{q}^{\frac{1}{2}})^{|\beta| - r}
    R(W)[(\bm{q}^{\frac{1}{2}} - \bm{q}^{-\frac{1}{2}})^{\pm 1}].
\end{aligned}$$
:::

By Proposition [\[prop:rationality\]](#prop:rationality){reference-type="ref" reference="prop:rationality"}, $\langle{-}\rangle_{\bm{q}}$ takes values in $R(W)[\bm{q}^{\pm\frac{1}{2}}]$, so the proof amounts to the following lemmas:

::: lem
[]{#lem:symmetry label="lem:symmetry"} For all $\beta \in \mathit{Br}_W$, we have $\langle{\beta}\rangle_{\bm{q}} \mapsto \varepsilon \langle{\beta}\rangle_{\bm{q}}$ under $\bm{q}^{\frac{1}{2}} \mapsto -\bm{q}^{-\frac{1}{2}}$.
:::

::: proof
*Proof.* Recall that for all $\beta \in H_W$, we have $(\psi, \langle{\beta}\rangle_{\bm{q}})_W = \sum_{\phi \in \hat{W}} {\{\phi, \psi\}} \phi_{\bm{q}}(\beta)$. Using Lemma-Postulate [\[lempost:fourier\]](#lempost:fourier){reference-type="ref" reference="lempost:fourier"}(3), we compute $$\begin{aligned}
\begin{split}
(\psi, \varepsilon \langle{\beta}\rangle_{\bm{q}})_W 
&= (\varepsilon\psi, \langle{\beta}\rangle_{\bm{q}})_W \\
&= \sum_\phi
    {\{\phi, \varepsilon \psi\}}
    \phi_{\bm{q}}(\beta)\\
&=  \sum_\phi
    {\{\varepsilon \phi, \varepsilon \psi\}}
    (\varepsilon \phi)_{\bm{q}}(\beta)\\
&=  \sum_\phi
    {\{\phi, \psi\}}
    (\varepsilon \phi)_{\bm{q}}(\beta).
\end{split}
\end{aligned}$$ It remains to show that if $\beta$ is in the image of $\mathit{Br}_W$, then $$\begin{aligned}
\phi_{\bm{q}}(\beta) \mapsto (\varepsilon \phi)_{\bm{q}}(\beta)
\quad\text{under}\quad
\bm{q}^{\frac{1}{2}} \mapsto -\bm{q}^{-\frac{1}{2}}.
\end{aligned}$$ This follows implicitly from the proof of [@gp Prop. 9.4.1(a)]. ◻
:::

::: lem
We have $\bm{q}^{\frac{r}{2}} [\Sym(\bb{V})]_{\bm{q}} \mapsto \varepsilon \bm{q}^{\frac{r}{2}} [\Sym(\bb{V})]_{\bm{q}}$ under $\bm{q}^{\frac{1}{2}} \mapsto -\bm{q}^{-\frac{1}{2}}$.
:::

::: proof
*Proof.* Observe that $\sum_i {(-\bm{q})^i} \mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V})$ is the multiplicative inverse of $[\Sym(\bb{V})]_{\bm{q}}$. So the claim follows from Lemma [\[lem:self-dual\]](#lem:self-dual){reference-type="ref" reference="lem:self-dual"} with $x = \bm{q}$. ◻
:::

###  {#section-6}

We show that Proposition [\[prop:rationality\]](#prop:rationality){reference-type="ref" reference="prop:rationality"}, Proposition [\[prop:symmetry\]](#prop:symmetry){reference-type="ref" reference="prop:symmetry"}, and Theorem [\[thm:pole\]](#thm:pole){reference-type="ref" reference="thm:pole"} together imply Theorem [\[thm:symmetry\]](#thm:symmetry){reference-type="ref" reference="thm:symmetry"}.

::: proof
*Proof of Theorem [\[thm:symmetry\]](#thm:symmetry){reference-type="ref" reference="thm:symmetry"}.* Proposition [\[prop:rationality\]](#prop:rationality){reference-type="ref" reference="prop:rationality"} shows that if $W$ has no factors of type $E_7$ or $E_8$, then $\langle{\beta}\rangle_{\bm{q}}^0$ and $(1, \langle{\beta}\rangle_{\bm{q}}^0)_W$ are indeed rational functions in $\bm{q}$, not just power series in $\bm{q}^{\frac{1}{2}}$. Theorem [\[thm:pole\]](#thm:pole){reference-type="ref" reference="thm:pole"} extends this result to all $W$. These results, combined with Proposition [\[prop:symmetry\]](#prop:symmetry){reference-type="ref" reference="prop:symmetry"}, establish $$\begin{aligned}
\langle{\beta}\rangle_{\bm{q}} 
&\in \bm{q}^{-\frac{|\beta|}{2}}R(W)[\bm{q}] \cap R(W)[\bm{q}^{\frac{1}{2}} - \varepsilon \bm{q}^{-\frac{1}{2}}],\\
\langle{\beta}\rangle_{\bm{q}}^0
&\in 
    R(W)[\![\bm{q}]\!] \cap R(W)(\bm{q}) \cap
    (\bm{q}^{\frac{1}{2}})^{|\beta| - r}
    R(W)[(\bm{q}^{\frac{1}{2}} - \bm{q}^{-\frac{1}{2}})^{\pm 1}].
\end{aligned}$$ In particular, the $\bm{q}$-degrees of $\langle{\beta}\rangle_{\bm{q}}^0$ and $(1, \langle{\beta}\rangle_{\bm{q}}^0)_W$ are well-defined. The following observations show that their degrees must be $|\beta| - r$:

-   Proposition [\[prop:rationality\]](#prop:rationality){reference-type="ref" reference="prop:rationality"} shows that $\langle{\beta}\rangle_{\bm{q}}^0$, and hence $(1, \langle{\beta}\rangle_{\bm{q}}^0)_W$, belong to $\bb{Z}[\![\bm{q}]\!]$, *i.e.*, their lowest-order term in $\bm{q}$ is the constant term.

-   By Proposition [\[prop:symmetry\]](#prop:symmetry){reference-type="ref" reference="prop:symmetry"}, we have $$\begin{aligned}
    \langle{\beta}\rangle_{\bm{q}}^0 \mapsto (-\bm{q})^{r - |\beta|}\langle{\beta}\rangle_{\bm{q}}^0
    \quad\text{under}\quad
    \bm{q}_0 \mapsto \bm{q}_0^{-1}.
    \end{aligned}$$

-   Proposition [\[prop:rationality\]](#prop:rationality){reference-type="ref" reference="prop:rationality"} also shows that $(1, \langle{\beta}\rangle_{\bm{q}}^0)_W$, and hence $\langle{\beta}\rangle_{\bm{q}}^0$, have nonzero constant term.

 ◻
:::
