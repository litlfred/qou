---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-006-6-khovanovrozansky-homology
section_title: "Khovanov–Rozansky Homology"
section_number: 6
pages: 41-45
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.957
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the Weyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
[]{#sec:kr label="sec:kr"}

## 

A link in a $3$-manifold is the image of a disjoint union of finitely many circles under a smooth embedding. The HOMFLY series of a link in $S^3$ is a bivariate Laurent series that only depends on its isotopy class [@homfly].

Dunfield--Gukov--Rasmussen predicted [@dgr], and Khovanov--Rozansky constructed [@kr], a categorification of the HOMFLY series, sending a link in $3$-space to a triply-graded vector space over $\bb{Q}$. This isotopy invariant is now known as **HOMFLY** or **Khovanov--Rozansky homology**. The original construction used the homotopy theory of matrix factorizations. In [@khovanov], Khovanov gave an alternative approach via the Hochschild homology of Soergel bimodules for the groups $W = S_n$. Via Soergel's Erweiterungssatz [@soergel Thms. 15-17], the output of his construction (after base change from $\bb{Q}$ to $\bar{\mathbf{Q}}_\ell$) is equivalent to a functor $$\begin{aligned}
\sf{HHH} : \sf{H}_W \to \sf{K}^b(\mathsf{Vect}_2) \subseteq \mathsf{Vect}_3,
\end{aligned}$$ where $\mathsf{Vect}_d$ denotes the category of $\bb{Z}^d$-graded $\bar{\mathbf{Q}}_\ell$-vector spaces. Khovanov's construction extends to Soergel bimodules for any Coxeter group, so in particular, $\sf{HHH}$ can be defined on the Hecke category of any such group.

::: rem
[]{#rem:dgr label="rem:dgr"} To dispel any ambiguity from our conventions, we state explicitly: If $\beta$ is a topological braid on $n = r + 1$ strands, and $\hat{\beta}$ is the link closure of $\beta$, then $$\begin{aligned}
\bb{P}(\beta) = {(at)^{|\beta|}} a^{-r} \sum_{i, j, k} 
{(a^2 \bm{q}^{\frac{1}{2}} t)^{r - i}} \bm{q}^{\frac{j}{2}} t^k
\dim \sf{HHH}^{i, i + j, k}(\cal{R}(\beta))
\end{aligned}$$ is an isotopy invariant of $\hat{\beta}$ that equals $1$ when $\hat{\beta}$ is the unknot. It matches the invariant in [@dgr] once we substitute $\bm{q}^{\frac{1}{2}} = q$. In particular, for $\beta = \bb{1}$, we have $$\begin{aligned}
\bb{P}(\bb{1}) = \pa{\frac{\bm{q}^{\frac{1}{2}}}{a} \pa{\frac{1 + a^2 t}{1 - \bm{q}}}}^r.
\end{aligned}$$ Compare to Example [\[ex:identity\]](#ex:identity){reference-type="ref" reference="ex:identity"}, below.
:::

## 

In [@ww_2008], Webster--Williamson interpreted the Hochschild homology of a Soergel bimodule as the hypercohomology of a sum of shifted pure perverse sheaves over $G$. In subsequent papers [@ww_2011; @ww_2017], they showed how to interpret $\sf{HHH}^{\ast, \ast, \ast}$ in a similar way, except in terms of a *complex* of such objects. We will rewrite their work in our notation.

For any $G_0$-variety $X_0$ over $\bb{F}$, we write $$\begin{aligned}
\bb{H}_G^\ast(X, -) \vcentcolon= \SHom^\ast(\bar{\mathbf{Q}}_\ell, -) : \underline{\sf{D}}_{G, m}^b(X_0) \to \mathsf{Mod}_1(\bar{\mathbf{Q}}_\ell[F]),
\end{aligned}$$ where $\bar{\mathbf{Q}}_\ell[F]$ is concentrated in degree zero. In other words, $\bb{H}_G^\ast(X, K)$ is the hypercohomology of $\xi K \in \underline{\sf{D}}_G^b(G)$, implicitly endowed with the Frobenius action coming from $K$. With this notation, the theorem below summarizes the main results of [@ww_2008] and [@ww_2017].

::: thm
[]{#thm:ww label="thm:ww"} We have $$\begin{aligned}
\begin{split}
\sf{HHH}^{i, i + j, k}
\simeq 
    \ur{H}^k \circ \sf{K}^b(\gr_{i + j}^{\bm{w}} \bb{H}_G^j(G, (\kappa \circ \sf{CH})(-)))
\end{split}
\end{aligned}$$ for all $i, j, k \in \bb{Z}$. In particular, we have $$\begin{aligned}
\sf{HHH}^{i, i + j, k}(\mathit{IC}_{w, 0}[-n]_\triangle)
&\simeq \left\{\begin{array}{ll}
\gr_{i + j}^{\bm{w}} \bb{H}_G^j(G, \sf{CH}(\mathit{IC}_w)) &k = n\\
0   &k \neq n
\end{array}\right.
\end{aligned}$$ for all $w \in W$ and $n \in \bb{Z}$.
:::

::: ex
[]{#ex:identity label="ex:identity"} Below, we review the calculation of $\sf{HHH}(\mathit{IC}_1) \simeq \gr_\ast^{\bm{w}} \bb{H}_G^\ast(G, \cal{G})$. Since $\cal{G}$ is the pushforward of the constant sheaf on the Grothendieck--Springer resolution, it suffices to calculate the $G$-equivariant cohomology of $\tilde{G}$ together with its weight filtration.

Fix a maximal torus $T_0 \subseteq G_0$ and a Borel $B_0 \supseteq T_0$. By Lemma [\[lem:assoc-bundle\]](#lem:assoc-bundle){reference-type="ref" reference="lem:assoc-bundle"}, $[\tilde{G}_0/G_0] \simeq [B_0/B_0]$, where $B_0$ acts on itself by conjugation. Therefore, there are weight-preserving isomorphisms $$\begin{aligned}
\begin{split}
\bb{H}_G^j(G, \cal{G}) 
&\simeq \ur{H}_B^j(B, \bar{\mathbf{Q}}_\ell) \\
&\simeq \ur{H}_T^j(T, \bar{\mathbf{Q}}_\ell) \\
&\simeq \bigoplus_i {\ur{H}_T^{j - i}(\mathit{pt}, \bar{\mathbf{Q}}_\ell) \otimes \ur{H}^i(T, \bar{\mathbf{Q}}_\ell)}.
\end{split}
\end{aligned}$$ Above, Frobenius acts by $q^{\frac{j - i}{2}}$ on $\ur{H}_T^{j - i}(\mathit{pt})$ and by $q^i$ on $\ur{H}^i(T)$, so it acts by $q^{\frac{i + j}{2}}$ on the $i$th summand of the last expression. We deduce that $$\begin{aligned}
\gr_{i + j}^{\bm{w}} \bb{H}_G^j(G, \cal{G}) \simeq \ur{H}_T^{j - i}(\mathit{pt}, \bar{\mathbf{Q}}_\ell) \otimes \ur{H}^i(T, \bar{\mathbf{Q}}_\ell).
\end{aligned}$$ The proof of [@ww_2011 Prop. 11] shows that this isomorphism is $W$-equivariant with respect to:

1.  The $W$-action on the left-hand side induced by $\bar{\mathbf{Q}}_\ell[W] \subseteq \bb{A}_W \simeq \bb{A}_\cal{G}$, *i.e.*, the Springer action arising from the monodromy of $\cal{G}$ over the regular semisimple locus of $G$.

2.  The $W$-action on the right-hand side induced by $\ur{H}_T^{j - i}(\mathit{pt}, \bar{\mathbf{Q}}_\ell) \simeq \Sym^{\frac{j - i}{2}}(\bb{V})$ and $\ur{H}^i(T, \bar{\mathbf{Q}}_\ell) \simeq \mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V})$.
:::

## 

In the rest of this section, we prove Theorem [\[thm:a_w-to-kr\]](#thm:a_w-to-kr){reference-type="ref" reference="thm:a_w-to-kr"}, stating that Khovanov--Rozansky homology is a summand of the $\bb{A}_W$ trace.

In what follows, recall from Section [\[sec:hecke\]](#sec:hecke){reference-type="ref" reference="sec:hecke"} that for all $\phi \in \hat{W}$, we write $V_\phi$ for an irreducible representation of $W$ that affords the character $\phi$, endowed with the trivial action of Frobenius.

::: lem
[]{#lem:sheaves-to-reps label="lem:sheaves-to-reps"} Let $K \in \sf{C}_{\hat{W}}(G_0)$ be an indecomposable shifted perverse sheaf, and write $K = \cal{G}_\phi \otimes M$, where $\phi \in \hat{W}$ and $M$ is the pullback of a pure weight-zero object of $\sf{D}_{G, m}^b(\mathit{pt}_0)$. Then we have $W$-equivariant isomorphisms: $$\begin{aligned}
        \label{eq:covariant}        
        \gr_{i + j}^{\bm{w}} \bb{H}_G^j(G, K)
        &\simeq \Hom_W(V_\phi, {(\Sym^{\frac{j - i}{2}} \otimes {\mathop{\mathrm{\text{$\Lambda$}}}^i})}(\bb{V})) \otimes \xi M,\\[1ex]
        \label{eq:contravariant}
        \gr_0^{\bm{w}} \SHom^0(K, \cal{G}\langle i\rangle)
        &\simeq \Hom_W(V_\phi^\vee, \bar{\mathbf{Q}}_\ell[W] \otimes \Sym^{\frac{j}{2}}(\bb{V})) \otimes \xi M^\vee\\
        &\simeq 
            V_\phi \otimes \Sym^{\frac{i}{2}}(\bb{V}) \otimes \xi M^\vee.\nonumber
        
\end{aligned}$$ Moreover, these isomorphisms are functorial in $K$.
:::

::: proof
*Proof.* By Example [\[ex:identity\]](#ex:identity){reference-type="ref" reference="ex:identity"}, there is a $W$-equivariant isomorphism $$\begin{aligned}
\gr_{i + j}^{\bm{w}} \bb{H}_G^j(G, \cal{G}) 
    \simeq {(\Sym^{\frac{j - i}{2}} \otimes \mathop{\mathrm{\text{$\Lambda$}}}^i)}(\bb{V}),
\end{aligned}$$ which yields [\[eq:covariant\]](#eq:covariant){reference-type="eqref" reference="eq:covariant"}. Next, Theorems [\[thm:lusztig-algebra\]](#thm:lusztig-algebra){reference-type="ref" reference="thm:lusztig-algebra"} and [\[thm:pure-iso\]](#thm:pure-iso){reference-type="ref" reference="thm:pure-iso"} give a $W$-equivariant isomorphism $$\begin{aligned}
\gr_0^{\bm{w}} \SHom^0(\cal{G}, \cal{G}\langle i\rangle) \simeq \bar{\mathbf{Q}}_\ell[W] \otimes \Sym^{\frac{i}{2}}(\bb{V}),
\end{aligned}$$ which yields [\[eq:contravariant\]](#eq:contravariant){reference-type="eqref" reference="eq:contravariant"}. Functoriality is a consequence of the fact that $\bb{A}_\cal{G} \xrightarrow{\sim} \bb{A}_\cal{S} \xrightarrow{\sim} \bb{A}_W$ is an isomorphism of algebras, not just of vector spaces. ◻
:::

::: lem
[]{#lem:h-to-g label="lem:h-to-g"} We have $$\begin{aligned}
(\gr_{i + j}^{\bm{w}} \bb{H}_G^j(G, -))^\vee
\simeq \Hom_W(\mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V}), \gr_0^{\bm{w}} {\SHom^0(-, \cal{G}\langle j\rangle)})
\end{aligned}$$ as contravariant functors $\underline{\sf{C}}(G_0)^\op \to \sf{Vect}_0$.
:::

::: proof
*Proof.* By the preceding lemma and the self-duality of $\Sym^\ast(\bb{V})$ as a representation of $W$, the statement holds with $\underline{\sf{C}}_{\hat{W}}(G_0)$ in place of $\underline{\sf{C}}(G_0)$. Now apply Theorem [\[thm:summand\]](#thm:summand){reference-type="ref" reference="thm:summand"}, observing that the constant sheaf is a summand of $\cal{G}$. ◻
:::

::: lem
[]{#lem:g-to-s label="lem:g-to-s"} We have $$\begin{aligned}
\gr_0^{\bm{w}} {\SHom^0(-, \cal{G}\langle j\rangle)}
&\simeq \SHom^0(i^\ast(-)\langle-r\rangle, \cal{S}\langle j\rangle)
\end{aligned}$$ as contravariant functors $\underline{\sf{C}}(G_0)^\op \to \sf{Mod}_0(\bar{\mathbf{Q}}_\ell[W])$.
:::

::: proof
*Proof.* By Theorem [\[thm:pure-iso\]](#thm:pure-iso){reference-type="ref" reference="thm:pure-iso"}, the statement holds with $\underline{\sf{C}}_{\hat{W}}(G_0)$ in place of $\underline{\sf{C}}(G_0)$. Now apply Theorem [\[thm:summand\]](#thm:summand){reference-type="ref" reference="thm:summand"}, observing that $i^\ast\langle -r\rangle$ is compatible with the functors $\sf{PR}$. ◻
:::

::: proof
*Proof of Theorem [\[thm:a_w-to-kr\]](#thm:a_w-to-kr){reference-type="ref" reference="thm:a_w-to-kr"}.* The theorem claims that $$\begin{aligned}
(\sf{HHH}^{i, i + j, k})^\vee
&\simeq \Hom_W(\mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V}), \sf{AH}^{j + k, j}(-))
\end{aligned}$$ as contravariant functors on $\sf{H}_W = \sf{K}^b(\sf{C}(\cal{B}_0 \times \cal{B}_0))$. For ease of notation, let $$\begin{aligned}
\Phi^j &= \Hom_{\underline{\sf{C}}(G_0)}(i^\ast (-)\langle -r\rangle, \cal{S}\langle j\rangle),\\
\emph{resp.}\qquad
\Psi^{i, j} &= \Hom_{\sf{K}^b(\underline{\sf{C}}(G_0))}(i^\ast(-)\langle -r\rangle, \cal{S}\langle j\rangle [i - j]_\triangle),
\end{aligned}$$ as a functor $\underline{\sf{C}}(G_0) \to \sf{Mod}_0(\bar{\mathbf{Q}}_\ell[W])$, *resp.* $\sf{K}^b(\underline{\sf{C}}(G_0)) \to \sf{Mod}_0(\bar{\mathbf{Q}}_\ell[W])$. By Lemma [\[lem:pullback-kappa\]](#lem:pullback-kappa){reference-type="ref" reference="lem:pullback-kappa"}, we have $\kappa \circ i^\ast \langle -r\rangle \simeq i^\ast\langle -r\rangle \circ \kappa$ as functors on $\sf{C}(G_0)$, and therefore, $$\begin{aligned}
\sf{AH}^{j + k, j} 
&\simeq
    \Psi^{j + k, j} \circ \sf{K}^b(\kappa \circ \sf{CH}).
\end{aligned}$$ At the same time, we have $$\begin{aligned}
\Psi^{j + k, j}
&\simeq
    \ur{H}^k \circ \sf{K}^b\Phi^j.
\end{aligned}$$ Furthermore, by Lemmas [\[lem:unipotent\]](#lem:unipotent){reference-type="ref" reference="lem:unipotent"} and [\[lem:g-to-s\]](#lem:g-to-s){reference-type="ref" reference="lem:g-to-s"}, $$\begin{aligned}
\begin{split}
\Phi^j
&\simeq
    \SHom^0(i^\ast(-)\langle -r\rangle, \cal{S}\langle j\rangle)
\simeq
    \gr_0^{\bm{w}} \SHom^0(-, \cal{G}\langle j\rangle).
\end{split}
\end{aligned}$$ Combining these equivalences with Lemma [\[lem:h-to-g\]](#lem:h-to-g){reference-type="ref" reference="lem:h-to-g"}, we compute $$\begin{aligned}
\begin{split}
&\Hom_W(\mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V}), \sf{AH}^{j + k, j}(-))\\
&\simeq
    \Hom_W(\mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V}), \ur{H}^k \circ \sf{K}^b(\Phi^j \circ \kappa \circ \sf{CH}))
        \\
&\simeq
    \Hom_W(\mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V}), \ur{H}^k \circ \sf{K}^b(\gr_0^{\bm{w}} \SHom^0((\kappa \circ \sf{CH})(-), \cal{G}\langle j\rangle)))\\
&\simeq
    \ur{H}^k \circ \sf{K}^b(
    \Hom_W(\mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V}),\gr_0^{\bm{w}} \SHom^0((\kappa \circ \sf{CH})(-), \cal{G}\langle j\rangle)))\\
&\simeq
    \ur{H}^k \circ \sf{K}^b(
    (\gr_{i + j}^{\bm{w}} 
        \bb{H}_G^j(G, (\kappa \circ \sf{CH})(-))
    )^\vee).
\end{split}
\end{aligned}$$ The last expression is equivalent to $(\sf{HHH}^{i, i + j, k})^\vee$ by Theorem [\[thm:ww\]](#thm:ww){reference-type="ref" reference="thm:ww"}. ◻
:::

##  {#subsec:kr-to-varieties}

Let $\cal{X}(\beta)$ be defined by the cartesian square: $$\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2em, column sep=2.5em, text height=2ex, text depth=0.5ex]
{   \cal{X}(\beta)
        &\cal{U}(\beta)\\
    \{1\}
        &\cal{U}\\
        };
\path[->,font=\scriptsize, auto]
(m-1-1)     edge (m-1-2)
(m-1-1)     edge (m-2-1)
(m-1-2)     edge node{$p_\beta$} (m-2-2)
(m-2-1)     edge (m-2-2);
\end{tikzpicture}$$

::: proof
*Proof of Corollary [\[cor:kr-to-varieties\]](#cor:kr-to-varieties){reference-type="ref" reference="cor:kr-to-varieties"}.* We claim that for all $\beta \in \mathit{Br}_W^+$, we have $$\begin{aligned}
\sf{HHH}^{0, j, k}(\cal{R}(\beta))^\vee
    &\simeq \gr_{j + 2r}^{\bm{w}} \ur{H}_{-(j + k + 2r)}^{!, G}(\cal{U}(\beta)),\\
\sf{HHH}^{r, r + j, k}(\cal{R}(\beta))^\vee
    &\simeq \gr_{j + 2(r - N)}^{\bm{w}} \ur{H}_{-(j + k + 2(r - N))}^{!, G}(\cal{X}(\beta)).
\end{aligned}$$ Let $1$ and $\varepsilon$ be the trivial and sign characters of $W$, respectively. Then $1$, *resp.* $\varepsilon$, is the character of $\mathop{\mathrm{\text{$\Lambda$}}}^0(\bb{V})$, *resp.* $\mathop{\mathrm{\text{$\Lambda$}}}^r(\bb{V})$, so Theorems [\[thm:a_w-to-kr\]](#thm:a_w-to-kr){reference-type="ref" reference="thm:a_w-to-kr"} and [\[thm:a_w-to-varieties-strong\]](#thm:a_w-to-varieties-strong){reference-type="ref" reference="thm:a_w-to-varieties-strong"} give us $$\begin{aligned}
\sf{HHH}^{0, j, k}(\cal{R}(\beta))^\vee
    &\simeq \gr_{j + r}^{\bm{w}} \SHom^{j + k + r}(p_{\beta, !}\bar{\mathbf{Q}}_\ell, \cal{S}_1)\\
\sf{HHH}^{r, r + j, k}(\cal{R}(\beta))^\vee
    &\simeq \gr_{j + r}^{\bm{w}} \SHom^{j + k + r}(p_{\beta, !}\bar{\mathbf{Q}}_\ell, \cal{S}_\varepsilon).
\end{aligned}$$ By Springer theory, we know that:

-   $\cal{S}_1$ is the sheaf $\bar{\mathbf{Q}}_\ell\langle -r\rangle$ over $\cal{U}$.

-   $\cal{S}_\varepsilon$ is the skyscraper sheaf at $1 \in \cal{U}$ with stalk $\bar{\mathbf{Q}}_\ell\langle -r - 2N\rangle$.

Now, both of the desired isomorphisms follow from Lemma [\[lem:borel-moore\]](#lem:borel-moore){reference-type="ref" reference="lem:borel-moore"}. ◻
:::
