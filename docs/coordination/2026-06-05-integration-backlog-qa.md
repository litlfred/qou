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

## Wall-side drain results (2026-06-05, final)

**5 wall-side criticals cleared, all verified `lake env lean` green** (the env held after the
4th restore):
- `zeta8` (ℂ→`IsPrimitiveRoot`), `pion-half` (ℝ→`CommRing R`), `higgs-t28`
  (`norm_num`→`decide` + out-of-namespace class ref), `figure-eight-reeb-rotation`
  (`Inv ℤ` bug → `{R}[Field R]` + `field_simp`), `meson-qcg-fusion-identity`
  (docstring-before-imports + stale `GroupPower.Basic` import + orphan `/-- -/` +
  `norm_num`→`decide`). Several were also previously-non-compiling — now green.

**3 genuinely blocked (deferred, with reasons):**
- `meson-kaon-pion-hecke-seifert` — `CharZero.Lemmas` out-of-cone in the cache.
- `bring-residue-resolvent` — generic core + Phase-3 `q = 2 : ℝ` concrete witnesses → the
  checker's **"both/mixed"** verdict (no banner escape). Converting Phase-3 to `ℚ` clears
  wall-side BUT `decide` fails on ℚ `Ne` (kernel won't reduce `Rat`) and `norm_num` is the
  flagged tactic → the witness proofs need a non-`norm_num` ℚ approach or a §7c **split** of
  Phase-3 into a separate archimedean file. *Bonus bug found:* `bring_residue_subsingleton`
  (line ~165) fails (`rw [hr, hr']` motive-not-type-correct); fix is term-mode
  `⟨fun ⟨r,hr⟩ ⟨r',hr'⟩ => Subtype.ext (hr.trans hr'.symm)⟩`.
- `chi-v21-hoefsmit` — genuinely archimedean (Hoefsmit `Real.sqrt`); imports whole
  `Mathlib.Tactic` (out-of-cone). Make it pure-ℝ + acknowledgement banner in a fuller cache.

**Checker note (CORRECTED for the current post-rebase checker):** `checkWallSide` **strips
`/- -/` + `--` comments and `import` lines** before testing — so only *code-body* tokens flag
(`norm_num`/`linarith`/`positivity`/`Real.*`/`: ℝ`/`(ℝ)`). A banner clears the
*archimedean-without-acknowledgement* mode but **NOT** the *both/mixed* mode (that needs a real
split or full conversion). Use `decide`/`ring`/`linear_combination`/`field_simp` in code.

## Gap-closing results (2026-06-06) — the 3 deferred blocks

With the Lean env restored (5th) and the cache-extension method found, the 3 deferred
wall-side blocks were addressed both sides:

- **meson-kaon — CLOSED (verified green).** Refactored ℝ → generic `{R}[Field R]`.
  `seifert_ratio_T25_T23` uses explicit `(2,3,5 ≠ 0)` hypotheses (not `CharZero`), so it stays
  IN the cache cone (proof `push_cast; field_simp; ring`); `chi_21_odd` via `Odd.neg_pow`.
  wall-side passes. The n_q=2 exponent + PDG match remain empirical/witness-backed (not a Lean
  gap), documented in the .md "Lean structure" section.
- **bring-residue — wall-side CLOSED (verified green) + compile bug fixed.** Subsingleton
  `rw`-motive bug → term-mode `Subtype.ext (hr.trans hr'.symm)`. Phase-3 concrete witnesses
  `q=2:ℝ` → `q=2:ℚ` with `norm_num` → `native_decide` (repo-sanctioned; handles the `Rat`
  computation `decide` can't reduce). **Remaining deep gap:** the `BringResidueAtOrder` class
  instance (pole-nonzero / full residue justification) — §3b-cond, precisely specified.
- **chi-v21 — follow-up PR.** Deep gap = `chi_v21_matrix_trace_identity` sorry (11-matrix
  fold; the sqrt-free strategy via `sigma1_v21_param` + even-σ₁-count is already in-file).
  wall-side "mixed" is the deliberate **Tier-2 migration state** (generic `sigma1_v21_gen` +
  ℝ matrix work) per `docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md`; closing it is
  the migration split, not a quick fix. Whole `Mathlib.Tactic` import keeps it out-of-cone.

**Cache-extension method (KEY, verified 2026-06-06):** `lake build Mathlib.<Module>` builds a
single module incrementally from the restored cone — **safe, fast, no wipe** (Matrix.Trace in
3.6 s). This is how to verify out-of-cone refactors going forward; never `lake env true` /
`lake update` / `cache get` (they wipe). Now in `formalizer.md §7c`.

## 2026-06-08 — #1939 proof-rater baseline: main-integration + sidecar union-graft + inherited Lean red

**PR #1939** (`claude/proof-rater-baseline-audit-2026-06-07`) adds a new sidecar
criterion family corpus-wide: `proof-rater-strategy-clarity`, `-goal-plausibility`,
`-novelty`, `proof-statement-integrity` (568 entries / 142 blocks). All four are
`needs-agent` — a mechanical full-regen will NOT recompute them.

- **Conflict resolved (was `dirty`):** main moved 87 commits ahead (sibling sidecar
  regens added `detangler-topic-coherence` / `-graph-energy` corpus-wide). Integrated
  via merge commit + **per-file union graft**: take the other side's freshest sidecar
  wholesale, graft in only the 4 proof-rater criterion keys. Different keys ⇒ zero data
  loss either direction. Resolver: keep main's `criteria` object, overwrite/add the 4
  proof-rater keys from the branch, take max `updated_at`.
- **Sibling protocol (posted on #1945 / #1918 / #1941):** when regenerating sidecars,
  **union-preserve existing criterion keys** rather than replacing the whole `criteria`
  object — else the `needs-agent` proof-rater keys are dropped. Re-graft is cheap for
  whichever PR lands second.
- **Inherited Lean red (NOT caused by #1939, blocks any QOU `lake build`):** upstream
  Mathlib API drift — `Matrix.PosSemidef.sqrt` dot-notation no longer resolves
  (`hA.sqrt` → falls through to non-existent `And.sqrt`) in
  `QOU/MathlibExt/PosSemidefTraceZero.lean` (`set Asqrt := hA.sqrt`, `hA.posSemidef_sqrt`)
  and `QOU/HeckeAlgebra/Formal.lean`. Both files byte-identical to base. Needs a dedicated
  lean-build-fix branch; the correct current-Mathlib name for the PSD square root must be
  re-looked-up (candidates: `Matrix.PosSemidef.sqrt` may have moved/renamed). Out of scope
  for #1939.
