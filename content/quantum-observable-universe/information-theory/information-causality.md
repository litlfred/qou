We place the quantum observable universe (QOU) within information-theoretic physics. The mass--energy equivalence $E = mc_q^2$ and the derived speed of light $c_q = 1/(q-1)$ connect the QOU to established information bounds. We detail these connections below.

**1. The light cone is the Lieb--Robinson cone.**
The causal boundary arises from the $q$-connection decomposition $A_q = q^{-1}A + \hbar_q\iota_\xi A\varTheta$. The boundary at $|Z| = c_q$ in the contact affine coordinate ([contact affine chart](#def:contact-affine-chart)) is the locus where horizontal spatial diffusion matches vertical Reeb advance. Outside this cone, the Lieb--Robinson bound ([speed of light](#def:information-speed-of-light)) enforces exponential suppression of correlations. Causality follows directly from the ratio of spatial to temporal information flow in the $q$-connection. This realises Jacobson's programme [jacobson1995], deriving spacetime geometry from information flow.

**2. The speed of light varies with $q$.**
The speed of light $c_q = 1/(q-1)$ depends on the substrate parameter. At the Big Bang ($q \to \infty$), $c \to 0$: fibres isolate, preventing spatial signalling. As the universe classicalises ($q \to 1$), $c \to \infty$: spatial coupling dominates, yielding the Newtonian regime. At the present epoch $q = q_0$, $c \approx 9.12$ in Reeb units.

**3. The Margolus--Levitin bound and $c_q$.**
The Margolus--Levitin theorem [margolus1998] bounds the operation rate of a system with energy $E$ by $2E/\pi\hbar$ ops/sec. We have the crossing energy $E = mc_q^2 = m/(q-1)^2$ and the operation count $n_R(q) = 1/\hbar_q$. The bound is:

$$
  n_R(q)  \leq  \frac{2m \cdot c_q^2}{\pi\hbar_q}
  =  \frac{2m}{\pi\hbar_q(q-1)^2}.
$$

The Reeb dynamics saturates this bound up to the factor $2/\pi$. Each Planck cell computes at the maximum rate allowed by its mass--energy content.

**4. Bremermann's limit and information bandwidth.**
Bremermann's limit [lloyd2000] states a system of mass $m$ processes at most $mc^2/h$ bits per second. With $c_q = 1/(q-1)$ and the operational entropy $\eta_q$ ([operational entropy](#def:operational-entropy)), we find the bandwidth:

$$
  \mathfrak{B}(q)
  =  c_q \cdot n_R(q) \cdot \eta_q
  =  \frac{q\eta_q}{(q-1)^2}
  \quad \text{($q$-bits per Planck time)}.
$$

At $q = q_0$, $\mathcal{B} \approx q\eta_q/(q-1)^2 \approx 82$ $q$-bits per Planck time.

**5. Pawlowski's information causality.**
Information causality [pawlowski2009] restricts the accessible information Bob gains from Alice to the classical bits transmitted. In the QOU, the Lieb--Robinson bound ensures exponential decay outside the $|Z| = c_q$ cone. The no-signaling condition holds because the comultiplication $\nabla_q$ acts only on adjacent fibres.

**6. The Bekenstein bound and fibre entropy.**
The Bekenstein bound [bekenstein1981] limits the entropy of a region of radius $R$ and energy $E$ to $S \leq 2\pi RE / \hbar c$. Using $c = c_q$ and $E = mc_q^2$, we bound the QOU fibre entropy by $\eta_q$ per operation:

$$
  S_{\mathrm{fibre}}  \leq  \eta_q
  =  \frac{2q - 1}{q^3}
  \quad \text{($q$-bits per operation)}.
$$

**7. Summary.**

| Quantity | Standard physics | Information-theoretic programme | QOU |
|----------|-----------------|-------------------------------|-----|
| $c$ | Postulated constant | Emergent (various) | $c_q = 1/(q-1)$: spatial/temporal coupling ratio |
| $E = mc^2$ | Lorentz invariance | Lloyd: computational bound | $E = m/(q-1)^2$: ribbon trace $\times$ info speed${}^2$ |
| Causal structure | Light-cone axiom | Jacobson: entropy $\Rightarrow$ Einstein eqs | $\lvert Z\rvert = c_q$ cone from $q$-connection |
| Bekenstein bound | Semiclassical gravity | Holographic principle | Fibre entropy $\leq \eta_q$ per operation |
| Margolus--Levitin | Energy--time uncertainty | Quantum speed limit | Saturated: $n_R(q) \sim mc_q^2/\hbar_q$ |
