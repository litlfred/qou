# NS vector 3 — Tao's averaged-NS barrier vs the corpus's regularity / blowup claims

*Bean `qou-hjl0` (parent `qou-vo9t`). Setting: unforced 3D incompressible NS, `f ≡ 0`
(Fefferman alternatives A/B). Audit only — no content block, Lean file or witness edited.*

## 0. The barrier, stated precisely

T. Tao, *Finite time blowup for an averaged three-dimensional Navier–Stokes equation*,
J. Amer. Math. Soc. **29** (2016) 601–674, DOI 10.1090/jams/838, arXiv:1402.0290
(verified against the AMS listing and arXiv, 2026-10-12; **not held in `library/`**).
Tao replaces `B(u,u) = P[(u·∇)u]` by an averaged operator `B̃` (averages of `B` over
rotations, dilations and order-0 Fourier multipliers). `B̃` keeps (a) the energy identity
`⟨B̃(u,u),u⟩ = 0` and (b) every harmonic-analysis bound that the Littlewood–Paley,
Sobolev and Hölder machinery gives for `B`. For a suitable `B̃` some smooth solution
blows up in finite time; the mechanism is a dyadic-cascade ODE circuit of Katz–Pavlović
type. **Consequence (the barrier):** a global-regularity proof for NS whose only inputs
are (a), (b) and the linear dissipative part would also prove regularity for `B̃`, which
is false. So any such proof is wrong. A correct proof must use structure `B̃` destroys.
Tao's companion programme (blog, 2014–) instead tries to *realise* such a circuit with
the true Euler/NS nonlinearity ("fluid computer"), which would give blowup.

**Two scope points used throughout.**
- **Asymmetry.** The barrier constrains *regularity* proofs. It does not refute a
  *blowup* claim. A blowup argument is judged instead by whether it uses a mechanism the
  true nonlinearity realises.
- **Subcritical dissipation is not engaged.** Tao's own *Global regularity for a
  logarithmically supercritical hyperdissipative NS equation* (Analysis & PDE 2 (2009);
  **this citation is from memory and was not web-verified**) proves regularity using
  only (a)+(b). That proof transfers verbatim to `B̃`, and there is no contradiction,
  because strong enough dissipation makes the averaged equation regular too. So
  "(a)+(b) only" is a defect **only when the dissipation is critical or supercritical,
  as it is for true NS**.

## 1. Per-claim table

Paths are relative to `folio/quantum-observable-universe/`. Verdict key:
**(i)** consistent with the barrier; **(ii)** suspect, because the argument (or the
inference drawn from it) uses only averaged-invariant structure or none at all, yet
asserts something about true NS; **(iii)** unclear. Each verdict describes the
*argument as written*. None of these blocks has a Lean proof of an analytic statement:
every NS-relevant declaration checked is a projection of a context class
(`QNsWellposednessContext.existence_uniqueness` in
`lean/QOU/FluidDynamics/q_ns_wellposedness.lean:223–235`; `QBKMContext` in
`q_bkm_criterion.lean:69–71`; `VorticityLowerBoundContext` in
`fluid-dynamics/vorticity-lower-bound.lean:85–93`). Those are assumptions, not proofs.

| # | Claim (file:line) | Structure of the nonlinearity actually used | Verdict | Evidence / note |
|---|---|---|---|---|
| 1 | `thm:q-ns-wellposedness`, `fluid-dynamics/q-ns-wellposedness.md:4–32` — global smooth solution for every `q > 1` | Energy inequality (item 2), linear spectral decay (item 3). Nothing nonlinear-specific. | **(i)** for `q > 1` | The dissipation symbol is `[k]_q² ~ q^{2k}`, exponential in the spectral index. That is far above the Lions threshold `(−Δ)^{5/4}`, so the equation is energy-subcritical and the barrier does not bite (see §0, second point). Being consistent with the barrier says nothing about whether the argument is correct; see #2–3. |
| 2 | `rem` proof strategy, `fluid-dynamics/q-ns-proof-strategy.md:4–25` | Exponential UV damping; a "finite cascade depth" reduction; parabolic bootstrap. All are linear-part or estimate-level. | **(i)**, with internal gaps | (α) line 11 states `dΩ/dt ≤ −νΩ + CΩ^{3/2}`. With linear damping this gives only **small-data** global existence, not global regularity. (β) lines 17–24: "reduces to a finite-dimensional ODE" and "higher modes are damped to zero in finite time" are false as stated. Linear exponential decay never reaches zero, and the nonlinearity couples every mode. |
| 3 | nonlinear estimates, `fluid-dynamics/q-ns-proof-details.md:2–33` | A Ladyzhenskaya-type bound `‖B(v)‖ ≤ ‖d_q v‖·‖v‖_{ℓ¹}` and Gronwall | **(i)**, with a model defect | Line 3 writes the advection as a **scalar one-index convolution** `Σ_{k+ℓ=m}[k]_q v̂_k v̂_ℓ`. That drops the SU_q(2) Clebsch–Gordan, multiplicity and Leray-projection structure. It is a shell or dyadic model, i.e. averaged-type structure. Fine for a subcritical `q > 1` result, but it shows that nothing nonlinear-specific is carried. Line 28: `Λ_q = −ν + C²E₀/ν` can be positive, so the bound gives exponential growth, not decay. |
| 4 | "the classical 3D NS regularity problem is an artefact of the `q → 1` singularity", `fluid-dynamics/q-ns-properties.md:31` | None beyond #1–3 | **(ii)** as an inference | (α) The same file's table (`:26`) says `q → 1` gives **Euler** (`ν₁ = 0`), not NS. Only the fixed-`ℏ_q` row (`:27`) gives NS plus a Bohm term. (β) Every mechanism in #1–3 is averaged-invariant. An argument that regularity "survives" or "fails" in the limit for these reasons alone cannot distinguish NS from `B̃`. |
| 5 | `prop:q-spectral-sobolev`, `fluid-dynamics/p1-spectral-sobolev.md:28–38` | Sobolev embedding only | **(i)** | Linear analysis. It correctly notes the 3D embedding constant degenerates as `q → 1` (`:38`). That is an honest statement of the barrier's premise, not a way around it. |
| 6 | `thm:q-bkm`, `fluid-dynamics/q-bkm-criterion.md:1–3` | BKM uses vorticity transport plus the Biot–Savart log estimate, i.e. genuine NS structure | **(i)**, but vacuous for `q > 1` | It is a continuation criterion, not a regularity claim. The text admits it is "non-trivial only in the `q → 1` limit". The Lean is the iff assembled from two assumed class fields. |
| 7 | `def:ns-regular-qou`, `fluid-dynamics/ns-regular-qou.md:17–25` — `NS(A)=0` ⇒ "classical NS processes all smooth data into smooth global solutions" | **None.** `NS(A)` depends only on `χ(A)`, "independently of … `q` and … initial data" (`:20`). | **(ii) — strongest finding** | A PDE consequence is attached to a cohomology class *by definition*, and no theorem derives it. Read as a statement about true NS, it uses no property of the nonlinearity, not even the energy identity. It would therefore apply equally to `B̃` on the same domain, which blows up on `ℝ³` (Tao). (Whether Tao's construction transfers to `𝕋³` was not verified here.) Also, `:17` says "specialised via `q = 1` from the q-NS system", but `q = 1` gives Euler (#4). |
| 8 | **Internal contradiction with #7.** `fluid-dynamics/ns-singularity-descartes.md:5` (item 3) and `…-proof.md:6,14` | — | **(ii)**, and a corpus inconsistency | Item 3 proves `κ₀|_Σ = 0` for **every** one-dimensional `Σ`, because `H²(Σ,·) = 0`. Since `NS(A) := κ₀|_Σ` (`ns-regular-qou.md:6–13`), **every** QOU is NS-regular, including Descartes (`χ = −6`). So the table at `ns-regular-qou.md:22–25` ("`χ ≠ 0` ⇒ NS-singular") is false by the corpus's own theorem. Combined with #7's wording, the corpus as written entails "classical NS is globally regular" through an argument using no nonlinear structure. The 2026 retraction (`…-proof.md:8–14`) fixed the Descartes theorem but not the definition it feeds. Also `def:ns-obstruction` (`ns-obstruction.md:5`) puts `NS(A)` in `H³_loc(A,Θ)`, while `ns-regular-qou.md:8` puts it in `H²(Σ,𝓑)`. The two disagree on degree. |
| 9 | `ex:torus-ns-regular`, `fluid-dynamics/torus-ns-regular.md:14–17, 33–34` | None (`χ = 0` ⇒ NS-regular) | **(ii)** | Same mechanism as #7. On a 2D torus the conclusion is true but classical (2D NS is globally regular; Ladyzhenskaya), and it is not the Clay problem. Line 34 extends it to **3-manifolds** (the Heisenberg nilmanifold, Seifert fibrations). There it would be a 3D regularity claim derived from `χ` alone, which is what the barrier excludes as a proof. Note `χ = 0` for every closed odd-dimensional manifold, so the argument would "settle" `𝕋³` (alternative B) by topology alone. |
| 10 | `def:ns-obstruction`, `fluid-dynamics/ns-obstruction.md:12–13` — `NS(A)=0` iff global regularity; `≠0` mandates blowup | None | **(ii)** for the regularity half | Same as #7. The blowup half is not barrier-refuted, but it is unsupported (#8 makes the class zero in any case). |
| 11 | `conj:regularity-breakdown`, `fluid-dynamics/regularity-breakdown.md:5–27` (blowup at `q = 1`) | The three "obstructions" (`:14–18`) are failures of exponential damping, of viscosity and of finite cascade depth. All are **failures of estimates**. | **(iii)**; honestly scoped | Correctly labelled a conjecture, and `:1` explicitly disclaims the internal-flow-to-`ℝ³` bridge. But the failure of an estimate is not a blowup mechanism. Tao's theorem shows exactly that energy plus estimates are compatible with **both** outcomes. Obstruction 2 (`ν → 0`) is again the Euler limit, not NS. |
| 12 | `rem:q-ns-research-programme`, `fluid-dynamics/q-ns-research-programme.md:7,27` — "blowup is a structural consequence of the degeneration" | Same as #11 | **(ii)** as worded | "Consequence" overstates a conjecture, and the cited mechanisms are averaged-invariant. Problem 1 (`:11–12`) concedes that the `q > 1` proof is itself only a sketch, which agrees with #2–3. |
| 13 | `rem:ns-surreal-bound`, `fluid-dynamics/ns-surreal-bound.md:9–17`; `appendix-surreals/millennium-unification.md:1,23`; `observations/ns-blowup-physical-evidence.md:1` — `𝒵_q ≍ ε^{−4/3} > Δ_q ≍ ε³` ⇒ finite-time blowup | **Scaling only** (a Kolmogorov-type rate comparison) | **(ii)** — unsound as a proof (scope (a), not via Tao) | A scaling mismatch is the *premise* of the barrier (supercriticality), not a blowup mechanism. Counterexample to "scaling-only ⇒ blowup": axisymmetric NS **without swirl** has the same scaling and is globally regular (Ladyzhenskaya; Ukhovskii–Yudovich). `millennium-unification.md:23` calls this row an "unconditional surreal translation". The translation may be unconditional, but the conclusion it encodes is not. |
| 14 | `prop:vorticity-lower-bound`, `fluid-dynamics/vorticity-lower-bound.md:1–11` and `…-argument.md:2–5` | **Genuine NS structure**: Biot–Savart induction, vortex stretching `Γ/d²` | **(i)** in kind; unproved | This is the right *kind* of input, since it uses structure `B̃` destroys. But (α) the claim is about the weak limit `q → 1`, i.e. **Euler**, not NS. (β) `d ~ √(T*−t)` is asserted, not derived; anti-parallel collapse is numerically contested and not proved. (γ) The Lean only projects assumed class fields. |
| 15 | `prop:leray-profile` and construction, `fluid-dynamics/leray-profile.md:3–5`, `leray-profile-construction.md:2,8,23` | Leray scaling; Nečas–Růžička–Šverák exclusion, whose proof uses NS-specific structure; SU_q(2) fusion | **(i)/(iii)**; honest open question (`:23`) | The discretely self-similar route is legitimate and is not excluded by NRS/Tsai. **Caution:** the 5-ODE truncation at `q ≈ 1.110` (`:8`) is a finite Galerkin or cascade model. Tao's blowup lives exactly in such models, so blowup of the truncated system would be evidence about the model, not about NS. |
| 16 | `conj:ns-counterexample`, `fluid-dynamics/p5-counterexample.md:7–17` | Biot–Savart plus a linking-number obstruction `κ₂ = lk(ϱ₁,ϱ₂)·[𝓑]` | **(i)** in kind; conjecture | Vortex-line linking (helicity) is tied to the exact Euler transport structure, so it is plausibly non-averaged. But phase 2 is again the `ν → 0` (Euler) limit, and "descent fails ∝ linking number" (`:17`) is not derived. |
| 17 | `fluid-dynamics/townsend-biot-savart-strain.md:19–22` | Local viscous strain (Burgers/Townsend) | **(i)** | Uses genuine local NS mechanics, and records its own breakdown at core overlap. Not a regularity proof. |
| 18 | `fluid-dynamics/ns-obstruction-spectral-gap.md:1–7` — "abandons continuous energy estimates entirely" | Hecke eigenvalue collision `(q,−q⁻¹) → (1,−1)` | **(iii)** | This is the one claim that invokes non-averaged *algebraic* structure. No map from the eigenvalue collision to a property of PDE solutions is given, so it cannot yet be checked against the barrier. |

## 2. Summary of verdicts

- **(i), consistent: 1, 2, 3, 5, 6, 14, 15, 16, 17.** The `q > 1` theorem is consistent
  only because exponential dissipation makes it subcritical. Its own proof has the gaps
  noted in #2–3 (small-data-only inequality; false finite-dimensional reduction; scalar
  shell model) and no Lean proof.
- **(ii), suspect: 4, 7, 8, 9, 10, 12, 13.** The sharpest is **#7 + #8**. The definition
  `def:ns-regular-qou` attaches "classical NS is globally regular" to a class that the
  corpus's own theorem `thm:ns-singularity-descartes` item 3 forces to vanish for every
  QOU. Read literally, the corpus derives Clay regularity from topology. That is
  structure-free, so by Tao's theorem it cannot be a valid proof (scope (b): the
  invariant is that the inference never uses any property of `B` and so applies
  unchanged to `B̃`). **Caveat:** the scope-(b) inference assumes the domains match.
  Tao's theorem is on `ℝ³`, and transfer to `𝕋³` was not checked here.
- **(iii), unclear: 11, 18.**
- **Passage `q > 1 → q = 1`.** In every place where the corpus takes `q → 1` with
  `ν_q = (q−1)/(2q)`, the limit is **Euler**, by its own table (`q-ns-properties.md:26`).
  NS appears only on the fixed-`ℏ_q` scaling branch (`:27`), and no block proves
  convergence along that branch. So no claim transfers the `q > 1` regularity to NS.

## 3. What a QOU regularity or blowup argument must use (heuristic — agent's judgement, labelled)

**Must use (regularity side).** Something `B̃` lacks. Candidates from the PDE literature
include: vorticity transport `∂ₜω + u·∇ω = ω·∇u` together with `u = BS(ω)` (the exact
Biot–Savart geometry); geometric depletion of stretching via vorticity-direction
regularity (Constantin–Fefferman); conservation of circulation and helicity for the
inviscid part; and the pressure–Bernoulli maximum structure used by
Nečas–Růžička–Šverák and Tsai. An argument built from exponential `q`-dissipation, the
Frobenius / `L²` pairing, Sobolev constants or rate comparisons is averaged-invariant.
It is admissible at `q > 1` only because it is subcritical there, and it is
inadmissible at the NS endpoint.

**Must use (blowup side).** A mechanism the true nonlinearity realises: a
self-replicating cascade (Tao's programme), or a discretely self-similar profile solved
for the real Leray system (#15), not for a truncated model.

**Does the categorical structure plausibly encode such structure?** (Heuristic;
nothing below is established.)
- **Frobenius pairing → no.** It plays the role of the energy inner product, which `B̃`
  preserves by construction. Positivity or Frobenius arguments are averaged-invariant.
- **`q`-Laplacian spectrum and exponential damping → no.** Linear part only.
- **Braiding / Hecke relation / linking → plausibly yes, but unconnected today.** The
  braiding records how vortex lines link and cross. Linking of vortex lines is helicity,
  a conserved quantity of exact Euler transport that is not generally preserved by
  averaged operators. This is the corpus's one candidate for "finer structure". At
  present no block derives a PDE estimate from it. #16's `κ₂ ∝ lk` and #18's Hecke
  eigenvalue collision assert the link but do not derive it.
- **Next honest step.** State, as a Lean conditional class, an explicit transfer
  hypothesis: a map from braid/linking data of a solution's vortex-line field to a
  quantitative bound such as a depletion inequality. Then check whether the hypothesis
  itself fails for `B̃`. If it fails for `B̃`, it carries real NS structure; if it holds
  for `B̃`, it cannot help.

## 4. Recommended follow-ups (not done here; each needs the owner)

1. Resolve #8. Either `def:ns-regular-qou` / `def:ns-obstruction` drop the "classical NS
   is globally regular" clause, or the class is redefined so that it is not forced to
   zero. The first option is the cheap, honest one.
2. Add the `q → 1` = Euler caveat to #4, #7, #12, #14 and #16.
3. Downgrade the "⇒ finite-time blowup" wording in #13 to "is consistent with", citing
   the axisymmetric-no-swirl counterexample.
4. Fix or flag the internal gaps in #2–3: `Ω^{3/2}` gives small data only; the
   finite-dimensional reduction is false; the scalar convolution model is not the
   SU_q(2) advection.

Sources: [AMS JAMS 29 (2016) 601–674](https://www.ams.org/jams/2016-29-03/S0894-0347-2015-00838-4/),
[arXiv:1402.0290](https://arxiv.org/abs/1402.0290v1).
