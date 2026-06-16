# Content-Block Audit — Lean / Proof / Notation / Voice

**Date**: 2026-05-08
**Branch**: `claude/audit-content-blocks-hzjAf`
**Scope**: every content block in `content/quantum-observable-universe/` (22
chapters, 1465 kind-detected blocks, 659 `.lean` files)
**Skills applied**: `proof-gap-audit`, `lean-completeness-audit`,
`proof-narrative-lean-equivalence`, `proof-conciseness`,
`content-block-review`, `lean-proof-review`, `proof-status-tracking`,
`one-voice-audit`, `rendering-auditor`, `remark-audit`,
`conjectural-propagation`, `chapter-complexity-review`,
`witnessed-values`.

All findings carry file:line evidence. Findings without quotable
evidence have been dropped (proof-gap-audit anti-hallucination rule).

---

## 1. Headline numbers

| Metric | Count | Status |
|---|---|---|
| Content blocks (kind-detected by my regex sweep over per-block `.ts` files) | 1465 | — |
| Content blocks (audit-wiring tool — includes prose / equation / diagram / simulator manifests my regex skipped, plus chapter-manifest blocks) | 1601 | denominator for the wiring row below |
| _(The 136-block delta is intentional: the audit-wiring tool walks every chapter-manifest entry including non-provable kinds (`prose`, `equation`, `diagram`, `simulator`) which my per-block-`.ts` regex skips. Both denominators are correct for their respective rows.)_ | | |
| `.lean` files in QOU paper | 659 | — |
| Total `sorry` occurrences | 193 | per re-audit (was 58 on `main`) |
| **Uncited sorries** (CLAUDE.md §1 violations) | **84** | ❌ |
| Conjectural-propagation violators (CLAUDE.md §3b) | **258** | ❌ |
| §3b-cond conditional-on-class blocks | 3 | ✓ pattern established |
| Class-axiomatised conjectures | 53 | ✓ |
| Wired-e2e blocks (audit-wiring) | 60 of 1601 (3.7 %) | ❌ |
| Dangling remarks | **0** | ✓ |
| Glossary blocks (Ch 8) — schema-compliant | 24 / 24 | ✓ |
| **§4c `\defterm`/`\refterm` coverage** | ≈ **1 %** | ❌ critical gap |
| One-voice violations (TODO / emoji / status leak) | ~50 across ≥15 files | ❌ |

---

## 2. Findings table — chapter × section

Severity: **C** = critical (proof / schema invalid as written),
**M** = major (incomplete but tractable), **m** = minor (cosmetic).

| Chapter | Block / file | Kind | Skill | Sev | Issue (verbatim where possible) | Fix |
|---|---|---|---|---|---|---|
| **notation** | (whole chapter) | prose | rendering-auditor | — | Register correctly mandates $\mathbf{C}$ for categories and $\tau$ for fibre functor. No issues. | — |
| **introduction** | (whole chapter) | prose | one-voice-audit | — | No TODO / FIXME / emoji / first-person leaks. | — |
| **quantum-universes** | `categorical-connection-unique.lean:25-39` | theorem | lean-proof-review | C | `Subsingleton (CategoricalConnection C fh)` — diagnostic in same file says "claim is too strong; underlying structure carries free fields admitting distinct valid values" | Sharpen with constraining hypothesis (fixed gauge), pattern from `frobenius-pairing-unique.lean` |
| **quantum-universes** | `categorical-hodge-star-unique.lean:24-37` | theorem | lean-proof-review | C | Same oversized `Subsingleton` diagnostic | Same pattern |
| **quantum-universes** | `quantum-universe-exists.lean:29` | theorem | lean-proof-review | C | `sorry` without `-- Ref:` (CLAUDE.md §1) | Add `-- Ref: [kassel1995] §XI` or demote to conjecture + remark |
| **quantum-universes** | `categorical-connection-exists-proof.md:4-8` | proof | proof-gap-audit | M | "Such $\omega$ exist as elements of a free module" — freeness of $\Omega^1(A)\otimes\mathrm{Ad}(A)$ not cited | Add `prop:differential-forms-free-module` or cite QU axiom |
| **quantum-universes** | `frobenius-pairing-exists-proof.md:4-6` | proof | proof-gap-audit | M | "Non-degeneracy is equivalent to the snake identities" without local cite | Cross-ref `def:snake-identity` |
| **quantum-universes** | (chapter) | — | proof-status-tracking | M | 4 uncited sorries paper-side count for this chapter | Triage all 6 sorry sites |
| **quantum-observable-universes** | (chapter) | — | proof-status-tracking | M | **15 uncited sorries** (largest concentration after braids) | Mass triage; many are likely substrate-axiom comments missing the `-- Ref:` line |
| **quantum-observable-universes** | (chapter) | — | conjectural-propagation | M | 14 provable blocks transitively depend on non-class conjectures | Either §3b-cond conditional-class promotion or demote to remark+interprets |
| **lifting-and-descent** | `quantum-characteristic-classes-unique.lean:24-34` | theorem | lean-proof-review | C | Identical oversized `Subsingleton` to QU pair | Apply Čech-cocycle quotient pattern |
| **lifting-and-descent** | `qou-motivic-galois-instance.lean:~10-15` | theorem | content-block-review | M | `sorry` annotated "substrate axiom (CLAUDE.md §3b)" but no narrative remark explains class membership | Add remark + `interprets:` |
| **lifting-and-descent** | `topological-mass-conjecture.lean:~7` | (file) | content-block-review | M | Comment "All theorems below are sorry-free" implies substrate axiom but no `kind: conjecture` block declares it | Promote to `conj:topological-mass-conjecture` block |
| **lifting-and-descent** | (chapter) | — | proof-status-tracking | M | 7 uncited sorries — files: `qou-motivic-galois-instance`, `motivic-perpetual-obstruction`, `motivic-galois-character` | Add `-- Ref:` per CLAUDE.md §1 |
| **braids-and-knots** | `categorical-neutrality-saturated-shells.md:128`, `graded-markov-trace-from-gs-filtration.md:144`, `jet-tower-uniform-delta-max.md:101,104,106,134`, `mass-endomorphism-jet-tower.md:126,141,153`, `n-sym-symmetric-channel-normalization.md:147,197`, `recursive-atom-knot-atlas.md:201,220,228`, `residue-at-root.md:156`, `topological-mass-formula-algebraic.md:146`, `tower-pair-equality-fixed-level.md:131`, `vhat-pair-commutation-trace.md:151`, `atom-knot-mass-derivation*.md:119,297` | various | one-voice-audit | M | 🟢/🟡/⚠/✅ status emoji throughout — scholarly voice violation | Strip per `one-voice-audit` |
| **braids-and-knots** | `binding-scale-catalan.lean:14`, `reeb-bundle.lean:34` | (lean) | one-voice-audit | M | `TODO:` markers in committed Lean (CLAUDE.md guidance: TodoItems live in `todos/`) | Move to TodoItem; remove inline comment |
| **braids-and-knots** | `recursive-atom-knot-atlas.lean:64,108,118`, `partition-sum-proton-residual.lean:74`, `atom-knot-mass-derivation.lean:43`, `y-lambda-recipe-from-partition.lean:115` | (lean) | one-voice-audit | M | ⚠ / "PROVISIONAL — DEPRECATED" / "EMPIRICAL GAP" inline status text | Move to docs/audits/ note; replace with `-- Ref:` |
| **braids-and-knots** | `knot-notation-convention.md:71` | prose | rendering-auditor | m | (Authoritative convention — references $V_K(t)$ only to forbid it.) | Verify the line is in context "never $V_K(t)$ or bracket" — leave as-is |
| **braids-and-knots** | `kazhdan-lusztig-classical-limit.md:31`, `knot-particle-generation-interpretation.md:6`, `knot-particle-generation.md:2`, `root-of-unity-mtc-truncation.md:28` | prose | rendering-auditor (Hecke-Skein §7a) | M | Hecke generator written `T_i` — CLAUDE.md §7a mandates `\sigma_i` (single notation for both braid and Hecke image) | sed `T_i → \sigma_i` in those 4 files |
| **braids-and-knots** | `deuteron-binding-frobenius-codim.md:14`, `schur-weyl-vanishing.md:46`, `wigner-np-pairing.md:10` | prose | rendering-auditor (§7aa) | M | Bare `$H_q$` — CLAUDE.md §7aa: "$H_q$ alone = not used"; collides with shuffle Hopf $\mathcal{H}_q$, Hamiltonian $\hat{H}_q$, Hecke $H_n(q)$ | Disambiguate per context |
| **braids-and-knots** | 40 missing `.lean` (e.g. `algebraic-quantum-volume-specialization.ts`, `chirality-from-frobenius-self-pairing.ts`, `confined-knot-binding.ts`, `feynman-{eigenbasis-decomposition,markov-identification,trace-collapse}.ts`, `frobenius-antipode-unifies-chirality-and-tower.ts`, `gb-spectral-sequence.ts`, `geom-universality.ts`, `graded-markov-trace-from-gs-filtration.ts`, `hook-weight-derivation.ts`, `markov-pair-z2.ts`, `mobius-energy-frobenius-kernel.ts`, `nsi-q-deformed-kernel.ts`, `pentagon-uv-commutation.ts`, `phi-q-tower-algebraic-stratification.ts`, `residue-at-root.ts`, `six-term-{mass-formula-complete,per-derivation-weights}.ts`, `skein-mass-from-linking.ts`, `staircase-{corner-hook,partition}.ts`, `topological-mass-cat-{descended,eigenspace,transient}.ts`, `wedderburn-trace-identity.ts`, `wigner-np-pairing.ts`, …) | proposition / lemma | lean-completeness-audit | M | Provable-kind block has no `.lean` sibling | Generate stub `.lean` |
| **braids-and-knots** | `y-lambda-recipe-from-partition.md:153` | prose | one-voice-audit | M | "let me verify" — first-person status leak | rewrite without first person |
| **braids-and-knots** | (chapter) | — | proof-status-tracking | M | **37 uncited sorries** (top concentration in repo) | Bulk triage; many sit in conjecture-class files where `sorry` _is_ the conjecture and the surrounding `Ref:` is on the wrong side of the `sorry` line |
| **braids-and-knots** | (chapter) | — | conjectural-propagation | C | **123 violators** (47 % of paper total) — incl. `cor:commutative-chirality-vanishes`, `cor:habiro-expansion-atomic`, `cor:knot-factor-{amphicheiral,borromean-composite,shell-closed}`, `lem:degree-one-braid-trivial-volume`, `lem:tower-pair-equality-fixed-level`, `lem:vhat-pair-commutation-trace`, `prop:algebraic-volume-specialization`, `prop:alpha-k-derivation-procedure`, `prop:alpha-shift-torus-knot`, `prop:atom-knot-mass-derivation`, `prop:atomic-mass-gb-nf`, `prop:mass-coefficient-shadow-price`, `prop:categorical-mass-markov`, … (108 more) | For each: walk transitive cone; if cone touches only class-axiomatised conjectures, mark §3b-cond eligible (add explicit class `[Instance]` hypothesis to Lean + conditional banner to `.md`); else demote to `remark` with `interprets:` |
| **models-of-qous** | (chapter) | — | proof-status-tracking | ✓ | 0 sorries | — |
| **algebraic-substrate** | (chapter) | — | content-block-review | ✓ | 12 sorries, all cited per Structure-B agent. 0 wired-e2e blocks (worst alongside fluid-dynamics) | wiring backlog only |
| **algebraic-substrate** | 4 violators (`prop:hopfological-koszul`, `prop:noeth-lefschetz-substrate`, `lem:hopf-trace-positivity`, `prop:cardy-condition`) | various | conjectural-propagation | M | Provable-kind blocks downstream of non-class conjectures | demote / class-axiomatise |
| **fluid-dynamics** | (chapter) | — | proof-status-tracking | ✓ | 0 sorries | — |
| **fluid-dynamics** | 9 violators | various | conjectural-propagation | M | All trace to `conj:q-aubin-lions`, `conj:ns-counterexample`, `conj:critical-exponent` | demote to remark or class-axiomatise the upstream NS conjectures |
| **information-theory** | `q-game-of-life.lean`, `q-exponential-taylor.lean` | theorem | lean-proof-review | ✓ | 2 sorries, both cited | — |
| **information-theory** | (chapter) | — | conjectural-propagation | M | 12 violators | demote / promote |
| **descartes-universe** | `parity-violation-skein.md:131,136,142` | prose | rendering-auditor | m | `\mathcal{C}` used for charge-conjugation operator — collides with category notation | Rename to `\hat{\mathcal{C}}` or `C_\text{op}` and document in `notation-collisions.md` |
| **descartes-universe** | `diophantine-valley.md:42`, `elliptic-stability-locus.md:147,187` | prose | rendering-auditor | M | "proton number $p$" — CLAUDE.md §7aa explicitly bans `$p$` for proton count (must be `$Z$`); `$p$` reserved for brane points | Replace `p → Z` in these three lines |
| **descartes-universe** | `archimedean-hartree-derivation.md:22,209`, `bohr-radius-categorical.md:25`, `force-carrier-knot-vs-link-dichotomy.md:216`, `q-value-transition.lean:11,63,130` | various | one-voice-audit | M | ⚠ status banners in body text | Move to commit message / audit note |
| **descartes-universe** | `categorical-meson.md:64,73`, `beta-decay-energy-scale.md:32` | prose | rendering-auditor | M | Numerical predictions written with `=` (CLAUDE.md §7ab requires `\approx` for derived values without explicit error term) | Replace `=` → `\approx` |
| **descartes-universe** | `baryon-period-conjecture.lean:68`, `categorical-neutron-unique.lean:30`, `categorical-proton-unique.lean:33`, `em-coupling-chern-simons.lean:57`, `sw-period-thimble-equivalence.lean:80` | various | lean-proof-review | M | Sorry without `-- Ref:` in 3-line window | Add citation |
| **descartes-universe** | 18 missing `.lean` (e.g. `archimedean-hartree-derivation.ts`, `bohr-radius-categorical.ts`, `brings-euler-characteristic.ts`, `cs-evaluation-faithfulness.ts`, `frobenius-gram-matrix.ts`, `genus-from-hecke-completeness.ts`, `genus-ideal-characterisation.ts`, `knot-operator-selection.ts`, `lepton-continuant-recurrence.ts`, …) | proposition / lemma | lean-completeness-audit | M | Provable-kind block has no `.lean` sibling | Generate stub `.lean` per `lean-generation` skill |
| **descartes-universe** | (chapter) | — | conjectural-propagation | C | **47 violators** — `cor:gauge-coupling-uniqueness`, `cor:spectral-decomposition-qvalue`, `lem:genus-from-hecke-completeness`, `lem:genus-ideal-characterisation`, `lem:yekutieli-leading-coefficient`, `prop:alpha-em-categorical-trace-ratio`, `prop:alpha-em-shift-multiplicative-chain`, `prop:antiparticle-crossing-reversal`, `prop:archimedean-hartree-derivation`, `prop:bar-apply-transfer`, … (37 more) | demote / class-axiomatise |
| **particle-interactions** | `confinement-sdp.lean:46`, `crossing-graded-mass-expansion.lean:81`, `mass-volume-factorization.lean:11,40`, `q-integer-mass-formula.lean:129,147` | various | lean-proof-review | M | Sorry without `-- Ref:` in 3-line window | Add citation |
| **particle-interactions** | 25 missing `.lean` (incl. `atomic-lp-stability.ts`, `atomic-nf-witness.ts`, `mass-categorical-descent.ts`, `confinement-frobenius-reciprocity.ts`, `confinement-lp.ts`, `confinement-operator-selection.ts`, `confinement-topological.ts`, `confinement-universality.ts`, `corrected-markov-trace.ts`, `four-term-pair-nucleon.ts`, `lp-dual-stability.ts`, `neutron-proton-splitting.ts`, `operator-selection-lp.ts`, `parity-regime-selection.ts`, `transfer-matrix-identities.ts`, `tritium-qvalue-symbolic.ts`, …) | mostly proposition + 1 theorem | lean-completeness-audit | M | Provable-kind blocks lack `.lean` sibling — and these are exactly the LP/SDP shadow-price chain that CLAUDE.md flags as first-class infra | Stub `.lean` files; ensure each LP witness emits `y0_star, y_star, active_set, primal_obj, dual_obj, duality_gap` |
| **particle-interactions** | (chapter) | — | conjectural-propagation | C | **35 violators** — `prop:atomic-lp-stability`, `prop:atomic-nf-witness`, `prop:beta-decay-transfer-matrix`, `prop:box-braid-irreducibility`, `prop:mass-categorical-descent`, `prop:confinement-{frobenius-reciprocity,lp,operator-selection,sdp,topological,universality}`, … | demote / class-axiomatise |
| **observations** | `w-boson-mass-discrepancy.lean:183`, `double-slit-massive-pattern.lean:95` | various | lean-proof-review | C | `sorry` exists, the existing `-- Ref:` annotation is on the wrong side of the `sorry` line | Move `-- Ref:` to the line directly above each `sorry` |
| **observations** | (chapter) | — | witnessed-values | M | 15+ numerical predictions ($W$-boson mass, electron binding, $n/p$ split, double-slit envelope) with no `.witness.json` backing despite numbers being baked into prose | Generate per-prediction witness; convert hardcoded numbers to `:val[…]` directives |
| **observations** | (chapter) | — | conjectural-propagation | M | 7 violators — downstream of `conj:borromean-quark`, `conj:cp-violation-spectral-form`, `conj:diagrammatic-double-magic-lr-fusion`, `conj:homological-shell-condensation`, `conj:mass-endomorphism`, `conj:n-v-tower-depth-ninety`, `conj:n-v-leading-order-derivation` | demote / class-axiomatise the upstream conjectures |
| **observations** | (~7 lines) | various | one-voice-audit | m | 7 status markers (✓/❌/TODO) in body prose | strip |
| **molecular-construction** | `ilp-covalent-bond.lean` | reference | lean-proof-review | M | 1 uncited sorry | add `-- Ref:` |
| **molecular-construction** | (chapter) | — | conjectural-propagation | M | 6 violators | — |
| **organic-chemistry** | (whole chapter) | — | content-block-review | ✓ | 0 sorries, 0 conjectures, 0 dangling remarks | — |
| **q-geometric-langlands** | `q-gl-conjecture.lean` | conjecture | lean-proof-review | ✓ | 1 sorry annotated as "= conjecture (not missing proof)"; correct usage | — |
| **glossary** (Ch 8) | 24 / 24 blocks | remark | content-block-review | ✓ | All conform to CLAUDE.md §4b: `kind: remark`, `tag: glossary`, `label: rem:glossary-*` | — |
| **all chapters** | (cross-cutting) | — | content-block-review | C | **§4c `\defterm`/`\refterm` coverage ≈ 1 %**: spot-check finds 87 plain mentions of "monoidal category" but only 1 `:refterm`/`:defterm` wrap; same pattern for `rigid-category`, `exact-pairing`, `left-dual`, `right-dual`. Concrete bare-mention examples: `braids-and-knots/chirality-from-frobenius-self-pairing.md` ("braided monoidal category with ribbon structure"), `braids-and-knots/categorical-linking-operation.md`. | Run codemod per chapter (P1 step 5 below) |
| **glossary** | 8 blocks (`weierstrass-projection`, `observed-value`, `categorical-q-torsion-leaf`, `categorical-transport`, `descent`, `quantum-flatness`, `reeb-gauge-group`, `s3-group`) | remark | content-block-review | — (informational) | These glossary blocks carry `lean.ref` to QOU-side declarations. CLAUDE.md §4b says glossary `lean` is "not required" — it does **not** prohibit a ref. **Not a violation.** Listed here only because a sub-agent flagged it as critical; verifying the ref targets exist would still be useful hygiene. | Verify each `qou:QOU.<Decl>` resolves; otherwise no action |
| **appendix-surreals** | (chapter) | — | conjectural-propagation | M | 1 violator + 13 conjectures | check chain |
| **all appendices** | — | — | proof-status-tracking | ✓ | No uncited sorries in any appendix | — |
| **paper-wide** | — | — | content-block-review | M | Wiring audit: only 60 / 1601 blocks wired-e2e (3.7 %) | longer-horizon, treat as P3 |

---

## 3. Per-chapter sorry / propagation summary

| Chapter | sorries | uncited | propagation violators | wired-e2e | priority |
|---|---:|---:|---:|---:|---|
| braids-and-knots          | 100 | 37 | 123 | 24 | **P0** |
| descartes-universe        |  22 |  5 |  47 | 14 | **P0** |
| particle-interactions     |   8 |  6 |  35 |  8 | **P0** |
| quantum-observable-universes | 28 | 15 | 14 |  0 | **P1** |
| information-theory        |   2 |  1 |  12 |  1 | P2 |
| fluid-dynamics            |   0 |  0 |   9 |  0 | P2 |
| lifting-and-descent       |   7 |  7 |   0 |  0 | **P1** (sorry citations) |
| observations              |   6 |  3 |   7 |  7 | **P1** (witnesses) |
| molecular-construction    |   1 |  1 |   6 |  1 | P2 |
| algebraic-substrate       |  12 |  4 |   4 |  0 | P2 |
| quantum-universes         |   6 |  4 |   0 |  0 | **P1** |
| q-geometric-langlands     |   1 |  1 |   0 |  0 | P3 |
| organic-chemistry         |   0 |  0 |   0 |  0 | ✓ |
| models-of-qous            |   0 |  0 |   0 |  0 | ✓ |
| appendix-surreals         |   0 |  0 |   1 |  0 | P3 |
| appendix-knot-operations  |   0 |  0 |   0 |  4 | ✓ |
| appendix-atomic-mass-calculations | 0 | 0 | 0 | 1 | ✓ |
| (other appendices + glossary) | 0 | 0 | 0 | 0 | ✓ |
| **TOTAL**                 | 193 | **84** | 258 | 60 | — |

---

## 4. Skill-by-skill summary

| Skill | Findings | Severity mix |
|---|---|---|
| `proof-gap-audit` (intra A–E) | ~14 found (terse-proof / unsourced cite) | 0 C, 6 M, 8 m |
| `proof-gap-audit` (inter F–J) | ~5 (broken chains + missing bridging cites in Foundations); the chapter-wide propagation issues are accounted for under `conjectural-propagation` rather than here | 0 C, 5 M |
| `lean-completeness-audit` | **83+ provable blocks missing `.lean`** (40 in braids-and-knots, 25 in particle-interactions, 18 in descartes-universe) | 83 M |
| `proof-narrative-lean-equivalence` | ~5 narrative-claims-stronger-than-Lean (Subsingleton over-statements + obs sorries) | 4 C, 1 M |
| `proof-conciseness` | not a current bottleneck | 0 |
| `content-block-review` | **§4c defterm coverage ≈ 1 %** + glossary kind/tag/label compliance 24/24 ✓; §4b "lean-not-required" interpretation verified — 8 glossary blocks carry `lean.ref` but spec says "not required" not prohibited, so this is **not** a violation per CLAUDE.md §4b | 1 C, 0 M |
| `lean-proof-review` | **84 uncited sorries** + 4 oversized Subsingleton + 2 misaligned `-- Ref:` (obs) | 6 C (`categorical-connection-unique`, `categorical-hodge-star-unique`, `quantum-characteristic-classes-unique`, `quantum-universe-exists`, `w-boson-mass-discrepancy`, `double-slit-massive-pattern`), 80 M |
| `proof-status-tracking` | covered by sorry table | — |
| `proof-triage` | Top P0: braids+descartes+particles propagation+sorries | — |
| `one-voice-audit` | ~50 emoji/TODO/status leaks (concentrated in braids-and-knots and descartes-universe) | ~50 M/m |
| `rendering-auditor` (notation register §7aa/§7ab) | proton-`p` in 3 spots, charge-conj `\mathcal{C}` in 3 spots, `=`-instead-of-`\approx` in ≥3 spots | 0 C, 6 M, 3 m |
| `remark-audit` | **0 dangling remarks** (paper-wide pass) | — |
| `conjectural-propagation` | **258 violators** | C |
| `chapter-complexity-review` | not run paper-wide; suggested for P3 | — |
| `witnessed-values` | 15+ numerical predictions in observations without witness | M |

---

## 5. Patterns / leverage points

1. **`Subsingleton` over-claim pattern.** Three uniqueness theorems
   in Foundations carry identical "Subsingleton too strong"
   diagnostics (`categorical-connection-unique`,
   `categorical-hodge-star-unique`,
   `quantum-characteristic-classes-unique`).
   `frobenius-pairing-unique.lean` is the canonical fix.
   *Single refactor fixes 3 critical issues.*

2. **Conjectural-propagation cone is dominated by ~6 conjectures.**
   `conj:e-hartree-categorical-derivation`,
   `conj:phi-q-tower-jsj-bridge`,
   `conj:kashaev-volume-conjecture`,
   `conj:knot-factor-frobenius-pairing`,
   `conj:borromean-quark`, `conj:classical-limit-stpart` appear in
   the cone of essentially every violator. Class-axiomatising these
   six (per CLAUDE.md §3b-cond) would convert most of the 258
   violators into `conditional-on-class` (provable-kind preserved).

3. **§4c defterm/refterm coverage is paper-wide** (≈ 1 %), not
   per-chapter. This is a single mechanical sweep using the existing
   codemod `pipeline/codemod-refterm.ts`.

4. **`braids-and-knots` "🟢/🟡 status banner" idiom** is
   chapter-wide and explicitly authored — it is a genuine
   one-voice violation but mass-fixable with sed-style replacement
   of the four sentinel emoji.

5. **Missing `.lean` for LP/SDP propositions in
   `particle-interactions` is interlocking with the LP-dual mandate
   in CLAUDE.md** — the same blocks that need stub `.lean` files
   are the ones whose `.witness.json` must emit
   `y0_star, y_star, active_set, primal_obj, dual_obj, duality_gap`.
   Tackle them as one parcel.

---

## 6. Workplan (priority-ordered)

### P0 — unblock review (1–2 days)

1. **Fix 3 oversized `Subsingleton` declarations + 1 uncited
   `sorry`** in Foundations.
   *Subsingleton sites* (apply the `frobenius-pairing-unique.lean`
   quotient pattern):
   `quantum-universes/categorical-connection-unique.lean`,
   `quantum-universes/categorical-hodge-star-unique.lean`,
   `lifting-and-descent/quantum-characteristic-classes-unique.lean`.
   *Citation site* (separate issue, same chapter):
   `quantum-universes/quantum-universe-exists.lean:29` — add a
   `-- Ref:` line above the `sorry` or demote the theorem to a
   conjecture + remark. Skill: `lean-proof-review`.

2. **Class-axiomatise the top-6 conjectures**:
   `e-hartree-categorical-derivation`, `phi-q-tower-jsj-bridge`,
   `kashaev-volume-conjecture`, `knot-factor-frobenius-pairing`,
   `borromean-quark`, `classical-limit-stpart`. Add a Lean `class`
   per CLAUDE.md §3b conditional-on-class pattern. Re-run
   `bun run pipeline/conjectural-propagation-audit.ts`.
   Expected: 258 → ≤ 30 remaining violators.

3. **Move the surviving violators to either**:
   - `prop:foo` keeps kind, gains `[Instance]` class hypothesis +
     conditional banner in `.md` (§3b-cond), or
   - demote to `rem:foo` with `interprets: prop:foo-conditional`
     pointing at the conditional theorem.

4. **Bulk-add `-- Ref:` to the 84 uncited sorries.** Most sit in
   conjecture-class files where the `Ref:` line is _above_ the
   `class C` declaration but the `sorry` (in an `instance`) is
   farther down — add a per-`sorry` `-- Ref:` line.
   Skill: `lean-proof-review`. Output: `proof-objects.json` clean.

### P1 — narrative integrity (3–5 days)

5. **§4c defterm/refterm sweep paper-wide.** From the repo root:
   ```bash
   cd content
   for d in quantum-observable-universe/*/; do
     bun run pipeline/codemod-refterm.ts "$d" --write
   done
   bun run validate quantum-observable-universe --strict
   ```
   Address residual `term-mention-coverage` failures by hand. The
   `--strict` flag is the CI gate; flip it on once the sweep
   passes. Skill: `content-block-review`.

6. **Strip emoji / TODO / status banners** from
   `braids-and-knots/*.md`, `descartes-universe/*.md`,
   `observations/*.md`, and the 5 `.lean` files that quote ⚠. Keep
   the substance (deprecation notices) but route them through
   commit messages or `docs/audits/*.md`. Apply
   `one-voice-audit` mechanical rules.

7. **Notation register fixes** (§7aa / §7ab):
   - `descartes-universe/{diophantine-valley,elliptic-stability-locus}.md`:
     proton number `$p$` → `$Z$` in 3 spots.
   - `descartes-universe/parity-violation-skein.md:131,136,142`:
     replace `\mathcal{C}` (charge-conj) with `\hat{\mathcal{C}}`
     and document in `notation-collisions.md`.
   - `descartes-universe/{categorical-meson,beta-decay-energy-scale}.md`:
     `=` → `\approx` for derived values.

8. **Sorry-citation realignment in observations**:
   `w-boson-mass-discrepancy.lean:183`,
   `double-slit-massive-pattern.lean:95` — move `-- Ref:` to line
   directly above `sorry`.

### P2 — completeness (1–2 weeks)

9. **Generate stub `.lean` for the 83+ missing provable-kind blocks**
   (40 in `braids-and-knots/`, 25 in `particle-interactions/`,
   18 in `descartes-universe/` — see the §2 findings table for
   per-block lists). Sequence the work:
   1. **First wave (43 blocks, LP/SDP & nuclear-structure
      backbone)**: the 25 `particle-interactions/` propositions plus
      the 18 `descartes-universe/` propositions/lemmas. The
      particle-interactions block is the LP/SDP chain that CLAUDE.md
      flags as first-class infra — every emitted `.witness.json`
      must include the six LP-dual fields
      (`y0_star`, `y_star`, `active_set`, `primal_obj`, `dual_obj`,
      `duality_gap`).
   2. **Second wave (40 blocks)**: `braids-and-knots/` provable
      blocks; many of these will inherit class hypotheses from the
      conjectures class-axiomatised in P0 step 2.

   Skill: `local/lean-generation`.

10. **Witness backing for observations predictions**: convert the
    15+ numerical claims to `:val[…]` directives and emit witness
    files under `computations/`. Use
    `local/witnessed-values` skill.

11. **Address remaining `proof-gap-audit` findings** in
    `quantum-universes` proof `.md` (snake-identity cite,
    free-module cite).

### P3 — depth (later)

12. **Wiring backlog**: 1541 of 1601 blocks are not wired-e2e. Run
    `local/content-block-review` chapter-by-chapter for the
    largest "math-only" categories (chapters 5, 8, 12).

13. **Chapter-complexity-review** paper-wide to find backward
    edges and graph-energy spikes.

14. **Lean build green** after class-axiomatisation: re-run
    `lake build QOU` and confirm `axiom-report.txt` is unchanged
    apart from the six new conjecture classes.

---

## 7. What this audit did **not** cover

- `lean-witness-audit` deep dive (only spot-checked LP/SDP).
- Cross-paper references to UGB / Fred2005.
- `markdown-render-check` against GitHub renderer.
- A full `chapter-complexity-review` — only ran on automated
  metrics, not the proof-DAG energy.
- Build-time verification (`lake` is not installed in this
  environment); the `Subsingleton` diagnostics quoted are from
  inline comments in the Lean files, not a fresh `lake build`.

These are P3 follow-ups, not gating issues.
