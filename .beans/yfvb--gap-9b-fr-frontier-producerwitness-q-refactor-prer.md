---
# yfvb
title: 'gap-9b FR frontier: producer→witness q₀ refactor (prereq) + H_{3A} Borromean FR driver'
status: completed
type: task
priority: normal
created_at: 2026-07-06T04:25:00Z
updated_at: 2026-09-03T20:39:57Z
---

## Context (2026-07-06)

The Step-9b FR-projector compute is now **unblocked** — adding `litlfred/Clarabel.rs`
to session scope cleared the metadata-time 403; the `pyhecke_native` wheel builds
(`maturin build --no-default-features`, rug builds GMP/MPFR from source) and imports.
Recipe + κ-leg formalization landed on PR #3404
(`docs/audits/2026-07-05-gap9b-frprojector-unblock-and-kappa-asymptote.md`).

Two prerequisites remain before the **H_{3A} Borromean per-partition FR test** can
produce a *committable* result:

### Prereq 1 — producer→witness q₀ refactor (the real blocker; bean `tnjb`-adjacent)
`computations/substrate/q_parameter.py` re-exports the **proton-pinned**
`qou_substrate.constants`, but the ~840 committed `computations/*.witness.json` are
**muon-q₀ canonical** (q₀ = 1.10997859555733471…, in `q-pinning-50-digit.witness.json`).
Re-running any producer in this sandbox drifts its witness proton-ward by ~11.5 ppb.

A runtime wrapper that patches `q_parameter.Q/Q_INV/HA` was tried and **FAILED**
(produced an 88× wrong B_MeV): q-derived constants (dim_q/[n]_q tables, χ caches, and
mpf literals whose binary precision depends on dps-at-import) are baked at import time,
so a post-import patch does not faithfully reproduce the canonical compute. The robust
fix is to have producers **source q₀ (and q_inv, ℏ_q) from the q-pinning witness**
rather than `q_parameter.Q`. Owner-gated (touches ~72 producers); scope formalize-first.

### Prereq 2 — new H_{3A} Borromean FR driver (not turn-key)
No existing script runs `fr_pullback` over Borromean **atom words**. `fr_pullback_k3_test.py`
operates on H_3 *knot* words (4_1/5_2/6_1) only. A new driver is needed:
Borromean atom-word construction (A nucleons → 3A strands) → per-partition χ via
`compute_atom_chi_rust` / `pyhecke_native` → fr_pullback weight redistribution → vs B_AME.
A ≤ 4 cheap; A ≥ 5 hours. Author per `compute-author` skill (algebraic preflight,
cross-checks).

### What is already validated (does NOT need redoing)
- Compute unblocked (wheel builds + imports).
- k3 FR result is scientifically sound (partial FR support: 4_1 best 1.55×, paper's
  6_1 NOT best) — the variance ratios are q₀-insensitive at the 11.5 ppb level.
- κ-leg asymptote formalized sorry-free (`QOU/Mass/KappaWritheAsymptote.lean`, PR #3404).

**Order:** do Prereq 1 (owner sign-off) → Prereq 2 driver → run A≤4 → commit muon witness.

## Investigation findings (2026-07-06) — de-risking Prereq 1

Design doc: `docs/audits/2026-07-06-q0-producer-muon-refactor-design.md`. Key traps found:

- **The canonical q₀ matches NEITHER current code path.** Committed witnesses use
  `q-pinning-50-digit.witness.json` q = 1.10997859555733471…; `q_at()` is proton
  (…8275138), `q_muon_at()` is a *different* muon closed form (…5541806, differs at
  digit ~11). **The witness is the only faithful source — do NOT recompute via q_muon_at.**
- **Closure trap:** `q_int`/`log_q`/`q_int_err` close over `qou_substrate.constants`'
  proton globals; a `q_parameter.Q` override does NOT fix them (13 scripts use `q_int`).
  The override must re-define these too.
- **≥22-constant family** (f64 + `_MP` + `Q_50_DIGIT_STR`) must be re-derived consistently;
  a partial patch gave an 88× B_MeV error.
- **`mass_at_3A_proper`** is a second choke point (re-exports Q).

**Merge gate:** requires a full re-run+diff sweep of ALL producers vs committed witnesses
(provenance-drift-filtered) — NOT sample-validatable; a missed constant silently corrupts
the canonical layer. Focused-session task with the harness in the design doc.


## CLOSE-OUT 2026-09-03 (arc update)

Closed as **superseded**, not delivered-in-full. Both legs resolved, neither
by this bean finishing its original scope.

**Leg 1 — producer/witness q0 refactor (the ~72-producer prereq): DISSOLVED.**
load_q_50dps() flipped to the proton default on 2026-08-22 (bean qou-dkm2), so
'witness q0' and 'runtime proton q' are now the same anchor and the
inconsistency this leg existed to fix no longer exists. The bean's Prereq-1
finding (committed atom-chi caches sat at the runtime proton q) was TRUE when
measured 2026-07-06 and is preserved as dated historical data in the driver's
witness. Its assertion committed_atomchi_is_proton_q was RETIRED today: its
second clause (visible drift at the witness q0) can no longer be satisfied by
any input, so it could only ever FAIL. The broader migration continues under
qou-1c4y / qou-6p3b.

**Leg 2 — H_3A Borromean FR driver: RAN, refuted-(a), now ABSORBED.**
The beta_Bor FR proxy trimmed the light-series spread only 1.190 -> 1.142 and
lost to the 4_1 proxy (1.1355), so 'the nucleon's own knot supplies the weight'
failed on its own terms. Stronger later work subsumes it: the per-lambda
Delta_lambda VALUE was proved 2026-08-02 (sorry-free), and the 2026-08-30
cheat-sheet banner relocates the gate to the assembly functional — no per-block
weight can turn an intensive quantity into an extensive one.

**Why this sat in-progress for two months:** the deliverables were committed to
claude/cheat-sheet-derivation-gaps-0ykco4 AFTER PR #3440 merged, stranding four
commits (tip 3409f9df39) that never reached main. Restored today, with
supersession banners.

**Live residue, tracked separately:** the balanced-convention normalization
finding (dim_q^2/[n]_q! is not a probability measure; c_n up to 1.517 at H_12),
still unregistered in the trace-convention registry.
