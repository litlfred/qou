---
# qou-07vh
title: Measure the q-degree of the six atom NF coefficients vs A
status: in-progress
pr: 8205
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T18:08:19Z
updated_at: 2026-10-04T15:13:19Z
parent: qou-v2om
---

## What is being measured (PR #6304, branch `claude/nf-q-degree-2026-08-30`)

`hecke_core_symbolic.build_atom_nf_sym(Z, N)` returns the atom's Hecke normal
form as six coefficients carried symbolically in `q`. Their **q-degree counts
crossings**: the coefficients are built by repeated `hm_sym(nf, 1, d, gen)`,
i.e. by multiplying by `(σ_gen + d·I)` with `d ∈ {0, −h, −h/2}` and
`h = q − q⁻¹`, and each such factor moves the Laurent degree by at most one.
So the degree reads the braid word's length off algebraically — no `q₀`, no
anchor, no AME.

Probe: `computations/substrate/atom_nf_q_degree_probe.py`.

## Method note (the gate is the interesting part)

Two implementations cross-checked before any number is reported: the
authoritative `hm_sym` (sympy) and an exact Laurent-dict mirror
(`dict[int, Fraction]`) fast enough to reach A=40. The gate runs both builds
**in lockstep and compares after every factor** (6 nuclei / 174 steps), not
just the final vectors — a control-flow transcription error is then caught at
the step it happens rather than hidden by a later cancellation.

`sp.expand` on the sympy side each step is not optional: `build_atom_nf_sym`'s
unexpanded expression tree is not traversable at A ≥ 3 (a first attempt that
compared final vectors with `sp.cancel(sp.expand(...))` hung and was killed).

## Results

1. **Crossing count is exactly `11A + C(A,2) + Z`** — verified against the
   measured factor count on all 17 nuclei, ¹H … ⁴⁰Ca.
2. **Every coefficient is bar-even or bar-odd, never neither**, and which one
   is fixed by the parity of the crossing count: `{γ, L₊, L₋}` carry
   `(−1)^steps`, `{σ₀, σ₁, e⁻}` the opposite. The NF vector is bar-graded by
   word length.
3. **All exponents in a slot share one parity**, and for A ≥ 12 the slot is
   dense in that sublattice (`gaps = 0`): the coefficient is `q^{−D}·P(q²)`
   with `P` of full degree `D`. The degree is not a sparse leading term that
   could cancel downstream.
4. **The degree is quadratic in A, and the quadratic is entirely the
   inter-nucleon loop** — settled by ABLATION, not by a fit. Rebuilding with
   `for prev in range(k)` switched off:

   | | span (N=Z chain) | 2nd difference in A |
   |---|---|---|
   | loop OFF | `23A − 2` | **0** → linear |
   | pair crossings alone | `A² − 9A + 44` | constant → leading coeff exactly 1 |
   | loop ON (as written) | `A² + 14A + 42` | constant → quadratic |

   Exact integer arithmetic on measured integers; closed forms checked at
   every point, no tolerance. Off the N=Z chain the Z-dependence is real
   (³H span 68 vs ³He 74), so the closed forms are stated for N=Z only.

## Why it matters for `qou-brng`

The q-degree is an algebraic readout of **which bond set a producer's braid
word encodes**: complete graph → `A²/2`; bounded/chain coordination → linear.
Measured, `build_atom_nf_sym` encodes the complete graph — the bond set
`QOU.Mass.CoordinationSaturation` proves gives `B/A = ε·(A−1)/2`, unbounded,
no plateau, and which observed saturation refutes.

Eleven other non-deprecated files carry the same `for prev in range(k)` loop.

Scope: **scope-(a)** about these producers. It does not say the framework's
physics requires the complete graph, and it does not decide the
coefficient/mechanism question `qou-brng` is open on.

## Open follow-up

`computations/closed_form_tau_M.py::closed_form_ratio` uses a DIFFERENT bond
set — `for k_idx in range(A-1)` over adjacent pairs of `["p"]*Z + ["n"]*N`,
i.e. the LINEAR CHAIN, A−1 bonds. So two inequivalent bond sets are live in
the corpus (already noted from the other direction in
`pn_convention_flip_effect_probe`). Both are hit by an existing sorry-free
result in this arc: the complete graph by `CoordinationSaturation`, the chain
by `ChainBondOrderDependence.orderIndependent_iff` (arrangement-invariant iff
`L_pp = L_pn = L_nn`, and `closed_form_ratio` uses three manifestly different
factors `z`, `z − h`, `z − h(1/2 − δ/4)`). Not yet written up; needs its own
measurement before any durable claim. See also `qou-48is`.


## Extended: three bond sets, and the sibling's Z=0 artifact (2026-08-30)

**The measurement upgraded from an ablation to a three-way comparison**, which is
what actually supports the diagnostic claim. Changing ONLY the pair-bond set,
N=Z chain A=12..40, exact integer finite differences:

| bond set | in the corpus | growth |
|---|---|---|
| complete graph `C(A,2)` | `build_atom_nf(_sym)` | **quadratic**, leading coeff exactly 1 |
| adjacent chain `A−1` | `closed_form_ratio`, `atom_braid_word_3A(include_inter=True)` | **linear**, 25/nucleon |
| none | `atom_braid_word_3A` **default** | **linear**, 23/nucleon |

**Measured on `atom_braid_word_3A` directly** (all (Z,N), A=1..8), not inferred
from the flag name: `include_inter=True` adds exactly `A−1`, **not** `C(A,2)`,
and the default is `False`. `binding_canonical.py:528-530` computes binding as
the difference of the two words, its own comment reading
`resid_exp = 5*(2A−1)  # 10A−5 = per-object (A nucleons + A−1 bonds)`.

So there are **three** bond sets live across the atom-word builders, in two
growth classes.

## Sibling coordination — a correction delivered before it cost them

Sibling PR **#6306** (`qou-tower`) opened on the same measurement minutes after
#6304, independently reaching the same Laurent-dict technique.

* **Independent agreement at A=1** — all six degrees and all six term counts,
  both nucleons, two implementations. Banked as a correctness gate.
* **Their headline is a Z=0 artifact.** They report the span peaking at A=5 (94)
  then falling (86, 76, 72) and were about to scan to A=20 reading it as
  possible shell structure. Those four numbers are exactly the **Z=0** column;
  max over Z at each A is 22, 48, 76, 106, 138, 172, 208, 246 — strictly
  increasing, ΔΔ = 2 constant, quadratic. Pure-neutron matter maximises
  cancellation (nn bonds carry `d = −h` in both slots; the charge-closure loop
  is empty at Z=0). Flagged on #6306 before their scan ran.
* Genuine non-monotonicity exists but in **Z at fixed A** (A=8: Z=1→2 dips
  164 → 158), a different axis, needing A ≥ 8 to see. One dip is not a pattern.

Also flagged on **#6302** (same bean `qou-brng`): its §2 rests on the count
channel being affine in A, which holds — but because the default word carries
no pair bonds, a scope label the PR does not currently carry.

## Method traps worth keeping

1. **`sp.expand` after every `hm_sym` step.** Comparing final vectors with
   `sp.cancel(sp.expand(...))` hangs at A=3: the unexpanded result is a DAG in
   memory that sympy walks as a tree. #6306 independently hit this as an 862 s
   A=2 verify.
2. **Compare in lockstep, not at the end.** The gate compares after every
   factor, so a control-flow transcription error surfaces where it happens
   rather than being masked by later cancellation — which matters precisely
   because cancellation is what the Z=0 line is made of.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress Update (PR #8205)
- [x] Pure Lean 4 formalization wired into `QOU.lean` (`AtomNFQDegreeBondSetDichotomy.lean`, `TwoNucleonChannelSignObstruction.lean`, `PairLayerLinearRampParity.lean`, `ChainMirrorSplittingChargeSymmetry.lean`; 0 `sorry`, 0 vacuity advisories across all 6 static audits)
- [x] 50-dps `mpmath` + exact `TL_3` Laurent polynomial probe (`computations/probes/atom_nf_qdegree_pair_ramp_mirror_probe.py`) and stamped witness (`computations/probes/atom-nf-qdegree-pair-ramp-mirror-probe.witness.json`, 0 raw `float64` fields)
- [ ] Awaiting adversarial review and Merge Manager merge of PR #8205 (`ready: ed5c0c87c86301f2666c843555cc576831d17a74`)
