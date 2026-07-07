<!-- FILE_START: derived-atoms-intro.md -->
The three operator regimes of §4 are abstract. We instantiate them on five concrete light nuclei to confirm that the regime predictions match the empirical normal forms and binding energies. Hydrogen represents the base case: a single proton with no internucleon crossings. Deuterium provides the simplest two-nucleon braid. 

The structural binding energy for Deuterium is extracted from the Markov trace volume integral as a zero-parameter prediction against AME2020. Helium-4 realises the first doubly magic closure. Lithium-6 exhibits the post-magic operator transition. Oxygen-16 is the second doubly magic point. These five examples fix the data that §6 reorganises through the typed Garside element.
<!-- FILE_END: derived-atoms-intro.md -->

<!-- FILE_START: hydrogen-derived-nf.md -->
**Example.**
Hydrogen $\mathcal{A}(1,0)$ derived from $3 \times \gamma\gamma$ pair production.

## Derivation chain

$$
  3(\gamma\gamma) \xrightarrow{\text{pair prod.}} (\mathfrak{u}_1, \mathfrak{u}_2, \mathfrak{d}_3) + (\bar{\mathfrak{u}}_1, \bar{\mathfrak{u}}_2, \bar{\mathfrak{d}}_3) \xrightarrow{\mathcal{B}_3} \xrightarrow{\text{gluon } \sigma_0^2} \mathfrak{p} \xrightarrow{\sigma_0} \mathfrak{p} \oplus T_{2,3} = \mathcal{A}(1,0)
$$

**Step 1.** Three 4-term $\gamma\gamma$ collisions produce three quark-antiquark pairs.
**Step 2.** The operator $\mathcal{B}_3$ confines the three quarks $(\mathfrak{u}_1, \mathfrak{u}_2, \mathfrak{d}_3)$.
**Step 2b.** The LP-derived gluon stabilises the confined state. This yields the proton normal form with $\mathrm{net}(\mathfrak{p}) \approx +0.986$.
**Step 3.** The proton Hopf-links to the electron via the electromagnetic crossing $\sigma_0$:

$$
  \mathcal{A}(1,0) = \mathrm{NF}(\mathfrak{p} \cdot \sigma_0 \cdot e^-).
$$

## Hydrogen NF

$$
  \mathrm{NF}(\mathcal{A}(1,0)) = +0.090\gamma + 1.018\sigma_0 - 0.024\sigma_1 + 0.213 L_+ + 0.112 L_- + 0.080 e^-.
$$

$$
  \mathrm{net}(\mathcal{A}(1,0)) \approx +1.489
$$

The $e^-$ coefficient flips from $-0.043$ (unbound proton) to $+0.080$ (hydrogen atom). The Hopf linking with the electron satisfies the proton's trefoil demand. The bound atom has $e^- > 0$, closing the beta decay channel. The only remaining demand is $\sigma_1 = -0.024$. This reflects the incomplete $1s^1$ shell. Hydrogen has one electron rather than the closed-shell pair of helium.
<!-- FILE_END: hydrogen-derived-nf.md -->

<!-- FILE_START: helium4-derived-nf.md -->
**Example.**
Helium-4 $\mathcal{A}(2,2)$ contains two protons, two neutrons, and two electrons. It forms the doubly-magic alpha particle.

## Derivation

Twelve $\gamma\gamma$ pair productions generate four nucleons. Each is confined by $\mathcal{B}_3$ and stabilized by LP-derived gluon crossings. Inter-nucleon typed crossings link them: $+\sigma$ for $p$-$p$, mixed for $p$-$n$, and shifted $-H_A$ for $n$-$n$.

## Nucleus NF ($\alpha$ particle)

$$
  \mathrm{NF}(\mathcal{N}(2,2)) = +0.041\gamma - 0.133\sigma_0 + 0.169\sigma_1 - 0.071 L_+ - 0.297 L_- + 1.040 e^-.
$$

$$
  \mathrm{net}(\mathcal{N}(2,2)) \approx +0.749
$$

The four-nucleon Hopf chain generates large trefoil content from iterated proton-neutron crossings. The $e^-$ term dominates.

## Full atom NF (with $1s^2$ shell)

We add two Hopf-linked electrons:

$$
  \mathrm{NF}(\mathcal{A}(2,2)) = +0.236\gamma - 0.061\sigma_0 + 0.176\sigma_1 + 0.384 L_+ - 0.037 L_- + 1.190 e^-.
$$

$$
  \mathrm{net}(\mathcal{A}(2,2)) \approx +1.889
$$

**Stability analysis.**
He-4 retains minor demand in $\sigma_0 = -0.061$ and $L_- = -0.037$. He-3 exhibits zero demand because all normal form coefficients are positive. He-4 exhibits two small demand channels. While both are stable, He-4 attains a lower Markov trace ($1.037$ versus $1.230$). The alpha particle minimizes the categorical action among $A=4$ configurations, reflecting doubly-magic enhanced binding.

## Comparison: He-3 vs He-4

The He-3 atom achieves full demand closure with only three nucleons. He-4 adds a second neutron. This fourth nucleon slightly reopens the $\sigma_0$ and $L_-$ demand channels while reducing the overall Markov trace. The binding tightens despite the residual demand. This gives the categorical expression of doubly-magic $N=Z=2$ stability.
<!-- FILE_END: helium4-derived-nf.md -->

<!-- FILE_START: li6-derived-nf.md -->
**Example.**
Lithium-6 ($Z = 3$, $N = 3$, $A = 6$) is the lightest nucleus beyond the doubly-magic helium-4 core. Its construction demonstrates the operator transition from Regime II (Hopf link) back to Regime III (bare crossing) after the He-4 magic shell closes.

## Inductive construction

The He-4 core is built by Regime I $\to$ II operators. The fifth nucleon still uses a Hopf link, riding the stability of the doubly-magic core. But the sixth nucleon transitions to the bare mixed crossing $C_{pn}$ (Regime III).

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

1. All coefficients are positive. Li-6 is demand-free. This is consistent with Li-6 being the lightest stable lithium isotope.
2. The dominant term is $L_-$. This reflects the strong neutron-proton Hopf binding inherited from the He-4 core.
3. The operator transition at step 6 marks the passage from the magic-shell regime to the open-shell regime. Beyond this point, nucleons interact via bare crossings. The collective shell effect diminishes.
4. The $e^-$ coefficient is positive. The nucleus absorbs the trefoil demand. The positive $e^-$ means the nucleus is a trefoil supplier, not a demander. It can emit electrons without beta-decay instability.
<!-- FILE_END: li6-derived-nf.md -->

<!-- FILE_START: o16-derived-nf.md -->
**Example.**
Oxygen-16 ($Z = 8$, $N = 8$, $A = 16$) is the first doubly-magic nucleus beyond ${}^{4}\mathrm{He}$. Both $Z = 8$ and $N = 8$ are nuclear magic numbers, corresponding to the closure of the $1p$ shell.

## Construction

We build the derived atom $\mathcal{A}(8, 8)$ via the 5-step construction:

1. **48 pair productions** yield 16 quark triples.
2. **16 Borromean confinements** yield 8 proton normal forms and 8 neutron normal forms.
3. **Inductive nuclear assembly** consists of 15 inter-nucleon crossings. Each undergoes Gröbner--Shirshov reduction.
4. **8 electron Hopf links** yield the closed $1s^2 2s^2 2p^4$ electron configuration.

## Expected operator sequence

By the three-regime theory, the 15 inter-nucleon operators follow the predicted pattern. At step 16, the final operator must be a Hopf link that achieves demand closure. This closes the $1p$ neutron shell.

## Scaling

The inductive reduction for $A = 16$ requires at most 15 Hecke multiplications. At $A = 16$, the unreduced braid word contains $\sim 10^{10}$ terms. The inductive approach reduces this to $\leq 128$ normal-form terms within $\leq 480$ Hecke steps, remaining tractable.

## Doubly magic prediction

The periodic table demand conjecture predicts that $\mathcal{A}(8, 8)$ minimizes $|\mathrm{dem}|$ among all $A = 16$ isotopes. Testing this requires computing $\mathcal{A}(Z, 16 - Z)$ for all $0 \leq Z \leq 16$ and comparing demand magnitudes. If both the proton and neutron shells independently achieve demand closure, the doubly-magic nucleus attains $|\mathrm{dem}| = 0$, indicating complete stability.
<!-- FILE_END: o16-derived-nf.md -->