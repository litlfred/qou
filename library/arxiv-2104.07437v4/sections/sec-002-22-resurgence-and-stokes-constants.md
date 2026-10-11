---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-002-22-resurgence-and-stokes-constants
section_title: "Resurgence and Stokes constants"
section_number: 2.2
pages: 7-10
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.993
---
\label{sc:resurg}

Formal power series with factorial growth lead, under some assumptions, to a universal mathematical structure 
described by the theory of resurgence, see ~\cite{abs,msauzin} for a formal description and \cite{mmbook,mmlargen} for applications 
in gauge and string theory. This mathematical structure involves a family of numerical data called Stokes constants. 
When the perturbative series under consideration 
are topological invariants of some underlying geometric object, the corresponding Stokes constants lead to 
numerical, topological invariants. Surprisingly, these 
invariants turn out to be {\it integers} in many situations. In this section we will provide the formal definition of Stokes constants, and we will then apply this definition to the 
perturbative series (\ref{phiN}). 

Let us consider a factorially 
divergent (or Gevrey-1) series, of the form, 

\begin{equation}
  \varphi(\tau)=\sum_{n \ge 0} a_n \tau^{n},\qquad a_n  \sim n!. 
\end{equation}

The theory of resurgence tells us that, generically, this series will not be on its own, 
but will be accompanied by an additional set of 
formal power series. To understand how this comes about, 
we consider the Borel transform of $ \varphi(\tau)$, defined by

\begin{equation}
  \widehat \varphi(\zeta)= \sum_{k \ge 0} {a_k \over k!} \zeta^k. 
\end{equation}

It is a holomorphic function in a neighborhood of the origin. In
favorable cases, this function can be extended to the complex
$\zeta$-plane (also called Borel plane), but it will have
singularities. Let us label by an index $\omega$ the (perhaps infinite) set 
of singularities in the Borel plane $\zeta_\omega\in \IC$. Let us assume for the moment being
that this singularity is a logarithmic branch cut, and consider the behavior 
of $ \widehat \varphi(\zeta)$ near $\zeta_\omega$: 

\be
\label{log-sing}
\widehat \varphi(\zeta)= -\mS_\omega {\log (\xi) \over 2 \pi \ri} \widehat \varphi_\omega (\xi)+ \cdots  
\ee

In this expression, $\xi=\zeta- \zeta_\omega$, the dots denote regular terms in $\xi$, the function 

\be
 \widehat \varphi_\omega (\xi)= \sum_{n \ge 0} \hat a_{n, \omega} \xi^n
 \ee
 
 is an analytic function at $\xi=0$, and $\mS_\omega$ will be later identified as Stokes constants. 
 As the notation suggests, we can regard this series as 
 the Borel transform of the Gevrey-1 series
 
 \be
 \label{phiomco}
 \varphi_\omega(z)=  \sum_{n \ge 0} a_{n, \omega} z^n, \qquad a_{n, \omega}= n! \hat a_{n, \omega}. 
 \ee
 

 We then see that, starting with a single formal power series, we can obtain a new family of them by just looking at 
 the behavior near the singularities of the Borel 
 transform. We can now repeat the procedure with the series obtained in this way. Eventually, one ends up with a 
family of formal power series
 
 \be
 \mathfrak{B}_\varphi=\{ \varphi_\omega(z)\}_{\omega \in \Omega}, 
 \ee
 
 which we will call the {\it minimal resurgent structure} associated to the original series $\varphi(z)$. The Borel transform 
 of the formal power series in the minimal resurgent structure have local expansions 
 
 \be
 \widehat \varphi_\omega (\zeta)= -\mS_{\omega \omega'} {\log (\xi) \over 2 \pi \ri} \widehat \varphi_{\omega'} (\xi)+ \cdots. 
 \ee
 
 The complex numbers $\mS_{\omega \omega'}$ are called {\it Stokes constants}. Note that their values depend on a choice of normalization 
 of the series $ \varphi_\omega(z)$. 
 

 
 The Stokes constants appear in a different type of calculation, which often is easier to perform in practice. 
Let $\varphi(z)$ be a generic Gevrey-1 series, and let us assume that the analytically continued Borel transform $\widehat \varphi(\zeta)$ 
does not grow too fast at infinity. The {\it Borel resummation} of
$\varphi(z)$ is defined as the Laplace transform

\begin{equation}
  \label{eq:brlsum}
  s(\varphi)(z) = \int_0^\infty \re^{-\zeta}
  \widehat \varphi(\zeta z) \rd \zeta. 
\end{equation}

This function, when it exists, is locally analytic, but has discontinuities at special rays in the $z$ plane. 
Let $\zeta_\omega$ be a singularity of $\widehat \varphi(\zeta)$. A ray in the Borel plane 
which starts at the origin and passes through $\zeta_\omega$ is called a {\it Stokes ray}. It is of the form $\re^{\ri\theta}\IR_+$, where 

\be
\label{theta-ray}
\theta= {\rm arg}(\zeta_\omega).
\ee

The integral (\ref{eq:brlsum}) has a discontinuity whenever
$ {\rm arg}(z)= {\rm arg}(\zeta_\omega)$. 


\begin{figure}
  \centering \includegraphics[height=5cm]{contour-def.pdf}
  \caption{The difference between lateral Borel resummations in (\ref{disc-Stokes}) (left) can be computed as a contour integral, given by the contribution 
of the singularities (right).}
  \label{contour-def-fig}
\end{figure}


To calculate the discontinuities, we define the lateral Borel
resummations for $z$ near a Stokes ray by

\begin{equation}
  s_\pm (\varphi)(z)= \int_0^{\re^{\pm \ri \epsilon} \infty}
  \re^{-\zeta} \widehat \varphi(\zeta z) \rd \zeta. 
\end{equation}

The discontinuity is then simply given by 
 
 \be
 {\rm disc}_\theta \varphi (z)=s_+ (\varphi)(z)-s_- (\varphi)(z), 
 \ee
 
where $\theta$ is defined in (\ref{theta-ray}). A simple contour-deformation calculation (see \figref{contour-def-fig}) shows that, in the case that all singularities 
are logarithmic, one has

\be
\label{disc-Stokes}
s_+ (\varphi_\omega)(z)-s_- (\varphi_\omega )(z)= \sum_{\omega'} \mathsf{S}_{\omega \omega'} 
\re^{-\zeta_{\omega'}/z}  s_-(\varphi_{\omega'})(z), 
\ee

where the sum over $\omega'$ runs over all the singularities located on the Stokes ray. This equation 
turns out to give a powerful method to compute Stokes constants, by comparing (lateral) Borel resummations. 

To write the fundamental equation (\ref{disc-Stokes}) in a more convenient form, we note 
that the $\zeta_{\omega'}$ appearing in the r.h.s.~depend implicitly on $\omega$. To have 
a more symmetric form, we introduce the {\it basic trans-series} $\Phi_\omega(z)$
as 

\begin{equation}
  \Phi_\omega(z)=\re^{-V_\omega /z} \varphi_\omega(z),
\end{equation}

where the $V_\omega$ are chosen in such a way that $\zeta_{\omega'}=V_{\omega'}- V_\omega$. 
The Borel resummation of the basic trans-series $\Phi_\omega (z)$ is
defined by

\begin{equation}
  s(\Phi_\omega)(z) =\re^{-V_\omega /z} s(\varphi_\omega)(z)
\end{equation}

To measure the discontinuity of Borel resummations across a Stokes
ray, it is also useful to introduce the {\it Stokes automorphism} $\mathfrak{S}$ as

\begin{equation}
  s_+= s_- \mathfrak{S}. 
\end{equation}

In this way, (\ref{disc-Stokes}) can be written as 

\begin{equation}
  \mathfrak{S} (\Phi_\omega)= \Phi_{\omega}+ \sum_{\omega'}
  \mathsf{S}_{\omega \omega'} \Phi_{\omega'}. 
\end{equation}


Let us emphasize that the definition of Stokes constants given above
relies on relatively mild assumptions. In technical terms, we are
assuming that the formal power series $\varphi_\omega(z)$ are simple
resurgent functions. The property of being resurgent means that, on
every finite line issuing from the origin, the Borel transform
$\widehat \varphi_\omega(\zeta)$ has a finite number of singularities,
and one can analytically continue it along a path which circumvents
these singularities. Simple resurgent functions have only logarithmic
singularities, as in (\ref{log-sing}). However, it is straightforward
to extend this formalism to resurgent functions with more general
singularities, like branch cuts of the form

\begin{equation}
\label{borel-bc}
\widehat \varphi(\zeta_\omega+ \xi) = (-\xi)^{-\nu} {\mS_\omega  \over
  2 \ri \sin (\pi b)} \sum_{n \ge 0} \widehat a_n \xi^n+
{\text{regular}}, \qquad

\nu\not\in\IZ.
\end{equation}

In this case, we regard $\widehat \varphi_\omega(\xi)$ as the Borel
transform of

\be
\varphi_\omega(z)=z^{-\nu} \sum_{n \ge 0} a_n z^n, \qquad a_n= \Gamma(n+1-\nu) \widehat a_n, 
\ee

and it is easy to check that the discontinuity formula (\ref{disc-Stokes}) still holds in the same form. 

In summary, the machinery of resurgence gives a well-defined procedure to 
obtain a (possibly infinite) set of Stokes constants: starting from a single perturbative series $\varphi$, 
one first finds the minimal resurgent structure $\mathfrak{B}_\varphi$, and then the set of Stokes constants. Schematically, we have

\be
\varphi(\tau) \longrightarrow \mathfrak{B}_\varphi=\{ \varphi_\omega(\tau) \}_{\omega \in \Omega} \longrightarrow \{ \mS_{\omega \omega'} \}_{\omega, \omega' \in \Omega}. 
\ee


 \begin{remark} At this point, it might be useful to add some clarifying remarks on the notion of minimal resurgent structure introduced above. 
 The minimal resurgent structure associated to a formal series $\varphi(z)$ is the smallest set of resurgent functions which 
is needed to find a closed system under Stokes automorphisms. It does not include necessarily all the formal power series in the theory. A surprising example of this situation occurs in complex CS theory, where formal power series are associated to perturbative expansions around flat connections on a three-manifold $M$. If $M$ is the complement of a hyperbolic knot, there are two special flat connections, namely the trivial connection, and the so-called geometric connection, which corresponds to the unique complete hyperbolic metric on $M$. They lead to two different formal power series, which we denote by $\Phi_0$ and $\Phi_g$, respectively. It follows e.g. from the results in \cite{witten-acs,ggm1, ggm2, gar-zag-2} that the minimal resurgent structure associated to $\Phi_g$, $\mathfrak{B}_{\Phi_g}$, 
does {\it not} include $\Phi_0$. The minimal 
resurgent structure associated to $\Phi_0$ is however 
strictly bigger: $\mathfrak{B}_{\Phi_g} \subsetneq \mathfrak{B}_{\Phi_0}$ \cite{garoufalidis,ggmw, gar-zag-2}. \qed

 
 \end{remark}
