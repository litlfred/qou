# Binding residual `10A−5` — chain-topology derivation (2026-06-29)

**Status:** derive-or-refute / **near-match tier** (Δ_λ-gate discipline: derives the *structure* of
the canonical residual, NOT a 7th fit ansatz; nothing wired to production).
**Bean:** binding closure (Δ_λ gate); follows
[`2026-06-09-delta-lambda-canonical-residual.md`](2026-06-09-delta-lambda-canonical-residual.md).
**Probe:** [`computations/binding_residual_exponent_chain_topology.py`](../../computations/binding_residual_exponent_chain_topology.py)
(+ witness). **Lean (sorry-free):**
[`QOU/Mass/BindingResidualExponent.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/BindingResidualExponent.lean).

## The target

The canonical trace-binding `B_pred(Z,N) = E₀·(tr_M(W_free) − tr_M(W_atom))`
([`binding_canonical.py`](../../computations/binding_canonical.py)) undershoots AME by a
near-integer q₀-power: `Δ_λ(K) = B_AME/B_pred ≈ q₀^(10A−5)` (deuteron exact to 0.01 exponent units).
The audit's open question: does `10A−5` have a categorical derivation from the `W_free`/`W_atom`
crossing/jet bookkeeping?

## The derivation — `10A−5 = 5·(2A−1)` over the chain topology

Reading the **actual** braid word `atom_braid_word_3A` (not a model): the `W_atom` braid is a
**chain** of `A = Z+N` nucleons, each a 3-strand 𝓑₃ on `g0`(7) + `g1`(4) = 11 crossings, linked by
`A−1` interface crossings (one per consecutive pair). Verified D/T/³He/⁴He/⁶Li:

| atom | A | strands 3A | len W_free | len W_atom | interfaces | bonds A−1 | bond types pp/pn/nn |
|---|--:|--:|--:|--:|--:|--:|:--|
| D | 2 | 6 | 22 | 23 | 1 | 1 | 0/1/0 |
| T | 3 | 9 | 33 | 35 | 2 | 2 | 0/1/1 |
| ³He | 3 | 9 | 33 | 35 | 2 | 2 | 1/1/0 |
| ⁴He | 4 | 12 | 44 | 47 | 3 | 3 | 1/1/1 |
| ⁶Li | 6 | 18 | 66 | 71 | 5 | 5 | 2/1/2 |

So `len(W_free) = 11A`, `len(W_atom) − len(W_free) = A−1` (= bonds), and the residual exponent
factorizes over the chain's `2A−1` topological units:

$$10A-5 \;=\; 5\,(2A-1) \;=\; 5\big[\underbrace{A}_{\text{nucleons}} + \underbrace{(A-1)}_{\text{bonds}}\big].$$

**Each topological unit — nucleon or bond — carries exactly `5` q₀-exponent units.** The `2A−1`
decomposition is **derived** (chain topology, formalized sorry-free in Lean:
`residualExponent_five : residualExponent 5 A = 10*A − 5`, with the per-unit weight carried as a
parameter `w`). The open question is now sharply reduced: **why `5` per unit.**

## Per-bond (not per-nucleon) — and the Z-correction

The A-scaling alone is ambiguous between "5/nucleon + 5/bond" and "10/nucleon − 5 global". The
**per-bond** reading is selected by the Z-dependence: ³He and T have the **same** A=3 and the same
bond count (2), but different bond **types** (³He `{pp,pn}`, T `{pn,nn}`), because the interface
factors differ (`f_pp = f_pn = z`, `f_nn = z − h`). A per-nucleon-only law would be blind to this;
the per-bond law is not. This is the source of ³He's `−1.40` deviation from `5(2A−1)=25` (the only
proton-rich `A=3` case; N≥Z isotopes are within `0.27`). The residual Z-correction
(`~ −1.4` per excess proton at A=3) is the bond-type asymmetry `log_{q₀}(f_pp/f_nn)` carried into the
sub-leading term — quantifying it exactly is the open sub-task.

## Scope / discipline

- **Derived (exact, Lean sorry-free):** `2A−1 = nucleons + bonds`; `len(W_free)=11A`;
  `interfaces = bonds = A−1`; `10A−5 = 5·(2A−1)`.
- **Open (reduced):** the per-unit weight `5`. Candidate structural origin: the **5 A₅-irreps** of
  the Bring/icosahedral substrate — the same five-fold the **s5-so3 keystone** (`s5bb`) W_λ index
  runs over. Whether the `5` is a **confinement-SDP** shadow-price / active-channel count is the next
  probe (owner-asked).
- **Not claimed:** a closure of binding; a derivation of the `5`; production wiring. Near-match tier,
  no fit, Δ_λ gate untouched.
