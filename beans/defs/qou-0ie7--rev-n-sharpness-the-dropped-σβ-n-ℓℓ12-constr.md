---
# qou-0ie7
title: 'REV_n sharpness: the dropped Σβ = n + ℓ(ℓ−1)/2 constraint after the (ℓ,W) route closed (takeover of #7093, qou-hok7)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T18:06:40Z
updated_at: 2026-10-10T07:04:47Z
parent: qou-3e6w
---

PR #7093 (branch claude/rev-pair-term-even-gap-minimizer-2026-09-07, 3 commits, awaiting merge permission) closed the (ℓ,W) route: Jensen is optimal per distance class, and the inter-class coupling factor SHRINKS with ℓ (1.208 at ℓ=8 → 1.072 at ℓ=60; 1.128 at the maximizer's ℓ=22, 8.2 % of B against a ~3× gap). The only remaining relaxation of size is the dropped constraint Σβ = n + ℓ(ℓ−1)/2, which ties the β's to n directly rather than through two summary integers. Task: formulate the bound WITH that constraint (fresh formulation, not another bound on the same object), measure against the exact REV_n (n ≤ 44 available from rev_free_energy_over_shapes_probe), and say whether the 3/4 exponent is sharp. REV_n is the free energy over partition shapes: energy = excess hook length, entropy = shape multiplicity. Exact / mpmath, no float64.



**ROAST 2026-09-07 (qou-pbwj) — verdict: CONTINUE, conditional on a budget measurement first.** Strongest objection: 'the dropped Σβ = n + ℓ(ℓ−1)/2 constraint is the only remaining relaxation of size' is asserted, not measured. The over-statement at the n = 40 argmax is 3.09× (#7081); PR #7093 prices the Jensen inter-class coupling at only 1.21× and shrinking with ℓ; ~2.5× is unattributed, and (III) is a restriction on the feasible set, not a term in the bound — it cannot reduce the per-configuration slack of the one-body term Σ_i F(β_i) ≤ ℓC, where F(k) saturates at C = 6.1714 only as k → ∞ and the maximiser's β's are O(√n) with W/ℓ ≈ 1.7. Before formulating: at n ∈ {16,24,32,40} and the maximiser's own (ℓ,W), split the 3× into (one-body slack) × (Jensen) × (what (III) removes). Formulate only if (III) owns the majority. Fit exposure: none in the forbidden sense (a bound is valid or not), but the live hazard is reading n ≤ 44 numerics as sharpness — rev_sharpness_discriminator_control_probe shows a provably √n object is flat at 1.20–1.23 on the n^{3/4} column over exactly the reachable range; no 'tracks √n / n^{3/4}' claim below n ~ 150. Arity: the proved bounds are ∀n with constants; sharpness is ∃c ∀N ∃n > N — undecidable from any finite table; and REV_n is a one-parameter family in q evaluated at one archimedean point (say so). L2 relevance: none — qou-hok7 itself records the resummation route to B_D as negative since 2026-08-21; REV's asymptotics is a statement about the object. Full frame: docs/audits/2026-09-07-takeover-fronts-roast.md §Front 4.

## 2026-09-11 — first attempt LOST to a rate limit; the recovered progress block claims O(√n)

The dispatched agent died at step 3 (API 429, 2026-09-07 ~18:45 UTC) with its worktree uncommitted; the worktree was reclaimed. What survives is its last progress block, verbatim in the parent session:

(a) β_i = λ_i + ℓ − i (first-column hook lengths, strictly decreasing, β_ℓ = λ_ℓ ≥ 1); (I') R_λ = Σ_i F(β_i) − Σ_{i<j} ε(β_i−β_j) − F(n); (II) H = Σ β_i(β_i+1)/2 − Σ_{i<j}(β_i−β_j); (III) n = Σβ_i − ℓ(ℓ−1)/2. #7070's bound B(ℓ,W) = ℓC − J(ℓ,W) − F(n) replaces every one-body F(β_i) by its saturation C — that step discards the β values, and (III) is exactly what fixes them; #7081's Hhat (Cauchy–Schwarz) is the second place.
(b) Constrained bound via exact-sum knapsack transfer matrix over (rank k, partial sum s) per (ℓ, β₁=t): B_Σ = 16.11/26.14/34.25/40.04/42.24 at n=16,24,32,40,44 vs true M_n = 8.08/12.41/16.28/19.75/21.15 vs #7081's 35.07/46.30/54.96/61.13. B_Σ/REV_n = 1.50 at n=40.
(c) Rate scan to n=200: B_Σ/√n = 6.42 → 6.08 (falling); B_Σ/n^{3/4} = 2.31 → 1.62.
(d) CLAIMED short proof that the exponent is 1/2: row form H(λ) = Σ_i λ_i(λ_i+2i−1)/2 (from existing Lean lemmas sum_hookZ_eq, sum_fst_eq_bStat, two_mul_sum_snd); expanding around the min-hook shape λ⁺ (staircase δ_k with first r rows extended, n = T_k + r) gives H(λ) − H(λ⁺) ≥ (ℓ−k)₊²/2 − r/2 for every λ ⊢ n with ℓ rows; with R_λ ≤ Cℓ this yields M_n ≤ (C + ln q₀/2)√(2n) + C²/(2 ln q₀), so REV_n ≤ 8.80√n + 182.6 + log p(n) = O(√n). Numerically: U*(n)/√n = 29.7 (n=44) → 8.92 (n=10⁶), converging to C√2 = 8.727; the H lower bound held on all partitions n ≤ 22 (exact).

NOTHING of this is committed or verified. It is a claim by a dead agent. If (d) holds, REV_n = Θ(√n) (the Ω(√n) lower bound is prior) and the 3/4 exponent is NOT sharp — that settles qou-hok7's sharpness question. Re-dispatched 2026-09-11 on branch claude/rev-sqrt-n-upper-bound-2026-09-11 with this block as the starting point; the first task is to re-derive (d) and prove the H lower bound in Lean, not to trust it.



## 2026-09-11 — second attempt: (d) HOLDS. REV_n = Θ(√n); the 3/4 is not sharp (PR #7185)

Branch `claude/rev-sqrt-n-upper-bound-2026-09-11`, commits `f50c51b04bc` (probe + Lean),
`d0a7d8d9b77` (witness). Nothing here was taken from the dead agent's block on trust; each
item was re-derived from the definitions the corpus computes with.

**The claimed inequality is a tangent-line bound, and it is exact where it matters.** With
`m_i = λ_i − 1` the row form `2H = Σ_{i<ℓ} λ_i(λ_i + 2i + 1)` (rows 0-indexed; from
`sum_hookZ_eq` + `two_mul_sum_snd` + `sum_fst_eq_bStat`) is a sum of convex row terms.
Tangent lines of slope `2j+1` at `λ_i = (j−i)₊` give, for EVERY `j ≥ 0`,

    2H ≥ ℓ(ℓ+1) + (n−ℓ)(2j+1) − Σ_{i<ℓ} ((j−1−i)₊)²,

with equality on `δ_j + 1^{ℓ−j}`. At `j = k`, `n = T_k + r`, and `6P_k = k(k+1)(2k+1)` this is
the polynomial identity `2(H − H⁺) ≥ (ℓ−k)² − r`, `H⁺ = P_k + r(k+1) = H(λ⁺)` — the recovered
block's `(ℓ−k)₊²/2 − r/2`, and it needs NO `ℓ ≥ k` hypothesis (for `ℓ < k` the correction is a
sub-sum of `P_{k−1}`; the sharper form there is `−r + (k−ℓ)(2k+1−2ℓ)(k+1−ℓ)/6`).

**The rest of the chain.** `R_λ = Σ_c ε_{h(c)} − F(n)` exactly (every `ln q₀`, `ln(t−1)` cancels;
this is #7070's (I') before the β change of variables); `N_m ≤ ℓ` (hooks strictly decrease along
a row, #7018) gives `R_λ ≤ (ℓ−1)C`. Hence

    M_n ≤ (C + L/2)√(2n) + C²/(2L) − C = 8.80√n + 176.3,
    REV_n ≤ M_n + log p(n) ≤ (C + L/2 + π/√3)√(2n) + C²/(2L) − C = 11.37√n + 176.3,

(`L = ln q₀`, `C = 6.1714`, `log p(n) < π√(2n/3)` elementary, Apostol Thm 14.5). With the prior
Ω(√n) (#7014): **REV_n = Θ(√n).** The quadratic's maximiser is `x = ℓ − k = C/L = 59` rows above
the staircase — the argmax drift #7081 measured (`ℓ = 151` at `n = 4000`, `√(2n) = 89`) and
could not explain.

**Where the flaw was looked for.** (i) `(ℓ−1)C` vs `C·min(ℓ,λ₁)`: weakens only R, and is what
lets the energy be indexed by ℓ. (ii) The block's `r` is `n − T_k`, not #7070's `min(ℓ,λ₁)` —
overloaded letter, never the same object in one line. (iii) #7081's relaxation RISING above
`n^{3/4}` to n = 4000: its Cauchy–Schwarz `Ĥ` is **48.9 % of `H_min(4000)`** at its own argmax
`(151, 357)` — the column half spreads `n − ℓ` cells evenly over `λ₁ − 1` columns, which no
151-row partition can — so the maximiser fed on a negative energy no shape has. Its 99–100 %
calibration was at n ≤ 40 where `ℓ − k` is small. Not evidence against Θ(√n).

**Verified.** `rev_sqrt_n_upper_bound_probe.py` 7/7 (38.6 s): identity (1) to 1e-59 on all
shapes n ≤ 16; `N_m ≤ ℓ`, `R ≤ (ℓ−1)C`, the tangent bound for all `0 ≤ j ≤ n+1`, (5) and (5′),
`H⁺ = H_min(n)` = brute force = committed closed form, `H(λ⁺) = H⁺` — all exact integers on
every partition n ≤ 30; every link `M_n ≤ U_exact ≤ U_tan ≤ U* ≤ (6′)`, `REV_n ≤ M_n + log p(n)
≤ (7)` at n = 2..44 (60 dps). n = 44: M = 21.146, REV = 28.604, U_exact = 190.87, U* = 226.13,
(6′) = 234.72, (7) = 251.73. The bound is loose by the additive `C²/(2L) = 182.5`; its growth is
√n, which is the claim. Rate scan from the closed form: `U*/√n` → 8.80 within `188.7/√n`;
`U*/n^{3/4}` → 0.

**(b), (c) of the recovered block.** The Σβ-constrained one-body bound is ~8× M_n with the pair
term dropped (the recovered 16.11/…/42.24 kept Jensen); Σβ alone closes nothing — it is the
energy-vs-rows step (5) that does. (c) reproduced as above.

**Lean.** `QOU/BraidKnot/HookSumRowTangentBound.lean` on `YoungDiagram` over ℤ:
`two_mul_sum_hookZ_rowform`, `two_mul_sum_hookZ_ge_tangent` (every j), `sum_trunc_sq_eq_of_le`,
`sum_trunc_sq_le`, **`two_mul_sum_hookZ_sub_hminClosed_ge`**, `..._of_le`, `quad_max_le` (ℝ).
`lean -DautoImplicit=false -s 65536` exit 0, no warnings, restored cache; `#print axioms`:
`propext, Classical.choice, Quot.sound` on all six. Zero sorry.

**Not proved in Lean (honest gap, not blocking).** That `hminClosed k r` is the GLOBAL minimum
hook sum; the theorem is against the defined quantity. The argument needs only `H⁺ ≥ H_min(n)`
(attainment by `λ⁺`), verified exactly n ≤ 30 and by the committed closed form to n = 26. A
Lean construction of `λ⁺` as a `YoungDiagram.ofRowLens` and `H(λ⁺) = hminClosed` is the next
formalisation step if anyone wants the constant in Lean too.

**Gates.** `precision-gates.sh --changed` RED on tree-wide ratchets only (tree 16 behind main;
`Q0_FLIP: 1` = `hadron-knot-table`, `Q0_ANCHOR_UNRECOGNISED: 1` = `qbeta-derived-w-overdetermined-test`,
verified by running the anchor audit alone); the ten contended audit witnesses it regenerated
were reverted (bean `qou-v0t8`).


## Reorganisation 2026-10-10 — now A4 of the REV_n asymptotics arc

Re-parented from the PROGRAM root `qou-10v9` (where it hung as one of ~70 direct task children)
to the arc's new epic `qou-3e6w`. Read `qou-hok7` for the arc's ledger and `qou-fxym` (A3) for
the headline bound this task's answer discriminates: A3 asks whether `REV_n = O(√n)` can be
*proved*; this bean asks whether the 3/4 exponent is *sharp*, which the data at `n ≤ 44` cannot
decide. The two are siblings, not sequential.

## Progress Update (Round 64 — PR #8263)
- **Status**: `in-progress` (per active rule: no unilateral `qou` bean closures).
- **PR**: [`litlfred/qou#8263`](https://github.com/litlfred/qou/pull/8263) (branch `feat/round64-hooksum-formality-charge-ocneanu-coupling-43c1`, Commit 1 `30d0d4f4e437e19904cd4438468a9ecf56eadd3a`, Commit 2 / Head `545135545dc8e721846ea1fb0e54556f69a5a166`).
- **Lean 4 Artifact**: `folio/quantum-observable-universe/lean/QOU/BraidKnot/HookSumRowTangentBound.lean (`six_mul_hminClosed`, `hminClosed_step_continuity`)` (0 sorry, 0 findings across all 6 static vacuity audits).
- **80-dps Witness**: `computations/probes/hooksum_formality_charge_ocneanu_coupling_probe.py` (`scriptHash: dae747aae6b4`) + `test/results/witnesses/hooksum-formality-charge-ocneanu-coupling.witness.json` (`allPassed: true`).
