# T1 (n=6, n=7 Frobenius codim closure) — manual build review

**Status:** **build-pending.** Local `lake build` not run (sandbox has no
network for elan toolchain download). Manual review below; CI run is
the user's call (`lean_ci.yml` is `workflow_dispatch` only — no auto-trigger).

**Commit:** [`4e876b6`](https://github.com/litlfred/qou/commit/4e876b6489edbff4ba8bf51708af185422116540) on `claude/upgrade-klr-algebras-OdYFc`.

**File:** `content/quantum-observable-universe/braids-and-knots/frobenius-codim-universal.lean`

## 1 — Mathematical verification

`dim_q(λ)` for partitions of n=6 (eleven partitions) and n=7 (fifteen
partitions) computed via the q-hook-length formula
`dim_q(λ) = [n]_q!/∏ [h(x)]_q`.

**At q=1 (S_n character degrees):**

| n | Partitions | dim values at q=1 | sum-of-squares check |
|---|-----------|-------------------|----------------------|
| 6 | (6),(5,1),(4,2),(4,1,1),(3,3),(3,2,1),(3,1,1,1),(2,2,2),(2,2,1,1),(2,1,1,1,1),(1⁶) | 1,5,9,10,5,16,10,5,9,5,1 | 1+25+81+100+25+256+100+25+81+25+1 = 720 = 6! OK: |
| 7 | 15 partitions of 7 | 1,6,14,15,14,35,20,21,21,35,15,14,14,6,1 | 1+36+196+225+196+1225+400+441+441+1225+225+196+196+36+1 = 5040 = 7! OK: |

Both Burnside identities check out. Conjugate pairs verified (e.g.
`(5,1)↔(2,1,1,1,1)` both = 5; `(3,3)↔(2,2,2)` both = 5).

## 2 — Lean syntactic review

The new declarations follow the existing n=4 / n=5 pattern at lines 240–345
of the same file:

| Aspect | n=4/n=5 (existing) | n=6/n=7 (new) | Match? |
|--------|--------------------|----------------|--------|
| `noncomputable def heckeH<n>DimQ (q : ℝ) (i : Fin <p>)` | yes | yes | yes |
| `match i with \| ⟨k, _⟩ => …` for k=0..p-1 | yes | yes | yes |
| Catch-all `\| ⟨_+<p>, h⟩ => absurd h (by omega)` | yes | yes | yes |
| `@[simp] heckeH<n>DimQ_<digit>` lemmas via `rfl` | yes | yes | yes |
| Final theorem body `rw [Fin.sum_univ_<p>]; simp; ring` | yes | uses custom `Fin_sum_univ_eleven`/`_fifteen` | partial |

**The single divergence from the existing pattern:** Mathlib provides
`Fin.sum_univ_two`/`_three`/`_four`/`_five`/`_six`/`_seven`/`_eight`
as pre-baked `rfl`-or-`simp`-provable lemmas, but **not**
`Fin.sum_univ_eleven` or `Fin.sum_univ_fifteen`. The branch adds two
`private` lemmas:

```lean
private lemma Fin_sum_univ_eleven {M : Type*} [AddCommMonoid M]
    (f : Fin 11 → M) :
    ∑ i, f i = f 0 + f 1 + … + f 10 := by
  simp [Fin.sum_univ_succ, Fin.sum_univ_zero, add_assoc]
```

(and the analogous `Fin_sum_univ_fifteen`).

## 3 — Risk assessment

**Low risk (very unlikely to fail):**
- The 26 `@[simp] heckeH<n>DimQ_<digit>` lemmas via `rfl` — the
  `match` in the def reduces definitionally to the explicit RHS for
  literal Fin index arguments. Identical pattern as existing.
- `omega` closing `_+11 < 11` and `_+15 < 15` impossibility — these
  are arithmetic over ℕ, well within `omega`'s decidable fragment.

**Medium risk (most likely failure mode):**
- `simp [Fin.sum_univ_succ, Fin.sum_univ_zero, add_assoc]` may not
  fully unfold the 11-fold (resp. 15-fold) recursion to the
  left-associated `f 0 + f 1 + … + f 10` form. Specifically, after
  applying `Fin.sum_univ_succ` repeatedly, the indices become
  `Fin.succ 0`, `Fin.succ (Fin.succ 0)`, …, which need to reduce to
  the literals `1, 2, … : Fin 11`. The `add_assoc` simp lemma is
  meant to rebracket, but `simp` is finicky about `AddCommMonoid`
  associativity directionality.

**Low-medium risk:**
- The final `rw [Fin_sum_univ_eleven]; simp; ring` may not close if
  the `simp` after `rw` doesn't normalise the divisions enough for
  `ring`. Existing n=5 uses the exact same closing tactic and works,
  so the precedent is favourable. The (3,2,1) self-conjugate term
  in n=6 introduces a triple product `(q^3+q⁻³)·[4]_q·[2]_q` that
  `simp` should handle since it appears identically on LHS and RHS.

## 4 — Fallback tactics if `Fin_sum_univ_*` `simp` fails

**Option 4A — explicit `rw` chain** (most robust, brittle but always works):
```lean
private lemma Fin_sum_univ_eleven (f : Fin 11 → M) :
    ∑ i, f i = f 0 + f 1 + f 2 + f 3 + f 4 + f 5
                + f 6 + f 7 + f 8 + f 9 + f 10 := by
  rw [Fin.sum_univ_succ, Fin.sum_univ_succ, Fin.sum_univ_succ,
      Fin.sum_univ_succ, Fin.sum_univ_succ, Fin.sum_univ_succ,
      Fin.sum_univ_succ, Fin.sum_univ_succ, Fin.sum_univ_succ,
      Fin.sum_univ_succ, Fin.sum_univ_succ, Fin.sum_univ_zero, add_zero]
  rfl
```

**Option 4B — bridge via `Fin.sum_univ_eight`** (Mathlib-provided):
```lean
private lemma Fin_sum_univ_eleven (f : Fin 11 → M) : … := by
  -- 11 = 3 + 8: peel 3 indices, then use sum_univ_eight on the rest
  rw [Fin.sum_univ_succ, Fin.sum_univ_succ, Fin.sum_univ_succ]
  simp only [Fin.sum_univ_eight]
  ring  -- or rfl after rebracketing
```

**Option 4C — `decide` on `Fin 11`** (only works if M = ℝ explicitly,
not for generic `AddCommMonoid M`).

## 5 — If the inner `ring` fails after `simp`

This is the SAME pattern as the existing n=5 case which builds, so
should work. If it doesn't:

```lean
theorem hecke_n6_frobenius_codim (q : ℝ) : … := by
  rw [Fin_sum_univ_eleven]
  simp only [heckeH6DimQ_zero, heckeH6DimQ_one, heckeH6DimQ_two,
             heckeH6DimQ_three, heckeH6DimQ_four, heckeH6DimQ_five,
             heckeH6DimQ_six, heckeH6DimQ_seven, heckeH6DimQ_eight,
             heckeH6DimQ_nine, heckeH6DimQ_ten]
  field_simp        -- normalises divisions
  ring
```

## 6 — Recommended next steps

1. **Trigger CI manually** via `lean_ci.yml`'s `workflow_dispatch`
   on branch `claude/upgrade-klr-algebras-OdYFc`. The CI installs
   elan and runs `lake build`.

2. **If CI passes**: T1 done. Move to the actual 1ppb frontier
   (Strategy-3 prediction errors per
   [`docs/audits/2026-05-09-proton-m_e-anomaly.md §9.5`](2026-05-09-proton-m_e-anomaly.md)).

3. **If CI fails on `Fin_sum_univ_*`**: apply Option 4A / 4B in a
   follow-up commit.

4. **If CI fails on `ring`**: apply the §5 fallback (explicit
   `simp only [...]; field_simp; ring`).

## 7 — Cross-references

- T1 commit: `4e876b6` "T1: extend Frobenius codim closure
  to n=6 and n=7"
- Existing n=2..5 closures: lines 196–345 of the same file
- n=6 fallback target: `frobeniusCoCasimirTraceFallback` opaque in
  `knot-mass-formula-unified.lean:36`
- 1ppb plan T1 entry: `docs/audits/2026-05-09-mass-table-1ppb-audit.md §5`
- Lean CI workflow: `.github/workflows/lean_ci.yml` (workflow_dispatch only)

## 8 — Note on Lean toolchain version

`lean-toolchain` pins `leanprover/lean4:v4.24.0`, but
`lean_ci.yml:51` declares `LEAN_VERSION: "leanprover/lean4:v4.16.0"`.
The CI workflow's env var is unused (the actual toolchain comes from
`lean-toolchain` via elan), but the discrepancy is worth noting for
future cleanup.