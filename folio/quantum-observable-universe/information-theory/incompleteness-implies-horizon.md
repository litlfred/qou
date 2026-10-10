*Let $(P, e, \mathrm{eval})$ denote a Turing-complete resolution system:*

- *$P$ forms a set of programs (finite braids).*
- *$e \colon \mathbb{N} \twoheadrightarrow P$ provides a surjective enumeration (the braid group on finitely many strands is countable).*
- *$\mathrm{eval} \colon P \to (\mathbb{N} \to \mathbb{N})$ maps each program to its computed total function.*

*There exists a function $f \colon \mathbb{N} \to \mathbb{N}$ outside the image of $\mathrm{eval}$:*

$$
  \exists\, f \colon \mathbb{N} \to \mathbb{N},\;
  \forall\, p \in P,\;
  \mathrm{eval}(p) \neq f.
$$

*The computable fragment is strictly smaller than the full function space.*
