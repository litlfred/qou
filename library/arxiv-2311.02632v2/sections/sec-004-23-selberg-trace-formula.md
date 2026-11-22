---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE"
section_id: sec-004-23-selberg-trace-formula
section_title: "Selberg trace formula"
section_number: 2.3
pages: 6-7
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.964
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
Let $X=\Gamma\backslash \uhp$ be a compact Riemann surface of genus $g\geq 2$, where $\Gamma$ is discrete, torsion-free subgroup of $\PSL_2(\R)$. Hence, every non-trivial element of $\Gamma$ is hyperbolic.

The Selberg trace formula establishes a link between the conjugacy classes of $\Gamma$ and and the eigenvalues of the Laplacian. Before delving into the formula itself, we present some requisite notation.

Given a positive parameter $\varepsilon>0$, define $$\mathscr{S}_{\varepsilon}=\left\{r \in \C : | \Im r \mid<\frac{1}{2}+\varepsilon\right\}.$$ Suppose that $h: \mathscr{S}_{\varepsilon} \rightarrow \C$ is a holomorphic even function fulfilling the condition: $$h(r)=O\left(1+|r|^{2}\right)^{-1-\varepsilon} \text { uniformly on } \mathscr{S}_{\varepsilon}.
\label{eq:hdecay}$$ The Fourier transform of $h$ is then given by: $$g(u)=\what{h}(u)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{+\infty} e^{-i r u} h(r)\, d r
, \quad u \in \R.$$ The pair $h, g$ is called an *admissible transform pair*.

A non-trivial element $S$ of $\Gamma$ is primitive if it does not admit a representation in the form $S = R^m$ for some $R\in \Gamma$ and $m\geq 2$. For any hyperbolic element $\gamma\in \Gamma$, there corresponds a unique primitive $\gamma_0$ such that $\gamma=\gamma_0^{m}$ for an integer $m \geq 1$; see [@MR2742784 Lemma 9.2.6]. The quantity $\La(\gamma)$ is defined as $\ell\left(\gamma_{0}\right)$.

We now state Selberg's trace formula [@MR2742784 Theorem 9.5.3]. Let $$r(\la) = \begin{cases}
i \sqrt{\frac{1}{4}-\la} & \text{if } 0 \leq \la < \frac{1}{4} \\
\sqrt{\la - \frac{1}{4}} & \text{if } \la \geq \frac{1}{4}
\end{cases}.$$ Denote by $r_n$ the quantity $r(\la_n)$. Let $\calC(\Gamma)$ be the set of conjugacy classes of hyperbolic elements, and $\{\gamma\}$ be the conjugacy class containing $\gamma \in \Gamma$. With a given admissible transform pair $h,g$, we have $$\label{eq:STF1}
\sum_{n=0}^{\infty} h(r_{n})
=
\frac{\area(X)}{4 \pi} \int_{-\infty}^{+\infty} r h(r) \tanh (\pi r)\, dr+
\frac{1}{\sqrt{2\pi}}\sum_{\{\gamma\} \in \calC(\Gamma)} \frac{\La(\gamma)}{2 \sinh(\ell(\gamma)/2)} g(\ell(\gamma)).$$ All sums and integrals in the formula are absolutely convergent.

Our chosen convention for the Fourier transform is different from the one presented in [@MR2742784]. This difference leads to an altered constant before the sum on the right-hand side of equation [\[eq:STF1\]](#eq:STF1){reference-type="eqref" reference="eq:STF1"}.

In literature, the Selberg trace formula is often phrased in terms of closed geodesics of $X$. In fact, there is a bijection between the oriented closed geodesics of $X = \Gamma\backslash \uhp$ and the conjugacy classes in $\Gamma - \{\id\}$. Under this bijection, the length $\ell(T)$ of a conjugacy class containing $T$ matches the length of the corresponding closed geodesic $\gamma_{T}$. For a detailed description of this relationship, see  [@MR2742784 Section 9.2].
