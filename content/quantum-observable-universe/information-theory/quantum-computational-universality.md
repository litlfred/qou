**Conjecture.**
*Let $\beta$ be a braid on $n$ strands with $c = 3N$ crossings,
encoding a reversible computation of $N$ Toffoli gates
([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)).
Let $P_L(q)$ be the Skein polynomial of the braid closure
$\hat{\beta}$, with $\deg P_L \leq c^2 - 1$
([transfer matrix product](#prop:skein-polynomial-transfer-matrix)).*

*Then:*

1. **(Quadratic level.)** *There exists a root of unity
 $q_k = e^{2\pi i/(k+2)}$ with $k \geq 3$ and*

 $k + 2  \leq  c^2 - 1$

 *such that $P_L(q_k) \neq 0$ — the Skein polynomial does
 not degenerate at $q_k$. The level $k$ grows
 **quadratically** in the crossing number: a computation
 with $c$ crossings lives accordingly at level $k \sim c^2$.
 This is the degree of $P_L$: the minimal $k$ for which
 evaluation at $q_k$ retains all information of the
 computation without reduction modulo the cyclotomic
 ideal $(q^{k+2} - 1)$.*

2. **(Quantum universality.)** *At $q_k$ with $k \geq 3$, the
 braiding representation $\rho_{q_k} \colon B_n \to \mathrm{End}(V^{\otimes n})$ is dense in $\mathrm{SU}(2^n)$
 \cite{freedman2003}. Every quantum circuit on $n$ qubits
 with $N$ gates can be approximated to precision $\epsilon$
 by a braid $\beta$ with $c = O(N \cdot \mathrm{polylog}(1/\epsilon))$ crossings.*

3. **(:refterm[Descent]{#descent} projects quantum to classical.)** *The :refterm[descent]{#descent}
 involution $\hat{\tau}$
 ([:refterm[descent]{#descent} involution](#def:descent-involution)) decomposes
 the endomorphism algebra at the root-of-unity level into*

 $$
     \mathrm{End}(V^{\otimes n})
     = 
     \mathcal{A}^{\mathrm{desc}}  \oplus  \mathcal{A}^{\mathrm{trans}}
   $$

 *([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)).
 The descended subalgebra $\mathcal{A}^{\mathrm{desc}} = \mathrm{im}\hat{\tau}$ is the classical shadow — the
 Toffoli computation at real $q$. The transient complement
 $\mathcal{A}^{\mathrm{trans}} = \ker\hat{\tau}$ carries
 the quantum parallelism: exponentially many Skein
 resolution paths that destructively interfere upon
 observation.*

 *The projection $\hat{\tau}$ is observation: it collapses
 the quantum computation at $q_k$ to the classical
 computation at real $q$, with the transient modes erased.*

4. **(Information content.)** *The information content of the
 computation is the crossing number $c$ of the braid
 closure — the minimum jet order at which the computation
 first becomes resolvable
 ([jet–Planck steps](#rem:jet-planck-steps)). The Skein
 polynomial encodes up to $c^2 - 1$ independent
 coefficients (the full quantum state); the factored form
 $P_L(q) = \prod_i \hat{V}_i(q)$ compresses this to
 $O(c)$ factors (the observable output).*

*The flow from real $q$ to the root of unity $q_k$ is the
**lifting** of a classical computation to its quantum
completion
([complex substrate](#rem:complex-substrate-interpretation)):
$q$ leaves the real axis, traverses the complex plane, and
arrives at a point on the unit circle where the full density
of $\mathrm{SU}(2^n)$ becomes available. The :refterm[descent]{#descent}
involution projects back. The round-trip*

$$
  q_{\mathrm{real}}
  \xrightarrow{ \text{lift}}
  q_k = e^{2\pi i/(k+2)}
  \xrightarrow{\hat{\tau}}
  q_{\mathrm{real}}
$$

*is the quantum computation: the lift explores the full
Hilbert space; the :refterm[descent]{#descent} collapses it to the observable.*

**Archimedean specialisation (§7c).** This block is stated over the real field $\mathbb{R}$ — the archimedean side of the substrate wall: its constructs are real-valued (physical observables, real-analytic bounds, or numerical evaluations at the substrate parameter $q_0$) rather than generic-ring $q$-deformation data. The generic categorical / $q$-deformation machinery it draws on is stated over an abstract coefficient ring in its own blocks; only the archimedean realisation is specialised here.
