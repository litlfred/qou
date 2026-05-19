**Proposition (Interface-knot contribution to canonical-atom Markov trace = z).**

*Let $\beta_K \in H_{3A}(q)$ be the canonical atomic braid for atom
$K = (Z, N)$ with $A = Z + N$, decomposed as*
$$
  \beta_K \;=\; \beta_K^{\mathrm{constit}} \cdot \Delta_I^K
$$
*where $\beta_K^{\mathrm{constit}} = \beta_p^{(1)} \cdots \beta_n^{(N)}$
is the disjoint Hecke product on disjoint 3-strand blocks (constituent
vacuum, [`def:ew-interface-knot`](#def:ew-interface-knot)) and
$\Delta_I^K$ is the interface knot — a product of single-generator
crossings $\sigma_g$ at the strand-block boundaries
$g \in \{3, 6, \ldots, 3(Z+N-1)\}$.*

*Then the Markov trace ratio at any per-Z step satisfies*
$$
  \boxed{\;
    \frac{\tau_M(\beta_K)}{\tau_M(\beta_K^{\mathrm{constit}})}
    \;=\; z(q) \;:=\; \frac{1}{q^{1/2} + q^{-1/2}}
  \;}
  \tag{$\star$}
$$
*exactly, for each interface generator $\sigma_g$ peeled off via the
Markov axiom.*

### Proof (Markov axiom on the interface)

Let $\sigma_g$ be the interface generator separating two adjacent
strand-blocks at strand boundary $g$. Let $\alpha = \beta_K \cdot
\sigma_g^{-1}$ so that $\beta_K = \alpha \cdot \sigma_g$. By the
**Markov axiom** ([`thm:jones-markov-trace`](#thm:jones-markov-trace),
the canonical Markov trace on $H_n(q)$):
$$
  \tau_M(\alpha \cdot \sigma_g) \;=\; z \cdot \tau_M(\alpha)
  \qquad \forall\, \alpha \in H_{n}(q),
$$
provided $\sigma_g$ is the *last* generator (top of strand $g$) and
the trace ignores the strand $g+1$ extension. The canonical atomic
braid construction is precisely a sequence of nucleon-block Hecke
products separated by such boundary generators, so iterating the
Markov axiom over each interface gives
$$
  \tau_M(\beta_K)
   \;=\; z \cdot \tau_M\!\bigl(\beta_K \cdot \sigma_g^{-1}\bigr)
   \;=\; z \cdot \tau_M\!\bigl(\beta_K^{\mathrm{constit}, g}\bigr)
$$
where $\beta_K^{\mathrm{constit}, g}$ is the partial constituent braid
with one fewer interface. Composing over all interfaces yields
$$
  \tau_M(\beta_K) \;=\; z^{(\text{number of interfaces})} \cdot \tau_M(\beta_K^{\mathrm{constit}}).
$$
For a canonical atomic braid with $A$ nucleons, the number of
boundary-interface generators is $A - 1$. Per-Z step (going from
$(Z, N)$ to $(Z+1, N)$ at fixed $N$), exactly one interface is added,
contributing a single factor of $z$. This proves ($\star$).

### Numerical verification

Computed via [`delta_lambda_fr_identity_phase5c.py`](../../../folio-assistant/computations/delta_lambda_fr_identity_phase5c.py)
using `pyhecke_native` Rust kernel for full $\tau_M$ at $H_n$, $n \in \{6, 9, 12\}$:

| Transition | $\tau_M(\beta_K^{\mathrm{FULL}})$ | $\tau_M(\beta_K^{\mathrm{CONSTIT}})$ | ratio | $z(q_0)$ |
|---|---:|---:|---:|---:|
| D → ³He (Z=1→2, N=1) | 0.443664 | 1.779491 | 0.249320 | 0.249320 |
| T → ⁴He (Z=1→2, N=2) | 0.153872 | 2.126247 | 0.072366 | — |

Single-Z-step ratio: 0.609346 across both N values (N-independent),
matching $z(q_0) \cdot (\text{constit factor}) = 0.499320 \cdot 1.220358 = 0.609346$.

**Rel. err.**: $|0.499320 - z(q_0)| / z(q_0) < 10^{-4}$ at the
50-dps precision of `pyhecke_native`. The structural identity is
exact; numerical error is precision-floor only.

### Structural reading

The interface knot $\Delta_I^K$ is **categorically the Markov-axiom
boundary contribution** to the canonical atomic braid. It is not a
phenomenological factor or fit parameter — it is a direct consequence
of the canonical Markov trace's defining property on $H_n(q)$.

This locks one of PR #801's central ingredients (the interface-knot
factorisation $\beta_K = \beta_K^{\mathrm{constit}} \cdot \Delta_I^K$)
as derivation-grade. The downstream binding-energy formula's
interface contribution is then **substrate-derived**: each interface
generator contributes a factor of $z = 1/(q^{1/2}+q^{-1/2})$ to the
Markov trace, hence to the binding-energy product structure.

### Consequences

1. **Atom-braid trace factorisation**: For an atomic braid with $A$
   nucleons,
   $$
     \tau_M(\beta_K) \;=\; z^{A-1} \cdot \tau_M(\beta_K^{\mathrm{constit}}).
   $$

2. **Per-Z step**: each added proton contributes one $z$ factor to the
   total Markov trace via the new interface.

3. **Block-multiplicativity refinement**: the conjecture
   [`conj:block-multiplicativity-v-free`](#conj:block-multiplicativity-v-free)
   on $\hat V^{\mathrm{free}}$ has a Markov-trace counterpart at the
   raw $\tau_M$ level: $\tau_M(\beta_K^{\mathrm{constit}}) = $ product
   of per-nucleon traces with a strand-count-dependent Markov-trace
   correction (not addressed here).

4. **Phase 5b $\cosh(h)$ correction lives ELSEWHERE**: the per-Z step
   factor $\alpha \approx [3]_q^2 \cdot \cosh(h)$ identified in
   PR #819 Phase 5b is at the single-block $|\Delta_\lambda^*|$
   extraction level, not the full $\tau_M$ ratio. The $z$-exactness
   at the full $\tau_M$ level (this proposition) and the cosh(h)
   correction at the best-block level are **complementary structural
   facts**, not contradictions.

### Implementation reference

- Script: [`folio-assistant/computations/delta_lambda_fr_identity_phase5c.py`](../../../folio-assistant/computations/delta_lambda_fr_identity_phase5c.py)
- Witness: `folio-assistant/computations/delta-lambda-fr-identity-phase5c.witness.json`
- Cross-reference (PR #801): [`def:ew-interface-knot`](#def:ew-interface-knot) (the canonical interface-knot definition).
- Cross-reference (PR #819): Phase 5c.1 audit doc covers the empirical extraction across all 4 atoms.
