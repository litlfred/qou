# The n = 6 discriminator for the Temperley–Lieb identification

**Verdict: CONFIRMED, and upgraded from a corank match to an ideal equality.**

`corank(6) = 588 = 6! − Catalan(6)`, pinned **exactly** — not bounded — at all
12 rational `q` samples and at two independent primes. The sequence is now
**1, 10, 78, 588** at n = 3, 4, 5, 6, and the fourth point was predicted before
it was measured.

Probe: [`computations/probes/tl_n6_discriminator.py`](../../computations/probes/tl_n6_discriminator.py)
· output [`tl-n6-discriminator.json`](../../computations/probes/tl-n6-discriminator.json)
· total runtime 39 s.

## Credit

Sibling PR [#5185](https://github.com/litlfred/qou/pull/5185) ("S2", branch
`claude/s2-gram-radical-quotient-2026-08-16`) did the work this rests on: the
`H_n(q)` T_w-basis arithmetic, the Ocneanu trace by coset recursion, the exact
`Fraction`/GF(p) backends, the q-antisymmetriser, the n = 3, 4, 5 coranks, the
`det G ≡ 0` over ℚ(q) result, and the hypothesis `corank = n! − Catalan(n)`
itself. That machinery is **reused** here (vendored verbatim, see
§Provenance), not reimplemented.

S2's framing correction is also carried forward and is independently
reconfirmed at n = 6: this is **not** special-parameter reducibility. Corank
is constant across `q ∈ [1/3, 5]`, so **no `q₀` re-pin moves it**. What
degenerates is the **trace**, not the algebra.

## Results

### Test A — which block dies at n = 3 (S1's question)

Corank 1 is equally consistent with "the TL ideal" and with "some other
one-dimensional radical". Answered directly, symbolically over ℚ(q), without
characters and without assuming the TL picture:

| Measured (symbolic, ℚ(q)) | Result |
|---|---|
| corank at n = 3 | 1 — reproduces S2 |
| null vector `= (−1/q)^ℓ(w)` identically in q | **true** |
| `T_{s_i} E₋ = E₋ T_{s_i} = (−1/q)·E₋` for every i | **true** |
| `E₋` (sign channel) in the radical | **true** |
| `E₊` (trivial channel, `λ = (3)`) in the radical | **false — survives** |

The Hecke relation `(σ−q)(σ+1/q) = 0` admits exactly two one-dimensional
channels: `σ ↦ q` is `λ = (3)`, `σ ↦ −1/q` is `λ = (1³)`. So `ℚ(q)·E₋` is a
one-dimensional **two-sided** ideal carrying the antisymmetric eigenvalue —
it *is* the `(1³)` block. Since the radical has dimension 1 and contains it,

> **the n = 3 radical is the `(1³)` isotypic block.** Its support is
> identified, not merely its dimension.

Consistent with, and independent of, S2's weights (`y₍₁³₎ = 0` exactly,
`y₍₃₎ = (q⁴+1)/(q²+1)²` and `y₍₂,₁₎ = q²/(q²+1)²` nonzero) — that was a
weight computation; this is a direct identification of the radical's support.

The same two channels behave the same way at every n tested (exact over ℚ):

| n | `(1ⁿ)` sign block in radical | `(n)` trivial block in radical |
|---|---|---|
| 3 | yes | no |
| 4 | yes | no |
| 5 | yes | no |
| 6 | yes | no |

which is what TL predicts: `(1ⁿ)` has n ≥ 3 rows and dies, `(n)` has one row
and survives.

### Test B — n = 6

**corank(6) = 588.** Both bounds, and they meet:

| Bound | How | Value |
|---|---|---|
| `corank ≤ 588` | `rank_p ≤ rank_ℚ` always; measured `rank_p(G) = 132` | 132 = Catalan(6) |
| `corank ≥ 588` | the two-sided ideal `⟨E⟩ ⊆ radical`, `dim_p⟨E⟩ = 588` | 588 |

Pinned at **all 12** q samples and at **two** primes (2³¹−1 and 2³¹−99); every
one of the 24 cells reads `dim⟨E⟩ = 588, rank = 132, corank = 588`. Per-sample
ranks are in the JSON; they are constant, not merely maximal.

The lower bound's two exact ingredients, both verified over ℚ with
`fractions.Fraction` at n = 6:

1. `tr(E_b T_v) = 0` for **every** `v` and every `b` — so each 3-strand
   q-antisymmetriser is in the radical.
2. `G` is **symmetric** — so `tr(T_w T_v) = tr(T_v T_w)` on a basis, hence
   `tr(xy) = tr(yx)` by bilinearity, hence the radical is a **two-sided**
   ideal: `tr((a x b) y) = tr(x (b y a)) = 0`.

### The identification is an ideal equality, not a numerical coincidence

`⟨E⟩ ⊆ radical` and `dim⟨E⟩ ≥ 588 ≥ dim radical`, so all are equal:

> **radical `= ⟨E⁽³⁾⟩`, as ideals**, measured at n = 3, 4, 5, 6.

`TL_n(q) := H_n(q)/⟨E⁽³⁾⟩` is the *definition* of the Temperley–Lieb quotient
(Jones), so the quotient by the radical **is** `TL_n` — not a corank number
that happens to agree with `n! − Catalan(n)`. As a by-product the probe
re-derives `dim TL_n = Catalan(n)` from the ideal side rather than assuming it.

### The two-sided part is load-bearing — and would have read as a refutation

Worth recording, because the cheaper argument fails. The **right** ideal
`Σ_b E_b H` needs no cyclicity, so it is tempting to stop there. Measured:

| n | 3 | 4 | 5 | 6 |
|---|---|---|---|---|
| right ideal `Σ_b E_b H` | 1 | 7 | 50 | 371 |
| two-sided `⟨E_b⟩` = corank | 1 | **10** | **78** | **588** |

The right ideal is short at every n ≥ 4. An agent who checked only the right
ideal would have concluded the TL identification fails at n = 4 and never
reached n = 6. The symmetry of `G` is what licenses the two-sided closure, and
it is checked exactly rather than assumed.

### Block arithmetic (hook-length formula, independent of any Gram computation)

`Σ (dim V_λ)²` over `λ ⊢ n` with **≥ 3 rows** equals `n! − Catalan(n)` at every
n tested, and over `λ` with **≤ 2 rows** equals `Catalan(n)`:

| n | ≤2-row λ (dim) | Σdim² | ≥3-row Σdim² |
|---|---|---|---|
| 3 | (3):1, (2,1):2 | 5 | **1** |
| 4 | (4):1, (3,1):3, (2,2):2 | 14 | **10** |
| 5 | (5):1, (4,1):4, (3,2):5 | 42 | **78** |
| 6 | (6):1, (5,1):5, (4,2):9, (3,3):5 | 132 | **588** |

So the measured coranks decompose consistently with "exactly the ≥3-row blocks
die". That the blocks of `TL_n` are the ≤2-row `λ` is classical TL structure
theory, **cited not measured**; the arithmetic above is the cross-check that
the measured numbers are compatible with it.

## Measured vs hypothesised — read this before citing

**Measured** (exactly, this probe): corank = 1, 10, 78, 588 at n = 3, 4, 5, 6;
generic in q; `radical = ⟨E⁽³⁾⟩` as ideals at those four n; the n = 3 radical
is the `(1³)` block; `(1ⁿ)` dies and `(n)` survives for n = 3…6; the right-ideal
dimensions 1, 7, 50, 371.

**Cited, not measured here**: `TL_n := H_n/⟨E⁽³⁾⟩` (Jones); the blocks of
`TL_n` are the ≤2-row `λ`; S2's `det G ≡ 0` over ℚ(q) and the `y_λ` values.

**Still hypothesised**: the identification **for all n**. Four points is four
points. A proof would go through the Ocneanu-trace weight formula — showing
`y_λ = 0 ⟺ λ has ≥ 3 rows` at `z_D = q³/(q²+1)` for general n — and is **not**
done here. Nothing in this document should be read as closing that.

No scope-(b) structural exclusion is claimed anywhere in this document, and
nothing is refuted; the one negative result (the right ideal is too small) is
scope-**(a)** — a statement about that construction alone, and specifically
*not* evidence against the TL identification, which the two-sided ideal
confirms.

## Consequence worth flagging: the form sees a vanishing fraction of `H_n`

`Catalan(n)/n!` collapses. The share of `H_n` annihilated by the trace form:

| n | 3 | 4 | 5 | 6 |
|---|---|---|---|---|
| dies | 16.7 % | 41.7 % | 65.0 % | **81.7 %** |

At n = 6 the Markov–Gram form retains 132 of 720 dimensions. Any compute that
treats `G` as a form on `H_n` — rather than on `TL_n` — is working almost
entirely in the kernel by n = 6, and it gets worse with n. S2 surveyed the
existing consumers (none arithmetic); this note is about *future* ones at
higher n.

## Provenance of the reused code

The probe carries a vendored copy of S2's builder, clearly delimited, and
*additionally* imports S2's module and cross-checks against it entry for entry
whenever that module is present. **#5185 has since landed on `main`
(`b7bc9cb2f8`), so both halves of that check now run**, and the results are
unchanged:

```
S2's module importable (lands with PR #5185): True
n=3 N=  6  identical=True  vs S2 module=True
n=4 N= 24  identical=True  vs S2 module=True
n=5 N=120  identical=True  vs S2 module=True
```

Before #5185 landed, only the vendored half could run, and the copy was
verified mechanically to be S2's code and not a paraphrase — AST-level
comparison of the 15 shared declarations:

- **14/15 byte-identical.** `QQ` differs only by two unused `staticmethod`
  lambdas (`add`, `mul`) that are dead in S2's source too.
- `slow_gram` vs S2's `gram`: rename `P → Pl`, an added docstring, and the
  removal of a dead local (`cur`, assigned and `del`'d, never read). No
  semantic difference.

That AST argument is now superseded by the direct comparison — it is recorded
because it is what licensed the n = 6 run at the time, not because the result
still depends on it.

**The vendored copy is not dead code and is not removed.** It supplies the
probe's whole arithmetic substrate (`QQ`/`GFp`/`SymQ`, `hmul`, `trace_table`,
`antisymmetriser`, and `slow_gram` itself), so the probe stays runnable
standalone; and `slow_gram` is the *independent reference* that `fast_gram` is
validated against. Deleting it would make the probe's correctness rest on a
module it does not own and would collapse a three-way agreement
(fast / vendored reference / S2's module) into a two-way one.

## Method

- **The cost wall dissolved.** S2's `gram()` is `O(n!²·|support|)` because it
  recomputes every product `T_w T_v`; it does not reach n = 6. Writing
  `ψ_w[v] := tr(T_w T_v)` for the w-th *row* gives
  `ψ_{w s_i} = L_iᵀ ψ_w` with `L_i` left multiplication by `T_{s_i}`, so the
  whole matrix costs `O(n!²)` — one `O(n!)` application per row. Exact ℚ Gram
  at n = 6 in **1.9 s** rather than never. Validated entry-for-entry against
  the reference builder at n = 3, 4, 5 *before* being used at n = 6.
- **No float64 anywhere.** Exact `Fraction` over ℚ, sympy over ℚ(q), integer
  arithmetic mod a prime. Where numpy appears it is `int64` exact modular
  arithmetic, never a float dtype. The prime is `2³¹−1` so `p² < 2⁶³` and every
  int64 product is exact rather than wrapped.
- **Modular arithmetic is used only for inequalities it always satisfies.**
  `rank_p ≤ rank_ℚ` for the rank bound; `dim_p(span) ≤ dim_ℚ(span)` for the
  ideal bound. Never as an approximation to a characteristic-0 answer. The
  second prime is a guard against a coding error in the elimination, not a
  rigour requirement — either prime alone suffices.
- **Specialisation is one-sided in the right direction too.** Rank at a
  rational `q₀` is `≤` the generic rank over ℚ(q), and the span of specialised
  vectors has dimension `≤` the generic span, so both measured bounds transfer
  to generic `q`.

## Verification

CI unavailable per AGENTS.md (Actions auto-triggers disabled repo-wide). No
Lean, no content blocks, and no witness files were touched, so no sidecar or
`#print axioms` gate applies. Verification is the probe itself: it runs to
completion in 39 s in exact arithmetic, carries its own assertions (it
`assert`s the fast/reference Gram agreement rather than merely printing it),
and every claim in this document is a line of its output, saved to
`tl-n6-discriminator.json`.
