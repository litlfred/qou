---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-053-173-flat-functions-with-respect-to-a-divisor
section_title: "Flat functions with respect to a divisor"
section_number: 17.3
pages: 94-95
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.831
latex_coverage_ratio: 0.985
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:flatfunctions label="subsection:flatfunctions"}

In the proof of theorem [\[theo:BorelRitt\]](#theo:BorelRitt){reference-type="ref" reference="theo:BorelRitt"}, function $F$ was defined up to a function of the form $\dfrac{P}{\theta_\Lambda}$, where $P$ is a polynomial in $z$ and $z^{-1}$. We shall see that, if $h$ denotes a meromorphic function at $z=0$, then $\dfrac{h}{\theta_\Lambda}$ represents a function with trivial asymptotic expansion, that is, $\dfrac{h}{\theta_\Lambda} \in \text{Ker~}J$ with notations from theorem [\[theo:BorelRitt\]](#theo:BorelRitt){reference-type="ref" reference="theo:BorelRitt"}.

::: theo
[]{#theo:Lambdaplate label="theo:Lambdaplate"} A function $f\in{\mathbb A}_{q}^{\Lambda}$ is *flat*, *i.e.* has trivial expansion, if, and only if, $\theta_\Lambda f$ is meromorphic in a neighborhood of $0 \in {\mathbf C}$.
:::

::: proof
*Proof.* If $f \in {\mathbb A}_{q}^{\Lambda}$ has trivial asymptotic expansion, then, for all $\epsilon > 0$ and $z \in {\mathbf C}^*$ with small enough modulus: $$\label{eqn:plateN}
d_q(z,\Lambda) > \epsilon \Longrightarrow
\left |f(z) \right |< \dfrac{C}{\epsilon}~A^N~\left |q \right |^{N^2/(2\nu)}~\left |z \right |^N$$ for any integer $N \geq 0$. Using relation [\[eqn:minqgevrey\]](#eqn:minqgevrey){reference-type="eqref" reference="eqn:minqgevrey"}, one deduces that $\theta_\Lambda f$ has moderate growth at zero, thus is at worst meromorphic at $z = 0$.

Conversely, note that if $f(z) = \dfrac{h(z)}{\theta_\Lambda(z)}$ with $h(z) = O(z^\mu)$, $\mu\in{\mathbf Z}$, then lemma [\[lemm:thetamin0\]](#lemm:thetamin0){reference-type="ref" reference="lemm:thetamin0"} entails the following relation for all $z$ with small enough modulus: $$d_q(z,\Lambda) > \epsilon > 0 \Longrightarrow
\left |f(z) \right |< 
\dfrac{M}{\epsilon}~{\left |z \right |^\mu}~
\prod_{j=1}^m\left(e\left(\dfrac{z}{\lambda_j}\right)\right)^{-\nu_j}~,$$ where $M$ denotes a constant $>0$. But for any integer $n \in {\mathbf Z}$: $$e(z) = \sum_{k\in{\mathbf Z}}\left |q \right |^{-k(k-1)/2}~\left |z \right |^k>\left |q \right |^{-n(n-1)/2}~\left |z \right |^n~,$$ so that: $$\label{eqn:e-1}
\prod_{j=1}^m\left(e\left(\dfrac{z}{\lambda_j}\right)\right)^{-\nu_j} <
\Vert \Lambda \Vert^{-n}~\left |q \right |^{\nu n(n-1)/2}~\left |z \right |^{-\nu n}~.$$ One thereby gets an estimate of type [\[eqn:plateN\]](#eqn:plateN){reference-type="eqref" reference="eqn:plateN"} for $f$, for a sequence of integral values of $N$, with $N=\mu+\nu n$, $n\to+\infty$ and, as a consequence, for all integers $N \geq 0$: this achieves the proof of the theorem. ◻
:::

::: coro
[]{#coro:f12 label="coro:f12"} Let $f_1, f_2 \in {\mathbb A}_{q}^{\Lambda}$. Assume that $f_1$ et $f_2$ have the same asymptotic expansion. Then $f_1 = f_2$ if, and only if, one of the following conditions is satisfied:

1.  One has $f_1(z_n) = f_2(z_n)$ for some sequence of points $(z_n)$ tending to zero outside of divisor $\Lambda$.

2.  On some spiral $[\lambda_i]$ belonging to divisor $\Lambda$: $$\lim_{z\to\lambda_iq^{n}}(z-\lambda_iq^{n})^{\nu_i}~f_1(z) =
    \lim_{z\to\lambda_iq^{n}}(z-\lambda_iq^{n})^{\nu_i}~f_2(z)$$ as $n \to -\infty$.
:::

::: proof
*Proof.* Immediate. ◻
:::
