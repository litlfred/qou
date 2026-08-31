---
# qou-vsqh
title: 'GAP: derived_bond_graph_binding computes in float64 and emits a witness'
status: completed
type: task
priority: normal
created_at: 2026-08-31T03:20:02Z
updated_at: 2026-08-31T03:36:57Z
---

Found while checking `qou-x0su`. Not fixed there — it is a producer change with a
witness behind it, so it wants its own PR.

`computations/derived_bond_graph_binding.py` is a **live, witness-emitting**
producer (`derived-bond-graph-binding.witness.json`) and it computes in float64
end to end:

    line 77:   q0, h, me = float(q0), float(h), float(me)
    line 99:   e_bond = {k: E0 * math.log(1.0 / v) for k, v in f.items()}
    line 133:  e_bond_bar = {k: 0.5 * E0 * math.log(1.0 / v) ...}
    line 170:  B_chain    = E0 * sum(math.log(1.0 / f[b]) for b in cb)
    line 171:  B_complete = E0 * sum(math.log(1.0 / f[b]) for b in comp)
    line 157:  ta = float(r["tr_M_atom"].strip("()").split("+")[0])

So the substrate constants are downcast at entry, the per-bond energies and both
bond-graph bindings accumulate through `math.log` over a `sum()`, and the
upstream traces are parsed back out of strings with `float()`. AGENTS.md
§"PROBES ARE NOT EXEMPT" items 1 and 2 name exactly this shape, and the witness
means the numbers are recorded rather than merely printed.

**Why it matters beyond hygiene.** This producer is the corpus's free-energy
channel for the chain-vs-complete-graph binding comparison — the object
`QOU.Mass.CoordinationSaturation` covers. The A-dependence there is a sum of
`C(A,2)` logs, so the accumulation is the part float64 degrades, and it is the
part the saturation verdict is read off.

**Fix at the producer:** carry `q0`, `h`, `me`, `delta` as `mpmath.mpf` from
their sources, replace `math.log` with `mp.log`, replace `sum(...)` with
`mp.fsum(...)`, and read the upstream traces as `mp.mpf(str(...))` rather than
`float(...)`. Then re-run and refresh the witness. Do NOT baseline it.

Second, unrelated defect in the same file, cheap to fix in the same PR: the
docstring at line 18 declares `z = 1/(q^½+q^{-½})` (**convention C**) while line
78 computes `q0**3/(q0**2+1)` (**convention D**). The body is correct; the
docstring is stale. Same shape as the `markovZc` docstring collision recorded in
`qou-961o` — name/doc agreeing with each other and both wrong, only the body
right.


## FIXED — PR #6338 (branch `claude/vsqh-bond-graph-float64-2026-08-31`)

Two-stage fix, and the second stage is the one that mattered.

**Stage 1, the arithmetic.** `math.log` → `mp.log`, `sum()` → `mp.fsum`,
`prod_chain` seeded `mp.mpf(1)`, upstream traces `mp.mpf(...)` not `float(...)`,
`0.5` → `mp.mpf(1)/2`, `set_compute_dps()` at module scope, witness serialized
with `_precision.fmt` instead of `round(x, 4)`.

Residual after stage 1: **still 5.6e-16**. Float64-shaped at 70 dps — the tell,
and easy to have shipped as "fixed".

**Stage 2, the inputs.** `q_parameter.Q` and `HA` are Python **floats**
(measured: `Q = 1.1099785827513808`, 17 digits), so `mp.mpf(str(Q))` faithfully
preserves float64 and creates no precision that is not there. Now reads
`Q_50_DIGIT_STR` and derives `h = q − 1/q` from it.

| derivation residual | |
|---|---|
| before | 5.6e-16 |
| arithmetic only | 5.6e-16 (no gain) |
| + inputs | **3.66e-31** |

**raw-float64 ratchet: 108 → 0, fully drained.**

**The verdict does not move.** Every physics number unchanged — `B_chain(D)`
2.8332 → 2.8331625720…, `miss_chain(4He)` 3.259 → 3.2592474303…, chain miss
range 0.7852–3.259×, complete 0.6236–1.647×. What changes is the evidence for
the `f_bond = c·z + d` derivation the producer's headline calls EXACT: it was
resting on agreement at the float64 floor and now has 31 digits behind it.

Stale docstring also fixed (line 18 declared convention C over a D body).

**Method note worth keeping.** The diagnostic that found stage 2 was noticing a
residual sitting at exactly the float64 floor *after* the arithmetic was
migrated, then checking the upstream witness (50 digits, so not the limiter) and
only then the inputs. A residual at 1e-16 in an mpmath producer is a claim that
something upstream is still f64 — it is not a precision result.

**Process note.** This bean was created on the `qou-x0su` branch, so switching
branches took the file out of the tree and a `beans update` here silently wrote
nothing (`beans show` reported "bean not found" and the tree stayed clean).
Restored with `git checkout <other-branch> -- .beans/<file>` before updating.
Beans are per-branch files; a cross-branch update is a no-op that does not
announce itself.
