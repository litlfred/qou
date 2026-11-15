# Work plan — updating the mass/binding compute

**Date:** 2026-08-25 · **PR:** [#5765](https://github.com/litlfred/qou/pull/5765) · **Bean:** `qou-9ot5`

Built from four measured audits run this session. Companion docs:
[staleness-vs-gap](../audits/2026-08-25-low-isotope-binding-error-staleness-vs-gap.md) ·
[cheat-sheet alignment](../audits/2026-08-25-cheat-sheet-paper-alignment.md).

---

## The finding that shapes the whole plan

**The live low-isotope dashboard cone is already CURRENT on all three owner rulings.**
Established by runtime trace (`builtins.open` + import interception over a real
`main(['7Li'])` run), not by grep:

- **Convention D** confirmed by arithmetic at **three independent points** — the
  `y_λ`-implied `z` recovered as `tr_M(σ₁) = y₍₂₎q − y₍₁,₁₎q⁻¹ = 0.612688037146465`
  (= `z_D` exactly; `y₍₁,₁,₁₎ = 0`, the D row-cap), the inline `z` in
  `borromean_binding_recompute`, and `closed_form_tau_M.markov_z`.
- **Proton pin** confirmed by tracing the manifest resolution and by the one witness's
  own `q0Anchor`.
- **`bring_color_weighted`** is the default and nothing in the cone overrides it.
- **Zero convention-C residue** in the cone (targeted AST grep for `sqrt(q)`, `q**0.5`,
  `q**(1/2)` over all 20 substantive cone files: nothing). **No muon leak** — the
  anchor-defining muon witness is never opened.
- Its single witness (`m-p-substrate-identity-50dps`) **reproduces byte-exactly** from
  live code: all 25 committed digits. `scriptHash` recorded == live.

**So "re-run the witnesses with convention D" is already done where it governs these
numbers.** The remaining error is not waiting on a migration.

**And the migration would not have helped.** Measured lever magnitudes against the
226 % rise needed at ⁴He: pin **128 ppb** (1.8 × 10⁷× too small — exact, since α enters
linearly), colour weighting **1.2 × 10⁻⁴** relative (1.8 × 10⁴×), writhe **zero** on
N = Z. Convention D is the largest lever, is already applied, and moved A ≥ 3 accuracy
**against** the target by 27–40 %.

**Staleness ≤ 10 % of the error, 0 % at ⁴He. ≥ 90 % is a missing term.**

---

## Tier 0 — Correct what is actively misleading (no compute, do first)

Nothing here changes a number. Everything here changes what a reader — or the next
agent — believes. Ordered by blast radius.

| # | Item | Evidence | Bean |
|---|---|---|---|
| 0.1 | **Cheat sheet `:41`: downgrade Step 2 from "✅ proved".** The Lean is `field_simp; ring` on a quadratic factorisation; the companion file *defines* the curvature 2-form to be the Hecke quadratic so flatness recovers it tautologically; the cited `prop:hecke-spectral-sequence` **does not exist**. This is the sole geometry→algebra bridge and steps 3–11 ride on it. | `HeckeStokesEigenvalues.lean:38-41`, `NaStokesKeystone.lean:22-25` | new |
| 0.2 | **Cheat sheet `:340`: STRICT violation.** Quotes `beats_100x_count = 2` / "2 of 7"; AGENTS.md forbids the bare figure. Live: `beats_100x_scoreable = 1`, `scoreable_total = 5`; unconditional **0/5** per the 2026-08-22 red team. Also fix the gap membership (m_p is `NOT SCORED`) and m_μ (211.2 ppb / 970.2×). | `per-observable-100x-status.witness.json` | new |
| 0.3 | **Cheat sheet `:48`: Step 9a is an anchor round-trip, not "🟢 settled".** the *ratio* `m_p,can/m_e = 1836.152673426000032` reproduces the CODATA anchor `1836.152673426` to **~1.7e-17** by construction (in MeV: **2.85 ppq**; **corrected 2026-08-25** — an earlier draft of this line said "CODATA to 40 digits", which is unverifiable since CODATA quotes only **11** significant digits for `m_e` and `m_p`, and the number it cited is in fact the −1.35 ppb de-fitted round-trip). `mba-step09a` and the live witness both say so honestly. Copy their wording. | recomputed 40 dps | new |
| 0.4 | **Cheat sheet `:500`: retract `Δ_λ = (q-Reeb phase density)_λ`.** Contradicts sorry-free general-n `dtEuler_eq_deltaLambda_unconditional` (`Δ_λ = (−1)^{n(λ)}·dim V_λ`). Keep the value/magnitude split the witness caveat states. | Lean + `delta-lambda-witness.json` | new |
| 0.5 | **Cheat sheet: convention C at `:221`, `:774`, `:783–787`.** `α_2 = z_C²` is listed under "NOT empirical fits" and is a **50 % error**. Do **not** substitute `z_D` into `:783` — half-integer powers of `q` mean that derivation must be **redone** (`qou-cds1`). | registry `:46` | `qou-cds1` |
| 0.6 | **Dead labels:** `prop:geom-universality` → `conj:` (`:107`, `:321`); `prop:hecke-spectral-sequence` (`:189`) does not exist; `prop:averaging-resonance-rule` → `thm:` (`:231`). The 2026-07-05 currency audit cleared all 14 by **stem**-grep; two do not resolve by label. | corpus-grep | new |
| 0.7 | **Live dashboard legend defects** (not just the committed file): `r₀ = 1.2 fm` is wrong — `coulomb_energy.R0_FM = 1.41381693076303648646` (`ℏc/m_π`, CAL-3, since 2026-08-09); "α_EM·ℏc … not fit" is wrong in the other direction (now *derived*, and conditional on an open Witten-κ `sorry` — `E_C` is tagged `DERIVED` with no conditionality marker); legend documents `B_gate`/`B_vol`/`B_lin` which the tables do not emit. | `coulomb_energy.py` | new |
| 0.8 | **The dashboard's legend asserts a manifest listing it does not have.** It claims the stem is "now declared explicitly as `physical_proton` … rather than relying on the 'not listed ⇒ proton' default". `mass_binding_dashboard` **does not appear** in `q0_anchor_manifest.json`. The resolution is correct; the claim about *how* is false — and load-bearing, since it is what would protect the numbers if `ideal_muon` were driven differently. Same for `canonical_mass`, `borromean_binding_recompute`, `coulomb_energy`. | manifest grep | new |
| 0.9 | **`mba-step09b` appendix contract is broken two ways.** Witness `dashboard_and_sweep_results.md` **does not exist** (`find` → 0); the alternate `canonical-mass-table-242ppb` has **no producer**, `computedAt: null`, `scriptHash: null`, and reports +3–6 % over-binding where the live pipeline under-binds 38–226 %. Its "Python API entry point" names `mass_binding_dashboard._row` for a `B_unified`/`CKRecursion` model whose symbols live in `probes/strong_unified_binding_probe.py`. AGENTS.md makes this appendix a mandatory sync target. | `qou-ahbz` | `qou-ahbz` |
| 0.10 | **`mba-step11` instructs *"`c_k` never reported as 'fitted'"*** while the authoritative registry classifies **c_4 as "EMPIRICAL — CODATA fit / artifact"**. An anti-fit-discipline inversion sitting in the paper. | registry §3 | new |
| 0.11 | **Registry is behind its own downstream block:** §1/§3 still call `c_2 = −1` *"proved, Taylor-exact"*; AGENTS.md retracted "proved" 2026-08-16 and `mba-step11` already carries the corrected wording. §3 also still carries `dc_3/dq ≈ 4.6×10⁶` (live **3.84e6**) — AGENTS.md said "five other sites", **≥19 measured**. | `qou-3nva` (re-scope) | `qou-3nva` |
| 0.12 | **Numeric corrections in the cheat sheet:** `:346` `η_0 = 0.1043407203` ⇒ ratio **0.8908357** (not 0.8913); `:358` `h = 0.2090602988`, `π·h = 0.6567823`, deviation **+0.50 %** not +0.26 % — **2× the advertised figure, in a table whose entire content is the size of that deviation**; `:198` `Δ(net) = −0.1872071945`; `:422` + `epistemic-status-of-calibrations.md:41` proton pin `0.06 → 0.017 ppb`; `:49` vs `:626` reconcile `Vol₄ = 8.05` against `8G = 7.3277`. | recomputed ≥40 dps | new |
| 0.13 | **The two committed root artifacts are stale by three superseded mechanisms and predate 2026-08-08**, dated by *arithmetic attribution* rather than by dates (shallow clone makes dates unusable). The committed header `pp=0.695 pn=0.534 nn=1.237` matches **z_C + Reeb-override-on-pn + no-writhe** exactly, 3/3; live `pp=0.607 pn=0.677 nn=0.790` matches **z_D + writhe + trace-pn** exactly. Independently corroborated by `E_C(³He)`: committed 1.00 = `r₀ = 1.2 fm`, live 0.85 = `λ̄_π`. Its flagship `err sym = 1.00` deuteron row is a property of the **removed** Reeb override; live is 0.79. Its validator line reads `max|Δ| = 1.7e+00 MeV` mislabelled "float64 noise" — 12 orders off; live `8.9e-16`. **Blast radius downstream: zero** — no content block and no audit cites them. Regenerate or delete both. | `qou-ql19` (itself carrying a superseded expected value) | `qou-ql19` |

---

## Tier 1 — R3 colour weighting: LARGELY SUPERSEDED by PR #5767

> **🛑 RE-SCOPED 2026-08-25 after coordinating with [#5767](https://github.com/litlfred/qou/pull/5767)
> ("Excise float64, convention C, and non-colour-weighted p/n").** That branch has already
> drained most of this tier and drove off-canon `pn_convention` baseline entries **8 → 6**.
> Most importantly it **answered item 1.4**, which I had marked *"ADJUDICATE, do not flip"*:
> `binding_canonical.py`'s convention line was the **symptom**, not the defect — its
> symbolic path had **no branch at all** for the weighted interface and fell through to
> `sp.nsimplify`, freezing a q₀ float into a rational. Leaving that line alone, as my
> caution implied, would have been the wrong call. Confirmed two ways on their side: the
> deuteron moves onto `qou-4e5k`'s bridge/peel value, and the closed-form and transfer
> paths now agree to 15 figures where they disagreed by 1.5e-4.
>
> **Check #5767 before starting anything below.** What is likely to survive is the
> witness regeneration (items 1.1–1.2) and the unregistered convention names (1.6).

### Original scoping (retained for the file lists)


Measured by **AST** walk (grep over-reports ~3× here — docstrings quote the other
conventions constantly). Defaults are already canonical (`closed_form_tau_M.py:245,344,392,495`,
`mass_at_3A_proper.py:435`). **10 off-canon call sites in 6 files; 5 live
non-comparison; 4 unjustified.**

| # | Item | Effect |
|---|---|---|
| 1.1 | `_habiro_coefficient_extract.py:175,208` (`chi_lambda_braid`, no stated reason — **the mass-table extract**) | regenerates **25** `habiro-coefficients-*` witnesses |
| 1.2 | `atomic_tr_m_helium4_canonical.py:117,123` + its comment calling `chi_lambda_braid` "the default" (**stale** — the default is now `bring_color_weighted`) | +1 witness |
| 1.3 | `closed_form_tau_M_verification_phase5q.py:168,173,174` | — |
| 1.4 | **`binding_canonical.py:295` — ADJUDICATE, do not flip.** Its `strict_averaged` deliberately matches the symbolic path's literal `σ − h/2` p-n factor; a blind flip changes the canonical binding producer's numbers. Fix its stale "default is `chi_lambda_braid`" comment either way. A file named *canonical* asserting a non-canonical convention is exactly what the owner-ruling audit predicted (`…:214`). | needs a call |
| 1.5 | `binding_combiner_markov_peel_fallback.py:134` — **blocked**, documented technical constraint: the exact-symbolic trace path can only carry the colour-blind averaged crossing. Leave labelled. | blocked |
| 1.6 | `binding-triangle-3body-cluster.witness.json` uses two **unregistered** convention names (`chi`, `bar-averaged`) | register or fix |

`binding_bring_enhancement_compare.py:69,70` calls both deliberately — **not a defect**.
(Bean `qou-cds4` says six files; the sixth is that comparison.)

---

## Tier 2 — R1 convention C: now **9**, and it is a FLOOR, not a queue

> **RE-MEASURED AGAIN 2026-08-25 after a second rebase — 11 → 9 actionable.**
> Independently confirmed by [#5767](https://github.com/litlfred/qou/pull/5767), which
> reports the same 9 on the merged tree. `main`'s audit has grown a
> **`BLOCKED on C by design (registry)`** bucket, which formalises the floor/queue
> distinction we both arrived at separately. Deliberate C-named comparisons: 50.
> **Item 2.7 (the 269-file `braid-registry` surface) is DONE** — #5767 took it and
> retired the directory to `fsh-guts/deprecated/computations/braid-registry/` with a README;
> confirmed present on this tree after rebase.
>
> Two details from #5767 worth keeping, neither of which I had:
> - **That `z` is not even convention C at a real anchor.** `z_C` at the proton pin is
>   `0.49932033418369445`; the registry recorded `0.4993200830735895`. It is C evaluated
>   at the **rounded `q = 1.11`** — neither pin.
> - **A false negative in the `deliberate` flag.**
>   `probes/markov_reduction_h3_to_h4_verify.py` declares in its own header that it is
>   deliberately left in C as the historical record a Lean docstring cites, with a live
>   both-conventions companion — and still counts as actionable.

> **🛑 RE-SCOPED 2026-08-25.** I listed the 11 as a drain queue. [#5767](https://github.com/litlfred/qou/pull/5767)
> independently measured **the same 11** and gives the reason it is a **floor**:
>
> - **9 sit in the qbeta/decay cone where a z-swap is invalid** — not merely unreviewed.
>   `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free) makes the C-frame ladder and
>   the mass channel's two-row forcing **mutually exclusive**. They need the S1
>   re-derivation (`qou-cds1`), which is **science, not drain**.
> - **1** is adjudicated in its own header as a deliberate historical record with a live
>   both-conventions companion.
> - **1** needs re-derivation of three C-specialised closed forms rather than substitution.
>
> So the migratable set is **2 live producers**, and the rest is blocked on `qou-cds1`.
> Two independent measurements agreeing on 11 by different routes is worth more than
> either alone. Their framing supersedes mine.

**Corrected counts** (AGENTS.md says 26; `--list --json` said **14**, and the
`tools/pyhecke/regime_scanner.py:94` site it calls "the last unexplained one" is
**closed**). `_li_2_q_util.py` is **migrated** — AGENTS.md's "lines 302 and 312,
load-bearing" is stale; only a historical comment survives at 330.

> **RE-MEASURED after rebasing onto `main` @ `5483aa95f` — now 11 actionable, not 14.**
> Five commits landed on `main` during this session and closed three of the fourteen:
> `a97d415bd` migrated `pauli_young` (a stale convention-C hand-copy), `b837f3a51`
> migrated `mirror_split eps_bonds` (a superseded convention-C *expansion*), and
> `3a58ca57b` registered `markov_reduction_h3_to_h4_verify::z` as **blocked on C by
> design** — which moves it out of the actionable set **without fixing it**. Deliberate
> C-named comparisons rose 47 → 49. **This count decays fast — re-run the detector rather
> than quoting any figure in this document.**

| # | Item | Count |
|---|---|---|
| 2.1 | **Live producers first:** `lepton_tower_core.py:126` (`markov_z`), `qbeta/qbeta_prearchimedean_z_recursion.py:103` | 2 |
| 2.2 | Probes / exploratory (**not exempt** — AGENTS.md 2026-08-18: a probe conclusion is an *argument* nothing re-derives). Two of the original twelve landed on `main` this session; one more is now registry-blocked rather than fixed | 12 → **9** |
| 2.3 | **`scripts/sync-qou-mass-vendor.py --apply`** — closes the 1 generated-mirror site **+ 23 drifted + 3 missing in one move**. Never hand-edit `_internal/`. Drifted includes all 21 `canonical-isotope-witness-Z*`; missing includes `closed_form_tau_M`, `y_lambda_wenzl_bridge`. | 1 command |
| 2.4 | **NEW DETECTOR BLINDNESS #14 — the Lean `⁻¹` spelling.** The 2026-08-19 Lean audit greped `Real.sqrt q + 1 / Real.sqrt q` and `√q + 1/√q`; the corpus also spells it `Real.sqrt q + (Real.sqrt q)⁻¹` — **13 hits in 9 files**, structurally invisible. Missed site: `QBetaCategoricalPrecisionLadder.lean:43`. | +1 site |
| 2.5 | **NEW DETECTOR BLINDNESS #15 — scope.** That audit walked `lean/QOU` only. **8 content-block sibling `.lean` files outside it carry a C shape** and were never in scope (`mass-theory/markov-trace-ratio-exact.lean`, `nuclear-interactions/q-beta-cos-resummation.lean`, …). | 8 files, **UNMEASURED** |
| 2.6 | 2 failing content blocks: `deuteron-fusion-frame` (`ts:35`), `interface-knot-markov-z-proof` (`md:56` ×2) + its Lean sibling `:118` | 2 |
| 2.7 | **NEW SURFACE — `computations/braid-registry/*.json`: 269 files, 268 carrying `z_markov = 0.4993200830735895` (C) and ZERO carrying z_D.** Worse, every one records `q = 1.11` — a *rounded* q that is neither pin, so it is off on **both R1 and R2**. Producer is `_deprecated/braid-registry.py`; **no runtime loader found**. **Recommend: move the directory under `_deprecated/`** (every detector skips it) rather than regenerate 268 files from a dead engine. | 268, disposition |
| 2.8 | Triage the **43 unexplained** z_C-carrying live artifacts (63 total, 20 self-evidently deliberate). Mass/binding-relevant: `alpha-k-jones-markov-h3/h4`, `confinement-operator-selection`, `hadron-knot-table`, `free-neutron-decay`, `beta-decay-matrix`, `deuteron-fpn-wlambda-wiring`, +5 under `deltalambda/`. **A floor, not a total** — beans `qou-mhij`/`qou-bvk7`/`qou-u5z0` record C propagating into payload that never *equals* `z_C`. | 43 |

**C-specialised closed forms — migrating `z` does NOT migrate the file.** The detector's
own note: `h·z+1` and `(q·z+1)/(q²+1)` are *rational* under D, so **a square root
surviving in one of them is `z_C` showing through**. Now **2** such bindings (was 4 —
`mirror_split_milnor_one_third_probe`'s three closed at `b837f3a51`):
`computations/probes/qbeta_5two_categorical_markov_volume_probe.py:133`
(`ocneanu_weights ← sqrt(_q)`), and the generated mirror
`qou-mass/src/qou_mass/_internal/_li_2_q_util.py:749`
(`borromean_markov_trace_h2 ← sqrt(q)`) which item 2.3 closes.

The structural/symbolic detector is down to **2 witnesses** (`derived-chi-catalogue`,
`y-lambda-macdonald-telescope`) from the 14 tranche H3 was scoped against.

---

## Tier 3 — R2 proton pin: the real backlog is stamping, not re-pinning

**The headline number in AGENTS.md is the wrong one to chase.** Re-measured with the
*three* live muon families (`constants.py:349-351` — a single prefix undercounts; my own
first pass gave 425 and missed the live-solve family):

| | all tracked | live (excl `_deprecated/`) |
|---|---:|---:|
| `*.witness.json` | 3088 | 2758 |
| **muon-bearing** | **480** | **264** (159 muon-only, 105 both) |

AGENTS.md says 870 (801/69). **Live is 264.** `ideal_muon` is **35 stems**, not ~72.

Fresh `q0_anchor_consistency_audit.py`:

```
Q0_OK 970   Q0_FLIP 0   Q0_ANCHOR_MISSING 1638   Q0_AMBIGUOUS_NO_REASON 14
```

- **`Q0_FLIP = 0`** — no witness self-contradicts its stamp. But this is **weaker than
  "computed at the anchor it claims"**, and the distinction matters for how the sweep is
  scored. The audit's own docstring defines the verdict as *"anchor ∈ {muon,proton} and
  `q0Value` matches that anchor's pin"* — it compares the two **recorded stamp fields to
  each other**, never against the constants the producer actually consumed. A producer
  that copies `constants.q_0` out of an **input witness** inherits whatever pin that input
  carried, is stamped from the manifest, and reports `Q0_OK` either way.

  > Verified from the primary source (`q0_anchor_consistency_audit.py` lines 12–13, 241 ff),
  > not from the sibling report that raised it. **The instance PR #5500 named
  > (`parabolic_cylinder_channel_mixing_probe`) is CLOSED on the current tree** — measured
  > this session, its witness stamps `proton` and its payload `constants.q_0 =
  > 1.1099785827513808076` is the proton value, and the stem is listed under
  > `physical_proton`. So cite the **mechanism**, which is live and general, not that
  > example, which is fixed. This is the AGENTS.md "a sibling's bean is not a primary
  > source" rule applied in both directions: the warning was right, its example was stale.

  Two consequences for sequencing:

  1. **`Q0_FLIP → 0` is not evidence a migration completed.** Report `Q0_ANCHOR_MISSING`
     beside it, always.
  2. **Regenerating can shrink the audited population rather than fix it.** PR #5500
     measured **seven** producers that stop emitting `q0Anchor`/`q0Value` when re-run —
     and those two fields *define* the muon-anchored set, so for those a re-run converts a
     `Q0_FLIP` into a `Q0_ANCHOR_MISSING`, which the audit's own docs call **"not a
     failure"**. Four such transitions already happened on `main` while #5500 was
     measuring. ⚠ UNVERIFIED here — I did not re-run those seven.

  The `qou-m9xp` class (a witness disagreeing with its own stamp) **is** closed. The
  broader claim — that every stamped witness was computed at its stamped pin — is **not
  established by this audit and cannot be**.
- **`Q0_ANCHOR_MISSING = 1638` IS the R2 backlog.** AGENTS.md rule 4 — *"Say which pin
  you used"* — is unmet for **53 %** of the corpus.

| # | Item |
|---|---|
| 3.1 | **Fix the generator, not the manifest** (`gen_q0_anchor_manifest.py`, `qou-khmj`). Manifest covers **700 of 3184** producers — 78 % undeclared. Hand-stamping 1638 witnesses is not the move. |
| 3.2 | **3 hard declared-proton/records-muon-only mismatches**, no comparison intent: `alpha-k-jones-markov-h4`, `binding-k-solver`, `rho-prefactor-structural-verifier`. Confirm by reading the producers (stem-matching is heuristic). |
| 3.3 | **Record the expanded must-stay-muon list in AGENTS.md — it names 4 of ≥ 11.** Additional confirmed: `q0_anchor_consistency_audit` (the flip detector itself, needs both), `aoperator_a5_crosscheck`, `habiro_interpolation_wlambda`, `qbeta_jacobi_anger_tower_general`, `rho_f_categorical_probe`, `lambda_scale_substrate_probe`, `m_p_borromean_verification_50dps`. Separately, **4 are legacy-default not must-stay** (`theta_jet_gb_grading_probe`, `lever1_binding_habiro_single_element_test`, `wlambda_q0_continuation`, `q1_mass_gap_probe`) and **13–15 have no muon rationale at all** — pure migration candidates, including `hadron_knot_table`, `binding_via_interface_knot`, `block_swap_binding`, `gram_norm_binding_probe`. |
| 3.4 | 14 `AMBIGUOUS_NO_REASON` + 3 `INDEPENDENT_NO_REASON` need one line each. |
| 3.5 | Manifest hygiene: `alpha_high_precision` (`ideal_muon`) and `binding_k_enumerator` (`physical_proton`) resolve **only** to `_deprecated/` files. |
| 3.6 | **⚠ 1600 witnesses carry no q₀ literal at all** — neither text method nor the canonical audit can say which pin they used. Neither clean nor dirty. **Unmeasurable until 3.1 lands**, which is why 3.1 outranks the 264. |

> **The muon-witness population is contested and both figures are moving.** PR #5500
> reports **56** muon-anchored witnesses carrying the old value where it earlier said 53,
> and its own author says *"53 should be re-measured before you act on it — `main` has
> moved several hundred commits since that count."* My independent measure over a
> different population (all `computations/**/*.witness.json`, three muon families) gives
> **264 live muon-bearing**. These are **not the same quantity** — #5500 counts witnesses
> stamped `muon` under its A→C re-pin; mine counts any witness carrying any muon literal —
> so they do not reconcile directly and neither supersedes the other. Do not merge the two
> numbers.

**Constraints on any sweep** (the 2026-08-19 authorisation carries four, each bought by
a failure): never re-pin an anchor-defining witness; the muon anchor keeps its
definition; comparison producers need both pins via per-process override; **do not split
the manifest change from the witnesses it re-pins**.

---

## Tier 4 — The gap (this is where the error actually is)

Ordered by cost, not by size of prize.

### 4.1 GAP-1 — the ²H per-bond defect. Cheapest real item on the board. `qou-5d6k`

`αL_pn = 2.833` vs `B_AME(²H) = 2.225`, **+27 %**. ²H is a *single* p–n bond with no
coordination topology — nothing else in the calculation can carry it. Under D the target
is **reachable**: the admissible interface band `[2.051, 3.798]` contains it. But the
**derived** colour weight gives `t = 0.499656` where `t = 0.119453` is required
(`qou-kj4v`). One fully-specified, parameter-free quantity, off by a factor whose source
is localised.

> The old `α ≤ 3.209 MeV` "α is too large" bound (`qou-qlma`, `bond_energy_floor`) is
> **convention-C scoped** — it rests on `z ≤ ½` via AM-GM, and `z_D = 0.6127 > ½`. The
> Lean file carries its own retraction. This is **not** an impossibility and **not** an
> α defect.

### 4.2 GAP-2 — the missing additive extensive term. `qou-ib3g`

Shape measured by extending the same chain to **A = 238**: `B_sym/A` is monotone and
**saturates at 2.998 MeV/nucleon** against nature's 8.790 peak. So
**R/A = (B_AME/A) − ≈3.0** — the residual *is* the nuclear binding curve minus a
constant, peaking at ⁵⁶Fe and falling.

`B_sym` is a pure saturating **volume** term at **2.93×** too small a coefficient
(**5.25×** against SEMF `a_V ≈ 15.75`), with **every other SEMF term absent** — the
model's B/A never turns over (no surface) and it carries no Coulomb.

Owned by: the Δ_λ **magnitude** leg (open — the *value* `(−1)^{n(λ)}·dim V_λ` is proved
and does **not** close this), the "separate additive extensive object"
(`2026-08-02-…-additive-term.md` §4, open), and `qou-v0yw` — which brackets everything
**except** ⁴He.

### 4.3 ⁴He is beyond any pairwise edge set — scope-(b)

Against the complete graph `K_A` (the **maximum** edge set), truth is bracketed for every
nucleus **except ⁴He**, which exceeds the maximum by **11.12 MeV = 39.3 % of its
binding**. In bond equivalents ⁴He needs **9.99 against a hard ceiling of C(4,2) = 6**.
Three independent estimates agree at **11–14 MeV**.

Invariant cited: the exact `K_A` Laplacian spectrum
`det_A(m) = (1+(A−1)m)(1−m)^{A−1}`. The ⁴He term is **irreducibly ≥ 3-body**.

The only *derived* thing here is the SU(4) `[1⁴]` locality gate
(`dim[1^A] = C(4,A)`, sorry-free) — it says **where** a 4-body term can live, not how
big. Every construct that reproduces the ⁴He *number* (`B_gate` 0.944, `B_vol` 0.933,
`B_magic` 0.944) is a **deprecated postdiction with a selected functional form**, and two
structurally unrelated ones land near the same ~8 MeV/nucleon — a numerology signature,
not corroboration.

### 4.4 Blockers that gate the gap work

- **`qou-cds2` — the Gram singularity under D** (H₃ corank 1, n=4 corank 10, n=5 corank
  78; `G_INV` computed at import so **all** consumers are affected). `qou-o3ta`: the
  metric blocker and the colour-weight blocker are **the same null vector, created by
  convention D**. Deepest item in the tranche.
- **`qou-cds1` — the `c_k` ladder under D.** Not a z-swap:
  `decayLadder_zC_threeRow_ne_zero` proves the C-ladder and three-row forcing are
  mutually exclusive. Every `c_k` fact stays **C-conditional** until this lands.
- **`qou-cds5`** — verify the `r*` D-frame band **before** re-scoring the six Δ_λ ansätze.
- **`qou-58sa`** — the muon anchor-defining witness is **0.85 ppb stale** (CODATA-2018
  baked in); blocks the C→D witness migrations.

---

## Tier 5 — Hygiene surfaced in passing

| # | Item |
|---|---|
| 5.1 | **`B_sym_exact` cannot test the claim made about it.** `_row` does `float(ta), float(tf)` before `math.log(tf/ta)`, so "chain ≡ exact trace **to the 50-dps floor**" is checked at the **f64** floor — the `8.9e-16` residual *is* that floor. The only non-circular check on the production chain is precision-capped three orders below what it claims to verify. |
| 5.2 | **NO-FLOAT64 in the m_p producer.** `m_p_substrate_identity_50dps` does `mpf(M_E_MEV)` where `M_E_MEV` is a Python `float` — 25 serialised digits on ~16 good ones. *Measured, not inferred*: matching `mpf(float)` rather than `mpf(str)` moved the replication by 1.7e-17 **onto** the committed digits. The dashboard's own `_constants()` avoids this via `mpf(str(me))`; the producer does not. |
| 5.3 | **`B_tetra` is unbacked** — no citation, no witness, no content block, no derivation anywhere; its own comment says only "to observe jet-order scaling". Computed **entirely in float64**. Correctly tagged `EXPLORATORY`, but it prints beside derived columns at 118× error. |
| 5.4 | **A non-physical degree of freedom.** `atom_braid_word_3A` hard-codes ordering `['p']*Z + ['n']*N`; a nucleus has no ordering. Spread over all orderings under D: ³H **5.6 %**, ⁴He 2.7 %, ⁷Li 2.9 %. Immaterial against 226 %, but `B_sym` should not be quoted to four digits as convention-free. |
| 5.5 | **Stale docstring names over correct arithmetic** (the AGENTS.md-warned pattern): `_li_2_q_util.load_q_50dps` says `z = 1/(q^{1/2}+q^{-1/2})` while returning D; `atom_braid_word_3A` says `flavor_split_subleading` while using `_leading`. Values right, names wrong. |
| 5.6 | **Arity flag against AGENTS.md.** It states the pairwise cap `ρ_A ≤ C(A,2)` is "proved in `exchangeDet_pow_two_le_four`", and `qou-i8oq` is **completed**. The file is `BindingSaturationCapA4.lean`; the theorem is `(1−m²)^6 ≤ (1+3m)(1−m)^3` — the **A = 4 instance only**. No general-A version in `content/`. Changes no conclusion here (A = 4 is the case that bites); re-scope or prove. |
| 5.7 | **The dashboard prints a 79-day-old Lean banner** (`quantum-observable-universe=FAIL(357err/7sorry)`) as though current. |

---

## Corrections this plan makes to AGENTS.md

Each was re-measured, with method stated in the source audits.

| AGENTS.md says | Measured |
|---|---|
| convention-C audit: **26 actionable** | **14** (2 live producers / 12 probes) |
| `_li_2_q_util.py` "carries the same C at 302 and 312, load-bearing" | **migrated**; only a historical comment at 330 |
| muon-pin witnesses **870** (801/69) | **264 live** (159/105); 480 including `_deprecated/` |
| `ideal_muon` "~72 producers" | **35 stems** |
| must-stay-muon = **4** producers | **≥ 11** |
| `qou-cds4`: 6 files / 28 witnesses | **5 live non-comparison** (10 sites) / **30** witnesses |
| Lean C surface = 5 sites | all 5 survive **+ ≥ 4 more**; two new detector blindnesses |
| `dc_3/dq` correction "five other sites" | **≥ 19**, the authoritative registry included |

---

## Sequencing

**Tier 0 first, and it is not optional.** It costs no compute and it is the difference
between a corpus that tells the next agent the truth and one that does not. Two items
there — the Step-2 "proved" label and the Step-9a "settled" label — are load-bearing
mislabels in the document AGENTS.md tells agents to read first.

**Then Tier 1** (two producers, 26 witnesses, mechanical) and **Tier 2.3**
(`sync-qou-mass-vendor --apply`, one command, closes 27 items).

**Then Tier 3.1** — the generator fix — because 1638 unstamped witnesses is a larger and
more tractable problem than the 264 muon-bearing ones, and it is what makes the 1600
no-literal population measurable at all.

**Tier 4 is the actual physics and does not depend on any of the above.** GAP-1 (²H) is
the cheapest genuine derivation item in the corpus right now: one bond, one parameter,
target inside the admissible band, discrepancy localised to a single derived weight.

**What no amount of Tier 0–3 will do is close the binding number.** That is Tier 4, it is
≥ 90 % of the error, and at ⁴He it is 100 % of it.
