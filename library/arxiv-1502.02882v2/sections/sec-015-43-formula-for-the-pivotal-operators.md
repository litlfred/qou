---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-015-43-formula-for-the-pivotal-operators
section_title: "Formula for the pivotal operators"
section_number: 4.3
pages: 24-25
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.843
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
\label{Form_piv_op}
We now show how to compute the pivotal operators directly in terms of the associator matrix elements. More precisely, we express them in terms of the {\em apex associator monodromy}.
\begin{defn} The {\em apex associators} are the associator matrix elements where the top strand is the identity\footnote{Thus they form a sharp angle diagrammatically, hence the name.}:
\begin{equation} \label{apex_1}
 \ig{d19.pdf} = \sum_\beta (S_{ijk})_{\beta \alpha} \ig{d20.pdf}
\end{equation}
That is, $(S_{ijk})_{\beta \alpha} = (F^1_{ijk})_{\eta_{i^*} i^* \alpha}^{\eta_k k^* \beta}$. The {\em apex associator monodromy} $A_{ijk}$ is the product of matrices $S_{jki} \, S_{kij} \, S_{ijk}$.
\end{defn}
\begin{example} In the Yang-Lee category, we read off from \eqref{yl2} that $S_{\tau\tau\tau}=1$. For category $\mathcal{E}$, we read off from \eqref{cate2} and \eqref{cate3} that  
\[
S_{xxx} = \frac{1}{\sqrt{2}} e^{\frac{7 \pi i}{12}} \left( \begin{array}{cc} 1 & -i \\ -i & i \end{array} \right)
\]
and the apex associator monodromy is $A_{xxx} = S_{xxx}^3 = \id$.
\end{example}
\begin{rem} In all examples that the author knows of, the apex associator monodromy in a fair basis is the identity.
\end{rem}

\begin{prop} In a fair basis, the cyclic operators $C_{ijk}$ compute as
\[
C_{ijk} = p_k S_{ijk}
\]
where $p_k$ is the pivotal indicator of $X_k$ and $S_{ijk}$ are the apex associators.
\end{prop}
\begin{proof}
By definition, and using the pairing convention, the bending matrix elements $(C_{ijk})_{\beta \alpha}$ are the coefficients appearing in the expansion
\[
 d_k \, \ig{d15.pdf} = \sum_\beta (C_{ijk})_{\beta \alpha} \ig{d16.pdf} \, .
\]
We can rewrite the left-hand side using the apex associators \eqref{apex_1}:
\[
 \text{LHS} = d_k \sum_\beta (S_{ijk})_{\beta \alpha} \ig{d18.pdf} = d_k a_{k^*} \sum_\beta (S_{ijk})_{\beta \alpha} \ig{d16.pdf} 
\]
The second equality uses (\ref{snake_numbers}b) and Lemma \ref{bequalsa}. In a fair basis, $d_k a_{k^*} = p_k$ and we are done.
\end{proof}
We have thus proved the following result.
\begin{cor} In a fair basis, the monodromy of the cyclic operators is the product of the pivotal indicators with the apex associator monodromy:
\begin{equation}
 T_{ijk} = p_i p_j p_k A_{ijk} . 
\end{equation}
\end{cor}
Combining this with Lemma \ref{piv_op_lem_form} gives the following explicit formula for the pivotal operators $T^i_{jk}$ in terms of the apex associator monodromy.
\begin{thm} In a fair basis, the pivotal operator $T^i_{jk}$ is equal to the product of the pivotal indicators with the conjugate of the apex-associator monodromy,  \label{formula_piv}
\begin{equation} \label{form_for_piv_ops}
 T^i_{jk} =  p_i p_j p_k Y^{-1} A_{i^* j k} Y \,.
\end{equation}
\end{thm}

\begin{rem} The above formula \eqref{form_for_piv_ops} refines a formula of Wang \cite[Prop 4.17]{wang2010-topological}, which treats the multiplicity-free case and does not include the pivotal indicators. 
\end{rem}
\begin{example} In the Yang-Lee category, $T_{\tau \tau \tau} = (-1)^3 = -1$. In category $\mathcal{E}$, all the pivotal operators are the identity. 
\end{example}
