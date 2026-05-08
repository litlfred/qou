**Example.**
Helium-4 $\mathcal{A}(2,2)$: two protons, two neutrons, two electrons.
The doubly magic alpha particle.

## Derivation

Twelve $\gamma\gamma$ pair productions produce four nucleons
(2 protons, 2 neutrons), each confined by $\mathcal{B}_3$
([confinement selection](#prop:confinement-operator-selection))
and stabilised by LP-derived gluon crossings: $2\sigma_0$
per proton, $L_+L_-$ per neutron
([integer LP gluon](#prop:mass-endomorphism-tower)).
The four nucleons ($11$ crossings each for protons, $13$ for
neutrons) are linked by inter-nucleon typed crossings
($p$-$p$: $+\sigma$, $p$-$n$: mixed, $n$-$n$: $-H_A$ shifted).

## Nucleus NF ($\alpha$ particle)

$$
  \mathrm{NF}(\mathcal{N}(2,2))
  =
  +0.041\gamma - 0.133\sigma_0 + 0.169\sigma_1
  - 0.071 L_+ - 0.297 L_- + 1.040 e^-.
$$

$$
  \mathrm{net}(\mathcal{N}(2,2)) \approx +0.749
$$

The dominant term is $e^- \approx +1.040$: the four-nucleon
Hopf chain generates a large trefoil content from the iterated
proton--neutron crossings.

## Full atom NF (with $1s^2$ shell)

After adding two Hopf-linked electrons
([helium Hopf diagram](#rem:helium-hopf-diagram)):

$$
  \mathrm{NF}(\mathcal{A}(2,2))
  =
  +0.236\gamma - 0.061\sigma_0 + 0.176\sigma_1
  + 0.384 L_+ - 0.037 L_- + 1.190 e^-.
$$

$$
  \mathrm{net}(\mathcal{A}(2,2)) \approx +1.889
$$

**Stability analysis.**
He-4 retains small demand in $\sigma_0 = -0.061$ and
$L_- = -0.037$.  Compare with He-3:

| Atom | $\mathrm{net}$ | Demand channels | $\mathrm{tr}_M$ |
|:---|---:|:---:|---:|
| ${}^3\mathrm{He}$ | $+2.338$ | **0** (fully stable) | $1.230$ |
| ${}^4\mathrm{He}$ | $+1.889$ | $2$ ($\sigma_0$, $L_-$) | $1.037$ |

He-3 has zero demand (all NF coefficients positive), while
He-4 has two small demand channels.  Both are stable, but
He-4's lower Markov trace ($1.037$ vs $1.230$) reflects the
doubly-magic enhanced binding: the alpha particle minimizes
the categorical action among $A = 4$ configurations.

## Comparison: He-3 vs He-4

The He-3 atom ($2p + 1n + 2e^-$) achieves full demand closure
(no negative NF coefficients) with only 3 nucleons.  He-4 adds
a fourth nucleon (second neutron) which slightly reopens the
$\sigma_0$ and $L_-$ demand channels, but reduces the overall
Markov trace — the binding is tighter despite the residual
demand.  This is the categorical expression of the
doubly-magic $N = Z = 2$ stability.

**Witness**: `four-term-photon-to-atoms.witness.json`.
