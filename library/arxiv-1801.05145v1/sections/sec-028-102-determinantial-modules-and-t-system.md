---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-028-102-determinantial-modules-and-t-system
section_title: "Determinantial modules and T-system"
section_number: 10.2
pages: 80-81
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.825
latex_coverage_ratio: 0.957
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
We will use the materials in \S\,\ref{sec:Quantum minors and T-systems} to obtain properties on the determinantial modules.

In the rest of this paper,
we assume  that {\em  $R$ is symmetric and the base field $\ko$ is of characteristic $0$.}
Under this condition, the family of self-dual simple $R$-modules
corresponds to the upper global basis of $\An$
by Theorem \ref{thm:categorification 2}.


Let $\ch$ be the map from $K(R \gmod)$ to $\An$ obtained by composing $\iota$ and the isomorphism  \eqref{eq:KLRU} in Theorem \ref{thm:categorification 1}.

\begin{definition}
For $\lambda \in \wl^+$ and $\mu,\zeta \in W \lambda$ such that $\mu \preceq \zeta$, let $\M(\mu,\zeta)$ be a simple $R(\zeta-\mu)$-module
such that $\ch(\M(\mu,\zeta))=\D(\mu,\zeta)$.
\end{definition}
Since $\D(\mu,\zeta)$ is a member of the upper global basis,
such a module exists uniquely due to Theorem \ref{thm:categorification 2}.

The module $\M(\mu,\zeta)$ is self-dual and we call it {\em the determinantial module}.




\begin{lemma}
$\M(\mu,\zeta)$ is a real simple module.
\end{lemma}

\begin{proof}
It follows from $\ch(\M(\mu,\zeta) \conv \M(\mu,\zeta)) =\ch\big( \M(\mu,\zeta) \big)^2=q^{-(\zeta,\zeta-\mu)}\D(2\mu,2\zeta)$ which is a member of the upper global
basis up to a power of $q$.
Here the last equality follows from Corollary~\ref{cor:Duv}.
\end{proof}

\begin{prop} \label{prop: commute 1}
Let $\lambda,\mu \in \wl^+$, and $s,s',t,t' \in W$ such that $\ell(s's)=\ell(s')+\ell(s)$,
$\ell(t't)=\ell(t')+\ell(t)$, $s's \lambda \preceq t'\lambda $ and
$s'\mu \preceq t't\mu$. Then
\bnum
\item $\M(s's\lambda,t'\lambda)$ and $\M(s'\mu,t't\mu)$ commute,
\item $\La\bl\M(s's\lambda,t'\lambda),\M(s'\mu,t't\mu)\br
= (s's\lambda+t'\lambda,\;t't\mu-s'\mu)$,
\item $\tLa\bl\M(s's\lambda,t'\lambda),\M(s'\mu,t't\mu)\br
=(t'\lambda,\;t't\mu-s'\mu)$, \\
$\tLa\bl\M(s'\mu,t't\mu),\M(s's\lambda,t'\lambda)\br
=(s'\mu-t't\mu,\;s's\lambda)$.
\end{enumerate}
\end{prop}

\begin{proof}
It is a consequence of Proposition \ref{prop: BZ form}~(ii) and
Corollary \ref{cor:qcomm_module}.
\end{proof}


\begin{prop} \label{prop: weyl left right}
Let $\lambda \in \wl^+$, $\mu,\zeta \in W \lambda$
such that $\mu \preceq \zeta$ and $i \in I$.
\begin{enumerate}
\item[{\rm (i)}] If $n \seteq \lan h_i,\mu \ra \ge 0$, then
$$ \ve_i(\M(\mu,\zeta))=0 \ \ \text{ and } \ \ \M(s_i\mu,\zeta) \simeq \widetilde{F}_i^n\M(\mu,\zeta) \simeq L(i^n) \hconv \M(\mu,\zeta)
\ \text{in $R\gmod$.}$$
\item[{\rm (ii)}] If $\lan h_i,\mu \ra \le 0$ and $s_i\mu \preceq \zeta$, then $\ve_i(\M(\mu,\zeta))=-\lan h_i,\mu \ra$.
\item[{\rm (iii)}] If $m \seteq -\lan h_i,\zeta \ra  \ge  0$, then
$$ \ve^*_i(\M(\mu,\zeta))=0 \ \ \text{ and } \ \ \M(\mu,s_i\zeta) \simeq
\tF_i^{*\,m}\M(\mu,\zeta) \simeq \M(\mu,\zeta) \hconv L(i^m )
\ \text{ in $R\gmod$.}$$
\item[{\rm (iv)}] If $\lan h_i,\zeta \ra \ge 0$ and $\mu \preceq s_i\zeta$, then $\ve^*_i(\M(\mu,\zeta))=\lan h_i,\zeta \ra$.
\end{enumerate}
\end{prop}
\Proof
It is a consequence of Lemma~\ref{lem: weyl left right}.
\QED

\begin{prop}\label{prop:T}
Assume that $u,v \in W$ and $i \in I$ satisfy $u<us_i$ and $v<vs_i \le u$.
\bnum
\item
We have exact sequences
\begin{equation} \label{eq: deteminatial seq1}
\begin{aligned}
& 0 \Lto \M(u\lambda,v\lambda) \Lto q^{(vs_i\varpi_i,v\varpi_i-u\varpi_i)}\M(us_i\varpi_i,vs_i\varpi_i) \conv \M(u\varpi_i,v\varpi_i) \\
& \hspace{14ex} \Lto q^{-1+(v\varpi_i,vs_i\varpi_i-u\varpi_i)}\M(us_i\varpi_i,v\varpi_i) \conv \M(u\varpi_i,vs_i\varpi_i) \Lto 0,
\end{aligned}
\end{equation}
and
\begin{equation} \label{eq: deteminatial seq2}
\begin{aligned}
& 0 \Lto  q^{1+(v\varpi_i,vs_i\varpi_i-u\varpi_i)}  \M(us_i\varpi_i,v\varpi_i) \conv \M(u\varpi_i,vs_i\varpi_i)  \\
& \hspace{3ex} \Lto   q^{(v\varpi_i,vs_i\varpi_i-us_i\varpi_i)}  \M(u\varpi_i,v\varpi_i)\conv \M(us_i\varpi_i,vs_i\varpi_i) \Lto \M(u\lambda,v\lambda)  \Lto 0,
\end{aligned}
\end{equation}
where  $\lambda = s_i\varpi_i+\varpi_i$. 
\item
$\de\bl \M(u\varpi_i,v\varpi_i), \M(us_i\varpi_i,vs_i\varpi_i)\br=1$.
\ee
\end{prop}


\begin{proof}
Since the proof of \eqref{eq: deteminatial seq1} is similar,
let us only prove \eqref{eq: deteminatial seq2}.
(Indeed, they are dual to each other.)

Set
\eqn
&&X=q^{(v\varpi_i,vs_i\varpi_i-u\varpi_i)}  \M(us_i\varpi_i,v\varpi_i) \conv \M(u\varpi_i,vs_i\varpi_i) ,\\
&&Y=q^{(v\varpi_i,vs_i\varpi_i-us_i\varpi_i)}  \M(u\varpi_i,v\varpi_i)\conv \M(us_i\varpi_i,vs_i\varpi_i),\\
&&Z=\M(u\lambda,v\lambda).
\eneqn
Then Proposition \ref{prop: the ses} implies that
$$\ch(Y)=\ch(qX)+\ch(Z).$$
Since $X$ and $Z$ are simple and self-dual,
 our assertion follows from
Lemma~\ref{lem:short}.
\QED
