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

## Algebraic shadow: knot operators / inverse Gram (the carrier is the ghost mode)

Per [`thurston-relaxation.md`](../../content/quantum-observable-universe/brings-surface/thurston-relaxation.md)
the algebraic solver is the `ℤ[q^{±1/2}]`-shadow of the shape geometry. Probe
[`qbeta_c3_barodd_knot_operator_gram_probe.py`](../../computations/qbeta/qbeta_c3_barodd_knot_operator_gram_probe.py)
locates the bar-odd carrier at the H₃(q) level (all computed, no fit):

- `β(4₁) = nf(σ₀σ₁⁻¹σ₀σ₁⁻¹) = L₊ + HA·e⁻` in the NF basis (`HA = q−q⁻¹`).
- The **flip** `σ₀↔σ₁, L₊↔L₋` (`e⁻=σ₀σ₁σ₀` fixed by the braid relation) is the
  algebraic bar `σ`; its decay projection `½(β − flip β) = ½(L₊−L₋)`.
- The Frobenius/Gram form `G_{ij}=tr_M(b_i b_j)` is **indefinite**: signature
  `(5+,1−)`, `det G<0`. The **unique negative-norm (ghost) direction is
  `(L₊−L₋)/√2`** — and the decay projection lands on it **exactly**
  (`|cos|=1.0000`, Gram-norm² `= −0.4275 < 0`); the mass projection sits in the
  positive/unitary cone (`+1.11`).

So the bar-odd `S` carrier is pinned to a **single algebraic mode** — the Gram
ghost `(L₊−L₋)` — the concrete realization of `EkParitySplit.decayProj`.

## Physics intuition (knot–particle mapping) — a simplification lead

`e⁻ = σ₀σ₁σ₀ = T_{2,3}` (trefoil) **is the electron**
([`knot-notation-convention.md`](../../content/quantum-observable-universe/braids-and-knots/knot-notation-convention.md)).
So `β(4₁) = L₊ + HA·e⁻` reads **chirality + (bandwidth)·electron**, and:

- **Q_β is neutron β-decay** (`n→p+e⁻+ν̄`) — the maximally **parity-violating**
  weak process. Its `c₃` leak being **bar-ODD (parity-odd)** is then *required*,
  not incidental: the carrier is the parity-odd chirality mode `(L₊−L₋)`, and the
  operator carries an explicit `e⁻` (the emitted electron), weight `HA=q−q⁻¹`
  (itself bar-odd/sinh: `HA ↦ q⁻¹−q = −HA` under `σ`).
- **Amphichirality reconciliation:** `4₁` amphichiral ⇒ `J_{4₁}(q)` palindromic
  (bar-even at the *closed-knot* level, `CS=0`); the bar-odd content lives only
  in the *deformed/open* operator's ghost mode — consistent throughout.

**Simplification lead (parameter-free scale, phase still open):** guess the
meridian deformation magnitude `|u| = HA` (the electron's bar-odd weight). Then
the NZ form gives `(√3/2)HA² = 0.03785`, vs measured `|S(proton)| = 0.03946`
(~4%) and `|S(muon)| = 0.00968` — i.e. `|sin 2φ| = 1.04` (proton, ~1) and `0.26`
(muon). The **magnitude scale matches** with no free parameter (`√3` = cusp
shape, `HA` = electron weight); only the **phase `φ(q₀)`** (which carries the
sign-flip) remains the open `z(q₀)`. The slight `>1` for proton shows `|u|=HA`
is leading-order (higher NZ terms / exact branch tracking pending). **This is a
lead, not a closure — no `c_k` wired.**

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
