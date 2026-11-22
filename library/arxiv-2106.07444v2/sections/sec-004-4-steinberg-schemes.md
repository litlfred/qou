---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-004-4-steinberg-schemes
section_title: "Steinberg Schemes"
section_number: 4
pages: 32-38
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.973
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the Weyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
[]{#sec:steinberg label="sec:steinberg"}

## 

In Section [\[sec:hecke\]](#sec:hecke){reference-type="ref" reference="sec:hecke"}, we reviewed the (mixed) Springer sheaf $\cal{S} \in \sf{D}_{G, m}^b(\cal{U}_0)$ and the (mixed) Grothendieck--Springer sheaf $\cal{G} \in \sf{D}_{G, m}^b(G_0)$. In Section [\[sec:a_w\]](#sec:a_w){reference-type="ref" reference="sec:a_w"}, we gave a construction of a graded algebra $\bb{A}_K$ from a mixed complex $K$: explicitly, $$\begin{aligned}
\begin{split}
\bb{A}_K 
&= \bigoplus_n
{\gr_0^{\bm{w}}}
\SHom^0(K, K\langle n\rangle)\\
&\simeq \bigoplus_n
{\gr_n^{\bm{w}}}
\SEnd^n(K).
\end{split}
\end{aligned}$$ In this section, we use topological methods to prove Theorem [\[thm:pure-iso\]](#thm:pure-iso){reference-type="ref" reference="thm:pure-iso"}: The map $$\begin{aligned}
i^\ast : \bb{A}_\cal{G} \to \bb{A}_\cal{S}
\end{aligned}$$ induced by $i : \cal{U}_0 \to \cal{G}_0$ via Lemma [\[lem:pullback\]](#lem:pullback){reference-type="ref" reference="lem:pullback"} is an isomorphism of graded $\bar{\mathbf{Q}}_\ell$-algebras.

::: rem
[]{#rem:impure label="rem:impure"} By Lemma [\[lem:unipotent\]](#lem:unipotent){reference-type="ref" reference="lem:unipotent"}, $\SEnd^n(\cal{S})$ is concentrated in weight $n$ (see also [@rider Lem. 5.4].) However, if $n > 0$, then $\SEnd^n(\cal{G})$ is not concentrated in weight $n$, essentially because the cohomology of the Grothendieck--Springer resolution of $G$ contains the cohomology of a torus. See Example [\[ex:identity\]](#ex:identity){reference-type="ref" reference="ex:identity"}.
:::

::: rem
Our proof of Theorem [\[thm:pure-iso\]](#thm:pure-iso){reference-type="ref" reference="thm:pure-iso"} is inspired by an unpublished note of Riche about the analogous statement at the level of Lie algebras, which is well-known. Riche states that his note was inspired by [@cg §3.4].
:::

## 

If $X_0$ is a $G_0$-variety over $\bb{F}$, with structure map $a : X_0 \to \mathit{pt}_0$, then its mixed equivariant dualizing complex is $$\begin{aligned}
\omega = \omega_{X_0/G_0} \vcentcolon= a^!\bar{\mathbf{Q}}_\ell\in \sf{D}_{G, m}^b(X_0).
\end{aligned}$$ Its equivariant Borel--Moore homology (with coefficients in $\bar{\mathbf{Q}}_\ell$) is $$\begin{aligned}
\ur{H}_{-\ast}^{!, G}(X) \vcentcolon= \SHom^\ast(\bar{\mathbf{Q}}_\ell, \omega),
\end{aligned}$$ viewed as a graded $\bar{\mathbf{Q}}_\ell[F]$-module. Borel--Moore homology is functorial in the following senses:

1.  If $f : Y \to X$ is proper, then it induces a pushforward $$\begin{aligned}
    f_\ast : \ur{H}_{-\ast}^{!, G}(Y) \to \ur{H}_{-\ast}^{!, G}(X)
    \end{aligned}$$ via the composition $f_\ast \omega_{Y/G} \xrightarrow{\sim} f_! f^! \omega_{X/G} \to \omega_{X/G}$.

2.  If $f : Y \to X$ is smooth of relative dimension $d$, then it induces a pullback $$\begin{aligned}
    f^\ast : \ur{H}_{-\ast}^{!, G}(X) \to \ur{H}_{-\ast}^{!, G}(Y)\langle -2d\rangle
    \end{aligned}$$ via the composition $\omega_{X/G} \to f_\ast f^\ast \omega_{X/G}  \xrightarrow{\sim} f_\ast \omega_{Y/G}\langle -2d\rangle$. If $f$ is an affine-space bundle, then $f^\ast$ is a shifted isomorphism.

3.  If $i : Z \to X$ is a closed immersion with complement $j : U \to X$, then it induces a long exact sequence $$\begin{aligned}
    \label{eq:long-exact}
    \cdots \to \ur{H}_i^{!, G}(Z) \to \ur{H}_i^{!, G}(X) \to \ur{H}_i^{!, G}(U) \to \ur{H}_{i - 1}^{!, G}(Z) \to \cdots
    \end{aligned}$$ via the exact triangle $i_!i^! \to \id \to j_\ast j^\ast \to i_!i^![1]$.

4.  If we have a cartesian square $$\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
    \matrix(m)[matrix of math nodes, row sep=2em, column sep=2.5em, text height=2ex, text depth=0.5ex]
    {   Y
            &Y'\\
        X
            &X'\\
            };
    \path[->,font=\scriptsize, auto]
    (m-1-1)     edge node{$f_Y$} (m-1-2)
    (m-1-1)     edge node[left]{$g$} (m-2-1)
    (m-1-2)     edge node{$g'$} (m-2-2)
    (m-2-1)     edge node{$f$} (m-2-2);
    \end{tikzpicture}$$ in which $[X/G], [X'/G]$ are smooth of respective dimensions $d, d'$, then $f$ induces a **pullback with restricted support** $$\begin{aligned}
    f_Y^\ast : \ur{H}_{-\ast}^{!, G}(Y') \to \ur{H}_{-\ast}^{!, G}(Y)\langle 2(d' - d)\rangle
    \end{aligned}$$ via the composition $$\begin{aligned}
    \omega_{Y'/G}\langle -2d'\rangle \xrightarrow{\sim} {g'}^! \bar{\mathbf{Q}}_\ell\to f_{Y, \ast} g^! f^\ast \bar{\mathbf{Q}}_\ell\xrightarrow{\sim} f_{Y, \ast} \omega_{Y/G}\langle -2d\rangle.
    \end{aligned}$$ Here, we use proper base change [@lo_2008 §5] to identify ${g'}^! f_\ast \simeq f_{Y, \ast} g^!$.

## 

We can express $\SHom$-spaces between pushforward sheaves, like $\bb{A}_\cal{S}$ and $\bb{A}_\cal{G}$, in terms of the Borel--Moore homology of associated schemes.

::: lem
[]{#lem:borel-moore label="lem:borel-moore"} If we have a cartesian square of $G$-varieties $$\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2em, column sep=2.5em, text height=2ex, text depth=0.5ex]
{   \tilde{Y}
        &\tilde{X}\\
    Y
        &X\\
        };
\path[->,font=\scriptsize, auto]
(m-1-1)     edge node{$\tilde{f}$} (m-1-2)
(m-1-1)     edge node[left]{$p_Y$} (m-2-1)
(m-1-2)     edge node{$p$} (m-2-2)
(m-2-1)     edge node{$f$} (m-2-2);
\end{tikzpicture}$$ in which $[\tilde{X}/G]$ is smooth of dimension $\tilde{d}$, then $$\begin{aligned}
\label{eq:borel-moore}
\SHom^\ast(f_! \bar{\mathbf{Q}}_\ell, p_\ast \bar{\mathbf{Q}}_\ell)
\simeq \ur{H}_{-\ast}^{!, G}(\tilde{Y})\langle -2\tilde{d}\rangle.
\end{aligned}$$ In particular, if $p$ is proper and $K = p_\ast \bar{\mathbf{Q}}_\ell$, then $$\begin{aligned}
\bb{A}_K^n \simeq \gr_{n - 2\tilde{d}}^{\bm{w}} \ur{H}_{-(n - 2\tilde{d})}^{!, G}(\tilde{X} \times_X \tilde{X})
\end{aligned}$$ for all $n$, and $\ur{H}_{-\ast}^{!, G}(\tilde{Y})$ forms a left graded $\bb{A}_K$-module.
:::

::: proof
*Proof.* By proper base change, $$\begin{aligned}
\begin{split}
f^! p_\ast \bar{\mathbf{Q}}_\ell
&\simeq p_{Y, \ast} \tilde{f}^! \bar{\mathbf{Q}}_\ell
\simeq p_{Y, \ast} \tilde{f}^! \omega_{\tilde{X}/G} \langle -2\tilde{d}\rangle 
\simeq p_{Y, \ast} \omega_{\tilde{Y}/G} \langle -2\tilde{d}\rangle,
\end{split}
\end{aligned}$$ giving $\SHom(f_! \bar{\mathbf{Q}}_\ell, p_\ast \bar{\mathbf{Q}}_\ell) \simeq f_\ast \SHom(\bar{\mathbf{Q}}_\ell, f^! p_\ast \bar{\mathbf{Q}}_\ell) \simeq f_\ast p_{Y, \ast} \SHom(\bar{\mathbf{Q}}_\ell, \omega_{\tilde{Y}/G})\langle -2\tilde{d}\rangle$. ◻
:::

## 

In the notation of Section [\[sec:hecke\]](#sec:hecke){reference-type="ref" reference="sec:hecke"}, let $$\begin{aligned}
\cal{Z}_0 &= \tilde{\cal{U}}_0 \times_{\cal{U}_0} \tilde{\cal{U}}_0,\\
\cal{Z}'_0 &= \tilde{G}_0 \times_{G_0} \tilde{G}_0.
\end{aligned}$$ In the literature, the underlying reduced scheme of $\cal{Z}$ is called the **Steinberg variety**, since it was introduced in [@steinberg_1976]. Lemma [\[lem:borel-moore\]](#lem:borel-moore){reference-type="ref" reference="lem:borel-moore"} implies that $$\begin{aligned}
\label{eq:z}
\bb{A}_\cal{S}^n &\simeq \gr_{n + 2r}^{\bm{w}} \ur{H}_{-(n + 2r)}^{!, G}(\cal{Z}) \pa{\simeq \ur{H}_{-(n + 2r)}^{!, G}(\cal{Z})},\\
\label{eq:z-prime}
\bb{A}_\cal{G}^n &\simeq \gr_n^{\bm{w}} \ur{H}_{-n}^{!, G}(\cal{Z}').
\end{aligned}$$ It remains to compare the Borel--Moore homologies of $\cal{Z}$ and $\cal{Z}'$.

Let us outline the strategy. We will lift the Bruhat strata of $\cal{B} \times \cal{B}$ to strata $\cal{Z}_w \subseteq \cal{Z}$ and $\cal{Z}'_w \subseteq \cal{Z}'$. To compare the Borel--Moore homologies of $\cal{Z}_w$ and $\cal{Z}'_w$, we will further replace these strata with affine-space bundles $\cal{Y}_w$ and $\cal{Y}'_w$ such that there is an explicit map $\cal{Y}_w \times T \to \cal{Y}'_w$, where $T$ is a maximal torus of $G$. Finally, we will use the long exact sequence [\[eq:long-exact\]](#eq:long-exact){reference-type="eqref" reference="eq:long-exact"} to patch the stratum-wise comparisons together.

## 

Let $\tilde{i} : \tilde{\cal{U}}_0 \to \tilde{G}_0$ be the lift of the inclusion $i : \cal{U}_0 \to G_0$. Let $\tilde{p}_1, \tilde{p}_2 :\cal{Z}_0 \to \tilde{\cal{U}}_0$ be the two projection maps, and let $\tilde{p}'_1, \tilde{p}'_2 : \cal{Z}'_0 \to \tilde{G}_0$ be defined similarly. Below, we will continually refer to the commutative diagram: $$\label{eq:tilde}
\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2em, column sep=2.5em, text height=2ex, text depth=0.5ex]
{   \cal{Z}_0
        &\cal{Z}'_0\\
    \tilde{\cal{U}}_0
        &\tilde{G}_0\\
    \cal{U}_0
        &G_0\\
        };
\path[->,font=\scriptsize, auto]
(m-1-1)     edge node{$i_\cal{Z}$} (m-1-2)
(m-1-1)     edge node[left]{$\tilde{p}_j$} (m-2-1)
(m-1-2)     edge node{$\tilde{p}'_j$} (m-2-2)
(m-2-1)     edge node{$\tilde{i}$} (m-2-2)
(m-2-1)     edge node[left]{$p$} (m-3-1)
(m-2-2)     edge node{$p'$} (m-3-2)
(m-3-1)     edge node{$i$} (m-3-2);
\end{tikzpicture}$$ Note that both squares in the diagram are cartesian.

::: lem
We have a commutative diagram $$\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2em, column sep=2.5em, text height=2ex, text depth=0.5ex]
{   \bb{A}_\cal{G}^n
        &\bb{A}_\cal{S}^n\\
    \gr_n^{\bm{w}} \ur{H}_{-n}^{!, G}(\cal{Z}')
        &\ur{H}_{-(n + 2r)}^{!, G}(\cal{Z})\\
        };
\path[->,font=\scriptsize, auto]
(m-1-1)     edge node{$i^\ast$} (m-1-2)
(m-1-1)     edge node[rotate=90,above]{$\sim$} (m-2-1)
(m-1-2)     edge node[rotate=90,below]{$\sim$} (m-2-2)
(m-2-1)     edge node{$i_\cal{Z}^\ast$} (m-2-2);
\end{tikzpicture}$$ where $i^\ast$ is defined by [\[eq:pullback\]](#eq:pullback){reference-type="eqref" reference="eq:pullback"}, the vertical isomorphisms are [\[eq:z\]](#eq:z){reference-type="eqref" reference="eq:z"} and [\[eq:z-prime\]](#eq:z-prime){reference-type="eqref" reference="eq:z-prime"}, and $i_\cal{Z}^\ast$ is the pullback with restricted support induced by $\tilde{i}$ via the top square of [\[eq:tilde\]](#eq:tilde){reference-type="eqref" reference="eq:tilde"}.
:::

::: proof
*Proof.* The morphism $i_\cal{Z}^\ast$ is induced by the morphism $$\begin{aligned}
(\tilde{p}')_1^! \to (\tilde{p}')_1^! \tilde{i}_\ast \tilde{i}^\ast
\xrightarrow{\sim} i_{\cal{Z}, \ast} {\tilde{p}}_1^! \tilde{i}^\ast,
\end{aligned}$$ while the morphism $i^\ast$ is induced by the composition $$\begin{aligned}
\begin{split}
\tilde{p}'_{2, \ast} (\tilde{p}')_1^! 
&\xrightarrow{\sim} {p'}^! p'_\ast \\
&\to {p'}^! i_\ast i^\ast p'_\ast\\
&\xrightarrow{\sim} \tilde{i}_\ast p^! p_! \tilde{i}^\ast\\
&\xrightarrow{\sim} \tilde{i}_\ast \tilde{p}_{2, !} \tilde{p}_1^! i^\ast\\
&\xrightarrow{\sim} \tilde{p}'_{2, \ast} i_{\cal{Z}, \ast} \tilde{p}_1^! i^\ast.
\end{split}
\end{aligned}$$ By further diagram-chasing, the latter is obtained by applying $\tilde{p}'_{2, \ast}$ to the former. ◻
:::

To analyze $i_\cal{Z}^\ast$, we decompose $\cal{Z}_0$ and $\cal{Z}'_0$ into strata. For each $w \in W$, we define subschemes $\cal{Z}_{w, 0} \subseteq \cal{Z}_0$ and $\cal{Z}'_{w, 0} \subseteq \cal{Z}'_0$ by stipulating that both squares in the commutative diagram below are cartesian: $$\label{eq:z-w}
\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2em, column sep=2.5em, text height=2ex, text depth=0.5ex]
{   \cal{Z}_{w, 0}
        &\cal{Z}'_{w, 0}
        &O_{w, 0}\\
    \cal{Z}_0
        &\cal{Z}'_0
        &\cal{B}_0 \times \cal{B}_0\\
        };
\path[->,font=\scriptsize, auto]
(m-1-1)     edge node{$i_{\cal{Z}, w}$} (m-1-2)
(m-1-1)     edge (m-2-1)
(m-1-2)     edge (m-1-3)
(m-1-2)     edge (m-2-2)
(m-2-1)     edge node{$i_\cal{Z}$} (m-2-2)
(m-2-2)     edge (m-2-3)
(m-1-3)     edge node{$j_w$} (m-2-3);
\end{tikzpicture}$$ Here, the map $\cal{Z}'_0 \to \cal{B}_0 \times \cal{B}_0$ is induced by the map $\cal{Z}'_0 \xrightarrow{\tilde{p}'_1 \times \tilde{p}'_2} \tilde{G}_0 \times \tilde{G}_0$.

To analyze $i_{\cal{Z}, w} : \cal{Z}_{w, 0} \to \cal{Z}'_{w, 0}$, we rewrite these strata in a way that expresses their structure as fiber bundles over $O_{w, 0}$. Choose a split maximal torus $T_0 \subseteq G_0$. Choose a Borel $B_0 \supseteq T_0$ with unipotent radical $U_0 \subseteq B_0$, so that $B_0 \simeq T_0 \ltimes U_0$. Let $N_0$ be the normalizer of $T_0$ in $G_0$. For each $w \in W$, fix a lift $\dot{w} \in N_0$. Then $\dot{w}B_0 \dot{w}^{-1}$ contains $\dot{w}T_0 \dot{w}^{-1} = T_0$ and only depends on $w$. If we write $$\begin{aligned}
B_{w, 0} &= B_0 \cap \dot{w}B_0 \dot{w}^{-1},\\
U_{w, 0} &= U_0 \cap \dot{w}U_0 \dot{w}^{-1},
\end{aligned}$$ then $B_{w, 0} \simeq T_0 \ltimes U_{w, 0}$. In what follows, let $B_{w, 0}$ act on $G_0$ by right multiplication and on $U_{w, 0}$ and itself by right conjugation.

::: lem
[]{#lem:assoc-bundle label="lem:assoc-bundle"} We have a commutative diagram $$\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2em, column sep=1.5em, text height=2ex, text depth=0.5ex]
{   (G_0 \times U_{w, 0})/B_{w, 0}
        &(G_0 \times B_{w, 0})/B_{w, 0}
        &G_0/B_{w, 0}\\
    \cal{Z}_{w, 0}
        &\cal{Z}'_{w, 0}
        &O_{w, 0}\\
        };
\path[->,font=\scriptsize, auto]
(m-1-1)     edge (m-1-2)
(m-1-2)     edge (m-1-3)
(m-1-1)     edge node[rotate=90,above]{$\sim$} (m-2-1)
(m-1-2)     edge node[rotate=90,below]{$\sim$} (m-2-2)
(m-1-3)     edge node[rotate=90,below]{$\sim$} (m-2-3)
(m-2-1)     edge node{$i_{\cal{Z}, w}$} (m-2-2)
(m-2-2)     edge (m-2-3);
\end{tikzpicture}$$ where the middle vertical map sends $[g, b] \mapsto [gbg^{-1}, gBg^{-1}, g\dot{w}B\dot{w}^{-1}g^{-1}]$.
:::

::: rem
The vertical isomorphisms respectively transport the $G$-actions on $\cal{Z}_w$, $\cal{Z}'_w$, $O_w$ to the $G$-actions on $(G \times U_w)/B_w$, $(G \times B_w)/B_w$, $G/B_w$ given by left multiplication on the factor of $G$.
:::

::: proof
*Proof.* The $w = 1$ case, entailing isomorphisms $(G \times U)/B \simeq \tilde{\cal{U}}$ and $(G \times B)/B \simeq \tilde{G}$, is explained in [@slodowy Ch. 4], and the general case is similar. ◻
:::

Again, let $T_0$ act on $G_0$ by right multiplication and on $U_{w, 0}$ and $B_{w, 0}$ by right conjugation. Let $\cal{Y}_{w, 0}$ and $\cal{Y}'_{w, 0}$ be defined by the cartesian squares: $$\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2em, column sep=2.5em, text height=2ex, text depth=0.5ex]
{   \cal{Y}_{w, 0}
        &(G_0 \times U_{w, 0})/T_0\\
    \cal{Z}_{w, 0}
        &(G_0 \times U_{w, 0})/B_{w, 0}\\
        };
\path[->,font=\scriptsize, auto]
(m-1-1)     edge node{$\sim$} (m-1-2)
(m-1-1)     edge (m-2-1)
(m-1-2)     edge (m-2-2)
(m-2-1)     edge node{$\sim$} (m-2-2);
\end{tikzpicture}
\qquad
\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2em, column sep=2.5em, text height=2ex, text depth=0.5ex]
{   \cal{Y}'_{w, 0}
        &(G_0 \times B_{w, 0})/T_0\\
    \cal{Z}'_{w, 0}
        &(G_0 \times B_{w, 0})/B_{w, 0}\\
        };
\path[->,font=\scriptsize, auto]
(m-1-1)     edge node{$\sim$} (m-1-2)
(m-1-1)     edge (m-2-1)
(m-1-2)     edge (m-2-2)
(m-2-1)     edge node{$\sim$} (m-2-2);
\end{tikzpicture}$$ Let $i_{\cal{Y}, w} : \cal{Y}_{w, 0} \to \cal{Y}'_{w, 0}$ be the pullback of $i_{\cal{Z}, w} : \cal{Z}_{w, 0} \to \cal{Z}'_{w, 0}$. The advantage of $i_{\cal{Y}, w}$ over $i_{\cal{Z}, w}$ is that the former can be factored as $$\begin{aligned}
\cal{Y}_{w, 0} \xrightarrow{\sim} \cal{Y}_{w, 0} \times \{1\}
\to 
\cal{Y}_{w, 0} \times T_0 \xrightarrow{\sim} \cal{Y}'_{w, 0}.
\end{aligned}$$ If we let $G_0$ act trivially on $T_0$, then these maps are all $G_0$-equivariant.

## 

In what follows, if $M = \bigoplus_n M^n$ is a $\bb{Z}$-graded $\bar{\mathbf{Q}}_\ell[F]$-module, then we write $$\begin{aligned}
\begin{split}
M^\dagger 
&\simeq \bigoplus_n {\gr_n^{\bm{w}} M^n}.
\end{split}
\end{aligned}$$ Let $i_{\cal{Z}, w}^\ast : \ur{H}_{-\ast}^{!, G}(\cal{Z}'_w) \to \ur{H}_{-\ast}^{!, G}(\cal{Z}_w)\langle 2r\rangle$ be the pullback with restricted support induced by $\tilde{i}$ via the top square of [\[eq:tilde\]](#eq:tilde){reference-type="eqref" reference="eq:tilde"} and the left square of [\[eq:z-w\]](#eq:z-w){reference-type="eqref" reference="eq:z-w"}, and let $$\begin{aligned}
i_{\cal{Z}, w}^\dagger : \ur{H}_{-\ast}^{!, G}(\cal{Z}'_w)^\dagger \to \ur{H}_{-\ast}^{!, G}(\cal{Z}_w)\langle 2r\rangle
\end{aligned}$$ be its restriction to $\ur{H}_{-\ast}^{!, G}(\cal{Z}'_w)^\dagger$. Let $i_{\cal{Y}, w}^\dagger$, $i_{\cal{Y}, w}^\dagger$ be defined similarly.

::: lem
The map $i_{\cal{Y}, w}^\dagger$ is an isomorphism.
:::

::: proof
*Proof.* Writing $N_w = \dim U_w$, we have $$\begin{aligned}
\ur{H}_{-\ast}^{!, G}(\cal{Y}_w)
\simeq \ur{H}_{-\ast}^{!, G}(G/T)\langle 2N_w\rangle
\simeq \ur{H}_{-\ast}^{!, T}(\mathit{pt})\langle 2N_w\rangle.
\end{aligned}$$ By Poincaré duality, $\ur{H}_{-i}^{!, T}(\mathit{pt}) \simeq \ur{H}_{!, T}^{-i}(\mathit{pt}) \simeq \ur{H}_T^{i - 2r}(\mathit{pt})$, where $\ur{H}_{!, T}^\ast$ denotes $T$-equivariant, compactly-supported cohomology. So Frobenius acts on $\ur{H}_{-i}^{!, T}(\mathit{pt})$ by $q^{\frac{i}{2} - r}$, which means it is concentrated in weight $i - 2r$.

Again by Poincaré duality, $\ur{H}_{-j}^!(T) \simeq \ur{H}_!^{-j}(T)^\vee \simeq \ur{H}^{j + 2r}(T)$, where $\ur{H}_\ast^!$, *resp.* $\ur{H}_!^\ast$, denotes non-equivariant Borel--Moore homology, *resp.* compactly-supported cohomology. So Frobenius acts on $\ur{H}_{-j}^!(T)$ by $q^{j + 2r}$, which means it is concentrated in weight $2j + 4r$.

Altogether, the Künneth isomorphism $$\begin{aligned}
\ur{H}_{-n}^{!, G}(\cal{Y}'_w) \xrightarrow{\sim} \bigoplus_{i + j = n} \ur{H}_{-i}^{!, G}(\cal{Y}_w) \otimes \ur{H}_{-j}^!(T)
\end{aligned}$$ restricts to an isomorphism $$\begin{aligned}
\ur{H}_{-n}^{!, G}(\cal{Y}'_w)^\dagger \xrightarrow{\sim} \ur{H}_{-(n + 2r)}^{!, G}(\cal{Y}_w) \otimes H_{2r}^!(T).
\end{aligned}$$ But $i_{\cal{Y}, w}^\ast$ is the composition of the Künneth isomorphism with $$\begin{aligned}
\begin{split}
\ur{H}_{-\ast}^{!, G}(\cal{Y}_w) \otimes \ur{H}_{-\ast}^!(T) 
    &\to \ur{H}_{-\ast}^{!, G}(\cal{Y}_w) \otimes \ur{H}_{2r}^!(T)\\    
    &\xrightarrow{\sim} \ur{H}_{-\ast}^{!, G}(\cal{Y}_w) \otimes \ur{H}_0^!(\mathit{pt})\langle 2r\rangle\\
    &\xrightarrow{\sim} \ur{H}_{-\ast}^{!, G}(\cal{Y}_w)\langle 2r\rangle,
\end{split}
\end{aligned}$$ so we win. ◻
:::

::: lem
[]{#lem:i-z-pur label="lem:i-z-pur"} The map $i_{\cal{Z}, w}^\dagger$ is an isomorphism.
:::

::: proof
*Proof.* The maps $\cal{Y}_{w, 0} \to \cal{Z}_{w, 0}$ and $\cal{Y}'_{w, 0} \to \cal{Z}'_{w, 0}$ define affine-space bundles of rank $N_w$, so they induce pullback isomorphisms $$\begin{aligned}
\ur{H}_{-\ast}^{!, G}(\cal{Z}_w) &\xrightarrow{\sim} \ur{H}_{-\ast}^{!, G}(\cal{Y}_w)\langle -2N_w\rangle,\\
\ur{H}_{-\ast}^{!, G}(\cal{Z}'_w) &\xrightarrow{\sim} \ur{H}_{-\ast}^{!, G}(\cal{Y}'_w)\langle -2N_w\rangle
\end{aligned}$$ that preserve weights. Now we are done by the previous lemma. ◻
:::

::: proof
*Proof of Theorem [\[thm:pure-iso\]](#thm:pure-iso){reference-type="ref" reference="thm:pure-iso"}.* Fix a total order $\preceq$ on $W$ in which $w_1 \preceq w_2$ implies $|w_1| \leq |w_2|$, where $|{-}|$ denotes Bruhat length. Such a total order is necessarily a refinement of the Bruhat partial order. For any $w \in W$, let $$\begin{aligned}
\cal{Z}_{\preceq w, 0} 
&= \coprod_{x \preceq w} \cal{Z}_{x, 0} \subseteq \cal{Z}_0,\\
\cal{Z}_{\prec w, 0} 
&= \coprod_{x \prec w} \cal{Z}_{x, 0} \subseteq \cal{Z}_0.
\end{aligned}$$ Then $\cal{Z}_{w, 0} \to \cal{Z}_{\preceq w, 0}$ is a closed immersion with complement $\cal{Z}_{\prec w, 0} \to \cal{Z}_{\preceq w, 0}$. Let $\cal{Z}'_{\preceq w, 0}, \cal{Z}'_{\prec w, 0}$ be defined similarly. The map $i_\cal{Z} : \cal{Z}_0 \to \cal{Z}'_0$ gives rise to the following commutative diagram whose rows are long exact sequences and whose vertical arrows are pullbacks with restricted support: $$\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2.5em, column sep=1.5em, text height=2ex, text depth=0.5ex]
{   \cdots 
        &\ur{H}_n^{!, G}(\cal{Z}'_w)
        &\ur{H}_n^{!, G}(\cal{Z}'_{\preceq w})
        &\ur{H}_n^{!, G}(\cal{Z}'_{\prec w})
        &\cdots\\
    \cdots 
        &\ur{H}_n^{!, G}(\cal{Z}_w)\langle 2r\rangle
        &\ur{H}_n^{!, G}(\cal{Z}_{\preceq w})\langle 2r\rangle
        &\ur{H}_n^{!, G}(\cal{Z}_{\prec w})\langle 2r\rangle
        &\cdots\\
        };
\path[->,font=\scriptsize, auto]
(m-1-1)     edge (m-1-2)
(m-1-2)     edge (m-1-3)
(m-1-3)     edge (m-1-4)
(m-1-4)     edge (m-1-5)
(m-2-1)     edge (m-2-2)
(m-2-2)     edge (m-2-3)
(m-2-3)     edge (m-2-4)
(m-2-4)     edge (m-2-5)
(m-1-2)     edge node[left]{$i_{\cal{Z}, w}^\ast$} (m-2-2)
(m-1-3)     edge node{$i_{\cal{Z}, \preceq w}^\ast$} (m-2-3)
(m-1-4)     edge node{$i_{\cal{Z}, \prec w}^\ast$} (m-2-4);
\end{tikzpicture}$$ Since $(-)^\dagger$ is exact, we obtain another commutative diagram $$\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2.5em, column sep=1.5em, text height=2ex, text depth=0.5ex]
{   \cdots 
        &\ur{H}_n^{!, G}(\cal{Z}'_w)^\dagger
        &\ur{H}_n^{!, G}(\cal{Z}'_{\preceq w})^\dagger
        &\ur{H}_n^{!, G}(\cal{Z}'_{\prec w})^\dagger
        &\cdots\\
    \cdots 
        &\ur{H}_n^{!, G}(\cal{Z}_w)\langle 2r\rangle
        &\ur{H}_n^{!, G}(\cal{Z}_{\preceq w})\langle 2r\rangle
        &\ur{H}_n^{!, G}(\cal{Z}_{\prec w})\langle 2r\rangle
        &\cdots\\
        };
\path[->,font=\scriptsize, auto]
(m-1-1)     edge (m-1-2)
(m-1-2)     edge (m-1-3)
(m-1-3)     edge (m-1-4)
(m-1-4)     edge (m-1-5)
(m-2-1)     edge (m-2-2)
(m-2-2)     edge (m-2-3)
(m-2-3)     edge (m-2-4)
(m-2-4)     edge (m-2-5)
(m-1-2)     edge node[left]{$i_{\cal{Z}, w}^\dagger$} (m-2-2)
(m-1-3)     edge node{$i_{\cal{Z}, \preceq w}^\dagger$} (m-2-3)
(m-1-4)     edge node{$i_{\cal{Z}, \prec w}^\dagger$} (m-2-4);
\end{tikzpicture}$$ in which the top row remains exact.

We induct along $\preceq$. If $w = 1$, then $i_{\cal{Z}, \prec w}^\dagger = i_{\cal{Z}, w}^\dagger$. By Lemma [\[lem:i-z-pur\]](#lem:i-z-pur){reference-type="ref" reference="lem:i-z-pur"}, the latter is an isomorphism in every homological degree $n$. Now let $w$ be arbitrary. If $x$ is the immediate predecessor of $w$ in the total order $\preceq$, then $\cal{Z}_{\prec w} = \cal{Z}_{\preceq x}$ and $i_{\cal{Z}, \prec w}^\dagger = i_{\cal{Z}, \preceq x}^\dagger$. Lemma [\[lem:i-z-pur\]](#lem:i-z-pur){reference-type="ref" reference="lem:i-z-pur"} and the inductive hypothesis respectively imply that $i_{\cal{Z}, w}^\dagger$ and $i_{\cal{Z}, \prec w}^\dagger$ are isomorphisms in every degree. So, by the five lemma, $i_{\cal{Z}, \preceq w}^\dagger$ is an isomorphism in every degree as well, completing the induction. ◻
:::
