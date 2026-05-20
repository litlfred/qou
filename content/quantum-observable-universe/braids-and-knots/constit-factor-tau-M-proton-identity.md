**Proposition (Constit-side per-Z step factor = $\tau_M^3(\beta_p)$).**

*Let $\beta_K^{\mathrm{constit}}$ be the disjoint Hecke product
defining the constituent vacuum of atom $K = (Z, N)$ — per
[`def:ew-interface-knot`](#def:ew-interface-knot), the canonical
atomic braid with all interface generators removed.  Then the
constit-side per-Z step ratio admits the closed form*
$$
  \boxed{\;
    \rho_Z^{\mathrm{constit}}(q)
    \;:=\;
    \frac{\tau_M\!\bigl(\beta_{(Z+1, N)}^{\mathrm{constit}}\bigr)}
         {\tau_M\!\bigl(\beta_{(Z, N)}^{\mathrm{constit}}\bigr)}
    \;=\;
    \tau_M\!\bigl(\beta_p,\, H_3(q)\bigr)
  \;}
  \tag{$\dagger$}
$$
*for all $q$ in the substrate window, where $\beta_p \in H_3(q)$
is the canonical 3-strand proton braid (intra-nucleon crossings
only) and $\tau_M$ is the Jones–Markov trace.*

### Proof

The canonical atom braid factorises (per
[`def:ew-interface-knot`](#def:ew-interface-knot)) as
$$
  \beta_K \;=\; \beta_K^{\mathrm{constit}} \cdot \Delta_I^K,
$$
where $\beta_K^{\mathrm{constit}}$ is a **disjoint** Hecke product
of per-nucleon 3-strand factors: for atom $K = (Z, N)$ in ordering
$\mathrm{p}, \mathrm{p}, \ldots, \mathrm{n}, \mathrm{n}$,
$$
  \beta_K^{\mathrm{constit}} \;=\;
    \beta_p^{(1)} \otimes \beta_p^{(2)} \otimes \cdots
    \otimes \beta_p^{(Z)}
    \otimes \beta_n^{(1)} \otimes \cdots \otimes \beta_n^{(N)},
$$
each $\beta_p^{(k)}, \beta_n^{(k)} \in H_3(q)$, with the
$k$-th block on strands $\{3k+1, 3k+2, 3k+3\}$ and the $\otimes$
denoting parabolic embedding into $H_{3A}(q)$ with $A = Z + N$.

**Wenzl's disjoint Markov-trace multiplicativity**
([wenzl1988] §1.7) states that for any
$\alpha \in H_n(q)$ and $\beta \in H_m(q)$ acting on **disjoint
strand sets** inside $H_{n+m}(q)$,
$$
  \tau_M(\alpha \otimes \beta) \;=\; \tau_M(\alpha) \cdot \tau_M(\beta).
$$
Applying this inductively across the $A = Z + N$ disjoint nucleon
blocks of $\beta_K^{\mathrm{constit}}$,
$$
  \tau_M\!\bigl(\beta_K^{\mathrm{constit}}\bigr)
    \;=\; \prod_{k=1}^{Z} \tau_M(\beta_p^{(k)})
    \cdot \prod_{k=1}^{N} \tau_M(\beta_n^{(k)}).
$$
Since all proton blocks are isomorphic ($\beta_p^{(k)} = \beta_p$ as
abstract H_3 braids) and likewise all neutron blocks
($\beta_n^{(k)} = \beta_n$),
$$
  \tau_M\!\bigl(\beta_K^{\mathrm{constit}}\bigr)
    \;=\; \tau_M(\beta_p)^Z \cdot \tau_M(\beta_n)^N.
$$
The per-Z step ratio then satisfies
$$
  \rho_Z^{\mathrm{constit}}(q)
    \;=\;
    \frac{\tau_M(\beta_p)^{Z+1} \cdot \tau_M(\beta_n)^N}
         {\tau_M(\beta_p)^Z \cdot \tau_M(\beta_n)^N}
    \;=\; \tau_M(\beta_p),
$$
yielding $(\dagger)$. $\square$

### Empirical verification (Phase 5l, 50 dps)

Direct measurement at five $q$-values in the substrate window via
[`rho_constit_equals_tau_M_proton_phase5l.py`](../../../folio-assistant/computations/rho_constit_equals_tau_M_proton_phase5l.py),
recomputing $y_\lambda(q)$ (Wenzl bridge) and
$\chi_\lambda(\beta, q)$ (Hecke characters) at each $q$:

| $q$ | $\tau_M^3(\beta_p, q)$ | $\rho_Z^{\mathrm{constit}}(q)$ | rel. err. |
|---|---:|---:|---:|
| $1.050$ | $0.79284191942392$ | $0.79284191942392$ | $5.97 \times 10^{-16}$ |
| $1.080$ | $0.99328958564705$ | $0.99328958564705$ | $1.04 \times 10^{-15}$ |
| $1.10998$ ($q_0$) | $1.22037426648745$ | $1.22037426648745$ | $1.45 \times 10^{-15}$ |
| $1.130$ | $1.39054700525733$ | $1.39054700525733$ | $6.34 \times 10^{-16}$ |
| $1.170$ | $1.78584582119413$ | $1.78584582119413$ | $1.01 \times 10^{-15}$ |

The identity holds at **machine precision** ($\sim 10^{-15}$ in
f64) at every $q$ — confirming both the proposition statement and
the soundness of the $y_\lambda \cdot \chi_\lambda$ measurement
pipeline shared with PR #819 Phase 5c.1.

### Relation to other constit-factor results

| Result | Status |
|---|---|
| [`conj:constit-factor-2q-minus-1`](#conj:constit-factor-2q-minus-1) (Phase 5g, PR #831) | RESOLVED — $(2q - 1)$ was a numerical coincidence at $q_0$ ($\tau_M^3(\beta_p, q_0) \approx 1.220 \approx 2 q_0 - 1$), not a global structural identity.  Phase 5l ($\dagger$) is the correct closed form. |
| Phase 5k.1 unit-coefficient $h^5$ (PR #831) | RESOLVED — same coincidence: $\tau_M^3(\beta_p, q_0) - (2 q_0 - 1) \approx h^5(q_0)$ at $q_0$ only, not globally. |
| Phase 5k.2 varying-q falsification (PR #842) | CONSISTENT — the falsification of $(2q - 1)$ was the bridge to identifying $(\dagger)$ as the actual structural form. |

### Combined per-Z step at the full $\tau_M$ level

Combining $(\dagger)$ with the interface-knot factor $z$ from
[`prop:interface-knot-markov-z`](#prop:interface-knot-markov-z)
gives the **exact** full $\tau_M$ per-Z step at a p-$\ast$ boundary:
$$
  \boxed{\;
    \frac{\tau_M(\beta_K^{Z+1, N})}{\tau_M(\beta_K^{Z, N})}
    \;=\; z(q) \cdot \tau_M^3(\beta_p, q)
  \;}
$$
— no $O(h^k)$ residuals.  This is the substrate-derived "Z-step
factor" in fully closed form at the $\tau_M$ level, living in a
different spectral channel of $H_n(q)$ than the
$|\Delta_\lambda^*|$-level conjecture
[`conj:alpha-cosh-h-z-step-correction`](#conj:alpha-cosh-h-z-step-correction).

### Open questions

1. **Closed form for $\tau_M^3(\beta_p, q)$ as a substrate primitive.**
   $(\dagger)$ reduces the per-Z step factor to a per-proton H_3
   Markov-trace evaluation.  The next step is to characterise
   $\tau_M^3(\beta_p, q)$ itself as a substrate-derived function —
   the proton braid is a specific Hecke word $(\sigma_1)^{6} \cdot
   (\sigma_2^{-1})^{3} \cdot \sigma_2$ (modulo averaged crossings),
   so $\tau_M^3(\beta_p, q)$ is a closed-form rational/Laurent
   expression in $q$.  Phase 5l.1 (queued): extract this expression
   symbolically.

2. **Neutron analogue.**  Same identity holds with $\beta_n$ in place
   of $\beta_p$ for the per-N step at an n-n boundary (combined with
   the $(z - h)$ interface factor from
   [`prop:interface-knot-markov-z`](#prop:interface-knot-markov-z)).
   Verification deferred to a follow-on probe.

### Implementation reference

- Script: [`folio-assistant/computations/rho_constit_equals_tau_M_proton_phase5l.py`](../../../folio-assistant/computations/rho_constit_equals_tau_M_proton_phase5l.py)
- Witness: `folio-assistant/computations/rho-constit-equals-tau-M-proton-phase5l.witness.json` (1 assertion: max rel.err. $< 10^{-12}$, passes at $\sim 10^{-15}$)
- Falsification audit (precursor): [PR #842](https://github.com/litlfred/qou/pull/842) Phase 5k.2 (varying-q sweep)
- Companion proposition: [`prop:interface-knot-markov-z`](#prop:interface-knot-markov-z) (interface factor $z$, exact)
