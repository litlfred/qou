# Δ_λ: derive the frustration weight κ from the interface operator ρ_F / s5-so3 — the last step to the magnitude (session intent 2026-07-26)

**Goal.** Upgrade the #4316 additive-term result from "sign derived, magnitude a FIT"
to a DERIVATION by fixing the two weights (κ, s) of `M(A)=s·(edges − κ·triangles)`
from 0–1 derived parameters — NOT a 2-point fit to the residuals.

**Where #4316 left it (proved):**
- Sign derived: `signChange_iff_window` — (+,−) at (A=3,A=4) iff κ∈(3/2,3), 0 free params.
- Magnitude a proven non-evidential fit: the 2-weight map is an iso (det=−6), hits any
  2 targets. Canonical un-tuned κ=[3]_q MISSES the ratio −0.1738. Fitted κ=2.385 lands it.

**The derivation target.** Fix κ (ideally to a value in (3/2,3) that lands −0.1738)
from DERIVED structure:
- **Route A (interface operator ρ_F):** the PROBE-2 A=4 interface operator computes the
  ≥4-body assembly weight; its A=3 vs A=4 ratio should PIN κ. Rust `hecke-engine`-gated —
  check if buildable/available; the corpus `computations/` may have a cached ρ_F.
- **Route B (s5-so3 fibre-action):** the WRT `W_λ` level-selection (keystone s5-so3,
  owner-opened) — the crystal level = nucleon count fixes the frustration weight.

**Discipline (STRICT).** A κ read from a DERIVED ρ_F / W_λ is a derivation; a κ tuned to
land −0.1738 is a FIT (labelled, never wired). If the Rust/WRT infra is unavailable,
report the honest infra-gate (do NOT fake κ). Formalize-first; scope-(a)/(b); nothing
wired. "No seventh fit-based ansatz" + PROBE-4 KL-prune stand.

**Coordinate.** #4047 (covariance-kernel Δ_λ), the PROBE-2 interface work, the s5-so3
keystone ledger. Overlap OK (owner); bring the κ∈(3/2,3) + −0.1738 discriminator.

---

## VERDICT (2026-07-26) — WALL for κ + redirect to μ₄

**κ is NOT derived; it is the wrong object.** The derivation attack found the
DERIVED third point `M(2)=0` (deuteron self-reference: `ρ_grad(2)=[2]!/[2]!=1`,
`ρ_strong(2)=B(²H)/B(²H)=1`) that #4316's A=3,4-only fit omitted. The
`edges − κ·triangles` model with s>0 predicts `M(2)=s>0` and is therefore
**refuted at the deuteron**; κ=t/s is ill-posed (edge coefficient forced to 0).

The exact 0-parameter simplex (Mayer) decomposition over the derived C(A,k) basis
(A=2,3,4): **μ₂(edge)=0, μ₃(triangle)=+0.4708, μ₄(tetra)=−4.591** — a **pure
≥3-body** residual, tetrahedron-dominant-negative, matching the ρ_F full-binding
Mayer `b₄/b₂=4.16` ([1⁴] SU(4) supermultiplet).

- **Route A (ρ_F):** compute AVAILABLE (`pyhecke_native` present; Rust gate lifted).
  The correct derivation target is μ₄ (4-body α-cluster residual) via the residual
  cluster integrals — identified, infra-scoped, NOT yet run. NOT a κ.
- **Route B (W_λ):** infra-GATED (WRT / full-Hecke principal specialization not
  reachable here for a per-A frustration weight).
- κ=2.385 explicitly a FIT; μ₂=0 the derived AME-independent fact. Nothing wired.

**Deliverables:** probe `deltalambda_kappa_interface_residual_simplex_probe.py`
(+witness); Lean `AdditiveResidualSimplex.lean` (sorry-free, lean-direct EXIT 0);
audit `2026-07-26-deltalambda-interface-operator-kappa.md`; option-e ledger row.
PR #4320.
