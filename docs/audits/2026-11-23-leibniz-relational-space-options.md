# Leibniz Relational Space in QOU: Post-`#9207` Audit & Architectural Options Brief

**Date:** 2026-11-23 · **Branch:** `claude/leibniz-relational-options-audit-20261123` (off `origin/main` at `e7ceba55f05`)
**Beans:** `qou-wywz` (audit PR `#9207`'s Chapter 0 Leibniz framing and present architectural options to the owner before any further monograph edit), `qou-u58f` (trace-radical $TL_n(q)$ quotient, Leibniz Identity of Indiscernibles, and Rieffel–Connes–Kantorovich–Rubinstein metric finiteness prior art; landed in PR `#9207`), `qou-adwi` + `qou-5uj7` (three-layer scale stratification and finite Rieffel $TL_3(q_0)$ metric; landed in PR `#9207`), `qou-cvu9` (active sibling prior-art branch `claude/prior-art-doi-verified-pkg-20261123` at `63446514c77`)
**Scope of this commit:** **Read-and-analyze decision brief only.** Zero monograph `.md`/`.ts`/`.lean` files, zero computation probes, and zero `.witness.json` files were modified.

---

## 0. Decision Brief & Turnkey `AskUserQuestion` Chat Mirror

> **Usage note for foreground coordinator:** Everything inside §0.1 is formatted to be pasted verbatim above `AskUserQuestion` (satisfying `AGENTS.md` cold-reader rules 1–6: every identifier expanded on first use, decision-first opening, self-contained per-option 4-part frames with concrete prose/Lean previews, explicit default-if-silent, physics-and-paper blast radius, and a 1-sentence recommendation marked as judgement). §0.2 supplies the matching structured `AskUserQuestion` JSON payload (`multiSelect: true`, `🟡` prefix).

### 0.1 Plain-Chat Mirror (Paste Immediately Above `AskUserQuestion`)

🟡 **Waiting on user — How should Gottfried Wilhelm Leibniz's relationalism underpin the Quantum Observable Universe (QOU) monograph, and where should it sit across the Introduction versus downstream chapters?**

Pull request `#9207` (commits `b67c7efb137..5a350c1a535` on `origin/main`) added a single 17-line paragraph in the Chapter 0 Overview (`folio/quantum-observable-universe/introduction/intro.md:90-106`, block `sec:introduction-overview`) equating Leibniz's Principle of the Identity of Indiscernibles (PII) to quotienting the Iwahori–Hecke braid algebra $H_n(q)$ by the null radical $\mathrm{rad}\,\tau_q = \{a \in H_n(q) : \tau_q(a b^\ast) = 0\;\forall b\}$ of the Convention-D Jones–Markov trace ($z_D = q^3/(q^2+1)$) to obtain the Temperley–Lieb algebra $TL_n(q)$, alongside Marc A. Rieffel's Lipschitz-seminorm metric theory in `QOU/InformationTheory/FiniteRieffelQuantumMetric.lean` and `mass-theory/gram-degeneracy-blocks-connes.md`. Choosing whether to leave that Chapter 0 paragraph untouched, tighten its prior-art contrasts and scope caveats in place, thread a three-stop relational spine through Chapter 2 (`quantum-observable-universes/`) and Chapter 13 (`gravity-spacetime/`), or relocate the philosophical discussion out of Chapter 0 into `information-theory/` is an expository and architectural judgement call for the author (`AGENTS.md`, "Ask the owner before changing things").

**Default if you say nothing or defer:** **Option 1 (Status Quo on `origin/main`)** stays in effect — zero files change, `intro.md:90-106` remains as landed in `#9207`, no numerical quantity or witness moves, and bean `qou-wywz` (this architectural review task) stays parked as `needs-owner-ok`.

**Blast radius in physics-and-paper terms:**
- **Zero empirical or numerical impact under every option (Options 1–4):** No scored mass ratio, nuclear binding energy, $\beta$-decay $Q$-value, or fine-structure residual in `per_observable_100x_status.py`, `derived_masses.py`, or `finite_rieffel_tl3_metric_probe.py` (`finite-rieffel-tl3-metric.witness.json`) is read from or altered by any of the four options.
- **Paper, Lean, and sibling-PR surfaces touched per option:**
  - *Option 1:* `0` files.
  - *Option 2:* `1` prose block (`introduction/intro.{md,ts}`, lines `90-106`) + `3` new bibliography entries (`earman1989`, `barbour-bertotti1982` with live-verified DOI `10.1098/rspa.1982.0102`, `rovelli1996` with live-verified DOI `10.1007/BF02302261`). Zero overlap with sibling branch `claude/prior-art-doi-verified-pkg-20261123` (`63446514c77`, bean `qou-cvu9`) except additive lines in `folio/schema/references.ts` and `references.bib`.
  - *Option 3:* `1` edited block in Ch. 0 (`introduction/intro.{md,ts}`), `1` new remark block in Ch. 2 (`quantum-observable-universes/rieffel-metric-quotient-faithfulness.{md,ts}` wired into `sec:categorical-dirac-operator`, giving `QOU/InformationTheory/FiniteRieffelQuantumMetric.lean` its first direct `lean.ref` block link), `2` updated blocks in Ch. 13 (`gravity-spacetime/cr-structure-lorentzian-lift.{md,ts}` and `lqg-adm-ashtekar-comparison.{md,ts}` line `19`), `1` Lean file extended (`QOU/InformationTheory/FiniteRieffelQuantumMetric.lean`, ~55 lines over a generic ordered field), plus the `3` new bibliography entries above. Sequencing note: sibling branch `claude/prior-art-doi-verified-pkg-20261123` (`63446514c77`) edits `categorical-dirac-operator-intro.md` and enriches `lewandowski-nurowski-tafel1990.json` / `nurowski-trautman2002.json`, so Option 3 should stack on or merge after `qou-cvu9`.
  - *Option 4:* `1` trimmed block in Ch. 0 (`introduction/intro.{md,ts}`, removing lines `90-106`) + `1` new self-contained remark block (`information-theory/leibniz-relational-indiscernibility.{md,ts}`) placed beside `rem:spacetime-length-distance-layers` in `information-theory/information-theory.ts:102`, plus the `3` bibliography entries above.

**Recommendation (judgement, not a finding):** I recommend **Option 3 (sequenced right after sibling prior-art branch `qou-cvu9` merges, incorporating Option 2's scope caveats)** because `intro.md:90-106` on `origin/main` currently drops $H_n(q)$ and $TL_n(q)$ cold before knots are introduced and says QOU "fulfills" Leibniz's programme and "recovers... metric geometry" without the Lorentzian CR non-claim (`cr-structure-lorentzian-lift.md:13`), while `FiniteRieffelQuantumMetric.lean` currently has no content block pointing its `lean.ref` to it. *(Pick any combination — e.g. `2`, `3`, `2 + 3`, or `4` — or add a note under Other.)*

---

#### Option 1 — Status Quo on `origin/main` Post-`#9207` (Keep Minimal Ch. 0 Trace-Radical PII Framing Only)

- **What it means:** Leave the 17-line paragraph landed by PR `#9207` (`b67c7efb137`) in `folio/quantum-observable-universe/introduction/intro.md:90-106` (`sec:introduction-overview`, citing `leibniz-clarke1717`, `gelfand-naimark1943`, `segal1947`) together with the downstream Rieffel/Connes remarks in `mass-theory/gram-degeneracy-blocks-connes.md:44-83` and `information-theory/spacetime-length-distance-layers.md:25-28` completely unchanged.
- **What it costs:** `0` files touched, `0` lines changed, `0` validator or Lean builds required, `0` minutes.
- **What it risks:** Three live expository and referee-facing vulnerabilities remain on `origin/main` (documented with line numbers in §1.1 below):
  1. *Scope over-claim risk:* `intro.md:90` says QOU *"fulfills the programme"* of Leibniz and `intro.md:105-106` says it *"recovers differential, contact, and metric geometry downstream"*, without disclosing that `gravity-spacetime/cr-structure-lorentzian-lift.md:13` explicitly records *"No such [four-dimensional Lorentzian metric] lift is constructed here"* and that `mass-theory/hecke-radical-is-temperley-lieb.md:93-97` records that the algebra isomorphism $H_n(q)/\mathrm{rad} \cong TL_n(q)$ written at `intro.md:100` is supported by block/Catalan dimension counts rather than proved as an algebra isomorphism in this paper.
  2. *Milnor linear-argument hazard (Hallmarks H4/H5):* `intro.md:98-100` names the *"Iwahori–Hecke algebra"* and *"Temperley–Lieb quotient ($H_n(q)/\mathrm{rad} \cong TL_n(q)$)"* in the opening overview before braids, knots, or $H_n(q)$ are introduced two subsections later in `sec:introduction-state-space-knots` (`intro-particles-as-knots.md`).
  3. *Missing physics prior-art positioning:* Foundations-of-physics readers seeing a Leibniz relationalism claim will expect explicit positioning against Julian B. Barbour and Bruno Bertotti's classical relational shape dynamics (`10.1098/rspa.1982.0102`) and Carlo Rovelli's relational quantum mechanics (`10.1007/BF02302261`); meanwhile `gravity-spacetime/lqg-adm-ashtekar-comparison.md:19` lists `Relational QM` in a table with no citation.
- **What it commits to:** Keeping Leibniz relationalism as a brief historical analogy in Chapter 0 only, leaving the connection between `intro.md:90-106`, Rieffel's metric kernel theorem (`FiniteRieffelQuantumMetric.lean`), and the Chapter 13 CR spacetime boundary implicit for the reader to assemble.
- **Preview (current `origin/main` text at `folio/quantum-observable-universe/introduction/intro.md:90-106`):**
  ```markdown
  This relational starting point fulfills the programme Gottfried Wilhelm
  Leibniz set out in his 1715--1716 correspondence with Samuel Clarke
  \cite{leibniz-clarke1717}, where time is the chronological order of
  successions, space is the order of coexistences, and the Principle of
  the Identity of Indiscernibles equates states that agree on every
  observable relation. In a braided monoidal category equipped with a
  trace, sequential composition ($\circ$) encodes the order of
  successions, the monoidal product and braiding ($\otimes, \sigma$)
  encode the order of coexistences, and passing from the Iwahori--Hecke
  algebra to its Temperley--Lieb quotient modulo the trace radical
  ($H_n(q)/\mathrm{rad} \cong TL_n(q)$) enforces indiscernibility in the
  algebraic sense of Israel M. Gelfand, Mark A. Naimark, and Irving E.
  Segal \cite{gelfand-naimark1943,segal1947}: combinations annihilated by
  every closed trace pairing coalesce into one observable class. Because
  relational order and trace quotienting state the axioms in full, a
  quantum observable universe posits no background manifold at the outset
  and recovers differential, contact, and metric geometry downstream.
  ```

---

#### Option 2 — Modest Ch. 0 Refinement + Explicit Prior-Art Contrasts & Non-Claims

- **What it means:** Keep Leibniz relationalism strictly confined to `folio/quantum-observable-universe/introduction/intro.{md,ts}` (`sec:introduction-overview`), replacing lines `90-106` with a tightened ~24-line passage in Milnor voice that:
  1. Removes the unglossed forward jump to $H_n(q)/TL_n(q)$ in `sec:introduction-overview` (stating indiscernibility in terms of the already-introduced trace pairing $\int_A$ and the Gelfand–Naimark–Segal null ideal, while pointing gently to the finite-dimensional braid quotient developed in Part II without claiming an in-paper proof of $H_n(q)/\mathrm{rad} \cong TL_n(q)$);
  2. Contrasts QOU's *algebraic* relationalism (no spatial configuration manifold $\mathbb{R}^{3N}$ at the outset; states indistinguishable under all closed trace pairings coalesce in the quotient, and state-space distance emerges from Marc A. Rieffel's Lipschitz seminorms `rieffel1999`) against Julian B. Barbour and Bruno Bertotti's classical Euclidean quotient / best-matching dynamics (`barbour-bertotti1982`, DOI `10.1098/rspa.1982.0102`), John Earman's substantivalism-versus-relationalism taxonomy (`earman1989`), and Carlo Rovelli's observer-relative Hilbert-space relational quantum mechanics (`rovelli1996`, DOI `10.1007/BF02302261`);
  3. Explicitly states what is **not** claimed: while no background $3$-manifold is assumed, the derived Rieffel metric acts on finite algebraic state spaces rather than a four-dimensional Lorentzian spacetime, and constructing a Lorentzian Einstein metric lift from the contact Cauchy–Riemann (CR) three-manifold remains open.
- **What it costs:**
  - `2` monograph files edited: `folio/quantum-observable-universe/introduction/intro.md` (lines `90-106`, ~24 lines replacing 17) and `folio/quantum-observable-universe/introduction/intro.ts` (adding `"earman1989"`, `"barbour-bertotti1982"`, `"rovelli1996"`, `"rieffel1999"` to `cites[]`).
  - `3` new CSL-JSON reference files (`folio/references/earman1989.json`, `barbour-bertotti1982.json`, `rovelli1996.json`) + `folio/schema/references.ts` + regenerated `references.bib` + refreshed `intro.jsonld` / `intro.attestations.json`.
  - Validation runs (~5–10 min at `-j 1` / `nice -n 15`): `run-validate.ts`, `run-validate-references.ts`, `paper-commentary-audit.ts introduction`, `qa-sweep` on `intro`. Zero Lean rebuilds and zero probe runs.
- **What it risks:** Reversible in one `git revert`. Slight risk of making `sec:introduction-overview` one paragraph denser (~7 lines longer than `#9207`) with four additional citations in the opening section; zero detangler risk because Chapter 0 is a designated preview chapter; zero content-file conflict with sibling branch `claude/prior-art-doi-verified-pkg-20261123` (`63446514c77` edits `intro-particles-as-knots.{md,ts}`, not `intro.{md,ts}`).
- **What it commits to:** Framing QOU's relationalism publicly in Chapter 0 with explicit scholarly boundaries (distinguishing algebraic GNS/Rieffel relationalism from classical shape dynamics and RQM, and stating upfront that 3+1 Lorentzian Einstein geometry is open), without adding cross-chapter remarks in Chapters 2 or 13 or extending the Lean library.
- **Preview (proposed replacement for `folio/quantum-observable-universe/introduction/intro.md:90-106`):**
  ```markdown
  This starting point is relational in the sense Gottfried Wilhelm Leibniz
  set out in his 1715--1716 correspondence with Samuel Clarke
  \cite{leibniz-clarke1717,earman1989}: sequential composition ($\circ$)
  records the order of successions, the monoidal product and braiding
  ($\otimes, \sigma$) record the order of coexistences, and the Principle
  of the Identity of Indiscernibles equates processes that agree on every
  closed trace pairing. In the algebraic construction of Israel M. Gelfand,
  Mark A. Naimark, and Irving E. Segal \cite{gelfand-naimark1943,segal1947},
  elements annihilated by every trace pairing form a two-sided null ideal;
  quotienting by that radical identifies empirically indistinguishable
  combinations into one observable class, and Marc A. Rieffel's Lipschitz
  seminorms \cite{rieffel1999} induce a finite transport distance on the
  resulting faithful state space. Unlike the classical relational mechanics
  of Julian B. Barbour and Bruno Bertotti \cite{barbour-bertotti1982},
  which quotients a pre-existing Euclidean configuration space
  $\mathbb{R}^{3N}$ by rigid motions, and unlike Carlo Rovelli's relational
  quantum mechanics \cite{rovelli1996}, which relativises Hilbert-space
  state vectors to pairs of observers while leaving the spacetime metric
  external, a quantum observable universe posits no spatial manifold at the
  outset and enforces observer consistency through a shared fibre functor.
  What this yields downstream is contact Cauchy--Riemann geometry on
  three-dimensional slices and a finite Kantorovich--Rubinstein metric on
  truncated braid quotients; a four-dimensional Lorentzian spacetime lift
  satisfying the Einstein field equations is not constructed here
  ([Gravity and Spacetime Emergence](#chap:gravity-spacetime-emergence)).
  ```

---

#### Option 3 — Cross-Chapter Thread (Ch. 0 PII $\to$ Ch. 2 Rieffel Spectral Distance $\to$ Ch. 13 Causal/CR Relational Bridge + Generic Lean Bridge Theorem)

- **What it means:** Build a concise, detangler-clean three-stop relational spine across the monograph, backed by a generic ordered-field Lean bridge theorem:
  1. **Stop 1 — Ch. 0 (`introduction/intro.md:90-106`, `sec:introduction-overview`):** Keep Chapter 0's opener tight (~14 lines, no unglossed $H_n(q)/TL_n(q)$ symbols), introducing Leibniz's orders of succession ($\circ$) and coexistence ($\otimes, \sigma$) plus operational PII via the GNS trace radical (`leibniz-clarke1717`, `earman1989`, `gelfand-naimark1943`, `segal1947`), and pointing forward to the Ch. 2 metric construction and Ch. 13 spacetime scope boundary.
  2. **Stop 2 — Ch. 2 (`quantum-observable-universes/`, `sec:categorical-dirac-operator`, right after `categorical-dirac-operator-unique-proof` at `quantum-observable-universes.ts:285`):** Add a ~22-line self-contained `remark` block `rem:dirac-rieffel-quotient-metric` (`rieffel-metric-quotient-faithfulness.{md,ts}`) stating how a first-order operator such as $\mathcal{D}_\nabla = q^{-1}\nabla + (1-q^{-1})\iota_\xi\nabla$ induces a Connes–Rieffel Lipschitz seminorm $L(a)$ (`connes1989`, `connes1994`, `rieffel1999`), why non-scalar elements of $\ker L$ (in particular any nonzero trace radical $\mathrm{rad}\,\tau$) send the dual state distance to $+\infty$, and why quotienting modulo $\mathrm{rad}\,\tau$ yields strict metric separation $d_L(\bar{\varphi},\bar{\psi}) = 0 \iff \bar{\varphi} = \bar{\psi}$ — giving `QOU.InformationTheory.FiniteRieffelQuantumMetric` its **first direct `lean.ref` block link** in the paper (`uses: ["def:categorical-dirac-operator", "def:quantum-observable-universe"]` — 100% backward references, zero forward links to Ch. 11 or Ch. 20, obeying strict reading-order rule `qou-d4kh`).
  3. **Stop 3 — Ch. 13 (`gravity-spacetime/cr-structure-lorentzian-lift.{md,ts}` lines `12-17` & `lqg-adm-ashtekar-comparison.{md,ts}` line `19`):** Add `rovelli1996` (`10.1007/BF02302261`) and `barbour-bertotti1982` (`10.1098/rspa.1982.0102`) to `sec:gravity-spacetime-lqg-comparison` (fixing the currently uncited `Relational QM` row at `lqg-adm-ashtekar-comparison.md:19`), and add one crisp paragraph to `cr-structure-lorentzian-lift.md` contrasting QOU's algebraic relational hierarchy (Ch. 0 PII quotient $\to$ Ch. 2 Riemannian/transport state-space metric $d_L$ from $\mathcal{D}_\nabla$ $\to$ Ch. 13 twisting 3D contact CR ray space with Reeb causal ordering $\phi_t = \exp(t\xi)$) against Barbour–Bertotti Euclidean best-matching and substantivalist 4-manifolds, while preserving verbatim the honest non-claim that **no 4D Lorentzian metric lift or full 3+1 Einstein solution is constructed** (and never reviving the withdrawn bilinear-Gram Lorentzian reading of `mass-theory/markov-gram-bilinear-vs-star.md:34-48`).
  4. **Lean 4 generic-field bridge (`QOU/InformationTheory/FiniteRieffelQuantumMetric.lean`, ~55 lines added, zero `ℝ`, zero `sorry`):** Prove two theorems over `[Field K] [LinearOrder K] [IsStrictOrderedRing K]` directly connecting indiscernibility (`traceRadical`) to metric separation (`IsDualBound`):
     - `isDualBound_zero_iff_eq`: $d_L(\varphi,\psi) = 0 \iff \varphi = \psi$ (`IsDualBound L φ ψ 0 ↔ φ = ψ`) — strict metric Identity of Indiscernibles on unital states via scalar homogeneity $b = L(x)^{-1} \cdot x$;
     - `finite_dualBound_vanishes_on_traceRadical`: if $L$ vanishes on `traceRadical tr` (`∀ r ∈ traceRadical tr, L.toFun r = 0`), any two states $\varphi, \psi$ at finite Connes–Rieffel distance (`∃ M, IsDualBound L φ ψ M`) agree identically on `traceRadical tr`, so finite-distance state Equivalence classes factor injectively through the trace-radical quotient $A / \mathrm{rad}\,\mathrm{tr}$ (applicable directly to $H_n(q) \twoheadrightarrow TL_n(q)$).
- **What it costs:**
  - `4` prose/remark blocks touched or created (`introduction/intro.{md,ts}`, new `quantum-observable-universes/rieffel-metric-quotient-faithfulness.{md,ts}` + `quantum-observable-universes.ts:285`, `gravity-spacetime/lqg-adm-ashtekar-comparison.{md,ts}`, `gravity-spacetime/cr-structure-lorentzian-lift.{md,ts}`).
  - `1` Lean library file extended (`folio/quantum-observable-universe/lean/QOU/InformationTheory/FiniteRieffelQuantumMetric.lean`, ~55 lines) + `lean-direct-cone.sh -j 1` (~2 min).
  - `3` new CSL-JSON reference files (`earman1989.json`, `barbour-bertotti1982.json`, `rovelli1996.json`) + `folio/schema/references.ts` + `references.bib`.
  - Validation runs (~15–20 min at `-j 1` / `nice -n 15`): `lean-direct-cone.sh`, `lean-axiom-guard.py`, `lean-self-assuming-audit.py`, `run-validate.ts`, `run-validate-references.ts`, `paper-commentary-audit.ts`, and `qa-sweep` across the 4 blocks (scoring 16/16 on `expo-milnor-clarity`). Zero Python probe re-runs.
- **What it risks:**
  - *Sibling-branch merge coordination:* Active branch `claude/prior-art-doi-verified-pkg-20261123` (`63446514c77`, bean `qou-cvu9`) edits `categorical-dirac-operator-intro.md`, `lewandowski-nurowski-tafel1990.json`, `nurowski-trautman2002.json`, `folio/schema/references.ts`, and `references.bib`. Stacking Option 3 after `qou-cvu9` merges avoids all rebase friction; running before `qou-cvu9` merges creates trivial additive conflicts in `references.ts` / `references.bib`.
  - *Detangler discipline (`qou-d4kh`):* Ch. 2 (`quantum-observable-universes/`) precedes Ch. 11 (`mass-theory/`) and Ch. 20 (`information-theory/`), so the new Ch. 2 remark **must not** contain markdown `#prop:gram-degeneracy-blocks-connes` or `#rem:spacetime-length-distance-layers` forward links; Ch. 11 and Ch. 13 instead link *backward* to Ch. 2.
  - *Vacuity-audit discipline:* Both new Lean theorems have concrete algebraic conclusions (`φ = ψ` and `∀ r ∈ traceRadical tr, φ r = ψ r`) with zero typeclass-bundled hypotheses, so `lean-self-assuming-audit.py` passes cleanly.
- **What it commits to:** Treating relationalism as an explicit, formally witnessed three-step mathematical spine (trace-radical quotient $\to$ Rieffel state-space metric $\to$ contact CR ray geometry with Reeb causal ordering and an explicit 4D Lorentzian gap), rather than an isolated historical paragraph in Chapter 0.
- **Preview (Lean 4 bridge theorem signatures in `QOU/InformationTheory/FiniteRieffelQuantumMetric.lean` + Ch. 2/Ch. 13 spine):**
  ```lean
  /-- **Metric Identity of Indiscernibles (`d_L(φ, ψ) = 0 ↔ φ = ψ`):**
  Zero Connes–Rieffel dual bound equates unital states on `A` over any
  strictly ordered field `K` (zero `ℝ`). -/
  theorem isDualBound_zero_iff_eq (L : LipSeminorm K A)
      (φ ψ : UnitalState K A) :
      IsDualBound L φ ψ 0 ↔ φ = ψ

  /-- **Trace-Radical Descent of Finite-Distance States:**
  Whenever `L` vanishes on `traceRadical tr` (as for any GNS-represented
  seminorm on `H_n(q)`), any state pair admitting a finite Connes–Rieffel
  bound agrees identically on `traceRadical tr` and therefore descends
  uniquely to the faithful quotient `A / rad(tr)`. -/
  theorem finite_dualBound_eq_on_traceRadical (L : LipSeminorm K A)
      (tr : A → K) (hrad : ∀ r ∈ traceRadical tr, L.toFun r = 0)
      (φ ψ : UnitalState K A) (hbdd : ∃ M : K, IsDualBound L φ ψ M) :
      ∀ r ∈ traceRadical tr, φ.toLinear r = ψ.toLinear r
  ```
  ```
  Ch. 0 (sec:introduction-overview)
    └─ Leibniz successions (∘) & coexistences (⊗, σ); GNS null ideal = operational PII
         │
         ▼
  Ch. 2 (rem:dirac-rieffel-quotient-metric, sec:categorical-dirac-operator)
    └─ D_∇ Lip-seminorm L(a); ker L = K·1_A criterion [rieffel1999];
       lean.ref → FiniteRieffelQuantumMetric.isDualBound_zero_iff_eq
         │
         ▼
  Ch. 11 (prop:gram-degeneracy-blocks-connes, already on main) & Ch. 20 (rem:spacetime-length-distance-layers)
    └─ Convention-D H_n(q) has det G = 0 for n ≥ 3 ⇒ forces quotient TL_n(q) = H_n(q)/rad
         │
         ▼
  Ch. 13 (rem:lqg-adm-ashtekar-comparison & prose:cr-structure-lorentzian-lift)
    └─ Contrasts Barbour–Bertotti E(3) shape space & Rovelli RQM; Reeb flow φ_t = exp(tξ)
       supplies causal ordering on twisting 3D CR ray space; 4D Lorentzian metric lift OPEN
  ```

---

#### Option 4 — Trim / Relocate Out of Ch. 0 Intro into Information-Theory Remark

- **What it means:** Restore Chapter 0's Overview (`folio/quantum-observable-universe/introduction/intro.{md,ts}`) to its strictly mathematical/observational pre-`#9207` flow by excising lines `90-106` (and removing `"leibniz-clarke1717"`, `"gelfand-naimark1943"`, `"segal1947"` from `intro.ts`), and relocate the entire Leibniz relationalism discussion — enriched with the Earman (`earman1989`), Barbour–Bertotti (`barbour-bertotti1982`, DOI `10.1098/rspa.1982.0102`), and Rovelli (`rovelli1996`, DOI `10.1007/BF02302261`) contrasts plus explicit non-claims — into a dedicated self-contained `remark` block `rem:leibniz-relational-indiscernibility` (`information-theory/leibniz-relational-indiscernibility.{md,ts}`) placed immediately after `rem:spacetime-length-distance-layers` in `information-theory/information-theory.ts:102` (with `lean.ref` wired to `QOU.InformationTheory.FiniteRieffelQuantumMetric.hasScalarKernel_of_state_bounded`).
- **What it costs:**
  - `2` files edited in Ch. 0 (`introduction/intro.md` deleting lines `90-106`; `introduction/intro.ts` trimming `cites[]`).
  - `2` new block files + `1` manifest line in Ch. 20 (`information-theory/leibniz-relational-indiscernibility.{md,ts}`, `information-theory/information-theory.ts:103`).
  - `3` new CSL-JSON reference files (`earman1989.json`, `barbour-bertotti1982.json`, `rovelli1996.json`) + `folio/schema/references.ts` + `references.bib`.
  - Validation runs (~10 min at `-j 1` / `nice -n 15`): `run-validate.ts`, `run-validate-references.ts`, `paper-commentary-audit.ts`, `qa-sweep` on `intro` and `leibniz-relational-indiscernibility`. Zero Lean rebuilds and zero probe runs.
- **What it risks:**
  - A reader who reads only the Introduction (`chap:introduction`) and Part I (`chap:qu`, `chap:qou`) will not encounter the relational-space motivation or the Barbour–Bertotti / Rovelli positioning until Part IV (`chap:info-theory`, Chapter 20).
  - Conversely, it **eliminates 100%** of the Chapter 0 over-claim and forward-notation risks identified in Option 1, because by Chapter 20 the reader has already met $H_n(q)$, $TL_n(q)$, $\mathcal{D}_\nabla$, `prop:gram-degeneracy-blocks-connes`, and `prose:cr-structure-lorentzian-lift`, so every link in `rem:leibniz-relational-indiscernibility` is a clean backward reference!
- **What it commits to:** Keeping the Chapter 0 opener austere and free of philosophical history beyond the existing one-sentence Heisenberg, Wigner, Einstein, and Noether anchors (`intro.md:37-56, 118-128`), housing relational-spacetime philosophy in Part IV (`Information-Theoretic Perspectives`) alongside `rem:spacetime-length-distance-layers` and `FiniteRieffelQuantumMetric`.
- **Preview (file-diff summary for Option 4):**
  ```diff
  --- a/folio/quantum-observable-universe/introduction/intro.md
  +++ b/folio/quantum-observable-universe/introduction/intro.md
  @@ -87,23 +87,6 @@
   thesis is that the observations *determine* the ingredients; nothing
   else is added by hand.
   
  -This relational starting point fulfills the programme Gottfried Wilhelm
  -Leibniz set out in his 1715--1716 correspondence with Samuel Clarke
  -... [17 lines relocated to information-theory/leibniz-relational-indiscernibility.md] ...
  -and recovers differential, contact, and metric geometry downstream.
  -
   The categorical language then recovers, as internal pieces of the
   structure, the concepts that describe a universe's mechanics.

  +++ b/folio/quantum-observable-universe/information-theory/leibniz-relational-indiscernibility.ts
  +export default remark({
  +  label: "rem:leibniz-relational-indiscernibility",
  +  title: "Algebraic relationalism, indiscernibility quotients, and finite state metrics",
  +  interprets: "prop:reeb-coefficient-is-hbar-q",
  +  lean: {
  +    ref: "qou:QOU.InformationTheory.FiniteRieffelQuantumMetric.hasScalarKernel_of_state_bounded",
  +    validation: "not_checked",
  +  },
  +  uses: [
  +    "rem:spacetime-length-distance-layers",
  +    "prop:gram-degeneracy-blocks-connes",
  +    "rem:hecke-radical-is-temperley-lieb",
  +  ],
  +  cites: [
  +    "leibniz-clarke1717", "earman1989", "barbour-bertotti1982", "rovelli1996",
  +    "gelfand-naimark1943", "segal1947", "rieffel1999",
  +  ],
  +});
  ```

---

### 0.2 Structured `AskUserQuestion` Tool Payload (Ready for Foreground Coordinator)

```json
{
  "questions": [
    {
      "header": "Leibniz arc",
      "question": "🟡 Waiting on user — How should Leibniz relationalism sit across Ch. 0, Ch. 2, Ch. 13, and Information Theory? (Pick all that apply; add 'Other' with a note if needed.)",
      "multiSelect": true,
      "options": [
        {
          "label": "1. Keep #9207 status quo (Ch. 0 PII only)",
          "description": "Zero edits; keep intro.md:90-106 as landed on main. Leaves H_n/TL_n forward jump and Lorentzian/isomorphism scope caveats unstated in Ch. 0."
        },
        {
          "label": "2. Tighten Ch. 0 + prior-art contrasts only",
          "description": "Edit intro.{md,ts} only (+3 bib keys: Earman 1989, Barbour-Bertotti 1982, Rovelli 1996); smooth forward jargon and state 4D Lorentzian non-claim."
        },
        {
          "label": "3. Cross-chapter spine + Lean bridge (Recommended)",
          "description": "Thread Ch. 0 PII -> Ch. 2 D_nabla Rieffel remark -> Ch. 13 CR/LQG contrast + prove d_L(rho1,rho2)=0 <-> rho1=rho2 & radical descent in Lean."
        },
        {
          "label": "4. Relocate out of Ch. 0 to Info Theory",
          "description": "Remove intro.md:90-106 for an austere Ch. 0; place full Leibniz/Barbour-Bertotti/Rovelli/Rieffel remark beside rem:spacetime-length-distance-layers."
        }
      ]
    }
  ]
}
```

---

## 1. Corpus Audit: What PR `#9207` Already Landed & Exact State on `origin/main`

PR `#9207` landed on `origin/main` as three commits (`62cc0b24599..5a350c1a535`):
1. `b67c7efb137` — `bib,intro,mass-theory: Leibniz relational space and trace-radical/Connes prior art (qou-u58f)`
2. `a62506a5c91` — `info-theory,lean,probes: 3-layer scale consolidation (§7c) and finite Rieffel TL_3 metric (qou-adwi, qou-5uj7)`
3. `5a350c1a535` — `witness,bib: stamp scriptCommitSha on finite-rieffel-tl3-metric witness post-rebase`

Below is the exact file-by-file, line-by-line state across all five monograph surfaces on `origin/main` (`e7ceba55f05`).

### 1.1 Chapter 0 — Introduction (`folio/quantum-observable-universe/introduction/`)

| File & lines (`origin/main`) | Block label | What `#9207` landed | Critical-distance / Milnor assessment |
|---|---|---|---|
| `introduction/intro.md:90-106` & `intro.ts:9-11` | `sec:introduction-overview` | Added 17-line paragraph citing `leibniz-clarke1717`, `gelfand-naimark1943`, `segal1947`. Maps $\circ \leftrightarrow$ successions, $(\otimes,\sigma) \leftrightarrow$ coexistences, and $H_n(q)/\mathrm{rad} \cong TL_n(q) \leftrightarrow$ GNS operational indiscernibility; concludes QOU *"fulfills"* Leibniz's programme and *"recovers differential, contact, and metric geometry downstream."* | **Three defects identified:**<br>1. **Unqualified algebra isomorphism (`intro.md:100`):** Writes $H_n(q)/\mathrm{rad} \cong TL_n(q)$ as established, whereas `mass-theory/hecke-radical-is-temperley-lieb.md:93-97` states explicitly: *"No proof of $H_n(q)/\mathrm{rad} \cong TL_n(q)$ is given, and nothing above supplies one."*<br>2. **Unqualified metric/spacetime recovery (`intro.md:90, 105-106`):** Saying QOU *"fulfills"* Leibniz's programme and *"recovers... metric geometry"* risks misreading the finite-dimensional state-space transport metric $d_L$ on $TL_n(q_0)$ as a 4D Lorentzian spacetime metric, which `gravity-spacetime/cr-structure-lorentzian-lift.md:13` explicitly says is **not** constructed.<br>3. **Unglossed forward symbols (Milnor H4/H5, `intro.md:98-100`):** Mentions Iwahori–Hecke $H_n(q)$ and Temperley–Lieb $TL_n(q)$ two subsections before braids and $H_n(q)$ are introduced in `sec:introduction-state-space-knots` (`intro-particles-as-knots.md`). |
| `introduction/intro-model-and-measurement.md:33-35` | `sec:introduction-mathematics-measurement` | Added 3-line pointer to `[stratified spacetime, length, and distance scales](#rem:spacetime-length-distance-layers)` separating dimensionless $\mathbb{Q}(q)$ clock grains and state-space moduli from Compton and SI Planck unit bridges. | **Clean.** Matches `AGENTS.md` mathematical-model-by-default discipline and CAL-1/2/3 boundary. |
| `introduction/introduction.ts:1-73` | `chap:introduction` | Untouched by `#9207` (avoided conflict with `#9194`). | Five subsections under `sec:introduction-overview` + `sec:chapter-overview`. |

### 1.2 Chapter 20 — Information Theory & Lean (`information-theory/` & `lean/QOU/InformationTheory/`)

| File & lines (`origin/main`) | Block / module | Exact mathematical content on `origin/main` | Audit note |
|---|---|---|---|
| `information-theory/spacetime-length-distance-layers.md:1-33` & `.ts:1-53` | `rem:spacetime-length-distance-layers` | Stratifies all 7 step, clock, distance, volume, and length notions into Layer I (Tier 1 generic field $k$, $q \in k^\times\setminus\{1\}$: $\hbar_q = 1-q^{-1}$, $t_P(q) = \hbar_q^{-1}$, $\hbar_q t_P(q) = 1$, Thomae–Jackson UV partial sum $< t_P(q)$), Layer IIa (Tier 2 ordered field: Connes–Kantorovich–Rubinstein metric $d_L(\varphi,\psi)$ on faithful $TL_n(q) = H_n(q)/\mathrm{rad}$), Layer IIb ($\mathrm{Vol}(S^3\setminus K)$), and Layer IIIa/b (empirical Compton $\lambda_{C,e}$ and SI Planck $\ell_{\mathrm{Planck}}^{\mathrm{SI}}$). Cites `kantorovich1942`, `rubinstein1957`, `connes1989`, `rieffel1999`, `rieffel2004`, `dandrea-martinetti2010`. | **Unwired Lean module note:** `spacetime-length-distance-layers.ts:9` sets `lean.ref` to `UnifiedClockScaleLayers.hbarQ_mul_planckTick`; `FiniteRieffelQuantumMetric.lean` is mentioned only in `authorNotes` (`.ts:48`), so **zero content blocks on `origin/main` currently carry `lean.ref` pointing to `FiniteRieffelQuantumMetric`**. Options 3 and 4 wire it directly. |
| `information-theory/connes-distance-not-reeb-step-count.md:1-40` | `rem:connes-distance-not-reeb-step-count` | Records two independent qualifications on $d_{\mathrm{Connes}}$ built from $\mathcal{D}_\nabla = q^{-1}\nabla + (1-q^{-1})\iota_\xi\nabla$: (1) at $q_0$, $q_0^{-1} \approx 90.09\%$ weights horizontal gradient transport and $\hbar_{q_0} \approx 9.91\%$ weights Reeb transport (anisotropy $c_{q_0} = 1/(q_0-1) \approx 9.093$), so $d_{\mathrm{Connes}}$ is **not** a pure Reeb step count except as $q \to \infty$; (2) under Convention D, Gram degeneracy blocks finiteness until $\mathrm{rad}\,\tau_q$ is quotiented out. | **Essential constraint for Option 3:** Any Ch. 2 or Ch. 13 text must describe $d_L$ accurately as an *anisotropic horizontal–contact transport metric*, never as a pure Reeb step counter. |
| `lean/QOU/InformationTheory/UnifiedClockScaleLayers.lean:1-108` | `QOU.InformationTheory.UnifiedClockScaleLayers` | Sorry-free generic-field (`[Field K]`) and ordered-field proofs of `hbarQ_mul_planckTick`, `planckTick_eq_div`, `jackson_uv_geom_sum`, `jackson_uv_sum_lt_planckTick`, and `atomic_clock_scales_with_planckTick`. | Clean §7c compliance (zero `ℝ`). |
| `lean/QOU/InformationTheory/FiniteRieffelQuantumMetric.lean:1-264` | `QOU.InformationTheory.FiniteRieffelQuantumMetric` | Sorry-free `[Field K] [LinearOrder K] [IsStrictOrderedRing K]` formalization (zero `ℝ`) of `LipSeminorm`, `UnitalState`, `IsDualBound` (`isDualBound_self`, `isDualBound_symm`, `isDualBound_triangle`), `HasScalarKernel`, `unbounded_of_nonscalar_kernel`, `hasScalarKernel_of_state_bounded`, finite-graph Kantorovich–Rubinstein duality (`kr_lip_le_pathCost`, `kr_shortest_path_attained`, `kantorovich_primal_ge_dual`), and `dirac_convex_weights`. | **Gap closed by Option 3's Lean bridge:** Currently proves $\text{finite bound} \implies \ker L = K\cdot 1_A$, but does **not** yet state `IsDualBound L φ ψ 0 ↔ φ = ψ` (metric Identity of Indiscernibles) or connect `LipSeminorm` to `TemperleyLiebTower.traceRadical`. |
| `computations/probes/finite_rieffel_tl3_metric_probe.py:1-532` & `finite-rieffel-tl3-metric.witness.json` | 80-dps `mpmath` probe (`6/6` assertions passing) | Evaluates the 6D $H_3(q_0)$ Convention-D star-Gram null vector $r_{[1^3]} = (1, -q_0^{-1}, -q_0^{-1}, q_0^{-2}, q_0^{-2}, -q_0^{-3})$ ($\|S\cdot r_{[1^3]}\|_\infty = 0$ at 80 dps while $\chi_{(1^3)}(r_{[1^3]}) > 0$), constructs the positive-definite 5D planar $TL_3(q_0)$ star-Gram matrix, and computes the exact $5\times 5$ Rieffel–Kantorovich state-space metric with duality gap $< 10^{-76}$. | Zero float64; proton anchor `q_at(80)`. Untouched under all 4 options. |

### 1.3 Chapter 11 — Mass Analysis (`folio/quantum-observable-universe/mass-theory/` & `lean/QOU/QBeta/`)

| File & lines (`origin/main`) | Block / module | Exact mathematical content on `origin/main` | Audit note |
|---|---|---|---|
| `mass-theory/hecke-radical-is-temperley-lieb.md:1-131` & `.ts:1-52` | `rem:hecke-radical-is-temperley-lieb` | `#9207` (`b67c7efb137`) added `## Lineage of the trace-radical quotient` (`lines 39-57`) crediting Temperley–Lieb 1971, Jones 1987, Wenzl 1988, Orellana 1998, Geck–Lambropoulou 2004, BHMV 1995, Turaev 2010, Barrett–Westbury 1993, and Jimbo 1986, contrasting root-of-unity skein semisimplification ($q = e^{i\pi/r}$) against QOU's real $q > 1$ two-row rank cap. Lines `93-100` explicitly record that the algebra isomorphism $H_n(q)/\mathrm{rad} \cong TL_n(q)$ is **not** proved in this paper. | Already complete and exemplary; Ch. 0 (`intro.md:100`) should respect lines `93-100` by not over-claiming the isomorphism as proved in-house. |
| `mass-theory/gram-degeneracy-blocks-connes.md:1-91` & `.ts:1-45` | `prop:gram-degeneracy-blocks-connes` | `#9207` (`b67c7efb137`) added `## Prior art and structural synthesis` (`lines 44-83`) crediting Kantorovich 1942, Rubinstein 1957, Connes 1989/1994, Rieffel 1999/2004, Latrémolière 2016, Iochum–Krajewski–Martinetti 2001, D'Andrea–Martinetti 2010, Gelfand–Naimark 1943, Segal 1947, Haag–Kastler 1964, Henneaux–Teitelboim 1992, and Chamseddine–Connes 1997 (contrasting stipulated semisimple $\mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})$ against dynamically forced $H_n(q) \twoheadrightarrow TL_n(q)$). | Does **not** cite `leibniz-clarke1717` (`intro.ts` is the sole consumer of `leibniz-clarke1717` on `origin/main`). |
| `mass-theory/markov-gram-bilinear-vs-star.md:34-48` | `rem:markov-gram-bilinear-vs-star` | Explicitly **withdraws** the earlier claim that the $(4,1,1)$ signature of the untwisted bilinear pairing $\mathrm{tr}_M(ab)$ defines a physical Lorentzian causal structure; metrics use the Hecke $\ast$-involution $T_w^\ast = T_{w^{-1}}$, giving positive-semidefinite $\mathrm{tr}_M(ab^\ast)$ of signature $(5,0,1)$ on $H_3$ and $(5,0,0)$ on $TL_3$. | **Hard guardrail for Option 3:** Causal structure in QOU enters via the Reeb flow $\xi$ / braiding order $\prec_c$ and contact CR ray geometry (`chap:gravity-spacetime-emergence`), **never** via the withdrawn bilinear Markov–Gram signature. |
| `lean/QOU/QBeta/TemperleyLiebTower.lean:738-785` | `traceRadical`, `traceRadical_two_sided`, `traceRadical_star_eq` | Proves over a generic `[Ring A]` with `[Zero R]` that `traceRadical tr = {a | ∀ b, tr (a * b) = 0}` is a two-sided ideal whenever `tr` is cyclic, and coincides with the star radical `{a | ∀ b, tr (a * star b) = 0}` whenever `star` is surjective. | Ready to import or mirror cleanly in Option 3's `FiniteRieffelQuantumMetric` descent theorem. |

### 1.4 Chapter 2 — Quantum Observable Universes (`folio/quantum-observable-universe/quantum-observable-universes/`, `chap:qou`)

| File & lines (`origin/main`) | Block label | Current content on `origin/main` | Relevance to Options 2–3 |
|---|---|---|---|
| `qou-axioms-physical-reading.md:7-9` | `rem:qou-axioms-physical-reading` | Explains **Non-degenerate integration** (*"An element pairing to zero against everything would sit in the algebra yet be invisible to every integral, beyond the reach of any experiment"*) and **Observability** ($\mathrm{Hom}_{\mathbf{C}}(\mathbf{1},\mathrm{Ad}(A)) = 0$). | Already expresses operational indiscernibility at the axiom level without naming Leibniz or Rieffel. |
| `braiding-induced-ordering-interpretation.md:1-8` | `rem:braiding-induced-ordering-interpretation` | Pairs the **categorical arrow of time** ($c_{V,V}$, Gröbner–Shirshov reduction $\prec_c$) with the **geometric arrow of time** (Reeb vector field $\xi$). | Concrete realization of Leibniz's "order of successions" inside Ch. 2. |
| `categorical-dirac-operator.md:1-10` & `wavefront-propagation.md:1-8` | `def:categorical-dirac-operator`, `rem:wavefront-propagation` | Defines $\mathcal{D}_\nabla = q^{-1}\nabla + (1-q^{-1})\iota_\xi\nabla \colon A \to \Omega^1(A)$ (`sec:categorical-dirac-operator`, manifest lines `277-286`). Zero mention of Connes/Rieffel Lipschitz seminorms or quotient faithfulness in Ch. 2. | Exact insertion point for **Option 3 Stop 2** (`rem:dirac-rieffel-quotient-metric` after line `285` of `quantum-observable-universes.ts`), obeying strict reading order (`qou-d4kh`) with zero forward references. |

### 1.5 Chapter 13 — Gravity and Spacetime Emergence (`folio/quantum-observable-universe/gravity-spacetime/`, `chap:gravity-spacetime-emergence`)

| File & lines (`origin/main`) | Block label | Current content on `origin/main` | Relevance to Options 2–3 |
|---|---|---|---|
| `lqg-adm-ashtekar-comparison.md:8, 19, 33` | `rem:lqg-adm-ashtekar-comparison` | Maps ADM 3+1 foliation to contact distribution $H = \ker\varTheta_A$ + Reeb flow $\phi_t = \exp(t\xi)$ (`line 8`), lists `Relational QM \| Adelic product formula` **with zero citation** (`line 19`), and notes *"No 'problem of time'"* (`line 33`) because time emerges from $\phi_t = \exp(t\xi)$ rather than an external ADM coordinate. Zero mention of Barbour–Bertotti. | **Option 3 Stop 3** cites `rovelli1996` and `barbour-bertotti1982` here and clarifies how QOU's shared fibre-functor observability differs from Rovelli's observer-relative states. |
| `sym2-adjoint-spin-two-gauge-not-lorentz.md:1-12` | `rem:sym2-adjoint-spin-two-gauge-not-lorentz` | States explicitly that $\mathrm{Sym}^2(V_1)\ominus V_0 \cong V_2$ is spin-$2$ of the internal gauge group $\mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$, **not** helicity $\pm 2$ of Poincaré / $\mathrm{SO}(3,1)$, and claims no graviton or field equation. | Reinforces the non-claim boundary required in Options 2, 3, and 4. |
| `cr-structure-lorentzian-lift.md:1-17` & `.ts:1-15` | `prose:cr-structure-lorentzian-lift` | Cites `nurowski-trautman2002` and `lewandowski-nurowski-tafel1990`: twisting 3D contact CR manifolds arise as spaces of shear-free null geodesics of 4D Robinson/Lorentzian spacetimes, **but** *"No such lift is constructed here. In particular the $q$-exterior derivative does not select a deformed CR structure"* (`QExteriorCR.dq_cr_iff`). | **Option 3 Stop 3** threads the relational causal summary directly into this block while preserving the explicit non-construction statement verbatim. |

---

## 2. Live-DOI-Verified Prior-Art Ledger & Structural Comparison Matrix

### 2.1 🚨 Bibliographic & DOI Verification Alert (`barbour-bertotti1982`)

Live verification against the Crossref API (`api.crossref.org/works/...`) and the `doi.org` Handle System API (`doi.org/api/handles/...`, `responseCode == 1`) caught a **wrong DOI** circulating in external/task notes:
- ❌ **WRONG DOI `10.1098/rspa.1982.0094`:** Resolves to **C. W. Nutt (1982)**, *"The physical basis of the displacement of oil from porous media by other fluids: a capillary bundle model"*, *Proc. R. Soc. Lond. A* **382**(1782), 155–178!
- ✅ **TRUE LIVE-VERIFIED DOI `10.1098/rspa.1982.0102` (`responseCode == 1`):** Resolves to **Julian B. Barbour and Bruno Bertotti (1982)**, *"Mach's principle and the structure of dynamical theories"*, *Proceedings of the Royal Society of London. Series A, Mathematical and Physical Sciences* **382**(1783), 295–306!

Every downstream PR implementing Option 2, 3, or 4 **must** use `10.1098/rspa.1982.0102`.

### 2.2 Complete Verified Bibliography Table for Relationalism & Quantum Metric Emergence

| Key (`folio/references/`) | Status on `origin/main` | Verified authors (full names for $\le 5$ authors), title, venue, year | Live-verified identifier (`doi.org` / ISBN / URL) |
|---|---|---|---|
| `leibniz-clarke1717` | Present (`#9207`) | Gottfried Wilhelm Leibniz and Samuel Clarke, *A Collection of Papers, Which passed between the Late Learned Mr. Leibnitz, and Dr. Clarke, In the Years 1715 and 1716*, James Knapton, London (1717), Third Letter §4 & Fourth Letter §§3–6 | Pre-DOI primary print; `https://archive.org/details/collectionofpape00leibuoft` |
| `earman1989` | **Add in Opt. 2/3/4** | John Earman, *World Enough and Space-Time: Absolute versus Relational Theories of Space and Time*, MIT Press (Bradford Book), Cambridge, MA (1989), xiv + 233 pp. | ISBN `978-0-262-05040-1` (hc) / `978-0-262-55021-5` (pbk) |
| `barbour-bertotti1982` | **Add in Opt. 2/3/4** | Julian B. Barbour and Bruno Bertotti, "Mach's principle and the structure of dynamical theories", *Proc. R. Soc. Lond. A* **382**(1783), 295–306 (1982) | DOI `10.1098/rspa.1982.0102` (`responseCode = 1`) |
| `rovelli1996` | **Add in Opt. 2/3/4** | Carlo Rovelli, "Relational quantum mechanics", *Int. J. Theor. Phys.* **35**(8), 1637–1678 (1996) | DOI `10.1007/BF02302261` (`responseCode = 1`); `arXiv:quant-ph/9609002` |
| `gelfand-naimark1943` | Present (`#9207`) | Israel M. Gelfand and Mark A. Naimark, "On the imbedding of normed rings into the ring of operators in Hilbert space", *Mat. Sb. (N.S.)* **12(54)**(2), 197–217 (1943) | `http://mi.mathnet.ru/msb6155` |
| `segal1947` | Present (`#9207`) | Irving E. Segal, "Irreducible representations of operator algebras", *Bull. Amer. Math. Soc.* **53**(2), 73–88 (1947) | DOI `10.1090/S0002-9904-1947-08742-5` |
| `haag-kastler1964` | Present (`#9207`) | Rudolf Haag and Daniel Kastler, "An algebraic approach to quantum field theory", *J. Math. Phys.* **5**(7), 848–861 (1964) | DOI `10.1063/1.1704187` |
| `henneaux-teitelboim1992` | Present (`#9207`) | Marc Henneaux and Claudio Teitelboim, *Quantization of Gauge Systems*, Princeton University Press (1992) | ISBN `978-0-691-03769-1` |
| `kantorovich1942` | Present (`#9207`) | Leonid V. Kantorovich, "On the translocation of masses", *Dokl. Akad. Nauk SSSR* **37**(7–8), 227–229 (1942) | Pre-DOI Soviet journal |
| `rubinstein1957` | Present (`#9207`) | Leonid V. Kantorovich and Gennady Sh. Rubinstein, "On a functional space and certain extremum problems", *Dokl. Akad. Nauk SSSR* **115**(6), 1058–1061 (1957) | Pre-DOI Soviet journal |
| `connes1989` | Present (`#9207`) | Alain Connes, "Compact metric spaces, Fredholm modules, and hyperfiniteness", *Ergodic Theory Dynam. Systems* **9**(2), 207–220 (1989) | DOI `10.1017/S0143385700004934` (`responseCode = 1`) |
| `connes1994` | Present (`main`) | Alain Connes, *Noncommutative Geometry*, Academic Press, San Diego (1994) | ISBN `978-0-12-185860-5` |
| `rieffel1999` | Present (`#9207`) | Marc A. Rieffel, "Metrics on state spaces", *Doc. Math.* **4**, 559–600 (1999) | `https://arxiv.org/abs/math/9906151` (*Doc. Math.* vol. 4 predates Crossref DOIs) |
| `rieffel2004` | Present (`#9207`) | Marc A. Rieffel, *Gromov–Hausdorff distance for quantum metric spaces*, *Mem. Amer. Math. Soc.* **168**(796) (2004) | DOI `10.1090/memo/0796` (`responseCode = 1`) |
| `latremoliere2016` | Present (`#9207`) | Frédéric Latrémolière, "The quantum Gromov–Hausdorff propinquity", *Trans. Amer. Math. Soc.* **368**(1), 365–411 (2016) | DOI `10.1090/tran/6334` (`responseCode = 1`) |
| `iochum-krajewski-martinetti2001` | Present (`#9207`) | Bruno Iochum, Thomas Krajewski, and Pierre Martinetti, "Distances in finite spaces from noncommutative geometry", *J. Geom. Phys.* **37**(1–2), 100–125 (2001) | DOI `10.1016/S0393-0440(00)00044-9` (`responseCode = 1`) |
| `dandrea-martinetti2010` | Present (`#9207`) | Francesco D'Andrea and Pierre Martinetti, "A view on optimal transport from noncommutative geometry", *SIGMA* **6**, 057 (2010) | DOI `10.3842/SIGMA.2010.057` (`responseCode = 1`) |
| `lewandowski-nurowski-tafel1990` | Present (`main`; DOI enriched on `qou-cvu9`) | Jerzy Lewandowski, Paweł Nurowski, and Jacek Tafel, "Einstein's equations and realizability of CR manifolds", *Class. Quantum Grav.* **7**(11), L241–L246 (1990) | DOI `10.1088/0264-9381/7/11/003` (`responseCode = 1`) |
| `nurowski-trautman2002` | Present (`main`; DOI enriched on `qou-cvu9`) | Paweł Nurowski and Andrzej Trautman, "Robinson manifolds as the Lorentzian analogs of Hermite manifolds", *Differential Geom. Appl.* **17**(2–3), 175–195 (2002) | DOI `10.1016/S0926-2245(02)00106-7` (`responseCode = 1`) |

### 2.3 Five-Way Mathematical-Physics Comparison Matrix

| Programme | Primitive arena assumed at the outset | How indiscernibles / redundancies are removed | How metric / causal structure enters | Key contrast with QOU |
|---|---|---|---|---|
| **Newton–Clarke substantivalism** (`leibniz-clarke1717`, `earman1989`) | Absolute Euclidean space $\mathbb{E}^3$ and universal time $\mathbb{R}$ prior to matter | None — global translations/boosts of all matter yield distinct states in Clarke's defense | Stipulated Euclidean metric $\delta_{ij}$ and absolute simultaneity | Violates Leibniz PII; QOU assumes no ambient manifold $\mathbb{E}^3$ or $\mathbb{R}^{1,3}$. |
| **Barbour–Bertotti Machian / shape dynamics** (`barbour-bertotti1982`, `10.1098/rspa.1982.0102`) | Classical $N$-particle configuration space $\mathbb{R}^{3N}$ | Quotient $\mathcal{Q}_{\mathrm{rel}} = \mathbb{R}^{3N}/\mathrm{E}(3)$ (or $\mathrm{Sim}(3)$) via variational "best matching" along trial curves | Jacobi arc-length metric on relative configuration space; York extrinsic-curvature time in ADM shape dynamics | Still presupposes continuous $\mathbb{R}^3$ particle positions and classical configuration-space group quotients; QOU quotients a **noncommutative process algebra** by a **trace radical** $\mathrm{rad}\,\tau_q$ with zero background coordinates. |
| **Rovelli relational quantum mechanics** (`rovelli1996`, `10.1007/BF02302261`) | Standard quantum systems $(S, O)$ with Hilbert-space operator algebras | Rejects universal state $|\Psi\rangle$; states $|\psi\rangle_{S|O}$ are indexed by observer–system pairs | Leaves background spacetime metric, causal cone, and particle mass spectrum external to RQM | QOU enforces **inter-observer consistency** via a shared braided category and faithful fibre functor $\tau$ (`def:quantum-observable-universe`), internalizes observation as an open braid morphism (`chap:measurement-observation`), and derives finite state-space transport metrics internally. |
| **Chamseddine–Connes spectral Standard Model** (`connes1994`, `chamseddine-connes-1997`) | Product geometry $C^\infty(M) \otimes \mathcal{A}_F$ over a **4D spin manifold $M$** plus stipulated finite semisimple $\mathcal{A}_F = \mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})$ | $\mathcal{A}_F$ is chosen semisimple with a faithful Hilbert–Schmidt trace by hand | Connes spectral distance $d_D(\varphi,\psi) = \sup_{\| [D,a] \| \le 1}|\varphi(a)-\psi(a)|$ combining continuum $M$ and discrete $\mathcal{A}_F$ | Assumes continuum 4-manifold $M$ and finite algebra $\mathcal{A}_F$ up front; QOU starts on $H_n(q)$ at real $q_0 > 1$, proves Convention D forces $\det G = 0$ ($n \ge 3$), and uses Rieffel's kernel theorem (`rieffel1999`) so metric finiteness **forces** the projection $H_n(q) \twoheadrightarrow TL_n(q)$. |
| **Quantum Observable Universe (QOU)** (this monograph) | Rigid braided monoidal category $(\mathbf{C}, A, \tau)$ with Frobenius–Hopf trace $\int_A$ and substrate parameter $q$ | GNS / Markov trace null radical $\mathrm{rad}\,\tau_q = \{a : \tau_q(ab^\ast)=0\;\forall b\}$ kills $\ge 3$-row Young blocks at real $q > 1$ via $\mathrm{SU}_q(2)$ rank cap | **Metric:** Rieffel–Kantorovich distance $d_L$ from $\mathcal{D}_\nabla = q^{-1}\nabla + \hbar_q\iota_\xi\nabla$ on faithful quotients $TL_n(q_0)$.<br>**Time/causal order:** Braiding/GS order $\prec_c$ and Reeb flow $\phi_t = \exp(t\xi)$ on 3D twisting contact CR slices | **Honest open boundary (`cr-structure-lorentzian-lift.md:12-17`, `sym2-adjoint-spin-two-gauge-not-lorentz.md:3-12`):** No 4D Lorentzian Einstein metric lift from the 3D contact CR ray space, no $\mathrm{Aut}^{\otimes}(\tau) \to \mathrm{SO}(3,1)$ Lorentz homomorphism, and no in-paper algebra isomorphism proof $H_n(q)/\mathrm{rad} \cong TL_n(q)$ are yet established. |
