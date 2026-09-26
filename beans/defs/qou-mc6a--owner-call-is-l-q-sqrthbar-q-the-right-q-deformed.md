---
# qou-mc6a
title: 'OWNER CALL: is L_q = sqrt(hbar_q) the right q-deformed filament length? It fixes the whole E_0 tower factor'
status: todo
type: task
priority: high
created_at: 2026-09-12T20:27:08Z
updated_at: 2026-09-12T20:28:08Z
---

**Owner decision, not agent work.** Successor to `qou-y3bm`, whose own task
(derive-or-record the `E₀` tower series) is done — this is the modelling question
that derivation *uncovered*.

**The decision, in one line.** `qbeta_e0.tower_summed` multiplies the Q_β energy
scale by `1/(1 − ℏ_q²)`. That value is **not** a free choice of factor — it is
equivalent to fixing the **q-deformed filament length** to `L_q = √ℏ_q`, and `L_q`
is a free geometric scale in the corpus. Is `√ℏ_q` right?

**Why `L_q` is what is being chosen** (Lean: `towerSum_iterated`,
`towerSum_iterated_eq_simple_iff`, `leadingMode_lam_eq_one_iff`, all sorry-free).
`prop:brane-tower-q-laplacian-decay` Step 3 is an **equality**:
`|⟨e_k, Δ^{(n)} e_k⟩| = (λ_k^{(q)})^n` with `λ_k = [k]_q²·ℏ_q/L_q²`. So `Δ^{(n)}` is
the **n-th iterate** of the q-Laplacian, the tower sums to `1/(1 − ℏ_q²λ_k)`, and
that equals `1/(1 − ℏ_q²)` **iff `λ_k = 1`** — at the leading mode, iff
`L_q = √ℏ_q = 0.314772482985`.

**What the choice is worth** (probe `qbeta_e0_tower_lq_dependence_probe.py`, 6/6):

| `L_q` | `λ₁` | tower factor | `E₀` (MeV) | vs implemented |
|---|---|---|---|---|
| **`√ℏ_q` — implemented** | **1.0** | **1.00991452** | **4.22748336** | — |
| `1` (Kelvin `L_q = L`, `L = 1`) | 0.09908172 | 1.00097365 | 4.19005705 | **−0.8853 %** |
| `ℏ_q` | 10.0926795 | 1.10997858 | 4.64634966 | **+9.908 %** |
| `h = q − 1/q` | 2.26699408 | 1.02276209 | 4.28126303 | **+1.272 %** |

**The choice is not a detail — it IS the effect.** Widest sampled departure
**9.908 %** against a *total* tower correction of **0.9915 %**. Convergence is not
the constraint: the divergence threshold is `L_q ≤ √(ℏ_q³) = 0.0311882`, far below
any plausible value.

**What the corpus says `L_q` is.** `fluid-dynamics/discrete-vortex-spectrum` — "the
**q-deformed filament length**". `kelvin-dispersion-derivation-steps` takes
`L_q = L·[1]_q/1 = L`, i.e. **the period**, because `[1]_q = 1`. So there is a
precedent, and it is **not** `√ℏ_q`.

**Options.**

- **(A) Keep `√ℏ_q`, and state it as the assumption it is.** *Means:* `λ₁ = 1` is
  adopted as the normalisation of the leading Reeb mode. *Costs:* nothing to
  compute; a scope line wherever `E₀` is quoted. *Risks:* a free scale stays fixed
  at a value chosen without derivation. *Commits to:* defending `λ₁ = 1` as
  natural.
- **(B) Adopt the Kelvin precedent `L_q = L` and derive `L`.** *Means:* the filament
  length is the physical period of the vortex, to be derived. *Costs:* real work —
  identify `L` for the decay channel; `E₀` moves −0.885 % at `L = 1`. *Risks:* `L`
  may itself be undetermined, moving the problem rather than solving it. *Commits
  to:* the fluid-dynamics reading of the tower.
- **(C) Derive `λ_k` from the Reeb-bundle normalisation instead**, bypassing `L_q`.
  *Means:* fix the eigenvalue directly from the geometry. *Costs:* largest; needs
  the Reeb normalisation the corpus has not written down. *Commits to:* a genuinely
  parameter-free tower.
- **(D) Do nothing.** *Default:* `E₀` keeps its current value, now **correctly
  labelled** as assuming `L_q = √ℏ_q` (the module and audit §6c both say so). Safe:
  the label is honest even if the value is unjustified.

**🛑 The move that is forbidden, and it is the obvious one.** Do **not** justify
`√ℏ_q` on the grounds that it reproduces the current `E₀`. That is
selection-against-the-target — the same defect as ranking the admissible Q_β cells
by residual, one level up. If `L_q` is derived and gives a different factor, the
number moves and that is the correct outcome.

**Blast radius.** `qbeta_e0.canonical()` feeds the L2 dashboard's `Q_β`, and through
`Q_beta_best` the `m_n` and `Δ_pn` rows. A 0.9 % `E₀` move is invisible against
those rows' current ~1.7e+8 ppb misses, so **nothing reader-facing changes on any
option** — which is what makes this cheap to decide either way.

**My judgement, not a finding: (A) now, (C) as the real answer.** The label is
already honest, nothing downstream is sensitive at this magnitude, and (B) risks
relabelling the freedom rather than removing it. (C) is what a parameter-free
framework eventually needs.

Audit doc §6c:
[`2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md`](../docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md).
