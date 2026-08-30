---
# qou-re90
title: Two blocks map q to temperature in OPPOSITE directions, and nothing adjudicates them
status: todo
type: task
priority: normal
created_at: 2026-08-30T16:51:46Z
updated_at: 2026-08-30T16:52:24Z
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
