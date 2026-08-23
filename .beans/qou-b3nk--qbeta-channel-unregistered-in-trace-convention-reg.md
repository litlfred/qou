---
# qou-b3nk
title: Q_beta channel UNREGISTERED in the trace-convention registry — the ladder is convention-C end-to-end; settle its convention
status: completed
type: task
priority: high
created_at: 2026-08-15T13:30:00Z
updated_at: 2026-08-23T13:17:34Z
---

Found by the 2026-08-15 owner-redirect validity audit
(docs/audits/2026-08-15-c3-refutation-chain-convention-validity-audit.md;
probe qbeta_c3_ladder_trace_convention_sensitivity_probe.py, 9/9; registry
9g).

## The gap

`trace-convention-registry.json` registers channels mass / binding /
borromean-binding-single-pipeline (all convention D since the 2026-08-09
owner ruling). **The Q_beta channel is not registered**, yet its ladder
consumes the Markov parameter end-to-end:

    alpha = (z - 1) * h / 2,  z = sqrt(q)/(1+q)   <- convention C
    qbeta_utils.py:124-125 (the c_3 extractor)
    qbeta_ck_sseries_exact_rational.py:20,248 (the KC21/KC22 D-ladder core)
    ZBarParity.lean:59-79 (KC13's bar-even z)

Measured consequences (all in the audit's witness):

- re-extraction under D shifts c_3 from ~ -2.07 to ~ **-974** -> every ~ -2
  value-level fact ((H1) -Vol(4_1), [3]_q/25, J-hbar^2, S_leak, q*_S) is
  C-conditional;
- the implied empirical c_2 under D is ~ **-9.30** and the rung convergence
  (58x at N2 under C) disappears -> even the canonical c_2 = -1 (Lean-proved
  Taylor-exact) is a C-frame statement;
- bar(z_D) = q^-4 * z_D exactly -> KC13's no-scalar-z-source prune is
  C-scoped;
- the REFUTED-as-real-q verdict is convention-IMMUNE (swing D/C = 1.0052) —
  that part of the record needs no rescue.

## The task (one of three honest outcomes)

1. **Derive C for the decay channel.** The beta channel's explicit weight
   instance is y = (z, 1/2 - z, z) with y_(1^3) != 0 — it genuinely uses the
   third row, so the mass channel's forcing (two-row cap => y_(1^3) = 0 =>
   D, docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md,
   markovWeights_eq_jones_of_threeRow_eq_zero) may simply NOT apply. That is
   currently an observation, not a derivation. Formalize-first: the decision
   object is the decay channel's H_3 decomposition — does it kill the third
   row or not? Lean-sized, not a scan.
2. **Show the forcing transfers** -> then the whole Q_beta ladder (c_2 = -1
   included) must be re-derived from the D-trace and the c_3 value record is
   superseded. Do NOT do this by swapping z in the existing ladder — the
   probe shows that breaks the ladder's empirical convergence (N1 residual
   7.4e-5 -> 6.7e-4); it is a re-derivation, not a substitution.
3. **Register `disputed`** with the audit as open_item, if neither derivation
   lands.

Whichever lands: add the channel entry to trace-convention-registry.json
(+ .md), and from now on any quoted c_3/S/q*_S value names its convention
(the registry's own rule: convention-silent trace values are not comparable).

## Anti-fit guardrail

Do not pick the convention by which one makes a downstream number look
better. C currently "works" numerically because the ladder was BUILT in the
C frame — that is provenance, not evidence. The convention must come from the
channel's representation theory, exactly as the mass channel's did.

## Session note (2026-08-15, claude/qbeta-channel-convention-2026-08-15, PR #5111)

Outcome (c) of the three, leaning (b): NEITHER convention is derived for the
decay channel. Registered `channels.qbeta-decay` DISPUTED (definitional null —
the decay blocks write the excised-C value while naming it "the Markov--Jones
parameter", whose referent has read D since 2026-08-09; production C) +
R9 tripwire on qbeta_utils.markov_parameter (CONFIRMED C, |d|=1.9e-51).

Proved (Lean, sorry-free, lean-direct exit 0, no sorryAx —
QOU/QBeta/MarkovZFullBarCondition.lean):

- decayLadder_zC_threeRow_ne_zero: any faithful normalised Markov trace at
  the ladder's z_C has y_(1^3) != 0 for ALL s = sqrt(q) > 1. So option 2 of
  this bean (forcing transfers) and "keep the C ladder" are MUTUALLY
  EXCLUSIVE — proved, not observed. D-adoption = ladder re-derivation.
- Full-bar condition bar(z) = z - h in Lean: D holds exactly
  (zD_full_bar_covariant); any bar-even z (= C) fails away from q^2 = 1.
  Premise (trace bar-compatibility) named, not proved.

Witness correction to this bean's own framing: the explicit instance
y = (z, 1/2-z, z) is NOT an Ocneanu z_C-trace (sigma_0 value = h/2 exactly,
z-independent) — it inhabits a normalisation-only class. The correct
y_(1^3) != 0 witness is C's own Ocneanu solve (0.02274 at q0) + the Lean.
Conclusion (third row present under C) unchanged.

What remains open (the honest residue): the decay channel's FIBRE — no
corpus block derives it (corpus-grep clean); D is conditional on
conj:binding-qbeta-complex-volume (same-object identification) or trace
bar-compatibility; C is conditional on the decay trace being neither
bar-compatible nor a fibre trace, and even then z_C itself is underived
(third-row presence leaves z a one-parameter family). Routes in audit §4:
docs/audits/2026-08-15-qbeta-decay-channel-convention-disputed-registration.md.

Status stays in-progress; closing is a human action.


---

## CLOSED 2026-08-23 — C is excluded; D is not thereby derived

Branch `claude/b3nk-decay-convention-c-excluded-2026-08-23`.

**The bean's question — "settle its convention" — is answered twice over, and
the registry had absorbed neither answer consistently.**

**1. Status: settled by owner ruling 2026-08-15** ("convention D is convention.
excise convention C"). The JSON registry absorbed this; its **authoritative
markdown twin did not** — the `.md` still carried `definitional: null
(contradictory)` / `status: disputed (bean qou-b3nk)`, i.e. the registry
disagreed with itself about the one disputed channel. Fixed here.

**2. Convention C is now a scope-(b) STRUCTURAL EXCLUSION, identically in q.**
Not "not derived", and not "would exclude it IF demanded" — excluded, by a
named invariant:

  z_r = q^(2r-1)(1-q^2)/(1-q^(2r)) = q^r/[r]_q  lies in Q(q) for EVERY r.
  z_C = sqrt(q)/(q+1) does NOT: x^2 - q is Eisenstein at the prime q of Q[q],
  hence irreducible over Q(q), so sqrt(q) is not in Q(q); and z_C in Q(q)
  would give sqrt(q) = z_C*(q+1) in Q(q).

For non-integer real r the same follows from non-constancy of the formal level
(r_C(1.05) = 2.2267 vs r_C(1.15) = 2.9553). Evidence: `wenzl_level_family.py`
W4/W9, 10/10, sympy-exact over Q(q), no float64 (this work re-ran it green).

This **subsumes** one of the two conditions the registry listed and shows they
were never independent: W3 proves N_eff and the Wenzl level are the SAME MAP,
so the registry's "N_eff(z_C) = 2.5995 pointwise, q-dependent" was a pointwise
shadow of a q-identical structural fact. The full-bar condition remains a
genuinely separate, still-premised route.

**What is NOT settled — do not read this as deriving D.**
- Excluding C says z_C is NO level. It does not say WHICH level the decay
  channel occupies. r = 2 here still needs the decay fibre's RANK — that is
  `qou-cds1`, and it is OPEN.
- The unconditional part is the mathematics: `z_C != z_r for all r`. The
  inference "therefore C is inadmissible for this channel" is conditional on
  the channel's z being a fibre-level parameter at all — the categorical-fibre
  premise, which is the framework's own and is not proved here.
- W10 (every channel in the family sits at r = 2, none at r >= 3) is
  suggestive, not a derivation.

**Role change for the mutual-exclusivity theorem.**
`decayLadder_zC_threeRow_ne_zero` (sorry-free) blocked the mass channel's
two-row forcing from transferring *while the ladder keeps z_C*. That antecedent
is now itself excluded, so the theorem no longer stands as an obstruction to D
— it is an argument for abandoning z_C.

Successor: `qou-cds1` (re-derive the ladder under D; a z-swap is NOT a
migration — measured c_3 -> ~-974, rung convergence collapses).
