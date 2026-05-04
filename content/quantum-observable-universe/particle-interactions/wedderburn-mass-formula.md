For a neutral atom $(Z, N)$ with $n_{\mathrm{gen}}$ Hecke–NF generators, the
three-invariant mass formula decomposes the total atomic mass as

$$
  M(Z, N) \;=\; Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e
  \;+\; \alpha \sum_{i=1}^{n_{\mathrm{gen}}} \ln \bigl|\hat{V}_i^{\mathrm{full}}\bigr|,
$$

where the \emph{full traced volume per generator} is the Wedderburn-weighted sum

$$
  \hat{V}_i^{\mathrm{full}}
  \;=\;
  w_{\mathrm{sym}}(q)\,\lambda_i^{\mathrm{sym}}
  + w_{\mathrm{std}}(q)\,\hat{V}_i^{\mathrm{std}}
  + w_{\mathrm{alt}}(q)\,\lambda_i^{\mathrm{alt}},
$$

and the Wedderburn–Markov weights at the baryon level $n = 3$ are

$$
  w_{\mathrm{sym}} = w_{\mathrm{alt}} = \frac{1}{[3]_q!},
  \qquad
  w_{\mathrm{std}} = \frac{[2]_q^2}{[3]_q!},
  \qquad
  [3]_q! = (1+q+q^2)(1+q).
$$

The binding scale is $\alpha = m_e \cdot 8G$ where $G \approx 0.9159$ is Catalan's constant.

**Proof.**
The mass split $M(Z,N) = Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e + \mathrm{bindingTerm}(Z,N,q)$
is a structural identity: the total mass is defined as the sum of nucleon and
electron rest masses plus the categorical binding term.  The identity holds by
definition (`wedderburnMass_split` — `rfl`).
The closed-form value of $w_{\mathrm{sym}} + w_{\mathrm{std}} + w_{\mathrm{alt}}$
follows by `ring` from the $q$-integer arithmetic.
See `QOU.Interactions.WedderburnMassFormula` for the Lean verification.
