---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-011-23-generalized-young-diagrams
section_title: "Generalized Young diagrams"
section_number: 2.3
pages: 15-17
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.858
latex_coverage_ratio: 0.975
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
[]{#SubsectGeneralizedYD label="SubsectGeneralizedYD"} The second description of $\Lambda_\star^{(1)}$ is interesting because it shows that the value of a polynomial function is defined on more general objects than just Young diagrams.

::: definition
A *generalized Young diagram* is a broken line going from a point $(0,y)$ on the $y$-axis to a point $(x,0)$ on the $x$-axis such that every piece is either a horizontal segment from left to right or a vertical segment from top to bottom.
:::

Any Young diagram can be seen as such a broken line: just consider its border. The notions of inner and outer corners can be easily adapted to generalized Young diagrams, as well as the sets $\mathbb{I}_L$ and $\mathbb{O}_L$ of their contents. It is illustrated in Figure [1](#FigGeneralizedYD){reference-type="ref" reference="FigGeneralizedYD"}. Note also that the relation $p_1(\mathbb{I}_L-\mathbb{O}_L)=0$ holds for generalized Young diagrams as well.

<figure id="FigGeneralizedYD">
<div class="center">

</div>
<figcaption>A generalized Young diagram <span class="math inline"><em>L</em></span> with the corresponding sets <span class="math inline">𝕆<sub><em>L</em></sub> = {<em>o</em><sub>1</sub>, <em>o</em><sub>2</sub>}</span> and <span class="math inline">𝕀<sub><em>L</em></sub> = {<em>i</em><sub>1</sub>, <em>i</em><sub>2</sub>, <em>i</em><sub>3</sub>}</span>.</figcaption>
</figure>

Any polynomial function $F$ on the set of Young diagrams corresponds to the function $$\lambda \mapsto f(\mathbb{I}_\lambda - \mathbb{O}_\lambda)$$ for some symmetric function $f$. Recall that $f$ is uniquely determined up to addition of a multiple of $p_1$. Thus, $F$ can be canonically extended to generalized Young diagrams by setting $$F(L) = f(\mathbb{I}_L - \mathbb{O}_L).$$ As the relation $p_1(\mathbb{I}_L-\mathbb{O}_L)=0$ holds, $F(L)$ is well-defined, *i.e.* it does not depend on the choice of $f$.

<figure id="FigStretching">
<p><span class="math display">$$\begin{array}{c}
        \begin{tikzpicture}[scale=0.8]
            \draw[dashed,gray] grid (4.3,3.4);
            \draw[-&gt;,thick] (-0.2,0) -- (4.7,0);
            \draw[-&gt;,thick] (0,-0.2) -- (0,3.7);
            \draw[ultra thick] (0,2) 
            -- (.5,2) 
            -- (.5,.5) 
            -- (3,.5) 
            -- (3,0) ;
        \end{tikzpicture}\\
        \lambda
    \end{array}
    \mapsto 
     \begin{array}{c}
        \begin{tikzpicture}[scale=0.8]

            \draw[dashed,gray] grid (7.2,3.5);
            \draw[-&gt;,thick] (-0.2,0) -- (7.7,0);
            \draw[-&gt;,thick] (0,-0.2) -- (0,3.7);

            \begin{scope}[xscale=2,yscale=.5]
                        \draw[ultra thick] (0,2) 
                        -- (.5,2) 
                        -- (.5,.5) 
                        -- (3,.5) 
                        -- (3,0) ;
            \end{scope}
        \end{tikzpicture}\\
        T_{2,\frac{1}{2}} (\lambda)
    \end{array}$$</span></p>
<figcaption>Example of a Young diagram <span class="math inline"><em>λ</em></span> on the left and a stretched Young diagram <span class="math inline">$T_{2,\frac{1}{2}} (\lambda)$</span> on the right.</figcaption>
</figure>

We will be in particular interested in the following generalized Young diagrams. Let $\lambda$ be a (generalized) Young diagram and $s$ and $t$ two positive real numbers. $T_{s,t}(\lambda)$ denotes the generalized Young diagram obtained from $\lambda$ by stretching it horizontally by a factor $s$ and vertically by a factor $t$ in French convention (see Figure [2](#FigStretching){reference-type="ref" reference="FigStretching"}). These *anisotropic* Young diagrams have been first considered by Kerov in [@KerovAnisotropicYD], also in the context of Jack polynomials.

In the case $s=t$, we denote by $D_s(\lambda) := T_{s,s}(\lambda)$ the diagram obtained from $\lambda$ by applying a homothetic transformation of ratio $s$ and we will call it *dilated Young diagram*. In the case $s = t^{-1} = \sqrt{\alpha}$ for some $\alpha \in \mathbb{R}_+$ we denote by $A_\alpha(\lambda) := T_{\sqrt{\alpha},\sqrt{\alpha}^{-1}} (\lambda)$ the diagram obtained from $\lambda$ by stretching it horizontally by a factor $\sqrt{\alpha}$ and vertically by a factor $\sqrt{\alpha}^{-1}$. We call it *$\alpha$-anisotropic Young diagram*.

It is easy to check that the sets $\mathbb{I}_{D_s(\lambda)}$ and $\mathbb{O}_{D_s(\lambda)}$ are obtained from $\mathbb{I}_\lambda$ and $\mathbb{O}_\lambda$ by multiplying all values by $s$. In particular, if $F$ is a polynomial function such that the corresponding symmetric function $f$ is homogeneous of degree $d$, then $$\lambda \mapsto F(D_s(\lambda)) = f(\mathbb{I}_{D_s(\lambda)} - \mathbb{O}_{D_s(\lambda)})
= s^d f(\mathbb{I}_\lambda - \mathbb{O}_\lambda) = s^d F(\lambda)$$ is also a polynomial function. Finally, for any fixed $s>0$, $F$ is a polynomial function if and only if $\lambda \mapsto F(D_s(\lambda))$ is a polynomial function.
