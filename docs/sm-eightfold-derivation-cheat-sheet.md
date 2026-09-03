# Standard Model + eightfold way — standing derivation cheat sheet

**Status:** standing reference. Read this before making, citing, or reviewing
any claim about a Standard-Model parameter or an eightfold-way multiplet.
Analogous in role to
[`canonical-derivation-cheat-sheet.md`](canonical-derivation-cheat-sheet.md)
and [`canonical-mass-formula-guardrail.md`](canonical-mass-formula-guardrail.md);
this one is the *SM/flavour* counterpart, which the corpus previously lacked.

**Created:** 2026-08-14, on the owner's question *"what of the 8-fold way and
std model is derived or near-term derivable from QOU?"*

**What this file is NOT.** It is not a new result and it does not supersede any
per-block tier. Every row below is sourced to a block, a Lean file, a witness,
or an audit. Where this file disagrees with a source, the source wins and this
file is stale — fix it here.

> **Currency 2026-09-03.** Refreshed against the live corpus in session `qou-ggdk`;
> the measurement and every correction below are recorded in
> [`audits/2026-09-03-sm-26-term-status.md`](audits/2026-09-03-sm-26-term-status.md).
> Headline unchanged (1 input / 1 proxy / 1 partial / 2 conjectural / 21 open;
> all eight `sm-params-*` blocks byte-identical to their sidecars). Rows marked
> *(2026-09-03)* were stale and are corrected in place.

---

## 0. The one-paragraph answer

**Nothing in the Standard Model is derived to experimental precision, and one
eightfold-way entry is derived at all.** The framework's SM/flavour surface is
a large, unusually honest catalogue of *what is missing*, plus a growing stack
of proved negatives that delete false evidence. The genuinely valuable
structural finding is that the 21 "open" parameters are **not 21 independent
problems** — they funnel into **three missing objects** (§4). Two of the three
have partial derivations already.

All four of the eightfold way's headline quantitative relations are now scored.
Gell-Mann–Okubo, the decuplet equal-spacing rule behind the `Ω⁻` prediction, and
the Coleman–Glashow relation are all **proved content-free as derivation
targets** (identities of the ansatz), with their deviations (≈ 6 %, ≈ 9.2 % and
≈ 0.8 %) relocated as the real testable content. The **nonet mixing angle is proved content-bearing** — the ansatz does
not constrain it at all — which makes it the one eightfold-way quantity whose
derivation would be evidence for anything. It is gated on `N = 3` (§4-A).

---

## 1. Where the authoritative sources live

There is no single source; that is itself the problem this file addresses.
SM-relevant results are spread over **six** locations, and the most-cited audit
covers only two of them.

| Source | Kind | Scope | Currency |
|---|---|---|---|
| [`appendix-standard-model/sm-params-*.md`](../content/quantum-observable-universe/appendix-standard-model/) (8 blocks) | in-paper | the 26 parameters, one section per chunk | live |
| [`appendix-standard-model/sm-open-problems.md`](../content/quantum-observable-universe/appendix-standard-model/sm-open-problems.md) | in-paper ledger | 14 structural ingredients | live |
| [`eightfold-way/eightfold-open-problems.md`](../content/quantum-observable-universe/eightfold-way/eightfold-open-problems.md) | in-paper ledger | 23 ingredients + 9 numbered open items | live |
| [`audits/2026-08-08-sm-eightfold-epistemic-accounting.md`](audits/2026-08-08-sm-eightfold-epistemic-accounting.md) | point-in-time audit | **only** the two chapters above | 2026-08-08 |
| [`coordination/sm-26-parameter-chip-away.md`](coordination/sm-26-parameter-chip-away.md) | active ledger | attack fronts, PR cluster, convergences | live |
| `particle-interactions/`, `nuclear-interactions/`, `mass-theory/`, `QOU/AlphaEM/` | scattered | T₃/GMN, Weinberg, staircase-EW, α_EM ladder | live |

> ### ⚠ The scope trap — do not quote "1 derived" as a corpus figure
>
> The 2026-08-08 epistemic accounting is the best single document on this
> subject and its numbers are correct **for its declared scope** — the
> `eightfold-way/` and `appendix-standard-model/` chapters only. It says so in
> its own §9. But at least four *other* chapters carry SM-relevant results, including
> the two strongest ones:
>
> - `QOU/ParticleInteractions/WeakIsospinT3Grading.lean` — T₃ from signed
>   writhe, GMN closure (§3.2 below)
> - `QOU/AlphaEM/FormLadderAnchorDominance.lean` + the α_EM form ladder —
>   **0.313 ppb** proton-anchored with the derived Schwinger term (§3.3 below)
>
> So "one derived entry" is a **chapter** count, not a **corpus** count. It
> errs conservative, but an agent citing it as corpus-wide is misciting it.

---

## 2. Tier legend (used in every table below)

| Tier | Meaning |
|---|---|
| `input` | one of the three calibration observables — not a prediction |
| `proxy` | a calibration proxy, exact by construction under the canonical pin |
| `derived` | output of the construction, no fitted parameter, no data inversion |
| `partial` | a derived or conditional structure exists; the parameter is not closed |
| `conjectural` | a precise identification exists without a derivation |
| `standard` | true of any `SU(3)` / any `ℕ` — correctly applied textbook material |
| `proved-neg` | a machine-checked negative: deletes a target or a route |
| `open` | nothing in the corpus closes it |

`sorry-free ≠ derived`; `conditional-proved ≠ premise-established`;
`defined residual ≠ derived decomposition`. See AGENTS.md for all three.

---

## 3. The 26 Standard-Model parameters

**Headline: 1 input + 1 proxy + 1 partial + 2 conjectural + 21 open.** Zero
derived to experimental precision. Source:
[`sm-params-intro.md`](../content/quantum-observable-universe/appendix-standard-model/sm-params-intro.md).

Counting convention: 19 renormalisable (9 charged-fermion masses, 4 CKM,
3 gauge couplings, 2 Higgs, 1 θ_QCD) + 7 neutrino (3 masses, 3 PMNS angles,
1 Dirac phase) = 26. Majorana phases are not counted.

### 3.1 Charged-fermion masses (9)

| # | Parameter | Tier | What exists | What is missing |
|---|---|---|---|---|
| 1 | `m_e` | **input** | CAL-1, the dimensional unit | — (not a prediction) |
| 2 | `m_μ` | **proxy** | CAL-2 proxy, `m_μ/m_e = Vol(4₁)/ℏ_q²` pins q₀ | under the proton pin it is a genuine prediction and **misses L2 by 963.6×** (~210 ppb) — the μ–p substrate tension |
| 3 | `m_τ` | **open** | `prop:tau-leptonic-universality` (branching-ratio universality, not a mass) | carrier ID. Direct volume reading refuted over a 25-knot search (scope-(a)); complex-volume `Vol + i·CS` search sharpened the negative (#4591): 14.5 bits of entropy forbids census ID |
| 4–5 | `m_u`, `m_d` | **open** | constituent structure of the Borromean baryon braid | see the extraction note below |
| 6 | `m_s` | **open** | winding `n=5`, gen-2 block | collides with charm on `(n, T₃)`; needs a third flavour grade |
| 7 | `m_c` | **open** | complex-mass constituent functional (conjecture, no instance) | **4 negatives** (#4584, #4594): tower scope-(a), carrier scope-(b), composite volume, Frobenius block ratio O(1) vs O(100) |
| 8–9 | `m_b`, `m_t` | **open** | nothing | no knot/braid identification as mass carriers |

> **Reframing (#4602) — read before attacking any quark mass.** Confined-quark
> masses are **not direct observables**: they are scheme-dependent Lagrangian
> parameters extracted by inverting hadron spectroscopy. The framework need not
> *define* `m_q`; it needs to derive the observables the extraction consumes.
> Four charm attacks were category errors for exactly this reason.

> **`m_d − m_u` — the one honestly extractable quark quantity, and its single
> blocker.** Its experimental source is `Δ_pn` minus the EM self-energy, and the
> framework derives `Δ_pn`. Stage-1 scoping is done
> ([`quark-mass-extraction-stage1.witness.json`](../computations/quark-mass-extraction-stage1.witness.json)):
> `δ_QCD = Δ_pn + E_EM`, with `Δ_pn = 1.2933 MeV` framework-derived. **Blocked on
> one object** — the intra-nucleon EM self-energy, i.e. the open *two-like-charge
> EM-linking invariant*. (This previously added *"which is the same invariant
> owning 69 % of the ³He mirror residual. Deriving it closes both."* — **wrong
> on both counts, corrected 2026-08-25**; see the box under §4-B. The mirror
> split is a *binding* difference, and single-nucleon self-energy provably
> cancels in binding energy.) No `m_d − m_u` value is claimed.
> `m_u + m_d` is **not** extractable: its source is `m_π²`, and `m_π` is CAL-3 —
> circular.

### 3.2 Quark mixing — CKM (4)

| # | Parameter | Tier | Status |
|---|---|---|---|
| 10 | `θ₁₂` (Cabibbo) | **open** | no candidate mechanism |
| 11 | `θ₂₃` | **open** | — |
| 12 | `θ₁₃` | **open** | — |
| 13 | `δ_CKM` | **open** | CP violation surveyed observationally; a spectral-form section discusses where a phase *could* live |

**These are `unposed`, not merely uncomputed.** A mixing matrix presupposes a
flavour basis; the framework has not fixed what its flavour DOF are beyond the
isospin doublet. Blocked behind §4-A and §4-C.

> **Adjacent partial result — the weak isospin `T₃` (#4618, `qou-tdrd`).**
> `QOU/ParticleInteractions/WeakIsospinT3Grading.lean`, sorry-free. The signed
> writhe factors as `κ = sign(κ)·|κ| = T₃ × generation-winding`, so
> `T₃ = sign(κ)/2 ∈ {±½}` is orthogonal to the generation *by construction*,
> derived from an oriented crossing already in the corpus. It resolves
> charm ≠ strange (both `n = 5`, opposite `T₃`) and closes Gell-Mann–Nishijima.
>
> **Read the GMN closure at its true width — now machine-checked (2026-08-15).**
> `gellMannNishijima` is stated over six quarks, but `hyperchargeLeft` is the
> **constant** `1/3` and both `emCharge` and `T3` are functions of the
> up/down-type bit alone, so the six cases collapse to **two distinct arithmetic
> rows** (`2/3 = 1/2 + 1/6`, `−1/3 = −1/2 + 1/6`). That collapse is now proved
> rather than merely observed:
>
> | theorem | content |
> |---|---|
> | `hyperchargeLeft_constant` | `Y` carries no per-quark information |
> | `gmn_data_factors_through_weakType` | all three GMN ingredients factor through the up/down bit |
> | `gmn_check_has_two_distinct_rows` | every quark lands on one of two distinct `(Q, T₃, Y)` rows |
> | `genWinding_finer_than_gmn_data` | `u`, `c`, `t` differ in winding but share a GMN row — the relation is blind to the generation |
>
> The check is real (a wrong sign or a wrong `½` still breaks it) but it is one
> sign correlation plus one normalisation, verified twice — not six independent
> confirmations. The wide phrasing is corrected at both sites (the Lean
> docstring and the chip-away ledger) and can no longer recur unnoticed. Bean
> `qou-8z5j`. Compare the "4 of 10,000" over-presentation (§6).

### 3.3 Gauge couplings (3)

| # | Parameter | Tier | Status |
|---|---|---|---|
| 14 | `α_EM` | **partial** | conditional fixed-point structure; **per-loop measure open** |
| 15 | `sin²θ_W` | **conjectural** | `conj:weinberg-angle-categorical` |
| 16 | `α_s` | **open** | *(2026-09-03)* no derivation — two written expressions exist and neither determines a value: `1/α_s = q^p[9]_q` in `computations/alpha_k_selection_rule_conditional.py` (bracket writhe-forced, `p` an undetermined 1-parameter family, only `α_s·α_W = α_EM` invariant, conditional, scale-free) and a fit-shaped `α_s(M_Z) = q⁻¹/[7]_q ≈ 0.1181` in `docs/beta-decay-handoff.md` that `qou-5iaz` forbids wiring. No fixed-point analogue for the colour sector; blocked on the colour SU(3) action (`conj:sm-colour-stabilizer-action`) |

> **`α_EM` — the corpus's most accurate SM number, and the appendix does not
> state it.** The assembled form is
> `1/α = q[9]_q[10]_q + 2g/(4π(g−1)) + αH(1−h²α) + Δ₂`, `g = 4`, `H = [2]_q/(8π)`,
> `h = q−q⁻¹` (the Hecke structure constant, **not** `ℏ_q = 1−q⁻¹`); `Δ₂` is the
> uncomputed archimedean two-loop. `α` is on both sides — solved as a fixed
> point, not a series. Integers
> structurally derived (Bring genus; crossing numbers of `T(2,9)`, `T(3,5)`),
> **no coefficient fitted**. Residuals
> ([`alpha-em-form-ladder.witness.json`](../computations/alpha-em-form-ladder.witness.json),
> [`2026-08-11-alpha-em-anchor-dominance.md`](audits/2026-08-11-alpha-em-anchor-dominance.md)):
>
> | form | anchor | residual |
> |---|---|---:|
> | quadratic (truncate after `αH`) | **proton** (2026-08-07 default) | 1.67 ppb |
> | quadratic | muon | 81.04 ppb *(live CODATA-2022 anchor, regenerated 2026-09-03; 80.51 at the retired pin A)* |
> | **cubic** (retain `(1−h²α)`) | **proton** | **0.313 ppb** ≈ 2.09 σ_α |
>
> The cubic is the corpus's best; quoting 1.67 understates it by 5.3×. Against
> the L2 100× criterion (`σ_α/100 ≈ 0.0015` ppb) it is still ~209× short — the
> schwinger witness's *"misses its 100× target by only ~2×"* conflates the σ
> multiple with the target multiple (`qou-ydmy`).
>
> Three cautions, all load-bearing:
> 1. **Three unproved classes** remain in the derivation — conditional, not closed.
>    The per-loop measure is not derived. `partial` is the correct tier.
> 2. **The anchor choice IS the residual.** The μ–p spread (78.84 ppb) is ~47×
>    the proton-anchored residual, and
>    `no_anchor_blind_affine_correction_closes_gap` proves no anchor-blind
>    term can absorb it. This is the μ–p substrate tension surfacing in a second
>    observable — which also makes α_EM a **second independent witness for the
>    proton pin** (chosen on precision grounds in 2026-05-28, prior to and
>    independently of α_EM — so this is not anchor-shopping).
> 3. **Appendix currency — FIXED 2026-08-14 (`qou-fmyd`).**
>    [`sm-params-gauge-couplings.md`](../content/quantum-observable-universe/appendix-standard-model/sm-params-gauge-couplings.md)
>    now states the form, both anchored residuals, and all three
>    undischarged qualifications. **Resolved / re-scoped (2026-09-03):** the assertion `source` strings are now
>    proton-framed; the one stale field is `honest_status.not_at_target`
>    (*"best ~81 ppb muon"*). The quoted muon figure 80.51 ppb is at the
>    **retired** pin A — at the live CODATA-2022 anchor it is 81.04 ppb
>    (verdicts unchanged). Both ladder producers hardcode their q₀ literals and
>    are invisible to the three anchor detectors. **Larger issue:** three rival
>    α_EM constructions circulate — this ladder (0.313 ppb), the Chern–Simons
>    `.md` form the L2 dashboard actually consumes (−467.6 ppb, κ conjectural),
>    and the CS `.lean` (+2.59 ppb, κ = 8q, PSLQ-ruled-out); the block's `.md`
>    and `.lean` disagree by 470 ppb (`qou-aemx`). The per-loop measure stays
>    owner-gated; the EM holonomy germ is LIVE (necessary, not sufficient)

> **`sin²θ_W` — the two numbers are now reconciled in-paper (`qou-s2pl`, 2026-08-14).**
> They measure different constructions, so neither refutes the other — but the
> smaller one is **not** an accuracy result, and the block now says so.
> - [`weinberg-angle-categorical.md`](../content/quantum-observable-universe/nuclear-interactions/weinberg-angle-categorical.md)
>   evaluates the Hecke-eigenvalue ratio at the pure pattern and gets
>   `cot θ_W ≈ 0.6594` against the CODATA `1.823` — a **64 % miss**, and says so.
> - [`2026-05-06-close-321-weinberg-gap.md`](audits/2026-05-06-close-321-weinberg-gap.md)
>   claims the `(3,2,1)` eigenvalue-ratio gap closes to **0.127 %** via a factor
>   `q^(1/h_corner)` with `h_corner = 5`, "no fit constants introduced".
>
> **Reconciled in-paper 2026-08-14.** They measure different constructions, so
> neither refutes the other. **Do not cite 0.127 % as a framework accuracy
> result:** the producing witness declines to support it. The residual factor
> was the **closest of 74 enumerated candidates**, the best missing the required
> `1.02239` by `1.3×10⁻³`, and the witness records
> `ansatz_supported_at_1e_3 = false`, `ansatz_falsified_at_1e_2 = false`,
> `path_c_status = "inconclusive"`. The surviving exponent *is* expressible as a
> corner hook of `(3,2,1)`, which makes it structurally **available** — but
> availability after a proximity search is not derivation, and the sweep ranged
> well beyond the hook set `{1,3,5}`. Tier stays `conjectural`.
>
> The tractable lever is #4597: the **Milnor triple linking `μ̄₁₂₃`** is the
> writhe-independent second invariant and separates the two `U(1)`s (Lean,
> sorry-free). The relative `U(1)` coupling normalisation still inherits the
> open SU(3)-flavour sector.

### 3.4 Higgs sector (2)

| # | Parameter | Tier | Status |
|---|---|---|---|
| 17 | `m_H` | **conjectural** | `conj:electroweak-higgs-torus-link-triplet`: `H = T(2,8)`, `W = T(2,4)`, `Z = T(2,6)`. Torus links have `Vol = 0`, so the chain is Reshetikhin–Turaev at a root of unity, with **two open inputs** (level selection; invariant→mass formula). Best probes land **within a factor of two** — honestly reported as not a prediction |
| 18 | `v` (EW scale) | **open** | `conj:g-action-on-substrate` is the natural home; open at the closure level. Nothing extracts `v` (or `G_F`) |

> **Structural divergence worth stating.** `v` normalises every SM mass via
> Yukawa. Its absence means the framework's mass predictions run an entirely
> different route (calibrated volume–density and Hecke-energy chains). Any
> completed derivation must reconcile the two parameterisations — this is not a
> missing number, it is a missing bridge.

### 3.5 Strong-CP angle (1)

| # | Parameter | Tier | Status |
|---|---|---|---|
| 19 | `θ_QCD` | **open** | ceiling proved, smallness open |

The framing phase `q^{w·c}` is the same *kind* of object as a θ-term, and its
per-crossing coupling is already structurally fixed at `c = 1/2` by
`def:coulomb-charge`. **Proved sorry-free (#4596):** charge conjugation acts as
the bar involution `q ↦ q⁻¹`, so a CP-even (bar-symmetric) colour sector has a
*real* framing phase, forcing `θ_QCD ∈ {0, π}`. **Not a solution:** (i) the
CP-evenness hypothesis is undischarged — a single `T(2,9)` gluon knot has
writhe `9 ≠ 0`, so it needs a colour-singlet writhe cancellation over the
`9 = 3×3` tube structure, which needs the open SU(3) sector; (ii) `{0, π}` is a
discrete ceiling, not the observed `|θ_QCD| < 10⁻¹⁰` smallness.

### 3.6 Neutrino sector (7)

| # | Parameter | Tier | Status |
|---|---|---|---|
| 20–22 | `m_ν₁`, `m_ν₂`, `m_ν₃` | **open** | carrier identified (`def:neutrino-knot` = unknot, antineutrino = mirror). `Vol = 0` ⇒ zero mass at leading order — consistent with near-masslessness but **supplies no mechanism** for the nonzero masses oscillation requires. Volume–density route **scope-(b) excluded** (#4589, ~10¹⁰ gap) |
| 23–25 | `θ₁₂`, `θ₂₃`, `θ₁₃` (PMNS) | **open** | same structural reason as CKM |
| 26 | `δ_CP` (PMNS) | **open** | — |

Dirac vs Majorana is not distinguished; on a Majorana reading two further
phases join and are equally open. **The generation-counting problem is prior to
every parameter in this table** — see §5.

---

## 4. The three objects that gate everything (the useful synthesis)

The 21 open parameters are not 21 problems. Tracing every blocker backward,
they funnel into three missing objects. This is the single most actionable
content in this file.

### 4-A. A three-dimensional flavour object — "the `N = 3` problem"

**Gates:** every quark row, every `Y` value, the meson octet, the entire baryon
decuplet, all inter-multiplet mass splittings, the `η'`, all 4 CKM, all 4 PMNS,
`α_s`, `θ_QCD` smallness, `sin²θ_W` normalisation, `m_s`/`m_c` separation.

**State.** The obstruction is **proved** (`RowCapObstruction.lean`:
`dim V_{(1³)} = C(N,3) = 0 ⟺ N < 3`); the *construction* is missing. The
framework supplies `dim V = 2` and **no choice of `q` raises it** (Drinfeld–Jimbo
does not change dimensions).

**The live surface has collapsed to one question**
([`2026-08-07-eightfold-live-surface-collapse.md`](audits/2026-08-07-eightfold-live-surface-collapse.md)):

> **Does QOU's braided category admit inequivalent fibre functors?**

> **🛑 The "equivalently" that used to follow this was NOT equivalent — re-posed
> 2026-08-25.** The line read *"Equivalently: is `H¹(base, Aut^⊗)` non-trivial,
> and can the resulting gerbe's band be `SU(3)`?"*. That second sentence is
> **symmetric**-category machinery, and QOU's category is non-symmetric.
>
> The band / `H¹` formulation comes from classical Tannakian duality, which
> every source states under an explicit symmetric hypothesis: Tonini
> (`arxiv-2010.12445v1` §1, `arxiv-1409.4073v1` §2) defines the structure as
> *"symmetric or **commutative**"*, and Nuiten–Toën (`arxiv-2508.03145v1`) say
> *"solely based on **symmetric** monoidal ∞-categories"*. Tonini attributes the
> band identification itself to **[DM82, Prop. 2.8 / Thm. 3.2]** — theorems
> **about `Rep G`**.
>
> So *"`Aut^⊗(τ) = SU(2)`, therefore the band is not `SU(3)`"* **assumes what
> this section is asking**. It is circular, not merely unlicensed.
>
> **QOU's non-symmetry is not a reading — it is proved.**
> `QOU.Eightfold.HeckeBraidingNonSymmetric.double_braiding_eq_one_iff`
> (sorry-free): an element satisfying the Hecke relation has `σ² = 1` **iff**
> `q² = 1`. Symmetry of a braiding *is* triviality of the double braiding, so at
> `q₀ ≈ 1.10998 > 1` the braiding is non-symmetric as a **consequence** of the
> Hecke relation, not as a stipulation
> (`QOU.Archimedean.HeckeBraidingSubstrateNonSymmetric`). The corpus already
> said so in prose — `qou-definition-intro.md`: *"the **non-symmetric** braiding
> provides a canonical well-ordering on the Hecke basis"* — and derives the
> arrow of time from it.
>
> **The question to ask instead.** The general non-symmetric reconstruction
> (Lentner–Mombelli, `arxiv-2311.14221v2` §6.4) produces a **Hopf algebra in
> `C`** via a relative coend, not a group scheme with a band. So: *what is the
> reconstructed Hopf algebra of a QOU, and does it contain an `SU(3)`-like
> sub-object?*
>
> **This is a re-posing, not an exclusion.** It does **not** say `SU(3)` is
> absent — it says `H¹(base, Aut^⊗)` cannot carry the answer either way. The
> seven exclusions below are untouched and were separately provenance-audited
> the same day.
> [`2026-08-25-4a-question-imports-symmetric-theory.md`](audits/2026-08-25-4a-question-imports-symmetric-theory.md).

Routes already **excluded** (scope-(b), invariants cited — do not re-attack
without dropping a named premise):

| Route | Exclusion |
|---|---|
| Odd-dimensional summand of `V^⊗n` | Frobenius–Schur **parity**: odd-dim `SU(2)` irreps are orthogonal ⇒ singlet lands in `Sym²` ⇒ fails the gate. (Even-dim summands *pass* — they are simply the wrong dimension. The exclusion is parity, **not** self-duality; §6 of that audit corrects an earlier misstatement) |
| `S₄`/Fano bridge → Klein quartic | marked-pair obstruction: `S₄` has no orbit of size ≤ 2 on `ℙ²`; and the `S₄`-invariant quartics form an **infinite pencil**, so the datum has essentially no separating power |
| "4-form degenerates" → `Spin(7)` → `G₂` → `SU(3)` | no open `GL(8)`-orbit on `Λ⁴(ℝ⁸)`; Cayley locus is codim 27 |
| Re-tune the Ocneanu parameter to `N = 3` | the `N=2` and `N=3` traces are not proportional — and **not only those two**: `[n+1]_q[n+3]_q − [n]_q[n+4]_q = [3]_q` for **every** `n`, with an `n`-independent right-hand side, so *every* adjacent `N` re-weights and by the same amount (`QOU.Eightfold.OcneanuTwoThreeNotProportional.qb_shift_identity`, `QOU.Archimedean.OcneanuTwoThreeSubstrate.ocneanu_ratio_adjacent_ne`, sorry-free). Widened 2026-08-25: the recorded reason was a finite sample (*"differs at every `q` tested"*), now an identity |
| Permutation `S₃ = W(A₂)` 3-dim rep | permutation reps are self-dual with FS `+1` ⇒ fails the same gate. `S₃` supplies the **Weyl group**, not the fundamental |
| Hecke centralizer on regular `H₃` | dim 6 < 8 exclusion (#4564) |
| Tetraplectic / quaternionic | supplies `SU(2)`, already spent on electroweak |

> **🛑 The "surviving direction" below is ANSWERED, and the answer does not
> help (2026-09-03, PR #6458, bean `qou-yjwg`).** *Inequivalent fibre functors
> exist* — Bichon 2003 classifies them on `Rep(SL_q(2))`: one at every
> dimension `n ≥ 2`, real at `q₀` (`E ∈ GL_n`, `tr(E⁻¹Eᵗ) = −q − q⁻¹`). But a
> fibre functor is monoidal and preserves the fusion rules, so under a 3-dim
> one `V^{⊗3} = 21 + 3 + 3`, never `10 + 8 + 8 + 1`; the singlet is absent by
> Clebsch–Gordan parity (`FibreFunctorDimensionNotCategorical.lean`,
> sorry-free). Scope-(b): the fibre-functor route is closed; the missing object
> is in the **category** (`Λ³W ≠ 0`), which axiom 5 forbids for the
> fundamental. The 2026-08-25 "what is the reconstructed Hopf algebra?"
> re-posing was also already answered by `ex:tannaka-krein-su2`
> (`𝒪_q(SU(2))`) and does not bear on the multiplets, since every fibre
> functor's reconstruction gives an equivalent category. The `ℤ/2` lead below
> is thereby moot for the single-fibre category.
> [`2026-09-03-fibre-functors-do-not-change-the-category.md`](audits/2026-09-03-fibre-functors-do-not-change-the-category.md)

**Surviving direction:** the non-neutral Tannakian gerbe (`qou-y7vg`, T3g),
merged in scope with `qou-8p1i` (T3b). The sharp first question: *is
`Out(SU(3)) = ℤ/2` an obstruction to **every** gerbe route, or only to the
degree-3-extension one?* The framework carries its own `ℤ/2` (the bar
involution) — **record as an open lead, do not wire it**; "both are `ℤ/2`" is
exactly the coincidence the anti-laundering discipline exists to catch. A
refutation would be equally valuable: it would close the last live route, at
which point the honest corpus position is that colour and flavour `SU(3)` are
**imported**, and the chapters should say so plainly.

### 4-B. The two-like-charge EM-linking invariant

**Gates:** `m_d − m_u` (§3.1). The framework's only derived EM mechanism
(`tanh(ln q₀) × strong bond`) is **inter**-nucleon; the **intra**-nucleon
self-energy is the open object. Smallest scope of the three, and the only one
that yields a new comparable number without touching `SU(3)`.

> **🛑 "One invariant, two fronts" was wrong — corrected 2026-08-25.** This read
> *"Gates `m_d − m_u` **and** the remaining 69 % of the ³He mirror split. One
> invariant, two fronts."* Both halves fail.
>
> **The phrase covers two different objects.** For `m_d − m_u` the two like
> charges are the two up **quarks** inside one nucleon (**intra**-nucleon); for
> the mirror split they are the two **protons** of ³He (**inter**-nucleon). Both
> are "two like charges, linked", which is presumably how they merged.
>
> **They provably cannot be the same.**
> [`mirror_split_s3_em_functional_probe.py`](../computations/deltalambda/mirror_split_s3_em_functional_probe.py)
> §(A1) *derives* that per-component self-terms cancel identically in binding
> energy `B = Z·m_p + N·m_n − M`, because single-nucleon EM self-energy already
> lives in `m_p`, `m_n` — and `split_AME` is defined as `B(lo) − B(hi)`, a
> **binding** difference. So the intra-nucleon self-energy contributes **exactly
> zero** to the mirror split. Deriving one does **not** deliver the other.
>
> **The 69 % is unsourced.** Fixed-string grep over `docs/`: it occurred three
> times, all inside this file, and in no audit, ledger or witness. *(Corrected
> 2026-09-03: it also survived at line 145 of
> [`coordination/sm-26-parameter-chip-away.md`](coordination/sm-26-parameter-chip-away.md)
> — a line-scoped grep missed it because "mirror" sits on the next line. Struck there.)*
>
> **And the "cannot be the same" is itself partially reversed by channel
> (2026-08-30, `qou-bn8e` → `qou-o6ml`).** The self channel `A·Σqᵢ²` does *not*
> merge with the mirror front (it cancels in binding, exactly as above); the
> pairwise channel `B·Σqᵢqⱼ` *does*. Derived ratio on record: `h/[2]_q =
> tanh(ln q₀) = 0.10396371…`, so what 4-B owes is the bond that multiplies it,
> not a coupling. `ChargeQuadraticSumRule.lean` (sorry-free): the quadratic
> ansatz **saturates the octet** (bijection, det −1/3) — Coleman–Glashow could
> not have failed. (For scale,
> the `A=3` mirror ratio is `0.765`, so the residual against the canonical
> Coulomb is ≈ 23.5 % — the figure does not correspond to that either.) Both
> other occurrences are corrected with this one.
>
> Overloaded-symbol failure of the kind AGENTS.md flags in the `c_k` registry:
> *distinct objects sharing a glyph is a recurring root cause*.
> [`2026-08-25-4b-corrections-duplication-and-two-fronts.md`](audits/2026-08-25-4b-corrections-duplication-and-two-fronts.md).

> **State of the route, corrected 2026-08-25 (`qou-17mq`).** The route is
> identified — the metric Coulomb pairing `⟨A₁, J₂⟩` on the `H³` scalar Green's
> function — but the **kernel is not**, and the contest that appeared to have
> selected one does not support that reading. Its winner `H_coth` is scored on
> an *unsubtracted* `coth(α)`, which the same audit's own **O2** obstruction
> (finite-volume neutrality, `∫Δu = 0`) excludes: an admissible kernel has zero
> mean, hence takes both signs, so no admissible kernel saturates at `κ → +1` —
> and saturation is exactly what separated `H_coth` from its rivals. Its two
> rivals had already lost their warrant in round 5. So **no member of that
> contest carried a live structural warrant when it was scored.** Re-scored
> under the admissible family, scatter rises monotonically with neutralisation
> (3.5 % → 11.2 % → 22.3 %) and the best admissible member carries *more*
> residual structure than the hypothesis rejected for carrying structure.
> Do **not** cite hyperbolic-saturation as the selected mechanism. **Nor was
> the contest capable of selecting one:** the series spans `α ∈ [0.317, 0.873]`
> while `coth` reaches within 10 % of its limit only at `α = 1.522`, i.e.
> `A = 334` — past the heaviest known nuclide (`A = 294`). Saturation is
> unreachable in any nucleus, `coth` is within 0.97 % of `1/α + α/3` over the
> measured range against 3.505 % scatter, and the two hypotheses differ by at
> most 1.79 × that scatter. So **more AME data cannot settle it** — which was
> `qou-i6rg`'s stated premise. **And the separation law is itself imported:**
> `α ∝ A^{1/3}` is the Euclidean liquid-drop nuclear radius, fed into a kernel
> that is hyperbolic by construction; using the geometry consistently
> (`H³` volume growth gives `R ~ ½ ln V`, so `α ∝ ln A`) costs **2.64×** in
> fit. The corpus cannot adjudicate — it holds hyperbolic link volumes at
> `A = 2, 3` only. Deflationary but honest: `κ(A)` is close to plain Coulomb
> in a Euclidean nucleus (5.499 %), with the hyperbolic curvature term worth
> a factor 1.57 (→ 3.505 %) on one shared parameter — suggestive, not
> decisive. Rank 1 is unchanged: 4-B is still the smallest-scope gating
> object, but the front carries **three** distinct gaps, not one — the route
> is identified, the kernel is not, and the separation law is imported.
> [`2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md`](audits/2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md)

### 4-C. Content → hyperbolic braid map (retitled 2026-09-03; formerly "A third flavour grade (strangeness / charm Cartan)")

**Gates:** the charmed-hadron observable spectrum, `m_s`/`m_c`, the `D`-meson
mass, `Y = B + S` on strange states, and thereby `sin²θ_W`'s normalisation.

> **🛑 THE TITLE OF THIS ROW IS WRONG — no third flavour grade is missing
> (corrected 2026-08-25, `qou-17mq`).** `orderedContent_injective` is proved
> **sorry-free, `by decide`**, on `main`: `D̄⁰ (−5,+3)` and `K⁰ (+3,−5)` collide
> **only as multisets**, and the ordering is the quark/antiquark strand
> orientation — the same `signedWrithe` datum that gives `T₃`, *"topological
> strand-orientation data, not a fit"* per its own docstring. The arity slip:
> `mass_from_graded_content_cannot_separate` quantifies over
> `f : Multiset ℤ → ℚ`, i.e. **symmetric** functions of the *unordered*
> content; it does not say the content cannot carry the mass, and the ordered
> complement is injective. **So 4-C does NOT reduce into 4-A** — that
> dependency, the load-bearing claim of the sentence below, is not there.
> What remains is `qou-qpj9`'s Obstruction A: a canonical, parameter-free map
> from the ordered content to a hyperbolic braid word at `H₃(q)` — geometric,
> and needing no `SU(3)`, flavour or colour. **Not** thereby solved:
> injectivity gives a factorisation, never a derivation of the factorising
> map, and fitting through five injectively-labelled points is the per-state
> fit the J/ψ attack already recorded as worthless.
> [`2026-08-25-4c-no-third-flavour-grade-is-missing.md`](audits/2026-08-25-4c-no-third-flavour-grade-is-missing.md)

**State — partly derived.** `(n, T₃)` separates all six quarks (§3.2,
sorry-free), but the symmetric-multiset content **collides** `D̄⁰{c̄,u}` with
`K⁰{d̄,s}`. `mass_from_graded_content_cannot_separate` is proved for symmetric
`f`. ~~The missing grade is the **flavour** `SU(3)` Cartan — distinct from the
excluded **colour** `SU(3)` (#4564, gauge). So 4-C reduces into 4-A, but with a
much more concrete target.~~ **Struck 2026-08-25** — see the banner above; the
ordered content is injective, so no grade is missing and the 4-A dependency
does not hold.

Second blocker on the same front: the **canonical meson flux-tube braid word**
(`qou-qpj9`) — resolved to an honest negative (#4614): the Y-junction 3→2
reduction gives `B₂` (abelian) → torus link → `Vol = 0`, scope-(b),
SnapPy-verified. Strand *removal* cannot build hyperbolic structure.

---

## 5. The eightfold way, part by part

The classical eightfold way is not one object. Here is every part, with the
framework's coverage. **The chapter covers 2 of the 4 classical multiplets and
none of the programme's quantitative successes.**

| Eightfold-way part | Block | Tier | Note |
|---|---|---|---|
| `A₂` root system from 3 strands | [`a2-from-three-strands`](../content/quantum-observable-universe/eightfold-way/a2-from-three-strands.md) | **standard** | true *by construction* (`B_n` has type `A_{n−1}`); the block says "nothing about the substrate is derived from it". An earlier claim to derive the Cartan matrix from a counting formula is **withdrawn** |
| `q`-deformation of the weight lattice | [`q-deformation-weight-lattice`](../content/quantum-observable-universe/eightfold-way/q-deformation-weight-lattice.md) | **standard** + 1 **proved** | Drinfeld–Jimbo `q`-independence is standard, not formalised. `WeylInvarianceQDeformation.lean` proves the "two 2s" separation (`[2]_q` moves with `q`; Cartan `a_ii = 2` does not) — the formal statement of why this layer carries **no L2 precision leverage** (consistent with refuted-class C20) |
| Quantum Schur–Weyl duality | [`schur-weyl-eightfold`](../content/quantum-observable-universe/eightfold-way/schur-weyl-eightfold.md) | **standard** | duality itself not formalised; only its row-cap consequence |
| `N = 2` cannot host the decomposition | `RowCapObstruction.lean` | **proved-neg** | ⚠ **tier caveat** — see §6 |
| **Meson octet** (0⁻): `3 ⊗ 3̄ = 8 ⊕ 1` | [`meson-octet-decomposition`](../content/quantum-observable-universe/eightfold-way/meson-octet-decomposition.md) | **standard**, conditional on `N=3` | the block calls it "a theorem of `SU(3)` representation theory" |
| **Baryon decuplet** (3/2⁺) | [`borromean-decuplet-derivation`](../content/quantum-observable-universe/eightfold-way/borromean-decuplet-derivation.md) | **standard**, conditional on `N=3` | "a *matching of dimensions and weights*, not a derivation". Brunnian-ness → Young-symmetriser selection **withdrawn** as a non-sequitur |
| **Baryon octet** (½⁺) | partial — [`u-spin-coleman-glashow`](../content/quantum-observable-universe/eightfold-way/u-spin-coleman-glashow.md) | **proved-neg** | **Partly closed 2026-08-15** — the octet now carries real content via the Coleman–Glashow null result. *(2026-09-03)* the decomposition block **exists**: [`baryon-octet-decomposition`](../content/quantum-observable-universe/eightfold-way/baryon-octet-decomposition.md), `prop:baryon-octet-decomposition`, backed by sorry-free `OctetWeightDegeneracy.lean`, and it is content-bearing — the octet weight map is non-injective (`Λ`, `Σ⁰` both at `(0,0)`), so any weight-only mass formula predicts `m_Λ = m_Σ⁰`, refuted by 77 MeV (scope-b). `borromean-decuplet-derivation.md` now redirects to it |
| **Vector meson nonet** (1⁻) | [`vector-meson-nonet`](../content/quantum-observable-universe/eightfold-way/vector-meson-nonet.md) | **open — and the one content-bearing target** | **CLOSED 2026-08-14.** The mixing is **unconstrained** by the first-order octet ansatz (`NonetMixingUnconstrained.lean`, sorry-free): with the GMO-fixed `m₈` held fixed, *any* spectrum is realisable. So unlike GMO and equal spacing it is **not** automatic. Two nonets, identical `SU(3)` content, opposite mixing: `φ` is **99.5 %** `ss̄` (ideal), `η′` only **50.3 %**. Not currently attemptable — the singlet needs `N = 3` |
| Gell-Mann–Nishijima `Q = I₃ + Y/2` | [`flavor-charge-assignments`](../content/quantum-observable-universe/eightfold-way/flavor-charge-assignments.md) + `WeakIsospinT3Grading.lean` | **derived** (`I₃` side) / **open** (`Y` side) | see §3.2 for the closure's true width |
| `I₃` on the nucleon doublet | [`flavor-charge-assignments`](../content/quantum-observable-universe/eightfold-way/flavor-charge-assignments.md) | **derived** | **the one derived entry** — see §7 |
| Hypercharge `Y` | — | **open** | writhe map **falsified** (`p`, `n` share `Y = +1`, writhes differ). Candidates: strand twist (§6), Milnor `μ̄₁₂₃` (#4597) |
| GMO mass formula `4m_K² = 3m_η² + m_π²` | [`meson-mass-splitting`](../content/quantum-observable-universe/eightfold-way/meson-mass-splitting.md), `GellMannOkuboIdentity.lean` | **proved-neg** | holds **identically** for *any* first-order octet breaking ⇒ **zero discriminating power**. Reproducing it is evidence for nothing. GMO **withdrawn as a derivation target** |
| The GMO **deviation** (≈ 6 %) | — | **open** | the only testable content. Framework derives no second-order term ⇒ predicts **0** |
| **Decuplet equal-spacing rule + the `Ω⁻` mass prediction** | [`decuplet-equal-spacing`](../content/quantum-observable-universe/eightfold-way/decuplet-equal-spacing.md) | **proved-neg** | **CLOSED 2026-08-14** — the rule is an identity of first-order octet breaking, so it has **zero discriminating power**, same as GMO. `m(Ω) = 2m(Ξ*) − m(Σ*)` identically, so the Ω⁻ extrapolation reads off a value the ansatz already fixed. Cause: on the decuplet `2I = Y + 2`, collapsing the quadratic Casimir term to linear — and this **fails on the octet** (Σ, Λ share `Y = 0`), so it is not generic. Testable content relocated to the **≈ 9.2 %** spacing spread; framework predicts 0. `DecupletEqualSpacing.lean`, sorry-free |
| **U-spin / V-spin + Coleman–Glashow** | [`u-spin-coleman-glashow`](../content/quantum-observable-universe/eightfold-way/u-spin-coleman-glashow.md) | **proved-neg** | **CLOSED 2026-08-15.** The "likely the same null-result class" guess recorded here was **checked, not assumed** — and it holds: CG vanishes identically for all **six** first-order parameters (`ColemanGlashowIdentity.lean`, sorry-free). Mechanism: the octet's three U-spin multiplets each sit at fixed `Q`, so the alternating sum cancels every parameter. **One real difference from the other two nulls** — CG rests on a *conjunction* (isospin-exact strong ∧ U-spin-scalar EM), and dropping the second makes the combination nonzero, so it does test those two premises. Residual `−0.064` MeV ≈ **0.8 %** — the *tightest* of the three, hence the hardest second-order target. V-spin yields no independent octet relation |
| **Coleman–Glashow relation** | ✗ **no block** | — | coverage gap; zero mentions |
| Colour `SU(3)` from octonionic `G₂` | [`color-su3-from-g2`](../content/quantum-observable-universe/eightfold-way/color-su3-from-g2.md) | **standard** skeleton + **proved-neg** | `PSL(2,7) ≅ GL(3,𝔽₂)` machine-verified. The `S₄` bridge is **refuted** and the Bring→Klein degeneration **excluded**; `S₄ ⊂ PSL(2,7)` maximality as *selection* is **withdrawn**. Continuous `G₂` completion is a **Mathlib gap** (infrastructure, not structural). *(2026-09-03)* `𝕆` is now defined in-paper ([`octonion-algebra`](../content/quantum-observable-universe/eightfold-way/octonion-algebra.md), 2026-08-29, `qou-7arp`). The `λ_a ↔ e_a` generator-identification route to octonionic `SU(3)` is scope-(b) excluded (`OctonionicSu3RankObstruction.lean`: dim 8 → 7 non-injective; Cartan collapses to rank 1); only the stabiliser route survives |
| Flavour vs colour `SU(3)` | — | **open** | *(2026-09-03)* the "cannot both come from one construction" claim is **withdrawn** in-paper (2026-08-26): the premise compared two different objects, and `T₁` fails the gate because it is *real*, not because it is icosahedral. Strengthened to a proved blindness — **no object-level gate separates the two triples** (`FlavourColourDiscriminator.lean`: `no_object_gate_separates`); the discriminator lives in the Young-symmetry channel, and the colour-antisymmetry input is *located* in `μ̄₁₂₃` (sign rep of `S₃`, established) but the state's channel being `(1³)` is not established. On the Brunnian configuration `Λ³` is the only non-empty channel (`BrunnianIsotypeExclusion.lean`) |
| Spin–flavour–colour selection rule | — | **open** | neither the spin factor nor colour antisymmetry is derived |
| Truncation / "freeze-out" | — | **open** | heuristic; every use of the phrase is a label for the gap |
| Three generations | — | **open** | ⚠ tier caveat — see §6 |
| Ocneanu trace parameter `z` | — | **open** | whether `z` is extracted from categorical data or chosen |

**Chapter self-assessment, and it is accurate:** the chapter contributes *"the
placement of the braid dictionary against that classification, one derived
entry (`I₃` on the nucleon doublet), and a sharpened statement of what is
missing."* If anything it is **stingy on the negatives** — five self-withdrawals
and several proved negatives are a larger contribution than the one derived
entry, and the intro does not count them.

> ### Deleting false evidence is the dominant mode of contribution here
>
> Five withdrawals + three proved negatives + two machine-verified refutations,
> against one derived entry. A reader asking "what do these derivations give
> us" should be told that **first**. Removing GMO as a target is worth more
> than most positive results would have been, because it stops a
> zero-information success from being counted as one.

---

## 6. Guardrails — recurring over-claims, with the correct phrasing

These are live or recently-live. Each has a bean. *(Corrected 2026-09-03: this
read "none of the four 2026-08-08 findings was `completed` as of 2026-08-14";
all four — `qou-xu5t`, `qou-b4lo`, `qou-a5os`, `qou-cy2h` — completed on
2026-08-14/15.)*

| # | Over-claim | Correct phrasing | Bean |
|---|---|---|---|
| G1 | *"4 of 10,000 strand-twist assignments survive; `u`, `e` multisets uniquely determined"* | **Zero selectivity.** The constraint `T = 3Q` **factorises per flavour**; the survivors are `1 × 2 × 2 × 1`. The `10⁴` is the *unconstrained* product, so the ratio reads as ~2500× filtering where there is none. `u` and `e` are unique only because `T = +2` and `T = −3` each admit one multiset of three draws from `{−1,0,+1}` — a composition fact, not a framework fact. `TwistBatteryVacuity.lean` proves the battery is *exactly* `T = 3Q` and the `ℤ₆` condition never sees the assignment. **Drained 3 of 3** *(corrected 2026-09-03 — this row said 2 of 3 with `sm-open-problems.md:11` still carrying the original wording; that site was fixed by 2026-08-19, hash-verified against its sidecar)* | `qou-xu5t` ✅ |
| G2 | `RowCapObstruction` tiered *"the obstruction is **proved** … not an observation but a theorem"* | Same construction as `Sym2Gate` and `WeylInvarianceQDeformation`, which **both** get the arithmetic-vs-rep-theory caveat. Every proof in the file is `Nat.choose` arithmetic; the rep theory is carried by `def` names and docstrings. The chapter knows the rule and applies it in 2 of 3 places — omitting it at the one place where it is load-bearing | `qou-b4lo` |
| G3 | Three generations tiered *"partially derived"* from `{3,5,7,9} \ {9}` | Three is obtained by **removing one element from a four-element set**, on a criterion (continuant harmonicity) unrelated to generation counting. Any criterion eliminating exactly one of four yields "three". The row's own status says the physical bridge is open. Accurate tier: **`open`, with an adjacent proved divisibility lemma** | `qou-a5os` |
| G4 | `a5` orbital fracture *"falsifiable in principle"* | Unaddressed against **exact free-atom `f`-shell degeneracy**: free-atom states are labelled by `J` with `2J+1` exact by rotational invariance, and observed lifting is spin–orbit in a `J` pattern, not a `3' ⊕ 4` seam. Either already in tension with spectra, or below all resolution — in which case *untestable*, not falsifiable. (Referee objection, not a computed bound.) Also: this block and `cal2-higgs-knot-coupling` have **no `.qa.json` sidecar**, so they are invisible to every per-block checker | `qou-cy2h` |
| G5 | *"GMN proved for all six quarks"* | Collapses to **two** distinct arithmetic rows — see §3.2. **Now machine-checked** (2026-08-15): `gmn_check_has_two_distinct_rows` + `gmn_data_factors_through_weakType` prove the collapse, and `genWinding_finer_than_gmn_data` proves the relation is blind to the generation, so the wide phrasing cannot recur unnoticed | `qou-8z5j` ✅ |
| G6 | Citing the Weinberg **0.127 %** as an accuracy result | **Still a live guardrail** — but now stated in-paper (2026-08-14). It is the residual after picking the best of **74** swept candidates, and the witness itself records the ansatz as neither supported at `10⁻³` nor falsified at `10⁻²` (`path_c_status: inconclusive`). See §3.3 | `qou-s2pl` ✅ |
| G7 | Quoting the 2026-08-08 audit's *"1 derived"* as a corpus figure | It is a **two-chapter** figure. See §1 | — |
| G9 | Presenting an order-zero-only construction (leading term, single crossing, first-order ansatz) as a derivation of an SM parameter | **Owner ruling 2026-09-03:** derivations must be carried on the **full tower**; only the order-zero rendering is observable. Say the tower status (FULL-TOWER / ORDER-ZERO-ONLY / MIXED) beside every SM claim; an order-zero-only residual is not evidence about the tower. Reading confirmed by the owner the same day — both: all `n` of the Hecke tower and all orders in `q`: [`audits/2026-09-03-sm-26-term-status.md` §10](audits/2026-09-03-sm-26-term-status.md) | `qou-bsu0` |
| G8 | Citing colour-row proofs at `qou:QOU.StandardModel.ColourStabilizerAction` | The proofs are real but live in `QOU/MathlibExt/Octonion*` (9-module cone, verified `ok=9, err=0`). A reader following the `lean.ref` finds none of them | — |

> **`grep -c sorry` is unusable in this corpus.** Raw counts hit the phrase
> "sorry-free" in docstrings. Use word-bounded
> `grep -nE '(^|[^-[:alnum:]])sorry([^-[:alnum:]]|$)'`.

> **No fitted content has been found in either chapter.** To be explicit: no
> parameter is tuned to data anywhere in the 31 blocks, no hidden continuous
> DOF, and the anti-fit discipline is intact. The defects above are
> **presentation and tier**, which is a different and much smaller failure.

---

## 7. What is actually derived — the complete list

Three items, corpus-wide (not the two-chapter figure):

1. **`Q = w/2`, and `I₃` on the nucleon doublet.** The per-crossing coupling
   `c` in the framing phase `q^{w·c}` is **not free**: `c = 1/2`, structurally
   fixed by the pre-existing `def:coulomb-charge`. The history is what makes it
   non-trivial — an earlier session had `c = 1` missing `(m_n − m_p)/m_p` by
   ~305×, and the author flagged tuning `c` as a FIT; `c = 1/2` was then found
   **already in the corpus** rather than fitted. That is the anti-fit discipline
   working as designed, and it is the strongest single result on this surface.
   **Scope honestly:** the `I₃` *identification* is a two-point sign-and-ratio
   match on `{p, n}`. Prefer *"matches sign and ratio across the nucleon
   doublet, scale-free"* over bare *"derived"*, which invites the reading that
   `I₃` is output for general states.
2. **`T₃ = sign(κ)/2` as a grading orthogonal to the generation winding**
   (§3.2). Genuinely derived from an oriented crossing already present; the
   GMN closure is a real check at two-row width.
3. **`α_EM` to 0.313 ppb under the proton pin** (§3.3) — with three unproved
   classes, so `partial`, and with the anchor choice constituting the residual.

Everything else is `standard`, `proved-neg`, `conjectural`, or `open`.

---

## 8. Near-term derivable — ranked

Ordered by *(probability of closing) × (parameters unlocked) ÷ effort*. This
ranking is an agent's judgement, not a corpus fact; argue with it.

| Rank | Target | Why near-term | Blocker |
|---|---|---|---|
| 1 | **Two-like-charge EM-linking invariant** (4-B) | Smallest scope of the three gating objects; needs **no** `SU(3)`; stage-1 scoping already done and well-posed. ⚠ **The two-for-one rationale is withdrawn** (2026-08-25): this row read *"Closes `m_d − m_u` **and** 69 % of the ³He mirror residual together"*, and that is false — see the box under §4-B. The rank may still stand on the remaining grounds, but **not** on closing two fronts | intra-nucleon EM self-energy is genuinely underived. Two structural prunes landed 2026-08-25 (pairwise linking cannot see the Borromean carrier; the map must be **even** in `μ̄₁₂₃`), narrowing the shape but deriving no value. Per `qou-17mq` (merged above) the front carries **three** distinct gaps: the route is identified, the kernel is not, and the separation law is imported |
| 2 | **Content → hyperbolic braid map** (4-C; re-scoped 2026-08-25, heading retitled 2026-09-03 by #6458) | `(n, T₃)` separates all six quarks sorry-free, and `orderedContent_injective` (`by decide`) separates all five mesons — **no third flavour grade is missing**; the `D̄⁰`/`K⁰` collision is a symmetric-multiset artefact | `qou-qpj9` Obstruction A — geometric, and **not** gated on 4-A |
| ~~3~~ | **GMO deviation ≈ 6 %** — *(2026-09-03)* **drops from the ranking.** `GellMannOkuboSecondOrder.lean` (sorry-free, `qou-s4h6`): at second order the octet GMO combination is `16(4e − 3f)`, the decuplet `8(4e + 9f + 6g)`, equal spacing supplies no third constraint, and `g` is absorbable on both multiplets — **two equations, three unknowns**, so matching both deviations is a fit with a free parameter, not a prediction. `eightfold-open-problems.md` item 8 still calls a 6 % derivation "a genuine prediction" and needs the same correction | conditional on `N=3`; and now under-determined |
| 4 | **Non-neutral Tannakian gerbe** (4-A) | The whole eightfold surface has collapsed onto **one** question; seven routes are excluded with cited invariants, so the search is narrow | hardest of the three; a **refutation is equally valuable** and would settle the corpus position |
| 5 | **`α_EM` per-loop measure** | Would move the corpus's best number from `partial` toward closed | its own witness calls it *"highest-value but long-horizon conjectural close, not near-term"* — believe the witness |
| 6 | **`sin²θ_W`** | `μ̄₁₂₃` separates the two `U(1)`s (sorry-free) | relative `U(1)` normalisation inherits open `SU(3)`-flavour; **and** the 0.127 % / 64 % reconciliation (G6) should be settled first |
| — | **`θ_QCD` smallness, `α_s`, CKM, PMNS, `v`, `m_τ`, heavy-quark masses** | **not** near-term | all gate on 4-A, or have recorded negatives |

**Full-tower note (owner ruling 2026-09-03).** Every row in this table is an
order-zero attack as currently posed; under the ruling the *full-tower* version of
each step is the one that counts, and a row whose only formulation is order-zero
should say so. See G9.

**Formalize-first note.** Before any wide numerical search on this surface,
check §4's exclusion table. Seven `N=3` routes are already excluded with named
invariants — that table *is* the prune, and re-running a scan it covers is the
exact waste AGENTS.md §"Formalize-first probe discipline" exists to prevent.

---

## 9. Chapter organisation — measured, then proposed

### 9.1 The measurement that drives everything below

Section block-counts against the detangler's 3–18 band
([`local/detangler-integration-watcher`](../.claude/skills/local/detangler-integration-watcher.md)
Slot A):

| Chapter | Sections | Blocks | Blocks/section | In band |
|---|---:|---:|---:|---|
| `eightfold-way` | 8 | 11 → **16** *(2026-09-03)* | **1.4** → 2.0 | **0 of 8** |
| `appendix-standard-model` | 13 → **14** | 20 → **22** *(2026-09-03)* | **1.5** | **1 of 13** (`sec:sm-truncation`, 6); `sec:sm-results-surface` added |

**20 of 21 sections are below band.** This is the dominant structural fact
about both chapters, and it inverts the naive fix: the eightfold chapter's
problem is *not* too few blocks in too few places, it is **too many sections
for the blocks it has**. Any proposal that adds a section per missing multiplet
makes the measured defect worse.

> **Self-correction.** An earlier draft of this section proposed one new section
> per coverage gap (baryon octet, vector nonet, equal spacing, T₃ surface,
> octonion definition) — which would have taken the eightfold chapter to 13
> sections / 16 blocks, i.e. **1.2 blocks/section**, a *deeper* violation than
> the status quo. The measurement above is what caught it. The structure below
> is the band-aware replacement: same content, fewer sections.

### 9.2 Proposed eightfold structure — 4 sections, 18 blocks, all in band

Four movements: **setup → what is imported → what the braid adds → splittings
and open problems.** `◇` marks a new placeholder block (§9.4).

```
§1  The A₂ datum and its q-deformation                              [3 blocks]
      eightfold-intro
      a2-from-three-strands
      q-deformation-weight-lattice          ← moved up from old §6
    ▸ Why up: this is setup for every multiplet, and it carries the
      "no L2 precision leverage" statement. Sitting after the multiplets,
      it lets a reader meet q-deformed multiplets before learning the
      classification data is q-independent. Moving it up removes a
      genuine backward edge, not just a stylistic one.

§2  The eightfold classification (imported)                         [6 blocks]
      ◇ eightfold-imported-preamble
      schur-weyl-eightfold                  ← retier RowCapObstruction (G2) first
      meson-octet-decomposition                    (0⁻)
      ◇ baryon-octet-decomposition                 (½⁺)
      borromean-decuplet-derivation                (3/2⁺)
      ◇ vector-meson-nonet                         (1⁻)
    ▸ One part-level preamble states ONCE that everything here is standard
      SU(3) representation theory, conditional on N = 3, placed to show
      consistency and not derived. That retires ~6 in-block repetitions of
      the same disclaimer and makes the imported/contributed boundary
      visible in the table of contents — which is where the audit's main
      risk (mistaking volume of correct rep theory for framework support)
      is cheapest to address.
    ▸ All four multiplet blocks carry the §3b-cond banner form —
      "Proposition (conditional on N = 3)" — rather than a bare
      `proposition` kind (audit Finding 3).

§3  What the braid construction contributes                         [5 blocks]
      flavor-charge-assignments             ← the ONE derived entry
      ◇ weak-isospin-t3-grading             ← surfaces WeakIsospinT3Grading.lean
      color-su3-from-g2
      ◇ octonion-algebra                    ← def:𝕆 and G₂ = Aut(𝕆)
      dictionary-flavor-layer
    ▸ This section is the chapter's answer to "what do you actually add?".
      Keeping it separate from §2 is the whole point of the reorganisation.

§4  Mass splittings, the null results, and open problems            [4 blocks]
      meson-mass-splitting                  ← retitle to foreground the negative
      ◇ decuplet-equal-spacing                     (equal spacing + Ω⁻)
      ◇ u-spin-v-spin                              (U-spin, Coleman–Glashow)
      eightfold-open-problems               ← cross-ref §4-A's exclusion table
```

`meson-mass-splitting`'s current home is a section titled *"The meson octet via
tensor decomposition"*, which hides the chapter's second-strongest result — GMO
has zero discriminating power — inside a standard one. Retitle the block's
section, and the block, to lead with the null result.

### 9.3 Proposed appendix adjustment — leave the parameter sections alone

The appendix's **per-parameter chunk sections are correct and should not be
merged**, even though eight of them are single-block. They are a deliberate
navigation affordance: a reader looking up "what does the framework say about
the CKM angles" finds `sec:sm-params-ckm` in the table of contents. That is
exactly the class the detangler skill accepts as **`wontfix: architectural`**
(alongside the archimedean wall) — but it must be *recorded* as such in the
watcher ledger, not left as a silent band violation. Recording it is the ask.

The four **non-architectural** single-block sections should merge:

```
sec:sm-scope (1) + sec:sm-gauge-symmetry (2) + sec:sm-hecke-realization (1)
  ⇒ sec:sm-gauge-foundations                                       [4 blocks]
      sm-intro, gauge-action-groupoid,
      sm-lagrangian-selection-rules, gauge-hecke-realization

sec:sm-parameters (1) stays as the parameter-part preamble; the 8 chunk
  sections follow it unchanged, recorded wontfix: architectural.

sec:sm-open-problems (1) — merge the open ledger into the final parameter
  part, or keep standalone and record as architectural (a closing ledger is
  a legitimate one-block section). Author's call; state which.
```

Net: 13 sections → 10, with the 8 architectural ones explicitly flagged.

### 9.4 The placeholder blocks — what they are and what they must not be

Six new blocks, ranked by value:

| # | Block | Value | Why |
|---|---|---|---|
| ~~1~~ | ~~`vector-meson-nonet`~~ | **DONE 2026-08-14** | Landed. The mixing is proved unconstrained by the ansatz — the first eightfold-way quantity whose derivation would carry information. Measured: `φ` 99.5 % `ss̄` vs `η′` 50.3 %, witness `nonet-mixing-purity`. Still gated on `N = 3` |
| ~~2~~ | ~~`decuplet-equal-spacing`~~ | **DONE 2026-08-14** | Asked and settled: **automatic**, hence zero discriminating power, exactly as GMO. Block landed, Lean sorry-free, deviation (≈ 9.2 %) named as the real target. See [`2026-08-14-decuplet-equal-spacing-null-result.md`](audits/2026-08-14-decuplet-equal-spacing-null-result.md) |
| ~~3~~ | ~~`baryon-octet-decomposition`~~ | **DONE (by 2026-08-15; recorded 2026-09-03)** | Landed as `prop:baryon-octet-decomposition` with `OctetWeightDegeneracy.lean`; content-bearing (weight-only mass formulas force `m_Λ = m_Σ⁰`, refuted by 77 MeV) |
| 4 | `weak-isospin-t3-grading` | medium | The chapter has **no** presence for the T₃ result, though it is the second derived item on the surface. State the GMN closure at two-row width (G5) |
| ~~5~~ | ~~`octonion-algebra`~~ | **DONE 2026-08-29** (`qou-7arp`; recorded 2026-09-03) | Landed as `def:octonion-algebra`, first in `sec:color-algebra` |
| ~~6~~ | ~~`u-spin-v-spin`~~ | **DONE 2026-08-15** | Landed as `u-spin-coleman-glashow`. Ranked "low" here on the assumption it was another null; that assumption was checked and confirmed, but the *mechanism* (U-spin multiplets at fixed `Q`) and the conjunction-of-premises distinction were worth having explicitly |

> **A placeholder is a `prose` block, full stop.** It names the missing object,
> its tier, and its blocker. It is **never** a `theorem`/`proposition` with a
> vacuous body, never a `: True := trivial` Lean sibling, and never a
> `def`-disguised tautology (AGENTS.md §1a). Blocks 1–3 become `proposition`
> **only** when they carry real content, and then with the §3b-cond banner.

---

## 10. Consolidation plan for the SM results (detangle-sensitive)

The scatter measured in §1 is the thing to fix. **11 `.md` blocks outside the
two chapters carry SM/flavour content**, across five chapters:

| Chapter | Blocks | Examples |
|---|---:|---|
| `nuclear-interactions` | 3 | `weinberg-angle-categorical` |
| `mass-theory` | 3 | `complex-mass-constituent-functional`, `flavor-split-habiro-derivation` |
| `knots-particles-confinement` | 3 | `electroweak-higgs-torus-link-triplet`, the involution triplet pair |
| `observations` | 1 | `cp-violation-evidence` |
| `index-of-definitions` | 1 | index entry |

Plus Lean and compute that no chapter surfaces: `WeakIsospinT3Grading.lean`,
`MesonOperatorSelectionT3.lean`, `FormLadderAnchorDominance.lean`, the α_EM
form ladder, `quark-mass-extraction-stage1`.

### 10.1 The consolidation principle — surface, don't move

**Do not bulk-relocate blocks into the SM appendix.** Three reasons, all
detangler-grounded:

1. **Cross-chapter moves are the escalate-to-author class**, not the
   auto-discharge class. A 11-block cross-chapter migration is the single most
   disruptive operation the detangler recognises.
2. **The blocks are correctly placed for their *own* chapters' arguments.**
   `weinberg-angle-categorical` is used by the nuclear-interactions argument;
   `electroweak-higgs-torus-link-triplet` belongs with the knot–particle
   dictionary. Moving them creates **new backward edges** in the donor chapters
   — trading one defect for a worse one.
3. **The actual defect is not location, it is *discoverability*.** No reader of
   the SM appendix can find the T₃ result or the α_EM ladder. That is fixed by
   a reference surface, not by a move.

So: **consolidate the ledger, not the blocks.**

### 10.2 The plan — five phases, each independently landable

Ordered so every phase is useful alone and none blocks the next.

**Phase 1 — Drain the four standing 2026-08-08 findings.** (`qou-b4lo`,
`qou-xu5t`, `qou-a5os`, `qou-cy2h` — **all `completed` 2026-08-14/15**; this read
"all still `todo` six days on" until 2026-09-03. Phase 1 is done.)
Content edits only, no structure. Start with `qou-xu5t`'s **third site**
([`sm-open-problems.md:11`](../content/quantum-observable-universe/appendix-standard-model/sm-open-problems.md)),
which still carries the "4 of 10,000 … `u`, `e` multisets unique" wording after
the other two sites were fixed — the one materially misleading number in either
chapter, live on `main`. Each edit needs its `.qa.json` refreshed and the
render-QA gate run.
*Detangle impact: none. No `uses[]`, `kind`, `label` or manifest change.*

**Phase 2 — Close the three currency gaps.** Also content-only:
- ~~`sm-params-gauge-couplings` gains the α_EM ladder number~~ **done
  2026-08-14** with all three cautions (`qou-fmyd`);
- the α_EM witness's muon-anchored assertion strings are re-run under the
  proton default;
- ~~the Weinberg 0.127 % / 64 % reconciliation~~ **done 2026-08-14** — the block
  now scores the 74-candidate selection and cites the witness's own
  inconclusive verdict (`qou-s2pl`).
*Detangle impact: none. One witness re-run (long-compute logging discipline).*

**Phase 3 — Build the SM reference surface.** *This is the consolidation.*
**DONE 2026-08-30 (PR #5744, `qou-fqzs`; recorded 2026-09-03)** — both blocks
landed in `sec:sm-results-surface`. Caveat: `sm-gating-objects` landed carrying
the struck 4-C "third grade reduces into 4-A" claim; corrected on
`claude/standard-model-terms-status-ftoejr` (`qou-ok51`).
Two new blocks in the appendix, no moves:
- `sm-results-index` — a table of **every** SM-relevant result in the corpus
  with its home chapter, tier, and Lean/witness pointer. This is the in-paper
  twin of §1 + §7 of this file, and it is what makes the scattered results
  discoverable without relocating anything.
- `sm-gating-objects` — §4's three-object synthesis, in-paper. The most
  valuable single piece of structure on this surface and currently only in
  `docs/`.
Both go in the merged `sec:sm-gauge-foundations` or a new
`sec:sm-results-surface`; either keeps the section in band.
*Detangle impact: 2 new blocks, `uses[]` pointing **backward** to existing
blocks only — no forward edges. Update `docs/reorganization-map.md`.*

**Phase 4 — Eightfold restructure (§9.2).** The one phase that touches
manifests. Escalate to the author before landing: it is a section
merge/split, which the detangler routes to author-ask, not auto-discharge.
Land in two commits — (a) the section merge with existing blocks only,
(b) the six placeholder blocks — so the structural change is reviewable
independently of the new content.
*Detangle impact: 8 → 4 sections, 1.4 → 4.5 blocks/section, all in band.
Moving `q-deformation-weight-lattice` up removes a real backward edge.
`docs/reorganization-map.md` update is mandatory.*

**Phase 5 — Fill the two high-value placeholders.** `vector-meson-nonet` and
`decuplet-equal-spacing`. These are research, not editing — they are the only
two items in this plan that could *add falsifiable content*, and the
equal-spacing question (does reproducing it carry information, or is it
automatic like GMO?) is cheap and currently unasked.
*Detangle impact: 2 blocks into an in-band section.*

### 10.3 What this plan deliberately does NOT do

- **No `α_EM` / `T₃` block relocation.** Surfaced by Phase 3's index, left in
  place.
- **No merging of the 8 per-parameter sections.** Recorded `wontfix:
  architectural` instead (§9.3).
- **No new conjecture classes.** Every gap named here is already a
  content-bearing class with no instance, or an honest `open` row. Adding
  scaffolding would be motion, not progress.
- **No tier promotions.** Phases 1–3 *demote* or *qualify*; nothing in this
  plan moves a parameter up a tier, because no new derivation is claimed.

### 10.4 Sequencing note

Phases 1–3 are content-and-doc work with zero manifest risk and can run in
parallel with any sibling branch. Phase 4 is the only one needing coordination
— it touches `eightfold-way.ts`, so post intent on any sibling PR in eightfold
scope (`qou-8lxd`, `qou-vwu9`, `qou-8fl1`) before starting.

---

## 11. Maintenance

Update this file when any of the following change: a parameter's tier; a
gating object in §4; an exclusion in the §4-A table; an entry in §7; a
guardrail in §6 draining. Do **not** let it drift into a second source of
truth — every row must stay traceable to a block, Lean file, witness, or audit.
