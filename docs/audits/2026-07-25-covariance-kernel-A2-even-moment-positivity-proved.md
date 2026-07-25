# Covariance-kernel epic (`qou-x631`) — PROVED: even hook-power moment positivity

**Date:** 2026-07-25 · **Branch:** `claude/covariance-kernel-even-moment-proof-2026-07-25` · **Tier:**
proved sub-result (exact polynomial + manifest positivity certificates) · **Discipline:** scope-(a);
no fit; nothing wired; no `c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`, attack `qou-ogrk` (A2).

## Result

The even-`k` proof lead of the [moment skeleton](2026-07-25-covariance-kernel-A2-moment-skeleton.md) is
**executed**. The even hook-power moments of the covariance measure

> `M_{2j} = Σ_v v^{2j} ν_v = Cov_Planch(Σ_□ h^{2j}, Σ_□ h²)`   (with `ν_v = Cov_Planch(N_v, ω₃)`)

are **proved positive for all `n ≥ 3`**. Both `Σh^{2j}` and `Σh²` are shifted-symmetric, so each
`M_{2j}` is an exact polynomial in `n` (Ivanov–Olshanski, [`math/0304010`](https://arxiv.org/abs/math/0304010));
derived here by exact-`Fraction` Lagrange interpolation (cross-verified on extra points) and factored to
expose a **manifestly positive** cofactor:

| moment | exact factorization | cofactor certificate |
|---|---|---|
| `M_2(n)` | `n(n−1)(n−2)/3` | `= \|C₃\|`; cofactor `≡ 1` |
| `M_4(n)` | `n(n−1)(n−2)/3 · 5(n − 8/3)` | linear, unique root `8/3 < 3` ⇒ `> 0` for `n ≥ 3` |
| `M_6(n)` | `n(n−1)(n−2)/3 · 7(3n − 8)²` | **perfect square** ⇒ `≥ 0`, `> 0` for `n ≠ 8/3` |

Since `n(n−1)(n−2)/3 > 0` for `n ≥ 3` and each cofactor is positive for every integer `n ≥ 3` by
inspection (constant / linear-past-its-root / perfect square), `M_{2j}(n) > 0` for `n ≥ 3` is a
**theorem** — not a numerical observation. This is the first genuinely-proved positivity in the epic
beyond the `k ≤ 7` `decide` instances.

## Scope and honesty

This settles the **even** half of the moment skeleton. Odd-`k` moments are non-polynomial (not
shifted-symmetric) and remain empirical. It does **not** prove A2: the A2 weight `ln(v)` is *concave*,
not a positive combination of even powers, so `M_{2j}>0` does not close it — the global argument
identified by the [pointwise-route correction](2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md)
is still required. The kernel and A2 themselves remain open §3b conjectures (both verified exactly
`k,n ≤ 40`).

## Formalizability

The certificates are Lean-ready: `M_6`'s cofactor `7(3n−8)²` is one `positivity`/`nlinarith` line, `M_4`'s
`5(n−8/3)` a `linarith` on `n ≥ 3`, and `M_2 = |C₃|` already carried in
`YoungDiagramKernel.lean`. A follow-up may formalize `M_4, M_6 > 0` directly.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_A2_even_moment_positivity_proved.py`](../../computations/deltalambda/wlambda_covariance_epic_A2_even_moment_positivity_proved.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-A2-even-moment-positivity-proved.witness.json`

## Cross-references

- Moment skeleton (the lead): [`2026-07-25-covariance-kernel-A2-moment-skeleton.md`](2026-07-25-covariance-kernel-A2-moment-skeleton.md)
- Pointwise-route correction: [`2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md`](2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md)
- Epic map: [`2026-07-25-covariance-kernel-epic-synthesis.md`](2026-07-25-covariance-kernel-epic-synthesis.md)
- Attack plan: bean `qou-v8t7`; A2 `qou-ogrk`. Ivanov–Olshanski `math/0304010`.
