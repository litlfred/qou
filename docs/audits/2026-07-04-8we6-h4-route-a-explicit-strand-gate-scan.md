# 8we6 — H₄ route-A explicit-strand build: both fixed-coupling 4th-strand routes move the trusted rungs (scope-(a))

**Date:** 2026-07-04 · **Bean:** `8we6` (genuine c₄ rungs → Casoratian W₃ sign test)
· **Axis:** Q_β 1ppQ achievable arm — H₄ `c₄^even` rung
· **Tier:** measured (exact-rational s-series ladder; the H₃ reference reproduces
`c₂^even=−8.00641`, `c₃^even=+86.66116` exactly, validating the harness)
· **Verdict:** **scope-(a) negative** — the two *explicit fixed-coupling* 4th-strand
constructions (lepton, brane-tower) **fail the stability gate**; this does **not**
exclude the 4th-strand ingredient (see §Scope).

## What was built

Route B (re-decompose the unchanged H₃ element at λ⊢4) is machine-checked-pruned
([`H4RouteBBranchingPrune.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/H4RouteBBranchingPrune.lean),
PR #3273). Route A is the surviving path: a genuine `c₄^even` rung needs an H₄
object with **σ₂-support** (a word touching a 4th strand).

New shared machinery
[`qbeta_h4_nucleon_assembly.py`](../../computations/qbeta/qbeta_h4_nucleon_assembly.py):
a headless, n-agnostic port of the Gröbner–Shirshov reducer + crossing algebra
from `free-neutron-decay.py`. The nucleon "net" functional the Q_β ladder reads
is the **augmentation** (counit) of the reduced NF, `net_side(q)=Σ_w coeff_w(q)`;
`Δ(net)=net_neutron−net_proton`. **Self-test: reproduces the committed
`free-neutron-decay.witness.json` Δ(net) exactly** (symbolic, all of
net_neutron/net_proton/Δ(net)) for the 3-quark H₃ object.

Two explicit 4th-strand routes (the owner-chosen framings), each `B₃ · Π
crossing(type_i,type_j; gen=i)` over a **4-element** type list — adding pairs
(i,3) at gens {0,1,2}, i.e. genuine σ₂-support:

- **Lepton** — 4th strand carries the emitted β-decay lepton, weak u–d-averaged
  coupling `σ_gen − (q−q⁻¹)/2`. Types `[u,d,d,e]` (n) / `[u,u,d,e]` (p).
- **Brane-tower** — 4th strand bare Hopf coupling `σ_gen` (the `crossing()`
  else-branch). Types `[u,d,d,b]` / `[u,u,d,b]`.

## Result (the stability gate, operationalized)

Exact-rational s-series ladder (`s=q−1`, `u=b·ℏ_q²`), c_k at `s^{2k}`, identical
to [`qbeta_c3even_exact_sseries_probe.py`](../../computations/qbeta/qbeta_c3even_exact_sseries_probe.py).
Scan [`_h4_route_ladder_scan.py`](../../computations/qbeta/_h4_route_ladder_scan.py)
(≈300 s/object, sympy exact):

| object | c₂^even | c₃^even | c₄^even | max word len |
|---|---|---|---|---|
| **H₃ (reference / gate)** | **−8.00641** | **+86.66116** | −1819.74 | 3 |
| H₄ lepton (g=1) | −6.83974 | +73.44626 | −1561.58 | **4** |
| H₄ brane (g=1) | +3.99359 | −65.50271 | +743.15 | **4** |

**The harness is validated** — the H₃ reference reproduces the trusted
`c₂^even=−8.00641`, `c₃^even=+86.66116` exactly (and the known scale-check
`c₄≈−1819.74`).

**Both explicit routes reach word length 4** (real σ₂-support — the c₄ rung *is*
representable) but **move the lower rungs**: lepton shifts c₂/c₃ by ~15 %, brane
sign-flips them. Per the gate stated in
[`2026-07-03-8we6-h4-route-b-structural-prune.md`](2026-07-03-8we6-h4-route-b-structural-prune.md)
§"What this forces on route A" — *"if lower rungs move, the object is wrong"* —
**a 4th strand appended at full physical coupling is not the right object.** The
same σ₂ crossing that creates the length-4 word feeds back into c₂,c₃.

## Scope (STRICT — this is a scope-(a) negative, not a structural exclusion)

Per AGENTS.md §"Before declaring refuted": this is **(a) scope-limited** — *the
explicit appended-strand construction, at full coupling, alone, does not preserve
the rungs.* It constrains the **coupling magnitude/combination**, **not** the
4th-strand **ingredient**. No proved invariant forbids a 4th strand; two
refinements survive and are the owner-gated modelling calls the route-B-prune
audit already flagged:

1. **Coupling-perturbative reading.** The gate says "in whatever *limit* removes
   the coupling." The interpolated crossing `C(g)=(1−g)·I+g·P` gives H₃ **exactly**
   at g=0 (verified). The sharp, decidable question is the **g→0 linear
   response**: is the 4th strand a *pure-c₄* perturbation (`dc₂/dg|₀=dc₃/dg|₀=0`)
   or does it contaminate the lower rungs already at linear order? Tested in
   [`_h4_g_linear_response.py`](../../computations/qbeta/_h4_g_linear_response.py)
   (result appended below on completion).
2. **Brunnian via the operator-selection SDP** (owner directive "brunnian through
   SDP and G"). Structurally *different* from appending a strand: select the
   symmetric **bar-even** singlet channel of the n=4 cup-diagram space (Gram
   `G=[[δ²,δ],[δ,δ²]]`, δ=[2]_q; the antisymmetric eigenvector is the bar-odd
   channel) via `solve_psd_operator_selection_sdp`, reading the active-set
   (`y_star>0` = the saturated channel). Does not touch c₂,c₃ because it is a
   different object. The SDP-channel → c₄^even ladder linkage is the remaining
   modelling decision.

## Kill-criterion status

Nothing is refuted in scope-(b). The **appended-strand-at-full-coupling** class
is set aside (scope-(a)); the coupling-perturbative and SDP-channel routes remain
open and are the productive next moves.

## Provenance

- Assembly + self-test: `computations/qbeta/qbeta_h4_nucleon_assembly.py` (H₃
  reproduction exact).
- Ladder scan: `computations/qbeta/_h4_route_ladder_scan.py` → table above.
- g-response: `computations/qbeta/_h4_g_linear_response.py`.
- Gate reference values: `qbeta-c3even-exact-sseries.witness.json`
  (c₂/c₃^even), audit `2026-07-02-1jrh-c3even-exact-measurement.md`.
