---
# qou-emyt
title: 'EXCISION (measured): convention C is a PRODUCER-layer problem -- 70 producers, 86 witnesses, 12 content blocks'
status: todo
type: task
priority: normal
created_at: 2026-08-09T19:35:36Z
updated_at: 2026-08-24T03:13:41Z
---


## What the ruling asked for, and what it actually costs

Owner ruling 2026-08-09: **"excise all convention C"**, "switch to D, we need to be
consistent anywhere." The scope was estimated from a grep (`181 files match`).
That estimate was wrong in an important way — most of those matches are
*labelled* C references (history, comparisons, excision notes) which are fine
and should stay. The real surface is smaller in content and far larger in code.

Measured 2026-08-09 with the new mechanical axis
`content/pipeline/trace-convention-audit.ts` (committed 997cfca7a, selftest 10/10):

| layer | C sites | note |
|---|---|---|
| live producers hardcoding `z_C = 1/(q^½+q^-½)` | **70** | `computations/`, `qou-mass/`, `tools/`; excludes `_deprecated/` |
| committed witness JSONs carrying a C value | **86** | regenerate-only, never hand-edit |
| content blocks failing the axis | **12** | 1 critical + 11 `gram-inverse-unqualified` |
| shipped `qou-mass` package | **1** | |

Content sweep: 3108 blocks scanned, 646 in scope, 12 failing. So the content
layer is ~2% of the job. **The excision is a producer-layer change**, and every
producer touched drags its witnesses with it.

## The one critical content defect

`prf:interface-knot-markov-z`
(`content/quantum-observable-universe/mass-theory/interface-knot-markov-z-proof.md:56`)
— the 4-atom verification table is entirely convention-C arithmetic:

| atom | p₊ | p₋ | in the block (C) | under production D | shift |
|---|---|---|---|---|---|
| D    | 1 | 0 | 0.49932033 | 0.61268803 | +22.7% |
| T    | 1 | 1 | 0.14493273 | 0.24729788 | +70.6% |
| ³He  | 2 | 0 | 0.24932079 | 0.37538663 | +50.6% |
| ⁴He  | 2 | 1 | 0.07236786 | 0.15151645 | **+109.4%** |

(computed at 60 dps with `decimal`, NO-FLOAT64 respected; `h = q − q⁻¹ =
0.20906029879563931543`, `z_C = 0.49932033418369445241`,
`z_D = 0.61268803714646525160`.)

**Two defects in one block.** Besides the convention, it claims "Max rel. err.
across all 4 atoms: ~10⁻¹⁵ — exact at f64 precision" — a float64 claim under a
NO-FLOAT64 directive.

**Do not hand-edit this table.** Producer is `computations/mass_at_3A_proper.py`
(`atom_braid_word_3A`) via `pyhecke_native`; regenerate under D.

**The identity itself is convention-independent.** `tr_M^FULL/tr_M^CONSTIT =
z^{p₊}(z−h)^{p₋}` follows from the Markov property plus the Hecke quadratic
relation and holds for *any* Markov parameter `z`. So regenerating under D
should reproduce agreement to the same ~10⁻¹⁵ — and if it does, the block gets
*stronger*, because the identity is then confirmed at two independent values of
`z` rather than one. That is the check to run, not a number to retype.

## The 11 `gram-inverse-unqualified` blocks are a MATH defect, not a label defect

These assert the Markov pairing on `H_n(q)` is non-degenerate, that
`det G ≠ 0`, and that `G⁻¹` enters the Frobenius co-Casimir
`C = Σ (G⁻¹)_{ij} b_i b_j`. Under D **all of that is false about `H_n`**:
`y₍₁³₎ = 0`, so the antisymmetric block *is* the radical and `det G = 0` exactly.

Not "numerically singular" — exactly. Under C, `y₍₁³₎ = 0.0227449…` is small but
nonzero and `G` genuinely inverts. A `G⁻¹` computed under C is **not an
approximation** to one under D, because the latter does not exist.

Blocks affected:
- `prop:vertex-algebra-relations` (climax-volume-mass) md:249
- `prf:shell-closure-stability` (knots-particles-confinement) md:27
- `def:frobenius-dual-h3` (mass-theory) md:2, 11
- `rem:frobenius-gram-matrix-context` (mass-theory) md:5, 6
- `prop:frobenius-gram-matrix` (mass-theory) ts:37
- `rem:gram-matrix-spectral-connection` (mass-theory) md:9,10,12,14,33,68,77,78 ← worst
- `prf:operator-selection-lp` (mass-theory) md:56
- `rem:confinement-frobenius-reciprocity-interpretation` (nuclear-interactions) md:7,20,23
- `sec:garside-gram-intro` (nuclear-interactions) md:1
- `conj:e-hartree-categorical-derivation` (predicted-spectra) md:49
- `prf:knot-operator-selection` (predicted-spectra) md:44

**The repair is citation, not deletion.** The Frobenius structure is real — it
lives on `H_n / rad τ ≅ TL_n(δ)`, not on `H_n`. `QOU/QBeta/MarkovGramDegenerate.lean`
proves both halves so each block can be repaired by pointing at a theorem:

1. `TemperleyLiebTower.conventionD_kills_antisymmetriser` — the pin forces `y₍₁³₎ = 0`
2. `block_mem_radical` — a zero-weight block lies in the trace radical (cyclicity is the content)
3. `gram_det_eq_zero_of_radical_combination` — a radical element in the span puts a
   nonzero vector in `ker G`, so `det G = 0` ← **this refutes the 11 blocks**
4. `TemperleyLiebTower.traceRadical_two_sided` — radical is a two-sided ideal, quotient is a ring
5. `pairing_descends` — the pairing is constant on radical cosets
6. `mem_radical_of_pairing_zero` — and is non-degenerate on the quotient
   ← **this tells the 11 blocks where to move the claim**

Corank accounting (`RankAccounting` section): `n=3` corank 1, `n=4` corank 10
(`3²+1²`), `n=5` corank 78 (`6²+5²+4²+1²`).

## Order of attack

1. ✅ mechanical axis committed, so a relapse is detectable (997cfca7a)
2. ✅ Lean refutation + descent (`MarkovGramDegenerate.lean`)
3. repair the 11 gram blocks by citation — cheap once (2) builds
4. regenerate `prf:interface-knot-markov-z` from its producer under D
5. the 70 producers + 86 witnesses — **needs a scoped plan and owner sign-off on
   blast radius**: this moves published numbers (per the registry, 195.8 ppm on
   β_Bor and −197 ppm on m_p). Do NOT start this as a text substitution.

## NEEDS OWNER

Step 5 is the real excision and it is not a mechanical edit. Two sub-questions:
- do the 70 producers switch to D wholesale, or does each get audited for whether
  its result is convention-scoped at all (many may be C-independent)?
- the 86 witnesses regenerate from their producers — but that is 86 producer runs,
  serialised (never two producers concurrently in one checkout).

---

## CORRECTION (same session): the producer count above is WRONG

The "70 producers" figure in the table above, and in commit 8e8860509's message,
is an artefact of a loose grep. The pattern included a bare `0.5 + ` alternative,
which matches any occurrence of that string anywhere in any Python file — it was
not measuring convention C at all.

Re-measured with patterns that actually pin the convention-C definition of `z`
(`q0**0.5 + q0**(-0.5)`, `Q0**0.5 + Q_INV0**0.5`, `q_half + q_half_inv`,
`sqrt(q) + 1/sqrt(q)`, `A + 1/A`), excluding `_deprecated/`:

| layer | claimed | **actual** |
|---|---|---|
| live producers defining `z` the C way | 70 | **13** |
| witness JSONs with a C fingerprint | 86 | **59** at ≥8 sig digits (86 at ≥7 — the looser threshold pulls in short quotations) |
| content blocks failing the axis | 12 | 12 (unchanged — this one was mechanical) |

The 13:

```
computations/atom_mass_derived.py
computations/atom_mass_partition.py
computations/deltalambda/deuteron_trefoil_qinvariant_closed_form_probe.py
computations/deltalambda/nuclear_quotient_jones_torus_link_probe.py
computations/free-neutron-decay.py
computations/garside-irrep-qvalues.py
computations/mass-from-q-symbolic.py
computations/phase5/phase3b_universal_vs_knot_specific_decomposition.py
computations/qbeta/qbeta_habiro_phase5q_dn_refactorize.py
computations/qbeta/qbeta_symbolic_chain_alpha_b.py
computations/rigid_monoidal_gap_invariance_check.py
computations/substrate/deuteron_tower_fusion_frame_probe.py
computations/substrate/hecke_core_symbolic.py
```

Six other producers already define `z` the D way, and the registry's
`entry_points` are **all** convention D — which is the tell I should have taken
seriously before quoting 70. The mass/binding pipeline has already migrated; what
is left is a tail of probes and two or three live computations.

**This makes the excision materially smaller and changes the recommendation.**
It is no longer "needs a scoped plan and owner sign-off on blast radius" as a
blocker — 13 files is a reviewable change. The blast-radius question still stands
for whichever of the 13 feed published numbers (`atom_mass_derived.py`,
`mass-from-q-symbolic.py`, `free-neutron-decay.py` are the ones to check first),
but the other ten look like probes whose results are convention-scoped anyway.

Lesson for the axis: the mechanical content sweep was right (12, and it stayed
12). The two numbers I got wrong were both hand-greps done outside the
instrument. Where a detector exists, quote the detector.

---

## Progress 2026-08-09 — content layer 31 → 17

Two more detector findings after the first sweep, both of which changed the count:

**`c-formula-unlabelled` (new detector).** The axis only saw decimal literals; a
block writing `z = 1/(q^{1/2}+q^{-1/2})` quotes no number and passed. That
symbolic form is the *larger* surface — 20 files against 1. Real starting point
was **31 failing blocks, not 12**. Two bugs found while testing it:
`TRACE_SURFACE` didn't know the phrase "Markov parameter" (so such blocks were
out of scope and *no* detector could fire), and three new fixtures passed
vacuously by being out of scope. `Case.scope` now asserts in-scope-ness.

**`gram-inverse-under-d` (new, critical).** Found by my own repair going wrong.
`gram-inverse-unqualified` cleared on "some convention is named nearby" — so
after switching `frobenius-gram-matrix-context` to D, its still-false `G⁻¹` claim
*passed*. Relabelling was a way to silence the detector. Split the rule:
`RADICAL_CAVEAT` (already relocated to the quotient) clears; `C_LABEL` nearby
clears (true under C); any other convention means D, and the claim is **false**,
so it fires critical. Naming the convention you are wrong under is worse than
naming none.

### Repaired (14 blocks, all re-scanned clean)

| block | kind of repair |
|---|---|
| `per-braid-mass-tower` | dropped the √q reason for ℝ; two valid reasons remain |
| `hecke-satisfies-blitvic-hypothesis` | √q was its ONLY reason for ℝ — flagged, not generalised |
| `markov-trace-product`, `vhat-pair-commutation-trace-proof`, `wedderburn-mass-formula-proof`, `prop-rigid-monoidal-…`, `markov-trace-axiomatic-closed-form` (.md+.ts), `rho-k-graded-expansion`, `markov-trace-factorization`, `mass-endomorphism-tower`, `volume-perturbation-formula` | straight z → D swap; safe (no residual √q, no z-dependent numbers) |
| `frobenius-gram-matrix-context` | the real correction: det G = 0, corank 1, read G⁻¹ on TL₃ |
| `h3-markov-wenzl-weights` | **a reversed owner adjudication** — see below |

### The reversed adjudication (worth owner attention)

`h3-markov-wenzl-weights`'s 2026-06-13 note scopes its closed forms to the
Jones/TL trace and warns they "must not be read as the general tr_M y_λ", because
the pipeline used a *different* trace (full-Hecke Ocneanu, y₍₁³₎ ≠ 0). It closes:
**"Owner adjudication 2026-06-13 (full-Hecke canonical; scope the prop, do not
re-normalize the pipeline)."**

The 2026-08-09 ruling reversed exactly that. Convention D **is** the Jones/TL
trace — registry name "SU(2)/Temperley-Lieb (Jones) decomposition";
`thm:jones-markov-trace` says D "lands on the Jones–Temperley–Lieb normalisation
exactly". So the pipeline no longer uses a different trace, it uses *this* one;
y₍₁³₎ = 0 not ≠ 0; the traces no longer "diverge at q ≠ 1"; and the closed forms
are the general ones. **Every clause of the caveat inverted.** There may be other
artefacts of the 2026-06-13 adjudication still in place — worth a sweep for
"full-Hecke canonical" as a phrase.

### Remaining: 17 blocks

**7 `c-formula`, all needing judgement rather than a swap:**

- `markov-trace-recursive-reducer` — quotes z-dependent traces (proton
  1.633154…, neutron 1.248248…). **Producer run, do not retype.** This is why the
  safety test must check numbers as well as √q: it has zero residual √q mentions
  and would have passed a √q-only filter.
- `y-lambda-cyclotomic-factorization` (12 residual √q — built on `q̌ = q^{1/2}`),
  `markov-pair-z2` (4), `conj-rho-k-pair-gen-canonical-form` (3),
  `explicit-alpha-k-h3` (2), `shell-structure-eigenvalues` (2),
  `qvalue-derivation-chain` (1) — each genuinely uses the half-argument variable,
  so switching z is a substantive change, not a relabel.

**19 `gram-inverse` hits across 9 blocks**, all refuted by
`MarkovGramDegenerate.lean`. The `frobenius-gram-matrix-context` callout is the
template — copy it and adjust:

```
climax-volume-mass/vertex-algebra-relations.md                      x1
knots-particles-confinement/shell-closure-stability-proof.md        x1
mass-theory/frobenius-dual-h3.md                                    x2
mass-theory/gram-matrix-spectral-connection.md                      x8   ← worst
mass-theory/operator-selection-lp-proof.md                          x1
nuclear-interactions/confinement-frobenius-reciprocity-interpretation.md x3
nuclear-interactions/garside-gram-intro.md                          x1
predicted-spectra/e-hartree-categorical-derivation.md               x1
predicted-spectra/knot-operator-selection-proof.md                  x1
```

`gram-matrix-spectral-connection` already contains its own refutation without
noticing: it writes `G_{λμ} = δ_{λμ}·τ(e_λ)`, block-diagonal with the **weights**
on the diagonal. Under D one weight is zero, so its own formula gives det G = 0 —
two lines after it asserts `G⁻¹_{λμ} = δ_{λμ}·[n]_q!/(dim_q(λ)·dim(λ))`, which
divides by zero for that block.

**Stale q₀ (separate defect, not convention-related):**
`frobenius-gram-matrix-context` carries `1.109978595554181`; canonical q₀ is
`1.1099785827513808…`. Diverges at the 9th significant digit. Not fixed here —
it is a witness value and needs a producer, and it is out of this axis's scope.

---

## Final state of the content layer: 31 → 6

All 22 `gram-inverse` hits cleared. `gram-inverse-under-d` reports zero, so the
Frobenius claims are relocated rather than merely relabelled. 25 blocks repaired,
each re-scanned clean.

Lean verification: `lake build` of `MarkovGramDegenerate`, `TemperleyLiebTower`,
`QDimNormalisation`, `BallotNumbers`, `YoungDiagramThreeRowCorner`,
`WedderburnTraceDecomposition`, `GramSignature`, `InterfaceScalar` **plus their
full import closure — 2032 jobs, exit 0.** That is the closure of what this work
touches, **not** the whole `QOU` library: two attempts at `lake build QOU` were
killed by container restarts at ~1 hour each (it was live and progressing both
times — `HeckeH4BlockMap31`/`BlockMap211` alone take 30+ min CPU apiece). The
whole-library build is still owed.

### One correction propagated three times, found by one detector

`markov-trace-frobenius-selection-proof` had already retired its `ℚ(q^{1/2})`
hypothesis as "an artefact of convention C, whose z = 1/(q^{1/2}+q^{-1/2}) needs
the square root; convention D's z = q³/(q²+1) does not". Three other blocks were
missed when that propagated, and all three were invisible to a value-based sweep
because none of them quotes a number:

1. `hecke-satisfies-blitvic-hypothesis` — the √q was its **only** stated reason
   for an `ℝ` trace codomain. Flagged, **not** generalised: losing the stated
   reason is not proving no reason exists, and `pairWeight`/`centredMoment` are
   unaudited. Open Lean question.
2. `per-braid-mass-tower` — same argument as one of three reasons; the other two
   (absolute values, `Φ_q`) stand, so the conclusion is unchanged.
3. `qvalue-derivation-chain` — claimed `V̂_i` exact in `ℚ(q^{1/2})` when `z` was
   its only √q source and the transfer matrix `T` is over `ℚ(q)`. Corrected to
   `ℚ(q)`.

### Remaining 6

| block | why it is not a swap |
|---|---|
| `interface-knot-markov-z-proof` | the 4-atom table, **producer run** (`mass_at_3A_proper.py`). Also claims "exact at f64 precision" under NO-FLOAT64. |
| `markov-trace-recursive-reducer` | quotes z-dependent traces (proton 1.633154…, neutron 1.248248…) — **producer run**, do not retype |
| `y-lambda-cyclotomic-factorization` | built on `q̌ = q^{1/2}` (12 residual √q); the half-argument variable is structural here |
| `explicit-alpha-k-h3` | 2 residual √q in the prefactors |
| `shell-structure-eigenvalues` | 2 residual √q |
| `conj-rho-k-pair-gen-canonical-form` | 3 residual √q |

### Flagged, deliberately unpatched

`markov-pair-z2`'s Hopf-link normalisation
`J_Hopf = -(q^{1/2}+q^{-1/2})·z²`. The prefactor is the half-argument loop
parameter `[2]_√q = 2.0027…`; the production TL loop value is
`δ = [2]_q = 2.010896866707122…`. Under D — which *is* the Jones/TL trace — both
the prefactor and `z²` move, so the second equality cannot be assumed. Editing
the prefactor to quiet the detector would ship an unchecked formula, which is the
same failure mode as the relabelling loophole. Needs a derivation. See `qou-98g5`.

---

## RETRACTION: the "stale q₀" in `frobenius-gram-matrix-context` was not stale

An earlier entry on this bean reported:

> **Stale q₀ (separate defect, not convention-related):**
> `frobenius-gram-matrix-context` carries `1.109978595554181`; canonical q₀ is
> `1.1099785827513808…`. Diverges at the 9th significant digit.

**That was wrong.** There are two *legitimate, documented* pinnings of q₀:

| pinning | value | derivation |
|---|---|---|
| proton | `1.1099785827513808075916690956107688798744991218736` | the registry's `meta.q0.value`, citing `computations/substrate/q_parameter.py` |
| muon | `1.10997859555418057528159407960950937799328227995870` | `Vol(4₁)/(m_μ/m_e)`, i.e. `HBAR_Q_SQ = VOL_FIGURE_EIGHT / MASS_RATIO_MU_E` |

`computations/substrate/q_parameter.py` supports selecting between them
explicitly — *"When muon is selected, we re-derive the ENTIRE q-family (f64 +
`_MP` + `Q_50_DIGIT_STR`)"* — and `qou-mass`'s own `q_parameter.py` is the
muon-pinned family. `1.109978595554181` is the muon q₀ to the digits quoted, not
a stale copy of the proton one.

I inferred "stale" from a digit-9 mismatch against the registry without checking
whether a second pinning existed. It did. Nothing to fix in that block on this
count.

**Consequence for verification:** a convention-D `z` must be checked against the
q₀ of *its own* module. Under the muon pinning `z_D = 0.6126880505455892`, not
the registry's `0.6126880371464652`; both are correct convention D. Checking a
muon-pinned module against the proton-pinned registry value would report a false
failure at 2.2e-8. The R9 evaluator and the two `pyhecke_native` gates all use
the proton-pinned registry value and all run against proton-pinned code, so they
are unaffected — but any future gate placed on muon-pinned code must not reuse
that constant blindly.


---

## Evidence from `claude/mass-table-comprehensive-triage` (2026-08-23/24)

This bean measures the excision as 70 producers / 86 witnesses / 12 content
blocks and sits at `todo`. A staleness-drain campaign on that branch produced
**seven independent instances of the migration's downstream cost**, all found
by accident while looking for something else. They are worth recording here
because they are what the backlog looks like when it is not migrated.

**1. `qbeta_jacobi_anger_tower_general` — a frozen convention-C constant.**
`PHYSICAL_WEIGHT_RESIDUAL_N3 = 0.0683508`, copied from a reference producer.
Under D the same reference yields 0.142709 and the two harnesses still agree
exactly; only the copy had rotted. Fixed by reading the reference LIVE
(9a5d18462).

**2. `qbeta_sym_part_hecke_natural_form` — an EXACT identity re-indexed.**
`sym = -h·h̃/2` (full-q × half-q, /2) under C becomes `-h·H/8` with
H = q⁴−q⁻⁴ (full-q × q⁴, /8) under D. The structure survives — still a product
of two bar-antisymmetric quantities — so the identity was never refuted, only
re-indexed. Six sympy identities verify to 0 (cffc1265f).

**3. `a4_brunnian_deficit_closed_form` — a third frozen literal.**
`measured = 1.000145898` against a D value of 1.0001284313359779…, agreeing to
~14 significant digits once the measurement probe is re-run under D. Fixed by
reading the witness live (bf3c70c8c).

**4. `atomic-tr-m-helium4-canonical`** — `abs_tau_4he_positive` 0.1539 → 0.4185;
recorded pass 2026-05-25, producer untouched since 08-02.

**5. `alpha-em-b2-canonical-scale-ratio`** — `y_(4,1)` 0.10937853 (≈ 7/64,
convention C) → 0.12498540 (≈ 1/8, D, trace-certified to 5.0e-31). A C-era
7/64 was being served past its own gate.

**6. `nucleus_real_sdp` ×4 atoms (he3, deuteron, he4, tritium)** — tr_M moves and
`negative_norm_blocks` / `sign_flip_conjugate_pairs` empty to `[]` on every
atom. The payload shrink IS the content becoming correct.

**7. `qbeta_ck_local_taylor_around_u0_probe` — NOT a stale pass, a dead solve.**
Under D the Wenzl bridge returns `y_(1,1,1)` as the INTEGER 0 (the row cap
y_λ = 0 for ℓ(λ) > 2), so `tr_M = y₃χ₃ + y₂₁χ₂₁ + y₁₁₁χ₁₁₁` loses its third
term and a 7-unknown fit loses a degree of freedom it needs. `mnewton`'s
Jacobian is singular, identically at dps 50/60/70/90. **The producer cannot
compute its answer at all under the current formulation** — see bean qou-w7qk.
That one is not fixable by re-reading a constant; it needs a re-derivation.

## The finding that should change how the remaining 70 are approached

**Twice the migration reached a producer through an IMPORT, and a file-grep
pre-check could not see it.**

  - qou-w701: `cyclic_intertwiner_verify` contains none of the family names;
    `a_operator_gauge_align` changed the p-n interface underneath it.
  - qou-w7qk (#7 above): the probe contains no reference to `y_lambda_at`,
    `gram`, `TR_M` or `habiro-coefficients-atomic` — it imports
    `y_lambda_wenzl_bridge_symbolic`, a different entry point to the same
    family.

Quantified afterwards (`computations/audits/import_staleness_audit.py`): of
2122 witnesses the self-staleness axis rates FRESH, **921 (43.4%) sit on a
first-party import committed after the witness was computed**, and the modules
that move most are `q_parameter` (914), the constants family, and
`pyhecke/gram` (703) — the C→D families exactly.

**So any triage of the 70 must follow first-party imports, not grep the file.**
Grepping will systematically under-count, and the two hardest instances found
on that branch are both in the part it misses.
