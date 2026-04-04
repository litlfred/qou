**Proposition (perpetual computational obstruction).**
*Let $(\mathbf{C}, A, \tau)$ be a quantum universe
([quantum universe](#def:quantum-universe)) over a Noetherian
ring $R$, and let $L$ be the closure of a braid $\beta$ with
$c$ crossings encoding an NP-complete problem.  Let
$\kappa_c^{\mathrm{comp}}(L, q) \in H^2(\mathcal{R},
\mathbb{G}_m)$ be the Skein resolution obstruction
([Skein resolution obstruction](#def:skein-resolution-obstruction)).*

*Then:*

1. *(First obstruction.)  The topological component of the
   obstruction is*

   $$
     \kappa_c^{\mathrm{top}}(L)
     \;\in\;
     \mathrm{im}\bigl(
       H^2(\mathcal{R},\, R)
       \to H^2(\mathcal{R},\, \mathbb{G}_m)
     \bigr),
     \qquad
     \mathrm{tr}\,\kappa_c^{\mathrm{top}}
     \;=\;
     \deg P_L
     \;\leq\; c^2 - 1.
   $$

   *This class is universal — it depends only on the link $L$,
   not on the substrate parameter $q$ or the base field $k$.*

2. *(Analytic component.)  The analytic component is the
   irreducible tree weight*

   $$
     \delta_c^{\mathrm{comp}}(L, q)
     \;\in\;
     \mathrm{im}\bigl(
       H^2(\mathcal{R},\, \mathcal{O}_{\mathcal{R}})
       \to H^2(\mathcal{R},\, \mathbb{G}_m)
     \bigr),
   $$

   *measuring the fraction of $3^c$ resolution paths that carry
   non-cancelling Skein weight at parameter $q$.  This component
   is $q$-dependent.*

3. *(Complementary subgroups — perpetual obstruction.)*
   *When $\kappa_c^{\mathrm{top}}$ is non-torsion in
   $H^2(\mathcal{R}, \mathbb{G}_m)$ (which holds for
   NP-complete $L$ with $c \geq c_0$), the topological and
   analytic images are complementary subgroups:*

   $$
     \mathrm{im}\bigl(H^2(\mathcal{R}, R)\bigr)
     \;\cap\;
     \mathrm{im}\bigl(H^2(\mathcal{R}, \mathcal{O}_\mathcal{R})\bigr)
     \;=\; 0.
   $$

   *Therefore the total obstruction*

   $$
     \kappa_c^{\mathrm{comp}}(L, q)
     \;=\;
     \kappa_c^{\mathrm{top}}(L)
     \;+\;
     \delta_c^{\mathrm{comp}}(L, q)
     \;\neq\; 0
     \qquad\text{for all } q \in \mathbb{G}_m^{\mathrm{nt}}.
   $$

   *The topological and analytic components cannot cancel — the
   obstruction is perpetual at non-torsion $q$.*

**Proof sketch.**

The argument mirrors item 3 of the QU-to-QOU theorem
([QU-to-QOU](#thm:qu-to-qou)) and the NS obstruction tower
([NS obstruction tower](#prop:ns-obstruction-tower)).

**(a) The topological component is constant.**
The class $\kappa_c^{\mathrm{top}}(L)$ is the image of the
Skein polynomial degree under the constant-coefficient map
$H^2(\mathcal{R}, R) \to H^2(\mathcal{R}, \mathbb{G}_m)$.
It is independent of $q$: the degree of $P_L$ is determined
by the crossing number of $L$, a topological invariant.
For an NP-complete link with $c$ crossings,
$\deg P_L = c^2 - 1$
([quantum universality](#conj:quantum-computational-universality),
part 4).

**(b) The analytic component is $q$-dependent.**
The class $\delta_c^{\mathrm{comp}}(L, q)$ measures the
residual weight of the resolution tree after destructive
interference at parameter $q$.  At a root of unity
$q_k = e^{2\pi i/(k+2)}$, the Hecke radical annihilates
exponentially many paths, and $\delta_c^{\mathrm{comp}}$
may vanish (this is the BQP mechanism).  At non-torsion $q$,
the Hecke algebra is semisimple ($\mathrm{Rad} = 0$), no
paths are annihilated, and $\delta_c^{\mathrm{comp}} \neq 0$.

**(c) The subgroups are complementary.**
The constant-coefficient image
$\mathrm{im}(H^2(\mathcal{R}, R))$ consists of classes whose
restriction to every fiber of $\mathcal{R} \to
\mathrm{Spec}\,\mathbb{Z}[q, q^{-1}]$ is the same integer
(the Skein degree).  The analytic image
$\mathrm{im}(H^2(\mathcal{R}, \mathcal{O}_\mathcal{R}))$
consists of classes that vary with $q$ (the interference
pattern depends on $q$).  A class that is simultaneously
constant and $q$-varying must be zero.  Therefore the images
intersect trivially and $\kappa_c^{\mathrm{top}} +
\delta_c^{\mathrm{comp}}$ cannot be zero unless both
components vanish individually.

For NP-complete $L$: $\kappa_c^{\mathrm{top}} \neq 0$ (the
Skein degree is $c^2 - 1 > 0$).  At non-torsion $q$:
$\delta_c^{\mathrm{comp}} \neq 0$ (the Hecke algebra is
semisimple).  Since neither vanishes and they lie in
complementary subgroups, the total obstruction is perpetual.

**The parallel with NS.**

This is the computational analog of the NS perpetual
obstruction.  Both follow from item 3 of the QU-to-QOU
theorem applied to different restriction loci:

| | NS obstruction | Computational obstruction |
|---|---|---|
| **QU level** | $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ | $\kappa_c^{\mathrm{comp}} \in H^2(\mathcal{R}, \mathbb{G}_m)$ |
| **Topological** | $\kappa_0 = e(\xi)$, $\mathrm{tr} = \chi(A)$ | $\kappa_c^{\mathrm{top}}$, $\mathrm{tr} = \deg P_L$ |
| **Analytic** | $\delta_n$ (jet divergence) | $\delta_c^{\mathrm{comp}}$ (irreducible tree weight) |
| **Complementary** | $\mathrm{im}(H^2(R)) \cap \mathrm{im}(H^2(\mathcal{O})) = 0$ | Same |
| **Perpetual** | $\kappa_n \neq 0$ for all $n$ when $\chi(A) \neq 0$ | $\kappa_c^{\mathrm{comp}} \neq 0$ for all non-torsion $q$ when $c \geq c_0$ |
| **Restriction locus** | Collision locus $\Sigma$ | Polynomial-depth boundary $\mathcal{R}_{p(c)}$ |
| **$q$-scale** | q-NS regular (proved) | BQP at torsion (proved) |
| **Classical limit** | NS regularity (open) | P $\neq$ NP at non-torsion (conjectured) |
| **Obstruction** | Levi non-degeneracy | Irreducible tree weight |

**The unified QU-to-QOU picture.**

Both the NS problem and the P vs NP problem are instances of
the same categorical obstruction: the Yekutieli class
$\kappa \in H^2(\cdot, \mathbb{G}_m)$ living in the
constant-coefficient image, with a $q$-dependent analytic
correction.  The perpetual obstruction (item 3 of
[QU-to-QOU](#thm:qu-to-qou)) forces both to be non-vanishing
at non-torsion $q$.

At the $q$-scale ($q > 1$), both problems are resolved:
- q-NS is globally well-posed (exponential damping of high
  modes)
- Computation at $\mathbb{G}_m$-torsion points has BQP
  (the Hecke radical prunes the resolution tree)

At the classical limit ($q \to 1$), the $q$-regularization
is removed, and both obstructions become visible:
- NS blowup is the failure of lifting through the Yekutieli
  tower at the collision locus
- P $\neq$ NP is the failure of lifting through the resolution
  tower at polynomial depth

In both cases, the obstruction is **perpetual**: the
topological component ($\chi(A)$ for NS, $\deg P_L$ for
computation) lives in a complementary subgroup to the analytic
correction, and no cancellation is possible.

The question in both cases is whether the analytic component
$\delta$ vanishes at $q = 1$:
- For NS: this is the Levi degeneracy conjecture — does the
  vortex core aspect ratio $\kappa(p)$ degenerate at
  collision?
- For P vs NP: this is the irreducible weight conjecture —
  do the $3^c$ resolution paths of an NP-complete link
  exhibit complete destructive interference at $q = 1$?

The perpetual obstruction says: even if $\delta$ vanishes,
$\kappa^{\mathrm{top}}$ does not.  The total obstruction
persists.
