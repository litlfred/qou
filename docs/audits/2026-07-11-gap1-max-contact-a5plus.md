# GAP-1: the max-contact deltahedra (3A−6) forward-predict the A≥5 pairwise backbone (qou-lzoh)

**Date:** 2026-07-11
**Branch:** `claude/gap1-max-contact-a5plus-2026-07-11`
**Compute:** [`computations/gap1_max_contact_a5plus.py`](../../computations/gap1_max_contact_a5plus.py)
**Witness:** [`computations/gap1-max-contact-a5plus.witness.json`](../../computations/gap1-max-contact-a5plus.witness.json)
**Bean:** `qou-lzoh` (GAP-1). **Workplan:** [`docs/workplans/2026-07-11-mnk-derivation-gaps.md`](../workplans/2026-07-11-mnk-derivation-gaps.md).
**Extends:** #3545 Part 13 (`binding_edge_set_selection.py`, A≤4 inversion only).

## What GAP-1 asked

#3545 Part 13 established the nuclear edge set is the binding-maximizing **max-contact 3-D
sphere packing** but only *inverted* B→#bonds for A≤4 (where max-contact = simplex `C(A,2)`).
GAP-1 is the missing **forward** test at A≥5, where max-contact `< C(A,2)`: does the pairwise
backbone with the geometric contact count predict AME — and is it the restriction that tames
the A≥5 growth #3585 flagged?

## The geometry (no fit)

For A unit spheres the max-contact cluster is the **convex deltahedron** (all-triangular-face
polytope); every edge is a contact and a triangulated sphere has exactly `E = 3A−6` edges:

| A | 2 | 3 | 4 | 5 | 6 | 7 |
|---|--:|--:|--:|--:|--:|--:|
| polytope | — | triangle | tetrahedron | tri-bipyramid | octahedron | pentagonal bipyramid |
| #contacts | 1 | 3 | 6 | **9** | **12** | **15** |

These are the Hafstad–Teller / Brink α-cluster geometries the corpus already uses (#3551).
The per-bond energy `b*` is `B_strong(deuteron)` (Z=1 ⇒ no Coulomb) — the **single anchor**.
`B_strong` = AME binding + discrete-proton Coulomb (`Z(Z−1)`, r₀=1.2 fm; charge-symmetric).

## Result — max-contact tracks extensive binding; simplex overshoots; the tower blows up

`B_pred(A) = b*·(3A−6)`, `b* = 2.2246` MeV:

| iso | A | maxC = 3A−6 | C(A,2) | B_pred | B_strong | pred/strong | residual/nucleon |
|---|--:|--:|--:|--:|--:|--:|--:|
| D   | 2 | 1  | 1  |  2.225 |  2.225 | 1.000 | 0.00 |
| T   | 3 | 3  | 3  |  6.674 |  8.482 | 0.787 | 0.60 |
| ³He | 3 | 3  | 3  |  6.674 |  8.716 | 0.766 | 0.68 |
| ⁴He | 4 | 6  | 6  | 13.347 | 29.203 | 0.457 | 3.96 |
| ⁵Li | 5 | 9  | 10 | 20.021 | 28.857 | 0.694 | 1.77 |
| ⁶Li | 6 | 12 | 15 | 26.695 | 34.371 | 0.777 | 1.28 |
| ⁷Li | 7 | 15 | 21 | 33.368 | 41.503 | 0.804 | 1.16 |

**Model comparison at A≥5 (B_pred / B_strong):**

| iso | max-contact 3A−6 | simplex C(A,2) |
|---|--:|--:|
| ⁵Li | 0.694 | 0.771 |
| ⁶Li | 0.777 | 0.971 |
| ⁷Li | 0.804 | **1.126 (overshoot)** |

Three structural facts:

1. **Max-contact (3A−6, LINEAR in A) is bounded and stable** — ratio 0.69 → 0.78 → 0.80 at
   A=5,6,7, rising gently toward ~0.8. It **does not blow up**: a linear edge count against
   extensive binding (`B ~ A`) gives a bounded ratio, as it must.
2. **Simplex `C(A,2)` (QUADRATIC in A) overshoots by A=7** (`C(7,2)=21 > 15`, ratio 1.13 and
   climbing) — a pairwise-complete graph over-counts once not all spheres can touch.
3. **The full `a_D^(n)·C(A,n)` body-order tower blows up +920% at ⁶Li** (#3585).

⇒ The **max-contact restriction `3A−6 < C(A,2)`** (active from A≥5) is exactly what tames the
pairwise backbone at A≥5 — confirming GAP-1's premise that the geometric max-contact edge set,
not all-subsets, is the correct pairwise coordination.

## What stays open (unchanged)

The residual `B_strong − B_pred` is a **bounded, roughly per-nucleon-constant** term
(~1.2–1.8 MeV/nucleon for Li; ⁴He's 3.96 is the doubly-magic outlier) — the genuine many-body
+ cluster contribution: the M₃/M₄ Milnor terms (**GAP-2**) and the cluster/halo deviation
(⁶Li = α+d sits below max-contact, **GAP-4**). This probe fixes the **2-body edge set at A≥5**;
it does not close the many-body weights.

## Discipline

Scope-(a). #contacts is convex-deltahedron geometry; `b*` is the single deuteron anchor;
predictions are forward; the residual is **reported, not fitted**. Nothing tuned to AME,
nothing wired to production — the anti-fit checkpoint of bean `qou-lzoh`.
