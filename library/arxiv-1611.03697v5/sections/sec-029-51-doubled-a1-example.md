---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-029-51-doubled-a1-example
section_title: "Doubled A1 example"
section_number: 5.1
pages: 23-27
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
text_source: latex
latex_prose_ratio: 0.694
latex_coverage_ratio: 0.981
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



\subsection{Solution in the doubled A$_1$ case}

The formula
\begin{equation}
\label{cheedale}\Lambda(w)=\frac{e^w \cdot\Gamma(w)}{\sqrt{2\pi}\cdot w^{w-\half}}\end{equation}
defines a  meromorphic  function of $w\in \bC^*$, which is multi-valued due to the   factor
\[w^{w-\half}=\exp\big({(w-\half)\log w}\big).\]
Since $\Gamma(w)$ is meromorphic on $\bC$ with poles only at the non-positive integers, it follows that
$\Lambda(w)$ is holomorphic on $\bC^*\setminus\bR_{<0}$. We specify it uniquely by taking the principal branch of $\log$.

The Stirling expansion \cite[Section 12.33]{WW} gives an asymptotic expansion
\begin{equation}\label{stirling}\log \Lambda(w)
\sim  \sum_{g=1}^{\infty} \frac{B_{2g}}{2g(2g-1)}w^{1-2g},
\end{equation}
where $B_{2g}$ denotes the $(2g)$th Bernoulli number. This expansion is valid as $w\to \infty$ in the complement of a closed sector containing the ray  $\bR_{<0}$. It implies in particular that $\Lambda(w)\to 1$.


\begin{prop}
\label{twotier}
 When $\xi=1$, Problem \ref{eps} has a unique solution, namely 
\[\Psi_+(t)=\Lambda\Big(\frac{z}{2\pi i t}\Big), \qquad \Psi_-(t)=\Lambda\Big(\frac{-z}{2\pi i t}\Big)^{-1}.\]
\end{prop}

\begin{proof}
Note that the function $\Psi_+(t)$ is indeed holomorphic on the domain $\bC^*\setminus i\ell_+$  as required, because if we set $w=z/2\pi it$ then \[t\in i\ell_+ \iff w\in \bR_{<0}.\]
Similarly $\Psi_-(t)$ is holomorphic on $\bC^*\setminus i\ell_-$.

The
Euler reflection formula  gives
\[\Gamma(w)\cdot \Gamma(1-w) =\frac{\pi}{\sin(\pi w)},\quad w\in \bC\setminus\bZ.\]
Since $\Gamma(n)=(n-1)!$ for $n\in \bZ_{>0}$, it follows that  $\Gamma(w)$ is nowhere vanishing. The same is therefore true of  $\Lambda(w)$.
The reflection formula also implies that for $w\in \bC\setminus \bZ$
\[\Lambda(w)\cdot \Lambda(-w)=\frac{1}{2\pi}\cdot  \frac{\pi }{\sin(\pi w)}\cdot e^{-( (w-\half)\log(w)+(-w+\half)\log(-w))},\]
where we used $\Gamma(1-w)=(-w)\cdot \Gamma(-w)$.
For the principal branch of $\log$ we have \[\log(w)=\log(-w)\pm \pi i\text{ when }\pm \Im(w)>0.\]
Thus we conclude that
\begin{equation}
\label{luminy}\Lambda(w)\cdot \Lambda(-w)=\frac{i\cdot e^{-\pi i(w-\half)}} {e^{\pi iw}-e^{-\pi i w}}=(1-e^{2\pi iw})^{-1}\end{equation}
when $\Im(w)>0$.
Note that if $w=z/2\pi i t$ then \[ t\in \bH_{\ell_-}\iff \Im(w)>0,\]
so we get the second of the relations \eqref{rabbit}. The other follows in the same way.
Property (ii) is immediate from the Stirling expansion \eqref{stirling}. Property (iii) is a simple consequence of the fact that $\Gamma(w)$ has a simple pole at $w=0$. Finally, the uniqueness statement follows from Lemma \ref{brownpaperbag}.
\end{proof}





\subsection{The finite uncoupled case}

In the case of a finite, uncoupled,  integral BPS structure we can construct a unique solution to the Riemann-Hilbert problem by superposing the solutions from the previous section.

\begin{thm}
\label{hd}
Let $(Z,\Gamma,\Omega)$ be a finite, uncoupled,  integral BPS structure. Suppose that $\xi\in \bT$ satisfies $\xi(\gamma)=1$ for all active classes $\gamma\in \Gamma$. Then the  corresponding Riemann-Hilbert problem has a unique solution, which associates to a non-active ray $\rr$ the function
\begin{equation}
\label{blbl}
\Psi_{\rr,\beta}(t)= \prod_{Z(\gamma)\in i\bH_\rr} \Lambda\bigg(\frac{Z(\gamma)}{2\pi i t}\bigg)^{\Omega(\gamma) \<\beta,\gamma\>}
\end{equation}
 where the product is taken over the finitely many active classes $\gamma\in \Gamma$ for which  $Z(\gamma)\in i\bH_\rr$.
\end{thm}

\begin{proof}
Note first that the expression \eqref{blbl} is holomorphic and non-zero on $\bH_\rr$ because in each factor both $Z(\gamma)/i$ and $t$ lie in $\bH_\rr$, so the argument of $\Lambda$ does not lie in $\bR_{<0}$.  The properties (RH2) and (RH3) then follow immediately as in the proof of Proposition \ref{twotier}. 
Consider two non-active rays $\rr_-$ and $\rr_+$ obtained by small  perturbations, anti-clockwise and clockwise respectively, of an  active ray $\ell$. Then $\ell\subset i\bH_{\rr_+}$ whereas $-\ell\subset i\bH_{\rr_-}$. Assume that  $t\in \bH_{\rr_-}\cap \bH_{\rr_+}$. Then  $t\in \bH_\ell$ and hence $-Z(\gamma)/2\pi it$ lies in the upper half-plane whenever $Z(\gamma)\in \ell$. Using \eqref{luminy} we therefore obtain 
\[\frac{\Phi_{\rr_+,\beta}(t)}{\Phi_{\rr_-,\beta}(t)}=\prod_{Z(\gamma)\in \ell} \bigg(\Lambda\Big(\frac{Z(\gamma)}{2\pi i t}\Big)\cdot\Lambda\Big(\frac{-Z(\gamma)}{2\pi i t}\Big)\bigg)^{\Omega(\gamma)\<\beta,\gamma\>}= \prod_{Z(\gamma)\in \ell} (1-e^{-Z(\gamma)/t} )^{\Omega(\gamma) \<\gamma,\beta\> }\]
 This is precisely the condition \eqref{garage} since  Lemma \ref{null} and the assumption on $\xi$ implies that
$\Phi_{\gamma}(t)=\exp(-Z(\gamma)/t)$ whenever $\Omega(\gamma)\neq 0$. 
\end{proof}

Using the Stirling expansion we obtain an asymptotic expansion
\begin{equation}\log \Phi_{\rr,\beta}(t)\sim \frac{Z(\beta)}{t}-2\pi i \theta(\beta)+\sum_{g\geq 1} \sum_{\gamma\in \Gamma}
 \frac{\Omega(\gamma)\<\beta,\gamma\>B_{2g}}{4g\,(2g-1)}\bigg(\frac{2\pi i t}{Z(\gamma)}\bigg)^{2g-1},\end{equation}
valid as $t\to 0$ in the half-plane $\bH_\rr$. We have set $\xi(\beta)=\exp(2\pi i \theta(\beta))$. The extra factor of 2 in the denominator arises because  in \eqref{blbl} we take a product over half the classes in $\Gamma$.  Note that this  expansion is independent of the choice of  ray $\rr\subset \bC^*$.






\subsection{Tau function in the uncoupled case}

 
Consider the expression
\[\Upsilon(w)=\frac{e^{-\zeta'(-1)}\, e^{\frac{3}{4}w^2} \,G(w+1)}{(2\pi)^{\frac{w}{2}}\,w^{\frac{w^2}{2}}},\]
where $G$ is the Barnes $G$-function  \cite{Barnes}, \cite[Appendix]{Vo}, and $\zeta(s)$ is the Riemann zeta function. It defines a holomorphic and nowhere vanishing function on $\bC^*\setminus \bR_{<0}$ which we specify uniquely by defining the factor $w^{w^2/2}$ using the principal value of $\log$.   The asymptotic expansion of $\Upsilon(w)$ is
\begin{equation}
\label{deb}\log \Upsilon(w)\sim -\frac{1}{12} \log(w) + \sum_{g\geq 2} \frac{B_{2g}}{2g(2g-2)} w^{-(2g-2)},\end{equation}
valid as $w\to \infty$ in the complement of any sector in $\bC^*$ containing the ray $\bR_{<0}$. This can be found for example in  \cite[Section 15]{Barnes} or \cite[Appendix]{Vo},
although note that Barnes uses a different indexing for the Bernoulli numbers, and refers to the real number
\[A=e^{\frac{1}{12}} \cdot e^{-\zeta'(1)}\]
 as the Glaisher-Kinkelin constant.

\begin{lemma}
\label{oldy}
There is an identity
\[\frac{d}{dw} \log \Upsilon(w)=w\frac{d}{dw} \log \Lambda(w).\]
\end{lemma}

\begin{proof}
Note that this is obvious at the level of the  asymptotic expansions. For the proof we use the identity
\[\frac{d}{dw} \log G(w+1)=  \frac{1}{2} \log(2\pi)+\frac{1}{2} - w+w\frac{d}{dw}\log \Gamma(w)\]
which can be found in  \cite[Section 12]{Barnes}
(see also \cite[Formula (A.13)]{Vo}) to get
\[\frac{d}{dw} \log \Upsilon(w)=\frac{1}{2} +w\frac{d}{dw}\log \Gamma(w)-w\log w.\]
The result then follows from \eqref{cheedale}  by taking $\log$ and differentiating.
\end{proof}

In the case of variations of BPS structures satisfying the conditions of Theorem \ref{hd} the following result gives a natural choice of $\tau$-function. 
\begin{thm}
Let $(\Gamma,Z_p,\Omega_p)$ be a framed, miniversal variation of finite, uncoupled,  integral BPS structures over a complex manifold $M$. Given a ray $\rr\subset \bC^*$, the function
\begin{equation}\label{holo}\tau_\rr(p;t)=\prod_{Z_p(\gamma)\in i\bH_\rr} \Upsilon\bigg(\frac{Z(\gamma)}{2\pi i t}\bigg)^{\Omega(\gamma)}\end{equation}
is a   $\tau$-function for the  family of solutions of Theorem \ref{hd}. 
\end{thm}


\begin{proof}
The expression \eqref{holo} is holomorphic and non-zero on $\bH_\rr$ for the same reason given  in the proof of Theorem \ref{hd}. It is also clearly invariant under simultaneous rescaling of $Z$ and $t$.
Choosing a basis $(\gamma_1,\cdots,\gamma_n)\subset \Gamma$, and using the local co-ordinates $z_i=Z(\gamma_i)$ on $M$, we have
\[2\pi i \cdot \sum_i \epsilon_{ij}\frac{\partial \log \tau_\rr}{\partial z_i}=\sum_i   \sum_{Z_p(\gamma)\in i\bH_\rr} \Omega(\gamma) \, \frac{\epsilon_{ij}\,m_i(\gamma)}{ t} \Big(\frac{d}{dw}\Big|_{w=\frac{Z(\gamma)}{2\pi i t}}\Big)\log \Upsilon (w),\]
where we wrote $\epsilon_{ij}=\<\gamma_i,\gamma_j\>$ and   used the decomposition $\gamma=\sum_i m_i(\gamma)\gamma_i$. Using Lemma \ref{oldy} this  can be rewritten as
\[\sum_{Z_p(\gamma)\in i\bH_\rr} \Omega(\gamma)\, \frac{\<\gamma,\gamma_j\>}{ t} \Big(w\frac{d}{dw}\Big|_{w=\frac{Z(\gamma)}{2\pi i t}}\Big)\log \Lambda (w)=\frac{\partial}{\partial t} \sum_{Z_p(\gamma)\in i\bH_\rr} 
\log \Lambda\Big(\frac{Z(\gamma)}{2\pi i t}\Big)^{\Omega(\gamma) \<\gamma_j,\gamma\>}=\frac{\partial\log \Psi_{\rr,\gamma_j}}{\partial t},\]
which gives \eqref{nick2}, and hence completes the proof that \eqref{holo} defines a $\tau$-function.
\end{proof}




Applying \eqref{deb} we get an asymptotic expansion
\begin{equation}\label{em}\log \tau_\rr(p;t)\sim \frac{1}{24} \sum_{\gamma\in \Gamma} \Omega(\gamma)\log \bigg(\frac{2\pi i t}{Z(\gamma)}\bigg) +\sum_{g\geq 2} \sum_{\gamma\in \Gamma}   \frac{\Omega(\gamma)\cdot B_{2g}}{4g\, (2g-2)} \bigg(\frac{2\pi i t}{Z(\gamma)}\bigg)^{2g-2}\end{equation}
valid as $t\to 0$ in  the half-plane $\bH_\rr$. Once again this expansion is independent of the ray $r\subset \bC^*$.


\begin{remark}
\label{andrei} The function $\Upsilon(w)$  is closely related to the function $\gamma_\hbar(x;\Lambda)$ which plays an important role in Okounkov and Nekrasov's work on supersymmetric gauge theories \cite[Appendix A]{ON}. More precisely,  they consider a function $\gamma_\hbar(x;\Lambda)$ which is uniquely defined up to a linear function in $x$ by two properties: a difference equation, and the existence of an asymptotic expansion. Using the property $G(w+1)=\Gamma(w)\cdot G(w)$ of the Barnes $G$-function, and the expansion \eqref{deb},  it follows that we can take
\[e^{\gamma_t(z;1)}={e^{-\zeta'(-1)}\cdot G\Big(\frac{z}{t}+1\Big)\cdot t^{\frac{1}{2} (\frac{z}{t})^2-\frac{1}{12} }}\cdot {(2\pi)^{-\frac{z}{2t}}}=\Upsilon\Big(\frac{z}{t}\Big)\cdot t^{\frac{1}{12}}\cdot e^{\frac{1}{t^2}(\frac{1}{2}z^2\log(z)-\frac{3}{4} z^2)}.\]
 The term appearing in the exponential on the right-hand side gives rise to the prepotential of the gauge theory. We hope that a clearer understanding of the definition of the $\tau$-function will enable us to give a mathematical definition of the prepotential. 
\end{remark}
