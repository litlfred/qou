---
doc_id: arxiv-1707.02991v1
doc_title: "BPS states, knots and quivers"
section_id: sec-002-moduli-of-quiver-representations
section_title: "Moduli of quiver representations"
section_number: null
pages: 3-3
source_pdf: 1707.02991v1.pdf
source_sha256: f4f539f74403dd24
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.966
doc_brief: "BPS states, knots and quivers — 7 sections: Front matter; BPS states, knots and quivers; Knot invariants, knot homologies"
---
We now turn to a seemingly unrelated field of moduli of quiver representations. A quiver $Q$ is an oriented graph with a finite set of vertices $Q_0$ and finitely many arrows between vertices $\alpha:i\rightarrow j$. On ${\bf Z}Q_0$, we define the Euler form of $Q$ by $\langle {\bm d},{\bm e}\rangle_Q=\sum_{i\in Q_0}d_ie_i-\sum_{\alpha:i\rightarrow j}d_ie_j.$ A quiver representation assigns to each vertex $i\in Q_0$ a vector space of dimension $d_i$ and a linear map to each arrow. Recently it turned out that the structure of moduli spaces of quiver representations is very rich, and it is a natural playground for the theory of (motivic) Donaldson-Thomas invariants, Cohomological Hall Algebras, etc.

In particular various explicit results that we use in what follows are known for symmetric quivers, i.e. such that for any pair of vertices $i$ and $j$, the number of arrows from $i$ to $j$ equals the number of arrows from $j$ to $i$ [@Kontsevich:2010px; @efimov2012; @FR; @MR].

Of our main focus in what follows will be the following motivic generating series assigned to a symmetric quiver $$P_Q(x)=\sum_{{\bm d}\in{\bf N}Q_0}(-q)^{-\langle {\bm d},{\bm d}\rangle_Q} {\bm x}^{\bm d} \prod_{i\in Q_0}\prod_{j=1}^{d_i}\frac{1}{1-q^{-2j}}   \label{PQx}$$ where ${\bm x}^{\bm d}=\prod_{i\in Q_0}x_i^{d_i}$. Motivic Donaldson-Thomas invariants $\Omega_{{\bm d},j}\equiv \Omega_{d_1,\ldots,d_m;j}$ (with $m$ denoting the number of vertices) are then defined via the factorization $$P_Q(x)=

\prod_{{\bm d}\neq 0} \prod_{j\in\mathbb{Z}} \prod_{k\geq 0} \big(1 - (-1)^j {\bm x}^{\bm d} q^{j+2k+1} \big)^{-\Omega_{{\bm d},j}},   \label{PQx-Omega}$$

and proved to be positive integers [@efimov2012]. In [@MR; @FR] two geometric interpretations of coefficients of $\Omega_{\bm d}(q)$ are given: as the intersection Betti numbers of the moduli space of all semisimple representations of $Q$ of dimension vector ${\bm d}$, or as the Chow-Betti numbers of the moduli space of all simple representations of $Q$ of dimension vector ${\bm d}$.
