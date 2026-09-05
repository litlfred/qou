# Deriving `S = Q_β/E₀` (Subgoal-2): the leading NZ channel decouples into two orthogonal sub-obstructions

> **Notation note.** This document predates the 2026-09-05 calibration rename and uses
> the superseded symbols `𝔇_β` (CAL-2) and/or `𝔇_π` (CAL-3). Those are now
> `P_skew^β` (the bar-skew β-channel) and `P_avg^π` (the bar-even π-channel); the
> `𝔇` family is reserved for genuine decay rates (`𝔇_n`, `𝔇_μ`, `𝔇_K` = ℏ/τ).
> The analysis below is left as the record of what was analysed at the time.

**Date:** 2026-08-01
**Axis:** Subgoal-2 substrate-derivation of the CAL-2 archimedean scalar
`S = Q_β/E₀` (the c₃ bar-odd swing / β-decay Q-value), off the fibre→observable
bridge verdict (PR #4520).
**Tier:** corpus-first synthesis + one formalize-first increment
(proved-lean bound). **No fit; no c_k value claimed; nothing wired; no tier
change.** scope-(a)/(b) classified throughout. "Sorry-free ≠ derived."

## One-line verdict

**OPEN — reduced, and the reduction is sharpened.** Deriving `S = Q_β/E₀`
from the substrate is Subgoal-2 (owner-declined 2026-05-08, **generally reversed
/ open-for-all 2026-07-11**; anti-fit still gates *how*). The corpus had already
reduced it to a single open sub-obstruction — the substrate meridian-deformation
map `u(q₀)` of the SDeformedVolumeChannel keystone. This pass adds a
**proved-lean upper bound** that splits that single piece into **two orthogonal**
sub-obstructions and shows the "derive the spin part" framing is **incomplete**:
the spin part can supply the proton *sign flip* but is **provably unable** to
supply the muon *magnitude* at leading order. **Not derived, not axiomatized,
not wired.**

---

## 1. What the corpus has already ESTABLISHED (independently re-verified here)

The corpus-grep checklist (`docs/audits/`, `content/`, `computations/`,
`docs/coordination/`) was run; the frontier below is grounded in existing
audits / Lean / probes and is **not** re-declared open.

**1a. Two distinct objects both called "S".** This is a live confusion trap:

| object | value | where | role |
|---|---|---|---|
| **gross ratio** `S = Q_β/E₀` | `S_p ≈ 908.4`, `S_μ ≈ 886.8` | `SRigidityPrune.lean`, heat-fmap §2 (#1752) | the **CAL-2 anchor** scalar; `Q_β = ℏ/𝔇_β` |
| **bar-odd complex-volume leak** `S = c₃ + Vol(4₁)` | `S_μ ≈ +0.00968298`, `S_p ≈ −0.03945936` | `sdeformed_channel_signflip_probe.py` L78 | the **c₃-projection** residual; the sign-flipping datum |

The task's `S = Q_β/E₀` is the **gross ratio**; the sign-flipping small `S` is
the c₃ leak. They are *not* the same number. The gross-ratio sign is controlled
by the closed-form factor `(q₀²−2q₀−1)` (cheat-sheet
`Q_β = m_e·|q₀²−2q₀−1|(q₀+1)/(2q₀³)`): `q₀²−2q₀−1 ≈ −1.9879` at both anchors,
far from its zero at the silver ratio `q₀ = 1+√2 ≈ 2.4142` — so the **gross Q_β
does NOT change sign near the substrate**. The measured sign flip lives entirely
in the c₃ complex-volume leak, not in the gross closed form. (Numeric check in
the companion probe.)

**1b. The rigidity prune (proved-lean, scope-(b)).**
[`SRigidityPrune.no_anchor_invariant_realizes_swing`](../../content/quantum-observable-universe/lean/QOU/QBeta/SRigidityPrune.lean)
(sorry-free): `S` is **not** a pure function of any anchor-invariant datum, which
**excludes** every fixed CAL constant (`𝔇_β, 𝔇_π, m_π`) and every classical
topological invariant, and **forces** the anchor-dependent **quantum** complex
volume `𝔙_q(K)`. `S_bar_odd_of_ratio` records `σ S = −S` (CAL-2 / 𝔇_β).

**1c. The concrete channel object (proved-lean).**
[`FigureEightComplexVolume.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/FigureEightComplexVolume.lean)
(T1, bean `qou-6s8k`, sorry-free) realizes the abstract keystone field `V` as the
leading Neumann–Zagier form of the figure-eight (lepton knot):
`𝔙₄₁(u) = Vol(4₁) + i·(√3/4)·u²`, from the **rigorous A-polynomial** cusp modulus
`τ = −i√3` (purely imaginary, ℚ(√−3)) — anti-fit, not tuned to any `S`. Hence
`Im 𝔙₄₁(u) = κ(Re²u − Im²u)`, `κ = √3/4`, a harmonic quadratic form vanishing on
the diagonals `|Re u| = |Im u|`.

**1d. Sign-flip → diagonal-crossing (proved-lean).** `imV₄₁_pos_iff`,
`imV₄₁_neg_iff`, `signflip_forces_diagonal_cross`, `f3_re_linear_same_sign`
(T2, bean `qou-fook`): the measured `S(μ) > 0 > S(p)` forces `u(q₀)` to cross the
diagonal between anchors; the #3773 F3 family is scope-(b) refuted.

**1e. The real-boost part of `u(q₀)` is DERIVED (sorry-free).**
`braids-and-knots/meridian-holonomy-boost.md` (bean `qou-zuk4`): the cusp-torus
meridian holonomy *is* multiplication by `q₀` = a hyperbolic **boost** of rapidity
`ln q₀` at real `q₀>1` (a compact **spin** only at `|q|=1`). So `Re u = ln q₀`
is geometrically fixed; probe `qbeta_geometric_boost_udeform_probe.py`:
- **[G1]** real boost ⇒ `Im 𝔙₄₁ = κ(ln q₀)² = +0.004714`, correct muon sign,
  "within ~0.49×" of `S_μ`;
- **[G2]** across-anchor `Δ(ln q₀) ≈ 1.2e-8` ⇒ nearly constant, so the real boost
  alone cannot make the proton sign flip;
- **[G3]** the sign flip = the **boost→spin transition** (the spin/imaginary part
  of `u(q₀)`), left **open**.

**Established frontier:** derive the **spin/imaginary part** of `u(q₀)` (the
boost→spin transition) that supplies the diagonal crossing. Everything else in
the channel is Lean sorry-free.

---

## 2. What THIS pass ADDS — the leading-order upper bound decouples the frontier

**Formalize-first.** State the invariant before the probe. Since `Im²u ≥ 0` and
`κ > 0`, the concrete leading form obeys a **hard upper bound**:

> `Im 𝔙₄₁(u) = κ(Re²u − Im²u) ≤ κ·(Re u)²`   for **every** `u` (any real `Im u`).

New Lean (this PR, `FigureEightComplexVolume.lean`, sorry-free):
- `imV₄₁_le_cuspModulus_reSq : (V₄₁ u).im ≤ cuspModulus * u.re ^ 2` — the bound;
- `imV₄₁_leading_unreachable_of_lt : cuspModulus * r ^ 2 < S → ∀ u, u.re = r →
  (V₄₁ u).im ≠ S` — its contrapositive: if the target exceeds the `Re`-capped
  bound, **no** `u` with that real part realizes it at leading order.

**Instantiate at the derived boost `Re u = ln q₀`** (§1e) — inputs are *derived*
(`Re u = ln q₀`, `imV₄₁ = κ(Re²−Im²)`) and *measured* (`S_μ, S_p`); **nothing is
inverted to match `S`** (I compute a bound and compare):

| anchor | `κ·(Re u)²` (leading cap) | `S` target | `S / cap` | leading-order reachable? |
|---|---|---|---|---|
| **muon** | `+0.0047142` | `+0.0096830` | **2.054×** | **NO** — needs `Im²u = −0.01147 < 0` |
| **proton** | `+0.0047142` | `−0.0394594` | (sign) | YES — `Im²u = +0.10201 > 0` (spin exists) |

**The decoupling (the contribution).** The single open sub-obstruction "derive
`u(q₀)`" splits into two **orthogonal** pieces:

1. **Proton SIGN FLIP ← the spin/imaginary part of `u(q₀)`.** A real `Im u` with
   `Im²u = 0.102` reproduces `S_p < 0` (diagonal crossed, spin ON). This is the
   already-named open piece (boost→spin transition, `qou-zuk4`/`qou-fook`) and it
   is genuinely realizable at leading order.

2. **Muon MAGNITUDE ← NOT the spin part** (scope-(a), *newly sharpened*, proved
   bound). `S_μ = 2.054 × κ(ln q₀)²` **exceeds the leading cap**. Because the
   spin part only *decreases* `Im 𝔙₄₁` below `κ·Re²u`, **no** real `Im u` can
   reach `S_μ` at leading order. The muon deficit must therefore be closed by a
   real `Re u` larger than the pure boost `ln q₀`. It **cannot** be the spin part.

> **Convergence with sibling PR #4515 / #4508 (independent, sharper).** While
> this pass was in flight, sibling
> [`claude/c3-exact-volume-boost-enhancement-2026-08-01`](https://github.com/litlfred/qou/pull/4515)
> reached the same `A ≈ 2.05` gap from the **exact** figure-eight CS integral and
> sharpened it: (i) it independently states "the spin part only *decreases*
> `Im 𝔙₄₁`" — exactly the content of this pass's Lean bound
> `imV₄₁_le_cuspModulus_reSq`, which now supplies the **sorry-free formalization**
> of that numerical assertion; and (ii) via #4508 (radius of convergence
> `0.96 ≫ u = 0.104`) it shows the even `O(u⁴)` NZ tail is **negligible**, so the
> deficit is **unambiguously** a `Re u` boost-rapidity enhancement — the "O(u⁴)
> tail" alternative this pass initially offered is **excluded** by #4508. The
> muon magnitude reduces to a single derived `O(1)` factor
> `c = √A ≈ 1.4305 ln q₀` (why is the effective boost rapidity `√2.05·ln q₀`, not
> the meridian rapidity `ln q₀`?) — to be *derived*, not fit.

This refines the frontier: the "derive the spin part" program (`qou-fook`) is
necessary for the proton *sign* but **structurally cannot** supply the muon
*magnitude* (proved: spin only decreases `Im 𝔙₄₁`). The muon magnitude is the
orthogonal sub-obstruction — the boost-rapidity factor `c = √A ≈ 1.43` (#4515),
which the prior single-piece "derive `u(q₀)`" framing masked.

### 2a. Scope discipline

- **scope-(a), not (b).** The bound does *not* exclude the channel identity
  `S = Im 𝔙_q` — the full quantum complex volume carries the even `O(u⁴)` tail
  the leading form drops. It is a **magnitude insufficiency of the leading form**
  under the derived boost, citing the invariant `Im²u ≥ 0, κ > 0`. The honest
  phrasing: *the leading NZ term of `𝔙₄₁`, alone, at `Re u = ln q₀`, cannot
  reproduce `|S_μ|` for any real spin.*
- **Not a derivation of `S`.** `Q_β = ℏ/𝔇_β` is a CAL-2 input; identifying `S`
  with `Im 𝔙_q(u(q₀))` would *identify* it, not *derive* it around the
  calibration. The genuinely open pieces stay open and beaned; nothing is
  axiomatized.
- **Anti-fit.** No coefficient chosen to match `S`; `κ = √3/4` and `Re u = ln q₀`
  are both derived (A-polynomial cusp modulus; meridian-holonomy boost). `S_μ, S_p`
  are cited measurements.

---

## 3. Honest verdict

- **Derived?** No. `S = Q_β/E₀` remains a CAL-2 input; Subgoal-2 open.
- **Reduced?** Yes, and sharpened. The reduction is now: the leading-order
  SDeformedVolume channel is **magnitude-insufficient** for the muon; closing
  `S` needs BOTH (1) the spin part (proton sign, open — `qou-fook`) AND (2) the
  boost-rapidity factor `c = √A ≈ 1.43 ln q₀` (muon magnitude, open — sibling
  #4515's survivor `qou-iyj5`; the O(u⁴)-tail alternative is excluded by #4508).
- **Wired?** No. Q_β stays c₂-only in production (honest ≈1279 ppb prediction);
  the guardrail (`docs/canonical-mass-formula-guardrail.md`) stands.

---

## Beans

- **`qou-fook`** (existing) — the spin/imaginary part of `u(q₀)` (boost→spin
  transition) that supplies the proton sign flip. Unchanged; still open.
- **`qou-iyj5`** (sibling #4515) — the muon-magnitude survivor: derive the
  boost-rapidity factor `c = √A ≈ 1.4305`, i.e. why the effective rapidity is
  `√2.05·ln q₀` not `ln q₀`. This pass's `imV₄₁_le_cuspModulus_reSq` is the
  sorry-free Lean backing for "spin only decreases `Im 𝔙₄₁`, so the deficit is a
  `Re u` enhancement." The `O(u⁴)`-tail alternative is excluded by #4508.
- **`qou-0pym`** (filed this pass, re-scoped) — records the decoupling +
  `imV₄₁_leading_unreachable_of_lt` bound; points at `qou-iyj5` for the derived
  `c`-factor. Anti-fit; falsifiable; open.

## Cross-references

- [`2026-08-01-fibre-to-observable-bridge-verdict.md`](2026-08-01-fibre-to-observable-bridge-verdict.md)
  (PR #4520) — the trigger; c₃-odd home Lean-forced, value CAL-2-anchored.
- Sibling [PR #4515](https://github.com/litlfred/qou/pull/4515) (survivor
  `qou-iyj5`) — exact figure-8 CS integral; the muon `A ≈ 2.05` gap is the
  boost-rapidity factor `c = √A ≈ 1.43`; O(u⁴) tail excluded by #4508. This
  pass's Lean bound is the sorry-free backing for its "spin only decreases
  `Im 𝔙₄₁`" step.
- [`2026-07-07-c3-even-solved-s-complex-volume-rigidity.md`](2026-07-07-c3-even-solved-s-complex-volume-rigidity.md)
  — c₃-even substrate-exact; the S rigidity prune.
- [`docs/coordination/keystone-sdeformedvolume-channel-attack.md`](../coordination/keystone-sdeformedvolume-channel-attack.md)
  — the SDeformedVolumeChannel campaign (T1/T2 + geometric-boost readout).
- Lean: [`FigureEightComplexVolume.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/FigureEightComplexVolume.lean)
  (new bound lemmas), [`SRigidityPrune.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SRigidityPrune.lean).
- Probe (this pass): `computations/probes/qbeta_sdeformed_leading_bound_probe.py`.
- Precision context: [`docs/precision-goals.md`](../precision-goals.md) §Subgoal-2;
  [`2026-07-11-subgoal2-owner-reversal-open-for-all.md`](2026-07-11-subgoal2-owner-reversal-open-for-all.md).

-- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-- Ref: [manuscript] docs/coordination/keystone-sdeformedvolume-channel-attack.md
