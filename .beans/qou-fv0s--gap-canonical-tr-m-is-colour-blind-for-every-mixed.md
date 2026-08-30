---
# qou-fv0s
title: 'GAP: canonical tr_M is colour-BLIND for every mixed nucleus — the sign wire format cannot carry R3'
status: todo
type: task
priority: normal
created_at: 2026-08-30T18:21:32Z
updated_at: 2026-08-30T18:22:29Z
---

## The canonical tr_M path structurally cannot honour owner ruling R3

Owner ruling 2026-08-15 (R3) makes `bring_color_weighted` the canonical p/n
convention. The canonical Markov-trace producer cannot apply it.

`canonical_braid_crossings.sign_for_ctype` says so in its own docstring:

  > ⚠ **Lossy for `averaged_weighted`, by construction.** A sign cannot carry a
  > magnitude, so both averaged interfaces collapse onto `0` — the colour-blind
  > projection. The p-n colour weighting `-h(1/2 - δ/4)` is *not* representable
  > in this format at all.

`canonical_tr_m_via_rust` wires the word to the Rust engine as signs in
{−1, 0, +1}. So **`averaged` and `averaged_weighted` both go over as 0**, and
every trace it returns is colour-blind.

## Where it bites — measured

Colour weighting is the **p–n interface** crossing: absent for a free nucleon,
exactly one per mixed nucleus.

| atom | ctypes | colour-weighted | canonical tr_M (colour-BLIND) |
|---|---|---|---|
| p | σ 6, σ⁻¹ 3, avg 2 | **0** | 1.14575969245730086935241774516176649113 |
| n | σ 5, σ⁻¹ 4, avg 2 | **0** | 0.98774368811580957144294046174148798302 |
| D | σ 11, σ⁻¹ 7, avg 4, **avg_w 1** | **1** | 0.57509087162981031565376396300046787027 |
| T | σ 16, σ⁻¹ 12, avg 6, **avg_w 1** | **1** | 0.22927766053968917795626336907991385602 |
| ³He | σ 23?, avg_w 1 | **1** | 0.40370991405397142157994463601783332536 |
| ⁴He | σ 23, σ⁻¹ 15, avg 8, **avg_w 1** | **1** | (still computing) |

**For p and n the colour-blind value is CORRECT** — a free nucleon has no p–n
interface, so there is nothing to weight. **For D and every heavier nucleus it
is not**: the one interface crossing that carries the proton-neutron colour
asymmetry is being sent over as the colour-blind `0`.

## Magnitude

δ (flavour split) = 0.001375710807027096, h = 0.20906029879563937:

    averaged           d = -h/2        = -0.10453014939781968
    averaged_weighted  d = -h(1/2-δ/4) = -0.10445824776972631
    relative difference                = 6.87855e-4

matching to the digit the `6.879e-4` that `classify_crossing`'s own comment
records. One such crossing per nucleus, so this is a ~7e-4-scale effect on one
of 23–47 crossings — **small, and not an explanation for the 42–85 % spread
among the six tr_M(p) values**. It is a correctness question, not a magnitude
one.

## `qou-gdtb` is marked COMPLETED while its own named residual is live

`sign_for_ctype`'s docstring ends: *"The representational gap itself stays open
under bean `qou-gdtb`."* That bean's status is **completed**. What it closed is
real — `classify_crossing` now returns the two labels distinctly, which is what
made this measurable — but the gap it names is demonstrably still there: the
sign format still collapses both onto 0, in code I read today.

So either the docstring is stale or the bean closed early. **The code is the
evidence**, and it says the gap is open.

## What is NOT claimed

That the Rust engine is wrong, or that the colour-blind numbers are wrong *as
colour-blind numbers*. The wire format is documented and deliberate. What is
missing is a path from `d_for_ctype` (which is exact, and carries the weighting)
to a canonical trace for mixed nuclei. Closing it means either widening the wire
format past a sign, or computing mixed-nucleus traces through the Python ctype
route instead — a design choice, not a patch.
