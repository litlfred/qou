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
