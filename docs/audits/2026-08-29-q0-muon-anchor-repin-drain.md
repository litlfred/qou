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
