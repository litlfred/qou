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

## 5. Stage 3c outcome: the far relation `[s₁₃, s₂₄] = 0`

Lean: `RationalAssociator/TransportedDK4.lean`, no `sorry`. Scripts:
`computations/rational_associator/grt_far_relation/`.

**Decision.** The pentagon of `g` alone does not force the far relation. Adding (5.13) does not
force it either. The evidence, exact over ℚ:

- Give `g` the degree-2 part `[X, Y]`. That part satisfies the pentagon to its order and also
  `g(X,Y) g(Y,X) = 1`.
- Then the degree-4 part of `[s₁₃, s₂₄]` is not in the degree-4 Drinfeld–Kohno ideal of the free
  algebra: 995 relations against 1296 words, so `dim U(𝔱₄)₄ = 301`, and the reduction leaves a
  nonzero residual.
- That degree-4 part depends only on the degree-2 part of `g`.
- Drinfeld associators with `μ ≠ 0` satisfy the pentagon and (5.13) and have exactly this kind of
  degree-2 part (Drinfeld 1991, Prop. 5.3 and Thm. A). So they are counterexamples.

The μ = 0 hexagon (5.14) of `GRT` excludes a degree-2 part. Evidence that GRT is enough:

- In degree 3, the only Lie direction satisfying the pentagon is `σ₃ = [X,[X,Y]] + [Y,[X,Y]]`.
- For `σ₃`, `[s₁₃, s₂₄]₅` lies in the ideal; for the other three directions tested it does not.
- This was checked modulo two primes, not over ℚ, and it covers the leading order only.
- So it is evidence that (5.14) is what makes `hfar` hold. It is not a proof.

**Proved in Lean.**

- `dk4_of_locals`: ten bracketing-local commutations plus `[s₁₃, s₂₄] = 0` imply `DK4`. The
  degree-2 rank count supports this: the locals span 10, and adding the far relation gives 11.
- `transported_dk4`: given the pentagon of `g` and `hfar`, the transported family (with
  `s₁₄ = t₁₄+t₂₄+t₃₄ − s₂₄ − s₃₄`) is a `DK4` family.
- Nilpotence: in `U4 N`, a word of length `N` in elements of `Fil N 1` vanishes. Every `sᵢⱼ`
  lies in `Fil N 1`.
- `pentagon_act_universal`: in `U4 N`, the pentagons of `φ` and `g` together with `hfar` imply
  the pentagon of `φ̃`. It is obtained through `lift`.

**Still open (bean `qou-3fdg`).**

1. Derive `hfar` in Lean from the hexagon (5.14), and (5.13) if needed. Reduced in §6 to the
   t-compatibility identity `TCompat`; deriving `TCompat` from (5.14) is what remains.
2. The five units `G` remain hypotheses. They exist whenever `g` has constant term 1, because
   `Fil N 1` is nilpotent, but that is not yet written in Lean.

## 6. Stage 3d: the far relation reduced to t-compatibility

Lean: `RationalAssociator/FarRelation.lean`, no `sorry`, axioms `propext`, `Classical.choice`,
`Quot.sound`. Script: `computations/rational_associator/grt_far_relation/t3.py`.

**The bridge.** For a three-strand family `(u, v, w) = (t_ab, t_ac, t_bc)`, t-compatibility of `g`
(`TCompat`) is

    g(v,w) · v · g(v,w)⁻¹ = g(u,w) · (v + w) · g(u,w)⁻¹ − w,

equivalently `g(v,w) v g(v,w)⁻¹ + g(u,w) u g(u,w)⁻¹ + w = u + v + w`, because `u + v + w` is
central in `U(𝔱₃)`.

**Proved in Lean.** `far_of_tcompat` derives `hfar : [s₁₃, s₂₄] = 0` in any `ℚ`-algebra from:

- `TCompat` at `(t₁₂, t₁₃, t₂₃)`, which gives `s₁₃ = Y⁻¹ t₁₃ Y` with `Y = g(t₁₃,t₂₃)⁻¹ g(t₁₂,t₂₃)`;
- `TCompat` at `(t₃₄, t₂₄, t₂₃)`, together with (5.13) at `(t₃₄, t₂₃)` and `(t₂₄, t₂₃)`, which
  gives `s₂₄ = (H·G_d·G_a)⁻¹ t₂₄ (H·G_d·G_a)` with `H = g(t₂₃,t₂₄)`;
- the pentagon of `g` at the 2↔3-relabelled family, which gives `H·G_d·g(t₁₃,t₂₃) = M·W` with
  `M = g(t₁₃, t₂₃+t₃₄)` commuting with `t₂₄` and `W = g(t₁₂+t₂₃, t₂₄)` commuting with `t₁₃`.

So `s₂₄ = Y⁻¹ (W⁻¹ t₂₄ W) Y`, `s₁₃ = Y⁻¹ (W⁻¹ t₁₃ W) Y`, and `[t₁₃, t₂₄] = 0` conjugates to
`hfar`. In `U4 N` the relabelled pentagon is not an extra hypothesis: `pentagon_swap23` gets it
as the image of the pentagon under the relabelling automorphism `swap23Hom = lift N (t ∘ π)`.
`pentagon_act_universal_of_tcompat` is `pentagon_act_universal` with `hfar` replaced by the two
`TCompat` and two (5.13) instances.

**Exact over ℚ (`t3.py`).**

- `TCompat` holds for `g = exp(σ₃)` through degree 5 and fails for `g = exp([X,Y])`.
- Among degree-3 directions `a·[X,[X,Y]] + b·[Y,[X,Y]]`, only `(1,1) = σ₃` satisfies `TCompat`;
  (5.13) selects the same direction.
- (5.14) excludes a degree-2 part. So through degree 3 of `g`, (5.13) and (5.14) imply `TCompat`.

**The obstruction that remains.** `TCompat` is a hypothesis in Lean. A derivation of `TCompat` from
(5.13) and (5.14) for all degrees is not given here; only the degree-3 check above is established.
The statement is of the Kashiwara–Vergne type (`grt ⊂ krv` in Alekseev–Torossian); whether that
inclusion supplies it in this form has not been checked against the library. Bean `qou-3fdg` stays
open on this point and on the existence of the units `G`.
