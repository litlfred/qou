---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.964
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
Let $(X_n)_{n \in \N}$ be a sequence of real-valued random variables. In the series of papers \cite{JKN11,DKN11,KN10,KN12,FMN13}, we introduced the notion of mod-Gaussian convergence (and more generally of mod-convergence with respect to an infinitely divisible law $\phi$):

\begin{definition}\label{def:mod}
The sequence $(X_n)_{n \in \N}$ is said to converge in the mod-Gaussian sense with parameters $t_n \to +\infty$ and limiting (or residue) function $\theta$ if, locally uniformly in $\R$,
$$\esper[\E^{\I t X_n}]\,\E^{\frac{t_n\,t^2}{2}} = \theta(t) \,(1+o(1)),$$
where $\theta$ is a continuous function on $\R$ with $\theta(0)=1$. 

\end{definition}

\noindent A trivial situation of mod-Gaussian convergence is when $X_n=G_n+Y_n$ is the sum of a Gaussian variable of variance $t_n$ and of an independent random variable $Y_n$ that converges in law to a variable $Y$ with characteristic function $\theta$. More generally $X_n$ can be thought of as a Gaussian variable of variance $t_n$, plus a noise which is encoded by the multiplicative residue $\theta$ in the characteristic function. In this setting, $\theta$ is not necessarily the characteristic function of a random variable (the residual noise). For instance, consider $$X_n=\frac{1}{n^{1/3}}\sum_{i=1}^n Y_i,$$ where the $Y_i$ are centred, independent and identically distributed random variables with convergent moment generating function. Then a Taylor expansion of $\esper[\E^{\I t Y}]$ shows that $(X_n)_{n \in \N}$ converges in the mod-Gaussian sense with parameters $n^{1/3}\,\mathrm{Var}(Y)$ and limiting function $$\theta(t)=\exp\left(\frac{\esper[Y^3]\,(\I t)^3}{6}\right),$$
which is not the characteristic function of a random variable, since it does not go to zero as $t$ goes to infinity. In 2008, during the workshop "\textit{Random matrices, L-functions and primes}" held in Z\"urich, Marc Yor asked the second author A.~N. about the role of the limiting function $\theta$. In \cite{KNN13} it is proved that the set of possible limiting functions is the set of continuous functions $\theta$ from $\R$ to $\CC$ such that $\theta(0)=1$ and $\theta(-t)=\bar\theta(t)$ for $t\in\R$. But this characterization does not say anything on the probabilistic information encoded in $\theta$.  We now wish to develop more on  probabilistic interpretations of the limiting function and the implications of mod-Gaussian convergence in terms of classical limit theorems of probability theory.
\bigskip

We first note that  by looking at $\esper[\E^{\I t X_n/\sqrt{t_n}}]$, one immediately sees that mod-Gaussian convergence implies a central limit theorem for the sequence $(\frac{X_n}{\sqrt{t_n}})$:
\begin{equation}
\frac{X_n}{\sqrt{t_n}} \rightharpoonup_{n \to \infty} \mathcal{N}(0,1),\label{eq:clt}
\end{equation}
where the convergence above holds in law (see \cite[\S 2-3]{JKN11} for more details on this). On the other hand, with somewhat stronger hypotheses on the remainder $o(1)$ that appears in Definition \ref{def:mod}, a local limit theorem also holds, see \cite[Theorem 4]{KN12} and \cite[Theorem 5]{DKN11}:
$$\proba[X_n \in B] = \proba[G_n \in B]\, (1+o(1)) = \frac{m(B)}{\sqrt{2\pi t_n}}\,(1+o(1))$$
for relatively compact sets $B$ with $m(\partial B)=0$, $m$ denoting the Lebesgue measure. \bigskip

In \cite{FMN13}, it is then explained that by looking at Laplace transforms instead of characteristic functions, and by assuming the convergence holds on a whole band of the complex plane, one can obtain in the setting of mod-Gaussian convergence precise estimates of moderate or large deviations. In fact these results provide a new probabilistic interpretation of the limiting function as a measure of the "breaking of symmetry"  in the Gaussian approximation of the tails of $X_n$ (see \S\ref{subsec:brisesymm} for more details).
\bigskip

The goal of this paper is threefold:\vspace{2mm}
\begin{itemize}
\item to propose a new interpretation of the limiting function in the framework of mod-Gaussian convergence with Laplace transforms; these results allow us in particular to recover some well known exotic limit theorems from statistical mechanics due to Ellis and Newman \cite{EN78} and similar one for other models or in higher dimensions.\vspace{2mm}
\item to show that once one is able to prove mod-Gaussian convergence, then one can expect to obtain finer results than merely convergence in law, such as speed of convergence and local limit theorems. Results on the rate of convergence in the Curie-Weiss model were recently obtained using Stein's method (see \emph{e.g.} \cite{EL10}) while the local limit theorem, to the best of our knowledge, is new.\vspace{2mm}
\item to explore the applications of the results obtained in \cite{FMN13} on the "breaking of symmetry" in the central limit theorem  to some classical models of statistical mechanics. In particular our approach determines the scale up to which the Gaussian approximation for the tails is valid and its breaking at this critical scale.\vspace{2mm}
\end{itemize}
Our results are best illustrated with some classical one-dimensional models from statistical mechanics, such as the Curie-Weiss model or the Ising model. To illustrate the flexibility of our approach, we shall also prove similar results for weighted symmetric random walks in dimensions $2$ and $3$. The statistics of interest to us will be the total magnetization, which can be written as a sum of dependent random variables. These examples add to the already large class of examples of sums of dependent random variables we have already been able to deal with in the context of mod-$\phi$ convergence. 
\bigskip

In the remaining of the introduction we recall the results obtained in \cite{FMN13} which led us to the "breaking of symmetry" interpretation, as well as an underlying method of cumulants that enabled us to establish the mod-Gaussian convergence for a large family of sums of dependent random variables. The important aspect of the cumulant method is that it provides a tool to prove mod-Gaussian convergence in situations where one cannot explicitly compute the characteristic function. We eventually give an outline of the paper.
\medskip
