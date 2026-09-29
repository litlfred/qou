---
# qou-zryq
title: The NF inter-nucleon block encodes a bond COUNT, not a coordination graph — so k is not derivable from it
status: completed
type: task
priority: normal
created_at: 2026-08-31T03:54:56Z
updated_at: 2026-08-31T03:55:41Z
---

## Measured (branch `claude/nf-bonds-are-counts-not-graph-2026-08-31`)

Follows #6345, which closed by asking for "a `k` derived from the substrate —
from the braid word's own geometry — and then COMPARED to the plateau." This
answers it: **the NF word has no geometry in its inter-nucleon block to derive
one from.**

**The observation.** Every inter-nucleon factor in `build_atom_nf_sym` is applied
at **gen 0**, for every pair `(prev, k)`. Nothing in the factor records *which*
two nucleons the bond joins — only the pair's TYPE, via `d ∈ {0, −h, −h/2}`.

**Why that is decisive.** All those factors are polynomials in the same generator
`σ₀`, so they commute, so `∏_bonds (σ₀ + d_bond)` depends on the bond set only
through the multiset `(n_pp, n_pn, n_nn)`.

**Measured, not argued** (exact Laurent arithmetic, nothing evaluated at any q):

    order-invariance      40/40 shuffles bit-identical, on each of
                          4He, 6Li, 9Be, 12C, 14N (6..91 bonds)
    structure-invariance  a degree-4 graph (5 pp, 4 pn, 3 nn) and a DIFFERENT
                          pairing with the same counts -> bit-identical
                          the complete graph (3,9,3) -> differs, by COUNT only

**Consequence for `qou-brng`.** "Complete graph vs bounded degree" is expressible
in this producer only as a difference in bond COUNT. A degree-`k` graph and the
complete graph are distinguishable solely by having different type counts, never
by their structure. So a coordination *number* cannot be derived from this word,
and that is a property of the encoding rather than a gap in anyone's search.

**Where the geometry does live.** `atom_braid_word_3A` places its pp/nn/pn
crossing at **gen 3k+2** — a genuine bridge between strand blocks `k` and `k+1`.
Adjacent-only, hence `A−1` bonds **by construction** rather than by choice. That
is the word to ask geometric questions of, and it explains the split #6304
measured: the NF word's `C(A,2)` is a repeated scalar factor, the 3A word's
`A−1` is a strand bridge.

**Scope (a).** Nothing here says the framework cannot have a coordination graph,
and nothing here touches `atom_braid_word_3A`.

Probe: `computations/substrate/nf_inter_nucleon_is_a_count_not_a_graph_probe.py`.
The probe returns exit 1 if the commutation claim fails, so its conclusion cannot
print over a failed measurement.
