# Session bean-triage — verified done/stale vs sandbox-blocked (2026-06-25)

**Advances:** `ylgh` (Session: frontier triage + bean-backlog hygiene).
**Purpose:** record which open beans are actually **done / stale** (so the owner can close
them — §4a close is owner-only) vs **blocked by this session's sandbox limits**, so the next
session does not re-investigate. No code change; a hygiene map.

## Sandbox capability gates (this container)

| capability | state | blocks |
|---|---|---|
| **Lean** (lake-cache restore) | ✅ **works** — `lake-cache/qou-v4-24-0` exists on origin; restored **2951 mathlib oleans**; `lean`-direct green-check available | — (Lean-pure beans are doable) |
| **`mpmath`/`sympy`** | ⚠️ **pip-installable** — not preinstalled, but `pip install mpmath` → 1.4.1 (PyPI reachable; **verified this session**) | nothing on its own — **pure-`mpmath`/`sympy` computes run** (e.g. the spectral-bridge witness regen, #2752) |
| **`pyhecke_native`** (custom Hecke wheel) | ❌ **not on PyPI** (verified: no distribution) | full-precision **Hecke** compute — `ct80`-class witness regen, mass-table sweeps, λ_A migrations (`0voz`/`4f2d`); needs a `maturin` build of `tools/pyhecke-native`, or a full env |
| **folio-assistant / content validation** | ❌ **clone 403** (proxy scoped to `litlfred/qou`; sibling repo inaccessible) | all content-block + detangler beans: `foxn`/`flus`/`e5tn`/`yjxk`, and any content-block authoring incl. `48yu` follow-up #1 |

`bun` 1.3.11 is present, but `scripts/run-validate.ts` imports schemas from the (un-clonable)
folio-assistant sibling, so content validation cannot run.

> **Correction (later 2026-06-25, post-#2764).** An earlier version of this row said "`mpmath`
> absent → all compute blocked." That was overstated: `mpmath` pip-installs (PyPI reachable), so
> **pure-`mpmath`/`sympy` compute runs here**. The genuine binding constraint is `pyhecke_native`
> (the custom Hecke wheel, not on PyPI) — only Hecke-precision producers are blocked. Sibling
> #2764 independently pip-installed `mpmath` 1.3.0 + `sympy` in-container.

## Verified DONE / STALE — owner-closeable

| bean / item | verdict | evidence |
|---|---|---|
| `bwkg` (3 broken frontier Lean files) | **DONE** — all 3 green sorry-free; awaiting its PR merge + human close | bean tail "RESOLVED 2026-06-24"; `MarkovPeel.lean` inspected green (class carries `[Add H][SMul R H]`, `hecke_quadratic` uses `h • top n`, proofs close by `ring`); `CategoricalDqSquared`/`QHookBound` noted green on main / fixed |
| `lean-catalan-G-numerical-bound` (lean-discharge-queue) | **STALE** — already discharged 2026-06-10 | `catalan_G_numerical_bounds` is now a theorem in `HyperbolicVolumeTranscendence.lean` (alternating-series bracket); `BorromeanVolumeCatalan.lean` §1 + §6 document it. Queue item (created 2026-06-03) predates the discharge |
| `48yu` (Δ_λ co-Casimir refutation → Lean) | **Lean DONE** (#2676); only folio-gated content promotion remains | `QOU/BraidKnot/DeltaLambdaRefutation.lean` on main: 3 sorry-free ℚ lemmas (`coCasimir_closureGap_eq`, `coCasimir_refuted_deuteron`, `coCasimir_wrong_sign`). Follow-up #1 (content block `lem:frobenius-cocasimir-refuted-deuteron`) blocked by folio-403; follow-up #2 **correctly hedged** — the other 5 ansätze fail by non-miss mechanisms (tautological / under-determined / KL-positivity / ill-posed), so forcing miss-lemmas would misrepresent them (per the file's own landscape table) |
| `ixx4` + placeholder-drain class (`i6p9` `b3pe` `95jh` `ekb8` `zslh` `mlt7` `doth` `ldup` `xj99` `1osq`) | **non-actionable** — owner-only close/retitle | `docs/audits/2026-06-24-placeholder-bean-count-resweep.md`: **0 uncited `sorry` corpus-wide**; titles are inflated raw-grep counts; remaining markers are intentional `-- TODO upstream:` / witness-dep / research notes. Re-confirmed first-hand: `ixx4`'s 6 are all `-- TODO upstream:` on **proved** lemmas |

## Tracked / gated — NOT clean idle-drains (leave for full-env or owner)

- **canonical-watcher** `46ke` (P31 hidden codata, 53 scripts) / `j1hg` (over-count 3-input, 51+117) / `cmiy` (P30 WitnessBuilder, 133) / `trmo` (term6 fit) — large rollups, mostly Class-B/C/D *acceptable* per `2026-05-11-three-calibration-discipline-violations.md`; the vol-hyp uniform shortcut is **owner-settled 2026-06-13 (do not re-litigate)**; `trmo` is AUTHOR-ASSIST. Each needs per-file Class triage **+ running scripts** (mpmath absent).
- **research levers** `kehn` `w5tg` `thb7` `ovud` `p3t6` `ae4b` — need `pyhecke_native` Hecke compute / Sage / owner-gated keystone. **`z2bn`** got a calibration pass this session (PR #2752); its depth-2 `(b)`-exclusion is now **Lean-formalized** (#2764, `Lever1Depth2Exclusion.lean`) and the owner **lifted** the `τ`-derivation gate 2026-06-25 — the coral `E_q` `λ_SW` holonomy derivation is now in-scope (formalize-first, no-fit guard; numerical elliptic-period integration may suffice without full Sage).
- **data-integrity** `ct80` (runner delivered on #2747; regen is full-env), `tnjb`, `z5vu` (owner-gated) — full-env or owner.

## Takeaway

The agent-actionable **in-sandbox** surface is **Lean-pure** (env warm) + markdown + **pure-`mpmath`/
`sympy` compute** (`mpmath` pip-installs — verified). Only two classes stay blocked: **`pyhecke_native`-
dependent Hecke compute** (custom wheel, not on PyPI — `ct80`-class regen, mass-table sweeps) and
**content validation** (folio-assistant clone 403). Sibling sessions drained the Lean-broken-file +
catalan + co-Casimir beans on 2026-06-24 (done-pending-merge, not open); the `z2bn` `τ`-derivation
gate was **lifted** by the owner 2026-06-25 (#2764).
