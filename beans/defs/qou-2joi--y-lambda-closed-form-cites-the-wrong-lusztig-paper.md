---
# qou-2joi
title: y_lambda closed form cites the wrong Lusztig paper; BLM is absent and the DOI contradicts itself
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T13:20:20Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-q4oa
---

## Survey: are the Delta_lambda / y_lambda assertions Lean-proved?

211 declarations across 219 files mention Delta_lambda or y_lambda.

    sorry            0        `: True` conclusions   0
    axioms           0        empty Prop carriers    0
    theorems       136        of which conditional on a CONJECTURE class: 2
                              (17 more are ordinary [Field K]/[DecidableEq], not conjectures)
    classes          8        all content-bearing; 7 have NO instance = honestly open

So the file-level answer is clean, but it splits:

- **Delta_lambda: PROVED, unconditionally.**
  `QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional` takes no class
  hypothesis, is sorry-free and general-n.
- **y_lambda: NOT proved.** The closed form is a conjecture class,
  `QSchurYLambdaClosedFormClaim`, with the real content as a field
  (`closed_form_holds : forall lam q, ySchurClosedForm lam q = qSchurWeight lam q`)
  and **no instance**. That is the honest open state, correctly encoded.

## Need lit? YES — and the provenance was pointing at the wrong paper

The class docstring said the conjecture is "equivalent to the Lusztig 1990 /
BLM identity" and carried one `-- Ref: [lusztig1990]`. Three problems:

1. **`lusztig1990` is the wrong paper.** It is *Canonical bases arising from
   quantized enveloping algebras* (JAMS 3) — canonical bases, not a q-Schur
   Markov-trace weight identity.
2. **BLM was absent entirely.** `grep -c 'q-schur' references.ts` = 0; the only
   "Beilinson" in the bibliography is the p-adic Beilinson conjecture paper.
   Added as `blm1990`, explicitly marked **UNVERIFIED** — fields are from recall,
   egress is blocked, and the paper is not in `library/`.
3. **Two DOIs, one key.** `references.ts` says `10.2307/1990961`;
   `OptionE/CrystalDeltaLambdaScaffold.lean` and `IwahoriHecke/TypeA.lean` both
   say `10.2307/2152736`. NOT resolved here — guessing is what produced it.

## What is actually holdable, measured

| key | title | ingested? |
|---|---|---|
| wenzl1988 | Hecke algebras of type A_n and subfactors | **NO** |
| jones1987 | Hecke algebra representations of braid groups | **NO** |
| orellana1998 | Weights of Markov traces on Hecke algebras (1999) | YES `arxiv-math-9806163v1` |
| lusztig1990 | Canonical bases... | NO |
| blm1990 | A geometric setting for the quantum deformation of GL_n | NO |

**The one ingested paper is the wrong type.** Orellana's weight formula is type
B_n/D_n — double partitions (alpha,beta) with a second parameter Q. The QOU
y_lambda is type A: single partition, one parameter. Do not read the section
"5. The Weight Formula" as settling the type-A claim; that is the same
object-vs-object slip as the (2,1)-vs-(1^3) conflation.

The type-A sources that WOULD settle it — Wenzl 1988 and Jones 1987, both
already cited by the file — are **not ingested**, so nothing in this repo can
check the identity. That is the actionable ask: ingest those two.

Minor: `orellana1998` is keyed 1998 but the entry is 1999 (Crelle 508). Left
alone — a key rename is corpus-wide.


## Both pre-existing status disagreements RESOLVED — same root cause family

### prop:confinement-frobenius-reciprocity — a q0 layer straddle

`lp_duality_gap_zero` reported 2.088e-02 at tolerance 1e-10. Not a solver bug.
The solver was handed an objective at the MUON pin and a Gram at the PROTON pin:

    t[1]   = 0.6126880505488901   z_D(muon)
    G[0,1] = 0.6126880371464652   z_D(proton)

Why one mismatch produces that gap:

    t_proton . ker(G_proton) = -1.11e-16    objective FLAT along the null dir
    t_muon   . ker(G_proton) = +2.21e-08    objective TILTED

The convention-D Gram is singular (corank 1), and `||G @ gramRadicalD|| =
3.8e-16` confirms the PR #5618 Lean radical IS the numerical null direction. A
flat objective makes the radical harmless; tilt it by 2e-8 and the optimum
slides along it to the artificial `M_bound` (x*[0] pinned at exactly -1e6). The
box multiplier is then nonzero and `dual_obj = n_target*y0` omits it — the
omitted term IS the "gap".

    straddled    primal 0.0208845641  gap 2.088e-02  x* on bound: yes
    consistent   primal 0.0000000000  gap 3.821e-16  x* on bound: no

Fixed by reclassifying `borromean-axial-coupling` ideal_muon -> physical_proton
with the witness regenerated in the SAME commit (migration constraint 4).

### thm:topological-mass — a prediction asserted as a definition

`hbar_q^2 = Vol(4_1)/(m_mu/m_e)` was asserted at tolerance 1e-15 with source
"Definitional". True until the 2026-05-28 proton re-pin; a PREDICTION since.
Decomposed exactly: 209.806 ppb genuine mu-p tension + 1.399 ppb artifact (the
muon pin was solved against CODATA 206.768283, the check used 206.7682827).
Re-specified as a falsifiable band plus the same relation checked AT the muon
pin where it is definitional. m_mu still misses its target by 963.6x; nothing
here touches the dashboard.

## THE STRADDLE IS A CLASS, NOT A ONE-OFF — 11 of 119, unfixed

Swept every `ideal_muon` producer for consumption of a proton-anchored witness:

    atomic_tr_m_mpfr_50dps                    <- atomic-tr-m-mpfr-50dps-PROTON.witness.json
    gap_a3_deuteron_p_lambda_channels_probe   <- chi-deuteron-h6-at-q0-50dps
    gap_a3_plambda_bar_even_admissibility_probe
    gap_a3_transpose_invariant_plambda_probe
    option_e_kashiwara_crystal_delta_lambda_probe
    parabolic_cylinder_channel_mixing_probe   <- binding-bar-even-odd-probe
    probe_9b_gate_interface_algebra
    qbeta_decay_sdp_extended_ck
    qbeta_route_alpha_lift_prediction
    rho_f_categorical_probe                   <- markov-peel-atomic-tr-m
    rho_w_crystal_vertex_trace

The first one consumes a witness with "proton" IN ITS FILENAME while classified
muon. NOT fixed here: each needs checking for whether it is a deliberate
comparison (migration constraint 3), and the bulk sweep is qou-1c4y.

**The reason this matters more than 11 files.** None of these currently produce
a status disagreement — the gate is at 0. The borromean one was caught only
because a SINGULAR Gram amplified a 2e-8 anchor tilt into a 2e-2 duality gap.
Where no such amplifier exists the straddle is silently wrong at ~1e-8
relative, which is above the L1 target of 1e-15 and invisible to every check
we have.


## MEASURED: the straddle class is 1 real, not 11 — my last claim was wrong

I wrote that these are "silently wrong at ~1e-8 relative, above the L1 target
and invisible to every check we have." **That was an inference, not a
measurement, and it is wrong.** Ran each producer under both anchors
(`QOU_Q0_ANCHOR=ideal` vs `physical`) and diffed its output with volatile AND
stamp fields masked:

| producer | anchor-sensitive? |
|---|---|
| gap_a3_deuteron_p_lambda_channels_probe | NO — byte-identical |
| gap_a3_plambda_bar_even_admissibility_probe | NO |
| gap_a3_transpose_invariant_plambda_probe | NO |
| option_e_kashiwara_crystal_delta_lambda_probe | NO |
| parabolic_cylinder_channel_mixing_probe | NO |
| probe_9b_gate_interface_algebra | NO |
| qbeta_decay_sdp_extended_ck | NO |
| rho_f_categorical_probe | NO (stdout hash identical) |
| **rho_w_crystal_vertex_trace** | **YES** |

**8 of 9 move nothing.** For those the manifest entry is a LABELLING defect: the
output does not depend on q0 at all, so the anchor is irrelevant to the numbers
and only the stamp is wrong. Worth fixing for honesty, not for correctness.

**Two were never straddles:**
- `atomic_tr_m_mpfr_50dps` writes BOTH `atomic-tr-m-mpfr-50dps.witness.json`
  (muon) and `...-proton.witness.json` (proton). That is a DELIBERATE
  COMPARISON producer — migration constraint 3 — and correctly needs both. My
  detector missed it because it tests for `q_muon_at()`-style calls, and this
  one expresses the comparison by emitting two witnesses instead.
- `qbeta_route_alpha_lift_prediction` writes a PROTON-stamped witness while
  classified `ideal_muon`. Stamp contradicts classification, but its output
  declares proton, so consumers are not misled.

**The one real hit, sized.** `rho_w_crystal_vertex_trace` mixes a q0-dependent
`Delta_lambda^rho_w` against an anchor-fixed `chi^lambda_cache` (the cache is
byte-identical across pins; only Delta moves). Magnitude ~1e-11 relative — real,
above the 1e-15 L1 target, and **five orders below that producer's own
cross-check residual** `|Sum_w rho_w - chi^lambda_cache| = 8.9e-7`. So even
there the straddle is not the dominant error; the ~1e-6 Delta_lambda
cross-check discrepancy is, and it is pre-existing and unexplained.

**probe_9b is straddled AND failing, but not because of it.** Five failing
assertions with ORDER-UNITY discrepancies (`gate_near_cancellation_A3`
computed -0.4709 vs expected -0.0337). A 1e-8 anchor difference cannot produce
that. No block cites the witness, so it is not a status disagreement. Its
`gate_near_cancellation_A3` / `cancellation_fails_A7` pair IS bean qou-zf9n
item 4 (A=3 mirror fails to cancel while A=7 does) — same producer, separate
investigation.

**Why borromean was different, and why the amplifier is the real lesson.** Its
Gram came from a committed proton WITNESS FILE while its q came from the muon
manifest — two numerical layers genuinely combined in one computation, and a
singular Gram turned a 2e-8 tilt into a 2e-2 duality gap. That amplifier is
what made it visible and what made it matter. Absent such an amplifier the
straddle is mostly cosmetic, which is the opposite of what I asserted.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-24 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (PR #8443)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/BarParityReadoutPartitionWeightBraidedTraceSurfaceGenusPolarizationPair.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_2djn_2joi_4khc_51l1_8ava_probe.witness.json` (`Commit 1` = `76eb5ed3bb589e3c0713062c1916ff3df6e16b60`, `HEAD` = `bd4d50a998e0b0519e966f309ff7ef17c810abac`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8443, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-24: "bean(qou-2joi): both disagreements resolved; the straddle is a class of 11"). The work may be partly or fully done. Read the bean before you close it.

## 2026-11-21 — paper-structure drain (https://claude.ai/code/session_01Qmmkt8R1YXFpKDbBiKB3hh)

blm1990 registered and refs added on main. Left: lusztig1990 DOI conflict (references json 10.2307/1990961 vs two Lean files 10.2307/2152736) — no DOI resolver reachable from this container, not guessed. Wenzl 1988 / Jones 1987 still not ingested.

Report: docs/audits/2026-11-21-paper-structure-bean-drain.md on branch claude/paper-structure-drain-2026-11-21.

Ruling check (owner-rulings.md on main 2ae54ab401, 2026-11-21): no superseded premise (photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ = 2 − h⁴, fitted values in proofs) is used by this bean's finding.
