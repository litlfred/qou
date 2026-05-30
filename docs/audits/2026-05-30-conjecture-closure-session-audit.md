# Conjecture-closure session audit (2026-05-30, post-#1451/#1467 merge)

Session-summary audit captured after merging the m_K/m_π wire ([#1451](https://github.com/litlfred/qou/pull/1451)) and SnapPy migration ([#1467](https://github.com/litlfred/qou/pull/1467)), in response to the user's "close any more conjectures?" prompt.

## Tier-A source-conjecture status (post-merge)

Per [`docs/workplans/2026-05-30-source-conjecture-closure-plan.md`](../workplans/2026-05-30-source-conjecture-closure-plan.md) §"Phase 1 — Tier A", 4 leaves were earmarked as "provable now":

| # | Conjecture | Status (2026-05-30 18:50 UTC) | Notes |
|---|---|---|---|
| 1 | `conj:pontryagin-dual-coxeter-character` | ✅ **closed** as `thm:` in [`ad094372d`](https://github.com/litlfred/qou/commit/ad094372d) | sorry-free via `Equiv.Perm.sign` + `ZMod 2` finite case analysis |
| 2 | `conj:atom-braid-exterior-algebra` | ✅ **structurally closed** (verified cases sorry-free) | 0 actual tactic sorries — D / T / ³He / ⁴He proven via Pascal-row totals (`binomial_sum_pow_two`); general case is the open §3b-cond class instance per CLAUDE.md, not a missing proof |
| 3 | `conj:dilogarithm-archimedean-limit` | ⚠ **still open** | Standard Faddeev-Kashaev limit `(1-q) log Φ_n(x; q) → Li_2(x)`. Needs Mathlib analysis infra: q-Pochhammer + Riemann-sum convergence + Li_2 series. **Not single-session work** despite the workplan's 50-150 LOC estimate — the estimate assumes the analysis infra exists; in practice it would have to be authored first. Demote to Tier B. |
| 4 | `conj:averaging-resonance-rule` | ✅ **closed** in [`c662572c5`](https://github.com/litlfred/qou/commit/c662572c5) | + Sprint 1 IwahoriHecke skeleton |

**Net Tier-A progress today**: 3/4 leaves effectively closed (Pontryagin, averaging-resonance-rule explicitly; atom-braid-exterior-algebra structurally via sorry-free verified cases). Only `dilogarithm-archimedean-limit` remains, and should be re-classified Tier B (Mathlib analysis infrastructure dependency).

## Numeric drift flagged: `partition-sum-proton-residual.lean:89`

Spot-checked during the session looking for tractable single-session closures. The theorem `proton_tower_residual_frobenius` ([lean source line 80](../../content/quantum-observable-universe/mass-theory/partition-sum-proton-residual.lean#L80)) asserts:

```lean
∃ ε, |ε| ≤ electronMass * (4 / 1000) ∧
     protonCodata - protonTowerMass = electronMass * frobeniusCoCasimirTraceN3 + ε
```

with the literal values:
- `protonCodata = 938.27208816`
- `protonTowerMass = 938.7228`
- `electronMass = 0.51099895`
- `frobeniusCoCasimirTraceN3 = 2 + 1/(qSubstrate + 1/qSubstrate)` ≈ `2.49729` at `qSubstrate = 1.10998`

Plugging in:

```
LHS  = protonCodata - protonTowerMass                 ≈ -0.45071 MeV
RHS₀ = electronMass · frobeniusCoCasimirTraceN3       ≈ +1.27613 MeV
ε    = LHS - RHS₀                                     ≈ -1.72684 MeV
|ε|                                                   ≈  1.72684 MeV
```

The target bound is `electronMass · 4/1000 ≈ 0.00204 MeV`. The actual `|ε| ≈ 1.727 MeV` is **~840× larger than the bound**.

The docstring comment claims `|ε| ≈ 0.00179 MeV`, which is consistent with a different `protonTowerMass`. Working backwards from the documented residual `1.2779 MeV`:

```
protonTowerMass_expected = protonCodata + 1.2779 ≈ 939.5500 MeV
```

The literal `protonTowerMass = 938.7228` appears to be **stale** — likely from an earlier version of the proton-tower formula that produced a different mass. The relationship in the theorem requires the literal to be updated to match the current `frobenius_partition_sum.py` output, after which the `by sorry` bound proof should close by `norm_num`.

**Why this matters**: a future agent attempting to close the `by sorry` on line 89 would get a goal that's unprovable as stated (the bound is violated by 3 orders of magnitude). The literal needs to be refreshed first.

**Action item (not done in this session — outside scope of doc-audit branch)**:

1. Run `folio-assistant/computations/frobenius_partition_sum.py` to get the current canonical `m_p_tower` value.
2. Update `protonTowerMass` literal in `partition-sum-proton-residual.lean` to match.
3. Close the `by sorry` on line 89 via `norm_num` (the bound should hold after the literal refresh).
4. If the closure fails because the inequality is genuinely violated even with the refreshed value, the bound `4/1000` itself needs reconsideration — file as a separate conjecture audit.

## SDP rank-via-eigenvalues axiom (re-attempt)

Per the user's session-2 selection, attempted to discharge `axiom Matrix.PosSemidef.rank_via_eigenvalues` in [`SDPRankEquality.lean:172`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/SDPRankEquality.lean#L172) via the candidate composition:

```lean
theorem Matrix.PosSemidef.rank_via_eigenvalues_proven
    {n : ℕ} {M : Matrix (Fin n) (Fin n) ℝ} (hM : M.PosSemidef) :
    M.rank = (Finset.univ.filter (fun i => 0 < hM.1.eigenvalues i)).card := by
  rw [hM.eigenvalues_pos_filter_eq_ne_zero_filter]
  exact hM.1.rank_eq_card_non_zero_eigenvalues   -- candidate Mathlib name
```

**Blocker (unchanged from earlier in session)**: container's network policy blocks
`leansearch.net` / `loogle.lean-lang.org` (HTTP 403 via egress proxy; Python sees SSL cert chain failure since the proxy intercepts with self-signed cert). The Lean LSP wrapper can't start because `lake` isn't in its child-process PATH (elan installed but PATH not propagated).

**Verdict**: tractable in principle (1-line composition once the exact Mathlib name is verified), but blocked by the container environment. Carries the [#1502](https://github.com/litlfred/qou/pull/1502) audit doc's recommendation — verification needs a container with Lean toolchain + Mathlib local cache provisioned.

## Recommendations

1. **Demote `conj:dilogarithm-archimedean-limit` from Tier A to Tier B** in the source-conjecture-closure-plan workplan. Closing it requires Mathlib analysis infra (q-Pochhammer + Riemann-sum + Li_2 series) that doesn't exist; the original "50-150 LOC" estimate was optimistic.
2. **Promote `conj:atom-braid-exterior-algebra` framing** in the workplan from "Tier A — provable now" to "Tier A — verified cases done, general case is open §3b-cond conjecture by design". The block already meets the §3b-cond standard; further "closure" is the general categorical proof, not a missing sorry.
3. **Refresh `partition-sum-proton-residual.lean` literals** per the action item above. Single-session work; would close the `by sorry` on line 89.
4. **Provision a Lean-stable container** (preloaded toolchain + Mathlib cache) for the next conjecture-closure session — this would unblock the SDP rank discharge and several other "1-line composition" candidates.

## Coordination

- Workplan: [`docs/workplans/2026-05-30-source-conjecture-closure-plan.md`](../workplans/2026-05-30-source-conjecture-closure-plan.md)
- Earlier sibling audit on uniqueness backlog (T_w SDP):
  [PR #1445](https://github.com/litlfred/qou/pull/1445) +
  [PR #1502](https://github.com/litlfred/qou/pull/1502)
