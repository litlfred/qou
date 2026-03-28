**Beta decay is the Skein relation applied to one crossing of
the Gröbner normal form.**

The weak force in the Descartes universe ($\chi(A) = -6$,
$q = 1.1097$) is not a separate interaction — it is the Skein
relation acting on the braid word of a nucleus.

**Setup.**
A nucleus $\mathcal{N}(Z, N)$ is a satellite link of $A = Z + N$
Borromean components ([stable nucleus](#def:stable-nucleus)).
Its braid word in $B_{3A}$ reduces to a unique Gröbner normal form
$\bar{\mathcal{N}}(p, n)$ in the Hecke algebra $H_{3A}(q)$
([nuclear Gröbner reduction](#prop:nuclear-groebner-reduction)).

Each nucleon is a Borromean link $\mathcal{B}_3(q_1, q_2, q_3)$
with quark strands:
- Proton: $\mathfrak{p} = \mathcal{B}_3(u, u, d)$
  ([categorical proton](#def:categorical-proton))
- Neutron: $\mathfrak{n} = \mathcal{B}_3(u, d, d)$
  ([categorical neutron](#def:categorical-neutron))

The crossing type at each generator $\sigma_i$ depends on the
quark flavours of the two strands: $u$-$u$ (positive), $d$-$d$
(negative), or $u$-$d$ (mixed).

**Definition ($\beta^-$ decay).**
*A $\beta^-$ transition is a single Skein crossing change*
$d \to u$ *in the normal form* $\bar{\mathcal{N}}(p, n)$*,*
*followed by re-reduction to the daughter normal form:*

$$
  \bar{\mathcal{N}}(p, n)
  \;\xrightarrow{\;\text{Skein at } \sigma_k\;}
  \bar{\mathcal{N}}(p + 1, \, n - 1)
  \;\sqcup\;
  L_0^{-}
$$

where $\sigma_k$ is the generator at the converting $d$-quark
crossing, and $L_0^{-}$ is the Skein smoothing (the superscript
matches $\beta^-$).

In the Skein relation:

$$
  q \, [\bar{\mathcal{N}}(p, n)]
  \;-\;
  q^{-1} [\bar{\mathcal{N}}(p+1, n-1)]
  \;=\;
  (q^{1/2} - q^{-1/2}) \, [L_0^{-}]
$$

- $L_+$: the parent normal form (the $d$-$d$ crossing at $\sigma_k$
  is a negative crossing in the Hecke algebra)
- $L_-$: the daughter normal form (the $u$-$d$ or $u$-$u$ crossing
  after the $d \to u$ change)
- $L_0^{-}$: the smoothing — the **emitted lepton pair** ($e^- + \bar{\nu}_e$)

**Definition ($\beta^+$ decay).**
*A $\beta^+$ transition is the mirror operation:* a single
Skein crossing change $u \to d$:

$$
  \bar{\mathcal{N}}(p, n)
  \;\xrightarrow{\;\text{Skein at } \sigma_k\;}
  \bar{\mathcal{N}}(p - 1, \, n + 1)
  \;\sqcup\;
  L_0^{+}
$$

The mirror Skein relation (with $q \leftrightarrow q^{-1}$):

$$
  q^{-1} [\bar{\mathcal{N}}(p, n)]
  \;-\;
  q \, [\bar{\mathcal{N}}(p-1, n+1)]
  \;=\;
  (q^{-1/2} - q^{1/2}) \, [L_0^{+}]
$$

**The $\mathbb{Z}/2$ symmetry.**
$\beta^-$ and $\beta^+$ are related by the involution
$q \mapsto q^{-1}$ on the Hecke algebra, which acts as:

| $\beta^-$ | $\beta^+$ |
|:---:|:---:|
| $d \to u$ | $u \to d$ |
| $q \, [L_+]$ | $q^{-1} [L_+]$ |
| electron $T_{2,3}$ | positron $\sigma(T_{2,3})$ |
| antineutrino $\bar{K}_{0_1}$ | neutrino $K_{0_1}$ |
| $\mathcal{S}_{ab}(q)$ | $\mathcal{S}_{ba}(q) = \mathcal{S}_{ab}(q^{-1})$ |

This $\mathbb{Z}/2$ acts on the pair Skein mass formula:

$$
  \mathcal{S}_{ab}(q)
  = \frac{q \mu_a + q^{-1} \mu_b}{q^{1/2} + q^{-1/2}}
  \;\;\xrightarrow{\;q \leftrightarrow q^{-1}\;}\;\;
  \mathcal{S}_{ba}(q)
  = \frac{q \mu_b + q^{-1} \mu_a}{q^{1/2} + q^{-1/2}}
$$

When $\mu_a \neq \mu_b$ (i.e., $\mu_u \neq \mu_d$), the two
are distinct: the asymmetry $\mathcal{S}_{ab} - \mathcal{S}_{ba}
= (q - q^{-1})(\mu_a - \mu_b)/(q^{1/2} + q^{-1/2})$ is the
**weak asymmetry** that drives the $Q$-value.

**The lepton pair $L_0^{\pm}$.**
The Skein smoothing at a Borromean crossing produces exactly
two link components.  The sign on $L_0$ matches the decay type:

$$
  L_0^{-} \;=\; T_{2,3} \;\sqcup\; \overline{T_{1,0}}
  \qquad (\beta^- \text{ decay: } e^- + \bar{\nu}_e)
$$

$$
  L_0^{+} \;=\; \overline{T_{2,3}} \;\sqcup\; T_{1,0}
  \qquad (\beta^+ \text{ decay: } e^+ + \nu_e)
$$

This is the **categorical origin of the weak force**: the
Skein relation decomposes one nuclear crossing into a daughter
nucleus plus a lepton pair.  No separate weak boson or $W^{\pm}$
field is postulated — the Skein relation itself is the weak
interaction.

**The $Q$-value.**
The transition energy is the difference in categorical actions
between parent and daughter:

$$
  Q_\beta
  \;=\;
  \mathcal{S}_q[\bar{\mathcal{N}}(p, n)]
  \;-\;
  \mathcal{S}_q[\bar{\mathcal{N}}(p \pm 1, n \mp 1)]
  \;-\;
  m_e
$$

The parent and daughter masses are **not assumed equal**.
They differ because the normal forms $\bar{\mathcal{N}}(p, n)$
and $\bar{\mathcal{N}}(p \pm 1, n \mp 1)$ have different
crossing structures, different R2 step counts, and different
Markov traces.  The difference is small (order $Q/M \sim 10^{-5}$
for typical nuclei) but it is the entire signal.

**Re-reduction cost.**
After the crossing change $d \to u$ at $\sigma_k$, the braid word
is no longer in Gröbner normal form.  Re-reduction to
$\bar{\mathcal{N}}(p+1, n-1)$ requires a specific sequence of
$q$-deformed R2 moves ($T^2 = (q - q^{-1})T + 1$)
and R3/far-commutativity moves.  The R2 moves change the
gauge-sector action; the R3 and far-commutativity moves
do not ([Reidemeister action table](#prop:reidemeister-action-table)).

The net change in R2 step count between parent and daughter
normal forms determines the $Q$-value:

$$
  Q_\beta \;=\; \Delta(\text{R2 steps}) \;\times\;
  (q - q^{-1}) \;\times\; (\text{pair Skein scale at } \sigma_k)
$$

This is exact — no approximation, no fitted parameter.
