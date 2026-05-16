# Coordination ledger — isotope-mass witness data

**Branch**: `claude/isotope-mass-witness-data-x5lCh`
**PR**: [#663](https://github.com/litlfred/qou/pull/663)
**Goal**: honest no-cal regen of `low-isotope-mass-table.witness.json`
under strict three-calibration discipline (CAL-1 m_e, CAL-2 q₀, CAL-3
Q_β; m_p and m_n are predictions, never inputs) + anti-staleness
infra to prevent the failure mode that produced the ¹H tautology.

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
