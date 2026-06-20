*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Definition.**
*In the [atomic braid](#def:atomic-braid) $\mathcal{A}(Z, N)$, each
of the $Z$ electrons is a trefoil $T_{2,3}$ Hopf-linked to the
nuclear core.  The **shell capacity** of the atom is determined
by the electron arrangement that minimizes $\Phi_1$.*

*Each electron trefoil $T_{2,3} = \sigma_0\sigma_1\sigma_0$ in
$H_3(q)$ occupies a **bonding site**.  The maximum number of
bonding sites at shell level $n$ is conjecturally $2n^2$ — this is
the **open shell-capacity derivation** (the electron-shells-Hopf
shell conjecture, open problem 1), not yet established: the
photon-electron transfer matrix is $2\times2$, so its $n$-th power
fixes the shell *energies* (the Chebyshev/Rydberg ladder) but supplies
only a $2$-fold degeneracy, not the $2n^2 = 2\sum_{\ell=0}^{n-1}(2\ell+1)$
count, which would require an $\mathrm{SO}(4)$-type accidental
degeneracy bundling angular-momentum levels $\ell = 0,\ldots,n-1$ into
principal shell $n$:*

| Shell $n$ | Capacity $2n^2$ | Subshells |
|:----------|:---------------|:----------|
| 1 | 2 | 1s (2) |
| 2 | 8 | 2s (2) + 2p (6) |
| 3 | 18 | 3s (2) + 3p (6) + 3d (10) |

*An atom with $Z$ electrons fills shells in order of increasing
$\Phi_1$ contribution.  The **valence** (number of open bonding
sites available for covalent bonds) is:*

$$
  v(Z) = \min\bigl(Z_{\mathrm{val}},\; 2n_{\mathrm{val}}^2 - Z_{\mathrm{val}}\bigr)
$$

*where $Z_{\mathrm{val}}$ is the number of valence electrons
and $n_{\mathrm{val}}$ is the outermost shell level.*

| Atom | $Z$ | Config | $v(Z)$ | Open sites |
|:-----|:----|:-------|:-------|:-----------|
| H | 1 | $1s^1$ | 1 | 1 |
| C | 6 | $[He]\,2s^2 2p^2$ | 4 | 4 |
| N | 7 | $[He]\,2s^2 2p^3$ | 3 | 3 (+1 lone pair) |
| O | 8 | $[He]\,2s^2 2p^4$ | 2 | 2 (+2 lone pairs) |

*A **lone pair** is an electron pair whose $\Phi_1$ contribution
is lower when bound to a single nucleus than when shared.  The
LP dual assigns electrons to bonding vs lone-pair positions
by comparing the $\Phi_1$ cost of sharing vs retaining.*
