**Remark (what the involution argument localises, and what it does not).**
*The empirical mirror-isobar mass split $\mathfrak{m}({}^3\mathrm{H}) - \mathfrak{m}({}^3\mathrm{He}) \approx 0.530\;\mathrm{MeV}$ breaks both Hecke-skein sign-flip invariance and Hopf-antipode invariance. Every sector of the mass functional that respects those involutions therefore contributes nothing to it. This constraint is weaker than a localisation onto the Coulomb term.*

A functional invariant under an involution contributes exactly zero to the split across it, and a sum of such sectors splits exactly like its remainder (`QOU.MassTheory.InvolutionSelectionRule`). The rule consumes an enumeration: that the sectors listed are all of them, and that each is invariant. Omitting one non-invariant sector makes the conclusion false rather than weaker.

Sector by sector, one entry of that enumeration fails. The unified mass formula ([`thm:knot-mass-formula-unified`](knot-mass-formula-unified.md)) carries three terms — descended trace, brane tower, Frobenius co-Casimir — and the four sectors named above overlap them only partly; the brane tower is missing from the list, though invariance holds for it anyway.

| sector | status under generator sign-flip |
|---|---|
| Frobenius co-Casimir | **invariant**, by arity: $\tau(C_{\dim_q}) = \sum_\lambda 1/\dim_q(\lambda)$ takes no braid word at all, so it factors through $(n, q)$ (`QOU.MassTheory.InvolutionSelectionRule.coCasimir_sector_contributes_zero`) |
| descended trace | **not invariant** at the substrate — see below |
| brane tower | **invariant** — its trace-invariant form takes no braid word either (`QOU.Mass.BraneTowerIsospinBlind.braneTowerR_eq_binom_sum`); the general form is invariant once the per-subset weight is Markov-invariant (`braneTowerW_isospin_blind`). Absent from the list above, but benignly so |
| shell correction | invariant in the **crystal limit** $q \to 0$ only ([`prop:crystal-isospin-degeneracy`](crystal-isospin-degeneracy.md)) |
| chirality | **breaks both involutions**: it is the unique S-odd term ([`frobenius-s-classification`](frobenius-s-classification.md), `chirality_is_unique_S_odd`), and its factor reads the crossing signs directly, $\prod_c (1 + \mathrm{sign}(c)\,h)$ with $h = q - q^{-1}$ ([`prop:chirality-dual-space-derivation`](chirality-dual-space-derivation.md)). It does not *itself* source this split, though: ${}^3\mathrm{H}$ and ${}^3\mathrm{He}$ carry the same crossing multiset (one positive, one negative), so both get the same factor $1 - h^2$ |

Two of the four named sectors therefore fail the premise, not one. The descended trace is the entry the argument can least afford to lose, and it fails outright. The Hecke relation gives $\sigma^{-1} = \sigma - (q - q^{-1})$, so a generator flip moves the trace by $(q - q^{-1})\,\mathrm{tr}(1)$ — about $0.209\,\mathrm{tr}(1)$ at $q_0$ — which vanishes only where $q^2 = 1$, the symmetric-braiding locus the framework sits off (`QOU.MassTheory.TraceSignFlipRegime`). A $q \to 0$ invariance does not transfer to $q_0$.

The split is also not Coulomb-dominated. Writing it as the free-nucleon term minus the binding difference,

$$
\mathfrak{m}({}^3\mathrm{H}) - \mathfrak{m}({}^3\mathrm{He}) = (\mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}}) - \bigl(B({}^3\mathrm{H}) - B({}^3\mathrm{He})\bigr) \approx 1.293 - 0.764 \approx 0.530\;\mathrm{MeV},
$$

the Coulomb-driven binding difference enters with the opposite sign to the split, at $1.44$ times its magnitude; the free-nucleon difference enters at $2.44$ times. Acting alone, the Coulomb term gives the wrong sign.

The surviving statement is the italic one: the split lives outside the involution-invariant sector. That sector's complement holds both the nuclear Coulomb term and $\mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}}$, and the second dominates. The intra-nucleon electromagnetic self-energy is carried in the free-nucleon masses rather than in the binding difference, so this split requires a quantity the framework does not yet derive.
