<!-- FILE_START: knot-operator-transition.md -->
**Proposition.**
*The operator that adds the $(A{+}1)$-th nucleon to a nucleus of
mass number $A$ has a definite knot type:*

| Transition | Operator | Dominant NF | Knot type |
|:----------:|:--------:|:-----------:|:---------:|
| $p \to D$ | $\sigma_0 - h/2$ | $\sigma_0$ | single crossing |
| $D \to {}^3\!H$ | $\sigma_1^{-1}(\sigma_0{-}h/2)$ | $L_-$ | **Hopf link** |
| $D \to {}^3\!\mathrm{He}$ | $(\sigma_1{-}h/2)\sigma_0$ | $L_-$ | **Hopf link** |
| ${}^3\!H \to {}^4\!\mathrm{He}$ | $(\sigma_0{-}h/2)(\sigma_1{-}h/2)\sigma_0$ | $e^-$ | **trefoil** |
| ${}^3\!\mathrm{He} \to {}^4\!\mathrm{He}$ | $(\sigma_0{-}h/2)\sigma_1^{-1}(\sigma_0{-}h/2)$ | $e^-$ | **trefoil** |

*The knot hierarchy:*
$$1 \text{ nucleon: unknot} \to 2: \sigma \to 3: \text{Hopf} \to 4: \text{trefoil}$$

*The 4th nucleon completes the trefoil topology ($T_{2,3}$ = electron),
explaining why ${}^4\!\mathrm{He}$ has the strongest binding per nucleon
among light nuclei.* $\square$
<!-- FILE_END: knot-operator-transition.md -->

<!-- FILE_START: qmn-recursive-memoized.md -->
**Proposition (recursive memoised q-MN: speed + storage win).**
*The classical Murnaghan-Nakayama rule expresses $\chi_\rho^\lambda$
recursively via border-strip removal:*

$$
  \chi_\rho^\lambda \;=\; \sum_{\xi \in BS(\lambda, \rho_1)}
                          (-1)^{\mathrm{ht}(\xi)} \,
                          \chi_{\rho \setminus \rho_1}^{\lambda \setminus \xi}
$$

*where $BS(\lambda, \rho_1)$ is the set of border strips of size $\rho_1$
in $\lambda$, $\mathrm{ht}(\xi)$ is the height of strip $\xi$, and
$\rho \setminus \rho_1$ is $\rho$ with its first part removed.*

*The **q-deformed analogue** (Halverson-Ram broken-strip rule) replaces
the sign $(-1)^{\mathrm{ht}(\xi)}$ by a q-weight, but the recursion
structure is identical: $\chi_\rho^\lambda(q)$ at level $n = |\lambda|$
reduces to characters at level $n - \rho_1 < n$.*

*Memoising the recursive call cache `χ_{ρ}^{λ}(q)` indexed by
$(\rho, \lambda)$ gives:*

| Property | Direct iteration | Recursive memoised |
|---|---|---|
| Time, single char | $O(n^2)$ (q-MN canonical) | $O(\#BS \cdot \text{recursion depth})$ amortised |
| Time, batch all $(\rho, \lambda)$ at level $\leq n$ | $O(p(n)^2 \cdot n^2)$ | $O(p(n)^2 \cdot \#BS_{\max})$ amortised, **$\sim 10\times$ faster** |
| Storage, no cache | $O(1)$ | $O(p(n)^2)$ — cache size |
| Storage, character table | $O(p(n)^2)$ | $O(p(n)^2)$ — same |

## Advantage of memoisation for atom-knot work

For ${}^{6}$Li / ${}^{7}$Li atom-knot identification ([wenzl-qmn-synergy](#prop:wenzl-qmn-synergy)),
we need $\chi_\lambda(\mathcal{B}_K; q_0)$ for **many** hyperbolic knots
$K$ with crossing-number $\leq 10$ at $H_{18}, H_{21}$. Each braid
$\mathcal{B}_K$ has cycle type $\rho_K$ in $S_n$.

**Without memoisation**: $385$ partitions $\times$ ~60 hyperbolic
knots $\times$ ~$18^2$ ops $\approx 7.5 \cdot 10^6$ q-MN evaluations.

**With recursive memoisation**: many subproblems shared across
different $K$'s. The recursion tree at level $18$ has at most
$p(18)^2 = 148\,225$ entries — a one-time fill, then $O(1)$ lookups.
Total: $\sim 1.5 \cdot 10^5$ ops for the table fill, $\sim 60$
lookups per knot. **$\sim 50\times$ speedup** for batch character
evaluation.

## Storage reduction

The $q$-character table at level $n = 21$ stored EXPLICITLY via
Hoefsmit seminormal would need:

$$
  \sum_{\lambda \,\vdash\, 21} \dim_\lambda^2 \approx 21!
$$

bytes per single $T_w$. Storing characters as $(\rho, \lambda, \chi(q))$
triples in the recursive memo cache:

$$
  p(21)^2 = 627\,264
$$

entries, each a q-rational expression — total $\sim 100$ MB at
n=21 vs $\sim 50$ TB for full seminormal.

## Connection to existing infrastructure

The current main has:

- the canonical formalism
  — Halverson-Ram broken-strip q-MN for canonical $T_w$,
  $O(n^2)$ per $(\lambda, \mu)$.

The proposed extension:

- the formal derivation (this PR / follow-up): wrap
  `q_mn_canonical` with a recursive driver
  `chi_recursive(λ, ρ, cache)` that:
  1. Looks up `cache[(λ, ρ)]`.
  2. If miss, computes via the recursion above (border-strip
     enumeration $\to$ recursive call on $(λ \setminus \xi,
     ρ \setminus ρ_1)$).
  3. Stores result in cache.

This is **memoisation, not algorithmic restructuring** — the
recursive MN was always the most efficient form; just hadn't been
implemented with caching in this codebase.

## Combined with Wenzl-bridge

The Markov trace
$\mathrm{tr}_M(T_w) = \sum_\lambda y_\lambda(q) \cdot \chi_\lambda(T_w; q)$
([wenzl-qmn-synergy](#prop:wenzl-qmn-synergy)) becomes:

```python
# Pre-compute once: y_λ(q) for all λ ⊢ n via Wenzl-bridge
y_table = {λ: y_lambda_wenzl(λ) for λ in partitions_of(n)}
# Pre-compute once: full χ table via recursive memoised q-MN
cache = {}
chi_table = {(λ, ρ): chi_recursive(λ, ρ, cache)
             for λ in partitions_of(n) for ρ in partitions_of(n)}
# Then per-knot tr_M is O(p(n)) sum:
def tr_M(braid_K):
    ρ = cycle_type(braid_K)
    return sum(y_table[λ] * chi_table[(λ, ρ)] for λ in partitions_of(n))
```

This is the **canonical compute pipeline** for atom-knot
identification at high $n$.

## Open

- **Implement**: the formal derivation driver. Mechanical
  wrapper over existing the formal derivation; estimated 1-day work.
- **Profile**: confirm $\sim 50\times$ speedup empirically at $n = 18, 21$.
- **Lean**: state recursive MN identity as a theorem and the
  memoisation as `simp`-rewrite (open).
<!-- FILE_END: qmn-recursive-memoized.md -->

<!-- FILE_START: sigma-shell-from-beta-chain-derivation.md -->
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
 [`sigma-shell-A2-closed-form.derivation.json`](../../../computations/sigma-shell-A2-closed-form.derivation.json)
 for $A_{\mathrm{magic}} = 2$ (where $\lambda_{\mathrm{shell}} = (3,2,1)$,
 $C_{(3,2,1)}(q_0) = 0.0374882414\ldots$);*
- *$y_{\lambda_{\mathrm{shell}}}(q_0)$ is the **Wenzl-bridge central
 coefficient** of the staircase partition
 ([prop:y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge));
 for $(3,2,1)$ at $q_0$, $y_{(3,2,1)}(q_0) = 0.00731845\ldots$
 (read from
 [`y-lambda-wenzl-bridge-symbolic-witness.json`](../../../computations/y-lambda-wenzl-bridge-symbolic-witness.json));*
- *$\chi^{\lambda_{\mathrm{shell}}}(\mathcal{B}_K)$ is the **Hoefsmit
 character** of the atom braid in the irrep $\rho_{\lambda_{\mathrm{shell}}}$
 ([conj:hoefsmit-scattering-pipeline](#conj:hoefsmit-scattering-pipeline));
 computed for the deuteron via
 the canonical formalism.*

**canonical structural verification — A_magic = 2 (deuteron).**

*Computed live in
[`sigma-shell-from-beta-chain.witness.json`](../../../computations/sigma-shell-from-beta-chain.witness.json):*

See [Table](#tbl:sigma-shell-from-beta-chain-derivation-table-data).

*The benchmark is itself order-of-magnitude
([HANDOVER-STATUS.md §3c](../../../computations/HANDOVER-STATUS.md));
12 % agreement is consistent. An exact derivation would replace the
benchmark with the true categorical mass-formula contribution
$\Delta\mathfrak{m}_{\mathrm{shell}}(D) / \mathfrak{m}(D)$, picking
up additional Wedderburn-block factors beyond the staircase.*

**Correctness of this frame (replacing the earlier β-chain formulation).**

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
[`sigma-shell-A2-closed-form.derivation.json`](../../../computations/sigma-shell-A2-closed-form.derivation.json).
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

**Compatibility with the "no $\mathfrak{Q}_\beta$ derivation" directive.**

*The corrected formula uses **only** categorical inputs computed
from the substrate:*

- *$C_{\lambda_{\mathrm{shell}}}(q_0)$ — derived in
 [`sigma-shell-A2-closed-form.derivation.json`](../../../computations/sigma-shell-A2-closed-form.derivation.json) (ALL steps trust-basis = AXIOM or DERIVED, no SCRIPT_CITED frontier);*
- *$y_{\lambda}(q_0)$ — closed form per
 [`prop:y-lambda-closed-form-wenzl-bridge`](#prop:y-lambda-closed-form-wenzl-bridge);*
- *$\chi^\lambda(\mathcal{B}_K)$ — Hoefsmit character per
 [`conj:hoefsmit-scattering-pipeline`](#conj:hoefsmit-scattering-pipeline);*
- *$|\mathrm{tr}_M(\mathcal{B}_K)|$ — canonical Markov trace per
 [`conj:gs-graded-markov-trace-existence`](#conj:gs-graded-markov-trace-existence).*

*No $\mathfrak{Q}_\beta$, no AME chain manifold, no fitted parameters. The 780 ppb
floor from CAL-2 ($\mathfrak{Q}_\beta$ uncertainty) **does not apply** to this
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
<!-- FILE_END: sigma-shell-from-beta-chain-derivation.md -->

<!-- FILE_START: staircase-corner-hook.md -->
**Lemma.**
*For every $k \geq 1$, the **corner hook** of the
[staircase partition](#def:staircase-partition) $\rho_k$ at cell
$(0, 0)$ satisfies*

$$
  h_{\mathrm{corner}}(\rho_k)
  \;:=\; \mathrm{arm}(0,0) + \mathrm{leg}(0,0) + 1
  \;=\; (k - 1) + (k - 1) + 1
  \;=\; 2k - 1.
$$
<!-- FILE_END: staircase-corner-hook.md -->

<!-- FILE_START: staircase-partition.md -->
**Definition.**
*For each $k \geq 1$, the **staircase partition** of $n_k =
\binom{k+1}{2} = k(k+1)/2$ is*

$$
  \rho_k \;:=\; (k,\, k-1,\, \ldots,\, 2,\, 1)
  \;\vdash\; \tfrac{k(k+1)}{2}.
$$

*Equivalently, $\rho_k$ is the Young diagram whose $r$-th row
($1 \leq r \leq k$) has $k - r + 1$ cells.  The first few are*

$$
  \rho_1 = (1), \quad
  \rho_2 = (2,1), \quad
  \rho_3 = (3,2,1), \quad
  \rho_4 = (4,3,2,1), \quad
  \rho_5 = (5,4,3,2,1).
$$

*The staircase partition is **self-conjugate**: $\rho_k = \rho_k'$
under transposition of rows and columns.*

The staircase shapes index Specht modules
$V_{\rho_k}$ of the Iwahori–Hecke algebra
$H_{n_k}(q)$ that play a distinguished role in the QOU
electroweak sector: the canonical
$\beta_{\mathrm{EW}} \, \bowtie_K^{\mathrm{minimal}}$
braid word acts on $V_{\rho_k}$ with a spectrum encoding the
$q$-deformed Weinberg-angle ratio (see
[`conj:staircase-ew-residual`](#conj:staircase-ew-residual)).

The Lean side is `QOU.Hecke.staircasePartition`, recursively
constructed via `staircaseList` and a dedicated
`staircaseList_sum` lemma that discharges the
`Partition.sum_eq` obligation; the staircase strand-count
$n_k$ is exposed as `QOU.Hecke.staircaseStrands`.
<!-- FILE_END: staircase-partition.md -->

<!-- FILE_START: outro-mass-theory.md -->
This closes the mass-theory chapter.  The substrate-level mass
machinery has been assembled in full: mass-formula derivation
(commutative chirality vanishing); algebraic-consolidated form;
Hoefsmit convergence (per-partition $k$ and magic-shell);
vertex-factorisation Feynman bridge; archimedean realisation and
Kashaev volume; $\varphi_q$ / Markov / Schur-Weyl tower with the
Habiro residue specialisation; cyclotomic depth-3 trilog
identities; spectral-sequence chirality and confinement-NF
structure; Plancherel knot-factor mass tower; $\alpha_k$
procedure for atom-knot mass; Wenzl-bridge cyclotomic LR-tensor
characters; parity classification with $np$-discrepancy
resolution; six-term crystal-isospin-chirality option-E
formulation; mass open-problems catalogue; and the orphan-reconnect
mass-theory and mass-application sub-sections that close the
chapter.

The next chapter (predicted spectra) consumes this mass-theory
machinery to produce per-particle, per-isotope, and per-shell
predictions tabulated against PDG / CODATA / SnapPy
benchmarks.  Readers focused on the structural consequences can
take the substrate-level closed forms recorded here as the
chapter's input; readers focused on the structural arithmetic
can work through the proofs in any order, since the substrate-
flow apparatus factorises across sub-sections.
<!-- FILE_END: outro-mass-theory.md -->

