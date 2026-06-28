# Non-fit binding frontier — verification + status synthesis (thb7 / w5tg / Option-E PROBE 2)

**Date:** 2026-06-28
**Branch:** `claude/backlog-drain-7c-orphan-2026-06-28`
**Trigger:** owner steer — *"open research gates — just not fitting; do corpus
grep first; some refutations may be overzealous."*

This note records a verification pass over the binding-energy "FOCUS levers"
(beans `thb7`, `w5tg`) and the Option-E A=4 frontier (`ae4b`/`ae42`/`ae43`),
prompted by an earlier triage that declared both levers *"BLOCKED-AT-CEILING,
not agent-actionable without owner reversal."* That phrasing was **overstated**;
this note corrects it and pins the true non-fit frontier so the next agent does
not re-run the triage.

## 1. Retraction: "needs owner reversal" conflated two distinct gates

The earlier triage merged two gates that are **not** the same:

| Gate | Governs | Status |
|---|---|---|
| **q₀-substrate-derivation decline** (coord ledger 2026-05-08) | Subgoal-2: absolute m_p/m_n/⁴He *below* the CAL-2 floor | genuinely owner-gated; narrowly reversed only for the s5-so3 keystone |
| **Δ_λ / occupancy / ρ no-fit gate** | thb7, w5tg, Option-E — the *binding* levers | forbids **fitting**, *not* work; non-fit categorical work is the sanctioned direction |

thb7 and w5tg live under the **second** gate. AGENTS.md itself names the non-fit
path as "the productive direction" (GAP-A-3/A-4, Option-E PROBE 2 — the A=4
interface operator). None of that needs an owner reversal. The correct statement
is **"not closeable *by fitting*; the non-fit frontier is open and active,"** not
"blocked pending owner reversal."

## 2. Refutation-scoping verification (per AGENTS.md §"Before declaring refuted")

Owner flagged that some refutations may be over-zealous scope-**(b)** structural
exclusions lacking a cited invariant. **Checked every durable refutation in the
binding-lever artifacts; all are correctly scoped.** Findings:

- **Static integer bond-graphs "refuted"** (lever 2) — legitimate **(b)**, backed
  by a *proved invariant*: **exact finite enumeration** over `{0,1}`-pn edge sets
  (`bond-edge-set-selection.witness.json`: `deuteron_not_closable_by_integer_edge_set`
  exact; `he4_requires_more_than_complete_graph` = 1.197 ≈ 1.20×). It excludes
  *that class only* and explicitly preserves the genuine `Z·N` fractional/
  categorical occupancy as "research-scale, not categorically forced, owner-gated"
  (`2026-06-23-delta-lambda-three-lever-status.md` §Lever 2). Not over-claimed.
- **3-body saturating product non-positive** — legitimate **(b)**, cited invariants
  `QOU.BraidKnot.Cluster.productModel_3body_nonpos` (premises `c≥0, fᵢ∈[0,1]`) +
  `markovParam_le_half` (AM-GM, forecloses the *pairwise* enhancing escape only),
  both sorry-free. The audit explicitly leaves the non-product / chirality-weighted
  route open (`2026-06-23-interface-operator-derivation-and-4body-assembly.md:267–295`).
  Not over-claimed.
- **Grep for `permanently closed / dead end / ruled out / impossible`** across the
  durable lever-2 artifacts → **empty**. The over-zealous "permanently closed,
  yield to keystone" language existed **only in the triage subagent's verbal
  summary**, never in a committed artifact.

**Outcome: no durable refutation required re-scoping; no edit made.** A separate
scoping subagent flagged `productModel_3body_nonpos` as an over-zealous (b) — that
flag was a **false positive** (the theorem carries explicit `fᵢ∈[0,1]` premises and
the audit preserves the escape routes); it was verified against the source and
**not** acted on. (This is the inverse-error guard: re-scoping a correctly-proved
(b) to (a) would have wrongly *weakened* a correct result.)

## 3. The non-fit frontier is OPEN and already well-advanced

The binding investigation has made real, parameter-free, non-fit advances —
contradicting "nothing actionable":

- **3-body sign: SOLVED.** The chirality involution `Σ y_λ sgn(w₀^{S_{λ'}}) χ_λ`
  flips `c₃` to **attractive** (`+0.076`/`+0.120` for ³H/³He), escaping
  `productModel_3body_nonpos` exactly as predicted — zero fit, Rust kernel
  (`chirality-weighted-3body-cluster.witness.json`, 2026-06-24).
- **Structured combiner run** (|χ|-magnitude on pairwise + chirality sign on the
  3-body correlation) — best of three; **relocates** the gap to a **pairwise-trace
  magnitude deficit (~40%)**, explicitly *"consistent with the CAL-2 floor / missing
  operator-valued branching combiner"* (`structured-combiner-and-triangle.witness.json`).
- **Long-range triangle bond** — genuine non-product attractive contribution
  (`Δ_LR ≈ +0.3 MeV`, ~5% of the gap), confirming the topology escape is real.

**Net diagnosis:** the residual is **no longer a sign or topology problem** — it is
**pairwise-trace magnitude at the CAL-2 floor**, i.e. the operator-valued branching
combiner (Subgoal-1), shading into the owner-gated absolute scale for the last part.

## 4. Genuinely-open non-fit candidates (and why each is not a clean in-lane drop)

| Candidate (non-fit) | State | Gate |
|---|---|---|
| A=4 interface operator scalar `ρ_F` extraction | topological support correct (LR fusion); preflight step-1 identity reduction exact @1e-25 (`a_operator_categorical.py`) | **Rust-gated** (seminormal matrices at MPFR; H₉/H₁₂ kernel) |
| q-Reeb `|Δθ_λ|` cooperative object (closes A=3 ~2%) | diagnostic infra exists; binding-wiring open | **sibling-owned** (#2612) |
| Operator-valued branching combiner (the pairwise-magnitude residual) | the dominant residual per §3 | **in-flight** (bean `ovud` "wire Li2q brane-tower into F_Bor"; PR #1698) |
| Absolute ρ / Z·N occupancy magnitude | research-scale | **owner-gated** (s5-so3 keystone) |

Every remaining non-fit step is Rust-gated, sibling-owned, in-flight, or owner-gated.
There is no independent, non-fit, in-lane *binding-physics* deliverable left that is
not already being worked — which is the honest reason this lever cluster reads as
"at ceiling," even though the gate is *no-fit*, not *no-work*.

## 5. Stale-record corrections made alongside this note

- **`z1lz` (YLambdaQSchur §7c orphan):** the bean's "true orphan, 0 importers, wire
  it in" premise is **stale** — `YLambdaQSchur.lean` is already generic
  `{R : Type*} [Field R]` *and* already imported in `BraidKnot.lean:134` (+ 3 other
  importers: `f-bor-borromean-observable.lean`, `proton-mass-substrate-identity.lean`,
  `QSchurYLambdaClosedForm.lean`). No work needed; sub-task effectively done.

## References

- `docs/audits/2026-06-23-interface-operator-derivation-and-4body-assembly.md`
- `docs/audits/2026-06-23-delta-lambda-three-lever-status.md`
- `docs/audits/2026-06-28-delta-lambda-l1-ceiling-sign-only-prune.md`
- `docs/coordination/option-e.md` (PROBE 2 ledger)
- `computations/bond-edge-set-selection.witness.json`
- `computations/chirality-weighted-3body-cluster.witness.json`
- `computations/structured-combiner-and-triangle.witness.json`
