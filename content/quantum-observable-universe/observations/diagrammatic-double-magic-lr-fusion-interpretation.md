A nuclide is **double-magic** when both its proton and neutron counts
lie in $\mathfrak{M} = \{2, 8, 20, 28, 50, 82, 126\}$ — the
canonical examples being $^4\mathrm{He}$, $^{16}\mathrm{O}$,
$^{40}\mathrm{Ca}$, $^{48}\mathrm{Ca}$, $^{56}\mathrm{Ni}$,
$^{132}\mathrm{Sn}$, $^{208}\mathrm{Pb}$. The empirical signature is
exceptional binding-energy stability — these nuclei sit at sharp
local maxima of the binding-per-nucleon curve. This block names the
algebraic content of double-magicity directly: the LR-fusion of the
two saturated $Z$- and $N$-blocks is *rigid* — a single
self-conjugate Specht module on the diagonal — with no off-diagonal
flux.

## Why "rigidity"

The classical LR rule \cite{ariki1996} typically produces a sum
over many $\nu$, with multiplicities counting LR tableaux. The
conjecture says that at double-magic levels the sum collapses to a
single term with multiplicity one. Self-conjugacy
($\lambda = \lambda'$, $\mu = \mu'$) constrains the LR product to
$\nu = \nu'$, and the saturated-shell content-sum-zero condition
($c(\lambda) = c(\mu) = 0$) constrains $c(\nu) = 0$. The rigidity
asserts that these two constraints combined leave at most one
$\nu$ admissible.

The empirical content is direct: there is **no Wedderburn block** at
the double-magic level capable of absorbing further binding energy
through Hecke channels. The exceptional double-magic stability is
the algebraic absence of decomposition channels, not a fitted
shell-correction term.

## Examples

The illustration blocks
[`ex:single-magic-O18-diagram`](single-magic-O18-diagram.md),
[`ex:double-magic-Ca40-diagram`](double-magic-Ca40-diagram.md), and
[`ex:non-magic-Li6-diagram`](non-magic-Li6-diagram.md) show the
diagrammatic content of LR-fusion on the partition level for one
representative case from each regime:

- $^{40}\mathrm{Ca}$ ($Z = N = 20$): both blocks self-conjugate, LR
  fuses to a single $\nu = \nu'$ with content sum zero —
  **rigid**.
- $^{18}\mathrm{O}$ ($Z = 8$, $N = 10$): the $Z$-block is
  self-conjugate (saturated), but $N = 10 \notin \mathfrak{M}$ —
  the fusion is non-rigid, and $\kappa$-leakage from the $N$ side
  is the algebraic source of the $^{18}\mathrm{O}$ binding tail
  beyond the saturated $Z = 8$ contribution.
- $^{6}\mathrm{Li}$ ($Z = N = 3$): neither block is saturated;
  Frobenius "arms" exceed Frobenius "legs" in both partitions, so
  the fusion produces non-zero full-twist flux vectors and the
  binding curve is far from a magic peak.

## Predictions for the higher-magic ladder

The combinatorial barrier at $k \geq 12$ blocks Hoefsmit
matrix-evaluation for $\{50, 82, 126\}$, but the LR-rigidity
conjecture predicts a uniquely determined $\nu_{ZN}$ at each
double-magic candidate independent of matrices. The predicted
double-magic targets in the higher-magic ladder include
$^{132}\mathrm{Sn}$ ($Z = 50, N = 82$) and $^{208}\mathrm{Pb}$
($Z = 82, N = 126$); for each the LR fusion is conjecturally rigid
and the algebraic prediction of the binding-per-nucleon peak is a
**zero-parameter** statement.

*The dominant component $V_{\lambda_A}$ in the LR decomposition need
**not** itself be self-conjugate — empirical Yamanouchi enumeration
([`lr_fusion_self_conj_test.py`](https://github.com/litlfred/qou/blob/claude/qou-algebraic-refactor-1qVFc/computations/lr_fusion_self_conj_test.py))
finds the dominant $\nu$ is non-self-conjugate at every tested
$(Z, N)$. The criterion is **content additivity** on the LR-fusion,
not self-conjugacy of the dominant component.*
