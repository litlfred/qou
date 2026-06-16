# Q_β Step 1 — symbolic q-rational min-L2 closure of T_β NF coordinates

**Date.** 2026-06-03
**PR.** [#1739](https://github.com/litlfred/qou/pull/1739) (`claude/qbeta-habiro-recursion-and-bridge-2026-06-02`)
**Supersedes.** [`2026-06-02-qbeta-pre-archimedean-status-and-bridge-instance.md`](2026-06-02-qbeta-pre-archimedean-status-and-bridge-instance.md) §"Step 1 — extract c_k from witnesses" (the bullet that was marked *partially done*)
**Companion compute.** [`computations/qbeta/qbeta_symbolic_tbeta_min_l2.py`](../../computations/qbeta/qbeta_symbolic_tbeta_min_l2.py)
**Companion witness.** [`qbeta-symbolic-tbeta-min-l2.witness.json`](../../computations/qbeta/qbeta-symbolic-tbeta-min-l2.witness.json)

## Result

The 6 numerical NF coordinates of $T_\beta$ that the 2026-06-02 audit
localised as the residual archimedean leak in the Q_β pre-archimedean
chain are now computed as **q-rational closed forms × a single
archimedean scalar**:

$$
x_i(q) \;=\; \dfrac{A_i(q)\,\cdot\, S}{\lVert A(q)\rVert^2},
\qquad
A_i(q) \;=\; \sum_{\lambda}\,y_\lambda(q)\;\chi_\lambda(b_i)(q),
\qquad
S \;=\; \dfrac{Q_\beta(q_0)}{E_0(q_0)}.
$$

All ingredients in the *shape* are exact in $q$:

- $\chi_\lambda(b_i)(q)$ — Hoefsmit seminormal traces of the NF basis
  matrices per Hecke block $\lambda \vdash 3$, reusing the existing
  `qbeta_per_block_symbolic.py` infrastructure.
- $y_\lambda(q)$ — Schur-element cyclotomic forms from
  [`y-lambda-cyclotomic-factor.witness.json`](../../computations/y-lambda-cyclotomic-factor.witness.json).
- $\lVert A(q)\rVert^2$ — q-rational sum of squares.

The *only* archimedean input is the scalar $S = Q_\beta(q_0)/E_0(q_0)$
— one number, not six.

## Sanity at $q_0 \approx 1.10998$

50-dps symbolic evaluation vs 64-bit numeric SDP witness
[`qbeta-decay-sdp-knot-operator.witness.json`](../../computations/qbeta/qbeta-decay-sdp-knot-operator.witness.json):

| Quantity | Max abs diff |
|----------|--------------|
| 6 NF coordinates $\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-$ | $3.8\times 10^{-10}$ |
| $\tau_M(T_\beta)$ Taylor $a_0\ldots a_7$ | $3.0\times 10^{-10}$ |

The residue is the 64-bit SDP solver's numerical precision; the
symbolic side is exact.

## Structural observation — symmetries are now identities, not coincidences

The numerical SDP witness reports $\sigma_0 \approx \sigma_1$ and
$L_+ \approx L_-$ to ~12 digits. The symbolic computation discharges
this as an **exact q-rational identity**:

$$
A_{\sigma_0}(q) \;\equiv\; A_{\sigma_1}(q),
\qquad
A_{L_+}(q) \;\equiv\; A_{L_-}(q),
$$

both as elements of $\mathbb{Q}(q^{1/2})$ — the Hecke $S_3$ symmetry
acting on the NF basis. The numerical match in prior witnesses was
not a coincidence to be cross-checked; it is a categorical fact.

## What this buys downstream

### Step 2 — Habiro integrality (PR [#1511](https://github.com/litlfred/qou/pull/1511), [#1727](https://github.com/litlfred/qou/pull/1727) territory)

The Habiro-membership probes can now run on the q-rational *shape*

$$
F_i(q) \;:=\; \dfrac{A_i(q)}{\lVert A(q)\rVert^2}
$$

directly. CODATA $Q_\beta$ (the only archimedean datum) cancels in
the $c_k$ *ratios* on which the Habiro integrality test operates, so
the test result is anchor-invariant.

### Step 3 — bridge instance

The bridge between this NF coordinatisation and the Habiro element
$[2]_q \cdot (1 - h^2\alpha)$ from PR #1511 acquires a concrete
candidate identification: **the Habiro element is $S \cdot F_i(q)$
for the channel $i$ realising the dominant $A$-block.** This is *not
discharged* by the present work — it is the next concrete probe.

## Caveats reviewers should focus on

1. **Min-L2 is the *Euclidean* coordinate norm.** It is the standard
   SDP minimum-norm primal-feasible solution; basis-dependent.
   The natural categorical replacement is the **Markov-trace inner
   product** $\langle X, Y \rangle := \tau_M(X^\dagger Y)$. Whether
   the SHAPE × S decomposition survives under that swap is the next
   probe. **Planned as a sibling PR** (per PR #1739 review-thread
   decision 2026-06-03) — not a follow-up commit on this PR.

2. **Step 3 is not discharged here.** The bridge instance is
   *identified*, not *proved*. Discharging it requires either:

   - showing $S \cdot F_i(q) \in \widehat{\mathbb{Z}[q]}$ explicitly
     (Habiro completion); or
   - a categorical argument that the dominant-$A$-block channel is
     the unique one realising the bridge.

3. **CODATA $Q_\beta$ presence in $S$ is intentional, not a fitting
   knob.** $Q_\beta(q_0)$ is the experimental neutron β-decay width
   used as CAL-2 in the three-calibration discipline (per
   [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)).
   It enters the shape via the substrate identity Q_β → q₀, not as a
   free parameter. The shape × S decomposition is therefore consistent
   with the calibration discipline — it does *not* introduce a fourth
   calibration knob.

## Cross-link to the canonical chain

Per [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md),
the affected steps in the chain are:

```
… → tr_M = Σ_λ y_λ χ_λ           (Step 9a)  — y_λ now symbolic ✓
  → confinement SDP                (Step 9b)  — coords now symbolic ✓
  → canonical T_w                  (Step 10)  — T_β shape now symbolic ✓
  → Archimedean functor at q_0     (Step 11)  — S = Q_β/E_0 is the
                                                only archimedean input
```

Steps 9a–10 are now SHAPE-level pre-archimedean; Step 11 is localised
to a single scalar.

## Follow-up planned on PR #1739

1. `qbeta_uw_reparam_probe.py` — compare $c_k$ under $u = b\hbar^2$
   (current production) vs $w = q - 1/q$ (the natural Habiro
   variable). Cheap (~30 min sympy).
2. (this audit doc).

## Follow-up planned on a sibling PR

3. Markov-trace inner product replacement of min-L2. Replaces the
   Euclidean norm with $\langle X, Y \rangle_{\tau_M} :=
   \tau_M(X^\dagger Y)$ as the SDP objective. Test whether the
   SHAPE × S decomposition survives; if it does, the basis-dependence
   caveat (1) above is fully discharged.
