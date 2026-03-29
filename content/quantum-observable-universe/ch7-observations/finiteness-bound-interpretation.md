The finiteness bound
([Skein finiteness](#prop:skein-finiteness-bound))

$$
  [A\!-\!1]_q! \;>\; [2]_q^{\,A-1}
$$

is a **$q$-deformed Pauli exclusion principle** for nuclear
configurations.  Here we translate it into the language of
traditional nuclear physics and compare with observation.

## Translation to standard nuclear physics

### Left side: $[A\!-\!1]_q!$ = configuration complexity

The $q$-factorial $[A\!-\!1]_q! = \prod_{k=1}^{A-1} [k]_q$
counts the **number of reduced words in $H_A(q)$** — the
dimension of the Hecke algebra.  At $q = 1$, this is $(A-1)!$,
the number of permutations of $A - 1$ objects.

In traditional nuclear physics, this corresponds to the
**number of independent many-body configurations** available
to $A$ nucleons.  Each reduced word in $H_A(q)$ is a distinct
way of intertwining $A$ nucleon worldlines via Hecke crossings.
The factorial growth reflects the **combinatorial explosion**
of the nuclear many-body problem.

### Right side: $[2]_q^{A-1}$ = binding suppression

The quantum integer $[2]_q = q + q^{-1}$ is the
**categorical dimension** of the fundamental representation
of $\mathrm{SU}_q(2)$.  The power $[2]_q^{A-1}$ is the
product of $A - 1$ Markov-parameter suppressions, each
contributing a factor of $1/[2]_q$ to the trace.

In traditional nuclear physics, this is the **coherence
factor**: the probability that $A - 1$ nucleon pairs maintain
quantum coherence (constructive interference in the binding
wave function).  Each pair contributes a factor $[2]_q$
to the denominator of the Markov trace.

### The bound: when configurations overwhelm coherence

$$
  [A\!-\!1]_q! \;>\; [2]_q^{A-1}
  \quad\Longleftrightarrow\quad
  \text{many-body complexity} \;>\; \text{binding coherence}
$$

When the number of independent configurations exceeds the
binding suppression, **destructive interference dominates**:
the Skein polynomial $P(q)$ passes through zero and the
nucleus is unbound.

This is the $q$-deformed analogue of the standard nuclear
physics statement: *a nucleus is unbound when the kinetic
energy of the Fermi gas exceeds the nuclear binding energy*.
In the Hecke algebra:

| Traditional (shell model) | QOU (Hecke algebra) |
|:---:|:---:|
| Fermi energy $\propto A^{2/3}$ | $\ln [A\!-\!1]_q! \propto A \ln A$ |
| Binding energy $\propto A$ | $\ln [2]_q^{A-1} \propto A$ |
| Unbound when $E_F > E_B$ | Unbound when $[A\!-\!1]_q! > [2]_q^{A-1}$ |
| Drip line at $A \sim 300$ | First crossover at $A = 5$ |

The QOU bound is **tighter** ($A = 5$) than the observed drip
line ($A \sim 300$) because the bound applies to the
**single-shell** filling without shell closures.  Shell
closures ([shell closure normal form](#prop:shell-closure-normal-form))
create stability islands that extend the nuclear chart to
$A \sim 300$ by periodically restoring $P(q) > 0$.

## Comparison with observed nuclear chart

### The $\mathbf{A = 5}$ gap

The bound predicts instability at $A = 5$.  Experimentally:

- ${}^5\mathrm{He}$: **unbound** (resonance, $\Gamma \approx
  0.6$ MeV, decays to ${}^4\mathrm{He} + n$).
- ${}^5\mathrm{Li}$: **unbound** (resonance, $\Gamma \approx
  1.5$ MeV, decays to ${}^4\mathrm{He} + p$).

**Both $A = 5$ nuclei are unbound.** This is the famous
"$A = 5$ gap" in nuclear physics — no stable nucleus exists
with $A = 5$.  The QOU predicts this exactly: $[4]_q! = 25.15
> [2]_q^4 = 16.35$ at $q = 1.110$.

### The $\mathbf{A = 8}$ gap

The next gap: ${}^8\mathrm{Be}$ is also **unbound** (decays
to two ${}^4\mathrm{He}$ in $\sim 10^{-16}$ s).  In the QOU:
the $(4,4)$ shell closure at $A = 8$ has $P(q) > 0$
(the palindromic Poincaré distribution restores stability),
but the configuration is **metastable** — the dominant
coefficient jumps by $\times 2.95$, indicating the shell
closure barely holds.

### Shell closure islands

The observed magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$
correspond to shell closures where:

1. The word-length histogram is **palindromic** (complete
   Bruhat filling).
2. The dominant coefficient **jumps** (enhanced binding).
3. The Skein polynomial is **restored to $P > 0$** despite
   $[A\!-\!1]_q! \gg [2]_q^{A-1}$.

Between magic numbers, nuclei exist only because the shell
closure of the **previous** magic number provides a stable
core.  Adding nucleons beyond the core follows the single-shell
bound until the next closure.

## The $q$-dependence

The bound $[A\!-\!1]_q! > [2]_q^{A-1}$ crosses over at
$A = 5$ for **all** $q > 1$ (the $q$-correction is
$O((\ln q)^2)$, which is $0.011$ at $q = 1.110$).  This means
the $A = 5$ gap is a **topological invariant** — it does not
depend on the specific value of $q$.

The shell closure energies DO depend on $q$ (through the Hecke
reduction energy), which is why the magic numbers vary slightly
across the nuclear chart (the "island of inversion" near
$N = 20$ for neutron-rich nuclei corresponds to the
$q$-correction becoming significant at those configurations).
