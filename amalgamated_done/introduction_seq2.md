<!-- FILE_START: authors-note.md -->
Every proof in this paper possesses a corresponding Lean 4 formalisation, except where explicitly citing external references for large prior results. **574 of 583 (98.5%) provable claims** (theorems, lemmas, propositions, corollaries) carry **full Lean proofs** (sorry-free); the remainder bear the `sorry` marker against an explicit bibliographic reference. The paper presents **135 open conjectures**, of which **125 (92.6%) are class-axiomatised in Lean** using the conditional-class convention. This allows downstream results to persist as fully verified conditional theorems. All computations—braid-word reductions, Gröbner–Shirshov normal forms, linear programs, hyperbolic volumes—execute symbolically in the substrate parameter $q$ and attach as witnesses to their supporting proofs. The Rust and Python implementations, alongside the Lean sources, reside at [https://github.com/litlfred/qou](https://github.com/litlfred/qou). Large language models assisted the drafting and formalisation process, necessitated by a physical disability preventing sustained typing and deployed for Lean proof engineering. Human adjudication remains incomplete.

> *I have made this longer than usual only because I have not had the leisure to make it shorter.*
> — Blaise Pascal
<!-- FILE_END: authors-note.md -->

