---
doc_id: arxiv-1411.6062v2
doc_title: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-003-13-evaluation-of-state-integrals
section_title: "Evaluation of state-integrals"
section_number: 1.3
pages: 4-6
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.975
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quantum diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨uller theory"
---
[]{#sub.evaluation label="sub.evaluation"}

Our main theorem evaluates the state-integral at $\mathsf{b}^2=M/N$ in terms of the state-sums $G_{M,N}$, the Rogers dilogarithm and the cyclic dilogarithm.

Fix an admissible pair $(M,N)$, and define $$\label{eq.bs}
\mathsf{b}= \sqrt{M/N}, \qquad \mathsf{s}= \sqrt{MN} \,.$$ Let $$\label{eq.calS}
\mathcal{S}=\{ w \,\, | \,\, 
\operatorname{g}(e^{2\pi\mathsf{s}w})=1, 
\,\, 0 < \mathsf{s}\, \mathrm{Im}(w)-\lambda < 1 \},$$ where $\lambda$ is a generic real number such that $$\label{eq.lambda}
-(M+N)/2 < \lambda < 0$$ and $$\operatorname{g}(z)=
(-z)^{A} (1-z)^{-B} \in \mathbbm Q[z^{\pm 1}] \,.$$ Note that if $w \in\mathcal{S}$, then $e^{2\pi\mathsf{s}w}$ is an algebraic number with a fixed choice of $N$ and $M$-th roots.

::: theorem
[]{#thm.1 label="thm.1"} When $\mathsf{b}^2=M/N$ we have: $$\begin{aligned}
\label{eq.Ib}
\mathcal I_{A,B}(\mathsf{b}) &=
e^{\pi\mathsf{i}\frac{B+3A(M+N+1)^2-6 M N}{12 M N}} 


\mathsf{s}^{-1}
\sum_{w \in \mathcal{S}}
\frac{e^{\frac{\mathsf{i}B}{2\pi \mathsf{s}^2}\operatorname{R}(z)} 
(1-z)^{\frac{(2N+1)(2M+1)}{4 M N}B}
}{z \operatorname{g}'(z) \slashed{\operatorname{D}}_N(\theta_+,q_+)^{B} 
\slashed{\operatorname{D}}_M(\theta_-,q_-)^{B}}  
G_{M,N}(\theta_+,\theta_-) \,,
\end{aligned}$$ where $$\label{eq.conventions}
z=e^{2\pi\mathsf{s}w}, \quad
\theta_+ =e^{2\pi\mathsf{b}w}=z^{1/N}, \quad \theta_- =
e^{2\pi\mathsf{b}^{-1}w}=z^{1/M}, \quad 
q_+ = \zeta_N^M, \quad q_-=\zeta_M^N \,.$$
:::

Note that when $\operatorname{g}(z)=1$, we have $$\label{eq.gp}
\operatorname{g}'(z)=A z^{-1} + B (1-z)^{-1} \,.$$

::: corollary
[]{#cor.1 label="cor.1"} For $M=1$ we obtain that $$\label{eq.IbN}
\mathcal I_{A,B}(\mathsf{b})=
e^{\pi\mathsf{i}\frac{B+3 A (N+2)^2-6N}{12 N}} 
\frac{1}{\sqrt{N}}
\sum_{w \in \mathcal{S}}
e^{\frac{\mathsf{i}B}{2\pi N}\operatorname{R}(z)}
\frac{(1-z)^{\frac{2N+3}{4N}B}}{
(A+B z/(1-z)) \slashed{\operatorname{D}}_N(\theta_+,q_+)^{B}}  
G^+_N(\theta_+) \,.$$ When $M=N=1$ we obtain that $$\label{eq.Ib1}
\mathcal I_{A,B}(1)=
e^{\pi\mathsf{i}\frac{B+3 A -6}{12}} 
\sum_{w \in \mathcal{S}}
e^{\frac{\mathsf{i}B}{2\pi}\operatorname{R}(z)}
\frac{(1-z)^{\frac{B}{4}}}{(A+B z/(1-z))} \,.$$
:::

Let us denote $$\label{eq.ex}
\mathsf{e}(x)=e^{2 \pi \mathsf{i}x} \,.$$

::: corollary
[]{#cor.41.b=1 label="cor.41.b=1"} When $M=N=1$ and $(A,B)=(1,2)$, we choose $\lambda$ to be a negative real number near zero,

$$\begin{aligned}
\operatorname{g}(z) &=-z(1-z)^{-2} \\
\mathcal{S}&= \{\mathsf{i}/6, 5 \mathsf{i}/6 \} \\
z_\pm &= \mathsf{e}(\pm1/6)\\
e^{\pi\mathsf{i}\frac{B+3 A -6}{12}} &= \mathsf{e}\left(-\frac{1}{24}\right) \\
(e^{\frac{\mathsf{i}B}{2\pi}\operatorname{R} (z_+)} ,
e^{\frac{\mathsf{i}B}{2\pi}\operatorname{R} (z_-)} )
&= \left(e^{-C} \mathsf{e}\left(-\frac{1}{24}\right),
- e^{C} \mathsf{e}\left(-\frac{1}{24}\right) 
\mathsf{e}\left(\frac{1}{3}\right) \right)
\\
\frac{(1-z_\pm)^{\frac{B}{4}}}{(A+B z_\pm/(1-z_\pm))}
&=\frac{1}{\sqrt{3}} \mathsf{e}\left(\mp \frac{1}{3}\right)
\end{aligned}$$ where $C=V/(2\pi)$ and $V$ is the volume of the $4_1$ knot. When computing the Rogers dilogarithm of $z_\pm$, keep in mind that we use the branches of the logarithm $\log z_+= 2 \pi \mathsf{i}/6$ and $\log z_-= 10 \pi \mathsf{i}/6$ dictated by Equations [\[eq.calS\]](#eq.calS){reference-type="eqref" reference="eq.calS"} and [\[eq.lambda\]](#eq.lambda){reference-type="eqref" reference="eq.lambda"}.

The above computation, combined with Equation [\[eq.Ib1\]](#eq.Ib1){reference-type="eqref" reference="eq.Ib1"} implies Equation [\[eq.I211\]](#eq.I211){reference-type="eqref" reference="eq.I211"}. As was already mentioned, the proof of this equation was a main motivation for the results of our paper.
:::

We now make few remarks about the number-theoretic, analytic and geometric properties of Equation [\[eq.Ib\]](#eq.Ib){reference-type="eqref" reference="eq.Ib"}.

::: remark
[]{#rem.algebraic label="rem.algebraic"} It [@GZ1] (see also [@DG2]) it was observed that although $(G^+(\theta_+))^N$ and $(\slashed{\operatorname{D}}_N(\theta_+,\zeta_N))^N$ lie in the field $F_{G,N}=\mathbbm Q(\theta_+,\zeta_N)$, their ratio lies in the smaller field $\mathbbm Q(z,\zeta_N)$ (where $z$ satisfies $\operatorname{g}(z)=1$) which is an extension of $\mathbbm Q(z)$ by $\zeta_N$. In particular, the above mentioned ratio is independent of the choice of the $N$-th root of $z$.
:::

::: remark
[]{#rem.multivalued label="rem.multivalued"} Although $\slashed{\operatorname{D}}_N$ is a multivalued function, the sum in Equation [\[eq.Ib\]](#eq.Ib){reference-type="eqref" reference="eq.Ib"} is well-defined. This is a consequence of Theorem [\[thm.2\]](#thm.2){reference-type="ref" reference="thm.2"} below and the fact that the quantum dilogarithm is a meromorphic function.
:::

::: remark
[]{#rem.parabolic label="rem.parabolic"} When the state-integral is associated with a cusped hyperbolic manifold $M$, the set $\mathcal{S}$ is often in bijection with the set of nonabelian parabolic $\mathrm{PSL}(2,\mathbbm C)$ representations of $M$. Under such a bijection, the Rogers dilogarithm matches with the complex volume, and the value of $g'(z)$ matches with the value of the 1-loop invariant of [@DG], suitably normalized. For an illustration, see Section [\[sub.pretzel\]](#sub.pretzel){reference-type="ref" reference="sub.pretzel"}.
:::

::: remark
[]{#rem.QHG label="rem.QHG"} When the state-integral is associated with a cusped hyperbolic manifold $M$ and the identification of Remark [\[rem.parabolic\]](#rem.parabolic){reference-type="ref" reference="rem.parabolic"} is available, one can identify Equation [\[eq.Ib\]](#eq.Ib){reference-type="eqref" reference="eq.Ib"} with a sum of invariants of $M$ parametrized by nonabelian parabolic $\mathrm{PSL}(2,\mathbbm C)$ representations of $M$. Such invariants appear in Quantum Hyperbolic Geometry--see [@K97] and also [@BB]. The invariants of Quantum Hyperbolic Geometry are defined up to multiplication by an $N$-root of unity. However, Equation [\[eq.Ib\]](#eq.Ib){reference-type="eqref" reference="eq.Ib"} gives a well-defined *relative* choice of the $N$-th roots of unity. This is a consequence of the meromorphicity of the quantum dilogarithm.
:::

::: remark
[]{#rem.taylor label="rem.taylor"} As we already mentioned above, a numerical computation by the first author and Zagier suggests an explicit formula for the Taylor series of $\mathcal I_{1,2}(\mathsf{b})$ at $\mathsf{b}=1$ in terms of the asymptotics of the Kashaev invariant at $q=1$. We expect that the Taylor series of state-integrals at $\mathsf{b}=\sqrt{M/N}$ can be expressed in terms of the loop invariants of Garoufalidis--Dimofte [@DG2]. We plan to study this in a later publication.
:::

Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"} follows from a lemma from complex analysis regarding integrals of quasi-periodic functions [\[lem.main\]](#lem.main){reference-type="ref" reference="lem.main"}. This lemma is used twice, once to evaluate the quantum dilogarithm in terms of the cyclic dilogarithm, and another time to evaluate the state-integral $\mathcal I_{A,B}(\mathsf{b})$.
