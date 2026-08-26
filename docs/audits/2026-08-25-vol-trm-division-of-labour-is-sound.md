# The `Vol` / `tr_M` division of labour is sound; the bridge between them is not

**2026-08-25 · bean `qou-qpj9` · scope (a) · no new computation — a reading of
existing code, following up
[the Ito/Dehornoy audit](2026-08-25-ito-dehornoy-hyperbolicity-criterion.md)
Addendum 4.**

## The worry, and why it does not materialise

Addendum 4 established that the atom object is **not a link**: what
`atom_braid_word_3A` returns is an element of `H_n(q)` outside `im(ρ)`, because
`2A+1` of its letters are genuine weight-1 averages over crossing sign. The
obvious follow-on worry is that the mass law reads `Vol(K)`, and if the atom has
no link then something must be reading a volume off an object that has none.

**Nothing is.** Traced through the live consumers:

| quantity | comes from | is it a link? |
|---|---|---|
| `Vol(K)` | the **atlas knot** — `𝓑₃`, `6₂`, `8₁₁`, `L6a4` | **yes**, genuine links |
| `tr_M(K)` / `ρ(K)` | the **atom `H_n(q)` element** | **no — and it needs none** |

The Markov trace is a linear functional on all of `H_n(q)`, so it is defined on
the atom element without any closure. The volume is only ever taken of an atlas
knot. `per_knot_density_per_block_wiring.py` states the per-block form over
*"partitions of the **knot's own** strand count"* and works it for `𝓑₃`; the
production scalar is `[Vol(𝓑₃)/ℏ_q²]·linking_weight(q)`, a constant of the
**Borromean link**, not of any atom word.

The one producer that *does* push the atom word through SnapPy —
[`vol_t_he3_snappy_probe.py`](../../computations/deltalambda/vol_t_he3_snappy_probe.py)
— is exploratory, says so, comments the averaged letters as *"Hecke element
`σ−h/2·1`, not a topological crossing"*, and returns a refutation.

**So the division of labour is already correct throughout.** Recorded as a
negative because it was my own worry and it failed — the second one this arc.

## What is actually missing

The two halves are each sound; **what is unestablished is that they are about the
same object.** The atlas knot stands in for the atom, and the right to make that
substitution is exactly what the previous two addenda found unsupported:

- **The general principle offered was *"Same Markov class"*** — corrected in
  Addendum 6, because a non-braid has no Markov class to share.
- **For `D` / `T` / `³He` the actual selection is a fit** — the knot chosen for
  volume proximity to `B_AME`
  ([sibling audit](2026-08-25-knot-id-is-an-admitted-fit.md)).
- **For `p` / `n` it is sound** — the volume comes from the particle registry's
  canonical `T_w` σ-braid word (Addendum 7), a genuine braid.

That is the gap, stated precisely: **not a dataflow defect, a warrant defect.**
`tr_M` legitimately reads the atom element; `Vol` legitimately reads a link; and
for three of six atlas entries there is no principled reason those two readings
concern the same physical object.

## What this does and does not imply

**Does not** imply any volume or binding number is wrong. Nothing here recomputes
anything.

Worth noting for calibration rather than as a further claim: the surviving
consumers of `per-atom-hyperbolic-volume.witness.json` are absolute-mass tables
(`mass_table_comprehensive.py`, `per_knot_mass_table_demonstration.py`), and
[`canonical_mass.py`](../../computations/canonical_mass.py) already deprecates
exactly these `Vol`-based forms for absolute mass — *"`m_e · Vol(𝓑₃) · tr_M / ℏ_q²`
→ 406 (−57 %)"*. Under the 2026-08-11 excision ruling absolute mass is a
rendering rather than a prediction, so the warrant gap above sits under a claim
the framework has already stepped back from. It still wants closing, because the
same substitution is what a *binding-ratio* reading would rely on, and binding
ratios are not excised.

## Cross-references

- Addendum 4, 6, 7 — [Ito/Dehornoy audit](2026-08-25-ito-dehornoy-hyperbolicity-criterion.md)
- The admitted fit — [sibling audit](2026-08-25-knot-id-is-an-admitted-fit.md)
- Atlas provenance, unenforced — bean `qou-4b6g`

---

## Addendum — the charitable reading, measured (2026-08-25)

Calling *"Same Markov class"* a category error is an **argument**, and it invites
a charitable reply: *granted the phrasing is loose, but surely the two objects
agree on the invariant that matters.* The Markov trace **is** that invariant — it
is what `ρ(K)` in the mass law actually is, it is defined on **both** objects (on
the atom element by linearity, on the knot braid as a braid), and it is a Markov
invariant, so genuinely Markov-equivalent objects **must** agree on it.

So the charitable reading is testable.
[`atom_vs_atlas_markov_trace_probe.py`](../../computations/meson/atom_vs_atlas_markov_trace_probe.py),
2 assertions, symbolic in `q`:

$$\mathrm{tr}_M(\mathcal{B}_3) \;=\; -\,\frac{q^{12}-3q^{10}+2q^{8}-4q^{6}+2q^{4}-3q^{2}+1}{q^{4}\,(q^{2}+1)^{2}}$$

| pair | difference |
|---|---|
| proton element − Borromean braid | **≠ 0** |
| neutron element − Borromean braid | **≠ 0** |
| proton element − neutron element | **≠ 0** |

**They do not agree.** The charitable reading fails, exactly — which turns
Addendum 6 from an argument into a measurement.

**Three guards make the negative trustworthy.** *Same algebra*: `A = 1` gives
`3A = 3` strands and `(σ₁σ₂⁻¹)³` is a 3-braid, both in `H₃`, so no stabilisation
or normalisation mismatch. *Same convention*: both sides go through
`markov_peel` / `markov_trace_canonical`, and the guard tests the **answer**
rather than the source, per AGENTS.md — the `(q²+1)²` denominator is the
convention-D peel signature, and there are no half-integer powers of `q`, which
is what convention C would leave. (Deliberately **not** via
`from_scratch/wenzl_y_axiomatic.py`, whose `z = 1/(q^{1/2}+q^{-1/2})` is
convention C; that comparison would have measured the convention, not the
objects.) *Symbolic*: no anchor, no dps, no float, so "agrees to N digits"
cannot arise.

### The third row is a sanity check, not a defect

`p` and `n` share an atlas entry — both the Borromean link — so `Vol` is shared
and the p–n difference must come from `ρ`. It does, and it factors:

$$\mathrm{tr}_M(\mathfrak{p}) - \mathrm{tr}_M(\mathfrak{n}) \;=\; \frac{(q-1)(q+1)(q^{4}+1)(q^{4}+2q^{2}+2)}{4q\,(q^{2}+1)^{2}}$$

**Vanishing at `q = 1`** — the splitting switches off in the classical limit,
which is what it should do. So sharing a knot is deliberate and correct.

### What it settles, and what it does not

Settled: the atlas knot is **not** a Markov-equivalent stand-in for the atom
element, in the one sense that could have rescued the sentence. The warrant gap
above is real, not a phrasing quibble.

Not settled, and not claimed: that the framework is wrong. This **confirms** the
division of labour is a genuine split rather than a redundancy — the two objects
really are different, and really are used for different factors. Scope **(a)**:
two specific objects, `H₃`, convention D.

---

## Addendum 2 — which object production's `ρ(proton)` actually is (2026-08-26)

The check-in prompt I wrote for this arc said *"p/n is sound"*. **That was
understated, and this corrects it.**

Addendum 7 of the Ito audit established that `p`/`n`'s *volume* provenance is
sound — it comes from the particle registry's canonical `T_w` σ-braid word, a
genuine braid. **That stands.** What was never checked is what that volume is
*paired with*.

`mass_per_knot_density.py` pairs them explicitly:

```python
vol = vol_borromean()                                    # 8·Catalan, the LINK
tr_M_proton = _load_tr_M_proton_at_q0()                  # ← which object?
vd_pb = per_knot_density_vd(vol, q, density=density_per_block(tr_M_proton))
```

Settled by value rather than by reading. Evaluating both symbolic traces at the
proton-pinned `q₀` against what production loads from
`chi-proton-h3-at-q0-50dps.witness.json`:

| object | `tr_M` at `q₀` | Δ vs the cached production value |
|---|---|---|
| **atom `H₃` element** `(Z=1,N=0)` | `1.1457596924573008697` | **2.7 × 10⁻⁴⁰** |
| Borromean braid `(σ₁σ₂⁻¹)³` | `0.99856216383678726595` | `0.147` |

**Production's `ρ(proton)` is the atom element's trace, exactly.** So the live
pairing is

$$\underbrace{\mathrm{Vol}(\mathcal{B}_3)}_{\text{the LINK}} \;\times\; \underbrace{\mathrm{tr}_M(\text{atom element})}_{\text{a DIFFERENT object}}$$

and the addendum above proves symbolically that those two objects **do not share
a Markov trace**.

### What this changes

**The warrant gap covers `p`/`n` as well — and differently.** For `D`/`T`/`³He`
the defect is a fit (knot chosen for volume proximity to `B_AME`). For `p`/`n`
there is no fit; there is a **pairing** of a geometric factor taken from one
object with an algebraic factor taken from another, and nothing on record saying
that is intended or why. So it is 6 of 6, not 3 of 6, with two distinct causes.

**The size is not marginal.** Anyone reading *"Same Markov class"* at its
charitable face value would expect these two traces to agree. They differ by
**≈ 15 %** in the very quantity the mass law calls `ρ`.

### What it does not show

**Not that the number is wrong, and not that the pairing is wrong.** Taking the
geometric factor from the knot and the algebraic factor from the quark-structured
element is a perfectly coherent design — arguably the intended one, since the
per-block form is explicitly *"the Markov trace over the partitions of the knot's
own strand count"* and `H₃` is where both live. What is missing is the statement
that this is deliberate, and the reason.

The one justification on record was *"Same Markov class, different topological
realization"* — which is a category error, and which, read charitably as trace
equality, is now measured false. Scope **(a)**: one production path, `H₃`,
convention D, proton pin.

---

## Addendum 3 — the corpus answers most of it; I over-claimed again (2026-08-26)

Addendum 2 called the `p`/`n` pairing *"unexplained"* and said nothing was on
record saying it is intended. **The corpus-grep I should have run first says
otherwise.**

[`prop:hoefsmit-scattering-pipeline`](../../content/quantum-observable-universe/mass-theory/hoefsmit-scattering-pipeline.md)
Stage 3 states the architecture directly:

> *"The factor `Geom(K)` **projects the algebraic trace into a measurable
> observable**: `Vol(K)/ℏ_q²` for hyperbolic `K` (mass/energy), `CS(K)·ℏ_q²` for
> torus `K`, or `0` for the unknot."*

and, in the proof:

> *"On the algebraic side this is the algebraic-quantum-volume pairing in
> `ℤ[q^{±1/2}]`; **the geometric reading appears only after applying
> `τ_arch`**."*

**Pairing an algebraic factor with a geometric one is the design**, and the two
sit on opposite sides of the fibre functor by construction — that is what the
observation frame *is*. So "an algebraic factor from one object and a geometric
factor from another" is not an anomaly to be explained; it is the Tannakian
structure working as specified. **Addendum 2's framing is withdrawn.**

### What survives, narrowed to one question

The block's formula carries **one** `K` throughout —
`𝔪(K) = m_e · Geom(K) · ‖J_K(q)‖`, the trace *of* `K` against the volume *of*
`K`. Production evaluates `Vol` of the Borromean link against a trace that is
**not** `J_{𝓑₃}(q)`: measured, `tr_M(β_Bor) = 0.9986` while production's
`ρ(proton) = 1.1458`.

Two readings, and **the corpus does not settle between them**:

- **(A)** the formula means one `K`, and the atom element is that `K`'s algebraic
  side under a description the block does not spell out;
- **(B)** the algebraic side carries the full quark-structured element while
  `Geom` carries the geometry of its *carrier link* — two objects by design.

(A) is what the formula literally says; (B) is what the `τ_arch` prose suggests.
This is a **design-intent** question, and per this arc's own discipline it goes
to the author rather than being guessed at.

### Tally, because it is the point

Five worries on this arc: the word-level "load-bearing" claim (**retracted**),
"does anything read `Vol` off the atom object" (**no**), "is `p`/`n`'s
`principled-derivation` a fit" (**no**), "is the pairing unexplained"
(**no — documented**), and the conjugacy-floor exclusion (**held, and upgraded to
a proof**). One in five. The corpus-grep checklist earned its place four times
here; the one time I skipped a tier of it — `INDEX.md` only — it cost the Malyutin
bound that was quoted in a paper already on disk.

---

## Addendum 4 — reading (A) refuted in Lean; (B) stands by elimination (2026-08-26)

Addendum 3 left two readings and said the corpus does not settle between them.
**(B) is a statement of design intent and is not a proposition — nothing can
prove it. (A) is a mathematical claim, and it is now refuted**, which settles the
pair by elimination.

[`QOU/MassTheory/TraceReadingsDiffer.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/TraceReadingsDiffer.lean)
— `lean`-direct **exit 0**, six declarations, **no `sorryAx`** on any
(`propext`, `Classical.choice`, `Quot.sound` only; `not_rel_of_invariant_ne`
depends on **no axioms at all**).

### The separation is cleanest at the classical limit

Both denominators are nonzero at `q = 1`, and there:

$$\mathrm{tr}_M(\mathcal{B}_3)\big|_{q=1} = 1, \qquad \mathrm{tr}_M(\text{proton atom})\big|_{q=1} = \tfrac{1}{2}$$

A clean factor of two, in exact small rationals — so the refutation needs no
`q₀`, no dps, and no float. Stated over an arbitrary characteristic-zero field,
so the separation is not an artefact of ℚ.

| declaration | content |
|---|---|
| `trMBorromean_one` | `= 1` at the classical limit |
| `trMProtonAtom_one` | `= 1/2` at the classical limit |
| `trM_readings_differ_at_one` | the two differ **at `q = 1`** |
| `trM_readings_differ` | hence differ **as functions** |
| `not_rel_of_invariant_ne` | an invariant separates — general, axiom-free |
| `readings_not_related_of_invariance` | given trace-invariance as an explicit hypothesis, the two are not related |

### Why this refutes (A), and what it does not do

Under **(A)** the atom element and `β_Bor` name the same `K`, hence are Markov
equivalent, hence share **every** Markov invariant — including `tr_M`. They do
not. So (A) is false.

**Three things this deliberately does not claim.** The coefficients are **not**
re-derived from the Hecke algebra inside Lean; they come from the corpus's own
producers via
[`atom_vs_atlas_markov_trace_probe.py`](../../computations/meson/atom_vs_atlas_markov_trace_probe.py),
and what Lean adds is an **independent kernel-checked evaluation** of the
separating inequality — a cross-check on that sympy run, not a replacement.
That `tr_M` **is** a Markov invariant is standard (Jones) and is carried as an
**explicit hypothesis** in `readings_not_related_of_invariance`, never asserted
as proved — the §3b-cond pattern, with the class content being the invariance
itself and the theorem *deriving* the conclusion by contraposition rather than
projecting it.

And **(B) is not thereby proved.** Elimination gives that (B) is the only
surviving reading of the pipeline; (B)'s actual content is that the pairing is
*intended*, which no theorem supplies. That still wants one sentence from the
author in the block.

### Correction to my own note above — the guidance was right, I did not read it

An earlier version of this section claimed AGENTS.md's `lean`-direct recipe
"needs one correction for toolchain v4.24.0". **That was false and is
withdrawn.** AGENTS.md gives no path of its own; it routes to
[`local/lean-environment-setup` §"VERIFY a single file with lean-direct"](../../.claude/skills/local/lean-environment-setup.md),
which already carries exactly the working form:

```sh
LP=$(find "$ROOT/.lake/packages" -maxdepth 5 -type d -path '*/.lake/build/lib/lean' | tr '\n' ':')
```

`build/lib/lean` — the very segment I lost two attempts to. The skill even adds
the workspace and paper olean dirs, which my improvised version omitted.

What actually happened is that I invented a `find` pattern instead of opening the
document AGENTS.md points at, **against a STRICT rule that says to do exactly
that**: *"On **any** Lean env/tool failure … FIRST `grep -ri "<error keyword>"
.claude/skills/ AGENTS.md docs/`."* A grep for `LEAN_PATH` would have landed on
the right line in one call.

**This is the second instance of one failure in this arc**, and the pair is worth
more than either. The Malyutin bound was quoted in a paper already on disk and I
missed it by running only tier 1 of corpus-grep path 5 (`INDEX.md`, one line per
document, structurally unable to see a result cited *inside* a held paper). Here
the recipe was in the skill and I missed it by not running the lookup at all.
Same shape: **the answer was on disk, the checklist names where, and I
improvised.** Both times the improvisation looked like progress and cost more
than the lookup would have.

Nothing about the Lean result changes — `lean`-direct exit 0, no `sorryAx`.
Only the attribution of my own path error was wrong.
---

## Addendum 5 — (B) has no motivation, and the corpus says so in three places (2026-08-26)

Asked for the motivation behind reading (B) before declaring it. **There is none,
and (B) should not be declared.** My earlier elimination argument was wrong
because the alternatives were framed too narrowly: there is a third reading I did
not consider, and the corpus supports it in three independent places.

### 1 · The canonical formula is ONE `K` — explicitly

[`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
§5, quoted verbatim in the
[Vol-usage audit](2026-06-02-vol-usage-audit-uniform-vs-per-knot.md):

```
m(K) = m_e · VolDensity(K, q_0)
VolDensity(K, q) = Vol(K) / ℏ_q² · linking_weight(K, q)
```

One `K`, in both factors. The cheat-sheet chain is likewise single-object:
`braid β → tr_M → J_K(q) → ω → Geom(K) → × m_e → 𝔪`, with `J_K = tr_M(𝓑_K)` —
the trace **of `K`'s own braid**.

### 2 · The corpus already calls the mismatch a bug

The same audit's TL;DR: *"Production compute is overwhelmingly
uniform-`Vol(𝓑₃)`… **Net: 64 atom-touching scripts use ONLY uniform `Vol(𝓑₃)` —
the bug.**"* 87 scripts uniform against 2 per-knot, with a per-isotope error
budget (`m_p +2.89 %`, `⁴He +3.65 %`, `⁵⁶Fe +3.86 %`). Triggered by owner
pushback: *"thought we determined this knot-dependent and should not be
uniform."*

So a `Vol` that does not belong to the object being traced is **already
classified as a defect**, not a design.

### 3 · The literature is the volume conjecture — and it is one-`K` too

The library holds at least eight sources
([`arxiv-1002.0126v1`](../../library/arxiv-1002.0126v1/) *An introduction to the
volume conjecture*, [`arxiv-1203.2182v1`](../../library/arxiv-1203.2182v1/)
*Volume Conjecture: Refined and Categorified*,
[`arxiv-1003.4808v2`](../../library/arxiv-1003.4808v2/) *QFT and the Volume
Conjecture*, and more), and the corpus carries
[`conj:kashaev-volume-conjecture`](../../content/quantum-observable-universe/mass-theory/kashaev-volume-conjecture.md)
plus `QOU.Kashaev.VolumeConjecture` in Lean.

This **is** the literature for relating an algebraic invariant to a geometric
volume. But note what it says, in the cheat sheet's own words:

> *"Volume is **NOT** the carrier — it is the **exponential** of it.
> `tr_M ~ exp(Vol)`."*

The volume conjecture relates `J_K` and `Vol(K)` **for one and the same `K`**, as
a *correspondence* — asymptotically the trace **is** the exponentiated volume. It
gives no licence to take `Vol` from one object and `tr` from another; if
anything, for a single `K` the two carry the *same* content in two forms.

### The third reading, which is the one the evidence supports

- **(C)** The framework intends **one `K` per atom**, that `K` being the atom's
  own braid word — the cheat sheet says so explicitly: *"each atom's canonical
  `K` (proton `𝓑₃`, **deuteron `β_D` via `atom_braid_word_3A(1,1)`**, etc.)"*.
  But that object **is not a link** (PR #5765: outside `im(ρ)`, `2A+1` averaged
  letters — measured), so it **has no hyperbolic volume**, and production
  substitutes the Borromean one. The pairing is the *symptom* of an
  unsatisfiable specification, not a design.

Note the inconsistency (C) exposes, visible in that one cheat-sheet parenthesis:
the **proton**'s `K` is named as a genuine link (`𝓑₃`) while the **deuteron**'s is
named as a Hecke element (`atom_braid_word_3A(1,1)`). Those are different kinds
of object, and only one of them has a volume.

### Consequence

**Do not add a sentence declaring (B).** It would put a rationalisation into the
paper for something the corpus classifies as a defect in one place, contradicts
in another, and has no literature support for. The honest statement is (C): the
one-`K` formula is currently **unsatisfiable at the atom level**, because the
object the chain traces is not the kind of object that has a volume.

That is a real open problem and it sits upstream of Obstruction A — bean
`qou-7p7d`. My elimination in Addendum 4 stands as far as it goes (**(A) is
refuted in Lean**), but "therefore (B)" does not follow: (C) was always available
and is better supported.

---

## Addendum 6 — the pruning invariant: the atom trace is a convex combination (2026-08-26)

Working `qou-7p7d` formalize-first: find the invariant that prunes *before*
running a search.

`tr_M` is **linear** on `H_n(q)`, and each letter `c·σ_g + d·1` expands over
`{σ_g, σ_g⁻¹}` via `σ⁻¹ = σ − h`. So the atom element — which has no closure —
is nonetheless a weighted sum of genuine braid images:

$$\mathrm{atom} = \sum_b w_b\,\rho(\beta_b), \qquad \mathrm{tr}_M(\mathrm{atom}) = \sum_b w_b\, J_{K_b}(q)$$

**Measured** ([`atom_branch_convexity_bound_probe.py`](../../computations/meson/atom_branch_convexity_bound_probe.py),
3 assertions): the weights are a **convex combination** — every `w_b > 0`,
`Σ_b w_b = 1` **exactly** — at `A = 1, 2, 4`.

| isotope | `A` | letters | averaged | `2A+1` | branches | `Σ|w|` | convex |
|---|---:|---:|---:|---:|---:|---:|---|
| proton | 1 | 11 | **2** | 3 | 4 | `1.0` | ✓ |
| neutron | 1 | 11 | **2** | 3 | 4 | `1.0` | ✓ |
| deuteron | 2 | 23 | 5 | 5 | **32** | `1.0` | ✓ |
| ⁴He | 4 | 47 | 9 | 9 | 512 | `1.0` | ✓ |

**Proved** ([`AtomBranchConvexityBound.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/AtomBranchConvexityBound.lean),
`lean`-direct exit 0, three declarations, **no `sorryAx`**): a convex combination
cannot exceed its largest term, so `|tr_M(atom)| ≤ max_b |J_{K_b}(q)|` — and the
bound is **sharp**, attained by a one-branch expansion.

**Why it matters.** It collapses `2^(2A+1)` independent hyperbolicity questions
into one: *is any single branch large?* That is the prune, and it is why no wide
search was run.

### The step I did not take, and why

I was about to push the bound through `tr_M ~ exp(Vol)` — the cheat sheet's own
shorthand — to get `Vol_eff(atom) ≤ max_b Vol(K_b)`. **Not licensed.** The volume
conjecture is an asymptotic in the **colour** `N` at a root of unity,
`lim (2π/N)·log|J_N(K; e^{2πi/N})| = Vol(K)`, not a pointwise bound on the
ordinary Jones value at fixed `q`.

The corpus's own numbers refute the misuse: every `²H` branch closure was
measured non-hyperbolic, so a pointwise `|J| ≤ exp(Vol) = 1` would force
`|tr_M(atom)| ≤ 1` — against the production proton value **1.1458**. The
shorthand in the cheat sheet invites exactly this error; it is worth reading as
the asymptotic statement it is.

### Two corrections that fell out

**1 · `2A+1` fails at `A = 1`.** `atom_braid_word_3A`'s docstring says *"there are
`2A+1` such non-braid letters (two per nucleon… plus one per interface)"*.
Measured: `A=2 → 5` ✓, `A=4 → 9` ✓, but **`A=1 → 2`, not 3** — a single nucleon
has no interface, so the `+1` has nothing to count. My own
`atom_word_braid_letter_census_probe.py` asserts the identity **only over
`A ≥ 2`**, so its assertion is true as tested while its framing implies a
generality it never checked.

**2 · The sibling's stated reason does not reproduce.** The
[atom-word audit](2026-08-25-atom-word-closures-are-not-hyperbolic.md) argues
*"each branch braid is monotone, so its closure is a connected sum of `(2,k)`
torus links"*. Tested under both readings — all letters sharing a sign, and
Stallings-homogeneous (each generator consistently signed) — **the branches are
neither**, at `A = 1` or `A = 2`. Their **measurement** (32/32 non-hyperbolic via
SnapPy) is untouched; only the stated reason fails to reproduce, and possibly
"monotone" carries a third sense I have not found.

### Scope

SnapPy is **unavailable** in this container, so **no volume is computed here** —
the `²H` branch result is the sibling's, cited. For `A = 1` branch hyperbolicity
nothing is established. The convexity bound and its Lean consequence are about
**traces**, and stand on their own.

---

## Addendum 7 — the one question, answered: no branch is hyperbolic (2026-08-26)

SnapPy installed (3.3.2), so the question the convexity bound reduced everything
to is now measured rather than deferred.

[`atom_branch_hyperbolicity_probe.py`](../../computations/meson/atom_branch_hyperbolicity_probe.py),
3 assertions:

| isotope | `A` | branches | hyperbolic | solver statuses |
|---|---:|---:|---:|---|
| proton | 1 | 4 | **0** | `degenerate` |
| neutron | 1 | 4 | **0** | `degenerate` |
| deuteron | 2 | 32 | **0** | `degenerate` |

**Not one of the forty branch closures carries hyperbolic volume.** `A = 1` had
never been checked — the sibling swept `²H` only — and `²H` here is an
**independent re-run** that corroborates their 32/32 rather than citing it.

### Both controls, because a null needs them

A detector that can only say zero would produce this table whatever the truth.
So the run asserts before reporting:

- **positive** — the figure-eight must read `2.029883212819307`. Measured at
  `high_precision()` (~212 bits): **delta `2.5 × 10⁻¹⁶`**. The pipeline can see
  hyperbolic volume.
- **negative** — the trefoil, a torus knot, must not read geometric. It reads
  `degenerate`. So a `degenerate` verdict is a fact, not a solver default.

### What this establishes, combined with the bound

`|tr_M(atom)| ≤ max_b |J_{K_b}(q)|` is sorry-free, and **every branch in that max
is non-hyperbolic**. So there is no branch from which a hyperbolic volume could
be drawn: substituting `Vol(𝓑₃) = 7.3277` is not recovering something latent in
the expansion — it is supplying, from outside, a quantity the object does not
have anywhere in it.

That is **Obstruction A with a mechanism** rather than as an observation, and it
now covers `A = 1`, which the torus-closure framing never reached.

### Still not a volume statement

The temptation remains and is still refused: this does **not** say
`Vol_eff(atom) = 0`. Going from "every branch is non-hyperbolic" to a statement
about the atom element's own volume needs the `tr_M ~ exp(Vol)` step, which is an
asymptotic in the **colour** `N`, not a pointwise bound — see Addendum 6, where
the corpus's own numbers refute the misuse. What is established is exactly the
table: **no branch is hyperbolic**.

### A note on the precision fix, because `fmt` was the wrong instinct

The first run put SnapPy's float64 volumes into the witness and the raw-float64
ratchet flagged 50 fields, correctly. The reflex fix — `fmt()` them — would have
been **laundering**: `_precision`'s own docstring says `fmt` *"will happily render
a 53-bit value out to the full serialization width, so the number reads as
measured while carrying ~15 significant digits"*, which is precisely what the
float64-padding ratchet exists to catch.

The real fix was that there was nothing to serialise. Every branch is
**`degenerate`** — not "volume `0.0`" but *no hyperbolic structure*, so a `0.0`
would misrepresent an absence as a measured zero. Branch rows now carry the
solver status and the boolean, no volume field; only the calibration, a genuine
measurement, carries a number, taken at ~212 bits where its digits are real.
`precision-gates.sh --changed`: **all blocking gates green.**
