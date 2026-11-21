---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-027-45-null-vectors-and-uniqueness
section_title: "Null vectors and uniqueness"
section_number: 4.5
pages: 20-22
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.65
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
Let  $(Z,\Gamma,\Omega)$ be a  BPS structure, and denote by $\bT$ the corresponding twisted torus.
\begin{defn}
An element $\gamma\in \Gamma$ will be called null if it satisfies $\<\alpha,\gamma\>=0$ for all active classes $\alpha\in \Gamma$. A twisted character $x_\gamma\colon \bT\to \bC^*$ corresonding to a null element $\gamma\in \Gamma$  will be called a  coefficient.
\end{defn}

Note that the definition of the wall-crossing automorphisms $\bS(\ell)$ shows that they fix all coefficients:
$\bS(\ell)^*(x_\gamma)=x_\gamma$. This leads to the following partial uniqueness result.

\begin{lemma}
\label{null}
Let $(Z,\Gamma,\Omega)$ be a convergent BPS structure and $\gamma\in \Gamma$ a null element. Then for any solution to the Riemann-Hilbert problem, and any non-active ray $\rr\subset \bC^*$, one has 
$\Psi_{\rr, \gamma}(t)=1$
for all $t\in \bH_\rr$.
\end{lemma}

\begin{proof}
Since coefficients are unchanged by wall-crossing, condition (RH1) shows that the functions $\Psi_{\rr,\gamma}(t)$ for different rays $\rr\subset \bC^*$ piece together to give a single holomorphic function $\Psi_\gamma\colon \bC^*\to \bC^*$. Since we can cover $\bC^*$ by  the half-planes  $\bH_{\rr_i}$ defined by finitely many non-active rays $\rr_i\subset \bC^*$, condition (RH2) shows that this function has a removable singularity at $0\in \bC$ with value $\Psi_\gamma(0)=1$, and condition (RH3) shows that it has at worst polynomial growth at $\infty$. It follows that $\Psi_\gamma$ extends to a meromorphic function $\bC\bP^1\to \bC\bP^1$ which has neither zeroes nor poles on $\bC$. This implies that $\Psi_\gamma(t)$ is constant, which proves the result.
\end{proof}

Recall the definition of an uncoupled BPS structure from Section \ref{defns}. 

\begin{lemma}
\label{brownpaperbag}
Let $(Z,\Gamma,\Omega)$ be a finite, uncoupled, integral  BPS structure. Then the associated Riemann-Hilbert problem has at most one solution.
\end{lemma}

\begin{proof}
Note that uncoupled BPS structures are in particular generic, so Remark \ref{wet} applies.
Fix an arbitrary class $\beta\in \Gamma$. The uncoupled condition implies that all classes $\gamma\in \Gamma$ appearing in the product on the right-hand side of \eqref{garage} are null. Lemma \ref{null} shows that for these classes  the corresponding functions
\[\Phi_{\rr,\gamma}(t)=\exp(-Z(\gamma)/t)\cdot \xi(\gamma)\]
are uniquely determined. It follows that if we have two systems of solutions \[\Phi^{(i)}_{\rr,\beta}(t)\colon \bH_\rr\to \bC^*, \quad i=1,2,\] to the Riemann-Hilbert problem, then the ratios\[q_{\rr,\beta}(t)=\Phi^{(2)}_{\rr,\beta}(t)\cdot (\Phi^{(1)}_{\rr,\beta}(t))^{-1} \colon \bH_\rr\to \bC^*\]
piece together to give a single holomorphic function $q_\beta\colon \bC^*\to \bC^*$. Arguing exactly as in Lemma \ref{null},  we can use conditions (RH2) and (RH3) to conclude that $q_\beta(t)=1$ for all $t\in \bC^*$, which proves the claim.
\end{proof}


\begin{remark}
Let $(\Gamma,Z,\Omega)$ be a convergent BPS structure, and consider the doubled BPS structure $(\Gamma\oplus \Gamma^\dual,Z,\Omega)$ of  Section \ref{double}.  For each class $\gamma\in \Gamma$ the  corresponding element \[\gamma_D=(\gamma, \<-,\gamma\>)\in \Gamma\oplus \Gamma^\dual\]
is  null, because, by the formula \eqref{job},   it is orthogonal to any class of the form $(\alpha,0)\in \Gamma\oplus \Gamma^\dual$. Lemma \ref{null} therefore implies that any solution to the Riemann-Hilbert problem for the double satisfies $\Psi_{\gamma_D,\rr}(t)=1$. This implies that
\[\Psi_{\rr, (0,\<\gamma,-\>)}(t)=\Psi_{\rr,(\gamma,0)}(t),\]
 for all  non-active rays $\rr\subset \bC^*$, and all $t\in \bH_r$. 
 
  In this way one sees that  if a BPS structure has a non-degenerate form $\<-,-\>$, then solving the Riemann-Hilbert problem for the doubled BPS structure is precisely equivalent to solving the problem for the original BPS structure. However, when the form $\<-,-\>$ is degenerate,  a solution to the Riemann-Hilbert problem for the doubled BPS structure contains strictly more information than a solution to the  original problem. We will see an example of this in Section \ref{a1} below. \end{remark}



\subsection{Tau functions} 

Consider a framed, miniversal variation of BPS structures $(\Gamma,Z_p,\Omega_p)$  over a complex manifold $M$.
For the relevant definitions the reader can either consult the summary in Section \ref{vbpss}, or the full treatment in Appendix \ref{two}. There is a holomorphic map \[\pi \colon M\to \Hom_\bZ(\Gamma,\bC), \quad p\mapsto Z_p,\]
which we call the period map. The miniversal assumption ensures that the derivative
\begin{equation}
\label{friday}(D\pi)_p \colon T_p M\to \Hom_{\bZ}(\Gamma,\bC)\end{equation}
at each point $p\in M$ is an isomorphism. We  can  therefore identify the tangent space $T_p M$    with the  vector space $\Hom_\bZ(\Gamma,\bC)$.   The  form $\<-,-\>$  then induces a Poisson structure on $M$.

More explicitly, we can choose a basis $(\gamma_1,\cdots,\gamma_n)\subset \Gamma$ and use the functions \[z_i(p)=Z_p(\gamma_i)\colon M\to \bC\]
as  co-ordinates on $M$. The dual of the map \eqref{friday}  identifies  $\gamma_i\in \Gamma$ with the element $dz_i\in T_p^*M$, and the Poisson structure   has the Darboux form
\[\{z_i,z_j\}=\epsilon_{ij}, \qquad \epsilon_{ij}=\<\gamma_i,\gamma_j\>.\]

Let us  consider a family of solutions \[\Psi_\rr=\Psi_\rr(p,t)\colon M\times \bC^*\to\bT_+\]
 to the  Riemann-Hilbert problems associated to the BPS structures $(\Gamma,Z_p,\Omega_p)$. For each ray $\rr\subset \bC^*$ we assume that $\Psi_\rr(p,t)$ is a piecewise holomorphic function, with discontinuities at points $p\in M$ where the ray $\rr\subset \bC^*$ is active in the BPS structure $(\Gamma,Z_p,\Omega_p)$. Differentiating with respect to $t$ and translating to the identity $1\in \bT_+$ we get a map
\[\Psi_\rr^{-1}\cdot \frac{d\Psi_\rr}{dt}\colon M\times \bC^*\to \Hom_\bZ(\Gamma,\bC).\]
Composing with  the inverse of \eqref{friday}, this can be viewed as a vector field $V(t)$ on $M$ depending on $t\in \bC^*$. A $\tau$-function for the family of solutions $\Psi_\rr(p,t)$  is a piecewise holomorphic function \[\tau_\rr=\tau_\rr(p,t)\colon M\to \bC^*,\]
 such that $V(t)$ is the Hamiltonian vector field of the function $(2\pi i)\cdot \log \tau_\rr$. In terms of the co-ordinates $z_i=Z(\gamma_i)$ described above,  the condition is that
 \begin{equation}
 \label{nick2}\frac{1}{2\pi i}\cdot\frac{\partial \log \Psi_{\rr,\gamma_j}}{\partial t}=\sum_i \epsilon_{ij}  \frac{\partial \log \tau_\rr}{\partial z_i}.\end{equation}
By the second symmetry property of Section \ref{sym} it is natural to also impose the condition that  $\tau$ is invariant under simultaneous  rescaling of $Z$ and $t$. In the case when the form $\<-,-\>$ is non-degenerate this is enough to determine the  $\tau$-function uniquely up to multiplication by an element of $\bC^*$.
