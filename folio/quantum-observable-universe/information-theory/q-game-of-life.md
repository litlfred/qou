Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q$ and Planck time $t_P(q) = 1/\hbar_q$. Let $\mathcal{L} \subset M$ be a discrete sublattice of brane points $\{p_i\}$. Each site carries a qubit $|\psi_i\rangle \in \mathcal{S}_{p_i}$. The **$q$-Game of Life** ($q$-GoL) is the discrete-time invertible cellular automaton
$$
  \mathcal{U}_{\mathrm{q\text{-}GoL}}
    \colon  \mathcal{H}_{\mathcal{L}}
    \to  \mathcal{H}_{\mathcal{L}},
  \qquad
  |\Psi(t{+}1)\rangle
   = 
  \mathcal{U}_{\mathrm{q\text{-}GoL}}
  |\Psi(t)\rangle.
$$
The operator $\mathcal{U}_{\mathrm{q\text{-}GoL}}$ is constructed entirely from $q$-deformed Toffoli gates acting on Reeb bundle fibres of neighbour sites. The construction requires five properties:

1. **Building block.** The transition operator is the $q$-AND gate:
$$
  \mathrm{Toff}_q
  \colon  |c_1, c_2, t\rangle
  \longmapsto
  |c_1, c_2,  t \oplus_q (c_1 \wedge_q c_2)\rangle.
$$
The symbol $\wedge_q$ denotes the Hecke-algebra q-AND amplitude $P_{7,6}(q)$, given in the canonical convention $z_D$ under **Stability condition** below. Each $\mathrm{Toff}_q$ executes in three Planck steps.

This item previously defined $\wedge_q$ as $\Phi(q) = (q-1)(q^{3/2}+q^{1/2}-1)(q^{3/2}+q+1)/2(q+1)^2$, which is withdrawn: $\Phi$ is not in the image of the Toffoli construction under any indexing or convention ([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)), so it cannot be what $\wedge_q$ denotes.

2. **Superposition.** Cell states admit superpositions $|\psi_i\rangle = \alpha_i|0\rangle + \beta_i|1\rangle$ via Hadamard rotations $H \in \mathrm{End}(\mathcal{S}_{p_i})$. The set $\{\mathrm{Toff}_q, H\}$ is universal for **reversible** computation, in the sense of Bennett, for every $q > 0$: reversible universality needs the gate to be invertible with a firing target-flip channel, both of which item 4 and the non-vanishing of $P_{7,6}$ on $q \neq 1$ supply.

**Open.** This item formerly claimed universality for *quantum* computation. That is a stronger claim and is in tension with item 4: the standard Toffoli-plus-Hadamard universality theorem is a statement about unitary gates, and $\mathrm{Toff}_q$ is provably **not** unitary for $q \neq 1$. Whether a non-unitary invertible gate set can be universal in any quantum sense — and if so which — is not settled in this corpus, and the claim is narrowed to the reversible statement until it is.

3. **Conway's rules as Toffoli circuits.** Survival ($k = 2, 3$) and birth ($k = 3$) at site $i$ with neighbourhood $N(i)$ are enacted by the composite operator
$$
  \mathcal{U}_i^{\mathrm{rule}}
   = 
  \prod_{\{j_1, j_2\} \subset N(i)}
  \mathrm{Toff}_q
  \!\left(
    |\psi_{j_1}\rangle,  |\psi_{j_2}\rangle;  |\psi_i\rangle
  \right).
$$
Ancilla qubits encode the neighbour sum. A ripple-carry adder of $O(|N(i)|)$ Toffoli gates computes the binary count $k$.

4. **Reversibility.** Each $\mathrm{Toff}_q$ is invertible, with
$$
  \sigma_i^{-1}
   = 
  \sigma_i - (q - q^{-1})\cdot \mathbb{1},
$$
so $\mathcal{U}_{\mathrm{q\text{-}GoL}}$ is invertible and the automaton is reversible. It is **not** unitary away from the classical limit: the eigenvalues of $\sigma_i$ are $q$ and $-q^{-1}$, of modulus $\neq 1$ for $q \neq 1$, so no inner product makes $\mathrm{Toff}_q$ unitary, and the Markov trace form is degenerate under the production trace convention. Reversibility in the sense a reversible cellular automaton requires — invertibility of the tick — therefore holds for every $q > 0$, being a property of the quadratic relation alone and independent of the amplitude signs discussed below; unitarity holds only at $q = 1$.

5. **Information bandwidth budget.** One generation advances in $3 |\mathcal{L}|$ Planck steps. The substrate bandwidth $\mathfrak{B}(q) = q \eta_q / (q - 1)^2$ bounds the generation rate:
$$
  \text{gens / sec}
   \leq 
  \frac{\mathfrak{B}(q)}{3  |\mathcal{L}|}
   = 
  \frac{q \eta_q}{3  (q - 1)^2  |\mathcal{L}|}.
$$

**Well-definedness condition.** The evolution is well-defined only when the Toffoli diagonal $P_{7,7}(q)$ is positive and the q-AND amplitude $P_{7,6}(q)$ is **non-zero**. In the canonical convention $z_D = q^3/(q^2+1)$ the two amplitudes are

$$
  P_{7,7}^{D}(q) \,=\, \frac{q^{3}\bigl(q^{4}+1\bigr)}{\bigl(q^{2}+1\bigr)^{2}},
  \qquad
  P_{7,6}^{D}(q) \,=\, -\,\frac{(q-1)(q+1)\bigl(q^{6}+q^{4}+2q^{2}+1\bigr)}{2q\bigl(q^{2}+1\bigr)^{2}}.
$$

The second amplitude is written $P_{7,6}$, not $\Phi$. This is a naming correction only and leaves the criterion above exactly as ruled: $\Phi$ named a specific published closed form that the Toffoli construction does not produce under any indexing or convention, so it is retired as an *object* rather than re-derived in a new frame ([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)), and item 1 of this proposition already records that withdrawal.

For $q > 0$ the first is strictly positive, having no positive root. The second vanishes exactly at $q = 1$: the factor $(q+1)$ is positive there, and the sextic $q^{6}+q^{4}+2q^{2}+1$ has no positive real root, so the whole zero set on $q > 0$ is carried by $(q-1)$. The condition therefore holds on $q \neq 1$, which contains the substrate value $q_0 \approx 1.110$.

**Non-vanishing, not positivity.** The criterion is that the q-AND does not degenerate, not that it carry a particular sign. This is the same condition the universality argument of [Toffoli q-AND](#rem:toffoli-q-and) uses — it turns on $P_{7,6}(q) \neq 0$ — and it is what invertibility of the tick requires. At $q = 1$ the q-AND vanishes and the braiding ceases to act: that is the classical limit, where the $q$-Toffoli degenerates to the ordinary Toffoli, and it is the one point the condition excludes.

Strict positivity would be a different and stronger requirement. Under $z_D$ it holds only on $0 < q < 1$, since $P_{7,6}^{D}(q_0) \approx -0.1438$, and would place the substrate outside the well-defined regime. It is not the criterion in force here.

**A measurement that strengthens the ruling rather than reopening it.** Amplitude positivity was standing proxy for feasibility of the confinement LP. That proxy does not track what it proxies for. Constructing the q-Toffoli as an element of $H_3(q)$ — $T_q = \sigma_1 + \hbar_\times\,\sigma_0\sigma_1$ for the all-proton ordering — and evaluating the LP condition $G\vec t(q_0) \geq 0$ directly against the production Gram gives strictly positive components, for all eight strand-type orderings ([Toffoli LP-stability](#prop:toffoli-lp-stability)). So the substrate satisfies LP feasibility *as well as* non-vanishing; the counterfactual above is exact about amplitude positivity and would be wrong if read as "the LP would have excluded the substrate". Two caveats bound this: the Gram is entrywise non-negative and $\vec t$ is too for the all-proton ordering, so that ordering's positivity is forced by shape (2 of the 8 are trivial in this sense, 6 are not); and $\vec t$ turns negative on $0 < q < 1$, the *opposite* side of $q = 1$ from where $P_{7,6}$ does, so the amplitude sign and the cone condition disagree about which regime is admissible. A regime boundary at the golden-ratio threshold $q_\star = 1/\varphi^{2}$ is an artifact of the excised convention $C$ (see [Toffoli LP-stability](#prop:toffoli-lp-stability)); under $z_D$ the diagonal has no zero at all and $q_\star$ does not exist.
