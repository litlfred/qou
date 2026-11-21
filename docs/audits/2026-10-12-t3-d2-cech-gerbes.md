# T3 / design D2: Čech-cocycle gerbes and a cocycle-level Yekutieli Thm 4.17

Bean `qou-0xk8` (parent `qou-533l`). Branch `t3-d2-cech`. Date 2026-10-12.

**File:** `folio/quantum-observable-universe/lean/QOU/MathlibExt/CechGerbe.lean`
(517 lines, imports the T2b file `PresheafCentralExtensionObstruction.lean`).

## Verdict

D2 is **feasible and is done for the class of gerbes it can represent**. The
cocycle-level Thm 4.17 is proved sorry-free in two forms, exact and up to
isomorphism. Its cost is the one the design accepted going in: **the
equivalence between a gerbe and its cocycle data is assumed, not proved**. A
second, narrower cost turned up during the work: the model covers only gerbes
bound by `lien(𝒢)` with a **central** twist. Non-inner outer twisting
(Giraud's general non-abelian 2-cocycles `(λ_ij, g_ijk)`) is not covered.

## Verification (measured this session)

- `lean -DautoImplicit=false -s 65536 CechGerbe.lean` gives **exit 0**, with 0
  errors and 0 warnings. It was compiled against a private hardlinked Mathlib
  olean tree (`olean-d2`) with the T2b olean built alongside it. No `lake build`
  was run.
- There are **0 real `sorry`s**. The one textual hit is the word "sorry-free"
  in the module docstring. There are no `axiom` declarations and no
  `native_decide`.
- `#print axioms` on all 11 headline declarations returned only `propext`,
  `Classical.choice` and `Quot.sound`. The log is in
  `/tmp/d2-cech-axioms.log` (container-local).
- Not run: `scripts/lean-library-sweep.py`. The check is container-scoped
  lean-direct only.

## What is proved

The formalism is Mathlib's `CategoryTheory.Sites.NonabelianCohomology.H1`
1-cochains on a family `U : I → C`, plus T2b's `TwoCochain`.

| declaration | content |
|---|---|
| `core_*_tw` | the group-theoretic core of T2b, re-done with a central twist `τ` |
| `TwoCocycle`, `TwoCocycle.one` | Čech 2-cocycles: the cocycle model of a gerbe banded by abelian `𝒜` |
| `TwoCocycle.Rel`, `equivalence_rel` | differing by a coboundary; an equivalence relation when `𝒜` is commutative |
| `H2`, `TwoCocycle.class`, `class_eq_iff`, `class_eq_one_iff` | Čech `H²(U, 𝒜)` as a quotient; a class is trivial iff it is a coboundary |
| `TwistedCocycle ζ β` | global objects, presented on `U`, of the gerbe `H_β` bound by `lien(𝒢)` with central twist `β` (a 2-cochain of `𝒵`, with `ζ : 𝒵 ⟶ 𝒢`): `g_ij g_jk = ζ(β_ijk) g_ik` |
| `TwistedCocycle.ev_trans_of_rel` | isomorphisms (Mathlib `OneCohomologyRelation`) preserve the twist, so they are the gerbe's isomorphisms |
| `TwistedCocycle.retwist` | cohomologous twists `β' = β·∂t` give corresponding objects `ζ(t)·g` |
| `CentralGerbeExtension` | Yekutieli Def 3.21 in this model: a T2b central extension `1 → 𝒜 → 𝓔 → 𝒢` together with a central lift `ζE : 𝒵 ⟶ 𝓔` of `ζG` |
| `pushTw` | the functor `F = π_* : G_β → H_β` on objects |
| `obstruction`, `obstruction_spec` | Yekutieli's Construction (`const1`): `ξ_ij ξ_jk = ι(c_ijk) ζE(β_ijk) ξ_ik` for a local lift `ξ` |
| `obstruction_cocycle` | `c` is a Čech 2-cocycle; this uses `β` being a cocycle and `ζE` being central |
| `obstruction_lift_change`, `cl2_indep` | the class `cl²_F(g) ∈ H²(U,𝒜)` does not depend on the local lift (Def 4.15) |
| `exists_lift_iff`, `cl2_eq_one_iff` | **Thm 4.17, exact form:** `g = π_* η` for some `η ∈ G_β(X)` iff `cl²_F(g) = 1` |
| `exists_iso_lift_iff` | **Thm 4.17 as stated:** there is `η ∈ G_β(X)` with `H_β(X)(Fη, g) ≠ ∅` iff `cl²_F(g) = 1`, under `hsurj` (see below) |

Setting `β = 1` recovers the T2b torsor statement.

## What is ASSUMED, or not covered

1. **Gerbe ≃ cocycle data is assumed.** Nothing proves that a gerbe (a stack)
   is equivalent to its Čech data on some cover. In particular nothing proves
   that every gerbe bound by `lien(𝒢)` admits a twisting cocycle, that the
   model is cover-independent up to refinement, or that a stack's
   objects and morphisms are recovered from twisted cochains. Nikolaus–Waldorf
   (`library/arxiv-1103.4815v3`) prove equivalences of this kind for
   **smooth** gerbes with a Lie 2-group / crossed-module band. Their cocycle
   data (`g_ij ∈ G`, `f_ijk ∈ H`, `g_ij g_jk = t(f_ijk) g_ik`) appears to
   specialise to ours with the crossed module `𝒵 → 𝒢` and trivial action. That
   was not checked line by line, and their theorems are about manifolds, not a
   general site `C`.
2. **Only central twists.** Bands with non-inner outer twisting are out of
   scope.
3. **The local lift is a hypothesis** (`ξ`, `hξ`). It is the counterpart of
   Yekutieli's "`cl²_F(j)` is defined". The model does not prove sufficient
   conditions for it (Yekutieli Thm 5.11).
4. **`hsurj` in `exists_iso_lift_iff`.** It requires that sections of `𝒢` over
   each cover member `U i` lift to `𝓔`, and it is used only in the forward
   direction. It is an artefact of the cocycle model, which fixes the local
   objects: Yekutieli re-chooses the `i_k`, the model cannot. The exact form
   `cl2_eq_one_iff` needs no such hypothesis.
5. **The cover is fixed.** Classes live in `Ȟ²(U, 𝒜)` for a single family `U`,
   with no colimit over refinements. T2b's `isCoboundary_pull` shows that
   vanishing survives refinement, but this file does not lift that to `H2`.

## Comparison with D1 / D3

- **D2 versus D1** (gerbes as stacks / fibred categories): D2 avoids all stack
  machinery, which is why it closes. It does so by assuming exactly the
  equivalence D1 would have to build. If D1 lands, it should state the
  comparison theorem that turns item 1 above from an assumption into a result.
  D2 is then its cocycle shadow.
- **D2 versus D3:** not assessed here, because this agent did not see D3's
  output.
- **D2's own value:** the cocycle-level statement is what any consumer actually
  computes with, and it is a faithful generalisation of T2b. Its limits are
  items 1 and 2.

## Not done / follow-ups

- Lift `isCoboundary_pull` (refinement) to `H2`, giving cover-independence of
  `cl2` up to a common refinement.
- Yekutieli Prop 4.16 (isomorphic objects have equal classes). In this model it
  needs `hsurj` for the same reason as item 4. It is not stated separately.
