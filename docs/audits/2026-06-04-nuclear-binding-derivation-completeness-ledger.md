# Nuclear binding — derivation-completeness ledger (100% standard)

**Standard:** *fully derived, no guessing / fitting / justification.* Every
input to the A=3 binding prediction is classified **DERIVED** (cite the
math), **INPUT** (one of the 3 calibrations), or **OPEN GAP** (the precise
missing categorical object — no fit may fill it). The point is that the path
to 100% is explicit and no gap hides behind a "justification."

## Inputs (the 3 calibrations — by design)

| input | role | note |
|-------|------|------|
| m_e | CAL-1 | electron mass (Penning trap) |
| q₀ | CAL-2 | from neutron β-decay (τ_n). Substrate-*derivation* of q₀ = **Subgoal-2, owner-declined 2026-05-08** |
| m_π | CAL-3 | pion decay. Provides the **nuclear length scale** λ_π = ℏc/m_π = 1.414 fm (Yukawa range) via 𝐂 |

## Derived (100%, no fit)

| component | derived from |
|-----------|-------------|
| canonical braid β_atom | substrate 𝐂 categorical action → `atom_braid_word_3A` |
| Markov trace tr_M(β) | Hecke/Hoefsmit, Markov axioms |
| Jones–Markov weights y_λ | Wenzl bridge, closed form (50 dps) |
| characters χ^λ(β) | Hoefsmit seminormal representation |
| energy scale E₀ = m_e/(q₀(q₀−1)) | CAL-1 + q₀ |
| per-block / pair-sum binding `E₀·Σ_λ y_λ\|χ^λ\|` | no fit → deuteron +3.6% |
| C(A,2) pair multiplicity | combinatorial bond count |
| per-bond embedding growth (+16–20%) | embedded H₉ marginals, Rust kernel, no fit (#1776) |
| **embedded all-pairs combiner → A=3 at −13%** | multiplicity × embedding (#1778), **zero fit** |
| Coulomb mechanism (31% of T−³He) | `def:coulomb-charge`: Q_pp=+1, ratio tanh(ln q₀) (#1775) |
| Coulomb length scale = λ_π | m_π (CAL-3) via 𝐂 — *not* a missing scale |

## Open gaps (none fillable by fitting)

| gap | what's missing | tractability |
|-----|----------------|-------------|
| **3-body joint-trace correlation (the −13% A=3 residual)** | binding is the *joint* trace over all interfaces, not the *sum* of independent pair-marginals; the inter-pair correlation = the genuine 3-body force | **PURE COMPUTE — no Subgoal-2, no length scale, no link choice. The one gap a derivation can actually close.** |
| Δ_λ per-partition weights | the per-block binding density; six ansätze failed on the deuteron | same family as above |
| atom→knot link assignment (L6a4) | (a) heuristic registry (#1784); (b) the interface is the **averaged crossing σ−h/2** (a superposition, not a definite crossing) → a definite link is a *choice* | **structurally non-100% via the link-volume path** |
| magic-A / link volume (8G) | rests on the heuristic link above | inherits the gap |
| EM structure factor (3/4) for T−³He | `E_C = α_EM·m_π·(cusp ratio)`; the ≈3/4 cusp ratio of L6a4 needs the link (heuristic) | blocked on the link gap |
| q₀ substrate-derivation | absolute-scale closure | **Subgoal-2, owner-declined** |
| tooling: HOMFLY at n≥3 | `homflypt_engine` returns 0 for n≥3 (unimplemented); no SnapPy | implementable (in progress) |

## Verdict

There is **no 100% derivation of nuclear binding today.** Fully-derived
Markov traces reach **A=3 at −13%**; the rest is the genuine open frontier.
Two structural facts the 100% standard forces:

1. **The link-volume / magic-A path can never be 100%** — the averaged
   crossing is a superposition, so a definite link (and its 8G volume) is a
   choice, not a derivation. 100% work must use only the Markov-trace path.
2. **The single closable gap is the 3-body joint-trace correlation** (the
   −13%): no calibration-beyond-3, no length scale, no link choice — purely
   the operator-valued joint Markov trace of all C(A,2) interfaces at once,
   minus the pair-sum. That is the next derivation to attempt.

Everything else (Δ_λ same family, link assignment, EM 3/4, q₀) is either the
same 3-body problem in disguise, blocked on the link gap, or Subgoal-2.
