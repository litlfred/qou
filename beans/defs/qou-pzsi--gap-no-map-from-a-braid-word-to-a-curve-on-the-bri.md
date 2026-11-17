---
# qou-pzsi
title: 'GAP: no map from a braid word to a curve on the Bring surface — the embedding-energy selection rule cannot be built without it'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T16:50:05Z
updated_at: 2026-10-10T12:30:00Z
parent: qou-v2om
---



## The gap, precisely

Opened 2026-09-14 from the owner's objection on `qou-99qc`: *"The selection rule
shouldn't be minimum crossing... It may be higher energy than a non-minimal
crossing. A sibling has worked on connecting hecke energy to O'Hara energy via
brings embedding... You're minimizing not just the hecke energy but how the knot
is embedded into brings surface."*

**Why it is needed.** The gluon-dressing selection on `qou-99qc` is blocked on
its cost function. Two proxies have been measured and both fail, for one
structural reason:

- **crossing count** — `FrobeniusSelected`'s own instantiation. Ties σ₁ with
  σ₁⁻¹.
- **crossing energy** (`def:crossing-energy`) — breaks that tie (σ₁⁻¹ = −0.90092
  beats σ₁ = +1.10998) but ties all three 2-crossing candidates at `2q`.

Both are **sums over letters**, hence constant on the permutation orbit of a
letter multiset — while the closure is not. That is now a **scope-(b) structural
exclusion of the whole letter-sum class** (probe
`qbeta_embedding_energy_can_discriminate_probe.py`, 5/5, PR #7370): σ₁σ₀ and
σ₀σ₁ have the same multiset and the same writhe `+2` and close to **different
links** (traces apart by 6.78e-2 / 1.42e-2). So no functional of the multiset
alone can select here, for any `q` and any coefficients.

**And an isotopy-class energy is NOT barred** — all four 2-crossing candidates
are distinct links, so the O'Hara/Möbius **infimum** can take different values on
them. Green light for the route on discriminability grounds.

## What exists

- [`mobius_cross_energy_hopf_calibration.py`](computations/mobius_cross_energy_hopf_calibration.py)
  — a cross-energy integrator **calibrated against the proved** `E(Hopf) = 2π²`
  (Agol–Marques–Neves, arXiv:1205.0825), mpmath end to end.
- `mobius_cross_energy_borromean.py`, `mobius_borromean_topology_guard.py`.
- `QOU.MobiusEnergy` — categorical `E_cat` from the Frobenius–Hopf
  comultiplication and the q-Hodge star, with the encoded relation
  `E_cat = ¼·E_classical + const`.
- Bring machinery: period matrix, mapping-torus residue weights, zero modes.
- Beans `qou-zfs6` (Möbius invariance / FHW bound / minimiser as Lean gates) and
  `qou-dux3` (the Möbius-invariant exponent) are `completed`; `qou-6xt9`
  (ingest the knot-energy literature) is `in-progress`.

## What is missing — the gap itself

**Any map from a braid word to a curve in or on the Bring surface.** The
integrators consume hand-parametrised *named* embeddings (Hopf, Borromean);
nothing feeds them an arbitrary 9/10/11-letter Hecke word. Searched
`computations/` and `tools/` for embedding/curve/parametrisation code near
"bring", and for every consumer of
`mobius_energy|ohara_energy|E_mobius|mutualIntegrand|cross_energy`.
`embeddable_knot_operator.py` is **not** it — it is σ/π orbital-overlap
weighting with a per-system `w_perp`. **An absence on the surfaces searched, not
a proof of absence.**

## Why it is hard, not merely unbuilt

Möbius energy is a property of an **embedding** and is **not a knot invariant** —
it varies over the isotopy class, and the invariant is the **infimum** (FHW). So
"the energy of a word" needs either

1. the **minimiser** over the isotopy class (existence is the FHW theorem's
   content, and computing it is a variational problem), or
2. a **canonical embedding** — which is exactly what the Bring surface would be
   for, and is the substantive proposal.

That is the research content. It is not a wiring job.

## Caveat that must not be skipped

`QOU/MobiusEnergy.lean` carries **2 sorries**, and its own header records a
prior vacuity incident in which `classicalLimit` made `E_cat` **blind**
(`E_cat = 1 + const` for every knot) **with no `sorry` to flag it**. The
categorical↔classical leg therefore cannot bear weight unexamined — check it
before building on it.

## Next honest step

Not "build the bridge". First establish which of (1) or (2) above the Bring
surface is supposed to supply, and whether `E_cat`'s classical limit is sound
after the recorded vacuity incident. Until then the gluon dressing stays
unselected and the `qou-99qc` dashboard rows stay un-re-scored.

## 2026-09-14 (session gifted-feynman) — the caveat checked: both its reasons are wrong, and its conclusion is right for a better one

This bean's "Next honest step" names two things to establish before building.
The second — *whether `E_cat`'s classical limit is sound after the recorded
vacuity incident* — is settled here. **Both stated grounds for doubt are wrong,
and a third, worse one is proved.**

**1. "`QOU/MobiusEnergy.lean` carries 2 sorries" — FALSE. It carries ZERO.**
Measured on the merged head: `grep -cE '(^|[[:space:]])sorry([[:space:]]|$)'`
returns **0**, and the file is `lean`-direct **exit 0**
(`-DautoImplicit=false -s 65536`), so that is an elaborated fact, not a parse
artifact. The three `sorry` strings in the file are all prose — two inside the
docstring *describing* the incident, one in a §-heading.

**2. The vacuity incident is FIXED, and has been since 2026-08-30.** The field
now reads `unknot_iff : value = 4 ↔ isUnknot`, which is the Freedman–He–Wang
statement. The broken spelling was `value = 4 ↔ True`; `P ↔ True` is `P`, so it
forced `value = 4` for *every* instance and, through `classicalLimit`, made
`E_cat = 1 + const` for every knot. The file's own docstring records the repair.
So the bean's caveat is **stale**, not merely imprecise.

**3. 🛑 But there is a SECOND defect in the very same field, it is live, and it
is worse.** `CategoricalMobiusEnergy.classicalLimit` reads

    energy = (1/4) * classicalEnergy.value + classicalLimitConst

and `classicalLimitConst` is a **free field of the same structure**, occurring
once and linearly. So the field **constrains the pair `(energy,
classicalEnergy)` not at all**: for any `e` and any `c` whatever, exactly one
constant satisfies it. Proved, sorry-free, appended to the file itself:

| declaration | statement |
|---|---|
| `QOU.classicalLimitConst_eq` | `classicalLimitConst = energy − ¼·classicalEnergy.value` — determined by the other two fields |
| `QOU.classicalLimit_unconstraining` | `∃! k, e = ¼·c.value + k` for **every** `e` and **every** `c` |

`#print axioms` on both: `[propext, Classical.choice, Quot.sound]`, no `sorryAx`.

**Why it matters, in the framework's terms.** The mathematical statement the
docstring quotes — `lim_{q→1} E_cat(γ) = ¼ E(γ) + const` — means a **universal**
constant, the same for every knot. That is what carries the content. Encoded
**per instance**, the content is gone: the categorical energy and the classical
energy are related by nothing.

**It is the same class as the incident the file already records** — *"no
`sorry`, no `axiom` and no tautological conclusion, so no vacuity detector saw
it"* — one field over, and it **survived that repair**. The 2026-08-30 fix
corrected `unknot_iff` and did not look at the field consuming it.

**Not repaired, deliberately.** Making the constant universal changes what the
structure asserts; that is an authoring decision for the owner, not an agent's
fix, and §ASK THE OWNER applies. Recorded in the file and here.

**Corpus-grep before claiming:** `classicalLimitConst` appears **nowhere else**
in the corpus — not in any bean, audit, probe or other `.lean`. Not previously
recorded.

**So this bean's conclusion stands and its reasons should be replaced.** The
categorical↔classical leg still cannot bear weight — not because of sorries
(there are none) or the old blindness (fixed), but because the bridge field is
unconstraining as encoded. Open item (1) — *which of minimiser-or-canonical-
embedding the Bring surface is meant to supply* — is untouched and remains the
live research question.

---

## CORRECTION (2026-09-14) — the headline claim of this bean is WRONG

This bean, and PR #7370 which opened it, assert that the corpus has **no map
from a braid word to a curve in or on the Bring surface**. The owner said
otherwise and was right. `computations/qbeta/qbeta_cusp_lattice_geodesic_probe.py`
carries exactly that map, on the author's own steering of 2026-07-27: *"we can
associate to a braid word a geodesic (flow) on the torus for the particle/vortex
path"*. It is filed under **geodesic**; I searched for *embed / curve /
parametrise* near *bring*, and for consumers of the Möbius integrators, and the
map was one word away from every query I ran. A detector-blindness instance in
my own corpus-grep, not in a tool.

What was genuinely missing was the **geodesic → O'Hara energy** step, and that is
now built (`qbeta_bring_ohara_bridge_probe.py`, 7/7, merged #7374).

## What the built bridge gives — a NEGATIVE, and it is structural

`(m, ℓ) = (exponent sum, strand count)`. Both are letter-sum-type: the exponent
sum is a sum over letters, the strand count does not depend on the word at all.
So all four two-crossing gluon dressings share one lattice class, one geodesic
and one energy. **The O'Hara energy is innocent; the cusp-torus embedding is the
lossy step**, and it provably forgets the knot — the class is computed before the
modulus is ever consulted, so no modulus can repair it.

## Modulus sensitivity — DERIVED from Neumann–Zagier, correcting my own number

The bridge computes at `ω = e^{iπ/3}`, the shape at the **complete** structure
`u = 0`; the framework evaluates at meridian log-holonomy `∼ ln q₀ ≠ 0`, which
is the concern `qbeta_cusp_shape_drift_robustness_probe` raises. I first answered
it by drifting `ω` by hand at the `O(u) = 10.4 %` scale and reported 3.9–16.3 %
energy shifts. **That was an assumption about the drift dressed as a measurement
of it.**

`qbeta_neumann_zagier_cusp_modulus_probe.py` (8/8) derives the deformation from
NZ's own gluing equations (65)–(66) for `4₁` by series-inverting `u(v)`:

    τ(u) = 2√−3 · (1 + u²/3 + O(u⁴))

with `τ₀ = c₁ = 2√−3` and `c₃/c₁ = 1/3` **exactly**, matching NZ eq. (68) at
that slot; NZ eq. (52)'s odd-only structure is **verified on the computed
series**, not imposed, which is what forces the leading correction to be `u²`.
Cross-check worth having: `2√−3 = −2 + 4ω` **exactly**, so the NZ
meridian–longitude lattice is the index-4 sublattice of the corpus's hexagonal
`ℤ⟨1, ω⟩` (`cusp-shape-bar-parity.md`) — two independent sources, one lattice,
an exact integer relation.

Consequence: the real drift is **second order**, so the `(2,3)` energy moves
**0.163 %** (`u = ln q₀`) or **0.637 %** (`u = 2 ln q₀`), against the 4.29 % my
hand-picked `O(u)` drift gave. The bridge's figures are **robust at the
sub-percent level**, and the concern is answered without needing the
normalisation binary resolved — both branches clear it.

## What stays OPEN

The `u = ln q₀` vs `u = 2 ln q₀` meridian normalisation is the same factor of two
as bean `qou-yh67`'s NZ-½ binary (`κ_shape = √3/2` vs `κ_pot = √3/4`, the
`Φ = 2𝔙` factor), which `qou-yh67` records **cannot be settled numerically**.
Both branches are computed and **neither is adopted** — choosing the one that
lands a target is selection against the target. The factor enters `τ` squared, so
the two drifts differ by exactly 4×.

The `qou-99qc` dashboard rows stay un-re-scored and the gluon dressing stays
unselected: this bridge does not select, and nothing here proposes that it
should.

## 2026-09-14 (session gifted-feynman, 2) — THE FORK COLLAPSES: the answer is NEITHER

This bean asks which of (1) the FHW minimiser or (2) a canonical Bring embedding
supplies "the energy of a braid word", and calls it the research content.
**Measured, and neither branch survives.** Probe
`computations/qbeta/qbeta_candidate_closures_are_links_probe.py` (5/5).

### Route (1) cannot be cited: the candidates are LINKS, not knots

The closure of a braid word has one component per cycle of its underlying
permutation. Computed exactly in `S₃` (integer arithmetic; **no floats anywhere
in the probe**, inputs, intermediates or witness):

| candidate | letters | permutation | components |
|---|---|---|---|
| `nuc9` | 9 | `(0,2,1)` | **2** |
| **`nuc11_interleaved`** — LIVE SCORED | 11 | `(0,2,1)` | **2** |
| `nuc11_gen_grouped` | 11 | `(1,0,2)` | **2** |
| `…σ₁σ₀` | 11 | `(1,0,2)` | **2** |
| `…σ₀σ₁` | 11 | `(2,1,0)` | **2** |
| `…σ₁σ₁` | 11 | `(0,2,1)` | **2** |
| `…σ₀σ₀` | 11 | `(0,2,1)` | **2** |

**Not one is a knot.** FHW Theorem B, as held
(`library/arxiv-math-9301212v1/sections/sec-000-2-…md:12-14`), reads verbatim:

> Theorem B. If K is a smooth prime (not a connected sum) **knot**, then there
> exists a simple closed rectifiable γ_K of knot type K with E(γ_K) ≤ E(γ) for
> all rectifiable loops γ which are topologically ambient isotopic to K.

and the document quantifies throughout over **a single** curve `γ : S¹ → R³`
(`sec-front-matter.md:25-26`). A 2-component link satisfies neither hypothesis.
**Scope-(b); the invariant is the component count.**

**The corpus agrees from the other side.** `def:hadron`
(`content/…/knots-particles-confinement/hadron.md:3`) defines a hadron as
`K_1,…,K_n` **prime knot types** ⊕ `𝓛` a **link** — a composite of primes *and*
a link, i.e. both things Theorem B excludes, at once.

### 🛑 What is NOT claimed, and the distinction is load-bearing

This does **not** show no minimiser exists for these links. That is the
**Kusner–Sullivan CONJECTURE**, and the held text says so in terms
(`library/arxiv-1905.06064v1/sections/sec-000-1-introduction.md:85-86`):
*"Kusner and Sullivan **conjectured** that there are no minimizers in composite
knot classes, **supporting their intuition with numerical experiments** [33]."*
`[KS97]` is **not held**; FHW 1994 itself is **not held** (only the 1993 BAMS
announcement); and the held literature does not treat **links** at all. So:
Theorem B **does not apply** (proved), whether a minimiser exists anyway is
**open** — do not upgrade it.

### Route (2) is asserted nowhere

A canonical embedding of a braid word into/onto the **Bring** surface is not
proved, not conjectured, and not named as an object. Three homonyms are not it:
`prop:cohomological-embedding` is a genus/spectral admissibility **filter** for
**torus knots** and supplies no curve (and the corpus already flags the naive
geometric reading as **WRONG AS STATED**,
`docs/audits/2026-08-01-tau-knot-discussion-review.md:33`); *canonical
embedding* in the Bring audits means the algebro-geometric map of the genus-4
curve; and `qbeta_cusp_lattice_geodesic_probe` lands on the **genus-1 cusp
torus**, not Bring — its own bridge probe says *"the genus-4 Bring curve itself
is not used here"* — and is proved order-blind.

### So the question to ask is a different one

Not *which* of the two, but **whether the selection object should be a curve in
R³ at all**, given that every scored element is a 2-component link, that
`def:hadron` says so independently, and that the owner-ruled selection rule
(γγ + confinement SDP, `qou-ales`) already rejects `nuc11_interleaved` on the
`(2,1)` block. **That is an owner decision and is not taken here.** Nothing
selected, nothing re-scored.

### Two stale claims found in passing

`qou-6xt9`'s "WHAT IS ACTUALLY MISSING" lists (a) O'Hara 1991 not greppable and
(b) its DOI unverified. **Both are closed**: the paper is ingested at
`library/1-s20-0040938391900102-main/`, and `content/schema/references.ts:5602`
records the DOI verified 2026-09-13 against that full text. That bean wants an
update; not edited here, since it is another arc's.

## Option 4 enacted 2026-09-15 — the Möbius block is scoped in its own prose

The owner picked options 4 / 2 / 3 on `CategoricalMobiusEnergy.classicalLimit`
and asked for the formalize-first comparison first. The comparison established
that **option 2 (make the constant universal) is not available as the structure
is encoded** — `no_universal_classicalLimitConst` is now a sorry-free theorem,
so 2 is a request for new structure, not a value to supply. Option 4 is enacted;
option 3 (retire the field) is NOT, because retiring it would delete the affine
shape that is the block's actual content.

Enacted:

- `climax-volume-mass/mobius-energy.md` — a paragraph after the classical-limit
  display saying the additive constant is not determined by the construction,
  that every real value is realised by an additive shift preserving both Möbius
  invariance and the relation, and that a topological reading needs further
  structure fixing the additive zero of `E_cat`.
- `climax-volume-mass/mobius-energy.ts` — an `authorNotes` entry naming the
  three declarations and their axiom set.

Verification: render-QA grep battery clean (`$$` 6, inline `$` 52, braces 33/33,
`\Bigl`/`\Bigr` 3/3, no list-parser hijack, no non-ASCII inside math — the em
dashes are in prose, matching the file's existing §Archimedean paragraph);
`run-validate folio/quantum-observable-universe` against pinned platform
`df28d02` → **2 issue(s)**, both pre-existing and unrelated (a bibliography info
line, `lem:piece-a-corner-removal-obligation` without a Lean declaration).
No Lean changed in this commit.

The research target that option 2 actually names is `qou-uh5f`.


## 2026-10-10 — route 1 run: link Möbius energy of the canonical closed-braid embedding, multi-start (owner-chosen)

Owner, 2026-10-10: work the energy / O'Hara principle by **route 1**, *"Multi-start first"*, then record it. Probe: `computations/probes/ohara_link_energy/` (README there).

**Numerical evidence only.** Every value is a float64 **upper bound** from gradient flow, i.e. a local minimum. No Q_β, CODATA or mass number enters anything. Existence of minimisers is **open**: these are links, and FHW Theorem B covers prime knots only (2026-09-14 entry above).

**1. 🛑 Correction to this bean: the four 2-crossing gluon dressings close to TWO links, not four.** Checked by hand; the probe confirms it with matching Jones and Alexander polynomials. With `σ₁ = gen0` and `σ₂ = gen1`, `NUC9 = (σ₁σ₂)³·σ₁²σ₂`, and `Δ² = (σ₁σ₂)³` is central.
- `σ₁²σ₂·σ₁σ₂ = σ₁³σ₂σ₁ ~ σ₁⁴σ₂` and `σ₁²σ₂·σ₁σ₁ ~ σ₁⁴σ₂`. So **`gluon_s0_s1` ≅ `gluon_s0_s0` = `nuc11_interleaved`** (class B).
- `σ₁²σ₂σ₂σ₁ ~ σ₁³σ₂²`, and `σ₁²σ₂³ ~ σ₁³σ₂²` by conjugation with Δ. So **`gluon_s1_s0` ≅ `gluon_s1_s1`** (class A).

"All four 2-crossing candidates are distinct links" (§"The gap, precisely") holds for the corpus's **q-shift-decorated letters**, not for any geometric closure. The traces that differ there are traces of the decorated elements.

**2. Calibration.**
- Hopf: `8 + 4π² = 47.4784`; the flow gives 47.4805–47.4839, with the mutual term always ≥ 2π² and within 0.012 %.
- Trefoil: 74.42. The literature ≈74.4 is not held in `library/`, so it is unverified.
- Möbius invariance holds to 3e-13.

**3. Ranking (multi-start, pre-registered analysis).**

| pair | gap | combined error | separated? |
|---|---|---|---|
| nuc9 (234.2) < A (≈291.0) | 56.7 | 1.1 | yes |
| nuc9 < B (≈291.6) | 57.9 | 0.9 | yes |
| A < gen_grouped | 23.6 | 1.0 | yes |
| B < gen_grouped | 22.4 | 0.7 | yes |
| **A vs B** | **1.1** | **1.2** | **no** |

- Route 1's single-start A/B gap of 4.8 was an artefact: every start landed in one of B's four local minima.
- `gen_grouped` did not converge (12 different minima from 12 starts).
- The discrete flow undercounts the energy by a shape-dependent 0.4–0.8 at N=256, which limits how finely close minima can be ranked.

**4. 🛑 What this route can never do.** The flowed link energy depends only on the isotopy class, so it **cannot separate `gluon_s0_s1` from `nuc11_interleaved`**: they are the same link. If those must be told apart, no embedding energy of the closure can do it. What distinguishes them is the decoration on the letters, not the closure.

**What it does give.** An order-sensitive, parameter-free ranking that separates `nuc9` from the 11-letter dressings, and both from `gen_grouped`. It cannot currently decide between the two gluon-dressing classes.

**Not claimed.** Nothing is selected or wired, and no dashboard row is re-scored. Disclosed post-hoc method changes are listed in the probe README.

**Open next steps (none started).**
- To try to settle A vs B: flow the spectral functional directly, and put more points on the knotted component. Both are method changes and would need a new pre-registration.
- Route 2 (a Bring-surface embedding) remains undefined.
- Route 3 (`qou-uh5f`) is untouched.

## 2026-10-11 — CORRECTION: route 2 used sign-erased candidates (results_signed.md)

Route 2 and options 1 through 1d (and route 1, ohara_link_energy) took the seen candidates from the sign-erased generator list in qbeta_candidate_closures_are_links_probe. The canonical nucleon (pyhecke.atom.build_nucleon_nf) has a (σ₀σ₁⁻¹)³ core and averaged ud letters, so it is a SUM OF FOUR BRAIDS. Under route 2 every proton term has a Bring loop (L = 9.21 / 15.94 / 6.37 / 20.44), whereas the sign-erased nuc11 is parabolic with no loop. Every seen-candidate read-across from route 2 is WITHDRAWN, including 1d's "Rule A → nuc11, Rule B → class A". The fresh-positive-word results stand. γγ words (σ₀σ₁⁻¹)^k never get a Bring loop under route 2's "exactly one fixed point" rule: this is a limit of the rule (3 ∤ k: no conjugate of Γ₀(2) contains the word; 3 | k: the word is pure, so all three conjugates contain it). Scope (a). The selection rule stays OPEN.


## 2026-10-11 (PR #7695)

Neutron expansion in `signed_candidates_probe.py` was wrong (uu→dd instead of ud·ud·dd); fixed and now checked against `build_nucleon_nf_mp`. Core (σ₀σ₁⁻¹)³ and 00001100011 are the same Bring loop though not conjugate. B3: under Hecke H₃(q₀) the 2×2 quantity reduces to Wedderburn characters, x = |χ_(2,1)|/√|χ_(3)χ_(1³)|, det = −([2]_q/2)⁴ for both nucleons; under Burau t = −q₀, det = χ_(3). The normalisations disagree in type on every row; neither adopted; B4 (no energy for sums) stays default. Selection still OPEN.

## Round 69 Formalization Progress (PR #8293)
- Formalized `QOU.shiftEnergy_comp_const_and_energy` (sorry-free, 0 advisories across all 6 static vacuity audits).
- Verified at 80-dps `mpmath` (`computations/probes/scale_mobius_adjoint_reduced_trefoil_probe.py`, `scriptHash: ae187b673714`, Commit 1 `9b139cda51963d9af6817b576a80c90bb2f74d00`, Commit 2 / Witness `474ee8c61ef5b687f244b6a129aeb23ef9956372`, PR `litlfred/qou#8293`).
