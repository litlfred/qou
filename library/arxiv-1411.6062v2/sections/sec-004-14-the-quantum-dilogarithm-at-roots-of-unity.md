---
doc_id: arxiv-1411.6062v2
doc_title: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-004-14-the-quantum-dilogarithm-at-roots-of-unity
section_title: "The quantum dilogarithm at roots of unity"
section_number: 1.4
pages: 6-7
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.898
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quantum diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨uller theory"
---
[]{#sub.evalphi label="sub.evalphi"}

We fix an admissible pair $(M,N)$. Recall $\mathsf{b}$ and $\mathsf{s}$ from Equation [\[eq.bs\]](#eq.bs){reference-type="eqref" reference="eq.bs"}. Let $\mathrm{Li}_2(z)=\sum_{n=1}^\infty \frac{z^n}{n^2}$ denote the Euler dilogarithm, defined for $|z|<1$ and analytically continued as a multivalued function on $\mathbbm C\setminus\{0,1\}$.

::: theorem
[]{#thm.2 label="thm.2"} We have: $$\label{eq.Phieval}
\operatorname{\Phi}_{\mathsf{b}}\!\left(\frac{z}{2\pi\mathsf{s}}-c_{\mathsf{b}}\right)=
\frac{e^{\frac{\mathsf{i}}{2\pi\mathsf{s}^2}\operatorname{Li_2}(e^{z})}
\left(1-e^z\right)^{1+\frac{\mathsf{i}z}{2\pi\mathsf{s}^2}}}{
\operatorname{D}_N(e^{z/N};q_+)\operatorname{D}_M(e^{z/M};q_-)} \,.$$
:::

It is remarkable that the left-hand side is a meromorphic function of $z$ whereas the right hand side is assembled out of multivalued functions of $z$.

In particular when $M=1$, we obtain that $$\label{eq.evalphiN}
\operatorname{\Phi}_{\mathsf{b}}(x-c_{\mathsf{b}})= \frac{e^{-\frac{1}{2 \pi \mathsf{i}N}\mathrm{Li}_2(z^N)}}{
\operatorname{D}_N(z)}
(1-z^N)^{1+ \frac{\mathsf{i}x}{\sqrt{N}}}, \qquad z=e^{2 \pi \mathsf{b} x} \,,$$ and when $M=N=1$, we obtain that $$\label{eq.phi1}
\operatorname{\Phi}_{1}(x)=\exp\left( \frac{\mathsf{i}}{2 \pi} \left( \mathrm{Li}_2(e^{2 \pi x})+2 \pi x
\log(1-e^{2 \pi x})\right)\right) \,.$$

By using the equality $$\frac{\operatorname{\Phi}_{\mathsf{b}}\!\left(\frac{z}{2\pi\mathsf{s}}-c_{\mathsf{b}}\right)}
{\operatorname{\Phi}_{\mathsf{b}}\!\left(\frac{z}{2\pi\mathsf{s}}+c_{\mathsf{b}}\right)}=
\left(1-e^{z/N}\right)\left(1-e^{z/M}\right)$$ we also have $$\label{eq.Phieval+}
\operatorname{\Phi}_{\mathsf{b}}\!\left(\frac{z}{2\pi\mathsf{s}}+c_{\mathsf{b}}\right)=
\frac{e^{\frac{\mathsf{i}}{2\pi\mathsf{s}^2}\operatorname{Li_2}(e^{z})}
\left(1-e^z\right)^{1+\frac{\mathsf{i}z}{2\pi\mathsf{s}^2}}}{
\slashed{\operatorname{D}}_N(e^{z/N};q_+)
\slashed{\operatorname{D}}_M(e^{z/M};q_-)},$$

::: remark
[]{#rem.ORV label="rem.ORV"} The cyclic dilogarithm is in a sense a radial limit of the generating series $$M(x,q)=\prod_{n=1}^\infty \frac{1}{(1-x q^n)^n}$$ where $M(x,q)$ is the McMahon generating series of 3-dimensional *plane partitions*; see [@top-vertex] and [@ORV Sec.2.1]. The latter appear in M-theory and mirror symmetry. It would be interesting and useful to understand a precise relation between the function $\operatorname{D}_N$ and plane partitions.
:::
