---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 4-5
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.992
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\subsection{Mod-\texorpdfstring{$\phi$}{phi} convergence}
The notion of mod-$\phi$ convergence has been studied in the articles \cite{JKN11,DKN11,KN10,KN12,BKN09}, in connection with problems from number theory, random matrix theory and  probability theory. The main idea was to look for a natural renormalization of the characteristic functions of random variables which do not converge in law (instead of a renormalization of the random variables themselves). After this renormalization, the sequence of characteristic functions converges to some non-trivial limiting function. Here is the definition of mod-$\phi$ convergence that we will use throughout this article
(see Section~\ref{subsec:discussion_hypotheses} for a discussion on the different parts of this definition).

\begin{definition}\label{def:modphi}
    Let $(X_{n})_{n \in \N}$ be a sequence of real-valued random variables,
    and let us denote by \hbox{$\varphi_{n}(z)=\esper[\E^{zX_{n}}]$} their moment generating functions, which we assume to all exist in a strip 
    $$\mathcal{S}_{(c,d)}=\{z,\,\,c < \Re\, z <d\},$$
     with $c<d$ extended real numbers (we allow $c=-\infty$ and $d=+\infty$). We assume that there exists a non-constant infinitely divisible distribution $\phi$ with moment generating function $\int_{\R} \E^{zx}\, \phi(dx)=\exp(\eta(z))$ that is well defined on $\mathcal{S}_{(c,d)}$, and an analytic function $\psi(z)$ that does not vanish on the real part of $\mathcal{S}_{(c,d)}$, such that locally uniformly in $z \in \mathcal{S}_{(c,d)}$, 
\begin{equation}
\exp(-t_{n}\,\eta(z))\,\varphi_{n}(z) \to \psi(z),\label{eq:modphi}
\end{equation}
where $(t_{n})_{n \in \N}$  is some sequence going to $+\infty$. We then say that $(X_{n})_{n \in \N}$ \emph{converges mod-$\phi$} on $\mathcal{S}_{(c,d)}$, with parameters $(t_{n})_{n \in \N}$ and limiting function $\psi$. In the following we denote $\psi_{n}(z)$ the left-hand side of \eqref{eq:modphi}.
\end{definition}\medskip

\noindent When $\phi$ is the standard Gaussian (resp.~Poisson) distribution, we will speak of mod-Gaussian (resp.~mod-Poisson) convergence. 
Besides, unless explicitely stat\-ed, we shall always assume that $0$ belongs to the band of convergence $\mathcal{S}_{(c,d)}$, \emph{i.e.}, $c<0<d$. Under this assumption, Definition \ref{def:modphi} implies mod-$\phi$ convergence in the sense of \cite[Definition 1.1]{JKN11} or \cite[Section 2]{DKN11}.\bigskip    

It is immediate to see that mod-$\phi$ convergence implies a \emph{central limit theorem} if the sequence of parameters $t_{n}$ goes to infinity (see the remark after Theorem \ref{thm:cltlattice}). But in fact there is much more information encoded in mod-$\phi$ convergence than merely the central limit theorem. Indeed, mod-$\phi$ convergence appears as a natural extension of the framework of sums of independent random variables (see Example \ref{ex:sumiid}): many interesting asymptotic results  that hold for sums of independent random variables can also be established for sequences of random variables converging in the mod-$\phi$ sense (\cite{JKN11,DKN11,KN10, KN12, BKN09}). For instance, under some general extra assumptions on the convergence in Equation \eqref{eq:modphi}, it is proved in \cite{DKN11,KN12,FMN14} that one can establish local limit theorems for the random variables $X_n$. Then the local limit theorem of Stone appears as a special case of the local limit theorem for mod-$\phi$ convergent sequences.
But the latter also applies to a variety of situations where the random variables under consideration exhibit some dependence structure (\emph{e.g.} the Riemann zeta function on the critical line,  some probabilistic models of primes, the winding number for the planar Brownian motion, the characteristic polynomial of random  matrices, finite fields $L$-functions, \emph{etc.}). It is also shown in \cite{BKN09} that mod-Poisson convergence (in fact mod-$\phi$ convergence for $\phi$ a lattice distribution) implies very sharp distributional approximation in the total variation distance (among other distances) for a large class of random variables. 
In particular, the total number of distinct prime divisors $\omega(n)$ of an integer $n$ chosen at random can be approximated in the total variation distance with an arbitrary precision by explicitly computable measures. \bigskip

Besides these quantitative aspects, mod-$\phi$ convergence also sheds some new light on the nature of some conjectures in analytic number theory. Indeed it is shown in \cite{KN10} that the structure of the limiting function appearing in the moments conjecture for the Riemann zeta function by Keating and Snaith \cite{KS1} is shared by other arithmetic functions and that the limiting function $\psi$ accounts for the fact that prime numbers do not behave independently of each other. More precisely, the limiting function $\psi$ can be used to measure the deviation of the true result from what the  probabilistic models based on a naive independence assumption would predict. One should note that these naive probabilistic models are usually enough to predict central limit theorems for arithmetic functions (\emph{e.g.} the naive probabilistic model made with a sum of independent Bernoulli random variables to predict the Erd\"os-Kac central limit theorem  for $\omega(n)$ or the stochastic zeta function to predict Selberg's central limit theorem for the Riemann zeta function) but fail to predict accurately mod-$\phi$ convergence by a factor which is contained in $\psi$.
There is another example, where dependence appears in the limiting function $\psi$,
while we have independence at the scale of central limit theorem: the log of the characteristic polynomial of a random unitary matrix, as a vector in $\mathbb R^2$, converges in the mod-Gaussian sense to a limiting function which is not the product of the limiting functions of each component considered individually although when properly normalized it converges to a Gaussian vector with independent components \cite{KN12}. 
\bigskip
