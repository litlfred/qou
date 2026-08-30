---
# qou-tower
title: 'There is no tower: the production chain reduces every nucleus to the same 6 dims'
status: todo
type: task
priority: high
created_at: 2026-08-30T00:00:00Z
updated_at: 2026-08-30T00:00:00Z
---

Asked to walk the generative production chain step by step, look past the
Gröbner normal form at the **full tower**, and check whether twist data changes
on magic isotopes. Probe:
[`gamma_chain_tower_magic_probe.py`](../computations/probes/gamma_chain_tower_magic_probe.py), 3/3.

**The first magic number is 2**; the first *doubly*-magic nucleus is ⁴He
(Z = N = 2), which on the N = Z line the producer walks is A = 4.

## THE FINDING: there is no tower

The atom braid nominally lives in `H_{3A}` — 3 strands per nucleon. But
`build_atom_nf_mp` applies the **H₃ Gröbner–Shirshov reduction after every
crossing**, so the state is a 6-vector at every step of every nucleus.
Measured:

| | NF dimension |
|---|---|
| all 33 stages of Z=N=4 | **6** |
| hydrogen (Z=1, N=0) | **6** |
| lead-208 (Z=82, N=126) | **6** |

**Hydrogen and Pb-208 occupy the same state space.** The `H_{3A}` structure is
destroyed as it is built, so "the full tower" does not exist in this code path —
the GS normal form *is* the whole object, not a projection of something larger.

**That one fact explains every negative on this arc.** Nothing in the
construction can distinguish one nucleon count from another except through
smooth growth, so no shell signal is expressible — not in δ²Φ, not in the LP
dual, not in the shell SDP. The searches were not unlucky; the degree of
freedom is absent.

## Twist / framing data does not change at magic

Replaying the chain and accumulating signed crossings (`d=0` is σ, `d=-h` is
σ⁻¹, `d=-h/2` a mixed interface that is not a pure crossing):

    writhe(Z) = 3Z        exactly  ->  writhe/A = 1.5 for EVERY nucleus
    mixed(Z)  = Z² + 4Z   exactly

Both smooth polynomials, no feature at 2, 8, 20, 28. The crossing schedule is
fixed per nucleon plus an O(A²) pair loop; it has no shell dependence to carry.

## The LP cannot be asked about T₃,₅ receptivity

Swept `n_target` over 0.25, 0.5, 1, 2, 3, 4, 6, 8, 12, 16, 20, 28, 50, 82, 126,
200, 500, 1000 — the active set is the singleton `{γ}` at **every** target. It
is not the target choice: the LP is structurally one-dimensional on this
6-channel basis, so "is the isotope receptive to a different knot such as
T₃,₅" is not a question this LP can express.

## 🛑 A candidate signal at ⁴He — RETRACTED, and it was mine

The final NF at Z=2 has σ₁, L₊, L₋ collapse to ~1e-3 while every neighbour is
O(1–30) — the state condensing onto the trivial channel exactly at the first
doubly-magic nucleus. I flagged it as promising. It does not survive its
control. With `R = ||nf_non-γ|| / |nf_γ|`:

- **R is strictly monotone increasing over even Z** — 0.489, 0.808, 1.143,
  1.404, … → 2.959 at Z=30 — and the odd branch descends to the same limit
  from above (2.997 at Z=29);
- so **Z=2 is the global minimum by being the smallest even Z**;
- magic Z rank **1st, 4th, 10th, 14th of 15** among even Z — spread across the
  whole range.

Parity split plus monotone convergence: the same artifact δ²Φ turned out to be.
And *"is the global minimum magic?"* returns **True** while being empty — 2 is
both the smallest even number and the first magic one, so any
monotone-in-even-Z quantity answers yes. Fifth instance of the input-presented-
as-output pattern today, second one mine.

## Where this says to look instead

The tower has to survive. A construction that reduces to H₃ at each step cannot
carry shell structure, so the question is whether the chain can be run **without
the per-step GS reduction** — keeping the H_{3A} state and reducing only at the
end (or not at all). That is a real compute problem (dim H_{3A} = (3A)!), but it
is the only place a shell degree of freedom could live in this construction.

Note this is not the same as the `qou-mgq3` finding that `gram.py` is hardwired
to H₃. That was about the LP's channel space; this is about the state itself
being collapsed during production, upstream of any LP.
