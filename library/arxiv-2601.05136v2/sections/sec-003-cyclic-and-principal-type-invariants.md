---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-003-cyclic-and-principal-type-invariants
section_title: "Cyclic and principal type invariants"
section_number: null
pages: 4-5
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
text_source: latex
latex_prose_ratio: 0.87
latex_coverage_ratio: 0.967
doc_brief: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant — Previous work of the author and N."
---
[]{#sec:negative type label="sec:negative type"}

There appear to be two inequivalent (but perhaps both natural) branches of complex Chern-Simons theory. Above we described invariants [@Baseilhac2004; @Bonahon2021; @Kashaev2005; @McPhailSnyderVolume] that

-   are defined as a sum over a finite state space,

-   are conjectured to exponentially grow as $N\to \infty$, and

-   are well-defined for any (or any geometrically non-degenerate) hyperbolic structure.

In contrast, invariants [@zbMATH06324352; @arXiv:1305.4291; @arXiv:2508.05120]

-   are defined using integrals over a noncompact, continuous state space,

-   are conjectured to *decay* as $N\to \infty$, but

-   are only defined when the hyperbolic structure satisfies a positivity condition so that the integrals converge.

These two branches are related to different quantizations of the moduli space of $\slg$ local systems. Principal type invariants are related to the representations of quantum cluster varieties defined by @zbMATH01607168 [@zbMATH01607168] and @zbMATH05530519 [@zbMATH05530519]. These are infinite-dimensional representations analogous to the principal series representations of $\operatorname{SL}_{2}$. The cyclic quantizations studied in detail by @arXiv:2501.02316 [@arXiv:2501.02316] are finite-dimensional and analogous to highest-weight modules. Cyclic type invariants are more directly related to the Kashaev invariant and the original Volume Conjecture. It is typically easier to prove volume conjectures for principal type invariants: they are *defined* in terms of integrals, so [\[step 1\]](#step 1){reference-type="ref" reference="step 1"} holds automatically, subject to the positivity condition.

Asymptotic growth of cyclic type invariants has been established only for knots with up to $7$ crossings [@zbMATH06684922; @Ohtsuki2017; @Ohtsuki2018] and for twist knots [@Chen2023II]. For principal type invariants much more is known: the invariant of @arXiv:2508.05120 satisfies the conjecture for every hyperbolic manifold with totally geodesic boundary, and the Andersen-Kashaev Teichmüller TQFT satisfies it for twist knots [@zbMATH07761477] and many other manifolds [@arXiv:2410.10776; @arXiv:2512.17437; @arXiv:2512.23198]. We hope that our result leads to a proof of asymptotic growth of $\qinv{}$ using similar techniques.

In addition, our work may lead to a better understanding of the relationship between cyclic and principal invariants. @arXiv:1305.4291 showed that their principal type TQFT can be defined using integrals over compact state spaces. This form of the partition function formally resembles the sum of state integrals [\[eq:state integral sum intro\]](#eq:state integral sum intro){reference-type="eqref" reference="eq:state integral sum intro"} after a Wick rotation and changing the overall sign of the action. Their reformulation is accomplished via a Weil-Gel'fand-Zak transform taking values in a space of quasi-periodic functions. Similar quasi-periodic functions are used in the definition of $\qinv{}$ [@McPhailSnyderVolume] and this may lead to a more precise relationship between the two constructions.

## Acknowledgements

I would like to thank Francis Bonahon, Effie Kalfagianni, Lillian Pierce, and Ka Ho Wong for helpful conversations.
