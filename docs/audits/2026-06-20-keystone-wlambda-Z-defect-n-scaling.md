# W_λ partition-function defect Z(n): sign change at n=7 sharpens *and* tempers the q-Bessel lead

**Date:** 2026-06-20
**Branch:** `claude/fervent-noether-zssd1k`
**Status:** Structural narrowing — no fit, no correspondence chain
**Extends:** [`keystone_qbessel_plancherel_precheck.py`](scripts/keystone_qbessel_plancherel_precheck.py) (8d781b21, n=5 only)
**Script:** [`scripts/keystone_wlambda_Z_defect_n_scaling.py`](scripts/keystone_wlambda_Z_defect_n_scaling.py) (`ALL CHECKS PASS`, exit 0)
**Frontier:** q-Bessel/heat-kernel geometric realization of the Ocneanu weights `W_λ = d_q(λ)²/[n]_q!` (#2503 DG plan; #2488 scope handoff)

## What the precheck left open

The precheck (8d781b21) found the candidate weight `W_λ = d_q(λ)²/[n]_q!` is **not**
a probability measure at `q_0`: it is sub-normalized, with partition function
`Z(5) = Σ_{λ⊢5} W_λ = 0.98222`, defect `1 − Z(5) = 0.0178`. It named `1 − Z` as
"the geometric quantity to explain" (the heat-kernel trace any `S¹`-equivariant
index realization must reproduce) — **but computed it only at `n = 5`.**

This note extends that single number to a structural object, using **only**
balanced-q-integer arithmetic (`[m]_q = (qᵐ − q⁻ᵐ)/(q − q⁻¹)` and the q-hook-length
formula `d_q(λ) = [n]_q!/∏_cells [h]_q`). The `2I → E8 → Poincaré → Lawrence–Zagier`
correspondence chain is **never invoked** — this is a property of `W_λ` itself.

## Result

`Z(n) = Σ_{λ⊢n} d_q(λ)²/[n]_q!` at `q_0 = 1.10997858` (`h_0 = q_0 − q_0⁻¹ ≈ 0.2091`):

| n | Z(n) at q₀ | 1 − Z(n) |
|---|-----------|----------|
| 2 | 0.994581 | +0.005419 |
| 3 | 0.987440 | **+0.012560** |
| 4 | 0.982165 | +0.017835 (max) |
| 5 | 0.982224 | +0.017776 |
| 6 | 0.991080 | +0.008920 |
| 7 | **1.012426** | **−0.012426** |

**Small-h leading order** `1 − Z(n) = C(n)·h² + O(h⁴)` (verified bar-even: `C(n)`
is stable across `h = 10⁻³` and `10⁻⁴`). Empirical `24·C(n)` for `n = 2..8`:
`3, 7, 10, 10, 5, −7, −28`.

## Three findings

1. **`1 − Z(3) = 0.01256`** — the keystone generation blocks live at `n = 3`
   (the Borromean `H₃`), not `n = 5`. This value was previously un-computed.

2. **The defect is non-monotone and changes sign.** It rises to a max `≈ 0.0178`
   near `n = 4`, falls, and `Z(n)` **crosses 1 at `n = 7`** (defect goes negative).
   The leading `h²` coefficient `C(n)` itself flips sign there.

3. **Leading order is `h²` — bar-even** (invariant under `q → q⁻¹`). A bar-even
   quantity **cannot by itself** be the bar-odd 210 ppb muon shift, consistent
   with [44377f33](../coordination/s5-so3-keystone.md) (the frontier carries the
   `O(1)` generation skeleton, not the fine shift).

## Why it matters (sharpens **and** tempers the lead)

- **Sharpens:** the q-Bessel/heat-kernel realization (#2503) now has a sharp,
  falsifiable target — any `S¹`-equivariant index whose index measure is `W_λ`
  must reproduce a partition function `Z(n)` that is `< 1` for `2 ≤ n ≤ 6` **and
  `> 1` for `n ≥ 7`**. A geometric object with this `n`-profile is a strong
  constraint; one without it refutes the identification.

- **Tempers:** the framing "`1 − Z` is the mass defect" is **not** a clean
  monotone-positive heat-kernel-trace story once the sign change is included. A
  partition function / heat-kernel trace is conventionally positive and definite;
  a normalization constant that crosses 1 is more naturally read as `W_λ`
  simply not being the right (un-normalized) measure — the genuine q-Plancherel
  probability measure is `W_λ/Z(n)`, and `Z(n)` may be a normalization artifact
  rather than a geometric defect. The DG build (#2503 Step-1 gate) should treat
  the sign change as a discriminating test, not assume `1 − Z > 0`.

## What this does NOT do

- No closed form for `C(n)` is claimed. A hook-moment ansatz
  `C(n) = (1/n!)Σ_λ dim(λ)·Σ_cells h²` was **tested and refuted** (the script's
  self-check caught it); `C(n)` is reported empirically only.
- Manifold existence stays **owner-gated** (subgoal-2 differential geometry).
- **No physical claim** and **no fit**: `q_0` anchors the table; the 210 ppb
  target is referenced only to note the bar-parity mismatch (it tunes nothing).

## Addendum (2026-08-21) — the heat-kernel reading of `Z`, and what it is *not*

Recorded while resolving the closed PR #2521, whose reconciliation reached the
same conclusion as this note by a different route. That PR was closed as
superseded (correctly — this note is broader: n = 2..7 with the sign change,
which #2521 never computed), but it carried two pieces of framing that never
landed anywhere on `main`. They belong here, with their epistemic status
attached.

### 1. `Z(n) = 1` is exactly the q-deformed RSK identity, and it fails

This is pure algebra from the definition above, not a new claim. Since
`W_λ = d_q(λ)²/[n]_q!`,

```text
  Z(n) = Σ_λ d_q(λ)² / [n]_q!        so       Z(n) = 1  ⟺  Σ_λ d_q(λ)² = [n]_q!
```

At `q → 1` that is the classical Burnside/RSK identity `Σ_λ (f^λ)² = n!`
(`[5]_1! = 5! = 120`), which holds. So the measured `Z(n) ≠ 1` is precisely the
statement that **this identity does not survive q-deformation** at the substrate
anchor, and the `n = 7` sign change says the failure is not one-signed — a
q-deformation defect that overshoots as readily as it undershoots.

That is a sharper reading of the same numbers than "sub-normalized measure", and
it does not require the heat-kernel picture at all.

### 2. The heat-kernel normalizer: `Σ_λ d_q(λ)²`, not `[n]_q!`

Under the Peter–Weyl decomposition `L²(G) ≅ ⊕_λ V_λ ⊗ V_λ*` the λ-isotypic
component has dimension `d_λ²`, so the **trace** of the heat operator is

```text
  Z_heat(t) = Tr e^{-tΔ} = Σ_λ d_q(λ)² · exp(-μ_λ(q)·t)
```

whose `t → 0` value is `Z_heat(0) = Σ_λ d_q(λ)²`. At `q₀`, `n = 5` that is

```text
  Σ_λ d_q(λ)²  =  Z(5) · [5]_q!  =  0.982224 × 131.313  =  128.979
```

against `[5]_q! = 131.313`. On this reading `[n]_q!` is simply the wrong
denominator and `Z_heat(0)` is the right one, which is the sense in which the
"defect" is a normalizer artifact rather than a geometric quantity —
`Z(5) = Z_heat(0)/[5]_q!` reproduces the precheck's `0.982224` exactly.

**But note what that does and does not buy.** `d_q(λ)²/Z_heat(0)` sums to `1` **by
construction** — dividing a positive family by its own sum always does. So
"it normalizes to 1" is not evidence for the heat-kernel reading, for the
S¹-equivariant index, or for anything else; it is what normalization means. The
substantive question is not *whether* a normalizer exists but *which* one is
canonical, and that is exactly what remains open. This note's own temper stands:
`Z(n)` **may** be a normalization artifact, and the sign change is the
discriminating test.

### 3. Lean status of the above — none of it is proved

Stated explicitly so no later reader cites this addendum as formalised.

| assertion | Lean status |
|---|---|
| `Σ_λ d_q(λ)² = [n]_q!` fails at `q ≠ 1` | **not formalised** — numeric, from the table above |
| `Z_heat(0) = Σ_λ d_q(λ)² = 128.979` | **not formalised** — numeric evaluation |
| `d_q(λ)²/Z_heat(0)` is a probability measure | **not formalised**, and trivial by construction |
| the Peter–Weyl heat-kernel series converges | **named conjecture, no proof term** |
| `Z_q(k) = Σ_{λ⊢k} d_q(λ)²` | **axiomatised as an opaque class field** |

Two of these deserve the detail:

- **`QOU.qHeatKernelPeterWeyl`**
  ([`q-heat-kernel-peter-weyl.lean`](../../content/quantum-observable-universe/information-theory/q-heat-kernel-peter-weyl.lean))
  is a `def … : Prop` with **no instance and no proof term** — its own docstring
  says so ("the honest open state", per AGENTS.md §3b Pattern C). It is a
  primary conjecture carrier, not a theorem. **And it is a different series:** it
  asserts `Summable (fun λ => dLambda λ * exp(-μ_λ t))` — `d_λ` to the **first**
  power, the Peter–Weyl expansion of the *solution* `u(t,x)`. The trace `Z_heat(t)`
  above carries `d_λ²`. Both are correct for their own object; they are not the
  same sum, so **do not cite that carrier as backing for the trace**.
- **`QOU.MathlibExt.QPlancherel`**
  ([`QPlancherel.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/QPlancherel.lean))
  is sorry-free, but `HasPartitionFunction.Z : ℕ → R` is an **opaque class field**
  carrying only `Z_pos`. The identity `Z_q(k) = Σ_{λ⊢k} d_q(λ)²` appears in its
  docstring, which itself records that `Z` is "stated as a class field rather
  than constructed". So the identity is *documentation, not a theorem*, and
  `measure_mul_partitionFunction : Z k * measure λ k = d_q(λ)²` reduces to
  `Z · (d²/Z) = d²` — true for **any** positive `Z`, saying nothing about `Z`
  being the sum. There is **no** `Σ_λ measure λ k = 1` theorem in the corpus.

So the whole normalization story is currently numeric plus one unproved
conjecture carrier. Formalising `Σ_λ d_q(λ)²` as a constructed finite sum (rather
than an opaque field) and proving total mass `1` on the quotient is the smallest
real Lean step available here; it would also let the `q ≠ 1` failure in §1 be
stated as a theorem rather than a table.
