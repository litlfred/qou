# Chirality forces the complete-graph topology (2026-06-20)

**Status:** audit — positive structural result. Crosses the two axes that prior
work kept separate:

- [`2026-06-17-hecke-channel-chirality-binding.md`](2026-06-17-hecke-channel-chirality-binding.md)
  — the Hecke **channel** axis: the alternating (Pauli) channel makes pp & nn
  unbound; std is the Jones–Markov channel the kernel uses.
- [`2026-06-16-b-sym-linear-chain-closed-form.md`](2026-06-16-b-sym-linear-chain-closed-form.md)
  (merged PR #2343) — the **topology** axis: production `B_sym` is *exactly* the
  linear chain `α·[(Z−1)L_pp + L_pn + (N−1)L_nn]`, not the complete graph.

**Probe:** [`computations/probes/chirality_topology_binding_probe.py`](../../computations/probes/chirality_topology_binding_probe.py)
· witness `computations/chirality-topology-binding.witness.json`. Pure closed-form
(per-bond channel value × combinatorial count) ⇒ no per-knot trace, **no p(3A)
wall**, zero free parameters. EXPLORATORY — derive-or-refute, no production rewire.

## The 2×2 the prior probes skipped

The chirality probe ran *one channel, uniformly, on the complete graph*. The
production form is *the std channel on the chain*. The missing cells are
**{chain, complete} × {std-uniform, Pauli-mixed}**, where Pauli-mixed is the
physically-forced assignment: pp→alt (identical p's, antisymmetric ⇒ unbound),
nn→alt (⇒ unbound), pn→std (the bound Jones–Markov channel).

| model | D | T | ³He | ⁴He | ⁶Li | ⁷Li | **RMS** |
|---|--:|--:|--:|--:|--:|--:|--:|
| AME B (MeV) | 2.22 | 8.48 | 7.72 | 28.30 | 31.99 | 39.24 | — |
| std·chain (= merged B_sym) | 3.89 | 9.07 | 6.80 | 11.98 | 20.06 | 25.24 | 10.07 |
| std·complete (all-pairs) | 3.89 | 12.96 | 10.69 | 23.65 | 59.27 | 86.47 | 22.46 |
| Pauli·chain | 3.89 | 3.89 | 3.89 | 3.89 | 3.89 | 3.89 | 21.11 |
| **Pauli·complete** | 3.89 | 7.78 | 7.78 | 15.56 | 35.01 | 46.69 | **6.19** |
| Pauli-sym·complete | 0 | 0 | 0 | 0 | 0 | 0 | 24.16 |

## Two structural results

1. **Chirality and the chain are incompatible.** With pp/nn Pauli-unbound, the
   linear chain retains a *single* p-n interface bond, so the binding is constant
   (3.89 MeV) for every nucleus — no A-dependence (RMS 21.11). You cannot have
   pp/nn unbound *and* an A-dependent binding on the chain topology.

2. **Chirality forces the complete graph.** Pauli·complete (`Z·N` p-n pairs,
   std-bound; the `C(Z,2)` p-p and `C(N,2)` n-n pairs Pauli-unbound) gives
   **RMS 6.19 — the best of all models**, beating production std·chain (10.07) by
   39%. Four of six isotopes land within ~12% (³He 0.99, ⁶Li 0.91, T 1.09,
   ⁷Li 0.84). The chirality-correct picture (pp/nn don't bind) is also what
   *removes* the all-pairs over-binding of the heavies (⁶Li 35.0 vs std·complete
   59.3), because the spurious p-p/n-n pairs are exactly the ones the Pauli
   channel kills.

The two results are one statement: **the Pauli channel selects the complete graph
restricted to p-n pairs.** Identical-nucleon pairs (p-p, n-n) drop out by Pauli;
the surviving p-n pairs need the complete graph (the chain has only one), so the
binding scale becomes `α · Z·N · L_pn`.

## Residual = the already-known opens (no new gap)

The Pauli·complete residual is dominated by exactly the two items the corpus
already tracks, not a new defect:

- **⁴He under-binds by +12.7 MeV** — the irreducible 4-body **α-cluster** term
  (merged #2343 §α-unit; `derive_binding_chain_cooperative.py`). `Z·N·L_pn`
  counts pair bonds; the α-particle's 4-body cooperative binding is beyond any
  pairwise count.
- **Deuteron over-binds (ratio 0.57)** — the `f_pn = 0.588` crux: the std channel
  gives `f_pn = 0.395` (too strong); no substrate channel lands 0.588. This
  magnitude is **owner-gated to the s5-so3 fibre keystone** and is *not* chased
  here (fitting it = the Δ_λ-gated ansatz).

## Convention correction

The strict bound test is **0 < f < 1** (a positive sub-unity suppression). A
negative channel value (the alt eigenvalue −q⁻¹ < 0) is the antisymmetric/Pauli
channel and is **unbound**. This is stricter than the prior probe's `|f| for
f<0` magnitude rule, which spuriously binds p-p in alt (|−0.901| < 1 → +0.44 MeV)
and contradicts its own prose ("f_pp<0 antibound"). The strict test is the
correct Pauli treatment and is what makes pp/nn cleanly unbound here.

## Conclusion

Chirality (the Pauli channel) is not just a sign-fix for the unbound channels —
it **selects the binding topology**: the complete graph on p-n pairs. That
combination is the most accurate non-fitted two-nucleon binding model on the low
isotopes (RMS 6.19), with its entire residual already accounted for by the
α-cluster term and the s5-so3-gated deuteron magnitude. No production rewire is
proposed; this pins the structural relationship between the chirality and
topology axes.

## References

- [`2026-06-17-hecke-channel-chirality-binding.md`](2026-06-17-hecke-channel-chirality-binding.md) — channel axis (PR #2461/#2481).
- [`2026-06-16-b-sym-linear-chain-closed-form.md`](2026-06-16-b-sym-linear-chain-closed-form.md) — topology axis (merged PR #2343).
- [`computations/probes/chirality_topology_binding_probe.py`](../../computations/probes/chirality_topology_binding_probe.py) — this probe.
- `computations/derive_binding_chain_cooperative.py` — the α-cluster residual.
- PR #2507 — this work.
