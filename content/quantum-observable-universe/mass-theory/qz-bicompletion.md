**Definition (proposed; conjectural utility).**
*The **$(q, z)$-bicompletion** is the inverse limit*

$$
  \widehat{\mathbb{Z}[q^{\pm 1}, z]}_{q,z}
  \;:=\;
  \varprojlim_{(m, n)} \;
  \mathbb{Z}[q^{\pm 1}, z] \big/ \bigl(I_{m,n}\bigr),
$$

*indexed by pairs $(m, n) \in \mathbb{N}^2$ with $(m, n) \leq (m', n')$
iff $m \leq m'$ and $n \leq n'$, where the bigraded ideal is*

$$
  I_{m,n}
  \;:=\;
  \bigl((q;q)_m \;\cdot\; P_n(q, z)\bigr)
  \;=\;
  \Bigl(\prod_{k=1}^{m}(1 - q^k) \;\cdot\; \prod_{k=1}^{n}(1 - q^{-k} z)\Bigr).
$$

*The transition maps $\mathbb{Z}[q^{\pm 1}, z]/I_{m',n'} \twoheadrightarrow \mathbb{Z}[q^{\pm 1}, z]/I_{m,n}$
for $(m, n) \leq (m', n')$ are well-defined because $I_{m',n'} \subseteq I_{m,n}$.*

The bicompletion sits at the apex of the diagram of cyclotomic
completions, jointly carrying the $q$-only ([Habiro ring](#def:habiro-ring))
and $z$-only ([$z$-Habiro ring](#def:z-habiro-ring)) cyclotomic structures.

**Archimedean specialisation (§7c).** This block is stated over the real field $\mathbb{R}$ — the archimedean side of the substrate wall: its constructs are real-valued (physical observables, real-analytic bounds, or numerical evaluations at the substrate parameter $q_0$) rather than generic-ring $q$-deformation data. The generic categorical / $q$-deformation machinery it draws on is stated over an abstract coefficient ring in its own blocks; only the archimedean realisation is specialised here.
