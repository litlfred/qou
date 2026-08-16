---
# qou-brg3
title: size the isospin-T interface replacement from the deuteron's 27.34 percent one-bond miss
status: todo
type: task
created_at: 2026-08-16T00:11:01Z
updated_at: 2026-08-16T00:11:01Z
---


## Arc status 2026-08-16 — Wenzl level 2 reframes the H₆ result

The selection principle this bean was looking for is supplied by the framework:
convention D **is** SU(2) Wenzl level 2, so `y_λ = 0` on every ≥3-row partition
and the two-nucleon trace sees **4 of 11 blocks**. Three of the four unbind in
all three systems. Details + the conjugate-pair consequence: `qou-8zjc`.

Corrections this forced on my own committed work, all landed:

* the "7 of 11 sign-flipped blocks are the deuteron's channel" obstruction —
  those blocks have `y = 0` and are not in the trace. Residue is one block,
  `(3,3)`, unexplained.
* a guard against reading "3 of 4 unbind" as "nearly unbound": the aggregate is a
  ratio of sums, not a mean of ratios, and the exact trace ratio is `1/μ` to
  `1e-30` — the diproton is still bound at +2.54 MeV.
* `μ±` verified to BE the n=2 Wedderburn weights (`0.7527021133`,
  `0.2472978867`), which I had asserted without checking.

Still open on this bean: the isospin-`T` sizing itself. It is better posed than
before — the surviving-block structure is now known and small — but no magnitude
statement is available until `qou-jtfo` (per-block reconstruction) closes.
