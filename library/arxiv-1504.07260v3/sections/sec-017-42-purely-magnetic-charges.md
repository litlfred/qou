---
doc_id: arxiv-1504.07260v3
doc_title: "Fricke S-duality in CHL models"
section_id: sec-017-42-purely-magnetic-charges
section_title: "Purely magnetic charges"
section_number: 4.2
pages: 27-29
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 1.0
doc_brief: "Fricke S-duality in CHL models — We consider four dimensional CHL models with sixteen spacetime supersym- metries obtained from orbifolds of type IIA superstring on K3×T 2 by a ZN symmetry acting"
---
Let us now determine the lattice $\Lambda_m$ of purely magnetic charges. Once again, we will focus on the case $\lambda=1$, postponing the discussion of the general case to section [\[s:genlatticeem\]](#s:genlatticeem){reference-type="ref" reference="s:genlatticeem"}.

By the Dirac quantization condition, the lattice of purely magnetic charges $\Lambda_m$ must be contained in the dual of the lattice [\[electLattsimpl\]](#electLattsimpl){reference-type="eqref" reference="electLattsimpl"}, that is

$$\label{magnincl} \Lambda_m\subseteq \Lambda_e^*=\Gamma_{K3}^g\oplus \langle N u^*, u\rangle \oplus \Gamma_{\tilde S^1}\ ,\qquad \text{for }\lambda=1\ .$$We will now argue that the CHL model contains non-perturbative states whose charges generate the lattice $\Lambda_e^*$, so that this inclusion is actually an equality. It is useful to split the problem into two parts: we consider separately the states that carry magnetic charges within $\langle N u^*, u\rangle \oplus \Gamma_{\tilde S^1}$ and the states that carry charges within $\Gamma_{K3}^g$. The former are related to the four $U(1)$ gauge fields arising from metric and B-field along $S^1\times \tilde S^1$ and are dual to the winding and momentum along $S^1\times \tilde S^1$. The latter are related to the remaining $U(1)^{4+d}$ gauge group, which survives in the decompactification limit where the volume of $S^1\times \tilde S^1$ is large and the theory becomes effectively six-dimensional (heterotic string on $T^4$ or, equivalently, type IIA on K3).

Let us start from the latter. In the original unorbifolded theory, the magnetic charges under these $4+d=24$ $U(1)$ gauge fields generate the lattice $\Gamma_{K3}\cong \Gamma^{4,20}$. After orbifolding by the symmetry $\hat g=(\delta, g)$, only the states invariant under $g\in O(\Gamma_{K3})$ should be included in the spectrum (the shift $\delta$ has no effect on this set of charges). The magnetic charges of these $g$-invariant states generate a lattice $\Gamma_{K3}^g\subset \Lambda_m$, which must therefore be contained as a sublattice of $\Lambda_m$ in the CHL model.

Now, let us consider the four $U(1)$ gauge fields given by the metric and B-field with one leg along $S^1\times \tilde S^1$ and one leg in an uncompactified direction. The associated electric charges correspond to momenta $m,\tilde m$ and windings $w,\tilde w$ along, respectively, $S^1$ and $\tilde S^1$ and generate the lattice $\langle \frac{u}{N}, u^*\rangle \oplus \Gamma_{\tilde S^1}$. Explicitly, the lattice is spanned by vectors $$(\begin{matrix}
m, \tilde m , w , \tilde w
\end{matrix})\in \mathbb{Z}\oplus \mathbb{Z}\oplus \frac{1}{N}\mathbb{Z}\oplus \mathbb{Z}\ ,$$ with standard quadratic form $$\label{quadform} (m,\tilde m,w,\tilde w)^2=2mw+2\tilde m\tilde w\ .$$ Notice that, in our conventions, both the charges and the moduli are normalized as in the original unorbifolded model. Let us denote by $M,\tilde M,W,\tilde W$ the dual magnetic charges. In the unorbifolded theory, one unit of charge $M$, dual to momentum $m$ along $S^1$, is carried by a NS5-brane wrapping $T^4\times \tilde S^1$. The orbifold projection preserves a configuration of $N$ such branes, periodically localized at distance $\delta$ along $S^1$. Therefore, in the CHL model, $M$ is quantized in units of $N\mathbb{Z}$. One unit of charge $\tilde M$, dual to the momentum $\tilde m$ along $\tilde S^1$, is carried by an NS5 brane wrapped along $T^4$ and wrapped once along $S^1/\mathbb{Z}_N$, so that $\tilde M\in \mathbb{Z}$. One unit of charge $W$, dual to the winding $w$ along $S^1$, is carried by a KK monopole with asymptotic circle $S^1/\mathbb{Z}_N$, so that $W\in \mathbb{Z}$. Finally, one unit of charge $\tilde W$ is carried in the unorbifolded theory by a KK monopole with asymptotic circle $\tilde S^1$. This configuration is not affected by the symmetry $\hat g$, so it also appears in the CHL model, where it carries the same charge. The magnetic charges of these non-perturbative states span a lattice $$(\begin{matrix}
M , \tilde M , W , \tilde W
\end{matrix})\in N\mathbb{Z}\oplus \mathbb{Z}\oplus \mathbb{Z}\oplus \mathbb{Z}\ ,\qquad \qquad (M , \tilde M , W , \tilde W)^2=2MW+2\tilde M\tilde W\ ,$$ which is isomorphic to $\langle N u^*, u\rangle \oplus \Gamma_{\tilde S^1}$.

To summarize, we have identified in the CHL model a set of states whose magnetic charges generate a lattice $$\Gamma_{K3}^g\oplus \langle N u^*, u\rangle \oplus \Gamma_{\tilde S^1}\ .$$By [\[magnincl\]](#magnincl){reference-type="eqref" reference="magnincl"}, this is the finest possible lattice compatible with the Dirac quantization condition, so that $\Lambda_m=\Lambda_e^*$ and $$\Lambda_{em}=\Lambda_e\oplus\Lambda_m=\Bigl((\Gamma_{K3}^g)^*\oplus \langle \frac{u}{N}, u^*\rangle \oplus \Gamma_{\tilde S^1}\Bigr)\oplus \Bigl(\Gamma_{K3}^g\oplus \langle N u^*, u\rangle \oplus \Gamma_{\tilde S^1}\Bigr)\ ,\qquad \text{for }\lambda=1\ .$$

For $\lambda>1$, the argument showing that $\Gamma_{K3}^g\subset \Lambda_m$ goes through without essential modifications. However, as explained in appendix [\[s:genlatticeem\]](#s:genlatticeem){reference-type="ref" reference="s:genlatticeem"}, the analysis of the charges carried by NS5-branes and KK monopoles is more subtle in this case. The outcome is that the inclusion $\Lambda_m\subset \Lambda_e^*$ is strict for $\lambda>1$ and, as a consequence, $\Lambda_{em}$ is not simply the direct sum of the purely electric and purely magnetic sublattices.
