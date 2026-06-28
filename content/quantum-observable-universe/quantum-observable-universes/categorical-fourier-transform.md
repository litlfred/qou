The Laplace transform ([categorical Laplace transform](#def\:categorical-laplace))
pairs against the *real* exponential grouplike $\exp_q(-s\cdot)$.  Its
companion pairs against the *unitary* grouplike $\exp_q(i\xi\cdot)$ — a
second grouplike of the same Hopf algebra $\mathcal{H}_q$, distinguished only by
the sign of the spectral parameter.

**Categorical Fourier transform.**  The **categorical Fourier transform**
is the :refterm[monoidal functor]{#monoidal-functor}

$$
  \mathcal{F}\colon \bigl(\mathrm{End}_{\mathbf{C}}(A), \ast_q\bigr)
  \;\longrightarrow\;
  \bigl(\mathrm{End}_{\mathbf{C}}(A), \cdot\bigr),
  \qquad
  \mathcal{F}[f](\xi) \;=\; \mathrm{tr}_M\bigl(\exp_q(i\xi\cdot)  \cdot  f\bigr),
$$

where $\xi$ ranges over the categorical spectrum
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, A^\vee)$ — the Pontryagin dual
of the Reeb-translation object.
