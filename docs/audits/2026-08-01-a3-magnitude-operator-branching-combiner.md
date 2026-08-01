# A=3 magnitude ROUTE 1 — operator-valued branching combiner = scalar Markov trace (scope-(b))

**Date:** 2026-08-01
**Branch:** `claude/a3-magnitude-operator-branching-combiner-2026-08-01`
**Bean:** `qou-jv64` (this task); surviving-route record `qou-tnvz`
**Lean:** `content/quantum-observable-universe/lean/QOU/BraidKnot/A3OperatorCombinerMagnitude.lean`
(sorry-free, lean-direct exit 0, generic `[CommRing R]`)
**Verdict:** **REFUTE (scope-(b) structural exclusion)** of ROUTE 1 as stated.
Nothing wired; `free_parameters = 0`; `μ₃` never inverted.

## The question

The A=3 triton `Δ_λ` magnitude factor `r* = μ₃/c₃ ≈ 1.585`
(μ₃ = +0.4708 the target #4320 residual simplex moment; c₃ = 0.297 =
`E₀·(1 − τ_Borr)` the **derived** single-Markov-trace near-miss #4364) is
bracketed out of every *single-Markov-trace* ingredient — derived level
(#4364/#4376), geometric `W_λ` (#4392), coordination-edge (#4472), exact-order
`μ̄_A` (#4480), and the Vassiliev leading weight of the single Borromean deficit
(#4526). The surviving hypothesis (`qou-tnvz`) is that the missing `1.585×` is a
genuinely **many-body / cross-channel** object.

**ROUTE 1 proposed:** replace the scalar `Σ_λ y_λ χ_λ` Frobenius pairing with
the **operator-valued branching combiner** — the `H₉ → H₆ → H₃` (peel one
nucleon at a time) Wenzl branching, *keeping the operator (matrix) structure*
instead of collapsing to a scalar trace at each level — on the premise (parent
task) that "a single trace loses the cross-channel information; the branching
combiner retains it."

## Finding — the premise is false at the observable level

The observable read off the operator-valued combiner is a **cyclic, additive
trace** `τ` (the Markov trace) of the assembled operator, sliced by the isotypic
projector family `{P i}` of the branching (`i = (ξ,ν)`). The governing invariant
is the **partition-of-unity trace collapse**:

> For any orthogonal resolution of unity in the operator algebra
> (`P i · P j = 0` for `i ≠ j`, `Σ i, P i = 1`) and any cyclic additive `τ`,
> `τ X = Σ i, τ (P i · X · P i)` — off-diagonal blocks vanish under the closed
> trace, and the per-block weight is **identically 1**.

Consequences, all proved sorry-free (generic `[CommRing R]`, `[Ring A]`,
`[Fintype ι]`):

| Decl | Statement |
|------|-----------|
| `trace_partition_collapse` | `τ X = Σ i, τ (P i · X · P i)` (the cited invariant) |
| `operatorCombiner_eq_scalarTrace` | block-resolved readout `= τ X` **exactly** — keeping operator structure multiplies the scalar trace by a factor of **exactly `1`** (0 % of the needed `+58.5 %`; gap identically `0`) |
| `weightedReadout_sub_trace` | deviation `(Σ w_i·τ(P_i X P_i)) − τ X = Σ (w_i − 1)·τ(P_i X P_i)` — the "by how much": all of `μ₃ − c₃` must live in a per-block weight `w_i ≠ 1` |
| `weightedReadout_eq_of_uniform` | uniform weights (`w ≡ 1`) recover `τ X`: no magnitude change |
| `magnitude_change_forces_nonuniform_weight` | contrapositive: a magnitude change **forces** a non-uniform per-block weight |

**Numerical shadow (independent confirmation).** The production compute already
carries the empirical shadow of `operatorCombiner_eq_scalarTrace`:
`computations/canonical_tr_m_via_branching.py` records the operator-valued
branching combiner agreeing with the scalar fine-Bratteli transfer trace to
`4.7e-15` for A≥3, and `computations/a_operator/canonical_tr_m_combiner_crosscheck.py`
is an independent re-derivation confirming the same value. The two produce
identical observable numbers — exactly what the Lean invariant predicts.

## Scope classification

**scope-(b) structural exclusion.** The cited invariant is the
partition-of-unity trace collapse (`trace_partition_collapse`): a proved
identity, not an empirical near-miss. It forces the operator-combiner readout to
equal the scalar Markov trace `c₃`, so ROUTE 1 as stated (keep the matrix
structure, close the canonical trace) supplies **exactly `c₃ = 0.297`, never
`μ₃ = 0.4708`**, and `0` of `r* − 1 ≈ 0.585`.

**What is NOT excluded (the honest boundary).** The invariant excludes only the
*trace-based* readout. It does **not** exclude a genuine **per-block weight**
`w_i ≠ 1` — i.e. a `Δ_λ`-type per-partition weight, which is a *different
functional* than the trace (`weightedReadout_sub_trace` isolates exactly where
such a weight would enter). The missing `1.585×` therefore requires that
`Δ_λ` weight — precisely the standing (open, gate-relaxed) `Δ_λ` closure object.
This is consistent with, and does not re-close, the A=4 PROBE-2 finding
(2026-08-01, `GeometricWLambdaA4Helium.lean`) that a *normalized geometric*
per-block weight can bracket the target: that is exactly a non-uniform `w_i`
route, which lies outside this scope-(b) and stays open. Per the `Δ_λ` gate, any
such `w_i` fixed by inverting `μ₃` is a **fit**, not a derivation, and may not be
wired canonical.

## Why the premise felt plausible — and why it is wrong

The branching *does* retain the operator (matrix) structure internally: the
per-level ρ_ξ(W) ⊗ ρ_ν(β) products and the interface operators A^λ_{ξν}(I) are
matrices, contracted only at the end. The intuition "a single trace loses info"
is correct for the *intermediate* operators. But the **observable** is a single
closed trace of the *assembled* operator, and the Wenzl branching is an **exact
(lossless) decomposition** of that same trace — a change of basis / iterated
partial trace, not a lossy collapse. Trace is basis-independent; reorganizing the
computation cannot change the total. The cross-channel structure is real but
**invisible to the trace** — it is a shadow-price / which-block-saturates
diagnostic (as `canonical_tr_m_combiner_crosscheck.py` already notes), not a
magnitude source.

This is the companion `W = β = 1` magnitude corollary of the existing
`QOU/BraidKnot/InterfaceOperatorBlockDiagonal.lean` (`trace_block_diagonal`),
which proves off-diagonal blocks vanish under the closed trace; the new file adds
the explicit magnitude conclusion + the weighted-readout deviation that isolates
`Δ_λ` as the only remaining handle.

## Next honest step

ROUTE 1 as stated (trace-based operator combiner) is closed. The surviving
handle is the non-uniform per-block weight `w_i` (`Δ_λ`), which the operator
combiner does **not** supply and cannot supply while remaining a trace. Route to
the `Δ_λ` closure program (gate OPEN FOR ALL 2026-07-13); the A=4 PROBE-2
geometric-`W_λ` bracket is the live instance of a non-uniform `w_i`. Anti-fit
still gates: a `Δ_λ`/`w_i` obtained by inverting `μ₃` is a fit.
