*Proof.*
The [NS obstruction](#def:ns-obstruction) is
$\mathrm{NS}(A) = \kappa_0|_\Sigma$ where
$\mathrm{tr}(\kappa_0) = \chi(A) = -6$.

**Step 1** (arithmetic).
For $\kappa \geq 4$, $2\kappa \geq 8 > 6 = |\chi(A)|$, so
$2\kappa \nmid -6$.  By the
[Kummer specialisation](#prop:ns-kummer-specialisation),
$\kappa_0 \bmod 2\kappa \neq 0$ for all $\kappa \geq 4$.  The
obstruction survives through infinitely many levels of the
Kummer tower.

**Step 2** (algebra).
The [perpetual obstruction](#thm:qu-to-qou) (item 3) says
$\kappa_0$ and the jet corrections $\delta_n$ live in
complementary subgroups of $H^2(\mathcal{S}, \mathcal{B})$.
The total obstruction $\kappa_n|_\Sigma = \kappa_0|_\Sigma +
\delta_n|_\Sigma$ is nonzero because the topological term
$\kappa_0|_\Sigma \neq 0$ cannot be cancelled by the analytic
term $\delta_n|_\Sigma$.

*Scope of Step 2.* It inherits item 3 of [QU-to-QOU](#thm:qu-to-qou) in its earlier, jet-tower form, which is retracted. Item 3 now states persistence in the Kummer tower (the obstruction $\chi(\mathcal{S}) \bmod n$ to an $n$-th root of the Reeb bundle), not at every level of the jet tower. For the bands used in this corpus the complementary-subgroup step is not established on a closed surface such as Bring's. There $H^2(\mathcal{S}, \mathcal{O}_{\mathcal{S}}) = 0$, so the jet corrections $\delta_n$ vanish. For the band $\mathbb{Z}$, the group $H^2(\mathcal{S}, \mathbb{Z}) \cong \mathbb{Z}$ has no non-trivial complement. For $\mathcal{O}^{\times}$ and $\mathbb{G}_m$, the obstruction group itself is zero. See the scope note in the [proof of QU-to-QOU](#prf:qu-to-qou).

**Step 3** (geometry).
$\mathrm{NS}(A) \neq 0$ implies, via the
[core-Levi equivalence](#prop:core-levi-form), that the
Levi form stays non-degenerate at the collision locus: the
contact structure does not degenerate.

**Step 4** (dynamics).
Non-degenerate Levi form implies bounded core aspect ratio,
which gives the [vorticity lower
bound](#prop:vorticity-lower-bound)
$\|\omega\|_\infty \geq c/(T^*-t)$, which gives
[BKM divergence](#thm:q-bkm) $\int \|\omega\|_\infty \, dt = \infty$.
