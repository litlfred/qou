---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-017-52-satellite-knots
section_title: "Satellite knots"
section_number: 5.2
pages: 24-27
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.975
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
In this subsection we show that if $K$ is a satellite L-space knot of the same genus as $T_{p,q}$, and if $S^3_r(K) \cong S^3_r(T_{p,q})$, then $r$ must be large enough so that their common $r$-surgery is an L-space.

\begin{lemma} \label{lem:prelim-satellite-surgeries}
Suppose for some nontrivial satellite knot $K=P(C)$ and slope $r\in\Q$ that the companion torus $\partial \nu(C)$ is compressible in $S^3_r(K)$.  Then $r\neq 0$, and if $S^3_r(K)$ is irreducible then 
\begin{itemize}
\item the pattern $P \subset S^1\times D^2$ has a nontrivial $S^1\times D^2$ surgery, and is therefore a 0-bridge braid or a 1-bridge braid, with winding number $w \geq 2$ in either case;
\item $r$-surgery on the pattern $P \subset S^1\times D^2$ is a solid torus;
\item and $S^3_r(K) \cong S^3_{r/w^2}(C)$.
\end{itemize}
\end{lemma}

\begin{proof}
Since the companion torus $\partial \nu(C)$ in $S^3 \setminus \nu(K)$ compresses in $S^3_r(K)$, the result $Z$ of $r$-surgery on the pattern $P \subset S^1\times D^2$ must have compressible boundary.  Thus Gabai \cite[Theorem~1.1]{gabai-solid-tori} showed that either
\begin{itemize}
\item $Z \cong S^1\times D^2$, and $P$ is either a $0$-bridge braid or a $1$-bridge braid; or
\item $Z \cong (S^1\times D^2) \# Y$, where $Y$ is closed with $|H_1(Y)|$ finite and nontrivial.
\end{itemize}
Scharlemann \cite{scharlemann-reducible} showed that in the latter case $P$ must be a cable of a $0$-bridge braid, and $Y$ is then a lens space.  Thus in either case $P$ has nonzero winding number $w \geq 1$.

Next, we determine how the $S^1\times D^2$ summand of $Z$ is glued to the exterior of the companion $C$ to form $S^3_r(K)$.  Writing $V = S^1\times D^2$ for the solid torus containing $P$, we know from \cite[Lemma~3.3]{gordon} (plus the fact that $w \neq 0$) that in $V_r(P) \cong Z$, the peripheral class
\[ a[\{\pt\} \times \partial D^2] + bw^2[S^1\times \{\pt\}] \]
is nullhomologous.  Since $\{\pt\}\times \partial D^2$ and $S^1\times \{\pt\}$ in $\partial V$ are identified with the meridian $\mu_C$ and longitude $\lambda_C$ of $C$, respectively, it follows that the $S^1\times D^2$ summand of $Z$ fills the exterior of $C$ along a curve of slope $\frac{a}{bw^2} = \frac{r}{w^2}$.  In other words, we have
\[ S^3_r(K) \cong S^3_{r/w^2}(C) \text{ or } S^3_{r/w^2}(C) \# Y \]
depending on whether $Z$ is $S^1\times D^2$ or $(S^1\times D^2) \# Y$.

We now claim that $Z \cong S^1\times D^2$.  Indeed, if we assume instead that $Z \cong (S^1\times D^2) \# Y$, then we have seen that $S^3_r(K) \cong S^3_{r/w^2}(C) \# Y$; but $C$ being nontrivial means that $S^3_{r/w^2}(C) \not\cong S^3$, and so $S^3_r(K)$ would then be reducible.  Assuming from now on that $S^3_r(K)$ is irreducible, which is automatically satisfied if $r=0$ \cite{gabai-foliations3}, we then have $Z \cong S^1\times D^2$ as claimed, and so $S^3_r(K)$ is a Dehn filling of $C$.  It follows that
\[ S^3_r(K) \cong S^3_{r/w^2}(C), \]
and moreover that $P$ is a $0$-bridge braid or a $1$-bridge braid in $S^1\times D^2$.  The latter fact tells us that $w \geq 2$, because if we had $w=1$ then $P$ would have to be isotopic to the core of $S^1\times D^2$ and we know that it is not.

Finally, in the case $r=0$ we have $S^3_0(K) \cong S^3_0(C)$, so $g(K)=g(C)$ \cite{gabai-foliations3}.  On the other hand, since $w\geq 2$ we know that
\[ g(K) = g(P(U)) + w\cdot g(C) \geq 2g(C), \]
hence $g(C) \geq 2g(C)$ and we have a contradiction.  We conclude that $r \neq 0$ after all.
\end{proof}

\begin{lemma} \label{lem:torus-surgery-essential}
Let $T_{p,q}$ be a torus knot, with $|p|,|q| \geq 2$ relatively prime, and fix a slope $r \in \Q$.
\begin{enumerate}
\item The Dehn surgery $S^3_r(T_{p,q})$ is reducible if and only if $r=pq$. \label{i:torus-surgery-reducible}
\item If $S^3_r(T_{p,q})$ has an incompressible torus, then $r=0$ and $T_{p,q} = T_{\pm 2,3}$. \label{i:torus-surgery-atoroidal}
\end{enumerate}
\end{lemma}

\begin{proof}
Moser \cite{moser} showed that $S^3_{pq}(T_{p,q})$ is a connected sum of two lens spaces, of orders $p$ and $q$; and that if $r \neq pq$ then $S^3_r(T_{p,q})$ is small Seifert fibered with base orbifold $S^2(p,q,\Delta(pq,r))$, hence irreducible.  This establishes \eqref{i:torus-surgery-reducible}.

For \eqref{i:torus-surgery-atoroidal}, we can assume that $r \neq pq$ since a sum of lens spaces is atoroidal.  Since $S^3_r(T_{p,q})$ is small Seifert fibered it has no vertical incompressible tori, so it must be covered by $T^3$ \cite[Corollary~10.4.13]{martelli} and therefore admit a flat metric.  Up to orientation, the only such $3$-manifold with cyclic first homology is $S^3_0(T_{2,3})$, by \cite[Theorem~12.3.1]{martelli} and \cite[Proposition~10.3.38]{martelli}.  But if $S^3_r(T_{p,q}) \cong \pm S^3_0(T_{2,3})$ then $r=0$ for homological reasons, and by \cite{moser} the two sides of this identification are both Seifert fibered with base orbifolds $S^2(|p|,|q|,|pq|) \cong S^2(2,3,6)$, so we must have $\{|p|,|q|\} = \{2,3\}$ and therefore $T_{p,q}$ is a trefoil.
\end{proof}

\begin{proposition} \label{prop:compare-satellite-surgeries}
Fix a positive torus knot $T_{p,q}$, where $p,q\geq 2$ are relatively prime positive integers, and suppose for some nontrivial satellite knot $K$ and rational $r \in \Q$ that $S^3_r(K) \cong S^3_r(T_{p,q})$.  If $K$ is an L-space knot, then $r \geq 2g(K)-1$.
\end{proposition}

\begin{proof}
We write $K = P(C)$, with pattern $P$ and companion $C$.  If $r=pq$ then $S^3_r(K) \cong S^3_r(T_{p,q})$ is a connected sum of two lens spaces, of orders $p$ and $q$ \cite{moser}, so $S^3_r(K)$ is an L-space and therefore $r \geq 2g(K)-1$.  Thus we can assume from now on that $r \neq pq$.  In particular, Lemma~\ref{lem:torus-surgery-essential} says that $S^3_r(K) \cong S^3_r(T_{p,q})$ is irreducible, and that it is atoroidal unless $S^3_r(K) \cong S^3_0(T_{2,3})$.  In the latter case we must have $r=0$, and then $K$ must be fibered of genus 1 \cite{gabai-foliations3}; but the only genus-1 fibered knots are the trefoils and the figure eight, and none of these are satellites, so in fact $S^3_r(K) \cong S^3_r(T_{p,q})$ must be atoroidal.

We have now shown that the companion torus must compress in $S^3_r(K)$, so we can apply Lemma~\ref{lem:prelim-satellite-surgeries} to see that $r$-surgery on $P$ is a solid torus -- in other words, that $P$ is a \emph{Berge--Gabai knot} -- and that
\[ S^3_r(K) \cong S^3_{r/w^2}(C), \]
where $w \geq 2$ is the winding number of $P$.  As a consequence of $P$ being a Berge--Gabai knot, Lemma~\ref{lem:prelim-satellite-surgeries} tells us via \cite{gabai-solid-tori} that the pattern $P$ is either a torus knot (i.e., a $0$-bridge braid) or a $1$-bridge braid; we will handle each of these cases separately, bearing in mind that we are not interested in arbitrary $1$-bridge braids but only those with solid torus surgeries.

First, if $P$ is a torus knot then $K$ is some $(m,n)$-cable of the companion $C$, where $\gcd(m,n)=1$ and $n = w \geq 2$.  Then since $K$ is an L-space knot, Hom \cite{hom-cabling} proved that $C$ is an L-space knot and that
\[ \frac{m}{n} \geq 2g(C) - 1; \]
in fact, the inequality must be strict since $n \nmid m$, so $\frac{m-1}{n} \geq 2g(C)-1$.  Moreover, we know from \cite[Corollary~7.3]{gordon} that $S^3_r(K)$ is only irreducible and atoroidal if $r=mn\pm\frac{1}{k}$ for some $k\in\Z$, in which case
\[ S^3_r(K) \cong S^3_{r/n^2}(C). \]
Now we have
\[ \frac{r}{n^2} = \frac{mn\pm\frac{1}{k}}{n^2} \geq \frac{m}{n} - \frac{1}{n^2} \geq \frac{m-1}{n} \geq 2g(C)-1, \]
so $S^3_r(K) \cong S^3_{r/n^2}(C)$ is an L-space, hence $r \geq 2g(K)-1$.

More generally, Hom--Lidman--Vafaee \cite[Theorem~1.3]{hom-lidman-vafaee} classified the L-space satellite knots whose patterns are Berge--Gabai knots.  Each Berge--Gabai knot $P$ is described by a triple of integers
\[ (w,b,t), \qquad 0 \leq b \leq w-2, \]
which are the winding number, bridge width, and twist number of $P$ respectively; they show that $K = P(C)$ is an L-space knot if and only if $C$ is an L-space knot and $b+tw \geq w^2(2g(C)-1)$.  Moreover, if the Berge--Gabai knot $P$ is specifically a 1-bridge braid, then \cite[Lemma~2.1]{hom-lidman-vafaee} says that $r$-surgery on $P$ is a solid torus only if
\[ r = tw+d, \qquad d \in \{b,b+1\}. \]
So in this case we have
\[ \frac{r}{w^2} \geq \frac{b+tw}{w^2} \geq 2g(C)-1 \]
and hence $S^3_r(K) \cong S^3_{r/w^2}(C)$ is an L-space.  This means that $r \geq 2g(K)-1$ once again, and we are done.
\end{proof}
