# Lever-1 binding-τ keystone — the `M`-operator construction (owner-authorized)

**Date:** 2026-06-25
**Bean:** `z2bn` (Lever-1 FOCUS). Owner green-lit the binding-τ keystone geometry (this session).
**Predecessors:** PR #2755 (τ>2/extensive Lean + Step-1 residue-gap), `Lever1TauClosedForm` (τ closed
form), `Lever1Depth2Exclusion` (#2764, constant-τ (b)-exclusion).

## The single open object

The binding kernel is `R(q,x)=x²−τx+1`, `τ=tr B=2.6424`. The keystone is to derive `τ` as the trace
of the prolongation operator `M` (`a_D^(n+1)=M·a_D^(n)`) — **not** to fit it. Two halves are settled
and one is open:

| # | piece | status |
|---|-------|--------|
| (i) | **Existence** of a fixed-depth recurrence on the `a_D^(n)` | **PROVED** sorry-free (`prop:prolonged-periods-fixed-depth`, Cayley–Hamilton on the rank-≤8 Bring Gauss–Manin space) |
| (ii) | **Curve** = color/descartes `E_q`, genus 1 (`Jac(Bring)~E⁴`) | **PINNED** (j(q₀)=129.86; Step-1 + Step-2 probes) |
| (iii) | **Identification** `M` = the Bring Picard–Fuchs operator, *abelianised* | **OPEN** (this workplan) |

## What the two probes established (the brackets around (iii))

- **Step 1** (`lever1_color_sigma_geometry_probe.py`, PR #2755): the bare differential `λ_SW=X dz`
  carries **Res=0 at every finite branch point** (Puiseux slope finite); only `z=∞` has residue.
  So `a_D^(n)=2πiΣRes` for `n≥1` needs the *prolongation*, not the bare form.
- **Step 2** (`lever1_descartes_eq_qfamily_geometry.py`, this PR): the explicit q-family `E_q`
  (= `M`'s genus-1 block base) — j(1)=128, j(q₀)=129.86, golden cusp `s=1/φ` is the **j=1728 CM
  point**, **6 singular fibres** in q. Its **topological** Gauss–Manin monodromy is in `SL₂(ℤ)`
  (cusps + the j=1728 elliptic point) ⇒ **integer trace ≠ τ=2.6424∉ℤ**.

So both the bare-residue route and the topological-monodromy route are pinned **negative** on the
explicit geometry — confirming (not by assertion, by computation) that (iii) is genuinely the
**abelianisation**.

## The open delta — the abelianised `λ_SW` holonomy `B`

Per the M-workplan (`2026-06-06-deriving-bring-M-abelianisation-scalar.md`, `prop:mi-sw-abelianisation`):
`M = id_W ⊗ B`, `B ∈ SL₂(ℝ)` real/hyperbolic, `τ = 2cosh θ`, `θ_binding ≈ 0.78145`. `B` is the
holonomy of the **abelianised Cartan sub-connection** `A⁰ = λ_SW`, **not** the topological
`SL₂(ℤ)` monodromy of `H¹(E_q,ℤ)` (which Step 2 just showed is integer-trace). The construction:

1. **Derive `B` from `A⁰=λ_SW`** — the real-trace abelianised holonomy on `E_q`, distinct from the
   integral monodromy. This is the deep step; it must NOT be a fit to 2.6424 (numerology guard).
2. **Feed `B` through** [`bring_picard_fuchs_kernel.py`](../../computations/substrate/bring_picard_fuchs_kernel.py)
   (`supply M ⇒ get R` via Cayley–Hamilton) and check `tr` of the resulting kernel `= τ` —
   falsifiable.
3. **Discharge** `conj:qdifference-kernel-prolongation-symbol`: instantiate the conditional class,
   making `thm:binding-closure-conditional` unconditional.

## Refinement (from `2026-06-06-deriving-bring-M-abelianisation-scalar.md`) — the irreducible open core is exactly #1765

Reading the M-workplan sharpens (iii) to a single identity. `B` is **fully
structurally pinned except its trace**:

- `M = id_W ⊗ B` with `W` the irreducible 4-dim `S₅`-rep, multiplicity 2 in `H¹`
  (`s5_bring_hodge_depth.py`, 3/3) ⇒ `B` is **2×2** (depth 2);
- **`det B = 1`** (symplectic / Hodge–Riemann, `sl2_prolongation_recurrence`, sorry-free);
- so `B = [[?,?],[?,?]]` collapses to the **one** scalar `τ = tr B`, and
  `τ = (a_D⁽²⁾+a_D⁽⁴⁾)/a_D⁽³⁾` (the three-period solve, `sl2_tau_solver`).

Given the three periods, `τ` = the closed form (proved: `Lever1Tau.tau_kernel_closed_form`),
`τ>2`, extensive (proved: `BindingTauAnchorClosure`, PR #2755). **The ONLY remaining
open input is that the three SW prolonged periods equal the selection-rule values**

> `a_D⁽ⁿ⁾ = ∮ λ_SW⁽ⁿ⁾ = lw(n−1) = (1/n)·Σ_{λ⊢n} dim_q V_λ`   (the #1765 identity).

Steps 1–2 (this thread) proved this **cannot** come from bare-differential residues
(`Res(X dz)=0`) or the topological monodromy (`SL₂(ℤ)` integer-trace). So #1765 needs
either **Griffiths–Dwork on the genus-4 quintic** (a major undertaking) or a
**structural rep-theory proof** that the abelianised `λ_SW` period equals the mean
quantum dimension. Neither is a turn's compute — it is the genuine, irreducible
keystone core, now isolated with everything around it proved.

## Honest status

This PR delivers **Step 2** (the (a)-baseline: explicit q-family, topological-monodromy negative).
Step (iii)-1 (the abelianised holonomy `B`) is the genuine multi-session frontier and is **not**
attempted here — a `B` that reproduces 2.6424 must come from the `λ_SW` connection structure, not a
numerical match. No fit; nothing wired; no tier change.
