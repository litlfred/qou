---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-014-6-schäffers-dual-girth-conjecture
section_title: "Schäffer's dual girth conjecture"
section_number: 6
pages: 21-22
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.95
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
---
[]{#sec:girth label="sec:girth"}

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
