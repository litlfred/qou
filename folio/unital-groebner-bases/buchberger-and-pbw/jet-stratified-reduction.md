Let $R$ be a commutative ring with unity, $A$ an $R$-algebra
with [admissible system](#def:admissible-system) $(B, <)$, and
$\{A_n\}_{n \geq 0}$ a jet tower with
$A_{n+1} = A_n \otimes \Omega^1(A_n)$.  At each level, the jet
prolongation introduces $k$ new generators (the Kähler
directions).  Let $\Sigma_n$ be the defining relations of $A_n$
and suppose $\Sigma_n$ is a
[Gröbner--Shirshov basis](#def:groebner-basis) for the ideal
it generates.

The **jet-stratified reduction algorithm** exploits two
structural features of the jet tower to reduce the cost of
verifying and applying the GS basis at level $n+1$:

1. **Descended/transient splitting.** The descent involution
   $\hat{\tau}_n$ classifies each relation in $\Sigma_{n+1}$ as
   *descended* (inherited from level $n$) or *transient* (new at
   level $n+1$).  Descended $S$-polynomials are already resolved.

2. **Degree bucketing.** The deg-lex order compares by word
   length first.  A monomial of degree $d$ can only be reduced
   by a rule whose leading monomial has degree $\leq d$.

---

## Algorithm 1: Jet-Stratified GS Verification

**Input:** Rewriting system $\Sigma_{n+1}$ at level $n+1$,
partitioned as $\Sigma_{n+1} = \Sigma_n^{\mathrm{desc}} \cup
\Sigma_{n+1}^{\mathrm{trans}}$; proof that $\Sigma_n$ is a GS
basis.

**Output:** Decision whether $\Sigma_{n+1}$ is a GS basis.

1. **Inherit.** Accept all $\binom{|\Sigma_n|}{2}$ descended
   $\times$ descended $S$-polynomial pairs as resolved (by the
   level-$n$ GS property).

2. **For each** pair $(g_i, g_j)$ with at least one rule
   transient:

   a. Compute the overlap compositions $S(g_i, g_j)$.

   b. Reduce $S(g_i, g_j)$ to normal form using the
      [division algorithm](#def:division-algorithm) applied to
      $\Sigma_{n+1}$ (full system).

   c. **If** the remainder is nonzero, **return** "not a GS
      basis".

3. **Return** "$\Sigma_{n+1}$ is a GS basis".

**Pair count.** Let $m = |\Sigma_n^{\mathrm{desc}}|$ and
$k = |\Sigma_{n+1}^{\mathrm{trans}}|$.  Step 2 processes
$m \cdot k + \binom{k}{2}$ pairs (excluding self-compositions).
The savings over naive Buchberger are $\binom{m}{2}$ skipped
pairs.

---

## Algorithm 2: Degree-Bucketed Division

**Input:** Element $f \in A_{n+1}$, GS basis $\Sigma_{n+1}$
partitioned into degree buckets $B_0, B_1, B_2, \ldots$ where
$B_d$ contains rules whose leading monomial has degree $d$.

**Output:** Normal form $\mathrm{NF}(f)$.

1. Set $r := 0$, $h := f$.
2. **While** $h \neq 0$:

   a. Let $d := \deg(\mathrm{LM}(h))$.

   b. Scan only buckets $B_0, B_1, \ldots, B_d$ for a rule $g$
      with $\mathrm{LM}(g) \mid \mathrm{LM}(h)$.

   c. **If** no such $g$ exists: set
      $r := r + \mathrm{LT}(h)$, $h := h - \mathrm{LT}(h)$.

   d. **Else**: choose $g \in B_{\leq d}$ with
      $\mathrm{LM}(g) \mid \mathrm{LM}(h)$; choose
      $\lambda \in R^*$, $u, v \in B$ with
      $\lambda\,\mathrm{LT}(u \cdot g \cdot v) = \mathrm{LT}(h)$;
      set $h := h - \lambda\, u \cdot g \cdot v$.

3. **Return** $r$.

**Per-step cost.** At degree $d$, the scan in step 2b examines
$|B_{\leq d}|$ rules instead of $|\Sigma_{n+1}|$.  For the
Hecke algebra, $|B_2| = O(n)$ (Hecke + far-commutativity) and
$|B_3| = O(n)$ (Yang--Baxter), so most reductions scan $O(n)$
rules instead of $O(n^2)$.

---

## Algorithm 3: Combined Jet-Stratified + Degree-Bucketed Reduction

**Input:** Element $f \in A_{n+1}$; jet-stratified system
$(\Sigma_n^{\mathrm{desc}}, \Sigma_{n+1}^{\mathrm{trans}})$;
degree buckets $B_0, \ldots, B_D$; normal-form cache
$\mathsf{C}$ from level $n$.

**Output:** Normal form $\mathrm{NF}(f)$.

1. **Decompose.**  Write $f = f^{\mathrm{desc}} +
   f^{\mathrm{trans}}$ where $f^{\mathrm{desc}}$ contains only
   descended monomials and $f^{\mathrm{trans}}$ contains at least
   one transient generator per monomial.

2. **Cache lookup.**  For each descended monomial $m$ in
   $f^{\mathrm{desc}}$:

   a. **If** $m \in \mathsf{C}$: replace $m$ by
      $\mathsf{C}[m]$.

   b. **Else**: reduce $m$ using degree-bucketed division
      (Algorithm 2) restricted to $\Sigma_n^{\mathrm{desc}}$;
      store result in $\mathsf{C}$.

3. **Reduce transient part.**  Apply degree-bucketed division
   (Algorithm 2) to $f^{\mathrm{trans}}$ using the full system
   $\Sigma_{n+1}$.

4. **Combine.**  Set $h := \mathsf{C}[f^{\mathrm{desc}}] +
   \mathrm{NF}(f^{\mathrm{trans}})$.

5. **Final pass.**  Apply degree-bucketed division to $h$ using
   $\Sigma_{n+1}$ (cross-terms between descended and transient
   parts may create new reducible monomials).

6. **Return** $\mathrm{NF}(h)$.

**Correctness.**  By the composition lemma
([Buchberger's theorem](#thm:buchberger)), the normal form is
unique.  Each sub-step computes a partial normal form; the
final pass resolves cross-terms.  The cache is valid because
the descended subsystem's normal forms are stable under
extension by transient rules (the leading monomials of transient
rules involve new generators that cannot appear in descended
monomials).

---

## Complexity summary

| | Naive Buchberger | Jet-stratified |
|---|---|---|
| **GS verification** (S-poly pairs) | $\binom{m+k}{2} \approx O((m+k)^2)$ | $mk + \binom{k}{2} \approx O(mk + k^2)$ |
| **Per-reduction scan** | $O(m + k)$ rules | $O(|B_{\leq d}|)$ rules |
| **Normal-form cache** | None | $O(m)$ cache hits per element |

For $\mathrm{SU}(2)$ at level $n$: $m \sim 3n$, $k = O(1)$.

| | Naive | Jet-stratified |
|---|---|---|
| S-poly pairs per level | $O(n^2)$ | $O(n)$ |
| Per-step rule scan | $O(n^2)$ | $O(n)$ |
| **Total per level** | $O(n^4)$ | $O(n^2)$ |
| **Cumulative through level $N$** | $O(N^5)$ | $O(N^3)$ |

---

## Empirical benchmark

<!-- literal-source: parameter specialization q = 1.1097 for empirical pair-count benchmark -->
The Hecke algebra $H_n(q)$ at $q = 1.1097$, starting from
$H_3(q)$ (3 generators) and adding 3 generators per jet level.
The rule count includes Hecke ($n$), Yang--Baxter ($\sim n$), and
far-commutativity ($\sim n^2$) relations.

| Level | Gens | Rules | Naive pairs | Strat pairs | Skipped | Speedup |
|-------|------|-------|-------------|-------------|---------|---------|
| 1 | 6 | 21 | 210 | 195 | 15 | 1.1$\times$ |
| 3 | 12 | 78 | 3,003 | 2,013 | 990 | 1.5$\times$ |
| 6 | 21 | 231 | 26,565 | 12,030 | 14,535 | 2.2$\times$ |
| 9 | 30 | 465 | 107,880 | 36,627 | 71,253 | 3.0$\times$ |
| 12 | 39 | 780 | 303,810 | 82,365 | 221,445 | 3.7$\times$ |

Pair counts exclude self-compositions ($i < j$ only, matching
$\binom{m}{2}$ convention).  Scaling exponents (fitted):
naive pairs $\sim n^{3.95}$, stratified pairs $\sim n^{3.08}$.
The pair-count speedup ratio grows linearly with level
($\approx 0.3 \cdot \text{level}$).  Wall-clock speedup at
level 12: $3.5\times$.

Caveat: these timings are generated by
`jet-stratified-benchmark.py`, which performs a proxy reduction
(monomial rewriting with first RHS term, not full S-polynomial
reduction over linear combinations).  The reported wall-clock
speedups should be read as indicative of pair-screening and
reduction-structure savings rather than as faithful GS verification
runtimes.

Witness: `computations/jet-stratified-benchmark.witness.json`.
