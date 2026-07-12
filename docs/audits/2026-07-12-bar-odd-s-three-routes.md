# The bar-odd S, three routes: κ̃₁(u) at the substrate meridian, the D(u) ladder scope, and the experimental Q_β budget

**Date:** 2026-07-12 · **Branch:** `claude/bar-odd-s-routes-byoiy8` (PR #3691) ·
**Axis:** Q_β c₃ bar-odd `S` (post-capstone) · **Tier:** numerical-derived
(deformed-rung extraction, theorem-grade regime) + error-propagation arithmetic ·
**Discipline:** no fit to QOU data; no c_k wired; no tier change; registry untouched.

## Setting

The wall-resolution capstone left `S = h·D(u)` (`h = q−1/q`) needing its exact
normalization by one of three routes — explicitly **without** a singular map, the
deformed volume conjecture, or a fit:

1. the exact ladder `D(u)` (even/odd-channel program) — internal/theory route;
2. the odd Ohtsuki invariants `κ_k(u)` **at the substrate meridian** — the
   state-integral route (#3654 derived the leading scale `i·t·κ₁ = 0.058` but at
   the complete structure `u=0`, hence anchor-blind; the open item it named was
   "κ₁(u) at the substrate meridian `u = 2 log q₀`");
3. a sharper experimental neutron `Q_β` (`dq*/dQ_β ≈ −0.539`, #3636).

This PR advances routes 2 and 3 and scopes route 1.

## Route 2 — the deformed rungs κ̃₁(u), κ̃₂(u) at the substrate meridian

**Probe:** [`qbeta_ohtsuki_deformed_meridian_rungs.py`](scripts/qbeta_ohtsuki_deformed_meridian_rungs.py)
(+ witness). Method: the **exact deformed Habiro sum**

  `J_N(4₁; e^{ξ/N}) = Σ_k ∏_{j≤k} (2cosh u − 2cosh(ξj/N))`,  `ξ = u + 2πi`,

whose term reduces at `u=0` to `4sin²(πj/N)` — the merged u=0 extractor's term
(#3628) — so this is that extractor's direct generalization. For 4₁ and real
`0 < u < log((3+√5)/2) ≈ 0.9624` the asymptotic template
`log J_N = α(u)N + ½log N + γ(u) + Σ κ̃_n(u)/N^n` is **H. Murakami's theorem**
(J. Topology 6 (2013), arXiv:1203.5622) — *no deformed-volume-conjecture
assumption*; the substrate meridian `u = 2 ln q₀ ≈ 0.2087` sits well inside.

Extraction and its two branch-safe channels, plus validations (V1–V6: u=0
reproduces the exact `κ₁ = 11√3π/108`; free-fit `β = 0.500000000015`; 12-digit
ladder self-consistency; geometry cross-check below; anchor-blindness; adaptive
precision headroom — the deformed-saddle cancellation costs `~u^{1.9}·N` digits,
measured and handled) are documented in the probe header.

**Results (substrate meridian, proton pin; muon pin identical to 7.9e-9):**

| quantity | value | remark |
|---|---|---|
| `κ₁(0)` | 0.5542164724 (exact `11√3π/108`) | u=0 reference (#3606) |
| `Re κ̃₁(u_sub)` | **0.587343387311** (12 digits) | +5.98% from `κ₁(0)` — smooth |
| `Im κ̃₁(u_sub)` | **−0.0195072496** | intrinsic odd channel: `u≠0` breaks `J_N` reality — a **new derived bar-odd-channel datum** |
| finite-b lead `t·Re κ̃₁` | **0.061284** | deformed version of #3654's `i·t·κ₁ = 0.0578` scale |
| `dκ̃₁/du` (grid) | 0.12…0.45 | smooth O(1) — no wall, capstone-consistent |
| anchor split | 7.9e-9 | κ̃₁ is anchor-blind: sign-flip stays representational (#3636) |

Comparisons against the two S targets (`S(muon)=+0.00968`, `S(proton)=−0.03946`):
`t·Re κ̃₁` sits at 6.3× / −1.55× of S; `Im κ̃₁` at −2.01× / +0.49×. These are
**scale statements only** — the state-integral b-dictionary normalization for the
deformed case is not pinned here, and κ̃₁'s anchor-blindness means neither term
alone can carry the sign flip (consistent with the capstone: the flip lives in the
`1/u³` ladder representation, not in the geometry).

**Bonus structural finding (from validation V4).** The growth rate `Re α(u)`
minus the pure-volume prediction `2π·Vol(u)/(u²+4π²)` (with `Vol(u)` from the
corpus's validated gluing-Newton solve) decomposes as

  `resid(u) = (1/2)·u + b·u² + O(u³)`,  `b ≈ 0.1723`,

with the linear coefficient hitting `1/2` to ~4 digits across the whole grid —
i.e. `Im S(u) ⊃ π·u`, a framing/meridian normalization term that is **odd under
`u ↦ −u`** (bar-odd). The `b·u²` coefficient is left unidentified (it mixes the
Im-S quadratic with a possible Re-S linear term; identifying it would need the
Im-side of α, which the mod-2π branch structure hides from a doubling ladder).

**What route 2 still needs:** κ̃₃(u) (the next odd rung — the ladder currently
resolves κ̃₁ to 12 digits and κ̃₂ roughly; κ̃₃ needs either a taller ladder at
~450+ dps or the state-integral saddle expansion), and the deformed b-dictionary
normalization (which #3596's Φ_b construction supplies once its saddle expansion
is pushed to 2-loop at `m = q₀`).

## Route 3 — the experimental Q_β budget (quantified)

**Probe:** [`qbeta_qstar_experimental_budget.py`](scripts/qbeta_qstar_experimental_budget.py)
(+ witness). Pure error propagation on committed values (CAL-3
`Q_β = 0.78233341(61) MeV`; `dq*/dQ_β = −0.5389653` and `q*` from the merged
#3636 witness; pins from `qou_substrate.constants`):

| threshold | needs σ(Q_β) | improvement over 0.61 eV |
|---|---|---|
| σ(q*) today | — | **296 ppb** (25.7× coarser than the 11.5-ppb μ–p pin spread) |
| q* arbitrates the μ–p tension | **0.024 eV** | **~26×** |
| q* competitive with the muon pin (22 ppb) | 0.045 eV | ~13.5× |
| q* competitive with the proton pin (0.06 ppb) | 0.12 meV | ~4900× (beyond current technique) |

This is #3636's falsifiable lever made quantitative: a next-generation neutron
`Q_β` (or `Δ_np`) measurement at the few-hundredths-of-an-eV level would let the
decay sector **independently arbitrate** the μ–p substrate tension.

## Route 1 — exact D(u) ladder (scoped, not attempted)

The bar-split witness (`qbeta-even-channel-bar-split`) has `D₁…D₅` exact in
ℚ(√3) but the two-variable hypothesis `log R = E(ũ) + h·D(ũ)`, `ũ = q·u`, fails
exactly at order 11. Extending the exact ladder and re-attacking the order-11
residual is queued (bean `qou-gmm6`) — kept out of this PR for reviewability.

## Honest scope (anti-laundering)

Everything in route 2 is a **4₁ topological/asymptotic fact at a deformed
meridian** (theorem-grade regime); route 3 is arithmetic on committed
experimental inputs. Nothing closes `S`, wires a `c_k`, or changes any tier.
The near-integer ratios in the comparison table (e.g. `Im κ̃₁/S(proton) ≈ 0.49`)
are reported as data, **not** identified — cross-anchor swing of `S` against an
anchor-blind κ̃₁ forbids any single-term identification.

## Cross-references

- Capstone + routes framing: [`2026-07-12-c3-wall-resolution-capstone.md`](2026-07-12-c3-wall-resolution-capstone.md)
- u=0 exact rungs: [`2026-07-12-ohtsuki-higher-rungs-exact.md`](2026-07-12-ohtsuki-higher-rungs-exact.md) (#3628)
- finite-b mechanism `2πb² = i·t`: `qbeta_c3_phib_finite_b_volume_correction_probe.py` (#3654)
- `1/u³` artifact + `dq*/dQ_β`: [`2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md`](2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md) (#3636)
- Growth-class obstruction (why the bridge is resummation, not term-matching): [`2026-07-12-fmap-4one-qbeta-bridge-growth-obstruction.md`](2026-07-12-fmap-4one-qbeta-bridge-growth-obstruction.md)
