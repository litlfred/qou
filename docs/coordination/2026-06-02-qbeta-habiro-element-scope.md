# Topic 1 — Q_β Habiro element categorical identification

**Date:** 2026-06-02
**Branch:** `claude/qbeta-habiro-element-2026-06-02`
**Trigger:** PR #1698 Subgoal-1 follow-up (merged `4cd808f05b`); owner directive "1 2 3"; AGENTS.md gap-map highest-priority item.

Per AGENTS.md "Precision goals" + the L2 100× shared-root audit (`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`), the Q_β Habiro element is the **highest-priority gap**: gates c_4-c_7 Taylor coefficients of `Q_β = Q_base · Π(1 + c_k u^k)` AND, via shared root, the three failing L2-100× observables (m_n, Q_β, Δ_pn).

## State of the framing (AGENTS.md §"Q_β c_k truncation order")

- `u = b · ℏ_q² ≈ 0.00852` — Q_β precision-ladder variable.
- `c_2 = -1` — **PROVED Taylor-exact**.
- `c_3 = -2 = J_Hopf(q=1)` — **NEAR-MATCH at q_0** (2.98 % cross-anchor swing between q_proton and q_muon; up to 3.47 % displacement at the m_p-anchor q_0 alone per AGENTS.md §"Q_β c_k truncation order"); 4-session flip-flop history settled 2026-05-31 as fibre-vs-observable Im(q) distinction (AGENTS.md §"Critical framing").
- `c_4 - c_7` — **OPEN**, blocked on the Habiro element identification.

## What the open question actually is

Per AGENTS.md §"Im(q) at fibre vs observable level (2026-06-01)":

> The c_k Taylor coefficients live in the FIBRE (formal q-deformation, potentially complex). Each q_0 anchor is a different archimedean evaluation of the SAME fibre object. The "cross-anchor swing" caught as "near-match" is the fibre object having structure beyond a real constant — exactly what you'd expect if c_k(q) is a complex-analytic function evaluated at real q_0.

So Topic 1 is: **find the fibre-level Habiro element `F(q) ∈ Habiro ring` whose archimedean evaluation at any q_0 reproduces c_k at that anchor.** Looking for a REAL formula `c_3 = f(q_0_real)` matching multiple anchors was already known to fail. The fibre-level object is the actual research target.

## Categorical reuse from sibling #1521 (α_em Habiro element)

PR #1521 (open, not yet merged) **proposes** the **categorical identification** for the **α_em Habiro element**:

| α_em piece | categorical structure |
|---|---|
| `[2]_q` | `J_2(unknot)` — colored Jones of trivial knot at N=2 = q-dim of fundamental SU_q(2) rep |
| `(1 - h²α)` | 2-vertex Hecke quadratic σ² = hσ + 1 with α coupling |
| `1/(8π)` | `1/(π · dim H¹(M_Bring))` — Bring cohomology dimension at g=4 |

Combined: `α · [2]_q/(8π) · (1 - h²α)`.

**Reuse for Q_β Habiro:** if the Q_β Habiro element has analogous structure (colored Jones of some specific knot × Hecke quadratic × Bring-cohomology normalization), the same framework applies — but with potentially:
- A DIFFERENT knot (Q_β is the neutron β-decay width, observable structure is different from α_em vacuum polarization)
- A FIBRE-level (complex) construction rather than archimedean-real
- A different Bring-cohomology slot (M_Bring's H¹, H², or some other Hodge piece)

**Cherry-pick targets** from #1521 to reuse:
- `[N]_q = J_N(unknot)` sanity (verified N=1..5)
- `dim H¹(M_Bring) = 2g = 8` at g=4 (structural constant)
- Habiro Taylor coefficient binomial-series patterns

## Phase A — re-frame using the fibre-level distinction

Per AGENTS.md, the trio `c_2 / c_3 / c_4` should be re-examined at fibre level:
- `c_2 = -1` proved Taylor-exact ✓ (archimedean fact too)
- `c_3` cross-anchor swing 2.98 % (compute precision << 1 ppQ, so swing IS structural, not noise)
- `c_4` unknown

The α_em PR #1511 (merged) `[2]_q · (1 - h²α)` is a FIBRE-level element. Its Taylor evaluation gives the empirical numerical pattern. For Q_β, what fibre element has Taylor evaluation matching `c_2 = -1` exactly and `c_3` with the empirically-observed cross-anchor swing?

## Phase B — Galois descent on Habiro ring (per gap map)

Per the gap map (PR #1698 session): "Symbolic q-difference solver (sympy on multi-block Iwahori-Hecke) OR Galois descent on Habiro ring; cross-anchor (q_proton + q_muon) validation required before wiring".

Two attack methodologies:
1. **Symbolic q-difference solver** — represent the Q_β precision-ladder as a q-difference equation, solve symbolically, extract Habiro Taylor coefficients
2. **Galois descent on Habiro ring** — use the fibre-level complex-analytic structure to constrain Habiro coefficients via Galois action

## Phase C — Lean §3b-cond scaffold (deferred)

After the categorical identification, add a Lean class `QBetaHabiroElement` mirroring the §3b-cond pattern used in `OperatorValuedCombiner.lean` (PR #1698): class fields encode the fibre-level identification, theorem applies it at concrete c_k.

## Out of scope (per AGENTS.md)

- **No new ansatz fits** for c_k (the 4-session c_3 flip-flop saga is the cautionary tale).
- **No "binary wired/dropped" decisions** — report TIERED (proved / near-match / fitted) per the canonical reference [`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](../audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).
- **No production wiring** until cross-anchor validation passes at both q_proton and q_muon.

## Coordination

Sibling #1521 (α_em Habiro) — methodology DEPENDENCY + CHERRY-PICK. Intent posted on sibling PR; we'll cite their categorical-identification verdict if Q_β Habiro element exhibits same RT-shadow-world structure, or diverges.

## Cross-references

- L2 100× shared-root: [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](../audits/2026-05-30-l2-100x-status-3-failing-shared-root.md)
- Q_β c_k canonical framing (settled 2026-05-31): [`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](../audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
- Fibre vs observable Im(q) (2026-06-01): AGENTS.md §"Im(q) at fibre vs observable level"
- α_em Habiro categorical ID (sibling): PR #1521 + [`PR #1511`](https://github.com/litlfred/qou/pull/1511) (merged)
