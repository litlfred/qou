---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-003-13-basic-models
section_title: "Basic models"
section_number: 1.3
pages: 7-8
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.977
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
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
