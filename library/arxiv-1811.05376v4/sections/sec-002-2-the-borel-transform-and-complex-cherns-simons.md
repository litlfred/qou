---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-002-2-the-borel-transform-and-complex-cherns-simons
section_title: "The Borel transform and Complex Cherns-Simons"
section_number: 2
pages: 15-17
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.985
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphere X we show that the q-series invariant ˆZ0(X; q) introduced by"
---
[]{#sec:BOREL label="sec:BOREL"}

We now provide the proof of Theorem [\[2.1\]](#2.1){reference-type="ref" reference="2.1"}. The reader not familiar with the Borel transform $\mathcal{B}$ and its relation to the Laplace transform is encouraged to read Section [\[sec:Borel\]](#sec:Borel){reference-type="ref" reference="sec:Borel"}, before reading the proof of Theorem [\[2.1\]](#2.1){reference-type="ref" reference="2.1"}. For a measurable function $g:\mathbb{R}_+ \rightarrow \mathbb{C}$ of sufficient decay, we use the notation $\mathcal{L}_{\mathbb{R}_+}(g)$ for the Laplace transform -- see Equation [\[eq:Laplacetransform\]](#eq:Laplacetransform){reference-type="eqref" reference="eq:Laplacetransform"}.

::: proof
*Proof of Theorem [\[2.1\]](#2.1){reference-type="ref" reference="2.1"}.* We start by giving a characterization of which of the phases in [\[phasedecomp\]](#phasedecomp){reference-type="eqref" reference="phasedecomp"} give a non-zero contribution. Introduce for $\mu \in \mathbb{Q}/ \mathbb{Z}$ the set $$\begin{aligned}
\label{R}
\mathcal{T}(\mu) = & \{m=1,...,2P -1 :-m^2/4P=\mu \ \mathop{\mathrm{mod}}\ \mathbb{Z} \}
\\ =& \{m=1,...,2P -1 :g(2\pi i m)=2\pi i \mu \ \mathop{\mathrm{mod}}\ 2\pi i\mathbb{Z} \}
\end{aligned}$$

The set of phases $2\pi i R^*(X)$ in [\[expansionX\]](#expansionX){reference-type="eqref" reference="expansionX"} consists of the values $g(2\pi i m)=  \frac{-m^2 2\pi i}{4P}$ for which $$\label{sumresiduesnotzero}
\sum_{x \in \mathcal{T}(-m^2/4P)} \text{Res} \left( \frac{F(y)e^{kg(y)}}{1-e^{-ky}}, y=2\pi i x \right) \not=0,$$ for $m=1,...,2P-1$. Thus, by Corollary [\[cor:HUHU\]](#cor:HUHU){reference-type="ref" reference="cor:HUHU"}, we must prove that if [\[sumresiduesnotzero\]](#sumresiduesnotzero){reference-type="eqref" reference="sumresiduesnotzero"} holds, then there exists $\tilde m \in \mathcal{T}(-m^2/4P)$ such that at most $n-3$ of the $p_j$'s which divide $\tilde m$.

We start by noting that the set of poles of $F$ is given by $$\label{PolesofF}
\mathcal{P}_F=\{ 2\pi im \mid m \in \mathbb{Z} \ \text{and $m$ is divisible by at most $n-3$ of the $p_j$'s} \}.$$ It follows that if $\tilde m$ is divisible by at least $n-2$ of the $p_j,$ then $F(y)$ does not have a pole at $y=2\pi i \tilde m$ and we get for integral $k$ $$\begin{aligned}
\text{Res} \left( \frac{F(y)e^{kg(y)}}{1-e^{-ky}}, y=2\pi i \tilde m \right)&=F(2 \pi i \tilde m) e^{kg(2\pi i\tilde m)} \text{Res} \left(\frac{1}{1-e^{-ky}}, y=2\pi i \tilde m \right)
\\ &=F(2 \pi i \tilde m) e^{kg(2\pi i\tilde m)}\frac{1}{k}. 
\end{aligned}$$ As we already noted above, Lawrence and Rozansky checked that all the $k^{-1}$ terms cancels, so it follows that $$\sum_{\substack{\tilde m \in \mathcal{T}(-m^2/4P), \\ \text{ and $\tilde{m}$ is divisible by at least $n-2$ of the $p_j$}}}  \text{Res} \left( \frac{F(y)e^{kg(y)}}{1-e^{-ky}}, y=2\pi i \tilde m \right)=0.$$ Therefore we see that if [\[sumresiduesnotzero\]](#sumresiduesnotzero){reference-type="eqref" reference="sumresiduesnotzero"} holds, then there is some $\tilde{m} \in \mathcal{T}(-m^2/4P)$ which is divisible by at most $n-3$ of the $p_j.$ This establishes $R^*(X) \subset \mathop{\mathrm{CS}}_{\mathbb{C}}^*$ and we get [\[EXPANSIOON\]](#EXPANSIOON){reference-type="eqref" reference="EXPANSIOON"}. Observe that as a corollary we obatin for each $\theta \in \mathop{\mathrm{CS}}_{\mathbb{C}}^*$ the formula $$\label{eq:formulaforpolynomial}
e^{2\pi ik \theta} \mathop{\mathrm{Z}}_{\theta}(k)=- \sum_{\tilde m \in \mathcal{T}(\theta)}  \text{Res} \left( \frac{F(y)e^{kg(y)}}{1-e^{-ky}}, y=2\pi i \tilde m \right).$$

We now turn to $\mathcal{B}(\mathop{\mathrm{Z}}_{0}).$ The formal series $\mathop{\mathrm{Z}}_{0}$ is the the asymptotic expansion of the Laplace integral $$\mathop{\mathrm{Z}}^{\mathop{\mathrm{I}}}(k)=\frac{1}{2\pi i} \int_{\gamma} F(y) e^{kg(y)} \ \mathop{\mathrm{{d}\hskip-.6mm}}y.$$ Let $G$ be the rational function introduced in [\[eq:G\]](#eq:G){reference-type="eqref" reference="eq:G"} and introduce the multivalued function $\mathcal{B}_0(\zeta)$ given by $$\mathcal{B}_0(\zeta)= \frac{\kappa}{\pi i \sqrt{\zeta}} G\left( \exp\left(\frac{\kappa\sqrt{\zeta}}{P} \right)\right)= \frac{\kappa i}{4\pi } \frac{\prod_{j=1}^n \sinh\left(\frac{\kappa\sqrt{\zeta}}{p_j}\right)}{ \sqrt{\zeta} \left(\sinh\left(\kappa\sqrt{\zeta}\right)\right)^{n-2}}.$$ With this notation, the equation for the Borel transform [\[ComputingBorel\]](#ComputingBorel){reference-type="eqref" reference="ComputingBorel"} which we want to prove, reads as follows $$\label{eq:reduction}
\mathcal{B}(\mathop{\mathrm{Z}}_0)= \mathcal{B}_0.$$ The function $\mathcal{B}_0$ is related to $F$ as follows $$\label{eq:BORELLO}
\mathcal{B}_0(\zeta)=\frac{\sqrt{ 2 P }}{ \sqrt{\pi i\zeta}} F\left(\sqrt{8\pi i P \zeta}\right).$$ Now as, $F(-y)=F(y)$ we have a convergent power series expansion valid for $y$ close to $0$ $$F(y)=\sum_{m=1}^{\infty} \frac{F^{(2m)}(0)}{(2m)!} y^{2m}.$$ Therefore Equation [\[eq:BORELLO\]](#eq:BORELLO){reference-type="eqref" reference="eq:BORELLO"} implies that if we set $$B_m=  \frac{1}{2 \pi i} \sqrt{8\pi i P} \frac{F^{(2m)}(0)}{(2m)!}  \left(8\pi i P \right)^{m}$$ then we have a convergent expansion valid for $\zeta$ close to $0$ of the form $$\label{eq:zetanearzero}
\mathcal{B}_0(\zeta) = \sum_{m=1}^{\infty}  B_m \zeta^{m-1/2}.$$ Introduce the variable $t$ defined by $$-t=g(y)= \frac{ i y^2}{8 \pi P}.$$ Thus $$\mathop{\mathrm{{d}\hskip-.6mm}}y= \frac12 \sqrt{\frac{8 \pi i P }{  t}} \mathop{\mathrm{{d}\hskip-.6mm}}t.$$ We now rewrite $\mathop{\mathrm{Z}}^{\mathop{\mathrm{I}}}(k)$ as the Laplace transform of $\mathcal{B}_0$ $$\begin{aligned}
 \label{ComputeBorel} \begin{split}
\mathop{\mathrm{Z}}^{\mathop{\mathrm{I}}}(k)&= \frac{1}{2 \pi i} \int_\gamma F(y) e^{kg(y)} \ \mathop{\mathrm{{d}\hskip-.6mm}}y =  \frac{1}{2 \pi i} \int_0^{\infty} e^{-kt} \int_{g=t} \frac{F}{\mathop{\mathrm{{d}\hskip-.6mm}}g} \ \mathop{\mathrm{{d}\hskip-.6mm}}t
\\ &= \frac{1}{2 \pi i} \int_0^{\infty} e^{-kt} \sqrt{\frac{8 \pi i P}{ t}} F\left(\sqrt{8\pi i Pt}\right) \ \mathop{\mathrm{{d}\hskip-.6mm}}t
\\ &= \int_0^{\infty} e^{-kt} \mathcal{B}_0(t) \ \mathop{\mathrm{{d}\hskip-.6mm}}t = \mathcal{L}_{\mathbb{R}_+} (\mathcal{B}_0)(k).
 \end{split}
\end{aligned}$$ The existence of the asymptotic expansion [\[expansionX\]](#expansionX){reference-type="eqref" reference="expansionX"}

$$\mathop{\mathrm{Z}}^{\mathop{\mathrm{I}}}(k)= \mathcal{L}_{\mathbb{R}_+} (\mathcal{B}_0)(k) \sim_{k \rightarrow \infty}  \mathop{\mathrm{Z}}_0(k)$$ can now be obtained by appealing to the first part of Lemma [\[lem:masterlemma\]](#lem:masterlemma){reference-type="ref" reference="lem:masterlemma"} where we set $B=\mathcal{B}_0$. Here we use the existence of the expansion [\[eq:zetanearzero\]](#eq:zetanearzero){reference-type="eqref" reference="eq:zetanearzero"}. Therefore the desired identity [\[ComputingBorel\]](#ComputingBorel){reference-type="eqref" reference="ComputingBorel"} $\mathcal{B}(\mathop{\mathrm{Z}}_0)=\mathcal{B}_0$ follows from the second part of Lemma [\[lem:masterlemma\]](#lem:masterlemma){reference-type="ref" reference="lem:masterlemma"} and the convergence of the expansion [\[eq:zetanearzero\]](#eq:zetanearzero){reference-type="eqref" reference="eq:zetanearzero"}.

As $F(-y)=F(y)$ we note that the factor

$$\zeta \mapsto F\left(\sqrt{8\pi iP\zeta}\right)$$ gives a well-defined meromorphic function. Thus $\mathcal{B}(\mathop{\mathrm{Z}}_{0})(\zeta)$ is a multivalued meromorphic function with a square root singularity at $0$ and with singularities for $\sqrt{8\pi iP\zeta} \in  \mathcal{P}_F$ where $\mathcal{P}_F$ is the set of poles of $F(y).$ This set was computed above (see equation [\[PolesofF\]](#PolesofF){reference-type="eqref" reference="PolesofF"}) and we conclude that the poles of $\mathcal{B}(\mathop{\mathrm{Z}}_{0})(\zeta)$ occur at

$$\zeta_m=\frac{ -\pi  m^2}{2iP}=\frac{- m^2}{4P} \frac{2\pi }{i}$$ with $m\in \mathbb{Z}$ being divisible by less than or equal to $n-3$ of the $p_j$'s. This concludes the proof of [\[Inclu\]](#Inclu){reference-type="eqref" reference="Inclu"}. ◻
:::

It is of course expected that only a Chern-Simons invariant $\theta$ of a flat $\mathop{\mathrm{SU}}(2)$ connection have a non-vanishing polynomial $\mathop{\mathrm{Z}}_{\theta} \not=0,$ i.e. $$R^*(X)=\mathop{\mathrm{S_{CS}}}(\mathcal{M}^*\left(X,\mathop{\mathrm{SU}}(2)\right) ).$$
