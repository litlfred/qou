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
*(Corrected in §9: `TCompat` is Drinfeld's own (5.14), one of the defining conditions of `GRT₁`.
It is not a consequence to be derived, and the Kashiwara–Vergne framing given here was wrong.)* Bean `qou-3fdg` stays
open on this point and on the existence of the units `G`.

## 7. Stage 3e: the GRT action preserves the hexagon

Lean: `RationalAssociator/HexagonAction.lean`, no `sorry`, axioms `propext`, `Classical.choice`,
`Quot.sound`. Script: `computations/rational_associator/grt_far_relation/hexagon_act.py`.

**The hexagon.** This is the repo's form (`LowDegree.lean`), with the exponential `E` an arbitrary
one-variable polynomial:

    E(t₁₃+t₂₃) = φ(t₁₃,t₁₂) E(t₁₃) φ(t₂₃,t₁₃) E(t₂₃) φ(t₁₂,t₂₃).

`hexagon_expHalfPoly_iff` recovers the degree-3 truncated form of `LowDegree.lean`.

**The route.** Write `G₁ = g(t₁₃,t₁₂)`, `G₂ = g(t₂₃,t₁₃)`, `G₃ = g(t₁₂,t₂₃)`. Transport `t` to
`s = (t₁₂, G₁ t₁₃ G₁⁻¹, G₃⁻¹ t₂₃ G₃)`. Two facts drive the proof:

- (5.14), in the form `G₂ G₃ G₁ = 1`, makes `Z = G₂G₃ = G₁⁻¹` conjugate the pair
  `(G₂ t₂₃ G₂⁻¹, t₁₃)` to `(s₂₃, s₁₃)`.
- `s₁₃ + s₂₃ = t₁₃ + t₂₃`. This follows from `DK3`, from (5.13) at `(t₂₃,t₁₂)`, and from one
  `TCompat` instance at `(u,v,w) = (t₂₃,t₁₃,t₁₂)`.

Then the factors map as follows, and the product telescopes:

- `φ(s₁₃,s₁₂) = φ̃(t₁₃,t₁₂) G₁⁻¹`
- `E(s₁₃) = G₁ E(t₁₃) G₁⁻¹`
- `φ(s₂₃,s₁₃) = G₁ φ̃(t₂₃,t₁₃) G₃`
- `E(s₂₃) = G₃⁻¹ E(t₂₃) G₃`
- `φ(s₁₂,s₂₃) = G₃⁻¹ φ̃(t₁₂,t₂₃)`

**Proved in Lean.**

- `hexagon_act_of_transport` and `hexagon_act` give the instance form: the hexagon of `φ` at `s`
  implies the hexagon of `φ̃` at `t`.
- `transported3_dk3` shows that `s` is again a `DK3` family.
- `hexagon_act_all`: if `φ` satisfies the hexagon at every `DK3` family of `R`, then `φ̃`
  satisfies it at every `DK3` family at which `g` satisfies (5.13), (5.14) and `TCompat`.
- No truncation enters any of these statements. Unlike the pentagon (§5–6), no far-relation
  issue arises, because a `DK3` family only asks each generator to commute with the total.

**Exact over ℚ (`hexagon_act.py`, through degree 5).**

- Take `φ` solving the hexagon with degree-2 part `[X,Y]/24`, and `g = exp(σ₃)`. Then the
  hexagon of `φ̃` holds, and so do both transport identities.
- With `g = exp([X,Y])`, all three fail.

**What remains as hypotheses.** These are the same as for the pentagon: `TCompat` (one instance
here), and the existence of the units `G`.

## 8. Stage 3d: units discharged; what Exp has to be

Lean: `RationalAssociator/NilpotentUnits.lean`, no `sorry`, axioms `propext`, `Classical.choice`,
`Quot.sound`.

**(a) Units, closed.**

- `NilIdeal S`: a ℚ-submodule `S` that is a two-sided ideal of nilpotent elements.
- `eval_sub_mem`: for `a, b ∈ S`, `eval a b p − ε(p) ∈ S`, where `ε` is the constant term
  `FreeAlgebra.algebraMapInv`.
- `evalUnit`: when `ε(g) = 1`, `eval a b g = 1 + (nilpotent)` is a unit (`IsNilpotent.isUnit_one_add`).
- `nilIdeal_Fil`: in `U4 N`, `x ∈ Fil N 1` gives `xᴺ ∈ Fil N N = 0`, so `Fil N 1` is such an ideal.
- `pentagon_act_U4` and `hexagon_act_U4` restate the action theorems in `U4 N`. Every `G` is
  `gU N hg1 l m = g(Σ_l t, Σ_m t)`. The hypotheses left on `g` are:
  - `ε(g) = 1`;
  - its pentagon;
  - (5.13), and (5.14) for the hexagon;
  - `TCompat`.

**A caveat on `hexagon_act_all` (§7).** Its hypothesis quantifies over *every* `DK3` family of
`R`. That includes non-nilpotent families, where a truncated exponential `E` does not satisfy the
hexagon. So for `R = U4 N` that hypothesis is not expected to hold for a genuine associator.
`hexagon_act_U4` avoids this: it takes the hexagon of `φ` at the transported family. To discharge
that hypothesis from the universal hexagon, one needs a 3-strand universal algebra `U3 N` with
`lift`, or the quantifier restricted to families in a `NilIdeal`. Neither is written yet.

**(b) Exp: the top-degree statement alone does not serve stage 4.** Stage 4 (bean `qou-3fdg`)
takes a `K`-associator `Φ` with `Φ_{≤N}` rational and `y ∈ grt_{N+1}(K)`. It needs an associator
`Φ'` with `Φ' ≡ Φ + y` modulo degree `N + 2`. The induction then continues from `Φ'`, so `Φ'` must
be an associator in every degree, or at least in every truncation `U4 M` for arbitrarily large
`M`.

- Modulo degree `N + 2`, `g = 1 + y` satisfies the `GRT₁` equations exactly when `y ∈ grt`, since
  those conditions are linear in the top degree. So `Φ ∘ (1 + y)` is an associator only mod
  degree `N + 2`, and nothing says it lifts.
- What stage 4 needs is the existence of `g ∈ GRT₁(K)`, in all degrees, with `g ≡ 1 + y` mod
  degree `N + 2`. This is the surjectivity of `GRT₁ → grt` on top-degree pieces. It is smaller
  than a full exponential map with group-law properties, but it is not a truncation statement.
- The congruence `Φ ∘ g ≡ Φ + y` mod degree `N + 2` for such `g` is easy, and it is not the
  bottleneck.
- The naive series `exp(ψ)` is not the required `g`. Exact check over ℚ in `U(𝔱₃)` (`t3.py`
  functions): `exp(σ₃)` satisfies (5.13) and `TCompat` through degree 6, but **fails (5.14) at
  degree 6**. `Exp` must use the `GRT₁` group law `g₁ ∘ g₂ = g₁(g₂ A g₂⁻¹, B)·g₂`, not the
  product of series. Equivalently, `g` is built degree by degree, and each step needs an
  obstruction to vanish.

The degree-by-degree construction of `g ∈ GRT₁` with prescribed leading term (Drinfeld §5,
(5.17)–(5.20); Ihara) is not attempted here. It is the next blocker for stage 4.

## 9. The stage-4 blocker: Exp for the group law (5.16)

Lean: `RationalAssociator/HexagonUniversal.lean`, no `sorry`, axioms `propext`,
`Classical.choice`, `Quot.sound`. Script: `computations/rational_associator/grt_far_relation/exp516.py`.

**Numbering correction (read first).** Drinfeld (1991, §5, `library/drinfeld1991-quasitriangular`,
page 12) defines `GRT₁` by four conditions:

| Drinfeld | condition | name in this repo until now |
|---|---|---|
| (5.12) | `g(B,A) = g(A,B)⁻¹` | "(5.13)" |
| (5.13) | `g(C,A) g(B,C) g(A,B) = 1` for `A+B+C = 0` | "(5.14)", "the μ = 0 hexagon" |
| (5.14) | `A + g(A,B)⁻¹Bg(A,B) + g(A,C)⁻¹Cg(A,C) = 0` for `A+B+C = 0` | `TCompat` |
| (5.15) | the pentagon | pentagon |

So `TCompat` is one of the defining conditions of `GRT₁`. The question in §6 of deriving it from
"(5.14)" was the wrong question, and the Kashiwara–Vergne remark there is withdrawn. Every action
theorem so far assumes exactly the `GRT₁` conditions on `g`, plus `ε(g) = 1`, and nothing more.

**1. The (5.16)-exponential, exact over ℚ.**

- Under (5.16), `θ_g : A ↦ gAg⁻¹, B ↦ B` satisfies `θ_{g₁∘g₂} = θ_{g₂} ∘ θ_{g₁}`.
- A one-parameter subgroup `g_s` with leading term `sψ` therefore solves the linear equation
  `g' = D_ψ(g) + gψ`, where `D_ψ(A) = [ψ, A]` and `D_ψ(B) = 0`.
- Its solution is `Exp(ψ) = Σ_k L^k(1)/k!` with `L(x) = D_ψ(x) + xψ`. The sum is finite in each
  truncation.
- `exp516.py` checks (5.12)–(5.15) exactly, using a normal form of `U(𝔱₄)`:
  - `Exp(σ₃)` satisfies all four through degree 8.
  - Ordinary `exp(σ₃)` fails (5.13) and (5.15) at degree 6, and (5.14) at degree 7.
  - `Exp([X,[X,Y]])`, which is not in `grt`, fails (5.12) and (5.15) at degree 3.

  This agrees with Drinfeld's Prop. 5.9.

**2. The smallest statement stage 4 needs.**

> (S4) For `y ∈ grt₁(K)` homogeneous of degree `n`, there is `g ∈ GRT₁(K)`, satisfying
> (5.12)–(5.15) in every degree, with `g ≡ 1 + y` modulo degree `n + 1`.

Given (S4), `Φ ∘ g` is again a `K`-associator. That uses the action theorems:
- `pentagon_act_U4` and `hexagon_act_U4_universal` in each truncation `U4 M`;
- the lift from `U4 M` to every truncated `DK` family.

Also `Φ ∘ g ≡ Φ + y` modulo degree `n + 1`. That congruence is elementary and not yet in Lean.

(S4) is weaker than a full exponential map: it asks for no group-law properties of `Exp`, only
that `GRT₁(K)` mod degree `n+1` surjects onto `grt_n(K)`. Two routes, neither formalised:

- **Route A, flow.** Take `g = Exp(y)`. For each condition `C`, the defect `C(g_s)` satisfies a
  linear equation in `s`:
  - the closure theorems give how `C` transforms under `g ↦ g ∘ (1 + εy)`;
  - `y ∈ grt` makes the inhomogeneous term vanish.

  Then `C(g_s) = 0`, because the solution of a linear equation in a graded nilpotent setting is
  unique. The closure ingredients are the action theorems at `μ = 0` (`φ := g₁`, `E := 1`); the
  pentagon and hexagon cases are now in Lean. Still missing: (5.12) and (5.14) for the composite,
  and the derivative computation.
- **Route B, degree by degree.** Extend `g ∈ GRT₁` mod degree `m` to mod degree `m+1`. The
  obstruction is a cohomology class, and nothing elementary shows that it vanishes. Route A
  avoids this, so it is the one to formalise.

**3. Proved in Lean now.**

- `DK3.toDK4`: a `DK3` family `(a,b,c)` extends to the `DK4` family `(a,b,0,c,0,0)`.
- `hexagon_of_universal`: the hexagon at the universal family of `U4 N` gives the hexagon at
  every `DK3` family in `Fil N 1`, via `lift`.
- `hexagon_act_U4_universal`: the hexagon action theorem with `φ`'s hexagon assumed only at the
  universal family. This removes the caveat of §8, and no `U3 N` is needed.
- With `φ := g₁` and `E := 1`, the pentagon and hexagon (5.13) of `g₁ ∘ g₂` follow from those of
  `g₁` and the `GRT₁` conditions of `g₂`. These are two of the four closure statements Route A
  needs.

**4. Closure of (5.12) and (5.14) under (5.16), now proved** (`GRTClosure.lean`, sorry-free,
axioms `propext`, `Classical.choice`, `Quot.sound`). The setting is a nil ideal `S` of a
`ℚ`-algebra `R`. Write `compEval g₁ g₂ a b := g₁(G a G', b)·G` with `G = g₂(a,b)` and
`G' = g₂(b,a)`.

- `comp_inv512`: if `g₁` and `g₂` satisfy (5.12) on `S`, then
  `compEval(a,b)·compEval(b,a) = 1` for all `a, b ∈ S`.
- `comp_tcompat`: suppose `g₂` satisfies (5.12) on `S`, and `g₁`, `g₂` satisfy (5.14) at every
  `DK3` family in `S`. Then the composite satisfies (5.14) at every `DK3` family in `S`.
  - The proof: the transported family `(G_u u G_u', G_v v G_v', w)` is again `DK3`, because
    `u+v+w` commutes with every `G`.
  - So `g₁`'s (5.14) applies there. `g₁`'s (5.12) is not needed.
- `tcompat_iff_poly`: equates the unit form `TCompat` of §6 with the polynomial form used here,
  given (5.12) at the pairs.
- `compEval_eq_actEval`: identifies `compEval` with `actEval` of §7.

Together with the pentagon and hexagon cases above, all four conditions are closed under
(5.16) at the level of evaluations. Every hypothesis is a named argument.

**5. The composite as a polynomial; `GRT₁` closed in `U4 N`** (`GRTComposite.lean`, sorry-free,
axioms `propext`, `Classical.choice`, `Quot.sound`).

- `compPoly g₁ g₂ = g₁(g₂·A·g₂(B,A), B)·g₂` is (5.16) with the inverse written through (5.12).
  `eval_compPoly` (no hypotheses): `eval a b (compPoly g₁ g₂) = compEval g₁ g₂ a b`.
- `algebraMapInv_compPoly`: the constant term of `compPoly g₁ g₂` is `ε(g₁)·ε(g₂)`.
- `pentagon_compPoly_U4` and `hexagon_compPoly_U4` (any `E`): the pentagon and hexagon of the
  composite at the universal family, from those of `g₁` and the conditions on `g₂`.
- `structure GRT1U4 N g` packages:
  - the constant term `1`;
  - (5.12) and (5.14) on all of `Fil N 1`;
  - (5.13), the `E = 1` hexagon, at the universal family;
  - (5.15) at the universal family.

  `grt1U4_comp`: `GRT1U4 N` is closed under `compPoly`.

## 10. Stage 4, the flow argument settled on paper (handoff)

**Goal (S4).** For `y` homogeneous of degree `n` in `grt` (the linearised (5.12)–(5.15) hold
for `y`), `Exp(y) := Σ_k L_y^k(1)/k!` satisfies `GRT1U4 N` for every `N`, with
`L_y(z) = D_y(z) + z·y`, `D_y(A) = [y,A]`, `D_y(B) = 0`.

**Discrete argument (no derivatives).** Write `C` for any one of the four conditions and
`δ_C(g) = LHS − RHS ∈ U4 N`. Each step is first a statement on paper; none is in Lean yet.

- **(G) Grading.**
  - `L_{xy} = x·L_y` for `x ∈ ℚ`, so `Exp(xy) = Σ_k x^k e_k`, with `e_k = L_y^k(1)/k!`
    homogeneous of degree `kn`.
  - Each condition is homogeneous in the `t`'s, with `e_C` explicit `t` factors per term:
    `e_C = 0` for (5.12), (5.13), (5.15), and `e_C = 1` for (5.14).
  - Hence the degree-`d` component of `δ_C(Exp(xy))` is a monomial `c_{C,d}·x^{(d−e_C)/n}`, and
    it is zero when `n ∤ d − e_C`.
- **(A) Top-defect additivity.** Suppose all defects of `g₁` and `g₂` lie in `Fil N d`. Then
  `δ_C(g₁∘g₂) ≡ δ_C(g₁) + δ_C(g₂) (mod Fil N (d+1))`.
  - Proof idea: rerun the closure proofs of §9.4–§9.5 with each hypothesis replaced by
    "equation + error in `Fil N d`".
  - Errors in `Fil N d` multiply with `Fil N 1` into `Fil N (d+1)`. The unit factors are
    `≡ 1 (mod Fil N 1)`.
  - So each error enters additively. Conjugation by a unit fixes it modulo `Fil N (d+1)`.
- **(P) One-parameter law.** `Exp(sy) ∘ Exp(ty) = Exp((s+t)y)`, in particular `s = t`.
  - Exact over ℚ through degree 9 for `y = σ₃` and for `y = [X,[X,Y]]`
    (`exp516_oneparam.py`). Not proved.
  - A proof is ODE uniqueness in disguise. Both sides `F` satisfy
    `F(x + x') = F(x) ∘ Exp(x'y)`, whose `x'`-linear part is `L_y`.
  - Discrete form to try: compare `x`-coefficients. Both sides have `F_0 = 1` and
    `(k+1)F_{k+1} = L_y(F_k)`. The left side needs the coefficient of `x'^1` in
    `g ∘ Exp(x'y)`, which is `L_y(g)`. This is a polynomial identity in `x'`, read off from the
    definition of `compPoly`.

**The induction.** Let `d₀` be the lowest degree of any defect of `Exp(xy)`, and suppose
`d₀ < ∞`. Set `P(x) = c x^m` with `m = (d₀ − e_C)/n`.

1. By (P), `Exp(2xy) = Exp(xy) ∘ Exp(xy)`. By (A), `P(2x) = 2P(x)`, so `c(2^m − 2) = 0`.
2. If `m ≠ 1`, then `c = 0`.
3. If `m = 1`, then `c` is the `x`-linear part of `δ_C(Exp(xy)) = δ_C(1 + xy + O(x²))`. That is
   the linearised condition at `y`, which vanishes because `y ∈ grt`.
4. So every degree-`d₀` defect vanishes, contradicting the choice of `d₀`.
5. Hence `Exp(y) ∈ GRT1U4 N`, and `Exp(y) ≡ 1 + y (mod degree n+1)`.

**Order for a fresh agent.**
1. Define `ExpPoly y N` in Lean as `Σ_{k≤N} L^k(1)/k!`. `L` is a ℚ-linear map; `D_y` is a
   derivation, built via `FreeAlgebra.lift` to `ℚ⟨A,B⟩ ⋊ ε`, or by words.
2. Prove (G).
3. Prove (P) by the coefficient recursion.
4. Prove (A) by error-carrying copies of `comp_inv512`, `comp_tcompat` and the action
   theorems. This is the bulk.
5. Run the induction.
6. Separately, prove the congruence `Φ ∘ g ≡ Φ + y`.

The linearised conditions defining `grt` need a Lean definition matching step 3 of the
induction. No `grt` predicate exists in the repo yet.

**Still open (bean `qou-3fdg`):** (G), (A), (P), the induction, the `grt` predicate and
`Φ ∘ g ≡ Φ + y`.

## 11. Stage 4: the exponential, `grt`, and the induction in Lean (doubling hypothesis open)

Lean: `RationalAssociator/GRTFlow.lean`, no `sorry`, axioms `propext`, `Classical.choice`,
`Quot.sound` (checked with `#print axioms` on `grt1U4_expPoly_of_doubling` and
`coeff_mem_of_doubling`; `lean -DautoImplicit=false -s 65536`, exit 0).

**Proved.**

- `leibD d`: the Leibniz map of `ℚ⟨A,B⟩` with prescribed values on `A, B`, built as the upper-right
  entry of an algebra map into upper-triangular `2×2` matrices. Leibniz rule, linearity, scaling
  `leibD (x•d) = x • leibD d`, and `ε ∘ leibD = 0`.
- `Ly y z = D_y z + z·y` with `D_y(A) = [y,A]`, `D_y(B) = 0`; `expTerm y k = L_y^k(1)/k!`;
  `expPoly y K = Σ_{k<K} expTerm y k`.
- `expTerm_smul`: `expTerm (x•y) k = x^k • expTerm y k`, so `Exp(xy) = Σ_k x^k e_k` exactly. With
  `expTerm_zero = 1`, `expTerm_one = y`, and `ε(Exp(y)) = 1` when `ε(y) = 0`.
- **(G) is not needed.** `coeff_mem_of_doubling`: in a `ℚ`-module, if
  `Σ_j (2^j − 2) x^j c_j ∈ F` for every `x ∈ ℚ`, then `c_j ∈ F` for `j ≠ 1` (dual functionals on
  `M ⧸ F` and a polynomial vanishing on all of `ℚ`). So the induction runs on the filtration
  `Fil N d` alone, with no grading of `U4 N` and no homogeneity assumption on `y`.
- `eval_eq_zero_of_doubling`: the induction of §10, for any family of polynomials in `x` over a
  `ℚ`-algebra with a filtration `F 0 = R ⊇ … ⊇ F N = 0`.
- `GrtU4 N y`: the `x`-linear parts of the four `GRT1U4 N` conditions, i.e. Drinfeld (5.17),
  (5.18) and (5.20) at the universal family, and the linearisation of (5.14) in the polynomial
  form `TCompatPoly`: `y(v,w) v + v y(w,v) = y(u,w)(v+w) + (v+w) y(w,u)` for `DK3` triples. Given
  (5.17) this is `[y(v,w), v] = [y(u,w), v+w]`; matching it to Drinfeld's (5.19) literally is a
  paper step, not formalised (Prop. 5.7 makes (5.19) redundant anyway).
- `defectPoly y K i`: the defect of each condition instance for `Exp(xy)` as a polynomial in `x`
  over `U4 N`; `coeff_one_defectPoly`: its `x`-linear coefficient is the `GrtU4` expression, so it
  vanishes for `y ∈ grt` (step 3 of §10).
- `grt1U4_expPoly_of_doubling` (**conditional**): `GrtU4 N y`, `K ≥ 2` and the doubling
  hypothesis `hdouble` give `GRT1U4 N (expPoly (x•y) K)` for every `x ∈ ℚ`. `hdouble` says: if
  every defect of `Exp(xy)` lies in `Fil N d` for all `x`, then
  `δ(Exp(2xy)) − 2 δ(Exp(xy)) ∈ Fil N (d+1)`. It is a named argument, not an axiom.

**Still open (bean `qou-3fdg`).** The doubling hypothesis, which is (P) and (A) of §10 together:

- **(P)** `Exp(2xy) = Exp(xy) ∘ Exp(xy)` in `U4 N`. Trap: `compPoly` writes the inverse through
  (5.12), so (P) in `compPoly` form already presupposes (5.12) for `Exp(xy)`. State (P) with the
  genuine inverse (`actEval` with a unit), or show `compPoly` and the unit form differ only in
  `Fil N (d+1)` when the (5.12) defect is in `Fil N d` (true: the error is multiplied by a `t`).
  The coefficient recursion of §10 needs `d/dx' (G ∘ Exp(x'y))|₀ = L_y(G)` as a polynomial identity,
  i.e. a chain rule for substituting `G A G⁻¹` into `G`. Not attempted.
- **(A)** top-defect additivity: error-carrying copies of `comp_inv512`, `comp_tcompat`,
  `pentagon_act_U4` and `hexagon_act_U4_universal`. Not attempted; it is the bulk.
- The congruence `Φ ∘ g ≡ Φ + y` (§9.2) is still not in Lean.

## 12. Stage 4 closed: `Exp(xy) ∈ GRT₁` for `y ∈ grt`, with the bound `N ≤ K`

Lean: `RationalAssociator/GRTValued.lean` and `RationalAssociator/GRTFlowExact.lean`. Neither has a
`sorry`. Checked with `lean -DautoImplicit=false -s 65536`, exit 0. `#print axioms` gives
`propext`, `Classical.choice` and `Quot.sound` for `grt1U4_expPoly`, `hdouble_of_le` and
`grt1U4_expPoly_via_doubling`; the check ran in a scratch copy.

**Result.** `grt1U4_expPoly (hy : GrtU4 N y) (hK : 2 ≤ K) (hNK : N ≤ K) (x : ℚ) :
GRT1U4 N (expPoly (x • y) K)` holds unconditionally. `hdouble_of_le` proves the hypothesis
`hdouble` of `grt1U4_expPoly_of_doubling` under the same bounds, so the §11 statement is also
closed through its own route (`grt1U4_expPoly_via_doubling`).

**The extra hypothesis `N ≤ K` is needed.** With only `2 ≤ K`, `expPoly (x•y) K` is a truncation
of the exponential, not the exponential. Example: take `K = 2`, so `G = 1 + xy`. Then `(5.12)`
fails at order `x²`, because of the term `y(a,b)·y(b,a)`. This argument was worked by hand and is
**not machine-checked**. With `K ≥ N`, every term `e_k(a,b)` with `k ≥ K` already vanishes in
`U4 N`, since it lies in `Fil N k` (`eval_expTerm_eq_zero`). So the truncation is exact.

**Route: an exact flow in dual numbers, not doubling.** Neither (P) nor (A) of §10–§11 was proved.
The proof goes around both.

- Work in `D = DualNumber (U4 N)`. `Hh y a b = 1 + ε·y(a,b)` is a unit, by (5.17).
- **The flow identity** `evD_EP`: evaluating `Exp(xy)` at `x + ε` equals `actEval` of `Exp(xy)` by
  `Hh`. Its inputs:
  - the Leibniz chain rule;
  - `L_y(e_k) = (k+1) e_{k+1}`;
  - the exactness `e_K = 0` from `N ≤ K`.

  This identity is the exact replacement for (P).
- **Value-function action theorems** (`GRTValued.lean`). These are the action theorems of §4–§8,
  restated for a value function `γ` and a defect, not for a single element:
  - `inv_actV`;
  - `tc_actV`;
  - `hexagon_actV`;
  - `pentagon_actV`, with `far_of_tcompatV` and `transported_dk4V`.

  Each one shows that a defect of `φ ∘ γ` equals a unit times the same defect of `φ` at a
  transported family. They replace (A): additivity is never needed, because the identity is exact.
- **The `GoodAt` filtration.** `GoodAt d z` means `fst z ∈ Fil d` and `snd z ∈ Fil (d+1)`.
  `goodAt_liftD` says that an algebra map `U4 N → D` with generator values `GoodAt 1` sends `Fil d`
  into `GoodAt d`. The theorems `goodAt_inv`, `goodAt_tc`, `goodAt_hex` and `goodAt_pent` then
  show: if a defect at `x` lies in `Fil d`, the defect at `x + ε` is `GoodAt d`.
- **The induction** `evq_eq_zero_of_flow`. The `ε`-part of the defect at `x + ε` is
  `Σ_j j x^{j−1} P_j`. If it lies in `Fil (d+1)` for every `x`, then every `P_j ∈ Fil (d+1)`,
  using `P_0 = 0` (`coeff_zero_defectPoly`). Hence `P ∈ Fil N = 0`.
- **Transfer.** The universal defects are carried to arbitrary pairs and `DK3` triples by
  `liftU3`, the lift extended by zeros.

**Still open.**
- Nothing in the `hdouble` / Stage-4 item.
- The congruence `Φ ∘ g ≡ Φ + y` (§9.2) is still not in Lean.
- Matching the polynomial form of `GrtU4`'s t-compatibility to Drinfeld's (5.19) is still a paper
  step, as stated in §11.

## 13. The induction step: what is proved, and what still blocks it

Lean: `RationalAssociator/AssociatorInduction.lean`. No `sorry`. Checked with
`lean -DautoImplicit=false -s 65536`, exit 0. `#print axioms` gives `propext`, `Classical.choice`
and `Quot.sound` for every theorem named below; the check ran in a scratch copy inside the tree,
since deleted.

**1. The congruence `Φ ∘ g ≡ Φ + y` (§9.2), proved.**

- `compPoly_congr`: if `ε(Φ) = 1`, `y ∈ FF n` and `g − 1 − y ∈ FF (n+1)`, then
  `compPoly Φ g − (Φ + y) ∈ FF (n+1)`. No hypothesis on `n`.
- `expPoly_congr`: for `y ∈ FF n`, `n ≥ 1`, `K ≥ 2`, `Exp(y) − 1 − y ∈ FF (n+1)`. It uses the
  sharper bound `expTerm y k ∈ FF (k·n)` (`expTerm_mem_FF_mul`).
- `compPoly_expPoly_congr` combines the two.

**2. The `GRT₁(ℚ)` shift of an associator in `U4 N`, proved.**

- `AssocU4 N E Φ`: constant term `1`, (5.12) on `Fil N 1`, the hexagon with exponential `E` at the
  universal three-strand family, the pentagon at the universal four-strand family.
- `assocU4_compPoly`: `GRT1U4 N g` and `AssocU4 N E Φ` give `AssocU4 N E (compPoly Φ g)`.
- `assocU4_shift`: for `GrtU4 N y`, `y ∈ FF n`, `n ≥ 1`, `2 ≤ K`, `N ≤ K`, the element
  `Φ ∘ Exp(y)` is again an associator in `U4 N`, and it is `≡ Φ + y (mod FF (n+1))`.

**3. The descent step, proved conditional on a named hypothesis.**

- `assocU4_add_iff`: for `ε(Φ) = ε(E) = 1`, `d ≥ 1`, `x ∈ FF d`, the element `Φ + x` is an
  associator in `U4 (d+1)` iff `assocLin x = −assocDefect Φ`. `assocLin` is (5.17), (5.18), (5.20)
  in `U4 (d+1)`; `assocDefect Φ` is the vector of defects of `Φ` there. The proof is
  `Linearization.lean` with `I = Fil 1`, `J = Fil d`.
- `SolvableOver K d E Φ` (named hypothesis): the base change to `K` of this system has a
  solution.
- `exists_rational_lift`: `SolvableOver K d E Φ` for some nontrivial `ℚ`-algebra `K` gives
  `x ∈ FF d` with `Φ + x` an associator in `U4 (d+1)`. Proof: `exists_of_baseChange`.
- `solvableOver_of_lift`: conversely, such a rational `x` gives `SolvableOver K d E Φ` for every
  `K`. So the hypothesis is exactly what the step needs, not a stronger assumption.

So "associator mod degree `d` over `ℚ` ⟹ associator mod degree `d+1` over `ℚ`" is proved, under
`SolvableOver K d E Φ`. It does not use that `Φ` is an associator mod `d`, because the hypothesis
already contains that information.

**4. (5.19), proved on zero-sum triples.**

- `lin514_iff_drinfeld519`: on a triple `(u, v, w)` with `u + v + w = 0`, given (5.17) at
  `(v, w)` and `(u, w)`, the `lin514` field of `GrtU4` is Drinfeld's (5.19) at
  `(A, B, C) = (w, v, u)`.
- `drinfeld519_of_grtU4`: `GrtU4 N y` gives (5.19) at every pair `A, B ∈ Fil N 1`, with
  `C = −A − B`.
- `lin514_of_drinfeld519`: (5.17) and (5.19) give `lin514` at every zero-sum triple of `Fil N 1`.
- Not covered: `lin514` at a `DK3` triple whose central sum `c = u + v + w` is nonzero. Matching
  it to (5.19) needs `y(a + c, b) = y(a, b)` for central `c`. That holds for Lie elements, and
  `GrtU4` does not ask that `y` be Lie.

**What blocks the full induction.** The hypothesis `SolvableOver K d E Φ` holds when `Φ` is the
truncation of a `K`-associator. Drinfeld's argument (Prop. 5.8) keeps that true from one degree
to the next. It shifts the `K`-associator `Φ_K` by `Exp(y)` with `y = ψ − (Φ_K)_d`, where `ψ` is
the rational solution. Item 2 does this shift, but only over `ℚ`. Three things are missing over `K`:

- **(B1) Coefficients in `K`.** `eval`, `U4`, `Fil`, `GrtU4`, `GRT1U4`, `expPoly` and every
  action theorem are stated for `FreeAlgebra ℚ (Fin 2)`. Here `y` has coefficients in `K`.
  - One way round: write `y = Σ cᵢ yᵢ` with `yᵢ ∈ grt(ℚ)`, `cᵢ ∈ K`. Then `defectPoly yᵢ K i`
    vanishes at every `x ∈ ℚ`, so it is the zero polynomial, and it can be evaluated at
    `cᵢ ∈ K`.
  - This still needs every evaluation and action theorem in `K ⊗[ℚ] U4 N`. That is not written.
- **(B2) The linearised (5.14) for `y`.** `y` satisfies the linearised (5.12), (5.13) and (5.15),
  because both `ψ` and `(Φ_K)_d` solve the same linear system. `GrtU4` also asks for `lin514`.
  - Drinfeld's Prop. 5.7 gives it, but only for Lie `y`. Its proof needs the symmetric-Lie-
    polynomial lemma (`s(B, C)` symmetric with (5.24) forces `s = 0`).
  - The repository has no Lie or group-like structure on associators.
- **(B3) Homogeneity.** The linearised conditions on `y` hold in `U4 (d+1)`, but `assocU4_shift`
  needs them in `U4 M` for every `M`. For homogeneous `y` of degree `d` this follows if the
  degree-`d` part of `U4 M` maps isomorphically to that of `U4 (d+1)`. There is no grading on
  `U4` in Lean.

There is also a missing bridge (B0): a `K`-associator `Φ_K ≡ Φ (mod FF d)` gives
`SolvableOver K d E Φ`. This is the linearisation lemma applied in `K ⊗[ℚ] U4 (d+1)`, and it is
not written either. So the named hypothesis is the base-changed linear system, and is stated as
that. It is not literally "a `K`-associator exists".

**Order for the next agent.** (B0) and (B1) are the same piece of work: base change of `eval`,
`Fil` and the four action theorems to `K ⊗[ℚ] U4 N`. Then (B3), then (B2). (B2) is the
mathematically substantive one.

**Still open (bean `qou-3fdg`).** (B0)–(B3). Nothing else in Stage 4 is open.

## 14. (B0) and (B3) closed; (B1) not done

Branch `claude/grt-basechange-2026-11-27`. Two new files in
`folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/RationalAssociator/`:
`BaseChange.lean` and `Homogeneity.lean`. Both pass `lean`-direct (`-DautoImplicit=false
-s 65536`, exit 0). `#print axioms` on the main theorems lists only `propext`,
`Classical.choice` and `Quot.sound`. Neither file contains `sorry` or `axiom`. (B2) is used only
as a named hypothesis.

**(B0), proved.** `BaseChange.lean` defines:

- `evK a b : K ⊗[ℚ] ℚ⟨X, Y⟩ →ₐ[K] S`, evaluation into any `K`-algebra `S`;
- the filtrations `FilK` (in `K ⊗ U4 N`) and `FFK` (in `K ⊗ ℚ⟨X, Y⟩`);
- `AssocK K N E Φ`, an associator with coefficients in `K`. Its conditions are (5.12) at pairs of
  rational `Fil N 1`, and the hexagon and pentagon at the universal family.

Theorems:

- `rational_lift_of_assocK`. Take `d ≥ 1` and `ε(Φ) = ε(E) = 1`. Suppose `1 ⊗ Φ + z`, with
  `z ∈ K ⊗ FF d`, is a `K`-associator in `K ⊗ U4 (d + 1)`. Then there is a rational `x ∈ FF d`
  with `Φ + x` an associator in `U4 (d + 1)`. Moreover `1 ⊗ x − z` solves the base-changed
  homogeneous system, component by component (`KerK`).
  - The proof linearises in `K ⊗ U4 (d+1)` (`isTop_FilK`).
  - It then contracts each component with a `ℚ`-linear retraction `K → ℚ`.
  - It does not need `K ⊗ (product) → product (K ⊗ …)` to be injective.
- `solvableOver_of_assocK`. The same hypothesis gives `SolvableOver K d E Φ`.

**(B3), proved modulo (B2).** `Homogeneity.lean`:

- `exists_homog_part`: every `y ∈ FF d` is `h + (element of FF (d+1))` with `h` homogeneous of
  degree `d`.
- `eq_zero_of_homog_mem_FF`: a homogeneous `h` of degree `d` lying in `FF (d+1)` is zero.
  The proof extracts Vandermonde coefficients through `coeff_mem_of_forall`.
- `grtU4_of_lin`: take `h ∈ FF d` homogeneous of degree `d ≥ 1` with `assocLin (d+1) h = 0`.
  Then `GrtU4 M h` holds for every `M`, given `Lin514 M h`, the linearised (5.14) in `U4 M`, as
  a hypothesis.

How the transfer works:

- **(5.12).**
  - `U4 (d+1)` acts on `ℚ⟨X, Y⟩ ⧸ FF (d+1)` by `t₁₂ ↦ X`, `t₁₃ ↦ −X−Y`, `t₂₃ ↦ Y` and the
    other generators `↦ 0`.
  - So the condition at `(t₁₂, t₂₃)` gives `h + h(B, A) ∈ FF (d+1)`.
  - By homogeneity `h + h(B, A) = 0` in `ℚ⟨X, Y⟩`, which gives (5.12) in every ring.
- **(5.13) and (5.15).**
  - `U4 (d+1)` acts on `U4 M ⧸ Fil M (d+1)` by left multiplication by the generators.
  - So the identity in `U4 (d+1)` puts the `U4 M` expression in `Fil M (d+1)`.
  - The scaling `tᵢⱼ ↦ r tᵢⱼ` of `U4 M` multiplies the expression by `r^d`. An element of
    `Fil M (d+1)` with that property is `0`.
- No grading on `U4 M` was needed. The scaling endomorphisms and the Vandermonde argument
  replace it.

**(B1), not done.** What is needed, in order:

1. **`AssocK` is closed under rational `GRT1U4 N g`** (`Φ_K ↦ evK(g A g(B,A), B) Φ_K · g`).
   - The rational proofs are `pentagon_act`, `hexagon_act_of_transport` and `comp_inv512`.
     They use `φ` only through `eval_conj`, i.e. equivariance under conjugation by a unit.
   - Every `g`-side lemma is generic in the ring and applies unchanged in `S = K ⊗ U4 N`:
     `transported_dk4`, `far_of_tcompat`, `transported3_sum`, `transported3_dk3`,
     `tcompat_iff_poly`.
   - So the work is:
     - copy the three `φ`-side theorems with `eval · · φ` replaced by a function `f` satisfying
       that equivariance;
     - prove the equivariance and naturality of `evK` (both by `TensorProduct.induction_on`);
     - move the universal pentagon and hexagon to the transported family. Use the `K`-algebra
       map `K ⊗ U4 N → S` built from `lift N s` with `Algebra.TensorProduct.lift`. Its
       word-vanishing condition comes from `s ∈ FilK 1`.
2. **From `c ∈ ℚ` to `c ∈ K`.**
   - Let `gX = Σ_k X^k ⊗ expTerm h k ∈ (K ⊗ ℚ⟨X, Y⟩)[X]`.
   - Map each defect of `compK Φ_K gX` into `(K ⊗ U4 N)[X]` with `Polynomial.mapAlgHom (evK …)`.
   - Each defect vanishes at every rational `c`, by step 1 and
     `expPoly (c • h) = Σ c^k expTerm h k`. So by `coeff_mem_of_forall` with `⊥` it is the zero
     polynomial.
   - Evaluate it at `b ∈ K` with `Polynomial.eval₂AlgHom'`. The scalar `b` is central.
3. **The congruence `compK Φ_K gX(b) ≡ Φ_K + b ⊗ h (mod FFK (d+1))`.**
   - For rational `c` it follows from a version of `compPoly_congr` that is linear in `φ`:
     `compPoly φ g − φ − ε(φ) y ∈ FF (n+1)`. Then extend linearly to `Φ_K`.
   - Then apply the step-2 argument with `FFK (d+1)` in place of `⊥`. `FFK (d+1)` is closed
     under multiplication by `K`.
4. **Assemble.**
   - Write `KerK`'s `1 ⊗ x − z = Σ bᵢ ⊗ yᵢ` in a `ℚ`-basis of `K`. Each `yᵢ` lies in
     `ker linFF`.
   - Take degree-`d` parts `hᵢ` (`exists_homog_part`). Then `grtU4_of_lin` gives `GrtU4 N hᵢ`
     under (B2).
   - Shift `Φ_K` by `gX(bᵢ)` for each `i`.
   - The invariant should be stated at a fixed final level `N`: `AssocK K N E Φ_K` and
     `Φ_K − 1 ⊗ Φ ∈ FFK d`. `rational_lift_of_assocK` gets level `d+1` through the projection
     `U4 N → U4 (d+1)`.

Estimate: 600 to 800 lines, mostly copies of existing proofs with `eval · · φ` replaced by `f`.
None of it needs new mathematics beyond what is listed.

**A caveat on the (B2) hypothesis.**
- `Lin514 M h` is required for the specific `hᵢ`: degree-`d` parts of differences between
  rational solutions and the `K`-associator's degree-`d` part.
- Drinfeld's Prop. 5.7 proves (5.14) only for Lie `y`. The `hᵢ` here are Lie only if both
  associators are group-like. Neither `AssocU4` nor `AssocK` records that.
- So whatever the (B2) sibling proves has to cover these `hᵢ`. Either it proves (5.14) for
  non-Lie elements of the kernel, or group-likeness is added to both associator predicates and
  carried through the induction.

**Still open (bean `qou-3fdg`).** (B1) as above, and (B2).

## 15. Gap B2 (Drinfeld Prop. 5.7): what is proved, and the one bridge left

Bean `qou-3fdg`, PR #9696. New files `Prop57.lean` and `Prop57Cocycle.lean` under
`QOU/BraidsAndKnots/RationalAssociator/`. Every declaration below is sorry-free; lean-direct
(`-DautoImplicit=false -s 65536`) exits 0, and `#print axioms` shows only `propext`,
`Classical.choice`, `Quot.sound`.

Drinfeld's argument has two steps. Write `s(B, C) = [B, ψ(A, B)] + [C, ψ(A, C)]`, `A = −B − C`.

**Step 2, the vanishing lemma: proved in general** (`vanishing_of_cocycle`). Take `s ∈ ℚ⟨B, C⟩`
that is `LieLike`, symmetric, and whose cocycle
`s(Y₁, Y₂) − s(Y₁, Y₂ + Y₃) + s(Y₁ + Y₂, Y₃) − s(Y₂, Y₃)` lies in the words of length `≥ N`.
Then `s` itself lies in the words of length `≥ N`. The proof substitutes `Y₃ = x·C` with `x`
central, takes the `x`-coefficient, and gets that the Euler operator kills `s` below degree `N`.
It is purely algebraic.

**`s` is `LieLike` and symmetric for every `ψ`, Lie or not** (`sPoly_lieLike`, `sPoly_symm`). At
commuting `x, z`, the element `ψ(−x−z, x)` commutes with `x`, so both brackets vanish. The
vanishing lemma therefore carries no Lie hypothesis on `ψ`.

**Step 1, the cocycle identity: proved** (`cocycle_identity`, `uDefect_eq_zero`,
`GrtU4.uDefect_eq_zero`). At a four-strand Drinfeld–Kohno family,

`u = S(t₁₂, t₁₄, t₂₄) − S(t₁₂+t₁₃, t₁₄, t₂₄+t₃₄) + S(t₁₃+t₂₃, t₁₄+t₂₄, t₃₄) − S(t₂₃, t₂₄, t₃₄)`
`  = −[t₁₂+t₁₃+t₂₃, μ¹²³⁴] − [t₁₄+t₂₄, μ¹²⁴³] + [t₁₄, μ¹⁴²³]`,

where `S(A, B, C) = [B, ψ(A, B)] + [C, ψ(A, C)]` and `μ` is the linearised pentagon defect.
The identity uses only:

- antisymmetry (5.17);
- the linearised hexagon (5.18) at the DK3 subfamilies `(t₁₂, t₁₄, t₂₄)`,
  `(t₁₄, t₁₂+t₁₃, t₂₄+t₃₄)`, `(t₂₃, t₂₄, t₃₄)` and `(t₃₄, t₁₃+t₂₃, t₁₄+t₂₄)`;
- ten commuting facts.

The relation list came from an exact linear solve over ℚ, and Lean checks it with `noncomm_ring`.
In `U4 N`, `GrtU4`'s `lin512`, `lin513` and `lin515` give `u = 0`: the hexagon through `liftU3`,
and the pentagon at strand orders `1243` and `1423` through `lift` on permuted DK4 families.
**No Lie hypothesis is used in step 1.**

**The bridge still open (not formalised): from `u = 0` in `U4 N` to `cocycle(s) ∈ FF3 N`.** The
`A`-argument of each `S` term is `t₁₂`, `t₁₂+t₁₃`, `t₁₃+t₂₃` or `t₂₃`. It must be replaced by
`−B−C`, using that the sum of a DK3 triple commutes with each member. This **central shift** is
the one place a Lie hypothesis is needed: `ψ(a + z, b) = ψ(a, b)` for central `z` holds for Lie
`ψ` without linear part. The linear part `α(X − Y)` is harmless, because it is killed by the
bracket with `B`.

After the shift, every `S` term is a polynomial in `t₁₄, t₂₄, t₃₄`, and `u = 0` becomes
`cocycle(s)(t₁₄, t₂₄, t₃₄) = 0` in `U4 N`. To pull this back to `ℚ⟨Y₁, Y₂, Y₃⟩` modulo length
`N`, a retraction is needed: the DK4 family in `End(ℚ⟨Y⟩ ⧸ FF3 N)` with
- `t_{i4} ↦` left multiplication by `Y_i`;
- `t₁₃, t₂₃, t₁₂ ↦` the derivations with `Y₁ ↦ [Y₁, Y₃], Y₃ ↦ [Y₃, Y₁]` (and similarly for the
  other two).

Evaluate at `1`. The DK4 relations of this family were checked by machine (exact arithmetic,
low degree). In Lean the derivations can be built with the upper-triangular trick of
`GRTFlow.leibD`.

Finally, `lin514` at DK3 triples whose sum is nonzero needs the same central shift again
(`lin514_of_drinfeld519` covers only zero-sum triples). So, **as proved here, Lie-ness of `ψ`
enters only through the central shift**. Whether (5.19) holds for non-Lie `y` satisfying the
other three conditions is **not established**: it was neither tested nor proved.

## 16a. Gap B2 closed: (5.14) from (5.17), (5.18), (5.20) for Lie `y`

Bean `qou-3fdg`. New file `QOU/BraidsAndKnots/RationalAssociator/Prop57Link.lean`. It is
sorry-free and lean-direct (`-DautoImplicit=false -s 65536`) exits 0. `#print axioms` on
`lin514_of_lie`, `grtU4_of_lie` and `sPoly_mem_FF_of_lin` shows only `propext`,
`Classical.choice` and `Quot.sound`. The axiom check ran on a scratch copy, which was then
deleted. No `sorry`, `axiom`, `: True` or `native_decide` appears in the file.

**The headline result** is `lin514_of_lie`. Let `y ∈ ℚ⟨X, Y⟩` be a Lie element, and assume
`GrtU4`'s conditions `lin512` (5.17), `lin513` (5.18) and `lin515` (5.20) in `U4 N`, each stated
exactly as in `GrtU4`. Then `lin514` holds in `GrtU4`'s form at every `DK3` triple of
`Fil N 1`. `grtU4_of_lie` packages this as `GrtU4 N y`. Its `const` field follows from Lie-ness
(`IsLieElt.const`). Being a Lie element is an explicit hypothesis:

`IsLieElt y := y ∈ LieSubalgebra.lieSpan ℚ ℚ⟨X, Y⟩ {X, Y}`

with bracket `pq − qp`. No statement in the file was weakened.

The pieces, in the order of §15's plan:

1. **Central shift** (`central_shift`, `shift_left`, `shift_right`). Suppose `z` and `w` commute
   with `a`, `b` and with each other. Then

   `y(a + z, b + w) = y(a, b) + α z + β w` for some `α, β ∈ ℚ`.

   The proof is induction over `lieSpan`. The linear part is kept as `α z + β w` instead of
   being assumed zero.
2. **`S` is `s`** (`S_eq_eval_sPoly`). At any `DK3` triple `(A, B, C)`,

   `[B, y(A, B)] + [C, y(A, C)] = s(B, C)`.

   The proof shifts `−B−C` by the central `A + B + C`. The linear terms die because `z`
   commutes with `B` and `C`. Hence (`uDefect_eq_lift_cocycle`)

   `u = cocycle(s)(t₁₄, t₂₄, t₃₄)`,

   using the `DK3` subfamilies `(t₁₂, t₁₄, t₂₄)`, `d2`, `d1` and `d0` of `dk4`.
3. **The retraction** (`retract`). This is an algebra map `U4 N → End(ℚ⟨Y₁, Y₂, Y₃⟩ ⧸ FF3 N)`.
   - `t_{i4}` acts as left multiplication by `Yᵢ`.
   - `t₁₂`, `t₁₃` and `t₂₃` act as the Leibniz maps with `Yᵢ ↦ [Yᵢ, Yⱼ]`, `Yⱼ ↦ [Yⱼ, Yᵢ]` and
     the third generator sent to `0`. They are built with the upper-triangular matrix trick
     (`triHom3`, `der3`).

   All fifteen `DK4` relations are proved in Lean (`gen_dk4`):
   - the three far relations, from the `0` entries;
   - the six mixed relations, from `[Y_i + Y_j, ·]`-type cancellations;
   - the three Leibniz–Leibniz relations, from generator checks by `noncomm_ring`.

   Words of length `N` vanish because every generator raises the word filtration
   (`gen_word_eq_zero`). Evaluating at `1` (`mem_FF3_of_lift_eq_zero`) turns
   `cocycle(s)(t₁₄, t₂₄, t₃₄) = 0` into `cocycle(s) ∈ FF3 N`.
4. **Assembly.**
   - `uDefect_eq_zero_of_lin` is `GrtU4.uDefect_eq_zero` restated with `lin512`, `lin513` and
     `lin515` as hypotheses, without `lin514`.
   - With `vanishing_of_cocycle` it gives `sPoly y ∈ FF N` (`sPoly_mem_FF_of_lin`).
   - Evaluating at `A, B ∈ Fil N 1` gives (5.19), since `Fil N N = 0`.
   - `lin514_of_drinfeld519` then gives the zero-sum triples.
   - A triple `(u, v, w)` with central sum `z ≠ 0` reduces to `(−(v + w), v, w)`. The two shifts
     `α z` and `β z` satisfy `(α + β) z = 0` by (5.17) at `(u, w)` and `(−(v + w), w)`. Since `z`
     commutes with `v + w`, the right side of (5.14) does not change.

**Scope.** These are statements in each truncation `U4 N`, which is how `GrtU4` is stated. Lie-ness
enters only through the central shift. Whether non-Lie `y` can satisfy the three conditions
without (5.14) is still **not established**, as §15 said: neither tested nor proved. B1, in
`BaseChange.lean` and `Homogeneity.lean`, was not touched.

## 16b. Gap B1, step (1) closed; steps (2)–(4) and the Lie-ness input still open

Bean `qou-3fdg`, branch `claude/grt-b1-basechange-2026-11-27`, file
`RationalAssociator/BaseChangeAction.lean` (sorry-free; `#print axioms assocK_compK` gives
`propext`, `Classical.choice`, `Quot.sound` only, checked in a scratch copy).

### What is proved

**Step (1): `AssocK` is closed under a rational `GRT₁` element.**

    theorem assocK_compK (hΦ : AssocK K N E Φ) (hg : GRT1U4 N g) : AssocK K N E (compK Φ g)

where `compK Φ g = (id_K ⊗ subst[A ↦ g·A·g(B,A), B ↦ B]) Φ · (1 ⊗ g)` is Drinfeld's (5.16)
with the inverse written through (5.12), base-changed in its first argument.
`evK_compK` evaluates it as `Φ(g(a,b)·a·g(b,a), b) · g(a,b)`.

How it is proved:

* The action theorems `pentagon_act` and `hexagon_act_of_transport` use `φ` only through
  `φ(u⁻¹au, u⁻¹bu) = u⁻¹ φ(a,b) u`. They are repeated for an arbitrary `f : R → R → R`
  with that property (`pentagon_actF`, `hexagon_act_of_transportF`). For `f = evK · · Φ`
  the property is `evK_conj`.
* The units `g(·,·)` and the transported family are rational, because `g` is. So the
  rational lemmas `far_of_tcompat`, `transported_dk4`, `transported3_sum` and
  `transported3_dk3` give the rational transported family as a nilpotent `DK4` (resp. `DK3`)
  family, unchanged. `pentK_of_universal` / `hexK_of_universal` move the pentagon / hexagon of
  `Φ` from the universal family to it, by the `K`-algebra map `id_K ⊗ lift`, which commutes
  with `evK` (`map_evK`).
* (5.12) of `compK Φ g` (`inv_compK`) is conjugation by the rational unit `g(b,a)` plus (5.12)
  of `Φ` at the rational pair `(g(a,b) a g(b,a), b)`. The constant term (`const_compK`) uses
  `eval 0 0 p = ε(p)` (`eval_zero_zero`).

### What is not done

**Step (2): `c ∈ ℚ` to `c ∈ K`.** The shifts needed in step (4) are `exp(β·h)` with `β ∈ K`,
whose coefficients are in `K`, so `assocK_compK` (rational `g`) does not apply directly. Planned
route: for the four defects (const, (5.12), hexagon, pentagon) of `Φ ∘ exp(β h)`, show each is
`Σ_{j<n} βʲ d_j` with `d_j ∈ K ⊗ U4 N` independent of `β` (work in `(K ⊗ U4 N)[T]` and evaluate
at the central element `β`), vanishing for every `β ∈ ℚ` by step (1) and `grt1U4_expPoly`; then
`coeff_mem_of_forall` with `F = ⊥` gives `d_j = 0`. Not written.

**Step (3): the `K`-congruence** `Φ ∘ exp(β h) ≡ Φ + β ⊗ h (mod FFK (d+1))` for `h ∈ FF d`. The
`K`-version of `compPoly_congr` / `expPoly_congr`. Not written; it is a filtration argument
of the same shape as the rational one.

**Step (4): the shift.** Decompose `z = Φ_K − 1 ⊗ x ∈ K ⊗ FF d` (with `x = contract π z` the
rational lift of `rational_lift_of_assocK`) in a `ℚ`-basis `β_i` of `K`, `z ≡ Σ β_i ⊗ h_i`
mod `FFK (d+1)`, and shift `Φ_K` by `exp(−β_i h_i)` one `i` at a time. Each `h_i` must be in
`grt`, which is where B2 enters. Not written.

### The Lie-ness input: carrying it is a real gap, not bookkeeping

B2 is now discharged in `Prop57Link.lean` (#9711): `grtU4_of_lie (hy : IsLieElt y) (h512)
(h513) (h515) : GrtU4 N y`, with `IsLieElt y` meaning `y ∈ lieSpan ℚ {ι 0, ι 1}`. So step (4)
needs `IsLieElt h_i` for the degree-`d` parts `h_i`.

The plan's suggestion was to carry group-likeness of the `K`-associator. Worked out (not in
Lean): if the `K`-associator is group-like modulo degree `N` and the rational `x` is the explicit
contraction, then each `h_i` is **primitive**, `Δ h_i = h_i ⊗ 1 + 1 ⊗ h_i`. But `grtU4_of_lie`
needs `h_i ∈ lieSpan`, and primitive ⟹ Lie is the **Friedrichs criterion**. It is not in this
corpus and not used anywhere in it (searched: `Friedrichs`, `primitive`, `lieSpan` in
`folio/` and `computations/`; Mathlib not searched for a version over `FreeAlgebra`, so
"not in Mathlib" is unverified).

Three ways to close it, none started:

1. **Prove Friedrichs for `ℚ⟨X, Y⟩`** (characteristic 0): via the Dynkin–Specht–Wever
   projector `θ(x₁⋯x_n) = [[x₁, x₂], …, x_n]`, which satisfies `θ(y) = n·y` on primitive
   homogeneous `y` of degree `n`, and whose image is in `lieSpan` by construction. A single
   self-contained algebraic file. Then carry group-likeness as planned.
2. **Carry `Φ_K = exp(ψ)` with `ψ` Lie.** Then the lowest-degree difference of two such is the
   difference of the `ψ`'s, which is Lie. But the shift must preserve the form, which needs
   Baker–Campbell–Hausdorff closure of `exp(Lie)` (the `actEval` composition of two
   exponentials). Harder than option 1.
3. **Change B2's input**: a version of `grtU4_of_lie` whose hypothesis is primitivity. Its
   proof uses Lie-ness only for the central shift `y(a+z, b) = y(a, b)` (§15), which primitivity
   also gives, at least in degree terms. Not checked.

The judgement here (not a finding): option 1 is the cleanest, because it is self-contained and
reusable, and it keeps `grtU4_of_lie` unchanged.

Default if nothing is chosen: B1 stays at step (1); the induction step stays conditional on
steps (2)–(4) and on the Lie-ness input.

## 17a. The Friedrichs criterion: primitive ⇒ Lie (proved)

`Friedrichs.lean`, sorry-free. `#print axioms` shows only `propext`, `Classical.choice` and
`Quot.sound`.

**Statement** (`isLieElt_of_primitive`). Let `Δ` be the shuffle coproduct on `ℚ⟨X, Y⟩`, the
algebra map with `Δ(ι i) = ι i ⊗ 1 + 1 ⊗ ι i`. If `Δ h = h ⊗ 1 + 1 ⊗ h`, then `IsLieElt h`.

The theorem assumes neither homogeneity nor a zero constant term. A primitive element has zero
constant term anyway (`algebraMapInv_eq_zero_of_primitive`). So `Homogeneity.exists_homog_part`
is not needed here.

**Proof** (Dynkin–Specht–Wever, with no coordinates on words):

1. **Antipode identity** (`idS_cop`). Let `S` be the anti-automorphism with `S(ι i) = −ι i`.
   Then `m ∘ (id ⊗ S) ∘ Δ = η ∘ ε`.
2. **The Dynkin map is Lie-valued** (`dS_cop_mem`). Let `D` be the Euler derivation,
   `D(ι i) = ι i`. Then `D ⋆ S = m ∘ (D ⊗ S) ∘ Δ` satisfies
   `(D ⋆ S)(ι i · w) = ε(w) ι i + [ι i, (D ⋆ S)(w)]`, so it maps every element into the Lie span.
   On a primitive `p`, `(D ⋆ S)(p) = D p`. Hence `D p` is Lie (`eulerD_mem_of_primitive`).
3. **D is a coderivation** (`cop_eulerD`): `Δ ∘ D = (D ⊗ id + id ⊗ D) ∘ Δ`. So `D` preserves
   primitives.
4. **Induction on word length.** Let `G N` be the span of the words of length `≤ N`. Then
   `D − (N + 1)` maps `G (N + 1)` into `G N`, and a primitive element of `G 0` is `0`. If `p`
   is primitive and lies in `G (N + 1)`, then `(N + 1) p = D p − (D − (N + 1)) p` is a
   difference of Lie elements.

The three tensor identities behind steps 1–3 are checked on pure tensors. Every statement about
`ℚ⟨X, Y⟩` is proved by induction on left multiplication by a generator (`induction_left`).

**Use for B1.** If the degree-`d` parts `hᵢ` of a difference of group-like associators are
shown primitive, this theorem gives the `IsLieElt` hypothesis of `grtU4_of_lie`. That
primitivity is **not** proved here. `IsPrimitive` is stated for the `cop` defined in this file.
Any group-likeness hypothesis has to use the same coproduct, or be shown equal to it.

**Verification.** `lean -DautoImplicit=false -s 65536` exits 0 with no warnings.
`Prop57Link.olean` was not in the restored cache, so it was compiled into a scratch shadow tree
first. No `lake build` was run.

## 17b. Gap B1, steps (2)–(4) closed; the induction step proved modulo primitivity of the top layer

Bean `qou-3fdg`, branch `claude/grt-b1-steps-2026-11-27`, file
`RationalAssociator/BaseChangeK.lean`. The file is sorry-free. `#print axioms`, run in a scratch
copy that was then deleted, gives `propext`, `Classical.choice` and `Quot.sound` only, for
`inductionStep_of_primitiveLayer`, `assocK_shift_finset`, `compKK_congr`, `assocK_shiftK` and
`grtU4_of_lin_primitive`.

### What is proved

**Step (2): shifts with coefficients in `K`.**

    theorem assocK_shiftK (hΦ : AssocK K N E Φ) (hg : ∀ x : ℚ, GRT1U4 N (expPoly (x • h) n))
        (c : K) : AssocK K N E (compKK Φ (GK h n c))

* `GK h n c = Σ_{k<n} cᵏ ⊗ hᵏ/k!` is the truncated exponential with `K`-coefficients.
* `compKK` is the action of §16b with a `K`-valued group element.

How it is proved:

* Each of the four defects (constant term, (5.12), hexagon, pentagon) is the evaluation at
  `T = c` of one polynomial over `K ⊗ U4 N` (`evT`, `ΓT`, `fT`).
* At every rational `T = x` that polynomial vanishes, by `assocK_compK` (§16b) and
  `grt1U4_expPoly` (§12).
* A polynomial over a `ℚ`-algebra that vanishes at every rational point is zero
  (`eq_of_forall_rat`, via `coeff_mem_of_forall`).

**Step (3): the `K`-congruence.** For `1 ≤ d`, `2 ≤ n`, `h ∈ FF d` and `Φ ≡ 1 (FFK 1)`:

    theorem compKK_congr : compKK Φ (GK h n c) - Φ - c ⊗ₜ h ∈ FFK K (d + 1)

The supporting facts:

* `GK h n c ≡ 1 + c ⊗ h` modulo `FFK (2d)` (`GK_sub_mem`).
* `FFK` is multiplicative (`mul_mem_FFK`).
* `evK` respects `FFK` in both arguments (`evK_sub_mem_FFK`, `evK_mem_FFK`).

**Step (4): finitely many shifts.** `assocK_shift_finset` shifts a `K`-associator `Ψ₀ ≡ 1` in
turn by `exp(c_i h_i)` for `i ∈ s`. The result `Ψ` satisfies
`Ψ ≡ Ψ₀ + Σ c_i ⊗ h_i (FFK (d+1))`.

**Projection.** `AssocK.proj : AssocK K N E Φ → M ≤ N → AssocK K M E Φ`. It uses the algebra
map `U4 N → U4 M` sending `t` to `t` (`projU`).

**The bridge (B2 + Friedrichs, no Lie-ness hypothesis).**

    theorem grtU4_of_lin_primitive (hy : Homog d y) (hlin : assocLin (d + 1) y = 0)
        (hp : Friedrichs.IsPrimitive y) : GrtU4 M y

It is the proof of `grtU4_of_lin` with `grtU4_of_lie (isLieElt_of_primitive hp)` in place of
the (5.14) hypothesis. As instructed, Lie-ness is discharged by §17a, not carried.

**The induction step.**

    theorem inductionStep_of_primitiveLayer (hd : 1 ≤ d) (hdN : d + 1 ≤ N) (hn : 2 ≤ n)
        (hNn : N ≤ n) (hE : ε E = 1) (hΦ : ε Φ = 1) (z : K ⊗ FF d)
        (hK : AssocK K N E (1 ⊗ Φ + z))
        (hprim : ∀ μ : K →ₗ[ℚ] ℚ, ∃ h, Homog d h ∧ contract μ z - h ∈ FF (d+1) ∧ IsPrimitive h) :
        ∃ x ∈ FF d, AssocU4 (d + 1) E (Φ + x) ∧
          ∃ Ψ, AssocK K N E Ψ ∧ Ψ - 1 ⊗ (Φ + x) ∈ FFK K (d + 1)

The proof:

1. Choose a retraction `π`, with `π(1) = 1`. Let `x = contract π z`.
2. (B0) `rational_lift_of_assocK` gives a solution `x₀`. Its kernel statement, contracted along
   any `μ`, shows two things: `x` solves the same degree-`d` system as `x₀`, so `Φ + x` is an
   associator in `U4 (d+1)`; and `u = 1 ⊗ x − z` has every contraction in the homogeneous
   kernel.
3. Take the `hprim` representatives `h_μ`. Then `H_μ = μ(1)·h_π − h_μ` is homogeneous and
   primitive, lies in `FF d`, and represents `contract μ u` modulo `FF (d+1)`.
4. `H_μ` is in the kernel, because `assocLin N` kills `FF N` (`assocLin_eq_zero_of_mem_FF`). So
   `H_μ ∈ grt` by the bridge, and `exp(r H_μ) ∈ GRT₁` by `grt1U4_expPoly`.
5. Expand `u` in a `ℚ`-basis `B` of `K` (`equivFinsuppOfBasisLeft`). Its coordinates are the
   contractions along `B.coord i` (`equivFinsuppOfBasisLeft_eq_contract`).
6. Shift `1 ⊗ Φ + z` by `exp(B_i · H_{B.coord i})` over the finite support (step 4).
7. The result agrees with `1 ⊗ (Φ + x)` modulo `FFK (d+1)`.

The output has the shape of the input one degree up. `Ψ − 1 ⊗ (Φ + x) ∈ FFK (d+1)` is
`Ψ = 1 ⊗ (Φ + x) + z'` with `z' ∈ K ⊗ FF (d+1)`. So the theorem can be iterated as long as
`d + 2 ≤ N`, provided `hprim` holds again at degree `d + 1`.

### What is not done: `hprim` is assumed, not derived

The theorem takes as a hypothesis that every rational contraction of the top layer `z` is,
modulo `FF (d+1)`, a homogeneous primitive element. It does **not** re-establish this at degree
`d + 1`. So the "still agreeing with a group-like `K`-associator" half of the target statement
is not proved. Group-likeness is never defined over `K` here.

What would discharge it, in order:

1. **Group-likeness over `K`.** Base-change `Friedrichs.cop` to `K ⊗ F → K ⊗ (F ⊗ F)`. Define
   `GLK N Ψ`: `Δ_K Ψ ≡ Ψ ⊗ Ψ` modulo the degree-`N` filtration of `F ⊗ F`. That filtration is
   not defined anywhere in the corpus. It is needed because a group-like element can only be
   asked for modulo a degree.
2. **Transport under the action.**
   * `compK` / `compKK` must preserve `GLK` when the acting element is group-like.
   * `Δ` must commute with the substitution `A ↦ g A g(B, A)`, `B ↦ B` for group-like `g`.
   * The truncated exponential `GK h n c` of a primitive `h` is group-like modulo degree `n`.
     This needs the binomial identity for `Δ(hᵏ)` with `h` primitive.
3. **Extraction.** Suppose `Ψ = 1 ⊗ Φ + z` is group-like modulo degree `d + 1`, and so is the
   rational `Φ`. Then `Δ z − z ⊗ 1 − 1 ⊗ z` lies in filtration degree `d + 1`.
   * Contraction along `μ` commutes with `Δ`. So each `contract μ z` is primitive modulo degree
     `d + 1`.
   * `Homogeneity.exists_homog_part` then gives the homogeneous degree-`d` part. It is primitive
     if `cop` commutes with the grading: `cop ∘ scF r = (scF r ⊗ scF r) ∘ cop`. This is not
     proved.
4. **Group-likeness of the rational lift.** `Φ + x` must be group-like modulo `d + 2` for the
   next step. It agrees with the group-like `Ψ` modulo `FFK (d+1)`, so it is group-like modulo
   `d + 1` for free. Degree `d + 1` itself needs its own argument, or the hypothesis can be moved
   to `Ψ` alone.

Each item is ordinary algebra with no analysis, but together they are a separate file of roughly
the size of `Friedrichs.lean`. They were not started in this tranche.

Default if nothing is chosen: B1 stands as `inductionStep_of_primitiveLayer`, a sorry-free
theorem conditional on `hprim`. The Drinfeld rational-associator induction is complete except
for the group-likeness transport above.

**Verification.** `lean -DautoImplicit=false -s 65536` on `BaseChangeK.lean` exits 0 with no
warnings. It was compiled against the restored cache, with this branch's new modules compiled
into a scratch tree. No `lake build` was run.

## 17c. Group-likeness transport over K: `hprim` derived, and re-established one degree up

Bean `qou-3fdg`. All four items of §17b are proved, sorry-free, in
`folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/RationalAssociator/GroupLikeK.lean`.
Axioms: `propext`, `Classical.choice`, `Quot.sound`. No analysis is used.

| §17b item | Lean | statement |
|---|---|---|
| 3. primitive layer | `exists_primitive_layer` | `p ∈ FF d`, `Δp − p⊗1 − 1⊗p ∈ FF2 (d+1)` ⇒ the degree-`d` part of `p` is primitive |
| 1. GLK over K | `GLK`, `primLayer_of_GLK` | `Δ_K Ψ − i₁Ψ · i₂Ψ ∈ FF2K m`; for `Ψ = 1⊗Φ + z`, `GLK (d+1)` gives exactly the `hprim` of `inductionStep_core` |
| 2. invariance under the shift | `GL_expPoly`, `GLK.subst`, `GLK.compK`, `GLK.compKK_GK` | `GLK N Ψ ⇒ GLK N (compKK Ψ (GK H n c))` for every `c ∈ K`, `H ∈ FF 1` primitive, `N ≤ n`, `exp(xH) ∈ GRT1U4 N` for all rational `x` |
| 4. the step | `inductionStep_of_groupLike` | `inductionStep_core` with `hprim := primLayer_of_GLK` and `Q := AssocK ∧ GLK N` |

How item 2 goes:

1. `cop (expTerm y k) = Σ_m expTerm y m ⊗ expTerm y (k−m)` for primitive `y`, so the truncated
   exponential of a primitive `y ∈ FF 1` is group-like modulo `FF2 n` (`GL_expPoly`).
2. A `K`-substitution `X ↦ a`, `Y ↦ b` with `a, b ∈ FF 1` primitive modulo `FF2 N` preserves
   `GLK N`. Two `K`-algebra maps congruent modulo the two-sided ideal `FF2K N` on `X` and `Y` are
   congruent everywhere (`sub_mem_FF2K_of_gen`).
3. (5.12) for `g ∈ GRT1U4 (M+1)` gives `g · g(Y,X) ≡ 1` modulo `FF (M+1)` (`mul_swap_sub_one_mem`,
   through `toFree` as in `add_swap_eq_zero`). With `GL N g` and `GL N g(Y,X)` (`GL.swap`), the
   substituted variable `g X g(Y,X)` is primitive modulo `FF2 N` (`conj_almost_primitive`). So
   Drinfeld's rational action `compK Ψ g` preserves `GLK N` (`GLK.compK`).
4. At rational `c = x`, `compKK Ψ (GK H n x) = compK Ψ (expPoly (xH) n)`. The defect
   `Δ_K(·) − i₁(·)i₂(·)` of `compKK Ψ (GK H n c)` is a polynomial in `c` with coefficients in
   `K ⊗ (ℚ⟨X,Y⟩ ⊗ ℚ⟨X,Y⟩)`, so `mem_of_forall_rat` carries the rational case to all `c ∈ K`.

Statement of the step:

```lean
theorem inductionStep_of_groupLike (hd : 1 ≤ d) (hdN : d + 1 ≤ N) {n : ℕ} (hn : 2 ≤ n)
    (hNn : N ≤ n) {E Φ : F2} (hE : algebraMapInv E = 1) (hΦ : algebraMapInv Φ = 1)
    (z : K ⊗[ℚ] FF d)
    (hK : AssocK K N E ((1 : K) ⊗ₜ Φ + LinearMap.lTensor K (FF d).subtype z))
    (hGL : GLK K N ((1 : K) ⊗ₜ Φ + LinearMap.lTensor K (FF d).subtype z)) :
    ∃ x ∈ FF d, AssocU4 (d + 1) E (Φ + x) ∧ GL (d + 1) (Φ + x) ∧
      ∃ Ψ, AssocK K N E Ψ ∧ GLK K N Ψ ∧ Ψ - (1 : K) ⊗ₜ (Φ + x) ∈ FFK K (d + 1)
```

§17b item 4 is resolved by the second route it named: the group-likeness hypothesis is carried by
the `K`-associator `Ψ` (at the full level `N`), not by the rational lift. `Φ + x` is group-like
modulo `FF2 (d+1)` only, which is what follows from `Ψ`.

**What is not done.** Iterating the step needs the output in the input's shape:
`Ψ = 1 ⊗ (Φ + x) + z'` with `z'` in the image of `K ⊗ FF (d+1)` under `lTensor`. The step gives
`Ψ − 1 ⊗ (Φ + x) ∈ FFK K (d+1)`. No lemma in `RationalAssociator/` converts `FFK` membership into
that `lTensor` form (searched: no hit for `FFK` together with `lTensor`). Also needed:
`ε(Φ + x) = 1`, from `x ∈ FF d` with `d ≥ 1`. Neither step is analysis, but neither was written in
this tranche, so the full induction is not yet assembled as one theorem.

**Verification.** `lean -DautoImplicit=false -s 65536` on `GroupLikeK.lean` exits 0 with no
warnings or errors. It was compiled against the restored cache plus this branch's modules
compiled into a scratch tree. `#print axioms` on `inductionStep_of_groupLike`, `GLK.compKK_GK`,
`GL_expPoly` and `primLayer_of_GLK` shows only `propext`, `Classical.choice` and `Quot.sound`. No
`lake build` was run.

## §17d. The chain: a rational associator modulo `N` from a group-like `K`-associator (2026-11-27)

New file `RationalAssociator/AssociatorChain.lean` (sorry-free). It closes the two gaps §17c
listed and iterates `inductionStep_of_groupLike` from degree 1 to degree `N`.

- **Input form.** `FFK K m` is defined as `LinearMap.range (lTensor K (FF m).subtype)`, so
  `Ψ − 1 ⊗ Φ ∈ FFK K m` unfolds to `Ψ = 1 ⊗ Φ + lTensor z` (`exists_lTensor_of_mem_FFK`, three
  lines).
- **Constant term.** `algebraMapInv_add_of_mem_FF`: `ε(Φ + x) = 1` from `x ∈ FF d`, `d ≥ 1`, via
  the existing `algebraMapInv_eq_zero_of_mem_FF`.
- **Base case.** `Φ = 1` at degree 1. `sub_evK_zero_mem_FFK`: every `x ∈ K ⊗ ℚ⟨X,Y⟩` agrees with
  `evK 0 0 x ⊗ 1` modulo `FFK K 1`; with `AssocK.const` this gives `Ψ₀ − 1 ∈ FFK K 1`
  (`AssocK.sub_one_mem_FFK`).
- **Invariant** (`chain_invariant`, by `Nat.le_induction` on `d ≥ 1`): for `1 ≤ d ≤ N` there is a
  rational `Φ` with `ε(Φ) = 1`, with `AssocU4 d E Φ ∧ GL d Φ` once `d ≥ 2`, and a group-like
  `K`-associator `Ψ` in `U4 N` with `Ψ ≡ 1 ⊗ Φ (mod FFK K d)`. The step uses truncation order
  `n = N`.

```lean
theorem rational_associator_of_groupLikeK {N : ℕ} (hN : 2 ≤ N) {E : F2}
    (hE : FreeAlgebra.algebraMapInv E = 1) {Ψ₀ : K ⊗[ℚ] F2} (hK : AssocK K N E Ψ₀)
    (hGL : GLK K N Ψ₀) :
    ∃ Φ : F2, AssocU4 N E Φ ∧ GL N Φ

structure GroupLikeKAssociatorTower (E : F2) : Prop where
  exists_assoc : ∀ N : ℕ, 2 ≤ N → ∃ Ψ : K ⊗[ℚ] F2, AssocK K N E Ψ ∧ GLK K N Ψ

theorem rational_associator_of_tower {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : GroupLikeKAssociatorTower K E) {N : ℕ} (hN : 2 ≤ N) :
    ∃ Φ : F2, AssocU4 N E Φ ∧ GL N Φ
```

**What remains.** The only unproved input is the hypothesis itself: for some field `K ⊇ ℚ`, a
`K`-associator in `K ⊗ U4 N` for `E`, group-like modulo `FF2K N`, for each `N ≥ 2`. For `K = ℂ`
this is Drinfeld's KZ associator truncated at `N`, an analytic construction that nothing in this
repository formalises. It enters as a hypothesis or as the fields of `GroupLikeKAssociatorTower`,
never as an axiom. Two further limits of scope:

- `N ≥ 2` is assumed. The cases `N ∈ {0, 1}` are not stated.
- The rational `Φ` is constructed separately for each `N`. The statement does not say that the
  `Φ` for `N + 1` reduces to the `Φ` for `N`, so this is not a compatible tower and not a rational
  associator in the completed algebra. Getting one needs either a compatible `K`-tower plus a
  choice that respects it, or a direct induction over `N` that keeps the earlier lift; neither is
  done here.

**Verification.** `lean -DautoImplicit=false -s 65536` on `AssociatorChain.lean` exits 0 with no
output, against the restored cache plus `/home/claude/gltbuild` (this branch's modules up to
`GroupLikeK`). `#print axioms` on `rational_associator_of_groupLikeK`,
`rational_associator_of_tower`, `chain_invariant` and `sub_evK_zero_mem_FFK` shows only `propext`,
`Classical.choice` and `Quot.sound`. No `lake build` was run.

## §17e. A compatible tower of rational associators, from a compatible `K`-tower (2026-11-27)

New file `RationalAssociator/AssociatorTower.lean` (sorry-free). It answers the second limit of
§17d: the `Φ_N` there were chosen independently for each `N`. Here one sequence is built whose
truncations agree.

```lean
structure CompatibleGroupLikeKAssociatorTower (E : F2) : Prop where
  exists_tower : ∃ Ψ : ℕ → K ⊗[ℚ] F2, ∀ N : ℕ, 2 ≤ N →
    AssocK K N E (Ψ N) ∧ GLK K N (Ψ N) ∧ Ψ (N + 1) - Ψ N ∈ FFK K N

theorem rational_associator_compatible_of_tower {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : CompatibleGroupLikeKAssociatorTower K E) :
    ∃ Φ : ℕ → F2, (∀ N, 2 ≤ N → AssocU4 N E (Φ N) ∧ GL N (Φ N)) ∧
      ∀ N, 1 ≤ N → Φ (N + 1) - Φ N ∈ FF N
```

**The hypothesis is strengthened, and this is route (b).** `GroupLikeKAssociatorTower` (§17d)
asks for a `K`-associator at each level separately; `CompatibleGroupLikeKAssociatorTower` also
asks that consecutive ones agree modulo `FFK K N`. The truncations of one group-like associator
in the completed algebra (for `K = ℂ`, Drinfeld's KZ associator) satisfy this, so the
strengthening is the natural form of the analytic input, but it is a strengthening.
`CompatibleGroupLikeKAssociatorTower.toTower` gives the old hypothesis from the new one. Route
(a), which would remove the strengthening, needs the transitivity of the `GRT₁` action on
group-like associators modulo `d` (Drinfeld Prop. 5.5) together with a lift of the connecting
element; that is not done.

How the induction is made uniform in the level:

- **Congruence of the shift.** `compKK_sub_mem`: `Ψ ≡ Ψ'` and `G ≡ G'` modulo `FFK m` give
  `compKK Ψ G ≡ compKK Ψ' G'` modulo `FFK m`. `GK_sub_GK_mem`: for `H ∈ FF 1`, the truncated
  exponentials `GK H n c` at two orders `n, n' ≥ m` agree modulo `FFK m`.
- **Lists of shifts.** `shiftL n L Ψ` applies the shifts `(c, H) ∈ L` at truncation order `n`.
  `shiftL_pred` (predicates kept), `shiftL_sub_mem` (congruence kept, at any two orders `≥ m`),
  `shiftL_sum` (`shiftL n L Ψ ≡ Ψ + Σ c ⊗ H` modulo `FFK (d + 1)` for `H ∈ FF d`).
- **The step's data at one level** (`stepData`). The proof of `inductionStep_core` re-run so that
  it returns the rational `x` and the list of shifts instead of applying them. It uses only the
  `K`-associator at level `d + 1`. The shift directions are primitive, in `FF d`, and in `grt` in
  **every** `U4 M` (`grtU4_of_lin_primitive` has no level hypothesis), so the same list preserves
  `AssocK K M` and `GLK K M` at every level `M`.
- **The tower step** (`towerStep`). Invariant `TowerInv K E d Φ Ψ`: `ε(Φ) = 1`, and from level
  `d + 1` on every `Ψ N` is a group-like `K`-associator in `U4 N`, `Ψ N ≡ 1 ⊗ Φ` modulo
  `FFK d`, and `Ψ (N + 1) ≡ Ψ N` modulo `FFK N`. The new tower is
  `Ψ' N = shiftL (N + 2) L (Ψ N)`; compatibility of `Ψ'` is `shiftL_sub_mem`, and
  `Ψ' N ≡ 1 ⊗ (Φ + x)` modulo `FFK (d + 1)` uses `Ψ N ≡ Ψ (d + 1)` modulo `FFK (d + 1)`
  (`sub_mem_FFK_of_consecutive`).
- **The sequence** (`exists_seq_of_step`): dependent choice along `ℕ`, by `Nat.rec` over a
  subtype; `Φ N` is the rational part after `N − 1` steps.

**Scope.** `AssocU4 N` and `GL N` are claimed for `N ≥ 2`; compatibility for `N ≥ 1`. The result
is still a sequence of polynomials with compatible truncations, not an element of a completed
algebra; no completion is defined in `RationalAssociator/`.

**Verification.** `lean -DautoImplicit=false -s 65536` on `AssociatorTower.lean` exits 0 with no
output, against the restored cache plus `/home/claude/chainbuild` (this branch's modules up to
`AssociatorChain`). `#print axioms` on `rational_associator_compatible_of_tower`, `towerStep`,
`stepData`, `shiftL_sub_mem`, `shiftL_sum`, `compKK_sub_mem` and
`CompatibleGroupLikeKAssociatorTower.toTower` shows only `propext`, `Classical.choice` and
`Quot.sound` (`exists_seq_of_step`: `Classical.choice` only). No `lake build` was run.

## 17f. Stage 5: the quasi-Yang–Baxter equation for the rational tower (bean `qou-3fdg`)

File: `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/RationalAssociator/QuasiYBE.lean`.

**Which reading.** Reading (a), a concrete quasi-triangular instance `(A, Δ, R)` over `ℚ` with a
rational `Φ`, needs a realisation `t_ij ↦ h·Ω_ij` of the Drinfeld–Kohno algebra in
`U(𝔤)^{⊗3}[h]/(h^N)` by a Casimir tensor, together with the invariance of `Ω` that makes the
`Ω_ij` satisfy the Drinfeld–Kohno relations and `(Δ ⊗ id)(e^{hΩ/2}) = e^{h(Ω₁₃+Ω₂₃)/2}`. None
of that is in the repository (the `HeckeTemperleyLieb/*Casimir*` files are about Hecke/TL
blocks, not about `Ω ∈ U(𝔤)^{⊗2}`). So reading (b) was taken: the universal statement in the
truncated algebra `U4 N`, and its transport to every realisation.

**What `AssocU4` encodes.** Constant term `1`, (5.12) on `Fil N 1`, the hexagon in the repo's
form `E(t₁₃+t₂₃) = φ(t₁₃,t₁₂) E(t₁₃) φ(t₂₃,t₁₃) E(t₂₃) φ(t₁₂,t₂₃)` at the universal three-strand
family `(t₁₂, t₁₃, t₂₃)` of `U4 N`, and the pentagon in `U4 N`. With `R_ij = E(t_ij)` this is
Drinfeld's hexagon `(Δ⊗id)R = Φ₃₁₂ R₁₃ Φ₁₃₂⁻¹ R₂₃ Φ₁₂₃`, with `Φ₁₃₂⁻¹ = φ(t₂₃,t₁₃)` by (5.12).
That matches `P, Q, Φ` of `quasiYBE_of_hexagon` (PR #9519) exactly.

**Proved (sorry-free).**

- `quasiYBE_of_hexagons`: in any `ℚ`-algebra, for a `DK3` family `(a,b,c)`, the hexagons at
  `(a,b,c)` and at the leg-swapped `(a,c,b)` give
  `e(a)·φ(b,a)e(b)φ(c,b)e(c)φ(a,c) = φ(c,a)e(c)φ(b,c)e(b)φ(a,b)·e(a)`. Both sides equal
  `e(a)e(b+c)`; the Drinfeld–Kohno relation `[t₁₂, t₁₃+t₂₃] = 0` plays the role that
  quasi-cocommutativity plays in `quasiYBE_of_hexagon`.
- `quasiYBE_U4`, `quasiYBE_of_assocU4`: in `U4 N` the swapped hexagon follows from the universal
  one by `hexagon_of_universal` (the swapped family is `DK3` and lies in `Fil N 1`), so every
  rational associator in `U4 N` satisfies the quasi-Yang–Baxter equation
  `R₁₂Φ₃₁₂R₁₃Φ₁₃₂⁻¹R₂₃Φ₁₂₃ = Φ₃₂₁R₂₃Φ₂₃₁⁻¹R₁₃Φ₂₁₃R₁₂` there. The pentagon is not used.
- `quasiYBE_compatible_of_tower`: the compatible rational sequence of §17e satisfies it at every
  level `N ≥ 2`, conditional on `CompatibleGroupLikeKAssociatorTower K E`.
- `quasiYBE_of_realization`: for a `ℚ`-algebra map `ρ : U4 N → (A⊗A)⊗A` sending
  `e(t₁₂), e(t₁₃), e(t₂₃)` to `R₁₂, R₁₃, R₂₃`, the quasi-Yang–Baxter equation holds in
  `(A⊗A)⊗A` with the `ρ`-images of the rational associators. No coproduct is used.
- `hexagon_of_realization`, `quasiYBE_of_hexagon_realization`: if moreover
  `ρ(e(t₁₃+t₂₃)) = (Δ⊗id)(R)`, the hypothesis `hhex` of `quasiYBE_of_hexagon` is discharged with
  `P, Q, Φ` the `ρ`-images of `φ(t₁₃,t₁₂), φ(t₂₃,t₁₃), φ(t₁₂,t₂₃)`, and that theorem applies.

**Hypotheses that remain.** (i) The named analytic input `CompatibleGroupLikeKAssociatorTower`
(as in §17e). (ii) For a concrete `(A,Δ,R)`: the realisation map `ρ` and its three/four
compatibilities, plus quasi-cocommutativity for `quasiYBE_of_hexagon_realization`; no instance
is constructed. (iii) The braid relation `σ₁σ₂σ₁ = σ₂σ₁σ₂` with `σ₁ = s₁₂R₁₂`,
`σ₂ = Φ⁻¹s₂₃R₂₃Φ` needs the semidirect product with `S₃`; only its equivalent quasi-YBE form is
proved. (iv) `quasiYBE_of_hexagon`'s conclusion is stated with `τ₁₂(P)` etc.; identifying
`τ₁₂(ρ φ(t₁₃,t₁₂))` with `ρ φ(t₂₃,t₁₂)` needs `ρ` to intertwine `τ₁₂` with the `S₃` action on
`U4 N`, which is not proved (the universal theorem gives the permuted form directly).

**Verification.** `lean -DautoImplicit=false -s 65536` on `QuasiYBE.lean` exits 0 with no
output, against a symlink overlay of the restored cache, `fr/out`, `b1sbuild`, `gltbuild`,
`chainbuild`, `towerbuild` (later ones winning) plus a fresh `lean`-direct olean of
`HeckeTemperleyLieb/QuasiYangBaxterFromHexagon.lean`. (The plain colon-separated `LEAN_PATH` does
not work: Lean resolves a module under the first root containing a `QOU/` directory.)
`#print axioms` on all seven theorems shows only `propext`, `Classical.choice`, `Quot.sound`.
No `lake build` was run.

## 17g. The compatibility hypothesis dropped: Prop. 5.5 at one degree (bean `qou-3fdg`)

**Result.** `rational_associator_compatible_of_groupLikeTower`
(`RationalAssociator/AssociatorRealign.lean`, sorry-free): from `ε(E) = 1` and
`GroupLikeKAssociatorTower K E` alone (one group-like `K`-associator per level `N ≥ 2`, no
relation between levels) there is one sequence `Φ : ℕ → ℚ⟨X,Y⟩` with `Φ N` an associator in
`U4 N` for `E`, group-like modulo `FF2 N` (`N ≥ 2`), and `Φ (N+1) − Φ N ∈ FF N` (`N ≥ 1`). This
is the conclusion of `rational_associator_compatible_of_tower` (§17e) without
`CompatibleGroupLikeKAssociatorTower`; `rational_associator_compatible_of_tower_via_groupLike`
re-derives §17e's theorem through the new one.

**How.** Only the degree-by-degree form of Drinfeld's Prop. 5.5 is needed:

- `primDef_mem_of_GL_add`: if `A ≡ 1 (FF 1)` and `A`, `A + y` (`y ∈ FF d`, `d ≥ 1`) are both
  group-like modulo `FF2 (d+1)`, then `Δy − y⊗1 − 1⊗y ∈ FF2 (d+1)`.
- `exists_grt_layer` (**Prop. 5.5 at one degree**): two rational group-like associators
  `Φ + x`, `Φ + x'` in `U4 (d+1)` (`x, x' ∈ FF d`, `ε(Φ) = ε(E) = 1`) differ at degree `d` by a
  homogeneous primitive `h`, with `x' − x − h ∈ FF (d+1)` and `GrtU4 M h` for every `M`. The
  linear equations of `x' − x` cancel by `assocU4_add_iff`; primitivity comes from the previous
  lemma and `exists_primitive_layer`; `grtU4_of_lin_primitive` concludes.
- `realign`: a group-like `K`-associator at level `N ≥ d+1` agreeing with `1⊗Φ` modulo `FFK d`
  can be replaced, inside the group-like `K`-associators at level `N`, by one agreeing with
  `1⊗(Φ+x)` modulo `FFK (d+1)` for **any** prescribed rational group-like associator `Φ + x` in
  `U4 (d+1)`: `inductionStep_of_groupLike` gives some `x'`, then one shift by `exp(h)`
  (`assocK_shiftK`, `GLK.compKK_GK`, `compKK_congr`) with `h` from `exists_grt_layer` replaces
  `x'` by `x`.
- `LevelInv` / `levelStep`: the invariant only asks, at each level, for *some* `K`-associator
  agreeing with `1⊗Φ` modulo `FFK d`. The correction `x` is chosen at level `d+1` and every
  higher level is re-aligned onto it, so no cross-level relation between the `Ψ_N` is needed.

**Not proved.** Prop. 5.5 in its full form (for two group-like associators modulo `N`, a single
`g ∈ GRT₁` modulo `N` with `Φ' = Φ ∘ g`) is not stated; the composite of the per-degree shifts
would give it but the composition law of the truncated `GRT₁` action is not used here. The
analytic input `GroupLikeKAssociatorTower K E` itself is still a hypothesis; nothing constructs
it. `quasiYBE_compatible_of_tower` (§17f) still states the compatible-tower hypothesis; it can
now be restated on `GroupLikeKAssociatorTower` by composing with the new theorem (not done here).

**Verification.** `lean -DautoImplicit=false -s 65536` on `AssociatorRealign.lean` exits 0 with
no output against the symlink overlay holding every module up to `QuasiYBE`. `#print axioms` on
`rational_associator_compatible_of_groupLikeTower`, `exists_grt_layer`, `realign` and the
corollary shows only `propext`, `Classical.choice`, `Quot.sound`. No `lake build` was run.

## 17h. The one-degree lifting obstruction, and field independence (bean `qou-3fdg`)

Scope, per Carl's choice of "Furusho first": this section formalises the obstruction theory and
its field independence only. The general vanishing (an `H⁴`/`H³` argument in the Drinfeld–Kohno /
`grt` deformation complex) and explicit low-degree existence were **not attempted**; a separate
front is doing Furusho's pentagon ⇒ hexagons.

**Follow-up from §17g, done.** `quasiYBE_compatible_of_groupLikeTower` (`QuasiYBE.lean`) states
the quasi-Yang–Baxter conclusion of `quasiYBE_compatible_of_tower` on the weaker hypothesis
`GroupLikeKAssociatorTower K E`, by composing with `rational_associator_compatible_of_groupLikeTower`.
`QuasiYBE.lean` now imports `AssociatorRealign` instead of `AssociatorTower`.

**Proved (`RationalAssociator/Obstruction.lean`, sorry-free, purely algebraic over `ℚ`).**
Throughout `ε(E) = ε(Φ) = 1` and `d ≥ 1`; "a lift" means `x ∈ FF d` with `AssocU4 (d+1) E (Φ+x)`
and `GL (d+1) (Φ+x)`.

- `GL_add_iff`: `GL (d+1) (Φ + x) ↔ glDefect Φ + primDef x ∈ FF2 (d+1)`, with
  `glDefect Φ = ΔΦ − Φ⊗Φ`. The coproduct condition one degree up is linear in the correction,
  like the associator equations (`assocU4_add_iff`).
- `obsLin d : ℚ⟨X,Y⟩ →ₗ[ℚ] AssocTarget (d+1) × (F2⊗F2 ⧸ FF2 (d+1))`,
  `x ↦ (assocLin (d+1) x, [primDef x])`: the linearised inversion, hexagon and pentagon together
  with the linearised coproduct condition. `obstruction d E Φ = (−assocDefect (d+1) E Φ,
  [−glDefect Φ])`.
- `lift_iff_obsLin`: a lift exists **iff** `∃ x ∈ FF d, obsLin d x = obstruction d E Φ`.
- `lift_iff_homog`: equivalently with `x` homogeneous of degree `d` (`obsLin d` kills `FF (d+1)`).
- `lift_iff_primitive`: if `GL (d+1) Φ`, a lift exists iff there is `h ∈ FF d`, homogeneous of
  degree `d` and primitive, with `assocLin (d+1) h = −assocDefect (d+1) E Φ`. This is the form in
  the task statement; the extra hypothesis `GL (d+1) Φ` is needed, because when `Φ` is only
  group-like modulo `FF2 d` the correction must also cancel the degree-`d` group-likeness defect
  and is then not primitive.
- `liftSolvableOver_iff`, `lift_iff_liftSolvableOver`: for any nontrivial commutative
  `ℚ`-algebra `K` (any field `K ⊇ ℚ`, e.g. `ℂ`), the lifting equation is solvable after base
  change to `K` iff a rational lift exists (`exists_of_baseChange`, no finiteness used). The
  existence question at each degree is field-independent.
- `obstruction_mem_range_of_groupLikeK`: a group-like `K`-associator modulo `N ≥ d+1` agreeing
  with `1⊗Φ` modulo `FFK d` puts the obstruction in the range of `obsLin d` over `ℚ`.
- `AssociatorObstructionVanishes E` (a `def … : Prop`, **not an axiom, not proved**): for every
  `d ≥ 1` and every `Φ` with `AssocU4 d E Φ` and `GL d Φ`,
  `∃ x ∈ FF d, obsLin d x = obstruction d E Φ`.
  `compatible_of_obstructionVanishes`: this `Prop` alone (no field `K`) gives a sequence
  `Φ : ℕ → ℚ⟨X,Y⟩` with `AssocU4 N E (Φ N) ∧ GL N (Φ N)` for `N ≥ 1` and
  `Φ (N+1) − Φ N ∈ FF N`. The induction starts from `AssocU4 1 E 1` and `GL 1 1`.

**Not proved.** `AssociatorObstructionVanishes E` itself. Classically it follows from the KZ
associator plus `GRT₁`-transitivity; an algebraic proof would show the obstruction is a cocycle
and the relevant deformation cohomology vanishes, which Bar-Natan (1998) records as unknown.
The converse implication `GroupLikeKAssociatorTower K E → AssociatorObstructionVanishes E` is
also **not** formalised: it should follow from `realign` applied with target `Φ + 0` at each
degree below `d`, but that needs `AssocU4 M E Φ → AssocU4 N E Φ` for `N ≤ M` (a level map
`U4 M → U4 N`, surjective onto `Fil N 1`), which is not in the repository.

**Verification.** `lean -DautoImplicit=false -s 65536` exits 0 with no output (no warnings) on
`Obstruction.lean` and `QuasiYBE.lean`, against the symlink overlay plus freshly built
`AssociatorRealign`, `QuasiYBE` and `Obstruction` oleans. `#print axioms` on
`quasiYBE_compatible_of_groupLikeTower`, `GL_add_iff`, `lift_iff_obsLin`, `lift_iff_homog`,
`lift_iff_primitive`, `liftSolvableOver_iff`, `lift_iff_liftSolvableOver`,
`obstruction_mem_range_of_groupLikeK` and `compatible_of_obstructionVanishes` shows only
`propext`, `Classical.choice`, `Quot.sound`. The `RationalAssociator/` directory and this audit
are byte-identical between the verified base and `origin/main` after rebase. No `lake build`.
## 17i. Furusho: `μ² = 24c` in degree 2, and pentagon ⇒ hexagon modulo the Lie statement (bean `qou-3fdg`)

**Target.** Furusho (Ann. Math. 171 (2010)): a group-like `φ` satisfying the pentagon satisfies the
hexagons for a unique `μ`, with `μ² = 24 · (coefficient of [A, B])`. Then: restate the hypothesis
`GroupLikeKAssociatorTower` in a pentagon-only form.

**Proved** (`RationalAssociator/FurushoReduction.lean`, sorry-free, algebraic over `ℚ`):

- `hexagon_mu_iff`. With the `𝔱₃` relations, the hexagon for `φ_c = 1 + c[A, B]` and the
  truncated `exp(μx/2)` holds modulo degree 3 iff `(c − μ²/24)·[t₁₂, t₂₃] = 0`. This is Furusho's
  `μ² = 24c` in the lowest degree where it says anything.
- `truncU4`, `pentagon_trunc`, `AssocU4.trunc`: the truncation `U4 N → U4 M` for `M ≤ N`
  (generators to generators), and the pentagon and associator conditions descend along it.
- `assocU4_succ_of_pentagon`. One degree of the reduction. If `Φ` carries the level invariant at
  degree `d ≥ 1`, is group-like modulo `FF2 (d+1)`, and satisfies the pentagon in `U4 (d+1)`, then
  `PentagonHexagonLie d` makes it an associator in `U4 (d+1)`. Proof: `levelStep` gives a genuine
  associator `Φ + x`; `−x` is primitive modulo `FF2 (d+1)`; `exists_primitive_layer` gives its
  homogeneous primitive layer `k`; the defects of `Φ` are `−assocLin x = assocLin k`; the pentagon
  makes the pentagon component of `assocLin k` vanish; `PentagonHexagonLie d` kills the rest.
- `assocU4_of_pentagon`, `assocU4_iff_pentagon`. Induction from degree 3 (`levelInv_three` builds
  the invariant there from the tower). Under `GroupLikeKAssociatorTower K E` and
  `PentagonHexagonLie d` for all `d ≥ 3`: for `N ≥ 3` and `Φ` group-like modulo `FF2 N`,
  `AssocU4 N E Φ ↔ AssocU4 3 E Φ ∧ Pentagon_N Φ`.

**The remaining statement** is a `def … : Prop`, neither assumed as an axiom nor proved:

```lean
def PentagonHexagonLie (d : ℕ) : Prop :=
  ∀ h : F2, Homog d h → IsPrimitive h → (assocLin (d + 1) h).2.2 = 0 → assocLin (d + 1) h = 0
```

A homogeneous Lie element of degree `d` (primitive = Lie, by §17a) whose linearised pentagon
vanishes in `U4 (d+1)` satisfies all the linearised associator equations there. By hand
computation (not formalised): true at `d = 1`, and false at `d = 2`, where `h = [A, B]` has zero
linearised pentagon and linearised hexagon `−3[t₁₂, t₂₃]`. The `d = 2` failure is the `μ` freedom
that `hexagon_mu_iff` records; the reduction therefore starts at degree 3 and takes
`AssocU4 3 E Φ` as input. For `d ≥ 3` it is the Lie-algebra form of Furusho's theorem
(`grt₁` cut out by the pentagon alone, in degrees ≥ 3), which is a hard theorem and is not proved
here.

**What this does not do.** It does not shrink `GroupLikeKAssociatorTower` to a pentagon-only
hypothesis. Each step compares `Φ` with a genuine group-like `K`-associator taken from the tower,
so the hexagon enters through the tower. The result is that, given the tower and the Lie
statement, the hexagon is redundant for rational group-like solutions normalised in degree 2.
Whether Furusho's own group-level deduction also uses an existing associator (the KZ one) is not
settled here: the paper is not in `library/`, so I could not check.

**Verification.** `lean -DautoImplicit=false -s 65536` on `FurushoReduction.lean` exits 0 with
no output, against the symlink overlay used for §17g. `#print axioms` on `hexagon_mu_iff`,
`AssocU4.trunc`, `assocU4_succ_of_pentagon`, `levelInv_three`, `assocU4_of_pentagon` and
`assocU4_iff_pentagon` shows only `propext`, `Classical.choice`, `Quot.sound`. No `lake build`
was run. Does not touch `claude/grt-h4-2026-11-27` (quasiYBE restatement, lift obstruction).

**Relation to §17h.** §17h (`Obstruction.lean`, merged as #9815) states the remaining input of the
degree-by-degree construction as `AssociatorObstructionVanishes E`. That obstruction includes the
linearised hexagon. `PentagonHexagonLie` addresses a different question: whether the hexagon
part of the obstruction is implied by its pentagon part, for Lie elements of degree `d ≥ 3`. The
two statements are independent, and this file does not use `Obstruction.lean`.

## 17j. Furusho's Lie-algebra theorem proved for `d ≥ 3` (bean `qou-3fdg`)

**Target.** Discharge the one input §17i left as a named `Prop`:

```lean
def PentagonHexagonLie (d : ℕ) : Prop :=
  ∀ h : F2, Homog d h → IsPrimitive h → (assocLin (d + 1) h).2.2 = 0 → assocLin (d + 1) h = 0
```

**Proved** (sorry-free, algebraic over `ℚ`, three new files under `RationalAssociator/`):

```lean
theorem pentagonHexagonLie_of_three_le : ∀ d, 3 ≤ d → PentagonHexagonLie d
```

and, with that hypothesis discharged, the corollaries of §17i:

```lean
theorem assocU4_of_pentagon' {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : GroupLikeKAssociatorTower K E) {N : ℕ} (hN : 3 ≤ N) {Φ : F2}
    (h3 : AssocU4 3 E Φ) (hp : Pentagon Φ (t N 0) (t N 1) (t N 3) (t N 4) (t N 5))
    (hg : GL N Φ) : AssocU4 N E Φ
theorem assocU4_iff_pentagon' … (hg : GL N Φ) :
    AssocU4 N E Φ ↔ AssocU4 3 E Φ ∧ Pentagon Φ (t N 0) (t N 1) (t N 3) (t N 4) (t N 5)
```

(`K` any field with `[Algebra ℚ K]`.)

The proof follows the shape of Furusho's Lie-algebra argument (Ann. Math. 171 (2010), Thm 3),
written out for the repo's definitions:

1. `FurushoTwoCycle.lean`. A shift by a central element commutes with evaluating a Lie
   polynomial (`eval_add_left`, `eval_add_right`). From the linearised pentagon, the 2-cycle
   identity `h(X, Y) + h(Y, X) = 0` follows (`add_swap_eq_zero_of_pentagon`).
2. `FurushoP5.lean`. Five-strand families `P5`: their relabellings, their compositions, and
   the `DK4` family of the first four strands. The linearised pentagon becomes a five-term
   expression `piExpr` (`piExpr_eq`). The permutation sum `rSum_eq` gathers four relabelled
   pentagons into the hexagon polynomial `R(X, Y) = h(X, Y) + h(Y, −X−Y) + h(−X−Y, X)`
   (`rPoly`), evaluated at four pairs.
3. `FurushoHexagon.lean`.
   - It builds a concrete five-strand family on `ℚ⟨Y₁, Y₂, Y₃⟩ ⧸ FF3 N`, whose entries are a
     left multiplication plus a Leibniz map (`xE`, `xE_p5`). Commutation is checked on all 15
     disjoint pairs.
   - Each relabelling lifts `U4 N`, so the pentagon is zero there (`piExpr_eq_zero`). Summing
     gives `hexSum (rPoly h) ∈ FF3 (d+1)` (`hexSum_mem`).
   - Two substitutions to `ℚ⟨X, Y⟩`, homogeneity and the symmetries of `R` give
     `(2^{d−1} − 2)·R = 0`. So `R = 0` for `d ≥ 3` (`rPoly_eq_zero`).
   - Then `t₁₂ + t₁₃ + t₂₃` is central in the `t₁₂, t₁₃, t₂₃` subalgebra, and the shift of
     step 1 turns the linearised hexagon into `−R(t₁₂, t₁₃) = 0` (`lin513_eq_zero`). The
     (5.17) components follow from the 2-cycle.

The factor `2^{d−1} − 2` vanishes exactly at `d = 2`. That matches §17i's hand computation,
where `[A, B]` has zero linearised pentagon and nonzero linearised hexagon, so the theorem cannot
be extended below degree 3. The `μ` normalisation (`AssocU4 3 E Φ`) remains an input.

**Verification.** `lean -DautoImplicit=false -s 65536` on each of `FurushoTwoCycle.lean`,
`FurushoP5.lean`, `FurushoHexagon.lean` and `FurushoReduction.lean` exits 0 with no output.
This was run against the symlink overlay used for §17g–§17i. `#print axioms` on
`pentagonHexagonLie_of_three_le`, `rPoly_eq_zero`, `hexSum_mem`,
`add_swap_eq_zero_of_pentagon`, `lin513_eq_zero`, `assocU4_of_pentagon'` and
`assocU4_iff_pentagon'` gives `[propext, Classical.choice, Quot.sound]`. The files contain no
`sorry`, no `axiom`, no `native_decide` and no analytic constructs. No `lake build` was run.

**What remains open.** The Lie statement is now fully closed. What is still not reduced to
pentagon-only data:

- `GroupLikeKAssociatorTower K E` is still a hypothesis of `assocU4_of_pentagon'`. Each degree
  step compares `Φ` with a genuine `K`-associator from the tower (§17i, "What this does not do").
  Removing it would mean building the degree-`(d+1)` associator correction from the pentagon
  alone. §17h's `AssociatorObstructionVanishes E` is the corresponding open input of the
  construction route. The present theorem says that the hexagon part of that obstruction is
  implied by its pentagon part in degrees `d ≥ 3`.
- Furusho's group-level theorem (pentagon ⇒ hexagon for group-like `φ` with no associator given)
  is not formalised. Only its Lie-algebra form is.

## 17k. The lifting obstruction splits into a pentagon part and a group-level Furusho step (bean `qou-3fdg`)

**Target.** Attack the pentagon half of §17h's `AssociatorObstructionVanishes E`, aiming to remove
the `GroupLikeKAssociatorTower K E` hypothesis (a `K`-associator, classically KZ) from the
rational-associator chain.

**Result, in one line.** The hypothesis is not removed. It is replaced, with no field `K`, by two
named `Prop`s. For `d ≥ 3` the replacement is an exact equivalence, so nothing is lost by it.

**Proved** (`RationalAssociator/PentagonObstruction.lean`, sorry-free, algebraic over `ℚ`):

- `GL.mul`: group-likeness modulo `FF2 m` is closed under products over `ℚ`.
- `exists_GL_lift`: **the group-likeness half of the obstruction always vanishes.** For
  `ε(Φ) = 1`, `d ≥ 1` and `GL d Φ`, there is `x ∈ FF d` with `GL (d+1) (Φ + x)`. Proof: build
  `Ψ = Π expPoly(kᵢ)`, one homogeneous primitive `kᵢ` per degree, with `Ψ ≡ Φ` modulo `FF m` for
  `m = 1, …, d` (`GL_expPoly`, `primDef_mem_of_GL_add`, `exists_primitive_layer`,
  `expPoly_congr`). No logarithm and no `K`. This was not previously in the repository: §17h's
  `lift_iff_primitive` needed `GL (d+1) Φ` as a hypothesis.
- `ObstructionVanishesAt E d` (a `def … : Prop`): §17h's statement at one degree;
  `associatorObstructionVanishes_iff`: `AssociatorObstructionVanishes E ↔ ∀ d ≥ 1,
  ObstructionVanishesAt E d` (definitional).
- `obstructionVanishesAt_of_pentagon` (`d ≥ 2`):
  `PentagonLiftVanishes E d → FurushoGroupStep E d → ObstructionVanishesAt E d`.
- `furushoGroupStep_of_obstructionVanishesAt` (`d ≥ 3`): `ObstructionVanishesAt E d →
  FurushoGroupStep E d`. This uses `pentagonHexagonLie_of_three_le` (#9876). The vanishing gives
  a lift `Φ + x`. The primitive layer `k` of `x` has zero linearised pentagon, because `Φ` and
  `Φ + x` both satisfy the pentagon. So `assocLin k = 0`, and `Φ` was already an associator.
- `pentagonLiftVanishes_of_obstructionVanishesAt` (`d ≥ 1`), and so
  `obstructionVanishesAt_iff` (`d ≥ 3`):
  `ObstructionVanishesAt E d ↔ PentagonLiftVanishes E d ∧ FurushoGroupStep E d`.
- `compatible_of_pentagon_furusho`: a seed `Φ₃` with `AssocU4 3 E Φ₃` and `GL 3 Φ₃`, together
  with both `Prop`s for every `d ≥ 3`, gives `Φ : ℕ → ℚ⟨X,Y⟩` with `AssocU4 N E (Φ N)`,
  `GL N (Φ N)` and `Φ (N+1) − Φ N ∈ FF N` for every `N ≥ 3`. No `K` and no tower.

**The two remaining statements** (both `def … : Prop`, neither assumed nor proved):

```lean
def PentagonLiftVanishes (E : F2) (d : ℕ) : Prop :=
  ∀ Φ : F2, AssocU4 d E Φ → GL (d + 1) Φ →
    ∃ h ∈ FF d, Homog d h ∧ IsPrimitive h ∧
      Pentagon (Φ + h) (t (d + 1) 0) (t (d + 1) 1) (t (d + 1) 3) (t (d + 1) 4) (t (d + 1) 5)

def FurushoGroupStep (E : F2) (d : ℕ) : Prop :=
  ∀ Φ : F2, AssocU4 d E Φ → GL (d + 1) Φ →
    Pentagon Φ (t (d + 1) 0) (t (d + 1) 1) (t (d + 1) 3) (t (d + 1) 4) (t (d + 1) 5) →
      AssocU4 (d + 1) E Φ
```

- `PentagonLiftVanishes` is the pentagon (Drinfeld–Kohno / Stasheff) part. It asks for a Lie
  correction `h` of degree `d` that cancels the degree-`d` pentagon defect `ψ ∈ U(𝔱₄)`. Hexagon
  and inversion are not required of `Φ + h`. The hypothesis still carries `AssocU4 d E Φ`, the
  hexagon included, because a pentagon-only hypothesis could make the statement false. Whether
  pentagon solutions modulo `d` always lift is not settled here.
- `FurushoGroupStep` is Furusho's group-level pentagon ⇒ hexagon at a single degree. #9876 proved
  only the Lie-algebra form. The Lie form gives the converse direction above. It does not give
  this statement by itself, because the hexagon defect of `Φ` is nonlinear in `Φ`.

**What the equivalence says.** Once #9876 is in, the hexagon is redundant for the *obstruction
question*. In degrees `d ≥ 3`, a rational group-like associator modulo `d` lifts iff (i) its
pentagon defect can be cancelled by a Lie element, and (ii) pentagon-solutions one degree up are
automatically hexagon-solutions. Neither (i) nor (ii) mentions a field `K`.

**What was not done.**

- Neither `Prop` is proved. For (i), the natural route would show the defect `ψ` is a cocycle in
  `U(𝔱₅)` (the five relabelled pentagons, the 3-dimensional associahedron) and then that every
  such cocycle of degree `d` is `δ` of a Lie element of degree `d`. That is an `H⁴` vanishing
  statement for the pentagon complex. The cocycle step is not formalised here. The `H⁴` step is
  the known hard point.
- No explicit low-degree check (`d = 3, 4`) was run. Deciding equalities in `U4 (d+1)` needs a
  normal form for `U(𝔱₄)` truncated, and the repository has none.
- No converse from the tower: the repository does not show that `GroupLikeKAssociatorTower K E`
  implies `ObstructionVanishesAt E d` for arbitrary `Φ` (§17h, same gap: `AssocU4 M → AssocU4 N`
  for `N ≤ M` exists now as `AssocU4.trunc`, but the level invariant for an arbitrary `Φ` does
  not). So it is not checked inside Lean that the two `Prop`s are consistent with the tower.
- Literature. Furusho 2010 IS held: `library/arxiv-math-0702128v3/` (merged in #9836). Its INDEX
  row is titled "PENTAGON AND HEXAGON EQUATIONS" and does not name the author, so a grep for
  `furusho` in `library/INDEX.md` misses it. Theorem 1 there (§0, p. 1) is the group-level
  statement behind `FurushoGroupStep`; its proof is §2 (pp. 5-8). Drinfeld 1990 and Bar-Natan
  1998 are not in `library/` (INDEX and `ocr/` searched); their `H⁴` claims were not checked.

**Verification.** `lean -DautoImplicit=false -s 65536` on `PentagonObstruction.lean` exits 0 with
no output, against the `/home/claude/furov` symlink overlay. The `RationalAssociator/` directory is
byte-identical between the overlay's source branch (`b9d209162`) and `origin/main` after #9876.
`#print axioms` on `exists_GL_lift`, `GL.mul`, `obstructionVanishesAt_of_pentagon`,
`furushoGroupStep_of_obstructionVanishesAt`, `pentagonLiftVanishes_of_obstructionVanishesAt`,
`obstructionVanishesAt_iff` and `compatible_of_pentagon_furusho` gives
`[propext, Classical.choice, Quot.sound]`. The file has no `sorry`, no `axiom`, no
`native_decide` and no analytic constructs. No `lake build` was run.

## 17l. The group-level Furusho step: from any `K`-tower, and unconditionally for `E = 1` (bean `qou-3fdg`)

**Target.** Prove §17k's `FurushoGroupStep E d` for `d ≥ 3`, or as much of it as possible.

**Proved** (`RationalAssociator/FurushoGroupStep.lean`, sorry-free, algebraic over `ℚ`):

```lean
theorem levelInv_of_assocU4 {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : GroupLikeKAssociatorTower K E) {d : ℕ} (hd : 3 ≤ d) {Φ : F2}
    (hA : AssocU4 d E Φ) (hG : GL d Φ) : LevelInv K E d Φ
theorem furushoGroupStep_of_tower (hE) (hT : GroupLikeKAssociatorTower K E) (hd : 3 ≤ d) :
    FurushoGroupStep E d
theorem obstructionVanishesAt_of_tower (hE) (hT) (hd : 3 ≤ d) : ObstructionVanishesAt E d
theorem pentagonLiftVanishes_of_tower (hE) (hT) (hd : 3 ≤ d) : PentagonLiftVanishes E d
theorem groupLikeKAssociatorTower_one : GroupLikeKAssociatorTower K (1 : F2)
theorem furushoGroupStep_one (hd : 3 ≤ d) : FurushoGroupStep (1 : F2) d
theorem obstructionVanishesAt_one (hd : 3 ≤ d) : ObstructionVanishesAt (1 : F2) d
theorem pentagonLiftVanishes_one (hd : 3 ≤ d) : PentagonLiftVanishes (1 : F2) d
```

- `levelInv_of_assocU4` closes the gap §17k listed under "No converse from the tower": for
  `d ≥ 3`, **every** rational associator modulo `d` that is group-like modulo `FF2 d` carries the
  level invariant. The proof builds it at degree 3 (`levelInv_three`) and raises it one degree
  at a time with `LevelInv.succ_of_assoc`, feeding in the truncations `AssocU4.trunc` of `Φ`
  itself. So the tower implies all three of §17k's statements (`FurushoGroupStep`,
  `ObstructionVanishesAt`, `PentagonLiftVanishes`) at every `d ≥ 3`. This also checks inside Lean
  that the two `Prop`s of §17k are consistent with the tower.
- For `E = 1` (hexagon without exponential, i.e. `μ = 0`, the `GRT₁` case) the tower is inhabited
  by the constant `Ψ = 1`, over any `K` (`assocK_one`, `GLK_one`). Hence `FurushoGroupStep 1 d`,
  `ObstructionVanishesAt 1 d` and `PentagonLiftVanishes 1 d` hold for every `d ≥ 3` with no
  hypothesis. No existing associator, no KZ, no field other than `ℚ` is used.

**Relation to the source** (Furusho, arXiv math/0702128v3, §2 "Proof of Theorem 1", pp. 5-8,
read from `library/arxiv-math-0702128v3/sections/sec-002-2-proof-of-theorem-1.md`):

- Lemma 9 (pp. 6-7): a commutator group-like `φ` with `c₂(φ) = 0` satisfying the 5-cycle relation
  satisfies the 3-cycle relation (14). Its proof is an induction on degree: `φ ∈ GRT₁^{(n)}`, the
  corresponding Lie element `ψ` "also determines an element of `grt₁(k)`", `φ₁ = Exp ψ` agrees
  with `φ` modulo degree `n`, `φ = φ₂ ∘ φ₁` (Lemma 8), and Theorem 3 (the Lie form) puts the
  degree-`n` part of `φ₂` in `grt₁`. `furushoGroupStep_one` is that inductive step in the repo's
  terms. The comparison object is not `Exp ψ` but the degree-`(d+1)` lift `Φ + x` that `levelStep`
  produces by re-aligning `Ψ = 1` onto `Φ` through `Exp` of `grt` layers (`realign`), and the
  Lie form is `pentagonHexagonLie_of_three_le` (§17j). `obstructionVanishesAt_one` is the
  one-degree surjectivity onto `GRT₁^{(d)}` that Lemma 9 uses.
- Theorem 10 (pp. 7-8), the case `μ ≠ 0`: the proof passes to the weight-graded ring and uses
  "`Gr^W O(M₁)` is isomorphic to `O(GRT₁)` by [F06] theorem 6.2.2". [F06] is not in `library/`
  (not checked further), so whether that input itself rests on the existence of an associator is
  not settled from the held text. The held text does show that Theorem 10 is not a one-degree
  argument: it compares filtered coordinate rings of the two solution varieties.

**What is open.** `FurushoGroupStep E d` for `E ≠ 1` (`μ ≠ 0`) without a `K`-tower. It remains a
named `Prop`; this file proves it only from `GroupLikeKAssociatorTower K E` (classically the KZ
associator). The question "can the degree-`d` associator `Φ` of the hypothesis serve as the
comparison object" has a negative answer in the form attempted: the linearisation used throughout
(`assocDefect_add`) compares `Φ` with a degree-`(d+1)` associator congruent to it modulo `FF d`,
and `Φ` is only an associator modulo `d`, so it cannot be its own comparison object. The natural
next step is a one-degree version of Furusho's weight-filtration argument: show that the
`μ`-dependent part of the degree-`d` hexagon defect of `Φ` is determined by lower-degree data
already satisfying the equations, so that the `E = 1` step transfers. This is not attempted here.

**Verification.** `lean -DautoImplicit=false -s 65536` on `FurushoGroupStep.lean` exits 0 with no
output, against the `/home/claude/furov` overlay; `RationalAssociator/` is byte-identical between
the overlay's source (PR #9880 head `74e97b66c`) and `origin/main` after #9880 merged. `#print
axioms` on all eight theorems above gives `[propext, Classical.choice, Quot.sound]`. No `sorry`,
no `axiom`, no `native_decide`, no analytic constructs. No `lake build` was run.

## 17m. The `μ ≠ 0` group step is exactly one-degree existence (bean `qou-3fdg`)

**Target.** Prove `FurushoGroupStep E d` for `E ≠ 1` (`μ ≠ 0`), `d ≥ 3`, with no tower hypothesis.

**Result: not proved. A sharper reduction is proved, and it is an equivalence.** New file
`RationalAssociator/FurushoSingleLevel.lean`:

- `LevelInvAt K E d N Φ`: the level invariant of `AssociatorRealign.lean` at one level `N`.
- `levelInvAt_of_assoc`: one group-like `K`-associator modulo `N` aligns onto every rational
  associator `Φ` modulo `d ≤ N` (`realign`, one degree at a time along the truncations of `Φ`).
- `assocU4_succ_of_pentagon_at`: the reduction step of `FurushoReduction.lean` from the invariant
  at the single level `N = d + 1`. The step never used the levels above `d + 1`.
- `furushoGroupStep_of_exists_assocK`: `FurushoGroupStep E d` (`d ≥ 3`) from **one** group-like
  `K`-associator for `E` modulo `d + 1`. This replaces `GroupLikeKAssociatorTower K E` (every level)
  in `furushoGroupStep_of_tower` by one level.
- `assocK_of_assocU4`: base change of a rational associator.
- `furushoGroupStep_iff_exists`: for `d ≥ 3` and any one `Φ₀` satisfying the step's hypotheses,
  `FurushoGroupStep E d ↔ ∃ Ψ : ℚ⟨X,Y⟩, AssocU4 (d + 1) E Ψ ∧ GL (d + 1) Ψ`.

**What this means for `μ ≠ 0`.** When the step's hypothesis set is non-empty (which it is,
for example, whenever a rational associator modulo `d` exists and `PentagonLiftVanishes E d`
holds), the group-level Furusho step at degree `d` **is** the existence of one rational group-like
associator for `E` modulo `d + 1`. So any proof of the `μ ≠ 0` step, by a weight-filtration
argument or otherwise, is a proof of that existence statement, and conversely. Classically that
existence is Drinfeld's theorem (the KZ associator over `ℂ`, then descent, as in
`rational_associator_of_tower`); no algebraic proof of it is in the repository.

**Why the suggested route does not close, as attempted (scope (a)).** The weight-filtration
transfer from `E = 1` asks that the `μ`-dependent part of the degree-`d` hexagon defect be
determined by lower-degree data. By `pentagonHexagonLie_of_three_le` the defect of a
pentagon-solution is indeed a function of `Φ mod FF d` only (two degree-`d` corrections differ by a
primitive layer with zero linearised pentagon, hence zero linearised hexagon). But showing that
function vanishes at a `μ ≠ 0` point needs a comparison object at that `μ`: for `E = 1` it is
`Ψ = 1`; for `E ≠ 1` the `E = 1` objects cannot serve, because the `GRT₁` action preserves `μ`,
and rescaling `Φ(sA, sB)` moves `μ` to `sμ` and never to or from `0`. By
`furushoGroupStep_iff_exists` a comparison object at `μ` modulo `d + 1` is exactly what the step is
equivalent to. Furusho's Theorem 10 supplies it globally through `Gr^W O(M₁) ≅ O(GRT₁)` [F06,
6.2.2], which presupposes that `M₁` is a non-empty torsor. This is a negative about the route as
attempted, not a proof that no algebraic argument exists.

**What is open.** `FurushoGroupStep E d` for `E ≠ 1`, equivalently (given the hypotheses are
inhabited) `∃ Ψ, AssocU4 (d + 1) E Ψ ∧ GL (d + 1) Ψ` over `ℚ`, by an algebraic argument.

**Verification.** `lean -DautoImplicit=false -s 65536` on `FurushoSingleLevel.lean` exits 0 with
no output against the `/home/claude/furov` overlay (which carries `FurushoGroupStep.olean` from
#9887). `#print axioms` on all six theorems gives `[propext, Classical.choice, Quot.sound]`. No
`sorry`, no `axiom`, no `native_decide`, no analytic constructs. No `lake build` was run.

## 17n. The pentagon obstruction as a class; the whole degree-`d` step is one-degree existence (bean `qou-3fdg`)

**Target.** Prove `PentagonLiftVanishes E d` for `d ≥ 3` with no tower hypothesis, by the
algebraic route: the obstruction to lifting a pentagon solution one degree is a cocycle in a
cohomology group that vanishes (Drinfeld 1991 §5; Bar-Natan 1998).

**Result: not proved for `E ≠ 1` (scope (a)). A sharper reduction is proved.** (`E = 1` was
already unconditional: `pentagonLiftVanishes_one`, §17l, where the tower is built from `Ψ = 1`.)
New file `RationalAssociator/PentagonObstructionClass.lean`:

1. **The whole step at degree `d` is one-degree existence, for every `E` and every `d ≥ 1`.**
   - `obstructionVanishesAt_of_exists_assocK`: one group-like `K`-associator for `E` modulo
     `d + 1` gives `ObstructionVanishesAt E d` (`d ≥ 1`). It uses `levelInvAt_of_assoc` and
     `inductionStep_of_groupLike` at the single level `d + 1`; no other level and no use of the
     Lie-algebra Furusho theorem.
   - `obstructionVanishesAt_of_exists`, `pentagonLiftVanishes_of_exists`: the same over `ℚ`.
   - `obstructionVanishesAt_iff_exists`: given one rational associator modulo `d`, group-like
     modulo `FF2 d`, `ObstructionVanishesAt E d ↔ ∃ Ψ, AssocU4 (d + 1) E Ψ ∧ GL (d + 1) Ψ`.
   - `obstructionVanishesAt_of_exists_le`: existence modulo `N + 1` gives the step at every
     `1 ≤ d ≤ N`.

   So §17m's equivalence for the Furusho half extends to the full obstruction (pentagon part
   included), at `d ≥ 1` rather than `d ≥ 3`.

2. **The pentagon obstruction is a well-defined class.** `pentObs d E Φ` is the pentagon defect
   of `Φ` in `U4 (d + 1)`; `lieLayer d` is the submodule of homogeneous primitive (Lie) elements of
   degree `d`; `pentLin` is the linearised pentagon (Drinfeld's (5.20)); `pentCob d` is
   `pentLin (lieLayer d)`.
   - `pentagon_add_iff`: for `x ∈ FF d`, the pentagon for `Φ + x` modulo `d + 1` holds iff
     `pentObs Φ + pentLin x = 0`.
   - `pentagonLiftVanishes_iff_mem`, `pentagonLiftVanishes_iff_class`: `PentagonLiftVanishes E d`
     iff the class of `pentObs d E Φ` in `U4 (d + 1) ⧸ pentCob d` is zero for every `Φ` in its
     hypothesis set.
   - `pentObs_sub_mem`, `pentClass_eq`: that class depends only on `Φ` modulo degree `d` (among
     `Φ` group-like modulo `FF2 (d + 1)`).

**Why the cohomological route does not close here.** Two steps separate `pentClass` from the
statement "a cocycle in a group that vanishes", and neither is done:

- *The cocycle condition.* The pentagon defect satisfies the five-strand (Stasheff `K₅`) identity
  in `U(𝔱₅)`. Stating it needs a five-strand universal algebra `U5` and its five coface maps
  `U4 → U5`; the repository has `U4` only. This is mechanical but substantial, and it was not
  attempted in this tranche.
- *The vanishing.* The held source says it is not known. Drinfeld 1991, §5, p. 14
  (`library/drinfeld1991-quasitriangular/sections/page-014.md`), after Prop. 5.8, on the fourth
  cohomology `H⁴` of the relevant complex `L̄*`: *"The author does not know whether its 4th
  cohomology group H⁴ is equal to 0. It is easily seen that Hⁿ = Lⁿ = 0 for n < 2, dim H² =
  dim L² = 1, and H³ is the algebraic direct sum of the homogeneous components of grt₁."* So in
  the held literature the "obstruction lies in a vanishing group" route rests on an open
  question, and Drinfeld's own existence proof goes through the KZ associator.
- *Bar-Natan 1998 is not held.* `library/` has no copy of "On associators and the
  Grothendieck–Teichmuller group I" (`arxiv-q-alg-9707006v1` is a different paper, on the Drinfeld
  twist for quantum `su(2)`), and arXiv is blocked here. No claim in this section rests on it. My
  recollection, unchecked against the text, is that its rationality proof is a descent argument
  from an existing `ℂ`-associator, i.e. the route `exists_rational_lift` already formalises; that
  recollection should be checked before it is relied on.

**What is open.** For `E ≠ 1`: `pentClass d E Φ = 0`, equivalently (given a rational associator
modulo `d`) one-degree existence `∃ Ψ, AssocU4 (d + 1) E Ψ ∧ GL (d + 1) Ψ`, by an algebraic
argument. As a cohomological statement, it would need (i) `U5` and the `K₅` cocycle identity for
`pentObs`, and (ii) vanishing of the relevant degree-`d` part of `H⁴`, which Drinfeld records as
unknown in general.

**Verification.** `lean -DautoImplicit=false -s 65536` on `PentagonObstructionClass.lean`
exits 0 with no output against the `/home/claude/furov` overlay, after adding
`FurushoSingleLevel.olean` (#9888) to it. `#print axioms` on all ten theorems gives `[propext,
Classical.choice, Quot.sound]`. A deliberately false `example : (2 : ℚ) = 3 := by norm_num`
in the same check file fails (so the check is live) and was removed. No `sorry`, no `axiom`, no
`native_decide`, no analytic constructs. No `lake build` was run.

## 17o. The KZ fallback: the fixed-`E` tower is false at `μ ≠ 0`, and the per-level target (bean `qou-3fdg`)

File: `QOU/Transcendental/BraidsAndKnots/KZTowerTarget.lean` (new). It is behind the
transcendental boundary because it is the interface to the analytic KZ construction. It
contains no analysis: no limit, integral, `exp`, `π` or `ζ`.

**What already exists, and why it does not discharge the descent.** `AssociatorKZ.lean` builds
`Φ_KZ` as a connection matrix. `DrinfeldAssociator.lean` packages it as
`structure Associator` (`kz : Associator`, line 134), and `KZPentagon` / `KZHexagon` prove
the pentagon and the hexagon (in the central `e^{πi·}` form) in complete normed `ℂ`-algebras,
for non-resonant arguments. Four pieces are missing to obtain `AssocK ℂ N E Ψ ∧ GLK ℂ N Ψ`:
(i) a complete normed structure on the truncated free algebra `ℂ ⊗ ℚ⟨X, Y⟩ / (deg ≥ N)`;
(ii) group-likeness, which is not a field of `Associator`; (iii) matching the `e^{πi·}`
hexagon convention to `E = exp(t/2)` by rescaling the arguments by `2πi`; (iv) realising
`Φ_KZ` there as a polynomial `Ψ`. None of these is attempted in this tranche.

**The main finding: `GroupLikeKAssociatorTower K E` cannot hold for the exponential case.**
The tower fixes one polynomial `E` for every level `N`.

- `hexagon_sq_eq`: if `AssocU4 N E Φ`, then in every commutative `ℚ`-algebra, for every `y` with
  `y ^ N = 0`, `(E(2y))² = (E(y))⁴`, where `E(x) = eval x 0 E`. Proof: send all six generators
  `tᵢⱼ` to `y` (`diagMap`). The hexagon becomes `E(2y) = F·e·F·e·F`, with `F = Φ(y, y)` and
  `e = E(y)`, and inversion gives `F² = 1`.
- `not_assocU4_expHalfPoly`: for `expHalfPoly = 1 + X/2 + X²/8` and `N ≥ 4`, no `Φ` exists.
  The witness is `y = 8z` in `ℚ[X]/(X⁴)`:
  `(1 + 8z + 32z²)² − (1 + 4z + 8z²)⁴ = −128z³ + (z⁴-terms)`, and `z³ ≠ 0`.
- `not_groupLikeKAssociatorTower_expHalfPoly`: the tower hypothesis for `expHalfPoly` is false
  over every field `K`.
- `not_exists_assocK_expHalfPoly_four`: so is the single-level form at level `4`.
- `tower_forces_square_law`: any tower forces the square law at every nilpotency order.
  Informally, this makes `x ↦ E(x, 0)` an exact exponential series, which a polynomial is only
  when `E = 1` (`μ = 0`). That general claim is argued, not formalised. Only the `expHalfPoly`
  case is formalised.

**Consequence for §17d–§17n.** Every theorem that takes `GroupLikeKAssociatorTower K E` as a
hypothesis is vacuous for `E = expHalfPoly`. The same holds for any `μ ≠ 0` polynomial `E`, by
the informal argument above. The `E = 1` results (§17l) are unaffected. The open item of §17n,
one-degree existence `∃ Ψ, AssocU4 (d + 1) E Ψ ∧ GL (d + 1) Ψ` for a fixed `E ≠ 1`, is
**false** for `E = expHalfPoly` at `d + 1 ≥ 4`. The right open item takes `E` to be the
level-`(d + 1)` truncation of `exp(X/2)`. I have not changed `GroupLikeKAssociatorTower` (a core
definition); that change is escalated to the coordinator.

**The per-level target.** `expHalfTrunc N = Σ_{k<N} X^k / (2^k k!)` is exact in `U4 N`.

- `class KZAssociatorExists (K)` requires, for every `N ≥ 2`,
  `∃ Ψ : K ⊗[ℚ] F2, AssocK K N (expHalfTrunc N) Ψ ∧ GLK K N Ψ`. This is a **conditional
  hypothesis with content**. It is Drinfeld's KZ theorem for `K = ℂ`, rescaled. No instance is
  declared, and it is not proved here.
- `rational_associator_of_kz`: under the class, for every `N ≥ 2` there is a rational `Φ` with
  `AssocU4 N (expHalfTrunc N) Φ ∧ GL N Φ` (via `rational_associator_of_groupLikeK`). This is
  conditional.
- Unconditionally: `assocU4_three` and `GL_three` show that `1 + [X, Y]/24` is a rational
  associator modulo `3` for `expHalfTrunc 3 = expHalfPoly`, group-like modulo `FF2 3`.
  `kzLevel_three` follows: the class's field holds at `N = 3` over every field `K`, with no
  analysis. Level `2` was not stated separately.

**What remains open.** Levels `N ≥ 4` of `KZAssociatorExists`, by any route. The
analytic route needs (i)–(iv) above. The algebraic route needs the one-degree step of §17n
restated for per-level `E`, with `E` changing between the truncations. The existing lift
machinery (`assocU4_add_iff`, the pentagon class) takes a fixed `E`, so it would need a
version where `E` changes by a degree-`N` term between levels.

**Verification.** `lean -DautoImplicit=false -s 65536 KZTowerTarget.lean` exits 0 with no
output against the `/home/claude/furov` overlay. `#print axioms` on all fifteen public
theorems gives `[propext, Classical.choice, Quot.sound]`. A false `example : (2 : ℚ) + 2 = 5
:= by norm_num` appended to the file fails (`⊢ False`), so the check is live; it was removed.
No `sorry`, no `axiom`, no `native_decide`, no `: True`. No `lake build` was run.
`scripts/transcendental-boundary-audit.py --check` reports `new 0`. It exits 1 only because of
353 `GONE` entries: files absent from this sparse worktree, not changed by it. `QOU.lean`
imports the new module.

## 17p. The hexagon exponential is per level (owner ruling 2026-11-28, bean `qou-3fdg`)

**Ruling.** Owner card tap, 2026-11-28 01:04Z. The card asked *"Change the tower so E is exp(X/2)
truncated at each level?"* and the owner chose *"Yes, per-level E"*. Recorded in
`docs/coordination/owner-rulings.md`. It answers the escalation at the end of §17o.

**What changed (one definition, reformulated; no parallel copy).**

| | before | after |
|---|---|---|
| `GroupLikeKAssociatorTower K E` | `E : F2`; `∀ N ≥ 2, ∃ Ψ, AssocK K N E Ψ ∧ GLK K N Ψ` | `E : ℕ → F2`; `∀ N ≥ 2, ∃ Ψ, AssocK K N (E N) Ψ ∧ GLK K N Ψ` |
| `LevelInv K E d Φ` | uses `AssocK K N E` | `E : ℕ → F2`, uses `AssocK K N (E N)` |
| `rational_associator_of_tower` | `(hE : ε(E) = 1)`, gives `AssocU4 N E Φ` | `(hE : ExpFamily E)`, gives `AssocU4 N (E N) Φ` |
| `expHalfTrunc` and the level-3 results | `Transcendental/…/KZTowerTarget.lean` | `RationalAssociator/ExpHalfTrunc.lean` (algebraic, no analysis imported) |

New in `AssociatorChain.lean`: `structure ExpFamily (E : ℕ → F2)`, with fields `const` (`ε(E N) = 1`
for `N ≥ 1`) and `compat` (`E (N + 1) − E N ∈ FF N`). Also `ExpFamily.sub_mem`,
`ExpFamily.assocU4_iff` (for `N ≤ M`, `AssocU4 N (E M) Φ ↔ AssocU4 N (E N) Φ`), `ExpFamily.assocK`
and `expFamily_const`. These rest on `eval_congr_of_sub_mem_FF` and `AssocU4.congr_exp`: two
exponentials that agree modulo `FF N` give the same hexagon in `U4 N`.

The theorems below now take a family `E : ℕ → F2` with `ExpFamily E`, and level `N` uses `E N`:

- `levelStep` and `rational_associator_compatible_of_groupLikeTower` (`AssociatorRealign`);
- `assocU4_succ_of_pentagon`, `LevelInv.congr`, `LevelInv.succ_of_assoc`, `levelInv_three`,
  `assocU4_of_pentagon` and `assocU4_iff_pentagon` (`FurushoReduction`);
- `assocU4_of_pentagon'` and `assocU4_iff_pentagon'` (`FurushoHexagon`);
- `quasiYBE_compatible_of_groupLikeTower` (`QuasiYBE`);
- `levelInv_of_assocU4`, `furushoGroupStep_of_tower`, `obstructionVanishesAt_of_tower` and
  `pentagonLiftVanishes_of_tower` (`FurushoGroupStep`).

`FurushoGroupStep` also gains `exists_lift_of_tower`. It lifts an associator for `E d` modulo `d`
to one for `E (d + 1)` modulo `d + 1`, with correction in `FF d`.

The one-degree `Prop`s (`ObstructionVanishesAt`, `FurushoGroupStep`, `PentagonLiftVanishes`) keep
a single exponential, and the tower results instantiate them at `E (d + 1)`. `LevelInvAt`
(`FurushoSingleLevel`) is single-level and keeps a fixed `E`.

**Kept as the `E = 1` special case.** `expFamily_one : ExpFamily (fun _ => 1)` and
`groupLikeKAssociatorTower_one : GroupLikeKAssociatorTower K (fun _ => 1)`. `furushoGroupStep_one`,
`obstructionVanishesAt_one` and `pentagonLiftVanishes_one` (`GRT₁`, §17l) keep their statements
unchanged and are re-proved through the constant family.

`CompatibleGroupLikeKAssociatorTower` (`AssociatorTower`) is still fixed-`E`. Its `toTower` now
lands in the constant family `fun _ => E`, and its docstring says that it is vacuous for an
exponential of positive degree. It is kept for `E = 1`. It was not converted to per-level form;
that is a follow-up if anything needs it.

**The top-degree difference** (`ExpHalfTrunc.lean`):

- `expHalfTrunc_succ_sub`: `expHalfTrunc (N+1) − expHalfTrunc N = X^N / (2^N N!)`. Hence
  `expFamily_expHalfTrunc`.
- `assocDefect_add_exp`: take `d ≥ 1`, `ε(E) = ε(Φ) = 1` and `D ∈ FF d`. Then in `U4 (d + 1)`,
  `assocDefect (d+1) (E + D) Φ` equals `assocDefect (d+1) E Φ` plus
  `(0, D(t₁₃ + t₂₃) − D(t₁₃) − D(t₂₃), 0)`. The inversion and pentagon components do not move.
  The hexagon component moves by an explicit degree-`d` term, since all cross terms with `δ` vanish
  modulo `d + 1`.
- `assocDefect_expHalfTrunc_succ`: the case `E = expHalfTrunc d`, where the added term is
  `((t₁₃ + t₂₃)^d − t₁₃^d − t₂₃^d) / (2^d d!)`. This is the right-hand-side shift that a
  degree-by-degree solver for `μ ≠ 0` has to absorb when moving from level `d` to level `d + 1`.

**Non-vacuity at the first step.** `assocU4_three_expHalfTrunc_four`: `1 + [X, Y]/24` is an
associator modulo `3` for the level-`4` exponential. Together with `GL_three`, this means the
hypotheses of `exists_lift_expHalfTrunc_of_tower`, `obstructionVanishesAt_expHalfTrunc_of_tower`,
`furushoGroupStep_expHalfTrunc_of_tower` and `pentagonLiftVanishes_expHalfTrunc_of_tower` are met
at `d = 3`, apart from the tower itself. Under the old definition the analogous tower
(`fun _ => expHalfPoly`) is **false** (`not_groupLikeKAssociatorTower_expHalfPoly`). The new one,
`GroupLikeKAssociatorTower K expHalfTrunc`, is not refuted by `hexagon_sq_eq`:
`tower_forces_square_law` is now stated per level, and `expHalfTrunc M` is the exponential modulo
degree `M`.

**KZ.** `kzAssociatorExists_iff_tower`: `KZAssociatorExists K ↔ GroupLikeKAssociatorTower K
expHalfTrunc`. `rational_associator_of_kz` now goes through `rational_associator_of_tower
expFamily_expHalfTrunc`.

**What remains open.**

- **Inhabiting `GroupLikeKAssociatorTower K expHalfTrunc`** (equivalently `KZAssociatorExists K`)
  over any field. This is Drinfeld's theorem and needs (i)–(iv) of §17o. Not proved.
- **Any level `≥ 4` unconditionally.** No associator for `expHalfTrunc 4` modulo `4` is
  constructed. The candidate `1 + [X, Y]/24` plus a degree-3 correction would need an explicit
  computation in `U4 4`, which was not attempted.
- **The `μ ≠ 0` degree-`d` step now has a non-vacuous statement** whose hypotheses are met at
  `d = 3`. That step is `∃ x ∈ FF d` lifting an associator for `E d` modulo `d` to one for `E (d+1)`
  modulo `d + 1`. It is proved only **from the tower**. An unconditional algebraic proof would
  solve the linear system of `assocU4_add_iff`, shifted by `assocDefect_expHalfTrunc_succ`, using
  §17j–§17n. Not done.

**Verification.** Every changed module and its downstream consumers were recompiled lean-direct
(`lean -DautoImplicit=false -s 65536`), in dependency order, against a private overlay
(`/home/claude/furov-pl`), and all exit 0:

- `AssociatorChain`, `AssociatorTower`, `AssociatorRealign`, `Obstruction`, `FurushoReduction`,
  `QuasiYBE`, `FurushoTwoCycle`, `FurushoP5`, `FurushoHexagon`, `PentagonObstruction`,
  `FurushoGroupStep`, `FurushoSingleLevel`, `PentagonObstructionClass`, `ExpHalfTrunc`;
- `Transcendental/BraidsAndKnots/KZTowerTarget`;
- `HAdicDrinfeld/Hexagon`, after building `HAdicDrinfeld/CasimirData` and `FourStrand`.

`#print axioms` on the key theorems gives `[propext, Classical.choice, Quot.sound]`. The theorems
checked are:

- `rational_associator_of_tower`, `levelStep`, `exists_lift_of_tower`,
  `obstructionVanishesAt_of_tower`;
- the three `_one` results, `assocU4_iff_pentagon`, `assocU4_iff_pentagon'`,
  `quasiYBE_compatible_of_groupLikeTower`;
- `expFamily_expHalfTrunc`, `assocDefect_add_exp`, `assocDefect_expHalfTrunc_succ`,
  `assocU4_three_expHalfTrunc_four`;
- `not_groupLikeKAssociatorTower_expHalfPoly`, `tower_forces_square_law`,
  `KZAssociatorExists.tower` and `rational_associator_of_kz`.

The check is live. In a scratch file, the true identity `expHalfTrunc 4 − expHalfTrunc 3 = 48⁻¹ •
X³` passes, the false variant with `24⁻¹` fails with an unsolved goal, and the scratch file was
deleted. There is no `sorry`, `axiom`, `native_decide` or `: True`, and no `lake build` was run.
`scripts/transcendental-boundary-audit.py --check` reports `outside boundary: 378 (baseline 378),
new 0, gone 0`.

## 17q. Explicit rational associators modulo 4 and 5 on the per-level tower (bean `qou-3fdg`)

§17p left open "any level ≥ 4 unconditionally". This section closes levels 4 and 5 by explicit
construction, with `E N = expHalfTrunc N` (the per-level exponential of §17p). Write `X, Y` for the
two free generators of `F2`, and `L = [X, Y]`.

**Results (sorry-free, lean-direct).**

- Level 4, in `ExplicitLevelFour.lean`:
  `exists_assoc_GL_four : ∃ Φ : F2, AssocU4 4 (expHalfTrunc 4) Φ ∧ GL 4 Φ`, witnessed by
  `assocU4_four : AssocU4 4 (expHalfTrunc 4) (phiPoly (1 / 24))` and
  `GL_four (c : ℚ) : GL 4 (phiPoly c)`. So

      Φ ≡ 1 + L/24            (mod words of length 4)

  with **no degree-3 term**. The degree-3 hexagon defect of the level-3 associator is cancelled by
  the new `X³/48` term of `expHalfTrunc 4`.
- Level 5, in `ExplicitLevelFiveAlg.lean` and `ExplicitLevelFive.lean`:
  `exists_assoc_GL_five : ∃ Φ : F2, AssocU4 5 (expHalfTrunc 5) Φ ∧ GL 5 Φ`, witnessed by
  `assocU4_five : AssocU4 5 (expHalfTrunc 5) phi5Poly` and `GL_five : GL 5 phi5Poly`, where

      Φ₅ ≡ 1 + L/24 + L²/1152 − [X,[X,L]]/1440 − [Y,[X,L]]/5760 − [Y,[Y,L]]/1440
                                                                 (mod words of length 5).

The coefficients are solutions of the hexagon, pentagon and inversion equations. They were not
fitted, and no measured value enters. As a remark only, not used anywhere: `1/1440 = ζ(4)/(2π)⁴`
and `1/24 = ζ(2)/(2π)²`. Whether these match the KZ associator's coefficients in this
normalisation was not checked.

**The solution space (probe only).** `computations/audits/rational_associator_level4_probe.py`
solves the degree-3 and degree-4 equations by hand in exact `Fraction` arithmetic. It uses the
eleven Drinfeld–Kohno rewriting rules, whose normal words are the PBW basis
`U(f₃) ⊗ U(f₂) ⊗ U(f₁)`. Output: `ALL CHECKS PASS`.

- Degree 3 has a one-parameter family `1 + L/24 + α([X,L] + [Y,L])`, with `α ∈ ℚ` free. This is
  the GRT direction of §17j–§17n. The Lean proves the case `α = 0`.
- Degree 4, for `α = 0`, is **unique** (kernel rank 0) and equals the Lie form above.
- Control: with `expHalfTrunc 3`, `1 + L/24` fails the degree-3 hexagon.

**Method.** In the abstract layer, `R` is any `ℚ`-algebra. The truncation hypotheses `Trunc4` and
`Trunc5` say that 4-fold and 5-fold right-associated products vanish. The three-strand and
four-strand relations enter as rewriting rules, obtained from the `DK4` commutation fields by
`rule_of_commute`.

- Hexagon and inversion are proved by expanding, truncating, rewriting to normal form and then
  `module`.
- The level-5 pentagon first removes every cross term of degree at least 5, using `Fil`
  multiplicativity in `U4 5` (`mul_two_of`, `mul_three_of`). This leaves the linear identity
  `pentagon5_lin`, which takes the 22 rule instances as hypotheses and needs no truncation.
- The concrete theorems instantiate the abstract ones at `t 4 i` and `t 5 i`, discharging the
  truncation by `trunc4_fil` and `trunc5_fil`.

**Verification.**

- Every new module compiles lean-direct (`lean -DautoImplicit=false -s 65536`) against a private
  overlay, exit 0. `ExplicitLevelFiveAlg` takes about 4 min; the other two take seconds.
- `#print axioms` on `exists_assoc_GL_four`, `assocU4_four`, `GL_four`, `hexagon4_central`,
  `exists_assoc_GL_five`, `assocU4_five`, `GL_five`, `hexagon5` and `pentagon5_lin` gives
  `[propext, Classical.choice, Quot.sound]`.
- The check is live. In scratch files outside the repo:
  - level 4: the same hexagon proof with `phi (1/12)` fails (`ring failed`);
  - level 5: changing the `[X,[X,L]]` coefficient from `1/1440` to `1/1400` makes
    `inversion5`, `hexagon5` and `pentagon5_lin` all fail (`ring failed`).
- There is no `sorry`, `axiom`, `native_decide` or `: True`, no analysis import, and no
  `lake build` was run.

**What remains open.**

- **Level ≥ 6.** It is not proved. The method extends, but the `module` normalisation grows quickly:
  the level-5 pentagon needed the cross-term elimination to finish at all.
- **The general degree-`d` step** (§17n one-degree existence), and so the full tower. Inhabiting
  the tower `∀ N, ∃ Φ, AssocU4 N (expHalfTrunc N) Φ ∧ GL N Φ` is still open. Levels 4 and 5 are
  separate witnesses, not a coherent tower. `Φ₅` does reduce to `Φ₄` modulo 4, but that
  compatibility is not stated in Lean.
- **The α-family.** That `α` is free is a probe result. Only `α = 0` is in Lean.
- **Confluence.** That the eleven rewriting rules are confluent, so that the PBW normal form is
  unique, is checked by the probe only. The Lean proofs do not depend on it: each identity is
  closed by `module` after rewriting, so the Lean stands alone.
