# Coordination ledger — 2026-05-09 sibling PR cleanup

**Goal**: address every unresolved review comment on the three
sibling PRs opened today (2026-05-09) after the morning merges
(#600, #607, #612), then rebase + merge them in order. No proxies,
no shortcuts (per user direction).

## Scope (open siblings)

| PR | Branch | Title | Owner | Status (start) |
|---|---|---|---|---|
| [#616](https://github.com/litlfred/qou/pull/616) | `claude/kite-tail-reconciliation` | Kite-tail reconciliation: explain PR #546 round-3 vs PR #545 D(u) discrepancy | this session | dirty, 1 active comment |
| [#617](https://github.com/litlfred/qou/pull/617) | `claude/ppb-math-infrastructure-p3oQQ` | mass-table: derived m_p only, mark m_n & B(⁴He+) pending, wire duals + 50dps cache | this session | dirty, 3 active comments |
| [#618](https://github.com/litlfred/qou/pull/618) | `claude/wedderburn-lp-sdp-wiring` | v3 §3 item 4: Wedderburn pair-volume LP/SDP-EW wiring + alt-Δ_I Weinberg probe | this session | dirty, 9 active comments incl. 2 semantic |

## Already merged today (out of scope but recorded for traceability)

| PR | Merge SHA | Merged at | What it carried |
|---|---|---|---|
| [#607](https://github.com/litlfred/qou/pull/607) | [`48732e1d`](https://github.com/litlfred/qou/commit/48732e1d) | 2026-05-09 ~17:50 UTC | Lean trivial-skeleton-audit fix (12→0 violations); arity fixes; chirality probes; prepare-merge.md hardening |
| [#600](https://github.com/litlfred/qou/pull/600) | [`2899a681`](https://github.com/litlfred/qou/commit/2899a681) | 2026-05-09 ~17:55 UTC | mass-table-fitting-audit doc; ρ_K → Li extension; stale-witness regen; Δ_λ Options C/E |
| [#612](https://github.com/litlfred/qou/pull/612) | [`8ef67c30`](https://github.com/litlfred/qou/commit/8ef67c30) | 2026-05-09 ~18:00 UTC | atomic-braid-recipe-{p,n,d} chains (3 fully-trusted) |

## Classification (skill §2 axes)

| Sibling | Overlap with mine | Dependency | Cherry-pick candidate? |
|---|---|---|---|
| #616 ↔ #617 | low (different files; both touch `computations/*.py`) | none | no |
| #616 ↔ #618 | low (both touch `derivation-chain-audit.witness.json` only) | none | no |
| #617 ↔ #618 | medium (both add LP/SDP dual witnesses; both extend `lp_dual_witness_validator` flagged set) | none direct (no `uses[]` chain) | no |
| #617 ← #607 | resolved by base ref (already on `48732e1d`) | n/a (already absorbed) | n/a |
| All 3 ↔ post-#607+#600+#612 main | high — every rebase will regen `compute-audit-scan` + `derivation-chain-audit` + `cross-check-trM-1ppb` + `e0-calibration-audit` | none | no |

## Merge order (planned)

1. **#616** — smallest diff (5 files, 569+/8-), 1 active comment, isolated `kite_tail_reconciliation.py` + audit doc.
2. **#617** — base already on post-#607 main; 3 active comments (field-name unification + WitnessBuilder upgrade); rebase needs witness regen only.
3. **#618** — biggest fix surface; semantic correction of audit-doc `active_set` interpretation + implement off-diagonal Wedderburn Gram coupling (no diagonal proxy per user direction) + LP-statement contract alignment + WitnessBuilder + smaller cleanups.

After each merge: re-rebase the next two onto the new main (witness conflicts auto-resolved by the `prepare-merge` § 1·a loop).

## Fix surface per PR

### #616
- Switch `kite_tail_reconciliation.py` to `WitnessBuilder` so `auditOnly` + `scriptHash`/`commitSha`/`durationMs` are recorded automatically.
- Add at least one assertion (e.g. `sp.simplify(together_expr - cancel_expr) == 0` for the un-reduced↔cancel identity).
- Optional: replace `sp.expand(d)` with `as_powers_dict()` per Gemini's outdated suggestion (cleaner code; not behavior-changing).

### #617
- Unify field names: emit `derivation_status` on the row level (drop the `row_` prefix), and emit `B_derivation_status` consistently in pending-Δ status messages.
- Switch `low_isotope_mass_table.py` to `WitnessBuilder`.
- Drop dead `sweep_table` variable.
- Add `# noqa: E402` on post-sys.path imports.
- Refactor unreachable `else` block at line 188 into a clean `else`.
- Move `U_MEV` / `M_E_MEV` (consumed CODATA) out of `reference_constants_for_comparison_only` into `derivation_inputs` (they're inputs, not refs).

### #618
- **Semantic**: rewrite `docs/audits/2026-05-09-wedderburn-lp-ew-wiring.md` so `active_set` is described as "indices i with `y_star[i] > 0` (saturated Frobenius positivity constraints; corresponding primal `x_k` typically at zero)", not "channels with positive mass". Re-state the helium-4 finding accordingly: "53 of 55 pair channels are saturated-at-zero; only 2 carry nonzero mass."
- **Semantic**: rewrite the LP statement in both code comment (line 104) and audit doc (line 72) to match `solve_operator_selection_lp`'s actual contract: `min ⟨t, x⟩ s.t. Σ x_i = n_target, G x ≥ 0, x_i ≥ -M`.
- **Semantic + scope**: implement the off-diagonal Wedderburn Gram coupling that the comment block (lines 114–117) describes, instead of `np.diag(t) + ε I`. Pulls in pair-pair interactions per the actual Wedderburn factorization.
- Switch `wedderburn_lp_ew_wiring.py` to `WitnessBuilder`.
- Drop unused `standard_young_tableaux` import.
- Add `# noqa: E402` on post-sys.path imports.
- Move sympy → numpy conversion before the per-generator `M @ matrices[g]` loop (perf).
- Update witness `description` to lead with helium-4 + atom sweep, not "proton EW-sector".

## Watch state (skill §8)

- `origin/main` watch is armed via Monitor (poll every 5 min); will integrate any new commits per skill §3 checklist.
- No new sibling PRs opened since this ledger was created.

## Post-merge KLR-positivity correction (follow-up to #618)

After all six PRs merged, the user pointed out that KLR
(Khovanov-Lauda-Rouquier) positivity should guarantee non-negativity
of certain Wedderburn observables — contradicting #618's "LP
unbounded for mixed-sign $t$" finding. Investigation confirmed:

- **#618's finding was a setup error**, not an LP-theory issue.
  The supply vector `t_k = pair["full"]` is a sum of seminormal-
  basis matrix entries (`(M_i M_j)_{12}` etc.), **not** a Markov
  trace. KLR positivity does NOT apply to matrix-entry projections
  on a chosen seminormal basis (which can have signs).
- **The KLR-positive replacement** is `t_k = tr_M(σ_i σ_j) =
  Σ_λ y_λ · χ_λ(σ_i σ_j)`, the actual pair Markov trace. By KLR
  positivity (operators in the canonical-basis cone are non-
  negative at q > 0), `t_k ≥ 0` for every pair (verified:
  `min t_k = +5 × 10⁻⁶` for triton).
- **Plus** `M_bound = 0` (enforces `x ≥ 0`, matching the natural
  "operator selection" reading of `prop:knot-operator-lp-selection`)
  is needed alongside the KLR fix — without it, low-`t` entries
  still let the LP scale linearly with `M`.

**Result**: with both fixes, strong duality holds on every atom in
the computable sweep (proton, neutron, deuteron, triton — all gap
= 0). ⁴He remains deferred-by-budget pending `pyhecke_native`
installation.

**Branch**: `claude/klr-positive-supply-vector` (this entry will be
updated with the merge SHA when the follow-up PR lands).

**Files**:
- [`computations/wedderburn_lp_ew_wiring.py`](../../computations/wedderburn_lp_ew_wiring.py)
  — added `_klr_positive_supply_vector(...)`, switched LP calls
  to `M_bound=0.0`, kept legacy matrix-entry sum under
  `t_legacy_matrix_entries_*` for comparison.
- [`docs/audits/2026-05-09-wedderburn-lp-ew-wiring.md`](../audits/2026-05-09-wedderburn-lp-ew-wiring.md)
  — appended §0 KLR-positivity correction with post-fix table
  (gap = 0 for every atom).
- [`computations/wedderburn-lp-ew-wiring.witness.json`](../../computations/wedderburn-lp-ew-wiring.witness.json)
  — regenerated; assertions
  `lp_strong_duality_all_klr_atoms` (4/4),
  `klr_positivity_supply_vector_all_atoms` (4/4),
  `weinberg_minimal_delta_I_optimal` (✓) all pass.

**No sibling-PR coordination needed**: all six PRs from today are
merged; this is a forward-only correction landing on top of the
merged #618 content. The audit doc patch documents the historical
sequence (PR #618 first attempt → KLR correction).
