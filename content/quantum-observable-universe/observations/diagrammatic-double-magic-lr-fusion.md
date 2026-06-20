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

## Setup

Let $Z, N \in \mathbb{N}$ with $A = Z + N$. The atomic-knot framework
([prop:recursive-atom-knot-atlas](../appendix-knot-periodic-table/recursive-atom-knot-atlas.md))
constructs the nuclide knot $\mathfrak{H}(Z, N)$ as a fused product
of the $Z$-block (proton braid word at level $Z$) and the $N$-block
(neutron braid word at level $N$). On the Hecke side, fusion is the
Littlewood–Richardson product

$$
  V_\lambda(Z) \otimes V_\mu(N)
  \;\cong\;
  \bigoplus_{\nu \vdash A} c^\nu_{\lambda, \mu} V_\nu(A),
$$

with LR coefficients $c^\nu_{\lambda, \mu} \in \mathbb{Z}_{\geq 0}$
\cite{ariki1996, ram1991}. The Wedderburn-decomposition support of
the categorical mass at level $A$ is determined by which partitions
$\nu$ enter the fusion with non-zero coefficient.

The **content sum** is additive: $c(\nu) = c(\lambda) + c(\mu)$
along the LR fusion, so the full-twist eigenvalue at level $A$
is $q^{c(\lambda) + c(\mu)}$. When both $\lambda$ and $\mu$ are
self-conjugate ($\lambda = \lambda'$, $\mu = \mu'$, both with content
sum zero), the full-twist eigenvalue at the fused level $A$ is
$q^0 = 1$ — and the LR fusion is constrained to self-conjugate
$\nu = \nu'$.

## Statement

**Proposition (Conjecture — diagrammatic double-magic LR-fusion
rigidity).**
*Let $Z, N \in \mathfrak{M}$. By
[`prop:categorical-neutrality-saturated-shells`](../braids-and-knots/categorical-neutrality-saturated-shells.md)
the categorical mass at level $Z$ is supported on a single
self-conjugate partition $\lambda_Z \vdash Z$, and similarly $\Phi_N$
is supported on $\mu_N \vdash N$ with $\mu_N = \mu_N'$. Then the
LR-fusion at level $A = Z + N$ is **rigid**:*

$$
  V_{\lambda_Z} \otimes V_{\mu_N}
  \;\cong\;
  V_{\nu_{ZN}}(A)
$$

*for a uniquely determined self-conjugate $\nu_{ZN} \vdash A$ with
$\nu_{ZN} = \nu_{ZN}'$ and $c(\nu_{ZN}) = 0$. In particular, the
LR multiplicity is one:* $c^{\nu_{ZN}}_{\lambda_Z, \mu_N} = 1$
*and all other LR coefficients vanish.*

*Equivalently, $\sum_{x \in \nu_{ZN}} c(x) = 0$, and the categorical
mass at the double-magic level $A$ is supported on the single
self-conjugate Specht module $V_{\nu_{ZN}}$ — there is no off-
diagonal Wedderburn capacity to absorb crossing energy beyond the
Coulomb / Casimir / pairing terms already present at $\lambda_Z$
and $\mu_N$.*

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

## Discussion

**Conjectural** under AGENTS.md §3b. The conjecture is
*conditional* on
[`prop:categorical-neutrality-saturated-shells`](../braids-and-knots/categorical-neutrality-saturated-shells.md)
and
[`prop:homological-shell-condensation`](../lifting-and-descent/homological-shell-condensation.md).
A proof would proceed in two steps: (1) the upstream conjectures
force self-conjugate support of $\Phi_Z$ and $\Phi_N$; (2) a
self-conjugacy + content-sum LR rigidity lemma (provable Hecke
fragment) collapses the LR product to a single $\nu$.

Step 2 is plausibly provable in pure Hecke combinatorics; this is
deferred to Phase 2 of the algebraic refactor (see workplan in the
sibling branch).

The downstream cone is the double-magic prediction set — every
binding-energy claim at $\{^{132}\mathrm{Sn},
^{208}\mathrm{Pb}, \ldots\}$ derived by the conjecture is itself
conjectural until one of the upstream conjectures is closed.
