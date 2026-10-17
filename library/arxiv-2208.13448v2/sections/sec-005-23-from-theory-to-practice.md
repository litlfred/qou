---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-005-23-from-theory-to-practice
section_title: "From theory to practice"
section_number: 2.3
pages: 7-9
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.966
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀerence Galois groups of order three equations for a large class"
---
\label{sec:theoryPractice}
We recall that the aim of this paper is to explain how one can compute theoretically the Galois group of a difference equation of order $3$.
In practice we may also need to make more assumptions on the difference field $(\k,\phi)$ in order to compute effectively the difference Galois groups:
\begin{itemize}
\item
Assume that $\mathbf{k}$ is an effective field,
i.e. that one can compute representatives of the four operations $+,-,\times,/$ and one can effectively test whether two elements of $\mathbf{k}$ are equal.  
\item 
Assume that, given a homogeneous linear difference system $[A]$ with $A\in \GL_n(\mathbf{k})$, we can effectively find a 
basis of its rational solutions, i.e. its solutions $Y\in \mathbf{k}^n$.
\item Assume that given a difference operator $L$, if $L$ admits at least one right factor of order one, then we are able to compute effectively one of such right factors.
\end{itemize}


When $C=\overline{\Q}$,  for the cases (S, Q, M), the  two first points are satisfied. One can find some references for the second point in this table:
\medskip
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
    cases &  (S) & (Q) & (M)&(E) \\
\hline 
    ref. & \cite{Abr95,AB98,vanHoeij1998,AB2001} & \cite{Abr95,AB2001,Abr02} & \cite{CDDM18} & \cite{dreyfus2015galois,combot2022hyperexponential}\\
\hline
\end{tabular}
\end{center}
\medskip 

Note that in the elliptic case the second  point is not satisfied, unless considering the case $n=2$, see \cite{dreyfus2015galois} (note that the latter is concerned by the more general problem of solving Riccati equations), or when the framework is modified,  see for instance \cite{combot2022hyperexponential}.  Thus, in that case, our algorithm may not lead to a systematic computation of the difference Galois group. It will reduce the computation to the determination of rational solutions of certain linear difference equations that may be complicated to solve concretely.
Throughout this paper, we will emphasize which kind of equations we have to be able to solve. 


We saw in Section \ref{secfact} that the study of the irreducibility of the Galois groups is closely related to the factorisation of the difference operator.  From Lemma \ref{lem:eq left factor}, when we look at a right factor of order one, we have to solve a Riccati equation of the form  $$
\sum\limits_{i=0}^n a_i \prod\limits_{j=0}^{i-1} \phi^j(\alpha) = 0.
$$

When $C=\overline{\Q}$,  we are able to compute right-factors of order $1$ in the cases (S,Q,E) but we want to emphasis that the complexity is exponential, in the order of the equation, contrary to the search of rational solutions, whose complexity is polynomial. 
   Here-below, one can find some references for these computations:

\medskip
\begin{center}
\begin{tabular}{|c|c|c|c|}
\hline
    cases &  (S) & (Q) & (E)\\
\hline 
ref.  & \cite{Petkovsek92,CvH06,abramov2021rational} & \cite{APP98,CvH06,abramov2021rational} &\cite{dreyfus2015galois,combot2022hyperexponential} \\
\hline
\end{tabular}
\end{center}
\medskip 
For the Mahler case, the computation of Riccati solution is a work in progress by the first author of this paper, Chyzak, Dumas and Mezzarobba.
\medskip
\begin{ex}\label{ex1}
Let us now present the strategy of \cite{abramov2021rational} to show that the difference Galois group of  \eqref{eq0} over $\C(z^{1/*})$ is irreducible, which is equivalent to show that the corresponding operator has no factor of order $1$. We point out the fact that $\C(z^{1/*})$ is not an effective field but the strategy still work in that case. 
Assume that $t\neq 0$. 
 Let us begin by proving that there is no right factor of order one. Let 
 $$L=a_0+a_1 \phi+ a_2\phi^2+a_3 \phi^3$$
  be the $q$-difference operator corresponding to \eqref{eq0}, and let $L^{\vee} $ be its dual. 
By  \cite[Lemma 3]{abramov2021rational},
 For any $\alpha \in \k^{\times}$  there exist $\lambda \in \C^{\times}$, $\ell\in\N^*$ and unitary $b,c,r\in \C[z^{1/\ell}] \setminus \{0\}$  such that 
$$
  \alpha =\lambda\hspace{0.1cm}  \frac{b}{c} \hspace{0.1cm}\frac{\phi(r)}{r}
$$
 and 
\begin{itemize}
\item $\gcd (b, \phi^k (c))=1$ for all $k\in \lbrace 0,1, 2\rbrace$;
\item $\gcd (b, r)=1$;
\item $\gcd (c, \phi (r))=1$.
\end{itemize}
Using this, one can deduce by  \cite[Lemma 3]{abramov2021rational} that if $\phi-\alpha$ is a right factor of order $1$ of $L$ for some  $\alpha \in \k^{\times}$, then, in the above decomposition for $\alpha$, we have $b \vert a_{0}$,   $c \vert \phi^{-2}(a_{3})$,  and 
\begin{equation}\label{eq:bla}
 \lambda^3  a_{3} b \phi(b)\phi^2 (b)  \phi^3 (r) +\lambda^2 a_{2}  b \phi(b)\phi^2 (c) \phi^2 (r)+\lambda a_{1} b \phi(c)\phi^2 (c)  \phi (r)+ a_{0} c \phi(c)\phi^2 (c) r=0.
\end{equation}


The strategy to decide whether $L$ has a right factor of order one is the following.  For every unitary pair   $(b,c)\in \left( \C[z^{1/\ell}]\setminus \{0\}\right)^2$ such that $b \vert a_{0}$,   $c \vert \phi^{-2}(a_{3})$,  we decide whether there exist $\lambda \in \C^{\times}$ and $r\in \C[z^{1/\ell}] \setminus \{0\}$ such that \eqref{eq:bla} holds. If we find a solution then we have a right factor of order one, otherwise there is no right factor of order one.
Here, since $a_0=q^3 z$, $a_3=t$ are monomials in $z$ (recall that $t\neq 0)$ the choices are very limited. The only possibilities for the pair $(b,c)$ are $(z^d,1)$, with $0\leq d\leq 1 $.   Recall that $\deg(a_3)=0$,  $\deg(a_2)=2$,  $\deg(a_1)=\deg(a_0)=1$.  
The degrees of the terms in \eqref{eq:bla} are respectively given by  
$$3d+\deg r(z), \quad 2+2d+\deg r(z), \quad 1+d+\deg r(z), \quad 1+\deg r(z)$$
and a direct calculation shows that, for $0\leq d\leq 1 $,  $2+2d+\deg r(z)$ is greater than the remaining ones, whence there is no solution.
  We proceed similarly with the dual for the left factor of length one.
  \begin{multline*}
 L^{\vee}=a_{3}(q^{-3}z)\sigmaq^{-3}  + a_{2}(q^{-2}z)\sigmaq^{-2} +a_{1}(q^{-1}z)\sigmaq^{-1} +a_{0}(z)\\
=\sigmaq^{-3}\Big(a_{3}(z)  +a_{2}(qz)\sigmaq +a_{1}(q^{2}z)\sigmaq^{2} +a_{0}(q^{3}z)\sigmaq^{3}\Big)
\end{multline*} 
Here the possible pairs for $(b,c)$ are $( 1,z^d)$, with $0\leq d\leq 1 $. The degrees of the terms of the equation corresponding to \eqref{eq:bla}  are
$$1+\deg r(z), \quad 1+d+\deg r(z), \quad 2+2d+\deg r(z), \quad 3d+ \deg r(z) .$$
Again, for $0\leq d\leq 1 $,  $2+2d+\deg r(z)$ is greater than the remaining ones.
\end{ex}
