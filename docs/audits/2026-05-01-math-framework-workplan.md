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

### P0.1 — Wall enforcement audit on every proof, not just statements — ✅ landed

- **W**: User directive: "strict archimedean wall **including in
  proofs**". A statement may be algebraic while its proof leaks via
  Mostow / hyperbolic volume.
- **D**: ✅ Wall-sweep agent surveyed all 149 `*-proof.md` blocks for
  archimedean terminology used as derivation steps. Result recorded
  in [`2026-05-01-p0-1-wall-sweep.md`](2026-05-01-p0-1-wall-sweep.md):
  - **0 hard violations** 🔴
  - **2 soft risks** 🟠 (`local-substrate-q-proof.md`,
    `skein-mass-relation-proof.md`) — both use `prop:topological-mass-formula` in
    calibration steps; honest under the three-calibration
    discipline ($H^1$ calibration via lepton ratio) but recommended
    for future recast to lead with the algebraic Markov-trace form.
  - **7 cleared** 🟢.
- **B**: nothing.
- **S**: ✅ no proof-block hard-violates the wall.
- **E**: 1 day → done.

### P0.2 — Land the `algebraic-quantum-volume` recast on `main` — ✅ already landed

- **W**: §4·B. The recast was thought to live on the followups
  branch only; inspection of `main` shows it already landed.
- **D**: ✅ `algebraic-quantum-volume-specialization.md` on `main`
  already explicitly tags routes 1 (q→1) and 2 (roots-of-unity /
  volume conjecture) as "post-Archimedean naming"; only route 3
  ($q = q_0$ substrate evaluation) is "pre-Archimedean, exact" and
  used in QOU-internal derivations. The $8G = \mathrm{Vol}(\mathcal{B}_3)$
  scale is named via route 2 but not used as a derivation step.
- **B**: nothing.
- **S**: ✅ wall-clean on main; verified by P0.1 sweep.
- **E**: 0 (already done).

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
- **B**: nothing blocks (b); (a) is research-grade.
- **S**: every compute script that uses $q_0$ derives its value
  from a single declared $H^1$ input (e.g. CODATA $m_\mu/m_e$),
  not from a separate fit-against-mass-tower step.
- **E**: (a) 1 week; (b) 0.5 day.

### P1.2 — BW term 8 (Hook) coefficient — kill the "ad hoc" tag — ✅ already derived

- **W**: BW-8 was tagged "ad hoc" in DERIVATION-STATUS line 52.
- **D**: ✅ Re-inspection shows the live paper formulation
  ([derived-mass-formula-light-isotopes](../../content/quantum-observable-universe/braids-and-knots/derived-mass-formula-light-isotopes.md))
  uses
  $\Delta_W = -m_e \cdot H_q((2,2)) \cdot \min(Z,N)/A$
  with $\beta_4 = -\tfrac12 w_{[2,2]}(4)$ derived from the
  Wedderburn weight $w_{[2,2]}(4) = \dim_q([2,2])^2 / [4]_q!$
  ([hook-weight-derivation](../../content/quantum-observable-universe/braids-and-knots/hook-weight-derivation.md)).
  The "ad hoc" tag in DERIVATION-STATUS was a stale summary from
  an older formulation.
- **B**: nothing.
- **S**: ✅ DERIVATION-STATUS.md table updated to remove the "ad
  hoc" tag and link the live derivation.
- **E**: 0 (already done; only documentation refresh needed).

### P1.3 — BW term 11 (pn corr) coefficient — kill the "approx" tag — ✅ already derived

- **W**: BW-11 was tagged "approx" in DERIVATION-STATUS line 55.
- **D**: ✅ Same status as P1.2: the live paper formulation has
  $\Delta_{T=1} = -m_e \cdot H_q((2,2)) \cdot (n_{pp}+n_{nn})/A$
  as the **natural T=1 extension** of BW-8 using the same
  self-conjugate $(2,2)$ partition and same $1/A$ normalisation,
  with $n_{pp}=Z(Z{-}1)/2$, $n_{nn}=N(N{-}1)/2$
  ([derived-mass-formula-light-isotopes](../../content/quantum-observable-universe/braids-and-knots/derived-mass-formula-light-isotopes.md)).
  The "approx" tag was stale.
- **B**: nothing.
- **S**: ✅ DERIVATION-STATUS.md table updated.
- **E**: 0 (already done).

### P1.3a — BW vs Wenzl-bridge vs shadow-price equivalence — ✅ landed (verified)

🟢 **Closed.** Symbolic verification in
[`folio-assistant/computations/bw_wenzl_shadow_equivalence.py`](../../folio-assistant/computations/bw_wenzl_shadow_equivalence.py)
proves the three forms are NOT independent; they are the same
$w_\lambda = \dim_q(\lambda)^2 / [n]_q!$ scaled by explicit
factors of $h = q - q^{-1}$:

- BW form: $\beta_\lambda = -\tfrac12 w_\lambda$
- LP shadow-price: $C_\lambda = w_\lambda \cdot h/2$
- Wenzl-bridge: $y_\lambda = (-1)^{\kappa_\lambda} w_\lambda$ (= $w_\lambda$ for self-conjugate)

Ratios verified for $\lambda = (2,2)$ at $k=4$ (BW-8 / BW-11) and
$\lambda = (3,2,1)$ at $k=6$ (BW-7 Wigner-2). See
[`2026-05-01-p1-3a-bw-equivalence-audit.md`](2026-05-01-p1-3a-bw-equivalence-audit.md)
and the witness JSON.

The three forms remain in the paper as alternative views; no
schema or content changes required.

### P1.3b — **Follow-up**: Consolidate to canonical $w_\lambda$ + three named scalings

- **W**: User question after P1.3a closure: "implications? can we
  reduce complexity? solidify on one approach?" Answer:
  three forms are scalings of one canonical
  $w_\lambda = \dim_q(\lambda)^2 / [n]_q!$. Each context picks the
  natural form, but the underlying mathematics is one object.
- **D**: New block `prop:wedderburn-weight-canonical` (in
  `braids-and-knots/`) that:
  1. Defines $w_\lambda$ as the canonical Wedderburn-block weight.
  2. States the three named scaling identities:
     $\beta_\lambda := -\tfrac12 w_\lambda$ (BW),
     $C_\lambda := w_\lambda \cdot h/2$ (shadow-price),
     $y_\lambda := (-1)^{\kappa_\lambda} w_\lambda$ (Wenzl).
  3. Cites the three existing derivation blocks
     (`hook-weight-derivation`, `bw-coefficient-shadow-price`,
     `y-lambda-closed-form-wenzl-bridge`) as proofs of each scaling.
  4. Refers to
     [`bw_wenzl_shadow_equivalence.py`](../../folio-assistant/computations/bw_wenzl_shadow_equivalence.py)
     for symbolic verification.
- **B**: nothing.
- **S**: existing derivation blocks update their `uses[]` to point
  at `prop:wedderburn-weight-canonical`; ~50–100 lines of redundant
  exposition removed; reader sees one object instead of three.
- **E**: 1 day.

### P1.3a-historical — Follow-up flag (now resolved by P1.3a above)

- **W**: User flag — the BW-8 / BW-11 coefficients have **three
  candidate derivation paths** in the paper:
  1. **BW (Bethe-Weizsäcker) hook form**:
     $-m_e \cdot H_q((2,2)) \cdot \min(Z,N)/A$
     ([derived-mass-formula-light-isotopes](../../content/quantum-observable-universe/braids-and-knots/derived-mass-formula-light-isotopes.md),
     [hook-weight-derivation](../../content/quantum-observable-universe/braids-and-knots/hook-weight-derivation.md)).
  2. **Wenzl bridge form**: $y_\lambda$ closed-form via the
     Wenzl bridge ([y-lambda-closed-form-wenzl-bridge](../../content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.md)).
  3. **LP shadow-price form**: BW coefficient as the dual variable
     of the partition's Frobenius-positivity constraint in the
     nuclear operator-selection LP
     ([bw-coefficient-shadow-price](../../content/quantum-observable-universe/braids-and-knots/bw-coefficient-shadow-price.md)).
- **D**: Decide between two outcomes:
  - **(Equivalence)** Prove the three forms agree on every BW
    coefficient (one derivation, three views) — preferred outcome:
    each coefficient is a rational identity in $\mathbb{Q}(q)$,
    and proving the three rational expressions are equal is a
    finite computation per coefficient.
  - **(Three independent ladders)** If equivalence cannot be
    established for some coefficient, keep all three as parallel
    derivations and document the gap explicitly.
- **B**: nothing technical, but it requires the symbolic-in-$q$
  refactor (P2.5) to compare expressions cleanly.
- **S**: a witness JSON
  (`bw-derivation-equivalence.witness.json`) listing each BW
  coefficient and confirming all three derivation forms reduce to
  the same $\mathbb{Q}(q)$-element. If any coefficient lacks
  equivalence, the gap is named.
- **E**: 1 week (mostly mechanical: symbolic-in-$q$ comparison
  per coefficient, BW vs Wenzl vs LP).

### P1.4 — Magic numbers — extend Hoefsmit-character derivation past $k=10$ (4/7 already done)

- **W**: MAG-1, post-correction. The earlier "Bring's surface — not
  derived" framing is **superseded**. The live derivation is via
  Hoefsmit-character second differences
  ([`prop:magic-numbers-from-q`](../../content/quantum-observable-universe/observations/magic-numbers-from-q.md)),
  which already reproduces {2, 8, 20, 28} from $q_0$ at $K=10$. The
  remaining three (50, 82, 126) require $k\geq 12$ Wedderburn
  coverage.
- **D**: Two parallel paths:
  - **(a) Compute path** — extend `shell_closure_compute.py` past
    $k=10$ once Hoefsmit-witness coverage at $k\geq 12$ lands
    (gated by **P2.2**: $H_{3A}$ Wedderburn coverage via CRT
    polynomial reconstruction).
  - **(b) Homological path** —
    [PR #500](https://github.com/litlfred/qou/pull/500)
    (`claude/qou-algebraic-refactor-1qVFc`) bypasses the matrix-evaluation
    barrier with three new conjectures:
    - `conj:categorical-neutrality-saturated-shells` — full twist
      $\theta_n \in Z(H_n(q))$ acts trivially on $V_\lambda$ iff
      $\kappa_\lambda = \sum_{x \in \lambda} c(x) = 0$.
    - `conj:homological-shell-condensation` — Białynicki–Birula
      filtration of the Hecke category gives a spectral sequence
      $E_r^{p,q}(n)$; $E_\infty^{p,>0} = 0$ exactly at the magic
      ladder $\{2,8,20,28,50,82,126\}$.
    - `conj:diagrammatic-double-magic-lr-fusion` — double-magic
      stability is LR-fusion of two self-conjugate
      $\kappa$-balanced Young diagrams.
- **B**: (a) gated on P2.2; (b) gated on PR #500 landing on main.
- **S**: All seven magic numbers either (a) reproduced numerically
  via $\delta^2\Phi$ peaks at $Z = 50, 82, 126$, or (b) derived
  homologically via the BB-filtration spectral sequence collapse.
- **E**: (a) 1 week of compute after P2.2 lands. (b) Conditional on
  the three conjectures of PR #500.

The Bring-surface route is **no longer the live path** for this
derivation; if reopened, it would be as an alternative
cross-check, not the primary derivation.

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

### P1.6 — Neutrino: unknot consistency sweep (was: "demote or fix")

- **W**: Re-audited per
  [`audit §2·F`](2026-05-01-math-framework-deep-audit.md#§2·f-—-neutrino-mass)
  — neutrino is the unknot, $J_\nu(q)=1$, bare-knot mass exactly
  zero. The previously circulating "wrong by 10⁶" claim was a
  neutron/neutrino comparison error. There is nothing to fix on
  the algebraic side; the workplan task becomes a
  **consistency sweep**.
- **D**: Grep `folio-assistant/computations/` for any script that
  emits a numerical $m_\nu$ from a knot-Markov-trace path (rather
  than from the vacuum-drag formula
  $m_\nu \sim \mu_0\cdot(q-1)$). Any such script is buggy by the
  unknot identity and must be removed or renamed.
- **B**: blocked by nothing.
- **S**: zero compute scripts produce a knot-derived neutrino
  mass; vacuum-drag predictions are clearly labelled as such; the
  obsolete "10⁶ off" line in
  [`DERIVATION-STATUS.md`](../../folio-assistant/computations/DERIVATION-STATUS.md)
  is replaced (already done in this audit pass).
- **E**: 0.5 day.

### P1.7 — 1/α residual — ✅ already at 6.7 ppb (within CODATA)

- **W**: ALPHA-2 was tagged "399 ppb residual; J³ Massey-product
  speculation" in DERIVATION-STATUS line 180. Re-inspection shows
  this was a **legacy formulation**.
- **D**: ✅ The live closed form
  ([`alpha-em-categorical-trace`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-categorical-trace.md))
  is
  $1/\alpha_{EM} = 45 \cdot [3]_q \cdot (1 + \delta_{CS} + 8q\,\delta_{CS}^2)$
  with $\delta_{CS} = \hbar_q^4 \cdot [5]_q$, predicting
  $137.035998166$ vs CODATA $137.035999084$ — residue **~6.7 ppb**,
  within the 21-ppb CODATA uncertainty. Each factor is forced by
  an upstream block (`exterior-square-borromean`,
  `force-carrier-bring-uniqueness`,
  `gram-determinant-plancherel-ratio`, genus-4 torus-knot
  enumeration). PSLQ uniqueness confirms no shorter rational
  combination matches.
- **B**: nothing.
- **S**: ✅ residue at 6.7 ppb < CODATA uncertainty;
  DERIVATION-STATUS.md updated in this audit pass.
- **E**: 0 (already done; only documentation refresh needed).

---

## P2 — Compute pipeline 100% wiring

### P2.1 — Full Wedderburn channels in `crt_markov.py` (audit §3·A)

- **W**: ~99% of the mass is missing from CRT compute because only
  the std (2-dim) channel is implemented at the descended level.
- **2026-05-01 refresh** (per
  [`AUDIT-crt-k-level.md`](../../folio-assistant/computations/AUDIT-crt-k-level.md)):
  `crt_markov.py` *already has* `tower_mass_symbolic_eval` which
  computes V_full + full tower at **H_3 weights**. But **no caller
  uses it** — the 5 callers (`canonical_isospin_pyhecke.py`,
  `derived_only_extended_A12.py`, `deuteron_error.py`,
  `gb_residue_tower.py`, `paper_six_term_isotope_sweep.py`) all
  invoke the descended-only `markov_trace_symbolic_eval`. So the
  gap is *practical* even though the code has caught up in principle.
- **D** split into two phases:
  - **P2.1a (small optimization, immediate)**: migrate appropriate
    callers from `markov_trace_symbolic_eval` to
    `tower_mass_symbolic_eval`. Per-caller decision (some may be
    *intentionally* descended-only — e.g., `derived_only_extended_A12.py`).
    Each migration is ~1-2 line.
  - **P2.1b (CRT main task, multi-week)**: replace H_3 weights
    with H_{3A} weights via CRT polynomial reconstruction. Gated
    on P2.2.
  - Originally-listed (3): `z²Σ Φ_q(|V_i^full V_j^full|)` adjacent-pair
    term — **already in** `tower_mass_symbolic_eval` (line 240–249).
- **B**: P2.1a blocks nothing; P2.1b blocked by P2.2.
- **S**: P2.1a — every caller intentionally on descended-only is
  documented; appropriate ones migrated. P2.1b — MAE on light-A
  nuclei ≤ 50 ppm without per-isotope fitting.
- **E**: P2.1a 1 day; P2.1b multi-week.

### P2.2 — Wedderburn coverage at $H_{3A}(q)$ via CRT polynomial reconstruction — **elevated**

**2026-05-01 elevation**: was tagged "approximation accuracy fix"; the
P2.1a witness
([`2026-05-01-p2-1a-tower-vs-descended.witness.json`](2026-05-01-p2-1a-tower-vs-descended.witness.json))
shows it is actually a **structural-convergence fix**. Using H_3
weights at H_{3A} pushes V̂_i values above the Φ_q convergence
radius ($|z| < q$); the tower formula becomes divergent, not just
inaccurate. Per user confirmation: "probably H_3 weights are wrong
at H_{3A}". P2.2 now both restores convergence AND improves
accuracy.

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

### P2.5 — Symbolic-in-$q$ everywhere, late $q_0$-substitution — 🟡 surveyed; Tier B kickoff landed

**Tier B kickoff (2026-05-01):** helper module
[`witness_polynomial.py`](../../folio-assistant/computations/witness_polynomial.py)
+ first exemplar (`bw_wenzl_shadow_equivalence.py`) migrated. Per
[`2026-05-01-p2-5-tier-b-kickoff.md`](2026-05-01-p2-5-tier-b-kickoff.md):
re-survey corrects target count from 110 to **81** scripts; remaining
80 are mechanical 3-line refactors against the helper.

- **W**: §3·E. Currently many scripts substitute $q_0$ early,
  producing 50-digit floats that read as "fitted".
- **Scope refined** (per
  [`2026-05-01-p2-5-symbolic-in-q-survey.md`](2026-05-01-p2-5-symbolic-in-q-survey.md)):
  605 scripts total; 122 sympy-capable; **0** currently emit a
  `polynomial_q` field. Original "1 week" estimate was too low.
  Three tiers:
  - **Tier A** — live mass-tower scripts (`crt_markov.py`,
    `hecke_core.py`, `hecke_characters.py`, `mass_endomorphism.py`,
    `tower_binding_full.py`, `shell_closure_compute.py`). Currently
    purely mpmath. Direct sympy refactor hits polynomial explosion
    at $A=4$ (per `tower_binding_symbolic.py`). **Blocked on
    P2.2** (CRT polynomial reconstruction).
  - **Tier B** — ~110 already-sympy-capable scripts that don't yet
    emit `polynomial_q`. Mechanical refactor; ~1 day.
  - **Tier C** — 107 purely-numerical scripts. Document as
    "evaluation harness", no refactor needed.
- **B**: Tier A blocked on P2.2; Tier B independent.
- **S**: every Tier A/B witness exposes `polynomial_q`.
- **E**: Tier B 1 day; Tier A multi-week after P2.2 lands.

Reference example for the canonical late-substitution pattern:
[`bw_wenzl_shadow_equivalence.py`](../../folio-assistant/computations/bw_wenzl_shadow_equivalence.py)
(written for P1.3a).

### P2.6 — GS-filtration narrative — ✅ already landed

- **W**: §3·F. The Lean `gradedMarkovTrace` / `residueAtRoot` are
  `noncomputable opaque`; the *narrative* must define them
  algebraically.
- **D**: ✅ Both narrative blocks exist:
  - [`prop:graded-trace-residue-split`](../../content/quantum-observable-universe/braids-and-knots/graded-trace-residue-split.md)
    — canonical decomposition $\mathrm{tr}_M = \mathrm{tr}_{\mathrm{gr}} + \mathrm{Res}_{\mathrm{GB}}$ via the symbol map $\sigma : J^\ell \to J^\ell/J^{\ell+1}$. Cohomological interpretation as $E^\infty$-page pairing. Strutinsky-shell-correction physics analogy.
  - [`prop:gb-residue-spectral-sum`](../../content/quantum-observable-universe/braids-and-knots/gb-residue-spectral-sum.md)
    — symbolic feeding lemma:
    $r_\ell(T_w; q_0) = \mathrm{Res}_{q=\zeta_\ell}[\Phi_q \cdot \mathrm{tr}_{M,\ell}(T_w)] / (q_0 - \zeta_\ell)$
    — explicitly **symbolic** in the Grothendieck group of the
    filtered differential algebra, not a $\mathbb{C}$-analytic identity.
    Strict-wall caveat: $R$-side stays formal; convergent $\mathbb{C}$-side identification is the τ-image via Picard–Lefschetz thimbles
    ([sw-period-thimble-equivalence](../../content/quantum-observable-universe/descartes-universe/sw-period-thimble-equivalence.md)).
- **B**: nothing.
- **S**: ✅ both narrative propositions exist; both are explicitly
  $R$-side / archimedean-wall-respecting. Lean opaques can now point
  at these blocks for their semantic content.
- **E**: 0 (already done).

---

## P3 — Resolve / classify open conjectures (CLAUDE.md §3b propagation)

### P3.1 — Conjectural-propagation sweep

- **W**: §5 of audit. Many `conj:` blocks have downstream
  `theorem`/`proposition` cones; per CLAUDE.md §3b, downstream
  blocks must be `conjecture` not `theorem`.
- **D**: Run `local/proof-gap-audit` skill (§I conjectural
  propagation) over the paper. Demote any provable block whose
  `uses[]` cone touches a `conj:` to `conjecture`. Promote
  proof blocks downstream of conjectures to `remark` with
  `interprets:`.
- **B**: blocked by nothing.
- **S**: zero `theorem`/`proposition`/`lemma`/`corollary` blocks
  have a transitively-conjectural `uses[]` cone.
- **E**: 1–2 days for the sweep.

### P3.2 — Pentagon $uv = q\,vu$ at traced-volume level — ✅ already landed

- **W**: line 113 of [`derivation-audit-2026-04-20.md`](../derivation-audit-2026-04-20.md)
  flagged the pentagon $q$-commutation identity as "expected but
  unwritten". Re-inspection shows it IS written.
- **D**: ✅ `prop:pentagon-uv-commutation`
  ([pentagon-uv-commutation.md](../../content/quantum-observable-universe/braids-and-knots/pentagon-uv-commutation.md))
  contains the full 4-step derivation:
  1. Reduce to a two-generator commutator via far-commutativity.
  2. Eigenvalue specialisation on the $q$-block (Hecke relation).
  3. Pair-swap from the braid relation $\sigma_s\sigma_{s+1}\sigma_s = \sigma_{s+1}\sigma_s\sigma_{s+1}$.
  4. Quantum-torus identity on the transient summand $B_\lambda^{\mathrm{trans}} = \ker\hat\tau_n \cap B_\lambda$.
- **B**: nothing.
- **S**: ✅ block exists with derivation; cited in
  `phi-q-tower-jsj-bridge.md`.
- **E**: 0 (already done).
- **Open extensions** (folded into P3.3 sharpness audit):
  - Direct check on the std (2×2) Wedderburn block.
  - Sharpness of the descended residual $R_q$.

### P3.3 — Descent sharpness on pairs (audit GAP 17b)

- **W**: line 114 of prior audit. Pentagon gives an upper bound on
  pair contributions; sharpness (i.e., is the bound tight?) is open.
- **D**: Derive sharpness or replace pentagon-bound with an
  inequality flag in the tower formula.
- **B**: blocked by nothing.
- **S**: the tower formula is either an *equality* (sharpness
  proved) or an *inequality* with a named gap term.
- **E**: 3–5 days.

### P3.4 — Jet-level uniform $\Delta_{\max}$ (audit GAP 14a)

- **W**: line 112 of prior audit. Convergence of the jet-tower sum
  is conditional on a uniform per-level descent residue bound;
  uniform proof open.
- **D**: Either (a) prove uniform $|\Delta^{(n)}| \leq \Delta_{\max}$
  from the GS spectral sequence's $E_2$-collapse (which lives on the
  followups branch), or (b) state the bound as a conjecture and
  measure $|\Delta^{(n)}|$ across $n=0..N$ in compute to confirm
  geometric decay.
- **B**: depends on followups-branch landing for path (a).
- **S**: jet-tower sum convergence is established (proved or
  conjectured-with-numerical-evidence).
- **E**: (a) 1–2 weeks; (b) 2 days.

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

### P4.2 — Conjecture cone diagram

- **D**: Add a downstream-cone diagram for each open `conj:` block
  to `audits/conjecture-cones.md`. Visualises §5 of audit.
- **E**: 0.5 day.

### P4.3 — One-voice / scholarly-voice review

- **D**: After P1/P2 land, run `local/one-voice-audit` over the
  paper to remove status-leak comments, TODOs in prose, etc.
- **E**: 0.5 day.

---

## Priority queue (recommended ordering)

| Order | Task | Why first |
|------:|------|-----------|
### Tier-1 + Tier-2 (May 1 session) — landed

| Order | Task | Result |
|------:|------|--------|
| 1 | **P0.4** Three-calibration-discipline block | ✅ landed (`prop:three-calibration-discipline` aligned to $H^0/H^1/H^2$) |
| 2 | **§2·F + P1.6** Neutrino correction | ✅ landed (NU-1 withdrawn; ν = unknot, $J_\nu = 1$, bare mass 0) |
| 3 | **P1.5** Compound-shell / atlas / light-isotopes audit | ✅ landed (no AME fit; SHELL-1 cleared) |
| 4 | **P0.3** JSJ algebraic reformulation (main side) | ✅ landed (`phi-q-tower-jsj-bridge` adds *Algebraic-side statement* via $J^\bullet$-stratification) |
| 5 | **P0.1** Wall-violation sweep over proof blocks | ✅ landed (0 hard violations; 2 soft risks documented) |
| 6 | **P0.2** Land algebraic-quantum-volume recast | ✅ already on main (verified) |
| 7 | **P1.4** Magic numbers reclassified | ✅ 4/7 derived via Hoefsmit (`prop:magic-numbers-from-q`); 3/7 await k≥12 (P2.2 dependency) |
| 8 | **P1.2 / P1.3** BW-8 / BW-11 ad-hoc/approx tags | ✅ already derived (`derived-mass-formula-light-isotopes`); DERIVATION-STATUS updated |
| 9 | **P1.7** 1/α residual | ✅ already at 6.7 ppb (within CODATA 21-ppb uncertainty); legacy "399 ppb" superseded |

### Tier-3 (May 1 continuation — partial)

| Order | Task | Result |
|------:|------|--------|
| 1 | **P3.1** Conjectural-propagation sweep | ✅ landed (audit only); witness `docs/audits/2026-05-01-p3-1-conjectural-propagation.witness.json`; memo `2026-05-01-p3-1-conjectural-propagation-audit.md`. **Policy decision required (A / B / C)**: 260 provable blocks transitively touch a `conj:`; ~225 share a common cone of ~20 substrate-foundation conjectures. Recommend Option B (substrate-axiom classification). |
| 2 | **P3.2** Pentagon $uv = q\,vu$ derivation | ✅ already landed in `prop:pentagon-uv-commutation` (4-step proof: far-commutativity reduction, eigenvalue specialisation, braid-relation pair-swap, transient-block restriction). Open extensions (std-block direct check, $R_q$ sharpness) folded into P3.3. |
| 3 | **P2.6** GS-filtration narrative blocks | ✅ already landed: `prop:graded-trace-residue-split` (canonical $\mathrm{tr}_M = \mathrm{tr}_{\mathrm{gr}} + \mathrm{Res}_{\mathrm{GB}}$ split via symbol map) + `prop:gb-residue-spectral-sum` (symbolic feeding lemma; $R$-side; cohomological interpretation; strict-wall convergent $\mathbb{C}$-side via PL thimbles). |
| 4 | **P1.3a** BW vs Wenzl-bridge vs shadow-price equivalence | ✅ landed (symbolic verification): all three forms are the same $w_\lambda$ scaled by explicit factors of $h$. Ratios BW/shadow $=-1/h$, BW/Wenzl $=-1/2$, shadow/Wenzl $=h/2$. Verified for $\lambda=(2,2)$ and $\lambda=(3,2,1)$. |
| 5 | **P2.5** Symbolic-in-$q$ survey | 🟡 surveyed: 605 scripts, 122 sympy-capable, 0 emit `polynomial_q`. Tier A (live mass tower) blocked on P2.2 (CRT reconstruction). Tier B (~110 already-symbolic scripts) tractable. Memo `2026-05-01-p2-5-symbolic-in-q-survey.md`. |
| 2 | **P2.5** Symbolic-in-$q$ refactor | Mechanical; makes witness JSONs less "fitted-looking" |
| 3 | **P2.6** GS-filtration narrative blocks | Closes the largest opaque-axiom surface |
| 4 | **P2.2** $H_{3A}$ Wedderburn coverage | Unblocks P1.4 (magic numbers 50/82/126) and P2.1 |
| 5 | **P2.1** Full Wedderburn channels in CRT | The single biggest compute fix (~99% of mass) |
| 6 | **P1.3a** BW vs Wenzl-bridge vs shadow-price equivalence | User flag; show all three derivation paths agree (or document gaps) |
| 7 | **P3.2** Pentagon $uv = q\,vu$ derivation | Closes a stale "expected" claim |
| 8 | **P2.3** Shortcut undo functions L4–L7 | Unlocks molecular layer |
| 9 | **P2.4** Multi-level SDP | Unlocks shell-closure layer |
| 10 | **P1.1** Substrate-uniqueness closure / cross-check discipline | Long path; nice-to-have |
| 11 | **P3.3** Pair descent sharpness | Open algebra problem |
| 12 | **P3.4** Uniform $\Delta_{\max}$ | Long path; nice-to-have |
| 13 | **P3.5** `family-4` motivic instance | Research-grade |
| 14 | **P4.1–P4.3** Documentation pass | Final |

The first 11 items can complete in **3–4 weeks** of focused work
and remove every empirical / numerology flag except possibly
neutrino mass. Items 12–22 are the long tail; some may legitimately
remain conjectural.
