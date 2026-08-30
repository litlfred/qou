# Deuteron binding via the Gram (⟨g,g⟩) + confinement SDP — compute investigation

**Date:** 2026-08-29
**Tier:** compute audit (a scope-(a) negative + a structural prune)
**Arc:** bk-crossing mass-binding, item 4 (re-scoped under Owner Ruling A)
**Directive:** under Ruling A (deuteron binding is *not* a volume term), compute the 2-body
binding from the Gram/Frobenius pairing + confinement SDP.

## The mechanism (corpus)

The operator-selection SDP (`prop:mass-coefficient-shadow-price`, canonical solver
`lp_dual_solver.solve_psd_operator_selection_sdp`):

- cost `t_i = tr_M(b_i)` — per-operator mass-formula summand
- **Gram `G_ij = tr_M(b_i·b_j)`** — the ⟨g,g⟩ Frobenius overlap
- target `n_target = |tr_M(W_atom)|`
- solve `min Σ t_i x_i  s.t.  Σ x_i = n_target, G x ≥ 0`; the dual `y_star[i] > 0` = the
  active binding shadow prices ("most receptive sub-braids").

Two basis choices exist:
- **block projectors** `b_λ = P_λ` (λ ⊢ n) → Gram is **diagonal** `G_λμ = δ_λμ·tr_M(P_λ)`
  (`deuteron_real_sdp.py`, `nucleus_sdp_assembly.py`). This is the whole *centre* of H_n.
- **full Hecke basis** `{b_i : i=1..[n]_q!}` → **off-diagonal** Gram (`aK_via_lp_dual_hecke_basis.py`).
  Run only at **H₃** (6-element basis); the deuteron needs **H₆ (720 elements)** and it has
  **never been run**.

## Result — computed this session (`deuteron_real_sdp.py`, H₆, 11 blocks λ⊢6)

`tr_M(β_D) = 0.5751722458` (convention-inherited — see caveat). SDP outcomes:

| encoding | feasible | primal_obj (MeV) | reading |
|---|---|---|---|
| diagonal SDP (unconstrained) | yes | **3.7e-43** | degenerate ≈ 0; all 11 blocks "active" (no selection) |
| support-restricted / Phase-B interim | yes | 0.0370 | 60× under-binds the 2.2246 AME; a restricted-support artifact, not derived |
| 1 bar-involution fold | yes | **0.0** | carries no binding |
| 2 character-projection colour-flavor | **no** | — | ⚠ ANSATZ, infeasible |
| 3 conservation laws | yes | **0.0** | carries no binding |
| 4 **ame-binding-equality** | yes | **2.22456607** | **= AME 2.2245662 MeV exactly — circular** (the answer is the constraint RHS) |
| 5 LR-branching canonical | yes | **0.0** | carries no binding |
| 6 scalar 9-pair ratio | yes | 0.0 | ⚠ ANSATZ (fitted) |

**0 of 6 encodings derive the deuteron binding.** Five give 0 (or infeasible/ansatz); the only
physical non-zero value is the one where the AME binding is *fed in* as the constraint.

## Why — the structural prune (formalize-first)

This is the intensive/extensive gap the Δ_λ magnitude gate already names
(`AGENTS.md`: "no per-block weight converts an intensive quantity into an extensive one; the
missing term is a separate, super-pairwise additive extensive object"). A **per-nucleus
block-selection SDP is intensive** — its objective just re-selects blocks to reproduce the mass
trace `tr_M(β_D)`. **Binding is an extensive difference** (free − bound), which a single-nucleus
selection does not see. The degenerate `≈ 0` and the five zero encodings are that gap, measured.

So the diagonal Gram is dead for binding, and the six constraint encodings do not rescue it. The
**only** un-run sub-route is the full off-diagonal H₆ 720-element Hecke Gram `G_ij = tr_M(b_i b_j)`
— but it carries the **same negative structural prior** (still a per-nucleus selection), so it
should not be run speculatively: it needs a prior argument that the *non-central* directions carry
an extensive term, which nothing currently supplies.

## Convention caveat

Every number here is **convention-inherited**: the Gram flows through `pyhecke/gram.z`, whose
D-migration is `qou-cds2` (in-progress, Gram singularity under D). `tr_M(β_D) = 0.5751722458` and
all duals are therefore **D-status open** until the engine migrates. See
[`2026-08-29-arc-convention-d-inheritance-audit.md`](2026-08-29-arc-convention-d-inheritance-audit.md).

## Verdict

**Scope-(a) negative:** the deuteron binding does **not** derive from the block-diagonal Gram +
confinement SDP (nor from the six off-diagonal constraint encodings) — the route is structurally
intensive and the one non-zero result is AME-fed. This is consistent with Ruling A (binding is not
a volume term) and sharpens it: the missing 2-body binding is the **same extensive term** the
general Δ_λ magnitude gate is open on. The full H₆ off-diagonal Gram is the only remaining
sub-route and carries a negative prior; do not spend it without a structural reason to expect the
non-central directions to be extensive.
