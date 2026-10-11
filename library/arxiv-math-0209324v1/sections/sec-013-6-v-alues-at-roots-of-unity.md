---
doc_id: arxiv-math-0209324v1
doc_title: "Cyclotomic completions of polynomial rings"
section_id: sec-013-6-v-alues-at-roots-of-unity
section_title: "V alues at roots of unity"
section_number: 6
pages: 12-14
source_pdf: 0209324v1.pdf
source_sha256: ae2ea5024a0a45e8
doc_brief: "Cyclotomic completions of polynomial rings — The main object of study in this paper is the completion Z[q]N = lim←− n Z[q]/ ((1− q)(1− q2)···(1− qn)) of the polynomial ring Z[q], which arises from"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
---
\label{sec:values-at-roots}

\begin{theorem}
  \label{thm:3}
  Let $R$ be a subring of the field $\bar\modQ $ of algebraic numbers,
  $S\subset \modN $ a $\Leftrightarrow _R$-connected subset, and $T\subset S$ a subset.  Suppose
  that for some $n\in S$ there are infinitely many elements $m\in T$ with
  $m\Leftrightarrow _Rn$.  Then the homomorphism $\tau ^R_{S,T}\zzzcolon \RqS\rightarrow P_T(R)$ is
  injective.

  In particular, if $R$ is a subring of the ring of algebraic
  integers, then, for any subset $T\subset \modN $ containing infinitely many
  prime powers, $\tau ^R_{\modN ,T}\zzzcolon \RqN\rightarrow P_T(R)$ is
  injective.
\end{theorem}

\begin{proof}
  Suppose for contradiction that there is a nonzero element $a\in \RqS$
  with $\tau ^R_{S,T}(a)=0$.  By Theorem~\ref{thm:17}, $\rho ^R_{S,\{n\}} $
  is injective, and therefore we have $\rho ^R_{S,\{n\}}(a)\neq 0$.
  Hence we can write $\rho ^R_{S,\{n\}}(a)=\sum_{j=l}^\infty a_j\Phi _n(q)^j$,
  where $l\ge 0$ and $a_j\in R[q]$ for $j\ge l$ with $a_l\not\in (\Phi _n(q))$.
  There are infinitely many elements $m_1,m_2,\ldots\in T$ with
  $m_i\Leftrightarrow _Rn$ and $n|m_i$.  For each $i$, $m_i/n$ is a power of a prime
  $p_i$ such that $R$ is $p_i$-adically separated.  It follows from
  $\tau ^R_{S,T}(a)=0$ that $\Phi _{m_i}(q)|a$ in $\RqS$ for each $i$.
  Since $R$ is an integral domain of characteristic $0$, we can show
  by induction that $\Phi _{m_1}(q)\cdots\Phi _{m_k}(q)|a$ in $\RqS$ for
  each $k\ge 0$, and hence we have $\Phi _{m_1}(q)\cdots
  \Phi _{m_k}(q)|\rho ^R_{S,\{n\}}(a)$ in $\Rqn$.  By~\eqref{eq:6} we have
  $\Phi _{m_i}(q)\in (p_i,\Phi _n(q))$ for each $i$.  Hence we have
  $\Phi _{m_1}(q)\cdots \Phi _{m_k}(q)\in (p_1\cdots p_k,\Phi _n(q))$.  In other
  words, for each $k\ge 0$, $\bar a_l= a_l\mod{(\Phi _n(q))}
  \in R[q]/(\Phi _n(q))$ is divisible by $p_1\cdots p_k$.  Note that
  $R[q]/(\Phi _n(q))=R\oplus Rq\oplus\cdots\oplus Rq^{d-1}$ with
  $d=\deg\Phi _n(q)$, and $\bar a_l$ is expressed as a polynomial in $q$
  of degree$<d$, each coefficient of which is divisible by $p_1\cdots
  p_k$ in $R$ for $k\ge 0$.  Since $R$ is a subring of $\bar \modQ $ and
  each $p_i$ is a non-unit in $R$, it follows that the coefficients of
  $\bar a_l$ are zero.  Consequently, we have $a_l\in (\Phi _n(q))$.
\end{proof}

\begin{proposition}
  \label{thm:9}
  Let $R$ be a subring of $\bar\modQ $, and $S\subset \modN $ an infinite subset.
  Then the completion $\RqS$ of $R[q]$ is {\em not} an ideal-adic
  completion, i.e., there is no ideal $I$ in $R[q]$ such that
  $\id_{R[q]}$ induces an isomorphism
  $\RqS\simeq\varprojlim_jR[q]/I^j$.
\end{proposition}

\begin{proof}
  Let $I\subset R[q]$ is a nonzero ideal, and $f(q)\in I$ a nonzero element.
  Then there are only finitely many elements $n\in S$ with $\Phi _n(q)|f(q)$.
  For each $n\in R$ the power $f(q)^j$ for $j\ge 1$ is divisible by
  $\Phi _n(q)$ if and only if $f(q)$ is divisible by $\Phi _n(q)$.  It
  follows that $f(q)^j$ does not converge to $0$ as $j\rightarrow 0$ in $R[q]$
  with the topology defining the completion $\RqS$.  Hence we have
  $\RqS\not\simeq\varprojlim_{j}R[q]/I^j$.
\end{proof}

Let $R$ be a subring of $\bar\modQ $, and let $Z\subset Z^{\bar \modQ }$ be a
subset.  Set
\[
  P_Z(R) = \prod_{\zeta \in Z}R[\zeta ],
\]
which generalize the definition of $P_Z(\modZ )$.
If $S\subset \modN $ is a subset and $Z\subset Z_S^{\bar\modQ }$, then let
\[
  \tau ^R_{S,Z}\zzzcolon \RqS\rightarrow P_Z(R)
\]
denote the homomorphism induced by $R[q]\rightarrow P_Z(R)$,
$f(q)\mapsto(f(\zeta ))_{\zeta \in Z}$.

\begin{theorem}
  \label{thm:2}
  Let $R$ be a subring of $\bar\modQ $, and let $S\subset \modN $ and
  $Z\subset Z^{\bar\modQ }_S$ be subsets.  Suppose that there is an element
  $n\in S$ such that for infinitely many $\zeta \in Z$ we have $\ord\zeta \Leftrightarrow _R n$.
  Then the homomorphism $\tau ^R_{S,Z}\zzzcolon \RqS\rightarrow P_Z(R)$ is injective.

  In particular, if $R$ is a subring of the ring of algebraic
  integers, and $Z\subset Z^{\bar\modQ }$ is a subset containing infinitely many
  elements of prime power orders, then $\tau ^R_{S,Z}\zzzcolon \RqS\rightarrow P_Z(R)$ is
  injective.
\end{theorem}

\begin{proof}
  Set $N_Z=\{\ord\zeta \zzzvert \zeta \in Z\}\subset \modN $.  Let $\gamma \zzzcolon P_{N_Z}(R)\rightarrow P_Z(R)$ be
  the homomorphism defined by
  $\gamma ((f_n(q))_{n\in N_Z})=(f_{n_\zeta }(\zeta ))_{\zeta \in Z}$.  Since $\gamma $ is the
  direct product of the injective homomorphisms
  $R[q]/(\Phi _n(q))\rightarrow \prod_{\zeta \in Z, \ord\zeta =n}R[\zeta ]$,
  $f(q)\mapsto(f(\zeta ))_\zeta $, it follows that $\gamma $ is injective.  We have
  $\tau ^R_{S,Z}=\gamma \tau ^R_{S,N_Z}$, where $\tau ^R_{S,N_Z}\zzzcolon \RqS\rightarrow P_{N_Z}(R)$
  is injective by Theorem~\ref{thm:3}.  Hence $\tau ^R_{S,Z}$ is
  injective.
\end{proof}

\begin{conjecture}
  \label{thm:5}
  For any infinite subset $Z\subset Z^{\bar\modQ }$, the homomorphism
  $\tau ^\modZ _{\modN ,Z}\zzzcolon \ZqN\rightarrow P_Z(\modZ )$ is injective.
\end{conjecture}

If $Z'\subset Z\subset Z^R$, then we have a homomorphism
\[
  \tau ^R_{Z,Z'}\zzzcolon \RqZ\rightarrow  P_Z(R),
\]
induced by $R[q]\rightarrow P_Z(R)$, $f(q)\mapsto (f(\zeta ))_\zeta $.

\begin{theorem}
  \label{thm:15}
  Let $R$ be a subring of $\bar \modQ $, let $Z\subset Z^R$ a $\Leftrightarrow _R$-connected
  subset, and let $Z'\subset Z$.  Suppose that for some $\zeta \in Z$ there are
  infinitely many elements $\xi \in Z'$ with $\xi \Leftrightarrow _R\zeta $.  Then the
  homomorphism $\tau ^R_{Z,Z'}\zzzcolon \RqZ\rightarrow P_{Z'}(R)$ is injective.
\end{theorem}

\begin{proof}
  The proof is similar to that of Theorem~\ref{thm:3} with the
  cyclotomic polynomials replaced with the polynomials $q-\zeta $ with
  $\zeta $ a roots of unity.  The details are left to the reader.
\end{proof}
