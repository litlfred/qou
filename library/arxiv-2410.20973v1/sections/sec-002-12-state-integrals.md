---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-002-12-state-integrals
section_title: "State integrals"
section_number: 1.2
pages: 4-5
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.983
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜no [9] that perturbative series associated with the hyperbolic knots 41 and 52 are resurgent and"
---
We are interested in the resurgent and summability properties of the series $\Phi_{\Xi}(\hbar)$, which was defined in terms of the quantum dilogarithm $\Psi(z,\hbar)$ in Equation~\eqref{eq:def.phi}. The latter was shown to be resurgent and Borel--Laplace summable to a function given in terms of Faddeev's quantum dilogarithm $\Phi(z;\tau)$ (see~\cite{GK:resQD,andersen.mero}). The function $\Phi(z;\tau)$ is a meromorphic function of $(z,\tau)\in\BC\times(\BC\backslash\BR_{\leq0})$ with poles located on a cone $z\in\BZ_{\geq0}+\tau\BZ_{\geq0}$ and zeros located on the opposite cone $z\in\BZ_{<0}+\tau\BZ_{<0}$. In addition, it has a variety of descriptions
\be\label{eq:fad.expressions}
  \frac{(q\e(z);q)_{\infty}}{(\e(z/\tau);\tq)_{\infty}}
  
  
  
  
  
  
  \=
  \Phi(z;\tau)
  \=
  \exp\Big(
    \int_{i\sqrt{\tau}\BR+\varepsilon\sqrt{\tau}}\frac{\e((z+1+\tau)w/\tau)}{(\e(w)-1)(\e(w/\tau)-1)}
    \frac{dw}{w}
  \Big)\,,
\ee
where $(x;q)_{k}=\prod_{j=0}^{k-1}(1-q^jx)$, the first equality holds for $\tau\in\BH$, and the second for $\Re(-\sqrt{\tau}-1/\sqrt{\tau})<\Re(z/\sqrt{\tau})<0$. We refer to~\cite{AK:I,Faddeev} and Appendix~\ref{app:Faddeev} for general properties of the function~$\Phi(z;\tau)$. We can now consider integrals of the same form as Equation~\eqref{eq:form.int} replacing\footnote{The relation between the variables is $\hbar=-2\pi i/\tau$.} $\Psi(z,\hbar)$ by $\Phi(z\tau;\tau)$: for $(A,B)\in\BZ_{>0}^2$ with $A\neq B$ and $m,\ell\in\BZ$ we define
\be\label{eq:state_int}
\calI_{m,\ell}(\tau)
\;:=\;
\mu_8^B\tq^{-B/24}q^{B/24}
\int_{\calJ_{\ell,\tau}}\Phi((z-\ell)\tau;\tau)^B \e\Big(\frac{A}{2} z(z\tau+\tau+1)+mz\tau\Big) dz\,,
\ee
where $\calJ_{\ell,\tau}:=(\tfrac{i}{\sqrt{\tau}}e^{-iA\epsilon}\BR_{\geq0}-\frac{1}{2}+\ell)\cup(\tfrac{i}{\sqrt{\tau}}e^{-i(A-B)\epsilon}\BR_{\leq0}-\frac{1}{2}+\ell)$ for some small $\epsilon>0$. The fact that $\Phi(z;\tau)$ is meromorphic for $\tau\in\BC\backslash\BR_{\leq0}$ implies that $\calI_{m,\ell}(\tau)$ is holomorphic for $\tau\in\BC\backslash\BR_{\leq0}$.
These integrals are not independent. Indeed, using the quasi-periodicity of Faddeev's quantum dilogarithm, $\Phi(z-\tau;\tau)=(1-\e(z))\Phi(z;\tau)$,
one easily finds the relations
\be\label{eq:state_integral_1}
\sum_{k=0}^B\binom{B}{k}(-1)^kq^{-\ell k}\calI_{m+ k,\ell}(\tau)
\=
\calI_{m,\ell+1}(\tau)
\=(-1)^A q^{A+m}\calI_{m+ A,\ell}(\tau)\,.
\ee
Therefore, over the field $\BQ(q)$ there are $\max\{A,B\}$ independent integrals. The Andersen--Kashaev state integrals for $4_1$ and $5_2$ given in~\cite{AK:I} correspond to $m=\ell=0$. 

The conjectural description of the resurgent structure of the series $\Phi_{K}$ requires the introduction of all of the $\max\{A,B\}$ integrals~\cite{GGM:I}. What was not previously clear was how to construct the explicit combination of state integrals to give the Borel--Laplace resummation of one of the asymptotic series of interest. In Section~\ref{sec:alg}, we describe an algorithm to compute this combination using the geometry of the function~$V$ and the asymptotics of Faddeev's quantum dilogarithm. 

\medskip

To understand the asymptotics of $\Phi(z\tau;\tau)$ for large $\tau$, we need to consider an unusual but useful principle branch of the dilogarithm function. For $\theta\in(0,2\pi)$ define the domain $\BC_{\theta}=\BC\backslash\big((\BZ_{\geq0}+e^{i\theta}\BR_{\leq0})\cup(\BZ_{<0}+ e^{i\theta}\BR_{\geq0})\big)$ depicted in Figure~\ref{fig:prin.bran.fad}. 

\begin{figure}[ht]
\begin{tikzpicture}[scale=0.5]
\draw[<->,thick] (0,-3) -- (0,3);
\draw[<->,thick] (-7.5,0) -- (7.5,0);
\foreach \x in {-6,-4,-2,0,2,4,6}{\filldraw[red](\x,0) circle (2pt);};
\draw[red] (0,0) -- (3,-3);
\draw[red] (2,0) -- (2+3,-3);
\draw[red] (4,0) -- (4+3,-3);
\draw[red] (6,0) -- (6+1,-1);
\draw[red] (-2,0) -- (-2-3,3);
\draw[red] (-4,0) -- (-4-3,3);
\draw[red] (-6,0) -- (-6-1,1);
\end{tikzpicture}
\caption{Domain of $\mathrm{D}_{3\pi/4}(z)$ given by $\BC\backslash\big((\BZ_{\geq0}+(i-1)\BR_{\leq0})\cup(\BZ_{<0}+(i-1)\BR_{\geq0})\big)$.}
\label{fig:prin.bran.fad}
\end{figure}

\noindent Define $\mathrm{D}_{\theta}:\BC_{\theta}\rightarrow\BC$ to be
\be
  \mathrm{D}_{\theta}(z)
  \=
  \int_{z}^{e^{i\theta/2}\infty}
  \int_{w}^{e^{i\theta/2}\infty}
  \frac{\e(\z)}{1-\e(\z)}d\z\,dw\,,
\ee
where the contours are contained in $\BC_{\theta}$. This branch of the dilogarithm allows for us to describe the asymptotics of $\Phi(z\tau;\tau)$.
\begin{theorem}\label{thm:fad.asymp}
Suppose that $\tau\in\BC\backslash\BR_{\leq0}$ and $\varepsilon\in\BR_{>0}$. Then as $|\tau|\rightarrow \infty$ with fixed argument and $z$ is bounded away from $\BC\backslash\BC_{\theta}$ by $\varepsilon$, there exists a constant $C>0$, independent of $\varepsilon$, such that
\be
    \Big|\e(-\mathrm{D}_{\theta}(z)\tau)\Phi(z\tau;\tau)
    -
    \e\Big(\frac{1}{2}\mathrm{D}_{\theta}'(z)
    +
    \sum_{k=2}^{K}\frac{B_k}{k!}\frac{(2\pi i)^{k-2}}{\tau^{k-1}}\Li_{2-k}(\e(z))\Big)
    \Big|
    <
    C\,\varepsilon^{-K}\,K!\,|\tau|^{-K}\,,
\ee
with $\theta=\arg(-1/\tau)\in(0,2\pi)$.
\end{theorem}
\noindent The proof of this theorem is described in Appendix~\ref{app:Faddeev} (see Theorem~\ref{thm:fad.asy.app}).
