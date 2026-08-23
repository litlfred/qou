# The bar involution is isospin conjugation

**Date:** 2026-08-19
**Bean:** `qou-e58e` (option D of the fibre workplan)
**Probe:** [`computations/substrate/bar_involution_is_isospin_probe.py`](../../computations/substrate/bar_involution_is_isospin_probe.py) — ASSERTIONS PASS
**Workplan:** [`2026-08-19-frakv-fibre-workplan-options.md`](2026-08-19-frakv-fibre-workplan-options.md)

Option D was opened to make `tr_M(q₀⁻¹)` computable, on the stated ground that
the canonical color-weighted atom word is `q₀`-baked and cannot re-lift. **That
premise was false**, and the work that replaced it produced a structural result
the corpus did not have.

---

## 1. The premise was false, and the false statement was load-bearing

`tr_m_atom_via_transfer.tr_m_atom_zn`'s docstring said two contradictory things
about the same function, thirty lines apart:

> *"the canonical color-weighted atom word is **q₀-baked** … passing `q ≠ q₀`
> with that convention raises `ValueError` (a true q-sweep needs a
> q-parameterised word builder)"*

> *"q-parameterised core: build the word AT q … so `q≠q₀` (e.g. `q₀⁻¹`,
> simulator N-grids) re-lifts cleanly instead of raising"*

The second is true. `tr_m_atom_zn(1, 1, q=1/q₀)` returns in **milliseconds**, and
12 of the deuteron word's 23 letters change under the substitution. The first
paragraph predated the q-parameterisation and was never updated.

This was not a cosmetic staleness. The sentence was read — by me, in the
predecessor audit — as evidence that the bar image is uncomputable, and a whole
workplan item was opened on it. Both sites are corrected in this commit.

A second, independent site said the same thing:
`complex_volume_witness.py`'s bar-norm guard cited that docstring as its reason
for returning `None`. **It is not the reason.** The `try`/`except` never fires;
what fires is `bar_prod > 0` failing, because

| quantity | value |
|---|---|
| `tr_M^atom(q₀)·tr_M^atom(q₀⁻¹)` | **−8.5174e-4** |
| `tr_M^free(q₀)·tr_M^free(q₀⁻¹)` | **−3.2974e-3** |

Both negative. So the "principled bar-norm mass modulus" is not *"not yet
computable"* — **as a real number it does not exist for this word**. That is a
stronger claim than the one the guard was making, and it should be recorded as
such rather than left looking like a tooling gap someone might close.

## 2. The Jones–Markov weights are exactly bar-even

Measured at five values of `q`, over all 11 partitions of 6:
`max |y_λ(q) − y_λ(1/q)| / |y_λ(q)| = 0` — bit-identical, not merely close.

The values do vary with `q` (`y₍₆₎` runs 0.1153 → 0.1630 → 0.3495 across the
grid), so this is bar-evenness, not a constant or a cache hit.

The reason is structural: `y_λ` is built from ratios of `q`-integers
`[k]_q = (q^k − q^{−k})/(q − q^{−1})`, whose numerator and denominator are each
bar-**odd**, so every such ratio is bar-**even**.

**Consequence.** No bar-odd material can enter `tr_M` through the Wedderburn
weights. All bar parity lives in the **word**. This generalises the
convention-D two-row observation (`y₍₃₎ = (q⁴+1)/(q²+1)²`,
`y₍₂,₁₎ = q²/(q²+1)²`, both manifestly bar-even) from `n = 3` to a measured
statement at `n = 6` with a reason that holds at every `n`.

## 3. The result: bar exchanges mirror nuclei

Write `L(Z,N; q) = ln(tr_M^free / tr_M^atom)` — the argument of the log-trace
binding `𝔈_bind = E₀·L`. Then

> **`L(Z, N; q) − L(N, Z; 1/q) = δ(q)`, with `δ` independent of `(Z,N)`.**

Measured over `A = 2 … 6`, both orientations of every mirror pair (11 nuclei),
at five values of `q`:

| `q` | `δ(q)` | spread over nuclei |
|---|---|---|
| `q₀` | 3.2828999269244323183e-5 | 7.9e-24 |
| `1+π/30` | 2.6018423704218041749e-5 | 6.6e-24 |
| `√5/2` | 4.5864264788095878698e-5 | 1.6e-22 (well-conditioned subset) |
| `√2/1.1` | 2.5986147556136785145e-3 | 5.5e-30 |
| `e^{1/3}` | 1.0437444437813325899e-2 | 2.4e-30 |

So on the canonical color-weighted convention, **`q ↦ q⁻¹` acts as
proton↔neutron conjugation**, exactly, up to one universal `q`-dependent offset.
Self-mirror nuclei (`Z = N`) are bar-even up to `δ`; mirror pairs map to each
other. ³H at `q₀` and ³He at `q₀⁻¹` agree to 22 digits after subtracting `δ`.

**Conditioning, stated rather than hidden.** `L` is a log, so a nucleus whose
`tr_M` sits near a zero at the bar image has an ill-conditioned `L`. At `q = √5/2`
five of the eleven nuclei have `|tr_M(1/q)|` down to 8.9e-18 and their deviations
rise to 5.3e-16 accordingly. The probe asserts strictly on the well-conditioned
subset and reports the rest with `|dev|·|tr_M|min` bounded by 1e-25 (measured
range 3e-30 … 3e-27). That product spans three decades, so it is a **bound**, not
a sharp `1/|tr_M|` scaling law, and the probe says so. Raising `mp.dps` does not
help — the values are bit-identical at 60 and 140 dps, so the precision cap is
internal to the transfer path, which is worth knowing independently.

## 4. How big is `δ`, and why it matters

`δ(q) = O(h⁵)` with `h = q − q⁻¹` — the mirror asymmetry vanishes to fifth order
at the classical point. At the substrate anchor:

- `δ(q₀) = 3.2829e-5`
- `L(deuteron; q₀) = 0.67682`
- **relative: 4.85e-5**

The L2 100× target for `Q_β` is 7.8 ppb. **`δ/L` is 6219× that target.** The
mirror asymmetry is therefore not a negligible correction at the precision the
framework aims for — it is four orders of magnitude above the target for the
observable it most plausibly bears on.

**Not identified.** `δ/h⁵` is 0.0822 at `q₀` but 0.0723 by `q = 1.396`, so `h⁵` is
the leading *order* only. No closed form is asserted; naming a constant against
this five-point sample would be a fit, and the corpus forbids it.

## 4b. Where `δ` lives: an exact extensive/intensive split (added on the second pass)

Asked to try for `δ`'s closed form. I did not get it. What the attempt produced
instead is the structure, exactly — and a named blocker.

**Symbolically, the interface letter is the sole bar-parity defect.** The word
builder *is* fully symbolic (sympy), and every letter of the atom word is
exactly bar-odd — `d(1/q) = −d(q)` — for `d ∈ {0, −h, −h/2}`. The one exception
is the color-weighted interface letter `d = −h·(½ − f/4)`, `f =
flavor_split_leading`. Because `f(1/q) = −q²·f(q)` (exact) the `f`-part does not
flip sign along with `h`, leaving

```
d(q) + d(1/q)  =  (q−1)⁴ (q+1)² (q²+1)² / (12 q⁵)
```

fully factored, manifestly positive for `q > 0`, vanishing to fourth order at
`q = 1`. Sympy-verified against `h·f·(q²+1)/4`.

The interface letters are also **exactly what distinguishes the atom word from
the free word**. So the atom/free asymmetry and the bar-parity defect have the
same support — which is why `δ` is a property of the interfaces and of nothing
else.

**The split is exact, and it is extensive vs intensive.** Summing
`ln|tr_M(Z,N;q)/tr_M(N,Z;1/q)| / ln q` over a mirror pair:

| `A` | `S_free(A)` | first difference | `S_atom − S_free` |
|---|---|---|---|
| 2 | 114.28105868230766694 | — | −0.00062926533703645 |
| 3 | 171.42158802346150041 | 57.1405293411538335 | −0.00062926533703645 |
| 4 | 228.56211736461533389 | 57.1405293411538335 | −0.00062926533703645 |
| 5 | 285.70264670576916736 | 57.1405293411538335 | −0.00062926533703645 |
| 6 | 342.84317604692300083 | 57.1405293411538335 | −0.00062926533703645 |

- The first difference is **constant to 3.6e-24**, so `S_free(A) = A·c(q)` is
  *measured*, not fitted — no two-parameter form was ever solved for. And the
  residual `max|S_free(A) − A·c|` is **3.4e-24**, i.e. there is **no constant
  term**: the free channel's mirror log is **purely extensive**.
- The atom channel obeys the same extensive law **minus a purely intensive
  constant** `2δ`, identical at every `A` (spread 6.0e-23).

That is the same extensive/intensive language the `Δ_λ` magnitude problem is
stated in — where the missing object is likewise *"a separate additive extensive
term"* rather than a per-block weight. Here the separation is exact and measured.

**Still open, and not explained.** ~~The *number* of interface letters grows with
`A`, yet `δ` does not.~~ **Retracted in §4d** — there is exactly **one** interface
letter at every `A`; I had miscounted. The `A`-independence needs no such
explanation.

**The blocker for the symbolic route, named.** `chi_monotone_transfer.word_to_mpfr`
calls `float(h)` — not as a computation (precision is fine; it rebuilds `d` at
full dps afterwards) but as a **template classifier**, matching each letter
against `σ / σ⁻¹ / averaged / color-weighted`. That `float` is what refuses a
sympy symbol, so `chi_all_lambda_reduced_block` — and therefore the whole trace
— cannot be evaluated symbolically. The word builder is symbolic; the transfer
is not. Making the classifier structural rather than numeric would open the
symbolic derivation of `δ`, and is the concrete next step.

**A refuted guess, recorded.** I expected `q ↦ 1/q` to act as the conjugate
partition `λ ↦ λ′` (the standard `H_n(q) ≅ H_n(q⁻¹)` fact). For the self-mirror
deuteron the per-`λ` ratios are all ≈ −1 (defect 1.6e-4 … 1.8e-3), so the shape
is right there — but at `n = 9` they scatter (−0.66, −0.70, +1.08, +3.47). **The
naive per-`λ` conjugation law is refuted as stated**; it cannot be the mechanism,
since `y_λ ≠ y_{λ′}` anyway and the sum would not transform cleanly.

## 4c. `δ` in closed form — derived (third pass)

The previous pass named a blocker and said fixing it was what stood between here
and a derived `δ`. It was fixed (bean `qou-j320`, two edits), and `δ` followed
immediately.

### The two edits

1. **`chi_monotone_transfer.word_to_mpfr`** — a symbolic word already carries its
   `d` exactly at the requested `q`, so there is nothing to re-identify and
   nothing to re-lift: pass it through. The numeric branch is untouched, and
   `tr_M` at `q₀` and at `q₀⁻¹` is **bit-identical** before and after (checked to
   30 digits).
2. **`wedderburn_jones_markov.y_lambda_at`** — a symbolic `q_val` fell through to
   the numeric branch and died inside mpmath with *"invalid literal for int()
   with base 10: 'q'"*, even though the exact convention-D solver was already
   wired for `q_val=None`. Symbolic `q_val` now reaches it. The numeric branch is
   unchanged and the two agree at `q₀`.

Both also removed `mp.mpf(0)`/`mp.mpf(1)` seeds in favour of exact Python ints —
identical for any numeric `q` (an int is exact and mpmath promotes it
losslessly), but an `mpf` seed drags a sympy product into `Float` contagion, the
same trap `flavor_split_leading`'s own docstring documents.

The symbolic weights come out as convention D exactly, which is an independent
check on the plumbing: `y₍₃₎ = (q⁴+1)/(q²+1)²`, `y₍₂,₁₎ = q²/(q²+1)²`,
`y₍₁,₁,₁₎ = 0`.

### The result

Tracing the deuteron word symbolically:

```
tr_M^free / tr_M^atom  =  12 q⁵ (q²+1) / P(q)

P(q) = q¹⁰ − 2q⁹ + 7q⁸ − 2q⁶ + 4q⁵ + 4q⁴ + q² − 2q + 1        (irreducible /ℚ)
```

and therefore

> **`exp(δ(q)) = q¹² · P(1/q) / P(q)`**

Checked against all five independent numeric measurements of §3 — agreement
1e-29 … 2e-23 relative, which is the transfer path's own floor. **Nothing was
fitted**: this is the symbolic value of the trace.

### Two things that were open one pass ago

**(a) The order is derived, not measured.** Exactly

```
q¹² P(1/q) − P(q)  =  (q−1)⁵ (q+1)³ (q²+1)²
```

so `δ` vanishes to order **exactly 5** at `q = 1`, and

```
lim_{q→1} δ / h⁵  =  1/12        (exact)
```

The previous pass measured `δ/h⁵ = 0.0822` at `q₀` drifting to `0.0723`, and
declined to name a constant on the grounds that naming one would be a fit. That
was the right call and it is now superseded properly: the limit is `1/12`, the
drift is subleading terms, and `0.0822` vs `0.0833` at `q₀` measures their size.

**(b) The interface defect is the source, with an explicit factor.** With
`Δ_int = d(q) + d(1/q)` the interface bar-defect of §4b,

```
q¹² P(1/q) − P(q)  =  12 q⁶ h · Δ_int          (exact)
```

So `δ`'s numerator **is** the interface defect, times `12 q⁶ h`. §4b's claim —
that `δ` is generated by the single non-bar-odd letter — becomes an identity
rather than an inference, and the `12` is the same `12` in `Δ_int`'s denominator
and in `R`'s numerator.

### Nucleus-independence, now visible rather than observed

Symbolically, for every nucleus checked,

```
R(Z,N; q)  =  12 · q^{a(Z,N)} · (q²+1)^{b(A)} / P(q)
```

with the **same** `P` at `n = 6`, `9` and `12`. All the nucleus dependence sits in
the monomial prefactor:

| nucleus | `n` | `a` | `b` | `a + a′ + 2b` |
|---|---|---|---|---|
| `(1,1)` | 6 | 5 | 1 | 5 + 5 + 2 = **12** |
| `(1,2)` / `(2,1)` | 9 | 6 / 2 | 2 | 6 + 2 + 4 = **12** |
| `(2,2)` | 12 | 3 | 3 | 3 + 3 + 6 = **12** |

The mirror-crossed ratio contributes `q^{a + a′ + 2b}`, and that exponent is `12`
in every case while `P` is universal. **That cancellation is the `A`-independence
of `δ`** — the open item of §4b, `qou-kgsx`. It is no longer a puzzle about
growing interface counts: the interface count enters only through `a` and `b`,
and their mirror sum is constant.

### Caveat: which trace path all of this is on

Every number in this audit is computed through
`tr_m_atom_via_transfer.tr_m_atom_zn`. While verifying the §4c edits I found
that path's committed witness is **stale** (bean `qou-r9dv`, *not* caused by the
edits — it reproduces on a clean tree):
`tr-m-atom-via-transfer.witness.json` records `passed: true` against
`tr_M^atom(D) = 0.388357`, a value **neither live path produces**, and records a
`passed: false` that current code passes.

The live paths do agree with each other:

| path | `tr_M^atom(D)` |
|---|---|
| `tr_m_atom_via_transfer` (used here) | 0.57517224391777187083 |
| `canonical_tr_m_via_branching` | 0.57509087229027536125 |
| committed witness / hardcoded expectation | 0.3883571225623529 ← neither |

So the conclusions here are unaffected — 1.4e-4 relative between the two live
paths, and the `δ` derivation is a symbolic identity *of the transfer path*
cross-checked against five independent numeric evaluations of that same path.
But the 1.4e-4 is itself worth a second look: both are described as lossless
50-dps computations of the same object and should agree at the 50-dps floor, not
the fourth digit. Which is canonical is not decided here.

### What is still not claimed

- `P` is irreducible over `ℚ` and I have **no structural interpretation of it** —
  it is the symbolic trace, correct and verified, but not *explained*. Where its
  coefficients `(1, −2, 7, 0, −2, 4, 4, 0, 1, −2, 1)` come from is open.
- Why `a + a′ + 2b = 12` universally is verified at three `n`, **not proved**. A
  general-`A` argument is the natural next step and would close `qou-kgsx`
  outright rather than at three points.
- None of this derives `Im 𝔙`, and none of it identifies the mirror difference
  with `Q_β`. §5 stands unchanged.

## 4d. General `A` — the product formula, and a correction to §4b

§4b called this the real open step:

> *"the **number** of interface letters grows with `A`, yet `δ` does not …
> That is the missing step."*

**That premise is false.** Censusing the words by letter type, every atom word
carries **exactly one** color-weighted p–n interface, at every `A`. The bond
census, verified on 16 nuclei up to `A = 10`:

| | count |
|---|---|
| p–n interface (the one non-bar-odd letter) | **1**, always |
| p–p bonds (`d = 0`, plain `σ`) | `Z − 1` |
| n–n bonds (`d = −h`, `σ⁻¹`-like) | `N − 1` |
| **total bonds** | `A − 1` |

Both bond types are *exactly* bar-odd (`0 → 0` and `−h → +h`), so they contribute
nothing to `δ`. **`δ` is `A`-independent for the plain reason that its sole source
occurs once, however many nucleons there are.** There was no puzzle; I had
miscounted, and the bean opened on that miscount (`qou-kgsx`) is answered by
correcting it rather than by solving it.

### The product formula

```
tr_M^free / tr_M^atom  =  (12 / P(q)) · (q + q⁻¹)^{A−1} · q^{6 + 2(N−Z)}
```

Worst `|ratio − 1|` over 16 nuclei, `A = 2…10`: **4.5e-31** — the transfer path's
own floor (§4b), not a mismatch.

Each factor does one job, and each earns its place in `δ`:

- **`(q + q⁻¹)^{A−1}`** — one Cayley–Hamilton denominator per bond, and there are
  exactly `A − 1` bonds. `q + q⁻¹` is **bar-even**, so it *cancels* between
  `R(Z,N;q)` and `R(N,Z;1/q)`. **That cancellation is the `A`-independence of `δ`.**
- **`q^{6 + 2(N−Z)}`** — a pure **isospin** monomial. Mirror-crossing gives
  `q^{6+2(N−Z)} / q^{−6−2(Z−N)} = q^{12}`: the isospin dependence cancels and
  leaves exactly the `12`. **The `12` is `2 × 6`** — twice the isospin-neutral
  exponent.
- **`P(q)`** — universal, so it contributes `P(1/q)/P(q)` and nothing else.

Multiplying the three,

> `exp(δ(q)) = q¹² · P(1/q) / P(q)` **for every `(Z,N)`**

no longer three checked points but an identity, given the product formula.
§4c's closed form is now general, and the earlier exponent bookkeeping
(`a = 7 − 3Z + N`, `b = A − 1`, `a + a′ + 2b = 12`) is the same statement in
less transparent coordinates: `a = 6 + 2(N−Z) − (A−1)`, where the `−(A−1)` is
just the `q` in each bond's `(q²+1)/q`.

### Symbolic confirmation, not only numeric

Five nuclei were also run through the (now unblocked) **symbolic** trace, which
returns `R` as an exact rational function. Every one lands on the predicted
monomial, and the mirror-crossed ratio is `q¹² P(1/q)/P(q)` **symbolically**, not
to a tolerance:

| nucleus | `n` | `R · P / 12` | predicted `q^a (q²+1)^b` | mirror ratio `= q¹²P(1/q)/P(q)` |
|---|---|---|---|---|
| `(1,1)` | 6 | `q⁵(q²+1)` | `a=5, b=1` | ✓ |
| `(1,2)` | 9 | `q⁶(q²+1)²` | `a=6, b=2` | ✓ |
| `(2,1)` | 9 | `q²(q²+1)²` | `a=2, b=2` | ✓ |
| `(2,2)` | 12 | `q³(q²+1)³` | `a=3, b=3` | ✓ |
| `(1,3)` | 12 | `q⁷(q²+1)³` | `a=7, b=3` | ✓ |
| `(3,1)` | 12 | `(q²+1)³/q` | `a=−1, b=3` | ✓ |

Both orientations of the `A=4` mirror pair are included, which is the case that
matters: the exponents differ (`7` vs `−1`) and the mirror-crossed result is
identical.

### What is still not derived

- ~~**The product formula is verified, not proved.**~~ **Derived in §4f** from a
  single rule; what remains is that rule itself, stated there. The bond count and the one-`(q+q⁻¹)`-per-bond factor follow from the
  Cayley–Hamilton reduction in `_alpha_beta`; the isospin exponent `6 + 2(N−Z)`
  is measured, not derived.
- ~~**`P` remains uninterpreted.**~~ **Identified in §4f**:
  `P = 12 q⁵ (q²+1)(z + d_iface)`, the interface's Markov weight with
  denominators cleared. The §4e literature question is withdrawn.

## 4e. The bond factors are Markov parameters; and what `P` is not

### The per-bond factors are `z` and its bar image

Convention D's Markov parameter is `z = q³/(q²+1)`, and its bar image is
`z̄ = z(1/q) = 1/(q(q²+1))`. Against the product formula of §4d:

| bond | factor in `R = tr^free/tr^atom` | identification |
|---|---|---|
| p–p (`d = 0`, plain `σ`) | `(q²+1)/q³` | `1/z` |
| n–n (`d = −h`, `σ⁻¹`-like) | `q(q²+1)` | `1/z̄` |
| p–n interface | `q⁵(q²+1)` | `q⁴/z̄` |

and the `Z`, `N` dependence **cancels out of the interface factor** — it is
`q⁵(q²+1)` for every nucleus, which is what makes it a constant rather than a
third `A`-dependent term.

This is what makes the isospin reading more than a slogan: **`p ↔ n` under the
bar involution is exactly `z ↔ z̄`.** The p–p bond carries the Markov parameter,
the n–n bond carries its bar image, and conjugating `q ↦ q⁻¹` swaps them — which
is the same statement as §3's mirror-nuclei exchange, now at the level of the
individual bond rather than the whole trace.

### The interface's eigenvalue sum *is* the p–n mass split

For the single interface letter `σ + d·I` the Cayley–Hamilton data is trivial
(`α = 1`, `β = d`), but the eigenvalue **sum** is not:

```
E₁ + E₂  =  (q + d) + (−q⁻¹ + d)  =  h · f / 2
```

exactly, where `f = flavor_split_leading = (q−1)²(1−q⁻⁴)/3` — the p–n mass split
itself. So the bar-defect of §4b is `Δ_int = (q²+1)(E₁+E₂)/2`: the quantity that
breaks bar symmetry is the flavour split, directly, with no intermediate step.

### `P(1) = 12`

The `12` in the numerator of the product formula is not a free constant — it is
`P(1)`. Hence `R(1) = 1`, i.e. `tr^free = tr^atom` at the classical point, i.e.
**zero binding at `q = 1`**, which is the right answer and is now a consequence
rather than an input.

### Why `P` probably has no knot-theoretic name

`P` is irreducible over `ℚ` and has no real roots (all ten come in complex
conjugate pairs). The natural guess — that it is the HOMFLY or Jones polynomial
of some link — runs into a structural objection: **the interface letter is
`σ + d·I`, which is not a braid generator.** The atom word is therefore an
element of the Hecke *algebra*, not of the braid group, and `tr_M` of it is not a
link invariant. Markov traces of genuine braids are well covered in the library
(Orellana on the weights of Markov traces; Geck–Lambropoulou for type B; Birman
on Markov's theorem; Webster–Williamson on the geometry of the Jones–Ocneanu
trace) — none of that reaches an inhomogeneous `σ + d·I` word.

So `P` stays open, and the honest form of the literature question is narrower
than "what is this polynomial": it is *"is there a treatment of Markov traces of
Hecke-algebra elements with one non-group-like letter?"* — which the library, as
scanned, does not appear to hold.

## 4f. The product formula derived, and `P` with it — `qou-kgsx` closed

Both items §4d left open turn out to be one item, and it is a single rule.

### One rule

> **A letter `σ + d·I` contributes `z + d` to `tr_M^atom / tr_M^free`**, with
> `z = q³/(q²+1)` the convention-D Markov parameter.

It reproduces all three bond types, and the middle one is not a fit:

| bond | `d` | `z + d` | |
|---|---|---|---|
| p–p | `0` | `z` | |
| n–n | `−h` | `z − h = z̄` | **exactly** the bar image, `9.1e-72` |
| p–n | `d_iface` | `z + d_iface` | |

So the entire product formula of §4d is

```
tr_M^free / tr_M^atom  =  ∏_{bonds b}  1 / (z + d_b)
```

Worst `|ratio − 1|` over 16 nuclei, `A = 2…10`: **4.45e-31**, the transfer's own
floor.

### `P` is the interface's Markov weight

```
P(q)  =  12 · q⁵ · (q²+1) · (z + d_iface)        (symbolically verified)
```

`P` is not a link polynomial and needs no knot-theoretic name — §4e's objection
was right for the right reason, but the conclusion "open" was premature. The
`12` and the `q⁵` are exactly the clearing of denominators; `P(1) = 12` follows.
**The literature question of §4e is withdrawn: nothing needs looking up.**

### Nucleus-independence in one line

Since `z(1/q) = z̄`, and the mirror swaps the p–p and n–n bond counts while the
bar swaps `z` and `z̄`:

```
R(Z,N; q)    =  1 / [ z^{Z−1} · z̄^{N−1} · (z + d) ]
R(N,Z; 1/q)  =  1 / [ z̄^{N−1} · z^{Z−1} · (z̄ + d̄) ]
──────────────────────────────────────────────────────
exp(δ)       =  (z̄ + d̄) / (z + d)
```

The `z^{Z−1} z̄^{N−1}` **cancels identically** — the two swaps undo each other. So
**`δ` depends only on the single p–n interface**, and nucleus-independence is
immediate. The exponent bookkeeping of §4c–§4d (`a = 7−3Z+N`, `b = A−1`,
`a + a′ + 2b = 12`) was never needed; it was the same statement in coordinates
that hid the cancellation.

Verified symbolically: `(z̄ + d̄)/(z + d) = q¹² P(1/q)/P(q)`.

### The remaining rigor gap, stated precisely

The rule `tr(x·(σ + d·I)) = (z + d)·tr(x)` is **verified, not proved from
Markov's theorem** — 16 nuclei numerically, 6 symbolically. These bond generators
are *not* the last-strand generator Markov's theorem addresses, so the rule has
the *form* of the Markov property without being an instance of it. That is the
entire remainder, and it is a much smaller object than what §4b started with.

## 5. What this does and does not say about `conj:binding-qbeta-complex-volume`

The conjecture assigns the bar-even channel to binding (`Re 𝔙`) and the bar-odd
channel to `Q_β` (`Im 𝔙`). The result above says the bar-odd partner of the
bar-even binding is the **mirror-pair difference** — and ³H → ³He *is* a β decay.
The channel the conjecture assigns to `Im 𝔙` is exactly the channel the bar
involution turns out to generate.

That is a **consistency, not a derivation**, and the distinction is the whole
point of recording it carefully:

- Nothing here derives `Im 𝔙`. `complex_volume_witness.py` still **assigns** it
  from `q_beta_substrate`.
- The identification of the mirror difference with `Q_β` is **not made**. The
  free-neutron `Q_β` (0.784 MeV) and the ³H→³He `Q`-value (18.6 keV) are
  different numbers; relating them needs an argument this probe does not have.
- The observable-level degeneracy is untouched: `Im(q₀) = 0` still gives
  `Im 𝔙 ≡ 0` after `τ`.

What it does change is the workplan. Option D was scoped as compute-engineering
to unblock bar-parity checks. The unblocking was already done; what the checks
then showed is that **bar has a meaning on these words** — isospin conjugation —
which is a structural input the other options can use, and which nothing in the
corpus stated.

## 6. Follow-on

1. **Formalize the mirror law**, together with the §4b split: `S_free(A) = A·c(q)`
   exactly, `S_atom = S_free − 2δ` exactly, and the interface defect
   `(q−1)⁴(q+1)²(q²+1)²/(12q⁵)`. The last is already a sympy-verified identity
   and is the easiest of the three to state in Lean.
2. **Unblock the symbolic route** by making `word_to_mpfr`'s template match
   structural instead of `float`-based (§4b). That is what stands between here
   and a derived `δ`; identifying `δ` from the numeric sample instead would be a
   fit.
3. ~~**Explain the `A`-independence** of `δ` against a growing interface count.~~
   **Answered in §4d by correcting the count** — there is one interface letter at
   every `A`. What remains is proving the product formula from the transfer, and
   interpreting `P`.
4. **Re-scope the four bar-oddness sites** (`qou-sglq`) with this in hand: the
   supporting quantity *is* computable, and what it shows is a mirror law, not
   the bar-oddness those sites assert.
5. **The bar-norm claim should be retired, not repaired.** It is negative.

## What this audit did not do

- It did **not** identify `δ(q)`. The second pass tried and failed; §4b records
  the structure it got instead, the blocker that stopped it, and a refuted guess.
  No basis was scanned, and no two-parameter form was solved for — the affine law
  in §4b is a constant first difference, which is a measurement.
- It did **not** derive `Im 𝔙`, nor connect the mirror difference to `Q_β`.
- It did **not** re-run or refresh `complex-volume-unification.witness.json`.
  The edit there is comment-only and every emitted number is byte-identical; a
  regeneration in this container drops `scipy` and `clarabel` from the
  environment block, trading a richer provenance record for nothing. The
  `scriptHash` drift is accepted and noted here instead.
