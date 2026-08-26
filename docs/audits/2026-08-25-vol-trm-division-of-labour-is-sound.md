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
