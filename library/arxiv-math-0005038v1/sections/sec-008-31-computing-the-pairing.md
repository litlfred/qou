---
doc_id: arxiv-math-0005038v1
doc_title: "Braid groups are linear"
section_id: sec-008-31-computing-the-pairing
section_title: "Computing the pairing"
section_number: 3.1
pages: 6-8
source_pdf: 0005038v1.pdf
source_sha256: db0b9b7a8534f161
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.949
doc_brief: "Braid groups are linear — The braid groups Bn can be deﬁned as the mapping class group of the n-punctured disc."
---
We now describe how to compute the pairing between a give noodle and fork. Let $N$ be a noodle and let $F$ be a fork. By applying a preliminary isotopy, we can assume that $T(F)$ intersects $N$ transversely at a finite number of points, which we label $z_1,\dots,z_l$. Let $F'$ be a parallel copy of $F$. Choose $F'$ so that $T(F')$ intersects $N$ transversely at $z'_1,\dots,z'_l$, where $z_i$ and $z'_i$ are joined by a short arc in $N$ which meets no other $z_j$ or $z'_j$. Let $z$ be the vertex which lies in all three edges of $F$, and let $z'$ be the vertex which lies in all three edges of $F'$.

For every pair $\{z_i,z'_j\}$ there exist unique integers $a_{i,j}$ and $b_{i,j}$ such that $\tilde{\Sigma}(F)$ intersects $q^{a_{i,j}}t^{b_{i,j}}\tilde{\Sigma}(N)$ at a point in the fiber of $\{z_i,z'_j\}$. Let $\epsilon_{i,j}$ denote the sign of that intersection. Let $m_{i,j} = q^{a_{i,j}}t^{b_{i,j}}$. Then $$\label{pairsum}
\langle N,F \rangle = \sum_{i=1}^l \sum_{j=1}^l \epsilon_{i,j}m_{i,j}.$$

We can compute $m_{i,j}$ as follows. Define the following embedded arcs in $D \setminus P$.

-   $\alpha_1$ from $d_1$ to $z$ along the handle of $F$,

-   $\alpha_2$ from $d_2$ to $z'$ along the handle of $F'$,

-   $\beta_1$ from $z$ to $z_i$ along $T(F)$,

-   $\beta_2$ from $z'$ to $z'_j$ along $T(F')$,

-   $\gamma_1$ from $z_i$ to $d_k$ along $N$, where $k=1,2$ is such that $\gamma_1$ does not pass through $z'_j$,

-   $\gamma_2$ from $z'_j$ to $d_{k'}$ along $N$, where $k'=1,2$ is such that $\gamma_2$ does not pass through $z_i$.

Let $$\delta_{i,j} = 
\{\alpha_1,\alpha_2\}
\{\beta_1,\beta_2\}
\{\gamma_1,\gamma_2\}.$$ Then $$m_{i,j} = \phi(\delta_{i,j}).$$

We can calculate the exponent $a_{i,j}$ even more explicitly. For $k=1,\dots,l$, let $\zeta_k$ be the arc from $d_1$ to $z_k$ along $F$, then back to $d_1$ along $N$. Let $a_k$ be the sum of the winding numbers of $\zeta_k$ around each of the puncture points. Let $\zeta$ be the arc from $d_1$ to $d_2$ along $N$, and then back to $d_1$ moving clockwise along $\partial D$. Let $a$ be the sum of the winding numbers of $\zeta$ around the puncture points.

::: clm
[]{#a label="a"} $a_{i,j} = a_i + a_j + a$.
:::

::: proof
*Proof.* Let $\zeta'_k$ be the arc from $d_2$ to $z'_k$ along $F'$, then back to $d_2$ along $N$. Let $a'_k$ be the sum of the winding numbers of $\zeta'_k$ around each of the puncture points. If $z_i$ is closer to $d_1$ than $z'_j$ along $N$ then $a_{i,j} = a_i + a'_j$. If not, then $a_{i,j} = a'_i + a_j$. But $a'_k = a_k + a$ for all $k=1,\dots,l$, so in either case $a_{i,j} = a_i + a_j + a$. ◻
:::

In order to compute $\epsilon_{i,j}$ we need to choose orientations for $\Sigma(F)$, $\Sigma(N)$ and $C$. We choose the orientation on $C$ induced by the product orientation on $D \times D$. We orient $\Sigma(F)$ and $\Sigma(N)$ as follows.

Let $f \colon\thinspace T(F) \to I$ and $f' \colon\thinspace T(F') \to I$ be diffeomorphisms which give $T(F)$ and $T(F')$ parallel orientations. Let $f_1$ and $f_2$ be the maps from $\Sigma(F)$ to $I$ such that if $x \in T(F) \setminus P$ and $y \in T(F') \setminus P$ then $f_1(\{x,y\}) = f(x)$ and $f_2(\{x,y\}) = f'(y)$. Then the $2$-form $df_1 \wedge df_2$ defines an orientation on $\Sigma(F)$.

Let $g \colon\thinspace N \to I$ be a diffeomorphism such that $g(d_1) = 0$ and $g(d_2) = 1$. Let $g_1$ and $g_2$ be the maps from $\Sigma(N)$ to $I$ given by $g_1(\{x,y\}) = \min(g(x),g(y))$ and $g_2(\{x,y\}) = \max(g(x),g(y))$. Then the $2$-form $dg_1 \wedge dg_2$ defines an orientation on $\Sigma(N)$.

::: clm
[]{#sign label="sign"} With these orientations, $\epsilon_{i,j} = -m_{i,i}m_{i,j}m_{j,j}|(q=1,t=-1)$.
:::

::: proof
*Proof.* By definition, $\epsilon_{i,j}$ is the sign of the volume form $dg_1 \wedge dg_2 \wedge df_1 \wedge df_2$ at the point $\{z_i,z'_j\}$ in $C$. This is determined by the following three things:

-   the sign of the intersection of $N$ with $T(F)$ at $z_i$,

-   the sign of the intersection of $N$ with $T(F')$ at $z'_j$,

-   which of $z_i$ and $z'_j$ is closer to $d_1$ along $N$.

These in turn are determined by the following three values respectively:

-   $m_{i,i}|(q=1,t=-1)$,

-   $m_{j,j}|(q=1,t=-1)$,

-   $m_{i,j}|(q=1,t=-1)$.

To see this, observe that in general the sign of $m_{i',j'}|(q=1,t=-1)$ is determined by whether the two points switch places in the path $\delta_{i',j'}$. This in turn is determined by which of $z_{i'}$ and $z'_{j'}$ is closer to $d_1$ along $N$.

It follows from the above considerations that $\epsilon_{i,j}$ is determined by the value of the product $m_{i,i}m_{i,j}m_{j,j}$ evaluated at $q=1$ and $t=-1$. It remains to check that the sign is as claimed. This can be done by calculating $\epsilon_{i,j}$ in a specific example. ◻
:::
