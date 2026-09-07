# Closed form for the substrate landmark q* / c₃(q)? — Route B (Habiro / dilog)

> **Notation note.** This document predates the 2026-09-05 calibration rename and uses
> the superseded symbols `𝔇_β` (CAL-2) and/or `𝔇_π` (CAL-3). Those are now
> `P_skew^β` (the bar-skew β-channel) and `P_avg^π` (the bar-even π-channel); the
> `𝔇` family is reserved for genuine decay rates (`𝔇_n`, `𝔇_μ`, `𝔇_K` = ℏ/τ).
> The analysis below is left as the record of what was analysed at the time.

**Date:** 2026-08-01
**Status:** CANONICAL for the "is q* a closed-form constant?" question.
**Branch / PR:** `claude/qstar-closed-form-habiro-dilog-2026-08-01` (PR #4483)
**Compute:** [`qbeta_qstar_closed_form_dilog_probe.py`](../../computations/qbeta/qbeta_qstar_closed_form_dilog_probe.py) → `qbeta-qstar-closed-form-dilog.witness.json`
**Lean:** [`QBetaQStarClosedFormExclusion.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaQStarClosedFormExclusion.lean)

---

## The question

The substrate landmark `q*` is the **S-channel zero**:

$$S(q) := c_3^{\text{target}}(q, Q_{\text{codata}}, m_e) + \mathrm{Vol}(4_1), \qquad
\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3),$$

with `q*` the root of `S`, i.e. `c₃(q*) = −Vol(4₁)` exactly (the pure
bar-even / ε = 0 substrate point). Numerically

$$q^* = 1.109978593031523288402328\ldots$$

**Is `q*` — or `c₃(q)` as a function — expressible in a _forced_ closed
form (dilog / Habiro / Faddeev / cyclotomic), rather than only as a
numerical transcendental root?**

This is Route B. It is distinct from the earlier scope-(a) probes
(#3600 / #3636 / #3821), which asked whether _more anchors_ or a _longer
D-ladder_ sharpen `q*` (answer: no — `q*` is experiment-limited). Route B
asks the **closed-form** question directly, by separating the symbolic
shape from the experimental anchor.

**Builds on** the merged Bring-embedding magnitude audit
([`2026-08-01-bring-embedding-magnitude.md`](2026-08-01-bring-embedding-magnitude.md),
PR #4473), which records the same landmark `q* = 1.109978593031523288…`
and the key fact that `S(q) = c₃-target(q) + Vol(4₁)` is _the same function_
at both anchors (the magnitude `|S_p/S_m|` is an anchor-offset ratio, not a
Bring period). This PR closes the complementary question — whether the
_landmark itself_ is a closed-form constant — with the same `S`.

## Result — honest NEGATIVE with a positive sub-result

### P1 (positive, partial) — the S-channel-zero condition IS a closed-form equation

Clearing denominators in `c₃(q*) = −Vol(4₁)` (with `c₂ = −1`
Lean-proved) gives the **closed-form defining equation**

$$\boxed{\;\Phi(q^*) = \dfrac{Q_{\text{codata}}}{m_e}\;}$$

where

$$\Phi(q) = \frac{|q^2 - 2q - 1|\,(q+1)}{2q^3}
\cdot \cos\!\Big(\alpha(q) - \tfrac{b(q)\,\hbar_q(q)^2}{2}\Big)
\cdot (1 - u(q)^2)\cdot\big(1 - \mathrm{Vol}(4_1)\,u(q)^3\big),$$

with the substrate quantities `h = q − 1/q`, `ℏ_q = (q−1)/q`,
`b = √((h²+3)/(h²+4))`, `u = b·ℏ_q²`, `z = 1/(√q + 1/√q)`,
`α = (z−1)·h/2` (all rational · √). The first factor is `Q_A/m_e`.

`Φ(q)` is **fully elementary in q** (rational functions, one square
root, one cosine). The _only_ transcendental special-function constant
in the whole construction is

$$\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) = 2\,\mathrm{Im}\,\mathrm{Li}_2\!\big(e^{i\pi/3}\big),$$

the figure-eight-knot hyperbolic volume — a **Bloch–Wigner dilog value**.
It appears as the _target constant_ `−Vol(4₁)` that `c₃` must hit, not in
the q-dependence of `c₃`. **No Faddeev / Habiro q-series is needed** to
write either `c₃(q)` or `q*`'s defining equation in closed form.

Verification (`qbeta-qstar-closed-form-dilog.witness.json`, 70 dps):

| check | result |
|---|---|
| `Vol(4₁)` via `2·Cl₂(π/3)` vs `2·Im Li₂(e^{iπ/3})` | identical to `< 10⁻⁴⁰` (dilog identity) |
| root of `Φ(q) = Q_codata/m_e` vs root of `S(q) = 0` | `|Δ| = 2.4·10⁻⁷²` (recast is exact) |
| recast `q*` vs committed k=31 value | `|Δ| = 3.4·10⁻²⁵` (findroot floor) |

### N1 (negative, **scope-(b) structural exclusion**) — q* is NOT an experiment-independent constant

The right-hand side `R := Q_codata/m_e` is a ratio of **two
experimentally measured CODATA inputs**:

- `Q_codata = 0.78233341(61) MeV` — the measured neutron β-decay
  Q-value (`cal-3-q-beta.witness.json`; the CAL-2 proxy 𝔇_β),
- `m_e = 0.51099895069(15) MeV` — the CODATA-2022 electron mass (CAL-1).

`q* = Φ⁻¹(R)`. The **invariant** that forbids a pure closed form:

$$\Phi'(q^*) = -3.63094\ldots \neq 0,\qquad
\frac{dq^*}{dQ_\beta} = \frac{1}{m_e\,\Phi'(q^*)} = -0.5389652956\ldots \neq 0,$$

verified to match the direct `findroot` derivative and the committed
`−0.5389653` (#3636) with residual `0` at 70 dps. `Φ'` is sign-definite
on a neighbourhood of `q*` (checked at `±10⁻⁸, ±10⁻⁶`), so `Φ` is
strictly monotone there.

A mathematical constant is by definition independent of any experimental
input. `q*` is a **strictly monotone (hence non-constant) function of the
measured anchor** `R`. Therefore `q*` cannot be an experiment-independent
closed-form (dilog/Habiro/cyclotomic) constant. Concretely, `q*` is known
only to the precision of the neutron `Q_β` measurement: within
`σ(Q_β) = 6.1·10⁻⁷ MeV`, `q*` moves by `±3.3·10⁻⁷` — so only its first
~7 digits are experimentally determined, the rest are `Q_codata`-set
noise. **A more precise neutron `Q_β` measurement directly sharpens `q*`**
— the falsifiable lever (confirming and re-deriving #3636 from the
closed-form side).

**Scope classification.** This is a genuine **scope-(b)** structural
exclusion for the specific claim _"q\* is an experiment-independent
closed-form mathematical constant"_, with the invariant cited
(`Φ'(q*) ≠ 0`, sign-definite ⇒ strict monotone dependence on the measured
anchor). It is **not** a scope-(b) claim about the shape `Φ`, which _is_
closed form (P1, the positive partial). The earlier scope-(a) findings
("more anchors / longer ladder don't help") stand unchanged; this PR adds
the closed-form-side reason.

### N2 (anti-fit) — R is not itself a forced closed constant

`R = Q_codata/m_e = 1.53098829057…`. A NEGATIVE check (not a search)
against a few natural constants, reported in full per the anti-fit
discipline (the dense-fit resource [D4] is FORBIDDEN as evidence):

| candidate | `|R − c|/R` |
|---|---|
| `2·Cl₂(π/3)` (= Vol(4₁)) | 0.326 |
| `Cl₂(π/3)` | 0.337 |
| `π/2` | 0.026 |
| `3/2` | 0.020 |
| `ζ(2) = π²/6` | 0.074 |
| golden `φ` | 0.057 |

No candidate matches better than `~2·10⁻²`. `R` is a ratio of two
independent measurements with no structural reason to be a closed
constant; any closer match would be [D4] numerology and is rejected.

## Why the dilog / Habiro layer does not rescue a symbolic q*

The framework's Habiro-element program (parallel to the α_EM
`[2]_q·(1−h²α)` closure, PR #1511) aims to make the `c_k` Taylor
coefficients **q₀-independent (Taylor-exact) in the FIBRE** — see the
`Im(q)` fibre-vs-observable banner in AGENTS.md. That is a genuine open
target, but it is **orthogonal** to the present question:

- The Habiro element concerns the _q-series structure of `c_k`_ (making
  the near-match `c_3 ≈ −2` an exact fibre coefficient), not the _value
  of the anchor_ `R = Q_codata/m_e` that `Φ` must equal at `q*`.
- Even with a fully Taylor-exact Habiro `c_k(q)`, `q*` is still defined by
  `[Habiro-exact Φ](q*) = Q_codata/m_e`, whose RHS remains a measured
  ratio. The shape becomes "more canonical"; the anchor stays experimental.

So the dilog only ever enters as the _target constant_ `Vol(4₁)`, and the
Habiro program can at most upgrade the _shape_ `Φ` — neither makes `q*` a
Q_codata-independent dilog-root.

## Lean

[`QBetaQStarClosedFormExclusion.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaQStarClosedFormExclusion.lean):

- `qstarShape (vol41 q : ℝ)` — the explicit closed form `Φ` (documents
  P1: the shape is elementary; `vol41` carried as the external dilog
  constant).
- `qstarRootStrictMonoInAnchor` — sorry-free: `StrictMonoOn Φ I` ⇒ the
  root strictly tracks the anchor (the scope-(b) exclusion invariant's
  consequence).
- `qstarRootUniqueInAnchor` — sorry-free: the landmark is uniquely
  determined by the anchor (via `StrictMonoOn.injOn`).

Per **conditional-proved ≠ premise-established**: `StrictMonoOn Φ I` is the
numerically-verified _hypothesis_ (`Φ'(q*) ≠ 0`, sign-definite, 50 dps);
Lean proves the _implication_, not the monotonicity premise.

## Bottom line

- **c₃(q) as a function:** closed form — but trivially so (elementary in
  `q`, scaled by the experimental `R`); it needs no dilog/Habiro layer,
  and being closed-form-in-`q` is not the interesting "Taylor-exact/Habiro"
  sense.
- **q\* as a mathematical constant:** **NO** forced closed form. It is
  `Φ⁻¹(Q_codata/m_e)` — a closed-form function of a _measured_ ratio, with
  proven-nonzero sensitivity. Scope-(b) excluded from being an
  experiment-independent dilog/Habiro/cyclotomic constant.
- The sole dilog is the _target_ constant `Vol(4₁) = 2 Im Li₂(e^{iπ/3})`;
  the Habiro program is orthogonal to symbolizing `q*`.

This is the expected and acceptable honest negative: `Q_codata` is a
measured input, so a fully-symbolic `q*` is structurally impossible.

## Cross-references

- Prior scope-(a) q* probes: `qbeta_c3_imq_qstar_ladder_amplification_probe.py`
  (#3600/#3636), `qbeta-c3-qstar-k31-repin.witness.json` (#3821).
- Extractor: [`qbeta_utils.py::c3_target_at`](../../computations/qbeta/qbeta_utils.py).
- c_k truncation-order framing: [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).
- Habiro-element keystone: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
