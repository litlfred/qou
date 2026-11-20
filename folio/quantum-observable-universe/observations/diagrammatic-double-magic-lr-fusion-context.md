This remark records the setup, mechanism, worked cases, higher-magic predictions, and proof outlook for [Conjecture (diagrammatic double-magic)](#conj:diagrammatic-double-magic-lr-fusion).

A nuclide is double-magic when its proton and neutron counts both fall in $\mathfrak{M} = \{2, 8, 20, 28, 50, 82, 126\}$. Canonical examples include $^4\mathrm{He}$, $^{16}\mathrm{O}$, $^{40}\mathrm{Ca}$, $^{48}\mathrm{Ca}$, $^{56}\mathrm{Ni}$, $^{132}\mathrm{Sn}$, and $^{208}\mathrm{Pb}$. The empirical signature is exceptional binding-energy stability: these nuclei occupy sharp local maxima on the binding-per-nucleon curve. The Littlewood-Richardson (LR) fusion of the two saturated $Z$- and $N$-blocks is rigid (a single self-conjugate Specht module on the diagonal) and permits no off-diagonal flux.

## Setup

Let $Z, N \in \mathbb{N}$ with $A = Z + N$. The atomic-knot framework ([prop:recursive-atom-knot-atlas](../appendix-knot-periodic-table/recursive-atom-knot-atlas.md)) constructs the nuclide knot $\mathfrak{H}(Z, N)$ as a fused product of the $Z$-block (proton braid word at level $Z$) and the $N$-block (neutron braid word at level $N$). On the Hecke side, fusion executes the LR product

$$
  V_\lambda(Z) \otimes V_\mu(N)
  \;\cong\;
  \bigoplus_{\nu \vdash A} c^\nu_{\lambda, \mu} V_\nu(A),
$$

with LR coefficients $c^\nu_{\lambda, \mu} \in \mathbb{Z}_{\geq 0}$ \cite{ariki1996, ram1991}. The Wedderburn-decomposition support of the categorical mass at level $A$ is determined by the partitions $\nu$ entering the fusion with non-zero coefficients.

The content sum is additive along the LR fusion: $c(\nu) = c(\lambda) + c(\mu)$. The full-twist eigenvalue at level $A$ is $q^{c(\lambda) + c(\mu)}$. When both $\lambda$ and $\mu$ are self-conjugate ($\lambda = \lambda'$, $\mu = \mu'$, carrying content sum zero), the full-twist eigenvalue at the fused level $A$ is $q^0 = 1$. The LR fusion is constrained to self-conjugate partitions $\nu = \nu'$.

## Meaning of "rigidity"

The classical LR rule \cite{ariki1996} generally produces a sum over many $\nu$, with multiplicities counting LR tableaux. The conjecture dictates that at double-magic levels, the sum collapses to a single term with unit multiplicity. Self-conjugacy ($\lambda = \lambda'$, $\mu = \mu'$) constrains the LR product to $\nu = \nu'$. The saturated-shell content-sum-zero condition ($c(\lambda) = c(\mu) = 0$) constrains $c(\nu) = 0$. Rigidity asserts that these two constraints combined leave at most one admissible $\nu$.

Physically, there is no Wedderburn block at the double-magic level capable of absorbing further binding energy through Hecke channels. Exceptional double-magic stability is the algebraic absence of decomposition channels, not a fitted shell-correction term.

## Examples

The illustration blocks [Single-magic illustration: $^{18}\mathrm{O}$ at $Z = 8$, $N = 10$](single-magic-O18-diagram.md), [Double-magic illustration](double-magic-Ca40-diagram.md), and [Non-magic illustration](non-magic-Li6-diagram.md) display the diagrammatic content of LR-fusion at the partition level for one representative case from each regime:

- $^{40}\mathrm{Ca}$ ($Z = N = 20$): both blocks are self-conjugate. LR fusion yields a single $\nu = \nu'$ with zero content sum (**rigid**).
- $^{18}\mathrm{O}$ ($Z = 8$, $N = 10$): the $Z$-block is self-conjugate (saturated), but $N = 10 \notin \mathfrak{M}$. The fusion is non-rigid. The $\kappa$-leakage from the $N$ side is the algebraic source of the binding tail beyond the saturated $Z = 8$ contribution.
- $^{6}\mathrm{Li}$ ($Z = N = 3$): neither block is saturated. Frobenius "arms" exceed Frobenius "legs" in both partitions. The fusion produces non-zero full-twist flux vectors, placing the binding curve far from a magic peak.

## Predictions for the higher-magic ladder

The combinatorial barrier at $k \geq 12$ prevents Hoefsmit matrix-evaluation for $\{50, 82, 126\}$. The LR-rigidity conjecture nonetheless predicts a uniquely determined $\nu_{ZN}$ at each double-magic candidate independent of matrix evaluations. Predicted targets in the higher-magic ladder include $^{132}\mathrm{Sn}$ ($Z = 50, N = 82$) and $^{208}\mathrm{Pb}$ ($Z = 82, N = 126$). At each target, the LR fusion is conjecturally rigid. The algebraic prediction of the binding-per-nucleon peak is a zero-parameter statement.

*The dominant component $V_{\lambda_A}$ in the LR decomposition need not be self-conjugate. Empirical Yamanouchi enumeration ([`lr_fusion_self_conj_test.py`](../../../computations/lr_fusion_self_conj_test.py)) finds the dominant $\nu$ is non-self-conjugate at every tested $(Z, N)$. The criterion is content additivity on the LR-fusion, not self-conjugacy of the dominant component.*

## Discussion

This conjecture is conditional on [Categorical neutrality of saturated shells](../mass-endomorphism/categorical-neutrality-saturated-shells.md) and [Proposition (homological shell condensation)](../mass-endomorphism/homological-shell-condensation.md). A proof proceeds in two steps: (1) the upstream conjectures force self-conjugate support of $\Phi_Z$ and $\Phi_N$; (2) a self-conjugacy and content-sum LR rigidity lemma (provable Hecke fragment) collapses the LR product to a single $\nu$.

Step 2 is plausibly provable in pure Hecke combinatorics. It is not attempted here.

The downstream consequence is the double-magic prediction set. Every binding-energy claim for $\{^{132}\mathrm{Sn}, ^{208}\mathrm{Pb}, \ldots\}$ remains conjectural until the upstream conjectures are closed.
