# AJ arc reassessment + Borromean A-polynomial revival (2026-08-29)

Reassessment of the AJ-Conjecture / Borromean colored-Jones arc after a
~7-week gap, and revival of its one surviving open piece. Supersedes the
stale branch `claude/aj-conjecture-qou-uz5m6x` (PR #3470 **closed without
merging**).

## Reassessment (what changed on main)

1. **The branch is superseded.** Main carries a *fuller* copy of the whole
   AJ toolchain (`aj_*`, `borromean_qzeil_*`, `borromean_recurrence_crt_driver.py`,
   the whitehead-diagonal-recurrence witnesses the old branch never had);
   `git diff origin/main <old-tip>` on the AJ files is net −87 lines. The old
   branch adds nothing main lacks.

2. **The c_k physics hope is refuted-in-class — independently, on main.** The
   only reason colored-Jones q-holonomy mattered to the physics was the hope
   that it would *deliver the Q_β `c_k` truncation constants*. Main's 2026-07
   c₃-wall capstone proved the odd D-ladder **non-holonomic** (KC22) and then
   **withdrew** the resurgent/Écalle inference (`κ = 0`, 2026-08-09). Any `c_k`
   closure therefore lies **outside every holonomic class** — the class in which
   an AJ-style recurrence lives. `ck-dk-canonical-registry.md` still lists the
   kernel / f-map as the OPEN keystone.

   Scope (per AGENTS.md "refuted / ruled out" discipline): this is a
   **scope-limited negative backed by a proved invariant** — the c_k constants
   are excluded from the *holonomic* construction class (KC22 is proved), **not**
   excluded from non-holonomic closures. The AJ→c_k *bridge* is dead; a c_k
   closure by other means is not.

3. **What survives is pure knot theory, decoupled from the physics.** The one
   unfinished *novel* object is the explicit Borromean diagonal-recurrence
   operator and its `q → 1` limit — a candidate **Borromean A-polynomial**
   (diagonal restriction), not in the literature. It feeds no mass/binding
   observable. Pursued here for its own sake.

## The surviving piece — status on main

- **Existence certificate (green):** a q-difference operator annihilating the
  diagonal tower `J_{B,n}` exists at order `r=5`, `m`-window `W=13`
  (`borromean-diagonal-recurrence-hunt.witness.json`).
- **q-Zeilberger route (negative):** `borromean-qzeil-*` all report `found:
  False` — no clean low-order telescoper in the searched ansatz shapes
  (over-rich op-projection, `r ≤ 7` exhausted).
- **Explicit reconstruction (not green):**
  `borromean-diagonal-recurrence-reconstruct.witness.json` →
  `reconstructed: False`. The `(6,11)` canonical coefficients are rational
  functions of q-degree up to 252 (median 208). The ill-conditioning was
  **fixed** (hint-bisect + modal-degree CRT consensus); the *only* remaining
  blocker is **environmental** — the multi-prime sample needs a multi-hour
  uninterrupted run, which container reclaim has killed on every attempt.

## Approach (this branch)

Break the environmental blocker with a **reclaim-safe** run:

- `borromean_operator_reconstruct_laptop.py` is per-prime resumable
  (`load_ckpt` → `resuming: N primes`, atomic per-prime save) at `DEG_CAP=320`.
- **Resume from main's committed prime-0 checkpoint** (184 columns, max
  degree 252 — reusable as-is).
- **Commit the checkpoint after each prime**, so any container reclaim resumes
  from the last committed prime instead of restarting.
- The CRT lift is attempted after every prime `≥ 2`; the run stops as soon as
  the integer coefficients lift. On success: exact symbolic annihilation check
  on the tower, then `q → 1` for the candidate A-polynomial generator.

Deliverable: the explicit operator + Borromean A-polynomial, or — if the
coefficient height proves too large for the prime pool — an honest
`primes_used` ceiling recorded in the witness.
