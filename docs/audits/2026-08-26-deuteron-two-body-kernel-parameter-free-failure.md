# The deuteron +27 % is a parameter-free prediction failure of the two-body kernel

**Date:** 2026-08-26 · **Branch:** `claude/isotope-mass-binding-dashboard-kdvhz6` ·
**PR:** [#5812](https://github.com/litlfred/qou/pull/5812) ·
**Bean:** `qou-39bx` (epic `qou-v2om`) ·
**Discipline:** scope-(a) scope-limited negative; zero free parameters; nothing wired;
mpmath `mpf` end to end at 60 dps; `scripts/precision-gates.sh --changed` green.

## The question

`α·L_pn = 2.8328 MeV` against `B_AME(²H) = 2.2246 MeV`, **+27.34 %** — and `²H` is the
**only** negative residual in the low-isotope table (`R(²H) = −0.61`; every other isotope
has `R > 0`). Is that a *tuning gap* (some quantity in the calculation is free and set
wrongly) or a *prediction failure* (nothing is free and the answer is simply wrong)?

The distinction decides the disposition. If something is free, name it and the item is a
calibration question. If nothing is free, the overshoot is a real refutation of the
two-body kernel as defined and must be reported as one.

## Verdict

**Nothing is free. The two-body kernel has zero continuous free parameters, so the +27 %
is a parameter-free prediction failure.** It is a **scope-(a)** negative: the two-body
Markov-trace kernel *alone* does not reproduce the deuteron. It is **not** scope-(b) —
`B_AME(²H)` sits *inside* the convention-D admissible band, so no invariant excludes the
target; what is excluded is reaching it at the derived interface weight, and any
*additive* term is untouched by anything measured here.

## 1. The Lean statement, and its status

New module
[`QOU/MassTheory/DeuteronTwoBodyKernel.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/DeuteronTwoBodyKernel.lean)
— **seven theorems, all sorry-free**. `lean`-direct **exit 0** against the real import
cone; `#print axioms` on all seven returns `[propext, Classical.choice, Quot.sound]` and
no `sorryAx`.

| theorem | content |
|---|---|
| `interfaceFactor_half` | `z_D(q) − h(q)/2 = (q⁴+1)/(2q(q²+1))` — the bar-symmetric p–n interface factor is an exact rational function of `q`; the writhe exponent `2t−1` vanishes there, so the bond energy is `E₀·ln(2q(q²+1)/(q⁴+1))` with no free constant in it |
| `bondL_half` | the writhe factor is exactly `1` at `t = ½` |
| `bondL_strictMono` | `t ↦ L(q,t)` is **strictly increasing**: the admissible interface family is swept monotonically, so an endpoint bound is sharp |
| `overshoot_core` | numerical core, on abstract reals with interval hypotheses |
| `deuteron_overbinds` | for `q` in the proton-pin interval, `mₑ` in the CODATA interval, and **any** near-balanced weight `t ∈ [0.499, ½]`: `E₀·L > 1.25 · B_AME(²H)` |
| `required_weight_far_from_balanced` | conversely, any `t` giving a binding `≤ 2.4 MeV` has `t ≤ 0.4` |
| `derived_weight_near_balanced`, `no_flavour_split_rescue` | the derived weight is `½ − δ/4` with `δ/4 < 3.5 × 10⁻⁴`, so the departure from balance the deuteron demands exceeds **250 ×** the entire derived flavour split |

The inequality is proved from `Real.log_le_sub_one_of_pos` and `Real.log_two_gt_d9`
through a chain of *rational* bounds; every one of those bounds is re-checked against the
`mpf` values by the probe (15/15), so the formal statement and the compute cannot drift
apart silently.

The statement is deliberately an **inequality**, not an equality: "there is no free
parameter" as a Lean congruence would be a tautology, and AGENTS.md §"No trivial trues"
forbids that. The falsifiable content is that the kernel *strictly over-binds*, uniformly
over the whole neighbourhood of weights the framework can reach.

## 2. The free-parameter inventory

| ingredient | value | fixed by | continuous freedom |
|---|---|---|---|
| `mₑ` | `0.51099895069 MeV` | CAL-1 (it *is* the MeV unit) | 0 |
| `q₀` | `1.109978582751380807…` | CAL-2 proxy, proton pin (0.017 ppb) | 0 |
| `E₀ = mₑ/(q₀(q₀−1))` | `4.185981363294475897 MeV` | derived — [`observations/mass-formula-validation.md`](../../content/quantum-observable-universe/observations/mass-formula-validation.md) | 0 |
| `z_D = q³/(q²+1)` | `0.6126880371464652516` | owner ruling R1, 2026-08-15 (discrete convention) | 0 |
| `a = 1` in `a·σ + b·1` | — | **forced**: `(1−t)σ + tσ⁻¹ = σ − h·t·1` by the skein relation, so `a = (1−t)+t = 1` | 0 |
| `t = ½ − δ/4` | `0.4996560722982432260` | owner ruling R3 + `prop:flavor-split-substrate` | 0 |
| `(1−h)^(Δe/2)` | — | `QOU.QBeta.WritheNormalisation`, sorry-free, unique up to sign | 0 |
| one p–n bond | — | `A = 2` has exactly one nucleon pair | 0 |

The only discretionary elements are two **owner-ruled conventions**, and neither was
chosen against the deuteron: convention D made every `A ≥ 3` isotope **worse** by 27–40 %
(it helped only `²H`), and `bring_color_weighted` fixes the p/n *sign*, not the magnitude.
So the two discrete choices are not a fit to `²H`, and the continuous count is zero.

`L_pn` is **not** a linking number. It is `−ln f_pn` with `f_pn` the Markov-trace
suppression of the two-nucleon sub-braid relative to the unlinked pair: the interface
element `a·σ₂ + b·1` spans the two-dimensional `span{1, σ₂}` (since `σ² = hσ + 1`), and
the Markov property `tr_M(W·σ₂) = z·tr_M(W)` gives `f = a·z + b` directly. With `a = 1`
and `b = −h·t` this is `f = z − h·t`, exactly the `interfaceFactor` above.

## 3. Where the 27 % lives

Each ingredient moved **alone** to the value that would reproduce `B_AME(²H)`, against the
displacement that ingredient is actually allowed
([witness](../../computations/deuteron-two-body-kernel-overshoot.witness.json)):

| ingredient | required move | allowed | ratio |
|---|---|---|---|
| colour weight `t` | `−0.23159` (to `t* = 0.26807`) | `δ/4 = 3.439 × 10⁻⁴` | **673 ×** |
| energy scale `E₀` | `−21.47 %` | 128 ppb (whole proton↔muon pin spread) | **1.68 × 10⁶ ×** |
| Markov parameter `z` | `+12.97 %` | convention, and C is *farther* not nearer | — |
| writhe normalisation | carries `−5.6 × 10⁻⁴` of the miss | — | cannot hold it |
| `q₀` with the pin abandoned | `+2.28 %` | `1.7 × 10⁻¹¹` | `1.3 × 10⁹ ×` |

Read down the column: **no ingredient can carry the miss.** The only one that reaches the
target at all is the colour weight, and it has to travel 673 × its own derived scale — at
which point it is no longer "the p–n bond with a corrected weight", it is a different bond
type (`t = 0.268` is much nearer the p–p crossing `t = 0` than the balanced superposition).

## 4. Can `L_pn` be corrected without touching `α`? — and the CAL-2 answer

**A fix through `α = E₀` is not available, and this is now quantitative rather than
asserted.** `E₀` enters the binding *linearly*, so repairing a 21.5 % miss needs a 21.5 %
move in `E₀`. `E₀ = mₑ/(q₀(q₀−1))` is a closed form in CAL-1 and CAL-2; the entire spread
between the two documented `q₀` pins moves it by **128 ppb**. The required move is
`1.68 × 10⁶ ×` the available room. Any fix must therefore live in `L_pn`.

Inside `L_pn`, the *only* continuous freedom is the interface weight `t`, and §3 rules it
out at 673 ×. So **there is no correction to `L_pn` of the form "re-weight the interface"**
that respects CAL-2. What is *not* ruled out — and this is the whole remaining space — is a
term that is not of the form `E₀ × (interface log)` at all: an **additive** contribution,
or a replacement of the single-crossing Markov peel by something carrying the non-abelian
content of the interface.

That second option is not speculation: `deuteron_interface_handle_curvature_probe`
(2026-08-25) measured `F_q = [σ₂, σ₃] ≠ 0` and exactly traceless in the real `H₆`
seminormal rep — an interface curvature that enters in quadrature and that the scalar peel
`f = z + d` does not see. Whether it is worth `0.6 MeV` is open.

## 5. Why this front is logically prior

This morning's Faddeev–Niemi refutation
([`2026-08-26-faddeev-niemi-qh34-verdict.md`](2026-08-26-faddeev-niemi-qh34-verdict.md))
proved a non-negative functional cannot equal a sign-changing target. That argument does
not depend on Faddeev–Niemi: it generalises to **any** correction non-negative for all `A`.
`⁴He` **under**-binds (`R = +19.61`) and `²H` **over**-binds (`R = −0.61`), so no
positive additive term repairs both. Any candidate additive term must therefore be
**sign-changing in `A`** — and `A = 2` is the cheapest place to test that, having no
cluster structure, no shell effects and no p–n Coulomb.

## 6. Scope discipline

**Scope (a) — scope-limited negative.** *The two-body Markov-trace kernel, alone, with the
convention-D Markov parameter and the derived colour weighting, does not reproduce
`B_AME(²H)`; it over-binds by `+27 %`, and no interface weight within 250 × the derived
flavour split closes the gap.*

**Not scope (b).** Two things would be needed for a structural exclusion of `B_sym` and
neither is in hand:

1. The admissible family is `t ∈ [0,1]` and `B_AME(²H)` **is inside** the band
   (`[1.5598, 4.2887] MeV`, reached at `t = 0.26807`). No reachability invariant excludes
   the target.
2. `t` enters only through the interface factor, so an additive term is untouched.

Under the **excised** convention C the band was `[2.907, 5.178] MeV` and `2.2246` sat
below *all* of it — under C the deuteron was genuinely unreachable. The R1 ruling reversed
that. **Do not carry the older impossibility claim forward.**

## 7. Two corrections found on the way

**(a) The 2026-08-25 low-isotope audit's §6 band and required weight are pre-writhe.**
[`2026-08-25-low-isotope-binding-error-staleness-vs-gap.md`](2026-08-25-low-isotope-binding-error-staleness-vs-gap.md)
§6 gives the admissible band as `[2.051, 3.798]` and the required interface weight as
`t = 0.119453`. Both are **no-writhe** values, computed as if `L = −ln(z − h·t)` — but the
production `_bond_type_L` has applied the writhe normalisation `−(t−½)·ln(1−h)` to the p–n
bond since 2026-08-09, and varying `t` varies `Δe = 2t−1` with it. Writhe-consistent, the
band is `[1.5598, 4.2887]` and the root is `t = 0.26807`. **The GAP-1 verdict is
unaffected** — the target is inside the band either way, and the derived weight still
misses — only the two quoted numbers were wrong. (The same docstring in `_bond_type_L`
carries the pre-writhe band; it is quoted there as a *convention-C-vs-D* comparison, which
is what it was computed for.)

**(b) `QOU.Hecke.ClosedFormInterfaceFactors` is convention C.** The only other Lean
formalisation of the three named bond factors `f_pp`, `f_nn`, `f_pn` — the module that
*looks* like the formal backing for the production deuteron number — defines

```lean
def markovZ (s : R) : R := s / (s ^ 2 + 1)
```

in the square-root variable `q = s²`, i.e. `z = √q/(q+1)`. Its own docstring says so:
*"with Markov parameter `z = 1/(√q + 1/√q)`"*. That is **convention C**, excised by owner
ruling R1 on 2026-08-15.

This spelling is invisible to every convention-C detector in the tree — none of them scan a
square-root-variable rational form — which is how it survived the 2026-08-10 drain that
AGENTS.md records as having cleared `.lean` to zero. It is the fourteenth entry for
[`2026-08-15-detector-blindness-taxonomy.md`](2026-08-15-detector-blindness-taxonomy.md).
The corpus also contains the **D** spelling under the same name
(`QOU/MathlibExt/MarkovBondRule.lean:84`, `markovZ q = q^3/(q^2+1)`), whose docstring
already warns that the C parameter *"must not be used as the base"* — so two Lean modules
export `markovZ` under opposite conventions.

`DeuteronTwoBodyKernel` therefore states `zD` afresh and does **not** import
`ClosedFormInterfaceFactors`. **Do not "reconcile" the two by substituting `s² = q`** — the
substitution is not convention-preserving, and the algebraic theorems in the C module
(bar-involution behaviour, the `δ` cubic factorization, the `f_pn = (f_pp+f_nn)/2 + hδ/4`
identity) are correct *for C* and need re-deriving, not rewriting. Tracked as follow-up
work, not fixed here.

## Compute

- [`computations/deuteron_two_body_kernel_overshoot_probe.py`](../../computations/deuteron_two_body_kernel_overshoot_probe.py)
  — `mpf` at 60 dps, no float64, 0 free parameters, `B_AME` a comparison target only and
  never inverted. 15/15 Lean bounds cross-checked. `precision-gates.sh --changed` green.
- [`computations/deuteron-two-body-kernel-overshoot.witness.json`](../../computations/deuteron-two-body-kernel-overshoot.witness.json)
- [`content/.../lean/QOU/MassTheory/DeuteronTwoBodyKernel.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/DeuteronTwoBodyKernel.lean)
  — 7 theorems, sorry-free, `lean`-direct exit 0.

## What is still open

- The **magnitude** of the missing deuteron term (`0.608 MeV`, and it must be *negative*
  at `A = 2` while positive at `A ≥ 3`). Nothing here supplies it.
- Whether the interface curvature `‖F_q‖²` is the carrier — the pairing
  `tr_M(ρ_deuteron · dF_q)` is still uncomputed (`qou-jqof` / `qou-dp32`).
- Re-deriving `ClosedFormInterfaceFactors` under convention D (§7b).
