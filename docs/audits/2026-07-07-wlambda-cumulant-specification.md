# W_λ per-body-order specification — a falsifiable cumulant signature for the Δ_λ-gate closure

**Date:** 2026-07-07 · **Type:** GAP-A bridge (reeb-flow program → Δ_λ-gate
extensive-series frontier). **Discipline:** measurement + scope, **no seventh
fit-based ansatz**, no closure claim, no production rewire. Every negative is
scope-(a) unless a proved invariant licenses (b).

Bridges the just-completed reeb-flow program (tranches 1/7 — the open-bond/loop
dichotomy and the collective-determinant many-body finding) to the standing
Δ_λ gate as reframed in
[`2026-07-05-delta-lambda-gate-status.md`](2026-07-05-delta-lambda-gate-status.md)
§0.1: nuclear binding is **extensive** ($\propto A$), the trace-difference is
**intensive** (saturates ~3–4 MeV), so the closure is an additive many-body
series $B(K)=\sum_{b}B_b + (\text{higher-body})$, and the object supplying the
higher-body terms is the knot-ideal projector $W_\lambda$.

## 1. Measured specification (probe `wlambda_cumulant_specification.py`)

The best current many-body categorical object is the **collective
complete-graph determinant** $B_{\det}=-E_0\ln\det(I+G)$ (tranche 7; all
inter-nucleon crossings at the derived magnitude $g$). Ursell-inverting its
light-series binding into connected cumulants (same inversion as the AME
target, non-circular) and comparing to AME:

| body order | AME (MeV) | collective det (MeV) | det / AME | W_λ correction (MeV) |
|---|--:|--:|--:|--:|
| $b_2$ (pair) | 2.2245 | 0.9318 | **0.419** | **+1.293** |
| $b_3$ (connected 3-body) | 1.4264 | 1.4868 | 1.042 | −0.060 |
| $b_4$ (connected 4-body) | 9.2431 | 15.058 | **1.629** | **−5.814** |

**The W_λ signature (falsifiable).** The correction $W_\lambda$ must inject,
relative to the collective determinant, is **sign-definite and body-order
specific**:

1. **$b_2$: raise by +1.29 MeV/pair.** The determinant under-supplies the
   2-body term (0.42×) because it treats the single pn pair as a *closed loop*
   ($O(g^2)$), but the pair is an *open bond* ($O(g)$) — precisely the proved
   open-bond/loop dichotomy (`ss_det_no_linear_term`,
   `QOU.MassTheory.ReebPnMagnitude`). The proved open-bond value $5g=2.234$
   (in-unit) already supplies exactly this correction. **This leg is
   understood.**
2. **$b_3$: leave ≈ intact.** The determinant's connected 3-body is within
   4.2 % of AME (1.042×). W_λ must perturb it only slightly.
3. **$b_4$: lower by −5.81 MeV.** The determinant *over*-supplies the connected
   4-body (1.63×). W_λ must *subtract* here — the opposite sign from $b_2$.

So $W_\lambda$'s cumulant fingerprint is **(+, ≈0, −)** across (2-body, 3-body,
4-body): it raises the open-bond pair term and lowers the connected 4-body,
leaving 3-body nearly unchanged. This is a *measured, falsifiable target* — not
a closure and not a fit; scope-(a) (the determinant is one categorical object;
the spec constrains any $W_\lambda$ relative to it).

## 2. Scope — a cheap falsifiable W_λ sub-step (before the DG build)

The `uer8` core is the Beasley–Witten Seifert–Chern-Simons DG realization of
$W_\lambda$ (the FR-projector survivor of the value-step narrowing;
[`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md), value-step legs
A/B/C + capstone formalized). That build is hard and multi-session. §1 supplies
a **cheap gate to run first**:

> **Falsifiable sub-step (proposed).** Compute the FR-projector $W_\lambda$'s
> per-body-order contribution to $B(K)=m_e\sum_\lambda y_\lambda\chi^\lambda W_\lambda$
> and check its **cumulant sign signature** against §1: does it **add** to
> $b_2$, leave $b_3$ ≈ intact, and **subtract** from $b_4$? 
>
> - **If the signs mismatch** (e.g. the FR-projector also over-supplies $b_4$,
>   or under-supplies $b_2$), the geometric $W_\lambda$ is **pruned or
>   re-scoped before any DG construction** — a scope-(a) negative that saves
>   the multi-session build.
> - **If the signs match**, the DG build has a *quantitative falsifiable
>   target* (the exact +1.29 / −5.81 MeV corrections), turning an open-ended
>   construction into a checkable one.

This is the formalize-first discipline applied to the geometric leg: the §1
signature is an invariant the DG realization **must** meet, cheap to test on
the FR-projector's known Wedderburn action *before* committing to the
differential-geometry machinery. It does **not** attempt the build, propose a
$W_\lambda$ form, or fit — it converts the reeb-flow program's many-body finding
into a falsifiable gate for the next keystone session.

## 3. Relation to prior GAP-A results

- **Consistent with the extensive-series reframing** (gate-status §0.1): the
  higher-body cumulants are large ($b_3+b_4$ supply ~55 % of $B(^4\mathrm{He})$),
  confirming *why* an intensive per-block density fails and a many-body series
  is required.
- **Consistent with the six-ansatz refutations** (`b9ra`): §1 does not propose
  a seventh $\Delta_\lambda$; it specifies what the *categorical* $W_\lambda$
  (GAP-A-3/A-4 route) must do, which is the owner-sanctioned direction.
- **New content:** the sign-definite body-order signature (+, ≈0, −) — a
  falsifiable gate not previously stated, derived from the collective-determinant
  vs AME cumulant comparison.

## 4. Cross-references

- Probe: [`computations/probes/wlambda_cumulant_specification.py`](../../computations/probes/wlambda_cumulant_specification.py) + witness.
- Extensive-series reframing: [`2026-07-05-delta-lambda-gate-status.md`](2026-07-05-delta-lambda-gate-status.md) §0.1.
- Open-bond/loop dichotomy (the $b_2$ leg): [`2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md`](2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md) §2h–2i; `QOU.MassTheory.ReebPnMagnitude`.
- W_λ value-step narrowing: [`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md).
