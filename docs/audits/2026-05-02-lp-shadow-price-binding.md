# LP/SDP shadow-price binding — replacing scheme-fitted hybrid

## User directive

> "don't like scheme fitting. should be shadow prices or SDP or so.
> you should see the knot operator. you should be able to detect
> most receptive sub-braids on the shell to determine what are
> input braids."

The per-braid hybrid hand-picks sub-braids (single-nucleon, pp/nn/pn
pairs) and characters (q-Hecke vs q=1 MN) per term. Even with no
numerical fits, scheme-selection IS soft fitting. The framework's
principled answer is the **operator-selection LP**.

## Framework's principled mechanism

`prop:operator-selection-lp`
([content](../../content/quantum-observable-universe/particle-interactions/operator-selection-lp.md))
formulates an LP at $H_n(q)$:

**Primal**: minimize $\sum_i t_i x_i = \mathrm{tr}_M(\Phi)$
subject to:
- net constraint: $\sum_i x_i = n_{\text{target}}$
- Frobenius positivity: $\sum_j G_{ij} x_j \geq 0$ for all $i$
- boundedness

where $\{b_i\}$ is the NF basis of $H_n(q)$, $t_i = \mathrm{tr}_M(b_i)$,
$G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$, and $n_{\text{target}}$ is
the target categorical mass.

**Output**: optimal $\Phi^* = \sum_i x_i^* b_i$ — the **knot operator**
(this is what the user wants to "see"). The dual variables $y_i^* > 0$
identify the **active demand channels** $\mathcal{A}$ — the
"most receptive sub-braids" the user wants detected.

**Strong duality**: $\sum_i t_i x_i^* = n_{\text{target}} \cdot y_0^*$
(no duality gap; categorical action = target mass × shadow price of
net constraint).

## Existing infrastructure

| script | scope | status |
|--------|-------|:------:|
| `confinement-operator-selection.py` | LP at $H_3(q)$ | ✅ working |
| `lp-duality-check.py` | dual verification | ✅ |
| `sdp_on_shadows.py` | SDP version | ✅ |
| `sdp_multi_level.py` | multi-level SDP | partial |
| `sdp_knot_match.py` | knot-match SDP | ✅ |

The H_3 case reproduces proton (target 0.999) and neutron (target 0.811)
NF coefficients to ~5e-5 accuracy. The active channel set at H_3 is
$\mathcal{A} = \{\sigma_0, L_-\}$ — two demand channels.

## What's needed for per-atom binding

For atom $(Z, N)$: run LP at $H_{3A}(q)$ with $n_{\text{target}}$ =
AME mass / $m_e$. The LP optimum gives:
- $\Phi^*(Z, N)$ = the categorical mass operator (bound state)
- $y_0^*(Z, N)$ = mass per unit target (calibration constant)
- $\mathcal{A}(Z, N)$ = active sub-braids (the "input braids")

**Tractability**: $\dim H_{12}(q) = 12! = 479M$ — direct LP infeasible.
The shadow-price reduction solves this: most $y_i^* = 0$ (Frobenius
constraint inactive), so the effective basis is small.

**Iterative reduction approach**:

1. Start at $H_3$ — solve LP, get active set $\mathcal{A}_3$.
2. Lift to $H_6$ via braid extension: $b_i \otimes b_j$ for
   $b_i, b_j \in \mathcal{A}_3$. Solve LP on this reduced basis.
3. Iterate to $H_{3A}$ — at each step the active set bounds basis
   growth.

This is the **principled alternative** to my per-braid hybrid — no
hand-picked sub-braids, the LP self-determines the active channels
from $G$ and $t$.

## Why this captures binding (the missing knot operator)

The per-braid hybrid's level-0 formula is $\Phi^{(0)} = \sum_i t_i b_i$
with hand-picked $\{b_i\}$ and unit weights. This is the FREE-ATOM
operator — every basis element gets unit weight, no constraint
satisfaction.

The LP optimizer $\Phi^* = \sum_i x_i^* b_i$ picks weights that
satisfy Frobenius positivity (no channel over-saturated). The
**reduction** $\sum_i t_i x_i^* < \sum_i t_i$ (LP minimum vs naive
sum) IS the binding energy — saturating channels efficiently
*subtracts* mass via the Frobenius constraint.

This matches the user's hint: "real bind via knot operator that
reduces binding energy". The LP optimizer IS that knot operator;
its reduction below the naive sum is the binding.

The operator $\Phi^*$ "may not be observable" — it's a transition
operator (Hecke algebra element selecting the bound state), not a
measurable observable in the standard QM sense. Matches user's
"may not be observable not operator" framing.

## Implementation path

1. **Probe at $H_6$** (4He = 2 nucleons × 3 strands = $H_6$, dim 720).
   Build LP with Markov traces + Gram matrix at q_0; solve; report
   $\Phi^*$ + $\mathcal{A}_6$ + $y_0^*$. Compare $y_0^*$ to AME(4He)/m_e.
2. **Iterate to $H_{12}$ via reduced basis** from $\mathcal{A}_6$.
3. **Replace per_braid_tower_hybrid.py** with this LP-driven mass
   formula. Rename: `per_braid_mass_lp.py` or `lp_shadow_mass.py`.

## Status

Hand-built per-braid hybrid (current) is **scheme-fitting**. The
LP/SDP shadow-price approach (framework-prescribed) is the
**principled** alternative. Existing H_3 LP infra works; extension
to per-atom $H_{3A}$ requires shadow-price-driven basis reduction
(research-grade implementation, ~1-2 weeks).

This is the actual closer for the cal/m_e spread — the LP's
strong-duality-derived $y_0^*$ should match AME/m_e per atom
WITHOUT scheme selection.
