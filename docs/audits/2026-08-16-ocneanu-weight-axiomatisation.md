# Axiomatising the Ocneanu-weight input

**Status: in progress.** Owner-directed follow-up to
[#5217](https://github.com/litlfred/qou/pull/5217), which proved
`y_λ = 0 ⟺ ℓ(λ) > r` sorry-free for all `n` and `r`, resting on one external
input — Wenzl (1988), that the Ocneanu weights **are** the principal
specialisations — carried as a `-- Ref:` comment and nothing more.

The owner has directed that the input be **axiomatised**: made machine-legible
and machine-checkable rather than a comment a reader can miss.

**This is a truthfulness change, not a strengthening.** Nothing becomes more
proved. Statements that were unconditional stay unconditional; the bridge from
the *formula* to the *actual Ocneanu weight* becomes an explicit hypothesis in
the signature, and every statement about the actual weight is thereby
downgraded in presentation from "proved" to "proved conditional on Wenzl 1988"
— which is what it always was.

To follow: the class design, the conditional/unconditional boundary, the
`#print axioms` table, and a scoping of what an *unconditional* route would
cost.
