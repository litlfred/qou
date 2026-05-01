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

### P0.1 — Wall enforcement audit on every proof, not just statements

- **W**: User directive: "strict archimedean wall **including in
  proofs**". A statement may be algebraic while its proof leaks via
  Mostow / hyperbolic volume.
- **D**: A grep + manual sweep over every `proof` block in
  `content/quantum-observable-universe/**/*.md`. Output: a
  `wall-violations.witness.json` listing every proof block whose
  text invokes Vol(K), hyperbolic, Mostow, Gromov, Thurston,
  SnapPy, Kashaev, Murakami at the proof level (not as a τ-image).
- **B**: blocked by nothing.
- **S**: every flagged proof either (a) is recast to use
  `algebraic-quantum-volume` instead of $\mathrm{Vol}(K)$, or (b)
  is moved to a `remark` interpreting the algebraic statement.
- **E**: 1 day for the sweep + recast. The recast template already
  exists on the followups branch
  ([`recast-tightening-audit-2026-04-27.md`](../recast-tightening-audit-2026-04-27.md)).

### P0.2 — Land the `algebraic-quantum-volume` recast on `main`

- **W**: §4·B of the audit. Until `prop:topological-mass-formula`
  reads in $\mathbb{Q}(q)$ via `algebraic-quantum-volume`, every
  proof citing it is on the wrong side of τ.
- **D**: Cherry-pick / merge the recast already on
  `claude/mass-units-bridge-followups` (commit `7588970f`) into
  `main`. Update all callers.
- **B**: blocks P0.1 (cleanly).
- **S**: `bun run validate` passes; no `prop:topological-mass-formula`
  caller goes through Vol(K).
- **E**: 1–2 hours (mostly cherry-pick + caller fixup).

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

### P1.2 — BW term 8 (Hook) coefficient — kill the "ad hoc" tag

- **W**: BW-8. Coefficient $|\beta_4|\cdot|\ln\lambda|\cdot m_e$ is
  marked "ad hoc" in [DERIVATION-STATUS.md line 52](../../folio-assistant/computations/DERIVATION-STATUS.md).
- **D**: Re-derive via Wenzl bridge or LP-shadow-price (per
  `bw-coefficient-shadow-price`). Replace with the symbolic
  $\mathbb{Q}(q)$-coefficient.
- **B**: depends on `wedderburn-bratteli-recursion` covering
  $\lambda = (2,2)$ self-conjugate at $H_{n\geq 4}$.
- **S**: tag changes to "DERIVED" in DERIVATION-STATUS.md.
- **E**: 2 days.

### P1.3 — BW term 11 (pn corr) coefficient — kill the "approx" tag

- **W**: BW-11. Coefficient $2[2][3]/[4]\cdot[2]\cdot m_e$ is marked
  "approx".
- **D**: Same template as P1.2 but for the conjugate pair
  $[4,1]\oplus[2,1,1,1]$.
- **B**: same as P1.2.
- **S**: "DERIVED" tag.
- **E**: 2 days.

### P1.4 — Magic-number derivation from Bring's surface

- **W**: MAG-1. $\{2,8,20,28,50,82,126\}$ "from Bring's surface — not
  derived" ([DERIVATION-STATUS.md line 178](../../folio-assistant/computations/DERIVATION-STATUS.md)).
- **D**: New block `prop:magic-numbers-bring`. Bring's surface
  $y^5 + xy + 1 = 0$ has automorphism group $S_5$ and a known
  period lattice. Show that the seven nuclear magic values are the
  ranks of subgroups / period sub-lattices that close shells under
  the categorical descent operator.
- **B**: depends on `brings-coordinate-ring` and the descent
  involution at the categorical level.
- **S**: each of the seven values is reproduced as a closed-form
  algebraic expression, not a numerical match.
- **E**: 1 week (genuinely new content; may end up as a
  conjecture if the period-lattice path is too thin).

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

### P1.7 — 1/α 399-ppb residual — derive or honest-conjecture

- **W**: ALPHA-2. Currently flagged "J³ correction (Massey
  products?)" — speculative.
- **D**: Either (a) compute the next-order Hoefsmit / GS
  correction and verify it accounts for the 399 ppb; or (b)
  state explicitly that the 399 ppb is the truncation error from
  cutting at $k = 5$.
- **B**: depends on $H_6$ Wedderburn coverage (P2.2).
- **S**: residual either drops below 100 ppb after k=6 corrections,
  or the truncation interpretation is documented and the residual
  shrinks predictably with $k$.
- **E**: 3–5 days after P2.2.

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

### P2.5 — Symbolic-in-$q$ everywhere, late $q_0$-substitution

- **W**: §3·E. Currently many scripts substitute $q_0$ early,
  producing 50-digit floats that read as "fitted".
- **D**: Refactor every `*_witness.py` script to:
  1. Compute the polynomial / rational expression in $\mathbb{Z}[q^{\pm 1}]$ first;
  2. Substitute $q_0$ only at the final reporting step;
  3. Emit both the symbolic $\mathbb{Q}(q)$ expression *and* the
     numerical value in the witness JSON.
- **B**: blocked by nothing; can run in parallel with P2.1–P2.4.
- **S**: every witness JSON exposes a `polynomial_q` field
  alongside the numerical value.
- **E**: 1 week paper-wide (mechanical refactor).

### P2.6 — GS-filtration `gradedMarkovTrace` / `residueAtRoot` — narrative form

- **W**: §3·F. These are `noncomputable opaque` in Lean. The user
  is less concerned about Lean — but the *narrative* must say what
  these are without hand-waving.
- **D**: New narrative block
  `prop:graded-markov-trace-from-gs-filtration` that defines
  $\mathrm{tr}_{M,\ell}$ as the induced trace on $J^\ell / J^{\ell+1}$
  for the GS-filtration $J^\bullet$, and `prop:residue-at-root` that
  defines the cyclotomic residues purely algebraically (not via
  meromorphic continuation in $\mathbb{C}$).
- **B**: blocked by nothing.
- **S**: every block previously citing `gradedMarkovTrace` /
  `residueAtRoot` opaquely now points at the new propositions.
- **E**: 2 days.

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
- **Pending P3.1 work** (out of scope for this pass):
  - The remaining 17 cone members are all already typed
    `conjecture` / `remark` / `definition` / `example`. No further
    demotions needed at the audit-conjecture level.
  - A document-wide sweep covering *every* open conjecture
    (not just the §5 ten) would extend the cones doc's seed list
    and re-run; if other open conjectures have provable cones, the
    same case (1) / case (2) workflow applies. Estimated 0.5 day
    once a sweep target list is decided.
- **B**: blocked by nothing.
- **S**: ✅ zero violations across the §5 audit conjectures.
- **E**: 0.5 day actual (against the 1–2 day estimate).

### P3.2 — Pentagon $uv = q\,vu$ at traced-volume level (audit GAP 17a)

- **W**: line 113 of [`derivation-audit-2026-04-20.md`](../derivation-audit-2026-04-20.md).
  Pentagon ascension assumes a $q$-commutation identity at the
  traced-volume level that is "expected but unwritten".
- **D**: Write a one-page derivation as a `lemma` block:
  $\mathrm{tr}_M(\hat V_i \hat V_j) = q\, \mathrm{tr}_M(\hat V_j \hat V_i)$
  for adjacent $i,j$ — most likely a direct application of the
  Markov property.
- **B**: blocked by nothing.
- **S**: pentagon-ascension proof in `mass-endomorphism-jet-tower`
  no longer cites an "expected" identity.
- **E**: 1 day.

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
