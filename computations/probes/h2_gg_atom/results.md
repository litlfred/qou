# Results: H₂ with a γγ-built nucleon block (owner decision C)

Pre-registration: [`preregistration.md`](preregistration.md), commit `97dacc709d3`, pushed before computing.
Producer `h2_gg_atom_probe.py`, witness `h2-gg-atom.witness.json`, 2/2 checks. mpmath 40 dps (the
`h2_one_rule` code reused unchanged; the pre-registration said 70 dps, which was wrong about the reused
code), convention D, proton pin. Run time 583 s.

## Calibration

- K0: with the production nucleon block, all 28 rows of `h2-one-rule.witness.json` are reproduced
  (levels 3–12) to better than 1e-18.
- K5: χ_(3)(Vᵐ) = 1 for m = 3…7, matching `mjw.chi`. (The pre-registration's parenthetical about
  how V acts on the trivial block was garbled; the correct statement is σ ↦ q, σ⁻¹ ↦ q⁻¹, so V ↦ 1.)

## The nucleon on its own three strands

| nucleon | reading 3, every level | χ_(2,1) at level 3 |
|---|---|---|
| V³ | pass | +1.9942 |
| V⁴ | fail (levels 2, 3) | −1.1707 |
| V⁵ | fail (levels 2, 3) | −0.7724 |
| V⁶ | pass | +1.9768 |
| V⁷ | fail (levels 2, 3) | −1.2908 |

Only m = 3 and m = 6 survive. Within the pre-registered range these are the multiples of 3, i.e.
the core V³ and the core repeated. On three strands the quark block and the gluon merge into the
power of V, so a γγ nucleon is the core alone (or the core twice), and proton and neutron are the
same word (stated in the pre-registration before computing).

## H₂ on the surviving atoms (m = 3 and m = 6 give the same verdicts)

| electron | order | bare H₂ word | bonds passing every level | trace ratio of those bonds |
|---|---|---|---|---|
| T_w0 = σ₀σ₁σ₀ | pe | **pass** | **V³ at s = 4 and s = 5** | 0.99740, 0.99850 |
| T_w0 | ep | **pass** | **V³ at s = 4 and s = 5** | 0.99740, 1 (to 20 digits) |
| trefoil σ₀³σ₁ | pe | fail (level 6) | — | — |
| trefoil | ep | fail (level 6) | — | — |

V and V² bonds fail at levels 6–12 with the T_w0 electron. With the trefoil electron the bare word
fails at level 6, block (3,3), χ ≈ −0.247; K = V or V² at s = 4 (pe order) pass every level, but
the outcome rule requires the bare word to pass, so they do not count.

For m = 4, 5, 7 every row fails, starting at level 2 (the nucleon itself fails).

## Outcome

Per electron, as pre-registered:

- **T_w0 electron: outcome (i), a γγ bond exists.** The bond letters that pass are exactly V³ (at
  either bond site, either order). V³ is also the minimal reading-3 γγ word on H₃, the same word that
  selects the core. The trace drops for three of the four (ratio < 1), and is unchanged to 20
  digits for ep at s = 5; under ruling B that is reported, not used.
- **Trefoil electron: outcome (ii), blocked by the electron.** The nucleon is now pure γγ, so the
  level-6 failure comes from the electron, which is not a γγ word.

This reverses the `h2_one_rule` verdict for T_w0 (there the bare word failed at levels 3–4 because
of the census quark letters). It does not say which electron is right; that is an open owner
question (does the one rule cover the electron?).

## Colour channel (not pre-registered)

Every γγ word has χ_(1³) = 1 exactly, because σ acts on the sign block by −q⁻¹ and σ⁻¹ by −q, so
V acts by 1. Under a rank-3 colour trace the alternating block therefore never fails for a γγ
nucleon. The production template blocks have χ_(1³) = −0.739 (p) and −0.911 (n), from their quark
letters (measured independently on PR #7896). Convention D gives that block weight 0, so this
probe does not see it.

## Scope

Scope (a): this family (Vᵐ, m ≤ 7), these two corpus electrons, the owner-option-1 cell, convention
D at the proton pin. Flavour cannot be represented by a three-strand γγ nucleon; that needs more
strands or a non-γγ letter.

## Derivation of the level-6 trefoil failure (added 2026-11-15, owner request)

Checked by [`level6_trefoil_derivation.py`](level6_trefoil_derivation.py) (sympy over Q(q), 7/7 checks).
Scope: the bare H₂ word, nucleon V³, owner option 1 (no p–e or junction letter).

1. Atom 1 is p ⊗ e on strands 1–6. Closing strands 7–12 multiplies by the trace of atom 2, which
   is positive, so the sign at level 6 is that of χ_(3,3)(p ⊗ e).
2. (3,3) restricted to H₃ ⊗ H₃ is (3)⊠(3) ⊕ (2,1)⊠(2,1) (dimensions 1 + 2·2 = 5), so
   χ_(3,3)(p ⊗ e) = χ_(3)(p) χ_(3)(e) + χ_(2,1)(p) χ_(2,1)(e).
3. In the seminormal (2,1) representation σ₀ = diag(q, −q⁻¹) and σ₁ has diagonal
   (−q⁻²/[2], q²/[2]), so χ_(2,1)(σ₀ᵏσ₁) = (−q^(k−2) + (−1)ᵏ q^(2−k))/[2]. Hence
   χ_(2,1)(σ₀³σ₁) = −1 for every q, and χ_(2,1)(σ₀σ₁σ₀) = 0 (conjugate to k = 2).
4. For p = V³: χ_(3)(V³) = 1 and χ_(2,1)(V³) = −(q⁴−q²+1)(q⁸−2q⁶−2q²+1)/q⁶ ≈ 1.99419 at q₀.
5. Trefoil: χ_(3,3) ∝ q⁴ − χ_(2,1)(V³) ≈ 1.51795 − 1.99419 < 0. T_w0: χ_(3,3) ∝ q³ > 0.
   V³ electron: χ_(3,3) ∝ 1 + χ_(2,1)(V³)² > 0.

Predicted (3,3)/(6) = −0.31373335326276292589; the witness gives the same to 1e-18.
The bracket is negative for 1 ≤ q < 1.18313, so the failure is not specific to q₀.
The T_w0 pass rests on its (2,1) character vanishing; its closure is a Hopf link, not a trefoil.
Not derived: words with a bond letter inside atom 1, where step 1's tensor split does not apply.
