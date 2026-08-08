# The bar-parity gate is vacuous on a one-dimensional HH¹ (2026-08-08)

**Bean:** `qou-jcmw` · **Tier:** exact symbolic (ℚ(i) + ℚ[x]/Φ₅) · **Wired:** nothing.
**No fit, no free parameter.** Producer:
[`hh1_bar_parity_is_not_an_invariant.py`](../../computations/hh1_bar_parity_is_not_an_invariant.py) ·
witness: `computations/hh1-bar-parity-not-an-invariant.witness.json`.

Completes the bean opened by
[`2026-08-08-qbeta-l2-assessment-post-week-landings.md` §5](2026-08-08-qbeta-l2-assessment-post-week-landings.md)
and continued in
[`2026-08-08-hh1-h5-bring-root-cocenter-action.md`](2026-08-08-hh1-h5-bring-root-cocenter-action.md).

**Result: the proposed gate cannot prune anything.** Not because the outer class
passes it — because bar parity is not a property of the class at all.

---

## 0. What was being asked, and why it was ill-posed

The 08-08 assessment set the test:

> *"test whether the outer class's action on the cocenter is **bar-odd**. If it is
> bar-**even**, the whole route dies to the same bar-parity invariant that killed
> the real resolvent."*

Parts 1–2 established `dim HH¹(H₅(ζ₅)) = 1` and that the class acts with rank 1
on the 7-dimensional cocenter. Part 3 could only measure a *sign-twisted* shadow
of bar, because over `F_p` the involution `q ↦ q⁻¹` has no home.

Done properly over `ℚ(ζ)`, the question dissolves: **a one-dimensional HH¹ has
generators of both parities.**

## 1. Bar really is an automorphism over ℚ(ζ) — the step F_p could not see

Over `K = ℚ(ζ)`, `bar : T_i ↦ T_i − a` together with `σ : ζ ↦ ζ⁻¹` is a
**σ-semilinear algebra automorphism of `A = H_n(ζ)` itself** — it maps `A` to
`A`, unlike over `F_p` where it maps `H_z → H_{z⁻¹}`. Applying it to the defining
relation and using `σ(a) = −a`:

```
(T_i − a)^2 − σ(a)(T_i − a) − 1  =  T_i^2 − a T_i − 1  =  0
```

Verified exactly in the producer (`M · σ(M) = I`, and `bar(B_i B_j) =
bar(B_i)·bar(B_j)` on all 36 basis pairs).

## 2. The argument

`bar` preserves `Der` and `Inn`, so it acts σ-semilinearly on `HH¹`. With
`dim_K HH¹ = 1`, write `[D^bar] = μ·[D]`. Applying `bar` twice:

```
D  =  bar^2 D bar^{-2}  =  σ(μ)·μ·D      =>      μ·σ(μ) = 1
```

`K/K^σ` is a quadratic extension, so **Hilbert 90** gives `μ = ν/σ(ν)`. Then:

| generator | parity |
|---|---|
| `ν·D` | **bar-even** |
| `a·ν·D` | **bar-odd** |

because `σ(a) = −a`. Both are generators of the *same line*. So parity is a
property of a **chosen generator**, not of the class — and on a one-dimensional
`HH¹` it carries no information.

**Free corollary.** Since `B·D₀·B⁻¹ = μ·D₀` is a scalar multiple, `im(D₀)` and
`ker(D₀)` are automatically **bar-stable**. The refined form of the question —
"does the outer class respect the bar-decomposition of `HH₀`?" — is therefore
also answered, affirmatively, with no computation.

## 3. Verification

The argument uses only three hypotheses: `dim HH¹ = 1`, `σ(a) = −a`, and
`K/K^σ` quadratic. It is uniform in `n`, so it was verified in **exact ℚ(i)
arithmetic on `H₃` at `q = i`** — 6-dimensional, every step checkable — rather
than asserted:

```
dim Der = 4   dim Inn = 3   dim HH^1 = 1                      ✓
sigma(a) = -a                                                 ✓
bar is an involution  (M . sigma(M) = I)                      ✓
bar is an algebra automorphism (all 36 basis pairs)           ✓
D^bar is again a derivation                                   ✓
[D^bar] = mu.[D]   with mu = 1,   mu.sigma(mu) = 1            ✓
Hilbert 90:  mu = nu/sigma(nu),  nu = 2                       ✓
  generator  nu.D    :  bar-even                              ✓
  generator  a.nu.D  :  bar-odd                               ✓
```

All three hypotheses hold for `H₅(ζ₅)`: `dim HH¹ = 1` was computed in part 1;
`σ(a) = −a` and `σ² = id` are verified **algebraically** in `ℚ[x]/Φ₅(x)` with
`σ : x ↦ x⁴` (going through `exp(2πi/5)` leaves sympy holding an unreduced
`conjugate(sin(2π/5))` and reports a spurious failure — noted because the first
run did exactly that); and `ℚ(ζ₅)/ℚ(√5)` is quadratic with `Gal = {1, σ}`.

## 4. Scope, and what this does and does not mean

**Scope-(b) — but about the GATE, not about the route.** Invariant cited: Hilbert
90 for `K/K^σ` together with `σ(a) = −a`. What is excluded is the *inference*
"the class is bar-even, therefore the route dies". That inference is unavailable,
permanently, for any one-dimensional `HH¹`.

**This neither advances nor refutes c₃.** It removes a proposed filter. The
surviving state of the route is unchanged from part 2:

- source object exists (`HH¹ = 1`), computed not assumed;
- it is trace-visible (`D₀ ≠ 0`, exact), so the `HH₀`/`HH¹` degree mismatch is
  not an obstruction;
- **no parity obstruction exists** (this document);
- and it is still true that nobody has shown the c₃ swing *is* this class, that
  the HH¹ modules were built for the P≠NP residue, and that `q₀ ≈ 1.10998` is not
  a root of unity — the target remains a Habiro-ring element evaluated at `q₀`.

Co-location is still not identification. What has changed is that the three cheap
ways of killing this lead are now all spent, so it has to be worked or left
alone on its merits.

## 5. Consequence for how parity gates are stated elsewhere

The bar-parity argument that *did* work — the real-`q₀` exclusion chain
(#4282/#4288/#4293), where a real, trace-built bar-**even** Gram resolvent cannot
carry the bar-**odd** `S` — is unaffected. There the objects compared are
*specific elements* with fixed normalisations, not generators of a line, so
parity is genuinely an invariant of what is being compared.

The lesson is narrow and worth recording: **a parity gate needs a canonically
normalised object.** Applied to a one-dimensional cohomology class it is vacuous,
and any future "is class X bar-odd?" test should first say what fixes X's scale.
If the normalisation would come from matching the c₃ magnitude, that is a fit and
is forbidden — which is the real reason this particular gate was never going to
work.
