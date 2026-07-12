# The binding q-deformation Habiro tail D(n): exact forms + the cyclotomic→non-cyclotomic boundary

**Date:** 2026-07-12
**Branch:** `claude/lever1-sw-period-lw-rate-refine-2026-07-12`
**Compute:** [`computations/lever1_habiro_tail_closed_form.py`](../../computations/lever1_habiro_tail_closed_form.py)
**Witness:** [`computations/lever1-habiro-tail-closed-form.witness.json`](../../computations/lever1-habiro-tail-closed-form.witness.json)
**Bean:** `z2bn`. **Extends:** `QOU/Mass/BindingEigenfunctionTwoTier.lean` (`D4_habiro_factor`,
`q²·D(4)=(q−1)²·Φ₃`).

## What D(n) is

The exact binding q-deformation is `S(n) = S(n−1) + [n−1]_q·S(n−2) + D(n)`, where
`S(n)=Σ_{λ⊢n} dim_q(λ)` is the na-Stokes period and `D(n)` is the **Habiro tail** — the
deviation of the exact period from the leading q-telephone recurrence. `D(2)=D(3)=0` (the
recurrence is exact at the seed); this note derives the exact closed forms for n = 4…9 and
pins their universal structure.

## Exact closed forms (n = 4…9)

| n | `q^{n−2}·D(n)` (factored) | cofactor after (q−1)² |
|---|---|---|
| 4 | `(q−1)²·Φ₃` | cyclotomic |
| 5 | `2(q−1)²·Φ₂²·Φ₆·Φ₃ / q` | **cyclotomic** |
| 6 | `(q−1)²·Φ₅·(q⁸+4q⁷+6q⁶+2q⁵+2q⁴+2q³+6q²+4q+1) / q³` | non-cyclotomic, deg 8 |
| 7 | `4(q−1)²·Φ₃²·Φ₅·(deg-10 palindromic) / q⁵` | non-cyclotomic, deg 10 |
| 8 | `(q−1)²·Φ₃·Φ₅·Φ₇·(deg-14 palindromic) / q⁸` | non-cyclotomic, deg 14 |
| 9 | `(q−1)²·Φ₄·Φ₇·(deg-28 palindromic) / q¹²` | non-cyclotomic, deg 28 |

(`Φ_k` = the k-th cyclotomic polynomial.)

## Three derived invariants

- **(H1) Universal `(q−1)²` double root at q=1** for every n≥4 (`D(1)=D'(1)=0`) — the Habiro /
  smooth-at-classical signature. This is what makes the classical limit
  ([the exact telephone kernel](2026-07-12-lever1-sw-period-lw-rate-refine.md)) clean:
  `D(n)→0` as q→1.
- **(H2) Bar-even:** `D(1/q)=D(q)` (self-reciprocal Laurent) for every n — the `q↔q⁻¹` bar
  involution symmetry, matching the fibre's bar structure. The non-cyclotomic cofactors are
  themselves palindromic.
- **(H3) Cyclotomic head × cofactor** that is **fully cyclotomic through n=5** (D(5) is the last
  all-cyclotomic tail) and genuinely **non-cyclotomic (bar-even) from n=6**, with the cofactor
  degree growing `8, 10, 14, 28, …`.

## Verdict (scope-(a))

The Habiro tail has **no finite general closed form**: the non-cyclotomic bar-even cofactor grows
in degree and is not q-holonomic — which is exactly *why* `S(n)` forks from any fixed-order
q-difference recurrence (the eigenfunction-audit fork). What **is** derived and universal is the
`(q−1)²` double root and bar-evenness; the growing non-cyclotomic cofactor is the genuine
non-holonomic content of the binding period. The `n≤5`-cyclotomic → `n≥6`-non-cyclotomic boundary
is sharp and now explicit.

**Discipline note.** This is the **binding recurrence** `D(n)` (the na-Stokes period deviation),
**not** the Q_β precision-ladder `c_k` — the two are distinct objects and this result does not
touch the c_k flip-flop discipline. Exact symbolic (sympy); no fit, no wiring. Scope-(a).
