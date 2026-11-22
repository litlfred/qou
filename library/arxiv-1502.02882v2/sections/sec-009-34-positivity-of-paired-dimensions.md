---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-009-34-positivity-of-paired-dimensions
section_title: "Positivity of paired dimensions"
section_number: 3.4
pages: 14-16
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.941
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
In this subsection, we show that the paired dimensions $d_{\{i,i^*\}}$ are positive real numbers.

The first step is to show that a root choice gives rise to a `twisted' homomorphism from the Grothendieck ring to $\mathbb{C}$, which is to be compared with \eqref{FPeqn}.

\begin{prop}[{cf. \cite[pg. 593]{eno02-ofc}}]\label{homprop} In any root choice $\{d_i\}$, we have 
\[
d_j d_k = \displaystyle \sum_i \Tr (T^i_{jk}) \, d_i.
\]
\end{prop}
\begin{proof} \begin{align*}
 d_j d_k &= \ba \ig{e213.pdf} \ea \\
  &= \ba \ig{e214.pdf} \ea \\
  &= \sum_{i,\alpha} \ba \ig{e215.pdf} \ea \\
 &= \sum_{i,\alpha} \epsilon^i_{jk,\alpha} d_i \quad \text{(by Lemma \ref{discomb})} \\
 &= \sum_i \Tr(T^i_{jk}) \, d_i.
  \end{align*}
\end{proof}



\begin{lem}[{cf. \cite[pg 594]{eno02-ofc}}]\label{Tsymprop} The numbers $\Tr(T^i_{jk})$ have the following symmetry properties:
 \begin{enumerate}
  \item $\Tr(T^i_{jk}) = \Tr(T^{k^*}_{i^*j}) \quad$ \text{(Conjugate cyclic)} \\
  \item $\Tr(T^i_{jk}) = \Tr(T^{i^*}_{k^*j^*}) \quad$ \text{(Conjugate symmetric)}
 \end{enumerate}
 \end{lem}
 \begin{proof} To establish (i), suppose that $\{ e_\alpha \colon X_i \rightarrow X_j \otimes X_k \}$ are eigenvectors of $T^i_{jk}$, so that $T^i_{jk} e_\alpha = \epsilon^i_{jk, \alpha} e_\alpha$. Choose arbitrary right duals $(X_i^*, \eta_i, \epsilon_i)$ and $(X_k^*, \eta_k, \epsilon_k)$ for $X_i$ and $X_k$. Then the basis for $\Hom(X_k^*, X_i^*, X_j)$ given by
  \[
   f_\alpha := \ba \ig{e216.pdf} \ea
  \]
are also eigenvectors of $T^{k^*}_{i^*, j}$ with the same eigenvalues as the $e_\alpha$, since
  \[
  T^{k^*}_{i^*, j} (f_\alpha) = \ba \ig{e217.pdf} \ea = \epsilon^i_{jk, \alpha} \ba \ig{e216.pdf} \ea = \epsilon^i_{jk,\alpha} f_\alpha.
  \]
The proof of (ii) is similar, except one uses the {\em dual} basis $\{\hat{e}_\alpha \colon X_j \otimes X_k \rightarrow X_i\}$ to define a basis $\{g_\alpha\}$ for $\Hom(X_i^*, X_k^* \otimes X_j^*)$ by setting
 \[
  g_\alpha := \ba \ig{e218.pdf} \ea.
 \]
A similar string diagram argument then establishes that $T^{i^*}_{k^*j^*} g_\alpha = \epsilon^i_{jk, \alpha} g_\alpha$.
 \end{proof}
\begin{thm}[{cf. \cite[Thm 2.3]{eno02-ofc}}]\label{realpositive} The paired dimensions $d_{\{i, i^*\}}$ are real and positive.
\end{thm}
\begin{proof} We organize the various roots $d_i \equiv \ba \ig{e288.pdf} \ea$ into a column vector:
 \[
   \mathbf{d} = \left( \ba \ig{e219.pdf} \ea, \ba \ig{e220.pdf} \ea, \ldots, \ba \ig{e221.pdf} \ea \right)^T.
 \]
Define the matrices $A_j$ via $[A_j]_{ik} = \Tr(T^k_{ji})$. Then Proposition \ref{homprop} says that $\mathbf{d}$ is a simultaneous eigenvector of each $A_j$ with eigenvalue $d_j$, i.e.
 \[
  A_j \mathbf{d} = d_j \mathbf{d}.
 \]
Thus we have $A_j A_{j^*} \mathbf{d} = d_j d_{j^*} \mathbf{d} = d_{\{j,j^*\}} \mathbf{d}$ and so $d_{\{j,j^*\}}$ is an eigenvalue of the matrix $A_j A_{j^*}$. But $A_{j^*} = A_j^T$, by the symmetry properties established in Lemma \ref{Tsymprop}:
 \begin{align*}
  [A_{j^*}]_{ik} &= \Tr(T^k_{j^* i}) \\
   &= \Tr(T^{i^*}_{k^* j^*})  \\
   &= \Tr(T^i_{jk}) \\
   &= [A_j]_{ki}.
  \end{align*}
Thus $d_{\{j,j^*\}}$ is an eigenvalue of the positive definite real matrix $A_j A_j^T$ and is therefore real and positive.
\end{proof}
\begin{rem} From now on, we will always work in the {\em canonical} root choice on a fusion category given by the positive square roots of the paired dimensions, $d_i = \sqrt{d_{\{i, i^*\}}}$. 
\end{rem}
\begin{cor}[{cf. \cite[Prop 8.21]{eno02-ofc}}] A fusion category is pseudo-unitary if and only if its Frobenius-Perron dimensions equal its fusion dimensions, that is $d^+_i = d_i$ for all $i \in I$. \label{char_pseudo_cor}
\end{cor}
\begin{proof} It suffices to show that $d_i \leq d^+_i$ for all $i \in I$. Use the Frobenius-Perron dimensions to define a norm on $\mathbb{C}^{|I|}$ by setting $\| \mathbf{x} \| = \sum_k d^+_k |x_k|$. Then we can estimate the operator norm of the operators $A_j$ from the proof of Theorem \ref{realpositive} as follows:
\begin{eqnarray*}
 \| A_j \mathbf{x} \| &=& \sum_{k} d^+_k \left| \sum_i \Tr(T^i_{jk}) x_i \right| \\
	& \leq & \sum_{k, i} d^+_k  N^i_{jk} |x_i| \\
	& = & \sum_{i,k} d^+_k N^k_{j i^*} |x_i| \\
	& = & d^+_j \sum_i d^+_{i^*} |x_i| \\
	& = & d^+_j \|x\| \, .
\end{eqnarray*}
In the second line we used $\Tr(T^i_{jk}) \leq N^i_{jk}$, in the third line the symmetry $N^i_{jk} = N^k_{ji^*}$, in the fourth line we used the definition of the Frobenius-Perron dimensions, and in the fifth line we used $d^+_{i^*} = d^+_{i}$.
\end{proof}
\begin{cor} In a pseudo-unitary fusion category, the pivotal operators $T^i_{jk}$ are the identity maps. \label{pseudo_unitary}
\end{cor}
\begin{proof} Combining eq. \eqref{FPeqn} with Proposition \ref{homprop} and Corollary \ref{char_pseudo_cor}, we have
\[
d_j d_k = \sum_i \Tr(T^i_{jk}) d_i \leq \sum_i N^i_{jk} d_i = d_j d_k
\]
and hence we must have $T^i_{jk} = \id$.
\end{proof}
