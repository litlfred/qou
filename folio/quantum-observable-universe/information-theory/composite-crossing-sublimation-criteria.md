The single Hecke algebra $H_n(q)$ of [the composite crossing parity conjecture](#conj:composite-crossing-parity) governs the phase behaviour through the following criteria.

**Sublimation criterion.**
There is no split/non-split dichotomy to state this criterion in. At a substrate parameter that is not a root of unity $H_n(q)$ is semisimple, so every short exact sequence of $H_n(q)$-modules splits and $\mathrm{Ext}^1_{H_n(q)}$ vanishes on every pair of modules ([the phase-transition boundary](#prop:phase-transition-boundary)); the $S_\lambda$ are irreducible summands of $V^{\otimes n}$ ([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)(1)), and an irreducible module is not an extension of anything by anything.

What is left is a correlation with the Young diagram of the valence shell, stated without a mechanism. The liquid phase is stable when the outermost electron shell is closed or nearly closed — in terms of partitions, when the diagram $\lambda_{\mathrm{outer}}$ labelling the valence electrons satisfies $\lambda_1 - \lambda_2 \leq 1$, so that the valence shell inhabits the symmetric or near-symmetric sector of the Schur--Weyl decomposition. Sublimation is instead associated with a half-filled valence shell ($\lambda_1 \approx \lambda_2 + n/2$), where the mixed Hecke channel achieves maximal dimension. That dimension statement is a fact about $S_\lambda$; the step from it to a thermodynamic instability is not supplied here.

**Crossing parity.**
Sublimation behavior correlates with the composite crossing parity. The composite crossing number identically satisfies $n_K(\mathcal{A}) \equiv Z \pmod{2}$, stemming from the crossing budget $A^2 + 7A + 5Z$ and the invariant parity $A(A+1) \equiv 0 \pmod{2}$. This parity detects the mod-2 shadow of the Young diagram structure. It acts as a necessary but not sufficient condition for sublimation, as it fails to distinguish closed shells from half-filled ones.

**Full criterion.**
Let $\ell_v$ denote the number of valence electrons beyond the last closed shell. Let $\ell_{\max}$ dictate the capacity of the valence shell ($\ell_{\max} = 2n^2$ for principal quantum number $n$). The macroscopic phase is classified across four shell regimes:

1. **Closed shell** ($\ell_v = 0$ or $\ell_v = \ell_{\max}$): The liquid phase is stable.
2. **Near-closed shell** ($\ell_v = 1$ or $\ell_v = \ell_{\max} - 1$): The liquid phase is stable.
3. **Half-filled shell** ($\ell_v \approx \ell_{\max}/2$) with odd $Z$: The atom is structurally prone to sublimation.
4. **Metallic band** (delocalized electrons): The single-atom Hecke module $S_\lambda$ expands to the band-structure module $\bigoplus_k S_{\lambda(k)}$ over crystal momenta $k$, and the liquid phase is stable.

The classification is empirical: nothing above derives it from the Hecke representation theory.
