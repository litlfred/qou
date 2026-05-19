# Coordination ledger — `claude/show-mass-sweep-table-2xEBG` (PR #781)

Goal: align mass tables with canonical pipeline; remove legacy compute;
surface Borromean p, n predictions in the recursive atom-knot atlas;
extend toward full AME 2020 coverage; vendor AME 2020; stand up
distributable `qou-mass` library.

## Sibling scope map (per `local/coordinate` §2)

| PR | Title | Classification | Relation |
|----|-------|----------------|----------|
| #788 | I12 audit batch + I13 recursion + Borromean class | **dependency** | Adds `class BorromeanMassFormula` (Lean §3b-cond for `conj:borromean-baryon-mass-formula`, which #781 cross-references). I13 naming collision resolved: #788 = incomplete-coverage self-recursion, #781 = witness-provenance audit renamed I13 → I14. |
| #777 | v7 two-leg precision (L1 compute + L2 100× experimental) | **shared-data** | Borromean predictions (251 ppb m_p / m_n) consumed by #781 atlas; #781 doesn't propose a 7th Δ_λ ansatz. |
| #772 | 210× scale-gap root cause audit | **upstream-clarification** | Documents ρ_K·m_e ≠ E_0^(N=0); #781 uses the Borromean closure consistently with this framing. |
| #787 | Δ_λ categorical closure on deuteron (NEGATIVE) | **complement** | #787's Δ_λ track failed at 97 % miss on D; #781's Kashaev/ρ-F track lands at +1.09 %. Different formula tracks, same target. |
| #761 | combined Rust kernel work (Hoefsmit / GP / chirality / v6) | **infrastructure** | Touches `tools/hecke-engine/`; #781 uses `markov_peel` Python path. Mostly orthogonal. |
| #786 | Lean backlog audit + 4 sorry discharges | **weak-overlap** | Lean side of conjectures; no direct content overlap. |
| #774 | i3 audit (rationale-backed skips) | **weak-overlap** | Audit infra; tightens i3, not i14. |
| #736 | orphan conjectures + 29 bib entries | **weak-overlap** | Bibliography additions; no compute overlap. |

## Coordination comments posted

- #788 — [coordination-1](https://github.com/litlfred/qou/pull/788#issuecomment-4484038833): I13 → I14 rename in #781 (per `local/coordinate` §6 escalation; I14 is provenance, I13 stays self-recursion); ack BorromeanMassFormula class dependency.
- #777 — [coordination-1](https://github.com/litlfred/qou/pull/777#issuecomment-4484040443): ack Borromean values reuse; #781 doesn't propose a 7th Δ_λ ansatz; surface knot-vol _precision finding.

## Review-comment triage (PR #781) — [status comment](https://github.com/litlfred/qou/pull/781#issuecomment-4484042402)

| Thread | Reviewer | Verdict | Status |
|---|---|---|---|
| `engine` enum in `atomic-mass-gb-nf.ts` | copilot | accept | fixed in `b41477565+1` (this batch): `"python+mpmath"` |
| `content-block-label-audit` failure | copilot+gemini (×2) | reject-with-reason | pre-existing, out of scope; tracked in I7 stale-probe `md_missing` |
| Hardcoded `data.rows.2` for D | gemini | accept-with-modification | docstring on DEFAULT_ATOMS + note in registry.ts in this batch |

## Open follow-ups (filed here; not in #781's scope)

1. **Knot-vol _precision propagation.** Most knot-vol consumers (`mass_table_ppb.py`, `alpha_cluster_recursion.py`, `family_1_kashaev.py`, `low_isotope_binding_sweep.py`, `magic_A_formula.py`) use **hardcoded f64** for VOL_BORROMEAN / VOL_7_SQ_1 / VOL_4_1 instead of pulling from `hyperbolic_volumes.py` (mpmath 50dps Clausen). For L2-subgoal-1 (≥ 780 ppb CAL-2 floor) tolerable; for L2-subgoal-2 (sub-CAL-2) blocking. **Active task: fix per user directive 2026-05-19 "fix knot vol issues".**
2. **(Z, N)-keyed lookup** for value-registry instead of `data.rows.<index>` indexing. Gemini #781 review #3 partial accept; mechanical fix deferred.
3. **`prop:` vs `conj:` prefix mismatch** in 7 witnesses (flavor-dressed-mass-from-substrate-split family). Out of #781 scope; needs per-witness retarget across the workplan-0b probe-script set.

## Watcher state

- `local/watch` on origin/main (current baseline `4fdce59b15e59ae9ab33742b3f76bccecee25a1d`, the AME 2020 upload commit).
- 5-min poll; §3 overlap classification per new main commit.

## Session work plan (TodoWrite-equivalent, in priority order)

- [x] Commit unified prediction semantics + AME 2020 vendor + I13→I14 rename + Thread 1 fix + Thread 3 docstring + 6Li recompute + atlas refresh
- [ ] Knot-vol _precision refactor: route all consumers through `hyperbolic_volumes.py` (per user 2026-05-19)
- [ ] Per-Z shard producer skeleton (canonical_isotope_witness.py extending canonical_mass_table_extended)
- [ ] Atlas per-Z sections layout (3300-row presentation)
