---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-002-13-applications
section_title: "Applications"
section_number: 1.3
pages: 7-8
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.983
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{subsec:applications}
After proving our abstract results, we provide a large set of (new) examples where these results can be applied. 
We have thus devoted the second half of the paper to examples, from a variety of different areas.\bigskip

Section \ref{sec:firstexamples} contains examples where the moment generating function is explicit,
or given as a path integral of an explicit function.



First, in Section \ref{subsec:arithmetic},
we recover results of Radziwill \cite{Rad09} on precise large deviations for additive arithmetic functions,
by carefully recalling the principle of the Selberg-Delange method.
The next examples --- Sections \ref{subsec:cycles} and \ref{subsec:rises} --- involve the total number of cycles (resp. rises) for random permutations.
The precise large deviation result in the case of cycles was announced in a recent paper of Nikeghbali and Zeindler \cite{NZ13},
where the mod-convergence was proved by the singularity analysis method.
Finally, in Section \ref{subsec:rmtpol}, we compute deviation probabilities of the characteristic polynomial of random matrices in compact Lie groups.
This completes previous results by Hughes, Keating and O'Connell \cite{HKO01} on large deviations for the characteristic polynomial.
\medskip 

Surprisingly, mod-Gaussian convergence can also be established in some cases,
even if neither the moment generating function nor an appropriate bivariate generating series is known explicitly.
A first example of this situation is given in Section \ref{sec:zeros}.
We give a criterion based on the location of the zeroes of the probability generating function,
which ensures mod-Gaussian convergence. We then apply this result to the number of blocks in a uniform random set-partition of size $n$. As a consequence, we obtain the normality zone for this statistics,
refining the central limit theorem of Harper \cite{HarperCLTBlocks}.
\medskip

Our next examples lie in the framework in which mod-Gaussian convergence
is obtained {\em via} bounds on cumulants (Section \ref{subsec:modgaussfromcumulants}). 
In Section \ref{sec:depgraph}, we show that such bounds on cumulants typically arise 
for $X_n=\sum_{i=1}^{N_n} Y_i$,
where the $Y_i's$ have a {\em sparse dependency graph}
 (references and details are provided in Section \ref{sec:depgraph}).
With weak hypothesis on the second and third cumulants, this implies mod-Gaussian convergence of a renormalized version of $X_n$
(Theorem \ref{thm:modgaussiangeneralsparsegraph}).
This allows us to provide new examples of variables converging in the mod-Gaussian sense.\vspace{2mm}






\begin{itemize}
    \item First, we consider subgraph count statistics $X_\gamma$ in Erd\"os-R\'enyi random graph $G(n,p)$ (Theorem \ref{thm:moddevgraphs}) for a fixed $p$ between $0$ and $1$. 
        Moderate deviation probabilities in this case are given and compared with the literature on the subject in Section~\ref{sec:erdosrenyi}. We are also able to determine the size of the normality zone of $X_\gamma$.\vspace{2mm}


    \item In our last application in Section \ref{sec:central}, we use the machinery of depen\-den\-cy gra\-phs in non-commutative probability spaces, namely, the algebras $\C\sym(n)$ of the symmetric groups, all endowed with the restriction of a trace of the infinite symmetric group $\sym(\infty)$. The technique of cumulants still works and it gives the fluctuations of random integer partitions under so-called {\em central measures} in the terminology of Kerov and Vershik. Thus, one obtains a central limit theorem and moderate deviations for the values of the random irreducible characters of symmetric groups under these measures.\vspace{2mm}
\end{itemize}    
The variety of the many examples that fall in the seemingly more restrictive setting of mod-Gaussian convergence makes it tempting to assert that it can be considered as a universality class for second order fluctuations. 
\bigskip

\begin{remark}
The idea of using bounds on  cumulants to show moderate deviations for a family of random variable with some given dependency graph is not new --- see in particular \cite{DE12}. Nevertheless, the bounds we obtain in Theorem \ref{thm:dependencygraphs} (and also in Theorem \ref{thm:dependencygraphsrefined}) are stronger than those which were previously known and, as a consequence, we obtain deviation results at a larger scale. Another advantage of our method is that it gives estimates of the deviation probability itself,
and not only of its logarithm.
\end{remark}
\bigskip
