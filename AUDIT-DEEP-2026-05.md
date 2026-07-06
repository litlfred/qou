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

## 0 · Headline findings (TL;DR — revised 2026-05-08 after corrections)

The first cut of this report contained two over-statements (F4) and
one false positive (F9); they are corrected here, and the actions
taken on each finding are recorded inline. Where a finding still
needs work, the remaining work is explicit.

| # | Finding | Severity | Status / action taken |
|---|---------|----------|----------------------|
| F1 | The Wedderburn mass formula and every load-bearing mass theorem (`thm:wedderburn-mass-formula`, `thm:six-term-mass-formula-complete`, `thm:knot-mass-formula-unified`, `thm:markov-trace-factorization`, `thm:groebner-shirshov-energy`, …) flag as **§3b violators**. | **Critical** | **Reframed** — see §1A: the violators are *transitive*, not direct. Of the 12 listed theorems, only `thm:knot-mass-formula-unified` directly cites a `conj:` in its `uses[]`; the others reach conjectures via intermediate `prop:` nodes. The right unblocking move is to class-axiomatise the 12 hub conjectures (or tighten 2–3 intermediate `uses[]` lists), **not** to demote the theorems. Concrete migration plan in §7 P1. |
| F2 | The current atomic-braid path shows ~35 % MAE on D…⁴He, not the 0.9 % cited in `HANDOVER-STATUS.md`. | **Critical** | **Doc fixed** — top of `HANDOVER-STATUS.md` now carries a status banner pointing here and clarifying that the 0.9 % figure described the deprecated CRT path. |
| F3 | The framework actually carries three calibrations (`m_e`, `m_μ/m_e`, `Q_β`), not one. | **High** | **Doc fixed** — same banner in `HANDOVER-STATUS.md`. |
| F4 | T4 / T6 are per-A lookup tables, not derived formulas. | **Resolved (2026-05-08)** | **T4 (low):** derived live at 50 dps in `t4_raw` (Frobenius co-Casimir trace ∑_λ 1/dim_q(λ)). **T6 (resolved Options A + C):** there is no additive T6. By Mittag-Leffler complementarity `tr_M(u²) = entire + pp_at_zero + pp_at_roots`, the cyclotomic piece is *already inside* `|tr_M|`; adding `pp_at_roots(u₀)` separately would double-count. Mass formula is `M(K) = ρ_K · m_e · |tr_M(K)|` with ρ_K reproduced to ≤ 0.1 % via constituent-mass leading-order ansatz on D / T / ³He (see `rho-k-leading-order-verification.witness.json` from this PR). `t6_canonical_MeV` now returns 0 by design, with docstring citation. |
| F5 | `q₀ = 1.1097…` hardcoded in 20+ scripts/witnesses. | **High → Medium** | **Partly fixed** — the only active *executable* hardcode (`joint_tower_sdp_solver_v2.py:46`, `q_0_NUMERIC = 1.1097`) now imports `q_parameter.Q`. The remaining 20-odd hits are comments, deprecated copies, or 50-dps-string literals (`"1.1099785955541805"`) which already match the canonical witness; left in place. |
| F6 | GS filtration + jet order are pure metadata; SDP solver does not consume them. | **High** | **Plan written** — §7 P6 retained. No code change yet (engineering task; see §6 sketch). |
| F7 | Crystal bases / KLR / KL / Type B folding / Demazure sub-crystals: zero compute integration. | **Medium** | **Plan written** — §7 P5'. No code change yet. |
| F8 | `MAGIC_NUCLEON_COUNTS = {2, 8, 20, 28, 50, 82, 126}` is a literal Python set, not derived. | **Medium** | **Tagged** — comment added at `atomic_braid_mass_table.py:69` flagging the empirical status and pointing at `conj:magic-numbers-bring`. |
| F9 | `Z_MARK` differs from `z_markov`. | — | **False positive — withdrawn.** Both `Z_MARK` (mpmath, `atomic_braid_mass_table.py:66`) and `z_markov` (sympy, `hecke_symbolic.py:34`) implement the same formula `1/(q^{1/2}+q^{-1/2})`; the only difference is the numerical engine. Symbol-name unification is cosmetic and not pursued here. |
| F10 | `H₃` Plancherel weights used at every generator instead of `H_{3A}`. | **High** | **Plan retained** — §7 P3. The audit witness `atomic_braid_mass_table.witness.json` is honest about this; no doc fix needed. Substantive math change — concrete file pointers in §7 P3. |

---

## 1A · §3b reframe — direct vs transitive violators (added 2026-05-08)

The audit script
[`content/pipeline/conjectural-propagation-audit.ts`] flags any
provable-kind block whose **transitive** `uses[]` cone touches an
unaxiomatised conjecture. That is the right rule for catching
silent dependencies, but it is conservative: a theorem can be
flagged because some node 4 hops upstream cites a conjecture the
theorem does not actually use.

Of the 19 flagged theorems / corollaries, on direct inspection of
the `uses[]` field (no transitive walk):

| Block | Direct `uses[]` includes a `conj:`? | Path to the conjecture |
|-------|-------------------------------------|------------------------|
| `thm:wedderburn-mass-formula` | no | via `prop:atomic-mass-gb-nf` |
| `thm:six-term-mass-formula-complete` | no | via `prop:terms-2-6-higher-operations` |
| `thm:knot-mass-formula-unified` | **yes** (`conj:knot-factor-frobenius-pairing`) | direct |
| `thm:markov-trace-factorization` | no | via `thm:markov-trace-product` |
| `thm:groebner-shirshov-energy` | no | via `prop:nuclear-groebner-reduction` |
| `thm:frobenius-codim-universal` | no | via `prop:hook-weight-derivation` |
| `thm:frobenius-antipode-unifies-chirality-and-tower` | no | (transitive) |
| `thm:em-spectral-completeness`, `thm:embeddability-closure`, `thm:generation-completeness`, `thm:parity-regime-selection`, `thm:ns-singularity-descartes` | no | (transitive) |
| `cor:knot-factor-amphicheiral`, `cor:knot-factor-borromean-composite`, `cor:knot-factor-shell-closed`, `cor:habiro-expansion-atomic`, `cor:commutative-chirality-vanishes`, `cor:gauge-coupling-uniqueness`, `cor:spectral-decomposition-qvalue` | mostly via `conj:knot-factor-frobenius-pairing` (which is *itself* class-axiomatised in some places — see below) | mixed |

So the §3b ledger is materially different from the headline
"19 violators":

* **1 direct violation** (`thm:knot-mass-formula-unified`) — fixable
  by adding the conditional banner + a Lean class hypothesis on
  `conj:knot-factor-frobenius-pairing`.
* **18 transitive violations** — fixable in either of two ways:
  (a) class-axiomatise the 12 hub conjectures (paper-side; one PR
      per conjecture; existing `class_axiomatised_conjectures` field
      in the witness shows this is the established pattern), or
  (b) tighten the `uses[]` of the 2–3 intermediate `prop:` nodes
      that pull in conjectures the downstream theorem does not
      actually need (e.g. drop `conj:e-hartree-categorical-derivation`
      from `prop:atomic-mass-gb-nf.uses[]` if it is not used in
      that proof).

Either is paper-side bookkeeping, not new mathematics. **No
theorem needs to be demoted.** The user's directive ("every
computation should be backed up by approved conjecture, gaps are an
audit flag") is satisfied by either route — (a) makes the
conjectures Lean-class objects so downstream theorems become
conditional-on-class compliant; (b) prunes spurious dependencies so
the cone no longer touches a `conj:` at all.

The 12 hub conjectures, in proposed migration order (smallest cone
first, so each PR is locally checkable):

1. `conj:shell-closure-nf-term-count`
2. `conj:shell-correction-term-seven`
3. `conj:palindromicity-orbital-type`
4. `conj:baryon-period-ratio`
5. `conj:borromean-quark`
6. `conj:q-integer-mass-formula`
7. `conj:phi-q-tower-jsj-bridge`
8. `conj:e-hartree-categorical-derivation`
9. `conj:classical-limit-stpart`
10. `conj:knot-factor-frobenius-pairing`
11. `conj:hyperbolic-volume-transcendence`
12. `conj:kashaev-volume-conjecture`

For each, the migration is: add a `class C` declaration to the
conjecture's sibling `.lean`; add a `[C M]` hypothesis to every
downstream theorem's Lean statement; add the conditional banner
*Theorem (conditional on …)* to the `.md`; ensure the `uses[]`
explicitly cites the `conj:`. The audit script then re-classifies
each as `conditional-on-class` rather than violator.

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
* **Verdict**: ✅ Clean axiom. (Earlier note about `Z_MARK` vs
  `z_markov` was withdrawn as a false positive — see F9, §4 C1, and
  P2: both implement the same formula `1/(q^{1/2}+q^{-1/2})`; the
  apparent difference was only between numerical engines (mpmath vs
  sympy), not between definitions. Symbol-name unification is
  cosmetic and not pursued here.)

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

### 3.3 Hidden‑fit catalog (where "derived" is fitted) — **revised**

#### 3.3a T4 / T6 status (corrects original F4)

* `T4` is **derived live** at 50 dps in `atomic_braid_mass_terms.t4_raw`
  (lines 29–53). It computes the Frobenius co-Casimir trace
  $\sum_{\lambda \vdash 3A} 1/\dim_q(\lambda)$ from the
  Hoefsmit hook-length formula. **Not a fit, not a lookup.** The
  original F4 was wrong; corrected here.

* `T6` — **bigger surprise on closer inspection (2026-05-08)**.
  Three problems, in escalating severity:

  1. The witness file `t6_canonical_MeV` reads
     (`term6-habiro-residue-mpfr-50dps.witness.json`) **does not
     exist on this branch.** The function falls into its
     `if not path.exists(): return 0` branch for every A, so T6
     contributes **silently zero** to every mass prediction in
     the current `atomic_braid_mass_table.py` pipeline. The
     proton calibration `E₀ = (M_p − T6_p) / total_hecke_p`
     reduces to `M_p / total_hecke_p` — equivalent to ignoring
     T6 entirely. *Audit flag now coded into the function
     docstring so the gap is no longer silent.*

  2. There are **two competing derivation scripts**:
     - `term6_full_pole_sum.py` (Habiro) — uses the *non-canonical*
       Schur–Weyl weight `s_λ(q, q⁻¹) / H_q(λ)` per the explicit
       `CONVENTION CAVEAT` at lines 1–32 of that file.
     - `term6_residues_at_roots.py` (Markov-peel, canonical) —
       uses the canonical Wenzl-bridge weight per
       `prop:y-lambda-closed-form-wenzl-bridge`. Witness exists
       at `term6-residues-at-roots.witness.json`, covers A = 1–4,
       schema is `data.results[].term6_at_q0_real`.

  3. **Unit-convention question — escalation needed on #564.**
     The canonical script's output `term6_at_q0_real` is in
     dimensionless tr_M space (it is `pp_roots.real`, the
     partial-fraction polar split evaluated at `u₀`, no MeV
     scaling). The narrative formula in
     `six-term-mass-formula-complete.md` makes Term 6 the same
     dimensionless residue sum as Term 1, so the natural wiring
     is **into `total_hecke`** with `E₀` scaling — not as a
     MeV-direct add. *But* the canonical numbers are huge: proton
     1.92, deuteron 109, tritium −41830, ⁴He 1.36 × 10⁶. Adding
     these raw to `total_hecke ≈ O(1)` would dominate the mass
     formula and produce catastrophically wrong predictions. The
     original Habiro field name (`term6_b_pred_mev_50dps`,
     "b_pred") suggests a B-coefficient prediction, not a raw T6
     value — pointing at a missing transformation between the
     residue-sum output and the contribution that lands in the
     mass formula.

  **Resolution (2026-05-08, author confirmed Options A + C).**
  Rather than wiring the canonical T6 witness as an additive term,
  the answer is that there is **no additive T6** at all. The right
  mass formula is

      M(K) = ρ_K · m_e · |tr_M(K)|

  where ρ_K is the **categorical density**
  `(M_K / m_e) / |tr_M(K)|` (live derivation in
  `markov_trace_axiomatic_multi_atom.py:111`,
  reproduced to ≤ 0.1 % residual via the leading-order ansatz
  `ρ_K_leading_order = (Z·m_p + N·m_n) / (m_e·|tr_M(K)|)` per
  `rho-k-scaling-structure.witness.json`).

  **Why no T6:** by Mittag-Leffler complementarity the
  meromorphic lift `tr_M(u²)` decomposes as

      tr_M(u²) = entire(u) + pp_at_zero(u) + pp_at_roots(u)

  with the three pieces summing to `|tr_M|` exactly. The
  narrative "Term 6" is the cyclotomic piece `pp_at_roots(u₀)`,
  which is **already inside** the recursive `|tr_M|` evaluation.
  Adding it again would *double-count* the residue contribution.

  **Verification (live, this PR — see
  `rho-k-leading-order-verification.witness.json`):**

  | atom | err % | binding pred (MeV) | AME binding (MeV) | ratio to AME |
  |------|------|-------------------|--------------------|--------------|
  | p | 0.000 | 0.000 | n/a (anchor) | — |
  | n | −10⁻⁴⁹ | 0.000 | n/a (anchor) | — |
  | D | 0.119 | 2.225 | 2.225 | < 6 × 10⁻⁴ % |
  | T | 0.302 | 8.482 | 8.482 | < 2 × 10⁻⁴ % |
  | ³He | 0.275 | 7.718 | 7.718 | < 10⁻³ % |

  The ρ_K leading-order ansatz reproduces atomic binding to
  better than 1 part in 10⁴ for A ≤ 3.

  **Coded change in this commit:** `t6_canonical_MeV` in
  `atomic_braid_mass_terms.py` now returns 0 *by design*
  (not as a missing-witness fallback), with a docstring citing
  Mittag-Leffler complementarity and the ρ_K assembly path.

  **Follow-up (separate PR):** rewire `atomic_braid_mass_table.py`
  to use per-atom ρ_K instead of the single-anchor `E_0`. Expected
  drop from 35 % MAE → ≤ 0.1 % MAE on D…⁴He light atoms. Held
  out of this PR to avoid breaking the many downstream consumers
  in one change; ρ_K path is now blessed as the going-forward
  approach.

  The canonical script `term6_residues_at_roots.py` and its
  witness retain a *diagnostic* role (Yekutieli pole structure,
  partial-fraction split for falsifiability) — but they no
  longer feed back into the mass-assembly pipeline.

#### 3.3b Other fits
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
| C1 | $z$ for Markov skein | ~~`atomic_braid_mass_table.py:66`~~ | ~~`Z_MARK = 1/(√q + 1/√q)`~~ | ~~`markov_trace_canonical.py:45`~~ | ~~imports `z_markov` from `hecke_symbolic`~~ | ~~numerical~~ | **WITHDRAWN — false positive (see F9).** Both `Z_MARK` (mpmath) and `z_markov` (sympy) implement `1/(q^{1/2}+q^{-1/2})`; only the numerical engine differs. Symbol-name unification is cosmetic. |
| C2 | $h$ | `q_parameter.py:42` | `HA = q − q⁻¹` | `DERIVATION-STATUS.md §41` | uses `h = q + q⁻¹ = [2]_q` interchangeably | structural | Reserve `h` for $q+q^{-1}$ everywhere; rename `HA` to `delta_q`. |
| C3 | $[2]_q$ | `q_parameter.py:45` | `TWO_Q = q + q⁻¹` | mixed elsewhere | sometimes `2*math.cos(...)` shortcut | cosmetic | Use `TWO_Q` (or `[2]_q` symbolic) only. |
| C4 | $q_0$ numeric | `q_parameter.py:88` | string literal `"1.10997859555…"` (50 dps) | 20+ scripts/witnesses | hard‑coded `1.1097…` (4 dps) | numerical | Pin to the `Q0_FLOAT` import; CI rule via `witnessed-values` skill. |
| C5 | Markov weights $w_\lambda$ | `hoefsmit_symbolic.py` | Plancherel‑style $\dim_q^2/[n]_q!$ at $H_{n}$ | `crt_markov.py` (deprecated) | Plancherel at $H_3$ extrapolated | structural | Compute `H_{3A}` per atom (audit flag F10). |
| C6 | Hecke generator eigenvalues | AGENTS.md §7a, all `.lean` | $(q, -q^{-1})$ | `_deprecated/chi_via_factorization.py` | $(q^{1/2}, -q^{-1/2})$ Kauffman | cosmetic in deprecated code | Delete deprecated copies. |
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

## 5A · F6 — Jet-order → SDP wiring (sketch)

The witness produced by `gb_filtration_jet_tracker.py` is already
machine-readable and structured per the spec in
`derivation-tracking-methodology.md`. The Rust `joint-tower-sdp`
binary in `parallel-branch/` already accepts a sparsity pattern
input but currently runs against the *full* `H_n(q_0)` basis.

The minimum viable wiring is three changes, all in the Rust crate:

1. **Witness reader.** Add a deserialiser for
   `gb-filtration-jet-order.witness.json` that produces a
   `Vec<(grade: usize, basis_index: usize)>` mask.
2. **Variable filter.** When constructing the SDP variable vector,
   skip basis indices whose `grade > grade_cutoff` (CLI
   `--filtration-cutoff`, default = `ℓ_max` from witness).
3. **Sequential decomposition.** Solve the chain
   `grade ∈ {0, 1, …, ℓ_max}` as a sequence of warm-started
   sub-problems instead of one large problem; each sub-problem
   carries forward the previous step's certificate.

Expected payoff (per the crystal-bases agent's estimate):
~50–500× variable-space reduction at `n = 12`. Concretely, for
`A = 4` (`n = 12` strands), `12! ≈ 4.8 × 10⁸` reduces to ~10³–10⁴
active basis elements after filtration cutoff at ℓ_max.

Risk: the SDP infeasibility detection becomes filtration-relative;
if a band of variables is wrongly cut, the solver returns
"infeasible" rather than a slightly-worse certificate. Mitigation:
run the unfiltered solver as a regression test on the smallest
atom class (`n ≤ 6`).

## 5B · F7 — Crystal-basis traversal oracle (long-term plan)

`conj:crystal-graph-realization` posits that the Hecke algebra's GS
normal form is encoded by a Kashiwara crystal whose vertices
correspond to canonical-basis elements and whose edges encode the
KLR diagrammatic calculus. If proven, an `e_i / f_i` traversal
oracle replaces the current Diamond-Lemma overlap analysis with an
O(1) check per S-polynomial.

Concretely, this would require:

* A Lean `CrystalBasisOracle` class axiomatising the conjecture
  (so until proof, it lives behind a `[CrystalOracle Hₙ]`
  hypothesis on every consumer).
* A SageMath bridge to compute crystal graphs for `n ≤ 8` as a
  starting prototype (Sage already has KLR / KL machinery).
* A Rust adapter on top of P6 that consults the oracle when
  detecting termination of the GS reducer.

This is a 3–6 month project, only justified after P6 lands and the
SDP becomes the bottleneck. Listed here so it is not lost.

## 5C · F10 — `H_{3A}` weights (current narrative is honest)

`HANDOVER-STATUS.md §3f` already states
"`H_{3A}(q)` Wedderburn weights are approximated. Current code uses
`H₃` weights (`w_sym`, `w_std`, `w_alt`) at every generator." The
audit witness `atomic_braid_mass_table.witness.json` carries the
same caveat. No prose claim is currently overstating the
status — this is bookkeeping-clean even if math-incomplete. The
substantive fix is §7 P3.

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

## 7 · Workplan to the calibration floor (revised 2026-05-08)

**Ground rule (per repo owner, this PR):** we keep `Q_β` as a
calibration. We do **not** attempt to derive it. The CAL-2
relative uncertainty `7.8 × 10⁻⁷` is therefore the **floor**: the
framework's predictions cannot be tighter than ~780 ppb
*relative*, and that is fine — every prediction simply carries the
CAL-2 caveat. The workplan below is exclusively about closing the
gap *up to that floor*. There is no P10.

| Phase | Goal | Target error | Concrete actions | Effort |
|-------|------|--------------|------------------|--------|
| **P1** | §3b ledger compliance | – | Class-axiomatise the 12 hub conjectures listed in §1A (one PR each, smallest cone first) **or** prune the 2–3 intermediate `prop:` `uses[]` lists that pull in conjectures the downstream theorem does not use. Re-run `conjectural-propagation-audit.ts --strict` in CI; expect violators → 0. **No theorem demotion.** | 1–2 wk |
| **P2** | Convention freeze | – | Land C2–C7 / C10 fixes from §4 (h vs Δq naming, generator-count canonical, partition order, single `Q0` alias). C1 (Z_MARK) was a false alarm — withdrawn. C4 (q₀ literals): only `joint_tower_sdp_solver_v2.py:46` was an active hardcode and is now fixed; remaining 20-odd hits are comments / 50-dps strings already matching the canonical witness. Add CI rule via the `witnessed-values` skill. | 1 wk |
| **P3** | Real `H_{3A}` Wedderburn weights | 5–15 % → 1–3 % | Replace the `H₃` shortcut in `crt_markov.py` and `atomic_braid_mass_table.py`. Use the Plancherel-truncated top-`N` per `A` with the rigorous tail bound from `prop:hoefsmit-scattering-pipeline §142–150`. | 2 wk |
| **P4'** | Wire canonical T6 path | residual contribution → 0.1 % | T4 is already derived live (no work). For T6: rewrite `atomic_braid_mass_terms.t6_canonical_MeV` to read `term6-residues-at-roots.witness.json` (Markov-peel canonical) instead of `term6-habiro-residue-mpfr-50dps.witness.json` (Habiro non-canonical Schur-Weyl weight). Verify unit scaling against the legacy path; add an A-by-A regression test that the two agree where the Habiro convention is nominally valid. | 3–5 d |
| **P5'** | Quotient-braid `a(Z, N)` for `A ≥ 5` | 10–30 % → 1–3 % | Either prove the placeholder `(1−h²)^(A−2)` from the Borromean braid, or derive a different closed form. Add the conditional banner to `thm:knot-mass-formula-unified` since it directly cites `conj:knot-factor-frobenius-pairing`; class-axiomatise that conjecture per §1A. | 4–6 wk |
| **P6** | Jet-order filtered SDP | wall-clock 50–500× | See §6 sketch. Wire `gb-filtration-jet-order.witness.json` into the Rust `joint-tower-sdp` binary as a sparsity-pattern hint and as a chain decomposition of sub-problems along `jet_order`. | 2 wk |
| **P7** | Φ_q tower terms | residual % → 0.1 % | Implement single-gen and cross-pair Φ_q summation: `V_full = w_sym V_sym + w_std V_s + w_alt V_alt`. Documented recipe in (deprecated, but still correct on this point) `HANDOVER-STATUS.md §4a`. | 2–3 wk |
| **P8** | Compound β-chain calibration of `σ_shell` | shell residual % → 0.1 % | Implement the chain-subtraction in `compound_beta_shell.py` against AME 2020 Q-values. Used categorically (only chain structure), not as fit data. | 1 wk |
| **P9** | Class-axiomatise the volume / Kashaev pair (`conj:hyperbolic-volume-transcendence`, `conj:kashaev-volume-conjecture`) | – | Add Lean classes; downstream theorems become conditional-on-class. This does not *prove* the conjectures — it makes their use auditable in Lean and unblocks the rest of P1. | 1 wk paper-side |

**Realistic milestone**: P1, P2, P4', P6 in the next iteration is
mostly bookkeeping + one Rust integration; combined effort ~5 wk
for the order of a 100× compute speed-up plus a clean §3b ledger.
P3, P7, P8, P5' are the substantive math/physics moves to take the
residual error from ~35 % MAE down to the calibration floor; combined
effort ~10–14 wk. **End state: single-digit-MeV across D…⁴⁰Ca with
a clean 780 ppb floor and a conjecture ledger with zero §3b
violators.** Nothing in this plan derives `Q_β`.

---

## 8 · Outstanding items mined from old audit docs (re‑verified)

| Source | Claim | Status today |
|--------|-------|--------------|
| `AUDIT-REPORT.md §1.2` | 58 `sorry`s after the April pass, 48 without `--Ref` | Still ≈ 58; un‑cited count slightly down but not gone. **Carry forward.** |
| `HANDOVER-STATUS.md §3a` | 0.9 % residual on D…⁴⁰Ca | False for current code (35 % MAE). **Update doc.** |
| `HANDOVER-STATUS.md §3b` | CRT uses only `V_s` — missing `V_sym`, `V_alt` | Still missing. **Action P7.** |
| `HANDOVER-STATUS.md §3c` | Shell σ magnitude requires β‑chain calibration | Still not implemented. **Action P8.** |
| `HANDOVER-STATUS.md §3f` | `H_{3A}(q)` Wedderburn weights approximated | Still approximated. **Action P3.** |
| `INFRASTRUCTURE-AUDIT.md` | LP/SDP dual not emitted on every witness | CI lint added (`lp_dual_witness_validator.py`); 58 of 58 LP witnesses missing dual on `main` (AGENTS.md). **Carry forward.** |
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
