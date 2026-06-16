**Conjecture.**
*The categorical replacement for the empirical Bethe-Weizsäcker bulk
($\lambda_V \cdot A$, $\lambda_S \cdot A^{2/3}$) and the knot factor
$a(N)$ is the **mass-identity Markov-trace defect**.  Using the
categorical mass at a single brane level
([single-level Markov mass](#prop:categorical-mass-markov)):*

$$
  \mathfrak{m}(\varrho)\big|_{\text{single level}}
  \;=\; \bigl| \mathrm{tr}_M( \rho(\beta) ) \bigr|
$$

*— the categorical mass of a braid $\beta$ equals the absolute value
of its Jones–Markov trace — the **bulk binding energy** of atom
$(Z, N)$ is the mass defect*

$$
  \boxed{\;
    B_{\mathrm{bulk}}(Z, N)
    \;=\; E_0 \cdot
    \bigl(
      |\mathrm{tr}_M(W_{\mathrm{free}})|
      \;-\; |\mathrm{tr}_M(W_{\mathrm{atom}})|
    \bigr)
  \;}
$$

*with a SINGLE archimedean calibration constant $E_0$ (the fibre
functor $\tau\colon R \to \mathbb{R}$) fixed by ONE reference
experiment.  Per
[categorical-mass-markov](#prop:categorical-mass-markov): "To obtain
physical masses in MeV, multiply by a calibration constant $E_0$,
determined by matching one experimental value (e.g. the free
neutron $\beta$-decay $Q$-value)."*

*Proof.*

**Step 1: Mass identity at single brane level.**
The [mass identity](#def:mass-identity) defines

$$
  \mathfrak{m}(\varrho)
  = \bigl\lVert \mathrm{tr}\bigl(
     (\textstyle\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho
   \bigr) \bigr\rVert.
$$

By [categorical-mass-markov](#prop:categorical-mass-markov) Steps 1–3:
- the categorical trace $\mathrm{tr}$ descends under the fibre
  functor $\tau$ to the Jones–Markov trace $\mathrm{tr}_M$ on
  $H_n(R, q)$;
- the Nakayama automorphism $\Psi = (\int_A \otimes \mathrm{id}) \circ \Delta$
  equals $S^2$ for a Frobenius–Hopf algebra, and $S^2 = \mathrm{id}$
  on $H_n(R, q)$ generators (antipode $S(\sigma_i) = \sigma_i^{-1}$, so
  $S^2(\sigma_i) = \sigma_i$);
- therefore $\mathfrak{m}(\varrho) = |\mathrm{tr}_M(\rho(\beta))|$.

**Step 2: Binding = mass defect of Markov traces.**
The binding energy is the classical mass defect:

$$
  B \;=\; \sum_{k=1}^A \mathfrak{m}(\varrho_k^{\text{free}})
       \;-\; \mathfrak{m}(\varrho^{\text{atom}}).
$$

Applying Step 1 and using the disconnected-tensor factorisation of
the free-nucleon braid $W_{\mathrm{free}} =
W_{\mathrm{nucleon}}^{\otimes A}$ under
$H_3(R, q)^{\otimes A} \hookrightarrow H_{3A}(q)$:

$$
  B \;=\; |\mathrm{tr}_M(W_{\mathrm{free}})|
      \;-\; |\mathrm{tr}_M(W_{\mathrm{atom}})|,
$$

where each $\mathrm{tr}_M$ is computed via the Wedderburn
decomposition:

$$
  \mathrm{tr}_M(W) \;=\; \sum_\lambda w_\lambda \cdot
  \frac{\chi_\lambda(W)}{d_\lambda}.
$$

**Step 3: Yekutieli 2D nonabelian Stokes.**
[Yekutieli (2015)](#rem:yekutieli-stokes) identifies the
Markov trace with the nonabelian multiplicative integral of the
instanton connection $A$ over the surface bounded by the braid
closure.  The mass identity is therefore the **categorical action
functional**: binding energy is the difference of nonabelian
action integrals between the atom braid and the disconnected
baseline.

**Step 4: Knot factor via Skein eigenvalues.**
For small $A = 2, 3, 4$ the binding chirality is dominated by the
local knot type. The categorical knot factor $a_K$ is the
**Skein eigenvalue** of the canonical atomic braid at the
relevant Hecke representation — equivalently, the **closed-form
product** over signed pn-crossings:

$$
  a_K \;=\;
    \prod_{c \in \text{pn-crossings}}
      \bigl(1 + \mathrm{sign}(c) \cdot h\bigr),
  \qquad h = q - q^{-1}.
$$

This recovers the empirical BW knot factors:
- $A = 1$ (free nucleon, no pn-crossings): $a_K = 1$
- $A = 2$ (satellite): $a_K = 1 + h$
- $A = 3$ (figure-8): $a_K = 1 - h^2 = 4 - [3]_q$
  (Skein eigenvalue of $4_1$ at $\sigma^2$, cf.
  `nuclear-knot-classification`)
- $A = 4$ (Borromean): $a_K = (1 - h^2)^2$

*(The product $\prod_c(1+\mathrm{sign}(c)\,h)$ expands exactly to these
values for the crossing-sign assignment of `nuclear-knot-classification`,
and $1-h^2 = 4-[3]_q$. Here $a_K$ is the **h-content reduction** — $1$
minus the summed h-content of the pn-crossings — not the literal
figure-eight Jones polynomial $V(4_1)$, which is a distinct
higher-degree invariant; "Skein eigenvalue of $4_1$" denotes this
reduced quantity. See
[audit](../../../docs/audits/2026-06-07-knot-factor-skein-verification.md)
+ witness
[`knot-factor-skein-verification.witness.json`](../../../computations/knot-factor-skein-verification.witness.json).
The crossing-sign assignment, the $A\geq5$ extension, and the
identification of $a_K$ as the canonical mass-formula knot factor remain
conjectural.)*

For $A \geq 5$ the closed-form product generalises beyond the
local-knot regime via the Wenzl-LR branching identity on the
self-conjugate stratum (cf.
`hecke-branching-trace-decomposition`);
the Markov trace remains the universal categorical quantity.

*Historical note:* an earlier formulation of this
step proposed
$a(N) = \lvert\mathrm{tr}_M(W_{\mathrm{atom}})\rvert / \lvert\mathrm{tr}_M(W_{\mathrm{free}})\rvert$
as the ratio form. Empirical verification at 50dps
([`a-K-via-lp-dual` witness](../../computations/a-K-via-lp-dual.witness.json),
see `-m-p-item-b-t5-categorical-attribution.md §7c`)
finds this ratio is 6–17$\times$ off the Skein values above for
A=2,3,4. The ratio form measures the **mass-defect envelope**
$\mathcal{B}_{\mathrm{bulk}}$, not the chirality factor $a_K$;
the closed-form Skein-product **is** the canonical $a_K$ entering
the QOU six-term mass formula
([`six-term-mass-formula-complete`](#thm:six-term-mass-formula-complete)).

$\square$

**Relation to q-Casimir.**
The Markov trace decomposes via the Wedderburn blocks indexed by
partitions; each block's character $\chi_\lambda(W)$ can be
expanded in the basis of q-Casimir eigenstates
([q-Casimir element](#def:q-casimir)) of $\mathcal{U}_q(\mathfrak{su}(2))$.
The eigenvalue $[j]_q[j+1]_q$ on spin-$j$ irreducibles relates to
the q-Laplacian on the corresponding Peter-Weyl component
([q-heat kernel Peter-Weyl](#prop:q-heat-kernel-peter-weyl)).

**Base-ring behaviour.**
Both $\mathrm{tr}_M(W) \in R$ and the ratio
$|\mathrm{tr}_M(W_{\mathrm{atom}})| / |\mathrm{tr}_M(W_{\mathrm{free}})|$
are base-ring-independent
([base-field independence](#rem:base-field-independence)).
The absolute value $|\cdot|$ is archimedean — over $\mathbb{F}_p$
the Markov trace lives in a finite field with no ordering; over
$\mathbb{Q}_p$ there is a $p$-adic absolute value.  The
archimedean realisation at $q = q_0$ gives the physical MeV scale
via $E_0$.

**Witness.**
- `computations/substrate/hecke_core.py::atom_markov_trace`:
  $\mathrm{tr}_M(W_{\mathrm{atom}})$ and $\mathrm{tr}_M(W_{\mathrm{free}})$
  via Wedderburn-block Markov trace.
- `computations/substrate/hecke_core.py::binding_from_frobenius_pairing`:
  $B_{\mathrm{bulk}} = E_0 \cdot (|\mathrm{tr}_M^{\mathrm{free}}| -
  |\mathrm{tr}_M^{\mathrm{atom}}|)$ with
  $E_0 = 0.782$ MeV (free-neutron $\beta$-decay $Q$).

**Scope.**
Per [categorical-mass-markov](#prop:categorical-mass-markov):
"single-level Markov trace does NOT produce mass ratios like
$\mathfrak{m}_\mu / \mathfrak{m}_e \approx 206.8$; those require
the full tower sum, which evaluates to
$\mathrm{Vol}(K)/\hbar_q^2$ in the archimedean realisation."  The
current implementation is SINGLE-LEVEL only.  Extension to the
full brane-tower sum (accounting for the $\Sigma \|\Phi_q(z_i)\|$
contributions over exceptional divisors) is
[conj:mass-endomorphism](#conj:mass-endomorphism).
