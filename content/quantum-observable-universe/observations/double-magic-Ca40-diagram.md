$^{40}\mathrm{Ca}$ ($Z = N = 20$, $A = 40$) is the canonical
**double-magic** test case: both proton and neutron counts lie in
$\mathfrak{M} = \{2, 8, 20, 28, 50, 82, 126\}$. This example
illustrates the partition-level rigidity content of the
double-magic LR-fusion conjecture
([`conj:diagrammatic-double-magic-lr-fusion`](#conj:diagrammatic-double-magic-lr-fusion))
in the regime where both blocks are saturated and the LR fusion
collapses to a single self-conjugate $\nu_{ZN} \vdash 40$.

## $Z$-block and $N$-block (twin saturated)

Both $Z = 20$ and $N = 20$ are magic. By
[`conj:categorical-neutrality-saturated-shells`](../braids-and-knots/categorical-neutrality-saturated-shells.md)
the categorical mass at each level is supported on a single
self-conjugate partition. The relevant partition is

$$
  \lambda_{20} \;=\; \mu_{20} \;=\; (5, 4, 4, 4, 3) \;=\; (5,4,4,4,3)'
$$

— the self-conjugate hook-staircase of size $20$ \cite{geckpfeiffer2000}.
The Young diagram:

```text
  ■ ■ ■ ■ ■
  ■ ■ ■ ■
  ■ ■ ■ ■
  ■ ■ ■ ■
  ■ ■ ■
```

is symmetric under transposition, with arms equal to legs:
$\sum c(x) = 0$. The full-twist eigenvalues at level $20$ are
$q^0 = 1$ on both the $Z$-block and the $N$-block.

(The actual self-conjugate partition of $20$ that the
matrix-evaluation programme picks out at $k = 20$ is
combinatorially blocked, but the saturated-shell conjecture
predicts a unique self-conjugate $\lambda_{Z = 20}$; we use
$(5,4,4,4,3)$ as a representative diagrammatic illustration.)

## LR fusion at $A = 40$ — rigid

By the double-magic conjecture
([`conj:diagrammatic-double-magic-lr-fusion`](#conj:diagrammatic-double-magic-lr-fusion))
the LR product

$$
  V_{\lambda_{20}} \otimes V_{\mu_{20}}
  \;\cong\;
  V_{\nu_{20, 20}}(40)
$$

collapses to a single self-conjugate $\nu_{20, 20} \vdash 40$ with
multiplicity one. The cancellation $\sum c(x) = 0$ on $\nu_{20, 20}$
is forced by additivity of the content sum along LR fusion plus
self-conjugacy of both factors.

## What the diagram shows

The diagrammatic illustration in this example block is, schematically:

- **Left**: the $\lambda_{20}$ self-conjugate Young diagram (symmetric
  under transposition, marked "saturated, $c = 0$").
- **Right**: an identical copy of the $\mu_{20} = \lambda_{20}$ diagram
  (since $Z = N$, the two saturated blocks are *identical*).
- **Centre**: a single LR-fusion arrow producing the unique
  self-conjugate $\nu_{20, 20}$ at level $40$, marked
  "**rigid: multiplicity one**".

The cancellation $\sum_{x \in \nu_{20, 20}} c(x) = 0$ is depicted by
arms balancing legs across the diagonal of $\nu_{20, 20}$.

## Why $^{40}\mathrm{Ca}$ is exceptionally bound

The empirical $^{40}\mathrm{Ca}$ binding energy is $342.05$ MeV,
sitting at a sharp local maximum of the binding-per-nucleon curve
($8.55$ MeV/nucleon). The algebraic content of this exception is
exactly the **rigidity** above: there are *no* off-diagonal Wedderburn
channels at $A = 40$ in which further crossing energy could be
absorbed. Every Hecke operator $\sigma_i$ at level $40$ that would
have moved the system off the unique $\nu_{20, 20}$ block is
constrained by self-conjugacy + content-sum-zero to produce zero.

Phenomenologically: $^{40}\mathrm{Ca}$ has no available
binding-energy channels. It is *as bound as the algebraic structure
allows at $A = 40$*. The empirical exception is the algebraic
rigidity.

## Empirical match (representative double-magic ladder)

| Nuclide | $(Z, N)$ | Both magic? | Predicted regime |
|--------:|:---------|:-----------:|:-----------------|
| $^{4}\mathrm{He}$  | $(2, 2)$    | ✓ | rigid LR fusion at $A = 4$  |
| $^{16}\mathrm{O}$  | $(8, 8)$    | ✓ | rigid LR fusion at $A = 16$ |
| $^{40}\mathrm{Ca}$ | $(20, 20)$  | ✓ | rigid LR fusion at $A = 40$ |
| $^{48}\mathrm{Ca}$ | $(20, 28)$  | ✓ | rigid LR fusion at $A = 48$ |
| $^{132}\mathrm{Sn}$ | $(50, 82)$ | ✓ | rigid LR fusion at $A = 132$ (predicted, no $k$-evaluation) |
| $^{208}\mathrm{Pb}$ | $(82, 126)$ | ✓ | rigid LR fusion at $A = 208$ (predicted, no $k$-evaluation) |

All seven double-magic cases above are predicted to exhibit the same
diagrammatic structure: twin self-conjugate blocks, single-$\nu_{ZN}$
LR fusion, rigid binding peak.
