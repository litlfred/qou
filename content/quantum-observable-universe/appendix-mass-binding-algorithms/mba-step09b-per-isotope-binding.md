**Algorithm (Per-isotope binding energy — experimental $q$-difference generating-function model; the $\Delta_\lambda$ gate is open).**
*Evaluate the binding energy $B_n \propto w_n$ for multi-body nuclear clusters via the universal `CKRecursion` depth-2 discrete generating function, seeded by the topological traces of the strong mediator knots.*

### Input

- *Topological trace constants: $r_{\mathrm{gluonic}} = 3$ and $r_{\mathrm{residual}} = 2.5$.*
- *The universal bar-even structural prior $a_0 = 1/2$.*
- *SU(4)/$S_3$ isospin representation anomaly shifts (e.g., $+1.4947 m_e$).*

### Output

- *Predicted binding energy $B_n$ in MeV.*

### Algorithm

```
1. Compute the exact residual trace r_{res} evaluated at the substrate root q_0 (yields ~2.596).
2. Seed the depth-2 CKRecursion engine: w_{n+1} = 0.5 * w_n + r_{res} * w_{n-1}.
3. The engine natively generates the multi-body binding hierarchy (w_2 = 4.35, w_3 = 8.60, w_4 = 15.60).
4. Scale weights by the nucleon parameters to yield baseline binding energies.
5. Apply exact categorical SU(4) anomaly splits to resolve degeneracies (e.g., 3H vs 3He).
```

### Correctness conditions

These are **fit residuals of the experimental model**, not derived error bounds:

1. *With the seed constants calibrated, the generating function reproduces $^4$He ($n=4$) to within $\sim 3.4$ keV of the AME value — a fit residual, not a parameter-free bound ($^4$He remains open, the $\mathrm{Vol}_4$ census gap).*
2. *The isospin anomaly correction resolves the $n=3$ doublet ordering ($^3$H vs $^3$He); the residual is a calibrated near-match, not an accuracy claim against the L2 target.*

**Scope (open gate, not a closure).** The $\Delta_\lambda(K)$ closure — the Track A gate — remains **open** (AGENTS.md §"Δ_λ gate"; six ansätze have failed). This module is an **experimental / phenomenological** generating-function model: the depth-2 `CKRecursion` reproduces the multi-body binding hierarchy from a small set of seed constants ($r_{\mathrm{res}} \approx 2.596$, $a_0 = 1/2$, the isospin anomaly shift $\approx +1.4947\,m_e$) that are **calibrated, not derived** from the 13 categorical drivers. It is a structural fit, **not** a parameter-free derivation — the `status: "experimental"` and `open-gate` labels on this block's manifest are authoritative.

### Python API entry point

```python
from computations.mass_binding_dashboard import _row

# The B_unified mass table outputs the model's (calibrated) binding values
```

### Witness contract

*Witness generated via the mass binding dashboard runs: `dashboard_and_sweep_results.md`. (The dashboard logs report the model's fit residuals per isotope; these are calibrated near-matches, not a closure — the $\Delta_\lambda$ gate is open.)*

### Notes

*This module explores a $q$-difference generating-function route to the multi-body binding hierarchy. It does **not** supersede the $\Delta_\lambda$ closure search — that gate is open. The shared `CKRecursion` shape across the weak ($Q_\beta$) and strong (binding) sectors is a **structural observation / working hypothesis**, not a proven identity. Per AGENTS.md §"Axiomatization is NOT a Proof", any wiring of a $c_k$ or $\Delta_\lambda$ value to production remains blocked pending a genuine closed-form derivation from the categorical drivers.*

*The `CKRecursion` recurrence is extensive and algebraically convenient, but its seed constants are calibrated inputs, so the binding it produces is a fit, not a derivation.*

### Tier note: experimental generating-function model (2026-07-08)

*The $w_n$ values and the $\sim 3$ keV $^4$He fit residual come from the discrete $q$-difference recurrence with calibrated seeds — a phenomenological reproduction, not a structural bound. A kernel-constraints Lean file for the $q$-difference recurrence exists on the $Q_\beta$ side (`QBetaCKRecursionKernelConstraints.lean`); a binding-sector analogue that would formalize any derived (non-calibrated) constant is not yet written.*
