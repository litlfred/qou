---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-013-5-integrability-of-funk-billiard-in-conics
section_title: "Integrability of Funk billiard in conics"
section_number: 5
pages: 18-22
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
text_source: latex
latex_prose_ratio: 0.603
latex_coverage_ratio: 0.947
---
[]{#sec:conics label="sec:conics"} Recall that by Example [\[exm:hyperbolic\]](#exm:hyperbolic){reference-type="ref" reference="exm:hyperbolic"}, the reflection laws of the $B^n$-Funk and Beltrami-Klein hyperbolic metrics coincide. Similarly, the Funk geodesics on a manifold $M\subset \mathop{\mathrm{int}}(B^n)$ are also those of the metric induced from hyperbolic space.

In particular, if $K$ is an ellipsoid nested in $B^n$, the Funk billiard in $K$ is completely integrable [@veselov; @tabachnikov_hyperbolic]. We now recover and refine this observation in the case of the projective plane by analyzing the Funk billiard directly. Let $K\subset \mathop{\mathrm{int}}(B)$ be nested conics in $\mathbb{P}^2$.

::: Theorem
Any given orbit in $\mathop{\mathrm{Funk}}_B(K)$ remains tangent to a conic $Q_{i}$, while the points of the outer orbit all lie on a conic $Q_o$. Furthermore, $Q_o$ belongs to the linear pencil of conics defined by $Q_K=\partial K,Q_B=\partial B$, while $Q_i$ belongs to the dual pencil. Moreover, the quadruplet $Q_i, Q_K, Q_B, Q_o$ is harmonic.
:::

We first observe that by Proposition [\[prop:duality_billiards\]](#prop:duality_billiards){reference-type="ref" reference="prop:duality_billiards"}, the existence of an inner caustic implies the existence of an outer caustic and vice versa. Moreover, the outer caustic belongs to the linear pencil of $Q_K, Q_B$ if and only if the inner caustic lies on the dual pencil.

Let us establish the existence of an outer caustic which belongs to the linear pencil through $Q_K$ and $Q_B$. We may assume $B$ is the unit disc. By applying a projective transformation preserving $B$, we may further assume that $Q_K$ is a centered ellipse, that is $Q_K=\{q:\langle Aq,q\rangle=1\}$. Consider a point $z_0\in B^c$, and let $z_1$ be its image under the outer Funk billiard map. Each $z_j$ belongs to a unique conic in the linear pencil, which is parametrized by $t\in \mathbb{R}$, $Q_t:=\{\langle (A+tI)v, v\rangle =1+t\}$. It remains to show that $t_1=t_2$, or equivalently $$\label{eq:t1t2} \frac{\langle Az_0,z_0\rangle -1}{1-|z_0|^2}= \frac{\langle Az_1,z_1\rangle -1}{1-|z_1|^2}.$$ Let $p_0\in Q_ B$ be the tangency point of $[z_0,z_1]$. Denoting $\|v\|_A:=\langle Av, v\rangle$, we have $$\frac{|z_0|^2-1}{|z_1|^2-1}=\frac{|z_0-p_0|^2}{|z_1-p|^2}=\frac{\|z_0-p_0\|_A^2}{\|z_1-p_0\|_A^2},$$ the last inequality due to the fact that $z_0,pp_0,z_1$ lie on one line. Similarly, $$\frac{\langle Az_0,z_0\rangle -1}{\langle Az_1,z_1\rangle -1}=\frac{\|z_0-q_0\|_A^2}{\|z_1-q_1\|_A^2}.$$ Thus [\[eq:t1t2\]](#eq:t1t2){reference-type="eqref" reference="eq:t1t2"} becomes

$$\frac{\|z_0-q_0\|_A}{\|z_0-p_0\|_A}=\frac{\|z_1-q_1\|_A}{\|z_1-p_0\|_A}\iff \frac{\sin\measuredangle_Az_0q_0p_0}{\sin\measuredangle_Az_0p_0q_0}=\frac{\sin\measuredangle_Az_1q_1p_0}{\sin\measuredangle_Az_1p_0q_1},$$ where $\measuredangle_A$ is the angle with respect to $\|\bullet\|_A$. As $\measuredangle_Az_0p_0q_0+\measuredangle_Az_1p_0q_1=\pi$, it remains to notice that $\measuredangle_Az_0q_0p_0=\frac12 \measuredangle_A q_0oq_1=\measuredangle_Az_1q_1p_0$.

![Outer caustic](conics1){#fig:conics1 width="0.48\\linewidth"}

For the last statement, we consider a point $z\in Q_t$, tangent to $Q_B$ at $p$ and to $Q_K$ at $q$ as in figure [2](#fig:conics2){reference-type="ref" reference="fig:conics2"}.

![Relating the inner and outer caustics](conics2_new){#fig:conics2 width="0.48\\linewidth"}

Define the conic $Q$ by $Q^{-1}:=(Q_B^{-1}Q_o)Q_K^{-1}$. To show that $Q_i=Q$, we ought to prove that $p-q$ is tangent to $Q$. Now the line through $p,q$ is represented in $\mathbb{R}^3$ by $w:=(p,1)\times (p-q,0)=(J(p-q), \det(p,p-q))$, where $J$ is the counterclockwise rotation by $\frac\pi 2$. It remains to check that $$\langle Q^{-1}w, w\rangle=0\iff \langle (I+tA^{-1})J(p-q), J(p-q)\rangle -(1+t)\det(p,p-q)^2=0.$$ Putting $t=-\frac{\langle Az, z\rangle-1}{|z|^2-1}$ and $z=p+sJp=q+rJAq$ for some $s, r\in \mathbb{R}$, we find $$|z|^2-1=s^2,\quad \langle Az,z\rangle =1+r^2\langle AJAq, JAq\rangle.$$ Since $\det(p,p-q)^2+\langle p,p-q\rangle ^2=|p-q|^2$, the claimed equality becomes $$s^2\langle p,p-q\rangle^2=r^2\|JAq\|_A^2(\|J(p-q)\|_{A^{-1}}^2-\det(p,p-q)^2).$$ The left hand side can be rewrriten as $$\begin{aligned}
\langle sp, p-q\rangle^2&=\langle sJp, J(p-q)\rangle^2=\langle z-p, J(p-q)\rangle^2=\\&\langle z-q, J(p-q)\rangle^2=r^2\langle JAq, J(p-q)\rangle^2=r^2\langle Aq, p-q\rangle^2.
\end{aligned}$$ It thus remains to check that whenever $|p|=1$ and $\langle Aq,q\rangle=1$, one has $$\langle Aq, p-q\rangle^2=\|JAq\|_A^2(\|J(p-q)\|_{A^{-1}}^2-\det(q,p-q)^2).$$ We can write $$\begin{aligned}
\|J(p-q)\|_{A^{-1}}^2-\det(q,p-q)^2&=\|J(p-q)\|_{A^{-1}}^2-\langle J(p-q), q\rangle^2\\&=\|J(p-q)\|_{A^{-1}}^2-\langle Aq, J(p-q)\rangle_{A^{-1}}^2\\&=\langle J(p-q), \nu \rangle_{A^{-1}}^2
\end{aligned}$$ where $\nu=\frac{Jq}{\|Jq\|_{A^{-1}}}$, since $\|Aq\|_{A^{-1}}^2=\langle A^{-1}Aq, Aq\rangle=1$ and $\langle \nu, Aq\rangle_{A^{-1}}=0$.

It remains to check that

$$\|Jq\|_{A^{-1}}\langle JAq, J(p-q)\rangle=\|JAq\|_A\langle A^{-1}Jq, J(p-q)\rangle,$$ or equivalently that $$\|Jq\|_{A^{-1}}JAq=\|JAq\|_A A^{-1}Jq.$$ If $JAq=\lambda A^{-1}Jq$ then $$\lambda =\frac{\|JAq\|_A}{\|A^{-1}Jq\|_A}=\frac{\|JAq\|_A}{\|Jq\|_{A^{-1}}},$$ so it remains to check that $JA$ and $A^{-1}J$, or equivalently $AJA$ and $J$, are proportional. Both are anti-symmetric $2\times 2$ matrices, and so that must be the case.

::: Remark
When $K$ approaches $B$, $Q_i$ and $Q_o$ become polars of one another with respect to $\partial B$.
:::

# Schäffer's dual girth conjecture {#sec:girth}

The Gutkin-Tabachnikov duality of Minkowski billiards has a continuous counterpart, namely Schäffer's dual girth conjecture [@schaeffer], which is a theorem of Álvarez Paiva [@alvarez-paiva]. The setting of Funk geometry is no different, providing another collection of projective invariants enjoying duality.

::: Theorem
[]{#thm:girth label="thm:girth"} Let $L$ be a smooth, strictly convex body in $\mathbb{P}^n$.

1.  Let $M\subset\mathop{\mathrm{int}}(L)$ be a compact submanifold with boundary, and consider $\mathop{\mathrm{Funk}}^\eta_L(M)$. Then its Holmes-Thompson volume, its geodesics and the length of closed geodesics are all independent of $\eta$, and thus constitute projective invariants of $(M,L)$.

2.  If $K\subset\mathop{\mathrm{int}}(L)$ is strictly convex, then $\mathop{\mathrm{Funk}}_L(\partial K)$ and $\mathop{\mathrm{RFunk}}_{K^\vee}(\partial L^\vee)$ have the same Holmes-Thompson volumes and length spectra.
:::

The first claim follows immediately by Proposition [\[prop:funk_exact\]](#prop:funk_exact){reference-type="ref" reference="prop:funk_exact"} and Lemma [\[lem:exact_property\]](#lem:exact_property){reference-type="ref" reference="lem:exact_property"}, as the Funk metric induces on $M$ a projectively-invariant exact co-nomadic Finsler structure.

For the second claim, we follow closely the proof in [@alvarez-paiva]. Write for simplicity $\partial K$ for $\mathop{\mathrm{Funk}}^\eta_L(\partial K)$, and similarly $\partial L^\vee$ for $\mathop{\mathrm{RFunk}}^\theta_{K^\vee}(\partial L^\vee)$.

Define a smooth embedding $\Phi_\eta:S^*\partial K\to \partial K\times\partial L^\vee$ as follows. Let $\pi_x: T_x^*K\to T_x^*\partial K$ be the natural projection. Recall that by Proposition [\[prop:projective_funk\]](#prop:projective_funk){reference-type="ref" reference="prop:projective_funk"}, $S^*_xK=H_\eta(x\times \partial L^\vee)$, where $H_\eta: K\times L^\vee\to T^*K$ is given by eq. [\[eq:identification\]](#eq:identification){reference-type="eqref" reference="eq:identification"}. Now $\pi_x(S^*_xK)=B_x^*\partial K$, and $S^*_x\partial K$ is diffeomorphic to its preimage under $\pi_x$, namely the shadow boundary $Z_x\subset S_x^* K$. Denote $\tau_x=\pi_x^{-1}:S^*_x\partial K\to Z_x$, and define $\tau_\eta:S^*\partial K\to S^*K, (x,\xi')\mapsto (x,\tau_x(\xi'))$. Set $$\Phi_\eta(x,\xi')=H_\eta^{-1}\circ\tau_\eta(x, \xi').$$

Let us describe the image of $\Phi_\eta$. It holds that $(x,\xi)\in \mathop{\mathrm{Im}}(\Phi_\eta)$ if and only if the restricted projection $\pi_x:T_\xi S^*_xK\to T_x^*\partial K$ is not an isomorphism, or equivalently if the natural pairing $T_x\partial K\otimes T_\xi\partial L^\vee\to \mathbb{R}$ is degenerate. The latter pairing is induced from the natural non-degenerate pairing $T_x\mathbb P\otimes T_\xi \mathbb P^\vee\to \mathbb{R}$, which is given by identifying $\xi=x^*$, $(x^\perp)^*=\xi^\perp$, so that $T_x \mathbb{P}=x^*\otimes (x^\perp)^*=\xi\otimes \xi^\perp=T_\xi^*\mathbb{P}^\vee$. In particular, $\mathop{\mathrm{Im}}(\Phi_\eta)$ does not depend on $\eta$.

Turning to the dual manifold, define $\overline{\Phi_\theta}=\overline{H_\theta}^{-1}\circ\tau_\theta:S^*\partial L^\vee\to \partial K\times\partial L^\vee$ in full analogy with $\Phi_\eta$. Observe that the images of the two maps $\Phi_\eta$, $\overline \Phi_\theta$ coincide by their common description as the degeneracy locus of the pairing $T_x\partial K\otimes T_\xi\partial L^\vee\to \mathbb{R}$.

Let $\alpha_1$ be the canonical contact form on $S^*\partial K$, and $\overline\alpha_1$ that of $S^*\partial L^\vee$.

Define $\alpha_\eta =(\Phi_\eta^{-1})^*\alpha_1\in\Omega^1(\mathop{\mathrm{Im}}(\Phi_\eta))$ and $\overline\alpha_\theta =(\overline\Phi_\theta^{-1})^*\alpha_1\in\Omega^1(\mathop{\mathrm{Im}}(\Phi_\eta))$, which coincide with the restriction to $\mathop{\mathrm{Im}}(\Phi_\eta)$ of the corresponding $1$-forms on $\partial K\times\partial L^\vee$ in the proof of Theorem [\[thm:dual_lengths\]](#thm:dual_lengths){reference-type="ref" reference="thm:dual_lengths"}, in particular by that proof $\alpha_\eta-\overline\alpha_\theta$ is an exact form.

We now have

$$\begin{aligned}
\mathop{\mathrm{vol}}^{HT}(\mathop{\mathrm{Funk}}_L(\partial K))&=\int_{S^*\partial K}(d\alpha_1)^{n-2}\wedge\alpha_1=\int_{\mathop{\mathrm{Im}}(\Phi_\eta)}d\alpha_\eta^{n-2}\wedge\alpha_\eta\\&=\int_{\mathop{\mathrm{Im}}(\overline\Phi_\theta)}d\overline\alpha_\theta^{n-2}\wedge\overline\alpha_\theta=\mathop{\mathrm{vol}}^{HT}(\mathop{\mathrm{Funk}}_{K^\vee}(\partial L^\vee)).
\end{aligned}$$ Similarly, the length spectrum of $\mathop{\mathrm{Funk}}^\eta_L(\partial K)$ coincides with the action spectrum of $\alpha_\eta$ on $\mathop{\mathrm{Im}}(\Phi_\eta)$, which is also the action spectrum of $\overline \alpha_\theta$.

We remark that the Holmes-Thompson volumes of $\mathop{\mathrm{Funk}}_L(\partial K)$ and $\mathop{\mathrm{RFunk}}_L(\partial K)$ trivially coincide.

*Proof of Corollary [\[cor:hilbert_plane\]](#cor:hilbert_plane){reference-type="ref" reference="cor:hilbert_plane"}.* This follows at once from Theorem [\[thm:girth\]](#thm:girth){reference-type="ref" reference="thm:girth"}, since the Hilbert length of a curve coincides with its 1-dimensional Funk Holmes-Thompson volume. 0◻.
