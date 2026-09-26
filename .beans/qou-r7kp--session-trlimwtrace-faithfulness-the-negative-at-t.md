---
# qou-r7kp
title: 'Session: trLim/wtrace faithfulness -- the negative at the carrier'
status: completed
type: milestone
priority: normal
created_at: 2026-09-26T14:15:29Z
updated_at: 2026-09-26T14:16:20Z
---

## Result (2026-09-26, PR #7458)

`trLim` is **NOT faithful**, sorry-free, and neither is `wtrace` on `H_3(q)`.
Both statements are new; the mathematics behind them was already settled.

```lean
OcneanuTraceNotFaithful.exists_nonzero_wtrace_orthogonal :
  ∃ x : Hecke ℝ q q⁻¹ 2, x ≠ 0 ∧ ∀ b, wtrace q hq0 hq2 2 (x * b) = 0
HeckeColimitNotFaithful.exists_nonzero_trLim_orthogonal :
  ∃ a : HeckeLim ℝ q q⁻¹, a ≠ 0 ∧ ∀ c, trLim q hq0 hq2 hq21 hgen (a * c) = 0
HeckeColimitNotFaithful.not_isFaithful_trLim
```

Plus the notion itself, which the corpus did not have at this carrier:
`MathlibExt/MarkovTraceRadical.lean` — `rad`, `IsFaithful`, two-sided ideal,
`one_notMem_rad` (proper, from `tr 1 = 1`), `tr_mul_gen_sub_z_of_mem` ((T3) read
as ORTHOGONALITY: `g n − z•1` ⊥ `H n`), and the lifting chain
`tr_mul_sandwich_of_orthogonal` → `tr_mul_eq_zero_of_mem_sup` →
`tr_mul_eq_zero_of_mem_shiftedUpTo` → `mem_rad_of_exhausted`.

## This was an ASSEMBLY, and that is the finding

A six-path corpus-grep (path 0 unavailable — `paper-assistant` MCP failed to
connect, so grep-strength not graph-strength) found the mathematics **settled and
sorry-free on `main`**: the form is degenerate on `H_n` at convention D
(`QBeta/MarkovGramDegenerate.lean`, `det G = 0` exactly), the radical is exactly
the `ℓ(λ) ≥ 3` blocks with corank `n! − Catalan n`, and `H_n/rad ≅ TL_n` exists
as a Lean object on which the form **is** nondegenerate
(`QBeta/MarkovTraceQuotient.quot_pairing_nondegenerate`). `qou-vndn` is
**scrapped** with the scope-(b) exclusion; `qou-phlk` is **completed** as the
adjudication of the `H_∞` over-claim.

**What was missing was the statement about the carriers the tower results use.**
Four Lean docstrings say so in terms (`HeckeColimitFaithful:40`,
`HeckeColimitMarkovTrace:69`, `HeckeTowerStrict:59`, `HeckeInclInjective:53`).

I had started building the negative from scratch — an explicit 3-strand
antisymmetriser `κ = q³ − q²(g₀+g₁) + q(g₀g₁+g₁g₀) − g₀g₁g₀` with `κ·g_i =
−q⁻¹·κ` and `tr κ = 0` at `z = q³/(q²+1)`, all verified by hand. **Dropped.** It
would have been a longer route to a weaker result, since `wtrace` is *defined* as
the Frobenius sum (`wtrace_apply` is `rfl`) and
`ocneanuWeight_conventionD_eq_zero_of_three_rows` is unconditional, so the
negative is three lines given the corpus.

## Two traps worth carrying forward

1. **"Faithful" is a three-way homonym here** — trace-form nondegeneracy (this),
   injectivity of a tower inclusion (`heckeIncl`/`ofLim`, proved yesterday, the
   OPPOSITE answer), and faithfulness of the braid representation (Jones 1985, a
   conjecture in the held library). A grep for it mixes all three.
2. **`towerSpan_heckeColimit` is a `theorem`, not an `instance`** — it must be
   supplied by `haveI` before any `[TowerSpan T]` consumer will elaborate.

## Scope

Convention **D** throughout, `ℝ`, and the four genericity hypotheses `wtrace`
already carries — none added. Under the excised convention C the three-row weight
is nonzero, `G` is invertible, and the verdict inverts. `det G = 0` is exact, not
ill-conditioning.

## Verification

`lean -DautoImplicit=false -s 65536` exit 0 on all three files; `#print axioms`
on all fifteen declarations `[propext, Classical.choice, Quot.sound]`; six
mutants, all required to fail and all do. Content sweep NOT run (needs ~2.3 GB
shadow, ~1.2 GB free disk) — these are library modules with no `.qa.json`, so
`lean`-direct plus the axiom audit is the whole gate available here.
