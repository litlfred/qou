# Physics-claim scope: re-check against main (2026-11-21)

Bean-drain sibling `physics-scope`. Re-checks the 21 beans of epic `qou-ddmn`
(physics-claim scope audits: conformal cyclic cosmology, TQFT, gravity,
cosmology) and epic `qou-3fjn` (perturbative QFT subsumption) against
`main` at `2ae54ab40`. Every finding below was measured on that commit by
grep or by reading the file; none is carried over from a bean unverified.

**Register.** This is a scope audit. It states what each block or Lean
declaration proves, and where a physics word in the prose claims more than
that. It makes no empirical comparison and proposes none. Where a bean
quotes an observed number (η, CODATA, PDG), that number stays in the bean
as context and enters no formal statement.

No content block, Lean file or number is changed by this document. The
edits in §6 are proposals awaiting the owner (AGENTS.md §ASK THE OWNER
BEFORE CHANGING THINGS: they neither raise precision nor follow mechanically
from a corpus artifact).

## 1. Already resolved on main (beans can close with evidence)

| bean | question | evidence on `2ae54ab40` |
|---|---|---|
| `qou-51l1` | Does the introduction say the lifting obstructions *force* χ(A) = −6? | No longer. `introduction/chapter-overview.md:30` now reads "The lifting obstructions reduce to the genus of the base curve: χ_eu(M₀) = 2 − 2g with g ≥ 1, and the Descartes condition fixes g = 4." That is the wording the bean recommended (option 2). A whole-folio grep for "force[sd] the Descartes" returns nothing. |
| `qou-h0ou` | `HasAction.action` is scalar → scalar, so `einsteinTensor` cannot be rank-2. | Retyped. `MathlibExt/MonoidalCalcVar.lean:181-184`: `action : PairingSpace C X Y → R`; `:231` `einsteinTensor : PairingSpace C X Y`; `GaugeTheory.lean:161` likewise. `PairingVariationalDerivative.lean` (the bean's new file) is on main. |
| `qou-plck` (part) | Planck length as a calibration. | Already self-corrected in the bean (2026-09-06): ℓ_P = √q, m_P, t_P are functions of q alone, not calibrations. Open remainder in §3. |
| (from `qou-4khc`) | `massEnergyEquivalence` proved E = E by defining mass as E(q−1)². | Withdrawn 2026-11-15: `information-theory/mass-energy-equivalence.lean` header says the theorem was false with the mass of `def:mass-identity`; energy is now a definition (bean `qou-078y`). |
| (from `qou-ogj5`) | `G` in `α = m_e·8G` read as Newton's constant. | Withdrawn 2026-09-14: `observations/gravity-spectral-prefactor.md` states G is Catalan's constant and 8G = Vol(Borromean complement); the `.lean` header records the withdrawal. |

## 2. Scope findings that still hold on main

### 2a. TQFT (`qou-4khc`)

- No cobordism category, no symmetric monoidal functor out of one, and no
  Atiyah axioms exist as Lean declarations. Measured: no `def` / `structure`
  / `class` / `theorem` whose name contains `Cob` or `Bordism` under
  `lean/QOU/` (the hits for "cobordism" are docstring words in
  `Elaboration.lean`).
- `quantum-observable-universes/tqft-context.md` opens "The axioms … are
  grounded in topological quantum field theory" and says the contact
  condition "ensures irreducibility of the associated 3d TQFT". No 3d TQFT
  is constructed anywhere for it to be associated with. The same block's
  precise claim, the cited isomorphism Cob(2) ≅ Cob(3)_{S²,CF}
  (`li2026-two-sphere`), is a citation and is fine as one.
- `fluid-dynamics/root-of-unity-truncation.md` (§"Three regimes") states
  that generic q > 1, the QOU regime, has infinitely many simple objects.
  A modular tensor category needs finitely many, so the framework's own
  regime excludes the Reshetikhin–Turaev 3d TQFT that "TQFT" would name.
  This is the bean's decisive point and it still holds.
- What is real: Hecke-algebra and Markov-trace mathematics (the bean lists
  `MathlibExt/MarkovMoves.lean`, `Machinery/MarkovTraceOnHecke.lean`,
  `MathlibExt/Ribbon.lean`). "TQFT" in the prose is a name for that
  setting, not a construction.

### 2b. Conformal cyclic cosmology (`qou-a2d7`)

- `prop:qou-is-ccc` → `QOU.qou_is_ccc` (`lean/QOU/JetHorizon.lean:306-312`)
  is proved by `⟨H.degree_zero_vanishes, H.degree_one_leaks,
  H.degree_two_leaks⟩`, three field projections of `structure JetHorizon`.
  It is a restatement of the structure's fields. The `.ts` carries
  `validation: "not_checked"`.
- The title was already narrowed ("Aeon boundaries satisfy the
  horizon-local conditions of a conformal cyclic cosmology"), but the
  statement in `information-theory/qou-is-ccc.md` still says the aeon chain
  "satisfies the three defining properties of a conformal cyclic cosmology",
  and its CCC-2 item asserts that "the CMB of aeon A_{k+1} precisely
  matches the terminal boundary datum of aeon A_k". CCC-2 is not in the
  Lean (the Lean docstring says so), and "CMB" is an observational object
  inside a proposition statement.
- `penrose-ccc.md` ("The underlying mechanism, however, differs", four key
  differences) and the proof block's "Limitations of the claim" are honest.
  The statement block is the outlier.

### 2c. Gravity (`qou-ogj5`, `qou-k34v`)

- `variational-equations.md` says varying ∫_A "yields the categorical
  Einstein equation". In Lean, the equation is a field of the class
  `HasCategoricalEOM`; its one instance, `hasCategoricalEOM_of_facts`
  (`GaugeTheory.lean:208-218`), takes the equation as a `Fact` hypothesis.
  `variational_einstein` (`:228-233`) projects that field. No variation
  produces it. The `.ts` carries `validation: "not_checked"`.
- `archimedean-realisations.md:5` says "The categorical Einstein equation
  reduces to Ric_{g_Θ} = T^{(q)}". No Ricci tensor of g_Θ is defined in
  Lean, so this reduction is asserted, not shown.
- No gravitational observable (post-Newtonian, light deflection, redshift,
  perihelion, Shapiro delay) appears; the corpus says itself
  "This paper does not model quantum gravity"
  (`information-theory/swampland-connections-intro.md:3`), and the LQG
  comparison blocks disclaim derivation. The analogue-gravity blocks
  (`fluid-dynamics/madelung-acoustic-metric.md` and neighbours) are titled
  as analogue gravity.
- `qou-k34v` (Dubrovin's Frobenius manifolds uncited) still holds: the
  measured zero hits for "Frobenius manifold" / "Dubrovin" in content is a
  citation gap for the metric-from-pairing step. Not re-measured in
  `library/` this session.

### 2d. Cosmology (`qou-v1jg`, `qou-fi93`, `qou-qjh8`, `qou-b2bb`)

- `observations/cosmological-chirality-flip.md:18` still says the electron
  and muon survive at q → 1 "with vanishing masses". The bean `qou-v1jg`
  measured that Σ_λ y_λ(H₃) → 3/4 as q → 1, so ρ does not vanish and
  m(K)/m_e = Vol·ρ/ℏ_q² diverges, since ℏ_q = 1 − q⁻¹ → 0. Scope (a): the
  sum, not each knot's ρ, was measured. The sentence has no support in the
  corpus; it is the blocker the bean names.
- `qou-fi93`: every counting object built from q-integers is bar-even
  ([n]_q is invariant under q ↦ q⁻¹), so the bar-odd colour-curve
  asymmetry cannot reach a number density through them. That is a
  structural exclusion with a cited invariant (bar-evenness), scope (b),
  for that class only. No density-producing coupling is derived and none
  is excluded. The comparisons to η_obs in the bean are empirical context
  and stay there.
- `qou-qjh8`: a codimension-1 interface dilutes as a⁻¹, dark matter as
  a⁻³. That is a scaling argument about a model object compared with an
  observed component. It belongs in an empirical-comparison remark, not in
  a theorem. Its Lean (PR #8452) was closed with the batch PRs; nothing of
  it is on main.
- `qou-b2bb`: four follow-ups (mirror vs C antiparticle; a Vol(mirror)
  lemma; density bar-parity; C-equivariance of γγ production). Untouched
  since its claim was released. The Vol(mirror) lemma is pure mathematics
  (hyperbolic volume is mirror-invariant); the rest needs scoping.

## 3. Still open, as mathematics

- `qou-aawz`: no non-trivial `FrobeniusHopfData` on `k[G]` in Lean.
  `QOU.IdemLine.model` (`FrobeniusHopfNilpotentAndNonFieldModel.lean`) is a
  non-trivial model but a proper summand of 𝟙. The `k[G]` model with the
  Frobenius comultiplication and S(g) = g⁻¹ passes the Python probe 7/7;
  formalising it is transcription. No Lean toolchain in this container, so
  it is left for an environment that can build (owner instruction
  2026-11-21: resource-limited work goes to a bean for Antigravity).
- `qou-nnyn`: χ(A) = −6 as one component of ch(A) in HH₀. Its 2026-09-15
  work landed (option A + C chain edits); the bean lists 17 dangling `uses`
  references as the remainder. Not re-measured here.
- `qou-plck`: three objects carry the name "Planck length" (normalised
  total 1, per-step share ℏ_q, dimensional √q). Which one a given block
  means is an author question.
- `qou-8hcq`: four content proposals in
  `docs/audits/2026-09-07-substrate-branch-and-the-q-eq-1-interface.md` §7
  await owner review.

## 4. The perturbative-QFT epic (`qou-3fjn`)

Seven task beans (`qou-txc1`, `qou-bgq9`, `qou-7ypv`, `qou-iw1d`,
`qou-qssg`, `qou-n1ks`, `qou-t3zb`) carry resolution text naming Lean files
of 492–1,274 lines and 80-dps probes. **None of those files exists on main.**
Measured: `git ls-files | grep` for each named file stem
(`WorldlineSchwinger`, `InfraredQFTSubsumption`, `BaryonSpinFlavour`,
`FourLoopQCD`, `DiracWeylClifford`, `RibbonPantBernKosower`,
`BringPushforwardAndGauge`) returns 0. Five of the seven were reopened on
owner approval 2026-11-20 (bean `qou-w12g`); `qou-n1ks` and `qou-t3zb` have
the same pattern and were not in that list.

Whole-folio greps for the epic's vocabulary: Cutkosky 0, Bern–Kosower 0,
Callan–Gross 0, Herm₂ 0, 41/10 0, Machacek 0, Larin 0.

Three problems with the epic as written, independent of the missing files:

1. **Empirical pins inside formal targets.** Titles name "g_A(q₀) = 1.2690",
   "(g−2)_e pin audit", "LHC α_s(Q²)", "4-loop running through 14 TeV",
   "DIS cross-section". Each is a comparison with measurement; under the
   owner's rule none of them may sit in a Lean statement.
2. **Virtual quanta.** Feynman perturbation theory sums over virtual
   particles (photon loops for (g−2)_e; gluon exchange in the Bern–Kosower
   vertex). The owner ruled on 2026-11-21 that virtual photons do not exist
   in QOU; exchange is prior entangled photons or unseen intermediary
   emitters. An epic whose goal is to reproduce Feynman expansions has to
   say how that squares with the ruling before any of it is formalised.
3. **Imported results.** The 4-loop β-coefficients, decoupling constants
   and DGLAP kernels are other people's calculations. Transcribing them
   into Lean proves arithmetic about cited numbers, not a QOU derivation.

What has a mathematical core that does not depend on (1)–(3):

- `Herm₂(ℂ) ≅ ℝ^{1,3}` with det as the Minkowski quadratic form (linear
  algebra).
- Clifford algebra Cl(1,3) trace identities (algebra).
- sin²θ_W = 3/8 as a trace ratio of the hypercharge normalisation in a
  stated embedding, and g_A⁽⁰⁾ = 5/3 on Sym³ of the 4-dim spin-flavour
  space (representation theory). Whether Bring's surface *produces* the
  embedding is the QOU content, and that step is the unstated one.

## 5. Corpus-grep record

Paths run this session: content/folio greps (path 2) for every claim
above; Lean greps; beans read in full (path 6). Paths 0 (`corpus_search`),
1 (`docs/audits/`), 3 (`computations/`) and 5 (`library/`) were not run for
§2, because §2 makes no "open" or "refuted" declaration: it reports what
named blocks say and what named declarations prove. §3 repeats the beans'
own open status and adds no new open claim.

## 6. Proposed scoping edits (owner decision; not enacted)

Each edit narrows a sentence to what is proved. No Lean, no number, no
witness changes.

1. `information-theory/qou-is-ccc.md`: "satisfies the three defining
   properties of a conformal cyclic cosmology" → "satisfies the
   horizon-local conditions CCC-1 and CCC-3 of a conformal cyclic
   cosmology; CCC-2 (boundary-data inheritance) is stated as a conjecture",
   and in CCC-2 replace "The CMB of aeon A_{k+1}" by "The initial boundary
   datum of aeon A_{k+1}", which is the model object.
2. `quantum-observable-universes/tqft-context.md`: "are grounded in
   topological quantum field theory" → "are modelled on the algebraic data
   of topological quantum field theory"; "ensures irreducibility of the
   associated 3d TQFT" → "is the condition that would ensure irreducibility
   of an associated 3d TQFT; no such TQFT is constructed here, and at
   generic q > 1 the category has infinitely many simples, so it is not
   modular".
3. `quantum-observable-universes/variational-equations.md` and
   `archimedean-realisations.md:5`: "yields the categorical Einstein
   equation" → "is postulated to yield …", with a sentence that in Lean the
   equation is a class field (`HasCategoricalEOM`), not a derived variation;
   "reduces to Ric_{g_Θ} = T^{(q)}" → "is expected to reduce to …".
4. `observations/cosmological-chirality-flip.md:18`: drop "with vanishing
   masses" (unsupported; the measured trend is divergence of
   m(K)/m_e as ℏ_q → 0).

Blast radius: four `.md` files (five with item 3's second file). Each has
a `.qa.json` sidecar that goes stale and needs one `qa-sweep`. All five are
prose read in the PDF; no producer, witness or Lean file reads them.
