---
# qou-3qrv
title: 'Class I: is the Borromean trace CONVENTION forced, or selected because it lands on CODATA?'
status: todo
type: task
created_at: 2026-08-08T09:02:45Z
updated_at: 2026-08-08T09:02:45Z
---

Surfaced 2026-08-08 (PR #4727) while scoping Class I (the μ–p tension) per the
owner's "attack options class 1?". **Flag, not a refutation** — raised under the
standing critical-distance license as a suspected hidden degree of freedom.

## The numbers (reproduced at 50 dps, proton pin q₀ = 1.1099785827513808)

`m_p/m_e = 2·(Vol(4₁)/ℏ_q²·F_Bor − 6)`, `F_Bor = |tr_M(β_Bor)|·[3]_q!/q³`.

| Borromean trace | value at q₀ | ⇒ m_p/m_e | vs CODATA |
|---|---|---|---|
| **convention D** (Jones / Temperley–Lieb; the Lean closed form `(4+h²−3h⁴−h⁶)/(h²+4)`, used in production) | 0.998562163836787 | **1836.152673426** | **+1.35 ppb** |
| `tr_M_atomic(1,0)` (the "exact proton Markov trace" of the 2026-05-28 audit) | 1.0653 | 1959.671984282 | **+6.7 %** |

The 6.7 % figure in
[`2026-05-28-mu-p-tension-substrate-floor.md`](../docs/audits/2026-05-28-mu-p-tension-substrate-floor.md)
is **live and exactly reproducible** — not stale, not arithmetic error. It is a
**trace-convention** difference.

It is also a *third* object: `trM_borromean`'s own docstring records that
convention D and the Wenzl z-trace (convention C) differ by only 1.955e-4 at q₀
(195 ppm). Neither of those explains 6.7 %.

## The question

Production uses the convention whose value lands on CODATA to 1.35 ppb, while a
nearby categorical object for "the Borromean Markov trace" sits 6.7 % away. Two
readings:

- **(a) D is categorically forced.** The Jones/TL specialization is the right
  object for this formula on independent grounds, and `tr_M_atomic` answers a
  different question. Then there is no elephant, and the 1.35 ppb round-trip is
  the honest residual.
- **(b) The convention is a hidden discrete choice.** D was adopted *because* it
  matches. Then the m_p "derivation" carries an undeclared DOF, and the μ–p
  tension is being measured on a baseline selected by the answer.

**What does not settle it:** `BorromeanMarkovTrace.lean` proves the *closed form
for convention D*. That is a theorem about D, not a proof that D is the correct
convention here — the same "sorry-free ≠ derived" distinction the registry warns
about. The docstring's citation of the Lean file must not be read as settling
the selection.

## Next step

Settle (a) vs (b) on **categorical** grounds only — which trace the Archimedean
functor at q₀ actually induces on β_Bor — never by which value matches. If (a),
write the forcing argument into the docstring, since the file currently asserts
the convention without justifying the choice. If (b), the m_p formula carries an
undeclared DOF and Class I's 11.5 ppb framing needs restating.

Related: `2026-06-09-binding-trace-convention-split.md` (the D≠C analysis) and
`probe_convention_d_vs_c_borromean.py`. This bean is about **D-vs-atomic**,
which that split does not cover.

## Scope

No probe beyond the reproduction above, no fit, nothing wired, no tier changed.
Scope-(a) observation: a convention discrepancy is documented and its selection
is unjustified in-file — **not** a claim that the m_p formula is wrong.
