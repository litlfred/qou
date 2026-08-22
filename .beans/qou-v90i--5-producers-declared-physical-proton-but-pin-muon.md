---
# qou-v90i
title: 5 producers declared physical_proton but pin muon — disposition is per-file, not mechanical
status: todo
type: task
priority: normal
created_at: 2026-08-22T19:37:16Z
updated_at: 2026-08-22T20:50:22Z
---

Found while re-baselining `qou-1c4y`; measurement +
`computations/audits/q0_muon_population_partition.py --list-contradictions`,
audit `docs/audits/2026-08-22-q0-migration-worklist-partition.md`.

Five producers are declared `physical_proton` in `q0_anchor_manifest.json`
yet bind q0 straight out of the **muon-anchored**
`q-pinning-50-digit.witness.json`, never importing `q_parameter`. Confirmed
in both directions: the emitted witness is stamped `q0Anchor: proton` while
recording the muon value.

## The disposition is NOT uniform — this is why the sweep needs judgement

| producer | evidence | disposition |
|---|---|---|
| `b_over_m_order_probe` | docstring: *"Computed at the **proton-pinned** q₀"* | **read is the bug** — intent is proton |
| `path4_rho_K_at_h3A` | compares against proton/neutron `ρ_K_CODATA`; experimental-layer | **read is the bug** (docstring also carries the `1.1097859` rounding) |
| `q_beta_form_a_n1_extension` | comment: *"Load **CAL-2** q_0 from canonical pinning witness"* | **MANIFEST is the bug** — CAL-2 *is* the ideal muon layer; the code is right |
| `q1_mass_gap_probe` | reads the witness as a **reference table** (`plancherel_weights_n3`, `[2]_q`) AND binds q0 from it; `:170` comments "(proton anchor)" | **mixed** — table read legitimate, q0 bind is the bug |
| `aK_via_lp_dual_hecke_basis` | "H_3 (proton, neutron)" names the *particle*, not the pin; no pin statement | **ambiguous** — needs a call |

## Why this matters beyond the five

A mechanical "re-pin everything declared `physical_proton`" would have
**broken** `q_beta_form_a_n1_extension`, which deliberately wants the
ideal CAL-2 pin. That is the same class of failure as `qou-m9xp` (the
first sweep attempt, which broke main for 208 producers). Two of five
here need the *manifest* changed or a human call, not the code — so the
per-file read is load-bearing, not ceremony.

## Next

1. Fix the two clear read-bugs (`b_over_m_order_probe`,
   `path4_rho_K_at_h3A`): route through `q_parameter`, re-run, refresh
   the witness. Precision preflight per AGENTS.md before commit.
2. Fix the manifest entry for `q_beta_form_a_n1_extension`
   (`physical_proton` -> `ideal_muon`).
3. `q1_mass_gap_probe`: separate the two reads — keep the reference-table
   read, bind q0 via `q_parameter`, drop the wrong "(proton anchor)"
   comment at `:170`.
4. `aK_via_lp_dual_hecke_basis`: needs an owner/author call on which layer
   it belongs to.

Gate: `--list-contradictions` exits 1 while any remain, so it can be
wired into a preflight once drained.


## CORRECTION (same session) — the `q_beta_form_a_n1_extension` row was wrong

I read its comment *"Load **CAL-2** q_0 from canonical pinning witness"* as
a deliberate ideal-layer choice and called the manifest the bug. Wrong.

AGENTS.md §"q₀ anchor convention" states the 2026-08-07 directive *"is about
which **numerical evaluation** code defaults to, not about redefining the
3-CAL triple"* — the ideal CAL-2 definition is untouched while **compute
evaluates at the proton pin**. Naming CAL-2 identifies *which calibration*,
not *which pin*. The manifest entry is correct; the read is the bug.

Corrected: **three** plain read-bugs (`b_over_m_order_probe`,
`path4_rho_K_at_h3A`, `q_beta_form_a_n1_extension`), one **dual-purpose
read** (`q1_mass_gap_probe`), one with no stated intent
(`aK_via_lp_dual_hecke_basis` — directive default applies, no call needed).

**My "a sweep would have broken this one" argument does not survive** in the
form I wrote it. Re-pinning `q_beta_form_a_n1_extension` to proton is the
*correct* action.

What survives is narrower and real: `q1_mass_gap_probe` reads
`q-pinning-50-digit.witness.json` for **two** purposes — its q₀ bind *and*
its recorded `plancherel_weights_n3` / `[2]_q` as a cross-check reference
table. A naive re-pin that redirects the whole read fixes the first and
breaks the second. The sweep hazard is **dual-purpose reads**, not
layer-intent conflicts.

### Revised next steps

1. Three read-bugs: route q₀ through `q_parameter`, re-run, refresh witness.
   (`q_beta_form_a_n1_extension` re-runs in <180s, exit 0, and is
   mathematically byte-identical on re-run — its 12 raw-float64 fields are
   already baselined at exactly 12, so the ratchet is satisfied. It also
   carries a pre-existing float64 defect worth a separate bean.)
2. `q1_mass_gap_probe`: split the two reads before re-pinning either.
3. `aK_via_lp_dual_hecke_basis`: apply the directive default; no author call
   needed after all.


## FIXED 1 of 5 (2026-08-22) — `b_over_m_order_probe`

The cleanest case: declared `physical_proton`, docstring says *"Computed at the
**proton-pinned** q₀"*, single q₀ read, and **not** among the 21 dual-purpose
readers, so no co-read scalars to straddle.

Read now goes through `q_parameter.Q_MP` — the proton pin at the **same 50 dps**,
verified not a downgrade before the swap. Witness gained `q0_anchor`.

Verification:
- `q0_50dps` 1.10997859555733471… -> 1.10997858275138080…;
  `q0_value_drift_audit` reclassified `canonical` -> `proton-pin` at
  `ppb_vs_canonical: -11.537117889987831` — the μ–p tension, the right magnitude.
- **Conclusion unchanged**: `n6_family_splitting_at_q0` moved in the 9th
  significant digit. This is an order-of-magnitude probe; the fix corrects
  *which pin it declares*, not any finding.
- `scripts/precision-gates.sh --changed`: **all blocking gates green**.
- **Environment restored first.** The initial run warned this container recorded
  LESS than the committed witness (`clarabel` dropped, `mpmath` 1.4.1 -> 1.3.0).
  Installed both and re-ran rather than commit weaker provenance.
- Import is clean: it imports `plancherel_weight` from `q1_mass_gap_probe`
  (another of the five), but that module's q₀ read is inside `main()`, so the
  import triggers nothing.
- `q0-anchor-consistency-audit.witness.json` **reverted** — its only diff was
  `invocation.argv` gaining `--strict` from the gates wrapper. Drift.
  `q0-value-drift-audit` committed, because a count genuinely moved.

Gate now reports **4** contradictions, still exit 1. Census 640 -> 639.

### Remaining 4 — why each is NOT a one-liner

- `path4_rho_K_at_h3A` + `q_beta_form_a_n1_extension`: **dual-purpose**
  (`q_inv`, `hbar_q`). Re-pointing only the `["q"]` read leaves the derived
  scalars on muon — a straddle inside one producer.
- `q1_mass_gap_probe`: reads the witness as a **reference table**
  (`plancherel_weights_n3`, `[2]_q`) *and* binds q₀ from it. Separate the two
  before re-pinning either.
- `aK_via_lp_dual_hecke_basis`: states no pin intent; directive default applies,
  but it has no docstring to confirm against.


## ROOT CAUSE TRACED (2026-08-22) — a direct reader cannot be migrated by re-running it

The five are not independent slips. Tracing `a-K-via-lp-dual-hecke-basis`
against the anchor-defining witness:

| date | `q-pinning-50-digit` | the reader's witness |
|---|---|---|
| 08-11 `c3a7e16856` | **muon** | stamp muon, data muon — consistent |
| 08-15 `9a9c6b31c7` | **proton** ← *re-pinned* | stamp proton, data proton — *looks migrated* |
| 08-19 `2e4745448d` | **muon** restored | — |
| 08-19 `da2968cc33` | muon | stamp proton, data **muon again** — contradiction |

The 08-15 sweep appeared to migrate them correctly **only because it re-pinned
`q-pinning-50-digit.witness.json` itself** — the move AGENTS.md constraint 1
forbids, and the one that broke main for 208 producers (`qou-m9xp`). When
`2e4745448d` restored the muon anchor, every direct reader reverted to muon
data on its next run while the migration kept stamping `proton`.

**General statement:**

> A producer that reads `q-pinning-50-digit.witness.json` directly **cannot be
> migrated by re-running it.** Its q₀ comes from the anchor-defining witness,
> which by constraint 1 must stay muon. Re-running always yields muon data;
> stamping it proton from the manifest always manufactures a contradiction.
> **The only fix is to change the read.**

Three of the five were flipped to `proton` **by the migration batches
themselves** (`1fead8dd49` "batch to 172/254", `a718727acd` "batch to
192/254") with muon data already in place. `a718727acd` moved `computedAt`,
`durationMs`, `q0Anchor` muon->proton and `q0Value` to the proton string, while
the producer's own `q_0_50dps` stayed muon. Label and data are written by
independent paths.

**Implication:** the migration's progress counter cannot distinguish
"migrated" from "re-stamped while still on muon" for this class.
`--list-contradictions` is currently the only check that catches it — the
anchor-consistency audit exempts `-audit`/`-scan` suffixes, and the flip-risk
audit keys on `muon`-stamped witnesses, which these are not.


**Attribution.** All four commits in the trace above — the 08-15 anchor re-pin
(`9a9c6b31c7`, the `qou-m9xp` cause), `da2968cc33`, `1fead8dd49`,
`a718727acd` — carry `session_011Xe8o5r85SzhndKso9hXVK`, **this session**. I
wrote the sweep; it reported progress toward 254; for the direct-reader class
that progress was partly fictitious. Recording it as mine, not as a critique of
someone else's mechanism.
