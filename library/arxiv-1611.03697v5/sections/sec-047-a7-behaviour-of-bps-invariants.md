---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-047-a7-behaviour-of-bps-invariants
section_title: "A.7. Behaviour of BPS invariants"
section_number: null
pages: 41-43
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
Condition (V4) in Definition \ref{nick} completely describes the variation of the BPS (or equivalently DT)  invariants: if one knows the $\Omega_p(\gamma)$ at some point $p\in M$ then  they are uniquely determined at all other points $p\in M$.   This statement follows immediately from the following result.

\begin{lemma}
\label{cod}
Given a BPS structure $(\Gamma,Z,\Omega)$, the element \[\bS(\Delta)^*=\prod_{\ell\subset \Delta} \;\bS(\ell)^* \in \Hat{G}_{\Delta}\]determines
the invariants $\Omega(\gamma)$ for all classes $\gamma\in \Gamma$ satisfying $Z(\gamma)\in \Delta$.
\end{lemma}

\begin{proof}
Suppose that  $\Delta$ is the disjoint union of two subsectors $\Delta=\Delta_+\sqcup \Delta_-$ where we make the convention that $\Delta_+$ lies in the anti-clockwise direction. There is an obvious  decomposition
\[\Hat{\fg}_{\Delta}=\Hat{\fg}_{\Delta_+}\oplus \Hat{\fg}_{\Delta_-}.\]
It follows from this  that each element $g\in \Hat{G}_{\Delta}$ decomposes uniquely as a product $g=g_+\cdot g_-$ with $g_\pm\in \Hat{G}_{\Delta_{\pm}}$.  But the obvious relation
\[\bS(\Delta)^*=\bS(\Delta_+)^*\cdot\bS(\Delta_-)^*,\]
gives an example of such a decomposition, so by uniqueness it follows that $\bS(\Delta)^*$ determines the elements $\bS(\Delta_\pm)^*$. 

The  product \eqref{fin} can be thought of as corresponding  to a decomposition of $\Delta$ into a finite number of subsectors, each containing a single ray of height $<N$. Applying the first part repeatedly therefore shows that $\bS(\Delta)^*_{<N}$  determines each element $\bS(\ell)^*_{<N}$ for rays $\ell\subset \Delta$. Since this holds  for arbitrarily large $N$ it follows that $\bS(\Delta)^*$ determines the elements $\bS(\ell)^*$ for all such rays. But the elements $\bS(\ell)^*$   faithfully encode the invariants $\DT(\gamma)$  for classes $\gamma\in \Gamma$  satisfying $Z(\gamma)\in \ell$, so the result follows.
\end{proof}

\begin{remark}
\label{abelian}
Suppose given a framed variation of BPS structures $(\Gamma,Z_p,\Omega_p)$ over a manifold $M$ such that at some point  (and hence at all points) $p\in M$ the form $\<-,-\>=0$ vanishes.  Then  the Lie algebras $\Hat{\fg}_\Delta$ are abelian, and hence so too are the associated groups $\Hat{G}_\Delta$. It follows that the wall-crossing formula is satisfied if all elements $\bS_p(\ell)^*$ are taken to be constant as $p\in M$ varies. It follows from Lemma \ref{cod} that  the BPS invariants $\Omega_p(\gamma)=\Omega(\gamma)$ are constant.
 \end{remark}

One can also easily see the following statement: suppose given a framed variation of BPS structures $(\Gamma,Z_p,\Omega_p)$ over a manifold $M$. Then for any fixed class $\gamma\in \Gamma$ there is a locally-finite collection of codimension one real  submanifolds $\cW_i\subset M$ such that the invariant $\Omega(\gamma)$ is constant on the open complement \begin{equation}
\label{comp}M\setminus \bigcup \cW_i.\end{equation}
The submanifolds $\cW_i$ are called walls for the class $\gamma$, and the connected components of the complement \eqref{comp} are called chambers.
