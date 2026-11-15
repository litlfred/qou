---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-016-3-topological-invariance-of-our-torsion
section_title: "Topological invariance of our torsion"
section_number: 3
pages: 15-16
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.959
---
[]{#sec.torsion label="sec.torsion"}

Given a one-cusped hyperbolic manifold $M$ with regular triangulation $\mathcal{T}=\{\Delta_i\}_{i=1}^N$ and Neumann-Zagier datum $\widehat\beta_\mathcal{T}=(z,\mathbf A,\mathbf B,f)$, we have proposed that the nonabelian torsion is given by

$$\label{tor}
\qquad \tau_{\mathcal{T}} := 
\pm \frac12\det\big(\mathbf A\Delta_{z''}
+\mathbf B\Delta_z^{-1}\big)z^{f''}z''^{-f} 
\quad\in\,E_M /\{\pm 1\}\,,$$

where $\Delta_{z}=\text{diag}(z_1,...,z_N)$, and similarly for $\Delta_{z''}$. Since $(z,z',z'') \in E_M$ we must have $\tau_\mathcal{T}\in E_M$ as well.

After a brief example of how the formula [\[tor\]](#tor){reference-type="eqref" reference="tor"} works, we will proceed to prove Theorems [\[thm.indep\]](#thm.indep){reference-type="ref" reference="thm.indep"} and [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"} on the topological invariance of $\tau_\mathcal{T}$. We saw in Section [\[sec.triang\]](#sec.triang){reference-type="ref" reference="sec.triang"} that the Neumann-Zagier datum depends not only on a triangulation $\mathcal{T}$, but also on a choice of

1.  quad type for $\mathcal{T}$,

2.  one edge of $\mathcal{T}$ whose gluing equation is redundant,

3.  normal meridian path,

4.  flattening $f$.

We will begin by showing that $\tau_\mathcal{T}$ is independent of these four choices, and then show that it is invariant under 2--3 moves, so long as the 2--3 moves connect two regular triangulations.

The four choices here are independent, and can be studied in any order. However, in order to prove independence of flattening, it is convenient to use a quad type for which the matrix $\mathbf B$ is non-degenerate. Such a quad type can always be found (Lemma [\[lemma.B\]](#lemma.B){reference-type="ref" reference="lemma.B"}), but is not automatic. Therefore, we will first show invariance under change of quad type, and then proceed to the other choices. It is interesting to note that of all the arguments that follow (including the 2--3 move), independence of flattening is the only one that requires the use of the full gluing equations $z^{\mathbf A}z''{}^{\mathbf B}=(-1)^\nu$.

## Example: $\mathbf{4_1}$ continued {#sub.torexample}

To illustrate the Definition [\[torintro\]](#torintro){reference-type="ref" reference="torintro"}, consider the figure-eight knot complement again. From Section [\[sec.41triang\]](#sec.41triang){reference-type="ref" reference="sec.41triang"}, we already have one possible choice for the Neumann-Zagier matrices [\[NZ41\]](#NZ41){reference-type="eqref" reference="NZ41"} and a generic flattening [\[flat41\]](#flat41){reference-type="eqref" reference="flat41"}. We use them to obtain

$$\begin{aligned}
\pm\tau_{\mathbf{4_1}} &= \frac12 \det\left[\begin{pmatrix} 2 & 2 \\ 1 & 1 
\end{pmatrix}\begin{pmatrix} z'' & 0 \\ 0 & w'' \end{pmatrix} 
+ \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} z^{-1} & 0 
\\ 0 & w^{-1} \end{pmatrix}\right] w''{}^{-1} \notag \\
&= \frac1{2w''}\det\begin{pmatrix} 2z''+z^{-1} & 2w''+w^{-1}
\\ z''+z^{-1} & w'' \end{pmatrix} \notag \\
&= \frac1{2w''}\det\begin{pmatrix} z''+1 & w''+1\\ 1 & w'' 
\end{pmatrix} \notag\\ 
&=\frac12(z''-w''{}^{-1}) = \frac12{\sqrt{-3}}\,, \label{tor41}
\end{aligned}$$

where at intermediate steps we used $z''+z^{-1}-1=w''+w^{-1}-1=0$, and at the end we substituted the discrete faithful solution $z=z''=w=w''=e^{i\pi/3}$.

The invariant $\tau_{\mathbf{4_1}}$ belongs to the invariant trace field $E_{\mathbf{4_1}} = \mathbb{Q}(\sqrt{-3})$, and agrees with the torsion of the figure-eight knot complement [@DFJ].
