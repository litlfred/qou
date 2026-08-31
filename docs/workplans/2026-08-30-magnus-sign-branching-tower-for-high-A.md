# Build plan: branching-basis transfer-matrix tower for the Magnus Ω₂ sign at A ≥ 5

**Date:** 2026-08-30
**Owner directive:** "for A≥5, the branching tower is the next build."
**Goal:** compute `P(A) = Σ_{λ⊢3A} y_λ·tr(ρ_λ Ω₂_λ)` (`y_λ = d_q(λ)²/[n]_q!`,
`Ω₂ = ½Σ_{i<j}[A_{g_i},A_{g_j}]`, germ `A_g = q·∂_qσ_g·σ_g⁻¹`, `ρ = ∏σ_{g_i}`,
word `atom_braid_word_3A(Z,N)`, n = 3A strands) **without** the flat-partition
cost `Σ_λ dim² = (3A)!` that caps the flat-sparse method at A=4.

This is the sign-vs-A map continued: A=2 `−` (deuteron, `qou-dp32`), A=3 `−`
(triton, #6107), A=4 (⁴He, #6183, running). The flat-sparse ceiling and the
measured optimization impacts are in
`docs/audits/2026-08-30-magnus-sign-sparse-scaling-optimization-impact.md`.

## What already exists (grounding — do not reinvent)

- **`computations/markov/markov_trace_recursive.py::markov_trace_of_word(n, word)`**
  — poly-time Markov trace of an arbitrary braid word by reducing to the `T_w`
  Hecke basis (`HeckeElement`) and peeling strands (`tr_m_basis_element`,
  `tr_M(α·σ_{n-1}) = z·tr_M(α)`). Returns a symbolic `sp.Expr` in `z, h`. Works
  for **any n** with no seminormal matrices.
- **`markov/markov_trace_canonical.py::tr_M_element(elem, z, h)`** — Markov trace
  of a general Hecke **element** (a `T_w`-combination), not just a word.
- **`markov/markov_peel.py`, `markov_peel_rust_bridge.py`** — the atomic
  Markov-peel used across the mass tables (Rust-backed).
- **Branching-trace line:** `probes/hecke_branching_trace_decomposition_probe.py`,
  `option-b-h3-h4-bratteli-probe`, `delta-lambda-h6-branching`,
  `sublemma_2_1_h12_he4_branching.py`, `computations/UNIVERSAL-BRANCHING-PLAN.md`.

## The obstruction (measured reasoning — why the cheap route is blocked)

The natural hope is: express `Ω₂` as a `HeckeElement` and feed it to
`markov_trace_of_word`/`tr_M_element` — poly-time for any A. **This does not
work, and the reason is structural, not incidental:**

`σ_g = T_g` is a *q-independent* basis element (the q-dependence lives in the
multiplication `T_g² = h·T_g + 1`, not in the symbol). So `∂_q σ_g = 0` **as an
algebra element**, yet the germ needs `∂_qρ_λ(σ_g) ≠ 0` — the derivative of the
seminormal **matrix**. That derivative is `(∂_qρ_λ)(σ_g)`, the derivative of the
*representation map*, which is a **derivation/cocycle** `H_n → Mat`, not `ρ_λ` of
any fixed element. (Formally the germs generate the *degenerate/graded affine
Hecke algebra* action, not the finite Hecke algebra.) Therefore `Ω₂` is **not** a
`HeckeElement`, and the `T_w`-basis Markov engines cannot consume it. The germ is
irreducibly a representation-level object.

**Consequence:** the tower must contract at the **representation level** (route b
below), keeping the derivative matrices but never forming the full `λ⊢3A` rep.

## The route (b): nucleon-chain transfer matrix

The word `atom_braid_word_3A` is **A disjoint 3-strand nucleon blocks**
(generators in `{3k, 3k+1}`) joined only by the **A−1 inter-nucleon links**
`σ_2, σ_5, σ_8, …` (each multiplicity 1). So:

1. `ρ` is nearly block-diagonal across nucleons — it factors through the
   branching `H_{3A} ↓ H_3^{×A}` with only A−1 crossings mixing adjacent blocks.
2. The germ `A_g` touches strands `g, g+1` only; `Ω₂` keeps adjacent commutators
   only (far-commutativity) → **2-local on the nucleon chain**.

Together these make `tr(ρΩ₂)` a **1D tensor-network / transfer-matrix contraction
along the nucleon chain**: a local H_3 tensor per nucleon, an operator per link,
contracted left-to-right. Cost is linear in A × (bond dimension)^c, **not (3A)!**,
**iff the bond dimension stays bounded**.

## The feasibility gate: bond dimension (measure BEFORE building)

The transfer-matrix bond at the cut between nucleon k and the rest is indexed by
the irreps of the sub-chain `H_{3k}` that appear — bounded by `p(3k)`:

| cut position 3k | 3 | 6 | 9 | 12 | 15 | 18 | 24 |
|---|---|---|---|---|---|---|---|
| p(3k) (bond upper bound) | 3 | 11 | 30 | 77 | 176 | 385 | 1575 |

**MEASURED (step 2, `branching_tower.py --measure-bond`, 2026-08-30):**

| A | n=3A | widest-cut bond p(3(A-1)) | max germ terms / cut | flat (3A)! |
|---|---|---|---|---|
| 3 | 9 | 11 | 2 | 3.6e5 |
| 4 | 12 | 30 | 2 | 4.8e8 |
| 5 | 15 | 77 | 2 | 1.3e12 |
| 6 | 18 | 176 | 2 | 6.4e15 |
| 8 | 24 | 792 | 2 | 6.2e23 |

- **Branching bond = `p(3(A-1))`** — **SUB-EXPONENTIAL** (`p(m) ~ exp(π√(2m/3)) ~
  exp(c√A)`), **not polynomial** (`p(m)` is not a polynomial), but vastly below
  the flat `(3A)!`. Corrected from the plan's earlier "polynomial" wording.
- **Germ locality = ≤ 2 straddling Ω₂ terms per cut, for every A** (each term
  spans 3 consecutive strands, so only `a ∈ {3k-2, 3k-1}` cross the cut). O(1),
  A-independent — measured, not argued.
- **Link/ρ locality:** a seminormal `σ_g` is a ⊕ of 1×1/2×2 blocks (step 1), so a
  straddling crossing couples the two sides at operator-Schmidt rank ≤ 2; ρ's
  A−1 links ⇒ its MPO bond across any nucleon cut is O(1).

**Verdict: the nucleon-chain contraction costs `~ A·p(3(A-1))^c ~ exp(c'√A)` vs
the flat `exp(3A·ln 3A)`.** A≫4 is feasible: A=16 → bond ~9e4 vs flat 48! ~1e61.
The germ does NOT blow the bond up (its locality is O(1)); the only growth is the
sub-exponential branching bond. **Step 2 decision: BUILD steps 3-4.**

## Correctness gate (non-negotiable)

The tower must reproduce the **flat-sparse** `P` to full precision at:
- **A=3** (triton, committed `triton-magnus-omega2-sign.witness.json`,
  `P = −19243689.1842…`), and
- **A=4** (⁴He, from #6183 once it lands).

Only after matching both may the tower be trusted for A≥5. Same discipline as the
flat-sparse probe's gate (reproduce dense on small λ before scaling).

## Build steps (ordered; each gated)

1. **Branching restriction map** `H_{3A} ↓ H_{3(A-1)}×H_3` in the SYT basis
   (remove-last-3-boxes; the SYT basis *is* the iterated branching basis, already
   used by `sublemma_2_1_h12_he4_branching.py`). Validate the restriction against
   the flat seminormal rep on H_6, H_9.
2. **Measure the bond dimension** at each nucleon cut for A=3,4 and the germ
   operator's rank on the bond. Decide poly vs blow-up. **If blow-up → stop and
   report; A is capped even for the tower.**
3. **Local tensors:** the per-nucleon H_3 block of `ρ` and the link operators;
   the germ `A_g` as a 2-local operator across a cut.
4. **Transfer-matrix contraction** left-to-right along the chain, carrying the
   `y_λ` Wedderburn weight through the branching (`y_λ` factorizes over the
   branching via the q-hook-length recursion).
5. **Gate** against A=3 then A=4. Then run A=5 (⁶Li/⁶He, H₁₅), A=6, …

## Honest status

- This plan is grounded and the bond-dimension bound is **promising (poly)**, but
  step 2 is a real feasibility gate that has **not** been measured yet — the germ
  operator's bond rank could still blow up. Do not promise A=8 until step 2.
- The germ-blocks-the-Markov-word finding above is a genuine negative that
  *narrows* the build to route (b); it is not a dead end for the tower, only for
  the cheap shortcut.
- Anti-fit/scope-(a) discipline unchanged: any A≥5 sign is a dimensionless
  structural datum, no MeV, nothing wired.

**Immediate next action:** implement step 1 (branching restriction + validation
on H_6/H_9) and step 2 (bond-dimension measurement), gated against the triton.
Not started here — this file is the plan.
