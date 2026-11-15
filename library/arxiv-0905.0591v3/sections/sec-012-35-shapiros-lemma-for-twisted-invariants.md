---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-012-35-shapiros-lemma-for-twisted-invariants
section_title: "Shapiro's lemma for twisted invariants"
section_number: 3.5
pages: 10-11
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.981
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
Let $N$ be a 3--manifold with empty or toroidal boundary.
Let $p:\hat{N}\to N$ be a finite cover of degree $d$.
Let $F$ be a free abelian group and let $\hat{\alpha}:\pi_1(\hat{N})\to \mbox{GL}(k,R[F])$ a representation.

 Now consider  the $R[F]^k$--module
 \[ \mathbb{Z}[\pi_1({N})]\otimes_{\mathbb{Z}[\pi_1(\hat{N})]} R[F]^k.\]
 If $g_1,\dots,g_d$ are representatives of $\pi_1(N)/\pi_1(\hat{N})$ and if $e_1,\dots,e_k$ is the canonical basis of $R[F]^k$,
 then it is straightforward to see that the above $R[F]$--module is a free $R[F]$--module with basis $g_i\otimes e_j, i=1,\dots,d, j=1,\dots,k$.
 The group $\pi_1(N)$ acts on
\[ \mathbb{Z}[\pi_1({N})]\otimes_{\mathbb{Z}[\pi_1(\hat{N})]} R[F]^k =R[F]^{kd}\]
via left multiplication which defines a representation $\pi_1(N)\to \mbox{GL}(kd,R[F])$ which we denote by $\alpha$.

\begin{remark}
\begin{enumerate}
\item
Let  $\hat{\gamma}:\pi_1(\hat{N})\to \mbox{GL}(k,R)$  be a  representation.
Let  $\psi:\pi_1(N)\to F$ be a non--trivial homomorphism to a free abelian group $F$.
We write $\hat{\psi}=\psi\circ p_*$ and we  denote by $\gamma$ the
 representation given by left multiplication by $\pi_1(N)$ on
\[ \mathbb{Z}[\pi_1({N})]\otimes_{\mathbb{Z}[\pi_1(\hat{N})]} R^k =R^{kd}.\]
Given $\hat{\alpha}=\hat{\gamma}\otimes \hat{\psi}$ we have in that case $\alpha=\gamma \otimes \psi$.
\item If $\hat{\gamma}$ is the trivial one--dimensional representation, and $\hat{N}$ the cover of $N$ corresponding to an epimorphism
$\varphi:\pi_1(N)\to G$ to a finite group, then we have $\gamma=\varphi$.
\end{enumerate}
\end{remark}


The following is now a variation on Shapiro's lemma (cf. \cite[Lemma~3.3]{FV08a} and \cite[Section~3]{HKL08}).

\begin{theorem}\label{thm:shapiro}
We have
\[ \tau(\hat{N},\hat{\alpha}) \doteq \tau(N,\alpha).\]
If $R$ is furthermore a  Noetherian UFD, then
\[ \Delta_{\hat{N},i}^{\hat{\alpha}} \doteq  \Delta_{N,i}^{\alpha}.\]
\end{theorem}

In its simplest form Theorem \ref{thm:shapiro} says that given an
epimorphism
$\gamma:\pi_1(N)\to G$ to a finite group the corresponding twisted Alexander polynomials of $N$ are just  untwisted Alexander polynomials of the corresponding finite cover.
