# Δ_λ gate — redesign along the master-formula / active-set route (2026-06-17)

**Branch:** `claude/tender-brahmagupta-17txfq` (PR #2405)
**Trigger (owner steer):** "look at how the other one was done — partition →
representation, active channel — hints from physics?" — i.e. attack the
cooperative α/shell binding (the Δ_λ gate) the way the *working* bound-state
observable (g_A) is computed, not via a per-partition content-count ansatz.
**Discipline:** derivation-route scoping; **no fit, no production rewire, no
witness.** This records the redesign + the honest obstacles, superseding a
content-multiplicity probe that was itself fit-adjacent.

## 1. The steer is right: binding is the one observable still on the raw trace

The framework already has a **master formula** for bound-state observables
([`prop:confinement-frobenius-reciprocity`](../../content/quantum-observable-universe/particle-interactions/confinement-frobenius-reciprocity.md)):

> ⟨O⟩_T = Σ_{i,j ∈ A*(T)} u_i* (G⁻¹)_{ij} ⟨O, b_j⟩

— the **Gram-inverse dual pairing** weighted by the **LP-active shadow prices**
`u_i* = y_i*`, on the active set `A*(T) = {i : y_i* > 0}` selected by the
confinement operator-selection LP. The prop is explicit that the **raw Markov
trace is NOT the physical expectation** of an observable (it is non-orthonormal
on the NF basis; dualisation needs `G⁻¹`), and that *only* the active channels —
the "most receptive sub-braids" — carry physical weight.

| observable | computed via | file |
|---|---|---|
| **g_A** (axial coupling) | **master formula** (G⁻¹ + LP active set) | [`borromean-axial-coupling.py`](../../computations/borromean-axial-coupling.py) |
| **binding** (the Δ_λ gate) | **raw trace defect** `E₀·(\|tr_M(W_free)\|−\|tr_M(W_atom)\|)` | [`binding_canonical.py`](../../computations/binding_canonical.py), [`conj:knot-factor-frobenius-pairing`](../../content/quantum-observable-universe/mass-theory/knot-factor-frobenius-pairing.md) |

So **binding is the one observable still computed the "wrong" way** (raw trace =
exactly what `B_sym` / the dashboard use). `prop:confinement-frobenius-reciprocity`
*asserts* binding is the `O=H` special case that "reduces to the known
expression in knot-factor-frobenius-pairing" — but that collapse is stated in a
**proof sketch and never verified**. If the collapse is *false*, the
`G⁻¹`+active-set structure the raw trace drops is precisely the missing
cooperative term — derived, not fitted. That is the live, non-fit question.

## 2. Live machinery + the partition→representation→active-channel datum

The machinery runs in-repo (`gram-matrix-dual.witness.json` 6×6 H₃ Gram +
`pyhecke.lp_dual_solver` + scipy). For the **proton 𝓑_3** (`n_target=1`):

```
active_set    = [0]            # only the identity channel 'γ'
shadow_prices = [1, 0,0,0,0,0]
⟨O_V⟩=⟨O_A⟩   = 2.9977   →   g_A = 1.000   (PDG 1.2754)
```

This is a concrete instance of "partition → representation → active channel" —
but a **degenerate** one: the LP selects only the identity, so the master
formula collapses and `g_A=1`. The script's own note: it "establishes the
correct STRUCTURE — the conjugation bug is gone — with refinement (proper
isospin projector on T) deferred." **The master formula is a scaffold, not yet
a finished predictor.**

## 3. Honest obstacles (critical-distance)

The route is the right *framing*, but it is a real research build, not a quick
win:

1. **Type mismatch — binding is not naturally a one-state ⟨O⟩_T.** The master
   formula gives the expectation of an observable `O` on a *single* bound state
   `T`. Binding is a **difference of traces of two different braids**
   (`W_atom` vs `W_free`). Reformulating it as `⟨H⟩_{T_atom} − Σ_k ⟨H⟩_{T_free,k}`
   requires **defining the categorical Hamiltonian `H ∈ H_{3A}(q)`** as a linear
   functional ("`H` acting diagonally on the NF basis", per the prop) — which is
   **not done**. The knot-factor conjecture sidesteps this by using the raw
   trace defect. *Defining `O=H` is the actual missing piece, and it is the
   prerequisite for everything downstream.*

2. **The v1 master formula is degenerate.** Even for the proton it gives
   active_set = {identity}, `g_A=1.0 ≠ 1.275`. The non-trivial content
   (categorical Clebsch-Gordan / isospin projector) that would make the active
   set richer is itself unbuilt. A binding computation inherits this gap.

3. **Atom-level Gram inherits the SAME p(3A) wall.** g_A uses the 6×6 **H₃**
   Gram (one nucleon). Deuteron binding needs the **H₆** Gram (720×720 entries
   `tr_M(b_i b_j)`); ⁴He needs **H₁₂** — i.e. the very `p(3A)` feasibility wall
   PR #2405 documents. So the active-set route does **not** dodge the wall for
   the heavy nuclei it is meant to explain; at best it reaches the deuteron / A=3.

4. **Physics hint (⁴He doubly-magic = closed shell = saturated active set) is
   appealing but speculative.** There is no evidence yet that the LP active set
   for the ⁴He atom braid "saturates" so as to produce the +16 MeV cooperative
   term; testing it needs the H₁₂ Gram (walled).

## 4. Verdict + concrete first step

The master-formula / active-set route **supersedes** the uniform-Δ_λ and
content-count ansätze (it is derivation-based, and it is how the framework's
*own* working observable is computed) — but it is **gated on defining the
categorical Hamiltonian `O=H`**, not on another coefficient search. It is the
right place to push *and* it is honestly a multi-step build, not a one-session
closure. It does not violate the no-7th-fit discipline because there is no fit
in it.

**Concrete, non-fit first step (tractable):** define `O=H` at the **H₃** level
and test the collapse claim — does the master-formula `⟨H⟩` for a single
nucleon equal the raw `|tr_M|`? Reuses the existing 6×6 Gram + LP (no new wall).

**The principled `O=H` candidate is the q-Casimir, not an invented operator.**
`knot-factor-frobenius-pairing` §"Relation to q-Casimir" already supplies it:
each Wedderburn block's character expands in q-Casimir eigenstates
([`def:q-casimir`](../../content/quantum-observable-universe/braids-and-knots/q-casimir.md))
with eigenvalue `[j]_q[j+1]_q` on the spin-`j` irreducible (the q-Laplacian /
energy operator on the Peter–Weyl component). So `O=H` = q-Casimir, acting
diagonally on the Wedderburn blocks by `[j]_q[j+1]_q` — a substrate-given
Hamiltonian, **no tuning**. This is exactly the "diagonal on the NF basis"
operator the master-formula prop names, made concrete.

- **Collapse holds** ⇒ the active-set route adds nothing for `O=H`; the raw-trace
  binding (B_sym) is already the master formula, and the cooperative term must
  come from elsewhere (α-cluster recursion as a separate additive object —
  the status quo).
- **Collapse fails** ⇒ the `G⁻¹`+active-set correction is real for energy, and
  scaling it to the H₆ deuteron (then testing the cooperative sign) is the live
  derivation of the missing term.

Either outcome is decisive and parameter-free — exactly the formalize-first
"cheap and decisive" test the discipline calls for before any wider build.

## 4a. H₃ probe result (2026-06-17) — the blocker is the degenerate LP active set

Ran the §4 first step:
[`computations/probes/delta_lambda_master_formula_h3_probe.py`](../../computations/probes/delta_lambda_master_formula_h3_probe.py)
(existing 6×6 H₃ Gram + LP; `O = C_q` both readings). Result — **decisive, and it
relocates the gate**:

- **LP active set for the proton = [0]** (identity `γ` only), shadow `u*=[1]` —
  the *same* degeneracy as the g_A v1 (`g_A=1.0`).
- **Consequence:** with `|A*|=1` at the identity, the master formula collapses to
  `⟨O⟩_T = (G⁻¹)₀₀ · tr_M(O)` — a constant rescaling of `tr_M(O)` that is **blind
  to the bound-state braid 𝓑_K**. Measured `master ≈ 3.00 × raw` *uniformly* for
  `O ∈ {1, C_q^{SU(2)}, C_q^{JM}}` (collapse "fails" only by that flat factor —
  no braid-dependent structure).
- **Root cause — the LP solver does not reproduce its own prop.**
  [`prop:operator-selection-lp`](../../content/quantum-observable-universe/mass-theory/operator-selection-lp.md)
  is explicit: the cost is `t_i = tr_M(b_i)` (universal, **by design** — feeding
  the braid was the wrong guess), and bound states are distinguished by
  `n_target` (proton ≈ 1.000, neutron ≈ 0.811). The prop claims the proton
  optimum is **`𝓑_3` with active set `{σ_0, L_-}`** (two channels, objective
  `tr_M(𝓑_3) ≈ 0.998`). But the live solver returns a **degenerate vertex**:
  `active = {γ}`, `primal_obj = 1.1e-10 ≈ 0` — it finds *lower* action than `𝓑_3`,
  so it does **not** select the Borromean braid. (Same call in
  `borromean-axial-coupling.py:101-104`; same degeneracy ⇒ `g_A = 1.0`.) The
  general operator-selection LP as implemented evidently lacks the constraint(s)
  that `prop:confinement-lp` uses to pin `𝓑_3` as the unique vertex — it admits
  a near-zero-action operator the confinement LP must be excluding.

**Verdict (relocates §3 obstacle #2 to the front):** the gate for the *entire*
master-formula route — binding **and** g_A — is **making the LP reproduce its
prop's confinement selection** (`𝓑_3`, active `{σ_0, L_-}`), i.e. fixing the
`solve_operator_selection_lp` / `prop:confinement-lp` constraint mismatch so the
active set is non-degenerate. It is **not** the cost vector (that is correctly
`TR_M`), **not** the `O=H` choice, and **not** the H₆ Gram — those are all
downstream. Until the LP selects `𝓑_3`, the master formula is a blind constant
rescaling (`master ≈ 3.00×raw` for every `O`) and cannot supply cooperative
binding. This is the cheap-and-decisive formalize-first outcome: one H₃ probe
re-pointed a multi-hour H₆ build at the actual upstream blocker — an LP-solver
correctness gap that also explains the stuck `g_A = 1.0`.

(Aside: the committed `gram-matrix-dual.witness.json` is itself stale at the old
q₀ — same q₀-repin class as the borromean witness — a ~1e-8 inconsistency,
harmless here but worth a refresh when the route is next touched.)

## 5. Cross-links

- [`prop:confinement-frobenius-reciprocity`](../../content/quantum-observable-universe/particle-interactions/confinement-frobenius-reciprocity.md) — the master formula.
- [`conj:knot-factor-frobenius-pairing`](../../content/quantum-observable-universe/mass-theory/knot-factor-frobenius-pairing.md) — the `O=H` binding special case (raw-trace form; the unverified collapse).
- [`borromean-axial-coupling.py`](../../computations/borromean-axial-coupling.py) — the working master-formula instance (g_A scaffold).
- `docs/audits/2026-06-10-binding-active-set-compute-optimization.md` — the active set as a *trace truncation* was rejected (10⁻³ tail); this redesign uses it in the *master formula*, a different object.
- `docs/audits/2026-06-17-bsym-p3a-bottleneck-and-closed-form-wiring.md` — the compute-speed sibling (PR #2405); §E flagged the α/shell gap this doc attacks.
