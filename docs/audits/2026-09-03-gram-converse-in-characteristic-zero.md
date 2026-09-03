# The Gram criterion's converse holds in characteristic zero — `det(twGram) ≠ 0` at every rank

*2026-09-03, beans `qou-kwoa` / `qou-0y6h`. Lean:
[`QOU/MathlibExt/RegTraceGramNondegenerate.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/RegTraceGramNondegenerate.lean),
[`QOU/MathlibExt/TracePi.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/TracePi.lean),
[`QOU/Hecke/TwGramDetNonzero.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/TwGramDetNonzero.lean).
PR #6517.*

## Result

```lean
twGram_det_ne_zero {K} [Field K] [CharZero K] (q : K)
    (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
  (twGram K (q ^ 2) n).det ≠ 0
```

Sorry-free, `[propext, Classical.choice, Quot.sound]`, at **every** `n`. No determinant is
evaluated anywhere in the proof.

## This does not contradict the 2026-08-30 scope-(b) exclusion — it is its complement

[`2026-08-30-tw-gram-determinant-measured.md`](2026-08-30-tw-gram-determinant-measured.md)
records, correctly, that

    det(twGram) ≠ 0  ⟹  H_n(q) semisimple

is one-directional, with a **characteristic-2** counterexample: at `n = 2` the constant
`2⁴ = 0`, so the determinant vanishes while Dipper–James still gives semisimplicity.

That exclusion stands, unamended. What it excludes is a *characteristic-free* converse. The
same audit says so in its own words — *"any general Lean theorem along this route must carry
a characteristic hypothesis"* — and `twGram_det_ne_zero` carries exactly that, so the audit
predicted this theorem's shape rather than forbidding it.

**But one bullet in that audit is stated unqualified** — *"an agent hoping to get the
converse should stop: it is false"* — and read alone it closes a route that was open. It has
been scoped in place. This is the AGENTS.md over-narrowing failure mode in miniature: the
numerical finding was right, the scope sentence was one clause short, and the clause was the
one a later agent would act on.

### Independent corroboration between the two

The 2026-08-30 audit derives its obstruction as *"for `A = M_d(K)` the regular trace form is
degenerate exactly when `char K ∣ d`"*. The new Lean reaches the same place from the other
side: `regTraceForm_one_one` proves `B(1, 1) = finrank K A`, which for `M_d(K)` is `d²`. For
a prime `p`, `p ∣ d²` iff `p ∣ d` — so the two statements agree, having been obtained by
completely different arguments.

## Why the expensive route was not needed

Both prior audits price the remaining work as Geck–Pfeiffer character theory, and both are
right that **the determinant's VALUE** needs it. They are also right that the obvious
combinatorial shortcut is closed —
[`2026-09-02-tw-regular-trace-not-combinatorial.md`](2026-09-02-tw-regular-trace-not-combinatorial.md)
refutes it with an explicit `S₅` witness, and that refutation is untouched.

What changed is that **non-vanishing does not go through the value.** Semisimplicity of
`H_n(q)` is proved independently, via the Wedderburn decomposition
(`QOU.SchurWeyl.heckeWedderburn`), which owes the Gram determinant nothing. So the Gram
implication can be run backwards:

    semisimple  ⟹  regular trace form nondegenerate  ⟹  det ≠ 0, in every basis

The missing piece was the *converse of the Gram criterion*, which is three short lemmas.
`tr(L_{T_u})` for general `u` is not needed at any point, so the `S₅` witness — which closes
the search for a combinatorial `tr(L_{T_u})` — does not bear on it.

## The argument

1. **The radical is a two-sided ideal.** `regTraceForm_mul_assoc` gives `B(xy, z) = B(x, yz)`
   (both are `trace (L_z)` for the same `z`). Right-closure is immediate; **left**-closure
   needs that together with `regTraceForm_comm`, because the form is associative only in that
   one shape. Packaged as `regTraceRadical : TwoSidedIdeal A`.
2. **On a simple ring the radical is `⊥` or `⊤`**, and `⊤` would put `1` in it, giving
   `B(1,1) = 0`. With `regTraceForm_one_one` (`B(1,1) = finrank K A`, since `L_1 = id`) that
   is excluded in characteristic zero.
3. **A matrix block is simple** for nonempty index (`IsSimpleRing.matrix` over the simple ring
   `K`). Empty index is handled separately: it is the zero ring, which is *not* simple —
   simplicity requires `Nontrivial` — but whose form is nondegenerate because `0` is its only
   element.
4. **A product of matrix algebras is not simple**, so block verdicts are *summed*, not
   transported: `regTraceForm_pi`. That needed `trace_piDiag`, a genuine Mathlib gap —
   Mathlib has only the binary `LinearMap.trace_prodMap'`.
5. **Transport** to the `T_w` basis along `skeinIwahoriEquiv ∘ heckeWedderburn`.

Mathlib's `Algebra.traceForm_nondegenerate` does not apply: it is about separable field
extensions, whereas `regTraceForm x y = trace(L_{xy})` is the regular trace of a
possibly-noncommutative algebra.

## Cross-check at the one rank computed by hand

`twGram_det_ne_zero_rank_one_agrees`. `twGram_det_rank_one` evaluates the four Markov-trace
entries directly and gives `det = (1 + Q)²`; at `Q = q²` its non-vanishing is `q⁴ ≠ 1`, which
is exactly what `NotRootOfUnity q` supplies. Same conclusion, same hypothesis, two entirely
different routes — Wedderburn plus the trace-form radical, versus an explicit `2 × 2`
determinant. Kept in the Lean as a regression.

## What is still open

1. **The determinant's VALUE.** Geck–Pfeiffer 7.2.6, `det(Gram) = ∏_λ (Schur_λ)^{f^λ}`, is
   untouched and remains the book-length development `qou-kwoa` was split out to carry.
   `qou-avt2`'s symbolic characters are still the right material for it, and the `S₅` witness
   still closes the combinatorial shortcut to it. A consumer needing the Schur-element product
   gets nothing from this result.
2. **Small characteristic.** Untouched and, per the 2026-08-30 exclusion, unreachable by this
   route at all — not merely unproved.
3. **The square root.** The statement is at `Q = q²`, the same caveat as
   `isSemisimpleRing_iwahoriHecke_sq` (`qou-j377`) and for the same reason: `skeinIwahoriEquiv`
   relates the skein algebra at `q` to the Iwahori carrier at `q²`, and a general field need
   not contain a root. Removing it needs base change of `IwahoriHecke` along a field
   extension. The *hypothesis* would survive that move for free — `NotRootOfUnity Q ⟹
   NotRootOfUnity q` when `q² = Q`, since `q^m = 1` forces `Q^m = 1` — so only the algebra's
   scalar extension is missing. Over `ℝ` with `Q > 0`, or any field where `Q` is a square,
   `twGram_det_ne_zero_of_sq` already gives the statement at `Q`.

## Scope

Semisimplicity and the Gram determinant are **magnitude-axis** facts. Nothing here bears on
the P≠NP wall, as `TwGram.lean` also records.
