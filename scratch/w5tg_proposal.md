# w5tg Proposal: Resolving the Z·N p-n Occupancy Gate

## 1. Problem Statement & Current State
Bean `w5tg` tracks the need for an edge-set/occupancy model that moves beyond the static complete-graph integer model (`n_pn = Z·N`). 
As implemented in `computations/channel_binding.py`, the complete graph assigns exactly $Z \cdot N$ proton-neutron bonds. `computations/binding_factor_f_pair_count.py` demonstrates this static integer count brackets the non-magic light nuclei (D, 6Li, 7Li) to within 1% with zero free parameters. However, it severely overbinds at scale (growing as $\mathcal{O}(A^2)$) and lacks the required saturation mechanisms (halo-D, magic-$\alpha$ blockers).

## 2. The s5-so3 Keystone Blocker
The true occupancy model cannot be phenomenologically guessed or fitted (per the strict anti-numerology rules in `AGENTS.md`). It must be derived canonically from the braid-interface count and operator branching.
As established in the `w5tg` bean, this derivation is gated by the `s5-so3` keystone. Specifically, deriving the macroscopic limits of the operator-combiner branching (which dictates the saturated edge-set) depends fundamentally on the exact geometric origin of the Plancherel weights $W_\lambda$.

## 3. Why Agent-Led Mathematical Resolution is Blocked
According to `docs/coordination/s5-so3-keystone.md` (Update 2026-06-26), Phase G1 of the keystone (the Beasley–Witten Seifert–CS equivariant-index construction on $S^3/2I$) is owner-authorized but remains blocked by "research-level DG" (differential geometry).
Because any attempt to resolve the occupancy model before G1 is closed would require phenomenologically fitting the edge rule or blindly guessing the DG reduction, it violates the repository's strict formalize-first and anti-guessing directives. The agent cannot mathematically close this without violating discipline.

## 4. Proposed Path Forward (Author Assist Required)
To unblock `w5tg`, the following sequence requires author-driven research:

1. **Close Phase G1 (PR #2524):** Complete the rigorous differential-geometric evaluation of the Beasley-Witten CS localization on $S^3/2I$, proving it analytically yields the required Plancherel weights $W_\lambda = d_q^2 / D^2$.
2. **Bridge to Occupancy:** With the geometric index secured, apply the already-verified Frobenius reciprocity rules from `CombinerBranchingCompleteness.lean`.
3. **Derive the Saturation Curve:** Project the geometrically-fixed $W_\lambda$-weighted representation onto the macroscopic inter-nucleon edge set. This will dynamically derive the structural counts for shell closures (magic-$\alpha$ blockers) and valence drops, cleanly replacing the static $Z \cdot N$ bound without introducing any free parameters.

Once the author completes Phase G1, the agent can be re-invoked to formalize the bridge and implement the dynamic occupancy evaluator in `channel_binding.py`.
