---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-017-43-d-modules-on-stacks
section_title: "D-modules on stacks"
section_number: 4.3
pages: 29-29
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 1.0
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
Throughout what follows, by a stack, we will always mean a quasi-compact stack over $\mathbb C$ with affine diagonal. By a representable morphism, we will always mean a quasi-compact schematic morphism.

For schemes $X$, the category ${\mathcal D}(X)$ satisfies smooth descent with respect to $!$-pullbacks. Thus for a stack $X$, one may define the category ${\mathcal D}(X)$ as a limit over smooth covers.

More explicitly given a smooth cover $U\to X$ by a scheme, with induced augmented Cech simplicial scheme $U_*\to X$, one obtains a cosimplicial category ${\mathcal D}(U_*)$, with maps given by $!$-pullbacks, such that its totalization satisfies $${\mathcal D}(X) \simeq\lim {\mathcal D}(U_*)$$ (See [@BD Section 7.5] for a discussion in the language of derived categories.) Alternatively, one may calculate ${\mathcal D}(X)$ as the limit over $*$-pullbacks (over the smooth face maps) in the above Cech simplicial scheme.

For an arbitrary morphism $f:X\to Y$ of stacks, composition identities provide a continuous pullback functor $f^!$ which can be calculated locally with respect to smooth covers. In particular, there is an object $\omega_X\in {\mathcal D}(X)$ whose $!$-pullback along any smooth cover $U\to X$ is the corresponding object $\omega_U\in {\mathcal D}(U)$.

For a representable morphism $f:X\to Y$, base change provides a continuous functor $f_*$ which can be calculated locally with respect to smooth covers.

For a smooth representable morphism $f:X\to Y$, there is a functor $f^*$ along with an adjunction $(f^*, f_*)$ and canonical isomorphism $f^*\simeq f^![-2(\dim X - \dim Y)].$

One can extend the definition of $f_*$ to arbitrary morphisms $f:X\to Y$, but it is no longer continuous. In particular, the de Rham cohomology functor $\Gamma_{dR}$ is not continuous in general. It is however representable by an object $\mathbb C_X\in {\mathcal D}(X)$ whose $*$-pullback along any smooth cover $U\to X$ is the corresponding object $\mathbb C_U\in {\mathcal D}(U)$.
