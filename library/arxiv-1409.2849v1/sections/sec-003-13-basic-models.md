---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-003-13-basic-models
section_title: "Basic models"
section_number: 1.3
pages: 7-11
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.961
---
As mentioned above, the goal of the paper is to study the phenomenon of mod-Gaussian convergence for probabilistic models stemming from statistical mechanics; this extends the already long list of models for which we were able to establish this asymptotic behavior of the Fourier or Laplace transforms (\cite{JKN11,KN12,FMN13}). More precisely, we shall focus on one-dimensional spin configurations, which already yield an interesting illustration of the theory and technics of mod-Gaussian convergence. Given two parameters $\alpha \in \R$ and $\beta \in \R_+$, we recall that the Curie-Weiss model and the one-dimensional Ising model are the probability laws on spin configurations $\sigma : \lle 1,n\rre \to \{\pm 1\}$ given by
\begin{align}
\CW_{\alpha,\beta}(\sigma) &= \frac{1}{Z_n(\CW,\alpha,\beta)}\,\exp\left(\alpha \sum_{i=1}^n \sigma(i)+\frac{\beta}{2n} \left(\sum_{i=1}^n \sigma(i)\right)^{\!\!2\,}\right);\label{eq:curiemeasure}\\
\IS_{\alpha,\beta}(\sigma) &= \frac{1}{Z_n(\IS,\alpha,\beta)}\,\exp\left(\alpha \sum_{i=1}^n \sigma(i)+\beta \left(\sum_{i=1}^{n-1} \sigma(i)\,\sigma(i+1)\right)\right).\label{eq:isingmeasure}
\end{align}
The coefficient $\alpha$ measures the strength and direction of the exterior magnetic field, whereas $\beta$ measures the strength of the interaction between spins, which tend to align in the same direction. This interaction is local for the Ising model, and global for the Curie-Weiss model. Set $M_n=\sum_{i=1}^n \sigma(i)$: this is the total magnetization of the system, and a random variable under the probabilities $\CW_{\alpha,\beta}$ and $\IS_{\alpha,\beta}$.\bigskip

In Section \ref{sec:ising}, we quickly establish  the mod-Gaussian convergence of the magnetization for the Ising model, using the explicit form of the Laplace transform of the magnetization, which is given by the transfer matrix method. Alternatively, when $\alpha=0$, in the appendix, we apply the cumulant method and give an explicit formula for each elementary cumulant of spins (see Section \ref{sec:cumulantspin}). This allows us to prove the analogue for joint cumulants of the well-known fact that covariances between spins decrease exponentially with distance in the $1\mathrm{D}$-Ising model. This second method  is much less direct than the transfer matrix method, but we consider the Ising model to be a very good illustration of the method of joint cumulants. Moreover it illustrates the fact that one does not necessarily need to be able to compute precisely the moment generating function of the random variables.  
\bigskip

In Section \ref{sec:l1}, we focus on the Curie-Weiss model, and we interpret the magnetization as a change of measure on a sum of i.i.d.~random variables. Since these sums converge in the mod-Gaussian sense, it leads us to study the effect of a change of measure on a mod-Gaussian convergent sequence. We prove that in the setting of $\mathrm{L}^1$-mod-Gaussian convergence, such changes of measures either conserve the mod-Gaussian convergence (with different parameters), or lead to a convergence in law, with a limiting distribution that involves the residue $\psi$. We thus recover the results of \cite{EN78,ENR80}, and extend them to the setting of $\mathrm{L}^1$-mod-Gaussian convergence. In Section \ref{sec:rate}, using Fourier analytic arguments, we quickly recover the optimal rate of convergence of the Ellis-Newman limit theorem for the Curie-Weiss model which was recently obtained in \cite{EL10} using Stein's method, and then we establish a local limit theorem, thus completing the existing limit theorems for the Curie-Weiss model at critical temperature $\CW_{0,1}$. 
\bigskip
\bigskip



















\section{Mod-Gaussian convergence for the Ising model:\\ the transfer matrix method}\label{sec:ising}

In this section, $(\sigma(i))_{i \in \lle 1,n\rre}$ is a random configuration of spins under the Ising measure \eqref{eq:isingmeasure}, and $M_n=\sum_{i=1}^n \sigma(i)$ is its magnetization. The mod-Gaussian convergence of $M_n$ after appropriate rescaling can be obtained by two different methods: the \emph{transfer matrix method}, which yields an explicit formula for $\esper[\E^{zM_n}]$; and the \emph{cumulant method}, which gives an explicit combinatorial formula for the coefficients of the power series $\log \esper[\E^{zM_n}]$. We use here the transfer matrix method, and refer to the appendix (Section \ref{sec:cumulantspin}) for the cumulant method.

\figcap{ising1d.pdf}{Two configurations of spins under the Ising measures of parameters $(\alpha=0,\beta=0.3)$ and $(\alpha=0,\beta=1)$.}


 The Laplace transform $\esper[\E^{zM_n}]$ of the magnetization of the one-dimensional Ising model is well-known to be computable by the following transfert matrix method, see \cite[Chapter 2]{Bax82}. Introduce the matrix
$$T=\begin{pmatrix}
\E^{\alpha+\beta} & \E^{-\alpha-\beta} \\
\E^{\alpha-\beta} & \E^{-\alpha+\beta}
\end{pmatrix}, $$
and the two vectors $V=(\E^{\alpha},\E^{-\alpha})$ and $W=(\begin{smallmatrix}1 \\ 1\end{smallmatrix})$. If the rows and columns of $T$ correspond to the two signs $+1$ and $-1$, then any configuration of spins $\sigma=(\sigma(i))_{i \in \lle 1,n\rre}$ has under the Ising measure $\IS_{\alpha,\beta}$ a probability proportional to 
$$V_{\sigma(1)}T_{\sigma(1),\sigma(2)}T_{\sigma(2),\sigma(3)}\cdots T_{\sigma(n-1),\sigma(n)}.$$
Therefore, the partition function $Z_n(\IS,\alpha,\beta)$ is given by
\begin{align*}
\sum_{\sigma(1),\ldots ,\sigma(n)} V_{\sigma(1)}T_{\sigma(1),\sigma(2)}T_{\sigma(2),\sigma(3)}\cdots T_{\sigma(n-1),\sigma(n)} &= V(T)^{n-1}W\\
&=a_+(\lambda_+)^{n-1}+a_-(\lambda_-)^{n-1},
\end{align*}
where 
\begin{align*}
a_+ &= \cosh \alpha + \frac{\E^{\beta}\sinh^2\alpha + \E^{-\beta}}{\sqrt{\E^{2\beta}\sinh^2\alpha + \E^{-2\beta}}}\qquad;\qquad a_-= \cosh \alpha - \frac{\E^{\beta}\sinh^2\alpha + \E^{-\beta}}{\sqrt{\E^{2\beta}\sinh^2\alpha + \E^{-2\beta}}}\\
\lambda_+ &=\E^{\beta}\,\cosh \alpha + \sqrt{\E^{2\beta} \sinh^2\alpha + \E^{-2\beta} }\qquad;\qquad \lambda_- =\E^{\beta}\,\cosh \alpha - \sqrt{\E^{2\beta} \sinh^2\alpha + \E^{-2\beta} }.
\end{align*}
Indeed, $\lambda_{\pm}$ are the two eigenvalues of $T$, and $a_+$ and $a_-$ are obtained by identification of coefficients in the two formulas \begin{align*}
Z_1(\IS,\alpha,\beta)&=\E^{\alpha}+\E^{-\alpha}\\
Z_2(\IS,\alpha,\beta)&=\E^{2\alpha+\beta}+\E^{-2\alpha+\beta} + 2\E^{-\beta}. 
 \end{align*}
Then, the Laplace transform of $M_n$ is given by 
$$\esper_{\alpha,\beta}[\E^{zM_n}]=\frac{Z_n(\IS,\alpha+z,\beta)}{Z_n(\IS,\alpha,\beta)}.$$
In particular, 
$$
\esper_{\alpha,\beta}[M_n]=\left.\frac{\partial \esper[\E^{zM_n}]}{\partial z}\right|_{z=0} = \frac{\partial }{\partial \alpha} \log Z_n(\IS,\alpha,\beta)= n \,\frac{\E^{\beta}\sinh\alpha }{\sqrt{\E^{2\beta}\sinh^2 \alpha+\E^{-2\beta}}}+O(1).
$$
whence a formula for the (asymptotic) mean magnetization by spin: $$\overline{m}=\frac{\E^{\beta}\sinh\alpha}{\sqrt{\E^{2\beta} \sinh^2 \alpha + \E^{-2\beta}}}.$$\bigskip

A more precise Taylor expansion of $Z_n(\IS,\alpha+z,\beta)$ leads to the following:

\begin{theorem}\label{thm:modgaussising}
Under the Ising measure $\IS_{\alpha,\beta}$, $\frac{M_n-n\overline{m}}{n^{1/3}}$ converges in the complex mod-Gaussian sense with parameters $$t_n = n^{1/3}\,\frac{\E^{-\beta}\cosh \alpha}{(\E^{2\beta}\sinh^2\alpha+\E^{-2\beta})^{3/2}}$$
and limiting function
$$\psi(z)=\exp\left(-\frac{2\E^{\beta}\sinh^3 \alpha+(3\E^{\beta}-\E^{-3\beta})\sinh\alpha}{6(\E^{2\beta}\sinh^2\alpha+\E^{-2\beta})^{5/2}}\,z^3\right).$$
\end{theorem}

\begin{proof} In the following, we are dealing with square roots and logarithms of complex numbers, but each time in a neighborhood of $\R_+^*$, so there is no ambiguity in the choice of the branches of these functions. That said, it is easier to work with log-Laplace transforms:
\begin{align*}
\log \esper\!\left[\E^{z\,\frac{M_n-n\overline{m}}{n^{1/3}}}\right]&= \log Z_n\left(\IS,\alpha + \frac{z}{n^{1/3}},\beta\right)-\log Z_n(\IS,\alpha,\beta)-zn^{2/3}\overline{m}\\
\log Z_n(\IS,\alpha,\beta) &= \log a_+(\alpha,\beta) + (n-1) \log \lambda_+(\alpha,\beta) + o(1)\\
\log Z_n\left(\IS,\alpha+ \frac{z}{n^{1/3}},\beta\right) &= \log a_+\left(\alpha+ \frac{z}{n^{1/3}},\beta\right) + (n-1) \log \lambda_+\left(\alpha+ \frac{z}{n^{1/3}},\beta\right) + o(1)\\
&= \log a_+(\alpha,\beta) + (n-1) \log \lambda_+(\alpha,\beta)+zn^{2/3} \frac{\partial}{\partial \alpha}\left(\log \lambda_+(\alpha,\beta)\right)\\
&\quad + \frac{z^2n^{1/3}}{2} \frac{\partial^2}{\partial \alpha^2}\left(\log \lambda_+(\alpha,\beta)\right) + \frac{z^3}{6} \frac{\partial^3}{\partial \alpha^3}\left(\log \lambda_+(\alpha,\beta)\right) +o(1).
\end{align*}
Thus, it suffices to compute the first derivatives of $\log \lambda_+(\alpha,\beta)$ with respect to $\alpha$:
\begin{align*}
\log \lambda_+(\alpha,\beta)&=\log\left(\E^{\beta}\cosh\alpha + \sqrt{\E^{2\beta}\sinh^2 \alpha + \E^{-2\beta}}\right)\\
\frac{\partial}{\partial \alpha}\left(\log \lambda_+(\alpha,\beta)\right)&=\frac{\E^{\beta}\sinh\alpha}{\sqrt{\E^{2\beta} \sinh^2 \alpha + \E^{-2\beta}}}=\overline{m}\\
\frac{\partial^2}{\partial \alpha^2}\left(\log \lambda_+(\alpha,\beta)\right)&=\frac{\E^{-\beta}\cosh \alpha}{(\E^{2\beta}\sinh^2\alpha+\E^{-2\beta})^{3/2}}=\sigma^2\\
\frac{\partial^3}{\partial \alpha^3}\left(\log \lambda_+(\alpha,\beta)\right)&=-\frac{2\E^{\beta}\sinh^3 \alpha+(3\E^{\beta}-\E^{-3\beta})\sinh\alpha}{(\E^{2\beta}\sinh^2\alpha+\E^{-2\beta})^{5/2}}=K_3.
\end{align*}
We therefore get
$$\log \esper\!\left[\E^{z\,\frac{M_n-n\overline{m}}{n^{1/3}}}\right] = n^{1/3}\,\frac{\sigma^2\, z^2}{2}+\frac{K_3\,z^3}{6}+o(1).$$
\end{proof}
\bigskip

By using Formula \ref{eq:upbound}, this result leads to new estimates of moderate deviations for the probability $\proba_{\alpha,\beta}[M_n \geq n\overline{m}+n^{1/3}x]$. In the special case when $\alpha=0$, the limiting function $\psi(z)$ of Theorem \ref{thm:modgaussising} is equal to $1$, and one has to push the expansion of $\log Z_n(\IS,0,\beta)$ to order $4$ to get a meaningful mod-Gaussian convergence (the same phenomenon will occur in the case of the Curie-Weiss model):

\begin{theorem}\label{thm:modgaussising2}
Under the Ising measure $\IS_{0,\beta}$, $\frac{M_n}{n^{1/4}}$ converges in the complex mod-Gaussian sense with parameters $t_n=n^{1/2}\,\E^{2\beta}$ and limiting function 
$$\psi(z)=\exp\left(-\frac{3\E^{6\beta}-\E^{2\beta}}{24}\,z^4\right).$$
\end{theorem}
\bigskip
\bigskip















\section{Mod-Gaussian convergence in $\mathrm{L}^1$ and the Curie-Weiss model}\label{sec:l1}

In this Section, $(X_n)_{n \in \N}$ is a sequence of random variables with entire moment generating series $\esper[\E^{zX_n}]$, and we assume the following:\vspace{2mm}
\begin{enumerate}[(A)]
\item One has mod-Gaussian convergence of the Laplace transforms, \emph{i.e.}, there is a sequence $t_n \to +\infty$ and a function $\psi$ continuous on $\R$ such that
$$\psi_n(t)=\esper[\E^{tX_n}]\,\E^{-\frac{t_n\,t^2}{2}}$$
converges locally uniformly on $\R$ to $\psi(t)$.\label{hyp:laplacemod}\vspace{1mm}
\item Each function $\psi_n$, and their limit $\psi$ are in $\mathrm{L}^1(\R)$.\label{hyp:l1mod}\vspace{1mm}
\end{enumerate}
We denote $\proba_n$ the law of $X_n$, 
\begin{equation}
\qproba_n[dx]=\frac{\E^{\frac{x^2}{2t_n}}}{\esper\!\left[\E^{\frac{(X_n)^2}{2t_n}}\right]}\,\,\proba_n[dx],\label{eq:exponchange}
\end{equation}
and $Y_n$ a random variable under the new law $\qproba_n$. Note that hypothesis \eqref{hyp:l1mod} implies that $Z_n=\esper[\E^{(X_n)^2/2t_n}]$ is finite for all $n \in \N$. Indeed,
$$
\int_{\R} \psi_n(t)\,dt = \esper\!\left[\int_{\R} \E^{t X_n-\frac{t_n \,t^2}{2}}\,dt\right]=\esper\!\left[\E^{\frac{(X_n)^2}{2t_n}}\,\left(\int_\R \E^{-\frac{(X_n-t_n t)^2}{2t_n}}\,dt\right)\right]=\sqrt{\frac{2\pi}{t_n}}\,\,\esper\!\left[\E^{\frac{(X_n)^2}{2t_n}}\right].
$$
Therefore the new probability measures $\qproba_n$ are well defined. The goal of this section is  to study the asymptotics of the new sequence $(Y_n)_{n \in \N}$. As we shall see in \S\ref{subsec:curieweiss}, the Curie-Weiss model defined by Equation \eqref{eq:curiemeasure} is one of the main examples in this framework. However, it is more convenient to look at the general problem, and we shall introduce later other models concerned by our general results.
\medskip
