The mass--energy equivalence $E = mc_q^2$ and the derived speed
of light $c_q = 1/(q-1)$ place the QOU in the context of
information-theoretic approaches to fundamental physics.  This
remark summarises the connections and identifies the QOU's specific
contributions.

**1. The light cone is the Lieb--Robinson cone.**
The light cone of an affine chart
([light cone](#rem:light-cone-affine)) is the boundary at
$|Z| = c_q$ in the contact affine coordinate
([contact affine chart](#def:contact-affine-chart)): the locus where
horizontal spatial diffusion exactly matches vertical Reeb advance.
This is not a geometric postulate (as in special relativity) but
a *consequence* of the $q$-connection decomposition
$A_q = q^{-1}A + \hbar_q\iota_\xi A\varTheta$ --- the spatial
and temporal coupling weights determine the causal boundary.
Outside the cone, the Lieb--Robinson bound
([speed of light](#def:information-speed-of-light)) gives
exponential suppression of correlations.

The causal structure of the QOU is therefore *information-theoretic*:
causality follows from the ratio of spatial to temporal information
flow in the $q$-connection, not from an axiom about geometry.  This
realises Jacobson's programme [jacobson1995] of deriving spacetime
geometry from information, with the $q$-connection decomposition
playing the role of Jacobson's local Rindler horizons.

**2. The speed of light varies with $q$.**
Unlike standard physics (where $c$ is a postulated constant) or
many information-theoretic approaches (where $c$ emerges but is
fixed), the QOU speed of light $c_q = 1/(q-1)$ varies with the
substrate parameter.  At the Big Bang ($q \to \infty$),
$c \to 0$: fibres are informationally isolated, no spatial
signalling is possible.  As the universe evolves toward the
classical limit ($q \to 1$), $c \to \infty$: spatial coupling
dominates and the Newtonian regime of instantaneous propagation
emerges.  At our local $q = q_0$, $c \approx 9.12$ in
Reeb units --- a large but finite ratio of spatial to temporal
information flow.

**3. The Margolus--Levitin bound and $c_q$.**
The Margolus--Levitin theorem [margolus1998] bounds the operation
rate of a system with energy $E$: at most $2E/\pi\hbar$ ops/sec.
In the QOU, the crossing energy $E = mc_q^2 = m/(q-1)^2$ and the
operation count is $n_R(q) = 1/\hbar_q$.  The bound becomes:

$$
  n_R(q)  \leq  \frac{2m \cdot c_q^2}{\pi\hbar_q}
  =  \frac{2m}{\pi\hbar_q(q-1)^2}.
$$

The Reeb dynamics saturates this bound (up to the factor $2/\pi$):
each Planck cell computes at the maximum rate allowed by its
mass-energy content.

**4. Bremermann's limit and information bandwidth.**
Bremermann's limit states that a system of mass $m$ can process at
most $mc^2/h$ bits per second [lloyd2000].  With $c_q = 1/(q-1)$
and the operational entropy $\eta_q$
([operational entropy](#def:operational-entropy)):

$$
  \mathfrak{B}(q)
  =  c_q \cdot n_R(q) \cdot \eta_q
  =  \frac{q\eta_q}{(q-1)^2}
  \quad \text{($q$-bits per Planck time)}.
$$

At $q = q_0$: $\mathcal{B} \approx q\eta_q/(q-1)^2 \approx 82$ $q$-bits per Planck time.

**5. Pawlowski's information causality.**
Information causality [pawlowski2009] states that if Alice sends
$m$ classical bits to Bob, Bob's total accessible information about
Alice's data is at most $m$ bits.  The $m = 0$ case is the
no-signaling condition.  In the QOU, information causality is
automatic: the Lieb--Robinson bound gives exponential decay outside
the $|Z| = c_q$ cone, and the $m = 0$ case follows from the
locality of $\nabla_q$ (the comultiplication acts on adjacent fibres
only).

**6. The Bekenstein bound and fibre entropy.**
The Bekenstein bound [bekenstein1981] limits the entropy of a
region of radius $R$ and energy $E$: $S \leq 2\pi RE / \hbar c$.
With $c = c_q$ and $E = mc_q^2$, the QOU fibre entropy is
bounded by $\eta_q$ per operation:

$$
  S_{\mathrm{fibre}}  \leq  \eta_q
  =  \frac{2q - 1}{q^3}
  \quad \text{($q$-bits per operation)}.
$$

**7. Summary: QOU position in the landscape.**

| Quantity | Standard physics | Information-theoretic programme | QOU |
|----------|-----------------|-------------------------------|-----|
| $c$ | Postulated constant | Emergent (various) | $c_q = 1/(q-1)$: spatial/temporal coupling ratio |
| $E = mc^2$ | Lorentz invariance | Lloyd: computational bound | $E = m/(q-1)^2$: ribbon trace $\times$ info speed${}^2$ |
| Causal structure | Light-cone axiom | Jacobson: entropy $\Rightarrow$ Einstein eqs | $\lvert Z\rvert = c_q$ cone from $q$-connection |
| Bekenstein bound | Semiclassical gravity | Holographic principle | Fibre entropy $\leq \eta_q$ per operation |
| Margolus--Levitin | Energy--time uncertainty | Quantum speed limit | Saturated: $n_R(q) \sim mc_q^2/\hbar_q$ |
