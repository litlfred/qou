# W1 audit — `MarkovTrace` class fields: Wenzl positivity is SURPLUS to the general-`n` instance gap

**Bean:** `qou-xik5` (W1 of epic `qou-utb3`, created by PR #4222).
**Verdict up front:** the general-`n` instance of `QOU.Machinery.MarkovTrace`
requires **cyclicity + `R`-linearity only**. **Wenzl positivity is surplus** —
it is not a class field, no consumer uses it, and it is not even *expressible*
over the generic `[CommRing R]` the class lives on. This mirrors the #4151
lesson exactly (PSD surplus to the B2 lift, `LoopWeightRealSymmReduction.lean`:
"the harder positivity — Wenzl's positive Markov trace, the compact real form —
is a *bonus*, not a requirement").

Scope discipline: this is a **scope-limited** finding about the
`QOU.Machinery.MarkovTrace` class and its consumers — not a claim that Wenzl
positivity is useless corpus-wide (it remains the input to the
unitarity/subfactor/semisimplicity-ascent layer, e.g. `WenzlTowerStep`,
PF/Ocneanu–Wenzl weight selection in `BWVacuumRowIsHecke.lean` — those stand,
untouched).

## 1. The class and its fields

`content/quantum-observable-universe/lean/QOU/Machinery/MarkovTraceOnHecke.lean:62-71`:

```lean
class MarkovTrace (R H : Type*) [CommRing R] [Ring H] [Algebra R H]
    (tr : H → R) : Prop where
  cyclic   : ∀ x y : H, tr (x * y) = tr (y * x)          -- (M2), line 65
  map_add  : ∀ x y : H, tr (x + y) = tr x + tr y         -- (M1a), line 67
  map_smul : ∀ (r : R) (x : H), tr (r • x) = r * tr x    -- (M1b), line 69
  -- (M3) Markov reduction: documented, NOT a field (lines 70-71)
```

Three fields. **No positivity field exists** — and none *could*: the signature
carries `[CommRing R]` with no order or star structure, so `0 ≤ tr (x * x̄)` is
not statable (§7c: ordering is an archimedean construct, post-wall; the wall
enters the consumers only through `ev : R →+* ℝ`).

### Field-by-field consumer table (whole-tree grep, 2026-07-25)

The only file that threads `[MarkovTrace R H tr]` as a hypothesis is
`QOU/Archimedean/TauFunctorReduction.lean`; the only instances are the concrete
`n = 2, 3` carriers. Full sweep:

| Field | Consumer | Evidence (file:line) |
|---|---|---|
| `cyclic` | `observationFrame_cyclic` | `TauFunctorReduction.lean:82` (`rw [‹MarkovTrace R H tr›.cyclic x y]`); re-consumed by `tau_construction_reduces` at `:146` |
| `map_add` | `observationFrame_add` | `TauFunctorReduction.lean:92` (`rw [‹MarkovTrace R H tr›.map_add x y, map_add]`) |
| `map_smul` | **none** at audit time; `observationFrame_smul` added by this PR | `TauFunctorReduction.lean` (new lemma; pre-audit grep for `.map_smul` on this class returned zero hits) |
| *(positivity)* | *(no such field)* | — |

Instance providers (both over **generic** `[CommRing R]`, zero positivity used):

- `n = 2`: `QOU/Machinery/HeckeH2AlgebraInstance.lean:131` (`H2A`)
- `n = 3`: `QOU/Machinery/HeckeH3AlgebraInstance.lean:120-124` (`markovTrace_H3A`,
  discharging the fields from the sorry-free `H3.trM_cyclic` / `trM_add` /
  `trM_smul` of `MarkovTraceOnHecke.lean:169-207`)

Other importers of `MarkovTraceOnHecke`
(`HeckeH3GramNondegeneracy`, `HeckeBraidedCategoryScaffold`,
`HeckeH4StabilizationRung`, `HeckeH3AlgebraLaws`) use the `H3` concrete block
or the `HeckeAlgebra` marker — none threads the `MarkovTrace` class, none
touches positivity.

`observationFrame_stabilizes` (`TauFunctorReduction.lean:156-165`) consumes the
**separate** class `MarkovStabilization.stabilizes`
(`HeckeBraidedCategoryScaffold.lean:96-102`) — the (M3)/tower axis. Also
positivity-free (generic `[Field R]`).

## 2. Does ANY consumer need positivity? — No

- The docstring-pattern prediction from the task is **confirmed and sharpened**:
  the consumers are carried by cyclicity + linearity. (The prediction said
  "cyclicity + the Markov normalization property"; in fact the class does not
  even carry the Markov normalization — (M3) is documented-not-enforced
  (`MarkovTraceOnHecke.lean:70-71`), and the tower/stabilization consumer runs
  through the separate `MarkovStabilization` class. Normalization `tr(1)=1` is
  likewise not a field.)
- Where `[wenzl1988]` is cited near the gap
  (`MarkovTraceOnHecke.lean:25`, `TauFunctorReduction.lean:49`), it is cited for
  *existence of the Markov trace on `H_n(q)`* — but existence + (M1)/(M2) is
  Ocneanu/Jones combinatorics (`[jones1987]` §5), valid over any commutative
  ring with chosen `(z, h)`. Wenzl 1988's *additional* content — the trace is a
  **positive** trace for the appropriate real-`q` regime, giving the
  C*/subfactor tower and unitarity — is exactly the part the class cannot state
  and the consumers do not use.
- The "requires upstream Wenzl" phrase in
  `MarkovTraceOnHecke.lean:96-98` (`ResidueACompositeIdentification` docstring)
  refers to the **Jones–Wenzl projector** infrastructure (`p_3`), a different
  Wenzl object again — not a positivity requirement on the trace, and not part
  of the `MarkovTrace` instance gap.
- Corollary observation (same pattern, out of W1 scope, no change made): the
  sibling ℝ-level tower class `MarkovTraceTower`
  (`QOU/Braiding/HnMarkovTrace.lean:48-49`) carries a `z_pos : 0 < z` field
  labeled "Wenzl regime"; its only external consumer
  (`TrMHopfSigma1SqClosedForm.lean:97`) uses `trM_sigma1_sq_stabilises` only —
  `z_pos` is consumer-free there too. A future cleanup may demote it.

**Verdict (scope (a), per §Before declaring "refuted"):** for the
`QOU.Machinery.MarkovTrace` general-`n` instance, Wenzl positivity is
**surplus** — the gap statement "requires upstream Wenzl [positivity]" is
over-scoped and is corrected in the `MarkovTraceOnHecke.lean` §"Extending past
H₃" docstring in this PR.

## 3. Minimal construction that discharges the needed fields at general `n`

The class is per-`(R, H, tr)` — the consumers are satisfied level-by-level as
each `(H_n, tr_n)` instance lands; no single "inductive-limit object" is
demanded by the signature. Three candidate routes:

| Route | What it needs | Positivity? | Assessment |
|---|---|---|---|
| **(a) Ocneanu conditional-expectation tower** `E_n : H_{n+1} → H_n`, `tr_{n+1} = tr_n ∘ E_n` (epic W2–W3) | `E_n` linear + the basic-construction absorption + the spanning decomposition `H_{n+1} = H_n + H_n σ_n H_n` (Ocneanu induction for cyclicity) | **No.** The OPEN classes already staged for this (`HeckeConditionalExpectation` `HeckeTowerBasicConstruction.lean:169`, `JonesBasicConstruction` `:187`) are positivity-free (`[Field R]`). Only `WenzlTowerStep` (`:209`, the semisimplicity ascent along a *nondegenerate* trace) is Wenzl-flavoured — and it is **not needed** for the three fields (nondegeneracy/semisimplicity is a different deliverable). | The right abstract general-`n` route. **Re-scope: W2 must NOT thread `WenzlTowerStep`.** |
| **(b) Direct NF-basis definition per level** (`tr` on the GB normal-form basis, cyclicity = finite Gram symmetry) | Per-level NF tables from the verified generator (`hecke_regular_nf_table.py` / `gb_nf_reducer.rs`) | **No** (generic `[CommRing R]` throughout) | Proven pattern: `n=2,3` **done** (instances live); `n=4` is one finite step from done — `MarkovTraceH4.lean` has M1+M3 sorry-free and cyclicity sorry-free-**reduced** to `gram_symm` (`:233-235`, cited sorry, 24² finite, marked CLOSEABLE via `computations/markov/gen_gram_closure.py` → `MarkovTraceH4Gram`). Cheapest next concrete instance; does not by itself give *generic* `n`. |
| **(c) Seminormal / Hoefsmit weight route** | Young-orthogonal reps, `Real.sqrt` weights | Implicitly drags in the archimedean/real-`q` regime (e.g. `hoefsmitB` is `ℝ`-specialised) — the route where positivity assumptions creep in | Heavy AND wrong side of the §7c wall for a `[CommRing R]` class. Not minimal; avoid for this purpose. |

**Recommended minimal construction:** **(b) to close `n = 4` now** (generate
`MarkovTraceH4Gram`, discharge `gram_symm`, wrap `H4A` as Ring/Algebra mirroring
`H3A`, register the instance) **and (a) for the generic-`n` statement**, in
class-conditional §3b-cond form with the hypothesis set trimmed to
`HeckeConditionalExpectation` + `JonesBasicConstruction` — explicitly
*excluding* `WenzlTowerStep`/nondegeneracy/positivity.

## 4. Re-scoped W2–W4 plan (bean notes updated, none closed)

- **W2 (`qou-2017`)** — build `E_n` and the absorption identity; deliverable
  trimmed: no Wenzl-positivity or nondegeneracy ingredient; do **not** thread
  `WenzlTowerStep`. The Ocneanu-cyclicity induction needs the spanning
  decomposition lemma, not positivity.
- **W3 (`qou-r765`)** — title says "cyclic + Markov normalization"; corrected
  target: prove the **three class fields** (`cyclic`, `map_add`, `map_smul`)
  for `tr = tr_1 ∘ E_1 ∘ ⋯ ∘ E_{n-1}`. Markov normalization/(M3) is NOT a class
  field — its consumer is the separate `MarkovStabilization` class
  (`observationFrame_stabilizes`), which W3 may feed but need not block on.
- **W4 (`qou-o2dk`)** — "register the general-n instance": note instances
  already exist at `n = 2, 3` (`H2A`/`H3A`), so the consumers are *already*
  non-vacuously served at those levels; W4's real content is `n ≥ 4`
  (concretely: the `H4A` wrapper + `gram_symm` closure, then the generic-`n`
  conditional registration from W2-W3). No positivity anywhere in the
  acceptance criteria.

## 5. Lean brick landed with this audit (sorry-free, lean-direct exit 0)

`TauFunctorReduction.observationFrame_smul` — homogeneity of the observable
`τ_∞(r • x) = ev(r)·τ_∞(x)`, the third leg of F3 linearity. With it, the three
class fields are each consumed by exactly one `observationFrame_*` theorem —
the class is now *witnessed-minimal*: every field has a consumer, and the
consumers use nothing beyond the fields. Verified via lake-cache restore +
`lean`-direct (`MarkovTraceOnHecke.lean`, `TauFunctorReduction.lean` both
exit 0); no `lake build` run.

## Cross-references

- #4151 precedent: `QOU/Archimedean/LoopWeightRealSymmReduction.lean` (PSD
  surplus to B2), merge `3e05cf560`
- Attack-options doc §E:
  [`2026-07-24-alpha-em-b2-tau-identification-attack-options.md`](2026-07-24-alpha-em-b2-tau-identification-attack-options.md)
- H4 cyclicity reduction bricks: `9e85264c3` (`trM_cyclic_of_gram_symm`),
  `0f6dd24b2` (gram_symm CLOSEABLE), `4ac696fde` (H3→H4 stabilization rung)
- Tower OPEN classes: `QOU/Machinery/HeckeTowerBasicConstruction.lean`
- Epic: `qou-utb3` (W1 `qou-xik5`, W2 `qou-2017`, W3 `qou-r765`, W4 `qou-o2dk`)
