# The n = 6 discriminator for the Temperley–Lieb identification

**Status: SCOPE (in progress).** Findings land as they are measured.

## What is being tested

Sibling PR [#5185](https://github.com/litlfred/qou/pull/5185) (branch
`claude/s2-gram-radical-quotient-2026-08-16`, "S2") established by exact
symbolic computation over ℚ(q) that the convention-D Markov–Gram form has

```
corank(n) = n! − Catalan(n)      measured: 1, 10, 78  at n = 3, 4, 5
                                 (6−5, 24−14, 120−42)
```

and hypothesised that the radical is therefore the **Temperley–Lieb ideal**
`ker(H_n(q) ↠ TL_n(q))`, with quotient `TL_n`. S2 also established the
framing correction that matters most: this is **not** special-parameter
reducibility. `det G ≡ 0` identically over ℚ(q) and corank is constant across
12 rational `q`, so no `q₀` re-pin moves it. What degenerates is the **trace**,
not the algebra.

Three points fitting a formula is suggestive, not proved. Two tests here.

### Test A — the `(1³)` block at n = 3 (cheap, run first)

Corank 1 is consistent with "the TL ideal" and equally with "some other
one-dimensional radical". S1 asked *which block* dies. S2's measured weights
point at `(1³)` — `y₍₁³₎ = 0` exactly, with `y₍₃₎ = (q⁴+1)/(q²+1)²` and
`y₍₂,₁₎ = q²/(q²+1)²` both nonzero — but that is a weight computation, not a
direct identification of the radical's support. Verify that the radical's
support **is** the `(1³)` isotypic component.

### Test B — the n = 6 discriminator

```
6! − Catalan(6) = 720 − 132 = 588
```

A match makes the TL identification very hard to explain away. A mismatch
refutes it outright and is equally valuable.

## Method (planned)

Reuse S2's probe machinery rather than reimplementing it — it rebuilds
`H_n(q)`, the Ocneanu trace and the Gram form from scratch without importing
`pyhecke.gram`, yet reproduces that module's `TR_M` entry for entry, so the
two check each other. Credit for the machinery and for the n = 3,4,5
measurements is S2's (PR #5185).

Exact arithmetic throughout: `fractions.Fraction` over ℚ, sympy over ℚ(q),
and modular arithmetic over a prime field used **only** where it is a
rigorous one-sided bound. **No float64 anywhere** — this is a rank
computation, and floating point would make the answer meaningless. Where
numpy appears it is `int64` exact modular arithmetic, never a float dtype.

Cost note: S2's `gram()` is `O(n!²·|support|)` and does not reach n = 6.
A cheaper exact recursion for the same matrix is needed; it will be
cross-checked entry-for-entry against S2's `gram()` at n = 3 and n = 4
before being trusted at n = 6.

## Discipline

- Anti-fit: nothing here is tuned. This measures a rank and reports it.
- Any refutation carries the (a)/(b) scope classification per AGENTS.md.
- **Measured vs hypothesised** stays explicit. A confirmed n = 6 makes TL a
  very strong hypothesis; it is still not a proof of the ideal-theoretic
  identification for all `n`, and this document must not upgrade it silently.
