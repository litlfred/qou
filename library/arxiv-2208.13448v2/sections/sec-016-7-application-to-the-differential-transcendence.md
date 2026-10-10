---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-016-7-application-to-the-differential-transcendence
section_title: "Application to the differential transcendence"
section_number: 7
pages: 34-35
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.978
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
---
\label{sec:appliDiffalTranscendence}

Let $\k$ be a field of characteristic zero and $(\k,\phi,\partial)$ be a $\mathcal{C}^1$-field with no proper finite difference field extension,   equipped with an automorphism $\phi$, and a derivation $\partial$, that is an additive morphism satisfying the Leibnitz rule $\partial(fg)=\partial(f)g+f\partial(g)$. Let us assume that $\phi$ and $\partial$ commute.  In our examples, we may take $\partial=\partial_z$ (case S and E),  and $\partial=z \partial_z$ (case Q).  In the Mahler case,  we could adapt as in \cite{dreyfus2018hypertranscendence} the framework with the derivation $\partial= z \partial_z \log(z)$ but this will complicate the exposition of a general criterion, so let us drop the Mahler case in what follows. \par 
Let us consider $R$, a ring extension of $\k$ such that $\phi$ and $\partial$ extend on $R$.  We say that $f\in R$ is $\partial$-algebraic over $\k$ if there exists $n\in\N$ and a nonzero $P\in \k [X_0,\dots, X_n]$ such that $P(f,\dots, \partial^n f)=0$.  We say that $f$ is $\partial$-transcendent over $\k$ otherwise.  In  our examples,  $f$ is $\partial$-algebraic over $\k$ if and only if it is $\partial_z$-algebraic over $\k$.  Many proof of $\partial$-transcendence of solutions of $\phi$-equation are based on the difference Galois theory.  Roughly speaking, this kind of theorem says that if the difference Galois group is sufficiently big, then the nonzero solutions of the linear equation are $\partial$-transcendent.  Let $f\in R^*$ be a solution of 
$$ a_3\phi^3 (y)+ a_2 \phi^2 (y)+a_1 \phi (y)+a_0 y=0, \quad \text{where}\quad  a_i\in \k\quad \text{and}\quad  a_0 a_3 \neq 0.$$
Consider the dual 
$\sum_{i=0}^{3}  \phi^{-i} (a_{i})
\phi^{-i}$ that is equivalent to 
$$ \phi^3(a_0)\phi^3 (y)+ \phi^2(a_1) \phi^2 (y)+\phi(a_2) \phi (y)+a_3 y=0, \quad \text{where}\quad  a_i\in \k.$$



\begin{thm}

Let us assume that 
\begin{itemize}
\item there is no $u\in \k$ such that
$$a_3 u\phi(u)\phi^2 (u)+a_2 u\phi(u)+ a_1 u+a_0=0.$$
\item there is no $u\in \k$ such that
$$\phi^3(a_0) u\phi(u)\phi^2 (u)+\phi^2(a_1) u\phi(u)+ \phi(a_2) u+a_3=0.$$
\item there is no $g\in \k$ and nonzero linear differential operator $L\in C[\partial]$, such that  
$$L(\partial (a_0/a_3 )/(a_0/a_3))=\phi(g)-g. $$
\end{itemize}
Then,  $f$ is $\partial$-transcendent over $\k$.
\end{thm}

\begin{proof}
Let $G$ be the difference Galois group of the equation of order three satisfied by $f$.  The first assumption ensures that the operator has no right factor of order one and the second assumption ensures that the operator has no left factor of order one.  So the operator is irreducible and then the difference Galois group is irreducible.  When $G$ is  imprimitive, this is the same reasoning as \cite[Theorem 3.5]{arreche2021differential}.  When $G$ is primitive, it contains $\mathrm{SO}_3 (C)$ and   we now follow the proof  of \cite[Theorem 3.5]{arreche2021differential}. 
\end{proof}

\bibliographystyle{alpha}
