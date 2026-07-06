# Palindromicity does NOT justify the scalar projection — it confirms the 2ℓ non-scalar size

**Date:** 2026-06-21
**Branch:** `claude/zealous-hypatia-05xyp9` (PR #2348, bean `e2nf`)
**Trigger:** owner option 1 — "attack `conj:palindromicity-orbital-type` on the
non-scalar content; proving `ℓ = ½·defect` would justify the scalar projection."
**Verdict:** the premise does not hold. Proving palindromicity would **not**
justify the scalar (`q^ℓ`) energy; it **confirms the non-scalar size `2ℓ`**.

## What palindromicity actually says

`conj:palindromicity-orbital-type` (a **conjecture**, tier:E, itself downstream of
`conj:shell-closure-nf-term-count`) characterises orbital *type* by the
palindromic defect of the whole-atom Hecke NF histogram:

| sub-shell | `ℓ` | defect |
|---|--:|--:|
| s | 0 | 0 (palindromic, self-dual) |
| p | 1 | 2 |
| d | 2 | 4 |
| f | 3 | 6 |

i.e. **defect `= 2ℓ`**, and `ℓ = ½·defect`. The `s` content is palindromic
(self-dual ⇒ symmetric block); `ℓ ≥ 1` is **chiral** (non-self-dual ⇒ the
**non-scalar** standard block). This is a *structural label*, not an energy.

## Why this does NOT bridge to the scalar `q^ℓ` energy

1. **The defect `2ℓ` is the SAME `2ℓ` as the non-scalar overshoot.** The
   `(2ℓ+1)`-dim irrep `V_ℓ` has weights `q^{2m}` (top `q^{2ℓ}`) and q-dimension
   `[2ℓ+1]_q ~ q^{2ℓ}` (a=+2). The palindromic defect is likewise `2ℓ`. Both
   measure the **non-scalar size** of the angular content. They are parallel, not
   opposed.
2. **The `½` recovers the LABEL `ℓ`, not the ENERGY.** `ℓ = ½·defect` extracts the
   angular-momentum *quantum number* from the size `2ℓ`. It is **not** a statement
   that the orbital energy is `q^{½·defect} = q^ℓ`. Palindromicity assigns **no**
   energy weight (that is `symmetric-block-domain-weight`, which applies to
   *scalar-block* domains — and palindromicity puts `ℓ ≥ 1` on the **non-scalar**
   block).
3. **So proving the conjecture supports `q^{2ℓ}` (overshoot), not `q^ℓ`.** If
   anything, defect `= 2ℓ` reinforces that the angular content's natural size is
   `2ℓ` — the a=+2 reading. The empirical Madelung `q^ℓ` (a=+1) still requires the
   orbital energy to be the **symmetric-block component** of the angular word —
   the scalar-projection assumption the owner flagged — which palindromicity
   neither contains nor implies.

## The single load-bearing open hypothesis (isolated)

After this, the ordering gap reduces to **one** sharply-stated physical hypothesis,
upstream of palindromicity:

> **H_scalar:** the energy of an atomic orbital with angular momentum `ℓ` is the
> **symmetric-block (scalar, `σ_i ↦ q`) component** of its braid word — `q^ℓ` —
> **not** the genuine non-scalar `V_ℓ` action `q^{2ℓ}`.

- If `H_scalar` holds, Madelung (`a=+1`) follows and `ℓ = ½·defect` is the
  consistent label. But `H_scalar` is **not derived** — it is the assumption that
  the angular (chiral, non-scalar) content contributes its scalar projection to
  the energy.
- Palindromicity is **consistent with** `H_scalar` (defect `2ℓ`, label `ℓ`) but
  does **not force** it; the genuine non-scalar action gives `q^{2ℓ}` (a=+2).
- Both `conj:palindromicity-orbital-type` and `conj:shell-closure-nf-term-count`
  are conjectures, so even a palindromicity-based account would be **doubly
  conditional**.

## Verdict (owner STRICT — Madelung not accepted)

Option 1 does **not** close the ordering gap. It **clarifies** that palindromicity
cannot justify the scalar projection — it parallels the `2ℓ` non-scalar size — and
**isolates** the one open hypothesis `H_scalar` (orbital energy = symmetric-block
component of the angular word). That hypothesis is the precise derivation target;
per owner STRICT it is **not** accepted as a semi-empirical input. The honest
framework-level statement: **QOU's natural non-scalar angular objects give `a=+2`
(overshoot); the empirical `a=+1` Madelung requires `H_scalar`, which is currently
an assumption, not a theorem.**

## Provenance

Corpus: `conj:palindromicity-orbital-type` (+ table2 `defect=2ℓ`),
`conj:shell-closure-nf-term-count`, `prop:symmetric-block-domain-weight` (Lean,
scalar-block only). Builds on `2026-06-20-aufbau-lambda-plus-channel-from-
symmetric-block.md` (the scalar-channel correction). No new compute — this is a
corpus + structural reading, not a numerical search (formalize-first).
