---
name: production-vs-exploratory-discipline
roles: [reader, collaborator, owner]
description: >
  Distinguish PRODUCTION (canonical-only, no fits) from EXPLORATORY
  (empirical-fit probes OK as shape-hints) from NUMEROLOGY (post-hoc
  fits to known constants). The CAL-4 / empirical-fit antipattern is
  the single most common review-churn source in this repo:
  agents repeatedly promote empirical fits into production scripts,
  cheat-sheet "closed" status, dashboards, and named LAMBDA_*
  constants without categorical derivation. This skill is the
  bright-line guide for which output goes where, the 13-driver
  categorical-menu, and the §Rule-14 escalation path for off-menu
  coefficients.
allowed-tools: Read Bash Grep Glob Edit Write AskUserQuestion Skill
---

# Production vs exploratory vs numerology — the bright-line guide

## Why this skill exists

The lambda_scale CAL-4 cluster (PRs #888, #892, #895, #904, #909,
#916, #917, #920, #923, #928, #939, #941, #942, plus the
`d348ad8c` Faddeev-pentagon spike + 4 others) is the largest
single source of post-merge review churn in this repo's history.
The single recurring antipattern: **agents probing empirically,
finding a numerical near-match, and promoting it to production**
— sometimes within minutes of the original probe, before the
near-match has any categorical derivation.

By the time PR #895 retired `LAMBDA_PROTON_DOC = 2.4599527869`,
five separate "5/2 − h²·G" coincidence candidates had been
proposed, falsified, and re-proposed in different framings.
PR #701 needed five independent structural-falsification routes
to settle the question. Rule 14 (this skill §5) is the
preventative codification.

## Three categories of output

### PRODUCTION

What it is — the framework's published predictions. Lives in
the canonical compute pipeline; reported in observable dashboards;
referenced as "the framework predicts X".

Concrete locations:
- `computations/m_p_borromean_verification_50dps.py`
  (m_p chain)
- `computations/mass_table_ppb.py` and the
  `*_50dps.py` family
- `computations/canonical_*` family
- Named constants: `LAMBDA_PROTON_*`, `LAMBDA_NEUTRON_*`,
  `ALPHA_*`, `Q_*`, anything in `codata_constants.py`
- Witnesses with naming `*-50dps.witness.json`, `*-canonical.witness.json`
- `docs/canonical-derivation-cheat-sheet.md` §5 Migration
  Backlog "closed" status
- `computations/per-observable-100x-status.witness.json`
  (the 100× dashboard)
- `computations/onepb-status-dashboard.witness.json`

**Discipline.** Production accepts ONLY:
1. **Proved theorems.** Algebraic identities or Lean-proved
   statements (e.g. the canonical Wedderburn theorem
   `(1/4)·Σ dim_q V_λ = 5/2 + (3/4)h²` from PR #701).
2. **Conjecture-conditional substrate forms with explicit
   owner authorisation.** E.g. PR #895 adopted the canonical
   Wedderburn form as `λ_scale` despite the 3% framework gap
   to CODATA — owner authorized this swap because the form is
   substrate-derived (no CAL-4) even though not yet proved to
   match CODATA at ppb.
3. **Standard-physics imports.** Three measured masses: CAL-1 m_e,
   CAL-2 m_μ, CAL-3 m_π. m_e from CODATA (the unit); m_μ from CODATA
   fixes q_0 via m_μ/m_e (phys-obs may anchor q_0 on the more-precise
   proton ratio m_p/m_e); m_π from PDG (the orthogonal meson scale).
   These are the three calibration anchors per CLAUDE.md
   §"three-calibration discipline". Q_β is **derived** from
   CAL-1+CAL-2, not a calibration.

**Disallowed in production.** Any of:
- Empirical fits against CODATA values (e.g.
  `LAMBDA_PROTON_FITTED_FROM_CODATA = 2.4599527869` literal —
  PR #888 retired)
- Möbius / rational-function ansätze that hit CODATA via
  fitting (e.g. `(4-q)/(4q+3)` — PR #892 demoted to conjecture)
- PSLQ matches against transcendental constants without a
  derivation explaining the match (e.g. `5/2 − h²·G`
  numerology — PR #701 falsified across 5 routes)
- Higher-order h^k corrections fit to close the residual gap
  to CODATA (e.g. `α = (3/4 + 1 − G)·h^4` — flagged as
  EXPLORATORY in PR #916 per user direction 2026-05-23)

### EXPLORATORY

What it is — shape-probing, hypothesis-generation work. May
contain empirical fits, PSLQ near-matches, ansatz tests, "what
shape is this?" computations. Lives in `probe_*` scripts and
`*_alt_*` / `*_refinement_*` family.

Concrete locations:
- `computations/probe_*.py`
- `computations/lambda_scale_alt_*.py`
- `computations/lambda_scale_refinement_*.py`
- `computations/strategy_d_*.py`
- `computations/spike_*.py`
- `docs/audits/2026-??-??-*-spike-*.md` (audit docs)

**Discipline.** Exploratory probes:
1. **MAY contain empirical fits** as shape-hints
   (e.g. "the residual ≈ 0.86·h^4 — what's α structurally?")
2. **MUST clearly label themselves as exploratory** in the
   docstring header (`EXPLORATORY shape-probe`, not bare claim)
3. **MUST NOT be referenced as production** in the cheat-sheet,
   dashboards, or PR bodies (cross-reference is fine; "framework
   prediction" claim is not)
4. **SHOULD propose categorical derivations** for any
   coefficient they find, citing the 13-driver categorical menu
   (this skill §4)
5. **MUST classify their witness assertion** so a numerical
   negative result doesn't block CI — use the "assert the
   refutation" pattern (cf. `probe_phiq_n_star_rule.py`):
   `assert(no_match)` not `assert(match)`, so `allPassed=true`
   on the expected-negative outcome

**Allowed in exploratory.** Anything that PROBES shape:
- PSLQ at high precision against substrate-natural bases
- Ansatz tests (does `5/2 + α·h^k` for small α work?)
- Numerical near-match documentation
- Cross-cluster comparisons (e.g. PR #909 stage-1 found
  `5/2 − h²·G + (−h^6/6)` at 32 digits — exploratory hint
  about the next-order term)
- Visualisation / sweeps over q-window

### CANONICAL INFRASTRUCTURE (distinct from both PRODUCTION and EXPLORATORY)

What it is — structural pipeline components that are
mathematically valid and part of the canonical derivation chain,
but whose specific NUMERICAL OUTPUT at q₀ is not yet proved.
The INFRASTRUCTURE is canonical; the specific coefficient is
exploratory.

**The Yekutieli distinction (critical — 2026-05-24):**

| Component | Status | Why |
|---|---|---|
| Yekutieli 2015 non-abelian Stokes theorem | **CANONICAL** | Valid external mathematics; published, peer-reviewed |
| Geom(K) functor (prop:geom-universality) | **CANONICAL** | Unique functional satisfying additivity + functoriality + normalisation |
| Three-layer chain (algebra → geometry → observable) | **CANONICAL** | Structural pipeline; Geom IS the geometrization step |
| Linking weight concept (Geom_full / Geom_leading) | **CANONICAL** | What Geom assigns to multi-component links beyond bare volume |
| Non-abelian Stokes applied to 𝓑₃'s 8 ideal octahedra | **CANONICAL INFRASTRUCTURE** | The APPLICATION of Yekutieli to the Borromean surface is structural |
| S₄↓S₃ branching factor = 2/5 | **PROVED** (Lean) | Standard S_n representation theory |
| The specific coefficient `−G·h²` at q₀ | **EXPLORATORY** | The numerical claim that the h² coefficient IS −G (Catalan) is not yet derived from the canonical infrastructure |

**The user's position (2026-05-24):** "I do think we are missing
a quadratic term. We just haven't properly derived it yet." The
h² correction from Geom EXISTS (the canonical infrastructure
demands it); the specific VALUE (−G? something else?) is what's
unproved. Scripts implementing the Yekutieli infrastructure are
CANONICAL INFRASTRUCTURE, not deprecated — only the specific
−G·h² NUMERICAL CLAIM is exploratory.

**Concrete rule:** a function like `geom_full_borromean()` that
implements the Geom pipeline IS canonical infrastructure. A
function like `yekutieli_correction_h2()` that returns the
specific `−G·h²` value IS exploratory. Don't deprecate the
infrastructure because the coefficient is unproved.

### NUMEROLOGY

What it is — post-hoc fits to known constants (G, π, ζ-values,
modular forms, hyperbolic-knot volumes, etc.) without any
categorical reason for that constant to appear. Numerology is
NOT the same as exploratory — it's a SUB-CATEGORY of empirical-
fit that specifically anchors to a named transcendental.

Concrete examples from the cluster:
- `5/2 − h²·G` (G = Catalan; 5.6 ppm match; PR #701 falsified)
- `5/2 + (3/4)·h² + α·h^4` for α = `(3/4 + 1 − G)` (22 ppm
  near-match in PR #916 — the "+1" leading h^4 is numerology)
- `1/(1 − h·q_0^10)` (19 ppm match; cluster currently treating
  as conjecture-conditional on color-tube structural backing)
- `λ ?= ratio of two hyperbolic-knot volumes` (Bring-Bloch
  search Tier 0-5; all 52 candidates fell into the numerology
  basin)

**Discipline.** Numerology findings:
1. **MUST be labeled "PSLQ coincidence" or "post-hoc fit"** in
   the audit doc that records them
2. **MUST be checked against the q-locality criterion** — does
   the form predict the right value at `q_0 ± ε`, or does it
   only match at q_0? PSLQ at q_0 finds coincidences that fail
   q-locality.
3. **MUST be tested against the 13-driver canonical menu** (§4)
   — does the numerology constant appear in any of those
   derivations naturally? If yes, it's a structural candidate;
   if no, it's coincidence-basin.
4. **SHOULD be retired explicitly** if a falsification lands
   (e.g. PR #701's 5-route falsification of `5/2 − h²·G`)

**Disallowed.** Numerology MUST NEVER enter production. Period.
The CAL-4 antipattern this skill exists to prevent.

## The 13-driver canonical menu

Per the canonical-unification audit (PR #916,
`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`),
every coefficient in a production substrate prediction must be
derivable from ONE or more of these 13 categorical drivers:

| # | Driver | Where it lives | What it gives |
|---|---|---|---|
| 1 | Faddeev recursion `Φ_q(qz) = (1/(1-z))·Φ_q(z)` | `_phi_q_util.py`, [faddeev1996] | All-orders Φ_q expansion |
| 2 | Φ_q power series `log Φ_q(z) = Σ z^n / (n·(1-q^{2n}))` | `_phi_q_util.py` | h^k Bernoulli-like factors |
| 3 | Rogers Li_2^q pentagon (5-term functional eq) | `_li_2_q_util.py`, [kashaev1995] | h^k constraints via 5-term consistency |
| 4 | Yang-Baxter equation (R-matrix cubic) | `hecke_core.py`, [jimbo1986] | Iterated h^k braid corrections |
| 5 | Hexagon equations (braiding ↔ fusion) | Monoidal-category structure | h^k braiding-fusion compatibility |
| 6 | Frobenius reciprocity (non-degenerate pairing) | `frobenius-pairing.md` | h^k pairing duality |
| 7 | Quantum 6j-symbols (Racah-Wigner) | Biedenharn-Elliott + orthogonality | h^k partition-decomposition |
| 8 | Modular dual `q ↔ q̃` (S-transformation) | MTC / Reshetikhin-Turaev | Asymptotic h^k constraints |
| 9 | KLR positivity (Khovanov-Lauda-Rouquier) | `kl-canonical-basis` | Non-neg integer h^k coefficients |
| 10 | MacMahon partition-algebra identities | `dim_q V_λ` formulas at H_n | h^k from partition sums |
| 11 | Lobachevsky / Catalan-G identities | `Vol(𝓑_3) = 8G`, `Λ(π/4) = G/2` | Topological-volume constants |
| 12 | Chern-Simons perturbative (Ohtsuki series) | WRT TQFT at large level | h^k from CS asymptotics |
| 13 | Crystal-graph / Kashiwara `q → 0` limit | KLR canonical bases at q=0 | h^k from crystal structure |

Every production h^k coefficient must come from ≥ 1 of these.

## Rule 14 — escalate off-menu coefficients to author

**If a candidate h^k coefficient cannot be derived from any of
the 13 drivers, the agent MUST escalate to the author/owner via
`AskUserQuestion` BEFORE adopting it in production.**

Exploratory shape-probing is permitted without escalation — but
the moment a coefficient is proposed for production (cheat-sheet
"closed" status, dashboard refresh, named LAMBDA_* constant), the
escalation must happen.

The escalation must include:
- Exact numerical coefficient at MPFR-50dps
- Candidate categorical mechanism (if any partial hint exists)
- Which of the 13 drivers the agent has tried to map it to
- What closure of this coefficient would unlock

The owner may then:
1. Identify a 14th driver this skill missed (which extends the
   menu — please update this skill)
2. Authorise the coefficient as conjecture-conditional with
   explicit production adoption (analogous to PR #895's
   canonical Wedderburn move)
3. Direct the agent to wait until categorical derivation lands

## Decision tree — where does my code go?

Asking yourself "is this production or exploratory?" — walk
this tree:

```
Does my code change any of these production locations?
  - m_p_borromean_verification_50dps.py
  - mass_table_ppb.py
  - LAMBDA_*, ALPHA_*, Q_* named constants
  - cheat-sheet §5 "closed" status
  - per-observable-100x-status.witness.json
  - onepb-status-dashboard.witness.json
  - codata_constants.py (CAL anchors)
  ↓
  YES → it's PRODUCTION code.
        Every coefficient must come from the 13-driver menu.
        Any off-menu coefficient → Rule 14 escalation.
        Use `proved theorem | conjecture-conditional with explicit
        owner authorisation | standard-physics CAL anchor` only.
        ↓
        If you can't satisfy this, the code does NOT go in
        production. Make it a probe instead.
  ↓
  NO → it's EXPLORATORY (probe, ansatz test, shape-hint).
       Empirical fits OK. PSLQ coincidences OK as documented
       finds. MUST label docstring "EXPLORATORY shape-probe".
       MUST NOT be referenced from production code or cheat-sheet
       "closed" status. CAN be referenced as a documented audit /
       hypothesis-generation finding.
```

## Common antipatterns (recognize + avoid)

### Antipattern 1: "the literal is the framework prediction"

Symptom: `LAMBDA_PROTON_DOC = 2.4599527869` hardcoded literal
labeled as if it were the framework's prediction.

Why it's wrong: 2.4599527869 was obtained by solving the
formula `m_p = m_e · Vol/ℏ_q² · λ` for λ using CODATA m_p as
input. That's CAL-4 — a 4th calibration anchor disguised as a
substrate quantity.

Fix: rename to `LAMBDA_PROTON_FITTED_FROM_CODATA` (truth-in-naming,
PR #888) AND add a banner explaining the discipline violation,
THEN replace with a canonical form (PR #895's Family A swap).

### Antipattern 2: "PSLQ found a 5.6 ppm match → it's structural"

Symptom: PSLQ at q_0 finds `5/2 − h²·G ≈ 2.4599666` matches
the CODATA-derived target at 5.6 ppm; agent claims this is the
substrate form.

Why it's wrong: PSLQ at a SINGLE q value finds numerical
coincidences. The structural test is q-locality: does the form
match across the substrate window `q_0 ± ε`? AND is the form
derivable from the 13-driver menu?

**The q-locality gate (mandatory pre-flight, per commit
`c18e562b9` on main 2026-05-23).** Sweep q ∈ [q_0 − 0.05,
q_0 + 0.05] and plot `residual = target − candidate` vs q.

- **Genuine structural identity** → smooth residual (slope ≈ 0
  across the window).
- **Substrate-q_0 coincidence** → zero-crossing with slope
  ~10⁷ ppm/q (matches at q_0, diverges rapidly away).

The empirical-exhaustion tally on 2026-05-23 ran q-locality on
four known λ_scale near-matches. **0 / 4 surviving:**

  | candidate | slope (ppm/q) |
  |---|---:|
  | `1/(1 − h_q · q_0^{10})` (Faddeev × Bring) | −1.5×10⁷ |
  | `5/2 − h_q²·G` (numerology) | −1.7×10⁷ |
  | V_7 = Σ dim_q V_λ / [4]_q (PR #916 Strategy H) | −1.86×10⁷ |
  | `5/2 − ℏ_q²·⟨𝓑_3⟩(q_0^{1/2})` (PR #916 Strategy G) | −1.69×10⁷ |

The q-locality gate is now a first-class pre-flight filter. Any
near-match candidate that fails it is automatically
coincidence-basin, regardless of how close the ppm value at q_0.

**Mandatory pre-flight before any "structural" claim.** Apply
the q-locality gate. If slope is < ~10² ppm/q across the
substrate window, the candidate has earned the right to be
analyzed for the 13-driver menu. If slope is > ~10⁵ ppm/q,
it's coincidence-basin — stop.

Fix: PR #701 falsified `5/2 − h²·G` across 5 routes:
- 32 sign-flipped Wedderburn sums at H_4 all give positive h²
- Hecke level scan H_2 through H_7 all give positive h²
- Transcendental ansätze: no match within 1e-3
- Single-knot Vol search: no manifold has Vol = 18.03 within
  0.28%
- Family A theorem directly: c_2 = +3/4 ≠ −G

The 5.6 ppm match is in the **coincidence basin** at q_0;
PSLQ-level matches at a single substrate point don't imply
structural identity.

### Antipattern 3: "we need this h^4 to close the residual"

Symptom: production prediction is off by 670 ppm; agent finds
`α = 0.86 ≈ (3/4 + 1 − G)` gives 22 ppm; agent commits this to
production.

Why it's wrong: the `+1` leading h^4 coefficient has NO
derivation from any of the 13 drivers. It was fit to close the
gap. CAL-4 violation.

Fix: explicitly label as EXPLORATORY shape-probe (PR #916
commit). Escalate to author per Rule 14. Find a categorical
derivation OR get owner authorisation OR retire the candidate.

### Antipattern 4: "Family A is the canonical theorem, so the
framework is done"

Symptom: PR #895 swapped `LAMBDA_PROTON_FITTED_FROM_CODATA →
canonical Wedderburn Family A`. Some readings then claim "the
framework's prediction is now correct" without acknowledging
the 3% framework-vs-CODATA gap.

Why it's wrong: Family A is a PROVED theorem about the
specific Wedderburn sum `(1/4) Σ dim_q V_λ`. Asserting that this
equals λ_scale is the production-adoption decision; the 3% gap
is the framework's honest accuracy under this adoption — not a
match.

Fix: see PR #917 dashboard refresh — m_p prediction is now
966 MeV, ~3% off CODATA. Frame it as the framework's
substrate-derived prediction, not as a CODATA match. Further
refinements (Yekutieli additive, Bring color-tube, h^4) are
conjecture-conditional improvements.

### Antipattern 5: "Reading A vs Reading B agnosticism"

Symptom: agent proposes two competing readings of a structural
argument (e.g. "Yekutieli REPLACES Wedderburn h²" vs
"Yekutieli ADDS to Wedderburn h²") and doesn't pick one.

Why it's wrong: both readings give different production
predictions. Punting forces the next agent to make the same
choice.

Fix: per CLAUDE.md §"Agent work-plan policy" rule 5 (escalate
inconsistencies), AskUserQuestion to decide. The
canonical-unification audit (PR #916) explicitly distinguishes
exploratory comparison from production claim — use that pattern.

### Antipattern 6: "rebasing with witness drift = whatever, just push"

Symptom: rebasing merges in witness JSON drift from upstream
without re-running the validators; witness commitSha and
scriptCommitSha don't match the rebased commit; downstream
script-quality checkers fail.

Fix: per `prepare-merge.md` §1.a, the witness-regen loop
auto-resolves drift by re-running the 5 self-emitting
validators. THIS IS NOT OPTIONAL — CI will fail without it.

## Pre-promotion checklist (run before adopting any candidate in production)

If you are about to:
- modify `m_p_borromean_verification_50dps.py` or any `*_50dps.py`
  production script,
- add or change a `LAMBDA_*`, `ALPHA_*`, `Q_*` named constant,
- mark a cheat-sheet §5 Migration Backlog item as "closed",
- update `per-observable-100x-status.witness.json` or
  `onepb-status-dashboard.witness.json`,

then run this 7-step pre-promotion checklist BEFORE the commit.
Skipping any step has caused review-cycle churn in the cluster's
history — every cluster CAL-4 PR that needed multiple Gemini
review rounds skipped at least one of these.

### Step 1 — categorize the candidate (production / exploratory / numerology)

```bash
# Where is the proposed code going?
git diff --cached --name-only | grep -E '_50dps\.py|LAMBDA_|ALPHA_|Q_50_DIGIT|onepb-status|per-observable-100x'
```

If any output, it's a PRODUCTION change. Continue checklist. If
nothing, it's exploratory — label the docstring `EXPLORATORY
shape-probe` and commit without further gate.

### Step 2 — q-locality gate (mandatory for any "structural" claim)

Sweep `q ∈ [q_0 − 0.05, q_0 + 0.05]` and compute the residual
slope. Reference implementation in
[`q_dilog_tower_q_locality_spike.py`](../../computations/q_dilog_tower_q_locality_spike.py)
(or the equivalent on `claude/iw-explore-q10-2026-05-23`).

| slope range | classification | action |
|---|---|---|
| `< 10² ppm/q` | smooth (passes q-locality) | proceed to step 3 |
| `10² – 10⁴ ppm/q` | marginal | escalate to author (Rule 14) before production |
| `> 10⁵ ppm/q` | coincidence-basin | RETIRE; do not promote |

The 4 known cluster near-matches all fail this gate (slopes
~10⁷ ppm/q). Run the gate; report the slope in the commit message.

### Step 3 — 13-driver categorical menu check

Which of the 13 drivers (this skill §"13-driver canonical menu")
does the candidate coefficient come from? Cite by number:

```
λ_scale = canonical + Yekutieli additive at h²
  - canonical:       Driver 10 (MacMahon partition-algebra)
  - Yekutieli per-cell:  Driver 11 (Lobachevsky-Catalan: G = Vol(𝓑_3)/8)
```

If the candidate cannot be traced to ≥ 1 driver, **invoke Rule 14**:
escalate to author via `AskUserQuestion`. Do not commit production.

### Step 4 — q-locality on the FULL CANDIDATE, not just the leading term

A common slip: agents q-locality-gate the LEADING term (passes)
and skip the gate on the SUBLEADING correction (which fails).
Per the cluster: V_7's leading 5/2 passes; the h² coefficient
−13/16 fails q-locality. Check EVERY h^k coefficient up to the
order you claim.

### Step 5 — naming discipline

Production constants must be named:

| pattern | meaning | example |
|---|---|---|
| `*_CANONICAL` or unsuffixed | proved theorem | `LAMBDA_PROTON_FAMILY_A` |
| `*_FITTED_FROM_CODATA` | empirical fit (NEVER imported as λ_scale) | `LAMBDA_PROTON_FITTED_FROM_CODATA` |
| `*_CODATA_VALIDATION` | standard-physics anchor (CAL-1/2/3) | `M_P_MEV_VALIDATION` |
| `*_EXPLORATORY` | shape-probe result | `LAMBDA_PROTON_EXPLORATORY` |

Mislabeling has been the most common review-thread cause —
the literal `LAMBDA_PROTON_DOC = 2.4599527869` looked production-
ready but was fitted. PR #888 fix: rename to
`LAMBDA_PROTON_FITTED_FROM_CODATA` (truth-in-naming). DO this
proactively in your own PR.

### Step 6 — register the witness assertion correctly

Falsification probes (expected-negative outcomes) MUST assert
the refutation so `allPassed: true`:

```python
# Wrong — witness allPassed: false on the expected-negative outcome
w.add_assertion("strategy_g_skein_yields_lambda_scale",
                computed=val, expected=target, tolerance=1e-6)

# Right — witness allPassed: true; CI / audit dashboards stay green
identity_falsified = int(not (abs(val - target) < target * 1e-6))
w.add_assertion("strategy_g_single_polynomial_identity_falsified_at_1ppm",
                computed=identity_falsified, expected=1, tolerance=None,
                source="...")
```

Reference: `probe_phiq_n_star_rule.py` for the canonical pattern.
Get this wrong and `validate` CI fails on every PR that registers
an honest-negative probe. The h^4 refinement probe in PR #916
hit this; commit `d89dc364` was the fix.

### Step 7 — banner the script (mandatory for exploratory probes)

Top of every `probe_*.py` / `*_alt_*.py` / `*_refinement_*.py`:

```python
"""EXPLORATORY shape-probe (per .claude/skills/local/production-vs-exploratory-discipline.md).

This script is exploratory hypothesis-generation; the finding it
surfaces is NOT for production without:
  - passing the q-locality gate (step 2 of pre-promotion checklist)
  - tracing to one of the 13 canonical drivers
  - explicit owner authorisation if off-menu (Rule 14)
"""
```

The banner is the bright line the post-hoc audit (compute-audit
skill) looks for. Without it, the script will be flagged as a
production candidate and trigger CAL-4 review threads.

### One-line gate summary

```
production change?  → Step 1 yes  → Step 2 q-locality < 10² ppm/q  → Step 3 13-driver cite  → Step 4 every h^k  → Step 5 naming  → Step 6 witness  → Step 7 banner
                                                                      (any "no" → Rule 14 escalation)
```

## Tunable-knob fences (`EVOLVE-VALUE` markers)

A syntactic complement to the categories above, adopted (and **inverted**)
from AlphaProof Nexus's `EVOLVE-VALUE` markers (arXiv:2605.22763; see
[`docs/audits/2026-06-06-alphaproof-nexus-comparative-assessment.md`](../../../docs/audits/2026-06-06-alphaproof-nexus-comparative-assessment.md)).
There the marker *grants* a search agent freedom to vary a value; here it is
a **fence that labels the few legitimately tunable knobs** — everything
outside a fence is FIXED (canonical / derived, never tuned).

Fence syntax (compute scripts):

```python
# EVOLVE-VALUE-START kind=production knob=N rationale="truncation order; N>=log10(1/eps)/2.07-1"
N_TRUNCATION = 5
# EVOLVE-VALUE-END

# EVOLVE-VALUE-START kind=exploratory knob=c_3 see=docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md
C3_NEAR_MATCH = -2.0   # J_Hopf(q=1) near-match — NOT a derived value
# EVOLVE-VALUE-END
```

Rules:

| Situation | Allowed? |
|---|---|
| Vary a `kind=exploratory` knob in a `probe_*` / exploratory script | ✓ (that is what exploratory scripts are for) |
| Vary a `kind=production` knob | ✓ **only** if the stated `rationale` still holds (e.g. raising a truncation order for more precision) |
| Tune a value **outside** any fence | ✗ — it is canonical / derived; changing it is a CAL-4 / numerology risk |
| Introduce a **new** `kind=production` fenced knob off the 13-driver menu | ✗ → **Rule 14** escalation |
| A `:val[…]`-witnessed (derived) value inside an *exploratory* fence | ✗ contradiction — a value is derived **or** tunable, never both (`witnessed-values.md`) |

The fence makes "what may be searched" auditable and gives the
production/exploratory bright line a concrete syntactic hook: a post-hoc
audit can grep `EVOLVE-VALUE-START kind=production` and check each knob's
`rationale` against the 13-driver menu, and grep `kind=exploratory` to
confirm those values never leak into a `canonical_*` / production script.

## How to recognize what category an EXISTING script is in

Grep / file-pattern heuristics for retrospective audit:

```bash
# Production scripts — strict no-fits required
grep -rln '_50dps\b' computations/*.py | wc -l
grep -rln 'def main' computations/canonical_*.py | wc -l
grep -rln '^LAMBDA_\|^ALPHA_\|^Q_50_DIGIT_STR\b' computations/*.py | wc -l

# Exploratory scripts — empirical fits OK
ls computations/probe_*.py 2>/dev/null | wc -l
ls computations/*_alt_*.py 2>/dev/null | wc -l
ls computations/*_refinement_*.py 2>/dev/null | wc -l
ls computations/*_spike_*.py 2>/dev/null | wc -l

# Numerology / coincidence-basin documented in audits
grep -rln 'PSLQ coincidence\|substrate-q_0 coincidence\|coincidence basin\|FITTED_FROM_CODATA' computations/ docs/audits/ 2>/dev/null
```

The naming convention is the first-line signal. A file named
`canonical_*.py` in `m_p_borromean_verification_50dps.py`'s import
graph is production; a file named `probe_*.py` is exploratory.
Cross-reference the docstring banner (Step 7 above) for
confirmation. Mismatched name vs banner is a review red flag.

## Where this skill connects

- **`compute-author.md`** (pre-work briefing for compute) —
  sibling skill; covers precision discipline and substrate-pure
  authoring patterns. This skill covers the discipline AFTER
  authoring (where does the result go?).
- **`compute-audit.md`** (post-hoc compute audit) — uses the
  3-category classification from this skill to flag
  empirical-fit candidates that ended up in production.
- **`canonical-watcher.md`** — the integration watcher that
  catches CAL-4 promotions; this skill is the rule it enforces.
- **`Δ_λ gate`** (CLAUDE.md, top-of-repo) — the standing
  "no 7th ansatz" rule; this skill's Rule 14 is the same
  discipline at the coefficient level.
- **`prepare-merge.md`** §1.a witness drift — the standardized
  rebase pattern for production scripts.

## Cluster history reference

Major events that informed this skill:

| Date | PR / commit | Discipline lesson |
|---|---|---|
| 2026-05-18 | PR #701 | Family A theorem; falsified `5/2 − h²·G` across 5 routes |
| 2026-05-18 | `docs/audits/2026-05-18-conjecture-proof-step3-yekutieli.md` | Yekutieli structural argument; load-bearing categorical-bijection step explicitly flagged |
| 2026-05-22 | PR #888 | Truth-in-naming: literal `LAMBDA_PROTON_DOC = 2.4599527869` → `LAMBDA_PROTON_FITTED_FROM_CODATA` |
| 2026-05-22 | PR #892 | Demoted `prop:mobius-limit-from-thimble → conj:` (Möbius pencil CAL-4) |
| 2026-05-22 | PR #895 | Production swap: canonical Wedderburn (Family A) replaces fitted literal |
| 2026-05-22 | PR #904 | Demoted `prop:lambda-scale-bring-bloch-identity → conj:` (vacuous-rfl + PSLQ refuted) |
| 2026-05-22 | af2d27ee | q-dilog Tier 0 spike negative |
| 2026-05-22 | PR #928 | q-dilog Tier 1+ (|V̂_S| + Q(ζ_60) + Tier-0 knots) negative |
| 2026-05-22 | `d348ad8c` | Faddeev-pentagon operator-theoretic spike: `1/(1 − h_q·q_0^10) ≈ λ_p` to 19 ppm; integer power n=10 traces to Bring color-tube weighted averaging (cheat-sheet §"Bring color-tube") |
| 2026-05-22 | PR #942 | Substrate flavor-split wired; `Δm/M_N = ℏ_q²·h_q·[2]_q·(1+ℏ_q³)/3` to 0.03% |
| 2026-05-23 | PR #916 | Reading-A-vs-B framing question; user direction "Yekutieli quadratic as added"; canonical-unification audit + 13-driver menu + Rule 14 + this skill |

The pattern across all these: the first probe finds an
empirical near-match, the agent labels it "structural", reviewers
flag it as CAL-4, the discipline is restored. Rule 14 + this
skill exist to short-circuit that cycle — escalate up front
rather than after CI / Gemini catches it.
