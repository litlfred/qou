# Φ_b proof-status + the monodromy-datum gap audit (mass / binding usability)

**Date:** 2026-07-13 · **Branch:** `claude/faddeev-phi-b-construction-wp7xau` ·
**Tier:** status + gap map (read-only survey; no formalization, no wiring) ·
**Scope:** (a) — dependency-ordered gaps between "Φ_b structural laws proved"
and "Φ_b usable in a mass / binding number", plus the
existence / uniqueness / constructive narrowing framework for the open keystone.

## Resolution update (2026-07-13) — G2 CLOSED via the combinatorial route

The **combinatorial (cyclotomic / tetraplectic) route** — replacing the
contour integral by finite root-of-unity algebra — was executed (PR #3768,
[workplan](../workplans/2026-07-13-phib-combinatorial-fibre-lean-workplan.md)).
**Five Lean results, all machine-verified sorry-free** (`lean`-direct exit 0,
v4.24.0; `#print axioms` clean = only `propext`/`Classical.choice`/`Quot.sound`):

| # | File (`QOU/QBeta/`) | Result |
|---|---------------------|--------|
| L1 | `CyclotomicDilogCollapse` | `∏_{k<N}(1−xζ^k) = 1−x^N` (finite reduction of `(x;q)_N` at `ζ_N`) |
| L2 | `CyclicQuantumDilog` | finite cyclic dilog + the true boundary-trade shift `(1−x)D(ζx)=(1−xζ^N)D(x)` ⇒ N-periodicity |
| **L3** | `FaddeevPhiFibreBranch` | **`CyclicFaddeevPhi` class + unconditional discharge `cyclicFaddeevPhi_cyclic` at every primitive `ζ_N` — the fibre-branch mirror of `PhiBProd`'s substrate discharge. This CLOSES G2.** |
| L4 | `CyclicDilogPentagon` | finite Faddeev–Volkov rigidity core (`solution_unique_of_seed`) + `faddeevPhi_unique_of_pentagon` (uniqueness *implication*; pentagon an honest open input) |
| L5 | `TetraplecticYoungStateSum` | N=5 index: `p(5)` (7 partitions), `\|S₅\|=120`, `7 ≤ card(Partition 5)`; deep correspondence an honest §3b structure |

**What this closes and what it does not (honest):**
- **G2 is closed** — the fibre-regime (`\|q\|=1`, root-of-unity) Φ_b construction now
  exists in Lean as a discharged shift-structure instance (L3), where the decay
  physics lives. The contour integral is replaced by finite algebra.
- **G0/G1 are re-scoped, not closed** — L3 is the *algebraic fibre-branch analog*
  (`CyclicFaddeevPhi`), not the ℂ-analytic `FaddeevPhi`; the bridge is a genuine
  *degeneration* of the functional equation (`(1+e^{2πbz})→1` at `ζ^N=1`), recorded
  as prose, NOT faked as a theorem. Integrability / def↔contour (G1) untouched.
- **G3 — the keystone monodromy datum `z(q₀)→S` = Stokes constant `A_ω` via `Δ_ω`
  — remains OPEN.** No L-result closes it; it is the resurgent computation (with
  #3683). L4 converts it to a rigidity statement (the datum is *forced* if the
  pentagon holds), but the pentagon + Liouville step stay the open input. The
  conjecture stays a conjecture — anti-laundering respected throughout.

## 0. Executive summary

The Faddeev non-compact quantum dilogarithm `Φ_b` exists in the Lean corpus at
**three levels of rigor** — a genuine integral `def`, an axiomatized §3b
conjecture-`class`, and a `def` (the modular-double product) that **discharges**
that class on one branch — and **every structural law is machine-verified
sorry-free and axiom-free** (7 files, 0 `sorry`, 0 `axiom`). But **Φ_b feeds no
production observable.** The gap is not more structural theorems; it is a single
**argument-identification / monodromy datum** that no amount of proved algebra
supplies, plus a **branch mismatch**: the one place Φ_b is *constructed* is not
the branch where the physics lives.

**Two faces must not be conflated (this is the key clarification):**

| Face | Object | Observable | Equivalence block | Status |
|------|--------|-----------|-------------------|--------|
| **bar-EVEN** (mass / binding) | compact `Φ_q` → `Vol_hyp` (real Bloch–Wigner `D(z)`) | `m`, binding `B` | `conj:algebraic-geometric-dilog-equivalence` | item 1 **proved**; items 2–3 conditional on the (4₁-proved) volume conjecture |
| **bar-ODD** (decay) | non-compact `Φ_b` → `Im 𝔙` (S-leak) | `Q_β` (CAL-2) `c₃` | the monodromy-datum keystone (this audit) | structural laws proved; **the map is open** |

**Mass and binding run on the bar-EVEN face — not on Φ_b.** Φ_b is the bar-ODD
(decay) carrier; its target is `Q_β`, and the missing piece is the monodromy datum
`z(q₀) → S`.

## 1. Proof-status inventory (7 files, all 0-sorry / 0-axiom)

| File | Φ_b object | Rigor | What is proved (sorry-free) |
|------|-----------|-------|------------------------------|
| `MathlibExt/FaddeevPhiBRealIntegral.lean` | `phiB` = genuine `def` (Bochner integral) | **constructed** | `phiB_self_dual`, `norm_phiB` (unitarity), `phiB_inversion`, `phiB_zero` |
| `MathlibExt/PhiBProd.lean` | `phiBProd` = product `def` | **constructed (Im b²>0)** | `faddeevPhi_phiBProd_substrate`: the product **inhabits** `FaddeevPhi` unconditionally at the substrate b-map |
| `MathlibExt/FaddeevQuantumDilogarithm.lean` | `FaddeevPhi` = §3b conjecture-`class` | **axiomatized** | derived zero-locus, ratio forms, `phi_b_quasiperiod` (the `q_b = e^{iπb²}` T3↔T1 bridge) |
| `QBeta/FaddeevModularDouble.lean` | `FaddeevModularDouble` = `structure` | **axiomatized** | `bar_parity_decomposition` (sinh/cosh split); σ-unitarity monoid; "bar-even unitary ⇒ involution"; `crossFactor` (cross-anchor = pure phase) |
| `QBeta/BarOddLadderShape.lean` | hypothesis-carrier `class` | **axiomatized (phenomenology)** | `eventually_sign_flip_S`, `unlevered` (`S·u³=A`), `hasDerivAt_S_at_qstar` |
| `MathlibExt/QuantumDilogarithm{,Infinite}.lean` | compact `Φ_q` (**mass face, not Φ_b**) | constructed | `qPochProd` cocycle + functional equation |

The strongest single result: **`PhiBProd.faddeevPhi_phiBProd_substrate`** — a
genuine inhabitant of the defining `FaddeevPhi` axioms, unconditional, on the
`Im b² > 0` branch. Uniquely among the framework's hard transcendental objects,
Φ_b is *not* a bare conjecture-class: it is a discharged one.

## 2. The gaps, in dependency order

**G0 — Branch mismatch (the sharpest, structural).** `PhiBProd` converges and is
proved on the **substrate branch** (`arg b = π/4`, `Im b² > 0`). The decay physics
(`Q_β`, the bar-odd `S`) lives at the **fibre saddle `|q| = 1` (real `b`)**, where
the product **diverges** and only the (un-formalized, un-integrable) contour
integral defines Φ_b. *Construction and physics sit on different branches.* Any
route to the observable must either (i) construct Φ_b on the fibre branch, or
(ii) transport the substrate-branch object to the fibre saddle — which is exactly
the monodromy datum (G3).

**G1 — Integrability + def↔contour identity.** The real-integral `def phiB` is
total by convention; convergence of `J(b,z)` is unproved, and `phiB = Φ_b`
(the contour object) is only the `8e-29` numerical pin (P1–P4), not a theorem.
These block promoting the sorry-free *structural* laws to *analytic* facts.

**G2 — The fibre-regime construction.** No convergent construction of Φ_b at
`|q| = 1` (real `b`). This is the one clean, well-posed open analytic target, and
it is the branch the physics needs (G0). Candidate tool: heat-kernel / theta
representation (§4).

**G3 — The argument-identification / monodromy datum `z(q₀) → S` (THE keystone).**
No `FaddeevPhi` argument has been exhibited whose archimedean evaluation
reproduces the anchor targets `S(muon) = +0.00968298`, `S(proton) = −0.03945936`.
Per [`2026-07-12-fibre-observable-categorical-not-analytic.md`], the fibre→observable
passage is **not analytic continuation** but a **categorical Stokes / monodromy
datum** (an irregular q-difference connection). So the missing object is not a
resummation *constant* — it is a **monodromy** (Stokes automorphism). This is the
load-bearing gap; everything else is upstream plumbing for it.

**G4 — `decay = binding` is conjecture-conditional.** Φ_b touches binding *only*
through the claimed channel identity `bar-odd = Im 𝔙 = decay = binding`
(`conj:binding-qbeta-complex-volume`; the H₃ Gram negative-norm ghost mode). The
algebra is unconditional; the identification is not. No production binding number
consumes Φ_b.

## 3. What mass and binding actually run on (verified)

- **Mass:** `computations/canonical_mass.py`, `mass_vol_density.py` build the muon
  anchor from `Vol(4₁)` directly (`m_μ = m_e·Vol(4₁)/ℏ_q²`) and the proton from
  the Borel factor `F_Bor`. **Zero `phi_b` references.** The muon knot `4₁` is
  **amphichiral ⇒ zero bar-odd part**, so Φ_b is structurally absent from mass *by
  design*. The only dilogarithm in mass is the compact bar-even `Φ_q` backbone.
- **Binding:** goes through the **bar-EVEN** `conj:algebraic-geometric-dilog-equivalence`
  (`AlgebraicGeometricEquivalence` class): `Φ_n(x;q) → D(z) = Vol_hyp`, JSJ
  piecewise volume sum. **Item 1 (pole-cusp bijection) is proved sorry-free**
  (`pole_cusp_bijection_proved`, renamed 2026-09-14 to `denomPolyLocal_roots_explicit`); items 2–3 are conditional on two fields — the
  volume-conjecture saddle asymptotic (`vc_asymptotic`, a *theorem* for `4₁` by
  Ohtsuki / Andersen–Hansen) and the matched-cusp identification
  (`pole_cusp_matched` = `conj:shared-denominator-cusp-holonomy`). So binding's
  Φ-dependence is on the **real-volume** face, conjecture-conditional but with the
  pole side proved and the 4₁ asymptotic a literature theorem.
- **All Φ_b consumers in `computations/`** are probes + witnesses
  (`phi_b_evaluator.py`, `phi_b_substrate_regime.py`, `qbeta_c3_phib_*`,
  `qbeta_fmap_phi_b_*`, `qbeta_phi_b_real_form_pin.py`). None is on a production /
  registry path. Registry `ck-dk-canonical-registry.md` has **no** Φ_b entry.

## 4. Narrowing the monodromy datum (G3) — existence / uniqueness / constructive

The keystone is a *monodromy datum* (Stokes automorphism of an irregular
q-difference connection), not a constant. Three corpus-grounded levers narrow it —
each attacks a different one of existence / uniqueness / constructive:

### 4a. EXISTENCE — heat kernel / quantum theta (attacks G2 + G0)

The non-compact quantum dilogarithm is a ratio of **quantum thetas**, and the
q-theta / q-Gaussian is the fundamental solution of a **q-heat equation** — the
corpus already carries this machinery
([`q-heat-kernel-analysis-intro.md`](../../content/quantum-observable-universe/information-theory/q-heat-kernel-analysis-intro.md),
[`q-gaussian-solves-q-heat.md`](../../content/quantum-observable-universe/information-theory/q-gaussian-solves-q-heat.md)).
A **theta representation of Φ_b** gives existence on the *fibre branch* `|q|=1`
via the heat semigroup, precisely where the product diverges (closes G2, and
transports across G0). This is the concrete first probe: test whether the
substrate-branch `phiBProd` and a q-heat-kernel theta ratio agree, and whether the
theta ratio survives the `|q|=1` limit the product cannot.

### 4b. UNIQUENESS — the pentagon (5-term / "cubic") relation (rigidity)

Faddeev's Φ_b satisfies the **pentagon (5-term) identity**, and — with
**inversion + unitarity + modular invariance** (all already proved in our Lean:
`phiB_inversion`, `norm_phiB`, `phiB_self_dual`) — the pentagon **rigidly
determines Φ_b uniquely** (Faddeev–Volkov / Faddeev–Kashaev rigidity). Corpus
pentagon infrastructure: [`dim-master-pentagon.md`](../../content/quantum-observable-universe/mass-theory/dim-master-pentagon.md)
(DIM master pentagon), [`archimedean-functor-uniqueness.md`](../../content/quantum-observable-universe/mass-theory/archimedean-functor-uniqueness.md).
**Consequence for the keystone:** the monodromy datum is *unique* if it satisfies
the pentagon — so the search is not "find a function" but "verify the pentagon
pins the already-proved structural bundle." This converts G3 from an existence
hunt into a **rigidity check**: add the pentagon as the missing structural law,
and uniqueness follows. This is the highest-leverage Lean target after G2.

### 4c. CONSTRUCTIVE — the monodromy datum **is** `Δ_ω` (alien calculus)

**The monodromy datum is not merely *related* to the alien derivative — it is
what `Δ_ω` computes.** Precisely, from the corpus's own resurgence definitions
([`ecalle-borel-resummation.md`](../../content/quantum-observable-universe/appendix-surreals-archimedean/ecalle-borel-resummation.md),
§"alien derivatives and the bridge equation"): the **bridge equation**

$$\Delta_\omega \tilde f \;=\; A_\omega\,\frac{\partial \tilde f}{\partial z}$$

ties the **alien derivative** `Δ_ω` (a derivation reading the Borel-plane
singularity at `ω`) to the ordinary derivative, with scalar `A_ω` the **Stokes
constant** at `ω`. The collection `{A_ω}` **determines the Stokes automorphism —
i.e. the monodromy** — of the irregular q-difference connection. So:

> **monodromy datum ≡ Stokes automorphism ≡ `{A_ω}` (Stokes constants) ≡ the
> content read off by the alien derivatives `Δ_ω`.**

The identification pins the whole keystone concretely:

- **The datum for the S-leak is `A_ω` at the leading singularity** `ω`, computed
  by `Δ_ω log Φ_b` at the fibre saddle. `S = Im 𝔙` is the archimedean evaluation
  of that Stokes constant at the substrate anchor.
- **The leading `ω` is the complex volume** — `ω ≈ Vol(4₁)/π ≈ 0.646`, which is
  **exactly PR #3683's κ-tower Borel action `A ≈ 0.646–0.657`**. The odd-channel
  `A_ω` and the even-channel Borel singularity are the *same* resurgent datum read
  on the two bar-parity faces. This is why the two programs are one object seen
  twice (audit §0 table).
- **This is where my PR #3737 q-Borel scan bottomed out:** the S-ladder singularity
  is resurgent and the Stokes constant `A_ω` was unresolvable at `k=21` (the
  finite-n shadow). `A_ω` needs the *bridge equation* structure, not just more
  terms — which is exactly the alien-calculus route, PR #3683's machinery.

So **G3 = compute `A_ω` via `Δ_ω`**. This is the constructive route, and it is
literally the resurgent program — coordinated with #3683 (even face) applied to
the odd face.

### 4e. TWO-ROUTE RIGIDITY — quantum modularity / the Habiro ring (the strongest lever)

The keystone has been attacked from **two independent routes that construct the
same fibre-branch Φ_b**: the **analytic** route (#3773 — the contour-integral
`phiB`, transcendental, carrying the resurgent Stokes phase) and the
**combinatorial** route (#3768 — the finite `∏(1−xζ^k)=1−x^N`, exact algebraic at
roots of unity). Their agreement where they overlap is **not a redundancy — it is
a rigidity constraint**, and it is exactly **quantum modularity**
(Garoufalidis–Zagier): the Kashaev / quantum-dilog object has both a *perturbative*
(`Vol + iCS` + resurgent) expansion **and** an *algebraic root-of-unity*
evaluation, whose compatibility **pins the Stokes constants `{A_ω}`**.

**Consequence for G3.** The combinatorial route makes the monodromy datum
**algebraic at `ζ_N`**; the analytic route makes it **transcendental at `q₀`**.
Quantum modularity identifies them, converting *"compute the resurgent `A_ω`"*
(§4c, hard) into *"the algebraic `ζ_N` values + analyticity + pentagon rigidity
(§4b) **force** `A_ω`"* — an **anti-fit** determination (the datum is derived from
arithmetic rigidity, not inverted from an anchor).

**Corpus home — the Habiro ring.** This two-face structure *is* the Habiro ring
(functions defined at all roots of unity with compatible Taylor expansions), the
same structure as the **AJ identification** (`Φ_q`/`Li₂^q` = one `Â_K` at real vs
root-of-unity saddles, `phi-q-aj-machinery-identification.md`) and the **Q_β
Habiro element** (α_EM PR #1511 `[2]_q·(1−h²α)`; the Q_β Habiro chain,
`docs/coordination/2026-06-03-qbeta-habiro-chain-1-scope.md`). So G3 reframes from
"resurgent computation (with #3683)" to "**quantum-modularity / Habiro-ring
rigidity**" — for which the corpus already carries partial machinery. **This is
the most promising forward lever**, and it is only visible *because* both routes
were built: the combinatorial route (this PR) is what makes the datum algebraic,
which is what makes quantum-modularity rigidity applicable.

### 4d. The narrowing, assembled

- **Existence** (that a Φ_b lives on the fibre branch): heat-kernel theta ratio.
- **Uniqueness** (that it is THE Φ_b, hence its monodromy is forced): pentagon
  rigidity on the proved inversion/unitarity/self-duality bundle.
- **Constructive** (the actual `S` value): alien-derivative / Stokes automorphism
  (resurgent, with #3683).

If existence + uniqueness land, the monodromy datum is *determined* (not fitted) —
and its archimedean evaluation is `S`, the anti-fit-safe route the corpus demands.

## 5. Prioritized next steps

1. **(this session, probe)** Heat-kernel / theta-ratio existence probe for the
   fibre regime (§4a) — the one clean, well-posed open analytic target (G2), and
   the branch physics needs (G0).
2. **(Lean target)** Add the **pentagon** law to the Φ_b bundle and check
   Faddeev–Volkov rigidity (§4b) — converts the keystone to a uniqueness/rigidity
   statement.
3. **(with #3683)** Alien-derivative / Stokes computation of the datum (§4c) —
   the constructive `S` value, resurgent.

**Discipline.** None of this wires a `c_k` or an `S` value to production; the
anti-fit rule stands — a monodromy datum *derived* from pentagon rigidity +
resurgent Stokes is a derivation, an inverted anchor is a fit. The keystone stays
a conjecture until the datum is genuinely determined.

## Cross-references

- Φ_b Lean: `FaddeevPhiBRealIntegral`, `PhiBProd`, `FaddeevQuantumDilogarithm`,
  `FaddeevModularDouble`, `BarOddLadderShape`.
- Bar-even keystone: `conj:algebraic-geometric-dilog-equivalence`
  (`mass-theory/algebraic-geometric-dilog-equivalence.{md,lean}`).
- S-leak target: [`2026-07-11-qbeta-c3-barodd-sleak-phib-target.md`](2026-07-11-qbeta-c3-barodd-sleak-phib-target.md);
  categorical passage: `2026-07-12-fibre-observable-categorical-not-analytic.md`;
  ladder capstone: `2026-07-12-c3-wall-resolution-capstone.md`.
- Route memo: `2026-07-11-phib-lean-route-memo.md`. Sibling resurgent program:
  PR #3683 (κ-tower Borel / alien calculus).
