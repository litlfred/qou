# Coordination — QA staleness infra + `/integration-backlog all` drain (#1885)

**Branch:** `claude/dreamy-albattani-RKsjx` · **PR:** [#1885](https://github.com/litlfred/qou/pull/1885)
**Goal:** drain the integration-watcher QA backlog; fix lean-compile-audit staleness (SHA-based).

## Scope map (2026-06-05)

| PR | Branch | Scope | Overlap w/ #1885 | Dep | Cherry-pick |
|----|--------|-------|------------------|-----|-------------|
| **#1885** (this) | `claude/dreamy-albattani-RKsjx` | QA pipeline `.ts` (qa-checkers-extended/voice, qa-sweep, lean-compile-audit); 955 proof sidecars → `n/a`; 25 one-voice `.md` (mba + mechanical) | — | — | — |
| **#1871** | `claude/confident-newton-R8lIx` | M=Vol×Density SU(2)/SO(3) symmetry — `mass_vol_density.py`, `_li_2_q_util.py`, `MassVolDensity.lean`, `binding-manybody-jet-filtration.*`, `sw-period-residue-sum.*`, audit docs | **none** (no shared file; adjacent chapters mass-theory / brings-surface) | none | none |

## Classification (skill §2)
- **#1871:** overlap LOW/none, dependency none, cherry-pick none. Coordination point: #1885's `proof-lean-compiles` change (SHA-staleness → `n/a` for stale/missing cache) governs how #1871's **new Lean blocks** are QA'd. Both PRs billing-blocked.

## Comments posted
- #1871: intent + QA-semantics heads-up — https://github.com/litlfred/qou/pull/1871#issuecomment-4634037427

## #1885 own-PR review triage (skill §5)
- 4 threads (Gemini ×1, Copilot ×3) — all **accepted + fixed** in `657e34dc` (path.resolve + containment/`.lean` guard; hashFile reorder; `$schema` `v1|v2` union). 3 marked outdated; no open actionable threads.

## Escalations (skill §6)
- None. Findings consistent across PRs (shared billing-block diagnosis; no contradictory framing).

## main watch (skill §8)
- `origin/main` +18 since divergence (qbeta / gap-a4 activity). No main landing touches #1885's QA-pipeline files. Rebase deferred to `/prepare-merge`.

## Landed in #1885 (final)
- SHA-staleness infra (`lean_sha`, `--stale`, checker `n/a` gate) + Gemini/Copilot review fixes.
- proof axis: 638 stale `proof-lean-compiles` fails → `n/a` (955 sidecars).
- one-voice mechanical: 25 blocks (unicode-crash/emoji/editorializing/status-leak/time-stamped).
- one-voice author-notes: 13 blocks migrated (§4d, provenance → authorNotes / dropped).
- detangler: 5 spurious forward-edges pruned (4 blocks).
- coordination ledger + #1871 intent.

## Deferred work (post-#1885 — needs owner input / different env / larger scope)
1. **detangler reorders (3, quantum-observable-universes)** — `adjoint-trace` + `archimedean-realisations` (remarks → move after the prop they interpret); `braiding-eigenvalue-extraction` (prop → reorder before `prop:tannaka-krein-reconstruction`). Chapter-manifest surgery + forward-ref cascade check. Owner leaned "move rmk forward" — held for approval (manifest edits change reading order).
2. **detangler prop→conj (1)** — `archimedean-functor-uniqueness` → `conj:dilogarithm-archimedean-limit` (genuine dep, 6 mentions, 168 apart). ALSO a §3b conjectural-propagation flag (a proposition downstream of a conjecture). Route to a proof/propagation pass, not a reorder.
3. **detangler-block-tanglement (13)** — block splits / relocations; judgment-heavy.
4. **author-notes — true backlog ≈ 100 (not 14)** — re-sweeping with the current checker surfaced ~86 more blocks whose stale `pass` entries now fail (PR/date provenance accreted since last clean audit). Batch in a follow-up.
5. **un-authorized voice criteria** — `wall-side-correct` (12, critical), `voice-scholarly-default` (7), `voice-statement-no-interpretation` (5). Need judgment; not in this campaign's scope.
6. **compute axis (15) — ENV-BLOCKED** — `compute-witness-exists` (4), `compute-prop-has-probe`/`-consumer` (5+5), `compute-lp-dual-present` (1) all require running Python producers (`lp-duality-check.py`, `probe_he4_*`, …). This container has **no numpy/mpmath/qou_substrate**. Needs a Python-provisioned env.
7. **surreal forward-refs (2)** — `surreal-rate-calculus`, `conway-normal-form` — owner accepted appendix-surreals forward-refs as OK; left as-is.
8. **full sidecar re-sweep** — the committed `qa-checkers` notes-field change re-staled all voice/extended sidecar entries; CI's next full `qa-sweep` is the canonical refresh (will surface item 4's true count).

## Next action
- **`/prepare-merge #1885`** (owner-selected): rebase onto `origin/main` (+18), validate, request Gemini + Copilot reviews. Merge on owner's explicit "merge it" (CI billing-blocked → green-local). Deferred items 1-8 → follow-up branch.

## Generic-R refactor campaign (owner: "push as much to category ring R as possible")

**Done + verified:** `zeta8-witness-level2-su2` → `{R}[Field R] {ζ:R} (hζ : IsPrimitiveRoot ζ 8)`.
Dropped the analytic ℂ model (`Complex.exp(Real.pi·I/4)`); imports-first (fixed a real
`/-! -/`-before-imports compile bug); order-8 fact now proved via
`IsPrimitiveRoot.pow_ne_one_of_pos_of_lt`; clears wall-side-correct. `lake env lean` green
(only Ref'd sorries). Commit `95425708`. **This is the template for the rest.**

**Per-file disposition (corpus sweep of analytic root-of-unity / ℝ blocks):**

| block | verdict | action |
|---|---|---|
| `meson-kaon-pion-hecke-seifert` | **clean** (Seifert-Euler + Hecke χ, rational arith, no √/exp) | ℝ → `{R}[Field R][CharZero R]` |
| `pion-half-figure-eight` | **clean** (2×2 char-poly; also the `λ`-token parse bug + `linarith`→`ring`) | ℝ → `{R}[Field R]` |
| `lagrange-resolvent-transform` | **mixed** — ζ₅ algebraic BUT `1/√5` DFT normalisation is genuinely archimedean | partial: ζ₅→IsPrimitiveRoot, √5 stays |
| `hyperelliptic-quintic`, `x5-z5-automorphism`, `x5-bring-weight-identification` | **mixed** — ζ₅ + genuine Bring/icosahedral √5 geometry (3-6 archimedean tells each) | partial: generalise ζ₅, keep √5 |
| `chi-v21-hoefsmit-matrix-derivation` | **legitimately archimedean** (Hoefsmit radicals, `Real.sqrt`) | §7c banner, keep ℝ |
| `reeb-bundle` | **legitimately archimedean** (declared "Ground ring ℝ"); non-compiling stub (`ExceptionalDivisor` pending) — AND a real **bug**: `holonomy : ℝ := Real.exp(2π/[2]_q)` dropped the `i`; should be the U(1) phase `Complex.exp(2πi/[2]_q)` | fix the missing-`i` + route to categorical q-exp (`q-exponential.lean`) when the stub is completed |

**Corpus framing rule (owner's insight):** a ζ-block drops ℂ → `IsPrimitiveRoot ζ n` over
generic `R` **iff** it only uses the root's *cyclotomic/order algebra*; if it evaluates an
*analytic function* (Li_n, Bloch–Wigner, Clausen) or a *real √/angle/holonomy* (√5, 2π/5
radial, real Reeb exp), ℝ/ℂ is essential. Keep-ℂ analytic blocks: `Infra/Polylogarithm`,
`Archimedean/BlochWigner*`, `Clausen*`, `BraidKnot/CyclotomicTrilogImaginary`,
`mass-theory/archimedean-functor-uniqueness`.

**Update (2026-06-05, late) — after a 4th Lean-env restore succeeded** (toolchain via GitHub
asset + `lake-cache/qou-v4-24-0` oleans, with the `lake env true` source-materialisation fix):
- **`pion-half-figure-eight` → `{R}[CommRing R]` — DONE + verified** (`lake env lean` green,
  wall-side cleared). λ-token bug fixed; `linarith`→`linear_combination`; `norm_num`→`decide`
  on the ℤ det facts (the wall checker greps `norm_num`); comment reworded to drop the literal
  `ℝ` glyph (the checker greps comments too).
- **`meson-kaon-pion-hecke-seifert` — BLOCKED by the partial cache cone.** Its `seifert_ratio`
  needs `Mathlib.Algebra.CharZero.Lemmas` (the 2,3,5 ≠ 0 cast lemmas), which is **out-of-cone**
  in the `MassVolDensity`-seeded cache (missing-olean). The refactor is written + template-
  ready; verify with a fuller cache (or after compiling `CharZero.Lemmas` once). Reverted to
  the committed ℝ original to avoid leaving it broken.

So **zeta8 + pion-half** are the verified generic-R wins (2 wall-side criticals cleared).
**Checker gotchas (next agent):** `ARCHIMEDEAN_LEAN_RE` is a naive whole-file grep — it flags
`norm_num`/`linarith`/`positivity` and the bare `ℝ` glyph **even inside comments**. Use
`decide`/`ring`/`linear_combination`, and never write `ℝ` in a generic-R file's prose.
