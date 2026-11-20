One lifts the Kummer-tower perpetuity result ([Kummer tower](#rem:kummer-tower)) to a single algebraic statement at the level of the [motivic Galois character](#def:motivic-galois-character).

**Theorem (motivic perpetual obstruction)** (proved via Route A: prime-ideal collapse, $C = a_0(-1) + 2 \cdot a_1(-1)$).
Let $A$ be a Frobenius–Hopf substrate with motivic class $[A] \in \widehat{\mathcal{M}}$ and motivic Galois character $\chi^{\mathrm{mot}}_A$. If $\chi(A) \neq 0$, then $\chi^{\mathrm{mot}}_A$ is non-trivial at every finite place $p$ of $\mathbb{Q}$ with $p \nmid \chi(A)$. Equivalently, the local Frobenius character $\chi^{\mathrm{mot}}_{A, p}$ has a non-trivial element in
$$
  H^1_{\mathrm{Gal}}\!\bigl(\mathrm{Gal}(\bar{\mathbb{Q}}_p/\mathbb{Q}_p),\, \mu_n(1)\bigr)
$$
for every $n$ coprime to $p\,\chi(A)$. The obstruction $\kappa_0$ projects to a non-trivial Frobenius character at every such place.

**Sketch.**
One applies [QU-to-QOU](#thm:qu-to-qou) to identify $\kappa_0$ with the Euler class $e(\xi)$ of the Reeb bundle, satisfying $\langle e(\xi), [M_0] \rangle = \chi_{\mathrm{eu}}(M_0)$ (Poincaré–Hopf). Under the realization $\rho_p \colon \widehat{\mathcal{M}} \to \mathbb{Z}[q]/\Phi_{p^k}(q)$ ([motivic substrate](#def:motivic-substrate)), the Euler class projects to a Frobenius character whose trace equals $\chi_{\mathrm{eu}}(M_0) \bmod p$. Because $p \nmid \chi(A)$, this trace is non-zero modulo $p$. The character is non-trivial. The class $\kappa_0$ retains a non-trivial Galois-cohomological component at every such place. By [Hochschild–Kummer](#rem:hochschild-kummer-connection), gerbe non-vanishing in $H^2(\mathcal{S}, \mathbb{G}_m)$ and Galois non-vanishing in $H^1_{\mathrm{Gal}}(\dots, \mu_n(1))$ are HKR-equivalent.
$\square$

**Subsumption of prior arguments.**
This theorem subsumes every prior argument for the non-vanishing of $\kappa_n$ at the Kummer levels $n \nmid \chi(A)$; it does not give non-vanishing at every level, and at $n \mid \chi(A)$ the obstruction vanishes (item 3 of [QU-to-QOU](#thm:qu-to-qou)). In particular:
- [The Kummer tower and persistence of the obstruction](#rem:kummer-tower) summary item 6
- [Bring's surface and $q$-flatness obstructions](#ex:archimedean-yekutieli) "Motivic-Galois reading"
- [$\chi_{\mathrm{eu}}(M_0) = -6$: the derivation chain](#ex:chi-minus-six-derivation) Step 8
- [The Hochschild--Kummer connection](#rem:hochschild-kummer-connection) "Motivic-Galois interpretation"
These all reduce to corollaries of this motivic perpetual obstruction.
