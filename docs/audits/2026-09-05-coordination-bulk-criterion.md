# An edge set can supply a surface term only if it has a bulk — and every **affine** candidate fails, for two opposite reasons

**Date:** 2026-09-05 · **Beans:** `qou-99rx` (this), `qou-glji` (#6780, the question this answers),
`qou-kqdn` (#6761, the amplitude this is prior to), `qou-556v`, `qou-v0yw`, `qou-brng` ·
**Arc:** binding law / extensive term · **Scope:** formalize-first Lean (sorry-free) plus a probe;
**the conclusion was narrowed twice by the corpus-grep, and both narrowings are recorded here.**
**Nothing is wired, nothing is fitted.**

## 1. The question, and where it came from

#6780 rejected the production braid word's chain against the AME chart: its coordination graph is
a path, so its bond count is `A − 1`, its per-nucleon law is the `p = 1` member of
`B/A = a − b·A^(−p)`, and `RSS(1) = 147.0` against `RSS(p*) = 38.2`. Its §7 recommendation was to
ask the prior question — **not** "what fixes the amplitude `1 − k'/k`?" (#6761 measured that answer
generic at 67.9 % of its window) but **"what edge set could supply a surface term at all?"**

## 2. Corpus-grep, six paths — and it narrowed the tranche twice

**Path 0 unavailable** (the `paper-assistant` MCP server failed to connect, `ENOENT`), so these are
grep-open, not graph-open. Path 5 (`library/`, all four tiers including `ocr/`) is **empty**: the
library holds nothing on the SEMF surface term, liquid-drop, coordination number or sphere packing.
Bethe–Bacher 1936 and von Weizsäcker 1935 are registered in `references.ts` but **not ingested**.

Four prior results sit between this tranche and a claim of novelty. Two of them changed what may be
claimed; all four are now cited in the Lean header.

| prior result | what it covers | what it leaves |
|---|---|---|
| `QOU.Mass.AffineCountMultiplicityWindow.mu (α β A : R) := α * A + β` | **the same object**, generic field, sorry-free — used for *cumulants* | never for a surface exponent; its own note says it is *"instantiated at nothing"*, which is the step taken here |
| `qbeta_chain_cannot_carry_coulomb_or_surface_probe.py` §2 | **`boundedSurface_not_hasBulk` in prose**, verbatim: *"a deficit of 2, independent of A. No `A^(2/3)` piece can arise from the edge count of a path, for any letters."* | no Lean; restated in `2026-09-05-binding-law-arc-synthesis.md` |
| #6780's own header (mine) | the deltahedron objection: *"`d = 3` geometrically while having no bulk at all"* | prose only — `linearSurface_not_hasBulk` promotes it to a decidable `Prop` |
| `every_seifert_invariant_is_affine_probe.py` | scope-(b) for any Seifert invariant *"via `AffineCountIsNotASurfaceTerm`'s strictly-monotone ratio"* | measured on six nuclei, target fixed at `A^(2/3)`, never written as a theorem |

**`AffineCountIsNotASurfaceTerm` is a one-instance result** — read in full: both sides are hardcoded
`def`s (`crossingCount = 12A − 1`, `surfaceOfCube = m^2`) and the exclusion quantifies only over
`m₁ m₂ c`. No arbitrary `α`, `β` or `p`.

**So what is new is narrow, and is stated as such:** arbitrary `(α, β)` against **every** `p ≠ 1`
rather than one count against one target; the deltahedron instantiation in Lean; and `HasBulk`
itself, which a full grep finds nowhere in any wording — neither the conjunction nor
`Tendsto (A_surf A / A) atTop (nhds 0)` in any Lean file.

## 3. Lean — `QOU/Mass/CoordinationBulkCriterion.lean` (sorry-free, 10 declarations axiom-clean)

**Part 1 — every affine bond count is `p = 1`.** `M(A) = α·A + β` gives `εα + εβ/A` exactly
(`affine_perNucleon`), which is `perNucleonExp (εα) (−εβ) 1` (`affine_eq_perNucleonExp`), and by
#6780's `perNucleonExp_exponent_inj` it differs from every `p ≠ 1` law at some `A`
(`affine_ne_surfaceLaw`, needs `β ≠ 0`). Instantiated at the chain (`α = 1, β = −1`) and the
deltahedron (`α = 3, β = −6`). **So the obstruction is not one-dimensionality; affineness alone
suffices, and both candidates share it.**

**Part 2 — the criterion.** `HasBulk A_surf := A_surf → ∞ ∧ A_surf/A → 0`. Each clause alone is
cheap; the conjunction has content. The two candidates fail one clause each, **for opposite
reasons**: the chain's `A_surf = 2` is constant (interior, no growing surface); a convex deltahedron
has `A_surf = A` (growing surface, **no interior at all** — every nucleon is a hull vertex). The
satisfying case is `A_surf = c·A^θ`, `0 < θ < 1` (`powerSurface_hasBulk`) — exactly what
`CoordinationSurfaceDeficit` assumed.

`lean`-direct exit 0 (3.1 s); `#print axioms` on all ten `= {propext, Classical.choice, Quot.sound}`;
zero `sorry`.

## 4. Probe — `computations/probes/coordination_bulk_criterion_probe.py`, **17/17**

The deltahedron edge sets are loaded **out of** `geometric_saturation_and_labelling_probe.py` with
`ast` rather than re-typed. That module imports `networkx` at module level and it is not installed
here, but its `deltahedron` function uses only `itertools`, so compiling that one `FunctionDef`
gets the corpus's real data — a re-typed copy could drift; this cannot.

**Two measurements that sharpen the Lean rather than restate it.**

**Non-affine is necessary, not sufficient.** The complete graph is non-affine (second difference 1,
not 0) and is refuted for the *opposite* reason — `B/A` = 13.2, 144.8, 1460.7 at `A` = 10, 100,
1000, unbounded. So the target is specifically **sublinear-but-unbounded** surface growth. "Affine
bad, non-affine good" would have been the wrong reading.

**The data require a bulk.** Under `perNucleon_split` the deficit is `(ε(k−k')/2)·(A_surf/A)`, so
#6780's fitted `p` implies `A_surf ∼ A^(1−p)`. All five of its analysis variants give `1 − p`
strictly inside `(0,1)`: 0.6360, 0.4300, 0.4177, 0.5973, 0.7708. The all-nuclide 0.636 sits near
the compact-packing 2/3 = 0.667 — **a consistency check, not a prediction**, since #6780 measured
that exponent mass-cut dependent with disjoint intervals.

**Also validates #6780's profiler against a known answer.** Profiling the exponent of each edge
set's *exact* affine law returns `p = 1.0` with RSS ~1e-38. Until now that profiler had only been
run on data, where the true answer is unknown.

## 5. Two narrowings — the honest limits, both measured

**(i) The enumeration of derived edge sets is EMPIRICAL, so the conclusion is scope-(a) and is
about AFFINE edge sets only.** The corpus keeps its own list at `QOU.Hecke.BoundedDegreeCoulomb`
and it is longer than two. **Max-contact sphere packing** (`binding_edge_set_selection.py`) is
derived-in-principle, is **not** the deltahedron family in general, and is **not known to be
affine** — Part 1 does not reach it. The degree-capped count `A·min(A−1,k)/2` is piecewise (second
difference −6 at the knee, 0 past it), so not affine on `ℝ` either, though Part 2 reaches it.
α-cluster contact deltahedra are a further uncovered object. **"No derived edge set has a bulk"
would overclaim; "no affine one does" is what was proved.**

**(ii) `deltahedronSurface_not_hasBulk` extrapolates a family that barely exists.** `HasBulk` is an
`A → ∞` criterion, but convex deltahedra exist only for `A ∈ {4,…,10,12}` and **the corpus records
them only up to `A = 7`**. So that row is applied to the *idealisation* `A_surf = A`, never to the
corpus's data, which does not reach far enough to have an asymptotic regime at all. Stated in the
Lean docstring rather than left for a reviewer.

## 6. Verdict and scope

- **Scope-(b) for the class {affine bond count, uniform `ε`}**, the invariant being
  `perNucleonExp_exponent_inj` (sorry-free): no affine edge set is ever a surface term, for any `p`.
- **Scope-(b) for the two surface-count shapes** (constant, linear) — the invariant is the limit.
- **Scope-(a) for "no derived edge set has a bulk"**, because the enumeration is empirical and the
  deltahedron row extrapolates.
- **NOT writable in either scope: "the substrate cannot emit a non-affine coordination object."**
  No invariant exists, and the corpus already carries two scope-(a) negatives pointing that way —
  `every_seifert_invariant_is_affine_probe.py` (*"the framework's nuclear encoding has no surface …
  a surface term must come from geometry the encoding does not currently carry"*) and
  `nf_inter_nucleon_is_a_count_not_a_graph_probe.py` (**stronger** on one layer: the NF encoding
  expresses a bond *count* and no graph at all). Both are cited in the Lean so this is not a fourth
  statement of a conclusion the corpus already carries twice.

## 7. Options for the author (default first; recommendation is judgement)

- **Default — nothing changes.** The criterion is on the record with its two narrowings; Avenue 2
  stays open with the amplitude question demoted below the bulk question. Cost 0.
- **Test max-contact sphere packing against `HasBulk`.** It is the one derived-in-principle
  candidate this tranche does not cover, and it is the only one that could still have a bulk: its
  contact numbers are case-by-case geometry, not obviously affine. Cost: a probe over the known
  contact numbers plus, if they are affine, a one-line instantiation. Risk: the family is
  case-by-case and may not be defined far enough out to test an `A → ∞` criterion — the same limit
  that already weakens the deltahedron row. Commits to nothing.
- **Attack the scope-(b): is every edge set the braid word can express affine?** This would close
  Avenue 2 outright rather than leave it open. Cost: a formalize-first tranche on the encoding.
  Risk: `nf_inter_nucleon_is_a_count_not_a_graph_probe.py` suggests the NF layer carries no graph
  at all, so the question may have to be posed at the braid-word layer instead, where it is harder.
- **Do not** re-derive "the encoding has no surface". The corpus states it twice already.

**Recommendation (judgement):** the second. It is cheap, it is the single named gap in this
tranche's own conclusion, and either outcome is useful — a bulk would be the first edge set in the
corpus that could carry a surface term, and no bulk would let the scope-(a) be stated over the
corpus's whole enumeration rather than over its affine subset.

## 8. Verification

- `lean`-direct exit 0; 10 declarations axiom-clean; 0 `sorry`; the imported
  `SurfaceExponentIsDimension.olean` built lean-direct from `main`.
- Probe 17/17. One check's wording was corrected after passing: it asserted "no edge set on main
  has a bulk", which overclaims past the narrowing in §5(i); it now says "no affine edge set".
  Another was tightened from the source docstring's `{4..10,12}` to the measured `[2..7]`.
- No float64: 50 dps throughout; every reported quantity asserted `mpmath.mpf`.
- `scripts/precision-gates.sh --changed`: standing reds only, new probe in none of them.
- Repo CI is `workflow_dispatch`-only; this agent verification is the gate.
