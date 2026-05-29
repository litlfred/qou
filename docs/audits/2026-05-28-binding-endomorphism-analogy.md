# Binding endomorphism: B = m_e × Vol(K_bind) × Δtr (2026-05-28)

## Summary

The nuclear binding energy follows the **mass-endomorphism analogy**.
Where the nucleon mass is

$$
  m(K) = m_e \cdot \frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2}
         \cdot \mathrm{lw}(K, q_0),
$$

the binding energy of a composite nucleus is

$$
  B(K) = m_e \cdot \mathrm{Vol}(K_{\mathrm{bind}}) \cdot \Delta\mathrm{tr},
  \qquad
  \Delta\mathrm{tr} = |\mathrm{tr}_M(\text{free})| - |\mathrm{tr}_M(\text{atom})|,
$$

where $K_{\mathrm{bind}}$ is the **binding link** — the closure of the
inter-nucleon crossings in the $H_{3A}(q_0)$ braid — and $\Delta\mathrm{tr}$
is the Wedderburn trace difference between the free (disjoint) and bound
(interleaved) nucleon configurations.

## Deuteron: confirmed at +0.19%

| Factor | Value | Source |
|--------|-------|--------|
| $m_e$ | $0.51099895$ MeV | CAL-1 anchor |
| $\mathrm{Vol}(\mathcal{B}_3) = 8G$ | $7.327725$ | Borromean knot complement (proved) |
| $\Delta\mathrm{tr}(d)$ | $0.595240$ | $H_6$ Wedderburn (binding_canonical) |
| **$B(d)$** | **$2.2289$ MeV** | vs AME $2.22452$ — **+0.19%** |

Zero free parameters. Witness:
[`binding-endomorphism-deuteron.witness.json`](../../folio-assistant/computations/binding-endomorphism-deuteron.witness.json).

This confirms the existing
[`prop:deuterium-derived-binding`](../../content/quantum-observable-universe/mass-theory/deuterium-derived-binding.md)
result, now framed explicitly as the binding-endomorphism analogue of
the mass formula.

## The binding link is atom-specific (SDP registry)

The [binding-K SDP solver](../../folio-assistant/computations/binding-k-solver.witness.json)
identifies the binding link $K_{\mathrm{bind}}$ per atom:

| Atom | $A$ | $H_{3A}$ | Binding link $K_{\mathrm{bind}}$ |
|------|-----|----------|----------------------------------|
| $d$ (²H) | 2 | $H_6$ | Hopf link $L_H$ |
| $t$ (³H) | 3 | $H_9$ | $8_{11}$-class link |
| ³He | 3 | $H_9$ | L6a4 (3-component) |
| ⁴He | 4 | $H_{12}$ | (pending SnapPy) |

The volume scale for the deuteron matches $\mathrm{Vol}(\mathcal{B}_3) = 8G$
to $0.19\%$ — the Borromean volume, inherited from the per-nucleon
Borromean braid structure, governs the binding.

## Extension to T / ³He / ⁴He (open)

The deuteron formula uses $\mathrm{Vol}(\mathcal{B}_3)$ because both
nucleons are Borromean and the single inter-nucleon crossing is a Hopf
link (whose Seifert volume vanishes, so the Borromean scale dominates).

For $A \geq 3$ the binding link is genuinely hyperbolic (8₁₁-class,
L6a4) with nonzero volume. The honest extension requires:

1. **SnapPy computation** of $\mathrm{Vol}(K_{\mathrm{bind}})$ for each
   binding link in the registry.
2. **Per-pair decomposition** — the large-$A$ pair-sum structure
   described in `prop:deuterium-derived-binding` (the continuum limit
   reproduces Bethe–Weizsäcker).
3. **Verification** that $B(K) = m_e \cdot \mathrm{Vol}(K_{\mathrm{bind}})
   \cdot \Delta\mathrm{tr}$ matches AME without rescaling.

### Anti-pattern warning

A prior attempt (PR #1383, **retracted**) manufactured a match by
multiplying $\Delta\mathrm{tr}$ by $A(A-1)/2$ pair counts and $q^{-A}$
powers — a multi-parameter fit disguised as a derivation. The actual
trace ratio $\Delta\mathrm{tr}(⁴\mathrm{He})/\Delta\mathrm{tr}(d) = 0.67$,
not the $12.7$ needed for $[4]_q!/2$. The binding link volume — not
hand-chosen rescaling — must supply the $A$-dependence.

## Raw data (binding_canonical, $H_{3A}$)

| Atom | $|\mathrm{tr}_{\mathrm{free}}|$ | $|\mathrm{tr}_{\mathrm{atom}}|$ | $\Delta\mathrm{tr}$ | scale needed (MeV) |
|------|------|------|------|------|
| $d$ | 0.9835 | 0.3883 | 0.5952 | 3.74 (= $m_e \cdot 8G$ ✓) |
| $t$ | 0.9080 | 0.1041 | 0.8040 | 10.55 |
| ³He | 1.0478 | 0.2065 | 0.8412 | 9.17 |
| ⁴He | 0.9673 | 0.0553 | 0.9120 | 31.03 |

The deuteron scale $3.74 = m_e \cdot \mathrm{Vol}(\mathcal{B}_3)$. The
heavier scales (10.55, 9.17, 31.03) await their binding-link volumes.

## RESOLVED: the trace-convention gap was a weight-scheme error

An earlier note here flagged a 29 % gap between `binding_canonical`'s
$\Delta\mathrm{tr}(d) = 0.5952$ and an $H_{3A}$-direct value $0.4241$,
calling it an unresolved inconsistency. **This is now resolved**
([`trace_convention_reconciliation.py`](../../folio-assistant/computations/trace_convention_reconciliation.py)):
the gap is purely a **$y_\lambda$ weight-scheme difference**, not a
framework inconsistency.

Both paths evaluate $\mathrm{tr}_M = \sum_\lambda y_\lambda \cdot
\chi_\lambda(W)$ on the *same* joint $H_6$ braid word with the *same*
characters $\chi_\lambda$. They differ only in $y_\lambda$:

| Convention | $y_\lambda$ | $\Delta\mathrm{tr}(d)$ |
|------------|-------------|------------------------|
| **Wenzl Jones–Markov** (`binding_canonical`) | $z = 1/(\sqrt q + 1/\sqrt q)$ per Markov move | **0.59524** |
| normalized-Plancherel (q-Schur) | $\dim_q(\lambda)^2 / [n]_q!$ | 0.42405 |

The Wenzl-bridge value on the joint word matches `binding_canonical`'s
factorized closed form to 11 digits ($3\times10^{-12}$, full mpf — no
float64), so `binding_canonical` *is* the Wenzl convention. Per CLAUDE.md,
**the mass/binding chain uses Wenzl JM** (the Plancherel scheme is for
the torus-knot lepton tower). The `binding_per_bond_decomposition.py`
probe erroneously used Plancherel weights — that was the source of the
apparent gap, not a real disagreement.

**Consequence:** the deuteron $+0.19\%$ endomorphism result (Wenzl JM)
is correct and stands. The A≥3 $-60\%$ failure of the single-link
volume **persists in the correct Wenzl convention** — so it is the
genuine open problem, not a convention artifact. Witnesses:
[`trace-convention-reconciliation.witness.json`](../../folio-assistant/computations/trace-convention-reconciliation.witness.json),
[`binding-per-bond-decomposition.witness.json`](../../folio-assistant/computations/binding-per-bond-decomposition.witness.json).

## Binding-link volumes (SnapPy, PR #1397)

| Atom | Link | Vol | Note |
|------|------|-----|------|
| ²H | Hopf (L2a1) | 0 | Seifert-fibred |
| ³H | $8_{11}$ | 8.2863 | hyperbolic |
| ³He | L6a4 | 7.3277 | **= 8G = Vol(Borromean)** |

The ³He binding link L6a4 *is* the Borromean rings. The single-link
endomorphism $B = m_e \cdot \mathrm{Vol}(K_{\mathrm{bind}}) \cdot
\Delta\mathrm{tr}$ matches ²H (via Hopf→$\mathrm{Vol}(\mathcal{B}_3)$)
but gives $-60\%$ for ³H/³He: the A-dependence is not carried by a
single binding-link volume.

## Multi-bond test (Wenzl JM, PR follow-up)

With conventions reconciled, the additive per-bond model
$B = m_e \cdot \mathrm{Vol}(\mathcal{B}_3) \cdot \sum_{\text{bonds}}
\Delta\mathrm{tr}_{\text{bond}}$ (each chain bond's Wenzl trace shift,
no scale fit) gives:

| Atom | bonds | $\sum\Delta\mathrm{tr}$ | $B(\Sigma)$ | err | $B$(combined) | err |
|------|-------|------|------|------|------|------|
| ²H | 1 | 0.5952 | 2.229 | +0.2% | 2.229 | +0.2% |
| ³H | 2 | 1.1940 | 4.471 | −47% | 3.010 | −64% |
| ³He | 2 | 1.1587 | 4.339 | −44% | 3.150 | −59% |

**Findings (no fit):**
1. Binding is **more additive than multiplicative** — the per-bond sum
   beats the combined product ($-47\%$ vs $-64\%$ for ³H), confirming
   binding lives in the inter-nucleon bonds.
2. The per-bond sum is still **~2× short** for $A=3$ ($t$ needs
   $4.24$ MeV/bond; the model gives $\sim 2.2$). The factor of two
   points to **all-pairs vs chain** bond counting: ³He has
   $\binom{3}{2}=3$ pairs (pp + pn + pn) but the chain braid
   `atom_braid_word_3A` encodes only $A-1=2$ adjacent bonds. The
   missing non-adjacent (nucleon₀–nucleon₂) bond is a long-range
   braid generator the current chain word does not carry.

**Next:** an all-pairs braid (not the linear chain) is the topology
to test — a genuine braid-structure question, not a rescaling.
Witness: [`binding-multibond-wenzl.witness.json`](../../folio-assistant/computations/binding-multibond-wenzl.witness.json).

## CORRECTION: the all-pairs "−15%" was a summing artifact

The multi-bond note above suggested an all-pairs 2-body **sum**
($\sum_{\text{pairs}} \Delta\mathrm{tr}$) improves ³He to $-15\%$.
**This is wrong** — and the correction is important.

Summing three independently-computed $H_6$ pair-traces is **not** a
valid 3-nucleon trace. The physically correct object is the **joint
$H_9$ trace** with all three nucleons mutually coupled (including the
long-range nucleon₀–nucleon₂ bond). Computed directly
([`binding_threebody_joint_trace.py`](../../folio-assistant/computations/binding_threebody_joint_trace.py)):

| Atom | joint-$H_9$ Δtr | $B$(joint) | err | (all-pairs *sum* was) |
|------|------|------|------|------|
| ³He | 0.8479 | 3.175 | **−58.9%** | (−15%, artifact) |
| ³H | 0.8122 | 3.041 | **−64.1%** | (−21%, artifact) |

The joint trace matches the combined/single-link value (−59%), **not**
the additive sum. The irreducible 3-body term is therefore **large and
destructive**: $\Delta\mathrm{tr}_{3\text{body}} = 0.848 - 1.759
\approx -0.91$ for ³He — the bonds interfere destructively, making the
joint binding *smaller*, not larger.

**Consequence.** First-principles categorical binding (the correct
joint Markov trace) genuinely **undershoots A≥3 by ~60%**. The
deuteron ($+0.2\%$) works because it is a true 2-body system. The
additive multi-bond model does **not** close the gap — it overcounted
by treating pairs as independent. The A≥3 binding deficit is real, not
a missing-constructive-term artifact.
