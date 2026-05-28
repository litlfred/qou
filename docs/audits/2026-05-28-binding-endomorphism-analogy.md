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

## Caveat: the deuteron result is trace-convention-specific

The $\Delta\mathrm{tr}(d) = 0.5952$ above comes from `binding_canonical`
(the Wenzl-bridge closed form). The independent $H_{3A}$-direct
Wedderburn sum (`binding_per_bond_decomposition.py`, same
`atom_braid_word_3A` + normalized-Plancherel weights used everywhere
else) instead gives $\Delta\mathrm{tr}(d) = 0.4241$ — a **29 % gap**,
which turns the $+0.19\%$ match into $-28.6\%$. So the clean deuteron
result is **specific to the Wenzl-bridge convention** and is *not*
reproduced by the $H_{3A}$ Wedderburn trace.

**Reconciling the two binding-trace conventions is the prerequisite
for the A≥3 problem** — before any per-bond / per-pair sum or
binding-link volume can be trusted, the two production paths must be
shown to compute the same $\Delta\mathrm{tr}$. Witness:
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
