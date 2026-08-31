---
# qou-re90
title: Two blocks map q to temperature in OPPOSITE directions, and nothing adjudicates them
status: completed
type: task
priority: normal
created_at: 2026-08-30T16:51:46Z
updated_at: 2026-08-30T18:15:56Z
---

Found 2026-08-30 while answering an owner question about `qou-vvv4` (the
spectrahedral-melt block). It is NOT that block's question — it is older and
wider — so it is beaned separately rather than settled inside a prose fix.

## The two maps

**(A) `content/quantum-observable-universe/information-theory/quantum-temperature.md`**

    t_P(q) = q/(q-1) = 1/hbar_q ,   T_q(U) = hbar_q = (q-1)/q ,   beta_q = 1/T_q = t_P(q)

`T_q` is **strictly increasing in q** (d/dq[1 - 1/q] = 1/q^2 > 0), and is
**negative for q < 1**. So under (A), "hotter" means "larger q".

**(B) `content/quantum-observable-universe/observations/deconfinement-golden-threshold.md`**

    k_B T_c ~ (1/2)(q + 1/q) * n_link
    "Temperature changes the effective crossing energy ... The effective q at
     which the chiral structure of the fiber is thermally disrupted is q_gold"
    q_gold = 1/phi^2 ~ 0.382       (BELOW the substrate q_0 = 1.10998)

Deconfinement is reached by driving the **effective q DOWN** to 0.382. So
under (B), "hotter" means "smaller effective q".

## The numbers, measured at 30 dps

| | q | T_q = (q-1)/q under (A) |
|---|---|---|
| substrate q_0 | 1.1099786 | +0.0991 |
| aeon boundary | 1.0 | 0 |
| deconfinement q_gold = 1/phi^2 | 0.3819660 | **-1.6180** |
| melt threshold 1/psi^2 (convention C) | 0.4655712 | **-1.1479** |

So (B)'s deconfinement point sits where (A) reports a **negative** temperature,
and (A)'s "hotter" direction is the one (B) calls colder.

## Why this is not obviously just two different objects

It may well be: a categorical/geometric `T_q` and a physical `T` need not agree,
and that would be a fine resolution. But it is **not written down anywhere**,
and two things make the "they're different" reading non-automatic:

1. (B) itself computes a `k_B T_c` from `q` and calls the result the QGP
   transition temperature, i.e. it is claiming a physical temperature FROM the
   substrate parameter — the same job (A) does.
2. (A) carries a `> **Superseded.**` banner, but it is scoped to the **`rho_q =
   1/hbar_q^2` ansatz**, NOT to the `T_q = hbar_q` definition. So the
   definition is live as far as the block says.

## What would settle it

Cheapest discriminating question: does anything CONSUME `T_q` numerically, and
does any consumer sit at `q < 1`? If every consumer is at `q > q_0` the two maps
never meet and "different objects" is safe to write down. If a consumer crosses
`q = 1`, (A) hands it a sign change and that is a defect.

Not measured yet. Grep `T_q`, `quantum-temperature`, `beta_q` across `content/`,
`computations/` and the `.lean` tree.

## Why it matters beyond bookkeeping

Every low-q threshold in the corpus (`q_gold = 0.382`, the convention-C melt at
`1/psi^2 = 0.4656`) is on the far side of the aeon boundary `q = 1`, where (A)
gives negative temperature and `t_P` changes sign. Whether those thresholds are
"the universe heated up" or "the universe cooled past its own Planck boundary"
is decided entirely by which of (A)/(B) is the physical map — and the two blocks
that name those thresholds are currently written in opposite languages.

## Scope

Scope-(a): this records a disagreement between two blocks and does not claim
either is wrong. Nothing here is wired, no value is proposed, and no `c_k` is
involved. NOT blocking `qou-vvv4` — the melt-block correction is defensible
without resolving this, because it only has to agree with its own parent
theorem, which makes no temperature claim at all.


## RESOLVED 2026-08-30 — the two maps have DISJOINT DOMAINS, and my framing above was misleading

PR #6299. Resolved by compiling the thing rather than reading it.

**The answer.** `T_q = hbar_q = (q-1)/q` is defined only over
`ArchimedeanSubstrateField`, which carries the classicality bound as a
STRUCTURE FIELD:

    field_ge_one : forall (p : M), 1 <= field p

with the docstring "q(p) = 1 is the classical limit (hbar_q = 0); q(p) > 1 is
the quantum regime, where the physical substrate sits". Its range is `[0,1)`,
proved by `quantumPlanckConstant_nonneg` + `quantumPlanckConstant_lt_one`.

So below the aeon boundary `T_q` is **not negative — it is UNCONSTRUCTIBLE.**
You cannot build the structure at `q < 1`. Map (B)'s effective-q regime
(descending to `q_gold = 0.382`) lies wholly outside map (A)'s domain, so the
two never compete. "They are different objects" is correct, and the corpus
carries the reason in a docstring; it was simply never written where the
temperature question is asked.

**CORRECTION of my own table above.** I wrote that deconfinement "sits where
(A) reports a negative temperature" and tabulated `T_q = -1.618` at `q_gold`
and `-1.148` at `1/psi^2`. Those numbers are arithmetically right and
epistemically wrong: they are the formula evaluated OUTSIDE ITS TYPE. The
framework assigns no temperature there at all. Do not quote that table as
evidence of a sign problem.

**What the discriminating test actually found.** The test I proposed was
"does any numerical consumer of T_q sit at q < 1". Measured: there are **ZERO**
numerical consumers — every `computations/` hit is `_deprecated/` or an
unrelated `net_q` / softmax `temperature`. Five content blocks `uses` it
(quantum-pressure, boltzmann-constant, molecular-hbond-phase-transition,
quantum-temperature-interpretation, and boltzmann-constant-proof) and none
evaluates below 1. So the question was answerable from the type alone.

**Found en route, and it is the bigger finding:** six content-block Lean
siblings under `information-theory/` DID NOT COMPILE, left behind by the
`SubstrateParameter` -> `ArchimedeanSubstrateField` split. 31 theorems
recovered, all axiom-clean. Two further files fail for other causes
(`substrate-parameter-exists` on a missing dep, `quantum-planck-constant` on
something else) and are NOT this class — unclaimed, worth their own bean.
