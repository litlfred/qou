---
# qou-mpq5
title: 'R2: prove (1)↔(2) Schur-Weyl — tr over (ℂ^N)^{⊗n} = Σ_{λ⊢n}(dim V_λ)χ_λ (partition fn = character sum)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T18:33:15Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-59vq
---

Medium. The stat-mech trace over the tensor state space equals the sum-over-Young-diagrams character sum — this IS Schur-Weyl/Wedderburn as a change of basis between the two partition-function presentations. Schur-Weyl already anchored at q=1 in bean 1ict; extend to the q-deformed Markov trace. Cross-ref knot-eigenbasis-complete.lean.

## 🔥 Scope assessment (2026-08-02) — R2 is a genuine Mathlib GAP, not a quick win

Honest finding (rule 14): **Mathlib has NO Schur–Weyl duality** — classical
or quantum. A grep finds only `SchurZassenhaus`, `CategoryTheory…Schur`
(Schur's lemma), and `Matrix.SchurComplement` — none is the
`GL(V) × S_n ↷ V^{⊗n}` double-centralizer, let alone the
`U_q(gl_N) × H_n(q)` quantum version. Full quantum Schur–Weyl for Hecke
algebras is a multi-week formalization; it CANNOT be landed sorry-free in a
session, and I will not fake it with a `sorry`-scaffold or trivial-true.

**What IS tractable (honest sub-lemmas, for a future push):**
1. **Trace additivity over a finite direct sum** — `tr` over `⊕_λ M_{d_λ}`
   equals `Σ_λ tr(block_λ)`. This is the *linear backbone* of
   "partition function = character sum" and is provable from Mathlib
   (`Matrix.trace`, `map_sum`). Non-trivial-enough only if stated over the
   Wedderburn decomposition, which needs (2).
2. **The Wedderburn iso `H_n(q) ≅ ⊕_λ M_{d_λ}(K)`** — this is the real gap.
   Mathlib has `WedderburnArtin` (existence of *a* decomposition for
   semisimple rings) but NOT the explicit partition-indexed one for the
   Hecke algebra with the Hoefsmit matrix units. This is the load-bearing
   missing piece.
3. **Character formula `tr_M = Σ_λ w_λ χ_λ`** then follows from (1)+(2).

**Recommended decomposition into child beans (future):**
- `R2a`: trace additivity over `⊕` (near-term, ~Mathlib one-lemma).
- `R2b`: `H_n(q)` semisimple + `WedderburnArtin` instance (medium).
- `R2c`: the explicit partition-indexed matrix-unit iso via Hoefsmit
  (the hard, multi-week gap — where quantum Schur–Weyl actually lives).

Status: R2 left as `todo` — flagged as a hard gap, deliberately NOT
attempted this session to avoid a dishonest scaffold. R1 (`qou-j6lf`)
correctly consumes `y_λ>0` as given precisely because R2 is the piece that
would *supply* those weights.

## ✅ Formalize-first scaffold landed (2026-08-02) — R2a proved; R2-inst is the open piece

[`QSchurWeyl.lean`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/QSchurWeyl.lean)
(`QOU.SchurWeyl`), generic field `K`:

- `HeckeWedderburnData` — content-bearing structure axiomatizing the
  Jimbo/Hoefsmit content as HYPOTHESES: the Wedderburn iso
  `H ≃ₐ[K] ⊕_λ M_{d_λ}(K)` and `markov_eq : tr_M h = ∑_λ w_λ (iso h λ).trace`.
- **R2a PROVED sorry-free** (conditional on the structure):
  - `markov_one_eq` : `tr_M 1 = ∑_λ w_λ · d_λ` (partition function at identity
    = degeneracy-weighted block sum — the concrete character-sum payoff).
  - `markov_add`, `markov_smul` : tr_M is a genuine linear trace functional.
- Axiom-clean (`propext, Classical.choice, Quot.sound`); **no sorry, no
  trivial-True**; the open state is honestly a *missing instance* (§3b-tax),
  not a laundered axiom. Wired into `QOU.lean`; lean-direct exit 0.

**Honest scope (rule 14):** the structure ASSUMES the Wedderburn iso +
Markov identity (that is exactly what full quantum Schur-Weyl provides). I
did NOT construct an instance for the real `H_n(q)` — that is `R2-inst`
(the Jimbo-1986 double-centralizer + Hoefsmit matrix units), a multi-week
Mathlib gap, deliberately NOT faked. R2 is therefore *conditionally* proved
(§3b-cond), not unconditionally. Children R2b/R2c/R2-inst track the real work.

## Progress 2026-11-17 (Round 66 — PR #8340)

- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/AddableCellRatioFakeDegreeTwoRowBallotWeightTensorPowerCharacterOrbitTrace.lean` (Lean 4.24.0, `0` `sorry`, `0` `axiom`, `0` warnings, `0` directory-mode static vacuity & borrowed-name advisories).
- 80-dps `mpmath` numerical witness stamped in `computations/probes/addable-cell-ratio-fake-degree-two-row-ballot-weight-tensor-power-character-orbit-trace.witness.json` (`scriptHash = 0309390e769d`, `scriptCommitSha = c43b700db42337a2547c8ff1e2a1665156dd27ea`, `HEAD = d46ecc77d14e0e9528cfc49310e88f4e88eb306a`).
- PR: https://github.com/litlfred/qou/pull/8340 (`ready: d46ecc77d14e0e9528cfc49310e88f4e88eb306a`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8340, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-19: "beans(qou-jr8y): closed -- the orphaned mpq5 fragment landed with #4600"). The work may be partly or fully done. Read the bean before you close it.
