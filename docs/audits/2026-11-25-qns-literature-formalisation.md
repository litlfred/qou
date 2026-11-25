# Which fluid and holography results can be formalised in the QOU q-NS setup

Date: 2026-11-25. Epic `qou-i6e2` (beans `qou-50hi`, `qou-q5wm`, `qou-0v0e`,
`qou-0nqs`). PR #9434. Sibling epic `qou-qrrb` / PR #9428, whose review
(`docs/audits/2026-11-25-holography-qns-essay-review.md` on that branch) this
document builds on and does not repeat.

Owner request, verbatim: *"I want to see what of the lit we can fomalize in QOU
q-NS setup..."*.

Photon form in scope (owner ruling): γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹. Nothing
below depends on it.

## The setup used

`def:q-navier-stokes` (`fluid-dynamics/q-navier-stokes.md`) writes the system
with `d_q`, its adjoint `δ_q` and `Δ_q = d_qδ_q + δ_q d_q`. The only place a
literature theorem can be stated *and proved* is where those operators are
realised concretely. The realisation used here is a finite 2-complex
`C⁰ →d₀ C¹ →d₁ C²` with unit Hodge stars (`δ := dᵀ`). This is the
Mohamed–Hirani–Samtaney setting, and the Bring {5,4} map is one instance of it
(V, E, F = 30, 60, 24; Betti (1, 8, 1); exact, PR #9428).

Lean: `folio/quantum-observable-universe/lean/QOU/FluidDynamics/DECNavierStokes.lean`.
Generic coefficient ring `R` (ordered field where an inequality is needed); no
`ℝ`, no `q₀`, no metric.

**Verification.** `lean -DautoImplicit=false -s 65536` against the restored olean
cache (`cat/folio-assistant-sci/lake-cache/qou-v4-24-0`, 3975/3975 oleans traced):
exit 0. `#print axioms` on `energy_equality`, `harmonic_circulation`,
`enstrophy_decay_of_spectral_gap`, `mass_conservation`, `nelson_consistency`,
`nuQ_one_add_le` and `nuPhys_eq` lists only `propext`, `Classical.choice`,
`Quot.sound`; no `sorryAx`. `scripts/check-sidecars.sh`: no §7c flags.

## One row per literature result

Status key: **Lean** = proved sorry-free in the file above; **Lean, conditional**
= proved from a named hypothesis that is *not* proved in Lean; **exact** = exact
computation (rational / algebraic, no float64); **scope-limited** = needs
structure QOU lacks, scope (a); **not applicable** = no QOU object to state it on.

| # | Literature result | Source | Status | Lean name / evidence | What it needs that QOU lacks, or caveat |
|---|---|---|---|---|---|
| 1 | Discrete Stokes theorem `⟨dα, w⟩ = ⟨α, ∂w⟩` | Mohamed–Hirani–Samtaney (MHS) 1508.01166 §3.2 | Lean | `pairing_adjoint`; also `sum_coboundary_eq_zero` (#9428) | none |
| 2 | Incompressibility as `δu = 0`, and the pressure gradient drops out of the energy | MHS §2–3 | Lean | `pressure_orth_of_divFree`, `exact_orth_coexact` | none |
| 3 | Energy equality `dE/dt = −ν Ω`, `Ω = |ω|²` | MHS §5 (energy); classical | Lean | `energy_equality`, `energy_nonincreasing` | needs a skew advection `⟨v, B(v)⟩ = 0`, taken as a hypothesis. MHS's own advection is not shown here to be skew. |
| 4 | Vorticity equation; pressure drops out | MHS §3.3 | Lean | `d1_lap1`, `vorticity_equation` | none |
| 5 | Exact discrete conservation of mass and total circulation | MHS §5, pp. 29–32 | Lean | `mass_conservation`, `total_circulation_zero` | closed oriented surface (`1ᵀd₁ = 0`), constants closed (`d₀1 = 0`) |
| 6 | Kelvin circulation | classical; MHS §5 (discrete form) | Lean for two discrete forms; full Kelvin scope-limited | `total_circulation_zero`; `harmonic_circulation`: along any harmonic 1-cochain the circulation changes **only by advection** | The material-loop theorem needs a loop transported by the flow, i.e. a moving mesh or a Lie derivative. A fixed complex has neither. Scope (a). |
| 7 | The 2g harmonic modes are steady Stokes solutions and are not decayed by viscosity | Hodge theory; corrects MHS's stream-function form, which drops them (`qou-k5jb`) | Lean + exact | `lap1_harmonic`, `harmonic_circulation`; dim ker Δ₁ = 8 on Bring (exact rank, #9428) | the dimension 8 is exact rank in a probe, not Lean |
| 8 | Enstrophy decay at rate ≥ 2νλ₁ | classical Poincaré-type bound | Lean, conditional + exact | `enstrophy_equality_stokes` (unconditional identity), `enstrophy_decay_of_spectral_gap` (hypothesis `hgap`); on Bring λ₁(Δ₂) = 5 − √5 from an exact characteristic polynomial (#9428) | linear (Stokes) part only. The gap itself is not proved in Lean. Not Bring-specific: every closed surface has its own gap. |
| 9 | Bredberg–Keeler–Lysov–Strominger ε-expansion as a (q − 1)-expansion | BKLS 1101.2451 §3, p. 5, eq. (4) | Lean (power counting) + scope-limited | `nuQ_one_add_le`: ν_q(1 + ε) ≤ ε/2; `nuPhys_eq`: ν_phys = 1/(2q) | Their scaling keeps the viscosity η **fixed** (eq. 4). Setting ε := q − 1 in the substrate layer makes η = O(ε), so the viscous term is O(ε⁴) against O(ε³) for advection: leading order is incompressible **Euler**. In the physical layer (`def:qns-unit-layers`) ν_phys → ½ is fixed, which is the right shape, but then ε is an independent amplitude parameter, not q − 1. Also needs the Rindler bulk and cutoff surface, which QOU lacks. |
| 10 | η/s = 1/4π | Bhattacharyya–Hubeny–Minwalla–Rangamani 0712.2456 §4.5, p. 24 | not applicable | — | needs an entropy density s; theirs is the horizon area of an AdS₅ black brane. The corpus has an acoustic Hawking temperature (`acoustic-horizon-thermodynamics.md`) but no entropy density for the brane fluid, and acoustic horizons are kinematic: they do not fix a viscosity. |
| 11 | Viscosity fixed by horizon regularity (η = r_c) | BKLS §4, pp. 5–7 | scope-limited | — | the shape of argument qou-0nqs would need; there is no regularity condition in QOU that fixes ν_q. Scope (a). |
| 12 | HaPPY bulk-to-boundary isometry and Ryu–Takayanagi on {5,4} | Pastawski et al. 1503.06237 Thm 1–2 | not applicable | — | needs an asymptotic boundary and perfect (unitary) tensors; Bring is a closed quotient. #9428 records the [[60, 8]] homological code instead. |
| 13 | Turaev–Viro / Levin–Wen state sums | Turaev–Virelizier 1006.3501; Levin–Wen cond-mat/0404617 | scope-limited | `realGtOne_not_rootOfUnity` (#9428) | needs a fusion category, i.e. q a root of unity; q₀ > 1 is not. Applies only to `prop:root-of-unity-truncation`. |
| 14 | Beale–Kato–Majda criterion | classical | already in corpus; trivial on a finite complex | `q_bkm_criterion.lean` (conditional class) | On a finite complex the system is a finite-dimensional ODE with a dissipative linear part, so BKM has no content there. It says nothing about 3D. |
| 15 | Helicity conservation | Moffatt; corpus `helicity_conservation.lean` | not applicable on Bring | — | helicity is a 3-form quantity; on a 2-dimensional complex it vanishes identically. |

Nothing in this table bears on 3D regularity. A finite complex gives a
finite-dimensional ODE, and Bring's surface is two-dimensional, where
Navier–Stokes is globally regular classically.

## qou-0nqs: is "ℏ_q is the kinematic viscosity" a derivation?

**Verdict: no. It is a modelling choice, and the corpus carries it as a
definition.** One exact consistency fact constrains it.

Corpus-grep, all eight paths (AGENTS.md §"Before declaring open"):

| path | searched | found |
|---|---|---|
| 0 `corpus-search.ts` | "kinematic viscosity", "viscosity", "Navier", "nu_q" (`--search-text`, limit 60) | `def:q-navier-stokes`, `def:qns-unit-layers`, `planck-reynolds`, `q-ns-properties`, the Kelvin-dispersion blocks. All **use** ν_q; none derives it. |
| 1 `docs/audits/` | `viscos`, `nu_q`, `ν_q` | 2026-08-14 uniformity audit: "ν_q is derived from q (zero new DOF)" means it is a function of q, not that the formula is derived. 2026-07-18: the closure ε = ν_qΩ is tagged `heuristic`. |
| 2 `folio/` | as above, plus `\hbar_q/2` | `def:qns-unit-layers` calls ν_q = (q−1)/(2q) "the derived ladder quantity" with no derivation given; `planck-reynolds.md` defines Re = c_qℏ_q/ν_q = 2/(q−1), which presupposes ν_q. |
| 3 `computations/` | `viscos`, `nu_q` | the qns_* probes take ν_q as input. |
| 4 `docs/coordination/` | same | nothing. |
| 5 `library/` (INDEX, sections, ocr) | Nelson, stochastic mechanics, viscosity | no Nelson source held; BHMR and BKLS (PR #9428) derive *their* viscosities from a horizon, which QOU lacks (rows 10–11). |
| 6 `beans/defs/` | `viscosity` | `qou-a3n3`, `qou-habm`: both use ν_q, neither derives it. |
| 7 `q-navier-stokes.qa.json` agent verdicts | | `trap-negation-contrast`: "the derived-vs-postulated status of nu_q is the point being defined". Records the claim; does not derive it. |

This is a statement about the surfaces searched, not a proof that no derivation
exists.

**What is exact.** The same block writes the quantum pressure as
`Q_q = −½ℏ_q² Δ√ρ/√ρ`, which is Madelung's `−(ℏ²/2m)Δ√ρ/√ρ` at `m = 1`. Nelson's
diffusion constant at that mass is `D = ℏ_q/(2m) = ℏ_q/2 = ν_q`, and the
Madelung coefficient is `2D²` (`nelson_consistency`, Lean). So ν_q is the same
number as the diffusion constant the corpus's own `Q_q` already fixes. The ½ is
not free once `Q_q` is fixed.

**What that does not give.** In Nelson's theory `D` drives an *osmotic* term of
an inviscid fluid; the forward and backward stochastic drifts average to a
Madelung (Euler) flow. Nothing in that theory makes `D` multiply `Δv` as a
dissipative term. So the identification `ν_q = D` remains a choice. The
fluid/gravity results (rows 10–11) show what a derivation would look like: a
regularity or horizon condition that admits exactly one viscosity. QOU has no
such condition.

### Decision for the owner

What is being decided: how `def:q-navier-stokes` should describe ν_q. It needs
the owner because it changes what the paper asserts, not what it computes.

1. **Record it as a modelling choice tied to the Nelson constant (my
   recommendation).** Change the sentence "it is an induced parameter" to say
   that ν_q is chosen equal to Nelson's diffusion constant ℏ_q/(2m) at the m = 1
   used by Q_q, and cite `nelson_consistency`. Cost: one sentence in
   `q-navier-stokes.md`, the same in `planck-reynolds.md` and
   `def:qns-unit-layers` ("derived ladder quantity"). Risk: none to any
   number; every probe already takes ν_q as input. Commits to: ν_q is an
   assumption until someone supplies a dissipation mechanism.
2. **Keep the wording and leave qou-0nqs open as research.** Cost: nothing now.
   Risk: the paper keeps asserting "induced", which a referee will read as
   "derived".
3. **Look for a derivation** (for example, a regularity condition on the brane
   fluid that, as in BKLS §4, admits one viscosity). Open-ended research, no
   candidate in hand.

Default if the owner says nothing: nothing changes; `qou-0nqs` stays open, and
the paper keeps the word "induced".

## Not done here

- `qou-k5jb` (the DEC q-NS probe on the Bring map) belongs to the #9428 sibling.
  The lemmas above give it its exact checks: energy equality, the 8 conserved
  harmonic circulations, and the enstrophy rate.
- Building the Bring complex itself in Lean, so that `hgap` and dim ker Δ₁ = 8
  become theorems rather than exact-rank facts. Possible (24×24 integer
  matrices) but heavy; not attempted.

## Addendum: does a regularity condition fix ν_q? (bean `qou-gd5s`)

Coordinator route (owner question *"can we generalize and make use?"*): take
the *shape* of the Bredberg–Keeler–Lysov–Strominger §4 argument (smoothness forces η = r_c)
and test whether a regularity or convergence condition on the q-step forces ν_q.
I did not choose the conditions because they give ℏ_q/2 (anti-fit), and none of them does.
Lean: `QOU/FluidDynamics/ViscosityRegularityRoutes.lean`, lean-direct exit 0,
axioms `propext` / `Classical.choice` / `Quot.sound` only.

| condition | outcome | Lean |
|---|---|---|
| positivity of energy dissipation | leaves ν free: any ν ≥ 0 | `DEC.Complex2.energy_nonincreasing` |
| stability of the explicit q-step on every rung of the unbounded ladder [k]_q² | forces **ν = 0** (Euler); an implicit step leaves ν free | `explicit_mode_stable_iff`, `nu_eq_zero_of_stable_on_unbounded_ladder` |
| Habiro integrality of ν | **excludes** ν_q = ℏ_q/2: at q = i, ν_q = (1+i)/2 ∉ ℤ[i]; ℏ_q itself is a Habiro element | `two_mul_ne_one_add_I`; Habiro's evaluation property is cited, not proved |

Scope (a) throughout: these three conditions alone do not fix ν_q; that is not a
claim that no condition can. The literature's mechanism (a horizon or cutoff
regularity that admits exactly one viscosity) has no QOU counterpart yet. The
Habiro row is the sharpest: if the paper ever asks ν_q to live in the same
integral ring as its other q-objects, the factor ½ has to go or be justified.

## Addendum: abelian DEC Stokes vs Yekutieli's non-abelian Stokes (bean `qou-4k93`)

Owner question, verbatim: *"is the discrete Stokes, discrete na-Stokes per
yektieli? do we need to use that?"*

**Answer: the DEC Stokes of #9434 is the abelian specialisation of Yekutieli's
discrete multiplicative integral. For the velocity 1-form, the abelian form is
all that is needed.** Lean: `QOU/FluidDynamics/DECYekutieliStokes.lean`,
lean-direct exit 0 (with `MathlibExt/YekutieliIntegration` and
`DECNavierStokes` built into a scratch olean dir; neither is in the restored
cache). Axioms: `propext`, `Classical.choice`, `Quot.sound` only.

- `faceHolonomy`: Yekutieli face holonomy, i.e. the path-ordered product
  `MathlibExt.YekutieliIntegration.holonomy` along a face's oriented boundary
  word. It works for any group G.
- `faceHolonomy_abelian`, `faceHolonomy_eq_vort` (general → paper): for the
  abelian connection U = ofAdd ∘ v, the face holonomy equals ofAdd((d₁v)_f).
  Here d₁ is the signed incidence read off the same boundary words, so the
  DEC vorticity `DEC.Complex2.vort` is the abelian case. Provenance runs both
  ways: the DEC file cites Mohamed–Hirani–Samtaney, and this file cites
  Yekutieli and proves the specialisation.
- `faceHolonomy_perm_abelian`: only in the abelian case can a boundary word be
  reordered or rebased freely.

**Where q-NS would need the non-abelian form:** a connection-valued vorticity.
Two cases: the SU_q(2) connection of the gauge-covariant diffusion
(`q-ns-properties.md` item 2), or braid / Hecke-valued edge transports. In
both, the curvature of a face is a group element defined up to conjugation,
and the energy identities of #9434 no longer apply verbatim.

**Not done:** the global non-abelian Stokes theorem on Bring. It would say
that the ordered, conjugated product of the 24 face holonomies equals the
product of commutators of the 8 generators. It needs a spanning tree and a face
order of the Bring map in Lean.

## Addendum: does non-commutative vorticity give the gap? (owner question 2026-11-25)

Owner, verbatim: *"can we use non-commutative vorticity? does that give the gap
neede?"*

**No, if the twist is flat; possibly, if it is curved, but then the q-NS energy
identities change.** Lean: `QOU/FluidDynamics/TwistedHarmonicBound.lean`
(lean-direct exit 0; axioms `propext`, `Classical.choice`, `Quot.sound`).

- A flat G-connection in a rank-r representation gives a twisted cochain complex
  (flatness is d₁d₀ = 0). By rank–nullity, dim H¹ ≥ dim C¹ − dim C⁰ − dim C²
  (`finrank_H1_lower`). On Bring this is 60r − 30r − 24r = 6r
  (`bring_twisted_H1_pos`). So every flat twist, abelian or not, leaves at least
  6r harmonic velocity modes that viscosity does not damp. The abelian case
  (r = 1, trivial ρ) has 8. An irreducible twist removes H⁰ and H² but
  *raises* H¹ to exactly 6r. **Scope (b):** the invariant is the Euler
  characteristic χ(Bring) = −6 < 0.
- A curved (non-flat) connection can open a gap in the section Laplacian (the
  magnetic / Landau-level mechanism: on a line bundle with flux B the
  Laplacian on sections is bounded below by |B|). But then d₁d₀ = F ≠ 0. There
  is no cochain complex, and the energy and vorticity identities of
  `DECNavierStokes.lean` no longer hold verbatim. This route is not formalised.
  It would need a definition of the q-NS system on a curved connection, which
  the paper does not give.
- Neither bears on 3D regularity. The vorticity on Bring is already gapped
  (λ₁(Δ₂) = 5 − √5). The only ungapped modes are harmonic velocities, and those
  are what χ protects.

## Cross-check against the sibling's exact DEC probe (PR #9428)

`computations/probes/bring54_dec_qns_probe.py` (witness `bring54-dec-qns`,
12/12, exact, sibling session) independently measures, on the Bring map:
- dE/dt = −ν·enstrophy exactly. This matches `energy_equality`.
- The divergence-free space is 31 = 8 harmonic + 23 coexact.
- Harmonic fields are exact steady states. This matches `lap1_harmonic`.
- Coexact data moves energy into the harmonic modes only through the nonlinear
  term. This matches `harmonic_circulation`, by which harmonic circulation
  changes only by advection.

The Lean identities are generic; the probe is the Bring instance. Neither
derives ν. The sibling's non-abelian file `QOU/BringsSurface/NonabelianStokesTrace.lean`
(#9428) is the other half of the Yekutieli question. This branch proves the abelian
specialisation (`DECYekutieliStokes.lean`) and does not duplicate it.
