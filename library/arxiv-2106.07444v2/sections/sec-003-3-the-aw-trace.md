---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-003-3-the-aw-trace
section_title: "The AW Trace"
section_number: 3
pages: 30-32
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.934
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the Weyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
[]{#sec:a_w label="sec:a_w"}

## 

If $A$ is a $\bb{Z}$-graded $\bar{\mathbf{Q}}_\ell$-algebra, then we write:

1.  $\mathsf{Mod}_1(A)$ for the category of graded left $A$-modules in which the grading is bounded below and each graded piece is finite-dimensional.

2.  $\mathsf{Mod}_2^b(A)$ for the category of left $A$-modules $M$ equipped with a $\bb{Z}^2$-grading such that $M \in \sf{Mod}_1(A)$ with respect to both gradings and the value of $i - j$ is uniformly bounded among the nonzero components $M^{i, j}$.

If $R$ is an (ungraded) $\bar{\mathbf{Q}}_\ell$-algebra and $A$ forms an $R$-module, then we write $R \ltimes A$ for the vector space $R \otimes A$ endowed with the ring structure where:

-   $R$ and $A$ form subrings.

-   The only relations between $R$ and $A$ are those of the form $ra = (r \cdot a)r$ for all $r \in R$ and $a \in A$.

If the $R$-action on $A$ preserves the grading, then we extend the grading on $A$ to a grading on $R \ltimes A$ in which $R$ is placed in degree zero, so that $R \ltimes A$ forms a graded $A$-algebra.

Recall that $\bb{X}$ is the character lattice in the root datum of $G$. We set $$\begin{aligned}
\bb{V} = \bb{X} \otimes \bar{\mathbf{Q}}_\ell.
\end{aligned}$$ Let the symmetric algebra $\Sym(\bb{V})$ be endowed with the grading where $\Sym^i(\bb{V})$ is placed in degree $2i$, and let $$\begin{aligned}
\bb{A}_W = \bar{\mathbf{Q}}_\ell[W] \ltimes \Sym(\bb{V}).
\end{aligned}$$ Below, we construct a contravariant, monoidal trace from the Hecke category to $\mathsf{Mod}_2^b(\bb{A}_W)$.

## 

Suppose that $X_0$ is a $G_0$-variety over $\bb{F}$ and that $\sf{C}(X_0)$ is a full, additive subcategory of $\sf{D}_{G, m}^b(X_0)$ stable under $\langle n\rangle$ for all $n \in \bb{Z}$. Any object $K \in \underline{\sf{C}}(X_0)$ gives rise to a graded $\bar{\mathbf{Q}}_\ell$-algebra: $$\begin{aligned}
\bb{A}_K = \bigoplus_n
{\Hom_{\underline{\sf{C}}(X_0)}(K, K \langle n\rangle)}.
\end{aligned}$$ We write the multiplication in $\bb{A}_K$ as right-to-left composition: $g \cdot f = g \circ f$. Then we have additive functors $$\begin{aligned}
\bigoplus_n
{\Hom_{\underline{\sf{C}}(X_0)}(-, K\langle n\rangle)}
    : \underline{\sf{C}}(X_0)^\op &\to \mathsf{Mod}_1(\bb{A}_K),\\  
\bigoplus_n
{\Hom_{\underline{\sf{C}}(X_0)}(K, (-)\langle n\rangle)}
    : \underline{\sf{C}}(X_0) &\to \mathsf{Mod}_1(\bb{A}_K^\op).
\end{aligned}$$ Above, the gradings are bounded below by Remark [\[rem:bounded-below\]](#rem:bounded-below){reference-type="ref" reference="rem:bounded-below"}. These functors can be respectively extended to $$\begin{aligned}
\bigoplus_{i, j} 
{\Hom_{\sf{K}^b(\underline{\sf{C}}(X_0))}(-, K\langle j\rangle [i - j]_\triangle)}
    : \sf{K}^b(\underline{\sf{C}}(X_0))^\op &\to \mathsf{Mod}_2^b(\bb{A}_K),\\  
\bigoplus_{i, j} 
{\Hom_{\sf{K}^b(\underline{\sf{C}}(X_0))}(K, (-)\langle j\rangle [i - j]_\triangle)}
    : \sf{K}^b(\underline{\sf{C}}(X_0)) &\to \mathsf{Mod}_2^b(\bb{A}_K^\op),
\end{aligned}$$ once we embed $\underline{\sf{C}}(X_0)$ into $\sf{K}^b(\underline{\sf{C}}(X_0))$ as the full subcategory of complexes concentrated in degree zero. Above, in either direct sum, the value of $i - j$ is uniformly bounded among the nonzero terms precisely because the objects of $\sf{K}^b(\underline{\sf{C}}(X_0))$ can be represented by bounded complexes.

In the rest of this section, we only use the contravariant functors; the covariant ones will appear again in Section [\[sec:kr\]](#sec:kr){reference-type="ref" reference="sec:kr"}. The following lemma is a consequence of Proposition [\[prop:realization\]](#prop:realization){reference-type="ref" reference="prop:realization"}.

::: lem
[]{#lem:hom-pure label="lem:hom-pure"} If $\sf{C}(X_0)$ is $\SHom$-pure, then we have a commutative diagram: $$\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=3em, column sep=9.5em, text height=2ex, text depth=0.5ex]
{   \sf{K}^b(\sf{C}(X_0))^\op
        &\sf{K}^b(\underline{\sf{C}}(X_0))^\op\\
    \sf{D}_{G, m}^b(X_0)^\op
        &\mathsf{Mod}_2^b(\bb{A}_K)\\
        };
\path[->,font=\scriptsize, auto]
(m-1-1)     edge node{$\sf{K}^b\kappa$} (m-1-2)
            edge node[left]{$\rho$} (m-2-1)
(m-1-2)     edge node{$\bigoplus_{i, j} \Hom(-, K\langle j\rangle [i - j]_\triangle)$} (m-2-2)
(m-2-1)     edge node{$\bigoplus_{i, j} \gr_j^{\bm{w}} \SHom^i(-, K)$} (m-2-2);
\end{tikzpicture}$$
:::

## 

We now set $X_0 = \cal{U}_0$ and $\sf{C}(X_0) = \sf{C}(\cal{U}_0)$ as in Definition [\[df:unipotent\]](#df:unipotent){reference-type="ref" reference="df:unipotent"}. Recall that $\cal{S} \in \sf{C}(\cal{U}_0)$ denotes the (mixed) Springer sheaf.

::: thm
[]{#thm:lusztig-algebra label="thm:lusztig-algebra"} We have $\bb{A}_W \simeq \bb{A}_\cal{S}$ as graded $\bar{\mathbf{Q}}_\ell$-algebras.
:::

::: proof
*Proof.* By [@lusztig_1988 Cor. 6.4], $\bb{A}_W 
\simeq \End^\ast(\xi \cal{S})$. By Lemma [\[lem:unipotent\]](#lem:unipotent){reference-type="ref" reference="lem:unipotent"} (or [@rider Lem. 5.4]), we have $\End^i(\xi\cal{S}) \simeq \SHom^0(\cal{S}, \cal{S}\langle i\rangle)$ for all $i$ after we forget Frobenius. ◻
:::

::: rem
Although we will not use it, the proof of [@rider Prop. 6.5] implies that the functor $\bigoplus_i \Hom(\cal{S}, (-)\langle i\rangle)$ induces a triangulated equivalence $$\begin{aligned}
\sf{K}^b(\sf{C}_{\hat{W}}(\cal{U}_0))
\simeq \sf{D}^b(\mathsf{Mod}_1(\bb{A}_W)),
\end{aligned}$$ where the right-hand side is the bounded derived category of $\mathsf{Mod}_1(\bb{A}_W)$.
:::

::: df
The **$\bb{A}_W$ trace** on the Hecke category is the contravariant functor $$\begin{aligned}
\sf{AH} : \sf{H}_W^\op \to \mathsf{Mod}_2^b(\bb{A}_W)
\end{aligned}$$ defined by the commutative diagram $$\label{eq:a_w}
{\small
\begin{tikzpicture}[baseline=(current bounding box.center), >=stealth]
\matrix(m)[matrix of math nodes, row sep=2.5em, column sep=6.5em, text height=2ex, text depth=0.5ex]
{   \sf{K}^b(\sf{C}(\cal{B}_0 \times \cal{B}_0))^\op
        &\sf{K}^b(\sf{C}(\cal{U}_0))^\op
        &\sf{K}^b(\underline{\sf{C}}(\cal{U}_0))^\op\\
    \sf{D}_{G, m}^b(\cal{B}_0 \times \cal{B}_0)^\op
        &\sf{D}_{G, m}^b(\cal{U}_0)^\op
        &\mathsf{Mod}_2^b(\bb{A}_W)\\
        };
\path[->,font=\scriptsize, auto]
(m-1-1)     edge node{$\sf{K}^b(i^\ast\langle -r\rangle \circ \sf{CH})$} (m-1-2)
(m-2-1)     edge node{$i^\ast\langle -r\rangle \circ \sf{CH}$} (m-2-2)
(m-1-2)     edge node{$\sf{K}^b\kappa$} (m-1-3)
(m-1-1)     edge node[left]{$\rho$} (m-2-1)
(m-1-2)     edge node{$\rho$} (m-2-2)
(m-1-3)     edge (m-2-3)
(m-2-2)     edge (m-2-3);
\end{tikzpicture}}$$ that we obtain by combining Remark [\[rem:compatible\]](#rem:compatible){reference-type="ref" reference="rem:compatible"}, Lemma [\[lem:unipotent\]](#lem:unipotent){reference-type="ref" reference="lem:unipotent"}, Lemma [\[lem:hom-pure\]](#lem:hom-pure){reference-type="ref" reference="lem:hom-pure"}, and Theorem [\[thm:lusztig-algebra\]](#thm:lusztig-algebra){reference-type="ref" reference="thm:lusztig-algebra"}. Explicitly, $$\begin{aligned}
\begin{split}
\sf{AH}^{i, j} 
&=  \Hom_{\sf{K}^b(\underline{\sf{C}}(\cal{U}_0))}(\sf{K}^b(\kappa \circ i^\ast\langle -r\rangle \circ \sf{CH})(-), \cal{S}\langle j\rangle [i - j]_\triangle)\\
&\simeq 
    \gr_j^{\bm{w}} \SHom^i((\rho \circ \sf{K}^b(i^\ast\langle -r\rangle \circ \sf{CH}))(-), \cal{S})\\
&\simeq
    \gr_j^{\bm{w}} \SHom^i((i^\ast\langle -r\rangle \circ \sf{CH} \circ \rho)(-), \cal{S})
\end{split}
\end{aligned}$$ for all $i, j$. It is a monoidal trace in the sense of Lemma [\[lem:monoidal-trace\]](#lem:monoidal-trace){reference-type="ref" reference="lem:monoidal-trace"} because it factors through $\sf{CH}$.
:::
