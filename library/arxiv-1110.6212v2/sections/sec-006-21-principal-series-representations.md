---
doc_id: arxiv-1110.6212v2
doc_title: "On calibrated representations and the Plancherel Theorem for aﬃne Hecke algebras"
section_id: sec-006-21-principal-series-representations
section_title: "Principal series representations"
section_number: 2.1
pages: 8-9
source_pdf: 1110.6212v2.pdf
source_sha256: 1923b6a0bfdc810f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.98
doc_brief: "On calibrated representations and the Plancherel Theorem for aﬃne Hecke algebras — This paper has two main purposes."
---
The large commutative subalgebra $\mathbb{C}[L]$ of $\mathscr{H}_L$ can be used to construct finite dimensional representations of $\mathscr{H}_L$. The *principal series representation* with *central character* $t\in\mathrm{Hom}(L,\mathbb{C}^{\times})$ is $$M(t)=\mathrm{Ind}_{\mathbb{C}[L]}^{\mathscr{H}_L}(\mathbb{C}v_t)=\mathscr{H}_L\otimes_{\mathbb{C}[L]}(\mathbb{C}v_t),$$ where $\mathbb{C}v_t$ is the $1$-dimensional representation of $\mathbb{C}[L]$ with $x^{\lambda}\cdot v_t=t^{\lambda} v_t$ for all $\lambda\in L$. It is clear that this representation is $|W_0|$-dimensional, and that $\{T_w\otimes v_t\mid w\in W_0\}$ is a basis of $M(t)$.

For $t\in\mathrm{Hom}(L,\mathbb{C}^{\times})$ define $$\begin{aligned}
N(t)&=\{\alpha\in R_0^+\mid n_{\alpha}(t)n_{-\alpha}(t)=0\}\\
D(t)&=\{\alpha\in R_0^+\mid d_{\alpha}(t)=0\}.
\end{aligned}$$ Note that $N(t)$ and $D(t)$ are closely related to the zeros of the numerator and denominator of the Macdonald $c$-function (respectively).

For $t\in\mathrm{Hom}(L,\mathbb{C}^{\times})$, let $$\begin{aligned}
W_t&=\{w\in W_0\mid wt=t\}\\
W_{(t)}&=\langle\{s_{\alpha}\mid \alpha\in D(t)\}\rangle.
\end{aligned}$$ Note that $W_{(t)}$ is a normal subgroup of $W_t$ (since $ws_{\alpha}w^{-1}=s_{w\alpha}$). Moreover, if $L=P$ then necessarily $W_{(t)}=W_t$ (see [@steinberg2 §4.2, 5.3]).

The following Theorem of Kato [@kato Theorem 2.2] is fundamental.

::: thm
[]{#thm:kato label="thm:kato"} The module $M(t)$ is irreducible if and only if $N(t)=\emptyset$ and $W_t=W_{(t)}$.
:::

The fundamental importance of the principal series representations is highlighted by the following fact (see, for example, [@ramcalib Proposition 2.6]).

::: prop
[]{#prop:quotient label="prop:quotient"} If $M$ is an irreducible representation of $\mathscr{H}_L$ with central character $t$ then $M$ is a quotient of $M(t)$. In particular $\mathrm{dim}(M)\leq |W_0|$.
:::
