---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-024-42-statement-of-the-problem
section_title: "Statement of the problem"
section_number: 4.2
pages: 17-18
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
\label{real}
 



Let $(\Gamma, Z, \Omega)$ be a convergent BPS structure, and denote by $\bT$ the associated twisted torus. Given a ray $\rr\subset \bC^*$ we consider the corresponding half-plane
\[\bH_\rr=\{t\in \bC^*:t=z\cdot v \text{ with } z\in \rr\text{ and }\Re(v)>0\}\subset \bC^*\]
centered on it.
We shall be dealing with functions of the form \[\Phi_\rr\colon \bH_\rr\to  \bT.\] Composing with the twisted characters of $\bT$ we can equivalently consider functions
\[\Phi_{\rr,\gamma}\colon \bH_\rr\to \bC^*,\qquad \Phi_{\rr,\gamma}(t)=x_\gamma(\Phi_\rr(t)).\]

The Riemann-Hilbert problem associated to the BPS structure $(\Gamma, Z, \Omega)$ depends on a choice of element $\xi\in \bT$ which we call the constant term. It reads as follows:



\begin{problem}
\label{dtsect}
Fix an element $\xi\in \bT$. For each non-active ray $\rr\subset \bC^*$, we  seek a holomorphic function
$\Phi_\rr\colon \bH_\rr\to \bT$
such that the following three conditions are satisfied:
\begin{itemize}

\item[(RH1)] {\it Jumping.} Suppose that two  non-active rays $\rr_-,\rr_+\subset \bC^*$ form the  boundary rays of a convex sector $\Delta\subset \bC^*$, taken in clockwise order. Then
\[\Phi_{\rr_+}(t)= \bS(\Delta)( \Phi_{\rr_-}(t)), \]
for all $t\in \bH_{\rr_-}\cap \bH_{\rr_+}$ with  $ 0<|t|\ll 1$.
\smallskip

\item[(RH2)] {\it Finite limit at $0$}.
For each non-active ray $\rr\subset \bC^*$, and each class $\gamma\in \Gamma$, we have
\[\exp(Z(\gamma)/t)\cdot \Phi_{\rr,\gamma}(t) \to \xi(\gamma)\]
as $t\to 0$ in the half-plane $\bH_\rr$.\smallskip

\item[(RH3)] {\it Polynomial growth at $\infty$}. For any class $\gamma\in \Gamma$, and any non-active ray $\rr\subset \bC^*$, there exists $k>0$ such that
\[|t|^{-k} < |\Phi_{\rr,\gamma}
(t)|<|t|^k,\]
for  $t\in \bH_\rr$ with  $|t|\gg 0$.
\end{itemize}
\end{problem}

 
To make sense of the condition (RH1) note that by Proposition \ref{barneyy} we can find  $R>0$ such that the partially-defined automorphism $\bS(\Delta)$ is well-defined on the open subset $U_{\Delta}(R)\subset \bT$. Observe that if an active class $\gamma\in \Gamma$ satisfies $Z(\gamma)\in \Delta$, and we take $t\in \bH_{\rr_1}\cap \bH_{\rr_2}$, then the quantity $Z(\gamma)/t$ has strictly positive real part.  Using the support property it follows (see the proof of Lemma \ref{dyl}) that for  $ 0<|t|\ll 1$
\[\exp(-Z/t)\cdot \xi\in U_\Delta(R).\]
Condition (RH2) then implies that  $\Phi_{\rr_i}(t)\in U_\Delta(R)$ whenever  $t\in \bH_{\rr_1}\cap \bH_{\rr_2}$ with  $ 0<|t|\ll 1$, so that 
 the  relation (RH1) is indeed well-defined.

\begin{remark}
\label{wet}
When the BPS structure $(\Gamma,Z,\Omega)$ is finite, integral and generic, we can rewrite the condition (RH1) using Proposition \ref{barneyy}. Given an active ray $\ell$, consider a small anticlockwise perturbation $\rr_-$, and  a small clockwise perturbation $\rr_+$, both rays being  non-active.  Then  (RH1) is the condition that
\begin{equation}
\label{garage}\Phi_{\rr_+,\beta}(t)=\Phi_{\rr_-,\beta}(t)\cdot \prod_{Z(\gamma)\in \ell}   (1-\Phi_{\rr_{\pm,\gamma}}(t))^{\Omega(\gamma)\<\gamma,\beta\>}.\end{equation}
Note that the generic assumption ensures there is no need to distinguish the functions $\Phi_{\rr_\pm}(t)$ inside the product, since for classes $\gamma\in \Gamma$ satisfying $Z(\gamma)\in \ell$ they are equal.
\end{remark}


It will be useful to consider the maps $\Psi_\rr\colon \bH_\rr\to \bT_+$ defined by
\[\exp(Z/t)\cdot \Phi_\rr(t)=\Psi_\rr(t)\cdot \xi.\]
 Composing with the characters of $\bT_+$ we can also encode the solution in the system of maps
\[\Psi_{\rr,\gamma}(t)=y_\gamma(\Psi_\rr(t))=\exp(Z(\gamma)/t)\cdot \Phi_{\rr,\gamma}(t) \cdot \xi(\gamma)^{-1}.\]
Of course the maps $\Phi_\rr$ and $\Psi_\rr$ are equivalent data: we use whichever is most convenient.


\begin{remark}
\label{whoopsy}
It follows from the condition (RH1) that if two non-active rays $\rr_1,\rr_2$ bound a convex sector containing no active rays, then the two functions $\Phi_{\rr_i}\colon \bH_{\rr_i}\to \bT$ required in Problem \ref{dtsect} glue together to give a holomorphic  function on $\bH_{\rr_1}\cup\bH_{\rr_2}$. It follows that if a non-active ray $\rr\subset \bC^*$ is  not a limit of active rays, then  the corresponding function  $\Phi_\rr$  extends analytically to a neighbourhood of the closure of  $\bH_\rr\subset \bC^*$.
\end{remark}
