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

The full Markov trace on the regular representation is

$$
  \mathrm{tr}_M^{\mathrm{full}}
  = w_{\mathrm{sym}}\,\mathrm{tr}_{\mathrm{sym}}
  + w_{\mathrm{std}}\,\mathrm{tr}_{\mathrm{std}}
  + w_{\mathrm{alt}}\,\mathrm{tr}_{\mathrm{alt}}
$$

with Wedderburn-Artin weights $w_\lambda = d_\lambda^2 / |S_3|$.

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

All traces computed at $q = 111/100$ (exact rational arithmetic).
Binding energy from the Skein binding Lagrangian
([Skein binding Lagrangian](#def:skein-binding-lagrangian))
with $q$-derived Bethe--Weizsäcker coefficients.

See [Table](#tbl:atom-mass-full-hecke-table-data).

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
   the trivial and sign representations.

4. **Binding energy deviations.**  The Skein Lagrangian with
   $q$-derived Bethe--Weizsäcker coefficients reproduces
   $B/A$ to within $\sim 1$ MeV of AME2020 for most atoms,
   with the largest deviation at ${}^4\mathrm{He}$ ($+1.1$
   MeV/$A$) where the semi-empirical formula is known to
   undercount the doubly-magic shell closure.

**Witness**: `atom-mass-full-hecke.witness.json`
(exact rationals, three-channel traces, Skein binding decomposition).
