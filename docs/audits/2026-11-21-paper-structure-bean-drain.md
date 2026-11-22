# Paper-structure bean drain: statement reports, refs, notation (2026-11-21)

Wave-1 bean-drain sibling "paper-structure", 38 beans. Every claim below was
re-measured on `main` at `2ae54ab401` (2026-11-21) unless it says otherwise.
Nothing in a content block's mathematics was changed by this tranche: the
statement-correctness items (epic `qou-q4oa`) are owner-gated, so each is a
report with a proposed fix, and the fixes wait for the owner's choice.

The only edit made is mechanical: 13 relative links retargeted to blocks that
moved chapters (§3).

## 1. Statement-correctness reports (`qou-q4oa`)

Each row: what the bean claimed, what `main` says now, and what is left.

### `qou-umev` — prop:unit-modulus-eigenvalue

**Mostly fixed on main.** The statement is now conditional (even length gives
`det = 1`; unit modulus iff `χ` real with `|χ| ≤ 2`), the proof gives the
`σ₁²` counterexample, the table reads `e^{±2πi/3}` for `σ₁σ₂`, and the
"baryon–meson duality" is withdrawn in the block's own words.

**One wrong sentence remains** (`mass-theory/unit-modulus-eigenvalue-proof.md`,
paragraph after the table):

> "Note that unit modulus holds specifically for the three-cycle and Borromean
> elements above rather than for arbitrary even words, with
> χ₍₂,₁₎(β_Bor) = 2 − h⁴ …"

- `2 − h⁴` is wrong. Checked with sympy this session: the block's own displayed
  formula `−(q⁴−q²+1)(q⁸−2q⁶−2q²+1)/q⁶` equals `2 − 3h⁴ − h⁶` identically, and
  differs from `2 − h⁴` by `−q⁶+4q⁴−7q²+8−7q⁻²+4q⁻⁴−q⁻⁶ ≠ 0`. At `q₀`:
  `2 − 3h⁴ − h⁶ = 1.99418581297996…` (the table's 1.994), `2 − h⁴ = 1.99809…`.
  The explicit 2×2 model in the proof was also re-checked: braid relation and
  quadratic relation hold, and its trace reproduces the displayed formula.
- "holds specifically for … Borromean" is only true near `q₀`: the same block
  says that at `q = 2` the trace is `−1573/64` and the eigenvalues are real.

**Proposed fix (derived from the block's own formula):** replace the sentence
by "Unit modulus is not automatic for even words; it holds for `σ₁σ₂` at every
`q`, and for `β_Bor` exactly when `|2 − 3h⁴ − h⁶| ≤ 2` (true at `q₀`, false at
`q = 2`)."

### `trm1` — prop:terminal-resolution

**Caption fixed on main** (PR #5008: scoped to the splitting, quotes 6.9 keV,
says the deuteron and binding rows are not derived). **Still open, and sharper
than the bean put it:**

1. The proof determines the dressed quark masses from `μ̄ ≈ M_N/3`
   (`dressed-quark-numerology-at-q0.md`: "derived from `M_N` and `q₀`"). So the
   table's proton and neutron rows reproduce an input, not a prediction: only
   the splitting `m_n − m_p` is predicted. The caption says the rows are "the
   dimensionless ratio rendered against the `m_e` unit", which hides that `M_N`
   is an input.
2. The formula column (`Q(q)·𝔪(L_Hopf)`) and the proof route (Skein pairs) are
   still two different computations; the block says so but keeps both.
3. The deuteron and binding rows are tabulated with no derivation.
4. First sentence ("collapses into a combination of neutrino vacuum drag and
   pure strong-force binding energy") is supported by nothing in the proof.

**Options** are on the decision card (§5).

### `qou-pwd4` + `qou-tvsp` — PBW freeness

**Live on main.** Both `cor:pbw` (`unital-groebner-bases-chapter/pbw-corollary.md`)
and `cor:ugb-pbw` (`buchberger-and-pbw/ugb-pbw-corollary.md`) still state PBW
over an arbitrary commutative ring with no hypothesis on 𝔤, and both proofs
open "choose a well-ordered basis for 𝔤". Every neighbouring block
(`buchberger.md`, `groebner-basis.md`, `division-algorithm.md`,
`remainder-module.md`, `generator-choice-lemma.md`) says "free as an
`R`-module". `bokutchen2015pbw` is registered. The two Lean docstrings
(`UGB/UnitalGroebner/pbw_corollary.lean`, `UGB/BuchbergerPBW/ugb_pbw_corollary.lean`,
"## Manuscript statement") repeat the unqualified claim.

**Proposed fix (corpus-derived):** add "which is free as an `R`-module" to both
statements and both docstrings, add `bokutchen2015pbw` to `cites`, and (tvsp)
a sharpness remark phrased as reported by that survey (§3.7: Shirshov 1953,
Cartier 1958, Cohn's `L_p`), without citing the unread primaries.

### `qou-bzj5` — trivial-lcm compositions over a commutative ring

**The check the bean asked for, done.** The Bokut–Chen obstruction
([bokutchen2015pbw] §1) arises in the double-free algebra `M_{k[Y]}(X)`, where
a leading coefficient is itself a `Y`-monomial and `lcm(u_Y, v_Y) ≠ u_Y v_Y`.
`thm:buchberger` here is stated for a *unital* generating set (leading
coefficients in `R^×`, `s-polynomial.md` takes `λ ∈ R^*`). With unit leading
coefficients every generator can be made monic, the coefficient ring carries
no monomial order, and the classical argument that a composition with trivial
`lcm(u_X, v_X)` is trivial modulo the ideal goes through verbatim over any
commutative ring: for monic `f = ū + r_f`, `g = v̄ + r_g` and disjoint leading
words, `f·w·v̄ − ū·w·g = −r_f·w·g + f·w·r_g`, whose terms are below `ū w v̄`.
So the unit condition excludes the problem; it does not merely avoid it in
examples. **A one-line remark is warranted**; its wording waits for the owner.

### `qou-k6ks` — no quasi-zeros

**Done on main.** `NoQuasiZeros` / `NoQuasiZerosFree` are in
`UGB/GrobnerShirshov/Basic.lean`, threaded through `local_confluence`,
`buchberger`, `pbw_corollary`, `main_theorem_statement`, and discharged by
`noQuasiZerosFree_of_generator`. Bean can close.

### `qou-kh7e` — q\* as a third determination of q₀

**Done on main.** `rem-qstar-decay-sector-q0.md:9` now says `q*` is *not* an
independent third determination and is conditional on `c₃^even = −Vol(4₁)`;
`epistemic-status-of-calibrations.md` says the same. Bean can close.

### `qou-slpd` — slope ½

**Mostly done on main**: `natDegree_c1MultPoly`, `l1CoeffAt_eq_zero_iff`
(`Mass/C1FormalSolutionGrowth.lean`), `c1InfCoeff_order_two`
(`Mathlib/QGevreyOrder.lean`), `newtonSlopes_c1_ne_ggm`
(`Mass/ThetaSlopeArithmetic.lean`), and the sympy check
`computations/qbeta/c3_w2_newton_slope_is_qgevrey_level.py` are all present.

**Two pieces the bean records as done are not on main:**
- `slopeOneCoeff_order_one` / `slopeTwoCoeff_order_half` (the Lean half of the
  "slope = level" model family) do not exist anywhere in `lean/QOU`.
- The docstring of `theta_eq_half_gs_bridge` (`QGevreyOrder.lean` ~l.571) still
  names "the RSZ slope=order theorem", which the bean found does not exist.

**Proposed fix:** correct the docstring (corpus-derived: the same file's
§"q-Gevrey LEVEL" already says the slope is a level); re-land the two model
lemmas as a separate Lean item.

### `qou-2joi` — y_λ citation

**Partly done on main**: `blm1990` registered; the y_λ class carries Wenzl,
Jones, BLM and Lusztig refs. **Left:** the DOI conflict for `lusztig1990`
(`references/lusztig1990.json` says `10.2307/1990961`; `OptionE/CrystalDeltaLambdaScaffold.lean`
and `IwahoriHecke/TypeA.lean` say `10.2307/2152736`). Not resolved here: no
network route to a DOI resolver from this container, and guessing is what
created the conflict. Wenzl 1988 and Jones 1987 are still not in `library/`.

### `qou-lsvj` — B_vol "DERIVED parameter-free"

**Done for `B_vol`**: `computations/mass_binding_dashboard.py` legend now marks
it DEPRECATED, not derived. **Same defect survives one row up:** the `B_gate`
legend row still says "Parameter-free (E₀ × Plancherel weight, no fit)" and
"the parameter-free nuclear SATURATION scale", while the file's own
2026-08-08 banner deprecates `B_gate` with `B_vol`. Corpus-derived fix: give
`B_gate` the same DEPRECATED wording.

### `qou-mumr` — computational length

**The inconsistency is resolved on main by notation**: `discrete-planck-step.md`
now calls `ℓ_P(q) = 1` the normalised total of one Reeb circuit, and
`planck-info-unit.md` uses `ℓ_P^step ∼ ℏ_q`; `planck-reynolds.md`'s
`ℓ_q = (q−1)/q` is that same per-step value. What remains in the bean is a
research opening (forming the spectral distance from the existing categorical
Dirac operator), not a statement defect.

### `qou-f9mv` — is `extracted_theta_all_real` a test?

**Checked: the worry does not apply, but the test is weaker than it reads.**
`computations/em_linking_sk_form_theta_extraction.py` computes
`θ_A² = ln²q₀ − (κ(A)/κ(3))(ln²q₀ − θ₃²)` from real `κ`. Nothing complex is
involved, so `ratio_im_zero_of_shared_law` (a statement about `Im` of a complex
ratio) does not reach it. At the reported family `θ₃ = 0`:

- `all_real` (θ² ≥ 0) is exactly `κ(A) ≤ κ(3)` for every `A`;
- `all_boost_dominated` (θ < ln q₀) is exactly `κ(A)/κ(3) > 0`.

So the two assertions are a monotonicity check and a sign check on the input
series. They are genuine, but the probe's source strings ("real angular
deformations", "binding sign never flips") describe more than they test. The
bean's note that boost-dominance is "genuine content" overstates it: it is the
sign of `κ`.

### `qou-i9gk` — Steps 27–28

Every positive claim of Steps 27–28 is withdrawn in the bean's own body; it is
open only because closing was left to a human. Recommend the owner closes it.

### `qou-1xck` — Noether callout (needs owner)

**Live.** `climax-volume-mass/noether-theorem-callout.md` lists
"Spatial translation | Braid stabilisation | … | `p_q(β)` (writhe) | Markov II
shift". Markov II, `β ↦ β σ_n^{±1}`, changes the writhe by ±1, so the move named
as the symmetry changes the quantity named as its conserved charge. The intent
is the owner's call.

### `qou-w14g` — existence witness (needs owner)

**Live.** `quantum-universe-exists-proof.md` uses Rep(SU(2)) as a witness;
`quantum-universe-su2.md` (v) says its flip braiding satisfies only axioms 2–4.
Which reading of axiom 1 is intended is the owner's call (filed under
`qou-d4kh`, included here because it is a statement report).

### `nhyq`

Title only, empty body ("audit note: D_nu energy, zero-point,
information=energy tiers"). Nothing to act on; recommend scrap unless the
owner remembers the note.

## 2. Notation register (`qou-lv2z`): `qou-6bla`, `qou-hnri`, `qou-zovy`

All three are renames across many files (ℏ_q spellings ~38 sites; three
filtrations called "depth"). Under the 2026-09-07 ask-first rule these are
sweeps, so they wait for the owner. `zovy` additionally records that the
third "depth" (curvature rank) is attached to no well-defined object, which a
rename alone would hide.

## 3. Dangling references (`qou-hqo3`): `qou-x78p`, `qou-lyni`

Re-measured relative links in `folio/quantum-observable-universe/**/*.md`
(excluding `lean/`, `latex/`, and math false positives): **22 broken**.

- **13 fixed in this branch**: the target exists under exactly one path
  (blocks moved `observations/` → `mass-theory/` or `predicted-spectra/`,
  `mass-endomorphism/` ↔ `mass-theory/`, `tools/witness-schema` →
  `schemas/witness-schema`).
- **9 left**: target exists nowhere — `bloch-wigner-mathlib-filler.lean`,
  `three-substantive-mathlib-fillers.lean`,
  `computations/{recursive_atom_knot_atlas_render.py, hp_volume.py,
  witness_staleness_tracker.py, methodology-deprecation.witness.json}` (×2),
  and `braids-and-knots/ew-interface-knot.md`.
- Cite keys: `milnor1950` is now registered; `faddeev1996` and `bokut1978` are
  no longer used; `manuscript` is still used in 7 block files (and as a Lean
  `-- Ref:` key corpus-wide; renaming it is a sweep).
- `qou-lyni`: the broken label `def:ew-interface-knot` was removed from two
  `.ts` files ("Phase 7"), but the grid row
  (`knot-indexed-convolution-grid-table1-data.md`) still names an
  "EW interface-knot definition" that does not exist, and the scope question
  (`H₆` instance vs `def:canonical-braid-interface-composition` over `H_{3A}`)
  is unanswered.

## 4. Not worked here, and why

- **Voice drain** (`qou-9aar`, `qou-x4nh`, `qou-ycjd`, `qou-a1k9`, `qou-e7ku`,
  `qou-qdf6`, `qou-rfp0`, `qou-t5iz`, `qou-ig2d`, `qou-fa1x`): epic `qou-d4kh`
  is W14 of the coordinator's work plan; PR #8756 reports L1 0 / L2 0 / L3 0
  and 14 L4 recorded as debt. Owned there.
- **Forward refs and `uses[]` semantics** (`dtg7`, `fwr6`, `dcy4`, `prn1`,
  `qou-0sq1`): each bean says it needs an owner ruling on what `uses[]` means
  before any edge moves; no agent-decidable subset.
- `qou-i4ml` (section placement, empty body) and `qou-f3mc` (Mathas 3.7
  selection rule, research) are not statement fixes.
