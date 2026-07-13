# conj:cyclotomic-boundary-at-keystone — the Habiro-tail cyclotomic boundary sits at n=5 (S₅), and the McKay 2I↔Ê₈ value map is the mechanism

**Date:** 2026-07-12
**Branch:** `claude/lever1-habiro-cofactor-not-salem-2026-07-12`
**Compute:** [`computations/lever1_cyclotomic_boundary_keystone_conjecture.py`](../../computations/lever1_cyclotomic_boundary_keystone_conjecture.py)
**Witness:** [`computations/lever1-cyclotomic-boundary-keystone-conjecture.witness.json`](../../computations/lever1-cyclotomic-boundary-keystone-conjecture.witness.json)
**Bean:** `z2bn`.

## Anti-duplication note (read first)

The D(m) **arithmetic** — closed forms, `(q−1)²` universal, bar-even, cyclotomic head + growing
generic (NOT Salem, NOT special-function) non-cyclotomic core — was **already derived on
2026-06-28** (Stages 7–9, `docs/audits/2026-06-28-lever1-binding-{correction-cyclotomic-core-
growth,core-bar-symmetric-irreducible,core-root-distribution}.md`, through m=11). This note does
**not** re-derive it. The McKay value map `d_q(λ)=[mark]_q` at the keystone was **derived on the
same day in #3685**
([`docs/audits/2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md`](2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md)).
This note **cites both** and adds the observations the corpus does not have: the boundary's
**alignment** with the framework's calibration/keystone structure, and the **rep-theory mechanism**
that ties the two merged results together.

The closely-named sibling `qou-7xit` (`lever1_habiro_tail_habiro_basis_expansion.py`, "(q;q)_n
Habiro **cyclotomic-basis** expansion of D(n)") is **complementary, not the same claim**: it expands
`D(n)` in the `(q;q)_k` Habiro basis and measures the **depth/height growth** of the coefficients
(the basis-side face of the "no finite closed form" verdict), inheriting the "cyclotomic through n=5"
fact as *context*. It does **not** connect that boundary to the `S₅` keystone, the E₈ McKay marks, or
the McKay-ADE alternating ladder — which is exactly the content of this note.

## Observation (i) — the alignment

The na-Stokes body-order `n` indexes both the Habiro tail `D(n)` and the framework's
calibration/keystone data:

| n | `a_D^(n)=lw(n−1)` | framework role | `D(n)` |
|---|---|---|---|
| 2 | lw(1) | **CAL c=1** (muon / leptonic anchor) | 0 |
| 3 | lw(2) | **CAL c=2** (Hopf / former gate) | `(q−1)²Φ₃` |
| 4 | lw(3) | **CAL c=3** (proton / Family-A) | cyclotomic |
| 5 | lw(4) | **KEYSTONE** S₅ ⊃ A₅ (icosahedral / Bring) | cyclotomic (`Φ₂²Φ₃Φ₆`) |
| 6 | lw(5) | first order **beyond** {cal ∪ keystone} | **NON-cyclotomic** (deg-8 core) |

**So the cyclotomic-pure regime `n ≤ 5` is *exactly* the framework's {3 calibration orders} ∪
{S₅ keystone}**, and the first non-cyclotomic (non-q-holonomic) content appears at the first
body-order `n=6` that is *neither* a calibration *nor* the keystone.

## Observation (ii) — the mechanism (ties to merged #3685)

Because `S(n) = Σ_{λ⊢n} dim_q(λ)`, the arithmetic of `D(n)` is governed by the `dim_q(λ)`. The
merged McKay value map (#3685) shows the four bwS0 conjugation classes `{λ,λ′}` of `S₅` carry
`dim_q` equal to the **E₈ Coxeter marks** `[mark]_q`, EXACT (no fit):

| bwS0 class `{λ,λ′}` | `dim_q(λ)` | E₈ McKay mark |
|---|---|---|
| `{(5),(1⁵)}` | `[1]_q` | 1 (trivial) |
| `{(4,1),(2,1³)}` | `[4]_q` | 4 (A₅ standard) |
| `{(3,2),(2,2,1)}` | `[5]_q` | 5 (A₅ 5-dim) |
| `{(3,1,1)}` self | `[5]_q+1` | 6 (A₅ split `3⊕3′`) |

This is available because `A₅ ≅ 2I/{±1}` is the **icosahedral** group and `2I ↔ Ê₈` (McKay). The
McKay-ADE ladder of alternating groups is **finite**:

| n | alternating group | McKay-ADE | keystone `dim_q` shape |
|---|---|---|---|
| 4 | `A₄ ≅ tetrahedral` | binary `2T ↔ Ê₆` | mostly single `[m]_q` (4+0 / 5) |
| 5 | `A₅ ≅ icosahedral` | binary `2I ↔ Ê₈` | **E₈ marks `[mark]_q`** (6 single + 1 split / 7) |
| 6 | `A₆ ≅ PSL(2,9)` | **not binary polyhedral — no McKay-ADE datum** | compound (only 4 / 11 single `[m]_q`) |

`A₅` is the **last** alternating group that is (the rotation group of) a Platonic solid / binary
polyhedral / McKay-ADE group. At `n=6` the `dim_q(λ)` become genuine **compound** products of
several cyclotomics (only `4/11` partitions have `dim_q` a single `[m]_q`, versus all `7/7` at
`n=5`), the McKay-mark structure is **gone**, and `D(6)` leaves the cyclotomic (Habiro) ring. So
the same `A₅→A₆` McKay exit marks the boundary from the *dimension* side.

## The conjecture (scope-(a), CORRELATION — causation open)

> **conj:cyclotomic-boundary-at-keystone.** `D(n)` is cyclotomic (Habiro-pure) ⟺ `n ≤ 5`, and
> `5` is the keystone order. `n=5` is distinguished as the **last exceptional-Lie alternating
> group**, from two dovetailing sides:
>
> - **(a) A₅ = icosahedral = last McKay-ADE alternating group** (`2I ↔ Ê₈`); the keystone `dim_q`
>   are the E₈ marks `[mark]_q` (#3685, exact). `A₆` (`n=6`) is the first non-McKay alternating
>   group — the McKay-mark structure exits exactly where `D(6)` goes non-cyclotomic.
> - **(b) n=6 = the unique exceptional S₆.** `S₆` is the **only** symmetric group with a
>   nontrivial **outer automorphism** — a deep, standard rep-theory fact — and the non-cyclotomic
>   core appears *exactly* at `n=6`.

The arithmetic **mechanism** is Stage-7's `Φ_d`-rule (`Φ_d` first divides `D(d+1)`); the
rep-theory **mechanism** is the McKay-mark exit at `A₆`. The **causation** — does the `A₅→A₆`
McKay exit / `S₆` anomaly *force* the boundary — is **open**, and is the formalization target.
This is a **correlation**, not a proved implication; specific root magnitudes are **not**
interpreted (numerology guard).

## Why it matters / formalization target

If provable, it ties the binding q-deformation's arithmetic **directly** to the s5-so3 keystone,
dovetailing with the Identity-I link (`S(n) = Σ_{λ⊢n} dim_q = Σ W_λ`, the keystone living at S₅):
the *same* S₅ whose `dim_q` are the E₈ marks (carrying `W_λ`, #3685) would control where the
binding tail leaves the Habiro (cyclotomic-completion) ring. A concrete formalizable sub-claim:
whether the `A₅→A₆` McKay exit (equivalently the `S₆` outer automorphism acting on the `λ⊢6`
character sum `S(6)`) forces the transition.

## Discipline

Correlation only; magnitudes not interpreted. Binding `D(n)`, **not** the Q_β `c_k` ladder. The
D(m) arithmetic is Stages 7–9 (cited); the McKay value map is #3685 (cited). The new content is the
calibration/keystone **alignment** + the McKay-ADE-exit **mechanism** + the S₅/S₆ candidate-cause
framing. Scope-(a), no fit, no wiring, no closure.
