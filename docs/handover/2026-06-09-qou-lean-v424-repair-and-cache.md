# Handover — QOU Lean v4.24.0 red-repair (#2001) + Mathlib-cache fix

**Date:** 2026-06-09
**Branch:** `claude/lean-repair-qou-red-2-2026-06-08` → PR **#2001**
**Author of this handover:** Claude Code session (winding down)

This document is the durable handover for a continuing agent. Read the
**Environment blockers** first — they cost hours if rediscovered.

---

## 0. TL;DR

- The v4.24.0 Lean repair (#2001) is **done and verified per-module**; the
  only thing missing is a **whole-library `lake build QOU`** confirmation,
  which is **infeasible locally** (incomplete Mathlib olean cache + a
  network-blocked `cache get` + ~30-min container restarts).
- The cache **can** be fixed permanently (from-source build → re-seed the
  `lake-cache/qou-v4-24-0` orphan branch), but it's a **multi-cycle grind**
  (~85 s/olean observed), not a quick fix.
- One **real review finding** is open (Copilot): `IsEmCoupling` is vacuous
  over `R_q` — see §3 item 1. It compiles (not red) but is a formalization
  bug to fix once a full build is possible.

---

## 1. ⚠️ Environment blockers (read FIRST)

| Blocker | Detail | Implication |
|---|---|---|
| **Mathlib `cache get` 403** | `lake exe cache get` → `7335 download(s) failed`, `403` on every `*.ltar.part` shard (`lakecache.blob.core.windows.net`). The container-root URL 403s; individual blob GETs also 403. | Can't fetch a complete olean cache. |
| **Partial local cache** | `lake-cache/qou-v4-24-0` orphan branch = 731 MB ≈ **2918/7435** Mathlib oleans + 18 QOU oleans (seeded when QOU was mostly red). The other cache branch `lake-cache/Qq-v4-24-0-e2e-test` is **empty**. | Individual modules whose Mathlib deps are cached build in seconds; the **full lib** hits a Mathlib-rebuild wall. |
| **From-source Mathlib build is slow** | Mathlib **source is fully present** (7435 `.lean`), so `lake build QOU` *does* build missing oleans — but ~**85 s/olean** (≈ +7 oleans / 10 min observed). | Completing the QOU-needed Mathlib subset is **many hours**. |
| **Container restarts ~every 30 min** | Kills any long build. **Oleans persist on disk**, so re-launching resumes. | Long builds need babysitting across cycles. |
| **CI billing failures** | `qa-sweep`, `paper-builder`, `witness-refresh` "fail" in **0 s** (same timestamp) — the GitHub Actions billing signature (AGENTS.md §"CI billing failures"). `section-title-audit` passes. No `lean_ci` runs on feature branches. | **Not code issues.** The Lean gate runs on `main` post-merge. |
| **Gemini review quota** | `/gemini review` → "reached your daily quota limit … up to 24 hours". | Reviews are **Copilot-only** until reset. |

### Lean env recovery after a restart
```bash
export PATH="$HOME/.elan/bin:$PATH"
export ELAN_TOOLCHAIN=lean-v4.24.0           # toolchain symlink survives restarts
elan override set lean-v4.24.0
# Build from REPO ROOT (root .lake keeps ~2918 Mathlib oleans; per-paper .lake gets wiped):
cd /home/user/qou && lake build QOU.<Module>   # single module = seconds if its Mathlib deps are cached
```

---

## 2. What was done on #2001 (verified)

6 red modules fixed + **each compiled green individually** (root workspace):

| Module | Root cause (v4.24.0) | Fix |
|---|---|---|
| `Interactions/HeckeEngine` | `ring` can't use `q·q⁻¹=1`; `simp only` left `fin_cases` `match` unreduced | `linear_combination (poly)*q_mul_q_inv` (coeffs sympy-derived, `rem=0` ×9) + **full `simp`** |
| `Archimedean/PauliWitness/Witness12C` | duplicate def block + 250-term `•`-chain `whnf` timeout | dedup + **`foldr`-over-`List (ℤ×ℤ)`** (sympy-verified data-preserving) |
| `Interactions/BringShellBinding` | `fin_cases` fails on Finset-coe membership | `Finset.mem_insert` → 7-way disjunction → `decide` (was a `sorry`) |
| `BraidKnot/ShellNeutrality` | `congr 1` left `Multiset.map _ 0 = 0` | `all_goals simp` |
| `Archimedean/EmCouplingProjection` | `/`,`q⁻¹` over non-field Laurent ring + dangling theorem | division-free `IsEmCoupling` relation (**see §3.1 — has a follow-up**) |
| `QuantumObservableUniverse/GaugeTheory` | `vd` uninferable from `… = 0` goal | `HasCategoricalEOM.transport (vd := vd)` |

Plus ~10 earlier drift fixes (Wedderburn, MarkovTrace, SDP, HeckeRep,
AlgebraicPrimality, PauliWitness ×9, Cl3Zeta5/KnotIndexed imports, TypeBFolded).

**Static reverse-dep check (clean):** EmCoupling's removed decls have **zero**
`.lean` consumers (`QOU.qInteger`/`q_param` hits are distinct decls in other
namespaces/files); the 5 EmCoupling decls have no name conflicts; the other 5
modules changed only proof bodies / a def *representation* (signatures intact).

**Rebase:** clean onto current `main` (no file conflicts; deps `GroundRing`
etc. unchanged by main since divergence). Force-pushed → tip `cbff3da8`-ish.
Content validates (`✓`). lean-ref migration is a no-op (0 legacy refs).

---

## 3. #2001 follow-ups (ordered)

1. **Fix `IsEmCoupling` vacuity** (Copilot, `EmCouplingProjection.lean:81`).
   `IsEmCoupling (α : R_q) := [9]_q·[10]_q·α = q⁻¹` is **vacuous**: in the UFD
   `R_q = ℤ[q,q⁻¹]`, `[9]_q·[10]_q` is a non-unit and `q⁻¹` a unit, so no
   `α : R_q` satisfies it — yet the docstring says α_EM *is* a fraction-field
   element. Compiles (not red) but inconsistent. **Fix:** range over a generic
   R_q-algebra / `FractionRing R_q` where α_EM lives, mapping the relation's
   data via `algebraMap` (keeps the division-free data in ℤ[q,q⁻¹]):
   ```lean
   def IsEmCoupling {K : Type*} [CommRing K] [Algebra R_q K] (α : K) : Prop :=
     algebraMap R_q K (qInt 9 * qInt 10) * α = algebraMap R_q K q_inv
   ```
   Update `isEmCoupling_iff` accordingly. **Rebuild to verify**, then
   reply+resolve the Copilot thread. (Deferred because it's architecturally
   significant and un-buildable in this sandbox — a blind edit risks
   re-reddening the module.)
2. **Gemini review** — re-post `/gemini review` once the daily quota resets (~24 h).
3. **Whole-library gate** — confirm `lake build QOU` is green via **post-merge
   CI on `main`** (or via the cache fix in §4).
4. **Merge** — needs the **owner's explicit** "merge it". Method per AGENTS.md
   rule 8 = **rebase** (the prepare-merge skill says merge-commit; confirm with
   owner). Do **not** squash.

---

## 4. Fixing the Mathlib cache "so all" (permanent path)

`cache get` is blocked, so the only path is **from-source build → re-seed**:

1. **Build** the QOU-needed Mathlib subset + QOU from source (source is on
   disk). Babysit across restarts — oleans persist, so re-launch resumes:
   ```bash
   cd /home/user/qou; export PATH="$HOME/.elan/bin:$PATH"; export ELAN_TOOLCHAIN=lean-v4.24.0
   (timeout 3500 lake build QOU > /tmp/qoufull.log 2>&1; echo "EXIT:$?" >> /tmp/qoufull.log) &
   ```
   Expect **many hours / several restart cycles** (~85 s/olean; ~4500 Mathlib
   oleans missing of which QOU needs a large subset).
2. **Re-seed** `lake-cache/qou-v4-24-0` after a green build so the NEXT session
   restores in ~2 min — see the **🗄️ PRESERVE THE BUILD** section of
   [`.claude/skills/local/lean-environment-setup.md`](../../.claude/skills/local/lean-environment-setup.md)
   (uses a separate `git worktree`; oleans tarred + split into <100 MB
   `lake-oleans.tgz.partNN` chunks; `scripts/lake-cache-produce.py` per PR #1957).

**Realistic recommendation:** unless someone will babysit the multi-hour
grind, treat the whole-library gate as a **CI/post-merge** job and rely on the
per-module + static verification for review. The from-source build left running
this session accumulates durable oleans either way.

---

## 5. The other 29 open PRs — `/prepare-merge` each

Run `local/prepare-merge-auto` (or `/prepare-merge`) per PR. Most belong to
**other live sessions** — coordinate before force-pushing.

Open PRs (as of 2026-06-09): #2001 (this), #2024, #2023, #2022, #2020, #2019,
#2014, #2011, #2008, #2006, #2003, #1990, #1977, #1976, #1975, #1966, #1944,
#1942, #1941, #1933, #1928, #1918, #1839, #1808, #1765, #1762, #1741, #1562,
#1062, #411.

**Per-PR recipe:** (1) fetch + checkout (use a **worktree** if a build is
running); (2) `git rebase origin/main` (auto-resolve witness drift per the
prepare-merge skill §1a); (3) `cd content && bun run migrate-lean-refs && bun
run validate <paper>`; (4) one-voice on touched `.md`; (5) **skip** the full
`lake build` (infra) — build only the touched modules from root; (6) `git push
--force-with-lease`; (7) request **Copilot** review (Gemini quota-blocked); (8)
subscribe. **Do not merge** without the owner's explicit per-PR "merge it".

**Cheapest wins first** (likely conflict-free): #2008 (skill), #2006/#1966
(docs), #1977 (cleanup), #1976/#1928/#1944 (voice/qa chores). Surface the
Lean-heavy ones (#2019, #1990, #1975, #1933, #1562, #1839) for focused review
once CI billing + Gemini quota recover.

---

## 6. Immediate next actions (for the continuing agent)

1. Re-establish the Lean env (§1 recovery block).
2. Decide cache strategy: babysit the from-source build toward a re-seed (§4),
   **or** rely on CI for the gate.
3. When buildable: apply & verify the `IsEmCoupling` fix (§3.1); resolve the
   Copilot thread.
4. Re-post `/gemini review` once quota resets.
5. Work the 29-PR drain (§5), cheapest-first, coordinating with sibling sessions.
6. Get the owner's explicit merge OK before merging any PR.
