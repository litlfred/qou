---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-005-5-steinberg-schemes-of-braids
section_title: "Steinberg Schemes of Braids"
section_number: 5
pages: 38-41
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.953
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the Weyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
[]{#sec:varieties label="sec:varieties"}

## 

Let $S \subseteq W$ be the set of simple reflections in the chosen Coxeter presentation of $W$. Let $\mathit{Br}_W$ be the Artin braid group of $W$, and let $\mathit{Br}_W^+ \subseteq \mathit{Br}_W$ be the monoid of positive braids determined by $S$. Each element $s \in S$ lifts to an element $\sigma_s \in \mathit{Br}_W^+$, such that $\{\sigma_s\}_{s \in S}$ is a generating set for $\mathit{Br}_W^+$. The following result is [@deligne_1997 §1.11].

::: thm
There is a map from elements $\beta \in \mathit{Br}_W^+$ to $G_0$-varieties $O(\beta)_0$ over $\cal{B}_0 \times \cal{B}_0$ such that:

1.  $O(\sigma_s)_0 = O_{s, 0}$ for all $s \in S$.

2.  If $\beta = \beta'\beta''$, then there is a fixed isomorphism $$\begin{aligned}
    O(\beta)_0 \xrightarrow{\sim} O(\beta')_0 \times_{\cal{B}_0} O(\beta'')_0,
    \end{aligned}$$ where the fiber product is formed with respect to the right projection $O(\beta')_0 \to \cal{B}_0$ and the left projection $O(\beta'')_0 \to \cal{B}_0$. These isomorphisms are associative in the sense that the diagram $$\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
    \matrix(m)[matrix of math nodes, row sep=2em, column sep=2em, text height=2ex, text depth=0.5ex]
    {   O(\beta'\beta''\beta''')_0
            &O(\beta'\beta'')_0 \times_{\cal{B}_0} O(\beta''')_0\\
        O(\beta')_0 \times_{\cal{B}_0} O(\beta''\beta''')_0
            &O(\beta')_0 \times_{\cal{B}_0} O(\beta'')_0 \times_{\cal{B}_0} O(\beta''')_0\\
            };
    \path[->,font=\scriptsize, auto]
    (m-1-1)     edge node{$\sim$} (m-1-2)
                edge node[rotate=90,above]{$\sim$} (m-2-1)
    (m-1-2)     edge node[rotate=90,below]{$\sim$} (m-2-2)
    (m-2-1)     edge node{$\sim$} (m-2-2);
    \end{tikzpicture}$$ is commutative.

    In particular, if $w = s_1 \cdots s_\ell$ is a reduced expression, then $$\begin{aligned}
    O(\sigma_w)_0 
    \simeq O(\sigma_{s_1})_0 \times_{\cal{B}_0} \cdots \times_{\cal{B}_0} O(\sigma_{s_\ell})_0
    \simeq O_{w, 0}
    \end{aligned}$$ by way of these fixed isomorphisms.
:::

Deligne attributes the varieties $O(\beta)_0$ to Broué--Michel [@bm_1997], though they are implicit in Lusztig's earlier papers on character sheaves.

Note that $\dim O(\beta) = |\beta| + N$, where $|\beta|$ is the writhe of $\beta$ (see §[\[subsec:braid-group\]](#subsec:braid-group){reference-type="ref" reference="subsec:braid-group"}).

## 

Rouquier introduced an extension of Deligne's result in which the full group $\mathit{Br}_W$ replaces the monoid $\mathit{Br}_W^+$, and in which objects of $\sf{H}_W$ replace varieties over $\cal{B}_0 \times \cal{B}_0$. The fiber product over $\cal{B}_0$ is replaced by the convolution on $\sf{H}_W$.

Each element $s \in S$ gives rise to objects $\cal{R}_s^+, \cal{R}_s^- \in \sf{H}_W$ that can be represented by complexes of the following form: $$\begin{aligned}
\begin{array}{rcllllll}
\cal{R}_s^+ &= &0 &\to &\underline{{\mathit{IC}_s}} &\to &\mathit{IC}_1\langle 1\rangle,\\[1ex]
\cal{R}_s^- &= &\mathit{IC}_1\langle -1\rangle &\to &\underline{{\mathit{IC}_s}} &\to &0.
\end{array}
\end{aligned}$$ Above, the underlined terms are the terms in degree zero. To describe the morphisms, factor $j_1 : O_{1, 0} \to \cal{B}_0 \times \cal{B}_0$ as the composition $$\begin{aligned}
O_{1, 0} \xrightarrow{i_s} \bar{O}_{s, 0} \xrightarrow{\bar{j}_s} \cal{B}_0 \times \cal{B}_0.
\end{aligned}$$ Since $O_{1, 0}$ and $\bar{O}_{s, 0}$ are smooth and closed in $\cal{B}_0^2$, we have $$\begin{aligned}
\mathit{IC}_1 &= j_{1, \ast}\bar{\mathbf{Q}}_\ell\langle -r - N\rangle,\\
\mathit{IC}_s &= \bar{j}_{s, \ast}\bar{\mathbf{Q}}_\ell\langle 1 - r - N\rangle.
\end{aligned}$$ Then the nontrivial morphism in $\cal{R}_s^+$, *resp.* $\cal{R}_s^-$, is induced by pushing forward $$\begin{aligned}
\bar{\mathbf{Q}}_\ell
    &\to i_{s, \ast} i_s^\ast \bar{\mathbf{Q}}_\ell
    \xrightarrow{\sim} i_{s, \ast} \bar{\mathbf{Q}}_\ell,\\
\emph{resp.}\qquad
i_{s, \ast} \bar{\mathbf{Q}}_\ell\langle -2\rangle 
    &\xrightarrow{\sim} i_{s,!} i_s^! \bar{\mathbf{Q}}_\ell
    \to \bar{\mathbf{Q}}_\ell,
\end{aligned}$$ along $\bar{j}_s$.

In [@soergel], Soergel gave a module-theoretic description of $\sf{C}(\cal{B} \times \cal{B})$ (see Remark [\[rem:by\]](#rem:by){reference-type="ref" reference="rem:by"}), and hence, of $\sf{H}_W$. Under it, the complexes $\cal{R}_s^+$ and $\cal{R}_s^-$ correspond to the complexes of bimodules over $\Sym(\bb{V})$ defined by Rouquier in §9.2.1 and §9.2.4 of [@rouquier_2006]. Thus, Thm. 10.5 of *ibid.* amounts to the following result:

::: thm
[]{#thm:rouquier label="thm:rouquier"} There is a map from elements $\beta \in \mathit{Br}_W^+$ to objects $\cal{R}(\beta) \in \sf{H}_W$ such that:

1.  $\cal{R}(\sigma_s) = \cal{R}_s^+$ and $\cal{R}(\sigma_s^{-1}) = \cal{R}_s^-$ for all $s \in S$.

2.  If $\beta = \beta' \beta''$, then there is a fixed isomorphism $$\begin{aligned}
            \cal{R}(\beta) \xrightarrow{\sim} \cal{R}(\beta') \star \cal{R}(\beta'').
            
    \end{aligned}$$ These isomorphisms are associative in the sense that the diagram $$\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
    \matrix(m)[matrix of math nodes, row sep=2em, column sep=2em, text height=2ex, text depth=0.5ex]
    {   \cal{R}(\beta'\beta''\beta''')
            &\cal{R}(\beta'\beta'')_0 \star \cal{R}(\beta''')\\
        \cal{R}(\beta')_0 \star \cal{R}(\beta''\beta''')
            &\cal{R}(\beta') \star \cal{R}(\beta'') \star \cal{R}(\beta''')\\
            };
    \path[->,font=\scriptsize, auto]
    (m-1-1)     edge node{$\sim$} (m-1-2)
                edge node[rotate=90,above]{$\sim$} (m-2-1)
    (m-1-2)     edge node[rotate=90,below]{$\sim$} (m-2-2)
    (m-2-1)     edge node{$\sim$} (m-2-2);
    \end{tikzpicture}$$ commutes.
:::

## 

The results of Deligne and Rouquier are related as follows. For all $w \in W$, let $j_\beta$ be the map $O(\beta)_0 \to \cal{B}_0 \times \cal{B}_0$. Let $$\begin{aligned}
\Delta(\beta) &= j_{\beta, !} \bar{\mathbf{Q}}_\ell\langle |\beta| - r - N\rangle,\\
\nabla(\beta) &= j_{\beta, \ast} \bar{\mathbf{Q}}_\ell\langle |\beta| - r - N\rangle.
\end{aligned}$$ In the case where $\beta = \sigma_s$, we abbreviate by writing $\Delta_s = \Delta(\beta)$ and $\nabla_s = \nabla(\beta)$. The following lemma is strongly suggested by the statements in [@rouquier_2006 §11], though it does not seem to appear there.

::: lem
[]{#lem:realization-rouquier label="lem:realization-rouquier"} We have $$\begin{aligned}
\rho(\cal{R}(\beta)) 
    &\simeq \Delta(\beta),\\
\rho(\cal{R}(\beta^{-1}))
    &\simeq \nabla(\beta)
\end{aligned}$$ for all $\beta \in \mathit{Br}_W^+$.
:::

::: proof
*Proof.* The explicit definitions of $\cal{R}_s^+$ and $\cal{R}_s^-$ show that $$\begin{aligned}
\rho(\cal{R}_s^+) &\simeq \Delta_s,\\
\rho(\cal{R}_s^-) &\simeq \nabla_s
\end{aligned}$$ for all $s \in S$. We now apply the commutativity of [\[eq:convolution-realization\]](#eq:convolution-realization){reference-type="eqref" reference="eq:convolution-realization"}. ◻
:::

## 

We define $G_0$-schemes $G(\beta)_0$, $\cal{U}(\beta)_0$, $\cal{Z}(\beta)_0$ by stipulating that all squares in the commutative diagram below are cartesian. $$\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2.5em, column sep=3.5em, text height=2ex, text depth=0.5ex]
{   O(\beta)_0
        &G(\beta)_0
        &\cal{U}(\beta)_0
        &\cal{Z}(\beta)_0\\
    \cal{B}_0 \times \cal{B}_0
        &G_0 \times \cal{B}_0
        &\cal{U}_0 \times \cal{B}_0
        &\tilde{\cal{U}}_0 \times \cal{B}_0\\
        };
\path[->,font=\scriptsize, auto]
(m-1-2)     edge (m-1-1)
(m-1-3)     edge (m-1-2)
(m-1-4)     edge (m-1-3)
(m-1-1)     edge node[left]{$\mathit{pr}_0 \times \mathit{pr}_\ell$} (m-2-1)
(m-1-2)     edge (m-2-2)
(m-1-3)     edge (m-2-3)            
(m-1-4)     edge (m-2-4)
(m-2-2)     edge node[above]{$\mathit{act}$} (m-2-1)
(m-2-3)     edge node[above]{$i \times \id$} (m-2-2)
(m-2-4)     edge node[above]{$p \times \id$} (m-2-3);
\end{tikzpicture}$$ Let $\bb{1} \in \mathit{Br}_W$ denote the identity braid. Then $\cal{U}(\bb{1})_0 = \tilde{\cal{U}}_0$, the Springer resolution, and $\cal{Z}(\bb{1})_0 = \cal{Z}_0$, the Steinberg scheme from the previous section.

::: df
For all $\beta \in \mathit{Br}_W^+$, we say that $\cal{Z}(\beta)_0$ is the **Steinberg scheme** attached to $\beta$.
:::

In what follows, let $p_\beta$ be the composition $\cal{U}(\beta)_0 \to \cal{U}_0 \times \cal{B}_0 \to \cal{U}_0$. Note that $p_{\bb{1}, !}\bar{\mathbf{Q}}_\ell\simeq p_{\bb{1}, \ast}\bar{\mathbf{Q}}_\ell\simeq \cal{S}$. We can now prove Theorem [\[thm:a_w-to-varieties\]](#thm:a_w-to-varieties){reference-type="ref" reference="thm:a_w-to-varieties"}, relating the $\bb{A}_W$ trace to the generalized Steinberg schemes $\cal{Z}(\beta)_0$.

::: thm
[]{#thm:a_w-to-varieties-strong label="thm:a_w-to-varieties-strong"} For all $\beta \in \mathit{Br}_W^+$ and $i, j$, we have: $$\begin{aligned}
\sf{AH}^{i, j}(\cal{R}(\beta))
    &\simeq \gr_{j + r}^{\bm{w}} \SHom^{i + r}(p_{\beta, !}\bar{\mathbf{Q}}_\ell, \cal{S}),\\
\sf{AH}^{i, j}(\cal{R}(\beta^{-1}))
    &\simeq \gr_{j + r}^{\bm{w}} \SHom^{i + r}(p_{\beta, \ast}\bar{\mathbf{Q}}_\ell, \cal{S}).
\end{aligned}$$ In particular, since $\cal{S} = p_\ast \bar{\mathbf{Q}}_\ell\langle -r\rangle$, we have $$\begin{aligned}
\begin{split}
\sf{AH}^{i, j}(\cal{R}(\beta))
    &\simeq \gr_{j + 2r}^{\bm{w}} \ur{H}_{-(i + 2r)}^{!, G}(\cal{Z}(\beta))
\end{split}
\end{aligned}$$ by Lemma [\[lem:borel-moore\]](#lem:borel-moore){reference-type="ref" reference="lem:borel-moore"}.
:::

::: proof
*Proof.* By the commutativity of [\[eq:a_w\]](#eq:a_w){reference-type="eqref" reference="eq:a_w"}, Lemma [\[lem:realization-rouquier\]](#lem:realization-rouquier){reference-type="ref" reference="lem:realization-rouquier"}, and both smooth and proper base change, $$\begin{aligned}
\begin{split}
\sf{AH}^{i, j}(\cal{R}(\beta)) 
&\simeq     \gr_j^{\bm{w}} \SHom^i(\sf{K}^b(i^\ast\langle -r\rangle \circ \sf{CH} \circ \rho)(R(\beta)), \cal{S})\\
&\simeq     \gr_j^{\bm{w}} \SHom^i((i^\ast\langle -r\rangle \circ \sf{CH})(\Delta(\beta)), \cal{S})\\
&\simeq     \gr_{j + r}^{\bm{w}} \SHom^{i + r}(p_{\beta, !} \bar{\mathbf{Q}}_\ell, \cal{S}).
\end{split}
\end{aligned}$$ The argument for $\cal{R}(\beta^{-1})$ is completely analogous. The remaining statement follows from Lemma [\[lem:borel-moore\]](#lem:borel-moore){reference-type="ref" reference="lem:borel-moore"}. ◻
:::
