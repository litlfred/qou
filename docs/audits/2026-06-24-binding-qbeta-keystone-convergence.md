# Two levers, one wall: the binding `R(q,x)` lever and the Q_β/m_n lever both reduce to the owner-gated keystone `M`

**Date:** 2026-06-24
**Type:** coordination synthesis (no fit; no new compute; references this session's merged probes + the kehn milestone). Not a c_k wire/un-wire decision — dodges the flip-flop guard by construction.
**Beans:** `z2bn` (binding lever-1), `kehn` (Q_β/m_n lever), `s5bb` (the keystone).

## Claim

The framework's two independent "lever-1" attacks on the binding/mass residuals — the **binding
generating-function kernel** (`z2bn`) and the **Q_β/m_n precision lever** (`kehn`) — are now
established to reduce to the **same single owner-gated object**: the s5-so3 Habiro keystone monodromy
`M`. Neither closes without it, and this session showed there is **no algebraic shortcut** to it.

## Lever A — binding `R(q,x)` (`z2bn`, this session, merged in #2708)

The binding kernel is the depth-2 `det=1` recurrence `R = x² − τx + 1`, and everything reduces to the
single trace `τ = tr B = 3(3q⁴+8q²+3)/(4q(q+1)²) = 2.6424` at `q₀`. This session mapped `B` exhaustively:

- The rank-2 `W` is the color/descartes elliptic curve `E_q` (`j(q₀)=129.86`; sibling `Jac(Bring)~E⁴`, on main).
- `B` is **not** compact SU(2) (`τ>2`, hyperbolic), **not** the topological `SL₂(ℤ)` monodromy (`τ∉ℤ`),
  **not** an `lw`-recurrence rate (the depth-2 recurrence fails past the n=2,3,4 seed), and **not** any
  integer/golden `τ` (the icosahedral `τ=3`, `λ=φ²`, is refuted by the wired seed — 19 % miss).
- `B` **is** the abelianised `λ_SW` Cartan-connection holonomy on `E_q` — `SL₂(ℝ)`, hyperbolic,
  `θ_binding=0.7815` — which is the keystone q-family `M` restricted to the elliptic factor.

Audits (all on main): `2026-06-24-lever1-{binding-monodromy-hyperbolicity, color-eq-monodromy-integrality,
lw-depth2-recurrence-falsified, lambda-sw-no-shortcut}.md`.

## Lever B — Q_β / m_n (`kehn`, sibling #2723)

PR #2723 wired the parameter-free Kashiwara b² truncation into the canonical neutron
(`m_n = m_p + Q_β + m_e`), achieving **m_n: −1759 → +1.04 ppb** (and Q_β `−2112 → +1.25` ppm) — tier
**near-match**. The bean records the exact closure as explicitly "gated on the s5-so3 / Habiro
keystone (bean `s5bb`; siblings #2409, #2524)." Per `ck-dk-canonical-registry.md`, the open object is
the **Q_β Habiro element / kernel `F(q)`** with cross-anchor (proton + muon) validation — an element of
the same keystone ring.

## The convergence

| | Lever A (binding) | Lever B (Q_β/m_n) |
|---|---|---|
| observable | binding `B(K)` / Δ_λ | `m_n`, Q_β |
| reduces to | `τ = tr B` of `M` on the color `E_q` factor | the Habiro element `F(q)` of `M` |
| status | near-mapped; `τ=2.6424` exact at seed | near-match (m_n +1.04 ppb) |
| residual | the abelianised `λ_SW` holonomy of `M` | the cross-anchor Habiro element of `M` |

Both residuals are **facets of the single s5-so3 keystone `M`** (the q-family Gauss–Manin monodromy /
Habiro element at `q₀`). The keystone ledger already carries the geometric `W_λ` side; this note records
that the **binding and Q_β/m_n observables are the two downstream consumers** that close together when
`M` is pinned.

## Implication (prioritization input for the owner)

1. **Closing `M` closes both** `m_n`/Q_β *and* the binding gate — so `M` gates ≥ 2 of the 4 failing L2
   observables, raising its priority above any single-observable patch.
2. **There is no algebraic shortcut** to `M`'s trace `τ=2.6424` (this session ruled out compact-SU(2),
   topological-`SL₂(ℤ)`, `lw`-recurrence, and integer/golden `τ`). The remaining path is the genuine
   genus-1 `λ_SW` period integration on `E_q` (needs Sage — blocked in the current sandbox) plus owner
   sign-off on the Subgoal-2 keystone derivation.
3. **Neither lever should be re-fit** to patch its observable (the Δ_λ "no 7th ansatz" rule for binding;
   the c_k flip-flop guard for Q_β). The honest disposition for both is **near-match, gated on `M`.**

No fit; nothing wired; no tier change. This note is coordination only.
