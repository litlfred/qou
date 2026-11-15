---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-015-why-floquet-edges-are-richer-than-standard-rmt-e
section_title: "Why Floquet edges are richer than standard RMT edges"
section_number: null
pages: 16-18
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.988
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
[]{#sec:2d-vs-1d label="sec:2d-vs-1d"}

The appearance of the Pearcey kernel---and the broader catastrophe hierarchy---in Floquet systems is not accidental. It reflects a fundamental difference between the geometry of edges in periodically driven systems and in standard random matrix theory [@Forrester2010; @DeanLeDoussal2019].

#### Standard RMT: edges in one dimension.

In a random matrix ensemble with one-dimensional eigenvalue support [@Forrester2010]---Hermitian ensembles on $\mathbb R$, or unitary ensembles on the circle---the eigenvalue density $\rho(x)$ is a function of a single spectral variable $x$. The support of $\rho$ is generically a union of intervals, and an "edge" is an endpoint of one such interval. At a generic endpoint the density vanishes as $\rho(x)\sim (x-x_{\rm edge})^{1/2}$---a square-root onset. In the language of stationary phase, this corresponds to the coalescence of two saddle points in the integral representation of the kernel, which is a *fold* singularity. The universal edge kernel is therefore the Airy kernel, and its fluctuation statistics are governed by the Tracy--Widom distribution [@TracyWidom1994; @Forrester2010].

In one dimension, a fold is the *only* generic singularity. To produce a cusp---where three saddle points coalesce simultaneously---one must fine-tune an additional external parameter (such as adding a deterministic source to the random matrix [@BleherKuijlaars2007]). In the absence of such tuning, cusps and higher singularities have codimension $\ge 2$ in the one-dimensional spectral variable and do not occur stably.

#### Floquet systems: edges in two dimensions.

In a periodically driven system, the one-body physics lives in the Sambe (Floquet--Bloch) space [@Sambe1973], which is intrinsically *two-dimensional*: the relevant coordinates are a Floquet angle $\theta\in[0,2\pi)$ (conjugate to the sideband index) and a quasienergy or frequency $\omega$. The outgoing one-body spectral function $\sigma(\theta,\omega)$---or, equivalently, the sideband-resolved occupation $C_{nn}$ as a function of sideband index and central energy---is a function on this two-dimensional cylinder. The "filled region" visible to the measurement is the set of $(\theta,\omega)$ points where $\sigma>0$, and the *spectral edge* is the boundary of this region.

This boundary is generically a *curve* in the $(\theta,\omega)$ plane. The singularities of a curve in two dimensions are classified by the $A_k$ catastrophe hierarchy [@ArnoldSingularities], and the key point is that the classification depends on how many control parameters are available:

-   *Fold* ($A_2$, codimension 1): a smooth turning point of the boundary curve. This is the generic edge encountered by scanning a single parameter (e.g., the analysis frequency $\omega_0$ at fixed drive). The local kernel is the Airy kernel.

-   *Cusp* ($A_3$, codimension 2): the boundary curve develops a cusp, where the tangent direction reverses. In two dimensions, the cusp is the canonical codimension-two singularity of smooth curves: extra control parameters make it *accessible*, though its location in $(\theta,\omega)$ shifts under perturbation. In a one-parameter family of edges (e.g., as a second drive amplitude $A_2$ is swept), a cusp is the natural singularity to look for at an isolated critical value of $A_2$, unfolding into two folds on either side. The local kernel at such a cusp is expected to be the Pearcey kernel; the transition from Pearcey to Airy at a cusp point has been rigorously analyzed in the context of random tiling models by Duse, Johansson, and Metcalfe [@DuseJohanssonMetcalfe2015].

-   *Swallowtail* ($A_4$, codimension 3): requires three control parameters, hence the natural edge singularity of a three-tone drive or a two-tone drive with one additional tunable coupling.

#### The physical mechanism.

The connection to the scattering picture is suggestive. In the Sambe (extended Hilbert space) formulation [@Sambe1973], the Floquet scattering amplitude $S_{nm}(E)$ can be expressed as a matrix element of a resolvent in the space of sideband indices. Heuristically, this admits an oscillatory-integral representation with a phase $\Phi(\xi;\theta,\omega)$ that depends on two external parameters ($\theta$ = Floquet angle, $\omega$ = quasienergy). An edge occurs when stationary points of $\Phi$ in $\xi$ coalesce---a caustic in the sense of diffraction catastrophes [@BerryUpstill1980]. The number of coalescing saddles---and hence the catastrophe type---is determined by the geometry of $\Phi$ in the two-dimensional $(\theta,\omega)$ plane: $$\partial_\xi \Phi = 0, \quad \partial_{\xi\xi} \Phi = 0 \quad\text{(fold)};
  \qquad
  \partial_\xi \Phi = 0, \quad \partial_{\xi\xi} \Phi = 0, \quad \partial_{\xi\xi\xi} \Phi = 0 \quad\text{(cusp)}.
  \label{eq:fold-cusp-conditions}$$ At a fold, the normal form of the phase is cubic ($\zeta^3/3 - u\zeta$) and the resulting integral is the Airy function. At a cusp, the normal form is quartic ($\zeta^4/4 - \gamma\zeta^2/2 - u\zeta$) and the integral is the Pearcey function.

#### Summary: dimensionality dictates the universal catalogue.

The enrichment can be stated concisely. For a single spectral variable with no external tuning parameters, the only generic edge singularity is the fold, and the only generic edge kernel is Airy. Cusp (Pearcey) universality is well established in RMT---it arises in external-source models [@BrezinHikami1998; @BleherKuijlaars2007] and has been proved in considerable generality [@TracyWidomPearcey; @AdlerFerrariVanMoerbeke2010]---but requires tuning an additional parameter to bring two edges together. A Floquet system provides such a parameter naturally: the two-dimensional Sambe space means that the boundary of the filled region is a curve, and its singularities can include cusps (codimension two) in addition to folds (codimension one). Extra control parameters---such as a second drive tone---make the cusp accessible without artificial tuning, with the Pearcey kernel emerging at the coalescence point [@DuseJohanssonMetcalfe2015]. This is the structural reason why periodically driven systems are a natural physical setting in which the catastrophe-kernel family beyond Airy may be realized.
