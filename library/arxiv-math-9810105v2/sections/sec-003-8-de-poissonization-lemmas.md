---
doc_id: arxiv-math-9810105v2
doc_title: "arXiv:math/9810105v2 [math.CO] 26 Mar 1999"
section_id: sec-003-8-de-poissonization-lemmas
section_title: "De-Poissonization Lemmas"
section_number: 8
pages: 50-51
source_pdf: 9810105v2.pdf
source_sha256: 0a432946234949c1
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.957
---
\label{s- dep}

In this section, we present two Lemmas which show that $\phi_n(N)$ is 
a good approximation of $q_{n,N}=f_{N,n}/N!$.

We need a Lemma showing the monotonicity of $q_{n,N}$ in $N$.
The statement and proof can be found in \cite{Johan}.
\begin{lem}\label{lem-dep1}
   For all $n,N\geq 1$, 
\begin{equation*}
  q_{n,N+1} \le q_{n,N}.
\end{equation*}
\end{lem}

Using this monotonicity result, 
the following Tauberian-like ``de-Poissonization'' Lemma can be proved.
This is a modification of Lemma 2.5 in \cite{Johan} and 
the proof is the same.
\begin{lem}\label{lem-dep2}
   Let $m>0$ be a fixed real number. 
   Set $\mu_N^{(m)}=N+(2\sqrt{m+1}+1)\sqrt{N\log N}$
and $\nu_N^{(m)}=N-(2\sqrt{m+1}+1)\sqrt{N\log N}$.
Then there are constants $C=C(m)$ and $N_0=N_0(m)$ such that 
\begin{equation*}
   \phi_n(\mu_N^{(m)})-\frac{C}{N^m} \le q_{n,N}
\le \phi_n(\nu_N^{(m)})+\frac{C}{N^m}
\end{equation*}
for $N\geq N_0$, $0\le n\le N$.
\end{lem}

The reader will observe that the above Lemma is actually 
enough for all of our future calculations.  
Nevertheless, for convenience and the purpose of illustration, 
we use the following Lemma for the convergence of moments.
\begin{lem}\label{lem-dep3}
   There exists $C>0$ such that 
\begin{equation*}
    q_{n,N} \le C\phi_n(N-\sqrt{N}),\quad
1-q_{n,N} \le C\bigl(1-\phi_n(N+\sqrt{N})\bigr)
\end{equation*}
for all sufficient large $N$, $0\le n\le N$.
\end{lem}
\begin{proof}
   Note that $q_{n,N} \geq 0$. Using Lemma~\ref{lem-dep1} and 
Stirling's formula for sufficiently large $N$, we have from~\eqref{e-int4}, 
\begin{equation*}
  \begin{split}
   &\phi_n(N-\sqrt{N})
= \sum_{N'=0}^{\infty} \frac{e^{-(N-\sqrt{N})}(N-\sqrt{N})^{N'}}{(N')!} q_{n,N'}\\
   &\qquad \geq \sum_{N'\geq N-\sqrt{N}}^{N} 
\frac{e^{-(N-\sqrt{N})}(N-\sqrt{N})^{N'}}{(N')!} q_{n,N'}\\
   &\qquad \geq q_{n,N}\sum_{N'\geq N-\sqrt{N}}^{N} 
\frac{e^{-(N-\sqrt{N})}(N-\sqrt{N})^{N'}}{(N')!}\\
   &\qquad \geq C q_{n,N} \sum_{N'\geq N-\sqrt{N}}^{N} 
\frac{e^{-(N-\sqrt{N})}(N-\sqrt{N})^{N'}}{(N')^{N'+1/2}e^{-N'}}
   = C q_{n,N} \sum_{N'\geq N-\sqrt{N}}^{N} e^{f(N')}, 
  \end{split}
\end{equation*}
where $f(x)=-(N-\sqrt{N})+x\log (N-\sqrt{N}) +x-(x+\frac12)\log x$.
One can easily check that $f(x)$ is a decreasing function 
for $x\geq (N-\sqrt{N})$. Thus 
\begin{equation*}
   \phi_n(N-\sqrt{N})\geq Cq_{n,N} \sqrt{N} e^{f(N)}
=Cq_{n,N} e^{\sqrt{N}+N\log (1-1/\sqrt{N})} \geq Cq_{n,N},
\end{equation*}
for sufficiently large $N$, $0\le n\le N$.

 For the second inequality, note that $q_{n,N} \le 1$ by definition.
 Again, using Lemma~\ref{lem-dep1} and
Stirling's formula for sufficiently large $N$,
\begin{equation*}
  \begin{split}
   &1-\phi_n(N+\sqrt{N})
= \sum_{N'=0}^{\infty} \frac{e^{-(N+\sqrt{N})}(N+\sqrt{N})^{N'}}{(N')!} 
(1-q_{n,N'})\\
   &\qquad \geq C (1-q_{n,N}) \sum_{N'=N}^{N+\sqrt{N}} e^{g(N')}
  \end{split}
\end{equation*}
where $g(x)=-(N+\sqrt{N})+x\log (N+\sqrt{N}) +x-(x+\frac12)\log x$.
One can check that for $N\le x\le N+\sqrt{N}$, 
$g''(x)<0$ so that $\min g(x)=\min \bigl(g(N), g(N+\sqrt{N})\bigr)$.
If $N$ is sufficiently large, $\min \bigl(g(N), g(N+\sqrt{N})\bigr)
=g(N+\sqrt{N})=-\frac12 \log(N+\sqrt{N})$. 
Therefore 
\begin{equation*}
   1-\phi_n(N+\sqrt{N})\geq C(1-q_{n,N}) \sqrt{N} e^{g(N)}
\geq C(1-q_{n,N}),
\end{equation*}
for sufficiently large $N$, $0\le n\le N$.
\end{proof}



\bigskip
