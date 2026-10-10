---
doc_id: arxiv-1103.2082v1
doc_title: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St)"
section_id: sec-012-4-a-trace-on-the-ideal-of-negligibles-in-reps0
section_title: "A trace on the ideal of negligibles in Rep(S0)"
section_number: 4
pages: 7-8
source_pdf: 1103.2082v1.pdf
source_sha256: 0ac5371486b38eac
text_source: latex
latex_prose_ratio: 0.648
latex_coverage_ratio: 0.89
doc_brief: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St) — Deligne has deﬁned a category which interpolates among the representations of the various symmetric groups."
---
\label{0trace}

We first work out the easiest example when the category is  $\uRep(S_0)$.  In this case everything can be computed explicitly.  


\subsection{Defining the Trace Function} 

Consider the indecomposable object $L(\Box)$ in the category $\uRep(S_0)$.  We will define a trace on the ideal $\ideal_{L(\Box)}$ by verifying by explicit computation that $L(\Box)$ admits an ambidextrous trace.  

 In order to define such a trace, we study the endomorphisms of the object $L(\Box)\otimes L(\Box)$.
By \cite[Proposition 6.1]{CO1} we can identify $\End(L(\Box))$ with the partition algebra $FP_1(0)$.  Hence $\End(L(\Box)\otimes L(\Box))=FP_2(0)$.  Consider the following table:
$$\includegraphics{trace1.pdf}$$
From the table above we have the following:  A linear map $\mt:\End(L(\Box))\to F$ satisfies 
$$\includegraphics{trace2.pdf}$$ for all partition diagrams $\pi\in FP_2(0)$ if and only if $\mt$ is constant on the two partition diagrams in $FP_1(0)$.  Therefore there is a unique ambidextrous trace function for $L(\Box)$ up to a constant multiple.  Hence by Theorem~\ref{T:ambitrace}  there is a unique trace on $\ideal_{L(\Box)}$ up to constant multiple.  We normalize by setting $\mt$ to be the trace function with $\mt(\id_{L(\Box)})=1$.  In summary, we have the following result.

\begin{theorem}\label{T:tzero}  There is a unique trace $\mt = \left\{\mt_{V} \right\}_{V \in \ideal_{L(\Box)}}$ on $\ideal_{L(\Box)}$ such that $\mt_{L(\Box)}(\id_{L(\Box)} )=1$.
\end{theorem}


We note that by the classification of tensor ideals in $\uRep(S_0)$ in \cite{CO2} there is a unique proper tensor ideal in the category and it contains all indecomposable objects except $L(\varnothing)$. This is the tensor ideal $\mN$ of negligible morphisms.  Using Lemma~\ref{L:ideals} it follows that there is a unique proper ideal.  That is, $\ideal_{L(\Box )}$ is the unique proper ideal and it equals $\ideal (\mN )$.


\subsection{Dimensions in the Non-Semisimple Block}\label{Dimsec}  By \cite[Theorem 6.4]{CO1} the category $\uRep(S_0)$ has a unique nontrivial block.  The indecomposables in this block can be described explicitly and are denoted by $L_n=L((1^n))$ for $n \in \Z_{\geq 0}$.   In this section we compute the modified dimensions $\md_{\mt}\left( L_n\right)$ for all $n>0$.  

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
