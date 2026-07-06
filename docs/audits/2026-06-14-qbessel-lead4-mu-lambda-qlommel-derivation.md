# Lead 4 derived: is the confinement spectrum a q-Bessel zero spectrum? (2026-06-14)

## Status: derive-first (no probe) — REFUTED for the finite spectrum, REDIRECT to the tower

Owner steer: *"first try to derive/prove, not fit/probe."* This settles **lead 4**
of the Bessel audit — the q-drumhead question, *"is the framework's confinement /
mode spectrum a q-Bessel **zero** spectrum?"* — by **exact symbolic algebra in
ℚ(q)**, no float, no fit.

- **Compute (exact, symbolic):** [`computations/qbeta/qbessel_mu_lambda_vs_qlommel_zeros.py`](../../computations/qbeta/qbessel_mu_lambda_vs_qlommel_zeros.py) → witness (3/3).
- **Companion (step 1, proved):** the 2nd-order q-Bessel equation `☆` is now a Lean theorem — [`QBesselContiguityRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QBesselContiguityRecurrence.lean) (`qbessel_second_order_recurrence`, sorry-free).

## The question

Classically, a drumhead's mode frequencies are the **zeros** of a Bessel function
`J_ν`. The q-analogue would read the framework's mode spectrum as the zeros of a
q-Bessel. The natural "mode spectrum" is the q-heat-kernel content-Casimir
([`prop:q-heat-kernel-peter-weyl`](../../content/quantum-observable-universe/information-theory/q-heat-kernel-peter-weyl.md)):

$$\mu_\lambda \;=\; \hbar_q^2 \sum_{x\in\lambda} [c(x)]_q\,[c(x)+1]_q,\qquad \hbar_q=\tfrac{q-1}{q},\; c(x)=\text{col}-\text{row}.$$

## The derivation (three exact facts)

**(A) Algebraic + finite.** Each `μ_λ ∈ ℚ(q)` — a rational function of q. Exactly
(λ ⊢ 3):

| λ | μ_λ |
|---|---|
| (3) | `q³ − 2 − 1/q + 2/q²` |
| (2,1) | `(q−1)²(q+1)/q²` |
| (1³) | `(q−1)²(q+1)/q⁵` |

At fixed n the spectrum is finite of size `p(n)` (the partition number), with
**content-Casimir degeneracies** — e.g. `μ_{(3,1)} = μ_{(3)}` and `μ_{(2,2)} =
μ_{(2,1)}`.

**(B) Cardinality obstruction.** The Hahn–Exton q-Bessel `J_ν^{(3)}(x;q)` is
entire in x with **infinitely many zeros**, transcendental over ℚ(q); a finite
algebraic set cannot be that zero set. Its finite/algebraic truncation is the
**q-Lommel polynomial** `h_{m,ν}` of degree m — but `p(n) ≠ n` (`p(4)=5≠4`,
`p(5)=7`, `p(6)=11`), so the per-n spectrum is **not** the zero set of the
degree-n q-Lommel polynomial.

**(C) Structural type.** `μ_λ` is a **compact-group (SU_q(2)) Casimir**
eigenvalue — quadratic in the cell contents; verified `q→1`:
`μ_λ/ℏ_q² → Σ_x c(x)(c(x)+1)`, the classical content-Casimir. q-Bessel zeros are
the **non-compact `E_q(2)` / q-disk** spectrum. The two are bridged **only** by
the `SU_q(2)→E_q(2)` contraction (PR #2279).

## Verdict

> **REFUTED for the finite per-n spectrum** (derived, not probed): it is the
> compact q-Casimir spectrum — algebraic, `p(n)`-fold, quadratic-in-content —
> **not** a q-Bessel/q-Lommel **zero** spectrum.
>
> **REDIRECT:** the q-Bessel/q-Lommel zero structure lives in the non-compact
> `E_q(2)` = `n→∞` **brane-tower / contraction limit**. There the **q-Lommel
> three-term recurrence** (the "tower from two seeds") is the right tool — and
> that is exactly where the binding `Δ_λ` ladder lives. So lead 4 and the binding
> `Δ_λ` direction are the **same infinite-tower object**; the finite-n confinement
> spectrum is the wrong place to look.

This confirms #2279/#2300's *"the Bessel object is the tower, not the n-trace"*
from the **spectral** side, and it does **not** refute the q-Lommel-for-binding
hypothesis (a different, infinite-tower object) — it pins where that hypothesis
must be tested.

## What is provable next (still derive-first, gated)

The binding `Δ_λ` test must derive the q-Lommel order-ν recurrence coefficient
`b_ν(x;q)` from the substrate (the q-Casimir / contraction data), **not** fit it,
and pass the deuteron. The formalize-first pre-check (cheap, decisive) remains:
do the existing `Δ_λ` values from the six failed ansätze lie on **any** 3-term
(q-Lommel) recurrence orbit? Per the AGENTS.md `Δ_λ` gate, no seventh fit-based
ansatz — only a substrate-derived recurrence.

## Cross-refs

- Bessel audit + leads: this session's q-Bessel sweep (paper + compute + docs).
- PR **#2279** (q-Bessel identification — the tower/contraction object).
- PR **#2300** (real-x c_3 closure refuted — same fibre-vs-archimedean wall).
- `prop:q-heat-kernel-peter-weyl`, `prop:q-beta-c-k-recursion-from-habiro-q-difference`.
- AGENTS.md `Δ_λ` gate (no seventh fit-based ansatz).
