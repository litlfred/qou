# B1.5 — what a level-mixing bridge would have to be (design note, no compute)

**Status:** design note. No probe, no witness, nothing wired. Written
after the B1 → B1.4′ negative sweep closed every parameter-free bridge
form at the W₋₁-block level, per the formalize-first discipline
(AGENTS.md §"Formalize-first probe discipline"): the next rung is a
*derivation*, and running another wide scan before stating what would
be scanned is exactly the failure mode that discipline exists to
prevent.

**Scope discipline.** Everything below is scope-(a) bookkeeping of what
has been excluded and what the surviving form must satisfy. Nothing here
claims a bridge exists. Comparison to observed only; no ontological
claims.

## 1. What is closed, and how

Five rungs, each a pre-registered parameter-free decision, all negative:

| Rung | Question | Decision | Result |
|---|---|---|---|
| B1 (#4226) | Does a single-sector Stokes population bridge O_φ to D_odd? | 180-candidate numeric scan, gate 1e-6 | 0 hits; σ-pair population **forced** n₁ = n₂ = 0 on the real-q ray |
| B1.2 (#4233) | Is a Habiro-face value a bare entry of the GK bilinear? | 440 parameter-free comparisons | 0 hits, 0 near-misses |
| B1.3 (#4235) | Which λ-row does the Masbaum tail occupy? | 21 exact rational membership decisions, O(q³⁴) | 0 in-span; tail is u-even (no half-integer-λ escape) |
| B1.4 (#4283) | Does the Euler-descendant tower bridge? | 63 exact decisions, O(q¹²⁸), margin 47 | 0 in-span; basis rank 81 of 99 |
| B1.4′ (#4283) | Is there an n-independent per-level dressing? | 165 exact cross-multiplications | 0 leads; every Masbaum level individually u-even |

Two independent structural facts fell out of the sweep and constrain
the successor:

- **The θ-tower is not a genuine enlargement.** 99 columns, rank 81 —
  18 of the descendant directions land back inside the original block
  span. Whatever enlarges the search space, it is not differentiation.
- **u-parity is even at every level, not just in the total.** A
  half-integer-λ or odd-u escape hatch does not exist anywhere in the
  Masbaum grading.

Independently, the sibling exclusion chain (#4282 / #4288 / #4293)
bounds the same family from the *anchor* side: the bar-odd datum is
anchor-smooth (4.56 ppm), amplification ρ ≥ N forces
`barOdd² ≤ 4/(N²−1)`, and the phase `arg(u)` is frozen at real q₀ so
its anchor-swing is exactly 0. Two methods — exact formal membership
here, anchor-swing bounds there — reach the same wall from opposite
directions.

## 2. The surviving form, stated precisely

Every excluded map shares one property: it acts on the block basis
**level-diagonally with a scalar**. Writing the two sides in their
level gradings,

```
F      = Σ_n T^Mas_n ,        T^Mas_n = C_n(a)·(u²;u²)_n²
H±_j,λ = Σ_n T^H_n(j,λ) ,     T^H_n   = p_j(n)·(±)ⁿ q^{e(n,λ)}/(q;q)_n³
```

everything excluded so far has the shape

```
T^Mas_n  =  r(q) · T^H_{n+k}          (B1.3, B1.4′: r scalar, k fixed)
F        =  Σ_{j,λ,m} c_{j,λ,m} · θ^m H±_{j,λ}   (B1.4: c constants)
```

The surviving form is a genuine **module map** — level-mixing with
n-dependent coefficients:

```
T^Mas_n  =  Σ_m  M_{n,m}(q) · T^H_m ,      M_{n,m}(q) ∈ ℤ[q^{±1}]
```

with `M` lower-triangular-ish in the Habiro sense (finitely many m per
n). This is the shape a Habiro-ring comultiplication induces, and it is
*not* reachable by any scan over a fixed finite basis: the unknown is a
matrix of q-polynomials, not a vector of scalars.

## 3. Why the next move is a derivation, not a probe

A brute search over `M` is ill-posed in exactly the way the
formalize-first rule warns about. Counting degrees of freedom: at
truncation O(q^N) with L levels, a general `M` carries ~L²·N unknowns
against N equations — massively underdetermined, so a "fit" would
always succeed and would mean nothing. Any scan over this family
produces a fit, not a derivation, and would be an anti-laundering
violation to report as a bridge.

The tractable route is the opposite order — derive `M` from the
structure that *generates* both gradings, then check the derived `M`:

1. **Identify the comultiplication.** Both sides are cyclotomic
   expansions of objects in the Habiro ring of the knot; the map
   between two such expansions is induced by the ring's structure maps,
   not chosen. Write it down for 5₂ specifically.
2. **State it as a Lean claim first** (formalize-first): the
   level-mixing relation with `M` as a defined object, hypotheses
   explicit. A conditional class is acceptable here per §3b-cond, but
   it must carry genuine hypotheses — not the conclusion (§3b-cond
   item 5).
3. **Then, and only then, verify numerically** with the exact-series
   engine already in-tree (`qseries_exact_util.py`) — the derived `M`
   is a *prediction*, so the check is parameter-free and decisive.
4. **Anchor-swing gate on any hit** (per #4282's suggestion): even a
   correct structural bridge inherits the anchor-smoothness bounds of
   #4288/#4293, so a bridge is not by itself a c₃ carrier. Report the
   two claims separately.

## 4. What is explicitly NOT proposed

- No seventh ansatz-style scan over `M` (see §3 — it would fit by
  construction).
- No c_k wiring. c₃ remains a q₀-dependent near-match (SETTLED, #1580);
  nothing in this note changes its tier.
- No claim that a bridge exists. The sweep result is that the *easy*
  forms do not; that is evidence about the search space, not about the
  answer.

## 5. Pointers

- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
  (rows B1, B1.2, B1.3, B1.4 + B1.4′, and the sibling C1/#4288/#4293 rows).
- Attack-options audit:
  [`docs/audits/2026-07-18-ck-odd-fibre-attack-options.md`](../audits/2026-07-18-ck-odd-fibre-attack-options.md).
- Exact-series engine (reusable):
  [`computations/probes/qseries_exact_util.py`](../../computations/probes/qseries_exact_util.py)
  — printed-GGM-table gated; fraction-free Bareiss for exact ranks.
- The (★) identity, now proved sorry-free at every order:
  [`QOU/QBeta/HabiroTailStar.lean`](../../folio/quantum-observable-universe/lean/QOU/QBeta/HabiroTailStar.lean).
