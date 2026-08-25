# Triage: the 5₂ survey's two "register this paper" recommendations do not buy what they claim

**Date:** 2026-08-18 · **Axis:** 5₂ / c₃ bar-odd / bibliography · **Tier:** triage —
corpus-grep against two recommendations · **Discipline:** no fit, nothing wired, no
tier change. This document argues for **not** doing two pieces of proposed work.

## Why this exists

A literature survey of the 5₂ lane (2026-08-18, run alongside the `qou-ynff` trace-field
correction) produced six ranked routes. Two of them — **R2** (register Ohtsuki 2016) and
**R3** (register Bettin–Drappeau) — were presented as bounded, low-risk wins, with R3
called *"a bibliography repair, low risk"* that would *"remove a conditional hypothesis
from every corpus argument that assumes QMC for 5₂"* and *"convert a standing conditional
into a theorem."*

Corpus-grepped before acting. **Neither buys what it claims.** R3's premise is false;
R2's is half-true and its stated motivation is contradicted by the corpus. Recording
this so the next agent does not spend the effort — a negative on proposed work is worth
the same as a negative on a probe.

## R3 — Bettin–Drappeau: the premise is false, twice over

### There is no conditional to discharge

The claim was that corpus arguments carry quantum modularity for 5₂ as an unproved
hypothesis. They do not. The load-bearing statement is in
[`2026-08-01-fibre-to-observable-bridge-verdict.md`](../audits/2026-08-01-fibre-to-observable-bridge-verdict.md):

> there *is* a named, **literature-established** bridge — quantum modularity / the
> Ohtsuki-tower expansion at the imaginary substrate / median resummation — and the
> corpus has it **Lean-scaffolded sorry-free**

and the unification ledger
([`2026-08-02-c3-odd-aomega-unification.md`](../coordination/2026-08-02-c3-odd-aomega-unification.md))
records the same row as **"Lean-proved sorry-free"**
(`OhtsukiTowerBarParity.lean`, `even_rung_real` / `odd_rung_imaginary`).

So quantum modularity is not what blocks anything here. The same verdict names what
actually blocks it, and none of it is QMC: the smooth Borel sum is **anchor-blind**
(supplies no swing), the anchor-dependent piece is a **CAL-2 calibration input** whose
derivation is Subgoal-2, and the exact-integer Stokes identification `A_ω = 3` is
**explicitly open**. Proving QMC moves none of those three.

### And it is the wrong QMC anyway

Every conjectural quantum-modularity reference in the corpus is to the **Refined**
Quantum Modularity Conjecture — the Garoufalidis–Gu–Mariño / GSWZ statement about the
full matrix of `(x,q)`-series indexed by boundary-parabolic flat connections
(`bib-qa-verifications.json`, beans `qou-41qf`, `qou-pxbv`). Bettin–Drappeau prove
**Zagier's** QMC. The refined statement is strictly stronger; a proof of the plain one
does not discharge it.

This is the [`da-arity-conflation`](../../AGENTS.md) failure mode from AGENTS.md
§"Grep the claim SHAPE, not only the topic": same topic, different proposition. A
topic-grep for "quantum modularity" finds both and cannot tell them apart — which is
presumably how the recommendation was generated.

**Disposition.** Registering Bettin–Drappeau is fine as ordinary bibliography hygiene
and would cost little. It is **not** an epistemic upgrade, and no corpus claim should be
re-tiered on the strength of it.

## R2 — Ohtsuki 2016: half-true, and its motivation is contradicted

The recommendation said Ohtsuki 2016 is *"not in the bibliography and not in uploads"*,
*"despite being the canonical source for exactly the κ-ladder the corpus reconstructs by
hand."*

**The narrow half is right.** Ohtsuki's solo 2016 *Quantum Topology* paper on the 5₂
Kashaev asymptotics is not a registered entry.

**The motivation is wrong.** The corpus is not working without Ohtsuki:

| | |
|---|---|
| `ohtsuki-takata-2015` | **registered** in [`references.ts`](../../content/schema/references.ts) (Kashaev asymptotics ↔ twisted Reidemeister torsion, two-bridge knots — a class that contains 5₂) |
| `OhtsukiKappaDependence.lean` | 143 lines of Lean |
| audits explicitly named for him | **four** — [higher rungs exact](../audits/2026-07-12-ohtsuki-higher-rungs-exact.md), [symbolic derivation Borel Φ_b](../audits/2026-07-12-ohtsuki-symbolic-derivation-borel-phib.md), [Φ_b a₁ mis-identified](../audits/2026-07-18-phib-a1-mis-identified-not-ohtsuki-kappa1.md), [s-channel saddle Ohtsuki vs c_k](../audits/2026-08-01-schannel-saddle-point-ohtsuki-vs-ck.md) |
| `references.ts` prose | already cites *"Ohtsuki's saddle-point/Borel-resummation analysis"* |

So this is **citation hygiene on one specific paper**, not the recovery of machinery the
corpus lacks. Worth doing when someone is next in `references.ts`; not worth a tranche,
and it will not validate the κ-ladder from outside in the way claimed — the corpus
already arbitrates that internally (it caught the GGM eq-20 τ² misprint on its own).

## The general lesson

A survey's recommendations are claims about the corpus, and they get the same
corpus-grep as any other claim before they are acted on. Both of these would have
consumed real effort — R3 in particular was framed as re-tiering standing conditionals,
which is exactly the sort of change that should never run on an unchecked premise.

The cheap test that caught both: **ask what specific proposition is currently carried as
conditional, and find it in the corpus.** For R3 there is no such proposition; for R2 the
machinery is already there under a different citation.

## Cross-references

- Trace-field correction that prompted the survey: [`2026-08-11-5two-trace-field-is-disc-minus-23.md`](../audits/2026-08-11-5two-trace-field-is-disc-minus-23.md)
- Bridge verdict (the "literature-established" statement): [`2026-08-01-fibre-to-observable-bridge-verdict.md`](../audits/2026-08-01-fibre-to-observable-bridge-verdict.md)
- Unification ledger row: [`2026-08-02-c3-odd-aomega-unification.md`](../coordination/2026-08-02-c3-odd-aomega-unification.md)
- Bean: `qou-35du`
