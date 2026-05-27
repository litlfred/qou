**Conjecture (meson mass ratio from dual volume).**
*The kaon-to-pion mass ratio admits a formula dual to the muon-to-electron
ratio:*

$$
  \frac{m_K}{m_\pi}
  \;\stackrel{?}{=}\;
  \frac{\mathrm{Vol}_{\mathrm{dual}}(\mathcal{M}_{K})}
       {\mathrm{Vol}_{\mathrm{dual}}(\mathcal{M}_{\pi})}
$$

*where $\mathrm{Vol}_{\mathrm{dual}}$ is a volume functional on the
meson braid evaluated at the lowest-weight (rather than highest-weight)
sector of $H_3(q)$, and $\mathcal{M}_K$, $\mathcal{M}_\pi$ are the
kaon and pion meson braids respectively.*

## Motivation: the lepton precedent

The lepton mass ratio is exact at CAL-2:

$$
  \frac{m_\mu}{m_\mathfrak{e}}
  = \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
  \approx 206.768
$$

where $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ is the hyperbolic
volume of the figure-eight knot complement.  The figure-eight knot $4_1$
is the **transition knot** connecting the first-generation torus knot
$T(2,3)$ (trefoil, electron) to the second-generation $T(2,5)$
(cinquefoil, muon).

The **same torus-knot step** $3 \to 5$ governs the flavor transition
$d \to s$ in the meson sector:

| Lepton ($H_2$) | Quark flavor ($H_3$) |
|---|---|
| $\mathfrak{e}$: $T(2,3)$ | $d$-quark: $T(2,3)^\sigma$ |
| $\mu$: $T(2,5)$ | $s$-quark: $T(2,5)^\sigma$ |
| transition: $4_1$ (figure-eight) | transition: same knot, different evaluation |

The conjecture is that the **same topological transition** (figure-eight
knot) controls both ratios, but evaluated in dual sectors:

- Leptons: highest-weight evaluation ($\sigma^n$, positive crossings)
  → $\mathrm{Vol}(4_1) / \hbar_q^2$
- Mesons: lowest-weight evaluation (Hopf-bound pair, mixed crossings)
  → $\mathrm{Vol}_{\mathrm{dual}}(\cdot)$

## What "dual volume" means

The Kashaev invariant $\langle K \rangle_N$ has two limits:

1. **Highest-weight limit** ($N \to \infty$, $q = e^{2\pi i/N}$):
   $\log|\langle K \rangle_N| / N \to \mathrm{Vol}(K)$ (the
   hyperbolic volume — used for leptons).

2. **Lowest-weight limit** (finite $N$, evaluation at $q_0$):
   the Markov trace $\mathrm{tr}_M(K, q_0)$ — used for baryons
   via the Borromean trace.

The meson sector may require a **mixed evaluation**: the Hopf binding
topology ($L_+$, coefficient $h^2 + 1$) evaluates in the lowest-weight
regime, while the flavor-carrying torus-knot component ($T(2,n)$)
evaluates in the highest-weight regime.  The dual volume would then be:

$$
  \mathrm{Vol}_{\mathrm{dual}}(\mathcal{M})
  = \mathrm{Vol}(\text{flavor knot}) \cdot
    \mathrm{tr}_M(\text{Hopf binding}, q_0)
$$

## Target values

| Quantity | Value | Source |
|---|---|---|
| $m_K / m_\pi$ | $3.5370$ | PDG 2024 ($m_{K^\pm} / m_{\pi^\pm}$) |
| $m_\mu / m_\mathfrak{e}$ | $206.768$ | CODATA (= $\mathrm{Vol}(4_1)/\hbar_q^2$) |
| $\mathrm{tr}_M(\sigma^5) / \mathrm{tr}_M(\sigma^3)$ | $\approx 1.36$ | H₂ Markov trace ratio |
| $(m_K/m_\pi) / ([2]_q)^2$ | $\approx 0.875$ | close to $7/8$, no derivation |

## Open questions

1. **What is the transition knot for the meson sector?** Is it $4_1$
   (same as leptons) or a different knot reflecting the composite
   structure?

2. **Does the Hopf binding contribute a multiplicative volume factor?**
   The meson NF has $L_+$ coefficient $h^2 + 1 = [2]_q^2 - 3$ —
   is this the binding-volume contribution?

3. **Can the meson mass ratio be written as a ratio of Kashaev
   invariants at finite $N$?** This would give an intermediate
   evaluation between the highest-weight (volume) and lowest-weight
   (Markov trace) limits.
