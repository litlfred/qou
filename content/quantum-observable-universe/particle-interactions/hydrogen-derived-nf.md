**Example.**
Hydrogen $\mathcal{A}(1,0)$ derived from $3 \times \gamma\gamma$ pair production.

## Derivation chain

$$
  3(\gamma\gamma) \xrightarrow{\text{pair prod.}} (\mathfrak{u}_1, \mathfrak{u}_2, \mathfrak{d}_3) + (\bar{\mathfrak{u}}_1, \bar{\mathfrak{u}}_2, \bar{\mathfrak{d}}_3) \xrightarrow{\mathcal{B}_3} \xrightarrow{\text{gluon } \sigma_0^2} \mathfrak{p} \xrightarrow{\sigma_0} \mathfrak{p} \oplus T_{2,3} = \mathcal{A}(1,0)
$$

**Step 1.** Three 4-term $\gamma\gamma$ collisions produce three quark-antiquark pairs ([4-term pair nucleon](#prop:four-term-pair-nucleon)).

**Step 2.** The operator $\mathcal{B}_3$ confines the three quarks $(\mathfrak{u}_1, \mathfrak{u}_2, \mathfrak{d}_3)$ ([confinement selection](#prop:confinement-operator-selection)).

**Step 2b.** The LP-derived gluon ($\sigma_0 \to \sigma_0$, two crossings) stabilises the confined state ([integer LP gluon](#prop:mass-endomorphism-tower)). This yields the proton normal form with $\mathrm{net}(\mathfrak{p}) \approx +0.986$ (11 total crossings: 6 from $\mathcal{B}_3$, 3 from quarks, 2 from the gluon).

**Step 3.** The proton Hopf-links to the electron (trefoil $T_{2,3}$) via the electromagnetic crossing $\sigma_0$:

$$
  \mathcal{A}(1,0) = \mathrm{NF}(\mathfrak{p} \cdot \sigma_0 \cdot e^-).
$$

## Hydrogen NF

$$
  \mathrm{NF}(\mathcal{A}(1,0)) = +0.090\gamma + 1.018\sigma_0 - 0.024\sigma_1 + 0.213 L_+ + 0.112 L_- + 0.080 e^-.
$$

See [Table 1](#tbl:hydrogen-derived-nf-table1-data).

$$
  \mathrm{net}(\mathcal{A}(1,0)) \approx +1.489
$$

**Key observation:** The $e^-$ coefficient flips from $-0.043$ (unbound proton) to $+0.080$ (hydrogen atom). The Hopf linking with the electron satisfies the proton's trefoil demand. The bound atom has $e^- > 0$, closing the beta decay channel.

The only remaining demand is $\sigma_1 = -0.024$. This reflects the incomplete $1s^1$ shell. Hydrogen has one electron rather than the closed-shell pair of helium.

## Mass budget

See [Table 2](#tbl:hydrogen-derived-nf-table2-data).

This is consistent with the [hydrogen knot structure](#ex:hydrogen-knot-structure).

**Witness**: `four-term-photon-to-atoms.witness.json`.
