**Example.**
Lithium-6 ($Z = 3$, $N = 3$, $A = 6$) is the lightest nucleus beyond the doubly-magic helium-4 core. Its construction demonstrates the operator transition from Regime II (Hopf link) back to Regime III (bare crossing) after the He-4 magic shell closes.

## Inductive construction

See [Table](#tbl:li6-derived-nf-table-data).

The He-4 core ($ppnn$) is built by Regime I $\to$ II operators (torus knot, then Hopf links). The fifth nucleon (proton) still uses a Hopf link ($L_-$), riding the stability of the doubly-magic core. But the sixth nucleon (neutron) transitions to the bare mixed crossing $C_{pn}$ (Regime III).

## Normal form at $q_0$

$$
  \mathrm{NF}(\mathcal{A}(3,3))
  \approx
  +0.087\gamma
  + 0.130\sigma_0
  + 0.455\sigma_1
  + 0.205 L_+
  + 1.288 L_-
  + 0.589 e^-
$$

$$
  \mathrm{net} \approx +2.754, \qquad
  |\mathrm{dem}| = 0
  \quad \text{(all coefficients positive).}
$$

## Physical interpretation

1. All coefficients are positive. Li-6 is demand-free (stable). This is consistent with Li-6 being the lightest stable lithium isotope.
2. The dominant term is $L_-$ ($\approx 1.29$). This reflects the strong neutron-proton Hopf binding inherited from the He-4 core.
3. The operator transition at step 6 ($L_- \to C_{pn}$) marks the passage from the magic-shell regime to the open-shell regime. Beyond this point, nucleons interact via bare crossings. The collective shell effect diminishes.
4. The $e^-$ coefficient is positive ($+0.589$). This is a key difference from the single-nucleon case, where $c_{e^-} < 0$. The nucleus absorbs the trefoil demand. The positive $e^-$ means the nucleus is a trefoil supplier, not a demander. It can emit electrons without beta-decay instability.

**Witness**: `nuclear-binding-lp.witness.json`.
