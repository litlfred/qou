---
# qou-6p3b
title: 'qfac/dim_q threading: 12 decisions, not 133 edits (scoped)'
status: todo
type: task
priority: normal
created_at: 2026-08-24T14:15:32Z
updated_at: 2026-08-24T20:43:46Z
---

## Scoped 2026-08-24 — full analysis in docs/audits/2026-08-24-qfac-dimq-threading-scope.md

Follow-on to `qou-wee5` (closed, #5646). **The site count is the wrong unit.**

### Measured (main @ b134176d93)

    191 call sites; 47 already pass q; 144 defaulted
    -11 generated qou-mass mirror (regenerated, never hand-edited)
    = 133 LIVE in 67 files -> 114 in producers, 19 in library modules

Producer sites by their own manifest bucket: 85 unlisted (->proton),
28 physical_proton, **1 ideal_muon**.

### The reframe

The anchor is a property of the RUNNING PROCESS, not the file. Threading
`Q0_PROTON` is **inert wherever the entry point already resolves proton — 113
of the 114 producer sites.** Those edits change no number today.

Real cost = entry points that can resolve muon AND reach these functions:
**12 muon producers.** And **11 of the 12 reach them INDIRECTLY**, via
`mass_at_3A_proper` / `hecke_characters` — only
`qbeta_hoefsmit_tbeta_matrix_build_probe.py:124` calls `dim_q` directly.

**So editing 133 call sites would leave the 11 exactly as they are.**

### Known failure mode, already paid for

Forcing proton on a deliberately-muon producer creates a NEW straddle. Measured
in #5634: `vhat_per_crossing_chain` moved 17 fields and flipped its own
`scalar_vs_matrix_agree` True -> False. It and `he3_tritium_cosh_asymmetry_diagnosis`
were reverted to their own q, then moved 0. **2 of the 12 are confirmed
deliberately muon; the other 10 are unadjudicated.**

### Recommended: B -> A -> C

- **B (API):** optional forwarding `q` on `mass_at_3A_proper` /
  `hecke_characters` entry points, using the backwards-compatible shape proven
  in #5646. Required before A is even expressible for the 11.
- **A (12 decisions):** per producer — deliberately muon (pass its own q) or
  accidentally muon (migrate + regenerate)? 14 witnesses in scope. ALL the
  judgement lives here. **Sequence behind #5500** (muon anchor -> CODATA 2022,
  audit red, 53 witnesses) — it collides directly.
- **C (113 inert sites):** mechanical, expect 0 fields moved, batch-sweep
  exception applies. **Buys no correctness today** — purely preventative against
  a producer later joining `ideal_muon`. Worth doing or not is a judgement call,
  and should be made as one rather than assumed.

### Not claimed

Nothing straddles today — the gate is green (clean=8 / STRADDLE=0). And which of
the 10 unadjudicated producers is deliberate is exactly what must not be guessed.


## Tranche A adjudicated — it is 7 decisions, not 10, and now 2/2/3 (2026-08-24)

### Three were already settled in AGENTS.md, not open at all

§q0-anchor-convention (~line 2023) names three producers that **refuse a proton
run by design**: `atomic_tr_m_mpfr_50dps` (dual-layer, one witness per layer),
`he4_stage2_ranking_seminormal_xcheck` (asserts the muon prefix off the
anchor-defining witness), `cross_check_trM_1ppb` ("L1 cross-check must run under
the MUON q0 pin"). An independent evidence scan flagged the same three before I
read that passage.

Plus the two measured deliberate in #5634 (`vhat_per_crossing_chain`,
`he3_tritium_cosh_asymmetry_diagnosis`). **5 of 12 settled; 7 open.**

### The 7, measured under an anchor flip — RUN TWICE, identical both times

| producer | verdict | disposition |
|---|---|---|
| `lever1_binding_habiro_single_element_test` | **clean** | MIGRATE — listing is inert |
| `gg_production_bond_probe` | **NO-WITNESS** | MIGRATE — writes nothing, no artifact consequence |
| `aoperator_a5_crosscheck` | **STRADDLE, 13 fields incl `/allPassed`** | **HOLD** |
| `qbeta_hoefsmit_tbeta_matrix_build_probe` | **STRADDLE, 3 fields at `/…/dim_q`** | **HOLD** |
| `binding_via_interface_knot` | TIMEOUT 240s | UNTESTED — needs a longer budget |
| `block_swap_binding` | TIMEOUT 240s | UNTESTED |
| `gram_norm_binding_probe` | TIMEOUT 240s | UNTESTED |

Run 1 spanned a branch switch while Tranche C was modifying `hecke_characters`
— the module `qbeta_hoefsmit`'s moving `dim_q` field comes from — so it was
re-run on the committed tree. **Identical, verdict for verdict and count for
count.** The risk was real to flag and did not materialise.

### The correction this measurement forced

I had recommended migrating SIX on header evidence — none of the seven mentions
muon or cross-anchor comparison, and binding is scale-cancelling. Measurement
says `aoperator_a5_crosscheck` flips `/allPassed`, a BOOLEAN ASSERTION, under
the anchor. That is the `vhat_per_crossing_chain` signature exactly.

**Header silence is not evidence of accidental listing.** Migrating it would
have broken a producer's own consistency check — the same failure #5634 already
paid for once.

### Defensible action

**Migrate 2, hold 2, measure 3** — not "migrate 6". Still sequenced behind
PR #5500 (muon anchor -> CODATA 2022, audit red, 53 witnesses), which touches the
same witnesses.


## CORRECTION: the anchor-flip verdicts on 5 of the 7 were UNSOUND (2026-08-24)

I ran all seven through `anchor_flip_straddle_audit` **by explicit path**, which
bypasses the `--candidates` selector. That selector exists to enforce the
audit's own stated precondition — *sound only for producers with a q of their
own*. I quoted that precondition in the tool and then did not apply it.

Measured, do these producers have an INDEPENDENT q (not the manifest-resolved
shim)?

| producer | q source | audit sound? |
|---|---|---|
| `aoperator_a5_crosscheck` | shim only | **NO** |
| `binding_via_interface_knot` | **no q at all** | **NO** |
| `block_swap_binding` | shim only | **NO** |
| `gg_production_bond_probe` | shim only | **NO** |
| `gram_norm_binding_probe` | shim only | **NO** |
| `lever1_binding_habiro_single_element_test` | independent | yes |
| `qbeta_hoefsmit_tbeta_matrix_build_probe` | independent | yes |

**A producer whose only q is the manifest's cannot straddle** — there is no
second layer to mix. Its numbers move under an anchor flip because you changed
its one and only anchor. That is a RE-PIN, which is trivially true, not a
defect.

### What survives

- `lever1_binding_habiro_single_element_test` — **clean**, and the verdict is
  sound. MIGRATE, free.
- `qbeta_hoefsmit_tbeta_matrix_build_probe` — **STRADDLE at `/…/dim_q`**, sound.
  HOLD. This is the one real straddle in the set.

### What was wrong

- `aoperator_a5_crosscheck` "STRADDLE, /allPassed flips" is **NOT a straddle**.
  `/allPassed` is `all(a["passed"] …)`; with no independent q, the flip means an
  assertion whose EXPECTED side is anchor-independent while its computed side is
  not. Still a concrete reason to HOLD it — just a different defect class, and
  the hold now rests on the right evidence.

### What this saved

I was about to spend HOURS measuring the three TIMEOUT producers. One leg of
`binding_via_interface_knot` alone exceeded 1700 s without finishing. **The
measurement could never have answered the question** — all three lack an
independent q, so the instrument does not apply to them. Killed the run.

### Disposition for the 5

Pure policy: should they be muon-pinned? **No straddle risk either way**, because
none has a second layer. `aoperator_a5_crosscheck` should still be held for its
assertion. The other four are free to migrate on the directive alone, with the
usual per-producer witness diff.
