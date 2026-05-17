# Coordination ledger — isotope-mass witness data

**Branch**: `claude/isotope-mass-witness-data-x5lCh`
**PR**: [#663](https://github.com/litlfred/qou/pull/663)
**Goal**: honest no-cal regen of `low-isotope-mass-table.witness.json`
under strict three-calibration discipline (CAL-1 m_e, CAL-2 q₀, CAL-3
Q_β; m_p and m_n are predictions, never inputs) + anti-staleness
infra to prevent the failure mode that produced the ¹H tautology.

## Scope map (2026-05-17 — /coordinate run after main rebase + Phase 5)

Owner invoked `/coordinate` after 31 commits landed on main. Walked
scope across siblings + posted intent on PR #671. Branch state:

- **31 commits ahead** of last push state (this branch, not yet
  reflected in PR view)
- **31 commits behind origin/main** (including #665 merge,
  cross-PR Lean fixes, new coordination ledger on main)
- **3 OUTDATED Gemini review comments** on PR #663 (already triaged
  in earlier coordination comment 4465620873)

### Sibling-PR state

| PR | Status | Bearing on #663 |
|---|---|---|
| **#665** | **MERGED** 2026-05-16 | N=4 ladder + n-strand BraidGroup foundation now on main; unlocks the Q_β substrate swap from form_a_cos (+306 ppm) → N=4 ladder (~7×10⁻⁶ ppm) per existing comment 4468003754 |
| **#672** | open | R&D inventory + YB d_1↔d_2 swap finding; orthogonal to #663 per comment 4469129860 |
| **#664** | open | Cherry-picked anti-staleness infra FROM #663; mergeable if #663 lands first |
| **#671** | open | Audits #663's "T1+T4 closure path"; Items A/B/C are R&D plan. **Coordination posted today** (comment 4469216060) — my Phase 4 work addresses Items A + C; Item B = audit GAP #17 |

### Main ledger from sibling session

Carl's coordination ledger landed on main as
`docs/coordination/1ppb-categorical-chain.md` (commit `4cc7561f`)
mentioning #663 directly. Open question for #663 author there:

> "Q_β substrate swap on #663: ship #663 as-is with form_a_cos
>  (residual +306 ppm), or wait for #665 to land then swap to the
>  N=4 ladder (residual ~7e-6 ppm)?"

**Answer (now actionable)**: #665 has merged. The N=4 ladder is on
main. Swapping `q_beta_substrate_cos_tightened_MeV()` →
`q_beta_full_chain_n4_MeV()` would tighten Q_β residual by ~4×10⁷.
This is a small follow-up; recommend deferring to a separate PR so
#663 ships the audit + Li_2^q + ν_SDP fix without entangling
substrate-helper migration.

### Gemini review triage (skill §5)

All 3 review threads are `is_outdated: true` — covered by earlier
coordination comment 4465620873:

| File:line | Verdict | Action |
|---|---|---|
| `low_isotope_mass_table.py` mtime docstring | accept | landed in 234282a3 |
| `probe_m2_codata_vs_cos_q_beta.py:120` | defer-to-source-PR | PR #662 (since merged) |
| `witness_dependency_drift.py` refactor | accept | landed in 234282a3 |

No new review comments since the original triage.

### Cross-PR findings this cycle (Phase 4 + Phase 5)

1. **ν_SDP notation fix** — disambiguates SDP-multiplicity ρ from
   categorical-density ρ_K (paper had both written "ρ" causing
   1700× value confusion). Edits landed in
   `atom-knot-mass-derivation.{md,ts,lean}`, proof sibling, and
   `rho_prefactor_structural_verifier.py` (with backward-compat
   alias key in witness).

2. **Symmetric Li_2^q replaces Faddeev Φ_q** per paper canon
   (2026-05-03 revision). Removes the pole artifact at
   |V̂_proton|=0.989 > q⁻¹=0.901 that gave spurious 1.50% closure.

3. **q-shuffle compound `*_q` on disjoint braids = concatenation**
   per `def:hq-bi-filtration` line 50. Full-order m(¹H) prediction
   landed (`hydrogen_qshuffle_compound.py`).

4. **173× ρ_K gap = paper open problem**, ruled out:
   - T7 = 0 for nucleons (Hecke-coefficient chain divergence at q=0)
   - Compound vs additive (≤0.4 MeV)
   - Plancherel vs Wenzl-tilde normalisation (1.3% shift)
   - Simple max dim_q at H_{3A} (90×-990× off)
   - 0.18% single-gen claim is circular per paper's own line 191-197

5. **Confinement-level multiplicative structure found** in
   `confined-knot-binding.md` line 108-120:
   `a(Z, N) = ∏_ℓ a_ℓ` where a_ℓ = V̂_confined / V̂_free at each
   level. This is the most-likely remaining candidate for the 173×
   factor; deferred to follow-up (research-level work).

### Next concrete task on queue

1. **Defer Q_β substrate-helper swap** to a separate PR (per
   recommendation above; #665 just merged, swap is now possible).
2. **Investigate `a_ℓ = V̂_confined/V̂_free` multiplicative
   structure** (confinement-level closure path) — owner-asked,
   research-level.
3. **PR #663 ready to merge** modulo CI green check. 31 commits
   ahead of last push reflected on remote.

## Scope map (2026-05-17 — Phase 4 audit + canonical-form + q-shuffle)

Owner directives this cycle:
1. "do a full audit": Phases 1-4 landed (54 files, ~150 claims,
   ~24 actionable gaps; INDEX in
   `docs/audits/2026-05-16-compute-paper-lean-audit-INDEX.md`)
2. "not adjacent only, full tail, canonical derived only" →
   switched T2/T3 from Faddeev Φ_q to symmetric Li_2^q per
   paper canon (2026-05-03 revision)
3. "validate the V̂_i terms, full tail, hydrogen step-by-step" →
   landed `hydrogen_step_by_step.py` (additive convention)
4. "knot convolution operator on compound braids, full order
   not LO" → landed `hydrogen_qshuffle_compound.py` with
   q-shuffle *_q for ¹H = proton ⊔ electron on 5-strand compound
5. "/coordinate PR 644" → ledger row added below (PR #644 CLOSED
   unmerged 2026-05-15, T5 work continued here)

### PR #644 cross-link

| Item | PR #644 (CLOSED 2026-05-15) | PR #663 (this branch) |
|---|---|---|
| Topic | Plan: 1 ppb mass closure — phased plan + Lean Phase 4 handover | Isotope-mass-table no-cal regen + canonical Li_2^q + *_q compound |
| T5 a_K convention | V1 backfill complete; 2.2 % gap on nucleons documented; V2/V3/V4 intractability flagged | Phase 4 audit confirms 2.2 % gap; recorded as audit GAP #17 |
| ⁴He Model B knot | Survey landed: 8_17 (0.186) > 10_123 > 8_18 > L6a4 (out) | not actioned here |
| Owner-decision items | Two left open at closure: (a) V1 vs V2/V3/V4 production wiring; (b) ⁴He final knot selection | Both items still open; logged as research-level in audit INDEX |
| Lean Phase 4 handover | scheduled to "separate PR" — never opened | covered by Phase 4 batches A-D agent reports (~50 files) on this branch |

**Action**: harvested nothing from #644 (commits never merged).
The Phase 4 audit on this branch is the de-facto continuation;
the same T5 V1 vs V2 owner-decision is now audit GAP #17.

### Headline empirical finding (2026-05-17)

m(¹H) prediction under the paper-canonical Li_2^q tower
(symmetric q-dilog, replaces retired Faddeev Φ_q):

| convention | m(¹H) pred | Δ vs CODATA 938.78 |
|---|---:|---:|
| LO additive (m_p + m_e − BE) | 5.92 MeV | −99.37 % |
| Full-order compound (*_q on 5-strand) | 6.30 MeV | −99.33 % |

The 932 MeV shortfall is **NOT** from additive-vs-compound
choice (same order of magnitude). The previous 1.50 % closure
was a Faddeev Φ_q artifact at |V̂_p|=0.989 > q⁻¹=0.901 (sitting
near the pole of Π(1−q⁻ᵏz)⁻¹). Canonical Li_2^q is mathematically
clean (no pole at q_0 inputs) but the truncated T1-T6 tower is
structurally off by ~170×.

Open hypotheses (per owner hint "hidden weighting/scaling factor"):
- T7 ≡ 0 for nucleons (skeleton extension confirmed this; ruled out)
- T8+ tail — not implemented
- V̂_i re-derivation under Li_2^q (current was tuned to Faddeev)
- Hidden q/h/z scaling factor lost in some derivation step
- Structural multiplicative factor (quark colour, gluon binding)
  outside brane-tower scope

## Scope map (2026-05-16 — fourth cycle, post-decisions checkpoint)

Owner closed PR #669 without merging on 2026-05-16; resolved six
decisions on this PR ("what decisions?" checkpoint). Cycle state:

| PR | Status | Bearing | Action this cycle |
|---|---|---|---|
| **#663 (this)** | open | — | threshold tightened to **1 ppb (1e-9)**; ¹H reverted from `derived` to `derivation_pending` (honest framework state); T5_e via V2 probed (not derived); Δ_λ catalog assembly **blocked** on upstream derivation; m_n + ⁴He documented as research items |
| **#666** | **MERGED** | χ^λ at H_9 for tritium (machine ε) — necessary but not sufficient for the Δ_λ catalog (Δ_λ derivation is the unsolved piece) | watch for follow-on PRs that close Δ_λ |
| **#668** | open | T6 closure infra (nucleon-only); doesn't extend to electron | cross-referenced; no action |
| **#669** | **CLOSED w/o merge** | (was) ⁴He anchor identification | backlog item: no active sibling owns ⁴He@H_12 |
| **#665** | open | n-strand BraidGroup Lean | tangential |

### Decisions executed (2026-05-16)

| # | Topic | Owner verdict | Branch action |
|---|---|---|---|
| 1 | PR #664 merge order | #663 first | none required; awaits merge |
| 2 | Δ_λ catalog on this PR | this PR | **blocked**: assembly requires Δ_λ derivation (still in flight); back-solving is fitting. Documented in audit + ledger. Pushed back to a follow-up PR after the derivation closes |
| 3 | m_n structural gap | document only | done (audit + witness) |
| 4 | T5 electron (option b) | try b if derived | probed: `aK_v2(0,0) = 1.0` works but `B_bulk(0,…)` ZeroDivisionError; **not derived** → falls back to (c) "exclude T5" |
| 5 | Threshold | **1 ppb** + within measurement error | landed; all 23 rows pending; honest framework precision floor |
| 6 | B(⁴He+) at H_12 | wait; cherry-pick if needed | backlog; no active sibling after #669 closed |

## Scope map (2026-05-16 14:55 UTC — third cycle, post-#666 merge)

| PR | Status | Bearing | Action this cycle |
|---|---|---|---|
| **#663 (this)** | open | — | rebased onto post-#666 main; m_p + ¹H closure landed (1.63 %); m_n full-tower closure landed with honest 62.97 % residual; T5/T6 electron + ⁴He@H_12 documented as research items |
| **#666** | **MERGED** | upstream dep — closes Δ_λ for tritium at H_9 (machine ε) | downstream catalog assembly (`delta-lambda-witness.json`) is a small bridge step; **not in scope** for this PR — would lift ²H/³H/³He B_pred from `delta_lambda_unavailable` |
| **#668** | open | T6 closure infra — derives `shift(Z,N) = 18Z + 21N + 1` categorically | nucleon-only formula; cannot directly close T6 for the electron; cross-referenced in audit |
| **#669** | open | ⁴He anchor identification — canonical pppnnn confirmed | explicit next step "apply #666's branching basis at H_12" — compute-heavy, separate PR |
| #665 | open | n-strand BraidGroup Lean | tangential |

## Scope map (2026-05-16 05:30 UTC — second cycle)

| PR | Status | Relationship | Action |
|---|---|---|---|
| **#663 (this)** | open | — | 6 commits on main; anti-staleness adoption extended to 3 scripts |
| #664 (`prop:hopf-jones-c3-categorical`) | **OPEN, today** | **cherry-picks from #663** (4 files: audit doc, drift validator, low_isotope_mass_table.py m_p guard, no-cal witness) — duplicate content | intent comment posted; merge-order suggestion (#663 first, #664 rebases to drop dupes) — no escalation, #664 attributed the cherry-pick explicitly |
| #665 (Lean `c_4 = b² + 1/2` N=4 rung) | **OPEN, today** | unrelated (Lean-only formalisation) | out of scope |
| #666 (Sub-lemma 2.1 H_9 tritium 30/30) | **OPEN, today** | **chain unblock**: closes Δ_λ for tritium → unblocks `binding_K_direct.py` (which I just adopted for upstream-witness-hash tracking) | intent comment posted; tritium row in `binding-K-direct.witness.json` will lift from `delta_lambda_unavailable` once a `delta-lambda-witness.json` catalog is wired |
| #657 (c_5/c_6 multi-link Jones) | **MERGED** | informational dep | none |
| #660 (Lean build fix) | **MERGED** | unrelated | none |
| #661 (c_2 = b² categorical) | **MERGED** | upstream dep (cherry-pick deduped by rebase) | none |
| #662 (cos Q_β source) | **MERGED** | upstream dep (cherry-pick deduped by rebase) | none |
| main `772bd656` (M2 mass table) | landed | parallel calibrated framing | not contradictory; cross-referenced |

**Scope collapsed.** All today's sibling PRs merged within the
session window. PR #663 stands alone against current main; the
cherry-picks that gave the branch its categorical-Q_β scaffolding
are now mainline.

## Rebase result

| Commit on branch before rebase | After rebase |
|---|---|
| 50c630b7 — wire(M2): cos Q_β source (cherry-pick from #662) | **dropped** (duplicate of `ee51ca3c` on main) |
| 670bc8a7 — fix(review): hoist mpmath/Q0_FLOAT (cherry-pick from #662) | **dropped** (duplicate of `c27494ac` on main) |
| 43006840 — fix(m2-probe): codata_constants (cherry-pick from #662) | **dropped** (duplicate of `98390c40` on main) |
| 8b5751e3 — proof: c_2 = b² categorical (cherry-pick from #661) | **dropped** (duplicate of `6807a720` on main) |
| ff29d9a1 — fix: Gemini review (cherry-pick from #661) | **dropped** (duplicate of `0f9749eb` on main) |
| a9c6ac2b — isotope-mass-table: honest no-cal regen + anti-staleness infra | **kept** |
| 164a834b — fix(ci): drift refresh + Gemini fixes on PR #663 | **partially kept** (drift-refresh content dropped because main's `50024712` + `760311ae` already cover it; the docstring fix + drift validator refactor preserved) |
| — | **new** `dda97390` — fix(ci): drift refresh after rebase onto post-#662 main (compute-audit-scan + derivation-chain-audit catch up on the +2 files now on the branch) |

Final branch state: **3 commits ahead of main**, all substantive (no
cherry-pick duplicates).

## Inconsistent findings — none

Two parallel mass-table framings now coexist on main + PR #663:

- **Calibrated M2** (main commit `772bd656`, witness
  `m2-codata-vs-cos-q-beta.witness.json`): per-derivation pathway
  using CODATA m_p / m_n as 4th/5th calibration inputs. Reports
  0.19 % MAE across {p, n, D, T, ³He, ⁴He} with the cos-tightened
  Q_β giving an extra 3.1 keV shift at ³He.
- **No-cal** (PR #663, witness `low-isotope-mass-table.witness.json`):
  refuses to consume m_p / m_n as inputs; reports all 23 rows
  `derivation_pending`. Documents the m_p chain's unclosed T1+T4
  frontier as the gate.

These are **deliberately different framings** under the same three-
cal discipline:
- Calibrated form acknowledges the n/p calibration leak and exists
  to track the binding-energy predictions and Q_β shift effects;
  m_p / m_n CODATA injection is documented as a tracked violation
  pending Workplan 0b.
- No-cal form is the honest "what can the framework predict from
  CAL-1/2/3 alone" view — currently nothing in the M column until
  the proton mass-endomorphism tower assembly closes.

Both framings consume the same substrate-Q_β producer (#662's
`q_beta_substrate_cos_tightened_MeV`) and the same c_2-c_4
categorical scaffolding (PR #655 c_3, c_4 + PR #661 c_2). The
no-cal form additionally guards against silent staleness with the
upstream-witness-hash mechanism.

**No §6 escalation needed.** The framings are complementary, not
contradictory.

## Anti-staleness adoption pattern

The infrastructure introduced by PR #663 is opt-in per script:

```python
import hashlib, json
from pathlib import Path

def _load_upstream(path: Path) -> tuple[dict, dict]:
    raw = path.read_bytes()
    w   = json.loads(raw.decode("utf-8"))
    return w, {
        "path":            path.name,
        "sha256":          hashlib.sha256(raw).hexdigest(),
        "size_bytes":      len(raw),
        "commitSha":       w.get("commitSha"),
        "scriptCommitSha": w.get("scriptCommitSha"),
        "computedAt":      w.get("computedAt"),
    }

# In the output witness dict:
"derivation_inputs": {
    ...,
    "upstream_witness_hashes": [hash_record_1, hash_record_2, ...],
}
```

The validator `witness_dependency_drift.py` walks every
`*.witness.json` and verifies recorded sha256 hashes against
current on-disk bytes. Single-script diagnostic; can be wired into
`witness-pipeline.yml` as a strict gate once adoption spreads.

**Candidate next adopters** (scripts that consume other witnesses):

| Script | Upstream witnesses |
|---|---|
| `low_isotope_mass_table.py` | proton-mass-codata-50dps ✓ (this PR) |
| `derived_masses.py` | proton-mass-codata-50dps, q-beta-predicted |
| `atomic_mass_via_rho_k.py` | atomic-tr-m-mpfr-50dps |
| `paper_six_term_isotope_sweep.py` | atomic-tr-m-mpfr-50dps, term6-habiro-residue |
| `binding_K_direct.py` | rho-k-h3a-refinement |

Adoption is a cross-PR effort — out of scope for #663.

## Next concrete task

**None blocking.** PR #663 has delivered both deliverables in the
"2 then 1" priority chain:

- **Task 2 (anti-staleness adoption)** — shared helper in
  `witness_base.py` + 3 adopter scripts + drift validator now
  checks both `derivation_inputs.*` and `data.*` hash locations.
  3 witnesses / 11 upstream hash records, 0 drift.
- **Task 1 (T1+T4 tower closure audit)** — finding documented in
  [`docs/audits/2026-05-16-t1-t4-tower-closure-plan.md`](../audits/2026-05-16-t1-t4-tower-closure-plan.md):
  the proton/neutron rows in `mass-formula-6term-mpfr-50dps.witness.json`
  carry `term2_single = 0.0` and `term3_pair = 0.0` with explicit
  error "No MPFR-native per-generator volumes found for Z=1, N=0".
  `derive_m_p_hecke_path_a` only sums T1+T4, giving m_p_hecke = 2.34
  and m_p/m_e = 1.169 vs CODATA 1836 — the 9-order-of-magnitude gap
  is **structural** (T2+T3 brane-tower contributions missing for
  single-strand atoms), not numerical. Closure is multi-PR
  research-level work.

Watch list (post-#663):

- **PR #664 lands** → cherry-pick duplicate (audit + drift validator +
  m_p guard + no-cal witness) deduplicates with main; #663 narrows
  to anti-staleness extensions + ledger.
- **PR #666 lands** → `delta-lambda-witness.json` wires in →
  tritium row in `binding-K-direct.witness.json` lifts from
  `delta_lambda_unavailable` to a derived B(T) value. Same for ³He
  (via #666 follow-up `I_pp` interface) and ⁴He (H_12, 3-interface).
- **MPFR-native per-generator volumes for {p, n}** (per
  `mass-formula-6term-mpfr-50dps.witness.json:term23_error`) →
  unblocks T2+T3 for proton and neutron → `m_p_hecke` grows from
  2.34 to a value giving m_p/m_e ≈ 1836 → ¹H row's
  `M_P_DERIVED_MAX_REL_DIFF` tightens from 1 % to ≤ 1 ppm.
- **CODATA-2027 Q_β tightening** — with PR #664's categorical c_3
  derivation, Story B is now favoured structurally even without
  experimental tightening.
