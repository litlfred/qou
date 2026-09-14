---
# qou-u96j
title: Walk the canonical derivation chain step by step and catalogue where CONDITIONS emerge
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T07:49:59Z
updated_at: 2026-09-14T08:08:32Z
---

## 2026-09-14 — first tranche: steps 5 and 10 walked

PARTIAL walk. Measured steps 5, 6 (partially), 10. Step 2's condition is already
in the cheat sheet's own §2a (curvature 2-form stipulated) and is cited, not
re-derived. **Not walked: 1, 3, 4, 7, 8, 9, 11** — named so the gap is visible.

### C5a — step 5's partition sum runs over TWO-ROW partitions only
The step says `tr_M = Σ_{λ⊢n} y_λ χ^λ` over ALL partitions. Measured against the
committed `y-lambda-at-q0.witness.json`: at **every n from 2 to 12**, every `y_λ`
with ≥3 rows is **exactly 0** and every nonzero one has ≤2 rows (at n=12: 7
nonzero, 70 zero). Production family is `y_lambda_su_n(n, q, 2)` — the trailing
`2` is a row cap. AGENTS.md does say "convention D = the two-row truncation", so
the fact is known; what is missing is that **the chain's own step statement does
not carry it**.

### C5b — `α` is a Wenzl weight, not an ad-hoc ratio
`y_(3)` at n=3 equals `(q⁴+1)/(q²+1)²` **exactly** (45 dps, |diff| 5.0e-47). That
is the same α as the 2026-09-08 Q_β ruling's augmentation-to-z_D factor and as
the flavour-split fork in #7334. Two arcs reached α independently; both were
reaching the trivial block's Wenzl weight.

### C5c — normalisation is dimension-weighted (and I got it wrong first)
`Σ d_λ y_λ = 1` exactly at every n (this is `tr_M(1)=1`, since `χ^λ(1)=d_λ`). The
unweighted `Σ y_λ` is 1 only at n=2 and falls to 0.0133 by n=12. My first reading
was the unweighted one and produced a false "the y are not a measure" claim.
Distinct from the `w_λ(q)` non-normalisation in the notation register — that is
the quantum Plancherel family, a different object.

### C10a — `n_target` has three inequivalent production meanings
Spec declares `n_target ∈ ℤ≥0` (integer). Measured at source:
* `aK_via_lp_dual_hecke_basis.py:175` — `tr_M_atom`, a Markov trace (REAL)
* `pn_alpha_lp_dual.py:375` — `float(pn_vec.sum())` (REAL, α-dependent)
* `option_b_proton_mass_full_chain.py:588` — `float(n_gg)`, γγ count (INTEGER)

Each cites a different authority. Only the third matches the declared type.
`n_target` is what *selects* `T_w`, so this is step 10's emergent condition.

### C10b — the cheat sheet states an objective the code does not have
§1 and §2 render step 10 as `min ‖tr_M(T_w)·𝔈₀ − B_tgt‖`. The authoritative
algorithm block has **no B_tgt** (`min Σ tᵢxᵢ s.t. net(x)=n_target, Gx≥0`) and
`solve_operator_selection_lp(t, G, n_target)` has no such argument. The defect
points the SAFE way — the doc looks more fitted than the code — but it is in the
primary coordination document and would lead a reader to conclude the chain fits
AME at its selection step.

### Next
Step 3's "unique trace" — where `z` enters, and the likeliest root of the
`qou-99qc` / `qou-qqm4` fork. Not established here, so not asserted.
