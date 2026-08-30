---
# qou-nsih
title: 'OWNER-AUTHORIZED SWEEP: excise convention C in python AND rust, everywhere'
status: todo
type: task
priority: normal
created_at: 2026-08-30T06:53:56Z
updated_at: 2026-08-30T09:52:14Z
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


## 2026-08-30 — TRANCHE 1 ATTEMPTED AND REVERTED: the migration is not mechanical

First real migration target: `compound_shift_nf.py:256` (`tr_m_weights_mp`), a
production module with a committed witness and a downstream audit doc
(2026-05-16-compound-shift-nf-impl.md), using z_C as THE Markov parameter with
no comparison framing.

### Method

Baseline first. The container was missing scipy and clarabel and had mpmath
1.3.0 against the witness's 1.4.1 -- and the PRODUCER DETECTED THIS ITSELF:

    environment: the environment block records LESS than the witness on disk --
    dropped clarabel; downgraded mpmath 1.4.1 -> 1.3.0. If this container is
    simply missing a library, install it and re-run rather than committing the
    weaker record; the numbers can be identical while the provenance silently
    degrades.

Installed all three; the clean baseline then reproduced the committed witness
byte-identically on substantive fields, 19/19. That is what made the comparison
below trustworthy -- without it I would have been diffing my container against
the corpus.

### Result: 19/19 STILL PASS, and 95 substantive fields MOVE

    /data/atoms[0]/categorical_mass   0.2903  ->  0.4442     (+53 %)
    /data/atoms[0]/y0_star           -0.7985  -> -2.8593     (3.6x)
    /data/atoms[0]/x_star[1..2]      -0.0457  -> -0.3333     (7.30x)
    /data/atoms[2]/x_star[1..2]                               (7.24x)
    /data/atoms[5]/y_star[0]                                  (6.22x)

**Assertions passing is NOT reassurance here.** They are structural (per-nucleon
linearity, the alpha_EM chain) and hold under either convention, while every
reported LP dual and shadow price moves by factors of 3-7. y0_star and y_star[i]
are the binding-energy shadow prices AGENTS.md calls first-class infrastructure.

### Why I reverted rather than committed

I have NO independent check that the D numbers are RIGHT. The probe verifies
internal consistency, not the correctness of the convention choice. Committing
would rewrite 95 published numbers on the strength of "assertions still pass",
which is exactly the reassurance that does not hold. Left uncommitted it risked
being swept up by a later auto prepare-merge, so the code is reverted and this
record stands in its place.

### A separate possible defect, NOT conflated with the migration

`tr_m_weights_mp` returns weights [1, z, z, z^2, z^2, z^3]. The Ocneanu value on
H_3's longest element is z(h z + 1), not z^3. If that is wrong it is wrong under
BOTH conventions, and migrating would carry it forward. Cheap to settle and it
could invalidate the migration either way, so it should go first.

### Consequence for the tranche

The remaining ~20 are the same shape: each rewrites published numbers, and
"assertions pass" will keep being true while they do. This needs either a
per-file review of the movement, or the D-frame derivation (qou-cds1) to give an
independent check. Raised with the author.


## Re-triage on the post-trace-fix baseline (2026-08-30)

50 blocking sites in convention-c-value-audit. Layered triage:

  27  ANNOUNCE THEMSELVES as C-vs-D comparisons (filename `*_C_vs_D_*` /
      `*convention_d*`, a scope literally named `z_C`, or co-bound with z_D).
      These need LEDGER ROWS, not migration.
   9  of the remaining 23 DECLARE convention C in a comment or docstring
      within 25 lines of the binding (`qbeta_ck_cache` is reached only via an
      explicit --historical-convention-C flag and refuses otherwise).
  14  silent locally.

Of the 14, spot-reading found several are NOT migration candidates at all.
They are THEOREMS WHOSE SUBJECT IS z_C:

  - qbeta_z_bar_parity_fmap_class_probe asserts "z = sqrt(q)/(1+q) is exactly
    bar-even". For z_D, bar(z_D)/z_D = q^-4 != 1, so the claim is FALSE, not
    merely different. Its Lean companion QOU/QBeta/ZBarParity.lean is C-frame.
  - qbeta_prearchimedean_z_recursion proves the ODE (4+6w+2w^2)z' + wz = 0,
    which z_C satisfies and z_D does not.
  - qbeta_t3_carrier_q1_order_preflight asserts z - 1/2 vanishes at q=1 to
    order exactly 2, a fact about z_C's expansion.

Substituting z_D there does not fix a defect -- it deletes the statement. This
is the same shape as the owner's challenge on the earlier tranche
("migrating its z_C would delete the proof --> why?"), and it generalises: the
excision sweep cannot reach any site where z_C is the SUBJECT rather than a
parameter. Those belong to the convention-D re-derivation (qou-cds1).

So the actionable migration surface is materially smaller than 50 and probably
smaller than the ~20-25 estimated. Next step is to finish reading the 14 and
split them into (i) parameter sites, migratable; (ii) subject sites, -> cds1;
(iii) comparison sites, -> ledger.
