# Algorithms Annex (`qou-mba8`) & 14-Appendix Back-Matter Consolidation (`qou-anx0` + `qou-lanx`): Post-Wave Audit & Architectural Decision Brief

**Date:** 2026-11-23 · **Branch:** `claude/annex-mba-consolidation-options-20261123` (off `origin/main` at `e330ab6aa04`)
**Beans:**
- `qou-mba8` (post-stabilization overhaul and prior-art pruning of `appendix-mass-binding-algorithms` plus scattered algorithm blocks),
- `qou-anx0` (epic to consolidate all `14` monograph back-matter appendices and build dense, 80-decimal-place witness-backed master reference tables with propagated calibration uncertainties),
- `qou-lanx` (monograph annex describing reusable `Mathlib4`-ready Lean 4 subgraphs and the `6` standalone Reservoir community contribution libraries, consolidated with `appendix-formalisation-notes`),
- Coordinated upstream/sibling beans: `qou-qzvs`, `qou-udad`, `qou-h6ef`, `qou-5lct` (all four blocking L2 1-ppQ derivation waves now landed on `origin/main` via `#9205..#9221`), `qou-nmjd` (replace internal `CAL-1/2/3` codes in paper prose with physical calibration observables $(m_e, \mathfrak{D}_\beta, m_\pi)$), `qou-g4x1` (remediate `6` vacuous conjecture kernels in `AppendixSurreals`), `qou-sm8w` + `qou-akee` (active Standard Model & Eightfold Way wave), `qou-7p89` + `qou-t0fc` + `qou-4b6g` (witness-table wiring & $Z=0\ldots 118$ isotope shards), and `qou-cvu9` (active sibling bibliography branch `claude/prior-art-doi-verified-pkg-20261123` at `63446514c77`).

**Scope of this commit:** **Read-and-analyze cold-reader decision brief only.** Zero monograph `.md`/`.ts`/`.lean` files, zero computation scripts, zero `.witness.json` files, and zero external-facing root metadata files (`CITATION.cff`, `README.md`, `home_page/`) were modified.

---

## 0. Decision Brief & Turnkey `AskUserQuestion` Chat Mirror

> **Usage note for foreground coordinator:** Everything inside **§0.1** is written for a cold reader who was not in this audit session (`AGENTS.md` strict rules 1–6: every identifier expanded on first use, decision-first opening, self-contained 4-part per-option frames with concrete structural previews, explicit default-if-silent, physics-and-paper blast radius, and a 1-sentence recommendation marked as judgement) and can be pasted verbatim into chat immediately above the structured question tool call. **§0.2** provides the matching structured `ask_question` JSON payload (`🟡` prefix, `"is_multi_select": true`) for both questions (**Q1** and **Q2**).

### 0.1 Plain-Chat Mirror (Paste Immediately Above `ask_question` / `AskUserQuestion`)

---

#### Question 1 (`qou-mba8`) — Algorithms Annex & Scattered Algorithm Blocks

🟡 **Waiting on user — Now that the Nakayama-twisted Frobenius (`#9205/#9206`), solver-free $(1^3)$ radical shadow-price (`#9208`), toric nuclear chamber Gröbner basis (`#9212`), and 5-layer confinement tower (`#9214`) derivations have landed on `origin/main`, how should we restructure `appendix-mass-binding-algorithms` (`22` blocks, `1,527` markdown lines) and the scattered procedural blocks in Chapters 7 and 12?**

Choosing whether to keep a separate step-by-step computational algorithms appendix, prune textbook prior-art derivations down to two-sentence citations plus QOU-specific parameter contracts, or fold the genuinely novel QOU computational procedures directly into the body chapters is an editorial and architectural decision for the author (`AGENTS.md`, "Ask the owner before changing things"). Meanwhile, our post-`#9205..#9221` audit caught six live mathematical and factual contradictions inside `appendix-mass-binding-algorithms` and the Chapter 7/12 procedural remarks (detailed in §1.3 below) that need resolution under whichever structural shape you pick.

**Default if you say nothing or defer:** **Q1 Option 1 (Status Quo on `origin/main`)** stays in effect — zero files change, all `22` blocks in `folio/quantum-observable-universe/appendix-mass-binding-algorithms/` and the `5` scattered procedural blocks in Chapter 7 (`knots-particles-confinement/`) and Chapter 12 (`nuclear-interactions/`) remain as currently rendered on `origin/main`, no numerical witness moves, and bean `qou-mba8` (the post-stabilization algorithms annex overhaul task) stays parked in `todo`.

**Blast radius in physics-and-paper terms:**
- **Zero empirical or numerical scoreboard impact under every option (Q1 Options 1–4):** No scored mass ratio, fine-structure value, $\beta$-decay $Q$-value, or nuclear binding residual in `computations/per_observable_100x_status.py`, `computations/derived_masses.py`, or any `.witness.json` file is read from `appendix-mass-binding-algorithms`.
- **Cross-reference blast radius is near-zero across the body of the monograph:** Across all `24` front-matter and body chapters (`introduction` through `q-geometric-langlands`), **`appendix-mass-binding-algorithms` has `0` incoming prose links (`\ref{...}` or `(#...)`) and `0` incoming `.ts` dependency links (`uses:` / `interprets:`)**; its only external callers in the entire 38-chapter repository are `1` back-matter prose link in `appendix-standard-model/sm-open-problems.md` (`#alg:mass-identity`) and `2` entries in `index-of-definitions/definition-index.md` (`#prop:mirror-baseline-cancellation`, `#prop:isovector-chiral-residue`). Likewise, the `4` procedural remarks in Chapter 12 (`nuclear-interactions/nuclear-reduction-algorithm`, `groebner-reduction-methods`, `atomic-nf-witness-procedure`, `step-lp-verification`) each have **`0` incoming prose links and `0` incoming `.ts` links**, while Chapter 7's `knots-particles-confinement/universal-ilp-algorithm` (`def:universal-ilp-algorithm`, currently marked `computation.status: "error"`) has only `2` incoming prose links (`gluon-stabiliser-ledger.md`, `definition-index.md`) and `2` incoming `.ts` links (`gluon-stabiliser-ledger.ts`, `molecular-construction/molecular-braid.ts`). By contrast, Chapter 9's `mass-endomorphism/mass-identity` (`def:mass-identity`, defining the categorical mass integrand $\Psi = (\int_A \otimes \mathrm{id})\circ \Delta$) has **`31` incoming prose links and `30` incoming `.ts` links** and is a core mathematical definition — **none** of Q1 Options 1–4 removes or relocates `def:mass-identity`.
- **Sibling-branch overlap:** Active sibling branch `claude/prior-art-doi-verified-pkg-20261123` (`63446514c77`, bean `qou-cvu9`, consolidated Ch. 0/1/2 prior-art package) touches **`0` files** in `appendix-mass-binding-algorithms/`, `knots-particles-confinement/`, or `nuclear-interactions/`, overlapping only additively in `folio/schema/references.ts` and `references.bib`.

**Recommendation (judgement, not a finding):** I recommend **Q1 Option 3 (Compact 9-Block QOU-Delta Algorithms Annex organized by Confinement Layers $\mathcal{L}_0\text{--}\mathcal{L}_4$ + Dual-Certificate Verification)** because it fixes all six post-`#9205..#9221` mathematical contradictions, cuts ~`1,305` lines (~`79%`) of textbook re-derivations and broken repo-internal API prose without breaking a single body-chapter cross-reference, and slots cleanly either as a standalone 5-page annex or as Annex B under Question 2. *(Pick all that apply — e.g. `3`, `2`, or `4` — or add a free-text note under Other.)*

---

##### Q1 Option 1 — Status Quo on `origin/main` (Keep All 22 MBA Blocks + 5 Ch. 7/12 Procedural Blocks Untouched)

- **What it means:** Leave all `22` blocks in `folio/quantum-observable-universe/appendix-mass-binding-algorithms/` (`1,527` `.md` lines + `748` `.ts` lines) and the `5` procedural blocks in Chapter 7 (`knots-particles-confinement/universal-ilp-algorithm`, `59` lines) and Chapter 12 (`nuclear-interactions/{nuclear-reduction-algorithm, groebner-reduction-methods, atomic-nf-witness-procedure, step-lp-verification}`, `59` lines combined) unchanged on `origin/main`.
- **What it costs:** `0` files edited, `0` lines changed, `0` validator or Lean runs, `0` minutes.
- **What it risks:** Leaves **six live mathematical and scholarly defects** exposed to referees on `origin/main` (full file-and-line evidence in §1.3):
  1. *False Diamond Lemma confluence claim for $n \ge 4$:* Both `mba-step02-gs-reduction.md:22-28,44` and `nuclear-interactions/groebner-reduction-methods.md:1-7` assert that the uncompleted 3-rule rewriting system (Hecke quadratic $\sigma_i^2 = h\sigma_i + 1$, far commutativity, and adjacent Yang–Baxter $\sigma_i\sigma_{i+1}\sigma_i = \sigma_{i+1}\sigma_i\sigma_{i+1}$) is confluent on $H_n(q)$ by the Diamond Lemma — a statement **proved false for $n \ge 4$** in QOU's own Lean library (`NotAGSBasis.hecke_not_gs_basis_four`, noted in `appendix-transfer-matrices/tm-gs-normal-form.md:17`), because confluence requires Seok-Jin Kang, In-Sok Lee, Kyu-Hwan Lee, and Hyekyung Oh's (`kangleeleeoh2002`, Prop. 4.3) completion family $T_{i+1,j}T_{i+1} \to T_i T_{i+1,j}$ ($i \ge j$).
  2. *False $S^2 = \mathrm{id}$ and non-degenerate untwisted Gram claims at $q \neq 1$:* `mba-chain-map.md:11` and `mba-step06-frobenius-pairing.md:1-35` assert `Ψ = S² = id` on $H_n(q)$ (which is not a Hopf algebra — `no_rlinear_hecke_inv_antihom` in `62cc0b24599` — while $O_q(\mathrm{SU}(2))$, Sweedler $H_4$, and Taft algebras have non-trivial Nakayama twist $\nu \neq \mathrm{id}$ and $S^2 \neq \mathrm{id}$ per `#9205/#9206`) and call the untwisted pairing $\mathrm{tr}_M(a\cdot b)$ non-degenerate on $H_n(q)$ (contradicting Convention-D Gram singularity $\det G = 0$ for $n \ge 3$ in `#9207` `prop:gram-degeneracy-blocks-connes` and the `2026-11-22` owner ruling on `qou-baov` requiring the twisted $\ast$-form $\tau(X X^\dagger)$).
  3. *Float64 interior-point solver (`numpy+cvxpy`) on a singular Gram matrix:* `mba-step10-confinement-sdp.{ts,md}` and `mba-sidecar-lp-sdp-dual-emission.{ts,md}` declare `engine: "python+numpy+cvxpy"` on the rank-deficient $6\times 6$ $H_3(q_0)$ Gram matrix, lagging behind PR `#9208` (`06253f4b4b4`, `QOU/Nuclear/ECatRadicalShadowPriceEvaluation.lean`, which evaluates the exact solver-free $(1^3)$ radical shadow price over $\mathbb{Q}(q_0)$) and PR `#9212` (`e5e181fad21`, `SymmetryReducedDualCertificate.lean`, which places numerical solvers outside the trusted kernel).
  4. *Broken `def:universal-ilp-algorithm` in Ch. 7:* `universal-ilp.py` crashes with `NameError: apply_atom_nf is not defined` (`computation.status: "error"`), hardcodes gluon $= \sigma_0\sigma_0$ (whereas owner ruling `2026-11-22` keeps the step-4 gluon open across 4 arms), and is superseded by the landed 5-layer `ConfinementLayerTower.lean` (`#9214`, `70e23fed87a`).
  5. *Zero inline citations (`cites = []`)* in `mba-step02`, `mba-step03`, `mba-step05`, `mba-step07`, and `mba-step10`, plus two live bibliography bugs in `folio/references/` (`ram1991.json` carries Bidaut-Véron & Véron's PDE DOI `10.1007/BF01243922` instead of Arun Ram's `10.1007/BF01243921`; `hoefsmit1974.json` misstates Peter Norbert Hoefsmit's given name as `"Philippus Nicolaas"` and omits UBC DataCite DOI `10.14288/1.0080112`).
  6. *`50` broken `../../../computations/...` and `../../../tools/...` relative links* and `10` internal `CAL-1/2/3` and `L1/L2` repo-jargon leaks in published monograph prose (`qou-nmjd`).
- **What it commits to:** Deferring all algorithmic accuracy, citation, and voice-leak fixes in back-matter until a later pass.
- **Preview (current `origin/main` contradictions in `mba-step02` & `mba-step06`):**
  ```markdown
  # mba-step02-gs-reduction.md:22-25, 44 (currently on origin/main — FALSE for n >= 4)
  a. Apply braid relations σ_iσ_jσ_i = σ_jσ_iσ_j (|i-j| = 1) ...
  The Diamond Lemma guarantees that any reduction order reaches the same normal form...

  # mba-step06-frobenius-pairing.md:1-4, 29-30 (currently on origin/main — contradicts #9205..#9208)
  Compute the symmetric bilinear pairing <a, b>_F = tr_M(a · b) on H_n(q) and
  verify the categorical self-duality Ψ = S² = id ... making it symmetric and non-degenerate.
  ```

---

##### Q1 Option 2 — Surgical In-Place Bug-Fix, Prior-Art Citation & Jargon-Scrub Pass (Keep 22-Block Layout)

- **What it means:** Preserve the existing 4-section, 22-block layout of `appendix-mass-binding-algorithms` and keep all `5` Chapter 7/12 blocks in place, editing them in place to: (a) fix the six mathematical/factual errors above (adding Kang–Lee–Lee–Oh's completion family for $n \ge 4$, replacing $S^2 = \mathrm{id}$ and untwisted Gram non-degeneracy with the Nakayama twist $\nu$ and Convention-D $\ast$-Gram radical quotient $TL_n(q) = H_n(q)/\mathrm{rad}\,\tau_q$, documenting solver-free `(1^3)` shadow prices and `mpmath` 80-dps / rationalized dual certificates instead of `numpy+cvxpy`, scoping `/q³` in `mba-step09a` as asserted per `#8964`, and aligning `universal-ilp-algorithm` with the open gluon ruling and `ConfinementLayerTower`), (b) wire live-DOI-verified citations into `mba-step02/03/05/07/10` while fixing `ram1991.json`, `hoefsmit1974.json`, `bokut2001.json`, `orellana1998.json`, `goulart-chen2024.json`, and adding `buchberger2006.json`, and (c) strip all `50` `../../../` repo file links, `CAL-1/2/3` codes (`qou-nmjd`), and `WitnessBuilder` Python/Rust packaging prose.
- **What it costs:**
  - `27` monograph block pairs (`.md` + `.ts`) edited in place (`22` in `appendix-mass-binding-algorithms/`, `1` in `knots-particles-confinement/`, `4` in `nuclear-interactions/`), ~`450` lines modified, net reduction ~`250` lines (`1,645 -> ~1,395` `.md` lines).
  - `6` CSL-JSON bibliography files updated/added (`ram1991.json`, `hoefsmit1974.json`, `bokut2001.json`, `orellana1998.json`, `goulart-chen2024.json`, `buchberger2006.json`) + `folio/schema/references.ts` + `references.bib`.
  - Validation (~20 min at `-j 1` / `nice -n 15`): `run-validate.ts`, `run-validate-references.ts`, `paper-commentary-audit.ts`, `qa-sweep` across modified blocks. Zero Lean rebuilds and zero Python probe re-runs.
- **What it risks:** Fully reversible, zero cross-reference churn, **but** retains ~`1,100` lines of low-density boilerplate (`O(1)` Bring constant-lookup pseudocode in `mba-step04`, textbook Hoefsmit/Buchberger/Clarabel restatements, duplicate GS remarks across Ch. 12 and MBA, and four physics-obstruction propositions/remarks sitting inside an "Algorithms" appendix).
- **What it commits to:** Keeping the legacy `Step 01 .. Step 11 + Sidecars` structure rather than aligning the annex with the 5-layer `ConfinementLayer` ($\mathcal{L}_0 \to \mathcal{L}_4$) architecture landed in `#9214`.
- **Preview (in-place fix in `mba-step06-frobenius-pairing.md` under Option 2):**
  ```markdown
  Evaluate the involution-twisted Markov-trace Gram pairing $\langle a, b\rangle_\ast = \tau_q(a\,b^\ast)$
  ($T_w^\ast = T_{w^{-1}}$) on $H_n(q)$ under Convention D ($z_D = q^3/(q^2+1)$), project modulo the
  $\ge 3$-row trace radical $\mathrm{rad}\,\tau_q$ onto the faithful Temperley–Lieb quotient $TL_n(q)$,
  and verify the Nakayama-twisted Frobenius law $\varepsilon(a b) = \varepsilon(b\,\nu(a))$ on Hopf
  substrate models ($O_q(\mathrm{SU}(2))$, Sweedler $H_4$, Taft $T_m(\zeta)$ where $S^2 \neq \mathrm{id}$).
  ```

---

##### Q1 Option 3 — Prune Textbook Boilerplate & Rebuild Compact 9-Block QOU-Delta Algorithms Annex Along $\mathcal{L}_0\text{--}\mathcal{L}_4$ (Recommended)

- **What it means:** Replace the sprawling `22`-block `appendix-mass-binding-algorithms` (`1,527` `.md` lines) and the `5` redundant/broken Chapter 7/12 procedural blocks (`118` `.md` lines) with a **tight, self-contained `9`-block (~`340` `.md` lines, ~5 PDF pages) QOU-Specific Computational & Certification Algorithms Annex** organized along the 5-layer `ConfinementLayer` ($\mathcal{L}_0 \to \mathcal{L}_4$) spine, enforcing three clean rules:
  1. **Category (A) — Compress standard prior art (`5` MBA blocks + `4` zero-caller Ch. 12 procedural remarks) to 2-sentence live-DOI citations + QOU convention pins:** Instead of re-deriving Kang–Lee–Lee–Oh Hecke Gröbner–Shirshov reduction (`mba-step02`, `nuclear-reduction-algorithm`, `groebner-reduction-methods`), Jones/Geck–Lambropoulou/Orellana Markov traces (`mba-step03`), Hoefsmit/Ram seminormal matrices & Gatermann–Parrilo block-diagonalization (`mba-step05`), Buchberger/Conti–Traverso/Sturmfels–Thomas toric Gröbner bases (`mba-step07`), or Goulart–Chen/Simmons-Duffin interior-point conic solvers (`mba-step10`, `step-lp-verification`), state each external algorithm in **2 sentences with pinpoint theorem/proposition citations** plus QOU's exact parameter pin ($h = q - q^{-1}$, $z_D = q^3/(q^2+1)$, 80-digit `mpmath` arithmetic). Retire pure software-packaging/trivial blocks (`mba-step01` lazy word wrapper, `mba-step04` $O(1)$ tuple return, `mba-sidecar-witness-json-pipeline` `WitnessBuilder` Python API docs, and `atomic-nf-witness-procedure`), and replace broken Ch. 7 `def:universal-ilp-algorithm` (`NameError`) with a concise forward-clean `rem:confinement-layer-operator-selection` pointing to `QOU.MathlibInfra.ConfinementLayerTower`.
  2. **Category (B) — Retain & standardize ONLY the `7` genuinely non-standard QOU algorithmic deltas (+ `1` 1-paragraph opener + `rem:lp-sdp-bootstrap-prior-art` = `9` blocks total):**
     - `prose:mba-intro` (~20 lines): 2-paragraph lecturer-cadence opener defining the mathematical Input/Output/Certification contract across $\mathcal{L}_0\text{--}\mathcal{L}_4$ (zero `pyhecke`/`WitnessBuilder`/`CAL-1/2/3`/`../../../` repo leaks).
     - `alg:hecke-gs-monotone-transfer` (~40 lines): Kang–Lee–Lee–Oh completed Hecke normal form (`kangleeleeoh2002` Prop. 4.3, noting `hecke_not_gs_basis_four` for uncompleted 3-rule systems) coupled to **QOU's monotone non-decreasing generator / fine-Bratteli $2\times 2$ transfer sweep** avoiding $n!$ basis explosion for multi-nucleon braids.
     - `alg:twisted-star-gram-radical-quotient` (~40 lines): **QOU's Convention-D $\ast$-Gram radical projection** $H_n(q_0) \twoheadrightarrow TL_n(q_0) = H_n(q_0)/\mathrm{rad}\,\tau_q$ (`prop:gram-degeneracy-blocks-connes`) and Nakayama-twisted Frobenius verification (`F3`, `#9205/#9206`).
     - `alg:ecat-radical-shadow-price` (~40 lines): **QOU's solver-free 6D $H_3(q_0)$ $(1^3)$ radical shadow-price evaluation** $y_0^\ast = \langle t_{\mathrm{geom}}, r_{[1^3]}\rangle / \langle \mathbf{1}, r_{[1^3]}\rangle$ over $\mathbb{Q}(q_0)$ (`ECatRadicalShadowPriceEvaluation.lean`, `#9208`), bypassing singular interior-point matrices at $\mathcal{L}_0/\mathcal{L}_1$.
     - `alg:confinement-tower-chamber-gs` (~45 lines): **QOU's 5-layer `ConfinementLayer` ($\mathcal{L}_0 \to \mathcal{L}_4$) recursion** combining the 11-rule physical nuclear cluster chamber $\mathcal{G}_{\mathrm{phys}} \subset I_{A_0}$ and Mayer–Jensen capacitated shell promotions (`NuclearChamberGS.lean`, `#9212`) with $\mathcal{L}_3/\mathcal{L}_4$ Mulliken–Parr–Pearson shell-filling and chemical toric stoichiometry (`ConfinementLayerTower.lean`, `#9214`).
     - `alg:substrate-period-mass-resolvent` (~45 lines): **QOU's 80-dps Archimedean period, Clausen $\mathrm{Cl}_2(\pi/3)$, Borromean $F_{\mathrm{Bor}}$ (with `/q³` explicitly marked asserted per `#8964`), and inhomogeneous lepton-resolvent evaluation** (`#9216`, `#9219`) from the physical calibration triple $(m_e, \mathfrak{D}_\beta, m_\pi)$ (renaming `alg:mass-identity` $\to$ `alg:substrate-period-mass-resolvent` to eliminate the naming collision with Ch. 9's `def:mass-identity`, updating the 1 caller in `sm-open-problems.md`).
     - `alg:q-beta-chirality-jet-evaluation` (~35 lines): **QOU's two-term Lagrangian trace & $\mathfrak{Q}_\beta$ chirality/jet evaluation** (`#8838`, `#9211`), explicitly recording the Convention-C vs Convention-D boundary (`decayLadder_zC_threeRow_ne_zero`) and tiered $c_k$ status without fit laundering.
     - `alg:rationalized-dual-slack-certificate` (~35 lines) + `rem:lp-sdp-bootstrap-prior-art` (`21` lines, retained verbatim from `#9212`): **QOU's solver-external rationalized dual-multiplier verification** over generic linearly ordered rings (`SymmetryReducedDualCertificate.lean`, `#9212`).
  3. **Category (C) — Relocate non-algorithmic physics/obstruction blocks to their mathematical home chapters:** Move `prop:mirror-baseline-cancellation` (`31` lines, `lean.ref` `QOU.BraidKnot.mirror_baseline_cancels`) and `prop:isovector-chiral-residue` (`17` lines, `lean.ref` `QOU.BraidKnot.binding_isovector_mirror_from_chiral`) + `rem:tjon-universality-external` (`124` lines, `QOU.MassTheory.TjonSimplexForm`) + condensed `rem:delta-lambda-value-vs-magnitude` (~`35` lines from `mba-sidecar-delta-lambda-closure` + `mba-step09b`) into Chapter 11 (`mass-theory/`) / Chapter 12 (`nuclear-interactions/`), preserving their exact block labels (`prop:mirror-baseline-cancellation`, `prop:isovector-chiral-residue`, `rem:tjon-universality-external`) so `index-of-definitions` and Lean links never break!
- **What it costs:**
  - Net deletion of **`18` redundant/boilerplate block pairs** (`27 -> 9` algorithmic blocks + `4` relocated math/physics blocks; **`1,645 -> ~340` `.md` lines in the annex, saving ~`1,305` `.md` lines / ~18 PDF pages**).
  - `6` CSL-JSON bibliography fixes/additions (`ram1991.json` DOI fix, `hoefsmit1974.json` given-name + DOI fix, `bokut2001.json` DOI, `orellana1998.json` DOI, `goulart-chen2024.json` DOIs, new `buchberger2006.json`) + `folio/schema/references.ts` + `references.bib` + `docs/reorganization-map.md`.
  - `3` cross-reference updates (`appendix-standard-model/sm-open-problems.md`, `knots-particles-confinement/gluon-stabiliser-ledger.{md,ts}`, `molecular-construction/molecular-braid.ts`).
  - Validation (~25–30 min at `-j 1` / `nice -n 15`): `content-graph-analysis.py`, `block-density-audit.py`, `run-validate.ts`, `run-validate-references.ts`, `paper-commentary-audit.ts`, and `qa-sweep`. Zero Lean rebuilds and zero probe re-runs.
- **What it risks:** Removes Python/Rust function-call snippets (`from pyhecke import ...`, `WitnessBuilder.save()`) from the published mathematics PDF; developer API docs already live in `.claude/skills/local/witnessed-values.md` and `compute-author.md`, so developer workflows lose nothing, while monograph readers gain a clean mathematical specification. Fully reversible via `git`.
- **What it commits to:** Enforcing a strict **QOU-Delta-Only** standard in the Algorithms Annex (every algorithm block must state a genuinely non-standard QOU mathematical construction in self-contained mathematical notation, backed by a Lean theorem or 80-dps witness, with textbook algorithms cited in $\le 2$ sentences).
- **Preview (standardized 5-field block template for Q1 Option 3):**
  ```markdown
  **Prior-art reduction.** Standard type-$A_{n-1}$ Iwahori–Hecke Gröbner–Shirshov word reduction follows
  Seok-Jin Kang, In-Sok Lee, Kyu-Hwan Lee, and Hyekyung Oh \cite[Prop.~4.3]{kangleeleeoh2002} (extending
  Leonid A. Bokut and L.-S. Shiao \cite{bokut2001} from $q=1$ Coxeter groups via the completion family
  $T_{i+1,j}T_{i+1} \to T_i T_{i+1,j}$, $i \ge j$; without that family, three-rule Yang–Baxter reduction fails
  confluence at $n \ge 4$), under QOU's unimodular skein parameter $h = q - q^{-1}$ ($\sigma_i^2 = h\sigma_i + 1$)
  and Convention-D Markov parameter $z_D = q^3/(q^2+1)$ \cite{jones1987,geck-lambropoulou-2004,orellana1998}.

  - **Input:** Multi-nucleon generator sequence $\beta = \prod_{g=0}^{3A-2}(c_g\sigma_g + d_g) \in H_{3A}(q_0)$ with monotone step index $g$; partition $\lambda \vdash 3A$ ($\ell(\lambda) \le 2$ on $TL_{3A}(q_0)$).
  - **Output:** Exact irreducible character $\chi^\lambda(\beta) \in \mathbb{Q}(q_0)$ and Markov trace $\tau_{q_0}(\beta) = \sum_{\ell(\lambda)\le 2} y_\lambda(q_0)\,\chi^\lambda(\beta)$ at 80 decimal digits.
  - **QOU delta (monotone fine-Bratteli sweep):** Because each interface crossing $(c_g\sigma_g + d_g)$ acts on a single level $s_g \subset s_{g+1}$ of the Gelfand–Tsetlin chain $\varnothing \subset s_1 \subset \cdots \subset s_{3A} = \lambda$ \cite{hoefsmit1974,ram1997}, trace closure projects each factor onto its $1\times 1$ or $2\times 2$ diagonal edge block, evaluating $\chi^\lambda(\beta)$ in one edge-graph sweep without materializing $(3A)!$ Hecke basis elements or $d_\lambda \times d_\lambda$ matrices.
  - **Complexity & precision:** $O(|E_{\mathrm{Bratteli}}(3A)|)$ arithmetic operations in $\mathbb{Q}(q_0)$ evaluated at 80 decimal places (`truncation_bound <= 1e-60`; zero IEEE-754 binary64 intermediates).
  - **Formal & witness backing:** `QOU.Nuclear.NuclearChamberGS`, `QOU.QBeta.TemperleyLiebTower`; witness `tr-m-atom-via-transfer.witness.json`.
  ```

---

##### Q1 Option 4 — Retire `app:mass-binding-algorithms` Separate Chapter Entirely; Fold the 7 QOU-Delta Blocks Directly Into Body Chapters (Ch. 11, Ch. 12, Ch. 16)

- **What it means:** Delete `folio/quantum-observable-universe/appendix-mass-binding-algorithms/` as a separate back-matter chapter (`quantum-observable-universe.ts:138`), apply all prior-art compressions and mathematical fixes of Q1 Option 3, and place each surviving standardized QOU-delta block directly beside the proposition it realizes in the body chapters:
  - Ch. 11 (`mass-theory/`): `alg:twisted-star-gram-radical-quotient`, `alg:substrate-period-mass-resolvent`, `alg:q-beta-chirality-jet-evaluation`, `rem:tjon-universality-external`, and `rem:delta-lambda-value-vs-magnitude`;
  - Ch. 12 (`nuclear-interactions/`): `alg:hecke-gs-monotone-transfer` (replacing the 4 zero-caller procedural remarks), `alg:ecat-radical-shadow-price`, `alg:rationalized-dual-slack-certificate`, `rem:lp-sdp-bootstrap-prior-art`, `prop:mirror-baseline-cancellation`, and `prop:isovector-chiral-residue`;
  - Ch. 16 (`molecular-construction/`): `alg:confinement-tower-chamber-gs` (beside `iterated-confinement-layer`).
- **What it costs:**
  - Removes `1` entire back-matter appendix immediately (`14 -> 13` appendices even before Question 2), deletes `18` redundant block pairs, moves `11` standardized/physics blocks into Ch. 11, Ch. 12, and Ch. 16, updates `3` chapter manifests + `quantum-observable-universe.ts` + `docs/reorganization-map.md`, and applies the same `6` bibliography fixes as Option 3 (~35–40 min validation including `chapter-complexity-review` and `content-graph-analysis.py` to verify zero new forward edges in Ch. 11/12/16).
- **What it risks:**
  - *Body-chapter pacing risk (Milnor Hallmark H2):* Adding `5` algorithm blocks into Ch. 11 (`mass-theory/`) and `4` algorithm blocks into Ch. 12 (`nuclear-interactions/`) interrupts the theorem–proof narrative flow of Part II for readers who want pure algebra/geometry first and computational evaluation procedures in an annex.
  - *Detangler risk:* Placed in Ch. 11/12, any reference from `alg:confinement-tower-chamber-gs` to Ch. 16 (`molecular-construction`) would create a Part II $\to$ Part III forward edge unless placed in Ch. 16 (after all 5 layers have been defined).
- **What it commits to:** Having zero standalone Algorithms Annex in back-matter (or, if paired with Q2 Option 3, folding only transfer-matrix recurrences into Annex B while keeping mass/LP algorithms inline in Part II/III).
- **Preview (paper manifest diff under Q1 Option 4):**
  ```diff
  --- a/folio/quantum-observable-universe/quantum-observable-universe.ts
  +++ b/folio/quantum-observable-universe/quantum-observable-universe.ts
  @@ -135,7 +135,6 @@
       chapterRef({ dir: "appendix-knot-operations" }),
       chapterRef({ dir: "appendix-knot-operations-archimedean" }),
       chapterRef({ dir: "appendix-transfer-matrices" }),
  -    chapterRef({ dir: "appendix-mass-binding-algorithms" }),
       chapterRef({ dir: "appendix-standard-model" }),
       chapterRef({ dir: "appendix-nf-witnesses" }),
  ```

---
---

#### Question 2 (`qou-anx0` + `qou-lanx`) — Consolidating All 14 Back-Matter Appendices & Building 80-dps Witness-Backed Master Reference Tables

🟡 **Waiting on user — How should we consolidate QOU's currently fragmented `14` back-matter appendices (`332` blocks, `16,823` markdown lines) and upgrade its empirical lookup tables to uniform 80-decimal-place witness-backed master tables with propagated $(m_e, \mathfrak{D}_\beta, m_\pi)$ calibration error bounds?**

Today the back matter of `quantum-observable-universe.ts` (`lines 131-147`) splits closely related material across `14` separate chapters — five of which (`appendix-knot-operations-archimedean`, `appendix-transfer-matrices`, `appendix-mass-binding-algorithms`, `appendix-nf-witnesses`, `appendix-qvalues`) have **`0` incoming prose or dependency links from the `24` body chapters** — while `0` of the `332` back-matter blocks use `:val[...]` directives, `0` of the `63` entries in `folio/values/registry.ts` populate `errorEntry`, and the `4,779`-line periodic-table registry (`recursive-atom-knot-atlas-registry.md`) carries `119` element headers mislabelled `CAL-3 Bound (ppb)` (attributing $Q_\beta$ to CAL-3 instead of $\mathfrak{D}_\beta$ and printing `±0.00` calibration error for the proton) alongside two conflicting retired/fitted ${}^4\mathrm{He}$ binding numbers (`29.9557` MeV at line `272` vs `28.2957` MeV at line `417`). Deciding how aggressively to merge the `14` appendices (`14` vs `9` vs `6` vs `4` annexes), how to fold `appendix-formalisation-notes` into the new Lean 4 Community Libraries Annex (`qou-lanx`), and whether to enforce a uniform 6-column Jacobian error-propagation table schema across all quantitative atlases requires the author's architectural ruling.

**Default if you say nothing or defer:** **Q2 Option 1 (Status Quo on `origin/main`)** stays in effect — all `14` back-matter chapters remain separate as listed in `quantum-observable-universe.ts:131-147`, no master-table schema or `folio/values/registry.ts` entries change, and epics `qou-anx0` and `qou-lanx` remain parked in `todo`.

**Blast radius in physics-and-paper terms:**
- **Empirical comparison honesty (`AGENTS.md`, "The comparison points carry the full burden"):** Options 1 and 2 leave existing numerical table cells untouched; **Options 3 and 4** replace unpropagated or `CAL-3`-mislabelled error columns in back-matter tables with exact 80-dps Jacobian calibration uncertainties $\sigma_{\mathrm{pred}}(O)$ propagated from the experimental uncertainties of $(m_e, \mathfrak{D}_\beta, m_\pi)$ against CODATA-2022 (`10.1103/RevModPhys.97.025002`), PDG-2024 (`10.1103/PhysRevD.110.030001`), and AME2020 (`10.1088/1674-1137/abddb0`, `10.1088/1674-1137/abddaf`), and quarantine retired AME-inverted volume-match rows (`D`, `T`, `${}^3\mathrm{He}$`, census `${}^4\mathrm{He}$`) out of the live prediction column so no reader mistakes a retired fit for a derived bound.
- **Body-chapter link blast radius across all `14` appendices:** Across all `24` body chapters, there are only **`13` incoming prose links** and **`26` incoming `.ts` `uses:` links** into the entire `332`-block back matter (detailed per appendix in §2.1). Preserving block-level `label:` strings (`rem:...`, `prop:...`, `def:...`, `conj:...`) during directory merges keeps `100%` of block-level links green automatically; only chapter-level `#app:...` / `#chap:...` links (`8` prose sites in `introduction/chapter-overview.md`, `authors-note/`, `eightfold-way/eightfold-intro.md`, `climax-volume-mass/mobius-energy-proof.md`, and `stochastic-mechanics/surreal-notation-cheat-sheet.md`) need label aliases or pointer updates.
- **Active sibling-branch sequencing:**
  - `claude/sm8w-ewsb-vew-mh-mz-rg-20261123` (`3293f5ed122`, bean `qou-ewsb`) actively edits `appendix-standard-model/sm-params-higgs.{md,ts}` as part of the 5-branch `qou-sm8w` Standard Model wave -> **Annex C (`appendix-standard-model`) edits must wait until `qou-sm8w` lands**.
  - Bean `qou-lref` (Lean Knowledge-Graph Stage 3 directory refactor `78 -> ~14` dirs under epic `qou-lnkg`) precedes `qou-lanx` -> **Annex E (`appendix-lean-libraries` evolving `appendix-formalisation-notes`) can scaffold its prose and 6-library Reservoir table now, with final module paths stamped once `qou-lref` lands**.
  - Detangler preview exemption (`.claude/skills/local/detangler-integration-watcher.md:72`): `PREVIEW_CHAPTERS = {'introduction', 'notation'}` is keyed by directory name `notation`; if `notation`, `glossary`, and `index-of-definitions` merge into Annex F, keeping `dir: "notation"` (or adding the merged directory slug to `PREVIEW_CHAPTERS`) prevents false forward-reference alarms.

**Recommendation (judgement, not a finding):** I recommend **Q2 Option 3 (Phased Consolidation `14 -> 6` Non-Overlapping Annexes A–F + Uniform 80-dps 6-Column Master Reference Tables with Propagated $(m_e, \mathfrak{D}_\beta, m_\pi)$ Jacobian Uncertainties)** executed in three conflict-free waves (Wave 1 now: Annexes B, E [`qou-lanx`], F; Wave 2: Annex A 80-dps master-table generator & `registry.ts` `errorEntry` upgrade + Annex D surreal merge/`qou-g4x1`; Wave 3 after `qou-sm8w` merges: Annex C Standard Model ledger), because it eliminates all six back-matter overlap clusters, prevents creating a duplicate Lean appendix alongside `appendix-formalisation-notes`, and fixes the `CAL-3` error-propagation defect across all `119` elements at the Comparison Boundary where QOU's physics claims are judged. *(Pick any combination — e.g. `3` on both Q1 and Q2, or `2` now + `3` table schema — or add a note under Other.)*

---

##### Q2 Option 1 — Status Quo on `origin/main` (Keep All 14 Appendices & Current Static/Hybrid Tables Separate)

- **What it means:** Leave all `14` back-matter chapters in `quantum-observable-universe.ts:131-147` (`332` blocks, `16,823` `.md` lines + `7,994` `.ts` lines) untouched, keep `appendix-formalisation-notes` (`25` blocks) as an unstructured filler dump without the `qou-lanx` 6-library Reservoir architecture, and leave `folio/values/registry.ts` and `recursive-atom-knot-atlas-registry.md` as they stand.
- **What it costs:** `0` files touched, `0` lines changed, `0` compute or validator runs.
- **What it risks:**
  1. *Severe structural fragmentation:* Readers face `14` back-matter appendices — including a 3-block `appendix-knot-operations-archimedean` (`153` lines), a 4-block `appendix-nf-witnesses` (`60` lines, documenting a `float64` fallback at $A=13\ldots 60$!), `4` appendices without `tabLabel`s in the web UI, and `5` appendices with zero incoming references from any body chapter.
  2. *Comparison-boundary vulnerabilities in `recursive-atom-knot-atlas-registry.md` (`4,779` lines):* Retains `119` element tables whose last column is mislabelled `CAL-3 Bound (ppb)` (calling $Q_\beta$ CAL-3 instead of $\mathfrak{D}_\beta$ / CAL-2, leaking `CAL-1/2/3` `122` times in violation of `qou-nmjd`, printing `±0.00` calibration uncertainty on the proton, and reporting both `29.9557` MeV [`+5.87%` retired census fit] and `28.2957` MeV [`-0.08 ppm` circular AME match] for ${}^4\mathrm{He}$ while nuclear binding magnitude is open), plus `lines 63-65` depicting the photon as the 4-strand identity $\mathbf{1}_{B_4}$ instead of the ruled chiral vertex $1 + \phi_0\sigma_0 + \phi_1\sigma_1 + \phi_{01}\sigma_0\sigma_1^{-1} \in H_3(R,q)$.
  3. *Missing `qou-lanx` community-library showcase & `pdg2024` citation:* External Lean 4 / `Mathlib4` readers have no map of QOU's `3,845` `.lean` files or its `6` standalone Reservoir-ready math libraries, and `folio/references/` has zero entry for PDG-2024 (`10.1103/PhysRevD.110.030001`).
- **What it commits to:** Keeping the 14-appendix layout and deferring both `qou-anx0` and `qou-lanx`.
- **Preview (current 14-chapter back-matter list in `quantum-observable-universe.ts:132-146`):**
  ```text
  glossary (31) · appendix-knot-periodic-table (14) · appendix-knot-operations (12) ·
  appendix-knot-operations-archimedean (3) · appendix-transfer-matrices (45) ·
  appendix-mass-binding-algorithms (22) · appendix-standard-model (22) ·
  appendix-nf-witnesses (4) · appendix-qvalues (19) · appendix-surreals (100) ·
  appendix-surreals-archimedean (21) · appendix-formalisation-notes (25) ·
  index-of-definitions (1) · notation (13)   [Total: 14 appendices, 332 blocks, 16,823 .md lines]
  ```

---

##### Q2 Option 2 — Conservative Pairwise Merge (`14 -> 9` Appendices) + Evolve `appendix-formalisation-notes` Into `qou-lanx` (Defer Master-Table Rebuild)

- **What it means:** Collapse only the purely structural split-lobes and micro-stubs (`14 -> 9` back-matter chapters) and author the `qou-lanx` Lean 4 Community Libraries Annex inside `appendix-formalisation-notes`, **without** rebuilding the quantitative `Z = 0..118` / particle / $Q$-value tables yet:
  1. Merge `appendix-knot-operations` (`12`) + `appendix-knot-operations-archimedean` (`3`) $\to$ `1` chapter with an explicit pre-wall vs post-wall section divider (`tags: ['archimedean-bridge']`);
  2. Fold the 4-block stub `appendix-nf-witnesses` (`60` lines, scrubbing the $f_{64}$ fallback claim) into `appendix-transfer-matrices` (`45` blocks);
  3. Merge `appendix-surreals` (`100`) + `appendix-surreals-archimedean` (`21`) $\to$ `1` two-part Surreal Annex (fixing the `2` stale $S^2 = \mathrm{id}$ lines in `os-reflection-positivity-from-reeb.md:14,25`);
  4. Merge `notation` (`13`) + `glossary` (`31`) + `index-of-definitions` (`1`) $\to$ `1` Reference Register (retaining `dir: "notation"` so `PREVIEW_CHAPTERS` stays green);
  5. Evolve `appendix-formalisation-notes` (`25` blocks) directly into the **`qou-lanx` Lean 4 Formalization DAG & 6 Community Libraries Annex** (`HeckeTemperleyLieb`, `TwistedFrobeniusHopf`, `ToricConicOpt`, `CompactQuantumMetrics`, `QCalculus`, `BraidKnotOctonion`);
  6. Leave `appendix-knot-periodic-table`, `appendix-qvalues`, `appendix-standard-model`, and `appendix-mass-binding-algorithms` (handled by Q1) as separate chapters for now.
- **What it costs:**
  - `5` back-matter chapter directories consolidated (`14 -> 9`), ~`8` new blocks authored for `qou-lanx`, `quantum-observable-universe.ts` + `docs/reorganization-map.md` + `4` chapter-level `#app:...` links updated; zero Python witness regenerations (~30 min validation at `-j 1` / `nice -n 15`).
- **What it risks:** Low merge risk and zero conflict with `claude/sm8w-*`, **but** leaves the `CAL-3 Bound (ppb)` mislabelling, missing 3-parameter $(m_e, \mathfrak{D}_\beta, m_\pi)$ Jacobian error propagation, `0` `errorEntry` links in `registry.ts`, and conflicting ${}^4\mathrm{He}$ rows in `recursive-atom-knot-atlas-registry.md` unaddressed until `qou-t0fc` / `qou-7p89` run separately.
- **What it commits to:** Structural tidy-up + `qou-lanx` delivery first, decoupling table-schema and witness-propagation work into a separate future decision.
- **Preview (`14 -> 9` back-matter chapters under Q2 Option 2):**
  ```text
  1. appendix-knot-periodic-table · 2. appendix-knot-operations (incl. Archimedean §) ·
  3. appendix-transfer-matrices (incl. NF witnesses) · 4. appendix-mass-binding-algorithms (per Q1) ·
  5. appendix-standard-model · 6. appendix-qvalues · 7. appendix-surreals (incl. Archimedean §) ·
  8. appendix-lean-libraries (evolved from formalisation-notes, qou-lanx) ·
  9. notation (Notation, Glossary & Index of Definitions)
  ```

---

##### Q2 Option 3 — Phased Consolidation Into `6` Crisp Non-Overlapping Annexes (A–F) + Uniform 80-dps Witness-Backed Master Tables with Propagated $(m_e, \mathfrak{D}_\beta, m_\pi)$ Uncertainties (Recommended)

- **What it means:** Reorganize the `14` fragmented appendices (`332` blocks, `16,823` `.md` lines) into **`6` cohesive, non-overlapping Reference Annexes (Annexes A–F, ~`165` blocks, ~`6,200` `.md` lines)** and replace prose/static table sprawl with **automated, 80-dps witness-generated dense master tables** governed by one uniform 6-column error-propagation contract:
  - **Annex A (`app:master-atlas`, tab `A`) — Master Braid, Particle, Coupling, Nuclear & Molecular Reference Atlas:** Consolidates `appendix-knot-operations`, `appendix-knot-operations-archimedean`, `appendix-knot-periodic-table`, and the empirical benchmark tables of `appendix-qvalues` (plus cross-referencing Part III molecular benchmarks) into:
    - §A.1 Pre-Archimedean Braid & Hecke Operator Dictionary (generic ring $R$, pre-wall);
    - §A.2 Archimedean Bridge & Calibration Uncertainty Propagation Law (explicitly defining the 3-observable weak/leptonic/mesonic calibration vector $C = (m_e, \mathfrak{D}_\beta, m_\pi)$ with zero internal `CAL-1/2/3` codes per `qou-nmjd`, and both proton-pinned $q_0^{(p)}$ and muon-pinned $q_0^{(\mu)}$ proxy arms);
    - §A.3 Five Uniform 80-dps Witness-Generated Master Tables (**Table A.1** Elementary Particles & Couplings; **Table A.2** Hadron & Eightfold Spectrum; **Table A.3** Weak/$\alpha$/$\beta$ Decay $Q$-Values & Lifetimes; **Table A.4** Nuclide Binding & Atomic Mass Atlas $Z = 0\ldots 118$ with honest `Open` binding cells where parameter-free magnitude is open and retired AME-inverted volume-match figures strictly quarantined out of prediction columns; **Table A.5** Benchmark Molecules $\mathcal{L}_4$), plus the interactive Periodic-Table/Diagram simulators (`sim:knot-periodic-table`, `sim:knot-atom-diagrams`, updated to the ruled chiral photon $\gamma(\phi) = 1 + \phi_0\sigma_0 + \phi_1\sigma_1 + \phi_{01}\sigma_0\sigma_1^{-1}$ and Hopf-link electron $\sigma_0\sigma_1\sigma_0$).
  - **Annex B (`app:algorithms`, tab `B`) — QOU Computational & Transfer-Matrix Algorithms:** Combines the `9` standardized QOU-delta algorithm & certification blocks from **Q1 Option 3** with the non-redundant $2\times 2$ monotone transfer-matrix theorem/proof (`prop:tm-gs-normal-form`, `prf:tm-gs-normal-form`, `tm-general-form`) and exact Pauli/five-two algebraic propositions from `appendix-transfer-matrices`, `appendix-nf-witnesses` (scrubbing `f_{64}`), and `appendix-qvalues` (~`24` blocks total, replacing `90` blocks across 4 appendices).
  - **Annex C (`app:standard-model`, tab `SM`) — Standard Model Parameter & Gauge Ledger:** Retains `appendix-standard-model` as a dedicated 26-parameter & gauge-groupoid annex, refreshed **after** the 5 in-flight `claude/sm8w-*` branches merge (and moving any proved Eightfold blocks to Ch. 8 per `qou-akee`), with uniform Table A.1/A.2 cross-links and `CAL-2` prose codes replaced by $\mathfrak{D}_\beta$ (`qou-nmjd`).
  - **Annex D (`app:surreals`, tab `No`) — Surreal & Non-Archimedean Substrate Lift:** Unifies `appendix-surreals` (Part D.1: Pre-Archimedean Conway normal form, birthday grading, Goncharov depth correspondence) and `appendix-surreals-archimedean` (Part D.2: Post-wall `st`-part functor, Écalle–Borel median resummation, $q_0$ evaluations), remediating the `6` vacuous conjecture kernels of `qou-g4x1` and the `2` stale $S^2 = \mathrm{id}$ claims in `os-reflection-positivity-from-reeb.md:14,25`.
  - **Annex E (`app:lean-libraries`, tab `Lean`) — Lean 4 Formalization DAG & Reusable Community Libraries (`qou-lanx`):** Evolves `appendix-formalisation-notes` (`25` blocks) directly into the single Lean Annex (avoiding a duplicate Lean appendix!), presenting: (1) the 4-tier Knowledge-Graph DAG across all `3,845` `.lean` files (`Mathlib4` $\to$ Pure-Math Reusable Subgraphs $\to$ Generic-Ring QOU Categorical Core [§7c] $\to$ Archimedean Comparison Boundary), (2) the `[propext, Classical.choice, Quot.sound]` trust & vacuity-audit boundary (`0 sorry`, `0` custom axioms), (3) Tier-A `Mathlib4` core upstreaming targets (Clausen/Bloch–Wigner dilogarithm fillers already in `formalisation-notes`, Laurent units, symmetry-reduced Farkas/LP duality), and (4) Tier-B's **`6` standalone Reservoir-ready Lean 4 community libraries** (`HeckeTemperleyLieb`, `TwistedFrobeniusHopf`, `ToricConicOpt`, `CompactQuantumMetrics`, `QCalculus`, `BraidKnotOctonion`) with their dependency DAG and public theorem signatures.
  - **Annex F (`chap:notation`, tab `Ref`) — Notation, Glossary & Index of Definitions:** Combines `notation` (§F.1 Symbol Register & Collision Ledger, keeping `dir: "notation"` so `detangler-integration-watcher` preview exclusion works out of the box), `glossary` (§F.2 Categorical & Geometric Glossary), and `index-of-definitions` (§F.3 Complete Definition & Theorem Index).
- **What it costs:**
  - Phased across **3 clean PR waves** so no PR exceeds reviewer bandwidth or collides with active siblings:
    - *Wave 1 (unblocked now, ~45 min):* **Annex B** (Q1 Option 3 + transfer-matrix/NF/five-two consolidation), **Annex E** (`qou-lanx` evolving `appendix-formalisation-notes`), and **Annex F** (`notation` + `glossary` + `index-of-definitions`), plus the `8` live-verified bibliography additions/fixes (`ram1991`, `hoefsmit1974`, `bokut2001`, `orellana1998`, `goulart-chen2024`, `buchberger2006`, `ame2020tables`, `pdg2024`).
    - *Wave 2 (~1.5–2 hrs single-threaded `nice -n 15` 80-dps `mpmath` compute + table render):* Build `computations/master_atlas_jacobian_80dps.py` emitting `master-atlas-80dps.witness.json` + regenerated `Z00..Z118` shards (`qou-t0fc`), populate `errorEntry` pairs and dual-anchor `q_0_proton` / `q_0_muon` entries in `folio/values/registry.ts`, render **Annex A** Tables A.1–A.5 with zero hand-edited numbers, and merge **Annex D** (`surreals` + `surreals-archimedean` + `qou-g4x1`).
    - *Wave 3 (sequenced after `claude/sm8w-*` merges, ~30 min):* Refresh **Annex C** (`appendix-standard-model`) and cross-link with Annex A + Ch. 8 (`qou-akee`).
- **What it risks:**
  - Touching `quantum-observable-universe.ts` and moving blocks across directories requires updating `docs/reorganization-map.md` in the same commit (`reorg-map-stale` invariant in `detangler-integration-watcher.md:230-237`) and keeping all block `label:` IDs invariant so `100%` of body-chapter `uses:` and `(#label)` links continue to resolve.
  - Quarantining the retired census/magic-$A$ ${}^4\mathrm{He}$ (`29.9557` MeV) and circular per-$Z$ ${}^4\mathrm{He}$ (`28.2957` MeV) rows out of Table A.4's live prediction column makes the open many-body nuclear binding magnitude visibly `Open (parameter-free under-bound)` in Annex A — which matches `intro-particles-as-knots`, `authors-note`, and `AGENTS.md` anti-fit discipline (`396-400`), but dramatically changes the visual appearance of `recursive-atom-knot-atlas-registry.md`.
- **What it commits to:** Six permanent, non-overlapping back-matter annexes (A–F), zero hand-maintained numbers in quantitative back-matter tables, mandatory 80-dps $(m_e, \mathfrak{D}_\beta, m_\pi)$ Jacobian $\sigma_{\mathrm{pred}}$ columns alongside $\sigma_{\mathrm{exp}}$, and zero `CAL-1/2/3` internal codes in published prose.
- **Preview (6-Annex architecture & uniform 6-column Master Table row schema under Q2 Option 3):**
  ```text
  Back Matter (6 Annexes replacing 14 fragmented chapters; ~165 blocks vs 332):
    Annex A [tab: A]    Master Braid, Particle, Coupling, Nuclear & Molecular Reference Atlas
    Annex B [tab: B]    QOU Computational & Transfer-Matrix Algorithms (includes Q1 Option 3)
    Annex C [tab: SM]   Standard Model Parameter & Gauge Ledger (sequenced post-qou-sm8w)
    Annex D [tab: No]   Surreal & Non-Archimedean Substrate Lift (§D.1 generic R | §D.2 at q_0)
    Annex E [tab: Lean] Lean 4 Formalization DAG & 6 Reusable Community Libraries (qou-lanx)
    Annex F [tab: Ref]  Notation, Glossary & Index of Definitions (dir: "notation", preview-exempt)
  ```
  ```markdown
  | 1. Observable & Layer | 2. Canonical Braid / Motif NF | 3. Symbolic Formula & Tier | 4. Predicted $O_{\mathrm{pred}} \pm \sigma_{\mathrm{pred}}$ (80-dps $(m_e,\mathfrak{D}_\beta,m_\pi)$ Jacobian; $[\Delta_{\mu\text{-pin}}]$) | 5. Experimental $O_{\mathrm{exp}} \pm \sigma_{\mathrm{exp}}$ (Source) | 6. Residual $\Delta$, Rel. (ppb/ppm), Pulls $(\Delta/\sigma_{\mathrm{exp}},\; z_{\mathrm{comb}})$ |
  |---|---|---|---|---|---|
  | $\alpha_{\mathrm{EM}}^{-1}$ ($\mathcal{L}_1/\mathcal{L}_3$) | $T(3,5) = (\sigma_0\sigma_1\sigma_0)^3\sigma_1 \in B_3$, $[10]_q$ CS arm | $q_0[9]_{q_0}[10]_{q_0}\text{ + CS tower}$ · *Conditional (arm open)* | `:val[inv_alpha_cs]{format=measured}` ($[\Delta_{\mu\text{-pin}} = \dots]$) | $137.035999177 \pm 0.000000021$ (`codata2022`) | $-0.365\text{ ppb}$, $-2.38\,\sigma_{\mathrm{exp}}$, $z_{\mathrm{comb}} = \dots$ |
  ```

---

##### Q2 Option 4 — Aggressive 4-Annex Minimalist Back-Matter (Relocate Master Atlas Tables Into Ch. 15 `observations/`, Trim Speculative Millennium Surreals)

- **What it means:** Compress the `14` back-matter appendices all the way down to **`4` compact technical annexes** by moving empirical reference tables into Part III and retiring speculative non-core surreal material:
  - Move the `5` dense 80-dps Master Reference Tables (with the full 6-column $(m_e, \mathfrak{D}_\beta, m_\pi)$ Jacobian schema of Option 3) directly into **Chapter 15 (`observations/`)** as the closing empirical comparison atlas of Part III;
  - Move proved/conjectured Eightfold gauge blocks from `appendix-standard-model` into **Chapter 8 (`eightfold-way/` per `qou-akee`)** and open-problem rows into `authors-note`, retiring `appendix-standard-model`;
  - Prune the `22`-block speculative Millennium-problem surreal section (`sec:millennium-bounds-via-surreals`: RH, BSD, Yang–Mills, P vs NP, Collatz) from `appendix-surreals`, keeping only the core Conway normal form, Goncharov depth-2 Bloch–Suslin theorems, and `st`-part calculus;
  - Retain just **4 Annexes**: **Annex I** (QOU Computational, Knot-Dictionary & Transfer-Matrix Reference), **Annex II** (Core Surreal & Non-Archimedean Substrate Lift), **Annex III** (Lean 4 Formalization DAG & 6 Community Libraries, `qou-lanx`), and **Annex IV** (Notation, Glossary & Index of Definitions).
- **What it costs:**
  - Largest editorial footprint: restructures Chapter 8 (`eightfold-way/`), Chapter 15 (`observations/`), `authors-note/`, and all `14` appendices simultaneously (~2.5–3 hrs across compute + body-chapter detangler passes), plus retiring `22` surreal Millennium blocks (`35` Lean links in `AppendixSurreals/` become unreferenced by monograph blocks unless re-homed).
- **What it risks:**
  - *Body-chapter bloat in Ch. 15 (`observations/`):* Embedding a full $Z = 0\ldots 118$ nuclide atlas inside Part III swells Chapter 15 by >1,500 table lines, breaking reading momentum before Part IV (`fluid-dynamics`, `information-theory`, `q-geometric-langlands`).
  - *Cross-chapter link churn:* `information-theory/skein-filtration-trichotomy` (`uses: ["conj:q-collatz"]`) and `gravity-spacetime/lqg-adm-ashtekar-comparison` (`uses: ["conj:os-reflection-positivity-from-reeb", "rem:yang-mills-surreal-bound"]`) actively depend on `sec:millennium-bounds-via-surreals`, so retiring those `22` surreal blocks breaks `3` Part II/IV body-chapter dependencies unless those body blocks are also rewritten.
  - *Direct collision with active `claude/sm8w-*` branches* if `appendix-standard-model` is dissolved before `qou-sm8w` finishes.
- **What it commits to:** Treating empirical master tables as Part III body content rather than back-matter lookup atlases, and permanently excising the Millennium/Collatz surreal explorations from the monograph.
- **Preview (`14 -> 4` annexes + Ch. 15 Master Atlas under Q2 Option 4):**
  ```text
  Part III Ch. 15 (observations/)  <-- receives Tables M.1..M.5 (80-dps Jacobian Master Atlas)
  Part II  Ch. 8  (eightfold-way/) <-- receives Standard Model gauge blocks (post-qou-sm8w)
  Back Matter (4 Annexes):
    Annex I   Computational, Knot-Operator & Transfer-Matrix Reference
    Annex II  Core Surreal Substrate Lift (Millennium/Collatz 22 blocks retired)
    Annex III Lean 4 Formalization DAG & 6 Community Libraries (qou-lanx)
    Annex IV  Notation, Glossary & Index of Definitions
  ```

---

### 0.2 Structured `ask_question` JSON Payload (Ready for Foreground Coordinator)

```json
{
  "questions": [
    {
      "header": "Q1: Algorithms Annex (qou-mba8)",
      "question": "🟡 Waiting on user — How should we restructure appendix-mass-binding-algorithms (22 blocks) and scattered Ch. 7/12 procedural blocks post-#9205..#9221? (Pick all that apply; add 'Other' with a note if needed.)",
      "is_multi_select": true,
      "options": [
        {
          "label": "1. Status quo on origin/main (Default if silent)",
          "description": "Zero edits; keep all 22 MBA blocks + 5 Ch. 7/12 blocks as-is. Leaves false n>=4 3-rule confluence, S^2=id, float64 cvxpy, and NameError universal-ilp live."
        },
        {
          "label": "2. In-place bug-fix, DOI cites & jargon scrub only",
          "description": "Keep 22-block Step 01..11 layout; fix the 6 post-#9205..#9221 math errors, add verified DOIs (fixing Ram 1991 & Hoefsmit 1974), and strip CAL/repo-path leaks."
        },
        {
          "label": "3. Compact 9-block L_0..L_4 QOU-Delta Annex (Recommended)",
          "description": "Cut ~79% (~1,305 lines): 2-sentence DOI cites for textbook prior art, standardize 7 genuine QOU deltas + dual certs along L_0..L_4, move 4 physics blocks to Ch. 11/12."
        },
        {
          "label": "4. Retire MBA chapter; fold 7 QOU-delta blocks into Ch. 11/12/16",
          "description": "Delete appendix-mass-binding-algorithms completely; place standardized QOU-delta algorithms inline beside their theorems in Part II/III (zero body links break)."
        }
      ]
    },
    {
      "header": "Q2: 14-Appendix Consolidation (qou-anx0 + qou-lanx)",
      "question": "🟡 Waiting on user — How should we consolidate the 14 back-matter appendices (332 blocks) and wire 80-dps (m_e, D_beta, m_pi) error-propagated master tables? (Pick all that apply; add 'Other' with a note if needed.)",
      "is_multi_select": true,
      "options": [
        {
          "label": "1. Status quo on origin/main (Default if silent)",
          "description": "Keep all 14 appendices & static/hybrid tables untouched; leaves 5 zero-caller appendices split, mislabelled CAL-3 Bound columns, and qou-lanx unwritten."
        },
        {
          "label": "2. Pairwise merge (14 -> 9) + qou-lanx Lean Annex only",
          "description": "Merge K+K', NF+TM, Surreals+Arch, Notation+Glossary+Index, and evolve formalisation-notes into the 6-library Lean Annex; defer master-table rebuild."
        },
        {
          "label": "3. Phased 6-Annex (A-F) + 80-dps Jacobian Master Tables (Recommended)",
          "description": "Collapse 14 -> 6 crisp Annexes (A: Atlas, B: Algos/TM, C: SM post-sm8w, D: Surreals, E: Lean 6-lib DAG, F: Ref) + uniform 6-col (m_e, D_beta, m_pi) error bounds."
        },
        {
          "label": "4. Minimalist 4-Annex; move Master Tables to Ch. 15 & trim Surreals",
          "description": "Move 80-dps Master Atlas into Part III observations/, fold SM into Ch. 8, trim 22 Millennium surreal blocks (requires rewriting 3 body callers), keep 4 annexes."
        }
      ]
    }
  ]
}
```

---

## 1. Task 1 Audit (`qou-mba8`): `appendix-mass-binding-algorithms`, Scattered Algorithm Blocks & Live-Verified DOIs

### 1.1 Corpus Scope & Exact Line/Caller Totals on `origin/main` (`e330ab6aa04`)

| Surface | Directory (`quantum-observable-universe.ts` index) | Block count | `.md` lines | `.ts` lines | Body prose callers | Body `.ts` callers | Back-matter callers (external) |
|---|---|---:|---:|---:|---:|---:|---:|
| **Primary Annex (`MBA`)** | `appendix-mass-binding-algorithms` (`[29]`, Back-matter) | **22** *(was 21 before `#9212` added `lp-sdp-bootstrap-prior-art`)* | **1,527** | **748** *(incl. manifest)* | **0** | **0** | **3** (`sm-open-problems` $\to$ `alg:mass-identity`; `definition-index` $\to$ 2 `prop:` blocks) |
| **Ch. 7 Operator ILP** | `knots-particles-confinement` (`[8]`, Ch. 7) | **1** (`universal-ilp-algorithm`) | **59** | **108** | **1** (`gluon-stabiliser-ledger`) | **2** (`gluon-stabiliser-ledger`, `molecular-braid`) | **1** (`definition-index`) |
| **Ch. 9 Mass Integrand** | `mass-endomorphism` (`[10]`, Ch. 9) | **1** (`mass-identity`, `def:mass-identity`) | **40** | **65** | **29** | **29** | **2** (`mba-step09a`, `definition-index`) + **1** `.ts` (`mba-step09a`) |
| **Ch. 11 $\alpha_k$ Procedure** | `mass-theory` (`[12]`, Ch. 11) | **4** (`alpha-k-derivation-procedure*`, `intro-alpha-k-procedure`) | **187** | **56** | **2** | **5** | **1** (`definition-index`) |
| **Ch. 12 Nuclear Procedural Remarks** | `nuclear-interactions` (`[13]`, Ch. 12) | **4** (`nuclear-reduction-algorithm`, `groebner-reduction-methods`, `atomic-nf-witness-procedure`, `step-lp-verification`) | **59** | **49** | **0** | **0** | **0** |
| **Adjacent Computational Appendices** | `appendix-nf-witnesses` (`4`), `appendix-transfer-matrices` (`45`), `appendix-knot-operations` (`12`), `appendix-knot-operations-archimedean` (`3`) | **64** | **1,381** | **821** | **0** | **1** (`trivial-knot-photon-interpretation` $\to$ `rem:knot-operator-basis-table`) | **7** (inter-appendix) |

> [!IMPORTANT]
> **Critical Disambiguation (`mass-endomorphism/mass-identity` vs `mba-step09a-mass-identity`):**
> `folio/quantum-observable-universe/mass-endomorphism/mass-identity.{md,ts}` (`def:mass-identity`, Chapter 9, `40` `.md` lines, `lean.ref: "qou:QOU.Torsion.MassTraceIdentity.massIntegrand"`) is **not** a computational sidecar — it is the **foundational mathematical definition** of the Frobenius mass integrand $\Psi = (\int_A \otimes \mathrm{id})\circ \Delta$, non-abelian holonomy $\mathrm{hol}(w)$, and Temperley–Lieb state sum, cited by `31` prose sites and `30` `.ts` `uses:` sites across Parts I–IV. It **must stay untouched in Chapter 9**. Conversely, `appendix-mass-binding-algorithms/mba-step09a-mass-identity.{md,ts}` (`alg:mass-identity`, `134` `.md` lines) computes the downstream Archimedean nucleon mass ratio at $q_0$ and explicitly opens (`lines 1-3`) by apologizing for colliding with `def:mass-identity`'s name! Under Q1 Options 3–4, `mba-step09a-mass-identity` is renamed `alg:substrate-period-mass-resolvent` to eliminate that collision permanently.

---

### 1.2 Block-by-Block Classification Table (`appendix-mass-binding-algorithms` + Scattered Algorithm Blocks)

Legend for Classification Column:
- **(A) Standard Prior Art $\to$ Compress to 2-Sentence Citation + Input/Output Pin:** Textbook / published literature algorithm currently re-derived without inline citations; compress or fold into the QOU-delta block that calls it.
- **(B) Genuinely Non-Standard QOU Delta $\to$ Retain & Standardize:** Novel QOU mathematical/computational construction (or core body definition) to retain, fix post-`#9205..#9221` assumptions, strip repo-plumbing leaks, and format uniformly.
- **(C) Non-Algorithmic Obstruction / Repo Plumbing $\to$ Relocate or Retire:**Either a mathematical proposition/remark about physics obstructions belonging in Ch. 11/12, or internal software-packaging documentation (`WitnessBuilder`, PyO3 crate layout, broken `apply_atom_nf` stub) to retire from monograph prose.

| # | Block path (`folio/quantum-observable-universe/...`) | Kind & `label` | `.md` / `.ts` lines | Ext. callers (`prose` / `.ts`) | `computation.status` & `cites[]` | Class | Audit Diagnosis, Stale Pre-`#9205..#9221` Assumptions & Action Under Q1 Option 3 |
|---:|---|---|---:|---:|---|---:|---|
| 1 | `appendix-mass-binding-algorithms/mba-intro` | `prose` `prose:mba-intro` | 19 / 12 | 0 / 0 | — / `[]` | **(B/C)** | Leaks internal Rust/Python package stack (`hecke-engine`, `qou-substrate`, `pyhecke-native`, `qou-mass`), `L1`/`L2` jargon, and `computations/` paths (`lines 5-14`). Replace with concise 2-paragraph mathematical scope & $\mathcal{L}_0\text{--}\mathcal{L}_4$ I/O contract. |
| 2 | `appendix-mass-binding-algorithms/mba-chain-map` | `prose` `prose:mba-chain-map` | 29 / 16 | 0 / 0 | — / `[]` | **(C)** | Duplicates `prose:pre-archimedean-derivation-chain`; hardcodes stale `Ψ = S² = id` (`line 11`), `R_s5bb` fit-tier factor in step title (`line 14`), `CAL-3` code (`line 17`), and "Level 6" (`line 26`, superseded by 5-layer $\mathcal{L}_0\text{--}\mathcal{L}_4$ in `#9214`). Fold summary into `prose:mba-intro` / Annex B lead. |
| 3 | `appendix-mass-binding-algorithms/mba-step01-categorical-action` | `algorithm` `alg:categorical-action` | 68 / 23 | 0 / 0 | `verified` (rust) / `[]` | **(C)** | Trivial identity pass-through ("stored implicitly as a braid word until passed to Step 2 — lazy", `lines 46-49`) + `tools/hecke-engine/src/lib.rs` link. Retire standalone block; 1-sentence input pin on `alg:hecke-gs-monotone-transfer`. |
| 4 | `appendix-mass-binding-algorithms/mba-step02-gs-reduction` | `algorithm` `alg:gs-reduce-to-hecke-nf` | 82 / 24 | 0 / 0 | `verified` (rust) / **`[]`** | **(A)** | **Mathematical error (`lines 22-28, 44`):** Claims 3-rule Yang–Baxter + Hecke system is confluent by Diamond Lemma for general $H_n(q)$ — **refuted for $n \ge 4$** by `NotAGSBasis.hecke_not_gs_basis_four`! Zero citations. Compress to 2-sentence citation of `kangleeleeoh2002` Prop. 4.3 + `bokut2001` inside `alg:hecke-gs-monotone-transfer`. |
| 5 | `appendix-mass-binding-algorithms/mba-step03-markov-trace` | `algorithm` `alg:markov-trace` | 106 / 25 | 0 / 1 (self: `step09b`) | `verified` / **`[]`** | **(A+B)** | `lines 1-95` re-state textbook Markov-trace / Wedderburn evaluation (`jones1987`, `geck-lambropoulou-2004`, `orellana1998`) with `cites=[]` + `L1/L2` & `../../../` links; **`lines 102-106` contain genuine QOU delta** (monotone non-decreasing nucleon generator / fine-Bratteli edge transfer sweep avoiding $n!$). Retain `lines 102-106` standardized as `alg:hecke-gs-monotone-transfer`. |
| 6 | `appendix-mass-binding-algorithms/mba-step04-bring-brane` | `algorithm` `alg:bring-brane` | 58 / 23 | 0 / 0 | `verified` / `[]` | **(C)** | Not an algorithm: `Input: (none)`, `Complexity: O(1) — table lookup`, `Return χ = -6, g = 4` (`lines 8-35`). Pure boilerplate duplicating `def:brings-surface`; retire. |
| 7 | `appendix-mass-binding-algorithms/mba-step05-wedderburn` | `algorithm` `alg:wedderburn-decomposition` | 74 / 25 | 0 / 0 | `verified` / **`[]`** | **(A)** | Re-states standard Young–Hoefsmit seminormal representations and hook-length dimensions with `cites=[]` + `../../../tools/pyhecke/...` links. Compress to 2-sentence citation (`hoefsmit1974`, `wenzl1988`, `ram1991`, `ram1997`, `gatermann-parrilo2004`) inside `alg:hecke-gs-monotone-transfer` / `alg:twisted-star-gram-radical-quotient`. |
| 8 | `appendix-mass-binding-algorithms/mba-step06-frobenius-pairing` | `algorithm` `alg:frobenius-pairing` | 65 / 24 | 0 / 0 | `verified` / `[]` | **(B)** | **Three stale pre-`#9205..#9208` errors (`lines 1-35, 58-65`):** Asserts `Ψ = S² = id` on $H_n(q)$, untwisted $\mathrm{tr}_M(a\cdot b)$ non-degeneracy & positivity (`qou-baov`), and claims no witness JSON exists (ignoring `frobenius-pairing-compute-audit.witness.json`). Rebuild as `alg:twisted-star-gram-radical-quotient` (`StarFrobeniusPositiveData`, Convention-D $\mathrm{rad}\,\tau_q$ quotient to $TL_n(q)$, Nakayama twist $\nu$ on Hopf models). |
| 9 | `appendix-mass-binding-algorithms/mba-step07-gb-filtration` | `algorithm` `alg:gb-filtration` | 62 / 26 | 0 / 0 | `verified` / **`[]`** | **(A)** | Standard Coxeter length filtration $\operatorname{span}\{T_w : \ell(w) \le \ell\}$ (`authorNotes` confirms $E_2$ collapse was already withdrawn in `qou-6qbv`). Compress into 2-sentence citation + filtration pin on `alg:q-beta-chirality-jet-evaluation` / `alg:confinement-tower-chamber-gs` (`buchberger2006`, `conti-traverso1991`, `sturmfels-thomas1997`). |
| 10 | `appendix-mass-binding-algorithms/mba-step08-jet-prefix` | `algorithm` `alg:jet-prefix-transport` | 60 / 26 | 0 / 0 | `verified` / `[]` | **(A/B)** | Elementary Taylor/Laurent series truncation in $h = q - 1$ up to order $h^N$ (`lines 20-25`) paired with `conj:jet-prefix-gb-filtration` and `70 dps / 60 dps` stale precision constants (now `80 dps` on L2 probes). Merge 1-paragraph jet-truncation bound into `alg:q-beta-chirality-jet-evaluation`. |
| 11 | `appendix-mass-binding-algorithms/mba-step09a-mass-identity` | `algorithm` `alg:mass-identity` | 134 / 41 | 1 (`sm-open-problems`) / 0 | `verified` / `['martelli2016']` | **(B)** | Genuine QOU Archimedean period & ratio evaluation, **but**: (1) collides with Ch. 9 `def:mass-identity`; (2) title still carries fit-tier `R_s5bb`; (3) omits `#8964`/`#9221` ruling that `/q³` in $F_{\mathrm{Bor}}$ is asserted, not derived; (4) uses `50-dps` & `CAL-1`/`CAL-2` codes (`qou-nmjd`); (5) lacks `#9216` inhomogeneous lepton resolvent & `#9219` intra-nucleon EM updates. Standardize as `alg:substrate-period-mass-resolvent` (~45 lines). |
| 12 | `appendix-mass-binding-algorithms/mba-step09b-per-isotope-binding` | `algorithm` `alg:per-isotope-binding` | 64 / 38 | 0 / 0 (self: `delta-lambda`) | `experimental` / `['garoufalidis-gu-marino2021']` | **(C)** | Explicitly states (`lines 25-36, 54, 60`) that `CKRecursion` seeds ($r_{\mathrm{res}} \approx 2.596$, $+1.4947 m_e$) are **calibrated phenomenological fits, not derivations**, and its declared witness (`canonical-mass-table-242ppb.witness.json`) has `null` provenance and retired 242-ppb Habiro numbers! Retire as an "algorithm"; fold the honest scope note into relocated `rem:delta-lambda-value-vs-magnitude` in Ch. 11/12. |
| 13 | `appendix-mass-binding-algorithms/mba-step10-confinement-sdp` | `algorithm` `alg:confinement-sdp` | 71 / 23 | 0 / 0 | `verified` (**`python+numpy+cvxpy`**) / **`[]`** | **(A+B)** | Generic interior-point LP solve is textbook prior art (`goulart-chen2024`, `simmons-duffin2015`, `gatermann-parrilo2004`), while `numpy+cvxpy` violates anti-float64 discipline and ignores Convention-D Gram singularity on $H_3(q_0)$. Replace with **QOU delta**: `alg:ecat-radical-shadow-price` (solver-free $(1^3)$ radical shadow price from `#9208`) + `alg:rationalized-dual-slack-certificate` (`#9212`). |
| 14 | `appendix-mass-binding-algorithms/mba-step11-q-beta-truncation` | `algorithm` `alg:q-beta-truncation` | 97 / 40 | 0 / 0 | `verified` / `[]` | **(B)** | Overlaps `90%` with `mba-sidecar-ck-truncation-ladder` (`85` lines); leaks `CAL-1, CAL-2, CAL-3` (`lines 9-10, 69-74`, misnaming $Q_\beta$ as CAL-3 vs `AGENTS.md:2460` CAL-2 $\mathfrak{D}_\beta$!) and lacks `#8838` two-term Lagrangian trace & `#9211` chirality/jet updates. Consolidate with `ck-truncation-ladder` into single 35-line `alg:q-beta-chirality-jet-evaluation`. |
| 15 | `appendix-mass-binding-algorithms/mba-sidecar-delta-lambda-closure` | `algorithm` `alg:delta-lambda-closure` | 85 / 48 | 0 / 0 (self: 2) | `verified` / `['shoji2019', 'springer1976']` | **(C)** | Not an algorithm (evaluates closed formula $(-1)^{n(\lambda)}\dim V_\lambda$ + lists 6 refuted deuteron ansätze and `BindingSaturationCapA4.lean` $A=4$ determinant bound). Convert to `remark` (`rem:delta-lambda-value-vs-magnitude`) and relocate to Ch. 11 (`mass-theory/`) beside `prop:delta-lambda-dt-index-unification`. |
| 16 | `appendix-mass-binding-algorithms/mba-remark-tjon-universality-external` | `remark` `rem:tjon-universality-external` | 124 / 23 | 0 / 0 | — / `['ame2020', 'hammer2007fourbody', 'jurgenson2009srg', 'platter2005tjon']` | **(C)** | Exemplary scholarly nuclear-EFT comparison remark (`QOU.MassTheory.TjonSimplexForm`), **zero algorithmic content**. Relocate intact (preserving label `rem:tjon-universality-external`) to Ch. 12 (`nuclear-interactions/`) or Ch. 11 (`mass-theory/`). |
| 17 | `appendix-mass-binding-algorithms/mba-sidecar-mirror-cancellation` | `proposition` `prop:mirror-baseline-cancellation` | 31 / 78 | 1 (`definition-index`) / 0 (self: 1) | **`failed`** (20 raw float64 upstream) / `[]` | **(C)** | Mathematical `proposition` (`QOU.BraidKnot.mirror_baseline_cancels`) on mirror nuclei $(Z,N) \leftrightarrow (N,Z)$, **not an algorithm**. Relocate intact (preserving `prop:mirror-baseline-cancellation`) to Ch. 12 (`nuclear-interactions/`). |
| 18 | `appendix-mass-binding-algorithms/mba-sidecar-isovector-chiral-residue` | `proposition` `prop:isovector-chiral-residue` | 17 / 24 | 1 (`definition-index`) / 0 | — / `[]` | **(C)** | Conditional mathematical `proposition` (`QOU.BraidKnot.binding_isovector_mirror_from_chiral`) paired with `prop:mirror-baseline-cancellation`. Relocate intact (preserving `prop:isovector-chiral-residue`) to Ch. 12 (`nuclear-interactions/`). |
| 19 | `appendix-mass-binding-algorithms/mba-sidecar-ck-truncation-ladder` | `algorithm` `alg:ck-truncation-ladder` | 85 / 37 | 0 / 0 | `verified` / `[]` | **(B/C)** | Duplicate of `mba-step11-q-beta-truncation` (`lines 1-85`); carries Convention-C cache warning (`decayLadder_zC_threeRow_ne_zero`) and `CAL-2`/`CAL-3` codes. Merge non-redundant Convention-C/D guard into `alg:q-beta-chirality-jet-evaluation` and retire duplicate block. |
| 20 | `appendix-mass-binding-algorithms/mba-sidecar-lp-sdp-dual-emission` | `algorithm` `alg:lp-sdp-dual-emission` | 61 / 22 | 0 / 0 (self: 2) | `verified` (**`python+numpy+cvxpy`**) / `[]` | **(B)** | Mixes CI script plumbing (`lp_dual_witness_validator.py`) with genuine mathematical content: **solver-external rationalized dual-slack optimality & support-uniqueness certification**. Rebuild as mathematical `alg:rationalized-dual-slack-certificate` wired to `QOU.MathlibInfra.SymmetryReducedDualCertificate` (`#9212`). |
| 21 | `appendix-mass-binding-algorithms/lp-sdp-bootstrap-prior-art` | `remark` `rem:lp-sdp-bootstrap-prior-art` | 21 / 47 | 0 / 0 | — / `21` verified keys | **(B)** | Just landed in PR `#9212` (`9ce8d04d27a`): clean Milnor-voice scholarly synthesis contrasting CFT/sphere-packing/NPA/Flyspeck bootstraps against QOU's finite-dimensional rationalized dual certificates. **Retain intact** right beside `alg:rationalized-dual-slack-certificate` (adding journal DOI `10.1007/s12532-026-00320-7` to `goulart-chen2024.json`). |
| 22 | `appendix-mass-binding-algorithms/mba-sidecar-witness-json-pipeline` | `algorithm` `alg:witness-json-pipeline` | 114 / 28 | 0 / 0 | `verified` / `[]` | **(C)** | Pure repository engineering documentation (`WitnessBuilder.save()`, npm/PyPI `witness-schema`, `compute_dps: 65 / 70` contradicting `24-27` vs `38-42` inside the same file!). Already covered in `.claude/skills/local/witnessed-values.md` and `compute-author.md`; retire from monograph PDF (keep 2-sentence reproducibility note in `authors-note` / Annex E). |
| 23 | `knots-particles-confinement/universal-ilp-algorithm` (Ch. 7) | `definition` `def:universal-ilp-algorithm` | 59 / 108 | 2 (`gluon-stabiliser-ledger`, `definition-index`) / 2 (`gluon-stabiliser-ledger`, `molecular-braid`) | **`error`** (`NameError: apply_atom_nf`) / `[]` | **(C $\to$ B)** | Producer crashes since April (`apply_atom_nf` undefined); hardcodes gluon $= \sigma_0\sigma_0$ (violating `2026-11-22` open 4-arm gluon ruling), electron $= \sigma_1^{-1}$, $\mathrm{H}_2$ bond $= T_{2,3}^{-1}$, and untwisted $G x \ge 0$; superseded by `ConfinementLayerTower.lean` (`#9214`). Replace body with clean cross-layer operator-selection summary (`alg:confinement-tower-chamber-gs`) honoring open gluon arms. |
| 24 | `mass-endomorphism/mass-identity` (Ch. 9) | `definition` `def:mass-identity` | 40 / 65 | **31** / **30** | — / `['alexander1923', 'markov1936']` | **(B — Keep in Ch. 9)** | Core mathematical definition of mass integrand $\Psi = (\int_A \otimes \mathrm{id})\circ \Delta$, holonomy monoid, and TL state sum (`MassTraceIdentity.lean`). **Do NOT prune or relocate.** |
| 25 | `nuclear-interactions/nuclear-reduction-algorithm` (Ch. 12) | `remark` `rem:nuclear-reduction-algorithm` | 16 / 18 | **0 / 0** | — / `['leitnerpawloski2004']` | **(A)** | Zero incoming refs; generic 4-bullet inductive division summary superseded by `prop:nuclear-chamber-groebner-basis` (`#9212`) and `alg:hecke-gs-monotone-transfer`. Retire/fold into `alg:hecke-gs-monotone-transfer`. |
| 26 | `nuclear-interactions/groebner-reduction-methods` (Ch. 12) | `remark` `rem:groebner-reduction-methods` | 27 / 12 | **0 / 0** | — / `[]` | **(A/C)** | Zero incoming refs; **repeats the false 3-rule Diamond Lemma confluence claim for $n \ge 4$** (`lines 1-7`) and lists internal Rust engine codenames `v9/v11/v13/v14` (`line 15`). Retire. |
| 27 | `nuclear-interactions/atomic-nf-witness-procedure` (Ch. 12) | `remark` `rem:atomic-nf-witness-procedure` | 7 / 9 | **0 / 0** | — / `[]` | **(C)** | Zero incoming refs; 7-line note about committing JSON certificates to the git repository (`line 5`). Retire (fold Pauli ratio definition into Annex B transfer-matrix block). |
| 28 | `nuclear-interactions/step-lp-verification` (Ch. 12) | `remark` `rem:step-lp-verification` | 9 / 10 | **0 / 0** | — / `[]` | **(C)** | Zero incoming refs; un-witnessed 9-line assertion ("All 20 atoms are verified..."). Superseded by `SymmetryReducedDualCertificate` + `NuclearChamberGS` (`#9212`); retire. |

---

### 1.3 Summary of Stale Pre-`#9205..#9221` Assumptions Caught Across Algorithmic Blocks

1. **Uncompleted 3-Rule Hecke Rewriting Asserted Confluent (`mba-step02-gs-reduction.md:22-28,44` & `nuclear-interactions/groebner-reduction-methods.md:1-7`):** Contradicts `NotAGSBasis.hecke_not_gs_basis_four` and `appendix-transfer-matrices/tm-gs-normal-form.md:17`. Confluence on $H_n(q)$ for $n \ge 4$ requires the Kang–Lee–Lee–Oh (`kangleeleeoh2002`, §4, Prop. 4.3) completion family $T_{i+1,j}T_{i+1} \to T_i T_{i+1,j}$ ($i \ge j$) unless restricted to monotone single-pass chain elements $\Xi_A = \prod_{i=0}^{A-2}\prod_{j=A-1}^{i+1}(c_{ji}\sigma_i + d_{ji})$.
2. **Untwisted Frobenius Pairing, Non-Degeneracy on $H_n(q)$, and $\Psi = S^2 = \mathrm{id}$ (`mba-chain-map.md:11`, `mba-step06-frobenius-pairing.md:1-35`, plus `appendix-surreals/os-reflection-positivity-from-reeb.md:14,25`):** Directly contradicted by `#9205/#9206` (`62cc0b24599`, proving Nakayama-twisted Frobenius pairing `F3`, `no_rlinear_hecke_inv_antihom`, and `StarFrobeniusPositiveData`), `#9207` (`prop:gram-degeneracy-blocks-connes`, proving Convention-D $\det G = 0$ on $H_n(q)$ for $n \ge 3$ and forcing projection to $TL_n(q) = H_n(q)/\mathrm{rad}\,\tau_q$), and owner ruling `2026-11-22` (`qou-baov`, requiring twisted $\tau(X X^\dagger)$ positivity).
3. **Float64 Numerical LP/SDP (`python+numpy+cvxpy`) on Degenerate 6D $H_3(q_0)$ (`mba-step10-confinement-sdp.{ts,md}`, `mba-sidecar-lp-sdp-dual-emission.{ts,md}`, `universal-ilp-algorithm.{ts,md}`):** Superseded by PR `#9208` (`06253f4b4b4`, `QOU/Nuclear/ECatRadicalShadowPriceEvaluation.lean`, proving solver-free algebraic shadow prices on the $(1^3)$ Convention-D radical) and PR `#9212` (`e5e181fad21`, `QOU/MathlibInfra/SymmetryReducedDualCertificate.lean`, formalizing solver-external rationalized dual certificates over generic ordered rings).
4. **Flat `Step 01..11` + Broken `universal-ilp-algorithm` (`NameError: apply_atom_nf`, Gluon $= \sigma_0\sigma_0$) vs 5-Layer `ConfinementLayer` (`#9212`, `#9214`):** Superseded by `QOU/MathlibInfra/NuclearChamberGS.lean` (`9ce8d04d27a`, 11-rule physical nuclear cluster Gröbner basis $\mathcal{G}_{\mathrm{phys}}$ & Mayer–Jensen shell promotions) and `QOU/MathlibInfra/ConfinementLayerTower.lean` (`70e23fed87a`, $\mathcal{L}_0 \to \mathcal{L}_4$ iterated confinement tower & chemical toric stoichiometry), alongside owner ruling `2026-11-22` keeping step-4 gluon stabilization open across 4 arms.
5. **Fixed-Point `f_{64}` Fallback at $A = 13\ldots 60$ (`appendix-nf-witnesses/witness-computation-method.md:25,33`):** Explicitly invokes 64-bit fixed-point evaluation $f_{64}$ for medium nuclei, conflicting with the repository-wide `mpmath >= 50 dps` (`workdps = 80`) zero-float64 precision gate.
6. **Posited $q = 1.020$ Check Across All 14 Appendices (`#9210`, `fc739b155c5`):** Verified **clean (`0` hits)** across all `332` back-matter blocks (`fc739b155c5` retired $q = 1.020$ cleanly in `observations/double-slit-analytical.{md,ts}` and `simulators/double_slit_simulator.html`).
7. **Unqualified `/q³` Normaliser, Convention-C $Q_\beta$ Framing, `50` Broken `../../../` Repo Links, and `149` Back-Matter `CAL-1/2/3` Leaks (`qou-nmjd`):** `mba-step09a` omits `#8964`/`#9221`'s ruling that `/q³` in $F_{\mathrm{Bor}}$ is asserted rather than derived; `mba-step11` and `recursive-atom-knot-atlas-registry.md:386` misname $Q_\beta$ as `CAL-3` (whereas `AGENTS.md:2459-2463` rules $(m_e, \mathfrak{D}_\beta, \mathfrak{D}_\pi)$ with $Q_\beta$ as the proxy for **CAL-2** $\mathfrak{D}_\beta$ and $m_\pi$ as the proxy for **CAL-3** $\mathfrak{D}_\pi$!); and `50` markdown links in `appendix-mass-binding-algorithms` point to `../../../computations/...` or `../../../tools/...`, which fail in standalone PDF/web distribution.

---

### 1.4 Live-DOI-Verified Bibliography Ledger for `qou-mba8` & `qou-anx0` (Crossref + DataCite + `doi.org` Handle API)

Every DOI below was verified live during this audit against the `doi.org` Handle System API (`https://doi.org/api/handles/<DOI>`, **`responseCode == 1` on 18/18 DOIs**) and Crossref (`api.crossref.org/works/<DOI>`) or DataCite (`api.datacite.org/dois/<DOI>`).

> [!CAUTION]
> **Two Live Repository Bibliography Bugs Caught in `folio/references/` on `origin/main`:**
> 1. **`folio/references/ram1991.json` (`lines 288-289`) carries a WRONG DOI (`10.1007/BF01243922`):** Live Crossref verification proves `10.1007/BF01243922` is **Marie-Françoise Bidaut-Véron and Laurent Véron (1991)**, *"Nonlinear elliptic equations on compact Riemannian manifolds and asymptotics of Emden equations"*, *Invent. Math.* **106**(1), 489–539 (off by $+1$ in the Springer suffix!). Arun Ram's true live-verified DOI is **`10.1007/BF01243921`** (`responseCode == 1`).
> 2. **`folio/references/hoefsmit1974.json` (`lines 8-12`) carries a hallucinated author given name (`"Philippus Nicolaas"`) and `DOI: null`:** Live DataCite verification against the University of British Columbia Library Open Collections record proves the author's official name on the dissertation is **Peter Norbert Hoefsmit**, with live-verified UBC DataCite DOI **`10.14288/1.0080112`** (`responseCode == 1`, `https://doi.library.ubc.ca/10.14288/1.0080112`).
> *(A third false-candidate trap was also caught and excluded during live verification: `10.1081/AGB-100106001` is Bertet et al. 2001 on quasi-symmetric functions, whereas Bokut & Shiao 2001 is **`10.1081/AGB-100106002`**.)*

| Bib key (`folio/references/`) | Status on `origin/main` | Full Author List ($\le 5$ named in full per `qou-nq4h`), Title, Venue & Year | Live-Verified DOI & Handle Check (`doi.org` `rc`) | Target Block(s) |
|---|---|---|---|---|
| `bokut2001` | Present (`DOI: null`) — **add DOI** | Leonid A. Bokut and L.-S. Shiao, "Gröbner–Shirshov bases for Coxeter groups", *Commun. Algebra* **29**(9), 4305–4319 (2001) *(scope: $q=1$ finite Coxeter groups)* | **`10.1081/AGB-100106002`** (`rc=1`, Crossref verified) | `alg:hecke-gs-monotone-transfer` (`mba-step02`) |
| `kangleeleeoh2002` | Present & verified | Seok-Jin Kang, In-Sok Lee, Kyu-Hwan Lee, and Hyekyung Oh, "Hecke algebras, Specht modules and Gröbner–Shirshov bases", *J. Algebra* **252**(2), 258–292 (2002) *(§4, Prop. 4.3: type-$A_{n-1}$ $H_n(q)$ GS basis)* | **`10.1016/S0021-8693(02)00071-6`** (`rc=1`, Crossref verified) | `alg:hecke-gs-monotone-transfer` (`mba-step02`, `tm-gs-normal-form`) |
| `hoefsmit1974` | Present (**wrong given name**, `DOI: null`) — **fix both** | **Peter Norbert Hoefsmit**, *Representations of Hecke Algebras of Finite Groups with BN-Pairs of Classical Type*, PhD thesis, University of British Columbia (1974; UBC Open Collections 2010) | **`10.14288/1.0080112`** (`rc=1`, DataCite verified) | `alg:hecke-gs-monotone-transfer` (`mba-step05`) |
| `ram1991` | Present (**WRONG DOI `10.1007/BF01243922`**) — **fix DOI** | Arun Ram, "A Frobenius formula for the characters of the Hecke algebras", *Invent. Math.* **106**(1), 461–488 (1991) | **`10.1007/BF01243921`** (`rc=1`, Crossref verified) | `alg:hecke-gs-monotone-transfer` (`mba-step05`) |
| `ram1997` | Present & verified | Arun Ram, "Seminormal representations of Weyl groups and Iwahori–Hecke algebras", *Proc. London Math. Soc.* **75**(1), 99–133 (1997) | **`10.1112/S0024611597000282`** (`rc=1`, Crossref verified) | `alg:hecke-gs-monotone-transfer` (`mba-step05`) |
| `jones1987` | Present & verified | Vaughan F. R. Jones, "Hecke algebra representations of braid groups and link polynomials", *Ann. of Math.* (2) **126**(2), 335–388 (1987) | **`10.2307/1971403`** (`rc=1`, Crossref verified) | `alg:hecke-gs-monotone-transfer` (`mba-step03`) |
| `wenzl1988` | Present & verified | Hans Wenzl, "Hecke algebras of type $A_n$ and subfactors", *Invent. Math.* **92**(2), 349–383 (1988) | **`10.1007/BF01404457`** (`rc=1`, Crossref verified) | `alg:hecke-gs-monotone-transfer` (`mba-step05`) |
| `geck-lambropoulou-2004` | Present & verified *(1997 Crelle; 2004 arXiv)* | Meinolf Geck and Sofia Lambropoulou, "Markov traces and knot invariants related to Iwahori–Hecke algebras of type B", *J. Reine Angew. Math.* **482**, 191–213 (1997) | **`10.1515/crll.1997.482.191`** (`rc=1`, Crossref verified) | `alg:hecke-gs-monotone-transfer` (`mba-step03`) |
| `orellana1998` | Present (`DOI: null`) — **add DOI** | Rosa C. Orellana, "Weights of Markov traces on Hecke algebras", *J. Reine Angew. Math.* **508**, 157–178 (1999) | **`10.1515/crll.1999.508.157`** (`rc=1`, Crossref verified) | `alg:hecke-gs-monotone-transfer` (`mba-step03`) |
| `gatermann-parrilo2004` | Present (`#9212`) & verified | Karin Gatermann and Pablo A. Parrilo, "Symmetry groups, semidefinite programs, and sums of squares", *J. Pure Appl. Algebra* **192**(1–3), 95–128 (2004) | **`10.1016/j.jpaa.2003.12.011`** (`rc=1`, Crossref verified) | `alg:rationalized-dual-slack-certificate`, `rem:lp-sdp-bootstrap-prior-art` |
| `goulart-chen2024` | Present (`#9212`, `DOI: null`) — **enrich with DOIs** | Paul J. Goulart and Yuwen Chen, "Clarabel: An interior-point solver for conic programs with quadratic objectives", arXiv:2405.12762 (2024); *Math. Program. Comput.* (2026) | **`10.48550/arXiv.2405.12762`** (`rc=1`, DataCite) & **`10.1007/s12532-026-00320-7`** (`rc=1`, Crossref) | `alg:rationalized-dual-slack-certificate`, `rem:lp-sdp-bootstrap-prior-art` |
| `simmons-duffin2015` | Present (`#9212`) & verified | David Simmons-Duffin, "A semidefinite program solver for the conformal bootstrap", *J. High Energy Phys.* **2015**(6), 174 (2015) | **`10.1007/JHEP06(2015)174`** (`rc=1`, Crossref verified) | `alg:rationalized-dual-slack-certificate`, `rem:lp-sdp-bootstrap-prior-art` |
| `buchberger2006` | **Missing** — **add new key** | Bruno Buchberger, "Bruno Buchberger's PhD thesis 1965: An algorithm for finding the basis elements of the residue class ring of a zero dimensional polynomial ideal", *J. Symbolic Comput.* **41**(3–4), 475–511 (2006) | **`10.1016/j.jsc.2005.09.007`** (`rc=1`, Crossref verified) | `alg:confinement-tower-chamber-gs` (`mba-step07`) |
| `conti-traverso1991` | Present (`#9212`) & verified | Pasqualina Conti and Carlo Traverso, "Buchberger algorithm and integer programming", *AAECC-9*, LNCS **539**, 130–139 (1991) | **`10.1007/3-540-54522-0_102`** (`rc=1`, Crossref verified) | `alg:confinement-tower-chamber-gs`, `prop:nuclear-chamber-groebner-basis` |
| `sturmfels-thomas1997` | Present (`#9212`) & verified | Bernd Sturmfels and Rekha R. Thomas, "Variation of cost functions in integer programming", *Math. Program.* **77**(3), 357–387 (1997) | **`10.1007/BF02614622`** (`rc=1`, Crossref verified) | `alg:confinement-tower-chamber-gs`, `prop:nuclear-chamber-groebner-basis` |
| `codata2022` | Present & verified | Peter J. Mohr, David B. Newell, Barry N. Taylor, and Eite Tiesinga, "CODATA recommended values of the fundamental physical constants: 2022", *Rev. Mod. Phys.* **97**(2), 025002 (2025) | **`10.1103/RevModPhys.97.025002`** (`rc=1`, Crossref verified) | Annex A Master Tables A.1, A.3, A.4 |
| `pdg2024` | **Missing** — **add new key** | S. Navas *et al.* (Particle Data Group), "Review of Particle Physics", *Phys. Rev. D* **110**(3), 030001 (2024) | **`10.1103/PhysRevD.110.030001`** (`rc=1`, Crossref verified) | Annex A Master Tables A.1, A.2, A.3; Annex C |
| `ame2020` / `ame2020tables` / `nubase2020` | `ame2020` & `nubase2020` verified; **`ame2020tables` missing DOI** | W. J. Huang, Meng Wang, F. G. Kondev, Georges Audi, and Sarah Naimi, *Chin. Phys. C* **45**(3), 030002 & 030003 & 030001 (2021) | **`10.1088/1674-1137/abddb0`** (I, `rc=1`), **`10.1088/1674-1137/abddaf`** (II, `rc=1` — **add**), **`10.1088/1674-1137/abddae`** (NUBASE, `rc=1`) | Annex A Master Tables A.3, A.4 |

---

## 2. Task 2 Audit (`qou-anx0` + `qou-lanx`): All 14 Back-Matter Appendices & 80-dps Master-Table Error-Propagation Schema

### 2.1 Complete Inventory of All 14 Back-Matter Appendices on `origin/main` (`e330ab6aa04`)

> [!NOTE]
> **Exact Block-Count Reconciliation (`331 -> 332` blocks):** Bean `qou-anx0` recorded `331` `.md` blocks prior to PR `#9212` (`9ce8d04d27a`), which added `lp-sdp-bootstrap-prior-art.{md,ts}` (`+1` block) to `appendix-mass-binding-algorithms`. On `origin/main` at `e330ab6aa04`, the `14` back-matter chapters in `quantum-observable-universe.ts:132-146` contain exactly **`332` `.md` blocks** (`16,823` `.md` lines + `7,994` `.ts` lines = **`24,817` total lines**).

| # | Back-matter directory (`quantum-observable-universe.ts` order) | `label` & `tabLabel` | Blocks (`.md`) | `.md` lines | `.ts` lines | Block-kind breakdown | Incoming prose refs (`body` / `other-app` / `self`) | Incoming `.ts` refs (`body` / `other-app` / `self`) | `lean.ref` / `comp` / `:val` / Liquid `{{}}` | Target under **Q2 Option 3** |
|---:|---|---|---:|---:|---:|---|---|---|---|---|
| 1 | `glossary` | `chap:glossary` (`G`) | **31** | 238 | 495 | `27` rem, `4` prose | `2` / `0` / `0` | `1` / `0` / `16` | `8` / `0` / `0` / `0` | **Annex F** (§F.2 Glossary) |
| 2 | `appendix-knot-periodic-table` | `app:knot-periodic-table` (`T`) | **14** | **5,322** | 574 | `6` rem, `3` tbl, `2` prose, `2` sim, `1` prop | `1` / `1` / `11` | `2` / `1` / `8` | `1` / `3` / `0` / `3` | **Annex A** (§A.3 Table A.4 + sims) |
| 3 | `appendix-knot-operations` | `app:knot-operations` (`K`) | **12** | 290 | 189 | `7` tbl, `4` rem, `1` prose | **`0`** / `0` / `8` | `1` / `1` / `9` | `0` / `3` / `0` / `0` | **Annex A** (§A.1 Pre-wall Dictionary) |
| 4 | `appendix-knot-operations-archimedean` | `app:knot-operations-archimedean` (`K′`) | **3** | 153 | 66 | `2` rem, `1` tbl | **`0`** / `0` / `2` | **`0`** / `3` / `1` | `0` / `0` / `0` / `0` | **Annex A** (§A.2/A.3 Table A.1) |
| 5 | `appendix-transfer-matrices` | `app:transfer-matrices` (`M`) | **45** | 878 | 486 | `27` tbl, `16` prose, `1` prop, `1` prf | **`0`** / `1` / `35` | **`0`** / `0` / `33` | `1` / `0` / `0` / `0` | **Annex B** (§B.2 Transfer Recurrences) |
| 6 | `appendix-mass-binding-algorithms` | `app:mass-binding-algorithms` (`MBA`) | **22** | 1,527 | 748 | `16` alg, `2` prose, `2` prop, `2` rem | **`0`** / `3` / `4` | **`0`** / `0` / `5` | `2` / `17` / `0` / `0` | **Annex B** (§B.1 QOU-Delta Algos; `4` physics blocks $\to$ Ch. 11/12) |
| 7 | `appendix-standard-model` | `app:standard-model` (`SM`) | **22** | 469 | 634 | `12` prose, `4` conj, `4` rem, `2` def | `2` / `6` / `22` | `1` / `0` / `10` | `6` / `1` / `0` / `0` | **Annex C** (post-`qou-sm8w`) |
| 8 | `appendix-nf-witnesses` | `app:nf-witnesses` *(none)* | **4** | 60 | 80 | `3` def, `1` rem | **`0`** / `3` / `0` | **`0`** / `0` / `3` | `3` / `0` / `0` / `0` | **Annex B** (§B.2 Pauli/NF Witnesses) |
| 9 | `appendix-qvalues` | `app:qvalues` *(none)* | **19** | 1,124 | 1,120 | `8` prop, `5` rem, `3` conj, `1` ex, `1` prose, `1` tbl | **`0`** / `12` / `11` | **`0`** / `0` / `17` | `11` / `3` / `0` / `0` | **Annex A** (Table A.3) + **Annex B** (five-two/Habiro props) |
| 10 | `appendix-surreals` | `app:surreals` *(none)* | **100** | 2,910 | 2,451 | `33` rem, `18` conj, `16` tbl, `8` prop, `8` prose, `7` prf, `6` def, `2` thm, `1` lem, `1` ex | `5` / `51` / `122` | `19` / `9` / `114` | `35` / `3` / `0` / `0` | **Annex D** (§D.1 Categorical Surreals) |
| 11 | `appendix-surreals-archimedean` | `app:surreals-archimedean` *(none)* | **21** | 1,599 | 522 | `8` rem, `5` conj, `4` tbl, `2` def, `1` prop, `1` thm | **`0`** / `12` / `14` | `2` / `6` / `15` | `9` / `0` / `0` / `0` | **Annex D** (§D.2 Archimedean Surreals) |
| 12 | `appendix-formalisation-notes` | `app:formalisation-notes` *(none)* | **25** | 323 | 472 | `13` tbl, `7` rem, `4` prop, `1` prose | `1` / `4` / `11` | **`0`** / `0` / `13` | `4` / `1` / `0` / `1` | **Annex E** (`qou-lanx` Lean 4 DAG & 6 Community Libraries) |
| 13 | `index-of-definitions` | `app:index-definitions` (`D`) | **1** | 1,358 | 30 | `1` prose | `1` / `0` / `0` | **`0`** / `0` / `0` | `0` / `0` / `0` / `0` | **Annex F** (§F.3 Definition Index) |
| 14 | `notation` | `chap:notation` (`N`) | **13** | 572 | 127 | `10` tbl, `3` prose | `1` / `0` / `10` | **`0`** / `0` / `0` | `0` / `0` / `0` / `0` | **Annex F** (§F.1 Symbol & Collision Register; `dir: "notation"`) |
| **Total** | **14 Back-Matter Chapters** | `9` with tab, `5` blank | **332** | **16,823** | **7,994** | `332` blocks | **`13` body** | **`26` body** | **`80` / `31` / `0` / `4`** | **`6` Crisp Annexes (A–F)** |

---

### 2.2 Six Back-Matter Overlap Clusters & `qou-lanx` 6-Library Consolidation Plan

1. **Cluster 1 — Split Knot Dictionary Lobes (`appendix-knot-operations` [12 blocks] + `appendix-knot-operations-archimedean` [3 blocks]):**
   - Split originally per Policy A (`q`-usage pre-wall vs post-wall), leaving `appendix-knot-operations-archimedean` as a 3-block orphan with `0` body callers, stale muon-pinned $q_0 = 1.109978595642739\ldots$ (`particle-nf-table.md:11`), and `hadron-level-knot-table.ts` in `status: "failed"`.
   - **Consolidation:** Merge into **Annex A** with §A.1 strictly over generic $R$ (pre-wall) and §A.2–A.3 carrying an explicit Archimedean-wall banner (`tags: ['archimedean-bridge']`, satisfying `.claude/skills/local/detangler-integration-watcher.md:92-98`).
2. **Cluster 2 — Four-Way Duplication of Monotone Transfer Matrices & Pauli Normal-Form Witnesses (`appendix-nf-witnesses` [4 blocks] + `appendix-transfer-matrices` [45 blocks] + `mba-step03:102-106` + Ch. 12 `atomic-nf-witness-procedure`):**
   - `appendix-nf-witnesses` is a 60-line 4-block stub (`def:witness-4he`, `def:witness-8be`, `def:witness-12c`, `rem:witness-computation-method`) with `0` body callers that repeats the exact $(c, d) \in \{(1,0), (1,-h_{\mathrm{A}}), (1,-h_{\mathrm{A}}/2)\}$ crossing table of `appendix-transfer-matrices/tm-general-form.md` while documenting a retired `f_{64}` fallback (`line 33`) and ad-hoc ideals $I_8, I_9$ (`lines 21-22`); meanwhile `tm-knot-pairs.md:62` still writes $K_2 = T_{2,3}$ (electron) instead of the Hopf-link $\sigma_0\sigma_1\sigma_0$ ruling (`2026-11-21`).
   - **Consolidation:** Fold `prop:tm-gs-normal-form`, `prf:tm-gs-normal-form`, `tm-general-form`, and the 3 exact Laurent witnesses (`4He`, `8Be`, `12C`) into **Annex B** §B.2 alongside `alg:hecke-gs-monotone-transfer`, collapsing `27` repetitive small worked-example table-data shards in `appendix-transfer-matrices` into compact witness-backed rows.
3. **Cluster 3 — Split $Q$-Value / Proton-Identity / Status Dashboard Blocks (`appendix-qvalues` [19 blocks] vs `mba-step09a/11` vs `appendix-knot-periodic-table`):**
   - `appendix-qvalues` (`0` body callers, missing `tabLabel`) mixes three distinct genres: (a) `8` pure-algebraic $5_2$-knot / Habiro star-identity propositions (`fivetwo-*`, `habiro-tail-star-identity`, all with Lean refs), (b) duplicate proton-identity and $Q_\beta$ $c_k$-truncation blocks (`proton-mass-substrate-identity*` with typo $q_0 \approx 1.10978$ at `line 3` instead of $1.10998$!, `qbeta-ck-truncation-canonical`), and (c) empirical status/benchmark tables (`per-observable-100x-status-dashboard`, `qvalue-benchmark-table`).
   - **Consolidation:** Route the empirical benchmark rows into **Annex A** (Tables A.1 & A.3), keep the `9` Lean-backed `fivetwo-*` / `habiro-tail-star-identity` propositions in **Annex B** §B.3 (or Ch. 11 `mass-theory/`), and retire the duplicate `proton-mass-substrate-identity` / `qbeta-ck-truncation-canonical` prose in favor of `alg:substrate-period-mass-resolvent` and `alg:q-beta-chirality-jet-evaluation`.
4. **Cluster 4 — Split Surreal Appendices (`appendix-surreals` [100 blocks] + `appendix-surreals-archimedean` [21 blocks]):**
   - `121` blocks (`4,509` `.md` lines, 27% of all back-matter prose!), neither carrying a `tabLabel`, with `6` cross-appendix `.ts` edges and `12` cross-appendix prose links between the two lobes, `2` stale $\Psi = S^2 = \mathrm{id}_A$ assertions in `os-reflection-positivity-from-reeb.md:14,25`, inconsistent muon-pinned 16-dps $q_0$ literals in `collatz-hausdorff-comparison.md:25` and `diophantine-birthday.md:92`, and the `6` statement-only vacuous conjecture kernels tracked in `qou-g4x1`.
   - **Consolidation:** Unify into **Annex D** with two top-level parts (§D.1 Pre-Archimedean Conway & Goncharov Depth Calculus; §D.2 Archimedean `st`-Part & Resurgent Substrate Lift across an explicit Archimedean-wall banner), fixing `os-reflection-positivity-from-reeb.md:14,25` and discharging `qou-g4x1`.
5. **Cluster 5 — Evolving `appendix-formalisation-notes` (`25` blocks) Directly Into `qou-lanx` (**Annex E** — Avoiding a Duplicate Lean Appendix):**
   - Currently `appendix-formalisation-notes` (`323` `.md` lines, `1` body caller from `authors-note-verification.md`, blank `tabLabel`) holds only ad-hoc dilogarithm/Bloch–Wigner filler tables (`19` blocks), `4` mass-kernel gate notes, a 1-line `formalisation-coverage.md`, and `recursive-atom-knot-atlas-interpretation.md` (which is Python script provenance with `6` broken `../../../computations/` links, belonging in Annex A's methodology note, not Lean!).
   - Under `qou-lanx` + `qou-anx0`, **Annex E (`appendix-lean-libraries`, tab `Lean`)** absorbs and upgrades `appendix-formalisation-notes` directly across QOU's **`3,845` `.lean` files**:

| Annex E Section | Scope & Absorbed Blocks | Concrete Lean 4 Modules & Guarantees |
|---|---|---|
| **§E.1 Layered Knowledge-Graph DAG & Trust Boundary** | Evolves `formalisation-coverage` (`1` $\to$ ~`45` lines) | 4-layer DAG (`Mathlib4` $\to$ Tier-B Pure-Math Libraries $\to$ Generic-Ring QOU Core [§7c] $\to$ Archimedean Comparison Boundary); `#print axioms` restricted to `[propext, Classical.choice, Quot.sound]`; `0 sorry`, `0` custom axioms; 4-rule `lean-self-assuming-audit.py` vacuity gate. |
| **§E.2 Tier-A `Mathlib4` Upstreaming Targets** | Consolidates the `19` dilogarithm / `Cl_2` / `BlochWigner` / `BlochGroup` filler blocks of `formalisation-notes` (`323` $\to$ ~`110` dense lines) | `QOU/MathlibExt/LaurentUnits.lean` ($\mathbb{Z}[q,q^{-1}]^\times = \{\pm q^m\}$), `complexLiTwo`, `Cl2PentagonFromBlochWigner.lean`, `PLPolygonalLink.lean` / `PLConeMap.lean` (PL knot topology stages 1–2, `#8902/#9072/#9114`). |
| **§E.3 Tier-B: Six Standalone Reservoir-Ready Lean 4 Community Libraries (`qou-lanx`)** | **New (`6` structured library blocks + `1` dependency-DAG table)** | 1. **`HeckeTemperleyLieb`**: Iwahori–Hecke $H_n(q)$, Kang–Lee–Lee–Oh GS (`NotAGSBasis`), Markov/Jones trace radical (`TemperleyLiebTower`), Young–Hoefsmit seminormal & Schur elements (`ProtonQ3SchurElement`, `CrossNucleonPairWedderburnZRemoval`).<br>2. **`TwistedFrobeniusHopf`**: Nakayama-twisted Frobenius algebras (`F3` ambidextrous adjunction), Sweedler $H_4$, Taft $T_n(\zeta)$, $O_q(\mathrm{SU}(2))$, Woronowicz 3D/4D differential calculus obstruction (`TwistedFrobeniusTower`, `CalculusDimensionObstruction`).<br>3. **`ToricConicOpt`**: Generic-ordered-field Farkas/LP duality, symmetry-reduced central cones, strict complementary-slackness uniqueness (`SymmetryReducedDualCertificate.lean`), Sturmfels–Thomas toric Gröbner/Graver bases (`NuclearChamberGS.lean`, `ConfinementLayerTower.lean`).<br>4. **`CompactQuantumMetrics`**: Ordered-field Rieffel Lipschitz seminorms, scalar-kernel theorem, finite-graph Kantorovich–Rubinstein duality (`FiniteRieffelQuantumMetric.lean`, `UnifiedClockScaleLayers.lean`).<br>5. **`QCalculus`**: Thomae–Jackson $q$-integrals, $q$-Pochhammer/Habiro products, Jackson–Gamow barrier bounds (`UnifiedClockScaleLayers`, `AlphaEmT35Linchpin`).<br>6. **`BraidKnotOctonion`**: Artin braid towers (`MassTraceMarkovClass`), Bring $\Sigma_4$ ($\chi=-6$, $S_5/A_5$ action), octonionic $G_2/\mathrm{SU}(3)$ colour algebra, PL link isotopy. |

6. **Cluster 6 — Split Reference Lookup Registers (`notation` [13] + `glossary` [31] + `index-of-definitions` [1]):**
   - Unifying all three into **Annex F** (`dir: "notation"`, preserving `PREVIEW_CHAPTERS = {'introduction', 'notation'}` in `detangler-integration-watcher.md:72`) gives readers one back-matter lookup destination while cutting `2` top-level appendix chapters (`3 -> 1`).

---

### 2.3 Calibration & Error-Propagation Gaps Measured on `origin/main`

1. **Zero `errorEntry` Wiring in `folio/values/registry.ts` & Near-Zero `:val[...]` Adoption:**
   - `folio/values/registry.ts` (`985` lines, `63` `WitnessedValueEntry` objects across `17` witness files) defines `readonly errorEntry?: string;` (`line 71`) and `format = "measured"` (`line 36`), yet **`0` of `63` entries set `errorEntry`** and **only `3` `:val[...]` directives exist in the entire 38-chapter monograph** (`0` across all `332` back-matter blocks; `70` older `{{ qou.computations... }}` Liquid tags exist, only `4` of which sit in back-matter).
   - Furthermore, `WITNESSED_VALUES.q_0` (`registry.ts:106-116`) still resolves to `computations/q-pinning-50-digit.witness.json` (`derived_50_digit.q`, the **50-dps muon-pinned** $q_0^{(\mu)} = 1.109978595642739\ldots$), whereas `per-observable-100x-status.witness.json` and the monograph's primary mass chain use the **proton-pinned** $q_0^{(p)} = 1.1099785827513808\ldots$! Both pins must be registered explicitly (`q_0_proton` and `q_0_muon` at `80 dps`) rather than conflated under a single 4-digit `q_0` key.
2. **Mislabelled & Incomplete Error Propagation in `recursive-atom-knot-atlas-registry.md` (`4,779` lines):**
   - **Wrong calibration label (`line 386` & `119` element headers `| CAL-3 Bound (ppb) |`):** Attributes free-neutron $Q_\beta$ (`±0.61 eV` older figure vs CODATA-2022 `0.782333559 ± 0.000000380 MeV`) to `CAL-3` instead of $\mathfrak{D}_\beta$ (**CAL-2** per `AGENTS.md:2460`), leaks `CAL-1/2/3` `122` times (`qou-nmjd`), prints `±0.00` calibration floor for the proton (`line 402`, ignoring CODATA-2022 $\sigma(m_e)/m_e = 0.313\,\mathrm{ppb}$ and $\sigma(m_{\mathfrak{p}}/m_e) = 0.029\,\mathrm{ppb}$), adds $N \cdot \sigma(Q_\beta)$ linearly without $\partial O/\partial m_e$ or $\partial O/\partial q_0$, omits $\sigma_{\mathrm{pred}}$ on binding energies $B_q$, and mixes two incompatible retired/circular ${}^4\mathrm{He}$ binding numbers (`29.9557` MeV at `line 272` vs `28.2957` MeV at `line 417`).
3. **Single-Sided Pulls (`\Delta / \sigma_{\mathrm{exp}}` Only) in `per-observable-100x-status` & `qvalue-benchmark-table.md:54-59`:**
   - Current tables divide residuals by $\sigma_{\mathrm{exp}}$ alone, without reporting the propagated theoretical calibration uncertainty $\sigma_{\mathrm{pred}}(O)$, the combined pull $z_{\mathrm{comb}} = \Delta / \sqrt{\sigma_{\mathrm{pred}}^2 + \sigma_{\mathrm{exp}}^2}$, or the proton-pin vs muon-pin anchor sensitivity $\Delta_{\mathrm{pin}}(O) = O(q_0^{(p)}) - O(q_0^{(\mu)})$ (which is vital wherever $\sigma_{\mathrm{exp}} \ll |\Delta_{\mathrm{pin}}|$, such as $m_\mu$ and $\alpha_{\mathrm{EM}}^{-1}$!).

---

### 2.4 Uniform 80-dps Master-Table & $(m_e, \mathfrak{D}_\beta, m_\pi)$ Error-Propagation Schema (`qou-anx0`)

#### A. Physical Calibration Vector & Dual-Proxy Anchor Protocol (Zero `CAL-1/2/3` Prose Codes per `qou-nmjd`)

Every observable $O(m_e, q_0, m_\pi)$ past the Archimedean wall is a smooth algebraic or Clausen/Thomae–Jackson function of at most the **three physical calibration observables** spanning the three real degrees of freedom of $H^1(\Sigma_4) = 2W$ (`QOU.Mass.calibrations_eq_cohomology`):

| Physical Calibration Role (Prose Name) | Mathematical Symbol | Experimental Proxy & Authoritative Reference | Value $\pm \sigma_{\mathrm{exp}}$ (`80-dps` rationalized input) | Relative $\sigma_{\mathrm{exp}}/C_a$ |
|---|---|---|---|---|
| **Leptonic mass unit** ($W$-plane scale) | $m_e$ | Electron rest-mass energy (`codata2022`, DOI `10.1103/RevModPhys.97.025002`) | $0.51099895069 \pm 0.00000000016\;\mathrm{MeV}$ | **$0.3131\;\mathrm{ppb}$** |
| **Weak decay-width modulus** ($W$-plane modulus $\mathfrak{D}_\beta$, fixing $q_0$) | $q_0(\mathfrak{D}_\beta)$ | **Primary Arm P (proton-ratio pin):** $2(\mathrm{Vol}(4_1)/\hbar_{q_0}^2)F_{\mathrm{Bor}}(q_0) - 12 = m_{\mathfrak{p}}/m_e$ (`codata2022`: $1836.152673426 \pm 0.000000032$)<br>**Comparison Arm M (muon-ratio pin):** $\mathrm{Vol}(4_1)/\hbar_{q_0}^2 = m_\mu/m_e$ (`codata2022`: $206.7682827 \pm 0.0000046$)<br>*(Weak cross-check: $Q_\beta(n) = 0.782333559 \pm 0.000000380\;\mathrm{MeV}$, `codata2022`/`ame2020`)* | $q_0^{(p)} = 1.1099785827513808\ldots$, $\sigma(q_0^{(p)}) \approx 1.07 \times 10^{-12}$<br>$q_0^{(\mu)} = 1.1099785956427392\ldots$, $\sigma(q_0^{(\mu)}) \approx 1.36 \times 10^{-9}$ | $\sigma(\hbar_{q_0})/\hbar_{q_0}$: **$0.0087\;\mathrm{ppb}$** (Arm P) vs **$11.1\;\mathrm{ppb}$** (Arm M); pin split $|q_0^{(p)} - q_0^{(\mu)}| = 1.289 \times 10^{-8}$ |
| **Orthogonal meson scale** ($\mathfrak{D}_\pi$ class) | $m_{\pi^\pm}$ (or $m_{\pi^0}$) | Charged pion mass (`pdg2024`, DOI `10.1103/PhysRevD.110.030001`) | $139.57039 \pm 0.00018\;\mathrm{MeV}$ | **$1.290\;\mathrm{ppm}$** ($1290\;\mathrm{ppb}$) |

#### B. Exact 80-dps Fréchet–Jacobian Uncertainty Formula (`workdps = 80`)

In the canonical producer `computations/master_atlas_jacobian_80dps.py` (`mpmath.mp.dps = 80`, serialized at `60` guard-checked digits with `truncation_bound = 1e-60`, zero IEEE-754 `float64`), for every predicted observable $O(C_1, C_2, C_3)$ with independent experimental calibration inputs $C = (m_e, R_{q_0}, m_\pi)$ (where $R_{q_0} = m_{\mathfrak{p}}/m_e$ on Arm P and $R_{q_0} = m_\mu/m_e$ on Arm M, so correlations with $m_e$ are tracked cleanly through the published dimensionless CODATA mass ratios!), compute exact 80-dps complex-step / analytic sensitivities $J_a(O) = \partial O / \partial C_a$ (via implicit differentiation $\partial q_0 / \partial R_{q_0} = [\Phi'(q_0)]^{-1}$) and emit:

$$
  \sigma_{\mathrm{pred}}(O)
  \;=\;
  \sqrt{
    \left(\frac{\partial O}{\partial m_e}\right)^{\!2} \sigma_{m_e}^2
    \;+\;
    \left(\frac{\partial O}{\partial q_0}\frac{\mathrm{d}q_0}{\mathrm{d}R_{q_0}}\right)^{\!2} \sigma_{R_{q_0}}^2
    \;+\;
    \left(\frac{\partial O}{\partial m_\pi}\right)^{\!2} \sigma_{m_\pi}^2
    \;+\;
    \varepsilon_{\mathrm{trunc}}^2
  },
  \qquad
  \varepsilon_{\mathrm{trunc}} \le 10^{-60}.
$$

*(Where $O$ is rendered in $\mathrm{MeV}$ from a dimensionless ratio $\hat{O}(q_0)$ via $O = m_e \hat{O}(q_0)$ and CODATA supplies $\mathrm{cov}(m_e, R_{q_0})$, the full $3\times 3$ CODATA-2022 covariance term $J\,\Sigma_C\,J^{\mathsf{T}}$ is evaluated directly at 80 dps; for calibration-input rows themselves, $\Delta \equiv 0$ by construction and the row is tagged `[Calibration Pin — Non-Scored]` per `per-observable-100x-status-dashboard.md:1`.)*

#### C. Uniform 6-Column Schema Across All Five Annex A Master Tables

Every quantitative lookup table in **Annex A** (**Table A.1** Elementary Particles & Gauge Couplings; **Table A.2** Hadron & Eightfold Multiplets; **Table A.3** Weak, $\alpha$, and $\beta$ Decay $Q$-Values & Lifetimes; **Table A.4** Nuclide Binding & Mass Atlas $Z = 0\ldots 118$; **Table A.5** Benchmark Molecules $\mathcal{L}_4$) shares one invariant 6-column contract:

1. **Species / Observable & Layer:** Standard symbol, quantum numbers $(Z, N)$ or $(I, J^P)$, and confinement layer $\mathcal{L}_k \in \{\mathcal{L}_0, \dots, \mathcal{L}_4\}$.
2. **Canonical Braid / Motif Normal Form:** Strand index $n$, generator word $\beta$ (honoring chiral photon $\sigma_0\sigma_1^{-1}$ and Hopf-link electron $\sigma_0\sigma_1\sigma_0$), Kang–Lee–Lee–Oh / `ChamberGS` normal form, and active Wedderburn/Temperley–Lieb sector $\lambda$.
3. **Symbolic Formula & Epistemic Tier:** Closed-form expression over $\mathbb{Q}(q_0)$ / $\mathrm{Cl}_2(\pi/3)$ / Thomae–Jackson series, plus explicit tier badge (*Calibration Pin* / *Proved* / *Derived* / *Conditional [named class/arm]* / *Open*).
4. **Predicted Value $O_{\mathrm{pred}} \pm \sigma_{\mathrm{pred}}$ (with Pin-Shift Diagnostic):** Rendered automatically via `:val[<id>]{format=measured}` (backed by `errorEntry: "<id>_sigma_pred"` in `folio/values/registry.ts` or witness-driven table generator), plus bracketed proton-vs-muon anchor shift $[\Delta_{\mu\text{-pin}} = O(q_0^{(\mu)}) - O(q_0^{(p)})]$ wherever $\partial O / \partial q_0 \neq 0$.
5. **Experimental Value $O_{\mathrm{exp}} \pm \sigma_{\mathrm{exp}}$ & Pinpoint Source:** CODATA-2022 (`codata2022`), PDG-2024 (`pdg2024`), AME2020 (`ame2020`, `ame2020tables`), or NUBASE2020 (`nubase2020`).
6. **Residual & Dual Pulls:** Signed residual $\Delta = O_{\mathrm{pred}} - O_{\mathrm{exp}}$, relative fractional miss ($\mathrm{ppb}$ / $\mathrm{ppm}$ / $\%$), experimental pull $\Delta/\sigma_{\mathrm{exp}}$, and combined calibration-aware pull $z_{\mathrm{comb}} = \Delta / \sqrt{\sigma_{\mathrm{pred}}^2 + \sigma_{\mathrm{exp}}^2}$.

---

## 3. Recommended Execution & Bean Coordination Notes (For Coordinator)

*(Per operating constraints, `/tmp/qou-beans-latest` was NOT modified or pushed by this worker; the status notes below are ready for the coordinator's bean ledger.)*

- **`qou-mba8` & `qou-anx0` unblocking verification:** All four upstream blocking beans listed in `qou-mba8` and `qou-anx0` (`qou-qzvs`, `qou-udad`, `qou-h6ef`, `qou-5lct`) have landed their core derivations on `origin/main` (`62cc0b24599`, `06253f4b4b4`, `9ce8d04d27a`, `70e23fed87a`). Both beans are ready to transition to `waiting-on-owner` (`🟡` `ask_question` payload in §0.2 above).
- **`qou-lanx` coordination:** Consolidating `appendix-formalisation-notes` (`25` blocks) directly into **Annex E (`appendix-lean-libraries`)** under Q2 Option 2 or Option 3 discharges `qou-lanx` without creating a second Lean appendix; schedule final module-path stamping right after `qou-lref` completes.
- **Immediate standalone bibliography fixes surfaced (`ram1991.json`, `hoefsmit1974.json`, `bokut2001.json`, `orellana1998.json`, `goulart-chen2024.json`, `buchberger2006.json`, `ame2020tables.json`, `pdg2024.json`):** Ready to land in Wave 1 immediately after `claude/prior-art-doi-verified-pkg-20261123` (`qou-cvu9`) merges so `folio/schema/references.ts` and `references.bib` rebase with zero conflict.
