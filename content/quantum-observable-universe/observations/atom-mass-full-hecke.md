The simple CODATA-recombination mass formula $M_q = Z\mathfrak{m}_{\mathfrak{p}} + N\mathfrak{m}_{\mathfrak{n}} + Z\mathfrak{m}_e - (Z+N)\,B/A$ uses only the 2$\times$2 **standard** irrep of $H_3(q)$ for the transfer matrix chain. Per-atom knot identifications are collected in the recursive knot$\to$particle dictionary ([recursive-atom-knot-atlas](#prop:recursive-atom-knot-atlas)). This projects the Hecke element onto the $(2,1)$-seminormal representation and discards the symmetric (trivial) and alternating (sign) channels. For multi-nucleon systems, this projection throws away the dominant contribution. The standard channel trace $\mathrm{tr}_{\mathrm{std}}$ decays exponentially with $A$, while $\mathrm{tr}_{\mathrm{sym}}$ and $\mathrm{tr}_{\mathrm{alt}}$ remain $O(1)$.

We compute the atomic mass for $Z = 1$ through $Z = 10$ using the full regular representation of $H_3(q)$. We track all three irreducible channels independently.

## Three-channel decomposition

See [Table: Three-channel $H_3(q)$ decomposition](#tbl:atom-mass-full-hecke-table-data).

The full Markov trace decomposes over the three Wedderburn blocks of $H_3(q)$ as

$$
  \mathrm{tr}_M^{\mathrm{full}}
  = \hat y_{\mathrm{sym}}\,\mathrm{tr}_{\mathrm{sym}}
  + \hat y_{\mathrm{std}}\,\mathrm{tr}_{\mathrm{std}}
  + \hat y_{\mathrm{alt}}\,\mathrm{tr}_{\mathrm{alt}},
$$

where $\hat y_\lambda = y_\lambda(q)\,d_\lambda$ are the $q$-deformed Jones--Markov weights. These weights are the Wenzl Schur principal specialisation of the canonical $y_\lambda$ ([Wenzl-bridge closed form](#prop:y-lambda-closed-form-wenzl-bridge)), normalised by $\sum_\lambda \hat y_\lambda = 1$. The production Markov-trace uses these weights throughout. The classical Wedderburn--Artin values $d_\lambda^2 / |S_3| = \{\tfrac16, \tfrac23, \tfrac16\}$ are only their $q \to 1$ limit. At the substrate scale, this deformation is large. From the cached weights, $\hat y_{\mathrm{sym}} \approx 0.42$, $\hat y_{\mathrm{std}} \approx 0.56$, and $\hat y_{\mathrm{alt}} \approx 0.02$. The symmetric weight rises by roughly $2.5\times$ and the alternating weight falls by roughly $7\times$ relative to the classical equal-weighting.

For a single nucleon ($A = 1$), this three-channel sum equals the full $H_3(q)$ Markov trace. For $A > 1$, it acts as a three-channel $H_3$ projection of the multi-nucleon state, not the full $H_{3A}(q)$ Markov trace. The two coincide only at $A = 1$. The columns below model this projection rather than the canonical $H_{3A}$ trace.

## Mass decomposition (fibre / horizontal / mixed)

For each nucleus, the mass integrand ([Hecke mass element](#def:hecke-mass-element)) splits along the charge--mass duality ([charge--mass duality](#rem:hecke-charge-mass-duality)):

1. **Horizontal** (crossing energy):
   $\mathfrak{E}_{\mathrm{cross}} = n_+ q - n_- q^{-1}$,
   where $n_+$ counts proton--proton pairs and $n_-$ counts neutron--neutron pairs.

2. **Vertical / fibre** (Markov trace mass):
   $\mathfrak{m}_{\mathrm{vert}} = \mathrm{tr}_M^{\mathrm{full}}(\Phi_{\mathrm{mass}})$.

3. **Mixed** (vertex operator coupling):
   $\mathfrak{m}_{\mathrm{mix}} = \mathfrak{E}_{\mathrm{cross}} \cdot (q - 1)^2$.

## Results for $Z = 1$--$10$

We evaluate the per-channel traces $\mathrm{tr}_{\mathrm{sym}}, \mathrm{tr}_{\mathrm{std}}, \mathrm{tr}_{\mathrm{alt}}$ below at $q = 111/100$. This is a convenient rational near the substrate $q_0 \approx 1.10998$, allowing exact arithmetic. Binding energy comes from the Skein binding Lagrangian ([Skein binding Lagrangian](#def:skein-binding-lagrangian)) with $q$-derived Bethe--Weizsäcker coefficients.

See [Table](#tbl:atom-mass-full-hecke-table-data).

**Note (weighting convention).** The $\mathrm{tr}_{\mathrm{full}}$ column of the table uses the canonical $q$-deformed weights $\hat y_\lambda$ above (witness `atom-mass-full-hecke.witness.json`). The $q \to 1$ classical weighting gives materially different values (for ${}^4\mathrm{He}$, $\mathrm{tr}_{\mathrm{full}} = 0.516$ q-deformed vs $0.422$ classical). The $B/A$ and $\Delta$ columns are independent of this weighting. They derive from the Skein binding Lagrangian (Bethe--Weizsäcker form), not from $\mathrm{tr}_{\mathrm{full}}$. The per-channel traces are inherited from the published table. An independent witness for the high-$A$ $\chi^\lambda$ remains a separate open item, as the Gröbner--Shirshov reducer is infeasible past the light nuclei.

## Key observations

1. **Standard channel suppression.** The standard (2$\times$2) trace shrinks rapidly with $A$ for odd-$A$ and neutron-excess nuclei: from $1.0$ at $A = 1$ to $\sim 10^{-7}$ at $A = 19$ (${}^{19}\mathrm{F}$). For even-even nuclei (${}^{16}\mathrm{O}$, ${}^{20}\mathrm{Ne}$), the standard trace remains $O(10^{-1})$ due to the symmetric ground-state ordering. In all cases, the symmetric and alternating channels remain $O(1)$. The full Wedderburn trace recovers the physically correct mass scale.

2. **Alternating channel sign flips.** The alternating trace changes sign according to the parity of the total crossing count (the exponent of $(-q^{-1})$ in the alternating eigenvalue product). This parity depends on the ground-state ordering rather than directly on even/odd $A$. Under classical equal weighting, this sign variation propagates to $\mathrm{tr}_{\mathrm{full}}$, producing negative entries at ${}^7\mathrm{Li}$, ${}^{11}\mathrm{B}$, and ${}^{19}\mathrm{F}$. Under canonical $q$-deformed weights, the alternating block is suppressed $\sim 7\times$. Consequently, $\mathrm{tr}_{\mathrm{full}}$ stays positive and $O(0.2$--$1)$ across the table. The apparent sign variation was a classical-weighting artifact.

3. **${}^{14}\mathrm{N}$ cancellation.** For the symmetric nucleus $Z = N = 7$, the symmetric and alternating traces nearly cancel: $\mathrm{tr}_{\mathrm{sym}} \approx -\mathrm{tr}_{\mathrm{alt}}$, giving $\mathrm{tr}_{\mathrm{full}} \approx 0$ under classical weights. The equal proton--neutron composition produces equal-and-opposite contributions in the trivial and sign representations. This near-cancellation depends entirely on the classical weighting $\hat y_{\mathrm{sym}} = \hat y_{\mathrm{alt}}$. Under the canonical $q$-deformed weights, the symmetric block outweighs the alternating one by $\sim 18\times$, giving $\mathrm{tr}_{\mathrm{full}} = 0.512$ at ${}^{14}\mathrm{N}$. The near-cancellation vanishes.

4. **Binding energy deviations.** The Skein Lagrangian with $q$-derived Bethe--Weizsäcker coefficients reproduces $B/A$ to within $\sim 1$ MeV of AME2020 for most atoms. The largest deviation occurs at ${}^4\mathrm{He}$ ($+1.1$ MeV/$A$), where the semi-empirical formula undercounts the doubly-magic shell closure.

**Witness**: `atom-mass-full-hecke.witness.json` (producer `computations/atom_mass_full_hecke_qdeformed.py`). We apply the canonical $q$-deformed weights $\hat y_\lambda$ (from [Wenzl-bridge closed form](#prop:y-lambda-closed-form-wenzl-bridge), `y-lambda-at-q0.witness.json`) to the inherited per-atom channel traces. The high-$A$ $\chi^\lambda$ are not yet independently witnessed (GS reducer infeasible past light nuclei).
