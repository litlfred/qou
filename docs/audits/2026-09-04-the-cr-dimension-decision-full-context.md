# The CR-dimension decision: `ker Θ` rank 4 vs `dim M_S = 3` — full context, options, and downstream

**Date:** 2026-09-04 · **Branch:** `claude/lean-prove-assertions-2026-09-04` (PR #6584)
**Beans:** `qou-xlw1` · **Issue:** #6583 item 2 · **Epic:** `qou-8lxd`
**Status:** a *framed decision*. Nothing here changes a content block, a witness, or a
number. The Lean it cites proves only arithmetic.

Requested by the owner: *"Analyze and discuss the pros and cons of the resolution
options. What are the implications and downstream?"*

---

## 0. What is being decided, in one paragraph

Three blocks assign three different dimensions to the CR manifold that carries the
framework's contact form. They are not typos and they are not two-against-nine: **each
value is derived, from a different requirement**, and the requirements are mutually
exclusive. The decision is not "which block has the error" but **which requirement the
framework keeps**, because whichever is kept, the others lose content that is currently
being used.

| | requirement | forces | who needs it |
|---|---|---|---|
| **A** | `Λ^±H^*` exists (self-duality of 2-forms on the distribution) | `rank_ℝ H = 4`, `n = 2`, **`dim M = 5`** | 23 content blocks; the instanton chain; `q(p)` itself |
| **B** | `M_S` is the unit circle bundle in `T*S`, `S` a Riemann surface | `rank_ℝ H = 2`, `n = 1`, **`dim M = 3`** | Bring's worked example; the Woronowicz 3D calculus; 9 sites |
| **C** | `Λ³_ℂ ξ ≅ 𝟙` (the eightfold's missing object) | complex rank 3, **`dim M = 7`** | the eightfold chapter — currently unsatisfied by anything |

---

## 1. The single fact everything turns on

The Hodge star on an oriented `m`-dimensional space maps `Λ^k → Λ^{m−k}`. It is an
**endomorphism** of `Λ^k` — the only way it can have `±1` eigenspaces, hence the only
way a self-dual / anti-self-dual splitting can exist — exactly when `m = 2k`.

For `k = 2`: **`m = 4`, and no other dimension.**

| `rank_ℝ H = 2n` | `n` | `dim M = 2n+1` | `dim Λ²H^*` | `⋆ : Λ² →` | splitting? |
|---|---|---|---|---|---|
| 2 | 1 | **3** | 1 | `Λ⁰` | no |
| **4** | **2** | **5** | 6 | `Λ²` | **yes, 3+3** |
| 6 | 3 | **7** | 15 | `Λ⁴` | no |
| 8 | 4 | 9 | 28 | `Λ⁶` | no |

Formalised sorry-free in
[`QOU/QuantumObservableUniverse/SelfDualityDegree.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/SelfDualityDegree.lean)
(`hodgeTarget_eq_self_iff`, `selfDual_two_forms_iff_dim_four`,
`splitting_forces_dim_five`, `bring_dim_admits_no_splitting`).

**Read the third row.** Self-duality does not merely fail at Bring's dimension 3 — it
also fails at **7**, the dimension the eightfold way needs. That is what makes this a
three-way collision rather than a two-way disagreement, and it is the single most
consequential line in this document.

---

## 2. The three sites, verbatim

### 2.1 `brings-qou-4tuple.md` — both halves, nineteen lines apart

Line 12:

> Because `S` is a Riemann surface (real dimension 2), it does not itself carry a
> contact form. The CR manifold is the unit circle bundle
> `M_S = {(p,η) ∈ T*S : |η|_{g_S} = 1}` … making `M_S` a **3-dimensional** strictly
> pseudoconvex CR manifold.

Line 31:

> `q(p) = 1 + |⟨L_Θ, F_A^+⟩|(p)`

**The framework's single substrate modulus is defined, in its own defining block, by a
quantity that does not exist at the dimension that block assigns.** `F_A^+` is the
`Λ^+H^*` component; at `rank_ℝ H = 2`, `Λ²H^*` is a line and there is no `Λ^±`.

Line 28, in between, is the cheapest discriminating observation in the corpus:

> the horizontal distribution `H` is spanned by the lifts of the color differentials
> `dx₂, dx₃, dx₄` to `M_S`

Three objects spanning a distribution the same block makes rank 2. A contact
distribution has **even** rank, so `H` is never rank 3; and three spanning objects
cannot give rank 4. Both readings therefore require a relation among the three — which
Bring's defining equations (`Σxᵢ = Σxᵢ² = Σxᵢ³ = 0`) do supply. **Whatever those three
differentials span, settling it settles the block**, and the answer is visible from the
curve's own equations rather than from any modelling choice.

### 2.2 `archimedean-realisations.md:3` — rank 4, and it is *derived*

> **Volume constraint:** The Levi form `L_Θ = −i dΘ|_{H×H}` is non-degenerate on the
> **rank-4** distribution `H = ker Θ`, realising the categorical volume form
> `ε : Λ²V → 𝟙`. The induced Hodge star forces the structure group to be `SU(2)`.

This reads like an assertion and is not. It is the hypothesis under which the corpus's
own simplicity constraint is well-formed. `self-dual-2group.md`,
`emergence-to-quantum-flat-proof.md`, `glossary-quantum-flatness.md` and
`self-dual-ses.md` all write

> `B ∈ Γ(Λ^+H^* ⊗ Ad(P))`

— the splitting is of **`Λ²H^*`**, the exterior square of the *distribution*, not of the
manifold's 2-forms. By §1 that forces `rank_ℝ H = 4`. The rank-4 value is what makes
`Λ^±H^*` mean anything.

There is a second, independent reason the same block wants rank 4. If the Levi form is
to *realise* `ε : Λ²V → 𝟙` with `V` the complex rank-2 fundamental, then `H ≅ V` as a
complex rank-2 bundle, i.e. `rank_ℝ H = 4`. At `rank_ℝ H = 2`, `H` is a complex **line**
and `Λ²_ℂ H = 0` — there is no `ε` to realise.

### 2.3 `brings-qou-axiom-map.md:10` — the same claim, plus a misquote

> `V` is the rank-2 defining representation carried by the state bundle fibre
> `𝒮_p ≅ ℂ²` ([Bring's QOU 4-tuple], item 3) … Because `L_Θ` is alternating and
> non-degenerate on the rank-4 real distribution …

The citation does not say `ℂ²`. `brings-qou-4tuple.md:18` and `c-quantum-universe.md:7`
both say `𝒮 = P ×_G ℙ¹(ℂ)` — the fibre is `ℙ¹(ℂ)`. **This misquote is load-bearing for
the rank-4 sentence it introduces**, because `ℙ¹(ℂ)` and `ℂ²` are different objects and
only the latter is a rank-2 vector space. Substituting one for the other is what makes
the rank-4 claim read as though it were sourced from item 3.

**And it points at a resolution the sourced reading supports** — see Option 3 below.

### 2.4 The categorical layer says it too, with no manifold involved

`self-dual-ses.md` opens:

> The `q`-Hodge star `⋆_q` is an **involution on `Ω²(A)`**. Its eigenspaces provide the
> splitting `Ω²(A) = Ω⁺(A) ⊕ Ω⁻(A)` …

But `categorical-hodge-star.md` defines `⋆ : Ω^k(A) → Ω^{n−k}(A)`. So `⋆_q` is an
endomorphism of `Ω²` only at calculus dimension **`n = 4`** — while
`brings-is-qou-verification.md:3` and `brings-is-qou-proof.md:10` declare the calculus
to be the **Woronowicz left-covariant 3-dimensional** one, where `⋆ : Ω² → Ω¹`.

This is the same mismatch one layer up, with no geometry in it at all. It matters
because it means the problem is **not** an artefact of how Bring's surface was built:
the categorical layer independently wants a 4-dimensional calculus.

*Standard and cited, not held:* `𝒪_q(SU(2))` also admits two **4-dimensional
bicovariant** calculi (Woronowicz's classification). `library/` holds no source on this
— all four tiers including `ocr/` return zero — and the corpus declares only the 3D
left-covariant one.

---

## 3. Blast radii, measured

| population | size | how measured |
|---|---|---|
| blocks needing `Λ^±H^*` / `Ω^±(A)` / `F_A^±` | **23** `.md` files | fixed-string grep over `content/quantum-observable-universe/` |
| consumers of `def:substrate-parameter` | **90** files | grep for the label across `.md` + `.ts` |
| sites asserting `dim M_S = 3` or `n = 1` | 9 | prior pass, `qou-xlw1` |
| sites asserting `rank_ℝ H = 4` | 2 explicit, **23 implicit** | the 23 above each require it |
| Lean gating self-duality on `n = 2` | 3 declarations | `instanton.lean:88,100`, `self-dual-curvature.lean:47` |

The 23 include `simplicity-from-category` (the whole `volume constraint ⇒ SU_q(2) ⇒
F_A = B ⇒ B = F_A^+ ⇒ F_A^- = 0` chain), `q-yang-mills-levi`,
`gravitational-constant-properties` (the q-YM action normalising `G`),
`w-boson-mass-discrepancy`, `calabi-yau`, `instanton-on-shell`,
`main-commutative-diagram`, and `hodge-su2`.

**The Lean is consistent and does not need changing under any option.**
`CRManifoldData` carries `n` as a free field with `n_pos : 0 < n` and a Levi signature
`(r,s)` with `r + s = n`; it pins `n` nowhere. Self-duality is *gated* on `cr.n = 2`
and never claimed for `M_S`. **No Lean statement is wrong — the prose asserts
unconditionally what the Lean correctly conditions.** That is a genuinely good position
to be in: the formalisation already encodes the conditionality this decision is about.

---

## 4. The resolution options

### Option 1 — Keep `dim M_S = 3`; drop self-duality

**What it means.** Bring's construction stands as written. `Λ^±H^*`, `F_A^±`, the
instanton condition `F_A^- = 0`, quantum flatness, the simplicity constraint and the
`⋆_q`-involution on `Ω²(A)` are all withdrawn as ill-formed at `n = 1`. The substrate
parameter needs a new definition that does not mention `F_A^+`.

**What it costs.** The 23 blocks above, in whole or in part. Most seriously,
`q(p) = 1 + |⟨L_Θ, F_A^+⟩|` is the *definition* of the substrate parameter, with 90
consumers downstream — so this option requires re-deriving `q₀` from something else, or
demoting the archimedean `q(p)` to a heuristic and letting the CAL-2 lepton-ratio
pinning carry it alone. The latter is close to what production already does
(`q_parameter.Q` is pinned on `m_p/m_e`, not on any curvature pairing), which makes the
cost smaller in *practice* than in *exposition*.

**What it risks.** The framework loses its only stated mechanism connecting `q` to
geometry — the sentence *"It couples the color curvature to the contact geometry"* and
the `q → ∞` at branch points / `q → 1` away from defects story. That story is
load-bearing for the physical narrative even though it is not load-bearing for any
computed number.

**What it commits to.** Explaining why `SU(2)` is the structure group without the
induced Hodge star, since `archimedean-realisations.md:3`'s derivation goes through the
rank-4 star. The categorical route (`Λ²V ≅ 𝟙` ⇒ `SL₂ = Sp₂ = SU(2)`) survives
independently and is already Lean-proved, so this is a rewrite, not a gap.

### Option 2 — Keep self-duality; make `M_S` 5-dimensional

**What it means.** `n = 2`, `rank_ℝ H = 4`, `dim M_S = 5`. The whole instanton chain
becomes well-formed. `M_S` is no longer the unit circle bundle in `T*S` over a Riemann
surface — it needs a new construction.

**What it costs.** Bring's worked example, as written. There is no obvious 5-dimensional
`M_S` built canonically from Bring's surface: `T*S` is real 4-dimensional and its unit
circle bundle is 3. Candidates would be the unit circle bundle over a complex *surface*,
or a 5-dimensional link of a singularity — and the corpus's June s5-so3 work does
contain an **SU(3) Sasaki–Einstein `S⁵ ⊂ ℂ³`**, which is 5-dimensional and has never
been compared to `M_S`. That comparison is the cheapest way to test this option and it
has not been done.

**What it risks.** The Woronowicz 3D calculus must be replaced by a 4-dimensional
bicovariant one, which changes `Ω^k(A)` throughout and therefore the categorical Hodge
star, the top form, and anything derived from `vol ∈ Ω^n(A)`. That is a deeper edit than
it looks, and the library holds nothing to cite for it.

**What it commits to.** Showing that the Descartes constraint `χ(𝒮) = −6` and the
genus-4 / six-branch-point data survive on a 5-dimensional carrier — they were derived
for the 3-dimensional one.

### Option 3 — Neither: `H` is not `V`, and the rank-4 claim is a category error

**What it means.** `V = P ×_G ℂ²` is the rank-2 **associated bundle** whose
projectivisation is the state bundle `𝒮 = P ×_G ℙ¹(ℂ)`. `H = ker Θ` is the contact
distribution. **They are different bundles on the same base**, and nothing requires them
to be identified. Then:

* `ε : Λ²V → 𝟙` is the `SU(2)` determinant on `V` — complex rank 2, `Λ²V` trivial
  because `det = 1`. It needs no Levi form and no rank-4 distribution. ✓
* `M_S` stays 3-dimensional, `H` is a complex line, the Levi form is a positive function
  (strictly pseudoconvex), all as `brings-qou-4tuple` says. ✓
* `archimedean-realisations.md:3`'s *"realising the categorical volume form
  `ε : Λ²V → 𝟙`"* is then the **error** — it conflates the contact distribution with the
  fundamental object, and the `ℂ²`-for-`ℙ¹(ℂ)` misquote in `brings-qou-axiom-map.md:10`
  is the trace of exactly that conflation.

**What it costs.** Two sentences rewritten, not 23 blocks. This is by far the cheapest
option **for the volume-constraint half**.

**What it risks — and this is why it is not a free lunch.** It does **not** rescue
`Λ^±H^*`. Self-duality is a statement about `H`, not about `V`, and Option 3 leaves `H`
at rank 2. So `F_A^+` is still ill-formed and the substrate-parameter problem is
untouched. Option 3 is a *partial* resolution that must be combined with Option 1 (drop
self-duality) or with relocating `F_A^±` to a genuinely 4-dimensional carrier.

**The natural completion:** put `F_A^±` on `T*S`, which **is** a real 4-manifold, with
`M_S` its unit circle bundle. Instantons on a 4-manifold with a contact 3-manifold link
is a standard and coherent picture, and it makes every dimension in the corpus correct
simultaneously — `T*S` 4-dimensional carries `Λ^±`, `M_S` 3-dimensional carries
`Θ ∧ dΘ`, `V` complex rank 2 carries `ε`. **The corpus never says this**, and the pairing
`⟨L_Θ, F_A^+⟩` would need a stated restriction map, but it is the only reading found in
which nothing has to be given up.

### Option 4 — Do nothing

**What it means.** The blocks stay as they are; the contradiction stays live.

**What it costs.** Nothing today.

**What it risks.** `q(p)` remains defined by an expression that is ill-formed at the
stated dimension, and 90 consumers inherit that. Any reader who checks the dimensions
finds it in about ten minutes — this pass took less.

---

## 5. The downstream consequence that outlives the choice

**Fixing this in either direction does not open the eightfold route.**

`ContactDistributionRank` (sorry-free, merged) shows `Λ³_ℂ ξ ≅ 𝟙` needs complex rank 3,
i.e. `dim M = 7`. §1 shows self-duality needs `dim M = 5`. `SelfDualityDegree`
(`self_duality_and_eightfold_exclusive`) records that `5 ≠ 7`. So:

* Option 1 (dim 3) → complex rank 1. Not 3.
* Option 2 (dim 5) → complex rank 2. Not 3.
* Option 3 (dim 3 for `H`) → complex rank 1. Not 3.

**No resolution of this decision supplies `W`.** The eightfold object is not hiding in
the rank disagreement, and settling the disagreement should be motivated by wanting the
corpus to be right — not by hoping it opens the flavour sector. It does not.

That is worth saying flatly because the opposite hope is the natural one: the rank-4
reading *looks* like it is heading toward higher-dimensional structure, and it is not —
it heads to 5 and stops, because 4 is the unique dimension where 2-forms self-dualise.

---

## 6. Recommendation — my judgement, not a finding

**Option 3 for the volume constraint, plus its `T*S` completion for self-duality.**

It is the only option under which no block loses content: `V` and `H` are separated (two
sentences), `F_A^±` moves to the 4-manifold it was always implicitly about, `M_S` keeps
the construction that derives its dimension, and the Woronowicz 3D calculus stays. Every
other option pays with either the worked example or 23 blocks.

Its weakness is honest: **the `T*S` completion is not stated anywhere in the corpus**, so
adopting it means asserting something new rather than repairing something written. If
that assertion turns out not to be what was meant, the fallback is **Option 1** — keep
Bring's construction, withdraw self-duality, and let `q₀` rest on the lepton-ratio
pinning it already uses in production.

**Option 2 I would not take** without first comparing `M_S` to the s5-so3 `S⁵`: it is
the only option that requires replacing the differential calculus, and it does so for a
literature result the library does not hold.

---

## 7. Default if nothing is decided

Nothing changes. The three blocks keep their three dimensions, `q(p)` keeps its
definition, and the Lean keeps correctly conditioning what the prose asserts
unconditionally. The Lean files from this pass stand on their own — they are arithmetic
about which dimensions admit which structures, and none of them depends on how the
decision goes.

## 8. What this pass did not settle

* **Which of the three differentials `dx₂, dx₃, dx₄` are independent on `M_S`.** This is
  computable from Bring's defining equations and would settle §2.1 outright. Not done.
* **Whether the s5-so3 `S⁵` and `M_S` are the same manifold.** Both are 5-dimensional
  under Option 2; the June audits never compare them.
* **Whether the corpus's `F_A` was ever intended to live on `T*S`.** Option 3's
  completion rests on this and nothing in `content/` states it either way.
* `corpus_search` (path 0 of the corpus-grep checklist) has been **unavailable for three
  consecutive sessions** (`paper-assistant` MCP, `ENOENT`), so every absence claimed here
  is *lexical*. Named residual risk: `pseudohermitian`, `Tanaka`, `Fefferman`, `Webster`
  are standard alternative entries to this subject.
