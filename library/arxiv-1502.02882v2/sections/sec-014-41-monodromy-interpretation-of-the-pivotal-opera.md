---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams Bruce Bartlett"
section_id: sec-014-41-monodromy-interpretation-of-the-pivotal-opera
section_title: "Monodromy interpretation of the pivotal operators"
section_number: 4.1
pages: 21-24
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
doc_brief: "Fusion categories via string diagrams Bruce Bartlett — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.905
---
We can write the pivotal operators $T^i_{jk}$ as the conjugate of a product of {\em cyclic operators}, defined as follows. Write $V_{ijk} = \Hom(1, X_i \otimes (X_j \otimes X_k))$.
\begin{defn} In a fusion category, the {\em cyclic operators} $C_{ijk} : V_{ijk} \rightarrow V_{kij}$ are defined as follows, using the pairing convention: \label{cyclic_op_defn}
\[
 \ba \ig{c5.pdf} \ea \mapsto \ba \ig{c6.pdf} \ea 
\]
The {\em monodromy} of the cyclic operators is the operator $T_{ijk}$ on $V_{ijk}$ given as the composite
\[
  T_{ijk} = V_{ijk} \stackrel{C_{ijk}}{\longrightarrow} V_{kij} \stackrel{C_{kij}}{\longrightarrow} V_{jki}  \stackrel{C_{jki}}{\longrightarrow} V_{ijk} \, .
\]
\end{defn} 
Write $Y$ and $Y^{-1}$ for the `yanking' maps
\[
 Y : \Hom(X_i, X_j \otimes X_k) \rightleftarrows \Hom(1, X_i^* \otimes X_j \otimes X_k)
\]
defined by making some choice of structure maps equipping $X_i^*$ as the right dual of $X_i$. The following lemma is immediate.
\begin{lem} The pivotal operator $T^i_{jk}$ computes as the conjugate of the monodromy of the cyclic operators: \label{piv_op_lem_form}
\[
T^i_{jk} = Y^{-1} T_{i^* j k} Y 
\]
\end{lem}
Note that the statement of the lemma is well-defined since the right-hand side is independent of the right dual structure maps needed to define $Y$ (the dependency cancels due to the $Y^{-1}$). 








\begin{rem} In the special case  $i=j=k$, the trace of the cyclic operator $C_{iii}$ is closely related, but not equal, to the 3rd Frobenius-Schur indicator $\nu_3(X_i)$ of $X_i$, as defined in \cite{ng2005higher}. The indicator $\nu_3(X_i)$ needs a pivotal structure $\gamma$ for its definition, whence we will write it as $\nu_3^\gamma(X_i)$, whereas the cyclic operator $C_{iii}$ is well-defined on the underlying fusion category. The 3rd Frobenius-Schur indicator $\nu_3^\gamma(X_i)$ is defined as the trace of an operator whose graphical formula is identical to the inverse of the formula for $C_{iii}$ in Definition \ref{cyclic_op_defn}, except it is to be interpreted using the pivotal structure $\gamma$ instead of the pairing convention. Hence on simple objects $X_i$ the relationship is 
\[
\nu_3^\gamma (X_i) = \gamma_i \Tr(C_{iii})
\]
where $\gamma_i \in U(1)$ are the scalars defining the pivotal structure (see Section \ref{Explicit_equations}). 
 \label{remark_frobenius}
\end{rem}



\subsection{The pivotal indicators \label{piv_ind_sec}} 
In this subsection we compute the paired dimensions explicitly and define the {\em pivotal indicators}. 

Let $\cat{C}$ be a fusion category, with representative simple objects $X_i$, $i \in I$. The right duality induces a map $* : I \rightarrow I$ with $**=\id$. Choose for each $i \in I$ a nonzero map $\eta_i : 1 \rightarrow X_{i^*} \otimes X_i$:
\[
\ig{d1.pdf}
\]
Define $\hat{\eta_i} : X_{i^*} \otimes X_i \rightarrow 1$ as the linear dual of $\eta_i$, so that
\[
\ig{d5.pdf} = 1
\]
for all $i \in I$. 
Define the complex numbers $a_i$ as the coefficients appearing in the associator expansion
\begin{equation}
\ig{d2.pdf} \, = a_i \! \ig{d3.pdf} \quad + \text{ other terms}.
\end{equation}
Similarly define $b_i$ as the coefficients appearing in the inverse associator expansion
\begin{equation}
\ig{d3.pdf} \, = \,\, b_i \! \ig{d2.pdf} \quad + \text{ other terms}.
\end{equation}
Clearly, these coefficients are precisely the numbers appearing in
\begin{equation} \label{snake_numbers}
\ig{d8.pdf} = a_i \, \ig{d9.pdf} \, , \quad \quad \ig{d10.pdf} = b_i \, \ig{d11.pdf} \, .
\end{equation}
In particular, they are nonzero as $\cat{C}$ is rigid (if they were zero, it would be impossible to choose counit maps satisfying the rigidity equations).
\begin{example} In the Yang-Lee category, we read off from \eqref{yl1} that $a_\tau = - \frac{1}{2}(1 + \sqrt{5})$. In category $\mathcal{E}$, we read off from \eqref{cate1} that $a_x = 1 + \sqrt{3}$; similarly $a_y = 1$.
\end{example}
\begin{lem} $b_{i} = a_{i^*}$ for all $i \in I$. \label{bequalsa}
\end{lem}
\begin{proof} Adapted from \cite[Prop 5.3.13]{bk01-ltc}.  Consider evaluating the morphism
\[
\ig{d12.pdf}
\]
in two different ways. On the one hand, by dragging the right-most $\eta_i$ downwards, and then using (\ref{snake_numbers}a), it equals $a_i \eta_i$. On the other hand, by dragging the left-most $\eta_i$ downwards, and then using (\ref{snake_numbers}b), it equals $b_{i^*} \eta_i$. Hence $a_i = b_{i^*}$.
\end{proof}
For each $i \in I$, define $\epsilon_i : X_i \otimes X_{i^*} \rightarrow 1$ by
\[
\ig{d6.pdf} = \frac{1}{a_i} \ig{d7.pdf} \, .
\]
We have just proved the following:
\begin{lem} For each $i \in I$, $(\eta_i, \epsilon_i)$ satisfy the rigidity equations furnishing $X_{i^*}$ as a right dual of $X_i$. 
\end{lem}
\begin{cor} The paired dimensions compute as $\displaystyle d_{\{i,i^*\}} = \frac{1}{a_{i^*}a_i}$. \label{paired_cor}
\end{cor}
\begin{lem} There exists a choice of basis of the $\eta_i$ such that $a_i = a_{i^*}$ for all $i \in I$.
\end{lem}
\begin{proof}
If $X_i$ is self-dual, then $i = i^*$ so we are done. Partition the non self-dual objects into ordered pairs $(X_i, X_{i^*})$. Scale the $\eta_i$ by setting $\eta'_i = \eta_i$ and $\eta'_{i^*} = \lambda_i \eta_{i^*}$ where $\lambda_i$ is a root of $\displaystyle \lambda_i^2 = \frac{a_i}{a_{i^*}}$. In this new basis we have $a'_i = a'_{i^*}$.
\end{proof}
In such a basis we have $a_i^{-2} = d_{\{i, i^*\}}$ for all $i \in I$. By Theorem \ref{realpositive}, the paired dimension $d_{\{i, i^*\}}$ is a positive real number, with the fusion dimension $d_i$ defined as its positive square root. Hence $\displaystyle a_i = \pm \frac{1}{d_i}$. If $X_i$ is not self-dual and $a_i = - d_i$, then we can remove this sign by setting $\eta'_i = -\eta_i$, $\eta'_{i^*} = \eta_{i^*}$, after which we have $a'_i = d_i$. We call such a basis choice $\eta_i \in \Hom(1, X_{i^*} \otimes X_i)$ satisfying $a_i > 0$ for all non self-dual $X_i$ a {\em fair basis}. 

Note that if $X_i$ is self-dual then this sign cannot be removed. We record this as a definition.

\begin{defn} Let $\cat{C}$ be a fusion category over $\mathbb{C}$. The {\em pivotal indicator} $p(X_i)$ of a simple object $X_i$ is defined as follows. If $X_i$ is not self-dual, $p(X_i) = 1$. If $X_i$ is self-dual, then $p(X_i)$ is the sign of the coefficient $a_i$ appearing in the associator expansion
\[
\ig{d13.pdf} = a_i \! \ig{d14.pdf} \quad + \text{ other terms}.
\]
where $\eta_i : 1 \rightarrow X_i \otimes X_i$ is some nonzero vector (the number $a_i$ is independent of this choice).
\end{defn}
\begin{example} In the Yang-Lee category, we read off from \eqref{yl1} that $p(\tau) = -1$. In category $\mathcal{E}$, we read off from \eqref{cate1} that $p(x)=1$, similarly $p(y)=1$.
\end{example}

\begin{rem} As in Remark \ref{remark_frobenius}, the pivotal indicator $p(X_i)$ of a self-dual simple object is closely related, but not equal to, the 2nd Frobenius-Schur indicator $\nu_2(X_i)$ of a self-dual simple object, as defined in \cite{ng2005higher}. The former is defined using only the underlying fusion category, while the latter depends on a pivotal structure $\gamma$, whence we can write it as $\nu_2^\gamma (X_i)$. The precise relationship is 
\[
 \nu_2^\gamma (X_i) = \gamma_i p(X_i)
\]
where $\gamma_i = \pm 1$ is the sign associated to the self-dual object $X_i$ in the pivotal structure $\gamma$ (see Section \ref{Explicit_equations}).
\end{rem}
