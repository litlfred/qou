---
# qou-ay84
title: 'T3c: Borromean 3-cusp deformation — proton/neutron effective κ and ϑ'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-30T16:59:40Z
updated_at: 2026-11-15T23:50:00Z
parent: qou-avtq
---

The proton is 𝔹₃ (Borromean, 3 cusps, τ=2i per cusp). The deformation space is 6D (3 complex u's), not 2D. At the symmetric point u₁=u₂=u₃=u the binding formula has cross-terms beyond 3×κ_per_cusp. Compute the full NZ Hessian for the Borromean link. Literature: Neumann-Zagier for links, Champanerkar-Kofman-Purcell.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** Open, well-posed geometry. Absorb qou-mcus here. Its "proton ϑ" comparison target is not determined by data (sign_flip_resolved=False).

Evidence: No commits or probes. The Borromean NZ Hessian is a well-posed computation.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.


## 2026-11-15 — executed under owner ruling `Q-AVTQ-2 = 1` (PR #8063, absorbing `qou-mcus`)

- **Probe & Witness:** `computations/qbeta/borromean_three_cusp_nz_hessian_probe.py` & `computations/qbeta/borromean-three-cusp-nz-hessian.witness.json` (exact Gaussian-rational `GFrac` linear algebra + 60-dps `mpmath` 8-variable Newton solver on the SnapPy 3.3.2 `L6a4` rectangular gluing equations).
- **Exact NZ Gluing Jacobian & Longitude Hessian:** At the complete regular-octahedral structure $Z_k^{(0)} = \frac{1+i}{2}$ ($\det M_{\mathrm{sys}} = -64i$), the scaled first-order shape variation $4\,\partial Z_k/\partial u_j\big|_{u=0} \in \{\pm 1 \pm i\}$ is completely dense across all 8 octahedral tetrahedra and all 3 cusps (`scaledZ1_normSq_eq_two`), yet the $3 \times 3$ longitude Jacobian is **strictly diagonal**:
  $$\left.\frac{\partial v_i}{\partial u_j}\right|_{u=0} = -2i\,\delta_{ij}, \qquad \tau_{ij} = \frac{\partial^2 \Phi}{\partial u_i \partial u_j}(0) = +2i\,\delta_{ij},$$
  with all 6 off-diagonal entries identically zero (`scaledLonJac_offDiag_zero`, forced by $\mathrm{lk}(K_i, K_j) = 0$ and $(\mathbb{Z}/2\mathbb{Z})^3$ component-reversal parity $u_j \mapsto -u_j$).
- **Quadratic vs Quartic Coupling Verdict (`sign_flip_resolved = False` at 2nd order):** Under symmetric 3-cusp deformation $u = (\delta, \delta, \delta)$, $\kappa_{\mathrm{Bor}}^{\mathrm{sym}} = 3\,\kappa_{\text{per-cusp}} + 6\,\kappa_{\text{off-diag}} = 3\,\kappa_{\text{per-cusp}}$ ($-12 < 0$ in NZ frame $u = \tfrac{1}{2}\ln M$; $+3/2 > 0$ in SnapPy log-holonomy frame $U = \ln M = 2u$). Inter-cusp coupling from shared octahedral tetrahedra first enters at **3rd order in $v_i(u)$** (quartic order $O(u^4)$ in $\mathrm{CVol}$):
  $$\frac{\partial^3 v_i}{\partial u_i^3}(0) = +\frac{i}{2}, \qquad \frac{\partial^3 v_i}{\partial u_i \partial u_j^2}(0) = -\frac{i}{2}\quad (j \neq i),$$
  flipping the cubic longitude coefficient from $+\frac{i}{12}$ on the single-cusp slice $(u,0,0)$ to $\frac{i}{12} - \frac{i}{2} = -\frac{5i}{12}$ on the symmetric locus $(u,u,u)$ (`borromeanCubicSymCoeff_eq_neg_five_twelfths`, confirmed at 60 dps to $5.21 \times 10^{-43}$).
- **Lean 4 Formalization:** `folio/quantum-observable-universe/lean/QOU/QBeta/BorromeanThreeCuspNZHessian.lean` (12 sorry-free theorems, wired into `QOU.lean`, compiled with `0` errors / `0` warnings / `0` `sorry`). Held at `status: in-progress` pending PR #8063 merge and owner closure review.
