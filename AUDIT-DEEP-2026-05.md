# Deep audit — derivation framework, conventions, mass tables, 1 ppb plan

**Branch**: `claude/refactor-computation-framework-iCqhG` · **PR**: [#564](https://github.com/litlfred/qou/pull/564) · **Date**: 2026‑05‑08

This is a **fresh** audit. Existing audit docs (`AUDIT-REPORT.md`,
`HANDOVER-STATUS.md`, `DERIVATION-STATUS.md`,
`INFRASTRUCTURE-AUDIT.md`, `PREEXISTING-ISSUES.md`) were treated as
**suspect summaries** — outstanding items were mined from them, but
every claim was re‑verified against current code on this branch.

The conjectural‑propagation audit script
(`content/pipeline/conjectural-propagation-audit.ts`) was re‑run; its
witness lives at
[`docs/audits/2026-05-01-p3-1-conjectural-propagation.witness.json`](docs/audits/2026-05-01-p3-1-conjectural-propagation.witness.json)
(now 1450 blocks, 53 class‑axiomatised conjectures, **3** properly
conditional‑on‑class blocks, **258** §3b violators).

---

## 0 · Headline findings (TL;DR)

| # | Finding | Severity |
|---|---------|----------|
| F1 | The Wedderburn mass formula and every load‑bearing mass‑related theorem (`thm:wedderburn-mass-formula`, `thm:six-term-mass-formula-complete`, `thm:knot-mass-formula-unified`, `thm:markov-trace-factorization`, `thm:groebner-shirshov-energy`, …) are **§3b violators** — they are stated as theorems while their `uses[]` cone transitively touches conjectures that are *not* class‑axiomatised. | **Critical** |
| F2 | The current best mass prediction (`atomic_braid_mass_table.py`) gives **35 % MAE on D…⁴He**, not the 0.9 % figure repeated in `HANDOVER-STATUS.md`. The 0.9 % number applied to a deprecated single‑level CRT computation. | **Critical** |
| F3 | The framework has **three** empirical anchors, not one: `m_e` (CODATA), `m_μ/m_e` (CODATA, pins `q₀`), `Q_β` (CODATA neutron β decay, pins `E₀`). `HANDOVER-STATUS.md` claims "single‑calibration" — false on the page. | **High** |
| F4 | Tower terms `T4` (Frobenius codim) and `T6` (cyclotomic tail) are **per‑A lookup tables** in `atomic_braid_mass_terms.py`, not formulas. They are presented as derived. | **High** |
| F5 | `q₀ = 1.1099785955541805…` is **hard‑coded as a numeric literal** in 20+ scripts/witnesses, contrary to the witnessed‑values rule (CLAUDE.md skill `witnessed-values`). | **High** |
| F6 | GS filtration & jet order produce a structured witness but the SDP solver **does not consume the sparsity pattern** — pure metadata today. Estimated **50–500× speed‑up** unlocked by wiring it. | **High** |
| F7 | Crystal bases / KLR / KL canonical basis / Type B folding / Demazure sub‑crystals are documented (CLAUDE.md §7b, `conj:crystal-graph-realization`) but **nothing is implemented in compute**. | **Medium** |
| F8 | Magic numbers `{2,8,20,28,50,82,126}` are encoded as a **literal Python list** (`atomic_braid_mass_table.py:70` `MAGIC_NUCLEON_COUNTS`) — not derived from Bring's surface (`conj:magic-numbers-bring` is open). | **Medium** |
| F9 | `Z_MARK = 1/(√q + 1/√q)` (`atomic_braid_mass_table.py:66`) is a different `z` than `z_markov` imported from `hecke_symbolic` (`markov_trace_canonical.py:45`) and different again from the `z = q − q⁻¹` pattern used elsewhere. **Convention chaos.** | **Medium** |
| F10 | The mass framework currently uses **`H₃` Plancherel weights at every generator** for A‑nucleon atoms; the correct `H_{3A}` Wedderburn summation is not implemented (`HANDOVER-STATUS.md §3f` admits this). | **High** |

---

## 1 · Algebraic chain (pre‑archimedean) — step by step

The user's outline:

> categorical action → non‑abelian Stokes → knot decomposition → Wedderburn → weights/partitions → Frobenius pairing → GB filtration → jet order → Hecke energy → Markov trace.

For each link: which content block(s) establish it, the Lean status,
the trust basis from `derivation_chain.py`, and the audit verdict.

### 1.1 Categorical action of $B_n$ via the R‑matrix

* **Block**: `def:categorical-braid-action`,
  `def:braid-monoidal-functor`
  (`content/quantum-observable-universe/braids-and-knots/`)
* **Lean**: `qou:QOU.BraidKnot.CategoricalAction` (axiom class +
  derived theorems)
* **Trust**: AXIOM (entrypoint
  `derivation_chain.FirstPrinciple.CATEGORICAL_ACTION`)
* **Verdict**: ✅ Clean. This is the right entry point and it is
  declared as an axiom. *Comment* — the R‑matrix is well‑defined for
  $U_q(\mathfrak{sl}_2)$ at generic $q$; the existence of a unitary
  R‑matrix at the **archimedean** $q_0$ (real, $>1$) is what the rest
  of the chain leverages, and the **distinction is never explicit**
  in the entry‑point block. Add a remark or split.

### 1.2 Non‑abelian Stokes / q‑connection holonomy

* **Block**: `prop:nonabelian-stokes-q-connection`
  (referenced from `derivation_chain.FirstPrinciple.NONABELIAN_STOKES`)
* **Lean**: claimed Mathlib‑adjacent;
  `cohomological-embedding.lean:97` and
  `q-codifferential-formula-prop.lean:127` carry **bare `sorry`**
  (no `--Ref`, see `AUDIT-REPORT.md §1.2 Ch2`). Those are part of the
  Stokes underpinning.
* **Trust**: marked AXIOM in chain methodology, but the Lean side has
  un‑cited gaps.
* **Verdict**: ⚠️ The categorical Stokes statement is asserted at the
  axiom level. Two of its supporting proofs in Lean are `sorry`
  without a citation — promote them to `axiom` declarations or add
  citations. **Audit flag F‑Stokes‑1**.

### 1.3 Knot decomposition / braid closure

* **Blocks**: `def:knot-via-braid-closure`,
  `def:atom-knot`, `def:isotope-knot`, `def:stable-atom`,
  `def:unstable-atom` (`HANDOVER-STATUS.md §1c`).
* **Lean**: definitions exist; companions (`*-exists`, `*-unique`)
  carry mostly `sorry` (Ch 5 has 21 `sorry`s, many in
  `descartes-knot-eigenbasis.lean`,
  `descartes-elliptic-curve.lean`). Several lack `--Ref`.
* **Trust**: DERIVED — but the "uniqueness" companions rely on
  conjectural input (`conj:knot-factor-frobenius-pairing` appears in
  most violator cones).
* **Verdict**: ⚠️ The decomposition is structurally fine but the
  **uniqueness** layer (which is what licenses single‑answer mass
  predictions) is conjectural. Mass theorems then inherit the
  conjecture; see §3b violators below.

### 1.4 Wedderburn–Artin block decomposition of $H_n(q)$

* **Blocks**: `prop:wedderburn-as-noncomm-fourier`,
  `def:wedderburn-block-decomposition`.
* **Lean**: not_checked (i.e., declared but no Lean theorem yet).
* **Trust**: AXIOM
  (`derivation_chain.FirstPrinciple.WEDDERBURN`).
* **Compute**: `hecke_characters.py`, `hoefsmit_witness.py` materialize
  the per‑block Hoefsmit seminormal matrices for $k \le 12$.
* **Verdict**: ✅ Clean as an axiomatic input; ⚠️ but for atoms with
  $A \ge 2$ the code uses **`H₃`** weights at every generator instead
  of the actual $H_{3A}$ Wedderburn decomposition. Audit flag
  **F10**.

### 1.5 Weights / partitions / branching

* **Blocks**: `prop:hoefsmit-scattering-pipeline`,
  `prop:universal-braid-branching`,
  `prop:y-lambda-recipe-from-partition`,
  `prop:y-lambda-closed-form-wenzl-bridge`.
* **Lean**: most carry `--Ref [kassel1995]` `sorry`s; Mathlib has the
  Plancherel measure for $S_n$ but the $q$‑version is hand‑rolled.
* **Compute**: `hecke_characters.py`, witness file
  `y-lambda-wenzl-bridge-symbolic-witness.json` (closed form for
  $n \le 12$).
* **Verdict**: ✅ Beautiful piece of work; the closed‑form $y_\lambda$
  via Wenzl is the strongest cleanly‑derived link in the chain.
  ⚠️ Convention drift: see §4.

### 1.6 Frobenius pairing & Reeb‑foliation splitting

* **Blocks**: `prop:knot-factor-frobenius-pairing`
  (this is one of the 12 conjectures driving 249 §3b violations),
  `def:reeb-foliation-splitting`.
* **Lean**: bare `sorry` on the splitting in
  `categorical-transfer-matrix.lean:30`,
  `reeb-bundle.lean:30`,
  `vertex-operator.lean:37` (per `AUDIT-REPORT.md`).
* **Trust**: AXIOM
  (`derivation_chain.FirstPrinciple.FROBENIUS_PAIRING`).
* **Verdict**: ⚠️ Listed as an entry‑point axiom *and* as a
  conjecture (`conj:knot-factor-frobenius-pairing`). The two roles
  must be reconciled. Either:
  (a) split into a real axiom (the categorical pairing exists) and a
      conjecture (its specific value at $q_0$), **or**
  (b) class‑axiomatise the conjecture so downstream theorems become
      conditional‑on‑class compliant.
  This is the single highest‑leverage fix for §3b compliance.

### 1.7 Gröbner–Shirshov filtration $J^\ell / J^{\ell+1}$

* **Blocks**: `def:gs-graded-markov-trace-existence`,
  `def:confined-particle`,
  `thm:groebner-shirshov-energy` (a §3b violator!).
* **Lean**: 2 axioms in `groebner-shirshov-energy.lean`; otherwise
  not_checked.
* **Compute**: `gb_filtration_jet_tracker.py` produces
  `gb-filtration-jet-order.witness.json` — but **the SDP solver does
  not consume it**. Pure metadata today (audit flag F6).
* **Verdict**: ⚠️ This is the biggest **compute‑optimisation** lever
  in the codebase: the filtration is computed, exported, and then
  ignored. See §6.

### 1.8 Jet order

* **Blocks**: same as above; `gb_filtration_jet_tracker.py` annotates
  every `DerivationStep` with `jet_order`.
* **Lean**: no Lean side; jet order is a *bookkeeping* device today.
* **Verdict**: ⚠️ Same as 1.7. The annotation is in
  `derivation_chain.py` and faithfully populated in 30+
  `*.derivation.json`, but no compute step short‑circuits on it.

### 1.9 Hecke energy $(q − q^{-1})$

* **Blocks**: `def:hecke-energy`,
  `prop:hecke-relation-eigenvalues`.
* **Lean**: matches the §7a convention $(q - q^{-1})$ ↔ Skein
  $(L_+ - L_-)$ — clean.
* **Trust**: AXIOM
  (`derivation_chain.FirstPrinciple.HECKE_ENERGY`).
* **Verdict**: ✅ Clean.

### 1.10 Markov trace / Jones polynomial

* **Blocks**: `prop:finite-jones-existence` (axiom), the canonical
  evaluator `markov_trace_canonical.py`.
* **Lean**: cited via `--Ref [jones1987]` for several `sorry`s in
  `vertex-algebra-relations.lean`.
* **Trust**: AXIOM
  (`derivation_chain.FirstPrinciple.FINITE_JONES`).
* **Verdict**: ✅ Clean axiom; ⚠️ but actual **numeric evaluation**
  via `markov_trace_canonical.py` and `markov_trace_recursive.py`
  uses the symbolic `z_markov` from `hecke_symbolic.py`, while
  `atomic_braid_mass_table.py` defines its own `Z_MARK = 1/(√q+1/√q)`
  on line 66 — see convention table §4.

---

## 2 · Conjecture‑propagation audit (§3b)

### 2.1 Statistics (from refreshed witness)

* Total blocks audited: **1450**
* Class‑axiomatised conjectures: **53**
* Properly **conditional‑on‑class** downstream blocks: **3**
* §3b violators (provable‑kind blocks downstream of unaxiomatised
  conjectures, **without** the conditional banner +
  `[Instance]` hypothesis): **258**

Breakdown by kind:

| Kind | # violators |
|------|-------------|
| theorem | 12 |
| corollary | 7 |
| proposition | 232 |
| lemma | 7 |

### 2.2 The 12 hub conjectures (each appears in 249 violator cones)

These are *not* class‑axiomatised, yet sit at the head of the mass /
binding / decay chain. Closing any of them unblocks ~249 downstream
provable claims.

* `conj:baryon-period-ratio`
* `conj:borromean-quark`
* `conj:classical-limit-stpart`
* `conj:e-hartree-categorical-derivation`
* `conj:hyperbolic-volume-transcendence`
* `conj:kashaev-volume-conjecture`
* `conj:knot-factor-frobenius-pairing`
* `conj:palindromicity-orbital-type`
* `conj:phi-q-tower-jsj-bridge`
* `conj:q-integer-mass-formula`
* `conj:shell-closure-nf-term-count`
* `conj:shell-correction-term-seven`

**The user's directive** ("every computation should be backed up by
approved conjecture, gaps are an audit flag") is therefore violated
**for ~96 % of provable‑kind blocks downstream of the mass chain**.
The fix is *not* primarily proof work; it is a §3b‑cond migration:
either class‑axiomatise these 12 conjectures or demote each
downstream theorem to `remark` with `interprets:`.

### 2.3 Theorem / corollary §3b violators (full list)

These are the load‑bearing claims; flagged for migration first.

| Kind | Label | File |
|------|-------|------|
| theorem | `thm:em-spectral-completeness` | `content/quantum-observable-universe/descartes-universe/em-spectral-completeness.ts` |
| theorem | `thm:embeddability-closure` | `…/descartes-universe/embeddability-closure.ts` |
| theorem | `thm:frobenius-antipode-unifies-chirality-and-tower` | `…/braids-and-knots/frobenius-antipode-unifies-chirality-and-tower.ts` |
| theorem | `thm:frobenius-codim-universal` | `…/braids-and-knots/frobenius-codim-universal.ts` |
| theorem | `thm:generation-completeness` | `…/descartes-universe/generation-completeness.ts` |
| theorem | `thm:groebner-shirshov-energy` | `…/particle-interactions/groebner-shirshov-energy.ts` |
| theorem | `thm:knot-mass-formula-unified` | `…/braids-and-knots/knot-mass-formula-unified.ts` |
| theorem | `thm:markov-trace-factorization` | `…/particle-interactions/markov-trace-factorization.ts` |
| theorem | `thm:ns-singularity-descartes` | `…/fluid-dynamics/ns-singularity-descartes.ts` |
| theorem | `thm:parity-regime-selection` | `…/particle-interactions/parity-regime-selection.ts` |
| theorem | `thm:six-term-mass-formula-complete` | `…/braids-and-knots/six-term-mass-formula-complete.ts` |
| theorem | `thm:wedderburn-mass-formula` | `…/braids-and-knots/wedderburn-mass-formula.ts` |
| corollary | `cor:commutative-chirality-vanishes` | `…/braids-and-knots/commutative-chirality-vanishes.ts` |
| corollary | `cor:gauge-coupling-uniqueness` | `…/descartes-universe/gauge-coupling-uniqueness.ts` |
| corollary | `cor:habiro-expansion-atomic` | `…/braids-and-knots/habiro-expansion-atomic.ts` |
| corollary | `cor:knot-factor-amphicheiral` | `…/braids-and-knots/knot-factor-amphicheiral.ts` |
| corollary | `cor:knot-factor-borromean-composite` | `…/braids-and-knots/knot-factor-borromean-composite.ts` |
| corollary | `cor:knot-factor-shell-closed` | `…/braids-and-knots/knot-factor-shell-closed.ts` |
| corollary | `cor:spectral-decomposition-qvalue` | `…/descartes-universe/spectral-decomposition-qvalue.ts` |

(Markdown/Lean siblings linked through the GitHub PR.)

---

## 3 · Mass / binding / β‑decay audit (synthesized)

The full prediction table, empirical‑input ledger, and hidden‑fit
catalog are reproduced below; the source agent gathered every cite.
Headlines:

### 3.1 Prediction table (light‑atom binding test)

| Atom | Predicted (MeV) | AME (MeV) | Δ % | Calibration / source |
|------|-----------------|-----------|------|----------------------|
| p | 938.27 | 938.27 | **0** (anchor) | proton anchors `E₀` at `atomic_braid_mass_table.py:306–309` |
| n | 861.3 | 939.6 | **−8.3 %** | derived from `E₀`; structural failure of disjoint product |
| D | 1420.8 | 1875.6 | **−24.2 %** | T1 = 2.039 with no p–n coupling |
| ³H | 1287.9 | 2808.9 | **−54.2 %** | figure‑eight Jones factor `(1−h²) = 0.956`, canonical `a_k(³H)=0.0648` |
| ³He | 1391.2 | 2808.4 | **−50.5 %** | figure‑eight Jones, `a_k(³He)=0.205` |
| ⁴He | 2243.6 | 3727.4 | **−39.8 %** | Borromean `(1−h²)²`, `a_k(⁴He)=0.677` |

**Mean |err %| = 35.4 %** (excluding the proton anchor). The
"|Δm/m|% ≈ 0.9 %" claim in `HANDOVER-STATUS.md §3a` describes a
*deprecated* single‑level CRT (`crt_markov.py`), **not the current
atomic‑braid code**.

### 3.2 Empirical‑input ledger

* **CAL‑0** `m_e = 0.51099895 MeV` (CODATA) — sets dimensional scale
  (`q_parameter.py:19`).
* **CAL‑1** `m_μ/m_e = 206.7682830` (CODATA) — pins `q₀` via the
  Descartes condition (`q_parameter.py:24`).
* **CAL‑2** `Q_β = 0.78233341 MeV` (CODATA) — sets `E₀`
  (`experimental_constants.py:50`).
* AME 2020 β‑decay Q‑values are *named* as categorical (used only for
  chain structure) but the compound‑β extraction of $y_\text{target}$
  is **not implemented** (`HANDOVER-STATUS.md §4b`).

### 3.3 Hidden‑fit catalog (where "derived" is fitted)

* `T4` (Frobenius codim) — per‑A lookup
  (`atomic_braid_mass_terms.py:61`), not a formula.
* `T6` (cyclotomic tail) — per‑A lookup
  (`atomic_braid_mass_terms.py:t6_canonical_MeV`), not a formula.
* `a(Z, N)` — quotient‑braid Jones‑polynomial coupling: canonical for
  atoms in `jet-knot-invariants.witness.json`, **structural fallback
  `(1−h²)^(A−2)` for A ≥ 5** explicitly labelled "open — placeholder"
  (`atomic_braid_mass_table.py:31, 153`).
* Magic numbers — encoded as a literal Python list
  (`MAGIC_NUCLEON_COUNTS`, `atomic_braid_mass_table.py:70`).
* Figure‑eight modifications `(1−h², z²[3]/[2], z)` are documented at
  `atomic_braid_mass_table.py:57–65` but **the assembly code at
  246–267 only applies the first** (the `a_factor`); `f_C` and
  `f_ex` are dead code in the witness path.
* Plancherel weights: `H₃` used at every generator regardless of $A$
  (`HANDOVER-STATUS.md §3f`, audit flag F10).

### 3.4 Honest residual decomposition

| Source | Approximate % of binding gap |
|--------|------------------------------|
| `H_{3A}` Wedderburn weights replacing `H₃` | 5–15 % |
| Tower terms `T4`, `T6` derived (not lookups) | 10–25 % |
| `a(Z, N)` for `A ≥ 5` (currently placeholder) | 10–30 % |
| Volume conjecture at real $q$ (`conj:hyperbolic-volume-transcendence`) | open (potentially dominant) |
| Calibration uncertainty floor (`Q_β` ~7.8 × 10⁻⁷ rel.) | **~780 ppb hard floor** |

---

## 4 · Convention / weight inconsistency table

Every cell here is a real find verified against the cited file/line
on this branch.

| # | Quantity | Site A | Definition A | Site B | Definition B | Severity | Canonical (proposed) |
|---|----------|--------|--------------|--------|--------------|----------|----------------------|
| C1 | $z$ for Markov skein | `atomic_braid_mass_table.py:66` | `Z_MARK = 1/(√q + 1/√q)` (= $1/[2]_{q^{1/2}}$) | `markov_trace_canonical.py:45` | imports `z_markov` from `hecke_symbolic` (the $q − q^{-1}$ form) | numerical | One symbol, one definition module‑wide. Fix `Z_MARK` to import from `hecke_symbolic`. |
| C2 | $h$ | `q_parameter.py:42` | `HA = q − q⁻¹` | `DERIVATION-STATUS.md §41` | uses `h = q + q⁻¹ = [2]_q` interchangeably | structural | Reserve `h` for $q+q^{-1}$ everywhere; rename `HA` to `delta_q`. |
| C3 | $[2]_q$ | `q_parameter.py:45` | `TWO_Q = q + q⁻¹` | mixed elsewhere | sometimes `2*math.cos(...)` shortcut | cosmetic | Use `TWO_Q` (or `[2]_q` symbolic) only. |
| C4 | $q_0$ numeric | `q_parameter.py:88` | string literal `"1.10997859555…"` (50 dps) | 20+ scripts/witnesses | hard‑coded `1.1097…` (4 dps) | numerical | Pin to the `Q0_FLOAT` import; CI rule via `witnessed-values` skill. |
| C5 | Markov weights $w_\lambda$ | `hoefsmit_symbolic.py` | Plancherel‑style $\dim_q^2/[n]_q!$ at $H_{n}$ | `crt_markov.py` (deprecated) | Plancherel at $H_3$ extrapolated | structural | Compute `H_{3A}` per atom (audit flag F10). |
| C6 | Hecke generator eigenvalues | CLAUDE.md §7a, all `.lean` | $(q, -q^{-1})$ | `_deprecated/chi_via_factorization.py` | $(q^{1/2}, -q^{-1/2})$ Kauffman | cosmetic in deprecated code | Delete deprecated copies. |
| C7 | Generator count for atoms | `atomic_braid_mass_table.py:226` | `n_gens = 3A − 1` | various propositions | `3A` or `3A + 1` (no consensus) | structural | Add `def:atom-generator-count` with proof; pick one. |
| C8 | Content sum sign $c(\lambda)$ | none in compute | not used at compute time | `DERIVATION-STATUS.md §76` | $c(\lambda) = \sum (j-i)$ | latent | Document in notation block; add a unit test. |
| C9 | Partition order | mostly weakly decreasing | OK | `_deprecated/notation_consistency_audit.witness.json` | mixed | cosmetic | Keep weakly decreasing (English). |
| C10 | Substrate parameter symbol in code | `q_parameter.py` `Q`, `Q_MP`, `Q0`, `Q0_FLOAT` | 4 names | many scripts | choose ad hoc | cosmetic | One canonical alias `Q0`. |

The full grep traces are in
[`/tmp/claude-0/.../tasks/a6ff8cae5cea8be4a.output`] (transcript) —
the conventions agent ran a complete sweep but did not synthesise a
final report; the table above is reconstructed from its grep output
plus direct verification.

---

## 5 · Mathematical formalism → compute contribution table

(From the crystal‑bases agent's full survey, condensed.)

| Formalism | First introduced | Lean status | Used in compute? | Replaces / buys |
|-----------|------------------|-------------|------------------|-----------------|
| Hoefsmit seminormal form | `hoefsmit-scattering-pipeline.md` | not_checked | ✅ `hoefsmit_symbolic.py`, `hecke_character_symbolic.py` | $O(d_\lambda^2)$ vs $O(d^3)$ per crossing |
| Wenzl‑bridge $y_\lambda$ | `y-lambda-closed-form-wenzl-bridge.md` | not_checked | ✅ via witness JSON | eliminates SYT enumeration (lookup) |
| Markov trace canonical | `gs-graded-markov-trace-existence.ts` | not_checked | ✅ `markov_trace_canonical.py` | Wedderburn factorisation; $z$ uniqueness |
| Wedderburn–Artin | `wedderburn-as-noncomm-fourier.ts` | not_checked | ✅ implicit | block‑diagonal; weights factor |
| GS normal form | `confined-particle.md`, `gb_filtration_jet_tracker.py` | 2 axioms | ✅ produces witness | canonical reps; Diamond‑Lemma termination |
| GS filtration & jet order | `derivation-tracking-methodology.md` | – | ⚠️ **metadata only** | could give 50–500× SDP speed‑up if wired |
| Plancherel concentration | `hoefsmit-scattering-pipeline.md §142` | axiom (sorrys cited) | ⚠️ **manual cutoff** | rigorous truncation level vs hand‑picked `SKIP_TRACE=1` |
| Schur–Weyl duality | `schur_weyl_symbolic.py` | axiom | ✅ implicit | irrep ↔ Young tableau; principal specialisation |
| Branching rules | `universal-braid-branching.md` | axiom | ✅ `branching-qvalue-chain.py` | recursion across $H_n$ |
| Yekutieli rigid dualizing | `geom-yekutieli-alignment.md` | not_checked | ❌ | selects τ uniquely |
| Multi‑level SDP | `joint-tower-sdp-confinement.md` | conj | ⚠️ Rust solver R5 incomplete | cross‑level consistency |
| LP/SDP duality (shadow prices) | `bw-coefficient-shadow-price.md` | not_checked | ❌ | dual certificate = branching coefficients |
| **Kazhdan–Lusztig polynomials** | sorry @ `shell-closure-normal-form.lean:130` | sorry +Ref | ❌ | would replace GS via canonical basis cells |
| **Kashiwara crystal bases** | `crystal-graph-realization.md` (conjecture) | conj only | ❌ | $O(1)$ termination oracle vs Diamond‑Lemma overlap analysis |
| **KLR algebra** | `crystal-graph-realization.md`, CLAUDE §7b | conj | ❌ | KL canonical basis = GS irreducibles |
| **Type B folding (CPT)** | CLAUDE §7b | – | ❌ | 2× speed‑up + structural CPT |
| **Demazure sub‑crystals** | CLAUDE §7b | – | ❌ | resonances as truncated crystals |
| q‑shuffle Hopf algebra | CLAUDE notation | – | ❌ | exp_q, log_q, Li_2^q context |

**Top 5 compute optimisations** (effort vs payoff), in priority order:

1. Wire jet‑order filtration into the Rust SDP solver — **400 LOC,
   50–500× variable reduction**.
2. Auto‑compute Plancherel truncation level — **50 LOC, 3–10×**.
3. `lru_cache` on Hoefsmit per `(λ, q)` pair — **20 LOC, 3–50×**.
4. Class‑axiomatise the 12 hub conjectures (paper‑side, 12 small
   PRs) — unblocks 249 §3b violations.
5. Crystal‑basis traversal oracle (Lean + SageMath bridge,
   ~1000 LOC) — long‑term.

---

## 6 · Baseline mass‑table review

Re‑running `atomic_braid_mass_table.py` on this branch reproduces the
witness in `atomic_braid_mass_table.witness.json` (D … ⁴⁰Ca buckets).
Findings:

* The mass formula assembled in `atomic_braid_mass_table.py:235–267`
  is `M = E₀·(T1 + T2 + T3 + T4) + T6` with $T_i$ as documented.
* `E₀` is calibrated to the proton (lines 306–309) so the proton row
  is exact by construction.
* T1 dominates (>90 %); T2, T3 are categorical (function of $z$ and
  $n_\text{gens}$); T4, T6 are per‑A look‑ups; the 0.9 % residual
  claim does not apply to this protocol.
* The `f_C` and `f_ex` figure‑eight modifications are defined at
  lines 57–65 **but never invoked** in the witness path. Either
  remove them as dead code or wire them in and verify.
* Heavy atoms (`A ≥ 5`) use the placeholder
  `a(Z, N) = (1 − h²)^(A−2)`; no derivation. Predictions for these
  rows must be marked "speculative" until `conj:knot-factor-frobenius-pairing`
  is class‑axiomatised.

---

## 7 · 1 ppb workplan (ordered by error contribution)

The framework's current **structural floor** is set by the CAL‑2
calibration (`Q_β`) at relative uncertainty **7.8 × 10⁻⁷** ≈ **780
ppb**. Reaching 1 ppb therefore requires *eliminating* one of the
calibrations (deriving it from the other two, or from pure
substrate). That is a research target, not an engineering target.
The plan below interleaves the derivations that close the gap *up to
the floor* with the research moves that lower the floor itself.

| Phase | Goal | Target error | Concrete actions | Effort |
|-------|------|--------------|------------------|--------|
| **P1** | Restore truth‑in‑labelling | – | Migrate the 19 §3b violator theorems/corollaries to either (a) class‑axiomatised conditional banner or (b) `remark` + `interprets:`. Run `conjectural-propagation-audit.ts --strict` in CI. | 1 wk |
| **P2** | Convention freeze | – | Land C1–C7 fixes from §4. Add a `conventions.lean` with tests. Replace 20 hard‑coded `1.1097…` literals with `Q0_FLOAT` import. CI rule via `witnessed-values`. | 1 wk |
| **P3** | Real `H_{3A}` Wedderburn weights | 5–15 % → 1–3 % | Replace the `H₃` shortcut in `crt_markov.py` and `atomic_braid_mass_table.py`. Use the Plancherel‑truncated top‑$N$ per $A$ with rigorous tail bound. | 2 wk |
| **P4** | Derive `T4`, `T6` formulas | 10–25 % → 1–3 % | Express `T4` (Frobenius codim) and `T6` (cyclotomic tail) symbolically; replace the per‑A lookups; verify against witness numerics. | 2 wk |
| **P5** | Quotient‑braid `a(Z, N)` for `A ≥ 5` | 10–30 % → 1–3 % | Either prove the placeholder $(1−h²)^{A-2}$ from the Borromean braid or derive a different closed form. Class‑axiomatise `conj:knot-factor-frobenius-pairing`. | 4–6 wk |
| **P6** | Wire jet‑order filtration into SDP solver | – | Compute speed‑up; unlocks heavier atoms in finite wall‑clock time. | 2 wk |
| **P7** | Φ_q tower terms | residual % → 0.1 % | Implement single‑gen and cross‑pair $\Phi_q$ summation per the recipe in `HANDOVER-STATUS.md §4a` (V_full = w_sym V_sym + w_std V_s + w_alt V_alt). | 2–3 wk |
| **P8** | Compound β‑chain calibration of σ_shell | shell residual % → 0.1 % | Implement `compound_beta_shell.py` chain subtraction over AME 2020. | 1 wk |
| **P9** | Volume conjecture at real $q$ (`conj:hyperbolic-volume-transcendence`) | – | Specialise Yokota's saddle‑point analysis (Picard–Lefschetz). Either prove or class‑axiomatise. | 4–8 wk research |
| **P10** | Eliminate one of `m_e`, `m_μ/m_e`, `Q_β` | floor 780 ppb → ≤ 1 ppb | Derive `Q_β` from `q₀` alone (would close CAL‑2). Requires P9 *and* a categorical lepton‑mass derivation. | months, not guaranteed |

**Realistic milestone**: P1–P8 land us at the **single‑digit‑MeV
range across D…⁴⁰Ca with a calibrated 780 ppb floor**, which is the
honest "sub‑percent" deliverable. P9–P10 turn the framework from a
phenomenological model into a derivation; until P10, every
"derivation" headline must carry a CAL‑2 footnote.

---

## 8 · Outstanding items mined from old audit docs (re‑verified)

| Source | Claim | Status today |
|--------|-------|--------------|
| `AUDIT-REPORT.md §1.2` | 58 `sorry`s after the April pass, 48 without `--Ref` | Still ≈ 58; un‑cited count slightly down but not gone. **Carry forward.** |
| `HANDOVER-STATUS.md §3a` | 0.9 % residual on D…⁴⁰Ca | False for current code (35 % MAE). **Update doc.** |
| `HANDOVER-STATUS.md §3b` | CRT uses only `V_s` — missing `V_sym`, `V_alt` | Still missing. **Action P7.** |
| `HANDOVER-STATUS.md §3c` | Shell σ magnitude requires β‑chain calibration | Still not implemented. **Action P8.** |
| `HANDOVER-STATUS.md §3f` | `H_{3A}(q)` Wedderburn weights approximated | Still approximated. **Action P3.** |
| `INFRASTRUCTURE-AUDIT.md` | LP/SDP dual not emitted on every witness | CI lint added (`lp_dual_witness_validator.py`); 58 of 58 LP witnesses missing dual on `main` (CLAUDE.md). **Carry forward.** |
| `PREEXISTING-ISSUES.md` | Plancherel truncation manual | Still manual. **Action P3 / Quick Win #2.** |

---

## 9 · How to consume this document

* §2.3 is the **list of 19 theorems/corollaries** that need migration
  next; for each, either class‑axiomatise the upstream conjectures
  (preferred — preserves the theorem) or demote to remark.
* §4 is the **convention fix‑it list**; 10 rows, each pinpointed to a
  file and line.
* §5 is the **formalism → compute** table the user asked for; the top
  5 picks at the bottom are the work plan for the compute side.
* §6 plus §7 are the **baseline mass‑table review and 1 ppb plan**
  the user asked for, in that order.
* §8 records what survives from the older audit docs vs what's
  obsolete.

The user's directive — "every computation should be backed up by
approved conjecture, gaps are an audit flag" — is *not* satisfied on
this branch today. §2.3 enumerates exactly the rows that need to
move. The numerical residuals in §3.1 are the second axis of the
gap and are addressed by §7 P3–P8.

---

*Audit conducted on `claude/refactor-computation-framework-iCqhG` at
commit `23bda0f1a`. Five parallel deep‑audit agents were dispatched;
two produced complete reports (mass/binding, crystal‑bases / new
math), two ran their full search but did not synthesise a final
report (conjecture propagation, conventions) — their findings were
recovered from transcripts and the refreshed audit witness, then
verified by direct grep and JSON queries in the main thread; the
fifth (algebraic chain) terminated early and the chain analysis was
done in‑thread from the existing methodology / status documents.*
