---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-014-7-linear-programming-with-dependence-on-the-cons
section_title: "Linear programming with dependence on the constraint matrix only"
section_number: 7
pages: 24-25
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.976
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:only-A}

Recent years have seen tremendous progress in the development of more efficient 
LP algorithms using interior point methods, see e.g. \cite{CLS19,LS19,Brand2020,Brand2021} and references therein. These algorithms are \emph{weakly} polynomial, i.e., their running time depends on the encoding length of the input $(A,b,c)$ of \ref{LP_primal_dual}.

A fundamental open problem is the existence of a \emph{strongly} polynomial LP algorithm; this was listed by Smale as one of the key open problems  in mathematics for the 21st century \cite{Smale98}. The number of arithmetic operations of such an algorithm would be polynomial in the number $n$ of variables  and $m$ of constraints, but independent of the input length.

Towards this end, there is a line of work on developing algorithms with running time depending only on the constraint matrix $A$, while removing the  dependence on $b$ and $c$. This direction was pioneered by Tardos's 1985 paper \cite{Tardos86}, giving an algorithm for \ref{LP_primal_dual} with integral $A$ that has runtime $\poly(m,n,\log \Delta_A)$.

A breakthrough work by  Vavasis and Ye \cite{Vavasis1996} introduced a \emph{Layered Least Squares Interior-Point Method} that solves \ref{LP_primal_dual} within $O(n^{3.5} \log (\bar \chi_A+n))$ iterations, each requiring to solve a linear system. Recall from Theorem~\ref{theorem:kappa_chi_bar_approx} that $\log (\bar \chi_A+n)=\Theta(\log(\kappa_A+n))$; also recall from  Proposition~\ref{prop:kappa-delta}  that $\kappa_A\le\Delta_A$.

Recently, \cite{DHNV20} improved the Vavasis--Ye bound to  $O(n^{2.5} \log(n) \log (\bar \chi_A^*+n))$ linear system solves, where $\bar \chi_A^*$ is the optimized version of $\bar\chi_A$, analogous to $\kappa^*_A$ defined in Section~\ref{subsec:def_chi_bar_star}. The key insight of this work is using  the circuit imbalance measure $\kappa_A$ as a proxy to $\bar\chi_A$. These results are discussed in Section~\ref{sec:LLS}.

Section~\ref{sec:black-box} exhibits another recent paper \cite{DadushNV20} that extends Tardos's black-box framework  to solve LP in runtime $\poly(m,n,\log (\bar \Le_A+n))$, based on the proximity results in Section~\ref{sec:hoffman}. We note that using an initial rescaling as in Theorem~\ref{thm:bar-chi-star}, we can obtain $\poly(m,n,\log (\bar \Le^*_A+n))$ runtimes from these algorithms.
