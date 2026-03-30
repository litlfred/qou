The torus knot $T_{2,11}$ has Seifert genus
$g(T_{2,11}) = (2-1)(11-1)/2 = 5 > 4$ and does not embed
on the Bring's surface $\Sigma_4$.  It is the **first excluded
generator** — the knot that would produce a fourth lepton
generation if it were embeddable.  Here we trace its behaviour
through every relation on the jet bundle, showing that
$T_{2,11}$ is systematically annihilated by the spectral filter
ideal $\mathcal{I}_4 \subset \mathcal{S}_q(\mathbf{C})$.

---

## 1. The spectral filter ideal

Define the **genus-$g$ spectral filter ideal**:

$$
  \mathcal{I}_g
  \;=\;
  \bigl\{
    w \in \mathcal{S}_q(\mathbf{C})
    \;\big|\;
    g(K_w) > g
  \bigr\},
$$

where $K_w$ is the knot type of the braid closure $\hat{w}$
and $g(K_w)$ is its Seifert genus.  In Hecke generators,
$\mathcal{I}_4$ is the two-sided ideal of $H^{(\infty)}(q)$
annihilated by the mass functional $\mathcal{M}$:

$$
  \mathcal{M}(w) = 0
  \qquad \forall\, w \in \mathcal{I}_4.
$$

**$T_{2,11} \in \mathcal{I}_4$** since $g(T_{2,11}) = 5 > 4$.

---

## 2. Relation-by-relation behaviour of $T_{2,11}$

### Structural relations

**(J-1) Hecke relations.**
$T_{2,11}$ is a legitimate braid word in $B_2$:
$\sigma_1^{11}$ (eleven positive crossings on two strands).
Its Hecke image is:

$$
  T_{(2,11)}
  \;=\;
  \rho_2(\sigma_1^{11})
  \;=\;
  T_1^{11}
  \;\in\; H_2(q).
$$

By iterating QU-1a ($T_1^2 = (q-q^{-1})T_1 + 1$) ten times,
$T_1^{11}$ reduces to a linear combination $\alpha(q)\,T_1 +
\beta(q)\cdot 1$ for explicit Laurent polynomials
$\alpha, \beta \in \mathbb{Z}[q^{\pm 1}]$.  **The Hecke
relation does not annihilate $T_{2,11}$** — it remains a
nonzero element of $H_2(q)$.

The Hecke algebra sees no genus bound.  The annihilation
comes from downstream relations.

**(J-2) Frobenius pairing.**
The Frobenius pairing of $T_{2,11}$ with any physical state
$T_\beta$ involves the Markov trace:

$$
  \langle T_{(2,11)},\, T_\beta \rangle_F
  \;=\;
  \mathrm{tr}_M(T_1^{11} \cdot T_\beta).
$$

This is **nonzero** in $H_2(q)$ — the Frobenius pairing
itself does not see the genus bound.  The Gram matrix entry
$G_{(2,11),\,\beta}$ is well-defined.

**(J-3) Markov trace.**
The Jones polynomial of $T_{2,11}$ is:

$$
  J_{T_{2,11}}(q)
  \;=\;
  \mathrm{tr}_M(T_1^{11})
  \;=\;
  \frac{1}{\delta}\,(\alpha(q) + \beta(q)\,\delta)
  \;\neq\; 0.
$$

**$T_{2,11}$ has a nonzero Jones polynomial.**  The Markov
trace does not kill it.

**(J-4) Translation operator.**
Acting with $L_{-1}$ on $T_{2,11}$:

$$
  L_{-1}(T_{(2,11)}^{(n)})
  \;=\;
  T_{(2,11)}^{(n+1)}
  \;\in\; H^{(n+1)}(q).
$$

The jet prolongation lifts $T_{2,11}$ to every brane level.
**No level of the brane tower kills it individually.**

**(J-5) Observability.**
$T_1^{11}$ does not commute with all generators (it lives in
$H_2(q)$, which is abelian, but in $H_n(q)$ for $n \geq 3$
it does not commute with $T_2$).  The observability axiom
is satisfied.

### Where the annihilation occurs

**(C-4b / JC-3) Euler characteristic and cohomological
embedding.**

The Descartes constraint $\chi(A) = -6$ forces genus $g = 4$.
The cohomological embedding
([cohomological embedding](#prop:cohomological-embedding))
requires that embeddable torus knots satisfy:

$$
  \mathrm{rank}\, H_1(\mathrm{Seifert}(T_{r,s}))
  \;=\;
  \frac{(r-1)(s-1)}{2}
  \;\leq\; g = 4.
$$

For $T_{2,11}$: rank $= 5 > 4$.  The Seifert surface of
$T_{2,11}$ **does not fit** in $H_1(\Sigma_4, \mathbb{Z})$.

In Hecke generators, this means: the braid word $T_1^{11}$,
when evaluated in the **representation ring restricted to
$\Sigma_4$**, projects to zero.  Concretely:

$$
  \pi_{\Sigma_4}(T_{(2,11)}) \;=\; 0,
$$

where $\pi_{\Sigma_4}\colon H_2(q) \to
H_2(q) / \mathcal{I}_4$ is the projection onto the
physical quotient.

**(C-9) Completeness of the knot basis.**
The $6 \times 5$ character matrix $M_{ij}$ has rank $5$,
and the embeddable torus knots span the representation ring.
The Jones polynomial of $T_{2,11}$, decomposed in this
basis:

$$
  J_{T_{2,11}}(q)
  \;=\;
  \sum_{\lambda \vdash 2}
  d_\lambda(q)\, \chi_\lambda(T_1^{11})
  \;=\;
  d_{(2)}(q)\, q^{11/2}
  + d_{(1,1)}(q)\, (-q^{-1})^{11/2},
$$

involves the same two irreps of $H_2(q)$ as the embeddable
$(2,n)$-knots.  The Jones polynomial **does not vanish**.
But the mass functional, which requires localizability in the
fibre $\mathcal{S}_c \cong \Sigma_4$, annihilates it:

$$
  \mathcal{M}(T_{(2,11)}) \;=\; 0
  \qquad\text{(genus $5$ does not fit in genus $4$)}.
$$

---

## 3. The ideal structure on the jet bundle

### Level-by-level filtration

At each brane level $n$, define the level-$n$ spectral ideal:

$$
  \mathcal{I}_4^{(n)}
  \;=\;
  \bigl\{
    w \in H^{(n)}(q) \;\big|\;
    g(\hat{w}) > 4
  \bigr\}.
$$

The jet embedding and descent respect the ideal:

$$
  \ell_n(\mathcal{I}_4^{(n)}) \;\subseteq\; \mathcal{I}_4^{(n+1)},
  \qquad
  \mathfrak{d}_{n+1}(\mathcal{I}_4^{(n+1)}) \;\subseteq\; \mathcal{I}_4^{(n)}.
$$

**$T_{2,11}$ stays in the ideal at every level**:

$$
  T_{(2,11)}^{(n)} \;\in\; \mathcal{I}_4^{(n)}
  \qquad \forall\, n \geq 0.
$$

No amount of jet prolongation rescues it — genus is a
topological invariant preserved by the embedding
$\ell_n$.

### Descent decomposition of $T_{2,11}$

Under the descent involution $\hat{\tau}_n$:

$$
  \hat{\tau}_n(T_{(2,11)}^{(n+1)})
  \;=\;
  \ell_n(\mathfrak{d}_{n+1}(T_{(2,11)}^{(n+1)}))
  \;=\;
  \ell_n(T_{(2,11)}^{(n)})
  \;=\;
  T_{(2,11)}^{(n+1)}.
$$

$T_{2,11}$ is **entirely descended** — it has no transient
component.  It is the same braid word $T_1^{11}$ at every
level, simply embedded.  This means:

- No new physics is created by jet-prolonging $T_{2,11}$
- Its transient projection is zero:
  $(1 - \hat{\tau}_n)(T_{(2,11)}^{(n+1)}) = 0$
- It contributes nothing to the Yekutieli obstruction $\kappa_n$

### Harmonic analysis

The $q$-Laplacian on $T_{2,11}$:

$$
  \Delta_{q,n}\, T_{(2,11)}^{(n)}
  \;\neq\; 0
  \qquad\text{(generically)}.
$$

$T_{2,11}$ is **not harmonic** — it does not belong to
$\ker \Delta_{q,n}$ (the particle Hilbert space).  The
harmonic projection

$$
  \Pi_{\mathrm{harm}} T_{(2,11)}^{(n)} \;=\; 0
$$

annihilates it because the harmonic states are precisely the
embeddable knots with $g \leq 4$.

### Hodge duality

The Poincaré dual of $T_{2,11}$ in $H^*(\Sigma_4)$:

$$
  \star\, [T_{2,11}] \;=\; 0
  \qquad\text{in } H^*(\Sigma_4),
$$

because $T_{2,11}$ does not define a class in $H^1(\Sigma_4)$
(its Seifert surface exceeds the available rank).  It has no
Hodge partner.

### Skein interaction with physical states

When $T_{2,11}$ appears as an intermediate term in a Skein
resolution of physical knots:

$$
  q\,[L_+] - q^{-1}[L_-]
  \;=\;
  (q^{1/2} - q^{-1/2})\,[L_0],
$$

the smoothing $L_0$ may produce a knot of genus $5$.  But the
mass functional projects this away:

$$
  \mathcal{M}\!\bigl(
    q\,[L_+] - q^{-1}[L_-]
  \bigr)
  \;=\;
  (q^{1/2} - q^{-1/2})\,
  \underbrace{\mathcal{M}([L_0])}_{= 0\text{ if }g(L_0) > 4}.
$$

The physical Skein relation on $\Sigma_4$ is:

$$
  q\,\mathcal{M}[L_+] - q^{-1}\mathcal{M}[L_-]
  \;=\; 0
  \qquad\text{when } g(L_0) > 4.
$$

This is a **modified Skein relation**: genus-$5$ intermediate
states impose the constraint
$q\,\mathcal{M}[L_+] = q^{-1}\mathcal{M}[L_-]$, fusing the
two crossing channels.

---

## 4. Knot operator product

In the spectral decomposition
([spectral decomposition](#cor:spectral-decomposition-qvalue)),
non-embeddable torus knots contribute $F = 1$ (the
multiplicative identity) to the knot operator product:

$$
  F(T_{2,11},\, N) \;=\; 1
  \qquad\forall\, N.
$$

**$T_{2,11}$ acts as the identity on every nuclear shell.**
It cannot create, destroy, or modify any physical state.
In the transfer matrix language:

$$
  \mathcal{T}_{T_{2,11}}(q) \;=\; \mathbf{I}_{2 \times 2}.
$$

The $(2,11)$ torus knot defines a **null force operator** —
an interaction channel that has been closed by the genus
bound.

---

## 5. Summary: the fate of $T_{2,11}$

| Relation | $T_{2,11}$ status | Why |
|----------|-------------------|-----|
| Hecke (J-1) | **Survives** | Valid braid word $T_1^{11} \in H_2(q)$ |
| Frobenius (J-2) | **Survives** | Nonzero Frobenius pairing |
| Markov trace (J-3) | **Survives** | $J_{T_{2,11}}(q) \neq 0$ |
| Translation (J-4) | **Survives** | Lifts to all brane levels |
| Observability (J-5) | **Survives** | Not in centre of $H_n$ |
| Volume (J-6) | **Survives** | Not killed by $\mathrm{Alt}_2$ |
| Euler / Descartes (JC-3) | **Killed** | $g = 5 > 4 = g(\Sigma_4)$ |
| Cohom.\ embedding (C-9) | **Killed** | $\pi_{\Sigma_4}(T_{(2,11)}) = 0$ |
| Mass functional | **Killed** | $\mathcal{M}(T_{(2,11)}) = 0$ |
| Harmonic projection | **Killed** | $\Pi_{\mathrm{harm}} T_{(2,11)} = 0$ |
| Hodge dual | **Killed** | $\star[T_{2,11}] = 0$ in $H^*(\Sigma_4)$ |
| Descent | **Fully descended** | No transient component |
| Knot operator | **Identity** | $F(T_{2,11}, N) = 1$ |

$T_{2,11}$ is an algebraically valid element of the Hecke
algebra — it satisfies all the structural relations (Hecke,
Yang--Baxter, Frobenius, Markov).  It has a nonzero Jones
polynomial and nonzero Frobenius pairings.  But the
**cohomological constraints** — specifically the Descartes
condition $\chi = -6$ and the completeness of the knot basis
on $\Sigma_4$ — place it in the spectral filter ideal
$\mathcal{I}_4$.  The mass functional, harmonic projection,
and Hodge duality all annihilate it.  On the jet bundle, it
is entirely descended (no new physics at any level) and acts
as the identity operator on all physical states.

$T_{2,11}$ is the **ghost of the fourth generation**: an
algebraically consistent but physically null knot, killed
not by the algebra but by the topology of Bring's surface.
