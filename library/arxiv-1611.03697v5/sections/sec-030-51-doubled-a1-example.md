---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-030-51-doubled-a1-example
section_title: "Doubled A1 example"
section_number: 5.1
pages: 23-24
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
\label{a1}

The following BPS structure arises from  the A$_1$ quiver, which consists of a single vertex and no arrows. It depends on a parameter $z\in \bC^*$.

\begin{itemize}
\item[(i)] The lattice $\Gamma=\bZ\cdot \gamma$ has rank one, and  thus $\<-,-\>=0$;
\smallskip
\item[(ii)] The central charge $Z\colon \Gamma\to \bC$ is determined by $Z(\gamma)=z\in \bC^*$;
\smallskip
\item[(iii)] The only non-vanishing BPS invariants are $\Omega(\pm\gamma)=1$. 
\end{itemize}

The Riemann-Hilbert problem associated to this BPS structure is trivial since all elements of $\Gamma$ are null. Let us instead consider the  double  of this BPS structure \[(\Gamma_D,Z,\Omega), \quad \Gamma_D=\Gamma\oplus\Gamma^\dual.\]
Let $\gamma^\dual\in \Gamma^\dual$ be the unique generator satisfying $\gamma^\dual(\gamma)=1$. Note that the definition  \eqref{job} shows that the skew-symmetric form $\<-,-\>$ on $\Gamma_D$  satisfies $\<\gamma^\dual,\gamma\>=1$.  

To define the Riemann-Hilbert problem for the doubled BPS structure we must first choose a constant term $\xi_D\in \bT_D$, where $\bT_D$ is the twisted torus corresponding to the lattice $\Gamma_D$.
For simplicity we take $\xi_D(\gamma^\vee)=1$, and write  $\xi=\xi_D(\gamma)\in \bC^*$.

The only active rays  are $\ell_\pm=\pm \bR_{>0}\cdot z$, and 
 Lemma \ref{null} shows that
\[\Phi_{\rr,\gamma}(t)=\exp(-z/t)\cdot \xi\]
for any non-active ray $\rr\subset \bC^*$.
The non-trivial part of the Riemann-Hilbert  problem for the doubled BPS structure consists of the functions
\[ \Psi_\rr(t)=\Psi_{\rr, \gamma^\dual}(t)\colon \bH_\rr\to \bC^*.\]

It follows from Remark \ref{whoopsy}  that the functions $\Psi_{\rr}(t)$ for non-active rays $\rr\subset \bC^*$ lying in the same component of $\bC\setminus \bR\cdot z$ are analytic continuations of each other. Thus we obtain just two holomorphic functions
\[\Psi_\pm(t)\colon \bC^*\setminus  i\ell_{\pm}   \to  \bC^*,\]
 corresponding to non-active rays lying in the half-planes $\pm \Im(z/t)>0$. 
 Using Remark \ref{wet}, the Riemann-Hilbert problem for the doubled BPS structure can therefore be restated as follows.

\begin{problem}
\label{eps}
 Find holomorphic functions $\Psi_\pm\colon \bC^*\setminus i\ell_\pm \to \bC^*$
  such that:
\begin{itemize}
\item[(i)]




There are relations
\begin{equation}
\label{rabbit}\Psi_+(t)=\begin{cases} \Psi_-(t) \cdot (1-\xi^{+1}\cdot e^{-z/t})^{-1}&\mbox{ if }t\in \bH_{\ell_+},\\ \Psi_-(t) \cdot (1-\xi^{-1}\cdot e^{+z/t})^{-1}&\mbox{ if }t\in \bH_{\ell_-}.\end{cases}\end{equation}


\item[(ii)] As $t\to 0$ in $\bC^*\setminus i\ell_{\pm}$ we have $\Psi_{\pm}(t)\to 1$.


\item[(iii)] There exists $k>0$ such that
\[|t|^{-k} < |\Psi_{\pm}(t)|<|t|^k\]
as $t\to \infty$ in $\bC^*\setminus i\ell_{\pm}$.
\end{itemize}
\end{problem}

To understand condition (i) note that if $t\in \bH_{\ell_+}$ then $t$ lies in the domains of definition $\bH_\rr$ of the functions $\Psi_\rr$ corresponding to sufficiently small deformations of the ray $\ell_+$. Thus \eqref{garage} applies to the ray $\ell_+$ and we obtain the first of  the relations \eqref{rabbit}. The second follows similarly from \eqref{garage} applied to the opposite ray $\ell_-$.
