# Δ_λ additive sign-changing many-body term — the route the #4307 damping-wall points to (session intent 2026-07-26)

**Goal.** After #4300 (single-q no-go) and #4307 (whole DAMPING class walled — the
residual changes sign), the Δ_λ magnitude closure is NOT a suppression factor. Per
the permanence principle, `[A]_q!` stays valid and the open target is an **ADDITIVE,
sign-changing-in-A many-body term** `M(A)` with `ρ_grad(A)+M(A)=ρ_strong(A)`:

| A | residual `ρ_strong−ρ_grad` (q₀) | M(A) must be |
|---|---|---|
| 3 | **+0.4708** | positive |
| 4 | **−2.7080** | negative |

This is a SHARP two-point target derived (not fitted) by #4307. Connects to the
corpus A=4 **interface operator** (PROBE-2, `docs/audits/2026-06-23-interface-operator-derivation-and-4body-assembly.md`)
+ `conj:s5-so3-fiber-action` (the ≥4-body assembly / brane-tower level selection).

**Overlap PERMITTED (owner: "ok to overlap", 2026-07-26).** Parallel to the active
interface/x631 work. Distinct handle: the exact two-point residual target from #4307.
Scout PROBE-2 + s5-so3 + the interface-operator audit FIRST; post intent; bring the
#4307 sign-change constraint as the discriminator.

**Discipline (STRICT).** The additive term must come from a DERIVED principle (the
interface operator's ≥4-body structure / the s5-so3 fibre action), not a two-point fit
to the residuals. A term inverted from the +0.47/−2.71 residuals is a FIT — labelled,
never wired. "No seventh fit-based ansatz" stands; PROBE-4 KL-prune stays pruned.
Formalize-first before any wide scan; scope-(a)/(b).

## Ledger

| Date | PR | Route | Free params (vs 2-pt) | Result | Wired? |
|------|----|-------|:-:|--------|:-:|
| 2026-07-26 | #4316 | **bond−frustration simplex term** `M(A)=s·(edges − κ·triangles)` on K_A | sign: **0** · magnitude: **2** | **scope-(a) PARTIAL.** Sign-change is DERIVED — `signChange_iff_window`: `(+,−)` at (A=3,A=4) iff κ∈(3/2,3), parameter-free (Lean, sorry-free). Magnitude is a **FIT** — `fit_hits_any_target`/`fit_is_unique`: the (s,t)↦(3s−t,6s−4t) map is a linear iso (det=−6), so matching both residuals is guaranteed → non-evidential. No 0/1-param derived form (κ∈{1,2,3,[3]_q}, tetra) lands the ratio −0.1738. | **No** |

**Finding summary.** The additive term the #4307 damping-wall demands *can* come
from the simplex bond/anti-bond crossing (edges attractive, frustrated triangular
faces sign-opposed): triangles grow faster than edges (`C(A,3)/C(A,2)=(A−2)/3`), so
a fixed frustration weight flips the sign between the triangle A=3 and tetrahedron
A=4. That **sign** is 0-parameter structural (Lean-certified window κ∈(3/2,3)). But
the **magnitude** match is a 2-parameter fit (invertible 2×2), hence non-evidential.
Derivation-vs-fit test: sign passes (0 params), magnitude fails (needs 2). A real
closure needs κ fixed by the PROBE-2 A=4 interface `ρ_F` (Rust-gated) or the s5-so3
level selection (WRT `W_λ`-gated) to 0–1 params. Nothing wired; anti-fit upheld.

- Audit: [`docs/audits/2026-07-26-deltalambda-additive-signchanging-term.md`](../audits/2026-07-26-deltalambda-additive-signchanging-term.md)
- Lean: [`QOU/MassTheory/AdditiveSignChangingTerm.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/AdditiveSignChangingTerm.lean) (sorry-free)
- Probe: [`computations/deltalambda/deltalambda_additive_signchanging_term_probe.py`](../../computations/deltalambda/deltalambda_additive_signchanging_term_probe.py)
