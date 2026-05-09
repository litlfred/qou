**Definition.**
*The **atomic braid** of a neutral atom $(Z, N)$ is the element of
$H_{A+Z}(q)$ obtained by assembling $Z$ protons, $N$ neutrons,
and $Z$ electrons into a single Hecke algebra with $A + Z$ strands,
where $A = Z + N$.  The crossing coefficients are:*

| Pair                       | Crossing                             | $c$ | $d$             | Origin                 |
| :------------------------- | :----------------------------------- | :-- | :-------------- | :--------------------- |
| $\mathfrak{p}\mathfrak{p}$ | $\sigma$                             | $1$ | $0$             | strong repulsion       |
| $\mathfrak{n}\mathfrak{n}$ | $\sigma^{-1}$                        | $1$ | $-(q - q^{-1})$ | strong inverse         |
| $\mathfrak{p}\mathfrak{n}$ | $\tfrac{1}{2}(\sigma + \sigma^{-1})$ | $2$ | $-(q - q^{-1})$ | strong mixed (doubled) |
| $\mathfrak{p}e$            | $\sigma^{-1}$                        | $1$ | $-(q - q^{-1})$ | EM attraction          |
| $\mathfrak{n}e$            | $\mathrm{id}$                        | $0$ | $1$             | no interaction         |
| $ee$                       | $\sigma$                             | $1$ | $0$             | EM repulsion           |

*The **ground-state ordering** is determined by:*

1. *Nuclear ordering: minimize $\Phi_1$ over all permutations of
   $Z$ protons and $N$ neutrons (exact search for
   $\binom{A}{Z} \leq 50000$, steepest :refterm[descent]{#descent} otherwise).*
2. *Electron insertion: greedily insert each of $Z$ electrons at
   the position minimizing $\Phi_1$.*

*The greedy insertion produces **ep pairs**: each electron sits
immediately before its proton.  The $\mathfrak{n}e = \mathrm{id}$
crossing means electrons pass through neutrons without generating
Hecke generators.*

*For hydrogen ($A = 1$): the bare $[e, \mathfrak{p}]$ braid is
LP-unstable (Proposition \ref{prop:atomic-lp-stability}).  The
$\mathfrak{p}e$ crossing uses the $\mathcal{B}_3$-dressed eigenvalues
$(q^5, -q^{-5})$ instead of bare $(q^{-1}, -q)$.*
