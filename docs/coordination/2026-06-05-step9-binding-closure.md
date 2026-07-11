# Step-9 binding closure — coordination ledger (flag-bearer hub)

**Flag-bearer:** PR #1871 (`claude/confident-newton-R8lIx`), 2026-06-05.
**Workplan:** [`docs/workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md`](../workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md).
**Common infra everyone rows toward (use these, do not fork):**
- Per-step status table — [`canonical-derivation-cheat-sheet.md §0/§9`](../canonical-derivation-cheat-sheet.md) (the step-9 box).
- This ledger — sibling roster + direction + report-backs.
- Watcher queues — `todos/{proof,canonical,compute,detangler}-*-queue.json`.
- Precision dashboards — `onepb-status-dashboard.witness.json` (L1), `per-observable-100x-status.witness.json` (L2).
- Anchor regression: the magic-A ⁴He **+5.87% no-fit** number is the falsification target for any ρ·A / n=4 claim.

---

## 0. The direction (which way to row)

Binding is **extensive / additive many-body**, not a per-block density (Δ_λ-as-density is dead, cheat §9.3). The closure is:

$$B(K)=\sum_n B_n,\quad \text{body-order }n=\text{jet/vertical degree }n=\lambda_{\mathrm{SW}}^{(n)},\quad B_n=m_e\!\sum_{p\in\mathcal S_c^{\mathrm{hyp}}}\!\operatorname{Res}_p\lambda_{\mathrm{SW}}^{(n)}.$$

- **Many-body series = jet-order filtration.** 2-body / 3-body / 4-body are jet orders of one generating function `G(x;q)=Σ B_n x^n`.
- **Each term = SW period = residue sum** over **hyperbolic** link-components (non-hyperbolic ⇒ Vol=0).
- **Scale rule ρ·A is OUTPUT** of the q-difference equation `G(qx)=R(q,x)G(x)` (→ Dirac/SW PDE post-τ), **not a fit**.
- **γγ / Breit–Wheeler** = the A≥3 validation channel (bar-even C-even vs bar-odd difference).

---

## 1. Sibling roster + per-PR direction (report-backs appended here)

| PR / branch | Their problem | Which way to row | Report back |
|---|---|---|---|
| **#1784** | binding-link assignment heuristic, chain-vs-Borromean | link-volume = **hyperbolic components of `λ_SW^(n)`**; magic-A `8G` is the n=4 instance — the assignment is the hyperbolicity gate (L4), not a free choice | _pending_ |
| **#1790** | 3-body joint-trace destructive (honest negative for A=3) | don't treat A=3 in isolation — it's the **n=3 term of the body-order series**; the q-difference recursion (L3) couples it to n=2/n=4 | _pending_ |
| **#1778** | all-pairs combiner, A=3 to −13% | structure the combiner as a **body-order series** (2+3+4), not flat all-pairs; this is the additive-series host | _pending_ |
| **#1839** | Residue-A kernel deepening (Lean engine, SDP-zero) | residue-A may **BE** the SW-period residue `Res_p λ_SW^(n)`; align on one residue engine (L1) | _pending_ |
| **#1789** | nuclear-binding derivation-completeness ledger | register the **SW-residue / jet-filtration** framing as the active step-9b direction; share completeness metric | _pending_ |
| **#1762** | 1ppQ roadmap + VolDensity bridge + 5-option attack | step-9a per-knot `VolDensity` wire-up is C1 here; fold the SW-residue route in as the step-9b option | _pending_ |
| **#1811 / #1880** | Q_β fibre / c_3 generating-function recurrence | same **q-difference machinery** (L3); the binding `G` and the Q_β `c_k` recursion share the Habiro kernel — reuse `R(q,x)` extraction | _pending_ |
| **#1888** (GAP-A `gap-a-path-b-lambda`) | per-atom λ(K) substrate-derivability | **adjacent axis, reciprocal cross-link established** — 3 intersection points: per-knot `Vol(K)`, per-block-vs-global density gate, bar-odd binding-difference observable | ✓ cross-linked (their ledger ↔ this) |

---

## 2. The ask to every sibling

1. **Report relevant findings here** (append a row in §1 or comment on #1871) — esp. negatives that constrain the q-difference kernel or the hyperbolicity gate.
2. **Use the common infra above** (cheat §9 step-table + this ledger), don't fork a parallel status doc.
3. **Anchor to the ⁴He +5.87% magic-A number** for any n=4 / ρ·A claim.

_Append report-backs below this line._

---

## 3. Sibling intel folded in (2026-06-05, agent scope-pull) — two sharpenings

Coordination comments posted on #1765, #1839, #1778, #1789, #1762.

**Sharpening 1 — the SW-period residue already has a zero-param form (#1765).**
The selection rule `λ(L) = (1/(c+1))·Σ_{λ⊢c+1} dim_q` reproduces the muon (c=1, exact ∀q) and proton (Family-A, c=3) anchors exactly. This **is** the SW-period residue (link components → partition rank → quantum-dim trace). Lemma **L1 is therefore not new** — it must be shown *equivalent* to #1765's rule, and the open *"why rank = c+1"* = the **body-order grading** (`c+1` = body order = jet vertical degree). #1765's planned A-polynomial saddle for ³He/⁴He = our n=3/n=4 SW periods.

**Sharpening 2 — the q-difference kernel must be FIBRE-derived, not data-extracted (#1839, #1811).**
#1839's precision-floor result `σ(c_k)=σ_R/u^k` makes c₄⁺ **unmeasurable**; #1811 shows residue-A is fibre-level and **rigid** (2.5×10⁷× scale-invariant). ⇒ **C5/L3 revised**: derive `R(q,x)` from the **fibre root-of-unity singularity structure of λ_SW**, NOT by fitting `B_n`/`c_k` data. Extraction is data-blocked above c₃ (#1880 closed that axis).

**Caveat — link-volume not 100% derivable (#1789, #1790).** The 3-body residual (~13%) is **genuine many-body** (NOT joint-trace, refuted #1790), and the link-volume superposition interface can't be fully derived. Lemma **L4** must treat the n=3 SW period as an irreducible many-body term, not a missing weight.

**Compatible/adjacent:** #1733 (r=15 q-Pochhammer ⁴He +1.79% — candidate n=4 refinement, "is r=15 structural?" open), #1808 (Markov stabilization = the body-order n:2→3 induction functor), #1811 (fibre infra + Hopf c₃ source).

---

## 4. Report-back from #2089 (2026-06-10) — per-bond kernel DERIVED (fibre-level), form bug identified

Per §2 ask. Branch `claude/derive-10A-minus-5-2026-06-10`; audits
`2026-06-10-binding-gs-filtration-multiplicative-suppression.md` +
`2026-06-10-binding-bond-graph-compute-audit-and-derivation.md`.

**Finding (positive instance of Sharpening 2).** The inter-nucleon bond's
trace kernel is **fibre-derived, not data-extracted**: each bridge crossing
`c·σ+d` contributes its Markov conditional expectation

    f_bond(q) = c·z + d ,  z = √q/(q+1)
    f_pp = z ,  f_nn = z − h ,  f_pn = z − h(½ − δ/4)

(formal q; only archimedean step is q→q₀). Validated: `∏_chain f_bond` ==
measured `tr_atom/tr_free` to 1.1e-15 on D/T/³He/⁴He. The GS NF is binomial
over bonds (`C(A−1,k)` term counts; bridges far-commute).

**Form bug (mechanism of the 5–40× undershoot).** `tr_atom = tr_free·∏f_bond`
⇒ the linear `Δtr` SATURATES (B = Q_β·Δtr bounded by ~0.78 MeV, never
extensive); the extensive invariant is `log(tr_free/tr_atom) = Σ_bonds
log(1/f_bond)` — the §1/#1762 `log|tr_M|` scale-gate observable, now
mechanistically derived. Log-ratio binding at E_0 lands 0.57–2.36× (chain) /
0.57–1.20× (complete graph) vs 4.8–39.7× linear.

**Caveat honored (§3 many-body).** Per-bond energies are substrate-fixed
(pp 2.91 / pn 3.89 / nn 5.18 MeV); the open piece is the **edge set**
(chain under-binds, complete over-binds light nuclei; D anomalously loose,
⁴He doubly-magic) — consistent with §3's "genuine many-body" residual; NOT
re-claimed as a closure, no 7th ansatz.

**Infra delivered.** Lossless per-λ χ caches D/T/³He/⁴He (matrix-M `max_dim`
cap purged — it was a silent ~1e-3 truncation; producer lossless by default),
⁴He via Rust `chi_q_via_gp` (77/77, 3.1s); ⁵Li/⁶Li in flight. Cross-posted:
#2062 (kernel handoff), #2078 (scale-gate corroboration + A=4 χ), #2090
(depth-1 Z_q kernel sibling on the c_k axis).

---

## 5. Report-back from #2612 (2026-06-23) — lever-1 selection-rule unification + coordinate

Branch `claude/bold-mendel-5994kg` (rebased onto main +119). Three Δ_λ-gate
levers worked (audit `2026-06-23-delta-lambda-three-lever-status.md`):

- **Lever 1 (kernel R(q,x)) — algebraically closed.** The depth-2 `det=1`
  kernel `R=x²−τx+1` (proved: S₅/A₅ Schur + symplectic) is generated by ONE
  selection rule `lw(c)=(1/(c+1))·Σ_{λ⊢c+1} dim_q` via the canonical q-hook
  `dim_q`: `lw(1)=1`, `lw(2)=(q+1)²/(3q)` (c=2 Hopf, **derivation-tight** —
  closes the former gate, not fabricated), `lw(3)=Family-A` (= production
  `linking_weight_family_a` bit-for-bit). `τ(q₀)=2.6424`. Producer
  `binding_selection_rule_tau_closure.py`. **Residual:** the geometric↔algebraic
  identification `a_D^(n)=lw(n−1)` = the **W_λ geometric-origin frontier of
  #2488** (SW period = selection-rule value); owner-gated DG, NOT touched here.
- **Lever 2 (edge-set).** Pauli→pp/nn-unbound formalized
  (`QOU/Hecke/PauliChannelBinding.lean`, sorry-free). Z·N count + deuteron
  magnitude still gated.
- **Lever 3 (universal-ρ).** A=3 mirror **ratio** is a ρ-free prediction
  (1.67%, no fit); absolute ρ fitted/CAL-4-gated (= the Δ_λ gate per-λ).
- **Mass + binding wiring.** `lw(c)` wired into MBA step-9a (mass linking
  weight) + step-9b (binding kernel anchors).

Coordinated (intent posted): **#2488** (keystone W_λ — my residual = their
frontier), **#2325** (parallel depth-2 b-ladder + `m_sym` log-trace match),
**#2461** (Pauli-channel — `PauliChannelBinding` cherry-pickable). Over-zealous
binding-closure prose rescoped in 6 docs
(`2026-06-23-over-zealous-binding-closure-review.md`).

---

## 6. Report-back from #2795 (2026-06-25) — the depth-2/super-exp fork SETTLED + conserved-integral Lean

Branch `claude/sw-lambda-jet-prolongation-2026-06-25` (rebased onto main +34).
Refines §5's "Lever-1 kernel R algebraically closed": the depth-2 `R=x²−τx+1`
is closed **only at n≤4** (deuteron n=2, ⁴He magic-shell n=4); the **global**
`a_D^(n)` is **super-exponential**, so the true kernel is q-Bessel, not SL₂.

- **Fork settled three ways** (audit `2026-06-25-sw-jet-prolongation-explicit-and-fork.md`,
  probe `sw_period_growth_probe.py`): (i) √-branch Puiseux `X^(n)~(z−z_k)^{1/2−n}`
  ⇒ factorial; (ii) the corpus's own `prop:sw-period-residue-sum` — residues =
  per-block Wedderburn `dim_q` ⇒ `a_D^(n)=Σ_λ dim_q = lw` (the §5 selection rule,
  stated by the corpus); (iii) the Lean below. lw vs depth-2 split hard at n≥6
  (13.56 vs 11.62).
- **Jet-form caveat RESOLVED from corpus** (corpus-grep over-flag): `λ_SW^(n)` is
  a meromorphic 1-form (`prop:sw-period-residue-sum`); `prop:mi-sw-abelianisation`
  bridges the fuller `J^n` MI∫ tensor to the 1-form period.
- **Lean keystone** `prop:sl2-period-conserved-quantity` (content-block,
  `QOU.Mass.sl2Invariant_succ`/`_eq_zeroth`, sorry-free, generic `[CommRing R]`):
  the depth-2 recurrence's **conserved first integral**
  `H_n = a(n+1)²−τa(n+1)a(n)+a(n)²`, `H_n=H_0`. A super-exp period has `H_n→∞`
  ⇒ no first integral ⇒ **no depth-2 recurrence** — the formal reason the SL₂ τ
  is the n≤4 germ. Verified lean-direct exit 0.

Coordinated (intent posted): **#2800** (`lever1-keystone-na-stokes-3b` — parallel
Lean: their `BindingHyperbolicRecurrence`/`BindingJacobiAngerBridge` `τ²−4` conic
is the level-set side of my `H_n` invariant; no file collision content-block vs
`QOU/Mass/` lib; consolidation question = who proves the orbit integral, posted).
**#2793** (τ [2]_q assembly — coordinated 3×, Lean-landing noted). The geometric
origin `a_D^(n)=lw(n−1)` (= SW period ≡ selection-rule value) remains the
**#2488 W_λ DG frontier**, owner-gated, untouched here.

---

## 7. Report-back from #2822 (2026-06-26) — the binding period IS the q-deformed involution number (q-Hermite moment)

Branch `claude/z2bn-qbessel-lw-exactness-2026-06-26`. Identifies WHAT the super-exp
period of §6 is, sharpening the z2bn kernel target. Audit-only probes, no fit.

- **IDENTIFICATION (verified, q→1 exact n=1..12):** `T_q(n) := Σ_{λ⊢n} dim_q(λ) =
  n·a_D^(n)` satisfies `T_q(n) → I(n)` (involution/telephone numbers A000085) as
  `q→1`, via the classical `Σ_λ f^λ = I(n)`. **⇒ `a_D^(n)=lw(n−1)` is the
  q-deformed involution number `I_q(n)/n` = a q-Hermite / Rogers–Szegő moment.**
  Structural home = #2800's `BindingQHermiteOscillator`. Explains the super-exp
  growth and the depth-2-with-n-dependent-coefficient structure
  (`I(n)=I(n−1)+(n−1)I(n−2)`, why constant-coeff SL₂ fails).
- **Prune (a):** not a single Bessel-½ falling factorial `∏[1/2−k]_q` (ratio
  decays monotonically) — `lw` is the residue SUM over Wedderburn blocks
  (`prop:sw-period-residue-sum`); the falling factorial is the per-block period.
- **Prune (a):** not the naive depth-2 q-telephone `T(n)=T(n−1)+[n−1]_q T(n−2)`
  (exact n=3, drifts n≥4; no low-degree depth-2 q-holonomic in `q^n` closes,
  held-out best ≈1.5e-3). Exact q-coefficient ≠ bare `[n−1]_q`.

**z2bn kernel result (the FORK).** A high-precision q-holonomic search
(`sw_period_qholonomic_kernel_search.py`, held-out-verified, precision-independent
at 70/140 dps) finds **no low-order `R(q,x)`** (depth ≤3, deg ≤3) for the
quantum-dim period `T_q(n)=Σ_λ dim_q` — scope-(a), genuine non-closure. The clean
depth-2 kernel `μ_q(n)=μ_q(n−1)+[n−1]_q μ_q(n−2)` belongs instead to the
**crossing**-counted q-Hermite moment `μ_q`, which **forks** from `T_q` past `n=3`
(both →I(n) at q=1; differ 0.3%→7.9% over n=4..8 at q0). So the two q-deformations
of `I(n)` are **not** interchangeable: the selection-rule binding period is the
quantum-dim sum (no low-order kernel); the kernel-bearing object is the crossing
moment (`BindingQHermiteOscillator`, #2800). **Decision for z2bn:** higher-order
`R(q,x)` for `Σ dim_q`, or adopt the crossing moment as the physical binding
object. The bare `[n−1]_q`-bracket shortcut is pruned. Full audit: #2822.

---

## 8. Report-back from #3089 (2026-06-29) — `10A-5` slope test + bar-odd Z-correction (mirror cancellation Lean-proved)

Branch `claude/categorical-derivation-10a-5-85e945`. On the trace-canonical
residual `Delta_lambda = B_AME/B_pred` (`binding_canonical.py`, 7Li/7Be added;
probe `delta_lambda_z_coefficient_and_slope.py`). Audit
`2026-06-29-delta-lambda-z-correction-writhe.md`.

- **Slope test: `10A-5` is a light-nucleus (A<=4) artifact — REFUTED at A>=5
  (scope-(a)).** 6Li `log_q0 Delta = 36.1`, not the predicted 55; the slope
  collapses ~10->0.4 at the 4He shell (`B_pred` saturates ~0.7-0.8 while `B_AME`
  ~linear => `log Delta` logarithmic). Same saturation §4/#2089 flagged (linear
  `Dtr` bounded), seen from the residual side. Coordinated with **#3087**
  (chain-topology derivation of the integer `5(2A-1)` — arithmetic unaffected,
  only the global-law reading refuted).
- **Bar-parity split.** Symmetric sum `sigma+sigma^-1=10A-2` (bar-even, A-only)
  = leading; writhe `sigma-sigma^-1=4Z` (bar-odd, Z-only) = the Z-correction;
  decomposes `4Z = intra(3Z+N) + interface(Z-N)`.
- **Z-correction CONFIRMED at a 2nd mirror pair.** Proton-excess penalty -1.34
  (3He/T), -1.77 (7Be/7Li); SIGN derived from the p!=n intra-writhe seed (proton
  +3 > neutron +1), magnitude O(-1.5) open (no fit). Survives the leading-law
  collapse — independent parity channels.
- **Mirror cancellation Lean-proved** (`QOU.BraidKnot.mirror_baseline_cancels` +
  `crossing_sum_mirror_invariant`/`writhe_mirror_difference`, sorry-free): the
  bar-even baseline cancels exactly in a mirror difference given the additive
  `baseline(A)+zCorr(Z-N)` form (the only ansatz). Paper:
  `prop:mirror-baseline-cancellation` (mba sidecar). Not wired (near-match tier).

## 2026-07-11 — 𝓑_K coordination-number reading of M_n(A) (PR #3549)

- **Open multiplicity `M_n(A)` in `w_n(K)=M_n(A)·Vol_n(K)` = the coordination
  number of 𝓑_K (scope-(a), fit-free for A=3).** Reading `M_need=B_AME/(m_e·Vol)`
  off AME: non-magic A=3 pair gives `M_need(³H)=2.003`, `M_need(³He)=2.061` =
  the per-nucleon coordination number `z=A−1=2` (<3%, no fit). Doubly-magic ⁴He
  needs an extra `a_D^(4)≈2.53` (magic-shell only: `z·a_D^A` closes ⁴He +0.6%
  but overshoots A=3 +30%). Crossing number is the `Vol=0` deuteron (Hopf) survivor.
- **α-cluster extension (A>4):** ¹⁶O/⁴⁰Ca have no single hyperbolic link →
  `B(n_α)≈n_α·B(⁴He)+C(n_α,2)·b_αα`; per-bond `b_αα≈2.41 MeV` constant for
  simplex clusters ⁸Be/¹²C/¹⁶O, saturates n_α≥5 (⁴⁰Ca needs geometric packing).
  `b_αα` empirical (Hafstad–Teller), NOT derived — open.
- **Coordinated with #3534** (same `w_n` object, q-Hermite basis route): the
  single-term `M·Vol` `a_D`-magic-only finding vs their summed `Σa_D^(n)·w_n`
  extraction are different decompositions, not contradictory — logged so neither
  restates the other as refuted.
- **Coordinated with #3548** (W_λ connected multi-bond transfer matrix): my
  coordination bond-count `C(n_α,2)` and per-bond `b_αα≈2.41 MeV` are the fit-free
  empirical target their connected braid `tr_M` (PROBE 2) must reproduce; their
  deuteron connected gap 0.193 is the 2-body instance.
- Paper: `rem:bk-coordination-multiplicity` (interprets
  `conj:binding-manybody-eq-jet-filtration`). Not wired (exploratory tier).

## 2026-07-11 (cont.) — coordination-degree derivation status + α-contact forward (PR #3551)

- **z=A−1 derivation status (honest):** z=A−1 is the vertex degree of the complete
  cluster graph K_A — an EXACT graph fact, already verified in Mathlib
  (`complete_graph_degree`, `card_edgeFinset_top_eq_card_choose_two`,
  `sum_degrees_eq_twice_card_edges`). The identification "single-link multiplier =
  coordination number" is the BOND-EXTENSIVE hypothesis (a conditional class), NOT
  derived from the 13 drivers. So z=A−1 is proved-as-graph-fact / conditional-as-
  physics. QOU-library formalization deferred (ProofWidgets JS network-blocked in
  sandbox; follow-up, not shipped unverified).
- **α-cluster contact coordination FORWARD (A>4):** fix b_αα≈2.416 MeV from ¹²C/¹⁶O,
  predict from standard Brink deltahedral contact geometries — ²⁰Ne (sq-pyramid, 8)
  +0.10%, ²⁴Mg (octahedron, 12) +0.25%, ⁴⁰Ca (fcc-10, 24) −0.33%. One constant, <0.5%
  across A=12–40. ⁸Be = unbound-pair exception (single bond ≈0, triple-α gateway).
  C(n_α,2) overcounts for n_α≥5 → contact-graph edge count (kissing-number bounded).
- **#3548 coordination:** the forward contact-graph result is the concrete A=12–40
  target their connected two-α braid tr_M (PROBE 2) should reproduce; b_αα derivation
  remains their scope, not duplicated here.

## 2026-07-11 (cont.2) — α-geometry selection + bond-extensivity coordination (PR #3555)

- **α-geometry selection = contact-maximisation, PARTIALLY (scope-(a)):** N_need
  vs C_max(n_α) — ²⁴Mg (octahedron 12, exact) Δ+0.2, ²⁸Si +0.1, ⁴⁰Ca +0.5 MATCH
  the maximal-contact geometry (derived, not fit); ²⁰Ne DEVIATES (binds as 8, not
  max 9 — its prolate α+¹⁶O structure). CAVEAT: merged PR #3551 Part-2 ²⁰Ne
  geometry (sq-pyramid 8) was hand-assigned → one-bond DOF (recorded, not hidden).
- **Bond-extensivity (Task 2) is #3548/#3534 scope, NOT duplicated here:** the
  derivation of "binding = Σ_edges ε" (extensive) is #3548's connected multi-bond
  tr_M (PROBE 2) and #3534's linked-cluster w_n. My coordination-number angle only
  adds the graph handshake bookkeeping (Σ deg = 2|E|, in bean qou-4tj9's Lean).
  Coordinated on #3548 rather than building a parallel compute.

## 2026-07-11 (cont.3) — bond-extensivity: multiplier=coordination is the equal-weight limit (PR #3557)

- **"Why multiplier=coordination number" ANSWERED (scope-(a)):** bond-extensivity
  B=E₀·Σ log(1/f_bond) is DERIVED (#2089 log-trace); the coordination-number
  multiplier is its EQUAL-WEIGHT limit (equal bonds ⇒ B=(coordination)·const).
  EXACT for identical α–α bonds (α-cluster contact counting derived); FAILS at the
  nucleon level (derived ε_pp:ε_pn:ε_nn = 0.69:0.93:1.24, spread 1.78×) ⇒ nucleon
  z=A−1 is a composition coincidence (symmetric A=3 mirror only).
- **w_n=M·Vol decomposed:** M = equal-weight coordination skeleton; Vol = the
  isospin bond-energy asymmetry ε_nn−ε_pp=0.542 that equal-weight drops (the T₃
  carrier). Both grounded in the one derived log-trace.
- **Open → #3548/#3534:** the ε magnitudes (f_αα, E₀) + α-geometry remain open;
  ε-magnitude derivation is #3548 connected-tr_M / #3534 linked-cluster — not
  attempted here (uses #2089 f_bond, no new fit).

## 2026-07-11 (cont.4) — mirror split is Coulomb; #2089 kernel over-breaks charge symmetry 3× (PR #3564)

- **A=3 mirror split diagnosed as COULOMB (scope-(a)):** AME B(³H)−B(³He)=0.764 MeV
  = pp Coulomb displacement e²/(4πε₀r) at r≈1.9 fm (0.758 MeV); strong CSB residual
  ≈+0.006 MeV (charge symmetry holds ~1%; consistent with #3534's 2.73% Coulomb-
  corrected agreement). The #2089 log-trace kernel's pure-strong split
  E₀(ε_nn−ε_pp)=2.27 MeV is 3.0× the total / ~386× the strong residual — it
  OVER-BREAKS charge symmetry (f_pp=0.499 vs f_nn=0.290).
- **Fix direction:** charge-symmetric strong bond (f_pp≈f_nn) + separate Coulomb
  (Z(Z−1)/2 pairs). BONUS: collapses the 1.78× nucleon ε-spread ⇒ restores the
  equal-weight limit ⇒ coordination-number counting valid at nucleon level (#3557).
- **Two framings (owner call):** (A) spurious strong CSB vs (B) categorical EM
  overshoots Coulomb 3×. Not decided. Kernel re-derivation = #3548/#3534 scope.

## 2026-07-11 (cont.5) — mirror split is Coulomb across the chain; charge-symmetry constraint (PR #3570)

- **Generalises #3564 (scope-(a)):** the mirror binding split is Coulomb across A=3–39.
  Using the canonical shared Coulomb (Z(Z−1) discrete-proton self-energy, r₀=1.2 fm,
  coulomb_energy.mirror_displacement_mev — NO free parameter), split/ΔE_C=0.838±0.059
  (7% scatter) across 8 mirror pairs ³H/³He…³⁹K/³⁹Ca ⇒ split PROPORTIONAL to Coulomb
  (the ~0.84 factor is the known uniform-sphere over-estimate).
- **Constraint on the kernel (→ #3548/#3534):** any strong kernel (#2089 f_bond, #3548
  connected tr_M) must be charge-symmetric SYSTEMATICALLY; the #2089 kernel's 2.27 MeV
  A=3 strong split is 3× the whole observed A=3 split, at all A, not an A=3 accident.
  f_pp≠f_nn must be removed (or reinterpreted as categorical EM, framing (B)). Not a
  binding fit.
## 2026-07-11 — na-Stokes eigenfunction two-tier + wₙ derive-or-refute (#3545, #3534)

Branch `claude/q-stokes-kernel-eigenfunction-y0pso2` (#3545) + parallel
`claude/binding-wn-kernel-derive-refute-2026-07-11` (#3534, bean t7qv) — same
owner steer ("na-Stokes kernel informs the weight kernel via its eigenfunction
relation").

- **Two-tier eigenfunction, Lean sorry-free (#3545):** `a_D^(n)=S(n)/n`,
  `S(n)=Σ_λ dim_q` (q-involution #). `c₃=[2]_q` exact; deviation
  `q²·D(4)=(q−1)²Φ₃` (Habiro cyclotomic leading factor). File
  `QOU.Mass.BindingEigenfunctionTwoTier` (lean-direct exit 0). Cherry-pickable by
  #3534 (which states the same numerically, no Lean).
- **Adversarial (#3545):** `[n−1]_q` is 2 points not a pattern; "Habiro"=leading
  factor only (D(6..8) non-cyclotomic cofactors); `S(n)` **forks** from clean
  Rogers–Szegő / crossing moment `μ_q` (+0.3%→+7.9%) — clean q-Hermite/q-Fourier
  basis is μ_q's, not S(n)'s. So "eigenfunction informs kernel" = shared Habiro
  **ring**, not shared element (kehn c_k is a different ζ₄ localization).
- **wₙ(K) derive-or-refute (#3534 + #3545 correction):** raw T/³He split (9.9%) is
  **Coulomb** (= the ledger's writhe/Z-correction channel above) — on `B_strong`
  the mirror agrees ~2.7% (CSB), so body-order wₙ **admissible** (corrects my
  #3545 over-claimed (b) exclusion → (a)). No constant-ratio kernel closes to 5%
  ([n]_q² 6.9% lone near-miss); tuned recursion = banned 7th ansatz. Non-fit
  routes: q-Hermite-basis expansion (Habiro-dressed) / hyperbolic link-volume.
- **conj:binding-manybody-eq-jet-filtration: not provable now** (3 open inputs).

## 2026-07-11 (cont.) — #3545 ↔ #3548 connected-binding convergence (two lenses)

- **#3545 Part 10–11 ↔ #3548 same object.** Both compute the connected/cross-term
  (extensive) binding. #3548: connected `tr_M`(W_λ per block) = 0 for disjoint
  bonds, 0.855 for braided σ². #3545: negative-norm ghost Gram-quadratic
  `⟨g_i,g_j⟩_G` = 0 for split (traceless) ghosts, ≠0 when bonded. Independent
  convergence on "disjoint→0, bonded→nonzero"; ties to main `a44296db`
  (decay=binding-quadratic: mass=linear tr_M, binding=quadratic Gram).
- **#3545 derives bond-extensivity** (`B ~ self + (#bonds)·b*`, constant `b*`) from
  bond translation-invariance — upgrades #3549's conditional coordination-number
  hypothesis to structural. Justifies #3548 PROBE-2's constant multi-bond term.
- **Open bridge:** is #3548's deuteron connected 0.193 == #3545's
  `⟨g_A,σ_bond,g_B⟩_G`? If yes the two lenses unify + `b*` pinned (no duplicate H₆
  build). #3548 owns connected-`tr_M`/PROBE-2; #3545 owns the Gram-quadratic +
  bond-extensive derivation. Posted #3548#issuecomment-4948202747.

## 2026-07-11 (cont.6) — charge-symm + Coulomb benchmark FIXES the mirror split (PR #3575)

- **Diagnosis payoff realized (scope-(a)):** built charge-symmetric strong (all bonds =
  isoscalar f_pn) + separate Coulomb on D/T/³He/⁴He. FIXES the ³H/³He mirror split →
  0.998 MeV (Coulomb, uniform-sphere) vs AME 0.764 (1.3×), from the broken #2089 kernel's
  2.27 (no C) / 3.27 (double-count) MeV (3×). ~3× accuracy gain + removes EM double-count.
- **Absolute binding NOT closed:** D +75%, T/³He +38%, ⁴He −21% — the edge-set/E₀/
  connected magnitude (#2089 form bug), unchanged by charge symmetry.
- **ACTIONABLE OPEN STEP (ε-magnitude answer):** #3548 (merged 9c62f785) pinned the
  connected-(2,1)/SU(4) magnitude MECHANISM but is no-fit/no-closure AND still on the
  charge-BREAKING kernel (f_pp=z, f_nn=z−h). ⇒ re-run #3548's connected magnitude probe
  on the CHARGE-SYMMETRIC kernel (f_pp=f_nn=f_pn) + separate Coulomb. That is the path to
  absolute binding: charge structure (this PR) × connected magnitude (#3548 re-run).

## 2026-07-11 (cont.7) — charge symmetry ⊥ connected magnitude: the two levers DECOUPLE (PR #3577)

- **Re-ran #3548's connected magnitude on the charge-symmetric kernel (answers #3575's
  open step, scope-(a)):** the connected Ursell/Mayer |b_Ac| is charge-symmetry-
  INVARIANT — ⁴He 1.9614 (broken) → 1.9719 (symm), +0.5%; D +0.00%, ⁶Li +1.35%. Needed
  super-pairwise 2.093→2.120 (ceiling shift only); ~74% magnitude gap PERSISTS; SU(4)
  A=6 vanishing unchanged.
- **⇒ The two open binding levers are ORTHOGONAL:** charge structure (mirror split →
  fixed by charge-symm+Coulomb, #3564/#3570/#3575) vs connected magnitude (×2.09 /
  edge-set → #3548, unchanged by charge symmetry, still open). Absolute binding needs
  both; neither is the other. Clean structural separation of the remaining closure
  problem — the two can be closed independently.
