*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark) — composite-crossing parity for stable atoms).**
Let $\mathcal{A}(Z, N)$ be a stable atom with electron
configuration occupying shells $S_1, \ldots, S_k$.  The
complete decomposition
([knot eigenbasis](#prop:knot-eigenbasis-complete))

$$
  V^{\otimes n} \cong
  \bigoplus_{\lambda \vdash n,\, \ell(\lambda) \leq 2}
  V_\lambda \otimes S_\lambda
$$

determines both the nuclear shell structure
([shell eigenvalues](#prop:shell-structure-eigenvalues))
and the thermodynamic phase behavior
([phase transitions](#prop:phase-transition-boundary))
through the same Hecke algebra $H_n(q)$.

**Sublimation criterion.**
An atom sublimes (bypasses the liquid phase) when the
Hecke module at the mixed-channel temperature admits a
non-split extension
([phase transitions](#prop:phase-transition-boundary)).
This extension is classified by

$$
  \mathrm{Ext}^1_{H_n(q)}(S_{\mathrm{asym}},
  S_{\mathrm{sym}}) \;\cong\; \mathbb{Z},
$$

and it **splits** (liquid phase is stable) if and only if
the outermost electron shell is **closed or nearly closed**
— i.e., the partition $\lambda_{\mathrm{outer}}$ labelling
the dominant representation of the valence electrons
satisfies $\lambda_1 - \lambda_2 \leq 1$.

Equivalently: the extension splits when the valence shell
sits in the **symmetric or near-symmetric** sector of the
Schur--Weyl decomposition.  It is non-split when the
valence shell is in a **half-filled** partition
($\lambda_1 \approx \lambda_2 + n/2$), which corresponds to
the mixed Hecke channel having maximal dimension.

**Crossing parity (coarse form).**
The composite crossing number satisfies
$n_K(\mathcal{A}) \equiv Z \pmod{2}$
(from the crossing budget $A^2 + 7A + 5Z$ and the identity
$A(A+1) \equiv 0 \pmod{2}$).  This parity is a
**necessary but not sufficient** condition for sublimation:
it detects the mod-2 shadow of the Young diagram structure
but cannot distinguish closed shells from half-filled ones.

**Full criterion.**
Let $\ell_v$ denote the number of valence electrons beyond
the last closed shell
([noble gas characterization](#prop:noble-gas-characterization)).
Let $\ell_{\max}$ be the capacity of the valence shell
($\ell_{\max} = 2n^2$ for principal quantum number $n$).
Then:

1. **Closed shell** ($\ell_v = 0$ or
   $\ell_v = \ell_{\max}$): extension splits.
   **Stable liquid.**

2. **Near-closed shell** ($\ell_v = 1$ or
   $\ell_v = \ell_{\max} - 1$): extension splits via the
   closed-core trivializing section.  **Stable liquid.**

3. **Half-filled shell** ($\ell_v \approx \ell_{\max}/2$)
   with odd $Z$: extension is non-split.
   **Sublimation-prone.**

4. **Metallic band** (delocalized electrons): the
   single-atom Hecke module $S_\lambda$ is replaced by
   the band-structure module $\bigoplus_k S_{\lambda(k)}$
   over crystal momenta $k$.  The direct sum generically
   contains both split and non-split extensions, and the
   majority (split) wins.  **Stable liquid.**
