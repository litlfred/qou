# Workplan — week of 2026-05-31 (status + strategy)

**Scope.** Strategic update after a high-throughput week on `main`:
222 commits, 20 open PRs, several large axes either crossing a
milestone or hitting their structural ceiling. This doc captures
where each axis stands, what's actively in flight on a sibling PR,
what's blocked, and the recommended next priorities.

Existing detailed plan docs continue to govern per-axis work:

- [`docs/mass-1ppm-workplan.md`](../mass-1ppm-workplan.md) — mass-table 1 ppm path
- [`docs/plans/F-precision-lift-mpfr.md`](F-precision-lift-mpfr.md) — Plan F (mpmath / MPFR migration)
- [`docs/plans/G-status-and-narrowing.md`](G-status-and-narrowing.md) — Plan G (Vol shortcut retirement)
- [`docs/plans/G-vol-shortcut-retirement.md`](G-vol-shortcut-retirement.md) — companion to G
- [`docs/plans/H-rho-from-wedderburn-multiplicity.md`](H-rho-from-wedderburn-multiplicity.md) — Plan H (ρ general rule)
- [`docs/picard-lefschetz-plan.md`](../picard-lefschetz-plan.md) — Picard–Lefschetz integration
- [`docs/pyhecke-optimization-workplan.md`](../pyhecke-optimization-workplan.md) — pyhecke Rust kernel
- [`docs/forward-ref-mass-endo-rewire-plan.md`](../forward-ref-mass-endo-rewire-plan.md) — mass-endo rewire

This is the **cross-axis strategy update**, not a replacement.

## A. α_EM derivation — at CAL-2 floor, structural form converging

**Status: at CAL-2 floor; structural form converging.** The best
result this week is **#1484 self-consistent fixed-point at 0.31 ppb
= 2.09× σ_α** — the strongest categorical α_EM result to date.
The form `[2]_q · (1 − h²α)` is being identified with
`J_2(unknot)` (#1523) and a Schwinger q-correction at 73.6 ppm
(#1480).

**Active sibling PRs (11):**

| PR | What |
|---|---|
| [#1463](https://github.com/litlfred/qou/pull/1463) | scaffold: α/(4π) RT 2-loop self-energy — open-gap inventory |
| [#1477](https://github.com/litlfred/qou/pull/1477) | derive: trio resolution candidate `[2]_q/(8π)` at +393 ppm |
| [#1480](https://github.com/litlfred/qou/pull/1480) | derive: H = `[2]_q/(8π)` + Schwinger q-correction at 73.6 ppm |
| [#1484](https://github.com/litlfred/qou/pull/1484) | derive: self-consistent fixed-point — α to **0.31 ppb** |
| [#1487](https://github.com/litlfred/qou/pull/1487) | scaffold: RT 2-loop derivation roadmap (4 checkpoints) |
| [#1489](https://github.com/litlfred/qou/pull/1489) | derive: q_0 sensitivity — residual at CAL-2 floor |
| [#1491](https://github.com/litlfred/qou/pull/1491) | derive: Task 2 H refinement — form at CAL-2 floor |
| [#1495](https://github.com/litlfred/qou/pull/1495) | coord: α/(4π) thread ledger + RT 2-loop Task 3 plan |
| [#1503](https://github.com/litlfred/qou/pull/1503) | closure: α_EM subgoal-1 to CAL-2 floor + O(α²) notation fix |
| [#1505](https://github.com/litlfred/qou/pull/1505) | walkthrough: α_EM through the canonical derivation chain |
| [#1523](https://github.com/litlfred/qou/pull/1523) | content: categorical identification `[2]_q · (1−h²α) = J_2(unknot)` |

**Recommended next**: pick the 1–2 strongest landing candidates and
prepare for merge. The thread is fragmenting; consolidating onto
one canonical narrative branch would reduce reviewer load. Treat
PRs #1484 + #1495 + #1505 as the **canonical chain** and the rest
as either superseded probes or follow-up tightening.

## B. Mass-table extension to 252 stable nuclides — landmark

**Status: ¹H..²⁰⁹Bi covered via parameterised SDP uniqueness.**
This is the biggest single-week expansion. The pipeline went from
"a handful of light nuclei verified" to "**252 stable nuclides
extended via parameterised SDP uniqueness**" (`24540f5616`), plus
a foundation `parameterised CODATA-AME deviation identity` in
`AtomicMass` (`969f95bcf5`) that #1548 applies to H/He/Li
(`47b6b1bff7`).

Per-nucleus witnesses now cite Lean uniqueness theorems
(`ff495d2698`, `b1b64be871`); an audit watcher polices the
`lean_uniqueness_ref` wiring (`96a3d16e83`); the observable-sector
tracker (`debfdc71`) gives a per-sector status dashboard.

**Active sibling**: PR #1516 (option-e Phase 1 Gram done,
Phase 2 entry-point) is downstream of this.

**Recommended next**: full-spectrum precision dashboard refresh.
The L2 100× target now applies to **252 isotopes** rather than the
4 historically tracked. The `per-observable-100x-status.witness.json`
needs a re-run + status doc update.

## C. Δ_λ closure (Option E) — eight failed probes, may need redirect

**Status: shape-probing dead-end.** Option E (Kashiwara crystal)
has gone through v1 → v7 this week (`acdd997f4d`, `619fdb0076`,
`6a931e064a`, plus `2e53af441e` "all 7 rules tested, all fail" and
the earlier docs/audits Δ_λ analyses). Best v6 ≈ 17.36% off (down
from v1 65.6%). v7 finally identified that **partition transpose
is the right family** but the verification still fails.

The author's discipline (per CLAUDE.md "Δ_λ gate (Track A
blocker)") explicitly excludes a 7th-or-later fit-based ansatz.
The productive directions are GAP-A-3 / GAP-A-4 (categorical
brane-tower level selection / ρ general rule) and Option E
(Kashiwara). v6 + v7 together suggest the partition involution is
real but the closure formula isn't reached.

**Recommended next**: a **strategy review**, not a v8. Surface
the question: is Option E's structural failure tractable with
more probing, or does it need GAP-A-3 (Plan H — ρ general rule
from Wedderburn multiplicity) first? PR #1516's Phase 1 (Gram)
done + Phase 2 entry-point is the natural bridge.

## D. IwahoriHecke sprint5/6 — opaque dissolution

**Status: 4/5 sorrys cleared in `Defn.lean`'s opaque
IwahoriHecke** (`e442fcf287`); sprint5 added 2 Tier-B closures
(`b62a152d02`) for a cumulative 6; sprint6 scaffold factored the
PR-D Step 4 out as a named axiomatised class (`c28d6fe0f1`).

This is the Lean-side cleanup of the §3b-cond architecture — same
philosophy as PR #1536's `lean-stub-conjecture-kind-check` rule,
applied to the Hecke algebra layer.

**Recommended next**: continue. This thread is healthy and
the §3b-cond rule + the IwahoriHecke dissolution are mutually
reinforcing — once the rule lands the demoted blocks
self-document and once Defn.lean is fully cleared the
§3b-cond stub generator can be re-run with the cleaner
substrate.

## E. Paper-infra cleanup — landed (this session)

**Status: shipped 2026-05-30 / 2026-05-31** across 3 PRs (#1496,
#1519, #1536):

- **§3b-cond validation rule** (`lean-stub-conjecture-kind-check`)
  prevents future drift at validate time.
- **32 kind-mismatches swept** (bigbang-heatdeath + 5 from
  PR #1519 + 26 caught by the new rule on PR #1536).
- **Brunnian Lean scaffold** — `borromean_brunnian` sorry-free
  modulo `[LinkEquivalence]` class; discharge tracked as TODO
  (needs Mathlib R-move primitives).
- **Cosmological-cone visualization** + Garside proof-status
  reader guide + Borromean topological-confinement remark
  (3 narrative additions).
- Orphan simulator removed; 1 val-block-computation warning
  eliminated; casimir block schema repaired.

**Recommended next**: nothing immediate. The drift sweep
verified UGB / fred2005 / QOU are all clean. The remark audit
returned 0 dangling.

## F. Witness pipeline — 9 drift refreshes this week (steady-state)

**Status: healthy churn.** 9 `fix(witness-pipeline)` commits in
the week, mostly post-rebase drift refresh. The new
`witness_constant_staleness.py` (committed alongside) and the
q0-aware `_is_stale` check (`c96e89db4a`) make the pipeline
self-healing across q_0 re-pins.

Plus `ci(wheels): ship the clarabel-lp binding in pyhecke_native
wheels` (`969cc143`) ⇒ moment-SDP cross-checks now build in CI
(`60d86cd3`). Significant infrastructure delta.

**Recommended next**: nothing — steady state. Watch for the
next q_0 re-pin event; the self-heal infrastructure should
handle it.

## G. Gap-i/ii/iii probes — fully refuted, closure logged

**Status: closure.** PRs #1466, #1469, #1471, #1473 are all
REFUTED. The comprehensive 3-way refutation map is complete.
These are research-closure PRs (not bug-fix PRs); they document
**negative results** that inform what Δ_λ closure can and can't
look like.

**Recommended next**: merge for the audit trail. They aren't
patches in the usual sense; they're falsification records that
future sessions will want indexed.

## H. Bloch-Wigner / SnapPy axiomatization — phase 1 done

**Status: BlochWignerUnitCircle wired into `QOU.Archimedean`
aggregator** (`75078a152e`); phase-1 complete with axiom-to-opaque
migration (`84199bbbe4`). Producer-witness layer for
`Vol(L_6a4) = 8·G` (`26cc2f5eb3`) lands the canonical Borromean
volume identity per CLAUDE.md "Vol(B_3) = 8·G".

**Recommended next**: continue phase 2 (downstream consumer
wiring). The phase-1 reverted-consumer fix (`dbc1c3c029`) shows
the phase-2 wiring is partially in-progress.

---

## Cross-axis themes

### The three §3b-cond architectures

This week saw §3b-cond conditional-class scaffolds land at three
levels:

1. **`LinkEquivalence`** (PR #1536, my session) — Brunnian
   Borromean property conditional on Mathlib R-move
   formalisation.
2. **`BindingForceCarrierKnot`** (`addde9da`, `268fb993`) — A≥3
   light-nuclei binding conditional on per-rep Reeb phase wiring.
3. **`AvgCrossingPreservesGrade`** (`7d106185a6`, `c28d6fe0f1`) —
   sprint6 PR-D Step 4 axiomatised as a named opaque Prop.

Plus `BigbangHeatdeath`, the original §3b-cond class. The pattern
is now widely used. The lean-stub-conjecture-kind-check rule
catches drift; the class instances themselves become the
explicit "what we still need to prove" inventory.

### The α_EM thread's fragmentation problem

11 open α_EM PRs is a lot. The author is exploring multiple form
candidates in parallel. Recommendation: **coordinate /
consolidate** — pick the canonical thread (likely #1484 + #1495
+ #1505) and either land or close the rest.

### Mass-table extension changes the precision-target math

With 252 nuclides now in the pipeline, the L2 100× target is no
longer "4 isotopes" but "252". Many will be hard. The "shared
root cause" doc (`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`)
may now apply to a larger denominator.

---

## Recommended priority queue (next session)

1. **Land the α_EM canonical thread.** Pick 1–2 PRs from the 11,
   tighten, merge. The 0.31 ppb result on #1484 deserves to be on
   `main`.
2. **Refresh the L2 100× dashboard** with the 252-nuclide
   extension. The status doc + audit need an update.
3. **Strategy decision on Δ_λ Option E.** v1–v7 have all failed.
   Either commit to GAP-A-3 / Plan H first, or articulate
   why a v8 would learn something the v1–v7 didn't.
4. **Continue IwahoriHecke sprint** — sprint6 PR-D Step 4 is
   on a good trajectory.
5. **Merge the gap-i/ii/iii closure PRs** for the audit trail.
6. **Coordinate on the α_EM fragmentation** — consolidate or
   close.

---

## What this session contributed

- Three merged PRs (#1496, #1519, #1536) — 15 commits, 32
  kind-mismatches, 1 new validation rule, Brunnian Lean
  scaffold, narrative additions (cosmo-cone, Garside guide,
  Borromean confinement remark).
- Brunnian discharge tracked as TODO (`todos/content-todos.ts`).
- Remark audit + proposition-consolidation audit dispatched;
  remark audit returned 0 dangling, consolidation returned
  1 high-confidence + 2 review-worthy clusters (genus trio,
  embeddability/generation, Yekutieli/Chebyshev).
- This workplan doc.

Total session footprint: paper-infra cleanup ✅, no math edits
on top of the existing axes.
