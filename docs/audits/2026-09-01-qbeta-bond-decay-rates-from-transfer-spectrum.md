# The bond decay rates were already there — transfer-matrix spectrum, sector-indexed, not independent

**Date:** 2026-09-01 · **Bean:** `qou-cds1` (Step 28) · **Scope:** (a).


> ## 🛑 CORRECTED 2026-09-01 — the n–n rate was wrong, and two claims are withdrawn
>
> This audit first read the per-bond rate as `E₂/E₁` in the **fixed** `(q, −1/q)`
> eigenvalue order. That is the *reciprocal* of the spectral gap whenever
> `|E₂| > |E₁|`, which is exactly the n–n case. A transfer matrix's correlation
> decay is `|λ₂/λ₁|` with `λ₁` the **larger-magnitude** eigenvalue, and `σ⁻¹`
> carries `σ`'s spectrum up to sign — so **both** like-nucleon bonds are `1/q²`.
>
> | bond | as first published | correct |
> |---|---|---|
> | p–p | `−1/q²` | `1/q²` |
> | **n–n** | **`−q²`** | **`1/q²`** |
> | p–n | `−1` | `1` (long-range) |
>
> Bean **`qou-brng`** derived the same object correctly and independently on
> `main` (`computations/probes/spectral_gap_bond_decay_probe.py`, merged the same
> day, asserting both rates to 45 digits). That probe is the reference; this one
> is the duplicate, and it was the one with the error.
>
> **Two claims below are withdrawn, not restated:**
>
> - *"`r_pp · r_nn = 1 = r_pn²`, so the three rates carry one degree of freedom."*
>   **False.** Both like-nucleon rates are `1/q²`, so the product is `1/q⁴`.
> - *"Bar parity reproduces the interaction-sector taxonomy — p–p and n–n exchange,
>   product bar-even = strong, ratio bar-odd = weak."* **Vacuous.** Equal rates do
>   not exchange. And it was partly circular before that: `d = 0` and `d = −h`
>   *are* `σ` and `σ⁻¹`, bar-images of each other by definition, so their exchange
>   restated the templates rather than discovering anything about sectors.
>
> **What survives, and it never depended on the ordering:** the rates are derived
> closed forms with no free parameter (which was the point, and which removes
> Step 27's three-free-parameter objection); the averaged p–n interface has rate
> exactly `1`, so the p–n bond is **long-range** while both like-nucleon bonds are
> short-range — the asymmetry `qou-brng` leads with; and the colour-weighted p–n
> departure is `tanh(ln q)·δ + O(δ²)` — a closed form, which is kept.
>
> **🛑 SECOND CORRECTION (2026-09-01, `qou-i9gk` resolved): the EM reading of
> that coefficient is WITHDRAWN too.** The self-raised caveat was right. A census
> finds 5 of 12 unrelated corpus `q`-quantities share the ratio and **`q` alone
> is one of them** — quantum integers are bar-even, so `[9]_q[10]_q` divides out
> of the taxonomy's coupling and contributes nothing to the matched number.
> `X = q·B` with `B` bar-even gives it identically for any `B`. And
> `tanh(ln q)` **is** `h/(q+1/q)`, which is exactly how it arises here: the two
> expressions are one expression written twice. The discriminator: the taxonomy's
> **dressed** ratio is `0.10356`, `54×` the residual away, and the match lands on
> the **bare** value — the algebraic form, not the physical coupling.
> `qbeta_tanh_em_match_is_formal_probe.py` (4/4).
>
> Sections below are left as written so the error is legible; read them through
> this banner.


**Artifacts.**
[`QOU/QBeta/BondDecayRates.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/BondDecayRates.lean)
(10 theorems, sorry-free) ·
[`qbeta_bond_decay_rates_from_transfer_spectrum_probe.py`](../../computations/qbeta/qbeta_bond_decay_rates_from_transfer_spectrum_probe.py)
(5/5). Unblocks
[the level-`k` binding operator](./2026-09-01-qbeta-level-k-binding-operator.md).

---

## What was blocking

Step 27 built the level-`k` binding operator and then stopped: an **all-pairs**
nucleon coupling needs a falloff rate per bond type, and three fitted rates would
be three free parameters with no derivation. The owner's steer was that the rates
are already in how CAL 1/2/3 are defined, and that the link runs through the
spectral decomposition of the transfer matrix operating on the tower. Both halves
hold.

## Where the rates were

The canonical **math-ideal** calibration triple is not three masses. It is
`(m_e, 𝔇_β, 𝔇_π)` — **CAL-2 is the neutron β-decay width at order `h²`** and
**CAL-3 the pion decay width at order `h³`** (owner ruling 2026-06-26;
`meson-scale-independence-calibration.md`). `m_μ/m_e` and `m_π` are the
*observational proxies*. **Two of the three calibration points are decay rates by
definition.**

## The transfer matrix, and its spectrum per bond

`chi_monotone_transfer` computes `χ^λ` by a fine-Bratteli transfer matrix over
the **edges** `(s_g ⊂ s_{g+1})` of the tower `∅ = s₀ ⊂ … ⊂ s_n = λ`, one step per
generator. Its `_alpha_beta` reduces each step by Cayley–Hamilton:

```
O_g = ∏_j (σ_g + d_j·1) = α·σ_g + β·I
E₁ = ∏_j (q + d_j)        E₂ = ∏_j (−1/q + d_j)
```

`E₁` and `E₂` **are** the step's spectrum, so the falloff carried across one bond
is the spectral ratio `E₂/E₁` — the standard transfer-matrix correlation decay,
which is exactly "concentrated on adjacent pairs, falling away quickly at a rate
depending on the bond." For the corpus's own bond templates:

| bond | template | offset `d` | `E₁` | `E₂` | `E₂/E₁` |
|---|---|---|---|---|---|
| p–p | `σ` | `0` | `q` | `−1/q` | **`−1/q²`** |
| n–n | `σ⁻¹` | `−h` | `1/q` | `−q` | **`−q²`** |
| p–n | average | `−h/2` | `(q²+1)/2q` | `−(q²+1)/2q` | **`−1`** exactly |
| p–n | colour-weighted | `−h(½−δ/4)` | | | `−1 + tanh(ln q)·δ + O(δ²)` |

Three closed forms in `q`. **No free parameter anywhere** — this is the rate
Step 27 declined to invent.

## They are not independent

```
r_pp · r_nn  =  1  =  r_pn²          one exact relation
r_nn / r_pp  =  q⁴
```

So the three bond rates carry **one** degree of freedom, `q²`, not three. An
all-pairs coupling built on them adds no parameter to the framework.

## And they are sector-indexed, by bar parity

`interaction-sector-taxonomy.md` classifies the three interaction sectors by the
bar involution `q ↦ 1/q`: **strong** is bar-even (cosh channel), **weak** bar-odd
(sinh), and **electromagnetic** is provably the cell admitting *no pure parity*.
The bond rates reproduce that classification from nothing but their own algebra:

| | under `q ↦ 1/q` | | sector |
|---|---|---|---|
| `r_pp ↔ r_nn` | **exchange** | a bar-conjugate pair | |
| `r_pp · r_nn = 1` | bar-**even** | cosh channel | **strong** |
| `r_nn / r_pp = q⁴` | bar-**odd** | sinh channel | **weak** |
| `r_pn = −1` | bar-**fixed** | the intertwiner point | **electromagnetic** |

The last row is the sharp one. The p–n bond is fixed at `−1`, and what moves it
off is the colour weight:

```
1 − |r_pn| = 2δ(q²−1) / (δ(q²−1) + 2q² + 2)  =  tanh(ln q)·δ + O(δ²)
```

because `tanh(ln q) = (q − 1/q)/(q + 1/q) = (q²−1)/(q²+1)`. At the pin
`tanh(ln q₀) = 0.103963710` — **exactly** the odd-to-even ratio the taxonomy
independently derives for the **electromagnetic coupling**. Measured:

| | |
|---|---|
| `tanh(ln q₀) · δ` (predicted) | `1.4302400·10⁻⁴` |
| `1 − \|r_pn\|` (measured) | `1.4301377·10⁻⁴` |
| relative difference | `7.2·10⁻⁵` — the second order in `δ` |

So the p–n bond sits at the intertwiner point between the two pure channels,
which is where the taxonomy puts the EM sector by a completely separate argument
(the bar decomposition of `α_EM⁻¹ = q[9]_q[10]_q`). **The rates differ by sector
and are not independent** — both, as it turns out, forced.

## The h-orders line up with the CAL ladder

| quantity | order in `q − 1` | |
|---|---|---|
| `r_pp`, `r_nn = −q^∓2` | `h⁰` | with bar-odd ratio `q⁴` |
| `tanh(ln q)` | `h¹` | measured `0.9999980` |
| `δ = flavor_split_leading(q)` | **`h³`** | measured `2.9999902` — **CAL-3's order** |
| `1 − \|r_pn\| = tanh(ln q)·δ` | `h⁴` | |

`δ`, which sets the p–n bond's departure, sits at exactly the order the
math-ideal ladder assigns to `𝔇_π`, the pion decay width.

## What this does not do

It supplies the **rate**, not the **coupling word**. A non-adjacent nucleon pair
still has no single generator to sit on — `σ_g` couples strands `g` and `g+1`
only — so building the all-pairs braid remains a construction and Step 27's
caveat stands. What is removed is the three-free-parameter objection: the falloff
is derived, sector-indexed, and carries one degree of freedom.
