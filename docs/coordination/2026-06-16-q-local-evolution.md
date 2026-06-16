# Coordination ledger — q ↔ CAL anchor drift + local-q evolution

**Goal slug:** `q-local-evolution`
**Lead PR:** [#2346](https://github.com/litlfred/qou/pull/2346) — branch `claude/gracious-lovelace-uzuovl`
**Opened:** 2026-06-16
**Owner driver:** "figure out CAL 1/2/3 and relation to q; how does q evolve locally at p" + 4 proposed routes.

## Scope map

| PR / branch | Relationship | Classification | Action |
|---|---|---|---|
| **#2346** (this) | lead | — | audit + routes 3/4 done; 1/2 sketched |
| [#1556](https://github.com/litlfred/qou/pull/1556) `m-mu-chain-audit` | **overlap (high)** — m_μ anchor-vs-prediction status | no file overlap; finding-dependency | intent posted; cited their ratio-anchored convention split for the m_μ L2 reconciliation |
| [#2345](https://github.com/litlfred/qou/pull/2345) `jolly-newton` (Q_β kernel / Koide) | overlap (moderate) — Q_β role, lepton masses | no file overlap; orthogonal (c_k ladder vs base-Q_β CAL) | intent posted; flagged Q_β-becomes-derived + "q is the ratio" reparam vs their Koide-CAL-4 refutation |
| [#2081](https://github.com/litlfred/qou/pull/2081) (metallic q↔ρ) | tangential — q↔ρ ≠ q↔CAL | not in scope | skipped (no comment — avoid noise) |

## Key findings

- **Anchor drift (3-way):** live compute is **proton-anchored** (`m_p/m_e`,
  re-pin 2026-05-28 `01c18125`); paper blocks still say muon; CLAUDE.md
  table says neutron. `m_μ/m_e` is now a 9.5σ prediction.
- **3rd-CAL fork:** paper blocks say `Q_β`; cheat-sheet diagram says
  `m_π` (`Q_β` derived). **Owner resolution:** 3rd CAL = `m_π`, `Q_β`
  derived, `q₀` proton-anchored.
- **"q is the ratio"** = reparameterization (any one ratio coordinatizes
  `q₀`), not an identity. Ratio-anchored convention is exactly this.

## Route status (see audit Part B)

| Route | Verdict | State |
|---|---|---|
| 4 fix-drift | ✅ | **done** — author-notes on both calibration blocks |
| 3 un-stub Lean | ✅ | **done + build-verified** (lean-direct exit 0, v4.24.0) |
| 2 germ-dynamics | ✅ ½-exists | **sketched** (scope doc); 2a/2b = paper-content follow-ups |
| 1 fixed-point | ⚠ naive refuted | **sketched** (scope doc); q₀-selection re-opened research |

## Follow-ups (tracked, not done here)

1. **Prose migration** of the calibration basis (muon→proton, Q_β→m_π)
   in `prop:three-calibration-discipline` + ripples
   (`prop:three-calibration-inputs`, Wedderburn-count prop, SDP
   `m_π`-independence). Owner-confirm before rewriting scholarly prose.
2. **Route 2a/2b** paper blocks (germ-commutator = q-curvature prop;
   q-harmonic flow conjecture) — gated on the content-validation tooling
   (`folio-assistant/schemas` absent on this checkout) + Lean.
3. **Route 1a** probe (`‖(q-1)𝓕_q^intr‖(q)` critical point) — owner-gated
   (re-opened substrate-q₀ derivation), needs `pyhecke_native`.
4. **Stale-doc cleanup:** cheat-sheet §1 internal CAL-3 inconsistency
   (diagram says `m_π`, CLAUDE.md table neutron); `qou-substrate/README.md:29`
   prints the muon `q₀`.

## ⚠ CORRECTION (owner, 2026-06-16 ~04:30) — convention is MUON-canonical

The earlier "Owner resolution: 3rd CAL = m_π, Q_β derived, **q₀ proton-anchored**"
was **half-corrected by the owner**. The corrected, authoritative convention is
**two-layer**:

- **Canonical *mathematical* triple = `(m_e, m_μ/m_e → q₀, m_π)`** — CAL-2 is the
  **muon** lepton ratio (it dimensionalises to `Vol(4₁)`), **not** proton.
- **`Q_β` is derived** (bar-odd `sinh` partner of the bar-even `cosh` meson scale
  `m_π` — the symbolic Q_β↔m_π relation is the cosh/sinh bar-parity split,
  `substrate-cohomology-calibration-story`). CAL-3 = `m_π` is *forced* (m_π
  independent via `Vol(Hopf)=0`; `Q_β = f(m_e,q₀)`).
- **Proton `m_p/m_e` is a Physical-Observations precision anchor only** (0.06 vs
  22 ppb; live `q_at`, re-pin 2026-05-28) — a precision substitution within the
  same H¹ datum, **not** the canonical CAL-2.

The prior commits (proton-canonical migration of the discipline block + cheat-sheet)
were **reverted** to muon-canonical, and the convention was propagated across
CLAUDE.md, the 4 discipline skills, `three-calibration-inputs`,
`epistemic-status-of-calibrations`, and the two `codata_constants.py` docstrings.

## Scope map (added 2026-06-16)

| PR / branch | Relationship | Action |
|---|---|---|
| [#2355](https://github.com/litlfred/qou/pull/2355) `youthful-faraday` (σ_F math/observed split) | overlap — shares math-vs-observed philosophy + q₀ precision | intent posted; aligned vocabulary to "canonical math vs physical-observations" |
| [#2295](https://github.com/litlfred/qou/pull/2295) `gallant-volta` (Lean two-layer drift / proof-objects regen) | overlap — I edited block-sibling `three-calibration-discipline.lean` (one of its 408 sibling-only refs; was broken on main, now lean-direct verified) | intent posted; flagged as resolved-not-stale for their relink |

## Log

- 2026-06-16 02:3x — PR #2346 opened; audit + route 4 author-notes +
  route 3 verified Lean repair landed; routes 1/2 scope doc; intent on
  #1556, #2345. Gemini at daily quota on #2346 (no review until reset).
- 2026-06-16 ~03:4x — Task 1 (prose migration) + Task 4 (cheat-sheet) done
  PROTON-canonical (pushed) — **superseded by the correction below.**
- 2026-06-16 ~04:30 — Owner correction: MUON-canonical, proton = phys-obs
  anchor. Reverted + propagated convention across CLAUDE.md + 4 skills +
  3 content blocks + 2 compute docstrings (commits A/B/C). Dashboards
  (low + sweep) re-run clean at α=E₀=4.186 MeV (convention is doc-only;
  compute unperturbed). Intent posted on #2355, #2295.

## Coordinate sweep — phase/color/S₅ tranche (2026-06-16 ~23:xx)

- **My PR #2346 review state:** no gemini/copilot review threads (gemini at
  daily quota — `#issuecomment-4714310301`, not a code issue). Incoming intent
  from **#2363** (`#issuecomment-4722425655`): q₀-anchor-agnostic, consumes
  `𝔈₀ = m_e/(q(q−1))`, no file collision; asks a ping only if CAL-3 reframing
  changes `𝔈₀`. **Verified: my muon-canonical convention leaves `𝔈₀`'s form
  unchanged (q₀ form unchanged) — no ping needed.**
- **Scope map (phase/color/S₅ tranche):**

  | PR | relationship | overlap / dep / cherry-pick | action |
  |---|---|---|---|
  | **#2346** (this) | lead | — | phase audit + S₅ Lean landed |
  | **#2297** `friendly-archimedes` (3D color-tube render) | **genuine overlap** — color-tube cubic, `conj:s5-so3-fiber-action`, complex roots {−1,±i} | overlap=high (structural), dep=none, cherry-pick=none; **no file collision** (they: `scripts/knot-plots`+`color-tube-cubic`/`coral-elliptic`; me: `mass-endo`+new Lean+audit) | **intent posted** (`#issuecomment-4724158064`) |
  | **#1552** α_EM RT Phase 4 (dim H¹(M_Bring)=8) | conceptual EM↔Bring only | overlap=low, no file overlap, modifies no content/Lean, stale (06-13) | **logged, not commented** (avoid noise) |
  | #2363 Q_β counit | incoming intent (above) | no collision | acknowledged in ledger |
- **main advanced** `9a2ee428..1017b897` — landed changes are schema-path +
  content-refactor housekeeping (`5808964b`, `d27b0027`, `fa58e1b1`); no direct
  conflict with the new phase/color files. **NOT merged silently** (§8).

## 𝔙 reorg + mass-endo phase investigation (2026-06-16 ~22:xx)

- **Reorg merged.** `claude/complex-volume-one-voice-reorg-2026-06-16` (6 commits)
  fast-forwarded into `gracious-lovelace` (ff-only; merge-base = HEAD). Chapters
  now tell one 𝔙 story (mass-endo §complex-volume, mass-theory ladder→Re/Im,
  observations β-decay→Im 𝔙, appendix-qvalues→Im 𝔙).
- **Items 6 + 7 done** (commit `ce61e8e5`): `bar-parity-split.md` +
  `substrate-cohomology-calibration-story.md` now name 𝔙=Re+iIm explicitly
  (cross-linked to `conj:binding-qbeta-complex-volume`, added to
  bar-parity-split `uses[]`); 3-col aspect|Re𝔙|Im𝔙 table in
  `complex-volume-intro.md`.
- **⚠ Validation gap:** `folio-assistant/` has **0 tracked files** on this
  branch — `bun run validate` (Zod/constraints) and qa-sweep CANNOT run on this
  checkout. Reorg `.ts` verified by `bun build` transpile only (passes modulo
  the absent `schemas/builders` re-export). **Full validate must run in CI or
  post-rebase on main.** Stale `section-title-audit.qa.json` key
  (`sec:mass-algebraic-qbeta-ladder`) left for qa-sweep refresh (can't run here).
- **Mass-endo phase investigation IN FLIGHT.** Owner asked: is mass = Re∘tr_M
  and color/EM = Im? Corpus-grep refuted the ℤ/3 framing: color is **C₅**
  (ζ=e^{2πi/5}, Bring resolvents), mass uses **|tr_M|** (modulus, not Re;
  `mass-endomorphism-conjecture.md:84-90`), EM = **U(1) σ-backbone** distinct
  from color, no SU(3). Owner chose "investigate C₅ vs U(1) phase first":
  probe running on whether arg(tr_M) is a U(1) CS/framing phase (→ Im 𝔙 / EM)
  or carries the C₅ character χ_ζ (→ color). Verdict → 
  `docs/audits/2026-06-16-mass-trace-phase-c5-vs-u1.md`. NO color block written
  until verdict (avoids injecting unsupported numerology per critical-distance).

## Coordinate sweep (2026-06-16 ~20:40, main +115)

- **#2346 reviews:** none yet (`reviews=[]`) — nothing to triage.
- **Broad-change coordination risk (log).** This branch now carries two
  *wide* changes that will conflict with siblings on rebase:
  1. **`Q_β → 𝔔_β` migration** (~138 content `.md`/`.ts` files; `.lean` keeps
     the `Q_β` identifier).
  2. **Calibration convention** sweep (CLAUDE.md + 4 skills + calibration
     blocks: muon-canonical CAL-2, `m_π` CAL-3, `Q_β` derived).
  Plus the **`𝔙` complex-volume unification** (binding = Re, `𝔔_β` = Im).
- **Intent posted:** [#2363](https://github.com/litlfred/qou/pull/2363#issuecomment-4723802115)
  (Q_β Path A counit observable — most direct overlap: notation + `Q_β=Im 𝔙` +
  derived-not-CAL-3).
- **Other overlapping siblings (will meet the migration on rebase; not posted
  individually — flagged here):** #2347 (Markov-M3 knot decoupling), #2348
  (atom→electron mass / e-Hartree binding), #2325 (m_qCLT factorized binding),
  #2285 (production mass-tables). All touch mass/binding/Markov content with
  roman `Q_β`; recommend they rebase onto #2346 after it lands. #2295 (Lean
  two-layer drift) already has intent re: the repaired `three-calibration-discipline.lean`.
