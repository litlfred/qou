---
# qou-y3bm
title: 'OPEN DERIVATION: the E_0 tower sum 1/(1-hbar_q^2) is canonical by ruling but never derived'
status: todo
type: task
priority: normal
created_at: 2026-09-12T19:04:21Z
updated_at: 2026-11-20T14:39:28Z
---

**What is wrong.** `E₀`, the Q_β energy scale, had **two live forms** in
`computations/qbeta/`, differing by `1/(1 − ℏ_q²) = 1.00991452` (**+0.9915 %**),
with no signal at either call site:

| form | value | where |
|---|---|---|
| order-zero `m_e/(q(q−1))` | 4.18598136 MeV | most call sites, incl. the dashboard |
| tower-summed `… /(1 − ℏ_q²)` | 4.22748336 MeV | `qbeta_bar_branch_refuted_probe.py:88`, annotated *"tower-summed, as ruled"* |

**Unified 2026-09-12 on owner instruction** in
[`computations/qbeta/qbeta_e0.py`](../computations/qbeta/qbeta_e0.py):
`canonical()` = `tower_summed()`, per the 2026-09-03 full-tower ruling
(*"should make use of the full tower even though what is observable is only
order zero"*). `order_zero()` is kept, named for what it is, so historical
figures stay reproducible. The dashboard routes through it.

**🛑 WHAT REMAINS OPEN — and it is the whole bean.** That the tower sum **is**
the geometric series `Σ_{k≥0} ℏ_q^{2k} = 1/(1 − ℏ_q²)` is taken from that one
precedent's annotation. **I did not find a derivation in the corpus and did not
construct one** — inventing a series to justify a factor already in use is
exactly the laundering AGENTS.md forbids. So `tower_summed` is canonical **by
ruling** and open **by proof**.

**What would close it:** derive the tower sum from the Hecke-tower structure —
which orders in `q` contribute, why the ratio is `ℏ_q²` rather than `ℏ_q` or
`h²`, and whether it terminates (the Habiro-ring element terminates at `M = 8`,
which is *not* a geometric series, so the two pictures need reconciling). Until
then, **say "assumed" wherever `E₀`'s tower factor is quoted.**

**Scale, so this is not mistaken for the Q_β problem.** `E₀` moves the row
**0.9915 %**. The convention-D functional moves it **257×** base-to-base. Two
different orders of magnitude; fixing `E₀` does not address the gap.

**Remaining call sites to route through the module** (not done — each needs
checking that it is not deliberately order-zero):
`qbeta_admissible_functionals_bracket_probe.py:164`,
`qbeta_counit_substrate_consistency.py:86`,
`qbeta_habiro_f_from_shape_collapse.py`, `qbeta_markov_trace_steps_4_5.py`.

**A guard fired during this unification and the lesson is worth keeping.**
Routing the dashboard onto the tower `E₀` **silently reverted the whole Q_β row**
to the retired `z = 1` cell: the re-score calibrates against a witness cell
computed at *order-zero* `E₀`, so the +0.99 % shift broke the comparison and the
producer correctly refused to publish. The guard worked; the calibration was
asking the wrong question (it conflated "is my trace right?" with "which `E₀` is
canonical?"). Fixed by calibrating the trace at the `E₀` the cell used, then
publishing at the canonical `E₀` — **one check per claim**. The failure mode was
a *silent revert*, not an error.

Full analysis: `docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md` §5(c), §6.


## 2026-09-12 — DERIVED, modulo one hypothesis now isolated in Lean. Closing.

**The series is not assumed.** Corpus-grep found two propositions nobody had
connected:

- **`prop:brane-tower-q-laplacian-decay`** writes the tower as
  `Σ_n ℏ_q^{2n}·Δ^{(n)}(ρ)`. The `ℏ_q^{2n}` is the tower's own **grading** — the
  bound in that proof is a *separate* factor `Cⁿq^{2nk}` on `Δ^{(n)}`.
- **`prop:delta-max-uniform-bound`** gives `|Δ^{(n)}| ≤ Δ_max`
  **independent of the jet level `n`**.

Together they give `1/(1−ℏ_q²)`. Formalised in
[`QOU/QBeta/TowerGeometricSum.lean`](../content/quantum-observable-universe/lean/QOU/QBeta/TowerGeometricSum.lean),
four sorry-free theorems, `lean`-direct exit 0, axioms
`[propext, Classical.choice, Quot.sound]`:

| theorem | content |
|---|---|
| `hbarQ_sq_lt_one` | ratio in `[0,1)` for `q>1` ⇒ converges (`ℏ_q² ≈ 0.0098` at the pin) |
| `towerSum_of_const` | `Δ^{(n)}` level-independent ⇒ tower is **exactly** `Δ/(1−ℏ_q²)` |
| `towerSum_le_of_uniform_bound` | uniform bound only ⇒ bounds the **magnitude**, termwise |
| `uniform_bound_not_const` | the gap as a statement, not a comment |

**The remaining hypothesis, stated precisely:** `delta_max_uniform_bound` proves
a bound uniform in `n`, **not** that `Δ^{(n)}` is *constant* in `n`. So
`E₀/(1−ℏ_q²)` is the tower **at saturation** and a magnitude bound otherwise.
That is a far smaller and sharper gap than "assumed", which is what this bean
asked for, so it closes here. **A successor bean should prove `Δ^{(n)}`
level-independence or compute its `n`-dependence** — that is new work, not this
bean's.

**Two traps recorded in the Lean file:**
1. The decay proof's ratio is `ℏ_q²·C·q²` with `C = ℏ_q/((q−q⁻¹)²L_q²)`, and
   **`L_q` is the q-deformed filament length — a free geometric scale.** It sits
   in the *bound* on `Δ^{(n)}`, not the grading, so it does not contaminate
   `towerSum_of_const`. Deriving the ratio *as* `ℏ_q²Cq²` **would** smuggle in a
   choice of `L_q` — a hidden parameter. Do not do that.
2. `computations/_deprecated/jet_level_geometric_series.py` attributes the
   `ℏ_q^{2n}` damping to `delta-max-uniform-bound`, which explicitly says its
   bound is *independent of n*. That misattribution is why the series looked
   undeserved. Its real home is the brane-tower decay.

PR #7235, commit `a56364abc24`.


## 2026-09-12 (later) — 🛑 the isolated hypothesis is FALSE. The factor pins `L_q = √ℏ_q`, a free scale.

Reopened in substance, though the bean's own task (derive-or-record) is done.
Lean: `towerSum_iterated`, `towerSum_iterated_eq_simple_iff`,
`leadingMode_lam_eq_one_iff` — sorry-free, `lean`-direct exit 0. Probe:
`qbeta_e0_tower_lq_dependence_probe.py` (6/6).

**`Δ^{(n)}` is NOT level-independent, and the corpus said so.**
`brane-tower-q-laplacian-decay-proof.md` Step 3 is an **equality**:
`|⟨e_k, Δ^{(n)} e_k⟩| = (λ_k^{(q)})^n` with `λ_k = [k]_q²ℏ_q/L_q²`. So `Δ^{(n)}` is
the **n-th iterate of the q-Laplacian**. `towerSum_of_const` is a true theorem
whose hypothesis this object does not satisfy — which is what isolating it was for.

**The true sum is `1/(1 − ℏ_q²λ_k)`**, equal to the implemented `1/(1 − ℏ_q²)`
**iff `λ_k = 1`**, which at the leading mode (`[1]_q = 1`) pins
**`L_q = √ℏ_q = 0.314772482985`**.

| `L_q` | `λ₁` | tower factor | `E₀` (MeV) | vs implemented |
|---|---|---|---|---|
| **`√ℏ_q` — implemented** | **1.0** | **1.00991452** | **4.22748336** | — |
| `1` (Kelvin `L_q = L`) | 0.09908172 | 1.00097365 | 4.19005705 | **−0.8853 %** |
| `ℏ_q` | 10.0926795 | 1.10997858 | 4.64634966 | **+9.908 %** |
| `h = q − 1/q` | 2.26699408 | 1.02276209 | 4.28126303 | **+1.272 %** |

**The choice of `L_q` is not a detail — it IS the effect**: widest departure
**9.908 %** against a total tower correction of **0.9915 %**. Convergence is fine
(threshold `L_q ≤ √(ℏ_q³) = 0.0311882`); the **value** is the question.

**🛑 So `qbeta_e0.tower_summed` carries a hidden parameter — now named.** And the
tempting move is forbidden: adopting `L_q = √ℏ_q` *because it reproduces the
current `E₀`* is selection-against-the-target, one level up from the cell-ranking
case. `qbeta_e0` is untouched.

**SUCCESSOR: an owner modelling call** — is `√ℏ_q` the right q-deformed filament
length? `L_q` is free in the corpus (`discrete-vortex-spectrum` calls it "the
q-deformed filament length"; the Kelvin derivation takes `L_q = L`, the period).
Audit doc §6c.


## 2026-11-20T14:39:28Z W13 — owner asked "if derived+proved, update compute; if not, work on it"

REOPENED (rule 13a: the open premise is unclosed). Tower E0 is canonical BY RULING (2026-09-12, 2026-11-20) but the series is conditional: towerSum_of_const assumes a level-independent residual; the decay proof gives lambda^n, equal only at lambda_1 = 1 (L_q = sqrt(hbar_q)), argued in TowerGeometricSum.lean prose only; the uniform bound is a structure field (DeltaMaxUniformBound.lean:93 projects b.per_level_bound). Still on order-zero E0: two_term_qed_isotope_and_nucleon_compute.py:166 (b_pp/pn/nn, b_sym, c_em at 415-506), qbeta/qbeta_counit_substrate_consistency.py:110. Open: prove lambda_1 = 1 or derive L_q.
