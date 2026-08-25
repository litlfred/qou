# Getting to 1 ppQ — L2 two-front survey (2026-07-26)

**Question surveyed.** "How to get to 1 ppQ?" — i.e. what actually closes the
headline precision goal. Grounded in the live dashboards on `main`.

## The two legs, disambiguated

- **L1 — compute precision (literally "1 ppQ" = 10⁻¹⁵):** ✅ **MET.** 70-dps
  cross-method agreement; `onepb-status-dashboard.witness.json` all-pass. The
  part-per-quadrillion *internal-consistency* target is **not** the open problem.
- **L2 — per-observable accuracy (σ_pred ≤ σ_exp/100):** **2/7**
  (`per-observable-100x-status.witness.json`, `beats_100x_count`).

| observable | err (ppb) | 100× target (ppb) | miss | tier |
|---|---|---|---|---|
| m_e | 0 (anchor) | — | ✅ | — |
| m_K/m_π | 23.4 | 264 | ✅ | — |
| Q_β | 1248 | 7.8 | 160× | Front A |
| Δ_pn | 756 | 4.7 | 159× | Front A |
| m_n | 2.39 | 0.006 | 416× | Front A (+ B) |
| m_p | 1.35 | 0.003 | 437× | Front B |
| m_μ | 210 | 0.22 | 964× | Front B (μ–p tension) |

The **Q_β / m_n / Δ_pn** trio share **one** root: the Q_β ladder is truncated at
k=2 (c₂ = −1 proved exact), and k≥3 needs a *canonical, non-fitted* rung
(`2026-05-30-l2-100x-status-3-failing-shared-root.md`). m_p/m_μ are separate
(pin round-trip; μ–p substrate tension).

## Front A — w(q) / the GGM crossing-weight derivation (Subgoal-1)

The k≥3 rung = the higher-order **crossing weight w(q)** whose odd part
reproduces the c₃ → −2 signature (z-ck ledger §4-octies "sharpened keystone").
**The constraint / parity layer is saturated** — proved-lean and closed:

| row | content |
|---|---|
| KC16 | c_k ladder has index-alternating bar-parity `(−1)^k` |
| KC18 | archimedean eval map splits exactly: bar-even shadow `h²/2` + bar-odd crossing `−h·w` |
| KC19 | eval map affine in w ⇒ ladder Möbius; **c₃ swing lives entirely in w(q)**, kernel K(q) anchor-rigid |
| KC20 | bar-odd carrier is not a root-of-unity object; degree-3 field ⇒ real-q/quadratic c₃ closures structurally excluded |
| — | valuation floor `(1−q)^{2n+3m}` **tight**; level map has **unbounded** degree — no small universal bridge (`LevelMapValuation.lean`, 2026-07-26) |
| — | graded-split parity: odd/decay face q=1 shadow = 0; split canonical (`OddDecayWeightParity`/`EvenFaceMassShadow`, PR #4275, 2026-07-25) |

**Open piece:** deriving w(q) is the **Garoufalidis–Gu–Mariño state-integral ↔
cyclotomic bridge** — the ledger explicitly records it as "*not a one-session
algebraic identity*." Actively worked by sibling branches (2026-07-26:
`no-bounded-degree-bridge`, `7xvy` G5). **Anti-fit-gated** (Δ_λ gate: six ansätze
failed on the deuteron; the m_p de-fit shows fits get caught). **No bounded
formalize-first brick remains** — the constraint scaffolding is complete; what's
left is the GGM derivation itself.

### The route is *proven* to be resurgent (alien calculus), and it is owned

The odd-channel c₃ closure is not merely "hard" — it is **structurally forced to
be transcendental/resurgent**:

- **KC21**: the c₃ bar-odd part factors `S = h·D(ũ)` (`h = q−q⁻¹` bar-odd carrier,
  `D(ũ)` a bar-even ℚ(√3) ladder); the `dc₃/dq ≈ 4.66×10⁶` "wall" is a `1/u³`
  ladder-inversion artifact over a smooth zero; `q*` (the `S=0` point) is a third
  decay-sector determination of q₀ (proved-lean `fig8Trace_im_odd`).
- **KC22**: `D(ũ)` is **not low-order (q-)holonomic in any tested class** (exact
  through k=21, prime-certified; separated ℚ, coupled ℚ(√3), q-holonomic base
  3/⅓/k, and log-closure all refuted) ⇒ the element is in the **Écalle
  acceleration class**. The entire (q-)holonomic search is **closed**. 2-adic
  parity grading proved; 2 the unique graded prime.

So **q-Borel / Écalle acceleration of the bar-odd D-ladder is the *only*
remaining route to c₃** — precisely the alien-calculus lens. It is **OWNED and
active, flagged "do not fork"** in
[`2026-07-17-1ppq-program-ownership-map.md`](../coordination/2026-07-17-1ppq-program-ownership-map.md):
#3817 (bean `qou-dri7`, parity split) + the k→31 extension session + even-κ
#3683 + Stokes-integer #3805 + Φ_b carrier #3773, using Ramis–Sauloy–Zhang
(Astérisque 355) q-Borel + Di Vizio–Zhang confluence machinery (latest attack
`2026-07-25-qborel-confluence-pos-attack.md`, bean `qou-xa89`, epic `qou-q04o`).
The front carries ~13 Lean files (`BorelWatson*`, `DLadderTwoAdicGrading`,
`DLadderAccelerationComposition`, `ecalle-borel-resummation`, `BarOddLadderShape`)
— no verification-pending flag to close as a quick win. The 2026-07-17
reassessment's "unowned" line is **stale**: it was picked up and is now densely
worked. **Contribute via a distinct coordinated angle, not a fork.**

## Front B — q₀ / W_λ substrate derivation (Subgoal-2)

Absolute m_p/m_n/m_μ targets sit **below** the CAL-2 floor (~780 ppb); no
calibration reaches them. Closure = deriving q₀ from the substrate, which
reduces (s5-so3 keystone) to the **colored Σ(2,3,5) WRT / `E_q(2)` q-Bessel
q-series whose q₀-evaluation must reproduce `W_λ`** (owner-opened-for-all
2026-07-11).

- **Self-conjugate sector — CLOSED exactly, continuation-free** (PR #4084,
  `KeystoneElectronBlockExact.lean`): on a self-conjugate block `c(λ)=0` ⇒
  `θ_λ = 1` for every q ⇒ `bwS0Concrete = S₀` exactly; flagship = the physical
  **electron block `[3,1,1]`**, value `[3]_q[4]_q/[2]_q`. **This survey
  independently re-verified that file lean-direct exit 0, sorry-free, against
  current `main`** (full 10-module QOU cone recompiled on the restored
  `lake-cache/qou-v4-24-0` oleans) — closing PR #4084's "full lean-direct
  blocked in-sandbox / CI to confirm" flag.
- **Open piece:** the non-self-conjugate blocks (`c(λ)≠0`, `θ^f≠1` at q₀>1) —
  the archimedean fibre continuation of the root-of-unity modulus out to q₀>1.
  Research-grade.

## Bottom line

- The literal "1 ppQ" (L1) is **done**.
- The L2 path is **two open research programmes**: GGM w(q) (Front A, closes the
  Q_β trio) and WRT q₀/W_λ (Front B, closes absolute masses). Both are
  multi-session, anti-fit-gated, and actively worked in parallel.
- The **constraint/parity layers of both are saturated** (KC16–20 + graded-split
  on A; self-conjugate sector on B). There is **no cheap single-session accuracy
  brick left** — a "derivation" produced now would be the guess the ledgers
  explicitly warn against. Honest role for a cache-equipped session: **discharge
  verification-pending flags** (done here for the electron-block keystone) and
  **narrow the derivation family** from the constraint side, not fabricate a
  bridge.

Scope: survey + one lean-direct verification. No fit; no c_k value; nothing
wired; no registry tier changed.
