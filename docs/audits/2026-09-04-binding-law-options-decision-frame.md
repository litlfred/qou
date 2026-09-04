# `B = scale · Δtr` cannot remain the stated law — a decision frame for the owner

**Date:** 2026-09-04 · **Branch:** `claude/q407-self-assuming-projections-2026-08-21`
**Beans:** `qou-n9qf` (closed form + full-table scan), `gm4q` (open since 2026-06-28:
"binding energy scales exponentially to physically absurd values instead of
saturating"), `qou-bmz8` (ℓ¹ ceiling / deciding test), `qou-fvzm` (row cap)
**Producers:** `computations/qbeta/qbeta_binding_law_options_probe.py` (10/10),
`content/quantum-observable-universe/lean/QOU/Hecke/BindingExtensivity.lean` (6 decls, sorry-free),
`qbeta_no_regime_of_validity_probe.py` (5/5), `qbeta_full_ame_scan_probe.py` (6/6),
`qbeta_bond_factors_derived_probe.py` (7/7)
**Status:** ✅ **DECIDED 2026-09-04.** Owner ruling: **Option B, with the Option C
framing, and the 2.656 factor stated as open.** The retraction sweep across every
surface stating `B = Q_β·Δtr` is tracked at `qou-2pnv` and has not yet run.

> **🛑 One claim in this note is RETRACTED, and a second is demoted — see §7,
> added after the ruling.** The p-p/n-n bond asymmetry was read as "the sign
> Coulomb repulsion would give ... a prediction, not a fit". True as algebra,
> **wrong as evidence**: aggregated it pushes the wrong way, and layout-free bond
> counting beats every isospin-resolved variant. And the "strongest lead" named
> in avenue 2 is wrong by 4× in correlation — the dominant missing term is the
> **symmetry energy**, not the surface term.

---

## 0. The question, in one paragraph

The corpus states the nuclear binding law as

```
B(Z,N) = Q_β · ( tr_M(β_free) − tr_M(β_atom) )        Q_β = 0.78233340931 MeV
```

This note asks whether that should remain the stated law; what the options are
if not; whether the scale is *knot dependent*; and what stays open. The short
answers: **no**, it is refuted at every scale; **the replacement is already in
the repo and is the log of the same derived numbers**; the scale is **not** knot
dependent, for three reasons of increasing finality; and the single largest open
item is one dimensionless factor of **2.656**, not a shape failure.

---

## 1. What is settled, and what is not

### 1.1 The algebra is not in question

The closed form derived this arc (`qbeta_bond_factors_derived_probe.py`,
`qbeta_mixed_chain_closed_form_probe.py`) has **zero fitted constants** and
reproduces the direct Markov trace to `1e-35`:

```
t_p  = (q²²+q²⁰+2q¹⁸+2q¹⁶+3q¹⁴+2q¹²+q¹⁰−q⁸−q⁴−q²−1) / (4q⁹(q²+1)²)  = 1.1457596925
t_n  = (q¹⁸−q¹⁶+2q¹⁴−2q¹²+4q¹⁰−3q⁸+3q⁶−2q⁴+q²−1)   / (4q⁹)          = 0.9877436881
b_pp = q³/(q²+1) = z                                                 = 0.6126880371
b_pn = (q¹⁰−2q⁹+7q⁸−2q⁶+4q⁵+4q⁴+q²−2q+1) / (12q⁵(q²+1))              = 0.5082297894
b_nn = 1/(q³+q)                                                      = 0.4036277384

tr_M(β_free) = t_p^Z · t_n^N
tr_M(β_atom) = t_p^Z · t_n^N · b_pp^(Z−1) · b_pn^[Z,N≥1] · b_nn^(N−1)
```

Three of the five constants collapse to closed identities exactly (`b_pp − z = 0`,
`b_pp/b_nn − q⁴ = 0`, `r_previous − t_p·z = 0`). **Nothing below touches any of
this.** What is refuted is a physical *ansatz* laid on top of it.

### 1.2 The obstruction is algebraic, not empirical

`tr_M` is **multiplicative** along the chain — the closed form is a product.
Binding energy is **extensive** — a sum over bonds. A constant times a product is
still a product, so

> `B = s · Δtr` asks an exponential to be a line.

The failure is therefore not that `Q_β` is mis-calibrated. It is that **no scale
exists**. Measured over the 2548 AME2020 nuclides whose binding energy is
*measured* rather than extrapolated, at the law's own **optimal** scale:

| | p5–p95 spread | full range |
|---|---:|---:|
| `B = s · Δtr` at optimal `s = 1.2219 MeV` | **1592 ×** | 4.21 decades |

Two worked points, both under the corpus `Q_β`:

| nuclide | `B` measured | `Q_β · Δtr` | |
|---|---:|---:|---|
| ⁵⁶Fe | 492.25 MeV | 18.58 MeV | 0.038 × — under by 26× |
| ²¹⁰Bi | 1644.8 MeV | 13 121 MeV | **7.98 ×** |
| ²³⁸U | 1801.7 MeV | 35 323 MeV | **19.6 ×** |

The deficit **changes sign** near `A ≈ 150` — undershoot below, overshoot above —
and 46 % of the full table is overshot. The *existence* of that crossover is
structural (an exponential and a line cross exactly once); its *location* is not,
moving ~40 mass units per decade of scale. See
`qbeta_no_regime_of_validity_probe.py`.

> **A note on `gm4q`.** That bean reports `8.25 × 10¹³` for ²¹⁰Bi from the
> **generator-volume** decomposition — a different pipeline from the Markov
> trace, and the numbers are not comparable (13 121 here). The *symptom* is the
> same and this note explains it: both pipelines multiply per-nucleon factors,
> and a product cannot saturate. The magnitudes differ because the factors do.

---

## 2. The options

### Option A — keep `B = Q_β · Δtr` as the stated law

| | |
|---|---|
| **Pros** | No retraction cascade. The law is wired through content blocks, witnesses and chapters; `Q_β` has its CAL-2 proxy story. |
| **Cons** | The corpus would state something the corpus's own compute refutes at 1592× robust spread, with `²³⁸U` over-bound 19.6-fold. `gm4q` has been open on exactly this since June. |

**Not viable.** Listed for completeness: keeping it is a choice to publish a
refuted claim.

### Option B — state the **additive** law instead *(recommended)*

`log` is the unique map carrying multiplicative to additive, so the functional
with the right extensivity is **forced, not chosen**:

```
B(Z,N) = E_0 · log( tr_M(β_free) / tr_M(β_atom) )
       = E_0 · [ (Z−1)(−ln b_pp) + (−ln b_pn) + (N−1)(−ln b_nn) ]

−ln b_pp = 0.489899   −ln b_pn = 0.676822   −ln b_nn = 0.907262
E_0 = m_e / (q₀(q₀−1)) = 4.185981 MeV      (closed substrate expression)
```

The `t_p^Z t_n^N` free factor cancels in the **ratio**. That is the whole
mechanism: the difference is exponential, the ratio's log is linear.

| | measured nuclides (n = 2548) |
|---|---|
| **p5–p95 spread** | **1.225 ×** (vs 1592 × — a **1300-fold** gain) |
| full range | 1.008 decades (vs 4.21) |
| band medians, A<40 → A>240 | 2.61 → 2.41 — **no drift** |
| ²H | over-bound 1.27× |
| ⁴He | under-bound 3.26× |
| ⁵⁶Fe | under-bound 3.00× |

**Pros**

- **The gain comes from the functional, not a constant.** Both laws consume the
  *same* derived `b_pp`, `b_pn`, `b_nn`. Nothing was added and nothing was fitted.
- **Linear in `Z` and `N` — it is the SEMF volume term**, with per-bond energies
  derived from the substrate.
- ~~**The p-p bond binds less than n-n**, the sign Coulomb repulsion would give —
  a prediction, not a fit.~~ 🛑 **RETRACTED 2026-09-04, §7.** The inequality is
  real; reading it as evidence is not.
- **It is already implemented**: `computations/binding_log_free_energy.py`, bean
  `lkpl`, completed 2026-06-23. Adoption is a *wiring* change. Its docstring
  quoted 0.57–2.36× on a small validation set; this is the first full-table scan,
  and the result is stronger than that range suggests.
- Flat band medians say the law is **structurally** extensive, not extensive by
  accident.

**Cons**

- **`E_0` is 2.656× low.** The best single additive scale is 11.119 MeV against
  the derived 4.186. One dimensionless number — but an unexplained one.
- **No surface, Coulomb, symmetry or pairing term.** Predicted `B/A` rises
  monotonically (2.17 → 3.11 MeV/nucleon from A=4 to A=238) and has **no peak**;
  the experimental curve peaks at A ≈ 62. The law is a *pure volume term*.
- **Unbound systems are outside it by construction.** With strictly positive bond
  energies it predicts ≈ `E_0 · 0.7A` for *any* configuration and cannot produce
  `B ≈ 0`. The full-range figure above is set by ⁵Be (`B = 0.09 MeV`,
  AME-**extrapolated**) and the ⁵H/⁶H/⁷H drip line. This is a **named**
  limitation, not noise — excluding extrapolated values takes the full range from
  2.51 decades to 1.01.
- The 3.00–3.01 ceiling across the iron peak, and ⁴He alone above it at 3.259,
  are unexplained.

### Option C — keep `Δtr`, but say what it is

`Δtr` is a perfectly good quantity; it is simply not an energy. In the
statistical-mechanics reading the closed form invites — `tr_M` as a partition
function `Z_q` — `−log(Z_atom/Z_free)` is a **free energy** and `Z_free − Z_atom`
is an unnormalised **overlap deficit**, which has no reason to be extensive.

**Pro:** costs nothing and is almost certainly the right framing.
**Con:** it is a rider on Option B, not an alternative to it. On its own it
leaves the corpus with no binding law.

### Option D — withdraw the binding claim entirely

**Pro:** maximally defensible; nothing left to attack.
**Con:** discards a law that lands 90 % of measured nuclides inside a 1.225×
band with **zero fitted constants**. That is a real result and should not be
thrown away to avoid stating an open factor of 2.656.

---

## 3. Is the scale knot dependent?

The question is a good one, because the natural rescue is exactly a
knot-dependent scale, **derived rather than fitted**: `tr_M` is *not* a link
invariant, and the HOMFLY normalisation `μ^(n−1) · ν^(e)` — braid index `n`,
exponent sum `e` — is precisely a per-closure factor that the Markov moves force
on you. Three reasons it is unavailable here, in increasing order of finality.

### (a) There is no knot. `e` does not exist.

The atom object is **not in the image of** `ρ : B_n → H_n(q)`. `2A+1` of its
letters are weight-1 averages of `σ` and `σ⁻¹` (two `ud` pairs per nucleon, plus
one per interface):

```
σ − (h/2)·1        = (σ + σ⁻¹)/2
σ − h(½ − δ/4)·1   = (½ + δ/4)σ + (½ − δ/4)σ⁻¹
```

By linearity `tr_M` here is a weighted sum of `2^(2A+1)` link invariants — 2⁴¹⁷
for ²⁰⁸Pb — each branch carrying a **different** exponent sum. There is no writhe
to normalise by and no single knot for a scale to depend on. (Established
independently: `atom_braid_word_3A` docstring;
`docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md`, which also
measured all 32 branch closures of ²H to be non-hyperbolic with `Vol = 0`.)

### (b) Granting a normalisation anyway, the rate is wrong

A factor `μ^(3A−1)` has log-slope `3 ln μ` per nucleon — a fixed number. The
slope the data demands along `N = Z` is **−0.061868 per nucleon**:

| `μ` | `3·ln μ` per nucleon | ratio to required | sign |
|---|---:|---:|:--:|
| `z = q³/(q²+1)` | −1.46970 | **23.76 ×** | ✅ |
| `b_pn` | −2.03046 | 32.82 × | ✅ |
| `1/(q³+q)` | −2.72179 | 43.99 × | ✅ |
| `[2]_q = (q²+1)/q` | +2.09574 | 33.87 × | ❌ |
| `q` | +0.31302 | 5.06 × | ❌ |

The closest **right-signed** substrate constant is the Markov parameter itself
and is 23.8× too steep; the closest **in magnitude** pushes the correction the
wrong way. No substrate constant is close on both counts.

### (c) The scale that *would* work is the algebra's own output, inverted

Regressing `ln(B/Δtr)` on `(Z, N)` over the measured nuclides returns

```
c_Z = −0.109942     −ln t_p = −0.136068     (19 % apart)
c_N = +0.012161     −ln t_n = +0.012332     (1.4 % apart)
```

A scale of shape `t_p^−Z t_n^−N` cancels `t_p^Z t_n^N` exactly and leaves the
scale carrying all of the physics and the trace carrying none. That is the
definition of a fit. It is recorded here **to be refused**, not adopted. (The
coefficients are not tighter than 19 % because `ln B ≈ ln(8.5A)` is not linear in
`(Z,N)` and contaminates both.)

### The sense in which knot dependence *is* already present — and derived

Worth separating out, because it is the steelman of the question and the answer
is affirmative. In the additive law the **scale stays one constant** `E_0`, and
the *bond energies* differ by bond type:

```
−ln b_pp = 0.4899      −ln b_pn = 0.6768      −ln b_nn = 0.9073
```

Bond type is a **colouring of the link**. So the topology-dependence the question
is reaching for is already carried — by the algebra, derived, in the right place
— and it does not need, and cannot use, a knot-dependent scale on top.

---

## 4. Recommendation

**Option B, with the Option C framing, and the 2.656 factor stated as open.**

Concretely: state the law as `B = E_0 · log(tr_M(β_free)/tr_M(β_atom))`; describe
`Δtr` as an overlap deficit rather than an energy; and say plainly that the
derived `E_0` is 2.656× below the best single scale, that the law is a pure
volume term with no surface/Coulomb/symmetry/pairing structure, and that unbound
systems lie outside it.

That is a **weaker headline** than the corpus currently carries and a much
stronger claim, because every number in it is derived and the failure modes are
named. The retraction discipline applies: the change is not landed until it
reaches every surface stating `B = Q_β · Δtr` — not just this note.

---

## 5. Avenues still open

Each with the measurement that would settle it. Anti-fit discipline applies
throughout: the numbers below are targets a future derivation is checked
**against**, never criteria to search **on**.

1. **The factor 2.656.** Derive the volume-energy conversion without routing
   through `m_e`. *Settled by:* a closed substrate expression that lands on
   11.119 MeV, produced before it is compared. *Falsified by:* any derivation
   that reproduces `E_0 = 4.186` and is right — which would mean the residual
   2.656 belongs to the bond factors, not the scale.

2. **The missing surface term.** ⚠️ **Demoted 2026-09-04 (§7): correlation
   −0.178, against −0.804 for the symmetry energy. Not the strongest lead.** The canonical atom wires an
   `A−1` **chain**: a 1-D edge set with coordination 2. Real nuclei are 3-D with
   saturating coordination, and `A^{2/3}` is exactly what a chain lacks. This is
   the "edge-set / fractional-occupancy" question already named at
   `derived_bond_graph_binding.py` and the 2026-06-10 bond-graph audit (static
   integer graphs refuted). *Settled by:* an edge set derived from the braid
   geometry rather than assumed, which adds surface behaviour with **no new
   constant**. *Falsified by:* the residual `B_exp/B_pred` failing to have the
   shape of `a_S A^(−1/3) + a_C Z²/A^(4/3) + a_A (N−Z)²/A²` — a **shape** test
   that needs no scale, and so is not a fit.

3. **The iron-peak ceiling.** `B_exp/B_pred` maxes at 3.00–3.01 across Si-28,
   S-32, Ar-36, Ca-40, Cr-50, Fe-52/54, Co-55, Ni-56/57/58 — the α-conjugate
   `N = Z` chain — with ⁴He alone above at 3.259. Is that ceiling exactly 3?
   *Settled by:* an argument that the ratio is bounded, or a counterexample above
   3.26.

4. **Make the object a braid.** If a crossing convention put the atom word inside
   `ρ(B_n)`, `tr_M` would become an honest link invariant and a genuine
   knot-dependent normalisation would open — reason (a) above is the *only* one
   of the three that is structural. `sign-only-crossings` (one of the four
   χ-witness conventions, `qbeta_chi_witness_convention_split_probe.py`) replaces
   the averages by definite signs and is the candidate. *Settled by:* checking
   whether that convention yields an object in `ρ(B_n)` — a decidable question,
   not a search. Note reason (b) survives it: the rate would still be wrong.

5. **Unbound systems.** The law cannot produce `B ≈ 0`. Needs either a competing
   repulsive term or an explicit binding threshold. *Settled by:* deriving a
   positive-energy contribution from the same algebra, or accepting the domain
   restriction explicitly.

6. **Formalisation — ✅ done, `QOU/Hecke/BindingExtensivity.lean`.** Both
   statements are proved, sorry-free, on `[propext, Classical.choice,
   Quot.sound]`:
   - `exists_pow_gt_linear` — for `1 < t`, `s > 0` and **any** `C`, some `n` has
     `C·n < s·t^n`. No constant scale makes an exponential linear, which is the
     refutation of §1.2 in its entirety.
   - `linear_le_bondSum` / `bondSum_le_linear` — the bond sum is pinned between
     two lines through the origin in `A−1`, for every `(Z,N)`. That is what
     extensive means, and it is §2.
   - `additive_is_linear_multiplicative_is_not` combines them: the two laws are
     not competing fits of one shape, they are different shapes, and only one of
     them can be a binding energy.

   Everything is proved for an arbitrary base and arbitrary bond energies, so no
   substrate constant enters. What is **measurement and explicitly not proved**
   there: `t_p = 1.1458 > 1` and the three bond energies being positive. Those
   are the theorems' hypotheses, established at 30 dps by the probe. Verified
   `lean`-direct, exit 0 in 4.6 s.

---

## 6. What this note does **not** touch

`Δtr(Z,N)` remains closed-form, derived with zero fitted constants, agreeing with
the direct trace to `1e-35`; its bond factors are exactly what the surviving law
consumes. The row cap (`qou-fvzm`), the ℓ¹ ceiling and the interface deciding
test (`qou-bmz8`) are unaffected — they said the missing piece is *not* a
reweighting, *not* reachable by larger `N`, and *not* in the interface
subalgebra. This note adds the fourth: it is not in the **scale** either. It is
in the **map from the trace to MeV**, and that map is `log`.

---

### Reproducing

```sh
python3 computations/qbeta/qbeta_binding_law_options_probe.py     # 10/10
python3 computations/qbeta/qbeta_no_regime_of_validity_probe.py   #  5/5
python3 computations/qbeta/qbeta_full_ame_scan_probe.py           #  6/6
python3 computations/qbeta/qbeta_bond_factors_derived_probe.py    #  7/7
python3 scripts/probe-float64-guard.py --diff <files>             # clean

# Lean, lean-direct against the restored root cache (never `lake build` on a
# restored tree -- it evicts the cache; see .claude/skills/local/lean-environment-setup.md)
export PATH="$HOME/.elan/bin:$PATH"
export LEAN_PATH=$(for d in .lake/packages/*/.lake/build/lib/lean; do printf "%s:" "$(realpath $d)"; done)
cd content/quantum-observable-universe/lean && lean QOU/Hecke/BindingExtensivity.lean   # exit 0
```

Witness: `computations/qbeta/qbeta-binding-law-options.witness.json`.

---

## 7. Post-ruling: the tower question, and the roast

Added 2026-09-04 after the owner adopted Option B. Producer:
`computations/qbeta/qbeta_tower_log_z_and_roast_probe.py` (9/9), witness
`qbeta-tower-log-z-and-roast.witness.json`. Bean `qou-q7ga`.

### 7.1 Option B *is* the tower's own additive counter — the answer is `log_z`

The tower is defined by the Markov relation `tr_{n+1}(x·σ_n) = z·tr_n(x)`:
adding a strand multiplies the trace by exactly one `z`. So the natural additive
invariant is the **Markov weight**

```
ν(x) := log_z tr_M(x),        ν(x·σ_n) = ν(x) + 1
```

and Option B is precisely its **archimedean realization at `q = q₀`**:

```
B = E_0·|ln z|·[ ν(atom) − ν(free) ]          E_0·|ln z| = 2.0507 MeV
```

The measured Markov weights of the three bonds are `1`, `1.3816`, `1.8519`, and
the first is **exactly 1** because `b_pp = z` is a derived identity — a
proton-proton bond *is* one Markov reduction, on the nose.

### 7.2 Order 0 is `q → 1`, and there every factor collapses to `z`

Verified symbolically: **all five closed-form factors equal exactly `1/2` at
`q = 1`** — `t_p`, `t_n`, `b_pp`, `b_pn`, `b_nn`, and `z(1) = 1/2`. The Hecke
algebra degenerates to `ℂ[S_n]` and `ν` becomes an exact integer **bond count**:

```
B = E_0·ln2·(A − 1)                                        [order 0]
```

Expanding in `e = q − 1` gives the deformation, with a clean pattern:

| factor | expansion | first-order |
|---|---|---:|
| `b_pp` | `1/2 + e + O(e²)` | **+1** |
| `b_pn` | `1/2 + 0·e + O(e²)` | **0** |
| `b_nn` | `1/2 − e + O(e²)` | **−1** |

The p-n interface has **no first-order term** and the like-species bonds split
symmetrically about `z`. In bond energies `−ln b = ln2 ∓ 2e`, so

```
B = E_0·[ ln2·(A − 1) + 2(q₀−1)·(N − Z) ] + O(e²)          [order 1]
```

a volume term plus an asymmetry linear in `N − Z`, good to 0.6–3.4 % against the
exact bond energies. **So yes: there is a `log_q` form naturally there, it is
`log_z`, its order-0 realization is bond counting, and the deformation is a
series in `q − 1` whose first term is the isospin splitting.**

**And Option C is the same object through a saturating map.** Exactly,
`Δtr/tr_free = 1 − e^{−S}` with `S` Option B's bond sum. That gap is `7.7e−4` by
**A = 11**, `1.5e−12` by A = 40, and below machine precision by A ≈ 100. So above
A ≈ 11, **`Δtr` does not merely mis-scale the binding energy — it does not
contain it**; what is left is the free factor `t_p^Z t_n^N`. That is the reason
no scale works, stated more sharply than §1.2 managed.

### 7.3 The roast — three results against the law

**(a) The asymmetry has the wrong sign.** Derived `κ = +2e = +0.2200`. Scanning
`κ` in `B ~ ln2(A−1) + κ(N−Z)` over 2548 measured nuclides puts the optimum at
**`κ ≈ −0.15`**. Adding the derived term makes the spread *worse*.

**(b) The bond count is the entire content.** Scale-free comparators:

| edge set | p25–p75 | p5–p95 | full |
|---|---:|---:|---:|
| segregated `p…p n…n` (`atom_braid_word_3A`) | 1.0953 | 1.2250 | 10.18 |
| alternating `p n p n …` (`build_atom_nf_exact`) | 1.0972 | 1.2323 | 10.40 |
| all-pairs, renormalised to `A−1` | 1.0958 | 1.2262 | 9.92 |
| **bond COUNT only, layout-free** | **1.0843** | **1.1809** | **8.17** |

The three edge sets agree to 0.6 %, and all three lose to counting. **The
q-deformation's contribution to the binding law is net-negative.** What Option B
earns is *"the algebra produces an extensive quantity"* — which Option A did not
— and, on this corpus, not the specific bond energies.

*Two things this does not refute:* the closed form (the `q=1` collapse and
`b_pp = z` are exact identities of it), and the possibility that the deformation
is right but read through the wrong observable. It does refute the edge set as
the culprit — see (c).

**(c) So the ordering gap `qou-48is` barely touches `B`.** `tr_M` moves 20–36 %
across orderings of the same `(Z,N)` — that bean's measurement stands — but the
three edge sets above land within 0.6 %, and the first-order asymmetry
coefficient is **exactly `N − Z` for all three**. The layout moves `tr_M`; it
does not move `B`. (Worth recording separately: the two canonical producers
genuinely disagree — `atom_braid_word_3A` is segregated, `build_atom_nf_exact`
alternating. Live for any `tr_M` consumer, near-invisible to `B`.)

**(d) The missing term is the symmetry energy.** Correlation of the residual
`B_exp/(E_0·S)` against the SEMF shapes:

| shape | correlation |
|---|---:|
| `(N−Z)²/A²` [asymmetry] | **−0.804** |
| `A^{−1/3}` [surface] | −0.178 |
| `Z²/A^{4/3}` [Coulomb] | −0.044 |

Avenue 2 named the surface term / edge set as "the strongest lead". Wrong by 4×.
🛑 **CORRECTED 2026-09-04, same day.** `qou-ubsl` is **completed and closed**,
and I promoted it off its title without reading its body. It is closed twice
over, and the first reason is *this arc's own Lean result*: the trace annihilates
every partition with `ℓ(λ) > 2` (`QOU/Hecke/RowCap.lean`), so the SU(4)-
distinguishing shapes — which need up to four rows — carry **zero weight**; and
on the two-row shapes that survive, `C₂^{GL(4)} − C₂^{GL(2)} = 2n`, a constant at
fixed strand number, so the SU(4) label collapses to the SU(2) isospin the trace
already carries. Its own text also concedes that the Casimir yields `(N−Z)²`,
not `(N−Z)²/A` — the `1/A` is Fermi-gas level density, a separate dynamical
input this framework does not have.

**So the measurement stands and the inference does not.** The residual's
dominant shape IS the symmetry energy (−0.804). What is *not* true is that this
points at a live route: the natural algebraic source is structurally forbidden.
That is worse news than "top lead", not better — the symmetry energy is a named
gap with **no available route**, and the tractable open item is back to the
2.656 scale factor (`qou-59j5`).

What survives of the sharpening: the law *already has* an `(N−Z)` term with the
opposite sign, so any future route must explain that, not merely add a symmetry
term. But there is currently no route to explain it with.

### 7.4 Where that leaves the avenues

| # | avenue | status after the roast |
|---|---|---|
| 1 | the 2.656 factor | **the tractable lead** — the single named open number, `qou-59j5` |
| 2 | surface term / edge set | **demoted** — corr −0.178, and three edge sets agree to 0.6 % |
| 3 | iron-peak ceiling 3.00 | unchanged |
| 4 | make the object a braid | unchanged; reason (b) of §3 still survives it |
| 5 | unbound systems | unchanged |
| 6 | formalisation | ✅ done |
| **7** | **symmetry energy, wrong-signed** | **named gap, NO route** — the residual's dominant shape (−0.804), but the isospin/SU(4) source is closed (`qou-ubsl`, completed). `qou-q7ga` |
