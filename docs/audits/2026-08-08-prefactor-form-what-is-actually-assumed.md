# The prefactor form: the ledger names the wrong thing, and two registered references were never consulted

**Date:** 2026-08-08 · **Beans:** `qou-fl4t`, `qou-pn5j`
**Amends:** `docs/audits/2026-08-08-c-sigma-derivation-status.md` §"THE ONE ASSUMPTION BEING CARRIED"
**New probe:** `computations/probes/one_loop_prefactor_exponent_probe.py`

## What was asked

`c_σ = 2^{−3/4}` was upgraded to DERIVATION carrying exactly one stated
assumption:

```
c_σ  ∝  |τ|^{−1/2}
```

described as "the standard GGMW/Ohtsuki saddle-point form … validated here, not
proved", with the closing note that *"proving it for links is the real remaining
gap, and it is a research problem, not a computation."*

That framing is right about the gap and wrong about where it sits.

## Finding 1 — the exponent was never the assumed part

Every validation in this arc computes

```
k_c := c_σ · |τ|^{1/2}
```

and checks that `k_c` agrees across manifolds. That test looks like it holds the
exponent fixed and measures `k`. Algebraically it does both at once, because for
any **pair** of manifolds

```
k_i = k_j   ⟺   log c_i + ½ log τ_i = log c_j + ½ log τ_j
            ⟺   (log c_i − log c_j)/(log τ_i − log τ_j) = −½
            ⟺   p_ij = −½
```

`k`-constancy and `p = −1/2` are **the same statement** on a pair. So the
exponent was pinned, to 17 digits, by data already in the corpus — the
`k_1 = k_2` agreement (rel diff 4.5e−18) *is* the measurement `p_{4_1,L5a1} =
−1/2`. Nobody read it that way, and the ledger consequently lists as "assumed"
something the data determines.

The new probe reports this explicitly as a re-expression, **not** as fresh
confirmation, because counting it twice would be the error this note exists to
prevent.

### What is genuinely new: the four-point fit

Four manifolds have `c_σ` determined independently of `τ` — `4_1`, `L5a1`,
`L6a4` from colored-Jones asymptotics, and `5_2` from Ohtsuki's Theorem 1.1.
With `p` and `k` both free that is 4 points against 2 parameters, leaving **2
residual degrees of freedom** — a test that can fail, which no pairwise identity
can be:

```
p = −0.498296258234        (predicted exactly −1/2)
k =  0.706990301516        (predicted 2^{−1/2} = 0.707106781187)
rms residual in log c_σ = 3.0e−4
```

Pairwise, over ~1 decade of `|τ|`:

| pair | p | \|p + ½\| |
|---|---|---|
| 4_1 vs L5a1 | −0.500000000000000009 | 9.2e−18 |
| 4_1 vs 5_2 | −0.500000000222371784 | 2.2e−10 |
| 5_2 vs L5a1 | −0.499999999669222325 | 3.3e−10 |
| 4_1 vs L6a4 | −0.498433015714425735 | 1.6e−3 |
| 5_2 vs L6a4 | −0.498194915333422998 | 1.8e−3 |
| L5a1 vs L6a4 | −0.497989547409452082 | 2.0e−3 |

The whole residual is L6a4, whose own witness already flags an unresolved
normalisation+cusp offset and returns `p = 1.4993` against an exact `3/2`
elsewhere. It is not evidence against `p = −1/2`.

### So the ledger should read

The single line "the prefactor form is assumed" is **two** statements with
different status:

* **the exponent `−1/2`** — pinned by existing data; not an assumption;
* **that `c_σ` is a function of `τ` alone** — genuinely assumed, and the
  load-bearing part.

A law `c_σ = k·|τ|^p·f(M)` with `f` weakly varying fits four points as well as
`f ≡ 1` does. Nothing in the corpus excludes it. **That** is the open problem,
and it is a smaller and better-shaped target than "the prefactor form".

## Finding 2 — two registered references bear on this and are cited by no audit

A survey of the reference ledger turned up material the `c_σ` audits never
reach for. Reporting what the registrations say; **none of these PDFs was read
here**, and the corpus's own notes say several were never read at all.

### Ohtsuki–Takata 2015 — may already be the `c = 1` prefactor form

`content/schema/references.ts:170` (`ohtsuki-takata-2015`, Geom. Topol. 19
(2015) 853–952) is registered with this note:

> "The second coefficient of the Kashaev-invariant asymptotic expansion of a
> two-bridge knot is a constant multiple of the square root of the twisted
> Reidemeister torsion at the holonomy representation"

If that paraphrase is accurate, it is the prefactor form for two-bridge knots —
i.e. the `c = 1` leg is **theorem-backed**, not merely "validated on `4_1` to 17
digits". No `c_σ` audit cites it. All four (2026-08-02 ×2, 2026-08-07,
2026-08-08) say the form is standard-but-unproved and reach only for
Garoufalidis–Yoon, which proves a *different* statement (1-loop = adjoint
torsion).

**Two reasons not to bank it yet**, both from the corpus's own record:

1. The registration says `DOI follows the msp.org pattern, PDF not read
   in-sandbox`, and there is no Ohtsuki–Takata file in `library/`.
2. The paraphrase says *square root of the torsion* — `τ^{+1/2}` — while the
   form in use is `|τ|^{−1/2}`. That is a sign discrepancy in the exponent. It
   is very likely a torsion-vs-inverse-torsion normalisation convention, which
   is exactly the kind of thing this corpus has been bitten by before, and it
   cannot be waved through from a bibliography note.

**Action:** obtain the paper and check the exponent convention. If it holds, the
`c = 1` leg upgrades from validated to proved and the open problem narrows to
links alone.

### Pandey–Wong 2023 — a *link* theorem the later audits do not mention

`references.ts:158` (`pandey-wong-2023`, arXiv:2308.06643):

> "Proves the Dimofte–Garoufalidis 1-loop conjecture for fundamental shadow
> link complements — which include the Borromean rings"

Two Borromean probes (`borromean_jones_1loop_torsion.py:50`,
`borromean_nz_adjoint_torsion.py:82`) call the reading "theorem-backed" on this
basis. Yet `2026-08-07-one-loop-multicusp-derivation.md:157` and
`2026-08-08-c-sigma-derivation-status.md:102` both state flatly that no theorem
covers the link case, citing only Garoufalidis–Yoon.

These are reconcilable — Pandey–Wong would cover `τ_DG = τ_adj` for links, while
nothing covers `c_σ ∝ |τ|^{−1/2}` for links — and that is probably the right
reading. But **no file says so**, and one part of the corpus calling a link
result theorem-backed while another says no link theorem exists is precisely the
sibling-file contradiction this arc has hit three times already. It should be
stated once, explicitly, wherever "no theorem covers links" appears.
`2308.06643` is also not in `library/` and its registration came from the
Garoufalidis–Yoon bibliography rather than a read.

### DGLZ — downloaded, registered, and cited nowhere

`library/arxiv-0903.2472v1/0903.2472v1.pdf`, Dimofte–Gukov–Lenells–Zagier, *Exact results for
perturbative Chern-Simons theory with complex gauge group*. Registered at
`references.bib:3975` with the note "1-loop / torsion identification from the
physics side."

That single bib entry is its **only occurrence in the repository**. It appears
in no audit, probe, bean, or Lean file. This is the canonical physics origin of
the `1/√torsion` one-loop term — the thing the audits gesture at when they say
"the standard GGMW/Ohtsuki saddle-point form" — and it is sitting unread in
`library/`.

**This is the cheapest available move on the open problem.** Before treating the
τ-alone dependence as a research problem, read the paper the form is
attributed to and find out what it actually derives and under what hypotheses.

## ADDENDUM — DGLZ was read: it supplies the form, not the constant

Recommendation 1 below was "read `library/arxiv-0903.2472v1/0903.2472v1.pdf`". Done.

Read it in two passes and the two passes disagreed, so the order matters here.
The first pass produced the paragraph immediately below and a claim that the
constant came free with it; the second pass, prompted by the question *"do we
want that `/2` for arbitrary characteristic?"*, showed the constant is
convention. Both are kept, in that order, because the correction is the point.

**DGLZ eq (2.1)/(2.3).** They expand the perturbative Chern–Simons partition
function as

```
Z^(ρ)(M; ħ) = exp( S₀/ħ − ½ δ log ħ + Σ_{n≥0} S_{n+1} ħⁿ )        (2.1)
```

and identify the one-loop coefficient with the Ray–Singer torsion of `M` twisted
by the flat bundle `E_ρ`:

```
S₁^(ρ) = ½ log( T(M; E_ρ) / 2 )                                    (2.3)
```

so the one-loop factor is `exp(S₁) = (T/2)^{1/2} = 2^{−1/2}·T^{1/2}`.

**~~The "calibrated" constant is the `/2` in their logarithm.~~ RETRACTED — see
the correction below.** That was written before reading far enough, and it is
wrong. The constant is a normalisation choice in DGLZ too.

**The exponent sign was a variable choice.** DGLZ carry `T^{+1/2}`, the corpus
`|τ_DG|^{−1/2}`. They agree exactly when `T = 1/|τ_DG|`, verified numerically:

| manifold | rel. deviation of `(c_σ√2)² ` from `1/|τ_DG|` | role |
|---|---|---|
| 4_1 | 9.1e−18 | calibration point — **not** evidence |
| 5_2 | 1.3e−10 | independent (Ohtsuki's theorem) |
| L5a1 | 6.2e−21 | independent (20-digit measurement) |
| L6a4 | 7.0e−3 | supporting only (known offset) |

With *nothing* calibrated, `c_σ = (1/(2|τ_DG|))^{1/2}` straight from eq (2.3) is
a zero-parameter prediction, matching the independently measured `c_σ` to
6.5e−11 on `5_2` and 3.1e−21 on `L5a1`.

This also **dissolves the Ohtsuki–Takata discrepancy** raised above: both DGLZ
and that registration carry `+1/2` in the torsion. The corpus simply works in
the reciprocal variable. No sign disagreement exists.

**And the corpus had already written eq (2.3) down.**
`jones_1loop_c0_calibration_fig8.py` states `exp(2c₀) = 1/(2|τ_DG|)`. DGLZ (2.3)
is `exp(2S₁) = T/2`. Under `T = 1/|τ_DG|` these are the same equation and
`c₀ = S₁` identically — derived independently, never connected to the source.

### CORRECTION — the constant is convention, and I claimed otherwise

Read further and the claim above collapses. DGLZ carry **at least three**
distinct additive offsets between conventions:

| where | offset |
|---|---|
| eq (2.3) | the `/2` inside `log(T/2)` |
| eq (4.5) | `S₁(0) = s₁ + log 2`, relating `S₁` to the **colored-Jones** coefficient `s₁` |
| footnote 24 | their `S₁` matches Gukov–Murakami "up to a shift by `log π`" |

and they say the `S_n` are determined by their differential hierarchy *only up
to an additive constant*, fixed "by comparison to the asymptotics of the colored
Jones polynomial". **DGLZ calibrate too.**

Worse for the retracted claim: the corpus measures `c_σ` from the colored-Jones
asymptotic, i.e. it corresponds to `s₁`, not `S₁`. Carry the eq (4.5) `log 2`
through and the identification itself moves:

```
c_σ = exp(S₁)   ⇒   T = 1/|τ_DG|
c_σ = exp(s₁)   ⇒   T = 4/|τ_DG|
```

A factor of 4 in `T` from one convention choice. So `2^{−1/2}` cannot be lifted
out of eq (2.3) as the corpus's `k`, **the corpus's calibration on `4_1` stands
and is not redundant**, and if anything DGLZ's constant and the corpus's are the
same calibration performed twice.

> **Addendum, same day — the second half of that sentence is now false.** The
> first half stands: `k` cannot be lifted out of DGLZ eq (2.3), for exactly the
> reasons above, and nothing below changes that. But the conclusion drawn from
> it — that the `4_1` calibration is therefore *irreducible* — assumed DGLZ was
> the only available route to the constant. It is not. Van der Veen's asymptotic
> for the Whitehead chains supplies `c_σ` **directly from the colored Jones**,
> with no convention to reconcile, and evaluating the integral he left
> unevaluated gives
>
> ```
> c_σ(W_{a,1,c,d}) = 2^{1/2−n} (n² + m²)^{−1/4},   n := c+d,  m := 4a−c+d
> ```
>
> which reproduces `k = 2^{−1/2}` on the link side with no calibration at all.
> The `4_1` calibration is now *corroborated rather than required* there — it
> remains load-bearing on the one-cusped side, which van der Veen's family does
> not reach (`b = 1` chains have `c+d+1 ≥ 2` components).
>
> The lesson for this audit's method: it correctly established that DGLZ's
> constant is unusable, and then over-concluded from "this route is blocked" to
> "the quantity is not derivable". Those are different claims, and only the
> first was shown.
>
> See `docs/audits/2026-08-08-vdv-constant-closed-form-and-the-open-bridge.md`.

### What survives, and it is the part that matters

**The exponent is invariant under every one of those offsets.** No multiplicative
constant changes `−1/2`. So the *form* `c_σ ∝ |τ|^{−1/2}` transfers from eq (2.3)
— stated for a general 3-manifold `M` with a flat `G_C` bundle, no restriction to
knots, two-bridge knots, or cusp number — while the prefactor does not.

That still answers Finding 1's "does `c_σ` depend on `τ` alone": the dependence is
a cited result. It does **not** hand over the constant.

### The c ≥ 2 risk, made concrete — and it is an exponent, not a constant

Following that up produced something sharper than a worry. DGLZ eq (2.1) carries
an explicit `ħ`-power, `Z ~ ħ^{−δ/2} ~ N^{δ/2}`, with `δ = h¹ − h⁰` (eq 2.2).
For a hyperbolic manifold with `c` cusps at the geometric representation with
adjoint coefficients the standard count is `h⁰ = 0`, `h¹ = c`, so **`δ = c` and
the power is cusp-dependent**. (That count is my inference — DGLZ state (2.2) but
never evaluate `h¹` for a cusped manifold.)

The corpus extracts `c_σ` with a **cusp-independent** `N^{−3/2}`, and the
exponent is *fitted*, not assumed:

| manifold | cusps | p measured | naive `δ/2 + 1` |
|---|---|---|---|
| `4_1` | 1 | 1.49999998391397 | 1.5 |
| `L5a1` | 2 | 1.499999207860905 | 2.0 |

Whatever `c`-independent offset reproduces `3/2` at `c = 1` demands `2` at
`c = 2`. The measured value is `3/2`.

**The measurement is the solid side of this.** A wrong exponent does not bias
`c_σ` by a constant — the discrepancy is a positive power of `N → ∞`, so the
limit diverges or vanishes instead of converging. At `N = 10⁴` the alternative
power differs by a factor of 100, and `c_σ(L5a1)` converges to 20 digits anyway.
So `p = 3/2` is correct at `c = 2` as a matter of measurement, and the naive
`δ = c` reading does not reach the observable.

**So a `c`-dependent step is missing from the dictionary** between the corpus's
`c_σ` normalisation and DGLZ's `S₁`/`s₁` — most plausibly in the colored-Jones
normalisation for a *link* (`c` components each coloured by `N`, and the eq (4.4)
ratio against the solid torus), which differs from the knot case in ways this
corpus has never worked out.

That is an independent reason the retraction above was necessary: constants
cannot be transported between the two while an unaccounted `c`-dependent power
sits in the dictionary. It also puts the `c ≥ 2` risk in one identified place —
the same place the retracted `2^{(c−1)/2}` and L6a4's 0.35% both live.

**And the missing step has almost no room — which partly relieves the worry.**
If it is `g(c)`, then `k_meas(c) = k_true·g(c)`, so the measured `k` ratios bound
it. The `c = 1 → c = 2` ratio pins it to 1 at ~17 digits:

```
g(2)/g(1) = k(2)/k(1) = 0.99999999999999999548
```

Every non-trivial candidate dies on that single number:

| candidate | predicts `g(2)/g(1)` | |
|---|---|---|
| `2^{(c−1)/2}` (the retracted per-cusp factor) | 1.41421356237 | excluded |
| `2^{c−1}` | 2.0 | excluded |
| `c` | 2.0 | excluded |
| `√c` | 1.41421356237 | excluded |
| `c^{1/4}` | 1.18920711500 | excluded |
| `1` (no step) | 1.0 | **survives** |

So whatever fixes the exponent bookkeeping contributes exactly 1 to the
**constant** at `c = 1` and `c = 2`. The tension is in the *power*, and it does
not leak into `k` at the cusp numbers tested. The `c ≥ 2` risk is real as a
bookkeeping gap and is **bounded** as a threat to the derivation.

The `c = 3` deviation (L6a4, 0.35%) does not change that and is not a cusp law
either: a systematic `c`-dependence would have shown at `c = 2` and does not, to
17 digits. More likely specific to that computation, as its own witness says.

### RESOLVED — by a theorem in `library/`, and against my inference

The N-power tension does not survive a search. `library/arxiv-math-0611181v2/0611181v2.pdf` is van der
Veen, *Proof of the volume conjecture for Whitehead chains* — **the paper this
corpus already reads its Whitehead colored-Jones values from**. Its Main theorem:

```
J_N(W_{a,b,c,d})(e^{2πi/N}) ~ exp{ (1/2π)[ (Vol + iCS)·N + D·log N + E ] }
```

> "If `b = 1` we have `D = 3π`"

so the power is `N^{D/2π} = N^{3/2}`, and **`D` does not depend on `c` or `d`** —
i.e. not on the number of components. Both manifolds at issue have `b = 1`:

| link | Whitehead-chain label | components | power |
|---|---|---|---|
| Whitehead | `W_{0,1,1,0}` | 2 | `N^{3/2}` |
| Borromean | `W_{0,1,1,1}` | 3 | `N^{3/2}` |

So the corpus's cusp-independent `N^{3/2}` is **theorem-backed at `c = 2` and
`c = 3`**, not merely fitted — and **the wrong step was mine**. The naive
`δ = c` reading of DGLZ (2.2) does not transfer to the colored-Jones observable.
Lemma 4 shows the mechanism: `J_N ~ C·N^{(c+d+3)/2}·S̃_N^{c+d}`, and `S̃_N`
carries its own `N^{−1/2}` per factor, so the component-dependence cancels out of
the net power.

That also retires the "most plausibly the colored-Jones normalisation for a link"
guess above: the link normalisation is exactly where it happens, and it is
already worked out — in a file we had.

### The same paper carries a live lead on the CONSTANT

Van der Veen's `E` is the constant this corpus measures as `c_σ`, and he gives it
**explicitly** in the proof of Lemma 4 (Steps 5–6) as a `(c+d+1)`-dimensional
Gaussian integral, for the whole family:

```
Q_∞ = ψ ∫ exp( −π[ (c+d−(4a+c−d)i)|w|²/2 + 2 Σ_j (|z_j| + |w|/2)² ] ) dw dz
```

He evaluates it only far enough to prove it is **nonzero**. And his closing
paragraph is this corpus's own open question, verbatim:

> "In the same paper it is also conjectured that the number `E` is determined by
> the Ray-Singer torsion of the complement twisted by the holonomy
> representation. We hope to investigate these conjectures for the Whitehead
> chains in a subsequent publication."

So `c_σ ↔ torsion` is named as an open problem at the end of the paper the corpus
reads its Jones values from, and nobody here connected the two.

**Not banked.** Connecting `Q_∞` to `c_σ` needs Lemma 3's constant for `S̃_N` and
the `J` vs `J'` normalisation, neither of which is done. A direct evaluation for
the Whitehead link gives `|Q_∞| / 2^{−3/4} = 0.8109`, not a recognisable
constant — which is what a missing normalisation factor looks like, not what a
dead lead looks like. Route, not result.

Machine-checked in
`computations/probes/one_loop_cusp_normalisation_tension_probe.py`.

### And it sharpens where the c ≥ 2 risk actually is

That `k` is the *same* at `c = 1` and `c = 2` (`k₁ = k₂` to 17 digits) is **this
corpus's empirical finding**, not something read off DGLZ — nothing there asserts
cusp-independence. Ray–Singer torsion on a cusped manifold requires a choice of
basis in `H¹`, whose rank *is* the cusp number. That is exactly where a
cusp-dependent normalisation would hide, and exactly where the retracted
`2^{(c−1)/2}` per-cusp factor lived. The `c = 3` (L6a4) 0.35% offset sits in that
same territory and is still unexplained.

### What is actually left

**Rigour, and only rigour.** Eq (2.3) is a one-loop saddle-point / Feynman-diagram
derivation citing Witten (1989), Bar-Natan–Witten (1991) and Gukov–Murakami
(2006). It is not a theorem, and nothing here makes it one.

But the gap is not shaped the way the corpus describes it. The repeated line
*"no theorem covers the link case"* is about **proof status**, not about the
formula's reach — the formula covers links already, and the missing rigour is
missing for knots too (`4_1` included). Anywhere that line appears it should say
so, otherwise it reads as though the link case needs a new formula when it needs
a proof of an existing one.

Machine-checked in `computations/probes/one_loop_dglz_prefactor_identification_probe.py`.

## Recommended action, in cost order

1. ~~**Read `library/arxiv-0903.2472v1/0903.2472v1.pdf` (DGLZ).**~~ **DONE** — see the addendum
   above. It supplied the form, the constant, and the generality, and it
   dissolved item 2 below as well.
2. ~~**Resolve the Ohtsuki–Takata exponent convention.**~~ **RESOLVED by the
   addendum** — DGLZ carry `+1/2` too; the corpus works in the reciprocal
   variable, so there was never a disagreement. Obtaining the paper is still
   worthwhile for the separate question of whether it makes the `c = 1` leg
   *rigorous*, which DGLZ does not.
3. **Reconcile Pandey–Wong** with the "no theorem covers links" line in the two
   audits that assert it — one sentence, in both places.
4. **Amend the assumption ledger** in `2026-08-08-c-sigma-derivation-status.md`
   to split exponent from functional dependence, per Finding 1. (Done in this
   change.)
5. Only then treat "does `c_σ` depend on `τ` alone" as the research problem. It
   may already be answered in (1).

## Scope

Finding 1 is a re-reading of existing numbers plus one new fit; it derives
nothing and adds no manifold. Finding 2 reports what registration notes say
about papers that **were not read** — including by the registrations' own
admission — and must not be cited as though the theorems had been checked.
