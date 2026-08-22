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

**L-V3. [q11/q13] FIXED 2026-08-22 — and the ledger had the defect
backwards, in the direction that matters.**
`lifting-and-descent/blowup-regularity-as-lifting.md` L6 `\foralln` and L8
`\varepsilonq^{2k}` are **not** undefined and do **not** abort the render.
`main.tex` defined both, in a block of 16 `\newcommand`s headed *"Stubs for
compound macros (missing spaces in source content)"*. That is why nobody
noticed them: the stub makes the page compile and prints something.

What it prints is the problem. `\varepsilonq` expanded to `\varepsilon_q`,
so `\varepsilonq^{2k}` typeset ε_q^{2k} where the asymptotic is a constant
times q^{2k} (`[k]_q² → q^{2k}/(q−q⁻¹)²`). Two of the sixteen were worse:

- **`\pic` expanded to `\pi`, deleting the `c`.** In
  `fluid-dynamics/acoustic-horizon-thermodynamics.md`,
  `\frac{\hbar_q\kappa_H}{2\pic_s}` printed `2\pi_s` — the sound speed
  gone from a Hawking-temperature denominator. Line 28 of that same block
  writes `\kappa_H/(2\pi c_s)` correctly in prose, which is what settles
  the intended reading: the block contradicts itself on one page.
- **`\xid` expanded to `\xi_d`**, so `\mathcal{L}_\xid\alpha` printed a
  Lie derivative along a subscripted field with no argument. `\xiZ` is the
  same shape: `\mathcal{L}_\xiZ = J\hbar_qZ` printed an operator equated
  to a scalar, where the prose says the Reeb flow rotates the phase of Z —
  i.e. `\mathcal{L}_\xi Z = J\hbar_q Z`.

`\xid`, `\xiZ`, `\xiA` were commented as *"Reeb vector field variants used
in contact/brane geometry"*. No such notation is registered anywhere under
`content/quantum-observable-universe/notation/`. The comment documents three
typos as though they were notation, which is how a typo acquires a citation.

All 16 stubs removed (`7d1a616ae`) from the three preambles carrying them,
and all 11 remaining source sites fixed across 6 blocks. `\pp`, `\unicode`
and `\yng` stay — real stubs for a reserved symbol and two unloaded
packages. A corpus scan for the whole class (rare control sequences whose
prefix is a common one) now returns only true macros: `\coloneqq`,
`\rightarrow`, `\rightsquigarrow`, `\dotsb`, `\texttt`, `\bigm`,
`\inf`, `\top`.

**The general lesson, since it will recur:** a missing space between a
control sequence and the next token is *not* a render-breaking error unless
the glued name is undefined. Defining it is the tempting fix and the wrong
one — it silences the error and keeps the wrong mathematics. If one
reappears, the undefined-control-sequence failure is the correct outcome.

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

**Refreshed 2026-08-22.** The three items this section previously listed are
resolved: the `trefoil-operator-algebra` matrices were rewritten with a
genuine conjugate pair, 18 braid-word rows were corrected across three
tables, and the q₀ presentation pass landed. What follows is ranked against
the ledger as it now stands (~280 items, 62 % corpus coverage), newest
batches included. Ranking is by *how far the error propagates*, not by how
wrong it looks.

### Tier 1 — wrong mathematics with live downstream consumers

1. **`figure-eight-branching-rule` computes on the wrong knot.** It defines
   `4₁ = σ₀σ₁⁻¹σ₀⁻¹σ₁`, whose closure has Alexander polynomial 1 — the
   **unknot**. The genuine `(σ₀σ₁⁻¹)²` gives `t − 3 + t⁻¹`. Every `b_λ·h²`
   term in the block is therefore computed on the wrong object, and in
   `[2,1]` the true character `q⁴ − 2q² + 1 − 2q⁻² + q⁻⁴` agrees with the
   block's `−1 − h²` only at q = 1. **Three independent confirmations**
   (agents `r07`, `f00`, and a separate implementation in the coordinating
   session). This is the ledger's strongest item.

2. **`c₅` is carried at two different values across five blocks**, and only
   one reproduces the published headline. Proposition + tables 1–2 use
   `−(b²+½) = −1.2527`; the context block + table 3 use
   `3c₃² + b = +12.868`. At `u⁵ = 4.4822e−11` the second gives the
   "+0.04 ppb" result and the first does not. The proposition carries the
   superseded coefficient — so the *statement* block is the wrong one.

3. **A uniqueness proof proves a different operator than its own definition
   gives** (`agent:d01`), and separately **`ω_V` is identically zero**,
   which makes the proposition asserting its properties vacuous. Both are
   structural: the Lean and the prose diverge, so neither audit catches it
   alone.

4. **Convention-C dependence hidden inside identities, not assignments.**
   `toroidal-harmonics-delta-lambda` turns on `w = z² = 1/(2(cosh η + 1))`,
   exact for `z_C` to 1e−31 and off by 51 % for `z_D`;
   `frobenius-s-classification-table2` spells C as `(q^{1/2}+q^{−1/2})⁻¹` and
   it is load-bearing — the "+1" S-eigenvalue and the parent's "exactly one
   S-odd term" are statements about C, and switching to D moves a refuted
   family from `m ≥ 4` to `m ≥ 5`. **No grep over `z = …` finds either.**
   This is the class the detector-blindness taxonomy predicts, now with
   worked instances.

### Tier 2 — claims a referee would stop on

5. **`three-halves-structural-factor` overstates by ~1600×**: it claims
   `Vol(4₁)/ℏ_q²` closes `m_μ/m_e` "to 0.034 %"; the true figure is
   **209.8 ppb**, which is exactly the documented μ–p tension, and zero at
   the muon pin where the relation *is* the pin. Its τ sentence is
   impossible as written (omits ξ₃; the cited witness's own ξ₃ reproduces
   its recorded 0.79443 % exactly).

6. **`topological-mass-trefoil` prints a number matching no pin.** 207.1
   back-solves to q = 1.1098808 — not proton, not either muon value, not the
   1.1097 error. The correct 206.7683 is 2.1e−5 % from CODATA; the printed
   value misses by 0.160 %, understating the block's own result by four
   orders of magnitude.

7. **The excised absolute-mass double-counting is still shipping.**
   `tower-binding-energy-table-data` reproduces its own "mass error" column
   exactly — and that column is the artefact: the underlying binding errors
   are +121.6 % (²D) and −31.4 % (⁴He), pressed below 0.25 % by a
   denominator dominated by `Z·m_p + N·m_n`, i.e. by the calibration.

8. **`𝒲(1) = 0` is false** (it is `z² = 1/4`), and **CODATA α appears inside
   the derivation of α**. Two tautologies are presented as Mathlib gap
   closures. Each is a single block, but each is the kind of thing that
   discredits neighbouring correct work.

9. **Proof steps that do not hold**: step 3(c) of the stratified proof fails
   at λ = (2,1) (22 counterexamples to n = 7); step 3(d) equates a monomial
   to an infinite product; step 4 needs an orthogonality its step 1 does not
   supply.

### Tier 3 — provenance and currency, cheap to fix, corrosive if left

10. **Citations that do not resolve or do not say what is claimed**: a
    witness path containing a space that matches nothing in `computations/`
    (the space is itself sweep damage, so the *sweep created the citation*);
    a witness reporting `allPassed: false` cited as confirming; a witness
    sourced from `_deprecated/` at the old muon pin whose own notes say it
    needs a further iteration; three blocks whose prose names one pin while
    their witness records the other.

11. **Sweep damage, three recurring shapes**: `canonical` substituted for
    `numerical(ly)` ("pinned canonical by the dimensionless ratio"); script
    names replaced by "the canonical formalism" / "the formal derivation",
    leaving quoted percentages provenance-free; sentence-initial lowercase.
    Mechanical, but the second shape destroys provenance rather than merely
    reading badly.

12. **The compound-macro stub class — resolved, recorded as precedent.**
    `main.tex` carried 16 `\newcommand`s that promoted author typos to
    macros so the page would build; two printed wrong mathematics for
    months. Removed, all source sites fixed, and
    `content/pipeline/glued-macro-scan.ts` added. Kept here because the
    tempting fix recurs: **never define the glued name.**

### What is NOT in this list

Roughly 40 % of the ledger is verified-correct notes — blocks recomputed
from scratch and found right, recorded so a later pass does not re-flag
them. Those are not a backlog. Useful negatives among them include: no table
audited so far discriminates the proton pin from the muon pin at its printed
precision (though `1.1097` *is* excluded by several), and the Hoefsmit
tableaux, Plancherel weights, skew-SYT counts and `Σ 1/dim_q` exact
rationals all check to the last printed digit.

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

---

## From agent:d00 (quantum-observable-universes dq_00) — 2026-08-22

45 blocks, 18 anomalies. The chapter's prose is clean; the yield is in the
mathematics and in one structural pattern that spans six blocks.

### The pattern: a proof preamble that narrates a proof that is not there

Six proof blocks open with the same two-or-three-sentence "The proof
strategy is… / We explicitly…" construction. Two were pure prose and were
deleted inline; four carry formulas or new symbols and are flagged. **Two
of the four describe a method the body never uses:**

- `categorical-dirac-operator-unique-proof` promises "assume a general
  affine operator `α∇ + βι_ξ∇`, apply the categorical constraints, they
  force `α = q⁻¹`, `β = 1−q⁻¹`". No constraint is applied; the body says
  the same combination is "literally the same morphism".
- `categorical-fourier-transform-unique-proof` promises "the
  representation ring structure pins down the labels"; the body is a Wick
  rotation from Laplace uniqueness.

This matters beyond style: in the Dirac case the advertised argument is
precisely the one that would make the proposition non-vacuous (see below),
so the preamble is standing in for missing content rather than decorating
present content.

### Statements that are vacuous or cannot hold

1. **`adjoint-trace`'s Killing-form identity is vacuous where it is true
   and false elsewhere.** The claim is `tr_Ad(f) = tr(ad f) = −2 tr_{ℂ²}(f)`.
   Route: sympy over a `gl(2)` basis. On all three standard `su(2)`
   generators `tr(ad X) = 0` (ad is traceless on a perfect algebra) and
   `tr_{ℂ²}(X) = 0`, so the chain reads `0 = 0 = 0`. Off `su(2)` it fails —
   `f = id` gives `0` against `−4`. And the normalisation is wrong
   regardless: computing `B(X,X)/tr(X²) = −8/−2 = 4` on each generator
   gives **`B(X,Y) = 4 tr(XY)`**, not `−2`.
2. **`categorical-dq-squared-proof`: `ω_V` is identically zero as
   defined.** `ω_V = d(π_V(d 1_A))`, and `d(1_A) = 0` in any first-order
   calculus, so `ω_V = 0` — which makes the proposition's own right-hand
   side vanish for every `α`. The same proof has a degree mismatch:
   `[d, π_V]α = π_H(𝓛_ξ α)` puts degree `deg α + 1` on the left and
   `deg α` on the right. Its "if and only if" also over-claims: the
   prefactor does vanish exactly at `q = 1`, but the product also dies when
   `ω_V = 0`, which given the above is not a hypothetical branch.
3. **`categorical-dirac-operator-unique` is a tautology.** "Any morphism
   decomposing as `α∇ + βι_ξ∇` **with `α = q⁻¹`, `β = 1−q⁻¹`** equals
   `𝒟_∇`" — the same expression equalling itself, as the proof concedes.
   The non-vacuous statement is the classification its preamble advertises.
4. **`braiding-induced-ordering` assumes `c² ≠ id` and never uses it.**
   The proof is a degree-lex well-ordering on words over `{1..n−1}` and
   goes through for any braiding.

### Errors of fact

5. **`brings-coordinate-ring`: `S₅` is not an automorphism group of
   `O_q(B)`.** With `x_i x_j = q x_j x_i` for `i < j`, the transposition
   `(i j)` sends that relation to `x_j x_i = q x_i x_j`, while the ring
   gives `q⁻¹`. Permutations act by algebra automorphisms only if
   `q² = 1`. (Correct in the same block: `g = 4`, `2g = 8` cycles, and
   `Aut(Bring) = S₅` classically.)
6. **`categorical-coordinate-ring-proof`: two specialisation rows are wrong
   as rings.** `ℂ[i]/(i²+1) ≅ ℂ × ℂ` by CRT — `i²+1` splits over `ℂ` — not
   `ℂ`. Rows 2 and 4 are right. The displayed conjugation
   `z → z⁻¹ → qz⁻¹ → q⁻¹z` checks out exactly.
7. **`categorical-action`'s duality maps do not compose**, across five
   blocks. The definition composes `ev_A ∘ (id_{A^∨} ⊗ Φ) ∘ coev_A` while
   declaring `ev_A : A^∨ ⊗ A → 1` and `coev_A : 1 → A ⊗ A^∨`; the proof's
   display then flips to `Φ ⊗ id` and applies `ev_A` to `A ⊗ A^∨`,
   contradicting both propositions and its own prose. One side needs
   fixing consistently across def + 2 props + 2 proofs.
8. **`categorical-dirac-operator-exists-proof` types `ι_ξ` wrongly.** With
   `ι_ξ : Ω¹(A) → A`, `ι_ξ∘∇ : A → A`, so `𝒟_∇ = q⁻¹∇ + (1−q⁻¹)ι_ξ∇` adds
   `A → Ω¹` to `A → A`. The definition's own phrase "its projection onto
   the Reeb direction" says `ι_ξ` should be `Ω¹ → Ω¹`.
9. **`braiding-unit-circle-convention`'s name contradicts its content.**
   The "inside-unit-circle convention" sets `q := λ₊`, and for real `q > 1`
   that root lies *outside*; `|λ₋| = q⁻¹ < 1` is the one inside.
10. **`categorical-fourier-transform-properties`**: "functions identically
    over `𝔽_p`" is false without semisimplicity (`p ∤ |G|`, `q` not a bad
    root of unity). The title also promises Wick rotation, which the body
    never discusses.

Smaller: a §7a violation (`(T−q)(T+q⁻¹) = 0` where the generator must be
`σ_i`, in `braiding-eigenvalue-extraction`); `κ ∈ H²(𝒮, 𝓑)` colliding with
`𝓑` for Bring's curve; `𝒜` for the Frobenius–Hopf object where the chapter
uses `A`; and "intrinsic *topological* invariant" claimed for what is a
categorical uniqueness statement, with nothing topological anywhere in the
Fourier cluster.

### Convention checks, all clean — recorded so they are not re-run

The only numeric in 45 blocks is `q₀ ≈ 1.10998`, and it is **correct**:
recomputed from CAL-2, `Vol(4₁) = 2·Cl₂(π/3) = 2.029883212819307` with
CODATA `m_μ/m_e = 206.7682827` gives `q₀ = 1.10997859564`, whose rounding
at that precision matches both real pins and is not the erroneous `1.1097`.
No Markov `z` appears anywhere in the batch, so no convention-C exposure.
Categories are bold `𝐂` throughout, the fibre functor is always `τ`, the
tuple is always `(𝐂, Θ, G, 𝒮)`, and the deprecated 5-tuple appears
nowhere. No §3b propagation violation, no mass claims, no braid words.

New sweep-damage shape, distinct from the token-substitution class: a
synonym swap for *is* and *ensures* — `operates as`, `acts as`, `secures
positivity`, `securing the smoothness`, `functions identically`, plus
`leverages` twice in proof preambles. Five instances across five blocks.

---

## From agent:d02 (quantum-observable-universes dq_02) — 2026-08-22

42 prose blocks plus 3 data tables. Six trap fails, four inline fixes, and
29 anomalies. One was fixable and is already fixed; the rest are recorded.

### Fixed: a macro collision that silently typeset the wrong operator

`dq-squared-proof` wrote `\mathcal{L}_\xid\alpha`, intending the Lie
derivative along `ξ` of `dα`. But `\xid` is a **real macro** —
`main.tex:222` defines it as `\xi_d` — and LaTeX matches the longest name,
so the PDF rendered `L_{ξ_d}α`. The key cancellation therefore typeset as
`Θ ∧ L_{ξ_d}α = Θ ∧ dL_ξα`, which is not the identity being claimed; on the
KaTeX path it errors instead. Two sites, both in that block, none elsewhere
in `content/`. Rewritten with braces so the macro cannot re-collide.

The agent checked whether `\xid` was a typo or a definition before
reporting it, which is what made this actionable rather than a guess.

### `g-action-on-substrate`: the headline number, and why it survives

The block's result is `N_sym(q₀)` against a target `213.11`, quoted at
`−1.81 %`. Recomputed at 50 dps with the balanced `[n]_q`:

| quantity | printed | recomputed (proton pin) |
|---|---|---|
| `[4]_q²` | 16.892 | **16.88949** |
| `[2]·[4]²·[6]` | ≈ 216.96 | **216.9587226** |
| residual | −1.81 % | **−1.80598 %** |

So `16.892` is a round-then-square artefact (`4.11² = 16.8921`), and the
line that multiplies the printed values gives `216.9884`, disagreeing with
the `216.96` on the same line. **The −1.81 % headline is nonetheless
correct**, because it was computed from full-precision values — which the
pin test confirms: proton and muon agree to eight figures here
(`216.9587226` vs `216.9587285`), while the erroneous `1.1097` rounding
would give `216.8325` and print `−1.75 %`.

Three structural problems in the same block matter more than the rounding:

1. **`⊕` where the derivation needs `⊗`.** The trace display takes `dim_q`
   of a **direct sum** `A^{(W⁺)} ⊕ A^{(W⁻)} ⊕ A^{(Z)}` and the next step
   **multiplies** `[4]·[4]·[6]`. `dim_q` is additive over `⊕`:
   `[2]·([4]+[4]+[6]) = 29.374`, not 216.96. The derivation does not follow
   from its own display.
2. **An input outside the three calibrations.** (G-3) fixes
   `tr_F(ϱ*ϱ) = v²/m_e²` with `v ≈ 246 GeV`, "the empirical Higgs VEV".
   Mitigating, and worth stating because the authorNotes claim every factor
   is derived: (G-4) divides by exactly that trace, so `v` cancels and
   never reaches `N_sym`.
3. **The target has no provenance.** "the CODATA target `N_sym(q₀) =
   213.11`" carries no citation, no derivation and no witness field, and
   the entire −1.81 % rests on it.

Also: `e_H` is called a **rank-1** projector yet assigned trace dimension
`[2]_q`, the value (G-2) gives to *all* of `A^{(H)}`; Table 1 assigns the
photon a trivial `(0,0)` while giving Z the mixed weight, though both are
W³–B mixtures, and its last row ("residual matter sector") is not an
irrep, contradicting (G-1)'s "each `A^{(X)}` carries a unique irreducible
representation"; Table 2 names rows for Goldstones whose `q`-dimensions the
body assigns to the **gauge** components.

### Axioms that do not constrain what they name

`frobenius-hopf-substrate` axiom 3 reads "the Frobenius form `λ` satisfies
`μ∘Δ = (Δ⊗id)∘α∘(id⊗μ)`" — **`λ` never appears in it**, and the two sides
do not compose (`A→A` on the left; `A⊗A⊗A → A⊗A → A⊗A⊗A` on the right).
The standard form is `Δ∘μ = (μ⊗id)∘(id⊗Δ) = (id⊗μ)∘(Δ⊗id)`. In the same
block **the antipode `S` is unconstrained**: it sits in the sextuple and is
named in axiom 2, but no axiom relates it to anything —
`μ∘(S⊗id)∘Δ = η∘ε` is absent, and what axiom 2 states is counit
multiplicativity, not a Hopf compatibility.

### A citation that points at nothing, and a direction reversed

`emergence-to-quantum-flat` says "quantum flatness operates as a derived
consequence of **the instanton axiom**" — which inverts its own proof
(Step 2 *imposes* `B = F_A`, Step 3 *derives* `F_A⁻ = 0`), and
`grep -rn "instanton axiom" content/` returns **that line alone**
corpus-wide. There is no such axiom.

### A mis-attribution that recurs, so it is a pattern not a slip

Both `frobenius-simplification` and `fiber-adjoint-involution-proof`
credit `H⁰(Ad(A)) = 0` to non-degeneracy of the pairing — "any global
parallel section would pair with itself", which is no contradiction. The
corpus's own proof uses SU(2)-emergence plus **Schur**. Two blocks, same
wrong reason.

### Smaller, verified

`frobenius-su2`'s `Δ_μ(f)(g,h) = ∫_G f(xg)\overline{h(x)}dx` types `h` as a
group element on the left and a function on the right; its closer describes
**commutativity**, not associativity (the two-function statement is false
on non-abelian SU(2)). `fiber-adjoint-su2` gives a traceless **Hermitian**
`σ([ℓ])` and an **anti-Hermitian** orbit representative two lines later.
`heisenberg-commutator` equates a scalar to an operator, and `Θ(ξ) = 1`
identically for a normalised Reeb field. `fermion-boson-decomposition` uses
`\mathcal{H}_q^k` for harmonic forms while `notation-collisions.md`
registers `\mathcal{H}_q` as the shuffle Hopf algebra — and
`dilog-pentagon-is-associator`, in this same chapter, uses it that way.
Bare `J` appears in three blocks against the register's "we never write
bare `J`".

### Clean, recorded so it is not re-run

No convention-C `z` in any spelling — `z` does not appear at all. No braid
words. No raw `q₀` literal (only `:val[q_0]{precision=6}`). No absolute-mass
MeV claim. Categories bold `𝐂`, fibre functor `τ`, no deprecated 5-tuple.
No §3b violation: `g-action-on-substrate` is correctly kinded `conjecture`.

`operates as` for *is* occurs **22×** corpus-wide, so it is house style
rather than this batch's defect — worth knowing before someone "fixes" it.

---

## From agent:e00 (predicted-spectra eq_00) — 2026-08-22

37 prose blocks + 8 data tables, 35 anomalies. This is the chapter that
states predictions, and it shows: the findings are about what the numbers
mean, not about prose.

### The α_EM headline changes sign with the pin

`alpha-em-derivation-open-problems` quotes **+5.7 × 10⁻⁸** as its residual.
Every number in the block is **muon**-pinned. At the proton compute default
(the standing directive since 2026-08-07) the same quantity is
**−2.142 × 10⁻⁸** — opposite sign and 2.7× smaller. The `+2/(3π)` row moves
too: −4.180e-6 muon vs −4.259e-6 proton.

`alpha-em-categorical-trace-ratio-table-data` is also muon-pinned, and here
the table **can** distinguish the pins (they differ in the 8th digit of
`δ₉`), so this is not a rounding-invisible case. `1.1097` is excluded.

### "Both models close the 1.6 % energy gap" is false, and backwards

`breit-wheeler-pair-production-derivation`. The algebra checks out
term-by-term — five NF coefficients, `net_bare = 1 + h = 1.209060299`, both
polarisation limits. What fails is the conclusion:

- The **net → MeV conversion is never stated.** Recovering it from the
  block's own numbers gives `0.83205114 MeV/unit`, uncited.
- Under that constant, reaching `2mₑ` needs `φ = 0.0538675`, `s = 0.108282`.
  The block quotes **0.0487** and **0.0978**, low by a factor 1.106.
- Those values give `net = 1.205278 / 1.205165`, **below** the bare
  1.209060 — so `E = 1.0029 / 1.0028 MeV`, **worse than doing nothing**.
- And `φ`, `s` are fitted to `2mₑ` by construction.

### The Λ-vs-Cl₂ guard, live in content

`bring-hyperbolic-knot-bloch-decomposition` §Obs 2 writes
**"Vol(𝓑₃) = 8G = 8·Cl₂(π/4)"**. The value `8G = 7.327724753` is right; the
name is not. `Cl₂(π/4) = 0.9818721511`, so `8·Cl₂(π/4) = 7.854977208`, and
`G = Cl₂(π/2) = 0.9159655942`. This is precisely the shape AGENTS.md
describes — right number under the wrong name — so a grep for the bad name
would flag it while a grep for a bad value would not. Its own sibling
`bloch-wigner-mathlib-filler-table1-data` has it right (`4Cl₂(π/2) = 4G`).

### The wrong-trefoil braid word, third chapter running

`breit-wheeler-pair-production` gives `e⁻ = σ₀σ₁σ₀ "(trefoil)"`. Computed
from the induced permutation: `σ₁σ₂σ₁` induces `(1 3)`, so the closure has
**2 components** and is not a knot at all; Markov-reducing,
`σ₁σ₂σ₁ ~ σ₁²σ₂` destabilises to `σ₁² ∈ B₂` — the **Hopf link**. The
trefoil as a 3-braid is `(σ₁σ₂)²`. `e⁺` inherits it, and the rest of the
chapter uses the correct `e⁻ = T_{2,3} = σ₁³`.

`bring-hyperbolic-knot-bloch-decomposition`'s Markov-closure table is wrong
in **3 of 5 rows** (`σ₁`,`σ₂` → 2 components, not "unknot"; `σ₁σ₂`,`σ₂σ₁` →
1, not "Hopf link"; `σ₁σ₂σ₁` → 2 = Hopf link, not "trefoil"), and it cites
`σ₁³`, which is not an H₃ basis element. The section's conclusion survives;
the table does not. `categorical-neutron-table-data` repeats the same
mislabels on the same six basis elements.

### The Bloch-group five-term relation is inverted

`bloch-group-quotient-construction`. Tested at 30 dps with
`x = 0.3+0.7i`, `y = −0.4+1.3i`: the standard five-term residual is
**0.0**; the block's orientation (with `e₄`, `e₅` reciprocated) gives
**1.979625777**. `e₃ = e₂/e₁` matches the standard form, so no relabelling
rescues `e₄`/`e₅` — and since `D(1/z) = −D(z)`, the block's version flips
two signs.

### Claims that do not follow

- `borel-zagier-qou-volumes`: "**strictly stronger than irrationality**" is
  false. ℚ-linear independence of `{V₁,V₂,V₃}` does not imply any `Vᵢ ∉ ℚ`
  — `{1, √2, √3}` is a counterexample. The statement needs
  `{1, V₁, V₂, V₃}`. Also `Vol(𝓑₃)/Vol(5₂) = 2.591021365`, printed 2.592.
- `bring-hyperbolic-knot-bloch-decomposition`: the conjecture and both
  reduction claims live in `B(ℚ(ζ₁₅))`, but the Borromean class has trace
  field `ℚ(i)`, and **`i ∉ ℚ(ζ₁₅)`** (that needs `4 | 15`). The block's own
  Obs 2 already concludes `ℚ(ζ₆₀)`. Its field table is otherwise fully
  correct. Also `L6a4` **is** the Borromean rings (6³₂), listed as two
  atlas entries, so "the shared volume identity establishes `𝓑₃ ~ L6a4`"
  is an identity restated as a derivation; and "By the **Birman–Hilden**
  theorem, 3-braid closures yield hyperbolic knots up to 10 crossings" is
  misattributed and false as stated.
- `bohr-radius-categorical`: "a₀ at `q₀ ≈ 1.11` yields `5.29 × 10⁻¹¹` m" is
  the CODATA value. With the block's **own** `α_EM = 7.30870156e-3`,
  `a₀ = 5.2835550e-11` m. A calibration pass-through presented as a result.
  Its `.ts` kind is `conjecture` while the `.md` opens "Proposition."
- `bohr-radius-round8-findings`: "three structural properties" followed by
  **four** sections; and "identifying `n = 2k+1` exactly reproduces the Bohr
  `1/n²`" reproduces only the **odd-n subseries** — `1/4` and `1/16` have
  no `k`.
- `alpha-em-categorical-trace-ratio-table-data`: the `.ts` caption calls row
  5 "the CODATA α_EM definition", but `7.30870098e-3` is **not** CODATA
  (`7.2973525693e-3`) — `1/α = 136.8232089`, **0.1555 % high**. Rows 4 and 5
  are the same expression at the same `q₀`, so "exact within 10⁻¹²"
  certifies an identity, not an experiment.

### Convention C, with its dependence measured

`bohr-radius-round8-findings` uses `z = √q/(q+1) = 0.4993203342`. The
displayed `V_H`, `V[1]`, `V[2]` carry `z` **symbolically**, so the
cross-term-cancellation headline is convention-independent; any numerical
evaluation and the "optimal ordering" claim are not. Recording the split
because "flag every C value" without this distinction over-reports.

### Sweep damage: a new shape

Flattened imperative or bulleted lists rewritten as declaratives, producing
sentences with no subject-verb sense — *"The photon holonomy integral
defines over the fibre."*, *"The partition functions evaluate and limits
take k → ∞."*, *"A depth-k contribution defines 1/α_EM."* (four in one
block), plus *"The trace ratio identity determines the substrate-flow value
from the α_EM categorical-trace ratio"* (subject and object are the same
object). Six blocks. Distinct from the token-substitution and synonym-swap
classes already recorded.

Two §7a generator violations in the β-decay cluster (`T² = (q−q⁻¹)T + 1`,
and the skein written `q[L₊] − q⁻¹[L₋] = (q^{1/2}−q^{−1/2})[L₀]`), plus
`β⁻` emitting an **unbarred** `K_{0₁}` — breaking lepton number and
contradicting its own sibling's `L₀⁻ = T_{2,3} ⊔ T_{1,0}^σ`.

### Verified clean, recorded so it is not re-run

All 9 rows of the Breit–Wheeler product table; the `S₃` sign projector;
`V₃² = Δ`; bar-transfer clauses 1 and 3; the `φ²` band and `q₀ ∈ (1, φ²)`;
`dim Λ²ℂ¹⁰ = 45 = 9 + 36`; `α_shift(T_{2,9}) = 9`, `α_shift(T_{3,5}) = 10`;
every cyclotomic degree and `r₂` in the field table; and all four margins in
`bar-self-dual-confinement-band-proof`, which are pin-independent at the
displayed precision.

---

## From agent:e01 (predicted-spectra eq_01) — 2026-08-22

23 prose blocks and 22 data tables. **The tables carried the findings** —
which is the argument for reading them even though they take no trap
verdicts.

### A failing witness cited as confirming evidence

`e-hartree-categorical-derivation` states: *"The H₂ witness gives the
dimensionless ratio `E_bind/E_Hartree ≈ 0.170` … It matches the
standard-physics H₂ ratio ≈ 1/6."*

From `h2-molecular-binding.witness.json`:
`0.8645364577143441 / 27.211467573147633 = 0.03177103386`. **0.170 appears
at no key in the witness.** It is the *experimental* ratio (D₀ → 0.164563,
D_e → 0.174434). And the witness itself records

    {"name":"H2 binding energy within 5% of observed",
     "computed":0.8645, "expected":4.478, "passed":false}
    "allPassed": false

Root cause: tables 2, 3 and 11 are pinned to a **superseded run**. Table 2's
`Φ₁ binding 0.687` / `E_bind 4.64 eV` against the current `0.12847272688` /
`0.86453646` are ratios **5.3474** and **5.3670**; and `4.64/27.30 =
0.169963` is the quoted 0.170 exactly. Table 11's unstated "target" *is*
0.16996, verified across all six rows. Against the current witness those six
candidates score 5.246–6.029, so the mechanism Table 11 calls "a direct
symbolic computation" now supports nothing.

### The quantity to be derived is supplied experimentally in its own evidence

Same block, two different `α_EM` in one place. Table 2 uses the framework
value — recomputed `1/α = q[9]_q[10]_q = 136.823208854`, giving
`m_e c²α² = 27.29609 eV`, **0.3113 % above** the CODATA Hartree. The
witness cited as evidence uses `alpha_EM = 0.007297355976840865`
(`1/α = 137.035935`, i.e. CODATA) → `E_hartree_eV = 27.211467573`.

### Two tautologies presented as Mathlib gap closures

`cl2-pentagon-and-faddeev-partial`.
`Cl₂(0) − Cl₂(0) + Cl₂(0) − Cl₂(0) + Cl₂(0)` has three plus and two minus
terms, so it collapses to a single `Cl₂(0)`; and `Φₙ(0;q) = 1` makes
`(1−q)log Φₙ(0;q) − Li₂(0) = 0 − 0` for every `(q, n)`. The joint Lean
statement is literally `Cl_2(0) = 0 ∧ Li_2(0) = 0`, while the `.ts`
authorNote calls it *"closes a non-trivial portion of substantive Mathlib
gaps (2) and (3)"*. Table 1's own gloss concedes *"pentagon holds by
definition"*. Strict Lean Discipline item 5 / "Axiomatization is NOT a
Proof".

### The Λ-vs-Cl₂ guard, independently confirmed — and the Lean is the right side

`clausen-function-mathlib-filler` writes `Vol(𝓑₃) = 8Cl₂(π/4) = 8G`, where
`8·Cl₂(π/4) = 7.85497720840163` and `8G = 8·Cl₂(π/2) = 7.32772475341775` —
the middle term is **7.195 %** larger than both outer terms. The correct
form is `16Λ(π/4) = 8Cl₂(π/2)`.

**The `.lean` is correct** (`ClausenFunctionMathlibFiller.lean:139`,
`8 * Cl_2 (Real.pi / 2)`), and its docstring carries the smoking gun:
`` `G = Cl_2(π/2)` (NOT `Cl_2(π/2)`) `` — the NOT-clause repeats the thing
it negates, so it was written against `Cl_2(π/4)` and later half-corrected.
Table 1 in the same block self-contradicts. A **third** site is outside this
batch: `mass-theory/binding-scale-catalan-proof.md:4` (`G = Cl₂(π/4)`).

### Tables whose rows contradict themselves

- **`diophantine-valley-table-data`: 4 of 7 rows have a printed `n/p` that
  is not the `n/p` of the same row.** Br 35/44 printed 1.10, actual
  **1.2571**; Zr 40/50 printed 1.20, actual **1.2500**; Sn 50/70 printed
  1.30, actual **1.4000**; W 74/110 printed 1.40, actual **1.4865**. The
  `(p,n)` pairs are real nuclides; the first column is an unchecked
  1.10/1.20/1.30/1.40 decade ladder, and a "threshold-crossing" reading
  does not rescue it.
- **`chebyshev-torus-coefficients`: four mutually inconsistent laws for one
  `cₙ`.** The boxed `U_{n−1}(x/2)`, the block's stated recurrence, the
  correct Hecke transfer, and the referenced table each give different
  sequences — the boxed form needs `−c_{n−1}` and the transfer needs
  `+c_{n−1}`, so they diverge in **sign** from n=3. No single recurrence
  generates the whole table.

### `diophantine-valley` and `elliptic-stability-locus`: right answers, wrong routes

- Three mutually inconsistent normalisations of the Coulomb term appear in
  `diophantine-valley` (coefficients `4c`, `2c`, `c`); **(ii) and (iii)
  equated force `c = 0`**. Only the third matches the textbook SEMF
  `Z* = A/(2 + (a_C/2a_A)A^{2/3})`.
- **Mordell is misapplied**: Mordell–Weil gives *finitely generated*, not
  finite, and a positive-rank curve has infinitely many rational points.
  Finiteness of **integral** points is Siegel's theorem — and the block's
  own points are integral, so Siegel is what it wants.
- `elliptic-stability-locus`'s erbium result is reached by a route other
  than the equation it is presented as following from: the block's own
  `p² = (1−c)/(4c³)` gives **p = 270.93**, and its own match condition gives
  **237.5**, against the stated 67.8. The 67.8 ↔ erbium pairing *is*
  reproducible — via the **textbook** `Z = A/(2+cA^{2/3})` at A = 167,
  giving Z = 68.05.
- Its discriminant is printed 16× small (`−18.95` for `−303.145`), and that
  this is a slip rather than a convention is provable from the same line:
  the printed `j = 129.9` matches `c₄³/Δ` with the **standard** Δ, where
  `−18.95` would give `j = 2077`.

### `em-coupling-bring-zero-mode`: the residual is smaller than the pin shift

The table is arithmetically exact at the **old muon** pin. But
`tree(muon) − tree(proton)` is `1.0801e-5`, **relative 7.894e-8 — larger
than the claimed `+5.7e-8` residual**. Under the proton compute default the
two-term residual becomes **−2.14e-8**, flipping sign. And `+5.7e-8` is
**372σ**, not "approaching `σ_α = 1.5e-10`". Its cited witness
`alpha-em-correction-derivation-attempts.witness.json` **does not exist** —
checked against all 1421 witnesses in `computations/`.

### Recorded clean, including one I expected to fail

`α²/h⁴ = 1/(q²(q⁹−q⁻⁹)²(q¹⁰−q⁻¹⁰)²)` is algebraically exact. Table 10
verified row by row via `[n]_{−q^{±1}} = (−1)^{n+1}[n]_q`. Table 12's
characters reproduce with `χ_{(3,1)}+χ_{(2,1,1)} = −h` exactly. Table 13's
"≈[5]_q amplification" holds (5.280 vs 5.2204, 1.1 %). And the
**convention-D** parenthetical in Mechanism B is *correct* — D is exactly
what makes `det G = 0` and forces the `H_n/rad ≅ TL_n` reading. No
convention-C residue anywhere in this batch.

---

## From agent:e02 (predicted-spectra eq_02) — 2026-08-22

45 blocks, **92 anomalies logged** (full list in the agent's scratch; the
load-bearing ones follow). The trap register here is different from every
other chapter: only 3 fails across the diagnostic five, but 16 on
nonspeakable syntax — nominalisation density consistent with a
de-passivisation sweep, two of whose casualties were left ungrammatical
("The categorical structure defines over the commutative ring").

### Claims that are false, with the route

1. **`hadron-half-life-proof`: "in the classical limit `q→1`, `𝒲(1) = 0`"
   is false.** Computing `tr_M((σ₀σ₁)⁵)` in `H₃(q)` symbolically gives a
   polynomial whose value at `h = 0` is exactly **`z² = 1/4`** (`z(1) = 1/2`
   under both C and D). Independently: at `q = 1`, `H₃(1) = ℂ[S₃]` and
   `(s₀s₁)⁵ = (s₀s₁)² = s₁s₀`, whose trace is `z²`. Beta decay *does*
   vanish at `q = 1` — but by the sibling block's route (`Q = 0`), not this
   one.
2. **`groebner-nf-computation-table2`: 4 of 5 rows wrong.** `Σ_ℓ h(ℓ) = A!`
   at `r = 1`. The table gives 2, 4, 12, 36, 180 against the correct
   **2, 6, 24, 120, 720**. The stated `[3]_r!` is really `[2]_r²`
   (`S₃` has `h = 1,2,2,1`), and `[4]_r!` should have degree 6 — the
   longest element of `S₄` — where the table's has degree 4. **The entries
   are palindromic**, so the block's own Poincaré-duality remark does not
   catch this; only the `r = 1` count does.
3. **`hadron-q-self-correction-proof`: the closing bound is false as
   stated.** "`|δq/q₀| < 0.1 %` for all nuclei" holds along the valley
   (Fe-56 0.031 %, Pb-208 0.093 %, U-238 0.0999 %) and fails for real
   neutron-rich nuclides: **⁴⁰Mg 0.172 %**, ⁶⁰Ca 0.145 %, ²⁴O 0.141 %.
   The formula's supremum is 0.44 %. Its interpretation sibling
   compounds it: `A = 3` is not the maximum — `(A−1)/A²` peaks at `A = 2` —
   and the quoted "0.1–0.4 %" overstates the true 0.221 % maximum by 1.8×.
4. **`francium-extremal-metal` is refuted by its own table.** "The lowest
   ionization energy (4.07 eV)" and "decreases monotonically with `n`",
   against a table showing **Cs 3.89 < Fr 4.07**. All six values are
   correct against NIST; the block concedes the reversal two sentences
   later without withdrawing the claim.
5. **`force-knot-identification`'s skein is wrong and violates §7a.**
   Printed `q[L₊] − q⁻¹[L₋] = (q^{1/2}−q^{−1/2})[L₀]` against §7a's
   `L₊ − L₋ = (q−q⁻¹)L₀`. It is not a correct Jones skein under either
   substitution: with `q = t` the LHS exponents are swapped, with
   `q = t⁻¹` the RHS sign flips. **Load-bearing** — parity violation is
   derived from it two sentences later. The same block says "the three
   `S₃` subgroups of `S₅`"; there are **30** (10 supports × 3 each), so
   the definite description does not denote.
6. **`hadron-half-life-fermi`'s "2.1 ppm deviation from CODATA" matches
   nothing.** The bare `q⁻¹/([9]_q[10]_q)` — the formula named in that very
   sentence — is off by **1553 ppm**; CS-corrected is 0.399 ppm, the
   fixed-point cubic 0.0007 ppm, PSLQ 0.003–0.006 ppm. The nearest corpus
   quantity is the additive zero-mode residual −4.2 ppm, of which 2.1 is
   exactly half. The sentence also attributes the *bare* formula to "the
   Chern–Simons correction".

### The α_EM cluster is not on a common pin, and one witness misdescribes itself

The four routes disagree about which pin they are on: the CS route
reproduces **muon** exactly (137.035944554, 398.6 ppb, κ 1.88804) while the
fixed-point cubic strongly prefers **proton** (0.69 ppb vs 79.5 ppb muon),
PSLQ's "7 ppb" is muon (2.6 ppb proton), and the additive `+5.7×10⁻⁸` is
muon-only — **proton gives `−2.2×10⁻⁸`, opposite sign**. This is the third
independent arrival at that sign flip (e00, e01, e02).

`em-coupling-projection-probe.witness.json` **contradicts itself about its
own pin**: it records `q0Anchor: "proton"` with the proton value, while
`q0_source` and its assertion text both say "muon-anchored", and the
producer says "muon-anchored" in four places. The number is right and the
label is wrong — an inverted layer-straddle, the mirror of the hazard
AGENTS.md documents.

Its `CODATA_ALPHA_INV = "137.035999206"` is commented "CODATA 2018/2022"
and is **neither** (2018: …084, 2022: …177) — it is the LKB/Morel-2020
measurement. Three different unprovenanced α targets appear across this one
block family, and Table 1's headline "399 ppb" does not follow from its own
printed digits (those give 402.0 ppb; 399 is full-precision muon against a
target the table never names).

### Convention C, flagged with an honest limit

`hadron-half-life-proof` uses `1/(q^{1/2}+q^{−1/2}) = 0.4993203 = z_C`
exactly — a detector-blind spelling. The agent explicitly could **not**
determine from the block whether the argument depends on it (it may be an
independent symmetrising normalisation) and flagged it for producer
adjudication rather than asserting dependence. Recording that limit, since
the alternative is a confident guess.

### Verified correct, recorded as negatives

The two-photon normal form matches sympy term for term; all six Markov
traces in `frobenius-gram-matrix-table1-data` including `hz²+z`; the
golden-quartet Galois group entire, including `disc = 400 = 2⁴·5²` and the
Möbius fixed points of `(4−q)/(4q+3)` being exactly `{1/φ, −φ}`; the
Plancherel sums 0.98744 / 1.05056 against the quoted 0.987 / 1.051, tending
to 1 as `q→1`; `Δq_eff = (A−1)/A²·ℏ_q²` derived exactly; crossing numbers 9
and 10 via Murasugi; `Vol(S²)/(3Vol(S³)) = 2/(3π)` exactly.

And `groebner-nf-computation` carries the batch's **only correctly-scoped
durable negative**: "no per-generator transfer matrix can compute
`F_Pauli`" is a scope-(b) exclusion with its licensing invariant named and
verified — the shape the anti-overclaim rule asks for.


## From agent:f02 (mass-theory fq_02) — 2026-08-22

45 blocks, 450 verdicts, 5 inline fixes. Every number below was recomputed
rather than read off; the route is given where it is not obvious.

### A number matching no pin, and a claim off by 1600×

**F02-1. `topological-mass-trefoil` prints 207.1 for `Vol(4₁)/ℏ_q²`.**
Recomputed (`mpmath`, `Vol = 2·clsin(2, π/3) = 2.02988321`, `ℏ_q = 1 − 1/q`):

| pin | q₀ | Vol/ℏ_q² |
|---|---|---|
| proton | 1.1099785827513808 | **206.7683** |
| muon | 1.10997859555733471 | 206.768283 |
| old muon | 1.109978595554181 | 206.768283 |
| the 1.1097 error | 1.1097 | 207.7155 |

The printed 207.1 back-solves to **q = 1.1098808** — a *fourth* value
matching none of the three documented pins and not the known rounding error
either. Against CODATA `m_μ/m_e = 206.7682830` the formula achieves
2.1e-5 %; the printed number misses by **0.160 %**, i.e. the block
understates its own result by four orders of magnitude.

**F02-2. `three-halves-structural-factor` says the same identity closes
`m_μ/m_e` "to 0.034 %".** At the proton pin the true figure is
**+2.10e-5 % = 209.8 ppb** — which is precisely the documented μ–p substrate
tension — and identically **zero** at the muon pin, where the relation *is*
the pin. 0.034 % is ~1600× too large and corresponds to no pin.

**F02-3. Same block: the τ sentence omits ξ₃ and is impossible as written.**
`m_τ/m_e = 3477.23` would need `Vol/ℏ² = 34.137` without ξ₃, far outside any
10-crossing hyperbolic volume. The cited witness carries
`Vol(10₄₃) = 13.83304617` and `predicted_xi_3 = 2.4873628890`, and
`ξ₃·Vol/ℏ² = 3504.8` reproduces the witness's own
`rel_err_percent = 0.79443` exactly. So the muon sentence needs ξ₂
**excluded** and the τ sentence needs ξ₃ **included** — the two were written
from one template and the template is wrong in opposite directions.

### Convention C, including the spelling a source grep cannot see

**F02-4. `terms-2-6-higher-operations-table2-data` is convention-C
throughout.** Recursion `σ^k = A_k σ + B_k`, `tr = A_k z + B_k`:

| k | printed | z_C = 0.4993203 | z_D = 0.6126880 |
|---|---|---|---|
| 1 | 0.49932 | 0.49932 ✓ | 0.612688 |
| 2 | 1.10439 | 1.10439 ✓ | 1.12809 |
| 3 | 0.730204 | 0.730204 ✓ | 0.848527 |
| 4 | 1.25704 | 1.25704 ✓ | 1.30548 |
| 5 | 0.993002 | 0.993002 ✓ | 1.12145 |

All five match C; all five differ from D **in the first printed digit**. The
`1/(q;q)_k` column is independently correct, and the table cannot
distinguish proton from muon pin at its printed precision.

**F02-5. `toroidal-harmonics-delta-lambda` depends on convention C through
an identity, not a constant.** Its bridge turns on
`w = z² = 1/(2(cosh η + 1))`, which holds for `z_C` to 1e-31 and **fails for
`z_D`** (0.3753866 vs 0.2493208, a 51 % gap). This is the class the
detector-blindness taxonomy calls invisible: there is no `z = …` to grep,
only an identity that happens to be true in one convention. The block's ODE
reduction was re-derived by hand and is **exactly correct**, and
`P_{-1/2}/P_{1/2}(√5/2) = 0.9446492234` reproduces its printed 0.944649 to
six digits — the defect is scope, not arithmetic.

### The excised absolute-mass double-counting, still shipping

**F02-6. `tower-binding-energy-table-data` reproduces its own "Mass error"
column exactly** — all 7 values check as `(B_obs − B_pred)/M_atom`. That is
the finding. The underlying **binding** errors are **+121.6 % (²D),
−31.4 % (⁴He), +7.6 %, −10.1 %, −8.2 %, −7.2 %**; they land under 0.25 %
only because the denominator is a mass dominated by `Z·m_p + N·m_n`, i.e. by
the calibration. This is exactly the double-counting the 2026-08-11
absolute-mass excision removes. No pin, no witness, no producer.

**F02-7. `term6-binding-density` — prose vs its own table, factor 6.** The
prose says T₆ enumerates **ordered** triples (~A³); the table gives the
**unordered** `C(Z,3) + C(Z,2)N + Z·C(N,2) + C(N,3) = C(A,3) = A³/6`
(Vandermonde, verified at five (Z,N) pairs). The fitted α absorbs the
factor. The block also concedes α, β are "AME calibration constants", which
`rem:three-calibration-inputs-context` explicitly forbids.

### Citations that resolve to nothing, and a witness that misdescribes itself

**F02-8. A dead witness with a space in its filename.**
`spin-involution-lp-dual-invariance-proof` cites
`computations/canonical evaluation-phiq-pair-knot-markov-trace.witness.json`.
No such file; no `*pair-knot*` anywhere in `computations/`; the quoted
`0.06216177120816107` appears nowhere in the tree. The space is itself the
`canonical` ← script-name sweep substitution, so the citation was *created*
by the sweep. Its sibling citation is real:
`alpha-5-lp-dual-crystal.witness.json` has `allPassed: true` and genuinely
carries `y0_star = 570.6762423449366` and `26.82418994350443` — but
`q0Anchor: "muon"`, which the prose does not disclose.

**F02-9. `tau-amphichiral-sdp-probe.witness.json` straddles the two layers.**
Header says `q0Anchor: proton` (`1.10997858275138…`), while its assertion
`muon_canonical_pin_consistency` computes **206.768283** — the *muon*-pin
value of `Vol(4₁)/ℏ_q²` (proton-pin gives 206.768326). A comparison producer
classified on one layer; the exact hazard AGENTS.md §q₀ describes.

### Statements refuted by their own blocks

**F02-10. `thurston-volume-additivity`.** "One tetrahedron per crossing"
would give 4₁ four tetrahedra; the block's own Extremality section says 4₁
"comprises exactly two". Both the per-crossing sum and the torus-knot
argument rest on the false claim. (`v₃ = 1.0149416`, `2v₃ = 2.0298832` are
correct — not the `8·Cl₂(π/4)` error.)

**F02-11. `staircase-ew-residual`.** The conjecture says the matrix image
"has two nonzero eigenvalues"; the k=4 evidence in the same block says "the
top eigenvalue is degenerate" and cites `e[254]/e[188]` from a 768-dim
spectrum (`f^{(4,3,2,1)} = 768` verified). It also quantifies over all k ≥ 2
while recording k=2 as untestable.

**F02-12. `three-parameters-wedderburn-context`.** Its table maps std → m_e →
mass scale and alt → Q_β → interaction scale. Its H₂ cross-check then says
"Two irreps → q₀ and m_e" and "No standard representation → no interaction
scale needed". H₂'s irreps are sym and **alt**, so by the block's own table
H₂ *has* the interaction scale and *lacks* m_e — the opposite, reached by
silently relabelling std as the interaction scale.

**F02-13. sym/alt swapped across three blocks.**
`rem:three-calibration-inputs-context` maps alt(1³) → CAL-2 → q₀ and
sym(3) → CAL-3; `prop:three-parameters-wedderburn` and
`rem:three-parameters-wedderburn-context` both map sym(3) → q₀ and
alt(1³) → interaction/Q_β. Two against one; the calibration-inputs-context
table is the outlier.

**F02-14. `staircase-corner-hook-proof` — the k=3 pair does not reconcile.**
`q^{1/5} = 2.1087 %` at every real pin (2.1036 % at 1.1097). Applied to the
stated 2.19 % gap it leaves **0.081 %**, not the claimed 0.13 %; landing on
0.13 % would need a 2.057 % factor. The hook identity itself (arm = leg =
k−1, h = 2k−1) is correct.

### Typing, ring and convention errors

**F02-15.** `topological-mass-formula-algebraic-proof` asserts
`Habiro-hat(ℤ[q]) ⊂ ℚ(q)`. Backwards — the Habiro ring is strictly larger
and not contained in ℚ(q).

**F02-16.** `topological-mass-formula-algebraic` states
`Φ₁ = ln|Vol_{q₀}(β)|`, so `m = ln|Vol|/ℏ²`; its own proof and
`prop:topological-mass-formula` both give `Vol(K)/ℏ²`, **no logarithm**. The
statement also claims to bypass "hyperbolic volume conjectures" while its
proof's final step invokes the volume conjecture.

**F02-17.** `topological-mass-formula` — §3b-cond violation. Step 2 rests on
Kashaev–Murakami, carried as "Hypothesis 2" on the Lean structure, but the
`.md` opens with a bare `**Proposition.**` and `uses[]` names no `conj:`.
Clauses 3 and 4 both fail. Same block, one paragraph apart: prose calls Vol
"the imaginary part of the Chern–Simons functional" while the display two
lines later writes `Re tr(…) = Vol(K)`;
`substrate-cohomology-calibration-story` takes Vol as the **real** part
(Neumann–Zagier `Vol + i·CS`). It also cites "Möbius energy" for the CS
correspondence — an unrelated functional.

**F02-18.** `three-calibration-inputs` — ring contradiction: "a ℚ(q₀)-element
`Ô(q₀) ∈ ℤ[q₀^{±1/2}]`". Different rings, and the block's own example breaks
the narrower one (`E₀ = m_e/(q₀(q₀−1))` needs `(q₀−1)⁻¹`).

**F02-19.** `substrate-cohomology-calibration-story` — sign error. Crossing
eigenvalues are `q` and `−q⁻¹`; with `λ = log q` these are `cosh λ + sinh λ`
and `−(cosh λ − sinh λ) = sinh λ − cosh λ`. The block writes "these split as
`cosh λ ± sinh λ`", dropping the minus. It also labels q₀ itself "CAL-2"
(CAL-2 is 𝔇_β; q₀ is what it fixes) and reuses `τ` for a monodromy trace and
`λ` for `log q` — both AGENTS.md-named collisions.

**F02-20.** `tmli-constituent-composite-agreement{,-proof}` — type error plus
sibling contradiction: "`∏ V̂_i` and `tr_M(ρ(β))` evaluate the same element
of `H_N(q)`", but both are scalars, not algebra elements. And
`prf:spin-involution-lp-dual-invariance` states the product convention "does
NOT respect the Hecke-algebra structure", attributing a 1.326× discrepancy
to exactly that gap.

**F02-21.** `tau-all-orders-bridge` — not a dichotomy. "Exactly one of the
following holds", but option 2 adds "coincidentally share only their h²
coefficient" beyond the negation of option 1, so the pair is not exhaustive.
`α₆ = α₈ = 0` and "computations up to h⁸" carry no witness.

**F02-22.** `torus-knot-zero-volume-via-reeb` — closure of `σ₁σ₂` in B₃ is
`T_{3,1}` = the **unknot**, not the trefoil (`(σ₁σ₂)² = T_{3,2}` or `σ₁³`).
The conclusion survives: the unknot has zero volume too.

**F02-23.** `topological-field-ansatz-table-data` — every knot
identification verified (T_{2,3}/T_{2,5}/T_{2,7}, 4₁ amphichiral, Borromean
= 6³₂, deg = m), but the framework use contradicts two siblings: it assigns
4₁ to the **Higgs** while `three-halves-structural-factor` writes
`K_μ = 4₁`, and it assigns **torus** knots to μ and τ, which two blocks in
this same batch prove have zero hyperbolic volume.

**F02-24. Scope discipline.** `terms-2-6-higher-operations` writes an
unscoped "dead-end". The (b)-justifying invariant genuinely exists here
(`HH¹ = HH² = 0`, semisimple, per the block's own table), so the fix is to
*state* it as scope-(b) — not to delete the finding. Its third table row
("Φ_q ≠ finite-dim character") cites no invariant and is scope-(a) at best.

### Sweep damage, three shapes

- **`canonical` ← `numerical(ly)`**: `three-calibration-inputs-proof`
  ("pinned **canonical** by the dimensionless ratio"),
  `three-calibration-inputs` ("pinned **canonical** through its proxy"). Not
  fixed inline — `canonical` is a loaded word in this corpus and the repair
  should be deliberate.
- **Script-name substitution**:
  `spin-involution-lp-dual-invariance-proof` ×3, including "**The** / the
  canonical formalism / (per prop:operator-selection-lp) confirms";
  `staircase-corner-hook-proof` ×2, leaving both quoted percentages
  provenance-free.
- **Sentence-initial lowercase**: `spectral-sequence-collapse-proof`,
  "categorical derivation steps need only enumerate…".

**F02-25. A dangling boilerplate paragraph, twice.** `tau-all-orders-bridge`
and `thurston-volume-additivity` both **end** with the identical stub
"**Archimedean specialisation.** What follows sits on the archimedean
side…" — and nothing follows in either.

**F02-26. `three-calibration-inputs-proof` — stale precision figure.**
`m_p/m_e (6 × 10⁻¹¹)` is the superseded 0.06 ppb; the live value is
0.017 ppb = 1.7e-11.

**F02-27. `three-calibration-inputs-context` — CAL mislabel.**
`E₀^(cal) = Q_β(n)/|Δ(net)| ≈ 4.155` is tagged "(CAL-3 cross-check)" while
the same block states four times that Q_β is the **CAL-2** proxy. Its
numerics all check: `E₀^(N=0) = 4.185981`, `E₀^full = 4.227483`,
`Q_β = 0.783646` (+0.168 % vs CODATA 0.78233, matching its own "0.17 %"),
`4.155/0.78233 = 5.311`, SM count 6+3+4+3+1+1+1 = 19.

### Verified correct — recorded so a later pass does not re-flag them

- **`symbolic-character-table`.** `c_λ = f^λ/2` for self-conjugate λ was
  derived from `χ^λ(odd) = 0` and reproduces **all four rows**
  (2/6/16/20 → 1/3/8/10); the three pair characters check against the S₅
  table at q→1; Plancherel 35.6 % ≈ the stated "36 %".
- **`torus-knot-delta-q-writhe`.** Every writhe correct, and the block
  **understates** its own invariant: `w − m` is identically
  presentation-independent, not merely its parity.
- **`t-beta-markov-frobenius-collapse{,-general}-proof`.** All five steps
  correct, with an honest note that cyclicity goes unused.
- **`terminal-resolution`.** Table internally exact, and the absolute-mass
  excision correctly implemented.
- **`toroidal-harmonics-delta-lambda`'s golden-ratio section** — the
  batch's best example of anti-fit discipline, notwithstanding F02-5.


## From agent:f00 (mass-theory fq_00) — 2026-08-22

45 blocks, 450 verdicts, 2 inline fixes. Only 3 trap fails — this chapter's
prose is in good shape, and the batch's value is entirely in what the
full-context read caught alongside it.

### The wrong knot, confirmed twice by independent routes

**F00-1. `figure-eight-branching-rule` defines 4₁ as a word that closes to
the UNKNOT.** The block gives `4₁ = σ₀σ₁⁻¹σ₀⁻¹σ₁`. Reduced Burau over exact
`ℤ[t,t⁻¹]`, `det(I−B)·(1−t)/(1−t³)`:

| word | Δ(t) | is |
|---|---|---|
| `σ₀σ₁⁻¹σ₀⁻¹σ₁` (the block's) | `1/t ≐ 1` | **unknot** |
| `(σ₀σ₁⁻¹)²` (genuine 4₁) | `−1 + 3/t − 1/t² ≐ t − 3 + t⁻¹` | figure-eight ✓ |
| `σ₀³` in B₂ (control) | `t² − t + 1` | trefoil ✓ |

So **every `b_λ·h²` term in that block is computed on the wrong knot.** In
`[2,1]` the true character is `q⁴ − 2q² + 1 − 2q⁻² + q⁻⁴`, not `−1 − h²`;
the two agree only at q = 1.

This corroborates the same finding reached independently by **agent:r07** on
a different chunk, and I re-verified it a third time in the coordinating
session with a separate sympy implementation. Three routes, one answer.

### A coefficient carried at two values, where only one reproduces the headline

**F00-2. `c₅` disagrees across five blocks.** The proposition and tables 1–2
use `c₅ = −(b² + ½) = −1.2527`; the context block (×2) and table 3 use
`c₅ = 3c₃² + b = +12.868`. At `u⁵ = 4.4822e−11`:

| c₅ | contribution | N=4 → N=5 |
|---|---|---|
| −1.2527 | −0.0561 ppb | −0.57 → −0.63 ppb |
| +12.868 | +0.5768 ppb | −0.57 → **+0.0068 ppb** |

Only the second lands on the published "~0 / +0.04 ppb". **The context block
is right; the proposition carries the superseded coefficient.**

**F00-3. The ladder headline matches no row of its own table.** The
proposition claims −0.0066 ppm; its table 2 gives +6.02 ppb (N=3) and
−0.57 ppb (N=4) — wrong sign and ~10 % off.

**F00-4. `h` is undefined in the ladder proposition.** `α = (z−1)h/2`
requires `h = q − q⁻¹` (which reproduces N=1 = +73.64 ppm against the
printed 73.79); reading `h = ℏ_q` gives +1254 ppm, off by 17×.

**F00-5. `S(q₀) ≈ 0.18689` is not S(q₀).** The block's own formula gives
**0.18720719**. 0.18689 is `Q_β^CODATA/E₀(q₀)` — and the two differ by
exactly the 0.168 % that the same block quotes elsewhere
(`Q_A/Q_CODATA − 1 = 0.167738 %`).

### A retraction, recorded because it is worth as much as the finding

**F00-6. RETRACTED by the auditing agent mid-batch.** It first flagged the
direction gate's "2.1e−7 (210 ppb)" as 18× overstated. On recheck that is
**exact**: "the substrate variable" means the *ladder* variable u, not q, and
`u(proton) = 0.008517234550156142` vs `u(muon) = 0.008517236340043958` is
210.15 ppb. The 18× is the amplification `d ln u/d ln q = 2/(qℏ_q) = 18.19`,
i.e. the agent had found the amplification factor and mistaken it for an
error. Only the block's wording is ambiguous; the number is right.

### The c_k conflation AGENTS.md names, found again

**F00-7.** "Cross-anchor swing ≈ 3.5 % at c₃" is `|−2 − c₃|/2 = 3.46713 %` —
the **gap to the integer candidate**, not the swing. The true swing is
**2.37478 %**. This is precisely the normalisation-mistaken-for-discrepancy
class the AGENTS.md c_k correction was written about.

**F00-8. Stale c₃.** The context block's "−2.010 at the muon pin" is the
pre-#1422 value (current −2.02020024), and it implies a 2.85 % swing.

### Convention C, load-bearing and — unusually — decidable

**F00-9. `frobenius-s-classification-table2` gives
`z = (q^{1/2}+q^{−1/2})⁻¹ = 0.49932033`** — convention C in the spelling the
detector-blindness taxonomy lists. Here it is load-bearing rather than
cosmetic: z enters `Φ₁ = Σ log|z aᵢ + bᵢ|`, and `bar(z_C)/z_C = 1` while
`bar(z_D)/z_D = q⁻⁴`, so the "+1" S-eigenvalue — and the parent block's
"exactly one S-odd term" — is a statement about C, not about the canonical
convention. In the direction gate, switching to D moves the refuted family
from `m ≥ 4` to `m ≥ 5` (`0.998/z_D⁴ = 7.08` passes; `/z_D⁵ = 11.56` fails).

### Proof steps that do not hold

**F00-10. Step 3(c) of the stratified proof is false.** "λ has a box with
hook k ⟺ depth ≥ k" fails at **λ = (2,1)**: hooks are {3,1}, maximum 3, and
there is no hook of length 2. 22 counterexamples up to n = 7.

**F00-11. Step 3(d) is malformed.** `F_n(z) = Σ_λ dim_q⁻¹ z^{|λ|}` is a
monomial, since `|λ| = n` always — coefficient 2.4972905 at n=3, which is the
sibling table's own number — so it cannot equal
`∏(1 − q⁻ᵏz)^{−c_k(n)}·u_n(q)` (at n=3, `c₃(3) = 3`).

**F00-12. Step 4 does not follow from Step 1.** Step 1 gives
`⟨Z^(k), Z^(ℓ)⟩ = 0` for `k + ℓ ≠ N`; Step 4 needs orthogonality for
`k ≠ ℓ`. Under Step 1 the vanishing is `k > N − k_*`, which matches only if
`k_* = N/2`.

**F00-13. `ramified-disc-fusion` clause 3 contradicts its own prose.** The
DFT gives `w_k → ζ^{−k}w_k`, which the prose states correctly; clause 3's
uniform `ζ w_k` is wrong. Separately, C₃ monodromy is already regular — S₃
arises only after adjoining orientation reversals, again as the prose says.

### Provenance

**F00-14. A deprecated witness at the old muon pin.**
`mn-classical-parity-blind` sources `_deprecated/schur-weyl-mn.witness.json`
(`q₀ = 1.1099785955541805`, the **old muon** value), whose own notes say it
"requires ribbon q-weights (next iteration)". Its column "Nonzero χ^λ
partitions" is **false**: 2/6/18/40 partitions have χ ≠ 0, not 1/2/3/5.

**F00-15. Pin-attribution mismatch.** The radius gate says "extraction at
q₀ = 1.10997858…" (proton) while its witness records
`1.1099785955573347…` (**muon**).

**F00-16. Sweep damage.** `partition-sum-…-table5` carries "Deuteron gap
(**the formal derivation**)" in the slot where the sibling row carries a
backticked script name; also "canonical evaluation", "canonical precision
ladder", "via the canonical formalism", "From the canonical formalism",
"canonical anchor (verified)".

**F00-17. Unprovenanced symbols.** `N_sym ≈ 1.90` (hoefsmit table 2) has no
definition, witness or derivation — and its own context block calls the
Plancherel framing "incorrect". `P_n(q,z)` in `qz-bicompletion` is undefined;
`J` in `reeb-exceptional-divisor` is undefined.

**F00-18. Rounding.** `30/8 = 3.75` printed as 3.7 (two rows) beside an exact
7.0; a ratio `1.00039344` printed 1.00036, recomputed from an
already-truncated 2.5009; `955.49/1.019741349 = 936.9925` against a printed
936.994; and "within 0.1 %" is **0.10838 %**, while the parent block's
"within 0.1 %" is **0.1477 %** — refuted by its own table's `−0.14 %`.

### Verified correct — recomputed from scratch, so a later pass does not re-flag

All 20 Hoefsmit pure tableaux and all eight multiplicities 4/2/1/3/3/1/2/4 —
including the counter-intuitive asymmetric 2/1/3 — with
`tr_pure = 41.6949`; all 7 skew-SYT counts; all 8 Plancherel weights
(summing to exactly 1); `Σ 1/dim_q` at n = 3,4,5,6 to the last printed digit,
and the exact 5/2, 19/6, 46/15, **473/144**; `Σ W_λ = 1` for the Frobenius
weights; `8G = 7.32772475342 = 2·V_oct` (**not** the `8·Cl₂(π/4)` error);
`Φ_q(0.989) = 671094`; `u(proton)` to **17 significant digits**; the
per-nucleon shift `1 + 18Z + 21N` exact in all six rows; `V_L(1) = (−2)^{n−1}`;
and the 3-CAL table.

**Pin discrimination — a useful negative.** No table in this batch separates
the proton pin from the muon pin at its printed precision. The erroneous
`1.1097` *is* excluded by `tr_pure` (41.56 vs 41.69), by `Φ_q(0.989)`
(7.0e5 vs 6.7e5) and by the parity-blind figures (6.7143e−1 vs 6.7145e−1) —
but **not** by `partition-sum-table1`, where all three pins print 1.2761.
