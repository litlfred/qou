# Status-label overclaim triage — the 95 sharp candidates

**Source:** [`computations/status_label_overclaim_audit.py`](../../computations/status_label_overclaim_audit.py) (devil's-advocate class-2 checker)
**Date:** 2026-06-24 · **Machine buckets:** [`2026-06-24-status-label-overclaim-buckets.json`](2026-06-24-status-label-overclaim-buckets.json)

The checker flags blocks wearing a **closure label** (`proved` / `closed-form` / `no-fit` / `RESOLVED` / `sorry-free`) over a **non-closure signal** in the same triple. 227 candidates total; the **95 "sharp"** carry the label over a vacuous/incomplete Lean (`: True`, `:= trivial`, or `sorry`). This triage buckets the 95 by disposition. **No claims were rewritten** — relabel vs finish-the-Lean is author judgement (math-adjacent), so the actionable buckets are queued as needs-author, not auto-applied.

## Buckets

### Bucket B — provable-kind vacuous (14) · **§1a review failures · highest priority**

A `theorem`/`proposition`/`lemma` whose Lean concludes `: True := trivial` (or `:= trivial`) while prose/docstring claims it is proved/theorem-level/closed-form. Per AGENTS.md §1a these are review failures: the honest dispositions are **(1) prove it**, **(2) restate the real proposition with `sorry` + `-- Ref:`**, or **(3) demote to `conjecture`**.

Confirmed exemplars (Lean verbatim):
- `b1-figure-8-row-theorem` — `theorem b1_figure_8_row : True := by trivial`, docstring "**PROPOSITION.** B1 keystone is theorem-level …".
- `depth-2-identification-bloch-suslin` — `theorem depth_2_identification : True := by trivial`.
- `b1-hyperbolic-rows-theorem`, `collatz-contact-boundary` (`:= trivial`), `q-heat-kernel-peter-weyl`, `markov-trace-axiomatic-closed-form`, `crystal-r-matrix-sub-lemma`, `hecke-1d-irrep-closed-form-character`, + 6 more (see buckets JSON).

These overlap exactly with the `lean-vacuity-axiom-audit` / `lean-proof-vacuity-audit` scope — the class-2 checker reaches them from the *content-label* side (it catches the overclaim even where the vacuity audit is satisfied by a `def`-disguise or a conjecture carve-out).

### Bucket C1 — `sorry-free` claim contradicted by a `sorry` (23) · **high priority**

The block's label literally says **`sorry-free`** while its Lean contains a `sorry`. Either the claim is stale (the `sorry` was added later) or the proof was never finished. Exemplars: `pontryagin-dual-coxeter-character` (theorem), `inter-nucleon-channel-color-tube` (conjecture), `vdw-pskew-isolation`, `casimir-first-q-correction`, `binding-qbeta-complex-volume`. Disposition: **finish the proof** or **drop the `sorry-free` label** (the latter is a safe mechanical relabel — a `sorry-free` claim over a `sorry` is unambiguously false).

### Bucket C2 — closure label + `sorry`, mostly legitimate (56) · **low priority / expected**

A closure label (`closed-form`, `proved`, `no-fit`) co-occurring with a `sorry`, predominantly on `conjecture` blocks where the label describes the *conjectured* closed form and the `sorry` is the honest conjecture marker (§3b). These are mostly **not** overclaims — e.g. `borromean-baryon-mass-formula` (a `conjecture` whose `closed-form` label describes the conjectured shape; its real defect is the separate wave-1 λ_scale finding, not this label). Triage individually only if a C2 block's prose asserts the closed form as *established* rather than conjectured.

### other (2)

Edge cases (a `remark`/`definition` with a `sorry` sibling); inspect individually.

## Recommended PR scope

1. **Bucket C1 safe relabel (23)** — drop the `sorry-free` tag/claim wherever a `sorry` is present. Mechanical, low-risk, unambiguous (the claim is false as written). Could be a single `chore(one-voice)` commit.
2. **Bucket B (14)** — per §1a, author chooses per block: finish the Lean, restate with honest `sorry` + `-- Ref:`, or demote to `conjecture`. Needs author judgement; queued.
3. **Bucket C2 (56)** — no action by default; spot-check only those whose prose asserts (not conjectures) the closed form.

## Note on the checker

`status_label_overclaim_audit.py` is high-recall by design (227 raw candidates). The sharp filter (`--json` then grep `lean:` signal for `True`/`trivial`/`sorry`) and these buckets are the actionable distillation. `qa:fail` was deliberately dropped as a signal (stale bib criteria flooded it). Re-run after any relabel batch to confirm the bucket shrinks.
