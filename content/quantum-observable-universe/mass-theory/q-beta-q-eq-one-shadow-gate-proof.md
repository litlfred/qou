## Proof sketch

The $c_2$ anchor is the structural $N = 2$ result: the operator-valued $N = 2$ correction $(1 - b^2 \cdot \hbar_q^4)$ rewrites as $(1 - u^2)$ in CommRing R, so the ladder coefficient at $u^2$ is exactly $-1$ — independent of the underlying $F(q)$, as long as $F$ generates this $N=2$ factor.

The $c_3$ anchor is conjectural at the value level (registry §3 records it as `EMPIRICAL — near-match`, refuted as a real-q fibre element by C1–C2) but **anchored as an integer shadow at q = 1**: it equals the Hopf-link Jones polynomial evaluated at $q = 1$, which is $-2$ in our normalization. A candidate whose $q \to 1$ limit gives anything other than $-2$ is structurally inconsistent with the registry anchor and is therefore REFUTED at the formalize-first level (before any numerical anchor sweep at $q_0$).

**The gate (rejection lemma):** if a candidate's $q \to 1$ Taylor coefficient at $u^k$ disagrees with the canonical integer shadow $a_k \in \{-1, -2\}$ for $k \in \{2, 3\}$, the candidate fails the gate. $\blacksquare$
