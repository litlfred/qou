# Audit — `Subsingleton` uniqueness axioms & existence-by-axiom (2026-06-09)

> **Lens.** This audit looks at the Lean development through the
> **axiom** footprint, not the **sorry** footprint. The two are not the
> same — see §6 ("sorry-free ≠ axiom-free"). Triggered by the request
> *"check lean for `Subsingleton` axioms… also check for
> not-necessarily-unique situations, or cases in which existence is
> asserted but not proved."*

## 0. Headline

| Stat | Value |
|---|---|
| Custom `axiom` declarations in `content/quantum-observable-universe/**/*.lean` | **272** across **145** files |
| Free-standing `axiom … : Subsingleton X` uniqueness axioms | **15** |
| …of those, **self-documented as too-strong / false** | **≥ 7** |
| Paired `*-exists.lean` / `*-unique.lean` blocks (both axiomatized) | **31** / **27** |
| Downstream **Lean** consumers of the 15 Subsingleton axioms | **0** (contained) |
| Precedent files already **downgraded** off the bad pattern | **5** |

The number to internalise is **272 custom axioms**. A clean Lean
development has an axiom audit that returns only `Classical.choice`,
`propext`, `Quot.sound`. Here, `#print axioms` on a typical "canonical X"
result returns a bespoke axiom that often asserts a **provably false**
proposition. That is the audit flag.

> **✅ Resolved 2026-06-09 (see [§7a](#7a-resolution-applied-2026-06-09)).**
> All 15 Class-A `Subsingleton` axioms are remediated: **13 downgraded
> to genuinely type-checked proofs (zero axioms)**, 2 retained as honest
> §3b-cond conditional axioms. The 15 `*-unique.lean` files were
> `validation:"not_checked"` display snippets that never imported their
> structures (the names auto-bound as type variables), so the false
> axioms never entered a checked build — **no live inconsistency**; the
> §3 `False` derivation is now moot. 10 content-only structures were
> relocated into the `QOU` library so the proofs type-check there.

## 1. Two patterns — one sound, one not

The repo legitimately uses the **§3b-cond conditional-class** pattern
(AGENTS.md §3b-cond; tracked in
[`docs/uniqueness-theorems-backlog.md`](../uniqueness-theorems-backlog.md)
and [`docs/audits/2026-06-03-lean-3b-cond-class-sorries-catalog.md`](2026-06-03-lean-3b-cond-class-sorries-catalog.md)).
It is important to separate it from the pattern this audit flags.

**Pattern A — SOUND (conditional class).** A conjecture `C` becomes a
`class C` whose body carries one `sorry`; downstream results take
`[C]` as an *explicit hypothesis* and are proved sorry-free
*conditional on the instance*. The claim is an **implication**
`[C] → result`. If `C` is false the implication is still sound
(vacuously). 194 such classes exist and are **permanent by design** —
NOT bugs. Example done right: `MarkovTraceUniqueness` (backlog item 1).

**Pattern B — UNSOUND (free-standing global axiom).** A bare
`axiom Foo.unique_axiom : Subsingleton Foo` asserts `Subsingleton Foo`
**unconditionally, globally**, with no hypothesis gate. If `Foo` has
≥ 2 distinct inhabitants, the axiom asserts a **false** proposition and
the environment becomes inconsistent (see §3). The wrapper
`theorem Foo.unique : Subsingleton Foo := Foo.unique_axiom` then *looks*
proved but rests entirely on the false axiom.

The 15 `Subsingleton` uniqueness axioms below are Pattern B.

## 2. Class A — `Subsingleton` uniqueness axioms ("not necessarily unique")

All 15 are `axiom … _axiom : Subsingleton X` re-exported by a sibling
`theorem X.unique := …_axiom`. "Self-assessment" quotes the file's own
docstring.

| # | Axiom | File:line | Asserts | File's own self-assessment |
|---|---|---|---|---|
| 1 | `Hadron.unique_up_to_isotopy_axiom` | `particle-interactions/hadron-unique.lean:55` | `Subsingleton Hadron` | **"strictly false … the `Hadron` structure has free fields"** |
| 2 | `FrobeniusHopfData.frobeniusForm_unique_axiom` | `quantum-universes/frobenius-pairing-unique.lean:58` | `Subsingleton (FrobeniusHopfData C)` | unique only *up to scalar*; "for `Subsingleton` we'd need scalar = 1" |
| 3 | `CategoricalConnection.unique_up_to_gauge_axiom` | `quantum-universes/categorical-connection-unique.lean:33` | `Subsingleton (CategoricalConnection C fh)` | connections form a **torsor** over `Ω¹(A)⊗Ad(A)` (false unless trivial) |
| 4 | `QResolvent.unique_axiom` | `quantum-observable-universes/q-resolvent-unique.lean:27` | `∀ H, Subsingleton (QResolvent H)` | **"too strong for the current structure (free fields)"** |
| 5 | `QDilogarithm.unique_axiom` | `quantum-observable-universes/q-dilogarithm-unique.lean:29` | `∀ H, Subsingleton (QDilogarithm H)` | **"bare `Subsingleton` is too strong"** |
| 6 | `CategoricalLaplace.unique_axiom` | `quantum-observable-universes/categorical-laplace-transform-unique.lean:24` | `∀ A, Subsingleton (CategoricalLaplace A)` | **"bare `Subsingleton` is too strong"** |
| 7 | `QHeatEquation.unique_solution_axiom` | `quantum-observable-universes/q-heat-equation-unique.lean:27` | `∀ S, Subsingleton (QHeatEquation S)` | **"bare `Subsingleton` is too strong"** |
| 8 | `CategoricalHodgeStar.unique_axiom` | `quantum-universes/categorical-hodge-star-unique.lean:32` | `Subsingleton (CatHodgeInvolution X)` | "auto-extracted from the single-sorry theorem body" |
| 9 | `CategoricalInstanton.unique_up_to_gauge_axiom` | `quantum-observable-universes/categorical-instanton-unique.lean:34` | `Subsingleton (CategoricalInstanton C fh)` | "auto-extracted …" |
| 10 | `CategoricalDirac.unique_axiom` | `quantum-observable-universes/categorical-dirac-operator-unique.lean:32` | `Subsingleton (CategoricalDiracOperator C fh)` | "auto-extracted …" |
| 11 | `CategoricalLagrangian.unique_axiom` | `quantum-observable-universes/categorical-lagrangian-unique.lean:31` | `Subsingleton (CategoricalLagrangian C fh)` | "auto-extracted …" |
| 12 | `CategoricalFourier.unique_axiom` | `quantum-observable-universes/categorical-fourier-transform-unique.lean:31` | `Subsingleton (CategoricalFourier A Irreps)` | "auto-extracted …" |
| 13 | `CategoricalQConnection.unique_axiom` | `quantum-observable-universes/categorical-q-connection-unique.lean:33` | `Subsingleton (CategoricalQConnection C)` | "auto-extracted …" |
| 14 | `CategoricalQExtDeriv.unique_axiom` | `quantum-observable-universes/categorical-q-ext-deriv-unique.lean:33` | `Subsingleton (CategoricalQExtDeriv C)` | "auto-extracted …" |
| 15 | `QuantumCharClasses.unique_axiom` | `lifting-and-descent/quantum-characteristic-classes-unique.lean:32` | `Subsingleton QuantumCharacteristicClass` | "auto-extracted …" |

- **Rows 1–7** are self-admitted too-strong/false.
- **Rows 8–15** are axiomatized (so: not proved), soundness **unverified** —
  each needs the same structural check as §3. The "auto-extracted from
  the single-sorry theorem body" docstring means they were *never*
  proved subsingleton; if they were genuinely subsingleton they would
  have been proved, not axiomatized.

**Contrast — the conditional form done right** (Pattern A, keep as
template): `QDilogarithm.unique_up_to_shift_axiom`
(`q-dilogarithm.lean:66`) takes two dilogs `L₁ L₂` *plus equality
hypotheses* and concludes `L₁ = L₂`. That is a conditional uniqueness,
not a global `Subsingleton`, and is sound.

## 3. Why a false `Subsingleton` axiom is worse than a `sorry`

A `sorry` is an *admitted gap*: it makes the one theorem unproved but
injects nothing into the global logic. A **false `axiom`** injects a
false proposition that **any** development importing it can use to prove
`False`. Worked example for row 1:

```lean
-- Hadron has free fields (particle-interactions/hadron.lean:35):
--   theta phi : R_q := LaurentPolynomial ℤ   (ℤ[q,q⁻¹], nontrivial)
--   constituents : List BraidWord  (length ≥ 2)
-- so two hadrons differing only in `theta` are distinct:
example : False := by
  have h0 : Hadron := ⟨0,        0, [[], []], by simp⟩
  have h1 : Hadron := ⟨q_param,  0, [[], []], by simp⟩   -- q_param = T 1 ≠ 0
  have : h0 = h1 := Subsingleton.elim h0 h1               -- from the AXIOM
  have : (0 : R_q) = q_param := congrArg Hadron.theta this
  exact absurd this (by simp [q_param, LaurentPolynomial.T])  -- 0 ≠ T 1
```

The construction is exactly the one the file's own docstring describes
as making the claim "strictly false." The inconsistency is **latent**
(no one has written the `False` derivation into the build), but
soundness is about what is *provable*, and `False` *is* provable from
this axiom plus the nontriviality of `R_q`. The same argument applies
verbatim to `QResolvent` (distinct `s`), `QDilogarithm`,
`QHeatEquation`, `CategoricalLaplace` (free fields), and to rows 8–15
for any of those structures that is genuinely multiply-inhabited.

**Containment.** A grep for downstream Lean consumers of all 15
wrapper theorems returns **only their own definitions** — nothing else
in the Lean tree applies `Hadron.unique_up_to_isotopy` &co. So the
false axioms do not currently poison other *Lean* proofs. They do,
however, (a) sit in the global environment ready to be used, and (b)
back content-block propositions whose `.md`/`.ts` may be cited in
`uses[]` cones (a §3b conjectural-propagation concern to verify
separately).

## 4. Class B — existence asserted but not proved

These axioms assert that an object exists (`∃` / `Nonempty` / `∃!`)
without constructing it. Severity varies.

### 4a. Physics headline claims, axiomatized (highest concern)

[`mass-theory/terminal-resolution.lean`](../../content/quantum-observable-universe/mass-theory/terminal-resolution.lean)
asserts the framework's *central empirical results* as bare axioms,
then wraps each in a trivially-true `∃` "theorem":

| Axiom | Line | Asserts |
|---|---|---|
| `qou_proton_bound` | 79 | `|qou_proton_MeV − codata_proton_MeV| ≤ 0.001` |
| `qou_neutron_bound` | 90 | `|qou_neutron_MeV − codata_neutron_MeV| ≤ 0.001` |
| `qou_deuteron_bound` | 101 | `|qou_deuteron_MeV − codata_deuteron_MeV| ≤ 0.001` |
| `qou_binding_bound` | 112 | `|qou_binding_MeV − codata_binding_MeV| ≤ 0.001` |

**Sharper finding (2026-06-09).** Inspecting the actual terms, the
"predictions" are the **CODATA literals copied**:

```lean
noncomputable def codata_proton_MeV : ℝ := 938.272
noncomputable def qou_proton_MeV    : ℝ := 938.272   -- identical literal
```

(same for neutron `939.565`, deuteron `1875.613`, binding `2.2245`). So
each `axiom qou_*_bound : |qou_*_MeV − codata_*_MeV| ≤ 0.001` is
`|x − x| ≤ 0.001` — a **tautology** that `norm_num` proves instantly; the
`axiom` keyword imports nothing. The agreement is *circular*: the
prediction **is** the measurement.

This answers the calibration test directly: the values do **not** reduce
to the three sanctioned calibrations (CAL-1 `m_e`, CAL-2 `Q_β/τ_n`,
CAL-3 `m_π`). The absolute proton mass from `q₀` is the framework's
**open mass-gap** (AGENTS.md "2.89% m_p gap"), so a genuine derivation
does not exist yet — and proton mass is not itself a legal calibration
input (that would be CAL-4). The file's docstring claim *"derived from
the topological mass formula at q ≈ 1.1097, externally verified"* is
**contradicted by the code**, which never evaluates the formula —
`qou_proton_MeV` is a constant. (The header comment even lists "Binding:
2.224 (QOU) vs 2.2245 (CODATA)" while the code sets both to `2.2245`.)

**Honest fix (applied in this PR):** the 4 `axiom *_bound` become
`theorem *_bound := by … norm_num` (they are provable), with a loud
in-file note that `qou_*_MeV` are **CODATA-pinned placeholders**, the
agreement is therefore **tautological, not a derivation**, and the
`q₀`-derivation is the open mass-gap. This removes 4 spurious axioms
from the count and stops the file presenting circularity as a proved
prediction. It does **not** fabricate a derivation.

### 4b. Numeric values by axiom

- `gram_kappa_numerical_value_axiom` — `mass-theory/gram-determinant-plancherel-ratio.lean:74` — `∃ κ, |κ − 1.722| < 0.001`.
- `h2_binding_energy` — `molecular-construction/ilp-covalent-bond.lean:31` — `∃ E, E > 0 ∧ E < 5.0`.

### 4c. Existence of categorical apparatus by axiom (paired with §2)

`Nonempty`/`∃` axioms that make a construction exist by fiat — and are
the existence half of the `*-exists.lean` / `*-unique.lean` pairs, so
the construction is *both* "exists" and "unique" purely axiomatically:

- `QuantumObservableUniverse.exists_instance_axiom` — `…/quantum-observable-universe-exists.lean:35` — `Nonempty (QuantumObservableUniverse k)`
- `QuantumUniverse.exists_instance_axiom` — `quantum-universes/quantum-universe-exists.lean:33`
- `QDilogarithm.exists_axiom`, `CategoricalLaplace.exists_axiom`, `CategoricalQExtDeriv.exists_axiom` (the partners of §2 rows 5, 6, 14)
- `QCasimir.exists_axiom` — `braids-and-knots/q-casimir-exists.lean:30`
- `categorical_reeb_exists` — `…/categorical-reeb-exists.lean:84`
- `tannaka_krein_isomorphism_axiom` — `q-geometric-langlands/tannaka-krein-isomorphism.lean:43` — `Nonempty (RepLoc ≃ ComodH)`
- `categorical_coordinate_ring_universal_axiom` — `…/categorical-coordinate-ring.lean:120` — `∃! φ, …` (universal property by axiom)
- `adjoint_exists_unique'` — `…/q-codifferential-formula-prop.lean:90` — `∃! L_star, …`

> **Update 2026-08-16 — two Class-B rows are no longer accurate.** Appended
> rather than edited: the findings above are a dated snapshot and stay as
> recorded.
>
> - **`QuantumUniverse.exists_instance_axiom` — DELETED.** It is now a theorem,
>   proved from a concrete witness (`ModuleCat R` with `A = 𝟙`) in
>   [`QOU/QuantumObservableUniverse/TrivialWitness.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/TrivialWitness.lean).
>   `#print axioms` reports only `propext`, `Classical.choice`, `Quot.sound`.
>   The audit's concern was exactly right: the axiom's own docstring claimed a
>   witness "requires category/monoidal-category instances not yet provided",
>   and that was false — the instances were provided.
> - **`QuantumObservableUniverse.exists_instance_axiom` — already gone when
>   this row was written, or shortly after.** The file has carried a
>   `theorem … := by sorry` with a `[kassel1995]` citation, not an `axiom`.
>   A cited `sorry` is a weaker claim than an axiom (it is honestly marked as
>   unproved rather than assumed), so this row overstated the current state.
>   Its hypotheses were rewritten 2026-08-16 from `[Field k]` to `[CommRing R]`
>   plus explicit unit and genericity conditions; the `sorry` is unchanged.
>
> Both tracked under bean `qou-fav8`.

### 4d. Class C — defensible / standard external (lower concern)

Citing an established external theorem as an axiom with `-- Ref:` is the
sanctioned pattern when re-proving in Lean is out of scope. These are
fine to keep, but should be on a tracked allowlist:

- Gröbner–Shirshov: `normal_form_exists`, `confluence`, `local_confluence`,
  `division_terminates_unique` (Diamond Lemma — Bergman).
- `hecke_basis_size_axiom` (Kazhdan–Lusztig 1979).
- `habiro_step_zero_axiom` (integer-poly factor theorem — actually
  *provable* in Mathlib; mild, could be discharged).
- `wedderburn_bratteli_recursion_holds` — **already a `theorem`** (proved
  `∃`), good.

## 5. Precedent — the fix already exists in-repo

Five files were already migrated off Pattern B; use them as templates:

- [`braids-and-knots/q-casimir-unique.lean`](../../content/quantum-observable-universe/braids-and-knots/q-casimir-unique.lean)
  — **downgraded** `Subsingleton (QCasimirData qs)` → *unique up to a
  ground-ring scalar* (the correct proposition).
- [`quantum-observable-universes/categorical-action-unique.lean`](../../content/quantum-observable-universe/quantum-observable-universes/categorical-action-unique.lean)
  — "claim previously axiomatised here" removed.
- `predicted-spectra/categorical-proton-unique.lean`,
  `predicted-spectra/categorical-neutron-unique.lean` — both note the
  old `Subsingleton` axiom "was *false* for the free real" structure and
  were corrected.

So the desired end-state is established repo practice; the 15 in §2 are
the un-migrated remainder.

## 6. The honesty regression: "sorry-free" ≠ "axiom-free"

Rows 8–15 share the docstring *"Auto-extracted from the single-sorry
theorem body in this file."* A mechanical pass rewrote

```lean
theorem Foo.unique : Subsingleton Foo := by sorry        -- honest gap
```

into

```lean
axiom Foo.unique_axiom : Subsingleton Foo                -- global axiom
theorem Foo.unique : Subsingleton Foo := Foo.unique_axiom -- now "sorry-free"
```

Net effect: the theorem **passes a `sorry` audit** (and `lean_verify`'s
sorry scan) while silently depending on a custom — sometimes false —
axiom. A sorry-count dashboard shows these files green; only an **axiom
audit** (this one) surfaces them. This is precisely why the
"check Lean for `Subsingleton` axioms" lens catches something the sorry
metrics hide, and why **272** is the right denominator, not the
sorry count.

## 7. Remediation options (per item in §2)

For each of the 15, pick one:

1. **Downgrade the statement** to the true proposition — *unique up to
   scalar / gauge / isomorphism* — following the `q-casimir-unique.lean`
   template. Removes the false axiom; states what's actually true.
2. **Convert global axiom → Pattern A conditional class.** Replace
   `axiom : Subsingleton X` with a `class XCanonical X` (normalisation
   field) and re-state uniqueness as `[XCanonical] → Subsingleton {…}`.
   Sound; matches the sanctioned §3b-cond pattern and the backlog.
3. **Tighten the structure** so `Subsingleton` is *true* (add the
   normalisation constraint as a structure field / `Prop` mixin), then
   **prove** it — deleting the axiom.
4. **Demote to `conjecture`/`remark`** if neither uniqueness nor a clean
   conditional is available yet, so nothing claims "proved."

For Class B §4a, the decision is editorial: either label the CODATA
bounds as **calibration inputs** (honest) or derive them.

### 7a. Resolution applied (2026-06-09)

All **15** Class-A items have been remediated, and Class B §4a was
de-axiomatised. Combination of options 1 + 3 (downgrade + tighten),
plus a structural prerequisite the audit had missed:

**Prerequisite — the 15 `*-unique.lean` files are
`validation:"not_checked"` display snippets that never imported their
subject structures.** Each `import`ed only `QOU.Basic`, so the
structure name (`Hadron`, `CatHodgeInvolution`, …) **auto-bound as a
fresh `Sort`-valued type variable**. The "`axiom : Subsingleton X`"
therefore desugared to `∀ {α}, Subsingleton α` — provably false, but
it never entered any *checked* build (these files are not in the
`lake build QOU` closure). So there was **no live environment
inconsistency**; the §3 `False` derivation is the entailment *if the
carrier were the concrete structure* — now moot, since the axioms are
replaced by genuinely type-checked statements.

**What was done:**

- **5 library-backed** (`CatHodgeInvolution`, `CategoricalInstanton`,
  `CategoricalConnection`, `CategoricalQExtDeriv`, `FrobeniusHopfData`):
  the `*-unique.lean` files now `import` the existing
  `QOU.QuantumObservableUniverse.*` library structure.
- **10 content-only structures** (`QResolvent`, `QHeatEquation`,
  `QDilogarithm`, `CategoricalFourier`, `CategoricalLaplace`,
  `CategoricalDiracOperator`, `CategoricalLagrangian`,
  `CategoricalQConnection`, `QuantumCharacteristicClass`, `Hadron`)
  were **relocated** into new authoritative library modules
  (`QOU.QuantumObservableUniverses.{QAnalysis, QIntegralTransforms,
  QDifferentialGeometry}`, `QOU.LiftingDescent.QuantumCharacteristicClassDisplay`,
  `QOU.ParticleInteractions.HadronDisplay`), added to the `QOU.lean`
  root so CI's `lake build QOU` checks them. Two latent never-checked
  errors were fixed in passing (`QDilogarithm` needed `[Add H]`;
  `QuantumCharacteristicClass.zero` had a non-synthesising default,
  dropped as redundant).

**Convergence with the `main` proof-integrity sweep (hybrid).** While
this branch was in flight, a parallel sweep landed on `main`
(`2864d683` dirac, `e0c6bb38` lagrangian, `a830e89b` fourier+laplace)
that remediated 3 of the same files with a *stronger* template:
strengthen the structure itself over an `R`-linear category and **pin
the derived morphism with a `*_formula` law field**, so uniqueness is a
genuine *determination*, not extensionality over free fields. Those
files, however, still referenced content-only structures (auto-bound →
unchecked). The two approaches were merged as a **hybrid**: `main`'s
strengthened statements + this branch's library relocation, so the
determination proofs genuinely type-check. Concretely: dirac and
lagrangian keep `main`'s structures/proofs verbatim, relocated into
`QDifferentialGeometry` and re-imported; `CategoricalQConnection` was
upgraded to the same law-field template (`qinv` + `q_unit` +
`nabla_q_formula`); laplace keeps `main`'s conditional-on-`transform`
statement with this branch's import.

**Outcome — axiom accounting for the 15:**

- **13 now PROVED, zero axioms**:
  - *law-field determinations* (morphism forced by a `*_formula` /
    witness field): dirac, lagrangian, q-connection, laplace
    (conditional on shared `transform`), q-resolvent (via
    `inverse_witness` + surjectivity), q-heat (via `evolves`);
  - *extensionality / degeneracy at the level the structure supports*
    (the structures carry no law field yet — strengthening them is the
    recorded open refactor): hodge-star, instanton, connection
    (Leibniz determination under `Epi fh.mul`), q-ext-deriv, fourier
    (+ `project_const` degeneracy lemma), char-classes, hadron.
- **2 honest §3b-cond conditional axioms** (named, cited, *not*
  `Subsingleton`): `FrobeniusHopfData.frobeniusForm_unique_axiom`
  (up-to-invertible-scalar on a simple object, Schur, [kock2004]) and
  `QDilogarithm.unique_axiom` (pentagon universal property,
  [kassel1995]).

Every `*-unique.lean` was verified by compiling it directly with the
toolchain `lean` binary against the built library oleans (all 15
exit 0, re-run after the rebase onto the proof-integrity sweep).
Declaration names are unchanged, so `.ts` `lean.ref`s did not churn.
Class B §4a is closed by the terminal-resolution commit
(tautological CODATA bounds de-axiomatised).

## 8. Method / reproduction

```bash
# the 15 Subsingleton uniqueness axioms
rg -U --multiline 'axiom\s+[\s\S]{0,400}?Subsingleton' -g '*.lean' content/quantum-observable-universe
# existence-by-axiom
rg -U --multiline 'axiom\s+[\s\S]{0,300}?(Nonempty|Inhabited|Exists|∃)' -g '*.lean' content/quantum-observable-universe
# total custom-axiom denominator
rg -c '^\s*(private\s+)?axiom\s' -g '*.lean' content/quantum-observable-universe | awk -F: '{s+=$2} END{print s}'
# downstream Lean consumers of the 15 wrappers → none
rg '(Hadron|QResolvent|QDilogarithm|CategoricalLaplace|QHeatEquation|FrobeniusHopfData\.frobeniusForm|CategoricalHodgeStar|CategoricalConnection|CategoricalInstanton|CategoricalDirac|CategoricalLagrangian|CategoricalFourier|CategoricalQConnection|CategoricalQExtDeriv|QuantumCharClasses)\.unique' -g '*.lean'
```

## 9. See also

- [`docs/uniqueness-theorems-backlog.md`](../uniqueness-theorems-backlog.md) — owner-tracked canonical-X uniqueness backlog (the 5 *physics-canonical* items; the 15 here are the *categorical-apparatus* remainder, not in that list).
- [`docs/audits/2026-06-03-lean-3b-cond-class-sorries-catalog.md`](2026-06-03-lean-3b-cond-class-sorries-catalog.md) — the 194 *sound* conditional-class sorries (Pattern A; do **not** conflate with §2).
- AGENTS.md §3b-cond — the conditional-class exception that makes Pattern A sound.
