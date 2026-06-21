---
# qkhc
title: 'Q_β kernel hunt — Stage C (fibre-level Habiro/recurrence kernel for c_k)'
status: in_progress
type: task
priority: normal
created_at: 2026-06-16T02:14:00Z
updated_at: 2026-06-16T02:40:00Z
parent: qz9k
---

## Result (2026-06-16) — Stage C scoped + formalize-first pruning; pending human close

Scope doc delivered:
[`docs/scope/2026-06-16-qbeta-kernel-hunt-stage-c-scope.md`](../docs/scope/2026-06-16-qbeta-kernel-hunt-stage-c-scope.md).

- **Stage C defined:** with C1–C12 refuted, target the **fibre-level q-difference
  kernel R(q,ξ)** in `F(qξ)=R(q,ξ)·F(ξ)` directly (the one open decay-side axis);
  formalization target is R(q,ξ), not another c_k value.
- **Formalize-first pruning (value-add):** the corpus-map agent's "use the q-Lommel
  ORDER recurrence (binding Δ_λ ladder, constant b=q₀¹⁰+q₀⁻¹⁰) as the c_k template"
  is a **double category error** — (i) wrong recurrence: c_k are k-indexed →
  *argument*/contiguity recurrence (`QBesselContiguityRecurrence.lean`), not the
  *order* recurrence (`QLommelOrderRecurrence.lean`, which the docstring binds to the
  binding ladder); (ii) wrong class: c_k are **q-holonomic** (first-order (★), q^k-dep
  coeffs), NOT C-finite — the constant-b recurrence is the degeneration PR #1839
  already falsified. Confirming numeric: constant-b predicts c_4≈−5.38 vs empirical
  c_4≈−0.97.
- **No probe run** — fibre-Habiro axis is owner-gated multi-session research;
  coordinate before any probe branch. Hoefsmit Stage-B localization noted as a
  separate, now-unblocked narrowing input.
- Disambiguated the two overloaded "Stage X" lineages (Hoefsmit per-block infra vs
  kernel hunt).

## Goal

Continue the Q_β kernel hunt into **Stage C**. Target: a **fibre-level**
Habiro element / recurrence kernel $F(q)\in$ Habiro ring whose archimedean
evaluation at the substrate $q_0$ reproduces the precision-ladder coefficients
$c_k$ in $Q_\beta = Q_{\text{base}}\cdot\prod_k (1 + c_k u^k)$,
$u = b\,\hbar_q^2 \approx 0.00852$.

## Corpus state (session start)

Master ledger: [`docs/coordination/1ppq-qbeta.md`](../docs/coordination/1ppq-qbeta.md).
Stage B is defined in
[`docs/scope/2026-06-04-hoefsmit-stage-b-per-block-tbeta-scope.md`](../docs/scope/2026-06-04-hoefsmit-stage-b-per-block-tbeta-scope.md).
Relevant audits:
- `docs/audits/2026-05-30-qbeta-recursive-pair-rules-and-habiro-pde.md`
- `docs/audits/2026-06-04-qbeta-1ppq-keystone-exact-construction-recipe.md`

(Background Explore agent reconstructing Stage A/B exactly + the refuted-mechanism
list + canonical scripts; results to be folded in before Stage C is fixed.)

## Discipline (read before any wire/un-wire)

- `c_2 = -1` PROVED Taylor-exact; `c_3` is a q_0-dependent **NEAR-MATCH**
  (NOT Taylor-exact) — settled 5×, flip-flop history in the ledger. `c_4..c_7`
  are §3b-cond classes (PR #1587). Report TIERED, never binary.
- **Fibre vs observable**: the c_k live in the fibre (formal q, possibly
  complex). Do NOT hunt a real closed form `c_3 = f(q_0_real)` — already known
  to fail. Hunt a fibre element whose evaluation at each anchor gives that
  anchor's c_3 (parallels α_EM `[2]_q·(1-h²α)`, PR #1511).
- Do NOT repeat already-refuted mechanisms (#1..#7+; e.g. Li_2^q × spectral
  combiner = mech #7, refuted PR #1609).

## Plan (formalize-first)

1. Pin Stage A and Stage B definitions precisely (from the scope doc) so
   Stage C is the genuine next increment, not a re-run.
2. Tabulate the refuted kernel mechanisms; pick the most promising UNTRIED
   structural angle (q-Lommel 3-term recurrence is the current candidate per
   beans v3po/vwpi — verify).
3. Formalize the invariant the kernel must satisfy (parity / bar-symmetry /
   recurrence order) to prune the class before any wide PSLQ-style scan.
4. Run only the survivors; report tiered.

## Acceptance

A scoped Stage-C definition + at least one formalize-first pruning result
(kills or constrains a kernel sub-class), recorded in the ledger with tiered
status. NO production wire/un-wire flip without ledger + tiered justification.

> **LEAN CONTRIBUTION 2026-06-20 (PR #2555).** Formalized invariant (b) bar-evenness as a
> sorry-free lemma: the (★) coefficient ratio ρ_k = c_{k+1}/c_k satisfies, under the bar
> involution q↦q⁻¹/a↦a⁻¹, a k-INDEPENDENT twist ρ_k(q⁻¹,a⁻¹) = (a q)·ρ_k(q,a) (a q =
> q^{ν+2}). So bar-evenness of the whole ladder collapses to ONE global normalization, a
> necessary-condition gate. `QOU/QBeta/QBesselBarCovariance.lean` (heckeCoeffRatio +
> heckeCoeffRatio_bar_covariance, [Field K], axioms [propext,Classical.choice,Quot.sound];
> wired into QOU.lean). Complements the sibling NUMERICAL bar-parity gate (qbeta-D, Type-B
> refuted) with the proved STRUCTURAL covariance. Machinery / necessary-condition lemma —
> NOT the kernel construction (owner-gated multi-session) and NOT a c_k value. No fit.
