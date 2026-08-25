# Which fibre does the mass channel trace over? — the row cap is already written into the mass chapter, and it forces convention D

Bean [`qou-n1dj`](../../.beans/qou-n1dj--gap-does-the-mass-fibre-functor-land-in-repsu-q2tl.md),
option 3. Branch `claude/n1dj-mass-fibre-dimension-2026-08-08`. 2026-08-08.

Predecessor: [`2026-08-08-borromean-trace-convention-forcing.md`](2026-08-08-borromean-trace-convention-forcing.md)
(bean `qou-3qrv`), which settled everything about the D-vs-C split except the
premise.

## Verdict

**Convention D**, on the corpus's own premise, with no experimental input.

The question was reframed from "which trace" to "which fibre do the three
strands live in". That reframing is what made it answerable, because **the mass
chapter already answers it, explicitly, in the block that defines the mass
channel's decomposition.**

`lem:feynman-eigenbasis-decomposition`
([`feynman-eigenbasis-decomposition.md`](../../content/quantum-observable-universe/mass-theory/feynman-eigenbasis-decomposition.md)):

> *Let $V$ be the fundamental representation of $\mathrm{SU}_q(2)$ with $q$ not
> a root of unity. … Then*
> $$V^{\otimes n} \cong \bigoplus_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}} V_\lambda \otimes S_\lambda,$$
> *where $V_\lambda$ is the irreducible $\mathrm{SU}_q(2)$-module of spin
> $j = (\lambda_1-\lambda_2)/2$ … The number of summands is
> $\lfloor n/2\rfloor + 1$.*

Three things are load-bearing here, and all three point the same way:

1. `V` is the **fundamental of $\mathrm{SU}_q(2)$** — so `dim V = 2`, `N = 2`.
2. The **row cap `ℓ(λ) ≤ 2` is in the index set of the sum.** At `n = 3` the sum
   runs over `{(3), (2,1)}`. The three-row block `(1³)` has `ℓ = 3 > 2` and is
   **absent** — there is no `(1³)` channel for a weight `y_(1³)` to occupy.
3. The summand count `⌊n/2⌋+1` is the count of partitions of `n` with at most
   **two** rows, i.e. it is the `N = 2` count and no other.

The proof block
[`feynman-eigenbasis-decomposition-proof.md`](../../content/quantum-observable-universe/mass-theory/feynman-eigenbasis-decomposition-proof.md)
repeats it ("by the $q$-analogue of Schur–Weyl duality … spins
$j = n/2, n/2-1, \ldots, \epsilon/2$").

So `y_(1³) = 0` for the mass channel is not an extra assumption to be argued
for — it is a restatement of the decomposition the mass chapter already uses.
Feeding it into `markovWeights_eq_jones_of_threeRow_eq_zero`
([`MarkovTraceTLUniqueness.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean),
sorry-free on `main`) yields convention D uniquely.

### And the next block does not merely imply D — it *is* D, in closed form

The decomposition block could be read as describing the ambient
representation-theoretic setting rather than the trace. The block that defines
the trace removes that reading.
[`feynman-markov-identification.md`](../../content/quantum-observable-universe/mass-theory/feynman-markov-identification.md):

> $$\langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}} := \sum_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}} w_\lambda \cdot \mathrm{tr}_{S_\lambda}\bigl(\rho_n(\beta)\bigr).$$
>
> *This equals the Jones–Markov trace $\mathrm{tr}_M\bigl(\rho(\beta)\bigr)$ on
> $H_n(R,q)$, where the Markov weights are
> $w_\lambda = \dim_q(V_\lambda)\cdot\dim(S_\lambda)/\dim_q(V^{\otimes n})$.*

Three things at once: the row cap `ℓ(λ) ≤ 2` sits **inside `tr_M` itself**; the
result is named the **Jones**–Markov trace; and the weights are given in **closed
form**. Evaluating that closed form at `N = 2` — `dim_q V_λ = [2j+1]_q` for
spin `j = (λ₁−λ₂)/2`, `dim_q V^{⊗n} = [2]_q^n` — at `n = 3`:

| `λ` | `ℓ(λ)` | spin `j` | `dim_q V_λ` | `dim S_λ` | `y_λ = dim_q V_λ / [2]_q³` |
|---|---|---|---|---|---|
| `(3)` | 2 | `3/2` | `[4]_q` | 1 | `[4]_q/[2]_q³ = 0.50540422650393080` |
| `(2,1)` | 2 | `1/2` | `[2]_q` | 2 | `[2]_q/[2]_q³ = 1/[2]_q² = 0.24729788674803460` |
| `(1³)` | **3** | — | — | — | **absent from the index set** |

That is **convention D's weight vector, all three components**, and the
Schur–Weyl normalisation `Σ_λ dim_q(V_λ)·dim(S_λ) = [4]_q + 2[2]_q = [2]_q³`
(i.e. the corpus's `Σ_λ y_λ d_λ = 1`) holds exactly. Machine-checked as C6 of the
probe below: normalisation `= 1` to 50 digits, agreement with
`([4]/[2]³, 1/[2]², 0)` to `3.3e-52`, Markov residual at `z_D` `1.1e-50`.

**One factor in that quoted formula is misplaced, and saying so is part of the
finding rather than a caveat on it.** Taken literally, `w_λ` includes
`dim(S_λ)`, so `Σ_λ w_λ = 1` — a probability weight over blocks. But the
Frobenius weights of `tr_M = Σ_λ y_λ χ^λ` are normalised by
`Σ_λ y_λ d_λ = 1` (since `χ^λ(1) = d_λ = dim S_λ`), and pairing the literal
`w_λ` against an *unnormalised* `tr_{S_λ} = χ^λ` double-counts the multiplicity:
it gives `tr_M(1) = Σ_λ w_λ d_λ ≠ 1`. The reading that normalises correctly is

  `y_λ = w_λ / dim(S_λ) = dim_q(V_λ) / dim_q(V^{⊗n})`,

whose `Σ_λ y_λ d_λ = Σ_λ dim_q(V_λ)dim(S_λ)/dim_q(V^{⊗n}) = 1` is exactly the
Schur–Weyl identity — which is presumably where the stray `dim(S_λ)` came from.
So the `dim(S_λ)` belongs in the normalisation identity, not in the weight.
Errata, filed as follow-up 4.

This does not soften the conclusion: the parts that identify the trace — the row
cap `ℓ(λ) ≤ 2` in the index set, the name *Jones*–Markov, and the `dim_q(V_λ)`
numerator over `dim_q(V^{⊗n})` — are unambiguous, and the only normalisation of
them that is a trace at all is D's.

So the corpus's own definition of the mass trace *already computes D*. The
"full-Hecke Ocneanu" Scope note is not describing a second option the mass
channel might take; it contradicts the definition two blocks earlier.

**The CODATA match played no part.** D is the convention that lands on
CODATA; that is exactly why the number cannot arbitrate, and it was not used.
The argument runs fibre → row cap → `y_(1³) = 0` → D. The new probe
records `uses_experimental_target_values: false`, and neither the new Lean nor
the derivation above mentions a measured quantity.

## The corpus was inconsistent, and this identifies which side is wrong

Bean `qou-n1dj` sub-task 2 asked which of the two conflicting statements to fix.
Answer: **the Scope note of `prop:h3-markov-wenzl-weights` is the wrong one.**

[`h3-markov-wenzl-weights-context.md` lines 8–15](../../content/quantum-observable-universe/mass-theory/h3-markov-wenzl-weights-context.md)
says:

> The framework's **mass and binding computations** use a *different* trace: the
> **full-Hecke Ocneanu** Markov trace, with parameter `z = 1/(q^{1/2}+q^{-1/2})`
> … and its three-row weight is `y_(1³)(q) ≠ 0` for `q ≠ 1`.

That is incompatible with the mass chapter's own `ℓ(λ) ≤ 2` decomposition, and
also with what production actually computes (`canonical_mass.py` consumes the D
value). Three independent corpus facts agree against it:

| Source | Says |
|---|---|
| `lem:feynman-eigenbasis-decomposition` | `ℓ(λ) ≤ 2`, `V` = fundamental of `SU_q(2)`, `⌊n/2⌋+1` summands |
| `feynman-markov-identification` | `tr_M` **is** the `ℓ(λ) ≤ 2` sum; calls it the **Jones**–Markov trace; its closed-form `w_λ` evaluates to D's vector exactly |
| `qou-w5fw` closure (2026-08-07) | `N` is the quantum dimension of the fibre; Descartes gives `dim V = 2`; `N = 2` |
| `qou-fvzm` closure, main commit `f92a8b15` | "`N = 2` is LOCKED IN for the mass pipeline" |

The Scope note is the outlier. **This audit does not edit it** — that is a
content change with its own review surface, and it should land as its own
commit with the block's sidecar refreshed; it is recorded as follow-up below.

Sub-task 3 of the bean (the Scope note's claim that the two traces "coincide …
on writhe-0, `π=id` braids — which is why every *physical* mass prediction is
insensitive to the distinction") is likewise refuted by the same file's own
numbers: `β_Bor` is writhe-0 with `π = id` and `D − C = 1.9554e-4` there. Since
that sentence is the load-bearing justification for the Scope note, the note
does not survive the correction of it either.

## The new mathematics: the fibre dimension *determines* the Ocneanu parameter

The above closes the question on the corpus's premise. It leaves a gap of
principle: it shows `y_(1³) = 0` from the decomposition, but not that "fibre of
dimension `N`" pins the trace parameter at all. If it did not, one could imagine
a `2`-dimensional fibre still carrying a one-parameter family of traces. It
does not. New, sorry-free:

[`QOU/BraidsAndKnots/FibreDimensionForcesTL.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/FibreDimensionForcesTL.lean)

| Declaration | Statement |
|---|---|
| `qNumber_shift_identity` | `q·[N+1] − q⁻¹·[N−1] = q^N·[2]` |
| `ocneanu_param_eq_of_fibre_qdim` | `z·[N]_q = q^N` — the Ocneanu parameter of the categorical trace on `V^{⊗n}` with `dim_q V = [N]_q` |
| `ocneanu_param_of_two_dim_fibre` | `N = 2 ⟹ z·(q+q⁻¹) = q²` (= convention D) |
| `threeRow_eq_zero_of_jones_ocneanu` | converse of the existing theorem: that `z` forces `y_(1³) = 0` |
| `twoDimFibre_pins_h3_weights` | composite: `dim_q V = [2]_q ⟹ y_(1³) = 0 ∧ [2]_q²·y_(2,1) = 1` |

Derivation. For the fundamental `V` of `U_q(sl_N)`, `V ⊗ V ≅ S²V ⊕ Λ²V` with
quantum dimensions `[N][N+1]/[2]` and `[N][N−1]/[2]`, and the braiding acts as
`q` on the symmetric and `−q⁻¹` on the antisymmetric part (AGENTS §7a: `σ_i` has
eigenvalues `q`, `−q⁻¹`). Reading the Ocneanu parameter off at `n = 2`,

```
z · [N]²  =  q·dim_q S²V − q⁻¹·dim_q Λ²V
          =  ([N]/[2])·( q·[N+1] − q⁻¹·[N−1] )
          =  ([N]/[2])· q^N·[2]                    ← the shift identity
          =  q^N·[N] ,
```

hence `z·[N] = q^N`. The whole computation collapses through the shift identity,
whose content is that the two `q^{−N}` contributions cancel — and they cancel
*identically*, without needing `q·q⁻¹ = 1`, which is why the Lean version needs
no hypothesis on `q − q⁻¹` at that step.

Consequences:

- **`N = 2` gives `z·[2]_q = q²`, verbatim the conclusion of
  `markovWeights_eq_jones_of_threeRow_eq_zero`.** That file derives it *from* the
  Temperley–Lieb condition; this one derives it *from* `dim_q V = [2]_q`, with no
  reference to the quotient. Two independent routes, one parameter. That is a
  genuine cross-check of the existing result, not a restatement of it.
- **A fibre leaves no residual freedom.** Once `N` is fixed, `z` is fixed. So
  there is no second trace on `H₃(q)` available to the mass channel to be
  "selected" over another; the selection happened when the fibre was chosen.
- `threeRow_eq_zero_of_jones_ocneanu` closes the loop in the other direction, so
  "factors through TL" and "`z·[2] = q²`" are equivalent labels for one trace
  (modulo `[2]_q ≠ 0` and `[3]_q ≠ 0` — the root-of-unity degeneracy at which
  `TL₃` itself collapses, so its exclusion is expected rather than an artefact).

Verification: `scripts/lean-verify.sh` → `✓ exit 0 — checks` on the new file and
on `MarkovTraceTLUniqueness.lean` (baseline). `#print axioms` on all five
declarations gives `[propext, (Classical.choice,) Quot.sound]` — **no
`sorryAx`**. Generic `{R : Type*} [CommRing R] [IsDomain R]`, division-free
(`q⁻¹` carried as `qi` with `q*qi = 1`), no `ℝ`, no ordering, no numerical `q₀`
(AGENTS §7c).

## Convention C corresponds to no integer fibre dimension

`z(N) = q^N/[N]_q = (q − q⁻¹)/(1 − q^{−2N})` is strictly decreasing in `N` for
`q > 1`, hence injective, so `N` is recoverable from `z`:
`N = −ln(1 − (q−q⁻¹)/z) / (2 ln q)`.

[`computations/ocneanu_param_from_fibre_dimension.py`](../../computations/ocneanu_param_from_fibre_dimension.py)
→ [`ocneanu-param-from-fibre-dimension.witness.json`](../../computations/ocneanu-param-from-fibre-dimension.witness.json),
50 dps, `q₀ = 1.1099785827513808` (**experimental / proton pin**, per the
AGENTS 2026-08-07 owner directive; recorded in the witness), 6/6 checks pass:

| | `z` | `N_eff` |
|---|---|---|
| D (`N = 2`) | `0.6126880371464652` | `2.0` |
| `N = 3` | `0.4493048090902079` | `3.0` |
| **C** (`1/(q^{1/2}+q^{-1/2})`) | `0.4993203341836945` | **`2.5995155364`** |

C4 also confirms that `z_C` *is* the source of the circulating C weight vector:
solving the Markov system at `z_C` reproduces `(0.415396, 0.280930, 0.022745)`
to better than `1e-6`. So C is that parameter read literally against the
corpus's balanced `q`.

**Scope of the negative — (b), structural exclusion, invariant named.** The
invariant is the **integrality of a fibre dimension**, made usable by the
injectivity of `N ↦ z` proved above plus `ocneanu_param_eq_of_fibre_qdim`. C's
parameter is not the categorical trace on *any* fibre, because there is no
object of quantum dimension `[2.5995…]_q`. This is a claim about C's
*candidacy as the mass channel's trace*, and it is conditional on the corpus's
own definition of the mass as a categorical trace on `V^{⊗n}` (the block quoted
above). It is **not** a claim that C is not a Markov trace on `H₃(q)` — it is
one, a perfectly good member of the Ocneanu family, and every statement about it
as such stands.

A likely mechanism for how C entered, offered as an **observation, not a
finding**: on the Temperley–Lieb side the trace parameter is `δ⁻²` where
`δ = t^{1/2}+t^{-1/2}` is the loop parameter (Jones 1985, relation (V), read —
see below). C's value is `δ⁻¹`: the same expression at the wrong exponent, with
the corpus's balanced `q` standing in Jones's `t`. That would explain a value
sitting between the `N = 2` and `N = 3` traces without being either. I have not
established that this is what happened, only that the shapes coincide.

## Colour: the mass chain does *not* inherit the `N = 3` problem

The tension the reframing raised in both directions, resolved:

- **Pauli, in the mass channel.** Three spin-½ strands in a 2-dimensional fibre
  cannot be antisymmetrised. `dim V_{(1³)} = C(N,3) = 0` for `N < 3` —
  `weyl_dim_alt_eq_zero_iff` in
  [`RowCapObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/RowCapObstruction.lean),
  sorry-free on `main`. So `(1³)` is empty, and D follows.
- **Colour antisymmetry is still load-bearing elsewhere**, e.g. the eightfold
  chapter's open item 7 (spin–flavour–colour selection rule), which does need a
  three-row block. That block requires `N ≥ 3`, i.e. a genuinely 3-dimensional
  fibre and a **different** functor.
- **The two cannot be the same trace re-tuned.** `ocneanu_N_lockin_probe.py`
  (bean `qou-w5fw`, 2026-08-07) shows `y_(2,1)/y_(3) = q[2]_q[N−1]_q/[N+2]_q`
  differs at every `q` tested, so moving to `N = 3` re-weights the *surviving*
  channels and changes `tr_M` on elements the mass pipeline already evaluates.
  `HnMarkovTrace.lean` types the Ocneanu parameter as a free class field, so two
  instances are typeable today — the separation is mandatory, not optional.

So the significant consequence the reframing anticipated lands on the
**favourable** side: because the mass channel does not need colour
antisymmetry, it does not inherit the unsolved `N = 3` construction
(`qou-8p1x`). That construction remains open, and remains necessary for the
flavour/colour chapter — but it is not a blocker on the mass chain.

## Literature: what was checked, and what could not be

Honest accounting, because the corpus names "the Wenzl `z`-trace" and "the
full-Hecke Ocneanu trace" throughout while citing neither author.

**Read.** `library/s0273-0979-1985-15304-2/S0273-0979-1985-15304-2.pdf` = Jones 1985, *A polynomial
invariant for knots via von Neumann algebras*, Bull. AMS **12**(1) 103–111,
DOI `10.1090/S0273-0979-1985-15304-2` (corpus key `jones1985`, metadata already
verified in `references.ts`). Bearing on this question:

- **p. 2, relations (I)–(VI).** On the algebra `A_n` generated by projections
  `e_i` with `e_i e_{i±1} e_i = t/(1+t)² e_i`, the trace is *"completely
  determined by the normalization tr(1) = 1"* together with cyclicity **(IV)**
  and the single Markov relation **(V) `tr(w e_{n+1}) = t/(1+t)²·tr(w)`** for
  `w ∈ A_n`; *"Conditions (I)–(VI) determine the structure of A up to
  ∗-isomorphism."* This is the literature form of *a trace that factors through
  Temperley–Lieb has no residual freedom*, and the parameter is **one specific
  number**, not a free knob. It is an independent, upstream corroboration of
  what `MarkovTraceTLUniqueness.lean` proves from the Markov axioms alone.
- **`t/(1+t)² = 1/(t^{1/2}+t^{-1/2})² = δ⁻²`** — the exponent observation used
  above.
- **p. 5, Theorem 12:** `t⁻¹V_{L⁻} − t·V_{L⁺} = (√t − 1/√t)·V_L` — the
  **one-variable** Jones skein, i.e. the `N = 2` specialisation, not the
  two-variable HOMFLY.
- **p. 9, reference [24]:** *"H. Wenzl, On sequences of projections, Univ. of
  Pennsylvania, 1984 (preprint)"* — cited by Jones on p. 2 for the constraint
  that an arbitrarily large family of such projections exists only for `t` real
  positive or `t = e^{±2πi/k}`.

**Not obtainable in this sandbox.** Recorded so the next agent does not repeat
the attempts:

| Wanted | Status |
|---|---|
| `jones1987` (Ann. Math. 126(2) 335–388, DOI `10.2307/1971403`) — constructs the two-parameter trace, i.e. the C-vs-D family | paywalled; **cited as existing, no claim attributed to it** |
| `geck2000`, `kassel1995` (in `references.ts`, verified metadata) | paywalled |
| Wenzl, *Hecke algebras of type Aₙ and subfactors*, Invent. Math. 92(2) 349–383, DOI `10.1007/BF01404457` (corpus key **`wenzl1988`**, already in `references.ts` with verified metadata) | entry exists; **PDF not obtainable**, so the weight-vanishing-for `ℓ(λ) > N` result is *believed standard, not verified in-sandbox* |
| FYHLMO 1985, *A new polynomial invariant of knots and links*, Bull. AMS 12 (1985) — the Ocneanu/HOMFLY side | `www.ams.org` is **egress-blocked** (`curl: (56) CONNECT tunnel failed, response 403`; `WebFetch` → `EGRESS_BLOCKED`). **No `ref()` entry added** — metadata unverified in-sandbox. |
| any of it via `paper-search` MCP | **broken**: `search_crossref`, `search_openalex`, `search_arxiv` all return `[]`, and `get_crossref_paper_by_doi("10.1007/BF01404457")` returns `{}` for a DOI known good |

No new `ref()` entry was added and `references.bib` was not touched. The
statements labelled "standard" above that I could not open are labelled
**believed, not verified in-sandbox**.

Correction to a claim made mid-session: `references.ts` does **not** lack Wenzl.
`grep -n "wenzl19" content/schema/references.ts` returns `wenzl1987`,
`wenzl1988`, `wenzl1988b`, `wenzl1988c`, `wenzl1990`, `kazhdanwenzl1993`. Only
**Ocneanu** and **FYHLMO/Freyd** are genuinely absent.

## What this does not settle

- **That `dim V = 2` is the right fibre on physical grounds.** It is an *input*
  here, taken from `lem:feynman-eigenbasis-decomposition` and
  `thm:su2-emergence` (`Aut^⊗(τ) ≅ SU(2)`, fibre `V = ℂ²`). What is new is that
  the input **suffices** — it leaves no freedom. Per AGENTS
  §"Conditional-proved ≠ premise-established": the Lean proves the implication;
  the premise is the corpus's, and is cited, not re-derived.
- **The `N = 3` construction** (`qou-8p1x`) remains open. Nothing here advances
  it; the finding is that it is not on the mass chain's critical path.
- **The 195 ppm.** Nothing here changes a production number, and none was
  changed. D was already what production computes; this says why it is the
  right one.

## Follow-ups

1. **Correct the Scope note** of `prop:h3-markov-wenzl-weights`
   ([`h3-markov-wenzl-weights-context.md`](../../content/quantum-observable-universe/mass-theory/h3-markov-wenzl-weights-context.md)),
   lines 8–24: mass/binding use the **Jones/TL (`N = 2`)** trace, and the
   "insensitive to the distinction" sentence is false on `β_Bor`. Own commit,
   `.qa.json` sidecar refreshed, render-QA gate (the file is math-bearing).
2. **Errata in `feynman-markov-identification.md`**: the quoted
   `w_λ = dim_q(V_λ)·dim(S_λ)/dim_q(V^{⊗n})` has `dim(S_λ)` in the weight rather
   than in the normalisation identity, so pairing it with an unnormalised
   `tr_{S_λ}` gives `tr_M(1) ≠ 1`. The Frobenius weight is
   `y_λ = dim_q(V_λ)/dim_q(V^{⊗n})`. Same commit as follow-up 1 (adjacent block,
   same reviewer context).
3. **Add `ref()` entries for Ocneanu and FYHLMO** when metadata can be verified
   — the corpus names both throughout and cites neither.
4. Consider hanging the new Lean off a content block so it is covered by the
   per-block checkers (a standalone library file under `lean/QOU/**` has no
   `.qa.json` sidecar and is checked by nothing but the authoring agent, per
   AGENTS §"QA is agent-owned").
