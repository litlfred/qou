# γγ word selection, step 11 — the interface bond's response is one-body at every placement

Bean `qou-ales`. Branch `claude/ales-step11-dineutron-channel-2026-09-12`, PR #7249.

Step 10 derived the pp response `r = (μ − 1)/h²` in closed form and described it as "the
trace-weighted response over **the two** free 11-letter nucleon words". This step extends the
same exact computation to all four ordered channels and all four interface vertices, and finds
that description too generous: `r` depends on **one** nucleon, at every placement.

Two of the three things this step establishes were **already the corpus's position** and are
cited rather than asserted here. One is new. Section 6 separates them, because getting that
wrong is the failure this repo's corpus-grep rule exists to prevent — and I got it wrong twice
before writing this document.

## 1. The geometry, and why there is no symmetric choice

Nucleons occupy generators `{0,1}` and `{3,4}` of `H₆` — strands 1–3 and 4–6 — so the interface
is the **single** generator `2`. A γγ vertex is `σ_g σ_{g+1}⁻¹`: it occupies **two adjacent**
generators, exactly one of them inverted. Since an adjacent pair has two distinct elements and
`{2}` is a singleton, **no vertex sits on the interface alone**. A vertex touching the interface
is `{1,2}` or `{2,3}`, and either way it **borrows** one generator from one nucleon.

Four vertices exist — two positions × which letter carries the inverse:

| | word | inverted letter | borrows |
|---|---|---|---|
| **V1** | `σ₂σ₃⁻¹` | the **borrowed** one | `σ₃`, right |
| V2 | `σ₃σ₂⁻¹` | the **interface** one | `σ₃`, right |
| V3 | `σ₁σ₂⁻¹` | the **interface** one | `σ₁`, left |
| V4 | `σ₂σ₁⁻¹` | the **borrowed** one | `σ₁`, left |

`V2 = V1⁻¹` and `V4 = V3⁻¹` as group inverses. V1 is the canonical one:
[`GammaGammaH6Interface.lean:223`](../../content/quantum-observable-universe/lean/QOU/Mass/GammaGammaH6Interface.lean)
defines `interfaceBond (m) := shift 2 (vertexPow m)` as a plain `def` with **no derivation of
`shift 2`**, and steps 6–10 use it exclusively.

Formalised sorry-free in
[`InterfaceVertexArity.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/InterfaceVertexArity.lean):
`no_vertex_on_interface_alone`, `straddles_iff` (exactly two positions), and
`interfaceVertex_borrows_exactly_one_side` (each meets exactly one nucleon support, never both
and never neither). **Every placement breaks the pair's left–right symmetry by construction.**

## 2. The new result: every vertex's response is one-body, in the slot it borrows from

Exact over `ℚ(q)`, convention D, `H₆`, all 16 vertex × ordered-channel combinations. The
deviations below are **symbolic identities**, `0` rather than a tolerance.

| vertex | borrows | `r_pp = r_np`? | `r_nn = r_pn`? | `r_pp = r_pn`? | `r_nn = r_np`? | verdict |
|---|---|---|---|---|---|---|
| V1 | right | ✅ | ✅ | ✗ | ✗ | **right-dependent** |
| V2 | right | ✅ | ✅ | ✗ | ✗ | **right-dependent** |
| V3 | left | ✗ | ✗ | ✅ | ✅ | **left-dependent** |
| V4 | left | ✗ | ✗ | ✅ | ✅ | **left-dependent** |

4/4, and the dependent slot is always the borrowed one. The free traces genuinely differ
(`tr_M(pp) = 0.39605`, `tr_M(nn) = 0.22575`, `tr_M(pn) = tr_M(np) = 0.29902`, all three
reproduced by disjoint-union multiplicativity `tr_M(W_l W_r) = tr_M(l)·tr_M(r)` with deviation
`0`), so the two words are different elements. **It is the response that collapses, not the
state.**

### The consequence, proved sorry-free

A functional with `f a b = g b` has `f p n = g n = f n n` *identically*, so `f p n · f n n` is
a real times itself and cannot be negative. Hence such a functional can **never** satisfy the
two-body isospin pattern bean `qou-q8vl` requires — the unlike pair on the opposite side of
zero from **both** like pairs. `no_signMixed_of_rightDependent`,
`no_signMixed_of_leftDependent`, and `no_signMixed_of_oneBody` covering either slot. The
contrapositive `signMixed_is_genuinely_two_body` states what a closure needs instead: any
functional realising the pattern depends on **both** arguments.

This is a different kind of objection from a sign objection. A sign objection says the numbers
come out the wrong way round and invites hunting for a letter that fixes them. This says the
**functional form cannot express the distinction**, whatever the letters are, for as long as
the response stays one-body.

### Where the one-body property comes from — and it is the corpus's own mechanism

The species table above cannot distinguish a mechanism from a coincidence, and the mechanism is
already stated in
[`mass-theory/canonical-trace-factorises-over-chain.md`](../../content/quantum-observable-universe/mass-theory/canonical-trace-factorises-over-chain.md):

> *"a closed braid whose word is a product of sub-words on strand sets **overlapping in one
> strand** is a connected sum, and the Markov trace — like every multiplicative link invariant —
> is multiplicative under connected sum"*

This geometry satisfies that hypothesis. `W₁` lies in `⟨σ₀,σ₁⟩` (strands 1–3); `W₂` *and a
right-borrowing bond* both lie in `⟨σ₂,σ₃,σ₄⟩` (strands 3–6). The two strand sets overlap in
**one** strand, so `tr_M(W₁·W₂G³) = tr_M(W₁)·tr_M(W₂G³)`, the left factor cancels in the ratio,
and the response depends on `W₂` alone — for **any** `W₁`, not merely for a proton or a neutron.

**Tested, and this is much stronger than the species table.**
`bond_response_junction_factorisation_probe` holds the right nucleon and the bond fixed and
varies the left word over six words on `⟨σ₀,σ₁⟩` unlike a nucleon — the **empty** word, a single
letter, an all-positive length-5 word, an inverse-heavy one, an averaged-heavy one, and the
nucleon reference. **7/7**, every response the same rational function as a symbolic identity,
`r = 0.0139840866412832240063492549091184388667922041310786488455123` in all six. A
species-only coincidence does not survive the empty word.

Lean now **derives** the premise rather than asserting it:
`response_oneBody_of_junctionFactorisation` (the shared left factor cancels, so
`f a b = (tL a · tRb b)/(tL a · tR⁰ b)` is a function of `b`) composed with the no-sign-mixed
result gives `no_signMixed_of_junctionFactorisation`.

**That same block already draws the stronger conclusion**, in its own words: *"The canonical
closure therefore carries **no many-body binding at all** — not by measurement, by theorem."*
So this step's arity finding is the **two-body isospin corollary** of something the corpus
knows, not a discovery about γγ vertices.

**Two things it is not.** (i) `QOU.MathlibExt.MarkovTraceMultiplicative` models the **disjoint
union**, and bean `qou-bsfg` exists because the two were once conflated: here the *free*
two-nucleon trace is a disjoint union (supports `{0,1}` and `{3,4}` share no strand) while the
*bonded* one is a connected sum. Different properties, asserted separately by the two probes.
(ii) That block's per-generator product formula requires **chain form** — one polynomial per
generator in Coxeter order — and says explicitly that interleaved bonds *"destroy the chain
form"*. `G³ = σ₂σ₃⁻¹σ₂σ₃⁻¹σ₂σ₃⁻¹` **is** interleaved, so the product formula does not cover it,
and the junction factorisation survives the interleaving anyway. **That refinement is the part
that is genuinely new here.**

**Epistemic split, stated precisely.** The *implication* (one-body ⇒ not sign-mixed) and the
*derivation of the premise from junction factorisation* are both proved in Lean. What is **not**
proved is junction factorisation itself: that block's own status note records *"Not formalised,
as ever, is the connected-sum multiplicativity itself."* So the chain rests on a cited standard
property, which is a better explanation than a measured table at the **same** epistemic tier —
not a promotion. **Formalising connected-sum multiplicativity is the one route to scope-(b)**,
and that block has been asking for it since it was written.

## 3. The sign: which letter carries the inverse, not which side is borrowed

| channel | vertex | inverted letter | ratio | `B` | |
|---|---|---|---|---|---|
| pp | V1 | borrowed | `1.00105775254516` | `−4.469268` keV | unbound |
| nn | V1 | borrowed | `1.00061119140688` | `−2.583012` keV | unbound |
| pn | V1 | borrowed | `1.00061119140688` | `−2.583012` keV | unbound |
| np | V1 | borrowed | `1.00105775254516` | `−4.469268` keV | unbound |
| pn | V2 | **interface** | `0.99689906291672` | `+13.129527` keV | **bound** |
| pn | V3 | **interface** | `0.98669973378340` | `+56.603918` keV | **bound** |
| pn | V4 | borrowed | `1.01317729989644` | `−55.342976` keV | unbound |
| np | V2 | **interface** | `0.99653660989228` | `+14.666837` keV | **bound** |
| np | V3 | **interface** | `0.98360747377736` | `+69.873410` keV | **bound** |
| np | V4 | borrowed | `1.01698712642581` | `−71.209668` keV | unbound |

```
sign tracks the BORROWED SIDE     : False
sign tracks WHICH GEN IS INVERTED : True
```

**Inverse on the borrowed letter (V1, V4) → unbound; inverse on the interface letter (V2, V3)
→ bound.** 4/4, both channels. The borrowed *side* sets the **magnitude** instead: right
~3–15 keV, left ~55–71 keV, an order apart.

### 🛑 How NOT to state this

It is **not** "replacing `σ₂` by `σ₂⁻¹` flips the binding". That statement is false, and it
contradicts a sorry-free theorem on `main`:
[`SingleCrossingAlwaysBinds.interface_mem_Ioo`](../../content/quantum-observable-universe/lean/QOU/QBeta/SingleCrossingAlwaysBinds.lean)
proves that for a **single-crossing** interface `μ = z + d` with `d ∈ [−h, 0]` — `d = 0` at
`σ`, `d = −h` at `σ⁻¹` — the whole family has `μ ∈ (0,1)`, i.e. **both orientations bind**. Its
own scope paragraph says so explicitly: *"no crossing-sign assignment can give an unbound
two-nucleon channel at the substrate anchor."*

Nor is `V2` obtained from `V1` by that substitution: `σ₂ → σ₂⁻¹` in `σ₂σ₃⁻¹` gives
`σ₂⁻¹σ₃⁻¹`, which is not a γγ word at all (a vertex has exactly one inverted letter). `V2` is
`V1`'s **group inverse** — reverse the order *and* invert the letters, an anti-automorphism.

That distinction matters here specifically, because
[`docs/audits/2026-05-24-isospin-categorical-source.md`](2026-05-24-isospin-categorical-source.md)
already carries a correction note for conflating two of the three relevant involutions: the bar
involution (`q ↔ q⁻¹` **and** `σᵢ ↔ σᵢ⁻¹`) and the isospin `ℤ/2` swap (`σᵢ ↔ σᵢ⁻¹` at fixed
`q`). `V2 = V1⁻¹` is a **third** map. Name which one you mean.

The rows do not contradict `interface_mem_Ioo` because a γγ word has **length 6**, and step 8
([`GammaGammaEscapesSingleCrossing.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/GammaGammaEscapesSingleCrossing.lean),
sorry-free) already proves no γγ word is a single crossing. The escape was established before
this step; only the *inside* of it is new.

## 4. Why the selection is untouched — and this part is proved, not measured

`trace_cayleyInverse`: for `M : Matrix (Fin 2) (Fin 2) R`, Cayley–Hamilton reads
`M² − (tr M)M + (det M)·1 = 0`, so at `det M = 1` the matrix `N = (tr M)·1 − M` is a right
inverse with `tr N = 2 tr M − tr M = tr M`. Step 4 proves `det V = 1` for the Hoefsmit `(2,1)`
vertex image, so **no character can see the swap**. Measured independently:
`χ_(2,1)((σ₁σ₀⁻¹)^k) = χ_(2,1)((σ₀σ₁⁻¹)^k)` for `k = 1…7`. **Steps 4/5/7's `3 ∣ k` selection
survives intact.**

### 🛑 I retracted this clause and the retraction was WRONG — the clause is restored, and stronger

For a few hours on 2026-09-19 this section carried a retraction of its own claim that
*"reading-3 feasibility is a condition on the character."* **That retraction is withdrawn. The
clause is correct.** What follows is the whole episode, because the way it went wrong is worth
more than the sentence.

**What reading 3 actually is.** Bean `qou-ales` records three readings of "the confinement SDP
on a word": **1** literal `Matrix.PosSemidef` of each Wedderburn projection; **2**
symmetric-part PSD; **3** Frobenius positivity, `χ_λ(w) ≥ 0` on every block with `y_λ > 0`
(constraint (1) of `prop:confinement-sdp` read on a word). The owner selected **3** on
2026-09-12, verbatim *"try PSD condfinement 3 for now, but keep 1 2 for later"*, and step 5
formalised it as `FrobeniusFeasible` / `FrobeniusSelected` in
`GammaGammaFrobeniusSelection.lean`. **Reading 3 is a condition on characters. Literally.** So
"feasibility is a condition on the character" is not an approximation of reading 3 — it is its
definition.

**And the argument is stronger than the clause claimed.** Reading 3 needs only character
invariance, which `trace_cayleyInverse` supplies: the `(2,1)` Hoefsmit block is
`2`-dimensional, step 4 proves `det V = 1`, so `χ_(2,1)(V⁻¹) = χ_(2,1)(V)`. That propagates to
the whole `H₆` interface for free, because
`GammaGammaH6Interface.InterfaceBranching` gives each `H₆` block character on `G^m` as
`a_λ + b_λ·χ_(2,1)(V^m) + c_λ` with `(a,b,c)` the Young-lattice path counts — **affine in the one
`(2,1)` character**. So all eleven `H₆` characters are swap-invariant, and under reading 3 the
orientation swap cannot change feasibility at `H₃` **or** at `H₆`. Reading (B) ("whole element")
moves the *letter scope*, not the reading, so it does not weaken this either.

**What the new Lean is, correctly labelled.** `det_cayleyInverse` and
`cayleyInverse_preserves_charpoly_data` — with `cayleyInverse_eq`, which identifies
`(tr M)·1 − M` with the classical adjugate `!![d,−b;−c,a]` — are sorry-free and true, and they
answer **reading 1**, which is parked. They are worth keeping for exactly that reason: the same
ruling keeps 1 and 2 "for later", and PSD *is* a matrix condition rather than a character one,
so when reading 1 is revisited this says the swap cannot change its verdict on a
`2`-dimensional block. They are **not** needed for the live reading, and the file's docstring
now says so.

Two limits on that reading-1 half, unchanged: the `(tr, det)` preservation is the part that is
a theorem — the step to equal `PosSemidef` uses the standard Hermitian spectral criterion and
is **not separately formalised**; and **nothing extends to a block of dimension `≥ 3`**, where
`(tr, det)` no longer determine the characteristic polynomial.

`mixed_trace_not_inverse_invariant`: and a *mixed* trace is not protected — a theorem, not a
measurement. `W = !![1,0;0,0]`, `M = !![2,1;1,1]`, `N = !![1,−1;−1,2]` have `M·N = 1` and
`tr N = tr M`, so no character separates them, while `tr(W·M) = 2 ≠ 1 = tr(W·N)`. That is
exactly the `H₆` situation: `tr_M(W·G³)` is mixed against the nucleon word, so nothing guards
it.

**The selection and the binding are guarded by different things, and only one of them is
guarded.** That is the cleanest thing this step produces.

There is a related invariance result worth knowing:
`content/quantum-observable-universe/.../crystal-isospin-degeneracy.md` proves `S_crystal(A)`
invariant under exponent inversion of every plain Hecke generator at the `q → 0` crystal limit,
and **explicitly flags the operator-valued interface case as open**. So this measurement is the
first evidence about what happens to that invariance at `q₀`.

## 5. The dineutron, which was the queued item

`c_P`'s numerator is order 0 at `q = 1` (`t⁰ = 3`); `c_N`'s is order 1 (`t⁰ = 0`, `t¹ = 6`). So
at V1 the dineutron/deuteron ratio deviates at **`h⁵`** against the diproton's `h⁴` — one power
weaker. All four channels are unbound at V1, the diproton most:
`B_pp = B_np = −4.469` keV, `B_nn = B_pn = −2.583` keV.

## 6. What was ALREADY in the corpus — cite, do not assert

A corpus-grep (five of six paths; path 0 `corpus_search` was **unavailable**, the
`paper-assistant` MCP server failing to connect, so it is *unrun* rather than clean) found that
two thirds of the framing I had drafted was already on the record.

**The orientation is pinned, three ways.** Not silent, as I had written:

1. **As a production convention.** `computations/isotope_record_schema.py:184-187` —
   `pp coupling: σ at gen 3k+2 (positive)`, `nn coupling: σ + (−h)·𝟙` (which *is* `σ⁻¹` by the
   Hecke quadratic), `pn coupling: σ + (−h/2)·𝟙 (averaged)`.
2. **As an acknowledged gap, since 2026-05-24.**
   [`docs/coordination/2026-05-24-low-isotope-mass-anatomy-ledger.md:31`](../coordination/2026-05-24-low-isotope-mass-anatomy-ledger.md)
   already says the rule is *"**asserted** in `isotope_record_schema.py` **without a `prop:`
   block** … Rule-14 escalation candidate"*, and
   [`option-e.md:340`](../coordination/option-e.md) calls it a *"crossing convention"*. **So
   "convention, not derivation" is the corpus's own position and is nearly four months old.**
3. **With a live conjectural derivation route.**
   `content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md` is a
   conjecture conditional on `conj:s5-so3-fiber-action` that the flavour-only `pp ↦ σ`,
   `nn ↦ σ⁻¹`, `pn ↦ σ_avg` map is the projection of a colour-tube-weighted assignment; its own
   open list asks *"Why is same-color ↦ +1, opposite-color ↦ −1?"*. Line 42: *"This over-break
   derives entirely from the σ-vs-σ⁻¹ inter-crossing sign of the flavor-only projection."*

**And the pin is separately argued to be wrong.** `InterfaceScalar.charge_independence_iff`
(sorry-free) shows `d_pp = 0` and `d_nn = −h` agree only at `h = 0`, so a charge-independent
strong force is incompatible with the σ/σ⁻¹ assignment at `q ≠ 1`; bean `qou-0pzi` (todo)
carries the same. Meanwhile `WeakIsospinT3Grading.lean` and
`inter_nucleon_linked_channel.py` treat the crossing sign as *derived* from isospin
(`I₃ = writhe/2`, pp `+1`, nn `−1`, pn `0`). **That tension is not this step's to resolve**, and
this document deliberately takes neither side.

**Sign flips under a word change are not unprecedented.** Cite, do not present as new:

- Bean `qou-pjx4` + `computations/probes/stacked_interface_writhe_normalised_probe.py` —
  **10 of 16 verdicts flip** under writhe normalisation, and *"unbinding is relocated, not
  lost"*. **Its polarity is opposite to this step's** (there positive binds, negative unbinds).
  Different objects: single-generator stacked powers *with* the normalisation, versus γγ
  vertices where step 8 proves the normalisation is identically `1`. Not a contradiction.
- [`2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md`](2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md)
  — the naive braid-topology assignment *"binds pp while unbinding the deuteron"*.
- `InterfaceScalar.stacked_crossing_gt_one` — `σ → σ²` alone flips the sign
  (`μ = 1.1044`, `B = −0.416` MeV).
- The contrast case: `qou-q8vl` / `2026-09-12-pn-betweenness-blocks-sign-mixed.md` — reflecting
  **every** bond leaves `b₃` byte-identical, because flipping both factors of a product does
  not flip it. This step's flip is asymmetric in exactly the way that one is not.

**The library holds the topology but not the physics.** `writhe` appears in 20 `sections/`
documents and 3 `ocr/` ones; `signed crossing` in one. The intersection of `writhe` with
`binding energy` / `bound state` is **zero documents**. So the crossing-sign topology is
citable from the literature; tying it to a *binding* sign is QOU-internal.

**And the mechanism for the arity is the corpus's own too** — §2's junction-factorisation
subsection, from `canonical-trace-factorises-over-chain.md`, which also already concludes that
*"the canonical closure carries no many-body binding at all — not by measurement, by theorem."*
The orientation-scoped corpus-grep did not surface that block (it is not about orientation); it
was found by reading the one block the grep did return. **A second reason a topic-scoped grep is
not a clean bill.**

**What is genuinely new** is therefore narrower than the first draft of this document claimed:

1. **the two-body isospin corollary** — that the same factorisation forbids the sign-mixed
   pattern, `no_signMixed_of_oneBody` and its junction-factorisation derivation (§2);
2. ~~**that the junction factorisation survives an INTERLEAVED bond**, which the chain product
   formula explicitly does not cover (§2);~~ **— withdrawn as a novelty claim.** A sibling arc
   measured the γγ assembly to be *exactly affine*, so `ProductionChainBondProduct`'s
   strand-window hypotheses are sufficient-not-necessary in general, which subsumes the special
   case (§6b). The observation stands; the claim to having found it first does not;
3. **the answer to the discriminator question this arc's own bean posed and left open** — it is
   which letter carries the inverse, not which side is borrowed (§3).

So after §6b the list is **two items, not three**, and item 1's forward requirement should now
be stated against `SecondArgBondNotPairFunction` rather than in `bondOf` terms.

## 6b. Independently confirmed and independently strengthened, after this step was written

Three sibling arcs reached this step's central fact from directions that do not share its
method. Recorded because two of them are *stronger* than what §2 proves, and one of them
removes a hedge §2 was careful to keep.

**The one-body pattern, reproduced numerically at 60 dps** (`qou-ix0x`, PR #7287, merged
`db8d3cefd9`). Measuring the bond factor `μ(G³)` on all four *ordered* pairs gives
`μ_pp = μ_np = 1.00105775254515984` and `μ_pn = μ_nn = 1.00061119140688078`, agreeing to
`1.6e-61` within each pair and differing by `4.47e-4` across them. Two things to note. That is
the same `pp = np`, `nn = pn` collapse this step measures at V1 (§3), from a probe that shares
no code with ours — and `μ_pn` reproduces this step's junction-factorisation value
`1.00061119140688077961…` digit for digit. So the arity fact does not depend on our probe.

**What we can give that arc back is the MECHANISM.** Its own record says the one-sidedness is
*"measured, not proved"*, and considers and rejects far-commutation as the explanation (`σ₃` sits
inside block 1, but `G³` also carries `σ₂`, adjacent to block 0's `σ₁`). §2 above answers it:
the cause is **connected-sum multiplicativity of the Markov trace**, which is why the empty left
word gives the identical response — a fact no species-level measurement can produce.

**A strictly stronger structural statement now exists, and it is not ours**
(`QOU/MassTheory/SecondArgBondNotPairFunction.lean`, 7 declarations, sorry-free, on `main`).
`ChainBondOrderDependence.bondOf` is **symmetric in its two nucleon arguments by construction**,
so a bond reading only one endpoint is not of the `bondOf` form *at all* unless it is constant
(`secondOnly_eq_bondOf_iff`, `not_exists_bondOf_of_ne`). That sharpens what
`signMixed_is_genuinely_two_body` hands forward: such a bond does not *violate* the chain
calculus's conclusions, it falls **outside its domain**. Anyone reading this step's requirement
should state it in terms other than `bondOf`.

**And §2's interleaving hedge can be dropped.** §2 notes that the chain-form per-generator
product formula does not cover an interleaved bond, and treats the factorisation surviving
anyway as a finding. The same arc measured the γγ assembly to be **exactly affine** —
`δ := μ_both − μ₀·μ₁ = 0` to the 60-dps floor — so `ProductionChainBondProduct`'s strand-window
hypotheses are **sufficient but not necessary**. That is the general form of our observation:
not "the factorisation happens to survive interleaving here", but "those hypotheses were never
the reason it holds".

**One apparent collision, resolved elsewhere and not by us.** A third arc (`qou-99qc`, PR #7295)
proves the alternating character is **order-blind** — a 1-dim rep sends a word to a product of
scalars, so it sees only the multiset of letter shifts (`wordChar_of_perm`, sorry-free) — which
reads against the order-*dependence* above. Per-block measurement settles it: both 1-dim blocks
of `H₆` sit at the arithmetic floor (`|y·Δχ| = 9.0e-62`) while the `≥ 2`-dimensional blocks carry
the whole `1.729e-3`. Both stand and they constrain different channels. Noted here so a later
reader does not stop on the pair.

## 7. Scope — (a), and deliberately nothing stronger

Under the repo's refuted/ruled-out discipline this is a **scope-(a)** negative: *this
construction, at these four placements, against these words, does not give the pattern.* Two
reasons it may not be promoted to (b):

1. A **conjectural derivation route for the orientation exists** (§6.3). Writing "the sign is a
   convention and cannot be derived" would be a (b) claim with no proved invariant behind it,
   against a live open conjecture that would supply one.
2. The arity premise is four words at one pin in `H₆` (§2) — though §6b's independent
   reproduction of the same collapse, from a probe sharing no code, weakens this particular
   reservation without removing it.

**The 2026-09-13 ruling does not change this scope, and it is worth saying why.** Reading (B)
moves the confinement SDP's *letter scope* to the whole word; it does **not** change the
reading, which stays **3** (Frobenius positivity, `χ_λ(w) ≥ 0`) per the owner's 2026-09-12
selection. It bears on the **selection** half of the arc (§4) and not on the **arity** half at
all: step 11's Lean contains no PSD hypothesis and no `Matrix.PosSemidef` anywhere, so the
arity obstruction is untouched under any of the three readings. The ruling's other half
is a caution to carry forward rather than a change here — the γγ *construction* provably
reaches only 6 of the 11 letters (γγ words have even length; 11 is odd), while the *SDP* now
reaches all eleven, so the 6-of-11 fact must not be read as an all-clear for the other five.

The one **(b)** statement available is the *negative* direction, and it is not new: orientation
cannot flip the sign for a **single-crossing** interface, invariant = `interface_mem_Ioo`. This
step's contribution there is only that the exclusion is *vacuous on γγ words* — which is step
8's theorem.

3. And the arity premise rests on **connected-sum multiplicativity**, whose formalisation
   status changed under us — see §7b. It is *conditionally* formalised on an open sibling PR,
   which keeps this scope-(a) but sharpens the follow-up considerably.

## 7b. The route to scope-(b) is no longer "formalise it from scratch" — and this step constrains where that arc hands off

§2 says the arity premise rests on connected-sum multiplicativity of the Markov trace, and
§7 used to add *"which is not formalised — that block's own note says ‘Not formalised, as
ever’."* **That is now out of date, and the correction cuts both ways.** Verified at source on
`origin/claude/trusting-planck-wncjcc` rather than from its PR text.

**What exists (PR #7418, `qou-2ss0`, OPEN — not on `main`).**
`QOU/MathlibExt/SingleCrossingChainFactorizes.lean`, 23 declarations, sorry-free, proves the
chain trace factorises and the three-body cumulant vanishes identically, from

```
DisjointBlockMultiplicative T :  ∀ n, ∀ a ∈ H n, ∀ b ∈ shifted n,  tr (a * b) = tr a * tr b
```

— which **is** the disjoint-block form of the multiplicativity §2 invokes. Its
`singleCrossingJoin_of_disjointBlock` derives the one-crossing join from that law in three
tactic lines, and it records that the *same* level-indexing error had been made twice before on
this object. That is the structural shape of this step's junction factorisation, one level of
abstraction up.

**Why scope-(a) nevertheless stands, unchanged.** Three reasons, and the file states all three
about itself:

1. `TowerSpan`, the hypothesis it runs on, is **unproved, has no Hecke instance, and is not
   provable from `MarkovTrace`** — the structure places no constraint on how `H (m+1)` is
   generated. Its own docstring cites AGENTS.md §"Axiomatization is NOT a Proof" and says the
   bond product is *"still not unconditionally derived"*. This is the
   conditional-proved-≠-premise-established rule, and it binds here.
2. **It is on an open PR, not in the product.** A result on a branch is not a corpus fact; that
   is the `qou-3v8h` lesson, and citing it as though it had landed is exactly the move this
   audit's §9 is a record of.
3. Its satisfiability witness is **degenerate by its own admission** — the only model is `R`
   with `⊥ = ⊤`, since Mathlib has no Hecke tower, so nothing yet connects the abstract
   `MarkovTrace` structure to the Hecke Markov trace on braid closures. **That instantiation is
   not established by anything read here**, and it is the step my §2 mechanism would actually
   need.

**What this changes for the follow-up, which is the useful part.** The decision this step hands
the owner was *"formalise connected-sum multiplicativity — session-scale, not started."* That
framing is superseded. The gap is now **`TowerSpan` plus instantiating the abstract tower at the
Hecke tower** — the sibling's own words for the first half are *"one classical, citable
structure theorem rather than two independent unknowns."* Sharper target, and a different
question from the one I asked.

**And step 11 constrains that arc's hand-off, which is why this is two-way.** #7418 ends by
handing off: route (b) *"needs a word whose interfaces are **adjacent and non-commuting**. Which
word is selected is the γγ / confinement-SDP question (`qou-ales`, `qou-99qc`)."* That is this
bean. §1 and §2 answer part of it: the `H₆` interface is the **single** generator `2`, every
γγ vertex occupies **two adjacent** generators and so must borrow one from a nucleon, and the
resulting response is one-body at **every** placement. So an adjacent-and-non-commuting
interface pair cannot be obtained by re-placing a γγ vertex on this interface — the obstruction
is the arity of the functional, not the geometry of the choice. Whatever word that arc needs, it
is not in the four-placement family.

**Independent agreement on a third point.** #7418's C9 reports that *"the corpus's bond-product
grounding cites a theorem whose hypothesis the production word fails."* §6b reaches the same
finding from the other side — `ProductionChainBondProduct`'s strand-window hypotheses are
sufficient-not-necessary. Two arcs, two methods, same conclusion about the same citation.

**Nothing here retracts step 10.** Its closed form, `Θ(h⁴)` bracket and `α/100` ceiling are
correct statements about the word they are about. What narrows is the interpretation of `r` as a
*pair* quantity.

## 8. By-product — a fourth confirmation of `qou-sikd`

`tr_M,H₃(p) = (q⁴+1)P_P/(4q⁹(q²+1)²) = 0.6293284022029219181653` and
`tr_M,H₃(n) = (q⁴+1)P_N/(4q⁹) = 0.4751335171556822125061`, both matching
`tr_M_canonical` on the 11-letter elements with deviation `0` — and neither of them the
`1.145759692` / `0.987743688` literals `assembly_chain_11_letter_recompute_probe` still compares
against. Fourth independent path to the same conclusion. Not fixed here: the drain across ≥ 8
committed witnesses is owner-gated.

## 9. Four reasoning errors of mine, recorded because the shape recurs

1. **"The mechanism is unknown, so the premise is measured."** Wrong twice: the mechanism is
   stated in a corpus block (§2) and it is *derivable*, and a species table could never have
   settled it. Caught by following a citation rather than by a grep — the orientation-scoped
   grep could not have found it.
2. **"`r_pn ≠ r_np` rules out right-dependence."** It rules out nothing. If `r(a,b) = g(b)`
   then `r_pn = g(n)` and `r_np = g(p)`, which *should* differ. Only the **like-pair**
   comparisons discriminate, and the first version of the probe did not compute them off
   V2/V3/V4 — so it could not have decided the arity it was built to decide. Fixed by extending
   to the full 4 × 4 grid.
3. **"The orientation choice is underived, i.e. unaddressed."** Right about derivation, wrong
   about silence — §6 above. The corpus had said "asserted, not derived" in a coordination
   ledger since 2026-05-24, and the corpus-grep is what found it. Had I written the record
   first, it would have re-declared a four-month-old known gap as a new finding.

4. **Retracting "reading-3 feasibility is a condition on the character" — the retraction was
   the error, not the claim.** §4 above. I read a sibling's coordination comment relaying the
   2026-09-13 ruling, which described the criterion as `Matrix.PosSemidef` on every Wedderburn
   projection, and retracted a correct clause against it. That description is **reading 1**;
   reading 1 is parked; the live criterion is **reading 3**, which is `χ_λ(w) ≥ 0` — a
   character condition, so the clause was right all along.

   **This is the corpus-grep discipline failing on a claim ABOUT A RULING rather than about a
   number.** The answer was one grep away and decisive: bean `qou-ales` carries the owner
   verbatim (*"try PSD condfinement 3 for now, but keep 1 2 for later"*) with reading 3 spelled
   out, and it names reading 1 as provably selecting nothing non-trivial for `k ≤ 5` on the
   interval. I ran no grep, because a ruling relayed by a sibling reads like primary source. It
   is not — AGENTS.md's own note on the same ruling records the identical mistake being made
   and corrected by that sibling (bean `qou-99qc`), i.e. the wrong reading had already
   propagated once before reaching me.

   **The generalisation, which is the reusable part:** *"the corpus is the source of truth"*
   applies to a claim about what a ruling REQUIRES, not only to a status or a figure — and a
   sibling's PR comment is exactly as secondary as a source file's `## Status` note. The three
   readings differ in what kind of object they constrain (a matrix, its symmetric part, its
   character), so getting the reading wrong does not shift a threshold, it changes which
   theorem is even relevant. Cost here: a true claim retracted, three Lean declarations
   written against a parked question, and the wrong framing pushed to five artifacts before a
   re-read caught it.

Also removed before commit: a `selection_blind_to_orientation` I had written whose proof was
`right; trivial`, concluding `… ∨ True`. It asserted nothing — the §1a audit-dodging shape,
caught by re-reading my own diff.
