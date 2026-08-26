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

---

## Addendum 8 — the design question, answered from inside the framework (2026-08-26)

Asked to investigate whether the mass law wants a different geometric functor for
non-link carriers, or a different carrier. **Neither. `Geom` is simply undefined
on the carriers it is being applied to.**

### The framework already states the rule — and applies it elsewhere

`prop:hoefsmit-scattering-pipeline` Stage 3 makes `Geom(K)` a **three-way case
split** on geometric type, with *different physical meanings*:

| case | `Geom(K)` | meaning |
|---|---|---|
| **hyperbolic** | `Vol(K)/ℏ_q²` | mass / energy |
| **torus** | `CS(K)·ℏ_q²` | coupling phase |
| **unknot** | `0` | vacuum |

And [`em-coupling-chern-simons.md`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.md)
**applies it**, verbatim:

> *"The torus knots `T_{2,9}` and `T_{3,5}` are **non-hyperbolic**. Their τ-image
> geometric invariant is the **Chern–Simons functional, not the hyperbolic
> volume**."*

So the framework does not need a new functor for non-hyperbolic carriers. It has
one, states when to switch, and switches correctly — **in the α_EM sector**.

### But no case covers the atom carriers

Non-hyperbolic is not the same as torus. By Nielsen–Thurston a non-hyperbolic
closure is torus **or reducible**, and a **connected sum is in neither** — Stage 3
has no case for it. Measured
([`atom_branch_geom_case_probe.py`](../../computations/meson/atom_branch_geom_case_probe.py),
3 assertions):

| isotope | branches | prime | **composite** | prime summands each |
|---|---:|---:|---:|---:|
| proton | 4 | 0 | **4** | 2 |
| neutron | 4 | 0 | **4** | 2 |
| deuteron | 32 | 0 | **32** | **5** |

**40 of 40 composite. Zero prime.** Controls: the granny knot (trefoil # trefoil)
splits into 2, the trefoil does not split.

So the `Vol(𝓑₃)` substitution is **not picking the wrong case of the split —
there is no case to pick.** Even the CS branch does not rescue it: `CS` is stated
for *torus* knots, and these are composites of them.

### Why there is no volume, mechanically

Hyperbolic volume is **additive under connected sum** (Thurston):
`Vol(K₁ # K₂) = Vol(K₁) + Vol(K₂)`. Each branch decomposes into summands that are
themselves non-hyperbolic, so the sum of their volumes is zero. That is *why*
Addendum 7's forty `degenerate` verdicts came out the way they did — the two
measurements agree, and this one supplies the mechanism.

Note the exact regularity: **the summand count equals the number of averaged
letters** — 2 for the proton and neutron, 5 for the deuteron, uniform across all
32 of its branches. Recorded as an observation; the natural reading is one
connected-sum factor per maximal single-generator block, but that is not measured
here.

### A correction to Addendum 6, in the sibling's favour

Addendum 6 reported that the sibling audit's stated reason — *"each branch braid
is monotone, so its closure is a connected sum of `(2,k)` torus links"* — did not
reproduce under either reading of "monotone" I tested. That stands. **But their
conclusion is now independently confirmed by direct measurement: the closures
*are* connected sums, 40 of 40.** The reasoning step I could not reproduce led to
a correct result, and it is only fair to say so.

### What this leaves

The mass law reads `Geom(K)` for a `K` on which `Geom` has no defined value. That
is not a bug in a producer, and it is not fixed by choosing the other branch of
the split. It is a gap in Stage 3 itself: **the case analysis is incomplete for
composite carriers**, and the framework's own carriers are all composite.

Two directions, both for the author — neither is a computation:

1. **Extend the split.** Give `Geom` a composite case. Additivity of volume makes
   `Σᵢ Geom(Kᵢ)` the natural candidate, and for these carriers it is `0` — which
   would say the atom carriers contribute no mass through this functor at all.
2. **Change the carrier.** Require the atom's `K` to be prime and hyperbolic,
   which the current `atom_braid_word_3A` construction does not produce in any
   branch.

Bean `qou-7p7d`. Obstruction A is unchanged in substance and now has its
mechanism: composite ⇒ additive ⇒ zero.

---

## Addendum 9 — what the carriers are, and how the sectors compare (2026-08-26)

### What the non-link carriers actually are

The proton carrier is not a link; it is a **convex combination of four links**,
each weight `1/4`:

| branch | closure |
|---|---|
| `σ₁⁷ σ₂⁻³ σ₂` | `T(2,7) # T(2,4)` |
| `σ₁⁷ σ₂⁻⁴` | `T(2,7) # T(2,4)` |
| `σ₁⁴ σ₁⁻¹ σ₁² σ₂⁻³ σ₂` | `T(2,7) # T(2,4)` |
| `σ₁⁴ σ₁⁻¹ σ₁² σ₂⁻⁴` | `T(2,7) # T(2,4)` |

measured as a 7-crossing 1-component piece and a 4-crossing 2-component piece —
the classical fact that a 3-braid `σ₁^a σ₂^b` closes to `T(2,a) # T(2,b)`. The
deuteron's 32 branches each carry **five** summands,
`T(2,4) # T(2,7) # T(2,4) # T(2,7) # unknot`.

So: **every constituent is a `(2,k)` torus link, glued by connected sum.** Not one
hyperbolic piece anywhere in the expansion.

### The mathematical context

Three standard facts fix the situation, and none of them is a QOU claim:

1. **A 3-braid `σ₁^a σ₂^b` closes to `T(2,a) # T(2,b)`.** The branch structure is
   forced by the word shape, not by the substrate.
2. **Volume is additive under connected sum** (Thurston):
   `Vol(K₁ # K₂) = Vol(K₁) + Vol(K₂)`. So a composite of torus pieces has volume
   `0 + 0 = 0` — Addendum 7's forty `degenerate` verdicts, explained.
3. **The natural extension of `Vol` to all knots already exists**: the **Gromov
   norm** (simplicial volume) `‖S³∖K‖`, which equals `Vol/v₃` on hyperbolic
   pieces, vanishes on Seifert-fibered ones, and *is additive under connected
   sum*. So "extend the functor to composites" is not an open construction — it
   is standard, and **it gives zero here.**

That last point is the sharp one: the obvious repair is available, principled,
and does not help.

### The physical context

Hyperbolic volume is the **classical action** of `SL(2,ℂ)` Chern–Simons theory on
the complement — which is why the volume conjecture reads `J_N ~ exp(N·Vol/2π)`
and why the framework maps it to *mass/energy*. Torus knots are
**Seifert-fibered**: no hyperbolic bulk, so no action to exponentiate; what
survives is the Chern–Simons invariant, a rational **phase**. Hence Stage 3's
*coupling phase*, and hence `em-coupling-chern-simons.md` switching functor.

A **connected sum** glues pieces at a point — no essential interaction, no new
bulk. So the atom carrier is a superposition of trivially-glued Seifert pieces:
**nothing in it has the bulk that carries mass**, and that is a statement about
the construction, not about the physics it is aimed at.

### The other sectors — measured

| sector | carrier | type | `Vol` | functor used |
|---|---|---|---:|---|
| lepton `m_μ` | `4₁` | **hyperbolic** | 2.02988 | `Vol/ℏ_q²` ✓ |
| nucleon `m_p, m_n` | `𝓑₃` (L6a4) | **hyperbolic** | 7.32772 | `Vol/ℏ_q²` ✓ |
| atom `D` | `6₂` | **hyperbolic** | 4.40083 | `Vol/ℏ_q²` ✓ |
| atom `T` | `8₁₁` | **hyperbolic** | 8.28632 | `Vol/ℏ_q²` ✓ |
| α_EM | `T(2,9)`, `T(3,5)` | torus | 0 | **`CS·ℏ_q²`** ✓ |
| meson `𝔐` | `T(2,5)` | torus | **0** | — **this is Obstruction A** |

**Every named atlas carrier is genuinely hyperbolic**, so the atlas is correctly
inside the `Vol` case. And α_EM correctly switches. So the framework gets the
case split right wherever it has actually classified the carrier.

### What this reframes

**Obstruction A is Stage 3 working, not failing.** The meson braid closes to
`T(2,5)`, a torus link. Stage 3 says a torus carrier yields `CS·ℏ_q²` — a
**coupling phase, not a mass**. So "the meson carrier has `Vol = 0`" is not an
accident blocking a mass derivation; it is the case split *declining to produce a
mass*, exactly as it declines for `T(2,9)` in the α_EM sector where the framework
accepts the answer.

Three distinct situations, then, and they should not be conflated:

1. **α_EM** — torus carrier, torus functor, coupling wanted. **Consistent.**
2. **Meson** — torus carrier, torus functor available, but a **mass** is wanted.
   Obstruction A: the split says this carrier cannot supply one.
3. **Atom** — the traced object is **composite**, which Stage 3 does not cover at
   all, and whose standard extension (Gromov norm) gives zero.

### Scope

Measured: carrier types and branch decompositions. **Not** claimed: that any
sector's number is wrong, or that the `CS` route would yield the meson mass —
the Chern–Simons branch produces a phase by the framework's own labelling, and
whether a mass can be recovered from it is not addressed here.

---

## Addendum 10 — the missing physical sector *is* the missing mathematical case (2026-08-26)

Asked whether the mathematical sectors exhaust the expected physical ones, and
where the missing binding term sits. **They do not exhaust, and the two gaps are
the same gap.**

### What the classification actually has

For a **prime** knot the classical trichotomy (Thurston, via JSJ) is exactly
three cases:

| case | complement | `Geom` in Stage 3 |
|---|---|---|
| **torus** | Seifert-fibered | `CS(K)·ℏ_q²` — coupling phase ✓ |
| **satellite** | essential **torus**, non-trivial JSJ | **— no case —** |
| **hyperbolic** | complete `H³` structure | `Vol(K)/ℏ_q²` — mass/energy ✓ |

Stage 3 lists torus, hyperbolic, and the unknot. **The satellite case is
missing** — and non-prime (connected sum, essential **sphere**) is missing too,
which is Addendum 8's measured 40/40.

### The missing binding term is the satellite case, and the corpus already says so

AGENTS.md describes the missing many-body term as *"a separate, super-pairwise
additive **extensive** object"*. That is a description of additivity over a
decomposition — and the corpus already has the conjecture,
[`conj:jsj-decomposition-linearity`](../../content/quantum-observable-universe/knots-particles-confinement/jsj-decomposition-linearity.md):

> *"The **inter-nucleon braids form essential tori**, the complement decomposes
> under the Jaco–Shalen–Johannson (JSJ) decomposition into `Z` proton-block
> pieces and `N` neutron-block pieces with isotope-independent volume quanta"*
>
> $$\mathrm{Vol}(\mathcal{K}(Z,N)) = Z\cdot\mathrm{Vol}_p + N\cdot\mathrm{Vol}_n$$

Additivity of volume over JSJ pieces is a **theorem** (Thurston); the block says
so, and correctly locates the conjectural content in the decomposition
hypothesis. An essential torus is a companion/pattern structure — a genuine
bound state — and additivity over its pieces is extensive and super-pairwise by
construction. **This is the missing term, in the right mathematical language.**

So the physical sectors and the mathematical cases line up exactly:

| physical | mathematical | status |
|---|---|---|
| coupling (α_EM) | torus | ✓ has functor, correctly used |
| mass/energy (lepton, nucleon) | hyperbolic | ✓ has functor, carriers verified hyperbolic |
| **many-body binding** | **satellite / JSJ** | **conjecture exists; `Geom` has no case** |
| vacuum | unknot | ✓ |

### Two things that block it, both measured

**1 · `Geom` assigns no value to a satellite carrier.** `conj:jsj-decomposition-linearity`
proposes the additive quantity, but Stage 3 gives no `Geom` case for the
essential-torus class, so the conjecture has no functor to land in. Extending the
split here is not cosmetic — it is where the binding term would enter.

**2 · The measured objects are not satellites.** They decompose along essential
**spheres**, not essential **tori** — connected sums of `(2,k)` torus links,
40/40 (Addendum 8). Connected sum is *not* the satellite case. So on the objects
the compute actually traces, `Vol_p = Vol_n = 0` and the linearity reads
`0 = Z·0 + N·0` — true, and empty.

### And the contradiction is at the definition, not the compute

[`def:atom-knot`](../../content/quantum-observable-universe/knots-particles-confinement/atom-knot.md):

> *"An **atom of type `(Z,N)`** is a **closed braid `K`** whose Gröbner–Shirshov
> normal form in `H_{n(K)}(q)` admits a block decomposition … `n(K) = 3(Z+N)`."*

A **closed braid** — a genuine link — on exactly the strand count
`atom_braid_word_3A` uses. What that producer returns is **not a closed braid**:
it lies outside `im(ρ)` because `2A+1` letters are averages (measured). So the
gap is not a producer bug downstream of a sound definition; **the definition
demands an object the construction does not build**, and `conj:jsj-decomposition-linearity`
inherits that, since `𝒦(Z,N)` presupposes it.

### What this makes the live question

Not "which functor for non-link carriers" — that was my framing and it was too
narrow. The live question is upstream:

**Can the atom be built as an actual closed braid, as `def:atom-knot` requires,
whose JSJ decomposition has the hyperbolic pieces `conj:jsj-decomposition-linearity`
needs?** If yes, the binding term follows from a theorem (volume additivity over
JSJ) rather than an ansatz — which is what the Δ_λ gate has been asking for. If
no, both the definition and the conjecture need restating.

That is a construction question, and it is where I would put the next effort.

### Scope

**(a)**. Measured: carrier types, branch decompositions, the definition's wording.
**Not** claimed: that `conj:jsj-decomposition-linearity` is false — it is stated
for an object the compute does not currently build, so it is untested rather than
refuted. Nor that a qualifying construction does not exist; none is exhibited
here either way.

---

## Addendum 11 — resolving the definitional contradiction: the averaging *is* Type B (2026-08-26)

`def:atom-knot` demands a **closed braid**; `atom_braid_word_3A` returns an
element outside `im(ρ)`. Asked how to resolve it. **The construction has already
folded to Type B — by hand, at a degenerate parameter — and that is why it fell
out of the braid group.**

### The averaged letter, identified

The averaged letter is `σ − h/2 = (σ + σ⁻¹)/2`. Its spectrum, computed:

$$\text{eigenvalues}\bigl((\sigma+\sigma^{-1})/2\bigr) = \pm\frac{[2]_q}{2}$$

Symmetric about zero, so it is **`[2]_q/2` times an involution** — *not* a braid
generator, whose eigenvalues are `q, −q⁻¹`.

Now compare the **Type B** Hecke algebra, whose extra generator `T₀` satisfies
its own quadratic `(T₀ − Q)(T₀ + Q⁻¹) = 0` with a **second parameter `Q`**.
Solving `c·T₀`'s eigenvalues `= ±[2]_q/2` has a **unique** solution:

$$Q = 1, \qquad c = \frac{[2]_q}{2}$$

**So the averaged letter is exactly `([2]_q/2)·T₀` at Type-B parameter `Q = 1`,**
where the quadratic degenerates to `T₀² = 1` — a genuine involution.

That is an identification, not an analogy. And `σ ↦ σ⁻¹` is the **bar
involution**, so `(σ + σ̄)/2` is a bar-symmetrization: the construction is
hand-encoding CPT/chirality neutrality.

### Which is precisely what AGENTS.md §7b says not to do

> *"**Type B folding for chirality / CPT.** To enforce matter–antimatter pairing
> structurally in the reduction engine, **do not write custom `ℤ/2ℤ` rules**.
> Fold the `𝔰𝔩ₙ` Cartan datum into a Type B datum; … its GS normal forms are
> **bar-involution (`q ↦ q⁻¹`) invariant by construction**."*

The averaging is a custom `ℤ/2ℤ` rule. Written inside a **Type A** algebra, those
elements are outside `im(ρ)`; written in the **Type B** datum they are
*generators*, and the object stays a braid. **The measured defect is the exact
cost §7b predicts.**

### Why this resolves three things at once

The library already holds the machinery — all three ingested:

| source | supplies |
|---|---|
| [`arxiv-math-0405508v1`](../../library/arxiv-math-0405508v1/) — Geck–Lambropoulou, *Markov traces and knot invariants related to Iwahori–Hecke algebras of type B* | the Type-B Markov trace, and the closure theory |
| [`arxiv-math-9806163v1`](../../library/arxiv-math-9806163v1/) — *Weights of Markov traces on Hecke algebras* | the weights at minimal idempotents for type `Bₙ` — the `y_λ` analogue |
| [`fd58d8e182ed…`](../../library/fd58d8e182edda805fed0946606c5ab82f81/) — *Gröbner–Shirshov bases for Temperley–Lieb algebras* | GS bases **of type B** — the normal-form machinery `def:atom-knot` is stated in |

And the geometric payoff is in Geck–Lambropoulou's own words, from the ingested
text: type-B braid closures *"correspond bijectively to **isotopy classes of
knots in the solid torus**"*.

A knot in a solid torus, embedded along a companion, **is a satellite** — its
complement contains an **essential torus**. So the single move §7b prescribes
delivers, simultaneously:

1. a genuine **closed braid** → `def:atom-knot` becomes satisfiable;
2. bar-invariance **by construction** → the CPT content the averaging hand-rolled;
3. a **solid-torus / satellite** carrier → the essential torus
   `conj:jsj-decomposition-linearity` needs, which is exactly the **missing
   `Geom` case** of Addendum 10.

Three separate gaps, one move, and the corpus already prescribes it and holds the
sources.

### The test that would settle it, and what would refute it

Since `([2]_q/2)·T₀` at `Q = 1` is the *same algebra element*, the natural
hypothesis is that reading the atom word in the Type-B setting **reproduces the
current `tr_M` values** — the numbers do not move, but the object becomes a
braid with a closure and a volume.

**That is a hypothesis, not a claim.** The Type-B Markov trace is a *different*
functional with its own parameters and weights, so it need not agree with the
Type-A one. The decisive computation:

1. Write the atom word in the Type-B generators (`σᵢ` for the intra-block
   crossings, `T₀` at `Q = 1` for the `2A+1` averaged sites).
2. Evaluate the **Geck–Lambropoulou** trace, with the `arxiv-math-9806163v1`
   weights.
3. Compare against the recorded `tr_M` — proton `1.1457596924573008697` at `q₀`.

**Refuted if** the Type-B trace disagrees with the recorded values, or if the
`Q = 1` specialisation is degenerate for the trace (a real risk: `Q = 1` is a
non-generic parameter, and Markov-trace weights can blow up there).

### Scope

**(a)**, and the identification is the only part that is measured. Computed here:
the averaged letter's spectrum, and that `Q = 1, c = [2]_q/2` is the unique
solution matching a scaled `T₀`. Verified by reading: §7b's wording, and
Geck–Lambropoulou's solid-torus statement in the ingested text.

**Not** established: that a Type-B construction reproduces the corpus's numbers,
that its JSJ pieces are hyperbolic, or that `conj:jsj-decomposition-linearity`
then follows. No construction is exhibited — this identifies the route and the
first computation on it. Bean `qou-7p7d`.

### Addendum 11a — two refinements, one of them to my own test

**The solid-torus identification is now sourced, not recalled.** Geck–Lambropoulou,
from the ingested text:

> *"there exist braid structures related to arbitrary 3-manifolds … also that, if
> the 3-manifold is a **solid torus**, then the sets of related braids form
> groups, which are in fact the **Artin–Tits braid groups related to the B-type
> Coxeter groups**."*

and their trace *"is used in [7] for constructing a **4-variable analogue of the
homfly-pt polynomial** for oriented knots inside a solid torus."* So Addendum 11's
central link is the paper's own theorem.

**But my test as stated is under-specified.** I wrote *"evaluate the
Geck–Lambropoulou trace"* as if it named one object. The paper's stated aim is

> *"to give a full **classification of all linear traces** on Iwahori–Hecke
> algebras of type B which support the Markov property"*

— a **family**, not a single functional. So the test must say *which* trace, and
the classification is what supplies the candidates. Corrected: the question is
whether **any** trace in the classified family reproduces the recorded `tr_M`,
and if one does, whether it is the one the Markov property singles out for
closures in the solid torus.

**Scoping the build, since none of it exists here.** `computations/kazhdan_lusztig.py`
cites Lusztig's *Hecke algebras with unequal parameters* for its convention but
implements **type A only** — `permutations_S_n`, plain permutations throughout,
no signed permutations. So the computation needs, in order:

1. `W(Bₙ)` — signed permutations, length function, Bruhat order;
2. the two-parameter Hecke algebra `H(Bₙ; q, Q)`, specialising `Q = 1`;
3. a trace from the GL classification, and the argument for which one.

That is a build, not a probe, and `Q = 1` is a non-generic specialisation where
trace weights may degenerate — the refutation condition already recorded. Noting
the size rather than starting it at the end of a long session: the route is
identified and sourced, and choosing to spend on it is the author's call.

### Addendum 11b — 🛑 the Type-B *route* is not realizable as I wrote it

Addendum 11 prescribed: *"write the atom word in the Type-B generators (`σᵢ` for
the intra-block crossings, `T₀` at `Q = 1` for the `2A+1` averaged sites)."*
**That is not realizable, and the prescription is withdrawn.**

Measured — the averaged letters sit at **distinct generator indices**:

| isotope | strands | averaged letters at `(position, generator)` |
|---|---:|---|
| proton | 3 | `(4, g=0)`, `(10, g=1)` |
| deuteron | 6 | `(4, g=0)`, `(10, g=1)`, `(11, g=2)`, `(15, g=3)`, `(16, g=3)` |

Type `Bₙ` has **exactly one** distinguished generator `T₀`, at one position; the
rest are ordinary braid generators. So the `2A+1` averaged sites cannot all be
`T₀` in a single type-`Bₙ` algebra. A single fold supplies one special node; the
word needs `2A+1` of them, at four distinct indices already at `A = 2`.

Nor does Lusztig's unequal-parameter setting rescue it directly: there the weight
function is **constant on conjugacy classes**, and the type-`A` generators
`σ₀ … σ_{n−2}` are all conjugate, so they cannot carry different parameters
within one type-`A` datum.

### What survives

- **The per-letter spectral identification, exactly.** Each averaged letter is
  `([2]_q/2)·ε` with `ε² = 1`, matching a `Q = 1` type-B generator's spectrum.
  `Q = 1, c = [2]_q/2` remains the unique solution. This is algebra and is
  Lean-provable; it is the next thing proved below.
- **The diagnosis.** The averaging is a hand-rolled bar-symmetrization —
  `σ ↦ σ⁻¹` is the bar involution — which is what §7b says not to write, and
  writing it inside a type-`A` algebra is exactly why the object left `im(ρ)`.
- **The geometric target.** Braids in a solid torus, satellites, essential tori,
  and the missing `Geom` case are unaffected; they are facts about what is
  needed, not about type `B` specifically.

### What is now open, restated honestly

The requirement is a structure with **`2A+1` involutive generators at distinct
positions**, interleaved with ordinary braid generators, whose closures live in a
manifold with essential tori. Type `Bₙ` is not it. Whether such a structure
exists — a multiply-folded datum, a Coxeter system whose special nodes are
non-conjugate, or something else — **is open, and I do not have a candidate.**

**And the trace comparison is moot in its stated form**: there is no type-`B`
word to trace, so running it would be computing on a premise this addendum has
just falsified. Not run, deliberately.

This is the ninth of my own claims corrected on this arc. It was found by
checking where the averaged letters actually sit, which took one measurement and
should have preceded the prescription rather than following it.

## Addendum 12 — the satellite vocabulary, and which third of my claim survives (2026-08-26)

Asked to unpack the terms in my own sentence: *"a knot in a solid torus,
embedded along a companion, is a satellite — an essential torus."* Each word is
load-bearing and none of them is framework jargon; they are standard 3-manifold
topology (Jaco–Shalen, Johannson, Thurston). Definitions first, then what the
construction actually buys, which is **less** than I claimed.

### The four terms

**Solid torus.** `V = S¹ × D²` — a circle thickened into a disc's worth of
directions, i.e. a doughnut *with* its inside. Its boundary `∂V = S¹ × S¹` is an
ordinary torus. Two curve classes on that boundary matter: the **meridian**
`{pt} × ∂D²`, which bounds a disc inside `V`, and the **longitude** `S¹ × {pt}`,
which does not.

**A knot in a solid torus.** A knot `P ⊂ V` — the *pattern*. It is a knot in the
doughnut, not in `S³`, so the same `P` can be realised in `S³` many different
ways depending on how `V` is put there. A pattern has a **winding number**: how
many times `P` runs around the `S¹` direction, algebraically. A closed braid on
`n` strands is exactly a pattern with winding number `n` that meets every
meridian disc in `n` points — that is the whole content of Alexander's theorem
read in the solid torus.

**Companion, and embedding along it.** Take a second knot `C ⊂ S³` — the
*companion* — and let `N(C)` be a tubular neighbourhood of it, which is itself a
solid torus. An **embedding along `C`** is a homeomorphism `f : V → N(C)` taking
the longitude of `V` to the longitude of `C` (the framing choice; the standard
one is Seifert framing). The image `K = f(P) ⊂ S³` is a knot in the 3-sphere.

**Satellite.** That `K` is a **satellite knot** with pattern `P` and companion
`C`, provided the construction is non-trivial: `P` is neither contained in a ball
inside `V` (else `K` is just `P` in a ball, and `C` is invisible) nor isotopic to
the core `S¹ × {0}` (else `K` is just `C`, and `P` is invisible). Cable knots,
Whitehead doubles and connected sums are all satellites; the last is the case
this arc keeps running into.

**Essential torus, and why the word "is".** The image of `∂V` in `S³` is a torus
`T ⊂ S³ ∖ K`. Non-triviality is exactly the statement that `T` is **essential**:
incompressible (no disc in the complement whose boundary is an essential curve on
`T`) and not boundary-parallel. So "satellite" and "the complement contains an
essential torus" are the *same* condition, not two conditions that happen to
co-occur. That is why the sentence says "is" rather than "gives".

**Why it matters for `Geom`.** The JSJ decomposition cuts a knot complement along
its essential tori into pieces that are each hyperbolic or Seifert-fibred, and
this decomposition is canonical. Thurston's trichotomy for prime knots — torus,
satellite, hyperbolic — is the statement that the complement either *has* such a
torus (satellite) or does not, and then is hyperbolic or Seifert-fibred. So the
missing case in the Stage-3 `Geom(K)` split is not a gap in coverage of some
list; it is the **one case with internal structure**, and it is precisely the
case `conj:jsj-decomposition-linearity` is about. That conjecture says the atomic
complement decomposes along inter-nucleon tori into `Z` proton and `N` neutron
pieces. Inter-nucleon tori *are* essential tori. A framework whose `Geom` has no
satellite case cannot state its own binding conjecture.

### What the construction buys — one of three, not three

I wrote that one move gives three things at once. Checked individually, **one
survives, one is weakened to a target, and one is withdrawn.**

| claim | status |
|---|---|
| a genuine closed braid, so `def:atom-knot` is satisfiable | **survives** — a pattern of winding number `n` meeting each meridian disc in `n` points is a closed braid in `V` by definition, and its satellite image is a knot in `S³`; nothing about this depends on the algebra |
| a satellite carrier — the essential torus the JSJ conjecture needs | **survives as a target, not as a construction** — the topology is what is *wanted*; no atom braid word producing it exists, and building one is the open construction question (bean `qou-7p7d`) |
| bar-invariance by construction (the CPT content) | **WITHDRAWN** — this rested on the type-`B` reading falsified in §11b |

The third is the one to be careful about, because it is the one that made the
sentence sound like a solution rather than a wish. "Bar-invariance by
construction" was §7b's promise about *folded* Cartan data: fold `𝔰𝔩ₙ` to type
`B` and the GS normal forms are bar-invariant for free. §11b measured that the
fold is unavailable here — `2A+1` involutive sites at distinct generator indices,
against type `Bₙ`'s single `T₀` — so there is no fold, and therefore no free
bar-invariance. What is left is the hand-rolled averaging that §7b tells you not
to write, which is the defect, not the fix.

The per-letter spectral fact does survive and is now Lean-proved
([`AveragedLetterSpectrum.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/AveragedLetterSpectrum.lean),
six declarations, sorry-free, axiom-clean): the averaged letter is `([2]_q/2)·ε`
with `ε² = 1`, and a scaled generator with eigenvalues `cQ, −cQ⁻¹` matches `±t`
only at `Q² = 1`, hence `Q = 1`, `c = t` under positivity. That is a statement
about **one letter's spectrum**. It is not a statement about an algebra, and the
file's docstring says so.

### The open question, in these terms

Find a pattern `P` in a solid torus which (i) is a closed braid, so
`def:atom-knot` is satisfied on the nose; (ii) has `Z + N` companion pieces under
JSJ, so `conj:jsj-decomposition-linearity` has something to be true of; and
(iii) has bar-invariant normal forms **structurally** rather than by averaging.
(i) and (ii) are ordinary satellite topology and are not the hard part. (iii) is
the hard part, it is what the averaging was standing in for, and after §11b there
is no candidate mechanism for it. Recorded as open on `qou-7p7d`; no route
claimed.

## Addendum 13 — colour averaging, and the prune I could not name in §11b (2026-08-26)

Four questions, and they turn out to be one. Asked whether I had tried **colour**
averaging rather than plain averaging; whether the thing is really a group action
with an `SU(5) → SU(3)×SU(2)×U(1)` shape, or a finite-group or groupoid action
wanting derived-category / gerbe machinery; which isotope would first show a
third channel; and what the SDP solution and LP shadow dual actually say.

I had not tried colour averaging. It is the distinction that decides §11b, and
it was named in the producer's own docstring all along.

### 1 · Two templates, not one — and only one of them has a second parameter

`atom_braid_word_3A` emits two non-braid templates:

```
sigma - (h/2)*1          == (sigma + sigma^-1)/2                  colour-BLIND
sigma - h*(1/2 - d/4)*1  == (1/2+d/4)sigma + (1/2-d/4)sigma^-1    colour-WEIGHTED
```

The second is the default and is canonical (`bring_color_weighted`, owner ruling
R3). Every measurement on this arc — the census, §11b's generator indices, and
[`AveragedLetterSpectrum.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/AveragedLetterSpectrum.lean)
— treated the `2A+1` non-braid letters as one kind.
[`atom_letter_colour_spectrum_probe.py`](../../computations/meson/atom_letter_colour_spectrum_probe.py)
splits them (8 assertions, exact template match at 60 dps, worst gap `0.0`, zero
unclassified):

| isotope | letters | σ | σ⁻¹ | symmetric | **colour** | colour at gen |
|---|---:|---:|---:|---:|---:|---|
| proton | 11 | 6 | 3 | 2 | **0** | — |
| neutron | 11 | 5 | 4 | 2 | **0** | — |
| deuteron | 23 | 11 | 7 | 4 | **1** | `[2]` |
| helium-3 | 35 | 18 | 10 | 6 | **1** | `[5]` |
| helium-4 | 47 | 23 | 15 | 8 | **1** | `[5]` |

So `2A+1 = 2A` symmetric **+ exactly one** colour-weighted letter, the unique
p–n interface. Under `strict_averaged` the colour count is `0` and the symmetric
count is `2A+1` — the control that separates the conventions, and the reason
lumping them hid this.

Spectra follow from `μ₊ = w₊q + w₋q⁻¹`, `μ₋ = −w₊q⁻¹ − w₋q`, so `μ₊ + μ₋ = 0`
iff `w₊ = w₋`:

| template | `w₊` | `μ₊ + μ₋` | `Q` |
|---|---|---|---|
| symmetric | `1/2` | `0` | `1` |
| colour | `1/2 + δ/4` | `1.438e-4` | **`1.0000715145…`** |

Matching a scaled generator `cQ, −cQ⁻¹` gives a unique `Q > 0` because
`Q ↦ Q − Q⁻¹` is a bijection `(0,∞) → ℝ`. On the symmetric letter it returns
`Q = 1`, `c = [2]_q/2` — reproducing the Lean result as a **control**. On the
colour letter it returns `Q ≠ 1`, departing at leading order `(δ/4)h/c`.

**§11b's count objection is therefore wrong as stated.** It said `2A+1` averaged
letters at distinct indices against type `Bₙ`'s single `T₀`. Exactly one letter
carries a second parameter, and type `B` has exactly one `T₀`.

### 2 · The prune that does hold, and it is proved rather than counted

The route still does not work, for a better reason. The `2A` symmetric letters
sit at `Q = 1`, where a type-`B` generator degenerates to a reflection
(`T₀² = 1`) — so they are neither ordinary `q`-generators (eigenvalues
`q, −q⁻¹`) nor `T₀` (`cQ, −cQ⁻¹` with `Q ≠ 1`). Three parameter classes are
needed; type `B` supplies two.

And underneath that sits a **structural** exclusion, scope (b), with a named
invariant. [`VolumeConstraintForcesFibreTwo.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/VolumeConstraintForcesFibreTwo.lean)
(sibling work, on `main` since `fed69b1c4d`, sorry-free) proves

```
exteriorSquareDim_eq_one_iff : exteriorSquareDim N = 1 ↔ N = 2
```

so the strong volume constraint `Λ²V ≅ 𝟙` — the non-degenerate volume form that
*defines* the fibre — pins the fibre dimension at `2`, hence the Schur–Weyl row
cap at two rows. A type-`B` fold is a refolding of **one fibre's** Cartan datum;
it does not change that fibre's dimension. So no type-`B` structure, and no
other single-algebra structure, can reach a third row. That is the exclusion
§11b reached for and could only support by counting.

Its anti-vacuity companion `weak_volume_reading_admits_three` (also sorry-free)
shows the two readings differ: the **weak** constraint `Λ²V ≠ 0` gives only
`2 ≤ N` and admits `N = 3`. So the third row is not absurd — it is what you get
by giving up `Λ²V ≅ 𝟙`.

**A caution, recorded because I nearly published the opposite.**
`conj:sm-gauge-truncation` says a single-fibre realisation of the three factors
"contradicts a proved theorem of the framework", citing `thm:su2-emergence`.
That citation does not carry: `QOU.SU2Emergence` is a `structure` whose fields
are `gaugeGroupType`, `ext_sq_action` and `det_one`; it never mentions `SU(2)`
or the rank, and its two supporting lemmas are `class … : Prop` restating their
own conclusions. I was going to report that as a finding. **The corpus already
records it** — `VolumeConstraintForcesFibreTwo.lean`'s own header sets it out in
two numbered points, including that the `lean.ref` does not resolve. Corpus-grep
caught it; the sixth time on this arc that the answer was already on disk.

### 3 · The SDP dual, and why its headline finding is convention C

`deuteron-real-sdp.witness.json` carries a full dual — `y0_star = −0.01443`,
`y_star` over 11 blocks, `active_set` of 7 — and reports
`strong_duality_holds: false` with `duality_gap: 43926.6`, against a
`phase_B_interim` gap of `8.1e-43`. Its diagnostic blames an **indefinite**
Frobenius Gram with three forbidden negative-norm blocks, and its `symmetry_note`
calls the pattern *"the §7b bar-involution / Type-B-folding signature"*.

I was about to cite that note as the mechanism §11b said did not exist.

The Gram is diagonal with `G_λλ = tr_M(P_λ) = y_λ(q₀)` — the producer says so at
its own lines 18–21 — so its signature is just the sign pattern of the Markov
weights. Convention D caps them at two rows, and all three "forbidden" blocks
have `ℓ ≥ 4`. Compared entry by entry at `n = 6`
([`markov_weight_support_conjugation_probe.py`](../../computations/meson/markov_weight_support_conjugation_probe.py)):
eleven nonzero entries in the witness against **four** live, the other seven
exactly zero, and **every survivor positive**. Swept `n = 3, 6, 9, 12`: **no
negative weight at any `n`.**

So that witness is convention **C**. Under **D** the Gram is positive
semidefinite with a kernel: the SDP is still ill-posed, but as a **singularity**
(bean `qou-cds2`), not an indefiniteness — a different defect with a different
fix, and the "folding signature" reading goes with it. The witness is not
corrected here, only shown not to describe D; re-running it under D is its own
change.

### 4 · The simplest isotope: A = 2, and the third channel is a third ROW

The D support is exactly the two-row partitions (`⌊n/2⌋+1` of them, asserted).
Conjugation `λ ↦ λ′` is the combinatorial shadow of the bar involution. A
two-row `λ` of `n ≥ 6` has `λ₁ ≥ 3`, so `ℓ(λ′) ≥ 3` and `λ′` lies in the kernel:
conjugation maps the **whole support** into the kernel. At `n = 3` it does not,
because the unique self-conjugate partition of `3` is the staircase `(2,1)` —
two rows, nonzero weight. The unique self-conjugate partition of `6` is
`(3,2,1)` — three rows.

| | `n` | support | self-conjugate | supported? |
|---|---:|---|---|---|
| A=1 | 3 | `(3), (2,1)` | `(2,1)` | **yes** |
| A=2 | 6 | 4 two-row | `(3,2,1)` | no |
| A=3 | 9 | 5 two-row | 2, both `ℓ≥3` | no |
| A=4 | 12 | 7 two-row | 3, all `ℓ≥3` | no |

**The bar-fixed sector is inside the supported sector at `A = 1` and outside it
from `A = 2`.** The deuteron is where it changes — and independently the first
isotope carrying a colour-weighted interface letter.

Joining this to §2: three rows means `N = 3` means abandoning `Λ²V ≅ 𝟙`. And the
level family `z_r = q^r/[r]_q` recorded in
[`su5-hypercharge-n3-gate`](../../content/quantum-observable-universe/appendix-standard-model/su5-hypercharge-n3-gate.md)
says `N = 3` would carry `z₃`, not the canonical `z₂ = q³/(q²+1)`. So the third
channel is not merely unmeasured — **convention D's trace is blind to it by
construction**, because seeing it would require a different trace parameter.
That is what `y_λ = 0` for `ℓ > 2` is saying.

### 5 · The group action, honestly

The symmetric letter **is** a group average: the Reynolds operator of
`ℤ/2 = {1, bar}` acting by `σ ↦ σ⁻¹`, weights `(1/2, 1/2)`. The colour letter is
the same `ℤ/2` with weights `(1/2 + δ/4, 1/2 − δ/4)` — a **non-uniform** average,
so not a group average and not a projection onto invariants. A weighting that is
not the group's own measure is the shape one reaches for a **groupoid** rather
than a group, which is the instinct behind the question.

The corpus says the same thing from the other side, and says it as an open item:
`su5-hypercharge-n3-gate` records that climbing to another level *"requires
structure at the groupoid level"*, and `conj:sm-gauge-truncation` that any
`SU(3)` or `U(1)` realisation *"must come from symmetry visible only at the
groupoid level — multi-strand structure, framing data, and the interaction of
distinct fibres."* Held sources that bear on it: `arxiv-2010.12445v1` (stacks of
fibre functors and Tannaka reconstruction — the framework is Tannakian with
fibre functor `τ`, so this is the right register) and `arxiv-1901.08945v2`
(derived categories of gerbes decompose by the characters of the banding group —
the right register for a support that splits by character).

**No route is claimed.** `SU(5)` is `r = 5` and the corpus block already places
it strictly downstream of the unbuilt `r = 3`; nothing here builds either. What
§4 adds is that the wall is not abstract — it has an isotope number, `A = 2`,
and a mechanism, the third row.

### What this changes, in one place

| §11b said | now |
|---|---|
| `2A+1` averaged letters vs one `T₀` | **wrong**: exactly one letter has `Q ≠ 1` |
| no candidate mechanism for structural bar-invariance | still none — but the *reason* is now a sorry-free invariant, not a count |
| type-`B` route withdrawn | **stays withdrawn**, on the fibre-dimension prune |

The withdrawal survives; its argument does not. Eleventh and twelfth corrections
on this arc, and the first to a withdrawal — I withdrew on a measurement made
against the wrong convention, which is the same failure as trusting a stale bean:
the measurement was real and was about something else.

## Addendum 14 — three requested fronts: the SDP, the SU(2) theorem, the groupoid gate (2026-08-26)

### 1 · Convention C excised from the deuteron dual (`qou-tmou`)

The producer **could not run on `main`**. `sublemma-2-1-deuteron-branching` serializes
its characters as 60-digit strings — the drained-precision convention — and
`deuteron_real_sdp.py` multiplied them as floats (`TypeError: can't multiply
sequence by non-int`, then `dtype '<U64'` in `np.mean`). That is why the
committed witness stayed C-framed while its **input** had already been migrated
to D and re-pinned to proton: nobody could re-run it. Both parses fixed.

What the re-run changed:

| | C | D |
|---|---|---|
| `tr_M(β_D)` | 0.38836 | 0.57517 *(was simply stale)* |
| `frobenius_gram_indefinite` | true | **false** |
| forbidden negative-norm blocks | 3 | **none** |
| `strong_duality_holds` | false | **true** |
| `duality_gap` | 43926.6 | **3.7e-43** |
| `sign_flip_conjugate_pairs` | 3 | **none** |

**How the singularity is handled: it needs no repair to make the LP well posed.**
The unboundedness *was* the indefiniteness, and that was convention C. The
"Phase B colour-flavour constraints required for a well-posed bounded program"
headline is dead, and so is the "§7b Type-B-folding signature" note — rewritten
in place rather than deleted, so the record of what it claimed survives.

**What the singularity does cost, and I got this wrong first.** I wrote that
restricting to the support "changes nothing about the optimum". False. The
feasible set is `{x : Σx = n_target, Gx ≥ 0}` — the net constraint is a **plain
sum**. A kernel block has zero cost *and* a vacuous constraint, so it absorbs
the whole net requirement free:

| | full space | support-restricted |
|---|---|---|
| `primal_obj` | 3.7e-43 | **0.0370** = `dual_obj` |
| `y0_star` | ~2e-48 | **0.0642671** |
| `y_star` | uniform 0.168 filler | `[1.0026, 0.4805, 0.0309, ~0]` |
| active | all 11 blocks | `(6,), (5,1), (4,2)` — **not** `(3,3)` |

So the full-space answer is a free lunch through the kernel, meeting the net
requirement with blocks contributing nothing to `tr_M`. `support_restricted` is
now emitted and is the dual to read. The deuteron saturates the three dominant
two-row blocks and does not saturate `(3,3)`.

**Left open, in the witness rather than silently:** the six Phase-B encodings
still solve on the full space, so 1, 3, 5 and 6 all return `primal_obj = 0.0` —
including `5_lr_branching_canonical`, the production default (C gave −0.0056,
−22523, −2780, −20230). Only `4_ame_binding_equality` is unaffected. Until
those rows are projected onto the support, **no Phase-B primal objective is a
result**.

### 2 · `thm:su2-emergence` made a theorem (`qou-v1h5`)

A sibling had already recorded the defect in an `authorNote` and in
`VolumeConstraintForcesFibreTwo.lean`'s header: the prose proof takes the rank
as an *input* to both sub-lemmas, the `lean.ref` resolved to a contentless
`structure`, and the two supporting lemmas are single-field classes restating
their own conclusions. That note recorded it;
[`SU2EmergenceRankForced.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/SU2EmergenceRankForced.lean)
fixes it — five declarations, sorry-free, axiom-clean, `lean`-direct against the
real import cone.

The content is the **decomposition**:

- **which subgroup** — unitary + `det = 1` ⇒ special unitary — holds at *every*
  `N`. Stated at general `n` precisely so it cannot be traded for the other
  half again.
- **which rank** — `N = 2` — comes from the volume constraint alone, via
  `exteriorSquareDim_eq_one_iff`, and is the only place `2` enters.

`su2_emergence_rank_forced` states both conjuncts of one theorem.
Non-vacuity: at `N = 3` the volume hypothesis fails while the subgroup half
applies unchanged, so the rank conjunct is doing work.

**Still assumed, and now in the statement rather than implicit:** that
`Aut^⊗(τ)` *is* such a matrix set. This narrows the gap from "rank and subgroup
both assumed" to "the realisation is assumed". It does not close it.

### 3 · The groupoid gate — a second route, and no new claim (`qou-5t4b`)

`su5-hypercharge-n3-gate` says climbing levels *"requires structure at the
groupoid level"*, and `conj:sm-gauge-truncation` that `SU(3)`/`U(1)` *"must come
from symmetry visible only at the groupoid level"*. **The corpus has already
proved the confinement**, and says so plainly in `eightfold-open-problems`:

> *"That the search is confined to the groupoid level is now a theorem, not an
> extrapolation."*

— on the strength of the `Sym²` gate (`Sym2Gate.lean`, `Sym2GateParity.lean`).
So this is **not** an open item to re-declare, and the corpus-grep discipline
applies: I nearly wrote it up as one.

What is genuinely additive is a **second, independent** derivation, added as
`no_three_dimensional_fundamental_in_one_fibre`. The `Sym²` route constrains a
candidate `W` through the representation theory of its symmetric square; this
one constrains the *fibre* through the non-degeneracy of its volume form and
never mentions `Sym²(W)` at all. Two independent derivations of the same
negative are worth having.

**Neither supplies what is actually open**, which `eightfold-open-problems`
states exactly: *construct a three-dimensional object `W` in the multi-fibre
groupoid whose `Sym²(W)` is irreducible.* Nothing here bears on that. The
corpus also records the adjacent open items — whether flavour and colour
`SU(3)` are the same, different, or groupoid-dual; the truncation mechanism;
three generations — and none of them moved.

**Where this meets §13.** The measured wall there was the third *row*, at
`A = 2`. The wall here is the third *dimension*, at one fibre. They are the
same wall counted two ways: `ℓ(λ) ≤ 2` is the Schur–Weyl row cap at level
`r = 2`, and `r = 2` is `N = 2` is `Λ²V ≅ 𝟙`. What §13 adds is that it has an
isotope number; what this adds is that one fibre provably cannot cross it.

### Addendum 14a — a PR-body link that will not stay fixed (2026-08-26)

Recorded because it wasted three edits and will waste more. One markdown link in
the #5817 body renders as `[Name](``https://…``)` — the URL wrapped in double
backticks, which breaks it. It is **not in the submitted text**: a clean
`[Name](url)` was sent three times, twice with backticks in the link text and
once without, and it came back wrapped every time.

What does NOT explain it, each checked against a link in the same body that
renders fine: URL length (the `VolumeConstraintForcesFibreTwo.lean` link is
comparable and fine), the `.lean` extension (same link, fine), a feature-branch
path (the `atom_letter_colour_spectrum_probe.py` link is on the same branch and
fine), or link text repeating the URL's final path segment (the
`VolumeConstraintForcesFibreTwo` link does exactly that and is fine).

No mechanism identified. The workaround that holds is to not hyperlink that
file at all — name it in a code span, as the body's Lean section already does
for all three files. Do not spend another full-body rewrite on it.

## Addendum 15 — projecting Phase B onto the support: a negative, and a sharper mechanism (2026-08-26)

Bean `qou-6tcn`, the follow-on the previous addendum left open. §14 §1 said the
six Phase-B encodings still solved on the full 11-block space and so returned
`primal_obj = 0.0` through a "kernel free lunch", and that projecting their
constraint rows onto the support was follow-up work. Done — and the result is
a negative, plus a correction to how I described the free lunch.

### What the kernel actually buys

I wrote that the kernel blocks "absorb the net requirement at zero cost". True,
and incomplete. On the support `G` is strictly positive, so `Gx ≥ 0` **is**
`x ≥ 0` there. On the kernel `G = 0`, so `Gx ≥ 0` imposes **nothing** and `x`
may go **negative**, down to the `-M` bound.

So the kernel supplies **signed occupations**, and that is the load-bearing
part. It is not that the visible blocks were paying for something for free —
it is that the invisible ones could pay a *negative* amount.

### The bound

With `x ≥ 0` on the support and `Σx = n_target`, the objective is a convex
combination scaled by `n_target`, so

```
t·x  ≤  max_{λ ∈ support} t_λ · n_target  =  0.253938 × 0.575172  =  0.146058
B_D(AME2020)                              =  2.224566
                                    short by 15.23×
```

Measured in [`deuteron_support_reachability_probe.py`](../../computations/meson/deuteron_support_reachability_probe.py)
(6 assertions, two of them controls). The cost vanishes **identically** on the
kernel — `t_λ = y_λ·χ^λ` and `y_λ = 0` there — which is why the full-space
objective is insensitive to kernel occupation in the first place.

### All six encodings, projected

| encoding | full `primal_obj` | projected |
|---|---|---|
| `1_bar_involution_fold` | 0.0 | **infeasible** (row 3 degenerates, `0 = 0`) |
| `2_character_projection_colorflavor` | — | **infeasible** |
| `3_conservation_laws` | 0.0 | **infeasible** |
| `4_ame_binding_equality` | 2.224566 | **infeasible** |
| `5_lr_branching_canonical` | 0.0 | **infeasible** (row 2 degenerates, `0 = b`, `b ≠ 0`) |
| `6_scalar_9pair_ratio_fitted` | 0.0 | **infeasible** |

Each row now carries a `projection_row_report` giving the fraction of its
weight that sits on the kernel — 30 % to 65 % for the non-degenerate rows. Two
rows degenerate entirely. The infeasible one is `5_lr_branching_canonical`
row 2, the `μ = (1,1,1)` Littlewood–Richardson row, whose weight is **100 %**
on the kernel — and that encoding is the **production default**.

That the `(1,1,1)` row is the one to die is not a coincidence: `(1,1,1)` is the
three-row partition of 3, and the D row cap is exactly what zeroes it. The
constraint was carrying its content on a block the canonical trace cannot see.

### Scope, and what this is not

**(a), scope-limited.** Measured: the support, the cost on it, the ceiling, and
the projected feasibility of all six. **Not** claimed: that
`conj:jsj-decomposition-linearity` or any binding conjecture is false; that the
encodings are wrong; that the framework cannot reproduce the deuteron binding.
The statement is narrower and exact — **this** cost vector, on **this** program,
with non-negative occupations of the D-supported blocks, cannot reach the AME
value. A different cost, a different Wenzl level `r`, or a program that admits
signed occupations *for a stated reason* are all untouched.

And the full-space numbers this replaces were **not wrong arithmetic**. They
were the correct optimum of a program whose kernel is unconstrained. The finding
is that such a program does not mean what its field names suggest — which is
the same shape as §5's convention-C witness, one level down.

### What it says to the binding front

The sibling coordination on #5817 reported a calibration-free residual of
`+31.4 %` at ²H against `−59.2 %` at ⁴He, and #5812's argument that no
correction non-negative for all `A` can fix ⁴He while ²H overshoots. This adds
an independent reason to expect signed structure: the one program here that
*did* reach the AME value did so through negative occupations, and removing
them costs a factor of 15. **That is a hint about where the sign structure has
to live, not evidence that any particular correction supplies it** — nothing
here computes a binding contribution.

## Addendum 16 — the level escape is closed on arithmetic (2026-08-26)

§15 left three escapes from the deuteron infeasibility: a different cost, a
different Wenzl level, or a program admitting signed occupations. Choosing among
them is a modelling decision and is still not made here. But one of the three is
now **closed by measurement**, without needing the hard existence question
answered first.

### Widening the level makes it worse, monotonically

The Ocneanu parameter is a family `z_r = q^r/[r]_q` whose `r = 2` member is the
canonical `z₂ = q³/(q²+1)`, and the Schur–Weyl row cap at level `r` is
`ℓ(λ) ≤ r`. So raising `r` widens the support, and `y_lambda_su_n(n, q, N)`
takes that rank directly. Recomputing the whole reachability calculation at each
level ([`deuteron_reachability_vs_level_probe.py`](../../computations/meson/deuteron_reachability_vs_level_probe.py),
6 assertions, three of them controls):

| `r` | support | max rows | `n_target` | `max t` | ceiling | AME/ceiling |
|---:|---:|---:|---|---|---|---:|
| **2** | 4 | 2 | 0.575172 | 0.253938 | **0.146058** | **15.23×** |
| 3 | 7 | 3 | 0.315377 | 0.161031 | 0.050785 | 43.80× |
| 4 | 9 | 4 | 0.212258 | 0.118222 | 0.025094 | 88.65× |
| 5 | 10 | 5 | 0.160273 | 0.095810 | 0.015356 | 144.87× |
| 6 | 11 | 6 | 0.130108 | 0.082596 | 0.010746 | 207.01× |

**No level clears AME, and the canonical one is the best of them.** The ceiling
is strictly decreasing in `r`.

The mechanism is the normalisation. `y` is fixed by `Σ_λ y_λ f^λ = 1`, so a
wider support spreads the *same* total weight over more blocks: both `max t` and
`n_target` shrink, and the ceiling is their product. Widening the level does not
add room — it subdivides the room already there.

`χ^λ(β_D)` is a character of the braid image in the irrep `λ` of `H_n(q)`,
depending on `q` and `λ` only and not on the Markov parameter, so the committed
characters are reused across levels unchanged. Only the weights move.

### What this does and does not settle

It **closes the level escape on arithmetic alone**. That matters because the
existence question is much harder and is now not needed: `Λ²V ≅ 𝟙` pins the
fibre dimension at 2 (`exteriorSquareDim_eq_one_iff`, sorry-free), and
`su5-hypercharge-n3-gate` records that the levels are *alternatives, not stages*
— no construction in the framework supplies a fibre at any `r ≠ 2`. Every row
above `r = 2` is therefore a statement about a fibre the framework does not
have. Had one of them cleared AME, that would have raised a real question about
whether to go looking for such a fibre. None does, so the question does not
arise.

**Two escapes remain**, and both are still the author's call:

* **A different cost.** Quantified: at the canonical level a cost reaching AME
  needs `max(t) ≥ AME/n_target = 3.8677` against the actual `0.2539` — a factor
  of **15.23×**. That is the same 15.23 as §15's shortfall, which is not a
  coincidence: with `n_target` held fixed the two statements are the same ratio
  read from either end.
* **Signed occupations**, with a stated reason. Untouched here.

**Scope (a).** Measured: the ceiling as a function of level, and the cost factor
required at the canonical level. **Not** claimed: that any level is realisable;
that a cost reaching the ceiling exists or is derivable; that signed occupations
are or are not justified; that any binding conjecture is true or false. A
ceiling clearing AME would have been **necessary, not sufficient** — it says
room exists, not that a derivable cost reaches it. Nothing here computes a
binding contribution.

## Addendum 17 — the two remaining escapes, and a correction to the first (2026-08-26)

§16 closed the level escape. Two remain — a different cost, and signed
occupations. Neither is chosen here; both are now quantified. Working the first
one properly shows the figure §15/§16 reported for it was wrong.

### The correction: `n_target` is not an independent input

It was reported that "a cost reaching AME needs `max(t) ≥ AME/n_target = 3.8677`
against the actual `0.2539` — a factor of **15.23×**, the same ratio read from
either end with `n_target` fixed."

**`n_target` cannot be held fixed.** It is not an input:

```
n_target = tr_M(β_D) = Σ_λ y_λ χ^λ = Σ_λ t_λ
```

The net-constraint target **is** the sum of the cost vector — verified to
`8e-17`. So the ceiling is

```
ceiling = max(t) · Σ(t)
```

which is **quadratic** in the cost, not linear. A uniform rescale `t → c·t`
scales it by `c²`, so it needs `c = √15.2307 = 3.903`, not 15.23. The 15.23 was
correct only for a variation that moves `max(t)` while pinning `Σ(t)`, and no
such variation exists. That "read from either end" remark was dressing an
algebraic identity as an insight, and the identity was the wrong one.

### What a cost change can and cannot buy

Since `ceiling = max(t)·Σ(t)`, redistributing the cost at **fixed total** is
maximised by putting everything on one block, giving `ceiling = (Σt)²`. That is
the best any reshaping can do:

| | value |
|---|---|
| actual ceiling | 0.146058 |
| **best possible shape** (all weight on one block) | **0.330823** — 2.265× better |
| AME | 2.224566 |
| **still short by** | **6.72×** |

So the constraint is **not on the cost's shape**. It is on `tr_M(β_D)` itself:
even a perfectly concentrated cost needs `Σ(t) ≥ √AME = 1.491` against the
actual `0.575` — the Markov trace of the deuteron braid would have to be
**2.59× larger**. That is a derived quantity, not a free parameter, so "pick a
different cost" is really "the deuteron braid's trace is too small", which is a
much harder thing to want.

**An independent check that this picture is right.** With `x ≥ 0` on the support
and `Σx = n_target`, `t·x` ranges over `[min(t)·n_target, max(t)·n_target]` =
`[0.0369647, 0.1460580]`, and a *minimising* LP should sit at the bottom. The
committed `support_restricted` optimum is `0.03696468028280623`. It matches
`min(t)·n_target` to `1e-12` — so the solver is doing exactly the convex
combination this analysis assumes, and the bound is not an artefact of how the
program was posed.

### Where the sign structure went

`χ^λ(β_D)` at `n = 6` takes both signs. Sorted by whether convention D gives the
block a nonzero weight:

| sector | `χ^λ(β_D)` |
|---|---|
| **support** (4 blocks) | `+1.560, +3.216, +1.674, +4.249` — **all positive** |
| **kernel** (7 blocks) | `−0.470, −1.972, −0.490, −3.497, −0.820, +2.156, −0.677` — **six negative** |

**Every negative character is in the kernel; the support has none.** The
convention-D row cap `ℓ(λ) ≤ 2` zeroes exactly the blocks carrying the sign
structure.

That is a sharper reading of §15 than "the kernel is unconstrained". The
full-space program could reach AME not merely because the kernel had no
positivity constraint, but because the kernel is *where the minus signs live*.
And it connects the three threads of this arc: the third row is where the weight
dies (§13), where one fibre cannot reach (§14 §3), and — now — where the
negative characters sit.

**Scope (a), and the limit is important.** This locates where the negative
characters are. It is **not** an argument that a program should occupy them, and
it does **not** justify signed occupations. A reason would have to say what a
negative occupation of a zero-weight block *means*, and nothing here supplies
one. Nor is it claimed that a cost with a larger trace exists or is derivable,
or that any binding conjecture is true or false. Nothing here computes a binding
contribution.

For the sibling fronts: this is a second, independent pointer at signed
structure alongside #5812's ²H/⁴He sign argument, and it says something more
specific than "signs are needed" — it says the framework's own characters
already supply them, in precisely the sector the canonical trace convention
cannot see.

## Addendum 18 — Addendum 17's last paragraph is wrong, and the negative blocks are nowhere (2026-08-26)

Bean `qou-6tcn`. Probe:
[`computations/meson/deuteron_negative_occupation_locality_probe.py`](../../computations/meson/deuteron_negative_occupation_locality_probe.py)
(8 assertions, all passing).

### The retraction

Addendum 17 closed with: *"the full-space program reached AME not merely
because the kernel is unconstrained but because the kernel is **where the minus
signs live**"*, and offered that to the sibling fronts as a second pointer at
signed structure. **The inference is causally wrong.** The cost vector is

$$ t_\lambda = y_\lambda\,\chi^\lambda(\beta_D), $$

and convention D's row cap sets $y_\lambda = 0$ for $\ell(\lambda) > 2$. So on
every kernel block $t_\lambda = 0$ **identically** — by construction, whatever
the character does. Measured on the committed witness: $\max|t|$ over the seven
kernel blocks is $0.0$, and $t\cdot x$ restricted to the kernel is $0.0$ in
every solution examined. A block that contributes nothing to the objective
cannot be the reason the objective got large. The character-sign *observation*
stands (assertions A6/A7 of the previous probe are untouched, and the retraction
is stamped into its docstring); the reading built on it does not.

This is the sixteenth correction in this arc, and the first where the error was
an inference rather than a number — the measurement that produced it was right,
and I attached a cause to it that its own data contradicts one field over.

### The mechanism, correctly

The net constraint is a plain sum over **all** blocks, and on the kernel
$G = 0$, so $Gx \ge 0$ imposes nothing there. A kernel deficit therefore buys
the support extra budget. Method 4 — the only encoding reaching AME, and it
reaches it by *imposing* AME as an equality:

| sector | $\sum x$ | $t\cdot x$ |
|---|---|---|
| support | $+12.3662$, all of it on the single block $(6)$ | $2.224566 = $ AME |
| kernel | $-11.7910$ | $0.0$ exactly |
| net | $+0.5752 = n_{\text{target}}$ | |

The zero-weight blocks are free in the objective ($t = 0$) *and* free in the
Frobenius cone ($G = 0$). They are pure ledger. That is the precise sense in
which the author's reading is right: this **is** a debt. What it is not is a
debt that is ever repaid — there is no term anywhere in the program that would
come due. It is an *unpriced* overdraft, and the only thing bounding it is the
artificial box $|x| \le M$.

### Which blocks go negative is not determined

The question has no invariant answer. Permuting the **variable order** — a
relabelling that leaves the polytope, the objective and the optimum untouched —
moves the negative set entirely:

| ordering | occupied support block | deficit $D$ | negative kernel blocks |
|---|---|---|---|
| identity | $(6)$ | $11.7910$ | $(4,1,1)\,(3,2,1)\,(3,1,1,1)\,(2,2,2)$ |
| perm 0 | $(5,1)$ | $8.1851$ | $(4,1,1)\,(3,2,1)\,(2,2,1,1)\,(2,1^4)$ |
| perm 1 | $(6)$ | $11.7910$ | $(3,1,1,1)\,(2,2,2)\,(2,2,1,1)\,(1^6)$ |
| perm 2 | $(3,3)$ | $34.0392$ | $(4,1,1)\,(2,2,2)\,(2,2,1,1)\,(1^6)$ |
| perm 3 | $(5,1)$ | $8.1851$ | $(3,2,1)\,(3,1,1,1)\,(2,2,2)\,(1^6)$ |

Five orderings, **five distinct negative sets**, one objective. The kernel is a
degenerate face: entries sit at $\pm M$ box bounds in near-cancelling
combinations, and only the net matters. Asking which partition carries the debt
is asking which vertex the simplex method stopped at. Every earlier attempt in
this session to characterise the negative set — by $(-1)^{n(\lambda)}$, by
$\ell(\lambda) \ge 3$, by content sign — failed for this reason, not for want
of the right invariant.

### What *is* determined: the floor on the debt

Only the support pays, so the cheapest route to a target $B$ concentrates
everything on the support block of largest cost, giving a floor

$$ D_{\min} \;=\; \frac{B}{\max_{\lambda \in \mathrm{supp}} t_\lambda} - n_{\text{target}}
   \;=\; \frac{2.224566}{0.253938} - 0.575172 \;=\; 8.185108, $$

attained on $(5,1)$, and matching the smallest $D$ in the table. That is
$14.23\times$ the entire net budget. If the debt reading is to attach to
anything, it attaches here: to reach AME through this program the zero-weight
sector must run a deficit of at least fourteen times the whole trace.

### What this asks of the framework

Stated as a requirement rather than a proposal: for "debt to vacuum" to be a
physical statement rather than a description of an LP degeneracy, something must
**price the kernel**. As posed it costs nothing to borrow there and nothing to
stay borrowed. Convention D sets that price to exactly zero by the row cap, so
the price cannot come from within convention D. The obvious candidate — a higher
Ocneanu level $z_r = q^r/[r]_q$, which gives $\ell(\lambda) \le r$ blocks a
nonzero $y_\lambda$ — was measured in Addendum 16 and makes the gap **worse**,
so that door is closed. Scope (a): this says the two mechanisms available in the
current program do not supply a price. It does not say none exists.

**Correction to the sibling-front note.** Addendum 17's closing offer to the
²H/⁴He sign front should not be taken up as written. What this arc supplies is
not "the framework's own characters already supply the signs" — the characters
that carry signs are exactly the ones the cost cannot see. What it supplies is a
sharper negative: a signed-occupation program reaches AME only by an unpriced
deficit whose location is not determined and whose magnitude is bounded below by
$14.23\,n_{\text{target}}$.

## Addendum 19 — the zero-weight sector is the Temperley–Lieb ideal; you don't price a radical (2026-08-26)

Bean `qou-6tcn`. Probe:
[`computations/meson/zero_weight_sector_is_temperley_lieb_probe.py`](../../computations/meson/zero_weight_sector_is_temperley_lieb_probe.py)
(8 assertions, all passing, 4 controls). Prompted by the author asking what
prices the zero-weight sector, and whether Frobenius duality is being used.

**Both questions have one answer, and it was already in the corpus.** This is
the third time in this arc that the answer was on disk before the measurement
started, and the corpus-grep found it in one pass.

### What the corpus already says

[`prop:markov-trace-frobenius-selection`](../../content/quantum-observable-universe/mass-theory/t-beta-markov-frobenius-collapse-proof.md)
part (iii), stated there **unconditionally**:

> the radical of $\langle x,y\rangle_\tau := \mathrm{tr}_M(xy)$ ... is exactly
> the Temperley–Lieb ideal $I_n = \ker(H_n(q) \twoheadrightarrow
> \mathrm{TL}_n(q))$, neither larger nor smaller. ... It is
> $(\mathrm{TL}_n(q), \mathrm{tr}_M)$, **not** $(H_n(R,q), \mathrm{tr}_M)$,
> that is a symmetric Frobenius algebra.

So the seven zero-weight blocks of Addendum 18 are not blocks the trace forgot
to charge for. They **span $I_6$**, and the Frobenius algebra the trace lives on
is the quotient $\mathrm{TL}_6(q)$, where the pairing is **non-degenerate**.

### Checked, not merely cited

If the convention-D support really is $\mathrm{TL}_6$ then its squared
dimensions must sum to the Catalan number — not merely to something less than
$6!$:

| | | |
|---|---:|---|
| $\sum_{\ell(\lambda)\le 2}(f^\lambda)^2$ | **132** | $= C_6 = \dim \mathrm{TL}_6$ |
| $\sum_{\lambda \vdash 6}(f^\lambda)^2$ | 720 | $= 6! = \dim H_6$ |
| $\sum_{\ell(\lambda)\ge 3}(f^\lambda)^2$ | 588 | $= \dim I_6$ |

Exactly, and at $n = 2,\dots,8$ (7/7), so it is not an $n=6$ coincidence. The
Gram is strictly positive on the support (min $0.0756$) and exactly zero off it,
and the two ways of naming the split — $\ell(\lambda) \le 2$ versus
$G_{\lambda\lambda} > 0$ — agree on all 11 blocks.

### What this closes, and what it costs me

**The signed-occupation escape is closed, and not by argument.** On the support
$G$ is strictly positive, so $Gx \ge 0$ **is** $x \ge 0$ there. The sector that
supplied the signs is $I_6$, which is not in the Frobenius algebra. There is
nothing left to sign. All three escapes opened in Addendum 15 are now closed.

**The support projection was never a modelling decision.** Addendum 15 and PR
[#5826](https://github.com/litlfred/qou/pull/5826) §1 defended it as one —
*"stated not smuggled"*. It is the **quotient map $H_6 \to \mathrm{TL}_6$**. So
the six encodings are infeasible in the actual Frobenius algebra, not in a
restricted model of it. The negative is stronger than it was reported to be.

**And Addendum 18's central word is wrong.** "Unpriced overdraft" presumes a
ledger with a missing entry. A radical is not an unpaid account; it is a
direction the pairing does not have. The measurements in 18 all stand — the
ledger identity, the vertex-dependence of the negative set, $D_{\min} =
8.185108$ — as facts about the LP **as posed on $H_6$**. What changes is that
posing it on $H_6$ was the defect. Seventeenth correction in this arc, and the
second consecutive one to my own framing of this same object.

### It also inverts the search

Two routes I was about to take are foreclosed by the same proposition:

- **"Widen the level so the kernel gets a weight"** is backwards. Part (ii)
  makes the row cap the **input** — the $\mathrm{SU}_q(2)$ fibre supplies no
  channel with $\ell(\lambda) \ge 3$ — and it is the row cap that *selects*
  $z = q^3/(q^2+1)$, i.e. convention D itself.
- **"Use a generic Ocneanu $z$, where the pairing is non-degenerate"** is true
  and useless. Part (i): non-degeneracy *"singles out nothing"*, since **every**
  weight vector with all $w_\lambda \ne 0$ induces a non-degenerate form. It
  cannot be a selection principle, which is exactly why the framework uses a
  prescribed **degeneracy** instead.

**Scope.** Parts (i) and (iii) are unconditional in the corpus and are what is
used here. Part (ii)'s antecedent — that the mass-channel trace *is* the
categorical trace of the fibre action — is **open** (bean `qou-n1dj`); nothing
here bears on it. Scope (a) throughout: this establishes *where the program
lives*, not what it yields, and computes no binding contribution.

### On the entanglement-cost reading

The author also asked whether a prior entanglement cost must be tracked, and
whether further entanglement costs something. Two findings, neither of them new:

1. **The framework already charges for the third channel, by removing it.**
   $\ell(\lambda) \ge 3$ needs a threefold antisymmetrisation, i.e.
   $\Lambda^3 V \ne 0$, i.e. $N \ge 3$; and `exteriorSquareDim N = 1 ↔ N = 2`
   pins $N = 2$, so $\Lambda^3 V = 0$. The cost of that sector is not high, it
   is **infinite** — the states are absent, which is the same fact as $I_6$
   being quotiented out. There is no prior ledger to carry.
2. **The direct test exists and is a light-end refutation.** The owner
   conjecture $B = E_0 \cdot S_{\mathrm{vN}}$ was tested in
   [`binding_von_neumann_entropy_probe.py`](../../computations/probes/binding_von_neumann_entropy_probe.py)
   with a state-dependent Born–Plancherel block weight. Binding **destroys**
   block entanglement rather than generating it — $\Delta S < 0$ for ²H
   ($-0.0135$) and ³H ($-0.0077$) — and $E_0\,|\Delta S|$ misses $B_{\rm AME}$
   by $39\times$ (²H), $263\times$ (³H), $1.3\times10^{5}$ (³He), while
   $E_0 S_{\rm bound}$ *overshoots* by 35–84 %. Scope (a): that refutes **one
   prescription**, not entanglement cost as an ingredient. Note the witness is
   muon-pinned ($q_0 = 1.10997859555\ldots$), pre-dating the 2026-08-07 proton
   directive; the sign of $\Delta S$ will not turn on an 11.5 ppb re-pin, but
   the magnitudes should be re-read after one.

A name collision worth recording:
[`q-beta-gamma-gamma-canonical-derivation.md`](../../content/quantum-observable-universe/stochastic-mechanics/q-beta-gamma-gamma-canonical-derivation.md)
is the $\mathfrak{Q}_\beta$ $c_k$-ladder derivation and **does not treat
two-photon production**. Nothing in the corpus does; a γγ-production
entanglement ledger would be new work, and would sit outside this LP entirely —
an entropy is not a trace, so it is not a linear functional on the algebra and
cannot appear as a cost vector.

## Addendum 20 — nothing destroys entanglement: the sign is forced, so the label was wrong (2026-08-26)

Bean `qou-6tcn`. Probe:
[`computations/meson/binding_cut_entropy_sign_is_forced_probe.py`](../../computations/meson/binding_cut_entropy_sign_is_forced_probe.py)
(8 assertions, all passing, 4 controls). Raised by the author against the
Addendum 19 §2 result I relayed — that binding "destroys" block entanglement.
**The objection is right, and it is stronger than a complaint about a sign.**

### Two reasons that number cannot be an entanglement entropy

1. **Unitarity.** For a closed process in which the same particles come back —
   virtual production and annihilation being the clean case — the global state
   stays pure, so its von Neumann entropy is identically $0$ and **cannot
   change**. Anything that moves under such a process is not the global entropy.
2. **Positivity across a cut.** Entanglement entropy is defined only once a
   bipartition is named, and across any cut a product state has $S_A = 0$ while
   every state has $S_A \ge 0$. Free nucleons are a product across the
   proton|neutron cut, so $\Delta S = S_{\rm bound} - 0 \ge 0$ **identically**.
   It is a theorem, not a measurement.

### What the committed probe actually computes

`block_entropy` is $-\sum_\lambda p_\lambda \ln p_\lambda$ with
$p_\lambda \propto W_\lambda \lVert \rho_\lambda(\beta)\rVert_F^2$. There is
**no bipartition, no partial trace and no reduced density matrix** anywhere in
it. It is the Shannon entropy of a classical distribution over the Wedderburn
blocks of the *whole* algebra — a measure of how spread a braid's character is
across irreps. A real quantity, and its arithmetic is not in dispute; it is
simply not an entanglement entropy, and *"von Neumann entanglement entropy"* is
the wrong label for it. Its $\Delta S < 0$ is the proof, since no bipartite
measure can do that.

**I relayed that label without checking it.** Eighteenth correction in this arc,
and the first prompted by the author rather than found in a re-measurement.

### The right cut is already in the corpus

The natural bipartition is proton strands | neutron strands, i.e.
$H_3 \otimes H_3 \subset H_6$. Restriction along it **is** Frobenius
reciprocity — the same duality Addendum 19 was about — and its multiplicities
are Littlewood–Richardson, already carried per $\lambda$ as
`lr_breakdown_per_lambda` in
[`sublemma-2-1-deuteron-branching.witness.json`](../../computations/sublemma-2-1-deuteron-branching.witness.json).
That witness also records `max_relative_diff_no_interface = 1.98e-70`: the
**disjoint** character matches the LR prediction to seventy digits, so the free
state is exactly the induced product across this cut — which is what makes its
cut entropy zero and lets the sign theorem bite.

Measured in exact integer arithmetic, no $q$ and no float64, with
$p^\lambda_{\mu\nu} = c^\lambda_{\mu\nu} f^\mu f^\nu / f^\lambda$:

| $\lambda$ | $f^\lambda$ | cut terms | $S_{\rm cut}$ (nats) |
|---|---:|---:|---:|
| $(6)$ | 1 | 1 | **0.000000** |
| $(5,1)$ | 5 | 3 | 1.054920 |
| $(4,2)$ | 9 | 4 | 1.273028 |
| $(4,1,1)$ | 10 | 5 | **1.470808** |
| $(3,3)$ | 5 | 2 | 0.500402 |
| $(3,2,1)$ | 16 | 5 | 1.386294 |
| $(3,1,1,1)$ | 10 | 5 | **1.470808** |
| $(2,2,2)$ | 5 | 2 | 0.500402 |
| $(2,2,1,1)$ | 9 | 4 | 1.273028 |
| $(2,1^4)$ | 5 | 3 | 1.054920 |
| $(1^6)$ | 1 | 1 | **0.000000** |

Non-negative on all eleven; exactly zero on exactly the two one-dimensional
blocks — the ones restricting to a single $(\mu,\nu)$, i.e. genuinely product
across the cut; strictly positive on the other nine; and invariant under
conjugation $\lambda \mapsto \lambda'$ on all eleven. The dimension control
$\sum_{\mu\nu} c^\lambda_{\mu\nu} f^\mu f^\nu = f^\lambda$ passes 11/11, so the
LR weights really are the restriction.

### What is NOT claimed, and one trap to name explicitly

Nothing here says $E_0 \cdot S_{\rm cut}$ is the binding energy. The value AME
would require, $S = B_{\rm AME}/E_0 = 2.224566/4.185981 = 0.5314$, **lies inside
the measured range $[0,\,1.4708]$** — and that is a *genericity observation, not
evidence*. A weighting over eleven blocks spanning that interval can be made to
hit almost anything in it, which is the same trap the `S_leak` offset window
records under §"Defined residual ≠ derived decomposition". No weighting is
chosen here and no binding contribution is computed.

Nor is entanglement cost excluded as an ingredient. The earlier probe refutes
**one prescription**; this one refutes that prescription's **label**. Neither
bears on whether a correctly-defined cut entropy plays a role — and the object
that would have to be tested now exists, is parameter-free, and is exact.

## Addendum 21 — every derived weighting overshoots AME by ~2×, robustly (2026-08-26)

Bean `qou-6tcn`. Probe:
[`computations/meson/binding_cut_entropy_derived_weightings_probe.py`](../../computations/meson/binding_cut_entropy_derived_weightings_probe.py)
(9 assertions, all passing, 4 controls). Addendum 20 built the cut entropy and
deliberately chose no weighting, since choosing one to hit AME would be a fit.
The author asked for the derived weighting to be worked. **Every candidate with
independent provenance was computed once. None reaches AME.**

### The four candidates

Under convention D only the four two-row blocks exist. The cut is closed on
them without any truncation being imposed: $c^\lambda_{\mu\nu} \ne 0$ requires
$\mu,\nu \subseteq \lambda$, so a two-row $\lambda$ restricts entirely inside
$\mathrm{TL}_3 \otimes \mathrm{TL}_3$.

The reduced proton-side state is block-diagonal in the $\mu$-isotypic
decomposition with eigenvalue $A_\mu = \sum_\lambda p_\lambda a^\lambda_\mu$ of
multiplicity $f^\mu$, where $a^\lambda_\mu = \sum_\nu c^\lambda_{\mu\nu}
f^\nu/f^\lambda$; so $S_{\rm vN} = -\sum_\mu f^\mu A_\mu \ln A_\mu$. *(Addendum
20 reported the **sector** entropy $-\sum_{\mu\nu} P \ln P$, a different and
larger quantity. Both are non-negative and both vanish on a product, so its sign
theorem is unaffected — but this one is the von Neumann entropy of the reduced
density matrix and is the right thing to set against an energy.)*

At the proton pin, $E_0 = m_e/(q_0(q_0-1)) = 4.185981$ MeV and
$B_{\rm AME}(^2\mathrm{H}) = 2.224566$, so AME needs $S_{\rm vN} = 0.531432$:

| weighting | provenance | $S_{\rm vN}$ | $E_0 S_{\rm vN}$ | vs $B$ |
|---|---|---:|---:|---:|
| **W1** $p = y_\lambda f^\lambda$ | Markov/Plancherel, **exact** closed form $y_{(n-k,k)} = [n{-}2k{+}1]_q/[2]_q^n$ | 1.035916 | 4.33633 | **1.949×** |
| **W2** $p = t_\lambda/\mathrm{tr}_M(\beta_D)$ | Born; the deuteron braid's own distribution | 0.896974 | 3.75471 | **1.688×** |
| W3 $p \sim (f^\lambda)^2$ | classical Plancherel — *control* | 1.096575 | 4.59024 | 2.063× |
| W4 uniform | structure-free — *control* | 1.014392 | 4.24623 | 1.909× |

**All four overshoot, by 1.69× to 2.06×.** W1's exact closed form reproduces the
committed Frobenius Gram diagonal to $4\times10^{-9}$ — a control that it really
is the framework's own weighting and not a reconstruction of mine.

### The overshoot is robust, not a knob — and this sharpens Addendum 20

Entropy is concave, so its minimum over weightings sits at a vertex:

| vertex | $S_{\rm vN}$ | vs $B$ |
|---|---:|---:|
| $\delta_{(6)}$ | **0.000000** | 0.000× |
| $\delta_{(5,1)}$ | 0.950271 | 1.788× |
| $\delta_{(4,2)}$ | 1.098612 | 2.067× |
| $\delta_{(3,3)}$ | 1.054920 | 1.985× |

Every **non-trivial** block lands in 1.79×–2.07×. The only low value anywhere in
the simplex is the trivial block, which by definition carries no cut structure —
it restricts to a single $(\mu,\nu)$, i.e. it *is* a product. Reaching AME from
W1 requires moving **69.3 % of the total weight onto $(6)$**, taking $p_{(6)}$
from 0.1153 to 0.7282 — a **6.31×** concentration on the one block that says
nothing.

**Addendum 20's caveat was right in principle and too weak in fact.** It warned
that a weighting spanning $[0, 1.4708]$ could hit almost anything in the
interval, so being in range was genericity rather than evidence. True — but the
*derived* candidates do not span it. They cluster a factor of ~2 above the
target, and the escape route is the contentless block. That makes this a
**robust negative rather than a free parameter**, which is a more useful outcome
than either a hit or a fit.

### The near-2 is recorded, asserted false, and not pursued

W1 gives $1.9493\times$, which is $2.5\,\%$ from exactly 2. In a framework
quoting accuracy in ppb, $2.5\,\%$ is not agreement, and "close to 2" is
precisely what the anti-numerology discipline exists to stop. It is asserted as
**not** equal to 2 (`markov_ratio_is_not_two`) so that the near-miss cannot
later be read as a hit.

### Scope

**(a).** This does **not** refute an entanglement-cost contribution to binding.
An overshoot of ~2× with the right sign and the right order of magnitude is not
an exclusion, and a term entering with a coefficient, or alongside others, is
untouched by it. What is established is narrower and firmer: **$E_0 S_{\rm cut}$
alone, under every weighting the framework already fixes, is about twice too
large at the deuteron.**

And it is **one isotope**. LR branching data exists only for $^2$H, so nothing
here speaks to $^3$H, $^4$He or beyond — and a single point could not have
distinguished a derivation from a coincidence even had it hit. Extending it
needs the $n = 9$ and $n = 12$ branching, which is the concrete next measurement
if this line is pursued.

## Addendum 22 — the cut entropy is CONSTANT in A: scope-(b), and Lean-proved (2026-08-26)

Bean `qou-6tcn`. Probe:
[`computations/meson/cut_entropy_is_A_independent_probe.py`](../../computations/meson/cut_entropy_is_A_independent_probe.py)
(8 assertions, 4 controls). Lean:
[`QOU/MassTheory/MarkovMarginalConstant.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/MarkovMarginalConstant.lean)
(6 declarations, sorry-free, `lean`-direct exit 0). Extension requested by the
author. **The result retires the line.**

### Measured

One nucleon against the rest, cut $H_3 \otimes H_{3(A-1)} \subset H_{3A}$,
Markov/Plancherel weighting:

| iso | A | n | $S_{\rm vN}$ | $E_0 S_{\rm vN}$ | $B_{\rm AME}$ | ratio |
|---|---:|---:|---:|---:|---:|---:|
| ²H | 2 | 6 | 1.0359164 | 4.33633 | 2.22457 | 1.9493× |
| ³H | 3 | 9 | 1.0359164 | 4.33633 | 8.48180 | 0.5113× |
| ³He | 3 | 9 | 1.0359164 | 4.33633 | 7.71804 | 0.5618× |
| ⁴He | 4 | 12 | 1.0359164 | 4.33633 | 28.29566 | 0.1533× |
| ⁶Li | 6 | 18 | 1.0359164 | 4.33633 | 31.99399 | 0.1355× |
| ⁷Li | 7 | 21 | 1.0359164 | 4.33633 | 39.24508 | 0.1105× |

$S_{\rm vN}$ is **the same number at every A**, to better than $10^{-50}$ out to
$n = 24$. $B_{\rm AME}$ is extensive and rises $17.6\times$. **A constant cannot
track an extensive quantity**, the ratio drifts by $17.6\times$, and Addendum
21's near-2 at the deuteron was a coincidence of its being the smallest binding.

### Why — a structural argument, not a fit

The measured marginal is exactly $A_{(3)} = [4]_q/[2]_q^3$ and $A_{(2,1)} =
[2]_q/[2]_q^3$, which are $y_\mu$ at **$n = 3$**. The one-nucleon marginal of
the $n$-strand Markov measure **is** the three-strand Markov measure, for every
$n$ — which is the Markov property itself. `prop:markov-trace-frobenius-selection`
defines a Markov trace as *"a **compatible** family of linear functionals"*, and
compatibility says precisely that restricting $\tau_n$ to $H_k$ gives $\tau_k$.
Any functional of an $n$-independent marginal is $n$-independent.

**This is scope (b)** — a structural exclusion with a named invariant, not the
usual scope-(a) negative. The invariant is Markov compatibility: definitional,
not fitted. It forbids *any* closure in which a **fixed-width** cut entropy of
the Markov measure carries an extensive quantity. It does **not** exclude
entanglement cost as an ingredient of binding, and a cut whose width **grows**
with $A$ is untouched by the argument.

### Lean

`MarkovMarginalConstant.lean` proves the invariant rather than asserting it. The
content is that a **one-step** hypothesis forces an **any-depth** conclusion:

- `margDown_eq_of_step` — `∀ n d, margDown restrict w n d = w n`, by induction
  on depth. The hypothesis constrains one step; the conclusion is about all.
- `marginal_functional_const` — hence any `F` of the marginal is
  depth-independent (the entropy is a special case; the proof does not care).
- `not_forall_eq_of_const_of_two_values` — a constant cannot agree pointwise
  with a target taking two values. Stated as a refutation of agreement rather
  than `∃ c, f c ≠ g c`, so the proof is constructive.
- `marginal_functional_ne_two_valued` — the exclusion assembled.
- **Non-vacuity, both guards** (AGENTS.md §3b-tax): `step_satisfiable` exhibits
  an inhabitant, and `margDown_ne_without_step` shows the hypothesis is
  **load-bearing** — drop it and the conclusion is false, so the main theorem is
  not a tautology about `margDown`.

Verification: `lean`-direct **exit 0**; `#print axioms` on all six — five
*"does not depend on any axioms"*, one on `propext` alone. **No `sorryAx`.**
No `ℝ`, no typeclass, and **no imports at all** (AGENTS.md §7c: the argument is
pure rewriting). `autoImplicit` is off, which is not decoration — with it on and
no imports, `ℕ` auto-bound as a fresh type variable and every numeral failed to
elaborate. That is exactly how the file first failed, twice.

### Formalize-first, missed — and recorded as such

The structural argument above predicts the entire table and needed **no
compute**. I ran the extension sweep first and found the reason afterwards. That
is precisely the failure mode AGENTS.md §"Formalize-first probe discipline"
exists to prevent: state the invariant, let it narrow the probe. Recorded so the
next agent reads the invariant before spending the sweep.

### A control that earned its keep

The probe carries its own Littlewood–Richardson implementation, so it is only as
good as its controls. It reproduces the committed `lr_breakdown_per_lambda`
exactly (35 coefficients, 0 mismatches, 0 invented terms), and the dimension
identity $\sum c^\lambda_{\mu\nu} f^\mu f^\nu = f^\lambda$ holds at every $n$.

**The second control caught a real bug**: a hard-coded row padding of 10
silently returned wrong coefficients for partitions with more than 10 rows — 2
failures out of 77 at $n = 12$ — which the two-row blocks this probe actually
uses would never have revealed.

## Addendum 23 — the two fronts Addendum 22 left: one closes, one does not (2026-08-26)

Bean `qou-6tcn`. Probe:
[`computations/meson/two_remaining_fronts_probe.py`](../../computations/meson/two_remaining_fronts_probe.py)
(9 assertions, 5 controls). Addendum 22 named exactly two things its theorem did
not touch. Both worked, at the author's request, and they land differently.

### Front 1 — a cut whose width grows with A. **Open, and genuinely different.**

The Markov property that made the fixed-width entropy constant hands over the
growing case for free: the marginal on the first $k$ strands *is* the $k$-strand
Markov measure, so $S(k) = -\sum_{\mu} f^\mu y^{(k)}_\mu \ln y^{(k)}_\mu$ — no
Littlewood–Richardson needed. Measured, this is a **volume law**:

| $k$ | 24 | 96 | 384 | 768 |
|---|---:|---:|---:|---:|
| $S(k)/k$ | 0.60928 | 0.66315 | 0.68108 | 0.68439 |

approaching $\ln[2]_q = 0.6985808$ from below, i.e. $S(k) = k\ln[2]_q - c +
o(1)$: an entropy density of exactly one $\ln[2]_q$ per strand — the log of the
fundamental's quantum dimension, which is what a strand carries. **So unlike the
fixed-width case this quantity is extensive, and Addendum 22's theorem does not
reach it.** The escape is real.

**It does not match, and why it cannot be made to is the point.** For the
balanced cut $k = \lfloor 3A/2 \rfloor$:

| iso | A | $E_0 S(k)$ | $B_{\rm AME}$ | ratio | $E_0S/A$ | $B/A$ |
|---|---:|---:|---:|---:|---:|---:|
| ²H | 2 | 4.3363 | 2.2246 | 1.9493× | 2.1682 | 1.1123 |
| ³H | 3 | 6.8866 | 8.4818 | 0.8119× | 2.2955 | 2.8273 |
| ⁴He | 4 | 11.9036 | 28.2957 | 0.4207× | 2.9759 | 7.0739 |
| ⁶Li | 6 | 19.7479 | 31.9940 | 0.6172× | 3.2913 | 5.3323 |
| ¹²C | 12 | 44.4404 | 92.1617 | 0.4822× | 3.7034 | 7.6801 |
| ¹⁶O | 16 | 61.2108 | 127.6193 | 0.4796× | 3.8257 | 7.9762 |

The ratio is not constant — $4.63\times$ across these, against $17.64\times$ for
the fixed cut — and settles near $0.48$, an undershoot of about $2.1\times$.
Asymptotically a cut growing at $w$ strands per nucleon gives $E_0 w \ln[2]_q$
per nucleon, so the balanced $w = 1.5$ yields **4.386 MeV/nucleon** against an
empirical approach to $\sim 8$.

**$w$ is a free parameter, and that is the whole problem.** Matching fixes
$w \approx 2.9$, which nothing derives — and at $w = 3$, the whole nucleon, the
cut is the entire system and the entropy is identically zero. So the front is
open in that the *object* is extensive, and closed in that nothing in the
framework selects the cut. Choosing $w$ to match is a fit and is not done.

### Front 2 — can $\mathrm{tr}_M(\beta_D)$ be $2.59\times$ larger? **Closed, scope (b).**

Addendum 21 established that even a perfectly concentrated cost needs
$\mathrm{tr}_M(\beta_D) \ge \sqrt{B_{\rm AME}} = 1.491498$ against the measured
$0.575172$. **The corpus already proves the bound that settles it.**
`atom-branch-convexity-bound` shows the atom is a *convex* combination of its
branch closures ($\sum_b |w_b| = 1$, every $w_b > 0$), so
$\mathrm{tr}_M(\text{atom}) = \sum_b w_b\,\mathrm{tr}_M(\beta_b) \le \max_b
\mathrm{tr}_M(\beta_b)$. Measured over all 32 deuteron branches:

| | |
|---|---:|
| $\min_b \mathrm{tr}_M$ | 0.291552 |
| $\max_b \mathrm{tr}_M$ | **1.018275** |
| required | 1.491498 |
| max / required | **0.68272** |

**No reweighting of the branches reaches it.** And the ceiling is quadratic, so
even *at* the convex maximum the best attainable objective is
$(\max_b \mathrm{tr}_M)^2 = 1.036884$ against $B_{\rm AME} = 2.224566$ — still
**2.15× short**.

That is **scope (b)**: the invariant is the convexity of the branch
decomposition, proved in the corpus and not fitted. It excludes reaching AME by
any redistribution over the branches of **this** braid word. It does **not**
exclude a different word, and says nothing about whether one exists or is
derivable.

### Controls, and a precision note

The branch computation's load-bearing control is that the weighted branch
average reproduces the committed $\mathrm{tr}_M(\text{atom})$ — without it,
$\max_b$ would be a bound on some other object. It agrees to $\sim 10^{-9}$,
not exactly, because `binding_k_solver.per_block_evaluation` is float64; the
verdict turns on a 47 % gap, far above that resolution. A second control asserts
the branch traces genuinely spread *above* the atom's own value ($\max_b /
\mathrm{tr}_M(\text{atom}) = 1.77$), so the bound is not trivially satisfied.
Front 1 is exact mpmath from the closed form throughout — no LR, no float64 —
and its $S(3)$ reproduces Addendum 22's fixed-width number as a cross-tie.

### Where this leaves the arc

Of everything opened since Addendum 15, **one thing remains open**: a
growing-width cut, whose object is extensive but whose width the framework does
not fix. Everything else — the level escape, the cost escape, signed
occupations, the fixed-width entropy, and now the trace magnitude for this word
— is closed, the last two by proved invariants.

## Addendum 24 — what a satellite is, and why the colour-tube refinement cannot carry the magnitude (2026-08-26)

Bean `qou-6tcn`. Probe:
[`colour_tube_refinement_is_convexity_bounded_probe.py`](../../computations/meson/colour_tube_refinement_is_convexity_bounded_probe.py)
(7 assertions, 4 controls). Lean:
[`QOU/MassTheory/BranchConvexityBound.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/BranchConvexityBound.lean)
(5 declarations, sorry-free). Prompted by the author asking what a satellite
torus is, how to attack `conj:jsj-decomposition-linearity`, and where the
missing binding term lives.

### What a satellite knot is

Take a knot $P$ drawn inside an unknotted **solid torus** $V$ — the *pattern*.
Take any knot $C$ — the *companion*. Now embed $V$ into $S^3$ so that its core
follows $C$, and carry $P$ along with it. The image is the **satellite** $K$
with pattern $P$ and companion $C$.

```
   pattern P inside the solid torus V        embed V along the companion C
   ┌───────────────────────────┐                      ___
   │   ╭─────╮   ╭─────╮       │                    /     \        the boundary
   │  ─┤  P  ├───┤     ├─      │      ───────►     |   ()  |  ◄─── ∂V becomes an
   │   ╰─────╯   ╰─────╯       │                    \ ___ /        ESSENTIAL TORUS
   └───────────────────────────┘                      C            in S³ ∖ K
```

The defining fact, and the one that matters here: **$S^3 \setminus K$ contains
an incompressible ("essential") torus**, namely $\partial V$. That is not an
extra property — *satellite* and *the complement contains an essential torus*
are the same condition. It is precisely the case the JSJ decomposition cuts
along, and precisely the case Stage 3's `Geom` trichotomy (hyperbolic / torus /
unknot) never assigns a value to.

Two familiar special cases: if $P$ is a $(p,q)$ curve on $\partial V$ you get a
**cable** knot; if $P$ is the Whitehead link's clasp you get a **Whitehead
double**. Both are satellites, both carry an essential torus, and neither is
hyperbolic or a torus knot.

**Contrast with what the atom carriers actually are.** #5817 measured all 40
branch closures **composite** — connected sums — whose complements contain
essential **spheres**, not tori. A connected sum is not a satellite. So as
currently constructed the atom complement has no essential torus, which is why
`conj:jsj-decomposition-linearity` is presently *true and empty*:
$\mathrm{Vol}_p = \mathrm{Vol}_n = 0$.

### Attack options on `conj:jsj-decomposition-linearity`

The conjecture reads $\mathrm{Vol}(\mathcal{K}(Z,N)) = Z\,\mathrm{Vol}_p +
N\,\mathrm{Vol}_n$, and its own text is explicit that *"additivity of hyperbolic
volume over the pieces … is a theorem of 3-manifold topology (Thurston); the
conjectural content therefore lies entirely in the decomposition hypothesis."*
So there is nothing to prove on the additivity side, and exactly three moves:

1. **Establish the hypothesis** — show the inter-nucleon braids form essential
   tori. Currently measured **false** for the production construction (40/40
   composite ⇒ essential spheres). Attacking this means changing the
   construction, not the proof.
2. **Change the inter-nucleon arc to a satellite move** — replace the single
   Hecke generator at each arc with a pattern-in-a-solid-torus threaded along
   the neighbouring nucleon. This is the "one move" that makes `def:atom-knot`'s
   *closed braid* requirement and the essential-torus requirement land together.
3. **Refute it as stated** — show no such decomposition exists, which would send
   the binding term elsewhere entirely. Nothing in this arc bears on this.

Route 2 is the only one this arc's results leave open, and §"the corollary"
below is why.

### The corollary: the colour-tube refinement is convexity-bounded

`conj:inter-nucleon-channel-color-tube` is the corpus's own candidate for the
inter-nucleon term — $A-1$ arcs, genuinely extensive — refining
$\mathrm{pp}\mapsto\sigma$, $\mathrm{nn}\mapsto\sigma^{-1}$,
$\mathrm{pn}\mapsto\sigma_{\rm avg}$ into
$\sigma^{(F_1,F_2)} = \sum W_{c_1c_2}\,\sigma^{\epsilon}$.

**That block's own statement fixes $W \in \mathbb{Q}_{\ge 0}$ normalised to
$\sum W = 1$**, with $\epsilon = 0 \mapsto \sigma_{\rm avg}$, itself
$(\tfrac12,\tfrac12)$. So every term lies in the convex hull of
$\{\sigma,\sigma^{-1}\}$ at each arc: the refined atom is a **reweighting of the
same 32 branches**, not a new element. `QOU.MassTheory.convex_comb_le_bound`
then applies verbatim:

$$ \text{refined } \mathrm{tr}_M(\beta_D) \;\le\; \max_b \mathrm{tr}_M(\beta_b)
   \;=\; 1.018275 \;<\; 1.491498 \;=\; \sqrt{B_{\rm AME}}. $$

**The colour-tube refinement cannot supply the deuteron binding magnitude.** It
is bounded by the same number as the production assignment. This does **not**
say the refinement is wrong — the p/n asymmetry and chirality sign structure it
exists for are untouched. It bounds the magnitude only.

**The premise is auditable, not asserted.** Assertion A6 greps the block for its
own non-negativity and normalisation sentences, so a reader checks the reading
against the source rather than against this addendum; if that block is ever
edited to drop the normalisation, A6 fails and the corollary voids — which is
the correct behaviour.

### And the Lean says exactly what escapes

`larger_index_set_escapes_the_bound` (sorry-free) exhibits the one way out: the
bound is *relative to the branch set it is taken over*, and a larger index set
can exceed it. A satellite replaces each strand by several, so its branches are
words in a **bigger algebra** — not a reweighting but a different index set,
outside the theorem's hypotheses. That asymmetry is the whole content of the
file, and it is why front 2 closes the reweighting route while leaving the
satellite route open. `bound_fails_without_nonneg` is the companion guard:
weights $(2,-1)$ still sum to 1 and reach 2 past a max of 1, so convexity is
doing the work — which is exactly what `atom-branch-convexity-bound` had to
*measure* (`every w_b > 0`) rather than assume.

### A library gap, stated rather than filled

The author asked whether the physics literature has something like mesonic
toroidal forces. I reported that **our ingested library has nothing** on
satellites, toroidal knots or cabling, on the strength of a `grep` over
`library/INDEX.md` returning zero.

> **🛑 That was wrong — see Addendum 27.** `INDEX.md` is tier 1 of a
> **three**-tier path-5 checklist, and its briefs are extractive, so a topic
> present in a body but absent from its abstract is invisible there. The
> pre-existing library already held 12 documents mentioning *satellite*, 19
> *cabling* and 13 *JSJ*. No answer was guessed, which was right; the gap was
> real but far smaller than reported. If that
literature is wanted it needs ingesting first; that is a concrete, cheap next
step and it is not done in this branch.

## Addendum 25 — the ingest is blocked, but the physics question has an answer (2026-08-26)

Bean `qou-6tcn`. Ledger:
[`docs/coordination/satellite-cabling-source-ledger.md`](../coordination/satellite-cabling-source-ledger.md).

Addendum 24 recorded that the library holds nothing on satellites or cabling and
declined to guess at the author's question about mesonic toroidal forces. Asked
to ingest that literature. **The ingest cannot be done in this sandbox; the
question can now be answered anyway, from verified links rather than from text.**

### Every paper host is blocked; one channel is not

Walking the [`local/sandbox-egress`](../../.claude/skills/local/sandbox-egress.md)
route table rather than stopping at the first 403: `export.arxiv.org` gives
`CONNECT tunnel failed, response 403`; `arxiv.org`, `api.openalex.org`,
`api.semanticscholar.org` and `api.crossref.org` all give `000`. Every
`paper-search-mcp` backend returns `[]` for the same reason — they ride the same
proxy. `raw.githubusercontent.com` gives `301` (open), as the route table says,
but arXiv PDFs do not live there.

**WebSearch is out-of-band and works** — exactly as the route table records — so
verified IDs and titles are obtainable even though the PDFs are not.

### So this is a citation ledger, not an ingest

The distinction matters and the ledger states it at the top. **The ledger's
claim that path 5 "still returns zero" was itself wrong** for the reason in
Addendum 27 — it was measured at tier 1 only. Both the ledger and the paragraph
above are corrected in place; the papers were subsequently ingested, and none of
them had been read at the time the ledger was written.

### The physics question: yes, and it is the Faddeev–Skyrme literature

The Hopfion literature *is* "mesonic toroidal forces" — knotted solitons whose
topology is the Hopf map $S^3 \to S^2$, carrying a **twisted toroidal**
structure, in an effective low-energy $SU(2)$ model. Three points from the search
summaries, flagged **unread**: Faddeev and Niemi conjectured the toroidal twisted
structure and numerics confirmed it up to Hopf charge sixteen **including torus
knots**; in low-energy QCD these appear as knots of the **gluon** field proposed
to describe **glueballs**; and via the **Cho–Faddeev–Niemi decomposition** the
model is conjectured to be the low-energy effective theory of $SU(2)$
Yang–Mills.

**The third point needs the most care.** QOU's fibre is pinned at rank two
(`exteriorSquareDim N = 1 ↔ N = 2`), so an $SU(2)$ effective description is a
*suggestive shape match* — precisely the class of observation the
anti-numerology discipline exists to slow down. Nothing is wired, cited in a
content block, or used in any derivation.

### And a better route than the `H₁₂` compute

The cabling group ([0807.2679](https://arxiv.org/abs/0807.2679) and the Kalfagianni–Tran
sequence) gives the colored Jones of a cable in terms of the companion's. That
would replace the one-isotope `H₁₂` measurement with a **closed form** — the
formalize-first route, generalising past the deuteron in one step rather than
one isotope at a time. Recorded as the preferred next move if this front is
continued.

## Addendum 26 — the satellite escapes, measured: 4.99× over (2026-08-26)

Bean `qou-6tcn`. Probe:
[`satellite_cable_escapes_the_bound_probe.py`](../../computations/meson/satellite_cable_escapes_the_bound_probe.py)
(9 assertions, 6 controls). The test Addendum 24 said needed doing and did not
do. **It is the first positive result in this arc**, and it is exactly what
`larger_index_set_escapes_the_bound` predicted before the number existed.

### What was tested

The **2-parallel cable** of the deuteron braid: each strand doubled, each
$\sigma_i \mapsto s_{2i}s_{2i-1}s_{2i+1}s_{2i}$ in $B_{12}$. Its closure is the
2-parallel of the original closure — a **genuine satellite** (pattern = the
2-parallel curve in the solid torus, companion = the original knot), so the
geometrically-motivated move rather than an arbitrary longer word.

| | value | vs required |
|---|---:|---:|
| uncabled, $\max_b$ (Addendum 23) | 1.018275 | 0.683× |
| **2-cable, $\max_b$** | **7.448220** | **4.994×** |
| **2-cable, atom's own convex weights** | **1.657034** | **1.111×** |
| required $\sqrt{B_{\rm AME}}$ | 1.491498 | 1 |

**The trace magnitude is no longer the binding constraint on the satellite
route.** And it is not only the max: the atom's *own* convex-weighted 2-cable
clears the requirement too — though by **1.11×**, a thin margin.

### Why this is the predicted escape, not a surprise

`convex_comb_le_bound` bounds a reweighting of a **fixed** branch set;
`larger_index_set_escapes_the_bound` shows a larger index set can exceed it. A
cable puts the branches in $H_{12}$ rather than $H_6$ — a different index set,
outside the theorem's hypotheses. The Lean identified this class as the escape;
this measures that it actually escapes, and by how much.

**A longer word generally has a larger trace, so "the cable is bigger" is not by
itself interesting.** What is: the *geometrically-motivated* move crosses the
specific threshold, by 5× rather than marginally; and the threshold is a
**necessary** condition derived generically — a concentrated cost needs
$\mathrm{tr}_M \ge \sqrt{B_{\rm AME}}$ at any $n$ — so the cross-algebra
comparison is licit, which control C1 below is what licenses.

### Controls — a positive needs more scrutiny than a negative

Six, and the load-bearing one is the third:

1. the same quantity **without** cabling falls short (0.683×), so A1 is a change
   rather than a restatement;
2. this code path reproduces Addendum 23's `1.018275083` exactly, so the cable
   number comes off a validated route;
3. **M1 normalisation $\sum_\lambda y_\lambda f^\lambda = 1$ holds at $n = 12$
   *and* $n = 6$**, both exactly — this is what makes $\mathrm{tr}_M$ values
   comparable across the two algebras and the A1 comparison legitimate at all;
4. $\mathrm{tr}_M(1) = 1$ at $n = 12$;
5. the convex average still reproduces the committed atom trace, so the branch
   weights carried into the cable are the right ones;
6. the cabling map stays within $H_{12}$'s generator range.

### What this does **not** show

* **Binding is not reproduced.** The cost vector, support, Gram and the whole LP
  change at $n = 12$ and none of that is redone. Exceeding a **necessary**
  condition is not sufficiency, and nothing here computes a binding
  contribution.
* **The pattern is a choice.** 2-parallel with blackboard framing is one
  satellite among infinitely many; nothing derives it.
* **`Geom` still assigns nothing to a satellite.** This shows the room exists,
  not that the framework can use it. The missing case is still missing.

### A 2500× cost difference from asking for less

The first attempt called `per_block_evaluation`, which builds **all 77**
partitions of 12. It reached **9.99 GB RSS** at 266 % CPU and was killed before
it could OOM the session. Only the **7 two-row blocks** matter under convention D
(max dimension 297), and `block_rep_braid_word` takes one partition at a time —
the whole 32-branch sweep then ran in **3.6 seconds**.

Two process notes worth keeping. The first attempt was also launched as
`… | tail -12`, which buffers until the process exits, so it produced **no**
progress output for its entire life — the long-compute discipline says `tee`,
and this is why. And `pkill -f cable_feas.py` matched the killing command's own
argv and killed that shell too.

## Addendum 27 — the library was not empty, and my correction did not land where I said it did (2026-08-26)

Bean `qou-6tcn`. Two errors, the second worse than the first.

### The first: a one-tier grep reported as a corpus-wide gap

Addendum 24 and the source ledger both state that the ingested library holds
**zero** sources on satellites, toroidal knots or cabling. **False.** I grepped
`library/INDEX.md` — the one-line briefs — got zero hits, and stopped.

AGENTS.md path 5 prescribes **three** tiers, cheapest first: `INDEX.md`, then
`summary.json`, then `grep -rln <topic> library/<doc-id>/sections/`. I ran tier
1. Measured now, **excluding** the 15 documents ingested on the strength of the
false report:

| term | pre-existing documents |
|---|---:|
| `satellite` | **12** |
| `cabling` | **19** |
| `JSJ` | **13** |
| `"essential torus"` | **4** |

`INDEX.md` genuinely has 0 hits for all four, and that is *by construction*: the
briefs are **extractive**, assembled from each document's abstract and section
titles, so a topic discussed in a body but absent from its abstract cannot
appear there. That is exactly why the checklist has three tiers and why its own
text warns the briefs are "only as good as the abstract [they] came from". The
failure is mine, not the index's.

**It cost the author work.** They uploaded 15 PDFs in response. The ingest is
still worth having — `arxiv-0807.2679v1`, the cabling formula, was genuinely not
held, and path 5 now reaches all of it — but the gap was far smaller than
reported.

### The second: I said I had fixed it, and had not

The ingest commit's message states *"the ledger's 'zero sources' framing is
corrected in the same commit"*. **It was not.** Neither
`satellite-cabling-source-ledger.md` nor Addendum 24 was touched by that commit;
the false claim stayed live in two durable artifacts while the commit message
asserted otherwise.

That is the more serious of the two. A wrong measurement is a wrong
measurement; a commit message claiming a correction that is not in the diff
makes the record actively misleading, and would have survived exactly as long as
nobody diffed the commit against its own message. Both files are corrected in
place now, each carrying the measured numbers rather than a bare retraction.

### The rule this earns

**Grep INDEX.md to decide whether to look further — never to decide that
nothing is there.** A zero at tier 1 is a statement about abstracts, not about
the corpus. Before writing "the corpus has nothing on X" into anything durable,
run tier 3.

And: **when a commit message claims a correction, the correction must be in that
commit's diff.** Check before writing the message, not after.
