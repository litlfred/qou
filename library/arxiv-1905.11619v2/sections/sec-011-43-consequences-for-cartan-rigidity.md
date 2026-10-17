---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-011-43-consequences-for-cartan-rigidity
section_title: "Consequences for Cartan rigidity"
section_number: 4.3
pages: 16-17
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.746
latex_coverage_ratio: 0.972
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an analysis of quantum Markov semi-groups."
---
We gather some Cartan rigidity properties; these were already obtained in an unpublished manuscript by Avsec [@Avsec], where they were proved for any $-1 < q < 1$. Our cohomological properties in the next section are new however. Recall that we assumed that $\dim(H_{\mathbb{R}}) < \infty$.

We recall that a von Neumann algebra $M$ has the W$^\ast$CMAP (weak-$\ast$ complete metric approximation property) if there exists a net $\Phi_i: M \rightarrow M$ of completely contractive normal finite rank maps such that for every $x \in M$ we have $\Phi_i(x) \rightarrow x$ $\sigma$-weakly and $\limsup_i \Vert \Phi_i: M \rightarrow M \Vert_{cb} = 1$.

::: thm
For any $H_{\mathbb{R}}$ and $\vert q \vert \leqslant  \dim(H)^{-\frac{1}{2}}$ the $q$-Gaussian algebra $\Gamma_q(H_{\mathbb{R}})$ is strongly solid.
:::

::: proof
*Proof.* By [@Avsec] we see that $\Gamma_q(H_{\mathbb{R}})$ has the W$^*$CMAP. In Corollary [\[Cor=Derivation\]](#Cor=Derivation){reference-type="ref" reference="Cor=Derivation"}, we have constructed a closable derivation $\partial(=\partial_1): \mathcal{A}_q \rightarrow L^2(\Gamma_q(H_{\mathbb{R}}))_{\nabla}$. This derivation is real by [@CaspersGradient Lemma 3.10] and proper as $\partial^\ast \overline{\partial} = \Delta$ and $\Delta$ has compact resolvent. Further, by Theorem [\[Thm=QGaussianSp\]](#Thm=QGaussianSp){reference-type="ref" reference="Thm=QGaussianSp"} we find that $(\Phi_t)_{t \geq 0}$ is immediately gradient-$\mathcal{S}_2$ and gradient $\mathcal{S}_2$ if $\vert q\vert <  \dim(H)^{-\frac{1}{2}}$.

In case $\vert q \vert <  \dim(H)^{-\frac{1}{2}}$ from Theorem [\[Thm=IGHS-GC\]](#Thm=IGHS-GC){reference-type="ref" reference="Thm=IGHS-GC"} we see that the left and right $\mathcal{A}_q$ actions on $L^2(\Gamma_q(H_{\mathbb{R}}))_{\nabla}$ extend to normal $\Gamma_q(H_{\mathbb{R}})$ actions. Moreover, the thus-obtained $\Gamma_q(H_{\mathbb{R}})$-$\Gamma_q(H_{\mathbb{R}})$ bimodule $L^2(\Gamma_q(H_{\mathbb{R}}))_{\nabla}$ is weakly contained in the coarse bimodule of $\Gamma_q(H_{\mathbb{R}})$. Then [@OzawaPopaAJM Corollary B] implies the result except that we need a reformulation of [@OzawaPopaAJM Corollary B] in terms of derivations instead of cocycles; that version can be found in [@CaspersGradient Appendix A] (even for stable normalizers).

For arbitrary $\vert q \vert \leq  \dim(H)^{-\frac{1}{2}}$ the proof follows in the same way using [@CaspersGradient Proposition 4.3] instead of Theorem [\[Thm=IGHS-GC\]](#Thm=IGHS-GC){reference-type="ref" reference="Thm=IGHS-GC"}; one only needs to prove that the left and right $\mathcal{A}_q$ actions on $L^2(\Gamma_q(H_{\mathbb{R}}))_{\nabla}$ extend to normal $\Gamma_q(H_{\mathbb{R}})$ actions. We do this in Proposition [\[Prop=NormalExtension\]](#Prop=NormalExtension){reference-type="ref" reference="Prop=NormalExtension"}. ◻
:::

::: prop
[]{#Prop=NormalExtension label="Prop=NormalExtension"} The left and right $\mathcal{A}_q$-actions on $L^2(\Gamma_q(H_{\mathbb{R}}))_{\nabla}$ extend to commuting normal $\Gamma_q$-actions.
:::

::: proof
*Proof.* The proof follows [@CaspersGradient Proposition 3.8]. We prove it for the left action, the proof for the right action is similar. We must show that the action is weakly continuous on the unit ball. Take elementary Wick operators $a = W_q(\bm{\xi}), b = W_q(\bm{\eta}), c = W_q(\bm{\mu}), d = W_q(\bm{\nu}) \in \mathcal{A}_q$. For $\bm{\xi} = \xi_1 \otimes \ldots \otimes \xi_n$ we refer to $n$ as the length of $W_q(\bm{\xi})$. Consider, $$\label{Eqn=Inn}
\langle x \cdot a \otimes_\nabla b\Omega, c \otimes_\nabla d\Omega \rangle =
- \frac{1}{2} \langle d^\ast (\Delta(c^\ast x a) + c^\ast \Delta(x) a - \Delta(c^\ast x) a  - c^\ast \Delta(xa)) b\Omega,  \Omega \rangle$$ Let $x,a,b,c,d$ have length $X, A, B, C, D$ respectively. The operator $\Delta$ preserves the length of a Wick word. Then using Lemma [\[Lem=WickProduct\]](#Lem=WickProduct){reference-type="ref" reference="Lem=WickProduct"} we see that each of the expressions $d^\ast \Delta(c^\ast x a) b$, $d^\ast c^\ast \Delta( x a) b$, $d^\ast \Delta( c^\ast x  ) a b$ and $d^\ast c^\ast \Delta( x )a b$ is a linear combination of Wick words of length at least $X - A - B - C - D$. Therefore if $X > A + B + C+D$ then [\[Eqn=Inn\]](#Eqn=Inn){reference-type="eqref" reference="Eqn=Inn"} is 0. We therefore see that the map $$\label{Eqn=Inn2}
\mathcal{A}_q \rightarrow \mathbb{C}: x \mapsto \langle x \cdot a \otimes_\nabla b\Omega, c \otimes_\nabla d\Omega \rangle,$$ factors through the normal projection $P_{\leq X}: \Gamma_q(H_{\mathbb{R}}) \rightarrow \Gamma_q(H_{\mathbb{R}})$ onto Wick words of length $\leq X$. The range of this projection is finite dimensional and contained in $\mathcal{A}_q$. Hence [\[Eqn=Inn2\]](#Eqn=Inn2){reference-type="eqref" reference="Eqn=Inn2"} extends to a normal map $\Gamma_q(H_{\mathbb{R}}) \rightarrow \mathbb{C}$.

Now let $x \in  \Gamma_q(H_{\mathbb{R}})$ with $\Vert x \Vert \leq 1$ and let $x_j \in \Gamma_q(H_{\mathbb{R}})$ with $\Vert x_j \Vert \leq 1$ be a net converging to $x$ weakly (Kaplansky's density theorem). Let $\xi, \eta \in  L^2(\Gamma_q(H_{\mathbb{R}}))_{\nabla}$ and let $\xi_0, \eta_0$ be in the linear span of vectors of the form $a \otimes b \Omega$ with $a, b \in \mathcal{A}_q$ as in the previous paragraph with $\Vert \xi - \xi_0 \Vert, \Vert \eta - \eta_0 \Vert < \varepsilon$. Let $j_0$ be such that for $j > j_0$ we have $\vert \langle (x - x_j) \xi_0, \eta_0 \rangle \vert < \varepsilon$. Then, $$\begin{split}
\vert \langle (x - x_j) \xi, \eta \rangle \vert \leq & \vert \langle (x - x_j) \xi_0, \eta_0 \rangle \vert  + \Vert x - x_j \Vert \Vert \xi - \xi_0 \Vert \Vert \eta_0 \Vert + \Vert x - x_j \Vert \Vert \xi  \Vert \Vert \eta - \eta_0 \Vert\\
 \leq & \varepsilon + 2 \varepsilon       \Vert \eta_0 \Vert + 2 \varepsilon    \Vert \xi  \Vert.
\end{split}$$ ◻
:::
