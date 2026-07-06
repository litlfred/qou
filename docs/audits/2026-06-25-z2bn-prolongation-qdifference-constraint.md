# z2bn lever-1 τ-derivation — second probe: the prolongation must be q-difference

**Date:** 2026-06-25
**Branch:** `claude/z2bn-tau-prolongation-probe-2026-06-25`
**Probe:** [`computations/substrate/z2bn_prolongation_qdifference_constraint.py`](../../computations/substrate/z2bn_prolongation_qdifference_constraint.py)
· **Witness:** [`computations/substrate/z2bn-prolongation-qdifference-constraint.witness.json`](../../computations/substrate/z2bn-prolongation-qdifference-constraint.witness.json)
· **Lean:** [`QOU/Mass/ColorCubicPowerSums.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/ColorCubicPowerSums.lean)

## Context

Continuation of the first τ-derivation probe ([#2767](https://github.com/litlfred/qou/pull/2767)),
which Lean-proved the τ closed form, confirmed the color curve `E_q` (`j(q₀)=129.86`), and found no
bare-period quantity reproduces `τ`. A corpus dig then pinned the exact framework, with three findings
that reshape what a "derivation" can be here:

1. **`λ_SW^(n)` has no explicit closed form.** `mi-sw-abelianisation-proof.md` defines it *inductively*
   only: `λ_SW^(0) = X dz`; the 1-jet component is `dX`; "higher jets follow by induction." There is
   no computable operator to integrate for `n ≥ 2`.
2. **The anchors are production-wired inputs, not curve-derived.** `a_D^(2)=1`, `a_D^(3)=(q+1)²/(3q)`,
   `a_D^(4)=`Family-A come from the Wedderburn-H₄ selection rule (#1765). `mba-step09b` states plainly
   that the identification `a_D^(n) = ∮λ_SW^(n)` (SW period = selection-rule value) **"is not closed"** —
   it is the open keystone. And `_li_2_q_util.py`'s `linking_weight_family_a` flags `a_D^(4)` itself as a
   **CODATA-implied near-match** (`≈2.533` near `λ≈2.46`), not a derived categorical count.
3. **The color spectral cubic is q-free.** `X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)=0` carries no quantum
   parameter; `z` is a free base coordinate (not `√q−1/√q`).

So a direct non-fitted residue computation of the anchors is **not yet possible** — the operator to
integrate does not exist in computable form. But finding (3) yields a rigorous constraint.

> **Convergence with sibling #2755 (Construction Step 1, merged to main).** In parallel, the #2755
> Step-1 probe (`computations/substrate/lever1_color_sigma_geometry_probe.py`) independently set up the
> same color spectral curve Σ and `λ_SW = X dz`, and **computed** the residues directly: `Res(X dz)=0`
> at every finite branch point (Puiseux slope finite ⇒ no `1/t` pole); only `z=∞` carries residue
> `{0, ±5i/16}` (sheet-sum 0). That locates the gap as the explicit jet-prolongation map. **My increment
> here is orthogonal and complementary:** Step 1 shows the bare `n=0` residues are empty at finite
> points; this audit shows *why a CLASSICAL prolongation cannot rescue it either* (q-free ⇒ q-independent
> periods), thereby **narrowing the open operator to the q-difference class**. The two findings agree the
> prolongation is the gap; this one constrains its type.

## Result — (b)-exclusion of the classical-jet identification; the operator must be q-difference

Because the color cubic is q-free, every **classical** (`d/dz`) object built from it is q-free
(verified, `sympy`):

- the cubic `F(X,z)` — q-free;
- the classical 1-jet `dX/dz = −F_z/F_X = (−X²−(2z+1)X−3z²−2z−1)/(3X²+2(z+1)X+z²+z+1)` — q-free;
- the color-root power sums `p₁=−(z+1)`, `p₂=−(z²+1)`, `p₃=−(z³+1)` — q-free (Lean-proved sorry-free,
  [`color_power_sums`](../../content/quantum-observable-universe/lean/QOU/Mass/ColorCubicPowerSums.lean), over a generic ring with no quantum parameter).

Hence any period `∮λ_SW^(n)` of a **classical** jet prolongation — an integral of q-free differentials
over q-free cycles — is **q-independent**. But the anchor `a_D^(3) = (q+1)²/(3q)` is **q-dependent**
(`d/dq = (q²−1)/(3q²) ≠ 0`).

> **(b)-structural exclusion (invariant cited: q-independence of classical-jet periods vs q-dependence
> of the anchor).** The identification `a_D^(n) = ∮λ_SW^(n)` with a **classical** (`d/dz`) jet
> prolongation is impossible — a q-independent quantity cannot equal a non-constant function of `q`.
> Therefore the lever-1 prolongation operator is **not** a classical jet; it **must** be a
> **q-difference** operator — precisely the bean's "fibre q-difference kernel `R(q,x)`" direction.

**Scope (per AGENTS.md (a)/(b) discipline).** This is a genuine **(b)** exclusion of *the classical-jet
identification only*. The **q-difference class is NOT excluded** — it is the surviving, indicated
direction. The explicit q-difference prolongation operator (the one whose residues should reproduce the
anchors) remains the open keystone; the anchors stay wired Wedderburn-H₄ inputs. No fit; nothing tuned.

## Net for z2bn

The two probes together convert a vague "the prolongation operator is open" into a sharp target:
**find the q-difference operator `R(q,x)`** (not a classical jet) whose `∮λ_SW^(n)` residues on the
color curve reproduce the wired anchors `1, (q+1)²/(3q), Family-A`. The first probe gave the τ closed
form (Lean) + the curve; this probe rules out the classical-jet route and points squarely at the
q-difference kernel the bean already names. The full geometric closure stays the owner-gated keystone.

## Cross-references

- [`docs/audits/2026-06-25-z2bn-tau-derivation-first-probe.md`](2026-06-25-z2bn-tau-derivation-first-probe.md) — first probe (τ closed form, curve, holonomy residual).
- `content/quantum-observable-universe/brings-surface/mi-sw-abelianisation-proof.md` — inductive `λ_SW^(n)`.
- `content/quantum-observable-universe/brings-surface/sw-period-residue-sum-proof.md` — `a_D^(n)=2πi ΣRes`.
- `content/quantum-observable-universe/mass-theory/mba-step09b-per-isotope-binding.md` — "identification not closed".
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — keystone ledger; #2722 holds the geometric `tr B` side.
