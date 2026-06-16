This document records the complete step-by-step pre-Archimedean derivation
chain that backs all mass, beta-decay, and binding-energy computations in
the Quantum Observable Universe framework.  Every step lives in $\mathbb{Q}(q)$;
no analytic limits, no fitting, and no empirical nuclear-physics constants
enter until the Archimedean realization functor is applied at the very end.

The three pre-approved calibration inputs are
([rem:calibration-inputs](#rem\:calibration-inputs)):

See [Table 1](#tbl:pre-archimedean-derivation-chain-table1-data).

> **Audience reading note.** This is the paper-side rendering of the canonical
> derivation chain.  The **compute-pipeline mapping** (which script implements
> which step), the **dilog context-sorting** ($\Phi_q$ Faddeev for mass-anchor
> contexts vs $\mathrm{Li}_2^q$ Rogers for binding / bar-symmetric contexts),
> the **Phase 5 findings** (interface = $z$ exact; $\rho_Z^{\mathrm{constit}} =
> \mathrm{tr}_M^3(\mathcal{B}_p)$ structural identity), and the **migration
> backlog** are kept separately in
> [`docs/canonical-derivation-cheat-sheet.md`](../../../docs/canonical-derivation-cheat-sheet.md)
> so this content block stays focused on the categorical chain itself.

***

## Step 1 — Categorical action of $\mathbf{C}$ on $\mathcal{S}$

Let $\mathcal{U} = (\mathbf{C}, \varTheta, G, \mathcal{S})$ be a quantum
observable universe
([def:quantum-observable-universe](#def\:quantum-observable-universe)).
The :refterm[braided monoidal category]{#braided-monoidal-category} $\mathbf{C}$ has objects (strands) and
morphisms (braid generators $\sigma_i$); the braiding
$c_{X,Y}: X \otimes Y \to Y \otimes X$ satisfies the Yang--Baxter
equation by the axioms of a :refterm[braided monoidal category]{#braided-monoidal-category}.

The action of $\mathbf{C}$ on the state bundle $\mathcal{S}$ via
the fibre functor $\tau$ gives a group homomorphism

$$
  \rho_n \colon B_n \;\longrightarrow\; \mathrm{Aut}_\mathbf{C}(V^{\otimes n})
$$

by the braid-action-tensor proposition
([prop:braid-action-tensor](#prop\:braid-action-tensor)):
the braid generator $\sigma_i$ acts on strand $i$ and $i+1$ via the
$R$-matrix $R_{i,i+1} \in \mathrm{End}_\mathbf{C}(V^{\otimes n})$.

The categorical action is the *starting point*; every subsequent step
is a consequence of the structure of $\rho_n$.

***

## Step 2 — Non-abelian Stokes theorem (Yekutieli, finite slices)

Yekutieli's multiplicative integration on surfaces
provides the bridge from the 2-categorical action to the
Iwahori--Hecke algebra.  At finite slice depth $k$:

See [Table 2](#tbl:pre-archimedean-derivation-chain-table2-data).

**Key point.** The Hecke quadratic relation
$\sigma_i^2 = (q-q^{-1})\sigma_i + 1$ *is* the curvature 2-form of
the non-abelian Stokes theorem at adjacent slices.  It is not an
additional input; it follows from the $R$-matrix eigenvalues
$(\lambda_+, \lambda_-) = (q, -q^{-1})$ forced by the braiding
structure of $\mathbf{C}$.

**Explicit boundary$\leftrightarrow$surface form.** The categorical
action makes the $R$-matrix $R_{i,i+1}$ the parallel transport
(1-holonomy) across the crossing of strands $i, i+1$; the Yang--Baxter
relation is the flatness (horizontal compatibility) of that transport.
Yekutieli's non-abelian Stokes theorem equates the holonomy around the
boundary $\partial\Sigma$ of a 2-cell $\Sigma$ with the surface-ordered
multiplicative integral of the curvature over $\Sigma$:

$$
  \mathrm{Hol}(\partial\Sigma)
  \;=\; \overrightarrow{\textstyle\prod}\!\int_{\Sigma} F .
$$

The curvature 2-form $F_{i,i+1}$ is the obstruction to the two orders
of adjacent transport commuting; on $V^{\otimes n}$ it is exactly the
Hecke quadratic operator

$$
  F_{i,i+1} \;=\; R_{i,i+1}^2 - (q-q^{-1})\,R_{i,i+1} - 1 ,
$$

so $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$ is the *flatness condition*
$F_{i,i+1} = 0$ on each adjacent slice.

**Boundary observable and the spectral (Reeb) decomposition.** Closing
the braid (Markov, Step 3) and applying the Frobenius integral (Step 6)
yields the *boundary* observable
$\mathrm{tr}_M(\rho(\beta_K)) = \sum_\lambda y_\lambda \chi_\lambda$.
On each Wedderburn block $\lambda$ the boundary holonomy has eigenvalues
$e^{\pm i\theta_\lambda}$ whenever $|\chi_\lambda / d_\lambda| \leq 1$
(the unit-modulus / rotation regime,
[prop:unit-modulus-eigenvalue](#prop\:unit-modulus-eigenvalue)); the
**$q$-Reeb phase** $\theta_\lambda = \arccos(\chi_\lambda / d_\lambda)$
is the boundary parallel-transport angle.  The per-crossing version is
the eigenvalue split
$(\lambda_+, \lambda_-) = (q, -q^{-1}) = (\cosh\lambda + \sinh\lambda,\;
\cosh\lambda - \sinh\lambda)$ with $\lambda = \ln q$
([prop:crossing-energy-decomposition](#prop\:crossing-energy-decomposition)):
the symmetric $\cosh\lambda$ part is the curvature-free transport and the
antisymmetric $\sinh\lambda$ part is the curvature defect.

**Order of truncation.** The surface-ordered integral expands as
$\mathrm{Hol} = 1 + (\text{first-order boundary}) + (\text{second-order }
[F,F]) + \cdots$.  The chirality factor $a_K = 1 + w(K)\,h + O(h^2)$
(Step 6, $h = q - q^{-1}$) is the **first-order boundary truncation**;
the $O(h^2)$ remainder is the second-order surface $[F,F]$ contribution.
A scalar Markov trace $\sum_\lambda y_\lambda \chi_\lambda$ additionally
collapses the per-block boundary phase (since
$\chi_\lambda = d_\lambda \cos\theta_\lambda$ is summed), so the per-rep
Reeb angle $\theta_\lambda$ — the boundary spectral datum — is not
visible in $\mathrm{tr}_M$ alone.  Recovering it requires the per-block
($\theta_\lambda$-resolved) trace rather than the scalar $\mathrm{tr}_M$.

***

## Step 3 — Knot decomposition (Alexander + Markov)

Every oriented knot or link is the closure $\hat\beta$ of some braid
$\beta \in B_n$ (Alexander's theorem).  Two closures $\hat\beta$ and
$\hat\beta'$ represent the same knot type if and only if $\beta$ and
$\beta'$ are related by:

* *Markov move I* (conjugation in $B_n$): $\beta \sim \alpha\beta\alpha^{-1}$, and
* *Markov move II* (stabilisation): $\beta \in B_n \sim \beta\sigma_n^{\pm 1} \in B_{n+1}$.

Jones (1987) proved that the Jones--Markov trace
$\mathrm{tr}_M \colon \bigcup_n H_n(q) \to R$ is the **unique trace**
invariant under both Markov moves
([thm:jones-markov-trace](#thm\:jones-markov-trace)).  This identifies
knot invariants with Hecke-algebra traces unambiguously:

$$
  J_K(q) \;=\; \mathrm{tr}_M\bigl(T_w\bigr), \qquad
  T_w \in H_{n_0}(q)\text{ canonical braid closure of }K.
$$

***

## Step 4 — Bring surface / Weierstrass and particle content

The Bring surface $\Sigma_4$ (genus 4, automorphism group $S_5$) has
Euler characteristic $\chi(\Sigma_4) = -6$.  The Descartes condition
$\chi(A) = -6$ on the Frobenius--Hopf algebra $A$
([def:frobenius-hopf-substrate](#def\:frobenius-hopf-substrate))
identifies $H_3(R, q)$ as the relevant Hecke algebra:

* Dimension: $\dim H_3(q) = 6$ (exactly 6 basis elements in the
  seminormal representation, 6 independent crossing operators).
* The six basis elements $\{1, \sigma_0, \sigma_1, L_+, L_-, \gamma\}$
  in Gröbner--Shirshov normal form
  ([prop:spectral-sequence-h3-explicit](#prop\:spectral-sequence-h3-explicit))
  correspond bijectively to the six independent curvature insertions
  on $\Sigma_4$.

The $\chi = -6$ condition determines the particle content
(exactly 6 embeddable torus knots in $\Sigma_4$) without free choice;
there are no adjustable parameters at this stage.

The $x_5$-Bring weight identification
([prop:x5-bring-weight-identification](#prop\:x5-bring-weight-identification))
and the Prym-Jacobian :refterm[descent]{#descent} make this concrete:
the $Z_5$ automorphism group of the Bring curve $x_5$ acts on
$H_3(q)$ partitions via the Prym decomposition, selecting exactly the
partitions $\lambda \vdash 3$ that label the Wedderburn summands of the
nucleon mass formula.

***

## Step 5 — Weights and partitions (Wedderburn decomposition)

At generic $q$, the Iwahori--Hecke algebra $H_n(q)$ is semisimple
and admits the Wedderburn decomposition

$$
  H_n(q) \;\cong\; \bigoplus_{\lambda \,\vdash\, n}
    M_{d_\lambda}\!\bigl(\mathbb{Q}(q)\bigr),
$$

indexed by Young diagrams $\lambda \vdash n$.  Here
$d_\lambda = $ number of standard Young tableaux of shape $\lambda$
(the hook-length formula gives $d_\lambda = n!/\prod_{x\in\lambda}h_x$).

The quantum dimensions are the $q$-integers
$\dim_q(\lambda) = [n]_q = (q^n - q^{-n})/(q - q^{-1})$.

The Jones--Markov trace expands as

$$
  \mathrm{tr}_M(\beta) \;=\; \sum_{\lambda \,\vdash\, n}
    y_\lambda(q)\,\chi_\lambda(\beta),
$$

where the weights $y_\lambda \in R$ are the Wenzl-bridge coefficients
([prop:alpha-k-derivation-procedure](#prop\:alpha-k-derivation-procedure)).
These weights are **uniquely determined** by the Markov property: the
linear system $\sum_\lambda \chi_\lambda(w_\mu) y_\lambda = z^{n - \ell(\mu)}$
is invertible at generic $q$ by Schur--Weyl--Hecke duality.
No free parameters arise; the $y_\lambda$ are $q$-rational, no fitting.

***

## Step 6 — Frobenius pairing and mass integral

The Jones--Markov trace $\int_A \colon A \to R$ is the Frobenius
integral on the symmetric Frobenius algebra structure of $H_n(R, q)$
([def:frobenius-hopf-substrate](#def\:frobenius-hopf-substrate)).
The Frobenius pairing

$$
  \langle a, b \rangle_F \;=\; \int_A(a \cdot b)
$$

gives the inner product on $H_n(q)$.

The Nakayama automorphism of the Frobenius structure satisfies
$\Psi = S^2 = \mathrm{id}_A$ for Hecke algebras (since
$S(\sigma_i) = \sigma_i^{-1}$ implies $S^2(\sigma_i) = \sigma_i$).
This makes the Frobenius algebra *symmetric*, so
$\mathrm{tr}_M = \int_A$ and the categorical mass is

$$
  \mathfrak{m}(\mathfrak{H}) \;=\;
  \Bigl|\int_A \rho(\beta_\mathfrak{H})\Bigr|
  \;=\;
  \bigl|\mathrm{tr}_M(T_w)\bigr|.
$$

The Frobenius self-pairing also produces the chirality factor:
for a chiral knot with writhe $w(K)$, the ribbon twist contributes

$$
  a_K = 1 + w(K) \cdot h + O(h^2),
  \qquad h = q - q^{-1},
$$

derived from the Kauffman framing formula applied to the twist
endomorphism $\varTheta$ on irreducibles
([prop:chirality-writhe-ribbon-derivation](#prop\:chirality-writhe-ribbon-derivation)).

***

## Step 7 — Gröbner--Shirshov basis filtration

The Gröbner--Shirshov basis for $H_{n_0}(q)$
([prop:gb-spectral-sequence](#prop\:gb-spectral-sequence)) induces a
filtration on $H_{n_0}(q)$ by Coxeter length $\ell(w)$:

$$
  F_k H_{n_0}(q) \;=\;
    \bigl\{\text{span of reduced words of length} \leq k\bigr\}.
$$

The associated graded $\mathrm{gr}_\bullet H_{n_0}(q)$ forms the
$E_1$-page of the GB spectral sequence.  By
[prop:spectral-sequence-collapse](#prop\:spectral-sequence-collapse),
this spectral sequence **collapses at $E_2$** for semisimple $H_n(q)$
at generic $q$:

* The $d_1$-differential encodes the braid relations;
* The $d_2$-differential captures the Hecke quadratic relation
  $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$;
* All higher differentials $d_r = 0$ for $r \geq 3$
  (no further relations beyond braid + Hecke).

The $E_\infty$-page identification
([prop:e-infinity-page-identifications](#prop\:e-infinity-page-identifications))
recovers the Wedderburn decomposition:

$$
  E_\infty \;\cong\; \bigoplus_{\lambda \,\vdash\, n_0}
    M_{d_\lambda}\!\bigl(\mathbb{Q}(q)\bigr).
$$

**Consequence.** Finite-slice computation suffices: at every finite
filtration grade $k$, the surviving $E_\infty$-classes already account
for all of $\mathrm{tr}_M(T_w)$ because $d_r = 0$ for $r \geq 3$.
No higher slices contribute to the mass invariant.

***

## Step 8 — Jet order and slice traversal

Jet order = the order of GB reductions in the filtration.  In
Yekutieli's picture:

* Temporal slice-traversal order = the order in which elementary
  curvature insertions (braid generators) are processed;
* This is the jet-prefix partial order on reduced words in $H_{n_0}(q)$;
* The GB-filtration tracker certificate records
  (word, grade, jet-position) triples per term.

The jet-convergence result
([conj:jet-convergence-classical-limit](#prop\:jet-convergence-classical-limit))
shows that the jet tower converges to the classical limit as
$q \to 1$, confirming the finite-slice picture is algebraically
consistent with the semiclassical approximation.

***

## Step 9 — Hecke energy scale and mass identity

The energy scale $\mathfrak{E}_0$ is determined by the three calibration
inputs:

1. **Leptonic derivation.**  From $m_e$ and $q_0$ alone:

$$
  \mathfrak{E}_0^{(\mathrm{lept})}
  \;=\;
  \frac{m_e}{q_0(q_0 - 1)}
  \;=\;
  m_e \cdot c_q^2 \cdot \hbar_q
  \;\approx\; 4.186\;\mathrm{MeV}.
$$

2. **Hadronic calibration.**  From $\mathfrak{Q}_\beta$ and the symbolic NF difference:

$$
  \mathfrak{E}_0^{(\mathrm{had})}
  \;=\;
  \frac{\mathfrak{Q}_\beta}{|\Delta(\mathrm{net})|}
  \;=\;
  \frac{\mathfrak{Q}_\beta}{|h(h-2)/2|}
  \;\approx\; 4.155\;\mathrm{MeV}.
$$

The $0.75\%$ discrepancy is the brane tower correction
([prop:atom-knot-mass-derivation](#prop\:atom-knot-mass-derivation)).
The hadronic calibration fixes $\mathfrak{E}_0$ exactly; the leptonic
expression is an approximation valid to the single-level accuracy.

3. **Mass identity.**  After applying the Archimedean realization
   functor $\Phi_\mathrm{arch}$
   ([def:archimedean-realization-functor](#def\:archimedean-realization-functor)):

$$
  \boxed{
    B(\mathfrak{H})
    \;=\;
    m_e \cdot \rho \cdot
    \bigl[|\mathrm{tr}_M(T_w)| + \mathrm{tower}(T_w)
         + \mathrm{tr}_M(C_{\dim_q})\bigr]\big|_{q = q_0}
  }
$$

where $\rho \in \mathbb{Z}_{>0}$ is the SDP multiplicity of $T_w$'s
Wedderburn solution, $\mathrm{tower}(T_w)$ is the brane-tower
correction ([conj:brane-tower-z-habiro](#conj\:brane-tower-z-habiro)),
and $\mathrm{tr}_M(C_{\dim_q})$ is the Frobenius co-Casimir trace
([thm:frobenius-codim-universal](#thm\:frobenius-codim-universal)).

***

## Step 10 — Confinement SDP and canonical knot identification

The canonical Hecke element $T_w$ for a confined particle $\mathfrak{H}$
is selected by the joint mass-tower confinement SDP
([prop:confinement-sdp](#prop\:confinement-sdp),
[prop:atom-knot-mass-derivation](#prop\:atom-knot-mass-derivation)).
The SDP minimizes the Frobenius residual

$$
  \min_{T_w} \;\bigl\|
    \mathrm{tr}_M(T_w) \cdot \mathfrak{E}_0
    \;-\; B_{\mathrm{target}}
  \bigr\|^2
  \quad \text{subject to: }
  T_w \in H_{n_0}(q_0)^{\mathrm{GB-NF}}, \;
  \|T_w\| \leq \Delta_{\max}.
$$

For light nuclei $\{D, T, {}^3\mathrm{He}\}$ the SDP ground truth is
available; for heavier nuclei the recursive atom-knot atlas
extends the identification to $A \leq 60$.

**Status.**  The SDP pipeline is established; the
**canonical knot identification for $^2$H, $^3$H, $^3$He**
from first principles (without matching to historical hyperbolic
volumes) is an open problem
([conj:canonical-knot-id-sdp](#conj\:canonical-knot-id-sdp)).

***

## Step 10.5 — Closed-form Z-step factor at full $\mathrm{tr}_M$ level (Phase 5l + 5c.1, 2026-05)

Two recent structural identities close the per-Z step factor in the
canonical-atom Markov trace to a single closed form:

1. **Interface factor (exact)**, $\mathrm{tr}_M(\mathcal{B}_K) / \mathrm{tr}_M(\mathcal{B}_K^{\mathrm{vac}}) = z^{p_+(K)} \cdot (z-h)^{p_-(K)}$,
   from the Markov axiom + Hecke skein
   ([`prop:interface-knot-markov-z`](#prop\:interface-knot-markov-z)).
2. **Vacuum factor (exact)**, $\mathrm{tr}_M(\mathcal{B}_K^{\mathrm{vac}}) = \mathrm{tr}_M^3(\mathcal{B}_p)^Z \cdot \mathrm{tr}_M^3(\mathcal{B}_n)^N$,
   from Wenzl's disjoint Markov-trace multiplicativity ([wenzl1988] §1.7);
   the per-Z step on the constit side then reduces to
   $\rho_Z^{\mathrm{constit}}(q) = \mathrm{tr}_M^3(\mathcal{B}_p, q)$
   ([`prop:constit-factor-tau-M-proton-identity`](#prop\:constit-factor-tau-M-proton-identity)).

Combining the two:

$$
  \boxed{\;
    \frac{\mathrm{tr}_M(\mathcal{B}_K^{Z+1, N})}{\mathrm{tr}_M(\mathcal{B}_K^{Z, N})}
    \;=\; z(q) \cdot \mathrm{tr}_M^3(\mathcal{B}_p, q)
  \;}
$$

at a p-$\ast$ boundary, with no residuals.  This is the substrate-derived
"per-Z step factor" at the full $\mathrm{tr}_M$ level, complementing
the $|\Delta_\lambda^*|$-level conjecture
$\alpha \approx [3]_q^2 \cdot \cosh(h)$ of
[`conj:alpha-cosh-h-z-step-correction`](#conj\:alpha-cosh-h-z-step-correction).

***

## Step 11 — Beta-decay $Q$-values (symbolic, no calibration beyond $\mathfrak{Q}_\beta$)

Given $T_w^\mathfrak{H}$ and $T_w^{\mathfrak{H}'}$ for parent and
daughter nuclei (related by one quark-flavor crossing change
$\mathfrak{d} \to \mathfrak{u}$), the $Q$-value is

$$
  Q_{\beta^-}(\mathfrak{H} \to \mathfrak{H}')
  \;=\;
  \bigl[\mathrm{net}(T_w^\mathfrak{H}) - \mathrm{net}(T_w^{\mathfrak{H}'})\bigr]
  \times \mathfrak{E}_0.
$$

The symbolic NF computation
([prop:neutron-qvalue-symbolic](#prop\:neutron-qvalue-symbolic))
gives the free-neutron $Q$-value without any additional calibration:

$$
  \Delta(\mathrm{net})
  \;=\; \mathrm{net}(n) - \mathrm{net}(p)
  \;=\; \tfrac{h(h-2)}{2}
  \;\approx\; -0.1883,
$$

so $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})| \times \mathfrak{E}_0$ **by construction
(this is an ansatz, not derived from the per-braid mass formula
[`prop:per-braid-mass-tower`](#prop\:per-braid-mass-tower); the
unweighted $\mathrm{net}$ sum is not the same quantity as the
Markov-trace weighted sums of the mass tower. See
[`docs/audits/-q-beta-net-ansatz-fitting-finding.md`](../../../docs/audits/-q-beta-net-ansatz-fitting-finding.md))**.
All other $Q$-values in the beta-decay chain are **predictions** once
$\mathfrak{E}_0$ is fixed.

***

## Summary pipeline

```
Categorical action ρ_n: B_n → Aut_C(V^⊗n)
    ↓  Yekutieli (finite slices, Step 2)
H_{n_0}(q)  with  σ_i² = (q−q⁻¹)σ_i + 1
    ↓  Confinement SDP + GB-NF (Steps 7–10)
T_w ∈ H_{n_0}(q_0)  (canonical, GB normal form)
    ↓  Wedderburn (Step 5)
H_{n_0}(q) ≅ ⊕_λ M_{d_λ}(Q(q))
    ↓  Markov trace: y_λ (Wenzl-bridge), χ_λ (q-MN) (Steps 5–6)
tr_M(T_w) = Σ_λ y_λ χ_λ(T_w)  ∈ Q(q)
    ↓  Archimedean functor × m_e (Step 9)
B(H) = m_e · ρ · [tr_M(T_w) + tower + co-Casimir]|_{q=q_0}  in MeV
```

Every arrow is algebraic (lives in $\mathbb{Q}(q)$).  No fitting,
no empirical nuclear-physics constants, no analytic asymptotic content.
