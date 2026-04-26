# Post-merge followups roadmap (PR #427 → next)

PR #427 merged the structural foundations:
- Wenzl-bridge closed-form for $y_\lambda$ (convention puzzle CLOSED)
- $y_\lambda$ symbolic at $n = 2, \ldots, 12$ (270 partitions in 45 s)
- GB filtration gauge invariance verified to $10^{-16}$
- $\alpha_\lambda$ closed forms at $H_4$, numeric at $H_5, H_6$
- Wedderburn-Bratteli recursion documented and Lean-stubbed

This branch picks up the **deferred** structural items.

## Open items (from PR #427 deferred)

### A. Cross-witness schema standardization (Copilot review)

| Key collision | Files | Resolution |
|---|---|---|
| `timestamp` vs `timestamp_utc` | 244 vs 34 (this PR's new files) | Standardize on `timestamp` (dominant) — ~34 files to update |
| `α_1, α_3` indexing in `strict-3cal-unified-mass.witness.json` | 1 file | Document convention divergence in metadata, OR migrate to closed-form values |
| `precision` field consistency | mixed `f64_numeric_fallback`, `mpfr_50dps`, `symbolic_q` | Already standardized via PR #427 metadata |

### B. ⁶Li, ⁷Li atom-knot identification

Mass-table-ppb in main has all of D, T, ³He, ⁴He, ⁸Be, ¹²C, ¹⁶O, ²⁰Ne,
²⁴Mg, ⁴⁰Ca but NOT ⁶Li/⁷Li (no rule). With the new MPFR characters
and Wenzl-bridge symbolic $y_\lambda$ at $n = 18, 21$, the
hyperbolic-volume hypothesis for ⁶Li↔K, ⁷Li↔K' is testable.

**Plan**:
1. Enumerate hyperbolic knots/links with crossing-number ≤ 10 and
   Hecke depth signatures matching ⁶Li (B = 31.99 MeV) and ⁷Li
   (B = 39.24 MeV) at the framework prefactors $\rho \in \{m_e, 2 m_e\}$.
2. Cross-check via Hoefsmit characters at $H_{18}, H_{21}$ from the
   Wenzl-bridge formula.
3. If a clean match is found, extend mass-table-ppb to A = 6, 7.

### C. $\alpha_\lambda$ → MeV $\alpha_k$ bridge

The existing `depth_resolved_phi_k_hoefsmit.py` uses fitted
$\alpha_k$ ≈ 18 MeV for the dominant strata. My structural
$\alpha_\lambda$ are dimensionless O(0.1–1). The bridge is:

$$
\alpha_k^{\mathrm{MeV}} \stackrel{?}{=} m_e \cdot \alpha_\lambda^{\mathrm{struct}} \cdot \kappa
$$

where $\kappa$ is a single physical-coupling constant. Determining
$\kappa$ structurally (vs from a fit) is the remaining gap to
1-ppb predictions.

**Probe**:
- Compute $\alpha_k^{\mathrm{MeV,fit}} / (m_e \cdot \alpha_k^{\mathrm{struct}})$ at $k = 0, 1, 2, 3$ for $H_3$ and $H_4$.
- If the ratio is constant across $k$, $\kappa$ is well-defined; can
  then identify $\kappa$ structurally via Catalan/q-rational forms.
- If the ratio varies with $k$, the bridge is more subtle (depth-
  dependent prefactor).

## Order of work in this branch

1. **C** (units bridge) — biggest impact on mass-table precision.
2. **B** (⁶Li/⁷Li atom-knot ID) — extends mass-table coverage.
3. **A** (schema standardization) — cleanup, no blocking.

Each will be a separate commit + content block. Branch will be
prepared for merge after all three or as user directs.
