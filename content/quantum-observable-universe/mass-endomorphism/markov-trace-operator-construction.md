The Jones–Wenzl Markov trace $\tau_M : \mathbf{B}_\infty \to \mathbb{R}$
on the inductive limit of braid groups is uniquely characterised by the
M1–M4 axioms (Jones 1985 / Wenzl 1988). Its realization as a single
operator on the von Neumann inductive-limit hyperfinite $\mathrm{II}_1$
factor proceeds in five stages: a per-$n$ Hilbert representation, an
inductive embedding $\iota_n : V_n \hookrightarrow V_{n+1}$, the inductive
limit $V_\infty = \varinjlim V_n$, the trace state on $\bigcup_n H_n$,
and the bicommutant closure $\mathcal{M} := (\bigcup_n H_n)''$, on which
$\tau_M$ is the unique faithful normal trace up to scaling.

The Lean class scaffold (`HnHilbertRep n q`, `HnInductiveEmbedding n q`,
`MarkovTraceVNFactor q`) encodes the per-$n$ Hilbert representation, the
inductive embedding, and the GNS / bicommutant von Neumann factor that
hosts $\tau_M$. Downstream Lean files import these classes as hypotheses;
the operator-algebra steps — the GNS state and the bicommutant closure
of the inductive-limit algebra — supply the per-$n$ instances.
