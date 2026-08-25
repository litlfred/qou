**Remark (figure-8 knot as the canonical algebraic / archimedean
example).**

The figure-8 knot $4_1$ is the smallest hyperbolic knot
[`thurston1978`] and serves as the cleanest illustration of the
dual existence forced by
[`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness):
*algebraic / motivic in the substrate, transcendental in the
laboratory*.

**Embedding in Bring's surface.** The figure-8 knot embeds smoothly
into Bring's surface (genus $4$) as the amphichiral mass mechanism.
Its braid word $\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$ realises
on $4$ strands and the braid closure reproduces $4_1$ inside the
genus-$4$ handlebody. The amphichirality
$4_1 \cong 4_1^{\,\text{mirror}}$ — equivalently, invariance under
the bar involution $q \mapsto q^{-1}$ — is what selects the
figure-8 as a *mass* invariant rather than a chirality invariant.

**Pre-archimedean (substrate) representation.**
On the algebraic side, $4_1$ has a rigorous motivic
representation via its Hecke normal form. The
[algebraic quantum volume](#def:algebraic-quantum-volume) of $4_1$
is a finite product of Laurent polynomials,

$$
  \mathrm{Vol}_q(4_1)
  \;=\;
  \prod_{i=0}^{2} \hat{V}_i(q)
  \;\in\;
  \mathbb{Z}[q^{\pm 1/2}],
$$

with the $\hat{V}_i(q)$ explicitly determined by the four-strand
braid word above (cf.
[`thm:markov-trace-factorization`](#thm:markov-trace-factorization)).
At this level no $\pi$, no $\zeta$-values, no real-analytic
transcendentals appear: the entire object is a Laurent polynomial
in $q^{\pm 1/2}$ and lives strictly in the substrate ring $R$.

**Archimedean (laboratory) image.**
Apply the archimedean realization functor $\tau_{\text{arch}} =
\pi_\infty \circ \tau$
([archimedean realization functor](#def:archimedean-realization-functor)).
The image of $\mathrm{Vol}_q(4_1)$ under $\tau_{\text{arch}}$ in
the Faddeev-Kashaev quasi-classical limit is the *hyperbolic
volume* of the figure-8 knot complement
$S^3 \setminus 4_1$
([Kashaev volume conjecture](#conj:kashaev-volume-conjecture)),
which evaluates as the transcendental

$$
  \boxed{\;
    \mathrm{Vol}(4_1)
    \;=\;
    2\,D(\mathrm{e}^{i\pi/3})
    \;=\;
    2\,\mathrm{Cl}_2\!\left(\tfrac{\pi}{3}\right)
    \;\approx\;
    :val[Vol_4_1]{precision=6}\ldots
  \;}
$$

where $D$ is the Bloch-Wigner dilogarithm and $\mathrm{Cl}_2$ is
the Clausen function. The transcendence of $\mathrm{Cl}_2(\pi/3)$
is conjectural in number theory but the *form* of the answer is
forced by Bloch-Suslin pentagon-uniqueness: any archimedean
realization of the substrate's pentagon-coherent class must
factor through $D$, and the figure-8's three ideal-tetrahedron
triangulation pins down the specific shape parameter $z = e^{i\pi/3}$.

**The dichotomy in one line.**
The motivic side guarantees exact, $q$-rational algebraic
relationships governing particle interactions; $\tau_{\text{arch}}$
supplies the transcendental continuum required for geometric
measurement. Both pictures are needed:

| Side | Object for $4_1$ | Lives in | Role |
|---|---|---|---|
| Pre-archimedean | $\mathrm{Vol}_q(4_1) = \prod_i \hat{V}_i(q)$ | $\mathbb{Z}[q^{\pm 1/2}]$ | Exact algebraic identities, mass-formula state sum, Hecke trace |
| Archimedean | $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ | $\mathbb{R}$ (transcendental) | Laboratory mass-scale, Higgs-like amphichiral mechanism |

The bridge between the two columns is uniquely determined by
[`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness):
no other archimedean image is admissible.

**Cross-reference: $\alpha_{EM}$.** The same dichotomy underlies
the additive Bring zero-mode candidate
[`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode):
the $\pi$ in $4_1$'s archimedean image
$2\,\mathrm{Cl}_2(\pi/3)$ and the $\pi$ in $1/\alpha_{EM}$'s
correction $2/(3\pi) = 2g/(4\pi(g-1))$ at $g=4$ share a single
provenance — the unique archimedean shadow of pentagon-coherent
substrate data on Bring's surface, factored through the
Bloch-Wigner dilogarithm. The exact algebraic values $:val[Vol_4_1]{precision=6}\ldots =
2\,\mathrm{Cl}_2(\pi/3)$ matches the standard hyperbolic
2-tetrahedra triangulation [`thurston1978`].
