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
`todos/canonical-watcher-queue.json` and
`todos/canonical-watcher-ledger.md`.

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
