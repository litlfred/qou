---
doc_id: arxiv-1103.2082v1
doc_title: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St)"
section_id: sec-015-42-dimensions-in-the-non-semisimple-block
section_title: "Dimensions in the Non-Semisimple Block"
section_number: 4.2
pages: 8-9
source_pdf: 1103.2082v1.pdf
source_sha256: 0ac5371486b38eac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 1.0
---
\label{Dimsec}  By \cite[Theorem 6.4]{CO1} the category $\uRep(S_0)$ has a unique nontrivial block.  The indecomposables in this block can be described explicitly and are denoted by $L_n=L((1^n))$ for $n \in \Z_{\geq 0}$.   In this section we compute the modified dimensions $\md_{\mt}\left( L_n\right)$ for all $n>0$.  

Recall that any indecomposable object in $\uRep(S_0)$ is of the form $([n], e)$ for some primitive idempotent $e\in FP_n(0)$ (see \cite[Proposition 2.20(2)]{CO1}).  Moreover, $A:=([n], e)$ is the direct summand of $B:=([n], \id_n)=L(\Box)\otimes ([n-1], \id_{n-1})$ where the inclusion map $A\to B$ and the projection map $B\to A$ are both given by $e$.  Hence 
\begin{equation*}\label{dcalc}\includegraphics{trace3.pdf}.\end{equation*}


Let $S_{n}$ be the symmetric group on $n$ letters whose elements are viewed as endomorphisms in Deligne's category \cite[Remark 2.14]{CO1}, and let $\sgn : S_{n} \to \{\pm 1 \}$ be the usual sign function.  Recall from \cite[Proposition 6.1]{CO1} that $L_n\cong([n], s_n)$ where 
\begin{equation}\label{E:sndef}
s_n=\frac{1}{n!}\sum_{\sigma\in S_n}\sgn (\sigma)\sigma.
\end{equation}
  In particular, $$\includegraphics{trace4.pdf}.$$  
For example, $$\includegraphics{trace6.pdf}$$ so that $$\includegraphics{trace7.pdf}.$$
More generally, given $\sigma\in S_n$, 
$$\includegraphics{trace5.pdf}.$$ Hence $$\md_{\mt}(L_n)=(-1)^{n+1}\frac{(\text{number of $n$-cycles in }S_n)}{n!}=\frac{(-1)^{n+1}}{n}.$$
