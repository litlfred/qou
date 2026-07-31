# P≠NP-in-QOU — the bundle-section / Euler-exclusion route (assessment)

**Date:** 2026-07-31 · **Bean:** `qou-0vqb` · **Scope:** (a) scope-limited
negative (a proposed route to the faithfulness link reduces to, and
sharpens, the transfer wall — it does **not** close it). Per AGENTS.md
§"Before declaring refuted": this is scope-**(a)** — "this construction,
alone, does not reach faithfulness," with the invariant that makes it (a)
cited below. It is **not** a scope-(b) structural exclusion of the
faithfulness link itself.

## The proposal

Frame `#P`-hardness of the Jones observable as a **section of a bundle**
over the substrate parameter space; `P = NP` would force that section to
**vanish**; and the vanishing is **excluded by the Euler characteristic**
`χ(A) = −6 ≠ 0`. If it worked, contraposition would give the open
faithfulness link `res ≠ 0 ⟹ P ≠ NP`.

## What is correct (and already proved on `main`)

The bundle-section picture faithfully describes the *proved* part of the
framework:

- **Section.** `q ↦ res_ℛ(χ(A))(q)` is a section over the `q`-line
  (𝔾_m). (`QouPNeqNp`, `PNeqNpEquivalence`.)
- **Zero-locus = torsion `n | 6`.** The residue vanishes exactly at
  roots of unity of order dividing `6` — the Jaeger–Vertigan–Welsh
  classically-tractable set.
- **`χ = −6` pins the locus.** `−6 mod n = 0 ⟺ n | 6`
  (`chi_mod_vanishes_iff`, sorry-free), where `−6 = 2 − 2g` for Bring's
  genus-4 curve.
- **`q₀` avoids the locus.** `q₀` strictly non-torsion ⟹ `res(q₀) ≠ 0`
  (`nontorsion_of_one_lt` + Kummer non-vanishing, sorry-free).

So "a section whose zeros are the tractable torsion points, pinned by the
Euler characteristic `−6`" is a re-description of the already-formalized
non-vanishing leg — not new leverage on the open link.

## Why it does not reach faithfulness (the sharpening)

The step "`P = NP` ⟹ the section vanishes at `q₀`" is false.

1. **The section detects counting-hardness, not decision-hardness.**
   `res(q₀) ≠ 0` ⟺ exact Jones evaluation at `q₀` `∉ FP`, which by JVW is
   a `#P`-hardness (counting) fact.
2. **`#P`-hardness is invariant under `P` vs `NP`.** By Toda, `#P` sits
   above the whole polynomial hierarchy; `P = NP` collapses `PH` to `P`
   but does **not** collapse `#P` to `FP` (that is the strictly stronger
   `P = P^{#P}`). The permanent/matching witness is concrete:
   matching-**decision** ∈ `P`, yet counting matchings stays
   `#P`-complete. Counting-hardness is untouched by the decision
   collapse. (This is `generic_transfer_false` viewed from the section
   side.)
3. **Therefore `res(q₀) ≠ 0` holds in the `P = NP` world *and* the
   `P ≠ NP` world.** A quantity that is identical in both worlds carries
   **no** information about which holds. Hence `res ≠ 0 ⟹ P ≠ NP`
   (faithfulness) cannot follow — the section is `P`-vs-`NP`-invariant.

**Bundle-theoretic statement of the wall.** The section lives over the
**counting** world (`#P`); `P` vs `NP` is a **decision**-world question.
The transfer that faithfulness needs is precisely the passage from the
counting world to the decision world — the one bridge `generic_transfer_false`
refutes as a generic law and Razborov–Rudich / algebrization block as a
uniform one. The bundle picture relocates the wall; it does not remove it.

## The Euler sign is backwards for the naive version

"A nonzero Euler class **excludes** a section's vanishing" is false: a
nonzero Euler class forces a section to **have** zeros (the Poincaré–Hopf /
Euler-class obstruction to a nowhere-zero section), not to avoid them.
What is actually true — and proved — is the milder statement that
`χ = −6` **pins the location** of the zeros (`n | 6`), and `q₀` sits off
that locus. Euler pins *where* Jones-evaluation is tractable; it says
nothing about the decision boundary. Any future "Euler ⟹ faithfulness"
attempt should stop here: the invariant `χ` is `P`-vs-`NP`-blind.

## Disposition

- **Do not** attempt to instantiate `TraceFaithfulness` / `QouPNeqNp`
  via this route — it reduces to the wall (fabricating the instance =
  claiming `P ≠ NP`; AGENTS.md §anti-laundering).
- The **positive** takeaway is a cleaner statement of the wall's nature:
  `res ≠ 0` is a counting (`#P`) invariant, orthogonal to the decision
  separation. Recorded here so the Euler-exclusion route is not re-run.
- The residue non-vanishing and its `χ`-pinned zero-locus remain fully
  proved and correct; only the extra implication "vanishing ⟺ decision
  boundary" is the (permanent) gap.
