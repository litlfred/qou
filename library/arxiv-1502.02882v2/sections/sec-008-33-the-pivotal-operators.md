---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-008-33-the-pivotal-operators
section_title: "The pivotal operators"
section_number: 3.3
pages: 10-14
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.976
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
\label{piv_op_sec}
Using the pairing convention, we can diagrammatically define involutions on the fusion vector spaces.
\begin{defn} Let $\{d_i\}$ be a root choice on $\cat{C}$. The {\em pivotal operators} 
\[
T^i_{jk} \colon \Hom(X_i, X_j \otimes X_k) \rightarrow \Hom(X_i, X_j \otimes X_k)
\] 
are defined by
 \begin{equation} \label{defn_piv_operator}
  \ba \ig{e290.pdf} \ea \mapsto \ba \ig{e291.pdf} \ea.
 \end{equation}
where the pairing convention has been used.
\end{defn}
\noindent That is, to evaluate the right hand side of \eqref{defn_piv_operator}, make an arbitrary choice of right duals $(X_i^*, \eta_i, \epsilon_i)$, $(X_j^*, \eta_j, \eta_j)$ and $(X_k^*, \eta_k, \epsilon_k)$ for $X_i$, $X_j$ and $X_k$, and then choose the left dual structure maps using the pairing convention. 

Note that changing the root choice by setting $d_i \mapsto x_i d_i$ for some signs $x_i = \pm 1$ with $x_i = x_{i^*}$ will change the sign of the pivotal operators according to $T^i_{jk} \mapsto x_ix_jx_k T^i_{jk}$.


\begin{lem} \label{mat_elements} In an arbitrary trivalent basis $\{e_\alpha \colon X_i \rightarrow X_j \otimes X_k\}$ with corresponding dual basis $\{\hat{e}_\beta \colon X_j \otimes X_k \rightarrow X_i\}$ in the sense of \eqref{dual_basis}, the matrix elements of $T^i_{jk}$ compute as
 \[
 \langle \hat{e}_\beta T^i_{jk} (e_\alpha) \rangle = \frac{1}{d_i} \, \ba \ig{e295.pdf} \ea \, .
 \]
\end{lem}
\begin{proof} We can compute the scalar $ \langle \hat{e}_\beta T^i_{jk} (e_\alpha) \rangle$ by closing the loop, as in \eqref{loop_scalar}:
 \[
 \hat{e}_\beta T^i_{jk}  e_\alpha = \frac{1}{\ba \ig{e288.pdf} \ea} \ba \ig{e294.pdf} \ea = \frac{1}{d_i} \, \ba \ig{e295.pdf} \ea \, .
 \]
\end{proof}

\begin{lem} Suppose $X_i, X_j$ are simple objects and $f : X_i \otimes X_j \rightarrow X_i \otimes X_j$. Then the following equations hold in the pairing convention: \label{flip_lem}
\[
 \ba \ig{h50.pdf} \ea \stackrel{\mathrm{(a)}}{=} \ba \ig{h51.pdf} \ea \stackrel{\mathrm{(b)}}{=} \ba \ig{h52.pdf} \ea \stackrel{\mathrm{(c)}}{=} \ba \ig{h53.pdf} \ea \,.
 \]
\end{lem}
\begin{proof}
To prove (a), write 
\[
 \ba \ig{h54.pdf} \ea \, = \, \lambda \, \ba \ig{h55.pdf} \ea 
\]
for some scalar $\lambda$, as in equation \eqref{extract_scalar}, and extract the value of $\lambda$ as in equation \eqref{loop_scalar}. Inserting this back into the left hand side of (a) immediately gives the right hand side. Equation (b) is the interchange law in a monoidal category. The proof of (c) is similar to the proof of (a), but uses in addition $d_i = d_{i^*}$.
 \end{proof}
 



\begin{thm}[{cf. \cite[Thm 3]{hh09-snbfcor3}}]  The operator $T^i_{jk}$ is an involution --- that is, $(T^i_{jk})^2 = \id$. \label{piv_involution_thm}
\end{thm}
\begin{proof} The operator $T^2$ sends
 \[
  \ba \ig{e207.pdf} \ea \mapsto \ba \ig{e206.pdf} \ea .
 \]
Its matrix elements are thus:




\[
\ba \ig{e200.pdf} \ea = \ba \ig{e201.pdf} \ea
\]
\[
= \ba \ig{e202.pdf} \ea = \ba \ig{e203.pdf} \ea = \ba \ig{e204.pdf} \ea = d_i \delta^\beta_\alpha
\]
where we have used Lemma \ref{flip_lem} twice in the third equation. In other words, we have expanded $T^2(e_\alpha)$ in the basis $e_\alpha$ using the technique from eq. \eqref{expand_loop}, and we have shown that $T^2 (e_\alpha) = e_\alpha$.  
\end{proof} \noindent
\begin{rem}This calculation is essentially the {\em Dirac belt trick} proving that $\pi_1 SO(3) = \mathbb{Z}/ 2\mathbb{Z}$, and provides a link between fusion categories and spin structures, as mentioned in Remark \ref{spin_remark}. See also \cite{Douglas:2013aa} and Remark \ref{remark_2_cocycle}.
\end{rem}
\begin{rem} If $\cat{C} = \text{Rep} H$ for a semisimple Hopf algebra $H$, then the identity
$(T^i_{jk})^2 = \id$ corresponds to the Larson-Radford formula $S^2 = \id$ (see \cite{eno02-ofc} and references therein). The string diagram argument above can be regarded
as giving a graphical proof of Radford's formula.
\end{rem}
\begin{rem} The proof in \cite[Thm 3]{hh09-snbfcor3} proceeds by first passing to a strictified skeletal category equivalent to $\cat{C}$. In our approach, the pairing convention, together with our conventions on string diagrams from Section \ref{string_conventions}, allows us to work directly in the category $\cat{C}$.
\end{rem}
Since $T^i_{jk}$ is an involution, the vector space $\Hom(X_i, X_j \otimes X_k)$ has a basis of eigenvectors $e_\alpha$ whose eigenvalues are $\pm 1$. We call such a basis a {\em pivotal basis} for the fusion category $\cat{C}$.

\begin{defn} The {\em pivotal symbols} $\epsilon^i_{jk,\alpha} = \pm 1$ are the eigenvalues of the pivotal operators,  $T^i_{jk} e_\alpha = \epsilon^i_{jk, p} e_\alpha$.
\end{defn}
Thus, in a fusion category, the vector spaces $\Hom(X_i, \, X_j \otimes X_k)$ decompose into the positive and negative eigenspaces of $T^i_{jk}$, \begin{equation} \label{decomp_eqn}
\Hom(X_i, \, X_j \otimes X_k) = \Hom(X_i, \, X_j \otimes X_k)_+ \,\oplus \, \Hom(X_i, \, X_j \otimes X_k)_-
\end{equation}
Note that this decomposition is {\em canonical} since our convention will be to make the unique root choice where the $d_i$ are positive real numbers, as guaranteed by Theorem \ref{realpositive} below.
\begin{lem}\label{discomb} In a pivotal basis, the pivotal symbols can be computed as follows:
 \[
 \epsilon^i_{jk, \alpha} = \frac{1}{d_i}
  \ig{d400.pdf} \, .
  \]
\end{lem}
\begin{proof}
Follows immediately from Lemma \ref{mat_elements}.
\end{proof}
\begin{lem} The pivotal operators $T^1_{11}$ and $T^1_{i i^*}$ are the identity maps for all $i \in I$. \label{triv_pivs}
\end{lem}
\begin{proof} Follows from an elementary string diagram argument.
\end{proof}
