---
# qou-xwur
title: Isospin lives in the two-row partition channel, not the bond channel
status: in-progress
pr: 8268
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T06:48:03Z
updated_at: 2026-10-04T15:21:00Z
parent: qou-v2om
---


Opened 2026-09-04 from the `qou-mu1h` / `qou-bygw` post-mortem. **Has results
already** — this is not a speculative bean.

## The correction that makes it work

Last turn I recommended this direction on the grounds that `prop:wigner-np-pairing`
ties the np preference to the SELF-CONJUGATE `(2,2) |- 4` partition. **That reason
is false as a general mechanism.** Self-conjugate partitions surviving convention
D's `<= 2`-row Wenzl cut exist at exactly three mass numbers:

| A | self-conjugate | and `<=2` rows |
|---|---|---|
| 1 | (1) | (1) |
| 2 | none | NONE |
| 3 | (2,1) | (2,1) |
| 4 | (2,2) | (2,2) |
| >= 5 | (3,1,1), (3,2,1), ... | **NONE** |

So a self-conjugacy-based Wigner channel is empty for every `A >= 5` and for
`A = 2`. Had that been the mechanism it would have been dead on arrival.

## The actual mechanism

Two-row partitions of `A` **are** the isospin multiplets:

    lambda = (a, b),  a + b = A,  T = (a - b)/2,  |N - Z| = a - b = 2T,

with Wenzl weight `y = [2T+1]_q / Z` — the quantum dimension of the isospin
multiplet. This exists for **every** `A`; self-conjugacy at `A = 4` is a
coincidence, not the channel. That reframes the Wigner block: its content is the
two-row label, and `(2,2)` is just where the label happens to also be
self-conjugate.

## Measured, no fitting, no free parameters

Candidate asymmetry term `-alpha log([2T+1]_q)` with `alpha` the existing
normalisation. Added to the chain bond model, the most-bound isobar becomes:

| A | peak Z, bond only | peak Z, bond + isospin | real |
|---|---|---|---|
| 4 | 1 | **2** | 2 |
| 6 | 1 | **3** | 3 |
| 8 | 1 | **4** | 4 |
| 12 | 1 | **6** | 6 |
| 16 | 1 | **8** | 8 |
| 20 | 1 | 1 | 10 |

Five exact, then collapse. The bond channel alone puts every peak at `Z = 1`
(`dB/dZ = -1.747` MeV per proton), so the isospin term is doing real work.

## Why it collapses, and it is structural

`-log[2T+1]_q` is **logarithmic** in `T`; the bond drift is **linear** in `Z`. The
isospin swing across the full range is about `alpha log(A+1)`, the bond drift is
about `1.747 (A/2 - 1)`, and linear beats log near `A ~ 18-20`. The SEMF asymmetry
term is `-a(N-Z)^2/A`, quadratic. So the direction is right and the FORM is wrong,
and no choice of `q` fixes it: quantum dimensions grow like `[m]_q`, so their logs
grow like `log m`. Getting `(N-Z)^2/A` out of a log of a quantum integer needs an
extra mechanism that is not present.

## What is NOT established, and it is most of it

- [ ] **The A=4..16 hit is nearly free and does not discriminate.** Any term
      monotonically peaked at `T = 0` puts the maximum at `Z = A/2` for these `A`.
      That is one bit per nucleus. The location test is close to vacuous.
- [ ] **The magnitude is completely untested.** Compare the asymmetry ENERGY
      against the SEMF coefficient `a_A ~ 23 MeV`, not the peak location. This is
      the test that could actually kill it, and it has not been run.
- [ ] Derive the `-alpha log(y_T)` form rather than positing it. Right now it is
      an ansatz chosen because `y_T` is the weight that exists.
- [ ] Reconcile with `prop:wigner-np-pairing`, whose 6.2894 MeV is a single
      number at `A = 4`; does the two-row reading reproduce it or replace it?
- [ ] Decide whether the bond channel should be present at all once isospin is in
      the partition channel — the `-1.747` drift is what the isospin term is
      fighting, and it may simply be spurious.


## The parity separation is now FORMALISED — 2026-09-14, sorry-free

`folio/quantum-observable-universe/lean/QOU/MassTheory/BondChannelTzParity.lean`
(13 theorems, no `sorry`, axioms `[propext, Classical.choice, Quot.sound]` on
every one; sweep 7 ok / 0 RED).

This bean's last open item reads: *"Decide whether the bond channel should be
present at all once isospin is in the partition channel — the `-1.747` drift is
what the isospin term is fighting, and it may simply be spurious."* There is now
a structural reason to doubt that channel, and it is proved rather than measured.

**The bond channel is odd in `T_z`, at every `q > 1`.** The corpus already
defines `interfaceFactor q t = zD q - hq q * t` with `t = 0` the p–p bond and
`t = 1` the n–n bond. Reading `t` against the pair isospin projection gives
`t = (1 - T_z)/2`, so the factor is affine in `T_z` and its parity is forced:

    f(T_z)   = (zD - h/2) + (h/2)*T_z
    even part = zD - h/2          (constant — does not see T_z)
    odd part  = (h/2)*T_z
    f(pp) - f(nn) = h             exactly

Charge symmetry — that the *strong* channel does not distinguish p–p from n–n —
demands evenness. It holds **iff `h(q) = 0` iff `q = 1`**. So the deformation
itself breaks charge symmetry and no choice of `q > 1` avoids it. Scope **(b)**,
with the invariant cited: the `T_z`-odd part of an affine function is its slope.

The writhe normalisation does not rescue it — under `t = (1-T_z)/2` the term
`-(t - 1/2)·log(1-h)` is `(T_z/2)·log(1-h)`, itself purely odd, so it adds a
second odd term. `bondL_pp_ne_nn` follows in one line from the already-proved
`bondL_strictMono`.

**This bean's channel is even for free.** Two-row `λ = (a,b)`, `T = (a-b)/2`,
weight `[2T+1]_q` — it reads only `|T_z|`, so `multipletWeight_even` holds for
every `q`, trivially. That triviality is the finding: evenness costs the
multiplet channel nothing and is **unavailable** to the bond channel at any
`q > 1`. `channels_opposite_parity` states the separation.

**What it does not settle.** It does not show an even-in-`T_z` bond factor exists
in the Hecke algebra, does not show `[2T+1]_q` is the *right* even object, and
says nothing about magnitudes — so this bean's other open items, in particular
*"the magnitude is completely untested … compare against the SEMF coefficient
`a_A ~ 23 MeV`"*, are untouched. It locates the violation; it does not repair it.

Related: the `-1.747` drift is the same number as bean `qou-1pig`'s
`α·ln(f_pp/f_nn) = 1.74707324276 MeV`, which that bean measures as 2.287× the
observed Coulomb displacement.

Bean stays `todo`.


### Correction to the entry above, same day

That entry said the parity separation "is now formalised" without saying how much
of it already was. Corrected after a corpus-grep:
`QOU.MassTheory.BondChargeRule.sumRule_like_pairs_differ` **already** proves the
like-pair difference (abstract charge parameterisation, `2c`), and its own
docstring cites `qou-1pig` and writes `f_pp − f_nn = h = 2·(h/2)`;
`pair-layer-isospin-parity.witness.json` already records the odd part as `h/2`
"forced exactly by the Hecke skein relation", with the isovector term **1454×**
the isoscalar one. Both verified directly, not taken from the report.

New in `BondChannelTzParity.lean` is therefore narrower than that entry implies:
(1) the **iff quantified over `q`** — even in `T_z` iff `q = 1`, which turns the
measured defect into a scope-(b) exclusion; (2) the **energy** level, where the
writhe term is itself purely odd so it adds a second odd term rather than
cancelling; (3) the **parity separation** against this bean's multiplet channel.
