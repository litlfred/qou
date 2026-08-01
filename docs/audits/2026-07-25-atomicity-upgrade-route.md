# Atomicity upgrade route — jet-order independence (route 1 closed negative), Tannakian route scoped

**Date:** 2026-07-25 · **Bean:** qou-ngwo · **Tier:** formalization audit —
scope-(b) structural exclusion with Lean-cited invariant, NO FIT, nothing
wired, no instance created.

**Lean:** [`QOU/AlgebraicSubstrate/AtomicityJetIndependence.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/AtomicityJetIndependence.lean)
— verified `lean`-direct, **exit 0, sorry-free** (olean-cache path,
`-D autoImplicit=false`; the dependency `PlanckStepAtomicity.olean` compiled
`lean`-direct first, also exit 0).

## 1. Mission

The atomicity audit
([`2026-07-25-planck-step-atomicity-formalization.md`](2026-07-25-planck-step-atomicity-formalization.md)
§3/§6) left `PlanckStepAtomicity` as a §3b-tax primary conjecture (PREMISE)
and named two upgrade routes to THEOREM:

1. derive rank-one-ness of the substrate computation monoid from the
   jet-tower ordering structure
   ([`prop:ordering-jet-compatibility`](../../content/quantum-observable-universe/lifting-and-descent/ordering-jet-compatibility.md));
2. a Tannakian `FibreFunctorRigidity`-style reconstruction
   ([`QGeometricLanglands.lean`](../../content/quantum-observable-universe/lean/QOU/QGeometricLanglands.lean)).

This tranche runs the decisive test for route 1 and scopes route 2.

**Verdict: INDEPENDENT.** The jet-compatibility axiom set neither proves nor
refutes atomicity — Lean-witnessed both ways
(`planckStepAtomicity_independent_of_jet_order`). Route 1 closes honestly
negative; route 2 is blocked with a named missing input whose content
contains atomicity itself (§4). `PlanckStepAtomicity` stays a primary
conjecture, now with a proved certificate that it is genuinely NEW content
beyond the jet-tower ordering — which *strengthens* the conjecture-class
representation.

## 2. Axiom inventory of `prop:ordering-jet-compatibility`

Block Lean:
[`ordering-jet-compatibility.lean`](../../content/quantum-observable-universe/lifting-and-descent/ordering-jet-compatibility.lean)
(namespace `QOU.Torsion`, carrier `MonomialBasis := List ℕ` with the
degree-lex order `degLex`). What each leg EXACTLY asserts, as formalized:

| Leg | Declaration | Kind | Formal content |
|---|---|---|---|
| 1 Extension | `ordering_extends (k a b) (hab : degLex a b) : degLex a b` | `axiom` | **Tautological as formalized** — the conclusion is literally the hypothesis. The intended content (the prolongation $\ell_n$ preserves the ordering) is representable only because all levels share ONE global `degLex`; the axiom adds zero deductive content. |
| 2 Compatibility | `ordering_compatible (a b c d) : degLex a b → degLex (c ++ a ++ d) (c ++ b ++ d)` | `axiom` | Two-sided translation invariance of `degLex` under concatenation. A genuine statement — and in fact TRUE of `degLex` (degree adds; equal-length lex is stable under a common prefix/suffix), i.e. provable rather than axiom-worthy. Not discharged this tranche (the block file is merged; out of scope). |
| 3 Well-foundedness | `wellfounded_at_level` / `degLex_wellFounded` | `theorem` | Proved (the one proved leg). |
| 4 Direct limit | `direct_limit_terminates (n w hw) : ∃ w', ¬ degLex w' w` | `axiom` | As stated, **implied by irreflexivity alone** (`w' := w`; `degLex` is irreflexive since it is well-founded) — near-zero content as formalized. |

Three findings decisive for route 1:

1. **No rank statement anywhere.** None of the legs asserts totality,
   cofinality of a single generator's iterates, one-dimensionality, or any
   rank-one property. Order-theoretically the axioms are: one global
   well-founded translation-invariant relation + an exhaustive increasing
   submonoid filtration.
2. **Type-level gap.** The axioms constrain the fixed monomial carrier
   `List ℕ` and mention no abstract computation monoid; there is no Lean
   bridge from `QOU.Torsion` order structure to the `SubstrateClock` monoid
   `M`. Route 1 therefore needs an abstract extraction before it can even be
   posed (built this tranche: `JetCompatibleOrder`, §3).
3. **The axioms' own carrier is maximally non-atomic.** `List ℕ` under `++`
   is the free monoid on countably many generators — rank $\omega$. The jet
   story itself ADDS generators at each level (`numNewDirs = 3` per
   prolongation in the block's `JetExtension`). If anything, the jet-tower
   ordering structure suggests rank growth, not rank one.

## 3. The decisive test — Lean outcome

**Extraction.** `JetCompatibleOrder M` (structure, §7c-generic
`[AddCommMonoid M]`) carries the strongest structural reading of the four
legs: global ordering `lt`, jet filtration `level` (submonoid closure +
monotone + exhaustive), translation invariance `compat`, well-foundedness
`wf`. The mirrors of all four corpus legs are *derived* from it (`ltAt_extends`,
`ltAt_wellFounded`, `terminates`), confirming the extraction is not weaker
than the block's axiom set.

**Rank-2 model.** `rankTwoJetOrder : JetCompatibleOrder (ℕ × ℕ)` — order
`degLexPair` (total degree first, then the jet coordinate: the exact
`degLex` analogue), filtration in which `(0,1)` is the level-1
jet-prolongation direction, ordered after `(1,0)` exactly as the prose
orders new $\Omega^1$ directions after old generators. Every field proved,
sorry-free. Combined with the already-merged
`atomicity_fails_for_two_generators` (`ℕ × ℕ` has no single generating
step):

| Theorem | Statement | Status |
|---|---|---|
| `planckStepAtomicity_not_forced_by_jet_order` | no theorem `JetCompatibleOrder M → atomicity of M` (refuted at `M = ℕ × ℕ`) | **proved, unconditional** |
| `rankOneJetOrder` + `nat_is_atomic` | `ℕ` carries a jet-compatible order AND is atomic (raw existential — deliberately NOT a `PlanckStepAtomicity` instance; the class's instance count stays 0) | **proved** |
| `planckStepAtomicity_independent_of_jet_order` | both directions: the axiom set neither proves nor refutes atomicity | **proved, unconditional** |

**Strengthenings also fail.** The SAME rank-2 model additionally satisfies
(`jet_order_strengthenings_still_insufficient`, one packaged statement):

- totality (`degLexPair_trichotomy`) — so upgrading "admissible ordering"
  to "total translation-invariant well-order" cannot force rank one;
- existence of a genuine least nonzero "Planck step" (`e1_least_nonzero`:
  `(1,0)` is the least nonzero element);
- cofinality of that step's iterates (`e1_iterates_cofinal`: every element
  is below some `n • (1,0)`).

So no order-theoretic strengthening along these natural axes can close
route 1. What atomicity adds beyond ANY such ordering axiom is precisely
the `generates` clause — every segment **is** an iterate of the step, not
merely comparable to iterates. A jet-tower formalization strong enough to
imply that clause would have to carry it as an assumption, i.e. assume the
conclusion.

**Refutation scope (per §Before declaring "refuted").** This is a
**(b) structural exclusion** with the invariant cited: the Lean-proved
counterexample model (`rankTwoJetOrder` satisfying every axiom leg +
`atomicity_fails_for_two_generators`). It excludes the *implication*
"current jet-compatibility axiom set ⇒ atomicity" — it does NOT exclude
atomicity itself (which stays open, primary conjecture), and it does not
exclude a future jet-tower formalization with genuinely new content
(but §2 finding 3 and the strengthening theorem bound what such content
would have to be: the `generates` clause itself, or something implying it).

## 4. Route 2 scoping — Tannakian `FibreFunctorRigidity` reconstruction

`FibreFunctorRigidity` as formalized
([`QGeometricLanglands.lean`](../../content/quantum-observable-universe/lean/QOU/QGeometricLanglands.lean)
§7) is one field:

- `eigenvalue_unique` — two `QLocalSystem`s with the same substrate and the
  same holonomy residues at every point are equal.

That is a separation/injectivity statement about **objects** (q-local
systems). It constrains which local systems exist; it says nothing about
the **monoid of natural endomorphisms** of the fibre functor $\tau$ — the
object a Tannakian derivation of clock rank would have to control. A
genuine route-2 derivation would need, named precisely:

1. **A Tannakian reconstruction carrier** — `End(τ)` (or
   $\mathrm{Aut}^{\otimes}(\tau)$) as a Lean monoid object, plus the
   reconstruction statement identifying the substrate's computation monoid
   with (a submonoid of) it. Not in Mathlib, not in the corpus; the corpus
   has no Lean object for $\tau$'s endomorphism monoid at all.
2. **The Reeb iteration as an ℕ-action on τ** — a distinguished natural
   transformation $R$ (one Reeb circuit) with computation segments
   identified as its orbit. The corpus's Reeb-flow Lean
   (`ReebEpsilon.lean` etc.) carries no action on a fibre functor.
3. **Orbit exhaustion** — a proof that every computation segment lies in
   the $R$-orbit (the image of the ℕ-action exhausts `M`). **This is
   verbatim the `generates` clause of `PlanckStepAtomicity`.**

So route 2, with any presently-nameable corpus structure, is *circular for
this purpose*: Tannakian rigidity can **transport** atomicity (once the
monoid is known to be one Reeb orbit, rigidity pins the clock uniquely —
which is SCU, already discharged *by* atomicity), but it cannot **create**
the single-orbit structure. Verdict: route 2 = blocked-with-named-input,
and the named input (item 3) contains the conjecture itself. Items 1–2 are
still worth building for other reasons (they would make the conjecture
*statable* categorically instead of monoid-abstractly), but they do not by
themselves upgrade the tier.

## 5. What WOULD settle the upgrade question

- **Positively:** a corpus derivation of the `generates` clause from
  non-order-theoretic structure — e.g. a categorical statement that the
  substrate's dynamics is the iteration of a single endofunctor application
  (one Reeb circuit as the unique connected generator of the flow), from
  which `M` = its orbit monoid falls out. That is new structure, not
  currently formalized anywhere (§4 items 1–2 are the prerequisite
  carriers).
- **Negatively (refuting atomicity):** exhibiting two computationally
  independent step directions in the substrate — e.g. a Lean-carried
  construction of two Reeb circuits whose counts cannot be merged into one
  ℕ-chart. Nothing in the corpus suggests this either.
- Until one of these lands, the honest state is exactly the current one:
  `PlanckStepAtomicity` = content-bearing primary conjecture class, no
  instance, with this tranche's independence certificate documenting that
  the jet-tower ordering axioms cannot decide it.

## 6. Scope discipline + render-QA

- **NO FIT; nothing wired; no instance created.** `PlanckStepAtomicity`'s
  instance count remains zero (`nat_is_atomic` is a raw existential by
  design). No content blocks touched; no witnesses, dashboards, or compute
  touched. `BalancedMomentConfluence` / balanced-moment files untouched
  (parallel-agent scope respected). The merged
  `ordering-jet-compatibility.lean` block file untouched (its provable
  axiom legs, §2, recorded here as a follow-up, not edited).
- **Lean verification:** `lean`-direct per
  [`lean-environment-setup.md` §lean-direct](../../.claude/skills/local/lean-environment-setup.md):
  `PlanckStepAtomicity.olean` compiled first (exit 0), then
  `AtomicityJetIndependence.lean` exit 0, sorry-free, `-D autoImplicit=false`.
  §7c pass: no `Real.*`, no archimedean construct; generic
  `[AddCommMonoid M]`; concrete witnesses on `ℕ × ℕ` / `ℕ`.
- **Corpus-grep (STRICT gate):** no prior `JetCompatibleOrder` /
  atomicity-independence work in `docs/`, `content/`, `computations/`
  (sole grep hit is the unrelated block-granularity sense of "atomicity"
  in `2026-06-28-atomic-content-audit-verdicts.json`).
- **Render-QA:** the preflight grep battery was run by hand on this
  document (balanced `$`/`$$`/braces; no `\operatorname`; no list-hijack
  lines inside display math; no inline align-family environments; no
  `$$…$$` used). The pipeline render was not run in this sandbox — stated
  explicitly per the render-QA gate: this document was **not
  machine-validated**.

## 7. Follow-ups (recorded; not done this tranche)

1. **Discharge the two provable axiom legs** of
   `ordering-jet-compatibility.lean`: `ordering_compatible` is a true,
   provable fact about `degLex` (concatenation compatibility);
   `direct_limit_terminates` follows from irreflexivity. Converting both
   `axiom`s to `theorem`s shrinks the block's axiom surface without
   changing its strength. (Does not affect this tranche's verdict: the
   independence witness satisfies the legs whether axiomatized or proved.)
2. **Rewrite `ordering_extends` non-tautologically** — as formalized it
   concludes its own hypothesis; the intended $\ell_n$-preservation
   statement needs an explicit embedding to be non-trivial (the abstract
   `ltAt_extends` shape here is one template).
3. **Aggregator wiring:** `AtomicityJetIndependence` (like
   `SubstrateClockUniqueness` / `PlanckStepAtomicity`) is not yet imported
   by `QOU/AlgebraicSubstrate.lean`; aggregate together once a
   lake-verifiable environment is available.
4. **Route-2 prerequisite carriers** (§4 items 1–2), if/when a Tannakian
   restatement of the conjecture is wanted.

## 8. Cross-references

- Premise formalization: [`2026-07-25-planck-step-atomicity-formalization.md`](2026-07-25-planck-step-atomicity-formalization.md), [`PlanckStepAtomicity.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/PlanckStepAtomicity.lean)
- Reduction chain: [`2026-07-25-substrate-clock-uniqueness-reduction.md`](2026-07-25-substrate-clock-uniqueness-reduction.md), [`SubstrateClockUniqueness.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/SubstrateClockUniqueness.lean)
- Jet ordering block: [`ordering-jet-compatibility.md`](../../content/quantum-observable-universe/lifting-and-descent/ordering-jet-compatibility.md) (+ `.lean`, `-proof.md`)
- Tannakian rigidity: [`QGeometricLanglands.lean`](../../content/quantum-observable-universe/lean/QOU/QGeometricLanglands.lean)
