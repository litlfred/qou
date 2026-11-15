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

**The 0.066 MeV denominator is also soft.**
- The scale ħ²/(m_N a²) gives **0.116 MeV** for the nn scattering length a = −18.9 fm.
- It gives **0.074 MeV** for the np singlet a = −23.7 fm.
- **0.066** corresponds to a ≈ 25 fm.
- I did not trace where 0.066 comes from.

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

**Recommendation (judgement).** Option 1, and trace the 0.066 MeV source first.

**Default.** Option 2: nothing changes.

## 5. Verification

- **Lean, `QuarkStrandConsequences.lean`.** lean-direct `lean -DautoImplicit=false -s 65536` exits
  0 against the restored Mathlib cache. `#print axioms` on the three main theorems gives the
  standard three only. No `sorry`, `native_decide` or `axiom`. Library file, Mathlib imports only.
- **Arithmetic checked by hand:**
  - q⁴ − (q − q⁻¹)q² − 1 = (q − 1)(q³ + 1)/1, as the left side q⁴ − q³ + q − 1;
  - the SU(N) exponents −(N+1)/N and (N−1)/N;
  - the scattering-length scale figures in §4.
