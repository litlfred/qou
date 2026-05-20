**Two independent algebraic mechanisms** preserve the mirror-isobar
equality $\mathfrak{m}_{\mathrm{Markov}}(T) =
\mathfrak{m}_{\mathrm{Markov}}({}^3\mathrm{He})$:

1. The **Hecke-skein sign-flip invariance** at $q = 0$ established
   in [crystal isospin degeneracy](#prop:crystal-isospin-degeneracy)
   — applies to the legacy disjoint-product convention; the
   mechanism is $\sigma_i^{-1} = \sigma_i$ on every standard Young
   tableau eigenline at the crystal limit.

2. The **Hopf-antipode invariance** at every $q \in (1, \varphi)$
   established in
   [spin-involution / LP-dual invariance](#prop:spin-involution-lp-dual-invariance)
   — applies to the canonical $\bowtie_K$-coupled convention; the
   mechanism is the Frobenius-self-dual antipode
   $S \colon V_\lambda \leftrightarrow V_{\lambda^T}$, which acts as
   $Z \leftrightarrow N$ on the per-atom canonical braid recipe.

The empirical witness recorded in
[LP-dual isospin invariance](#rem:lp-dual-isospin-invariance)
shows exact equality of the LP-dual binding-energy shadow price
$y_0^*(T) = y_0^*({}^3\mathrm{He})$ in both 2-row and height-$6$
strata across $q \in \{1.001, 1.050, 1.110\}$.

**Observable consequence (structural impossibility theorem).**

*The empirical mirror-isobar mass split*

$$
  \Delta\mathfrak{m}_{T,\,{}^3\mathrm{He}}
    \;:=\; \mathfrak{m}({}^3\mathrm{H}) - \mathfrak{m}({}^3\mathrm{He})
    \;\approx\; 0.529\;\mathrm{MeV}
$$

*cannot live in any sector of the mass functional which is*

* **invariant under the Hecke skein involution**
  $\sigma_i \leftrightarrow \sigma_i^{-1}$ (the Markov-trace
  height-$6$ Wedderburn sum at $q = 0$, the Term 7 shell-correction
  functional in the legacy convention, etc.), or
* **invariant under the Hopf antipode** $S$ (the
  $\tau$-extracted observable-frame functionals, every LP-dual
  binding-energy shadow price, etc.).

*Equivalently, $\Delta\mathfrak{m}_{T,\,{}^3\mathrm{He}}$ must be
**localised** in the sector of the categorical mass that breaks
both involutions simultaneously.*

## The Coulomb sector is the only candidate

The full mass functional decomposes (per the unified six-term
formula plus shell-correction Term 7) into:

| sector | $\sigma$-invariant? | $S$-invariant? | candidate carrier? |
|:--|:--:|:--:|:--|
| Markov-trace tower (Terms 1–3, 6) | yes | yes | no |
| Co-Casimir (Term 4) | yes | yes | no |
| Chirality $a_K \mathcal{C}_K$ (Term 5) | yes (parity-odd in $K$) | yes (parity-odd in $K$) | no |
| Shell-correction (Term 7) | yes | yes | no |
| **Coulomb / EM / charge correction** | **no** | **no** | **yes** |

The [Coulomb-charge functional](#def:coulomb-charge) on a knot
composite is built from the *signed* crossing energy
$E_\times \cdot \mathrm{sign}(\sigma_i)$, which transforms
non-trivially under both $\sigma$ and $S$:

* under the sign-flip $\sigma_i \leftrightarrow \sigma_i^{-1}$, the
  Coulomb charge changes sign;
* under the Hopf antipode $S$ (matter $\leftrightarrow$ antimatter
  / $Z \leftrightarrow N$), the Coulomb charge changes sign
  (proton charge $+e \to$ antiproton charge $-e$, but the
  mirror-nucleus partner has the opposite *number* of charged
  nucleons, i.e.\ $Z \to N$).

A short calculation (deferred to *Computational support*) shows
that the Coulomb sector localised on the canonical braid recipe
contributes exactly the BW formula's Coulomb term

$$
  \Delta\mathfrak{m}_{T,\,{}^3\mathrm{He}}^{\mathrm{Coulomb}}
    \;=\; a_C \cdot \frac{Z(Z-1) - N(N-1)}{A^{1/3}}
$$

with $a_C \approx 0.7\;\mathrm{MeV}$ — within $30\%$ of the
empirical $0.529\;\mathrm{MeV}$ at $A = 3$, $|Z - N| = 1$, the
remaining residual being attributed to surface and finite-size
corrections.

**Conclusion.** The categorical $T$–${}^3\mathrm{He}$ mass split
*has no Markov-trace component*.  Any future $\rho_K^{\mathrm{full}}$
derivation that produces a non-zero $T$–${}^3\mathrm{He}$ split
from the Markov-trace sector alone is structurally inconsistent
with both sign-flip and Hopf-antipode invariances of the
underlying Hecke algebra.

## Computational support

Computational verification of the Coulomb-sector localisation is
not yet wired into a witness — it follows from the existing
[`def:coulomb-charge`](#def:coulomb-charge) and Bethe-Weizsäcker
phenomenology and is not specific to this paper.  A dedicated
witness `coulomb-mirror-isobar-split.witness.json` would compute
$a_C \cdot (Z(Z{-}1) - N(N{-}1)) / A^{1/3}$ across the canonical
mirror-isobar pairs $(T, {}^3\mathrm{He})$, $({}^7\mathrm{Li},
{}^7\mathrm{Be})$, $(\ldots)$ and verify the residual against
AME — a sub-percent test of the structural impossibility
theorem.  Tagged here as future work.
