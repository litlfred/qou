---
doc_id: arxiv-math-0209324v1
doc_title: "Cyclotomic completions of polynomial rings"
section_id: sec-009-4-injectivity-of-ρr
section_title: "Injectivity of ρR"
section_number: 4
pages: 9-10
source_pdf: 0209324v1.pdf
source_sha256: ae2ea5024a0a45e8
doc_brief: "Cyclotomic completions of polynomial rings — The main object of study in this paper is the completion Z[q]N = lim←− n Z[q]/ ((1− q)(1− q2)···(1− qn)) of the polynomial ring Z[q], which arises from"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
---
\label{sec:injectivity-rs-s}

If $R$ a ring, and $S\subset \modN $ is a subset, then we have
$\RqS=\Rq{\PHI_S}$.  If $S'\subset S$, then we have
\[
\rho ^R_{S,S'}=\rho ^R_{\PHI_S,\PHI_{S'}}\zzzcolon \RqS\rightarrow \Rq{S'}.
\]

We will use the following well-known properties of cyclotomic
polynomials.
\begin{lemma}
  \label{lem:3}
  (1) Let $n\in \modN $, $p$ a prime, and $e\ge 1$.
  Then we have
  \begin{equation}
    \label{eq:6}
    \Phi _{p^en}(q)\equiv \Phi _n(q)^d \pmod{(p)},
  \end{equation}
  in $\modZ [q]$, where $d=\deg\Phi _{p^en}(q)/\deg\Phi _n(q)$.  (We have
  $d=(p-1)p^{e-1}$ if $(n,p)=1$ and $d=p^e$ if $p|n$.)

  (2) If $m,n\in \modN $, and $n/m\in \modQ $ is not an integer power of a
  prime, then we have $(\Phi _n(q),\Phi _m(q))=(1)$ in $\modZ [q]$.
\end{lemma}

For $m,n\in \modN $, we define $c_{m,n}\in \{0,1\}\cup \{p\zzzvert \text{prime}\}$ by
\begin{enumerate}
\item $c_{n,n}=0$,
\item $c_{m,n}=p$ if $p$ is a prime and $n/m=p^j$ for some
  $j\in \modZ \setminus \{0\}$, and
\item $c_{m,n}=1$ if $n/m$ is not an integer power of a prime.
\end{enumerate}
Note that $c_{m,n}=c_{n,m}$ for all $m,n\in \modN $.  It is straightforward
to see that $m\Leftrightarrow _Rn$ if and only if $R$ is $(c_{m,n})$-adically
separated.

Lemma~\ref{lem:3} implies that for each $m,n\in \modN $ we have
$\Phi _m(q)\in \sqrt {(\Phi _n(q),c_{m,n})}$ in $R[q]$, i.e.,
$\Phi _m(q)\overset{(c_{m,n})}\Rightarrow _R\Phi _n(q)$.  It follows that if $m\Leftrightarrow _Rn$,
then we have $\Phi _m(q)\Rightarrow _R\Phi _n(q)$.
Note also that if $S\subset \modN $ is
$\Leftrightarrow _R$-connected, then $\PHI_S$ is $\Rightarrow _R$-connected.  The following
follows immediately from Theorem~\ref{thm:21} and
Corollary~\ref{thm:14}.

\begin{theorem}
  \label{thm:17}
  Let $R$ be a ring and let $S'\subset S\subset \modN $.  Suppose that each connected
  component of the graph $\Gamma _R(S)$ contains at least one vertex of
  $\Gamma _R(S')$.  (In other words, for each element $n\in S$, there is a
  sequence $S'\ni n'\Leftrightarrow _R\cdots\Leftrightarrow _Rn$ in $S$.)  Then the homomorphism
  $\rho ^R_{S,S'}$ is injective.

  In particular, if $S\subset \modN $ is $\Leftrightarrow _R$-connected, then for any nonempty
  subset $S'\subset S$ the homomorphism $\rho ^R_{S,S'}\zzzcolon \RqS\rightarrow \Rq{S'}$ is
  injective.  More particularly, for any nonempty subset $S'\subset \modN $ the
  homomorphism
  $\rho ^\modZ _{\modN ,S'}\zzzcolon \ZqN\rightarrow \Zq{S'}$ is injective.
\end{theorem}

We remark that the special case of Theorem~\ref{thm:17} where $R=\modZ $,
$S=\modN $, and $S'=\{1\}$ is obtained also by P.~Vogel.  Another proof of
a special case of Theorem~\ref{thm:17} is sketched in
Remark~\ref{thm:11}.

For each $n\in \modN $ set $\langle n\rangle =\{m\in \modN \zzzvert m|n\}$.  Since
$\prod\PHI_{\langle n\rangle }=\prod_{m|n}\Phi _m(q)=q^n-1$, we have
\[
\Rq{\langle n\rangle } =\Rq{(q^n-1)} = \varprojlim_j R[q]/(q^n-1)^j.
\]
Note that the set $\langle n\rangle $ is $\Leftrightarrow _R$-connected if and only if for each
prime factor $p$ of $n$ the ring $R$ is $p$-adically separated.
A subset $S\subset \modN $ will be called {\em $R$-admissible} if $S$ is a
$\Leftrightarrow _R$-connected, directed subset of $\modN $ such that $n\in S$ implies
$\langle n\rangle \subset S$.  Note that a subset $S\subset \modN $ is finite and $R$-admissible
if and only if there is $n\in \modN $ such that $S=\langle n\rangle $ and $R$ is
$p$-adically separated for each
prime factor $p$ of $n$.  Note also
that an $R$-admissible subset $S\subset \modN $ satisfies
$S=\bigcup_{n\in S}\langle n\rangle $, and hence we have
$\RqS\simeq\varprojlim_{n\in S}\Rq{\langle n\rangle }$.
The following easily follows from Theorem~\ref{thm:17}.

\begin{corollary}
  \label{thm:16}
  Let $R$ be a ring, and let $S\subset \modN $ be $R$-admissible.
  Then for each $m,n\in S$ with
  $m|n$ the homomorphism $\rho ^R_{\langle n\rangle ,\langle m\rangle }\zzzcolon \Rq{\langle n\rangle }\rightarrow \Rq{\langle m\rangle }$ is
  injective.  Hence $\RqS$ can be regarded as the intersection
  $\bigcap_{n\in S}\Rq{\langle n\rangle }$, where the $\Rq{\langle n\rangle }$, $n\in S$, are
  regarded as $R$-subalgebras of $\Rq{\langle 1\rangle }=R[[q-1]]$.

  In particular, if $m,n\in \modN $ and $m|n$, then
  $\rho ^\modZ _{\langle n\rangle ,\langle m\rangle }\zzzcolon \Zq{\langle n\rangle }\rightarrow \Zq{\langle m\rangle }$ is injective.  We have
  $\ZqN=\bigcap_{n\in \modN }\Zq{\langle n\rangle }$.
\end{corollary}

We will see in Proposition~\ref{thm:10} that if $m|n$ and $m\neq n$,
then $\rho ^\modZ _{\langle n\rangle ,\langle m\rangle }$ is not surjective.
