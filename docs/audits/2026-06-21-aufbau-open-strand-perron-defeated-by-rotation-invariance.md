# Aufbau ordering — the open-strand `a=+1` reading is defeated by isolated-atom rotation invariance (Lean: Perron `q` on every block)

**Date:** 2026-06-21
**Branch:** `claude/h-scalar-open-strand-perron-2026-06-21`
**Bean:** e2nf (electron-shell program — Aufbau ordering gap)
**Type:** confirmation + sorry-free Lean anchor for the on-main `H_scalar`
refutation. **Not** a revival of `H_scalar`, **not** a closure, **not** a fit.
**Lean:** [`aufbau-open-strand-perron.lean`](../../content/quantum-observable-universe/molecular-construction/aufbau-open-strand-perron.lean)
(`QOU.Molecular`, sorry-free).

## Relation to the on-main refutation

This doc **agrees with and strengthens**
[`2026-06-21-h-scalar-refuted-post-hoc-functional-choice.md`](2026-06-21-h-scalar-refuted-post-hoc-functional-choice.md)
(sibling, on main). That refutation showed `H_scalar` (orbital energy `= q^ℓ`,
a=+1) is a *fit-by-functional-choice*: QOU's natural observables **bracket**
`a=+1` (confinement-SDP dual → `a=0`; rotation-invariant q-dim trace → `a=+2`)
and **none produces `a=+1`**; decisively, `V_ℓ` (ℓ≥1) has **zero** trivial-block
component, so `q^ℓ` is a **molecular `C_nv`** construct with no isolated-atom
analog.

This doc closes one residual candidate that the refutation did not address head
on — the **open-strand** reading of `q^ℓ` — and contributes the **sorry-free Lean
formalization** of the Perron fact the refutation used only in prose.

## The open-strand candidate (and why it is the natural way to "get `q^ℓ` without a scalar projection")

One could try to rescue `a=+1` without claiming `V_ℓ` has a trivial component:
the merged eigenvalue identity says `σ_i` satisfies `σ²−(q−q⁻¹)σ−1=0` in **every**
representation, so (Lean `hecke_eigenvalue_mem`) its eigenvalues are `{q,−q⁻¹}` in
every block, and for `q>1` the eigenvalue `q` **strictly dominates** in modulus
(Lean `perron_eigenvalue_is_q`: `|−q⁻¹| = q⁻¹ < q`). Hence an **open** strand — a
transfer-matrix *matrix element* `(σ^ℓ)_{ij}`, Perron-dominated — weighs `q^ℓ` on
*every* block, with no scalar projection. So `q^ℓ` does have a representation-
independent origin: ℓ open Perron-transfer steps of the fundamental strand.

## Why the open-strand reading is DEFEATED — isolated-atom rotation invariance

The open-strand matrix element is **not rotation-invariant**: `(σ^ℓ)_{ij}` selects
a preferred pair of basis vectors `i,j` — i.e. a preferred axis. A preferred axis
is exactly a **molecular `C_nv`** (or external-field) feature; an **isolated** atom
has full `SO(3)_q` symmetry and no such axis.

The energy of a rotationally-invariant system must be a **rotation-invariant**
scalar — the **trace** (the quantum dimension), a **closed loop** — not an
off-diagonal matrix element. That invariant is `[2ℓ+1]_q ~ q^{2ℓ}` (a=+2). So:

> For an isolated atom, `SO(3)_q` symmetry forces the energy to be the closed
> (trace) reading `q^{2ℓ}` (a=+2); the open-strand `q^ℓ` (a=+1) is unavailable
> because it requires a symmetry-breaking preferred axis the atom does not have.

This is the **same** lever as the refutation's "rotation-invariant scalar is the
q-dim trace" — applied to dispose of the open-strand candidate specifically.

## The arithmetic (Lean, sorry-free) — `closed = open²`

The two readings stand in an exact relation (Lean `closed_loop_is_open_squared`):

$$
  q^{2\ell} \;=\; (q^{\ell})^2,
  \qquad
  \underbrace{q^{\,n+2\ell}}_{\text{closed (rot-inv), key }n+2\ell}
  = \underbrace{q^{\,n+\ell}}_{\text{open, Madelung }n+\ell}\cdot q^{\ell}
  \quad(\texttt{closed\_key\_exceeds\_open}).
$$

The rotation-invariant (a=+2) reading is literally the **square** of the
open-strand (a=+1) reading; the isolated-atom symmetry selects the square. The
empirical Madelung order is the open key `n+ℓ`; QOU's canonical (rotation-
invariant) observable predicts the closed key `n+2ℓ` — the ℓ-dominated overshoot,
**disagreeing** with the periodic table. This is exactly the refutation's
conclusion, now with the `a=+1`/`a=+2` arithmetic and the Perron-dominance step
formalized.

## Net (owner STRICT — Madelung stays OPEN)

| candidate for the orbital energy | object | `a` | status |
|---|---|--:|---|
| confinement-SDP dual `σ_F` | key `n` | 0 | Coulomb-degenerate (refutation) |
| symmetric-block scalar `q^ℓ` | scalar block | +1 | molecular `C_nv`; no atomic analog (refutation) |
| **open-strand `(σ^ℓ)_{ij}`** | Perron matrix element | **+1** | **defeated here — not rotation-invariant** |
| **rotation-invariant trace** `[2ℓ+1]_q` | q-dimension (closed loop) | **+2** | **the canonical isolated-atom observable — predicts the wrong (ℓ-dominated) order** |

QOU **derives the shell capacities** (`2n²`, sorry-free) but **does not derive the
ordering**: every `a=+1` route (scalar-block, open-strand) requires a preferred
axis the isolated atom lacks, while the rotation-invariant observable gives `a=+2`.
Madelung remains a genuine open problem; per owner STRICT it is **not** accepted
as a semi-empirical input. A real derivation would need a *derived* screening
operator contributing exactly `+ℓ` (per the refutation's "what would a real
derivation need") — not in the corpus.

## Lean anchor (sorry-free)

[`aufbau-open-strand-perron.lean`](../../content/quantum-observable-universe/molecular-construction/aufbau-open-strand-perron.lean):
`hecke_quadratic_factor`, `hecke_eigenvalue_mem` (eigenvalues `∈{q,−q⁻¹}` every
rep), `perron_eigenvalue_is_q` (`|−q⁻¹|<|q|` for `q>1`),
`closed_loop_is_open_squared` (`q^{2ℓ}=(q^ℓ)²`), `closed_key_exceeds_open`. No
`sorry`; verified lean-direct against restored Mathlib oleans (`lake-cache/qou-v4-24-0`),
exit 0. Nothing wired; no fit.

## Provenance

Confirms/extends (on main): `2026-06-21-h-scalar-refuted-post-hoc-functional-choice.md`
(`aufbau_h_scalar_refutation.py`), `2026-06-20-electron-shell-program-synthesis.md`
(§4 + Net updated to record the refutation). Corpus: `symmetric_block_domain_weight`
(scalar-block `q^ℓ`), the `T_γe` Perron eigenvalue identity. No new compute —
structural reading + Lean (formalize-first).
