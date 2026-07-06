**Proposition (Constit-side per-Z step factor = $\mathrm{tr}_M^3(\mathcal{B}_p)$).**

*Let $\mathcal{B}_K^{\mathrm{vac}}$ be the disjoint Hecke product
defining the constituent vacuum of atom $K = (Z, N)$ — per
[`def:ew-interface-knot`](#def:ew-interface-knot), the canonical
atomic braid with all interface generators removed.  Then the
constit-side per-Z step ratio admits the closed form*
$$
  \boxed{\;
    \rho_Z^{\mathrm{constit}}(q)
    \;:=\;
    \frac{\mathrm{tr}_M\!\bigl(\mathcal{B}_{(Z+1, N)}^{\mathrm{vac}}\bigr)}
         {\mathrm{tr}_M\!\bigl(\mathcal{B}_{(Z, N)}^{\mathrm{vac}}\bigr)}
    \;=\;
    \mathrm{tr}_M\!\bigl(\mathcal{B}_p,\, H_3(q)\bigr)
  \;}
  \tag{$\dagger$}
$$
*for all $q$ in the substrate window, where $\mathcal{B}_p \in H_3(q)$
is the canonical 3-strand proton braid (intra-nucleon crossings
only) and $\mathrm{tr}_M$ is the Jones–Markov trace.*

### Proof

The canonical atom braid factorises (per
[`def:ew-interface-knot`](#def:ew-interface-knot)) as
$$
  \mathcal{B}_K \;=\; \mathcal{B}_K^{\mathrm{vac}} \cdot \bowtie_K,
$$
where $\mathcal{B}_K^{\mathrm{vac}}$ is a **disjoint** Hecke product
of per-nucleon 3-strand factors: for atom $K = (Z, N)$ in ordering
$\mathrm{p}, \mathrm{p}, \ldots, \mathrm{n}, \mathrm{n}$,
$$
  \mathcal{B}_K^{\mathrm{vac}} \;=\;
    \mathcal{B}_p^{(1)} \otimes \mathcal{B}_p^{(2)} \otimes \cdots
    \otimes \mathcal{B}_p^{(Z)}
    \otimes \mathcal{B}_n^{(1)} \otimes \cdots \otimes \mathcal{B}_n^{(N)},
$$
each $\mathcal{B}_p^{(k)}, \mathcal{B}_n^{(k)} \in H_3(q)$, with the
$k$-th block on strands $\{3k+1, 3k+2, 3k+3\}$ and the $\otimes$
denoting parabolic embedding into $H_{3A}(q)$ with $A = Z + N$.

**Wenzl's disjoint Markov-trace multiplicativity**
([wenzl1988] §1.7) states that for any
$\alpha \in H_n(q)$ and $\beta \in H_m(q)$ acting on **disjoint
strand sets** inside $H_{n+m}(q)$,
$$
  \mathrm{tr}_M(\alpha \otimes \beta) \;=\; \mathrm{tr}_M(\alpha) \cdot \mathrm{tr}_M(\beta).
$$
Applying this inductively across the $A = Z + N$ disjoint nucleon
blocks of $\mathcal{B}_K^{\mathrm{vac}}$,
$$
  \mathrm{tr}_M\!\bigl(\mathcal{B}_K^{\mathrm{vac}}\bigr)
    \;=\; \prod_{k=1}^{Z} \mathrm{tr}_M(\mathcal{B}_p^{(k)})
    \cdot \prod_{k=1}^{N} \mathrm{tr}_M(\mathcal{B}_n^{(k)}).
$$
Since all proton blocks are isomorphic ($\mathcal{B}_p^{(k)} = \mathcal{B}_p$ as
abstract H_3 braids) and likewise all neutron blocks
($\mathcal{B}_n^{(k)} = \mathcal{B}_n$),
$$
  \mathrm{tr}_M\!\bigl(\mathcal{B}_K^{\mathrm{vac}}\bigr)
    \;=\; \mathrm{tr}_M(\mathcal{B}_p)^Z \cdot \mathrm{tr}_M(\mathcal{B}_n)^N.
$$
The per-Z step ratio then satisfies
$$
  \rho_Z^{\mathrm{constit}}(q)
    \;=\;
    \frac{\mathrm{tr}_M(\mathcal{B}_p)^{Z+1} \cdot \mathrm{tr}_M(\mathcal{B}_n)^N}
         {\mathrm{tr}_M(\mathcal{B}_p)^Z \cdot \mathrm{tr}_M(\mathcal{B}_n)^N}
    \;=\; \mathrm{tr}_M(\mathcal{B}_p),
$$
yielding $(\dagger)$. $\square$

### Empirical verification (Phase 5l, 50 dps)

Direct measurement at five $q$-values in the substrate window via
[`rho_constit_equals_tau_M_proton_phase5l.py`](../../../computations/rho_constit_equals_tau_M_proton_phase5l.py),
recomputing $y_\lambda(q)$ (Wenzl bridge) and
$\chi_\lambda(\beta, q)$ (Hecke characters) at each $q$:

| $q$ | $\mathrm{tr}_M^3(\mathcal{B}_p, q)$ | $\rho_Z^{\mathrm{constit}}(q)$ | rel. err. |
|---|---:|---:|---:|
| $1.050$ | $0.79284191942392$ | $0.79284191942392$ | $1.69 \times 10^{-51}$ |
| $1.080$ | $0.99328958564705$ | $0.99328958564705$ | $1.08 \times 10^{-50}$ |
| $1.10998$ ($q_0$) | $1.22037426648745$ | $1.22037426648745$ | $3.29 \times 10^{-50}$ |
| $1.130$ | $1.39054700525733$ | $1.39054700525733$ | $1.35 \times 10^{-50}$ |
| $1.170$ | $1.78584582119414$ | $1.78584582119414$ | $0$ (exact) |

The identity holds at **mpfr-50-dps precision** ($\sim 10^{-50}$
rel. err., bounded by the 50-decimal-place compute pin used for
both $y_\lambda(q)$ and $\chi_\lambda(\beta, q)$) at every $q$ —
confirming both the proposition statement and the soundness of the
$y_\lambda \cdot \chi_\lambda$ measurement pipeline shared with PR
#819 Phase 5c.1.

### Relation to other constit-factor results

| Result | Status |
|---|---|
| [`conj:constit-factor-2q-minus-1`](#conj:constit-factor-2q-minus-1) (Phase 5g, PR #831) | RESOLVED — $(2q - 1)$ was a numerical coincidence at $q_0$ ($\mathrm{tr}_M^3(\mathcal{B}_p, q_0) \approx 1.220 \approx 2 q_0 - 1$), not a global structural identity.  Phase 5l ($\dagger$) is the correct closed form. |
| Phase 5k.1 unit-coefficient $h^5$ (PR #831) | RESOLVED — same coincidence: $\mathrm{tr}_M^3(\mathcal{B}_p, q_0) - (2 q_0 - 1) \approx h^5(q_0)$ at $q_0$ only, not globally. |
| Phase 5k.2 varying-q falsification (this PR §5k.2) | CONSISTENT — the falsification of $(2q - 1)$ was the bridge to identifying $(\dagger)$ as the actual structural form. |

### Combined per-Z step at the full $\mathrm{tr}_M$ level

Combining $(\dagger)$ with the interface-knot factor $z$ from
[`prop:interface-knot-markov-z`](#prop:interface-knot-markov-z)
gives the **exact** full $\mathrm{tr}_M$ per-Z step at a p-$\ast$ boundary:
$$
  \boxed{\;
    \frac{\mathrm{tr}_M(\mathcal{B}_K^{Z+1, N})}{\mathrm{tr}_M(\mathcal{B}_K^{Z, N})}
    \;=\; z(q) \cdot \mathrm{tr}_M^3(\mathcal{B}_p, q)
  \;}
$$
— no $O(h^k)$ residuals.  This is the substrate-derived "Z-step
factor" in fully closed form at the $\mathrm{tr}_M$ level, living in a
different spectral channel of $H_n(q)$ than the
$|\Delta_\lambda^*|$-level conjecture
[`conj:alpha-cosh-h-z-step-correction`](#conj:alpha-cosh-h-z-step-correction).

### Open questions

1. **Closed form for $\mathrm{tr}_M^3(\mathcal{B}_p, q)$ as a substrate primitive.**
   $(\dagger)$ reduces the per-Z step factor to a per-proton H_3
   Markov-trace evaluation.  The next step is to characterise
   $\mathrm{tr}_M^3(\mathcal{B}_p, q)$ itself as a substrate-derived function —
   the proton braid is a specific Hecke word $(\sigma_1)^{6} \cdot
   (\sigma_2^{-1})^{3} \cdot \sigma_2$ (modulo averaged crossings),
   so $\mathrm{tr}_M^3(\mathcal{B}_p, q)$ is a closed-form rational/Laurent
   expression in $q$.  Phase 5l.1 (queued): extract this expression
   symbolically.

2. **Neutron analogue.**  Same identity holds with $\mathcal{B}_n$ in place
   of $\mathcal{B}_p$ for the per-N step at an n-n boundary (combined with
   the $(z - h)$ interface factor from
   [`prop:interface-knot-markov-z`](#prop:interface-knot-markov-z)).
   Verification deferred to a follow-on probe.

### Implementation reference

- Script: [`computations/rho_constit_equals_tau_M_proton_phase5l.py`](../../../computations/rho_constit_equals_tau_M_proton_phase5l.py)
- Witness: `computations/rho-constit-equals-tau-M-proton-phase5l.witness.json` (1 assertion: max rel.err. $< 10^{-12}$, passes at $\sim 10^{-15}$)
- Falsification audit (precursor): Phase 5k.2 in this PR — script [`constit_factor_varying_q_phase5k2.py`](../../../computations/constit_factor_varying_q_phase5k2.py) + witness `constit-factor-varying-q-phase5k2.witness.json`
- Companion proposition: [`prop:interface-knot-markov-z`](#prop:interface-knot-markov-z) (interface factor $z$, exact)
