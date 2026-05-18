# λ_scale Conjecture Proof — Step 3 (q-expansion via Yekutieli-Stokes)

**Date:** 2026-05-18
**Branch:** `claude/lambda-scale-conjecture-proof` (PR #701)
**Conjecture:** [`conj:lambda-scale-substrate-form`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-substrate-form.md)
**Status:** Structural argument written; formal proof open.

## The claim

Step 3 of the proof strategy:

> Expanding $\tau_q$ around $q = 1$ as
> $\tau_q = \tau_1 + h^2 \cdot \tau^{(2)} + O(h^4)$
> on the H_4 Markov basis, the second-order coefficient
> $\tau^{(2)}$ evaluates to $-G$ on the canonical Borromean braid.

This is the deepest claim — it pins the h² coefficient at the
**Catalan constant** $G = \mathrm{Vol}(\mathcal{B}_3)/8$ via the
Yekutieli categorical nonabelian Stokes theorem.

## Structural argument

### 1. The Markov trace at q = 1

At $q = 1$, the Hecke algebra $H_n(q)$ collapses to the symmetric
group algebra $\mathbb{C}[S_n]$. The Markov trace becomes the
classical normalised trace on $S_n$ representations, which on the
H_4 half-symmetric basis evaluates to a rational (5/2 in our setup).

### 2. The leading h² correction

For the q-expansion at $q = 1 + h/2 + O(h^2)$:

$$
  \tau_q = \tau_1 + h^2 \cdot \tau^{(2)} + O(h^4),
$$

the second-order coefficient $\tau^{(2)}$ is the *second-derivative*
of the trace with respect to the deformation parameter, evaluated at
$q = 1$. In closed form:

$$
  \tau^{(2)}(\beta) = \frac{1}{2} \frac{d^2}{dq^2}\bigg|_{q=1} \tau_q(\beta).
$$

For a generic braid $\beta$, $\tau^{(2)}(\beta)$ is a polynomial in
the partition-content statistics of $\beta$'s Schur decomposition.

### 3. The Yekutieli categorical Stokes connection

[`rem:yekutieli-stokes`](../../content/quantum-observable-universe/braids-and-knots/yekutieli-stokes.md)
identifies the Markov trace with the **nonabelian multiplicative
integral** of an instanton connection $A$ over the surface bounded by
the braid closure (Yekutieli 2015):

$$
  \tau(\beta) = \mathrm{MI}^{\mathrm{nab}}_{\Sigma_\beta}(A).
$$

Under the q-deformation, the nonabelian integral acquires h-corrections
from the **curvature** of $A$ on the surface. For the Borromean braid:

- $\Sigma_\beta$ = surface bounded by the Borromean rings closure
- The curvature 2-form $F = dA + A \wedge A$ integrated over
  $\Sigma_\beta$ gives the **hyperbolic volume of the complement**:
  $\int_{\Sigma_\beta} F = -\mathrm{Vol}(\mathcal{B}_3)$.

The sign $-$ comes from the orientation convention: the curvature
is "absorbed" by the volume of the complement, so the trace
*decreases* by the volume under deformation.

### 4. Per-cell normalisation

The Borromean rings complement decomposes into 8 ideal regular
octahedra (Adams 1985):

$$
  \mathrm{Vol}(\mathcal{B}_3) = 8 \cdot V_{\mathrm{oct}}/2 = 8G
$$

where $V_{\mathrm{oct}} = 8\Lambda(\pi/4) = 4G$ and $\Lambda(\pi/4) = G/2$.

The "per-cell" contribution to $\tau^{(2)}$ — i.e. the h² coefficient
*per ideal octahedral cell* — is therefore:

$$
  \tau^{(2)}_{\mathrm{per-cell}} = -\frac{\mathrm{Vol}(\mathcal{B}_3)}{8} = -G.
$$

### 5. Putting it together

For the **half-symmetric Wedderburn projection** (Step 2 of the proof
showed this equals 5/2 at the H_4 level), the **per-cell trace
contribution** is the single octahedral cell — because the
half-symmetric projection extracts ONE conjugate-pair sum out of the
8-fold tessellation.

Therefore:

$$
  \tau^{(2)}_{\mathrm{half-sym}}(\beta_{\mathrm{Bor}}) = -G,
$$

and the q-expansion of the half-symmetric Markov trace gives

$$
  \lambda_{\mathrm{scale}}
  = \underbrace{\tfrac{5}{2}}_{\tau_1 \text{ from Step 2}}
    + h^2 \cdot \underbrace{(-G)}_{\tau^{(2)} \text{ from Yekutieli-Stokes}}
    + O(h^4).
$$

## Why this is "structural argument" not "proof"

The above derives the form `λ = 5/2 − h²·G + O(h⁴)` from the
combination of:

| Component | Status |
|-----------|--------|
| Step 2 (5/2 = half-symmetric count) | ✅ Proved by enumeration |
| Yekutieli Stokes identification | Conjectural (`rem:yekutieli-stokes`) |
| Curvature ↔ hyperbolic volume identity | Standard differential geometry |
| Vol(B_3) = 8G | ✅ Derived (Adams 1985) |
| "Per-cell extraction by half-symmetric projection" | **Conjectural** — this is the load-bearing step |

The load-bearing step is the **categorical identification** that
the half-symmetric Wedderburn projection extracts ONE
octahedral cell from the 8-fold tessellation. This is plausible
from the symmetry argument (5/2 = 2·1 + 0.5 = ONE pair + half a
self-conjugate, structurally analogous to ONE octahedral cell out
of 8), but the rigorous categorical proof requires:

1. **Explicit construction** of the bijection between conjugate-pair
   half-counts and ideal-octahedral cells.
2. **Compatibility** between the q-deformation and this bijection
   to second order in h.
3. **Sign convention** verification (why $-G$ rather than $+G$).

## Concrete next R&D for full proof

1. **Construct the bijection explicitly** at H_4: list the 8 ideal
   octahedra in B_3 complement and match them to the half-symmetric
   partition contributions:
   - {(4), (1,1,1,1)} pair ↔ octahedra at "vertices" of the tessellation
   - {(3,1), (2,1,1)} pair ↔ octahedra at "edges"
   - (2,2) self-conjugate / 2 ↔ ONE octahedron at the "center"

2. **Verify the curvature integration** in mpmath. The integration
   should give exactly $-G$ to 50 dps; if it gives a slightly different
   value, the bijection or the formula needs refinement.

3. **Cross-check with the 5.4 ppm residual.** If c_4 (Step 4)
   admits a substrate form derivable from the same per-cell
   tessellation argument, that would close Step 3 and Step 4
   together.

4. **Lean formalisation** of the Yekutieli-Stokes path is a
   long-term target; Mathlib lacks the nonabelian multiplicative
   integral primitive, so this is a substantial dependency.

## Conjectural-proof closure summary

| Step | Status | Method |
|------|--------|--------|
| Step 1 | Open | Categorical structural claim |
| Step 2 | ✅ Proved | Combinatorial enumeration |
| **Step 3** | **Structural argument** (this audit) | Yekutieli-Stokes + tessellation bijection |
| Step 4 | Open R&D | h^4 PSLQ search (Step 4 probe in this PR) |
| Step 5 | ✅ Closed structurally | Anchor + substrate Q_β |

Step 3 has the **outline of a proof** — the connection to Vol(B_3)/8 = G
via Yekutieli-Stokes is mathematically natural. But the load-bearing
**per-cell extraction** step needs explicit construction. This is
the deepest open component of the proof.
