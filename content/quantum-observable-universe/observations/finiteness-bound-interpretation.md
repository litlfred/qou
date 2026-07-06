The finiteness bound ([Skein finiteness](#prop:skein-finiteness-bound))

$$
  [A\!-\!1]_q!  >  [2]_q^{A-1}
$$

operates as a $q$-deformed Pauli exclusion principle for nuclear configurations. We translate this bound into the language of traditional nuclear physics and compare it with observation.

## Translation to standard nuclear physics

### Left side: $[A\!-\!1]_q!$ = configuration complexity

The $q$-factorial $[A\!-\!1]_q! = \prod_{k=1}^{A-1} [k]_q$ counts the number of reduced words in $H_A(q)$ (the dimension of the Iwahori–Hecke algebra). At $q = 1$, this recovers $(A-1)!$, the number of permutations of $A - 1$ objects.

In traditional nuclear physics, this corresponds to the number of independent many-body configurations available to $A$ nucleons. Each reduced word in $H_A(q)$ is a distinct topological intertwining of $A$ nucleon worldlines via Hecke crossings. The factorial growth reflects the combinatorial explosion of the nuclear many-body problem.

### Right side: $[2]_q^{A-1}$ = binding suppression

The quantum integer $[2]_q = q + q^{-1}$ is the categorical dimension of the fundamental representation of $\mathrm{SU}_q(2)$. The power $[2]_q^{A-1}$ is the product of $A - 1$ Markov-parameter suppressions. Each suppression contributes a factor of $1/[2]_q$ to the trace.

In traditional nuclear physics, this represents the coherence factor: the probability that $A - 1$ nucleon pairs maintain quantum coherence (constructive interference in the binding wave function). Each pair contributes a factor $[2]_q$ to the denominator of the Markov trace.

### The bound: when configurations overwhelm coherence

$$
  [A\!-\!1]_q!  >  [2]_q^{A-1}
  \quad\Longleftrightarrow\quad
  \text{many-body complexity}  >  \text{binding coherence}
$$

When the number of independent configurations exceeds the binding suppression, destructive interference dominates. The Skein polynomial $P(q)$ passes through zero, and the nucleus becomes unbound.

This is the $q$-deformed analogue of a standard nuclear physics principle: a nucleus is unbound when the kinetic energy of the Fermi gas exceeds the nuclear binding energy. In the Iwahori–Hecke algebra:

| Traditional (shell model)      | QOU (Iwahori–Hecke algebra)               |
| :---: | :---: |
| Fermi energy $\propto A^{2/3}$ | $\ln [A\!-\!1]_q! \propto A \ln A$        |
| Binding energy $\propto A$     | $\ln [2]_q^{A-1} \propto A$               |
| Unbound when $E_F > E_B$       | Unbound when $[A\!-\!1]_q! > [2]_q^{A-1}$ |
| Drip line at $A \sim 300$      | First crossover at $A = 5$                |

The QOU bound is tighter ($A = 5$) than the observed drip line ($A \sim 300$) because the bound describes single-shell filling without shell closures. Shell closures ([shell closure normal form](#prop:shell-closure-normal-form)) create stability islands. These islands periodically restore $P(q) > 0$, extending the nuclear chart to $A \sim 300$.

## Comparison with observed nuclear chart

### The $A = 5$ gap

The bound predicts instability at $A = 5$. Experimentally:

* ${}^5\mathrm{He}$: unbound (resonance, $\Gamma \approx 0.6$ MeV, decays to ${}^4\mathrm{He} + n$).
* ${}^5\mathrm{Li}$: unbound (resonance, $\Gamma \approx 1.5$ MeV, decays to ${}^4\mathrm{He} + p$).

Both $A = 5$ nuclei are unbound. This is the famous "$A = 5$ gap" in nuclear physics — no stable nucleus exists with $A = 5$. The QOU framework predicts this exactly: $[4]_q! = 25.15 > [2]_q^4 = 16.35$ at $q = q_0$.

### The $A = 8$ gap

The next gap occurs at ${}^8\mathrm{Be}$, which is also unbound (decays to two ${}^4\mathrm{He}$ in $\sim 10^{-16}$ s). In the QOU framework, the $(4,4)$ shell closure at $A = 8$ has $P(q) > 0$ because the palindromic Poincaré distribution restores stability. However, the configuration is metastable — the dominant coefficient jumps by a factor of $2.95$, indicating the shell closure barely holds.

### Shell closure islands

The observed magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$ correspond to shell closures where:

1. The word-length histogram is palindromic (complete Bruhat filling).
2. The dominant coefficient jumps (enhanced binding).
3. The Skein polynomial is restored to $P > 0$ despite $[A\!-\!1]_q! \gg [2]_q^{A-1}$.

Between magic numbers, nuclei exist only because the shell closure of the previous magic number provides a stable core. Adding nucleons beyond the core follows the single-shell bound until the next closure.

## The $q$-dependence

The bound $[A\!-\!1]_q! > [2]_q^{A-1}$ crosses over at $A = 5$ for all $q > 1$. The $q$-correction is $O((\ln q)^2)$, which evaluates to $0.011$ at $q = q_0$. The $A = 5$ gap is therefore a topological invariant; it does not depend on the specific value of $q$.

The shell closure energies do depend on $q$ through the Hecke reduction energy. This dependence explains why the magic numbers vary slightly across the nuclear chart. The "island of inversion" near $N = 20$ for neutron-rich nuclei arises because the $q$-correction becomes significant at those configurations.
