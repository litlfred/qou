---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-015-4-traces-and-rational-surgeries
section_title: "Traces and rational surgeries"
section_number: 4
pages: 19-23
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.976
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
\label{sec:rational-surgeries}
The goal of this section is to prove in Theorem~\ref{thm:trace-determines-hfhat-restated} that any trace $X_n(K)$  determines the Heegaard Floer homology of many or all rational surgeries on $K$; this quickly implies Theorem~\ref{thm:lspace-detection-main} as well. For this, we combine the results of the previous section with work of Hayden--Mark--Piccirillo, who proved in \cite[Theorem~1.4]{hayden-mark-piccirillo} that for any $n \geq 0$, the $n$-trace of a knot $K\subset S^3$ detects the Heegaard Floer $\nu$ invariant of $K$ in the following sense:

\begin{theorem} \label{thm:hmp-nu}
Suppose for two knots $J,K \subset S^3$ and some integer $n \in \Z$ that  $X_n(J) \cong X_n(K)$.  Then $\nu(J) = \nu(K)$, except possibly if $n<0$ and $\{\nu(J),\nu(K)\} = \{0,1\}$.
\end{theorem}

The recipe for extracting $\nu(K)$ from $X_n(K)$ is not very concise, but it is summarized on \cite[p.~17]{hayden-mark-piccirillo}.

Ozsv\'ath--Szab\'o \cite[Proposition~9.6]{osz-rational} proved that the $\nu$-invariants $\nu(K)$ and $\nu(\mirror{K})$ of $K$ and its mirror govern the ranks of $\hfhat$ for nonzero rational surgeries on $K$.  In \cite[Proposition~10.1]{bs-concordance} and \cite[Lemma~10.4]{bs-concordance} we reinterpreted this as follows:

\begin{proposition}\label{prop:hfhat-surgeries}
Define an integer $\hat\nu(K)$ by the formula
\begin{equation} \label{eq:hat-nu}
\hat\nu(K) = \begin{cases} \hphantom{-}\max(2\nu(K)-1,0), & \nu(K) \geq \nu(\mirror{K}) \\ {-}\max(2\nu(\mirror{K})-1,0), & \nu(K) \leq \nu(\mirror{K}). \end{cases}
\end{equation}
Then there is an integer $\hat{r}_0(K)$ such that
\[ \dim \hfhat(S^3_{p/q}(K)) = q\cdot \hat{r}_0(K) + |p-q\hat\nu(K)| \]
for all nonzero, relatively prime integers $p \neq 0$ and $q > 0$.
\end{proposition}

In fact, for nonzero integers $m \geq \hat{\nu}(K)$ the formula of Proposition~\ref{prop:hfhat-surgeries} says that
\[ \dim \hfhat(S^3_m(K)) = m + (\hat{r}_0(K) - \hat{\nu}(K)) \]
and so \eqref{eq:hfhat-odd-from-hfhat} becomes
\begin{equation} \label{eq:r-nu-hfodd}
\hat{r}_0(K) - \hat{\nu}(K) = 2\dim \hfhat_\godd(S^3_m(K)), \qquad m \gg 0.
\end{equation}
We also observe that the definition of $\hat\nu(K)$ readily implies that $\hat\nu(\mirror{K}) = -\hat\nu(K)$.

\begin{remark}
By comparing \cite[Proposition~10.1]{bs-concordance} to \cite[Proposition~9.6]{osz-rational} when $p/q$ is a large positive integer, we see that when $\nu(K) \geq \nu(\mirror{K})$, the difference $\hat{r}_0(K) - \hat{\nu}(K)$ can be extracted from $\cfkinfty(K)$ by the formula
\[ \hat{r}_0(K) - \hat{\nu}(K) = \sum_{s\in\Z} (\dim H_*(\hat{A}_s)-1), \]
where the complexes $\hat{A}_s = C\{\max(i,j-s)=0\}$ are certain subquotients of $\cfkinfty(K)$ that determine $\hfhat$ of large surgeries on $K$.
\end{remark}

\begin{lemma} \label{lem:sum-nu-mirror}
For any knot $K \subset S^3$, we have $\nu(K)+\nu(\mirror{K}) \in \{0,1\}$.  Thus if $\nu(K) \geq 1$ then $\hat\nu(K) = 2\nu(K)-1$, while $\nu(K) \leq 0$ implies that $\hat\nu(K) \leq 0$.
\end{lemma}

\begin{proof}
According to \cite[Equation~(34)]{osz-rational}, we have $\nu(K) \in \{\tau(K),\tau(K)+1\}$ and similarly for $\nu(\mirror{K})$, so
\begin{align*}
\tau(K) &\leq \nu(K) \leq \tau(K)+1 \\
\tau(\mirror{K}) & \leq \nu(\mirror{K}) \leq \tau(\mirror{K})+1.
\end{align*}
Since $\tau(\mirror{K}) = -\tau(K)$, we add these inequalities to get $0 \leq \nu(K)+\nu(\mirror{K}) \leq 2$.  In fact, the sum cannot be $2$, because this would imply that $\nu(K)=\tau(K)+1$ and $\nu(\mirror{K})=\tau(\mirror{K})+1$, and these cannot both be true by \cite[\S3]{hom-smooth-concordance}, so the sum must be either $0$ or $1$.

These inequalities immediately imply that if $\nu(K) \geq 1$ then
\[ \nu(\mirror{K}) < 2-\nu(K) \leq 1 \leq \nu(K), \]
in which case Proposition~\ref{prop:hfhat-surgeries} says that $\hat\nu(K) = \max(2\nu(K)-1,0) = 2\nu(K)-1$.  Similarly, if $\nu(K) \leq 0$ then
\[ \nu(\mirror{K}) \geq -\nu(K) \geq 0 \geq \nu(K), \]
hence $\hat\nu(K) = -\max(2\nu(\mirror{K})-1,0) \leq 0$ as claimed.
\end{proof}

\begin{lemma} \label{lem:rational-dim-nu-hfodd}
For any knot $K \subset S^3$, the pair of integers
\[ \big(\nu(K), \dim \hfhat_\godd(S^3_m(K))\big) \]
for some sufficiently large $m$ determine the values of $\dim \hfhat(S^3_r(K))$ for all positive rational $r$.
\end{lemma}

\begin{proof}
Suppose first that $\nu(K) \leq 0$, and write $r=p/q$ for some relatively prime $p,q > 0$.  Then Lemma~\ref{lem:sum-nu-mirror} says that $\hat\nu(K) \leq 0$, hence Proposition~\ref{prop:hfhat-surgeries} gives us
\begin{align*}
\dim \hfhat(S^3_r(K)) &= p + q(\hat{r}_0(K) - \hat{\nu}(K)) \\
&= p + 2q\cdot \dim \hfhat_\godd(S^3_m(K)),
\end{align*}
where the second equation comes from \eqref{eq:r-nu-hfodd}.

If instead $\nu(K) \geq 1$, then Lemma~\ref{lem:sum-nu-mirror} says that $\hat{\nu}(K) = 2\nu(K)-1$.  Once we know $\hat\nu(K)$ and $\dim \hfhat_\godd(S^3_m(K))$ for $m \gg 0$, we use \eqref{eq:r-nu-hfodd} to recover $\hat{r}_0(K)$, and then Proposition~\ref{prop:hfhat-surgeries} determines $\hfhat(S^3_r(K))$ for all nonzero $r$.
\end{proof}

We can now prove that $X_n(K)$ determines the dimension of $\hfhat(S^3_r(K))$ for all rational slopes $r$ of a given sign, and often simply for all $r\in\Q$.

\begin{theorem} \label{thm:trace-determines-hfhat-restated}
Fix an integer $n \in \Z$ and a knot $K \subset S^3$.  Given a nonzero rational number $r\in\Q$, the dimension
\[ \dim \hfhat(S^3_r(K)) \]
is completely determined by the oriented diffeomorphism type of $X_n(K)$, meaning that if $X_n(J) \cong X_n(K)$ then $\dim \hfhat(S^3_r(J)) = \dim \hfhat(S^3_r(K))$, if any one of the following conditions hold:
\begin{enumerate}
\item $n \geq 0$ and $r > 0$. \label{i:n-r-positive}
\item $n \geq 0$ and $\nu(K) \geq 1$. \label{i:n-nu-positive}
\item $n \in \Z$ and $|\nu(K)| \geq 2$. \label{i:n-nu-large}
\end{enumerate}
\end{theorem}

\begin{proof}
For case~\eqref{i:n-r-positive}, Lemma~\ref{lem:rational-dim-nu-hfodd} says it is enough to show that $X_n(K)$ determines both $\nu(K)$ and $\dim \hfhat_\godd(S^3_m(K))$ for sufficiently large $m \gg 0$.  The assumption that $n \geq 0$ guarantees that $X_n(K)$ detects each of these quantities, by Theorem~\ref{thm:hmp-nu} and Theorem~\ref{thm:trace-large-surgery}, so in these cases the proof is complete.

For cases \eqref{i:n-nu-positive} and \eqref{i:n-nu-large}, we claim that the $n$-trace $X_n(K)$ detects $\hat\nu(K)$ as long as either $\nu(K) = 1$ and $n\geq 0$, or $|\nu(K)| \geq 2$ and $n$ is arbitrary.  If $\nu(K) \geq 1$ then Theorem~\ref{thm:hmp-nu} says that $X_n(K)$ detects $\nu(K)$ as long as either $n\geq 0$ or $\nu(K) \geq 2$, and in this case we have $\hat\nu(K) = 2\nu(K)-1$ by Lemma~\ref{lem:sum-nu-mirror}, so $X_n(K)$ detects $\hat\nu(K)$.  If instead $\nu(K) \leq -2$ then Lemma~\ref{lem:sum-nu-mirror} says that 
\[ \nu(\mirror{K}) -2 \geq \nu(K)+\nu(\mirror{K}) \geq 0, \]
so $\nu(\mirror{K}) \geq 2$, and then the previous argument says that $X_{-n}(\mirror{K})$ detects $\nu(\mirror{K})$ and hence $\hat\nu(\mirror{K})=2\nu(\mirror{K})-1$ for arbitrary $n$; since $\hat\nu(K) = -\hat\nu(\mirror{K})$ and $X_n(K) \cong -X_{-n}(\mirror{K})$, it follows that if $\nu(K) \leq -2$ then $X_n(K)$ detects $\hat\nu(K)$ for all $n\in\Z$ as well.

Now if $n \geq 0$ then $X_n(K)$ detects $\dim \hfhat(S^3_m(K))$ for $m\gg0$ by Theorem~\ref{thm:trace-large-surgery}, and we have also seen that if we also have $\nu(K) \not\in \{-1,0\}$ then $X_n(K)$ also detects $\hat\nu(K)$.  According to \eqref{eq:r-nu-hfodd} these two integers are enough to recover $\hat{r}_0(K)$, and then by Proposition~\ref{prop:hfhat-surgeries} this is enough to determine $\dim \hfhat(S^3_r(K))$ for all nonzero $r\in\Q$.  This establishes case~\eqref{i:n-nu-positive}, as well as the $n\geq 0$ portion of case~\eqref{i:n-nu-large}.

Supposing now that $n<0$ but $|\nu(K)| \geq 2$, we know once again from above that $X_n(K)$ detects $\hat\nu(K)$ and hence $\hat\nu(\mirror{K}) = -\hat\nu(K)$.  Since $-n$ is positive it follows from Theorem~\ref{thm:trace-large-surgery} that $X_{-n}(\mirror{K}) \cong -X_n(K)$ detects $\dim \hfhat(S^3_m(\mirror{K}))$ for $m\gg0$, hence so does $X_n(K)$, and again by \eqref{eq:r-nu-hfodd} we conclude that $X_n(K)$ determines $\hat{r}_0(\mirror{K})$.  Now Proposition~\ref{prop:hfhat-surgeries} tells us that $X_n(K)$ determines
\begin{equation} \label{eq:reverse-r}
\dim \hfhat(S^3_r(K)) = \dim \hfhat(-S^3_r(K)) = \dim \hfhat(S^3_{-r}(\mirror{K}))
\end{equation}
for all rational $r\neq 0$, because the right side is determined by $\hat\nu(\mirror{K})$ and $\hat{r}_0(\mirror{K})$, and so this completes the remaining part of case~\eqref{i:n-nu-large}.
\end{proof}

\begin{corollary} \label{cor:0-trace-all-surgeries}
Given a knot $K \subset S^3$ and \emph{any} nonzero $r\in\Q$, the dimension $\dim\hfhat(S^3_r(K))$ is completely determined by the oriented diffeomorphism type of the $0$-trace $X_0(K)$.
\end{corollary}

\begin{proof}
If $r > 0$ then we apply case~\eqref{i:n-r-positive} of Theorem~\ref{thm:trace-determines-hfhat-restated} to $X_0(K)$.  On the other hand, if $r < 0$ then by \eqref{eq:reverse-r} it is enough to compute $\dim \hfhat(S^3_{-r}(\mirror{K}))$, and since $-r > 0$ we can recover this by applying case~\eqref{i:n-r-positive} of Theorem~\ref{thm:trace-determines-hfhat-restated} to $X_0(\mirror{K}) \cong -X_0(K)$.  In either case we see that the oriented diffeomorphism type of $X_0(K)$ determines $\dim\hfhat(S^3_r(K))$, as desired.
\end{proof}

We now prove Theorem~\ref{thm:lspace-detection-main}, which asserts that $X_n(K)$ detects whether $K$ is an L-space knot of some fixed genus.

\begin{proof}[Proof of Theorem~\ref{thm:lspace-detection-main}]
Suppose that $K \subset S^3$ is an L-space knot, and that $X_n(J) \cong X_n(K)$ for some knot $J$ and some $n \in \Z$.  If $K$ is a right-handed trefoil, then at the boundaries of these traces we have $S^3_n(J) \cong S^3_n(K)$, hence $J$ is also a right-handed trefoil by \cite{osz-characterizing} and we are done.  Since there are no other L-space knots of genus 1 \cite{ghiggini}, we assume from now on that $g(K) \geq 2$.

We now claim that $\nu(K) = g(K)$.  To see this, we recall that $\tau(K) \leq \nu(K) \leq g(K)$, where the first inequality is again \cite[Equation~(34)]{osz-rational} and the second follows from the definition of $\nu(K)$.  When $K$ is an L-space knot we have $\tau(K)=g(K)$ by \cite[Corollary~1.6]{osz-lens}, so equality must hold throughout.

Since $\nu(K) = g(K) \geq 2$, we can apply case~\eqref{i:n-nu-large} of Theorem~\ref{thm:trace-determines-hfhat-restated} to conclude that $\dim \hfhat(S^3_r(J)) = \dim \hfhat(S^3_r(K))$ for all rational $r \neq 0$.   But $S^3_r(K)$ is an L-space if and only if $r \geq 2g(K)-1$ \cite{osz-rational}, so $S^3_r(J)$ is also an L-space if and only if $r \geq 2g(K)-1$, and we conclude that $J$ is an L-space knot and that $g(J)=g(K)$.
\end{proof}

Recall from \S\ref{sec:veering} that $K \subset S^3$ is an \emph{almost L-space knot} if it satisfies
\begin{equation} \label{eq:almost-l-space-knot}
\dim \hfhat(S^3_m(K)) = m+2
\end{equation}
for all $m \gg 0$.  Since \eqref{eq:almost-l-space-knot} is equivalent (via \eqref{eq:hfhat-odd-from-hfhat}) to \[\dim \hfhat_\godd(S^3_m(K)) = 1\] for $m \gg 0$, Theorem~\ref{thm:trace-large-surgery} says that for each $n\geq 0$, the $n$-trace $X_n(K)$ detects whether $K$ is an almost L-space knot.    In fact, more is true: we further showed in \cite[Theorem~1.11]{bs-characterizing} that the only almost L-space knots of genus $1$ are the left-handed trefoil, the figure eight, and $\mirror{5_2}$; and that almost L-space knots of genus $g\geq 2$ are fibered and strongly quasipositive.  The latter implies that $(\hat{r}_0(K),\hat\nu(K))=(2g+1,2g-1)$ by \cite[Corollary~3.11]{bs-characterizing}, and moreover that $\nu(K) = g$, so now case~\eqref{i:n-nu-large} of Theorem~\ref{thm:trace-determines-hfhat-restated} yields the following.

\begin{theorem} \label{thm:almost-l-space}
Let $K$ be an almost L-space knot of genus at least 2, and suppose for some knot $J \subset S^3$ and some $n\in\Z$ that $X_n(J) \cong X_n(K)$.  Then $J$ is an almost L-space knot, and $g(J)=g(K)$.
\end{theorem}

For genus-1 almost L-space knots, we note that $\partial X_n(K) \cong S^3_n(K)$ is already enough to detect the left-handed trefoil and the figure eight \cite{osz-characterizing}, and if $n \geq 0$ then $\partial X_n(K)$ also detects $\mirror{5_2}$ \cite{bs-characterizing}.  We do not know whether $X_n(K)$ can detect $\mirror{5_2}$ when $n$ is negative.
