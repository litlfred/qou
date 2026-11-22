---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-013-32-the-cyclotomic-expansion
section_title: "The cyclotomic expansion"
section_number: 3.2
pages: 9-10
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.87
latex_coverage_ratio: 0.933
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sub.cyclotomic}


Habiro  found another interesting expansion of the colored Jones function, known as the
cyclotomic expansion. Although the cyclotomic expansion has important
arithmetic consequences, we discuss only its algebraic properties here. Let
us define:

\begin{equation}
\lbl{eq.Ckernel}
C_{n,k}(q) = \prod_{j=1}^{k} (q^n+q^{-n}-q^j-q^{-j}),
\quad \text{with} \quad C_{n,0}(q)
 :=1.
\end{equation}

Habiro  showed that there exist unique Laurent polynomials $H_{K,k}(q) \in \BZ[q^{\pm 1}], k=0,1,\dots $ such that


\begin{equation}
\lbl{cyc}
J_{K,n}(q) = \sum_{k=0}^{n-1} C_{n,k}(q)\, H_{K,k}(q).

\end{equation}







For details, see \cite[Section 6]{H1}. Note that our $H_{K,n}(q)$ is  $J_K(P''_n)$ in  Habiro's notation.
We will call the expansion
\eqref{cyc} the cyclotomic expansion. Since $C_{n,k}(q)=0$ if $k
\ge n$, the summation in \eqref{cyc} can be assumed from $0$
to $\infty$.



It is possible to solve for $H_{K,n}$ from Equation \eqref{cyc}. Explicitly, from \cite[Lemma 6.1]{H1} one has
\begin{equation}
  H_{K,n}(q)=\frac{1}{\{2n+2\}!}\sum_{k=1}^{n+1} (-1)^{n+1-k}
  \{2k\}\{k\}
\qbinom{2n+2}{n+1-k} J_{K,k}(q) \label{33}
\end{equation}

where we use the following definition

$$ \{n\} := q^{n/2} -q^{-n/2} \quad \text{and} \quad \{n\}! :=
\prod_{i=1}^n \{i\},$$



\begin{equation*}
 \qquad \{a\}_b :=
\frac{\{a\}!}{\{a-b\}!}=\prod_{j=a-b+1}^a\{ j \}, \qquad
\qbinom{a}{b} := \frac{\{ a \}!}{\{ b \}! \{ a-b \}!}
\end{equation*}
