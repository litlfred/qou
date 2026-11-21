---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-011-21-the-infinite-pochhammer-symbol
section_title: "The infinite Pochhammer symbol"
section_number: 2.1
pages: 18-20
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.91
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
\label{sub.poch}

A key role in our paper is played by the infinite Pochhammer symbol
$(t;q)_\infty \= \prod_{n \geq 0} (1-q^n t)$.
In this section we collect some elementary, although remarkable, properties of it. 
There are two well-known complementary expansions of the logarithm of $(t;q)_\infty$
\begin{align}
\label{logpoc}
\log (t;q)_\infty & \= -\sum_{\ell \geq 1} \frac{t^\ell}{\ell(1-q^\ell)}

\\
\label{logpoc2}

& \= \sum_{k \geq 0} \frac{B_k}{k!} \Li_{2-k}(t) \log(1+x)^{k-1}\,,

\end{align}
where $\Li_n(t)=\sum_{k \geq 1} \tfrac{t^k}{k^n}$ is the $n$th polylogarithm and
$B_k=B_{k}(0)$ are the Bernoulli numbers given by the generating series~\eqref{bern}
with $B_0=1$, $B_1=-1/2$, etc.

These two expansions in turn imply two complementary views
of the Dwork-type difference, namely for every prime $p$, and for $q=1+x$, we have

\begin{align}
\label{logpocc}
\log(t^p;q^p)_\infty-p \log(t;q)_\infty & \=
p \sum_{\ell \geq 1, \,\, p\nmid\ell} \frac{t^\ell}{\ell(1-q^\ell)}

\\
\label{logpocd}

& \=
-p \sum_{k \geq 0} \frac{B_k}{k!} \Li_{2-k}^{(p)}(t) \log(1+x)^{k-1}\,,

\end{align}
where 
\be
\label{Lip}
\Li_n^{(p)}(t) \= \Li_n(t) - \frac{1}{p^n} \Li_n(t^p) \=
\sum_{k \geq 1, \,\, p\nmid k} \frac{t^k}{k^n} 
\ee
is the $p$-version of the polylogarithm~\cite[Prop.6.2]{Coleman}.

On the one hand, ~\eqref{logpocc} implies that the coefficient of $x^{k-1}$ in the
Dwork-type difference is in $p\BZ_{(p)}[\![t]\!]$, and on the other hand,
~\eqref{logpocd} implies that it is a $\BQ$-linear combination of the series
$\Li_{2-s}^{(p)}(t)$ for $s=0,\dots,k$. 
But in fact, more is true. In~\cite[Prop.6.2]{Coleman} Coleman proves (working with
the variable $1/t$) that $\Li_n^{(p)}(t) \in \BZ_{(p)}[\![t]\!]$ is convergent for
$|t/(1-t)|< p^{(p-1)^{-1}}$ and consequently lies in the ring
$\BZ[\tfrac{t}{1-t}]^\wedge_p$ of all series in
$\BZ_p[\![t]\!]$ that converge for $|t/(1-t)| \leq 1$. In the present paper, we will
only use a weaker statement with an elementary proof.

\begin{lemma}
\label{lem.lip}
For every integer $n$ and prime number $p$ we have
\be
\label{eq.LIP}
\Li_n^{(p)}(t) \inn \BZ[t,\tfrac{1}{1-t}]^\wedge_p \,.
\ee
\end{lemma}



\begin{proof}
For $r=1,\dots,p-1$ we have
\be
\frac{1}{r+pk} \=
r^{-1}\sum_{\ell=0}^{\infty}(-1)^\ell(r^{-1}pk)^{\ell}\inn\BZ_p\,.
\ee
This implies that for all positive integers $n$ and $N$ we have
\be
\frac{1}{(r+pk)^n} \cm \frac{1}{(r+p(k+p^N))^n} \pmod{p^N} \,.
\ee
Using equation~\eqref{Lip} and separating the summation over the
positive integers prime to $p$ into congruence classes modulo $p^N$, we obtain that
\be
\Li_n^{(p)}(t) \cm \sum_{r=1}^{p-1} \sum_{k=0}^{p^N-1}
\sum_{\ell=0}^{\infty} \frac{t^{r+pk+p^N\ell}}{(r+pk)^n}
\=
\frac{1}{1-t^{p^N}} \sum_{r=1}^{p-1} \sum_{k=0}^{p^N-1}
\frac{t^{r+pk}}{(r+pk)^n} \pmod{p^{N}}\,.
\ee
Moreover, $\frac{1}{1-t^{p^N}}\in\BZ[t,\tfrac{1}{1-t}]^\wedge_p$, which completes
the proof.
\end{proof}

\begin{proposition}
\label{prop.poclip}
\emph{(}a\emph{)} For every prime $p$ we have 
\be
\label{logpocf}
\log(t^p;q^p)_\infty-p \log(t;q)_\infty \inn
\frac{p}{x}\BZ[t,\tfrac{1}{1-t}]^\wedge_p [\![x]\!]\,,\quad q\=1+x \,.
\ee
\emph{(}b\emph{)} Fix a root of unity $\z \in \BC_p\smallsetminus \{1\}$ of order
not a power of $p$. The function
\be
\label{eq.cor.logpoc}
\log(\z^p;q^p)_{\infty}
-
p\log(\z;q)_{\infty}
\inn
p\frac{\Li_{2}^{(p)}(\z)}{x}
+p\BZ_{(p)}[\z][\![x]\!]\,,\quad q\=1+x
\ee
is meromorphic on the disc $|x|<1$ with a simple pole at $x=0$ and the residue as
given. 
\end{proposition}

\begin{proof}
Equation~\eqref{logpocf} follows from~\eqref{logpocc}, Lemma~\ref{lem.lip},
and the elementary identity
\be
\label{elem}
\BZ[t,\tfrac{1}{1-t}]^\wedge_p [\tfrac{1}{p}] \cap
\BZ_{(p)}[\![t]\!] \,\, \subseteq \,\,   \BZ[t,\tfrac{1}{1-t}]^\wedge_p \,.
\ee
Part (b) follows trivially from part (a) by applying
the natural map
\be
\BZ[t,\tfrac{1}{1-t}]^\wedge_p \to \BZ_p[\z], \qquad t \mapsto \z \,,
\ee
which is compatible with the Frobenius endomorphism $t\mapsto t^p$.
\end{proof}




















The power series expansion in equation~\eqref{logpoc2} was centred about $q=1$,
but it has an extension at all roots of unity given by
\be
\label{logpocm}
\log  (t;q)_{\infty}
\=
\sum_{j=0}^{m-1} \log (q^jt;q^m)_{\infty}
\=
\sum_{j=0}^{m-1}\sum_{k=0}^{\infty}
\frac{B_{k}(j/m)m^{k-1}}{k!}
\Li_{2-k}(\z_m^j t)\log(1+x/\z_m)^{k-1} \,,
\ee
where $q=\z_{m}+x$ and the Bernoulli polynomials $B_k(y) \in \BQ[y]$
are defined by the generating series 
\be
\label{bern}
\frac{xe^{xy}}{e^x-1} \= \sum_{k=0}^\infty \frac{B_k(y)}{k!} x^k
\ee
with $B_0(y)=1$ and $B_1(y)=y-1/2$.
