---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-003-13-proving-borellaplace-summability
section_title: "Proving Borel–Laplace summability"
section_number: 1.3
pages: 5-8
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.974
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜no [9] that perturbative series associated with the hyperbolic knots 41 and 52 are resurgent and"
---
\label{sec:BL-intro}
Starting with a Gevrey-1 formal power series, the process of resurgence requires convergence and then analytic continuation of the series's Borel transform~\cite{EcalleI,diverg-resurg-i}. 

Recall that the Borel transform $\calB$ is defined as the formal inverse of the Laplace transform
\be\label{eq:laplace}
\calL^\vartheta(\phi):=\int_0^{e^{i\vartheta}\infty} e^{-\z/\hbar} \phi(\z) \, d\z\,,
\ee
where $\vartheta\in [0,2\pi)$. 
More precisely, the Borel transform maps Gevrey-1 formal series to convergent power series in a neighbourhood of the origin 
\be\label{eq:borel}
\calB\colon\sum_{n\geq 1} a_n \hbar^n\in\BC[\![\hbar]\!]\quad\mapsto\quad \sum_{n\geq 1} \frac{a_n}{n!} \zeta^{n-1}\in\BC\{\zeta\}\,,
\ee 
where $|a_n|\leq C A^n n!$ for some constants $A,C>0$.

When the analytic continuation of the Borel transform has good growth conditions at infinity, its Laplace transform in the direction $\vartheta$ is well defined and gives an analytic function, which is called the Borel--Laplace sum of the series $s_\vartheta:=\calL^\vartheta\circ\calB$. As the argument $\vartheta$ varies, the resummation $s_\vartheta$ can jump at {\em Stokes rays} defined by rays from the origin with arguments agreeing with that of singularities in Borel plane. 
Following \'Ecalle's formalism~\cite{EcalleI,diverg-resurg-i}, the Stokes automorphism $\mathfrak{S}_{\vartheta}$ associated to each Stokes ray is defined by comparing two later Borel--Laplace sums  
\be
s_{\vartheta_+}\=s_{\vartheta_-}\mathfrak{S}_{\vartheta}
\ee
where $\vartheta_\pm=\vartheta\pm\epsilon$ for some small $\epsilon$. When the difference of the two lateral Borel--Laplace sum of $\varphi$ is given by a transseries like 
\be
s_{\vartheta_+}\varphi-s_{\vartheta_-}\varphi\=\sum_{\arg(\omega)=\vartheta} S_\omega e^{-\omega\tau}s_{\vartheta_-}(\varphi_\omega)\,
\ee
where $S_\omega\in\BC$, and $\varphi_\omega\in\BC[\![\tau^{-1}]\!]$ are the secondary resurgent series arising at the singularity~$\omega$ (see for example~\cite[Sec.~5]{GGM:I}). Then the Stokes automorphism allows the computation of the Stokes constants $S_\omega$. Indeed, by factorising $\mathfrak{S}_{\vartheta}$ into automorphisms associated to each singularity $\omega$ in various orders, we can compute the so called alien derivatives~\cite[Def.~6.63]{diverg-resurg-i}. Hence we can compute the Stokes constants $S_\omega$ from $\mathfrak{S}_\vartheta$.  
Moreover, it is enough to compute the Stokes automorphisms between two distinct direction; given two such directions $\vartheta_1, \vartheta_2$, we can write
\be
  \mathfrak{S}_{\vartheta_1,\vartheta_2}
  \=
  \prod_{\vartheta\in(\vartheta_1,\vartheta_2)}\mathfrak{S}_{\vartheta}\,.
\ee
Therefore, factorising $\mathfrak{S}_{\vartheta_1,\vartheta_2}$ into $\mathfrak{S}_{\vartheta}$ and the previous remarks allow us to compute the individual Stokes constants. This formalism is closely related to the analytic wall-crossing structure of Kontsevich--Soibelman~\cite{kontsevich2022analyticity}.

When the Borel--Laplace sum exists, it has uniform asymptotics as $|\tau|\to\infty$ for~$\arg(\tau)$ contained in an interval of length greater than or equal to $\pi$. Conversely, an analytic function with such asymptotic properties is the resummation of its asymptotics~\cite{nevanlinna}. Indeed, the analytic continuation of the Borel transform can be explicitly computed using Mordell's formula for the inverse Laplace transform~\cite{watson.reg}. 
Using this method and Theorem~\ref{thm:fad.asymp} we can deduce that Faddeev's quantum dilogarithm is the resummation of its asymptotics.
\begin{corollary}\label{cor:fad.resum}
The Borel--Laplace sum of $\Psi(z;-2\pi i/\tau)$ in the direction $\vartheta$ is given by $\mu_8\tq^{-1/24}q^{1/24}\Phi(z\tau;\tau)$
\begin{itemize}
  \item for $\arg(z+1)+\tfrac{\pi}{2}<\vartheta<\arg(z)+\tfrac{\pi}{2}$ with $\Im(z)\geq0$,
  \item and for $\arg(z)-\tfrac{\pi}{2}<\vartheta<\arg(z+1)-\tfrac{\pi}{2}$ with $\Im(z)\leq0$.
\end{itemize}
\end{corollary}
\begin{proof}
By definition, if $z\in\BC\backslash(\BR_{\leq-1}\cup\BR_{\geq0})$ then $z\in\BC_\pi$. Then the first time the branch cuts of $D_{\theta}$ intersect the point $z$ are located at $\theta=\arg(\pm(z+1))$ and $\theta=\arg(\pm z)$. From Theorem~\ref{thm:fad.asymp}, the function $\Phi(z\tau;\tau)$ therefore has uniform asymptotics for $\arg(z+1)<\theta<\arg(z)+\pi$ or $\arg(z)-\pi<\theta<\arg(z+1)$ depending on the sign of $\Im(z)$.
\end{proof}
The same method can also be used to prove that exponential integrals along their steepest descent contours are the Borel--Laplace sum of their asymptotics (a different proof is given in~\cite{borel_reg}). Thus, given that $\Phi_\Xi$ is defined by formal Gaussian integration, one might expect that a similar argument would work for the state integrals in Equation~\eqref{eq:state_int}. However, the state integrals' contours are not defined on $\Sigma$ or on the Riemann surface of the dilogarithm. Moreover asymptotically, Faddeev's quantum dilogarithm chooses branch cuts of the dilogarithm. Therefore, trying to deform state integrals into thimble integrals cannot always be done. To remedy this, we make the crucial observation that the integrands of different $\calI_{m,\ell}$ can have the same leading asymptotics depending on the branching of $D_{\th}$. This allows us to patch together a variety of integrals that follow the contour of steepest descent up to a finite collection of extra integrals (we will call {\em tails}). The asymptotics of these finitely many integrals can again be represented as a collection of state integrals up to a finite collection of new tails. This process can be repeated and proved to eventually terminate, which happens when the tails have a (relatively) exponentially small contribution. This leads to our following main result.
\begin{theorem}\label{thm:main_intro}
The asymptotic series $\Phi_{\Xi}(-2\pi i/\tau)$ are Borel--Laplace summable with Stokes rays on the countable set of rays $\tau\in\mathcal{S}(V_{0})$ with two accumulation points at $\arg(\tau)=\pm\frac{\pi}{2}$. Moreover, there is an algorithm to compute the Borel--Laplace resummation away from Stokes rays, which gives rise to a $\BZ[q^{\pm}]$-linear combination of state integrals $\calI_{m,\ell}(\tau)$ for $\Re(\tau)>0$ and $\calI_{m,\ell}^{-}(\tau)$ for $\Re(\tau)<0$.\footnote{See Remark~\ref{rem:neg.rt} or Equation~\eqref{eq:neg.si} for a definition.}
\end{theorem}




















\begin{remark}\label{rem:neg.rt}
All of the proofs and statements work perfectly well for $\Re(\tau)<0$. To avoid cluttering the notation we only give the details for $\Re(\tau)>0$. To deal with the case $\Re(\tau)<0$ one would need to use the additional function
\be
  \Phi^{-}(z;\tau)
  \=
  \Phi(-z+1+\tau;-\tau)^{-1}
  \=
  \frac{(q\e(-z);q)_{\infty}}{(\e(z/\tau);\tq)_{\infty}}\,.
\ee
The function $\mu_8\tq^{-1/24}q^{1/24}\Phi^{-}(z\tau;\tau)$ gives the resummation of $\Psi(z;-2\pi i/\tau)$ for some $\vartheta\in (-\pi/2, \pi/2)$. The function $\Phi^-$ comes with its own state integrals
\be\label{eq:neg.si}
\calI_{m,\ell}^{-}(\tau)
\;:=\;
\mu_8^B\tq^{-B/24}q^{B/24}
\int_{\calJ_{\ell,\tau}^{-}}\Phi^{-}((z-\ell)\tau;\tau)^B \e\Big(\frac{A}{2} z(z\tau+\tau+1)+mz\tau\Big) dz\,,
\ee
where $\calJ_{\ell,\tau}^{-}:=(\tfrac{i}{\sqrt{-\tau}}e^{iA\epsilon}\BR_{\geq0}+\frac{1}{2}+\ell)\cup(\tfrac{i}{\sqrt{-\tau}}e^{+ i(A-B)\epsilon}\BR_{\leq0}+\frac{1}{2}+\ell)$ for some small $\epsilon>0$.
\end{remark}



We can use Theorem~\ref{thm:main_intro} to describe the full resurgent structure for our examples. First, notice that there are $\max\{A,B\}$ critical points. One can also see that there are exactly $\max\{A,B\}^2$ independent state integrals and asymptotic series. Indeed, consider the family of asymptotic series
\be
  \Phi_{\Xi,j}(\hbar)
  \=
  \int_{\calC_{p_0}} \Psi(z,\hbar)^B\exp\Big(-\frac{A}{2\hbar}(2\pi i)^2z\Big(z+1-\frac{\hbar}{2\pi i}\Big)+(2\pi i)^2\frac{m_0z}{\hbar}+2\pi izj\Big)dz\,,
\ee
and collect all these asymptotic series into one matrix
\be\label{eq:phimat}
  (\widehat{\Phi}_j(\hbar))_{\ell,p_0}
  \=
  \Phi_{(A,B,p_0),j+\ell}(\hbar)\,.
\ee
Then from Theorem~\ref{thm:main_intro}, we know that this whole matrix of asymptotic series is resummable for $\vartheta\in\arg(\BC\backslash(\cup_{p_0}\calS(V_0)))$ to a matrix we denote $\widehat{\calI}_{j,\vartheta}(\tau)$. We show that this matrix is invertible in Corollary~\ref{cor:phi.is.invert}. Moreover, the theorem implies that the entries of this matrix consist of finite $\BZ[q]$-integral combinations of state integrals. Therefore, for $\vartheta_1,\vartheta_2\in(\tfrac{\pi}{2},\tfrac{3\pi}{2})\cap\arg(\BC\backslash(\cup_{p_0}\calS(V_0)))$ we find that
\be
  \widehat{\calI}_{j,\vartheta_2}(\tau)
  \=
  \widehat{\calI}_{j,\vartheta_1}(\tau)
  \mathfrak{S}_{\vartheta_1,\vartheta_2}(q)
\quad\text{where}\quad
  \mathfrak{S}_{\vartheta_1,\vartheta_2}(q)
  \in
  \GL_{\max\{A,B\}}(\BZ[q^{\pm}])\,.
\ee
Moreover, for $\vartheta_1<\vartheta_2<\vartheta_3$ we have
\be
  \mathfrak{S}_{\vartheta_1,\vartheta_2}(q)
  \mathfrak{S}_{\vartheta_2,\vartheta_3}(q)
  \=
  \mathfrak{S}_{\vartheta_1,\vartheta_3}(q)\,.
\ee
 In Section~\ref{sec:ex}, we will compute a couple of Stokes constants explicitly using the algorithm of Section~\ref{sec:alg}. However, as will be clear to the reader this is not an efficient method of computation for $\vartheta$ near $\pm\tfrac{\pi}{2}$. The method is extremely effective when $\vartheta$ is near $0,\pi$ as the algorithm terminates almost immediately. Therefore, armed with Theorem~\ref{thm:main_intro} and an easy computation when $\vartheta$ is near $0,\pi$, we can compute the other Stokes constants using the methods of~\cite{GGM:I}. This involves computing the Stokes automorphism for a small $\epsilon>0$
\be
\begin{aligned}
  \mathsf{S}_+(q)
  &\=
  \mathfrak{S}_{\pi+\epsilon,\epsilon}(q)\in\GL_{\max\{A,B\}}(\BZ[q^{-1}][\![q]\!])\,,\\
  \mathsf{S}_-(q)
  &\=
  \mathfrak{S}_{\epsilon,-\pi+\epsilon}(q)\in\GL_{\max\{A,B\}}(\BZ[q][\![q^{-1}]\!])\,.
\end{aligned}
\ee
These series then store all the information of the Stokes constants. This allows for a complete computation of the Stokes constants with proofs.

This paper is organised as follows. In Section~\ref{sec:geometry} we define the geometric setting, namely a relative homology to which both the class of thimbles and of state integrals contours belong. Section~\ref{sec:asymp_state_int} is dedicated to the proof of our main results. More precisely, in Section~\ref{sec:alg} we illustrated the algorithm that leads to the proof of Theorem~\ref{thm:main_intro} in Section~\ref{sec:proof_main}. Finally in Section~\ref{sec:ex}, we illustrate the algorithm in two examples: the case $(A,B)=(1,2)$ corresponding to the $4_1$ knot in Section~\ref{sec:4_1}, and the case $(A,B)=(4,1)$ in Section~\ref{sec:A4B1}. As a result of the decomposition into state integrals, we verify the numerical computations of the first Stokes constants~\cite{GGM:I,Wh:thesis} in both examples. There are two appendices.
