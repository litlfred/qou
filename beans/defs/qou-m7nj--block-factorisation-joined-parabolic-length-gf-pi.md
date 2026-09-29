---
# qou-m7nj
title: 'Block factorisation joined: parabolic length + gf_pi -> gf_blocks'
status: completed
type: task
priority: normal
created_at: 2026-08-29T08:28:27Z
updated_at: 2026-08-29T08:28:59Z
---

## What landed (PR #5976, branch `claude/lean-gap-drain-2026-08-29`)

`BodyOrderExpansion.lean`'s section header said the parabolic length formula
was **"not proved here"** and called the section "the bookkeeping half of the
block factorisation, not the content". That was true when written. It stopped
being true one file over, **in the same PR chain**, and nothing updated it.

Rather than only correct the note, closed what the note was about.

### Part 1 — length additivity across A blocks
`length_one`, `lowerOnly_mul`, `lowerOnly_mono`, `blockProd`,
`lowerOnly_blockProd`, **`length_blockProd`**: `ℓ(blockProd w A) = Σ_{i<A} ℓ(w i)`.

I had declined this in #5961 as "index plumbing that adds no insight". The
insight claim was right; the declining was not — **two is not A**, and
`gf_pow`'s A-fold factorisation had nothing to stand on without it.

### Part 2 — a condition that satisfies BOTH hypotheses
`length_blockProd` takes `LowerOnly` and `UpperOnly` separately, leaving open
whether anything satisfies both. `SupportedIn a b w` does, and it is what a
nucleon block IS: block `i` moves strands `3i, 3i+1, 3i+2` and nothing else.
`length_blockProd_of_supportedIn` needs one hypothesis per block;
`supportedIn_one` records the family is inhabited.

### Part 3 — the join
`gf_congr`, **`gf_pi`** (multiplicativity over a **dependent** product index
set — `gf_pow` takes one index set for every factor, which is what A
*identical* blocks would need, and nucleon blocks are not identical), then
`QOU.Knot.BlockGeneratingFunction`: `ofFin`, `length_ofFin`,
**`gf_blocks`**, `gf_blocks_pow`.

`gf_pi` is stated at `CommSemiring` in `GradedGeneratingFunction` rather than
`CommRing` in `BodyOrderExpansion`, per the weakest-typeclass rule — nothing
in it subtracts.

**The content is the two degree functions.** The LHS grades by
`ℓ(blockProd f A)` — one permutation, one algebra, which is what the
Gröbner–Shirshov normal form of `H_{3A}` is filtered by. The RHS is a product
over A independent objects. Only the parabolic length formula makes them the
same number.

## What this does NOT close

That `H_{3A}`'s normal forms are **exhausted** by block products. A general
`w` is a block product times a minimal coset representative, and **the coset
factor is exactly where the inter-nucleon bonds live** — the
`∏_bonds (X + C d)` factor of the measured law
`G_A(x) = [∏_bonds (x + d)] · G_1(x)^A`. This proves the `G_1(x)^A` factor is
what it is claimed to be; it does not prove the decomposition into two
factors. Stated in the file, not only here.

That residue is the live successor: **the minimal-coset-representative
factorisation** (`w = u · v` with `u` a block product and `v` a minimal
representative, `ℓ(w) = ℓ(u) + ℓ(v)`). That is where the missing binding term
would have to enter the Lean side.

## Verification
lean-direct exit 0 on all four files; `#print axioms` on every new declaration
at most `[propext, Classical.choice, Quot.sound]`; `ofFin`, `ofFin_lt`,
`ofFin_ge` depend on none. No `sorry`, no `axiom`, no `native_decide`. No CI
run exists (Actions auto-triggers disabled repo-wide).
