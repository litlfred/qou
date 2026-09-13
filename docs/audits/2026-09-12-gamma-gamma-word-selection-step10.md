# γγ word selection, step 10 — the diproton response in closed form, and the order correction it forces

Bean `qou-ales`. Branch `claude/ales-step9-diproton-order-2026-09-12`, PR #7233.

Steps 6–8 settled *which* bond the owner's adopted reading-3 confinement SDP selects on the
`H₆` interface (`G³ = (σ₂σ₃⁻¹)³`) and *why* its unbinding is consistent with the recorded
single-crossing obstruction. Step 9 derived the *order* of the magnitude and left exactly one
quantity measured — the trace-weighted response

    r = tr(W·D)/tr(W),    D = (G³ − 1)/h²,    W = the two free 11-letter nucleon words.

**Step 10 derives it.** And in deriving it, corrects step 9's headline order by two powers.

## 1. The derivation

The convention-D Markov trace on `H₆` was evaluated **exactly over `ℚ(q)`** — every letter of
both nucleon words and of the bond, through the Hoefsmit seminormal representations, with the
convention-D weights `y_λ` solved symbolically. No numerics, no anchor, no census.

Convention D truncates to two rows, so `y_λ ≠ 0` on exactly four of the eleven blocks —
`(6), (5,1), (4,2), (3,3)` — which is step 6's support, re-derived here as a by-product. The
other seven contribute nothing and were not computed (they are the expensive ones: `(3,2,1)`
alone costs 89 s).

    tr_M(W)    = (q⁴+1)²·P(q)² / (16 q¹⁸ (q²+1)⁴)
    tr_M(W·G³) = (q⁴+1)²·P(q)·S(q) / (16 q²⁰ (q²+1)⁵)

    P(q) = q¹⁸ − 3q¹⁶ + 7q¹⁴ − 8q¹² + 10q¹⁰ − 9q⁸ + 10q⁶ − 6q⁴ + 3q² − 1
    S(q) = 2q²² − 6q²⁰ + 14q¹⁸ − 22q¹⁶ + 33q¹⁴ − 32q¹² + 34q¹⁰ − 28q⁸ + 21q⁶ − 11q⁴ + 4q² − 1

The free trace is a **perfect square**: `tr_M(W) = tr_M(p)²` with

    tr_M(p) = (q⁴+1)·P(q) / (4 q⁹ (q²+1)²)

the single nucleon's `H₃` trace — disjoint-union multiplicativity of the Markov trace,
verified independently by evaluating the 11-letter element at `n = 3` (symbolic deviation `0`).
That is why `P` is a *nucleon* polynomial rather than a two-body one.

Dividing and subtracting one:

    r(q) = (q² − 1)²·(q⁴ + q² + 1)·R(q) / ((q² + 1)·P(q)),
    R(q) = q¹⁰ − q⁸ + 4q⁶ − 4q⁴ + 2q² − 1.

## 2. THE CORRECTION: the magnitude is `Θ(h⁴)`, not `Θ(h²)`

`(q² − 1)² = q²h²`, so **`r` itself carries a factor `h²`**:

    r(q) = h²·c(q),    c(q) = q²(q⁴ + q² + 1)R(q) / ((q² + 1)P(q)),    c(q₀) = 0.5537296922

and therefore

    μ − 1 = h²·r = h⁴·c(q),

so `|B| = Θ(h⁴)`. Step 9's bracket theorem is **correct as proved** — `r` is a free positive
hypothesis in `binding_magnitude_second_order`, so nothing proved there was wrong — but its
*stated order* was two powers too weak, and in exactly the place step 9's own correction
looked and drew the wrong conclusion. That correction's closing clause read:

> The interface ratio is controlled by the matrix, since `tr(W·D)` carries no such
> cancellation — so checking the order on characters gives the wrong answer for the binding.

**The second half is false.** `tr(W·D)` does carry a cancellation. The docstring of
`bond_character_deviation` in `DiprotonSecondOrder.lean` has been corrected in place rather
than deleted, so the wrong claim and its refutation sit together.

### Three distinct orders, and why conflating any two of them misleads

| quantity | order in `h` | source |
|---|---|---|
| the bond's **matrix** deviation `G³ − 1` | `h²` | step 4, `vtx_three_sub_one` (proved) |
| the bond's own **character** deviation `χ_(2,1)(V³) − 2` | `h⁴` | step 9, `bond_character_deviation` (proved) |
| a **single block's** mixed response `(χ_λ(WG³) − χ_λ(W))/h²` | `h¹` | measured: one factor `q² − 1`, on each of `(5,1)`, `(4,2)`, `(3,3)` |
| the **`y`-weighted** response `r` | `h²` | measured: order 2 in `q² − 1` |
| hence the **ratio** `μ − 1` | `h⁴` | |

The `h⁴` of the ratio and the `h⁴` of the bond's own character are **not the same fact**. The
bond's character deviates at `h⁴` because `tr D = −3h² − h⁴` is itself `O(h²)`. The ratio
deviates at `h⁴` because each block's mixed response carries one factor of `q² − 1` and the
`y`-weighted sum carries a second. Different cancellations; they agree by arithmetic. A reader
who checks the order on the bond's character alone gets the right number for the wrong reason,
and a reader who checks it per block gets `h³` for the ratio and is simply wrong.

The `(6)` block contributes nothing at all: the bond acts as the identity there
(`trivChar_eq_one`), so its response is identically zero.

## 3. What is now proved, and what the ceiling costs

`QOU/Mass/DiprotonResponseClosedForm.lean` — 24 declarations, `lean`-direct
`-DautoImplicit=false -s 65536` **exit 0, zero warnings**, `#print axioms` on every
declaration shows only `propext / Classical.choice / Quot.sound`, **no `sorryAx`**.

Positivity is the pleasant surprise. Re-expanded at `q = 1 + t`, **every** coefficient is
non-negative:

    P(1+t) = 4 + 42t + 217t² + … + t¹⁸                        (`nucleonPoly_shifted`)
    R(1+t) = 1 + 14t + 55t² + … + t¹⁰                         (`responsePoly_shifted`)
    (q²+1)P − q²(q⁴+q²+1)R = 5 + 38t + 167t² + … + t²⁰        (`coeff_gap_shifted`)

so `0 < c(q) ≤ 1` for **every** `q ≥ 1`, with no interval hypothesis
(`responseCoeff_pos`, `responseCoeff_le_one`). Consequences:

* **`diproton_unbound_of_response_closed_form`** — for **every** `q > 1` the γγ-selected
  diproton is unbound. Derived: `c > 0` on the whole ray forces `μ > 1`, and step 8's log law
  turns that into `B < 0`. Nothing measured enters. Step 8 had the sign as a hypothesis on a
  measured ratio; it is now a theorem about the ray.
* **`binding_magnitude_fourth_order`** — step 9's bracket at the derived response, both ends
  carrying `h⁴`.
* **`binding_ceiling_on_interval`** — on `1 < q ≤ 23/20`, `|B| ≤ α/100`, from `h⁴ ≤ 1/100`
  (the interval) and `c ≤ 1` (the polynomial gap). At the pin `α/100 = 42.275` keV against the
  actual `4.469` keV.

That last one is the accounting change worth stating plainly. Step 9's ceiling was `α·r/10 =
10.231` keV and **needed a measured `r`**. The new ceiling is `α/100` and needs **nothing** —
`α = m_e c_q² ℏ_q/(1 − ℏ_q²)` is a closed form in `q` and the CAL-1 electron mass. So the keV
scale of the diproton channel is now forced by the deformation alone, with no input beyond the
calibration triple and the word selection.

## 4. The probe

`computations/probes/diproton_response_closed_form_probe.py` — **11/11**, wall 92 s.

Four **exact symbolic identities**, each deviation `0` (not a tolerance):

| identity | what it pins |
|---|---|
| `r − respPP(q)` | the Lean closed form *is* the computed trace ratio |
| `r − h²·responseCoeff(q)` | the `Θ(h⁴)` correction |
| `tr_M(W) − nucleonTrace(q)²` | disjoint-union multiplicativity |
| `tr_M,H₃(p) − nucleonTrace(q)` | the `H₃` trace of the 11-letter element |

plus, numerically at the proton pin (60 dps):

| quantity | value |
|---|---|
| `h²` | `0.043706208532521989402` |
| `h⁴` | `0.0019102326642882979503` |
| `c(q₀)` | `0.55372969216497729153` |
| `r(q₀) = h²c` | `0.024201425396411705082` |
| `μ − 1 = h⁴c` | `0.0010577525451598436344` |
| step-3 witness ratio | `1.0010577525451598436` — deviation **4.2e−60** |
| `α = 𝔈₀^full` | `4.227483355629` MeV |
| `\|B\|` | `4.46926800571` keV (step-3: identical) |
| proved bracket | `[4.466906397, 4.471631279]` keV |
| derived ceiling `α/100` | `42.27483356` keV |
| step-9 ceiling `α r/10` | `10.2311123` keV — *needed a measured `r`* |

`c` is evaluated twice — once by exact rational substitution in sympy and once by a direct
mpmath transcription of the same closed form — so the transcription into Lean is checked, not
only the arithmetic. Deviation `0.0`.

## 5. What remains a hypothesis

Exactly one thing: `ResponseClosedForm`, the statement that the `H₆` convention-D Markov trace
of these words **is** the rational function above. That is a claim about the Hoefsmit /
branching machinery, not about the deformation, and it is verified by the probe against two
independent code paths — the symbolic `ℚ(q)` path here and step 3's mpmath seminormal path,
agreeing to `4.2e−60`. It is not proved in Lean, and formalising it would mean formalising the
seminormal representations of `H₆`. Same epistemic position as step 6's `InterfaceBranching`.

## 6. Scope — what this is NOT

* The **word** is step 3's: the canonical 11-letter nucleon element on generators `(0,1)` and
  `(3,4)` with the **colour-blind** `−h/2` interface letters, plus the bond on `(2,3)`. The
  colour-**weighted** `−h(1/2 − δ/4)` variant is a different element and was not computed.
* The **`4.469` keV is not offered as a prediction.** It is what this word and this bond give
  under the log law. The comparison to a measured diproton is not made here.
* The **dineutron channel** and the `p`–`n` asymmetry are untouched.
* `m > 3` bonds, `k > 10` candidates, and the `θ/π` rationality question are all unchanged.

## 7. A by-product: a red probe on `main`, not this arc's

While cross-checking the nucleon trace, `computations/markov/assembly_chain_11_letter_recompute_probe.py`
was found **red on `main`: 3/7**. Its hardcoded `LIVE` producer values (`tr_M(p) = 1.145759692…`,
`tr_M(n) = 0.987743688…`) disagree with what its own recomputation now returns (`0.629328402…`,
`0.475133517…`) by 45 % and 52 %.

This is **not** a machinery regression and **not** caused by this branch. Commit `7db032fb48`
(*"atom_braid_word_3A emits beta_Bor — the intra word was not the object its own comment
named"*) changed the nucleon element, which changed its trace; the probe's literals and the
eight committed witnesses that carry `1.145759692…` predate it. Draining that is a producer
re-run across those witnesses and is **not** in scope here — filed as its own bean, not fixed.

The relevant point for *this* record: the word step 10 computes on is the **post-fix** one, and
it opens with `β_Bor = (σ₀σ₁⁻¹)³` — the γγ Borromean word this whole arc selects. The nucleon
word and the bond are now the same kind of object.
