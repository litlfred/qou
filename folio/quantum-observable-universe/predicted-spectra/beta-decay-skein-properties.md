The $\beta$-decay Skein operation requires the $T_{3,5}$ weak vertex, the $10$-crossing budget, the $\mathbb{Z}/2$ involution relating $\beta^\pm$, the lepton-pair decomposition, and the $10$-crossing $Q$-value.

**Setup.**
A nucleus $\mathcal{N}(Z, N)$ is a satellite link of $A = Z + N$ Borromean components. Its braid word in $B_{3A}$ reduces to a unique Gröbner–Shirshov normal form $\mathcal{N}(Z, N)$ in the Iwahori–Hecke algebra $H_{3A}(q)$.

Each nucleon is a Borromean link $\mathcal{B}_3(q_1, q_2, q_3)$ with quark strands:
- Proton: $\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$
- Neutron: $\mathfrak{n} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$

The crossing type at each generator $\sigma_i$ depends on the quark flavours of the two strands. The $\mathfrak{u}\text{-}\mathfrak{u}$ crossing is positive. The $\mathfrak{d}\text{-}\mathfrak{d}$ crossing is negative. The $\mathfrak{u}\text{-}\mathfrak{d}$ crossing is mixed.

## The $T_{3,5}$ weak vertex

The weak interaction is mediated by the torus knot $T_{3,5}$. Its braid word in $B_3$ is:

$$
  \beta_{T_{3,5}} =  (\sigma_1 \sigma_2)^5
$$

This word has $10$ crossings. In the Iwahori–Hecke algebra $H_3(q)$, the Hecke reduction of $(\sigma_1 \sigma_2)^5$ eliminates squares via $T^2 = (q - q^{-1})T + 1$. This produces a polynomial in the reduced basis of $H_3(q)$. The Markov trace of this polynomial is the weak vertex form factor:

$$
  \mathcal{W}(q)
   := 
  \mathrm{tr}_{\mathrm{Markov}}\bigl((\sigma_1 \sigma_2)^5\bigr)
   \in  \mathbb{Z}[q^{\pm 1/2}]
$$

The single-crossing Skein amplitude $s = q^{1/2} - q^{-1/2}$ appears as the coupling at each crossing of the $T_{3,5}$ braid. The full vertex factor is the Markov trace $\mathcal{W}(q)$ of all $10$ crossings, not $s^2$.

## The $10$-crossing budget

The $T_{3,5}$ braid insertion introduces $10$ crossings into the nuclear braid word. Gröbner–Shirshov reduction resolves these crossings into three components:

| Crossings | Destination | Structure |
|:---------:|-------------|-----------|
| $3$ | Electron $e^- = \sigma_0\sigma_1\sigma_0$ (closure: Hopf link) | $3$ positive crossings, a braid factor of the vertex |
| $0$ | Antineutrino $K_{0_1}$ (unknot) | Trivial topology |
| $7$ | Nuclear re-reduction | R2 moves absorbed into daughter normal form |

The $7$ re-reduction crossings change the R2 step count between parent and daughter normal forms. This dominates the $Q$-value. The single-crossing approximation misses $6$ of these $7$ crossings.

## Crossing partition and the Skein relation

Gröbner–Shirshov reduction partitions the $10$ crossings of $T_{3,5}$. The electron word takes $3$. The neutrino unknot takes $0$. The daughter nuclear braid absorbs the remaining $7$ as R2 moves.

The Skein relation acts at each of the $10$ crossings:

$$
  q  [L_+] -  q^{-1} [L_-]
  =  (q^{1/2} - q^{-1/2})  [L_0]
$$

The transition amplitude depends on the accumulated effect of $10$ such relations, not $1$.

## The $\mathbb{Z}/2$ symmetry

The involution $q \mapsto q^{-1}$ on the Iwahori–Hecke algebra relates $\beta^-$ and $\beta^+$. It acts as:

| $\beta^-$ | $\beta^+$ |
|:---:|:---:|
| $\mathfrak{d} \to \mathfrak{u}$ via $T_{3,5}$ | $\mathfrak{u} \to \mathfrak{d}$ via $T_{3,5}^{\sigma}$ |
| $q  [L_+]$ | $q^{-1} [L_+]$ |
| electron $e^- = \sigma_0\sigma_1\sigma_0$ | positron $e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$ |
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

These are distinct when $\mu_a \neq \mu_b$. The asymmetry $\mathcal{S}_{ab} - \mathcal{S}_{ba} = (q - q^{-1})(\mu_a - \mu_b)/(q^{1/2} + q^{-1/2})$ is the weak asymmetry. This drives the $Q$-value.

The pair Skein formula uses the excised convention-C Markov weight $1/(q^{1/2}+q^{-1/2})$. The identification $\mathcal{S}_{ba}(q) = \mathcal{S}_{ab}(q^{-1})$ also relies on that convention: the C denominator is invariant under $q \leftrightarrow q^{-1}$, but the canonical weight $z = q^3/(q^2+1)$ is not. Both statements are convention-C results until the pair-Skein formula is re-derived under the canonical weight.

## The lepton pair from $T_{3,5}$ decomposition

Gröbner–Shirshov reduction decomposes the $T_{3,5}$ braid $(\sigma_1 \sigma_2)^5$ into the lepton pair and a reduction residue. In the generators $\sigma_0, \sigma_1$ the vertex is $(\sigma_0\sigma_1)^5$, and the electron word $e^- = \sigma_0\sigma_1\sigma_0$ ([electron](#def:electron-knot)) is a braid factor of it:

$$
  (\sigma_0\sigma_1)^5 = e^- \cdot \bigl(e^- \cdot (\sigma_0\sigma_1)^2\bigr)
$$

(`QOU.BraidKnot.WeakVertexElectronFactor.weakVertex_eq_electron_mul`). The proof is the braid relation once: $e^- \cdot e^- = \sigma_0\sigma_1\sigma_0 \cdot \sigma_1\sigma_0\sigma_1 = (\sigma_0\sigma_1)^3$, the full twist. So the electron accounts for $3$ of the $10$ crossings as an identity of braids, not only as a count. The antineutrino unknot $K_{0_1}$ accounts for $0$. The remaining $7$ crossings, $e^- \cdot (\sigma_0\sigma_1)^2$, are the weak vertex residue. They are absorbed into R2 moves during re-reduction. The mirror vertex factors the same way through the positron: $(\sigma_0^{-1}\sigma_1^{-1})^5 = e^+ \cdot \bigl(e^+ \cdot (\sigma_0^{-1}\sigma_1^{-1})^2\bigr)$.

$$
  L_0^{-} =  e^- \sqcup T_{1,0}^{\sigma}
  \qquad (\beta^- \text{ decay: } e^- + \nu_e^{\sigma})
$$

$$
  L_0^{+} =  e^+ \sqcup T_{1,0}
  \qquad (\beta^+ \text{ decay: } e^+ + \nu_e)
$$

## The $Q$-value (10-crossing)

The transition energy is the difference in categorical actions between parent and daughter. It accounts for all $10$ crossings of the $T_{3,5}$ insertion:

$$
  Q
  = 
  \mathfrak{S}_q[\mathcal{N}(Z, N)]
  - 
  \mathfrak{S}_q[\mathcal{N}(Z \pm 1, N \mp 1)]
  - 
  m_e
$$

The parent and daughter normal forms differ at all crossings affected by the $T_{3,5}$ insertion and its re-reduction. The $7$ re-reduction crossings from the weak vertex residue modify inter-nucleon crossing types at the converting quark's strand. They change $\binom{A-1}{1} \cdot 3$ inter-nucleon crossings.

**Re-reduction cost (10-crossing).**
The $T_{3,5}$ insertion at the converting quark adds $10$ crossings to the braid word. The Gröbner–Shirshov reduction must:

1. Extract the $3$-crossing electron word $e^-$, a braid factor of the vertex.
2. Reduce the remaining $7$ crossings via R2 moves ($T^2 = (q - q^{-1})T + 1$) and R3/far-commutativity moves.
3. Propagate the flavour change through all inter-nucleon crossings involving the converting quark's strand.

The net R2 step count from all $10$ crossings determines the $Q$-value:

$$
  Q =  \Delta(\text{R2 steps})
   \times  (q - q^{-1})
   \times  (\text{pair Skein scale})
$$

## Insufficiency of the single-crossing approximation

The previous single-crossing approximation captured only $1$ of the $10$ crossings in the weak vertex. This explains:

1. **Systematic overshoot.** Predictions for heavy-nucleus half-lives overshoot by $10$–$17\%$. The missing $9$ crossings contribute phase space. Including them shortens the half-life.
2. **Tritium accuracy.** The error for $A = 3$ is $< 2\%$. The nuclear braid is short. The $7$ re-reduction crossings have limited room to propagate. The single-crossing approximation succeeds accidentally.
3. **Mass-dependent correction.** Heavier nuclei have more inter-nucleon crossings affected by the flavour change. The $7$ re-reduction crossings modify more transfer matrices.

**Open computation.** The braid-level split $3 + 0 + 7$ is the factorisation above. The exact weak vertex form factor $\mathcal{W}(q) = \mathrm{tr}_{\mathrm{Markov}}((\sigma_1\sigma_2)^5)$, and how the $7$-letter residue reduces against a given nucleus, still require explicit Iwahori–Hecke algebra computation.
