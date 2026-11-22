---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-005-2-the-algebra-u-hsl-2-and-its-subalgebras
section_title: "The algebra $U_h(sl_2)$ and its subalgebras"
section_number: 2
pages: 7-7
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 1.0
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec2 label="sec2"}

In this section, we recall the definition and some properties of the quantized enveloping algebra $U_h(sl_2)$. Then we define subalgebras $\Uq$ and $\Uqv$ of $U_h$, as well as their completions $\tUq$ and $\tUqv$, which we studied in [@H:uqsl2].

## $q$-integers {#sec:q-integers}

Let $h$ be an indeterminate, and set $$\begin{gathered}
  v=\exp\frac h2\in \modQ [[h]],\quad
  q=v^2=\exp h\in \modQ [[h]].
\end{gathered}$$ We have $\Zqq\subset \Zvv\subset \modQ [[h]]$.

We use two systems of $q$-integer notations. One is the "$q$-version": $$\begin{gathered}
  \{i\}_q = q^i-1,\quad
  \BBq{i}{n} = \{i\}_q\{i-1\}_q\cdots\{i-n+1\}_q,\quad
  \{n\}_q! =\BBq{n}{n},\\
  [i]_q=\{i\}_q/\{1\}_q,\quad
  [n]_q! = [n]_q[n-1]_q\cdots[1]_q,\quad
  \bbq{i}{n} = \BBq{i}{n}/\{n\}_q!,
\end{gathered}$$ for $i\in \modZ$, $n\ge 0$. These are elements in $\Zqq$. (In later sections, we also use $(q)_n=(-1)^n\{n\}_q!$.) The other is the "balanced $v$-version": $$\begin{gathered}
  \{i\} = v^i-v^{-i},\quad
  \BB{i}{n} = \{i\}\{i-1\}\cdots\{i-n+1\},\quad
  \{n\}!=\BB{n}{n},\\
  [i]=\{i\}/\{1\},\quad
  [n]! = [n][n-1]\cdots[1],\quad
  \bb{i}{n} = \BB{i}{n}/\{n\}!,
\end{gathered}$$ for $i\in \modZ$, $n\ge 0$. These are elements of $\Zqq\sqcup v\Zqq\subset \Zvv$. These two families of notations are the same up to multiplication by powers of $v$. The former system is useful in clarifying that formulas are defined over $\modZ [q,q^{-1}]$. The latter is sometimes useful in clarifying that formulas have symmetry under conjugation $v\leftrightarrow v^{-1}$.
