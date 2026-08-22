# **QOU MotivicGaloisCharacter instance** via Habiro evaluation

**Conjecture.** The QOU brane-tower substrate carries an instance of [`def:motivic-galois-character`](#def:motivic-galois-character) whose local Frobenius is the Habiro evaluation map:

$$
  \mathrm{Frob}_p \;=\; f(u) \big|_{u = \zeta_{2p}}
  \;\in\; \mathbb{Z}[\zeta_{2p}].
$$

Here $f(u) = \sum_{m \geq 0} a_m(u) (u; u)_m$ represents the Habiro cyclotomic expansion of the atomic Markov trace $\mathrm{tr}_M(T_w, q)$ and $u = q^{1/2}$. The cyclotomic Pochhammer $(u; u)_m$ vanishes for $m \geq 2p$. This forces the sum to terminate after a finite number of terms.

The finite-place compatibility checks, the downstream consumers, and
cross-prime coherence are recorded in
[the follow-on remark](#rem:qou-motivic-galois-instance-verification);
the per-cell $\mathrm{Frob}_p$ data appears in
[the accompanying example](#ex:qou-motivic-galois-instance-per-cell).

**Why this is stated as a conjecture.** The evaluation formula above is
explicit and total in $p$. What is not established is that it lands in
$\mathbb{Z}[\zeta_{2p}]$ at every prime and assembles into an instance.
The probe checks $9$ primes ($2$–$23$) against $5$ atoms and finds no
disagreement — but at all nine the Pochhammer truncation fires inside the
available data, so full-trace compatibility is *unreached*, not confirmed.
Compatible where checked; open beyond that.

**Lean status.** None. The co-located `.lean` file — which contained a
bare `axiom` laundering the perpetual obstruction into the
`MotivicGaloisCharacter` class — was deleted on 2026-08-12, and the
`lean.ref` it left behind
(`QOU.LiftingDescent.QOUInstance.qouMotivicGaloisChar`) named a module
that has never existed; it has now been dropped rather than repointed.

Writing an instance would not currently mean anything: since 2026-08-12
`MotivicGaloisCharacter` carries the single data field
`frobenius_at : Nat.Primes → Mhat` with no propositional obligation, so
any total function inhabits it. The formalisation this block actually
owes is the Habiro cyclotomic expansion $f(u)$ and its evaluation at
roots of unity. Nothing downstream waits on it: the motivic perpetual
obstruction takes `[MotivicGaloisCharacter …]` as an explicit
hypothesis, and is proved
sorry-free in
`lean/QOU/LiftingDescent/MotivicPerpetualObstructionFromTrace.lean`
(Route A: prime-ideal-collapse, $C = a_0(-1) + 2a_1(-1)$).
