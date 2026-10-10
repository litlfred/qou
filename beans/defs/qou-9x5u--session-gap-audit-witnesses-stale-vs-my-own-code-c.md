---
# qou-9x5u
title: 'SESSION GAP AUDIT: witnesses stale vs my own code changes, no PR, Lean-first directive violated, cheat sheet untouched'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T12:33:24Z
updated_at: 2026-10-04T15:13:55Z
---


Branch: claude/anchor-followups-2026-08-08, 38 commits ahead of main. Written
after the owner asked "did you make feature branch and PR and lean prove all
assertions? follow AGENTS.md" and "review the discussion -- are you missing
things". Yes. Several.

## P0 -- I INTRODUCED WITNESS STALENESS AND NEVER REGENERATED

The worst one, and it is self-inflicted. I changed two widely-consumed modules
AFTER the wave5 regen sweep ran, and regenerated NOTHING downstream:

  computations/mass_binding_dashboard.py::_bond_type_L
      z switched C -> D, AND the writhe term wired in (commit 0f608066).
      Bond energies moved: B_pp 2.907->2.542, B_pn 3.890->2.833, B_nn 5.178->3.307.
  computations/coulomb_energy.py
      alpha_EM CODATA -> derived (a188542f); nuclear length r0=1.2 -> CAL-3
      lambdabar_pi (9a1d7680). E_C(3He) 0.998413 -> 0.847422, a 15 % move.

Consumers found, several of which ARE producers writing witnesses:
    coulomb_energy        <- deltalambda/mirror_split_continuum_em_probe.py (3x WitnessBuilder)
                             binding_wn_kernel_derive_refute.py (2x WitnessBuilder)
                             deltalambda/deltalambda_coulomb_mirror_split_probe.py
                             gap2_borromean_triple_count.py
    mass_binding_dashboard <- probes/coulomb_mirror_killswitch_probe.py
                              probes/clambda_shape_invariant_probe.py
                              probes/su4_occupancy_binding_probe.py
                              probes/charge_symmetry_bond_probe.py

So committed witnesses now disagree with the code that produces them. This is
EXACTLY the staleness wave5 exists to detect, introduced after wave5 ran. Must
re-run those producers through witness_regen_wave --only, in dependency order,
on a clean tree, and adjudicate the diffs.

## P0 -- NO PR EXISTS

38 commits, zero review. AGENTS.md:50 wants related work combined into ONE
branch / ONE PR -- the branch is right, the PR was never opened. Also never
posted the intent comments AGENTS.md:40 asks for on overlapping sibling PRs.

## P0 -- AGENTS.md:779 VIOLATED THROUGHOUT

  "For any new math or physics derivation, agents MUST begin by writing the Lean
   structure, class, or proof scaffold in .lean files. Explicitly forbidden:
   agents must NOT start with Python fitting scripts or prose .md files until
   the Lean axioms compile."

I did Python-first then prose-bean for: the writhe bond wiring, the Reeb
coefficient identity, the CAL-3 length substitution, the A^(1/3) exponent
measurement, the Gram signature. GramSignature.lean (this session, build clean,
0 warnings) is the FIRST piece written the required way, and even that came
after the Python. The InterfaceScalar additions were Lean-proved but also
Python-first.

NOT retro-fixable for work already landed; the correction is to stop doing it.
Items still owed a Lean scaffold BEFORE more Python: the colour-weight
derivation (qou-kj4v), the binding-length radius law (qou-usft).

## P1 -- THE PRIMARY COORDINATION DOC IS UNTOUCHED

docs/canonical-derivation-cheat-sheet.md self-describes as "the PRIMARY
coordination document for the canonical chain" and says "Update the relevant row
when you open/land work on a step -- do not fork a parallel status doc". Last
touched 2026-08-01. I landed 38 commits without touching it, and instead created
~10 new beans, which is arguably the forked parallel status doc it forbids.
Known stale rows: :225 (f_pn = z, pre-excision), :229 (delta via
flavor_split_subleading, superseded by _leading). A^(1/3) appears NOWHERE in it
despite now being load-bearing. Workflow wt2l72ea0 is auditing it row by row.

## P1 -- NEVER-BEANED FINDINGS FROM EARLIER IN THE SESSION

  * The HABIRO CLUSTER: 8 producers failing on one
    `CoercionFailed: expected an integer, got -74*check_q - 74` root cause,
    PROVED pre-existing (they do not import wedderburn_jones_markov at all;
    they surfaced because 453b2a86 added record_upstream to 112 producers).
    Diagnosed in wave5 triage, recorded in qou-gjkv -- but NEVER given its own
    bean, so it is invisible to `beans list`. NEEDS A BEAN.
  * binding_energy_categorical_deuteron.py returned ANCHOR_MIGRATION_INFERRED in
    BOTH wave4 and wave5. Verdict is 'review' by design; I flagged it for human
    eyes twice and never surfaced it again.
  * The Ecalle agent's owed re-tiering of 11 ILL-POSED resummation witnesses
    (scope-(a) negative -> scope-(b) closed). Enumerated in the audit, never
    executed.
  * Three stale doc citations of atomic-braid-mass-table.witness.json
    (2026-05-17-p4tt-migration-triage.md:60,
     2026-05-10-workplan-0b-script-rewire-handoff.md:267,
     coordination/1ppb.md:132) -- doc-only, still unfixed.

## P2 -- OPEN AND CORRECTLY BEANED, listed for completeness

  qou-6nd0  56 of 57 wave5 VALUES unadjudicated; sign flips 2 and 3 never done.
  qou-adwi  two incompatible Planck lengths; GramSignature.lean now gives
            structural support for share-vs-total but does NOT close it.
  qou-5uj7  spectral distance -- and see the NEW NEGATIVE below.
  qou-kj4v  colour weight t = 0.499656 derived vs 0.119453 required.
  qou-7e67  A^(1/3) rulings 1-4 adopted, none executed yet.
  qou-usft  EM sector, blocked on NN.
  qou-h7mh  coordination / bond count for A >= 3. Untouched all session.
  qou-4waf  Nolen-Schiffer, CSB in the wrong channel.

## NEW RESULT THIS TURN (and it damages qou-5uj7)

The 6x6 Markov-Gram matrix G_ij = tr_M(b_i b_j) on the H_3(q) NF basis
{gamma, sigma0, sigma1, L+, L-, e-} is LORENTZIAN under BOTH conventions:

    C: eigenvalues -0.855067, +0.101797, +0.855067 x3, +3.476950   sig (5,1)
    D: eigenvalues -0.752702,  0,        +0.752702 x3, +4.230339   sig (4,1)+null
       det G = 2.89e-51, i.e. ZERO -- the form is DEGENERATE under production D.
       Repeated magnitude 0.75270211325196540159 = mu+ EXACTLY, the T=1 isospin
       projector scalar from InterfaceScalar.lean.
       Null vector (gamma,s0,s1,L+,L-,e-) =
         (-0.472689, +0.425854, +0.425854, -0.383660, -0.383660, +0.345646),
       symmetric under s0<->s1 and L+<->L-, i.e. the braid-symmetric direction.

CONSEQUENCE, now Lean-proved in QOU/QBeta/GramSignature.lean (build clean):
`lip_kernel_forces_unbounded` -- a Lipschitz seminorm with a nonzero kernel
element that the states separate makes the Connes sup UNBOUNDED. A degenerate
Gram supplies exactly such a kernel element. So under convention D the
Markov-Gram form CANNOT induce a finite Connes distance without first
quotienting by its radical. qou-5uj7 must be re-scoped accordingly: the metric
programme is blocked on the radical, not merely on identifying a state set.

Caveat recorded in the file: the numerical signature is MEASURED, not proved --
certifying eigenvalues of an explicit 6x6 over irrational q0 is separate work.
What is proved is the consequence.


## 2026-09-07 — the P0 was still live four weeks on, and it was 3 SECONDS of compute

This bean's P0 ("I introduced witness staleness and never regenerated") was
**still live**. Verified, not assumed:

- All three named commits are **on `main`**: `0f608066` (writhe + z C→D),
  `a188542f` (derived α_EM), `9a1d7680` (CAL-3 nuclear length) — all 2026-08-09.
- Both named consumer producers import `coulomb_energy` **at module level**
  (`mirror_split_continuum_em_probe.py:98`, `binding_wn_kernel_derive_refute.py:49`).
- Their witnesses were computed **2026-07-13** and **2026-07-11** — *before*
  the change, and never regenerated. `coulomb_energy.py` has since moved again
  (2026-08-29).

**Cost to fix: 2 s and 1 s.** A P0 with a self-reported 15 % magnitude
(`E_C(3He)` 0.998413 → 0.847422) sat for four weeks behind three seconds of
compute.

### What actually moved

| | old | new |
|---|---|---|
| headline `split_AME/split_pred` | **0.985 ± 0.069** | **0.985 ± 0.069** — unchanged |
| all 5 assertions | pass | pass, no `computed` value moved |
| 7Li/7Be fixed-1/3 error factor | **2.16×** | **11.35×** |

`binding-wn-kernel-derive-refute`: **no number moved** (unicode-escape
normalisation and environment fields only).

So the probe's own conclusion is untouched, and the **supersession is
strengthened** — the superseded A=3-only fixed-1/3 route now fails 7Li/7Be by
11.35× rather than 2.16×. The witness is internally consistent after the re-run
(description 11.4, source 11.35 — the same value at the two precisions the
producer prints), because **both figures are computed** (`%.1fx` at :259,
`.2f` at :297), not hardcoded. That distinguishes this from the `habiro`
witness in `qou-9ot5`, whose prose *is* hardcoded and therefore contradicted
its own recomputed values — which is why that one was reverted and this one is
committed.

### Why this class is invisible to the documented check

Neither producer's own source changed; only a module they import did. So
`git diff <producer>` — the check AGENTS.md's idle-pass policy names first —
shows nothing. This is `cosmetic_import_cone_drift`, the one bucket the fifth
staleness-triage run measured **growing 4 → 9** the same day (`qou-e9pp`).
Two live instances, both cheap, both four weeks stale, and the documented
triage step cannot see either.



## Summary of Changes

Session log closed 2026-10-04 (owner decision 2): open children were reparented to programme epics and prose follow-ups extracted as their own beans. Kept as a record, not deleted.
