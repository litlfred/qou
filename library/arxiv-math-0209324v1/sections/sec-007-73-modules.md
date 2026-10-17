---
doc_id: arxiv-math-0209324v1
doc_title: "arXiv:math/0209324v1 [math.AC] 24 Sep 2002"
section_id: sec-007-73-modules
section_title: "Modules"
section_number: 7.3
pages: 16-18
source_pdf: 0209324v1.pdf
source_sha256: ae2ea5024a0a45e8
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.624
---
\label{sec:modules}

We can define cyclotomic completions also for any $\modZ $-modules as
follows.  Let $A$ be a $\modZ $-module, and let $A[q]$ denote the
$\modZ [q]$-module of polynomials in $q$ with coefficients in $A$.  For
each $S\subset \modN $ let $\AqS$ denote the completion
\[
  \AqS= \varprojlim_{f\in \PHI_S^*}A[q]/ f A[q].
\]
If $A$ is a ring, then this definition of $\AqS$ is compatible with
the previous one.  Some results in the present paper can be generalized to the
$\AqS$.

For example, Theorem~\ref{thm:17} is generalized as follows.
Let $\Leftrightarrow _A$ denote the relation on $\modN $
such that $m\Leftrightarrow _An$ if and only if either we have $A=0$, or $m/n$ is
an integer power of a prime $p$ with $A$ being $p$-adically separated.

\begin{theorem}
  \label{thm:4}
  Let $A$ be a $\modZ $-module, and let $S'\subset S\subset \modN $ be subsets.  Suppose
  that for each $n\in S$ there is a sequence $S'\ni n'\Leftrightarrow _A\cdots\Leftrightarrow _An$ in
  $S$.  Then the homomorphism
  $\rho ^A_{S,S'}\zzzcolon \AqS\rightarrow \Aq{S'}$ induced by $\id_{A[q]}$ is injective.
\end{theorem}

\begin{proof}
  One way to prove Theorem~\ref{thm:4} is to modify
  Section~\ref{sec:lemma-compl-polyn} and the proof of
  Theorem~\ref{thm:17}.  We roughly sketch the necessary
  modifications.  Section~\ref{sec:lemma-compl-polyn} is generalized
  as follows.  For two elements $f,g\in \modM _R$ and an $R$-module, we
  write $f\Rightarrow _Ag$ if $f\overset{I}\Rightarrow _Ag$ for some ideal $I$ with $A$
  being $I$-adically separated.  Then Proposition~\ref{thm:20} with
  $R$ replaced with an $R$-module $A$ holds.  Generalizations of
  Theorem~\ref{thm:21} and Corollary~\ref{thm:14} to $R$-modules is
  straightforward.  Theorem~\ref{thm:4} follows immediately from the
  generalized version of Corollary~\ref{thm:21}.

  Alternatively, we can use Theorem~\ref{thm:17} as follows.
  Since the case $A=0$ is trivial, we assume not.
  Let
  $A'=\modZ \oplus A$ be the ring with the multiplication
  $(m,a)(n,b)=(mn,mb+na)$ and with the unit $(1,0)$.  Then for
  $m,n\in \modN $ we have $m\Leftrightarrow _An$ if and only if $m\Leftrightarrow _{A'}n$.  Hence we can
  apply Theorem~\ref{thm:17} to obtain the injectivity of $\rho ^{A'}_{S,S'}$.
  We can identify $\rho ^{A'}_{S,S'}$
  with the direct product
  \[
  \rho ^{\modZ }_{S,S'}\oplus\rho ^{A}_{S,S'}\zzzcolon \ZqS\oplus\AqS\rightarrow \Zq{S'}\oplus\Aq{S'}.
  \]
  Hence $\rho ^A_{S,S'}$ is injective.
\end{proof}


\subsection{Non-surjectivity of $\rho ^\modZ _{\modN ,\{n\}}$}
\label{sec:non-surjectivity}

\begin{proposition}
  \label{thm:10}
  \begin{enumerate}
  \item If $m,n\in \modN $, $m\Leftrightarrow _\modZ n$, and $m\neq n$, then the homomorphism
    $\rho ^\modZ _{\{m,n\},\{m\}}\zzzcolon \Zq{\{m,n\}}\rightarrow \Zq{\{m\}}$ is {\em not}
    surjective.
  \item If $m|n$ and $m\neq n$, then the homomorphism
    $\rho ^\modZ _{\langle n\rangle ,\langle m\rangle }\zzzcolon \Zq{\langle n\rangle }\rightarrow \Zq{\langle m\rangle }$ is {\em not} surjective.
  \item For each nonempty, finite subset $S\subset \modN $,  the homomorphism
    $\rho ^\modZ _{\modN ,S}\zzzcolon \ZqN\rightarrow \ZqS$ is {\em not} surjective.
  \end{enumerate}
\end{proposition}

\begin{proof}
  (1) We have $m/n=p^e$ for some
  prime $p$ and an integer $e\neq 0$.  Consider the following
  commutative diagram of natural homomorphisms.
  \[
  \begin{CD}
    \Zq{\{m,n\}} @>\rho ^\modZ _{\{m,n\},\{m\}}>> \Zq{\{m\}} \\
    @VVV @VVbV \\
    \modZ [q]/(\Phi _n(q)) @>>c> \modZ _p[q]/(\Phi _n(q))
  \end{CD}
  \]
  It follows from $\modZ _p[q]/(\Phi _n(q))\simeq
  \varprojlim_j{\modZ [q]/(\Phi _n(q), p^j)}$, $\Phi _m(q)\in \sqrt{(\Phi _n(q),p)}$,
  and $p\in (\Phi _m(q),\Phi _n(q))$ that $b$ is a well-defined, surjective
  homomorphism.  Since $c$ is not surjective, $\rho ^\modZ _{\{m,n\},\{m\}}$
  is not surjective.

  (2) We may assume that $n=pm$ for a prime $p$.  The case $m=1$ is
  contained in (1) above.  There are isomorphisms
  $\Zq{\langle m\rangle }\simeq \modZ [q^m]^{\langle 1\rangle }\otimes _{\modZ [q^m]}\modZ [q]$ and
  $\Zq{\langle pm\rangle }\simeq \modZ [q^m]^{\langle p\rangle }\otimes _{\modZ [q^m]}\modZ [q]$ induced by the
  isomorphism $\modZ [q]\simeq\modZ [q^m]\otimes _{\modZ [q^m]}\modZ [q]$.  Then the case
  $m=1$ implies the non-surjectivity of $\rho ^\modZ _{\langle pm\rangle ,\langle m\rangle }$.

  (3) This follows from (2) above, since $\rho ^\modZ _{\modN ,S}$ factors
      through $\rho ^\modZ _{\langle n\rangle ,\langle m\rangle }$ for some $m,n$ with $m|n$ and
      $m\neq n$.
\end{proof}


\subsection{The ring $\QqS$}
\label{sec:structure-qqh}

The structure of $\QqS$ for $S\subset \modN $ is quite contrasting to that of $\ZqS$.
Note that $\ZqS$ embeds into $\QqS$ by Lemma~\ref{lem:1}.  (The
following remarks holds if we replace $\modQ $ with any ring $R$ such that each
element of $S$ is a unit in $R$.)

Note that if $m,n\in S$, $m\neq n$, then $(\Phi _m(q)^i,\Phi _n(q)^j)=(1)$ in
$\modQ [q]$ for any $i,j\ge 0$.  Consequently, for each
$f(q)=\prod_{n\in S}\Phi _n(q)^{\lambda (n)}\in \PHI_S^*$ with $\lambda (n)\ge 0$
we have by the Chinese Remainder Theorem
\[
\modQ [q]/(f(q)) \simeq \prod_{n\in S}\modQ [q]/(\Phi _n(q)^{\lambda (n)}).
\]
Taking the inverse limit, we obtain an isomorphism
\[
  \QqS\simeqto \prod_{n\in S}\Qqn.
\]
Since each $\Qqn$ is not zero, it follows that $\QqS$ is not an
integral domain if $|S|>1$.  It also follows
that $\rho ^\modQ _{S,S'}\zzzcolon \QqS\rightarrow \Qq{S'}$ is not
injective (but surjective) for each $S'\subsetneq S$.
Since for each $n\in S$ the
(surjective) homomorphism $\Qqn\rightarrow \modQ [q]/(\Phi _n(q))$ is not injective,
the homomorphism $\tau ^\modQ _{S,S}\zzzcolon \QqS\rightarrow \modQ [q]/(\Phi _n(q))$ is not
injective.
