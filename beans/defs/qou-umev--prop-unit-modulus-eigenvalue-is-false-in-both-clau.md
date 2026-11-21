---
# qou-umev
title: prop:unit-modulus-eigenvalue is false in both clauses; its proof derives -2 from a theorem that gives +1.994
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-22T05:40:00Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-q4oa
---

Found by `agent:n02` on the mass-theory trap-drain; **re-derived
independently** in the coordinating session by constructing the
2-dimensional Hoefsmit representation of `H₃(q)` from scratch — solving the
braid relation for its free parameter and verifying
`(σ − q)(σ + q⁻¹) = 0` on both generators — rather than reusing any corpus
value.

## The block

`mass-theory/unit-modulus-eigenvalue.md`:

> *For any braid word `β` of **even length** in `H₃(q)`, the eigenvalues of
> the standard representation `ρ₍₂,₁₎(β)` lie on the unit circle `|λ| = 1`.
> The Borromean braid `β_Bor = (σ₁σ₂⁻¹)³` has the degenerate eigenvalue
> `λ = −1`.*

## Clause 2 is false, and the proof contradicts its own citation

`unit-modulus-eigenvalue-proof.md:15` asserts

> *"the Lean-proved closed form
> ([`thm:borromean-markov-trace-closed-form`]) together with the Wedderburn
> decomposition yield `χ₍₂,₁₎(β_Bor) = −2`. The characteristic polynomial is
> then `λ² + 2λ + 1 = (λ+1)² = 0`."*

That closed form is `2 − 3h⁴ − h⁶`. Symbolically, my construction gives

```
χ₍₂,₁₎((σ₁σ₂⁻¹)³) = −q⁶ + 3q⁴ − 3q² + 4 − 3q⁻² + 3q⁻⁴ − q⁻⁶
                  = 2 − 3h⁴ − h⁶        (difference simplifies to 0)
                  = +1.99418581297996   at the proton pin
```

**+1.994, not −2.** The proof cites a theorem and then states a value that
theorem contradicts. Two sibling blocks already have it right —
`borromean-markov-trace-closed-form` and `universal-braid-branching-proof`
("≈ 1.994").

The true eigenvalues, from `det = 1` and that trace:

| | |
|---|---|
| discriminant `tr² − 4` | **−0.02322294331** → complex conjugate pair |
| eigenvalues | `0.99709290649 ± 0.0761953793 i` |
| `\|λ\|` | **1.0** |
| angle | **±4.3699091°** |

So `λ = −1` (which would be 180°) is wrong by a wide margin — but note the
unit-modulus property *does* hold for this braid, for a reason the proof
never gives: `det = 1` with `|tr| < 2`.

## Clause 1 is false as stated, and `σ₁²` is the counterexample

`σ₁²` is an even-length word. `χ₍₂,₁₎(σ₁²) = (q⁴+1)/q² = 2.04370620853`,
discriminant `+0.17673507`, so the eigenvalues are **real**: `q² = 1.232052`
and `q⁻² = 0.811654`. Neither is on the unit circle.

The proof's parenthetical — *"|tr| ≤ 2, which holds for real traces of 2×2
matrices with unit determinant"* — is false in general (`diag(2, ½)`) and
false here. The correct statement is conditional: an even-length word has
`det ρ₍₂,₁₎ = 1`, and *then* `|tr| ≤ 2` iff the eigenvalues are on the unit
circle. Even length gives the determinant, not the trace bound.

## Why this matters beyond one block

The block's own eigenvalue table and its "baryon–meson duality" section are
built on `λ = −1`. `agent:n02` also found, in the same table, that
`χ₍₂,₁₎(σ₁σ₂) = −1` **exactly and independent of q** (confirmed here), so
the tabulated angle is **120°**, not the 59° printed; and that `σ₁σ₂` is
labelled the Hopf link when its closure is one component (the permutation is
a 3-cycle) — the Hopf link is `σ₁²` in `B₂`.

The Lean is **not** at fault and should not be "fixed": `borromean_eigenvalue_neg_one`
takes `tr = −2` as an explicit hypothesis and says so in its docstring. It is
a valid conditional whose premise is false, which is the
"conditional-proved ≠ premise-established" pattern AGENTS.md names — here
with the premise now positively refuted rather than merely unestablished.

## What would close this

1. **Correct the proof's `χ` value to `+1.994…`** and re-derive the
   eigenvalues (conjugate pair at ±4.37°, still on the unit circle).
2. **Restate clause 1 conditionally** — even length gives `det = 1`; the
   unit-circle conclusion needs `|tr| ≤ 2` as a hypothesis, which `σ₁²`
   violates.
3. **Re-examine what the duality section actually needs.** If it needs
   `λ = −1` specifically, it does not survive; if it needs only
   `|λ| = 1`, it survives clause 2's correction but must carry the trace
   hypothesis.
4. Fix the table's 59° → 120° and the `σ₁σ₂` link label.

Do **not** discharge this by weakening the proposition until it is trivially
true; state the hypothesis it actually needs.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8462, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — paper-structure drain (https://claude.ai/code/session_01Qmmkt8R1YXFpKDbBiKB3hh)

Mostly fixed on main (conditional statement, σ₁² counterexample, 120° row, duality withdrawn). One wrong sentence left in unit-modulus-eigenvalue-proof.md: 'χ(β_Bor) = 2 − h⁴' — the block's own formula equals 2 − 3h⁴ − h⁶ (sympy, this session; 1.99419 vs 1.99809 at q₀), and 'holds specifically for Borromean' fails at q = 2 (same block). Fix proposed, owner-gated.

Report: docs/audits/2026-11-21-paper-structure-bean-drain.md on branch claude/paper-structure-drain-2026-11-21.
