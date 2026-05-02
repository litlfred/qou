**Locality dropped.** In the algebraic-geometry refactor of the
QOU mass framework, the categorical mass endomorphism

$$
  \Phi_n
  \;\colon\;
  \mathbf{1}
  \longrightarrow
  A^{\otimes n}
$$

([mass endomorphism conjecture](#conj:mass-endomorphism))
is treated strictly as a **global section** over the rigid braided
monoidal category $\mathbf{C}$. There is no local trivialisation
hypothesis: $\Phi_n$ is not assumed to factor through any patchwise
construction, and there is no screening mechanism that could absorb
ribbon-operator action over a bounded neighbourhood.

**Why this matters.** Without locality, any non-trivial action of the
full-twist ribbon operator $\theta_n \in Z(H_n(q))$ on a candidate
state cannot be hidden. It propagates unbounded topological flux
through $\mathbf{C}$, contradicting the finite-mass requirement. The
finite-mass principle therefore *forces* topological neutrality of
the saturated state — this is the framework input for
[categorical neutrality of saturated shells](#conj:categorical-neutrality-saturated-shells).

**Relation to the existing tower picture.** The decomposition

$$
  \Phi_n
  \;=\;
  \Phi^{\mathrm{desc}} + \Phi^{\mathrm{trans}}
$$

into descended (Markov-trace) and transient (brane-tower) components
([mass endomorphism](#conj:mass-endomorphism))
remains intact under the global-section reading. What changes is the
*scope* of $\Phi^{\mathrm{trans}}$: every brane-tower contribution is
counted globally, none is localised to a sub-stratum and ignored.
The transient part is still summed over the Yekutieli tower, but the
sum is taken over the whole category, not over a chart-by-chart
patch decomposition.

**Operational consequence.** Numerical mass values previously
extracted via Hoefsmit matrix evaluation
([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form))
are reinterpreted as **empirical computational verification** of the
global-section prediction at strand counts $n \leq 10$ where the
matrices are still tractable; the prediction itself stands or falls
on the algebraic-geometry side, including for $n \geq 12$ where
matrix evaluation is no longer feasible
([k=12 barrier bypass](#rem:k12-barrier-bypass)).
