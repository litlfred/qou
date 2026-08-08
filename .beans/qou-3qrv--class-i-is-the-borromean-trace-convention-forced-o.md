---
# qou-3qrv
title: 'Class I: is the Borromean trace CONVENTION forced, or selected because it lands on CODATA?'
status: completed
type: task
priority: normal
created_at: 2026-08-08T09:02:45Z
updated_at: 2026-08-08T23:53:24Z
---

> ## ANSWERED 2026-08-08 — `claude/3qrv-borromean-trace-convention-2026-08-08`
>
> Full write-up:
> [`docs/audits/2026-08-08-borromean-trace-convention-forcing.md`](../docs/audits/2026-08-08-borromean-trace-convention-forcing.md).
>
> **1. The 6.7 % below is a FALSE ALARM — retract it.** It is not a trace
> convention at all. `tr_M_atomic(1,0)` traces a **different braid word**: an
> 11-crossing atomic word (confinement core *grouped* as `σ₀³σ₁⁻³`, plus 3
> quark-pair and 2 gluon crossings), not the 6-letter `β_Bor`. Tracing the
> **pure** `(σ₀σ₁⁻¹)³` through the *same* machinery gives
> **0.998366622585716 = convention C exactly** (195.8 ppm from D), reproducing
> the registry's documented D−C gap. The bean's phrase *"convention D for the
> same braid"* is the error — the braids differ. `tr_M_atomic` is not a fifth
> convention; it answers a different question.
> (`computations/probe3qrv.py`)
>
> **2. Verdict on (a) vs (b): (a) for the mathematics, (b) for the premise.**
>
> *(a) — the forcing argument now exists and is proved.* A normalised Markov
> trace on H₃(q) is fixed by `(tr 1, tr σ₀, tr σ₀σ₁) = (1, z, z²)`, so the
> weights are a 3×3 solve in the Ocneanu parameter `z`. The Temperley–Lieb
> condition `y_(1³)(z) = 0` has exactly **two** roots: `z = q`, degenerate
> (weights `(1,0,0)` — it kills the 2-row block too, so it is not faithful on
> TL₃), and `z = q³/(q²+1)`, whose weight vector is exactly
> `([4]_q/[2]_q³, 1/[2]_q², 0)` = **convention D**. So **D is the unique Markov
> trace factoring through TL₃ and faithful on it** — no residual freedom, no
> CODATA anywhere in the chain. Sorry-free in
> [`MarkovTraceTLUniqueness.lean`](../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean)
> (`lean`-direct exit 0; `#print axioms` → `[propext, Classical.choice,
> Quot.sound]`, no `sorryAx`). Now written into the `trM_borromean` docstring,
> which previously asserted the convention with no justification.
>
> *(b) — the premise is NOT established, and the corpus contradicts itself.*
> **This is the headline finding.** The scope note of
> `prop:h3-markov-wenzl-weights`
> ([`h3-markov-wenzl-weights-context.md`](../content/quantum-observable-universe/mass-theory/h3-markov-wenzl-weights-context.md))
> says verbatim that the **mass and binding computations use the full-Hecke
> Ocneanu trace** — convention **C** — while production uses **D**
> (`canonical_mass.py:108` → `F_Bor` → `trM_borromean`). Switching to the trace
> the paper names moves m_p by **−197 ppm**. The same note also claims the two
> traces coincide on writhe-0/π=id braids so "every physical mass prediction is
> insensitive to the distinction"; `β_Bor` **is** such a braid and `D−C =
> 1.9554e-4` there exactly, so that sentence is false.
>
> **3. What is actually open** — one categorical fact, not a numerical
> question: *does the mass fibre functor land in `Rep(SU_q(2)) ≃ TL₃` or in
> full `H₃(q)`?* If TL, D is forced and the scope note needs correcting. If
> full H₃, production is on the wrong trace by 197 ppm. **The answer must not
> be read off which value matches CODATA.**
>
> **4. Also superseded:** `h3-markov-wenzl-weights-proof.md` §Step 3 derives
> `y_(2,1) = 1/[2]_q²` *by comparing against the Borromean closed form* — fine
> for its own purpose, but it cannot serve as a forcing argument because it
> inputs the answer. The derivation above uses only the Markov axioms, the
> character table, and TL.
>
> Nothing wired, no tier changed, no production value altered.

Surfaced 2026-08-08 (PR #4727) while scoping Class I (the μ–p tension) per the
owner's "attack options class 1?". **Flag, not a refutation** — raised under the
standing critical-distance license as a suspected hidden degree of freedom.

## The numbers (reproduced at 50 dps, proton pin q₀ = 1.1099785827513808)

`m_p/m_e = 2·(Vol(4₁)/ℏ_q²·F_Bor − 6)`, `F_Bor = |tr_M(β_Bor)|·[3]_q!/q³`.

| Borromean trace | value at q₀ | ⇒ m_p/m_e | vs CODATA |
|---|---|---|---|
| **convention D** (Jones / Temperley–Lieb; the Lean closed form `(4+h²−3h⁴−h⁶)/(h²+4)`, used in production) | 0.998562163836787 | **1836.152673426** | **+1.35 ppb** |
| `markov_peel.tr_M_atomic(1,0)` (the "exact proton Markov trace" of the 2026-05-28 audit) | **1.06530614425445** | 1959.67 | **+6.7 %** |

**Recomputed from source, not quoted.** `tr_M_atomic(1,0)` returns a *sympy
expression in q* (a genuine categorical object, not a stored float); evaluating
it at the proton-pin q₀ gives **1.06530614425445**, which reproduces the audit's
`1.0653` to five significant figures. Gap vs convention D: **6.684 %**. So the
figure in
[`2026-05-28-mu-p-tension-substrate-floor.md`](../docs/audits/2026-05-28-mu-p-tension-substrate-floor.md)
is live, and it is a **trace-convention** difference, not arithmetic error and
not staleness.

**It is not any of the four registered conventions.** Per the registry in
[`2026-06-09-binding-trace-convention-split.md`](../docs/audits/2026-06-09-binding-trace-convention-split.md):
D ≈ 0.9985622, the Wenzl-bridge z-trace ≈ 0.9983666, convention A's `tr_M` =
1.332 (matrix-M parabolic, PR #2082), B is deprecated, C is
`markov_trace_canonical.tr_M_element`. The C-vs-D split that registry analyses
is ~195 ppm and does **not** explain 6.7 %. `tr_M_atomic` is a fifth object
relative to that table, and the table does not cover it.

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

## Reproduce

```python
# from computations/ ; needs sympy + mpmath
import _path_bridge, sympy as sp, mpmath as mp
from markov.markov_peel import tr_M_atomic
from q_parameter import Q                      # proton pin, per the standing directive
mp.mp.dps = 50
e = tr_M_atomic(1, 0)                          # sympy Add in q
q = list(e.free_symbols)[0]
print(sp.N(e.subs(q, sp.Float(str(Q), 50)), 30))   # 1.06530614425444993...
```

Convention D for the same braid at the same q₀:
`trM_borromean(q) = |(4+h²−3h⁴−h⁶)/(h²+4)|`, `h = q − 1/q` → `0.998562163836787`.

---

## CLOSED 2026-08-08 — owner ruled **D** (PR #4834)

Audit: [`2026-08-08-markov-z-convention-d-ruling.md`](../docs/audits/2026-08-08-markov-z-convention-d-ruling.md).

The `mass` channel leaves `disputed`. The **definition** moved to meet
production, not the reverse — the channel already ran D, so **no production
value changed** (no `F_Bor` consumer, no `m_p`). The −197 ppm was always the
cost of the opposite move, which was never made.

The bean's constraint — *"the answer must not be read off which value matches
CODATA"* — is met by two independent steps, neither touching a measured value:

1. **Bar-covariance of M3 excludes C** (new). M3 contains `σ_n`, which bar
   inverts, so the bar-partner of `z` is `z − h`. D satisfies `bar(z) = z − h`;
   C violates it by exactly `h`. Sorry-free: `QOU.BraidKnot.zD_bar_sub`,
   `zC_ne_bar_sub`, `hecke_inv_eq_sub`. **This step alone does not select D** —
   `bar_sub_of_bar_even` proves the solution set is D plus any bar-even
   function.
2. **TL faithfulness picks D out of the rest** — `MarkovTraceTLUniqueness`,
   already proved under §3 above.

Why the pair settles what step 2 alone did not: step 2's weak half was always
its **premise** (does the mass fibre functor land in TL₃ or full H₃?). Step 1
does not answer that either — it makes the answer *unnecessary for excluding
C*, since whatever the functor lands in, the stabilisation parameter must be
bar-covariant under the involution M3 lives under.

**Still open, but no longer load-bearing:** the fibre-functor question itself,
as a categorical fact.

Follow-up: `qou-ql2a` — the 68 remaining C-form sites (a per-file channel call,
explicitly *not* a sweep).
