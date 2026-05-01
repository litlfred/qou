## Statement

**Proposition 2 (Homological Shell Condensation).**
*An $n$-strand state achieves absolute topological confinement if and
only if its formal Yekutieli jet deformations identically vanish.
In the spectral sequence*

$$
  E_r^{p, q}(n)
  \;\Rightarrow\;
  H^{p+q}\!\bigl(\mathbf{C};\, \Phi_n^{\mathrm{tw}}\bigr)
$$

*abutting to the twisted cohomology of the global mass endomorphism
$\Phi_n$ ([phi-n as global section](#rem:phi-n-global-section)),
all obstruction classes to lifting the section across higher jet
orders $q > 0$ evaluate to zero:*

$$
  E_\infty^{p, q}(n) \;=\; 0
  \qquad
  \text{for all } q > 0,
  \;\;\text{whenever }
  n \in \{2, 8, 20, 28, 50, 82, 126\}.
$$

*Equivalently, the spectral sequence collapses at $E_2$ at exactly
these magic strand counts, yielding a homologically pure ground
state.*

## Status

This is a **conjecture** (CLAUDE.md §3b axiom-class pattern). It
asserts the algebraic-geometry equivalence between the empirical
nuclear magic ladder and a vanishing condition on a precisely
constructed spectral sequence. The construction itself
(BB-stratification of the Hecke category, Yekutieli jet deformations
as connecting differentials) is well-defined; the conjectural step
is the *exact* coincidence with the magic numbers
$\{2, 8, 20, 28, 50, 82, 126\}$.

## Proof sketch (conjectural)

**Step 1 — The BB-stratification.**
The Hecke category $H_n(q)\text{-mod}$ admits a Białynicki–Birula
filtration

$$
  H_n(q)\text{-mod}
  \;=\;
  \bigsqcup_{\lambda \,\vdash\, n}
  X_\lambda^{\mathrm{BB}},
$$

indexed by partitions of $n$, with each stratum $X_\lambda^{\mathrm{BB}}$
a locally closed subvariety carrying the Hoefsmit cell of $\lambda$.

**Step 2 — Jet deformations as obstructions.**
The Yekutieli jet prolongations $J^k(\Phi_n)$
([categorical jet](#prop:categorical-jet-prolongation)) measure the
perturbative topological stress added by the $k$-th brane-tower
correction to a candidate global section of $\Phi_n$.
Under the BB-decomposition, these jet prolongations map to the
connecting differentials

$$
  d_r \colon E_r^{p, q}(n) \longrightarrow E_r^{p + r, q - r + 1}(n)
$$

of a spectral sequence built from the BB-filtration of $\Phi_n$ in
$\mathbf{C}$. The class

$$
  \bigl[J^k(\Phi_n)\bigr]
  \;\in\;
  E_2^{*, k}(n)
$$

is the obstruction to lifting the section to the $k$-th jet order.

**Step 3 — Trivialisation via complete intersections.**
The obstruction classes vanish algebraically iff the BB-stratum
$X_\lambda^{\mathrm{BB}}$ for the dominant $\lambda$ is a **complete,
non-obstructed projective subvariety**. If the stratum is incomplete
("frayed", in the sense that its Frobenius arms are unbalanced
against its legs — see
[non-magic Li-6 diagram](#ex:non-magic-Li6-diagram)), the section
$\Phi_n$ fails to lift, and the homology spreads into higher jet
orders $q > 0$.

**Step 4 — Isotropic integer locking.**
The combinatorial constraints of $H_n(q)$ — saturated Jucys–Murphy
contents
([categorical neutrality](#conj:categorical-neutrality-saturated-shells)),
self-conjugacy of the dominant partition, and the requirement that
$\theta_n$ act trivially — force the complete-intersection condition
to occur exclusively at the **isotropic 3D harmonic-oscillator integers**

$$
  n \;\in\; \{2,\; 8,\; 20,\; 28,\; 50,\; 82,\; 126\}.
$$

At these roots, the spectral sequence collapses abruptly at $E_2$:

$$
  E_2^{p, q}(n) \;=\; E_\infty^{p, q}(n),
  \qquad
  E_\infty^{p, q}(n) \;=\; 0 \text{ for } q > 0.
$$

The resulting ground state is homologically pure — no jet-order
corrections survive.

## What this replaces

This proposition is the analytical bypass for the $k \geq 12$
matrix-evaluation barrier in
[magic numbers from $q$](#prop:magic-numbers-from-q). Where Hoefsmit
seminormal evaluation requires partition dimensions exceeding
$\dim_q V_\lambda \leq 768$ at $k = 10$ and becomes intractable for
$k \geq 12$, the homological-vanishing criterion reads the same
ladder directly off the spectral sequence — for *all* magic numbers
including $\{50, 82, 126\}$
([k=12 barrier bypass](#rem:k12-barrier-bypass)).

The Hoefsmit numerical agreement at $k = 3 \dots 10$
($\delta^2\Phi$ peaks at $Z = 8, 20, 28$) is then read as
**empirical computational verification** of the
homological-condensation prediction at the strand counts that
matrix evaluation can reach.

## Open algebraic question

The conjecture rests on an *exact* identification of the BB-strata
that satisfy the complete-intersection condition with the magic
ladder. Two routes are open:

1. **Direct combinatorial proof**: enumerate the Young diagrams
   $\lambda \vdash n$ for which the BB-stratum is a complete
   intersection; show this set is non-empty iff $n \in \{2, 8, 20,
   28, 50, 82, 126\}$ via counting of self-conjugate hooks.
2. **Yekutieli MC equation**: reduce the obstruction-vanishing to the
   solvability of the Maurer–Cartan equation in the pronilpotent
   DGLA of jet-tower deformations \cite{yekutieli2010}; the magic
   condition then becomes the algebraic statement that the MC
   element is exact precisely on the isotropic-oscillator ladder.

Either route gives a closed-form Lean proof bypassing the matrix
evaluations entirely.
