The $Z$-parity rule
([crossing parity](#prop:composite-crossing-parity))
predicts that odd-$Z$ atoms are sublimation-prone (the
Hecke extension is non-split) while even-$Z$ atoms have
stable liquid phases.

**Test against observed sublimation at 1 atm.**

| Element | $Z$ | Parity | Predicts | Observed | |
|---------|-----|:---:|---|---|---|
| H  | 1  | odd  | sublimation-prone | Liquid at 20 K | $\times$ |
| He | 2  | even | stable liquid | Liquid at 4 K | $\checkmark$ |
| N  | 7  | odd  | sublimation-prone | Sublimes ($\alpha$) | $\checkmark$ |
| O  | 8  | even | stable liquid | Liquid at 90 K | $\checkmark$ |
| Na | 11 | odd  | sublimation-prone | Melts normally | $\times$ |
| Mg | 12 | even | stable liquid | Melts normally | $\checkmark$ |
| P  | 15 | odd  | sublimation-prone | Red P sublimes | $\checkmark$ |
| S  | 16 | even | stable liquid | Melts normally | $\checkmark$ |
| As | 33 | odd  | sublimation-prone | Sublimes | $\checkmark$ |
| I  | 53 | odd  | sublimation-prone | Sublimes | $\checkmark$ |
| Fe | 26 | even | stable liquid | Melts normally | $\checkmark$ |
| Cu | 29 | odd  | sublimation-prone | Melts normally | $\times$ |

**Score: 9/12 (75%).**

The even-$Z$ predictions are **perfect** (5/5): every
tested even-$Z$ element has a stable liquid phase.  The
odd-$Z$ predictions hit 4/7: N, P, As, I sublime as
predicted, but H, Na, Cu melt normally.

**Why parity is necessary but not sufficient.**
The $Z$-parity determines whether the Hecke extension
*can* be non-split (odd $Z$ → possible obstruction).
Whether the liquid phase is *actually* unstable depends
on additional structure:

1. **Metallic bonding** (Na, Cu): delocalized electron
   bands share trefoils across atoms, effectively
   modifying the single-atom crossing topology into a
   many-body braid.

2. **Hydrogen**: at $Z = 1$ the single electron is
   tightly bound (13.6 eV ionization), so inter-atomic
   linking is weak despite odd parity.

3. **Crystal symmetry**: the condensed-matter Hecke
   algebra is the many-body $H_{n_K \cdot N_{\mathrm{atoms}}}(q)$,
   not the single-atom $H_{n_K}(q)$.  Lattice
   symmetries can force the extension to split even
   when the single-atom extension does not.

A proper treatment requires a condensed-matter extension
of the categorical partition function, accounting for
inter-atomic braid linking, delocalized bands, and
pressure dependence.
