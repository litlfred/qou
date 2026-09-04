---
# qou-xwur
title: Isospin lives in the two-row partition channel, not the bond channel
status: todo
type: task
created_at: 2026-09-04T06:48:03Z
updated_at: 2026-09-04T06:48:03Z
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
