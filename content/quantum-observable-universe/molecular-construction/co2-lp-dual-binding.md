**Proposition (conditional on [`conj:q-integer-mass-formula`](#conj:q-integer-mass-formula)).**
*The LP dual of the $CO_2$ molecular braid selects the symmetric
linear arrangement O=C=O with two double bonds as the ground
state, minimising $\Phi_1$ over all possible:*

1. *Bond order assignments: $(k_1, k_2)$ with $k_1 + k_2 \leq 4$
   (carbon's valence)*
2. *Electron-bond assignments: which electrons are shared with
   which oxygen*
3. *Strand orderings: permutations of 66 strands*

*The LP dual has three shadow prices:*

- *$y_{\sigma}$: value of each $\sigma$-bond shared pair*
- *$y_{\pi}$: value of each $\pi$-bond shared pair*
- *$y_{\mathrm{sym}}$: value of symmetric bond placement
  (equal bonds to both oxygens)*

*The symmetric double-bond configuration $(k_1, k_2) = (2, 2)$
wins over asymmetric alternatives $(3, 1)$ or $(1, 3)$ because:*

- *Each double bond contributes 4 attractive crossings*
- *The symmetric arrangement minimises $O_1$-$O_2$
  repulsion (protons are maximally separated)*
- *The asymmetric $(3, 1)$ configuration wastes one of
  oxygen's valence sites and places more electron density
  on one side, increasing $e$-$e$ repulsion*

*This is the braid-theoretic origin of **VSEPR geometry**:
electron-pair repulsion minimisation is literally $\Phi_1$
minimisation over strand orderings, and the LP dual formalises
the repulsion-minimisation principle as a linear program.*

*The binding energy per C=O bond should be compared with:*
- *$CO$ triple bond: $\approx :val[observed_D0_CO_eV]{precision=4, witness=computations/co-bond-order-active-set.witness.json} \;\mathrm{eV}$ (3 bonds)*
- *$CO_2$ double bond: $\approx :val[d0_co2_double_ev]{precision=3, witness=computations/molecular-experimental-refs.witness.json} \;\mathrm{eV}$ (2 bonds)*
- *The per-bond energy decreases with bond order as expected:
  $11.09/3 \approx 3.70$ vs $8.28/2 \approx 4.14 \;\mathrm{eV}$
  per shared pair.*
