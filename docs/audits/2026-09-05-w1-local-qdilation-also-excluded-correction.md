# The local q-dilation is excluded too — correcting #6695

**Date:** 2026-09-05 · **Bean:** `qou-7fnr` · corrects `qou-1z28` (#6695); follows `qou-an6y` (#6652), `qou-col1` (#6628), `qou-w0tx` (#6610), `qou-33hb` (#6582)
**Lean:** [`QOU/Mass/IrreducibleCubicNoQuadraticRoot.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/IrreducibleCubicNoQuadraticRoot.lean) — sorry-free, generic `[Field F] [Ring L] [Algebra F L] [Nontrivial L]`, no characteristic assumption, axioms `propext / Classical.choice / Quot.sound` only
**Probe:** [`w1_local_qdilation_branchpoint_probe.py`](../../computations/probes/w1_local_qdilation_branchpoint_probe.py) — exact sympy over `ℚ` and over `K = ℚ[z_c]/(branch sextic)`; no float64, no witness by design

## What I got wrong

#6695 pruned the first route of wall W1 (`qou-d8de`): a q-connection on the base
`z`-line with coefficients in `ℂ(z)` cannot have the colour sheets as flat sections.
That prune stands, unchanged.

In the same PR I then wrote, in four durable places, that the **local** q-dilation
`t ↦ μt` at a ramification point `z = z_c + t²` escapes the same exclusion. The reason
I gave was:

> the **local** q-dilation `t ↦ qt` at a ramification point, where every power series
> satisfies a first-order q-equation with a power-series coefficient and the theorem
> does not apply.

**That reason is about *power-series* coefficients. The theorem is about *rational*
ones.** So the sentence does not establish what it claims, and the claim itself is
false: the local case is excluded by the identical argument.

This is the second time in three tranches that the defect was in an *argument I
supplied for a negative*, not in a measurement — #6628 corrected the axis of the
kernel, and this corrects the reach of the prune. Both slipped through because a
plausible-sounding reason was not checked against the hypothesis it was invoking.

## The correction

In the local coordinate the sheets are power series in `t`. Each is algebraic over
`K(t)` — it satisfies the cubic `P(X, z_c + t²) = 0` over `K[t]` — and therefore
D-finite in `t`. A q-dilation `t ↦ μt` with coefficients rational in `t` makes a sheet
q-holonomic in `t` by the same rank count as on the base. The rationality theorem
(Bézivin; Ramis; Schäfke–Singer) then forces the sheet to be **rational in `t`**.

It is not, and the obstruction is a degree count:

- `t² = z − z_c`, so every element of `K(t)` is annihilated by a polynomial of degree
  `2` over `K(z)`, namely `X² − (z − z_c)`. And `[K(t):K(z)]` is exactly `2`, not `1`,
  because `z − z_c` is not a square in `K(z)`: `2 deg u = 1 + 2 deg v` has no solution.
- The colour cubic is irreducible over `K(z)` — `QOU.Mass.ColorCubicIrreducible`,
  proved for **every** field of characteristic zero, so in particular for
  `K = ℚ(z_c)`.
- **An irreducible cubic has no root of degree `≤ 2`** — the new lemma,
  `QOU.Mass.IrreducibleCubicNoQuadraticRoot.no_root_of_irreducible_cubic`. The minimal
  polynomial of such a root would have degree `3` (it is `p` up to a unit) and degree
  `≤ 2` at once.

So no sheet is rational in `t`, every hypothesis of the theorem is met in the local
chart exactly as on the base, and **the local rational q-dilation is excluded**.

The Lean carries the general obstruction rather than the instance. Its hypothesis is
"annihilated by a nonzero polynomial of degree `≤ 2`" instead of "lies in a quadratic
extension", which is the same thing in usable form and keeps the file clear of the
`IntermediateField` tower machinery. The instance for this curve is checked exactly in
the probe.

## What the probe measured (exact)

| section | result |
|---|---|
| **1** branch sextic irreducible over `ℚ` | **true** — so `K = ℚ(z_c)` is a genuine degree-6 number field, and `t` is annihilated by `X² − (z − z_c)` over `K(z)` |
| **2** colour cubic has no root in `K[z]` | **true** — leading-term bound for `d ≥ 2`, Gröbner basis `[1]` over `ℚ[c₀,c₁,z_c]` modulo the sextic for `d ≤ 1` |
| **3** local cubic has no root in `K[t]` | **true** — leading-term bound `3d > max(2+2d, 4+d, 6)` for `d ≥ 3`, Gröbner basis `[1]` over `ℚ[c₀,c₁,c₂,z_c]` modulo the sextic for `d ≤ 2` |
| **4** no rational-in-`t` q-difference relation on the unramified sheet | **true** at `μ ∈ {2, 3/2, 11/10}`, `D ∈ {2,4}` |

§3 is the hinge, and it is worth reading the local cubic's own coefficients: at
`z = z_c + t²` the constant term factors as `(t²+z_c+1)(t⁴+2t²z_c+z_c²+1)`, which is
just `(z+1)(z²+1)` rewritten — the local cubic is the same cubic, and nothing about
localising at the branch point makes a sheet any more rational than it was.

§4 uses the same specialisation-plus-mod-`p` certificate as #6695, one level up: the
rank over `K` is at least the rank of the image under any ring map `K → 𝔽_p`, so full
column rank mod `p` excludes a relation over `K`. §4b is the control — the same
truncated arithmetic that §4 searches with does verify the sheet's algebraic relation
`P(X(w), z_c + w) = 0` to the computed order.

## Two probe defects, both caught by the probe's own assertions

- **`sympy.gcd` cannot see the double root.** The unramified sheet was to be found by
  dividing out `gcd(P(·,z_c), P_X(·,z_c))`. Over `ℤ[z_c]` that gcd is **1** — the
  collision only exists *modulo the sextic*, and the gcd has to be taken in `K[X]`.
  The probe now writes out the one Euclid step explicitly: with `a = z_c+1`,
  `b = z_c²+z_c+1`, `c = z_c³+z_c²+z_c+1`, the double root is
  `X₀ = −(9c − ab)/(6b − 2a²)` and the simple root is `−a − 2X₀`. Both are asserted to
  be roots (and `X₀` a root of `P_X`) before use.
- **The mod-`p` root scan was written for primes near `2³¹`**, i.e. a two-billion
  iteration linear scan that never returns. The primes are now moderate and found by
  search. Nothing is lost: the rank argument is exact at **any** prime where the map
  is defined, so a large prime buys nothing here.

## Scope

- **Excluded (b), on the base and in the local chart alike:** a q-difference system
  in a dilation with **rational** coefficients, having the sheets as flat sections.
- **Still not excluded:** coefficients that are not rational functions, and operators
  living on Σ rather than on either coordinate line.
- **`D_q` is not constructed.** This tranche removes a route and a wrong sentence; it
  does not build anything.

## What it changes for the arc

`qou-d8de`'s route 1 is now excluded in both charts, so the "local at the ramification
point" escape hatch that #6695 left open is closed. What survives of W1 is route 2
(root-of-unity fibre monodromy) and route 3 (import the Ramis–Sauloy–Zhang / Sauloy
local framework) — and route 3 now has to supply something whose coefficients are
*not* rational in a coordinate, which is a sharper requirement than it looked
yesterday.

The arc's pattern is unchanged and one step stronger: every realisation of
"symbol = `L_K`" that stays inside rational-coefficient q-difference operators on a
coordinate line either fails or is empty.

## Corrections applied

| where the wrong claim reached | fixed |
|---|---|
| `docs/audits/2026-09-04-w1-route1-base-qshift-rationality-prune.md` | corrected in place, with a pointer here |
| `mass-theory/qdifference-kernel-prolongation-symbol.md` scope note | the "local at the ramification point" alternative removed |
| bean `qou-1z28` | corrected |
| bean `qou-d8de` route-1 entry | corrected |
| PR #6695 body | a correction comment posted on the merged PR |

## Reproduce

```bash
PYTHONPATH=computations python3 -u computations/probes/w1_local_qdilation_branchpoint_probe.py
lean content/quantum-observable-universe/lean/QOU/Mass/IrreducibleCubicNoQuadraticRoot.lean
```
