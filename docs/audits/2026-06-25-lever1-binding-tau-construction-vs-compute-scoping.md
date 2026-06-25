# Lever-1 binding-τ keystone: it is a CONSTRUCTION, not a turn-crank compute — precise gap + a refuted naive probe

**Date:** 2026-06-25
**Context:** PR #2755 (lever-1 τ-anchor algebraic closure, sorry-free Lean). Owner
(this session) extended the narrow Subgoal-2 reversal to the **binding-τ side**
(prior reversal, 2026-06-19, covered only the `W_λ` side — #2503/#2524). This doc
scopes what "derive the `λ_SW` holonomy" actually requires, before any probe is
run, per the formalize-first discipline (AGENTS.md §Formalize-first).

## What is already settled (do not re-derive)

- **Curve:** color `E_q` = descartes `y² = x³ + p(q)x + r(q)` (`s=√q`), confirmed by
  the invariant `j(q₀)=129.86` ([`2026-06-24-lever1-color-eq-monodromy-integrality.md`](2026-06-24-lever1-color-eq-monodromy-integrality.md)).
- **Kernel shape:** depth-2, `det=1`, `R(q,x)=x²−τx+1` (`prop:sl2-prolongation-recurrence`, sorry-free).
- **Algebraic τ-closure (NEW, PR #2755):** the three wired anchors
  `a_D^(2,3,4)=lw(1,2,3)` force `τ=3(3q⁴+8q²+3)/(4q(q+1)²)` and `τ>2` ⇒ kernel
  extensive — now sorry-free in `QOU.Mass.BindingTauAnchorClosure`.
- **What is NOT topological:** `τ=2.6424∉ℤ`, so `B` is not the integral `SL₂(ℤ)`
  Gauss–Manin monodromy ([integrality audit](2026-06-24-lever1-color-eq-monodromy-integrality.md)).

## The open object, stated precisely

The geometric↔algebraic identification (#1765):

$$ a_D^{(n)} \;=\; \oint_{\mathcal{S}_c} \lambda_{\mathrm{SW}}^{(n)} \;\stackrel{?}{=}\; \mathrm{lw}(n-1) \;=\; \tfrac{1}{n}\!\sum_{\lambda\vdash n}\dim_q V_\lambda . $$

From [`mi-sw-abelianisation-proof.md`](../../content/quantum-observable-universe/brings-surface/mi-sw-abelianisation-proof.md)
+ [`sw-period-residue-sum.md`](../../content/quantum-observable-universe/brings-surface/sw-period-residue-sum.md):

- `λ_SW^(0) = X dz` (explicit; `X` = color coordinate, root of the color cubic
  `X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)=0`);
- `λ_SW^(1)`: "the 1-jet component is `dX`" (implicit derivative of the cubic);
- **`λ_SW^(n≥2)`: "higher jets follow by induction"** — abstract; **no explicit /
  closed-form / computable prolongation rule is written down.**

The residue framework *asserts* each residue is "a per-block quantum-dimensional
weight on the Wedderburn decomposition" (= the `dim_q` summands of `lw`). That is
the **claim**, stated as interpretation — it is **not computed** anywhere.

## The naive residue probe is REFUTED (why this is a construction, not a compute)

A tempting in-sandbox probe: take `λ_SW^(1)=dX` literally as a 1-form on the
`z`-line `ℙ¹`, sum its residues at the branch points, compare to `a_D^(3)=lw(2)`.
**This is wrong, demonstrably:**

- `dX` is an **exact** form, so `∮_γ dX = 2πi·Σ_p Res_p(dX)` over any cycle, and
- at a branch point `X ∼ (z−z_c)^{1/2}` (square-root type, from the cubic
  discriminant), so `dX ∼ (z−z_c)^{−1/2}dz`, whose Laurent expansion has **no
  `(z−z_c)^{−1}` term** ⇒ `Res_p(dX)=0` at every branch point ⇒ `∮dX=0`.

But `a_D^(3)=lw(2)=(q+1)²/(3q)≠0`. So the literal-`dX` reading gives the wrong
answer (`0`), and the real period must come from the **prolonged connection on the
exceptional divisor `S_c`** (the blow-up `ℙ¹` at `z_c`, with the `J^nE` jet data),
**not** from a naive residue of the literal differential on the `z`-line.

`(a)`-scope (per AGENTS.md "before declaring refuted"): this refutes the *naive
literal-differential probe*, **not** the `λ_SW` route. It localizes why the route
needs the genuine construction.

## The genuine construction path (the actual owner-gated work)

1. **Make the 1-jet concrete on `S_c`.** Define `λ_SW^(1)` as the prolonged
   connection's Cartan component on the exceptional divisor `S_c` (blow-up at
   `z_c`), with its pole structure there — not `dX` on the `z`-line. Verify
   `∮_{S_c} λ_SW^(0)` reproduces the electron period and `∮_{S_c} λ_SW^(1)`
   reproduces `a_D^(2)=lw(1)=1`. This is the smallest honest, decidable check.
2. **Write the explicit `n→n+1` prolongation rule** on `J^nE` (the piece the proof
   currently defers to "by induction"). This is the keystone construction.
3. **Compute the residues** `Res_p λ_SW^(n)` on `S_c` and show the sum equals
   `Σ_{λ⊢n} dim_q V_λ /n` — i.e. that the residue family at level `n` *is* the
   Wedderburn `dim_q` weight family (the asserted interpretation, made a theorem).
4. **Instantiate** `QDifferenceKernelIsProlongationSymbol` (the conditional class)
   and discharge the conditional binding-closure theorem.

Steps 1–2 are **construction**, not numerics; Sage is *not* the blocker (the τ
arithmetic already runs at 70 dps in pure mpmath). The blocker is the explicit
prolongation map. Until step 2 exists, there is no well-posed residue to compute —
which is why a probe now would manufacture a number, not test the claim.

## Step 1 EXECUTED (2026-06-25) — geometry pinned; residue gap rigorously located

Probe [`computations/substrate/lever1_color_sigma_geometry_probe.py`](../../computations/substrate/lever1_color_sigma_geometry_probe.py)
→ `lever1-color-sigma-geometry-probe.witness.json` (6/6 assertions). Pure
sympy+mpmath, **no Sage**. Verified, all decidable:

- **Six singular fibres** (color-bundles.md): `deg Δ(z)=6`,
  `Δ=−16z⁶−24z⁵−35z⁴−50z³−35z²−24z−16` — **palindromic** (the z↔1/z bar
  symmetry) and **squarefree** (simple ramification).
- **Genus 1** (= color/descartes `E_q`): Riemann–Hurwitz `2g−2 = 3(−2)+6 = 0`.
- **Branch locus** = 3 bar-symmetric conjugate pairs at `|z| ≈ {1.000, 0.943,
  1.060}` (`0.943·1.060 ≈ 1`, reciprocal).
- **CRUX — `Res(λ_SW = X dz) = 0` at every finite branch point.** With the
  Puiseux uniformizer `z−z_c=t²`, the slope `(X−X_c)/t ≈ 1.00` is *finite*, so
  `λ_SW = X·2t dt` has lowest power `t¹` — **no `1/t` pole**. The bare
  differential carries no residue at the finite branch points.
- **Only `z=∞` carries residue:** `Res_∞(X_i dz) = {0, +5i/16, −5i/16}` on the
  three sheets (leading slopes `{−1, +i, −i}`), summing to `0` (`ΣX_i=−(z+1)`).

**Finding (rigorous, not asserted).** The residue structure `a_D^(n)=2πiΣRes` is
**empty at the finite branch points for the bare n=0 differential** — the n=0
period lives entirely at `z=∞`. Since `a_D^(n)=lw(n−1)` for `n≥2` are the
*prolonged* periods, they cannot arise from residues of `λ_SW=X dz`; they require
the poles introduced by the **prolongation `λ_SW^(n)` (n≥1)** — the jet-bundle map
left "by induction" in `mi-sw-abelianisation-proof.md`. The first genuinely
*decidable* `a_D^(n)=lw(n−1)` check (`n=2`, muon, `lw(1)=1`) is unreachable until
`λ_SW^(2)` is made explicit. So Step 1 **confirms and sharpens** the gap: it is the
explicit prolongation map, and nothing upstream of it. (The `5i/16` per-sheet
∞-residue is reported as a datum, no interpretation claimed.)

## Recommendation

Treat the binding-τ keystone as a **multi-step construction** (mirroring the `W_λ`
side's #2524 arc), beginning with **step 1** — the smallest decidable check
(`∮_{S_c}λ_SW^(0,1)` vs the electron period / `lw(1)=1`) once `S_c`'s local
coordinate + pole datum are pinned. Do **not** run a residue probe on the literal
`z`-line differential (refuted above). No fit; nothing wired; no tier change.
