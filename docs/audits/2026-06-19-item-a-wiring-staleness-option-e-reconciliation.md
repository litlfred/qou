# Item-A artifact wiring + staleness audit; Option E framing reconciliation (2026-06-19)

**Date:** 2026-06-19
**Scope:** read-only audit of the H₆ deuteron "item-A" compute artifacts on
`main`, plus reconciliation of the Δ_λ "Option E" framing between the
coordination ledger and `CLAUDE.md`. Nothing wired; no compute changed; `CLAUDE.md`
not edited.
**Follows:** the #2485 merge (first live H₆ deuteron χ_λ) and the sibling
𝓑_n−𝓑_p parity-obstruction work
([`2026-06-19-bn-bp-brane-tower-parity-obstruction.md`](2026-06-19-bn-bp-brane-tower-parity-obstruction.md)).
Requested by owner.

## 1. Wiring audit — who consumes the item-A artifacts

| Artifact | Consumers | Verdict |
|---|---|---|
| `joint-tower-sdp-h6-h9.witness.json` | 4 content blocks (`phi-q-categorical-truncation`, `conj-canonical-knot-id-sdp`, `conj-rho-prefactor-structural`, `mass-endomorphism-conjecture`) + 6 scripts | **well-wired** |
| `chi-deuteron-free-h6-*.witness.json` | `chi_free_via_lr.py` → `tr_m_atom_via_transfer.py`, `chi_atom_transfer.py`, `chi_atom_fmatrix_recoupling.py`, `test_7li_orig.py` | **wired** (tr_M atom pipeline) |
| `derived-chi-catalogue-bridge-factor-omega.witness.json` | only its own producer | **orphaned — no downstream consumer** |

The sibling's fresh probes (`h6_deuteron_free_word_chi_lambda_probe.py`,
`bn_minus_bp_brane_tower_parity_probe.py`, `bn_minus_bp_winding_iterate_probe.py`)
are `computations/probes/` investigations — unwired **by design**, not a finding.

## 2. Staleness audit

| Witness | Recorded provenance | Verdict |
|---|---|---|
| `derived-chi-catalogue-bridge-factor-omega` | `scriptHash` `6497bfb59a26` | **STALE** — producer `derived_chi_catalogue_bridge_factor_deuteron.py` now hashes `f9a3152cf53d`; the producer content changed since the witness was generated. Re-run to confirm the ω table is current. |
| `chi-deuteron-free-h6-at-q0-50dps` | none (carries `_provenance` but no `scriptHash` / `scriptCommitSha` / `computedAt`) | **un-trackable** — invisible to the witness-pipeline staleness detector |
| `joint-tower-sdp-h6-h9` | `computedAt` only (2026-06-02), no `scriptHash` / `scriptCommitSha` | **un-trackable** |

### Recommended actions (for a compute-env agent — blocked in the audit env, which has no `pyhecke_native` / `cvxpy`)

1. **Re-run** `derived_chi_catalogue_bridge_factor_deuteron.py` to refresh the
   stale ω witness, then decide: **wire** the ω table into the binding/Δ_λ
   pipeline, or **document** it as a standalone Littlewood–Richardson
   bound↔free factorization reference. It is rigorous **exact q-Laurent**
   work, held-out-cross-validated — **do not prune it** the way `fc43a2f4`
   pruned the float64 H₆ duplicate (that was a redundant float64 recompute;
   this is not).
2. On the next re-run of the free-χ and joint-tower producers, route them
   through `WitnessBuilder` so they carry `scriptHash` / `scriptCommitSha`
   and become staleness-trackable.

## 3. Option E framing reconciliation (Δ_λ gate)

`CLAUDE.md` §"Δ_λ gate" lists the productive directions as "GAP-A-3 / GAP-A-4 …
and **Option E (Kashiwara crystal)**." The
[`option-e.md`](../coordination/option-e.md) ledger shows this specific framing
is **partially stale**:

- **PROBE 4 (Δ_λ from the Kashiwara-crystal / KL-multiplicity weight) is
  pruned** — KL-positivity wall (2026-06-16): the target Δ_λ = sgn·dim is
  mixed-sign (n=3, n=6), but KL multiplicities are non-negative, so a
  Σ_w n^w_λ·X_w sum supplies at most |Δ_λ| = dim (already the f^λ factor),
  never the chirality sign. Engine-verified (PR #2381); the mixed-sign premise
  is Lean-proved sorry-free in `S5SO3FiberAction.lean` (PR #2416).
- **Option E as a program is not dead** — the ledger pivots the live frontier
  to **PROBE 2 (A=4 interface operator)** (sibling cluster #2369/#2371/#2372)
  and the categorical `conj:s5-so3-fiber-action`.
- **The deuteron is NOT closed** — the prior "+0.91% via E₀×q⁻¹" was an
  overclaim, corrected 2026-06-17; v9 `(1+q)/2` is a near-match **fit**
  (structural derivation refuted, PROBE 1 / PR #1707).

**Suggested `CLAUDE.md` refinement (owner decision — NOT applied here):** reword
"Option E (Kashiwara crystal)" so it reflects that the crystal / KL-weight
sub-mechanism is pruned, and the live Option-E frontier is the **A=4 interface
operator (PROBE 2)**. Left to the owner per the read-only scope of this audit.

## Discipline

- Read-only audit; no compute changed, nothing wired, `CLAUDE.md` not edited.
- Corpus-grep verified: the Option E verdict is read directly from
  `option-e.md` and its cited audits, not relayed second-hand.
