[`prop:two-filtration-bridge-small-cases`](#prop:two-filtration-bridge-small-cases)
verified the bridge map $d_{\mathrm{II}}$ at all partitions of $n \leq 4$.
*This proposition extends the verification to **all** partitions of
any $n$ via a structural bar-eigenspace argument.*

### Statement

For every partition $\lambda$ (of any $n \geq 1$), the iterated-
integral depth predicted by the two-filtration bridge conjecture
([`conj:two-filtration-bridge`](#conj:two-filtration-bridge))
depends only on the **bar-class** of $\lambda$:

$$
  \boxed{\;
    d_{\mathrm{II}}(\lambda)
    \;=\;
    \begin{cases}
      2 & \text{if } \lambda \text{ is self-conjugate } (\lambda = \lambda'), \\
      3 & \text{if } \{\lambda, \lambda'\} \text{ is a chiral pair } (\lambda \neq \lambda').
    \end{cases}
  \;}
$$
### Corollaries

**Generalises round 9**: the small-cases bridge verification
at $n \leq 4$ extends to all $n$ via the bar-eigenspace argument.

**Corollary for B1**:
- For each self-conjugate cell, B1's depth-2 row is theorem-level
 (combining Bloch–Suslin + per-knot VC where available).
- For each chiral pair, B1's depth-3 row is conditional on the CS
 computation per knot.

**Combined with
[`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general)
+
[`prop:cyclotomic-trilog-imaginary-closed-form`](#prop:cyclotomic-trilog-imaginary-closed-form)**:
the depth-3 content over $\mathbb{Q}(\zeta_N)$ for every prime $N$ is
controlled by $\lfloor (N - 1)/2 \rfloor - 1$ genuinely-new real
numbers, all pairing with chiral-pair cells in the appropriate
$H_n(q)$.

### Cross-references

- Bridge conjecture: [`conj:two-filtration-bridge`](#conj:two-filtration-bridge)
- Small-cases verification: [`prop:two-filtration-bridge-small-cases`](#prop:two-filtration-bridge-small-cases)
- Chirality structure: [`rem:chirality-period-pairing`](#rem:chirality-period-pairing)
- Joint action discharge: [`prop:joint-galois-braid-discharged`](#prop:joint-galois-braid-discharged)
- Hecke-Baer-* and bar action on $e_\lambda$:
 [`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic),
 [`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent)
