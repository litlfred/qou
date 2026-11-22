---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMATION"
section_id: sec-009-22-boundary-terms
section_title: "Boundary terms"
section_number: 2.2
pages: 9-10
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.903
latex_coverage_ratio: 0.986
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp shape."
---
[]{#subsec:boundary-terms label="subsec:boundary-terms"}

Our proof of Theorem [\[thm:main-cusp\]](#thm:main-cusp){reference-type="ref" reference="thm:main-cusp"} will involve certain boundary terms. In this section, we define these terms. We explain how they arise and recall certain properties. They will be used in the proof of Theorem [\[thm:main-cusp\]](#thm:main-cusp){reference-type="ref" reference="thm:main-cusp"}.

Using results of the last section, we may always assume that we have a harmonic representative $\omega = \eta + i*D\eta$. Thus $\eta$ satisfies equation ([\[eqn:d\*deta\]](#eqn:d*deta){reference-type="ref" reference="eqn:d*deta"}).

Let $N$ be any submanifold of $X = M-\Sigma$ with boundary $\partial
N$ oriented by the outward normal. When we take the $L^2$ inner product of equation ([\[eqn:d\*deta\]](#eqn:d*deta){reference-type="ref" reference="eqn:d*deta"}) with $\eta$ and integrate by parts over $N$, we obtain the boundary formula ([@hk:univ Lemma 2.3]): $$B(N)= \int_{\partial N} \eta \wedge *D\eta = \| \eta \|^2_N + \|
  *D\eta \|^2_N 
  \label{eqn:BN}$$ Here $\| \cdot \|$ denotes the $L^2$--norm on $N$. We will apply equation ([\[eqn:BN\]](#eqn:BN){reference-type="ref" reference="eqn:BN"}) to submanifolds of $X=M-\Sigma$ involving tubular or horoball neighborhoods.

First, we will introduce some notation. Let $V_j$ be a tubular neighborhood of a component (the $j$-th component) of the singular locus, or a horoball neighborhood of a cusp. Using similar notation to that of [@hk:univ], define $$b_{V_j}(\zeta,\xi)=\int_{\partial V_j}*D\zeta\wedge \xi,$$ where $\partial V_j$ is oriented such that the tangent vector orthogonal to $\partial V_j$ is an outward normal when viewed from $V_j$. We will be considering $b_{V_j}(\eta, \eta)$ in this paper, and we review results concerning this term.

The decomposition ([\[eqn:omega-decomp\]](#eqn:omega-decomp){reference-type="ref" reference="eqn:omega-decomp"}) of $\omega$ in $V_j$ into $\omega_0 + \omega_c$, and $\eta$ into $\eta_0 + \eta_c$ decomposes the term $b_{V_j}(\eta, \eta)$: $$b_{V_j}(\eta, \eta) = b_{V_j}(\eta_0, \eta_0) +
b_{V_j}(\eta_c, \eta_c).
\label{eqn:bV-decomp}$$ That is, cross terms vanish ([@hk:univ Lemma 2.5]). Additionally, the term $b_{V_j}(\eta_c, \eta_c)$ is actually non-positive ([@hk:univ Lemma 2.6]), so we find $$b_{V_j}(\eta, \eta) \leq b_{V_j}(\eta_0, \eta_0)
\label{eqn:eta<eta_0}$$

Now, let $V$ be a tubular neighborhood of the entire singular locus $\Sigma$, as well as horoball neighborhoods of cusps. Thus $V$ is a union of tubular neighborhoods $V_j$ of components $\Sigma_j$ of the singular locus and horoball neighborhoods $U_j$. Then letting $N=X-V$ in equation ([\[eqn:BN\]](#eqn:BN){reference-type="ref" reference="eqn:BN"}), $$\begin{aligned}
B(X-V)  & = &\| \eta \|^2_{X-V} + \|*D\eta\|^2_{X-V} =
 \int_{\partial V} *D\eta \wedge \eta \\
 & = &
 \sum_j b_{V_j} (\eta, \eta) + \sum_k b_{U_j}(\eta,\eta).
\label{eqn:sumbj=eta}
\end{aligned}$$ The first sum is over all components of the singular locus, the second over all horoball neighborhoods of cusps. This equation, along with equation ([\[eqn:eta\<eta_0\]](#eqn:eta<eta_0){reference-type="ref" reference="eqn:eta<eta_0"}), implies $$0 \leq  \sum_j b_{V_j} (\eta, \eta)+ \sum_k
  b_{U_k}(\eta,\eta)  \leq \sum_j b_{V_j} (\eta_0,
  \eta_0) + \sum_k b_{U_k} (\eta_0, \eta_0).
\label{eqn:sum>0}$$

Notice $\eta_0 = (\eta_0)_j$ depends on the neighborhood $V_j$ or $U_j$. However, using the notation $b_{V_j}(\eta_0, \eta_0)$, it should be clear that we are referring to the decomposition of $\eta$ particular to $V_j$ in this context, and similarly for $U_j$. We will further simplify notation, using the following definition.

::: define
Let $\Sigma_j$ be a component of the singular locus $\Sigma$. Let $V_j$ be a tubular neighborhood of $\Sigma_j$ of radius $R$. We let $b_j$ be the boundary term: $$b_j = b_{V_j}(\eta_0, \eta_0).$$ []{#def:bj label="def:bj"}
:::

::: remark
Note that for our applications of the results of this section, the one--form $\omega$ corresponds to an infinitesimal deformation of hyperbolic structure at time $t$. Thus $\omega$, $\eta$, $\eta_0$, $b_j$, etc. will all depend on time $t$ in our applications in future sections.

To avoid a notational nightmare, in the sequel we will assume the time $t$ has been fixed, and continue writing these terms without reference to $t$, except occasionally where we feel recalling the dependency on $t$ will help avoid confusion.
:::

# Change in Cusp Shape []{#sec:cusp-est label="sec:cusp-est"}

In Section [\[sec:deform-cone\]](#sec:deform-cone){reference-type="ref" reference="sec:deform-cone"}, we set up notation and reviewed known results. Given this information, we are ready to begin the proof of Theorem [\[thm:main-cusp\]](#thm:main-cusp){reference-type="ref" reference="thm:main-cusp"}.
