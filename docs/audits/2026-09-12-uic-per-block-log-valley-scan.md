# The UIC per-block log: does the one non-additive functional carry a valley?

**Date:** 2026-09-12 · **Branch:** `claude/uic-per-block-log-valley-scan-2026-09-12`
**Bean:** `qou-zlra` (this) · `qou-brng` (class D — **stays open**) · `qou-oooq`, `qou-eqwg` (origins)
**Continues:** PR #7223 / `docs/audits/2026-09-12-graded-binding-sign-convention.md` §5.3,
which closed the `+c_k / −c_k` question for every **product-additive** functional and
left exactly one thing unmeasured: the production accumulator
`hecke_core_legacy.unified_iterative_correction(Z, N)`.

> **STATUS: IN PROGRESS.** This file is committed early so the PR is the durable
> artifact from the first commit (AGENTS.md § Branch + PR workflow, rule 2). The
> measurement is not yet in it.

---

## 0. Why this functional and no other

`#7223` proved, sorry-free, that for any `F` with `F(fg) = F f + F g` — `log`,
`−log`, `α·log`, any sign, any scale — the Vassiliev type-two pair convolution
`Σ_{i<j} bᵢbⱼ` is **absent** from `F(∏ᵢ fᵢ)`. The live binding law
`B = E₀·log(tr_free/tr_atom)` is exactly such an `F` of the **total** trace, so it
cannot carry a two-bond correlation, hence cannot carry `(N−Z)²`, hence has no
valley of stability.

`prop:unified-iterative-correction` is the corpus's **second, inequivalent** log
reading: a weighted sum of logs of **single Wedderburn blocks**. A single block's
trace is *not* multiplicative over the word even when the total is, so the
additive-census theorem does not apply to it. It is therefore the only functional
in the corpus outside the additive class — the last place an order-zero
two-bond correlation could live.

---

## 1. The functional as the corpus actually defines it

*(see the PR for the in-progress working; file:line citations below are verified
against the tree at this branch's base, `origin/main` `a526f20b75d`)*

**Producer** — `computations/hecke_core_legacy.py`:

| line | what it fixes |
|---|---|
| 1693 | `unified_iterative_correction(Z, N, k_max=K_PARTITION_MAX, k_exact=K_PARTITION_MAX)` — wrapper, runs the body inside `mp.workdps(COMPUTE_DPS)` |
| 1719 | `_unified_iterative_correction_exact` — the body |
| 1915 | `scale = e['C_lambda_resolvent_MeV']` — the per-partition weight actually used |
| 548, 564 | `C_lambda_resolvent_MeV = H_q(λ) · y_λ · ρ_λ(s_*) · m_e` |
| 538 | `y_λ = lp_shadow_price(λ) = w_λ/d_λ − 1/[k]_q!` |
| 544, 521 | `ρ_λ(s_*) = 1/(μ_λ + s_*)`, `s_* = (q₀−1)/q₀ = ℏ_q` |
| 1908 | `L0 = _exact_log(dim)` — the `−ln d_λ` of the telescoped form |
| 2186-2192 | **Pass 2**: keep λ only when `final_tr_sign ≤ 0` |

**Content block** — `content/quantum-observable-universe/mass-theory/unified-iterative-correction.md`.

---

## 2. Profiling

*(in progress)*

## 3. The measurement

*(in progress)*

## 4. Scope

*(in progress)*
