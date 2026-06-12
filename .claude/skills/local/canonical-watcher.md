---
name: canonical-watcher
roles: [reader, collaborator, owner]
user_invocable: true
inherits: local/integration-watcher
watch_arg: canonical
description: >
  Canonical-derivation-discipline integration watcher — watches
  origin/main + open active PRs + newly-opened PRs for
  non-canonical empirical/fitting/calibration inputs beyond the
  three categorically allowed (CAL-1 m_e, CAL-2 m_μ/m_e→q_0,
  CAL-3 Q_β), numerology, or justification/rationalization in
  place of derivation. Inherits shared mechanics (Monitor,
  subscriptions, queue, ledger, idle sweep, author-ask,
  watch-prepared-PRs, witness-drift recovery, billing-quick-fail
  flake, post-completion one-voice, sibling-PR comment protocol,
  backlog-found PR spin-up, handover docs) from
  `local/integration-watcher`.
allowed-tools: Read Edit Write Bash Grep Glob Agent Monitor Skill
---

# /canonical-watcher

A concrete instance of [`local/integration-watcher`](integration-watcher.md).
The parent encodes the shared mechanics; this file fills the
nine domain-specific slots A-I.

**Setup:** use `NAME=canonical-watcher` everywhere the parent's
§1 references `${NAME}`. Files at
`.beans/canonical-watcher-queue.json` and
`.beans/canonical-watcher-ledger.md`.

**Authoritative reference:** the three-calibration discipline is
fixed by:
- [`prop:three-calibration-inputs`](../../../content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md)
- [`prop:three-calibration-discipline`](../../../content/quantum-observable-universe/observations/three-calibration-discipline.md)

Read both before opening any author ask — the proposition's
"What is forbidden" section is the closed list of violations.

## Slot A — Goal statement

Every numerical observable $\mathcal{O}$ in the paper factors as
$\mathcal{O} = \hat{\mathcal{O}}(q_0) \cdot m_e^{\,a} \cdot Q_\beta^{\,c}$
with $\hat{\mathcal{O}}(q_0) \in \mathbb{Q}(q_0)$ — the canonical
discipline minimum per `prop:three-calibration-discipline` — and
the empirically-observed Laurent refinement
$\hat{\mathcal{O}}(q_0) \in \mathbb{Z}[q_0^{\pm 1/2}]$ per
`prop:three-calibration-inputs`, with $a, c \in \mathbb{Z}_{\geq 0}$.
Anything else is a discipline violation — either a hidden fourth
calibration, a numerology, or a fit dressed as a derivation.

### Sibling skill: `production-vs-exploratory-discipline`

When this watcher flags a CAL-4 candidate, the resolution path is
through
[`local/production-vs-exploratory-discipline`](production-vs-exploratory-discipline.md):
- 3-category classification (production / exploratory / numerology)
- 13-driver canonical menu for production coefficients
- Rule 14 (off-menu coefficients escalate to author)
- q-locality gate (mandatory pre-flight: slope < 10² ppm/q vs
  q_0 ± 0.05 substrate window)
- Pre-promotion 7-step checklist before any production adoption

This watcher catches violations post-hoc; the discipline skill
defines the rule it enforces.

### Three categorically allowed calibrations

| ID | Quantity | (Co)homology | Wedderburn block | What it fixes |
|----|----------|--------------|------------------|---------------|
| **CAL-1** | $m_e$ (CODATA) | $H^0$ | std (2,1) | leptonic mass scale |
| **CAL-2** | $m_\mu/m_e \approx 206.768$ (CODATA) | $H^1$ | alt (1³) | substrate $q_0$ |
| **CAL-3** | $Q_\beta(n) \approx 0.78233$ MeV (PDG) | $H^2$ | sym (3) | hadronic scale $\mathbf{E}_0$ |

These are **exhaustive**. A fourth dimensional input anywhere is
a hard audit failure.

## Slot B — §3 trigger filter

```bash
SHA=<event sha>
changed=$(git diff-tree --no-commit-id --name-only -r "$SHA")

is_canonical_event=false

# (i) Any change in folio-assistant/computations/
echo "$changed" | grep -qE '^folio-assistant/computations/.*\.(py|json)$' && is_canonical_event=true

# (ii) Content block .md/.ts of provable / definitional / remark kind
echo "$changed" | grep -qE 'content/.*\.(md|ts)$' && {
  for f in $(echo "$changed" | grep -E 'content/.*\.(md|ts)$'); do
    ts="${f%.md}.ts"; [ "$f" = "$ts" ] || ts="${f}"
    [ -f "$ts" ] && grep -qE '^export default (theorem|lemma|proposition|corollary|conjecture|definition|remark)\(' "$ts" \
      && is_canonical_event=true
  done
}

# (iii) Three-calibration discipline blocks or canonical-derivation infra
echo "$changed" | grep -qE '(three-calibration|canonical-derivation|derivation_chain|e0_calibration|canonical_script_input|witness_reproducibility|codata_constants|experimental_constants)' && is_canonical_event=true
```

For PR review-comment events, pass through if comment body
mentions: `calibration`, `fit`, `empirical`, `numerology`, `magic
number`, `rationalization`, `CODATA`, `tautolog`, `back-fit`,
`Q_β`, `m_e`, `q_0`, `E_0`, `ρ_K`, `vol`, `hyperbolic`.

## Slot C — §4b dispatch table

| Specialist | When to run | What it checks |
|------------|-------------|----------------|
| `compute-audit` scanner (P1-P32) | Any changed `.py` | P12/P13/P31 (CODATA literal leakage, numerology), P32 (reproducibility), P30 (WitnessBuilder) |
| `canonical_script_input_audit.py` | Any changed `.py` | 3-input vs over-count vs vol-hyp-fitted classification |
| `derivation_chain_validator.py` | Any changed witness referencing derivation chains | Every numerical claim traces to first-principles axioms |
| `e0_calibration_audit.py` | Any change to $\mathbf{E}_0$, $Q_\beta$, $\rho_K$, or six-term | $\mathbf{E}_0$ form (A/B/C) discipline; CAL-3 cross-check |
| `witnessed-values` | Any changed block quoting numerical literals | Every literal uses `:val[...]`; no hardcoded drift |
| `scientific-accuracy` | Any changed proposition/theorem block with numerical claims | Claim is derived, not justified; no rationalization |
| `one-voice-audit` | Any changed block | Status leaks, work-tracker words that should be properly handled |
| `ontologist` | Any new symbol introduced | Notation register compliance |
| `compute_audit_scan` (full) | Session start + every 24h idle | Baseline scan over `folio-assistant/computations/` |

## Slot D — §4c finding taxonomy

| Violation | Severity | Definition | Auto-fix possible? |
|-----------|----------|------------|--------------------|
| `fourth-calibration` | critical | Script/block introduces an external input beyond {m_e, m_μ/m_e, Q_β(n)} | No — author ask |
| `coefficient-fit` | critical | Bethe-Weizsäcker / mass-formula coefficient labelled "ad hoc", "approx", "tuned to AME/CODATA" | Author ask; sometimes "demote to remark" |
| `numerology` | critical | Magic number ({2,8,20,28,50,82,126}, "0.7823...", any literal) asserted without derivation chain | Author ask |
| `hidden-codata-literal` (P31) | major | Free-floating CODATA string in production script outside the registry | Yes — `codata_constants` migration |
| `tautology` | major | "Derivation" that uses the result as input (LO tautology pattern, e.g. $\rho_K^{LO}$ via $m_p, m_n$ CODATA) | Yes — apply tautology banner + flag in `.md` |
| `archimedean-leak` | critical | Algebraic-side derivation consumes $\mathrm{Vol}(K)$, hyperbolic structure, Mostow constant, etc. | Author ask |
| `second-q0-pin` | critical | A second independent fit to $q_0$ beyond CAL-2 | Author ask |
| `second-hadronic-scale` | critical | $E_0$ pinned by something other than CAL-3 | Author ask |
| `three-route-convergence` | major | "Three routes agree at q_0" claim where routes compute different categorical objects | Author ask; demote to remark |
| `universal-extrapolation` | major | Single-atom result extrapolated to "universal" | Author ask; demote |
| `rationalization` | major | Prose in a proposition body arguing *why* a value is right rather than *deriving* it | `scientific-accuracy` rewrite or author ask |
| `over-count-3-input` | major | Script consumes both $m_p$ and $m_n$ from CODATA, double-counts hadronic | Yes — `canonical_script_input_audit` rewire |
| `vol-hyp-fitted` | major | Script's primary calibration is hyperbolic volume | Author ask; sometimes Class-C |
| `unverified-rho-K` | major | $\rho_K$ used without a derivation-chain witness | Author ask; sometimes Class-B |
| `ck-binary-negative-result` | major | Precision-ladder block (Q_β $c_k$, α_EM Habiro factor, any convergent truncation-order series) frames a coefficient as a binary negative result (`un-wire`, `drop c_k`, `just a fit`, `fails to beat`, `should be reverted`, `negative result`) without the tiered (proved / near-match / fitted) framing or a citation to `2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`. The four-session wire/un-wire flip-flop signature. | Add tiered framing or cite the canonical doc; author-assist |
| `negative-result-in-paper` | major | Paper block whose primary content is a negative empirical finding (tag `negative-result` / `falsified` / `superseded` / `scaffolding`, or `.md` opens with `## Status: ... falsified` / `## Status: open R&D — no known` / `**Hypothesis falsified**` / `Errata banner — ... superseded`). Detected by `canonical-no-negative-result-in-paper` checker. `kind: conjecture` blocks are exempt. | Author ask; the fix is to move the content to a dated `docs/audits/` doc and replace the paper block with a one-line forward reference. Established by `docs/audits/2026-05-31-ck-exploratory-probes-removed.md`. |

Automated by the `canonical-ck-tiered-not-binary` qa-criterion
(`content/pipeline/qa-criteria-registry.ts` →
`checkCanonicalCkTieredNotBinary` in `qa-checkers-extended.ts`).
It enforces **Rule 4** of the truncation-order canonical framing:
*report TIERED, never binary wired/dropped.* Context-gated on the
`precision-ladder` / `1ppb-roadmap` / `habiro` tags (or ladder prose);
passes when the block carries `near-match` / `tier` vocabulary or cites
the framing doc.

This is the **complement** to `canonical-no-negative-result-in-paper`
(PR #1574): that criterion catches falsified/superseded *probe-block*
leakage (`.ts` `negative-result`/`falsified`/`superseded` tags + `.md`
Status banners); this one catches the *prose-framing* failure mode
(binary wire/un-wire language in ladder context). Both are preventive;
neither fires on current content. Keep both registered.

### Allowed-class opt-outs (extends parent's defer band)

Per `docs/audits/2026-05-11-three-calibration-discipline-violations.md`:

| Class | What it is | How to mark |
|-------|------------|-------------|
| **Class-A** | Acknowledged stub with explicit "calibrated" / "tautology" banner — block/script openly states it is currently empirical and lists what would derive it | Banner in docstring (Python) or front-matter callout (`.md`); commit message cites `Class-A` |
| **Class-B** | Baseline-extraction script that *produces* the calibration input (e.g. computes $m_\mu/m_e$ → $q_0$, or extracts $Q_\beta$) — by definition it consumes CODATA | Filename or top-level docstring labels purpose; review confirms no algebraic-side claim is drawn from it |
| **Class-C** | Diagnostic probe / cross-check — read-only, never feeds a downstream witness, purpose is to *compare* an algebraic-side prediction against CODATA | Docstring `# Class: C — diagnostic probe` + no `*.witness.json` consumer |

When the watcher classifies a finding as `wontfix-allowed`, it
must record which class (A/B/C) and verify the class marker
exists. If the marker is missing, the finding is a violation and
the fix is to add the banner.

## Slot E — §4d discharge bands (examples)

| Band | Examples |
|------|----------|
| **Auto-discharge** | `hidden-codata-literal` (P31) → `codata_constants` import migration; `tautology` missing banner → add LO TAUTOLOGY banner + `.md` footnote; `over-count-3-input` with 3-input alternative scripted → switch the consumer |
| **Author-assist** | All other violations (fourth-calibration, coefficient-fit, numerology, archimedean-leak, second-q0-pin, second-hadronic-scale, three-route-convergence, universal-extrapolation, rationalization, vol-hyp-fitted, unverified-rho-K) |
| **Defer** | Class-A/B/C with banner present |

## Slot F — §4e author-ask templates

Per-violation template:

```markdown
**canonical-watcher ask — `<block-or-script>`** (from <source>)

- Violation: `<kind>` — <one sentence>
- Severity: <critical | major | minor>
- File: <github-blob-url to `.md` (or `.py` if compute-specific)>
- Evidence: `<file:line>` — `<offending literal/claim>`
- Attempted: <which fixes/scanners were tried>
- Question:
  1. Acknowledge as Class-A/B/C exception (add banner)
  2. Derive (point to a derivation chain or open as TodoItem)
  3. Demote to remark / null result
```

## Slot G — §5a backlog discovery

**Compute side:**

```bash
python3 folio-assistant/computations/canonical_derivation_pipeline_compliance.py
jq '.recommended_next[]' folio-assistant/computations/canonical-derivation-pipeline-compliance.witness.json
```

**Content side:**

```bash
find content -type f -name '*.ts' -print0 \
  | xargs -0 -r grep -lE '^export default (theorem|lemma|proposition|corollary|conjecture|definition|remark)\(' \
  | sort -u > /tmp/_cw_all_blocks.txt
```

## Slot H — §5b prioritisation

1. **Severity from §5a aggregator** (`fail` > `warn` > `pass`).
2. **Downstream dependents** (more dependents → earlier) via `uses[]`.
3. **Last-audit recency** (older → earlier) from `queue.audited[]`.
4. **Alphabetical** as tie-breaker.

## Slot I — §6 invariants

| Invariant | Check |
|-----------|-------|
| No new free-floating CODATA literal | `python3 folio-assistant/computations/compute_audit_scan.py` reports no new P31 hits vs `origin/main` |
| No new tautology without banner | New scripts/blocks that consume their own result either carry the LO tautology banner or are flagged in queue |
| No new fourth-calibration script | `canonical_script_input_audit.py` over-count delta vs `origin/main` is ≤ 0 |
| No new naked numerology | Any new numerical literal in proposition/theorem bodies uses `:val[…]` directive |
| Derivation chain unbroken | `derivation_chain_validator.py` all-passed remains true |

## Slot J — Probe follow-up discipline (mandatory for every probe / audit)

Every probe / audit / structural claim in a witness JSON, an audit
doc, or a content block **must** explicitly report (or note as N/A
with reason) the following three diagnostics. This is the
**noise-reduction discipline** — most "interesting" probe findings
turn out to be either bar-symmetry artifacts, GB-filtration boundary
effects, or jet-order mis-attributions, and the only way to keep them
straight is to label them at authoring time.

### The three required diagnostics

1. **GB filtration level.** Where does the claim sit in the
   Gröbner-Shirshov filtration of `H_n(q)`? Report the Coxeter length
   `ℓ(w)` of the largest braid word the claim involves, OR `N/A` if
   the claim is not about a Hecke element. Example:

   > "GB filtration: ℓ ≤ 11 (atomic proton braid at H_3)"
   > "GB filtration: N/A — claim is about content-block dependency graph"

2. **Jet order.** Which power of `h = q − q⁻¹` (or `q − 1`) does the
   claim live at? This is the **load-bearing question** for h^{2k}
   probes — getting it wrong is the #1 source of noise (e.g., a probe
   reporting an h⁴ closure that's actually h² mis-labelled).

   > "Jet order: h⁴ (k=2 in Yekutieli tessellation refinement)"
   > "Jet order: leading-h^0 + h^2 correction (Family A)"
   > "Jet order: all-orders resummation (Φ_q-pentagon)"

3. **Bar-symmetry status.** Per the duality tracker
   [`docs/duality-tracker.md`](../../../docs/duality-tracker.md) D1,
   classify the claim as bar-symmetric (retained), bar-anti-symmetric
   (discarded), or trivial. This catches "phantom" claims that come
   from un-canceled bar-anti-symmetric residuals.

   > "Bar-symmetry: bar-symmetric (P_avg image)"
   > "Bar-symmetry: bar-anti-symmetric — should cancel, residual = 305 ppm flavor split"

### When to apply

- **Probes**: every script under `folio-assistant/computations/`
  that emits a witness with a structural claim (not just numerical
  data) must include these in the witness `description` or a new
  `probe_diagnostics` field.
- **Audit docs**: every `docs/audits/*.md` with a "headline finding"
  table must include a row per diagnostic for each headline claim.
- **Content blocks**: every new `prop:` / `conj:` / `thm:` block
  that makes a structural claim must include `**Diagnostics:**`
  with the three lines in the .md narrative (just above
  `## Cross-references`).

### What this discipline prevents

- ❌ **Jet-order mis-attribution** — Phase 5g (constituent step
  factor `(2q-1)`) was falsely-globally identified as canonical at h^0
  before being downgraded to "h^5 numerical accident at q_0" per
  the 2026-05-23 audit. A `Jet order: h^5` label at probe authoring
  time would have caught this.
- ❌ **GB-filtration boundary effects** — claims at ℓ = 11 (atomic
  proton) often don't extend to ℓ ≥ 14 (atomic D); per-script
  ℓ-labels help reviewers see this.
- ❌ **Bar-anti-symmetric leakage** — most "anomaly" findings are
  bar-anti-symmetric residuals that should cancel; classifying at
  authoring time makes them visible.

### Cross-reference

- [`docs/duality-tracker.md`](../../../docs/duality-tracker.md)
  — coordinate-side duality classifier and probe-status tracking
- [`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`](../../../docs/audits/2026-05-23-lambda-scale-canonical-unification.md)
  §"13-driver menu" — the canonical mechanism catalogue
- [`bar-involution.md`](../../../content/quantum-observable-universe/braids-and-knots/bar-involution.md)
  + Tables 1-4 — bar-symmetry classification reference

## Domain-specific anti-patterns (extends parent)

- ❌ Auto-fix a `coefficient-fit` or `numerology` finding. Those
  always require author input — the framework's "no fits beyond
  three calibrations" is a mathematical claim about the paper,
  not a code-style choice.
- ❌ Silently mark a Class-A/B/C opt-out without verifying the
  banner/docstring marker exists in the source. The marker is
  what makes the opt-out auditable.
- ❌ "Resolve" a finding by reframing it as "this is acceptable
  because…". The discipline is not negotiable per-PR — if you
  think a violation is acceptable, escalate per §4e and let the
  author make that call.
- ❌ Emit a probe witness without the §Slot J diagnostics. A claim
  without (GB filtration, jet order, bar-symmetry) is unauditable
  — it cannot be cross-referenced against the duality tracker or
  the 13-driver menu without these labels.
