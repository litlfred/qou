Model a knot composite as a positive-crossing count $n_+$, a negative-crossing count $n_-$, and the value $q$ — the structure `KnotComposite`. The mirror operation $\sigma$ producing the antihadron is by definition the swap
$$
  \mathfrak{H}^{\sigma}: \quad (n_+, n_-, q) \longmapsto (n_-, n_+, q),
$$
i.e. `KnotComposite.mirror` — this is claim 1 (reversing every crossing sign interchanges the positive/negative tallies). Claims 2–4 are then computations.

**Claim 2 (crossing-energy bar-reversal).** With $+q$ per positive crossing and $-q^{-1}$ per negative crossing,
$\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) = n_+ q - n_- q^{-1}$, and its bar-involution ($q \leftrightarrow q^{-1}$) is $n_+ q^{-1} - n_- q$. Applying $\mathfrak{E}_{\mathrm{cross}}$ to the mirror swaps $n_+, n_-$:
$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}^{\sigma}) = n_- q - n_+ q^{-1}
  = -\bigl(n_+ q^{-1} - n_- q\bigr)
  = -\,\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})\big|_{q\leftrightarrow q^{-1}},
$$
so a positive crossing $(+q)$ becomes a negative crossing $(-q^{-1})$ and vice versa — the field identity `crossing_energy_bar_reversal` (by `ring`).

**Claim 3 (Coulomb charge reversal).** The antisymmetric component is $Q(\mathfrak{H}) = \tfrac12 (n_+ - n_-)(q - q^{-1})$. The mirror negates $(n_+ - n_-)$ and fixes $(q - q^{-1})$, so $Q(\mathfrak{H}^{\sigma}) = -Q(\mathfrak{H})$ (`coulomb_reversal`); for the proton $Q(\mathfrak{p}) = +1$ this gives the antiproton $Q(\mathfrak{p}^{\sigma}) = -1$.

**Claim 4 (bare-mass invariance).** The bare mass depends only on knot type (total crossing number, hyperbolic volume), not on individual orientations. The mirror permutes the tallies, preserving the total: $n_+(\mathfrak{H}^{\sigma}) + n_-(\mathfrak{H}^{\sigma}) = n_- + n_+$, so $\mathfrak{H}$ and $\mathfrak{H}^{\sigma}$ share the same volume and bare mass (`bare_mass_invariance`, by `omega`).

Bundling the three gives the proposition, formalized sorry-free as `antiparticle_crossing_reversal` = $\langle$`crossing_energy_bar_reversal`, `coulomb_reversal`, `bare_mass_invariance`$\rangle$. $\qquad\blacksquare$
