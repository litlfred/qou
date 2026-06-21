# Finite-page vs perpetual-`ε^ω` — SETTLED (to *language*)

**Date:** 2026-06-09 · **Branch:** `claude/surreal-rescope-ledger-rows-2026-06-09`
**Closes:** the Track-A "next step" checkbox left open on #1995 ("settle
finite-page vs perpetual-`ε^ω` on `motivic-perpetual-obstruction` +
`spectral-sequence-collapse`").

## Finding: already settled in the corpus

Per the corpus-grep discipline, this was **not** an open formalization task —
both legs already exist as content blocks with the decisive status. The
settling rests on a **standard mathematical result** (Whitehead's lemma), not on
a from-scratch Lean proof.

### Finite-page leg — rigorous by a standard (cited) result

[`prop:spectral-sequence-collapse`](../../content/quantum-observable-universe/mass-theory/spectral-sequence-collapse.md)
("GB spectral sequence collapses at `E_1` (semisimple cohomology vanishing)").
The **mathematical claim** is textbook: a semisimple algebra `A` over a field of
characteristic zero has `HH^k(A) = 0` for `k ≥ 1` (Whitehead's lemma,
Cartan–Eilenberg 1956 Ch. IX §7), so the GB-filtration spectral sequence
collapses at `E_1`, concentrating in `HH^0 = Z(A) = ⊕_λ R·e_λ`. `H_n(R,q)` is
semisimple at generic `q`, so this applies.

**Status of the Lean sibling** ([`spectral-sequence-collapse.lean`](../../content/quantum-observable-universe/mass-theory/spectral-sequence-collapse.lean)):
it formalizes the **structure**, not a from-scratch cohomology proof —

- `class SemisimpleAlgebra` records the central-idempotent data
  (`e_central`, `e_idem`, `e_orthogonal`);
- `class WhiteheadHH` records Whitehead's lemma as an **axiom-class**
  (`inner_of_derivation`), carrying `-- Ref: [cartan1956]` / `[weibel1994]`,
  *because Mathlib has no Hochschild-cohomology framework yet*;
- `theorem spectral_sequence_collapses_to_centre`, conditional on
  `[SemisimpleAlgebra R A] [WhiteheadHH R A]`, currently extracts the
  idempotence fact `e i * e i = e i`; the collapse content proper is carried by
  the cited `WhiteheadHH` class, not re-proved in Lean.

So the file is **sorry-free but rigorous-*by-citation***: the collapse is a
standard result, correctly cited and structurally encoded — **not** a completed
Lean proof of HH-vanishing (that awaits a Mathlib Hochschild framework). The
finite-page leg is settled on the strength of Whitehead's lemma, which is the
honest basis.

### Perpetual leg — named conjecture, class-axiomatized

[`conj:motivic-perpetual-obstruction`](../../content/quantum-observable-universe/lifting-and-descent/motivic-perpetual-obstruction.md)
(demoted from `lemma` → `conjecture` 2026-05-02) is the genuinely-perpetual
**volume / lifting tower**: `κ_0` persists at every level `n ∤ χ(A)` — the real
`ε^ω` structure. Its Lean
([`MotivicPerpetualObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/LiftingDescent/MotivicPerpetualObstruction.lean))
packages the conjectural content as the `MotivicGaloisCharacter` **class**
(`almost_everywhere_nontrivial` field); `theorem motivic_perpetual_obstruction`
is **conditional on a `[MotivicGaloisCharacter …]` instance** and contains no
literal `sorry` — a concrete instance is where the substrate axiom (or `sorry`)
would live (AGENTS.md §3b conditional-class pattern).

The tower is **Mostow-convergent**: the perpetual obstruction sum converges to
the (rigid) hyperbolic datum, so the `ε`-adic line `ℝ(ε)` suffices to *track* it
— the infinite-value-group object is never *manipulated as an element*, only its
standard part is read.

## Verdict

The rank-2 / `ε^ω` necessity question is **closed to L (language)**:

| Tower | Block | Page behaviour | Lean status | Surreal? |
|---|---|---|---|---|
| Mass / GS | `prop:spectral-sequence-collapse` | collapses at `E_1` (finite) | sorry-free; Whitehead **axiomatized** (cited `[cartan1956]`) — rigorous-by-citation, not from-scratch | surreal-free |
| Volume / lifting | `conj:motivic-perpetual-obstruction` | perpetual `κ_n ≠ 0 ∀n` | conjecture; class-axiomatized (`MotivicGaloisCharacter`), conditional theorem | L — Mostow-convergent ⇒ `ℝ(ε)` tracks it |

Neither tower makes surreals *load-bearing*: the finite-page tower collapses by a
standard (cited) result, and the perpetual tower's `ε^ω` tail is
Mostow-convergent (a standard-part read, not an infinite-value-group
manipulation).

**Combined with the millennium-cluster pass-2 rows (all L), every row of the
narrowing ledger is now L.** The corpus carries **no** surreal-*necessary*
narrowing. The keep verdict stands on the *narrowing-language* value, exactly as
#1995 concluded — and the one rank-≥2 candidate that could have made surreals
load-bearing degenerates at a finite page on the side that matters (mass, by
Whitehead), with the other side (volume) Mostow-removable.

## What is NOT claimed

- **Not** that the Lean *proves* the spectral-sequence collapse from scratch —
  Whitehead's lemma is an axiom-class (cited), pending a Mathlib Hochschild
  framework. The leg is rigorous because Whitehead is a **standard theorem**, not
  because Lean re-derives it.
- **Not** that `conj:motivic-perpetual-obstruction` is proved (it stays an open
  conjecture; the conjectural content is class-axiomatized, and the file carries
  no literal `sorry`).
- "Mostow-convergent ⇒ L" is the *necessity* verdict (surreals not required),
  not a claim that the perpetual structure is trivial.
