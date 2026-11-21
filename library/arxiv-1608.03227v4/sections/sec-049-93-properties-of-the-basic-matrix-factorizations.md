---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-049-93-properties-of-the-basic-matrix-factorizations
section_title: "Properties of the basic matrix factorizations"
section_number: 9.3
pages: 51-51
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.838
latex_coverage_ratio: 1.0
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
In this subsection we collect various facts about the matrix factorizations from the previous subsection. In particular we explain how one can interpret the positive intersection matrix factorization as a cone of the identity matrix factorization and the blob matrix factorization.

::: proposition
We have the following homotopy $$\crXpr\sim \crXpr\brwsh{1}{-1}.$$
:::

::: proof
*Proof.* Let $R=\CC[\calXr_2]$ then we have the following diagram

$$\begin{tikzcd}[column sep=3cm, row sep=1.75cm]
&
\rgR
\arrow[xshift=-0.35ex]{r}{\yt\txz}
\arrow[xshift=-0.35ex]{d}{\exatt}
\arrow[dashed, bend left=40]{r}{\exaot}
&
\rgR
\arrow[xshift=-0.35ex]{l}{\exato}
\arrow[xshift=-0.35ex]{d}{\exatt}
&
\\
\vphantom{1mm}
&
\rgR
\arrow[phantom,pos=0.02]{l}{\Bigl(}
\arrow[xshift=-0.35ex]{r}{\yt\txz}
\arrow[xshift=-0.35ex]{u}{\exaoo}
\arrow[bend right=40,dashed,']{r}{\exaot}
&
\rgR
\arrow[phantom,pos=0.22]{r}{\Bigr)\brwsh{1}{-1}}
\arrow [xshift=-0.35ex]{l}{\exato}
\arrow[xshift=-0.35ex]{u}{\exaoo}
&
\vphantom{1mm}
\end{tikzcd}$$

Here dashed arrows denote homotopy morphisms and we used the relation $\exaoo\exatt - \exaot\exato = 1$. ◻
:::

::: proposition
[]{#prop: cones label="prop: cones"} We have following homotopies: $$\begin{aligned}
\crXp & \sim(  \mathsf{q}  \mathsf{t})^{-1}\Bigl(\crXpr \xrightarrow{\;\xchp\;}\crXbl\brwsh{-1}{-1} \Bigr), &
\crXn & \sim
(  \mathsf{q}  \mathsf{t})^{-1}
\Bigl(\crXbl\brwsh{-1}{-1} \xrightarrow{\;\xchm\;}(  \mathsf{q}  \mathsf{t})^2\,\crXpr\brwsh{-1}{1} \Bigr),
\end{aligned}$$ where

$$\begin{tikzcd}[column sep=3cm, row sep=1.75cm]
\crXpr
\arrow{d}{\xchp}
&   \mathsf{t}^{-1}\rgRmomo

\arrow[xshift=-0.35ex]{r}{-\exato}
\arrow{d}{1}
&
\rgR

\arrow[xshift=-0.35ex]{l}{-\yt\txz}
\arrow{d}{-\txz}
\\
\crXbl\arrow[phantom,pos=0.22]{r}{\brwsh{-1}{-1}}
\arrow{d}{\xchm}

& \rgR \arrow[xshift=-0.35ex]{r}{\exato\txz}
\arrow{d}{-\txz}
&
  \mathsf{q}^2  \mathsf{t}\rgRmomo

\arrow[xshift=-0.35ex]{l}{\yt}
\arrow{d}{1}
\\
(  \mathsf{q}  \mathsf{t})^2\,\crXpr \arrow[phantom,pos=0.22]{r}{\brwsh{-1}{1}}

&   \mathsf{q}^2  \mathsf{t}\,\rgR \arrow[xshift=-0.35ex]{r}{-\exato}
&
  \mathsf{q}^2  \mathsf{t}^2\,\rgRmomo

\arrow[xshift=-0.35ex]{l}{-\yt\txz}
\end{tikzcd}$$
:::
