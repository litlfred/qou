# Next threads — owner-prioritized handover (2026-06-06)

Owner picked **2 → 1 → 3 → 4** as the queue after the Q_β `c_3` thread closed
(collapse-cancellation **refuted**, PR #1905; residue-A narrowed to the f-map /
anchor-dependent brane-tower level). Each thread below has a **de-risked entry
point** so a *fresh focused session* starts cold and runs fast (one tranche per
session — long mega-sessions are the observed failure mode, AGENTS.md).

---

## Thread 2 (TOP) — per-knot `VolDensity(K)` wire-up (the +2.89% headline gap)

**Goal.** Replace uniform `Vol(𝓑₃)` with per-knot `Vol(K)` so the mass table
stops carrying the +2.89 % (m_p) → +3.73 % (¹²C) error.

**The bug (canonical audit):** [`2026-06-02-vol-usage-audit-uniform-vs-per-knot.md`](../audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md)
— **64 atom-touching scripts** use `vol_density_borromean(q)` (uniform `Vol(𝓑₃)`); only 2 use the per-knot path.

**Infra already exists:** `_li_2_q_util.py::vol_density_per_block(vol_K, tr_M_K, q)`
(line 393) takes `vol_K` explicitly; the uniform shortcut is `vol_density_borromean`
(line 303, its own docstring labels it "global-scalar collapse, NOT the paper's
per-block sum"). Sole consumer: `vol_density_per_block_wiring.py` (testbed).

**The gate — `Vol(K)` per atom:**
| atom | `Vol(K)` | status |
|---|---|---|
| p, n (A=1) | `8·G = 7.328` | ✅ uniform IS correct here |
| D (A=2) | `Vol(6₂)` (fixed link) | ✅ **tractable — the concrete first step** |
| T, ³He, ⁴He (A≥3) | `Vol(β_atom)` | 🔴 **heuristic/open — §9.3 link-volume assignment ⇒ couples to Thread 4** |

**First concrete step (fresh session):** demonstrate the **deuteron** per-knot
`VolDensity` — `vol_density_per_block(Vol(6₂), tr_M(β_D), q₀)` vs the uniform
`vol_density_borromean` — and show the error drops from +2.86 % toward the AME value.
Then migrate the *mechanical* path (`vol_density_borromean` → `vol_density_per_block`)
for p/n/D only; A≥3 waits on Thread 4. (Machinery is fragile under ad-hoc
`PYTHONPATH` — run from `computations/`.)

---

## Thread 1 — Φ₂ categorical derivation (finish the residue-A keystone)

**Goal.** Derive **Φ₂** (`= −c₃/√2 = a₁/√2`, the kernel's bar-odd leading
coefficient) from the SW-residue / Hoefsmit `H₃(q)` kernel — the surviving
residue-A direction after #1905's refutation.

**State:** #1900 (merged) pinned `a₁` **bar-odd** + **depth ≥ 2** + refuted
constant-depth-2; the Φ₂ *value* is the open frontier (#1871's SW-residue).
The **Φ₂ = bar-odd reconciliation** (Φ₂ swing = c₃ swing) is on main (PR #1895).

**Entry point:** the merged #1900 kernel-constraint Lean lemmas
(`QOU.QBeta…` c_k-recursion) + the SW-residue period machinery
(`sw-period-residue-sum.lean`, `compute(C4,C3)` SW-period residue weight on main)
+ this session's Hoefsmit access (`hecke_character_symbolic.hoefsmit_matrices_symbolic`).
**Caveat:** research-grade, multi-session, may not close. Coordinate with #1900/#1871.

---

## Thread 3 — Lean §9.4 debt (L-1 / L-2 / L-3)

**Goal.** Formalize the cheat-sheet §9.4 backlog (classical + published, just not
in Lean): **L-1** Schur character-orthogonality ⇒ `y_λ` uniqueness; **L-2**
central-idempotent orthogonality `π_λπ_μ=δπ_λ`; **L-3** per-λ Frobenius
block-orthogonality.

**Entry point:** `QOU.Hecke.Wedderburn` / `wedderburn-as-noncomm-fourier.lean`;
refs **Mathas (1999) §3.43**. Route under the proof-integration-watcher queue.
**Env:** needs a lake build — restore from `lake-cache/qou-v4-24-0` (the cache
cold-restore re-clones Mathlib; budget the ~20-min source build, per this
session's experience). Most tractable of the four once the env is up.

---

## Thread 4 — binding A≥3 many-body series (the other §9.2 frontier)

**Goal.** Close the §9.3 open items: the **canonical link-volume assignment** per
nucleus + the **`ρ·A` scale rule** (why ρ=1 at A=2 but ρ=2A at A=4), reconciling
the pairwise (2-body) and whole-nucleus (4-body magic-A, ⁴He +5.87 %) decompositions.

**State:** *very active* — keystone-E q-difference kernel, `lem:bond-order-eq-jet-degree`,
SW-residue hyperbolicity gate (L4) all merged this week. **This is the per-atom
`Vol(K)` Thread 2 needs for A≥3** — so 2 and 4 are coupled.

**Entry point:** the binding cluster (open PRs #1778, #1789, #1784) + the merged
keystone-E content. **Caveat:** crowded with siblings — `/coordinate` first.

---

## Coupling map

```
Thread 2 (p/n/D)  ── independent, concrete ──►  ship first
Thread 2 (A≥3)  ◄── needs Vol(K) ──  Thread 4 (link-volume assignment)
Thread 1 (Φ₂)  ◄── SW-residue ──►  #1900 / #1871 kernel frontier
Thread 3 (Lean debt)  ── independent, lake-enabled ──►  any time
```
