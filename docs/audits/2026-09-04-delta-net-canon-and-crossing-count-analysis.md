# Δ: which net value is canonical, and does the crossing-count sentence survive?

> **Notation note.** This document predates the 2026-09-05 calibration rename and uses
> the superseded symbols `𝔇_β` (CAL-2) and/or `𝔇_π` (CAL-3). Those are now
> `P_skew^β` (the bar-skew β-channel) and `P_avg^π` (the bar-even π-channel); the
> `𝔇` family is reserved for genuine decay rates (`𝔇_n`, `𝔇_μ`, `𝔇_K` = ℏ/τ).
> The analysis below is left as the record of what was analysed at the time.

**2026-09-04.** Owner asked for pros/cons/recommendations/downstream impact on
two questions. One of them is already answered on `main` and I had been
carrying it as open; the other is not a two-way choice and cannot be posed as
one until a prior question is settled. Both corrections are below, with the
measurement that establishes them
([`qbeta_delta_candidate_census_probe.py`](../../computations/qbeta/qbeta_delta_candidate_census_probe.py),
10/10, exact in `h`, no float64).

Scope-(a) throughout. Nothing here selects, wires, or edits a nucleon model.

---

## 0. The decision, up front

There are **three** decisions tangled here, not two, and they are separable.
Untangling them is most of the value of this document, because two of the three
turn out to be cheap and only one is genuinely hard.

| | decision | status |
|---|---|---|
| **D-A** | Which **element** of `H₃(q)` is Δ | **open** — 11 candidate values, genuinely hard |
| **D-B** | Which **functional** evaluates it (`ε` vs augmentation vs `tr_M` at `z_D`) | open, tracked separately as `qou-99qc`; **independent of D-A** |
| **D-C** | The **crossing count** in the neutron block | **already decided** 2026-08-29; one stale consequence remains, and it is cheap |

The habitual framing — *"which of the four Δ values is canonical?"* — silently
merges D-A and D-B and inherits D-C's arithmetic. That is why it has not
closed.

---

## 1. D-C — "13 crossings": already struck, five days ago

### What the corpus actually says now

`content/quantum-observable-universe/knots-particles-confinement/categorical-neutron-properties.md:13`,
live on `main`:

> The integer LP dual selects $L_-$ as the minimum-action stabiliser, for a
> total of **11 crossings** (6 from $\mathcal{B}_3$, 3 from quarks, 2 from
> gluons) … The earlier "$L_+ \to L_-$, 4 gluon crossings, 13 total" was wrong
> on its own terms, independently of anything below.

So the sentence was **struck and replaced**, on owner authorisation, as
correction 1 of 4 under `qou-vtlj` (2026-08-29). The reasoning is recorded
inline: the block's own printed `net(𝔫) = +0.7976` is the **eleven**-crossing
value on the k-ladder (9 → 0.788010, **11 → 0.7975664**, 13 → 1.235859), and
the 13-crossing value appears nowhere in the corpus.

**The question "re-derived or struck?" is therefore stale.** It was struck, and
re-derived in the same edit. I had it queued as open; that was my bookkeeping
error, not a corpus gap. Recorded here because a stale open item is exactly the
failure mode this repo's corpus-grep discipline exists to prevent, and I hit it
on my own ledger.

### What is NOT resolved: the ledger was not swept

Two blocks in the **same chapter directory** now contradict each other:

| block | last edited | says |
|---|---|---|
| `categorical-neutron-properties.md:13` | 2026-08-29 | 11 total, **2 from gluons** |
| `gluon-stabiliser-ledger.md:13` | 2026-08-24 | "the proton takes two gluon crossings and **the neutron four**" |

The ledger predates the correction by five days. It is not merely stale
decoration — it goes on to say *"that difference is what makes the neutron
heavier and so feeds $\mathfrak{Q}_\beta$"*, i.e. the 2-vs-4 asymmetry is
load-bearing in its own argument. Under the corrected count the asymmetry is
2-vs-2 and that argument has no premise.

**This is a contamination sweep the 2026-08-29 correction owed and did not
make.** It is cheap: one block, one paragraph.

### And a second, deeper tension the correction did not touch

The *replacement* sentence still asserts **"The integer LP dual selects $L_-$
as the minimum-action stabiliser"**. Measured under convention D
(`nucleon-lp-convention-probe.py`, re-run 2026-09-03):

| | rank | `|tr_M|` | bare (0 gluons) |
|---|---|---|---|
| neutron `L₊.L₋` | **26 / 41** | 0.690056 | **0.408267** |
| proton `σ₀.σ₀` | 10 / 41 | 0.615273 | **0.544370** |

The min-`|tr_M|` optimum is a **single σ₀ at one crossing**; under the
minimum-crossing objective `def:universal-ilp-algorithm` actually states, it is
**zero**. The ledger reaches the same place independently and says so plainly:
*"Four statements of one quantity, three answers."*

So D-C is not fully closed. **What is closed is 13-vs-11.** What is open is
whether **11 itself** survives, since the selection rule that yields 11 does
not select `L₋` under the canonical convention. That is a strictly smaller and
better-posed question than the one that was asked.

---

## 2. D-A — the candidate set is 11 values, not four

### The measurement

`qou-bg3w` and `qou-vtlj` each conclude the corpus carries **four** net values.
Neither is wrong. They are **different fours**, overlapping in two rows:

```
qou-vtlj                             qou-bg3w
-----------------------------------  ------------------------------------
short model        -0.1872072   <->  Delta_S             -0.187207
blocks AS STATED   -0.2089           build_nucleon_nf    -0.1883216  ( 9x)
blocks CONSTRUCTED -0.2137638        build_atom_nf_exact -0.2272041  (11 interleaved)
hecke_core Delta_L -0.2331977   <->  nucleon_gen_chains  -0.2332459  (11 gen-grouped)
```

Measured at **one** pin (proton `q₀`) in **one** basis, the union is **11
distinct values**. The exact forms:

| model | crossings | net(Δ) at `q₀` | net(Δ) exact in `h` | `[z²] tr_M` | e⁻ |
|---|---|---|---|---|---|
| `build_nucleon_nf` | 9 | −0.18829060147138 | `h(h⁶+2h⁵+2h⁴+2h³−h²+2h−4)/4` | `−h(h²−h+1)(h²+h+1)/2` | −0.00097599 |
| `build_atom_nf_exact` | 11 interleaved | −0.22715971176557 | `h(2h⁷+2h⁶+5h⁵+4h⁴+2h³+h²−2h−4)/4` | `−h(h²+2)(2h⁴+h²+1)/4` | −0.02380508 |
| `nucleon_gen_chains` | 11 gen-grouped | −0.23319771131566 | `−h(h²+2h+4)/4` | `−h(h²+2)/4` | **0** |
| published closed form | 1 / 2 | −0.18720719452938 | `h²/2 − h` | — | — |
| blocks AS STATED | — | −0.2089 | — | — | — |
| blocks' own recipe | 11 | 6 distinct in `[−0.2507, −0.2047]` | — | — | — |

### Three defects in the beans, measured not argued

**(i) `qou-bg3w` has L₊ and L₋ swapped.** It states *"L+ vanishes exactly for
this bean's Delta_L — the exclusion there rides on L-"*. Measured on the
gen-grouped element: **L₋ = 0**, and **L₊ = −h(h²+2)/4 = −0.10681445765158**.
That reproduces `qou-vtlj` cont. 7's independently-derived closed form
`−(q²−1)(q⁴+1)/(4q³)` to 30 dps. Rewriting it confirms the algebra:
`−(q²−1)(q⁴+1)/(4q³) = −h(q²+q⁻²)/4 = −h(h²+2)/4`. **`qou-vtlj` is right; the
(D1) exclusion rides on L₊.** This is precisely the slot-order trap
`qbeta_d1_eleven_crossing_exclusion_probe.py` documents in its own header — the
`hm_sym` basis reverses positions 3 and 4 against `gram.py`'s canonical
`NF_BASIS` — and it caught a second bean.

**(ii) `qou-bg3w`'s 9-crossing residual is the PIN, not float64.** It calls
`−0.1883216147` the *exact* net and `−0.188290601` the *stored float64
coordinate sum*, attributing the gap to *"float64 h versus exact `_H_FRAC`"*.
Measured, the same exact expression gives:

```
  −0.18832161472187   at q = 111/100      <- bg3w's "exact"
  −0.18829060147138   at the proton pin   <- bg3w's "float64"
```

**Both of its numbers are exact; they are at different `q`.** Float64 rounding
would show at ~1e-16, not 1.6e-4. This is the same 185 ppm `_Q_FRAC` trap the
bean *itself* later caught for its own decimals ("every decimal in the entry
above was at q = 111/100") — it simply never went back and re-attributed this
one.

**(iii) The two beans' "agreeing" bottom rows are one element at two pins.**
Gen-grouped net is −0.233197711 at `q₀` and −0.233245896 at `q = 111/100`.
Agreement to four digits that is really a pin difference.

### The blocks' recipe does not determine a number — until the neutron pins it

The properties blocks give the typed **shifts** (uu → 0, ud → −h/2, dd → −h)
but never say which **generator** each quark crossing sits on. Enumerating all
16 readings (8 assignments × 2 Hopf orientations) gives net(Δ) spanning
`[−0.2507, −0.2047]` — **6 distinct values**. So "the constructed Δ" is not a
number without a selection rule.

Imposing the blocks' own stated `net(𝔫) = 0.7975664` collapses it: exactly **2**
of 16 readings survive, and they agree **exactly** at **−0.21376383061666**,
independently reproducing `qou-vtlj`'s −0.2137638. That is a genuine
reproduction from a different construction, and it is the strongest single
result here.

**But the pin rests on the neutron alone.** `qou-vtlj` separately established
that **no** reading of 96 (and later 240) reproduces the stated **proton** net
1.0065 — closest 1.00679, |err| 3.2e-4, against a neutron residual of ~1e-30.
So the constructed value is pinned by one of the block's two numbers and
contradicted by the other.

---

## 3. D-A: the options

### Option 1 — Δ_S, the published closed form (`h²/2 − h`, −0.18720719)

**What it means.** Canonise the 1-/2-crossing short model that the published
`c_k` ladder is already built from. Change nothing; write the choice down.

**What it costs.** Nothing computational. One content edit stating the element
explicitly, so the next reader cannot re-open it.

**What it risks.** It is the *only* candidate for which **(D1) is available** —
`2α = net(Δ) − tr_M^z(Δ)` is affine in `z` because Δ_S is supported off
`{L±, e⁻}`. Measured here: the `z²` coefficient is **nonzero on all three long
models**, so `α = (z−1)h/2` is not the counit-minus-trace gap on any of them.
Canonising Δ_S therefore *preserves* the corpus's only derivation of the ladder
phase. The risk is the opposite one: it is the candidate with the **weakest
constructive story** — a 1-/2-crossing element against a nucleon the blocks
describe with 11.

**What it commits to.** Accepting that the decay-channel Δ is a *different,
smaller* object than the nucleon normal forms — which is defensible (the
channel need not be the state) but must be *said*, not left implicit.

**Blast radius.** 27 sites, 18 of them witnesses, including
`q-beta-spectral-bridge.witness.json`,
`qbeta-decay-functional-unification-protium.witness.json`,
`probe-d-dressing-is-proton-net.witness.json`, plus
`docs/canonical-derivation-cheat-sheet.md`. Choosing it moves **zero** numbers.

### Option 2 — the constructed 11-crossing value (−0.21376383061666)

**What it means.** Canonise the element the properties blocks' own recipe
builds, selected by their stated `net(𝔫)`.

**What it costs.** Re-derivation of everything downstream of `ε(Δ)`. The
published `Q_β` ladder is built on `h²/2 − h`; this value differs by **14.2 %**.

**What it risks.** **(D1) is lost** — the `z²` coefficient is nonzero, so the
corpus's only derivation of `α` goes with it and branch 3 (KZ /
Kohno–Drinfeld holonomy) becomes the sole remaining route. It is also pinned by
the neutron number while *contradicting* the proton number from the same block,
and `qou-vtlj`'s weight-of-evidence reading is that **the stated proton net is
wrong**. Canonising on a block one of whose two numbers is judged erroneous is a
thin foundation.

**What it commits to.** A `Q_β` re-derivation, and accepting the block's neutron
figure as authoritative over its proton figure.

**Blast radius.** 3 sites today, all probes about the fork. But *adopting* it
would propagate into every one of Δ_S's 27.

### Option 3 — a long `pyhecke` model (−0.2272041 or −0.2331977)

**What it means.** Canonise one of the two 11-crossing builders in
`pyhecke.atom`.

**What it costs.** Same re-derivation as Option 2, plus a prior choice between
*interleaved* and *gen-grouped*, which differ **only in order** yet give
different elements (`H₃(q)` is non-commutative across generators) and nets 2.6 %
apart.

**What it risks.** Highest. `qou-vtlj` cont. 7 shows the gen-grouped element's
`Δtr_M(n−p)` is a **negative-definite** quadratic in `z` for **all q > 1** — max
`−(q−1)(q+1)(q²+1)²/(4q(q⁴+1)) < 0` — while the γγ anchor is **positive**
(+0.0445860283). So it cannot reproduce that anchor at **any** Markov parameter
and **any** substrate `q`. That is a structural exclusion, not a disagreement.
It also has **L₋ = 0 and e⁻ = 0 identically** — no weight in the Hopf-link or
trefoil channels the blocks call dominant.

**What it commits to.** Overriding a proved exclusion. I would not.

### Option 4 — decline to choose; canonise the *question*

**What it means.** Record in content that Δ is model-dependent, state which
element each published number is on, and leave selection open.

**What it costs.** One content edit. No re-derivation.

**What it risks.** The corpus keeps carrying 11 values, and the next agent
re-opens it — which has now happened at least three times (`qou-im4m`,
`qou-bg3w`, `qou-vtlj`).

**What it commits to.** Nothing. It is the honest floor.

### The default — what happens if you say nothing

Δ_S continues as the de-facto canon by incumbency: 27 sites, every published
`Q_β` number, the cheat sheet. Nothing breaks and no figure moves. **The no-op
is safe**, and that is worth knowing before spending anything here.

---

## 4. Recommendation (my judgement, not a finding)

**Option 1 + the D-C sweep, and explicitly *not* now attacking D-A's hard core.**

Reasons, in order of weight:

1. **(D1) is the asset.** It is the corpus's only derivation of the ladder
   phase `α`, and it exists *only* on Δ_S. Every alternative destroys it and
   offers nothing in exchange — measured here, on all three long models.
2. **The incumbency is 27-to-3 and the rivals have zero production consumers.**
   Every site of every alternative is a probe about the fork itself.
3. **The strongest rival is pinned by a number its own block contradicts.**
4. **The D-C sweep is cheap and unambiguous** — one stale paragraph asserting a
   2-vs-4 asymmetry that the 2026-08-29 correction removed.

**What I would *not* do:** canonise Δ_S silently. The choice must be written
down *as a choice*, naming the element, or this re-opens a fourth time.

**A caveat that limits all of the above.** Δ_S's headline virtue — (D1)'s
availability — is a **convention-C-frame** fact, and AGENTS.md records the whole
`c_k` ladder as C-frame pending re-derivation under D (`qou-cds1`). Separately,
`qbeta-counit-closed-form.md` establishes that `ε` is **inadmissible under
convention D**: it does not annihilate the trace ideal, and Δ has a non-zero
`(1³)` component. So Option 1 canonises an element whose evaluating functional
the canonical convention forbids. That is D-B, it is tracked as `qou-99qc`, and
**it is the question that should be answered before D-A**, because a functional
ruling may collapse the element question by itself.

---

## 5. Downstream impact

**If Option 1 (or the default):** nothing moves. No witness, no `Q_β`, no mass,
no binding, no L2 figure. The 27 sites stay correct; they gain a stated
provenance.

**If Option 2 or 3:** `ε(Δ)` moves 14.2 % or 24.6 %, which propagates to
`Q_β = ℏ/𝔇_β` — a **CAL-2 proxy** and a published comparison point. The `c_k`
ladder is extracted by inverting `Q_β`, so `c₃` and everything resting on it
(`c₃ = −2 = J_Hopf(q=1)`, the 3.47 % near-match, the cross-anchor swing) would
need re-extraction. `α` loses its derivation. This is a multi-tranche
re-derivation, not an edit.

**The D-C sweep, either way:** `gluon-stabiliser-ledger.md`'s
`𝔪_𝔫 − 𝔪_𝔭` argument loses its premise and needs restating. Since the
ledger's own closing paragraph already says the crossing count is "genuinely
unsettled", the restatement is small — the block is arguing the right thing on
a stale number.

**Not affected, contrary to a claim I nearly made:** `tools/hecke-engine`'s
isotope certificates carry **none** of these values. My first scan used
`rg -l` without `-F`, so `.` was a wildcard and matched digit runs
(`012331977`, `042332458`) inside long float lists. Caught before it reached a
write-up; recorded because the near-miss is the same detector-blindness class
the repo catalogues.

---

## 6. What would actually close D-A

In increasing cost:

1. **Answer D-B first** (`qou-99qc`). If the functional ruling forces an
   element with vanishing `(1³)` component, the element question may collapse
   without a separate decision.
2. **Re-run the producer of `tbl:categorical-neutron-table-data` at 50 dps.**
   `qou-vtlj` cont. 5 showed the constructed model matches 3 of 6 NF components
   exactly and the residual is *"consistent with `c(σ₀−σ₁)σ₀` and not
   distinguishable from it"* — because the table is quoted to 4 dp. Blocked:
   the block carries **no** `computation.script` and no `computation.witness`,
   and archaeology bottoms out at the shallow-clone graft boundary.
3. **Settle the proton.** No reading of 240 reproduces the stated 1.0065.
   Either that number is wrong (`qou-vtlj`'s reading) or one structural element
   is unaccounted for.

---

## Provenance

Measurement: [`computations/qbeta/qbeta_delta_candidate_census_probe.py`](../../computations/qbeta/qbeta_delta_candidate_census_probe.py),
10/10, 50 dps, exact sympy in `h` with an exact `h → h(q₀)` substitution, no
float64; witness
[`qbeta-delta-candidate-census.witness.json`](../../computations/qbeta/qbeta-delta-candidate-census.witness.json),
proton pin. Prior work: `qou-bg3w`, `qou-vtlj`, `qou-jqjx`, `qou-im4m`,
`qou-cds1`, `qou-99qc`.
