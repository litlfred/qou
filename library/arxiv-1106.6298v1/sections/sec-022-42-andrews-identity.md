---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS"
section_id: sec-022-42-andrews-identity
section_title: "Andrews identity"
section_number: 4.2
pages: 16-16
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.95
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariants."
---
To warm up
we start with the  identity from the Ramanujan ``Lost'' Notebook:
$$\prod_{k\geq 1}\frac{1}{(1-q^{5k-4})(1-q^{5k-1})}=\sum_{n\geq 0}
\frac{q^{n^2}}{(1-q)(1-q^2)\dots (1-q^n)} $$


Only in the
60s, MacMahon gave a combinatorial interpretation of this identity
as follows.
Let $\lambda=(\lambda_1, \lambda_2, \dots, \lambda_t)$ with
$\sum_i\lambda_i=n$ be a partition of $n$ into non--increasing integers.
Then the identity can derived from the fact that
the number of partitions of $n$ with all $\lambda_i$ of the
 form $5k+1$ or $5k+4$
is equal to the number of partitions where $\lambda_{i}-\lambda_{i+1}\geq 2$
for all $i$.

 This identity is a very special
case of the Andrews identity we used  in \cite{BBL}: For any numbers $b_i,c_i,
i=1,\dots,k$ and positive integer $N$ we have
\begin{multline*}  1+ \sum_{n =1}^N  q^{kn+Nn} (1+ q^n)  \frac{(q^{-N})_n}{(q^{N+1})_n} \prod_{i=1}^k
\frac{(b_i)_{n}}{b_i^{n}} \frac{(c_i)_{n}}{c_i^{n}}
\frac{1}{(\frac{q}{b_i})_n (\frac{q}{c_i})_n}=
\\
\frac{(q)_N\,  (\frac{q}{b_kc_k})_N}{(\frac{q}{b_k})_N\,
(\frac{q}{c_k})_N} \sum_{n_k \ge n_{k-1} \ge \dots \ge n_2 \ge n_1=0}
 \frac{q^{n_k} (q^{-N})_{n_k} (b_k)_{n_k}
(c_k)_{n_k}}{(q^{-N}b_kc_k)_{n_k}}\prod_{i=1}^{k-1}\frac{q^{n_i}
\frac{(b_i)_{n_i}}{b_i^{n_i}} \frac{(c_i)_{n_i}}{c_i^{n_i}}
(\frac{q}{b_i c_i})_{n_{i+1}-n_i} }{(q)_{n_{i+1}-n_i}
(\frac{q}{b_i})_{n_{i+1}}  (\frac{q}{c_i})_{n_{i+1}}} \label{1002}
\end{multline*}
where $(a)_n=(a;q)_n$.

The point is that (for a special choice of parameters)
the left hand side of the identity
 can be identified with
$\cL_{b,c;n}\left((q^{n};q)_{k+1}\; (q^{-n};q)_{k+1}\right)$, where
 the right hand side is a sum with all summands
divisible by $(q^{k+1};q)_{k+1}$.



In the case $b=\pm 1$, the computations are especially simple and we get
that
$$\cL_{-1,1;n}((q^{n};q)_{k+1}\; (q^{-n};q)_{k+1})=2(q^{k+1};q)_{k+1}\, .$$
The same holds also for $\cL_{1,1;n}$ up to units.
This allows to write the explicit formula for $I_M$ given in the introduction.
