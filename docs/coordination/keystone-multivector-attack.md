# Keystone-closure — multi-vector attack map (2026-07-19)

**Goal.** Close `conj:algebraic-geometric-dilog-equivalence` (the Φ_n → D(z)
regulator equivalence, bar-even/mass **and** bar-odd/decay faces) and its
sibling `conj:binding-qbeta-complex-volume` (𝔙 = Vol + i·CS complex volume).

**Method.** Coordinated multi-front attack. Most fronts are already staffed by
in-flight sibling PRs; this ledger maps them so effort composes instead of
colliding, names the *one* open piece each front must supply, and states the
honesty gate that separates a derivation from a laundering. It is a
**coordination artifact**, not a claim of new results — every disposition below
is sourced to a landed commit / audit / open PR.

**Discipline (STRICT, applies to every vector).** No fit; no `c_k` wired to
production; scope-(a) vs scope-(b) labelled per AGENTS.md; a §3b class instance
is NOT a proof; "sorry-free ≠ derived". The keystone stays a conjecture until a
front supplies a *derived* (not anchor-inverted) closure.

---

## 0. The two faces (why the attack splits)

The complex volume `𝔙 = Vol + i·CS` splits by the bar-involution, and this split
is now **Lean-proved** (`OhtsukiTowerBarParity.lean`, `even_rung_real` /
`odd_rung_imaginary`, sorry-free; commit `de1b0c62`):

| Face | Object | Observable | Regulator target | Frontier status |
|---|---|---|---|---|
| **bar-EVEN** | Vol (real), q→1 entire | mass / binding | `D(z) = Vol_hyp` (conj items 2–3) | reduced to the **ArchimedeanLimit / q→1⁻ Tauberian core** (V1) |
| **bar-ODD** | CS (imaginary), root-of-unity q | Q_β decay (c₃ S-leak) | the **G3 monodromy datum** `z(q₀) → S` | 4₁ **closed/null**; live on **5₂-class chiral** geometry (V2) + **integer Stokes A_ω** (V3) |

`4₁ is amphichiral ⇒ its deformed Stokes amplitude is real ⇒ it carries NO
bar-odd datum` is a **proved scope-(b) exclusion** (commits `fd17622b` /
`48e0c82d`; `qbeta-odd-channel-cornering-capstone`, 2026-07-18). This is *why*
the bar-odd face moved off 4₁ onto 5₂.

---

## The seven vectors

### V1 — Bar-even ArchimedeanLimit analytic core  *(closes conj items 2–3)*
- **Open piece.** The `q → 1⁻` × m-sum exchange (Abelian/Tauberian) that turns
  the finite-n double series into `D(z)`, plus the dilogarithm **reflection FE**
  (currently an honest `sorry`).
- **Landed toward it.** Part-A reductions `log Φ_n →` exact finite-n series
  (`e31a9a39`/`3d192dc8`/`359be603`); Part-B cusp-regulator constants
  `Li₂(1)=π²/6` (`bd7a4ac7`), `Li₂(−1)=−π²/12` (`d9419bcd`), duplication FE
  (`24a8ea9f`) — all sorry-free.
- **Coordinate with.** #3787 (Clausen filler, 4₁ saddle bricks — same dilog
  analytic layer). My #3773 `asymptotic_volume_of_vc` is the conditional shell
  the discharged limit would feed.
- **Character.** Pure Lean/Mathlib real-analysis — the single most tractable
  advance on the *original* conjecture. **Bean `qou-524t`.**

### V2 — Bar-odd 5₂ chiral geometry  *(the G3 decay datum)*
- **Open piece.** Exhibit the argument whose archimedean evaluation reproduces
  `S(muon)=+0.00968298`, `S(proton)=−0.03945936`, sourced from the **chiral 5₂**
  (non-amphichiral, CS≠0, trace field the **cubic of disc −23**, Vol(5₂)=3·D).
  *(Corrected 2026-08-11: this said "home field ℚ(√−7)". The tower law forbids
  it — 2 ∤ 3. ℚ(√−7) is 5₂'s Alexander layer; the quadratic attached to the trace
  field is ℚ(√−23), which is the line the A6 σ-pair tower already records. Note the
  `Vol(5₂)=3·D` factor is forced by `z₂ = 1/(1−z₁)` and carries no field information.
  Bean `qou-ynff`.)*
- **Landed toward it.** Masbaum 5₂ cyclotomic coefficients `C_{5₂,1..3}` verified
  + Lean-formalized bar-asymmetric (`c6efbf64`/`4b0852b1`/`4cae2d63`); 5₂ exact-Z
  Theorem-22 blocks (`57f97aed`); `FiveTwoSaddleCurve.lean` (complex singularity
  `ι₁₃ = −0.39349 − 0.65852i`).
- **Refuted sub-routes (do NOT re-run).** π²/5-analog (`faf5b706`, Gaussian
  growth dominates), naive twist-Gaussian (`1cc53075`), real-`u` identification
  (`3b2212d9`/`a50b67ae`), classical/1-loop saddle carrier (`fd17622b`).
  Survivor carrier: **categorical H₅(q) Markov trace** (`c8a61eb4`).
- **Coordinate with.** #4037 (5₂ wall-crossing at substrate bar-pair — honest
  negative so far, ill-conditioning). **Bean `qou-ized`.**

### V3 — Integer Stokes A_ω  *(anti-fit, DT / 3d-index)*
- **Open piece.** Derive `A_ω` as an **integer count** (Donaldson–Thomas /
  3d-index), never anchor-inverted; then identify it with the corpus `A_ω`
  normalization (`Im 𝔙 → N_odd`) — the *explicitly-not-yet-claimed* bridge.
- **Landed toward it.** GGM 4₁ Stokes data → integer Stokes constant **3**
  (`qbeta_g3_ggm_stokes_41.py`, GGM 2012.00062); trace-field hypothesis
  `−3 = disc(ℚ(√−3))` (H1, **not** verified). Imported: DGG/GGM/GK 3d-index
  papers (references `dimofte-gaiotto-gukov2013`, `garoufalidis-gu-marino2023peacock`).
- **Coordinate with.** #3805 (G3 Stokes via GGM 3d-index — heavily reviewed,
  24 comments; **do not duplicate — this is the owner front**). My
  `SDeformedVolumeChannel` can carry "A_ω = integer count" as a conditional
  field. **Bean `qou-ledr`.**

### V4 — Murakami deformed-VC / categorical N-selection  *(absolute q₀, Subgoal-2)*
- **Open piece.** A categorically-*derived* deformation datum on 4₁ giving
  `Vol(4₁; α) ⇒ ℏ_q ⇒ q₀` absolutely, independent of the μ/p mass anchors —
  the only route that could beat the 11.5 ppb μ–p pin tension (proved to live
  entirely in the absolute anchor `ℏ_q²`, `PinRobustnessOfRatios` sorry-free).
- **Landed toward it.** `FigureEightDeformedMeridianWinding.lean` (sorry-free);
  substrate matching `u(N,k)=N·ln q₀ − 2πik`; named-N menu {3,6,60,120} gave
  0/8 (winding forces `|u|≥2π`). C1–C4 literature candidates enumerated
  (`mq0-literature-candidates`), C2 (Murakami) "structurally richest, needs
  categorical N (no fit)". Imported: Murakami 0401084.
- **Coordinate with.** #2503 (keystone DG construction, draft plan). **Bean
  `qou-thj7`.**

### V5 — Δ_λ per-partition closure  *(binding)*
- **Open piece.** The per-partition `Δ_λ`: sign is **derived**, magnitude
  reduced to a **single scalar** `m ∈ (0, 1/√5)` (icosahedral `1/√5` is Vector 2
  of the `deltalambda-attack-vector-map`).
- **New engine (this week's machinery).** OV/Specht seminormal foundation
  (`OVBaseSeminormalVector.lean`, `SeminormalWeight.lean`, `JucysMurphy.lean` —
  last sorry reduced to the JM eigen-equation on the column-superstandard
  polytabloid); seminormal characters `χ_λ = c_λ·h` (discharged, `f79d472f`);
  H2A/H3/H4 Markov-trace tower (`HeckeH{2A,3}AlgebraInstance.lean`,
  `HeckeH4StabilizationRung.lean`); Wenzl Schur-element non-vanishing at the
  substrate (`WenzlSchurElement.lean`).
- **Coordinate with.** #4047 (Δ_λ covariance base cases k≤7), #3806 (RSK
  dimension side), #3432 (Hoefsmit Stage-B), #4049 (binding-period involution).
  **Bean `qou-hmr9`.**

### V6 — Deuteron-wall alien resummation  *(binding, concrete parameter-free)*
- **Open piece.** The Hopf deuteron has `Vol = 0` (perturbative binding
  vanishes) yet `B_D = 2.225 MeV`. Compute the bipartition-dual trans-series
  `B_D = m_e·Σ_{m≥1} S_m·A_ω^m·e^{−m ω₀/√x}·Φ_m(x)` — the "dualized entanglement
  energy" — to reach `B_D`.
- **Landed toward it.** bar-parity (proved) + binding period Gevrey-1/2 (proved,
  `7fee77ea`) + **derived** Stokes datum `A_ω = 4√2·e^{−3/8}`, `ω₀ = 1/√2`
  (`c7fdd8ae`). Leading (m=1) term undershoots (`m_e·A_ω = 1.987 < 2.225`) —
  scope-(a), NOT a refutation; the full `S_m`/`Φ_m` are uncomputed.
- **Character.** The strongest concrete parameter-free binding target. **Bean
  `qou-mbz4`.**

### V7 — Lean carrier + infra hygiene  *(foundational, unblocks all)*
- **Open piece.** Keep the §3b carrier layer honest (no fabricated instances),
  and grow the sandbox olean cone so the analytic fronts (V1, V6) are
  sandbox-verifiable.
- **Landed / in-flight.** My #3773 (Φ_b abstract carriers `SArgumentIdentification`
  / `SDeformedVolumeChannel` / `PhiBFibreExtension`; **kernel integrability now
  fully unconditional** after building the ExpDecay + ImproperIntegrals cone);
  #3793 (de-fabricate the archimedean_agreement `⟨0,rfl⟩` carriers) — **note:
  needs reconcile, current main already moved TorusKnotMass to `:= sorry`**;
  #4054 (carrier sign audit + Wenzl H₂ Wedderburn); #3411 (de-axiomatise 10
  Tier-2 carriers). **Bean `qou-szd6`.**

---

## The formalization spine (my non-colliding lane)

My #3773 owns the **abstract §3b keystone carriers**. The frontier fronts (V2,
V3, V4) each produce a *concrete* object that would **instantiate** one of my
abstract classes. The highest-value non-duplicating contribution is the
**wiring**: state, as §3b-cond conditional structure, the implications

- `[FiveTwoBarOddCarrier] ⟹ SArgumentIdentification` (V2 concrete ⟹ my abstract),
- `[IntegerStokesDatum] ⟹ SDeformedVolumeChannel.u-map` (V3 concrete ⟹ my abstract),
- `[ArchimedeanLimit-discharged] ⟹ asymptotic_volume` (V1 ⟹ conj item 2),

so that when a sibling *derives* a concrete piece it closes a named implication
rather than a fresh ad-hoc theorem. No instance is fabricated; the implications
are the honest map from "what a front proves" to "what the conjecture needs".

---

## Coordination roster (front → owner PR → my role)

| Vector | Owner / lead PR | My role |
|---|---|---|
| V1 ArchimedeanLimit | #3787 (adjacent) | contribute the Tauberian-exchange Lean; wire to `asymptotic_volume_of_vc` (#3773) |
| V2 5₂ chiral | #4037 | wiring implication `FiveTwoBarOddCarrier ⟹ SArgumentIdentification` |
| V3 integer Stokes | **#3805 (do not duplicate)** | wiring field on `SDeformedVolumeChannel`; coordinate only |
| V4 Murakami N-select | #2503 (draft) | wiring; watch |
| V5 Δ_λ | #4047 / #3806 / #3432 | consume OV/Specht machinery; no lead |
| V6 deuteron wall | (open) | candidate lead — the concrete resummation |
| V7 carrier/infra | #3773 / #3793 / #4054 | active lead (mine) |

Beans `qou-524t … qou-szd6` under epic milestone bean `qou-wzgm` carry the per-front
task decomposition and are the session work-plan source of truth.
