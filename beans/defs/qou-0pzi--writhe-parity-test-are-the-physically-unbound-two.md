---
# qou-0pzi
title: 'writhe-parity test: are the physically-unbound two-nucleon channels at even-negative stacked powers while the deuteron is not?'
status: in-progress
pr: 8205
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T00:11:01Z
updated_at: 2026-10-04T15:25:40Z
parent: qou-v2om
---


## Answer: the parity question is premature — the sector fails on SIGN first

The test was going to ask whether the physically-unbound channels sit at
even-negative stacked powers. Running the framework's own two-nucleon
predictions first:

| system | B_framework | nature | verdict |
|---|---:|---:|---|
| pn (deuteron) | +2.8328 | +2.2246 BOUND | bound, +27.3 % over |
| pp (diproton) | **+2.5416** | ≈ −0.10 **UNBOUND** | **WRONG SIGN** |
| nn (dineutron) | **+3.3069** | ≈ −0.10 **UNBOUND** | **WRONG SIGN** |

**2 of 3 two-nucleon systems are qualitatively wrong.** Not a normalisation
artifact — the un-normalised exact traces are +2.0507 and +3.7978, same sign.

The comparison is fair by the framework's own construction: `_bond_type_L`
defines `L_pp` as the isolated `(Z,N)=(2,0)` log-trace-ratio, so `L_pp` **is** the
diproton. There is no many-body reasoning in between to appeal to.

So `pp = sigma`, `nn = sigma^-1` cannot be the right assignment, and asking which
stacked power they sit at presumes an assignment that is already falsified. The
parity question survives as a repair *direction* (`qou-pjx4` shows unbinding is
available at even-negative powers) but not as a test of the current one.

## Consequences

- The chirality ordering `b_nn > b_pn > b_pp`, reported as a positive structural
  result (2026-06-16 audit), is an ordering among three numbers **two of which
  have the wrong sign**.
- Not confined to the two-nucleon rows: every `B_sym` with `Z >= 2` or `N >= 2`
  consumes `(Z-1)` pp and `(N-1)` nn bonds at these values.
- The magnitude framings I have been building (3.01x low at the asymptote,
  27.3 % over at the deuteron) **understate** the problem. A magnitude residual
  invites a missing additive term; a sign error says the per-bond object is not
  the two-nucleon interaction.

## Scope

Scope-(a). Does not refute the chain's additivity (1.78e-15 against the exact
p(3A) trace), any Lean theorem, or the framework at large — a statement about the
per-bond VALUES. Corpus already knew nature's pp/nn are unbound and that
projectors cannot unbind (`mu_+ + mu_- = 1`); what is new is that production does
not merely fail to unbind them, it binds them at +2.54 / +3.31 and feeds those
into every multi-nucleon B_sym.


## Progress Update (PR #8205)
- [x] Pure Lean 4 formalization wired into `QOU.lean` (`AtomNFQDegreeBondSetDichotomy.lean`, `TwoNucleonChannelSignObstruction.lean`, `PairLayerLinearRampParity.lean`, `ChainMirrorSplittingChargeSymmetry.lean`; 0 `sorry`, 0 vacuity advisories across all 6 static audits)
- [x] 50-dps `mpmath` + exact `TL_3` Laurent polynomial probe (`computations/probes/atom_nf_qdegree_pair_ramp_mirror_probe.py`) and stamped witness (`computations/probes/atom-nf-qdegree-pair-ramp-mirror-probe.witness.json`, 0 raw `float64` fields)
- [ ] Awaiting adversarial review and Merge Manager merge of PR #8205 (`ready: ed5c0c87c86301f2666c843555cc576831d17a74`)
