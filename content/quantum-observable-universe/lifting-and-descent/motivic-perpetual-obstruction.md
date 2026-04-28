The Kummer-tower perpetuity result
([Kummer tower](#rem:kummer-tower)) — the obstruction $\kappa_0$
persists at every level $n \nmid \chi(A)$ — lifts cleanly to a single
algebraic statement at the level of the
[motivic Galois character](#def:motivic-galois-character).

**Lemma (motivic perpetual obstruction).**
*Let $A$ be a Frobenius–Hopf substrate with motivic class
$[A] \in \widehat{\mathcal{M}}$ and let $\chi^{\mathrm{mot}}_A$ be its
motivic Galois character. If $\chi(A) \neq 0$ then
$\chi^{\mathrm{mot}}_A$ is non-trivial at every finite place
$p$ of $\mathbb{Q}$ with $p \nmid \chi(A)$ — equivalently, the
local Frobenius character $\chi^{\mathrm{mot}}_{A, p}$ has a
non-trivial element in*

$$
  H^1_{\mathrm{Gal}}\!\bigl(\mathrm{Gal}(\bar{\mathbb{Q}}_p/\mathbb{Q}_p),\, \mu_n(1)\bigr)
$$

*for every $n$ coprime to $p\,\chi(A)$. Equivalently still, the
Yekutieli obstruction $\kappa_0$ projects to a non-trivial Frobenius
character at every such place.*

**Proof sketch.**
*Apply [QU-to-QOU](#thm:qu-to-qou) to identify $\kappa_0$ with the
Euler class $e(\xi)$ of the Reeb bundle, satisfying
$\mathrm{tr}(\kappa_0) = \chi(A)$. Under the realization
$\rho_p \colon \widehat{\mathcal{M}} \to \mathbb{Z}[q]/\Phi_{p^k}(q)$
([motivic substrate](#def:motivic-substrate)), the Euler class
projects to a Frobenius character whose trace equals $\chi(A) \bmod p$.
Since $p \nmid \chi(A)$, this trace is non-zero modulo $p$, so the
character is non-trivial. The class $\kappa_0$ therefore retains a
non-trivial Galois-cohomological component at every such place, by
[Hochschild–Kummer](#rem:hochschild-kummer-connection): gerbe
non-vanishing in $H^2(\mathcal{S}, \mathbb{G}_m)$ and Galois
non-vanishing in $H^1_{\mathrm{Gal}}(\dots, \mu_n(1))$ are HKR-equivalent.*

$\square$

**Consequence (paper-wide).**
*Every block in the paper that previously argued non-vanishing of
$\kappa_n$ "at every level $n$ in the brane tower" by analytic /
topological means can be cited as a corollary of this lemma. In
particular:*

- [`rem:kummer-tower`](#rem:kummer-tower) summary item 6
- [`ex:descartes-yekutieli`](#ex:descartes-yekutieli) "Motivic-Galois reading"
- [`ex:chi-minus-six-derivation`](#ex:chi-minus-six-derivation) Step 8
- [`rem:hochschild-kummer-connection`](#rem:hochschild-kummer-connection) "Motivic-Galois interpretation"

*all reduce to corollaries of [motivic perpetual obstruction](#lem:motivic-perpetual-obstruction).*
