# Walking the canonical chain: where do conditions emerge? (2026-09-14)

**Bean** `qou-u96j` · **Probe**
[`computations/audits/canonical_chain_condition_walk_probe.py`](../../computations/audits/canonical_chain_condition_walk_probe.py)
(5/5, exit 0)

## What this asks

[`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
states the chain as eleven steps from the substrate `q₀` to MeV observables, each
written as though its output follows from its input. This walk asks a different
question at each step: **what condition enters that the previous step does not
force?**

A condition being unstated is not the same as its being wrong. Everything below
is scope (a) — measured observations about what the corpus contains, with no
invariant excluding any reading. The reason to surface them anyway is that the
cheat sheet is, in its own words, "the PRIMARY coordination document for the
canonical chain": it is what agents reason from.

## 🛑 This is a PARTIAL walk

Measured here: **steps 5, 6 (partially) and 10**. Step 2's condition is already
documented in the cheat sheet itself and is cited, not re-derived.

**Not yet walked: steps 1, 3, 4, 7, 8, 9, 11.** Named so the gap is visible
rather than implied. Step 3 in particular is expected to carry one (the Markov
trace's "unique" is unique *given* a parameter `z`, which is the fork
`qou-99qc` / `qou-qqm4` have been carrying) but this walk did not establish it
from the corpus and so does not assert it.

---

## Step 2 — the geometry→algebra bridge (already documented)

The cheat sheet's own §2a records it, downgraded from "✅ proved" on 2026-08-25:
the curvature 2-form is **stipulated** to be the Hecke quadratic, so setting it
to zero recovers it tautologically, and `prop:hecke-spectral-sequence` has **0
`label:` declarations** in `content/`. Cited here for completeness of the walk;
nothing in this audit adds to it.

---

## Step 5 — Wedderburn + partitions

The step is stated as

> `H_n(q) ≅ ⊕_{λ ⊢ n} M_{d_λ}(ℚ(q))`;  `tr_M = Σ_λ y_λ χ^λ`

— a sum over **all** partitions of `n`.

> ### 🛑 Read §"Step 3" below before C5a — it corrects C5a's framing
>
> C5a as first written called the two-row cap *"a condition the chain's step
> statement does not carry"*, which reads as though it were a truncation bolted
> on at step 5. **It is not.** The cap is derived in the corpus from the step-1
> choice of the fibre `V`, and it is what *forces* the Markov parameter. What
> step 5's statement omits is the **hypothesis**, not the truncation. The
> measurement in C5a is correct; its emphasis was wrong.

### C5a — the sum runs over TWO-ROW partitions only

Measured against the committed `computations/y-lambda-at-q0.witness.json`
(anchor `proton`, `q₀ = 1.1099785827513808…`): at **every `n` from 2 to 12**,
every `y_λ` whose partition has **three or more rows is exactly 0**, and every
nonzero one has **at most two rows**. At `n = 12` that is 7 nonzero against 70
zero.

The production family is `y_lambda_su_n(n, q, 2)` — the trailing `2` is a row
cap. AGENTS.md does say "convention D = the two-row truncation", so the fact is
known; what is missing is that **the chain's own step statement does not carry
it**. An agent reading step 5 would expect a sum over all `p(n)` partitions.

### C5b — `α` is not an ad-hoc ratio; it is a Wenzl weight

`y_(3)` at `n = 3` equals `(q⁴+1)/(q²+1)²` **exactly** (agreement to 45 dps;
`|diff| = 5.0e-47`, at the witness's serialization floor).

That is the same `α` the 2026-09-08 `Q_β` ruling names as the
augmentation-to-`z_D` factor, and the same `α` that
`QOU/Hecke/MarkovCrossingReversal.lean` (#7334) found relating the two admissible
cells of the flavour split. It was the **trivial block's Wenzl weight** all
along. Two arcs that reached `α` independently were both reaching this.

### C5c — the normalisation is dimension-weighted

`Σ_λ d_λ · y_λ = 1` exactly at every `n` from 2 to 12. This is just `tr_M(1) = 1`
expanded, since `χ^λ(1) = d_λ`.

The **unweighted** `Σ_λ y_λ` is 1 only at `n = 2`, where every `d_λ` is 1, and
then falls away: 0.7527, 0.5666, 0.3804, … , 0.0133 at `n = 12`.

**Recorded because the author got it wrong first.** My initial reading of the
witness was the unweighted sum, from which I drew a false "the `y_λ` are not a
probability measure" conclusion. They are one, under the correct weighting. This
is also distinct from the `w_λ(q)` non-normalisation AGENTS.md's notation
register describes (0.987 / 0.982 / … at `n = 3/4/…`) — that is the **quantum
Plancherel** family, a different object with different numbers, and the register's
"never conflate the three weight families" rule is exactly what keeps them apart.

---

## Step 10 — the confinement SDP

### C10a — `n_target` carries three inequivalent production meanings

The spec block
[`mba-step10-confinement-sdp.md`](../../content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step10-confinement-sdp.md)
declares *"Target net constraint `n_target ∈ ℤ≥0`"* — an **integer**. Measured at
source, the three production callers pass three different kinds of thing, each
citing a different authority:

| caller | value | kind | cites |
|---|---|---|---|
| `aK_via_lp_dual_hecke_basis.py:175` | `n_target = tr_M_atom` | **real** — a Markov trace | `prop:mass-coefficient-shadow-price` |
| `pn_alpha_lp_dual.py:375` | `target_net = float(pn_vec.sum())` | **real**, and α-dependent | its own `net(pn_α)` |
| `option_b_proton_mass_full_chain.py:588` | `n_target = float(n_gg)` | **integer** — γγ insertions | "AGENTS.md §LP/SDP duals" |

Only the third matches the declared type. `n_target` is the constraint that
*selects* `T_w`, so this is the condition that emerges at step 10 — and the
corpus does not have one definition of it.

*In fairness:* `option_b_proton_mass_full_chain.py` says in its own comment that
its `t = [1,1,1]` and `G = identity` are a "minimal end-to-end demo — replace
with full Gram for real chain", so it should not be read as the production chain.

### C10b — the cheat sheet states an objective the code does not have

The cheat sheet's §1 diagram and §2 table both render step 10 as

> `min ‖tr_M(T_w) 𝔈₀ − B_tgt‖` over GB-NF

The authoritative algorithm block has **no `B_tgt`**:

```
minimize   Σ_i t_i x_i
subject to net(x) = n_target,  G x ≥ 0,  x ≥ 0
```

and the canonical entry point is
`pyhecke.lp_dual_solver.solve_operator_selection_lp(t, G, n_target)` — no
target-binding argument exists in the signature.

**This defect points the safe way** — the document makes the chain look *more*
fitted than the code is — but it is in the primary coordination document, and an
agent reading it would conclude step 10 minimises distance to a measured binding
energy, i.e. that the chain fits AME at its selection step. It does not.

---

---

## Step 3 — the "unique trace", and where the fork actually roots

This was the next item; walking it **closed the question, in the direction
opposite to what I expected**, and corrects C5a above.

`rem:markov-axioms-primitive` states it correctly: axioms 1–2 (normalisation +
cyclicity) with an unspecified stabilisation parameter admit a **one-parameter
family**. So the cheat sheet's step 3 — *"Unique trace `tr_M`"* — is the
compressed form, and `z` is where the condition would enter.

**But the parameter is then forced, and the forcing is sorry-free:**

```
V = fundamental of SU_q(2)      ← the HYPOTHESIS, and the only one
  ⟹ ℓ(λ) ≤ 2                     lem:feynman-eigenbasis-decomposition
  ⟹ y_(1³) = 0
  ⟹ [+ faithfulness y_(2,1) ≠ 0]  markovWeights_eq_jones_of_threeRow_eq_zero
  ⟹ y_(2,1) = 1/[2]_q², y_(3) = (q⁴+1)/(q²+1)² = α, z = q³/(q²+1) = z_D
```

Verified symbolically and against the committed witness: `y_(3)` and `y_(2,1)`
both reproduce to 30 dps. So **`α` is not merely observed to equal `y_(3)` — it
follows**, as `y_(3) = 1 − 2/[2]_q²`.

**The competing root `z = q` is `markovWeights_degenerate_root`**: `y = (1,0,0)`,
so `y_(2,1) = 0` and the trace is **not faithful** on `TL₃` (`z·[2]_q = q²+1 ≠ q²`).

### What that does to the fork

This is a **derivation-first discriminator** on the fork `qou-99qc` / `qou-qqm4`
have been carrying, and it uses **no residual at all** — exactly the ranking
AGENTS.md's anti-fit rule demands. And it points **away** from the augmentation,
which is the cell that reproduced the flavour-split baseline *exactly* in #7334.

**Recorded, not acted on.** Which cell to adopt remains the owner's call; what
changes is that the call is no longer between two equally-derived options.

### And a measurement note

`grep -c sorry` on `MarkovTraceTLUniqueness.lean` returns **1**, and that hit is
the word inside a **comment** (*"sorry-free, `lean`-direct exit 0"*). The file has
no `sorry` tactic. Counting the word is not counting the tactic — I raised a false
alarm on it before checking.

---

## What the walk has produced so far

- **Step 3 + step 5 reduce to ONE condition**, and it sits at **step 1**: the
  choice `V = fundamental of SU_q(2)`. Everything else — the row cap, `y_(1³) = 0`,
  `z_D`, `α` — is derived from it, sorry-free.
- **`α` is derived**, not coincidental: it is `y_(3) = 1 − 2/[2]_q²`.
- **The augmentation is proved degenerate**, which informs the open fork without
  using accuracy.
- **Step 10 carries a genuinely open condition** (`n_target`, three meanings) and
  **the cheat sheet misstates step 10's objective**.
- Two self-corrections: the dimension-weighted normalisation, and C5a's framing.

---

## Steps 1 and 4 — where `V` comes from, and the cycle at the root

Step 3 left everything hanging on `V = fundamental of SU_q(2)`, so this walks it.

**Step 1 does not choose `V`.** `prop:braid-action-tensor` reads *"For each object
`V` in `𝐂`"* — the construction is for an **arbitrary** object.

**Step 4 does.** `why-b3.md`:

> *"The Descartes condition `χ(A) = −6` **forces** the gauge group to be a quantum
> form of `SU(2)`, which has rank 1. Consequently, the fundamental representation
> `V` is 2-dimensional."*

So the dependency runs **step 4 → step 1**, against the direction the chain is
drawn. That alone is worth recording: the chain is a line and the dependency is not.

### The cycle, and only half of it is declared

`chi-minus-six-chain.md` is the block that fixes `χ(A) = −6`. Its **Step 1** reads:

> ***"Step 1: Start with the QOU triple.** We have `(𝐂, A, τ)` with gauge group
> `G = SU(2)`."*

and Step 2 uses `G = SU(2)` to get the rank-2 bundle that Riemann–Roch then turns
into `χ = 2 − 2g`.

So:

```
why-b3            :  χ = −6   FORCES   SU(2)  ⟹  dim V = 2
chi-minus-six-chain: STARTS FROM  G = SU(2),  uses it at step 2
```

**Read as derivations, those form a cycle.**

The block *does* declare a different circularity, in its own words:

> *"Step 5, which fixes the branch-point count at six, reads that count off the
> Weierstrass points of Bring's surface — the surface the chain then identifies at
> Step 7 — so **the chain locates the value rather than deriving it from the axioms
> alone**."*

That candour is to its credit. **The step-1 assumption is the one it does not
declare**, and it is the larger of the two, because `dim V = 2` is what everything
downstream — the row cap, `y_(1³) = 0`, `z_D`, `α`, the flavour split — rests on.

### 🛑 What this is and is not

**This is not a claim that the mathematics is wrong.** Each block is sound read as
a *consistency* statement: "given the QOU triple with `G = SU(2)`, `χ = −6`
follows", and "given `χ = −6`, `SU(2)` follows" are both fine. The measured fact is
that neither derives `SU(2)` from anything prior, and that the condition the whole
chain rests on is **assumed at step 1 of the chain presented as deriving it**.
Scope (a): an observation about the corpus's dependency structure.

**There is a candidate independent route.** `cohomological-embedding.md` §(iv):

> *"Genus 4 is forced. The QOU axioms require `T_{2,3}` and `T_{2,9}` to embed, but
> `T_{2,11}` must not. This uniquely forces `g = 4` and `χ = −6`."*

This does not visibly assume `SU(2)` — but it takes a **knot-embedding pattern** as
input, which relocates the condition rather than removing it. Whether that route is
genuinely independent is **not settled here**.

### A rank contradiction, in passing

- `why-b3.md`: `SU(2)` *"has **rank 1**"* — correct.
- `descartes-knot-eigenbasis-derivation.md`: `χ = −6` *"sets the genus `g = 4` and
  gauge group `SU_q(2)` to **rank 2**"*.

`SU(2)` has rank 1; **2 is `dim V`**, not the rank. One of the two states a wrong
rank as a derived consequence of `χ = −6`.

---

## Answering (1): is there a route to `g = 4` that does not already hold `SU(2)`?

This was the walk's top-priority next question, because it is the one that would
break the cycle above. The corpus offers **three** routes to `g = 4` / `χ = −6`.
All three name `SU(2)` in their own first or last sentence, so **none of them
breaks the cycle** — and the third, which looked most promising because its
argument is combinatorial, turns out to state a criterion that its own genus
does not meet.

Measured in
[`genus_completeness_rank_probe.py`](../../computations/audits/genus_completeness_rank_probe.py)
(22/22, exact symbolic linear algebra over `ℚ(q)` — sympy `Symbol`/`Rational`
throughout, no float anywhere, so no precision claim arises).

### The three routes, each in its own words

| route | block | where `SU(2)` enters |
|---|---|---|
| 1 | `chi-minus-six-chain.md` | **step 1**: *"We have `(𝐂, A, τ)` with gauge group `G = SU(2)`"* — assumed outright |
| 2 | `cohomological-embedding.md` | closing line: *"the unique minimal environment that supports `SU₂` reconstruction"* |
| 3 | `genus-from-hecke-completeness-proof.md` | first line: *"The braiding on `V₁^{⊗n}` in `Rep(SU_q(2))` gives `H_n(q)`"* |

and `why-b3.md` supplies the return arrow — *"The Descartes condition `χ(A) = −6`
forces the gauge group to be a quantum form of `SU(2)`"*. So all three genus
routes sit **inside** the cycle rather than entering it from outside.

Route 3 is not even formally independent of route 2: its manifest declares
`uses: ["prop:cohomological-embedding"]`.

### 🛑 Route 3's completeness criterion is not met at `g = 4`

The proof's load-bearing sentence is:

> *"At `g = 3`: 4 evaluations cannot span a 5-dimensional space (rank ≤ 4). At
> `g = 4`: 6 evaluations span 5 irreps (verified numerically: the `6 × 5` matrix
> has rank 5 for all `q > 1`, `q ≠` root of unity). Therefore `g_min = 4`."*

and `vertex-algebra-relations.md` fixes what the matrix is:
`M_ij = χ_{λ_j}(T_{(r_i, s_i)})` over the irreps `λ ⊢ r` of `H_2(q) ⊕ H_3(q)`.

**`T_{r,s}` is the closure of a braid word on `r` strands**, so a row with
`r_i = 2` has support only in the two `H_2` columns and a row with `r_i = 3`
only in the three `H_3` columns. `M` is block-diagonal and rank is additive over
the blocks. At `g = 4` there are four `r = 2` rows (≤ 2 columns ⟹ rank ≤ 2) and
**two** `r = 3` rows (2 rows ⟹ rank ≤ 2):

```
rank(M) ≤ 2 + 2 = 4 < 5
```

This is structural — no `q`, no arithmetic. **No numerical verification at any
`q` could have returned 5.** Confirmed by exact symbolic rank, and the block
decomposition is measured rather than asserted (the `r = 2` rows' `H_3` entries
and the `r = 3` rows' `H_2` entries are checked to be the zero submatrices).

The full sweep is the decisive object:

| `g` | knots | (`r=2`, `r=3`) | rank | target | met? |
|---:|---:|:---:|---:|---:|:---:|
| 1 | 1 | (1, 0) | 1 | 5 | no |
| 2 | 2 | (2, 0) | 2 | 5 | no |
| 3 | 4 | (3, 1) | 3 | 5 | no |
| **4** | **6** | **(4, 2)** | **4** | **5** | **no** |
| 5 | 7 | (5, 2) | 4 | 5 | no |
| **6** | **9** | **(6, 3)** | **5** | **5** | **YES** |
| 7 | 11 | (7, 4) | 5 | 5 | yes |

Read three things off it.

- **The criterion is not blind** — the rank climbs 3 → 4 across `g = 3 → 4`, so
  the proof's *exclusion* of `g = 3` is correct on its own terms. Only the
  *acceptance* at `g = 4` is wrong, and it is wrong **by one**.
  *(I expected rank 4 at `g = 3` as well, i.e. that the criterion could not
  discriminate at all. That was wrong and the table corrected it; recorded
  because a negative claimed one way and true another way is worth more as the
  correction than as the claim.)*
- **`g = 5` adds nothing.** `T_{2,11}` is a fifth `r = 2` row against two `H_2`
  columns. Only a third `r = 3` knot can move the rank, and `T_{3,7}` has
  Seifert genus 6.
- **Taken self-consistently the criterion gives `g_min = 6`, not 4** — and at
  `g = 6` the proof's own restriction to `r ∈ {2,3}` lapses, because `T_{4,5}`
  has genus 6, `H_4` enters, and the target moves from 5 to 10. **The criterion
  has no fixed point at 4; pushed self-consistently it escalates.**

Every other reading falls short too. Stabilising all six words into `H_3` gives
a `6 × 3` matrix — rank ≤ 3 at any genus.

**And "verified numerically" has nothing behind it.** No producer in
`computations/` computes this matrix. (Two `computations/audits/*.witness.json`
name the lemma; both are corpus-wide *inventories* that list every block in the
tree — and one of them, `i1-no-probe-audit`, exists precisely to record which
blocks have no probe, so its hit is evidence for this point, not against it.)
The Lean carrier is declared `validation: "not_checked"`.

### 🛑 What this is and is not

**Scope (b), narrowly**, with a named invariant: rank subadditivity over a block
decomposition. The claim is that **this route's stated criterion cannot be met at
`g = 4`** — not at some `q`, at none.

It is **not** a claim that the genus is not 4, and **not** a claim against Bring's
surface. Routes 1 and 2 are untouched by it; `g = 4` may well be right, and route 2's
`T_{2,3}`/`T_{2,9}`/`T_{2,11}` embeddability arithmetic is independently clean
(1, 4, 5 against `g`, so `g ≥ 4` and `g < 5`). What is established is that route 3
cannot serve as the independent confirmation its `uses`-free reading would make it,
and that one sentence of it is false as written.

**It is also not a fitting finding.** Nothing here was selected against a target;
the criterion was taken exactly as the corpus states it and evaluated at every
genus, including the ones that do not help.

---

## Step 4 — "6 basis elements ↔ 6 torus knots" is a coincidence of counts

Walking one step further with the same tool. The cheat sheet's diagram renders
step 4 as

```
step 4. Bring χ = −6  ↓  6 basis elements ↔ 6 torus knots ↔ particle content
```

and its step table supplies the arithmetic: *"`dim H_3(q) = 6` = # embeddable
torus knots in `Σ_4`"*. The `↔` is load-bearing — it is what carries the genus
into the particle content.

**Two different sixes are being set against each other, and the corpus is
clearer about this than the diagram is.**
[`knot-operator-basis-table.md`](../../content/quantum-observable-universe/appendix-knot-operations/knot-operator-basis-table.md)
names the actual NF basis — `{γ, σ₀, σ₁, L₊, L₋, e⁻}` — and treats the torus
knots as **operators acting on** it, tabulating `b_i · β(T_{m,n}) · b_j` for
every basis pair and every knot. So the block does not claim the knots *are*
the basis. The diagram's arrow is what reads that way.

### The one linear-algebraic content the identification could have, measured

Do the six torus-knot braid words span `H_3(q)`? Exact symbolic rank over
`ℚ(q)` through the faithful representation `(3) ⊕ (2,1) ⊕ (1,1,1)` —
`1 + 4 + 1 = 6` matrix coordinates, so by Wedderburn the span of the six image
vectors **is** the span of the six words in the algebra, not merely of their
characters:

```
rank = 4,  against dim H_3(q) = 6
```

and the reason is structural, so it holds at every `q`:

| | words | span |
|---|---|---|
| 2-strand `T_{2,3}, T_{2,5}, T_{2,7}, T_{2,9}` | 4 | **2** |
| 3-strand `T_{3,4}, T_{3,5}` | 2 | **2** |
| | | **4 < 6** |

`σ₁^s` collapses into `span{1, σ₁}` by the Hecke relation, so **any** number of
`T_{2,s}` spans at most 2 — measured at seven of them (`s = 3…15`), still 2.
Adding `T_{2,11}` at `g = 5` adds nothing, exactly as in the genus sweep.

**This is the same 2 + 2 as §"Answering (1)", from the same cause**, one level
down: there the four 2-strand rows filled two `H_2` columns and the two
3-strand rows two of three `H_3` columns; here the four 2-strand words fill a
2-dimensional subalgebra and the two 3-strand words 2 more. One structural
fact — *the six knots are four copies of a 2-dimensional story plus two more* —
surfacing in both a character space and an algebra.

[`step4_torus_knot_span_probe.py`](../../computations/audits/step4_torus_knot_span_probe.py),
17/17, exact over `ℚ(q)`, no float. The `(2,1)` irrep is solved from the braid
relation rather than transcribed, with braid and Hecke relations asserted in
all three irreps.

### 🛑 WITHDRAWN — the cheat sheet's own §9.5 answers this, and I had not read it

Everything above is arithmetically correct and **its conclusion is withdrawn.**

[§9.5 of the cheat sheet](../canonical-derivation-cheat-sheet.md) names the
diagram's six explicitly — `{1, σ₁, σ₂, σ₁σ₂, σ₂σ₁, σ₁σ₂σ₁}`, the **GB basis of
`H_3`** — and exists precisely to correct *"a recurrent agent confusion …
reading '6 basis elements' as **6 independent** SM-equivalent operators"*. It
calls them **GENERATORS** whose multiplicative closure climbs the GB/jet tower.

So the right question is not what the six knots **span** but what they
**generate**. Measured:

| | |
|---|---:|
| span of the six knot words | **4** of 6 |
| **subalgebra generated** by them (products alone, no inverses) | **6 of 6** |

**Under the reading §9.5 tells readers to use, the six torus knots do generate
`H_3(q)`.** So *"the `6 ↔ 6` is a coincidence of counts, not a linear-algebraic
identification"* is **too strong and is withdrawn**: there is a correct
algebraic sense in which the six knots answer to the six-element basis.

What the span measurement *does* refute is the **basis** reading — which §9.5
refutes already, at greater length, and calls a recurrent agent confusion. **So
this section corroborates the corpus rather than finding a defect in it.**

The one narrow residue: the §1 diagram's bare `↔` still invites the basis
reading, and §9.5 sits ~700 lines below it.

Also note `{γ, σ₀, σ₁, L₊, L₋, e⁻}` is a **third** six, from a different
appendix, and is not what the diagram means — I reached for it because I had not
read §9.5.

**Scope (b) now applies only to the arithmetic** (span = 4 of 6, at no `q`),
**not to any reading of the diagram.**

---

## Step 11 — 🛑 the cheat sheet's hadronic `𝔈₀` inverts what step 11 derives

The step table gives **two** forms for the energy scale at step 9:

```
step  9.  𝔈₀ = m_e/(q₀(q₀−1)) = m_e c_q² ℏ_q    (lept)
          𝔈₀ = Q_β / |h(h−2)/2|                  (had)
```

and step 11 as `Q_β = |Δ(net(T_w))|·𝔈₀`, with `Δ(net) = h(h−2)/2 ≈ −0.1872071945`
for the free neutron. Substituting the hadronic form:

```
Q_β  =  |h(h−2)/2| · ( Q_β / |h(h−2)/2| )  =  Q_β
```

**identically.** Read literally, **step 11 derives its own input.** This is
AGENTS.md §"Derive-then-check" item 8 verbatim: *if it is true by unfolding, it
is notation, not a derivation.*

### The circularity is convention-independent

Which is what makes it worth recording. Whichever functional `Δ(net)` turns out
to be — the retired `z = 1` cell, the augmentation at `z = q`, or the **ruled**
Markov trace at `z_D = q³/(q²+1)` (owner ruling 2026-09-08) — defining
`𝔈₀ := Q_β/|Δ|` and then computing `Q_β := |Δ|·𝔈₀` is an identity. **The
`qou-99qc` fork cannot repair it.** Demonstrated over exact rationals at four
values of `Δ`, including one nine orders of magnitude from any physical scale.

### What the hadronic form actually is

At the proton pin:

| | MeV | |
|---|---:|---|
| `𝔈₀` leptonic, `m_e/(q₀(q₀−1))` | 4.1859813633 | step 9 |
| `𝔈₀` **tower-summed** | 4.2274833556 | **production** |
| `𝔈₀` hadronic, `Q_β/|Δ|` | 4.1789708525 | cheat sheet |

`𝔈₀^lept / 𝔈₀^had = 1.00167757` — a gap of **0.1678 %**, which *is* the famous
"0.17 % vs CODATA" for `Q_β`. So the hadronic line is **that agreement written
backwards**: not a second, independent determination of `𝔈₀`, but the first one
with the residual divided out. And AGENTS.md **retires** that cell as the base
(owner ruling 2026-09-08), so the line carries no content the corpus still
stands behind.

### Production does not do this

The live producers carry a **closed substrate expression with no `Q_β` in it** —
found in four `computations/qbeta/` files:

```python
E0 = M_E/(Q0*(Q0 - 1))/(1 - HBAR_Q**2)      # tower-summed, as ruled
```

So the defect is in the **primary coordination document, not the compute** —
the same class as C10b above, but worse: C10b makes the chain look *more fitted*
than it is, while this one makes a derivation step **vacuous**.

With the production `𝔈₀`, `|Δ|·𝔈₀ = 0.7914152989` MeV against CODATA
`0.7823334` — **+1.161 %**, a number that *can be wrong*, which the hadronic
form's exact 0.00 % cannot.

> 🛑 **Do not quote that +1.161 % as the framework's `Q_β` accuracy.** It is a
> **mixed cell** — the old functional `Δ(net) = h(h−2)/2` against the new
> tower-summed `𝔈₀`. The ruled cell is `ε` = the Markov trace at `z_D` on the
> γγ-selected element, recorded in AGENTS.md at **−16.678 %** and itself scored
> on an element the confinement SDP rejects (owner ruling 2026-09-13). Quote
> the witness.

[`step11_qbeta_e0_circularity_probe.py`](../../computations/audits/step11_qbeta_e0_circularity_probe.py),
10/10, mpmath `dps = 60`, no float64.

> **Two corrections inside this probe, both mine, both the error classes the
> walk keeps finding.**
>
> 1. **I asserted bit-equality at `dps = 60` for an arbitrary `Δ`, and it
>    failed** on `π/10` — correctly. Bit-equality is a claim about the
>    *arithmetic*; the identity is *algebraic*, and holds bit-exactly for `dnet`
>    only because that division round-trips. The demonstration now runs over
>    exact rationals, which is the honest way to show an algebraic identity —
>    asserting it in floating point would have been exactly what AGENTS.md names
>    as reporting an arithmetic floor as exactness.
> 2. **The precision gate caught a laundering defect in the probe itself.**
>    `mpf(str(Q))` pushes a **float64** through a string into a 60-dps
>    computation; `f64-into-mpmath` flagged it, and the fix is
>    `mpf(Q_50_DIGIT_STR)`. The same pass found I had hardcoded `Q_β` as
>    `0.7823334` from AGENTS.md prose when the live table carries
>    `Q_NEUTRON_MEV = 0.7823334093099085` — 1.2e-8 relative away, which moved
>    `𝔈₀^had` in its 9th digit (4.1789708027 → **4.1789708525**) and the gap
>    from 0.167758 % to 0.167757 %. **The conclusions are untouched**; only
>    these figures were wrong, and they are the figures quoted above.

### 🛑 What this is and is not

**Scope (b)** for the narrow claim, invariant = the algebraic identity
`|Δ|·(X/|Δ|) = X` for `Δ ≠ 0`: the cheat sheet's hadronic `𝔈₀`, substituted into
step 11, cannot produce a falsifiable `Q_β`.

It is **not** a claim that `Q_β` is circular in the framework — production is
not circular, and the measurement above is what establishes that. It is **not**
a claim about which `Δ` is right (that is `qou-99qc`, an owner call). What is
established is that **one line of the primary coordination document makes a
derivation step vacuous**, and that the code it summarises does not.

---

## Steps 7–8 — the diagram's arrow is not a `uses[]` edge

The step table already flags step 8's carrier honestly:
`conj:jet-convergence-classical-limit` — *"(conjecture, not prop — corpus
kind)"*. That is not the finding. **It is a *dependent* conjecture**, though:
its own `uses[]` is `["conj:jet-filtered-knot-factor"]`, so step 8 stands on a
second conjecture beneath it, which the table does not say.

The walk's question — if steps 9–11 are downstream of a conjecture, do they
declare it (AGENTS.md §3b)? — turns out to have a prior question in front of
it. Measured over the corpus's own dependency graph (3565 labelled blocks
parsed from the `.ts` manifests):

| step | carrier | cone | reaches the named 7/8 carriers |
|---|---|---:|---|
| 9 | `prop:atom-knot-mass-derivation` | 79 | **none** |
| 10 | `prop:confinement-sdp` | 3 | **none** |
| 11 | `prop:neutron-qvalue-symbolic` | 102 | **none** |

**🛑 But that is a statement about LABELS, not about dependence — and my first
framing got it wrong.** I wrote it as *"steps 9–11 stand independently of the
GB/jet machinery"*. They do not: step 9's cone **does** reach
`prop:jet-prefix-gb-filtration`, the same machinery under a different label.
Section 4 of the probe is the measurement that caught it. This is the *grep the
claim shape, not the topic* failure one label over.

So the honest, narrow statement: **the diagram's arrow is not a `uses[]` edge,
and the blocks it names for steps 7–8 are not the blocks the dependency graph
routes through.** An agent tracing the chain formally, by the manifests, will
not find what the cheat sheet sends it to.

Conjecture counts in the cones, for completeness: step 9 has **4**
(`conj:canonical-knot-id-sdp`, `conj:brane-tower-z-habiro`,
`conj:confinement-grading-correspondence`, `conj:crystal-graph-realization`)
by two independent routes; steps 10 and 11 have **zero**.

[`chain_uses_graph_vs_diagram_probe.py`](../../computations/audits/chain_uses_graph_vs_diagram_probe.py),
12/12. Manifest parsing and graph reachability only — no arithmetic, so no
precision question arises.

### 🛑 Prior art — what this pass deliberately does NOT report as new

Two things this data invites re-reporting, both already in the corpus and found
by corpus-grep **before** anything was written:

- **`prop:atom-knot-mass-derivation` is an already-adjudicated §3b-cond item-5
  violation.** Its Lean carries `[h : AtomKnotMassDerivationConjecture]` and
  the class field's type is character-for-character the theorem's conclusion,
  discharged by `h.atom_knot_mass_derivation cert T_w` — a bare projection.
  Bean **`qou-tmmt`** (2026-09-04) adjudicated 9 candidates, confirmed 8
  including this one, and is still `todo`.
- **`MassIdentity` reduces to `B_pred ≥ 0 ∧ |B_pred − B_AME| ≤ B_AME/4`** — a
  25 % tolerance against AME, so even a repaired conditional theorem would
  assert agreement-within-25 %, not the mass identity the `.md` states. The
  Lean docstring says so, and it is reported in
  [`2026-06-07-proof-rater-baseline-audit.md`](2026-06-07-proof-rater-baseline-audit.md).

Recorded because the checklist is what stopped a re-derivation here, not
because the findings are mine. **What survives as new from this pass is the
graph measurement alone.**

---

## Step 9 — the exit to ℝ is correctly scoped, under one undefined symbol

This is the step where the chain crosses from `ℚ(q)` to ℝ, so it is where an
unstated condition would matter most. **It is the most carefully written step
in the chain**, and the finding here is correspondingly small.

The carrier is `def:archimedean-realization-functor`,
`𝓡_top : 𝓜̂ →^{χ_top} 𝓜̂ ⊗ ℤ →^{π_∞} ℝ`. The block **withdraws its own name**:
*"The word 'functor' in the name and label is **legacy** … `𝓡_top` is a
realization / evaluation — a ring homomorphism out of `K_0(Var)` — not a functor
between categories."* That candour is the opposite of a defect and is worth
saying, given how much of this walk is about documents overstating.

**The condition that enters is declared: the agreement is SCOPED.** The
follow-on remark states

```
𝓡_top  =  τ_arch  :=  π_∞ ∘ τ      on  𝓜̂_QOU ⊆ 𝓜̂
```

so `τ`'s status as *"the exclusive exit from the categorical substrate to the
real numbers"* is established **on a subdomain**, not in general. That is a real
condition, correctly flagged.

### 🛑 The one defect: `𝓜̂_QOU` occurs once in the corpus and is defined nowhere

The same agreement is stated **three times under two names**:

| block | scope named | resolves? |
|---|---|---|
| `archimedean-realization-functor-interpretation.md` | `𝓜̂_QOU` | **no — 1 occurrence corpus-wide** |
| `vol-through-tau.md` | "the algebraic quantum volume" | yes — `def:algebraic-quantum-volume` |
| `vol-as-motivic-period.md` | "the algebraic quantum volume domain" | yes — same |

Measured across every `.md` under `content/`: **`\widehat{\mathcal{M}}_{\mathrm{QOU}}`
appears exactly once**, in the sentence that uses it. Its two siblings state the
identical claim scoped to a **defined** block. So this is a **one-symbol fix** —
the remark should say what its siblings say.

### What is NOT claimed

**Not** that `χ_top` is ill-defined. The remark does allow it to be *"an integer
(Euler characteristic) **or** a refined Hodge-theoretic invariant like hyperbolic
volume"* — two invariants with different codomains under one name — and `χ_top`
has **no notation-register entry**. That is an overload worth noting, but the
blocks that *use* it scope it to the volume domain, so it is recorded here and
not measured as a defect.

**And not** that step 9 hides a condition. It declares one. The contrast with
step 11 is the point: both steps concern the crossing to ℝ, and step 9 states
its scope while step 11's `𝔈₀` line quietly inverts its own output.

Pinned in section 8 of
[`canonical_chain_condition_walk_probe.py`](../../computations/audits/canonical_chain_condition_walk_probe.py)
— four exact quotes asserted at source plus the corpus-wide `𝓜̂_QOU` count.

---

## 🛑 Step 7, and a process failure of mine worth more than the finding

Walking step 7's interior turned up that the step-9 theorem's *hypotheses* are
free:

```lean
def gbSpectralCollapsePage : ℕ := 2
def GbSpectralSequenceCollapseAtE2 : Prop := gbSpectralCollapsePage = 2   -- 2 = 2
def YekutieliFiniteSliceMultiplicativeTrace (T_w : Type*) : Prop := Nonempty T_w
```

and both are hypotheses of `atom_knot_mass_derivation`. **This is already
reported**, verbatim, in
[`2026-09-08-l2-1ppq-research-program-gaps.md`](2026-09-08-l2-1ppq-research-program-gaps.md)
row 7 — *"`gbSpectralCollapsePage := 2` and `GbSpectralSequenceCollapseAtE2 :=
(2 = 2)` — **true by definition**"*, bean **`wpdb`**. I re-derived it. Credit
there, not here.

**In fairness to the Lean: it declares this itself.** Its docstrings say
*"pinning the collapse page to 2 by construction. Genuine content … awaits
Mathlib spectral-sequence support"*. That is honest authoring, not laundering —
the gap is stated at the site.

### The process miss

**That audit walks the same chain, step by step, and I did not find it until
step 7.** Every corpus-grep I ran was scoped to the *finding* — "has anyone
questioned the rank-5 claim", "is `M̂_QOU` defined" — and none asked the prior
question, *"has anyone walked this chain?"*. The checklist exists for exactly
that, and a topic-scoped grep is how it gets skipped without feeling skipped.

### Measured overlap, so the next reader does not have to re-check

| my defect | in `2026-09-08`? |
|---|---|
| #1 step-11 hadronic `𝔈₀` circularity | **no** (line 412 is q₀'s "third determination", a different circularity) |
| #2 `g = 4` rank-5 unmeetable | **no** — zero hits for rank-5 / completeness / `genus-from-hecke` |
| #3 step-4 `6 ↔ 6` span = 4 of 6 | **no** (its row 4 is the *Lean absence* and a 7-generator count — adjacent, different claim) |
| #4 steps 7–8 `uses[]` vs diagram | **no** |
| #5 step-9 `𝓜̂_QOU` undefined | **no** |
| step-7 `2 = 2` hypothesis | **YES — prior art, bean `wpdb`** |

Its step-10 row is **close to but not the same as** C10a above: it names
`nucleus_operator_selection_sdp.py` sweeping `n_target = |tr_M(W_atom)|` as
*"circular as a selector"*, i.e. one caller; C10a measures **three inequivalent
production meanings** across three callers against a spec declaring
`n_target ∈ ℤ≥0`. Read together rather than as duplicates.

### One small thing that does look new

The **collapse page disagrees across artifacts**: the cheat sheet says `E_2` in
three places (line 49 "🟢 derived", the line-167 diagram, the line-254 step
table), while `prop:spectral-sequence-collapse`'s own statement says the
sequence *"collapses at `E_1`"*. Collapse at `E_1` is **strictly stronger**
(all differentials vanish a page earlier), and the block's stated reason —
`HH^k(A,A) = 0` for semisimple `A` — is an `E_1` argument. So the cheat sheet
**understates** its own proposition. Safe direction, like C10b, and stated
cautiously: the 2026-09-08 audit's row 7 says "collapse at `E_2` is a class
field" and does not raise `E_1`, so this appears unreported, but it is a small
claim and I have not searched for it exhaustively.

---

## Where the walk stands

The chain's conditions do not accumulate step by step — they **converge on one**:

```
χ = −6  ⇄  G = SU(2)  ⟹  dim V = 2  ⟹  ℓ(λ) ≤ 2  ⟹  y_(1³)=0  ⟹  z_D  ⟹  α
   ↑ cycle, half-declared        └──────── all of this is sorry-free ────────┘
```

Everything to the right of `dim V = 2` is **derived and sorry-free**. Everything to
the left is a cycle with one leg undeclared. Step 10's `n_target` is the one
*separate* open condition found.

**(1) is now answered and the answer is no** — all three corpus routes to `g = 4`
name `SU(2)` in their own first or last sentence, so **the cycle is not broken by
anything currently in the corpus**, and one of the three states a criterion its own
genus misses by one (§"Answering (1)" above).

**Next**, in priority order:

1. **The `g = 4` completeness sentence needs an owner decision.** It is false as
   written and has no producer. Three dispositions, none taken here: re-scope it
   to what the rank sweep shows (the criterion is first met at `g = 6`, which
   does not support `g = 4`); restate the criterion so `g = 4` meets it (what
   *should* the target dimension be, if the observables are Markov traces and
   `y_(1³) = 0` makes one of the five directions unobservable?); or retire the
   route, since it `uses` route 2 and is not independent anyway. This is a
   judgement about what the argument was meant to say, which is the author's,
   not mine.
2. ~~**The cheat sheet's step-4 arrow**~~ — **WITHDRAWN.** §9.5 of the cheat
   sheet already names the six as the GB basis and calls them *generators*,
   and measured, the six knots **do generate `H_3`** (6 of 6). Only the basis
   reading fails, and §9.5 refutes that itself. Residue: the §1 diagram's bare
   `↔` invites the reading §9.5 sits 700 lines below correcting.
3. **The cheat sheet's hadronic `𝔈₀ = Q_β/|h(h−2)/2|`** makes step 11 vacuous
   as written, and is the 0.17 % agreement inverted — a cell the corpus has
   retired. Production is not circular. **Highest priority of the three
   document fixes**, because a vacuous derivation step is worse than an
   overstated correspondence. **Default if nothing is done:** an agent reading
   step 9 + step 11 together concludes `Q_β` is derived when that reading
   derives nothing.
4. **The rank contradiction** (`why-b3` "rank 1" vs `descartes-knot-eigenbasis`
   "rank 2") — still a one-line fix someone should own.
5. **The cheat sheet's step-7/8 labels** do not match the blocks the `uses[]`
   graph routes through (`prop:jet-prefix-gb-filtration`, not
   `prop:gb-spectral-sequence` / `conj:jet-convergence-classical-limit`). The
   cheapest of the four document fixes. **Default:** an agent tracing the chain
   by the manifests keeps not finding what the diagram names.
6. **All eleven steps are now walked** at least to the level of "what condition
   enters". What is *not* done is the interior mathematics of steps 7–9 — the
   GB spectral sequence's actual collapse, and the Archimedean realisation
   functor, whose absence is what `MassIdentity`'s 25 % tolerance stands in
   for.

Note what (1) does *not* threaten: `g = 4` itself. Route 2's embeddability
arithmetic is clean and independent of this defect.
