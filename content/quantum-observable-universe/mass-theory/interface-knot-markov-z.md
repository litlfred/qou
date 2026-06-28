**Proposition (Interface-knot contribution to canonical-atom Markov trace).**

*Let $\mathcal{B}_K \in H_{3A}(q)$ be the canonical atomic braid for atom
$K = (Z, N)$ with $A = Z + N$, decomposed as*
$$
  \mathcal{B}_K \;=\; \mathcal{B}_K^{\mathrm{vac}} \cdot \bowtie_K
$$
*where $\mathcal{B}_K^{\mathrm{vac}} = \mathcal{B}_p^{(1)} \cdots \mathcal{B}_n^{(N)}$
is the disjoint Hecke product on disjoint 3-strand blocks (constituent
vacuum, `def:ew-interface-knot`) and
$\bowtie_K$ is the interface knot — a product of single-generator
crossings at the strand-block boundaries
$g \in \{3, 6, \ldots, 3(Z+N-1)\}$, each one either $\sigma_g$
(positive) or $\sigma_g^{-1}$ (negative).*

*Then the Markov trace ratio satisfies the **Markov-axiom interface
identity***
$$
  \boxed{\;
    \frac{\tau_M(\mathcal{B}_K)}{\tau_M(\mathcal{B}_K^{\mathrm{vac}})}
    \;=\; z(q)^{p_+(K)} \cdot \bigl(z(q) - h(q)\bigr)^{p_-(K)}
  \;}
  \tag{$\star$}
$$
*exactly, where $z(q) = 1/(q^{1/2}+q^{-1/2})$ is the Markov parameter,
$h(q) = q - q^{-1}$ is the Hecke skein parameter, and $p_+(K)$ /
$p_-(K)$ are the counts of positive / negative interface generators
in $\bowtie_K$.*
### Corollaries

1. **Atom-braid trace factorisation.** For any canonical atomic braid:
   $$
     \tau_M(\mathcal{B}_K) \;=\; z^{p_+(K)} \cdot (z-h)^{p_-(K)} \cdot \tau_M(\mathcal{B}_K^{\mathrm{vac}}).
   $$
   This iterated product is formalised sorry-free as the theorem
   `interface_knot_markov_z` (Lean), proved by induction over the interface
   list from the two single-step identities (`interface_knot_markov_z_single`
   for $z$, `interface_knot_markov_z_negative` for $z-h$).

2. **Per-Z step.** Adding a proton (Z+1) inserts one positive interface
   (p-* boundary): $\tau_M$ multiplies by $z$.

3. **Per-N step within a pair.** Adding a neutron after an existing
   neutron (n-n boundary) inserts one negative interface: $\tau_M$
   multiplies by $z - h$ (not by $z$).

4. **Per-N step crossing pair-flavor.** Adding a neutron after a proton
   (p-n boundary) inserts one positive interface: factor $z$.

5. **Phase 5b $\cosh(h)$ correction lives ELSEWHERE.** The per-Z step
   factor $\alpha \approx [3]_q^2 \cdot \cosh(h)$ identified in
   `conj:alpha-cosh-h-z-step-correction`
   is at the **single-block $|\Delta_\lambda^*|$ extraction level**,
   not the full $\tau_M$ ratio. The $\tau_M$-level identity is
   *exact* ($\star$); the single-block-level correction is *empirical*
   and structurally distinct.

### Proved structural corollaries (binding assembly)

Two correctly-scoped structural facts about the binding assembly
`B = E_0\,\tau_M(\mathcal{B}_K^{\mathrm{vac}})\,(1-\prod_i f_i)` are formalised
sorry-free alongside the interface identity (same `.lean` file):

1. **Interface-deficit saturation** (`QOU.BraidKnot.InterfaceDeficit`). For bond
   factors $f_i \in [0,1]$ the deficit $D = 1-\prod_i f_i$ satisfies
   $0 \le D \le 1$, is monotone in the bond list, and the marginal deficit of an
   added bond is $(1-f)\prod < 1-f$. This is the *proved* form of the 4-body
   assembly observation: the multiplicative deficit **saturates** (extra bonds
   contribute ever less) — it does **not** show the interface program is
   excluded, only that the bond *count/topology* cannot supply unbounded scaling.
2. **SU(4) shell closure** (`QOU.BraidKnot.SU4Supermultiplet`). The
   fully-antisymmetric Wigner supermultiplet $[1^A] = \Lambda^A(\mathbb{C}^4)$ has
   dimension $\binom{4}{A}$, so it vanishes for $A>4$: ${}^4\mathrm{He}$ (the SU(4)
   singlet) is the last s-shell supermultiplet. Theorem `su4_shell_closure`.

### Implementation reference

- formalism: the canonical formalism
- Witness: `computations/delta-lambda-fr-identity-phase5c.witness.json` (2 assertions; **Markov-axiom interface identity passes to $10^{-15}$ rel. err.**)
- Cross-reference: `def:ew-interface-knot` (the canonical interface-knot definition).
- Cross-reference: Phase 5c.1 audit doc covers the empirical extraction; this proposition is the categorical resolution.
