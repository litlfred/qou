**Proposition (conditional on [conj:borromean-quark](#conj:borromean-quark)).** Let $\mathcal{A}(Z, N)$ be a stable atom with electron configuration occupying shells $S_1, \ldots, S_k$. The complete decomposition ([knot eigenbasis](#prop:knot-eigenbasis-complete))

$$
  V^{\otimes n} \cong
  \bigoplus_{\lambda \vdash n,\, \ell(\lambda) \leq 2}
  V_\lambda \otimes S_\lambda
$$

determines both the nuclear shell structure ([shell eigenvalues](#prop:shell-structure-eigenvalues)) and the thermodynamic phase behavior ([phase transitions](#prop:phase-transition-boundary)) through the same Hecke algebra $H_n(q)$.

**Sublimation criterion.**
An atom sublimes—bypassing the liquid phase—when the Hecke module at the mixed-channel temperature admits a non-split extension ([phase transitions](#prop:phase-transition-boundary)). This extension is classified by

$$
  \mathrm{Ext}^1_{H_n(q)}(S_{\mathrm{asym}},
  S_{\mathrm{sym}}) \;\cong\; \mathbb{Z}.
$$

The extension **splits** (yielding a stable liquid phase) if and only if the outermost electron shell is closed or nearly closed. In terms of partitions, the Young diagram $\lambda_{\mathrm{outer}}$ labelling the valence electrons must satisfy $\lambda_1 - \lambda_2 \leq 1$. Equivalently, the valence shell sits in the symmetric or near-symmetric sector of the Schur--Weyl decomposition.

The extension is **non-split** when the valence shell is half-filled ($\lambda_1 \approx \lambda_2 + n/2$). Here the mixed Hecke channel achieves maximal dimension, driving sublimation.

**Crossing parity.**
To estimate sublimation behavior, we check the composite crossing parity. The composite crossing number satisfies $n_K(\mathcal{A}) \equiv Z \pmod{2}$, following from the crossing budget $A^2 + 7A + 5Z$ and the identity $A(A+1) \equiv 0 \pmod{2}$. This parity detects the mod-2 shadow of the Young diagram structure. It is a necessary but not sufficient condition for sublimation because it cannot distinguish closed shells from half-filled ones.

**Full criterion.**
Let $\ell_v$ denote the number of valence electrons beyond the last closed shell ([noble gas characterization](#prop:noble-gas-characterization)). Let $\ell_{\max}$ be the capacity of the valence shell ($\ell_{\max} = 2n^2$ for principal quantum number $n$). We classify the macroscopic phase:

1. **Closed shell** ($\ell_v = 0$ or $\ell_v = \ell_{\max}$): The extension splits. The liquid phase is stable.
2. **Near-closed shell** ($\ell_v = 1$ or $\ell_v = \ell_{\max} - 1$): The extension splits via the closed-core trivializing section. The liquid phase is stable.
3. **Half-filled shell** ($\ell_v \approx \ell_{\max}/2$) with odd $Z$: The extension is non-split. The atom is prone to sublimation.
4. **Metallic band** (delocalized electrons): The single-atom Hecke module $S_\lambda$ is replaced by the band-structure module $\bigoplus_k S_{\lambda(k)}$ over crystal momenta $k$. The direct sum generically contains both split and non-split extensions. The split extensions dominate, yielding a stable liquid phase.
