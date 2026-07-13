<!-- FILE_START: markov-axioms-primitive.md -->
The Markov trace $\tau_M$ on the Iwahori-Hecke algebra $H_n(R, q)$ is the unique linear functional satisfying:

1. **Normalisation:** $\tau_M(1) = 1$.
2. **Cyclicity:** $\tau_M(xy) = \tau_M(yx)$ for all $x, y$.
3. **Stabilisation by $\sigma_n$:** $\tau_M(x \sigma_n) = z \cdot \tau_M(x)$, where $z = 1/(\sqrt q + 1/\sqrt q)$ is the Markov-Jones parameter.
4. **Stabilisation by $\sigma_n^{-1}$:** $\tau_M(x \sigma_n^{-1}) = z \cdot \tau_M(x)$.

These axioms force $\tau_M$ to be the non-degenerate Jones-Markov trace. Iterating the stabilisation axiom implies that the joint Markov trace of two braids acting on disjoint strand sets factorises:
$$
  \tau_M(K_1 \sqcup K_2) \;=\; \tau_M(K_1) \cdot \tau_M(K_2) \cdot z^k,
$$
where $k$ is the number of disjoint strands stabilised. This derives the inter-knot decoupling theorem from primitive Markov axioms.
<!-- FILE_END: markov-axioms-primitive.md -->

<!-- FILE_START: markov-trace-inductive-limit.md -->
The Markov trace extends to a single operator on the inductive limit of braid groups $\mathbf{B}_\infty = \bigcup_n \mathbf{B}_n$. The restrictions $\tau_M\big|_{\mathbf{B}_n}$ yield the per-$n$ trace. The inclusion $\iota_n : \mathbf{B}_n \hookrightarrow \mathbf{B}_{n+1}$ adjoins a non-interacting strand on the right. 

In Lean, the `MarkovTraceInductiveLimit` class provides a single global hypothesis. This bridge automatically derives every per-$n$ trace, eliminating repetitive per-$n$ axiomatization. This formalization resides on the archimedean side of the substrate wall, substituting the substrate parameter $q_0$ and verifying real-analytic bounds, while the generic categorical identities remain valid over an abstract coefficient ring.
<!-- FILE_END: markov-trace-inductive-limit.md -->

<!-- FILE_START: trm-hopf-sigma1-sq-closed-form.md -->
The canonical Markov trace of $\sigma_1^2$ has the closed form:
$$
\boxed{\quad
  \mathrm{tr}_M(\sigma_1^2)
  \;=\; \frac{q^{5/2} - q^{1/2} + q^2 + q}{q^2 + q}
  \;=\; 1 + \frac{q - 1}{q^{1/2}}.
\quad}
$$
This value is independent of $n$, and its closure is the positive Hopf link $L_+^{\mathrm{Hopf}}$.

The $\mathfrak{Q}_\beta$ factorisation takes the form:
$$
  \mathfrak{Q}_\beta \;=\; Q_A \cdot \cos\bigl(\alpha - b\hbar_q^2/2\bigr)
              \cdot \prod_{n \geq 2} (1 + c_n \hbar_q^{2n})
$$
with coefficients $c_2 = b^2$, $c_3 = -2 b^3$, $c_4 = b^2 + 1/2$. The $\varepsilon^{2n}$ coefficients of $\mathrm{tr}_M(\sigma_1^2) - 1$ do not match these $c_n$ values. Therefore, the factors $1 + c_n \hbar_q^{2n}$ arise from a separate categorical decomposition of $\mathfrak{Q}_\beta$ rather than from the bare Markov trace of $\sigma_1^2$.

**Mathematical Novelty:** This closed form is the simplest nontrivial derived Markov-trace in the framework. The explicit mismatch between the bare-Markov coefficients and the $\mathfrak{Q}_\beta$ precision-ladder coefficients proves that the latter represents a distinct categorical decomposition.
<!-- FILE_END: trm-hopf-sigma1-sq-closed-form.md -->

<!-- FILE_START: hecke-algebra-from-braiding.md -->
The Iwahori--Hecke algebra where normal-form computations occur is not an algebra with a free parameter. Instead, it is the quotient of the braid-group algebra by the minimal polynomial of the categorical braiding. 

The endomorphism $T = \tau(c_{V,V})$ satisfies the Hecke relation:
$$
  (T - q)(T + q^{-1}) =  0,
$$
where $q$ is the braiding eigenvalue. Consequently, the Iwahori--Hecke algebra on $n$ strands is:
$$
  H_n(R, q) =  k[B_n] \big/
  \bigl\langle (\sigma_i - q)(\sigma_i + q^{-1})  \big| 
  i = 1, \ldots, n{-}1 \bigr\rangle.
$$
The parameter $q$ is a fixed categorical datum determined by the braiding. The per-crossing weights $q$ and $-q^{-1}$ are exactly the eigenvalues of $T$ on $S^{2} V \oplus \Lambda^{2} V$, forced by the categorical volume constraint.
<!-- FILE_END: hecke-algebra-from-braiding.md -->

<!-- FILE_START: f-bor-borromean-observable.md -->
The Borromean categorical observable is the natural Wedderburn-content-shifted combination:
$$
  F_{\mathrm{Bor}}(q) \;:=\;
    \frac{\bigl|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)\bigr| \cdot [3]_q!}{q^3}.
$$
Using the q-Schur Markov-weight identification $y_{(3)}(q) := q^3 / [3]_q!$, this becomes:
$$
  F_{\mathrm{Bor}}(q) \;=\; \frac{|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)|}{y_{(3)}(q)}.
$$
This expresses $F_{\mathrm{Bor}}$ as the Markov trace of the Borromean braid normalised by the content-shifted Markov weight of the trivial partition $(3)$. 

Every coefficient of $F_{\mathrm{Bor}}$ in the variable $h = q - q^{-1}$ is an exact rational number:
$$
  F_{\mathrm{Bor}}(h)
  \;=\; 6 \;-\; 9h \;+\; \tfrac{19}{2}h^2 \;-\; \tfrac{57}{8}h^3
        \;-\; \tfrac{1}{2}h^4 \;+\; \tfrac{649}{128}h^5 \;-\; 7h^6 \;+\; \cdots
$$
The observable attaches two structural integers: $2$ (the classical dimension of the standard irrep of $S_3$) and $12$ (the order of $S_3$ scaled by this dimension). These integers carry no archimedean information and are available over any base ring.
<!-- FILE_END: f-bor-borromean-observable.md -->

<!-- FILE_START: hecke-normal-form.md -->
The Hecke normal form of an element $h \in H_n(R, q)$ is the unique representative obtained by iterated application of three rewriting rules:
1. Hecke relation: $\sigma_i^2 \to (q - q^{-1})\sigma_i + \mathbf{1}$.
2. Far commutativity: $\sigma_i \sigma_j \to \sigma_j \sigma_i$ for $|i - j| \geq 2$.
3. Yang--Baxter: $\sigma_i \sigma_{i+1} \sigma_i \to \sigma_{i+1} \sigma_i \sigma_{i+1}$ (in the shortlex-decreasing direction).

This reduction is confluent, making the normal form independent of rule order. The resulting basis elements correspond bijectively to the symmetric group $S_n$. Computationally, this may be evaluated by directed Kashiwara crystal traversal rather than S-polynomial overlap analysis.
<!-- FILE_END: hecke-normal-form.md -->

<!-- FILE_START: dark-vision-strand-bandwidth.md -->
Photons entering the eye are unknotted strands. Reflection from environmental matter braids these photon strands with the environment's state, producing a braid word in $H_n(R, q)$. Observation applies the functor $\tau$ to this state, yielding a classical scalar.

The dimension of the accessible phase space is fixed by the strand count $n$. In low light, $n$ is small, providing insufficient topological complexity to encode the scene. We cannot see in the dark due to a structural truncation of the observation channel, not a failure of the retina.
<!-- FILE_END: dark-vision-strand-bandwidth.md -->

<!-- FILE_START: markov-moves-brane-tower.md -->
The two Markov moves that ensure link invariance correspond to the horizontal and vertical directions of the brane tower's cosimplicial structure. 

Conjugation $\beta \mapsto \gamma\beta\gamma^{-1}$ is the horizontal direction. It represents gauge transformations within a single fibre at a fixed level $n$. The trace property $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$ guarantees invariance under these moves.

Stabilisation $\beta \mapsto \beta \cdot \sigma_n^{\pm 1}$ is the vertical direction. It represents movement between levels of the tower via jet prolongation $A_n \hookrightarrow A_{n+1}$. The Markov property $\mathrm{tr}_M(x \sigma_n^{\pm 1}) = z^{\pm 1}\mathrm{tr}_M(x)$ correctly scales the trace across these inclusions.

Thus, the Iwahori--Hecke algebra tower shadows the brane tower. Markov's theorem dictates that horizontal and vertical moves exhaust the gauge freedom. The direct limit algebra $\mathcal{A}_\infty = \varinjlim\mathrm{End}_{\mathbf{C}}(A_n)$ provides the receptacle where the Markov trace stabilises to a well-defined link invariant.
<!-- FILE_END: markov-moves-brane-tower.md -->

<!-- FILE_START: markov-trace-ambient-s3.md -->
The ambient three-sphere $S^3$ enters strictly through the closure construction via two classical theorems.

Alexander's theorem states that every oriented link in $S^3$ is the closure of some braid. Therefore, the disjoint union of braid groups exhausts all link types in the three-sphere.

Markov's theorem establishes that two braids have isotopic closures in $S^3$ if and only if they are related by a sequence of conjugation and stabilisation moves.

The Markov trace is invariant under both moves. Because closure surjects onto the links of $S^3$ and its fibres are exactly the Markov-move orbits, the Markov trace descends to a well-defined invariant of links in $S^3$. The ambient $S^3$ is thus constructed categorically as the target of the Alexander--Markov correspondence, rather than posited geometrically upstream.

This ambient $S^3$ base manifold must not be confused with the group manifold $\mathrm{SU}(2) \cong S^3$. The base manifold is fixed by the closure construction, while the gauge group enters only through the representation category.
<!-- FILE_END: markov-trace-ambient-s3.md -->

