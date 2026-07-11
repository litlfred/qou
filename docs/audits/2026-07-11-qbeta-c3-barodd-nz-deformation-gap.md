# c₃ bar-odd S: the NZ deformation gap — algebra closes, the observable does not

**Date:** 2026-07-11 · **Axis:** Q_β c₃ (bar-odd `S`) · **Branch:**
`claude/faddeev-phi-b-construction-e26myp` · **Tier:** structural + falsifiable
(scope-(a)). **No c_k wired; C14 anti-fitting; registry untouched.**
**Probe:** [`qbeta_c3_barodd_nz_deformation_probe.py`](../../computations/qbeta/qbeta_c3_barodd_nz_deformation_probe.py).

## What this session closed vs. what remains open (honest boundary)

Following the owner's combinatorial route and the `e_k(q̄,…)` correction, the c₃
bar-odd `S` reduces to a **single** open link. The rest is closed:

| layer | status | artifact |
|---|---|---|
| **Algebra** — `S = decay projection ½[e_k(q,q³,…)−e_k(q⁻¹,q⁻³,…)]`, bar-odd, nonzero | **closed** (sorry-free) | Lean `QOU.QBeta` `EkParitySplit.lean` (`massProj`/`decayProj`, `sigma_decayProj`, `decayProj_eq_zero_iff`, `decayProj_ne_zero_iff`) |
| **Object** — Faddeev `Φ_b` (modular double, sinh kernel, self-dual) | **built + validated** | `phi_b_evaluator.py` (vs Hikami math/0604094) |
| **Geometry** — `S` = bar-odd projection of the **4₁ deformation phase** | **framed** | this probe: `Vol(4₁)=2Λ(π/3)`, `CS(4₁)=0` |
| **Observable** — the two `S`-values from a *derived* `z(q₀)` | **OPEN (single link)** | the `z→c_k` evaluation map (PR #3458) |

## The geometry (why S is a deformation phase)

- `Vol(4₁) = 2·D(e^{iπ/3}) = 2Λ(π/3) = 2.02988…` (Bloch–Wigner; computed). This
  is the **bar-even** part of c₃ (`−Vol(4₁)`), already solved.
- **4₁ is amphichiral ⇒ `CS(4₁)=0`** at the complete structure (`log|e^{iπ/3}|=0`).
  So the bar-odd `S` is **not** the knot's own Chern–Simons — it is a
  **deformation phase** induced by the substrate `q₀` sitting off the complete
  point. Neumann–Zagier: `CVol(u)=CVol(0)−(τ/4)u²+O(u³)`, cusp modulus `τ ∝ √−3`
  (the `π/3` angle of `Vol(4₁)=2Λ(π/3)` — corpus-structural, not fitted).

## The falsifiable finding (no fit): a smooth deformation cannot close S

If `S(q₀)=Im[−(τ/4)u(q₀)²]` with a **smooth real-scaling** `u(q₀)` (natural
candidate `u ∝ log q₀`), then `S(proton)/S(muon)=(u_p/u_m)²`. The anchors differ
at `~10⁻⁸`, so:

| quantity | value |
|---|---|
| `(u_p/u_m)²` (smooth `u∝log q₀`) | `0.9999998` |
| measured `S(proton)/S(muon)` | `−4.0751` |

A smooth real deformation gives ratio `≈1`, **never** `−4.08` (let alone the sign
flip). This **rules out (scope-(a))** the smooth-deformation route and confirms
the variation is a **phase-channel** quantity: `u(q₀)` carries an
anchor-dependent phase with a **root-of-unity accumulation** near `q₀`
(consistent with `dc₃/dq≈4.66×10⁶`, the PR #1821 magnitude wall, and the
channel-separation spec). This is exactly the `z→c_k` evaluation map.

## Disposition

The derivation gap is **sharpened, not closed**: closing `S` ⟺ deriving the
complex meridian deformation `u(q₀)` (the evaluation map, PR #3458). The NZ
picture explains *why* the smooth route fails — the sign-flip lives in the phase
channel. Per the corpus discipline this is **scope-(a)** (a smooth-deformation
route excluded via a proved ratio invariant; the *ingredient* `Φ_b` is untouched
and remains the carrier) — **not** a `(b)` structural exclusion of the program.

## Cross-references
- Reduction: [`docs/scope/2026-07-11-qbeta-c3-barodd-tetraplectic-combinatorial-reduction.md`](../scope/2026-07-11-qbeta-c3-barodd-tetraplectic-combinatorial-reduction.md)
- Target: [`2026-07-11-qbeta-c3-barodd-sleak-phib-target.md`](2026-07-11-qbeta-c3-barodd-sleak-phib-target.md)
- Channel: [`2026-07-07-qbeta-fmap-phi-b-channel-separation-spec.md`](../scope/2026-07-07-qbeta-fmap-phi-b-channel-separation-spec.md)
- AGENTS.md §"Im(q) at fibre vs observable level"; §"Before declaring refuted (a)/(b)".
