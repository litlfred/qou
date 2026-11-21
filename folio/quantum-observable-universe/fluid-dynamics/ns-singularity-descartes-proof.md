*Proof.*
Item 1: by [QU-to-QOU](#thm:qu-to-qou), item 2, $e(\xi) = c_1(\xi) = \chi(\mathcal{S}) = -6$ for the unit tangent bundle. A nowhere-vanishing section would trivialise $\xi$ and force $e(\xi) = 0$.

Item 2: by [QU-to-QOU](#thm:qu-to-qou), item 3, $\xi$ has an $n$-th root if and only if $n \mid \chi(\mathcal{S}) = -6$, with obstruction $-6 \bmod n$; see also the [Kummer specialisation](#prop:ns-kummer-specialisation). The positive divisors of $6$ are $1, 2, 3, 6$.

Item 3: $\Sigma$ has dimension $1$, so $H^2(\Sigma, M) = 0$ for every coefficient group $M$ (Godement II.5.12).

*Retracted argument.* Earlier versions of this theorem asserted that the Descartes universe is NS-singular, $\mathrm{NS}(A) = e(\xi)|_\Sigma \neq 0$. They argued in four steps:
1. Kummer survival of $\kappa_0 \bmod 2\kappa$ for $\kappa \geq 4$;
2. a complementary-subgroup non-cancellation between $\kappa_0|_\Sigma$ and the jet corrections $\delta_n|_\Sigma$ (item 3 of QU-to-QOU in its jet-tower form);
3. non-degeneracy of the Levi form via the [core-Levi equivalence](#prop:core-levi-form) (withdrawn, see below);
4. the [vorticity lower bound](#conj:vorticity-lower-bound) and [BKM divergence](#thm:q-bkm).

Step 1 survives as item 2 above, but it is a statement about the global class on $\mathcal{S}$. Step 2 fails: the jet-tower form of item 3 is retracted, the corrections $\delta_n$ lie in the image of $H^2(\mathcal{S}, \mathcal{O}_{\mathcal{S}}) = 0$, and $e(\xi)|_\Sigma = 0$ by item 3 above. Step 3 is withdrawn: the [core-Levi form](#prop:core-levi-form) now gives a single Levi scalar $\xi\cdot\mathrm{curl}\,\xi$, and the implication "non-degenerate Levi data, hence blow-up" (branch (A) of the [Levi degeneracy conjecture](#conj:levi-degeneracy)) is refuted by an explicit Beltrami solution. Step 4 remains valid as a conditional implication from a non-vanishing obstruction on $\Sigma$, but no such class exists on a one-dimensional $\Sigma$. Whether the model's actual Reeb field vanishes on $\Sigma$ is a dynamical question, which this theorem does not address.
