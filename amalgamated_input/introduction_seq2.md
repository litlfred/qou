<!-- FILE_START: authors-note.md -->
Every proof in this paper has a corresponding Lean 4 formalisation,
except where external references are cited for large prior results.
**574 of 583 (98.5%) provable claims** (theorems, lemmas,
propositions, corollaries) carry **full Lean proofs** (sorry-free);
the remainder are marked by `sorry` against an explicit bibliographic
reference.  The paper contains
**135 open conjectures**, of which **125 (92.6%) are class-axiomatised in Lean**
following the conditional-class convention so that
downstream results can be stated as fully verified conditional
theorems.  Computations — braid-word reductions, Gröbner–Shirshov
normal forms, linear programs, hyperbolic volumes — are all symbolic
in the substrate parameter $q$ and are attached as witnesses to the
proofs they support wherever appropriate.  The implementations in
Rust and Python, together with the Lean sources, are available at
[https://github.com/litlfred/qou](https://github.com/litlfred/qou).
Large language models were used to assist the drafting and
formalisation process, both because a physical disability prevents
sustained typing and for Lean proof engineering.  Human
adjudication is not complete.

> *I have made this longer than usual only because I have not had
> the leisure to make it shorter.*
> — Blaise Pascal
<!-- FILE_END: authors-note.md -->

