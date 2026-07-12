# conj:cyclotomic-boundary-at-keystone — mechanism gap fixed, special-function synthesis, direction-(2) status

**Date:** 2026-07-12
**Branch:** `claude/cyclotomic-keystone-mechanism-fix-2026-07-12`
**PR:** #3719 (follow-up to merged #3686)
**Trigger:** owner asked "can you prove conj?" on the merged block.

## TL;DR

The conjecture splits into three logically distinct claims. Exactly one is
**proved** (finite); one is **open** (infinite family, verified through n=11);
one — the previously-stated **McKay "mechanism"** — had a **logical gap** and is
re-scoped. No part of the full conjecture is proved. The block's status is
corrected accordingly.

## The object (re-confirmed, all-n where noted)

`S(n) = Σ_{λ⊢n} dim_q(λ)`, `dim_q(λ) = [n]_q!/∏_c [h(c)]_q` (balanced/symmetric
`[k]_q`). Deviation from the q-lifted involution recurrence:

```
  D(n) := S(n) − S(n−1) − [n−1]_q · S(n−2).
```

- `S(n)|_{q=1} = Σ_λ f^λ = I(n)` = involution/telephone numbers
  (OEIS A000085: 1,1,2,4,10,26,76,232,764,2620). **All-n**, by RSK
  (involutions ↔ SYT) + q-hook-length → hook-length. Re-verified n=0..9.
- Explicit tails (q-monomial stripped), re-verified n=2..12:

  | n | D(n) | class |
  |---|------|-------|
  | 2,3 | 0 | — |
  | 4 | `(q−1)²·Φ₃` | cyclotomic |
  | 5 | `2·(q−1)²·Φ₂²·Φ₆·Φ₃` | cyclotomic |
  | 6 | `(q−1)²·Φ₅·(q⁸+4q⁷+6q⁶+2q⁵+2q⁴+2q³+6q²+4q+1)` | **non-cyclotomic**, deg-8 core |
  | 7 | `4·(q−1)²·Φ₃²·Φ₅·(deg-10 palindromic)` | non-cyclotomic |
  | ≥8 | `(q−1)²·(cyclotomic head)·(growing non-cyc. bar-even core)` | non-cyclotomic |

## Tier 1 — PROVED (finite): D(n) cyclotomic for n ≤ 5

Four explicit factorizations (above). Decidable; effectively proved. This is
the *content* of the conjecture — that the low orders are special. (Not a
theorem about the conjecture; a confirmed base case.)

## Tier 2 — OPEN (infinite): D(n) non-cyclotomic for all n ≥ 6

Verified through **n=11** (corpus Stages 7–9, 2026-06-28) and **n=12** (this
session). Cofactors are **not Salem/Lehmer** — generic bar-even, ≥2 off-circle
reciprocal pairs (2026-06-28 root distribution). **Not proved for all n.** A
proof needs a uniform structural invariant — e.g. a Mahler-measure bound
`M(D_n) > 1` for all n ≥ 6, or a persistent off-unit-circle root family. The
established structural reason is that the cofactor is **non-q-holonomic** and
grows in degree (2026-07-12 closed-form audit), which *motivates* but does not
*prove* the claim. Note also: non-cyclotomicity is the **generic** outcome for a
high-degree bar-even integer polynomial (cyclotomic-purity is codimension
~degree), so the surprise is entirely Tier 1; Tier 2 is "the special structure
does not persist, with no exceptions, ever" — genuinely open.

## Tier 3 — the McKay "mechanism": logical gap (fixed)

The block claimed (pre-fix):

> "only 4/11 partitions of 6 have `dim_q` a single `[m]_q` vs 7/7 at n=5 — the
> McKay-mark structure is gone, and D(6) leaves the cyclotomic ring."

**This conflates "single quantum integer `[m]_q`" with "cyclotomic."**
Every `dim_q(λ)` is a **product of cyclotomic polynomials for every n** (the
q-hook-length formula is a ratio of cyclotomic products that is a polynomial).
Re-verified: n=5, 6, 7 are 7/7, 11/11, 15/15 cyclotomic-pure. A product of
several cyclotomics is still cyclotomic, so single-vs-compound does **not**
locate the boundary. The non-cyclotomicity of `D(n)` comes from **cancellation
in the alternating sum** `S(n)−S(n−1)−[n−1]_q S(n−2)`, which the mark-count does
not control.

The McKay 2I↔Ê₈ value map (#3685) — at n=5 the four bwS0 classes carry the E₈
Coxeter marks `[1]_q,[4]_q,[5]_q,[5]_q+1`; A₅ the last McKay-ADE alternating
group; A₆=PSL(2,9) non-McKay — is a **true rep-theory fact** but is a
**coincidence of orders**, not the arithmetic mechanism. Re-scoped in the
block.

## Special-function synthesis (corpus, answering "recursion / q-Hermite / q-Bessel?")

Established in the corpus; recorded here for cross-reference:

- **q-Hermite / q-involution:** `S(n)` is the q-deformed involution number =
  Rogers–Szegő / q-Hermite moment (`QOU/Mass/BindingQHermiteOscillator.lean`;
  audit 2026-06-26). It is **not** the crossing-weighted (Touchard–Riordan)
  q-Hermite moment `μ_q` — those agree at q=1 but diverge from n=3 (re-verified
  here); `μ_q` as a binding object was **closed** (collapses at high isotope,
  2026-06-26).
- **q-Bessel / q-holonomic kernel:** the fibre kernel is the Hahn–Exton /
  Jackson q-Bessel (q-holonomic) class
  (`QOU/QBeta/QBesselContiguityRecurrence.lean`; audit 2026-06-27), of which the
  C-finite SL₂ depth-2 τ-recurrence is only the q→1 degeneration.
- **Recursions (all seed-exact then drift):** the naive 3-term
  `S=S(−1)+[n−1]_q S(−2)+D` (D = correction); the C-finite depth-2
  `τ = 3(3q⁴+8q²+3)/(4q(q+1)²)` **falsified** beyond seed (2026-06-24, windowed
  τ drifts 2.6424→2.6505→2.9933); monic order-2 q-holonomic fails from n=6;
  general non-monic order-2 q-holonomic **falsified** with held-out n=7,8,9
  (2026-06-27, up to q-deg ±4, X-deg 3). Not Askey–Wilson (multi-parameter; no
  reason to match a 0-parameter symmetric involution sum).
- **Numerical-holonomicity caveat (this session):** a fixed-q singular-value
  probe showed a spurious "order-2 nullspace" — an artifact of the huge dynamic
  range of `q^{jn}·S` entries. The exact symbolic solve returns the trivial
  solution; the corpus's held-out falsification is the authoritative negative.
  Recorded so the false positive is not re-derived.

## Lean scope (why no base-case Lean file in this PR)

A *meaningful* Lean formalization of Tier 1 requires defining
`S(n) = Σ_{λ⊢n} dim_q(λ)` (partitions, hook lengths, q-factorials) — a
substantial build. A bare polynomial-identity stub (`(q−1)²(q²+q+1) = q⁴−q³−q+1`)
would be **vacuous** (trivial by `ring`, disconnected from the actual tail) and
would trip the repo's anti-vacuity audit (§1a). Tier 2 (non-cyclotomicity) is
**not Lean-tractable** — it needs off-unit-circle root analysis. The
special-function home is already formalized (the two Lean siblings above). A
genuine `S(n)`-definition + base-case factorization Lean file is offered as a
scoped follow-up if the owner wants it.

## Disposition

- Block `.md`/`.ts`: mechanism section corrected; status re-tiered. Remains an
  **open conjecture** (correct kind).
- No wiring, no fit, no closure. Magnitudes not interpreted (numerology guard).
