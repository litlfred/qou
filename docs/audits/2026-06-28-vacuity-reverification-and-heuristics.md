# Vacuity re-verification + heuristic upgrade (2026-06-28)

Follow-up to `2026-06-28-vacuity-fix-complete.md` (the 95-genuine fix). The owner
asked to (1) **re-verify the 64 "legit / no-fix" bucket** with full agent
inspection — because `q_gl_obstruction_calc` had shown the heuristic triage can
mislabel a real defect "legit"; (2) **fix the heuristics** so the machine catches
what the triage missed and add **agent inspection, not just machine**; (3) fix
everything fixable.

## 1. Re-verification of the 64 — an 8-agent swarm

Each of the 64 remaining flags got a full agent inspection (file-disjoint
clusters). The triage's "legit" verdict was **wrong on 32 of them** — they were
genuine vacuity defects, now fixed (Pattern A/B/C, each `lake env lean` exit 0
before the cache broke; see §3):

| cluster | genuine fixed | advisory fixed (native_decide→decide) | legit confirmed |
|---|--:|--:|--:|
| 1 (mass-theory) | 11 | 0 | 3 |
| 2 (particle-interactions) | 8 | 6 | 0 |
| 3 (predicted-spectra + HoefsmitBridge) | 4 | 1 | 1 |
| 4 (climax/organic) | 0 | 6 | 0 |
| 5 (batch) | — | — | — |
| 6 (fluid-dynamics + Archimedean) | 2 | 0 | 4 |
| 7 (information-theory + BraidKnot) | 2 (partial) | — | — |
| 8 (mass-endomorphism + braids) | 3 | 1 | 2 |

**≥32 genuine defects the triage had mis-called "legit"** — including the
clearest case, `meson_scale_independence`, whose own `.md` admitted the Lean
"defers via sorry" while it actually shipped a physics-free tautology (a
degenerate `m_e = q_0 = 0` witness). The confirmed-legit remainder are honest
negative results (`zero_not_isAlgebraicallyPrime`, `reebCasimir_not_injective`,
the PSD spectral proof) whose "false premise" is a discharged impossible
*sub-case*, not vacuity. Many fixed files additionally had **pre-existing
standalone-compile breakage** (stale Mathlib imports, unclosed sections,
dangling docstrings) repaired so they verify.

## 2. Heuristic upgrade (machine layer) — `lean-vacuity-axiom-audit.ts`

- **`true-class-field`** (new, `proof-claims-unencoded`): a `class`/`structure`
  field typed literally `: True` carries zero content — the field-level analogue
  of a `: True` conclusion, which the empty-carrier (zero-field) and
  claims-unencoded (≥2 bullets) detectors both structurally missed. Honest
  opaque-marker fields (`@marker` / `opaque marker` in the field doc) are
  **exempt-but-tracked**. Surfaced **36** genuine un-annotated `: True` carriers
  tree-wide (16 honest markers exempted) — a previously-invisible tranche,
  e.g. `confinement-categorical` `hh_vanish : True` and the `Conjectures/*`
  carriers whose trivial `instance` "closes" an open conjecture.
- **trivial-true escalation**: a `placeholder-true` / `def-disguised-true`
  whose docstring asserts a provable claim (`**Theorem**`/`**Lemma**`/
  `**Proposition**`) and is not a conjecture carrier is annotated
  *"docstring asserts a provable claim while the Lean concludes `True`"* — the
  exact `q_gl_obstruction_calc` failure mode the triage kept missing.

## 3. Agent inspection made mandatory — the review ledger

Standalone library `.lean` files have no `<block>.qa.json` sidecar, so an agent
verdict had nowhere durable to live and a one-off triage doc could silently
mis-call a candidate. New mechanism (`content/pipeline/lean-vacuity-axiom-audit.ts`):

- **`--review-ledger`** seeds/refreshes
  [`docs/audits/lean-vacuity-review-ledger.json`](lean-vacuity-review-ledger.json)
  (`lean-vacuity-review/v1`): keyed by `<relpath>::<decl>::<category>`, recording
  the agent `verdict` + the `.lean` sha at review time.
- **`--check-ledger`** exits 1 unless every non-exempt candidate carries a
  **fresh** agent verdict (sha still matching). A verdict goes stale the moment
  the file changes — the machine can flag, only an agent can clear.

Current ledger: **45** candidates — **7 `legit`** (the agent-confirmed honest
negatives) + **38 `needs-agent`** (the 36 true-field tranche + 2 cache-blocked
cluster-7 leftovers).

## 4. What is NOT done this session — and why

Compile-verification went **hard-blocked** mid-session: a swarm agent's stray
`lake build` dropped `Mathlib/Tactic/Omega` (olean **and** source), there is no
`lake-cache/qou-v4-24-0` orphan branch to restore from, and the source clone is
incomplete. Per AGENTS.md's STRICT routing this is a genuine hard block → the two
kept cluster-7 edits are **hand-audited, not compile-verified** (noted in the
commit), and the risky cluster-7 edit (`q-heat-kernel-peter-weyl`, unbalanced
`end`) was reverted rather than shipped unverified.

The **38 `needs-agent`** candidates (true-field tranche + cluster-7 leftovers)
are therefore deferred to bean **`vtf0`** — they need a working Lean cache so an
agent can fix-and-verify rather than ship unverifiable edits. The ledger is the
work queue; `--check-ledger` is the gate.

## 5. Tranche-2 update — the true-field tranche fixed (supersedes §4)

§4 above said verification was "cache-blocked" and the 38 `needs-agent`
candidates were deferred. **Both turned out wrong/now-resolved:**

- **Verification was never blocked** — the on-disk Mathlib cache is intact
  (3099 oleans; `lake env lean <file>` works). The scare was a single file's
  bad `import Mathlib.Tactic.Omega` (no such module at the pinned rev; `omega`
  is a Lean *core* tactic), fixed alongside `composite-crossing-parity.lean`'s
  other never-compiled breakage (false constant `helium 56→54`; two nonlinear
  `omega` core proofs genuinely proved).
- **A 7-agent tranche-2 swarm fixed the tranche**, every edit `lake env lean`
  exit 0. Full-tree audit fell **64 → 10** candidates:
  - **34/36** `true-class-field` carriers resolved — `: True` fields replaced
    with the real claim-shaped content (mass-defect factorisations, quantum-torus
    `uv = q·vu`, Bloch-Wigner regulators, Cl₂ pentagon, sign-rep antisymmetry,
    the `Conjectures/*` carriers whose fabricated trivial `instance` was removed,
    …), or honest `opaque marker` annotations where Mathlib lacks the infra
    (Bloch group, Kashiwara crystal, Iwahori–Hecke trace).
  - **8 `legit`** (recorded in the ledger with agent evidence): 7 honest-negative
    false-premise proofs + `KauffmanTL3.borromean_crossing_minimal`
    (`native_decide` kept — `decide` times out at 590s on ~1365 Jones-bracket
    computations; documented axioms + Python oracle).
  - **2 `needs-agent`** remain — the `brings-surface/orbital-*` `BorromeanQuark`
    carriers, blocked by **pre-existing, vacuity-unrelated** file breakage
    (zero/broken imports, orphaned proof bodies). Deferred (not shipped
    unverified) to bean `vtf0`; the ledger gate stays red on exactly these two,
    which is accurate.

Several files additionally had pre-existing standalone-compile breakage repaired
in passing (removed-in-Lean4 `constant`, renamed Mathlib lemmas, over-purged
decl bodies, markdown-as-code) so the changed files verify.
