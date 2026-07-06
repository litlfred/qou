**Remark (Frobenius self-dual channel of molecular bound states).**
*The two Wedderburn channels carrying force-carrier content in the
H_2 molecular bound state — $\lambda^{(T_{3,5})} = (3, 1)$ and
$\lambda^{(T_{2,9})} = (2, 1, 1)$ from
[`prop:force-carrier-intertwining-correspondence`](#prop:force-carrier-intertwining-correspondence)
— are **transpose partitions** of each other:*

$$
  (3, 1)^{T} \;=\; (2, 1, 1).
$$

*Equivalently, the corresponding Young diagrams are mirror
reflections through the diagonal.*

### Frobenius self-duality

In the Hecke-algebra Wedderburn decomposition, transpose
partitions correspond to Hopf-antipode-conjugate irreducible
representations:

$$
  S\bigl(V_\lambda\bigr) \;\cong\; V_{\lambda^{T}}.
$$

A representation pair $(V_\lambda, V_{\lambda^T})$ is closed under
the Hopf-antipode action $S$ — this is precisely the
**Frobenius self-dual** structure.

For $\lambda = (3, 1)$ in $H_4(q)$:

- $\dim_q V_{(3,1)} = \dim_q V_{(2,1,1)}$
- $w_{(3,1)} = w_{(2,1,1)} = \dim_q^{2} / [4]_q!$
- $f^{(3,1)} = f^{(2,1,1)} = 3$ (number of standard Young tableaux)

The two channels carry **identical Wedderburn weights**.  Their
joint contribution to the molecular Markov trace —

$$
  w_{(3,1)} \cdot \frac{\chi_{(3,1)}(\beta) + \chi_{(2,1,1)}(\beta)}{f^{(3,1)}}
  \;=\;
  w_{(3,1)} \cdot \frac{\chi_{(3,1)}(\beta) + \chi_{(2,1,1)}(\beta)}{3}
$$

— is **invariant under the Hopf antipode** acting on the
molecular braid $\beta$.  This is the categorical analogue of
parity-symmetry: the bound state is self-conjugate, matching the
physical fact that $H_2$ has $J^{P} = 0^{+}$ ground state.

### Empirical signature in the witness

At $q_0 \approx 1.110$
([`delta-q-decoration.witness.json`](computations/delta-q-decoration.witness.json)):

| $\lambda$ | $\chi_\lambda(\sigma_1\sigma_2\sigma_3)$ | $w_\lambda \cdot \chi_\lambda/f^\lambda$ |
|---|---:|---:|
| $(3, 1)$ | $-1.110$ | $-0.136$ |
| $(2, 1, 1)$ | $+0.901$ | $+0.111$ |
| Sum (joint contribution) | — | $-0.025$ |

The two channels have **opposite signs**, with the magnitudes
nearly equal (modulo dressing differences). Their sum is
$-0.025$, a small residual reflecting the asymmetry between the
"3-strand intertwining" and "2-strand + 2-free" combinatorial
patterns.

### Connection to chirality and antiparticle structure

The transpose-pair structure connects to the **antiparticle
crossing-reversal** mechanism
([`prop:antiparticle-crossing-reversal`](#prop:antiparticle-crossing-reversal)):

- Crossing reversal $\sigma$ acts on the Hecke algebra by
  $\sigma_i \mapsto \sigma_i^{-1}$, equivalently $q \mapsto q^{-1}$.
- This induces $V_\lambda \mapsto V_{\lambda^{T}}$ on irreps —
  exactly the transpose action.
- A bound state in the **self-dual sub-sector**
  $V_{(3,1)} \oplus V_{(2,1,1)}$ is invariant under
  particle-antiparticle exchange, consistent with the
  electrical neutrality of the $H_2$ molecule (zero net charge).

### Significance

The Frobenius self-dual structure of the molecular bound-state
channel is **not a coincidence** — it is forced by the combination
of:

1. The genus-$4$ Bring force-carrier sector
   ([`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness)),
   which gives exactly two torus knots $T_{2,9}, T_{3,5}$.
2. The strand-count constraint
   ([`prop:force-carrier-intertwining-correspondence`](#prop:force-carrier-intertwining-correspondence)),
   which maps each force carrier to a partition with exactly one
   "fat" part.
3. The arithmetic of partitions of $4$:
   $\{(p, 1^{4-p}) : p = 2, 3\} = \{(2, 1, 1), (3, 1)\}$,
   which happen to be transpose of each other.

For other strand counts $n$, the analogous "force-carrier
Wedderburn channels" are $(p, 1^{n-p})$ for $p \leq n$.  These
are *not* transpose pairs in general — the self-duality at $n=4$
is special to the genus-$4$ Bring constraint matching the
4-strand H_2 molecular structure.

This may explain why the **simplest covalent bond** ($H_2$) has
a particularly clean categorical structure compared to larger
molecules.
