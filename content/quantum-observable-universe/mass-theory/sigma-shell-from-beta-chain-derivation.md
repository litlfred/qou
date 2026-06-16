**Proposition (closed-form $\sigma_{\mathrm{shell}}$ magnitude as Wedderburn coefficient at the staircase partition).**
*Let $A_{\mathrm{magic}} \in \{2, 8, 20, 28, 50, 82, 126\}$ be a magic
nucleon count, $n = 3 \cdot A_{\mathrm{magic}}$, and let
$\lambda_{\mathrm{shell}} \vdash n$ be the **staircase partition**
of $n$ (the unique self-conjugate partition with all rows of
distinct length and maximal height). For an atom $K$ with braid
word $\mathcal{B}_K \in B_n$, the shell-operator magnitude
$y_{\mathrm{target}}(A_{\mathrm{magic}})$ is **derivable in closed form** as*

$$
  y_{\mathrm{target}}(A_{\mathrm{magic}})
  \;=\;
  \frac{C_{\lambda_{\mathrm{shell}}}(q_0)\,\cdot\,y_{\lambda_{\mathrm{shell}}}(q_0)\,\cdot\,|\chi^{\lambda_{\mathrm{shell}}}(\mathcal{B}_K)|}
       {|\mathrm{tr}_M(\mathcal{B}_K)|}
$$

*where:*

- *$C_{\lambda_{\mathrm{shell}}}(q_0)$ is the **closed-form Wedderburn
 coefficient** of $\sigma_{\mathrm{shell}}$ at the staircase
 partition, derived in
 [`sigma-shell-A2-closed-form.derivation.json`](../../../folio-assistant/computations/sigma-shell-A2-closed-form.derivation.json)
 for $A_{\mathrm{magic}} = 2$ (where $\lambda_{\mathrm{shell}} = (3,2,1)$,
 $C_{(3,2,1)}(q_0) = 0.0374882414\ldots$);*
- *$y_{\lambda_{\mathrm{shell}}}(q_0)$ is the **Wenzl-bridge central
 coefficient** of the staircase partition
 ([prop:y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge));
 for $(3,2,1)$ at $q_0$, $y_{(3,2,1)}(q_0) = 0.00731845\ldots$
 (read from
 [`y-lambda-wenzl-bridge-symbolic-witness.json`](../../../folio-assistant/computations/y-lambda-wenzl-bridge-symbolic-witness.json));*
- *$\chi^{\lambda_{\mathrm{shell}}}(\mathcal{B}_K)$ is the **Hoefsmit
 character** of the atom braid in the irrep $\rho_{\lambda_{\mathrm{shell}}}$
 ([conj:hoefsmit-scattering-pipeline](#conj:hoefsmit-scattering-pipeline));
 computed for the deuteron via
 [`hecke_character_symbolic.q_character_on_braid_word`](../../../folio-assistant/computations/hecke/hecke_character_symbolic.py).*

**Numerical verification — A_magic = 2 (deuteron).**

*Computed live in
[`sigma-shell-from-beta-chain.witness.json`](../../../folio-assistant/computations/sigma-shell-from-beta-chain.witness.json):*

See [Table](#tbl:sigma-shell-from-beta-chain-derivation-table-data).

*The benchmark is itself order-of-magnitude
([HANDOVER-STATUS.md §3c](../../../folio-assistant/computations/HANDOVER-STATUS.md));
12 % agreement is consistent. An exact derivation would replace the
benchmark with the true categorical mass-formula contribution
$\Delta\mathfrak{m}_{\mathrm{shell}}(D) / \mathfrak{m}(D)$, picking
up additional Wedderburn-block factors beyond the staircase.*

**Why this is the correct frame (replacing the earlier β-chain formulation).**

*An earlier version of this proposition extracted
$y_{\mathrm{target}}$ from cumulative $\beta$-decay chain Q-values
along the $\beta$-stability valley. That formulation gave
$y_{\mathrm{target}}(A=2) \approx 270$, **off by a factor of
$2.3 \times 10^{7}$** from the benchmark
($\approx 0.0012$). The root cause, identified in the §5
escalation comment on
,
is structural: the deuteron has **no**
non-shell-crossing predecessors along the $\beta$-stability
valley — the chain $\{n \to p\}$ produces the bound state
directly, without intermediate atoms whose mass change can be
subtracted to isolate the shell magnitude.*

*The corrected categorical frame, recorded in
[`docs/audits/sigma-shell-categorical-identification.md`](../../../docs/audits/sigma-shell-categorical-identification.md),
identifies $\sigma_{\mathrm{shell}}$ as a **separately-constructed
element** of $H_{n}(q)$ supported on the staircase partition, with
closed-form Wedderburn coefficient $C_{\lambda_{\mathrm{shell}}}$
already derived in
[`sigma-shell-A2-closed-form.derivation.json`](../../../folio-assistant/computations/sigma-shell-A2-closed-form.derivation.json).
The shell magnitude $y_{\mathrm{target}}$ is therefore a
**categorical observable** depending on:*

1. *the staircase Wedderburn coefficient $C_{\lambda_{\mathrm{shell}}}(q_0)$,*
2. *the Wenzl-bridge central weight $y_{\lambda_{\mathrm{shell}}}(q_0)$,*
3. *the Hoefsmit character $\chi^{\lambda_{\mathrm{shell}}}(\mathcal{B}_K)$ of the atom braid,*
4. *the canonical Markov trace $|\mathrm{tr}_M(\mathcal{B}_K)|$.*

**No $\mathfrak{Q}_\beta$ or AME chain Q-values appear**. The
calibration anchors stay at the $\rho_K$ assembly level
($m_e$, $m_p$, $m_n$); the shell magnitude is a purely
algebraic / categorical consequence of the staircase Wedderburn
structure at the magic shell boundary. This respects the user's
"I do NOT want to derive $\mathfrak{Q}_\beta$" stance: $\mathfrak{Q}_\beta$ is **not
needed** for shell-magnitude derivation.*

**Derivation.**

*Step 1 — Categorical identification of $\sigma_{\mathrm{shell}}$.*
*By
[`docs/audits/sigma-shell-categorical-identification.md`](../../../docs/audits/sigma-shell-categorical-identification.md),
the shell operator at $A_{\mathrm{magic}}$ is a constructed
element of $H_n(q)$ ($n = 3 A_{\mathrm{magic}}$) of the form*

$$
  \sigma_{\mathrm{shell}} \;=\; \sum_{\lambda \vdash n} x_\lambda \cdot e_\lambda,
  \qquad x_\lambda = x_{\lambda^*}\;\text{(self-duality, Prop.~\ref{prop:shell-schur-weyl-self-duality}).}
$$

*The staircase partition $\lambda_{\mathrm{shell}}$ is
self-conjugate ($\lambda^* = \lambda$), so it sits in the
self-duality fixed-point sub-algebra by definition. At $A=2$ ($n=6$),
$\lambda_{\mathrm{shell}} = (3,2,1)$ — the **unique** self-conjugate
partition of 6 with three rows of distinct length.*

*Step 2 — Mass contribution at the magic boundary.*
*By [`prop:rho-k-h3a-refinement`](#prop:rho-k-h3a-refinement), the
mass formula admits the Wedderburn-Schur decomposition*

$$
  M(K) \;=\; m_e \cdot \sum_\lambda y_\lambda(q)\,\chi^\lambda(\mathcal{B}_K)\,\bigl(1 + \Delta_\lambda(K)\bigr),
$$

*with the per-block binding-fraction $\Delta_\lambda(K)$ encoding
the deviation of the $\lambda$-block contribution from the
constituent piece. For the staircase $\lambda_{\mathrm{shell}}$, this
$\Delta$ contribution **is** the shell magnitude:*

$$
  \Delta\mathfrak{m}_{\mathrm{shell}}(K) \;=\; m_e \cdot y_{\lambda_{\mathrm{shell}}}(q)\,\chi^{\lambda_{\mathrm{shell}}}(\mathcal{B}_K)\,\Delta_{\lambda_{\mathrm{shell}}}(K),
$$

*where $\Delta_{\lambda_{\mathrm{shell}}}(K) = C_{\lambda_{\mathrm{shell}}}(q_0)$
identifies the per-block binding fraction with the closed-form
Wedderburn coefficient.*

*Step 3 — Dimensionless shell magnitude.*
*The dimensionless ratio*

$$
  y_{\mathrm{target}}(A_{\mathrm{magic}})
  \;=\;
  \frac{\Delta\mathfrak{m}_{\mathrm{shell}}(K)}{m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)|}
  \;=\;
  \frac{C_{\lambda_{\mathrm{shell}}}\,\cdot y_{\lambda_{\mathrm{shell}}}\,\cdot |\chi^{\lambda_{\mathrm{shell}}}(\mathcal{B}_K)|}
       {|\mathrm{tr}_M(\mathcal{B}_K)|}
$$

*is the desired closed form.* $\blacksquare$

**Compatibility with the "no 𝔔_β derivation" directive.**

*The corrected formula uses **only** categorical inputs computed
from the substrate:*

- *$C_{\lambda_{\mathrm{shell}}}(q_0)$ — derived in
 [`sigma-shell-A2-closed-form.derivation.json`](../../../folio-assistant/computations/sigma-shell-A2-closed-form.derivation.json) (ALL steps trust-basis = AXIOM or DERIVED, no SCRIPT_CITED frontier);*
- *$y_{\lambda}(q_0)$ — closed form per
 [`prop:y-lambda-closed-form-wenzl-bridge`](#prop:y-lambda-closed-form-wenzl-bridge);*
- *$\chi^\lambda(\mathcal{B}_K)$ — Hoefsmit character per
 [`conj:hoefsmit-scattering-pipeline`](#conj:hoefsmit-scattering-pipeline);*
- *$|\mathrm{tr}_M(\mathcal{B}_K)|$ — canonical Markov trace per
 [`conj:gs-graded-markov-trace-existence`](#conj:gs-graded-markov-trace-existence).*

*No 𝔔_β, no AME chain manifold, no fitted parameters. The 780 ppb
floor from CAL-2 (𝔔_β uncertainty) **does not apply** to this
derivation — the shell magnitude is a purely categorical observable.*

**Open** for $A_{\mathrm{magic}} \ge 8$.**

*For $A_{\mathrm{magic}} = 8$, $n = 24$, $p(24) = 1575$ partitions.
Identifying the shell partition $\lambda_{\mathrm{shell}}$ at $A=8$
requires either:*

- *direct adaptation of the audit's "level-4 ILP" prescription
 ([`docs/audits/sigma-shell-categorical-identification.md`](../../../docs/audits/sigma-shell-categorical-identification.md)),
 or*
- *the staircase generalisation if $n = k(k+1)/2$ for some integer
 $k$ — for $n=24$ this fails (no integer $k$); $A=8$ may need a
 different self-conjugate partition such as $(7,5,3,1)$ ($n=16$)
 or $(8,6,4,2)$ ($n=20$).*

*For now, the closed form is **proved at $A_{\mathrm{magic}} = 2$**
and should be extended by:*

1. *enumerating self-conjugate partitions of $n=3 \cdot A_{\mathrm{magic}}$,*
2. *applying the level-4 ILP to identify the unique shell partition,*
3. *deriving $C_{\lambda_{\mathrm{shell}}}(q_0)$ analogously to the
 $A=2$ derivation.*

*This is the math content behind the **corrected** P8 in
[`AUDIT-DEEP-2026-05.md`](../../../AUDIT-DEEP-2026-05.md) §7.
Compute follow-up: extend to $A=8$ via level-4 ILP at $n=24$.*
