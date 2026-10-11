---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL(2)"
section_id: sec-007-the-haar-functional
section_title: "the haar functional"
section_number: null
pages: 9-10
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
doc_brief: "Twisted homology of quantum SL(2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra o f the quan- tum SL(2) group"
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.953
---
The Hopf algebra $\mathcal{A}$ is cosemisimple [@KS1], that is, there is a unique linear functional $h : \mathcal{A}\rightarrow k$ satisfying $h(1)=1$ and $$(h \otimes \mathrm{id}) \Delta (x) = h(x) 1 = ( \mathrm{id}\otimes h ) \Delta(x) 
    \quad \forall \; x \in \mathcal{A}$$ If $k=\mathbb{C}$ and $q \in \mathbb{R}$, then $\mathcal{A}$ can be made into a Hopf $\ast$-algebra whose C\*-algebraic completion is Woronowicz's quantum $SU(2)$ group [@wo_suq2]. The functional $h$ extends to the Haar state of this compact quantum group. Hence (with slight abuse of terminology) we also in the general case call $h$ the Haar functional of $\mathcal{A}$. For any $x$, $y \in \mathcal{A}$, we have $$\label{defn_mod_aut}
h( xy ) = h ( y \sigma_{mod}(x))$$ where $\sigma_{mod}$ is the so-called modular automorphism of $\mathcal{A}$ given by $$\label{smod_slq2}
\sigma_{mod}(a) = q^{-2} a, \quad
\sigma_{mod}(d) = q^{2} d, \quad
\sigma_{mod}(b) = b, \quad
\sigma_{mod}(c) = c$$ So $h$ is a $\sigma_{mod}^{-1}$-twisted cyclic 0-cocycle.

## the automorphism group of $\mathcal{A}( SL_q (2))$

For $\lambda,\mu \in k^\times$ there are unique automorphisms $\sigma_{\lambda, \mu},\tau_{\lambda, \mu}$ of $\mathcal{A}$ with $$\sigma_{\lambda, \mu}(a)=\lambda a,\quad
    \sigma_{\lambda, \mu}(b)=\mu b,\quad
    \sigma_{\lambda, \mu}(c)=\mu^{-1} c,\quad
    \sigma_{\lambda, \mu}(d)=\lambda^{-1} d,$$ $$\label{defn_lambda_tau}
 \tau_{\lambda, \mu}(a)=\lambda a,\quad
    \tau_{\lambda, \mu}(b)=\mu^{-1} c,\quad
    \tau_{\lambda, \mu}(c)=\mu b,\quad
    \tau_{\lambda, \mu}(d)=\lambda^{-1} d.$$ It is easy to check that this list is complete, although we do not know a reference where this was pointed out explicitly:

::: prop
[]{#autos label="autos"} If $\sigma$ is an automorphism of $\mathcal{A}(SL_q (2))$, then either $\sigma=\sigma_{\lambda, \mu}$ or $\sigma=\tau_{\lambda, \mu}$ for some $\lambda,\mu$.
:::

::: pf
Using the $\mathbb{Z}$-grading and the $\mathbb{N}$-filtrations mentioned above it is a straightforward calculation to check that up to rescaling and exchanging $b$ and $c$ the original generators are the only elements of the algebra that fulfill the defining relations.
:::

The $\sigma_{\lambda,\mu}$ act diagonally with respect to the generators $a,b,c,d$. The $\tau_{\lambda,\mu}$ are also diagonalizable. For fixed $\lambda, \mu$ define $x_\pm = c \pm \mu b$. Then $\tau_{\lambda,\mu} ( x_{\pm} ) = \pm x_{\pm}$, and $a, x_+ , x_- ,d$ generate $\mathcal{A}$. So by Proposition [\[tatata\]](#tatata){reference-type="ref" reference="tatata"}:

::: cor
[]{#crucial_isomorphism label="crucial_isomorphism"} For $\mathcal{A}= \mathcal{A}( SL_q (2))$, and for each $n$ and every automorphism $\sigma$, we have $HH_n^\sigma(\mathcal{A}) \cong H_n (\mathcal{A}, {}_\sigma\mathcal{A})$.
:::

# Twisted Hochschild homology of $\mathcal{A}( SL_q (2))$ {#section_th_slq2}
