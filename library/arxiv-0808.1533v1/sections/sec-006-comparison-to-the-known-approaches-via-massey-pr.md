---
doc_id: arxiv-0808.1533v1
doc_title: "On the third order helicity of magnetic ﬁelds on invariant domains in S 3"
section_id: sec-006-comparison-to-the-known-approaches-via-massey-pr
section_title: "Comparison to the known approaches via Massey products."
section_number: null
pages: 27-31
source_pdf: 0808.1533v1.pdf
source_sha256: 85bb9732afdd70ea
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.547
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order helicity of a volume preserving vector ﬁeld B, which leads us to a"
duplicate_of: "arxiv-0808.1533v3"
---
[]{#sec:massey label="sec:massey"}

In several prior works [@Berger90; @Berger-Evans92; @Laurence-Stredulinsky00b; @Mayer03] higher helicities were developed via the Massey product formula for $\bar{\mu}_{123}$. These approaches should be equivalent to the one presented here in the sense that invariants obtained this way measure the same topological information. Most notably the work [@Laurence-Stredulinsky00b] provides an explicit expression for the third order helicity of the borromean flux tubes, where the ergodic interpretation in the style of Arnold's asymptotic linking number is also provided. In [@Mayer03] one finds the following formula for the third order helicity $$\label{eq:massey-3A}
 \mathsf{M}_{123}(X_1,X_2,X_3)=\int_M A_1\wedge A_2\wedge A_3,$$ where $A_i=d^{-1}(\iota_{X_i}\mu)$. This formula is valid for three distinct vector fields $X_i$ on a closed manifold $M$. For invariant domains with boundary [\[eq:massey-3A\]](#eq:massey-3A){reference-type="eqref" reference="eq:massey-3A"} defines an invariant provided $A_i\bigl|_{\partial M}=0$, but this only happens in certain situations (e.g. $M$ is simply connected, and $A_i$'s are appropriately chosen).

The most commonly known formula directly related to the Massey products was developed by Berger [@Berger90], in the case of borromean flux tubes: $\mathcal{T}=\mathcal{T}_1\cup \mathcal{T}_2\cup \mathcal{T}_3$: $$\label{eq:massey123}
 \mathsf{M}_{123}(X_1,X_2,X_3)=\int_{\partial \mathcal{T}_1} A_1\wedge F_{23}+F_{12}\wedge A_3,$$ in [@Berger90] it is expressed as a volume integral over $\mathcal{T}$ by applying so called gauge fixing. When $\mathcal{T}_i$ are topologically solid tori there exists a single Massey product $<a_1,a_2,a_3>$ in the complement: $S^3\setminus \mathcal{T}$, and the 2-form $A_1\wedge F_{23}+F_{12}\wedge A_3$ is its representative. When $\mathcal{T}_i$ are handlebodies there are multiple Massey products in the complement $S^3\setminus \mathcal{T}$, but the formula [\[eq:massey123\]](#eq:massey123){reference-type="eqref" reference="eq:massey123"} should still be valid. Such extensions were not so far considered in the literature and the volume integrals over $\mathcal{T}$ may be harder to obtain in such case. One may also point out that ergodic interpretations of Massey products are more involved, [@Laurence-Stredulinsky00b], comparing to the approach presented in Section [\[sec:ergodic\]](#sec:ergodic){reference-type="ref" reference="sec:ergodic"}.

# Appendix A: Equations for the *frozen-in-field* forms

Given a volume preserving vector field $X$ on $M$ and a path $t\longrightarrow g(t)\in \text{Diff}^\text{vol}(M)$, let $$X^t:=g_\ast(t)X\ .$$ Then for $X^0=X$, by definition $$\label{eq:euler2}
 \dot{X^t}=\frac{d}{dt} X^t\bigl|_{t=0}=-{\cal L}_V X=-[V,X],$$ and as a result $$\frac{d}{dt} \iota_{X^t}\mu|_{t=0}  =  -\iota_{[V,X]} \mu$$ Next, calculate ($\partial_t+{\cal L}_V\equiv {\cal L}_{\partial_t+V}$) $$\begin{aligned}
 (\partial_t+{\cal L}_V)\iota_{X^t}\mu & = & \partial_t(\iota_{X^t}\mu)+{\cal L}_V\iota_{X^t}\mu\\
 & = & \iota_{\dot{X^t}}\mu+\iota_{X^t}({\cal L}_V\mu)+\iota_{[V,X^t]}\mu\\
 & = & \iota_{\dot{X^t}+[V,X^t]}\mu,
\end{aligned}$$ where in the second identity we applied the general formula: $\iota_{[A,B]}={\cal L}_A\iota_B-\iota_B{\cal L}_A$, and in the third equation the fact that $V$ is volume preserving i.e. ${\cal L}_V\mu=0$. As a result of [\[eq:euler2\]](#eq:euler2){reference-type="eqref" reference="eq:euler2"} we obtain $$(\partial_t+{\cal L}_V)\iota_{X^t}\mu=0\ .$$

# Appendix B: Zero contribution of short paths to the time average

It is clear when $\beta\in \Omega^3(\widetilde{\mathcal{T}})$ is at least a $C^1$ on $\widetilde{\mathcal{T}}\subset S^3\times S^3\times S^3$, then $f=\beta(X_1,X_2,X_3)$ is continuous on $\widetilde{\mathcal{T}}$ and $$\begin{gathered}
\int_{\bar{\mathscr{O}}^1_T(x)}\int_{\bar{\mathscr{O}}^2_T(y)}\int_{\bar{\mathscr{O}}^3_T(z)}
f=\\
\bigl(\int_{\mathscr{O}^1_T(x)}+\int_{\sigma(\Phi^1(x,T),x)}\bigr)
\bigl(\int_{\mathscr{O}^2_T(y)}+\int_{\sigma(\Phi^2(y,T),y)}\bigr)
\bigl(\int_{\mathscr{O}^3_T(z)}+\int_{\sigma(\Phi^3(z,T),z)}\bigr)f\ .
\end{gathered}$$ After expanding, it is obvious that we must show the following (for all choices), when $T\to \infty$: $$\begin{aligned}
\label{eq:lim-sp1}
\frac{1}{T^3}\int_{\sigma(\Phi^1(x,T),x)}\int_{\mathscr{O}^2_{T}(y)}\int_{\mathscr{O}^3_{T}(z)} f & \longrightarrow & 0,\\
\label{eq:lim-sp2}\frac{1}{T^3}\int_{\sigma(\Phi^1(x,T),x)}\int_{\sigma(\Phi^2(y,T),y)}\int_{\mathscr{O}^3_{T}(z)} f & \longrightarrow & 0,\\
\label{eq:lim-sp3}\frac{1}{T^3}\int_{\sigma(\Phi^1(x,T),x)}\int_{\sigma(\Phi^2(y,T),y)}\int_{\sigma(\Phi^3(z,T),z)} f & \longrightarrow & 0.
\end{aligned}$$ Since the lengths of the short paths in $\mathcal{S}$ are bounded by a common constant $d$, [\[eq:lim-sp1\]](#eq:lim-sp1){reference-type="eqref" reference="eq:lim-sp1"}-[\[eq:lim-sp3\]](#eq:lim-sp3){reference-type="eqref" reference="eq:lim-sp3"} follow immediately, e.g. for [\[eq:lim-sp1\]](#eq:lim-sp1){reference-type="eqref" reference="eq:lim-sp1"} we have

$$\begin{gathered}
\bigl|\frac{1}{T^3}\int_{\sigma(\Phi^1(x,T),x)}\int_{\mathscr{O}^2_{T}(y)}\int_{\mathscr{O}^3_{T}(z)} f\bigr|\leq \frac{1}{T^3} d(T+d)(T+d)\|f\|_{\infty} \longrightarrow  0.
\end{gathered}$$

# Appendix C: Notation

We adopt notation from the elegant exposition in [@Schwarz95]. Let $M$ be an orientable manifold with smooth boundary.

-   $\Omega^k(M)=C^\infty(M,\Lambda^k)$, smooth differential forms on $M$.

-   $\Omega^k_N(M)=\{\phi\in \Omega^k(M)\ |\ \mathbf{n}\phi=0,\, \mathbf{n}d\phi=0\}$ the subspace satisfying the Neumann boundary conditions, ($\mathbf{n}$ denotes a normal component of a form along $\partial M$).

The $L^2$-inner product on $\Omega^k(M)$ is defined as $$\bigl( \omega,\eta\bigr)_{L^2}=\int_M \omega\wedge\ast \eta,$$

-   $L^2\Omega^k(M)$, $L^2$-differential forms on $M$.

-   $H^s\Omega^k(M)$ the Sobolev space of differential $k$-forms with $s$ weak "derivatives" in $L^2$.

-   $\mathcal{H}^k_N(M)=\{\lambda\in H^1\Omega^k(M)\ |\ d\lambda=\delta\lambda=0, \mathbf{n}\lambda=0\}$ the subspace of the Neumann harmonic fields.

Next we justify [\[eq:potential-neumann\]](#eq:potential-neumann){reference-type="eqref" reference="eq:potential-neumann"}, first observe that for any $\gamma\in H^1\Omega^{k-1}(M)$: $$\label{eq:perp-neumann}
 (d\gamma,\lambda)_{L^2}=\int_{\partial M} \mathbf{t}\gamma\wedge\ast\mathbf{n}\lambda=0,\qquad \forall \lambda\in \mathcal{H}^k_N(M),$$ as a result if $\omega \in \mathcal{H}^k_N(M)^\perp$ we obtain a solution $\phi$ to the Neumann problem: $$\label{eq:neumann-phi}
 \delta d\phi+d\delta\phi=\omega,\quad \Rightarrow\quad \omega-d\delta\phi=\delta d\phi\ .$$ Formula [\[eq:perp-neumann\]](#eq:perp-neumann){reference-type="eqref" reference="eq:perp-neumann"} implies: $(\omega-d\delta\phi)\in \mathcal{H}^k_N(M)^\perp$, moreover $\mathbf{n}(\omega-d\delta\phi)=\mathbf{n}(\delta d\phi)=\delta\,\mathbf{n}(d\phi)=0$, by the boundary condition in [\[eq:neumann-problem\]](#eq:neumann-problem){reference-type="eqref" reference="eq:neumann-problem"}. If $\omega$ is a closed form, $\omega-d\delta\phi$ is also closed, and clearly coclosed by [\[eq:neumann-phi\]](#eq:neumann-phi){reference-type="eqref" reference="eq:neumann-phi"}. Thus $\omega-d\delta\phi$ is a harmonic field with zero normal component, and therefore it has to be in $\mathcal{H}^k_N(M)$, and therefore the zero form. This yields $$\omega=d\delta\phi\ .$$ As a result we obtain a necessary and sufficient conditions for $\omega$ to be exact:

-   $d\omega=0$,

-   $(\omega,\lambda)_{L^2}=0$, $\forall\lambda\in \mathcal{H}^k_N(M)$.
