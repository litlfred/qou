The existing atomic mass appendix
([atomic mass calculations](#sec:amc-calculations)) uses the 2$\times$2
**standard** irrep of $H_3(q)$ for the transfer matrix chain.
This projects the Hecke element onto the $(2,1)$-seminormal representation
and discards the symmetric (trivial) and alternating (sign)
channels.  For multi-nucleon systems, this projection throws
away the **dominant contribution**: the standard channel
trace $\mathrm{tr}_{\mathrm{std}}$ decays exponentially with
$A$, while $\mathrm{tr}_{\mathrm{sym}}$ and
$\mathrm{tr}_{\mathrm{alt}}$ remain $O(1)$.

This remark computes the atomic mass for $Z = 1$ through
$Z = 10$ using the **full regular representation** of $H_3(q)$
with all three irreducible channels tracked independently.

## Three-channel decomposition

See [Table: Three-channel $H_3(q)$ decomposition](#tbl:atom-mass-full-hecke-table-data).

The full Markov trace decomposes over the three Wedderburn blocks of
$H_3(q)$ as

$$
  \mathrm{tr}_M^{\mathrm{full}}
  = \hat y_{\mathrm{sym}}\,\mathrm{tr}_{\mathrm{sym}}
  + \hat y_{\mathrm{std}}\,\mathrm{tr}_{\mathrm{std}}
  + \hat y_{\mathrm{alt}}\,\mathrm{tr}_{\mathrm{alt}},
$$

where $\hat y_\lambda = y_\lambda(q)\,d_\lambda$ are the **$q$-deformed
Jones--Markov weights** — the Wenzl Schur principal specialisation of the
canonical $y_\lambda$
([Wenzl-bridge closed form](#prop:y-lambda-closed-form-wenzl-bridge))
— normalised by $\sum_\lambda \hat y_\lambda = 1$. These are the weights
the production Markov-trace compute uses throughout. The **classical**
Wedderburn--Artin values $d_\lambda^2 / |S_3| = \{\tfrac16, \tfrac23,
\tfrac16\}$ are only their $q \to 1$ limit; at the substrate scale the
deformation is large rather than a small correction. From the cached
weights, $\hat y_{\mathrm{sym}} \approx 0.42$, $\hat y_{\mathrm{std}}
\approx 0.56$, $\hat y_{\mathrm{alt}} \approx 0.02$ — the symmetric weight
rises by about $2.5\times$ and the alternating weight falls by about
$7\times$ relative to the classical equal-weighting of the symmetric and
alternating channels.

## Mass decomposition (fibre / horizontal / mixed)

For each nucleus, the mass integrand
([Hecke mass element](#def:hecke-mass-element)) splits along
the charge--mass duality
([charge--mass duality](#rem:hecke-charge-mass-duality)):

1. **Horizontal** (crossing energy):
   $\mathfrak{E}_{\mathrm{cross}} = n_+ q - n_- q^{-1}$,
   where $n_+$ counts proton--proton pairs and $n_-$ counts
   neutron--neutron pairs.

2. **Vertical / fibre** (Markov trace mass):
   $\mathfrak{m}_{\mathrm{vert}} = \mathrm{tr}_M^{\mathrm{full}}(\Phi_{\mathrm{mass}})$.

3. **Mixed** (vertex operator coupling):
   $\mathfrak{m}_{\mathrm{mix}} = \mathfrak{E}_{\mathrm{cross}} \cdot (q - 1)^2$.

## Results for $Z = 1$--$10$

The per-channel traces $\mathrm{tr}_{\mathrm{sym}},
\mathrm{tr}_{\mathrm{std}}, \mathrm{tr}_{\mathrm{alt}}$ below are
evaluated at $q = 111/100$ (a convenient rational near the substrate
$q_0 \approx 1.10998$; exact rational arithmetic). Binding energy is from
the Skein binding Lagrangian
([Skein binding Lagrangian](#def:skein-binding-lagrangian))
with $q$-derived Bethe--Weizsäcker coefficients.

See [Table](#tbl:atom-mass-full-hecke-table-data).

**Note (weighting convention).** The $\mathrm{tr}_{\mathrm{full}}$ column
of the table — and the $B/A$ and $\Delta$ columns derived from it — are
formed with the $q \to 1$ classical weights $\{\tfrac16, \tfrac23,
\tfrac16\}$, not the canonical $q$-deformed $\hat y_\lambda$ above. Under
$\hat y_\lambda$ these move materially (for ${}^4\mathrm{He}$,
$\mathrm{tr}_{\mathrm{full}}$ shifts from $\approx 0.42$ to $\approx
0.52$). A $q$-deformed regeneration of the table, with its own witness, is
the outstanding production step; the channel traces themselves are
weight-independent.

## Key observations

1. **Standard channel suppression.**  The standard (2$\times$2) trace
   shrinks rapidly with $A$ for odd-$A$ and neutron-excess
   nuclei: from $1.0$ at $A = 1$ to $\sim 10^{-7}$ at $A = 19$
   (${}^{19}\mathrm{F}$).  For even-even nuclei (${}^{16}\mathrm{O}$,
   ${}^{20}\mathrm{Ne}$) the standard trace remains $O(10^{-1})$
   due to the symmetric ground-state ordering.  In all cases the
   symmetric and alternating channels remain $O(1)$, and the full
   Wedderburn trace recovers the physically correct mass scale.

2. **Alternating channel sign flips.**  The alternating trace
   changes sign according to the parity of the total crossing
   count (the exponent of $(-q^{-1})$ in the alternating
   eigenvalue product), which depends on the ground-state
   ordering rather than directly on even/odd $A$.  This
   produces the sign variation in $\mathrm{tr}_{\mathrm{full}}$
   visible across the table.

3. **${}^{14}\mathrm{N}$ cancellation.**  For the symmetric
   nucleus $Z = N = 7$, the symmetric and alternating traces
   nearly cancel:
   $\mathrm{tr}_{\mathrm{sym}} \approx -\mathrm{tr}_{\mathrm{alt}}$,
   giving $\mathrm{tr}_{\mathrm{full}} \approx 0$.  This is
   a $Z = N$ symmetry artifact — the equal proton--neutron
   composition produces equal-and-opposite contributions in
   the trivial and sign representations.  The near-cancellation,
   however, depends on the equal *classical* weighting
   $\hat y_{\mathrm{sym}} = \hat y_{\mathrm{alt}}$: under the canonical
   $q$-deformed weights the symmetric block outweighs the alternating one
   by $\sim 18\times$, so $\mathrm{tr}_{\mathrm{full}}$ does not vanish at
   ${}^{14}\mathrm{N}$.

4. **Binding energy deviations.**  The Skein Lagrangian with
   $q$-derived Bethe--Weizsäcker coefficients reproduces
   $B/A$ to within $\sim 1$ MeV of AME2020 for most atoms,
   with the largest deviation at ${}^4\mathrm{He}$ ($+1.1$
   MeV/$A$) where the semi-empirical formula is known to
   undercount the doubly-magic shell closure.

**Weights witness**: the $q$-deformed Jones--Markov weights
$\hat y_\lambda$ are pinned by `y-lambda-at-q0.witness.json` (canonical
source
[Wenzl-bridge closed form](#prop:y-lambda-closed-form-wenzl-bridge)).
A dedicated witness for the per-atom three-channel table (channel traces +
$q$-deformed $\mathrm{tr}_{\mathrm{full}}$ + Skein binding) is not yet
produced.
