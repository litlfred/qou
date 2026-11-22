---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-027-4-adding-knots-and-links-into-m-3
section_title: "Adding knots and links into $M_3$"
section_number: 4
pages: 55-56
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.995
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
The goal of this section is to incorporate knots and links in a non-trivial 3-manifold $M_3$ and produce the corresponding homological invariants. In particular, it will give us the very first examples where *both* knots and 3-manifolds are non-trivial.

The physical setup that we use to make concrete predictions for the new homological invariants ${\mathcal H}_a[M_3;K,{\mathcal R}]$ was already briefly mentioned in [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"}. As before, $K$ denotes a knot in $M_3$ while ${\mathcal R}$ denotes a representation (color) of CS gauge group $G$. The case of links is similar and involves assigment of color to each component of the link. The space ${\mathcal H}_a[M_3;K,{\mathcal R}]$ can be explored from a number of vantage points and in a variety of duality frames (all of which lead to the same result). In particular, from the vantage point of the theory $T[M_3]$ on fivebrane world-volume, incorporating knots and links corresponds to introducing a 1d defect ("impurity") which preserves the same supersymmetry as the background along $D^2 \cong {\mathbb R}^2_q$ in our previous discussion, *cf.* Figure [\[fig:impurity\]](#fig:impurity){reference-type="ref" reference="fig:impurity"}.

Alternatively, starting from the brane system [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"}, there are many possibilities [@Gukov:2015gmm] to accommodate knots inside $M_3$. We focus on those which give rise to line operators in $T[M_3]$.[^1] They correspond to codimension-four defects in the 6d (2,0) theory, engineered by either M2- or M5-branes (see *e.g.* [@Gang:2015bwa] for a discussion in the context of 3d-3d correspondence). For example, one can insert a stack of M2-branes in the following way: $$\begin{aligned}
\begin{matrix}
{\mbox {\textrm{$N$ fivebranes:}}}~~~\qquad & {\mathbb R}& \times & M_3& \times & D^2  \\ \qquad & &
&   \cap &  & \cap \\
{\mbox{\rm space-time:}}~~~\qquad & {\mathbb R}&  \times  & T^*M_3 & \times & TN   \\ \qquad & &
&   \cup &  & $\rotatebox[origin=c]{90}{$\in$}$ \\
{\mbox{\rm M2-branes:}}~~~\qquad &{\mathbb R}& \times & T^*K & \times  & O   \\
\end{matrix}.
\label{CatGeom2}
\end{aligned}$$ We have chosen the line defect in $T[M_3]$ to sit at the tip $O\in D^2$ (also the Taub-NUT center) to preserve the $U(1)_q$ rotational symmetry. Naively, the way the stack of M2-branes ends on $N$ fivebranes is determined by a partition of the number of M2 branes into $N$. Such partitions are in one-to-one correspondence with Young tableaux with at most $N$ rows, which are in turn can be identified with irreducible representations of $U(N)$. In the case of $SU(N)$ we have to mod out configurations where M2 branes are equally distributed among $N$ fivebranes. This leads to Young tableaux with at most $N-1$ rows that label irreducible representations of $SU(N)$. In reality, mapping line operators in 3d/3d correspondence and in the fivebrane setup is a delicate business and should be dealt with care.

If one wishes to use M5-branes to represent knots, then besides ${\mathbb R}_{\text{time}}\times K$ they would also occupy the two-dimensional co-normal bundle $N^*K$ of $K$ inside $T^*M_3$ and the cotangent space $T^*|_O$ to $D^2$ at $O$ [@Ooguri:1999bv]. Both constructions, based on M2- and M5-branes, lead to Wilson loops --- in fact, they are related by the Hanany-Witten type effect in M-theory or, in TQFT on $M_3$, by the Fourier transform from representation basis to holonomy basis.

Using this physical setup, we compute the new homological invariants ${\mathcal H}_a[M_3;K,{\mathcal R}]$ for some simple examples of non-trivial knots and 3-manifolds. In particular, we verify that suitable variants of the Conjectures [\[Conjecture1\]](#Conjecture1){reference-type="ref" reference="Conjecture1"} and [\[Conjecture2\]](#Conjecture2){reference-type="ref" reference="Conjecture2"} hold in the presence of knots and links.

[^1]: The other options lead to a 3d "space-time filling defect," deforming the theory to a new one $T[M_3,K]$.
