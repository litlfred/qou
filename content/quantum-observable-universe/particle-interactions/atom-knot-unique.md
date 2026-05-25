**Proposition.**
*The atom-knot of type $(Z, N)$ is unique up to **Markov
equivalence** of braid representatives:*

*If $\beta_1, \beta_2$ are two braids in $B_{n(K)}$ both realising
the NF block decomposition $T_w = T_{w_{q^Z}} \cdot T_{w_{\bar q^N}}
\cdot T_{w_{\mathrm{inter}}}$ ([atom-knot](#def:atom-knot)), then
their Markov closures are isotopic in $S^3$:*

$$
  \hat\beta_1 \;\cong_{\mathrm{isotopy}}\; \hat\beta_2.
$$

*Proof.*
*The NF $T_w$ is unique by the Diamond Lemma
([hecke normal form](#def:hecke-normal-form)).  Two braids
realising the same NF differ only by a sequence of:*

- *Reidemeister II moves (Hecke relation $\sigma_i^2 \sim
  H_A \sigma_i + 1$ rewritten in NF);*
- *Reidemeister III moves (Yang–Baxter
  $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i
  \sigma_{i+1}$);*
- *Far commutations
  ($\sigma_i \sigma_j = \sigma_j \sigma_i$ for $|i-j| \geq 2$).*

*Each is a categorical Markov move
([Jones–Markov trace](#thm:jones-markov-trace)), so the closures
are isotopic.  $\square$*

**Scope.**
*Uniqueness is up to **isotopy**, not up to NF strict equality.
Two non-isotopic atom-knots with $(Z_1, N_1) = (Z_2, N_2)$ are
**isotopes** of each other ([isotope-knot](#def:isotope-knot)) only
if they share the proton-quark block $w_{q^Z}$.  Different $w_{q^Z}$
realisations (e.g. interchanging two protons via a non-trivial
permutation) yield different isotopy classes — these are
**distinct atom-knots** at the same $(Z, N)$, corresponding to
different physical isomers.*
