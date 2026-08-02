# Does a genuine GRADED substrate structure FORCE the top-cohomology concentration of Δ_λ? (NO — unified CANCELLATION mechanism; the concentration is an external categorification input)

**Date:** 2026-08-02 · **Epic:** `qou-r2nh` · **Bean:** `qou-7ygi` ·
**Branch:** `claude/deltalambda-graded-concentration-frontier-2026-08-02` · **PR #4581** ·
**Tier:** derivation / formalize-first (Lean, sorry-free) ·
**Scope:** (a) LIMITATIVE throughout; nothing fitted; nothing wired; no anchor inverted; L2 unchanged.

- Lean: [`QOU/BraidsAndKnots/DeltaLambdaGradedConcentration.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaGradedConcentration.lean) — sorry-free, `lean`-direct exit 0.
- Builds on: [`S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean) (`nStat`, `dim`, `deltaSign`, `deltaLambda`, `deltaSign_eq_nStat_parity`, `binding_magnitude_eq_dim`) — all on `main`.
- Direct parents (all merged / in flight, sorry-free): PR #4553 (single-degree `dtEuler` object, the VALUE); PR #4559 `qou-ylot` (moduli under-determined); PR #4570 `qou-nmpr` (SDP ungraded); PR #4574 `qou-71ma` (jet-order valuation degree-blind).

## The crux (the deepest, last-standing leg)

The VALUE `Δ_λ = (-1)^{n(λ)}·dim V_λ = DT(𝓑_λ)` is proved sorry-free and general
(#4553; `dtEulerG_eq_deltaLambdaG` + `chiralityParity_eq_w0_sign_general` on main).
The one input that upgrades it to the full geometric "Behrend-signed DT count of the
Springer fibre" is the **single-degree (top-cohomology) concentration**
`H^{2n(λ)}(𝓑_λ) = V_λ`, which distinguishes the concentrated Springer object `G_λ`
(= `Δ_λ`) from the honest coinvariant object `H_λ` (`V_λ` with graded multiplicity
`f_λ(q)`, whose signed evaluation `f_λ(-1) ≠ Δ_λ`). Three cheap forcing routes are
PROVED-DEAD:

- **#4559** (`qou-ylot`): the DT-**count** identity under-determines the moduli (pins
  only parity mod 2 + count). Count route dead.
- **#4570** (`qou-nmpr`): the confinement **SDP / T_w / tr_M** are UNGRADED functionals
  (factor through `⊕_λ End(V_λ)`; no degree variable). SDP route dead.
- **#4574** (`qou-71ma`): the GS jet-order **valuation** is degree-blind (reads the
  bottom grade only; monic leading coeff `1 ≠ dim`). Valuation route dead.

**THE question (this bean, `qou-7ygi`): does a genuine GRADED structure — not a
count / ungraded functional / valuation, but the jet-order/coinvariant TOWER itself,
a KLR / Demazure grading, the confinement filtration — force `G_λ` (top-degree
concentration) rather than `H_λ` (full coinvariant spread)?**

## Corpus / sibling state (grep + coordinate)

- **What the substrate's honest graded object IS (fixed by the corpus).** Per
  [`option-e.md`](../coordination/option-e.md) (2026-07-18 front (i); 2026-06-28
  fake-degree hidden-DOF), [`PrincipalGradingJetOrder.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/PrincipalGradingJetOrder.lean),
  and [`2026-07-11-deltalambda-grho-jet-order-derivation.md`](2026-07-11-deltalambda-grho-jet-order-derivation.md):
  the GS jet-order **tower** is the classical **fake-degree / coinvariant grading** —
  `V_λ` appears in the length-graded regular (coinvariant) representation with graded
  multiplicity the **fake-degree polynomial** `f_λ(q) = Σ_{T ∈ SYT(λ)} q^{maj T}`
  (Macdonald I.5; Steinberg / Lusztig), total `f_λ(1) = dim V_λ`. The valuation
  `n(λ) = min_T maj(T)` is only its *bottom exponent*. So the honest graded object the
  drivers produce is the **spread** object `H_λ` (graded dims = coefficients of
  `f_λ(q)`), NOT the concentrated `G_λ`.
- **KLR / Demazure give the same spread.** In the semisimple regime (substrate `q₀`
  generic, not a root of unity — the archimedean evaluation) the type-A KLR graded
  structure and the Demazure character grading both decategorify to the same fake-degree
  graded multiplicity of `V_λ`; none concentrates. (KLR-as-Δ_λ-closure was already
  assessed 0/6 in [`2026-05-30-klr-dialog-assessment.md`](2026-05-30-klr-dialog-assessment.md);
  §7b crystal techniques are authoring shortcuts, not a concentration mechanism.)
- **The concentration is everywhere IMPORTED as the classical Springer fact.** Corpus
  survey (Springer / fake-degree / coinvariant / top-cohomology / graded across
  `content/`, `docs/`, `computations/`): `H^{top}(𝓑_λ) = V_λ` is always cited (Springer
  1978 in `DeltaLambdaDTIndex.lean`), never derived from a substrate grading. No prior
  artifact claims a graded structure FORCES concentration.
- **Distinct from — and sharpening — the open `DeltaLambdaDTRealization` conjecture.**
  That primary conjecture (content-bearing, no instance, #4553) asks whether the
  substrate forces the DT moduli `𝓑_λ`. This audit answers the graded sub-question left
  by #4570/#4574 and characterizes the *exact* missing ingredient.
- **Sibling coordination.** Distinct-angle intent to be posted on **#4574** (companion,
  `qou-71ma`, the valuation route) and **#4570** (`qou-nmpr`, the SDP route), naming this
  graded-TOWER angle. **#4554** (`A_ω=3`, `qou-qnnq`, merged) independently reached
  "structurally-open"; this converges by a fifth direction (graded cancellation).

## The test — result: NO, with a UNIFIED mechanism (formalize-first, sorry-free)

The four dead routes had four different-looking obstructions. This file proves they are
**one** obstruction — **CANCELLATION** — and that the cancellation exactly characterizes
the missing input.

For any graded object `l` (graded dims `l[i] ∈ ℕ`), write the signed (Behrend/DT) Euler
characteristic as **even-graded mass minus odd-graded mass**, `χ(l) = E(l) − O(l)`, with
ungraded total `Σ l[i] = E(l) + O(l)` (`altSum_eq_masses`, `sum_eq_masses` — general).

| lemma | statement |
|---|---|
| `abs_altSum_le_sum` | `|χ(l)| ≤ Σ l[i]` — the ungraded total (dim) is the CEILING on `|χ|` |
| `abs_altSum_lt_sum_of_both_parity` | `0 < E ∧ 0 < O ⇒ |χ(l)| < Σ l[i]` — two-parity support ⇒ STRICT cancellation |
| `abs_altSum_eq_sum_of_single_parity` | `E = 0 ∨ O = 0 ⇒ |χ(l)| = Σ l[i]` — only a cancellation-free object saturates |
| **`deltaLambda_realization_is_cancellation_free`** | **THE FRONTIER: any `l` with `Σ l = dim V_λ` and `χ(l) = Δ_λ` is forced cancellation-free (`E=0 ∨ O=0`)** |
| `fake_both_parity` | `H_λ` carries positive mass at BOTH parities on every `dim > 1` block |
| `fake_abs_altSum_lt_dim` | `|χ(H_λ)| < dim V_λ` — the cancellation, quantified |
| `fake_cancels_ne_deltaLambda` | `H_λ` (the honest jet-order/coinvariant TOWER) never equals `Δ_λ` |
| `single_is_single_parity` / `single_gradedEuler_eq_deltaLambda` | `G_λ` is single-parity and `= Δ_λ` |
| **`graded_structure_cannot_force_concentration`** | **the packaged crux (same total; `H_λ ≠ Δ_λ`; `G_λ = Δ_λ`; any realization forced single-parity)** |

Since `|Δ_λ| = dim V_λ = Σ` (`binding_magnitude_eq_dim` ⇒ `abs_deltaLambda_eq_dim`), a
graded object realizes `Δ_λ` **only if it saturates the ceiling**, i.e. **only if it is
cancellation-free (single grade-parity)**.

### Fake-degree data at `n = 5` (`H_λ` cancels; both parities present on every non-trivial block)

`f_λ(q) = q^{n(λ)}·[5]_q!/∏_{cell}[h]_q`; graded dims are its coefficients; `E`/`O` = mass
at even/odd grades.

| λ | `n(λ)` | `dim V_λ` | `f_λ(q)` | `E(H_λ)` | `O(H_λ)` | `χ(H_λ)=f_λ(-1)` | `Δ_λ` |
|---|---|---|---|---|---|---|---|
| `(5)` | 0 | 1 | `1` | 1 | 0 | `+1` | `+1` |
| `(4,1)` | 1 | 4 | `q[4]_q` | 2 | 2 | `0` | `-4` |
| `(3,2)` | 2 | 5 | `q²[5]_q` | 3 | 2 | `+1` | `+5` |
| `(3,1,1)` | 3 | 6 | `q³[3]_q(1+q²)` | 2 | 4 | `-2` | `-6` |
| `(2,2,1)` | 4 | 5 | `q⁴[5]_q` | 3 | 2 | `+1` | `+5` |
| `(2,1,1,1)` | 6 | 4 | `q⁶[4]_q` | 2 | 2 | `0` | `+4` |
| `(1⁵)` | 10 | 1 | `q^{10}` | 1 | 0 | `+1` | `+1` |

Every `dim > 1` block has `E > 0 ∧ O > 0` (mass at both parities), so `χ(H_λ)` cancels to
`f_λ(-1)`, strictly below `dim` — never `Δ_λ`. The two `dim`-1 blocks are single monomials
(`q^0`, `q^{10}`): vacuously single-parity, so there `G_λ = H_λ` and both `= Δ_λ` (hence the
`dim ≠ 1` hypothesis).

**Reading.** Every algebraic graded object the substrate produces is a genuine graded
MULTIPLICITY space: it distributes the `dim V_λ` copies of `V_λ` across a *run of
consecutive grades* `[n(λ), …]` (the fake degree `f_λ(q)`), so it carries mass at BOTH
grade-parities and its signed Euler characteristic CANCELS. `Δ_λ = ±dim V_λ` is the
cancellation-FREE extreme, attained only by piling the entire `dim V_λ` onto a *single*
grade-parity — the top-cohomology projection `H^{2n(λ)}(𝓑_λ) = V_λ` (Springer 1978). That
projection is a statement about the cohomology of a specific VARIETY (the Springer fibre),
**not** any operation the algebraic gradings (jet-order tower / coinvariant / KLR-semisimple
/ Demazure) perform — they all realize `H_λ`, never `G_λ`.

## Proved / open split

- **PROVED (sorry-free, this file):** any graded object realizing `Δ_λ` under signed-Euler
  is forced to be cancellation-free (single grade-parity)
  (`deltaLambda_realization_is_cancellation_free`, general over `List ℕ`). The honest
  jet-order/coinvariant TOWER `H_λ` is a genuine two-parity multiplicity space, so it
  cancels (`|χ(H_λ)| < dim`) and can NEVER equal `Δ_λ` (`fake_cancels_ne_deltaLambda`).
  This UNIFIES the count (#4559), SDP (#4570), and valuation (#4574) negatives under one
  mechanism.
- **OPEN (unchanged, now sharply characterized):** whether the 13 categorical drivers can
  produce a **cancellation-free graded object** — equivalently, a driver-internal
  construction of a space with a symmetric obstruction theory whose cohomology is
  concentrated in the single degree `2n(λ)` with fibre `V_λ` (the Springer top-cohomology
  isomorphism *realized from the drivers* rather than imported). The primary conjecture
  `DeltaLambdaDTRealization` stays open; the missing ingredient is now precisely named:
  the **removal of the multiplicity-grading cancellation**, i.e. single-parity
  concentration.

## Verdict

**NO — no algebraic graded substrate structure forces the concentration**, proved as a
scope-(a) LIMITATIVE negative with a single structural backbone: the substrate's graded
objects are graded multiplicity spaces with two-parity support (genuine cancellation,
`χ = f_λ(-1)`), whereas `Δ_λ = ±dim` is cancellation-free and requires single-parity
concentration — the geometric top-cohomology projection, an INDEPENDENT categorification
input the drivers do not supply. This is **not** a claim that concentration is excluded
from every closure: a genuine graded substrate structure that is cancellation-free by
construction remains the (now precisely characterized) live route. The graded route is the
fourth and deepest candidate forcing mechanism to fall (count / SDP / valuation / graded
tower); a fifth-direction convergence with #4554 (`A_ω=3` structurally-open).

**Does NOT reopen the VALUE.** `Δ_λ = (-1)^{n(λ)}·dim V_λ` is a function of two substrate
SCALARS — the jet-order valuation parity (`deltaSign_eq_nStat_parity`) and the Wedderburn
dimension — both derived without any graded/geometric object. Only the DT/Springer
geometric REALIZATION is open; the number's derivation stands on its own legs.

## Anti-fit / honesty ledger

- **0 free parameters**; `Δ_λ`, AME, CODATA, `q₀` never inverted; the fake-degree
  polynomials `f_λ(q)` are the standard coinvariant graded dimensions (hook-length;
  `f_λ(1) = dim V_λ` machine-checked).
- Formalize-first honoured: the limitative claim is a sorry-free Lean statement; the
  structural core (`deltaLambda_realization_is_cancellation_free` and the three cancellation
  lemmas) is **general** over `List ℕ`, not an `n=5` artifact. No `sorry`, no
  `True`-conclusion, no `native_decide`/`decide`-laundering (the `decide`s discharge
  genuinely-finite concrete integer computations at `n=5`); base ring `ℤ`/`ℕ` (§7c — no
  archimedean construct).
- **No instance of the open realization conjecture fabricated.** The proved content is
  LIMITATIVE (no algebraic grading forces the concentration; a successful structure must be
  cancellation-free) — it does NOT close `DeltaLambdaDTRealization` and does not launder it.
  "Axiomatization is NOT a proof", "sorry-free ≠ derived", "conditional-proved ≠
  premise-established" respected.
- corpus-grep run before the "open"/"does-not-force" declaration (Springer / fake-degree /
  coinvariant / jet-order / KLR / top-cohomology paths walked across `content/`, `docs/`,
  `computations/`; the honest graded object confirmed to be the fake-degree spread `H_λ`
  from `option-e.md` + `PrincipalGradingJetOrder.lean`).

## Cross-references

- The VALUE (proved): PR #4553, [`2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md`](2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md).
- Count route dead: PR #4559, [`2026-08-01-deltalambda-dt-substrate-derivation.md`](2026-08-01-deltalambda-dt-substrate-derivation.md) (`qou-ylot`).
- SDP route dead: PR #4570, [`2026-08-02-deltalambda-sdp-topdegree-projection.md`](2026-08-02-deltalambda-sdp-topdegree-projection.md) (`qou-nmpr`).
- Valuation route dead: PR #4574 (`qou-71ma`), `DeltaLambdaJetOrderDegreeSelection.lean`.
- `A_ω=3` mirror (`qou-qnnq`): PR #4554.
- Jet-order tower = fake-degree / coinvariant grading; fake-degree hidden-DOF: [`docs/coordination/option-e.md`](../coordination/option-e.md); [`2026-07-11-deltalambda-grho-jet-order-derivation.md`](2026-07-11-deltalambda-grho-jet-order-derivation.md); `PrincipalGradingJetOrder.lean`.
- KLR / crystal not a concentration mechanism: [`2026-05-30-klr-dialog-assessment.md`](2026-05-30-klr-dialog-assessment.md); AGENTS.md §7b.
- Primary sources: Springer, *A construction of representations of Weyl groups*, Invent. Math. 44 (1978) 279–293, https://doi.org/10.1007/BF01403165 (`H^{top}(𝓑_λ) = V_λ`, single-degree concentration); Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., OUP 1995, §I.5 (fake degree `f_λ(q)`, coinvariant graded multiplicity of `V_λ`); Behrend, *DT type invariants via microlocal geometry*, Ann. of Math. 170 (2009) 1307–1338, https://doi.org/10.4007/annals.2009.170.1307.
- AGENTS.md §"Axiomatization is NOT a Proof"; §"Before declaring open/refuted"; §"Strict Lean Discipline"; §"Conditional-proved ≠ premise-established".
