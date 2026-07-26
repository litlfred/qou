# Δ_λ: μ₄ via ρ_F cluster integrals — the #4320 deuteron-wall redirect (session intent 2026-07-26)

**Goal.** Derive the Δ_λ light-nucleus magnitude residual moments from the interface
operator ρ_F cluster integrals — the redirect the #4320 deuteron-wall (`6851e214`)
pinned down. The residual `ρ_strong(A)−ρ_grad(A)` is PROVED (sorry-free,
`AdditiveResidualSimplex.lean`) pure **≥3-body**: μ₂=0, μ₃=+0.4708 (A=3, 3-body/triangle),
μ₄=−4.591 (A=4, 4-body/tetrahedron). The bond-frustration `edges−κ·triangles` model died
at the deuteron (μ₂=0 ⇒ κ ill-posed). So the derivation must come from the genuine
many-body cluster integrals of ρ_F, NOT a 2-parameter simplex fit.

**Target.** Compute the ρ_F (PROBE-2 A=4 interface operator) 3-body and 4-body **cluster
integrals**; extract μ₃, μ₄; compare to +0.4708 / −4.591. The derivation-vs-fit test is the
FREE-PARAMETER COUNT: if ρ_F's cluster integrals give μ₃,μ₄ from 0–1 derived params (no AME
inversion), that's the A=3,4 magnitude closure; if it needs one param per moment, it's a fit.

**Infra.** ρ_F is "infra-reachable" per #4320 — Rust `hecke-engine` / `pyhecke-native`, or a
cached witness under `computations/`. Check availability FIRST; if the cluster integral needs
a Rust build that isn't reachable, report the honest infra-gate (κ/μ₄ IDENTIFIED but blocked),
do NOT fake the moments.

**Discipline (STRICT).** μ₃,μ₄ read from DERIVED ρ_F cluster integrals = derivation; μ₃,μ₄
tuned to +0.4708/−4.591 = FIT (labelled, never wired). "No seventh fit-based ansatz" +
PROBE-4 KL-prune stand. Formalize-first; scope-(a)/(b); nothing wired. Coordinate on
#4047 + the PROBE-2/option-e ledger.
