# Transverse NA-Stokes surface-curvature — forward geometric route (does NOT close the deuteron magnitude; the object is bracketed but transport-unpinned)

**Date:** 2026-08-08 · **Branch:** `claude/nastokes-transverse-curvature-2026-08-08` ·
**Bean:** `qou-prjo` (LEAD-2, geometric surface-curvature route; LEAD-1 is the
parallel algebraic ≥3-body cumulant route) · **Epic:** `qou-r2nh` (Δ_λ arc) ·
**Tier:** 1 sorry-free Lean structure + 1 forward 0-fit probe (scope-(a) negative).
**No fit, no AME inversion, nothing wired, q₀-free.**

## 0. TL;DR

The transverse NA-Stokes surface-curvature pairing `Ω₂ = ½ P ∮∮ [𝓕,𝓕]` — the
named surviving carrier of the deuteron binding *magnitude* after braid-word /
scale / level / edge / DT-count are all excluded — was attacked **forward and
geometrically**. Committing to the geometric definition *before* comparing to
AME:

1. **Structure formalized, sorry-free** (`lean`-direct exit 0, `#print axioms`
   clean): the Seifert-surface Betti combinatorics (`b₁ = c−s+1 = 2g`) and the
   ordered transverse pairing over a generic ring, including **THE WALL** —
   a nonzero transverse magnitude *forces* position-dependent (transport-
   twisted) curvature, i.e. requires exactly the surface-2-form data the corpus
   lacks.
2. **Forward magnitude does NOT close it (scope-(a)).** With the trefoil anchor
   `b₁=2` and `A−1` inter-nucleon links, the AME binding ratios sit **between**
   the diagonal (additive `∝ b₁`, undershoots) and off-diagonal (full pairing
   `∝ C(b₁,2)`, overshoots) envelopes — the same bracketing shape as the
   na-Stokes `ℏ⁰`(diverge)/`ℏ²`(undershoot) leg.
3. **sorry-free ≠ derived.** The magnitude is *not* derived: the interpolating
   weight between the two envelopes is the transport `U(x,O)` across the Seifert
   surface.

**Convergence with concurrent siblings (corpus-grep, 2026-08-08).** Two sibling
PRs attacked the *deuteron* end of this object the same day and reached
**consistent negatives** — this route is now triply-confirmed:
- **#4798** (`nastokes-surface-curvature-deuteron`) **built** the trefoil Seifert
  discretization (`V=[[-1,1],[0,-1]]`, `J=V−Vᵀ`) and the explicit surface-ordered
  `½∮∮[𝓕,𝓕]`. Result: the transverse term **is nonzero** on `σ₁³` (confirms
  survival), but the scalar coefficient `c₂=‖Ω₂^⊥‖/h²` ranges **0…897** across
  natural germ/handle gauge choices — never ≈1 (the `g₂` that would close the
  deuteron). O(100×) gauge freedom the corpus does not fix.
- **#4619** (`sigma1cubed-seifert-tessellation`) showed the state-sum is
  **tessellation-independent** (`5e-51`, a topological invariant, *not* a fit)
  but **q₀-degenerate** (`σ₁³` is a torus knot, `Vol=0`, pinched octahedron;
  `value/target=0.136`), and **proved the scalar/character channel null**
  (`χ^λ` annihilates the commutator product, `tr[A,B]=0` at 40 dps).

So the earlier framing "the corpus lacks the discretization" is now **corrected**:
for the *deuteron trefoil* the discretization was built (#4798/#4619); it does
**not** close the magnitude because the surface→scalar map is gauge-
underdetermined (#4798) and trace-null / q₀-degenerate (#4619). What this LEAD-2
route adds is the **Lean formalization** of the pairing structure + the wall +
the **trace-null theorem**, and the **multi-isotope Betti bracketing** (below)
that #4798/#4619 (deuteron-only) did not compute.

## 1. The forward geometric definition (committed before matching)

The order-2 Magnus term of the surface-ordered exponential is
`Ω₂ = ½ P ∮∮ [𝓕,𝓕]`, `𝓕(x) = U(x,O)⁻¹ F_q U(x,O)`, quadratic in the germ
commutator q-curvature `F_q = [δq₁,δq₂]`
([`germ-commutator-q-curvature.md`](../../content/quantum-observable-universe/quantum-observable-universes/germ-commutator-q-curvature.md)).
It is **transverse** to the strand ordering (the two-observer-parallelogram
direction), so it survives on the single-generator `σ₁³` deuteron channel where
every *inter-crossing* Magnus commutator vanishes (`[a,a]=0`;
[`2026-07-24-eunit-magnus-order2.md` §2](2026-07-24-eunit-magnus-order2.md)).

Discretize the Seifert surface of a connected positive-braid diagram (`s`
strands, `c` crossing letters, Seifert's algorithm):

- Euler characteristic `χ = s − c`; first Betti number `b₁ = 1 − χ = c − s + 1 = 2g`
  — the number of independent transverse 2-cycles (handles) carrying curvature.
- Two envelopes of the magnitude, with `κ² = ‖F_q‖²` universal (cancels in ratios):
  - **diagonal / additive** — one `κ²` per handle: `M_diag ∝ b₁`;
  - **off-diagonal / full surface-ordered pairing** — all handle-pair
    commutators `[𝓕_i,𝓕_j]`: upper envelope `M_off ∝ C(b₁,2)`.
- The **true** magnitude sits between, weighted by the transport twists.

## 2. Lean (sorry-free, `lean`-direct exit 0)

[`QOU/MassTheory/TransverseSurfaceCurvature.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/TransverseSurfaceCurvature.lean)
(registered in `QOU.lean`; `#print axioms` = `propext, Classical.choice,
Quot.sound` only — no `sorryAx`):

| Declaration | Content |
|---|---|
| `seifertBettiOne s c := c − s + 1` | `b₁ = 2g` of the diagram's Seifert surface |
| `seifertBettiOne_trefoil : … = 2` | deuteron `σ₁³` (s=2,c=3), genus 1 — concrete, falsifiable |
| `seifertBettiOne_link_additive` | `b₁(c+k)=b₁(c)+k` — **exact linearity = the pairwise cap** |
| `seifertBettiOne_extensive` | `b₁(3A, ρA)=(ρ−3)A+1` — extensive iff crossing density `ρ>3` |
| `curvComm`, `curvComm_antisymm` | `⟦a,b⟧=a·b−b·a`, antisymmetric 2-form (generic `Ring`) |
| `listPairing` | discrete ordered `½P∮∮[𝓕,𝓕]` |
| `listPairing_eq_zero_of_all_comm`, `listPairing_const` | flat / commuting surface ⇒ pairing `= 0` |
| **`listPairing_trace_zero`** | **trace/character-null** — any cyclic `τ` (Markov trace / `χ^λ`) kills the pairing ⇒ invisible to the scalar trace; formalizes #4619's `tr[A,B]=0` |
| **`transverse_nonzero_needs_noncommuting_curvature`** | **THE WALL** — nonzero pairing forces position-dependent transported curvature |
| `transverseMagnitudeDiagonal` (+ trefoil/flat/link-additive) | `½·b₁·κ²` diagonal envelope |

**Discipline.** Axiomatizing the curvature is NOT deriving its magnitude. The
Lean proves the *structure* (vanishing conditions, combinatorics, the wall),
never the numerical magnitude. `listPairing_pair` shows the object is not
vacuously zero (nonzero for non-commuting curvatures).

## 3. Forward probe (0 free parameters)

[`computations/probes/nastokes_transverse_curvature_seifert_probe.py`](../../computations/probes/nastokes_transverse_curvature_seifert_probe.py)
(witness `nastokes-transverse-curvature-seifert.witness.json`, 6 assertions).
Geometric inputs — **pure geometry, not fitted**: trefoil anchor `b₁_link = 2`;
inter-nucleon links `L = A−1` (spanning tree = the color-tube audit's "A−1
inter-nucleon Hecke generators"); `b₁(A) = 2(A−1)`. AME as **fixed ratios only**.

| iso | A | links | b₁=2g | AME/D | diag/D (∝b₁) | off/D (∝C(b₁,2)) |
|-----|---|-------|-------|-------|--------------|-------------------|
| D   | 2 | 1 | 2 | 1.000 | 1.000 | 1.000 |
| T   | 3 | 2 | 4 | 3.813 | 2.000 | 6.000 |
| ³He | 3 | 2 | 4 | 3.469 | 2.000 | 6.000 |
| ⁴He | 4 | 3 | 6 | 12.720 | 3.000 | 15.000 |

**Forward findings (facts, not fits):**

1. The additive/diagonal envelope **undershoots** ⁴He (3.00 vs 12.72).
2. The off-diagonal envelope **overshoots** ⁴He (15.00 vs 12.72).
3. AME is **bracketed** between the two envelopes at every isotope — the same
   shape as the na-Stokes `ℏ⁰`(diverge)/`ℏ²`(undershoot) bracketing
   ([`2026-08-02-brane-resummation-nastokes-volume-difference.md`](2026-08-02-brane-resummation-nastokes-volume-difference.md)).
4. The additive envelope is **exactly linear** in link count (mirrors the Lean
   `seifertBettiOne_link_additive`) — i.e. **pairwise-capped**, so the diagonal
   reading **cannot** be the ≥3-body super-pairwise term the corpus proves is
   required ([`2026-08-02-deltalambda-value-proved-…-additive-term.md` §4](2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md)).
5. **Isospin-blind:** T and ³He (both A=3) get *identical* geometry but AME
   differs by ~8% (the p/n mirror split) — genus/Betti topology alone cannot
   produce the T vs ³He splitting (consistent with the color-tube weight being
   a *separate* object from the extensive magnitude).

## 4. Verdict (honest, scope-(a))

- **Does NOT close the deuteron magnitude.** Neither geometric envelope
  reproduces the AME ratios: the diagonal reading undershoots and is
  pairwise-capped; the off-diagonal reading overshoots. This is a
  **scope-(a)** result ("this construction, as-read, does not reproduce the
  numbers"), not a scope-(b) exclusion of the transverse object itself.
- **Scope-(b), proved sub-exclusion:** the *diagonal / Betti-count reading* is
  excluded as the ≥3-body carrier — invariant cited: exact linearity of `b₁`
  in crossing count (`seifertBettiOne_link_additive`, Lean-proved) ⇒
  pairwise-capped. A genuinely ≥3-body enhancement can only come from the
  *off-diagonal* cross-handle commutators.
- **The wall stands, now formalized.** A nonzero transverse magnitude forces
  position-dependent transported curvature `𝓕(x) = U(x,O)⁻¹ F_q U(x,O)`
  (`transverse_nonzero_needs_noncommuting_curvature`). The interpolating weight
  between the diagonal and off-diagonal envelopes **is** the transport `U(x,O)`
  across the Seifert surface — the canonical surface-2-form discretization the
  corpus lacks.

## 5. Precise surviving sub-question (the next honest unit)

> **Find the principle that fixes the germ + handle gauge, in an operator-valued
> (non-trace) channel, across the multi-nucleon tower.** #4798 already built the
> deuteron trefoil transport and got `c₂ ∈ 0…897` (O(100×) gauge freedom);
> #4619 proved the *scalar/character* channel is null. So the three concrete
> open inputs are:
> (i) a **new principle fixing the germ normalization + the two H₁ handle
>     holonomies** (the O(100× freedom #4798 exposed) — without it the surface→
>     scalar map is unpinned between the `b₁·κ²` and `C(b₁,2)·κ²` envelopes;
> (ii) an **operator-valued / eigenphase-weighted** readout (the scalar Markov
>     trace is provably null — `listPairing_trace_zero` here, `tr[A,B]=0` in
>     #4619; the surviving non-trace channel is the one both #4619 and
>     `2026-07-24-eunit-magnus-order2.md` §2 name);
> (iii) the **canonical multi-nucleon Seifert braid word** — the corpus pins only
>     the deuteron trefoil, so the isotope Betti numbers `b₁(A)` above use the
>     minimal spanning-tree model, not a corpus-canonical multi-nucleon surface.

Until (i)–(iii) exist the deuteron magnitude stays open. This route **localizes**
the missing physics to the off-diagonal, operator-valued, gauge-fixed transport
weighting, and **proves (Lean)** two dead ends: the diagonal Betti-count reading
is pairwise-capped (link-additive) and the scalar-trace channel is null.

## 6. Coordination

Four concurrent `qou-prjo`/Δ_λ-magnitude fronts (2026-08-08):

- **#4817** (LEAD-1) — algebraic **q₀-free ≥3-row extensive cumulant**, scope-(a).
  Convergence test: if the off-diagonal cross-handle pairing (this route) is
  genuinely non-additive over links, it *is* a ≥3-body cumulant (LEAD-1's
  object) — the two routes meet at the same super-pairwise term.
- **#4798** — built the deuteron trefoil discretization; found the surface→scalar
  map has O(100×) germ/handle gauge freedom (`c₂∈0…897`). This LEAD-2 Lean
  `transverse_nonzero_needs_noncommuting_curvature` + envelope bracketing is the
  *structural* statement of that same unpinning.
- **#4619** — tessellation-independence + **scalar/character channel provably
  null** (`tr[A,B]=0`); this route formalizes that as `listPairing_trace_zero`.
- This PR (**#4818**, LEAD-2) — Lean structure + wall + trace-null + the
  **multi-isotope** Betti bracketing + the **pairwise-cap** proof
  (`seifertBettiOne_link_additive`).

**Do NOT redo:** any diagonal/additive/Betti-count closure (Lean-proved
pairwise-capped here), any scalar-trace/character closure (Lean-proved null here
+ #4619), or the deuteron-only germ/handle scan (#4798 did it → gauge-
underdetermined). The live frontier is the **operator-valued, gauge-fixed,
multi-nucleon** transport — items (i)–(iii) in §5.

## Files
- Lean: [`content/quantum-observable-universe/lean/QOU/MassTheory/TransverseSurfaceCurvature.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/TransverseSurfaceCurvature.lean)
- Probe: [`computations/probes/nastokes_transverse_curvature_seifert_probe.py`](../../computations/probes/nastokes_transverse_curvature_seifert_probe.py)
- Witness: [`computations/probes/nastokes-transverse-curvature-seifert.witness.json`](../../computations/probes/nastokes-transverse-curvature-seifert.witness.json)
- This report: `docs/audits/2026-08-08-nastokes-transverse-surface-curvature-geometric-route.md`
