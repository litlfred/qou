# The OLD-MUON (CODATA-2018) witness population: 268 files, 20 of them drainable

Beans `qou-a1lw` (session), `qou-qgnl` (classify), `qou-vn63` (drain).
Harness: [`computations/audits/q0_old_muon_b_witness_triage.py`](../../computations/audits/q0_old_muon_b_witness_triage.py).
Sibling of, and disjoint from, the A-population harness of PR #5519.

## Every count here carries the prefix it was obtained with

Three values are all called "the muon q₀" and they agree to eleven significant
digits, so a ten- or twelve-digit prefix matches all three:

| | value | 13-digit prefix |
|---|---|---|
| **A** | frozen canonical pin | `1.109978595557` |
| **B** | CODATA-2018 lepton-tower derivation | `1.109978595554` |
| **C** | CODATA-2022 derivation | `1.109978595642` |

Measured over the 3170 tracked `computations/**/*.witness.json` on
`cdbdc84af1`, two independent ways (`grep -rlF --include='*.witness.json'`, and
a Python whole-payload scan):

| carries | n |
|---|---|
| A | 149 |
| **B** | **268** |
| C | 55 |
| A and B both | 6 |

**Do not quote any of these without its prefix.** This is the failure this
document exists to avoid repeating: a sibling agent grepped a
non-discriminating prefix, got ~150, and missed two thirds of the B population.

## Boundary with PR #5500 is one file

#5500 owns the A→C anchor migration. Its selector is `q0Anchor == "muon"` AND
`q0Value` starting with A, which is **78** witnesses on this tree — not the 149
that merely *carry* A. Its intersection with the B-population is **exactly
one**: `computations/audits/muon-pin-three-values.witness.json`, the probe whose
subject *is* all three values. Out of scope for both. The two drains are
disjoint at the file level and can run in parallel.

Worth recording for #5500: **B sits in the standardized `q0Value` metadata field
in 1 of 268 cases.** `q0Anchor` is `None` for 255 of them. A selector keyed on
`q0Anchor`/`q0Value` structurally cannot see this population, so "the muon
witnesses" is a narrower phrase than it sounds.

## 215 of the 268 are archived, not stale

**B-population 268 = 215 under `fsh-guts/deprecated/computations/` + 53 live.**

That directory's `README.md` states the deprecation criteria: no content block
consumes them, no audit doc cites them, the body carries no assertions. The
criteria were **verified rather than trusted**, because 115 files under
`content/` and `docs/` do mention one of the 196 basenames unique to
`_deprecated/`. Narrowing to the actual consumption channel — a `.ts` manifest
field — leaves **11 lines**, and the only one naming a unique-to-`_deprecated`
witness is prose inside a string:

    content/quantum-observable-universe/mass-endomorphism/
      conj-rho-k-pair-gen-canonical-form.ts:41:
        "Empirical witness: `rho-k-pair-gen-extension.witness.json`.",

No `computation.witness` field, no `:val[…]` registry entry. So nothing live
consumes a deprecated B witness, and the 215 stay archived.

One trap for anyone re-running this check: **19 basenames exist BOTH in
`_deprecated/` and live elsewhere**, so a basename grep over the whole tree
returns 1412 lines and is useless. Diff the basename sets first.

## The live 53 are not uniformly stale either

B almost never appears as the witness's own `q0Value`; it appears inside the
payload. **Where** it appears is what decides whether the file is stale:

| class | live n | what it means |
|---|---|---|
| `PRIMARY` | 33 | unmarked working q₀ (`parameters.q_0`, `q_0`, `q0`, `q`) — the producer computed at B |
| `MUON-LEG` | 11 | the muon leg of a cross-anchor comparison (`data.q_muon`, `data.anchors.q_muon`) |
| `SCANNER` | 5 | an auditor's witness that contains B because it **found** B in the tree |
| `HISTORICAL` | 4 | the key names it stale/old — **B is the subject** |

### HISTORICAL — regenerating these destroys the measurement

`computations/mp-dk-decisive-test.witness.json` carries
`data.pins.stale_muon_pin_q0 = B` beside `data.pins.canonical_mp_pin_q0`, and
exists to report `data.d4_vs_claim.pct_drift_between_pins = 99.99487` — i.e. to
show that the `d_4 = 46` brane-tower coefficient is a stale-pin artifact
(`46.0229885101` at the stale pin, `0.00236111602403` at the canonical one). B
is its subject. The other three are `per-basis-row-invariants-probe` and the
two `qbeta-multi-block-eigenphase` probes, same shape.

### SCANNER — a correct report, not a stale pin

This class had to be **measured into existence** rather than guessed.
`fitted_labelled_canonical_audit` and `q0_consistency_audit` both came back
`SUBSTANTIVE` with B still present after the re-run. Reading the values
explained why:

    fitted-labelled-canonical-audit : data.rows[].issues[].literal
                                      = '1.1099785955541805'   (quoted FROM source)
    q0-consistency-audit            : hits[].text
                                      = 'q₀_proton = 1.10997858275138…
                                         q₀_muon = 1.10997859555418…'  (a source LINE)

Neither is the producer's own pin. A path-name rule alone kept calling them
`PRIMARY`, which would have reported a scanner's *correct* report as a stale
anchor. They **are** stale — `q0-consistency-audit`'s hit list moved
**253 → 318** — but that is stale audit *output*, a different finding, and must
not be counted as a stale anchor.

### MUON-LEG — real, but it is #5500's substance on files #5500 cannot see

Eleven live witnesses hold B in a field explicitly labelled as the muon anchor
of a cross-anchor comparison (`qbeta_c3_swing_gate_probe` reports
`data.anchors.q_muon = B` beside `data.anchors.q_proton`). B is wrong there —
`qou_substrate.constants.q_muon_at()` returns **C** today, and
`witness._q0_value_for_anchor("muon")` returns C as well — so a re-run moves
them B → C. That is the A→C migration arriving through a side door, on files
#5500's selector does not match. Reported, not drained unilaterally.

## The binding constraint is provenance, not the anchor

| resolution | all 268 | live 53 |
|---|---|---|
| `no-scriptFile` | 131 | 13 |
| `unresolved` — names a `scriptFile` basename that is no longer in the tree | 94 | 2 |
| `unique` | 42 | 37 |
| `ambiguous(2)` | 1 | 1 |

**225 of 268 (84%) cannot be re-run at all.** 210 of those 225 are in
`_deprecated/`, which explains most of it; but 15 live witnesses are in the same
state, 9 of them `PRIMARY`. Two are honest about it — their `scriptFile` field
is prose:

    "(legacy — no matching producer found; provenance pending manual triage)"
    "(deferred — producer not in computations/ tree; see docs/audits/
      2026-05-09-workplan-update-rho-k.md)"

The remaining 13 simply have `scriptFile: null`, including seven
`keystone-*.witness.json`. **No anchor migration fixes any of these** — the
number cannot be recomputed because nothing in the tree knows how it was
computed. Re-running a producer that never emitted provenance would also delete
fields backfilled downstream (the `aoperator_a5_crosscheck` pattern).

## Drain set and outcome

Removing deprecated, `SCANNER`, `MUON-LEG`, `HISTORICAL`, anchor-defining and
legitimately-muon producers, and requiring a uniquely-resolved producer, leaves
**20 witnesses over 19 producers**.

The sweep was run over the pre-`SCANNER` set (22 producers), 300 s budget each,
17.2 min wall:

| verdict | n |
|---|---|
| `SUBSTANTIVE` | 7 |
| `CRASH` | 9 |
| `TIMEOUT` | 3 |
| `UNCHANGED` | 3 |

### Drained: 5

Of the 7 `SUBSTANTIVE`, two are `SCANNER` (see above) and are left for the
audits-tree drain. The five `PRIMARY` ones were re-run and committed, and **B is
gone from every one**:

| producer | B → | fields moved |
|---|---|---|
| `alpha_em/alpha_em_smatrix_perloop_probe.py` | proton | 3 |
| `implied_h2_coefficient_audit_50dps.py` | proton | 19 |
| `probes/delta_coupling_closed_form_probe.py` | proton | 25+ |
| `q_beta_predicted.py` | **A** | 25+ |
| `snappy_cusp_seeding.py` | proton | 25+ |

`q_beta_predicted` is an ideal-layer producer and resolves to the muon anchor,
so B → A is its correct destination rather than a layer straddle.

**The diffs superimpose causes.** Besides the q₀ step (B vs proton differ at
1.15e-8 relative, which is the size of most shifts) they carry
`engineVersion: mpmath 1.3.0 → 1.4.1` on two, `precisionMetadata.compute_dps:
50 → 70` on one, and `m_e_MeV: 0.51099895 → 0.51099895069` on another. Two
movements want a reviewer rather than a nod: `q-beta-predicted`'s `contentBlock`
changed `prop:q-beta-categorical-precision-ladder` →
`rem:beta-decay-energy-scale` and its **legacy** typed-crossings `err_pct` moved
`0.7474 → 1.7463` (the headline `err_pct` barely moves); and
`snappy-cusp-seeding`'s `data.results.2.pairings.4.snappy_index` moved `6 → 5`,
a discrete index rather than a rounding shift.

### The 9 CRASHes are three different things, and only 2 are defects

A nonzero exit is not a defect, so all nine were re-run under the seven
conditions AGENTS.md requires before calling a producer broken: `PYTHONPATH`
set to `computations/` plus the package `python/` dirs, **both** `cwd=repo root`
and `cwd=producer dir`, stdout **and** stderr captured separately, traceback
checked rather than exit code, and the exception type checked against guards the
corpus defines.

**Fixed here (1).** `hardcoded_q0_literal_families_audit.py` — the `SyntaxError`
below. Now `rc=0`.

**Missing upstream artifact — a guard working correctly, not a defect (6).**

| producer | what it refuses on |
|---|---|
| `audits/delta_n2_placeholder_audit.py` | *"Run its producer first."* |
| `audits/deuteron_delta_i_audit.py` | *"Run its producer first."* |
| `build_six_term_substrate_model_b.py` | `FileNotFoundError: Model B T1 witness missing: probe-sdp-canonical-paper-formula…` |
| `d_from_scratch.py` | `FileNotFoundError: habiro-coefficients…` |
| `neutron_error_diagnostic.py` | `FileNotFoundError: atomic-braid-mass-table…` |
| `compound_binding_via_differences.py` | prints `ERROR: atomic-braid-mass-table.witness.json missing`, exits 1, **no traceback** |

`probe-sdp-canonical-paper-formula*` and `atomic-braid-mass-table*` do not exist
anywhere in the tree. These are chained producers; they cannot be drained until
their upstream is regenerated, and that is a separate piece of work.

**Real defects (2), both verified absent rather than assumed.**

- `probes/lambda_scale_homflypt_skein_recursion_probe.py` —
  `ModuleNotFoundError: No module named
  'lambda_scale_alt_g_skein_polynomial_direct'`. That module exists **nowhere**
  in the tree; the only occurrences of the name are three docstring mentions in
  the failing file itself.
- `universal-ilp.py` — `NameError: name 'apply_atom_nf' is not defined. Did you
  mean: 'build_atom_nf'?` at lines 191 and 202. `apply_atom_nf` is defined
  nowhere. **Not repaired here**: Python's suggestion is a different function —
  `build_atom_nf(Z, N)` *builds* a normal form while the call sites are
  `apply_atom_nf(nf, 1, 0)` / `apply_atom_nf(nf, 6, 6)`, i.e. they pass an
  existing `nf` plus `(Z, N)`. Guessing the rename would change what the ILP
  computes. Beaned.

### The 3 TIMEOUTs are UNMEASURED, not unchanged

`audits/term5_aK_audit.py`, `garside-irrep-qvalues.py` and
`qbeta/qbeta_h4_route_a_gate_probe.py` each exceeded the 300 s budget. A timeout
is neither `UNCHANGED` nor `SUBSTANTIVE`; it is an absence of measurement, and
300 s is a **bound**, not a runtime. They need a real runtime measurement under a
budget that lets them finish. Beaned separately.

## A real defect found on the way: three q₀ auditors do not run at all

All three files that declare the `Q0_ROLE = "auditor"` marker place it **above**
`from __future__ import annotations`, which is a `SyntaxError` — the module
cannot be compiled, so the producer cannot run:

    computations/audits/hardcoded_q0_literal_families_audit.py   line 74
    computations/audits/undeclared_muon_pin_flip_risk_audit.py   line 97
    computations/audits/q0_literal_classification_audit.py       line 57

`ast.parse` does **not** catch this (`PyCF_ONLY_AST` skips the future-statement
placement check), which is presumably how it survived: a static check reports
the files as fine. `compile(..., 'exec')` catches it.

The marker is read by a position-independent regex
(`q0_independence_checker.AUDITOR_MARKER`), so moving the declaration below the
future import is safe. Fixed here; all three now reach argparse, i.e. the whole
import cone loads.

Three auditors of the muon-pin register being dead is worth noting beyond the
one-line fix: the register they maintain has not been recomputed for however
long they have been broken.


## What is left, and what nobody can fix

| bucket | n | disposition |
|---|---|---|
| archived under `_deprecated/` | 215 | out of scope, verified unconsumed |
| drained here | 5 | B cleared |
| `SCANNER` | 5 | correct reports; stale *output*, belongs to the audits-tree drain |
| `MUON-LEG` | 11 | B → C on re-run; that is #5500's substance |
| `HISTORICAL` | 4 | must NOT be regenerated |
| missing-upstream guards | 6 | blocked on absent upstream witnesses |
| real producer defects | 2 | 1 fixed (`SyntaxError` ×3 files), 2 beaned |
| unmeasured (timeout) | 3 | beaned with a bound, not a runtime |
| **no producer at all** | **15 live** (+210 deprecated) | **unfixable by any anchor migration** |

The last row is the finding that outlives this branch. Fifteen live witnesses —
nine of them `PRIMARY`, seven of them `keystone-*` — record a number with no
producer that can recompute it. Two say so honestly in the `scriptFile` field
itself; the other thirteen have `scriptFile: null`. Re-running a producer that
never emitted provenance would also delete fields backfilled downstream (the
`aoperator_a5_crosscheck` pattern), so the fix is at the producer, one at a time,
and it is not a sweep.
