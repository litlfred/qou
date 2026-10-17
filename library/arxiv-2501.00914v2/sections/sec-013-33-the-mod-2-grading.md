---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-013-33-the-mod-2-grading
section_title: "The mod 2 grading"
section_number: 3.3
pages: 17-19
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.972
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
Heegaard Floer homology has  a canonical $\Z/2\Z$ grading, with respect to which $\hfhat(Y)$ has Euler characteristic $|H_1(Y;\Z)|$ if this order is finite, and $0$ otherwise.  We will write the graded pieces as $\hfhat_\geven(Y)$ and $\hfhat_\godd(Y)$.

\begin{lemma} \label{lem:cobordism-degree}
For all $n \geq 0$, we have $\deg(F_{X^\circ_n}) = 1$ and $\deg(F_{W_{n+1}}) = 0$ with respect to the absolute $\Z/2\Z$ gradings on $\hfhat(S^3_n(K))$ and $\hfhat(S^3_{n+1}(K))$.  Therefore, each of the elements $z_{n,i}$ from \eqref{eq:zni} has odd grading.
\end{lemma}

\begin{proof}
A $\spc$ cobordism $(Z,\spint): (Y_0,\spint|_{Y_0}) \to (Y_1,\spint|_{Y_1})$ between connected, nonempty 3-manifolds induces a cobordism map on $\hfhat$ that shifts the absolute $\Z/2\Z$ grading by
\[ \deg(F_{Z,\spint}) \equiv \frac{1}{2}(\chi(Z)+\sigma(Z) + b_1(Y_1)-b_1(Y_0)) \pmod{2}. \]
This is discussed in detail for monopole Floer homology in \cite{km-book}: see \cite[\S22.4]{km-book} for the reduction of the canonical plane field grading on $\HMto(Y)$ to a canonical $\Z/2\Z$ grading, and \cite[\S25.4]{km-book} for the computation of the mod 2 degrees of cobordism maps.  In \cite[\S42.3]{km-book} this is applied to the surgery exact triangle \eqref{eq:surgery-triangle}, and the authors show that for $n\geq 0$ the map $F_{X^\circ_n}$ has odd degree while $F_{W_{n+1}}$ and the connecting homomorphism both have even degree.

In Heegaard Floer homology, Huang--Ramos \cite{huang-ramos} lifted the relative $\Z/d(c_1(\spinc))\Z$ grading on $\hf^\circ(Y,\spinc)$ (itself a lift of the absolute $\Z/2\Z$ grading) to an analogous plane field grading, and showed that this lift is compatible with the degree formula for cobordism maps, so the same formula used for $\deg(F_{Z,\spint}) \pmod{2}$ in $\HMto$ also applies to $\hfhat$.  In particular, since $\hfhat(S^3) \cong \F$ is supported in even grading, it follows that the elements $z_{n,i} = F_{X^\circ_n,\spint_{n,i}}({\bf 1})$ have odd grading.
\end{proof}

Lemma~\ref{lem:cobordism-degree} tells us that the subspaces of each $\hfhat(S^3_n(K))$ spanned by the relative invariants $z_{n,i}$ are also entirely in odd grading, i.e.,
\[ \cS_n \subset \hfhat_\godd(S^3_n(K)) \]
for all $n \geq 0$.  We can also use it to deduce the following:

\begin{proposition} \label{prop:large-odd-span}
Suppose that $K$ has genus $g \geq 1$, and fix nonnegative integers $n \leq m$ with $m \geq 2g-1$.  Then $\cS_n = \Span \{z_{n,i} \mid i\in\Z\}$ fits into a short exact sequence
\[ 0 \to \cS_n \to \hfhat_\godd(S^3_n(K)) \xrightarrow{F_{V_{n,m}}} \hfhat_\godd(S^3_m(K)) \to 0, \]
where $V_{n,m}$ is the cobordism $S^3_n(K) \to S^3_m(K)$ of \eqref{eq:vmn}.
\end{proposition}

\begin{proof}
For any $k \geq 0$, the exact triangle \eqref{eq:surgery-triangle} has the form
\[ \dots \to \hfhat(S^3) \xrightarrow{F_{X^\circ_k}} \hfhat(S^3_k(K)) \xrightarrow{F_{W_{k+1}}} \hfhat(S^3_{k+1}(K)) \xrightarrow{\delta} \dots, \]
and we recall from \cite[\S42.3]{km-book} (as noted in the proof of Lemma~\ref{lem:cobordism-degree}) that $\delta$ has even degree.  Since its codomain $\hfhat(S^3) \cong \F$ is supported in even grading, it follows that
\[ \delta\left(\hfhat_\godd(S^3_{k+1}(K))\right) = 0 \]
and hence by exactness that $\hfhat_\godd(S^3_{k+1}(K))$ lies in the image of $F_{W_{k+1}}$.  But then $F_{W_{k+1}}$ also has even degree, so $F_{W_{k+1}}$ must restrict to a surjection
\[ F_{W_{k+1}}: \hfhat_\godd(S^3_k(K)) \to \hfhat_\godd(S^3_{k+1}(K)) \]
for all $k \geq 0$.

To conclude, we observe that $F_{V_{n,m}}$ is equal to the composition
\[ F_{W_m} \circ F_{W_{m-1}} \circ \dots \circ F_{W_{n+1}} \]
of maps which are all surjective on $\hfhat_\godd$, and hence $F_{V_{n,m}}$ is surjective on $\hfhat_\godd$ as well.  Since $m \geq 2g-1$, we use Proposition~\ref{prop:ker-vmn} to say that the kernel of $F_{V_{n,m}}$ is equal to $\cS_n$.
\end{proof}

The main result of this section is now an immediate corollary:

\begin{theorem} \label{thm:trace-large-surgery}
Fix a nontrivial knot $K \subset S^3$ and an integer $n\geq 0$.  Then for all integers $m \gg 0$, the dimension of $\hfhat_\godd(S^3_m(K))$ is equal to
\[ \dim \hfhat_\godd(\partial X_n(K)) - \dim \Span \{ F_{X^\circ_n,\spint}({\bf 1}) \mid \spint \in \spc(X^\circ_n) \}. \]
In particular, $K$ is an L-space knot if and only if the elements $\{ F_{X^\circ_n,\spint}({\bf 1}) \}$ span all of $\hfhat_\godd(S^3_n(K))$.
\end{theorem}

\begin{proof}
The short exact sequence of Proposition~\ref{prop:large-odd-span} tells us that for all $m \geq \max(2g-1,n)$, the dimension of $\hfhat_\godd(S^3_m(K))$ is equal to
\[ \dim \hfhat_\godd(S^3_n(K)) - \dim \Span\{z_{n,i} \mid i\in\Z\}. \]
But this is exactly the quantity we wanted to prove equal to $\dim \hfhat_\godd(S^3_m(K))$.
\end{proof}

\begin{remark}
The proof of Theorem~\ref{thm:trace-large-surgery} applies equally well to show that $X_n(K)$ determines the odd portion of the $\Z/2\Z$-graded framed instanton homology $I^\#(S^3_m(K))$ for $m \gg 0$; in particular, the case where $I^\#_\godd(S^3_m(K)) = 0$ says that for any fixed $n\geq 0$, the $n$-trace $X_n(K)$ determines whether or not $K$ is an instanton L-space knot.  Indeed, the key Lemma~\ref{lem:fw-z} that we used to start the proof can be replaced by the original \cite[Proposition~7.1]{bs-lspace}, and then after some mild care with coefficients the rest of the argument follows in the same way.
\end{remark}

\begin{remark}
The case $n=0$ of Theorem~\ref{thm:trace-large-surgery} was used in \cite{bs-fibered-sqp} to prove that L-space knots are fibered and strongly quasipositive, as follows: we know (at least for $g\geq2$) that $\hfhat(S^3_0(K),\spinc_{g-1})$ is nonzero \cite{osz-genus}, and its Euler characteristic is zero, so the portions in even and odd gradings are both nonzero.  Theorem~\ref{thm:trace-large-surgery} says that if $K$ is an L-space knot then $\hfhat_\godd(S^3_0(K),\spinc_{g-1}) \neq 0$ must be spanned by $z_{0,g-1}=F_{X^\circ_0,\spint_{0,g-1}}({\bf 1})$; but then $\hfhat_\godd(S^3_0(K),\spinc_{g-1}) \cong \F$, and fiberedness follows.  Then $F_{X^\circ_0,\spint_{0,g-1}}({\bf 1}) \neq 0$ ultimately implies (via the Heegaard Floer contact invariant) that the open book for $S^3$ with binding $K$ supports the tight contact structure on $S^3$, and so $K$ must be strongly quasipositive.
\end{remark}
