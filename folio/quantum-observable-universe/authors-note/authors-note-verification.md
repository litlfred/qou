Every proof in this paper is accompanied by a formal, machine-verified counterpart in Lean 4, except where a large prior result is cited from the literature; the extent of that verification, and the conditional form in which open conjectures are carried, are recorded in the [formalisation notes](#app:formalisation-notes). The Lean library is rendered to HTML, with every declaration and its source, by the Lean documentation pipeline of [folio-assistant-sci](https://github.com/litlfred/folio-assistant-sci), and is published with the paper's site under the route [`lean/`](https://litlfred.github.io/qou/lean/). All computations (braid-word reductions, Gröbner–Shirshov normal forms, linear and semidefinite programs, hyperbolic volumes) execute symbolically in the substrate parameter $q$, or in arbitrary-precision arithmetic, and attach as witnesses to the statements they support.

The source of this paper, the formal proofs, and the Rust and Python implementations reside at [https://github.com/litlfred/qou](https://github.com/litlfred/qou), released under the Creative Commons Attribution 4.0 International License.

Large language models assisted the drafting and the formal verification, necessitated by a physical disability preventing sustained typing. Human adjudication remains incomplete.

> *Je n'ai fait celle-ci plus longue que parce que je n'ai pas eu le loisir de la faire plus courte.*
> — Blaise Pascal, *Lettres provinciales* (XVI, 1657)
