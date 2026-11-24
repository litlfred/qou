---
name: lean-mathlibext-curator
roles: [collaborator, owner]
description: >
  Curate QOU's non-QOU-specific Lean 4 mathematics under the Two-Tier Community
  Contribution Architecture: Tier A (`MathlibExt` selective `mathlib4` core PR
  candidates) and Tier B (6 standalone Lean Reservoir `lean_lib` community
  packages: `HeckeTemperleyLieb`, `TwistedFrobeniusHopf`, `ToricConicOpt`,
  `CompactQuantumMetrics`, `QCalculus`, `BraidKnotOctonion`). Enforces strict
  zero-`QOU.*` upward imports, §7c base-ring generality, and Mathlib4 style via
  `scripts/lean-best-practices-lint.py` and `scripts/lean-kg-detangler.py`.
allowed-tools: Read Edit Write Bash Grep Glob
---

# Two-Tier `Mathlib4` & Lean Reservoir Community Curator (`lean-mathlibext-curator`)

## 1. Architectural Role (Supersedes Single-File `QOU/MathlibExt.lean`)

QOU no longer stages reusable mathematics in a single 5-section `QOU/MathlibExt.lean` file. Instead, all non-QOU-specific mathematics (`~1,680` pure-math modules) is curated into a **Two-Tier Community Contribution Architecture** (Epic `qou-lnkg`, [`docs/audits/2026-11-23-lean-kg-detangler-and-reservoir-options.md`](../../docs/audits/2026-11-23-lean-kg-detangler-and-reservoir-options.md)):

### Tier A — Selective `leanprover-community/mathlib4` Core PR Staging (`MathlibExt`)
Small, foundational, domain-general lemmas that belong directly inside monolithic `mathlib4`:
- `List` / `Finset` / permutation / sort / `foldl`–`foldr` `Monoid` plumbing (`QOU/MathlibExt.lean` §1–§3)
- General linear algebra & matrix lemmas (`CauchyBinet`, `FrobeniusInnerProduct`, `EndBaseChange`, `EndSemisimple*`)
- Elementary ordered-field & `Real.sqrt` / `Real.rpow` / convexity / trapezoid bounds (`ConcaveOnSum`, `CorrectedTrapezoid`, `QOU/MathlibExt.lean` §4)
- General complex/analytic & Čech nerve infrastructure (`ArgumentPrinciple*`, `DoublyPeriodicLiouville`, `Borel*` resummation, `Clausen`, `DirichletL`, `Polylogarithm`, general `Cech*` colimits)

Every Tier-A declaration MUST carry a machine-readable upstream destination tag in its docstring:
```lean
/-- Sorting a list preserves its sum over any `AddCommMonoid`.

    TODO upstream: `Mathlib.Algebra.BigOperators.Group.List` — permutation invariance of `List.sum`. -/
```

### Tier B — 6 Standalone Lean Reservoir Community `lean_lib` Packages
Cohesive, specialized mathematical theories designed as standalone **Lean Reservoir** community libraries depending **only** on `Mathlib` (and `UGB` where applicable) with **strictly zero `QOU.*` model imports**:

| # | Reservoir `lean_lib` Target | Mathematical Scope |
|---:|---|---|
| 1 | **`HeckeTemperleyLieb`** | Iwahori–Hecke $H_n(q)$, Coxeter/Bruhat subwords, Temperley–Lieb $TL_n(q)$ & Catalan bases, Jones/Markov/Ocneanu traces, Hoefsmit seminormal irreps, Young/SYT/Schur–Weyl (layers on [`folio/unital-groebner-bases/lean/`](../../folio/unital-groebner-bases/lean/) `UGB` for Gröbner–Shirshov / Kang–Lee–Lee–Oh normal forms) |
| 2 | **`TwistedFrobeniusHopf`** | Nakayama-twisted Frobenius pairings (`NakayamaTwist`, `TwistedAmbidextrousAdjunction`), Sweedler $H_4$ & Taft $T_N(\omega)$ Hopf algebras (`SweedlerJet`, `SweedlerJetIso`, `SweedlerFrobenius`), Higman norm map (`HigmanNormMap`), antipode & tower adjunctions |
| 3 | **`ToricConicOpt`** | Sturmfels–Thomas toric Gröbner chambers, Graver/universal Gröbner test sets, Birch toric equilibria, symmetry-reduced LP/SDP dual certificates (`SymmetryReducedDualCertificate`, `SDP*`, `LPStrongDuality`, `MatrixFarkasInstance`), Perdew–Parr piecewise-linear kinks |
| 4 | **`CompactQuantumMetrics`** | Finite-dimensional Rieffel–Connes compact quantum metric spaces (`FiniteRieffelQuantumMetric`), `LipSeminorm`, Kantorovich–Rubinstein graph/state duality, Woronowicz $\mathcal{O}_q(\mathrm{SU}(2))$ coordinate algebra (`OqSU2ModularNakayama`), universal noncommutative differentials (`UniversalDifferentials`), finite bicommutant/GNS |
| 5 | **`QCalculus`** | $q$-numbers $[n]_q$, $q$-factorials, Gaussian binomials (`QInteger*`, `GaussianBinomial*`), Thomae–Jackson geometric-grid $q$-integrals & $q$-Leibniz rules (`ThomaeJacksonCalculus`), Faddeev & quantum dilogarithms, Rogers–Szegő, Habiro cyclotomic rings (`Habiro/*`) |
| 6 | **`BraidKnotOctonion`** | Artin braid groups $B_n$ (`BraidGroup*`), Burau/Lawrence–Krammer/Alexander invariants (`PLAlexander`), PL knot topology & $\Delta$-equivalence / Moise assembly (`PL*.lean`), octonion/Hurwitz composition algebras & $\mathfrak{g}_2$/$\mathfrak{su}(3)$ derivations (`Octonion*.lean`), pure Bring curve / Riemann–Hurwitz algebraic geometry |

---

## 2. Placement Decision Tree (Mandatory Before Authoring Any `.lean` File)

1. **Does the statement mention ANY QOU physics/model concept** (`substrate_q`, `q0`, `CODATA`, `MeV`, `Proton`/`Neutron`/`Quark`/`Hadron`/`Nucleus`, `QuantumObservableUniverse`, `BraneTower`, `*Context` manuscript class)?
   - **Yes** → Place in the single canonical **QOU chapter subgraph** (`QOU.Core`, `QOU.LiftingDescent`, `QOU.BraidsAndKnots`, `QOU.BringsSurface`, `QOU.Confinement`, `QOU.EightfoldWay`, `QOU.MassTheory`, `QOU.Nuclear`, `QOU.StandardModel`, `QOU.FluidDynamics`, `QOU.InformationTheory`, `QOU.Observations`). **Never** place QOU model types in `MathlibExt` or Tier-B libraries, and **never** create a new synonym directory (`BP009`).
   - **Hybrid file?** → Factor the pure mathematical theorem into Tier A / Tier B first, then import and instantiate it (`R := ℝ`, `q := substrate_q`) inside the QOU chapter module (`Process_GraphDetanglement` `Task_Move`: *move the shared target first, then the importers*).
2. **Is the pure-math result part of one of the 6 specialized Tier-B domains above?**
   - **Yes** → Curate under the corresponding Tier-B Reservoir subgraph with **zero `QOU.*` model imports**.
3. **Is it a small, general-purpose lemma fitting an existing `Mathlib.*` file?**
   - **Yes** → Curate under Tier-A `MathlibExt` with a `TODO upstream: Mathlib.<Module>` docstring tag (first verify via `lean_leansearch` / `lean_loogle` or `grep` in `.lake/packages/mathlib/Mathlib/` that Mathlib4 does not already have it!).

---

## 3. Strict Mathlib4 & Lean Reservoir Standards (`BP001`–`BP008`)

Every Tier-A and Tier-B module MUST satisfy all 8 standards enforced by [`scripts/lean-best-practices-lint.py`](../../scripts/lean-best-practices-lint.py):

1. **Explicit `autoImplicit` off (`BP001`):** Include `set_option autoImplicit false` after the module docstring so the file remains sound if extracted outside QOU's `lakefile.toml`.
2. **Header & Docstring Order (`BP002`):**
   - `/- Copyright (c) 2026 ... Apache 2.0 ... -/` header,
   - Targeted `import Mathlib.<Submodule>` lines **before** any `/-! ... -/` block (Lean 4.24+ requirement),
   - `/-! # Title ... -/` module docstring summarizing main definitions, theorems, and `[bibkey]` references,
   - `/-- ... -/` docstring on every public `def`, `structure`, `class`, `theorem`, and `lemma` (`docBlame`).
3. **Minimal Targeted Imports (`BP003`):** Never `import Mathlib` or `import Mathlib.Tactic`; import the exact `Mathlib.Algebra.*` / `Mathlib.Tactic.Ring` modules used.
4. **Mathlib4 Naming (`BP004`):** `UpperCamelCase` for types/`structure`s/`class`es/`inductive`s; `snake_case` for `theorem`/`lemma` proofs and `Prop`-valued predicates; `_of_` hypothesis suffixes on conditional implications.
5. **§7c Maximal Typeclass & Universe Generality (`BP005`):** State algebraic identities over `{R : Type*} [CommRing R]` / `[Field R]` and ordered inequalities over `[Field K] [LinearOrder K] [IsStrictOrderedRing K]` (never gratuitous `ℝ`); keep categories universe-polymorphic `Category.{v, u} C`.
6. **Zero Empirical / Float Literals (`BP006`):** Zero decimal literals (`1.1097`), `Float`, `CODATA`, or `substrate_q`.
7. **Zero Vacuity, Zero `sorry`, Zero Custom Axioms (`BP007`):** Kernel trust boundary strictly `[propext, Classical.choice, Quot.sound]`; zero `: True`, zero `native_decide`, zero `sorry`, zero `axiom`.
8. **Strict Zero-`QOU.*` Upward Import Boundary (`BP008`):** Zero imports from QOU physics/model modules.

---

## 4. Verification & Audit Commands (CPU-Throttled)

Always export single-thread caps and run under `nice -n 15` (see [`lean-build-hygiene.md`](lean-build-hygiene.md)):

```bash
export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 \
       OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1

# 1. Lint a specific Tier-B Reservoir package (or `MathlibExt` / `all-community`):
nice -n 15 python3 scripts/lean-best-practices-lint.py --package TwistedFrobeniusHopf

# 2. Lint your branch's changed/added .lean files (blocks critical BP001-BP009):
nice -n 15 python3 scripts/lean-best-practices-lint.py --diff

# 3. Verify zero new community -> QOU.* cut-edges in the KG DAG:
nice -n 15 python3 scripts/lean-kg-detangler.py --summary-only

# 4. Type-check in the isolated symlink-farm overlay (NEVER bare `lake build`):
nice -n 15 bash scripts/lean-overlay-env.sh init
nice -n 15 bash scripts/lean-overlay-env.sh build QOU/<Path>/<Module>.lean
```

---

## 5. Cross-References

- [`lean-build-hygiene.md`](lean-build-hygiene.md) — CPU throttling, `lean-overlay-env.sh`, and `scripts/*lean*` router.
- [`content-graph.md`](content-graph.md) — Lean subgraph heuristics `L1..L6` and monograph placement rules.
- [`formalizer.md`](formalizer.md) — §7c base-ring cheat-sheet and tactic ladder.
- [`lean-proof-vacuity-audit.md`](lean-proof-vacuity-audit.md) — Semantic non-vacuity and `#print axioms` verification.
