---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-002-12-the-generalized-volume-conjecture
section_title: "The generalized volume conjecture"
section_number: 1.2
pages: 4-5
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.979
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sub.volume}


In this section we state some new information about the Volume Conjecture;
the latter connects two very different approaches to knot theory,
namely Topological Quantum Field Theory and Riemannian
(mostly Hyperbolic) Geometry.

\begin{conjecture}
\lbl{conj.vc}\cite{K,MM}
For every hyperbolic knot $K$ in $S^3$ we have:
\begin{equation*}
\lbl{eq.VC}
\lim_{n \to \infty} \frac{\log| f_{K,n}(2 \pi i)|}{n}=
\frac{1}{2 \pi}\, \vol(\rho_{2\pi i}),
\end{equation*}
where $\vol(\rho_{2 \pi i})$ is the {\em hyperbolic volume} of the
 the knot complement $S^3-K$.
\end{conjecture}

In other words, the sequence $f_{K,n}(2 \pi i)$ of complex numbers
grows exponentially with respect to $n$, and the exponential
growth-rate is proportional to the volume of a hyperbolic knot.

One can define the volume function $\vol(\rho)$ of every
representation $\rho: \pi_1(S^3\setminus K)\to \SL_2(2,\BC)$, see
\cite{Du,CCGLS,Th}, and $\vol(\rho_{2\pi i})$ is exactly the value of this
volume function with $\rho_{2\pi i}$ being the discrete faithful
representation of the knot group.

The idea of the Generalized Volume Conjecture (formulated in part by
Gukov in \cite{Gu}) is that we should use other representations of
the knot complement in $\SL(2,\BC)$. For $\a$ nearby $2 \pi i$, in a
small neighborhood of $\rho_{2\pi i}$ there is a unique (up to
conjugation) representation
$$
\rho_{\a}: \pi_1(S^3-K) \longto \SL(2,\BC)
$$
which satisfies
\begin{equation}
\lbl{eq.meridian}
\rho_{\a}(\text{meridian})=
\mat {e^{\a}} {\star} 0 {e^{-\a}} .
\end{equation}
Alas, there is an additional difficulty. Namely, when $\a/(2 \pi i)$ is rational, we should distinguish
two cases: $\a/(2 \pi i)=1 $ or $\a/(2 \pi i)\neq 1$.
The Generalized Volume Conjecture for $\a$ sufficiently close to $2 \pi i$
may now be stated as follows.

\begin{conjecture}
\lbl{conj.gvc}
\lbl{eq.gvc}
If $\a/(2 \pi i) \in (\BR-\BQ) \cup \{1\}$ is sufficiently close to $1$
then
\begin{equation}
\lbl{eq.GVC}
\lim_{n \to \infty} \frac{\log| f_{K,n}(\a)|}{n} =
c_{\a}\, \vol(\rho_{\a}),
\end{equation}
and if $\a/(2 \pi i) \in \BQ- \{1\}$, then
\begin{eqnarray*}
\lbl{eq.GVCa}
\limsup_{n \to \infty} \frac{\log| f_{K,n}(\a)|}{n} &=&
c_{\a}\, \vol(\rho_{\a}),   \\
\lbl{eq.GVCb}
\liminf_{n \to \infty} \frac{\log| f_{K,n}(\a)|}{n} &=& 0,
\end{eqnarray*}
where $c_{\a} \neq 0$ are some nonzero constants.
\end{conjecture}

The distinction of $\a/(2 \pi i)$ being rational or not is a bit
with odds with the notion of {\em hyperbolic Dehn surgery}
developed by Thurston in \cite{Th}. When
$\a/(2 \pi i) $ is a rational number, the hyperbolic Dehn surgery
theorem associates an orbifold filling to the knot complement whose
volume is $\vol(\rho_{\a})$. Orbifolds are mild generalizations of
manifolds. On the other hand, when $\a/(2 \pi i)$ is irrational,
hyperbolic Dehn surgery associates a space which is topologically a
1-point compactification of the knot complement, with volume
$\vol(\rho_{\a})$. In the following, we will refer to the parameter
$\a$ in the Generalized Volume Conjecture as {\em the angle}, making
contact with standard terminology from hyperbolic geometry.


There are two rather independent parts in the Volume Conjecture:
\begin{itemize}
\item[(a)]
To show that the limit exists in \eqref{eq.GVC},
\item[(b)]
To identify the limit with the volume of the corresponding Dehn filling.
\end{itemize}

At the moment, the Generalized Volume Conjecture is known only for the $4_1$
knot and certain values of $\a$; see Murakami, \cite{M1}.




One may further ask what happens to the Generalized Volume
Conjecture when the angle $\a$ is small. For $\a=0$, it is natural
to define $\rho_0$ to be the {\em trivial} representation. Then for
$\a$ small enough, there is a unique (up to conjugation) {\em
abelian} $\SL_2(\BC)$ representation $\rho_{\a}$ that satisfies
\eqref{eq.meridian}.
Abelian representations have $0$ volume (see eg, \cite{CCGLS}).
On the other hand, for small enough
$\a$, we have $\D_K(e^{\a}) \sim \D_K(1)=1$. Thus Theorem \ref{thm.11}
implies that

\begin{theorem}
\lbl{thm.1alt}
For every knot $K$ there exists an open neighborhood $U_K$ of $0 \in \BC$,
such that for $\a \in U_K$, we have:
$$
\lim_{n \to \infty} \frac{\log| f_{K,n}(\a)|}{n}=0=\vol(\rho_{\a}).
$$
\end{theorem}

In other words, Theorem \ref{thm.11} settles the Generalized Volume
Conjecture for small complex angles.
