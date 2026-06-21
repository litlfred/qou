# Next-agent orientation — 2026-05-20

You are inheriting an active QOU session. The previous session just merged
**PR #863** (Phase 5l + 5l.1 + 5q: constit-factor structural identity +
closed-form tr_M) at commit `2f7eabe1e`. This document orients you for
the work queued behind that merge.

Read this whole document before doing anything substantive. The
authoritative pointers all live elsewhere in the repo — this file is the
**map**, not the territory.

---

## 1. Where you are, in one paragraph

The QOU framework derives every observable (proton/neutron masses, atomic
binding energies, β-decay Q-values, hadron lifetimes) from **three
calibration inputs** (`m_e`, `m_μ/m_e`, `Q_β`) via a strict categorical
chain: substrate `q₀ → 𝐂 categorical action → Yekutieli non-abelian
Stokes → 𝐇_n(q) Hecke → Wedderburn decomposition → Frobenius pairing
tr_M = Σ_λ y_λ χ_λ → confinement SDP → canonical T_w → Archimedean
functor → MeV observables`. The just-merged PR closed a 70-day open
question (the "constit factor") by identifying that
`ρ_Z^constit(q) = tr_M^3(𝓑_p, q)` exactly via Wenzl 1988 §1.7 disjoint
Markov-trace multiplicativity. Together with the prior Phase 5c.1
interface-knot identity, the FULL `tr_M(𝓑_K)` of any canonical atomic
braid now has a closed form that bypasses the H_{3A} character sum —
a 22.7-million-× speedup at ⁴He.

---

## 2. Read these documents in this exact order

Do **not** skim. Each one assumes the prior reads landed.

| Order | File | Why |
|---|---|---|
| 1 | [`AGENTS.md`](../../AGENTS.md) | Repo-wide agent policy: user accessibility, work-plan rules, notation/Lean discipline, protected files. Mandatory. |
| 2 | [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) | The "one-page-up" map of the derivation chain with per-step math, paper refs, canonical compute scripts, and the Phase 5 findings table (5b through 5q). **Read this before touching any math-affecting code.** |
| 3 | [`docs/precision-goals.md`](../precision-goals.md) | The L1/L2 precision-leg distinction. Don't conflate "1 ppb compute" with "100× experimental" — they're independent. |
| 4 | [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](../audits/2026-05-18-delta-lambda-gating-context.md) | The Δ_λ Track-A blocker: six ansätze have failed on deuteron binding. Do **not** propose a seventh fit. Productive directions are GAP-A-3, GAP-A-4, or Option E (Kashiwara crystal). |
| 5 | [`content/quantum-observable-universe/notation/notation-register.md`](../../content/quantum-observable-universe/notation/notation-register.md) + [`notation-collisions.md`](../../content/quantum-observable-universe/notation/notation-collisions.md) | Symbol register. AGENTS.md no longer mirrors per-chapter tables (drifted in Phase 5n) — these are the single source of truth. |
| 6 | [`docs/coordination/1ppb-categorical-chain.md`](../coordination/1ppb-categorical-chain.md) | Coordination ledger — append a row when you start substantive work. |
| 7 | The pre-merge commit log: `git log --oneline 2f7eabe1e~20..2f7eabe1e` | Walk the merged content; the 18 commits trace Phase 5l → 5l.1 → 5k.2 → 5l.2 → 5o → 5q. |

---

## 3. What the merged PR delivered (the facts you can build on)

### 3.1 New mathematical results (use freely)

1. **Phase 5l structural identity** — for any canonical atomic braid `𝓑_K`
   with constituent-vacuum factor `𝓑_K^vac = 𝓑_p^⊗Z ⊗ 𝓑_n^⊗N`:
   ```
       tr_M(𝓑_K^vac) = tr_M^3(𝓑_p, q)^Z · tr_M^3(𝓑_n, q)^N
   ```
   Verified at mpfr-50-dps across 5 q-values in the substrate window.
   See [`prop:constit-factor-tau-M-proton-identity`](../../content/quantum-observable-universe/braids-and-knots/constit-factor-tau-M-proton-identity.md)
   (Lean `pow_succ + field_simp + ring`, sorry-free; the only axiom is
   the §3b-cond `MarkovTraceDisjoint` class which encodes Wenzl §1.7
   disjoint multiplicativity).

2. **Combined closed form (Phase 5c.1 + 5l)** — for the FULL canonical
   atomic braid:
   ```
       tr_M(𝓑_K) = tr_M^3(𝓑_p)^Z · tr_M^3(𝓑_n)^N · ∏_i f_i(q)
   ```
   where each interface contributes `f_i ∈ {z(q), z(q) - h(q)}` for
   positive (p-p, p-n) / negative (n-n) crossings. Verified at
   mpfr-50-dps for D, T, ³He, ⁴He (max rel.err 1.09×10⁻⁴⁹).

3. **Phase 5g and 5k.1 globally falsified** — the `(2q - 1)` form and
   the `h^5` residual coefficient `c ≈ 1` were both shown to be
   numerical coincidences at `q₀ ≈ 1.10998`. Do not revisit them as
   identities; they're rec'd in the conjecture file with FALSIFIED
   banners.

### 3.2 New shared utilities (import these, do not duplicate)

| Module | Purpose | When to use |
|---|---|---|
| [`computations/closed_form_tau_M.py`](../../computations/closed_form_tau_M.py) | Closed-form `tr_M(𝓑_K)` from H_3 building blocks | Anywhere you'd otherwise call `chi_lambda_braid` over `partitions_of(3A)` to compute the scalar `tr_M`. 22.7M× faster at ⁴He. |
| [`computations/canonical_braid_marshalling.py`](../../computations/canonical_braid_marshalling.py) | Centralised `(c, d, gen) → (sign, gen)` and `→ (gen, cross_type)` marshalling | Whenever you marshal an `atom_braid_word_3A` output for `chi_lambda_braid` or `q_character_on_braid_word`. **Do not re-implement** — Copilot will flag inline marshalling. |

### 3.3 New documentation surfaces

- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md):
  the single page that orients math-affecting work. Updated whenever a
  Phase finding lands. §5 holds the pipeline-discipline migration backlog.
- [`notation-collisions.md` §"Archimedean / fibre / forgetful functors"](../../content/quantum-observable-universe/notation/notation-collisions.md):
  Phase 5o disambiguation note — three functors that were getting
  conflated in chat / commits.

---

## 4. What is **open** (your queue, in priority order)

### 4.1 Owner-direction items (highest priority)

1. **Bring color-tube weighted averaging at the p-n interface (open R&D).**
   The owner flagged in the prior session: "there's an averaging that
   should be using the Bring color tube weighted averaging to make sure
   it's correct." The current p-n convention (`(c=1, d=-h/2)` in
   `atom_braid_word_3A`) is the uniform bar-invariant projection
   `σ_avg = (σ + σ^{-1})/2 = σ - h/2·I`. The owner's intuition is that
   it should reflect the 3-color-tube structure (proton uud / neutron udd)
   weighted by quark mass. Empirical evidence in
   [`probe_pn_flavor_asymmetry.py`](../../computations/probe_pn_flavor_asymmetry.py)
   and [`probe_per_sheet_flavor_nonin.py`](../../computations/probe_per_sheet_flavor_nonin.py):
   the sum-weighted scheme reproduces Δm_{n-p} to ~0.14% of CODATA.
   **Status: queued.** `closed_form_tau_M.py` exposes
   `pn_convention="bring_color_weighted"` as a placeholder that raises
   `NotImplementedError` with the queue context.

   **What's missing to close it:**
   - Define the canonical color-sheet ↔ quark-flavor mapping (the
     probe's conclusion: "research-level, not explicitly stated in the
     paper").
   - Extend `closed_form_tau_M.py` to accept quark-mass inputs (μ_u, μ_d)
     and apply the 9-way color-pair-weighted average.
   - Decide whether this lives at the substrate H_{3A} level (algebraic,
     no quark mass) or the mass step (downstream, quark-mass-aware).

2. **Phase 5l.2 normalization reconciliation (open).** Phase 5l.1
   produces a symbolic `T(B_p, q)` from Wenzl-bridge SYMBOLIC y_λ that
   does **NOT** match Phase 5l's mpfr-50-dps `tr_M^3(𝓑_p, q)` by any
   simple multiplicative constant. Both Hyp A (T at q, spread 5.9e-2)
   and Hyp B (T at q², spread 81%) were refuted by the probe. The
   Wenzl-bridge symbolic implementation uses a deeper convention
   mismatch (likely a partition-structure-dependent y_λ normalization).
   See [`normalization-reconciliation-phase5l2.witness.json`](../../computations/normalization-reconciliation-phase5l2.witness.json).

### 4.2 Pipeline-discipline migration backlog (cheat sheet §5)

Five actions are queued. Each is a discrete, mechanical migration —
the math is settled, only the wiring needs catching up.

| # | Action | Where | Why |
|---|---|---|---|
| 1 | Replace `LAMBDA_PROTON_DOC` / `LAMBDA_NEUTRON_DOC` literals with `prop:lambda-scale-bring-bloch-identity` derivation | `m_p_borromean_verification_50dps.py` | 3-calibration discipline violation |
| 2 | Migrate 20 importers of SUPERSEDED `mass_endomorphism.py` to `mass_tower_operator_valued` | 20 scripts incl. `build_proton_mass_50dps_chain.py`, `mass_at_3A_proper.py` | SUPERSEDED dep in production |
| 3 | Wire Rust LR convention adapter (PR #829) into `atomic_tr_m_*` scripts for A ≥ 3 | `atomic_tr_m_helium4.py`, `atomic_tr_m_mpfr_50dps.py` + 6 mass scripts | ~500× speedup at ⁴He, ~10⁶× at ¹⁰B available, untaken |
| 4 | **PARTIALLY DONE.** Refactor 4 production tr_M scripts to use closed form | `atomic_chirality_residue.py`, `atom_level_wedderburn_tower.py`, `binding_canonical.py`, `binding_depth_stratified*.py` | Closed form is verified (Phase 5q witness); migration not yet applied to these 4 |
| 5 | Add compute verification for Reeb-flow / Garside closed-form (4 paper-only commits) | new script needed | substrate-side derivation unverified |

**Recommendation**: take Gap #4 first — the closed form is verified, the
4 scripts are named, and the migration pattern is the closed-form sanity
check shown in `closed_form_tau_M_verification_phase5q.py`. Each script
adds a `closed_form_tau_M` call + assertion comparing to the empirical
sum. Probably 1-2 hours per script.

### 4.3 Deferred (out of session scope unless owner reverses)

- **Phase 5m** — full Wenzl 1988 §1.7 Lean formalization replacing the
  §3b-cond `MarkovTraceDisjoint` class axiom with a proved theorem.
  ~1-3 weeks focused; queued.
- **Phase 5p** — Geom ↔ tr_M unification check (downstream `ω` stage of
  the Hoefsmit scattering pipeline). Depends on Phase 5q being live in
  mass-table compute, which is Gap #4.
- **Subgoal-2 of L2** — 100× targets below the CAL-2 floor for absolute
  `m_p`, `m_n`, `m_⁴He`. The coordination ledger declined this on
  2026-05-08 (requires substrate-derivation of `q₀`). Do **not** start
  without owner reversal.

---

## 5. The non-obvious rules (you will trip on these)

### 5.1 Three-calibration discipline (AGENTS.md §Precision goals)

Only `m_e`, `m_μ/m_e`, `Q_β` may be calibrated. Everything else MUST
derive from these three via the chain. The Δ_λ gate already broke six
ansätze; do not write a seventh. If you find yourself fitting parameters
to experimental data, **stop** — the canonical-watcher integration
review will catch it and you will be asked to revert.

### 5.2 §3b-cond conditional-class exception (AGENTS.md §3b)

A `theorem`/`proposition` whose `uses[]` cone touches a `conj:`
cannot stay provable **unless** all four conditions hold: (a) the
conjecture is a Lean `class`, (b) the downstream Lean has the class as
an explicit `[Instance]` hypothesis, (c) the `.md` opens with the
**Theorem (conditional on conj:C).** banner, (d) `uses[]` lists the
conjecture explicitly. The Phase 5l proposition uses this pattern;
copy it when adding new conditional results.

### 5.3 §7c base-ring convention

Lean declarations that hold in a generic ring must use `{R : Type*}`
with the weakest typeclass that admits the construction. Only specialise
to `ℝ` past the archimedean wall (when `Real.sqrt`, ordering, CODATA
numerics, etc. are genuinely needed). The Phase 5l proposition uses
`[Field R]`; new structural theorems should too.

### 5.4 Notation register conventions (post-Phase 5n)

- Markov trace: `\mathrm{tr}_M` (NOT `\tau_M`)
- Atomic braid word: `\mathcal{B}_K` (NOT `\beta_K`)
- Interface knot: `\bowtie_K` (NOT `\Delta_I^K`)
- Energies: `\mathfrak{E}` family (NOT `\mathbf{E}`)
- Info bandwidth: `\mathfrak{B}(q)` (NOT `\mathcal{B}(q)`)

When in doubt, open `notation-register.md` — do NOT trust your training-
data memory of the older names.

### 5.5 The chi_lambda_braid p-n convention (Phase 5q finding)

`chi_lambda_braid` only takes `(sign, gen)` pairs. The marshalling layer
(`canonical_braid_marshalling.marshal_to_chi_lambda_braid`) silently
maps the canonical averaged p-n form `(c=1, d=-h/2)` to `(sign=+1, gen)`
— the "averaged → σ convention". This means production `tr_M` values
use a SIMPLIFIED p-n convention (`f_pn = z`, not `z - h/2`). The
closed_form_tau_M default matches this; the strict-averaged
(`z - h/2`) variant is an opt-in.

If you find yourself debugging a 21% rel.err on a tr_M comparison,
this is almost certainly the convention mismatch.

### 5.6 Witness drift on rebase

`computations/*.witness.json` files drift on rebase
(`computedAt`, `commitSha`, `durationMs`, `files_scanned` change between
runs). The `/prepare-merge` skill auto-resolves this. Don't try to
hand-merge witness JSONs — re-run the four self-emitting validators
(`compute_audit_scan`, `derivation_chain_validator`,
`cross_check_trM_1ppb --strict`, `e0_calibration_audit --strict`) and
commit their fresh output.

### 5.7 Long-compute logging discipline (Gemini will flag this)

Any script expected to run > 5 minutes must emit periodic progress lines
with `units/sec`, `elapsed`, and `ETA`. The Phase 5q script is the
template — see `compute_tau_M_full()` for the pattern. The ⁴He
computation takes ~28 min; without the progress lines you can't tell if
it's making progress or hung.

### 5.8 PR-review-comment lifecycle

Gemini and Copilot will run on every PR. Triage protocol per
[`local/coordinate`](../../.claude/skills/local/coordinate.md):
- Trivial fix (rename, doc correction, raise-instead-of-fallback)
  → apply immediately
- Architectural change → escalate via `AskUserQuestion`
- Inconsistent findings between reviewers → escalate (don't pick one
  silently)
- Reviewer says X but you have evidence Y is correct → document the §6
  escalation reasoning in a code comment AND reply on the thread

---

## 6. How to start your first task

1. Read documents 1-3 from §2.
2. Run `git log --oneline -20` and skim the recent merges.
3. Decide which queue item to work — recommendation: Gap #4 from §4.2,
   one of the four production tr_M scripts (`atom_level_wedderburn_tower.py`
   is the simplest entry point because it already separates the
   per-partition Φ_q sum from the descended Markov trace).
4. Create a branch following the pattern: `claude/<theme>-<utc-ymd>`.
   For Gap #4: `claude/gap-4-tr-m-migration-2026-05-21` (or whatever
   today's date is).
5. Coordinate by posting an intent comment on any sibling PR touching
   the same scripts (per the AGENTS.md "Coordinate intent with sibling
   branches" rule).
6. Do the work. When ready, run `/prepare-merge` to set up review.

---

## 7. Tools you should know about

| Tool | When |
|---|---|
| `/prepare-merge` | Before requesting reviews on any PR — runs rebase + lean-ref migration + validate + remark-audit + one-voice + Lean audit + force-push |
| `/integration-watch <axis>` | Run the proof / canonical / compute / detangler integration watchers; one or all in parallel |
| `/coordinate` | When working alongside other in-flight PRs (sibling intent comments, cherry-picks, periodic triage) |
| `/integration-backlog` | Drain the integration-watcher backlog into reviewable PRs |
| `local/proof-gap-audit` (skill) | Before promoting a conjecture to a theorem — check the conditional-propagation chain |
| `local/witnessed-values` (skill) | Anywhere you have a numerical literal that should derive from witness data |
| MCP `lean_*` tools (when Lean is installed) | Lean diagnostics, goal state, search Mathlib, try tactics |

---

## 8. What NOT to do

- Do not edit `deploy/google-viewers.txt`, `deploy/github-collaborators.txt`,
  or `.github/CODEOWNERS` — protected, owner-only.
- Do not propose a 7th Δ_λ closure ansatz. The canonical-watcher will
  reject it.
- Do not introduce a 4th calibration parameter. Three only: `m_e`,
  `m_μ/m_e`, `Q_β`.
- Do not use `Φ_q` (Faddeev) in a binding-context script — use
  `Li_2^q` (Rogers / Kashaev). See cheat sheet §4 for the context-sort
  table.
- Do not write a new symbol convention without updating
  `notation-register.md` (the canonical source). AGENTS.md no longer
  mirrors the per-chapter tables.
- Do not re-implement `(c, d, gen) → (sign, gen)` marshalling inline;
  use `canonical_braid_marshalling`. Copilot will flag inline copies.
- Do not silently fall through on unknown `(c, d)` in any marshalling
  function — raise `ValueError`. (Fixed in #863; do not regress.)
- Do not hardcode an empirical value in a print or comment when a
  witness JSON carries it. Load dynamically. (Fixed in #863; do not
  regress.)

---

## 9. Conclusion of orientation

The constit-factor closure (PR #863, just merged) was the last
**substrate-side** structural identity blocking Track A. The next
substantive math work is either:

(a) Closing the Bring color-tube weighted averaging gap (research-level,
    owner-flagged), or

(b) Migrating the 4 production tr_M scripts to use the closed form
    (mechanical, ~6-8 hours total, unblocks downstream optimization).

Pick one based on the owner's current direction. When you start, append
a row to `docs/coordination/1ppb-categorical-chain.md` with your theme,
branch, and intended scope so sibling agents can coordinate.

Welcome to the project. The math is settled; the wiring needs you.
