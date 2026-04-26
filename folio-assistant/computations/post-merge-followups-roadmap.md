# Post-merge followups roadmap (PR #427 → #433)

PR #427 merged the structural foundations:
- Wenzl-bridge closed-form for $y_\lambda$ (convention puzzle CLOSED)
- $y_\lambda$ symbolic at $n = 2, \ldots, 12$ (270 partitions in 45 s)
- GB filtration gauge invariance verified to $10^{-16}$
- $\alpha_\lambda$ closed forms at $H_4$, numeric at $H_5, H_6$
- Wedderburn-Bratteli recursion documented and Lean-stubbed

This branch (PR #433) picks up the **deferred** structural items.
**Scope of this PR: initial roadmap + units-bridge probe + clean
closed-form derivations at small $n$.** Items B and C are mapped out
here and will be implemented in **subsequent commits / branches**;
this PR opens with the planning + first probes.

## Open items (from PR #427 deferred)

### A. Cross-witness schema standardization (Copilot review)

The repo's canonical schema (`folio-assistant/schemas/types.ts` →
`ComputationWitness`, with `folio-assistant/computations/witness_base.py`)
uses `computedAt`. Most witnesses pre-dating the schema use
`timestamp`; the 34 newer witnesses introduced in PR #427 use
`timestamp_utc`. Three legacy fields, one canonical:

| Key | File count | Action |
|---|--:|---|
| `timestamp` (legacy) | 244 | Migrate to `computedAt` |
| `timestamp_utc` (newer, PR #427) | 34 | Migrate to `computedAt` |
| `computedAt` (canonical) | (`ComputationWitness`-using files) | Keep |

| α-indexing in `strict-3cal-unified-mass.witness.json` | 1 file | Document convention divergence in metadata, OR migrate to closed-form values |
| `precision` field consistency | mixed `f64_numeric_fallback`, `mpfr_50dps`, `symbolic_q` | Already standardized via PR #427 metadata |

### B. ⁶Li, ⁷Li atom-knot identification

Mass-table-ppb in main has all of D, T, ³He, ⁴He, ⁸Be, ¹²C, ¹⁶O,
²⁰Ne, ²⁴Mg, ⁴⁰Ca but NOT ⁶Li/⁷Li (no rule). With the new MPFR
characters and Wenzl-bridge symbolic $y_\lambda$ at $n = 2, \ldots, 12$
**(PR #427 ceiling)**, the hyperbolic-volume hypothesis for
⁶Li↔K, ⁷Li↔K' is testable for $A \leq 4$ directly via 3A-strand
Hecke characters. Higher-A characters at $n = 18, 21$ require
**extending the Wenzl-bridge witness past $n = 12$** (mechanical
extension of the existing infrastructure since the formula is
$O(p(n) \cdot \max\text{hooks})$ — n=18 has $p(18) = 385$,
n=21 has $p(21) = 792$, both tractable in seconds).

**Plan**:
1. Extend Wenzl-bridge symbolic $y_\lambda$ to $n = 21$.
2. Enumerate hyperbolic knots/links with crossing-number ≤ 10 and
   Hecke depth signatures matching ⁶Li (B = 31.99 MeV) and ⁷Li
   (B = 39.24 MeV) at the framework prefactors $\rho \in \{m_e, 2 m_e\}$.
3. Cross-check via Hoefsmit characters at $H_{18}, H_{21}$ with
   Wenzl-bridge $y_\lambda$.
4. If a clean match is found, extend mass-table-ppb to A = 6, 7.

### C. $\alpha_k$ → MeV $\alpha_k$ bridge

The existing `depth_resolved_phi_k_hoefsmit.py` uses fitted
$\alpha_k$ ≈ 18 MeV for the dominant strata. My structural
**stratum-summed** $\alpha_k = \sum_{\lambda \in \Lambda_k} \alpha_\lambda$
are dimensionless O(0.1–1). The bridge is:

$$
\alpha_k^{\mathrm{MeV}} \stackrel{?}{=} m_e \cdot \alpha_k^{\mathrm{struct}} \cdot \kappa
$$

where $\kappa$ is a single physical-coupling constant. Determining
$\kappa$ structurally (vs from a fit) is the remaining gap to
1-ppb predictions.

**Probe** (`alpha_lambda_mev_bridge_probe.py`, in this PR): compute
the ratio at $k = 0, 1, 2, 3$ for $H_3$ and $H_4$.

**Probe result** (committed in this PR, see
`alpha-lambda-mev-bridge-probe.witness.json`): κ values at H_3
range from $-0.005$ to $+145$ to $-6$ — **NOT a single constant**.
At H_4 the κ values span $-980$ to $+373$. The bridge is **NOT**
reducible to a single multiplicative scaling. The structural
$\alpha_\lambda$ and the fitted $\alpha_k^{\mathrm{MeV}}$ live in
different parameterisations because the fit absorbs the divergent
$q$-deformed Plancherel weight $w_\lambda^{(q)} = \dim_q(\lambda)^2 / [n]_q!$,
while the structural derivation uses the gauge-free Jones-Markov
$y_\lambda$ which is bounded.

**Implication**: 1-ppb mass predictions from the structural side
require a **different mass-formula structure**, not a constant
rescaling of the fitted form. Specifically, the structurally
derived $y_\lambda$ would need to enter a formula where the
divergent $w_\lambda^{(q)}$ doesn't appear — a reformulation that
the lit search hasn't yet identified. **This is a research-grade
open problem**, not addressable by single-session computation.

## Order of work in this branch

1. **C** (units bridge probe) — ✅ implemented, NEGATIVE result documented.
2. **B** (⁶Li/⁷Li atom-knot ID) — pending; needs Wenzl-bridge extension to n=21 first.
3. **A** (schema standardization to `computedAt`) — pending bulk migration.

Each will be a separate commit + content block. Branch will be
prepared for merge after at least one item closes.
