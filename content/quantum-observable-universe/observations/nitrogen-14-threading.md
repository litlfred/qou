Both ${}^{14}\mathrm{N}$ and ${}^{14}\mathrm{C}$ possess mass number
$A = 14$ and share the braid word skeleton $(\sigma_1 \cdots \sigma_{13})^2$
(26 crossings). They differ exclusively in crossing chirality assignment:
which crossings are same-species (weight $q$ or $q^{-1}$) and which are
mixed (weight $(q + q^{-1})/2$).

**Crossing comparison.**

| | $\mathcal{N}^{\mathrm{thr}}(7,7)$ | $\mathcal{N}^{\mathrm{thr}}(6,8)$ |
|---|:---:|:---:|
| Mixed crossings | 26 (all) | 22 |
| Same-species | 0 | 4 ($\mathfrak{n}$-$\mathfrak{n}$) |
| Coulomb excess | 0 | $-2(q - q^{-1})$ |
| Pauli cost | 0 | $(n-p)^2/(4A)$ asymmetry |

**Ground-state character of $\mathcal{N}(7,7)$.**
For $p = n = 7$, every crossing is a $\mathfrak{p}$-$\mathfrak{n}$ mixed
crossing. The mixed crossing weight $(q + q^{-1})/2 \approx 1.005$ averages
the positive weight $q = q_0$ and the negative weight $q^{-1} = 0.901$.
No crossing incurs the Coulomb penalty $(q - q^{-1})/2 \approx 0.105$, and
none carries the attractive excess $-(q - q^{-1})/2$.

This constitutes the maximal braid shortcut: all 26 crossings contribute
identically. The alternation prevents any generator from appearing twice
consecutively, so the Hecke reduction encounters no $\sigma_i^2$ terms,
rendering the Gröbner--Shirshov normal form maximally efficient.

**Instability of $\mathcal{N}(6,8)$.**
For $p = 6$ and $n = 8$, the 8 neutrons generate 4 $\mathfrak{n}$-$\mathfrak{n}$
crossings (e.g., between neutrons 7–8, 7–9) that break alternation. These
same-species crossings carry weight $q^{-1}$ rather than $(q + q^{-1})/2$,
introducing three penalties:

1. **Coulomb deficit**: The 4 same-species crossings lack the electromagnetic
   contribution $(q - q^{-1})/2$, creating a net Coulomb excess of
   $-2(q - q^{-1}) \approx -0.42$ in Skein weight.
2. **Pauli asymmetry cost**: The $(n - p)^2 / (4A) = 4/56$ asymmetry penalty
   from the Skein binding Lagrangian
   ([Skein binding Lagrangian](#def:skein-binding-lagrangian)) contributes an
   antisymmetric product cost in the categorical action's matter sector.
3. **Hecke reduction cost**: The same-species crossings produce $\sigma_i^2$
   terms. Resolving these via the Hecke relation
   $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ increases the total energy.

The fractional ideal volume at the converting generator
([generator volume decomposition](#prop:generator-volume-decomposition))
evaluates to $e(I)/e(R) = 0.1563$. This matches the observed Q-value of
$0.156$ MeV
([hadron half-life verification](#ex:hadron-half-life-verification)).

**The transition ${}^{14}\mathrm{C} \to {}^{14}\mathrm{N}$.**
Beta decay converts one neutron to a proton, substituting 4 mixed crossings
for 4 same-species crossings. The braid word transforms from a broken
alternation into perfect alternation (the maximal shortcut).

Within the Iwahori--Hecke algebra, this transition:
- Eliminates 4 Hecke reduction steps ($\sigma_i^2$ resolutions).
- Lowers the total energy by $\Delta E = -3.361$ Skein weight units.
- Releases the Pauli asymmetry cost and Coulomb deficit as the decay $Q$-value.

The half-life of 5730 years reflects the $n = 8$ shell structure stabilizing
the broken-alternation configuration
([shell-structure worked examples](#ex:half-life-shell-worked)).
