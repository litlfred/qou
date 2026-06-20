# Q_β chain-D (Type-B folded crystal) — bar-parity formalize-first gate

**Date.** 2026-06-20.
**Bean.** qkhc (Q_β kernel hunt, Stage C) — fibre-level kernel `R(q,ξ)` in
`F(qξ) = R(q,ξ)·F(ξ)`.
**Status.** SCOPE / formalize-first gate — **no search run, no fit**. Owner-gated
multi-session; this is the cheap decisive prune *before* the 12–17 session
Type-B build.

## Why a gate before the build

The Stage-C kernel hunt has refuted every scalar `c_k` form (through C14:
Hahn–Exton trivial-kernel, [`a9c6b74f`](https://github.com/litlfred/qou/commit/a9c6b74f), 2026-06-20).
The surviving structural options are composite crystal chains:

- **B** — Wenzl × q-Pochhammer (5–6 sessions)
- **C** — Demazure × q-Pochhammer (5–7 sessions; reusable for the mass crystal)
- **D** — **Type-B folded crystal** (12–17 sessions; *bar-involution invariant
  by construction*, CLAUDE.md §7b)

**D is the most expensive.** Per the formalize-first discipline (CLAUDE.md
§"narrow the search before running it"), a *structural parity check* should
gate D before any infrastructure is built — because Type-B's defining virtue
(bar-invariance) is testable against Q_β's *known* bar-parity in one bookkeeping
step.

## The gate — bar-parity bookkeeping

**Setup.** The categorical ladder ([`prop:q-beta-categorical-precision-ladder`](../../content/quantum-observable-universe/mass-theory/q-beta-categorical-precision-ladder.md)):

$$Q_\beta = Q_{\text{base}}\cdot\prod_{k\ge 2}\bigl(1 + c_k\,u^k\bigr),\qquad u = b\,\hbar_q^2 .$$

**Bar action on `u`.** With `ℏ_q = 1 − q⁻¹`, the bar-involution `q ↦ q⁻¹` gives

$$\hbar_q \;\xmapsto{\;q\mapsto q^{-1}\;}\; 1 - q = -q\,(1 - q^{-1}) = -q\,\hbar_q
\quad\Longrightarrow\quad \hbar_q^2 \mapsto q^2\,\hbar_q^2 .$$

So **`u ↦ q²·u`** (modulo the bar-transform of the Hoefsmit base `b(q)`, see
"open input" below).

**Type-B's claim.** A Type-B folded crystal's content statistic `q^{c(T)}` is
**bar-invariant by construction** (§7b: "GS normal forms are bar-involution
`q↦q⁻¹` invariant"). So a Type-B kernel `R(q,ξ)` would deliver **bar-invariant
`c_k`**: `c_k(q⁻¹) = c_k(q)`.

**The decisive condition.** For the ladder rung `c_k u^k` to be bar-**even**
(the parity a bar-invariant kernel must reproduce against the `q²u` scaling):

$$c_k(q^{-1})\,\bigl(q^{2}u\bigr)^{k} = c_k(q)\,u^{k}
\quad\Longleftrightarrow\quad \boxed{\,c_k(q^{-1}) = q^{-2k}\,c_k(q)\,}.$$

A **bar-invariant** `c_k` (Type-B's output, `c_k(q⁻¹)=c_k(q)`) satisfies this
**iff `q^{-2k}=1`** — i.e. **never** for generic `q`. Concretely the proved rung
`c_2 = −1` (a bar-invariant constant) gives `c_2(q⁻¹) = −1` but
`q^{-4}c_2(q) = −q^{-4}` ≠ `−1`.

**⇒ apparent parity mismatch:** Type-B's bar-*invariant* content is the *wrong
transformation law* to be the c_k kernel directly. The kernel must transform as
`c_k(q⁻¹)=q^{-2k}c_k(q)` (a *weighted* bar-covariance, not bar-invariance).

## Verdict logic (what the completed gate decides)

| outcome of the symbolic check | meaning | action |
|---|---|---|
| `b(q)` bar-invariant ⇒ mismatch stands | Type-B bar-*invariant* content ≠ `q^{-2k}`-covariant kernel | **refute D** as the *direct* kernel; Type-B can only enter as the bar-**odd companion** (the sinh partner Q_β already is) — redirect the build to **C** (Demazure, no bar-constraint) |
| `b(q)` carries `q^{-2}`-type weight that absorbs the scaling | the `q²u` is cancelled; bar-invariant `c_k` becomes consistent | **greenlight D** — Type-B is the correct bar-symmetric kernel |

Either way the 12–17 session investment is **gated by one symbolic check**, not
launched blind.

## The one open input (next concrete sub-task)

The check needs the **fibre-level symbolic forms**, currently only available
numerically (`b = hoefsmit_b` is evaluated at `q₀` in
[`qbeta_ck_truncation_order_analysis.py`](../../computations/qbeta/qbeta_ck_truncation_order_analysis.py)):

1. **`b(q)`** — the Hoefsmit ladder base as a symbolic function of `q` (its
   bar-transform `b(q⁻¹)` is the deciding factor in the table above).
2. **`c_3(q), c_4(q)`** — the fibre-level `c_k` forms (the near-match `J_Hopf(q)`,
   `c_3·b⁴`, …) symbolically in `q`, to test `c_k(q⁻¹) =? q^{-2k}c_k(q)`.

Both are the *bar-odd / Im(q)-at-the-fibre* objects flagged in CLAUDE.md (the c_k
live in the fibre, possibly complex; the archimedean `Im(q₀)=0` constraint does
**not** apply at the fibre). Extracting `b(q)`/`c_k(q)` symbolically is the
first session of the D tranche — and it is exactly what this gate needs, so it
is *not* wasted even if D is subsequently refuted.

## Recommendation

- **Pick D** for its structural fit to Q_β's bar-odd (sinh-partner) nature — **but
  run this parity gate first.** The derivation above already shows a *prima facie*
  mismatch (Type-B is bar-*invariant*; the kernel needs `q^{-2k}` bar-*covariance*),
  which would **redirect to C** unless `b(q)` supplies the compensating weight.
- This is a **prune, not a closure**. Nothing wired; `c_k` stay cal-anchored.
- Owner-gated multi-session; coordinate with the Q_β upstream cluster before
  opening the symbolic-`b(q)` extraction.
