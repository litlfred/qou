**Proof.** $C_2$ is central, so by Schur's lemma \cite{serre1977} it acts on
the irreducible
$S^\mu$ by a scalar. That scalar is the common eigenvalue of $\sum_i L_i^2$ on
the Gelfand–Tsetlin basis of $S^\mu$: each $L_i$ acts on a basis vector indexed
by a standard tableau $T$ by the content of the cell holding $i$, so
$\sum_i L_i^2$ acts by $\sum_{\square \in \mu} c(\square)^2$ — the same value
for every $T$, as centrality requires. The restricted operator is therefore
$\bigl(\sum_{\square \in \mu} c(\square)^2\bigr) \cdot \mathrm{id}_{S^\mu}$,
and the trace of a scalar multiple of the identity is that scalar times the
dimension:

$$
  \operatorname{Tr}\bigl(C_2|_{S^\mu}\bigr)
  = \Bigl(\sum_{\square \in \mu} c(\square)^2\Bigr)\dim\bigl(S^\mu\bigr).
$$

For the regular representation, decompose $\mathbb{C}[S_n]$ by
Artin–Wedderburn \cite{sagan2001}: each $S^\mu$ occurs with multiplicity
$\dim(S^\mu)$, so

$$
  \mathbb{C}[S_n] \;\cong\; \bigoplus_{\mu \vdash n}
    \bigl(S^\mu\bigr)^{\oplus \dim(S^\mu)} .
$$

Trace is additive over that decomposition, and each summand contributes the
value just computed, giving

$$
  \operatorname{Tr}(C_2)
  = \sum_{\mu \vdash n}
     \dim\bigl(S^\mu\bigr) \cdot
     \Bigl(\sum_{\square \in \mu} c(\square)^2\Bigr) \dim\bigl(S^\mu\bigr)
  = \sum_{\mu \vdash n}
     \Bigl(\sum_{\square \in \mu} c(\square)^2\Bigr) \dim\bigl(S^\mu\bigr)^2 .
$$

Dividing by $n! = \sum_\mu \dim(S^\mu)^2$ turns the right-hand side into the
Plancherel expectation $\mathbb{E}_{\mathrm{Planch}}\bigl[\sum_\square
c(\square)^2\bigr]$, which is the form Piece B consumes. $\blacksquare$
