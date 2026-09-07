# Owner ruling 2026-08-15 — convention D, proton pin, colour weighting (READ FIRST)

> **Notation note.** This document predates the 2026-09-05 calibration rename and uses
> the superseded symbols `𝔇_β` (CAL-2) and/or `𝔇_π` (CAL-3). Those are now
> `P_skew^β` (the bar-skew β-channel) and `P_avg^π` (the bar-even π-channel); the
> `𝔇` family is reserved for genuine decay rates (`𝔇_n`, `𝔇_μ`, `𝔇_K` = ℏ/τ).
> The analysis below is left as the record of what was analysed at the time.

**Date:** 2026-08-15 · **Status:** CANONICAL — owner adjudication, received
verbatim in session. · **Branch:** `claude/owner-ruling-convention-d-2026-08-15`

This is the **anti-flip-flop "read first"** record for the trace-convention,
q₀-pin, and p/n-weighting questions. It is a **recording and scoping** document.
It changes **no** number, **no** registry value, and **no** content block. Its
job is to make the ruling findable and to state the blast radius **before**
anything moves.

## 1. The ruling, verbatim

Two messages, in order:

> **"convention D is convention. excise convention C."**

> **"similarly, use proton pin and color wighting"** *(sic)*

Read as three canonical rulings:

| | ruling |
|---|---|
| **R1** | Convention **D** (`z = q³/(q²+1)`) is *the* trace convention. Convention **C** (`z = 1/(√q + 1/√q) = √q/(q+1)`) is **excised**. |
| **R2** | The **proton pin** (experimental / Physical-Observations anchor, `q₀ ≈ 1.1099785827513808`) is canonical. |
| **R3** | **Colour weighting** (`pn_convention="bring_color_weighted"`) is canonical. |

## 2. What this supersedes — and what it does *not*

### R1 is a re-affirmation that closes two surviving carve-outs

**The corpus was already here.** The [2026-08-09 owner
ruling](../coordination/trace-convention-registry.json) already said *"excise
convention C"*, and three of the four registered channels are `status: agreed`
on D. R1 does not open new work in those channels — it **closes the two places
where C survived by explicit exception**:

1. **The `qbeta-decay` channel, registered `disputed` earlier today (PR #5111,
   bean `qou-b3nk`).** Registry state before this ruling:
   `definitional_convention: null` (contradictory), `production_convention: "C"`,
   `status: "disputed"`. The registering audit
   ([`2026-08-15-qbeta-decay-channel-convention-disputed-registration.md`](2026-08-15-qbeta-decay-channel-convention-disputed-registration.md))
   was explicit that **neither** convention was *derived* for that channel and
   left the settlement to the owner. **This ruling is that settlement.** The
   channel goes `disputed` → `D`.

   The disputed registration is **superseded as a status, not as analysis.** Its
   Lean and its measurements stand and are load-bearing for the tranche plan
   below — in particular `decayLadder_zC_threeRow_ne_zero`, which proves the
   C-frame ladder and the two-row forcing are **mutually exclusive**. That
   theorem is precisely why R1 cannot be discharged by a z-swap in the decay
   channel (§4, Tranche S1).

2. **The one `owner_decision_required: true` in the registry.**
   `blocked_migrations[0]`: `tools/pyhecke/python/pyhecke/gram.py::z` **stays C
   by design**, because `G_INV = np.linalg.inv(G)` runs at module import and
   under D the Markov–Gram form on the `H₃(q)` NF basis is **exactly singular**
   (one null direction; `det 3.998e-17`, `cond 4.9e16`; numpy raises nothing and
   returns entries to `7.6e15` with `‖G·G_INV − I‖ = 1.64`). R1 removes the
   *convention* question; it does **not** remove the singularity. See §4,
   Tranche S2 — this one has a named repair (quotient by the radical,
   `QOU/QBeta/GramSignature.lean`) and is the highest-risk item in the plan.

### R2 extends the 2026-08-07 directive from "new compute" to "canonical"

The [2026-08-07 owner directive](../../AGENTS.md) already made the proton pin
the default for *new and touched* compute, while explicitly **not** authorising
a bulk rewrite of the muon-pinned witness layer (tracked, unfinished, under bean
`qou-1c4y`). R2 states the target end state as canonical. It does **not**, on its
own wording, authorise the bulk regeneration — that is a scoped decision, and the
measured size of it is in §3.4. The ideal-mathematical CAL-2 definition
(`𝔇_β`, proxy `m_μ/m_e`) is a *definition* and is untouched by a ruling about
which pin compute evaluates at.

### R3 is largely already true in production

`bring_color_weighted` is already the default in the production mass/binding
path (`closed_form_tau_M.py` ×4, `mass_at_3A_proper.py`). R3 makes it canonical
and puts the surviving alternatives (§3.5) on notice. It does **not** by itself
say the alternatives must be deleted — several are deliberate *comparisons*, and
a comparison against an excised convention is still legitimate provided it says
so.

## 3. Measured blast-radius inventory

**Everything in this section was measured on this tree, this session, with the
repo's own detectors where one exists.** Where a figure is relayed rather than
measured, it is marked. Counts quoted from AGENTS.md and from beans were
**re-measured**, and two of them were wrong — see §3.4 and §3.6.

### 3.1 Convention-C producer sites — `scripts/convention-c-producer-audit.py` (AST-verified)

| class | sites | files | note |
|---|---|---|---|
| **ACTIONABLE** (live C definitions, excl. blocked-by-design) | **0** | 0 | the producer layer is already fully D |
| blocked on C **by design** (registry) | **3** | 2 | `tools/pyhecke` — the `G_INV` singularity, §4 S2 |
| deliberately C-named (labelled comparisons) | **9** | — | history/comparison, not defects |
| **blocked-symbol leaks** | **13 modules** re-export + **13 downstream consumers** | 26 | the registry exempts the symbol *inside* its module; nothing kept it there |

The 13 re-exporting modules (all `[qou-wgta]`):

```
computations/confinement-operator-selection.py:30      pyhecke.gram.z -> _PG_Z
computations/gram-matrix-dual.py:40                    pyhecke.gram.z -> z
computations/h2o_angle_activeset_gb.py:40              pyhecke.gram.z -> z
computations/h2o_angle_gb_truncation_inverse.py:47     pyhecke.gram.z -> z
computations/h2o_bond_angle_magnitude_vsepr.py:61      pyhecke.gram.z -> z
computations/h2o_bond_angle_shift_phi1.py:70           pyhecke.gram.z -> z
computations/hecke_core_legacy.py:75                   pyhecke.gram.z -> z
computations/jet_knot_invariants.py:42                 pyhecke.gram.z -> z
computations/molecular-frobenius-lp.py:43              pyhecke.gram.z -> _PG_Z
computations/pn_alpha_lp_dual.py:60                    pyhecke.gram.z -> _PG_Z
computations/substrate/hecke_core.py:61                pyhecke.gram.z -> z
computations/vhat_per_crossing_chain.py:63             pyhecke.gram.z -> z
qou-mass/src/qou_mass/_internal/hecke_core.py:60       pyhecke.gram.z -> z
```

**Note the last line.** `qou-mass/src/qou_mass/_internal/` is **generated** by
[`scripts/sync-qou-mass-vendor.py`](../../scripts/sync-qou-mass-vendor.py) and
must never be hand-edited; it moves when its source moves.

### 3.2 Convention-C witnesses — `scripts/convention-c-witness-audit.py` (structural test)

The structural test is *"a witness recording a nonzero `y_λ` on a three-or-more-row
partition is convention C — at any `n`, whatever numbers it contains."* It
replaced a decimal-fingerprint test that structurally could not see `n > 3`.

| detection | witnesses | entries |
|---|---|---|
| **structural** (nonzero `y_λ`, `ℓ(λ) ≥ 3`) | **13** | 825 dead-block entries |
| **symbolic** (half-integer power of `q` in a weight expression) | **1** | 14 expressions |
| **total** | **14** | — |

```
computations/alpha/alpha-k-jones-markov-h12.witness.json              (70)
computations/chi-deuteron-h6-at-q0-50dps-matrix-m.witness.json         (7)
computations/chi-helium-3-h9-at-q0-50dps-matrix-m.witness.json        (25)
computations/chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json       (70)
computations/chi-helium-4-h12-numeric.witness.json                    (70)
computations/chi-lithium-5-h15-at-q0-50dps-matrix-m.witness.json     (168)
computations/chi-lithium-6-h18-at-q0-50dps-matrix-m.witness.json     (375)
computations/chi-neutron-h3-at-q0-50dps-matrix-m.witness.json          (1)
computations/chi-proton-h3-at-q0-50dps-matrix-m.witness.json           (1)
computations/chi-tritium-h9-at-q0-50dps-matrix-m.witness.json         (25)
computations/derived-chi-catalogue.witness.json                        (2)
computations/probe-1b-li6-orthogonality.witness.json                   (9)
computations/tr-m-q-hecke-seminormal.witness.json                      (2)
computations/y-lambda-macdonald-telescope.witness.json         (symbolic, 14)
```

**Six of these are the `chi-*-matrix-m` family, which no Python producer owns** —
bean `qou-eea0` resolved them to `producer: "rust-chi-q-via-gp-lossless"`, a
`hecke-engine` binary. That is the layer where bean `qou-j6il` found a binary
silently returning C while its source read D. They must not be regenerated until
the convention gate is applied to the binary. This is the reason Tranche H3 is
sequenced after a gate, not before.

### 3.3 Convention-C in the kernel-constraints registry

| location | C-marker occurrences |
|---|---|
| [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) | **16** |
| [`kernel-constraints-registry.json`](../coordination/kernel-constraints-registry.json) (JSON twin) | **5** |

The C-conditional items live in **§9g** (`ck-dk-canonical-registry.md:693`), whose
measured table is the science inventory for Tranche S1 — reproduced in §4.

### 3.4 q₀ pin in the committed witness layer

Fixed-string measurement over `computations/**/*.witness.json`:

| | count |
|---|---|
| total witnesses | **2941** |
| carrying the **muon** fingerprint `1.109978595` | **870** |
| carrying the **proton** fingerprint `1.1099785827` | **588** |
| carrying **both** | **69** |
| **muon-only** | **801** |
| proton-only | **519** |

> **AGENTS.md's "~840 muon-pinned witnesses" is low, not stale-high.** The
> measured figure is **870** (801 muon-only). The AGENTS.md sentence flagging
> the number as needing re-measurement was right to flag it; the direction of the
> error is the opposite of what a reader would assume from "stale".

The **69 witnesses carrying both pins** are the interesting set: a witness quoting
two pins is either a deliberate comparison or a **layer straddle** — the defect
class AGENTS.md names STRICT ("never straddle the two layers inside one
quantity"). They are not yet triaged. Tranche S3.

### 3.5 p/n convention

Live Python assignment sites (excluding `_deprecated/`):

| value | assignment sites |
|---|---|
| **`bring_color_weighted`** (canonical per R3) | **16** |
| `chi_lambda_braid` | **9** |
| `strict_averaged` | **6** |

83 files mention `pn_convention` in total (`.py` + `.json` + `.md`). The 8 live
Python files carrying a non-colour-weighted assignment:

```
computations/_habiro_coefficient_extract.py
computations/atomic_tr_m_helium4_canonical.py
computations/binding_bring_enhancement_compare.py      <- a deliberate comparison
computations/binding_canonical.py
computations/binding_combiner_markov_peel_fallback.py  <- PN_CONVENTION = "strict_averaged"
computations/chi_monotone_transfer.py
computations/closed_form_tau_M_verification_phase5q.py
computations/iterative_knot_builder.py
```

**28 committed witnesses** record a non-colour-weighted `pn_convention`.

Two of these are named `*_compare` / `*_fallback` and are plausibly legitimate
under R3 (a labelled comparison against a non-canonical convention is fine). The
other six need reading. **`binding_canonical.py` is the one to look at first** —
a file with `canonical` in its name assigning a non-canonical p/n convention is
either a naming defect or a real one.

### 3.6 Two corrections to figures quoted in the tasking

- **`z_C` hard-coding at `y_lambda_wenzl_bridge.py:122,140`** — the tasking gave
  these as live starting points. The producer audit reports **0 actionable**
  sites, and `y_lambda_wenzl_bridge.py` does not appear in its output. Bean
  `qou-eea0` records this producer as **already migrated** (it is `y-lambda-wenzl`'s
  producer, resolved and run in the regeneration cascade). Treat those line
  numbers as historical.
- **`qbeta_ck_sseries_exact_rational.py:20,248`** — these **are** live, and are
  registered as such in the `qbeta-decay` channel's `production_source`. They are
  the KC21/KC22 `D(ũ)`-ladder core. **Naming hazard, called out in the registry
  and repeated here: the `D` in "`D(ũ)`-ladder" is KC21's bar-even ℚ(√3) ladder
  *function* `D`, NOT convention D.** Those lines evaluate `z = √q/(q+1)`, i.e.
  `z_C`.

## 4. Tranche plan

Ordered. **hygiene** = mechanical, safe to batch, no number moves.
**SCIENCE** = restates a number or a conclusion; needs review before it lands.

The ordering constraint that matters: **producers read each other's witnesses**
(bean `qou-eea0`'s hardest-won lesson — a stale upstream witness propagates into
a freshly-migrated downstream producer and the downstream output looks clean).
Nothing in H3 may run before S1/S2 settle what the decay and Gram layers compute.

### Hygiene tranches

| # | tranche | scope | why hygiene |
|---|---|---|---|
| **H1** | Register the ruling | Flip `channels.qbeta-decay` `disputed` → `D` in `trace-convention-registry.json`; resolve `blocked_migrations[0].owner_decision_required` → answered; add the ruling to `meta`. Add the §9g / §9h supersession pointer. | Records an owner decision. Moves no computed value. **Must land first** — it is what makes every later tranche's convention unambiguous. |
| **H2** | Close the blocked-symbol leak | The **13 re-exporting modules + 13 consumers** of `pyhecke.gram.z` (§3.1). Contain the symbol to its module so the registry exemption means what it says. | Pure containment; the symbol's *value* does not change here. Blocked on **S2** deciding what `pyhecke.gram.z` becomes. |
| **H3** | Regenerate the 14 C witnesses | §3.2. Serial, never two producers concurrently, never hand-edit a number. | Mechanical **given** a settled convention — but see the two gates below. |
| **H4** | Convention-label hygiene | The 9 deliberately-C-named comparison sites + the C-marker occurrences in the two registries (§3.3) that are *history* rather than live claims. | Labelling only. Each must say "convention C (excised 2026-08-09/2026-08-15)". |

**Two gates on H3**, both from `qou-eea0`, both non-negotiable:

- **6 of the 14 are `chi-*-matrix-m`, produced by a Rust binary**, not Python.
  Bean `qou-j6il` found that layer silently returning C while its source read D.
  Apply the convention gate to the binary *before* regenerating.
- **`delta_lambda_2row_stratum_analysis.py` has never completed** — it consumed
  the full 2400 s timeout on every attempt and is first in topo order, so every
  cascade restart pays 40 minutes before producer 2. Diagnose or re-order before
  starting a cascade.

### SCIENCE tranches

| # | tranche | what moves | measured impact |
|---|---|---|---|
| **S1** | **The Q_β `c_k` ladder** | Everything in registry §9g. | **This is the big one — see the table below.** |
| **S2** | **`pyhecke.gram.z` and the Gram singularity** | `G_INV` at module import. | Under D the Markov–Gram form on `H₃(q)` is **exactly singular** (corank 1; `n=4` corank 10, `n=5` corank 78). numpy returns garbage silently. Repair is named — quotient by the radical, `QOU/QBeta/GramSignature.lean` — but `G_INV` is exported at import, so every consumer is affected. |
| **S3** | **The muon→proton witness migration** | 801 muon-only + 69 both-pin witnesses (§3.4). | Tracked under `qou-1c4y`. **Not authorised by R2's wording alone**; needs its own scoped sign-off. The 69 both-pin witnesses should be triaged for layer-straddle *first* — that is a defect regardless of the migration. |
| **S4** | **p/n convention** | 6 live non-comparison files + 28 witnesses (§3.5). | Read `binding_canonical.py` first. |
| **S5** | **`r*` and the Δ_λ closure ansätze** | See below. | **Relayed, not measured here.** |

#### S1 — the Q_β ladder, measured (registry §9g, probe `qbeta-c3-ladder-trace-convention-sensitivity`, 9/9)

| fact | C frame | D re-extraction | consequence |
|---|---|---|---|
| extracted `c₃` (proton / muon) | −2.06934258 / −2.02020024 | **−974.43 / −974.38** | every ≈−2 value-level fact — **(H1) `c₃^even = −Vol(4₁)`, `[3]_q/25`, `J − ℏ²`, `S_leak`, `q*_S`** — is **C-conditional** |
| anchor swing | 0.0491423 | 0.0493990 (ratio **1.0052**) | the **REFUTED-as-real-q verdict is convention-immune** — it stands in both frames |
| implied empirical `c₂` | −1.0176 | **−9.299** | **`c₂ = −1` (proved Taylor-exact) is a C-frame statement.** The *proof* stands; its *object* now carries its convention |
| N2/N1 residual ratio | 0.017 (58× rung improvement) | 0.89 (**no convergence**) | the ladder's rung convergence exists **in the C frame only** |
| bar parity of `z` | `bar(z_C) = z_C` exact | `bar(z_D) = q⁻⁴·z_D` exact | KC13's no-scalar-`z`-source prune is **C-scoped** |

**S1 is not a z-swap, and this is proved.** `QOU.QBeta.decayLadder_zC_threeRow_ne_zero`
(sorry-free) shows any faithful normalised Markov trace at `z_C` carries
`y_(1³) ≠ 0` for **every** substrate `s = √q > 1`. So *"keep the C-frame ladder"*
and *"the mass channel's two-row forcing applies here"* are **mutually exclusive**.
Under R1 the decay trace is `z_D` — and **the existing ladder is not that trace.**
The ladder must be **re-derived**, not re-evaluated. The `c₃ ≈ −974` figure above
is what the *current extractor* returns when fed `z_D`; it is a sensitivity
measurement, **not** a proposed new value of `c₃`.

#### S5 — `r* ≈ 1.585` (relayed; **not** independently confirmed here)

The tasking states `r* ≈ 1.585` is a C number and that PR #4766 measured
**2.04–2.16 under D**, and that the **six Δ_λ closure ansätze** were tested
against the C value. **I could not locate the #4766 D-frame band in this tree**
and am recording the claim as relayed rather than quoting a corpus measurement
for it. What *is* in-corpus: `r*` appears as the needed ratio in the A3-magnitude
work (`2026-07-26-deltalambda-a3-magnitude-source-three-walls.md:32,39,48`;
`2026-07-27-deltalambda-s5so3-geometric-wlambda.md:35,74`), with derived
candidates `r = 52.6` and `r_both = 1.504`.

**If the relay is right, the consequence is large and should be stated plainly:**
the six ansätze were scored against a target that moves under R1, and
`r_both = 1.504` — recorded as *"a tantalizing 5.1 % short of r* ≈ 1.585"* — is
5.1 % short of a **C-frame** target. **Verify the band before re-scoring
anything.** Do not re-run the ansätze against a number nobody has re-measured.

## 5. What SURVIVES — do not re-derive these

Recorded explicitly so no later agent spends a session re-opening a closed
question.

1. **The KC21 structural parity is convention-IMMUNE, and this is proved, not
   asserted.** [`LadderParityReflection.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/LadderParityReflection.lean),
   `alphaPhase_im_odd_of_reflective_markov` — sorry-free, and **quantified over
   every reflective Markov parameter `z`**, not merely over C and D. The
   mechanism is Schwarz reflection: the only hypothesis on `z` is that it be
   real-valued on the real q-axis near `q₀`; the proof never reads `z`'s formula.
   A control convention `z_X = q/(1+q²)`, present in no channel, has the parity
   too. Verified numerically to `1e-45` relative over `ε ∈ [10⁻³⁰, 10⁻²]`,
   non-vacuously, **while the C→D shift moves the value by 972 — i.e. 470×|c₃^C|**.
   Immunity of the parity and catastrophic movement of the value are both true;
   they are statements about different things.

   Carry the §9h correction with it: the statement is about `Im S`. `Re S` is
   even in `ε` and nonzero (−0.0394593 at the proton pin), so `S(−ε) = −S(ε)`
   written of the *value* is false. The true statement is
   `Im S(q₀−iε) = −Im S(q₀+iε)`.

2. **The REFUTED-as-real-q verdict.** Anchor swing ratio D/C = **1.0052**. It
   stands in both frames.

3. **`c₂ = −1` is still Taylor-exact.** The proof is untouched. What changes is
   that its object is now known to be a C-frame object and must be quoted with
   its convention.

4. **The `z_C` full-bar-condition FAILURE now reads as evidence FOR this ruling.**
   PR #5111 proved `bar(z) = z − h` holds exactly for `z_D`
   (`zD_full_bar_covariant`) and fails for any bar-even `z` — hence for `z_C` —
   away from `q² = 1` (`barEven_fullBar_forces_classical`, `zC_fails_fullBar`).
   Registered at the time as an open structural puzzle, since its premise (trace
   bar-compatibility) was named but unproved and neither convention was derived.
   **Under R1 it is no longer a puzzle**: the convention the owner selected is the
   one that satisfies the condition, and the one excised is the one that fails it.
   The Lean is unchanged and its premise is still a premise — this is a change in
   how the result is *read*, not in what it proves.

5. **The mass channel does not move.** Registry:
   *"numerical_impact_on_this_channel: NONE. Production was already D; only the
   definitional side moved. m_p unchanged."* Verified there:
   `m_p = 938.27208943`, `m_n = 939.56542276`, both unchanged, because
   `trM_borromean` uses the Lean closed form `(4+h²−3h⁴−h⁶)/(h²+4)` and never
   calls `y_lambda_at`.

6. **The binding channel already moved, on 2026-08-09, and it got worse — that
   is recorded and is not a reason to revisit R1.** Mean |err| over
   {²H,³H,³He,⁴He,⁶Li,⁷Li} moved **37.39% → 43.85%**. ²H improved
   (+74.85% → +27.36%) and the ³H/³He mirror split moved 2.2708 → 1.7471 MeV
   (nature 0.7638); everything heavier under-binds worse. The registry states
   explicitly: `not_decided_by: "experimental match — D is worse on aggregate"`.
   **The structural gain is the reason:** under C, AME(²H) = 2.2246 sits 30.4%
   **below** the whole admissible band [2.9072, 5.1780] — an impossibility. Under
   D the band is [2.0507, 3.7978] and AME is **inside** it. A convention chosen
   on a structural forcing, against the aggregate fit, is the anti-fit discipline
   working as designed.

## 6. AGENTS.md — lines that must change (NOT changed in this PR)

Per the tasking, listed for owner approval of wording rather than edited. The
only AGENTS.md change in this PR is the pointer banner (§7).

| location | current text | required change |
|---|---|---|
| §"q₀ anchor convention" STRICT rule 2 | describes the `computations/` layer as "historically carries **muon-q₀** witnesses … ~72 producers / ~840 witnesses" | **840 → 870** (801 muon-only, 69 both-pin). Re-measured this session. |
| §"q₀ anchor convention" STRICT rule 4 | "Migration posture … does **not** authorise a bulk rewrite … still needs scoped sign-off" | Decide whether R2 upgrades this. **Recommendation: it does not** — R2 states the end state; the sweep still needs its own scope. If the owner intends R2 to authorise it, that must be said explicitly here. |
| §"q₀ anchor convention" table | two-layer table, muon vs proton | Add the R2 pointer. The *ideal CAL-2 definition row is unchanged* — R2 is about evaluation, not definition. |
| §"Canonical derivation chain" — `c_k` framing banner | "⚠ Critical framing — Q_β `c_k` is a TRUNCATION ORDER"; quotes `c_3 = -2 = J_Hopf(q=1)` and the "swings up to 3.47 %" figures | Every number in this banner is **C-frame**. Needs a convention label, and a pointer to S1. **Do not change the values** — they are correct *for C*; they need scoping, not correction. |
| §"Precision goals" / Δ_λ gate | "the six closure ansätze … tried to force the magnitude `r* ≈ 1.585`" | Blocked on S5 verification. Do not touch until the D-frame band is measured. |

**Registry lines** (also not changed here): `channels.qbeta-decay`
(`definitional_convention`, `production_convention`, `status`, `open_item`);
`blocked_migrations[0].owner_decision_required`; `ck-dk-canonical-registry.md`
§9g heading and its scope-(a) paragraph.

## 7. The one change this PR does make

A `🛑 OWNER RULING 2026-08-15` pointer banner at the top of the AGENTS.md
q₀-anchor section, directing readers here. Rationale: a ruling nobody can find
is a ruling that gets flip-flopped — which is the documented failure mode this
whole class of doc exists to prevent (six entries in the `c_k` flip-flop table;
the calibration-canon reversal chain of 2026-06-16 → #2832 → 2026-06-26).

## 8. Beans

| bean | role |
|---|---|
| `qou-cdx1` | **milestone** — excise convention C, adopt proton pin + colour weighting |
| `qou-cdh1` | H1 — register the ruling |
| `qou-cdh2` | H2 — close the `pyhecke.gram.z` blocked-symbol leak |
| `qou-cdh3` | H3 — regenerate the 14 convention-C witnesses |
| `qou-cdh4` | H4 — convention-label hygiene |
| `qou-cds1` | **SCIENCE** S1 — re-derive the Q_β `c_k` ladder under D |
| `qou-cds2` | **SCIENCE** S2 — `pyhecke.gram.z` and the Gram singularity |
| `qou-cds3` | **SCIENCE** S3 — muon → proton witness migration |
| `qou-cds4` | **SCIENCE** S4 — p/n convention |
| `qou-cds5` | **SCIENCE** S5 — verify the `r*` D-frame band before re-scoring |

## 9. Related records

- [`2026-08-15-qbeta-decay-channel-convention-disputed-registration.md`](2026-08-15-qbeta-decay-channel-convention-disputed-registration.md) — the registration this supersedes
- [`2026-08-15-c3-refutation-chain-convention-validity-audit.md`](2026-08-15-c3-refutation-chain-convention-validity-audit.md) — the C-conditionality pillar table
- [`2026-08-15-kc21-parity-convention-immunity-audit.md`](2026-08-15-kc21-parity-convention-immunity-audit.md) — what survives (§5.1)
- [`2026-08-08-mass-fibre-dimension-forces-convention-d.md`](2026-08-08-mass-fibre-dimension-forces-convention-d.md) — the mass-channel forcing
- [`2026-08-10-convention-c-witness-regeneration-impact.md`](2026-08-10-convention-c-witness-regeneration-impact.md) — prior regeneration impact
- [`trace-convention-registry.json`](../coordination/trace-convention-registry.json) / [`.md`](../coordination/trace-convention-registry.md) — the machine record
- Beans `qou-b3nk`, `qou-emyt`, `qou-eea0`, `qou-wgta`, `qou-j6il`, `qou-1c4y`
