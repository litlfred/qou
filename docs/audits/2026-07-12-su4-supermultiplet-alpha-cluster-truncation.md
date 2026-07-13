# SU(4) [1ⁿ] supermultiplet truncation — the algebraic source of the corpus's α-cluster binding geometry

**Date:** 2026-07-12 · **Axis:** Δ_λ / binding closure (the many-body building block) ·
**Tier:** structural-exact (`C(4,n)` combinatorics) + Wigner-supermultiplet reading (textbook) ·
**No fit, nothing wired, no tier change.** Structural synthesis connecting two established
corpus results.

## What this connects

Two corpus results, never linked:

- **#3569 / `SU4SupermultipletGate`** (sorry-free Lean): the fully-antisymmetric nucleon-flavor
  supermultiplet `[1ⁿ]` of SU(4) (4 flavors p↑p↓n↑n↓) has `dim[1ⁿ] = C(4,n)`, which **vanishes
  for n>4** — the measured ⁴He locality (super-pairwise excess 2.093× at ⁴He, →0.944× at ⁶Li
  where `C(4,6)=0`).
- **GAP-1 / qou-lzoh** ([`gap1_max_contact_a5plus.py`](../../computations/gap1_max_contact_a5plus.py)):
  the A≥5 binding backbone is the max-contact convex **deltahedron** (`E=3A−6`) — the
  Hafstad–Teller / Brink **α-cluster** geometry, adopted **empirically** (it maximizes contact
  and tracks AME).

A corpus-grep (per the anti-over-claim discipline) confirms the SU(4)-saturation ↔ α-clustering
link was **not previously explicit** in the corpus, even though it is textbook Wigner
supermultiplet theory.

Probe [`su4_supermultiplet_alpha_cluster_truncation_probe.py`](scripts/su4_supermultiplet_alpha_cluster_truncation_probe.py)
→ [witness](scripts/su4-supermultiplet-alpha-cluster-truncation.witness.json) (4/4).

## The synthesis

| n | `dim[1ⁿ] = C(4,n)` | meaning |
|---|---|---|
| 0…4 | 1, 4, 6, 4, **1** | supermultiplet ladder; the top `[1⁴]` (dim 1) is the **α singlet** (⁴He closed s-shell) |
| >4 | **0** | no `[1^{>4}]` nucleon supermultiplet (only 4 flavors) — the channel **truncates at n=4** |

**The argument.** A body-order binding tower whose n-body term lives in the `[1ⁿ]`
antisymmetric channel (the Wigner supermultiplet hypothesis — exactly what the #3569 gate
encodes for the 4-body term) has **no direct n-body term for n>4**, since `C(4,n>4)=0`. So A>4
binding **cannot** proceed via a single `[1^A]` supermultiplet; it must proceed by **clustering
4-body `[1⁴]=α` blocks** — which is precisely the Hafstad–Teller / Brink α-cluster geometry
GAP-1 uses.

**The convergence.** The empirical α building block (GAP-1, geometric: max-contact deltahedra)
and the algebraic α building block (SU(4), `[1ⁿ]` truncation at n=4) are the **same** — two
independent routes agreeing. The ⁶Li locality zero the corpus *measured* (`C(4,6)=0`,
super-pairwise excess →0.944×) is the same truncation GAP-1's A≥5 geometry needs, seen
algebraically rather than geometrically. So the α-cluster choice is **forced by the
already-Lean-proved supermultiplet gate**, not an independent geometric fit.

## What this buys, and what it does not

- **Buys:** GAP-1's empirical "use α-cluster deltahedra" is reduced to a **consequence** of the
  Lean-proved SU(4) `[1ⁿ]` gate — one fewer free model choice. The α building block is derived
  (algebraically) rather than adopted (geometrically).
- **Does not buy (STRICT scope guard):**
  - It does **not** derive the per-order `M_n` weights — **qou-v0yw stays open**. This explains
    the *building block* (why the α), not the *counts*.
  - It **wires nothing** and changes no production. The `C(4,n)` gate is already Lean-proved; the
    α-cluster geometry is already in GAP-1. This connects them.

## Update (2026-07-12): the flavor factor is Schur–Weyl-*derived*, not a hypothesis

The original scope guard flagged the "n-body term lives in `[1ⁿ]`" step as the *Wigner
supermultiplet hypothesis*. That step is **upgraded to a theorem for the flavor factor** by
**Schur–Weyl duality** (probe
[`su4_schur_weyl_flavor_factor_probe.py`](scripts/su4_schur_weyl_flavor_factor_probe.py)
→ [witness](scripts/su4-schur-weyl-flavor-factor.witness.json), 3/3):

- On `(C⁴)^{⊗n}` (n nucleons, 4 flavors), `(C⁴)^{⊗n} = ⊕_{λ⊢n,≤4 rows} V_λ^{GL₄} ⊗ S_λ^{Sₙ}`.
  The fully-antisymmetric n-body flavor channel is `λ=[1ⁿ]`: `V_{[1ⁿ]}^{GL₄} = ∧ⁿ(C⁴)`, of
  dimension **`C(4,n)` exactly** (Weyl dim formula = exterior power). So the `C(4,n)` is the
  flavor degeneracy **by the Schur–Weyl theorem**, not by assumption.
- Its `n>4` vanishing is **Pauli exclusion on 4 flavors** — *specific to the antisymmetric
  channel* (the symmetric `[n]` dimension `C(n+3,3)` stays nonzero for all n). So the n=4
  truncation is a Schur–Weyl fact, not a fit.
- **Weight factorization:** `w_n = C(4,n)_flavor · w_n^{spatial}`. The **flavor leg** `C(4,n)`
  is now **derived**; the **spatial leg** `w_n^{spatial}` (the Specht/Hecke binding kernel) is
  the separately-**open** piece — exactly what the active **z2bn/lever1** "DERIVE the exact
  classical binding kernel" line is working. This closes the flavor leg and points the spatial
  leg at that line; it does **not** close `B` (spatial factor + `M_n(K)` still open), and wires
  nothing.

This is **distinct** from the deprecated Schur–Weyl *mass-trace* route (the `S_{3A}` braid/color
projection); this is the **4-flavor supermultiplet** side.

## Cross-references

- SU(4) gate + ⁴He locality: [`2026-07-05-delta-lambda-gate-status.md`](2026-07-05-delta-lambda-gate-status.md) (PROBE 2), #3569
- GAP-1 max-contact deltahedra: [`2026-07-11-gap1-max-contact-a5plus.md`](2026-07-11-gap1-max-contact-a5plus.md)
- M_n(K) body-order tower (qou-v0yw): [`2026-07-11-mnk-coordination-graph-body-order-tower.md`](2026-07-11-mnk-coordination-graph-body-order-tower.md)
- Δ_λ residual = many-body term (#3569): [`2026-07-11-deltalambda-o1-manybody-residual.md`](2026-07-11-deltalambda-o1-manybody-residual.md)
