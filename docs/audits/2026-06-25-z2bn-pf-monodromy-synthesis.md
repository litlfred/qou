# z2bn lever-1 τ-derivation — third probe: PF-monodromy SL₂ synthesis

**Date:** 2026-06-25
**Branch:** `claude/z2bn-tau-pf-monodromy-synthesis-2026-06-25`
**Probe:** [`computations/substrate/z2bn_pf_monodromy_synthesis.py`](../../computations/substrate/z2bn_pf_monodromy_synthesis.py)
· **Witness:** [`computations/substrate/z2bn-pf-monodromy-synthesis.witness.json`](../../computations/substrate/z2bn-pf-monodromy-synthesis.witness.json)
· **Lean:** [`QOU/Mass/TauQuantumIntegerForm.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/TauQuantumIntegerForm.lean)

## What this synthesises

Three independent threads now bear on the binding-τ keystone operator `M` (the depth-2 prolongation
recurrence `a_D^(n+2) = τ a_D^(n+1) − a_D^(n)`):

- **Sibling #2755 (merged)** conjectured `M` = the Bring **Picard–Fuchs operator**, and Step-1
  computed the color curve has **six `I₁` nodal fibres** (Δ degree-6, *squarefree*).
- **Probe 2 (#2768, merged)** showed `M` is **not a classical `d/dz` jet** (those give q-free periods);
  it must be **q-difference**.
- **The 2026-06-24 monodromy-integrality audit** showed the topological PF monodromy is `SL₂(ℤ)`
  (integer trace) while `τ = 2.6424 ∉ ℤ`.

This probe ties them together through the `SL₂` trace, and adds one genuinely new structural fact.

## Results (all derived — no fit)

**1. `M ∈ SL₂`.** The transfer matrix `!![τ,-1;1,0]` has `det = 1` (Lean `transfer_det_one`). So the
eigenvalues `λ_±` multiply to 1 and sum to `τ`; `M` is an `SL₂` element with trace `τ`.

**2. (NEW) `τ` is a rational function of the quantum integer `[2]_q = q+q⁻¹` alone, hence bar-even.**
The proved closed form collapses:

    τ(q) = 3(3q⁴+8q²+3)/(4q(q+1)²) = 3(3[2]² + 2)/(4([2]+2)),    [2] = q+q⁻¹.

(Lean `tau_quantum_integer_form`, sorry-free.) Consequently `τ(q⁻¹) = τ(q)` — **bar-even** (Lean
`tau_bar_even`), as a Markov-trace / quantum-dimension object must be. A classical-jet trace would be
a function of `q` with no reason to collapse onto `[2]_q`; **the `[2]_q`-form is the Hecke / q-difference
fingerprint**, independently corroborating Probe 2.

**3. `M` is hyperbolic; the topological monodromy is parabolic.** `[2]_q ≥ 2` (AM–GM, equality at
`q=1`) and `9[2]²−8[2]−10 > 0` for `[2]≥2`, so `τ > 2 ∀q>0`, with **minimum `21/8` at `q=1`** (the
classical limit). Thus `M` is **hyperbolic** (`λ₊>1`): at `q₀`, `τ=2.6424`, `λ₊=2.1846`, `λ₋=0.4577`.
The `λ₊>1` growth witnesses the **seed kernel's** extensivity (`Lever1Tau.binding_extensive_at_substrate`,
#2767) — a correct conditional. **Per the #2752 calibration, the *physical* `lw` sequence grows
super-geometrically *past* `λ₊`** (ratios 1.34→2.76 > 2.185), so `λ₊` is the seed rate, **not** the full
physical binding rate. By contrast the topological PF monodromy at the `I₁` nodal fibres (squarefree Δ, #2755 Step 1) is
**parabolic, trace exactly 2** — marginal, `λ₊=λ₋=1`, no growth.

## (b)-exclusion + indicated direction

> **(b)-structural exclusion** (invariant cited: `τ ∉ ℤ` vs integer-trace `SL₂(ℤ)`). Since `τ(q) ∉ ℤ`
> for all `q` — even the classical `τ(1)=21/8` — `M ∉ SL₂(ℤ)`, so **`M` is not the topological
> Picard–Fuchs monodromy.** This formalises (via the explicit `SL₂` trace) the 2026-06-24
> monodromy-integrality finding.
>
> **Indicated (not excluded):** `M` is a q-difference operator with bar-even trace `τ([2]_q)`.
> **Base ring (§7c):** `M ∈ SL₂(ℤ[q,q⁻¹])` at the *fibre* level — `det = 1` holds over **any
> `CommRing`** (Lean `transfer_det_one` is generic) and the bar-even `[2]_q` trace lives over the
> Hecke ring `ℤ[q,q⁻¹]` / `ℚ(q)` with `q` formal (Lean `tau_quantum_integer_form`, `tau_bar_even`
> over any field). `SL₂(ℝ)` is **only** the *archimedean evaluation* at the substrate `q₀∈ℝ`, where the
> *order* statement `τ([2]_q) > 2` (hyperbolic, `λ₊>1` — the seed kernel's extensivity; the physical
> `lw` is super-geometric past it, #2752) lives. The `[2]_q`-dependence (Result 2) is the q-difference
> fingerprint. Constructing the **explicit q-difference PF operator** with this trace is the open
> keystone (owner-gated; `M` per #2755).

**Honest scope.** The integer-trace exclusion itself is the 2026-06-24 audit's; this probe's new
content is the bar-even `[2]_q` form (Result 2, Lean-formalised) and the `SL₂`-trace framing that unifies
the three threads and reads `λ₊` as the seed kernel's extensivity rate (not the full physical rate —
physical `lw` is super-geometric past `λ₊`, #2752). The construction of `M` remains genuine
multi-session math — *not* attempted here as a fit. The bar-even `[2]_q` collapse is a falsifiable
structural constraint any candidate `M` must reproduce.

## Cross-references

- [`docs/audits/2026-06-25-z2bn-prolongation-qdifference-constraint.md`](2026-06-25-z2bn-prolongation-qdifference-constraint.md) — Probe 2 (q-difference, #2768).
- [`docs/audits/2026-06-25-z2bn-tau-derivation-first-probe.md`](2026-06-25-z2bn-tau-derivation-first-probe.md) — Probe 1 (τ closed form, #2767).
- `docs/audits/2026-06-24-lever1-color-eq-monodromy-integrality.md` — integer-trace exclusion.
- `computations/substrate/lever1_color_sigma_geometry_probe.py` — #2755 Step 1 (I₁ fibres, residue gap).
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — keystone ledger; #2722 geometric `tr B`.
