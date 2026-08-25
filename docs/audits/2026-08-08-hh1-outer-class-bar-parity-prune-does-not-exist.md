# The bar-parity prune on the HH¹ outer class does not exist — it is normalization, not an invariant

**Date:** 2026-08-08 · **Bean:** `qou-qb8b` · **Probe:**
[`computations/hh1_outer_class_cocenter_bar_parity.py`](../../computations/hh1_outer_class_cocenter_bar_parity.py)
· **Witness:** `hh1-outer-class-cocenter-bar-parity.witness.json`
· **Tier:** symbolic-exact (exact cyclotomic linear algebra, no fit, nothing wired)

## What was asked

Bean `qou-qb8b` proposed a cheap decisive prune for the one surviving
fibre-level c₃ carrier:

> Read the bar-parity of the outer class's action on the cocenter at the
> Bring root of unity. Bar-even kills the route to the same invariant that
> killed the real resolvent.

## Answer: the quantity is not well-defined, so the prune cannot exist

**The bar-parity of the HH¹ outer class acting on HH₀ is a choice of
normalization, not an invariant of the class.** Both parities are always
available. Bar-parity therefore cannot prune this route — and cannot confirm
it either.

This is a **scope-(a) negative about the test**, not a refutation of the
carrier. The route is left exactly where it was: open.

## The computation

`H₃(q)`, dim 6, basis `[e, s₁, s₂, s₁s₂, s₂s₁, s₁s₂s₁]`, relation
`sᵢ² = a sᵢ + 1` with `a = q − q⁻¹` (AGENTS.md §7a). Inherits the
multiplication tables from the merged PROBE A
(`hh1_hecke_outer_derivations.py`).

| point | dim HH₀ | dim Der | dim Inn | dim HH¹ | Δ^bar ∝ Δ? | λ | raw parity |
|---|---|---|---|---|---|---|---|
| `q = i` (`[2]_q = 0`) | 3 | 4 | 3 | **1** | yes | `+1` | bar-EVEN |
| `q = ζ₆` (`[3]_q = 0`) | 3 | 4 | 3 | **1** | yes | `−1` | bar-ODD |
| `q = 2` (semisimple control) | 3 | 3 | 3 | **0** | — | — | n/a |

### Why the test is canonical at all — and where it stops being so

A derivation descends to the cocenter, since
`D(ab − ba) = [D(a), b] + [a, D(b)] ∈ [A,A]`. An **inner** derivation
descends to **zero**, because `ad_x(y) = xy − yx` *is* a commutator. So the
induced map `Δ : HH₀ → HH₀` depends only on the HH¹ **class** — the map
`HH¹ → End(HH₀)` is well defined.

*Asserted, not assumed:* `inner_acts_as_zero_on_cocenter` (all 6 `ad_x`
induce zero) and `delta_is_class_canonical` (6 alternative representatives
`outer + ad_x` each reproduce Δ **exactly**).

But class-canonicity is only **up to a scalar**: `dim HH¹ = 1`, so the
representative is fixed only modulo `D ↦ cD`. And that is precisely where the
parity leaks away.

### The normalization-dependence, demonstrated constructively

Under `D ↦ cD`: `Δ ↦ cΔ` and `Δ^bar ↦ bar(c)·Δ^bar`, so the parity is
multiplied by `bar(c)/c`. The involutivity `β² = id` forces
`λ·bar(λ) = 1` — checked (`lambda_has_norm_one`) — which is exactly the
**Hilbert 90** hypothesis for the quadratic extension `ℚ(ζ)/ℚ(ζ)⁺` (the
bar-fixed field). `H¹` of that extension vanishes, so `λ = bar(c)/c` is
*always* solvable.

Rather than lean on the theorem, the probe exhibits the flip:

```
q = i    : rescale by bar-ODD c = 2i                        bar-EVEN -> bar-ODD   FLIPPED
q = ζ₆   : rescale by bar-ODD c = (√3+3i)/(√3−i)            bar-ODD  -> bar-EVEN  FLIPPED
```

`ζ − ζ⁻¹` is bar-odd by construction (`bar(ζ−ζ⁻¹) = ζ⁻¹−ζ`), and `ℚ(ζ)`
always contains it. So a bar-odd rescaling is always available and the parity
always flips.

The two points landing on *opposite* raw parities (`λ = +1` vs `λ = −1`) is
itself the symptom: nothing canonical distinguishes them.

## Why the real-resolvent prune worked and this one cannot

This is the part worth carrying forward.

The real Gram resolvent lived over **ℝ**, where the bar involution acts
**trivially**. Its parity was therefore *rigid*, and the bar-odd target `S`
was genuinely unreachable — a real prune
([`2026-07-19-c3-q0-real-routes-closed-fibre-phase-survives.md`](2026-07-19-c3-q0-real-routes-closed-fibre-phase-survives.md)).

At a root of unity, bar acts as the **nontrivial** Galois map `ζ ↦ ζ⁻¹`, and
`ℚ(ζ)` contains bar-odd scalars. Both parities are available for free.

**That is precisely why the fibre-level route survived the real-route
exclusion chain in the first place.** The same feature that let it survive is
the feature that makes bar-parity uninformative about it. Expecting bar-parity
to prune it was expecting the fibre route to have the rigidity whose *absence*
defines it.

## Operational consequence — do not spend the H₅ computation on this

Bean `qou-jcmw` (dim HH¹(H₅(ζ₅)) at the Bring root) remains worth doing **for
its dimension count**. But its *parity* leg should not be run expecting a
prune: the normalization-dependence argument above is **field-theoretic**
(Hilbert 90 over `ℚ(ζ)/ℚ(ζ)⁺`) and does not depend on `n`. `H₅` is dim 120 —
14 400 unknowns and ~1.7M Leibniz equations — so this is a real saving, and it
is exactly the formalize-first discipline paying off: the structural argument
pruned the expensive search rather than the search pruning the hypothesis.

## What would make a parity test meaningful

Bar-parity regains content only against a **pinned normalization**. Candidates,
none attempted here:

1. **An integrality / Habiro-lattice normalization** — fix the representative
   by requiring it to preserve a `ℤ[q,q⁻¹]`-lattice, so only units `±qᵏ`
   remain and the residual scaling group is small enough to carry an invariant.
2. **A pinned pairing against `tr_M`** — the c₃ swing is a *number*, not a
   class. Pin the whole construction `S = ⟨tr_M, Δ(x)⟩` for a canonical
   generator `x ∈ HH₀`, and read the parity of that number.
3. **A finer invariant than parity** — e.g. the class of the induced operator
   in a bar-equivariant K-group, where Hilbert 90 does not trivialize it.

Route (2) is the closest to what the c₃ front actually needs, since it is the
only one that produces a scalar comparable to `S`.

## Successor result (same session) — the pinned test, run

Bean `qou-qb8d` was filed for route (2) above and then run:
[`hh1_outer_class_trace_paired_parity.py`](../../computations/hh1_outer_class_trace_paired_parity.py),
witness `hh1-outer-class-trace-paired-parity.witness.json`.

**Both pins are structural, not chosen:**

- **Generator** — He–Nie: `HH₀(H_n)` has a basis indexed by conjugacy classes
  of `S_n`, represented by **minimal-length** elements; for n=3 those are
  `e` (ℓ=0), `s₁` (ℓ=1), `s₁s₂` (ℓ=2). *Asserted* to project to a basis of HH₀.
- **Trace** — Ocneanu/Markov, Jones specialization per the corpus. `z` held
  **symbolic and bar-even**, which avoids a `q^{1/2}` branch choice at the root
  of unity *and* makes the conclusion independent of the Ocneanu-parameter
  question that [`2026-08-04-ocneanu-trace-parameter-audit.md`](2026-08-04-ocneanu-trace-parameter-audit.md)
  records as genuinely open. *Asserted*: `tr_M` kills all 36 commutators
  `[Bᵢ,Bⱼ]`, which validates both the recursion and the descent to HH₀.

### Result: not trace-blind, and the paired number is MIXED with a nonzero bar-ODD part

| point | x | `S_x = tr_M(Δ(x))` | `S_even` | `S_odd` | parity |
|---|---|---|---|---|---|
| `q = i` | `s₁` | `z/3 − i/3` | `z/3` | `−i/3` | **MIXED** |
| `q = i` | `s₁s₂` | `2iz/3 + 2/3` | `2/3` | `2iz/3` | **MIXED** |
| `q = ζ₆` | `s₁s₂` | *(see witness)* | `−z` | `√3·i(1−z²)/3` | **MIXED** |

Cross-checked against the **specialized** Jones `z` (guarding against the
verdict being an artifact of holding `z` formal): `z = √2/2` at `q = i` and
`z = √3/3` at `q = ζ₆` — both **real**, which independently verifies the
bar-evenness hypothesis on `z`. The bar-odd parts survive: `−i/3`,
`√2·i/3`, and `2√3·i/9` respectively, all nonzero (asserted).

### Reading

1. **The clean scale-invariant prune does not occur.** `tr_M ∘ Δ ≠ 0`, so the
   outer class is **not** trace-blind on the cocenter. Had it been zero, that
   would have been independent of both pins and a genuine kill; it is not.
2. **The pairing carries a nonzero bar-ODD component** — precisely the parity
   the c₃ swing `S` requires. So the bar-parity obstruction that closed every
   real route does **not** close this one. Consistent with, and now
   quantitative about, the §"why the real prune worked" argument above.
3. **Asymmetry worth noting:** at `q = ζ₆` the unit group of `ℤ[ζ₆]` contains
   **no** element with `bar(c)/c = −1`, so an integrality pin *would* fix the
   parity there; at `q = i` the units `±i` flip it. Integrality is therefore a
   point-dependent pin, not a general one.

### What this does NOT establish

Necessary, not sufficient — and the gap is wide:

- A nonzero bar-odd **component** is not a bar-odd **eigenvector**. The number
  is MIXED; isolating the odd part is a further structural choice that has not
  been justified.
- **Magnitude is completely untouched.** Nothing here reproduces c₃'s value or
  its anchor-swing; only the parity channel was tested.
- n=3 is the **mechanism**; the Bring fibre is H₅ at ζ₅.

**Net:** the HH¹ carrier survives the bar-parity screen with a positive
indication. It is not confirmed, and the c₃/Q_β derivation gap is unchanged.

## What the R-matrix says about that decomposition (asked mid-session)

Probe: [`hh1_bar_odd_channel_is_skein_generated.py`](../../computations/hh1_bar_odd_channel_is_skein_generated.py),
witness `hh1-bar-odd-channel-skein-generated.witness.json`.

The R-matrix **is** the braiding `σᵢ`, and bar sends `σᵢ ↦ σᵢ⁻¹`. So **bar is
crossing reversal — the mirror image.** Splitting the R-matrix into bar-
eigenparts using the Hecke eigenprojections `σ = qP₊ − q⁻¹P₋`:

| part | value | parity | note |
|---|---|---|---|
| `σ − σ⁻¹` | `(q − q⁻¹)·1 = a·1` | **bar-ODD** | **is the Skein relation**, and **central** |
| `σ + σ⁻¹` | `[2]_q (P₊ − P₋)` | **bar-EVEN** | the symmetric/antisymmetric channel grading |

All verified element-level and symbolically in `q`, both generators, with
`P₊`/`P₋` checked idempotent and summing to `1`. *(The first version of this
check was wrong and the assertion caught it: it substituted `q → 1/q` in the
**matrix** of left-multiplication, but the `T_w` basis is **not** bar-invariant,
so that is a different operation from bar-ing the element.)*

### Consequence — the bar-odd channel is Skein-generated

Since the bar-odd part of the R-matrix is `a·1` and is central, the bar-odd
channel is **generated by `a = q − q⁻¹`**: anything bar-odd is `a` × (bar-even),
because `bar(a) = −a`.

**Falsifiable prediction, and it holds.** Every `S_odd` from the qb8d pairing
divides by `a` with a bar-EVEN quotient (an `S_odd/a` that came out bar-odd
would have refuted it):

| point | x | `S_odd` | `S_odd / a` | quotient bar-even? |
|---|---|---|---|---|
| `q = i` | `s₁` | `−i/3` | `−1/6` | ✓ |
| `q = i` | `s₁s₂` | `2iz/3` | `z/3` | ✓ |
| `q = ζ₆` | `s₁s₂` | `√3·i(1−z²)/3` | `(1−z²)/3` | ✓ |

**So the bar-odd swing the c₃ route needs is forced into the shape**

```
S = (q − q⁻¹) · (bar-even)
```

This is a **shape constraint, not a value** — it does not supply the magnitude
(bean `qou-qb8e`) and is not a derivation of c₃. It is, however, the kind of
constraint that is formalizable, and it narrows what a candidate carrier may
look like.

### Corollary — the amphichiral sector cannot source the swing

Because bar is the mirror image, an **amphichiral** knot `K = mirror(K)` has
`J_K = bar(J_K)`, i.e. a **bar-EVEN** invariant with *zero* bar-odd content.
The figure-eight `4₁` is the standard amphichiral knot — so the muon anchor
`Vol(4₁)` sits entirely in the bar-even channel and **cannot** source the
bar-odd c₃ swing. The swing must come from a chiral object. This follows
immediately from `bar = mirror` plus the textbook amphichirality of `4₁`; it is
recorded as a deduction, not a new computation, and it is consistent with the
corpus already treating the swing as a separate object.

More broadly: **the bar-odd part of any knot invariant is its chirality
content** — the part that distinguishes `K` from its mirror. So the c₃ residual
lives in the chirality channel, which is the same channel the `Δ_λ` sign
(`(−1)^{n(λ)}·dim`) and the KL-positivity prune already live in.

## ⚠ RETRACTED — the `S_leak` filter below does not hold

**Retraction (same day, prompted by the author's question "this is not
derived? `S_leak := c₃ + Vol(4₁)`").** The section that follows built a
candidate filter on `S_leak`. That was an over-reach on my part and is
withdrawn. The `:=` is a **definition**, and it is only a *bar-decomposition*
of c₃ if `c₃`'s bar-even part is **derived** to equal `−Vol(4₁)`. I did not
establish that before using it. Three findings, in increasing severity:

**(1) The bar-decomposition of c₃ is not empirically accessible.** For a
function of real `q`, `c₃^even(q) = (c₃(q) + c₃(1/q))/2`. Both substrate
anchors sit at `q ≈ 1.10998`; computing the even part needs `c₃` at
`q ≈ 0.901`, which no anchor supplies. **Any** even/odd split of c₃ therefore
rests on an assumed structural form, never on the anchor data.

**(2) The sign flip is offset-generic — it is not evidence about `Vol(4₁)`.**
`S_leak(μ) > 0 > S_leak(p)` holds for *any* constant `V` strictly between
`−c₃(μ) = 2.02020024` and `−c₃(p) = 2.06934258` — a window of width **0.0491**.
Verified: `Vol(4₁) = 2.029883`, `2 + 1/36`, `2 + 1/30`, `2 + 1/25`, `2 + 1/24`,
`63/31`, `e^{0.708}` all lie in it and all produce the same "genuine sign
change". The flip is a restatement of *c₃ differing between the two anchors*,
not a property of `Vol(4₁)`.

**(3) The corpus carries two inequivalent "bar-even part of c₃" claims.**
[`2026-07-07-c3-even-solved-s-complex-volume-rigidity.md`](2026-07-07-c3-even-solved-s-complex-volume-rigidity.md)
— the audit cited for "c₃^even is solved" — identifies the bar-even channel as
an exact `ℚ(√3)` ũ-ladder (`e₁ = 3√3/4`, projection rung `≈ +86.66`) and the
bar-odd scalar as `S = Q_β/E₀ ≈ 908`, which **does not** sign-flip
(`S_p/S_μ ≈ 1.024`). The `S_leak` framing instead takes the even part to be
`−Vol(4₁) ≈ −2.03` with an odd residual `≈ 0.0097`. These are **not the same
decomposition**. `SLeakZeroCrossing.lean` is aware of the symbol clash and
guards it ("Do not conflate the two symbols"), but the guard separates the two
`S`s — it does not reconcile the two *even* parts. And that same 2026-07-07
audit tiers the `𝔙` identification **`exploratory`** in its own header.

**What this does and does not touch.** The Lean theorems in
`SLeakZeroCrossing.lean` are stated for a *generic* continuous function with
the anchor signs as hypotheses, and they are fine as stated — this is not a
claim that they are wrong. What is unsupported is the *interpretive* step that
`S_leak` is c₃'s bar-odd part, and everything I derived from it.

**Still standing, independent of `S_leak`:** the R-matrix decomposition
(`σ − σ⁻¹ = a·1` bar-odd and central; `σ + σ⁻¹` bar-even), the
Skein-generation of the bar-odd channel (`odd = a ×` even), the amphichirality
corollary (`4₁` amphichiral ⇒ its invariant is bar-even), and the qb8b/qb8d
results. None of those used `S_leak`.

**Withdrawn:** "the entire bar-odd content of c₃ *is* `S_leak`", and the
consequent exclusion of `−[2]_q` and the `q→1` shadow `−2` as candidates. Those
required `c₃^even = −Vol(4₁)` exactly. Whether that identification is in fact
derived is a question for the c₃ owners (#4725), not something this audit
adjudicates — flagged, not settled.

The original section is kept below **struck through in intent** for the record,
per the corpus convention of not deleting a finding that was published.

---

## ~~Composing with `S_leak` — a filter on c₃ candidates (cross-arc, from #4725)~~ [RETRACTED — see above]

Sibling #4725 flagged that ϑ_K and c₃ are the same open question, related
affinely, and pointed at `conj:binding-qbeta-complex-volume`. Verified against
the corpus: [`SLeakZeroCrossing.lean:11`](../../content/quantum-observable-universe/lean/QOU/QBeta/SLeakZeroCrossing.lean)
defines

```
S_leak(q₀) := c₃(q₀) + Vol(4₁)          -- the BAR-ODD residual of c₃
```

with `S_leak(muon) = +0.0096830`, `S_leak(proton) = −0.0394594`. Reproduced
here independently: `S_p/S_μ = −4.075` against the corpus's `−4.08`. ✓

Composing with the amphichirality corollary above: `4₁` is amphichiral, so
`Vol(4₁)` is bar-**EVEN** and contributes **zero** bar-odd content. Hence

> the entire bar-odd content of c₃ **is** `S_leak`, and by the Skein-generation
> result it must have the shape `S_leak = (q − q⁻¹) · (bar-even)`.

**The filter this gives.** A candidate for c₃ that is purely **bar-even** has
zero bar-odd part and therefore *cannot* produce a nonzero `S_leak` — yet
`S_leak` is measurably nonzero at both anchors. So the bar-even candidates are
structurally excluded **as the whole of c₃**:

| candidate | parity | verdict |
|---|---|---|
| `−[2]_q = −(q + q⁻¹)` | bar-EVEN | can be at most c₃'s bar-even part |
| `q→1` shadow `G(0,1) = −2` (constant) | bar-EVEN | same |

Each may still be the bar-even *part*; the leak needs a separate `a`-generated
term. This may also explain the shape of the near-miss history — the recurring
~0.5–3 % misses look like candidates capturing the bar-even part and missing
the bar-odd term entirely. *Offered as interpretation, not established.*

**Scope.** A shape constraint, not a value. The `dc₃/dq ≈ 4.6×10⁶` real-q
exclusion (PR #1821) already stands independently; this constraint bites on the
**fibre-level** carrier, which is where the surviving route lives.

**Corpus-status check performed on request (#4725).** The `[3]_q/25` 3-rung
"2.65 ppm" c₃ result is **NOT live**: superseded banner on
[`2026-06-03-l2-closure-habiro-3-q-25-universal-template.md`](2026-06-03-l2-closure-habiro-3-q-25-universal-template.md),
falsified one day later by cross-anchor rigidity
([`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md)) —
2.65 ppm at the **proton anchor only**, swinging −2.88 % to muon. Authoritative
tier in [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
§3: *"EMPIRICAL — near-match, REFUTED as real-q fibre element."* The same row
records a 2026-07-30 update: the B1 re-run with the canonical GGM `V₃ = −7.693`
gives **0 assembly hits in 180 candidates**, the earlier near-misses being
artifacts of a wrong `V₃`.

*Minor flag for the registry:* that row quotes `−[2]_q` as "0.54 % off at q₀";
recomputation gives **2.82 %** at the proton pin and ~0.46 % at the muon pin, so
the figure is anchor-specific and matches neither exactly. Not asserting the
registry is wrong — flagging that the anchor should be stated, since this is
exactly a quantity that swings between pins.

## Discipline

Nothing wired. No fit. The `cal-anchored` c₃ is untouched. Per AGENTS.md
§"Before declaring refuted", this is recorded as **scope-(a)**: a negative
about the readout, with no proved invariant excluding the HH¹ carrier itself.
The c₃/Q_β derivation gap is unchanged and remains open.
