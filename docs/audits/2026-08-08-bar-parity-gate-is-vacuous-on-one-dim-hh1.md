# Bar-parity on a 1-dim HH¹ — independent corroboration of `qou-qb8b`, and a cost correction

**Bean:** `qou-jcmw` · **Tier:** exact symbolic (ℚ(i) + ℚ[x]/Φ₅) · **Wired:** nothing.

> ## 🛑 THIS RESULT IS NOT NEW — READ [`2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md`](2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md) FIRST
>
> Bean `qou-qb8b` established the same conclusion earlier the same day and
> **landed on `main` first**: the bar-parity of the HH¹ outer class acting on
> the cocenter is a choice of normalization, not an invariant, so the proposed
> prune cannot exist. That audit is the canonical statement. This document is
> an **independent re-derivation**, kept per AGENTS.md §"Parallel exploration"
> ("two independent confirmations of an open result are valuable") — not a
> discovery, and it must not be cited as one.
>
> **My corpus-grep failure.** I ran the checklist at session start and then
> claimed this result hours later without re-running it, against a corpus that
> had moved. That is the #1515 / #1532 / #1543 pattern, committed by the same
> session that quoted the rule two documents earlier. Recorded, not buried.

---

## 1. What the two derivations share

Both reach: with `dim_K HH¹ = 1`, `[D^bar] = μ·[D]` forces `μ·σ(μ) = 1`;
Hilbert 90 for `ℚ(ζ)/ℚ(ζ)⁺` makes `μ = ν/σ(ν)` always solvable; and since
`σ(a) = −a` for `a = ζ − ζ⁻¹`, rescaling by a bar-odd scalar flips the parity.
Both verify on `H₃` in exact cyclotomic arithmetic.

`qou-qb8b`'s version is **stronger** and should be the one cited:

- it runs **two** roots (`q = i`, `q = ζ₆`) and finds them on **opposite** raw
  parities (`λ = +1` vs `λ = −1`) — the asymmetry is itself the symptom, and it
  is more convincing than my single-point check;
- it exhibits the flip **constructively** at both points rather than resting on
  the theorem;
- it explains *why* the real-resolvent prune worked and this one cannot (over
  ℝ bar acts trivially, so parity is rigid; at a root of unity `ℚ(ζ)` contains
  bar-odd scalars for free) — the part genuinely worth carrying forward;
- it carries a successor (`qou-qb8d`) that runs the **pinned** test and finds
  the trace-paired number `S_x = tr_M(Δ(x))` is **MIXED with a nonzero bar-odd
  part** — a positive indication for the carrier that my work does not reach.

My contribution to this specific question is one more independent confirmation.
That has some value and no priority.

## 2. What this branch does add

Two things, neither of which is the parity result.

**(a) The dimension count at the actual Bring root.** `qou-qb8b`'s audit says
explicitly that `qou-jcmw` *"remains worth doing for its dimension count"*.
Done: **`dim HH¹(H₅(ζ₅)) = 1`**, with a semisimple control at generic `q`
giving 0, and the outer class acting with **rank 1 on the 7-dimensional
cocenter** — the `H₅` instance of the not-trace-blind mechanism `qou-qb8b`
established at `H₃`. See
[`2026-08-08-hh1-h5-bring-root-cocenter-action.md`](2026-08-08-hh1-h5-bring-root-cocenter-action.md).

**(b) A cost correction that reverses an operational recommendation.** That
audit's §"do not spend the H₅ computation on this" estimates `H₅` at *"dim 120
— 14 400 unknowns and ~1.7M Leibniz equations"* and treats the expense as a
reason to skip it. That estimate parametrizes a derivation by its **full
matrix** on the 120-dimensional algebra.

A derivation is determined by its values on the `n−1` **generators**, with the
defining relations as constraints. For `H₅` that is

```
4 x 120  =   480 unknowns          (not 14 400)
10 relations x 120 = 1 200 equations (not ~1.7M)
```

— a 1 200 × 480 modular rank, which runs in seconds. The saving is ~30× in
unknowns and ~1400× in equations.

So the cost argument for skipping `H₅` does not hold, and the dimension count
it deferred is cheap. That is the actionable part of this branch: **`H₅` at the
Bring root is not an expensive computation**, and neither is `H₆`/`H₇` if
wanted.

## 3. Correction to my own earlier framing in this branch

An earlier commit here reported a **Θ-even** result from a sign-twisted bar
over `F_p` and called the true bar-parity question "the decisive gate", with
the ℚ(ζ₅) computation as the next step. Given `qou-qb8b`, that framing was
already wrong when written: there is no gate, and the ℚ(ζ₅) step it proposed
had already been run by someone else. The `F_p` Θ-shadow work retains only its
narrow correct point — that bar does not act on a single finite-field
specialization — which `qou-qb8b` states more directly.

## 4. Net

- Bar-parity: **duplicated**, cite `qou-qb8b`.
- `dim HH¹(H₅(ζ₅)) = 1` and rank-1 cocenter action at the Bring root: **new**,
  and explicitly the piece `qou-qb8b` left open.
- `H₅` is cheap, not expensive: **new**, and it reverses a recommendation.
- c₃ and the Q_β derivation gap: **unchanged** by any of this.
