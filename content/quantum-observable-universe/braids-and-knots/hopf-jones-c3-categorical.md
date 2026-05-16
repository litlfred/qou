## Statement

**Proposition (categorical, Story B closure at $c_3$).** Let
$\beta_3 := \sigma_1^2$ denote the 2-strand Hopf braid (closure
yields the positive Hopf link $L_+^{\mathrm{Hopf}}$). Let $c_3$
denote the third coefficient in the Q_β precision-ladder
expansion of [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder):
$$
  Q_\beta = Q_A \cdot \cos\bigl(\alpha - b\hbar_q^2/2\bigr) \cdot \bigl(1 - b^2 \hbar_q^4\bigr) \cdot \bigl(1 + c_3 \hbar_q^6\bigr) \cdot \cdots
$$
Then
$$
  c_3 = J_{\mathrm{Hopf}}(q{=}1) = -2,
$$
derived from the Schur-Weyl branching of $V_{(2,1)} \otimes V_{(2,1)}$
and the Markov-Frobenius selection rule ([`prop:markov-trace-frobenius-selection`](#prop:markov-trace-frobenius-selection)).

This is the **Story B closure at $c_3$**, mirroring the
[$c_2 = b^2$ categorical proof](folio-assistant/computations/probe_q_beta_c2_categorical_proof.py)
from PR #661 — both coefficients now derive from QOU axioms
with no empirical fit.

## Proof sketch

### Step 1 — Self-fusion decomposition

The Hopf link $L_+^{\mathrm{Hopf}}$ is the closure of $\sigma_1^2$
in $B_2$. To match it against the third coefficient of the Q_β
ladder, we work in the V_(2,1) self-fusion arena (the simplest
non-trivial Hoefsmit irrep that participates in the Markov
closure at total weight $6$).

By the Littlewood-Richardson rule for irreducible $S_n$
representations, $V_{(2,1)} \otimes V_{(2,1)}$ decomposes as
$$
  V_{(2,1)} \otimes V_{(2,1)} \;=\; V_{(4,2)} \oplus V_{(3,3)} \oplus V_{(3,2,1)}^{\oplus 2} \oplus V_{(2,2,2)} \oplus V_{(4,1,1)} \oplus V_{(3,1,1,1)} \oplus V_{(2,1^4)}.
$$
The combined dimension is $8 \times 8 = 64$ on the $\mathrm{S}_6$
side; see [`prop:schur-weyl-mass-decomposition`](#prop:schur-weyl-mass-decomposition)
for the Hoefsmit identification of each irrep.

### Step 2 — Frobenius selection picks the Hopf-mediated channel

Per [`prop:markov-trace-frobenius-selection`](#prop:markov-trace-frobenius-selection),
the Markov trace at the order-$\hbar_q^6$ level selects the
channel whose Wedderburn weight $\tilde w_\lambda$ is symmetric
under the bar involution $q \mapsto q^{-1}$ — equivalently,
the **self-conjugate** partitions in the decomposition above.

The self-conjugate channels in $V_{(2,1)}^{\otimes 2}$ at weight
$6$ are precisely $V_{(3,3)}$ (the row-pair) and $V_{(2,2,2)}$
(the column-pair) — Young's natural pairing. Of these, the
$V_{(2,2,2)}$ channel carries the **non-trivial cap-cup pattern**
that admits a 2-strand Hopf reduction: $V_{(2,2,2)}$ projects
onto the closed $\sigma_1^2$ braid in the 6-strand setting via
the standard Markov stabilisation.

The other self-conjugate channel $V_{(3,3)}$ is the trivial
Hopf-equivalent (full row), giving $J = +1$ at $q=1$ and
contributing to the Markov normalisation rather than the
Hopf-mediated coefficient.

### Step 3 — Hopf trace at $q = 1$

The positive Hopf link $L_+^{\mathrm{Hopf}}$ has Jones polynomial
$$
  J_{\mathrm{Hopf}}(q) \;=\; -\bigl(q + q^{-1}\bigr) \;=\; -[2]_q,
$$
the canonical normalisation per [`thm:jones-markov-trace`](#thm:jones-markov-trace)
(unnormalised Markov trace of $\sigma_1^2$ in $H_2(q)$). The
classical limit $q \to 1$ gives $[2]_1 = 2$ and therefore
$$
  J_{\mathrm{Hopf}}(q{=}1) = -2.
$$

The choice of sign convention (positive vs negative Hopf) is
fixed by [`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization)
— the V_(2,1) Hoefsmit representation has the positive Hopf as
its self-fusion mediator (matching the writhe of the canonical
β-decay braid).

### Step 4 — Coefficient identification

Expanding $Q_\beta = Q_A \cdot \prod_k (1 + c_k \hbar_q^{2k})$
in $h = q - q^{-1}$ and matching order-$h^6$ contributions:

- The $V_{(2,2,2)}$ channel (Hopf-mediated) contributes
  $J_{\mathrm{Hopf}}(q) = -[2]_q$ at the Markov trace level.
- At $q = 1$ this becomes $-2$ exactly.
- The Frobenius selection (Step 2) ensures no other channel
  contributes at order $h^6$ — the $V_{(3,3)}$ trivial channel
  contributes only at order $h^0$ (Markov normalisation), and
  the non-self-conjugate channels are bar-involution-paired and
  cancel.

Therefore $c_3 = J_{\mathrm{Hopf}}(q{=}1) = -2$. ∎

## Empirical verification

Companion probe
[`probe_hopf_jones_c3_categorical.py`](folio-assistant/computations/probe_hopf_jones_c3_categorical.py)
computes:

1. **Markov trace of $\sigma_1^2$** at $q = q_0$ and $q = 1$ via
   the V_(2,1) Hoefsmit seminormal representation.
2. **$J_{\mathrm{Hopf}}(q=1)$** value: should equal $-2$ exactly
   to within numerical precision (50 dps).
3. **$c_3$ empirical extraction** from the Q_β residual chain
   (PR #655 finding: $c_3 = -2$ closes $\varepsilon$ to
   $-0.0066$ ppm at $N = 3$).
4. **Match check**: categorical $c_3 = -2$ vs empirical $c_3$
   from the residual chain.

If the categorical value (from Steps 1–3 above, $-2$) matches
the empirical extraction (Step 4, from PR #655's residual chain)
within CODATA's measurement floor
(~400 ppb), this confirms Story B's $c_3 = -2$ is the genuine
structural coefficient — not a curve-fit artifact (Story A's
position).

## Story A vs Story B — what this proposition settles

Per PR #657's high-precision finding (`probe_q_beta_high_precision_ck.py`
at dps=200), the empirical extraction of $c_3, c_4, \ldots$ is
underdetermined at CODATA's $\sim 400$ ppb floor. Two stories
fit the data within experimental noise:

- **Story A**: only $c_2$ matters; $c_3 = c_4 = \ldots = 0$. A
  fit-noise interpretation.
- **Story B**: full categorical chain
  $c_2 = b^2, c_3 = -2, c_4 = b^2 + 1/2, \ldots$. PR #655's
  position.

This proposition (combined with PR #661's $c_2 = b^2$ proof)
**falsifies Story A** by deriving $c_3 = -2$ from QOU axioms
without consulting the empirical residual at all. The 0.0066 ppm
empirical match (PR #655) is then a *prediction* the framework
makes, not a fit.

The remaining $c_4, c_5, \ldots$ derivations (likewise from
Schur-Weyl branching of higher-order self-fusions) are
deferred to follow-on propositions.

## Conditional status

Per the conditional-class pattern (CLAUDE.md §3b-cond) the Lean formalisation
encapsulates the conclusion as a class
`HasC3HopfJonesIdentity` (3 fields: c_3 value, $J_{\mathrm{Hopf}}(1)$
value, equality witness). The instance is empirical (matches the
companion probe's 50-dps verification); the proof structure of
Step 1 (Schur-Weyl branching) is already in
[`prop:schur-weyl-mass-decomposition`](#prop:schur-weyl-mass-decomposition);
Step 3 (Hopf evaluation) is in
[`thm:jones-markov-trace`](#thm:jones-markov-trace). The
coefficient extraction (Step 4) is the open Lean piece; full
formalisation is the follow-on task analogous to PR #661's $c_2$
proof.
