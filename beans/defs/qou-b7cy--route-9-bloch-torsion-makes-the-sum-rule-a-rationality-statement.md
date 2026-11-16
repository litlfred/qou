---
# qou-b7cy
title: 'Route 9: Bloch torsion at ℚ(ζ₇)⁺ makes the 5₂ sum rule a RATIONALITY statement'
status: in-progress
pr: 8193
type: task
priority: high
tags:
    - qbeta
    - dilogarithm
    - 5two
    - bloch-group
    - reduction
    - reorg-2026-10-04
created_at: 2026-08-07T17:05:00Z
updated_at: 2026-11-16T20:41:00Z
parent: qou-n4nr
---


## Result: the rationality is PROVED. One rational number is left.

Route 6 hoped the open problem "would stop being a transcendental evaluation and
become a rationality statement", and failed. **That is now achieved**, by a
different mechanism, off the back of Route 8's transport (`qou-8v3k`).

Probe `computations/probes/qbeta_5two_route9_bloch_torsion_rationality_probe.py`,
witness `computations/qbeta-5two-route9-bloch-torsion-rationality.witness.json`,
6 gates at 40 dps, all pass.

## Setup

Route 8 reduced the sum rule to the totally real cyclotomic point. Put
`w := −y = 1 + 2cos(2πk/7)`, so `V(−1,y) = 2Li₂(w) + Li₂(−w) + log²w`, and the
target is `Σₖ Re V = −π²/2`.

`w` is a root of **`w³ − 2w² − w + 1 = 0`**, and

    N(w) = −1,     N(1−w) = −1,     N(1+w) = +1

so **`w`, `1−w`, `1+w` are all units** of `F = ℚ(ζ₇)⁺`.

## The algebraic key — a ring identity, hence a Lean one-liner

    (1 − w)²·(1 + w)  =  1 − w − w² + w³  =  w²        using   w³ = 2w² + w − 1

Therefore, for `ξ := 2[w] + [−w] ∈ ℤ[F]`,

    δ(ξ) = 2·(w ∧ (1−w)) + ((−w) ∧ (1+w)) = w ∧ [(1−w)²(1+w)] = w ∧ w² = 0

in `∧²F* ⊗ ℚ` (the torsion `−1` dies on tensoring). **So `ξ` lies in the Bloch
group `B(F)`.** This is elementary and fully formalizable — `ring` plus the
minimal polynomial.

## The classical input

`F = ℚ(ζ₇)⁺` is **totally real**, so `r₂ = 0` and by Borel `B(F) ⊗ ℚ = 0`: every
element of `B(F)` is torsion. The Rogers dilogarithm carries Bloch torsion into
`π²ℚ`. Hence

    Σ_σ L(σ(ξ)) ∈ π²ℚ           ← the rationality, PROVED modulo that theorem

## The measurement

    Σₖ Re[2L(wₖ) + L(−wₖ)] = π²/2       exactly, to 26 digits   (G5)
    Σₖ Re V = Σₖ Re L(ξₖ) − π²          exactly                 (G6)

giving `Σₖ Re V = π²/2 − π² = −π²/2` ✓, which is Route 8's target and hence the
sum rule.

## ⚠ What is NOT proved

1. **That the rational is exactly `1/2`.** Rationality is proved; the value is
   verified to 26 digits, not derived. Note `π²/2 = 3·L(1)`, which is a
   suspiciously clean value for a 3-embedding trace and is probably the tell for
   an explicit five-term / Y-system derivation.
2. **The `−π²` branch constant in G6.** A per-embedding formula
   `V − L(ξ) = iπ·log[(1−w)/w]` was tried and **is FALSE** — it fails at two of
   the three embeddings on branch grounds; only the *sum* comes out exact. That
   bookkeeping still needs doing properly, and the failed attempt is recorded so
   nobody re-derives it.
3. Nothing here is Lean. Toolchain unavailable in this environment (`qou-clx8`).

## Why this is nevertheless the qualitative step

Every earlier route died on *real part vs volume side*. The chain is now:

    sum rule  --Route 8-->  cyclotomic identity at Q(zeta_7)+
              --Route 9-->  L(xi) for xi in B(F), F totally real
              --Borel-->    L(xi) in pi^2 Q
              --???-->      L(xi) = pi^2/2

Only the last arrow is open, and it is a **rational-number** question, not a
transcendence question. That is a different kind of problem from the one this
bean started with.

## Next step

Pin `1/2`. Two concrete options:

1. **Explicit five-term derivation.** Use the Rogers duplication
   `L(z²) = 2L(z) + 2L(−z)` to rewrite `2L(w) + L(−w) = L(w) + ½L(w²)`, then
   exploit `w² = (1−w)²(1+w)` — exactly the shape that generates Y-system
   dilogarithm identities. **Not attempted.**
2. **Torsion order.** Compute the order of `ξ` in `B(F)` (equivalently the order
   of the relevant class); torsion of order `n` bounds the denominator, and a
   finite check then pins the numerator.

## Refs

* parent `qou-0yqu`; builds on `qou-8v3k` (Route 8)
* siblings `qou-r7ml` (Route 7, refuted), `qou-g2wr` (literature closed)
* PR #4658

---

## 2026-08-07 (later) — the identity is PER-EMBEDDING, and it is a level-7 ladder

The trace statement `Σₖ = π²/2` was weaker than the truth. Each embedding is
*individually* a rational multiple of `π²` (gate **G7**):

| k | `wₖ = 1+2cos(2πk/7)` | `Re[2L(wₖ) + L(−wₖ)]` | in units of `L(1)` |
|---|---|---|---|
| 1 | `2.246979603717…` | `17·π²/42` | `17/7` |
| 2 | `0.554958132087…` | `5·π²/42` | `5/7` |
| 3 | `−0.801937735805…` | `−1·π²/42` | `−1/7` |

**Verified at 100 dps, residuals `~1e-101`** (`0.0`, `1.4e-101`, `1.8e-102`), and
the denominator `42` is **minimal** — scanned all `d < 400` at `1e-60`.

`Σ mₖ = 17 + 5 − 1 = 21`, and `21/42 = 1/2` — which is exactly `Σₖ = π²/2`, hence
Route 8's `−π²/2`, hence the sum rule.

**Denominators of 7 in units of `L(1) = π²/6` are the signature of level-7
dilogarithm ladders.** This is no longer an exotic object: it is three explicit
classical-shaped ladder values.

### What this changes

The Bloch-torsion argument (G2 + `F` totally real) **proves each of the three
values lies in `π²ℚ`** — torsion in `B(F)` gives rationality at *every* embedding,
not merely in the trace, so the proved statement is stronger than first written
above. What remains is only the three **numerators** `17, 5, −1`.

So the final open arrow is now three explicit level-7 ladder identities, each of
a form the five-term relation is built to handle — not one opaque transcendental
constant.

### Also confirmed

Rogers duplication `L(w²) = 2L(w) + 2L(−w)` holds exactly per embedding, so
`2L(w) + L(−w) = L(w) + ½L(w²)`; and `Σₖ Re[L(wₖ) + ½L(wₖ²)] = π²/2` likewise.
Individually, `Σ L(w)`, `Σ L(−w)`, `Σ L(w²)`, `Σ L(1±w)`, `Σ L(1/w)`,
`Σ L(w/(w−1))`, `Σ L(1−1/w)` are **all irrational** — the rationality is a
property of the specific combination `2[w] + [−w]`, i.e. of the Bloch element,
which is exactly what the torsion argument predicts.

**Status: verified to 80 dps, unproved.** Nothing stubbed.

---

## ✅ 2026-08-07 — the algebraic core is now LEAN-PROVED, sorry-free

`QOU/QBeta/FiveTwoCyclotomicBloch.lean`, compiled against Mathlib
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7` on Lean 4.24.0 (toolchain obtained via
the github mirror — see `qou-clx8`). **Six theorems, zero `sorry`, zero `axiom`:**

| theorem | content |
|---|---|
| `bloch_poly` | `(1−w)²(1+w) − w² = w³ − 2w² − w + 1` **as polynomials** — `ring` |
| `bloch_key` | hence `(1−w)²(1+w) = w²` at any root — `linear_combination hw` |
| `minpoly_one_sub` | `1−w` satisfies `u³ − u² − 2u + 1` |
| `minpoly_one_add` | `1+w` satisfies `v³ − 5v² + 6v − 1` |
| `prod_one_sub_x_mul` | Route 8: `∏ⱼ(1 − x·yⱼ) = x` |
| `prod_x_sub` | Route 8: `∏ⱼ(x − yⱼ) = x²` |

`#print axioms` gives `[propext, Classical.choice, Quot.sound]` — the corpus's
standard set; `prod_one_sub_x_mul` and `prod_x_sub` do not even need
`Classical.choice`.

All are stated over an arbitrary `CommRing`, with the deformed-curve Vieta
hypotheses **denominator-cleared**, so no field or `x ≠ 0` assumption is needed.

**This does not shrink what is open.** It formalizes exactly the steps that need
no dilogarithm. The rationality argument (Bloch group + Borel) is **not**
formalizable — see `qou-mlbg` for the measured Mathlib survey — and the three
numerators remain unproved. See `qou-fivt` for the route that avoids Borel.

## ✅ End-to-end composition verified (gate G8)

Every other gate checks one link. G8 reconstructs the **original** sum rule from
the three numerators alone, back through both reductions:

    (Σ mₖ)·π²/42 − π² [Rogers→V] − π² [transport back] = 21/42 − 1 − 1 = −3/2

giving `−3π²/2` with **residual 0.0**. The two reductions compose; nothing was
fudged at a seam.

### ✅ Verified IN-TREE (not just in a scratch project)

The six theorems were first compiled in a standalone project; that is not the
same as compiling in this repo. Now done properly:
`lake build QOU.QBeta.FiveTwoCyclotomicBloch` in
`folio/quantum-observable-universe/lean` → **707 jobs, success**, olean at
`.lake/build/lib/lean/QOU/QBeta/FiveTwoCyclotomicBloch.olean`, and `#print axioms`
in-tree reproduces `[propext, Classical.choice, Quot.sound]` (and
`[propext, Quot.sound]` for the two Vieta products). Recipe: `qou-lnbk`.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## Round 53 Progress (PR #8193)
- [x] Added `unit_inv_w`, `unit_inv_one_sub_w`, `unit_inv_one_add_w`, `norm_one_sub_w_eq_neg_one`, and `norm_one_add_w_eq_one` to `folio/quantum-observable-universe/lean/QOU/QBeta/FiveTwoCyclotomicBloch.lean` (`0 sorry`, `0` vacuity hits).
- [x] Verified 80-dps Route 9 Bloch polynomial identity, unit inverses, norms, and per-embedding level-7 Rogers dilogarithm ladder `(17, 5, -1)/42` in `computations/probes/route89_staircase_wpdb_stargram_probe.py` (`computations/probes/route89-staircase-wpdb-stargram.witness.json`).
- [ ] Await CI verification and Merge Manager merge of PR #8193 (`9d88b10b75877699bcfe0134c2f9a3d95a32edf4`).
