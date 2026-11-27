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

**Still open (bean `qou-3fdg`).**

1. Lifting the evaluation-level closure to an element `g₁ ∘ g₂` of the truncated free algebra
   (substitute `G a G'` for `A` in `g₁`). This is needed for the pentagon and hexagon to apply
   to the composite as a polynomial.
2. The flow argument of Route A, and with it (S4). Two pieces are missing:
   - the derivative of each condition along `g ↦ g ∘ (1 + εy)`;
   - uniqueness for the resulting linear equation in the graded nilpotent setting.
3. The congruence `Φ ∘ g ≡ Φ + y`.
