# Finite-page vs perpetual-`ε^ω` — SETTLED (to *language*)

**Date:** 2026-06-09 · **Branch:** `claude/surreal-rescope-ledger-rows-2026-06-09`
**Closes:** the Track-A "next step" checkbox left open on #1995 ("settle
finite-page vs perpetual-`ε^ω` on `motivic-perpetual-obstruction` +
`spectral-sequence-collapse`").

## Finding: already settled in the corpus

Per the corpus-grep discipline, this was **not** an open formalization task —
both legs already exist as content blocks with the decisive status:

### Finite-page leg — PROVED (sorry-free)

[`prop:spectral-sequence-collapse`](../../content/quantum-observable-universe/mass-theory/spectral-sequence-collapse.md)
("GB spectral sequence collapses at `E_1` (semisimple cohomology vanishing)")
is a **proposition** whose Lean sibling
[`spectral-sequence-collapse.lean`](../../content/quantum-observable-universe/mass-theory/spectral-sequence-collapse.lean)
is **sorry-free** (`grep -c sorry` = 0). It is substantive, not a `holds:Prop`
stub:

- a real `class SemisimpleAlgebra` with central-idempotent data
  (`e_central`, `e_idem`, `e_orthogonal`);
- `Derivation` / `innerDerivation` with proved `map_add'` / `map_smul'`;
- the **Whitehead lemma** in axiom form, carrying
  `-- Ref: [cartan1956]` (Cartan–Eilenberg 1956, Ch. IX §7) — a *cited*
  standard result, not a `sorry`;
- the theorem `spectral_sequence_collapses_to_centre`: for semisimple
  `A = H_n(R,q)` at generic `q`, `HH^k(A) = 0` (`k ≥ 1`) ⇒ the GB-filtration
  spectral sequence collapses at `E_1`, concentrating in
  `HH^0 = Z(A) = ⊕_λ R·e_λ`. The Markov trace factors through the centre;
  Plancherel weights `w_λ` are bounded (`Σ_λ w_λ = 1`).

So the **mass / GS tower collapses at a finite page (`E_1`)** — finite order in
`ε`, rank-1, surreal-free. This is the rigorous finite-page leg.

### Perpetual leg — named CONJECTURE, Mostow-convergent

[`conj:motivic-perpetual-obstruction`](../../content/quantum-observable-universe/lifting-and-descent/motivic-perpetual-obstruction.md)
(demoted from `lemma` → `conjecture` 2026-05-02; the Lean `sorry` is the
conjectural content) is the genuinely-perpetual **volume / lifting tower**:
`κ_0` persists at every level `n ∤ χ(A)` — the real `ε^ω` structure. But it is
**Mostow-convergent**: the perpetual obstruction sum converges to the (rigid)
hyperbolic datum, so the `ε`-adic `ℝ`-line `ℝ(ε)` suffices to *track* it. The
infinite-value-group object is never *manipulated as an element*; only its
standard part is read.

## Verdict

The rank-2 / `ε^ω` necessity question is **closed to L (language)**:

| Tower | Block | Page behaviour | Surreal? |
|---|---|---|---|
| Mass / GS | `prop:spectral-sequence-collapse` (**PROVED**, sorry-free) | collapses at `E_1` (finite) | surreal-free |
| Volume / lifting | `conj:motivic-perpetual-obstruction` (conjecture) | perpetual `κ_n ≠ 0 ∀n` | L — Mostow-convergent ⇒ `ℝ(ε)` tracks it |

Neither tower makes surreals *load-bearing*: the finite-page tower collapses
rigorously, and the perpetual tower's `ε^ω` tail is Mostow-convergent (a
standard-part read, not an infinite-value-group manipulation).

**Combined with the millennium-cluster pass-2 rows (all L), every row of the
narrowing ledger is now L.** The corpus carries **no** surreal-*necessary*
narrowing. The keep verdict stands on the *narrowing-language* value, exactly as
#1995 concluded — and the one rank-≥2 candidate that could have made surreals
load-bearing is now confirmed to degenerate at a finite page on the side that
matters (mass), with the other side (volume) Mostow-removable.

## What is NOT claimed

- This does **not** prove `conj:motivic-perpetual-obstruction` (it stays an
  open conjecture; its Lean keeps the conjectural `sorry`).
- "Mostow-convergent ⇒ L" is the *necessity* verdict (surreals not required),
  not a claim that the perpetual structure is trivial.
