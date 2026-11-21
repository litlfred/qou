---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents"
section_id: sec-002-21-equivariant-quantization
section_title: "Equivariant quantization"
section_number: 2.1
pages: 8-9
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.979
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
\label{DI.sec:equiv}

There are several things to notice about \eqref{DI.Hks}. Perhaps the most salient is that, unlike in the case of Chern-Simons theory with compact gauge group \cite{DIWit-Jones, DIaxelrod-witten}, the Hilbert space is infinite-dimensional. This is no surprise, since it comes from quantizing a noncompact phase space. One may also recognize the $\BC^{2k}$ factor as being related to the standard Hilbert space for $SU(2)$ theory at (bare) level $k$. Indeed, if we ignore $\mu$ and consider functions $f(m)$ of an integer $m\in \BZ/(2k\BZ)$, such that $f(m)=f(-m)$ as in \eqref{DI.Weyl}, we find exactly $|k|+1$ independent values $f(0),f(1),...,f(|k|)$ that determine a state in the finite-dimensional Hilbert space of $SU(2)$ Chern-Simons.


What is less obvious, in particular for general $\Sigma$, is that the infinite-dimensional Hilbert space of complex Chern-Simons theory admits an additional $U(1)_t$ symmetry, introduced in \cite{DIGukovPei}. The graded components of $\CalH[\Sigma]$ (\DIie\ the subspaces of fixed $U(1)_t$ charge) turn out to be finite-dimensional, and in particular the subspace of zero charge is just the familiar $SU(2)$ Hilbert space.

The extra $U(1)_t$ symmetry comes from viewing $\CalP[\CalM]\simeq \CalM_{\rm Hit}(SU(2),\Sigma)$ as the Hitchin moduli space. There is a canonical $U(1)_t$ metric isometry of the Hitchin moduli space that rotates the $\cp^1$ of complex structures about an axis. In particular, it rotates $\omega_J=\text{Im}(\Omega)$ and $\omega_K$ into each other. This is an isometry of our quantization problem at least when $s=0$, since it preserves $\omega_{k,s=0}$, and leads to the desired symmetry of $\CalH[\Sigma]_{k,0}$.
(Since the Hilbert space, abstractly, does not depend on $s$, one might then hope to endow even spaces at $s\neq 0$ with the symmetry.)

In the case $\Sigma=T^2$, it is easy to describe the $U(1)_t$ symmetry: when we view $\CalP[T^2]\simeq T^*(S^1\times S^1)/\BZ_2\approx T^*\CalM_{\rm flat}(SU(2),T^2)$ as the cotangent bundle of the space of flat $SU(2)$ connections, $U(1)_t$ simply rotates the cotangent fibers. The $U(1)_t$-invariant subspace of $\CalH[T^2]_{k,s=0}$ simply consists of the functions $f(\mu,m)$ that are independent of $\mu$ --- \DIie\ the $SU(2)$ Hilbert space we found above. The full $U(1)_t$ action is trickier to describe in the polarization we are using. Roughly, one observes that at $s=0$ and $b=1$ the variables $x,\bar x$ can be written as

\DIbe x = z \eta^{-m}\,,\quad \bar x = z\eta^{m}\,, \DIee

where $z = \exp(\pi \mu/k)$ and $\eta=\exp(i\pi/k)$. Then, on functions of $f(z,m)$ that are analytic in $z$, the $U(1)_t$ symmetry just acts as rotations $z\to e^{i\theta}z$. The subspaces of fixed $U(1)_t$ weight contain monomials in $z$. After imposing Weyl invariance, the graded dimension of the Hilbert space becomes

\DIbe \begin{array}{ll} \text{dim}_{U(1)_t} \CalH[T^2]_{k,s=0} &:= \sum_{w\in \BZ} t^w \text{dim}\CalH[T^2]_{k,s=0}^{\text{weight $w$}} = |k|+1 + 2|k|(t+t^2+t^3+...) \\[.1cm]
&= \ds |k|+1 + \frac{2|k|t}{1-t}\,. \end{array} \label{DI.grdim} \DIee
