# H_scalar REFUTED — Madelung from QOU is a fit-by-functional-choice, not a derivation

**Date:** 2026-06-21
**Branch:** `claude/aufbau-h-scalar-refute-2026-06-21`
**Compute:** [`computations/aufbau_h_scalar_refutation.py`](../../computations/aufbau_h_scalar_refutation.py)
**Trigger:** owner option 2 — "attack or refute `H_scalar`" (the one open hypothesis
the palindromicity audit isolated).
**Verdict:** **refuted.** `H_scalar` is not a derivation; it is post-hoc selection
of the energy functional that happens to match Madelung. Per owner STRICT, the
ordering stays OPEN — and the honest framework-level statement is that QOU's
*canonical* observable predicts the **wrong** (ℓ-dominated, a=+2) ordering.

## H_scalar, restated

> An atomic orbital's energy is the **symmetric-block (scalar, σ_i↦q)** component
> of its braid word, `q^ℓ` (a=+1, Madelung) — not the non-scalar `V_ℓ` action
> `q^{2ℓ}` (a=+2).

The hidden question: **what *is* "the orbital energy" in QOU, and is `q^ℓ`
canonically privileged?** It is not.

## The framework offers THREE energy functionals → THREE orderings

| functional | object | `a` | fill order |
|---|---|--:|---|
| `σ_F` (confinement-SDP dual, bare `T_ee`) | key `n` | 0 | Coulomb-degenerate — diverges at `3d`/`4s` |
| **symmetric-block scalar [H_scalar]** | `q^ℓ` | **+1** | **= Aufbau ✓** |
| `tr_M` / q-dimension | `q^{2ℓ}` | +2 | ℓ-dominated — diverges at `3s`/`2p` |

`a=+1` (Madelung) sits **between** the framework's two natural outputs (`σ_F`→0,
`tr_M`→+2) and is **never produced** by either. `H_scalar` reaches it only by
selecting the *third* functional — the one that matches the empirical order.

## Why q^ℓ has no ATOMIC justification (the decisive rep-theory)

The atomic orbital with angular momentum `ℓ` is the irreducible spin-`ℓ` rep
`V_ℓ`. Compute (`cg_trivial_mult`):

- **trivial-block multiplicity in `V_ℓ` = `δ_{ℓ,0}`** — **zero for `ℓ≥1`.** So
  `q^ℓ` (the symmetric/trivial-block scalar weight) is **not a component of the
  atomic orbital** at all. It arises only as a braid *word* acting on the trivial
  rep — i.e. the **molecular** `C_nv`-projected domain of
  [`prop:symmetric-block-domain-weight`](../../content/quantum-observable-universe/molecular-construction/symmetric-block-domain-weight.md).
- the trivial block in `V_ℓ ⊗ V_ℓ` has multiplicity **1** — but that is the **2n²
  capacity self-square** (`prop:shell-capacity-self-square`), **not** the energy.
- the rotation-**invariant** scalar of `V_ℓ` (the natural atomic "energy", a
  trace) is the q-dimension `[2ℓ+1]_q ~ q^{2ℓ}` (a=+2) — **not** `q^ℓ`.

An isolated atom has full `SO(3)_q` symmetry; its trivial rep is **only** `ℓ=0`,
and there is **no `C_nv` projector** to import. So `q^ℓ` — a `C_nv` (molecular)
construct — cannot be the energy of an atomic `ℓ≥1` orbital without externally
imposing a symmetry the isolated atom does not have.

## Verdict

`H_scalar` selects the `a=+1` functional **because it matches Madelung**, not
because it is derived. Choosing the energy functional to fit the answer is exactly
the fitting the three-calibration discipline forbids. So:

1. **`H_scalar` is refuted as a derivation** — it is a fit-by-functional-choice.
2. The **canonical** QOU observable (`tr_M`, equivalently the rotation-invariant
   q-dimension trace) predicts **a=+2** — the ℓ-dominated overshoot — which
   **disagrees** with the empirical periodic table (`a=+1`).
3. Madelung therefore stays a genuine **OPEN** problem, and a deeper one than "one
   hypothesis": the framework's natural observables **bracket** `a=+1` (`σ_F`→0,
   `tr_M`→+2) but none produces it. Per owner STRICT it is **not** accepted as a
   semi-empirical input and **not** reached by selecting a functional to fit it.

This is the critical-distance duty discharged: QOU **derives the shell capacities**
(`2n²`, sorry-free Lean) but **does not derive the shell *ordering*** — its
canonical observable predicts the wrong (ℓ-dominated) filling order. That is the
honest reach of the electron-shell program.

## What would a real derivation need (for the record)

A non-fitted `a=+1` would require a *derived* reason the atomic orbital energy is
neither the SDP dual (`a=0`) nor the q-dim trace (`a=+2`) but specifically the
`q^ℓ` half — e.g. a screening operator that provably contributes exactly `+ℓ` per
unit angular momentum, derived from the inner-shell penetration braid
(`Δ(n)∝(n−1)` of `hybridization-sp-gap-braid`) rather than assumed. No such
operator is in the corpus; building/refuting one is the remaining research, not
this audit.

## Provenance

Compute: `aufbau_h_scalar_refutation.py` (3 functionals + CG trivial multiplicities
+ q-dim invariant). Closes the `H_scalar` line opened by
`2026-06-21-palindromicity-does-not-justify-scalar-projection.md`. Corpus:
`prop:symmetric-block-domain-weight`, `prop:shell-capacity-self-square`,
`hybridization-sp-gap-braid`. Structural argument — no wide numerical search
(formalize-first).
