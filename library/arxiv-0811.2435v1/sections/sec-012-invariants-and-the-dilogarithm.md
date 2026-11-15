---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-012-invariants-and-the-dilogarithm
section_title: "Invariants () and the dilogarithm"
section_number: null
pages: 32-33
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
Let $\Gamma$ be a free abelian group of finite rank $n$ as before, endowed with a skew-symmetric integer-valued bilinear form $\langle \bullet, \bullet\rangle : \Gamma \times \Gamma\to \Z$. Recall the Lie algebra $\g_{\Gamma}=\g_{\Gamma,\langle \bullet,\bullet \rangle}=\oplus_{\gamma\in \Gamma}\Q\cdot e_{\gamma}$ with the Lie bracket $$[e_{\gamma_1},e_{\gamma_2}]=(-1)^{\langle \gamma_1, \gamma_2\rangle}\langle \gamma_1, \gamma_2\rangle e_{\gamma_1+\gamma_2}\,\,.$$ Let us introduce a commutative associative product on $\g_{\Gamma}$ by the formula $$e_{\gamma_1}e_{\gamma_2}=(-1)^{\langle \gamma_1, \gamma_2\rangle}e_{\gamma_1+\gamma_2}\,\,.$$ We denote by ${\mathbb T}_{\Gamma}:={\mathbb T}_{\Gamma,\langle \bullet, \bullet\rangle}$ the spectrum of this commutative algebra. It is easy to see that ${\mathbb T}_{\Gamma}$ is a torsor over the algebraic torus $\op{Hom}(\Gamma, {\bf G}_m)$. Moreover ${\mathbb T}_{\Gamma}$ is an algebraic Poisson manifold with the Poisson bracket $$\{a,b\}:=[a,b]\,.$$ The Poisson structure on ${\mathbb T}_{\Gamma}$ is invariant with respect to the action of $\op{Hom}(\Gamma, {\bf G}_m)$.

We can specify the results of the previous sections to the Lie algebra $\g_{\Gamma}$. For stability data $(Z,a)$ we can write uniquely (by the Möbius inversion formula) $$a(\gamma)=-\sum_{n\geqslant 1, {1\over{n}}\gamma\in \Gamma\setminus \{0\}}{\Omega(\gamma/n)\over{n^2}}e_{\gamma}\,\,,$$ where $\Omega:\Gamma\setminus \{0\}\to \Q$ is a function. Then we have $$\exp\left(\sum_{n\geqslant 1}a(n\gamma)\right)=\exp\left(-\sum_{n\geqslant 1} \Omega(n\gamma)\sum_{k\geqslant 1}{e_{kn\gamma}\over{k^2}}\right):=
\exp\left(-\sum_{n\geqslant 1}\Omega(n\gamma)\op{Li}_2(e_{n\gamma})\right),$$ where $\op{Li}_2(t)=\sum_{k\geqslant 1}{t^k\over{k^2}}$ is the dilogarithm function.

The Lie algebra $\g_{\Gamma}$ acts on ${\mathbb T}_{\Gamma}$ by Hamiltonian vector fields. Let us denote by $T_{\gamma}$ the formal Poisson automorphism $$T_{\gamma}=\exp(\{-\op{Li}_2(e_{\gamma}),\bullet\})\,\,,\,\,\, T_\gamma(e_\mu)=(1-e_\gamma)^{\langle \gamma,\mu \rangle} e_\mu$$ considered as an automorphism of algebra of functions.

More precisely for any strict convex cone $C\subset \Gamma_{\R}$ containing $\gamma$ the element $T_{\gamma}$ acts on the formal scheme $Spf(\prod_{\mu\in \Gamma \cap C}\Q e_{\mu})$. Moreover $T_{\gamma}$ is the Taylor expansion of a birational automorphism of ${\mathbb T}_{\Gamma}$.

Finally, in the case when $\Gamma$ comes from a $3d$ Calabi-Yau category the numbers $\Omega(\gamma)$ are (conjecturally) integers for $(\gamma,Z)\in {\cal X}_2$ in notation of Section 2.4. They provide generalization of DT-invariants (BPS degeneracies in physics language).
