# The two RED q₀ gates are one unfinished migration, not two defects

**Date:** 2026-08-29 · **Bean:** `qou-3f7a` · **Status:** scoped, drain not yet run

## What is red

`scripts/precision-gates.sh` on a clean `main` (`0222d637e8`):

```
RED: q0-anchor flip   q0-value drift ratchet
```

- **`q0-anchor flip`** — 83 `Q0_FLIP`: witnesses stamped `q0Anchor: "muon"`
  carrying `q0Value = 1.10997859555733…` where the anchor now defines
  `1.109978595642…`.
- **`q0-value drift ratchet`** — 383 stale / baseline 329 / **165 NEW**, and
  every drifting site reports the **same** delta: `−0.0769 ppb`.

## They are the same defect

`−0.0769 ppb` is exactly the gap between the two muon values:

| | value | |
|---|---|---|
| **A** | `1.1099785955573347…` | the old frozen pin |
| **C** | `1.1099785956427390…` | CODATA-2022, derived live |

`(A − C)/C = −7.69e-11 = −0.0769 ppb`. The anchor-flip gate reads the
`q0Anchor`/`q0Value` pair; the drift gate reads value sites anywhere in the
tree. Both are seeing one population of stale witnesses from two angles.

## Why the anchor moved — it was deliberate, and it was right

Commit `fca08de7d2` (2026-08-22), on an owner ruling:

> *"2022 CODATA better than 2018. A → CODATA 2022."*

The old pin **A** was self-certifying. `q_pinning_50_digit.py` is listed
`ideal_muon`, so `q_parameter` rebound `q_at` for that very producer and it
wrote back the value it had just read. **A** inverts to
`m_μ/m_e = 206.768282989315`, matching no published CODATA and disagreeing by
1.4 ppb with the ratio the same witness declares in its own
`calibration_inputs`. The witness contradicted its own stated input.

The fix derives rather than re-freezes: `q_parameter`'s muon branch now takes
`q_muon_at()`, the live closed form over `constants.MASS_RATIO_MU_E_STR`, so
the anchor follows the next CODATA revision with no digit edited by hand.

## What remains, and it is stated in that commit

> *"WHAT REMAINS — 53 witnesses, measured not estimated. Stamped
> `q0Anchor: muon` with `q0Value = A`, so moving the anchor makes them stale…
> Each needs its producer re-run at C. NOT done here."*

The commit landed the core deliberately unfinished. **53 has since become 83**
as further muon-pinned witnesses landed on top.

So the red is not a regression, not a phantom, and not this branch's: it is
the tail of an authorised mid-migration, and it grows while it is left alone.

## Scope, measured

**83 witnesses → 75 distinct producers.** 9 witnesses carry no `scriptFile`
and need their producer identified by hand.

Three groups, and only the first is a plain re-run:

1. **Re-run at C** — the bulk. Cost is uneven: `atomic_tr_m_mpfr_50dps`,
   `ame_2020_binding_energies` and `derived_chi_catalogue_matrix_m_mu_n_mpfr`
   are long-compute; `hadron_knot_table` is documented in AGENTS.md as
   running > 50 min for one bound atom and **not finishing**.
2. **By design, so a re-run is not the fix** — `muon_pin_three_values_probe`
   and `muon_pin_stored_vs_live_gate` exist precisely to record A, C and the
   CODATA-2018 value side by side. A producer whose job is to hold the old
   value will hold it again after any re-run. These need the audit to know
   they are comparisons, not a producer change.
3. **Anchor-defining** — `q_pinning_50_digit.py`. Per AGENTS.md rule 1 of the
   migration constraints, **never re-pin it as a consumer**; it is what
   `witness._q0_value_for_anchor("muon")` reads. It is already at C.

## The order is load-bearing

Several of these producers read each other's witnesses. Running them
alphabetically re-emits stale upstream values into freshly-run downstreams —
the defect `q0_repin_sweep.topo_order()` exists to prevent (`qou-lt8x`). Any
drain must build producer → witness → reader edges from the actual files and
run in topological order.

## What must not be done

Per AGENTS.md: **never make a red run green by widening a baseline.** No
`--rebaseline`, no adding a file to `raw-float64-baseline.json`, no
hand-editing a digit. Baselines drain, they do not grow. The fix is at the
producer, and it is a re-run.

## Environment caveat for whoever runs it

This container reports **mpmath 1.3.0** where `main`'s committed witnesses
record **1.4.1**, and **clarabel is absent**. The audit itself warns that
committing from here would replace the environment stamp with a weaker
record. A drain run must either install the missing libraries first or
declare the degradation explicitly in its commit.

---

# Drain run, 2026-08-29 — what actually happened

Everything above this line is the **scoping** pass. This section is the
**drain** pass, and it corrects the scoping in four places. Where they
disagree, this section is the measured one.

## Correction 1 — the anchor-defining witness is internally inconsistent

The scope above says `q_pinning_50_digit` "is already at C". That is **half
true, and the false half is why it appears in the flip list**:

| field in `computations/q-pinning-50-digit.witness.json` | value | state |
|---|---|---|
| `derived_50_digit.q` — what `_q0_value_for_anchor("muon")` READS | `1.109978595642739…` (**C**) | correct |
| `q0Value` — the witness's own provenance self-stamp | `1.109978595557334…` (**A**) | **stale** |

So the anchor *definition* moved to C and the anchor witness's *self-stamp*
did not. This is why `check_reference_integrity()` passes (it reads the first
row) while the same file self-reports `Q0_FLIP` (the audit reads the second).

Consequence for the drain: **every consumer is already reading the correct
value C**, because consumers resolve through `derived_50_digit.q`. The 83 are
stale in their own recorded stamp, not poisoned by a bad upstream. That makes
the drain a pure re-stamp for group M, with no ordering hazard from the anchor
itself.

It also means fixing this file is **not** the forbidden re-pin. Constraint 1
forbids changing what "muon" MEANS — i.e. `derived_50_digit.q`. Bringing
`q0Value` from A to C changes only the self-stamp, making it agree with the
definition already present in the same file.

## Correction 2 — the "by design comparison" group does not exist as described

The scope above says of `muon_pin_three_values_probe` and
`muon_pin_stored_vs_live_gate`:

> *"A producer whose job is to hold the old value will hold it again after any
> re-run. These need the audit to know they are comparisons."*

**That premise is false, and acting on it would have damaged a working gate.**
Neither producer holds A as a literal. All three comparison producers read
their pins live, at run time, from the anchor resolver:

| producer | line | how it gets its muon leg |
|---|---|---|
| `muon_pin_stored_vs_live_gate` | 105 | `stored = mp.mpf(_q0_value_for_anchor("muon"))` |
| `muon_pin_three_values_probe` | 147 | `A = _q0_value_for_anchor("muon")` |
| `deuteron_two_body_kernel_overshoot_probe` | 316 | `_MUON_PIN_STR = str(_q0_value_for_anchor("muon"))` |

A is present in their committed witnesses only because those witnesses predate
the anchor move. A plain re-run fixes all three.

**No change to `q0_anchor_consistency_audit.py` was needed or made.** The audit
already models this correctly: the `comparison` anchor with a `q0Values` map is
verified leg-by-leg against each canonical pin, and it flagged
`muon-pin-stored-vs-live` precisely because that witness named a *wrong* value
as "muon". Exempting it — the change the scope proposed — would have blinded
the one check in the audit that can be *verified* rather than taken on trust.

Note in passing: `muon_pin_three_values_probe` binds a variable literally named
`A` to the resolver. That name is now wrong (the resolver returns C). The name
is stale, not the logic.

## Correction 3 — the 83 are not one population; they split by what a re-run DOES

The scope treats the 83 as one drain. They are three, and the discriminator is
not the producer's identity but **which anchor a re-run resolves to**, which is
decided by whether the producer's stem is listed `ideal_muon` in
`computations/q0_anchor_manifest.json` (45 stems; the list is **not** empty).

| group | witnesses | a re-run yields | in scope here? |
|---|---|---|---|
| **M** — stem is `ideal_muon`, or self-selects the anchor | 33 | muon at **C**, `+0.0769 ppb` | **yes** — this IS the `fca08de7d2` tail |
| **P** — stem is not `ideal_muon` and has no muon mechanism | 47 | **proton**, `−11.54 ppb`, and the anchor STAMP changes `muon → proton` | **no** — this is the 2026-08-15 proton migration, bean `qou-1c4y` |
| **C** — comparison producers | 3 | correct legs (see correction 2) | yes, as a plain re-run |

Measured: **41 of the 47** group-P producers contain no muon mechanism at all —
no `QOU_Q0_ANCHOR`, no `q_muon_at`, no anchor resolver. They carry a `muon`
stamp only because the manifest listed them when they were last run.

This matters because both migrations clear the same gate line while doing
physically different things: `+0.0769 ppb` re-stamp versus a `−11.54 ppb` layer
move. Draining group P here would clear 47 flips and quietly land a large part
of a *different*, separately-tracked migration inside a PR whose stated subject
is the A→C repin. It is left undone deliberately, and the gate stays red by
that amount.

## Correction 4 — these witnesses were stale in MORE than the pin

The scope treats the 83 as carrying one defect: a stale `q0Value`. Measured
with a full field diff (masking ephemeral keys), the drain moved **951 numeric
fields** across the witnesses it touched:

| category | fields | what it is |
|---|---:|---|
| q0 repin A→C | 71 | the expected `+0.0769 ppb` |
| tiny, `<1e-6` | 747 | that repin propagating through derived quantities |
| **convention C→D** | **8** | `rel = 0.2270`, and `z_D/z_C − 1 = 0.227044` |
| **cross-check residuals** | **8** | `1e-50 → 1e-9`, discussed below |
| other substantive | 117 | |

**Report the fields, not just the one the gate keys on.** The first version of
this drain named only `q0Value` in its commit messages, and a 23 % `z_markov`
move in the anchor witness went unmentioned — caught in review, not by me.

### The convention C→D moves are R1-compliant

`z_C(q₀) = 0.499320…`, `z_D(q₀) = 0.612688…`, so a C→D swap shows as
`rel = 0.2270`. Eight fields carry exactly that signature:

- `q-pinning-50-digit` → `.derived_50_digit.z_markov`
- `q-beta-spectral-bridge` → `.z_markov_jones`, `.form_b_log_one_plus_zh`
- `electron-m_e-derivation` → five fields including `.value_50dps_MeV` and
  `.co_casimir_h2_dimensionless`

Those producers migrated to convention D and were never re-run, so their
committed witnesses were **stale-C**. The 2026-08-15 owner ruling **R1** makes
D canonical and excises C, so the new values are correct and the move is
required rather than incidental. Anyone diffing one of these witnesses and
finding a 23 % jump is looking at R1, not at a defect.

### The cross-check residuals: I was wrong twice, and the third answer is tested

`atomic-tr-m-mpfr-50dps.peel_cross_check.abs_diff_vs_bridge` and
`cross-check-trM-1ppb…hoef_vs_habiro` move from `~1e-50` to `~1e-9`.

1. **First reading — wrong.** Off a truncated display I called it a residual
   *improving* to 1e-9. The values are `2.027e-50 → 5.717e-10`: it **degraded**
   by ~40 orders of magnitude.
2. **Second reading — wrong, and refuted by measurement.** I blamed a mixed-leg
   straddle: `cross_check_trM_1ppb` reads four upstreams and I had re-run one.
   So I closed the set — `habiro_coefficients_extended`,
   `markov_peel_atomic_witness` and `canonical_tr_m_via_chi_cache` all re-run at
   the muon anchor in dependency order. **The residuals did not move.**
3. **Third reading — tested.** `atomic-tr-m`'s committed witness records
   `scriptHash c4cdc753dd6d`; the current producer hashes `db23b7ba36cb`. The
   witness **predates its own producer code**, and the commit that last touched
   that producer is `fca08de7d2` — the anchor move itself, which changed the
   producer and did not re-run it, exactly as its own body says.

So the `~1e-9` bridge-vs-peel disagreement is the **honest current state of the
code**; the `1e-50` in the committed witness was produced by superseded code and
was concealing it. The drain reveals it rather than causing it. Corroboration:
`all_atoms_within_1ppQ` was **already `False`** on `main`.

**This is worth someone's attention** — `1e-9` is about six orders of magnitude
above the L1 target of 1 ppQ (`1e-15`), and the corpus's own cross-check now
reports `divergent: 6` of 6 atoms. It is not closed here.

## Six hardcoded muon pins, and why they are the real recurrence risk

The stale stamps are a symptom. The cause is that producers **froze the muon
pin as a literal** instead of reading the anchor, so an anchor move cannot
reach them. Six were found and fixed:

| producer | what it froze |
|---|---|
| `fivetwo_stokes_matrix_zq:93` | `mp.mpf("1.109978595557…")` |
| `theta_jet_gb_grading_probe:55` | `mpf("1.109978595557…")`, commented "muon-q0 **canonical**" |
| `qbeta_hoefsmit_…_build_probe:72` | a **bare float** literal — also a float64 input to a file running at `dps = 65` |
| `qbeta_c4even_…_probe:88` | a fallback that **always** fired, because `free-neutron-decay.witness.json` carries `parameters: null` |
| `lever1_binding_habiro_…:47` | read `qou_substrate.constants` **directly, bypassing `q_parameter`**, so its `ideal_muon` listing was inert and a re-run emitted **proton** (−11.54 ppb) |
| `canonical_tr_m_via_chi_cache:307` | recognised the muon pin by the frozen prefix `"1.10997859555"`, so after the anchor moved it **refused to run at all** |

Two patterns deserve naming:

- **A silently-swallowed import feeding a stale literal.** Both
  `deuteron_two_body_kernel_overshoot_probe:315` and the `c4even` fallback sit
  behind a `try`/`except` or an `if` that never succeeds, so the producer used
  its frozen fallback on *every* run while looking like it read the anchor.
  The deuteron one imported a module named `witness` that exists nowhere.
- **A frozen pin inside a dispatch guard** is worse than a frozen value: it
  does not produce a wrong number, it makes the producer *unrunnable* at the
  new anchor.

All six now resolve through the anchor, so they follow the next CODATA revision
with no digit edited by hand — which is what `fca08de7d2` set out to achieve.

## What was NOT done, and why

- **Group P (47 witnesses) was deliberately not drained.** A re-run moves them
  to **proton**, `−11.54 ppb`, and changes the anchor stamp. That is the
  2026-08-15 migration (`qou-1c4y`), not this one. Draining it here would clear
  47 flips while landing a different, separately-tracked migration inside a PR
  whose subject is the A→C repin. **The gate stays red by roughly that amount,
  and that is the honest number.**
- **`hadron_knot_table`** — not run. AGENTS.md documents it at > 50 min for one
  bound atom without finishing; not worth the session budget.
- **`cross_check_trM_cw_seminormal_leg`** — TIMEOUT at 1200 s. Genuinely long:
  it clears five atoms in ~1 s each and then dies on the A=4 atom in
  `markov_peel.tr_M_atomic`. No witness written, nothing committed.
- **`low_isotope_sign_flip_diagnostic`** — a real producer bug, not fixed here:
  `TypeError: unsupported operand type(s) for +: 'int' and 'str'` in
  `_pearson_r`, i.e. a list of numbers arriving as strings. Not a guard this
  corpus defines, so it is a defect rather than a refusal.
- **`muon-pin-three-values`** now carries one **failing** assertion where the
  committed witness had eight passing ones. The probe's *code* is newer than
  its committed witness, and the current code cannot locate value B in
  `qbeta-h-frame-rungs.witness.json`. That file was not touched here.
- **The `qou-mass` vendor mirror** carries four flipped witnesses —
  including a byte-identical copy of the anchor-defining
  `q-pinning-50-digit.witness.json` — and the audit **cannot see them**: it
  scans `computations/` only. `scripts/sync-qou-mass-vendor.py --check` is the
  mechanism; note it also reports **six pre-existing module drifts** unrelated
  to this work.

## What a future drain should reuse

Three things earned their keep and one did not:

1. **Topological order**, built from producer → witness → reader edges. It put
   `cross_check_trM_1ppb` after `atomic_tr_m_mpfr_50dps` without being told.
2. **A guarded run for the anchor witness** — capture `derived_50_digit.q`
   before, compare after, revert from backup on any difference. Cheap, and it
   is the one file where the 9a9c6b31c7 incident is reproducible.
3. **A full field diff, not an anchor-only check.** The anchor-only check
   passed everything while a 23 % `z_markov` move went unreported.
4. **Manifest membership is the WRONG scope test.** Three witnesses reached the
   muon layer through `QOU_Q0_ANCHOR=ideal` with a `-muon` suffix rather than
   through `ideal_muon`, so a manifest-only split misfiled them. The right test
   is *what anchor does a re-run actually resolve to*.

## Result — `scripts/precision-gates.sh`, before → after

| gate | before | after | |
|---|---|---|---|
| **q0-anchor flip** | 83 `Q0_FLIP` | **47** | 36 cleared |
| **q0-value drift** | 383 stale / 165 NEW | **318 stale / 101 NEW** | 65 stale, 64 NEW cleared |
| **raw-float64 ratchet** | *green* | **red on 1 field** | net **−29** fields, 0 new dirty files |

**All three are still RED, and no baseline was widened to make any of them
otherwise.** No `--rebaseline`, no file added to a baseline JSON, no
hand-edited digit.

### Why each is still red

- **q0-anchor flip, 47.** These are Group P — a re-run sends them to
  **proton**, not to C. That is `qou-1c4y`, a different migration. The number
  is the honest cost of not doing someone else's migration inside this PR.
- **q0-value drift, 318 / 101 NEW.** Same population, seen from the value side.
  Note the "NEW" count fell 165 → 101 while `stale total` fell 383 → 318, i.e.
  the drain removed 64 of the sites that made this gate newly red.
- **raw-float64 ratchet, 1 field.** `c-k-beta-decay-bound` 16 → 17. Measured,
  not inferred: the producer's `scriptHash` is unchanged, the raw float count
  is **identical (20 both sides)**, and the single field that moved is
  `.assertions[0].computed`, `0.0 → 9.961246986709384e-71`. It was exactly
  zero — which the audit excludes as an integral-valued float, exact in
  binary64 — and is now a small non-zero residual, so it **left the carve-out
  and started being counted**. Nothing new entered the witness.

  The correct producer fix is real but out of scope for a drain: that producer
  emits **20** raw float64 fields and its own run warns about all of them
  ("carry `mpmath.mpf` … serialize with `_precision.fmt`"). Doing it properly
  is an mpf refactor changing the representation of 20 committed values.
  Forcing this one field back to `0.0` would suppress a true residual to
  satisfy a counter, which is the thing the ratchet exists to prevent.

  Net on this gate the drain **removed 29 float64 fields** and added none —
  including `qbeta-hoefsmit-tbeta-matrix-build-probe` going `1 → 0`, and one
  real bare-float literal fixed at `wlambda_q0_continuation` (`"tolerance":
  1e-2` → `"0.01"`).

### Environment — an upgrade, not the degradation the scope predicted

The scope warned that committing from this container would weaken the
provenance stamp (mpmath 1.3.0, no clarabel). `pip install mpmath==1.4.1
clarabel` succeeded, so nothing degraded. Better: several of these witnesses on
`main` recorded **mpmath 1.3.0** themselves, so the drain moved them **up** to
1.4.1 + clarabel 0.11.1. `main` is mixed on this field. `sympy` 1.14.0 pins
`mpmath<1.4` and pip warns, but sympy was exercised and works.

---

# Second drain pass, 2026-08-29 — the PROTON half, and why a re-run alone could not do it

The first pass cleared 36 of 83 flips (the muon@C tail of `fca08de7d2`) and
left 47 as "Group P — a re-run sends them to proton; that is `qou-1c4y`, a
different migration". This pass ran that migration under the owner
authorisation recorded in AGENTS.md, and corrects the first pass's
characterisation of those 47 in three places.

## The premise "all 47 resolve to proton, so re-run them" is true of 20 of 45

**25 of the 45 producers hardcode a q0 literal in EXECUTABLE code** — measured
by AST, so a comment or docstring does not count, and 24 of the 25 freeze the
superseded muon pin **A**. For those, a bare re-run does not migrate anything.
It **manufactures a false witness**: the provenance stamp is resolved
independently of the arithmetic, so the re-run writes `q0Anchor: proton` and the
proton `q0Value` onto a payload computed with frozen muon A.

Measured on `a3_branching_asymmetry_vs_required_probe`: after a plain re-run the
stamp read `proton` while `inputs.q0` still read `"1.1099785955573347"` and
`inputs.q0_pin` still read `"muon (ideal CAL-2)"`. **That is strictly worse than
the flip it clears** — a truthful contradiction replaced by a silent one, and the
anchor gate goes green on it. All 25 were run, inspected and REVERTED before
anything was committed.

A sibling reached the same partition independently from the other end
(`qou-1c4y`, 2026-08-29: *"248 sources hardcode a pin the manifest cannot
reach"*). Its guidance — partition by **whether the producer resolves or
hardcodes** before sizing, because the resolving set is a re-run and the
hardcodes are edits each needing its own verdict-robustness check — is what this
pass followed.

## The manifest is not bookkeeping; it gates the staleness check

`ame_2020_binding_energies` re-ran clean and stayed `muon@A` with **zero fields
moved**, every time. The cause is in `WitnessBuilder`'s carry-forward: a producer
that declares no anchor of its own inherits the previous run's
`q0Anchor`/`q0Value` unless the pair is judged stale, and staleness has exactly
two tests —

1. **payload evidence** — `_q0_anchor_from_payload` recognises a q0 in the new
   payload that disagrees with the recorded label;
2. **declared re-anchor** — `q0_anchor_is_declared(script)` then
   `resolve_q0_anchor(script)`.

An **UNLISTED** stem fails test 2 by construction, and a producer with no q0 in
its payload fails test 1. **40 of the 48 muon@A witnesses had an unlisted stem**,
so their stale pair was immune to any number of re-runs.

This is what makes constraint 4 ("do not split the manifest change from the
witnesses") load-bearing rather than procedural: the manifest declaration is what
*enables* the re-run to take effect. Verified before use, on
`ame_2020_binding_energies`: declare `physical_proton`, re-run, `muon@A` becomes
`proton@proton-value`. The declaration changes **no runtime anchor** — an
unlisted stem already resolved proton — it makes the declaration explicit so the
check can fire.

Two further shapes were found in the same mechanism:

- **A label-only staleness test misses a value-only drift.**
  `aK_via_lp_dual_hecke_basis` reads `derived_50_digit.q` (muon, C) and recorded
  it as `repr(Q)` — the STRING `"mpf('1.1099…')"`, not a number — so
  `_q0_anchor_from_payload` could not read it. Recorded `muon`, resolved `muon`:
  the labels agreed, the values did not, `_stale` stayed False, and the witness
  inherited **A** while computing at **C**. Fixed at both ends (`mp.nstr(Q, 50)`
  and an explicit `save({"q0Anchor": "muon", "q0Value": …})`).
- **`q0_anchor=False` is a declaration, and eleven producers made it falsely.**
  It means "this witness carries no q0-dependent field". Eleven producers pass it
  while reading q0 and recording it, so the stamp was DELETED on every run —
  turning a visible `Q0_FLIP` into a silent `Q0_ANCHOR_MISSING`. All eleven were
  written by the same provenance-backfill pass (`qou-4un2`), which suggests the
  flag was applied without checking the payload.

## One frozen literal reached six witnesses

`deltalambda_jet_filtration_magnitude_probe` froze `Q0_STR = A`, and
`a3_precision_order_decomposition`, `a4_precision_order_decomposition`,
`deltalambda_damping_nonmonotone_wall`, `deltalambda_graded_two_anchor_nogo` and
`mu3_target_frame_robustness` all read q0 out of the witness it emits, carrying
no literal of their own. A file-local scan calls those five "resolving"; they are
not. **The AST test is file-local and cannot see an inherited pin** — the same
import-cone blindness AGENTS.md documents for witness staleness.

The discriminator that does work is empirical: re-run, then scan the whole
witness text for each pin family. A payload still carrying **A** under a
`proton` stamp is a false stamp; a payload carrying only **P** under a `proton`
stamp is a migration.

## A comparison producer cannot be fixed by choosing a pin

Four producers now declare `q0Anchor: "comparison"` with a `q0Values` map (2 of
them added here). Stating the legs found two real defects in
`murakami_deformed_vc_q0`, whose subject *is* the μ–p tension:

- its **muon** leg was the superseded pin **A**, so the muon side of a tension
  adjudication had not been the muon pin since PR #5500. The witness contains its
  own test: `m_mu_over_m_e_from_anchor` was `206.76828298931504382` — which
  AGENTS.md records as matching no published CODATA — and is now `206.7682827`,
  the CODATA-2022 ratio;
- its **proton** leg was **truncated to twelve digits** inside a file running at
  60 dps: ~0.1 ppb of fabricated error in a probe whose whole quantity is an
  11.5 ppb gap, i.e. ~1 % of the effect, injected by the input.

## Two "fallbacks" that fire on every run

`qbeta_c3even_exact_sseries_probe` and its c4even sibling read q0 from
`free-neutron-decay.witness.json` and fall back to a literal `if params is None`.
That witness carries `parameters: null`, so **the `else` fires on every run and
the literal was the pin** — a frozen muon A wearing the shape of a rare safety
net. This is the second instance of the class on this bean. A silently-always-
taken fallback is how a producer keeps computing at a retired anchor while its
source reads as though it resolves one.

`zhabiro_phiq_production_crosscheck` had the same shape plus the lever1 defect —
it imported `qou_substrate.constants.q_at` directly, bypassing `q_parameter`, so
the manifest and `QOU_Q0_ANCHOR` could not reach it and an `ideal_muon` listing
on that stem would have been inert.

## An LP-dual defect on main, found by the field diff

Every one of the 421 "large" field moves in the first commit is
`a-K-via-lp-dual-full .data.active_set[i][j]`. The dual variables are
**byte-identical** across the re-run — `y0_star`, `y_star`, `primal_obj`,
`dual_obj`, `duality_gap` all unchanged — while `active_set` went from a sparse
selection to every index. Checked against the definition (`active_set` = indices
with `y_star[i] > 0`) in the **committed** witness: it disagreed with its own
`y_star` in all six atoms — 1 vs 3, 1 vs 3, 7 vs 11, 25 vs 30, 25 vs 30, 70 vs
77. Every `y_star` entry is positive, so the correct active set is all of them.

Per AGENTS.md the active set is the structural payload of these witnesses
("which Wedderburn blocks the bound state actually saturates"), so this is a
**result correction on `main`**, not bookkeeping. That all 154 channels come out
active is itself worth someone's attention; it is what the committed duals say,
and nothing here changed them.

## A producer bug fixed — and it was a precision defect too

`low_isotope_sign_flip_diagnostic` had been dying on `TypeError: unsupported
operand type(s) for +: 'int' and 'str'` (filed by the first pass, not
diagnosed). Cause: upstream witnesses serialize numbers as **strings** under the
NO-FLOAT64 discipline, so `err_pct` arrives as `"-1.234"` and `sum(ys)` raises.

The naive fix — wrap each read in `float()` — would have installed exactly what
AGENTS.md bans for probes: `sum(xs)/n` and `** 0.5` aggregate a sample in
float64, and this function's output is an **argument** (an R² that picks the
verdict), not a display value. `_pearson_r` and `_linear_fit` now carry
`mpmath.mpf` end to end. Verdict unchanged ("WEAK correlation", R² 0.265287 →
0.265294), so this is a fixed producer, not a changed result.

## `c₂^even` moved, and it is NOT the q₀ re-pin — measured at both pins

Re-running `qbeta_c3even_exact_sseries_probe` after migrating its
always-taken fallback changed **exact symbolic coefficients**:

| | committed on `main` | after re-run |
|---|---|---|
| `c2_even_exact` | `-1049/144 - 5√3/12` | `-887/144 - 3√3/4` |
| `c2_even` | `-8.00641005870925442785865819785` | `-7.45876032789888019236780697835` |
| `c3_even` | `86.6611630646909942600690102713` | `78.5944241201958767026137262347` |

and the producer's own gate assertion `c_2^even gate vs prior robust rung
(−8.006 ± 0.05)` flips **PASS → FAIL**. `-8.006` is the figure AGENTS.md carries
as one of the three live meanings of `c₂`.

**An 11.5 ppb pin change cannot move an exact rational, and it did not.** Two
independent checks:

1. **By reading the code.** q₀ enters this producer at exactly three places: a
   validation `assert`, `sgn = sign(Δnet(q₀))`, and a recorded parameter. `sgn`
   multiplies `Qb_over_me`, hence `Rq` — and the series is taken of
   `log(Rq / R1)` with `R1 = Rq(q=1)`, so a global sign **cancels**. Everything
   else is symbolic in `q`.
2. **By measurement.** `origin/main`'s version of the producer, with its
   **frozen muon-A literal**, was run against the same tree. It produces
   `c2_even_exact = -887/144 - 3√3/4` and
   `c2_even = -7.458760327898880192367` — **identical to the proton run, to
   every digit emitted**. The exact block compares equal in full.

So the coefficients are the honest current state of the code and the committed
witness is stale relative to its own producer — the same class the first pass
proved for `atomic-tr-m`, and confirmed here by provenance: the committed
`scriptHash de6bb2573274` matches **neither** the current file (`416240070fda`)
**nor** `origin/main`'s (`af310a672f84`).

**The change traces to `7c2fd9d765 science(qou-cds1): all of the ladder's
convention-dependence is ONE phase`**, which edited this producer on `main` and
did not re-run it. `z = q³/(q²+1)` in the current source is **convention D**;
AGENTS.md records the whole `c_k` ladder as convention-C-frame and requires it to
be **re-derived** under D (bean `qou-cds1`), explicitly noting that this is *not*
a z-swap. `−8.006` is a C-frame number.

**NOT LANDED HERE, deliberately.** The witness was reverted. This is
`qou-cds1`'s result to publish, with its re-derivation reasoning attached;
landing a changed `c₂^even` and a newly-failing ladder gate inside a PR whose
subject is the q₀ anchor would be the same error this pass avoided for Group P.
The producer's fallback fix **is** committed, so re-running it is all that
remains — and the pin is no longer what stands in the way.

`qbeta_c4even_exact_sseries_probe` is the same shape and is likewise not landed.

## Result — `scripts/precision-gates.sh`, three passes compared

| gate | `main` | after pass 1 | after pass 2 |
|---|---|---|---|
| **q0-anchor flip** | 83 | 47 | **5** |
| **q0-value drift** | 383 stale / 165 NEW | 318 / 101 | **240 / 26** |
| **q0-anchor refill ratchet** | green | green | green (NEW 0) |
| **raw-float64 ratchet** | green | red on 1 field | **NEW 0, REGRESSED 0** |

`Q0_OK` 984 → **1025**; `Q0_COMPARISON` 2 → 4, all four with a reason and named
legs; `Q0_ANCHOR_MISSING` 1668 → **1667**.

**No baseline was widened at any point** — no `--rebaseline`, no file added to a
baseline JSON, no hand-edited digit.

### The 5 that remain, each with a reason rather than a guess

| witness | why it is still red |
|---|---|
| `qbeta-c3even-exact-sseries` | re-runs clean; its result is `qou-cds1`'s C→D ladder re-derivation, deliberately not landed here (above) |
| `qbeta-c4even-exact-sseries` | same shape as c3even; long compute, not landed |
| `qbeta-c3-complex-habiro-cross-anchor` | reads no live pin. Its two anchors are **historical** 12-digit values paired with the c₃ values measured at them, so re-pinning breaks the pairing and `comparison` would name legs that cannot match a canonical pin. Needs a judgement about whether the stored c₃ pair is still the right datum — not a labelling decision |
| `cross-check-trM-cw-seminormal` | genuinely long: clears five atoms in seconds and then runs indefinitely on the A=4 atom in `markov_peel.tr_M_atomic`. Two attempts, > 1200 s each, no witness written |
| `hadron-knot-table` | AGENTS.md: > 50 min for one bound atom of nineteen, and does not finish |

### What else was left undone

- **The `q0-value drift` NEW-26 are the FIRST migration's tail, not this one.**
  Every one reports `−0.0769 ppb` — the A→C muon step — at value sites inside
  witnesses whose producers were not re-run (`b-over-a`, `delta-S-chain-audit`,
  `a3-magnitude-berezinian-crossterm`, …). They are muon@C work, and each needs
  its producer re-run, not a re-pin.
- **The `q0-anchor-missing-baseline.json` was NOT regenerated**, though 11
  witnesses drained out of it. Banking them is a baseline edit, and this pass
  did not make baseline edits of any kind; a future pass can regenerate it in a
  commit whose subject is that.
- **`ambiguous` shrank by one**, `gap_a4_T11_klein_J_invariant_probe` →
  `physical_proton`. Not a re-classification by taste: its q₀ comes from
  `_gap_a4_qsafe.Q_0_50DPS = Q_50_DIGIT_STR`, one source with no branch, so it
  resolves the proton pin unambiguously. It had to move because
  `resolve_q0_anchor` returns `('ambiguous', None)` — **no value** — so the
  stamping path wrote nothing at all, and once the stale muon pair was correctly
  dropped the witness had no anchor. That tripped the refill ratchet, which is
  blocking and green-on-arrival. An `ambiguous` stem that *does* resolve a
  concrete pin is a silent hole in the stamping path.

## Post-rebase re-measurement (2026-08-29, `/prepare-merge`)

Everything above records what this branch's own two passes did, measured
against the `main` they started from. That `main` has since moved 61 commits,
and one of those arcs was **a concurrent q₀ drain of its own** (`cfe73b8eb5`,
"re-run the flip producers at the derived anchor — Q0_FLIP 83 → 34"). The
numbers below are the rebased head, and they differ from the tables above for
that reason. The tables are not corrected: they are a record of two passes
that happened, and they were right about the tree they ran on.

### Gate counts on the rebased head

| gate | this branch, pre-rebase | rebased onto `main` |
|---|---|---|
| **q0-anchor flip** | 5 | **3** |
| `Q0_OK` | 1025 | **1032** |
| **q0-value drift** | 240 stale / 26 NEW | **307 stale / 81 NEW** |
| **raw-float64 ratchet** | NEW 0, REGRESSED 0 | NEW 0, REGRESSED 0 |
| **witness shape guard** | — | collapsed 0 |

**The three remaining flips are a strict subset of the five named above**:
`cross-check-trM-cw-seminormal`, `hadron-knot-table`,
`qbeta-c4even-exact-sseries`. Each keeps the reason already given for it.
`main` independently drained the other two —
`qbeta-c3even-exact-sseries` and `qbeta-c3-complex-habiro-cross-anchor` — so
this branch's decision **not** to land the C→D ladder re-derivation
(`qou-cds1`) was not undone by the rebase; the flip cleared from the other
side.

**The drift number went up because two drains merged, not because a site
regressed.** Every NEW-stale entry still reports the same `0.0769 ppb` A→C
muon step described above. Attribution was measured rather than assumed: for
each NEW-stale witness, its q₀-bearing field values were compared against
*both* parents. **Zero differ from both** — 19 have values on which the two
parents agree, 2 are this branch's own. No q₀ value on the rebased head was
produced by the merge.

### Two defects the merge itself introduced, and how they were caught

Neither was in the branch as pushed; both were artifacts of resolving 81
overlapping witnesses between two concurrent drains.

1. **A split `q0Anchor` / `q0Value` pair in two witnesses.** The two fields
   are coupled and a field-level 3-way merge does not know that, so
   `habiro-coefficients-extended` and
   `lever1-binding-habiro-single-element-test` each ended up labelled
   `proton` while carrying the muon value — two `Q0_FLIP`s present on
   neither parent. Resolved by **re-running each producer on the merged
   tree** rather than by choosing a side: `habiro_coefficients_extended`
   emits proton and reproduces `main`'s witness exactly (of 409 leaves in
   `results`, the only 20 that differ are `timings_sec`);
   `lever1_binding_habiro_single_element_test` emits muon, matching this
   branch's copy with zero non-ephemeral differences — which is the branch's
   own producer fix from `97c6f695e0`, where the producer read
   `qou_substrate.constants` directly and its `ideal_muon` listing was inert.
   A tree-wide scan for the same shape now reports 0.
2. **39 witnesses re-serialized with `ensure_ascii=True`.** Caught by
   `witness_shape_guard.py`, which saw only the 2 unstaged vendored mirrors;
   scanning against both parents found the real population. The producers
   write UTF-8 — confirmed by round-tripping four `main` copies through
   `json.dumps(d, indent=2, ensure_ascii=False)`, which reproduces them
   byte-exactly. No value moved.

**The anchor-DEFINING witness was not re-pinned.**
`computations/q-pinning-50-digit.witness.json` is byte-identical to
`origin/main` on the rebased head. `main` had independently landed the same
self-stamp refresh this branch made, so that commit replayed as empty and
was dropped — 20 commits became 19.

### Still not done, unchanged by the rebase

No baseline was widened at any point in the rebase either: no
`--rebaseline`, no file added to a baseline JSON, no hand-edited digit, and
`q0-anchor-missing-baseline.json` still not regenerated. The two producers
this pass deliberately declined to re-run (`qbeta_c3even`, `qbeta_c4even`)
were **not** re-run during the merge.
