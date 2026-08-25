---
# qou-n1dj
title: 'GAP: does the MASS fibre functor land in Rep(SU_q(2))~TL or full H_3(q)? (corpus self-contradiction, D vs C, 197 ppm on m_p)'
status: todo
type: task
priority: normal
created_at: 2026-08-08T09:50:22Z
updated_at: 2026-08-16T03:04:29Z
---

> **Status reverted to `todo` by the parent session (2026-08-08).** The research
> question below is **answered** — convention **D**, see the verdict block — but
> closing a bean is a **human action** (AGENTS.md §4a: agents may move an item to
> in-progress and may add findings, never to resolved/completed). Both sibling
> agents on this bean left the status untouched for that reason. The owner closes
> it. Nothing about the technical verdict is affected by this revert.


## RESOLVED 2026-08-08 — the answer is D, and the premise was already in the mass chapter

Branch `claude/n1dj-mass-fibre-dimension-2026-08-08`. Full analysis:
[`docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md`](../docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md).

**Reframing "which trace?" → "which fibre?" made it answerable, because the mass
chapter already states the fibre.** `lem:feynman-eigenbasis-decomposition`
([`feynman-eigenbasis-decomposition.md`](../content/quantum-observable-universe/mass-theory/feynman-eigenbasis-decomposition.md))
defines the mass channel's decomposition as

    V^(tensor n)  ≅  ⊕_{λ ⊢ n, ℓ(λ) ≤ 2}  V_λ ⊗ S_λ ,   V = fundamental of SU_q(2)

with the **row cap `ℓ(λ) ≤ 2` in the index set** and `⌊n/2⌋+1` summands (the
two-row count). At `n = 3` the sum is `{(3), (2,1)}`: **`(1³)` is absent**, so
`y_(1³) = 0` is not an extra assumption — it restates the decomposition the mass
chapter already uses. Feed it into the sorry-free
`markovWeights_eq_jones_of_threeRow_eq_zero` ⟹ **convention D, uniquely.**

**And the block that defines the trace does not merely imply D — it IS D, in
closed form.**
[`feynman-markov-identification.md`](../content/quantum-observable-universe/mass-theory/feynman-markov-identification.md)
defines the mass amplitude as `Σ_{λ⊢n, ℓ(λ)≤2} w_λ · tr_{S_λ}(ρ_n(β))`, says
*"This equals the **Jones**–Markov trace `tr_M`"*, and gives
`w_λ = dim_q(V_λ)·dim(S_λ)/dim_q(V^{⊗n})`. At `N=2` (`dim_q V_λ = [2j+1]_q`,
`j = (λ₁−λ₂)/2`, `dim_q V^{⊗n} = [2]_q^n`), `n=3`:

| λ | ℓ(λ) | j | dim_q V_λ | y_λ = dim_q V_λ/[2]_q³ |
|---|---|---|---|---|
| (3) | 2 | 3/2 | [4]_q | 0.50540422650393080 |
| (2,1) | 2 | 1/2 | [2]_q | 1/[2]_q² = 0.24729788674803460 |
| (1³) | **3** | — | — | **absent from the index set** |

= convention D's vector, all three components, with the Schur–Weyl
normalisation `[4]_q + 2[2]_q = [2]_q³` exact. Machine-checked (probe C6:
normalisation = 1 to 50 digits, err vs D `3.3e-52`, Markov residual `1.1e-50`).
So the corpus's own mass-trace definition **already computes D** — the
"full-Hecke Ocneanu" Scope note contradicts a definition two blocks earlier.

The CODATA match was not used. Chain: fibre → row cap → `y_(1³)=0` → D.

**Sub-task 1 (find the independent argument) — DONE, plus new Lean.** New
sorry-free file
[`QOU/BraidsAndKnots/FibreDimensionForcesTL.lean`](../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/FibreDimensionForcesTL.lean)
(generic `[CommRing R] [IsDomain R]`, division-free, no `ℝ`/ordering/`q₀`;
`scripts/lean-verify.sh` exit 0; `#print axioms` clean on all 5):

- `qNumber_shift_identity` — `q[N+1] − q⁻¹[N−1] = q^N[2]`
- `ocneanu_param_eq_of_fibre_qdim` — **`z·[N]_q = q^N`**: the fibre's quantum
  dimension *determines* the Ocneanu parameter, so a fibre leaves **no residual
  trace freedom**
- `ocneanu_param_of_two_dim_fibre` — `N=2 ⟹ z(q+q⁻¹) = q²`, **verbatim** what
  `MarkovTraceTLUniqueness` concludes, but derived from `dim_q V = [2]_q` with no
  reference to the TL quotient. Independent cross-check, two routes one parameter.
- `threeRow_eq_zero_of_jones_ocneanu` — the converse, closing the biconditional
- `twoDimFibre_pins_h3_weights` — composite

**Sub-task 2 (reconcile) — the Scope note of `prop:h3-markov-wenzl-weights` is
the wrong side.** It says mass/binding use the full-Hecke Ocneanu trace with
`y_(1³) ≠ 0`; that contradicts the mass chapter's own `ℓ(λ) ≤ 2` decomposition,
`qou-w5fw` (N = qdim of fibre; `dim V = 2`), `qou-fvzm` (main `f92a8b15`,
"N = 2 is LOCKED IN for the mass pipeline"), and what production computes.
**Not edited here** — content change with its own review surface + sidecar +
render-QA gate. Filed as follow-up in the audit §Follow-ups.

**Sub-task 3 (false sensitivity claim) — confirmed refuted**, and it is the
Scope note's own load-bearing justification, so the note does not survive its
correction either.

**New: convention C corresponds to NO integer fibre dimension.**
`z(N) = q^N/[N]_q = (q−q⁻¹)/(1−q^{−2N})` is strictly decreasing in `N` for
`q > 1`, hence injective, so `N = −ln(1−(q−q⁻¹)/z)/(2 ln q)`.
[`computations/ocneanu_param_from_fibre_dimension.py`](../computations/ocneanu_param_from_fibre_dimension.py)
(5/5 pass, 50 dps, **proton** `q₀` pin recorded, `uses_experimental_target_values:
false`): `z_D → N = 2.0`, `z_{N=3} → N = 3.0`, but
`z_C = 1/(q^{1/2}+q^{-1/2}) = 0.4993203341836945 → N_eff = 2.5995155364`.
Scope **(b)**, invariant named: **integrality of a fibre dimension** (+ the
injectivity above + `ocneanu_param_eq_of_fibre_qdim`). C is not the categorical
trace on any fibre — conditional on the corpus's own definition of mass as a
categorical trace on `V^{⊗n}`. **NOT claimed:** that C is not a Markov trace on
`H₃(q)`; it is one, a fine member of the Ocneanu family.

**Colour — the mass chain does NOT inherit the `N = 3` problem.** Three spin-½
strands in a 2-dim fibre cannot be antisymmetrised (`dim V_{(1³)} = C(N,3) = 0`
for `N < 3`, `RowCapObstruction.weyl_dim_alt_eq_zero_iff`). Colour antisymmetry
is load-bearing in the eightfold chapter and does need `N ≥ 3` — but that is a
**different fibre and a different functor** (`ocneanu_N_lockin_probe`: the two
traces are not proportional, so it cannot be reached by re-tuning), so the
open `N = 3` construction (`qou-8p1x`) is not on the mass chain's critical path.

**Literature — one source read, the rest unobtainable.** Read: Jones 1985
(Bull. AMS 12(1) 103–111, `jones1985`, from `library/`). Its relations (I)–(VI)
p.2 state the TL trace is *"completely determined"* by `tr(1)=1` + cyclicity +
the single `tr(w e_{n+1}) = t/(1+t)²·tr(w)` — an upstream corroboration that a
TL-factoring trace has no free parameter. Thm 12 p.5 is the one-variable Jones
skein (`N=2`), not two-variable HOMFLY. Unobtainable: `jones1987`, `geck2000`,
`kassel1995` (paywalled — cited as existing, **no claim attributed**);
`wenzl1988` PDF (entry exists in `references.ts` with verified metadata, but the
`ℓ(λ) > N` weight-vanishing is *believed standard, not verified in-sandbox*);
FYHLMO 1985 (`www.ams.org` egress-blocked — **no `ref()` added**, metadata
unverified). `paper-search` MCP returns `[]`/`{}` for every query including a
known-good DOI. No `ref()` entry added; `references.bib` untouched.

**No production numerical value changed.**

Spun out of [`qou-3qrv`](qou-3qrv--class-i-is-the-borromean-trace-convention-forced-o.md)
on 2026-08-08 (branch `claude/3qrv-borromean-trace-convention-2026-08-08`), which
answered everything *except* this. Full analysis:
[`docs/audits/2026-08-08-borromean-trace-convention-forcing.md`](../docs/audits/2026-08-08-borromean-trace-convention-forcing.md).

## The one open question

> Does the Archimedean / fibre functor for the **mass** channel land in
> `Rep(SU_q(2)) ≃ TL₃`, or in the full `H₃(q)`?

Everything else is settled. This is a **categorical** question, and it must not
be answered by reading off which value matches CODATA — that is precisely the
failure mode `qou-3qrv` was opened to test for.

## Why it matters — 197 ppm on m_p, and the corpus disagrees with itself

Two normalised Markov traces on H₃(q) sit 195 ppm apart on `β_Bor`:

| | weight vector `(y_(3), y_(2,1), y_(1³))` at q₀ | `tr_M(β_Bor)` |
|---|---|---|
| **D** — Jones / Temperley–Lieb | `(0.505404, 0.247298, 0)` | 0.998562163836787 |
| **C** — full-Hecke Ocneanu / Wenzl z-trace | `(0.415396, 0.280930, 0.022745)` | 0.998366622585716 |

Both are legitimate (`Σ_λ y_λ d_λ = 1` for both) — two members of the Ocneanu
one-parameter family at different `z`.

- **Production uses D**: `canonical_mass.py:108` → `F_Bor` →
  `m_p_substrate_identity_50dps.trM_borromean`.
- **The paper says C**: the scope note of `prop:h3-markov-wenzl-weights`
  ([`h3-markov-wenzl-weights-context.md`](../content/quantum-observable-universe/mass-theory/h3-markov-wenzl-weights-context.md))
  states verbatim that the mass and binding computations use the **full-Hecke
  Ocneanu** trace at `z = 1/(q^{1/2}+q^{-1/2})`.

Switching production D→C moves m_p by **−197 ppm** (2026-07-03 impact probe),
destroying the CODATA match. So the two statements cannot both stand.

## What is already proved (do not re-derive)

`QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean` (sorry-free, no `sorryAx`,
generic `[CommRing R] [IsDomain R]`, division-free): the TL condition
`y_(1³)(z) = 0` has exactly two roots — `z = q`, degenerate (weights `(1,0,0)`,
not faithful on TL₃), and `z = q³/(q²+1)`, which **is** convention D. So:

> **TL ⟹ D, uniquely.** The implication is closed. Only the premise is open.

## Sub-tasks

1. **Find or write the independent argument** that the mass channel's fibre is
   2-dimensional (spin-½ / `Rep(SU_q(2))`) rather than the full Hecke module.
   In-tree hooks not yet chased: `QOU/Knots/KauffmanTL3.lean`,
   `conj:s5-so3-fiber-action`, `QOU/MathlibExt/WenzlSchurElement.lean`.
2. **Reconcile the two corpus statements.** The closed-form proof block and
   `h3-markov-wenzl-weights-context.md` §Scope disagree about which trace feeds
   mass. One is wrong; decide which and fix it.
3. **Correct the false sensitivity claim.** The same scope note says the two
   traces coincide on writhe-0 / π=id braids so "every physical mass prediction
   is insensitive to the distinction". `β_Bor` is writhe-0 with π=id and
   `D − C = 1.9554e-4` there **exactly** (nonzero rational function). The claim
   is refuted by a probe already in this corpus.
4. **Do not re-open the 6.7 %** — `qou-3qrv` settled it: `tr_M_atomic(1,0)`
   traces a different (11-crossing atomic) braid word, not `β_Bor`.

## Progress 2026-08-08 — the conditional is formalized (bean stays OPEN)

Branch `claude/n1dj-conditional-tl-forces-d-2026-08-08`; audit
[`docs/audits/2026-08-08-n1dj-conditional-tl-forces-jones.md`](../docs/audits/2026-08-08-n1dj-conditional-tl-forces-jones.md);
Lean
[`QOU/BraidsAndKnots/FibreCategoricalTraceForcesJones.lean`](../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/FibreCategoricalTraceForcesJones.lean)
(sorry-free, no `sorryAx`, `lean`-direct exit 0).

**What it buys.** The open question is now **one named premise** instead of a
chain, with every other link machine-checked:

> The mass channel's trace is the **categorical trace of the fibre action** on
> `V^{⊗3}`, rather than an abstract Ocneanu trace posited on all of `H₃(q)`.

Axiomatised as the §3b-cond class `MassTraceIsFibreCategorical R N` (row-cap
support `dim V_λ = 0 → y_λ = 0`, plus non-degeneracy of the surviving mixed
channel = faithfulness on `TL₃`). Granting it, plus `dim V = 2` from
`thm:su2-emergence` as an explicit hypothesis,
`markovWeights_eq_jones_of_fibre_categorical` **derives**
`[2]_q² y_(2,1) = 1 ∧ y_(3) = 1 − 2y_(2,1) ∧ z·[2]_q = q²` — convention **D** —
via the already-proved row-cap obstruction and Markov-trace uniqueness.
`ocneanu_eq_jones_of_fibre_categorical` excludes **C** under the same premise.

The class mentions neither `q`, nor `z`, nor the Jones vector, nor D, so this is
a derivation and not a self-assuming projection. Magnitudes are deliberately
*not* assumed (at `q ≠ 1` the weights are quantum, not classical, Weyl
dimensions — `y_(3)/y_(2,1) = 2.0437 ≠ 2` at `q₀`), which makes the conditional
stronger, not weaker.

Three anti-vacuity lemmas: `exists_fibre_categorical_markov_trace` (the
antecedent **has** a model at `N = 2` satisfying all three Markov equations —
D itself, at `z = q − t`, `t = [2]_q⁻¹`, so the conditional is not vacuous);
`weightAlt_ne_zero_at_three` (the class **alone** does not give Temperley–Lieb —
at `N = 3` it admits a nonzero `(1³)` weight, so `dim V = 2` is load-bearing);
`fibre_ne_zero_of_zero_dimensional` (premise + normalisation is refutable at
`N = 0`, so the row-cap fields have real content).

**What remains open — the bean is NOT closed.** The premise itself. Nothing
here shows the mass channel *satisfies* `MassTraceIsFibreCategorical R 2`;
"conditional-proved ≠ premise-established". Sub-tasks 1 (find the independent
argument for the 2-dimensional mass fibre), 2 (reconcile the two corpus
statements) and 3 (the false sensitivity claim) are all untouched. Sub-task 1 is
now sharply posed: exhibit an instance of the class for the mass channel, or
show the mass trace is not of that form.

## Progress 2026-08-08 — sub-tasks 2, 3, 4 DONE; sub-task 1 STILL OPEN

Branch `claude/n1dj-trace-registry-guard-2026-08-08`. Audit:
[`docs/audits/2026-08-08-trace-convention-registry-and-doc-fix.md`](../docs/audits/2026-08-08-trace-convention-registry-and-doc-fix.md).
**No production numerical value changed. The bean stays open** — the
categorical question below is untouched.

**Sub-task 2 (which statement is wrong) — ANSWERED.** The scope note of
`rem:h3-markov-wenzl-weights-context` is the wrong one, but only in its
*empirical* claim. The corpus **definition** of the mass trace,
`prop:categorical-mass-markov` (`mass-endomorphism/categorical-mass-markov.md:13`),
names "the Jones–Markov trace, functioning as the Frobenius integral on `A`"
with `A = H_n(R,q)` — i.e. **algebraically, on the full Hecke algebra**, no
fibre functor, no TL quotient. `rem:markov-axioms-primitive:5` then **pins**
`z = 1/(q^{1/2}+q^{-1/2})` as a stipulation (axioms 1–2 alone admit a
one-parameter family). So the definition chain says **C**. The scope note was
right about C being the corpus trace, right that **binding** uses it
(`binding_canonical.py` → `closed_form_tau_M.py:132 markov_z` +
`y_lambda_wenzl_bridge_numeric`), and **wrong that mass does** — production
mass is D (~30 `F_Bor` consumers). Correcting the doc does not resolve the
disagreement; it sharpens it into: *the corpus defines the mass trace as C,
production computes D, and D is the one matching CODATA.*

Consequence for sub-task 1: the charitable "the author was thinking
categorically, which is evidence for D" reading is **not supported at the
defining block**. The TL premise has no anchor in the definition chain.

**Sub-task 3 (the false insensitivity claim) — CORRECTED, with the true
lemma.** For any normalised Markov trace on H_3(q) and any writhe-0, π=id
braid: `tr_M(β) = 1 + y_(2,1)·(χ^(2,1)(β) − 2)` (verified symbolically for
arbitrary (y_(3), y_(1³)) under Σy·d = 1, plus `∂tr/∂y_(1³) = 0`, in
`computations/probes/probe_writhe0_trace_insensitivity.py`, PASS). So writhe 0
makes only the **y_(3)/y_(1³) split** invisible — the chirality asymmetry the
same block's own "Non-uniformity" section is about — and **not** y_(2,1). The
whole gap is one product: `(y^D_(2,1) − y^C_(2,1))·(−3h⁴ − h⁶) = 1.9554e-4`,
exact as a rational function, 195.82 ppm. The author had the right lemma about
the wrong ambiguity. The parent's alternative reading — "the traces agree on
braids whose image lies in TL_3" — is **refuted, scope (b)**:
`χ^(1³)(β) = (−q^{-1})^{w}` is a unit for every braid, so no braid image has a
vanishing three-row component.

**Sub-task 4 (do not re-open the 6.7 %) — now machine-enforced.**
`markov_peel.tr_M_atomic` and its aliases are recorded as **excluded tracers**
in the new registry; R7 of the validator errors if any convention row lists
them, and `--lint-docs` warns on doc lines pairing them with a Borromean
convention claim.

**New guard — the trace-convention registry.**
[`docs/coordination/trace-convention-registry.md`](../docs/coordination/trace-convention-registry.md)
+ JSON twin + `trace_convention_registry_validate.py` (R1–R8, `--selftest`,
`--lint-docs`, `--strict`). Channels carry **both** `definitional_convention`
and `production_convention`, so the mass dispute is a machine-visible field
rather than something a reader must reconstruct across two directories; R8
errors if a differing channel lacks an `open_item`. R3 recomputes each
convention's β_Bor value from the code it names (both CONFIRMED at 3.4e-19
relative). `--selftest` replays all three historical defects and fails if any
is not caught. Baseline: PASS, 0 errors, 21 warnings (21 Borromean tracers that
do not yet declare a convention — a tracked backlog).

**STILL OPEN (sub-task 1, the whole point of this bean):** does the mass fibre
functor land in Rep(SU_q(2)) ≃ TL_3 or in the full H_3(q)? Nothing above
answers it, and the definition-chain finding pushes *against* TL. Switching the
production trace is an owner decision (−197 ppm, ~30 consumers) and was not
done.

## Scope

Honest-gap bean per AGENTS §"When you can't close it". This is **not** a claim
that m_p is fitted or that D is wrong — D is a canonical, uniquely
characterised object. It is the narrower claim that D's *selection over C* does
not currently rest on an established premise, and that the corpus is
self-inconsistent about it.

## Progress 2026-08-16 — the bean's own framing is stale; and link 1 does not carry weight

Branch `claude/n1dj-fibre-premise-2026-08-16`. New sorry-free Lean:
[`QOU/BraidsAndKnots/VolumeConstraintForcesFibreTwo.lean`](../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/VolumeConstraintForcesFibreTwo.lean).
**No production numerical value changed. Bean stays open** — see the last section.

### First: two things above are no longer true of the corpus

Both are owner actions of **2026-08-09**, one day after this bean's last update,
and nothing above records them.

- **"The paper says C" — no longer.** `rem:markov-axioms-primitive` now fixes
  `z = q³/(q²+1)`, **convention D**, and says in terms that the earlier
  `z = 1/(q^{1/2}+q^{-1/2})` "is **convention C** … It is no longer the
  framework's trace".
- **"The corpus disagrees with itself" — no longer.** The Scope note of
  `rem:h3-markov-wenzl-weights-context`, identified above as the wrong side, has
  been rewritten: "the owner ruling of 2026-08-09 excised convention C. There is
  now **one** trace in the framework", and "the production mass channel uses
  convention D".

So the §"Why it matters" table, the "Production uses D / the paper says C"
split, and sub-task 2's conclusion that "the corpus **defines** the mass trace
as C" are all superseded. **The 197 ppm dispute is closed by ruling.** What
survives is narrower and is the honest remainder: *D's selection rests on the
row cap, the row cap rests on `dim V = 2`, and nothing establishes that.*

### Link 1 of the forcing chain does not carry weight

`markovWeights_eq_jones_of_fibre_categorical` takes `hN : N = 2` as an explicit
hypothesis "supplied by `thm:su2-emergence`". Chasing that citation:

- **The prose proof assumes the rank it is cited for.** `prf:su2-emergence`
  composes two lemmas *stated* as `G ⊆ SL(2, ℂ)` and `G ⊆ U(2)`. The `2` is an
  input to both. What is proved is which subgroup of a rank-2 general linear
  group survives — not the rank. `VolumeForm.lean` agrees in its own section
  heading: "SU(2) from **rank-2** + dagger".
- **Its `lean.ref` did not resolve.** `qou:QOU.RankOneGaugeData` — no such
  declaration exists anywhere in the tree; the canonical resolver returns
  unresolved. Before folio-assistant **PR #121** (merged 2026-08-16) it fell
  back to the import-only library root and every checker passed vacuously, which
  is why a dangling ref on link 1 of this chain survived unnoticed. **Repointed**
  to `qou:QOU.SU2Emergence`, which carries the theorem's own
  `\label{thm:su2-emergence}` — the label was the evidence, the ref's name was
  not. (Same failure mode, and same repair, as `qou-qc6s`.)
- **The Lean that does exist carries no rank content.** `QOU.SU2Emergence` has
  three fields: `gaugeGroupType : Type*`, `ext_sq_action`, and
  `det_one : ∀ g, ext_sq_action g = 𝟙 exteriorSquare`. It says a group acts
  trivially on the exterior square. It does not mention `SU(2)` and does not
  mention the rank; `exteriorSquare` is an unconstrained parameter. The two
  supporting lemmas are single-field classes restating their own conclusions
  (`SU2EmergenceVolumeDeterminant (det_g : ℝ) where det_eq_one : det_g = 1`),
  with docstrings recording the witness as pending Mathlib.

An `authorNote` on `thm:su2-emergence` now records this at the block, so the
next reader does not re-chase it.

### The framework already contains a source for the rank — now formalised

`def:quantum-observable-universe` condition (v), the **categorical volume
constraint**, posits a non-degenerate epimorphism `ε : Λ²V → 𝟙` preserved by all
tensor automorphisms. Read at the fibre that is a statement about `dim Λ²V =
C(N,2)`, and the two readings differ in strength — which is the point:

| reading of ε | dimension statement | forces |
|---|---|---|
| epimorphism (target hit) | `C(N,2) ≠ 0` | `N ≥ 2` only — admits the colour fibre `N = 3` |
| **iso** `Λ²V ≅ 𝟙` | `C(N,2) = 1` | **`N = 2`** |

Both are proved (`exteriorSquareDim_ne_zero_iff`, `exteriorSquareDim_eq_one_iff`),
stated in the same binomial idiom `RowCapObstruction` uses for the same `N`, so
the two constraints compose without a translation step.
`markovWeights_eq_jones_of_volume_constraint` and
`ocneanu_eq_jones_of_volume_constraint` are the forcing theorems re-sourced onto
`hvol` in place of `hN`. `weak_volume_reading_admits_three` is the anti-vacuity
check that the two readings genuinely differ in consequence.

This also puts the "colour does not infect mass" observation on a proof:
`exteriorSquareDim_three_ne_one` — the same axiom pins the two channels to
different ranks, so no re-tuning connects them.

Sorry-free: `#print axioms` gives `[propext, Classical.choice, Quot.sound]` on
all four, and **no axioms at all** on `weak_volume_reading_admits_three`. No
`sorryAx`. `check-base-ring` PASS, `check-wall-side` PASS, orphan gate exit 0,
`run-validate` exit 0. Registered in the `QOU.lean` umbrella.

This is **strictly better sourcing, not a discharge**: `N = 2` now comes from a
stated axiom of the framework rather than from a citation with no formal
content, and it is independent of every measured quantity — nothing in the file
mentions a numerical substrate value or compares against one.

### What is still open — and one item is newly visible

1. **The premise itself, unchanged.** `MassTraceIsFibreCategorical` — that the
   mass channel's trace *is* the categorical trace of the fibre action — is
   untouched. Everything above is about the *other* hypothesis.
2. **Which reading of condition (v) the author intends.** The forcing needs
   `Λ²V ≅ 𝟙`; the definition writes "non-degenerate epimorphism". Editorial, and
   not something Lean can settle. If the weak reading is intended, condition (v)
   gives only `N ≥ 2` and the rank is still unsourced.
3. **NEW — the formalised condition (v) is vacuous.** In
   `CategoricalFoundations.lean` it is `exteriorSquare : C` plus
   `volumeForm : exteriorSquare ⟶ (𝟙_ C)`, with nothing tying `exteriorSquare`
   to `Λ²(fundamentalObj)` and no non-degeneracy, epi, or invariance hypothesis.
   `QuantumUniverse` carries a `HasZeroMorphisms C` instance (needed for block
   orthogonality), so `volumeForm := 0` inhabits the field for *any*
   `exteriorSquare`. The formalised axiom therefore constrains nothing at all,
   and `QOU.SU2Emergence` inherits the same free parameter. Honest placeholders
   rather than errors — but a placeholder cannot be the source of a rank, so
   closing item 2 in the affirmative would still leave the Lean side to do.
4. **Do not use the `z·[N]_q = q^N` injectivity route to close this.** "D gives
   `N = 2` exactly, C gives `N ≈ 2.5995`, no integer fibre" already presumes the
   trace is the categorical trace of a fibre action of *some* integer dimension —
   which is premise 1. It is a good consistency check and a bad closure argument.
   The volume-constraint route above is independent of it because it never routes
   through the trace.

> **Status returned to `todo` (2026-08-16).** The slice above is finished and
> pushed on `claude/n1dj-fibre-premise-2026-08-16`; no session is holding this
> bean. The four open items in the preceding section are unclaimed and the next
> agent should take them without waiting.

## Progress 2026-08-22 — items 2 and 3 done; and item 2 was never mine to decide

Branch `claude/n1dj-volume-iso-reading-2026-08-22`. Owner instruction: take the
**iso** reading. **No production numerical value changed. Bean stays open** —
items 1 and 4 are untouched.

### Item 2 is settled by the corpus, not by an editorial call

The bean records item 2 as *"which reading of condition (v) the author intends
… Editorial, and not something Lean can settle."* That is true of Lean and
false of the corpus: **the author already wrote the answer, one block away.**
`lem:volume-from-rigidity`
([`volume-from-rigidity.md`](../content/quantum-observable-universe/quantum-observable-universes/volume-from-rigidity.md))
constructs this very `ε` and then says, verbatim:

> producing an epimorphism `ε : Λ²V → 𝟙`. **For `ε` to be non-degenerate, we
> must have `rank(Λ²V) = 1`.**

`rank(Λ²V) = 1` is `C(N,2) = 1` is `N = 2` — `exteriorSquareDim_eq_one_iff`,
already proved. So the corpus's own gloss on "non-degenerate" *is* the strong
reading, and the two-row table in the previous section is not a choice between
two readings the author might have meant: row 2 is the one the author defined.

I went looking to make an editorial decision and found it already made. Whoever
picks up item 1 should check the same way before treating a gap as open.

One thing that block's prose **overstates**, recorded so it is not cited as a
second route: *"this alternating condition forces `rank(V) = 2`"*. An
alternating form exists on every even rank; what forces `2` is the next
sentence's `rank(Λ²V) = 1`. Not corrected in the prose — the sentence after it
carries the real condition — but the Lean structure no longer repeats the claim.

### Item 3 — the formalised condition (v) is no longer vacuous

`CategoricalFoundations.lean`, `QuantumObservableUniverse`:

| before | after |
|---|---|
| `exteriorSquare : C` | `exteriorSquare : C` |
| — | `exteriorSquareProj : (fundamentalObj ⊗ fundamentalObj) ⟶ exteriorSquare` |
| — | `exteriorSquare_epi : Epi exteriorSquareProj` |
| `volumeForm : exteriorSquare ⟶ (𝟙_ C)` | `volumeIso : exteriorSquare ≅ (𝟙_ C)` |

Same defect and same repair as `adjointObj` under `qou-fav8`, which is cited in
the new docstring. Three sorry-free consequences, `#print axioms` clean
(`iso_unit_hom_ne_zero` needs only `propext`):

- `iso_unit_hom_ne_zero` — **the vacuity, killed.** `volumeForm := 0` used to
  inhabit condition (v) for *any* `exteriorSquare`, because `QuantumUniverse`
  supplies `Preadditive C`. An iso cannot: `e.inv ≫ e.hom = 𝟙` collapses, so a
  zero volume form forces `End (𝟙_ C)` trivial, and
  `QuantumUniverse.unitEndEquiv : R ≃+* End (𝟙_ C)` carries that to the base
  ring being trivial.
- `epi_of_iso_unit` — an iso is epi, so the weak reading comes free.
- `epi_proj_comp_volume` — `π ≫ ε : V ⊗ V ↠ 𝟙`. This is why the projection
  fields matter: the iso *alone* says `Λ²V ≅ 𝟙` about an object with no stated
  relation to `V`, and `π` alone lets `Λ²V` be any quotient. Together they say
  something about the fundamental object.

**Deliberately no braiding-eigenvalue condition on `π`.** On the `q`-exterior
square the braiding acts by `-q⁻¹`, not `-1`; demanding `β ≫ π = -π` would look
like extra rigour and would silently impose `q = 1`, ruling out the quantum
group the framework is about.

### Two things this does not do, and one it costs

1. **No categorical → numeric bridge.** Getting from `volumeIso` to
   `exteriorSquareDim N = 1` needs the fibre functor to be monoidal *and* to
   send `exteriorSquare` to `Λ²(τ V)`. `QuantumUniverse.fibreFunctor` is a plain
   `Functor C (Type*)`, so neither is available.
   `markovWeights_eq_jones_of_volume_constraint` still takes `hvol` as a
   hypothesis on a natural number. **The forcing chain is not shorter than it
   was** — what changed is that its top link is now a non-vacuous axiom.
2. **Item 1 is untouched.** `MassTraceIsFibreCategorical` is still the open
   premise.
3. **The cost: a higher bar for a witness.** There is no
   `QuantumObservableUniverse` instance anywhere in the tree — 50 files mention
   it, always as a hypothesis — and `WitnessObstruction.lean` already rules out
   module categories. Strengthening condition (v) cannot break an instance,
   because there is none; it does make one harder to build. Named as a cost
   rather than buried.

### Downstream consequence worth reading twice

`su2-emergence.lean`'s `RankOneGaugeData` carries a scope warning saying only
one of its three fields constrains the QOU — `volume_nondeg`. That field is now
**derivable** from `volumeIso` and carries a default value, so `RankOneGaugeData`
adds *nothing* to `QuantumObservableUniverse`. The content did not evaporate; it
moved upstream into the framework axiom, which is where the corpus states it.
But the scope warning now understates the situation and has been amended in
place: "none of the three, because the axiom already does".

### Two incidental findings, both from the same cause

Co-located `.lean` siblings are outside `globs = ["QOU", "QOU.+"]` in
`lean/lakefile.toml`, so `lake build` never sees them, and they have no
`.qa.json` compile gate either.

1. **`qou-exists-axiom-4.lean` did not compile on `main`** — two
   `unknown universe level 'v'` errors under the build's own
   `-DautoImplicit=false`, from `QuantumObservableUniverse.{u, v}` with no
   `universe` command. Verified against a stashed tree. Fixed here (one line).
   Its `exists_axiom_4_volume` also proved `Nonempty (Q.exteriorSquare ⟶ 𝟙)` by
   exhibiting `Q.volumeForm` — a satisfiability proof worth nothing, since the
   Hom-set contains `0`. Now states `Epi`, which is what Axiom 4 claims.
2. **`quantum-observable-universes/quantum-observable-universe.lean` is a second
   definition of `QuantumObservableUniverse`**, not a stub that imports the
   library one — and its field set had **diverged**: it carried a
   `volumeForm_epi` field the library structure never had. Because a co-located
   sibling wins candidate 1 of `lean.ref` resolution, every checker on
   `def:quantum-observable-universe` has been auditing the duplicate. Kept in
   sync here; the duplication itself is not fixed and deserves its own bean.

All four touched siblings now compile clean under `-DautoImplicit=false`
(`quantum-observable-universe`, `qou-exists-axiom-4`, `su2-emergence`,
`volume-from-rigidity`); one of them was red before. Library: `check-base-ring`
PASS, `check-wall-side` PASS, `run-validate` unchanged at 51 issues (no issue
added or removed).
