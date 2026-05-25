# Substrate-$q_0$ derivation — re-opened workplan

**Date:** 2026-05-25
**Branch:** `claude/substrate-q0-derivation-2026-05-25`
**Owner reversal:** 2026-05-25 (in response to PR
[#1246](https://github.com/litlfred/qou/pull/1246) CAL-2 critique)
**Supersedes:** 2026-05-08 coordination-ledger declination of
"subgoal-2 (substrate-$q_0$ derivation) out of scope"

---

## §0. Status

**Research-grade. Weeks-to-months scope. NOT a single-session task.**

This workplan is a **scaffold for future sessions**. It enumerates
candidate categorical / cohomological routes for deriving the
substrate parameter $q_0 \approx 1.10998$ from QOU structural data,
without consuming any physical input. It does **not** attempt the
derivation itself, propose a specific ansatz, run a numerical search,
or modify any existing content / compute / Lean files.

The deliverable for the *current* (scaffolding) session is exactly:

1. This workplan doc.
2. A draft PR registering the re-opened research direction.
3. One bounded first-session task identified for the next agent
   (§7 below) — an **inventory** task, not a derivation task.

Each candidate path listed in §3 is independently a multi-week
investigation. None are blessed; the workplan's purpose is to make
the option space visible and the anti-patterns explicit so future
agents do not silently fall into a back-fit.

---

## §1. Background — why $q_0$ was treated as CAL-2

The QOU framework derives every predicted observable from **three
calibration inputs** (the three-calibration discipline,
[`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
§8):

| Calibration | Pins | Mechanism |
|---|---|---|
| CAL-1 | $m_e$ (leptonic scale) | external CODATA |
| **CAL-2** | $q_0 \approx 1.10998$ (substrate parameter) | $m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^2$ with $\hbar_q = (q-1)/q$ |
| CAL-3 | $\mathfrak{E}_0$ (hadronic scale) | $Q_\beta$ |

CAL-2 currently pins $q_0$ via the CODATA muon-to-electron mass ratio
through a cohomological identity:

$$
\frac{m_\mu}{m_e} \;=\; \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
\qquad\text{where}\quad
\hbar_q = \frac{q - 1}{q},\qquad
\mathrm{Vol}(4_1) = 2 \cdot \Lambda(\pi/3) \approx 2.02988
$$

$\mathrm{Vol}(4_1)$ is itself a **pure cohomology** (Bloch–Wigner
motivic period, no empirical input), but $q_0$ is the unknown
algebraic root pinned by the equation — i.e., the framework currently
*observes* $q_0$ via the muon mass rather than *deriving* it.

### Why this was declined as "out of scope" on 2026-05-08

The 2026-05-08 coordination ledger ruled that subgoal-2 — deriving
$q_0$ from substrate-only structural data (no physical input) — was
research-grade and beyond the scope of the L2 100× campaign. The
ledger's working assumption was: $q_0$ is a free parameter of the
framework, pinnable to the universe we live in via CAL-2 (the muon
mass), and the framework's testable content is the per-observable
predictions downstream of CAL-2.

### Why the owner reversed the declination on 2026-05-25

PR [#1246](https://github.com/litlfred/qou/pull/1246) and the
companion audit
[`docs/audits/2026-05-25-cal-2-cohomological-vs-calibration-critique.md`](../audits/2026-05-25-cal-2-cohomological-vs-calibration-critique.md)
(branch `claude/busy-lamport-5NS40`) re-examined the CAL-2 status and
argued that the cohomological structure of the muon-mass identity
($\mathrm{Vol}(4_1)$ from the figure-eight knot, $\hbar_q^2$ as a
substrate object) is *too rigid* for $q_0$ to be a free parameter —
the equation has the shape of a structural constraint, not a
calibration. The owner accepted this framing and re-opened the
substrate-$q_0$ derivation as an in-scope research direction.

**Implication for the three-calibration discipline.** Re-opening
subgoal-2 does **not** retroactively invalidate CAL-2 — the
muon-mass identity remains the framework's current best
*observational* anchor for $q_0$. A successful derivation would
*upgrade* CAL-2 from a calibration to a derived consistency check
(predicted $q_0$ matches the muon-mass-implied $q_0$ to whatever
precision both sides support). Failure (or persistent absence of a
derivation) leaves CAL-2 intact.

---

## §2. What "derive $q_0$" means

A successful derivation produces a **categorical equation** or
**structural identity** whose unique real solution at $q > 1$ is
$q_0 \approx 1.10998$, where the equation is stated purely in terms
of QOU substrate data (Hecke / Wedderburn / Bring / motivic period
data) and consumes **no** physical input.

This is **NOT** a fit. The equation must be derivable from the
substrate axioms; the value $q_0$ then *falls out* as a root, rather
than being an input.

### Acceptance criteria (for any future submission)

A candidate $q_0$-derivation passes review iff **all four** of the
following hold:

| # | Criterion |
|---|---|
| **(a)** | The equation is stated as a `theorem` or `proposition` block with Lean formalization (per CLAUDE.md §3 — `theorem` kind requires sibling `.lean`). |
| **(b)** | The unique real solution at $q > 1$ is $q_0$, verified to ≥ 30 dps against `q_parameter.Q_50_DIGIT_STR`. |
| **(c)** | The formula does **NOT** consume CODATA $m_\mu / m_e$ (or any other physical input) as an input. All inputs are categorical / cohomological structural data. |
| **(d)** | The derivation passes `local/one-voice-audit` + `local/canonical-derivation-discipline` review. |

Note: criterion (b) is necessary but **not sufficient**. Matching
$q_0$ numerically to 6 ppb does not prove an equation derives $q_0$
structurally — see §6 anti-pattern 3.

---

## §3. Candidate paths

The following four candidate routes are enumerated as
**investigation directions**, not as blessed solutions. Each is a
multi-week scope. None has been validated; all are listed so future
sessions can pick a starting point with the option space visible.

For each path: a brief math description, the content blocks that
supply primitives, the gap to derivation, and a rough effort /
risk estimate.

### Path (a) — Spectral-collapse path

**Idea.** Pin $q_0$ as the unique value at which the Wenzl / Hecke
spectral sequence collapses at $E_2$ (or another distinguished
page). The framework already uses spectral-sequence collapse at $E_2$
as a structural fact at $q_0$ — the question is whether *uniqueness*
of the collapse point in $q$ can be extracted.

**Primitives from existing content.**

- [`prop:hecke-spectral-sequence`](../../content/quantum-observable-universe/braids-and-knots/hecke-spectral-sequence.md) — the spectral sequence on $H_n(q)$ arising from the Coxeter-length filtration.
- [`prop:spectral-sequence-collapse`](../../content/quantum-observable-universe/braids-and-knots/spectral-sequence-collapse.md) — collapse-at-$E_2$ statement.
- [`prop:gb-spectral-sequence`](../../content/quantum-observable-universe/braids-and-knots/gb-spectral-sequence.md) — GB-filtration version.

**Compute primitive.**
[`folio-assistant/computations/derivation_chain.py`](../../folio-assistant/computations/derivation_chain.py) — the GB-NF tracker, which records spectral-sequence page transitions.

**Gap.** No current uniqueness theorem for the $q$ at which collapse
holds. The existing propositions assert collapse *at* $q_0$
(downstream of CAL-2); they do not state collapse fails at other
$q$. A derivation here requires:

1. A precise statement of the collapse condition as an equation in
   $q$ (e.g., "differential $d_2$ vanishes iff $f(q) = 0$").
2. A uniqueness theorem: the equation has a single real root at
   $q > 1$.

**Effort:** weeks. **Risk:** the collapse may hold *generically* in
$q$ (i.e., at almost all values), in which case the structural
hypothesis does not pin $q_0$. Requires a non-generic obstruction
that selects $q_0$.

---

### Path (b) — K-theoretic / motivic-period path

**Idea.** Derive $q_0$ from a K-theory class fixed by the substrate
axioms, in the same world that gives $\mathrm{Vol}(4_1) = 2 \cdot
\Lambda(\pi/3)$ as a Bloch–Wigner motivic period. Since
$\mathrm{Vol}(4_1)$ is a pure cohomology object, and the CAL-2 identity
$m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^2$ pins $\hbar_q$ (and
hence $q_0$) against the muon mass, a parallel cohomology object
that pins $\hbar_q^2$ (or directly $q_0$) *without* the muon-mass
input would derive $q_0$.

**Primitives from existing content.**

- [`geom-yekutieli-alignment.md`](../../content/quantum-observable-universe/braids-and-knots/geom-yekutieli-alignment.md) — Geom-functor / Yekutieli alignment.
- [`prop:geom-universality`](../../content/quantum-observable-universe/braids-and-knots/geom-universality.md) — the canonical mass formula $m(K) = m_e \cdot \mathrm{Geom\_full}(K, q_0)$.
- [`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md) — Bring–Bloch identity for the linking-weight factor.

**Compute primitive.** Motivic-period machinery (Bloch–Wigner
dilogarithm, Borel regulator). No single canonical script yet;
infrastructure would need to be assembled from existing
$\mathrm{Vol}(4_1)$ computations.

**Gap.** Identifying the specific K-class that pins $q_0$. Candidate
sub-routes (each itself research-grade):

- A second motivic period (analogous to $\mathrm{Vol}(4_1)$) that
  algebraically determines $\hbar_q^2$ via a substrate-only equation.
- A Borel-regulator argument selecting a unique $q$ from the K-theory
  spectrum.
- A Bloch–Wigner identity that imposes a categorical constraint on
  $q$ (e.g., relating $D_2(q)$ at the substrate to a topological
  invariant).

**Effort:** months. **Risk:** the K-theoretic structure may not have
a natural class that pins $q_0$ uniquely; could end up with a family
parameter that itself needs calibration (re-introducing the same
problem one level up).

---

### Path (c) — Bring $\chi = -6$ path

**Idea.** Pin $q_0$ as the unique value fixed by the algebraic
K-class of the Bring surface $\Sigma_4$ (Euler characteristic
$\chi = -6$ condition). The framework already uses Bring $\chi = -6$
to fix the particle content at $H_3$ (6 = number of torus knots
embeddable in $\Sigma_4$); extending this to *also* pin the
substrate-$q$ value is a candidate route.

**Primitives from existing content.**

- [`prop:x5-bring-weight-identification`](../../content/quantum-observable-universe/braids-and-knots/x5-bring-weight-identification.md) — Bring weight identification.
- [`bring-zero-mode-bloch.md`](../../content/quantum-observable-universe/braids-and-knots/bring-zero-mode-bloch.md) — Bring zero-mode Bloch-class construction.

**Compute primitive.** `BringZeroModeBlochClass` (Lean class
introduced in the post-PR-#956 infrastructure). Currently the field
is `∃ z : ℝ, z = bringZeroModeValue`; the PR-#956 roadmap (cheat-sheet
§5 item 3) calls for strengthening to `∃ θ : ℝ, BlochWigner_unit_circle θ = bringZeroModeValue`, which would close a literal-rfl
loophole and exposes the Bloch–Wigner unit-circle structure.

**Gap.** Extending the BW unit-circle structure to pin $q_0$
algebraically. Specifically:

1. The Bloch–Wigner unit-circle class currently states existence of
   $\theta$ such that an identity holds — a derivation would need
   *uniqueness* of $\theta$ (or of the substrate $q$ such that
   $q$ maps to that $\theta$).
2. The mapping from $\theta$ (BW unit-circle angle) to $q$ (substrate
   parameter) is currently implicit; making it explicit may surface
   a constraint that pins $q_0$.

**Effort:** weeks to months. **Risk:** the Bring structure may pin
the *family* of substrates (the topological class of allowable $q$)
without selecting a unique numerical value — leaving $q_0$ as a
modulus of the family.

---

### Path (d) — Categorical-fixed-point path

**Idea.** Pin $q_0$ as the unique fixed point of a natural
endomorphism on $H_n(R, q)$ representation theory — for example, a
self-dual $q$ satisfying a bar-involution identity, or a $q$ at
which a specific natural transformation becomes the identity.

**Primitives from existing content.**

- [`prop:braid-action-tensor`](../../content/quantum-observable-universe/braids-and-knots/braid-action-tensor.md) — the braid action.
- [`def:categorical-action`](../../content/quantum-observable-universe/braids-and-knots/categorical-action.md) — categorical action infrastructure.
- [`prop:bar-involution`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.md) — bar-involution $q \mapsto q^{-1}$ on the Hecke algebra.

**Compute primitive.** Hecke endomorphism algebra (existing in
`hecke_core.py` and the symbolic Hoefsmit infrastructure).

**Gap.** Identifying the specific endomorphism + proving a
uniqueness statement for its fixed point at $q > 1$. Candidate
sub-routes:

- A natural transformation between two functors on $H_n(q)$
  representations that becomes the identity at $q_0$ (e.g., a
  Frobenius–Schur indicator collapse).
- A bar-involution self-duality constraint that algebraically pins
  $q$ (the bar-involution sends $q \mapsto q^{-1}$, so any self-dual
  object satisfies a $q = q^{-1}$ root-of-unity condition — but
  $q_0 > 1$ is *not* a root of unity, so the constraint must be
  more refined).
- A spectral-flow fixed point: $q_0$ is the $q$ at which a specific
  R-matrix eigenvalue equals a structural constant.

**Effort:** months. **Risk:** the categorical endomorphism algebra
is large; many natural transformations are constant in $q$ (giving
no constraint) and many are generic in $q$ (giving uncountably many
roots). Selecting the *right* endomorphism is itself the research
problem.

---

### Path (e) — Additional / unidentified routes

The four paths above are not exhaustive. Future sessions may
identify additional candidate routes by reading
[`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
and the substrate-side propositions ($\rho_n$, $\mathrm{tr}_M$, Wenzl
$y_\lambda$, the Frobenius pairing, etc.) for places where a $q$-
parametrised structural condition might fix $q_0$ algebraically.

Two flagged-but-not-detailed directions noted during scaffolding:

- **Confinement-SDP variational route** — the framework's
  confinement SDP ([`prop:confinement-sdp`](../../content/quantum-observable-universe/braids-and-knots/confinement-sdp.md))
  selects canonical $T_w$ at $q_0$. A variational principle over $q$
  (e.g., a structural Lagrangian whose stationary point is $q_0$)
  is conceivable but completely unscoped.
- **Yekutieli-MI minimisation** — the non-abelian Stokes derivation
  ([`prop:hecke-spectral-sequence`](../../content/quantum-observable-universe/braids-and-knots/hecke-spectral-sequence.md))
  involves a multiplicative integration; a variational characterisation
  of $q_0$ in terms of MI-stability is conceivable but unscoped.

Either of these would, if developed, become a new path (f), (g),
etc. in a future revision of this workplan. Do not start them in the
first session — they are listed only so the option space is on the
record.

---

## §4. Candidate-paths summary table

| Path | Status | Key content blocks | Primary risk | Est. effort |
|---|---|---|---|---|
| **(a) Spectral-collapse** | sketch | `prop:hecke-spectral-sequence`, `prop:spectral-sequence-collapse`, `prop:gb-spectral-sequence` | collapse holds generically → no constraint on $q$ | weeks |
| **(b) K-theoretic / motivic-period** | blocked-on identifying the K-class | `geom-yekutieli-alignment`, `prop:geom-universality`, `prop:lambda-scale-bring-bloch-identity` | no natural class uniquely pins $q_0$; family parameter regress | months |
| **(c) Bring $\chi = -6$** | first-step (strengthen `BringZeroModeBlochClass`) | `prop:x5-bring-weight-identification`, `bring-zero-mode-bloch.md` | Bring pins family / topological class, not numerical $q_0$ | weeks–months |
| **(d) Categorical fixed-point** | sketch | `prop:braid-action-tensor`, `def:categorical-action`, `prop:bar-involution` | selecting the right endomorphism is itself the research problem | months |
| **(e) Additional / unidentified** | not started | (see §3(e)) | scope unbounded | — |

---

## §5. Acceptance criteria (verbatim)

Repeating from §2 for visibility. A candidate $q_0$-derivation passes
review iff **all four** hold:

| # | Criterion |
|---|---|
| **(a)** | The equation is stated as a `theorem` or `proposition` block with Lean formalization (per CLAUDE.md §3 — `theorem` kind requires sibling `.lean`). |
| **(b)** | The unique real solution at $q > 1$ is $q_0$, verified to ≥ 30 dps against `q_parameter.Q_50_DIGIT_STR`. |
| **(c)** | The formula does **NOT** consume CODATA $m_\mu / m_e$ (or any other physical input) as an input. All inputs are categorical / cohomological structural data. |
| **(d)** | The derivation passes `local/one-voice-audit` + `local/canonical-derivation-discipline` review. |

---

## §6. Anti-patterns to avoid

These are explicit guardrails. The substrate-$q_0$ derivation is a
related-but-distinct problem from the $\Delta_\lambda$ closure
problem (CLAUDE.md "Precision goals" § Δ_λ gate), but it inherits
the same epistemic discipline: **structural identity, not fit.**

### Anti-pattern 1 — A 7th-style fit-based ansatz

The $\Delta_\lambda$ closure problem has six failed closure ansätze
(Frobenius co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius,
crystal-graph, augmented Markov), and CLAUDE.md states "do not
propose a seventh fit-based ansatz." The substrate-$q_0$ problem
is distinct in mathematical content, but the same anti-pattern
applies: **do not enumerate fit-based candidate formulae and check
which match $q_0$ numerically.** The route to a derivation is
*structural* (identify the categorical constraint that pins $q_0$),
not enumerative (try formulae until one matches).

### Anti-pattern 2 — Back-fitting CODATA in disguise

A formula that "happens to have $q_0$ as its solution" but whose
*choice* was guided by knowing $q_0 \approx 1.10998$ in advance is a
back-fit, not a derivation. Examples of disguised back-fits:

- Picking a function $f$ from a parameterised family because $f(q)
  = 0$ at $q \approx 1.10998$.
- Inserting structural data (a specific knot, a specific partition,
  a specific Wedderburn block) chosen because it produces the right
  numerical answer.
- Using an "obvious" categorical object whose obviousness is in fact
  retrospective — i.e., the object only seems natural *because* its
  associated equation has $q_0$ as a root.

**Test for back-fit.** Could the same derivation strategy be applied
*before* knowing $q_0$ — i.e., would the substrate axioms alone
single out the same equation? If not, it is a back-fit.

### Anti-pattern 3 — Conflating "matches to 6 ppb" with "uniquely fixed"

Numerical match alone is *necessary* but **not sufficient**. The
historical record contains many "$X$ matches at $q_0$ to $N$ ppb"
findings that turned out to be jet-mixing coincidences (PR #1126
W = √[2]_q retraction, PR #842 / PR #854 falsifying Phase 5g and
5k.1, etc.). A successful derivation requires:

1. The equation matches $q_0$ to the expected precision (necessary).
2. **And** the equation is derivable from substrate axioms
   (necessary — rules out numerical coincidences).
3. **And** uniqueness: the equation has $q_0$ as its unique real
   root at $q > 1$ (necessary — rules out trivial / generic
   identities).

The canonical-watcher framework (PR #1228, Slot J in
[`canonical-watcher.md`](../../.claude/skills/local/canonical-watcher.md))
enforces this triple-check (GB filtration + jet order +
bar-symmetry) on probe follow-up. Any submission claiming
$q_0$-derivation must pass this discipline.

### Anti-pattern 4 — Claiming $q_0$ as a fundamental constant prematurely

Until a derivation is **fully Lean-verified** *and* has passed
`local/canonical-derivation-discipline` review, do **not** claim
$q_0$ is a fundamental constant of nature derived by the QOU
framework. The framework's current honest statement is: $q_0$ is
*pinned by CAL-2* (the muon-mass identity) and *consistent with*
substrate cohomology (the $\mathrm{Vol}(4_1)$ closure). A derivation
upgrades this to "predicted from substrate cohomology"; without the
Lean + review pass, the claim is premature.

---

## §7. First-session plan (next agent)

The first follow-up session should perform a **bounded inventory
task only**, not a derivation attempt.

### Task

Audit the existing spectral-collapse / Wenzl-trace uniqueness
criteria in:

- [`folio-assistant/computations/derivation_chain.py`](../../folio-assistant/computations/derivation_chain.py)
  (GB-NF tracker; spectral-sequence page transitions)
- [`folio-assistant/computations/y_lambda_wenzl_bridge.py`](../../folio-assistant/computations/y_lambda_wenzl_bridge.py)
  (Wenzl $y_\lambda$ closed forms)
- [`folio-assistant/computations/hecke_core.py`](../../folio-assistant/computations/hecke_core.py)
  (canonical $\sigma_i$ matrices + Hecke quadratic verification)

Identify which (if any) collapse / uniqueness conditions are
**closest** to being a constraint that uniquely pins $q$.
Specifically:

- Does any current code path have a structural condition that holds
  at $q_0$ and fails at, e.g., $q = 1$ or $q = 2$?
- Are there spectral-sequence differentials computed symbolically in
  $q$ whose vanishing condition can be extracted as an equation?
- Are there Wenzl $y_\lambda$ identities that hold non-trivially as
  equations in $q$ rather than as definitions?

### Deliverable

An **inventory report** (audit doc under
`docs/audits/<date>-substrate-q0-inventory-spectral-wenzl.md`)
listing every candidate uniqueness condition found, with:

- The script + line range where the condition is computed.
- Whether the condition is currently stated as an identity, a
  definition, or an empirical match.
- A first assessment: is this a candidate for §3 path (a) (spectral
  collapse), or does it belong to a different path / no path?

### Hard constraints on the first session

- **No new derivation attempt** — inventory only.
- **No new compute scripts** — read existing scripts.
- **No modifications** to content blocks, compute scripts, or Lean
  files.
- The inventory report is the sole deliverable; the next session
  uses the report to scope the actual derivation work.

---

## §8. Cross-references

### Driver PRs / audits

| Ref | Topic |
|---|---|
| PR [#1246](https://github.com/litlfred/qou/pull/1246) | CAL-2 cohomological-vs-calibration critique (owner reversal driver) |
| Audit [`2026-05-25-cal-2-cohomological-vs-calibration-critique.md`](../audits/2026-05-25-cal-2-cohomological-vs-calibration-critique.md) | CAL-2 critique companion audit (branch `claude/busy-lamport-5NS40`) |

### Sibling PRs (related ongoing work)

| Ref | Topic |
|---|---|
| PR [#1127](https://github.com/litlfred/qou/pull/1127) | $Q_\beta$ net-ansatz fitting finding (anti-pattern reference for §6) |
| PR [#1228](https://github.com/litlfred/qou/pull/1228) | geom-derivation KLR path (related substrate-side derivation methodology) |
| PR [#1224](https://github.com/litlfred/qou/pull/1224) | $\Delta_\lambda$ closure synthesis (sibling closure problem with anti-pattern history) |

### Prior unsuccessful substrate-derivation attempts (background only — do not extend)

| Audit | Attempted route | Outcome |
|---|---|---|
| [`2026-05-15-a-minus-2-q-substrate-derivation.md`](../audits/2026-05-15-a-minus-2-q-substrate-derivation.md) | KLR / Markov-trace candidate for $[A-2]_q$ | research-grade scaffold, not closed |
| [`2026-05-17-delta-coupling-substrate-derivation.md`](../audits/2026-05-17-delta-coupling-substrate-derivation.md) | $\Delta$-coupling substrate route | not closed |
| [`2026-05-17-m-n-substrate-investigation-and-lit-search.md`](../audits/2026-05-17-m-n-substrate-investigation-and-lit-search.md) | $m_n$ via Picard–Lefschetz | PL prescription found to be non-standard / back-fit |

These are listed as **historical context only**. The current
workplan does not propose to extend any of them; each was a
substrate-side derivation attempt with a different target (per-
isotope coupling, per-mass quantity) than the CAL-2 substrate-$q_0$
target of this workplan. They are cited so the next agent does not
re-tread the same paths without recognising the precedents.

### Authoritative reference docs

| Doc | Section relevant to this workplan |
|---|---|
| [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) | §1 (chain), §5 (open work — `Geom_full` refinement parallels), §8 (three-calibration discipline) |
| [`docs/precision-goals.md`](../precision-goals.md) | L1 / L2 / subgoal-1 / subgoal-2 framing |
| [`CLAUDE.md`](../../CLAUDE.md) | "Precision goals" § subgoal-2 declination (the rule this workplan re-opens); §3 Lean requirements for `theorem` blocks (acceptance criterion (a)) |
| [`.claude/skills/local/canonical-watcher.md`](../../.claude/skills/local/canonical-watcher.md) | Slot J probe follow-up discipline (anti-pattern 3 triple-check) |

---

*This workplan is a scaffold. No derivation is attempted in this
session; the deliverable is this doc + the draft PR registering the
research direction. The first-session inventory task (§7) is the
sole bounded next action.*
