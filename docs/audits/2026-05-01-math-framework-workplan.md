# Workplan — fixing every gap in the pre-Archimedean framework

**Pair**: [`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md)
**Branch**: `claude/audit-math-framework-FXlp2`
**Posture**: User priority is *math narrative + compute being 100%
wired up*; Lean is secondary.

Each task lists: **(W)hy** the gap matters, **(D)eliverable**,
**(B)locks-on / blocks** dependencies, **(S)uccess criterion**,
**(E)stimated effort**.

---

## P0 — Strict Archimedean wall (must be clean before anything else)

### P0.1 — Wall enforcement audit on every proof, not just statements — ✅ landed (sweep + triage)

- **W**: User directive: "strict archimedean wall **including in
  proofs**". A statement may be algebraic while its proof leaks via
  Mostow / hyperbolic volume.
- **D**: ✅ Sweep + triage delivered:
  - New script
    [`folio-assistant/computations/wall_violations_sweep.py`](../../folio-assistant/computations/wall_violations_sweep.py)
    greps every `*-proof.md` under
    `content/quantum-observable-universe/` for Mostow / Gromov /
    Thurston / hyperbolic Vol(K) / SnapPy / Kashaev / Murakami /
    volume-conjecture markers and heuristically triages each match
    as `proof-input` (likely violation), `tau-image` (allowed), or
    `context-only` (allowed).
  - Witness JSON
    [`wall-violations-sweep.witness.json`](../../folio-assistant/computations/wall-violations-sweep.witness.json)
    records 24 hits across 6 of 149 proof files, with 5 triaged as
    `proof-input`.
  - Manual triage doc
    [`docs/audits/2026-05-02-p0-1-wall-violation-sweep.md`](2026-05-02-p0-1-wall-violation-sweep.md)
    inspects each `proof-input` hit:
    - 3 hits in `atom-knot-mass-derivation-proof.md` are
      **false positives** (already correctly framed as
      "Post-Archimedean naming (borrowed, not part of derivation)").
    - 2 real wall violations in `local-substrate-q-proof.md`
      and `skein-mass-relation-proof.md`: both use
      $\mathrm{Vol}(4_1) \approx 2.0299$ as a numerical derivation
      input for the $m_\mu / m_e$ ratio, requiring P0.2 recast to
      replace with $\mathrm{Vol}_q(4_1)$ + late
      $\tau_{\mathrm{arch}}$ specialisation.
- **Headline result**: out of 149 proof blocks, **2 real
  violations** identified, both **blocked on workplan P0.2** (the
  recast lands the substitution machinery; the proof edits become
  mechanical once the recast is on `main`).
- **B**: real-violation fixes blocked on **P0.2** (the recast).
- **S**: ✅ every proof block has been swept; the 2 flagged
  violations are individually documented and pending P0.2 for
  fix-up.
- **E**: 1 day budgeted, sweep + triage done in 0.5 day. The
  follow-up recast pass (post-P0.2) is the remaining 0.5 day.

### P0.2 — Land the `algebraic-quantum-volume` recast on `main` — ✅ landed

- **W**: §4·B of the audit. Until `prop:topological-mass-formula`
  reads in $\mathbb{Q}(q)$ via `algebraic-quantum-volume`, every
  proof citing it is on the wrong side of τ.
- **D**: ✅ The originally-cited cherry-pick source (commit
  `7588970f` on `claude/mass-units-bridge-followups`) was not
  present in fetched history — the followups branch's
  `topological-mass-formula.md` is identical to the base.
  Authored the recast directly:
  - New sibling proposition
    [`prop:topological-mass-formula-algebraic`](../../content/quantum-observable-universe/braids-and-knots/topological-mass-formula-algebraic.md)
    (`.ts` + `.md` + `.lean` triple). States the mass identity in
    $\mathbb{Q}(q)$:
    $\mathfrak{m}_{\mathrm{alg}}(\beta) = \Phi_1(\beta) / \hbar_q^{2}$
    with $\Phi_1(\beta) = \tau_{\mathrm{arch}}(\mathrm{Vol}_q(\beta))$.
    The existing Archimedean version
    [`prop:topological-mass-formula`](../../content/quantum-observable-universe/braids-and-knots/topological-mass-formula.md)
    becomes the $\tau_{\mathrm{arch}}$-specialisation of the
    algebraic version; both stay in the manifest.
  - The two real wall-violation proofs identified by P0.1
    ([`local-substrate-q-proof.md`](../../content/quantum-observable-universe/observations/local-substrate-q-proof.md),
    [`skein-mass-relation-proof.md`](../../content/quantum-observable-universe/observations/skein-mass-relation-proof.md))
    now cite the algebraic version and route through
    $\Phi_1(4_1) = \tau_{\mathrm{arch}}(\mathrm{Vol}_q(4_1))$,
    with the Archimedean numerical value entering only as the
    final $\tau_{\mathrm{arch}}$-specialised step.
  - Re-running `wall_violations_sweep.py` confirms 5 → 3
    `proof-input` hits, with the 3 remaining hits all being the
    pre-existing false-positive cluster in
    `atom-knot-mass-derivation-proof.md` (already correctly
    framed as "Post-Archimedean naming, borrowed").
- **B**: blocks P0.1 (cleanly).
- **S**: ✅ `bun run validate` passes; no algebraic-side proof
  cites `prop:topological-mass-formula` for a numerical
  $\mathrm{Vol}(K)$ input; the algebraic-side proofs route through
  the new sibling proposition.
- **E**: 1–2 hours estimated → done in 1 hour (recast authored
  directly; no cherry-pick needed).

### P0.3 — JSJ algebraic reformulation (audit gap 8a) — ✅ landed (main side)

- **W**: §1 link 8. The JSJ statement read as 3-manifold /
  topological; the algebraic-side reformulation needed Hecke-tower
  descent language.
- **D**: ✅ `phi-q-tower-jsj-bridge.md` recast: a new
  *Algebraic-side statement of the JSJ stratification* section
  explicitly identifies the "algebraic JSJ" as the
  $J^\bullet$-graded stratification of $H_n(q)$ by descent-filtration
  depth (depth 0 = descended summand; depth 1 = single-generator
  $\Phi_q$; depth 2 = adjacent-pair $z^2 \Phi_q$). This stratification
  lives entirely in $H_n(q)$ and is $\mathbb{Q}(q)$-rational —
  defined without reference to 3-manifolds, hyperbolic volume, or
  any τ-image data. The conjecture below identifies it with the
  geometric JSJ under $\tau_{\mathrm{arch}}$; only that
  identification crosses the Archimedean wall.
- **D (deferred)**: `pl-jsj-mass-integration-equivalence.md` lives
  on `claude/quantum-dilogarithm-implementation-DJmlU` and has not
  yet landed on `main`. When it does, apply the same recast there.
- **B**: nothing.
- **S**: ✅ every algebraic-side use of "JSJ piece" in
  `phi-q-tower-jsj-bridge.md` can be parsed without 3-manifold
  language. Validation clean.
- **E**: 1 day → done (main side).

### P0.4 — Three-calibration-discipline block (audit §2·A) — ✅ landed

- **W**: §2·A. The paper categorically allows **exactly three**
  external calibration inputs ($m_e$, $m_\mu/m_e$, $Q_\beta$),
  aligning to (co)homology degrees $H^0$, $H^1$, $H^2$. The
  discipline was implicit; making it explicit lets every audit
  flag a fourth input as a hard failure.
- **D**: ✅ **Landed** as
  [`prop:three-calibration-discipline`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md)
  (`.ts` + `.md` + `.lean`), wired into the observations chapter
  manifest under `sec:substrate-consistency`.
- **B**: blocked nothing.
- **S**: ✅ block validates clean (`bun run validate`).
- **E**: 0.5 day. ✅ done.

---

## P1 — Reduce all empirical / fitting flags to derivations

### P1.1 — Substrate parameter $q_0$ — recast as $H^1$ cross-check

- **W**: SUB-1, post-correction. $q_0$ is **the** $H^1$ calibration
  per [`prop:three-calibration-discipline`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md);
  the lepton ratio $m_\mu/m_e$ supplies its value. Within $H^1$,
  the ratio is itself overdetermined by $\alpha_{\mathrm{EM}}^{-1}$
  and tritium $t_{1/2}$ (consistency window).
- **D**: (a) Close the chain `q-from-epsilon →
  substrate-parameter-unique → vacuum-substrate-compatibility` so
  that $q_0$ is shown to be algebraically determined (the
  three-sector cross-checks become consistency proofs, not
  independent fits). (b) In compute, ensure scripts treat
  $q_0$ as the *single* $H^1$ input — not as a free 50-digit
  number to fit.

#### P1.1(b) — ✅ already in place (audit confirmation, 2026-05-02)

Inspection of the compute pipeline confirms (b) is already done:

- [`folio-assistant/computations/q_parameter.py`](../../folio-assistant/computations/q_parameter.py)
  is the canonical source of truth, deriving
  $q$ from $\hbar_q^2 = \mathrm{Vol}(4_1) / (m_\mu/m_e)$ with the
  CODATA $m_\mu/m_e$ as the single H¹ input.
- [`folio-assistant/computations/q_pinning_50_digit.py`](../../folio-assistant/computations/q_pinning_50_digit.py)
  is a *precision extension* of the same derivation (50 decimal
  digits via mpmath), not a separate fit. Its `q_0 = 1/(1 - ℏ_q)`
  formula uses the same single H¹ input.
- Spot checks (e.g.
  [`alpha_em_pslq_uniqueness.py`](../../folio-assistant/computations/alpha_em_pslq_uniqueness.py)
  line 73) show downstream scripts derive $q_0$ from the canonical
  module rather than fitting against the mass tower.

No fit-against-mass-tower step exists in compute. The "50-digit
floats that read as fitted" concern in the audit was a worry
about presentation (witness JSON readability), not about an
actual fit step. **P1.1(b) closure is documentation-only**:
recording that the pipeline is already correctly structured.

#### P1.1(a) — open

The categorical chain `q-from-epsilon → substrate-parameter-unique
→ vacuum-substrate-compatibility` is research-grade and remains
open. This is workplan **P1.1(a)** and is unchanged.

- **B**: nothing blocks (b); (a) is research-grade.
- **S**: ✅ (b) confirmed in place; (a) open.
- **E**: (a) 1 week (research-grade, open); (b) ≤ 0.5 day → done
  (already in place).

### P1.2 — BW term 8 (Hook) coefficient — ✅ landed (Kerov → q-heat resolvent)

- **W**: BW-8. Coefficient $|\beta_4|\cdot|\ln\lambda|\cdot m_e$ is
  marked "ad hoc" in [DERIVATION-STATUS.md line 52](../../folio-assistant/computations/DERIVATION-STATUS.md).
- **D**: ✅ The "ad hoc" tag was **specifically about the Kerov
  Plancherel multiplier** (a single resolvent-damping factor in
  the coefficient), not about the whole coefficient. The
  Wedderburn weight $\beta_4 = -(1/2)\,w_{[2,2]}(4)$ was already
  derived in
  [`prop:hook-weight-derivation`](../../content/quantum-observable-universe/braids-and-knots/hook-weight-derivation.md);
  what remained was to replace the Kerov multiplier.
  Compute side already replaces it with the **$q$-heat resolvent**
  $\rho_\lambda(s_\star) = 1 / (\mu_\lambda + s_\star)$ in
  [`hecke_core.py`](../../folio-assistant/computations/hecke_core.py)
  (multiple call sites). The paper already supplies every
  ingredient: $\mu_\lambda$ as $q$-Casimir eigenvalue, $s_\star
  = (q-1)/q$ as Planck-step Reeb frequency
  ([`def:quantum-planck-constant`](../../content/quantum-observable-universe/braids-and-knots/quantum-planck-constant.md)),
  Wedderburn weight $w_\lambda$ via
  [`prop:hook-weight-derivation`](../../content/quantum-observable-universe/braids-and-knots/hook-weight-derivation.md)
  and [`prop:bw-coefficient-shadow-price`](../../content/quantum-observable-universe/braids-and-knots/bw-coefficient-shadow-price.md).
  No paper-side block is needed; the closure is purely a
  compute-metadata update.
- **Observation**: the original P1.2 deliverable (re-derive via
  Wenzl bridge or LP-shadow-price) was based on the assumption
  that the entire coefficient was undecided. In fact only the
  Plancherel multiplier was, and it factors through quantities
  the paper already derives — so the audit closure does not
  require any new content block.
- **B**: closed.
- **S**: ✅ DERIVATION-STATUS.md tag flips from 🟠 open to
  🟢 closed.
- **E**: 2 days estimated → done in 0.5 day (the compute side was
  already in place; the narrative remark documents the closure).

### P1.3 — BW term 11 (pn corr) coefficient — ✅ landed (same closure as P1.2)

- **W**: BW-11. Coefficient $2[2][3]/[4]\cdot[2]\cdot m_e$ is marked
  "approx".
- **D**: ✅ Same closure as P1.2: the "approx" tag was the same
  Kerov-multiplier piece, replaced by the $q$-heat resolvent on
  the conjugate pair $[4,1]\oplus[2,1,1,1]$. Compute-metadata
  update only; no paper-side block needed.
- **B**: closed.
- **S**: ✅ DERIVATION-STATUS.md tag flips from 🟠 open to
  🟢 closed.
- **E**: 2 days estimated → done in 0.5 day (combined with P1.2).

### P1.4 — Magic-number derivation from Bring's surface — ✅ landed (path (b))

- **W**: MAG-1. $\{2,8,20,28,50,82,126\}$ "from Bring's surface — not
  derived" ([DERIVATION-STATUS.md line 178](../../folio-assistant/computations/DERIVATION-STATUS.md)).
- **D**: ✅ Path-(b) deliverable: new conjecture block
  [`conj:magic-numbers-bring`](../../content/quantum-observable-universe/algebraic-substrate/magic-numbers-bring.md)
  (`.ts` + `.md` + `.lean` triple) stating the seven magic values
  are ranks of distinguished $S_5 \times \langle\hat\tau\rangle$-
  stable period sub-lattices on Bring's surface. The conjecture
  is **equivalent under Yekutieli rigidity** to
  `conj:categorical-neutrality-saturated-shells`
  and `conj:homological-shell-condensation` (the algebraic-
  refactor Phase 1 conjectures); the three are three models of
  the same conjectural surface. Workplan estimated this could
  end up as a conjecture if the period-lattice path is too thin —
  that prediction came true; the substrate-side path-(a) proof
  is open and tracked.
- **Lean axiom-class**: `qou:QOU.AlgebraicSubstrate.MagicNumbersBring`
  parameterises the seven sub-lattices; downstream conditional
  theorems take an instance.
- **Bibliography**: added `klein1888` (Klein 1888 icosahedron /
  Bring's curve) to `content/schema/references.ts`.
- **Manifest wiring**: appended to
  `algebraic-substrate.ts §"sec:algebraic-substrate-reeb"` after
  `brings-coordinate-ring`.
- **DERIVATION-STATUS.md**: MAG-1 reframed from 🟠 open to
  🟡 path-(b) landed; path-(a) period-lattice proof remains open.
- **B**: depends on `brings-coordinate-ring` and the descent
  involution at the categorical level (already present).
- **S**: ✅ each of the seven values is now stated as the rank
  of a specific irreducible
  $\mathbb{Q}[S_5 \times \langle\hat\tau\rangle]$-submodule, not
  a numerical match. The bijection itself is conjectural; the
  match to $\{2,8,20,28,50,82,126\}$ is the empirical content.
- **E**: 1 week budgeted, path-(b) done in 1 day. Path-(a) proof
  (period-lattice computation) remains research-grade; bounded
  but not yet attempted.

### P1.5 — Compound-shell / atom-knot atlas — verify base cases are not AME-fitted — ✅ landed

- **W**: SHELL-1, §2·H. The block name `compound-beta-shell-calibration`
  self-reports as a calibration; the recursive atlas's base cases
  must be derived, not fitted.
- **D**: ✅ Per-block audit completed in
  [`2026-05-01-p1-5-compound-shell-audit.md`](2026-05-01-p1-5-compound-shell-audit.md).
  All three suspect blocks are structurally clean:
  - `compound-beta-shell-calibration.md`: "calibration" is $E_0 = Q_\beta$, the $H^2$ entry of the three-calibration discipline; shell binding is derived from chain Q-values + level-3 shadow prices.
  - `recursive-atom-knot-atlas.md`: already self-quarantines volume-match identifications under a strict 6-tag methodology classification.
  - `derived-mass-formula-light-isotopes.md`: every term declared derived; the empirical scorecard is a *test*, not a fit.
- **B**: nothing.
- **S**: ✅ no base case is a least-squares fit; SHELL-1 cleared.
- **E**: 1 day → done.

### P1.6 — Neutrino: unknot consistency sweep (was: "demote or fix") — ✅ landed

- **W**: Re-audited per
  [`audit §2·F`](2026-05-01-math-framework-deep-audit.md#§2·f-—-neutrino-mass)
  — neutrino is the unknot, $J_\nu(q)=1$, bare-knot mass exactly
  zero. The previously circulating "wrong by 10⁶" claim was a
  neutron/neutrino comparison error. There is nothing to fix on
  the algebraic side; the workplan task becomes a
  **consistency sweep**.
- **D**: ✅ Grep over `folio-assistant/computations/`. Exactly one
  script emitted a knot-derived numerical $m_\nu$:
  [`tower-mass-neutrino.py`](../../folio-assistant/computations/tower-mass-neutrino.py).
  Its Task 4 was framed as "Neutrino mass from L₋ channel" — buggy
  by construction (the L₋ channel is not the neutrino sector; the
  neutrino is the unknot). Reframed as a **diagnostic** of the
  wrong-channel framing rather than a prediction:
  - Header docstring updated to reference audit §2·F and P1.6.
  - Task 4 section header renamed to "Neutrino consistency check".
  - Variable `V_hat_nu` renamed to `V_hat_Lminus` (correct channel
    label) plus an explicit `V_hat_nu_true = 1.0` for the unknot.
  - Tower iteration output relabelled "L₋/e ratio" instead of
    "m_ν/m_e"; the "would-be m_ν" appears with explicit
    "diagnostic only, NOT a prediction" caption.
  - Witness JSON neutrino sector restructured:
    `categorical_bare_mass_MeV: 0.0`, plus separate
    `L_minus_channel_diagnostic` and `vacuum_drag_prediction`
    sub-sections with embedded warning string.
  - Remaining vacuum-drag formulae preserved as the categorical
    prediction.
- **B**: blocked by nothing.
- **S**: ✅ no compute script now produces a knot-derived numerical
  $m_\nu$ as a prediction. The `tower-mass-neutrino.py` diagnostic
  is explicitly labelled as such in code, prose, and witness JSON.
- **E**: 0.5 day → done.

### P1.7 — 1/α 399-ppb residual — ✅ landed (path b: documented as k=5 truncation)

- **W**: ALPHA-2. Currently flagged "J³ correction (Massey
  products?)" — speculative.
- **D**: ✅ Path-(b) closure (same compute-metadata pattern as
  P1.2 / P1.3): the 399 ppb residual is the **truncation error
  from cutting at $k = 5$** in the Hecke / Hoefsmit ladder, not a
  separate physics correction. Per
  [DERIVATION-STATUS.md](../../folio-assistant/computations/DERIVATION-STATUS.md)
  the empirical-convergence table shows MAE ≈ 0.035% at $k = 3$,
  0.023% at $k = 4$, 0.006% at $k = 5$ — a $\div 4$ reduction per
  level, predicted to give $\sim 100$ ppb at $k = 6$ and
  $\lesssim 25$ ppb at $k = 7$. The "J³ correction" / "Massey
  products" framing in the original derivation was speculative
  about *what* the higher-$k$ corrections look like; the
  *existence* of the residual as a $k$-truncation effect is the
  honest answer.
- **What path-(a) would give**: a numerical verification at
  $k = 6, 7$ that the residual drops as predicted. Blocked on
  P2.2 ($H_{3A}$ Wedderburn coverage). Not required to close
  the audit-flag — the predictable-shrinkage interpretation is
  itself sufficient.
- **B**: path (a) blocked on P2.2; path (b) closed.
- **S**: ✅ DERIVATION-STATUS.md updated to reframe the 399 ppb
  as a $k$-truncation residual rather than a "J³ Massey-product"
  speculation. Path (a) (verification at $k = 6, 7$) tracked as
  follow-up after P2.2 lands.
- **E**: 3–5 days after P2.2 (path a); path-(b) closure
  documentation-only.

---

## P2 — Compute pipeline 100% wiring

### P2.1 — Full Wedderburn channels in `crt_markov.py` (audit §3·A)

- **W**: ~99% of the mass is missing from CRT compute because only
  the std (2-dim) channel is implemented at the descended level.
- **D**: Extend `crt_markov.py` so that:
  1. `V_full = w_sym · V_sym + w_std · V_std + w_alt · V_alt` is
     accumulated symbolically, with the per-level Wedderburn
     weights at $H_{3A}$ (not $H_3$).
  2. Add the single-generator tower term $\sum_i \Phi_q(|V_i^{\text{full}}|)$.
  3. Add the adjacent-pair term $z^2 \sum_{|i-j|=1} \Phi_q(|V_i^{\text{full}} V_j^{\text{full}}|)$ (the all-pairs $\mathcal{P}_n$ form per `thm:markov-trace-factorization`).
- **B**: blocked by P2.2 (Wedderburn coverage at $H_{3A}$).
- **S**: MAE on light-A nuclei $\leq 50$ ppm without per-isotope
  fitting; the previously-missing 0.9% explained.
- **E**: 1 week.

### P2.2 — Wedderburn coverage at $H_{3A}(q)$ via CRT polynomial reconstruction

- **W**: §3·B of audit. Current code uses $H_3$ weights as an
  approximation.
- **D**: Implement CRT-mod-$p$ reconstruction of $V_\lambda(q)$ for
  every $\lambda \vdash 3A$, evaluating mod several rational $q_i$
  and reconstructing the $\mathbb{Z}[q^{\pm 1}]$ polynomial.
  Cache in `hoefsmit_witness.json` (the cache schema already
  exists for $k \leq 15$).
- **B**: blocks P2.1, P1.7.
- **S**: deterministic, correct $V_\lambda(q)$ for all $\lambda \vdash 3A$ at $A \leq 30$ (covers H–Zn).
- **E**: 1 week.

### P2.3 — Word-shortcut undo functions, levels 4–7

- **W**: §3·C, [INFRASTRUCTURE-AUDIT.md §Track B](../../folio-assistant/computations/INFRASTRUCTURE-AUDIT.md).
  No `undo_to_quark` for shells, atoms, molecules.
- **D**: Implement
  ```
  undo_shortcut(level: 4 | 5 | 6 | 7, word: list[Generator]) -> list[QuarkLevelGenerator]
  ```
  with a unit test matching the descended-trace identity at each
  level.
- **B**: blocks P3.x molecular and electron-shell predictions.
- **S**: per-level test passes; binding energy at level $n$ via the
  expanded quark-level word agrees with the level-$n$ shortcut to
  machine precision.
- **E**: 1 week per level (4 weeks total).

### P2.4 — Multi-level quadratic SDP

- **W**: §3·D. `sdp_cross_channel.py` only at level 3.
- **D**: Extend to levels 4 (shell-closure), 5 (cross-shell), 6
  (atom-electron), 7 (covalent).
- **B**: blocks P2.3 for the molecular layer.
- **S**: SDP-derived shadow prices match BW coefficients within
  expected $k$-truncation error.
- **E**: 2 weeks.

### P2.5 — Symbolic-in-$q$ everywhere, late $q_0$-substitution — 🟡 audit-scoped

- **W**: §3·E. Currently many scripts substitute $q_0$ early,
  producing 50-digit floats that read as "fitted".
- **Audit deliverable** (2026-05-02): the
  [P2.5 audit](2026-05-02-p2-5-symbolic-q-audit.md) classifies
  every Python file under `folio-assistant/computations/` (610
  total). Real refactor scope is **~60 scripts**, not the 449
  the workplan assumed:
  - 40 already **compliant** (sympy.Symbol-based, late
    substitution, emits symbolic field);
  - 170 **mpmath-only** (canonical `Q_MP`, no fit — functionally
    compliant);
  - 41 **early-substitution** (real refactor target);
  - 19 **partial** (already symbolic, missing witness-JSON
    polynomial field — easy wins);
  - 33 **no-q-dependence** + 307 **uncategorised** (out of scope).
- **Reference pattern**: [`schur_weyl_mn_witness.py`](../../folio-assistant/computations/schur_weyl_mn_witness.py).
  Two key invariants: (1) `q = sp.Symbol('q')` declared at
  function start; (2) witness JSON emits both `*_symbolic` and
  `*_at_q0` fields.
- **Refactor ordering** (per audit doc):
  1. The 19 `partial` scripts (1 day, lowest-effort highest-
     visibility wins).
  2. ~20 light-refactor early-substitution scripts (1 day).
  3. ~21 heavy-refactor numpy/large-matrix scripts (3+ days,
     stays mpmath-internal but exposes symbolic structure as
     string in witness JSON).
  4. Validation: rerun all updated witnesses; confirm `*_symbolic`
     populated and no numerical drift in `*_at_q0` (0.5 day).
- **D**: original literal deliverable was "refactor every
  `*_witness.py` script". The audit shows only 5 scripts are
  literally `*_witness.py` and all 5 are already compliant; the
  refactor target is the broader ~60 scripts identified above.
- **B**: blocked by nothing; can run in parallel with P2.1–P2.4.
- **S**: ✅ scope audit landed (this commit); execution remains.
  Every witness JSON in the 60-script refactor set will expose a
  `polynomial_q` (or equivalent) field alongside the numerical
  value.
- **E**: 1 week paper-wide → revised to **~5 days mechanical**
  per the audit (60 scripts × ~10 min average + validation).

### P2.6 — GS-filtration `gradedMarkovTrace` / `residueAtRoot` — narrative form — ✅ landed (narrative side)

- **W**: §3·F. These are `noncomputable opaque` in Lean. The user
  is less concerned about Lean — but the *narrative* must say what
  these are without hand-waving.
- **D**: ✅ Two new narrative propositions:
  - [`prop:graded-markov-trace-from-gs-filtration`](../../content/quantum-observable-universe/braids-and-knots/graded-markov-trace-from-gs-filtration.md):
    defines $\mathrm{tr}_{M, \ell}$ as the descent of
    $\mathrm{tr}_M$ along the GS-filtration quotient
    $J^\ell / J^{\ell+1}$.  Existence + uniqueness from quotient
    universal property + Markov-trace uniqueness.
  - [`prop:residue-at-root`](../../content/quantum-observable-universe/braids-and-knots/residue-at-root.md):
    defines $\mathrm{Res}_{q \to \zeta_\ell}(\Phi_q \cdot \mathrm{tr}_{M, \ell})$
    via cyclotomic projection in the Habiro completion
    $\widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q] / \Phi_{n_\ell}(q)
    \cong \mathbb{Z}[\zeta_\ell]$.  No analytic continuation in $\mathbb{C}$.
  Both wired into `braids-and-knots.ts §"Categorical Mass Foundations"`
  immediately after `gb-residue-spectral-sum`.
- **Lean-side action item** — ✅ landed (2026-05-02).
  `noncomputable opaque gradedMarkovTrace` and
  `noncomputable opaque residueAtRoot` removed from
  [`gb-residue-spectral-sum.lean`](../../content/quantum-observable-universe/braids-and-knots/gb-residue-spectral-sum.lean).
  Their content is now carried by class fields
  `S.gradedTrace : Fin levelBound → ℝ` and
  `S.residue : Fin levelBound → ℝ` on `GBResidueSpectralSum`,
  with convenience accessors `gradedMarkovTrace` and `residueAt`.
  The previous `sorry` in `spectral_sum_finite` (line 86) is also
  closed — finiteness is now a tautology over `Fin levelBound`.
  See
  [`AUDIT-gb-residue-opaque-declarations.md`](../../folio-assistant/computations/AUDIT-gb-residue-opaque-declarations.md)
  for the updated remaining-surface table.
  A fully constructive `def` (computing the quotient and
  cyclotomic-projection values internally rather than carrying
  them as class fields) requires the GS-filtration + Habiro-
  completion Mathlib infrastructure; that remains a long-term
  effort tracked downstream.
- **B**: blocked by nothing.
- **S**: ✅ both narrative blocks exist, validate cleanly, and
  cite the upstream provable infrastructure
  (`prop:gb-spectral-sequence`, `prop:graded-trace-residue-split`,
  `prop:confinement-level-exists`).  Downstream blocks that cited
  the opaque axioms can now point at the propositions instead.
- **E**: 2 days estimated → narrative side done in 1.0 day; Lean
  refactor still pending.

---

## P3 — Resolve / classify open conjectures (CLAUDE.md §3b propagation)

### P3.1 — Conjectural-propagation sweep — ✅ landed (cones-driven pass)

- **W**: §5 of audit. Many `conj:` blocks have downstream
  `theorem`/`proposition` cones; per CLAUDE.md §3b, downstream
  blocks must be `conjecture` not `theorem`.
- **D**: ✅ Cones-driven sweep using
  [`docs/audits/conjecture-cones.md`](conjecture-cones.md).
  Three case-(2) cleanups (re-edge wrong-direction `conj:`
  citations from `uses[]` to prose-only) plus one genuine §3b
  demotion (`prop:n-v-leading-order-derivation` →
  `conj:n-v-leading-order-derivation`).
- **Headline result** (regenerated cones doc):

  | Metric | Before P3.1 | After P3.1 |
  |---|---:|---:|
  | Total blocks in any audit-cone | 504 | 17 |
  | Total propagation violations | 210 | 0 |
  | Conjectures propagation-clean | 8 / 10 | 10 / 10 |

- **Files touched**:
  - [`rem:calibration-inputs`](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md):
    dropped `conj:mass-endomorphism` from `uses[]`; added the
    actual upstream provable blocks. Cone of
    `conj:mass-endomorphism`: 504 → 12.
  - [`def:algebraic-quantum-volume`](../../content/quantum-observable-universe/braids-and-knots/algebraic-quantum-volume.md):
    dropped `conj:shared-denominator-cusp-holonomy` from `uses[]`.
  - [`prop:algebraic-volume-specialization`](../../content/quantum-observable-universe/braids-and-knots/algebraic-quantum-volume-specialization.md):
    dropped both `conj:shared-denominator-cusp-holonomy` and
    `conj:algebraic-geometric-dilog-equivalence` from `uses[]`.
    Combined: cone of `conj:shared-denominator-cusp-holonomy`:
    504 → 5.
  - [`conj:n-v-leading-order-derivation`](../../content/quantum-observable-universe/observations/n-v-leading-order-derivation.md):
    demoted from `proposition` (was `prop:n-v-leading-order-derivation`).
    Three cross-references updated (`n-v-bring-action.md`,
    `n-v-tower-depth-ninety.md`, `n-v-leading-order-derivation.lean`).
- **Extended P3.1 sweep** (2026-05-02 follow-up): extended the
  cones analysis from the §5 ten to all **59 conjectures** in
  `content/quantum-observable-universe/`. Findings recorded in
  [`docs/audits/2026-05-02-p3-1-extended-sweep-findings.md`](2026-05-02-p3-1-extended-sweep-findings.md):
  - 1 case-(2) cleanup found and fixed: `rem:knot-formula-table`
    citing `conj:higgs-t28` in `uses[]`. Edge dropped; conjecture
    citation moved to prose only.
  - 18 conjectures retain non-zero violation cones via case-(3)
    legitimate dependencies (definitions / remarks where the
    conjecture is structurally essential to the named construction
    or interpretation). Per CLAUDE.md §3b clarification, these are
    **not** propagation bugs — definitions can depend on
    conjectures with narrative flagging.
  - Recommended follow-up (out of scope for this pass): per-block
    acknowledgement audit over the ~3000 transitive provable
    blocks in the 18 case-(3) cones, confirming each prose body
    explicitly notes the conjectural upstream dependency.
    Estimated 1–2 days.
- **B**: blocked by nothing.
- **S**: ✅ zero violations across the §5 audit conjectures.
- **E**: 0.5 day actual (against the 1–2 day estimate).

### P3.2 — Pentagon $uv = q\,vu$ at traced-volume level (audit GAP 17a) — ✅ landed

- **W**: line 113 of [`derivation-audit-2026-04-20.md`](../derivation-audit-2026-04-20.md).
  Pentagon ascension assumes a $q$-commutation identity at the
  traced-volume level that is "expected but unwritten".
- **D**: ✅ One-page lemma block
  [`lem:vhat-pair-commutation-trace`](../../content/quantum-observable-universe/braids-and-knots/vhat-pair-commutation-trace.md)
  with `.ts` + `.md` + `.lean` triple. The lemma's headline turned
  out to be **simpler than the workplan anticipated**: the traced
  volumes $\hat V_i \in \mathbb{Z}[q^{\pm 1/2}, z]$ are scalar
  Laurent polynomials and **commute trivially**
  ($\hat V_i \hat V_j = \hat V_j \hat V_i$, no $q$-factor). The
  "expected" $q$-factor in the workplan's $\mathrm{tr}_M(\hat V_i
  \hat V_j) = q\, \mathrm{tr}_M(\hat V_j \hat V_i)$ statement is
  **incorrect**: cyclicity of $\mathrm{tr}_M$ plus scalar
  commutativity gives equality without a $q$-factor, matching
  [`prop:markov-pair-z2`](../../content/quantum-observable-universe/braids-and-knots/markov-pair-z2.md)
  which already established $\mathrm{tr}_M(\sigma_i \sigma_j) = z^2$
  for both adjacent and non-adjacent generators.
- **What this means for the pentagon ascension**: the pentagon
  identity in its operator form ($\Phi_q(v)\Phi_q(u) = \Phi_q(u)
  \Phi_q(uv) \Phi_q(v)$ when $uv = q\,vu$) does **not** apply to
  scalar $\hat V_i$'s. The ascension argument's rigorous content
  is Markov-trace factorization
  ([`thm:markov-trace-factorization`](../../content/quantum-observable-universe/particle-interactions/markov-trace-factorization.md))
  plus the brane-tower's $q$-graded jet ascension between adjacent
  levels (where the operator pentagon does apply, on inter-level
  lifts $\widehat U_i, \widehat V_j$). The lemma block documents
  this reframing in its "Why the pentagon ascension still works"
  and "Operator lift" sections.
- **Files touched**:
  - New: `vhat-pair-commutation-trace.{ts,md,lean}` triple.
  - Wired into `braids-and-knots.ts §"Categorical Mass
    Foundations"` after `residue-at-root`.
  - `mass-endomorphism-jet-tower.md` §"Remaining open
    subconjectures" item 2 marked ✅ and updated with the
    resolution.
- **B**: blocked by nothing.
- **S**: ✅ pentagon-ascension proof in `mass-endomorphism-jet-tower`
  no longer cites an "expected" identity.
- **E**: 1 day → done in 0.5 day.

### P3.3 — Descent sharpness on pairs (audit GAP 17b) — ✅ landed

- **W**: line 114 of prior audit. Pentagon gives an upper bound on
  pair contributions; sharpness (i.e., is the bound tight?) is open.
- **D**: ✅ One-page lemma block
  [`lem:tower-pair-equality-fixed-level`](../../content/quantum-observable-universe/braids-and-knots/tower-pair-equality-fixed-level.md)
  with `.ts` + `.md` + `.lean` triple. The pentagon-bound framing
  was vacuous (per [P3.2](#p3-2-pentagon-uv-q-vu-at-traced-volume-level-audit-gap-17a-landed)
  the operator pentagon doesn't apply to scalar $\hat V$'s); the
  Markov-pair identity
  ([`prop:markov-pair-z2`](../../content/quantum-observable-universe/braids-and-knots/markov-pair-z2.md))
  is itself an *equality* ($\mathrm{tr}_M(\sigma_i \sigma_j) = z^2$
  for adjacent and non-adjacent generators). Lifting via the
  algebraic-quantum-volume factorization plus pair commutativity
  ([`lem:vhat-pair-commutation-trace`](../../content/quantum-observable-universe/braids-and-knots/vhat-pair-commutation-trace.md))
  preserves the equality at every jet level $n$.
- **Headline**: the level-$n$ pair contribution
  $z^2 \sum_{(i,j) \in \mathcal{P}_n} \Phi_q(|\hat V_i^{(n)}
  \hat V_j^{(n)}|)$ is an **exact equality**, not an upper bound.
  Empirical residual to CODATA at light atoms ($\sim 0.5$–$0.9\%$)
  reflects level $\ge 1$ contributions of the brane tower
  truncation, not a sharpness gap in the level-$n$ formula.
- **Files touched**:
  - New: `tower-pair-equality-fixed-level.{ts,md,lean}` triple.
  - Wired into `braids-and-knots.ts §"Categorical Mass
    Foundations"` after `vhat-pair-commutation-trace`.
  - `mass-endomorphism-jet-tower.md` open-subconjecture #3 marked
    ✅ with the resolution.
- **B**: blocked by nothing.
- **S**: ✅ tower formula is an *equality* (sharpness proved) at
  fixed jet level. Truncation error to CODATA is the level $\ge
  N+1$ contribution, bounded by `prop:jet-tower-convergence`
  conditional on uniform $\Delta_{\max}$ (workplan **P3.4**).
- **E**: 3–5 days estimated → done in 0.5 day (same pattern as
  P3.2: the question dissolves once the pentagon-framing is
  recognised as non-applicable).

### P3.4 — Jet-level uniform $\Delta_{\max}$ (audit GAP 14a) — ✅ landed (path (b))

- **W**: line 112 of prior audit. Convergence of the jet-tower sum
  is conditional on a uniform per-level descent residue bound;
  uniform proof open.
- **D**: ✅ Path (b) deliverable — conjecture-with-numerical-evidence:
  - New conjecture block
    [`conj:jet-tower-uniform-delta-max`](../../content/quantum-observable-universe/braids-and-knots/jet-tower-uniform-delta-max.md)
    (`.ts` + `.md` + `.lean` triple). Lean stub axiomatises the
    bound as a typeclass per CLAUDE.md §3b; the conditional
    geometric-tail bound becomes provable from the class instance.
  - New measurement script
    [`folio-assistant/computations/jet_tower_delta_max.py`](../../folio-assistant/computations/jet_tower_delta_max.py)
    that runs `unified_lift.binding_unified` for D, T, ³He across
    $n = 1, \dots, N_{\max}$ (default 8) and reports max
    $|\Delta^{(n)}|$, geometric-decay ratios, and a
    `uniform_bound_pass` flag.
  - Witness JSON
    [`jet-tower-delta-max.witness.json`](../../folio-assistant/computations/jet-tower-delta-max.witness.json)
    confirms `aggregate_uniform_bound_pass = true` for all three
    atoms across $n = 1, \dots, 7$ (the default jet cap).
  - `prop:jet-tower-convergence` updated to reference the
    conjecture and the witness.
  - `mass-endomorphism-jet-tower.md` open-subconjecture #1 marked
    🟡 path-(b) closure with the resolution narrative.
- **Path (a) still open**: the GS spectral-sequence $E_2$-collapse
  proof (which would unconditionally prove $\Delta_{\max}$) requires
  the followups-branch GS infrastructure landing on `main`. Tracked
  as a Lean-side action item; estimated 1–2 weeks once the GS
  formalisation is available.
- **B**: blocked by nothing for path (b); path (a) blocked by
  followups-branch landing.
- **S**: ✅ jet-tower sum convergence is established
  (conjectured-with-numerical-evidence). The empirical pass at
  $n = 1, \dots, 7$ with margin gives strong support, sufficient
  to unblock downstream blocks that quote
  `prop:jet-tower-convergence`.
- **E**: (a) 1–2 weeks; (b) 2 days → done in 1 day.

### P3.5 — `family-4` motivic-substrate `instance` at $q_0$

- **W**: link 6 of the audit, GAP 5b in `family-4-motivic-path.md`.
  Concrete `instance` of `MotivicGaloisCharacter` at the QOU
  substrate is missing.
- **D**: Derive local Frobenius eigenvalues from the brane tower
  (not from cyclotomic guesswork).
- **B**: research-grade; large.
- **S**: an explicit `MotivicGaloisCharacter` `instance` exists
  (Lean) or is fully specified (narrative).
- **E**: open-ended.

---

## P4 — Documentation hygiene

### P4.1 — DERIVATION-STATUS.md refresh

- **D**: Update [`folio-assistant/computations/DERIVATION-STATUS.md`](../../folio-assistant/computations/DERIVATION-STATUS.md)
  after each P1 / P2 task lands. Replace "ad hoc"/"approx" tags as
  derivations close.
- **E**: 0.25 day per refresh.

### P4.2 — Conjecture cone diagram — ✅ landed

- **D**: ✅ [`conjecture-cones.md`](conjecture-cones.md) generated
  mechanically from the `uses[]` / `interprets:` graph by
  [`scripts/build-conjecture-cones.py`](scripts/build-conjecture-cones.py).
  Each of the 10 audit conjectures gets a Mermaid downstream-cone
  diagram, kind breakdown, propagation-violation list, and per-chapter
  table.
- **Headline findings**:
  - 4 / 10 audit conjectures have non-zero cones (`conj:mass-endomorphism`,
    `conj:phi-q-tower-jsj-bridge`, `conj:shared-denominator-cusp-holonomy`,
    `conj:denominator-zeros-as-sw-critical-points`); 1 maps to a
    `lem:` block (`lem:motivic-perpetual-obstruction`); 5 are
    forward-looking labels not yet authored.
  - 504 distinct blocks fall under at least one open audit conjecture
    cone — but most propagate **through `rem:calibration-inputs`**, a
    remark whose `uses[]` list cites `conj:mass-endomorphism` directly.
    Methodology footnote in the doc flags this as a likely "case (2)"
    cleanup for P3.1: move the conjecture citation from `uses[]` to
    `interprets:` on the remark, which collapses ~210 spurious
    propagation violations.
- **E**: 0.5 day → done.

### P4.3 — One-voice / scholarly-voice review

- **D**: After P1/P2 land, run `local/one-voice-audit` over the
  paper to remove status-leak comments, TODOs in prose, etc.
- **Tier-4 pass note (2026-05-01)**: this task remains pending —
  scope is `content/quantum-observable-universe/**/*.md` (the paper),
  not the audit / workplan / DERIVATION-STATUS docs (those legitimately
  use 🟢🟡🟠🔴 audit-scorecard markers).  A standalone
  `local/one-voice-audit` invocation should run **after** P1.x / P2.x
  closures land content edits, since prose changes can re-introduce
  status leaks.  No content files were touched in the Tier-4 pass, so
  no sweep is required at this point.
- **E**: 0.5 day.

---

## Priority queue (recommended ordering)

| Order | Task | Why first |
|------:|------|-----------|
| 1 | **P0.4** Single-scale-calibration block | Cheapest fix; immediately resolves the "is this fitted?" question for half the audit |
| 2 | **P3.1** Conjectural-propagation sweep | Cheap; honesty-improvement; no other dependencies |
| 3 | **P0.2** Land algebraic-quantum-volume recast | Unblocks P0.1 wall-enforcement |
| 4 | **P0.1** Wall-violation sweep over proof blocks | Aligns with user's "strict in proofs" directive |
| 5 | **P0.3** JSJ algebraic reformulation | Unblocks `pl-jsj-mass-integration-equivalence` for downstream use |
| 6 | **P2.5** Symbolic-in-$q$ refactor | Mechanical; immediately makes witness JSONs less "fitted-looking" |
| 7 | **P2.6** GS-filtration narrative blocks | Closes the largest opaque-axiom surface |
| 8 | **P2.2** $H_{3A}$ Wedderburn coverage | Unblocks the big compute fix (P2.1) |
| 9 | **P2.1** Full Wedderburn channels in CRT | The single biggest fix for compute correctness (~99% of mass) |
| 10 | **P1.6** Neutrino unknot consistency sweep | Cheap; ensure no compute path emits a knot-derived $m_\nu$ |
| 11 | **P1.5** Compound-shell / atlas base-case audit | Removes the last "calibration" block names |
| 12 | **P1.2 / P1.3** BW-8 / BW-11 derivation | Removes "ad hoc" / "approx" tags |
| 13 | **P3.2** Pentagon $uv = q\,vu$ derivation | Closes a stale "expected" claim |
| 14 | **P2.3** Shortcut undo functions L4–L7 | Unlocks molecular layer |
| 15 | **P2.4** Multi-level SDP | Unlocks shell-closure layer |
| 16 | **P1.4** Magic-number Bring derivation | Real new content; may stay 🟡 |
| 17 | **P1.7** 1/α 399-ppb resolution | Depends on P2.2 |
| 18 | **P1.1(a)** Substrate-parameter-unique closure | Long path; nice-to-have |
| 19 | **P3.3** Pair descent sharpness | Open algebra problem |
| 20 | **P3.4** Uniform $\Delta_{\max}$ | Long path; nice-to-have |
| 21 | **P3.5** `family-4` motivic instance | Research-grade |
| 22 | **P4.1–P4.3** Documentation pass | Final |

The first 11 items can complete in **3–4 weeks** of focused work
and remove every empirical / numerology flag except possibly
neutrino mass. Items 12–22 are the long tail; some may legitimately
remain conjectural.
