Both ${}^{14}\mathrm{N}$ and ${}^{14}\mathrm{C}$ have mass number
$A = 14$ and share the same braid word skeleton
$(\sigma_1 \cdots \sigma_{13})^2$ with 26 crossings.  They differ
only in the **crossing chirality assignment**: which crossings are
same-species (weight $q$ or $q^{-1}$) and which are mixed (weight
$(q + q^{-1})/2$).

**Crossing comparison.**

| | $\mathcal{N}^{\mathrm{thr}}(7,7)$ | $\mathcal{N}^{\mathrm{thr}}(6,8)$ |
|---|:---:|:---:|
| Mixed crossings | 26 (all) | 22 |
| Same-species | 0 | 4 ($\mathfrak{n}$-$\mathfrak{n}$) |
| Coulomb excess | 0 | $-2(q - q^{-1})$ |
| Pauli cost | 0 | $(n-p)^2/(4A)$ asymmetry |

**Ground-state character of $\mathcal{N}(7,7)$.**
With $p = n = 7$, every crossing in the braid word is a
$\mathfrak{p}$-$\mathfrak{n}$ mixed crossing.  The mixed
crossing weight $(q + q^{-1})/2 \approx 1.005$ is the **average**
of the positive weight $q = q_0$ and negative weight
$q^{-1} = 0.901$.  No crossing carries the Coulomb penalty
$(q - q^{-1})/2 \approx 0.105$ and no crossing carries the
attractive excess $-(q - q^{-1})/2$.

This is the **maximal braid shortcut**: all 26 crossings
contribute identically, the Hecke reduction encounters no
$\sigma_i^2$ terms (because the alternation prevents any
generator from appearing twice consecutively), and the
Gröbner--Shirshov normal form is maximally efficient.

**Instability of $\mathcal{N}(6,8)$.**
With $p = 6, n = 8$, the 8 neutrons include 4
$\mathfrak{n}$-$\mathfrak{n}$ crossings (between neutrons 7–8,
7–9, etc.) that break the alternation pattern.  These same-species
crossings carry weight $q^{-1}$ instead of $(q + q^{-1})/2$:

1. **Coulomb deficit**: the 4 same-species crossings lack the
   electromagnetic contribution $(q - q^{-1})/2$, creating a
   net Coulomb excess of $-2(q - q^{-1}) \approx -0.42$ in
   Skein weight.

2. **Pauli asymmetry cost**: the $(n - p)^2 / (4A) = 4/56$
   asymmetry penalty from the Skein binding Lagrangian
   ([Skein binding Lagrangian](#def:skein-binding-lagrangian))
   adds an asymmetry energy from the antisymmetric product cost
   in the matter sector of the categorical action.

3. **Hecke reduction cost**: the same-species crossings produce
   $\sigma_i^2$ terms in the braid word (when two neutron
   crossings appear at the same generator), requiring Hecke
   reductions $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ that
   increase the energy.

The fractional ideal volume at the converting generator
([generator volume decomposition](#prop:generator-volume-decomposition))
captures this: $e(I)/e(R) = 0.1563$, matching the Q-value of
$0.156$ MeV
([hadron half-life verification](#ex:hadron-half-life-verification)).

**The transition ${}^{14}\mathrm{C} \to {}^{14}\mathrm{N}$.**
Beta decay converts one neutron to a proton, turning 4
same-species crossings into 4 mixed crossings.  The braid word
goes from $(\sigma_1 \cdots \sigma_{13})^2$ with 4 broken
alternations to $(\sigma_1 \cdots \sigma_{13})^2$ with perfect
alternation — the maximal shortcut.

In the Iwahori--Hecke algebra, this transition:
- Eliminates 4 Hecke reduction steps ($\sigma_i^2$ resolutions)
- Reduces the total energy by $\Delta E = -3.361$ Skein weight
  units
- Releases the Pauli asymmetry cost and Coulomb deficit as the
  decay $Q$-value

The half-life of $5730$ years reflects the $n = 8$ shell
structure that stabilises the broken-alternation configuration
([shell-structure worked examples](#ex:half-life-shell-worked)).
