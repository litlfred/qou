# Chirality-topology selection — formalized (2026-06-20)

**Status:** audit — formalize-first follow-up to merged PR #2507. Upgrades the
two structural results of
[`2026-06-20-chirality-forces-complete-graph-topology.md`](2026-06-20-chirality-forces-complete-graph-topology.md)
from an empirical RMS comparison to **parameter-free Lean theorems**, per the
AGENTS.md formalize-first probe discipline (state the invariant the whole class
must satisfy; formalize it; let it narrow the claim).

## What #2507 left as prose

The #2507 audit stated two structural results in words:

1. *Chirality and the chain are incompatible* — with p-p/n-n Pauli-unbound, the
   linear chain keeps a single p-n interface bond, so the binding is the constant
   3.89 MeV for every nucleus (no `A`-dependence).
2. *Chirality forces the complete graph* — the surviving p-n pair count is `Z·N`,
   which is genuinely `A`-dependent and gives the best non-fitted RMS (6.19 MeV).

Both are combinatorial facts about *bond counts* once the Pauli channel has
removed the identical-nucleon pairs. They carry **no archimedean input** (no `q₀`,
no `E₀`, no `ℝ`): the channel values only decide *which* bonds survive; the
`A`-dependence is entirely in the count. That is exactly the kind of claim the
formalize-first rule says to pin in Lean before reading anything further into the
numbers.

## The Lean statement

[`content/quantum-observable-universe/lean/QOU/BraidKnot/ChiralityTopologySelection.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/ChiralityTopologySelection.lean)
(namespace `QOU.BraidKnot.ChiralityTopologySelection`, base ring `ℕ`):

| Lean decl | Mirrors |
|---|---|
| `chainPnBonds Z N = if 0<Z ∧ 0<N then 1 else 0` | probe `_counts(...,"chain")["pn"]` |
| `completePnBonds Z N = Z * N` | probe `_counts(...,"complete")["pn"]` |
| `chain_binding_A_independent` | result 1 (chain ⇒ constant in `A`) |
| `complete_pn_strictMono_N` | result 2 (complete ⇒ strictly `A`-dependent) |
| `A_dependence_forces_complete` | the thesis (A-dependence ⇒ not chain) |

`chain_binding_A_independent` is proved by `simp` (the chain count is `1` for any
`Z,N ≥ 1`); `complete_pn_strictMono_N` by the term proof
`Nat.mul_lt_mul_of_pos_left (Nat.lt_succ_self N) hZ` (strict monotonicity of
left-multiplication by a positive `Z`; `completePnBonds` unfolds definitionally
to `Z * ·`); `A_dependence_forces_complete` is the contrapositive — a differing p-n
count between two nuclei contradicts the chain's forced equality, so the chain
cannot host an `A`-dependent Pauli binding. The complete graph is the parameter-free
topology that does (`complete_pn_strictMono_N`).

## What this does and does not buy

- **Does:** makes the topology-selection logic of #2507 a checked theorem, not a
  narrative inference from six data points. The "chain collapses to a constant"
  and "complete graph scales as `Z·N`" claims are now `rfl`/`simp`-level facts,
  decoupled from the substrate channel values.
- **Does not:** touch the numerical accuracy (RMS 6.19 stays in the probe
  witness), propose any production rewire, or address the two residuals
  (⁴He α-cluster 4-body term; deuteron `f_pn=0.588`, owner-gated to the s5-so3
  keystone). No fit, no CAL-4.

## References

- [`2026-06-20-chirality-forces-complete-graph-topology.md`](2026-06-20-chirality-forces-complete-graph-topology.md) — the parent empirical result (PR #2507).
- `computations/probes/chirality_topology_binding_probe.py` — the probe.
- `content/quantum-observable-universe/lean/QOU/BraidKnot/ChiralityTopologySelection.lean` — this formalization.
