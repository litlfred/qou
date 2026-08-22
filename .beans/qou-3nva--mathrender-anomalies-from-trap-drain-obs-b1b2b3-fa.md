---
# qou-3nva
title: 'MATH/RENDER anomalies from trap-drain obs-b1/b2/b3: FALSE self-conjugacy (5,4,4,4,3) in double-magic-Ca40-diagram; q0 muon/proton pin straddle (flavor-split-substrate-proof, g-q-closed-form vs fine-structure-observation); P_isolation 0.13 vs 0.153; V_B/hbar_q^2 749.2 vs 746.4; CFL-gap self-contradiction; ''forbids beta decay'' wrong term; broken LaTeX pid/pia/lambdaL; frac denominator 1; = vs approx; RESOLVED status leaks; higgs-t28 uniqueness unsupported'
status: todo
type: task
created_at: 2026-08-15T11:29:23Z
updated_at: 2026-08-19T00:00:00Z
---

# RECONCILED AGAINST MAIN, 2026-08-19

The findings below were recorded 2026-08-15/16 by a fleet of audit agents.
`main` has since advanced ~846 commits. This pass re-located every item in the
tree **as it stands today**, re-verified every numeric claim with
`python3`/`mpmath` rather than trusting the record, and re-tagged each item.

**Counts — 201 discrete findings triaged**

| status | n | meaning |
|---|---:|---|
| **FIXED** | 0 | defect gone from the tree |
| **PARTLY ADDRESSED** | 1 | a sibling landed a real but partial fix; residue is still live |
| **WRONG WHEN RECORDED** | 2 | the finding was itself an error; retracted below with the correction |
| **RE-SCOPED** | 3 | the defect is live but the ledger mis-stated its nature or its extent |
| **LIVE — re-verified** | 62 | located verbatim AND independently re-checked (arithmetic recomputed / text re-read) |
| **LIVE — located** | 128 | located verbatim; ledger evidence accepted without independent re-derivation |
| **CHANGED** | 2 | content moved; finding needs restating against the new location |
| **NOT-FOUND** | 3 | could not locate; recorded as unresolved, not as fixed |

**Headline: nothing in this ledger has been fixed.** The four-day sibling
landing wave touched `computations/` (convention-C excision, the
anchor-corruption family `qou-m9xp` / `qou-cezp`) and left the **content**
side of every item here untouched. The two commits that do reach this
ledger's territory — `aad30399c` and `2aa5a8ba7` — re-scope the χ(A) = −6
*epistemic* claim and do **not** touch the χ inconsistency itself.

**Verification note.** Committer dates in this repo are rewritten by
rebase-merge (rule 8), so `git log --since` is useless for "was this touched
since the ledger?" — every content file appears touched. Every FIXED/LIVE
call below is made against the **current file contents**, read directly.

---

## FIXED

*(none)*

---

## PARTLY ADDRESSED

**A1. [q15/q08] χ(A) = −6 presented as derived from the axioms.**
Two commits landed on `main` after this ledger and address exactly the
epistemic half of this finding:

- `aad30399c` — *content(brings-surface): chi(A) = -6 is located by the
  chain, not derived from the axioms alone* (bean `qou-1tls`). Fixes
  `chi-minus-six-chain.md` ("The value χ(A) = −6 is derived, not assumed")
  and `brings-surface-example.md` ("χ(A) = −6 is forced by the lifting
  obstructions" two sentences before "Setting χ(V) = −6 yields g = 4").
- `2aa5a8ba7` — *content(information-theory): scope the chi(A) = -6 leg of
  the non-vanishing argument*, same defect inherited by
  `conj:qou-p-neq-np`.

**Residue is LIVE.** Neither commit reconciles the *value*. See L-V1 below —
the corpus still carries χ = 2, χ = 3 and χ = −6 for the same symbol, and
`why-b3.md:1` still opens "The Descartes condition χ(A) = −6 forces the
gauge group to be a quantum form of SU(2), **which has rank 2**" (rank 1 —
see L-V2).

---

## WRONG WHEN RECORDED — retracted, with the correction

**W1. [it-b3] "FALSE `sigma_i^{-1} = sigma_i` mod Hecke in q-game-of-life-proof". RETRACTED.**
`content/quantum-observable-universe/information-theory/q-game-of-life-proof.md`
carries no such claim, and did not on 2026-08-15 (`git log -S` shows the file
untouched since `230cdd113`). What it actually says, verbatim:

> the quadratic relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ gives the
> explicit inverse $\sigma_i^{-1} = \sigma_i - (q - q^{-1})\cdot 1$, so every
> $\sigma_i$ is a unit … The generators are *not* involutions at generic $q$:
> $\sigma_i^{-1} = \sigma_i$ holds precisely when $q = q^{-1}$, i.e. in the
> classical limit $q \to 1$.

That is the correct inverse (AGENTS.md §7a) **and** an explicit denial of the
involution. The recording agent appears to have grepped the string
`\sigma_i^{-1} = \sigma_i` out of the sentence that refutes it. The
*companion* finding on the same line of this ledger (q > 1 vs q > 1/φ²) is
real and is kept as L-V47.

**W2. [it-b0/b1] "info-causality frak-B register" defect. RETRACTED.**
`information-theory/information-causality-table-data.md:6` writes the
Bremermann bandwidth as `$\mathfrak{B}(q)$`. AGENTS.md §7aa assigns **fraktur
to physical observables: mass, energy, bandwidth, particles** — `𝔅` for
bandwidth is exactly the register the notation table prescribes. There is no
defect. The *other* half of that ledger line (`c ≈ 9.12` from the stale
1.1097 pin) is real and is kept as L-V9.

---

## RE-SCOPED — live, but the ledger mis-stated the defect

**R1. [q12/q00] "KNOWN-BAD q0 string `1.109978595554181`".**
The **string is not corrupted and the value is not wrong.** Solving the
canonical CAL-2 muon identity `m_μ/m_e = Vol(4₁)/ℏ_q²` with
`Vol(4₁) = 2·Cl₂(π/3)` and CODATA `m_μ/m_e = 206.7682830` gives

```
q₀(muon) = 1.109978595554180575281594…
```

so `1.109978595554181` is that value **correctly rounded to 16 digits**. Back-
substituting, it implies `m_μ/m_e = 206.768282999998…` — CODATA to 12 digits.
`tools/qou-substrate/python/qou_substrate/constants.py:170` says so in as many
words: *"old muon value was 1.10997859555418…"*.

The **real** defects, both live:

1. **Mislabelled precision.** Every occurrence is written
   `q_0 = 1.109978595554181\ldots` **(50 dps)** on a 16-digit number.
2. **Off-canon pin.** The live canonical pin is the *proton* one,
   `Q = 1.1099785827513808075916690956107688798744991218736`
   (`q_at()`, verified by running it). The muon value is 11.5 ppb away.
   AGENTS.md does preserve the *ideal* (muon-proxy) framing for prose while
   requiring the proton pin in *compute*, so the pin question in narrative
   blocks is a convention call, not an arithmetic error — but the "(50 dps)"
   label is a defect in every case.
3. **Extent was understated by 30×.** The ledger names it in
   `knot-particle-dictionary` L24 "and 2 more blocks". Measured today:
   **33 content files**, spanning `observations/`, `mass-theory/`,
   `knots-particles-confinement/`, `notation/`, `appendix-*`, plus
   `mass-theory/wigner-coefficient-derivation.lean:40,45`.

*(Separately noted, outside this ledger's scope: `computations/q-pinning-50-digit.witness.json`
carries `q = 1.10997859555733471989…`, which matches neither `q_at()` nor
`q_muon_at()` — 2.8e-12 off the muon solve — while its own description claims
the m_p/m_e proton identity. That is the `qou-m9xp` / `qou-cezp` anchor family,
not a content-side item.)*

**R2. [q10] glossary-q-bit `η_{φ²} = 0.327`.** Correct as a defect —
`(2q−1)/q³` at `q = φ² = 2.618033989` is **0.23606798**, recomputed. But it is
live in **two** files, not one: `glossary/glossary-q-bit.md:19` and
`information-theory/operational-entropy-properties.md:49` (same row, same
wrong 0.327).

**R3. [q11] "the 1.1097 mis-rounding is baked into 4 data tables."** Three of
the four reproduce under `q = 1.1097` as claimed; the fourth does not
reproduce under **any** pin and is simply wrong:

| site | value | at q=1.1097 | at true pin | verdict |
|---|---|---|---|---|
| `hausdorff-dimension-recurrence-table3-data.md:3` | ℏ = 0.0989 | 0.0988555 ✓ | 0.0990817 | 1.1097 contamination |
| `information-causality-table-data.md:4` + `.md:7` | c_q ≈ 9.12 | 9.11577 ✓ | 9.092679 | 1.1097 contamination |
| `q-heat-kernel-peter-weyl-interpretation.md:1` | ℏ² ≈ 0.00976 | 0.0097724 (→0.00977) | 0.0098172 | **matches neither** |
| `electroweak-higgs-torus-...-table3-data.md` | q-powers | — | — | not re-derived this pass |

Note the corpus contradicts itself on ℏ_q within one chapter:
`hausdorff…table3` says 0.0989 and `discrete-planck-step.md:30` /
`q-heat-kernel-computational-fallback.md:7` say 0.0988, while
`regime-table.md:6` and `planck-length-share-vs-total.md:29` say the correct
0.0991.

---

## LIVE — re-verified (arithmetic recomputed or text re-read this pass)

### The three most urgent

**L-V1. [q07] `trefoil-operator-algebra` displayed matrices fail the braid
relation — three ways, and the failure is structural.**
`braids-and-knots/trefoil-operator-algebra.md` displays
`α = diag(e^{iπ/3}, e^{-iπ/3})`, `β = [[0,i],[i,0]]` and asserts
"both products evaluate to `[[0, i e^{2iπ/3}],[i e^{-2iπ/3}, 0]]`".
Recomputed at 25 dps:

```
αβα = [[0, i],[i, 0]]                        (= β)
βαβ = diag(e^{2iπ/3}, e^{-2iπ/3})            (diagonal, not off-diagonal)
displayed matrix ≠ either product
```

So `αβα ≠ βαβ`, and *neither* equals what the block says both equal. The
obstruction is structural, not a typo: `tr α = 1` and `tr β = 0`, so α and β
are not conjugate, and no braid representation can have them as σ₁, σ₂ — braid
generators are always conjugate. This is a *displayed identity in a content
block that is false*, load-bearing for the SU(2) trefoil holonomy story.

**L-V2. [q11/q12/kp-b0] The braid-word tables are wrong, and I re-derived
every row independently.** Closure component counts computed from the
underlying permutation (σ_i = transposition (i, i+1), 0-indexed):

`knots-particles-confinement/binding-knots-visual-inventory-table1-data.md`
— **8 of 12 rows wrong**:

| row | word given | comps | should be | verdict |
|---|---|---:|---|---|
| Unknot 0₁ | `1 ∈ B₁` | 1 | — | ✓ |
| Hopf L2a1 | `σ₀σ₁ ∈ B₃` | **1** | `σ₀² ∈ B₂` | ✗ closure is the **unknot** |
| Trefoil 3₁ | `σ₀σ₁σ₀ ∈ B₃` | **2** | `σ₀³ ∈ B₂` | ✗ closure is a 2-comp link |
| Cinquefoil 5₁ | `(σ₀σ₁)²σ₀` | **2** | `σ₀⁵ ∈ B₂` | ✗ |
| Septafoil 7₁ | `(σ₀σ₁)³σ₀` | **2** | `σ₀⁷ ∈ B₂` | ✗ |
| Fig-8 4₁ | `(σ₀σ₁⁻¹)²` | 1 | — | ✓ |
| T(2,9) 9₁ | `(σ₀σ₁)⁴σ₀` | **2** | `σ₀⁹ ∈ B₂` | ✗ |
| T(3,4) 8₁₉ | `(σ₀σ₁σ₂)⁴ ∈ B₄` | **4** | `(σ₀σ₁)⁴ ∈ B₃` | ✗ that is T(4,4) |
| T(3,5) 10₁₂₄ | `(σ₀σ₁σ₂)⁵ ∈ B₄` | 1 | `(σ₀σ₁)⁵ ∈ B₃` | ✗ that is T(4,5) |
| Borromean 6³₂ | `(σ₀σ₁σ₂)² ∈ B₄` | **2** | `(σ₀σ₁⁻¹)³ ∈ B₃` (3 comps) | ✗ all-positive **cannot be Brunnian** |

`knot-particle-dictionary-table1-data.md` carries the identical wrong words
for trefoil / 5₁ / 7₁ / T(2,9) / T(3,4) / T(3,5).
`knot-particle-dictionary-table2-data.md` is wrong on all four rows:

| row | word given | true closure | comps claimed vs actual |
|---|---|---|---|
| T(2,2) Hopf, gluon | `σ₀σ₁ ∈ B₃` | T(3,1) = unknot | 2 vs **1** |
| T(2,4) W boson | `(σ₀σ₁)² ∈ B₃` | T(3,2) = **trefoil** | 2 vs **1** |
| T(2,6) Z boson | `(σ₀σ₁)³ ∈ B₃` | T(3,3), 3-comp | 2 vs **3** |
| T(2,8) Higgs | `(σ₀σ₁)⁴ ∈ B₃` | T(3,4) = **8₁₉** | 2 vs **1** |

**Intent is recoverable and this is the strongest evidence the words are
typos rather than a different convention:** the correct words
`σ₀ⁿ ∈ B₂` (n = 2,3,4,5,6,7,8,9) and `(σ₀σ₁)ᵏ ∈ B₃` (k = 4,5) have letter
counts **3, 5, 7, 9, 8, 10** matching the tables' own *Crossings* columns
exactly, and give the component counts the tables claim.

**L-V3. [q11/q13] The blowup-regularity render breakage is still there.**
`lifting-and-descent/blowup-regularity-as-lifting.md` L6 `\foralln` and L8
`\varepsilonq^{2k}` — undefined control sequences, both inside math. These
abort the render, not merely mis-typeset. Highest mechanical priority.

### Numeric, re-verified

**L-V4.** `observations/double-magic-Ca40-diagram.md:8` asserts
`λ₂₀ = μ₂₀ = (5,4,4,4,3) = (5,4,4,4,3)'`. Conjugate recomputed:
`(5,4,4,4,3)' = (5,5,5,4,1)`. **Not self-conjugate.** LIVE.

**L-V5.** `observations/color-confinement-observation.md:34`:
`P_isolation ~ q^{-18} ≈ 0.13`. Recomputed `q₀^{-18} = 0.152875`. LIVE.

**L-V6.** `V_B/ℏ_q² = 749.2` in `color-superconductivity-borromean.md:69`,
`eos-borromean-cfl.md:70`, `borromean-hopf-energy-crossover.md:60`,
`borromean-hopf-energy-crossover-factor-250.md:1`. Recomputed
`Vol(𝓑₃)/ℏ_q² = 7.327724753 / 0.009817186 = 746.418`. 749.2 would require
`Vol = 7.35504`. `delta-skein-substrate-identity.md:44` already carries the
correct `746.4179…` — the corpus disagrees with itself. LIVE.

**L-V7.** CFL-gap self-contradiction, `color-superconductivity-borromean.md`:
computes `Δ_CFL^phys ≈ 2.5 MeV` then says *"This estimate aligns with
perturbative QCD predictions of Δ_CFL ∼ 10–100 MeV"*. 2.5 is 4–40× **below**
that range. LIVE. (The same block also uses `m_p ≈ 938 MeV` as an absolute
mass — see the 2026-08-11 excision ruling.)

**L-V8.** `s = q^{1/2} − q^{-1/2} = 0.05049` in
`observations/building-block-knots-table6-data.md:5` **and**
`appendix-knot-periodic-table/knot-periodic-table.md:128`. Recomputed:
**0.10438806**. Off by ~2×, in two files. LIVE.
Companion in the same table: `ℏ_q ≈ 0.09888` vs true `0.09908172`.

**L-V9.** `c_q ≈ 9.12` (`information-causality-table-data.md:4`,
`information-causality.md:7`, `regime-table.md:6`,
`speed-of-light-regimes-lieb-robinson.md:53,57`). `1/(q₀−1) = 9.092679`;
9.12 is the 1.1097 value 9.11577. LIVE across 5 sites.

**L-V10.** `[1/2]_q [3/2]_q = 0.818` in
`climax-volume-mass/q-angular-momentum-interpretation.md` rows 21–24 (four
rows). Recomputed at the proton pin: `[1/2]_q = 0.49932033`,
`[3/2]_q = 1.503402`, product **0.7506792** — matching the ledger's 0.7507
exactly, and essentially equal to the table's own classical column (0.75).
LIVE.

**L-V11.** `vertex-algebra-jet-relations.md` claims **34 relations** twice
(L9 and L403) and enumerates them, in the same sentence, as
`11 + 4 + 9 + 2 = 26`. The block contradicts its own arithmetic. LIVE.

**L-V12.** `branch-phase-mass-tower-witness.md:17` writes `3.4767` and calls
it a 0.014 % match to tritium's 3.4764. `|3.4767−3.4764|/3.4764 = 0.0086 %`;
the quoted 0.014 % requires **3.4769**, which is what
`frobenius-gram-matrix.md:42` carries (`+3.47694980`). The percentage is
right and the displayed number is the rounding error. LIVE.

**L-V13.** `figure-8-muon-mass-cross-check.md:18`: relative residual
`1.45 × 10⁻³⁰ ppm` = 1.45e-36 relative — 20 orders below f64 and below the
CODATA input uncertainty. Physically impossible as a residual. LIVE.

**L-V14.** `q-heat-kernel-peter-weyl-table-data.md:6`:
`[1]_q[2]_q + [2]_q[3]_q ≈ 8.84`. Recomputed — **balanced** convention gives
**8.13148**, **unbalanced** gives **9.1613**. 8.84 is a mix
(`2.11 + 2.011·3.341 = 8.83`). LIVE.

**L-V15.** `fundamental-knots-operator-basis.md` rows 19–23 carry
`0.499 / 0.499 / 0.249 / 0.249 / 0.551` under a caption claiming "exact
weights used for mass and binding computations". Recomputed:
`z_C = √q/(q+1) = 0.49932033`, `z_C² = 0.2493208`, versus canonical
`z_D = q³/(q²+1) = 0.61268804`. **These are convention-C values.** The C
excision that ran on `main` was compute-side; this content table was **not**
touched and is still off-canon under the 2026-08-15 owner ruling R1. LIVE.

**L-V16.** `vacuum-state-su2` quantum dims `[2]_q₀ ≈ 2.012`, `[3]_q₀ ≈ 3.041`.
Recomputed: `2.0108969` and `3.0436706` at the proton pin, `2.0108969` /
`3.0436…` at the muon pin, `2.0108445` / `3.0435` at 1.1097. **No pin gives
2.012.** LIVE.

**L-V17.** `q-game-of-life` golden threshold. `1/φ² = 0.381966 < 1`, so
"stability for q > 1/φ²" is vacuous everywhere the framework operates
(q₀ = 1.11). `q-game-of-life-interpretation.md:2` presents it as *the*
stability bound. LIVE (this is the surviving half of retracted W1).

### Structural / textual, re-read this pass

**L-V18.** `lifting-and-descent/qu-to-qou-su2.md:20–25`: degree `d = 1`,
`R_tot = 2·1 + |2| = 4`, `B = 2` branch points with `e = 2`. Riemann–Hurwitz
for `d = 1` on `CP¹` forces `R = 0` — a degree-1 holomorphic self-map of
`CP¹` is an isomorphism and is unramified. Taking R = 4 at face value gives
`χ = 1·2 − 4 = −2`, i.e. genus 2 for `CP¹`. LIVE.

**L-V19.** Euler-characteristic three-way inconsistency, all three legs still
verbatim:
- `χ(A) = 2` — `qu-to-qou-su2.md:13–15`, and the same value drives
  `quantum-characteristic-classes-su2`.
- `χ(M) = 3` — `q-harmonic-basis-brane.md:13`, used to count three basis
  vectors. **Impossible for a closed orientable surface** (χ = 2 − 2g is
  even); worse, the index in that very block runs over `b₁(𝒮_n)`, and
  `b₁ = 3` gives `χ = −1`.
- `χ(A) = −6` — `brings-surface/chi-minus-six-chain.md`,
  `braids-and-knots/why-b3.md:1`, `eightfold-way/schur-weyl-eightfold.md:52`,
  `eightfold-way/eightfold-open-problems.md:50`.
Plus `mass-brane-intro.md:3` "χ(A_n) is constant along the tower" against
`dim A_n = 3ⁿ dim A_0` with `χ = tr(id)`. See PARTLY ADDRESSED A1. LIVE.

**L-V20.** `why-b3.md:1`: "a quantum form of SU(2), **which has rank 2**".
SU(2) has **rank 1**. The intended chain is rank 1 ⇒ fundamental
representation 2-dimensional; the sentence states the wrong invariant and
then draws the right conclusion. LIVE.

**L-V21.** `holonomy-trefoil.md:15`: "The composite holonomy
`H₁H₂: w ↦ (w₃,w₄,w₁,w₂)` acts as the 3-cycle α and satisfies `(H₁H₂)³ = id`".
The displayed map is `(13)(24)`, an involution — order **2**, and
`(H₁H₂)² = id`. LIVE.

**L-V22.** `rho-s3-holonomy-exposition.md:8`: "α and β generate the Klein
four-group `V₄` … Their composition αβ is the 3-cycle". `V₄` has exponent 2
and contains no element of order 3; a group generated by two elements whose
product is a 3-cycle, inside S₃, is S₃. LIVE.

**L-V23.** `brings-surface/sw-period-residue-sum.md:1,9`: "Because λ is a
meromorphic 1-form on the compact Riemann surface 𝒮_c … **its period equals
the sum of its residues**", then "the period functions as an algebraic
residue sum … collecting the local residues at the branch-point poles". On a
compact Riemann surface the sum of **all** residues of a meromorphic 1-form
is **zero**; a period is `2πi ×` the sum of the residues *enclosed by that
contour*. As stated the period is identically 0. LIVE.

**L-V24.** `information-theory/hydrogen-partition-function*.md:30`, heat
capacity **inverted**: "At high temperature, only the j = 0 rotational mode
populates, sending `C_V → 0`. At low temperature, all rotational modes
contribute, driving `C_V → (3/2)Nℏ_q`." Exactly backwards — freeze-out is the
low-T behaviour and equipartition the high-T one, and the sentence then
"recovers the classical monatomic result" from the low-T limit. LIVE.

**L-V25.** `information-theory/hausdorff-dimension-recurrence.md`
flow-direction contradiction, three statements in one block:
- "The direction of decreasing d_H coincides with **increasing q** — pointing
  from the classical regime (q → 1) toward the Big Bang."
- "The **downward** iteration `q_{n+1} = q_n − ℏ_{q_n}` flows q **toward the
  classical limit q = 1**."
- "The parameter q flows from the classical limit toward the Big Bang."
The recursion itself is fine (`q − 1 + 1/q` fixes q = 1 with derivative
`1 − 1/q² = 0` there, superattracting) — the prose runs it in both
directions. LIVE.

**L-V26.** `observations/trace-ratio-interpretation.md:4`: "The squared ratio
spans **10 orders of magnitude**. This is the correct order of magnitude for
… `|M|²` spanning **~10⁶**." A 10⁴ mismatch presented as agreement. LIVE.

**L-V27.** `knots-particles-confinement/brunnian-property-of-borromean.md:3`:
"Deleting the 0-th strand produces `(σ₀⁻¹)³ ∈ B₂`, whose closure is the
negative trefoil `3̄₁`. Topological equivalence to `U₂` requires … two R2
moves and one R3 move." The negative trefoil is a **knot** (1 component);
`U₂` is the 2-component unlink. No sequence of Reidemeister moves changes the
component count. LIVE.

**L-V28.** `knots-particles-confinement/categorical-meson.md:12`:
`T₁₀ = σ₁σ₀ = L₋` called "the **negative** Hopf link" — both letters are
positive generators. LIVE.

**L-V29.** `knot-particle-dictionary.md:24`: "The figure-eight knot (4₁) is
the **unique** amphichiral knot". Unique among knots of ≤ 4 crossings only;
6₃, 8₃, 8₉, 8₁₂, 8₁₇, 8₁₈ are also amphichiral. LIVE.

**L-V30.** `meson-scale-independence-proof.md:3`: the Hopf-link complement
called "a **solid torus**". The solid torus is the *unknot* complement; the
Hopf complement is `T² × I`. The `Vol = 0` conclusion survives, the
identification does not. LIVE.

**L-V31.** `knot-particle-generation-consequences.md:3`: "All torus knots
have zero hyperbolic volume. They are **satellite** knots, not hyperbolic."
Thurston's trichotomy is torus / satellite / hyperbolic — torus knots are
torus knots, a distinct class. LIVE.

**L-V32.** `braids-and-knots/trefoil-knot-intro.md:1`: "**non-abelian first
homology**". `H₁` is abelian by construction (abelianisation of π₁). Reads
like sweep damage over "fundamental group". LIVE.

**L-V33.** `braids-and-knots/q-casimir-exists-proof.md:4`: "Centrality is
verified directly using the **Hecke relation**" — the relation used is the
`[E,F]` commutator of `U_q(sl₂)`, not the Hecke quadratic relation.
Companion misnomer: K-relations called "Serre relations". LIVE.

**L-V34.** `braids-and-knots/braid-group-su2.md:18` gives
symmetric = `q^{1/2} e₁⊗e₂ + q^{-1/2} e₂⊗e₁` and
antisymmetric = `q^{1/2} e₁⊗e₂ − q^{-1/2} e₂⊗e₁`. Independent structural
check: the two eigenvectors of the R-matrix (eigenvalues q and −q⁻¹) cannot
share the same coefficient ratio up to sign — the coefficient powers must
**swap** between the symmetric and antisymmetric vectors, not the sign.
Confirms the ledger's numeric finding. LIVE.

**L-V35.** `lifting-and-descent/jet-as-descent.md:1`: `δ⁰ : 𝔊_n → 𝔊_{n+1}`
declared, then described as "descent of information from the higher
categorical level `𝔊_{n+1}` to the lower level `𝔊_n`". Arrow and prose point
opposite ways. LIVE.

**L-V36.** `lifting-and-descent/cosimplicial-crossed-groupoid.md:9`: "The
**coface** maps `δⁱ` … (inserting the i-th **degeneracy** in the Čech
nerve)". Coface inserts a face, codegeneracy a degeneracy — the parenthetical
glosses are swapped. LIVE.

**L-V37.** `appendix-transfer-matrices/tm-heavy-atom-examples-intro.md:1`
promises "**Iron, silver, and uranium** form an increasing-mass ladder. The
worked examples below carry the transfer-matrix evaluation through each in
turn." The tables that follow work `¹⁴C → ¹⁴N` (tables 2, 3) and
`⁶⁰Co → ⁶⁰Ni` (table 5). Cross-block mismatch. LIVE.

**L-V38.** Magic-number set drift: `{0, 2, 8, 20, 28, 50, 82, 126}` — with a
leading **0** — in `tm-heavy-atom-examples.md:10`,
`tm-heavy-atom-examples-table1-data.md:2`,
`tm-heavy-atom-examples-table8-data.md:7`, against the standard
`{2, 8, 20, 28, 50, 82, 126}` used elsewhere. LIVE.

**L-V39.** `knots-particles-confinement/shell-transition-knot.md:2,36`: "the
Borromean baryon's **3 internal crossings**" / "`𝓑₃` has exactly 3 internal
crossings". The corpus-standard word `(σ₀σ₁⁻¹)³` has **6** letters, and
`stable-atom-properties` counts 9 = 6 + 3 consistently with 6. The `N ≥ 3`
threshold argument leans on this count. LIVE.

**L-V40.** `climax-volume-mass/jones-mobius-diagonal.md`: "excising the
diagonal" (L5) and "excising the singular diagonal" (L13) both bracket the
same finite-part display. Editing residue, and the block's own `.qa.json`
already flags it. LIVE. *(A naive exact-string grep returns 1 hit and reads
as FIXED — it is not.)*

**L-V41.** `climax-volume-mass/knot-operator-energy-exists.md:7`:
"`R = 𝔽_p`: no archimedean absolute value, `|R| = ∅`". `|R|` denotes the set
of absolute values; writing it `= ∅` where the intent is "the archimedean
place is absent" is an odd formalisation that reads as "R is empty". LIVE.

**L-V42.** `information-theory/q-exponential-taylor-proof.md:15`: "When
`|q| = 1` **is irrational**, convergence holds by Diophantine estimates."
`|q| = 1` is a modulus condition, not a number that can be irrational; the
intended statement is `q = e^{2πiθ}` with θ irrational. LIVE.

**L-V43.** `information-theory/quantum-temperature.md:1` opens with a
`> **Superseded.**` banner **in scholarly prose** — an `authorNotes`
migration case per AGENTS.md §4d. LIVE.

**L-V44.** `brings-surface/brings-surface-qou-intro.md:1` calls Bring's
surface "the S₅-symmetric **quartic-and-quadric** in ℙ⁴". Bring's curve is
cut by the vanishing of the degree-1, 2 **and 3** power sums — the cubic is
missing from the description. LIVE.

**L-V45.** `brings-surface/c-from-color-flavor-swap.md:40` — "commutes with
`σ_i ↔ σ_i`", a trivial self-map (inverse presumably intended); and L69 —
"Bring's **quintic** surface", where the object is Bring's *curve* / the
quartic-and-quadric surface. LIVE.

**L-V46.** `brings-surface/brings-qou-axiom-map.md:10`: "**Plucker**
relation" (missing umlaut, → Plücker) and a dangling "**See Seiberg–Witten**
for the explicit symplectic form" with no `\cite{}`.
`brings-surface/braid-group-action.md:4`: "**Mobius** involution" (→ Möbius).
LIVE.

**L-V47.** `brings-surface/brings-q-hyperbolic-geometry.md:1,3,5`: bare
`SU_q(1,1)` outside `\mathrm{}` (register violation, §7aa). LIVE.

**L-V48.** `brings-surface/descartes-proof.md:16`: "between Tannakian
categories are **accordingly isomorphic**" — word slip (canonically /
correspondingly). LIVE.

**L-V49.** `information-theory/quantum-computational-universality.md:12`:
"the parameter q leaves the real axis, **transverses** the complex plane"
(→ traverses). LIVE.

**L-V50.** `\pp` undefined macro, live in
`index-of-definitions/definition-index.md:867,868` (`$\mathbb{F}_\pp$`,
`$\mathbb{Q}_\pp$`) and `information-theory/discrete-planck-step.md:19`.
LIVE.

**L-V51.** `\xiZ` stripped token in `information-theory/discrete-planck-step.md:7`
and `quantum-observable-universes/substrate-radial-coordinate-proof.md:22`
(`\mathcal{L}_\xiZ = J\hbar_qZ`). LIVE.

**L-V52.** `\pid`, `\pia`, `\lambdaL` undefined macros in
`observations/double-slit-massive-pattern.md:14,22,37,43` and
`observations/double-slit-q-phase.md:25`. LIVE.

**L-V53.** `observations/double-slit-two-modes.md:33`: `\frac{…}{1}` —
denominator 1. LIVE.

**L-V54.** `\unicode{9737}` (MathJax-only; KaTeX does not implement it) in
`appendix-surreals/vacuum-epsilon.md:1,5`, `vacuum-epsilon.ts:6`,
`index-of-definitions/definition-index.md:799`, and ~3 more. LIVE.

**L-V55.** `\operatorname` — banned for KaTeX per AGENTS.md render-QA gate —
in `appendix-surreals/mobius-surreal-renormalization.md:7,9,13` and
`appendix-surreals/hyperreal-limit-transfer.md:11`. Note the same block mixes
`\operatorname{std}` and `\operatorname{st}` for the standard-part map.
Also live outside the appendix: `climax-volume-mass/jones-mobius-diagonal.md:5`
uses `[$\operatorname{prop:mobius-energy}$]` as a *cross-reference*. LIVE.

**L-V56.** Pandoc-style `[@key]` citations (do not render in this pipeline) in
`appendix-surreals/spectral-normal-form.md:131`,
`appendix-surreals/surreal-appendix-intro.md:6,20`. LIVE.

**L-V57.** Escaped-bracket citations `\[lusztig1993]` in
`lifting-and-descent/direct-limit-lusztig.md:1`. LIVE.

**L-V58.** Bare `Cech` (missing háček) in
`lifting-and-descent/cosimplicial-crossed-groupoid.md:9`,
`descent-cocycle-deviation.md:10`, `descent-condition.md:11`, and — the part
that needs a joint `.md` + `.ts` fix — `descent-cocycle-deviation.ts:8`
(`title:`), where nothing transliterates. LIVE.

**L-V59.** `index-of-definitions/definition-index.md:717`: `## Corollarys`
(generated heading; the pluraliser needs the `-y → -ies` rule). LIVE.

**L-V60.** `appendix-qvalues/proton-mass-substrate-identity-derivation.md:7`:
`q₀ = 1.10977859555…` — a **digit transposition** of `1.10997859555…`
(1.1097-78 vs 1.1099-78). Unlike R1 this one is genuinely wrong: it is
1.8e-4 relative from either pin, and the block's own table is consistent with
1.10998. LIVE.

**L-V61.** `Q_β` mislabelled **CAL-3** three times in
`knots-particles-confinement/delta-skein-substrate-identity.md` (L45 "CAL-3 +
CAL-1", L52 "the empirical CAL-3 value", L69 "CAL-3 enters only as a
consistency cross-check"). Per the 2026-06-26 owner ruling `Q_β = ℏ/𝔇_β` is
the **CAL-2** proxy; CAL-3 is `𝔇_π` / `m_π`. LIVE.

**L-V62.** `appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md:57`:
`Vol(4₁) = :val[Vol_4_1]{precision=6} \cdot \pi`. The witnessed value is
already 2.029883…; multiplying by π yields 6.3772 and the block calls it
"smallest hyperbolic volume". Spurious π. LIVE.

**L-V63.** Skein-convention cluster, **≥ 9 sites** confirmed by grep today,
all using the HOMFLY/`V_K(t)` form `qL₊ − q⁻¹L₋ = (…)L₀` against the AGENTS.md
§7a canonical `L₊ − L₋ = (q − q⁻¹)L₀`, and **inconsistent with each other**
on the right-hand side (`(q^{1/2} − q^{-1/2})L₀` vs `(q − q⁻¹)L₀` vs `sL₀`):
`knot-particle-generation-consequences.md:24`,
`knot-particle-generation-interpretation.md:36`, `crossing-energy.md:16`,
`observations/strangelet-double-beta.md:7`,
`appendix-surreals/q-collatz-conjecture.md:39`,
`information-theory/skein-turing-machine.md:6`,
`glossary/glossary-q-bit-skein.md:8`,
`climax-volume-mass/skein-crossing-asymmetry.md:4`,
`climax-volume-mass/skein-crossing-asymmetry-prop.md:4`.
This subsumes the separately-recorded "second / third / fourth / fifth"
divergence findings. LIVE.

---

## LIVE — located verbatim, ledger evidence accepted

Each of these was found in the current tree at the cited block; the ledger's
own reasoning is retained unchanged and was not independently re-derived this
pass. Ordered by original batch.

**Title-line.** "forbids beta decay" wrong term
(`observations/complexity-interpretation-intro.md:5` — the electron trefoil's
stability forbids *electron* decay, not β decay) · `=` used where `≈` is
required for derived values (§7ab, class-level) ·
`RESOLVED` status leaks in `observations/hadron-half-life-verification.md:22,23,24` ·
`observations/higgs-t28.md:2,60` uniqueness claim ("the unique genus-3 link …
Therefore T(2,8) is the unique Higgs candidate") unsupported by the argument
given · q₀ muon/proton straddle in `observations/flavor-split-substrate-proof.md:121`,
`observations/g-q-closed-form.md:64` and the fine-structure block (see R1 for
the corrected characterisation).

**obs-b8.** `observations/three-calibration-discipline-discussion.md:30` "They
sit in **distinct cohomological degrees**" — contradicts the standing framing
(three real DOF of the **single** H¹(Bring) = 2W, not three degrees
H⁰/H¹/H²), and contradicts the block's own closer ·
`observations/trefoil-vortex-chirality-flip` missing article.

**it-b2 / obs-b6 / b7.** `information-theory/mass-energy-equivalence-proof`
`c_q` factor inserted twice (E/m = c_q per crossing vs the displayed `c_q²`)
— derivation review, not a typo · `information-theory/julia-set-reeb`
golden-rotation linearizability inverted ·
`observations/substrate-consistency-window.md:1` "**a single free parameter**"
against the 3-CAL discipline — same claim at `observations/mass-comparison-table.md:3`,
`appendix-knot-periodic-table/knot-periodic-table.md:115`,
`appendix-transfer-matrices/tm-notation-table1-data.md:3` ·
`observations/pair-creation-energy` `tanh(ln q₀) ≈ 0.104` vs `α ≈ 0.0073`
overclaim (the 0.104 value itself checks out: `tanh(ln q₀) = 0.10397`) ·
`observations/strangelet-merger-signature.md:21` `\mathrm{MeVperbaryon}` token ·
`observations/q-deformed-double-slit` trailing-comma display.

**it-b0 / b1.** PRIOR-SWEEP DAMAGE class (mangled anti-negation idioms —
distinct from the intensifier class, needs author-checked repair) in
`information-theory/hopf-link-symmetric-decomposition.md`,
`information-theory/crossing-parity-test.md`, and
`information-theory/composite-crossing-sublimation-criteria.md` (see CHANGED
C1) · `information-theory/gas-constant-derivation` absolute-mass framing
against the 2026-08-11 excision ruling ·
`information-theory/golden-ratio-transport.md:58` `E_{1/q}` font drift (should
be `\mathcal{E}_{1/q}`, matching `\mathcal{E}_q` in the same sentence).

**bs-b0.** `g` symbol collision (genus vs Gauss sum) in
`brings-surface/bring-trefoil-cinquefoil-channel` · `w_k` vs `ω` drift in
`brings-surface/braid-group-action`.

**bs-b1.** X tuple/scalar drift between `brings-surface/color-elliptic` and
`color-bundles` · `SU_2` written for `\mathrm{SU}(2)` (class).

**bs-b2 / it-b4.** Skein divergence in
`embeddability-closure-spectral-filter` (q^{1/2}-normalised — folded into
L-V63) · `C_p` / `C_5` scope mismatch in `cyclotomic-reduction` · bare `=` on
Δ / j / x_T plus dangling `\cdots` in `descartes-elliptic`.

**it-b3.** `prop:p-vs-np-boundary` opens `**Conjecture**` — §3b block-kind
conflict · q₀ numerical values appearing outside the intro / Ch 7 register
(class; see R1 for the 33-file extent).

**bs-b5.** `brings-surface/unit-particle-state.md:5` "In the classical limit
q → 1, this recovers the classical dilogarithm `Li₂(z)`" — flagged for math
review (the ODE limit may be `li(z)`, not `Li₂`); **unresolved, not
adjudicated this pass** · `Φ_n` inverse-Pochhammer vs Faddeev `Φ_q` symbol
collision · Seifert-genus phrasing in `braids-and-knots/torus-knot-generators`.

**bs-b3 / b4, kp-b1 / b2.** `dim_q` vs involution numbers in
`sw-classical-jet-exactness` (q = 1 only) · third q₀ value in
`delta-skein-substrate-identity` matching neither pin, plus internal table
drift · Bolza attribution in `brings-surface/hyperelliptic-quintic.md:22`
(`x⁵ − 1` vs the Bolza curve `y² = x⁵ − x`) · odd-vs-prime in
`genus-filtration-ideal-derivation` · `electroweak-triplet` exposition
duplication (consolidation candidate).

**q00.** Magic-A `B = A·8G·m_e` missing ρ = 2 against the block's own 29.956 ·
CAL-3 mislabel recurrence at registry L370, `mba-chain-map` step 11, and in
witness filenames · `σ_0` in `H_1` (impossible — `H_1` has no generators) ·
0/1-index divergence in the B₃ braid word · photon-pair `(σ₀³)` label
mismatch · diagrams-vs-spec convention conflict.

**q01.** "6 = inverse of −1/12" (should be 12 = multiplicity × binding) ·
muon knot 4₁ vs 5₁ tension between `mba-step09a` and `cal2-higgs` ·
`sm-params-neutrino` "nowhere addressed" against the ledger · bare `&` in a
heading.

**q02.** Borel-rank parity SWAPPED in `appendix-surreals/borel-partial-resolution`
(false in general) · Bloch–Wigner Step 2 false for real z in
`b1-soft-sharpness-theorem-proof` (needs restriction to non-real arguments) ·
eleven-vs-ten rows and the fig-8 status tension in `b1-hyperbolic-rows` ·
`T(2,5) = T(5,2)` double-count · birthday `b(ε) = ω = b(ω)` self-contradiction ·
KL-cell partition vs generic S₃ cells in `on-p-modular-hecke` (unverified) ·
`appendix-surreals-archimedean/wenzl-positivity-implies-substrate-positivity.md:106-107`
"the choice of q₀ is not free — it's **locked by the unitarity** …" overclaim.

**q05.** Knot-assignment tensions (`T_{νν̄}` vacuum-vs-neutrino; up quark
trefoil vs Borromean) · `c₃ = −2` called a "mechanical identification" where
the canonical tier is *near-match* (canonical-watcher) ·
`braids-and-knots/bar-involution-grading-lean-proofs.md:97` "All **33
theorems** / definitions" against a Lean count of 32/37 plus 3 unnarrated ·
"singles" garble in `coxeter-geometric` · `j < k` index-origin leak in
`coxeter-strong-exchange`.

**q03 (appendix-surreals).** `q-collatz-conjecture` self-contradiction
(`κ_C` "reduces to unknot polynomial 1" against the block's own correction
that `C_q(1)` is undefined and the attractor is the 2-cycle
`{q⁻¹, 1 + q⁻¹}`) · `surreal-appendix-conclusion` "isomorphism" overclaim
(the proposition gives an injective **non-surjective** embedding) plus
`q_ω` vs `ζ_ω` drift · `local-infinitesimal-field` three incompatible readings
of the order (`st(ε) = 0` vs `q₀ − 1` at standard order vs an `ω⁻¹`
coefficient) · `infinitesimal-observability` `dim_No ≤ ε` against the worked
example `dim = 1, |ξ| = ε` (norm-weighted vs cardinal) · `kashaev-surreal`
"polynomial in n" dubious — the coloured Jones is q-holonomic, and this is
load-bearing for `J(ζ_ω, ω)` · `rh-surreal-bound` garbled "δ = 0 on the nose
for any standard δ > 0" · `conway-normal-form` "strict inequality ≤" ·
`q-birch-swinnerton-dyer` rank-0 ⇒ trivial torsion non-sequitur (holds only
via `q-bsd-rank-zero`) · `q-bsd-classical-limit` "primes > 3 and multiples"
mischaracterises `{n : n ∤ 6}` (misses 4, 8, 9) · `collatz-three-forms` "gap
collapses to q = 1" garble and "no margin" against the sharp threshold
1.585 < 2 · `sign-sequence-of-braid-invariant` "refines Jones" asserted, but
it is the open content of `conj:jones-birthday`.

**q04.** `yang-mills-surreal-bound` Wilson-loop self-inconsistency
(ω-order > 0 ⇒ `st = 0` **exactly**, not "exponentially suppressed"; L19
`δ ≥ Δ_q` vacuous for standard δ) · `transcendental-accounting` Fact 2
non-sequitur (equal Jones does not determine the coloured `J^{(N)}` or Vol) ·
`two-q-adic-valuation` unbalanced `[2]_q = q + 1` against the corpus-balanced
`q + q⁻¹` (cross-block symbol collision) · `tm-general-form` "a Iwahori"
grammar · `tm-inductive-construction` `M_i` type slip (2×2 matrix vs column
vector) · `tm-heavy-atom-examples` `𝔔_β` vs `\mathcal{Q}_exp` drift.

**q08.** `T`-vs-`σ_i` generator symbol divergence ×2 against §7a — relations
correct, symbol banned: `crossing-energy-categorical-origin`
(`T = P.R` with `(T−q)(T+q⁻¹) = 0`) and `crossing-energy-trefoil`
(`T − T⁻¹ = q − q⁻¹`) · `mobius-energy-frobenius-kernel-proof` `γ(s)` vs
`ϱ(s)` register (γ is reserved for the photon).
*Verified clean by the recording agent, re-affirmed: trm-hopf proton-pin value
to f64 precision, D coefficients exact, degree-6 discriminant roots, φ³ golden
identities.*

**q07.** `trefoil-knot-group` closure claim sloppy (an arbitrary 3-braid
closure is not the trefoil) · `three-strand-color-winding-rigidity` hypothesis
mismatch (`1 − q²` invertible vs the proof's `q⁴ ≠ 1`) ·
`trm-hopf-sigma1-sq-closed-form-proof` self-declared stale C-coefficient
witness, producer re-run outstanding.
*Verified clean: meson fusion / sinh identities (203.14 ppm, 46.9 ppb),
`tr_M(σ₁²)` closed form + Taylor coefficients to 30 dps, rigidity matrix
algebra, Planck-time ratios, `Vol(4₁)` name + value.*

**q06.** `feynman-eigenbasis` skein divergence (folded into L-V63) ·
`knot-notation-convention.md:5` calls `𝔎_μ` amphichiral where Table 1 assigns
the muon `T(2,5) = 5₁`, which is **chiral** (the amphichiral one is
`K_H = 4₁`), plus the e⁻/e⁺ sign assignment flipped against the Table 1
headers · `knot-complement-group` takes complements in `ℙ¹(ℂ) = S²` where the
sibling correctly uses `S³` · photon γ described as "not a knot, a Hecke
element" against Table 1's `K_γ = ∅` (needs a stated reconciliation) ·
`markov-axioms-primitive` narrates its own revision history in prose (§4d
`authorNotes` migration).
*Verified clean: `z_D` 20-digit proton-pin value exact, C-vs-D gap 0.408 %,
`tr M_{4₁} = −0.91068`, θ angles, Catalan / BCH / Hoefsmit algebra.*

**q09.** `vertex-algebra-relations` C-4 `χ(A) = [n]_q! > 0` against C-4b
`tr_M(id) = −6`, unreconciled (this is the χ family again — see L-V19) ·
`a2-from-three-strands` "120° between a root and its negative" (that is 180°;
120° is between simple roots) and its `T₁, T₂` generator naming ·
`q-momentum-properties` `p_q(β^σ) ≠ −p_q` against the sibling's exact
`p_q = w` · `E_x` symbol clash (half-difference vs `q/q⁻¹` under one symbol) ·
decuplet spread 13.5 vs 13.6, and the spacing is of *quadrupled* mass ·
`tr_τ` vs `tr_M` drift in `q-energy`.

**q10.** `meson-mass-splitting` omits the kaon hypercharge-averaging clause
that its own Lean carries (without it GMO = 4b) · `lqg-adm` quotes
`q₀ ~ 1.11` outside the intro/Ch 7 register · `vector-meson-nonet` "two of
three proved content-free" possibly stale against the CG third null ·
`glossary-categorical-transport` tikzcd drops the `ℏ_q` factor and the
jet-arrow direction · `crossing-energy-interpretation` Coulomb 0.3136
tabulated as 0.315, net 0.6272 vs 0.630 · unverifiable Mathlib references
`CompactClosedCategory`, `PivotalCategory` (named in prose; no such
declarations).

**q11.** `hadron-proton-example` `β_Bor = (σ₀⁻¹σ₁)³` is the bar-image of the
corpus standard `(σ₀σ₁⁻¹)³` — same link, but trace consumers may differ
(both give 3 components, verified) — **plus an absolute-mass excision
violation**: a CODATA witness value presented as a framework evaluation
`m_p ≈ 938 MeV` · `chapter-overview` "exact proton and neutron masses"
(same violation) and q₀ mis-rounded to 1.1097 (true 1.10998 → 1.1100) ·
`jet-planck-steps` table 1 and table 2 CONTRADICT (charm step 5 + bottom 7
vs b, s 5 + c 7), "down `u^σ`" ambiguity, and plain `c` for charm colliding
with the crossing column.
*Verified clean: Toffoli tables match the true q₀, compound-β Q-values,
author's-note percentages.*

**q13.** `shell-schur-weyl-self-duality-proof` carries a literal `?` as the
determinant-twist exponent — an unresolved stub inside a proof ·
`brane-boundary-su2` calls `U(1) × S²` (3-dimensional) a "solid-torus
boundary" (that is `T²`, 2-dimensional) · suspected sweep-injected adverb
pattern in the arc-space family ("safely retains", "predictably assigning",
"natively inherits") · `unstable-atom-decay-channel-proof` asserts a "unique
optimal vertex" with no LP objective specified.
*Verified clean: Hecke NF reduction at 4 q-values including the proton pin,
shell / magic tables exact, no numerical q₀ anywhere in that batch.*

**q14.** `descent-lemma-proof` `J¹(A) = A ⊗ Ω¹` against the sibling's
`A ⊕ (Ω¹ ⊗ A)`, and the unit section embeds Ω¹ rather than A ·
`direct-limit-algebra-su2` extra closing paren · `descent-reduction` "inverse
of the Reeb vector field" garble · `descent-involution-su2` `\varTheta`
angle colliding with the archimedean-tuple symbol · systemic de-hedging
intensifier residue ("strictly / precisely / identically / fully").
*Conventions clean: no `\mathcal` categories, τ throughout, no deprecated
5-tuple.*

**q12.** Same wrong trefoil word in `nucleon-hecke-element-normal-form.md:14`
while the sibling proofs in that chapter use the **correct** `σⁿ` words — the
chapter conflicts with itself · `T(2,9)` exceeds the block's own generator
cutoff `m + n ≤ 9` while `T(4,5)` (= 9) is absent · `Li_2^q` range claim
`[0.1, 0.82]` wrong at low z (→ 0 as z → 0; holds only for z ≳ 0.103 — the
upper bound and the `Φ_q` values do check out) · magic numbers applied to A
rather than Z/N in `level-sufficiency-interprets` · 4₁ identity conflict
(table 3: Higgs — confirmed present today; interpretation L40: muon; table 1:
muon = T(2,5)) · κ-table verified exact on the muon pin, no 1.1097
contamination, but it is an unannotated muon-layer witness (migration-posture
note, `qou-1c4y`).

**q15.** `J¹(A)` drift deepens — the batch defines the tensor form
`A ⊗ Ω¹` (dim 3×) while importing sum-only facts (the unit-section inclusion
`A → J¹` is natural only for `E ⊕ (T*M ⊗ E)`), and `jet-prolongation-proof`'s
geometric fibre gives 4× against the block's own 3× count ·
`localized-knot` puts a knot `S¹ → S³` inside the fibre `𝒮_p ≅ CP¹ = S²`,
with "resolved by blowup" asserted rather than established · de-hedging
intensifier flood, chapter-systemic (6 failing blocks; lemma "acts as an
object" against the proof's "is an object") ·
`motivic-perpetual-obstruction` embeds the Lean class name in prose and the
conjecture refers to itself as "This lemma" · `\hat\tau_n` descent involution
colliding with the fibre-functor τ glyph.
*Clean: Čech usage correct in this batch, no coface swap participation, `Φ_q`
series verified, no bad q₀ strings.*

---

## CHANGED — content moved; finding needs restating

**C1. [it-b0/b1] `composite-crossing-sublimation` → `composite-crossing-sublimation-criteria`.**
The block now lives at
`content/quantum-observable-universe/information-theory/composite-crossing-sublimation-criteria.md`.
The PRIOR-SWEEP-DAMAGE finding still applies; re-target the path.

**C2. [q15] "complementary-subgroups non-cancellation argument fails in
H²(CP¹,ℤ) = ℤ."** There is no block of that name. The claim lives in
**`fluid-dynamics/`**, not `lifting-and-descent/`:
`ns-singularity-descartes-proof.md:17` ("complementary subgroups of
`H²(𝒮, ℬ)`"), `ns-obstruction-tower.md:47` ("κ₀ and δ_n strictly occupy
complementary subgroups whenever κ₀ avoids torsion"), and
`ns-obstruction-computation-interpretation.md:1`. The objection — that in
`H²(CP¹,ℤ) ≅ ℤ` any two nonzero subgroups intersect, and `H²(CP¹,𝒪) = 0` —
is unchanged and untouched, but it is an objection to the **NS-obstruction**
chapter, and the finding should be re-filed there. Note this raises its
severity: `κ_n ≠ 0 unconditionally for all n` is the load-bearing conclusion
of the Navier–Stokes obstruction tower.

---

## NOT-FOUND — could not locate; recorded as unresolved

**N1. [bs-b3/b4] "cyclic-pairing step-count self-inconsistency."** No block,
file, or prose string containing "cyclic pairing" exists in `content/`. Either
the block was renamed beyond recognition or the identifier was garbled when
recorded. Not marked fixed.

**N2. [q02] "log_q-vs-ln mismatch 27.7 vs 2.9 (collatz-hausdorff)."** No
`collatz-hausdorff*` block exists; the Collatz family lives in
`appendix-surreals/` as `collatz-three-forms`, `collatz-no-cycles`,
`collatz-contact-boundary{,-defn}`, and neither `27.7` nor a matching `2.9`
appears in that directory. Not marked fixed.

**N3. [it-b2] "excised-cross-ref debris in three it blocks."** The three
information-theory blocks that reference the excised convention today —
`toffoli-lp-stability.md:21`, `toffoli-lp-stability-proof.md:2,14`, and their
sibling — read as **deliberate, well-scoped withdrawal notes** ("Open
(2026-08-09) … the figure previously quoted here is withdrawn … it came from
a Gram matrix built with the naive length rule under the excised convention C
… the replacement value must be read off a regenerated witness; it is not to
be hand-edited"). That is exactly the honesty discipline the corpus asks for,
not debris. If the original finding meant something else — dangling
`#label` cross-references into blocks that were deleted — it needs restating
with the specific labels. Not marked fixed, but the recorded evidence does
not survive re-reading.

---

## What to hand the owner first

1. **L-V1 — `trefoil-operator-algebra`.** A content block displays two matrix
   products, asserts they are equal, and gives a third matrix as their common
   value. All three statements are false, and the representation it claims to
   exhibit cannot exist (`tr α = 1 ≠ 0 = tr β`, so the two generators are not
   conjugate). This is the only item in the ledger where a *displayed
   equation* is wrong rather than a *label* or a *rounding*.
2. **L-V2 — the braid-word tables.** Three tables across two chapters give
   words whose closures have the wrong component count, the wrong knot type,
   or (Borromean) a topology that cannot be Brunnian. The intended words are
   recoverable from the tables' own crossing counts, so the fix is mechanical
   — but until it lands, `binding-knots-visual-inventory`,
   `knot-particle-dictionary` tables 1–2, and
   `nucleon-hecke-element-normal-form` disagree with the sibling proofs in
   their own chapter.
3. **R1 + L-V60 — the q₀ pin surface.** Not because the muon string is wrong
   (it is not — see R1), but because the corpus currently carries **four**
   distinct q₀ presentations: the correct proton pin, the correct muon pin
   mislabelled "(50 dps)" across 33 files, a stale 1.1097 baked into at least
   three data tables, and a genuine digit transposition (`1.10977859555`) in
   `proton-mass-substrate-identity-derivation` — a *production identity*
   block. A reader cannot tell which is authoritative from the text.

---

## r01 re-audit of the 35 changed blocks — findings recovered from the sidecars

`agent:r01` re-audited the 35 blocks whose `.md` had changed on main after
their original audit (so their old verdicts were deliberately not carried
forward). It completed all 35 with the full ten-category record, then died
on the weekly usage limit **while writing its summary**, so the prose report
was lost. The verdicts survived on disk; this section is reconstructed from
them, not rewritten from memory.

**17 fails over 35 blocks — 4 fixed inline, 13 flagged structural.**

Fixed: meta-commentary openers in `qbeta-ck-truncation-canonical` (twice, one
of them a negation-contrast in the same block), `quantum-peter-weyl-proof`
("This is the key step." deleted), `skein-filtration-trichotomy` ("It is worth
stating why …" → the plain predicate).

Structural, worth the owner's attention:

- **`millennium-unification` is internally contradictory after a correction
  pass.** Paragraphs were inserted establishing that the Navier–Stokes row is
  a *rate comparison*, not a squeeze instance — but the block's opener still
  says "Six … reduce to a single surreal inequality", and a later paragraph
  restates it. The block now claims six and demonstrates five-plus-one.
  `surreal-squeeze-interpretation` carries the same stale "every millennium
  remark reduces to this lemma" currency. Two blocks, one unreconciled edit.
- **A trace-class constant fails on its own step** in
  `p1-spectral-sobolev-proof` — verified by the agent, separate from the
  superlative flag on the same line.
- **Three correction/provenance notes sit in `.md` prose** where §4d puts
  them in `.ts` `authorNotes` (`q-collatz-conjecture`, `qou-p-neq-np`,
  `categorical-mass-markov-proof` — the last also carries a C-vs-D comparison
  table that is probably worth keeping in prose). Flagged rather than moved:
  deleting provenance is the wrong repair.
- `ns-kummer-specialisation` carries the de-hedging intensifier flood in both
  its superlative and nonspeakable dimensions; the proposed repair restores
  plain predicates ("zeroes out only spanning n in {1,2,3,6}" → "vanishes
  exactly when n divides −6").

---

## Reconciliation options worked, 2026-08-21

The three "hand the owner first" items are analysed with the mathematics
recomputed in
[`docs/audits/2026-08-21-three-reconciliations.md`](../docs/audits/2026-08-21-three-reconciliations.md).
Summary of what changed in the understanding of each:

1. **`ex:trefoil-operator-algebra`** — not a typo in the displayed product.
   The block applies the braid relation to a **dihedral** generator pair
   (3-cycle lift, transposition lift) taken from `def:su2-generators`. It is
   impossible as stated: braid generators are conjugate, so `tr α = tr β`,
   but `tr α = 1` and `tr β = 0`. The correct braid pair lives in the same
   group — `s₁ = β`, `s₂ = α²β` — and its composite has eigenvalues
   `e^{±iπ/3}`, which is the three-fold colour phase the block's closing
   sentence wants; the current `αβ` has eigenvalues `±i`. The repair
   improves the physics rather than merely correcting it.
2. **Braid-word tables** — one misconception with two variants: torus words
   written on `p` strands instead of `p−1`. The `T(2,n)` rows keep the right
   crossing count and gain a spurious component; the `T(3,n)` rows get both
   wrong and name `T(4,q)` instead. Correct words recovered for every row.
   **A component-count guard is not sufficient**: `T₃,₅` as written closes
   to a knot and is caught only by crossing count.
3. **q₀ surface** — re-measured, and the item's shape is different from how
   it was ledgered. The mis-rounded `1.1097` is **a Lean problem**: 110 of
   its 127 occurrences are in `.lean`, **79 inside statements** rather than
   comments (`q_approx : |q - 1.1097| < 0.001`, `cfl_gap 1.1097 > 2`). They
   are not false — the slack absorbs the error — but they discharge at a
   point that is not the substrate, so re-pointing them changes proof
   obligations and needs a Lean build this container does not have. The
   old-muon string is the mirror: 30 of 43 occurrences in `.md`, 27 of them
   labelled "(50 dps)" on a 16-digit value.

---

## From agent:r06 (mass-theory nq_00) — 2026-08-21

Fourteen findings, each recomputed by the agent rather than asserted. The
four that carry consequences:

1. **`deuteron-binding-dressing-proton-net`: `+0.12%` is the wrong route's
   number.** The prose credits the `(1−h/2)` dressing with `+0.12%` of
   AME2020. The block's own witness
   (`probes/probe-d-dressing-is-proton-net.witness.json`) records
   `B_cand_err_vs_AME_pct = 0.28666` for exactly that route; `0.11882`
   belongs to `B_via_kashiwara_qbeta_MeV`, which substitutes the Kashiwara
   Q_β for the ansatz one. The claim is **2.4× overstated**, and the same
   figure is repeated in the `.ts` authorNotes. Reproduced independently:
   `h = 0.20906030`, `net(p) = 0.89546985`, `1.1199 × 0.89546985 = 1.002866`.
2. **A convention-C survivor that is load-bearing, not cosmetic.**
   `deuteron-fusion-frame` sets `z = 1/[2]_v = 1/(√q + 1/√q) = 0.49932` —
   z_C exactly — and calls it "the Ocneanu–Markov normalization … not a
   modeling parameter". Its marginal-stability identity `g²(1+[2]_v²) = 1`
   holds **iff** `z = 1/[2]_v`, so the block's "rigidity of the integer 5"
   argument is convention-C-specific and does **not** survive the swap to
   canonical D. `delta-max-uniform-bound` carries the same z_C value.
3. **"Systematically under-predicts by 30% to 76%" is contradicted by the
   block's own Table 2.** The deuteron is **over**-predicted (+41%), and the
   under-prediction range over the other five rows is 32–76%. The sign flip
   is informative rather than incidental: D is the only isotope with no
   same-flavour pair, so `Δ_{T=1}` vanishes there.
4. **"Sub-percent, predictive not calibrated" scores a calibration
   pass-through.** The baseline `Z·m_p + N·m_n + Z·m_e` is CODATA input
   carrying >99 % of the mass, so "sub-percent on the total" restates
   "binding is under 1 % of the mass" — the ⁴He 0.576 % error *is* the
   21.5 MeV binding shortfall over 3728.40 MeV. Same class as the
   2026-08-18 `m_e`-scored-as-a-beat correction.

Table arithmetic, with the identities derived rather than guessed:

- `cyclotomic-orbit-sum-all-depths-table1` row (n=5, N=7) prints the
  fraction `16806/16807` against its own decimal `−1.03650`. From
  `Σ_j Cl_n(2πj/N) = −ζ(n)(N^{n−1}−1)/N^{n−1}` the value is **2400/2401**
  (= −1.036496); the printed fraction gives −1.036866. The other four rows
  satisfy the formula.
- `cyclotomic-trilog-imaginary-closed-form-table`: the closed form
  `(n−1)(n−2)π³/(3n³)` is exactly right, but three decimals are wrong —
  n=6 `0.95672` (true 0.9569838), n=7 `0.90369` (true 0.9039731), n=12
  `0.65779` (true 0.6579264).
- Two tables in one chapter disagree on one quantity: `−1.17751` vs
  `−1.17753` for N=7 (true −1.177525130).
- `canonical-braid-interface-composition-table3` row 1 gives `(1,1,1)` for
  `pppnnn`, but the parent block's own closed form gives `(2,1,2)`; the
  printed triple is the A=4 answer and duplicates row 3. The table is also
  **orphaned** — nothing in the parent `.md` references it.
- `n_pp` means two different things one chapter apart: `Z(Z−1)/2` (pairs)
  in `derived-mass-formula-light-isotopes`, `max(0, Z−1)` (adjacent
  interfaces) in `canonical-braid-interface-composition`. They agree at
  Z=2 and diverge at Z=3.

Infrastructure: `dt-spectrum-bar-eigenspace.ts` has `uses: []` while its
`.md` cross-references `conj:stokes-dt-bps-bridge` twice — §3b propagation
is *not* breached (the statement is unconditional integer arithmetic) but
the dependency is invisible to the graph. `descent-rate-probe-sim.md` is
empty (1 byte), so the `β(d) = 1` evidence that `rem:mass-tower-syt-cells`
cites *through* it is unreachable from the paper.

Recorded clean, so a later pass does not "fix" them: `Vol(4₁) =
2·Cl₂(π/3)` is right in both name and coefficient here, and the `T_w` in
`e-infinity-page-identifications` is the Hecke basis element sanctioned by
the cheat sheet, not a §7a generator violation.

---

## From agent:r07 (mass-theory nq_01) — 2026-08-21

25 findings over 42 blocks. The one that matters most is confirmed twice,
by two independent routes.

### `figure-eight-branching-rule` states a word that closes to the unknot

The block gives `4₁ = σ₀σ₁⁻¹σ₀⁻¹σ₁` — the commutator on three strands.
Cyclic permutation plus `σ₁⁻¹σ₂σ₁ = σ₂σ₁σ₂⁻¹` reduces it to `σ₁σ₂⁻¹`, and
two destabilisations give the **unknot**.

This is not a typo in the prose, and that is what makes it expensive.
`agent:r07` built the 2-dimensional `[2,1]` Hoefsmit representation in
sympy (braid relation verified) and found
`χ(σ₁σ₂⁻¹σ₁⁻¹σ₂) = −q² + 1 − q⁻² = −1 − h²`, which is **exactly Table 1's
entry**, while the true figure-eight `(σ₁σ₂⁻¹)²` gives
`q⁴ − 2q² + 1 − 2q⁻² + q⁻⁴`. So Table 1, `b_λ = −f^{λ/[2,1]}h²`, and every
Table 2 assignment are characters of an unknot-closing braid presented as
`4₁`. Correcting the word alone would leave the tables wrong; they need
regeneration.

Confirmed here by a different method —
[`content/pipeline/braid-alexander.ts`](../content/pipeline/braid-alexander.ts),
reduced Burau over exact `ℤ[t,t⁻¹]`:

| word | Alexander | |
|---|---|---|
| `σ₀σ₁⁻¹σ₀⁻¹σ₁` (as stated) | `1` | the unknot |
| `(σ₀σ₁⁻¹)²` (sibling block) | `1 − 3t + t²` | genuinely `4₁` |
| `σ₀³` (control) | `1 − t + t²` | `3₁` |

The sibling `figure-8-archimedean-illustration` carries the correct word,
so the chapter disagrees with itself.

### Three convention-C leaks, each load-bearing rather than cosmetic

1. `explicit-alpha-k-h3-proof` — the "equivalently `α₃ = z(1+q^{1/2}−q^{−1/2})`"
   step requires `h·z = q^{1/2} − q^{−1/2}`, true only at `z_C`. It
   evaluates to **0.676645** against the correct convention-D **0.691166**,
   a 2.1 % error rather than a restatement. (The statement block's boxed
   `q³(q⁴+1)/(q²+1)²` is exact under D, verified to 1e-31.)
2. `explicit-alpha-k-h4-proof` — the headline `tr_M(r₃) ≈ +0.003463` is a
   convention-C number. With the statement table's exact `(1⁴)` row, sympy
   gives `tr_M(r₃) = 0` **identically in q** under D, and
   `0.003462520932` under C — the quoted value to every digit.
3. `flavor-dressed-mass-from-substrate-split` — its two displays are equal
   iff `1/z = q^{1/2}+q^{−1/2}`, i.e. `z_C`. Both give **1.286429856 MeV**
   there (residual 4e-31); canonical `z_D` gives **1.048397466 MeV**, an
   18.5 % gap. Worth stating neutrally: the C value sits 0.53 % below
   CODATA `Δ_np = 1.29333`, in a block whose closing line stresses that
   `Δ_np` is "no longer an input".

### Claims that do not hold as written

- `em-spectral-completeness` clause (4): `w± = (dim_q V±)²/[2]_q!` cannot
  sum to 1 at `q ≠ 1` — the corpus's own `w_λ = [n]_q!/H_q(λ)²` gives
  `2/[2]_q = 0.99458`, the categorical reading `5.10426`. The fix is
  already in the corpus: the **linear** normalisation the four sibling
  Feynman blocks use, `w_λ = dim_q(V_λ)·dim(S_λ)/dim_q(V^{⊗n})`, is 1
  identically at n=2 because `[2]_q² = [3]_q + 1`. No `.lean` sibling
  exists, so nothing machine-checks the clause.
- `faddeev-phib-uniqueness`: two of three rigidity inputs are false on the
  block's own branch. `Φ_b(z)Φ_b(−z)` is not constant (it swings from
  `6.717e6+1.951e6i` to `−5.527e6−4.287e6i`), but
  `Φ_b(z)Φ_b(−z)/e^{iπz²} = 6994799.44082` at every test point — the
  relation is Faddeev's **Gaussian** inversion, not `= c₀`. And
  σ-unitarity fails: `|Φ_b(0)| = 2644.77` against `|Φ_b(1.1)| = 142623`.
  The branch making the products converge is the one destroying unitarity.
- `frobenius-antipode-unifies-chirality-and-tower`: `S(σᵢ) = σᵢ⁻¹` is not
  an endomorphism of `H_n(R,q)` — `σ⁻¹` satisfies `(x−q⁻¹)(x+q) = 0`, so S
  is the KL **bar involution**, semilinear over `q ↦ q⁻¹`. A sibling
  (`flavor-split-habiro-derivation`) uses the same symbol `S` for
  `T_w ↦ T_{w⁻¹}`, which **fixes** every generator.
- `explicit-alpha-k-h4-proof`: the six length-3 elements of `S₄` are two
  **transpositions** and four 4-cycles, not "3-cycle + 4-cycle" — 3-cycles
  have Coxeter length 2. The counts (6, and 2 classes) are right.
- `feynman-classical-limit`: `z → 0` is false (both conventions give
  `z = 1/2` at `q = 1`) and contradicts the block's own `tr_M(σᵢ) = z`.
- `exceptional-divisor-reeb-intro`: the Garside element `Δ = σ₁σ₂σ₁` closes
  to the **Hopf link**, Seifert-fibered with `V_hyp = 0`; `Δ²` closes to
  `T(3,3)`, also 0. Only the Borromean half of that sentence is right.

### Policy

`frobenius-antipode-neutron-tower-closure` puts an excised-class claim and
an anti-fit violation in six sentences: "dramatically corrects the neutron
mass … sub-ppm match **at the precise optimal mixing value**". Absolute
`m_n` is the excised class (2026-08-11) and is on the L2 miss list; a
parameter tuned to its optimum is a fit, and the next sentence reads it as
"confirms the structural role". No values, no witness, no pin anywhere in
the block.

Two more §7a generator violations (`T` for `σᵢ`): `eigenvalue-product-expansion-proof`,
`feynman-classical-limit`. Token substitution confirmed at 8 further sites,
including bold heads and sentence-initial lowercase "canonical evaluation",
which is what proves a capitalised "Numerical" was replaced.

### Recorded clean, so a later pass does not re-flag them

`five-two-saddle-sum-rule` verifies to **30 dps** (residual 1e-30), with
model epistemic labelling. `flat-tetrahedron-zero-volume`,
`feynman-eigenbasis-decomposition{,-proof}`, `finite-connes-forces-trivial-kernel`
and `flavor-mass-splitting-bound` are correct throughout.
`frobenius-…-interpretation`'s `G/3 = Vol(𝓑₃)/24` is exact because
`Vol(Borromean) = 8G` — though the `24 = |S₄|` reading is an
interpretation, not a consequence.

### Operational

Two agents collided on the shared path `/tmp/rec.sh`, silently zeroing one
helper's variables and costing a block's recording. Agent scratch paths
must be namespaced per batch id.

---

## From agent:r08 (mass-theory nq_02) — 2026-08-21

26 findings over 41 blocks, the densest batch of the campaign. Grouped by
what a reader would have to un-believe.

### The Gram-matrix cluster — four blocks, one tangle

1. **`gram-degeneracy-blocks-connes` gets both halves of one sentence
   wrong.** It states the convention-D star-form spectrum as
   `0, 0.752702^{×3}, 4.230339`, "exactly one null direction, and it is the
   **braid-symmetric** one". Rebuilt at 40 dps: the multiplicity is **×4**,
   not ×3 — the quoted list holds five eigenvalues for a six-dimensional
   form, and ×3 is the *bilinear* multiplicity, precisely the pairing
   confusion `prop:frobenius-gram-matrix` warns against one file away. The
   kernel vector is `(1, −0.900918284, −0.900918284, 0.8116537544,
   0.8116537544, −0.7312337075)` = `(−1/q)^{ℓ(w)}` to ten digits: the
   **q-antisymmetriser**, the `(1³)` block this chapter twice calls the
   radical. The symmetric direction has coefficients `q^ℓ` and is not in
   the kernel.
2. **`frobenius-gram-matrix`: the printed matrix does not produce the
   block's own numbers.** Every quoted value reproduces only with
   `tr_M(e⁻) = hz²+z` substituted (det G = 0 under D, spectrum
   `(−0.752702113, 0, +0.752702113^{×3}, +4.23033923)`; under C
   det G = −0.1892052191). But the block twice says the matrix is written
   with the naive `z³` and that the correction "has still to be
   propagated" — and with the naive entries det G = −0.334741 under D,
   **nonzero**, with no null eigenvalue. "det G = 0 identically" is false
   of the matrix as printed.
3. **`frobenius-gram-matrix-context`: convention-C numbers under an
   explicit convention-D declaration.** It writes "`z = q³/(q²+1)`
   (**convention D**)" and then `hz²+z ≈ 0.5514`, stale `z³ ≈ 0.1245`,
   "off by a factor of 4.4". Under D those are 0.69117, 0.22999 and 3.005;
   0.5514/0.1245/4.43 are the **C** values to every digit.
4. **The LP-dual trio rests on a premise this chapter refutes.** Its Step 1
   asserts non-degeneracy because "every `y_λ(q) ≠ 0`". Under canonical D,
   `y_{(1³)} = 0` at n=3 and det G = 0 — stated in two sibling blocks and
   reproduced independently. Steps 1–5 and both corollaries are
   convention-C statements; `Φ_τ` lives on `H_n/rad`.

### A wrong map, with the right one derived

**`frobenius-s-classification-proof`**'s antipode `(c,d) ↦ (c, d − c·h_A)`
is not an involution (`(1,0) → (1,−h_A) → (1,−2h_A)`) and does not preserve
`det T` (`Δ = −2cd·h_A`), so it cannot support the block's own
"`det` is S-invariant", and it contradicts Table 3's `S(1,−h_A) = (1,0)`.
The correct map is **`(c,d) ↦ (c, −c·h_A − d)`**: involutive,
det-invariant identically, and it reproduces all three table rows. It
agrees with the stated rule on `(1,0)` alone — which is why the `Φ₃`
spot-check still passed.

### Two off-by-ones that change a headline number

- **`graded-hecke-energy-truncation-bound-table`**: the theorem bounds the
  nonzero grades by `ℓ+1`, so the speedup is `p(n)/(ℓ+1)`. The table
  reports `p(n)/ℓ` — 1.5, 2.2, 3.7, 7.0 against the correct 1.0, 1.83,
  3.33, 6.42. **The proton and neutron rows should read 1.0×: no speedup
  at all.**
- **`geometric-invariant-piecewise`**: `ℏ_q² = 0.009817186`, so
  `Vol/ℏ_q²` **multiplies by 101.86** and `CS·ℏ_q²` suppresses. The block
  says the reverse of both.

### Convention C, in the spelling the taxonomy calls invisible

`frobenius-s-classification-proof` defines `z = 1/(q^{1/2}+q^{−1/2})`, and
its table-2 sibling repeats it as `(q^{1/2}+q^{−1/2})^{−1}`. That is
`√q/(q+1) = 0.4993203342` — convention C exactly. This is the
reciprocal-of-sum form recorded in the detector-blindness taxonomy, and it
survived the 2026-08-10 content-only drain.

### A recurrence AGENTS.md §7b names, found twice in one flight

`garside-as-compound-flow` runs the dilogarithm on `Δ₃ = σ₁σ₂σ₁`, whose
closure is the **Hopf link** (`s₁s₂s₁ = (1 3)`, two cycles; cyclic
permutation to `σ₁²σ₂` destabilises to `σ₁²` in `B₂`). Its complement is
`T² × I` — Seifert fibred, volume 0, `D(z) = 0` — so "does not admit a full
Seifert fibration / JSJ contains a hyperbolic piece / positive
Bloch–Wigner sum" is false for that closure. `frobenius-gram-matrix-proof`
misnames the same element "the trefoil". Independently, `agent:r07` found
the same class in `exceptional-divisor-reeb-intro`.

### Numbers that do not reproduce, and a scope-(b) overclaim

`frobenius-cocasimir-refuted-deuteron` quotes "+0.145 m_e"; the signed sum
in its own witness is **+0.2482770936** (per-λ contributions recomputed
independently; the −4.353365006 target is right). The same block writes
"This algebraic refutation eliminates the co-Casimir ansatz as a universal
correction factor" — a scope-(b) exclusion from one numerical probe at one
isotope with no invariant cited, and "algebraic" mislabels a 70-dps mpmath
evaluation.

### Structural

`graded-hecke-energy-truncation-bound` is a `proposition()` whose `uses[]`
lists `conj:gs-graded-markov-trace-existence` directly and whose proof
opens "By [that conjecture]", with no conditional banner — a §3b
propagation violation as written. `gram-matrix-spectral-connection` carries
five separate defects including a struck-through sentence left in published
prose. `full-pole-structure-mass-trace` discharges "Property (1)–(3)" in
its proof and interpretation while the proposition numbers no properties.
Two incompatible Wedderburn weights appear one file apart
(`dim_q·dim/[n]_q!` vs `dim_q²/[n]_q!`, equal only at q=1).

Token substitution: 7 further sites in 3 blocks, including sentences
opening on a bare "canonical" and "extending the the formal derivation
formalism" with a doubled article.

### Recorded because it is good

`ground-state-ordering` is the best block seen in the campaign: an explicit
Lean-backed counterexample, exact unrounded tallies, a scope-(b)
classification with its licensing invariant named, the empirical part
labelled empirical and capped at A ≤ 16, and a refusal to settle the
downstream question. Its one flaw is an *under*-claim — if the gap factors
as `(t−1)` times an all-positive degree-20 polynomial, it holds for every
`q > 1`, not merely "an interval containing the anchor".

---

## From agent:d01 (quantum-observable-universes dq_01) — 2026-08-22

45 blocks, only 4 trap fails — this chapter's prose is clean, and the yield
is mathematical. 15 anomalies; the first three carry consequences.

### The uniqueness proof proves a different operator than the definition gives

`categorical-q-ext-deriv-unique-proof`. Derived rather than eyeballed: with
`P = q⁻¹·id + (1−q⁻¹)π_V` and `π_H = id − π_V`, the **definition** gives

    d_q = P ∘ d

while the **proof** works with

    d′ = q⁻¹ d ∘ π_H + d ∘ π_V = d ∘ P.

Those agree iff `[π_V, d] = 0` — which this chapter's own `d_q² ≠ 0`
result denies. The same hidden hypothesis sits under
`categorical-q-ext-deriv`'s prose claim that `d_q` "acts as `q⁻¹d` on
horizontal forms and as `d` on vertical forms": `π_V` acts on the *output*
of `d`, so that reading needs `d` to preserve the H/V splitting.

### Lichnerowicz Step 4 is off by a factor of 0.8018, and drops a term

The step asserts `q⁻²∇² − ℏ_q²∇_ξ² = ∇*∇`. Its algebra is **correct** —
`q⁻² − ℏ_q² = (2−q)/q`, since `1 − (q−1)² = 2q − q²` and `ℏ_q = 1 − q⁻¹`
gives `qℏ_q = q−1`. But that quantity is not 1: at 30 dps it evaluates to
**0.801836567911** at the proton pin (0.801836547123 at muon), so the
identity is off by ~19.8 %. The same step also drops `L_ξ∇` without
comment.

### A definition whose axiom collapses its own decomposition

`categorical-reeb-brings` computes `ι_ξ dΘ_A = 0` — correct, that *is* the
classical Reeb condition, and it follows correctly from
`ι_{e₃}(ω₊ ∧ ω₋) = 0`. But `def:categorical-reeb`'s axiom
`π_V ∘ d = ι_ξ dΘ_A` then forces `π_V ∘ d = 0`, collapsing the
horizontal/vertical decomposition the chapter is built on. One of the two
is wrong, and the definition is the likelier culprit.

### Naming and typing, in a chapter where both are load-bearing

- **One term, two morphisms.** `def:categorical-reeb` and
  `def:categorical-reeb-derivation` both bold "categorical Reeb
  derivation" for different objects (`ξ` vs `ξ_q`) under different
  normalisations (`Θ_A(ξ) = id₁` vs `ξ_q ∘ Θ = Θ`).
- **The Dirac operator has two fonts**: `𝔇_∇` (fraktur) in
  `prop:categorical-lichnerowicz`, `𝒟_∇` (calligraphic) in all four
  Lagrangian blocks, both citing `def:categorical-dirac-operator`. §7aa
  admits at most one.
- **`Ω_q`** (Reeb period) collides with `Ω^k(A)` (forms) across the
  chapter; `ξ` serves as both Reeb generator and Fourier spectral
  variable.
- **Three codomains for one formula**: `tr_M(exp_q(−s·)·f)` is declared
  into `End_C(A)` by `def:categorical-laplace`, called an element of
  `Hom(1, A)` by its exists-proof, and as a Markov trace lands in
  `Hom(1,1)`. `def:categorical-fourier` repeats the mismatch.
- **Type mismatch** in the Lagrangian's second summand: `ψ* ⊗ 𝒟_∇ψ`
  composes to `Hom(A, Ω¹(A))`, not `End_C(A)`, unless `Ω¹(A) ≅ A` —
  asserted away as "via the rigid pairing".

### Vacuous and near-vacuous statements

`prop:categorical-lagrangian-unique` reads "any endomorphism equal to *the
formula* coincides with `L_q`" — true by substitution. Its proof's preamble
claims uniqueness follows "by enforcing the variational equations", and the
body enforces none; that absent variational characterisation is exactly
what would make the proposition non-vacuous, so deleting the preamble
should be paired with a decision on the claim itself.
`categorical-irreducible-proof` closes on a non sequitur: `∫_A` vanishing
on `Ad(A)` plus *global* non-degeneracy does not give `s = 0` without
non-degeneracy of the **restricted** pairing.

### A banner in the wrong chapter

`categorical-q-ext-deriv-unique` is the only block in this purely
categorical chapter carrying the "sits on the archimedean side of the
substrate wall" note (140 files corpus-wide). It has no real, no `q₀`, no
numeric and no transcendental; its `.ts` has no archimedean tag; its proof
uses only `π_H + π_V = id`. It is also positioned last, so nothing follows
what it announces.

### Verified correct, so a later pass does not re-flag them

The q-Lie bracket's antisymmetry and its `q = 1` limit; `∇_q → ∇` at
`q = 1`; the q-heat resolvent `û = (s + Δ̂_q)⁻¹u₀` including sign and
initial datum; the Bogomolny decomposition's factor 2 and topological term;
Bring's curve `8 = 2g` with `g = 4` and `S₅`-equivariance; and the
`q⁻² − ℏ_q² = (2−q)/q` algebra itself — it is the *use* of it that fails,
not the identity.
