# The body-order cumulants are the finite differences of one function

**Date:** 2026-08-30
**Bean:** `qou-edt7` (the successor question: what assembly produces `b₃ > 0`)
**Lean:** `QOU/Mass/CoordinationWeightDifferences.lean` — sorry-free, `lean`-direct exit 0, 11 declarations, standard axioms only
**Probe:** `computations/probes/body_order_is_finite_difference_of_coordination_weight_probe.py` — 5/5 assertions

## The question

`qou-edt7` records a trilemma, now machine-checked from both sides:

| assembly | forces | Lean |
|---|---|---|
| multiplicative Mayer, `W = 1 − Π f` | `b₃ < 0` | `MayerThreeBodySign.lt_of_b3_pos` |
| pairwise-additive, `B = Σ f(μ)` | `b₃ = 0` exactly | `PairwiseCumulantVanishing.b3_eq_zero_of_isPairwise` |
| **nature (AME2020)** | **`b₃ = +1.426220 MeV > 0`** | — |

The bean asks what replaces the assembly, and forbids the obvious cheat: *"do not
propose a functional chosen because it lands `b₃ > 0` — that is the anchor
inversion in new clothes."*

**This does not propose a functional.** It changes variables, and under the change
of variables the two walls turn out to be one wall seen from two sides.

## The change of variables

Write a binding map on the mass number as

    B(A) = C(A,2) · w(A−1),        z := A−1,   w(z) := B(A) / C(A,2)

`w(z)` is the **mean binding per nucleon pair** at coordination `z`. This is a
definition, not a model — given any `B`, that formula recovers it. Nothing is
assumed by writing it down and nothing is lost.

## The identity

Under it the Ursell/Möbius cumulant of order `n` becomes, exactly,

    bₙ = C(n,2) · Δ^{n−2} w(1)

with `Δ` the forward difference. The proof is **term by term**, not a summation
identity: the subset-of-a-subset rule `C(n,k)·C(k,2) = C(n,2)·C(n−2,k−2)` matches
the two sums entry for entry under `k = j+2`, signs included. The `k = 0, 1` terms
drop out because a bare nucleon carries no pairs.

**Scope on generality.** `n = 3` and `n = 4` are Lean-proved. The general `n` case
is verified symbolically against an arbitrary `w` for `n = 2…8` in the probe. That
is a check, not a proof, and is not claimed as one.

## What it buys

An infinite tower of unknown many-body coefficients is **one unknown function of
one integer variable**, and the three facts the corpus proved separately become
three readings of its shape:

| statement about `w` | cumulant consequence | status |
|---|---|---|
| `w` constant | `b₃ = b₄ = 0` | `b3_eq_zero_of_const` — recovers the pairwise wall as the `Δw = 0` case |
| `w` non-increasing | `b₃ ≤ 0` | `b3_nonpos_of_le` |
| `w(1) < w(2)` | `b₃ > 0` | `lt_of_b3_pos` — the falsifiable form |
| `w` convex at `z=1` | `b₄ > 0` | `lt_of_b4_pos` |

**The Mayer sign is not a separate obstruction.** Any saturating assembly has a
non-increasing `w`, and `b3_nonpos_of_le` sends every one of them to `b₃ ≤ 0`. The
multiplicative form's `b₃ < 0` is an instance of that, not a coincidence — which
is why changing the edge set, the like-pair typing or the energy scale never moved
the sign. They do not change whether `w` rises.

So **`b₃ > 0` is not exotic and needs no new functional.** It says exactly one
thing:

> the mean binding per pair is larger at coordination 2 than at coordination 1.

Measured: `w(1) = 2.2245662`, `w(2) = 2.6999729` MeV per pair, a rise of `0.4754`.

## The measured shape of `w`, and where the blow-up comes from

| A | z | | B/A | `w(z)` |
|---:|---:|---|---:|---:|
| 2 | 1 | ²H | 1.11228 | 2.2245662 |
| 3 | 2 | ³H/³He avg | 2.69997 | 2.6999729 |
| **4** | **3** | **⁴He** | **7.07392** | **4.7159437** |
| 5 | 4 | ⁵Li | 5.26613 | 2.6330662 |
| 6 | 5 | ⁶Li | 5.33233 | 2.1329325 |
| 9 | 8 | ⁹Be | 6.46267 | 1.6156673 |
| 16 | 15 | ¹⁶O | 7.97621 | 1.0634943 |
| 56 | 55 | ⁵⁶Fe | 8.79036 | 0.3196493 |

`w` **rises to a sharp maximum at the α particle and then decays monotonically.**
That single shape carries both open constraints at once, and they pull in opposite
directions:

* `b₃ > 0` ⟺ `w` rises at `z = 1`;
* saturation of `B/A` ⟺ `z·w(z)` is bounded, so `w(z) → 0`.

**So `w` must be non-monotone.** Any derivation that produces a monotone
coordination weight is refuted by one or the other, whichever end you check.

And the `A ≥ 5` blow-up gets a cause. High forward differences of a peaked
function grow and alternate; the tower multiplies them by a growing `C(n,2)`:

| n | `Δ^{n−2} w(1)` | `bₙ` |
|---:|---:|---:|
| 2 | 2.2245662 | 2.2245662 |
| 3 | 0.4754067 | 1.4262202 |
| 4 | 1.5405641 | 9.2433846 |
| 5 | −5.6394124 | −56.394124 |
| 6 | 11.321004 | 169.81507 |

The body-order series expands a peaked `w` around `z = 1`, **three steps below its
maximum**. The divergence is a defect of the expansion point, not evidence against
the assembly. That reframes the blow-up from "the framework is wrong at A ≥ 5" to
"this is the wrong series to expand", which is a different and much cheaper
problem.

## What this does NOT buy — read before citing

The identity is a **reparameterisation** and is therefore tautologically
available. **It derives no magnitude and cannot.** `w` is defined by inverting `B`,
so fitting `w` to AME2020 is fitting the binding to AME2020 with extra steps.
Nothing here closes the magnitude gate and nothing here should be cited as
evidence that it is closer to closing.

What it establishes is narrower and, I think, still worth having: the target is one
function of one integer variable rather than an infinite tower; the two proved
walls and the blow-up have a single common cause; and the open question has a
one-line falsifiable statement — **why does `w` rise from `z = 1` to `z = 2`, and
why does it turn over at the α particle?**

## Verification

- `lean`-direct exit 0 against the real Mathlib import cone (restored olean cache; **no** `lake build` — the tree carries `.lake/RESTORED-NO-TRACES` and a build would evict it, per `qou-r13s`).
- `#print axioms` on all 11 declarations: `propext` / `Classical.choice` / `Quot.sound` only. No `sorryAx`, no `sorry`, no `native_decide`.
- Probe 5/5, mpmath at 65 dps, no float64 anywhere; AME values read from the vendored table via `codata_constants.ame_binding_mev`, not hardcoded literals.
- `scripts/precision-gates.sh --changed` exits 1 on seven gates that are **red on `main`**; the full output mentions none of these three files, so this change widens none of them. Five audit witnesses were rewritten as a side effect of running the gates and were reverted: three carry an **environment downgrade** (records hold scipy 1.17.1 / sympy 1.12 / mpmath 1.4.1; this container has no scipy and mpmath 1.3.0). One of them, `witness-provenance-audit`, moved `PROV_MISSING` 78 → 94 — a real movement, not mine, and not separable from the environment change; flagged here rather than committed.
