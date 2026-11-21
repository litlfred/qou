Beta decay inserts the weak-force torus knot $T_{3,5}$ at the converting quark of a nuclear Gröbner–Shirshov normal form $\mathcal{N}(Z, N)$. The braid word is $\beta_{T_{3,5}} = (\sigma_1\sigma_2)^5$. It has $10$ crossings. The operation concludes with re-reduction. The emitted electron is the word $e^- = \sigma_0\sigma_1\sigma_0$ ([electron](#def:electron-knot)), whose closure is the Hopf link; the positron is $e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$ ([positron](#def:positron-knot)). Written in the generators $\sigma_0, \sigma_1$ of the electron word, the vertex is $(\sigma_0\sigma_1)^5$, and it carries the electron word as a braid factor:

$$
  (\sigma_0\sigma_1)^5 = e^- \cdot \bigl(e^- \cdot (\sigma_0\sigma_1)^2\bigr) \quad\text{in } B_3 ,
$$

so the $10$ letters split into the $3$ of $e^-$ and a positive residue of $7$ (`QOU.BraidKnot.WeakVertexElectronFactor.weakVertex_eq_electron_mul`).

A $\beta^-$ transition inserts the $T_{3,5}$ braid at the converting $\mathfrak{d}$-quark crossing of $\mathcal{N}(Z, N)$, followed by re-reduction:

$$
  \mathcal{N}(Z, N) \cdot \beta_{T_{3,5}}
  \xrightarrow{ \text{reduce}}
  \mathcal{N}(Z + 1,  N - 1)
  \sqcup
  e^-
  \sqcup
  K_{0_1}^{\sigma}.
$$

A $\beta^+$ transition is the mirror operation. It inserts the conjugate $T_{3,5}^{\sigma}$ braid with $q \leftrightarrow q^{-1}$:

$$
  \mathcal{N}(Z, N) \cdot \beta_{T_{3,5}}^{\sigma}
  \xrightarrow{ \text{reduce}}
  \mathcal{N}(Z - 1,  N + 1)
  \sqcup
  e^+
  \sqcup
  K_{0_1}.
$$
