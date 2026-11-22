---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-004-14-main-results
section_title: "Main results"
section_number: 1.4
pages: 4-4
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
toc_source: outline
text_source: latex
latex_prose_ratio: 0.898
latex_coverage_ratio: 1.0
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
As mentioned above, it is easy to define Christoffel deformations of orthogonal polynomial ensembles, but neither the Plancherel nor the $z$-measures are orthogonal polynomial ensembles. As for the characteristic polynomials, an obstacle is that, unlike for orthogonal polynomial ensembles, the number of points might be random or infinite. We still manage to give a meaning to Christoffel deformations of these processes, and also for the process with the Gamma kernel, and we now briefly explain our arguments and state our main results in an informal way.\

On the one hand, we know from Johansson's paper [@johanssonplancherel] that the poissonized Plancherel measure is the limit of the Charlier ensemble, i.e. the orthogonal polynomial ensemble with the Poisson weight. The poissonized Plancherel measure is a determinantal point process described by Bessel functions, the discrete Bessel kernel ([@borodinbessel]). Refining asymptotic results of [@johanssonplancherel], we prove the convergence of the Charlier polynomials towards the Bessel functions, see Lemma [\[lemme1\]](#lemme1){reference-type="ref" reference="lemme1"}, and obtain the following Theorem, see Theorems [\[thm1\]](#thm1){reference-type="ref" reference="thm1"} and [\[thmpalmbessel\]](#thmpalmbessel){reference-type="ref" reference="thmpalmbessel"} for precise statements.

::: Thm
The Christoffel deformation of the Charlier ensemble converges to a determinantal point process described by discrete Wronskians of Bessel functions, the latter being a deformation of the poissonized Plancherel measure. The Palm measures of the poissonized Plancherel measure are described by similar kernels.
:::

On the other hand, the $z$-measures are determinantal point processes described by specific Gauss hypergeometric functions. The analytic continuation argument presented in [@bomarkov] also allows us to describe the deformation of all $z$-measures, a particular case of them being the Meixner ensemble, and we obtain the following Theorem, see Theorems [\[thmzmeas\]](#thmzmeas){reference-type="ref" reference="thmzmeas"} and [\[thmpalmzmeas\]](#thmpalmzmeas){reference-type="ref" reference="thmpalmzmeas"} for precise statements.

::: Thm
The Christoffel deformations of the $z$-measures are determinantal point proccesses governed by a kernel involving discrete Wronskians of Gauss hypergeometric functions. Palm measures of the $z$-measures are governed by similar kernels.
:::

Moreover, a somehow tricky but elementary asymptotic analysis, similar to the one performed in [@bogamma], leads to a deformation of the process with the Gamma kernel, see Theorem [\[thmgamma\]](#thmgamma){reference-type="ref" reference="thmgamma"}.

::: Thm
The one-point deformations of the non-degenerate $z$-measures converge to a determinantal point process described by the Gamma function and its first derivative, which might be considered as a deformation of the process with the Gamma kernel.
:::

We strongly believe that the approximation procedure we use in the last two Theorems could also be applied to the $zw$-measures, since the same argument of analytic continuation from an orthogonal polynomial ensemble holds, see [@bo-zw].
