The Jones–Wenzl Markov trace $\tau_M : \mathbf{B}_\infty \to \mathbb{R}$
on the inductive limit of braid groups is uniquely characterised by the
M1–M4 axioms (Jones 1985 / Wenzl 1988). Its existence as a single
operator on the von Neumann inductive limit hyperfinite $\mathrm{II}_1$
factor is the substantive content of item 4 of the post-PR-#665 open
R&D inventory; the per-$n$ Hilbert representation + inductive
embedding + GNS / bicommutant von Neumann factor scaffolding (Lean
classes `HnHilbertRep n q`, `HnInductiveEmbedding n q`,
`MarkovTraceVNFactor q`) follows the explicit-residual pattern.

**Primary content moved to audits.** See
[`docs/audits/2026-06-03-wip-scaffolding-markov-trace-operator-construction.md`](../../../docs/audits/2026-06-03-wip-scaffolding-markov-trace-operator-construction.md)
for the full construction outline (per-$n$ Hilbert space $\to$ inductive
embedding $\to$ inductive limit $\to$ trace state $\to$ bicommutant closure) and
per-$n$ discharge status.

The Lean class scaffolding stays in place at
[`markov-trace-operator-construction.lean`](markov-trace-operator-construction.lean) —
downstream Lean files import the classes as hypotheses; the
operator-algebra steps (GNS state, bicommutant closure of the
inductive-limit algebra) remain the substantive open R&D.

This block is retained in the paper as an interpretive
forward-reference; it makes no logical claim.
