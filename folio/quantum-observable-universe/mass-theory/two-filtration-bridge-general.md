[Two-filtration bridge map verified at small partitions ($n \leq 4$)](#prop:two-filtration-bridge-small-cases)
verified the bridge map $d_{\mathrm{II}}$ at all partitions of $n \leq 4$.
*This conjecture proposes the extension to **all** partitions of any $n$.
It is conditional: it rests on
[Two-filtration bridge](#conj:two-filtration-bridge), which defines
$d_{\mathrm{II}}$, and on an unproved matching of the transposing involution
$\#$ on $H_n(q)$ with orientation reversal on periods. The bar involution
itself fixes every $e_\lambda$ and does not separate $\lambda$ from
$\lambda'$.*

*What is proved.* [Cell-depth filtration of $Z(H_n(q))$](#prop:cellular-depth-filtration),
item 4, is the provable core: under two named hypotheses (H-match: $\#$ is
intertwined with orientation reversal by a realisation map $\Phi$; H-parity:
orientation reversal acts on depth-$d$ periods by $(-1)^d$), odd-depth
components vanish on self-conjugate cells and are antisymmetric under
$\lambda\leftrightarrow\lambda'$. It does not give the values $2$ and $3$,
which need a further non-vanishing. Note also that the "otherwise" branch of the
definition of $d_{\mathrm{II}}$ in
[Two-filtration bridge](#conj:two-filtration-bridge) is empty, since every
partition is either self-conjugate or half of the pair $\{\lambda,\lambda'\}$.
So the boxed formula below restates that definition; the content of this
conjecture is the existence of a realisation for which it is non-degenerate.

### Statement

For every partition $\lambda$ (of any $n \geq 1$), the iterated-
integral depth predicted by the two-filtration bridge conjecture
([Two-filtration bridge](#conj:two-filtration-bridge))
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

**Scope**: the small-cases table at $n \leq 4$ is a comparison (the
cell-to-knot assignment there is chosen, not derived), so it does not
"extend" to all $n$; the general-$n$ content is item 4 of
[Cell-depth filtration of $Z(H_n(q))$](#prop:cellular-depth-filtration).

**Corollary for the depth correspondence**:
- For each self-conjugate cell, its depth-2 row is conditional on the
 bridge conjecture (with Bloch–Suslin and the per-knot volume conjecture
 where available).
- For each chiral pair, its depth-3 row is conditional on the CS
 computation per knot.

**Comparison, not a consequence.**
[General orbit-sum identity](#prop:cyclotomic-cl3-orbit-sum-general)
and
[Trilogarithm imaginary part at $\zeta_n$](#prop:cyclotomic-trilog-imaginary-closed-form)
count the depth-3 content over $\mathbb{Q}(\zeta_N)$ for prime $N$ as
$\lfloor (N - 1)/2 \rfloor - 1$ new real numbers. That these pair with
chiral-pair cells of some $H_n(q)$ would need the realisation $\Phi$ above;
it does not follow from this conjecture as stated.

### Cross-references

- Proved core: [Cell-depth filtration of $Z(H_n(q))$](#prop:cellular-depth-filtration)
- Bridge conjecture: [Two-filtration bridge](#conj:two-filtration-bridge)
- Small-cases verification: [Two-filtration bridge map verified at small partitions ($n \leq 4$)](#prop:two-filtration-bridge-small-cases)
- Chirality structure: [Chirality structure on Goncharov period classes via the bar involution](#rem:chirality-period-pairing)
- Joint action discharge: [Joint motivic-Galois $\times$ braid action commutes on every bi-filtration cell — discharged](#prop:joint-galois-braid-discharged)
- Hecke-Baer-* and bar action on $e_\lambda$:
 [Iwahori--Hecke algebra $H_n(q)$ is a Baer-*-ring at generic $q$](#prop:hecke-baer-star-generic),
 [Explicit central primitive idempotents $e_\lambda$ via Murphy elements](#prop:explicit-central-idempotent)
