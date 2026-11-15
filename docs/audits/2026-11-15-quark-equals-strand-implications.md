# "Quark = strand": downstream implications, what is proved, physics match; and the nuclear ratio

Beans `qou-qs1d` (framing) and `qou-qs4c` (epic `qou-qs0e`). Date 2026-11-15. PR #7823.

Owner, 2026-11-15: *"try quark = strand, explore downstream implications. what can we prove.
does it match physics?"* Lean: `QOU/SchurWeyl/QuarkStrandConsequences.lean`, lean-direct exit 0,
axioms `[propext, Classical.choice, Quot.sound]`, no `sorry`.

## 0. The reading

- A braid word on n strands describes n quarks (antiquarks are reversed strands).
- Each strand carries an internal space V.
- A Young channel λ is a symmetry type of all n strands together. At convention D, with
  dim V = 2 (u/d):
  - (3) is the Δ quartet, isospin 3/2;
  - (2,1) is the nucleon doublet, isospin ½;
  - (1³) is absent.
- If the quark carries colour, spin and flavour, then V = C ⊗ S ⊗ F.

## 1. What is proved

| # | result | Lean | scope |
|---|---|---|---|
| P1 | With colour (1³), spin, flavour and space as four S₃ factors, Fermi statistics and the Δ⁺⁺ force colour = (1³), δ(spin, flavour), and no ground-state flavour singlet | `ColourChannelSpinStatistics` | q = 1 representation theory; premises physical |
| P2 | **Under quark = strand, P1's premise "four factors with one S₃" is automatic at q = 1**: the strand swap on (C⊗S⊗F)^{⊗3} acts diagonally on C^{⊗3} ⊗ S^{⊗3} ⊗ F^{⊗3} | (classical, no new Lean) | q = 1 |
| P3 | **At q ≠ 1 a factorised strand space is NOT a Hecke representation.** The crossing on two factors is R_A ⊗ R_B, with eigenvalues q², −1, q⁻². These are pairwise distinct for q > 1, so they obey **no** quadratic relation at any parameter. Already q² ∈ {q, −q⁻¹} forces q = 1 or q³ = −1 | `tensor_eigenvalue_not_hecke`, `three_eigenvalues_no_quadratic`, `tensor_hecke_eigenvalues_distinct`, `tensor_crossing_not_hecke` | (b) structural; invariant = eigenvalue set |
| P4 | With imported charges, total 3Q ≡ −(n_q − n_q̄) (mod 3), so **integer total charge ⟺ triality zero**, the colour ℤ/3 condition | `charge3_sum_mod_three`, `integer_charge_iff_triality` | bookkeeping; charges are inputs |

## 2. Downstream implications

1. **At most one internal factor can carry the q-deformed braiding (from P3).** Either one factor
   is deformed and the others braid classically, or the crossings generate an algebra strictly
   larger than H_n(q). This is a scope-(b) consequence of "quark = strand + factorised V".
2. **Which factor is deformed is now a sharp question, and the corpus points two ways.**
   - Convention D deforms an N = 2 factor, i.e. isospin (`JimboActionKernel`).
   - Sibling PR #7830 (`qou-sl3f`, not merged) shows the colour one-gluon ratio comes out exactly 2
     **only** with colour deformed, in the SU(3) frame q^{−1/3}σ.
   - If colour braids classically its eigenvalues are ±1 and the colour "energies" −log|μ| vanish.
3. **The (2,1) projection in the `qs0e` hypothesis is a nucleon channel, not a quark.** Under this
   reading a quark state is one strand's label.
4. **`qou-gpb5`'s "s₁ is the up quark" needs re-reading.** σ₁ is a crossing *between* strands 1
   and 2, i.e. an interaction, not a strand. Under quark = strand, a quark is not a Hecke word.
5. **Gauge structure.** P4 shows charge integrality and colour triality are one condition. The
   sibling's hypothesis that the stripped u(1) piece q^{1/N} is baryon number 1/N (#7830) would
   then tie the u(1) of gl₃ to that ℤ/3. **Hypothesis only.**

## 3. Does it match physics?

**At q = 1 (order zero): yes.**
- Decuplet S = 3/2 and octet S = ½, with no ground-state singlet (P1).
- Δ charges {2, 1, 0, −1}, proton 1, neutron 0 (P4 examples).
- μ_p/μ_n = −3/2 against the measured −1.46, with μ ∝ Q imported.
- Mesons qq̄ and baryons qqq carry integer charge, while qq or a lone q do not (P4).

That is the textbook constituent quark model, unchanged.

**At q₀ ≈ 1.11: a structural tension (P3).** Real QCD has exactly one gauge-braided factor, colour,
while spin and flavour are global labels. "One deformed factor" is therefore physically natural
**if that factor is colour**. The corpus's only q-deformed Hecke structure (convention D) is
N = 2, i.e. isospin. So under quark = strand, the present corpus deforms the factor physics does
not gauge, and leaves classical the one it does.

That is the main downstream finding. It is (b)-structural given the reading, not a refutation of
the framework.

## 4. The nuclear ratio (owner question: "what to do?")

**What the number is.** `R_NUC = B_d / 0.066 MeV = 33.7055`
(`computations/probes/level_three_colour_channel_probe.py:155`).
- **Numerator:** the deuteron binding energy (T = 0, S = 1), a bound state.
- **Denominator:** a **virtual-state** energy of the unbound T = 1 singlet. It is not a binding
  energy.

**Why no Hecke frame reaches it.**
- For a single crossing, the ratio of log eigenvalue magnitudes in the SU(N) frame is
  (N+1)/(N−1). That is 3 at N = 2 and decreases with N (5/3 at N = 4, the Wigner spin-isospin
  frame).
- So **no N gives more than 3**. Invariant: (N+1)/(N−1) ≤ 3 for N ≥ 2.
- In the gl_N frame the ratio is 1 (`qou-o8ww`: |det T| = 1).

**Why 33.7 may be the wrong target (critical-distance judgement, not a finding).** Near threshold,
a binding energy is a strongly nonlinear function of the coupling. A ~1.5× difference in potential
strength separates "bound by 2.2 MeV" from "just unbound". A coupling ratio (what a crossing
eigenvalue gives) and an energy ratio across the bound/virtual threshold are different
observables, so 2 against 33.7 is not like-for-like.

**Correction (same day): the 0.066 MeV denominator is NOT soft.** An earlier version of this
section called it soft, from the zero-range scale ħ²/(m_N a²). That was my error.
- With the effective-range correction (a = −23.74 fm, r = 2.77 fm), the np ¹S₀ virtual-state pole
  sits at κ ≈ 0.0398 fm⁻¹. That gives E = (ħ²/m_N)κ² ≈ 41.47 × 0.001584 ≈ **0.0657 MeV**, i.e. the
  0.066 used.
- The probes label it correctly as the np ¹S₀ (T = 1) virtual state
  (`channel_asymmetry_crossing_budget_bound_probe.py:126`). That pair has the same nucleon content
  as the deuteron, so the target is well defined.
- Only the category point above stands. Nothing else repeated the "soft" claim: no bean or PR
  comment did, and the chat statement is superseded by this one.

### Decision for the owner: the nuclear ratio

**Option 1: re-scope the comparison.**
- *Means:* record "one-crossing ratio vs B_d / E_virtual" as **ill-posed**, a category mismatch,
  rather than as a miss by 33.7. The nuclear comparison then needs a derived two-body binding step:
  coupling → bound-state energy, with its range derived rather than fitted.
- *Costs:* edits to beans `qou-o8ww` and `qou-vlrq` and the probe's docstring. The derived bound-state
  step is new research.
- *Risks:* the "one mechanism caps two sectors" narrative in those beans weakens.
- *Commits to:* not quoting 33.7 as a target for a coupling ratio.

**Option 2: keep it as the recorded miss.**
- *Means:* no change.
- *Risks:* the corpus keeps comparing a coupling ratio to an energy ratio, which a referee would
  flag.

**Option 3: change the channel.** Treat T = 0 as spin-isospin S = 1 (Wigner N = 4). This gives
5/3, which is worse. Listed for completeness.

**Recommendation (judgement).** Option 1.

**Default.** Option 2: nothing changes.

**OWNER RULING 2026-11-15: Option 1.** The one-crossing coupling ratio against
B_d / E_virtual(¹S₀) is recorded as an **ill-posed comparison**, a category mismatch between a
coupling and an energy across the bound/virtual threshold, not as a 33.7× miss.
- Recorded in beans `qou-o8ww` and `qou-vlrq` by append.
- The probes that quote 33.7 as a target (≥ 10 under `computations/probes/`) were **deliberately not
  edited**. A docstring edit changes `scriptHash` and drifts their witnesses. They are dated records
  of what they measured; their "miss" readings are superseded by this ruling.
- The live follow-up: derive a coupling → binding step (two-body bound-state energy from a derived
  coupling and range, no fit) and compare *that* to B_d and E_virtual.

## 5. Verification

- **Lean, `QuarkStrandConsequences.lean`.** lean-direct `lean -DautoImplicit=false -s 65536` exits
  0 against the restored Mathlib cache. `#print axioms` on the three main theorems gives the
  standard three only. No `sorry`, `native_decide` or `axiom`. Library file, Mathlib imports only.
- **Arithmetic checked by hand:**
  - q⁴ − (q − q⁻¹)q² − 1 = (q − 1)(q³ + 1)/1, as the left side q⁴ − q³ + q − 1;
  - the SU(N) exponents −(N+1)/N and (N−1)/N;
  - the scattering-length scale figures in §4.

## 6. Decision for the owner: which single factor carries the q-deformation

**The decision.** Under quark = strand with V = colour ⊗ spin ⊗ flavour, P3 proves that at most one
factor can carry the Hecke braiding at q₀. Which one is a choice about what the substrate's q
*means*, so it belongs to the owner.

### A cheap measurement that separates the options

This was run before framing, per AGENTS.md: measure before asking. Klein-Kreisler & Ruiz-Altaba
compute the nucleon moment ratio for U_q(su₂) **isospin**, eq. (4.8), with m_u = m_d
(`library/arxiv-hep-ph-9612303v1`, sec-001 lines 211-221, transcribed from the section text).
Evaluated in exact rational arithmetic:

| q | μ_n/μ_p | vs measured −0.684979 |
|---|---|---|
| 1 | −0.666667 | −2.7 % |
| 0.992 (their fit) | −0.684699 | −0.04 % |
| q₀ = 1.1099786 | −0.462140 | −32.5 % |
| 1/q₀ | −0.933389 | +36.3 % |
| √q₀ = 1.0535552 (if U_q's q = √(Hecke q)) | −0.557957 | −18.5 % |
| 1/√q₀ | −0.790754 | +15.4 % |

**Reading (scope (a)).** Under this one model, an isospin deformation of size q₀ moves μ_n/μ_p by
15–36 %, while the undeformed quark model is 2.7 % off.

**Caveats.**
- The formula is transcribed from OCR'd section text. It is visibly not q ↔ q⁻¹ symmetric, although
  the paper says those are physically equivalent, so a transcription or convention issue is
  possible.
- The q normalisation between U_q(su₂) and our Hecke q is not settled here.

So this disfavours "isospin deformed at q₀" at one comparison point. It does not exclude it.

### Option I: deform isospin (the current corpus, convention D)

- **Means.** The H_n(q) action at N = 2 is the isospin action. Colour and spin braid classically.
- **Keeps.** Every convention-D result, read as an isospin-sector statement:
  - `JimboActionKernel`;
  - the Ocneanu/Wenzl weights;
  - the 2026-09-08 Q_β z_D ruling;
  - the mass and binding channel.
- **Loses.**
  - **Colour dynamics.** Classical colour has crossing eigenvalues ±1, so colour exchange energies
    −log|μ| vanish. The QCD colour-factor ratio is then not a substrate observable. Colour
    contributes only the q = 1 constraint (1³) plus Fermi statistics (P1).
  - **Confinement** would have to come from elsewhere.
- **Risks.**
  - The moment test above: q₀-sized isospin deformation is 15–36 % off μ_n/μ_p, under one model.
  - Physical isospin breaking is ~10⁻³ (e.g. (m_n − m_p)/m), against q₀ − 1 ≈ 0.11. A q-deformation
    is not a breaking, but its moment signature must still be small.
- **Commits to.** Treating colour as a classical label throughout, and finding the nuclear
  T-dependence inside isospin.

### Option II: deform colour (level 3, SU(3) frame)

- **Means.** H_n(q) acts as U_q(gl₃), in the SU(3) frame q^{−1/3}σ, on the colour factor. Isospin and
  spin braid classically.
- **Keeps / gains.**
  - The colour one-gluon ratio comes out as exactly 2 (sibling #7830).
  - The colour singlet (1³) is present, with weight q⁶/(Φ₃Φ₆)³ = 1/27 at q = 1.
  - The deformed factor is the one physics gauges.
  - μ_n/μ_p stays at the classical −2/3, 2.7 % off, because isospin is undeformed.
- **Loses / re-reads.**
  - Convention D (r = 2) stops being *the* substrate channel. JimboActionKernel stays true
    mathematics, but its physical reading moves.
  - The canonical Markov parameter would become z₃ = q⁵/(q⁴+q²+1), which reopens the 2026-09-08
    Q_β ruling.
  - The mass and binding dashboards rest on r = 2.
- **Costs.**
  - No N = 3 Jimbo action is formalised (gap G1).
  - The 2026-10-10 level-3 test measured the Borromean trace near-match at 2.69e-4, ~1100× worse
    than level 2. That figure is in the **gl₃** frame; the **SU(3)-frame** value has not been
    measured.
- **Commits to.** A corpus-wide re-reading of every r = 2 result. This is the largest blast radius
  of the three options.

### Option III: deform neither factor alone

- **Means.** The crossing on V ⊗ V has three eigenvalues (P3), so the substrate algebra is a cubic
  quotient of the braid group, strictly larger than H_n(q).
- **Costs.** It abandons H_n(q) as the substrate algebra: every Hecke, Markov and Wenzl result
  becomes a statement about a quotient.
- **Commits to.** New foundations. Listed for completeness.

### Default

Nothing is chosen. "Quark = strand" stays a framing in `qou-qs1d`, P3 records the fork, and the
corpus continues as Option I without having said so.

### Recommendation (judgement, not a finding)

Measure one more thing, then choose between I and II:
- re-run the 2026-10-10 Borromean near-match in the **SU(3) frame**;
- settle the U_q-vs-Hecke q normalisation for the moment test.

If the SU(3)-frame near-match is comparable to level 2, Option II is physically natural and its
moment prediction is the better one. I lean II on physics grounds, but its blast radius is the
whole r = 2 corpus, so it should not be chosen on one moment ratio.
