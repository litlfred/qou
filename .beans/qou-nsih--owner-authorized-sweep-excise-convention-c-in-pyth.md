---
# qou-nsih
title: 'OWNER-AUTHORIZED SWEEP: excise convention C in python AND rust, everywhere'
status: todo
type: task
priority: normal
created_at: 2026-08-30T06:53:56Z
updated_at: 2026-08-30T08:18:46Z
---

## Measured 2026-08-30 — the surface, before any edit

Owner instruction, verbatim: *"Excise convention C in python and rust and
wherever you see it."* That supersedes the standing caution in AGENTS.md
against launching a corpus-wide sweep off the recorded counts — but the counts
below are freshly measured, not quoted.

### Python — 93 blocking sites

`scripts/convention-c-value-audit.py` (the VALUE audit, which evaluates each
binding at two sample points rather than matching its shape, so it sees the
sqrt-variable disguise the shape audit is blind to):

    BLOCKING — confirmed convention C, unadjudicated   93
    ADJUDICATED as comparisons (ledger)                 1
    UNRESOLVED — variable name not recognised           2
    NOT C — 1/[2]_q on a q-variable                      3

The 2 unresolved are real C in a spelling the audit cannot name:
  - computations/probes/toffoli_qand_convention_d_derivation.py:185  (var `_s`)
  - computations/qbeta/qbeta_braid_image_eigenphase_exclusion_probe.py:134 (`ss`)

The 3 "NOT C" are 1/[2]_q on a q-variable — correctly excluded, do not touch.

### Rust — essentially already D

  tools/hecke-engine/src/main.rs:82        z: q*q*q/(q*q+1.0)   -> D
  tools/hecke-engine/src/bin/h9_beta.rs:76 z: q*q*q/(q*q+1.0)   -> D
  tools/hecke-engine/src/archive/v2.rs:205 z: 1/(sqrt q+sqrt qi) -> **C**, in archive/

One C site, and it is in `archive/`. All language bindings
(hecke-engine-{c,node,jvm,julia,gap,octave}) are clean; the Octave one is
explicitly labelled `// z = q^3 / (q^2 + 1), trace convention D`.

### Discipline for the sweep

Per AGENTS.md's own record of how this has gone wrong before: migrate
site-by-site, never by relabelling a manifest; NEVER touch an anchor-defining
witness; a producer that holds C as a DELIBERATE comparison stays (the ledger
has 1 such); and re-run the value audit rather than the shape audit to check
progress — the shape audit reported 26 where the value audit reports 93, and
21 of those were invisible to it entirely.

## 2026-08-30 — CORRECTION: 'INERT' does NOT mean safe to migrate, and there are ZERO measured-safe targets

I reported the 2 INERT sites as 'the safest migration targets, the only ones
where I have positive evidence that nothing moves'. **That was wrong twice.**

### 1. qbeta_utils.py:248 — the verdict is a HARNESS ARTIFACT

The module has **no `__main__`**. Running it standalone executes imports and
nothing else, so 'output identical' measured precisely nothing. It has **82
importers**. This is the measuring-my-own-harness failure for the third time
this session.

And the site must not be migrated on its merits either: it sits inside
`if convention == 'C':` — reachable only by asking for C by name — and carries
a documented bit-exactness reason for its exact spelling:

    the two spellings are algebraically equal but NOT bit-equal --
    1/(sqrt q + 1/sqrt q) against sqrt(q)/(1+q) differ by 1.6e-61 relative at
    60 dps -- and this is the one ladder that must not be perturbed by a
    substitution, however small

### 2. qbeta_phase_bar_parity_completeness_probe.py:105 — verdict REAL, reading wrong

Hand-verified: output is byte-identical under substitution. But that is not
evidence the migration is safe. `z_C` feeds `a_C`, which the file's own
docstring contrasts against `a_D_odd`; it IS a comparison arm whose contrast
the printed output happens not to expose.

### The general correction

**INERT means 'this probe's own output cannot detect the substitution', NOT
'the substitution is harmless.'** So the count of measured-safe migration
targets is **0, not 2**.

Note the ASYMMETRY, which does hold: COMPARISON_ARM is a POSITIVE detection --
assertions actually flipped -- so those 23 adjudications stand. It is the
NEGATIVE verdicts (INERT, and by the same argument DISCRIMINATES) that carry no
safety guarantee. A harness like this can confirm load-bearing; it cannot
certify harmless.

### What the INERT signal DID find

Chasing why the output could not move surfaced a real defect in that probe --
two assertions that cannot fail. Filed separately.

## 2026-08-30 — the remaining 53, classified by reading every one

93 -> 53 so far (41 ledger entries + 1 dead binding removed). The co-bound set
is drained; what remains is a different population, and reading it changes the
estimate again.

### The 53 break down as

  ~15  named `z_C` / `z_of` FUNCTIONS whose scope IS the C arm, in files often
       named *_C_vs_D_* — binding_closed_form_C_vs_D:94,
       binding_production_route_C_vs_D:84, binding_sum_C_vs_D_per_isotope:118,
       binding_channel_convention_exposure:109, mu3_door_sign_C_vs_D:90,
       toffoli_diagonal_convention_frame:61, qbeta_F_coordinate_bridge_audit:65,
       qbeta_d_frame_ladder_structure:83, qbeta_decay_channel_convention_status:79,
       qbeta_h_vs_u_frame_stability:80, qbeta_ladder_required_phase:72,
       qbeta_zcd_classical_coincidence:113, mayer_threebody_sign_threshold:74,
       markov_stab_trace_axis:130, gram_h3_symbolic_regression:72

   2   explicitly historical and self-labelled —
       schur_principal_mpmath:123 in `_wenzl_constants_convention_C_HISTORICAL`,
       ocneanu_param_from_fibre_dimension:178 `# EXCISED — audited here, not used`

   1   GUARDED DISPATCHER, and it is the one that looked most dangerous:
       qbeta_ck_cache.py:140 — the canonical c_k extractor. Reachable ONLY via
       an explicit --historical-convention-C flag, behind
       `if convention != "C": raise`, with the reason stated in place: "this
       path exists solely so the committed witness stays machine-reproducible,
       and it is never the default". NOT a defect. 11 importers.

   3   my own probes from this session, deliberately C-frame and documented as
       such (the c_3 extraction is DEFINED in C, so its probe must evaluate there)

 ~20-25  genuinely computational, no comparison framing — the real remaining
       targets. compound_shift_nf:256 (tr_m_weights_mp),
       markov_trace_weights_wenzl:254/457 (markov_trace_s),
       gram_h3_det_factorization:55, probe_markov_trace_ratio_exact:87,
       qbeta_c3_barodd_hs_matrix_resolvent:86, qbeta_c3_cross_anchor_exactness:55,
       qbeta_eta_singularity:180, qbeta_eval_map_bar_decomposition:48,
       qbeta_h_frame_rungs:73, qbeta_prearchimedean_z_recursion:103,
       qbeta_t3_carrier_q1_order_preflight:68, qbeta_z_bar_parity_fmap_class:72,
       and others.

### The estimate has moved twice, both times downward, both times on reading

  93 blocking -> ~36 "genuine" (co-bound triage) -> ~20-25 (reading the rest).

Each narrowing came from looking rather than from a heuristic, and each time the
heuristic would have over-counted. Do not quote 93 as a defect count.

### The next tranche is materially harder than everything so far

These ~20-25 CHANGE NUMBERS. Each needs its producer re-run, its witness
regenerated, and its recorded conclusions re-checked — and several sit in the
qbeta decay channel where qou-cds1 forbids substitution outright (a z-swap is
not a re-derivation). Expect the honest outcome for some of them to be "cannot
migrate by substitution; needs the D-frame derivation first", i.e. blocked on
qou-cds1 rather than on effort.
