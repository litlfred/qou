**Conjecture.** Let $\beta$ be a braid on $n$ strands with $c = 3N$ crossings, encoding a reversible computation of $N$ Toffoli gates. Let $P_L(q)$ be the Skein polynomial of the braid closure $\hat{\beta}$, with $\deg P_L \leq c^2 - 1$. Then:

1. **(Quadratic level.)** There exists a root of unity $q_k = e^{2\pi i/(k+2)}$ with $k \geq 3$ and $k + 2 \leq c^2 - 1$ such that $P_L(q_k) \neq 0$. The minimal level $k$ grows quadratically with the crossing number: $k \sim c^2$. Evaluation at $q_k$ preserves all information of the computation without reduction modulo the cyclotomic ideal.
2. **(Quantum universality.)** At $q_k$ with $k \geq 3$, the braiding representation $\rho_{q_k} \colon B_n \to \mathrm{End}(V^{\otimes n})$ is dense in $\mathrm{SU}(2^n)$. Every quantum circuit on $n$ qubits with $N$ gates can be approximated to precision $\epsilon$ by a braid $\beta$ with $c = O(N \cdot \mathrm{polylog}(1/\epsilon))$ crossings.
3. **(Descent projects quantum to classical.)** The descent involution $\hat{\tau}$ decomposes the endomorphism algebra at the root-of-unity level into
$$
  \mathrm{End}(V^{\otimes n}) = \mathcal{A}^{\mathrm{desc}} \oplus \mathcal{A}^{\mathrm{trans}}.
$$
The descended subalgebra $\mathcal{A}^{\mathrm{desc}}$ constitutes the classical shadow: the Toffoli computation at real $q$. The transient complement $\mathcal{A}^{\mathrm{trans}}$ carries the quantum parallelism: exponentially many Skein resolution paths that destructively interfere upon observation. The projection $\hat{\tau}$ represents observation. It collapses the quantum computation to the classical computation at real $q$.
4. **(Information content.)** The information content of the computation is the crossing number $c$. The Skein polynomial encodes up to $c^2 - 1$ independent coefficients representing the full quantum state. The factored form $P_L(q) = \prod_i \hat{V}_i(q)$ compresses this to $O(c)$ observable factors.

The flow from real $q$ to the root of unity $q_k$ signifies the lifting of a classical computation to its quantum completion. The parameter $q$ leaves the real axis, traverses the complex plane, and arrives on the unit circle where $\mathrm{SU}(2^n)$ density applies. The descent involution projects back. The round-trip
$$
  q_{\mathrm{real}} \xrightarrow{\text{lift}} q_k = e^{2\pi i/(k+2)} \xrightarrow{\hat{\tau}} q_{\mathrm{real}}
$$
forms the quantum computation. The lift explores the Hilbert space; the descent collapses it to the observable.
