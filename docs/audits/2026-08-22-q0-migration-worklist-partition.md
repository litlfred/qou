# The q₀ migration work-list is 5 confirmed, not 624 — and the largest muon population is a *different* defect

**Date:** 2026-08-22
**Bean:** `qou-1c4y` (re-baseline)
**Branch:** `claude/q0-migration-rebaseline-2026-08-22`

## Summary

`qou-1c4y` has carried a headline of "~840 muon-q₀ witnesses", which I
re-baselined earlier this session to a measured "624 fingerprint / 65
stamped". **Both numbers are wrong in the same way**: they were produced
by grepping a 12-digit prefix of the muon pin, and that prefix does not
identify the muon pin. It conflates two distinct q₀ values.

Measured over the 3030 tracked `computations/**/*.witness.json`:

| population | count | what it is |
|---|---:|---|
| current muon `1.109978595557334…` | 210 | the live ideal/CAL-2 pin |
| **superseded muon `1.109978595554180…`** | **374** | the *old* muon value — a pin-currency defect |
| both values present | 24 | deliberate cross-anchor comparison, mostly |
| rounded / low-precision variants | 31 | e.g. `1.10997859556` |
| **loose-prefix total** | **639** | |

The prefix sensitivity is the tell:

```
1.1099785955        -> 642
1.10997859555       -> 624   <- the number I re-baselined to
1.109978595557334   -> 236
1.10997859555733471 -> 206
```

The drop from 624 to 236 is not precision loss. It is 388 witnesses
carrying a **different number**. The two muon values diverge at the 12th
decimal digit.

## The superseded value is already documented

`1.109978595554181` is named in
[`.claude/skills/local/language-trap-agent-audit.md`](../../.claude/skills/local/language-trap-agent-audit.md)
as *"the **old muon value** — arithmetically correct (it solves the CAL-2
identity and back-implies CODATA m_μ/m_e to 12 digits), so report it as a
pin-currency defect, not a corrupt number"*. That guidance is right and I
am not restating it as new. What is new is the **size**: it is the
largest single muon population in `computations/`, and it was invisible
inside the "624 muon witnesses" headline.

This matters for how the sweep is framed. A witness on the superseded
muon value is wrong **under either convention** — re-pinning it to proton
and refreshing it to the current muon value are both improvements, and
leaving it is wrong either way. It is not "awaiting the proton
migration"; it is stale on its own terms.

## The confirmed defect class: declared proton, pins muon

Separately, and much sharper — the `q-pinning-50-digit.witness.json`
read path.

That witness is **muon-anchored** (`q0Anchor: "muon"`,
`q0Value: 1.10997859555733471…`). Narrowing over live (non-`_deprecated`)
producers:

| | count |
|---|---:|
| reference the file (152 including `_deprecated/`) | 136 |
| … read the JSON directly **and never import `q_parameter`** | 69 |
| … and bind q₀ from `derived_50_digit["q"]` | **55** (was 56; one fixed here) |

Those 56 pin to muon with no anchor resolution at all — they get whatever
that witness happens to carry, regardless of the 2026-08-07 owner
directive that compute defaults to proton. Crossed against
`q0_anchor_manifest.json`:

- **51 UNDECLARED** — nobody has classified them.
- **4 declared `physical_proton`** — a flat contradiction. (Was 5; `b_over_m_order_probe` is fixed in this PR — see below.)

The 5:

| producer | witness |
|---|---|
| `aK_via_lp_dual_hecke_basis.py` | `a-K-via-lp-dual-hecke-basis.witness.json` |
| `b_over_m_order_probe.py` | `b-over-m-order-probe.witness.json` |
| `path4_rho_K_at_h3A.py` | `path4-rho-K-at-h3A.witness.json` |
| `q1_mass_gap_probe.py` | `q1-mass-gap-probe.witness.json` |
| `q_beta_form_a_n1_extension.py` | `q-beta-form-a-n1-extension.witness.json` |

**Confirmed in both directions, not inferred.** Each of the five is
declared `physical_proton` in the manifest, binds q₀ from the
muon-anchored witness in code, *and* emits a witness stamped
`q0Anchor: "proton"` whose recorded q₀ is the muon value. The witness
contradicts itself.

`q1_mass_gap_probe.py:170` is the clearest instance — the line reads

```python
# q₀ from the canonical pinning witness (proton anchor)
```

directly above a read that returns the muon value.

## The disposition of the 5 is not uniform — but not for the reason I first wrote

**Corrected in the same session.** My first pass read
`q_beta_form_a_n1_extension`'s comment *"Load **CAL-2** q_0 from canonical
pinning witness"* as evidence that the producer deliberately wants the
ideal muon layer, and concluded the *manifest* was the bug. That was
wrong, and it inverted the argument I built on it.

AGENTS.md §"q₀ anchor convention" is explicit that the 2026-08-07
directive *"is about which **numerical evaluation** code defaults to, not
about redefining the 3-CAL triple"* — the ideal CAL-2 definition
(`𝔇_β`, proxy `m_μ/m_e`) is untouched, while **compute evaluates at the
proton pin**. So naming CAL-2 identifies *which calibration*, not *which
pin*. Treating it as a pin choice is exactly the conflation the directive
exists to prevent. The manifest entry is right; the read is the bug.

Corrected dispositions:

| producer | evidence | disposition |
|---|---|---|
| `b_over_m_order_probe` | docstring: *"Computed at the **proton-pinned** q₀"* | **read is the bug** |
| `path4_rho_K_at_h3A` | compares against proton/neutron `ρ_K_CODATA` | **read is the bug** |
| `q_beta_form_a_n1_extension` | *"Load CAL-2 q_0"* names the calibration, not the pin | **read is the bug** |
| `q1_mass_gap_probe` | reads the witness for **two** purposes — binds q₀ from it *and* uses its `plancherel_weights_n3` / `[2]_q` as a reference table | **dual-purpose read** |
| `aK_via_lp_dual_hecke_basis` | "H_3 (proton, neutron)" names the *particle*, not the pin | no stated intent — directive default applies |

### What survives, and what does not

**Does not survive:** my claim that a mechanical re-pin would have broken
`q_beta_form_a_n1_extension` by overriding a deliberate ideal-layer
choice. Under the directive, re-pinning it to proton is the *correct*
action. Three of the five are now plain read-bugs.

**Survives, but narrower:** `q1_mass_gap_probe` still resists a mechanical
sweep, for a different reason. It reads
`q-pinning-50-digit.witness.json` for two things at once — its q₀ bind
*and* its recorded Plancherel weights, used as a cross-check reference
table. A naive re-pin that redirects the whole read to the proton source
fixes the first and breaks the second. The hazard is a **dual-purpose
read**, not a layer-intent conflict.

That is a weaker argument than the one I first made, and it is the one
the evidence actually supports. The sweep still needs per-file reading —
but to find dual-purpose reads, not to adjudicate which layer each
producer wants.

## Relation to the trap `qou-1c4y` already names

The bean already flags `wedderburn_jones_markov.y_lambda_at`, where a
muon-built cache is served to a caller that passed the proton constant,
with no signal that a layer boundary was crossed. The 56 above are the
**direct-read sibling** of that trap: instead of a cached accessor
silently returning the ideal-layer value, the producer opens the
ideal-layer witness itself and never asks which anchor it wants. Same
failure, one layer down, and it bypasses every guard built into the
accessor path.

## 🛑 CORRECTION 2026-08-22 (post-merge): the dual-purpose count is 3, not 21

The section below reports **21** of the direct pinners as reading the pin
witness for more than q₀, and builds a "straddle-by-partial-repin" hazard on
20 of them co-reading q₀-derived scalars. **The 21 is wrong — measured
correctly it is 3.**

The detector matched the bare field name **anywhere in the file**. That also
catches locally-computed variables (`hbar_q_num = (q_0 - 1) / q_0`,
`hbar_q_sym`) and the producer's own *output* keys (`hbar_q_50dps`), none of
which are reads of the witness. The correct test is dict-key use — a
subscript or `.get()` against the loaded witness — and it is now
`co_read_fields()` in
[`q0_muon_population_partition.py`](../../computations/audits/q0_muon_population_partition.py),
so the number is re-derivable rather than hand-scanned.

Substring: **21**. Dict-key: **3**. A 7× over-report.

The three that genuinely co-read:

| producer | field | evidence |
|---|---|---|
| `nuclide_braid_pipeline` | `hbar_q` | `_QPIN["derived_50_digit"].get("hbar_q")` at `:66` |
| `qbeta/qbeta_decay_sdp_extended_ck` | `hbar_q_sq` | `mpf(str(data["hbar_q_sq"]))` at `:168` |
| `q1_mass_gap_probe` | `plancherel_weights_n3`, `two_q` | the reference-table case |

**What this changes.** The straddle hazard is real but **narrow**: 3 producers,
of which 2 co-read a q₀-derived scalar and 1 co-reads a reference table. It is
not the dominant shape of the migration's remaining work, and the earlier
framing ("only one is a reference table; the other 20 co-read q₀-derived
scalars") overstated it substantially.

**What this does not change.** The root-cause finding below — that a direct
reader cannot be migrated by re-running it, because its q₀ comes from the
anchor-defining witness, which must stay muon — is independent of this count
and stands. So do the census (210/374/24/31), the 55 direct pinners, the 4
remaining contradictions, and the `load_q_50dps` default.

**Consequence for two of the four remaining contradictions.** I had recorded
`path4_rho_K_at_h3A` and `q_beta_form_a_n1_extension` as dual-purpose and
therefore complicated. They are not: `path4_rho_K_at_h3A:46` computes
`q_inv = mpf(1) / q` locally, and `q_beta_form_a_n1_extension:163` computes
`hbar_q_num = (q_0 - 1) / q_0` locally. Both are simple single-read fixes of
the same shape as `b_over_m_order_probe`.

## The sweep hazard, measured: dual-purpose reads and a defaulting utility

Of the 56 direct pinners, **21 read the pinning witness for more than
q₀**. The shape matters more than the count:

| co-read field | producers |
|---|---:|
| `hbar_q` | 12 |
| `q_inv` | 4 |
| `two_q` | 4 |
| `hbar_q_sq` | 3 |
| `z_markov` | 3 |
| `H_A` | 1 |
| `plancherel_weights_n3` | 1 |

Only the last is a reference table. The other 20 co-read **q₀-derived
scalars**. So a sweep that re-points the `["q"]` read to proton and leaves
those alone produces a **straddle inside a single producer** — one leg on
the experimental pin, the rest on the ideal one. AGENTS.md forbids exactly
that ("Never straddle the two layers inside one quantity"), and the
measured cost of the last such case was 11.54 ppb. This is the concrete
form the sweep hazard takes.

### `_li_2_q_util.load_q_50dps()` — a muon default with 28 live callers

`computations/_li_2_q_util.py:191` falls back to the muon-anchored pinning
witness when its `path` argument is omitted:

```python
_Q_WITNESS_DEFAULT = Path(__file__).parent / "q-pinning-50-digit.witness.json"

def load_q_50dps(path: Path | None = None) -> tuple[mpf, mpf, mpf]:
    if path is None:
        path = _Q_WITNESS_DEFAULT        # muon-anchored
```

**Measured: 28 live no-arg call sites across 26 files**; the module has 104
importers. This is the `y_lambda_at` trap one more time — an ideal-layer
value reaching an experimental-layer caller with no signal — arriving via a
**default argument** instead of a cache-hit gate.

It has been found before and fixed **point-wise**:
`delta_lambda_v_hat_z_transfer_phase5d_4.py:80` still carries the marker
`# 🛑 Was: load_q_50dps(), which reads the MUON q-pinning-50-digit`. One
file was patched; the default was left, and 28 call sites still take it.

### A separate observation, deliberately not claimed as a defect

The same function returns `z = 1/(√q + 1/√q)`. Verified at 50 dps:

```
z from load_q_50dps  0.4993203340335612717689664
z_C = √q/(q+1)       0.4993203340335612717689664    agree to 1.3e-51
z_D = q³/(q²+1)      0.6126880505488901570445168    differs by 18%
```

It is **convention C exactly**, and `scripts/convention-c-producer-audit.py`
(1 actionable site) does **not** flag it — a C value returned as a *tuple
element* is a spelling the detector does not scan, which is a further entry
for the detector-blindness taxonomy.

**What is not claimed:** that this `z` is *the* Markov parameter subject to
owner ruling R1. `compute_t2_t3_from_vols` consumes it as `T3 = z²·Σ_{i<j}`,
a brane-tower pair weight, and a pair weight sharing a formula with the
Markov parameter is precisely the glyph-collision hazard AGENTS.md §"Grep
the claim SHAPE" describes. Settling it needs a corpus read or an owner
call, not a grep. Tracked as `qou-dkm2`.

## Classifying the 51 undeclared — and the retraction doing work as a rule

The stated next step was to classify the 51 undeclared direct pinners.
Triaging them by what each producer *says* it wants, reading comments and
docstrings only:

| what the producer states | count |
|---|---:|
| **silent on the pin** | **46** |
| muon-pin intent | 2 |
| both (comparison) | 2 |
| proton-intent | 1 |

**The classification is mostly not a reading task.** 46 of 51 never say
which layer they want — so the 2026-08-07 directive already answers them:
proton unless there is an explicit reason, and there is no stated reason.
That collapses most of the "51 unknown" into the directive default, and
leaves 5 that need a human look.

### The CAL-2 trap, applied as a classifier

A first pass counted 5 producers as muon-intent. Three of those matched
only on phrases like *"derived from CAL-2 q_0"* (`c_k_beta_decay_witness`,
`derive_m_e_hecke_path_a`, `q_beta_spectral_bridge_witness`) — which is
**the same inference retracted above**: CAL-2 names the calibration, not
the pin.

The two that survive name the *pin* explicitly:
`bring_2loop_weight3_coefficient_probe` prints `q0 (muon pin)` and is
*about* the muon anchor's CODATA uncertainty;
`probes/qbeta_c3_per_block_categorical_probe` states *"re-evaluating at
**muon-pin** q_0 reproduces muon-pin c_3"*. Those are genuine ideal-layer
producers.

So the correction made earlier on this branch is not bookkeeping — encoded
as a rule in `classify_intent()`, it reclassified three of five producers.
The classifier carries a comment saying why CAL-2 mentions are deliberately
not muon signals, so the next agent does not re-derive the same mistake.

## Coordination with `qou-o922` — the two audits catch opposite failure modes

A sibling branch is measuring a closely-related population under bean
`qou-o922` (`computations/audits/undeclared_muon_pin_flip_risk_audit.py`,
baseline ratcheted 49 → 40). Measured intersection against my 56:

| | count |
|---|---:|
| `qou-o922` at-risk | 49 |
| my direct muon-pinners | 56 |
| **intersection** | **4** |
| sibling only | 45 |
| mine only | 52 |

Nearly disjoint — and the reason is that the two populations behave
**oppositely on re-run**:

- **`qou-o922`:** witness stamped `muon`, producer absent from the manifest.
  On re-run, `q_parameter` falls through to the **proton default** *and*
  `WitnessBuilder` drops the `q0Anchor` label in the same step. **Re-running
  flips the pin and destroys the evidence that it flipped.**
- **This audit:** the producer reads `q-pinning-50-digit.witness.json`
  **directly** and never imports `q_parameter`. Manifest state is irrelevant
  to it. **Re-running does not flip anything** — it stays on muon
  indefinitely.

### The consequence for `qou-o922`'s stated fix

That bean's next step reads *"add a manifest entry under `ideal_muon` or
`physical_proton`, THEN re-run."* That is correct for its own 45, and it is
**a no-op for my 52**: a producer that never consults `q_parameter` does not
observe its manifest entry. Declaring it and re-running leaves it on the muon
pin while the declaration says otherwise — which is precisely how the 5
contradictions above came to exist.

The four in both populations are
`qbeta_dladder_ecalle_acceleration_probe`, `qbeta_fsc_g_pattern_comparison`,
`qbeta_symbolic_sdp_strict_complementarity`, and
`qbeta_trm_crosscheck_convention_pin_split_probe` — these need the read fixed
*before* the manifest entry, or the entry will not take effect.

Together the two audits cover 101 producers (49 + 56 − 4), and neither sees
the other's set.

## Re-measured after #5457 merged — and the `independent` test has a blind spot

A sibling asked on this PR to *"rebase and re-measure before trusting a
pre-merge q₀ census"*, since #5457 (`238fc79f6e`) dispositioned nine
producers as `q0Anchor: independent`. Done — and the two metrics move by
different amounts, which turns out to be the interesting part.

| metric | delta |
|---|---|
| their `canonical` count | 221 → 212 (−9) |
| **my muon-value census** | 642 → 640 (**−2**) |

Both are right; they measure different things. Theirs asks *does this
witness **assert** a muon pin?* — the `q0Anchor`/`q0Value` pair. Mine asks
*does this witness **carry** a muon-derived number anywhere?* Of the 10
witnesses stamped `independent` in that range, **8 still contain muon digits
elsewhere in the file**, which is exactly why my delta is 2.

### Where those digits come from

The `independent` disposition is assigned when a producer's output is
byte-identical under `QOU_Q0_ANCHOR=muon` vs `=proton`, taken as proof it
never reads q₀. But that variable only reaches q₀ resolution **routed through
`q_parameter`**. So the test measures *override-sensitivity*, and that
coincides with q₀-independence only when q₀ arrives by that path. Two routes
defeat it — a **hardcoded q₀ literal** (an env var cannot change a string
constant), and a **direct read of the pinning witness** (never consults
`q_parameter`). Both yield byte-identical output under either anchor while
being hard-pinned to muon.

Measured across all 37 `independent`-stamped witnesses on `main`:

| | count |
|---|---:|
| stamped `independent` | 37 |
| … still carrying muon digits | 9 |
| … … producer hardcodes a muon q₀ literal | **6** |
| … … producer reads the pinning witness directly | **1** |
| … … value inherited from an upstream input | 2 |

**7 of 9 are provably not q₀-independent.** Worked example —
`qbeta/qbeta_c3_rung_structure_analysis.py:74`:

```python
Q0_MP_PIN = "1.1099785955573347198997632204832250266562084087802"   # muon
...
q0_mp = mp.mpf(Q0_MP_PIN)          # "Numerical check at q_0"
```

Its witness records `q_0 = 1.1099785955573347198997` under the primary pin key
while asserting `independent`. The label says the producer does not use q₀;
the data block says it evaluated at the muon one.

**Scope.** The drain is good work and the `save()` carry-forward fix is
correct; this is a blind spot in one criterion, not a reason to revert
anything. 28 of the 37 labels are untouched by this. And a hardcoded literal
is not automatically wrong — a probe may legitimately pin a q₀ for a stability
check. The defect is the **label**: `independent` records the opposite of what
the producer does, and hides it from every later pin audit. Tracked as
`qou-324i`.

## One fix landed, end to end

`b_over_m_order_probe` was the cleanest of the five: declared
`physical_proton`, docstring says *"Computed at the **proton-pinned** q₀"*,
a single q₀ read, and **not** among the 21 dual-purpose readers — so no
co-read scalars to straddle. Fixed here as a demonstration that the finding
is actionable, not just measurable.

The read now goes through `q_parameter.Q_MP`. That is the proton pin at the
**same 50 dps** (`1.109978582751380807591669095610768879874499121873577636…`),
so it is not a precision downgrade — checked before the swap. The witness
gained a `q0_anchor` field naming the pin, per AGENTS.md's "say which pin you
used".

Verification, in order:

1. **The number moved as predicted.** `q0_50dps` went
   `1.10997859555733471…` → `1.10997858275138080…`, and every derived
   quantity with it. `q0_value_drift_audit` reclassified the witness
   `canonical` → `proton-pin` at `ppb_vs_canonical: −11.537117889987831` —
   the μ–p substrate tension itself, which is the right magnitude.
2. **The conclusion did not move.** `n6_family_splitting_at_q0` changed in
   the 9th significant digit. This is an order-of-magnitude probe, so its
   verdict is robust to an 11.5 ppb pin shift. The fix corrects *which pin
   the probe declares it used*, not any finding.
3. **`scripts/precision-gates.sh --changed`: all blocking gates green.**
   The one advisory `UNTRACEABLE` literal (`qbeta_t4_stokes3_crux_probe.py:60`,
   `A_omega = 3`) is pre-existing and unrelated.
4. **Environment restored before committing the witness.** The first run
   warned that this container recorded *less* than the committed witness —
   `clarabel` dropped, `mpmath` 1.4.1 → 1.3.0. Rather than commit a weaker
   provenance record, both were installed and the producer re-run; the
   environment block now matches.
5. **The import is clean.** `b_over_m_order_probe` imports
   `plancherel_weight` from `q1_mass_gap_probe` — itself one of the five —
   but that module's q₀ read is inside `main()`, not at module level, so the
   import triggers nothing.
6. **`q0-anchor-consistency-audit.witness.json` was reverted**, not
   committed: its only diff was `invocation.argv` gaining `--strict` from the
   gates wrapper. Drift, not a count change. `q0-value-drift-audit` *is*
   committed, because a count genuinely moved.

The gate now reports **4** contradictions and still exits 1, as it should
while any remain.

The other four are not fixed here. `path4_rho_K_at_h3A` and
`q_beta_form_a_n1_extension` are dual-purpose (`q_inv`, `hbar_q`) and need
their co-read scalars re-pointed in the same change or they straddle;
`q1_mass_gap_probe` needs its reference-table read separated from its q₀ bind
first; `aK_via_lp_dual_hecke_basis` states no pin intent. Tracked in
`qou-v90i`.

## Root cause, traced: a direct reader **cannot** be migrated by re-running it

**Attribution, stated plainly: this is my own defect.** All four commits in
the table below — the 2026-08-15 anchor re-pin that caused `qou-m9xp`, and
the migration batches that manufactured the contradictions — carry
`session_011Xe8o5r85SzhndKso9hXVK`, this session. I wrote the sweep, it
reported progress toward 254, and for the direct-reader class that progress
was partly fictitious. The finding below is not a critique of someone else's
mechanism; it is the bug in mine, found by the audit built to look for it.


The five contradictions are not five independent slips. Tracing
`a-K-via-lp-dual-hecke-basis.witness.json` and the anchor-defining witness
side by side gives a complete causal account:

| date | `q-pinning-50-digit` | the direct reader's witness |
|---|---|---|
| 2026-08-11 `c3a7e16856` | **muon** | stamp `muon`, data muon — consistent |
| 2026-08-15 `9a9c6b31c7` | **proton** ← *re-pinned* | stamp `proton`, data proton — *looks migrated* |
| 2026-08-19 `2e4745448d` | **muon** restored | — |
| 2026-08-19 `da2968cc33` | muon | stamp `proton`, data **muon again** — contradiction |

The 2026-08-15 sweep appeared to migrate these producers correctly. It did
so by re-pinning **`q-pinning-50-digit.witness.json` itself** — the one move
AGENTS.md constraint 1 forbids, and the one that broke `main` for 208
producers (`qou-m9xp`). When `2e4745448d` restored the muon anchor, every
direct reader silently reverted to muon data on its next run, while the
migration kept stamping it `proton` from the manifest.

So the general statement is stronger than "5 producers contradict their
manifest entry":

> **A producer that reads `q-pinning-50-digit.witness.json` directly cannot
> be migrated by re-running it.** Its q₀ comes from the anchor-defining
> witness, which by constraint 1 must remain muon. Re-running therefore
> always yields muon data; stamping it `proton` from the manifest always
> manufactures a contradiction. The only fix is to change the **read**.

This also explains the shape of the earlier count. `path4_rho_K_at_h3A`,
`q1_mass_gap_probe` and `q_beta_form_a_n1_extension` were flipped to
`proton` by the migration batches themselves (`1fead8dd49` "batch to
172/254", `a718727acd` "batch to 192/254") with muon data already in place —
the contradiction was manufactured *by the migration*, in the commits that
report progress toward 254.

`a718727acd` is explicit about what it re-ran: `computedAt` and `durationMs`
moved, `q0Anchor` went `muon` → `proton` and `q0Value` to the proton string,
while the producer's own `q_0_50dps` data field stayed
`1.10997859555733471989976322048322502665620840878015368660798114614493`.
The label and the data are written by independent paths, so re-running moves
one and not the other.

### What this implies for the sweep

The migration's own progress counter cannot distinguish "migrated" from
"re-stamped while still on muon" for this class. Any producer in the 55 that
the sweep marks done is done **only** if its read was changed — and the sweep
does not change reads. `--list-contradictions` is the check that catches it,
and it is currently the only one: the anchor-consistency audit exempts
`-audit`/`-scan` suffixes, and the flip-risk audit keys on witnesses stamped
`muon`, which these are not.

## Two more fixed (2026-08-22), and why the drift audit only saw one

`path4_rho_K_at_h3A` and `q_beta_form_a_n1_extension` both re-pointed to
`q_parameter.Q_MP`. Neither is dual-purpose (see the correction above), so
both were single-read fixes of the same shape as `b_over_m_order_probe`.

- `q_beta_form_a_n1_extension`: the comment being replaced said *"Load CAL-2
  q_0"* — the exact conflation this document already corrects. Its
  replacement says why. 3 assertions still pass; float64 at the baselined 12.
- `path4_rho_K_at_h3A`: `json` and the `_pb` alias became unused and were
  removed (the bare `_path_bridge` import stays — it is the path bridge).
  float64 at the baselined 7.

`scripts/precision-gates.sh` (full run): **all blocking gates green.**
Contradictions **4 → 2**; census 639 → 637.

### The count only moved by 1, and the reason matters

`q0_value_drift_audit` went `canonical` 211 → 210, not 211 → 209. Traced to a
single entry: only `q-beta-form-a-n1-extension`'s `parameters.q_0_50dps`
changed class. `path4`'s fix is invisible to that audit because **it scans
`q0Value` — the stamp — and not `q_pinned`, the field carrying the data.**

That is the same blind spot as the contradiction itself, one level up. A
witness whose *stamp* says proton and whose *data* says muon is counted
`proton-pin` by the drift audit, so the audit structurally cannot see the
contradiction, and its `canonical` count understates the muon population by
however many such witnesses exist. This is why `--list-contradictions`
compares the manifest against the **read**, not against any recorded field.

### Stopping point

Two remain, neither mechanical:

- **`q1_mass_gap_probe`** — genuinely dual-purpose, one of the 3. It reads
  `plancherel_weights_n3` and `two_q` as a reference table *and* binds q₀.
  Separate the two before re-pinning either.
- **`aK_via_lp_dual_hecke_basis`** — registers the pin witness as a **declared
  upstream** (`record_upstream` → `add_upstream_records`). Re-pointing to
  `Q_MP` would replace a file-hash-backed provenance record with a package
  constant. That is a provenance-architecture call, on a producer that states
  no pin intent either, so it is not a change to make unilaterally.

## What this does and does not license

- **It does not authorise the bulk sweep.** The first attempt broke
  `main` for 208 producers (`qou-m9xp`). Constraints 1–4 in AGENTS.md
  §"q₀ anchor convention" rule 4 stand.
- **It does not make the 51 undeclared producers defects.** A producer
  legitimately in the ideal/CAL-2 layer *should* read the muon pin. What
  the measurement shows is that 56 producers pin muon while the manifest
  declares exactly 3 producers `ideal_muon` — the discrepancy is the
  work, and classifying the 51 is the next honest step, not re-pinning
  them.
- **The 5 contradictions are actionable now.** Each is a single-file
  decision: either the manifest entry is wrong or the read is. They do
  not need the sweep.

## Corrected baseline for `qou-1c4y`

| claim | status |
|---|---|
| "~840 muon witnesses" | superseded |
| "624 fingerprint / 65 stamped" (my earlier re-baseline) | **superseded — the 624 conflates two q₀ values** |
| 210 current-muon + 374 superseded-muon + 24 both + 31 rounded | measured 2026-08-22, post-rebase onto `238fc79f6e` |
| 65 stamped `muon` = 3 `ideal_muon` + 11 `physical_proton` + 51 undeclared | measured; the 3 are the legitimately-muon producers |
| 55 producers pin q₀ directly from the muon witness; 4 contradict their own manifest entry | measured, confirmed both directions; was 56 / 5 before the fix below |
