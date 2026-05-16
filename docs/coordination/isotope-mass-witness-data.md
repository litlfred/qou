# Coordination ledger — isotope-mass witness data

**Branch**: `claude/isotope-mass-witness-data-x5lCh`
**PR**: [#663](https://github.com/litlfred/qou/pull/663)
**Goal**: honest no-cal regen of `low-isotope-mass-table.witness.json`
under strict three-calibration discipline (CAL-1 m_e, CAL-2 q₀, CAL-3
Q_β; m_p and m_n are predictions, never inputs) + anti-staleness
infra to prevent the failure mode that produced the ¹H tautology.

## Scope map (2026-05-16 04:30 UTC)

| PR | Status | Relationship | Action |
|---|---|---|---|
| **#663 (this)** | open | — | rebased onto current main; 3 commits net |
| #657 (c_5/c_6 multi-link Jones + CODATA-Q_β-floor) | **MERGED** | informational dep (same Q_β closure story; #657's "underdetermined at CODATA Q_β floor" finding lands on main and is consistent with my pending-m_p framing) | no cross-PR ask needed |
| #660 (Lean build fix) | **MERGED** | unrelated | out of scope |
| #661 (c_2 = b² categorical proof) | **MERGED** | upstream dep (cherry-picked into my branch; now on main via merge — duplicate commits dropped by rebase) | out of scope |
| #662 (cos Q_β source wire + 9 content blocks) | **MERGED** | upstream dep (cherry-picked into my branch; now on main via merge — duplicate commits dropped by rebase) | out of scope |
| (new main commit) `772bd656` — M2 mass table 0.19 % MAE | landed on main | parallel framing (calibrated form using CODATA m_p / m_n) | not an inconsistent finding — explicit different framing; cross-referenced in PR body |

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

CI should now go green with `dda97390`'s drift refresh. Once that
lands, the next step on this branch is:

- **None blocking.** PR #663 is ready for review. The remaining
  open questions (close T1+T4 in `build_proton_mass_50dps_chain.py`
  → lift ¹H from pending to derived) are out of scope and belong
  to a separate mass-endomorphism PR.

Watch list (next sibling-PR cycle):
- Workplan 2 Phase 2 50-dps `m_e^Hecke` lift — when it lands, this
  branch's `M_P_DERIVED_MAX_REL_DIFF` threshold tightens from 1 %
  to 1 ppm and ¹H becomes the first genuinely-derived row.
- CODATA-2027 Q_β tightening (per PR #657's deferred R&D) — would
  break the "Story A vs Story B" tie at the c_2 fit level.
