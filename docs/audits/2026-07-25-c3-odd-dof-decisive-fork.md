# c₃ DOF fork — DECISIVE: verdict (B), c₃ is a SEPARATE degree of freedom (not pinned by the determined even solve)

**Date:** 2026-07-25 · **Bean:** `qou-1dnr` (advances toward closure of the
"is c₃ pinned?" question) · **Branch:**
`claude/argument-principle-residue-sum-2026-07-20` · **Tier:** scope-(a)
structural resolution; no fit, no c_k wired, no tier change ·
**Follows:** [`2026-07-24-c3-barodd-fork-correction.md`](2026-07-24-c3-barodd-fork-correction.md)
(the over-claim correction this audit does NOT repeat).

## The question (from bean `qou-1dnr`)

Is the Q_β precision-ladder rung **c₃** genuinely a **separate degree of
freedom**, or is it **pinned** (exactly determined) by the determined ℚ(√3)
triangular solve on the derived net decay-width — the same solve behind
`c₂ = −1` and the exact `c_k^even`?

## Verdict: **(B) — c₃ is a SEPARATE DOF.**

Both independently were expected outcomes and both hold, exactly, over the ONE
determined net-route `log R` (symbolic GB-reduced `Δ(net)`, no CODATA, no fit).
Producer:
[`computations/qbeta/qbeta_c3_odd_dof_normalization_fork_probe.py`](../../computations/qbeta/qbeta_c3_odd_dof_normalization_fork_probe.py)
(witness `qbeta-c3-odd-dof-normalization-fork.witness.json`). Lean certificate:
[`QOU.Mass.QbetaC3OddDOF`](../../content/quantum-observable-universe/lean/QOU/Mass/QbetaC3OddDOF.lean)
(sorry-free).

## What changes at order 3 — the crux, two pillars

### Pillar 1 — leading rung is reparam-invariant; c₃ is not (the closed-factor / bar-weight fork)

`c₂ = −1` is not obtained from the s-series triangular solve at all. It is the
coefficient of the **closed finite N=2 correction factor**
`1 − b²ℏ_q⁴ = 1 − u²` (`u = b·ℏ_q²`; `QOU.QBeta.C2Structural`,
[`q-beta-c-2-eq-neg-one-structural.lean`](../../content/quantum-observable-universe/mass-theory/q-beta-c-2-eq-neg-one-structural.lean)):
a degree-2 polynomial in `u`, exact, **no subleading tail**. Its coefficient is
a genuine ring-identity structural invariant.

Equivalently — and this is the decisive, exactly-measured statement — `c₂` is
the **LEADING** ladder rung, pinned at `s⁴`, the leading order of `u²`. At that
order the bar-weight-2 variable `u` and the bar-even variable `ũ = q·u` **agree**
(`u₂ = ũ₂ = √3/2`; audit
[`2026-07-03-u-tilde-bar-weight-normalization.md`](2026-07-03-u-tilde-bar-weight-normalization.md)),
so the `c₂` extraction is **blind** to the `u → ũ` normalization. Measured over
the fixed net `log R`:

| rung | diff(`u`-conv, `ũ`-conv), exact ℚ(√3) | reparam-invariant? |
|---|---|---|
| **c₂** | **`0`** | **YES** (leading rung) |
| **c₃** | **`35/6 + 7343√3/216`** (`≈ 65.42`) | **NO** |
| c₄ | `−73021/48 − 4705√3/72` | NO |

`c₃` is the **first SUBLEADING** rung: pinning it at `s⁶` requires subtracting
the order-6 **tail** of the already-fixed `c₂` rung, `[u²]₆ = 2u₂u₄ + u₃²`.
That tail lives exactly where `u` (bar-weight 2) and `ũ` (bar-even) **diverge**,
so the extracted `c₃` inherits the `u`-vs-`ũ` ambiguity and **shifts by a
nonzero exact ℚ(√3) amount**. There is **no known closed N=3 factor** to make it
a presentation-invariant structural identity. Formalized as the exact identity

  `c₃(u) − c₃(ũ) = c₂ · (4u₃ + u₂) / u₂²`  (for `w = q`, i.e. `w₁ = 1, w₂ = 0`)

(`QbetaC3OddDOF.c3Of_reparam_shift_q`), with the general unit-reparam shift
`c₂·(4w₁u₃ + 2w₂u₂ + w₁²u₂)/u₂²` (`c3Of_reparam_shift`) and its non-vanishing
(`c3Of_reparam_shift_ne_zero`, `c2_pinned_c3_free`). The probe cross-checks the
`w = q` identity exactly.

**Reading:** a *canonical* / *Taylor-exact* c_k must be an invariant of the
observable, independent of arbitrary presentation choices. `c₂` is one; `c₃` is
not. Fixing `c₃` requires an **additional input** beyond the determined even
solve — that is the operational meaning of "separate DOF."

### Pillar 2 — the even-power ladder is BLIND to the bar-odd content c₃ must carry

With the even rungs `c₂..c₄` fixed, the single-variable ladder `∏(1+c_k u^k)`
leaves **every odd-order residual exactly nonzero** (`s³, s⁵, s⁷, s⁹` — exact
ℚ(√3), reproduced here and in the 9fnm table). The single-variable even-power
ladder simply **cannot see** odd information. The bar-odd content is the
**separate, exactly-determined companion** `h·D(ũ)` (`h = q − 1/q`,
`D = O/h = Σ d_k ũ^k`, `d₁..d₉ ∈ ℚ(√3)`; ai81/08ds). Its `d_k` are **not** the
observable rungs (`−1`, `−2`); mapping the companion to the observable `c₃^odd`
rung needs the `1/u³` **fibre f-map** (Reeb-`sinh`, parity-admissible only at
the fibre level — `qbeta_reeb_sinh_parity_probe.py`), i.e. the fibre-saddle
Stokes datum **`A_ω`** (`QOU.Mass.QbetaC3Stokes`, #3805).

## Consequence — A_ω is REQUIRED, not optional

Both pillars say the determined even-ladder solve does not, and structurally
cannot, pin `c₃`: (1) its value is not presentation-invariant and no closed N=3
factor exists; (2) the bar-odd content it must carry decouples into the fibre
companion. The non-invariance identity in `QbetaC3OddDOF` is the sorry-free
**algebraic certificate** that the sign+magnitude of `c₃` must come from the
fibre `A_ω` — consistent with, and sharpening, the 2026-07-24 correction (the
substrate Borel sum is anchor-blind; the observable datum lives on the fibre
branch).

## Honesty ledger

- **No fit.** Both channels are the determined ℚ(√3) solve on the symbolic
  GB-reduced `Δ(net)` (`free-neutron-decay.witness.json`); nothing tuned to
  Q_β/CODATA. c₃ was **not** inverted from CODATA.
- **No wiring / no tier change.** c₃ stays EMPIRICAL (registry §3); `c₂ = −1`
  canonical, unchanged. This audit does **not** derive c₃ — it proves c₃ is a
  separate DOF, a clean scope-(a) **negative**.
- **Scope discipline.** This is a **structural exclusion of "c₃ is a
  presentation-invariant pinned value"** — justified by a proved
  reparametrisation-invariance/shift identity (`QbetaC3OddDOF`), not a single
  numeric probe. It does **not** claim c₃ is unknowable: its value is fixed once
  the fibre `A_ω` datum is supplied.

## Files

- Probe: `computations/qbeta/qbeta_c3_odd_dof_normalization_fork_probe.py`
  (+ `qbeta-c3-odd-dof-normalization-fork.witness.json`)
- Lean: `content/quantum-observable-universe/lean/QOU/Mass/QbetaC3OddDOF.lean`
  (imported in `QOU.lean`)
