# q-D-module symbol calculus — algebraic core (QDM-1 / QDM-2)

**Date:** 2026-07-20
**Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20`
**Beans:** `qou-zj11` (QDM-1), `qou-mpne` (QDM-2); epic `qou-dap4`
**File:** [`QOU/Machinery/QuantumTorusSymbol.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/QuantumTorusSymbol.lean)

## What the symbol calculus provides

The quantum torus `T = A[L^±; σ]` (`QOU.Machinery.QuantumTorus`, the NT-T2
q-Weyl ring) carries the **order filtration** by top `L`-degree
`topDeg : T → WithBot ℤ`. This brick builds the **principal-symbol map** for
that filtration:

- `leadDeg P = (topDeg P).unbotD 0 ∈ ℤ` — the leading `L`-degree.
- `leadCoeff P = coeffAt P (leadDeg P) ∈ A` — the leading coefficient.
- `symbol P = monomial (leadDeg P) (leadCoeff P)` — the leading `L`-monomial,
  i.e. the image of `P` in the associated graded ring.

The symbol map is the algebraic gateway a genuine q-D-module theory needs: it
sends an operator to its principal part, and (QDM-2) it is multiplicative into
the associated graded, so the characteristic-variety machinery of QDM-3/4 would
be built on top of it.

## What is proved — sorry-free

`lean`-direct verification against the package oleans: **exit 0**, zero
warnings. `#print axioms` on `symbol_mul` and `coeffAt_mul_add` reports only
`{propext, Classical.choice, Quot.sound}` — **no `sorryAx`**.

### QDM-1 — principal symbol map (`qou-zj11`)

- `symbol_monomial`, `symbol_emb`, `symbol_Lgen` — the symbol of a monomial /
  order-0 coefficient / `L` is itself.
- `topDeg_emb` (order 0), `topDeg_Lgen` (order 1).
- `leadCoeff_ne_zero`, `topDeg_eq_leadDeg` — a nonzero element has a nonzero
  leading coefficient and a genuinely-integer top degree.

### QDM-2 — multiplicativity / associated graded (`qou-mpne`)

- **`coeffAt_mul_add`** (holds over **any** `CommRing`, no domain hypothesis):
  `coeffAt (P·Q) (m+n) = coeffAt P m · (σᵐ (coeffAt Q n))` for
  `topDeg P ≤ m`, `topDeg Q ≤ n`. This is the leading-coefficient product law;
  the twist `σᵐ = ofAdd m • ·` is the graded structure constant.
- **`coeffAt_mul_eq_zero_of_lt`** (any `CommRing`): coefficients above
  `m+n` vanish.
- **`topDeg_mul`** and **`symbol_mul`** (over `[IsDomain A]`):
  `topDeg (P·Q) = topDeg P + topDeg Q` and
  `symbol (P·Q) = symbol P · symbol Q`.

## Honest scope of the multiplicativity hypothesis

`symbol_mul` and `topDeg_mul` require `[IsDomain A]`. This is the honest,
minimal hypothesis: it is exactly what keeps the leading coefficient
`leadCoeff P · σ^{leadDeg P}(leadCoeff Q)` nonzero (in a domain, a product of
nonzeros is nonzero, and `σᵐ` — an automorphism — preserves nonzero). Without
it the top degree of a product can drop and the symbol is not multiplicative.
The *coefficient* law `coeffAt_mul_add` needs no such hypothesis; only the
identification "this coefficient is the leading one" does.

## What commutes in `gr` vs the ambient twist (precise note)

The quantum torus is **already** `ℤ`-graded by `L`-degree, so its associated
graded ring for the order filtration is `T` itself, with the **twisted**
product `L^m a · L^n b = L^{m+n}(a · σᵐ b)`. The classical-Weyl "principal
symbols commute" phenomenon **does not hold** here: the commutator
`[L, M] = (σ − id)(M)·L = (q²−1) M L` has the **same** order as `ML` (the
q-Weyl twist is a same-order deformation, not lower-order), so the symbol of a
commutator need not vanish. `symbol_mul` records the honest fact — leading term
of a product = twisted product of leading terms — and the surviving twist
`σ^{leadDeg P}` is exactly the graded structure constant.

## Open — QDM-3 / QDM-4 (the deep wall, out of scope here)

The geometric application is **not** done and is the deep open wall:

- **QDM-3** — characteristic variety / support of a q-D-module as the vanishing
  locus of the symbol ideal, and the associated dimension theory.
- **QDM-4** — a holonomicity / Bernstein-inequality analogue and its use in the
  strong-AJ / colored-Jones program (`qou-dap4`).

These require the commutative-algebra geometry of the symbol algebra (Poisson
structure from the same-order twist, Gröbner/Bernstein filtrations over the
Habiro/skew base), which is beyond this generic-ring algebraic core. This audit
records QDM-1/QDM-2 as the verifiable foundation; QDM-3/4 remain open research.
