# NS vector 2 — vortex-line topology: helicity, linking, reconnection

Date: 2026-10-12 (session ran into 2026-10-13). Bean `qou-p6tm` (parent `qou-vo9t`).
Setting: unforced 3D incompressible Euler / Navier–Stokes (`f ≡ 0`).
Lean: [`QOU/FluidDynamics/VortexLinkTopology.lean`](../../folio/quantum-observable-universe/lean/QOU/FluidDynamics/VortexLinkTopology.lean).

## 1. Decision in one paragraph

Vortex-line topology gives a **genuine Euler-level obstruction** but **no NS
regularity statement**. Under smooth Euler, vortex lines are material, so the
link type of any vortex tube is fixed and helicity is conserved. A flow that
*must* change the linking of tubes therefore cannot stay smooth. Under NS,
viscosity breaks line transport, so linking can change through **smooth**
reconnection, which experiments and simulations observe routinely. The topological
obstruction disappears exactly where the Clay problem lives. What QOU can honestly
contribute is the discrete core, now formalised and sorry-free: a crossing change
is the *only* braid move that alters a pairwise linking number, it alters it by
exactly ±1, and it alters mutual helicity by exactly `∓2 Γₐ Γ_b`.

## 2. Standard facts, with sources

These are cited, not proved here.

**(F1) Helmholtz–Kelvin transport (Euler).** For a smooth solution of
`ω_t + u·∇ω = ω·∇u`, `ω(X(a,t),t) = ∇_a X(a,t) · ω₀(a)` (Cauchy formula). Vortex lines
are material curves, flux through every material surface is conserved (Kelvin), and
the flow map `X(·,t)` is a volume-preserving diffeomorphism isotopic to the identity.
Any vortex tube is therefore carried by an ambient isotopy, so its link and knot type
is invariant. Sources: Helmholtz 1858, Kelvin 1869; Majda–Bertozzi, *Vorticity and
Incompressible Flow* (CUP 2002) ch. 1–2; Arnold–Khesin, *Topological Methods in
Hydrodynamics* (1998) ch. III.

**(F2) Helicity is conserved (Euler) and topological.** `H = ∫ u·ω dx` satisfies
`dH/dt = 0` for smooth Euler (Moreau 1961, Moffatt 1969, *J. Fluid Mech.* 35).
For thin unknotted tubes with circulations `Γᵢ`,
`H = Σᵢ Lkᵢ Γᵢ² + 2 Σ_{i<j} lk(i,j) Γᵢ Γⱼ`. The self term splits as
`Lk = Wr + Tw` (Călugăreanu 1959/61, White 1969, Fuller 1971). Held source:
`library/procrsoclondona92` (Moffatt–Ricca 1992, *Helicity and the Călugăreanu
invariant*, Proc. R. Soc. A 439). Its text is in `ocr/`, and the `sections/` stub is
a banner (AGENTS.md path-5 fourth tier). Also held: `library/helicity03mmj`.
Arnold (1974) gave the asymptotic-linking interpretation.

**(F3) NS breaks both.** For NS, `dH/dt = −2ν ∫ ω·(∇×ω) dx`, with no sign and no
conservation. Viscous diffusion of `ω` breaks line transport, and vortex lines
reconnect at finite time while the solution stays smooth (all known simulations).
Observations:
- Kida & Takaoka (1994, *Annu. Rev. Fluid Mech.* 26), anti-parallel reconnection
  review.
- Kleckner & Irvine (2013, *Nature Physics* 9): knotted and linked vortices made in
  water untie through a sequence of **local reconnections**.
- Scheeler, Kleckner, Proment, Kindlmann & Irvine (2014, *PNAS* 111:15350,
  arXiv:1404.6513): through reconnection, helicity moves from linking and knotting
  into **helical coiling (writhe/twist)**, and is *transferred across scales rather
  than dissipated*. This is efficient because reconnecting tubes go anti-parallel.
- Kerr (2018, *J. Fluid Mech.*), trefoil-vortex reconnection and helicity
  evolution.

**(F4) The classical argument and its failure.** "If Euler data force the vortex
topology to change, smooth Euler cannot persist, because (F1) forbids the change."
This is a valid *conditional* blow-up criterion for **Euler**. It is useless as stated:
no one has exhibited Euler data for which a topology change is forced, and since
helicity and link type are conserved, smooth Euler never has to change them. For
**NS** it fails at the first step. (F1) does not hold, a topology change is
available to smooth solutions, and nature uses it (F3). A topological argument
therefore cannot separate NS blow-up from NS regularity.

## 3. Lean results (sorry-free)

File: `QOU/FluidDynamics/VortexLinkTopology.lean`, namespace
`QOU.FluidDynamics.VortexLink`.

A braid word on `n+1` strands runs on a state made of a position-to-label map and a
symmetric signed crossing matrix `C`. For a pure braid, `lk(a,b) = C a b / 2`.

| Theorem | Statement |
|---|---|
| `run_R2` | `σᵢ^e σᵢ^{−e}` leaves the state unchanged (Reidemeister II) |
| `run_braid` | `σᵢσᵢ₊₁σᵢ` and `σᵢ₊₁σᵢσᵢ₊₁` (common sign) give the same state (Reidemeister III) |
| `run_far` | `σᵢσⱼ = σⱼσᵢ` for `i+2 ≤ j` |
| `run_congr` | local equalities propagate into any context `w₁ ++ u ++ w₂` |
| `crossingChange_C` | flipping one letter changes `C` by exactly `−2·sgn e` on the crossing pair `{a,b}` and nowhere else |
| `crossing_labels_ne` | with injective labels, the two strands at a crossing are distinct |
| `crossingChange_lk` | `lk(a,b)` moves by exactly `−sgn e`, i.e. ∓1 |
| `mutualHelicity_sub`, `crossingChange_mutualHelicity` | mutual helicity `ΣΣ (C/2) Γ Γ` moves by exactly `−2·sgn e·Γₐ·Γ_b` |
| `mutualHelicity_R2`, `mutualHelicity_braid` | mutual helicity is invariant under the isotopy moves |
| `hopf_C`, `single_crossing_C`, `unlink_C` | concrete checks, by `decide`: `σ₁²` gives `C 0 1 = 2` (Hopf, `lk = 1`); `σ₁σ₁⁻¹` gives `0` |

Each theorem is falsifiable. `crossingChange_C` would fail if the matrix tracked
positions rather than labels. `hopf_C` would fail at `0` or `1`. Axioms: see §6.

**Scope limits, stated plainly.**
- Component linking for **non-pure** braids is not treated. That needs a sum over
  closure cycles plus conjugation (Markov I) invariance, and neither is proved here.
- The diagonal (self-helicity, `Wr + Tw`) is not treated. It lives in the content
  sibling `fluid-dynamics/helicity-conservation.lean`, with CWF as a hypothesis.
- Nothing here touches the PDE. The step from (F1) to "a smooth Euler flow realises
  an isotopy, i.e. a word built from R2/R3/far-commutation moves only" is cited, not
  formalised. It is also only heuristic at the diagram level: a smooth isotopy
  projects to a diagram sequence that generically uses Reidemeister moves, and the
  braid-word model is the restriction to closed-braid presentations (Alexander +
  Markov).

## 4. Mapping to the corpus

- **Carrier.** `braid-fluid.md` identifies `σᵢ` with the half-twist exchange of
  filaments `i, i+1` and treats the confined `n`-filament state space as having
  `π₁ = Bₙ`. `helicity-conservation.md` defines `ℋ_q` with the mutual term
  `2Σ lk_q Γᵢ Γⱼ`. The new file supplies `lk` on braid words that
  `helicity-conservation.lean` previously took as data. At `q → 1` the mutual term is
  exactly `mutualHelicity`.
- **True statement QOU can support (Euler, conditional on F1).** *Let a smooth
  Euler flow carry `n` thin vortex tubes whose configuration is presented by a pure
  braid word. Every word reachable by the flow differs from the initial one by
  R2/R3/far-commutation moves only (F1, cited). So every `lk(a,b)` and the mutual
  helicity are constant along the flow (`run_congr`, `mutualHelicity_R2/_braid`). A
  corpus braid transition that contains a crossing change between distinct tubes
  changes `lk` by ±1 and `H_mut` by `2|ΓₐΓ_b|` (`crossingChange_*`). It therefore
  cannot be realised by a smooth Euler flow for nonzero circulations.* The only new
  input is the cited theorem (F1); the combinatorics is proved.
- **Why it does not transfer to NS.** NS lacks (F1). A crossing change between
  tubes is exactly what viscous reconnection performs, and it does so smoothly (F3).
  The obstruction is therefore not to smoothness but to *inviscid* smoothness.
  Applied to NS, the classical argument is a scope-(a) negative: this mechanism alone
  gives nothing. It is not a structural exclusion of topological ideas.
- **Could a viscous-quantitative version connect?** Only through a rate. A
  reconnection changes `H_mut` by `2|ΓₐΓ_b|` (proved), and
  `|dH/dt| ≤ 2ν ‖ω‖₂ ‖∇×ω‖₂` (Cauchy–Schwarz on F3). A reconnection completed in
  time `τ` therefore forces `∫_0^τ ‖ω‖₂‖∇ω‖₂ dt ≥ |ΓₐΓ_b|/ν`. That is a *lower
  bound on palinstrophy-type activity during reconnection*, not an upper bound, so it
  cannot by itself prevent or force blow-up. It is consistent with smooth
  reconnection, since finite `∇ω` suffices. Scheeler et al. (F3) further show the
  linking helicity is mostly **converted to coiling** rather than dissipated, so even
  this lower bound is loose in practice: the bookkeeping must use total `H`, not
  `H_mut`. Verdict: no regularity route, but a clean quantitative statement.
- **Corpus wording flag (not edited, per brief).** `helicity-physical.md` says
  "Smooth evolution cannot alter the total helicity". That is correct for (quantum)
  Euler only. Under NS-type viscosity it is false (F3). Worth a scoping note by the
  block owner.

## 5. Next step

1. Prove Markov-I invariance and the component-linking sum for non-pure braids. This
   makes `lk` a genuine link invariant of the closure, not just of pure braids.
2. If wanted, state the viscous inequality of §4 as a Lean lemma over abstract
   `ℝ`-valued functions (FTC + Cauchy–Schwarz hypothesis). It is cheap and honest,
   but it is a bookkeeping identity, not NS content.
3. Do not pursue "topology change ⇒ NS blow-up". (F3) is a direct counter-observation
   to its premise.

## 6. Verification

Compiled with lean-direct (`lean --root=/ -DautoImplicit=false -s 65536`) against the
private olean tree, **exit 0** (2026-10-13). `#print axioms` on all 14 named
theorems gives only `[propext, Classical.choice, Quot.sound]`. No `sorry`, no `axiom`,
no `native_decide`, no `: True`. The three `decide` checks are genuine finite
evaluations. Not run: `lake build`, the content/library sweeps, or UGB/Fred2005.
This is a standalone library file with no importers.
