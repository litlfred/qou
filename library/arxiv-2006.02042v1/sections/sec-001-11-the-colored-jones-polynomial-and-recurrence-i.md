---
doc_id: arxiv-2006.02042v1
doc_title: "The Strong AJ Conjecture for the Figure 8 Knot"
section_id: sec-001-11-the-colored-jones-polynomial-and-recurrence-i
section_title: "The colored Jones polynomial and recurrence ideal"
section_number: 1.1
pages: 1-1
source_pdf: 2006.02042v1.pdf
source_sha256: 9de75ced3a3360bb
doc_brief: "The Strong AJ Conjecture for the Figure 8 Knot — Motivated by the theory of quantum A-ideals of Frohman-Gelca-Lo Faro, the theory of q-holonomicity of quantum invariants of Garoufalidis-Le and the AJ"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.982
---
For a knot $K$ in $S^3$ and a positive integer $n$, let $J_K(n) \in \BZ[t^{\pm 1}]$ denote the $n$-colored Jones polynomial of $K$ with zero-framing. The polynomial $J_K(n)$ is the quantum link invariant, as defined by Reshetikhin and Turaev \cite{RT}, associated to the Lie algebra $sl_2(\BC)$, with the color $n$ standing for the irreducible $sl_2(\BC)$-module $V_{n}$ of dimension $n$. Here we use the functorial normalization, i.e. the one for which $J_{\mathrm{unknot}}(n)=[n] := (t^{2n}- t^{-2n})(t^2 -t^{-2}).$ 
It is known that $J_K(1)=1$ and $J_K(2)$ is the ordinary Jones polynomial \cite{Jones}. The color $n$ can take non-positive integer values by setting $J_K(-n) = - J_K(n)$ and $J_K(0)=0$.

 Consider a discrete function $f: \BZ \to \CR:=\BC[t^{\pm 1}]$ and define the linear operators $L, M$ acting on such functions by $(Lf)(n) := f(n+1)$ and $(Mf )(n) := t^{2n} f(n).$
It is easy to see that $LM = t^2 ML$, and that $L^{\pm 1}, M^{\pm 1}$ generate the quantum torus $\CT$, a non-commutative ring with presentation
$\mathcal T := \mathbb \CR\langle L^{\pm1}, M^{\pm 1} \rangle/ (LM - t^2 ML).$

Let $\mathcal A_K := \{ P \in \mathcal T \mid  P J_K=0\}$ which is a left-ideal of $\mathcal T$, called the {\em recurrence ideal} of $K$. It was proved in \cite{GL} that for every knot $K$, the
recurrence ideal $\mathcal A_K$ is non-zero. An element in $\mathcal A_K$ is called a recurrence relation for the colored Jones polynomial of $K$.
