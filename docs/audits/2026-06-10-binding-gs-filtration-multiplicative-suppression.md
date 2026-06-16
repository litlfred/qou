# Binding Δ_λ gate — GS-filtration shows multiplicative per-bond trace suppression (2026-06-10)

**Status:** exploratory structural finding (no production rewire). Owner
directive: *"break up computation into components, look at GB [Gröbner–
Shirshov] filtration/order"* + *"attack the Δ_λ(K) gate / energy-scale — keep
track of active sets through knot operations as nucleons constructed."*

Probes (PR #2089):
[`gs_filtration_binding_components.py`](../../computations/gs_filtration_binding_components.py)
/ `gs-filtration-binding-components.witness.json`, and
[`delta_lambda_energy_scale_extensivity_probe.py`](../../computations/delta_lambda_energy_scale_extensivity_probe.py)
/ `delta-lambda-energy-scale-extensivity.witness.json`.

## Setup — the binding trace, built nucleon-by-nucleon

The canonical binding (`binding_canonical.py`, Jones–Markov trace) is
`B = Q_β · Δtr`, `Δtr = tr_M(W_free) − tr_M(W_atom)`. The atom braid is built
nucleon-by-nucleon: nucleon `i` is a B₃ core on strands `[3i, 3i+1, 3i+2]`
(generators `σ_{3i+1}, σ_{3i+2}`); the **bridges `σ_{3i}` are the A−1
inter-nucleon bonds** (chain topology). `W_free` = cores only; `W_atom` = cores
+ bridges, so **Δtr is carried entirely by the bridge (bond) components**.

## Finding 1 — the GS normal form factorizes over bonds (binomial)

GS-reducing `W_atom` (length-then-lex order: R1 Hecke `σ²→(q−q⁻¹)σ+1`, R2
far-comm, R3 Yang–Baxter) and grading NF terms by **bridge-count** `k` (how
many distinct `σ_{3i}` a term contains) gives a **binomial** term count
`C(A−1, k) · base`:

| nucleus | A | bonds | term counts by bridge-count k |
|---------|---|-------|-------------------------------|
| D | 2 | 1 | `[16, 16]` = 16·[1,1] |
| T | 3 | 2 | `[64, 128, 64]` = 64·[1,2,1] |
| ³He | 3 | 2 | `[32, 64, 32]` = 32·[1,2,1] |
| ⁴He | 4 | 3 | `[128, 384, 384, 128]` = 128·[1,3,3,1] |

The bridges far-commute (`|3i − 3j| ≥ 3 ≥ 2`, R2) so they are **GS-independent
generators** — the NF is a **product** over bonds, not a sum.

## Finding 2 — multiplicative per-bond trace suppression, f ≈ 0.39

The product structure makes the Markov trace factor. Measuring
`f = (tr_M(W_atom)/tr_M(W_free))^{1/bonds}`:

| nucleus | bonds | tr_atom | tr_free | f (per-bond) | log(tr_free/tr_atom) | Δtr (linear) |
|---------|-------|---------|---------|--------------|----------------------|--------------|
| D | 1 | 0.388 | 0.984 | **0.395** | 0.929 | 0.595 |
| T | 2 | 0.104 | 0.908 | **0.339** | 2.166 | 0.804 |
| ³He | 2 | 0.207 | 1.048 | **0.444** | 1.624 | 0.841 |
| ⁴He | 3 | 0.055 | 0.967 | **0.385** | 2.861 | 0.912 |

`f ≈ 0.39` (mean 0.391, spread 0.11) across all four nuclei ⇒

> **`tr_M(W_atom) ≈ tr_M(W_free) · f^{bonds}`** — each inter-nucleon bond
> suppresses the trace **multiplicatively** by ~0.39.

(The ³He `f=0.444` > T `f=0.339` at equal A=3 is the p/n composition —
³He = ppn, T = pnn — so `f` is weakly composition-dependent, not a universal
constant.)

## Finding 3 — the linear difference is intensive; the LOG-RATIO is extensive

The multiplicative law is the mechanism behind the whole Δ_λ gate:

- **`Δtr = tr_free·(1 − f^{bonds})` SATURATES** toward `tr_free ≈ 1` as bonds
  grow (`f^{bonds} → 0`). So `B = Q_β·Δtr` is **structurally bounded** by
  `Q_β·tr_free ≈ 0.78 MeV` — it can **never** be extensive, regardless of A.
  This is the GS-level derivation of the F2 saturation
  (`delta_lambda_energy_scale_extensivity_probe.py`: Δtr log-growth +0.21/A
  vs B_AME +1.27/A).
- **`log(tr_free/tr_atom) = bonds · |log f|` is EXTENSIVE** — additive over
  bonds, growing with A (0.93 → 2.17/1.62 → 2.86). This is exactly the
  `log|tr_M|` **scale gate** that #2078 found (binding gate quadratic/linear
  in A, R²≈0.9999), now mechanistically explained: the product-over-bonds NF
  becomes a sum-over-bonds under `log`.
- The **1-bridge ("independent bond") fraction** of the bond trace falls with
  A (D 1.00 → T 0.60 → ³He 0.62 → ⁴He 0.36): the bonds are GS-**correlated**
  (≥2-bridge terms grow), consistent with the product (not sum) structure.

## Diagnosis of the Δ_λ gate (energy-scale + form)

Combining with the energy-scale split
(`Δ_λ = (E_0/Q_β)·r(K)`, `E_0 = m_e/(q_0(q_0−1)) ≈ 4.186 MeV`):

1. **Energy scale** (deuteron, 1 bond): `r(D) = Δ_λ(D)·Q_β/E_0 ≈ 0.89 ≈ 1` —
   the 1-bond gap is almost entirely `Q_β` vs `E_0` (use `E_0`).
2. **Functional form** (A-growth): the residual `r(K) ∝ bonds` arises because
   `B = Q_β·Δtr` uses the **linear** trace difference (intensive, bounded)
   where the **extensive** invariant is `log(tr_free/tr_atom)`. The binding
   undershoot's growth with A is a **wrong-functional-form** signature, not a
   missing scalar.

So the productive direction is a binding built on the **log-ratio / scale-gate
observable** (extensive over bonds) at the **E_0** scale — which is precisely
the per-nucleus volume route (#2078, `log|tr_M|` → `Li_2^q` volume image) and
the per-bond operator combiner (#2080). This corroborates both from the GS
side.

## Discipline / caveats (STRICT)

- **NOT a fitted Δ_λ closure / not a 7th ansatz.** `f` varies 0.34–0.44 with
  p/n composition; `B_AME/log(tr_free/tr_atom)` is not constant
  (2.4 / 3.9 / 4.8 / 9.9) — the per-bond *energy* is not universal. This is a
  **structural diagnosis of the functional form** (linear → saturating;
  log → extensive), consistent with the already-established #2078 scale gate,
  NOT a new closed form for Δ_λ.
- The braid wires **A−1 chain bonds**, not the physical `C(A,2)` (e.g. ⁴He: 3
  bridges vs 6 tetrahedron bonds) — a known under-wiring that compounds the
  ⁴He under-binding; the topology of the bond graph is a separate open item.
- Convention: the binding traces are the **averaged-crossing** Jones–Markov
  trace (`binding_canonical`); the active-set caches (#2089 lossless matrix-M)
  are sign-only — used only for the few-row active-set illustration.

## Cross-refs

- F2 saturation / energy-scale split:
  `delta_lambda_energy_scale_extensivity_probe.py`.
- Scale gate (`log|tr_M|` in A): #2078 (`claude/atom-vhyp-workplan-2026-06-09`).
- Per-bond operator combiner: #2080 (merged).
- Lossless χ caches enabling the active-set view: #2089 commit `054efed7`.
