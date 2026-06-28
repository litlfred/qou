The following develops the [$\beta$-decay Skein
operation](#def:beta-decay-skein): the $T_{3,5}$ weak vertex, its
$10$-crossing budget, the $\mathbb{Z}/2$ involution relating
$\beta^\pm$, the lepton-pair decomposition, and the $10$-crossing
$Q$-value.

**Setup.**
A nucleus $\mathcal{N}(Z, N)$ is a satellite link of $A = Z + N$
Borromean components ([stable nucleus](#def:stable-nucleus)).
Its braid word in $B_{3A}$ reduces to a unique Gröbner--Shirshov normal form
$\mathcal{N}(Z, N)$ in the Iwahori--Hecke algebra $H_{3A}(q)$
([nuclear Gröbner--Shirshov reduction](#prop:nuclear-groebner-reduction)).

Each nucleon is a Borromean link $\mathcal{B}_3(q_1, q_2, q_3)$
with quark strands:
- Proton: $\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$
 ([categorical proton](#def:categorical-proton))
- Neutron: $\mathfrak{n} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$
 ([categorical neutron](#def:categorical-neutron))

The crossing type at each generator $\sigma_i$ depends on the
quark flavours of the two strands: $\mathfrak{u}\text{-}\mathfrak{u}$ (positive), $\mathfrak{d}\text{-}\mathfrak{d}$
(negative), or $\mathfrak{u}\text{-}\mathfrak{d}$ (mixed).

## The $T_{3,5}$ weak vertex

The weak interaction is mediated by the torus knot $T_{3,5}$
([force identification](#rem:force-knot-identification)), whose
braid word in $B_3$ is:

$$
  \beta_{T_{3,5}} =  (\sigma_1 \sigma_2)^5
$$

This word has **$10$ crossings**. In the Iwahori--Hecke algebra $H_3(q)$,
the Hecke reduction of $(\sigma_1 \sigma_2)^5$ eliminates squares
via $T^2 = (q - q^{-1})T + 1$, producing a polynomial in the
reduced basis of $H_3(q)$. The Markov trace of this polynomial
is the **weak vertex form factor**:

$$
  \mathcal{W}(q)
   := 
  \mathrm{tr}_{\mathrm{Markov}}\bigl((\sigma_1 \sigma_2)^5\bigr)
   \in  \mathbb{Z}[q^{\pm 1/2}]
$$

The single-crossing Skein amplitude $s = q^{1/2} - q^{-1/2}$
appears as the coupling at each crossing of the $T_{3,5}$ braid.
The full vertex factor is **not** $s^2$ (single crossing) but
the Markov trace $\mathcal{W}(q)$ of all $10$ crossings.

## The $10$-crossing budget

When the $T_{3,5}$ braid is inserted at the converting quark,
it introduces $10$ crossings into the nuclear braid word. These
$10$ crossings are resolved by the Gröbner--Shirshov reduction into three
components:

| Crossings | Destination | Structure |
|:---------:|-------------|-----------|
| $3$ | Electron $T_{2,3}$ (trefoil) | $3$ positive crossings |
| $0$ | Antineutrino $K_{0_1}$ (unknot) | Trivial topology |
| $7$ | Nuclear re-reduction | R2 moves absorbed into daughter normal form |

The $7$ re-reduction crossings change the R2 step count between
parent and daughter normal forms. This is the dominant
contribution to the $Q$-value
([transition energy](#def:Q-value-transition)) — the single-crossing
approximation misses $6$ of these $7$ crossings.

## Crossing partition and the Skein relation

The $10$ crossings of $T_{3,5}$ are partitioned by the
Gröbner--Shirshov reduction: $3$ form the electron trefoil, $0$ form the
neutrino unknot, and $7$ are absorbed as R2 moves into the
daughter nuclear braid.

In the Skein relation at each of the $10$ crossings:

$$
  q  [L_+] -  q^{-1} [L_-]
  =  (q^{1/2} - q^{-1/2})  [L_0]
$$

The accumulated effect of $10$ such relations (not $1$) determines
the transition amplitude.

## The $\mathbb{Z}/2$ symmetry

$\beta^-$ and $\beta^+$ are related by the involution
$q \mapsto q^{-1}$ on the Iwahori--Hecke algebra, which acts as:

| $\beta^-$ | $\beta^+$ |
|:---:|:---:|
| $\mathfrak{d} \to \mathfrak{u}$ via $T_{3,5}$ | $\mathfrak{u} \to \mathfrak{d}$ via $T_{3,5}^{\sigma}$ |
| $q  [L_+]$ | $q^{-1} [L_+]$ |
| electron $T_{2,3}$ | positron $T_{2,3}^{\sigma}$ |
| antineutrino $K_{0_1}^{\sigma}$ | neutrino $K_{0_1}$ |
| $\mathcal{S}_{ab}(q)$ | $\mathcal{S}_{ba}(q) = \mathcal{S}_{ab}(q^{-1})$ |

This $\mathbb{Z}/2$ acts on the pair Skein mass formula:

$$
  \mathcal{S}_{ab}(q)
  = \frac{q \mu_a + q^{-1} \mu_b}{q^{1/2} + q^{-1/2}}
  \xrightarrow{q \leftrightarrow q^{-1}} 
  \mathcal{S}_{ba}(q)
  = \frac{q \mu_b + q^{-1} \mu_a}{q^{1/2} + q^{-1/2}}
$$

When $\mu_a \neq \mu_b$ (i.e., $\mu_{\mathfrak{u}} \neq \mu_{\mathfrak{d}}$), the two
are distinct: the asymmetry $\mathcal{S}_{ab} - \mathcal{S}_{ba} = (q - q^{-1})(\mu_a - \mu_b)/(q^{1/2} + q^{-1/2})$ is the
**weak asymmetry** that drives the $Q$-value.

## The lepton pair from $T_{3,5}$ decomposition

The $T_{3,5}$ braid $(\sigma_1 \sigma_2)^5$ decomposes under
Gröbner--Shirshov reduction into the lepton pair plus reduction residue.
The electron trefoil $T_{2,3} = (\sigma_1)^3$ accounts for $3$ of
the $10$ crossings; the antineutrino unknot $K_{0_1}$ accounts
for $0$. The remaining $7$ crossings are the **weak vertex
residue** — absorbed into R2 moves during re-reduction.

$$
  L_0^{-} =  T_{2,3} \sqcup T_{1,0}^{\sigma}
  \qquad (\beta^- \text{ decay: } e^- + \nu_e^{\sigma})
$$

$$
  L_0^{+} =  T_{2,3}^{\sigma} \sqcup T_{1,0}
  \qquad (\beta^+ \text{ decay: } e^+ + \nu_e)
$$

## The $Q$-value (10-crossing)

The transition energy is the difference in categorical actions
between parent and daughter, now accounting for all $10$
crossings of the $T_{3,5}$ insertion:

$$
  Q
  = 
  \mathfrak{S}_q[\mathcal{N}(Z, N)]
  - 
  \mathfrak{S}_q[\mathcal{N}(Z \pm 1, N \mp 1)]
  - 
  m_e
$$

The parent and daughter normal forms differ at all crossings
affected by the $T_{3,5}$ insertion and its subsequent
re-reduction — not the single converting crossing. The
$7$ re-reduction crossings from the weak vertex residue modify
inter-nucleon crossing types at the converting quark's strand,
changing $\binom{A-1}{1} \cdot 3$ inter-nucleon crossings
(one per quark strand of each partner nucleon).

**Re-reduction cost (10-crossing).**
After the $T_{3,5}$ insertion at the converting quark, the braid
word gains $10$ crossings. The Gröbner--Shirshov reduction must:

1. Extract the $3$-crossing electron trefoil from the
 $T_{3,5}$ decomposition.
2. Reduce the remaining $7$ crossings via R2 moves
 ($T^2 = (q - q^{-1})T + 1$) and R3/far-commutativity moves.
3. Propagate the flavour change through all inter-nucleon crossings
 involving the converting quark's strand.

The net R2 step count from all $10$ crossings (not just $1$)
determines the $Q$-value:

$$
  Q =  \Delta(\text{R2 steps from 10 crossings})
   \times  (q - q^{-1})
   \times  (\text{pair Skein scale})
$$

## Why single-crossing was insufficient

The previous single-crossing approximation captured only $1$
of the $10$ crossings in the weak vertex. This explains:

1. **Systematic overshoot** of $10$–$17\%$ in heavy-nucleus
 half-life predictions: the missing $9$ crossings contribute
 additional phase space that shortens the predicted half-life
 when properly included.

2. **Tritium accuracy** ($< 2\%$ error): for $A = 3$, the
 nuclear braid is short enough that the $7$ re-reduction
 crossings have limited room to propagate — the single-crossing
 approximation is accidentally good.

3. **Mass-dependent correction**: heavier nuclei have more
 inter-nucleon crossings affected by the converting quark's
 flavour change, so the $7$ re-reduction crossings modify
 more transfer matrices.

**Open computation:** The exact weak vertex form factor
$\mathcal{W}(q) = \mathrm{tr}_{\mathrm{Markov}}((\sigma_1\sigma_2)^5)$
and the crossing budget ($3 + 0 + 7$) must be
verified by explicit Iwahori--Hecke algebra computation of the $T_{3,5}$
braid word reduction.
