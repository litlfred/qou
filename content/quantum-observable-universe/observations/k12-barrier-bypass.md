**Computational state.** The Hoefsmit-seminormal magic-number signal
$\delta^2 \Phi(Z)$ in
[magic numbers from $q$](#prop:magic-numbers-from-q) is computed at
Hecke levels $k = 3 \dots 10$, with $k = 10$ ($42$ partitions,
$\dim \leq 768$) feasible in $48\,$s after the block-diagonal
optimisation. At $k = 12$ partition dimensions exceed
$\dim_q V_\lambda \gtrsim 2{,}000$ and the dense-matrix product chain
becomes intractable on commodity hardware (memory $\gtrsim 10\,$GB
per crossing, runtime $\gtrsim 1\,$h). The higher magic numbers
$\{50, 82, 126\}$ therefore lie beyond the matrix-evaluation
horizon.

**Analytic bypass.** The
[homological shell-condensation conjecture](#conj:homological-shell-condensation)
predicts the magic ladder $\{2, 8, 20, 28, 50, 82, 126\}$ purely
from collapse of a Białynicki–Birula spectral sequence at $E_2$.
This prediction is independent of $k$ and does not require Hoefsmit
matrix evaluation: the entire ladder, including the three magic
numbers $\{50, 82, 126\}$ that exceed the matrix-evaluation
horizon, is read off the algebraic-geometry side directly.

**Empirical computational verification.** The Hoefsmit numerical
agreement at $k = 3 \dots 10$
($\delta^2 \Phi$ peaks at $Z = 8, 20, 28$ with amplitudes
$+33.2, +20.4, +4.4$) is **not** the source of the magic-ladder
prediction in the refactored framework. It is reframed as
**empirical computational verification** of the homological
condensation prediction at the strand counts where matrix evaluation
is still tractable. The declining amplitude across $Z = 8, 20, 28$
is consistent with the expected resolution narrowing at higher
$k$ — and the framework predicts that running the same numerical
pipeline at $k \geq 12$, were it tractable, would yield further
peaks at $Z = 50, 82, 126$.

**Numerical witnesses to add.** Once the LR-fusion rigidity claim
([proposition 3](#conj:diagrammatic-double-magic-lr-fusion)) is
formalised in Lean, an explicit prediction of the dominant
self-conjugate composite for each magic pair $(Z, N)$ can be
extracted analytically and recorded in
`folio-assistant/computations/double-magic-witnesses.json`. This
gives a falsifiable numerical proxy for the full conjecture without
ever evaluating an $H_k(q)$ matrix at $k \geq 12$.
