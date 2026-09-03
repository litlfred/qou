# Coordination ledger — SM 26-parameter chip-away (2026-08-02)

**Goal.** Chip at the 26 Standard-Model parameters from the QOU categorical
model: identify which are fundamental observables vs. derived renderings, and
attack the tractable open fronts under strict derive-then-check / anti-fit
discipline. Owner-driven session; feeds the QOU→SM derivation queue (#4600,
bean `qou-jsx5`).

**Governing insight (the reframing, PR #4602).** The 26 are a *downstream
rendering* of the categorical action under archimedean evaluation
(cat action → q-CLT → archimedean → observables → rendered SM params). All
torus-knot *carriers* are Vol=0 (#4589), and confined-quark "masses" are not
direct observables — they are scheme-dependent Lagrangian parameters extracted
from color-singlet bound states. So ~14 of the "21 open" (6 quark masses + 8
mixings) are **derived quantities of the observable spectrum**, not independent
open knots.

## PR cluster (this session)

| PR | Front | Result | Copilot |
|----|-------|--------|---------|
| #4602 | reframing | observable-vs-rendering reclassification of the 26 | — |
| #4589 | m_ν + map | carrier≠mass-knot (all torus carriers Vol=0); neutrino volume-density scope-(b) excluded (~10¹⁰ gap) | — |
| #4584 | m_c scaffold | complex-mass constituent functional (primary conjecture, open); 3 charm negatives (tower scope-a, carrier scope-b, composite volume) | — |
| #4594 | m_c projection | Frobenius charm-block ratio O(1) vs O(100) hierarchy — scope-(a) negative | ✅ resolved |
| #4591 | m_τ | complex-volume (Vol+i·CS) search — sharpened negative (entropy 14.5 bits forbids census ID; torus carrier; CS-blind muon anchor) | ✅ resolved |
| #4597 | sin²θ_W / Y | **advance:** Milnor triple linking μ̄₁₂₃ = the writhe-independent 2nd invariant; separates the two U(1)s; Y=B on non-strange; Lean sorry-free | ✅ resolved |
| #4596 | θ_QCD | bar-symmetry ⟹ θ∈{0,π} proved sorry-free (modest anchor); CP-evenness → open SU(3); smallness open | ✅ resolved |
| #4582 | charm knot | charm/bottom column-swap fix + gg→cc̄ colour-threading reconciliation (T(3,5)=production vertex, not weak mediator; W=T(2,4)) | — |
| #4562 | EW even-tower | boson tower uniformly harmonic (continuant divisibility) | ✅ resolved |
| #4579 | reverse divisibility | b_a∣b_n ⟺ a∣n sorry-free (generation windings = odd primes, whole tower) | (DRY note: morganVoyceB now on main) |
| #4565 | generation bridge | general Fibonacci-poly harmonic law + honest quark-H₃ negative | — |
| #4564 | SU(3) | Hecke-centralizer obstruction on regular H₃ (dim 6<8 exclusion), sorry-free | — |

| #4608 | J/ψ observable | **mechanism-applicable + sharpened negative:** the J/ψ scale IS in-range (Vol≈24 hyperbolic braids → ≈3097 MeV) — distinguishes J/ψ (applicable) from ν (scope-(b) excluded). But NO derived braid: the canonical meson flux-tube operation is undefined (bean `qou-qpj9`); J/ψ vs η_c want different-topology braids (per-state-fit signature); dense spectrum (entropy). | — |

## Scorecard (honest)

- **Parameter tiers moved: 0.** Canonical L2 count: **1/5 scoreable** (`m_K/m_π` only), **0/5 unconditional** — the earlier "2/7" counted the calibration inputs `m_e`, `m_p` (AGENTS.md, corrected 2026-08-18/22; this line read "stays 2/7" until 2026-09-03); the 26-param split
  stays 1 input / 1 proxy / 1 partial / 2 conjectural / 21 open **by the SM's
  accounting** — but the reframing re-scopes ~14 of the 21 as *derived*.
- **One genuine structural advance:** μ̄₁₂₃ separating the two U(1)s (#4597) — the
  most tractable lever toward sin²θ_W.
- **One conceptual correction:** observable-vs-rendering (#4602) — explains why
  the four charm-mass attacks were category errors (targeting a non-observable).
- **A stack of honest negatives** pruning dead routes (charm tower/carrier/
  composite/projection; m_τ census; neutrino volume; θ_QCD ceiling at {0,π}).
- **Zero fabricated numbers.**


## Session log

| Date | Agent / branch | Intent | Results |
|---|---|---|---|
| 2026-09-03 | Claude / `claude/standard-model-terms-status-ftoejr` (session `qou-ggdk`) | INTENT: term-by-term status of the 26 against the live corpus; refresh this ledger + the cheat sheet; fix the in-paper 4-C contradiction; Lean best-practices sweep on the SM surface; one roasted bean per open term | RESULTS: see the 2026-09-03 section at the end of this file and `docs/audits/2026-09-03-sm-26-term-status.md`. |
| 2026-08-04 | Copilot / `copilot/eight-fold` | INTENT: external electron.pdf triage + drain nearby electron arc beans in SM/eight-fold scope | RESULTS: network fetch to physicsdetective blocked; corrected electron-arc prose to keep knot identification but remove standalone trefoil-mass overclaim, and aligned the example with CAL-1 framing. |

## Open fronts (beans / follow-ups)

1. **Canonical meson flux-tube operation** (bean `qou-qpj9`, #4608) — the J/ψ
   attack confirmed the observable is *in mechanism range* but is blocked on a
   *derived* c̄c-binding braid. **Resolved to an honest negative + the precise
   missing datum (#4614, bean `qou-mesont3`):** the Y-junction 3→2 reduction
   gives B₂ (abelian) → torus link → Vol=0 (scope-(b), SnapPy-verified) — strand
   *removal* can't build hyperbolic structure (the framework already puts the
   meson at H₃(q), Hopf-binding = 3rd strand). And the operator-selection input
   is under-determined because **`windingContent` is non-injective** (Lean-proved):
   charm (n=5) and strange (n=5) share the generation-2 block — the D-meson
   `{5,3}` collides with the kaon `{3,5}` (same multiset). The missing object is a
   **weak-isospin T₃ grading orthogonal to the winding n** (up-type charm vs
   down-type strange). Bonus: a live corpus inconsistency — charm assigned both
   T(2,5) and T(2,7) across tables (canonical-watcher).

**★ CONVERGENCE (the headline).** The charm-mass gate (`qou-mesont3`: a
weak-isospin T₃ distinguishing up/down-type at fixed generation) is **the same
missing object** as the electroweak-mixing gate. #4597 gave the writhe-independent
2nd invariant μ̄₁₂₃ = Y; the writhe→I₃ map (G2 #4561) is the T₃; and the
up/down-type distinction the D-meson needs IS weak isospin. So the charmed-hadron
observable spectrum, sin²θ_W, and hypercharge Y all block on **one** object: a
weak-isospin T₃ grading orthogonal to the generation winding. That is now the
single highest-leverage target — it unlocks three fronts at once.

**★★ UPDATE — T₃ DERIVED (partial), #4618 (`qou-tdrd`).** The signed writhe factors
canonically: `κ = sign(κ)·|κ| = T₃ × generation-winding`, so **T₃ = sign(κ)/2 ∈
{±½}** is the *sign-half of the very integer whose magnitude the framework already
reads as the generation* — orthogonal by construction, derived from the oriented
crossing already in the corpus (not a second postulate). Sorry-free Lean (exit 0,
axioms clean): **charm ≠ strange** (both n=5, opposite T₃) resolves the meson
degeneracy, and **GMN `Q = T₃ + Y/2` closes** — a real derive-then-check (a wrong sign or a
wrong ½ breaks it). **State its width, though:** quantified over six quarks it
collapses to **two** distinct rows, since `Y` is constant and `Q`, `T₃` both
depend only on the up/down-type bit. One sign correlation plus one
normalisation, checked twice — now machine-checked as such
(`gmn_check_has_two_distinct_rows`, `genWinding_finer_than_gmn_data`), so the
"all six quarks" phrasing cannot be read as six confirmations. Honest remainder
(conjecture class, no instance): up=positive is *inherited* from the ⋈_K strong-
isospin datum (consistent, not *forced*), and the SU(2)_L gauge/CKM lift is open —
both reduce to the open SU(3)-flavour sector. So: a real orthogonal ℤ/2 passing GMN,
NOT yet *the* gauged weak isospin. Chiral-EFT lit for the binding-side template in
`library/` (owner: 1011.1343, 1906.12122, s00601-2022).

**★★★ UPDATE — the two follow-on tests (both landed, both honest negatives that sharpen):**
- **`qou-buxs` (T₃ vs Δ_λ sign), #4623 — DERIVED negative.** The literal T₃ = sign(net
  writhe) is the WRONG sign *statistic*: matches 3/3 at n=3 but 8/11 at n=6 (fails the
  height-4/5 columns). The chiral-EFT template (HKvK p.12: isospin sign = exchange
  symmetry of the isospin wavefunction) *derives* the correct statistic = crossing-**count**
  parity `(−1)^C(c,2)`, which **is** `sgn(w₀^{S_λ'})` restated (not new info from T₃). So T₃
  locates *where* the sign lives (the antisymmetrizer crossings — what PROBE-4 demanded) but
  is too coarse. Scope-(a): surviving route = a **count-parity** closure, not net-writhe.
- **`qou-2udt` (T₃ into meson op-selection), #4625 — degeneracy RESOLVED, mass still open.**
  Signed-writhe `(n,2T₃)` separates all 6 quarks (sorry-free); charm block distinctly
  selectable from strange on `{π,K,η,D}`. But proved `mass_from_graded_content_cannot_separate`:
  the mass is NOT a function of `(n,T₃)`.

**⇒ The D-meson mass now gates on exactly TWO objects:**
1. **Third flavour grade — SU(3)/SU(4)-flavour Cartan** (`qou-dnm1`): `(n,T₃)` still collides
   D̄⁰{c̄,u} with K⁰{d̄,s} (same multiset); needs strangeness S / charm C. This is the
   **flavour** SU(3) eightfold-way (global) — DISTINCT from the excluded **colour** SU(3)
   (#4564, gauge). Owned partly by #4600 (`qou-d7h1`).
2. **Flux-tube braid word** (`qou-qpj9`): the hyperbolic braid giving the mass; `(n,T₃,flavour)`
   only pins the Vol=0 carrier.

2. **Generation physical bridge** — the *counting* (3 = odd primes in the
   Bring-genus window N(χ=−6)=9, {3,5,7}; 9 harmonic) is clean given the
   identifications; the *physical bridge* (why prime-winding = a fermion
   generation; why harmonic knots add none) stays open (G1: no rigorous
   argument). Blocks the 8 mixings.
3. **SU(3) colour sector** — only a negative (#4564); blocks α_s, θ_QCD-smallness,
   Y=B+S strangeness extension of #4597.
4. **sin²θ_W normalization** — #4597 separated the U(1)s but the relative U(1)
   coupling normalization inherits open SU(3)-flavour.

## Anti-fit discipline (held throughout)
Every "closest hit" was gated against search-space entropy; every scaffold is a
content-bearing conjecture with **no instance** (open); no anchor-inversion was
wired as canonical; negatives are scope-tagged (a)/(b) with cited invariants.

---

## 2026-08-25 — 4-B (two-like-charge EM-linking): the kernel is not identified

PR [#5770](https://github.com/litlfred/qou/pull/5770), bean `qou-17mq`. Two
findings, both negative, both scope-tagged. **The route is untouched; what is
gone is the belief that its kernel has been selected.**

4-B gates `m_d − m_u` — the one honestly extractable quark quantity — and is
rank 1 in the cheat sheet's near-term table because it needs no `SU(3)`.
(**Corrected 2026-09-03.** This sentence read *"and 69 % of the ³He mirror
residual"* — the figure is unsourced, and the single-nucleon self-energy
channel cancels identically in a binding difference; the cheat sheet's 2026-08-25
§4-B box records the withdrawal but this line was missed, and the cheat sheet's
own claim that the figure survives "in no ledger" was therefore wrong. The
2026-08-30 channel split in `qou-bn8e` — self channel does *not* merge, pairwise
channel *does* — is recorded in the 2026-09-03 section below.)

1. **The contest's winner is not an admissible kernel.** `H_coth` is scored on
   an *unsubtracted* `coth(α)`, which the round-2 **O2** obstruction excludes:
   on a finite-volume quotient the admissible kernel has zero mean, hence takes
   both signs, so none saturates at `κ → +1` — and saturation is what separated
   `H_coth` from its rivals. O2 had been recorded 2026-08-01 and applied to
   nothing (four mentions corpus-wide, all in one file, zero in
   `computations/`). Re-scored, scatter rises monotonically with neutralisation
   (3.505 % → 11.15 % → 22.32 %) and the best admissible member carries residual
   structure `r = −0.904`, more than the `r = +0.799` that got `H_FH_Z`
   rejected for carrying structure. Scope: **(b)** on the kernel as written,
   invariant cited (`∫Δu = 0`); **(a)** on the parameterisation.
2. **The test could not have discriminated.** The series spans
   `α ∈ [0.317, 0.873]`; `coth` reaches within 10 % of its limit only at
   `α = 1.522`, i.e. **`A = 334`** — past the heaviest known nuclide (294). Over
   the measured range `coth` is within 0.97 % of `1/α + α/3` against 3.505 %
   scatter, so its advantage tracks the curvature term, not saturation; and the
   two hypotheses differ by at most 1.79 × that scatter. Scope: **(a)** on a
   *test*, not on a hypothesis.

**Consequence for the ledger.** With round 5's withdrawal of the two `H_FH`
warrants, no member of that contest carried a live structural warrant when it
was scored. `qou-i6rg` is `completed` and its ranking has been read as a
settled selection; it is not one, and its own premise — *"needs NO new theory,
only more AME data"* — is wrong, since more data cannot reach `A = 334`.

**Next on 4-B changes.** Not "extend the series". Either derive the kernel
(zero-mean Green's function of an actual finite-volume quotient, *predicting*
`κ(A)` instead of scoring parameterisations against it), or find an observable
probing `α ≳ 1.5`, which no nucleus supplies under `α ∝ A^{1/3}`.

Recorded independently: on `H³` the decaying Green's function is
`−(coth r − 1)/4π`, so the subtraction O2 forces is also just the ordinary
boundary condition — a route needing neither compactness nor finite volume.

**Carried confound** (`qou-gcmn`): `B_pp` frozen at its `A = 3` value bounds
every scatter number above. Neither structural argument depends on it.

3. **The separation law is an unexamined Euclidean import.** Upstream of both
   findings above: every kernel on this front is fed `α ∝ A^{1/3}`, the
   Euclidean liquid-drop nuclear radius, imported as *"fixed in advance as the
   standard nuclear radius law"* — which guards against post-hoc selection but
   is not derivation. The kernel it feeds is hyperbolic by construction. Using
   the geometry consistently (`H³`: `R ~ ½ ln V`, so `α ∝ ln A` for extensive
   `V`) scores **9.253 %** against the import's **3.505 %** — consistency costs
   **2.64×**. The corpus cannot adjudicate: `binding-link-volumes` holds
   volumes at `A = 2, 3` only and says so. A free-power diagnostic lands at
   `p = 0.33`, indistinguishable from `1/3`, so the data independently prefers
   the Euclidean exponent. **Deflationary reading:** `κ(A)` is close to plain
   Coulomb in a Euclidean nucleus (`5.499 %` for pure `1/r`), the hyperbolic
   curvature term buying a factor `1.57` on one shared parameter — real, but
   suggestive rather than decisive and comparable to the `qou-gcmn` confound.
   Scope: **(a)** on an input assumption. Not claimed: that `A^{1/3}` is wrong
   (the data prefers it), that the geometry is Euclidean, or that `H_coth` is
   refuted.

**Net for the ledger.** 4-B carries **three** distinct gaps where the front had
been carrying one: the route is identified, the kernel is not, and the
separation law is imported. None of the three refutes the metric Coulomb
pairing. What they remove is the impression that a kernel had been selected,
that more data would settle it, and that the hyperbolic reading was
load-bearing for the fit.


---

## 2026-08-25 — 4-C retitled: no third flavour grade is missing

PR [#5770](https://github.com/litlfred/qou/pull/5770), bean `qou-17mq`.
**Corrects the "D-meson mass gates on exactly TWO objects" entry above: object 1
is void.**

`orderedContent_injective` is proved sorry-free (`by decide`) on `main`:
`D̄⁰ (−5,+3)` and `K⁰ (+3,−5)` collide **only as multisets**, and the ordering is
the quark/antiquark strand orientation — the same `signedWrithe` that gives
`T₃`, *"topological strand-orientation data, not a fit"*.

The arity slip: `mass_from_graded_content_cannot_separate` quantifies over
`f : Multiset ℤ → ℚ` — **symmetric** functions of the *unordered* content. It
does not say the content cannot carry the mass. The ordered complement is
injective. Fourth recorded instance of `da-arity-conflation`.

**Consequence for the ranking: 4-C does not reduce into 4-A.** That dependency
placed the rank-2 near-term object behind the `N = 3` problem, the framework's
hardest open question. It is not there. What remains is object 2 of the entry
above — `qou-qpj9`'s canonical content → hyperbolic-braid map — which needs no
`SU(3)`, flavour or colour.

**Not thereby solved.** Injectivity gives a factorisation, never a derivation of
the factorising map. Fitting through five injectively-labelled points is the
per-state fit the J/ψ attack already recorded as worthless.

Bean `qou-dnm1` (`todo`) carries the void framing and four attack options for
the absent grade; body appended, **status left for the author**. A prior agent
reached this on `qou-mesont3` and it never propagated here — re-verified at
source rather than taken from that bean.

---

## 2026-09-03 — currency refresh (session `qou-ggdk`, branch `claude/standard-model-terms-status-ftoejr`)

This ledger recorded nothing after 2026-08-25. What landed 2026-08-26 → 09-03 on
the SM surface, each verified at source this session (audit:
`docs/audits/2026-09-03-sm-26-term-status.md`). **Parameter tiers moved: 0** —
all eight `sm-params-*` blocks are byte-identical to their QA sidecars.

- **4-A (N = 3).** Five sorry-free Lean files (2026-08-26, PRs #5810/#5819):
  `Sym2GateFSTrichotomy` (real and quaternionic constructions excluded *as a
  class* at dim 3), `SelfDualSectorConfinement` (the required property is
  **non-self-duality**, now a pre-Sym² screening test), `OctonionicSu3RankObstruction`
  (the λ_a ↔ e_a generator-identification route is an **eighth** scope-(b)
  exclusion), `TrialitySelectionRule`, `FlavourColourDiscriminator` (**no
  object-level gate separates colour from flavour** — item 4's "cannot both come
  from one construction" is withdrawn in-paper). The T3g carrier `qou-y7vg` is
  stalled at step 1: naming the base is a decision (three candidates, two sharing
  the symbol `R_q`), and both prose carriers of its premise have no formal content
  (`CategoricalMordellWeil := trivial`). Eightfold half of this surface now lives
  in `docs/coordination/eightfold-n3-surface.md`.
- **4-B (intra-nucleon EM self-energy).** The 2026-08-25 "cannot be the same
  object as the mirror front" is **partially reversed** by channel (`qou-bn8e`,
  2026-08-30, merged into `qou-o6ml`): the self channel `A·Σqᵢ²` does not merge
  (cancels in binding), the pairwise channel `B·Σqᵢqⱼ` does. Derived ratio on
  record: `h/[2]_q = tanh(ln q₀) = 0.10396371…` — what 4-B owes is the bond that
  multiplies it. `ChargeQuadraticSumRule.lean` (sorry-free): the quadratic-charge
  ansatz **saturates the octet** (bijection, det −1/3), so Coleman–Glashow could
  not have failed; the same-branch "CG falls out parameter-free" claim was
  retracted (`docs/audits/2026-08-29-coleman-glashow-retraction-and-octet-saturation.md`).
- **4-C.** The in-paper `sm-gating-objects.md` (PR #5744, 2026-08-30) restated
  the struck "third flavour grade reduces into 4-A" claim five days after #5770
  struck it with `orderedContent_injective`. Fixed on this branch.
- **α_EM.** Three rival constructions circulate: the form ladder the appendix
  states (0.313 ppb cubic / 1.672 ppb quadratic at proton), the Chern–Simons
  `.md` form the L2 dashboard actually consumes (−467.6 ppb, κ conjectural), and
  the CS `.lean` (+2.59 ppb, κ = 8q, PSLQ-ruled-out per `qou-aymm`) — the block's
  `.md` and `.lean` disagree by 470 ppb (`qou-aemx`, in-progress, high). The
  quoted muon figure 80.51 ppb is at the **retired** pin A; at the live
  CODATA-2022 anchor it is 81.04 ppb (verdicts unchanged). Both ladder producers
  hardcode q₀ literals (no `q_parameter` import) and are invisible to three
  anchor detectors. The EM holonomy germ is **LIVE** (non-sterile,
  `docs/audits/2026-08-29-alpha-em-germ-viability-live.md`) — necessary, not
  sufficient; `1/(8π)` stays phase-4 owner-gated.
- **sin²θ_W.** `weinberg-angle-categorical.md` prints `cot θ_W ≈ 0.6594`;
  `q₀⁻⁴ = 0.65878` — a wrong digit, not an anchor artefact (the appendix prints
  0.659 correctly). The 0.127 % compute (`close_321_weinberg_gap.py`) is float64
  end to end (sympy → `np.complex128` → `eigvals`, 127 raw-float64 fields) under
  a witness declaring `compute_dps: 70`; verdict `inconclusive` unaffected. Its
  Lean carrier `weinberg-angle-categorical.lean` is a **vacuous** class (four
  `def … : Prop := True` + a global `trivial` instance), duplicated in
  `categorical-higgs-mechanism.lean`, absent from the vacuity ledger. A **third**
  circulating number, `1 − ([10]_q/[11]_q)² = 0.22998` (0.369 % off), lives only
  in `docs/beta-decay-handoff.md`.
- **α_s.** "No candidate formula" is stale as worded: `1/α_s = q^p[9]_q` exists
  in `computations/alpha_k_selection_rule_conditional.py` (bracket writhe-forced,
  `p` an undetermined 1-parameter family, only `α_s·α_W = α_EM` invariant,
  conditional, scale-free), and a fit-shaped `α_s(M_Z) = q⁻¹/[7]_q ≈ 0.1181`
  sits in `docs/beta-decay-handoff.md` — the exact thing `qou-5iaz` forbids
  wiring. Neither is a derivation; the tier stays open.
- **GMO deviation** is provably under-determined (`GellMannOkuboSecondOrder.lean`:
  two equations, three unknowns, `g` absorbable) — cheat-sheet rank 3 drops
  (`qou-s4h6`). **Quark charges** ±2/3, ∓1/3 are asserted, not derived; the braid
  element as carrier is scope-(b) closed (`QuarkBraidChargeObstruction.lean`,
  `qou-a468`). **`generation-completeness.lean`** is vacuous (`qou-0avp`).
- **Tower vs order zero (owner question).** Every SM-facing result is a
  leading-order or single-crossing statement; the eightfold results are
  first-order octet breaking with the second order under-determined; the
  central obstruction (`dim V = 2`) is invariant along the single-fibre tower,
  and `su5-hypercharge-n3-gate.md` proves Wenzl levels are alternatives, not
  stages. There is no all-orders SM derivation.
- **🟧 Owner ruling (2026-09-03, verbatim):** *"The QOU should be on the full tower
  in the derivations to the standard model — should make use of the full tower even
  though what is observable is only order zero."* Every attack front in this ledger
  is to be re-read against it: an order-zero-only construction is structurally
  incomplete regardless of residual; per-term beans (`qou-bsu0`) carry a tower-status
  line. The owner confirmed the same day that "full tower" means both — all `n`
  and all orders in `q`; recorded in the audit above.

