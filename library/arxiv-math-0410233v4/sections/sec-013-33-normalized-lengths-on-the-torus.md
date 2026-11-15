---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMATION"
section_id: sec-013-33-normalized-lengths-on-the-torus
section_title: "Normalized lengths on the torus"
section_number: 3.3
pages: 15-17
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.843
latex_coverage_ratio: 0.96
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp shape."
---
[]{#sec:normlength label="sec:normlength"}

We are interested in determining how *normalized lengths* of curves on the torus $\partial U$ change over the deformation.

::: define
Let $\beta$ be a slope on the torus $T$, that is, an isotopy class of simple closed curves. The normalized length of $\beta$ is defined to be: $$\mbox{Normalized length}(\beta) =
  \frac{\mbox{Length}(\beta)}{\sqrt{\mbox{Area}(T)}},$$ where $\mbox{Length}(\beta)$ is defined to be the length of a geodesic representative of $\beta$ on $T$.
:::

::: lemma
Let $\beta$ be a slope on $\partial U_t$. Let $L_t(\beta)$ denote its normalized length, with derivative $\dot{L}(\beta)$. Then $L_t(\beta)$ satisfies: $$-\|\gamma'(t)\| \, L_t(\beta) \;\leq\; \dot{L}(\beta) \;\leq\;
   \|\gamma'(t)\| \,L_t(\beta).
  \label{eqn:norm-length-L}$$ []{#lemma:ldot-bound label="lemma:ldot-bound"}
:::

::: proof
*Proof.* Fix a time $t=t_0$. We will show the lemma for $t_0$.

We saw in the proof of Lemma [\[lemma:a+b-gamma\]](#lemma:a+b-gamma){reference-type="ref" reference="lemma:a+b-gamma"} that $\gamma(t)$ agrees infinitesimally with an explicit Teichmüller geodesic $\zeta(u)$ determined by the matrix $A$ of equation ([\[eqn:define-A\]](#eqn:define-A){reference-type="ref" reference="eqn:define-A"}) when $t=t_0$ and $u=0$. More specifically, $\zeta(u)$ multiplies vectors along $F_1$ by $\exp(-u\sqrt{a^2+b^2})$, and multiplies vectors along $F_2$ by $\exp(u\sqrt{a^2+b^2})$, where $F_1$ and $F_2$ are orthogonal geodesic foliations (determined by the matrix $A$) on the torus $\partial U_{t_0}$. Thus we will prove the lemma by showing it is true when the change in metric on $\partial U_{t_0}$ is given by $\zeta(u)$.

Now, $L_t(\beta)$ is defined to be the length of a geodesic representative of $\beta$ divided by $\sqrt{\rm{Area}(\partial U_t)}$. Without loss of generality, we may assume that $\rm{Area}(\partial
U_t) = 1$, since $\gamma'(t)$ is given by a trace free (hence area preserving) matrix $A$. Thus $L_t(\beta)$ is just the length of a geodesic representative of $\beta$ at time $t_0$.

Let $\hat{\beta}_{t_0}\colon\thinspace I \to \partial U_{t_0}$ be a geodesic representative of $\beta$ at time $t_0$. Then $\hat{\beta}_{t_0}$ makes some angle $\theta$ with the foliation $F_1$. For any $u$, $\zeta(u)$ takes $\hat{\beta}_{t_0}$ to a new geodesic, still with slope $\beta$, and length $L_u(\beta) = \alpha_u(\theta) \,
L_{t_0}(\beta)$. Here $$\alpha_u(\theta)
= \sqrt{\cos^2\theta \,\exp(-2u\sqrt{a^2+b^2}) +\sin^2\theta \exp(2u\sqrt{a^2+b^2})}$$ is maximized when $\theta=\pi/2$ and minimized when $\theta=0$. Thus we have $$\exp(-\sqrt{a^2+b^2}\,u)\,L_{t_0}(\beta) \leq L_u(\beta) \leq
\exp(\sqrt{a^2+b^2}\,u) \,L_{t_0}(\beta).$$

Since $\left.\frac{d}{dt}\right|_{t=t_0} L_t(\beta) =
\left.\frac{d}{du}\right|_{u=0} L_u(\beta),$ $$-\sqrt{a^2+b^2} \, L_{t_0}(\beta) \leq \left.\frac{d}{dt}\right|_{t=t_0}
L_t(\beta) \leq \sqrt{a^2+b^2}\, L_{t_0}(\beta).$$ ◻
:::

Combining this with the inequality of Theorem [\[thm:cusp-1\]](#thm:cusp-1){reference-type="ref" reference="thm:cusp-1"}, we obtain the following theorem.

::: theorem
Let $L_t$ be the normalized length of a slope on a cusp torus $\partial U_t$ under a cone deformation, with derivative $\dot{L} =
  \frac{d}{dt} L_t$. Then the change in $L_t$ is bounded by the following inequality: $$-\left(\sqrt{\frac{\sum b_i(t)}{2\mbox{Area}(\partial
        U_t)}}\right) \, L_t
    \;\leq\; \dot{L} \;\leq\;
  \left(\sqrt{\frac{\sum b_i(t)}{2\mbox{Area}(\partial U_t)}}\right)\,
  L_t.$$ []{#thm:norm-length-1 label="thm:norm-length-1"}
:::

::: proof
*Proof.* Solving for $\|\gamma'(t)\|$ in the inequality of Theorem [\[thm:cusp-1\]](#thm:cusp-1){reference-type="ref" reference="thm:cusp-1"}, we find $$\|\gamma'(t)\| \leq \sqrt{\frac{\sum b_j(t)}{2\mbox{Area}(\partial
      U_t)}}.$$ The result is given by substituting this into equation ([\[eqn:norm-length-L\]](#eqn:norm-length-L){reference-type="ref" reference="eqn:norm-length-L"}). ◻
:::

### Normalized height

For our applications, the curve on the torus we are particularly interested in is the one running orthogonal to the meridian. When we are dealing with link complements in $S^3$, as in a future section of this paper, there is a well defined meridian on a cusp torus. Otherwise, choose the shortest nontrivial simple closed curve on the initial cusp torus to be the meridian (for our applications to knots and links in $S^3$, these choices will agree).

We will be interested in estimating the length of the next shortest nontrivial simple closed curve. This length will be at least as long as the length of the arc orthogonal to the meridian.

At time $t$, let $p_t$ denote the geodesic arc perpendicular to the meridian, running from meridian to meridian on $\partial U_t$. This arc will generally not be a closed curve. Let $h_t$ be the normalized length of $p_t$, that is, $h_t =
\rm{Length}(p_t)/\sqrt{\rm{Area}(\partial U_t)}$. We refer to $h_t$ as the *normalized height* of the torus at time $t$. Denote its derivative at time $t$ by $\dot{h}$.

::: lemma
The normalized height $h_t$ satisfies $$-\sqrt{a^2+b^2}\,h_t \leq \dot{h} \leq
\sqrt{a^2+b^2}\,h_t.$$ []{#lemma:hdot-bound label="lemma:hdot-bound"}
:::

::: proof
*Proof.* Let $\mu$ denote the meridian slope, with $L_t(\mu)$ its normalized length at time $t$. Then $h_t L_t(\mu) = 1$. Thus $$\frac{\dot{h}}{h_t} + \frac{\dot{L}(\mu)}{L_t(\mu)} = 0.$$ By Lemma [\[lemma:ldot-bound\]](#lemma:ldot-bound){reference-type="ref" reference="lemma:ldot-bound"} and Lemma [\[lemma:a+b-gamma\]](#lemma:a+b-gamma){reference-type="ref" reference="lemma:a+b-gamma"}, $$-\sqrt{a^2+b^2} \leq \frac{\dot{L}(\mu)}{L_t(\mu)} \leq
\sqrt{a^2+b^2}.$$ Hence $-\sqrt{a^2+b^2}\,h_t \leq \dot{h} \leq
\sqrt{a^2+b^2}\,h_t.$ ◻
:::

Again Lemma [\[lemma:hdot-bound\]](#lemma:hdot-bound){reference-type="ref" reference="lemma:hdot-bound"}, combined with the inequality of Theorem [\[thm:cusp-1\]](#thm:cusp-1){reference-type="ref" reference="thm:cusp-1"}, gives $$-\left(\sqrt{\frac{\sum b_i}{2\mbox{Area}(\partial U_t)}}\right) \,
h_t \leq \dot{h} \leq
\left(\sqrt{\frac{\sum b_i}{2\mbox{Area}(\partial U_t)}}\right) \,
h_t
\label{eqn:norm-height}$$

We simplify equation ([\[eqn:norm-height\]](#eqn:norm-height){reference-type="ref" reference="eqn:norm-height"}) by noting the area of $U_t$ is given by the length of the meridian times the actual length of the arc $p_t$. Recall that the length of $p_t$ is $\sqrt{\mbox{Area}(\partial U_t)}\,L_t(p_t) =
\sqrt{\mbox{Area}(\partial U_t)}h_t.$ So denoting the length of the meridian of $\partial U_t$ by $m_t$, we have $$\sqrt{\mbox{Area}(\partial U_t)} = m_t h_t.$$

Putting this into equation ([\[eqn:norm-height\]](#eqn:norm-height){reference-type="ref" reference="eqn:norm-height"}), we obtain:

::: theorem
Let $M$ be a hyperbolic 3--manifold with a cusp, and let $X$ be a hyperbolic 3--manifold which can be joined to $M$ by a smooth family of hyperbolic cone manifolds. Let $h_t$ denote the normalized height at time $t$ of the cusp which deforms to the cusp of $M$, and let $m_t$ denote the length of its meridian. Finally, denote by $\dot{h}$ the derivative of $h_t$. Then $$-\frac{\sqrt{\sum b_i(t)}}{m_t\sqrt{2}} \leq \dot{h} \leq
\frac{\sqrt{\sum b_i(t)}}{m_t\sqrt{2}}
\label{eqn:norm-height-mer}$$ []{#thm:norm-height-mer label="thm:norm-height-mer"}
:::

# Bounding the boundary terms []{#sec:bdrybound label="sec:bdrybound"}

In this section, we finish the proofs of Theorems [\[thm:main-cusp\]](#thm:main-cusp){reference-type="ref" reference="thm:main-cusp"} and [\[thm:main-norm-length\]](#thm:main-norm-length){reference-type="ref" reference="thm:main-norm-length"} by

finding a parameterization of the cone deformation for which we may bound the sum $\sum b_j$.

In order to bound $\sum b_j$, we need more explicit formulas for the $b_j$. Recall that $b_j$ was defined in Definition [\[def:bj\]](#def:bj){reference-type="ref" reference="def:bj"} as: $$b_j = b_{V_j}(\eta_0, \eta_0).$$ Here $\eta_0$ is the real part of the 1--form $\omega_0$ in the $j$-th component $V_j$ of a tubular neighborhood of the singular locus. Thus we begin by revisiting our decomposition of $\omega_0$ in $V_j$.
