**Conjecture (computational-time identification of the Schwinger variable).**

Let $s$ denote the Schwinger proper-time variable of the $\zeta$-regularized one-loop photon determinant on the Bring Jacobian, whose loop expansion weighs proper time by the scale-invariant measure $\varsigma\,\frac{ds}{s}$ with unit $\varsigma$ ([`def:schwinger-measure-unit`](#def:schwinger-measure-unit); the shape is the unique scale-invariant density, the unit is the open content of R2-core). Let $N(n)$ denote the binding normalizer forced by the keystone bridge — the unique strip $N(n) = (n-1)!$ making the binding generating function the carrier of the proved depth-2 confluent kernel (the normalization leg of [`conj:qdifference-kernel-prolongation-symbol`](#conj:qdifference-kernel-prolongation-symbol)).

The framework premises are named:

- **P1 (scale-freedom):** the substrate is scale-free; the locally realized modulus $q_0$ is local data, not a structural scale of the substrate.
- **P2 (computational time):** proper time is computational time — $s$ counts the substrate's computation steps.

**Statement.** *The binding sector's Borel variable and the loop's Schwinger proper time $s$ are the same substrate object.* Under P2 both are the substrate's computational time, and the identification takes the quantitative form: the keystone normalizer is the $n$-th moment of the loop's proper-time measure,

$$
N(n) \;=\; \int_0^\infty s^{\,n}\, e^{-s}\,\varsigma\,\frac{ds}{s} \;=\; \varsigma\,(n-1)! .
$$

**Conditional consequences.** Both are conditional on this conjecture (together with P1/P2 where noted); neither is a derivation of it.

1. **The unit is forced: $\varsigma = 1$.** The Lean-proved keystone identity $n \cdot N(n) = n!$ rescales under a unit $\varsigma$ to $\varsigma \cdot n! = n!$, so $\varsigma = 1$ exactly; the rival value $\varsigma = \tfrac12$ gives $n!/2 \neq n!$ (an exact distinguisher, proved unconditionally in the sibling Lean). Conditionally, this closes R2-core's unit — one nat per proper-time e-fold, with $k_B = 1$ so that entropy is counted in nats ([`prop:boltzmann-constant`](#prop:boltzmann-constant)).
2. **The $\tfrac12$ is located per-channel bar-even.** With total unit $\varsigma = 1$, the working per-channel coefficient $\tfrac12\,a_0 = 1/(8\pi)$ — where $a_0 = 1/(4\pi)$ is the derived two-dimensional heat-kernel unit entering the $\alpha_{EM}$ insertion ([`prop:em-coupling-fixed-point`](#prop:em-coupling-fixed-point)) — arises from the doubled-pair channel split. For the doubled bar pair $(q, q^{-1}) \leftrightarrow (t, 1/t)$ and a bar-even integrand $f$, i.e. $f(t) = f(1/t)$ under the bar involution $t \mapsto 1/t$, the exact fold identity $\int_0^\infty f(t)\,\tfrac{dt}{t} = 2\int_1^\infty f(t)\,\tfrac{dt}{t}$ places the $\tfrac12$ per channel on the bar-even side, while a bar-odd integrand receives $0$. This tips the $\tfrac12$-adjudication toward the $\rho$-split reading (total unit one, the $\tfrac12$ in the channel split) and against the energy-Jacobian reading ($\varsigma = \tfrac12$ on the proper-time side), which would break the moment identity.

The identification is a dictionary premise between two sectors — the $\alpha_{EM}$ loop measure and the binding $q$-Borel transform — of the same species as R2 itself. It is stated here as a precise, falsifiable structural claim: a derivation closes R2-core's unit; a refutation removes the lead. The two sectors would share one unit, and the binding side's is Lean-forced; the checkable content is the moment identity above, recorded exactly at orders $n = 1$ through $6$ in the exploration witness.

**Fibre-level refinement (bar-parity, 2026-07-25).** The statement above is archimedean ($q = 1$), where the proper time $s$ is real and hence bar-invariant. At the fibre level ($q \neq 1$) the identification is consistent only in the *balanced* $q$-Borel convention: the one-sided normalizer $[n-1]_q!$ is bar-covariant with exact weight $q^{-(n-1)(n-2)/2}$, so it cannot equal a bar-invariant proper-time object, while the balanced normalizer $q^{-(n-1)(n-2)/4}\,[n-1]_q!$ is exactly bar-invariant with vanishing first-order $q$-correction. The conjecture is therefore to be read in the balanced convention; the one-sided reading is refuted at $q \neq 1$ (exact weight mismatch, machine-verified at both substrate pins).
