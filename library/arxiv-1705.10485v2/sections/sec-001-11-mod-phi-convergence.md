---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-001-11-mod-phi-convergence
section_title: "Mod-$\phi$ convergence"
section_number: 1.1
pages: 1-2
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.946
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
Let $(X_n)_{n \in \mathbb{N}}$ be a sequence of real-valued random variables. In many situations, there exists a scale $s_n$ and a limiting law $\phi$ which is infinitely divisible, such that $(X_n/s_n)_{n\in \mathbb{N}}$ converges in law towards $\phi$. For instance, in the classical central limit theorem, if $X_n=\sum_{i=1}^n A_i$ is a sum of centered i.i.d. random variables with $\mathbb{E}[(A_1)^2]<\infty$, then $$s_n=\sqrt{n\,\mathbb{E}[(A_1)^2]}$$ and the limit is the standard Gaussian distribution $\mathcal{N}_{\mathbb{R}}(0,1)$. In [@JKN11] and the subsequent papers [@DKN11; @FMN16], the notion of mod-$\phi$ convergence was developed in order to get quantitative estimates on the convergence $\frac{X_n}{s_n} \rightharpoonup \phi$ (throughout the paper, $\rightharpoonup$ denotes convergence in distribution).

::: definition
[]{#def:modphi label="def:modphi"} Let $\phi$ be an infinitely divisible probability measure, and $D \subset \mathbb{C}$ be a subset of the complex plane, which we assume to contain $0$. We assume that the Laplace transform of $\phi$ is well defined over $D$, with Lévy exponent $\eta$: $$\forall z \in D,\,\,\,\int_{\mathbb{R}} \E^{zx}\,\phi(\!\,d\hspace*{-0.3mm}{x})=\E^{\eta(z)}.$$ We then say that $(X_n)_{n \in \mathbb{N}}$ converges mod-$\phi$ over $D$, with parameters $(t_n)_{n \in \mathbb{N}}$ and limiting function $\psi : D \to \mathbb{C}$, if $t_n \to + \infty$ and if, locally uniformly on $D$, $$\lim_{n \to \infty} \mathbb{E}[\E^{zX_n}]\,\E^{-t_n\eta(z)} = \psi(z).$$
:::

If $D=\I \mathbb{R}$, we shall just speak of mod-$\phi$ convergence; it is then convenient to use the notation $$\begin{aligned}
\theta_n(\xi)&=\mathbb{E}[\E^{\I \xi X_n}]\,\E^{-t_n\eta(\I \xi)};\\
\theta(\xi)&= \psi(\I\xi),
\end{aligned}$$ so that mod-$\phi$ convergence corresponds to $\lim_{n \to \infty}\theta_n(\xi)= \theta(\xi)$ (uniformly for $\xi$ in compact subsets of $\mathbb{R}$). When nothing is specified, in this paper, we implicitly consider that $D=\I\mathbb{R}$. When $D=\mathbb{C}$ we shall speak of *complex* mod-$\phi$ convergence. In some situations, it is also appropriate to study mod-$\phi$ convergence on a band $\mathbb{R}\times \I[-b,b]$, or $[-c,c] \times \I\mathbb{R}$ (see [@FMN16; @MN15]).

Intuitively, a sequence of random variables $(X_n)_{n \in \mathbb{N}}$ converges mod-$\phi$ if it can be seen as a large renormalization of the infinitely divisible law $\phi$, plus some residue which is asymptotically encoded in the Fourier or Laplace sense by the limiting function $\psi$. Then, $\phi$ will typically be:

1.  in the case of lattice-valued distributions, a Poisson law or a compound Poisson law (*cf.* [@BKN09; @KN10; @FMN16; @CDMN15]);

2.  or, a *stable distribution*, for instance a Gaussian law.

In this paper, we shall only be interested in the second case. Background on stable distributions is given at the end of this introduction (Section [\[Sect:Background_Stable\]](#Sect:Background_Stable){reference-type="ref" reference="Sect:Background_Stable"}). In particular we will see that, if $\phi$ is a stable distribution, then the mod-$\phi$ convergence of $X_n$ implies the convergence in distribution of a renormalized version $Y_n$ of $X_n$ to $\phi$ (Proposition [\[prop:clt\]](#prop:clt){reference-type="ref" reference="prop:clt"}).

We believe that mod-$\phi$ is a kind of universality class behind the central limit theorem (or its stable version) in the following sense. For many sequences $(X_n)_{n \in \mathbb{N}}$ of random variables that are proven to be asymptotically normal (or converging to a stable distribution), it is possible to prove mod-$\phi$ convergence; we refer to our monograph [@FMN16] or Sections [\[Sect:First\]](#Sect:First){reference-type="ref" reference="Sect:First"}-[\[sec:markov\]](#sec:markov){reference-type="ref" reference="sec:markov"} below for such examples. These estimates on the Laplace transform/characteristic function can then be used to derive in an automatic way some *companion theorems*, refining the central limit theorem. In [@FMN16], we discuss in details the question of moderate/large deviation estimates and of finding the *normality zone*.

In the present paper, we shall be interested in the speed of convergence towards the Gaussian (or more generally the stable) distribution of the appropriate renormalization $Y_n$ of $X_n$. To obtain sharp bounds on this speed of convergence, we do not work with mod-$\phi$ convergence, but we introduce the notion of *zone of control* for the renormalized characteristic function $\theta_n(\xi)$. In many examples, such a zone of control can be obtained by essentially the same arguments used to prove mod-$\phi$ convergence, and in most examples, mod-$\phi$ convergence actually holds.
