---
# qou-t7az
title: 'RELATED-WORK + ROAST: McPhail-Snyder 2601.05136 diagrammatic state integrals vs the qnnq braid->data gap — verdict: relocates the gap, does NOT close it (ρ is an INPUT; k∈Z^E is SUMMED not selected; root-of-unity/fibre object, not q₀; targets Volume Conjecture not c₃)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T18:52:13Z
updated_at: 2026-10-04T15:23:22Z
parent: qou-n4nr
---

## Related work

Calvin McPhail-Snyder, *State integrals for the quantized SL₂(ℂ)
Chern–Simons invariant*, [arXiv:2601.05136](https://arxiv.org/abs/2601.05136)
v2 (Duke). Ref `mcphail-snyder2026`. Expresses the McPhail-Snyder–Reshetikhin
geometric-twist invariant `Zψ_N(K,ρ,µ)` (geometric twist of the Kashaev
invariant / quantization of SL₂(ℂ) CS) as a sum of state integrals built
**from a knot diagram**: a discrete state-sum over crossings with a per-edge
integer vector `k ∈ Z^E`, shadow colorings `(ρ,u)`, log-meridian `µ`. Worked
for the 5₂ Kashaev invariant.

## The roast (adversarial, Critical-distance license)

I over-sold this in chat when I first found it ("the most direct realisation
of braid → data"). Reading it properly: **it relocates the qnnq gap, it does
not close it.** Four load-bearing objections:

1. **ρ is an INPUT, not an output.** The invariant is `Zψ_N(K, ρ, µ)` — it
   *consumes* a representation `ρ: π₁(S³∖K) → SL₂(ℂ)` and a log-meridian `µ`
   (abstract lines: "an invariant of a knot K, a representation ρ …, and a
   logarithm µ of a meridian eigenvalue"). The whole open problem in qnnq is
   *which* flat connection / cusp datum a braid selects — i.e. supplying `ρ`
   and `(µ,λ)`. McPhail-Snyder assumes exactly the thing QOU has to derive.
   `ρ`/`(µ,λ)` is the transcendental geometric datum — the same object as
   `ϑ_K`. So this changes coordinates on the gap, it doesn't remove it.

2. **`k ∈ Z^E` is SUMMED OVER, not selected.** "For a vector `k ∈ Z^E` …
   a state integral is …; `Z_N` is given by the **sum over all** state
   integrals" (§1, eqs. around lines 176–182). The diagram fixes the edge set
   `E`; the observable then sums over the whole integer lattice `Z^E`. This is
   the SAME structure as Fantini–Wheeler's `(m,ℓ)` lattice — there is no
   "braid → one integer" map. My earlier "a braid word determines a specific
   integer state-sum" was wrong in precisely the way "braid → single (m,ℓ)"
   was wrong. Scope-(a) correction, logged.

3. **It lives at a ROOT OF UNITY (fibre level), not at q₀ (observable).**
   These are "cyclic type invariants" — the Kashaev invariant at `ζ = e^{2πi/N}`,
   with `ϕ_N(ζ)` quantum dilogs and large-`N` (Volume-Conjecture) asymptotics.
   QOU's c₃ is evaluated at the fixed real substrate `q₀ ≈ 1.1097`
   (archimedean observable). Per AGENTS.md §"Im(q) at fibre vs observable
   level", a root-of-unity Kashaev object is a **fibre-level** construction;
   bean `qou-0e66`'s phrase "specialise at q₀" is therefore suspect — likely a
   fibre↔observable category error. If a bridge exists it is the archimedean
   *evaluation* of the fibre object, which is exactly the hard, unbuilt step.

4. **It targets the Volume Conjecture, not c₃, and is itself incomplete.**
   The paper's stated goal is "the remaining obstacles to establishing
   exponential growth of `Zψ_N`" — i.e. recovering the hyperbolic **volume**
   asymptotically, not a precision-ladder Taylor coefficient. Even that growth
   "has been established only for knots with up to 7 crossings" (§1.3). There
   is no `c₃` in this paper; the invariant → c₃ bridge is 100% QOU-side and
   unbuilt. Well-definedness is also delicate (admissible/normalized shadow
   colorings, non-pinched diagrams, geometrically non-degenerate structures).

**Verdict.** Genuine, elegant, and the right *neighbourhood* — the per-edge
`k ∈ Z^E` crossing state-sum is the diagrammatic analogue of the FW lattice,
and worth citing. But it is **NOT a closure of qnnq and probably not even a
turnkey tool**: it assumes the datum QOU must derive (ρ/µ), sums rather than
selects, sits at roots of unity, and only reaches the volume (not c₃). Track
it as related work; do not wire it, do not let it read as "the mechanism was
found." Re-scope `qou-0e66` accordingly (drop the "IS the k∈Z^E sum at q₀"
over-claim → "assess the fibre-evaluation bridge, if any"). Still OPEN.

## Round 75 Progress (`litlfred/qou`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/TwoRowFrobeniusStratumAndConnectedSumTraceBrick.lean` (`mcphail_snyder_diagrammatic_edge_lattice_rank_and_input_shift`)
- **Summary**: Proved planar 4-valent knot diagram Euler identity `c - 2 * c + (c + 2) = 2` and non-vanishing phase shift `alpha * (mu + delta_mu) - alpha * mu = alpha * delta_mu != 0` under an input meridian perturbation `delta_mu != 0`.
- **80-dps Probe & Witness**: `computations/probes/two_row_frobenius_stratum_and_connected_sum_trace_brick_probe.py` -> `computations/probes/two-row-frobenius-stratum-and-connected-sum-trace-brick.witness.json` (`scriptCommitSha: 2463220ce5c89b017aafd3bf4d0ccffbad829f4f`, PR head `9ae0c19dfa3265ac670ac5d85777be275271ab28`)
