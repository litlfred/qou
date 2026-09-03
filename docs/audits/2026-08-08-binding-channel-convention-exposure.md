# How exposed is the binding channel to the convention-D resolution? — measured

Branch `claude/binding-channel-convention-exposure-2026-08-08`. 2026-08-08.

Predecessors (established and merged the same day; not re-derived here):
[`2026-08-08-mass-fibre-dimension-forces-convention-d.md`](2026-08-08-mass-fibre-dimension-forces-convention-d.md)
(bean `qou-n1dj`) and
[`2026-08-08-borromean-trace-convention-forcing.md`](2026-08-08-borromean-trace-convention-forcing.md)
(bean `qou-3qrv`). Those settled the **mass** channel as convention D
(`z_D = q³/(q²+1) = q²/[2]_q`, `y_(1³) = 0`, the Jones/Temperley–Lieb trace),
by the chain *fibre → row cap `ℓ(λ) ≤ 2` → `y_(1³) = 0` → D*, with
`z·[N]_q = q^N` proved sorry-free
(`QOU.BraidsAndKnots.FibreDimensionForcesTL.ocneanu_param_eq_of_fibre_qdim`)
and injective in `N`, so C corresponds to `N_eff = 2.5995…` — no integer fibre
dimension.

This audit measures the **binding** channel's exposure to that resolution.
Everything below is **measurement only**: no production value was changed, no
weight or coefficient was tuned, and AME2020 appears exclusively as an output
comparison target. All numbers are at the **experimental / proton** pin
`q₀ = 1.1099785827513808075916690956107688798744991218736`
(`q_parameter.Q_50_DIGIT_STR`, per the 2026-08-07 owner directive), computed at
70 dps. No muon-built cache is read anywhere: `y_λ` comes live from the
Wenzl-bridge closed form at each `z`, and `χ^λ` live from the Hoefsmit
seminormal matrices at the proton `q₀`.

---

## 1. Structural verdict — the same fibre argument applies, and the binding channel's own code says so

**Yes.** The binding channel is exposed by the identical argument, and the
evidence is inside its own weight producer rather than in an analogy to the
mass channel.

### 1a. The binding channel's weight producer is parameterised by the fibre dimension

[`y_lambda_wenzl_bridge.py`](../../computations/y_lambda_wenzl_bridge.py) is the
`y_λ` source for the whole binding chain. At **lines 122 and 140** it hard-codes

```python
z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))      # convention C
Q = q ** 2
X = q * z / (1 - Q + q * z)
```

and builds every weight from `X` via the principal Schur specialisation
`s_{λ,X}(Q) = Q^{n(λ)} ∏_{x∈λ} (1 − X·Q^{c(x)})/(1 − Q^{h(x)})`.

That `X` is not an auxiliary variable. Substituting `z = q^N/[N]_q`:

```
X = q·z/(1 − q² + q·z)  =  Q^N          exactly,  Q = q²
```

verified **symbolically** (sympy residual `X(z = q^N/[N]_q) − Q^N → 0`,
identically zero) and numerically for `N = 1..6` at `q₀`
(`max |X − Q^N| = 1.81e-71` at 70 dps). Rearranged, `X = Q^N ⟺ z·[N]_q = q^N`
— *verbatim* the relation `ocneanu_param_eq_of_fibre_qdim` proves in Lean.

So the bridge's "fractional Wenzl rank" `r` in `X = Q^r` **is** the fibre
quantum dimension, and the hard-coded `z_C` sets it to a non-integer. Inverting:

| | `z` | `N_eff = log X / log Q` |
|---|---|---|
| **C** (binding, today) | `0.49932033418369445241` | **`2.5995155364`** |
| **D** (mass, settled) | `0.6126880371464652516` | `2.0` (and `\|z_D − z(N=2)\| = 0.0`) |

`N_eff(C) = 2.5995155364` reproduces the mass audit's figure to every printed
digit — obtained here from the *binding* channel's own code, independently.

The bridge's docstring already says as much, without drawing the consequence:

> *Earlier session claim "no closed-form exists for our generic z" was WRONG —
> it confused integer-N Wenzl `SU_q(N)` (**which our z is not**) with the
> analytic continuation in X (which IS valid).*

The analytic continuation is valid *as mathematics* — it is a perfectly good
Markov trace. What the sentence concedes is that the binding channel's `z`
belongs to no integer fibre.

### 1b. The row cap is already inside the bridge's closed form

At `X = Q^N` the numerator factor `(1 − X·Q^{c(x)}) = (1 − Q^{N+c(x)})` vanishes
iff `c(x) = −N`. Cell content is `c = j − i`, so `c = −N` requires the cell
`(i,j) = (N,0)`, which exists **iff `ℓ(λ) > N`**. Hence:

- **convention D annihilates every `>2`-row Wedderburn block, at every `n`**;
- **convention C annihilates none** — at a non-integer `r`, no cell ever hits
  content `−r`, so *every* partition of *every* `n` carries nonzero weight.

Machine-verified for all partitions of `n = 2..8`: `s_{λ,Q²} = 0 ⟺ ℓ(λ) > 2`,
no exceptions, and nothing vanishes at `X_C`. At `n = 3` the D vector
reproduces the mass audit's closed form
`([4]_q/[2]_q³, 1/[2]_q², 0) = (0.50540422650393080319, 0.24729788674803459841, 0)`
to `9.06e-72`; C gives
`(0.41539579536061340131, 0.28092963103101970778, 0.022744942577347183133)`,
matching the mass audit's C row. Both satisfy `Σ_λ y_λ d_λ = 1` exactly — both
are genuine normalised Markov traces; the question was never which is *a* trace.

### 1c. The corpus already states the cap for general `n`, on the same fibre — and records the tension

[`def:two-row-stratum`](../../content/quantum-observable-universe/mass-theory/two-row-stratum.md):

> *We restrict to the `SU(2)` action:* `H_n(q) ↠ End_{SU(2)}(V^{⊗n})`, `V = ℂ²`.
> ***Partitions with `ℓ(λ) > 2` map to zero.***

Same fibre `V = ℂ²`, stated at general `n` — exactly the row cap, as the kernel
of a projection. The binding chain runs at `n = 3A` on that same `V^{⊗n}`, so
the cap applies there by the same statement.

The same block then records the tension explicitly:

> ***Scope of the two-row dominance: the trace, not the binding sum.*** *… the
> `ℓ(λ) > 2` share of the binding sum grows from ≈26 % at ²H to ≈100 % at ⁴He,
> where the two-row contribution is ≈0.02 % of the total. The binding formula
> sums over **all** partitions and does not inherit the restriction described
> above.*

That paragraph is where the exposure lives. It says the binding sum draws
almost all of its ⁴He value from precisely the blocks the same block's own
`SU(2)` projection sends to zero.

### 1d. The escape hatch does not apply, and the exposure is not 195 ppm

The `195.8 ppm` figure (`D − C = 1.9554e-4` on `β_Bor`) is the **`n = 3`** case,
where one partition is affected. The block-count exposure grows sharply:

| `n` | isotope | `p(n)` | `ℓ ≤ 2` | zeroed under D |
|---|---|---|---|---|
| 3 | nucleon | 3 | 2 | **1** |
| 6 | ²H | 11 | 4 | **7** |
| 9 | ³H / ³He | 30 | 5 | **25** |
| 12 | ⁴He | 77 | 7 | **70** |

And "binding is a ratio, so the scale cancels" fails for a second, independent
reason beyond the weight-vector argument: **`z` enters production through the
per-interface factors directly.**
[`closed_form_tau_M.interface_factor`](../../computations/closed_form_tau_M.py)
returns `f = z`, `z − h`, `z − h/2` (`h = q − q⁻¹`) with
`markov_z(q) = 1/(√q + 1/√q)` at line 132. A per-block reweighting does not
cancel in a difference of two same-weight traces, and a change in `z` moves each
interface factor outright.

**The Markov-axiom identity behind those factors survives.** `tr(α σ_g) = z·tr(α)`
plus the Hecke skein `σ⁻¹ = σ − h` is what generates `z`, `z − h`, `z − h/2`, and
it is Lean-proved sorry-free as
`QOU.BraidKnot.interface_knot_markov_z_bar_symmetric`. That identity is
convention-**independent**: it fixes the *shape* of the factors, not the *number*
`z`. Under D it holds verbatim with `z_D` substituted. Per the permanence
principle in AGENTS §"Before declaring refuted", a proved per-bond factor stays
valid when its parameter is re-pinned.

---

## 2. The measured delta

### 2a. Production route — the closed-form chain, A = 2..7

`binding_canonical(Z, N, use_closed_form=True)` — the production path — never
sums `p(3A)` partitions. It uses the Phase-5q closed form, so the whole table is
computable under both conventions in milliseconds:

```
Δtr = τ_p^Z · τ_n^N · (1 − ∏_i f_i(q)),      B = E_0 · Δtr,  E_0 = Q_NEUTRON_MEV
```

Both convention entry points were swapped: the `H₃` nucleon blocks
(`τ_p 1.0653061442544499757 → 1.1457596924573008697`,
`τ_n 0.92323322991163717797 → 0.98774368811580957163`) **and** the interface
factors (`f_positive 0.49932033418369445241 → 0.6126880371464652516`,
`f_averaged 0.3947901847858747947 → 0.50815788774864559388`).

| atom | interfaces | `B_C` (MeV) | `B_D` (MeV) | AME2020 (MeV) | `B_D/B_C` | rel. err C | rel. err D |
|---|---|---|---|---|---|---|---|
| ²H | 1 | `0.4656758321` | `0.4354671419` | 2.224566 | **`0.93512935783`** | −79.1 % | −80.4 % |
| ³H | 2 | `0.6289740062` | `0.6951568776` | 8.481821 | `1.10522353974` | −92.6 % | −91.8 % |
| ³He | 2 | `0.6581109966` | `0.6985968991` | 7.718043 | `1.06151834975` | −91.5 % | −91.0 % |
| ⁴He | 3 | `0.7134686058` | `0.8760818142` | 28.295673 | `1.22791922032` | −97.5 % | −96.9 % |
| ⁶Li | 5 | `0.7381301369` | `1.098738996` | 31.994566 | `1.48854374134` | −97.7 % | −96.6 % |
| ⁷Li | 6 | `0.6855107205` | `1.10603151` | 39.244538 | `1.61344159393` | −98.3 % | −97.2 % |
| ⁷Be | 6 | `0.7896267471` | `1.274529502` | 37.600411 | **`1.61409109658`** | −98.0 % | −96.6 % |

**Two independent cross-checks.** (i) `B_C` reproduces the committed
[`binding-canonical.witness.json`](../../computations/binding-canonical.witness.json)
production values to ≤ `1.2e-4` relative (the μ–p pin offset plus the
averaged-crossing marshalling difference) — e.g. ²H `0.4656758321` vs the
witness's `0.465620587590569`, ⁴He `0.7134686058` vs `0.7134609413518084`.
(ii) The `D/C` ratios agree with a completely different route — the direct
`Σ_λ y_λ χ^λ` sum over all `p(3A)` partitions — to `2.7e-5`
(²H `0.93512935783` vs `0.935103747234`; ³H `1.10522353974` vs `1.10520923928`;
³He `1.06151834975` vs `1.0614979115`; ⁴He `1.22791922032` vs `1.2279`).

**The delta is real, it grows with interface count (−6.5 % at ²H to +61 % at
⁷Li/⁷Be), and it does not cancel.** It is also **not monotone in direction**: D
makes ²H worse and every `A ≥ 3` isotope slightly better. A convention change
that moved everything one way could be mistaken for an absorbable scale; this
cannot.

**The framing that matters more, stated plainly.** Both conventions sit **79–98 %
below AME2020**. The convention is not what stands between this chain and the
data; the deficit is a factor of 5–50 and neither convention touches it. Whether
D is "better" or "worse" here is cosmetic against that gap.

### 2b. The Δ_λ route — where the exposure is largest

`B/m_e = |Σ_λ y_λ χ^λ Δ_λ|` with `Δ_λ = (−1)^{n(λ)}·f^λ` (the PROVED
per-partition value, sorry-free general-`n`,
`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`) is the object
`def:two-row-stratum` discusses. It is *not* what production computes, and it is
far more exposed:

| atom | `Σ_λ y_λ χ^λ Δ_λ` D/C | two-row share of the C sum | rel. err C → D |
|---|---|---|---|
| ²H | `0.96459229738` | `0.737871293214` | −82.91 % → −83.52 % |
| ³H | `0.662704974891` | — | −77.50 % → −85.09 % |
| ³He | `0.671055852189` | — | −69.62 % → −79.61 % |
| ⁴He | ≈ `−147×`, **sign flip** | ≈ `−0.0218 %` | −99.998 % → **−99.655 %** |

Two things to read carefully here.

**The ²H two-row share independently reproduces the corpus.**
`two_row_share_of_C_binding_sum = 0.737871293214` ⇒ a `>2`-row share of
**26.2 %**, matching `two-row-stratum.md`'s "≈26 % at ²H" — computed at the
proton pin with a live weight vector.

**But the D/C ratio is 0.9646, not 0.7379.** D does not merely truncate; it
*re-weights* the survivors upward (`y_[6]: 0.0591877210 → 0.1153242249`, ×1.95;
`y_[5,1]: 0.0589606835 → 0.0789529624`). Most of the lost 26 % is recovered. The
truncation share is therefore a poor proxy for the convention delta, and any
argument of the form "D discards X % of the sum, so it changes the answer by
X %" is wrong.

**⁴He is where it breaks.** Under D only the 7 two-row blocks of 12 survive, so
`sum_D` is exactly computable from 7 characters (dims ≤ 297) instead of all 77
(dims to 2673) — 22 s instead of hours. Result: `B_D = 0.0975689999204` MeV
against a C full-sum value of
`3.038187709974314038612212037018576105611111188668` MeV
(from [`two-row-vs-higher-row-binding-split.witness.json`](../../computations/two-row-vs-higher-row-binding-split.witness.json),
**muon pin** — quoted in its own row, never combined into a single computed
quantity with a proton-pin number) and AME 28.295673. And the sign flips: the
two-row part is `+0.001296961869433110271148987806785111917677973964` against a
total of `−5.94558502688089744619708670466463048386403955390`. Cross-validation:
my proton-pin two-row partials `tr_M = 0.051295784459` and
`B_two_row = 0.000662685222287` against that witness's
`0.0512957929816070113912977885538` and
`0.000662746154365260133700194149922796652247658356` — agreement to `1.7e-7`,
the μ–p pin offset.

So on the Δ_λ route the ⁴He binding is a ~31× change and a sign change. This
route is not wired to production, which is the only reason that is not a live
regression.

---

## 3. Does any recorded corpus conclusion flip under D?

### 3a. The μ₃ door verdict — a sign, tested; it does NOT flip

The strongest flip candidate in the corpus, because the recorded verdict *is a
sign* rather than a magnitude.
[`mu3_abs_choice_robustness_probe.py`](../../computations/deltalambda/mu3_abs_choice_robustness_probe.py)
records

```
Δ²g = Σ_{λ ⊢ 9} y_λ · (χ_ab − χ_a − χ_b + χ_∅),   c₃ = −E₀·Δ²g
door = OPEN (submodular)  if Δ²g < 0  /  CLOSED (supermodular)  if Δ²g > 0
```

`Δ²g` is `y_λ`-weighted over `λ ⊢ 9`, and D zeroes **25 of the 30** weights. A
sign is not protected by a reweighting.

The probe first reproduces the recorded value exactly, using the upstream's own
`E₀ = m_e/(q₀(q₀−1)) = 4.1859813632944758969` MeV (the unit-cell scale — *not*
`Q_NEUTRON_MEV`; that mismatch cost one run):

| | `Δ²g` C | `Δ²g` D | door C | door D | `c₃` C (MeV) | `c₃` D (MeV) | `c₃` D/C |
|---|---|---|---|---|---|---|---|
| ³H, \|χ\| | `0.422547336382` | `0.327839832347` | CLOSED | **CLOSED** | `−1.768775275` | `−1.372331428` | `0.775865338908` |
| ³H, raw χ | `0.389987701252` | `0.327839832347` | CLOSED | **CLOSED** | `−1.632481249` | `−1.372331428` | `0.840641464577` |
| ³He, \|χ\| | `0.335745506599` | `0.246975840113` | CLOSED | **CLOSED** | `−1.405424433` | `−1.033836264` | `0.735604305222` |
| ³He, raw χ | `0.317449471663` | `0.246975840113` | CLOSED | **CLOSED** | `−1.328837572` | `−1.033836264` | `0.778000476168` |

Reproduction gate against `EXPECT = {"T": -1.769, "3He": -1.405}`
(`mu3_abs_choice_robustness_probe.py:53`): `−1.768775275` and `−1.405424433` —
both reproduced, asserted in the witness (4/4 assertions pass).

**Verdict: the door stays CLOSED (supermodular) under D, in both χ variants and
both mirror isotopes.** A recorded conclusion tested and *strengthened*, not
refuted. It now survives two conventions.

Two by-products:

1. **`r* ≈ 1.585` is a C-convention number.** `c₃` moves 22–26 %, so with `μ₃`
   held fixed the A=3 magnitude target would scale by `1.28888345677` (³H) or
   `1.35942651899` (³He) — `r* → 2.04–2.16`. Any probe aiming at 1.585 is aiming
   at a convention-dependent target. This is a scope observation about the
   target, **not** a claim that the A=3 magnitude wall dissolves: the wall's
   content is that `r*` is not 1 and is bracketed out of Hecke-level
   constructions, and `2.04` is no closer to 1 than `1.585`.
2. **Under D the `|χ|`-vs-raw-χ modelling choice becomes an exact no-op**
   (`0.327839832347` for both variants; `0.246975840113` for both) — every block
   carrying negative raw χ is a `>2`-row block that D annihilates. The upstream
   probe's entire robustness concern ("raw χ negative on n/30 blocks, so `abs()`
   is not a no-op") dissolves under D.

### 3b. Conclusions that survive by construction

- **`trace_convention_reconciliation.py`'s verdict** — *"the A≥3 −60 % gap
  (single-link volume) is the GENUINE open problem — it persists in the correct
  Wenzl convention and is not a convention artifact."* Under D the `A ≥ 3`
  deficit persists (−91.8 % to −97.2 %). **Survives, strengthened.** Note the
  same file states *"the canonical binding convention is Wenzl JM"* with
  `z = 1/(√q + 1/√q)` and attributes it to *"the canonical mass/binding
  convention"* — that attribution is now wrong on the mass side, which is
  follow-up 2.
- **The Δ_λ magnitude wall** — six ansätze failed because no per-block weight
  converts an intensive quantity into an extensive one, with the pairwise cap
  `ρ_A ≤ C(A,2)` proved in `QOU.MassTheory.exchangeDet_pow_two_le_four`. That
  argument is about intensive-vs-extensive scaling, not about `z`; a
  reweighting cannot make a per-block weight extensive. **Survives.**

### 3c. A conclusion that becomes vacuous rather than false

`prop:he4-two-row-dominance` — *the two-row stratum carries ≥ 80 % of
`tr_M(β_⁴He)`* (recorded 86.6 % in the `.md`, 92.66 % in its witness; that
internal 6-point discrepancy is a separate staleness item, follow-up 5). Under D
the share is **100 % by construction**, so the proposition is trivially true and
carries no information. Its content — that the dominance is a non-trivial
algebraic fingerprint — is specific to convention C. Not a flip; a change of
epistemic status that the block does not currently signal.

---

## 4. `n > 3` exposure

**The C/D distinction is perfectly well-defined at every `n`, and the same
untested defect class is present at all of them.**

- `X = Q^N ⟺ z·[N]_q = q^N` is an identity in `N` with no reference to `n`; the
  Ocneanu parameter is a property of the trace, not of a strand count. So
  "which fibre" is exactly as meaningful at `n = 12` as at `n = 3`.
- The row cap `ℓ(λ) ≤ N` is likewise `n`-general — verified for every partition
  of `n = 2..8` here, and it is what the corpus states at general `n`
  (§1c).
- **The exposure grows sharply with `n`** (table in §1d): 1 of 3 blocks at
  `n = 3`, but 70 of 77 at `n = 12`. Since binding runs at `n = 3A`, the
  isotope table sits entirely in the high-exposure regime, and the deltas in §2
  confirm it (`D/C` rising monotonically with interface count to `1.614` at
  A = 7).
- **The defect class was untested above `n = 3`** until this audit: the
  narrative "trace-convention registry" is discussed at `n = 3`, and
  `probe_convention_d_vs_c_borromean.py` tests `β_Bor` at `n = 3` only. §1b
  and §2 are the first `n > 3` coverage.

---

## 5. Recommendation, with its blast radius — for owner decision

**No production value was changed by this audit, and none should be changed
without a decision on the following.** The recommendation is stated so the
owner can rule; it is not acted on here.

The logic is uncomfortable and worth stating in full, because the honest reading
is *not* simply "move binding to D":

1. The mass channel is settled on D by the fibre argument, and the binding
   channel runs on the same `V^{⊗n}` with the same `V = ℂ²` (§1c). Applied
   consistently, that forces D on binding too.
2. But `def:two-row-stratum` records that the binding sum draws ≈100 % of its
   ⁴He value from blocks that fibre annihilates. Under D that route loses a
   factor ~31 and flips sign (§2b).
3. So either **(a)** the binding channel traces a *different, larger* fibre —
   in which case `N` must be an integer at least as large as the longest row
   used, and `z = q^N/[N]_q` for that integer. **`z_C` is not that either**:
   `N_eff(C) = 2.5995…` is not an integer, so C is unmotivated on this branch
   as much as on the other. Or **(b)** the binding channel is inconsistent with
   the mass channel's fibre, and the `>2`-row blocks it relies on carry no
   weight in the framework's own representation theory.
4. Either way, **C is not the answer.** That is the sharpest form of this
   finding, and it does not depend on which of (a) or (b) is true.

What this audit does **not** settle: which integer `N` the binding channel
should use if (a) is the answer. That is a genuine open question and is beaned
(follow-up 1), not guessed here. Naming a favourable `N` by inverting AME2020
would be a fit, and the anti-fit discipline forbids it regardless of the
Subgoal-2 scope reversal.

**Scope of every negative in this audit: (a), scope-limited.** No structural
exclusion is claimed. Specifically: nothing here shows the `>2`-row blocks
*cannot* contribute to binding (that would need a proved invariant, and the
row-cap proof is conditional on the `V = ℂ²` premise, which is the corpus's and
is cited, not re-derived — AGENTS §"Conditional-proved ≠ premise-established").
Nothing here refutes the binding chain: its 79–98 % AME deficit is unchanged by
the convention and is the pre-existing open problem.

---

## 6. Artifacts

| Producer | Witness | What it establishes |
|---|---|---|
| [`binding_channel_convention_exposure_probe.py`](../../computations/probes/binding_channel_convention_exposure_probe.py) | `binding-channel-convention-exposure.witness.json` | §1a–§1d: `X = Q^N ⟺ z[N]_q = q^N` (symbolic + numeric), `N_eff`, the row cap at `n = 2..8`, block counts, the `n = 3` D-vector cross-check. 9/9 assertions. |
| [`binding_closed_form_C_vs_D_probe.py`](../../computations/probes/binding_closed_form_C_vs_D_probe.py) | `binding-closed-form-c-vs-d.witness.json` | §2a: the production closed-form table, A = 2..7, both convention entry points swapped. |
| [`binding_production_route_C_vs_D_probe.py`](../../computations/probes/binding_production_route_C_vs_D_probe.py) | `binding-production-route-c-vs-d-*.witness.json` | §2a cross-check via the direct `Σ_λ y_λ χ^λ` route (`--two-row-only` is exact for D). |
| [`binding_sum_C_vs_D_per_isotope_probe.py`](../../computations/probes/binding_sum_C_vs_D_per_isotope_probe.py) | `binding-sum-c-vs-d-*.witness.json` | §2b: the Δ_λ route per isotope; two-row shares. |
| [`mu3_door_sign_C_vs_D_probe.py`](../../computations/probes/mu3_door_sign_C_vs_D_probe.py) | `mu3-door-sign-c-vs-d.witness.json` | §3a: the μ₃ door sign under both conventions, with the recorded-`c₃` reproduction gate. |

Every witness records `q_0_pin: experimental/proton`,
`uses_muon_built_cache: false`, and
`uses_experimental_target_values_as_input: false`.

**Scope cap, stated rather than hidden.** The full 77-partition ⁴He character
set at the proton pin was not completed (dims to 2673; ~10 partitions in
171 s). It is not needed for any claim above: the D side is exact from the 7
two-row blocks, the production route needs no partition sum at all, and the C
full-sum figure is quoted from the existing muon-pin witness in its own row.
Beaned as follow-up 6.

---

## 7. Follow-ups

1. **Which integer `N` does the binding channel trace, if it is not 2?** The
   open question behind §5.3(a). Must be derived, not fitted to AME.
2. **Correct `trace_convention_reconciliation.py`'s attribution** — it states
   `z_C` is *"the canonical mass/binding convention"*; the mass half is now
   wrong. Same class as the `prop:h3-markov-wenzl-weights` Scope-note correction
   already filed as follow-up 1 of the mass-fibre audit.
3. ~~`docs/coordination/trace-convention-registry.json` does not exist.~~
   **Corrected — the registry DOES exist and has been updated by this audit.**
   Recorded because the mistake is instructive: the branch was cut from a
   `origin/main` ref that a timed-out `git fetch` had left stale, and the
   registry (plus `trace-convention-registry.md` and
   `trace_convention_registry_validate.py`, 526 lines) landed on `main`
   *afterwards* via `2026-08-08-trace-convention-registry-and-doc-fix.md`. An
   earlier draft of this audit asserted the registry was absent — exactly the
   corpus-status over-claim the AGENTS §"Before declaring open" checklist
   exists to catch, produced here by a stale ref rather than a missing grep.
   **Re-fetch before asserting a file's absence.** See §7a below for what was
   actually changed.
4. **Re-scope `r* ≈ 1.585`** wherever it appears as a target
   (`vassiliev_magnitude_a3_probe.py`, the A=3 magnitude audits) to note it is
   a C-convention value that would read `2.04–2.16` under D.
5. **`prop:he4-two-row-dominance` staleness**: the `.md` says 86.6 %, its
   witness `two_row_stratum_ratio` says `0.9266121969291997`. Independent of
   this audit, but adjacent, and the block also needs the §3c epistemic note.
6. **Complete the ⁴He 77-block character set at the proton pin** if the C-side
   full sum is ever wanted at that pin (needs the `pyhecke_native` Rust wheel,
   unavailable in this sandbox — `ImportError: No module named 'pyhecke_native'`,
   so the pure-Python Hoefsmit path was used throughout).

---

## 7a. Registry update

[`docs/coordination/trace-convention-registry.json`](../coordination/trace-convention-registry.json)
`channels[binding]` now carries:

- an **`open_item`** (bean `qou-rm47`, this audit) with the measured blast
  radius and the ~15 live `markov_z` / `y_lambda_wenzl_bridge` consumers;
- an **`n_coverage`** field recording that the registry's conventions were
  stated at `n = 3` and that `n > 3` is first covered here, with the
  block-annihilation counts (1/3, 7/11, 25/30, 70/77) and the verifying probe.

**`status` deliberately stays `"agreed"`.** In this schema `status` means
`definitional_convention == production_convention`, and for binding both are C
— there is no definitional-vs-production mismatch, which is what `"disputed"`
denotes (R8). What this audit opens is the *definitional choice itself*, which
the schema expresses through `open_item`, not through `status`. Setting
`"disputed"` would have been the more dramatic edit and the wrong one: R8 emits
a warning for a `"disputed"` channel whose two conventions agree, and it would
have misrepresented the finding as a wiring inconsistency rather than a
question about which fibre binding traces.

`trace_convention_registry_validate.py --lint-docs --selftest` → **PASS
(0 errors, 21 warnings)**; all 21 warnings are pre-existing R5
undeclared-convention notices on unrelated Borromean tracers, and all three
selftest regression cases (RC1–RC3) are caught.
