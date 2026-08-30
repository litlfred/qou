# The μ₃ submodularity door is structurally vacuous at the deuteron (A=2)

**Date:** 2026-08-02
**Branch:** `claude/deltalambda-submodularity-parallel-2026-08-02` (PR #4617)
**Scope:** scope-(b) structural negative. Lean-proved, Mathlib-free. Nothing wired, nothing fitted.
**Route class:** deliberately-parallel, distinct-angle attack on the Δ_λ / deuteron-magnitude gate.

## Summary

The owner posed (bean context, 2026-08-02): *does the μ₃ cluster-modularity /
submodularity structure landed today* (`0e9bfc67`,
[`QOU/MassTheory/Mu3ClusterModularity.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/Mu3ClusterModularity.lean),
`c₃ = −E₀·Δ²g`, `μ₃ > 0 ⟺ Δ²g < 0`) *supply the deuteron binding magnitude that
the DT count provably does not?* (#4601: derived `Δ_λ = (−1)^{n(λ)}·dim V_λ`
gives B_D = 0.380 MeV, −82.9%.)

**Answer: no — and for a clean structural reason, not a numerical one.** The μ₃
door is the **second mixed finite difference** of the joint block-trace over
**two** interface bonds. The deuteron is a **single-bond** object. The second
difference is *identically zero* on any single-bond configuration, so the μ₃
cluster contributes **exactly 0** to the deuteron binding, for every `E₀`. The
submodularity door does not exist below A=3.

This is the honest negative the owner explicitly anticipated: "*if corpus-grep
shows μ₃/submodularity is … [an object] with no honest extension to Δ_λ binding,
SAY SO.*" It is stronger than a c₃/Q_β-scope objection — the μ₃ object here *is*
a binding cluster (E₀ = m_e/(q₀(q₀−1)), isotopes T/³He), but it is a
**beyond-pairwise** cluster whose lowest live order is A=3.

## The structure

On the interface Boolean lattice `{∅, a, b, ab}` the joint block-trace
`g(S) = Σ_λ y_λ |χ_λ(w_S)|` has a finite Möbius (cluster / Ursell) expansion:

    g_ab − g_∅  =  Δ¹g_a  +  Δ¹g_b  +  Δ²g,
      Δ¹g_x = g_x − g_∅                    (connected 2-body / single-bond)
      Δ²g   = g_ab − g_a − g_b + g_∅       (connected 3-body / the μ₃ door)

`Mu3ClusterModularity` proved `c₃ = −E₀·Δ²g` and `μ₃ > 0 ⟺ Δ²g < 0`
(submodular). Three derived operators were all found supermodular (door shut):
the multiplicative pairwise model (scope-b, Lean), the adjacent H₉ |χ|-joint
trace, and the non-adjacent BKL band bond (bean `qou-dpu1`).

**The deuteron sits below all of that.** A=2 carries exactly one p–n interface
generator — one bond. In lattice terms the second bond `b` is absent, i.e.
adding it changes nothing:

    g_b = g_∅,   g_ab = g_a    ⟹    Δ²g = g_a − g_a − g_∅ + g_∅ = 0.

So `c₃ = −E₀·Δ²g = 0` **identically**. The total deuteron change collapses to
the first-order term alone:

    g_a − g_∅  =  Δ¹g_a  +  0  +  0.

The deuteron's entire cluster content is **first order**. There is no
second-order (μ₃) content to be submodular *or* supermodular — the sign question
is empty.

## Lean (Mathlib-free, `lean`-direct exit 0, sorry-free)

[`QOU/MassTheory/DeuteronFirstOrderCluster.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/DeuteronFirstOrderCluster.lean)
— `import`-free core (`Int` + `omega`/`decide` only, so it checks without the
Mathlib olean cache, respecting the ~3 GB disk wall). Every identity is a pure
additive-group identity, true verbatim over `ℝ` (where the `g_S` live) by the
same cancellation.

| theorem | content |
|---|---|
| `secondDiff_single_bond_vanishes` | `Δ²g = 0` for a single-bond config |
| `cluster3_single_bond_vanishes` | `c₃ = −E₀·Δ²g = 0` for every `E₀` at A=2 |
| `total_change_decomp` | Möbius inversion `g_ab−g_∅ = Δ¹g_a + Δ¹g_b + Δ²g` |
| `deuteron_content_is_first_order` | deuteron total = `Δ¹g_a` alone (other two terms 0) |
| `nonzero_cluster_needs_second_bond` | `Δ²g ≠ 0 ⟹ g_b ≠ g_∅ ∨ g_ab ≠ g_a` (μ₃ exclusive to A≥3) |

## Derive-then-check (locked BEFORE any compute; 0 fit)

| quantity | value | source |
|---|---|---|
| B_D target | 2.224 MeV | AME2020 deuteron binding |
| first-order DT-derived | 0.380 MeV | #4601 (`Δ_λ=(−1)^{n(λ)}·dim V_λ`) |
| deficit factor | 2.224/0.380 = 5.853× | — |
| **μ₃ second-order contribution at A=2** | **0** | this branch (Lean) |

**No numerical probe is run**, and this is the honest call, not a gap: the
deuteron single-bond configuration has *no second interface to construct `Δ²g`
from*, so any "measurement" of `Δ²g` at A=2 would be a fabricated word, not a
derived one. The structural identity is the result; a compute would be
circular/vacuous. (Contrast the A=3 `triangle_bond_submodularity_probe.py`,
which *has* two bonds to measure.)

## Reconciliation with the live siblings (the pincer)

- **PR #4615** (per-pair uniform magnitude `z` / K₂–K₄ Gram determinant): `z`
  physical at A=2 (`1 − z² = 0.7507 > 0`) but closes only `0.506/2.225`; dead at
  A=4 (`det(I+G) < 0`). Kills the **per-pair amplitude** mechanism at every A.
- **This branch** (μ₃ / submodularity cluster): identically 0 at A=2. Kills the
  **beyond-pairwise cluster** mechanism at the deuteron.

Together: neither the per-pair magnitude nor the cluster hierarchy supplies the
deuteron 5.853× deficit. **The deficit is carried entirely by the bare
first-order per-bond amplitude `Δ¹g` itself** — precisely the FITTED
`C_knot = 5.853` of #4601/#4615. That bare amplitude is the surviving open
magnitude object (GAP bean, this branch). It is *not* a DT count (#4601), *not*
a uniform `z` (#4615), *not* a structural exponent `k` (#4615 found `k=6.16`
non-integer), and *not* a cluster/submodularity term (this branch).

## Scope discipline

Scope-(b) structural exclusion of a *mechanism at a specific A*, justified by a
proved algebraic identity (`Δ²g ≡ 0` on single-bond configs), per AGENTS.md
§"Before declaring refuted". It does **not** claim the deuteron is unclosable in
general (the bare first-order amplitude remains open); it claims the **μ₃
submodularity door specifically cannot contribute to A=2**. Anti-fit: `μ₃`, `z`,
and `B_AME` enter only as diagnostics; nothing is inverted or wired.
