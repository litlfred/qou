$^{6}\mathrm{Li}$ ($Z = N = 3$, $A = 6$) is the canonical
**non-magic** test case: neither proton nor neutron count lies in
$\mathfrak{M}$. This example illustrates the partition-level
diagrammatic content of the double-magic LR-fusion conjecture
([`prop:diagrammatic-double-magic-lr-fusion`](#prop:diagrammatic-double-magic-lr-fusion))
in the regime where *both* blocks are frayed, the categorical
mass at each level spreads over multiple non-self-conjugate
partitions, and the LR fusion produces non-zero **full-twist flux
vectors** in both the $Z$ and $N$ tensor factors.

## $Z$-block (frayed)

The proton count $Z = 3$ is not magic. The categorical mass at
level $3$ is *not* concentrated on a single self-conjugate
partition; instead the Wedderburn support spans

$$
  \lambda \in \{(3),\, (2, 1),\, (1, 1, 1)\} \;\vdash\; 3,
$$

with content sums $c((3)) = +3$, $c((2,1)) = 0$, $c((1,1,1)) = -3$.
Of the three, only $(2, 1)$ is self-conjugate (and lies on the main
diagonal of Young's lattice); the symmetric and antisymmetric
partitions $(3)$ and $(1, 1, 1)$ are conjugates of each other and
contribute opposite-sign full-twist eigenvalues
$q^{+3}$ vs. $q^{-3}$.

Frobenius arms exceed legs in $(3)$ (three arms, no legs);
legs exceed arms in $(1, 1, 1)$. Neither alone is balanced.

## $N$-block (also frayed)

By symmetry the same three partitions $\{(3), (2, 1), (1, 1, 1)\}$
contribute on the $N$ side, with the same content-sum imbalances.

## LR fusion at $A = 6$

The LR product
$V_\lambda(Z=3) \otimes V_\mu(N=3)$ on each pair of frayed blocks
spreads over many $\nu \vdash 6$:

$$
  V_\lambda \otimes V_\mu
  \;=\;
  \bigoplus_{\nu \vdash 6}
    c^\nu_{\lambda, \mu} \, V_\nu,
\qquad
  \lambda, \mu \in \{(3), (2,1), (1,1,1)\}.
$$

The combined Wedderburn support of $\Phi_6$ at $^{6}\mathrm{Li}$ is a
weighted sum of all such fusions, with weights determined by the
relative strengths of the three frayed components. The resulting
$\Phi_6$ has *non-zero off-diagonal full-twist flux vectors* — it is
not a fixed point of $\Delta_6^2$.

## Content of the diagram

The diagrammatic illustration in this example block is, schematically:

- **Left**: a *fragment of Young's lattice* between $(3)$, $(2,1)$,
  $(1,1,1)$ — a triangle with $(2,1)$ at the centre — marked
  "frayed, full-twist flux $\pm q^3$".
- **Right**: an identical copy on the $N$ side (since $Z = N = 3$).
- **Centre**: an LR-fusion *spread* — a wide arrow producing
  multiple $\nu \vdash 6$, with $c^\nu_{\lambda, \mu}$ printed at
  each target — marked "**non-rigid: multiple non-zero LR
  coefficients**".

Where the $^{40}\mathrm{Ca}$ diagram has a single arrow to a single
$\nu$, the $^{6}\mathrm{Li}$ diagram has a fan of arrows producing
the full Wedderburn spread.

## Loose binding of $^{6}\mathrm{Li}$

The empirical $^{6}\mathrm{Li}$ binding energy is $31.99$ MeV
($5.33$ MeV/nucleon) — far below the $8.55$ MeV/nucleon of
$^{40}\mathrm{Ca}$. The algebraic content: there are *many* off-
diagonal Wedderburn channels at $A = 6$ through which crossing
energy can leak, and the LR fusion of two frayed blocks produces a
spread of full-twist flux vectors that the deuteron-like topology
of $^{6}\mathrm{Li}$ cannot absorb without breakup.

Phenomenologically: $^{6}\mathrm{Li}$ has many available
binding-energy channels, all of them with non-zero capacity and
none of them shell-closed. The empirical loose binding is the
algebraic non-rigidity.

## Empirical contrast with the magic ladder

| Nuclide | $(Z, N)$ | Magic regime | $\Phi_n$ structure |
|--------:|:---------|:-------------|:-------------------|
| $^{6}\mathrm{Li}$  | $(3, 3)$    | non-magic both sides   | frayed both sides; LR spread |
| $^{16}\mathrm{O}$  | $(8, 8)$    | double-magic           | rigid both sides; single $\nu$ |
| $^{18}\mathrm{O}$  | $(8, 10)$   | single-magic ($Z$ only) | $Z$ rigid, $N$ frayed; $\kappa$-leakage |
| $^{40}\mathrm{Ca}$ | $(20, 20)$  | double-magic           | rigid both sides; single $\nu$ |

Reading the table top-to-bottom: as the regime moves from
non-magic to single-magic to double-magic, the LR-fusion
spread compresses to a single rigid $\nu_{ZN}$ — and the
binding-per-nucleon climbs from $5.3$ to $7.6$ to $8.6$ MeV. The
diagrammatic content of the LR-fusion conjecture is the algebraic
mechanism behind the magic-number step pattern in nuclear binding.
