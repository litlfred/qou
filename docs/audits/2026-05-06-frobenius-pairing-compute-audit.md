# Frobenius-pairing compute audit (2026-05-06)

**Scope.** Every Python script under `computations/`
that touches `tr_M`, `markov_trace`, `mat_trace`, `tr_std`, or any
"trace of a braid word" pattern.  The audit classifies each script
into one of three buckets relative to the master formula

$$
  \langle O \rangle_T
  \;=\;
  \sum_{i,\,j \,\in\, A^*(T)}
    u_i^*\,(G^{-1})_{ij}\,\langle O,\, b_j\rangle
$$

(`prop:confinement-frobenius-reciprocity`, added in this PR).

**Driver.**
[`computations/audit_frobenius_pairing.py`](../../computations/audit_frobenius_pairing.py).
Machine-readable report:
[`docs/audits/frobenius-pairing-compute-audit.witness.json`](frobenius-pairing-compute-audit.witness.json).

## 1. Bucket definitions

- **(A) trace-only.** Computes $\mathrm{tr}_M(W)$ directly — e.g. for
  binding-energy / mass-defect of a closed braid.  CORRECT use of the
  raw Markov trace; the binding observable is the Hamiltonian acting
  diagonally on NF basis elements, and the categorical mass identity
  reduces to $|\mathrm{tr}_M(W)|$ at single brane level
  (`conj:knot-factor-frobenius-pairing` § Step 1).

- **(B) observable-on-state.** Computes
  $\mathrm{tr}_M(O \cdot \rho(\beta_T))$ for some non-Hamiltonian
  observable $O$.  This is the *raw* Frobenius pairing
  $\langle O, T\rangle$, **not** the physical expectation
  $\langle O\rangle_T$.  Correct iff the witness exposes
  `gram_matrix`, `gram_inverse`, `lp_active_set`, `shadow_prices`
  (the four fields the new
  [bound-state-observable validator](../../computations/bound_state_observable_validator.py)
  enforces).

- **(C) conjugation pattern $\mathrm{tr}_M(\beta\,X\,\beta^{-1})$.**
  By cyclicity of the Markov trace this equals $\mathrm{tr}_M(X)$
  exactly, independent of $\beta$.  Any script interpreting such a
  quantity as a "bound-state observable for braid $\beta$" is
  structurally wrong — the dependence on $\beta$ has been silently
  erased.  **All bucket (C) hits are confirmed bugs.**

## 2. Counts (post-scan)

| Bucket | Count |
|---|---|
| (A) trace-only        | **307** |
| (B) observable-on-state (static-detected) | **0** |
| (C) conjugation pattern $\beta X \beta^{-1}$ | **1** |
| skip (no trace token) | 479 |

**Total scanned:** 791 scripts.

### Caveat on bucket (B) detection

Static regex cannot reliably distinguish
$\mathrm{tr}_M(O \cdot \rho(\beta))$ from
$\mathrm{tr}_M(\rho(\beta))$ when the operator is built up through
intermediate variables (e.g. `M_full_std = evaluate_braid_std(full_op)`
followed by `mat_trace(M_full_std)`, with `full_op` constructed
elsewhere).  A 0-count for bucket (B) does **not** mean there are no
observable-on-state computes — it means the conservative static pattern
did not catch any cleanly.  The CI gate
([`bound_state_observable_validator.py`](../../computations/bound_state_observable_validator.py))
provides the more important runtime check: any **witness** whose
`description`/`computation` claims a bound-state observable must
expose the four required fields, regardless of whether static analysis
flagged the script.

## 3. Bucket (C) findings — confirmed bugs

### 3.1 `borromean-axial-coupling.py` (g_A of the proton)

Source:
[`computations/borromean-axial-coupling.py`](../../computations/borromean-axial-coupling.py)
(lines 239–246, pre-fix).

```python
beta_borr     = [("s1", 1), ("s2", -1), ("s1", 1), ("s2", -1)]
beta_borr_inv = [("s2", 1), ("s1", -1), ("s2", 1), ("s1", -1)]
conversion_op = [("s1", 1)]                # σ₁
full_op       = beta_borr + conversion_op + beta_borr_inv   # β · σ₁ · β⁻¹
M_full_std    = evaluate_braid_std(full_op)
tr_full_std   = mat_trace(M_full_std)      # tr(β · σ₁ · β⁻¹) = tr(σ₁)  by cyclicity
suppression   = abs(tr_full_std / tr_bare_std)              # = 1.0 always
g_A_borromean = (5/3) * suppression                          # = 5/3 always
```

The `suppression` factor is structurally **1.0** regardless of $q$,
because $\mathrm{tr}(\beta X \beta^{-1}) = \mathrm{tr}(X)$ by cyclicity
of the matrix trace.  The reported "match" $g_A \approx 1.277$ in the
witness file (line 142 of `categorical-proton.md`) was a numerical
coincidence introduced by the *modulus* and intermediate normalisations
— the underlying claim that the Borromean braid topology modifies
$g_A$ is unsupported by this computation.

This is the same finding documented in
[`docs/audits/2026-05-04-deep-mass-beta-binding-audit.md` §0c](2026-05-04-deep-mass-beta-binding-audit.md);
the present audit promotes that ad-hoc finding into a class-level
diagnosis: any conjugation pattern is a red flag.

**Witness state (pre-fix).**
`computations/borromean-axial-coupling.witness.json`
lacks all four required fields:

- `gram_matrix` ✗
- `gram_inverse` ✗
- `lp_active_set` ✗
- `shadow_prices` ✗

**Remediation.** Rewrite to instantiate the master formula
(`prop:confinement-frobenius-reciprocity`) — load $G^{-1}$ from
[`gram-matrix-dual.witness.json`](../../computations/gram-matrix-dual.witness.json),
load active set + shadow prices from
[`lp_dual_solver.solve_operator_selection_lp`](../../computations/lp_dual_solver.py),
compute $g_A$ as the ratio of two dual pairings.  This is **Item 4b**
of the workplan; the rewrite lands in this same PR.

## 4. Suspected (B)/(C) candidates beyond static detection

Static regex on script source missed several bound-state-observable
computes; the **CI gate validator caught them at the witness level**.
The validator scan
([`bound_state_observable_validator.py`](../../computations/bound_state_observable_validator.py))
flagged the following 4 additional witnesses on the current branch:

| Witness | Hint | Bucket (manual review) | Status |
|---|---|---|---|
| `borromean-axial-coupling.witness.json` | filename `axial-coupling` | (C) — see §3.1 | **fixed in this PR (Item 4b)** |
| `g-a-g-action-derivation.witness.json` | description `g_A` | (B) — `tr_F(e_axial · e_GT) / tr_F(e_vector · e_GT)`, uses Frobenius projector products on $H_n$ but does **not** apply $G^{-1}$ on the LP-active subspace | ticket **AXIAL-G_A-002** |
| `gt-matrix-pslq-probe.witness.json` | description `g_A` | PSLQ ansatz tester — does not recompute $g_A$ from scratch; consumes a known leading expression | candidate for `"observable_type": "raw_trace"` opt-out |
| `shared-residual-test.witness.json` | description `g_A` | residual-comparison harness — consumes existing $g_A$ value | candidate for `"observable_type": "raw_trace"` opt-out |
| `t35-weak-vertex.witness.json` | description `form factor` | (A) — single closed-braid Markov trace; "form factor" wording is the trigger but the compute itself is bucket (A) | candidate for `"observable_type": "raw_trace"` opt-out |

**Decision (this PR).** Only the canonical (C) bug
(`borromean-axial-coupling.py`) is fixed in-line as Item 4b — that is
the cleanest first instance of the master formula and the requested
order of operations.  The remaining four witnesses are **left flagged**
by the validator (warn-only mode); follow-up tickets are filed in §5
below.  The validator is wired warn-only at the workflow level so
this PR does not break CI for the four remaining flags.

## 5. Remediation tickets

| ID | Witness / Script | Bug or status | Fix |
|---|---|---|---|
| **AXIAL-G_A-001** | `borromean-axial-coupling.py` | conjugation $\beta\sigma_1\beta^{-1}$ → cyclic-trivial (bucket C) | rewrite per `prop:confinement-frobenius-reciprocity` (Item 4b, **this PR**) |
| **AXIAL-G_A-002** | `g_a_g_action_derivation.py` | bucket (B) — Frobenius projector trace ratio without $G^{-1}$ + LP active set | follow-up: rewrite as instance of master formula |
| **TRIAGE-001** | `gt_matrix_pslq_probe.py` | PSLQ ansatz tester (consumer, not producer) | follow-up: add `"observable_type": "raw_trace"` to witness |
| **TRIAGE-002** | `shared_residual_test.py` | Residual-comparison harness (consumer) | follow-up: add `"observable_type": "raw_trace"` to witness |
| **TRIAGE-003** | `t35-weak-vertex.py` | Bucket (A) raw trace — wording triggers gate but compute is correct | follow-up: add `"observable_type": "raw_trace"` to witness |

The CI gate is wired warn-only (default) until **AXIAL-G_A-002**
ships and **TRIAGE-001..003** are confirmed; pass `--strict` to
`bound_state_observable_validator.py` once cleared to enforce
hard-fail.

## 6. New CI gate

[`computations/bound_state_observable_validator.py`](../../computations/bound_state_observable_validator.py)
walks every `*.witness.json` and flags entries whose `description`,
`computation`, or `name` claims a **bound-state observable**
(matching keywords `g_A`, `g_V`, `axial coupling`, `magnetic moment`,
`form factor`, `bound-state observable`, `expectation value of`,
…).  Each flagged witness must include either

- all four of `gram_matrix`, `gram_inverse`, `lp_active_set`,
  `shadow_prices`, **or**
- an explicit `"observable_type": "raw_trace"` opt-out at top level
  (for the legitimate (A) bucket case where the observable IS the
  Hamiltonian and the raw Markov trace is the answer).

Wired into `witness-pipeline.yml` warn-only by default; pass
`--strict` to fail CI.  Mirrors `lp_dual_witness_validator.py`.

## 7. Master formula recap

For every confined bound state $T$ and every observable $O$:

$$
  \langle O \rangle_T
  \;=\;
  \sum_{i,\,j \,\in\, A^*(T)}
    u_i^*\,(G^{-1})_{ij}\,\langle O,\, b_j\rangle.
$$

**Three ingredients required**, all witnessable:

1. $G$, $G^{-1}$ from
   [`gram-matrix-dual.witness.json`](../../computations/gram-matrix-dual.witness.json);
2. $A^*(T)$, $u^*$ from
   [`lp_dual_solver.solve_operator_selection_lp`](../../computations/lp_dual_solver.py);
3. $\langle O, b_j\rangle = \mathrm{tr}_M(O\,b_j)$ for $j \in A^*(T)$.

**Red-flag pattern.** $\mathrm{tr}_M(\beta\,X\,\beta^{-1})$ is always
cyclic-trivial; it carries zero bound-state information.  When
encountered in any bound-state-observable compute, fix via the master
formula above, not by ad-hoc rescaling.
