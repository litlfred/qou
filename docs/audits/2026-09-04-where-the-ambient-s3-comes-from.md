# Where the ambient `S³` comes from: three spheres under one glyph, and the contact volume form that is genuinely there

**Date:** 2026-09-04 · **Branch:** `claude/w-derived-from-axioms-2026-09-04`
**Bean:** `qou-fxou` (parent epic `qou-8lxd`)
**Lean:** [`QOU/Eightfold/CircleBundleBettiObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/CircleBundleBettiObstruction.lean)
— 11 declarations, `lean`-direct **exit 0**, no `sorry`, no `native_decide`, no
`: True`; `#print axioms` gives `[propext, Quot.sound]` on nine and additionally
`Classical.choice` on two (`surfaceEuler_eq_two_iff`,
`base_euler_eq_two_of_totalB1_eq_zero`, both from `omega` discharging an `↔`).
**Predecessor:** [`2026-09-04-w-derived-not-postulated-degree-of-the-volume-form.md`](2026-09-04-w-derived-not-postulated-degree-of-the-volume-form.md)
§3–§5, which *stated* the contradiction this note resolves.

---

## 0. Method, and the one path that did not run

Six-path corpus-grep, all six run.

- **Path 0 (`corpus_search`) — UNAVAILABLE.** The `paper-assistant` MCP server
  failed to connect this session (`ENOENT: … start-folio-assistant.sh`), as did
  `openalex-paper-search` and `paper-search-mcp`. So the standing
  **change-of-vocabulary blind spot is uncovered on this run**: everything below
  rests on lexical greps, and prior work phrased in words I did not guess would
  not have been found. This is a limit of the measurement, not a finding about
  the corpus.
- **Paths 1–4** (`docs/audits/`, `content/`, `computations/`,
  `docs/coordination/`) and **path 6** (`.beans/`) run and reported inline.
- **Path 5 (`library/`)** run on all four tiers, `ocr/` included.
  **math/0104104 IS held**: `library/arxiv-math-0104104v3/`, `sections/`
  complete, no `ocr/` directory, so nothing is hidden in the fourth tier for it.
  `3-Sasakian` returns **zero** hits across `library/*/sections/` and
  `library/*/ocr/` — the space-form classification of 3-dimensional 3-Sasakian
  manifolds is **not a held source** and is not relied on below.

---

## 1. The verdict

**The question.** Is the ambient `S³` in which the Markov closure of a braid is
taken the *same object* as the gauge group `SU(2) ≅ S³`, or a different
3-manifold that merely happens to be a 3-sphere?

**The answer: (c), and the reason the corpus contradicts itself is that there
are THREE objects, not two.** The recorded contradiction is not a disagreement
about one sphere; it is a conflation of three under one glyph. Once separated,
both sides of the contradiction are locally right, and a third object — the one
that actually carries the volume form the owner is asking about — is provably
**not** a 3-sphere at all.

| | what it is | where constructed | is it `SU(2)`? | verdict |
|---|---|---|---|---|
| **`S³_AM`** — the Alexander–Markov ambient | a **bare classical input** | nowhere: `thm:jones-markov-trace` is a statement about `H_n(ℂ,q)` and never mentions a 3-manifold. `S³` enters only when the trace is *read* as a link invariant, via Alexander + Markov, which are theorems **about links in `S³`** — so `S³` is a **hypothesis of the imported theorems**, not an output of the framework | **no** — nothing connects it to the gauge group | **(a)** in the brief's terms |
| **`S³_Reeb`** — the Reeb-bundle total space | **built from framework data**: the link of the exceptional divisor of a blow-up; a circle bundle over `𝒮_p ≅ ℂP¹ ≅ S²` | `def:reeb-bundle`, `rem:virtual-particles-exceptional-divisor`, `rem:knot-particle-generation-interpretation` | **yes, structurally** — that fibration *is* the Hopf fibration, i.e. the coset projection `SU(2) → SU(2)/U(1) = ℂP¹`, as a principal `U(1)`-bundle | **(b)** in the brief's terms |
| **`M_S`** — the QOU's own CR/contact manifold | the unit circle bundle `{(p,η) ∈ T*S : ‖η‖ = 1}` over Bring's **genus-4** surface, carrying `Θ = λ\|_{M_S}` restricted from the Liouville form | `rem:brings-qou-4tuple` item 1, `rem:brings-surface-unit-circle` | **no, and it cannot be** — `b₁ = 8 ≠ 0 = b₁(S³)`, proved below | **not a sphere at all** |

**So `rem:markov-trace-ambient-s3` and the 2026-06-28 audit §(i) are both
right, about different objects.** The remark's original disclaimer ("must not be
confused with `SU(2) ≅ S³`") is correct **for `S³_AM`**: the Alexander–Markov
ambient is an input to a classical theorem and carries no gauge content. The
audit's §(i) ("the ambient volume-`S³` **is** the gauge-group `SU(2)` itself,
fibered over the ED") is correct **for `S³_Reeb`**: the Hopf/coset reading is
forced once the sphere is presented as the link of the `(−1)`-curve. Neither
statement is about the other's object.

**The residual (c) — what is actually unproved, and what would settle it.**
The corpus asserts, in two places, that `S³_Reeb` *is* the closure arena:

> `def:reeb-bundle` (`mass-theory/reeb-bundle.md:9`): "The total space `S³` forms
> the **arena where braid words in `Bₙ` are evaluated** via the Iwahori–Hecke
> algebra `Hₙ(R,q)`."

> `rem:knot-particle-generation-interpretation`
> (`knots-particles-confinement/…:2`): the Hopf linking produces "a two-component
> link **in `S³`** fibered over `𝒮_c`."

**Neither derives it, and it cannot be derived from the trace side.** The
Markov trace is a linear functional on `Hₙ(ℂ,q)`; it is blind to which
3-manifold a closure is taken in. What would settle it is a statement — Lean or
prose, either is fine, but *stated* — that the QOU's braid closure is by
construction performed in the link of the exceptional divisor. That is a
**modelling choice, not a theorem**, and the honest disposition is to write it
as one.

**One constraint does point the same way, and it is not vacuous.** Alexander's
and Markov's theorems are specific to `S³`; in a general closed 3-manifold braid
closures do not exhaust links and the Markov moves do not generate isotopy. So
whatever the closure arena is, it must be a manifold with an Alexander theorem —
which `M_S` provably is not (§3). **The framework's braiding therefore has to be
local (at a blow-up point) rather than global (on the contact manifold)**, and
`S³_Reeb` is the only one of the three candidates that can play the role. That
is a *consistency* argument, not a derivation; it narrows the choice to one
without proving it was made.

---

## 2. The owner's actual question: yes, there is a natural degree-3 volume form, and it is the contact one

This is the part the predecessor note did not search for, and the answer is
affirmative and located.

**`Θ ∧ dΘ` is in the corpus, by name, as "the contact volume form".**

- `rem:bar-involution-geometric-kac-sunada`
  (`braids-and-knots/bar-involution-geometric-kac-sunada.md:1`): the
  bar-involution's geometric reading "yields … **the contact volume form
  `α ∧ dα`**".
- `stochastic-mechanics/bar-involution-table2-data.md:11`: the table row
  `| Volume forms $\alpha \wedge d\alpha$ | contact volume | Reeb dynamics |`.
- `information-theory/gravitational-constant-properties.md:22`: the
  `q`-Yang–Mills–Levi action integrates against `Θ ∧ (dΘ)ⁿ` — the same object in
  general odd dimension `2n+1`. This is the measure the gravitational coupling
  `G` is normalised against, so the contact volume form is **load-bearing**, not
  decorative.
- `def:reeb-bundle` (`mass-theory/reeb-bundle.md:7`): "The total space `S³`
  carries the contact structure `ker Θ|_{S³}`" — i.e. the ambient sphere is
  handed a contact form by restriction, and `Θ ∧ dΘ` is then its volume form.

**And it is genuinely natural, not postulated.** `rem:brings-qou-4tuple` item 1
builds it from nothing but the surface:

> "Because `S` is a Riemann surface (real dimension 2), it does not itself carry
> a contact form. The CR manifold is the unit circle bundle
> `M_S = {(p,η) ∈ T*S : ‖η‖_{g_S} = 1}` … The **Liouville 1-form** `λ = η dz` on
> `T*S` restricts to a contact form `Θ = λ|_{M_S}`, making `M_S` a
> **3-dimensional** strictly pseudoconvex CR manifold."

The Liouville form is canonical on any cotangent bundle — no choice is made — so
`Θ ∧ dΘ` is a **derived, canonical, degree-3 volume form** on the QOU's own
contact manifold. That is a direct affirmative answer to *"does it have a
natural volume form?"*, and it is a better answer than either the round metric
or the Haar form, because those need a metric or a group structure and this needs
neither.

**Its tier is low and this must not be elided.** All four carriers are `remark`s
or `table-data`; **none is a `definition`**, and a grep of the whole Lean tree
(`content/quantum-observable-universe/lean/`) for `alpha.*dalpha`,
`contactVolume`, `contact_volume`, `Theta.*dTheta` returns **zero**. So: the
object is present, named, and used in an action functional — and it is
**prose-tier throughout, with no Lean and no `definition` block**. Do not cite
it as formalised.

**Relation to `Λ³`.** None is drawn anywhere. `Λ³` appears in `content/` on
three lines only — `eightfold-open-problems.md:163` (the missing object `W` with
`Λ³W ≠ 0`) and twice in `baryon-product-from-alt-proof.md` — and **no block
connects `Θ ∧ dΘ` to `Λ³` of anything**. That is a measured absence of a *link*,
not evidence that no link exists; searched surface: `content/` `.md` + `.lean`,
`docs/`, `computations/`.

---

## 3. The obstruction: the manifold that carries the volume form is provably not `S³`

Here the two halves of §2 collide, and the collision is the substantive result
of this note.

`Θ` lives on `M_S`. `M_S` is a **circle bundle over Bring's genus-4 surface**.
The framework's own **Descartes condition** fixes that base: `χ(𝒮) = −6`
(`rem:brings-qou-4tuple`, summary line; `prop:archimedean-condition`).

**Gysin, with `ℚ` coefficients**, for an oriented circle bundle `S¹ → M → Σ_g`
of Euler number `e`:

```
0 → H¹(Σ_g;ℚ) → H¹(M;ℚ) → H⁰(Σ_g;ℚ) --∪e--> H²(Σ_g;ℚ)
```

so `b₁(M) = 2g` when `e ≠ 0`, and `b₁(M) = 2g + 1` when `e = 0` (then
`M ≅ Σ_g × S¹`). **`b₁(S³) = 0`.**

`CircleBundleBettiObstruction.lean` carries that count as the model — cited
standard algebraic topology, exactly as `Sym2GateFSTrichotomy.sym2Singlets`
carries the Frobenius–Schur singlet count — and proves the consequences:

| declaration | statement |
|---|---|
| `genus_eq_four_of_descartes` | `χ = −6 ⟹ g = 4` |
| `base_sphere_of_totalB1_eq_zero` | `b₁(total) = 0 ⟹ g = 0 ∧ e ≠ 0` |
| `descartes_forces_b1_pos` | `χ(base) = −6 ⟹ 8 ≤ b₁(total)`, **for every** `e` |
| `not_sphere_of_descartes` | `χ(base) = −6 ⟹ b₁(total) ≠ b₁(S³)` |
| `arenas_are_distinct` | `b₁` of the Reeb bundle `(g=0, e=−1)` is `0`; of the Descartes bundle `(g=4, e=−6)` is `8` |

**Scope: (b), structural exclusion. The named invariant is the first Betti
number, `8` against `0`.** It is not a scope-limited negative: no hypothesis on
the Euler number is used — the `e = 0` branch only makes `b₁` *larger* — so it
holds for **every** circle bundle over that base, not for one construction.

**What this buys.** The corpus's two "arenas" are distinguished by an invariant
of the total space. `S³_Reeb` (local, over the exceptional divisor) is
Betti-compatible with `S³`; `M_S` (global, over Bring's surface) is not, and
cannot be made so. **So "the arena where braid words are evaluated" and "the
manifold carrying `Θ ∧ dΘ`" are two different manifolds**, and any sentence
identifying them is false as stated. The repair is not to pick a side but to say
*local*.

---

## 4. The type obstruction, a fourth independent time

The brief asked whether the `S³` route bottoms out in a **real** volume form
again. **It does, and the corpus says so itself** — this is a corpus finding, not
an inference of mine.

`braids-and-knots/quaternion-so3-motivation.md`, lines 11 and 13–18:

> "the purely imaginary quaternions `Im ℍ` form a **3-dimensional** Lie algebra
> under the commutator … the structure constants exactly match
> `[e_a, e_b] = ε_{abc} e_c`."
> "conjugation by a unit quaternion acts on `Im ℍ ≅ ℝ³` via
> **orientation-preserving rotation** … This **adjoint representation** is the
> double cover `Sp(1) ↠ SO(3)`."

So the corpus's own 3-dimensional quaternionic object is the **adjoint**, an
`SO(3)` **rotation** representation, of **Frobenius–Schur real type** — the same
type as the icosahedral `T₁`, and excluded at any multiplicity by
`QOU.Eightfold.Sym2GateFSTrichotomy.real_triple_fails_gate:211` (sorry-free),
corroborated independently by
`QOU.StandardModel.ColourObstruction.real_rep_selfConjugate:91` (a real matrix
commutes with entrywise conjugation, so `𝟑 ≅ 𝟑̄`).

Every degree-3 volume form the `S³` route reaches is a **real** 3-form on a
**real** 3-manifold, and its symmetry algebra is that same real `𝔰𝔲(2)`:

- `Θ ∧ dΘ` on `M_S` or on `S³_Reeb` — a real 3-form;
- the bi-invariant Haar form on `S³ = SU(2)` — a real 3-form, invariance algebra
  `𝔰𝔲(2)`, the adjoint;
- `sp₁ = {X ∈ 𝔤𝔩₁(ℍ) : X + X* = 0} = Im ℍ` — the owner's own route through
  math/0104104, **the same object**, 3-dimensional, real.

**Scope: (b), invariant named** — Frobenius–Schur real type; equivalently, the
complexification of a real representation is self-conjugate, which
compactification, restriction and change of volume form cannot alter. Fourth
independent confirmation of one obstruction, from four directions
(`T₁`/icosahedral, the affine-compactification route, the `S₃` permutation
reading in `qou-ken6`, and now the quaternionic/`Sp(1)` route). **That is a
result, not a failure**: the routes are not four separate dead ends but one
invariant seen four times.

---

## 5. The tetraplectic pass, one more time — and the corpus got there first

Item 5 of the brief asked whether Foth–Leitner gives `S³` any degree-3 structure
via `sp₁ = Im ℍ`. **Answer: it does, and the corpus has already recorded both
the structure and its exclusion.** This is a corpus-grep hit, not a new
derivation.

- `def:bring-cone-tetraplectic-structure`: the affine cone `C(𝓑) ⊂ ℂ⁵` is a real
  4-manifold; at `m = 1` the tetraplectic condition is, in the block's **own**
  `authorNote`, "**vacuous** … the content in play here is the invariance, not
  the tetraplectic condition" (bean `qou-8p1g`).
- `lem:bring-cone-reeb-quaternionic-twist`: the cone's **3-dimensional link**
  carries a Reeb triad modelled by right-multiplication by `i, j, k`, with
  `[M_i, M_j] = 2M_k` and cyclic — sorry-free in
  `QOU/BringCone.lean:48,54,60` over a generic `CommRing`.
- `rem:tetraplectic-su2-gauge-reading` states the exclusion in as many words:
  "the triad is an `SU(2)` and nothing larger. Its three Reeb fields are the
  three dimensions of `𝔰𝔲(2)`, **the adjoint — not a three-dimensional
  fundamental** representation."

So the `sp₁ = Im ℍ` route is **already closed in the corpus**, by a block that
also names the reason. §4 above supplies what that block does not: the *general*
invariant (Frobenius–Schur type) rather than the particular observation, and the
sorry-free Lean carrier that makes it a class exclusion.

**A structural tension I am flagging, not resolving.** The Bring cone is the
cone over a **genus-4** curve, so the link of its singularity is exactly the
circle bundle of §3 — the same `M_S`, with `b₁ = 8`. `lem:bring-cone-reeb-…`
calls that link **3-Sasakian**. Three-dimensional 3-Sasakian manifolds are, in
the standard classification, space forms `S³/Γ` with finite fundamental group,
which has `b₁ = 0`. **I am not asserting a defect**: the library holds no
3-Sasakian source (path 5, all four tiers, zero hits), so I cannot cite the
classification from the corpus, and the block may intend "3-Sasakian" loosely as
"carrying a Reeb triad" — which is all its `.lean` actually proves (a quaternion
bracket identity, on `Quaternion R`, with no manifold in sight). **What would
settle it:** ingest a 3-Sasakian reference, or restate the block's claim as
"carries an `𝔰𝔲(2)` triad of operators" — which is what is proved — rather than
as a named geometric structure with a classification attached. Recorded for the
author; no edit made.

---

## 6. Two corrections to the predecessor note, both mine to make and one substantive

**(i) "`Sp(1)` appears in `library/` only, never in `content/`" is FALSE.**
The predecessor
([`…degree-of-the-volume-form.md`](2026-09-04-w-derived-not-postulated-degree-of-the-volume-form.md)
§3) states: *"`S³ = Sp(1)` is absent from the corpus entirely — `Sp(1)` appears
in `library/` only, never in `content/`, so the quaternionic leg of the chain is
not one step away, it is not present."* Measured with `grep -rlF 'mathrm{Sp}(1)'
content/ --include=*.md`: **5 files** —
`braids-and-knots/quaternion-so3-motivation.md`,
`brings-surface/geometric-drag.md`, `brings-surface/spectral-gauge-intro.md`,
`brings-surface/spectral-dynamics.md`,
`observations/brings-surface-simulator.md`. The first of these gives the
identification verbatim at line 3: `Sp(1) = {𝐪 ∈ ℍ : |𝐪| = 1} ≅ SU(2)`, with the
explicit `2×2` matrix map — and the unit-sphere description *is* `S³`.

**Why the error happened, since the shape recurs.** The predecessor's grep used
the bare string `Sp(1)`, which returns **zero** in `content/` because every
occurrence is written `\mathrm{Sp}(1)`. A single unknown spelling produced a
confident corpus-wide absence claim — the same detector-blindness class
`AGENTS.md` catalogues 26 rows of, one level up.

**What it changes:** the quaternionic leg is **present**, so the owner's
`sp_n := {X ∈ 𝔤𝔩_n(ℍ) : X + X* = 0}` question connects to existing corpus text
rather than to nothing. **What it does not change:** the verdict. The leg leads
to `Im ℍ = 𝔰𝔲(2)`, real type, excluded (§4) — the predecessor reached the right
answer by a route that happened to be unavailable.

**(ii) The dead citation is confirmed dead, and the replacement is now known.**
`docs/audits/2026-06-28-…-wlambda-scope.md:30` attributes "the total space
`S³ → 𝒮_c`" to `brings-surface/embeddability-closure.md`. Re-measured: that file
is **9 lines** and `grep -n "S\^3\|Hopf\|mathcal{S}_c"` on it returns **nothing**.
The real support is split across **two** blocks, neither cited by that audit:
`mass-theory/reeb-bundle.md` (the Hopf wording and the `S³` total space) and
`knots-particles-confinement/knot-particle-generation-interpretation.md:2` (the
`𝒮_c` notation, "the Hopf fibration `S³ → S² ≅ 𝒮_c`", and "a two-component link
in `S³` fibered over `𝒮_c`").

---

## 7. A contradiction found on the way, reported not fixed

**The corpus states two incompatible ranks for the Levi distribution
`H = ker Θ`,** and the disagreement is exactly about the degree of the contact
volume form — the subject of this note.

- `rem:brings-qou-4tuple` item 1: `M_S` is **3-dimensional**. A contact form on
  a 3-manifold has `ker Θ` of **rank 2**, and `Θ ∧ dΘ` is the volume form —
  degree **3**.
- `rem:archimedean-realisations:3` and `rem:brings-qou-axiom-map:10`: the Levi
  form is non-degenerate on the "**rank-4** distribution `H = ker Θ`" — which
  forces `dim M = 5` and makes the volume form `Θ ∧ (dΘ)²`, degree **5**.

The two cannot both hold of the same `M_S`, and `brings-qou-axiom-map:10`
explicitly cross-references `rem:brings-qou-4tuple` item 3 while asserting
rank-4, so they are describing one object. (`brings-qou-4tuple` item 4 adds a
third loose reading — `H` "spanned by the lifts of `dx₂, dx₃, dx₄`", three
1-forms — but those coordinates satisfy the cone relations, so that phrasing is
compatible with rank 2 and I do not count it as a third claim.)

**Why it matters here and not only bookkeeping:** the whole of §2 turns on `Θ ∧
dΘ` being a **top-degree** form. If `dim M_S = 5` it is not, and the QOU's
natural volume form is degree 5, not 3 — which would be a *different* answer to
the owner's question. The rest of the corpus (the Liouville construction, the
unit-circle-bundle definition, the `T*S` dimension count) supports **3**;
`rank-4` is the outlier and appears to be an uncorrected import of the general
CR-hypersurface setting. **Default if nothing is done:** two blocks continue to
assert a rank the framework's own construction contradicts. No edit made — it is
a two-block prose fix in an area this branch does not own.

---

## 8. What I could not settle, and what would settle it

1. **Is `S³_Reeb` the closure arena?** Asserted in two blocks, derived nowhere,
   and **underivable from the trace side** — `tr_M` is a functional on
   `Hₙ(ℂ,q)` and cannot see the ambient manifold. *Settled by:* the author
   stating it as a modelling choice, or by a construction placing the closure in
   the link of the exceptional divisor. The Alexander-theorem constraint (§1)
   narrows it to `S³_Reeb` but does not prove the choice was made.
2. **Is the Bring-cone link genuinely 3-Sasakian, or is that a loose name for a
   Reeb triad?** (§5.) *Settled by:* ingesting a 3-Sasakian source into
   `library/` (currently zero hits on all four tiers), or by restating the claim
   as the `𝔰𝔲(2)`-triad fact the Lean actually proves.
3. **Does `Θ ∧ dΘ` relate to `Λ³` of any categorical object?** No block draws
   the connection; searched `content/` (`.md` + `.lean`), `docs/`,
   `computations/`. This is *"I found no such statement on the surface I
   searched"*, **not** *"no such relation exists"*. *Settled by:* the search that
   path 0 would have run — `corpus_search` was unavailable, so the
   different-vocabulary blind spot is live on precisely this question.
4. **The `Sym²`-gate evasion `qou-ken6` left open** — that an object assembled
   from base *and* fibre may not be an object of the single-fibre tensor
   category — is **untouched by this note** and stays live. §3 and §4 exclude
   these *particular* bundles by `b₁` and by reality type; neither argument
   excludes the fibration route as a class. That bean names "Hopf `S³ → S²`, the
   Reeb bundle" as the next candidates, which is what §1–§4 measure; it does not
   name a mechanism, and I did not find one.
