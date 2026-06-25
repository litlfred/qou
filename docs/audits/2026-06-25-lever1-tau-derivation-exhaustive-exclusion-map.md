# Lever-1 `τ`-derivation: the exhaustive exclusion map, and why Griffiths–Dwork is the *wrong* tool

**Date:** 2026-06-25
**Bean:** `z2bn` (Lever-1 FOCUS). Capstone of the owner-authorized binding-τ keystone push
(PRs #2755, #2772 this session).

## The object

The binding kernel is `R(q,x)=x²−τx+1`, `det B=1`, so the keystone is the single number
`τ = tr B = 2.6424`. The corpus identifies `B` as the **abelianised `λ_SW` Cartan-connection
holonomy** — a real, hyperbolic `SL₂(ℝ)` element, `τ = 2cosh θ`, `θ_binding ≈ 0.78145`
(`prop:mi-sw-abelianisation`; 2026-06-24 integrality audit). It is settled that:

- existence of a fixed-depth recurrence — **proved** (`prop:prolonged-periods-fixed-depth`);
- depth 2, `B` is 2×2 — **proved** (S₅-Hodge, `s5_bring_hodge_depth.py`);
- `det B = 1` — **proved** (symplectic, `sl2_prolongation_recurrence`);
- given `a_D⁽²,³,⁴⁾`, `τ` = closed form, `τ>2`, kernel extensive — **proved**
  (`Lever1TauClosedForm`, `BindingTauAnchorClosure`, PR #2755).

The lone open piece is whether `τ` is the trace of a *geometric* object, or only a seed-fit from
the three wired anchors `a_D⁽²,³,⁴⁾ = lw(1,2,3)`.

## The exhaustive exclusion map

Every standard geometric route to `τ` is now **excluded** — each computes either zero, the wrong
(integer-trace) object, or a compact object:

| # | route | what it computes | verdict |
|---|-------|------------------|---------|
| 1 | residues of the bare differential `λ_SW=X dz` | `2πiΣRes` at finite branch points | **= 0** (holomorphic in the √-uniformizer; Step 1, PR #2755) |
| 2 | topological Gauss–Manin monodromy of `E_q` | `SL₂(ℤ)` element (preserves `H¹(E,ℤ)`) | **integer trace ≠ τ** (Step 2, PR #2772: cusps + j=1728) |
| 3 | **Griffiths–Dwork on Bring (genus 4)** | the **Gauss–Manin connection** — i.e. route 2's object on the full `H¹` | **integer trace** ⇒ *wrong tool* (see below) |
| 4 | coral / trefoil holonomy of `E_z` | compact `SU(2)`, `(H₁H₂)³=id` | `\|tr\|≤2` — cannot be hyperbolic `τ>2` (`coral-elliptic.md`) |
| 5 | the `lw` selection-rule sequence as `Mⁿv₀` | a constant-coeff depth-2 orbit | **`lw` is NOT depth-2** (#2764 / #2708): `τ` is a 3-pt seed-fit, `a_D` diverges from `lw` past `n=4` |
| 6 | bare SW periods `a, a_D` and their ratios | genus-1 elliptic periods of `E_q` | **no quantity reproduces `τ`** (`z2bn_tau_derivation_probe`) |

### Why Griffiths–Dwork (route 3) is the wrong tool — the key correction

The M-workplan (`2026-06-06-…-M-abelianisation-scalar.md`) proposed *"supply `M` via Griffiths–Dwork
on the genus-4 quintic."* But Griffiths–Dwork computes the **Gauss–Manin connection**, whose monodromy
preserves the integral lattice `H¹(Bring,ℤ)` and hence lies in `Sp(8,ℤ)`; its restriction to the
rational sub-Hodge-structure `W` (the `E_q` factor) lies in `SL₂(ℤ)` — **integer trace**. Route 2
*already computed this restriction* and found integer trace ≠ τ. So a full genus-4 Griffiths–Dwork
would faithfully reproduce the integer-trace topological object and **still miss `τ=2.6424∉ℤ`**.

The abelianised `B` (`τ=2cosh θ`, real) is **not** the Gauss–Manin monodromy — it is the holonomy of
a *different* flat connection, the Cartan reduction `A⁰ = λ_SW` (a real / "special-geometry"
connection, not acting on the integral lattice). Griffiths–Dwork has no access to it. **Do not spend
a multi-session Griffiths–Dwork effort here — it targets the wrong object** (this supersedes the
M-workplan's route-3 suggestion, consistent with the 2026-06-24 integrality audit).

## Honest frontier

What remains is genuinely *not* a standard period computation. The irreducible open object is the
**explicit abelianised Cartan-connection 1-form `A⁰ = λ_SW` and its real holonomy** — which the corpus
describes only abstractly (`prop:mi-sw-abelianisation`), and which is distinct from every geometric
monodromy/period above. Closing it needs **new differential-geometric construction** (the explicit
abelianised connection + its non-topological holonomy), not Griffiths–Dwork, not residues, not bare
periods.

Two honest framings of the present state:

1. **Production already uses the answer.** `τ` is fixed by the three wired anchors
   `a_D⁽²,³,⁴⁾ = lw(1,2,3)` (`a_D⁽⁴⁾` = the production proton multiplier), giving the proved closed
   form. The binding kernel + extensivity are machine-checked on this. This *works*; it is a
   3-point determination, not a from-first-principles geometric derivation.
2. **The first-principles geometric derivation is open** — and, per the exclusion map, will *not*
   come from any standard tool. It is a real research problem (the abelianised-connection
   construction), correctly isolated, with all shortcuts closed.

No fit; nothing wired; no tier change. This doc redirects future effort away from the excluded routes.
