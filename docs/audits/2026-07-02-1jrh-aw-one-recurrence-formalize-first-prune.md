# 1jrh — Askey–Wilson "one recurrence, two parities" test: formalize-first prune

**Date:** 2026-07-02
**Bean:** `1jrh` — *"test (binding, Q_β) satisfy one Askey–Wilson 3-term recurrence (`recurrence_invol_descent`)"*
**Origin:** the "genuine next probe" of
[`2026-06-30-complex-volume-bar-parity-binding-probe.md`](2026-06-30-complex-volume-bar-parity-binding-probe.md)
(the bar-parity projection test refuted the *simple* parity explanation; the
holomorphic tie the conjecture actually asserts is the `recurrence_invol_descent`
c_k-ladder: one three-term recurrence with a bar-even multiplier yielding *both*
the binding and Q_β ladders).
**Verdict:** **GATED — the test is under-determined with the currently measured
rungs; running it now would be a fit (Δ_λ-gate forbidden). The decisive
experiment is pinned below and becomes one line of arithmetic once the missing
rung exists.**

## The hypothesis, made precise

`conj:binding-qbeta-complex-volume` (holomorphic tie): there is **one** complex
ladder `C_k` satisfying a single three-term recurrence

$$C_{k+1} = A_k\,C_k + B_k\,C_{k-1},\qquad A_k \text{ bar-even } (A_k(q)=A_k(q^{-1})),$$

whose two parities are the **binding** (bar-even/Re) and **Q_β** (bar-odd/Im)
ladders. In the Askey–Wilson form, `A_k, B_k` are the standard AW
recurrence coefficients — rational in `q₀^k` with parameter set `(a,b,c,d)` at
fixed `q = q₀`.

**The structural content** (what makes this falsifiable at all): if both parity
ladders solve the *same* linear recurrence, they are two elements of its
2-dimensional solution space, so their **Casoratian** (discrete Wronskian)

$$W_k \;=\; c^{\mathrm{even}}_k\,c^{\mathrm{odd}}_{k+1} - c^{\mathrm{even}}_{k+1}\,c^{\mathrm{odd}}_k$$

must satisfy `W_{k+1} = -B_{k+1} W_k` — with `B_k` in the AW form, whose
positivity structure (λ_k > 0 for the positive-definite AW weight in the
compact regime) forces a definite **sign pattern** on successive `W_k`. That
sign pattern is parameter-free — it is the invariant a wide search would
otherwise chase numerically.

## What is measured today (tiered, per the c_k discipline)

| rung | bar-odd (Q_β) | tier | bar-even (binding) | tier |
|---|---|---|---|---|
| c₁ | 0 | proved (ladder seed) | — | — |
| c₂ | −1 | **proved Taylor-exact** | ≈ −8.0 | net-route (Hoefsmit Stage-B) |
| c₃ | ≈ −2 | near-match (cross-anchor swing ≤3.47%) | **not measured** | — |
| c₄ | ≈ −0.97 | CAL-anchored (NOT derived) | not measured | — |

## Degrees-of-freedom count (the prune)

- AW parameters: **4** (`a,b,c,d`; `q = q₀` fixed).
- Usable recurrence constraints from the odd ladder (seeds `c₁=0, c₂=−1`):
  `c₃ = A₂·c₂ ⇒ A₂ = 2`, and `c₄ = A₃·c₃ + B₃·c₂` — **2 equations**, of which
  one uses the CAL-anchored (untrusted-tier) c₄.
- Even-ladder constraints: **0** — a single rung (c₂ ≈ −8) cannot constrain a
  recurrence; the Casoratian test at k=2 requires `c₃^even`, which does not exist.

**2 (really 1 trusted) equations against 4 parameters.** Any AW-parameter
identification from this data is under-determined — a numerological fit of the
kind the Δ_λ gate ("no seventh fit-based ansatz") and the formalize-first
protocol (`compute-author §3.3`) exist to prevent. **Do not run the scan.**

## What IS already settled (do not re-derive)

- **Constant-coefficient depth-2 kernel: REFUTED** (PR #1900,
  `ck_c4_constant_depth_two_prediction`): constants over-determine
  `c₄ = 1 − c₃² ≈ −3.28` vs ≈ −0.97 (×3.4 miss). The surviving class is
  *depth ≥ 3 or non-constant* — the AW recurrence is precisely the leading
  non-constant candidate, which is why 1jrh is well-posed and not already closed.
- **Kernel leading coefficient is bar-ODD** (`ck_a1_bar_odd`, PR #1900):
  `a₁ = −c₃ = √2·Φ₂`. Note the 1jrh hypothesis wants a bar-EVEN multiplier
  `A_k`; these are compatible only if the AW `A_k`'s k-dependence carries the
  parity (the constant part bar-even, the `q₀^k` part supplying the odd
  component) — a structural constraint the future test must respect, recorded
  here so it isn't lost.
- **Mode→ladder bridge constraints** (PR #2465, C13): the surviving generating
  `f` is non-linear in `Δtr_M`; `bar-even (u↦1/u) ≠ even-in-ℏ` (two independent
  gradings — do not conflate when building the even ladder).

## The gated, decisive experiment (one line once the rung exists)

**Measure `c₃^even`** — extend the Hoefsmit Stage-B net-route extraction
(the machinery that produced `c₂^even ≈ −8`,
[`2026-06-16-hoefsmit-stage-b-attempt-verdict.md`](2026-06-16-hoefsmit-stage-b-attempt-verdict.md))
one order deeper in `u`. Then:

1. **Casoratian sign test (parameter-free):** compute
   `W₂ = c₂^even·c₃^odd − c₃^even·c₂^odd = (−8)(−2) − c₃^even(−1) = 16 + c₃^even`
   and `W₃` (needs c₄^even or uses the odd c₄ tier with a caveat). The AW
   positivity forces `sign(W₃/W₂) = −sign(B₃)` with `B₃ < 0` in the compact
   regime ⇒ **`W₃/W₂ > 0`**. A sign violation refutes the one-recurrence
   hypothesis outright, no parameters fitted.
2. Only if the sign test passes: the four rungs
   `(c₂,c₃)^{even,odd}` give 3 independent constraints — still one short of
   pinning `(a,b,c,d)`, so the *identification* stays gated on either a fifth
   rung or a structural relation (e.g. the ζ₄-residue constraint from
   `conj:binding-qbeta-complex-volume` §fields) supplying the fourth equation.

## Disposition

- `1jrh` is **scoped, not closed**: the test is well-posed, the prior
  refutations are transferred in, and the blocking measurement (`c₃^even` from
  Stage-B order-u³) is named. Re-title suggestion for the owner:
  *"1jrh: measure c₃^even (Hoefsmit Stage-B order-u³), then run the Casoratian
  sign test"*.
- No compute was run and no parameters fitted — this is the formalize-first
  prune the protocol prescribes for a wide under-determined search.
