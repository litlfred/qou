---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-016-5-negative-traces-and-positive-torus-knots
section_title: "Negative traces and positive torus knots"
section_number: 5
pages: 23-24
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.883
latex_coverage_ratio: 0.965
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
\label{sec:torus-surgeries}
The goal of this section is to prove Theorem~\ref{thm:negtracetorus}, which we restate here as follows:

\begin{theorem} \label{thm:negtracetorus-restated}
Let $T_{p,q}$ be a positive torus knot, and suppose for some knot $K \subset S^3$ and some integer $n \leq 0$ that $X_n(K) \cong X_n(T_{p,q})$.  Then $K = T_{p,q}$.
\end{theorem}

 For $n=0$ this follows from Theorem \ref{thm:main}, since positive torus knots are L-space knots. We  prove this theorem below, assuming some propositions which we will establish later in this section:


\begin{proof}[Proof of Theorem \ref{thm:negtracetorus-restated}]
Comparing the boundaries of the traces, we must have $S^3_n(K) \cong S^3_n(T_{p,q})$.  Thus if either $K$ or $T_{p,q}$ is unknotted then the other one must be as well, because all slopes are characterizing for the unknot \cite{kmos}.  From now on we assume that both knots are nontrivial, and we observe that since $T_{p,q}$ is an L-space knot, Theorem~\ref{thm:lspace-detection-main} says that $K$ must also be an L-space knot -- in particular, it is fibered \cite{ghiggini,ni-hfk} -- and that $g(K) = g(T_{p,q})$.

We know from geometrization for Haken manifolds that $K$ must be either a torus knot, a satellite knot, or a hyperbolic knot \cite[Corollary~2.5]{thurston-kleinian}.  In each case, the identification $S^3_n(K) \cong S^3_n(T_{p,q})$ will give us a contradiction:
\begin{itemize}
\item Proposition~\ref{prop:compare-torus-surgeries} says that if $K \neq T_{p,q}$ is a torus knot, then $g(K) \neq g(T_{p,q})$.
\item Proposition~\ref{prop:compare-satellite-surgeries} says that if $K$ is a satellite L-space knot, then $n \geq 2g(K)-1$.
\item Proposition~\ref{prop:compare-hyperbolic-surgeries} says that if $K$ is a hyperbolic L-space knot then $0 < n < 4g(K)$.
\end{itemize}
Since $K$ is indeed an L-space knot and $g(K) = g(T_{p,q})$, this means that the only way we can have $X_n(K) \cong X_n(T_{p,q})$ for any $n \leq 0$ is if $K = T_{p,q}$.
\end{proof}

The following subsections are dedicated to the proofs of Propositions~\ref{prop:compare-torus-surgeries}, \ref{prop:compare-satellite-surgeries}, and \ref{prop:compare-hyperbolic-surgeries}.






\subsection{Torus knots}

It is possible for two different torus knots to have a common surgery; in Appendix~\ref{sec:torus-pairs} we will prove Theorem~\ref{thm:torus-pairs}, providing a two-parameter family of examples where the resulting 3-manifold is always a lens space.  However, in these examples we are about to show that the torus knots in question cannot have the same Seifert genus, so Theorem~\ref{thm:lspace-detection-main} will tell us that the corresponding traces must be different.

\begin{proposition} \label{prop:compare-torus-surgeries}
Suppose for some $r \in \Q$ and some nontrivial torus knots $T_{a,b} \neq T_{c,d}$ that $S^3_r(T_{a,b}) \cong S^3_r(T_{c,d})$.  Then $r\neq 0$ and $g(T_{a,b}) \neq g(T_{c,d})$.
\end{proposition}

\begin{proof}
Let $A,B,C,D$ denote the absolute values of $a,b,c,d$ for convenience.  The case $r=0$ is ruled out by Lemma~\ref{lem:torus-knots-different-0-surgery}, so we will suppose that $r \neq 0$; then we can apply the surgery formula for the Casson--Walker invariant \cite{walker}, which says that
\[ \lambda(S^3_r(K)) = \lambda(S^3_r(U)) + \frac{1}{r}\frac{\Delta''_K(1)}{2}. \]
Since $S^3_r(T_{a,b}) \cong S^3_r(T_{c,d})$, it follows that
\[ \tfrac{1}{2}\Delta''_{T_{a,b}}(K) = \tfrac{1}{2}\Delta''_{T_{c,d}}(K). \]
These values are known explicitly: one can show as in, for example, \cite[Appendix~A]{mccoy-pretzel} that
\begin{equation} \label{eq:torus-casson}
\frac{\Delta_{T_{a,b}}''(1)}{2} = \frac{(a^2-1)(b^2-1)}{24} = g(T_{a,b}) \cdot \frac{(A+1)(B+1)}{12},
\end{equation}
and likewise for $T_{c,d}$.

If we assume that $g(T_{a,b}) = g(T_{c,d})$, then we get the system of equations
\begin{align}
(A-1)(B-1) &= (C-1)(D-1) \label{eq:torus-g-equal} \\
(A+1)(B+1) &= (C+1)(D+1) \label{eq:torus-g-plus}
\end{align}
where \eqref{eq:torus-g-equal} is equivalent to $2g(T_{a,b})=2g(T_{c,d})$, and \eqref{eq:torus-g-plus} comes from applying \eqref{eq:torus-casson} to $\Delta_{T_{a,b}}''(1) = \Delta_{T_{c,d}}''(1)$ and then dividing by \eqref{eq:torus-g-equal}.  Subtracting \eqref{eq:torus-g-equal} from \eqref{eq:torus-g-plus} gives us
\[ 2(A+B) = 2(C+D), \]
so $A+B=C+D$, and if we add this to \eqref{eq:torus-g-equal} then we get $AB=CD$ as well.  Now we have $\{A,B\} = \{C,D\}$, because these are the sets of roots of the quadratic polynomials
\[ x^2 - (A+B)x + AB = x^2 - (C+D)x + CD, \]
so it must be the case that $T_{c,d} = T_{-a,b}$.

We have now shown that $\{T_{a,b},T_{c,d}\} = \{T_{A,B},T_{-A,B}\}$, and thus
\[ S^3_r(T_{A,B}) \cong S^3_r(T_{-A,B}) \cong -S^3_{-r}(T_{A,B}). \]
The dimension of $\hfhat$ is preserved by orientation reversal, so it follows that
\begin{equation} \label{eq:hfhat-pm-r}
\dim \hfhat(S^3_r(T_{A,B})) = \dim \hfhat(S^3_{-r}(T_{A,B})).
\end{equation}
Since $T_{A,B}$ is an L-space knot of genus $g = g(T_{a,b})$, we have
\[ \hat{r}_0(T_{A,B}) = \hat\nu(T_{A,B}) = 2g-1, \]
see e.g.\ \cite[Remark~10.9]{bs-concordance}.  Writing $r = p/q$ for coprime integers $p,q$ with $p\neq 0$ and $q > 0$, we apply Proposition~\ref{prop:hfhat-surgeries} to \eqref{eq:hfhat-pm-r} to see that
\[ q(2g-1) + |p-q(2g-1)| = q(2g-1) + |{-p}-q(2g-1)|, \]
which simplifies to
\[ p-q(2g-1) = \pm(p+q(2g-1)). \]
But this is only possible if either $p=0$ or $q=0$, and in either case we have a contradiction.  Thus we must have had $g(T_{a,b}) \neq g(T_{c,d})$ after all.
\end{proof}
