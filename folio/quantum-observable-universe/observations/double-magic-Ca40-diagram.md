$^{40}\mathrm{Ca}$ ($Z = N = 20$, $A = 40$) is the canonical double-magic test case. Both proton and neutron counts lie in $\mathfrak{M} = \{2, 8, 20, 28, 50, 82, 126\}$. This example illustrates the partition-level rigidity of the [double-magic LR-fusion conjecture](#conj:diagrammatic-double-magic-lr-fusion) in the regime where both blocks are saturated and the LR fusion collapses to a single self-conjugate $\nu_{ZN} \vdash 40$.

## Twin saturated blocks

Both $Z = 20$ and $N = 20$ are magic. By [saturated-shell categorical neutrality](../mass-endomorphism/categorical-neutrality-saturated-shells.md), the categorical mass at each level is supported on a single self-conjugate partition, illustrated diagrammatically here by the self-conjugate hook-staircase of size $20$ \cite{geckpfeiffer2000}:

$$
  \lambda_{20} \;=\; \mu_{20} \;=\; (5, 5, 4, 4, 2) \;=\; (5,5,4,4,2)'
$$

```text
  ■ ■ ■ ■ ■
  ■ ■ ■ ■ ■
  ■ ■ ■ ■
  ■ ■ ■ ■
  ■ ■
```

This diagram is symmetric under transposition. Arms equal legs, yielding $\sum c(x) = 0$. The full-twist eigenvalues at level $20$ are $q^0 = 1$ on both the $Z$-block and the $N$-block.

## Rigid LR fusion at $A = 40$

The double-magic conjecture predicts the LR product collapses to a single self-conjugate $\nu_{20, 20} \vdash 40$ with multiplicity one:

$$
  V_{\lambda_{20}} \otimes V_{\mu_{20}}
  \;\cong\;
  V_{\nu_{20, 20}}(40)
$$

The cancellation $\sum c(x) = 0$ on $\nu_{20, 20}$ follows from the additivity of the content sum along LR fusion and the self-conjugacy of both factors.

The associated diagrammatic structure consists of:

- **Left**: The $\lambda_{20}$ self-conjugate Young diagram (symmetric, $c = 0$).
- **Right**: An identical copy $\mu_{20} = \lambda_{20}$.
- **Centre**: A single LR-fusion arrow targeting $\nu_{20, 20}$ at level $40$, rigid with multiplicity one.

Arms balance legs across the diagonal of $\nu_{20, 20}$, depicting the cancellation $\sum_{x \in \nu_{20, 20}} c(x) = 0$.

## Exceptional binding of $^{40}\mathrm{Ca}$

The empirical $^{40}\mathrm{Ca}$ binding energy is $342.05$ MeV. This is a local maximum on the binding-per-nucleon curve ($8.55$ MeV/nucleon). This empirical peak matches the algebraic rigidity. At $A = 40$, no off-diagonal Wedderburn channels exist to absorb further crossing energy. Self-conjugacy and a zero content sum constrain every Hecke operator $\sigma_i$ at level $40$ that would move the system off the $\nu_{20, 20}$ block to produce zero.

$^{40}\mathrm{Ca}$ lacks available binding-energy channels. The structure is maximally bound under the algebraic constraints at $A = 40$.

## Empirical match

See [Table](#tbl:double-magic-Ca40-diagram-table-data).

All seven double-magic cases exhibit the same diagrammatic structure: twin self-conjugate blocks, single-$\nu_{ZN}$ LR fusion, and a rigid binding peak.
