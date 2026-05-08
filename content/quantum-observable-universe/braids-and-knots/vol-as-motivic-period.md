**Reading.**
The hyperbolic volume $\mathrm{Vol}(S^3 \setminus K)$ of a hyperbolic
knot complement is a *motivic period* — specifically, the value of a
mixed-Tate motive under the **Bloch--Wigner regulator** $r_\infty$.
Under this reading, the
[archimedean realization functor](#def:archimedean-realization-functor)
is the period-evaluation map: it takes a class in the (quantum) Bloch
group and returns its archimedean image in $\mathbb{R}$.

**Period interpretation.**
A *period*, in the sense of Kontsevich--Zagier, is a complex number
expressible as the integral of an algebraic differential form over a
domain cut out by polynomial inequalities with rational coefficients.
For a hyperbolic knot complement triangulated with shape parameters
$z_1, \ldots, z_k \in \overline{\mathbb{Q}}$ satisfying Thurston's
gluing equations, the volume is

$$
  \mathrm{Vol}(S^3 \setminus K)
  \;=\;
  \sum_{i=1}^{k} D(z_i),
\qquad
D(z) := \operatorname{Im}\,\mathrm{Li}_2(z)
       + \log|z|\cdot\arg(1-z),
$$

where $D$ is the **Bloch--Wigner dilogarithm**. Each summand $D(z_i)$
is the period of an algebraic 1-form on $\mathbb{P}^1\setminus\{0,1,\infty\}$
integrated over a cycle determined by $z_i$, hence a period in the
Kontsevich--Zagier sense [`zagier1986`,`neumann-zagier1985`].

**Regulator interpretation.**
Equivalently, the shape parameters define a class
$[K] \in \mathcal{B}(\overline{\mathbb{Q}})$ in the (pre-)Bloch group,
and

$$
  \mathrm{Vol}(S^3 \setminus K)
  \;=\;
  r_\infty\bigl([K]\bigr),
$$

where $r_\infty : \mathcal{B}(\mathbb{C}) \to \mathbb{R}$ is the
archimedean Beilinson regulator restricted to the Bloch group. Under
this perspective, $\mathrm{Vol}(K)$ is exactly $K$-theoretic — the
image of an algebraic $K$-theory class under a transcendental
regulator.

**QOU placement.**
The
[archimedean realization functor](#def:archimedean-realization-functor)
already factorises as $\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$
on motivic inputs and as $\pi_\infty \circ \chi_{\mathrm{top}}$ on
arc-space inputs. The Bloch--Wigner reading is the third equivalent
factorisation, restricted to inputs that come from
$\mathrm{Vol}_q$:

$$
  \tau_{\mathrm{arch}}\!
  \begin{pmatrix}
    \text{algebraic quantum volume}\\
    \mathrm{Vol}_q(\beta_K) \in \mathbb{Z}[q^{\pm 1/2}]
  \end{pmatrix}
  \;=\;
  r_\infty\!\bigl([K]\bigr)
  \;=\;
  \mathrm{Vol}(S^3 \setminus K).
$$

The three pictures — adelic projection, Euler-characteristic
realization, Bloch--Wigner regulator — agree on this common domain.
Each is useful for a different formal manipulation:

* The **adelic** picture
  ([archimedean realization functor](#def:archimedean-realization-functor))
  is what controls the *categorical* compatibility ($\tau_{\mathrm{arch}}$
  factoring through the QOU fibre functor $\tau$).
* The **Euler-characteristic** picture
  ([motivic mass measure](#def:motivic-mass-measure)) governs the
  blow-up calculus for arc-space integrals.
* The **Bloch--Wigner / regulator** picture is the one that connects
  $\mathrm{Vol}_q$ to existing motivic-cohomology and quantum-topology
  literature (Kashaev, Murakami--Murakami, Garoufalidis--Zagier).

**Scope.**
This is an *interpretive remark*: it makes no new mathematical claim
beyond what is in
[$\mathrm{Vol}(K)$ factors through $\tau$](#prop:vol-through-tau).
It simply names the existing factorisation in motivic-period
language so that the
[Kashaev volume conjecture](#conj:kashaev-volume-conjecture) and the
[archimedean remainder decay conjecture](#conj:archimedean-remainder-exponential-decay)
can be cross-referenced cleanly with the regulator literature.
