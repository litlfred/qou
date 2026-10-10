# The `ker Θ` rank contradiction, seven-dimensional structure, and the complex structure on the contact distribution

**Date:** 2026-09-04
**Bean:** `qou-xlw1` (epic `qou-8lxd`)
**Branch:** `claude/lean-prove-assertions-2026-09-04`
**Author:** `corpus-grepper` sub-agent — **read-only on the corpus.** No content
block, `.ts`, `.lean` or witness was edited by this pass.
**Companion:** `QOU.Eightfold.ContactDistributionRank` (the arithmetic, written in
parallel by the parent session; this note supplies the corpus measurements it
defers to the author).

memory: MEMORY.md (234 lines, `a7092f55d0`) + library-and-staleness-traps.md, resolved-topics.md

---

## 0. Method, and the one path that is uncovered

**Path 0 — `corpus_search` (MCP): UNAVAILABLE, second consecutive session.** The
`paper-assistant` server fails to connect with `ENOENT: no such file or
directory, posix_spawn '/home/litlfred/folio-assistant/scripts/start-folio-assistant.sh'`
(so do `openalex-paper-search` and `paper-search-mcp`, both `CONNECTION_CLOSED`).
This is a connection failure, not a missing capability.

**Consequence, stated so it is not read past.** Paths 1–6 are greps and share one
blind spot: they find prior work only if it used *my* words. `corpus_search` is
the step that survives a change of vocabulary — it seeds lexically and then
expands along the knowledge graph. With it down, **every absence recorded below
is a lexical absence.** Where I could, I varied spellings deliberately (see §4);
where I could not think of the alternative spelling, the gap is real and
unmeasured.

Recorded because the predecessor pass on this same topic asserted *"`Sp(1)`
appears in `library/` only, never in `content/`"* on a bare-string grep, and it
is in **5** `content/` files written `\mathrm{Sp}(1)`. One unknown spelling, one
confident corpus-wide absence.

---

## 1. The `ker Θ` rank contradiction — VERDICT

### 1.1 The naive verdict is wrong, and I nearly filed it

The task as handed to me described `archimedean-realisations.md` and
`brings-qou-axiom-map.md` (rank 4 ⇒ `dim M = 5`) against `brings-qou-4tuple.md`
(`M_S` 3-dimensional ⇒ rank 2), and asked which is the derived value and which
the assertion.

A count answers that question the wrong way. **Rank-4 appears in exactly 2 files**
— `content/quantum-observable-universe/quantum-observable-universes/archimedean-realisations.md:3`
and `content/quantum-observable-universe/brings-surface/brings-qou-axiom-map.md:10`
— against **9 sites** asserting 3-dimensional / `n = 1` / contact-3-manifold:

| site | claim |
|---|---|
| `content/quantum-observable-universe/brings-surface/brings-qou-4tuple.md:12` | "making `M_S` a $3$-dimensional strictly pseudoconvex CR manifold" |
| `content/quantum-observable-universe/brings-surface/brings-is-qou-verification.md:7` | "(for $n = 1$, $\dim M_S = 3$)" |
| `content/quantum-observable-universe/models-of-qous/archimedean-models-intro.md:1` | "the categorical data becomes differential geometry on a **contact 3-manifold**" |
| `content/quantum-observable-universe/models-of-qous/ale.md:3` | "$M = S^3/\Gamma$ is a compact 3-dimensional strictly pseudoconvex CR manifold" |
| `content/quantum-observable-universe/models-of-qous/calabi-yau.md:3` | "induces a 3-dimensional strictly pseudoconvex CR structure on $M$" |
| `content/quantum-observable-universe/information-theory/reeb-turing-completeness.md:14` | "every contact 3-manifold" |
| `content/quantum-observable-universe/brings-surface/defect-legendrian-knot.lean:46` | "the contact 3-manifold `L_q`" |
| `content/quantum-observable-universe/lean/QOU/Elaboration.lean:118` | `cr_dim : ℕ := 1` — "**CR dimension is 1 (real dimension 3).**" |
| `content/quantum-observable-universe/lean/QOU/Elaboration.lean:124,138` | "A compact 3-dimensional strictly pseudoconvex CR manifold"; "making `M_S` a 3-dimensional strictly pseudoconvex CR manifold" |

(All other `rank 4` / `rank-4` hits in the tree — 20+ in `QOU/Machinery/HeckeH4*`
and `MathlibExt/TLContentStratification.lean` — are the **rank of the Hecke
algebra `H₄`**, an unrelated homonym. Do not count them.)

On that census alone rank-4 reads as two stray typos against a nine-site
consensus. **That verdict is wrong.** The 9 sites are the *carrier*; the 2 sites
are the *consumer*, and the consumer is load-bearing for far more of the
framework than the carrier is.

### 1.2 What is actually derived, on each side

**The 3-dimensional value is derived from the explicit carrier, and the
derivation is correct.** `brings-qou-4tuple.md:12` builds `M_S` as
`{(p,η) ∈ T*S : |η|_{g_S} = 1}` — the unit circle bundle in the cotangent bundle
of Bring's surface `S`. `S` is a Riemann surface, real dimension 2 (the block
says so in the preceding sentence: *"Because $S$ is a Riemann surface (real
dimension $2$), it does not itself carry a contact form"*). So `T*S` is real
4-dimensional and its unit circle bundle is real **3**-dimensional. Liouville
`λ = η dz` restricts to a contact form. Everything checks: CR dimension `n = 1`,
`H = ker Θ` real rank **2**, and `Θ ∧ dΘ` a genuine degree-3 volume form — which
matches the corpus's own `Ω^n(A)` with `n = 3`, the **Woronowicz 3-dimensional
calculus** (`brings-is-qou-verification.md:3`), the top degree at which
`categorical-hodge-star.md:1` places `vol`.

**The rank-4 value is derived from what the archimedean machinery consumes, and
that derivation is also correct.** It is not asserted out of nowhere. It is the
hypothesis under which the following exist at all:

* **The Hodge star on `Λ²H`.** `archimedean-realisations.md:3` says *"The induced
  Hodge star forces the structure group to be $\mathrm{SU}(2)$."* On a real
  rank-2 `H`, `Λ²H` is **one**-dimensional; the star maps `Λ²H → Λ⁰H` and there
  is no `Λ^± ` splitting whatsoever. Self-duality of 2-forms is a rank-4
  phenomenon (`Λ²ℝ⁴` is 6-dimensional and splits 3 + 3).
* **`F_A^+` — and therefore the archimedean substrate parameter itself.**
  `brings-qou-4tuple.md:31` defines
  `q(p) = 1 + |⟨L_Θ, F_A^+⟩|(p)`. The self-dual part `F_A^+` **does not exist**
  unless `dim_ℝ H = 4`. It appears in 17 `content/*.md` files in total, among them
  `quantum-observable-universes/levi-generalisation.md:3`,
  `brings-surface/descent-to-zero.md:1`, and
  `observations/w-boson-mass-discrepancy.md:8-9`.
* **The whole simplicity chain.** `quantum-observable-universes/simplicity-from-category.md:1`:
  *"volume constraint ⇒ $G_q = \mathrm{SU}_q(2)$ ⇒ $F_A = B$ ⇒ $B = F_A^+$ ⇒
  $F_A^- = 0$"*; `quantum-observable-universes/self-dual-2group.md:1` puts
  `B ∈ Γ(Λ^+ H^* ⊗ Ad(P))` — the self-dual part of `Λ²H^*`;
  `quantum-observable-universes/emergence-to-quantum-flat-proof.md:29` concludes
  `F_A^- = 0`.
* **The q-Yang–Mills action.** `information-theory/gravitational-constant-properties.md:21`:
  `∫_M q(p)‖F_A^+|_H‖² Θ ∧ (dΘ)^n`.
* **The categorical volume form as a `det`.** `brings-qou-axiom-map.md:10` needs
  `ε : Λ²V → 𝟙` with `V ≅ ℂ²` to be *instantiated by* `L_Θ`. At complex rank 2
  (= real rank 4) that is the `SU(2)` determinant and the argument
  *"forces $\det(g_V) = 1$, selecting $\mathrm{SU}(2)$ over $\mathrm{GL}(2)$"*
  goes through. At complex rank 1, `Λ²_ℂ H = 0` and the instantiation is empty.

**And the corpus already carries the rank-4 ⇒ `dim M = 5` implication in Lean,
as an explicit hypothesis.** This is the measurement that settles the framing:

```
content/quantum-observable-universe/models-of-qous/instanton.lean:85-88
  /-- When `n = 2` (`dim_ℝ H = 4`), the Hodge star on `Ad(P)`-valued
      2-forms restricted to `H`, determined by the Webster metric `g_θ`
      and the complex structure `J`. -/
  hodgeStar : cr.n = 2 → HodgeInvolution C(cr.M, ℝ)

content/quantum-observable-universe/models-of-qous/self-dual-curvature.lean:38
    When `dim_ℝ M = 5` (CR dimension `n = 2`, so `dim_ℝ H = 4`), the
    curvature of an instanton connection, restricted to `H`, is self-dual …
```

`self_dual_curvature` (`self-dual-curvature.lean:46-49`) takes `hn : cqou.n = 2`
as an explicit hypothesis. So the Lean is **not** inconsistent: it carries the
self-duality machinery *conditionally on `n = 2`* and never claims `n = 2` for
`M_S`. `CRManifoldData` (`lean/QOU/QuantumObservableUniverse/CRRealisation.lean:27-56`)
carries `n : ℕ`, `n_pos : 0 < n`, `r`, `s`, `rs_sum : r + s = n` and pins `n`
nowhere. The only pinned CR dimension in the tree is
`Elaboration.lean:118`, `cr_dim := 1`, and that is on the **Calabi–Yau
hypersurface example**, not on `M_S`.

### 1.3 Verdict

> **Neither claim is an assertion and neither is a typo. Both are derived, from
> two different halves of the construction, and the two halves are jointly
> unsatisfiable.** The 3-dimensional value is what the *carrier* delivers (unit
> circle bundle in `T*S`, `S` a Riemann surface). The rank-4 value is what the
> *archimedean machinery* requires (a `Λ^±` splitting, hence `F_A^+`, hence the
> archimedean `q(p)`, hence the volume-constraint ⇒ `SU(2)` argument). The
> outlier is not a block — it is the **assumption that one manifold carries
> both**.

**Scope: (b) structural exclusion, and I name the invariant.** These are not two
readings that a finer measurement might reconcile. For a CR manifold of
hypersurface type — which is what `c-quantum-universe.md:4` declares `M` to be —
`dim_ℝ M = 2n+1` and `rank_ℝ H = 2n` are the same integer datum, and `2n = 2`
and `2n = 4` have no common solution. The invariant is the hypersurface-type
dimension parametrisation, formalised as
`QOU.Eightfold.ContactDistributionRank.contactDim_eq_two_mul_complexRank`
and `realRank_succ` (integer arithmetic, sorry-free, this session). This is a
statement about `ℕ`, so it does not depend on any convention, anchor or witness.

**The sharpest form, and the one worth acting on:**
`brings-qou-4tuple.md` **contains both halves of the contradiction, 19 lines
apart.** Line 12 declares `M_S` 3-dimensional; line 31 defines the archimedean
substrate parameter as `q(p) = 1 + |⟨L_Θ, F_A^+⟩|(p)`, an expression that is
ill-formed at `dim_ℝ H = 2`. The framework's one substrate parameter is defined,
in its own defining block, by a formula that requires the dimension that block
denies.

### 1.4 The reading that makes each claim true

**Reading R2 (`dim M_S = 3`, `H` real rank 2) — what has to be given up.** `H` is
the contact *plane field*, real rank 2, complex rank 1 under `J`. `L_Θ = -i dΘ|_H`
is a Hermitian form on a complex **line** — signature `(1,0)`, which is exactly
`c-quantum-universe.md:4`'s "signature `(r,s)`" with `r + s = n = 1`, so
strict pseudoconvexity is fine. `Λ²_ℝ H` is a real line and `dΘ|_H` a nonvanishing
section, so there *is* a degree-2 form and a degree-3 volume form `Θ ∧ dΘ`,
matching the Woronowicz calculus. **What fails:** `ε : Λ²V → 𝟙` can only be the
real area form on the contact plane, so the `V` of `archimedean-realisations.md:3`
is a **real** rank-2 bundle, not the complex `ℂ²` defining representation — and
`brings-qou-axiom-map.md:10`'s identification of it with the state-bundle fibre
is false. There is no Hodge star on `Λ²H`, no `F_A^±`, no instanton equation, and
no archimedean `q(p)`. Under R2 the corpus keeps its carrier and loses its
archimedean derivation chain.

**Reading R4 (`H` complex rank 2, `dim_ℝ M = 5`, `n = 2`) — what has to be given
up.** `(H,J) ≅ V ≅ ℂ²`, `ε : Λ²_ℂ V → 𝟙` is the genuine `SU(2)` determinant, the
Hodge star on `Λ²H` splits 3 + 3, `F_A^±` exist, `q(p)` is well-formed, and every
consumer in §1.2 goes through — this is the reading the Lean already anticipates
via `hn : cr.n = 2`. **What fails:** `M_S` cannot be the unit circle bundle in
`T*S` of a Riemann surface; the top form is degree 5, contradicting the Woronowicz
3-dimensional calculus and the four blocks that name `Θ ∧ dΘ` as *the* volume
form; and `ale.md` / `calabi-yau.md` — both explicitly 3-dimensional — stop being
models of the definition.

**A third reading that makes both literally true, offered as mine and sourced
nowhere.** `S = P ×_G ℙ¹(ℂ) → M_S` has 2-real-dimensional fibres
(`brings-qou-4tuple.md:18`, `c-quantum-universe.md:7` — both say `ℙ¹(ℂ)`, *not*
`ℂ²`), so the **total space of the state bundle is real 5-dimensional**, and the
kernel of the pulled-back `Θ` on it has rank 4 = 2 (base-horizontal) ⊕ 2 (fibre).
Under this reading `brings-qou-4tuple` is about the base and
`archimedean-realisations` / `brings-qou-axiom-map` are about the total space,
both are correct, and the only defect is that both are written `H = ker Θ`.
**I found no block that states this**, and `c-quantum-universe.md:1,7` puts `Θ`
on `M` and `S → M`, so as written both blocks are about the base. Offered because
it is cheap to check and would be the least destructive repair.

### 1.5 Two further defects found in the same three blocks, reported not fixed

1. **`brings-qou-axiom-map.md:10` misquotes its own citation.** It says *"the
   state bundle fibre $\mathcal{S}_p \cong \mathbb{C}^2$ ([Bring's QOU 4-tuple],
   item 3)"*. Item 3 (`brings-qou-4tuple.md:18`) says the fibre is
   `ℙ¹(ℂ)` — a projective line, real dimension 2 — and `c-quantum-universe.md:7`
   agrees. `ℙ¹(ℂ)` and `ℂ²` are not the same object and the substitution is what
   makes the rank-4 sentence read as though it were sourced.
2. **The branched-covering degree disagrees, 3 vs 4.**
   `brings-qou-4tuple.md:15`: *"The branched covering $\pi\colon S \to
   \mathbb{P}^1(\mathbb{C})$ (**degree 3**, six branch points)"*.
   `brings-is-qou-verification.md:15`: *"The **degree-4** covering $\pi$ has 6
   branch points with total ramification $R_{tot} = 14$ (Riemann–Hurwitz)."*
   `lean/QOU/Elaboration.lean:151`: `covering_degree : ℕ := 4`.

   > **🛑 RETRACTED the same day, by the author of this audit.** This item
   > originally concluded: *"Riemann–Hurwitz for genus 4 over `ℙ¹` with `R = 14`
   > gives `6 = −2d + 14`, `d = 4`. So degree 4 is the derived value and
   > `brings-qou-4tuple.md:15` is the outlier."* **That is too strong.**
   > Riemann–Hurwitz constrains `R` *given* `d`; it does not adjudicate between
   > two *different* maps. A non-hyperelliptic genus-4 curve has **gonality 3** —
   > its canonical model lies on a quadric in `ℙ³` and the two rulings give two
   > degree-3 maps to `ℙ¹` — so a degree-3 covering genuinely **exists** and is
   > refuted by no count. `R = 2g − 2 + 2d` gives `R = 12` at `d = 3` and
   > `R = 14` at `d = 4`; both are self-consistent, **for different maps**.
   >
   > What survives is weaker: `R = 14` forces `d = 4`, so the two blocks describe
   > one map only if their degrees agree. Both write `π : S → ℙ¹(ℂ)` with six
   > branch points, so at best the corpus overloads one symbol — the same defect
   > class as the three distinct `S³`s (§1) and the five meanings of bare `W`.

   **What is actually wrong is sharper, and is now proved**
   ([`QOU/BringsSurface/CoveringDegreeRamification.lean`](../../content/quantum-observable-universe/lean/QOU/BringsSurface/CoveringDegreeRamification.lean),
   14 declarations, sorry-free). Take the 4-tuple block's own numbers at face
   value — degree 3, genus 4, exactly six branch points — and the ramification is
   fully determined:

   * Riemann–Hurwitz gives `R = 12`;
   * a fibre of a degree-3 map contributes at most `d − 1 = 2` to `R`, so six
     branch points contribute at most **12**;
   * twelve **is** the budget, so the bound is saturated: **every** branch point
     is totally ramified, fibre profile `(3)`, monodromy a 3-cycle. There is no
     slack — one branch point of profile `(2,1)` would contribute 1 instead of 2
     and the total could not reach 12.

   And a 3-cycle is **even**. So the monodromy group is generated by even
   permutations, contains no transposition, and is **not `S₃`** — it is cyclic
   `A₃ ≅ ℤ/3`, and the covering is Galois.

   **`brings-qou-4tuple.md:15` is therefore internally inconsistent**: its stated
   degree and branch-point count force cyclic `ℤ/3` monodromy, in the *same
   sentence* that derives the `SO(3)` holonomy representation from *"the `S₃`
   permutation of the three sheets"*. That bears on the colour leg. Not touched;
   flagged.

---

## 2. Seven-dimensional structure in the corpus

**Result: the corpus contains no seven-dimensional manifold, contact structure,
or CR structure anywhere. It contains three independent pointers at 7, two of
which predate this session by weeks.**

### 2.1 What is present

| object | dimension | where | tier |
|---|---|---|---|
| `M_S`, `S³/Γ`, CY hypersurface, torsion leaves | **3** | §1.1 table | prose + Lean structures |
| Bring-cone link, "3-Sasakian (degenerate quaternionic-contact)" | **3** | `content/quantum-observable-universe/brings-surface/bring-cone-reeb-quaternionic-twist.md:1-6`; `lean/QOU/BringCone.lean:7-8` | prose + Lean (`reeb_twist_ij/jk/ki` sorry-free) |
| colour **`S⁵ ⊂ ℂ³`, SU(3)-Sasaki–Einstein** | **5** | `docs/audits/2026-06-16-s5so3-two-sasakian-construction-attempt.md:42`; `docs/audits/2026-06-16-s5so3-hopf-coupling-and-reeb-obstruction.md:13,40,77` | audit-doc tier only (`docs/audits/scripts/s5so3_ingredient4_*.py`) |
| `Im 𝕆`, `𝔤₂ = Der(𝕆)` | **7** and **14** as *vector spaces* | `lean/QOU/MathlibExt/OctonionDerivationProperties.lean:18`; `lean/QOU/Eightfold/OctonionicSu3RankObstruction.lean:19` | Lean, sorry-free |

The `S⁵` is the one genuinely surprising find: **the corpus already built a
5-dimensional Sasaki–Einstein contact manifold**, in June 2026, as the colour side
of the s5-so3 keystone, with `A₅ ⊂ SO(3) ⊂ SU(3)` acting directly (no binary
cover). It is *not* in `content/` — it lives only in `docs/audits/` and
`docs/audits/scripts/`. A `content/`-only grep does not see it.

### 2.2 What is absent

Measured on paths 1–4 and 6 with fixed-string matching:

| term | `content/` | `docs/` | `computations/` | `.beans/` |
|---|---|---|---|---|
| `7-manifold`, `seven-manifold`, `seven-dimensional` | 0 | 0 | 0 | 0 |
| `Sasaki-Einstein` / `Sasaki–Einstein` | 1 (this session's `ContactDistributionRank.lean`) | 2 (the June audits) | 0 | 0 |
| `quaternionic contact` | 0 | 0 | 0 | 0 |
| `quaternionic-Kähler` | 0 | 1 | 0 | 1 |
| `4n+3` (the 3-Sasakian dimension formula) | 0 | 0 | 0 | 0 |
| `transverse holomorphic`, `transverse Kähler` | 0 | 0 | 0 | 0 |
| `nearly parallel`, `weak holonomy` | 0 | 0 | 1 (unrelated: two vectors "nearly parallel") | 1 (unrelated) |
| `associative 3-form` | 0 | 1 (Klein-quartic dependency audit, in passing) | 0 | 0 |
| `S^7` | 0 (outside Mathlib) | 0 | **1** | 0 |
| `Spin(7)` | 0 | 4 | 2 | 4 |

**Path 6 (`.beans/`) is empty for the whole contact/CR axis:** `Levi
distribution`, `ker Θ`, `ker \Theta`, `CR complex structure`, `Levi form`,
`contact distribution`, `horizontal distribution` all return **zero** bean files.
No bean has ever worked the rank question. `Sasaki` matches 3 beans, all
`completed`: `qou-8p1g`, `s5bb`, `wlk9`.

**Path 3 (`computations/`) is effectively empty for the axis:** `contact form` /
`CR manifold` / `Levi distribution` / `ker Theta` / `contact distribution` /
`Levi form` matches **2** files, one of which is `fsh-guts/deprecated/computations/`.

### 2.3 Path 5 — the library holds NOTHING on this, and that is the finding

Four tiers, `INDEX.md` + `summary.json` + `sections/` + **`ocr/`**, fixed-string:

| term | `library/*/sections/` | `library/*/ocr/` |
|---|---|---|
| `Sasakian` | **0** | **0** |
| `Sasaki-Einstein` / `Sasaki–Einstein` | **0** | **0** |
| `CR manifold`, `CR structure`, `CR-manifold` | **0** | **0** |
| `pseudoconvex` | 1 | 0 |
| `7-manifold`, `seven-manifold` | **0** | **0** |
| `quaternionic contact` | **0** | **0** |
| `quaternionic-Kähler`, `hyperkähler` | **0** | **0** |
| `G_2 holonomy`, `nearly Kähler` | **0** | **0** |
| `exceptional holonomy` | 1 | 0 |
| `S^7` | **0** | **0** |
| `canonical bundle` | 26 | 1 |
| `almost complex structure` | 28 | 0 |
| `Reeb` | 9 | 0 |

**This confirms and extends the predecessor's negative.** The predecessor
(`docs/audits/2026-09-04-the-g2-frame.md` §5) reported zero library hits for
`G₂/SO(4)`, Wolf space, nearly-Kähler and `S⁶`. Extending to the Sasakian/CR/
contact axis: **the library holds no source on CR geometry, Sasakian geometry, or
7-manifolds at all** — while `content/` uses the phrase "CR manifold" in **34**
`.md`/`.lean`/`.ts` files. The framework's entire contact/CR layer is un-sourced from the ingested
library. This is a *"there is nothing held to cite"* case, not a *"cite it, don't
derive it"* case: closing it would require an upload (Boyer–Galicki
*Sasakian Geometry*; Dragomir–Tomassini for the pseudohermitian/Webster package;
Bryant on `G₂` structures).

> **🛑 Do NOT generalise this absence to the neighbouring layer — I did, and it
> was wrong (added 2026-09-04, after the owner corrected me).**  The finding
> above is scoped to the **contact / CR / Sasakian / `G₂`-homogeneous**
> vocabulary and is correct there: re-measured across spellings, `Sasakian` 0,
> `nearly Kähler` 0, `nearly-Kahler` 0, `Wolf space` 0, `3-Sasakian` 0,
> `CR structure` 0, `CR manifold` 0, `quaternion-Kähler` 0, in `sections/` and
> `ocr/` alike (`Sasaki` returns 5, all surnames in bibliographies).
>
> **The adjacent hyperbolic-volume layer is the opposite of absent.**  Section-file
> hits: dilogarithm **849**, Kashaev **548**, volume conjecture **381**, Thurston
> **321**, gluing equation **215**, ideal tetrahedra **178**, Bloch–Wigner
> **135**, Neumann–Zagier **96**, Lobachevsky **46**; plus `ocr/` — dilogarithm
> 30, Kashaev 21, Thurston 19.  And Mathlib carries
> `Analysis/Complex/UpperHalfPlane/{Metric,Basic,Manifold,MoebiusAction}` — the
> hyperbolic metric on `ℍ²` and the Möbius action — plus the whole
> `NumberTheory/ModularForms/` tree.  What Mathlib lacks is a *dilogarithm* and a
> 3-dimensional hyperbolic-manifold API, not hyperbolic geometry as such.
>
> I generalised the CR-layer absence into "the hyperbolic volume form is not a
> QOU structure — it's imported", which is an **impossibility claim I never
> measured**, and which contradicts what the corpus itself asserts in
> `brings-surface/thurston-relaxation.md` — that the `q`-Pochhammer poles and the
> ideal vertices are in bijection and that the SDP and the gluing solver are
> *"different evaluations of one categorical object"*.  Retracted at
> `QOU/Eightfold/HyperbolicVolumeFormType.lean`; the route is being mapped
> separately.
>
> **The mechanical lesson, since this is the third instance this session:** one
> spelling of one name moves a count sevenfold — `Bloch-Wigner` (hyphen) returns
> 135, `Bloch–Wigner` (en-dash) returns 19.  A library count is evidence about
> the string you typed, never about the subject.

**Caveat on `Sasaki` as a bare string.** 5 `library/*/sections/` files match
`sasaki` case-insensitively; they are surname matches in bibliographies (e.g.
`library/arxiv-hep-th-9408113v2/sections/sec-004-6-anatol-n-kirillov.md`), not
Sasakian geometry. `Sasakian` itself is 0. Do not read the 5 as sources.

### 2.4 The three pointers at 7 — two of them predate this session

1. **`computations/form_stabilizer_genericity_su3_routes.py:21`** (bean
   `qou-8p1f`, August): the exceptional chain `Spin(7) → G₂ → SU(3)` with
   `S⁷ = Spin(7)/G₂` and `S⁶ = G₂/SU(3)`. Its result is that the *upper* link
   fails genericity (4-forms on `ℝ⁸` have codimension-27 orbits) while **"the
   generic-form route to the exceptional chain runs through 3-forms in dimension
   7"** — `G₂` is the stabiliser of a *generic* 3-form on `ℝ⁷`, open orbit,
   codimension 0. This is the only occurrence of `S^7` in the corpus outside
   Mathlib.
2. **Bean `qou-8p1g` §"What would change the verdict"** (completed 2026-08-24):
   the tetraplectic layer is vacuous at `m = 1` because the Bring cone is a real
   **4**-manifold, and Foth's machinery *"only bites at `m ≥ 2`, i.e. real
   dimension `≥ 8`"*. **The link of a real 8-dimensional cone is 7-dimensional**,
   and a 3-Sasakian manifold has dimension `4n+3` — so `n = 0 → 3` is the
   degenerate case the corpus actually has, and `n = 1 → 7` is the first genuine
   one. `bring-cone-reeb-quaternionic-twist.md:4` calls its own structure
   *"degenerate quaternionic-contact"* in as many words.
   **Do not read this as an open route without reading the bean's tail:** the
   `m ≥ 2` question was *asked and answered* on 2026-08-24 for the concrete
   candidate `Sp(3)/Sp(1)³` (real dim 12, `m = 3`) —
   `computations/quaternionic_flag_su3_exclusion.py`, 23/23 assertions, **the
   `S₃` on three quaternionic lines does not yield `SU(3)`**. That is a
   scope-(a) negative *for that candidate*; the bean does not consider a
   3-Sasakian 7-manifold at all, and `4n+3` returns **zero** hits corpus-wide.
3. **`qou-uq5x` / `docs/audits/2026-09-04-the-g2-frame.md`** (this session):
   `S⁶ = G₂/SU(3)` viable with complex `𝟑` isotropy.

**So there are now three legs at 7, reached from three directions** — contact
complex-rank arithmetic (this session), generic-3-form stabiliser genericity
(August), and the tetraplectic dimension floor (August) — plus the octonionic
`S⁶` leg one dimension below. **I assert no convergence.** Three arguments
landing on the same integer is a lead, and the corpus has a named recurring
defect for exactly this shape (`qbeta_rank_one_identity_is_n3_only_probe.py`,
PR #5337, *"do not generalise the n=3 coincidence"*).

### 2.5 The constraint anyone taking the 7-dimensional route will hit next

`docs/coordination/s5-so3-keystone.md:47` (path 4) carries a standing exclusion:

> **No compact Sasakian / compact MTC can host `W_λ`** at the substrate anchor:
> `q₀ ≈ 1.10998` is real `> 1` (growth regime, `[m]_q = sinh(mη)/sinh(η)`,
> `η = log q₀` real), not a root of unity.

and at line 31, *"there is **no finite colour-SU(3) Sasakian arena**"*, and at
line 51, *"a finite-dimensional Sasakian is ruled out"*.

**Read the shape before transferring it.** That exclusion is about whether an
*index on* a compact Sasakian manifold reproduces the Markov weight `W_λ` at the
substrate anchor. It says nothing about the *rank of the contact distribution* as
a bundle, which is the question `ContactDistributionRank` answers. So it does
**not** touch the parent's current step. It does bear on the step after: a
7-dimensional Sasaki–Einstein manifold is compact, and any attempt to read a
Markov weight off it walks straight into this. Scope **(a)** as applied to the
7-dimensional contact route — the negative is about a different construction, and
the argument (real `q₀ > 1`, not a root of unity) would have to be re-run against
whatever the 7-dimensional route actually proposes to compute.

---

## 3. Does anything give `ker Θ` a complex structure?

**Answer: YES — and the corpus not only attaches a `J` to `ker Θ`, it explicitly
identifies that `J` with the categorical `i`. The bridge the question asks about
is already asserted. What is missing is that the two objects it identifies live on
bundles of different rank, and the rank they would have to share is 4.**

### 3.1 What is present — seven sites, prose tier

| site | text |
|---|---|
| `content/quantum-observable-universe/quantum-observable-universes/q-deformed-commutator.md:1` | "Let $J \colon H \to H$ be the **complex structure on the Levi distribution** ($J^2 = -\mathrm{Id}$)." |
| `.../linearisation-convention.md:1` | "The symbol $i$ **evaluates as** the CR complex structure $J \colon H \to H$ on the Levi distribution." |
| `.../heisenberg-commutator.md:1` | "The complex structure $J \colon H \to H$ on the Levi distribution **supplies the imaginary unit**" |
| `.../substrate-radial-coordinate.md:7` | "$J$ is the complex structure on the horizontal distribution $H$" |
| `.../i-as-braiding-orientation.md:4` | "**CR complex structure**: The operator $J \colon H \to H$ secures the CR orientation." |
| `content/quantum-observable-universe/climax-volume-mass/commutative-crossing-energy.md:25` | "$i = \sqrt{\lambda_-}$ … This single datum appears in three faces: Wick rotation, **CR complex structure**, and arrow of time." |
| `content/quantum-observable-universe/models-of-qous/instanton.lean:85-87` | "the Hodge star … determined by the Webster metric `g_θ` **and the complex structure `J`**" |

Two more sites carry the identification rather than the object:
`climax-volume-mass/categorical-coordinate-ring-dedup.md:7` folds "the CR
structure" into the single categorical coordinate of
`prop:categorical-coordinate-ring`, and
`brings-surface/archimedean-chirality.md:1` reads chirality off "the complex
structure of $M$".

Adjacent and worth naming: `c-quantum-universe.md:4` declares the Levi form's
**signature `(r,s)`**, and `archimedean-realisations.md:3` writes it as
`L_Θ = −i dΘ|_{H×H}`. Both the `−i` normalisation and the notion of *signature*
presuppose a Hermitian form on a **complex** bundle — so the corpus's general
definition is already treating `H` as complex, one layer below the prose.

### 3.2 What is NOT present, measured

* **No Lean carries `J` as an endomorphism.** Every `J` in the tree is a bare
  scalar: `q-deformed-commutator.lean:37` `def qDeformedCommutator … (J : K) …`,
  `heisenberg-commutator-prop.lean:87` `(J : R)`,
  `substrate-radial-coordinate.lean:44` `J : ℝ`. `J² = −Id` appears **only in
  docstrings** (`q-deformed-commutator.lean:9,32`) and is asserted nowhere.
* **`CRManifoldData` has no `J` field, no Levi distribution, and no Levi form.**
  (`lean/QOU/QuantumObservableUniverse/CRRealisation.lean:27-56`: `M`, `n`,
  `n_pos`, `r`, `s`, `rs_sum`, `contactForm`, `contact_nondeg`, `reebField`,
  `reeb_preserves_contact`.) The complex structure is named in the
  `instanton.lean:87` docstring as an input to `hodgeStar` and is not a field of
  anything.
* **The one Lean `J² = −id` in the tree is on the octonion side, not on `ker Θ`.**
  `lean/QOU/MathlibExt/OctonionComplexStructure.lean:53`,
  `theorem Le_sq_eq_neg_id : Le ∘ₗ Le = -LinearMap.id`. That is `L_{e₁}` on
  `Im 𝕆` (bean `qou-uq5x`). **Nothing connects it to `ker Θ`** — I grepped for a
  joint occurrence and found none.
* `transverse holomorphic` / `transverse Kähler`: **0** across all of `content/`,
  `docs/`, `computations/`, `.beans/`.

### 3.3 The defect, and it feeds back into §1

`climax-volume-mass/commutative-crossing-energy.md:26` puts the categorical `J`
on the **fundamental object**: `J = i·id_V ∈ End_{R[i]}(V)`, `J² = −id_V`,
descending to a complex structure on `ℙ(V) ≅ S_p ≅ ℙ¹(ℂ) ≅ S²`. The CR `J` of
§3.1 is on **`H = ker Θ ⊂ TM_S`**. The corpus calls them "three faces of one
datum" and supplies **no bundle map between the carriers**.

At `dim M_S = 3`, `(H, J)` is a complex **line** bundle and `V ≅ ℂ²` is complex
rank 2. `J_CR` and `i·id_V` cannot be the same endomorphism because their
carriers have different rank. **The identification typechecks only at
`rank_ℝ H = 4`.**

So §3 is not independent of §1 — it is the same defect seen from the other side.
The corpus's claim that the CR complex structure *is* the categorical `i` is
exactly as true as the rank-4 reading, and exactly as false as the 3-dimensional
one.

**One genuinely new asset, merged this session.**
`lean/QOU/QuantumUniverse/CategoricalCoordinateForced.lean` (bean `qou-ywh9`)
derives `i² = −1` from the volume form (`det = 1`) plus trace-freeness, via
Cayley–Hamilton at rank 2 — no square root assumed. That closes the *categorical*
half: the framework does force `R[i]`. It says nothing about `ker Θ`, and it is
**rank-2-specific by construction** (Cayley–Hamilton `f² = (tr f)f − (det f)1`
holds at rank 2), which is worth noticing if the route is to move to complex
rank 3.

---

## 4. What I could not settle, and what would settle it

1. **Which reading the author intends for `H = ker Θ`.** This is a modelling
   decision, not a measurement, and §1.4 lays out what each costs. The cheapest
   discriminating observation: **read `brings-qou-4tuple.md:28`**, which says `H`
   *"is spanned by the lifts of the color differentials $dx_2, dx_3, dx_4$ to
   $M_S$"* — **three** differentials, on a distribution the same block makes
   rank 2. Whatever those three lifts span, it is not a rank-2 subbundle of a
   3-manifold's tangent bundle, and settling what they are settles the block.
2. **Whether a 3-Sasakian 7-manifold is reachable from the Bring cone.** The
   corpus has the degenerate `n = 0` case and a bean recommending real dimension
   ≥ 8; it has no `4n+3`, no `quaternionic contact`, no `quaternionic-Kähler`
   object. What would settle it: does the Bring cone `C(𝓑)` sit inside, or admit
   a canonical thickening to, a real 8-dimensional hyperkähler cone? That is a
   question about the corpus's own geometry and needs no new imports to *state*.
3. **Whether the s5-so3 `S⁵` and `M_S` are the same manifold.** Both are
   5-dimensional under reading R4; the June audits never compare them, and
   `docs/audits/2026-06-16-s5so3-hopf-coupling-and-reeb-obstruction.md:40-44`
   establishes the colour Reeb is *transverse* to the spin one. If they were the
   same object the rank-4 reading would acquire a built carrier. Settled by
   comparing `μ`'s image with `M_S`'s Reeb — the machinery is already in
   `docs/audits/scripts/s5so3_ingredient4_hopf_coupling_obstruction.py`.
4. **The lexical blind spot.** With `corpus_search` down I cannot rule out that
   the corpus works this material under vocabulary I did not guess. The specific
   risk here is high: "pseudohermitian", "Webster", "Tanaka", "Fefferman",
   "strictly pseudoconvex" are all standard alternative entries to the same
   subject, and `Webster` alone matches **28 `content/` files, 13 `docs/`, 6
   `computations/`, 4 beans** — a surface I sampled but did not exhaust.

---

## 5. Six-path record

| path | run | result |
|---|---|---|
| **0** `corpus_search` (MCP) | attempted | **UNAVAILABLE** — `paper-assistant` `ENOENT`. Every absence below is lexical. |
| **1** `docs/audits/` | ✔ | HIT — `2026-06-16-s5so3-two-sasakian-construction-attempt.md` (SU(3)-Sasakian `S⁵`, built), `2026-06-16-s5so3-hopf-coupling-and-reeb-obstruction.md`, `2026-09-04-the-g2-frame.md` (predecessor census), `2026-09-04-where-the-ambient-s3-comes-from.md` (the contradiction as recorded). No audit works the `ker Θ` rank. |
| **2** `content/` (whole tree) | ✔ | HIT — 9 sites at dim 3, 2 at rank 4, 7 sites carrying `J` on `H`, 17 `.md` files consuming `F_A^+`. Lean: `instanton.lean` / `self-dual-curvature.lean` gate self-duality on `cr.n = 2`; `CRManifoldData` pins nothing. |
| **3** `computations/` | ✔ | **EMPTY** for contact/CR/Levi (2 files, 1 deprecated). HIT for `S^7` — `form_stabilizer_genericity_su3_routes.py:21`. |
| **4** `docs/coordination/` | ✔ | HIT — `s5-so3-keystone.md:31,47,51`: compact/finite-dimensional Sasakian arenas excluded **for hosting `W_λ`** (different question; see §2.5). |
| **5** `library/` — INDEX + `summary.json` + `sections/` + **`ocr/`** | ✔ | **EMPTY.** `Sasakian` 0/0, `CR manifold` 0/0, `7-manifold` 0/0, `quaternionic contact` 0/0, `S^7` 0/0. Nothing held to cite on the corpus's entire CR/contact layer. |
| **6** `.beans/` (status + full bodies) | ✔ | **EMPTY** for `Levi distribution` / `ker Θ` / `contact distribution` / `Levi form` / `CR complex structure`. HIT for `Sasaki`: `qou-8p1g` (completed — the `m ≥ 2` / dim ≥ 8 pointer, and the `Sp(3)/Sp(1)³` closure), `s5bb`, `wlk9`. |

**Spellings varied** (per the `\mathrm{Sp}(1)` trap): `ker Θ` / `ker \Theta` /
`\ker\Theta` / `\ker \varTheta` / `H = \ker`; `Sasaki` / `Sasakian` /
`3-Sasakian` / `Sasaki-Einstein` / `Sasaki–Einstein` (en dash); `G_2` / `G₂` /
`\mathrm{G}_2` / `G_{2}`; `7-manifold` / `seven-manifold` / `7-dimensional` /
`seven-dimensional` / `dim M = 7` / `dimension 7`; `hyperkähler` / `hyperkahler`;
`quaternionic-Kähler` / `quaternionic Kahler` / `quaternionic-Kahler`;
`nearly Kähler` / `nearly Kahler`. The en-dash spelling of Sasaki–Einstein is the
one that matters — the hyphen spelling returns 0 in `content/` and the en dash
returns 1.
