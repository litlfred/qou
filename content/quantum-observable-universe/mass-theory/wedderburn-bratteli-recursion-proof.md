By [Jones–Markov trace](#thm:jones-markov-trace), the Markov property
$\mathrm{tr}_M(x \cdot T_n^{\pm 1}) = z^{\pm 1} \cdot \mathrm{tr}_M(x)$
extends $\mathrm{tr}_M$ uniquely from $H_n$ to $H_{n+1}$.  In the
Wedderburn block decomposition, this fixes
$\{y_\lambda^{(n+1)}\}_{\lambda \vdash n+1}$ in terms of
$\{y_\mu^{(n)}\}_{\mu \vdash n}$ via the central-character expansion
([linear-system characterisation](#prop:alpha-k-derivation-procedure)).

The Bratteli diagram of the Hecke tower $H_1 \subset H_2 \subset \cdots$
is **multiplicity-free at generic $q$** by Hoefsmit's seminormal-form
construction ([Hoefsmit](#prop:hoefsmit-seminormal-form)): each edge
$\mu \nearrow \lambda$ corresponds to a unique addable cell of $\mu$
to form $\lambda$.  The branching $V_\lambda \big\downarrow_{H_n} =
\bigoplus_{\mu \nearrow \lambda} V_\mu$ together with the Markov
condition therefore yields a **finite** linear relation between
$y_\lambda^{(n+1)}$ and the $y_\mu^{(n)}$ for $\mu \nearrow \lambda$.

The coefficients are $z$ times a $q$-rational function of the added
cell's $q$-content and of the hook structure of $\lambda$ — concretely
the Hoefsmit eigenvalue of $T_n$ on the per-edge orthogonal idempotent
$e_{\mu \to \lambda}$.  $\square$
