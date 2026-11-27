# GRT right action preserves the pentagon: derivation and what blocks the unconditional form

Bean `qou-3fdg`, stage 3b; epic `qou-dk7p`. Lean:
`folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/RationalAssociator/GRTAction.lean`
(sorry-free; `#print axioms pentagon_act` gives `propext, Classical.choice, Quot.sound`).

## 1. The formula

Drinfeld 1991, p. 852 (after Remark 3; `library/drinfeld1991-quasitriangular/sections/page-013.md`):
`φ̃(A, B) = φ(g A g⁻¹, B) · g(A, B)`. This is Furusho 2010, Lemma 8, `φ ∘ g`.

Since conjugation by `G = g(a, b)` is an algebra automorphism,
`φ(G a G⁻¹, b) = G · φ(a, G⁻¹ b G) · G⁻¹`, so `φ̃(a, b) = G · φ(a, G⁻¹ b G)` (`actEval_eq`).

The categorical form in Remark 3, "the old associativity composed with `g(ln τ ⊗ id, id ⊗ ln τ)`",
reads in coordinates as `Φ · g(t₁₂, Φ⁻¹ t₂₃ Φ) = g ∘ φ`. That has the roles of `φ` and `g`
swapped. The remark is stated for a category whose old associativity is the identity (`Ug`-modules
with `τ = e^{ht}`), where the two forms agree. Away from that case the right action is `φ ∘ g`,
and the file uses `φ ∘ g`.

## 2. The derivation (proved: `pentagon_act`)

Fix a `DK4` family `t`. Let `G₁₂₃ = g(t₁₂, t₂₃)`, `G_{12,3,4} = g(t₁₃+t₂₃, t₃₄)`,
`G_{1,2,34} = g(t₁₂, t₂₃+t₂₄)`, `G_{1,23,4} = g(t₁₂+t₁₃, t₂₄+t₃₄)`, `G₂₃₄ = g(t₂₃, t₃₄)`, all
units. Put `P = G_{1,2,34} G_{12,3,4}` and `Q = G_{1,23,4} G₁₂₃`. The pentagon for `g` at `t` is
`P = G₂₃₄ Q`.

Write each `φ̃`-factor as `G · φ(…)` and move every `G` to the far left by conjugation. Both sides
then become `P · (product of three or two φ-evaluations)`. The φ-evaluations are the pentagon of
`φ` at the **transported family**:

| | |
|---|---|
| `s₁₂` | `t₁₂` |
| `s₂₃` | `G₁₂₃⁻¹ t₂₃ G₁₂₃` |
| `s₁₃` | `t₁₃ + t₂₃ − s₂₃` |
| `s₃₄` | `G_{12,3,4}⁻¹ t₃₄ G_{12,3,4}` (`= P⁻¹ t₃₄ P`) |
| `s₂₄` | `P⁻¹(t₂₃ + t₂₄)P − s₂₃` |

This is `t` rewritten in `((12)3)4` coordinates along `g`'s constraints. The proof needs only the
pentagon of `g` and four commutations, each of the form "a `g`-evaluation commutes with whatever
both its arguments commute with" (`commute_eval`):

* `G_{12,3,4}` commutes with `t₁₂`;
* `G_{1,2,34}` commutes with `t₃₄`;
* `G_{1,23,4}` commutes with `t₂₃`;
* `G₁₂₃` commutes with `t₁₂+t₁₃+t₂₃`, and `G₂₃₄` with `t₂₃+t₂₄+t₃₄`.

No other GRT condition on `g` (5.13, 5.14) is used. So `pentagon_act` states:
**pentagon(g, t) ∧ pentagon(φ, s) ⟹ pentagon(φ̃, t)**.

## 3. What blocks the unconditional statement

To replace "pentagon(φ, s)" with "φ satisfies the pentagon at every `DK4` family", `s` must be a
`DK4` family, with some `s₁₄`; the natural choice is `s₁₄ = t₁₄+t₂₄+t₃₄ − s₂₄ − s₃₄`. Proved so far:

* `transported_d4`: `(s₁₂, s₁₃, s₂₃)` is `DK3` (`dk3_twist`).
* `transported_d0`: `(s₂₃, s₂₄, s₃₄)` is `DK3`. It is the `Q`-conjugate of the `G₂₃₄`-twist of
  `(t₂₃, t₂₄, t₃₄)`, and the proof uses the pentagon of `g`.

The `{12,3,4}` coface is the `G_{12,3,4}`-twist of `d₁t`, by the same lemma (not yet written). The
`{1,2,34}` and `{1,23,4}` cofaces are expected to follow the same way.

**The gap, measured.** Over the 15-dimensional space of degree-2 Lie words in six generators, the
`DK4` relations span 11 dimensions. The relations of the five three-strand cofaces span only **10**.
Adding the far relation `[s₁₃, s₂₄] = 0` brings the span to 11; adding `[s₁₂, s₃₄]` or
`[d, s_{ij}]` does not. The rank was computed with numpy; the script was in the scratchpad and is
not committed.

So even DK3 on all five cofaces would leave `[s₁₃, s₂₄] = 0`. That is a genuine coherence statement
about `g`'s constraints, with `s₁₃ = t₁₃ + t₂₃ − G₁₂₃⁻¹ t₂₃ G₁₂₃` and
`s₂₄ = P⁻¹(t₂₃+t₂₄)P − s₂₃`. Two things are not determined here:

* whether it follows from the pentagon of `g` alone, or needs 5.13/5.14;
* which bracketing makes it a direct conjugation identity.

Once `s` is `DK4`, the rest is mechanical. In `U4 N` (`UniversalDK.lean`), words of length `N` in
`s` vanish, because each `s_{ij}` lies in the augmentation ideal. Then `lift` sends the universal
pentagon of `φ` to `s`, and the action theorem holds at every truncated family.

## 4. Next honest steps

1. Prove `[s₁₃, s₂₄] = 0`, or find that 5.13/5.14 is needed, and name it as a hypothesis.
2. Prove DK3 for the `{12,3,4}`, `{1,2,34}` and `{1,23,4}` cofaces, then assemble `DK4 s`.
3. Prove that the augmentation ideal of `U4 N` has `I^N = 0`, so that words in `s` vanish.
4. Compose with `lift` to get the unconditional theorem.
