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

### P0.3 — JSJ algebraic reformulation (audit gap 8a)

- **W**: §1 link 8. The JSJ statement currently reads as
  3-manifold/topological. Its algebraic-side reformulation must be
  in terms of the Hecke-tower descent filtration's "rigid pieces"
  (those satisfying a strong descent invariance), not as
  3-manifold pieces.
- **D**: Recast `phi-q-tower-jsj-bridge.md` and
  `pl-jsj-mass-integration-equivalence.md` so that the JSJ
  decomposition is stated as a Wedderburn-block / descent-tower
  partition on the algebraic side. ℂ-side JSJ remains as the
  τ-image, identified via a (still 🟡) conjecture.
- **B**: blocked by nothing.
- **S**: every algebraic-side use of "JSJ piece" can be parsed
  without 3-manifold language.
- **E**: 1 day.

### P0.4 — Single-scale-calibration block (audit CAL-1)

- **W**: §2·A. The paper has *one* allowed external scale ($m_e$).
  Currently this is implicit and so easily becomes "two" (with
  $q_0$ also fitted).
- **D**: New `prop:single-scale-calibration` block in
  `observations/`. States: (i) every mass / Q-value / binding
  energy in the paper is a $\mathbb{Q}(q_0)$-element times $m_e$;
  (ii) $q_0$ is determined by the substrate-uniqueness
  conjectures, not fitted; (iii) the only numerical input from
  CODATA is $m_e$.
- **B**: optional follow-up — strengthen via the substrate-parameter
  derivation chain (P1.1).
- **S**: paper-wide sweep; every numeric mass prediction cites this
  block.
- **E**: 0.5 day.

---

## P1 — Reduce all empirical / fitting flags to derivations

### P1.1 — Substrate parameter $q_0$ derivation chain

- **W**: SUB-1. $q_0 = 1.10998$ pinned to CODATA $m_\mu/m_e$ (per
  [DERIVATION-STATUS.md line 110](../../folio-assistant/computations/DERIVATION-STATUS.md))
  is a *second* external calibration. Either derive or count.
- **D**: Either (a) close the chain
  `q-from-epsilon → substrate-parameter-unique → vacuum-substrate-compatibility`
  (currently 🟡 in algebraic-substrate) and prove $q_0$ is
  algebraically determined; **or** (b) explicit "two-scale" block
  acknowledging both $m_e$ and $q_0$ as inputs.
- **B**: blocked by nothing; (a) is the harder path.
- **S**: paper makes a single, internally-consistent claim (either
  one calibration or two) and never pins $q_0$ to $m_\mu/m_e$ in
  compute except as a *cross-check*, not as a definition.
- **E**: (a) 1 week of theory; (b) 0.5 day of accounting. Recommend
  (b) now and (a) as a P3 follow-up.

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

### P1.5 — Compound-shell / atom-knot atlas — verify base cases are not AME-fitted

- **W**: SHELL-1, §2·H. The block name `compound-beta-shell-calibration`
  self-reports as a calibration; the recursive atlas's base cases
  must be derived, not fitted.
- **D**: Per-block audit of `compound-beta-shell-calibration.md`,
  `recursive-atom-knot-atlas.md`, `derived-mass-formula-light-isotopes.md`
  to verify no base case is a least-squares fit to AME data.
- **B**: blocked by nothing.
- **S**: every base case is a $\mathbb{Q}(q)$-element from a
  Wedderburn / Hecke / GS computation; no `curve_fit`,
  `least_squares`, or "AME-anchored" parameter.
- **E**: 1 day.

### P1.6 — Neutrino mass — demote or fix

- **W**: NU-1. Wrong by 10⁶ — currently a hard claim.
- **D**: Re-classify the neutrino-mass block to `conjecture` with
  the 10⁶ discrepancy named explicitly. Then audit channel choice
  (`alt`-block weight) and operator-selection LP for the neutrino's
  word.
- **B**: blocked by nothing for the demotion; the fix may take
  weeks.
- **S**: paper does not claim a derived neutrino mass while the
  10⁶ gap stands.
- **E**: 0.5 day for demotion; open-ended for the fix.

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
| 1 | **P0.4** Single-scale-calibration block | Cheapest fix; immediately resolves the "is this fitted?" question for half the audit |
| 2 | **P3.1** Conjectural-propagation sweep | Cheap; honesty-improvement; no other dependencies |
| 3 | **P0.2** Land algebraic-quantum-volume recast | Unblocks P0.1 wall-enforcement |
| 4 | **P0.1** Wall-violation sweep over proof blocks | Aligns with user's "strict in proofs" directive |
| 5 | **P0.3** JSJ algebraic reformulation | Unblocks `pl-jsj-mass-integration-equivalence` for downstream use |
| 6 | **P2.5** Symbolic-in-$q$ refactor | Mechanical; immediately makes witness JSONs less "fitted-looking" |
| 7 | **P2.6** GS-filtration narrative blocks | Closes the largest opaque-axiom surface |
| 8 | **P2.2** $H_{3A}$ Wedderburn coverage | Unblocks the big compute fix (P2.1) |
| 9 | **P2.1** Full Wedderburn channels in CRT | The single biggest fix for compute correctness (~99% of mass) |
| 10 | **P1.6** Neutrino demote | Honesty fix; cheap |
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
