---
# qou-vvv4
title: The hadronic melt is recorded at three different points, and two of them are in sibling blocks that contradict each other
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:42:14Z
updated_at: 2026-11-17T07:44:10Z
parent: qou-10v9
---

## Measured 2026-08-30 — the mechanism, and what it does to the melt

PR #6270. Probe `computations/hecke/h3_gram_degeneracy_is_wedderburn_weight_vanishing.py` (19/19),
Lean `QOU/Hecke/WedderburnWeightDegeneracy{,Real}.lean` (13 theorems, sorry-free, axioms clean).

**The Gram determinant IS the Wedderburn product.** Measured, not assumed:

    det G(u) / (y_(3) * y_(2,1)^4 * y_(1^3))|_{z=z_C}
      = -(u^4+1)^2 (u^2-u+1)^6 (u^2+u+1)^6 (u^4-u^2+1)^6 / u^28

no positive real zero, no positive real pole. So on u>0 every degeneracy of the
corpus Gram is a weight vanishing, and the recorded factorisation is explained:
`(u^3+u-1)^5` is `z_C = q` (kills y_(2,1) at d^2=4, plus y_(1^3) at 1);
`(u^3+u^2+1)^5` is `z_C = -1/q` (y_(2,1) at 4, plus y_(3) at 1). Multiplicity 5
is d^2 bookkeeping — 5 of the 6 dimensions of the regular representation.

**Under convention D there is no degeneracy at any real q.**
`y_(2,1)(z_D) = q^2/(q^2+1)^2 > 0`; `y_(1^3)(z_D) = 0` identically (the D
radical, = `gramMatrixD_det_eq_zero`); `y_(3)(z_D) = (q^4+1)/(q^2+1)^2`; sum = 1.
Scope-(b) with the invariant cited. Scope-(a) for "no hadronic melt" generally —
this excludes the Wedderburn/Gram route only.

**The two sibling blocks disagree, and the theorem block is the right one.**
`spectrahedral-phase-collapse-melt.md` says threshold `q = psi ~ 1.4655` and
"heated past"; the theorem + its sorry-free Lean give `u = 1/psi` with
`u = sqrt(q)`, so `q = 1/psi^2 ~ 0.4656`, and the melt hypothesis is
`u^3+u-1 < 0`, i.e. BELOW. Measured: y_(2,1)(z_C) < 0 for u < 1/psi, > 0 above,
= 0.2809 at the proton pin. NOT FIXED — needs an author decision about what the
melt block was trying to say. No `content/` touched.

**Three "supergolden" points, not one.** `u = 1/psi` (Gram, convention C);
`q = psi` (z_D = 1, tr_M collapses onto the counit); `u = -psi` (detFactor4,
outside the regime). I hypothesised the first two were the same point and
checked; they are not. Recorded as refuted rather than dropped.

**Strengthening of an existing corpus claim.** `qbeta-counit-closed-form.md`
says the trivial loop value "is never attained on the substrate" — about q_0.
Measured: `z_C = u/(u^2+1) <= 1/2` for ALL u>0, so under C eps = tr_M is
unreachable at EVERY q.

**Cross-check gained for free:** the derived `y_(1^3)(z)` reproduces the
2026-08-26 audit's form exactly, though that audit solved for it from the
descent condition and this solves the character-table system.

### Wrong turns, recorded

1. First det-vs-Wedderburn run declared `u` without `positive=True`, so
   `sqrt(u^2)` never simplified and the ratio came back carrying spurious
   `(u^3+u-1)^5` and `(u-1)` — it LOOKED like the prediction had failed.
2. Started from the hypothesis that `z_D = 1` (q = psi) was the same point as
   the Gram collapse (u = 1/psi). It is not; refuted before it was written down.

### Still open

- The melt block's location + direction: author decision, untouched here.
- Whether any convention-D transition exists by a NON-Wedderburn mechanism
  (SDP feasibility boundary not driven by weight vanishing, higher-n block,
  archimedean bound). Nothing here bears on it.


## 2026-08-30 — the melt block IS corrected (owner authorised)

Owner said "work the block correction". Done in `3b5dc46a30`, PR #6270.

Correcting the number alone was NOT sufficient, and that is the finding:

- The block implied a monotone ladder (molecules ~1.045/1.17, then nucleons).
  The molecular thresholds are ABOVE q_0 = 1.10998; the corrected hadronic one
  is BELOW it, at 1/psi^2 = 0.4656. Opposite directions in q. The block now
  says so explicitly instead of implying one sequence.
- Under convention C there is NO Gram degeneracy above the substrate at all —
  the parent says it outright. Grepped: this block was the ONLY place in the
  corpus asserting a q > q_0 hadronic threshold. So "dissolution by heating"
  had nothing behind it and could not be repaired by renumbering.
- Gain: it stops contradicting `rem:deconfinement-golden-threshold` too
  (q_gold = 1/phi^2 = 0.382, also below q_0). Corrected, the two are ordered
  0.4656 then 0.382 as q descends — the hierarchy the block's title promises.
  Added as a `uses` edge.
- Added a Scope paragraph: convention-C only; under D the (2,1) weight is
  q^2/(q^2+1)^2 > 0 for all real q, so the degeneracy has no canonical
  counterpart. Fixing the number does not make the block canonical.

**No temperature verb used.** The q-to-T orientation is genuinely unsettled —
beaned separately as `qou-re90` — so "cooled past" would have picked a side.

**Left alone deliberately:** the molecular thresholds 1.045 / 1.17. No source
for them anywhere in `content/` or `computations/`; the Lean marks that claim
DEFERRED and mis-cites it to the parent block when it lives here. They carry
the same u-vs-q risk that caused this defect. Not mine to guess at.

Verification: pipeline render exit 0; `run-validate` exit 0 "Valid" with the new
cross-ref RESOLVING (absent from the undefined-xref warning); qa-sweep 0/0/0
with all 8 mechanical criteria refreshed at 0 findings; grep battery + expository
pass clean.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Implementation & Witness Progress (PR #8261)
- Branch: `qou-10v9-d5e8-lq6k-tqfm-ughq-vvv4` (`215564fea0bbd17193637e08e9f87df6e0ac73b7`), PR: `litlfred/qou#8261`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/BoltzmannExtensivityMilnorAntisymmetryShiftInertnessWenzlMarkovLockAndHadronicMeltOrdering.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/boltzmann_extensivity_milnor_antisymmetry_shift_inertness_wenzl_markov_lock_and_hadronic_melt_ordering_probe.py` -> `computations/probes/boltzmann-extensivity-milnor-antisymmetry-shift-inertness-wenzl-markov-lock-and-hadronic-melt-ordering.witness.json` (`allPassed: true`, `scriptHash: 6d6a6f5a2d13`, `scriptCommitSha: 83f7ff931c7cc699e6338421bf57c15a92f557d2`)
