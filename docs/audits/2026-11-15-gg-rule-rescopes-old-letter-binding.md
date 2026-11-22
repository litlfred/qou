# The γγ rule re-scopes the old-letter binding numbers

**Date.** 2026-11-15
**Rulings.**
- Owner decision A (2026-11-15): the γγ (pair-production) selection rule also covers the nuclear bond letters. No bond letter is exempt.
- Owner choice on the follow-up card the same day: *"Re-scope now, redo after #7876."*

**Bean.** `qou-brng`, plus the 30 beans listed below.

## What is no longer canonical

These numbers were computed on the single-crossing interface letters `g_{3k+2} + d_k`, which `atom_braid_word_3A` lays between nucleons. The γγ rule does not select those letters, so the numbers are **records of a superseded word**, not current results:

- the interface shifts `d_k` and the letter traces `μ_e`;
- the chain law `tr(atom)/tr(free) = ∏(z_D + d_k)`;
- the `b₃` magnitudes at the live chain bonds: `−1.2277` MeV (³H) and `−0.7973` MeV (³He);
- every sign map or magnitude computed from `atom_braid_word_3A` (for example the Magnus Ω₂ sign map A2 −, A3 +, A4 + in `qou-o6ov`).

They are kept as recorded, not deleted, and nothing numeric was changed in this PR.

## What still stands

The Lean results are stated for **generic bond weights** over a generic ring, so they do not depend on which letters supply the weights:

- `UrsellPartitionFunctionB3`: `b₃ = −φᵀ₃` and the Ursell alternation, so `b₃ < 0` for every bond triple in `(0,1)³`.
- `B3SignOneRoot`: a two-bond chain needs exactly one bond above 1.
- `MayerThreeBodySign` and `AggregatorConvexity`.

These theorems apply to the γγ word's bonds as soon as those bonds are known. Whether those bonds land in `(0,1)` is exactly what the redo has to measure.

## Redo

The redo waits on a γγ-selected word per nucleus (SM thread, PR #7876). A candidate word exists in PR #7741 (`computations/probes/h2_gg_atom/results.md`, `V = σ₀σ₁⁻¹`): only `V³` and `V⁶` pass reading 3, p and n become the same word, and the H₂ bond letters that pass are `V³`. That word is a **candidate, not ruled**, and nothing here adopts it.

Once a word is ruled, the redo recomputes `μ_e`, `b₃` for ³H and ³He, and the chain law on it, and re-checks every bean below against those numbers.

## Affected beans

- `qou-17mq`: EM-linking O2 (neutrality obstruction): on a COMPACT quotient int(Laplacian u)=0 forces to
- `qou-1pig`: The pair layer is a LINEAR RAMP in neutron count, not an isospin structure — B_nn > B_pn >
- `qou-2ss0`: b3Agg''s sign IS the origin-secant gap: an exact iff replacing two one-way convexity impli
- `qou-5c64`: binding-single-pipeline-comparison is 3 months stale and RED when re-run — 2 assertions fl
- `qou-6hm4`: confinement-topological-proof part (i): wrong lambda_-, unlabelled lambda_0 = 0, and a des
- `qou-8r6b`: Pose the composition feasibility program: variable = interface letter (1−e)σ + eσ⁻¹, feasi
- `qou-8uxw`: Route C step 1: groupoid-cardinality reading of the q=1 component-count cross term (Baez–H
- `qou-ales`: OWNER RULING 2026-09-08: braid-word selection via gamma-gamma production + confinement SDP
- `qou-brng`: OPEN KERNEL: derive that the saturated nuclear binding fraction = ℏ_q² (mass/binding rung)
- `qou-cgyn`: The per-generator volume route is grouped-era by construction and cannot express the borro
- `qou-d0qq`: Step-2 option C (research): the sl2 KZ connection on Conf3(C) pulled back along the colour
- `qou-edt7`: GAP: what replaces the multiplicative assembly W=1-PROD f — both corpus assemblies miss th
- `qou-gr3t`: GAP: general-A bond factorisation for the canonical NON-monotone word — Lean for disjoint 
- `qou-hu1f`: The full-tower ruling has not been applied to the mass/binding surface, where H_3 is the w
- `qou-ix0x`: The binding's divergent series is G, its Borel-Stokes plane is EMPTY, and the untried summ
- `qou-kgsx`: GAP: explain why delta is A-independent while the interface-letter count grows (bar-involu
- `qou-m0bv`: GAP: 4 particle-existence blocks prove a degenerate witness (zero-mass proton, two-unknot 
- `qou-m8f3`: Dominant-summand extensive test: Ursell-invert log|y_λ χ^λ(β_A)| of the trace''s dominant 
- `qou-pjx4`: sigma^2 unbinding is framing-dependent; even-NEGATIVE stacking unbinds after writhe normal
- `qou-q8vl`: b_3''s three-way wrong sign has ONE root: every derived bond scalar is confined to (0,1), 
- `qou-q9ih`: D1: Route C M1 — construct the (Q,W) reproducing {3,4} + bar split (7,1); fitted quiver = 
- `qou-qjhc`: GAP: identify the duality involution on PGL(3,C) reps with the sigma-transport on Ptolemy 
- `qou-qqm4`: DERIVE c2: the second-order hbar_q coefficient of the trace difference -- and why the pair
- `qou-rwhv`: Is the corpus b3 an Ursell function? The alternating-sign theorem says the sign obstructio
- `qou-tower`: There is no tower: the production chain reduces every nucleus to the same 6 dims
- `qou-u5qs`: gamma-gamma production DERIVES the contiguous strand layout, uniquely — and that is why th
- `qou-vtlj`: Delta is not a two-way fork: the corpus carries FOUR net values, and the "13 crossings" se
- `qou-vwu3`: Is the Markov-trace bond-multiplicativity defect CHARGE-sensitive? The n=4 cross term is d
- `qou-xf14`: PINNED: the normaliser convention is delta = [2]_q, forced by the identity sqrt(b_pp.b_nn)
- `qou-zlra`: Is graded binding +c_k or -c_k? The sign convention the type-two result hangs on
- `qou-o6ov`: Magnus Ω₂ trace decay (sign map on the old word)
