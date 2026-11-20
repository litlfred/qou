The categorical action $S = \mathrm{tr}(\Phi)$
([topological mass](#conj:topological-mass)) evaluates differently
depending on the geometry of the knot complement $S^3 \setminus K$.
The piecewise geometric invariant

$$
  \mathrm{Geom}(K) =
  \begin{cases}
    \mathrm{Vol}(K) / \hbar_q^2
      & K \text{ hyperbolic} \\[4pt]
    \mathrm{CS}(K) \cdot \hbar_q^2
      & K \text{ torus} \\[4pt]
    0 & K \text{ unknot}
  \end{cases}
$$

routes the physical weight of a state through its fundamental
topological geometry.  Each of the three cases arises from an established theorem in
low-dimensional topology.

**1. The piecewise split: Thurston's Geometrization.**
Thurston's theorem for knot complements states that
$S^3 \setminus K$ admits exactly one of three geometric structures:
(i) a hyperbolic metric of constant negative curvature (the vast
majority of knots), (ii) a Seifert-fibred structure (torus knots,
Vol $= 0$), or (iii) a decomposition along tori into simpler pieces
(satellite knots).  The piecewise definition of $\mathrm{Geom}(K)$
follows this classification directly.

**2. The hyperbolic case: the Volume Conjecture.**
For hyperbolic $K$, $\mathrm{Geom}(K) = \mathrm{Vol}(K)/\hbar_q^2$.
This originates from the Kashaev--Murakami--Murakami Volume Conjecture:
the asymptotic growth of the coloured Jones polynomial $J_K^{(n)}(q)$
at roots of unity is dominated by $\mathrm{Vol}(K)$.  In the
categorical framework, $c_K = \mathrm{tr}_M(\rho(\mathcal{B}_K))$ is the
Hecke algebra Frobenius character of the braid $\mathcal{B}_K$, and its
leading asymptotics recover $\mathrm{Vol}(K)$.  Division by
$\hbar_q^2 = (1 - 1/q)^2$ maps the topological volume to a
mass/energy scale.

**3. The torus case: Chern--Simons dominance.**
For torus knots $K = T_{m,n}$, the hyperbolic volume vanishes.  The
topological weight is purely the phase of the path integral, which is
the Chern--Simons invariant

$$
  \mathrm{CS}(T_{m,n})
  = \frac{\pi^2(m^2-1)(n^2-1)}{12mn}.
$$

Multiplying by $\hbar_q^2$ (rather than dividing) establishes a strict
**duality** between hyperbolic and torus states: if hyperbolic knots
represent massive, localised "bulk" particles where $\hbar_q^2$
suppresses the volume, torus knots represent boundary/phase states
where $\hbar_q^2$ amplifies the Chern--Simons phase.

**4. Self-duality and the Frobenius pairing.**
The $\mathrm{Vol}/\hbar_q^2$ vs $\mathrm{CS} \cdot \hbar_q^2$ duality
is the Frobenius pairing of the knot with its dual in the Hecke
algebra.  For a hyperbolic knot $K$, the dual $K^*$ (mirror image)
satisfies $\mathrm{Vol}(K^*) = \mathrm{Vol}(K)$ and the Frobenius
inner product $\langle K, K^* \rangle = 1$ (via the Markov trace).
The factor $\hbar_q^2$ mediates this pairing:

$$
  \langle K, K^* \rangle_{\mathrm{Frob}}
  = \frac{\mathrm{Vol}(K)}{\hbar_q^2}
    \cdot \frac{\hbar_q^2}{\mathrm{Vol}(K^*)}
  = 1.
$$

For torus knots (which are self-dual under the descent involution),
the pairing goes through the CS functional, and $\hbar_q^2$ appears
multiplicatively because the torus knot's phase *is* the pairing.

The figure-eight knot $4_1$ is special: it is **amphicheiral**
($K = K^*$), so the self-pairing is manifestly real.  This underlies
the figure-eight BW modification factors $1 - h^2$ and $h[2]_q$
([figure-eight BW coefficients](#thm:six-term-mass-formula-complete)),
both of which are real algebraic expressions in $q$.

**5. The unknot: vacuum normalisation.**
The unknot bounds a disk; its complement has trivial geometry
($\mathrm{Vol} = 0$, $\mathrm{CS} = 0$).  Setting
$\mathrm{Geom}(\bigcirc) = 0$ ensures that unknotted loops do not
contribute spurious mass or energy to the categorical trace.
