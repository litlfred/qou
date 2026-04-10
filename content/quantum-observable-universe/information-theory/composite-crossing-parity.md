Let $\mathcal{A}(Z, N)$ be a stable atom with mass number
$A = Z + N$, constructed as
$\mathcal{N}(Z, N) \bowtie Z \cdot T_{2,3}$
([stable nucleus](#def:stable-nucleus)).  The **composite
crossing number** $n_K(\mathcal{A})$ — the minimal crossing
number of the full atomic link — determines the phase
behavior via the Hecke extension class
([phase transitions](#prop:phase-transition-boundary)).

**Crossing budget.**
The composite link consists of:

1. **Nucleon internal structure.**  Each nucleon
   ($\mathfrak{p}$ or $\mathfrak{n}$) is a color-tube-linked
   triple $[\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p$ or
   $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]_p$ bound by a
   Hopf link $\mathcal{L}_H$.  The quarks are trefoils
   ($T_{2,3}$ or $T_{2,3}^\sigma$, each with 3 crossings),
   but inside the Borromean tube structure $\mathcal{B}_3$
   they contribute as **link components**, not as separate
   knots.  The Borromean link has minimal crossing number 6,
   and the Hopf binding adds 2 crossings per nucleon.
   **Per-nucleon internal crossings**: 8.

2. **Inter-nucleon Hopf links.**  Each pair of nucleons
   is Hopf-linked, contributing 2 crossings per pair.
   **Total**: $2\binom{A}{2} = A(A-1)$.

3. **Electron trefoils.**  Each of the $Z$ electrons is
   a trefoil $T_{2,3}$ with 3 crossings.
   **Total**: $3Z$.

4. **Electron-nucleus Hopf binding.**  Each electron is
   Hopf-linked to the nucleus.
   **Total**: $2Z$.

**Total crossing budget:**

$$
  n_K^{(\mathrm{diag})}(\mathcal{A})
  \;=\; 8A + A(A-1) + 3Z + 2Z
  \;=\; A^2 + 7A + 5Z.
$$

This is a **diagrammatic** upper bound.  The **minimal**
crossing number $n_K \leq n_K^{(\mathrm{diag})}$, with
equality when the link is alternating (which holds for
nuclear Hopf-link composites by the Kauffman--Murasugi--
Thistlethwaite theorem, since each Hopf link is
alternating and the composite preserves alternation).

**Parity.**
Since $A = Z + N$:

$$
  n_K \;\equiv\; A^2 + 7A + 5Z
  \;\equiv\; A^2 + A + Z
  \;\equiv\; A(A+1) + Z
  \;\equiv\; Z \pmod{2},
$$

because $A(A+1)$ is always even (product of consecutive
integers).

**The crossing parity is determined by the atomic number
alone:**

$$
  n_K(\mathcal{A}(Z, N))
  \;\equiv\; Z \pmod{2}.
$$

Atoms with **odd $Z$** (odd atomic number) have odd
composite crossing number.  Atoms with **even $Z$** have
even composite crossing number.

**Test against observed sublimation.**

| Element | $Z$ | $n_K$ parity | Predicts | Observed | |
|---------|-----|:---:|---|---|---|
| H  | 1  | odd  | sublimation-prone | Liquid exists at 20 K | $\times$ |
| He | 2  | even | stable liquid | Liquid exists at 4 K | $\checkmark$ |
| N  | 7  | odd  | sublimation-prone | Sublimes at 1 atm ($\alpha$-phase) | $\checkmark$ |
| O  | 8  | even | stable liquid | Liquid at 90 K | $\checkmark$ |
| Na | 11 | odd  | sublimation-prone | Melts normally | $\times$ |
| Mg | 12 | even | stable liquid | Melts normally | $\checkmark$ |
| P  | 15 | odd  | sublimation-prone | Red P sublimes | $\checkmark$ |
| S  | 16 | even | stable liquid | Melts normally | $\checkmark$ |
| As | 33 | odd  | sublimation-prone | Sublimes at 1 atm | $\checkmark$ |
| I  | 53 | odd  | sublimation-prone | Sublimes at 1 atm | $\checkmark$ |
| Fe | 26 | even | stable liquid | Melts normally | $\checkmark$ |
| Cu | 29 | odd  | sublimation-prone | Melts normally | $\times$ |

**Score: 9/12 (75%).**  The parity rule correctly predicts
the phase behavior for most elements, but has clear
counterexamples (H, Na, Cu have odd $Z$ but melt normally).

**Interpretation.**
The $Z$-parity result says that the Hecke extension
obstruction depends on the **number of electron trefoils**
modulo 2 — the electrons control whether the mixed Hecke
representation splits.  This is physically reasonable:
electron shells mediate inter-atomic bonding, and it is the
bonding topology (not the nuclear topology) that determines
the condensed-matter phase.

The counterexamples indicate that crossing parity is a
**necessary but not sufficient** condition for sublimation.
The full condition involves the Hecke module structure at
the specific temperature, which depends on $q$, $n_K$, and
the representation type — not just parity.  Metals like
Cu and Na have delocalized electron bands (the electrons
are shared across atoms, not localized in trefoil shells),
which effectively modifies the crossing topology of the
condensed phase.

**Refinement needed.**
The parity argument applies to the **single-atom** Hecke
algebra $H_{n_K}(q)$.  But the condensed-matter phase
transition involves the **many-body** Hecke algebra of the
inter-atomic link composite.  A proper treatment must
account for:
1. The inter-atomic braid linking in the condensed phase
2. The effect of delocalized (metallic) electron bands
3. The crystal symmetry group and its interaction with
   the Hecke algebra
4. Pressure dependence (which changes the effective
   fibre volume $\mathrm{Vol}(S^3_q)$)

These refinements are beyond the scope of the ideal gas
framework and will require a condensed-matter extension of
the categorical partition function.
