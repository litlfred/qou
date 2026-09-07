# Route 2's fibre datum supplies `q = −1`, and the C1 carrier's own hypothesis is false there

**Date:** 2026-09-07 · **Bean:** `qou-hmrm` · follows `qou-lmnq` (#6769), `qou-7fnr` (#6738), `qou-1z28` (#6695)
**Lean:** [`QOU/Mass/FibreMonodromyOrderTwo.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/FibreMonodromyOrderTwo.lean) — sorry-free, generic `[Field K] [CharZero K]`, `lean -DautoImplicit=false -s 65536` exit 0, axioms `propext / Classical.choice / Quot.sound` on all seven declarations
**Probe:** [`w1_fibre_monodromy_order_probe.py`](../../computations/probes/w1_fibre_monodromy_order_probe.py) — exact sympy over ℚ; one mpmath read-out at 60 dps; no float64; no witness by design; 23/23
**Cited, not re-derived:** `QOU.Mass.QDifferenceConfluentObstruction.qlift_normalized_kernel_exists` — the C1 carrier and its standing hypothesis

## What was asked

W1 (`qou-d8de`) wants a q-difference prolongation `D_q` built from the colour
spectral curve Σ. With route 1 — a q-shift on the base — now closed in all three
charts it could have lived in, route 2 is the live one. It reads, verbatim:

> *Root-of-unity fibre monodromy. The fibre singularity is a root of unity; a
> q-difference connection may arise naturally from its local monodromy.*

Formalize-first, before constructing anything: **which root of unity can that datum
actually supply?**

## The argument

1. **The branch sextic is squarefree.** `D(z) = 16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16 =
   −disc_X P`, `gcd(D, D′)` a unit, six distinct roots (probe S1; also #6769 §1).
2. **The colour cubic never has a triple root.** Matching `P(X,z)` against `(X − r)³`
   gives three coefficient equations. Eliminating `r` between the quadratic and linear
   ones forces `2z² + z + 2 = 0`; between the constant and linear ones,
   `26z³ + 24z² + 24z + 26 = 0`. Together these give `15z = 30`, and at `z = 2` the
   first reads `12 = 0`. So the system is inconsistent for **every** `z` and `r` —
   `QOU.Mass.FibreMonodromyOrderTwo.colorCubic_no_triple_root`, sorry-free.
3. **Hence every branch point is simple.** A branch point is where sheets collide; a
   *total* branch point is a triple root, which step 2 excludes. With `D` squarefree
   the collision is a double root: exactly two sheets meet.
4. **So the local monodromy is a transposition — order exactly 2.** The only root of
   unity the fibre datum supplies is `−1`. Never a primitive cube root, never higher.
5. **And `q = −1` is exactly where C1 cannot live.** `[n]_{−1} = 0` for even `n` and
   `1` for odd. The C1 carrier `qlift_normalized_kernel_exists` assumes
   `∀ k ≥ 1, [k]_q ≠ 0`; `[2]_{−1} = 0` **falsifies that hypothesis**, so the carrier
   theorem does not apply at `q = −1` rather than merely degenerating there
   (`c1_hypothesis_fails_at_neg_one`).

**Conclusion (scope (b); invariants: no-triple-root + squarefreeness for the order,
`[2k]_{−1} = 0` for the collapse).** Route 2 read as *"`q` is the eigenvalue of the
local fibre monodromy"* cannot produce the C1 symbol.

Step 3→4 — simple branch point ⇒ transposition — is **stated in prose and not
formalised**; Mathlib carries no branched-cover monodromy in usable form. The Lean
carries the algebraic fact it rests on, exactly as `DilationBranchLocusRigidity`
(#6769) carried its own geometric step's algebraic core.

## What the probe measured

| § | check | result |
|---|---|---|
| S1 | `D` squarefree; coefficients match the corpus; 6 distinct roots | all true |
| S2 | the triple-root system solved exactly over `ℚ̄` | **no solution**; both eliminations reproduce the Lean's polynomials, `gcd = 1` |
| S3 | multiplicity of every irreducible factor of `D` | `1` — so every branch is a double root |
| S4 | the fibre at `z = ∞` | `(Y+1)(Y²+1)`, `disc = −16` — three distinct sheets, **unramified** |
| S5 | Riemann–Hurwitz `2g−2 = 3(−2) + 6 = 0` | **Σ is elliptic, `g = 1`** |
| S6 | **control** — `X³ − z`, which does have a total branch | triple root `{R: 0, Z: 0}`, `disc = −27z²`, order 2 |
| S7 | `[n]_{−1}`, `n = 0…10` | `0,1,0,1,…` — `[2]_{−1} = 0` |
| S8 | the substrate `q₀` | `1.109978582751380807591669 > 1`, so `|q₀| ≠ 1`: not a root of unity at all |

**S6 is what makes S2 mean something.** An empty solution set is worth nothing unless
the same machinery returns a nonempty one when a total branch really exists; on
`X³ − z` it does, and the discriminant order separates the two cases (2 vs 1).

**S4 is a second, independent confirmation of step 3.** The fibre at infinity is
`(Y+1)(Y²+1)` — *identical* to the fibre at `z = 0`. That is the palindromic
`z ↦ 1/z` symmetry of `D` (`branchSextic_palindromic`) showing up in the geometry
rather than in the coefficients.

## What is genuinely new here, beyond the prune

**Σ is an elliptic curve.** Six simple finite branch points, degree 3, unramified at
infinity ⇒ `g = 1`. Nothing in the corpus had computed the genus of Σ. This is not
decoration for route 3: which q-difference structures a curve admits depends on its
genus, and Ramis–Sauloy–Zhang / Sauloy's local classification is stated for exactly
this kind of input. A genus-1 Σ also makes the `z ↦ 1/z` palindromic symmetry a
candidate automorphism to look at, which the dilation rigidity of #6769 does not
touch — that result is about `z ↦ λz` only.

## Scope — what is NOT excluded

Fixed **before** the argument was run, not after:

- **A q-difference structure that uses the monodromy *representation* without setting
  `q` to an eigenvalue.** The `S₃` covering monodromy is a genuine datum; nothing here
  says it cannot enter a construction, only that its *eigenvalue* is `−1`.
- **A construction at `z = ∞`,** or from the global `S₃` rather than a local generator.
- **Route 3** (Ramis–Sauloy–Zhang / Sauloy framework import) — untouched, and now
  better supplied: it has a genus.
- **The `z ↦ 1/z` involution.** #6769 closed dilations `z ↦ λz`; the palindromic
  symmetry is not of that form and is not covered by it.
- `D_q` is **not constructed.** This tranche removes a reading of a route.

## How this composes with route 1

| where | closed by |
|---|---|
| route 1, base coordinate `z` | #6695 |
| route 1, ramified local coordinate `t` | #6738 |
| route 1, Σ itself | #6769 |
| route 2, `q` = the local fibre-monodromy eigenvalue | this tranche |

The pattern across the four is worth stating plainly: every *global or eigenvalue-level*
realisation of the q-shift has failed, and what survives each time is more local and
more structural. That is consistent with the `qou-d8de` verdict — "pick route 3, import
the framework, before hand-rolling an operator" — and this tranche hands route 3 the
genus it would have had to compute anyway.

## Reproduce

```bash
PYTHONPATH=computations:tools/qou-substrate/python \
  python3 -u computations/probes/w1_fibre_monodromy_order_probe.py
# Lean (lean-direct against the restored olean cache; autoImplicit OFF is REQUIRED
# — a bare `lean` is a weaker check than lake build, see AGENTS.md):
lean -DautoImplicit=false -s 65536 \
  content/quantum-observable-universe/lean/QOU/Mass/FibreMonodromyOrderTwo.lean
```
