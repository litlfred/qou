# Survey: the QOU axiom system (monoidal / rigid / braided / dagger) and the running SU(2) example (2026-09-15)

**Purpose.** Input to the analysis in [`2026-09-15-chi-as-a-component-of-the-chern-character.md`](2026-09-15-chi-as-a-component-of-the-chern-character.md) (issue #7425, session milestone `qou-dgce`). Produced by a read-only survey agent this session and transcribed here unchanged apart from this preface and the removal of the agent's note that it could not write the file; paths were spot-checked by the session before commit. Read it as a **measurement of the corpus on `main` at `0509e4010`** (and, where stated, of the #7420 head `607d3874a`), not as an assessment — the assessment is in the analysis doc.

---

**Date** 2026-09-15 · **Read-only survey** · `origin/main` = `0509e4010`, working tree `c5c3c7b20`, PR #7420 branch `claude/antipode-anti-automorphism-package-2026-09-15` = `607d3874a`

Owner's framing, verbatim: *"we may have mixed up a bit the qou axioms and when we actually need rigid and or braided monoidal. what we need i guess is that QOU axioms still let us sl_2^q then its category of representations is a braided rigid monoidal category. what is the current state. how do we clean up?"*

## 0. Method

Commands run (all read-only), with counts:

| # | command | result |
|---|---|---|
| 1 | `git fetch origin claude/antipode-anti-automorphism-package-2026-09-15` | new remote ref `607d3874a` |
| 2 | `git diff origin/main...origin/claude/... --stat` | **28 files, +1349 / −463**; **19** are `.lean` |
| 3 | `git diff origin/main...origin/claude/... \| grep -c "^+.*BraidedCategory"` | **64** added lines mentioning `BraidedCategory` |
| 4 | same, `\| grep -o "\[(CategoryTheory\.)?BraidedCategory X\]"` | **60** added binder occurrences (bean `qou-k4zx` says "55") |
| 5 | `grep -rn "structure QuantumUniverse" content/quantum-observable-universe/lean/` | **1** hit: `CategoricalFoundations.lean:180` |
| 6 | `grep -rn "structure QuantumObservableUniverse\|structure QOUData"` | **1** hit: `CategoricalFoundations.lean:362` |
| 7 | `grep -rn "RigidCategory" --include=*.lean QOU/ ../*/*.lean` | **50** (0 in mathlib pkg, which was excluded) |
| 8 | `grep -rn "BraidedCategory" --include=*.lean QOU/ \| wc -l` | **81** lines, in **21** files; `[BraidedCategory X]`-shaped binders = **26** |
| 9 | `grep -roh "β_\|braiding\|hexagon" --include=*.lean QOU/ \| sort \| uniq -c` | `β_` **986**, `braiding` **415**, `hexagon` **28** |
| 10 | `grep -rn "SymmetricCategory" QOU/` / `RibbonCategory\|BalancedCategory` / `PivotalCategory\|Spherical\|spherical` | **11** / **115** / **146** |
| 11 | `grep -rn "\.braidedInst\|\.rigidInst\|\.balancedInst" --include=*.lean content/` | **0 field reads.** Only declaration sites. |
| 12 | `grep -rn "\.catInst\|\.monInst" --include=*.lean content/` | **32** field reads |
| 13 | python walk of the 3 chapter `.ts` manifests (section → block order, builder kind, `examples[]`) | see §6 |
| 14 | python cross-chapter `examples[]` reachability over `content/*/*.ts` | 13 orphan `ex:` blocks in the 3 chapters |
| 15 | `grep -rn "base manifold\|smooth manifold\|algebraic variety\|complex manifold\|Riemann surface\|archimedean tuple\|scheme"` over the 3 chapters + `brings-surface/` | see §7. **`descartes-universe` chapter does not exist** — `ls content/quantum-observable-universe/ \| grep -i descartes` → empty; the Descartes material is `brings-surface/` + `climax-volume-mass/`. |
| 16 | `ls .beans/ \| wc -l` | **5302** beans; on-topic filename filter → ~190 |

---

## 1. The axiom blocks

### 1a. `def:quantum-universe` — `content/quantum-observable-universe/quantum-universes/quantum-universe.{ts,md,lean}`

`.ts:4` `label: "def:quantum-universe"`, kind `definition`, `lean.ref: "qou:QOU.QuantumUniverse"`, `validation: "not_checked"`, `uses: ["def:rigid-monoidal-category"]`, `examples: ["ex:quantum-universe-su2"]`.

**Structure assumed on C, quoted from `.md`:**

- `.md:3` — *"an $R$-linear braided [monoidal category](#def:rigid-monoidal-category) $\mathbf{C}$ over a commutative ring $R$, whose unit endomorphisms recover the ground ring: $R \xrightarrow{\ \sim\ } \mathrm{End}_{\mathbf{C}}(\mathbf{1})$"*
- `.md:24` — **"Rigidity of $\mathbf{C}$ is not required here. It is imposed on a [quantum observable universe](#def:quantum-observable-universe), where duals carry the antiparticles."**
- `.md:8` axiom 1 *(Temporal braiding)*: *"The ordering $\prec_c$ induced by the braiding $c_{V,W} \colon V \otimes W \xrightarrow{\sim} W \otimes V$ on the Hecke basis of $A$ is well-founded."*
- `.md:10` axiom 3 *(Symmetric Frobenius)*: *"The left and right categorical traces on $\mathrm{End}(A)$ coincide."*
- `.md:11` axiom 4 *(Wedderburn semisimplicity)*.
- **Not in the .md at all:** ribbon / twist / balanced, pivotal, spherical, abelian, dagger. No `[Preadditive]`-equivalent prose beyond "$R$-linear".

**Lean binders (`lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean:180–340`)** — instance fields, verbatim:

```lean
structure QuantumUniverse (R : Type*) [CommRing R] where
  C : Type u
  [catInst    : CategoryTheory.Category.{v} C]
  [monInst    : CategoryTheory.MonoidalCategory C]
  [preInst    : @CategoryTheory.Preadditive C catInst]
  [linInst    : @CategoryTheory.Linear R _ C catInst preInst]
  [braidedInst: @CategoryTheory.BraidedCategory C catInst monInst]
  [balancedInst: @QOU.BraidKnot.Balanced.BalancedCategory C catInst monInst braidedInst]
```

So Lean carries **strictly more than the .md**: `Preadditive`, `Linear R`, and a **balancing twist** (`BalancedCategory` = ribbon-minus-duals, in-repo class, bean `rtrb`). `.md` never mentions the twist; the twist's own docstring (line 210 ff.) says:

> *"**The balancing twist** `θ_X : X ⟶ X` (axiom 1, categorical half). … This is what makes the substrate parameter `q` *derivable rather than carried*. … **Sphericality on all of `C`.** Axiom 3 gives left-trace = right-trace on `End(A)` only, but the Markov trace closes strands of `V^{⊗n}`, not of `A`. Ribbon = braided + spherical extends it to the objects the knot theory actually uses."*

And the anti-rigidity instruction, line 173–177:

> *"**Rigidity is deliberately absent here.** A quantum universe is braided but need not have duals; duals are imposed one level up, on `QuantumObservableUniverse` … **Do not add a `RigidCategory` instance to this structure.**"*

**Remaining full field list of `QuantumUniverse`** (not instance fields): `frobHopf`, `fibreFunctor`, `frobenius_symmetric`, `unitEndEquiv`, `blocks`, `[blocksFintype]`, `centralIdem`, `centralIdem_idem`, `centralIdem_orthogonal`, `centralIdem_complete`, `frobWeight`, `frobWeight_isUnit`, `dimQ`, `dimQ_isUnit`, `differentialForms`.

`fibreFunctor` docstring (line 241) records the gap verbatim:

> *"The paper asks for it to be exact, faithful, `R`-linear and monoidal; NONE of those four is carried by this type, which is a bare functor to `Type`."*

**Three divergent copies exist.** Same structure name in three files with different field sets:
- `lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean:180` (canonical; `fibreFunctor` only)
- `quantum-universes/quantum-universe.lean:126` (co-located sibling; **has an extra `fibreFunctor_faithful` field at :195**)
- `quantum-observable-universes/quantum-observable-universe.lean:110` (second co-located copy; `QuantumObservableUniverse` at :286, `rigidInst` at :293)

This is the `qou-hmhw` pattern ("Three structures named `FrobeniusHopfSubstrate` with different field sets — the markovZ overload defect again") repeating for `QuantumUniverse`.

**Stale docstring — decisive.** `quantum-universes/quantum-universes.ts:6`:

> *"The QU axioms: a rigid **symmetric** monoidal category with a Frobenius--Hopf object…"*

That is **wrong on both counts** against `.md:3`/`.md:24` (braided, not symmetric; not rigid). This is the single clearest "mixed up" artefact in the chapter.

### 1b. `def:quantum-observable-universe` + the three extra axioms — `quantum-observable-universes/quantum-observable-universe.{ts,md,lean}`

`.ts:4` `label: "def:quantum-observable-universe"`, `lean.ref: "qou:QOU.QuantumObservableUniverse"`, `uses: ["def:quantum-universe","def:rigid-monoidal-category","def:snake-identity","unital-groebner-bases:def:admissible-system"]`, `examples: ["ex:qou-su2","ex:c-quantum-observable-universe","ex:c-quantum-universe","rem:yekutieli-stokes"]`.

**`.md:1` opens with FIVE conditions, not three:** *"A quantum universe $(\mathbf{C}, A, \tau)$ over $R$ is a **quantum observable universe** if the forgetful functor $\tau$ is faithful and five conditions hold"*

1. `.md:3` *(Rigidity)* — *"Every object $V \in \mathbf{C}$ has a dual $V^{\vee}$, with evaluation $\mathrm{ev}_V$ … and coevaluation $\mathrm{coev}_V$ … satisfying the [snake identities](#def:snake-identity)."*
2. `.md:4` *(Non-degenerate integration)* — *"$\int_A$ induces an isomorphism $A \xrightarrow{\sim} A^{\vee}$"*
3. `.md:5` *(Observability)* — *"There are no hidden global symmetries: $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$."*
4. `.md:6` *(Measurability)* — *"The categorical Chern classes of the adjoint object vanish: $c_1(\mathrm{Ad}(A)) = 0$ and $c_2(\mathrm{Ad}(A)) = 0$."*
5. `.md:7` *(Categorical volume constraint)* — *"…there is an **isomorphism** $\epsilon \colon \Lambda^2 V \xrightarrow{\ \sim\ } \mathbf{1}$ preserved by all tensor automorphisms"*

**`.md:22` is the one-line statement of the whole rigid/braided split:**

> **"A quantum universe is thus braided; a quantum observable universe is braided and rigid."**

**Lean (`CategoricalFoundations.lean:362–455`):**

```lean
structure QuantumObservableUniverse (R : Type*) [CommRing R]
    extends QuantumUniverse.{u, v} R where
  [rigidInst : @CategoryTheory.RigidCategory C catInst monInst]
  adjointObj : C
  adjointIncl : adjointObj ⟶ frobHopf.obj
  adjoint_mono : CategoryTheory.Mono adjointIncl
  adjoint_augmented : adjointIncl ≫ frobHopf.counit = 0
  adjoint_nontrivial : adjointIncl ≠ 0
  adjoint_vanishing : Subsingleton ((𝟙_ C) ⟶ adjointObj)
  fundamentalObj : C
  exteriorSquare : C
  exteriorSquareProj : (fundamentalObj ⊗ fundamentalObj) ⟶ exteriorSquare
  exteriorSquare_epi : CategoryTheory.Epi exteriorSquareProj
  volumeIso : exteriorSquare ≅ (𝟙_ C)
```

**Mismatch, decisive:** the **measurability axiom (condition 4, Chern classes) has NO field in the Lean structure.** Grep for `chern|Chern|c_1|c_2` in `lean/QOU/QuantumObservableUniverse/` returns only `exists_axiom_3_chern.lean`, a *separate* existence-lemma carrier whose own docstring (line 18–24) says *"only the … object and its first two categorical Chern classes `c_1, c_2 ∈ ℝ`. The vanishing conclusion is **not** a field here"*. So the .md has 5 conditions, the Lean structure encodes 4 (rigidity, observability-as-adjoint-vanishing, volume, plus non-degeneracy structurally via the snake identities in `FrobeniusHopfData`), and measurability is prose-only.

Also: the `adjointObj` docstring (line 368) records that the braiding *should* build `Ad(A)` but does not:

> *"In a braided monoidal category it is constructed from `(A, μ, Δ, S)` and the braiding; **that construction is not available here**, so the object is provided together with the three fields below."*

And the `exteriorSquare_epi` docstring (line 423) is the one place braiding is *deliberately not* used:

> *"**Deliberately no eigenvalue condition on the braiding.** In a braided category the braiding acts on the `q`-exterior square by `-q⁻¹`, not by `-1`, so demanding `β ≫ π = -π` would silently impose `q = 1` and rule out the quantum group the framework is about."*

### 1c. `def:frobenius-hopf-substrate` — `quantum-observable-universes/frobenius-hopf-substrate.{ts,md,lean}`

`.ts:4` label, `lean.ref: "qou:QOU.AlgebraicSubstrate.FrobeniusHopfSubstrate"`, `uses: ["def:frobenius-pairing"]`, **`examples:` absent**.

**`main` — `.md:1`:** *"Let $\mathbf{C}$ be a **monoidal** category."* → monoidal only.
**`main` — `.md:21`, decisive:**

> *"**Duals are required of $A$ only, not of $\mathbf{C}$.** Axiom 4 supplies $\mathrm{coev}$ as part of the data, so $A$ carries its own duality datum and no object of $\mathbf{C}$ other than $A$ need have a dual. Consequently a Frobenius--Hopf object is available already at the level of a [quantum universe](#def:quantum-universe), which is braided monoidal but *not* rigid."*

**`main` Lean binders** — `CategoricalFoundations.lean:60`:
```lean
structure FrobeniusHopfData (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
```
and co-located `frobenius-hopf-substrate.lean:32`: `[Category.{v} C] [MonoidalCategory C]`. **No braiding, no rigidity.** 21 fields; antipode constrained by `antipode_left` / `antipode_right` (the convolution/Hopf condition, added 2026-09-14 per beans `qou-c64q`/`qou-qjhc`).

**#7420 state — `.md:1` becomes:** *"Let $\mathbf{C}$ be a **braided** monoidal category, with braiding $\beta$."*
New axiom 2 asserts six antipode laws; the .md adds, verbatim:

> *"The braiding $\beta$ is what makes "reverses" expressible, which is why $\mathbf{C}$ is taken braided; that is no extra demand, since the substrate is invoked at the level of a [quantum universe](#def:quantum-universe), which is braided monoidal."*
> *"**$S$ is constrained but not determined.** … the only condition that does is the convolution identity … and that identity forces $A$ to be trivial whenever the scalars form a field, so it cannot be imposed here."*

**#7420 Lean:** `FrobeniusHopfData (C) [Category] [MonoidalCategory C] [CategoryTheory.BraidedCategory C]`; `antipode_left`/`antipode_right` **deleted**, replaced by `antipode_anti_mul`, `antipode_anti_comul`, `antipode_unit`, `antipode_counit`, `antipode_involutive`, `antipode_frobeniusForm`; and `QuantumUniverse.frobHopf : @FrobeniusHopfData C catInst monInst` → `... catInst monInst braidedInst`. The PR's audit note (`docs/audits/2026-09-15-antipode-anti-automorphism-package.md`) makes the load-bearing point:

> *"`QOU.QuantumUniverse` **already carried a `braidedInst` field**, so its `frobHopf` field needed only `@FrobeniusHopfData C catInst monInst braidedInst` — the instance was sitting there unused."*

**Note the co-located `frobenius-hopf-substrate.lean` in #7420 is TRUNCATED** — the diff ends `/-- **Antipode axiom 5 — `S` is invol` with `\ No newline at end of file`. That sibling is syntactically broken on the PR branch.

### 1d. `def:rigid-monoidal-category` — `quantum-universes/rigid-monoidal-category.{ts,md,lean}`

`.ts:4` label, `lean.ref: "qou:QOU.RigidMonoidalCategory"`, `uses: ["def:snake-identity","rem:glossary-no-quasi-zeros"]`, `examples: ["ex:rigid-monoidal-vect"]`.

This one block defines **four** separate notions in sequence, which is a large part of the tangle:
- `.md:1` monoidal;
- `.md:29` *"The category is *rigid* if every object $V$ has a dual $V^{\vee}$ together with morphisms $\mathrm{ev}_V \colon V \otimes V^{\vee} \to \mathbf{1}$ and $\mathrm{coev}_V \colon \mathbf{1} \to V^{\vee} \otimes V$ satisfying the [snake identities](#def:snake-identity)."*
- `.md:31` *"We say $\mathbf{C}$ is *$R$-linear* … if every hom-set is an $R$-module and composition is $R$-bilinear."*
- `.md:33` *"The category is *braided monoidal* if it has a natural isomorphism $c_{X,Y}$ … satisfying the hexagon axioms. The braiding is *symmetric* when $c_{Y,X} \circ c_{X,Y} = \mathrm{id}$. Given a braiding, the *exterior power* $\Lambda^k V$ is the image of the antisymmetriser …"*

Its Lean sibling `rigid-monoidal-category.lean:31` is **not** a class on C but a per-object datum: `structure RigidMonoidalCategory (C) [Category] [MonoidalCategory C] where V : C; V_dual : C; eval; coeval; snake_left; snake_right`. So `def:rigid-monoidal-category` **does not correspond to Mathlib's `RigidCategory`** even though `QuantumObservableUniverse.rigidInst` uses Mathlib's. No `Preadditive`/`Linear`/`Braided` binder appears in that file at all, so the `.md`'s $R$-linearity and braiding clauses are unformalised there.

### 1e. `def:braided-*` — **not found on the surface searched**

`grep -rho 'label: "[a-z]*:[^"]*braided[^"]*"' content/` returns exactly one label: `rem:glossary-braided-monoidal-category`. There is **no `def:braided-monoidal-category`, no `def:braided-rigid-*`, no `def:ribbon-*`, no `def:spherical-*`, no `def:balanced-*`, no `def:pivotal-*`** anywhere in `content/`. Braiding is defined only as a clause inside `def:rigid-monoidal-category` (`.md:33`) plus glossary defterms:
- `glossary/glossary-braided-monoidal-category.md:1` — *"A monoidal category equipped with a natural isomorphism $\beta_{X,Y} \colon X \otimes Y \xrightarrow{\sim} Y \otimes X$ satisfying the two hexagon axioms."* + `Notation: β_ X Y`.
- `glossary/glossary-rigid-category.md:1` — *"A monoidal category in which every object has both a left dual and a right dual."* Mathlib ref `CategoryTheory.RigidCategory`.
- `glossary/glossary-symmetric-monoidal-category.md:1` — *"A braided monoidal category whose braiding is involutive."*
- `glossary/glossary-pivotal-category.md` — *"A rigid monoidal category equipped with a monoidal natural isomorphism $\delta_X \colon X \xrightarrow{\sim} X^{\vee\vee}$ …"* and, decisively: *"**Mathlib reference.** None — there is no `CategoryTheory.PivotalCategory`. … The classes this paper needs are therefore built in-repo, as `PivotalStructure` and `SphericalStructure` in `QOU/BraidKnot/KeystonePivotalSpherical.lean`."*

### 1f. `def:fibre-functor` — **not found on the surface searched**

`grep -rho 'label: "[^"]*fib[re]*-functor[^"]*"' content/` yields only `prop:fibre-functor-atlas`, `prf:fibre-functor-atlas`, `rem:fibre-functor-atlas-affine-charts`, `rem:fibre-functor-rigidity`, `conj:q-gl-fiber-functor`, `rem:q-gl-fiber-functor-sketch`. **There is no definition block for the fibre functor.** It is defined inline in `def:quantum-universe` `.md:5` — *"an $R$-linear faithful fibre functor $\tau \colon \mathbf{C} \to R\text{-}\mathbf{Mod}$"* — and the closest definitional block is `def:tannaka-dual` (`quantum-universes/tannaka-dual.md:1`): *"Let $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$ be the fibre functor."* The nearest constraint block is `rem:fibre-functor-rigidity` (`.md:1`): *"The fibre functor $\tau$ plays a rigid, passive role precisely because of the observability axiom."* — note "rigid" there is unrelated to duals; it means "unable to move".

### 1g. `def:dagger-*` — **no such label.** The dagger is `def:involutive-structure`

`quantum-universes/involutive-structure.{ts,md}`; `.ts:4` `label: "def:involutive-structure"`, `title: "Involutive structure ($\\ast$-structure)"`, `lean.ref: "qou:QOU.InvolutiveStructure"`, `uses: ["def:rigid-monoidal-category"]`, `examples: ["ex:dagger-su2"]`.

`.md:1`, decisive — it assumes **rigid**, inside the QU chapter, where C is not rigid:

> *"Let $(\mathbf{C}, \otimes, \mathbf{1})$ be an $R$-linear **rigid** monoidal category. An **involutive structure** on $\mathbf{C}$ is a contravariant endofunctor $\dagger \colon \mathbf{C}^{\mathrm{op}} \to \mathbf{C}$ satisfying: 1. **Identity on objects:** $X^{\dagger} = X$. 2. **Involutivity:** $f^{\dagger\dagger} = f$ … 3. **Monoidal compatibility** … 4. **Contravariance** …"*

Its Lean (`QOU/QuantumObservableUniverse/Structures.lean:45`) assumes **less**: `structure InvolutiveStructure (C) [Category] [MonoidalCategory C]` — no rigidity, no linearity. `PositiveDefiniteStructure` at :71 adds `[Preadditive C]`. So the .md over-assumes rigidity and the Lean under-assumes it; they are inconsistent in *opposite* directions. See §5.

---

## 2. The Lean structures: fields and consumers

### `QOU.QuantumUniverse` — `lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean:180`

Instance fields: `catInst`(184), `monInst`(185), `preInst`(195), `linInst`(203), `braidedInst`(209), `balancedInst`(238). **No `rigidInst`, no pivotal, no spherical, no dagger, no abelian, no semisimple-as-typeclass** (semisimplicity is hand-rolled as the `blocks`/`centralIdem` fields).

Data/prop fields: `frobHopf`(240), `fibreFunctor`(246), `frobenius_symmetric`(256), `unitEndEquiv`(266), `blocks`(306), `blocksFintype`(307), `centralIdem`(309), `centralIdem_idem`(311), `centralIdem_orthogonal`(315), `centralIdem_complete`(323), `frobWeight`(325), `frobWeight_isUnit`(331), `dimQ`(333), `dimQ_isUnit`(336), `differentialForms`(340).

### `QOU.QuantumObservableUniverse` — same file, :362, `extends QuantumUniverse.{u,v} R`

Adds `rigidInst`(366) + the 11 fields listed in §1b.

### Consumers that read `braidedInst` — **NONE**

`grep -rn "braidedInst" --include=*.lean content/` returns 8 lines, all declaration sites or the `balancedInst` binder that mentions it positionally:

```
lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean:209   (declaration)
lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean:238   (balancedInst binder)
quantum-universes/quantum-universe.lean:155 / :184                   (co-located copy)
quantum-observable-universes/quantum-observable-universe.lean:138 / :167  (co-located copy)
```

`grep -rn "\.braidedInst"` → **0 hits.** Same for `.rigidInst` and `.balancedInst`: **0 field reads.** By contrast `.catInst`/`.monInst` are read 32 times (`su2-emergence.lean:103,104,107,108,113,114,175,176,179,180`; `qou-exists-axiom-{1,2,3,4}.lean`; `frobenius-pairing-exists.lean:103–105`; `observation.lean:44` `attribute [local instance] QuantumUniverse.catInst QuantumUniverse.monInst`; `CategoricalFoundations.lean:526` in `gaugeGroup`; `categorical-mordell-weil.lean:55`; `QBirchSwinnertonDyer.lean:86`).

**This is the central finding for the owner's question.** On `main` the braiding and the rigidity of a QU/QOU are carried as instance fields that **nothing downstream consumes.** Every theorem stated *about* a `QuantumUniverse` re-derives from `catInst`/`monInst` only. #7420 changes this for exactly one field: `frobHopf` becomes `@FrobeniusHopfData C catInst monInst braidedInst`, making `braidedInst` load-bearing for the first time.

---

## 3. Where rigidity is USED vs. where it is a blanket binder

### 3a. Rigidity in Lean (50 hits in `QOU/` + co-located siblings)

**Needed for a stated theorem** (all in the knot/ribbon machinery, and all over Mathlib's `RightRigidCategory` rather than `RigidCategory`):
- `QOU/MathlibExt/PivotalCategory.lean:215` — `class PivotalCategory (C) [Category C] [MonoidalCategory C] [RightRigidCategory C]`; :266, :305 add `[BraidedCategory C]`.
- `QOU/MathlibExt/SphericalCategory.lean:84` — `class SphericalCategory (C) … [RightRigidCategory C]`.
- `QOU/MathlibExt/Ribbon.lean:173` — `… [RightRigidCategory C] extends BalancedCategory C where`; :185 `instance … [SymmetricCategory C] [RightRigidCategory C] : RibbonCategory C`.
- `QOU/MathlibExt/TwistedQuantumDimension.lean:87,182` — `[RightRigidCategory C] [RibbonCategory C]`.
- `QOU/MathlibExt/RigidTensorDual.lean:111,118,130`; `QOU/MathlibExt/BraidedQuantumDimension.lean:118`; `QOU/MathlibExt/BraidedTensorDual.lean:198`.
- `QOU/BraidKnot/KeystoneFramedTangleScaffold.lean:147`, `KeystoneRibbonMTCInput.lean:52,72`, `KeystoneRibbonCategory.lean:74`, `KeystonePivotalSpherical.lean:104,167,182,257,286,308`.

**Evidence rigidity is treated as removable where unused** — `KeystoneFramedTangleScaffold.lean:193,200` and `KeystoneRibbonCategory.lean:76` carry explicit `omit [RightRigidCategory 𝒞] in`, and `KeystoneRibbonCategory.lean:82`: *"(`RightRigidCategory` is omitted — only the unit's exact pairing is needed.)"* That is the discipline the axiom structures do not follow.

**Blanket binder, no consumer:** `QuantumObservableUniverse.rigidInst` (`CategoricalFoundations.lean:366`, and the co-located `quantum-observable-universe.lean:293`). 0 field reads.

`ExactPairing`, `HasLeftDual`, `HasRightDual` — **not found in `QOU/`** outside `MathlibExt`; the `FrobeniusHopfData` self-duality is hand-rolled as `coevaluation` + `pairing_snake_left`/`pairing_snake_right` (`CategoricalFoundations.lean:79–94`), with `ev` derived at :151 (`def ev := F.mul ≫ F.frobeniusForm`) and `leftTrace`/`rightTrace` at :155/:160.

### 3b. Rigidity in the `.md` of the three chapters

Used **explicitly and with the hypothesis restated locally** — which is the pattern `quantum-universes-intro.md:16` promises (*"the constructions later in this chapter that do use duals — the involutive structure, the categorical Hodge star, the internal Poisson object — say so in their own hypotheses"*):

- `quantum-universes/involutive-structure.md:1` — *"Let … be an $R$-linear **rigid** monoidal category"*
- `quantum-universes/fundamental-object.md:1` — *"Let $\mathbf{C}$ be an $R$-linear rigid monoidal category."*
- `quantum-universes/simple-objects-V.md:1` — *"Simple objects are the irreducible building blocks of a rigid monoidal category $\mathbf{C}$."*
- `quantum-observable-universes/volume-from-rigidity.md:1` — *"Let … be an $R$-linear rigid monoidal category, and let $V$ be a simple object that is symplectically self-dual … This alternating condition forces $\mathrm{rank}(V) = 2$."*
- `quantum-observable-universes/categorical-action-exists.md:1` — uses `ev_A`, `coev_A`, `A^\vee` directly.
- `quantum-universes/outro-quantum-universes.md:1`, decisive: *"Rigidity enters here and not in the quantum-universe axioms: the Hodge star and the class in $\Lambda^2 (\Omega^1)^\vee$ are stated over a category with duals, and each such construction carries that hypothesis explicitly."*

Explicitly-flagged absence: `quantum-universes/quantum-universe-axiom-motivation.md:25` — *"**What is deliberately absent.** Rigidity. A quantum universe need not have duals."*; `quantum-universes/frobenius-pairing-exists-proof.md:10` — *"**not** rigid — $\mathbf{C}$ carries no duality functor, so there is no … Those identities *exhibit $A$ as its own dual*; they are not consequences of a rigid structure."*

**But prose elsewhere in the corpus contradicts the split**, calling C rigid at the QU level or unqualified:
- `quantum-universes/rigid-monoidal-intro.md:1` — *"Why do the axioms of a physical theory land on a rigid braided monoidal category?"*
- `quantum-universes/quantum-universes-intro.md:7` — *"$\mathbf{Rep}(\mathrm{SU}_q(2))$ … is a rigid braided monoidal category carrying a Frobenius--Hopf object"* (correct as a statement about the *example*)
- `quantum-observable-universe.ts:17` (paper abstract) — *"the Quantum Observable Universe (QOU): a **rigid braided monoidal category** equipped with a Frobenius--Hopf object"* (correct for QOU)
- `mass-theory/em-spectral-completeness.md:8`, `mass-theory/wenzl-bridge-applicability-qou-proof.md:67`, `mass-endomorphism/categorical-neutrality-saturated-shells.md:5`, `mass-endomorphism/phi-n-global-section.md:5`, `climax-volume-mass/vertex-algebra-relations.md:17` (*"### QU-1: Rigid braided monoidal structure"* — **mislabels it QU-1**), `models-of-qous/step-categorical.md:1`, `models-of-qous/framing-arc-intro.md:3`, `appendix-surreals/millennium-unification.md:29`, `appendix-surreals-archimedean/algebraic-core-survives.md:91`, `knots-particles-confinement/hadron-operations-closure.md:1`.

`rigid-monoidal-intro.md:3` gets it right and is the model sentence for a cleanup: *"A quantum universe is braided: it has interactions. A quantum observable universe is braided *and* rigid: it also has duals, hence antiparticles and closed knots."*

### 3c. Braiding in Lean

`β_` 986, `braiding` 415, `hexagon` 28 occurrences in `QOU/`; `[BraidedCategory X]`-shaped binders **26**, across **21** files. Used for stated theorems throughout `BraidKnot/` and `MathlibExt/` (braid-group action, quantum dimension, Drinfeld iso, ribbon). Blanket-binder, unconsumed: `QuantumUniverse.braidedInst` on `main`.

### 3d. Braiding in the `.md`: assumed data, never derived

- `quantum-observable-universes/braiding-eigenvalue-extraction.md:1` — *"Let $V$ be the fundamental object with braiding $c_{V,V}$ … Because $\Lambda^2 V \cong \mathbf{1}$, $c_{V,V}$ acts on it by a scalar $\lambda_-$ … We define the substrate parameter as: $q := \lambda_+$, $\lambda_- = -q^{-1}$ … These eigenvalues encode the Hecke relation $(T - q)(T + q^{-1}) = 0$."*
- `quantum-observable-universes/braiding-eigenvalue-extraction-novelty.md:3`, decisive: *"**What this does not settle is the value.** The braiding is *assumed data* — a braided monoidal category comes equipped with a braiding, and different braidings give different eigenvalues."*
- `quantum-universes/axiom-independence.md:3` — *"We require only a braiding, and only over a commutative ring, so the fibre functor is not supplied for us. The braiding axiom is independent of the fibre functor."*
- `knots-particles-confinement/interactions-are-pairwise-intro.md:3` — *"A braided monoidal category is by definition one whose exchange datum is binary, and the hexagon identities … are **axioms of the structure, not consequences of it**."*

### 3e. PR #7420's `[BraidedCategory C]` additions

Diff: **28 files, +1349/−463; 19 `.lean` files.** `grep -c "^+.*BraidedCategory"` = **64**; binder-shaped matches on added lines = **60**; bean `qou-k4zx` states **55**. Per-file added/removed `BraidedCategory` mentions:

| file | +/− |
|---|---|
| `.beans/qou-c64q--*.md` | +1 / 0 |
| `.beans/qou-k4zx--*.md` | +2 / 0 |
| `content/.../lean/QOU/CategoricalDqSquared.lean` | +1 |
| `content/.../lean/QOU/ChannelSeparation.lean` | +2 |
| `content/.../lean/QOU/GradedFrobeniusHopf.lean` | +2 |
| `content/.../lean/QOU/LightningPath.lean` | +2 |
| `content/.../lean/QOU/QuantumObservableUniverse/AntipodeDetermined.lean` | +2 |
| `content/.../lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean` | +5 |
| `content/.../lean/QOU/QuantumObservableUniverse/DqTwist.lean` | +1 |
| `content/.../lean/QOU/QuantumObservableUniverse/FrobeniusBialgebraCollapse.lean` | +1 |
| `content/.../lean/QOU/QuantumObservableUniverse/FrobeniusHopfModelDichotomy.lean` | +1 |
| `content/.../lean/QOU/QuantumObservableUniverse/GaugeTheory.lean` | **+11** |
| `content/.../lean/QOU/QuantumObservableUniverse/Instanton.lean` | **+17** |
| `content/.../lean/QOU/QuantumObservableUniverse/Structures.lean` | +1 |
| `content/.../lean/QOU/QuantumObservableUniverse/TrivialWitness.lean` | +1 |
| `content/.../lean/QOU/QuantumObservableUniverse/VolumeForm.lean` | +1 |
| `content/.../lean/QOU/QuantumObservableUniverses/QDifferentialGeometry.lean` | +3 |
| `content/.../lean/QOU/RepresentationTheory.lean` | +1 |
| `content/.../lean/QOU/Torsion/Descent.lean` | +2 |
| `content/.../lean/QOU/Torsion/JetProlongation.lean` | +1 |
| `content/.../quantum-observable-universes/frobenius-hopf-substrate.lean` | +4 |
| `docs/audits/2026-09-15-antipode-anti-automorphism-package.md` | +2 |

**The six blanket-patched files**, named verbatim by `.beans/qou-k4zx--*.md` (PR-only bean):

> *"Six files were patched with a BLANKET regex that added the instance to EVERY `MonoidalCategory` binder in the file, including declarations that never touch `FrobeniusHopfData`. Those declarations are now over-constrained: usable only in a braided category where any monoidal one would previously do. … **Files to check first are the six blanket-patched ones: `Instanton`, `ChannelSeparation`, `LightningPath`, `QDifferentialGeometry`, `Torsion/Descent`, `CategoricalDqSquared`.**"*

Also in #7420: `Structures.lean` gains `[BraidedCategory C]` on `HigherForms` purely so `frobHopf : @FrobeniusHopfData C _ _` can become `_ _ _` — a pure ripple, no braiding used in the body.

---

## 4. The Tannaka–Krein / reconstruction chain, and where `sl_2^q` emerges

### 4a. Where the corpus says "Rep(…) is a braided rigid monoidal category"

| block | quote | status of the braiding |
|---|---|---|
| `quantum-universes/quantum-universes-intro.md:6–8` | *"$\mathbf{Rep}(\mathrm{SU}_q(2))$, the category of representations of the quantum group, is a rigid braided monoidal category carrying a Frobenius--Hopf object, and it is the guiding example throughout this chapter"* | **asserted in prose**, no citation, no derivation |
| `quantum-observable-universes/quantum-observable-universe-exists-proof.md:8–11` | *"take $\mathbf{C} := \mathbf{Rep}(U_{q}(\mathfrak{g}))$ — the **rigid ribbon braided monoidal category** of finite-dimensional type-I representations of the **Drinfeld--Jimbo** quantum group \cite{chari1994guide, kassel1995}"* | **cited to the literature** (Chari–Pressley, Kassel); the only place "ribbon" is claimed of C; **not derived in-repo** |
| `quantum-observable-universes/quantum-observable-universe-exists.md:1` | *"Setting $\mathbf{C} = \mathbf{Rep}(U_q(\mathfrak{sl}_2))$, $A = \mathcal{O}_q(\mathrm{SU}(2))$, and $\tau$ to the forgetful functor realizes the axioms explicitly."* | asserted |
| `quantum-universes/rigid-monoidal-vect.md:5` | *"The category $\mathrm{Rep}(\mathrm{SU}(2))$ of finite-dimensional representations is $\mathbb{C}$-linear rigid monoidal."* | classical $q=1$ case; no braiding named |
| `quantum-observable-universes/q-dilogarithm-properties.md:1` | *"The universal $R$-matrix of $U_q(\mathfrak{sl}_2)$ admits the Faddeev--Kashaev factorisation. The logarithm of $\mathcal{R}$ matches the $q$-dilogarithm at leading order. $\mathrm{Li}_2^q$ constitutes the categorical braiding potential."* | **the only mention of the R-matrix in the three chapters** — and it is used to *interpret* the braiding, not to construct it |

### 4b. Where SU(2) / sl_2^q EMERGES, and what the braiding's status is at each step

1. **`prop:braiding-eigenvalue-extraction`** (`quantum-observable-universes/braiding-eigenvalue-extraction.md`) — `q` read off `c_{V,V}`. Braiding **ASSUMED** (its own novelty remark says so: *"The braiding is *assumed data*"*).
2. **`prop:tannaka-krein-reconstruction`** (`quantum-observable-universes/tannaka-krein-reconstruction.md:1`) — *"By Tannaka--Krein duality, the coend $H = \mathrm{End}^{\otimes}(\tau) = \int^{X \in \mathbf{C}} \tau(X)^{\vee} \otimes_R \tau(X)$ carries a canonical Hopf algebra structure. This provides the monoidal equivalence $\mathbf{C} \simeq \mathrm{Rep}(H)$. **For generic braiding, $H$ reconstructs the compact quantum group algebra $\mathcal{O}_q(G)$. The deformation parameter $q$ is determined by the braiding.**"* → the quantum group is **derived FROM the braiding on C**, not the other way round. Note the coend formula uses $\tau(X)^\vee$ — duals **in the target**, not in C.
3. **`rem:tannaka-krein-overview`** (`quantum-universes/tannaka-krein-overview.md:8`) — *"**Origin of $q$.** … when the braiding $c_{V,V}$ is non-symmetric, $q$ is its eigenvalue on $S^2 V$, and **Woronowicz's reconstruction recovers $\mathrm{SU}_q(2)$ with that $q$**. This fixes what $q$ *is*, not what it equals — the braiding is assumed data, so its eigenvalue is determined by the assumption rather than by anything upstream of it."*
4. **`def:tannaka-dual`** (`quantum-universes/tannaka-dual.md:5`) — *"When $(\mathbf{C}, \tau)$ is neutral Tannakian in the sense of Deligne, $G$ is an affine group scheme over $R$ and the reconstruction $\mathbf{C} \simeq \mathrm{Rep}(G)$ holds \cite{deligne1990}."* — Deligne's neutral-Tannakian theorem is the **symmetric** statement; citing it for the braided case is a genuine mismatch.
5. **`thm:su2-emergence`** (`quantum-observable-universes/su2-emergence.md`, `lean.ref: qou:QOU.su2_emergence_rank_forced`) — hypotheses `.md:3–4`: *"(volume) the volume form is non-degenerate in the strong sense $\Lambda^2 V \cong \mathbb{1}$"*; *"(realisation) the gauge group $G = \mathrm{Aut}^{\otimes}(\tau)$ acts on $\tau(V) \cong \mathbb{C}^N$ by matrices, each preserving the volume form ($\det g = 1$) and the Frobenius dagger ($g\,g^{\dagger} = 1$)"*. Conclusion $N=2$, $G \subseteq \mathrm{SU}(N)$. `.md:16`: *"**The two conclusions are independent, and only the first is about the rank.**"* `.md:20`: *"**What is assumed and not proved.** Hypothesis (2) is a realisation assumption … Nothing here derives that identification."* **The braiding plays no role at all** in this theorem; it is a linear-algebra statement over the fibre. `VolumeConstraintForcesFibreTwo.lean:122–168` is `exteriorSquareDim (N) := N.choose 2` on ℕ, with `exteriorSquareDim_eq_one_iff : … = 1 ↔ N = 2`.
6. **`def:quantum-gauge-group`** (`quantum-observable-universes/quantum-gauge-group.md:1`) — *"The reconstructed Hopf algebra $H = \mathrm{End}^{\otimes}(\tau)$ gives the **quantum gauge group** $G_q = \mathrm{SU}_q(2)$, with $q$ categorically fixed by the **symmetric braiding eigenvalue**."*
7. **`rem:sqrt-q-ribbon-structure`** (`quantum-observable-universes/sqrt-q-ribbon-structure.md:1`) — *"A **ribbon structure on $\mathbf{C}$ demands a natural twist** $\varTheta_V \colon V \xrightarrow{\sim} V$. On the defining $\mathrm{SU}_q(2)$ representation, the twist axiom forces $\varTheta_V = q^{1/2}\mathrm{id}_V$."* This is the only block that *requires* ribbon on C — and it sits in `sec:braiding-conventions`, a convention section held out of the axiom sections, while the Lean `QuantumUniverse` carries `balancedInst` as an axiom.
8. **`thm:qu-to-qou`** (`lifting-and-descent/qu-to-qou.md:1–5`) — *"Let $(\mathbf{C}, A, \tau)$ be a quantum universe over a Noetherian ring $R$ with substrate parameter $q$, satisfying the observability condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ … Then $(\mathbf{C}, A, \tau)$ **is** a quantum observable universe with the following structural properties…"* **Decisive mismatch:** this theorem promotes QU → QOU on observability + the lifting condition alone, and **never supplies rigidity** — which `def:quantum-observable-universe` condition 1 requires and `def:quantum-universe` `.md:24` explicitly withholds. Nor does it supply the Chern-class condition 4. As written, `thm:qu-to-qou` cannot be true with the current definitions.
9. `quantum-observable-universes/simplicity-from-category.md:1` — *"The categorical axioms mandate the sequence: volume constraint $\Rightarrow G_q = \mathrm{SU}_q(2) \Rightarrow F_A = B \Rightarrow B = F_A^+ \Rightarrow F_A^- = 0$."*; `emergence-to-quantum-flat.md:1` — *"For a QOU meeting the categorical volume constraint, $G_q \cong \mathrm{SU}_q(2)$."*

**Verdict on the braiding's provenance.** Nowhere in the corpus is the braiding on `Rep(SU_q(2))` **DERIVED** — not from the universal R-matrix of $U_q(\mathfrak{sl}_2)$ (mentioned once, `q-dilogarithm-properties.md:1`, and only as the dilogarithm's source), and not from the Frobenius–Hopf data (`adjointObj` docstring, `CategoricalFoundations.lean:368`: *"In a braided monoidal category it is constructed from `(A, μ, Δ, S)` and the braiding; **that construction is not available here**"*). It is **ASSUMED as an axiom on C** (`def:quantum-universe` item 1 + axiom 1) and then **ASSERTED in prose** of the model (`quantum-observable-universe-exists-proof.md:9`, cited to Chari–Pressley/Kassel).

**So the answer to the owner's target is: yes, the axioms do let you take C = Rep(U_q(sl_2)) — but the logic runs the wrong way for the framing.** The axioms *assume* braided-and-(at QOU level)-rigid and then *exhibit* Rep(U_q(sl_2)) as one model, citing the literature for the braiding/ribbon structure. They do not derive "Rep of the reconstructed group is braided rigid".

---

## 5. The dagger / involution: where it comes from and whether it is axiom or derived

**Three sources, and the corpus is explicit that the dagger is DERIVED, not axiomatic:**

1. **From the antipode + Frobenius form.** `quantum-universes/involutive-structure.md:43`, last line: *"For the Hopf algebra $A$ in a quantum universe, **the antipode $S$ provides an involutive structure** via $f^{\dagger} = \int_A \circ \mu(S(f) \otimes -)$."*
2. **`prop:positive-definite-dagger`** (`quantum-universes/positive-definite-dagger.md:1–9`), a *proposition*, not a definition: *"Let $(\mathbf{C}, A)$ be a quantum universe whose endomorphism ring $\mathrm{End}(\mathbf{1}) \cong R$ is a formally-real ordered field. Assume a [Frobenius pairing](#def:frobenius-pairing) and **a pivotal antipode $S$ that is self-adjoint for the pairing**. Define the *Frobenius dagger* … $f^{\dagger} = \int_A \circ\, \mu(S(f) \otimes -)$. The Frobenius dagger satisfies $S^2 = \mathrm{id}$ and restricts to $S = \dagger$ on $\mathrm{End}(\mathbf{1})$."* — note **"pivotal antipode"** and **"$S^2 = \mathrm{id}$"** appear here as *hypothesis* + *conclusion*.
3. **`rem:dagger-notation`** (`quantum-universes/dagger-notation.md:3`) — *"$f^{\dagger}$ denotes the **Frobenius adjoint**: the involution derived from the Frobenius pairing. This is the categorical structure."* and `.md:7`: *"In the categorical setting, only $\dagger$ is defined."*

**Axiom status: DERIVED, with two unpaid debts.**
- **Debt 1 — "pivotal".** `positive-definite-dagger.md:1` assumes a *pivotal* antipode. **Nothing in `def:quantum-universe` or `def:quantum-observable-universe` supplies pivotality**: no `PivotalCategory` instance field anywhere in `QuantumUniverse`/`QuantumObservableUniverse` (`grep "PivotalCategory" CategoricalFoundations.lean` → 0). The in-repo `PivotalCategory` class (`QOU/MathlibExt/PivotalCategory.lean:215`) requires `[RightRigidCategory C]` and is never instantiated for a QU/QOU. `glossary-pivotal-category.md`: *"A pivotal category in which the two traces then **agree** on every object is called **spherical**; pivotal alone does not force that agreement."*
- **Debt 2 — `S² = id` is no longer even *stated* as a consequence on `main`, and on #7420 it becomes an axiom.** `frobenius-hopf-substrate.ts` authorNote 2026-09-14: *"`S^2 = \mathrm{id}$ was consequently **independent** of this definition — neither open nor false."* On #7420 it is `antipode_involutive : antipode ≫ antipode = 𝟙 obj`, and the PR audit says: *"**`S² = id` is carried but pins nothing on its own** — `S = id` satisfies it on every group tested … It is in the package because the classical antipode satisfies it and **because it is the pivotal-structure statement**, not because it constrains."* Bean `qou-k4zx` then measures it: *"**Only `involutive` is proved INDEPENDENT.** Witness on `V_4`: the 3-cycle on the three non-identity elements fixing the identity."*
- **No `DaggerCategory` typeclass anywhere.** `grep -rn "DaggerCategory" QOU/` → **0 hits**. The dagger is `structure InvolutiveStructure` (`Structures.lean:45`, fields `dagger`, `dagger_dagger`, `dagger_comp`, `dagger_id`) + `PositiveDefiniteStructure` (:71, adds `[Preadditive C]`, field `positive_definite`). **`InvolutiveStructure` is never a field of `QuantumUniverse` or `QuantumObservableUniverse`** — so the dagger that `thm:su2-emergence` hypothesis (2) requires (*"preserving … the Frobenius dagger ($g\,g^{\dagger} = 1$)"*) is not carried by the axioms at all.
- The Lean witness `QOU/frobenius_dagger_positive_definite.lean:41` is concrete, not categorical: its own docstring says *"We verify positive-definiteness concretely in `Rep(SU(2))` on the fundamental representation `V = ℂ²`. Schur's lemma pins an endomorphism down to `f = z • id`."*
- `.md`/Lean binder mismatch, opposite directions: `involutive-structure.md:1` says *rigid* + *$R$-linear*; `Structures.lean:45` says only `[Category] [MonoidalCategory]`.

---

## 6. The running SU(2) example, in chapter-manifest order

### 6a. `quantum-universes` (manifest `quantum-universes/quantum-universes.ts`)

| section | block (kind, label) | example |
|---|---|---|
| `sec:qou-intro` | prose ×2 | — |
| `sec:rigid-monoidal` | `definition def:snake-identity` | **none** |
| | `definition def:rigid-monoidal-category` | `ex:rigid-monoidal-vect` — **Vect_ℂ + Rep(SU(2))**, i.e. the SU(2) example's seed |
| | `remark rem:monoidal-justification` | — |
| | `example ex:rigid-monoidal-vect` | — |
| `sec:quantum-universe` | `definition def:quantum-universe` | **`ex:quantum-universe-su2`** ✓ |
| | `remark rem:quantum-universe-axiom-motivation`, `prop/prf:quantum-universe-exists`, prose `sec:tau-notation` | — |
| | `definition def:frobenius-pairing` | **`ex:frobenius-pairing-su2`** ✓ |
| | `prop/prf:frobenius-pairing-exists` | — |
| `sec:quantum-universe-frobenius-pairing-unique` | `prop/prf:frobenius-pairing-unique` | — |
| | **`example ex:frobenius-pairing-su2`** | |
| | `remark rem:frobenius-geometric-role` | — |
| | **`example ex:quantum-universe-su2`** | |
| | `table tbl:quantum-universe-su2-table1-data` | |
| | `definition def:higher-forms` | **`ex:higher-forms-su2`** ✓ |
| | **`example ex:higher-forms-su2`** | |
| | prose `sec:fundamental-object-explication` | — |
| | `definition def:fundamental-object` | **none** |
| | `definition def:tannaka-dual` | **none** |
| | `remark rem:unit-simplicity` | — |
| `sec:qu-consequences` | `proposition prop:frobenius-relation` | `ex:frobenius-su2` (**lives in ch. 2**) |
| | `prf:frobenius-relation`; **`example ex:frobenius-relation-su2`** | **orphan — referenced by nothing** |
| | `definition def:involutive-structure` | `ex:dagger-su2` (**lives in ch. 2**) |
| | `prop/prf:positive-definite-dagger` | — |
| | **`example ex:positive-dagger-su2`** | **orphan — referenced by nothing** |
| | `rem:dagger-notation`, `rem:tannaka-krein-overview`, `rem:axiom-independence` | — |
| `sec:qu-structures` | `definition def:categorical-connection` | `ex:connection-su2` (**lives in ch. 2**) |
| | `prop/prf` ×4; **`example ex:categorical-connection-su2`** | **orphan — referenced by nothing** |
| | `definition def:categorical-jet` | **none** |
| | `definition def:categorical-hodge-star` | **`ex:hodge-su2`** ✓ |
| | `prop/prf` ×4; **`example ex:hodge-su2`** | |
| | `definition def:poisson-object` | **none** |
| | `rem:poisson-hkr-connection`, `outro-quantum-universes` | — |

**Definitions in `quantum-universes` with NO `examples[]` (5):** `def:categorical-jet`, `def:fundamental-object`, `def:poisson-object`, `def:snake-identity`, `def:tannaka-dual`.
**Examples not referenced from ANY `examples[]` corpus-wide (3):** `ex:categorical-connection-su2`, `ex:frobenius-relation-su2`, `ex:positive-dagger-su2`. All three are SU(2) blocks sitting *next to* the definition they illustrate but not linked to it.
**Definitions whose example is NOT SU(2)/O(SU(2))/V=ℂ² (0).** (`ex:rigid-monoidal-vect` counts as SU(2)-bearing: `.md:5` *"The category $\mathrm{Rep}(\mathrm{SU}(2))$ … is $\mathbb{C}$-linear rigid monoidal … The *fundamental object* is $V = V_{1/2} \cong \mathbb{C}^2$."*)

`ex:quantum-universe-su2.md` is the canonical anchor: *"(i) Category. $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}(2))$ … (ii) Frobenius--Hopf object. $A = \mathcal{O}(\mathrm{SU}(2))$ … (iii) Fibre functor. $\tau \colon \mathrm{Rep}(\mathrm{SU}(2)) \to \mathrm{Vect}_{\mathbb{C}}$ … (iv) Differential calculus."* **It does not verify axiom 1 (braiding) at all** — Rep(SU(2)) is symmetric, so at $q=1$ there is nothing to check, which is exactly why the running example never exercises the braided axiom.

### 6b. `quantum-observable-universes` — the SU(2) chain in manifest order

`sec:qou-definition`: `def:quantum-observable-universe` → `ex:qou-su2` (whose entire `.md` is one sentence: *"The realization over $\mathrm{SU}(2)$ satisfies the QOU conditions."*), plus `ex:c-quantum-observable-universe`, `ex:c-quantum-universe`. Then `rem:fibre-functor-rigidity`, `example ex:qou-su2`, `rem:base-field-independence`.

`sec:emergence-volume-rigidity`: `example ex:frobenius-su2` → `example ex:dagger-su2` → `lem:volume-from-rigidity` (examples: `ex:frobenius-su2`, `ex:dagger-su2`, `ex:su2-volume-from-rigidity`, `rem:spin-half-representation`) → `example ex:su2-volume-from-rigidity` → `thm:su2-emergence` (`ex:su2-emergence`) → `lem:su2-emergence-volume-determinant` → `lem:su2-emergence-dagger-unitarity` → `prf:su2-emergence`.
`sec:emergence-spin-labels`: `example ex:su2-emergence` → `prop:spin-labels` (`ex:spin-labels-su2`) → `example ex:spin-labels-su2` → `rem:spin-half-representation`.
`sec:weight-decomposition`: `def:maximal-torus` (`ex:maximal-torus-su2`) → `example ex:maximal-torus-su2` → `def:weight-decomposition` (**no examples[]**) → `thm/prf:weight-decomposition-exists` → **`example ex:weight-decomposition-su2` (orphan)**.
`sec:differential-structures-reeb`: `def:categorical-reeb` (`ex:reeb-su2`, `ex:connection-su2`) → `example ex:reeb-su2` → **`example ex:categorical-reeb-brings` (orphan; Bring's surface, not SU(2))** → `def:projective-line-object` (`ex:projective-line-su2`) → `example ex:projective-line-su2` → `def:contact-affine-chart` (**no examples[]**).
`sec:differential-structures-fiber-adjoint`: `prop:fiber-adjoint-involution` (`ex:fiber-adjoint-su2`) → `example ex:fiber-adjoint-su2` → `example ex:connection-su2`.
`sec:substrate-parameter`: `def:substrate-parameter` (`ex:substrate-parameter-su2`) → `example ex:substrate-parameter-su2` → **`example ex:substrate-parameter-brings` (orphan; Bring)** → `def:quantum-gauge-group`, `def:quantum-planck-constant`, `def:q-hodge-star`, `def:exceptional-divisor`, `def:commutative-qou` (**all five: no examples[]**).
`sec:algebraic-substrate-reeb`: `def:frobenius-hopf-substrate` (**no examples[]**), `def:brings-coordinate-ring`, `def:substrate-parameter-planck`, `def:categorical-reeb-derivation`, `def:rigid-dualizing-complex` (**all: no examples[]**) → **`example ex:rigid-dualizing-brings` (orphan; Bring)**.
`sec:categorical-action`: `def:categorical-action` (`ex:categorical-action-notation-su2`, `rem:physicist-translation`, `ex:photon-wavefront`) → `example ex:categorical-action-notation-su2`.
`sec:particles`: `def:categorical-q-ext-deriv` → **examples are the six `ex:q-*` blocks, none SU(2)-named**: `ex:q-ext-deriv`, `ex:q-lie-bracket`, `ex:q-connection`, `ex:q-reeb-vector-field`, `ex:q-reeb-flow`, `ex:q-torsion-leaf`.

**Definitions in `quantum-observable-universes` with NO `examples[]` (30):** `def:brings-coordinate-ring`, `def:categorical-dirac-operator`, `def:categorical-fourier`, `def:categorical-instanton`, `def:categorical-lagrangian`, `def:categorical-laplace`, `def:categorical-point`, `def:categorical-q-connection`, `def:categorical-q-lie-bracket`, `def:categorical-reeb-derivation`, `def:commutative-qou`, `def:contact-affine-chart`, `def:exceptional-divisor`, `def:fermion-boson-decomposition`, **`def:frobenius-hopf-substrate`**, `def:observation`, `def:q-deformed-commutator`, `def:q-dilogarithm`, `def:q-exponential`, `def:q-harmonic-form`, `def:q-heat-equation`, `def:q-hodge-star`, `def:q-logarithm`, `def:q-resolvent`, `def:quantum-flatness`, `def:quantum-gauge-group`, `def:quantum-planck-constant`, `def:rigid-dualizing-complex`, `def:substrate-parameter-planck`, `def:weight-decomposition`.
**Orphan examples (4):** `ex:categorical-reeb-brings`, `ex:rigid-dualizing-brings`, `ex:substrate-parameter-brings`, `ex:weight-decomposition-su2`.
**Definition whose examples are NOT SU(2) (1):** `def:categorical-q-ext-deriv` (six `ex:q-*` blocks).

### 6c. `lifting-and-descent`

SU(2) examples in manifest order: `ex:jet-prolongation-su2` (→ `prop:jet-prolongation`), `ex:recursive-brane-tower-su2` (→ `def:recursive-brane-tower`), `ex:brane-tower-levels` (→ `prop:jet-prolongation`; **archimedean tuple, not SU(2)**), `ex:descent-lemma-su2` (orphan), `ex:descent-involution-su2` (orphan), `ex:yekutieli-lifting-condition-su2` (→ `def:yekutieli-lifting-condition`), `ex:quantum-characteristic-classes-su2` (→ `def:quantum-characteristic-classes`), `ex:yekutieli-lifting-su2` (→ `prop:yekutieli-lifting`), **`ex:qu-to-qou-su2` (→ `thm:qu-to-qou`)**, `ex:direct-limit-algebra-su2` (orphan), `ex:vacuum-state-su2` (orphan), `ex:descent-eigenspaces-su2` (orphan), `ex:brane-boundary-su2` (orphan).

**Definitions with NO `examples[]` (9):** `def:arc-space`, `def:brane-boundary`, `def:categorical-q-reeb-flow`, `def:ccg-cosimplicial-identities`, `def:descent-involution`, `def:localized-knot`, `def:motivic-galois-character`, `def:motivic-substrate`, `def:yekutieli-triple`.
**Orphan examples (6):** `ex:brane-boundary-su2`, `ex:descent-eigenspaces-su2`, `ex:descent-involution-su2`, `ex:descent-lemma-su2`, `ex:direct-limit-algebra-su2`, `ex:vacuum-state-su2`.
**Definition whose example is not SU(2) (1):** `def:direct-limit-algebra` → `['rem:jet-shell']` (a remark, not an example).

**Totals: 44 definitions across the three chapters carry no `examples[]`; 13 SU(2)/Bring example blocks are unreachable from any `examples[]`.** The running example is *physically present in the manifest next to its definition* far more often than it is *linked*, which is why the chain reads continuous in the PDF but is broken in the dependency graph.

---

## 7. The base manifold

**First statement of what the classical base is.** Not in the three chapters. The earliest concrete answer is in `brings-surface/`:

- `brings-surface/genus-maximal-descent.md:1` — *"If the geometric descent produces a compact one-complex-dimensional base $M_0$, then $M_0$ is a **Riemann surface of genus $g = 4$**."*
- `brings-surface/brings-curve.md:1` — *"Bring's curve is the unique Riemann surface of genus $4$ with the maximal automorphism group $S_5$ (order $120$)."*
- `brings-surface/brings-smoothness.md:1` — *"Bring's surface $\mathcal{S}$ … is a ***smooth* algebraic variety**. The three power-sum constraints intersect transversely in $\mathbb{P}^4$."*
- `brings-surface/brings-surface-def.md:1` — *"**Bring's surface** is the algebraic variety …"* over `R` with `30 ∈ R^×`.
- `brings-surface/brings-realisations.md:1` — *"Over an archimedean field $K$ … Bring's surface is a compact Riemann surface of genus $4$. The unit circle bundle $M_S$ in $T^*\Sigma_4$ is a CR manifold of hypersurface type (real dimension $3$)."*

**"archimedean tuple"** — `brings-surface/approach-to-exceptional-divisor.md:3`: *"In the QOU **archimedean tuple** $(\mathbf{C}, \varTheta, G, \mathcal{S})$, the base manifold $M$ carries the smooth metric in which two free vortices propagate."* Same tuple in `lifting-and-descent/brane-tower-levels.md:1`: *"Starting from an archimedean $\mathbb{C}$-quantum observable universe $(\mathbf{C}, \varTheta, G, \mathcal{S}_1)$ … $\mathcal{S}_{n+1}$ defines the orthonormal frame bundle of $J^1 \mathcal{S}_n$ … The first jet prolongation constructs $\mathcal{S}_2$ over the base manifold $M_1 = \mathcal{S}_1$."* `$\varTheta$` is the contact form: `brings-surface/brings-qou-4tuple.md:12` — *"The Liouville $1$-form $\lambda = \eta\,dz$ on $T^*S$ restricts to a contact form $\varTheta = \lambda\big|_{M_S}$, making $M_S$ a $3$-dimensional strictly pseudoconvex CR manifold."*

**`M_0` / `M₀`** — `lifting-and-descent/euler-char-stability-C.md:9`: *"Because each level of the brane tower alters only the bundle data while preserving the base geometry, **the base manifold $M_0$ remains invariant under jet prolongation.** Therefore, $\chi(M_0)$ persists unaltered at every level."* Also `brings-surface/chirality-trefoil.md:1`, `brings-surface/chi-minus-six-chain.md:5`, `brings-surface/light-cone-affine.md:1`.

**Is there a remark saying "under the axioms the classical analogue of the base behaves like a smooth manifold / algebraic variety"?** The closest, and the only one that frames it as a consequence of the axioms:

- `quantum-observable-universes/substrate-parameter-planck.md:9` — *"The pair $(q, \hbar_q)$ parametrizes the deviation of $A$ from commutativity. **In the classical limit $q \to 1$, $\hbar_q \to 0$ recovers the commutative coordinate ring and the smooth manifold geometry.**"*
- `lifting-and-descent/descent-reduction-zero.md:1` — *"When $\dim M_k = 0$, the base manifold is a discrete set of points…"*; `lifting-and-descent/qu-to-qou-proof.md:13` — *"the base becomes a discrete (Artinian) scheme."*
- `quantum-observable-universes/projective-line-object.md:1` — *"Under the canonical fibre functor, it manifests as the scheme-theoretic projective line $\mathbb{P}^1(R)$."*

**A statement of the form "under the axioms the classical analogue of the base is a smooth manifold / algebraic variety" is NOT FOUND on the surface searched** (`grep "base manifold\|smooth manifold\|algebraic variety\|complex manifold\|Riemann surface\|archimedean tuple\|scheme\|M_0\|M₀\|\\varTheta"` over `quantum-universes/`, `quantum-observable-universes/`, `lifting-and-descent/`, `brings-surface/` `.md` files; there is **no `descartes-universe/` chapter** — `ls content/quantum-observable-universe/ | grep -i descartes` is empty, and the paper manifest routes the Descartes material through `brings-surface/` and `climax-volume-mass/`). The base is introduced *by construction in the archimedean realisation*, never as an axiomatic consequence.

---

## 8. Docs/audits and beans on this exact question

### Audits (one line each)

- `docs/audits/2026-09-15-antipode-anti-automorphism-package.md` — **PR #7420 only.** The owner decision replacing the convolution antipode with the six anti-automorphism axioms; contains the table `ambient: monoidal → **braided**` and the line *"`QOU.QuantumUniverse` already carried a `braidedInst` field … the instance was sitting there unused."*
- `docs/audits/2026-09-15-frobenius-hopf-has-no-nontrivial-linear-model.md` — over a field the convolution-antipode substrate forces `dim A ≤ 1`; the reason the axiom had to change.
- `docs/audits/2026-09-14-antipode-is-free-data-s-squared-is-independent.md` — the prior state: `S` unconstrained, so `S² = id` was independent, not open.
- `docs/audits/2026-09-14-frobenius-bialgebra-collapse.md` — either unit-side bimonoid axiom collapses `A ≅ 𝟙`; why the substrate is a Frobenius monoid with an antipode, not a Hopf monoid.
- `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` — **30 hits** for braided/rigid/pivotal/ribbon/spherical; the inventory of what Mathlib supplies (braided, rigid) vs. what the repo must build (ribbon, pivotal, spherical).
- `docs/audits/2026-09-13-interior-markov-of-braided-tower.md` — 16 hits; the braided tower's Markov trace.
- `docs/audits/2026-08-01-fibre-to-observable-bridge-verdict.md` — 17 hits; the fibre-functor → observable bridge.
- `docs/audits/2026-07-18-tau-functor-construction-reduction.md` — 19 hits; reduction of the τ construction.
- `docs/audits/2026-09-03-fibre-functors-do-not-change-the-category.md` — the fibre functor is not where the structure lives.
- `docs/audits/2026-08-22-inconsistent-axioms-and-unbuilt-lean-siblings.md` — the co-located-sibling divergence pattern that §1a's three `QuantumUniverse` copies instantiate.
- `docs/audits/2026-08-26-live-axiom-surface-recheck.md`, `2026-09-03-axiom-tier-triage.md`, `2026-05-17-derivable-axioms-audit.md` — axiom-surface triage; which axioms are load-bearing.
- `docs/audits/2026-07-11-deltalambda-sign-pivotal-grading-capstone.md`, `2026-08-04-hypercharge-ribbon-twist-battery.md` — where pivotal/ribbon actually pay off downstream (mass channel).
- `docs/audits/2026-08-15-derivation-claim-audit-and-the-q-origin-contradiction.md` — 9 hits; the `q`-origin contradiction directly relevant to §4.

### Beans (one line each; **5302** total, ~190 on-topic by filename)

- `qou-c64q` — *"GAP: def:frobenius-hopf-substrate has NO antipode axiom -- S is free data, so S^2 = id is independent (owner decision)"* — `in-progress`, the driver of #7420.
- `qou-aawz` — *"GAP: is there a NON-TRIVIAL FrobeniusHopfData? the corpus only exhibits A = 1"* — `todo`, **priority high**.
- `qou-k4zx` — **PR #7420 only** — *"GAP: are the six antipode axioms independent, and is the braiding instance over-applied?"*; names the six blanket-patched files and measures 1-of-6 independent.
- `qou-6trs` — *"GAP: QU axiom 3 (symmetric Frobenius) is prose-only — no Lean field"* — `completed` (now `frobenius_symmetric`).
- `qou-aqyf` — *"QU axiom 1: well-foundedness of prec_c stays prose-only (encoding would be vacuous)"* — `todo`. **This is the braiding axiom.**
- `qou-w1g8` — *"QU axiom 4 Lean field omits idempotent orthogonality + completeness (needs Preadditive)"* — `completed`.
- `qou-t7mt` — *"def:frobenius-hopf-substrate presupposes A-dual; its own Lean needs only MonoidalCategory"* — `completed`; the rigid→monoidal correction that #7420 now reverses toward braided.
- `qou-hmhw` — *"Three structures named FrobeniusHopfSubstrate with different field sets -- the markovZ overload defect again"* — `completed`; the same defect now applies to `QuantumUniverse` (§1a).
- `qou-n1dj` — *"GAP: does the MASS fibre functor land in Rep(SU_q(2))~TL or full H_3(q)?"* — `todo`; source of the iso-vs-epi volume reading.
- `qou-v1h5` — *"fix thm:su2-emergence: structure assumes its rank"* — the repair behind `su2_emergence_rank_forced`.
- `qou-fav8` — *"QOU existence: the sorry is closeable DISHONESTLY, which is the real finding"* — `todo`; why `adjointObj` gained three pinning fields.
- `qou-ywh9` — *"Degree-N volume form: does anything in axioms 1-4 supply degree 3?"* — `completed`.
- `rtrb` — *"RT-1: RibbonCategory layer (twist θ) on Mathlib BraidedCategory+RightRigidCategory"* — `in-progress`, **priority high**; source of `BalancedCategory`, i.e. of `QuantumUniverse.balancedInst`.
- `bwrt` — *"bwse-RT: ground input (RT) in Mathlib braided/rigid categorical dimension (toward ribbon-MTC)"* — `in-progress`.
- `rtqd` — *"GAP: qDimObj(Xᘁ)=qDimObj X general-object conjugation symmetry needs a pivotal structure Mathlib lacks"* — `in-progress`.
- `qou-3thc` — *"SphericalCategory: the braiding-free spherical class, and sphericalOfRibbon"* — `completed`.
- `qou-djk4` — *"Twisted quantum dimension: ribbon => spherical, and the qDimObj borrowed name"* — `completed`; records that `qDimObj` is the *twistless* braided closure.
- `qou-knsx` — *"Front 1: naturality of drinfeldIso in a braided right-rigid category"* — `completed`.
- `qou-we9a` — *"GAP: pivotal transport identity qDimObj(Xᘁ) = leftQDim…"*; `qou-chkh` — *"front 2c: PivotalCategory FGModuleCat k instance"*; `qou-i7rq` — *"tranche: close the PivotalCategory instance (Drinfeld…)"*; `qou-ezas` — *"Step 3: state monoidality as a PivotalCategory field"*; `qou-ga7i` — *"tranche: monoidality of the pivotor and the tensor…"* — the pivotal front, all open-ish.
- `qou-i52l` / `qou-lyq2` — *"prop-rigid-monoidal-structural-gap-invariance"* — `todo` + 1 `sorry`.
- `vq17` — *"Vacuity fix: lean/FrobeniusHopfData (1 defect)"* — `completed`; category `self-assuming-projection`.
- `qou-178o` — *"Ch9.1 intro overclaims forced by the braiding rather…"*; `qou-mbar` — *"GAP: inv R_q braiding eigenvalue q-ext-deriv written…"*; `qou-pbjv` — *"infra: Hecke algebra H_n(q) as braided monoidal categ…"*; `qou-wqst` — *"Step 4: prove drinfeldIso is monoidal/braided instance"*.
- **Axiom-independence beans:** `qou-aqyf`, `qou-6trs`, `qou-ywh9`, `qou-k4zx` (the measurement), plus `bday`, `qou-8s7o`, `qou-0r4e`, `qou-ch3j` (*"diamond lemma: reduce the 5 framework axioms confluent…"*), `qou-58rx`, `qou-i6cn`.

---

## 9. Synthesis: the current state, and how to clean it up

### What is actually tangled (six findings, each with a file:line)

1. **The declared split is right and documented; the *ambient* prose and one chapter docstring contradict it.** `quantum-universe.md:24` + `quantum-observable-universe.md:22` + `rigid-monoidal-intro.md:3` + `quantum-universe-axiom-motivation.md:25` all say *braided at QU, braided+rigid at QOU*. Against that: `quantum-universes/quantum-universes.ts:6` says *"rigid **symmetric** monoidal"*, and ~11 `.md` blocks in later chapters say "rigid braided monoidal" of C generically (including `climax-volume-mass/vertex-algebra-relations.md:17` labelling it **"QU-1"**).
2. **The Lean axiom structures carry more structure than the `.md`, and less than the theorems need.** More: `Preadditive`, `Linear R`, `BalancedCategory` (a twist/ribbon-minus-duals) on `QuantumUniverse`, none of which `def:quantum-universe.md` mentions. Less: no pivotal (needed by `prop:positive-definite-dagger`), no dagger field (needed by `thm:su2-emergence` hypothesis 2), no Chern-class field (condition 4 of `def:quantum-observable-universe`).
3. **`braidedInst`, `rigidInst`, `balancedInst` have ZERO field reads on `main`.** They are inert. #7420 makes `braidedInst` live for the first time, via `frobHopf`.
4. **`thm:qu-to-qou` promotes QU → QOU without supplying rigidity or the Chern condition** (`lifting-and-descent/qu-to-qou.md:1–5`). With the current definitions that statement is unsound as written.
5. **Three divergent copies of `QuantumUniverse`** (canonical + two co-located siblings), one of which has an extra `fibreFunctor_faithful` field. Same defect class as bean `qou-hmhw`.
6. **The running SU(2) example is present but not wired.** 44 definitions in the three chapters have no `examples[]`, including `def:frobenius-hopf-substrate`, `def:tannaka-dual`, `def:fundamental-object`, `def:weight-decomposition`, `def:quantum-gauge-group`; 13 SU(2)/Bring example blocks are unreachable from any `examples[]`; and `ex:quantum-universe-su2` verifies items (i)–(iv) but **never checks axiom 1 (braiding)** — because Rep(SU(2)) is symmetric, so at $q=1$ there is nothing to check. The running example therefore never exercises the axiom the owner is asking about.

### The cleanest answer to the owner's actual question

> *"what we need i guess is that QOU axioms still let us sl_2^q then its category of representations is a braided rigid monoidal category"*

That **is** satisfied — but by *fiat*, not by derivation, and the directionality is the reverse of the framing. `quantum-observable-universe-exists-proof.md:9` takes `C := Rep(U_q(g))` and *cites* Chari–Pressley/Kassel for its rigid-ribbon-braided structure; `tannaka-krein-reconstruction.md:1` then goes the other way — *"For generic braiding, $H$ reconstructs the compact quantum group algebra $\mathcal{O}_q(G)$. The deformation parameter $q$ is determined by the braiding."* So: **the braiding is an axiom on C, and `SU_q(2)` is its output.** Nothing derives the braiding from the Frobenius–Hopf data or from an R-matrix.

### Six concrete cleanups, in dependency order

1. **Fix the two stale statements (5 minutes, zero math).** `quantum-universes/quantum-universes.ts:6` "rigid symmetric monoidal" → "braided monoidal (rigidity is imposed in Ch. 2)". `climax-volume-mass/vertex-algebra-relations.md:17` "QU-1: Rigid braided monoidal structure" → "QOU-1". Then sweep the ~11 generic "rigid braided monoidal $\mathbf{C}$" sites for whether they mean QU or QOU.
2. **Decide the ribbon/twist question and put it in ONE place.** `QuantumUniverse.balancedInst` (`CategoricalFoundations.lean:238`) is a ribbon-flavoured axiom with a long docstring justification, no `.md` counterpart, and no consumer. Either (a) promote it into `def:quantum-universe.md` as axiom 1′ ("the braiding is balanced; the twist is what makes `q` derivable") — the docstring already writes the argument — or (b) drop it and make `rem:sqrt-q-ribbon-structure` the only place ribbon is assumed, as a *hypothesis of the blocks that need it*, matching `outro-quantum-universes.md:1`'s stated discipline for rigidity. Same decision for `Preadditive`/`Linear R`: the `.md` says only "$R$-linear".
3. **Settle `def:rigid-monoidal-category`'s overload.** One block currently defines monoidal, rigid, $R$-linear, braided, symmetric and $\Lambda^k$. Split it — `def:monoidal-category` / `def:rigid-monoidal-category` / `def:braided-monoidal-category` — so `def:quantum-universe` `uses:` the *braided* one and `def:quantum-observable-universe` `uses:` the *rigid* one. Today both `uses: ["def:rigid-monoidal-category"]`, which is why the split reads as an afterthought. Note there is currently **no `def:braided-*` label anywhere in `content/`**.
4. **Close the QOU-side gaps that the .md promises and the Lean does not carry:** the Chern-class condition 4 (no field), pivotality (needed by `prop:positive-definite-dagger`'s "pivotal antipode $S$"), and an `InvolutiveStructure` field (needed by `thm:su2-emergence` hypothesis 2's `g g† = 1`). Cheapest first: make the dagger a field of `QuantumObservableUniverse` rather than a free-floating structure, since the emergence theorem consumes it.
5. **Repair `thm:qu-to-qou`** (`lifting-and-descent/qu-to-qou.md`): add rigidity (and the Chern condition) to its hypotheses, or restate the conclusion as "satisfies conditions 2, 3, 5 of `def:quantum-observable-universe`".
6. **Wire the running example.** Add `examples[]` links for the 13 orphan blocks (3 in ch. 1, 4 in ch. 2, 6 in ch. 3) and for the highest-value unexampled definitions (`def:frobenius-hopf-substrate`, `def:tannaka-dual`, `def:fundamental-object`, `def:weight-decomposition`). Then — the substantive one — **extend `ex:quantum-universe-su2` with an item (v) for axiom 1**, worked at $q \neq 1$ in `Rep(SU_q(2))` rather than at $q = 1$ in `Rep(SU(2))`, since the symmetric case makes the braided axiom invisible in the example that is supposed to motivate it.

### On PR #7420 specifically

The braiding demand is **corpus-derived and cheap** — `frobenius-hopf-substrate.md:21` already placed the substrate at QU level, which is braided, and `braidedInst` was already there. Two things to hold it to:
- The **six blanket-patched files** (`Instanton` +17, `ChannelSeparation` +2, `LightningPath` +2, `QDifferentialGeometry` +3, `Torsion/Descent` +2, `CategoricalDqSquared` +1) got `[BraidedCategory C]` on **every** `MonoidalCategory` binder, including declarations that never touch `FrobeniusHopfData`. Bean `qou-k4zx` prescribes the remedy: *"for each added instance, remove it and recompile the module; keep the removal where the module is still clean."* Note `GaugeTheory.lean` (+11) is not on the six-file list but has the second-highest count.
- The co-located sibling `quantum-observable-universes/frobenius-hopf-substrate.lean` is **truncated** on the PR branch (diff ends mid-docstring at `S is invol`, `\ No newline at end of file`). That must be fixed before merge.
- Independence is now measured, not assumed: **only `antipode_involutive` is proved independent** (witness: the 3-cycle on `V_4`), and `anti_mul ⟸ {anti_comul}` on both `V_4` and `S_3` — i.e. the package may carry a redundant axiom *in its most load-bearing position*. Bean `qou-k4zx` flags this as the live formalize-first question.
