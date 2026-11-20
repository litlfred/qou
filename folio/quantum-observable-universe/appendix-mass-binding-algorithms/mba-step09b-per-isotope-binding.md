**Algorithm (Per-isotope binding energy — experimental $q$-difference generating-function model; the $\Delta_\lambda$ magnitude is open).**
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

**The $q$-lift of the depth-2 kernel.** The $q$-lift of the proved classical depth-2 kernel exists exactly on the $[n]_q!$-normalized carrier ($c(q) = 1$, probe-verified; not yet formalized in Lean) and is distinct from the Garoufalidis–Gu–Mariño resurgent-Stokes carrier \cite{garoufalidis-gu-marino2021} up to scalar gauge. The identification is open.

**Scope (value proved; magnitude open, not a closure).** The per-partition
$\Delta_\lambda$ **value** is proved ($\Delta_\lambda = (-1)^{n(\lambda)}\dim V_\lambda$,
general-$n$, [`prop:delta-lambda-dt-index-unification`](#prop:delta-lambda-dt-index-unification) / `dtEuler_eq_deltaLambda_unconditional`); what remains **open** is
the many-body binding **magnitude**: six ansätze have failed on the deuteron
*magnitude* $r^\ast \approx 1.585$, which no per-block $\Delta_\lambda$ can supply. This module is an **experimental / phenomenological** generating-function model for that magnitude: the depth-2 `CKRecursion` reproduces the multi-body binding hierarchy from a small set of seed constants ($r_{\mathrm{res}} \approx 2.596$, $a_0 = 1/2$, the isospin anomaly shift $\approx +1.4947\,m_e$) that are **calibrated, not derived** from the 13 categorical drivers. It is a structural fit, **not** a parameter-free derivation.

### Python API entry point

```python
from qou_mass.api import predict          # the .ts manifest's declared entry point

# NOTE (corrected 2026-08-25, PR #5765): this block previously pointed at
# `computations.mass_binding_dashboard._row`. That module HAS `_row`, but it has
# ZERO occurrences of `B_unified`. The entry point above now matches
# `computation.script` in the .ts manifest.
#
# RE-CORRECTED 2026-09-19 (bean `qou-kjik`). The 2026-08-25 note went on to say
# that "the `B_unified` model lives in
# `computations/probes/strong_unified_binding_probe.py`". It does not, and that
# sentence should not be followed: no producer in this repository emits a live
# `B_unified`. That probe is an ANCHOR-INVERSION EXPERIMENT -- all three of its
# weights are solved out of the AME table it is then scored against, so its error
# column is identically zero on the D and 4He rows by construction, and the two
# NA-Stokes quantities its verdict credits for the closure are never used. It
# emits no witness and has no importers. Read its module docstring before
# quoting any number from it.
```

### Witness contract

*Witness: [`computations/canonical-mass-table-242ppb.witness.json`](../../../computations/canonical-mass-table-242ppb.witness.json), as declared by `computation.witness` in this block's `.ts` manifest.*

*The declared witness carries no provenance fields and records binding at the 242-ppb nucleon level (D $+23\,\%$, T $+6\,\%$, ³He $+13\,\%$, ⁴He $+3.6\,\%$, over-binding), which predates the removal of a fitted Habiro dressing. The live pipeline under-binds (²H $-27.5\,\%$, ³H $+38\,\%$, ³He $+44\,\%$, ⁴He $+69\,\%$); the witness figures are not this step's current accuracy.*

### Notes

*This module explores a $q$-difference generating-function route to the multi-body binding hierarchy. It does **not** supersede the $\Delta_\lambda$ closure search, which is open. The shared `CKRecursion` shape across the weak ($Q_\beta$) and strong (binding) sectors is a **structural observation / working hypothesis**, not a proven identity. Axiomatisation is not proof: no $c_k$ or $\Delta_\lambda$ value produced here is carried downstream, pending a genuine closed-form derivation from the categorical drivers.*

*The `CKRecursion` recurrence is extensive and algebraically convenient, but its seed constants are calibrated inputs, so the binding it produces is a fit, not a derivation.*

### Tier note: experimental generating-function model

*The $w_n$ values and the $\sim 3$ keV $^4$He fit residual come from the discrete $q$-difference recurrence with calibrated seeds — a phenomenological reproduction, not a structural bound. A kernel-constraints Lean file for the $q$-difference recurrence exists on the $Q_\beta$ side; a binding-sector analogue that would formalize any derived (non-calibrated) constant is not yet written.*
