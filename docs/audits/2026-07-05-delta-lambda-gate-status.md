# Δ_λ per-isotope binding gate — current honest status + productive directions

**Date:** 2026-07-05 (compiled) · **Type:** READ-ONLY status synthesis. No corpus
edits, no compute rewire, **no seventh fit-based ansatz** (the Δ_λ gate stands).
**Discipline:** every negative below is classified **(a) scope-limited** ("this
construction, *alone*, does not reproduce the numbers as-is") unless a **proved
invariant** licenses **(b) structural exclusion** — cited when it does. Per
AGENTS.md §"Before declaring open / refuted".

This note refreshes [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md)
after ~7 weeks of work. It is a status update for any agent picking up Track A,
and it is deliberately not a closure attempt.

---

## 0. Verdict — has anything moved?

**Yes, substantially — but the gate remains OPEN. No light nucleus (D, T, ³He,
⁴He) is honestly closed.** The movement is of three kinds:

1. **The gate was REFRAMED, not closed** (cheat-sheet §9.3, 2026-06-02/-03). The
   canonical trace-difference binding `B = E₀·(|tr_M^free| − |tr_M^atom|)` is
   **intensive** (saturates at ~3–4 MeV); nuclear binding is **extensive** (∝A).
   No per-block *density* `Δ_λ` can turn an intensive quantity extensive — which
   is *why* the six ansätze all failed. The closure is not "a density to
   multiply" but an **additive many-body series over inter-nucleon bonds**
   `B(K) = Σ_{b∈⋈_K} B_b + (higher-body terms)`. This reframing and the
   Option-E/keystone frontier **converge** on the same object (§3): whatever
   supplies the missing binding must inject **per-block content beyond the Jones
   trace of β_K** — the knot-ideal projector `W_λ`.

2. **The search was NARROWED by three new proved-invariant (b) exclusions**
   (§2). The sign leg is now structurally closed; a magnitude-adding ingredient
   is now *proved necessary*. These are genuine milestones — they retire whole
   families of ansätze without fitting.

3. **Two durable structural wins landed** (§2): the **binding SIGN** is now
   resolved parameter-free by the counit *defect* structure (2026-07-04), and the
   **A=4 locality** is now a proved + measured prediction (SU(4) supermultiplet
   gate, PROBE 2). Neither closes the magnitude; both sharpen where the open piece
   lives.

**Bottom line unchanged from 2026-05-18:** the productive directions are still
GAP-A-3/A-4 (categorical brane-tower level selection / `ρ` general rule → the
`W_λ` object) and Option-E via the **A=4 interface operator (PROBE 2)**. What
changed is that both now have Lean-formalized falsifiable gates and a proved
locality signature, and the six ansätze plus the pure Markov re-decomposition are
all anchored refutations so the next session does not re-walk them.

---

## 1. Corpus-grep checklist (four paths) — none empty

Per AGENTS.md §"Before declaring open", all four paths run on {Δ_λ, per-isotope
binding, brane-tower, Option-E, W_λ}. **None returns empty.** This item is
heavily worked; the sections below synthesize extant results, they do **not**
declare anything newly "open".

- **`docs/audits/`** — dense. Load-bearing: the gating-context doc; the two
  2026-07-05 companion state reports (`…-brane-tower-per-lambda-weight-delta-lambda-state.md`
  bean `zqyl`, `…-delta-lambda-ansatz-refutations-anchored.md` bean `b9ra`); the
  ℓ¹-ceiling prune (`2026-06-28-delta-lambda-l1-ceiling-sign-only-prune.md`); the
  KL-positivity prune (`2026-06-16-option-e-probe4-kl-positivity-prune.md`); the
  counit candidate (`2026-07-04-delta-lambda-counit-canonical-integral-candidate.md`);
  the deuteron dressing (`2026-07-04-deuteron-dressing-is-proton-net.md`); the IMME
  (`2026-06-29-delta-lambda-imme-askey.md`); the 9b probe series
  (`2026-07-02-9b-probes-*.md`); the A=4 scoping (`docs/scope/2026-07-05-gap-a4-interface-operator-attack-scoping.md`).
- **`content/`** — `braids-and-knots/rho-k-h3a-refinement.md` (Δ_λ formal
  definition), `conj-rho-prefactor-structural.md` (GAP-A-4), `mass-theory/magic-A-binding-formula.md`,
  `mass-theory/deuteron-binding-dressing-proton-net.md`, `mass-theory/bar-parity-split.md`,
  `particle-interactions/qbeta-counit-transition.md` + `qbeta-counit-closed-form.md`.
- **`computations/`** — the six-ansatz probes (`rho_k_h3a_{co_casimir,crystal,lp_dual,frobenius_pairing,wenzl_bridge,refinement}.py`),
  `rho_k_h3a_counit_canonical_integral.py`, `rho_k_counit_defect_form.py`,
  `probe_9b_perlambda_brane_tower.py`, `option_e_a4_full_reconciliation.py`,
  `kl_betti_cell_dependence_probe.py`, `delta_lambda_imme_triplet.py`.
- **`docs/coordination/`** — [`option-e.md`](../coordination/option-e.md) (the
  Δ_λ master ledger, v1..v9 + PROBE 1–4 + prunes + A=4 non-closure) and
  [`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) (the `W_λ` object).

---

## 2. What is proved / refuted-and-scoped / open

### 2a. Proved (permanent contributions — "inaccurate alone" ≠ "excluded")

| Object | Status | Where |
|---|---|---|
| Per-bond Hecke factors `z, z−h, z−h/2` (typed-crossing operators) | **Lean-exact** | `def:typed-crossing-operator`; `nf-qvalues.witness.json` |
| Proton/neutron NF net coefficients `net(p)=1−h/2`, `net(n)` | **derived** (typed-crossing + exact Hecke NF) | `borromean-quark.md`; `nf-qvalues.witness.json` |
| `Δ(net)=−h·net(p)`, `Q_β=|Δ(net)|·E₀=E₀·h·net(p)`, `B_D=E₀·net(p)·Δtr=Q_β·Δtr/h` | **Lean-exact** (conditional on `[BorromeanQuark]`) | `QOU.Mass.DeuteronBindingDressing` |
| `Δ_λ = sgn(w₀^{S_{λ'}})·dim` = magnitude(=Wedderburn dim, chirality-invariant) × chirality sign | **Lean-proved sorry-free** | `S5SO3FiberAction.lean`: `deltaSign_sq_one`, `binding_magnitude_eq_dim`, `deltaSign_mixed`, `electron_block` |
| Borromean τ pipeline scalar τ = \|tr_M(β_Bor)\| ≈ 0.998562, carried through `g(x)=−Li₂^q(−x)` | **derived, cross-checked** 3.3e-16 | `borromean-binding-recompute.witness.json`; `2026-06-28-brane-tower-formalize-first-plan.md` §2 |
| Wedderburn closure `Σ_λ y_λ χ^λ(β_D) = tr_M(β_D)` (the ONE hard constraint on any Δ_λ) | **exact** (residual 4.8e-52) | `probe_d_delta_lambda_terms.py` |
| `10A−5 = 5·(2A−1)` residual bookkeeping (chain units) | **Lean sorry-free** (as a *bookkeeping identity*; NOT a global law) | `QOU/Mass/BindingResidualExponent.lean`, `QOU/BraidKnot/DeltaLambdaExponentKeystone.lean` |
| IMME degree-2 form: residual `log_{q₀}Δ_λ = a(A)+b(A)T₃+c(A)T₃²`, `Δ³=0` (Wigner rank-≤2 / Askey–Racah cutoff) | **Lean sorry-free** (exact algebra) | `QOU/BraidKnot/DeltaLambdaIMME.lean` |
| SU(4) `[1^A]` supermultiplet dim `= C(4,A)`, **zero iff A>4** (⁴He-locality predictor) | **Lean sorry-free** | `QOU/MassTheory/SU4SupermultipletGate.lean` |
| Co-Casimir refutation (magnitude gap 4.5 m_e + wrong sign) | **Lean sorry-free** | `QOU/BraidKnot/DeltaLambdaRefutation.lean`: `coCasimir_refuted_deuteron`, `coCasimir_wrong_sign` |
| Keystone falsifiable gates (defect-cubic + heat-kernel ladder, `f_pn` bracket, `W_λ=W_{λ'}` conjugation) | **Lean sorry-free** (gates only) | `KeystoneG2Gate.lean`, `KeystoneG2LadderGate.lean`, `KeystoneFpnBracket.lean` |

**Two durable structural WINS since 2026-05-18:**

- **The binding SIGN is now resolved parameter-free** (2026-07-04). Both tr_M and
  the counit `ε(β)=Σ_λ χ^λ` are class functions → writhe-averaged, sign-blind; the
  absolute counit gives the **wrong** sign (`+4.927` vs target `−4.353` on D). But
  the **defect** form `ε(β_K) − ε(β_K^vac)` — isolating the signed interface
  crossings `⋈_K` via the exact factorization `β_K = β_K^vac·⋈_K` — is **negative
  for all four isotopes** (D −30.29, T −709.7, ³He −820.0, ⁴He −28488), the correct
  binding sign, **structurally, no fit**. This is the piece all six prior ansätze
  (tested on absolute/positive objects) lacked. Scope-(a) throughout; the sign
  mechanism is the durable win. *Referee caveat:* the object `Σ_λ χ^λ` is a novel
  repackaging of a classical Frobenius–Schur count, not the genuine 1-dim Hecke
  counit — state it as "TQFT counit against the handle element `ω=G⁻¹𝟙`", don't
  overclaim standardness.
- **A=4 locality is now a proved + measured prediction** (PROBE 2, 2026-07-05).
  The SU(4) `[1^A]` supermultiplet gate vanishes for A>4 (top closed shell), and
  the **measured super-pairwise excess peaks at ⁴He (2.093×) and returns to
  ~pairwise by ⁶Li (0.944×, where C(4,6)=0)** — a clean locality match. The
  ×5.10 ⁴He magnitude gap is pinned as a **missing ≥4-body, ⁴He-LOCAL term** — not
  a weight, not sign-fixable.

### 2b. Refuted-and-scoped

**The six ansätze** (anchored, scope-disciplined in `2026-07-05-delta-lambda-ansatz-refutations-anchored.md`):
all **(a) scope-limited** — Occam/LP-Plancherel/LP-Frobenius are *underdetermined*
(the LP cost is an unfixed DOF; two incompatible singletons λ=[5,1] Δ=−22.96 vs
λ=[6] Δ=−47.16); Demazure-fibre is *tautological* (Δ_λ~10⁻⁵, reproduces M_LO);
augmented-Markov is a *convention-dependent uniform prior*, not a measurement;
crystal-graph is a numeric WRONG_SIGN miss (sum/target −412.7 at q₀). **None
excludes the per-λ weight ingredient in general.**

**Three (b) structural exclusions — with cited invariants** (these are the new
narrowing):

1. **Sign leg of any KL-multiplicity crystal closure.** Target `Δ_λ=sgn·dim` is
   **mixed-sign** (Lean `deltaSign_mixed`, sorry-free; n=3: 1+/2−, n=6: 6+/5−); KL
   multiplicities `n^w_λ` are **non-negative** (KL positivity, engine-verified S₄,
   PR #2381). A `Σ_w n^w_λ·X_w` sum supplies at most magnitude `|Δ_λ|=dim`, never
   the chirality sign — the sign is exogenous. *(The magnitude leg is separately
   (a): KL left-cell Betti `B_λ` is **not cell-invariant** — `kl-betti-cell-dependence.witness.json`
   — so it has no canonical value, but it *contributes* ×2.0 on the deuteron:
   contributive-not-closing.)*
2. **Sign-only re-derivation ℓ¹ ceiling.** Triangle inequality bounds any
   sign/chirality reassignment by `‖c‖₁=Σ|y_λ χ^λ dim_λ|`; measured
   `‖c‖₁/|target| = {D 0.52, T 0.36, ³He 0.59, ⁴He 0.41}` — **< 1 for all four**
   ⟹ a **magnitude-adding** ingredient is *necessary* (Lean `DeltaLambdaL1Ceiling.lean`,
   sorry-free — decl `chirality_sum_below_target`).
3. **RAW (un-normalized) per-block tower divergence.** `χ^{(2,1)}² ≈ 3.977 > q₀ ≈
   1.110` exceeds the **proved** Li₂^q convergence radius `|z|<q`
   (`_li_2_q_util.py::li_2_q`) — forces the normalized `r_λ=χ^λ/d_λ` form.

**PROBE 4 (per-λ collapse-last tower), scope-(a) but decisive** (2026-07-02): the
*un-weighted* Markov re-decomposition `(y_λ, χ^λ)` of the same β_Bor trace through
the same `g` is **null to 6.6e-7** across ²H…⁵⁶Fe (Jensen gap over the block
spread O(10⁻⁶)). ⟹ the missing weight **cannot be a pure re-decomposition of the
Borromean trace**; it must carry new per-block content. This is the six ansätze's
wall hit from the other side.

**Option-E state** (`option-e.md`): deuteron NOT closed (the 2026-05-26 "closure"
retracted twice; best parameter-free = interface-knot+T3, −31%). A=3 mirror-pair
`(1+q)/2` is a **fit near-match** (PROBE 1 refuted: required 1.05372 ≠ (1+q)/2 =
1.05499 at the same pin). A=4 full 77-partition f^λ sum → −80.4% (needs ×5.10);
"584 closes A=4" refuted (single-partition scalar). KL-Betti ×2.0 not closing.

### 2c. The genuine open frontier (one paragraph)

The open object is a **single per-block weight `W_λ`** — the FR-restricted
knot-ideal projector `χ^λ·χ^λ(e_{K*})` / hyperbolic-volume enrichment — that
injects **content beyond the Jones trace of β_K**, and would simultaneously (i)
distinguish p/n at the trace level and (ii) close the binding normalization. The
sign is now solved (counit-defect structure), a magnitude-adding term is proved
necessary (ℓ¹ ceiling), the missing piece is proved ≥4-body and ⁴He-local (SU(4)
gate + 2.093× measurement), and the deuteron dressing `net(p)=(1−h/2)` is tied to
the already-derived Q_β counit (observation-tier +0.12%, conditional on
`conj:borromean-quark`, D-specific — cross-A fails −59…−90%, so A≥3 is a separate
extensive mechanism). Every closed-form per-block candidate (six ansätze + pure
Markov re-decomposition + counit `1/y_λ` + IMME residual) either misses on
magnitude or is a re-decomposition of the same scalar; the surviving candidate is
the **s5-so3 keystone `W_λ`**, whose remaining research content is its
**geometric derivation** (the colored Σ(2,3,5) WRT / `E_q(2)` q-Bessel index) plus
the **A=4 connected [1⁴] magnitude term** (the measured 2.093×). The gate stays
open because that geometric `W_λ` build is research-level differential geometry,
not because a new fit is missing.

---

## 3. The two productive directions — what each requires, honestly

### GAP-A-3 / GAP-A-4 — categorical brane-tower level selection / `ρ` general rule → `W_λ`

- **What it is.** GAP-A-3 (brane-tower level selection) and Δ_λ are the *same*
  per-partition-selector problem; GAP-A-4 (`conj:rho-prefactor-structural`) is the
  `ρ` general rule. Both reduce to the `W_λ` knot-ideal projector — the s5-so3
  keystone.
- **What has landed.** The keystone's falsifiable gates are now Lean-formalized:
  the **defect-cubic + heat-kernel ladder** gate (`a₂(n)=n144C`, with the
  falsifiable n=7 sign-flip discriminant; `KeystoneG2Gate.lean`,
  `KeystoneG2LadderGate.lean`), the **`f_pn ∈ (0.39479, 0.66067)` bracket** gate
  (`KeystoneFpnBracket.lean`, AME-exact 0.58776 strictly inside), and the
  **`W_λ=W_{λ'}` conjugation** symmetry (#2794). The Reeb=restriction scaffold is
  sorry-free (`S5SO3FiberAction.lean`). The Beasley–Witten Seifert–CS localization
  on S³/2I is identified as the construction mechanism (RT/Verlinde Plancherel
  weight `d_q²/D²` meets C1–C7).
- **Authorization (corrected 2026-06-26).** The hard core **G1** (the DG S³/2I
  equivariant-index build) is owner-**authorized** under the narrow 2026-06-19
  Subgoal-2 reversal (PRs #2503/#2524) — it is **not** owner-*gated*. The blocker
  is research-level differential geometry, not authorization. The Δ_λ "no seventh
  fit-based ansatz" rule still stands; the reversal does not reopen fit-based q₀
  derivation.
- **What it would require to advance.** Instantiate the published Beasley–Witten
  localization to produce an explicit `W_λ` index, then check it clears the four
  Lean gates (defect cubic + ladder, f_pn bracket, conjugation symmetry). This is a
  DG construction + MTC-matching + Lean Reeb=restriction discharge — a multi-session
  research build, not an agent-tractable one-shot. No fit is involved; the gates are
  the machine-checkable spec any candidate index must pass.

### Option-E via the A=4 interface operator (PROBE 2)

- **What it is.** The connected ≥4-body magnitude term that supplies ⁴He's
  missing binding, realized as the Markov trace of the closed antisymmetric `[1⁴]`
  SU(4) supermultiplet operator, *added* to the structured (`|χ|`-magnitude +
  chiral-sign) combiner — a **magnitude term**, not the refuted per-λ weight.
- **What has landed.** The formalize-first gate: SU(4) `[1^A]` dim `= C(4,A)`,
  zero iff A>4 (`SU4SupermultipletGate.lean`, sorry-free) — the degree/orbit-count
  vanishing that *predicts* ⁴He-locality. The narrow probe confirmed it: measured
  super-pairwise excess peaks at ⁴He (2.093×), returns to ~pairwise by ⁶Li — a clean
  locality match (not ∝ C(4,A), which peaks at A=2; it peaks at the maximally-bound
  α singlet).
- **What it would require to advance.** Compute the single connected `[1⁴]`
  operator magnitude and check it supplies the measured 2.093× at A=4 and 0 at A=6.
  This is the genuine untried lever with a clean provable gate already in place.
  The magnitude leg (2.093× ↔ the [1⁴] connected-operator value) is the
  multi-session follow-on; it is locality-consistency so far, **not** a magnitude
  closure. Do NOT run the wide combiner scan before computing the single gated term.

---

## 4. Anti-duplication — do NOT re-walk these

- Six ansätze (co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius,
  crystal-graph, augmented-Markov) — anchored refutations recorded, scope-(a).
- Option-E v9 `(1+q)/2` — PROBE 1 refuted as a fit.
- Extend KL to S₆/S₁₂ for Betti magnitude — PRUNED (KL positivity + `B_λ` not
  cell-invariant; ⁴He ceiling ~11 MeV).
- q-modular / Eisenstein / Klein / Bring pullbacks — refuted T9–T14 (q→1
  divergence, scope-(b)).
- Per-knot Vol / q-dim convention — refuted / hidden-DOF (Rule 14).
- "10³ color-tube" / "B_(10,2)=584 closes A=4" — unsubstantiated numerology /
  single-partition scalar.
- Counit `Δ_λ=1/y_λ` alone — refuted on sign; but the counit **defect** structure
  is the durable sign win (keep).
- The `10A−5` closed-form bookkeeping route — PROBE 1 refuted scope-(a).
- Any **seventh fit-based ansatz** — explicitly banned (AGENTS.md §Precision
  goals; caught by the three-calibration discipline review).

## 5. Key files

- [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — the original gate doc (Path A/B/C/D taxonomy)
- [`docs/coordination/option-e.md`](../coordination/option-e.md) — Δ_λ master ledger (v1..v9, PROBE 1–4, prunes, A=4)
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — the `W_λ` geometric object + falsifiable gates
- [`docs/scope/2026-07-05-gap-a4-interface-operator-attack-scoping.md`](../scope/2026-07-05-gap-a4-interface-operator-attack-scoping.md) — the A=4 probe graveyard + the one untried lever
- [`docs/audits/2026-07-05-brane-tower-per-lambda-weight-delta-lambda-state.md`](2026-07-05-brane-tower-per-lambda-weight-delta-lambda-state.md) / [`…-delta-lambda-ansatz-refutations-anchored.md`](2026-07-05-delta-lambda-ansatz-refutations-anchored.md) — companion state reports
- [`docs/audits/2026-07-04-delta-lambda-counit-canonical-integral-candidate.md`](2026-07-04-delta-lambda-counit-canonical-integral-candidate.md) — the counit-defect sign win
- [`docs/audits/2026-07-04-deuteron-dressing-is-proton-net.md`](2026-07-04-deuteron-dressing-is-proton-net.md) — `net(p)=(1−h/2)`, deuteron +0.12% observation-tier
- [`docs/audits/2026-06-29-delta-lambda-imme-askey.md`](2026-06-29-delta-lambda-imme-askey.md) — IMME degree-2 residual + Δ³=0
- cheat-sheet §9.3 [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) — the intensive-vs-extensive reframing
- Lean: `QOU/BraidKnot/DeltaLambdaRefutation.lean`, `QOU/BraidsAndKnots/DeltaLambdaL1Ceiling.lean`, `QOU/BraidsAndKnots/S5SO3FiberAction.lean`, `QOU/BraidKnot/DeltaLambdaIMME.lean`, `QOU/MassTheory/SU4SupermultipletGate.lean`, `QOU/.../KeystoneG2{,Ladder}Gate.lean`, `QOU/.../KeystoneFpnBracket.lean`
</content>
</invoke>
