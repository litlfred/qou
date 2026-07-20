# QProlongation — definitional sharpening of "R is the prolongation symbol"

**Date:** 2026-07-20
**Branch:** `claude/argument-principle-residue-sum-2026-07-20`
**File:** [`content/quantum-observable-universe/lean/QOU/Machinery/QProlongation.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/QProlongation.lean)
**Scope tag:** **DEFINITIONAL SHARPENING — NOT keystone gap-closure.**

## TL;DR (brutally honest)

This work re-encodes the already-proved confluent recurrence
`[n+2]_q b_{n+2} = b_{n+1} + b_n` as a single concrete element `D_q = κ·L² − L − 1`
of the `QuantumTorus` q-Weyl ring, and applies the proved QDM principal-symbol
machinery to it. The headline lemma

    symbol D_q = monomial 2 κ = recurrenceKernelLead κ    (sorry-free)

makes the left-hand side of the keystone conjecture
`conj:qdifference-kernel-prolongation-symbol` — "the q-difference kernel `R` is
the prolongation symbol" — a **precise algebraic statement on the quantum torus**.

**It does NOT prove the keystone.** The symbol-match is a **tautological
re-encoding**: `D_q` is written down *as* the recurrence, and the "kernel `R`"
it is matched against is *defined* as the leading term of that same recurrence.
So the match holds by construction. The conjecture stays a conjecture; nothing
is wired to production; the conjecture is NOT relabelled a theorem.

## What was actually proved (sorry-free, `lean`-direct, exit 0)

All in namespace `QOU.Machinery.QProlongation`, generic base ring
`{A : Type*} [CommRing A] [MulSemiringAction Ldeg A]` (§7c-clean — no `ℝ`, no
ordering):

| Lemma | Statement |
|---|---|
| `prolongationOp` (def) | `D_q := emb κ * Lgen^2 − Lgen − 1` |
| `prolongationOp_eq` | `D_q = monomial 2 κ − monomial 1 1 − monomial 0 1` |
| `Lgen_sq`, `emb_mul_Lgen_sq`, `one_eq_monomial` | monomial normal-form bridges |
| `coeffAt_add`, `coeffAt_neg`, `coeffAt_sub` | L-graded coefficient additivity |
| `coeffAt_prolongationOp{,_two,_of_gt}` | the `L^k`-coefficients of `D_q` |
| `topDeg_prolongationOp` | top L-degree `= 2` (for `κ ≠ 0`) |
| `leadDeg_prolongationOp`, `leadCoeff_prolongationOp` | leading degree `2`, leading coeff `κ` |
| `symbol_prolongationOp` | `symbol D_q = monomial 2 κ` |
| `recurrenceKernelLead` (def) | `monomial 2 κ` — the leading kernel term read off the recurrence |
| `symbol_eq_recurrence_kernel` | `symbol D_q = recurrenceKernelLead κ` (for `κ ≠ 0`) |

Verification (per `lean-environment-setup.md` §"VERIFY a single file with
lean-direct"): oleans restored from `lake-cache/qou-v4-24-0`; `LEAN_PATH` set to
the package + Mathlib olean dirs; `lean QOU/Machinery/QProlongation.lean` exits 0
with no diagnostics. **Not** verified via `lake build` (which wipes oleans).

**Sorry count: 0.** No `sorry`, no `axiom`, no `native_decide`, no `: True`.

## Is `D_q` independent, or a tautological re-encoding?

**Tautological re-encoding.** `D_q = κ·L² − L − 1` is literally the recurrence
operator: `L` is the forward shift (`(L·b)ₙ = b_{n+1}`), `L²` gives `b_{n+2}`,
and `κ : A` stands for the top-jet-order q-integer weight `[·]_q` in the
coefficient ring `A = R[M^±]`. Reading the recurrence
`[n+2]_q b_{n+2} − b_{n+1} − b_n = 0` off as an operator gives exactly this.

`recurrenceKernelLead κ := monomial 2 κ` is *defined* as the top-shift-order term
of that same recurrence. Hence `symbol_eq_recurrence_kernel` is true **by
construction** — the QDM `symbol` machinery is (correctly, sorry-free) extracting
the leading monomial of an operator we wrote down *as* the recurrence, and
comparing it to a kernel term we *defined* as that leading monomial. There is no
independent input.

`D_q` is **NOT** defined from the jet-bundle / Seiberg–Witten period geometry.
No SW connection, no prolongation operator `JⁿE → Jⁿ⁺¹E`, no branch-point /
Stokes monodromy of `λ_SW^{(n)}` on `𝒮_c ≅ ℙ¹` enters this file. So the label is:

> **tautological re-encoding of the recurrence's principal part — not
> gap-closure.**

## What genuinely remains open (the real wall this file does NOT touch)

The keystone `conj:qdifference-kernel-prolongation-symbol` asserts a **geometric
attachment**: that the q-difference kernel `R` coincides with the symbol of the
**SW jet-prolongation operator** — equivalently the monodromy/Stokes data of the
prolonged SW connection at the branch-point poles of `λ_SW^{(n)}`. Closing it
requires, on the geometric side and *independently of the recurrence*:

1. Constructing the jet-prolongation operator `JⁿE → Jⁿ⁺¹E` of the SW connection
   (keystone step D) and computing its principal symbol from the connection data.
2. Showing that symbol *equals* `κ L²` (this file's `symbol D_q`) **without
   assuming the recurrence** — i.e. deriving the same leading kernel term from the
   period geometry.

Only step 2 — an independent geometric computation matching this algebraic
symbol — would turn `symbol_eq_recurrence_kernel` from a tautology into a proof
of the keystone. That derivation is **not attempted here** and remains the single
open input (E) of the step-9b binding closure.

## Discipline compliance

- **Anti-laundering (AGENTS.md §"Axiomatization is NOT a Proof").** No axiom /
  conditional class is introduced to stand in for the open keystone; the existing
  `QOU.Mass.QDifferenceKernelIsProlongationSymbol` class is untouched and no
  instance is created. Nothing is wired to a dashboard.
- **"Refuted/closed" over-claim rules.** No durable "closed" / "proved keystone"
  claim is made; the conjecture's `kind` stays `conjecture`.
- **§7c base ring.** Generic `[CommRing A]`; no gratuitous `ℝ`.
- **Corpus-grep for the "open" status.** The keystone is stated open in
  `content/quantum-observable-universe/mass-theory/qdifference-kernel-prolongation-symbol.{md,lean}`
  and remains so; this file adds machinery on the LHS, not a resolution.
