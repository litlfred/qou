---
doc_id: arxiv-1103.2082v1
doc_title: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St)"
section_id: sec-018-52-the-object-mn
section_title: "The Object Mn"
section_number: 5.2
pages: 9-10
source_pdf: 1103.2082v1.pdf
source_sha256: 0ac5371486b38eac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.877
latex_coverage_ratio: 0.956
doc_brief: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St) — Deligne has deﬁned a category which interpolates among the representations of the various symmetric groups."
---
\label{SS:Mndef}   Let $M_n:=([n], s_n)\in\uRep(S_t)$ where $s_n$ is as in Equation~\ref{E:sndef}.  

\begin{proposition}\label{decM} We have the following results about $M_{n}$.
\begin{enumerate}
\item $M_n= L((1^n))$ in $\uRep(S_0)$ for all $n\geq 0$.
\item $M_n=L((1^n))\oplus L((1^{n-1}))$ in $\uRep(S_t)$ for all $n>0$ whenever $t\not=0$.
\end{enumerate}
\end{proposition}

\begin{proof} (1) This is \cite[Proposition 6.1]{CO1}.

(2)  Notice $\Lift_t(M_n)=([n], s_n)$ for all $t\in F$ (see \cite[\S3.2]{CO1}).  In particular, $\Lift_t(M_n)=\Lift_0(M_n)$ for all $t\in F$.  Hence, by part (1) along with \cite[Example 5.10(1), Lemma 5.20(2)]{CO1}, $\Lift_t(M_n)=L((1^n))\oplus L((1^{n-1}))$ for all $t\in F$.  
Notice that $P_{(1^n)}(x)=\frac{1}{n!}\prod_{k=1}^n(x-k)$ for all $n>0$ (see \cite[section 3.5]{CO1}).  Hence $L((1^n))$ is in a nontrivial block of $\uRep(S_t)$ if and only if $t$ is a nonnegative integer with $t\not\in\{1,\ldots, n\}$ (see \cite[Proposition 5.11]{CO1}).
If $t$ is an integer greater than $n$, then $L((1^n))$ is the minimal object in a nontrivial block of $\uRep(S_t)$ (see \cite[Corollary 5.9]{CO1}).  Hence, by \cite[Lemma 5.20(1)]{CO1}, $\Lift_t(L((1^n)))=L((1^n))$ for all $n>0$, $t\not=0$.  Therefore, by \cite[Proposition 3.12(3)]{CO1}, $M_n=L((1^n))\oplus L((1^{n-1}))$ in $\uRep(S_t)$ for all $n>0$, $t\not=0$.
\end{proof}

\begin{corollary}\label{Mneg} Suppose $t$ and $n$ are nonnegative integers with $t<n$.  Then $M_n$ is a negligible object in $\uRep(S_t)$.
\end{corollary}

\begin{proof} $M_n$ is negligible if and only if the image of $M_n$ is zero under the functor $\uRep(S_t)\to\Rep(S_t)$ (see for instance \cite[Theorem 3.24]{CO1}).  The result now follows from Proposition \ref{decM} along with \cite[Proposition 3.25]{CO1}.
\end{proof}

In the remainder of this section we examine the endomorphisms of $M_n$.  


\begin{proposition}\label{snprop} We have the following equalities.

\begin{enumerate}
\item $\sigma s_n=s_n\sigma=\sgn(\sigma)s_n$ for all $\sigma\in S_n$. 
\item  $s_n\pi s_n=0$ for all partition diagrams $\pi\not\in S_n\sqcup S_n^-$. 
\item  $s_n\sigma_i s_n=\sgn(\sigma)s_nx_n s_n$ for all $\sigma\in S_n, 1\leq i\leq n$.
\end{enumerate}
\end{proposition}

\begin{proof} Part (1) is clear.

(2) If $\pi\not\in S_n\sqcup S_n^-$ then one of the following is true:  (i) two of the top vertices of $\pi$ are in the same part; (ii) two of the top vertices of $\pi$ are in parts of size one; (iii) two of the bottom vertices of $\pi$ are in the same part; (iv) two of the bottom vertices of $\pi$ are in parts of size one.  If (i) or (ii) (resp. (iii) or (iv)) is true, then there exists a transposition $\tau\in S_n$ with $\pi\tau=\pi$ (resp $\tau\pi=\pi$).  By part (1) $\tau s_n$ (resp. $s_n\tau$) is equal to $-s_n$, hence we have   $s_n\pi s_n=s_n\pi\tau s_n=-s_n\pi s_n$ (resp, $s_n\pi s_n=s_n\tau\pi s_n=-s_n\pi s_n$).  The result follows since $F$ is not of characteristic 2.

(3) Suppose $\sigma\in S_n$ and $i\in\{1,\ldots n\}$.  If we let $\tau\in S_n$ denote the transposition $i\leftrightarrow n$, then $\tau\sigma^{-1}\sigma_i\tau=x_n$.  Hence, by part (1),  $s_n\sigma_i s_n=\sgn(\sigma^{-1})s_n\tau\sigma^{-1}\sigma_i\tau s_n=\sgn(\sigma)s_nx_n s_n$.
\end{proof}

\begin{corollary}\label{Mbasis} The set $\{s_n, s_nx_ns_n\}$ is a basis of $\End_{\uRep(S_t)}(M_n)$ for all $t\in F$, $n>0$.
\end{corollary}
