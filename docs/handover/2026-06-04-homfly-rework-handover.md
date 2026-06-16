# Handover — HOMFLY rework + mass/binding verification-gap audit

**Date:** 2026-06-04 · **Branch:** `claude/homflypt-n3-implementation-2026-06-04`
· **PR:** [#1792](https://github.com/litlfred/qou/pull/1792) (open, rebased on
main, reviews requested, **not merged** — awaiting explicit author merge).

## TL;DR for the next agent

A request to "surface a buried docstring admission and walk the mass/binding
pipeline" grew into a **verified fix** of the HOMFLY engine. The PR is
self-contained (docs + 4 compute files), rebased clean on main, local QA green,
reference gate **5/5**. CI is red but it is **GitHub Actions billing** (every
run finishes in ~4 s, jobs never start — see CLAUDE.md billing rule). Do **not**
diagnose CI red as a code problem here.

## What landed (7 commits)

| Area | File | State |
|---|---|---|
| Audit + pipeline walkthrough | `docs/audits/2026-06-04-hidden-fitting-verification-gap-mass-binding-walkthrough.md` | done |
| Convention discipline (KEEP THE WRITHE) | `docs/homfly-markov-convention-discipline.md` | done |
| Reference-value gate | `computations/homflypt_reference_qa.py` | **5/5 pass** |
| Reworked correct engine | `computations/homfly_ocneanu_trace.py` | n=2,3 validated |
| Exponent fix + de-buried warning | `computations/homflypt_engine.py` | done |
| Mass-tower demotion | `computations/homflypt_su_n_mass_tower.py` | done |

## The technical story (so you don't re-derive it)

1. **The buried admission** was real: `_homflypt_nstrand_numerical` is
   ratio-only (writhe framing dropped). Surfaced into the audit doc.
2. **Deeper root cause:** the SU(2) point `v = q^{(N-1)/2}` makes the loop
   value `δ ≡ −1` *identically* — the degenerate Jones point where every knot
   collapses to ±1 (this is why trefoil = figure-8 = ±1 in prior runs). Fixed
   to `v = q^{N/2}` (`δ = −[N]_s`, non-degenerate).
3. **KEEP THE WRITHE (author directive):** in QOU the writhe is the U(1)
   framing phase `q^{w·c}` = EM phase / chirality. So production uses the
   **framed** invariant `P_framed(β) = Σ_λ w_λ χ^λ(β)`; the textbook unframed
   value is `a^{w}·P_framed` and is used **only** by the gate to check the
   knot-type part. Do not strip the writhe.
4. **The correct engine** (`homfly_ocneanu_trace.py`):
   - `s = √q₀`, `a = s²`, `z = s − s⁻¹`; `χ^λ` is the **signed** seminormal
     Hecke character evaluated at **`s`** (NOT `q₀` — that variable mismatch
     was a concrete bug; `chi_lambda_braid(..., q_value=s)`).
   - Ocneanu weights `w_λ` are **unique constants** (forced by the Markov
     property). They are solved per-n from a skein-spanning set and
     **validated on held-out knots** (fig-8, trefoil, cinquefoil) to 1e-9
     inside `_weights()`. This is determination+verification, **not fitting**
     (zero residual freedom). At n=3: `w_(3)=0, w_(2,1)=1, w_(1,1,1)≈2.011`.
   - n≥4 raises `NotImplementedError` with the spanning-set recipe.
5. **Mass tower** (`homflypt_su_n_mass_tower.py`) was at the degenerate point →
   its SU(2) ratios/mirror-diffs were noise. Demoted to EXPLORATORY; the
   `E₀ = Q_β/|ΔP|` block is a **back-solve/fit** (a per-channel E₀ ≠ the
   universal `m_e/(q₀(q₀−1))` — that is the fit signature). Relabelled.

## Key distinction the audit hammers

- **Verification gap:** `cross_check_trM_1ppb.py` proves four methods *agree*
  (all share `Σ y_λ χ^λ`). Agreement ≠ correctness. The skein gate is the
  first **external** anchor.
- **Signed χ (HOMFLY) vs |χ| (binding) are different objects.** The mass
  pipeline uses `Σ y_λ |χ^λ|` (modulus, by design — "strong binding =
  modulus"). You cannot recover a signed knot invariant from absolute values.
  HOMFLY and binding must stay separate engines. (Done — the rework is a new
  file, untouched binding path.)

## Open follow-ups (priority order; from audit §4)

1. **n≥4 Ocneanu weights** in `homfly_ocneanu_trace.py`. Mechanical: add a
   spanning set of `len(partitions_of(n))` braids with independently-known
   unframed HOMFLY (torus + disjoint-union family), the module self-validates.
   Watch: at SU(2), partitions with >2 rows have quantum-dim 0 but their
   seminormal **character** is nonzero — the (1,1,1)-type weight is still
   needed (it came out ≈2.011, not 0). Use a genuinely spanning set (the
   stabilised-torus family alone is degenerate — it validated other torus
   knots but failed fig-8).
2. **`χ^λ` external anchor** for `cross_check_trM_1ppb` (small-partition closed
   form, e.g. `χ^{(n)}=s^{...}`, `χ^{(1ⁿ)}`).
3. **Binding-input SDP convergence** (rows 9–11: L6a4 heuristic) — separate
   track, see `docs/audits/2026-06-03-binding-link-assignment-heuristic.md`.

## Merge / process state

- PR rebased on `origin/main` (was 7 ahead / 52 behind — clean rebase).
- Copilot review requested; reviewer-facing summary comment posted with the
  `[skip-ci: billing]` note.
- **Merge is NOT authorized** — the author said "auto /prepare-merge", which is
  prep, not the strict "merge it"/"ship it" permission. Leave for the author.
- This session subscribed to PR #1792 activity. CI events on it are billing
  noise; review comments (Copilot earlier flagged a non-existent `||` table
  issue — false positive, the file uses single pipes; and a verbatim-quote
  typo that is intentional) need no action.

## How to verify quickly

```bash
cd computations && python3 homflypt_reference_qa.py
#   expect: reference symbolic PASS, "n≥3 path: 5/5 match reference"
python3 homfly_ocneanu_trace.py   # prints proton/neutron/fig-8 (self-validates on import)
```
