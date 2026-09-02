# The `qou-0y6h` blocker is not combinatorial — three hypotheses refuted, with witnesses

*2026-09-02, bean `qou-0y6h`. Probe:
[`computations/hecke/tw_regular_trace_statistics_probe.py`](../../computations/hecke/tw_regular_trace_statistics_probe.py).*

## The question this answers

`QOU.Hecke.TwBasis.twGram` reduces semisimplicity of `H_n(q)` to
`det (twGram) ≠ 0` at every rank, and
[`2026-08-30-tw-gram-determinant-measured.md`](2026-08-30-tw-gram-determinant-measured.md)
established the determinant's *value* at ranks 1–3. Knowing the value does not
supply the proof: the Gram entries are `tr(L_{T_v T_w})`, and the single thing
blocking rank ≥ 2 is the diagonal structure constant `[T_u T_w : T_w]` for a
general `u` — equivalently `tr(L_{T_u}) = Σ_w [T_u T_w : T_w]`.

The generator case is proved in Lean (`trace_lmul_σ`: only descents contribute,
`2·tr = (q−1)(n+1)!`). The obvious next move is to look for the combinatorial
generalisation. **Before spending a session formalising one, this measures
whether a simple one exists.**

## The measurement

Exact arithmetic — sympy in `q` for `S₂`–`S₄`, exact integers at five values of
`q` for `S₅`. No float anywhere.

| statistic of `u` | determines `tr(L_{T_u})`? |
|---|---|
| `length(u)` alone | **No** — fails from `S₄` on |
| `cycleType(u)` alone | **No** — fails from `S₃` on |
| the pair `(length, cycleType)` | **No** — holds in `S₄`, **fails in `S₅`** |

### The witness

Two elements of `S₅` with the **same** Coxeter length 4 and the **same** cycle
type `(2,2,1)`:

    u = (0,3,4,1,2)   tr(L_{T_u}) =  5 (q−1)² (q² + 4q + 1)
    u = (1,0,4,3,2)   tr(L_{T_u}) = 10 (q−1)² (q² +  q + 1)

Not proportional; not even the same irreducible factors. This is a finite exact
computation, so it is a **refutation with a witness**, not a numerical
near-miss — and it is checkable by hand from the multiplication rule.

## The trap, which I walked into twice

**`S₄` satisfies the joint statistic and `S₅` does not.** Worse, `S₂` satisfies
all three and `S₃` satisfies two. Reading upward:

* from `S₃` I concluded *"the trace depends only on length"* — false at `S₄`;
* from `S₄` I concluded *"it depends on `(length, cycle type)`"* — false at `S₅`.

Both readings were consistent with every datum available at the time. The rank
at which a Hecke-algebra pattern first breaks is routinely `n = 4` or `n = 5`,
because that is where the symmetric group first has two classes of equal size
and two elements of equal length in one class. **Do not promote a rank-3 or
rank-4 pattern in this corpus to a general claim without testing `S₅`.** The
probe asserts both halves of the split (`S₄` yes, `S₅` no) so a future edit that
breaks either one fails loudly.

## What this establishes, and what it does not

**Established (scope-(b), by exhaustive finite computation):** none of the three
named statistics determines `tr(L_{T_u})`. Any proposed closed form in
`length`, `cycle type`, or both is refuted by the witness above.

**Not established:** that no closed form exists. `tr(L_{T_u}) = Σ_λ d_λ
χ_λ(T_u)`, and Hecke characters are governed by **Geck–Pfeiffer's theory of
minimal-length conjugacy-class representatives**. The observed pattern is that
theory's signature: the trace at a class's *minimal* length differs from the
trace at higher length in the same class, which is precisely why cycle type
alone cannot determine it. In `S₄`, class `(3,1)` has minimal length 2 with
trace `4(q−1)²` and appears again at length 4 with trace `(q−1)²(q+1)²`.

So the closed form, if wanted, **is** Geck–Pfeiffer — the very theorem
`qou-0y6h` names. That is a book-length development, not a lemma.

## Consequence for `qou-0y6h`

Two things follow, and the second is the actionable one.

1. **Do not spend a session searching for a combinatorial formula** in length,
   cycle type, or descent set. The search is closed by the witness.
2. **Price the remaining work correctly.** Closing `det(twGram)` at rank ≥ 2 in
   Lean means formalising character theory for `H_n(q)` — Mathlib-scale,
   multi-session, and a genuine research formalisation rather than a proof to be
   typed out. Combined with the [characteristic
   bound](2026-08-30-tw-gram-determinant-measured.md) (`det ≠ 0 ⟹ semisimple`
   is one-directional, so the route cannot reach small characteristic even when
   finished), that is the honest state of the bean.

What is *already* unconditional and does not depend on any of this:
`isSemisimpleRing_rank_one` (and its substrate corollary over `ℝ`, `q > 0`),
`twGram` + `isSemisimpleRing_of_twGram_det_ne_zero` at every rank, the full
`σ_mul_Tw` table, `trace_lmul_σ`, and `IsHeckeOfFullRank` for `IwahoriHecke` at
every rank.
